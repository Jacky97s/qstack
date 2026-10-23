# Release readiness — <release>

**Recommendation:** GO / GO WITH CONDITIONS / NO-GO · **Decision owner:** <name>

## Artifact under test

- Release candidate: <commit SHA, build number, image digest>
- Every result below was produced against this artifact: yes / no (list exceptions)

## Exit criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| <criterion> | MET / NOT MET / UNKNOWN | <run link, report path, counts> |

## Open defects

| ID | Severity | Summary | Decision |
|----|----------|---------|----------|
| <id> | <sev> | <summary> | fix before release / accepted (by whom) |

## Residual risk

- Not tested: <area> — <why> — <mitigation>
- Quarantined or skipped tests: <test> — <what it guards> — <ticket>

## Conditions (for GO WITH CONDITIONS)

- <checkable condition and who verifies it>

## Post-release checks

- Read-only smoke: <journeys>
- Monitors and thresholds: <dashboards, alert levels, owner>
