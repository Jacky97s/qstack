#!/usr/bin/env python3
"""qstack PreToolUse guard for Claude Code.

Denies new fixed sleeps and reasonless skips written into test files, and asks
before Bash commands that mutate protected hosts or run irreversible device
operations. Prints one decision object, or nothing to leave the call alone.
Fails open: any internal error leaves the normal permission flow in charge.
"""
import json
import os
import re
import sys
from collections import Counter

TEST_PATH = re.compile(
    r"(^|/)(tests?|__tests__|e2e|specs?|cypress|playwright|integration[-_]tests?)/"
    r"|(^|/)test_[^/]*\.py$|_test\.(py|go|rs|c|cpp)$"
    r"|\.(spec|test)\.[cm]?[jt]sx?$|(Test|Tests|IT)\.(java|kt|cs|swift)$"
)
CODE_FILE = re.compile(r"\.(py|[cm]?[jt]sx?|go|rs|java|kt|cs|swift|rb|c|cc|cpp|h|hpp|robot|feature)$")
COMMENT_LINE = re.compile(r"^(#|//|/\*|\*|--|;)")
TRAILING_COMMENT = re.compile(r"\s(#|//)\s.*$")
QUOTED = re.compile(r"\"[^\"]*\"|'[^']*'|`[^`]*`")

SLEEP = [
    re.compile(r"\btime\.sleep\s*\("),
    re.compile(r"(?<![\w.])sleep\s*\(\s*[\d.]"),
    re.compile(r"\basyncio\.sleep\s*\(\s*(?!0*\.?0*\s*\))[\d.]"),
    re.compile(r"\bwait_?for_?timeout\s*\(", re.IGNORECASE),
    re.compile(r"\bThread\.(sleep|Sleep)\s*\("),
    re.compile(r"\bTimeUnit\.\w+\.sleep\s*\("),
    re.compile(r"\btime\.Sleep\s*\("),
    re.compile(r"\bTask\.Delay\s*\(\s*\d"),
    re.compile(r"\bcy\.wait\s*\(\s*\d"),
    re.compile(r"new\s+Promise\s*\(.*setTimeout\s*\(\s*\w+\s*,\s*(?!0\s*\))\d"),
]
SLEEP_OK = "qstack: allow-sleep"

BARE_SKIP = [
    re.compile(r"@pytest\.mark\.skip\s*(\(\s*\))?\s*$"),
    re.compile(r"@unittest\.skip\s*\(\s*\)"),
    re.compile(r"\bpytest\.skip\s*\(\s*\)"),
    re.compile(r"\b(it|test|describe)\.(skip|fixme)\s*\("),
    re.compile(r"(?<![\w.])x(it|describe|test)\s*\("),
    re.compile(r"@(Disabled|Ignore)\s*(\(\s*\))?\s*$"),
    re.compile(r"\bt\.Skip(Now)?\s*\(\s*\)"),
]
# A ticket, issue number, or URL outside string literals, or a reason string as the last argument.
TICKET = re.compile(r"qstack: skip-reason|\b(?!(?:UTF|ISO|SHA|UCS)-)[A-Z][A-Z0-9]+-\d+\b|#\d+\b|https?://\S+")
REASON_ARG = re.compile(r",\s*(['\"`])[^'\"`]+\1\s*\)\s*;?\s*$")

HTTP_MUTATION = re.compile(
    r"(-X|--request)\s*['\"]?(POST|PUT|PATCH|DELETE)\b"
    r"|\s(-d|--data(-raw|-binary|-urlencode)?|-F|--form|-T|--upload-file)(\s|=)"
    r"|\bhttps?\s+(POST|PUT|PATCH|DELETE)\b"
    r"|--method[ =]['\"]?(POST|PUT|PATCH|DELETE)"
    r"|-Method\s+(Post|Put|Patch|Delete)",
    re.IGNORECASE,
)
TEST_RUNNER = re.compile(
    r"\b(pytest|playwright|cypress|newman|k6|locust|jmeter|artillery|robot|behave"
    r"|go\s+test|cargo\s+test|mvn\s+\S*\s*test|gradlew?\s+\S*test|(npm|yarn|pnpm)\s+(run\s+)?test)\b"
)
IRREVERSIBLE = [
    re.compile(r"\bespefuse(\.py)?\b.*\bburn"),
    re.compile(r"\bburn[_-](efuse|key|bit)"),
    re.compile(r"\bfastboot\s+(oem|flashing)\s+lock\b"),
    re.compile(r"\bnrfjprog\b.*--(eraseall|recover)\b"),
    re.compile(r"\bSTM32_Programmer_CLI\b.*(\s-e\s+all\b|--erase\s+all\b|RDP=)"),
    re.compile(r"\bopenocd\b.*\b(mass_erase|lock)\b"),
    re.compile(r"\bpicotool\s+otp\s+(set|load|permissions)\b"),
    re.compile(r"\bdd\b.*\bof=/dev/(sd|disk|mmcblk|nvme)"),
]


def has_skip_reason(line):
    return bool(REASON_ARG.search(line) or TICKET.search(QUOTED.sub("", line)))


def violations(text):
    """Counter of offending stripped lines in the code of a test file."""
    found = Counter()
    for line in text.splitlines():
        s = line.strip()
        if not s or COMMENT_LINE.match(s):
            continue
        code = TRAILING_COMMENT.sub("", s)
        if any(p.search(code) for p in SLEEP) and SLEEP_OK not in s:
            found[("sleep", s)] += 1
        elif any(p.search(code) for p in BARE_SKIP) and not has_skip_reason(s):
            found[("skip", s)] += 1
    return found


def edit_texts(tool, inp):
    path = inp.get("file_path", "")
    if tool == "Write":
        old = ""
        try:
            with open(path, encoding="utf-8") as f:
                old = f.read()
        except OSError:
            pass
        return path, old, inp.get("content", "")
    if tool == "Edit":
        return path, inp.get("old_string", ""), inp.get("new_string", "")
    edits = inp.get("edits", [])
    return (path, "\n".join(e.get("old_string", "") for e in edits),
            "\n".join(e.get("new_string", "") for e in edits))


def find_qstack_file(cwd, name):
    d = os.path.abspath(cwd or os.getcwd())
    while True:
        p = os.path.join(d, ".qstack", name)
        if os.path.isfile(p):
            return p
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def read_lines(path):
    if not path:
        return []
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]


def check_edit(tool, inp):
    path, old, new = edit_texts(tool, inp)
    norm = path.replace("\\", "/")
    if not (TEST_PATH.search(norm) and CODE_FILE.search(norm)):
        return None
    added = violations(new) - violations(old)
    if not added:
        return None
    lines = [f"- {kind}: {line}" for (kind, line) in added]
    return ("deny",
            "qstack guard: this edit adds patterns that make tests untrustworthy.\n"
            + "\n".join(lines) + "\n"
            "Fixed sleep: wait for the condition the assertion needs (web-first assertion, "
            "polling with a deadline, an awaited event). A deliberate exception carries "
            f"`{SLEEP_OK} <reason>` on the same line.\n"
            "Skip: give a reason and a ticket on the same line (for example "
            "`reason=\"PROJ-123 flaky upstream\"`), or `qstack: skip-reason <why>`.")


def project_pattern(line):
    # A typo in one line must not disable the rest of the guard, so fall back to a literal match.
    try:
        return re.compile(line)
    except re.error as e:
        print(f"qstack guard: protected-commands line {line!r} is not a valid regex ({e}); "
              "matching it literally", file=sys.stderr)
        return re.compile(re.escape(line))


def check_bash(inp, cwd):
    cmd = inp.get("command", "")
    hosts = read_lines(find_qstack_file(cwd, "protected-hosts"))
    low = cmd.lower()
    hit = [h for h in hosts if h.lower() in low]
    if hit and (HTTP_MUTATION.search(cmd) or TEST_RUNNER.search(cmd)):
        return ("ask",
                f"qstack guard: this command may change state on protected environment(s) "
                f"{', '.join(hit)}. Confirm the operator approved this run and its "
                "destructive operations (principle-protect-shared-environments).")
    patterns = IRREVERSIBLE + [project_pattern(p) for p in
                               read_lines(find_qstack_file(cwd, "protected-commands"))]
    for p in patterns:
        if p.search(cmd):
            return ("ask",
                    "qstack guard: this looks like an irreversible operation "
                    f"(matched `{p.pattern}`). It needs the operator's explicit yes for "
                    "this unit and this run.")
    return None


def main():
    try:
        payload = json.load(sys.stdin)
        tool = payload.get("tool_name", "")
        inp = payload.get("tool_input") or {}
        if tool in ("Write", "Edit", "MultiEdit"):
            decision = check_edit(tool, inp)
        elif tool == "Bash":
            decision = check_bash(inp, payload.get("cwd"))
        else:
            decision = None
    except Exception as e:  # fail open, but say why on stderr
        print(f"qstack guard skipped: {e}", file=sys.stderr)
        return 0
    if decision:
        kind, reason = decision
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": kind,
            "permissionDecisionReason": reason,
        }}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
