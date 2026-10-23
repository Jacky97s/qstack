### Shift-left

**You own traceability from spec to case. Find the defects of the spec first, then plan, then write cases that trace back to it.**

Use for a spec set that needs a full audit and traceable cases before or during development. A spec set includes PRD, SRS, architecture, data model, API contracts, and design rules. For a single story or small change, use **Requirements review**, **Test plan**, and **Test design** instead.

Give the output of each stage in the reply, or where the tester asks. Do not create tracking files, folders, or process documents that the tester did not ask for. The spec is read-only.

| Stage | Uses | Output | Gate question |
|-------|------|--------|---------------|
| 0 Spec audit | **principle-label-the-unknowns**, **principle-oracle-first**, `references/spec-audit.md`, `scripts/audit_coverage.py` | Open questions with type, source, blocks, owner, status, and section and column coverage | Which blocking questions need an answer from an owner before planning? |
| 1 Plan | **principle-risk-before-coverage**, **principle-cheapest-layer-that-catches-it**, **principle-protect-shared-environments**, active lenses | Quality brief, goals, risk map and strategy, entry and exit criteria | Are the scope, goals, priorities, strategy, and criteria right and feasible? |
| 2 Cases | **test-design-techniques**, **principle-oracle-first**, **principle-isolate-test-data**, **principle-author-is-not-approver**, `references/gwt-rules.md`, `scripts/gwt_lint.py`, `qstack:test-reviewer` | Scenarios per goal, environment and data per scenario, Given/When/Then cases | Is a negative, boundary, or cross-role scenario missing? Can you provision the data? |
| 3 Coverage check | **principle-risk-before-coverage**, **principle-evidence-not-claims**, `scripts/qa_status.py` | Coverage by priority, scenarios without a case, goals without a scenario | Are the remaining gaps acceptable? An uncased P0 is never acceptable. |

The scripts are in the `scripts/` directory of this skill. Run them with that absolute path.

1. **Fix the spec scope.** List every file of the spec source recursively. Classify each file as include (requirements, data model, contracts, design rules, known-issue lists) or exclude (code, binaries, tooling), with a reason. When a classification is uncertain, confirm the scope with the tester. Record the source and its version or commit, so that others can reproduce the audit.
2. **Stage 0, spec audit.** Follow `references/spec-audit.md`.
   - Make an inventory of sections and columns with `audit_coverage.py inventory`.
   - Run the three layers: mechanical cross-reference with a per-column scan, semantic conflict probes, and implicit assumptions.
   - Confirm with `audit_coverage.py verify` that every section and column has a status.
   - Make each finding an open question with `type`, `source`, `blocks` (`plan`, `cases`, or `none`), `owner`, and `status`.
   - Stop at the gate.
3. **Stage 1, plan.** Build on the resolved questions. Keep the open ones visible.
   - Quality brief: business goals and the risk of each, in and out of scope, environments, roles, platforms, and external dependencies. Add how you avoid real sends, and the two to five focus alerts of this cycle.
   - Goals: `G1`, `G2`. Each goal has a spec reference, a quality risk, and a priority. No goal is so narrow that it cannot yield a happy, a negative, and a boundary scenario.
   - Strategy per goal: test types, layer, technique, oracle source, automation approach, and tactical risk with mitigation.
   - Entry and exit criteria as checkable conditions.
   - Stop at the gate.
4. **Stage 2, cases.**
   - For each goal, write scenarios `G1-S1`, `G1-S2` across the lenses positive, negative, boundary, cross-role, and data integrity. Each scenario has:
     - a one-line objective
     - a priority
     - a spec reference
     - a test type
     - a note on whether it needs an oracle for a computed or persisted value
   - For each scenario, write its environment and data, tied to real schema fields. Add the provisioning method and the oracle for computed values (`oracle == api == db`).
   - Then write one case per scenario, P0 first, in Given/When/Then per `references/gwt-rules.md`.
   - Lint the cases with `gwt_lint.py`. Add the vague words of the team language with `--banned`.
   - Have `qstack:test-reviewer` review the cases.
   - Stop at the gate for each batch.
5. **Stage 3, coverage check.** Report the gaps, not a document: coverage by priority, scenarios without a case, and goals or requirements without any scenario. The tester can keep a traceability table (CSV columns `case_id, goal_id, scenario_id, priority, spec_ac, test_type, stage_status`, with `stage_status` one of `scenario`, `case`). In that case, `qa_status.py rtm <table.csv> --goals <plan file>` computes the coverage. The option `--fail-on-p0` makes an uncased P0 a failing exit code for CI. Produce the full requirement-to-case matrix (`--full`) only in these cases: the regulated lens is active, a customer or contract requires it, or the tester asks.

When the work spans sessions, keep the open questions, the plan, and the traceability table where the tester chooses. Resume from them. When the tester explicitly tells you to run several stages in one go, continue. Collect every gate question in one list at the end.

**Reply:** per stage, the output, its self-check result, and the gate question. At Stage 3, coverage by priority and the gap list, with the full matrix only when it was required.
