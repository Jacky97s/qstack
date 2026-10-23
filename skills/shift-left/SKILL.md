---
name: shift-left
description: "Eight-stage shift-left QA pipeline that turns a spec, PRD, SRS, or API contract into traceable test artifacts before or alongside development: a spec audit with numbered open questions and script-verified coverage, a one-page quality brief, test goals, a test plan, test scenarios, an environment and data plan, strict Given/When/Then cases with a lint, and a generated requirement traceability matrix. Use to audit a spec for contradictions and gaps, plan QA for a release from its documents, decompose requirements into goals and scenarios, write automation-ready cases, or produce an RTM. Repository files are the only state, so any stage resumes from the repo alone."
---

# Shift-left pipeline

Author traceable test artifacts from a spec, early. The pipeline is the left half of the QA loop:

`spec → spec audit → quality brief → test goals → test plan → test scenarios → env & data → test cases → RTM`

Stage 0 finds defects in the spec itself before any test artifact exists, which is the cheapest place a defect can be caught. Execution and result write-back stay with the team's automation flow. This pipeline produces artifacts in a shape that flow can consume.

Scripts live in this skill's `scripts/` directory. Every `<skill>` in the stage references means this skill's absolute directory.

## Operating principles

1. **Repository files are the single source of truth.** Everything lives under `<project>/`. `test-index.csv` is the authoritative state for scenarios and cases. External trackers are optional one-way mirrors, never state. Any stage resumes by re-reading the repository alone.
2. **Thin, atomic stages.** Each run reads one stage reference and works one slice, for example one scenario at a time in Stage 6. Do not load the whole spec or every artifact into context.
3. **AI drafts the structured work. Humans own judgment.** The agent decomposes, drafts, enforces format, self-checks, and keeps the traceability bookkeeping exact. People decide risk and scope, validate coverage and boundaries, confirm data feasibility, and sign off. Every stage ends at a human gate: present a tight summary and the diff, ask the stage's gate question, and stop. When the operator explicitly asks to run several stages in one go, continue, and collect every gate question in one list at the end instead of answering them yourself.
4. **Never write to the spec.** The spec snapshot is read-only. All output goes to the stage folders.
5. **Prose in the team's language, machine tokens in English.** Write artifact prose in the language named by `.qstack/profile.md` (or the spec's language when there is no profile). Keep IDs (`G1`, `G1-S1`, `TC-...`), CSV headers, the `Given`/`When`/`Then` headers and verbs, assertion names, status values, OQ `type` values, and `[Helper]` labels in English so the scripts stay deterministic. Pass the team-language vague words to `gwt_lint.py --banned`.

## Repository layout

A QA repository can host several projects, one subdirectory each.

```
<qa-repo>/
  <project>/
    docs/                     # read-only spec snapshot
      .source                 #   provenance and audit-scope triage
    progress.md               # stage checkboxes and gate log (resume point)
    test-index.csv            # state source, seeded by Stage 4
    helpers-inventory.md      # [Helper] label → real automation helper
    SOP.md                    # human-readable process
    00-open-questions/open-questions.md
    01-quality-brief/quality-brief.md
    02-test-goals/test-goals.md
    03-test-plan/test-plan.md
    04-test-scenarios/test-scenarios.md
    05-test-env-data/test-env-data.md
    06-test-cases/<scenario_id>.md
    07-rtm/rtm.md             # generated
```

`test-index.csv` columns: `case_id, goal_id, scenario_id, priority, spec_ac, test_type, helpers, automatable, stage_status, owner, ticket, notes`.

## The eight stages

| Stage | Read | Produces | Gate question |
|-------|------|----------|---------------|
| 0 Spec Audit | `references/stage-0-spec-audit.md` | `00-open-questions/open-questions.md` | Which blocking open questions need an owner's answer before scoping? |
| 1 Quality Brief | `references/stage-1-quality-brief.md` | `01-quality-brief/quality-brief.md` | Is the risk framing and in/out scope right? Did we miss a high-risk surface? |
| 2 Test Goals | `references/stage-2-test-goal.md` | `02-test-goals/test-goals.md` | Are the goals complete and the priorities right? |
| 3 Test Plan | `references/stage-3-test-plan.md` | `03-test-plan/test-plan.md` | Are test types, automation approach, and entry/exit criteria right and feasible? |
| 4 Test Scenarios | `references/stage-4-test-scenario.md` | `04-test-scenarios/test-scenarios.md` and seeded `test-index.csv` | Any missing negative, boundary, or cross-role scenario? |
| 5 Env & Data | `references/stage-5-test-env-data.md` | `05-test-env-data/test-env-data.md` | Can the environment and every datum be provisioned? |
| 6 Test Case | `references/stage-6-test-case.md` and `references/gwt-rules.md` | `06-test-cases/<scenario_id>.md` and updated CSV | Final review and sign-off of the linted case. |
| 7 RTM | `references/stage-7-rtm.md` | `07-rtm/rtm.md`, generated | Are the remaining gaps acceptable? |

Stage 0 runs three audit layers (mechanical cross-reference with a per-column deep scan, semantic conflict probes, implicit-assumption scan), bracketed by `scripts/audit_coverage.py inventory` before and `verify` after, so no section or column is silently skipped. Stage 6 is the only stage with a machine-checked format, enforced by `scripts/gwt_lint.py`. Stage 7 is generated by `scripts/qa_status.py rtm` and never hand-edited.

## Orchestrator

You are the router. Keep your own turns short. The work happens inside one stage at a time.

1. **Locate the project and snapshot the spec.**
   - **Fresh start:** ask for the spec source (repository URL, local path, or pasted text). Create `<project>/`, copy `templates/` into it (including `progress.md`, `SOP.md`, `helpers-inventory.md`, and `test-index.csv`), and snapshot the spec into `<project>/docs/`.
   - **Existing project:** read `<project>/docs/.source`. When the source is a repository, offer to re-sync. When the snapshot is stale or missing, ask for the source and re-snapshot.
   - **Snapshot procedure.** Enumerate every file in the source recursively. Classify each as `include` (anything a spec audit should read: PRD, SRS, architecture, data model, feature specs, API contracts, UI guidelines, known-issue or TODO lists) or `exclude` (source code, binaries, images, tooling config, generated output), one line each with a reason. When any classification is uncertain, show the triage table and confirm scope before copying. Copy the `include` set into `docs/`. Write `docs/.source` with origin, sync time, commit when available, and both lists with reasons. After the snapshot, `docs/` is read-only, and Stage 0 audits exactly the `include` set.
2. **Read `progress.md`.** The earliest unchecked stage is the current stage. Cross-check with `python3 <skill>/scripts/qa_status.py <project>/test-index.csv` for Stage 6 detail.
3. **Confirm the next action in one line,** such as "Stage 4 has 12 scenarios seeded and no cases. Case the 3 P0 scenarios?"
4. **Read only that stage's reference** and do exactly what it says on the agreed slice.
5. **Stop at the gate.** Write the artifacts, update `test-index.csv`, tick the checkbox in `progress.md`, and add a gate-log row. Present what changed, the traceability deltas, and the gate question. Wait.

An interrupted run re-derives its state from `progress.md` and the CSV. There is nothing to remember.

## Traceability

Every row chains `case_id → scenario_id → goal_id → spec_ac`, plus an optional `ticket`. `test_type` records the type the Test Plan assigned. A reviewer can point at any case and walk back to its requirement, or at any requirement and see every case that covers it. Keep the CSV consistent on every write, because coverage and the RTM are computed from it.

## How qstack's principles apply here

- Stage 0 open questions are the canonical form of **principle-label-the-unknowns**: each carries a `type`, a `blocks` stage, a `suggested-owner`, and a `status`.
- Stage 4's lenses and Stage 6's `oracle == api == db` rule are **principle-oracle-first** made concrete.
- Stage 1 and Stage 3 apply **principle-risk-before-coverage**.
- A drafted case is reviewed by someone other than its author before sign-off (**principle-author-is-not-approver**).

## Out of scope

Say so when asked: test execution and result write-back, automatic tracker sync, and generating automation code from `[Helper]` labels. Cases come out automation-ready. Wiring them into code is the **Automate** playbook of `q-mode`.

## Bundled resources

- `references/stage-0-spec-audit.md` through `references/stage-7-rtm.md`: one file per stage.
- `references/gwt-rules.md`: the strict Given/When/Then contract and its 10-item self-check.
- `scripts/audit_coverage.py`: Stage 0 inventory and coverage verification for any number of spec files.
- `scripts/qa_status.py`: state summary and next-stage hint from the CSV, and `rtm` generation.
- `scripts/gwt_lint.py`: mechanical validation of a Stage 6 case file.
- `templates/`: seed files for a new project.
