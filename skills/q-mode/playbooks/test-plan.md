### Test plan

**You own the strategy. Scope by risk, decide how each risk is covered, define done.**

For a feature or a release.

1. Size the input. A release planned from a full spec set runs the **Shift-left** playbook, Stage 0 first when the spec has not been audited. Everything else runs the steps below.
2. Inventory what changed from artifacts, not titles: the diff or merge list, release notes, tickets, API schema diff, migrations, flags, and dependency bumps. Verify each change against the artifact (method, fields, existence) before planning around it. Mismatches become open questions.
3. Build the risk map: each area gets likelihood, impact, level, and the reason (**principle-risk-before-coverage**). Include non-functional risk (security, performance, accessibility, compatibility, data migration) only when a reason puts it on the map.
4. For each risk choose the coverage: the layer (**principle-cheapest-layer-that-catches-it**), technique, oracle source, data, environment, and whether it is automated, manual, or an exploratory charter.
5. Define entry and exit criteria as checkable conditions. Name what is out of scope and why.
6. List environment and data needs, and every destructive or shared-environment operation that will need approval (**principle-protect-shared-environments**).
7. Trace: requirement → risk → planned test or charter. A high risk with no planned coverage is a finding.
8. For a release-critical plan, get a fresh review of the plan (the **grill-the-plan** skill with the operator, or a fresh reviewer subagent).

**Reply:** the risk map, the coverage approach per risk, entry and exit criteria, out-of-scope with reasons, approvals needed, and open questions.
