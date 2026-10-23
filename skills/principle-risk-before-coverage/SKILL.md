---
name: principle-risk-before-coverage
description: "Apply when you plan, prioritize, select, or cut tests. Spend effort in the order of likelihood times impact and state the risk that you accept. The coverage percentage is a byproduct. It is never the target."
user-invocable: false
---

# Risk Before Coverage

Testing effort is finite. Spend it where a failure is both likely and costly. Say plainly what you chose not to cover.

**Likelihood signals.** The signals are:
- size and churn of the change
- complexity
- new technology or a new integration
- concurrency
- data migration
- code with a defect history
- areas that the spec audit flagged
- code that nobody on the team understands

**Impact signals.** The signals are:
- money movement
- data loss or corruption
- security and privacy exposure
- legal or regulatory obligations
- the critical user journeys
- the number of affected users
- how hard it is to detect or roll back the failure

Rules:

- Rank the risks before you choose tests. Give each risk a level (H, M, L) with the reason in one line.
- Give every high risk a named mitigation: a test, a review, a flag, a monitor, or an explicit acceptance by the owner.
- Report a coverage number with what it misses. 90% line coverage with no test on the payment rounding path is a finding.
- Write down accepted risk with its owner. Unwritten risk is not accepted. Someone only forgot it.
- Rank the risks again when the change, the defect data, or the release scope moves.
