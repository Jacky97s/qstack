---
name: principle-classify-before-you-fix
description: "Apply whenever a test fails. Name the failure class with evidence before changing anything: product regression, test defect, contract or doc drift, environment, data collision, flaky, or known issue. Never edit a test or expected value to match observed behavior unless the class is test defect and the oracle source agrees."
user-invocable: false
---

# Classify Before You Fix

A failing test is information. The cheapest way to destroy it is to change the test until it passes. Classify first, then act on the class. The full table with evidence and actions is `../q-mode/references/failure-taxonomy.md`.

| Class | Typical evidence | Action |
|-------|------------------|--------|
| Product regression | Fails on the new build, passes on the last good one, matches the oracle source | Bug report, test stays red |
| Test defect | The oracle source contradicts the test's expectation, or the test reaches the wrong element or state | Fix the test, cite the source |
| Contract or doc drift | System behavior and the spec disagree, and both look deliberate | Report the drift to its owner. Do not pick a side |
| Environment or infrastructure | Deploy, network, auth, quota, or a dependency down. Many unrelated tests fail together | Report to the owner with evidence, rerun after the fix |
| Data collision | Passes alone, fails in parallel or after another test | Isolate the data |
| Flaky | Passes and fails on the same commit, with run counts | Flaky triage |
| Rig, fixture, or instrument | The bench, fixture, probe, or station fails its doctor check or golden unit. Failures follow the station, not the unit | Repair or recalibrate, then rerun. Never count it against the product |
| Unit or sample defect | One serial fails and others of the same build pass. Assembly, component, or handling damage | Failure analysis on that unit. Count it in the sample statistics |
| Build or configuration mismatch | The firmware hash, hardware revision, or configuration on the unit differs from the one under test | Reflash or reconfigure, record identities, rerun |
| Known issue | Matches an open ticket | Link it. Quarantine only with ticket, owner, and expiry |

**The self-fix boundary.** You may fix on your own: typos, imports, assertion logic that contradicts its cited source, a locator after you verified the UI changed on purpose, and data isolation. You escalate: credentials, access, VPN, allow-lists, and environment configuration go to the operator. A disagreement between spec and system goes to the spec owner. A rewrite of the plan or design is the operator's judgment.

"The test is wrong" is a hypothesis with a burden of proof. Meet it with the oracle source, not with the observed value.
