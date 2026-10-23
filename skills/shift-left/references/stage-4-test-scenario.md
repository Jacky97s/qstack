# Stage 4 — Test Scenarios

**Goal:** decompose each Goal into concrete **Scenarios**, each with an
**Objective** (what passing proves), across the coverage lenses. This is the
highest-judgment step: structured enough to trace, exhaustive enough that a
missing negative or boundary path shows up here, not in production. Output
`04-test-scenarios/test-scenarios.md` and seed one row per scenario into
`test-index.csv`.

The Goal answers *what capability we verify*; the Scenario answers *under which
concrete situation*, and the Objective answers *what its passing demonstrates*.

## Inputs

- `<project>/02-test-goals/test-goals.md` — the goals (`G1, G2, ...`) with
  their quality-risk descriptions and priorities.
- `<project>/03-test-plan/test-plan.md` — the per-goal test types (§1 Test
  Strategy) and overall approach. Each scenario inherits its `test_type` from
  the goal's row here.

## Process

1. Read the goals and, for each, the goal's row in the Test Plan strategy table
   to know which `test_type`(s) apply. Pull the relevant acceptance criteria
   from the spec sections the goal references.
2. For each goal, generate scenarios across these lenses — this is the coverage
   discipline, not a checklist to pad:
   - **positive** — the spec's main happy path.
   - **negative** — invalid input, denied permission, missing precondition.
   - **boundary** — limits, zero/empty, max, expiry, off-by-one.
   - **cross-role** — same flow, different actor or region, where the spec
     implies a difference.
   - **data-integrity** — wherever a value is computed or persisted, mark that
     an oracle is needed (`oracle? = yes`); Stage 5 provisions for it.
3. Write one section per goal containing a scenario table (format below).
4. Assign each scenario a `priority` (P0 blocker / P1 / P2 / P3) consistent
   with the goal's risk, and a `test_type` drawn from the Test Plan.
5. Seed `test-index.csv`: one row per scenario with `goal_id`, `scenario_id`,
   `priority`, `spec_ac`, `test_type`, `stage_status=scenario`. Leave
   `case_id`, `helpers`, `automatable` blank — Stage 6 fills them.

## Scenario table format

One section per goal:

```markdown
## G1 — <goal name>

_Spec: <doc#section / AC id>_

| Scenario | Type | Objective (what passing proves) | Priority | spec_ac | test_type | oracle? |
|----------|------|---------------------------------|----------|---------|-----------|---------|
| G1-S1 | positive | <...> | P0 | <ac> | functional | no |
| G1-S2 | negative | <...> | P1 | <ac> | functional | no |
| G1-S3 | boundary | <...> | P2 | <ac> | API | no |
| G1-S4 | data-integrity | <...> | P0 | <ac> | API | yes |
```

- **Scenario ID** — `G1-S1, G1-S2, ...`, contiguous per goal.
- **Type** — one of positive / negative / boundary / cross-role /
  data-integrity.
- **Objective** — one line; forces each scenario to earn its place.
- **Priority** — P0–P3, tied to the goal's risk framing.
- **spec_ac** — the section or AC id this scenario traces to.
- **test_type** — from the Test Plan's strategy row for this goal.
- **oracle?** — `yes` for any computed/persisted value (money, permission,
  quota, balance); `no` otherwise.

## Coverage self-check (run before the gate)

- Every goal has ≥1 scenario (no orphan goals).
- Every scenario traces to a spec AC (no invented scenarios).
- Every happy path has ≥1 negative **and** ≥1 boundary sibling.
- Money / permission / data surfaces flagged `oracle? = yes`.
- Every scenario's `test_type` matches one the Test Plan assigned to its goal.

## Human gate

Coverage is a human call. Present the scenario counts per goal and per
priority, plus the self-check results, then ask: **"Is coverage complete — any
missing negative, boundary, or cross-role scenario, and are the priorities and
test types right?"** Expect the QA lead to add scenarios; catching them here is
the point of doing this early.

## Definition of done

- `04-test-scenarios/test-scenarios.md` has one section per goal; every
  scenario has an objective.
- Every scenario is a row in `test-index.csv` with `priority`, `spec_ac`,
  `test_type`, and `stage_status=scenario`.
- No orphan goals; no untraceable scenarios.
