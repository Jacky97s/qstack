# Stage 7 — Requirement Traceability Matrix (RTM)

**Goal:** produce a formal, reviewable matrix that walks every requirement down
to the test cases that cover it, surfaces coverage gaps, and serves as the
final quality gate. The RTM is the product made visible: a reviewer points at
any spec AC and sees its goals → scenarios → cases, and at any case and walks
back to the requirement.

**The RTM is NOT hand-authored.** It is generated from `test-index.csv` (the
state source) by `scripts/qa_status.py rtm`. Editing it by hand would let it
drift from the CSV. You run the generator, then *review* its output.

## Inputs

- `<project>/test-index.csv` — the authoritative state: the full
  `case_id → scenario_id → goal_id → spec_ac` chain plus `priority`,
  `test_type`, `stage_status`.
- `<project>/02-test-goals/test-goals.md` — goal descriptions, for human
  readability in the matrix.
- `<project>/04-test-scenarios/test-scenarios.md` — scenario objectives, for
  detail in the matrix.

## Process

1. Run `python3 <skill>/scripts/qa_status.py rtm <project>/`.
2. The script reads the CSV and the goal IDs declared in
   `02-test-goals/test-goals.md` (`## G<n>` headings), and writes
   `<project>/07-rtm/rtm.md` with the four sections below. Scenario objectives
   stay in `04-test-scenarios/test-scenarios.md` for the reviewer to read.
3. Review the generated RTM against the human gate question.

## Output — `<project>/07-rtm/rtm.md`

### 1. Traceability Matrix

Grouped `spec_ac → goal_id → scenario_id → case_id`, showing the full chain for
every requirement. A blank `case_id` means the scenario is not yet cased.

### 2. Coverage Summary

- Totals: goals, scenarios, cases.
- Percentage cased by priority tier (P0 / P1 / P2 / P3) — e.g. "P0: 8/8
  (100%), P1: 5/9 (56%)".

### 3. Gap Analysis

- Scenarios without a case (`stage_status=scenario`) — not yet written.
- Goals without any scenario — should be **zero** after Stage 4; if not, it is
  a coverage hole to fix before sign-off.

### 4. Test Type Distribution

- Count and percentage of cases by `test_type`
  (functional / API / E2E / performance / security / usability). Compare this
  against the Test Plan's strategy — a mismatch (e.g. plan called for API
  coverage but distribution is all functional) is a finding.

## Continuously updatable

The RTM is regenerable. After each Stage 6 batch adds cases, re-run
`python3 <skill>/scripts/qa_status.py rtm <project>/` to get an updated report — the
coverage percentages and gap list move as cases land. It is both a milestone
artifact and a live coverage dashboard.

## Human gate

Present the Coverage Summary and Gap Analysis, then ask: **"Does the
traceability matrix show adequate coverage — are the gaps acceptable, and is
the test type distribution aligned with the Test Plan strategy?"** Stop.
"Acceptable gaps" is a human call: deferring a P2 boundary case may be fine;
an uncased P0 is not.

## Definition of done

- `07-rtm/rtm.md` generated with all four sections populated.
- Coverage percentages computed per priority tier.
- Gap list reviewed; remaining gaps are explicitly accepted.
- No surprise gaps — every P0 scenario has a case.
