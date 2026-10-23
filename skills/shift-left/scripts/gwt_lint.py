#!/usr/bin/env python3
"""Mechanically validate a stage-6 test-case file against gwt-rules.md.

Usage:
  python3 gwt_lint.py <test-case.md> [--inventory <project>/helpers-inventory.md]
                      [--banned "word,word"] [--verbs "verb,verb"]

Checks the machine-checkable subset of the self-check checklist:
  (1) each When step is a single interaction (no second verb outside quotes)
  (2) each When step starts with an approved verb
  (4) each Then step avoids banned vague words
  (5) each Then step maps to a concrete assertion
  (8) [Helper] labels exist in the inventory (only if --inventory is given)

--banned adds vague words for the team's language. --verbs adds approved verbs.
Judgment items (3, 6, 7, 9, 10) stay with the reviewer, see gwt-rules.md.
Exit code is non-zero if any violation is found.
"""
import re
import sys

APPROVED_VERBS = {"click", "input", "select", "check", "scroll", "wait",
                  "navigate", "request"}
BANNED = ["should", "correct", "works", "as expected", "normally", "properly",
          "fine", "appropriate"]
ASSERTION_TOKENS = ["toHaveText", "toBeVisible", "toBeHidden", "toBeChecked",
                    "toHaveURL", "toHaveCount", "toHaveValue", "toBeEnabled",
                    "toBeDisabled", "toContainText", "toHaveAttribute",
                    "oracle", "status", "==", "json"]
LABEL_RE = re.compile(r"\[(?:Helper|Skill):\s*([^\]]+)\]")
QUOTED_RE = re.compile(r"\"[^\"]*\"|'[^']*'|“[^”]*”|「[^」]*」")


def section(lines, header):
    """Return the lines under '## <header>' up to the next '## ' header."""
    out, capture = [], False
    for ln in lines:
        if re.match(r"^##\s", ln):
            capture = ln.strip().lower().startswith(f"## {header.lower()}")
            continue
        if capture:
            out.append(ln)
    return out


def steps(lines, prefix):
    """Lines like 'W1: ...' / 'T1: ...' (fenced or not)."""
    return [ln.strip() for ln in lines if re.match(rf"^\s*{prefix}\d+\s*:", ln)]


def strip_labels(text):
    return LABEL_RE.sub("", text).strip()


def lint_when(step, verbs):
    body = strip_labels(step.split(":", 1)[1])
    toks = re.findall(r"[A-Za-z]+", QUOTED_RE.sub(" ", body))
    if not toks or toks[0].lower() not in verbs:
        return [f"[2] When not starting with approved verb: {step}"]
    if any(t.lower() in verbs for t in toks[1:]):
        return [f"[1] When looks like multiple interactions: {step}"]
    return []


def lint_then(step, banned):
    body = step.split(":", 1)[1]
    unquoted = QUOTED_RE.sub(" ", body).lower()
    out = []
    for bad in banned:
        b = bad.lower()
        hit = re.search(rf"\b{re.escape(b)}\b", unquoted) if b.isascii() else b in unquoted
        if hit:
            out.append(f"[4] Then uses vague word '{bad}': {step}")
    low = body.lower()
    if not any(tok.lower() in low for tok in ASSERTION_TOKENS) \
            and "→" not in body and "->" not in body:
        out.append(f"[5] Then has no assertion mapping: {step}")
    return out


def arg_list(argv, flag):
    if flag not in argv:
        return []
    return [w.strip() for w in argv[argv.index(flag) + 1].split(",") if w.strip()]


def main(argv):
    if len(argv) < 2 or argv[1].startswith("--"):
        print(__doc__)
        return 2
    path = argv[1]
    verbs = APPROVED_VERBS | {v.lower() for v in arg_list(argv, "--verbs")}
    banned = BANNED + arg_list(argv, "--banned")
    inventory = None
    if "--inventory" in argv:
        inv_path = argv[argv.index("--inventory") + 1]
        try:
            with open(inv_path, encoding="utf-8") as f:
                inventory = set(re.findall(r"^\|\s*([a-z0-9][a-z0-9\-]*)\s*\|",
                                           f.read(), re.MULTILINE))
        except FileNotFoundError:
            print(f"warn: inventory {inv_path} not found, skipping label check")

    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    violations = []
    whens = steps(section(lines, "When"), "W")
    thens = steps(section(lines, "Then"), "T")
    if not whens:
        violations.append("no When steps found (expected 'W1: ...')")
    if not thens:
        violations.append("no Then steps found (expected 'T1: ...')")
    for w in whens:
        violations += lint_when(w, verbs)
    for t in thens:
        violations += lint_then(t, banned)
    if inventory is not None:
        for ln in whens + thens:
            for label in LABEL_RE.findall(ln):
                if label.strip() not in inventory:
                    violations.append(f"[8] unknown [Helper: {label.strip()}]: {ln}")

    if violations:
        print(f"FAIL ({len(violations)} violation(s)) in {path}:")
        for v in violations:
            print("  - " + v)
        return 1
    print(f"OK: {path} ({len(whens)} When, {len(thens)} Then) passes mechanical lint")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
