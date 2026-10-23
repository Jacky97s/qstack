#!/usr/bin/env python3
"""Check a repository's project playbooks against this qstack version.

Run from the repository root: python3 <plugin>/scripts/check_playbooks.py

Project playbooks live in .qstack/playbooks/ or .agents/playbooks/. Each names
`extends` (bundled playbook files) and `when` in its frontmatter. Each change is
a list item starting with **After**, **Before**, **Replace**, or **In** followed
by a quoted run of the bundled step's own words. This fails when a playbook
extends a file this version lacks, or quotes text no extended playbook contains.
"""
import re
import sys
from pathlib import Path

BUNDLED = Path(__file__).resolve().parent.parent / "skills" / "q-mode" / "playbooks"
CHANGE = re.compile(r"^\s*[-*]\s+\*\*(After|Before|Replace|In)\*\*\s+[\"“](.+?)[\"”]", re.MULTILINE)


def meta(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip().strip('"')
    return out


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    found = [p for d in (".qstack/playbooks", ".agents/playbooks") for p in sorted(Path(d).glob("*.md"))]
    if not found:
        print("no project playbooks found")
        return 0
    problems = []
    for p in found:
        text = p.read_text(encoding="utf-8")
        m = meta(text)
        if "when" not in m:
            problems.append(f"{p}: frontmatter needs `when`")
        stems = [s.strip().removesuffix(".md") for s in m.get("extends", "").split(",") if s.strip()]
        bodies = []
        for s in stems:
            f = BUNDLED / f"{s}.md"
            if not f.exists():
                problems.append(f"{p}: extends '{s}', which this qstack version does not have")
            else:
                bodies.append(norm(f.read_text(encoding="utf-8")))
        for kind, quote in CHANGE.findall(text):
            if bodies and not any(norm(quote) in b for b in bodies):
                problems.append(f"{p}: **{kind}** quotes text not found in {', '.join(stems)}: \"{quote[:60]}\"")
    for line in problems:
        print(line)
    if not problems:
        print(f"OK: {len(found)} project playbook(s) anchor cleanly")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
