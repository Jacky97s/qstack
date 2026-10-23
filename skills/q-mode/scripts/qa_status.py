#!/usr/bin/env python3
"""Coverage check over a traceability table. Prints to stdout and writes no files.

Usage:
  python3 qa_status.py status <table.csv>
  python3 qa_status.py rtm <table.csv> [--goals <plan.md>] [--full] [--fail-on-p0]

The table needs the columns case_id, goal_id, scenario_id, priority, spec_ac,
test_type, stage_status (scenario or case); extra columns are ignored.

status  counts by stage, priority, and test type, and lists what to case next.
rtm     reports coverage by priority, scenarios without a case, and, with
        --goals, goals declared as '## G<n>' or '### G<n>' headings that have no
        scenario. --full adds the full requirement → goal → scenario → case
        matrix, for audits that need it. --fail-on-p0 exits 1 when any P0
        scenario has no case.
"""
import csv
import re
import sys
from collections import Counter

PRIORITIES = ["P0", "P1", "P2", "P3"]


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [{k: (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)]


def cased(r):
    return r.get("case_id") and r.get("stage_status") == "case"


def goal_ids(path):
    with open(path, encoding="utf-8") as f:
        return re.findall(r"^#{2,3}\s+(G\d+)\b", f.read(), re.MULTILINE)


def status(rows):
    print(f"rows: {len(rows)}")
    for title, key in (("stage_status", "stage_status"), ("priority", "priority"), ("test_type", "test_type")):
        print(f"\nby {title}:")
        for k, v in sorted(Counter(r.get(key) or "(blank)" for r in rows).items()):
            print(f"  {k:<14} {v}")
    pending = [r["scenario_id"] for r in rows if not cased(r)]
    if pending:
        print(f"\nnext: {len(pending)} scenario(s) without a case")
        p0 = [s for s in pending if any(r["scenario_id"] == s and r.get("priority") == "P0" for r in rows)]
        if p0:
            print(f"  P0 first: {', '.join(p0)}")
    else:
        print("\nevery scenario has a case")
    return 0


def rtm(rows, goals_file, full, fail_on_p0):
    out = ["# Coverage check", "", "## Coverage by priority", ""]
    for p in PRIORITIES:
        tier = [r for r in rows if r.get("priority") == p]
        if tier:
            done = sum(1 for r in tier if cased(r))
            out.append(f"- {p}: {done}/{len(tier)} ({done * 100 // len(tier)}%)")
    done_all = sum(1 for r in rows if cased(r))
    out.append(f"- Total: {done_all}/{len(rows)}")

    gaps = sorted((r for r in rows if not cased(r)),
                  key=lambda r: (r.get("priority") or "P9", r.get("scenario_id", "")))
    out += ["", "## Scenarios without a case", ""]
    out += [f"- {r['scenario_id']} ({r.get('priority') or 'no priority'}, {r.get('spec_ac') or 'no spec_ac'})"
            for r in gaps] or ["None."]

    if goals_file:
        declared = goal_ids(goals_file)
        present = {r.get("goal_id") for r in rows}
        orphans = [g for g in declared if g not in present]
        out += ["", f"Goals without any scenario: {', '.join(orphans) if orphans else 'none'}"]

    if full:
        out += ["", "## Traceability matrix", "",
                "| spec_ac | goal_id | scenario_id | case_id | priority | test_type |",
                "|---------|---------|-------------|---------|----------|-----------|"]
        for r in sorted(rows, key=lambda r: (r.get("spec_ac", ""), r.get("goal_id", ""), r.get("scenario_id", ""))):
            out.append(f"| {r.get('spec_ac') or '—'} | {r.get('goal_id') or '—'} | {r.get('scenario_id') or '—'} "
                       f"| {r.get('case_id') or '—'} | {r.get('priority') or '—'} | {r.get('test_type') or '—'} |")

    print("\n".join(out))
    uncased_p0 = [r for r in gaps if r.get("priority") == "P0"]
    return 1 if fail_on_p0 and uncased_p0 else 0


def main(argv):
    if len(argv) < 3 or argv[1] not in ("status", "rtm"):
        print(__doc__)
        return 2
    rows = load(argv[2])
    if argv[1] == "status":
        return status(rows)
    goals = argv[argv.index("--goals") + 1] if "--goals" in argv else None
    return rtm(rows, goals, "--full" in argv, "--fail-on-p0" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
