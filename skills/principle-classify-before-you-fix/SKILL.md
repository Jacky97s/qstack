---
name: principle-classify-before-you-fix
description: "Apply when a test fails. Name the failure class with evidence before you change anything: product regression, test defect, contract or doc drift, environment, data collision, flaky, or known issue. Do not edit a test or expected value to match the observed behavior unless the class is test defect and the oracle source agrees."
user-invocable: false
---

# Classify Before You Fix

A failing test gives information. The cheapest way to destroy that information is to change the test until it passes. Classify the failure first. Then act on the class. The full table with evidence and actions is in `../q-mode/references/failure-taxonomy.md`.

| Class | Typical evidence | Action |
|-------|------------------|--------|
| Product regression | Fails on the new build, passes on the last good build, matches the oracle source | Bug report, test stays red |
| Test defect | The oracle source contradicts the expectation of the test, or the test reaches the wrong element or state | Fix the test, cite the source |
| Contract or doc drift | System behavior and the spec disagree, and both look deliberate | Report the drift to its owner. Do not pick a side |
| Environment or infrastructure | Deploy, network, auth, quota, or a dependency is down. Many unrelated tests fail together | Report to the owner with evidence, rerun after the fix |
| Data collision | Passes alone, fails in parallel or after another test | Isolate the data |
| Flaky | Passes and fails on the same commit, with run counts | Flaky triage |
| Rig, fixture, or instrument | The bench, fixture, probe, or station fails its doctor check or golden unit. Failures follow the station, not the unit | Repair or recalibrate, then rerun. Do not count it against the product |
| Unit or sample defect | One serial fails and other units of the same build pass. Assembly, component, or handling damage | Failure analysis on that unit. Count it in the sample statistics |
| Build or configuration mismatch | The firmware hash, hardware revision, or configuration on the unit is not the one under test | Reflash or reconfigure, record identities, rerun |
| Known issue | Matches an open ticket | Link it. Quarantine only with ticket, owner, and expiry |

**The self-fix boundary.** You can fix these items on your own:
- typos
- imports
- assertion logic that contradicts its cited source
- a locator after you verify that the UI changed on purpose
- data isolation

You must escalate other items. Send credentials, access, VPN, allow-lists, and environment configuration to the operator. Send a disagreement between spec and system to the spec owner. A rewrite of the plan or design is a judgment for the operator.

"The test is wrong" is a hypothesis. You must prove it. Use the oracle source as proof, not the observed value.
