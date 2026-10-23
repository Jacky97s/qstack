# Test Scenarios — <release>

> Goal → Scenario → Objective. Each scenario traces to a spec AC and seeds one
> row in `test-index.csv`. `test_type` comes from the Test Plan.
> Lenses: positive / negative / boundary / cross-role / data-integrity.

## G1 — <business capability or quality attribute>

_Spec: <doc#section / AC id>_

| Scenario | Type | Objective (what passing proves) | Priority | spec_ac | test_type | oracle? |
|----------|------|---------------------------------|----------|---------|-----------|---------|
| G1-S1 | positive | <...> | P0 | <ac> | functional | no |
| G1-S2 | negative | <...> | P1 | <ac> | API | no |
| G1-S3 | boundary | <...> | P2 | <ac> | API | no |
| G1-S4 | data-integrity | <...> | P0 | <ac> | E2E | yes |

---

### Coverage self-check

- [ ] Every goal has at least one scenario (no orphan goals)
- [ ] Every scenario traces to a spec AC (no invented scenarios)
- [ ] Every happy path has at least one negative and one boundary sibling
- [ ] Money, permission, and persisted-data surfaces are flagged `oracle? = yes`
- [ ] Every `test_type` matches one the Test Plan assigned to the goal
