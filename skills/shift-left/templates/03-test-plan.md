# Test Plan — <release>

> HOW / WHO / WHEN. The Quality Brief is the input for WHY / WHAT; reference it,
> do not restate it. Input: `01-quality-brief/quality-brief.md`, `02-test-goals/test-goals.md`.

## 1. Test strategy (test types per goal)

| Goal | functional | API | E2E | performance | security | usability | Rationale (risk it answers) |
|------|:----------:|:---:|:---:|:-----------:|:--------:|:---------:|-----------------------------|
| G1 | ✓ | ✓ | | | | | <...> |

## 2. Automation strategy

- **Automate now:** <goals/areas and why>
- **Keep manual or exploratory this cycle:** <goals/areas and why>
- **Tools per layer:** <UI / API / data oracle, using existing helpers>
- **Depends on:** <stable selectors, seedable data, an oracle>

## 3. Entry / exit criteria

**Entry:** <checkable conditions, e.g. build X deployed to <env>, blocking OQs resolved, data provisionable>

**Exit:** <checkable conditions, e.g. all P0/P1 executed on the release build, no open blocker, RTM P0 coverage 100%>

## 4. Schedule and resources

| Goal area | Owner | Effort | Sequence / depends on |
|-----------|-------|--------|-----------------------|
| G1 | <name> | <size> | <...> |

## 5. Risk assessment (tactical)

| Goal | Tactical risk | Level (H/M/L) | Mitigation |
|------|---------------|:-------------:|------------|
| G1 | <...> | M | <...> |

## 6. Dependencies and assumptions

- **Environment:** <services and versions that must be up>
- **Third parties:** <mocks or stubs; never live sends or charges>
- **Test data:** <who provides it, how>
- **Assumptions that would invalidate the plan if false:** <...>
