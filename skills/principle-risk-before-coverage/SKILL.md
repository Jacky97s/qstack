---
name: principle-risk-before-coverage
description: "Apply when planning, prioritizing, selecting, or cutting tests. Spend effort in order of likelihood times impact and state the risk you accept. Coverage percentage is a byproduct, never the target."
user-invocable: false
---

# Risk Before Coverage

Testing effort is finite. Spend it where a failure is both likely and costly, and say plainly what you chose not to cover.

**Likelihood signals.** Size and churn of the change, complexity, new technology or a new integration, concurrency, data migration, code with a defect history, areas the spec audit flagged, and code nobody on the team understands.

**Impact signals.** Money movement, data loss or corruption, security and privacy exposure, legal or regulatory obligations, the critical user journeys, the number of users affected, and how hard the failure is to detect or roll back.

Rules:

- Rank risks before choosing tests. Each risk gets a level (H, M, L) with the reason in one line.
- Every high risk gets a named mitigation: a test, a review, a flag, a monitor, or an explicit acceptance by the owner.
- A coverage number is reported with what it misses. 90% line coverage with no test on the payment rounding path is a finding.
- Accepted risk is written down with its owner. Unwritten risk is not accepted, only forgotten.
- Re-rank when the change, the defect data, or the release scope moves.
