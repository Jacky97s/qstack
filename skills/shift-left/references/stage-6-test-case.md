# Stage 6 — Test Case

**Goal:** turn one scenario into a strict **Given/When/Then** test case that a
machine could run without guessing — which means a human reads it the same way
every time. This is the only stage with a machine-checkable format: read
`references/gwt-rules.md` and run `scripts/gwt_lint.py` before presenting.
Output `06-test-cases/<scenario>.md` and update the scenario's row in
`test-index.csv`.

## Thin slice

**One scenario per run by default.** Do not batch all scenarios into cases in a
single pass — pick the next scenario, write its case, lint, gate. Batching
bloats context and degrades quality. The orchestrator may request a specific
small set (e.g. "the 3 P0 scenarios"), but the unit of work is one scenario.

## Inputs

- `<project>/test-index.csv` — pick the next row where
  `stage_status=scenario` (P0 first). This row gives `goal_id`, `scenario_id`,
  `priority`, `spec_ac`, `test_type`.
- `<project>/04-test-scenarios/test-scenarios.md` — the scenario's Type and
  Objective (what passing must prove), under its goal section.
- `<project>/05-test-env-data/test-env-data.md` — the data and environment for
  this scenario: shared fixtures, pre-state, inputs, provisioning, and any
  oracle for computed values.
- `<project>/helpers-inventory.md` — the `[Helper: name]` labels that exist. Only
  label a step with a helper that is listed here.
- `references/gwt-rules.md` — the GWT contract and the 10-item self-check.

## Process

1. Run `python3 <skill>/scripts/qa_status.py <project>/test-index.csv` to find the next
   scenario(s) to case (P0 first). Pick one.
2. Read that scenario's row in `04-test-scenarios/test-scenarios.md` for its
   Objective, and its data in `05-test-env-data/test-env-data.md` for the
   `Given` pre-state and inputs.
3. Copy `templates/06-test-case.md` to
   `<project>/06-test-cases/<scenario_id>.md` (e.g. `G1-S1.md`).
4. Write the case following `gwt-rules.md`:
   - **Given** — fully-expanded, concrete observable pre-state (no
     cross-references, no backend-invisible state). Pull it from the data plan.
   - **When** — one interaction per step, approved verbs only
     (`click / input / select / check / scroll / wait / navigate`, plus
     `request` for API), target by visible label, explicit value.
   - **Then** — checkable assertions mapped to Playwright-style names
     (`toHaveText / toBeVisible / toBeChecked / toHaveURL / toHaveCount`, or
     status + JSON path for API). No banned vague words (should, correct, works, as expected, normally, or
     their equivalents). Computed values compare three-way `oracle == api == db`.
   - Attach `[Helper: name]` labels only from `helpers-inventory.md`. Unlabeled
     steps stay natural language (honest partial automation). List any missing
     helper under "Proposed helpers" at the case bottom.
5. **Self-check** the 10 items in `gwt-rules.md`, then run
   `python3 <skill>/scripts/gwt_lint.py <project>/06-test-cases/<scenario_id>.md`. Fix
   until lint passes. The lint covers the mechanical subset; items 3, 6, 7, 9,
   10 need your judgment by hand.
6. **Update `test-index.csv`** for this scenario's row: set `case_id`, `helpers`
   (the labels used), `automatable` (`T` only if every step is labeled),
   and `stage_status=case`.

## Human gate

Present the linted case and the traceability chain
(`case_id → scenario_id → goal_id → spec_ac`), then ask for **final review and
sign-off**. Stop. Do not roll into the next scenario without the gate.

## Definition of done

- `06-test-cases/<scenario_id>.md` exists and `gwt_lint.py` passes.
- The 10-item self-check passed (including the judgment-only items).
- `test-index.csv` row updated: `case_id`, `helpers`, `automatable`,
  `stage_status=case`.
- Full traceability chain intact: `case_id → scenario_id → goal_id → spec_ac`.
