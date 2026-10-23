# Shift-left QA SOP

## Why

Defects found in a spec cost a conversation. The same defects found in code
cost a fix, a retest, and sometimes an incident. This pipeline turns a spec into
traceable test artifacts early, so gaps surface while they are cheap.

## Scope

The left half of the QA loop: spec → spec audit → quality brief → test goals →
test plan → test scenarios → test environment and data → test cases → RTM.
Execution and result write-back belong to the team's automation flow, which
consumes these artifacts.

## Source of truth

- The repository files under `<project>/` are the only state. `test-index.csv`
  is authoritative for scenarios and cases.
- `<project>/docs/` is a read-only spec snapshot. Provenance and audit scope live
  in `docs/.source`.
- Trackers and wikis are optional one-way mirrors. State is never read back from them.

## Roles

| Role | Owns |
|------|------|
| AI agent | Decomposition, drafting, format enforcement, self-checks, traceability bookkeeping |
| QA lead | Risk framing, scope, priorities, coverage judgment, sign-off |
| Spec owners (PM, engineering, data) | Resolving open questions |

## Gates

Every stage ends at a human gate with one focused question. Downstream stages
inherit upstream decisions, so a wrong call is cheapest to fix at its own gate.

| Stage | Gate question |
|-------|---------------|
| 0 Spec Audit | Which blocking open questions need an owner's answer before scoping? |
| 1 Quality Brief | Is the risk framing and in/out scope right? Did we miss a high-risk surface? |
| 2 Test Goals | Are the goals complete and the priorities right? |
| 3 Test Plan | Are the test types per goal right, the automation approach feasible, and the criteria checkable? |
| 4 Test Scenarios | Any missing negative, boundary, or cross-role scenario? |
| 5 Test Env & Data | Can the environment and every datum be provisioned? |
| 6 Test Case | Final review and sign-off of the linted case. |
| 7 RTM | Are the remaining gaps acceptable? An uncased P0 never is. |

## Definition of done

Each stage's reference file states its definition of done. A stage is done when
its artifact exists, its self-check passes, its checkbox in `progress.md` is
ticked, and its gate decision is logged.

## Traceability

Every row chains `case_id → scenario_id → goal_id → spec_ac` (and optionally
`ticket`). A reviewer can start from any case and walk back to its requirement,
or from any requirement and see every case that covers it.
