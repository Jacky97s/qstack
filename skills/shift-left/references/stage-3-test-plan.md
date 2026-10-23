# Stage 3 — Test Plan

**Goal:** turn the Quality Brief's risk framing into an execution-level
strategy. The Brief answered *why we test* and *what's at risk* (WHY/WHAT);
the Test Plan answers *how / who / when* (HOW/WHO/WHEN) for each goal. It is
the bridge between risk and execution — read by QA, automation engineers, and
anyone scheduling the cycle.

**The Quality Brief is the INPUT, not something to restate.** Do not copy its
risk paragraphs, scope lists, or focus alerts into the plan. Reference them
(e.g. "see quality brief, focus alert #2") and build the *strategy* on top.

## Inputs

- `<project>/01-quality-brief/quality-brief.md` — risk framing, in/out scope,
  this release's focus + QA alerts. The plan's strategy must answer those
  alerts.
- `<project>/02-test-goals/test-goals.md` — the goals (`G1, G2, ...`) with
  priorities. Every goal here must appear in the test-strategy table.

## Output

`<project>/03-test-plan/test-plan.md` with these six sections, all filled (no
`TBD`):

### 1. Test Strategy

Which test *types* each goal needs. One row per goal; tick the types that
apply. Tie the choice back to the goal's risk, not to habit.

| Goal | functional | API | E2E | performance | security | usability | Rationale |
|------|:----------:|:---:|:---:|:-----------:|:--------:|:---------:|-----------|
| G1 | ✓ | ✓ | | | | | <why these types, which risk they answer> |
| G2 | ✓ | | ✓ | | ✓ | | <...> |

### 2. Automation Strategy

- Which goals / areas are worth automating now, and which stay manual this
  cycle (and why — flakiness, one-off, exploratory).
- Tool choices per layer (UI / API / data oracle), referencing the team's
  existing helpers where they exist.
- What the automation depends on (stable selectors, seedable data, an oracle).

### 3. Entry / Exit Criteria

- **Entry** — conditions that must hold before testing starts: spec frozen for
  scope, staging deployed at the right version, blocking OQs resolved, test
  data provisionable.
- **Exit** — conditions to declare testing done: P0/P1 coverage executed,
  defect thresholds met, no open blocker, RTM coverage at target.

### 4. Schedule & Resources

- Who tests what (by goal area / role).
- Estimated effort per goal area (rough person-days or relative size).
- Sequencing — what must be tested first (e.g. shared login flow before
  role-specific flows).

### 5. Risk Assessment

Per-goal *tactical* risk and mitigation — more granular than the Brief's
strategic framing. The Brief says "payments are the high-risk surface"; here
you say "G3 settlement rounding risk = High → mitigate with three-way oracle +
boundary cases at 0, negative, and the cap".

| Goal | Tactical risk | Level (H/M/L) | Mitigation |
|------|---------------|:-------------:|------------|
| G1 | <...> | M | <...> |

### 6. Dependencies & Assumptions

- Staging environment readiness (which services must be up, at which version).
- 3rd-party mocks / stubs needed (SMS, payment gateway, hardware) — never live.
- Test data availability and who provides it.
- Assumptions that, if false, invalidate part of the plan (state them so a
  reviewer can challenge them).

## Process

1. Create `<project>/03-test-plan/` if absent and copy
   `templates/03-test-plan.md`.
2. Read the Quality Brief's focus + QA alerts and the goal list from Stage 2.
   Do **not** re-read the full spec — the goals already distilled it.
3. For each goal, decide the test types (§1) tied to its risk, then derive the
   automation approach (§2).
4. Fill §3–§6. Keep entry/exit criteria *realistic* — conditions the team can
   actually meet and check, not aspirational.
5. Self-check: every Stage 2 goal appears in the §1 table; every focus alert
   from the Brief is answered by some strategy/mitigation; no `TBD` remains.

## Human gate

Present the strategy table and the entry/exit criteria, then ask: **"Is the
test strategy complete — are the test types per goal correct, is the automation
approach feasible, and are the entry/exit criteria realistic?"** Stop. Stage 4
reads the per-goal test types from here, so a wrong type choice propagates.

## Definition of done

- `03-test-plan/test-plan.md` exists with all six sections filled — no `TBD`.
- Every goal from Stage 2 appears in the test-strategy table with at least one
  test type selected.
- Automation strategy names real tools/helpers; manual-only areas are justified.
- Entry/exit criteria are checkable conditions, not vague intentions.
