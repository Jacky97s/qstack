# Stage 5 — Test Environment & Data Plan

**Goal:** describe *where* tests run and *what data* they need, together, so QA
can answer one question in a single review: **"can we provision this?"**
Combining environment config with data planning avoids the split-brain where
the env is ready but the data isn't (or vice versa). Output
`05-test-env-data/test-env-data.md` with two sections.

## Inputs

- `<project>/04-test-scenarios/test-scenarios.md` — the scenarios, and which
  ones are `oracle? = yes` (that column lives in the scenario tables, not in
  the CSV). `<project>/test-index.csv` lists the scenario rows.
- The data model spec: `<project>/docs/DB.md`, or the data-model chapter inside
  `<project>/docs/SRS.md` when there is no standalone `DB.md`. Every datum must
  tie to a real schema field — no invented columns.
- `<project>/03-test-plan/test-plan.md` — the tool chain (§2) and environment
  dependencies (§6) the plan committed to.

## Output

`<project>/05-test-env-data/test-env-data.md`, two sections.

### Section 1 — Test Environment

Make this **actionable**: a QA engineer should be able to set up without asking
follow-up questions.

- **Staging URLs and versions** — the environment(s) under test and the build
  version expected (never production).
- **Infrastructure config** — DB, cache, queues (host/role references, not
  secrets).
- **Tool chain** — automation frameworks, API clients, mock services, oracle
  tools, consistent with the Test Plan §2.
- **Access credentials reference** — *pointers* to where secrets live (vault
  path, config key, 1Password item). **Never the actual secrets.**
- **Device / browser matrix** — for UI testing: which browsers, viewports,
  devices, and OS combinations.

### Section 2 — Test Data

- **Shared fixtures** — accounts/roles reusable across scenarios.

  | Account | Role | Preconditions | Provisioning |
  |---------|------|---------------|--------------|
  | demo_user_a | <role> | <initial state> | seed script / DB insert |

- **Per-scenario data needs** — for each scenario, its pre-state, inputs, and
  how each datum is provisioned.

  | Scenario | Pre-state (real schema fields) | Inputs | Provisioning method |
  |----------|--------------------------------|--------|---------------------|
  | G1-S1 | `orders.status='pending'`, 1 row #1234 | <...> | seed script |

- **Oracle-backed data flagging** — every scenario marked `oracle? = yes` in
  the `04-test-scenarios` tables gets its computed value listed here with the deterministic
  oracle that produces the expected result (so `Then` compares
  `oracle == api == db`, never a hand-typed number).
- **Provisioning method** for each datum — one of: seed script, direct DB
  insert, UI setup, field manipulation. State which.
- **No real SMS / 3rd-party calls.** Where a scenario would trigger an external
  send or charge, note the mock or DB-read path used to verify instead.

## Process

1. Create `<project>/05-test-env-data/` if absent and copy
   `templates/05-test-env-data.md`.
2. Fill Section 1 from the Test Plan's tool chain + env dependencies. Resolve
   every "TBD env detail" into a concrete URL/version/host or a credential
   pointer.
3. Walk the scenarios in `test-index.csv`. For each, list its data needs and
   tie every field to a real column in the data-model spec.
4. For every `oracle? = yes` scenario, record the oracle and the computed value
   it backs.
5. Note the provisioning method per datum, and the mock/DB-read path for any
   external-service interaction.

## Human gate

Present Section 1 (env) and the per-scenario data table, then ask: **"Can
staging provision all of this — is the environment accessible, are the
oracle-backed items correctly identified, and is the data feasible?"** Stop.
Infeasible data or an unreachable env means Stage 6 cases can't run.

## Definition of done

- Section 1 is actionable — QA can set the environment up without asking.
- Every scenario's data needs are listed and tied to real schema fields.
- Every `oracle? = yes` scenario has its oracle and computed value flagged.
- A provisioning method is noted for each datum; external sends use a mock /
  DB-read path, never a live call.
