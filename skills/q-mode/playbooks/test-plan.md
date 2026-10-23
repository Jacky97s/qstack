### Test plan

**You own the strategy. Scope by risk, decide how to cover each risk, and define done.**

Use for a feature or a release.

1. Size the input. A release that you plan from a full spec set runs the **Shift-left** playbook, with Stage 0 first when nobody has audited the spec. Everything else runs the steps below.
2. Inventory what changed from artifacts, not titles: the diff or merge list, release notes, tickets, API schema diff, migrations, flags, and dependency bumps. Verify each change against the artifact (method, fields, existence) before you plan around it. Mismatches become open questions.
3. Build the risk map: each area gets likelihood, impact, level, and the reason (**principle-risk-before-coverage**). Include non-functional risk (security, performance, accessibility, compatibility, data migration) only when a reason puts it on the map.
4. For each risk, choose the coverage: the layer (**principle-cheapest-layer-that-catches-it**), technique, oracle source, data, environment, and whether it is automated, manual, or an exploratory charter.
5. Define entry and exit criteria as checkable conditions. Name what is out of scope and why.
6. List the environment and data needs. List every destructive or shared-environment operation that needs approval (**principle-protect-shared-environments**).
7. Trace: requirement → risk → planned test or charter. A high risk with no planned coverage is a finding.
8. For a release-critical plan, get a fresh review of the plan. Use the **grill-the-plan** skill with the operator, or a fresh reviewer subagent.

**Reply:** the risk map, the coverage approach per risk, entry and exit criteria, out-of-scope with reasons, approvals needed, and open questions.
