# Failure taxonomy

Classify every failing test before you change anything. First, group the failures that share a cause.

| Class | Signatures | Evidence that confirms it | Action | Never |
|-------|-----------|---------------------------|--------|-------|
| Product regression | The test fails on the new build and passes on the last good build. The expectation matches its cited oracle source. | The same test gives opposite results on two builds. The oracle source agrees with the test. | File a bug report. Keep the test red. | Do not edit the expectation to match the new output. |
| Test defect | The expectation of the test contradicts its oracle source. Examples: wrong element, wrong state, wrong data assumption, a typo, or an import error. | The cited source, a screenshot or DOM dump of the real state, and the corrected run. | Fix the test. Cite the source in the change. | Do not fix the test to match whatever the system returned. |
| Contract or doc drift | The system and the spec disagree, and both look deliberate. A schema snapshot is out of date. | Both sides are cited: the spec clause and the observed response or code path. | Report to the spec owner. Keep the test honest and mark it with the open question. | Do not pick a side yourself. |
| Environment or infrastructure | Many unrelated tests fail at once. Examples: connection refused, DNS, TLS, 401 or 403 on all tests, quota exceeded, a dependency is down, a stale deploy. | Health checks, the deploy log, and the same tests that pass elsewhere at the same commit. | Report to the owner with evidence. Run again after the fix. | Do not mark the tests flaky. |
| Data collision | The test passes alone and fails in the suite or in parallel. Unique-constraint errors. Counts are wrong by the number of other tests. | An isolated pass plus a suite failure, and the shared record that you identified. | Isolate the data. | Do not run the whole suite in series to hide the problem. |
| Flaky | Same commit, mixed results, with counts. | A pass rate over N runs. | Do flaky triage. | Do not run again until green and then continue. |
| Rig, fixture, or instrument | Failures follow a station, bench, fixture, or probe and not a unit. The doctor check or golden unit fails. Calibration is out of date. | The golden unit fails on that station and passes on another. The calibration record. | Repair or recalibrate. Run the affected units again. | Do not count the failure against the product. |
| Unit or sample defect | One serial fails and the other units from the same build pass. Visible damage, or an assembly or component fault. | Failure analysis on the unit. A swap test (move the suspect part and see if the failure follows). | Do failure analysis to find the root cause. Include the unit in the sample statistics. | Do not discard the unit and test again until it passes. |
| Build or configuration mismatch | The firmware hash, hardware revision, configuration, or dependency version on the target is different from the one under test. | The recorded identities and the expected identities. | Reflash or reconfigure. Record the identities. Run again. | Do not report results for the wrong artifact. |
| Known issue | The failure matches an open ticket. | The ticket link and the matching signature. | Link the ticket. Quarantine only with a ticket, an owner, and an expiry. | Do not skip the test silently. |

## Self-fix boundary

| Fix it yourself | Escalate |
|-----------------|----------|
| Typos, imports, and assertion logic that contradicts its cited source | Credentials, access, VPN, allow-lists, and environment configuration (to the operator) |
| A locator, after you verify that the UI changed on purpose | The spec and the system disagree (to the spec owner) |
| Data isolation that the test owns | A rewrite of the plan or design (to the operator) |
| Skip reasons that cite the wrong ticket | Quarantine or deletion of tests on a shared branch (to the operator) |
