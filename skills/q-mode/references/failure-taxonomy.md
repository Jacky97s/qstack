# Failure taxonomy

Classify every failing test before changing anything. Group failures that share a cause first.

| Class | Signatures | Evidence that confirms it | Action | Never |
|-------|-----------|---------------------------|--------|-------|
| Product regression | Fails on the new build, passes on the last good build. Expectation matches its cited oracle source. | Same test, two builds, opposite results. The oracle source agrees with the test. | Bug report. Test stays red. | Edit the expectation to the new output. |
| Test defect | The test's expectation contradicts its oracle source. Wrong element, wrong state, wrong data assumption. A typo or import error. | The cited source, a screenshot or DOM dump of the real state, the corrected run. | Fix the test. Cite the source in the change. | Fix it by matching whatever the system returned. |
| Contract or doc drift | System and spec disagree, and both look deliberate. Schema snapshot out of date. | Both sides cited: the spec clause and the observed response or code path. | Report to the spec owner. Keep the test honest, marked with the open question. | Pick a side yourself. |
| Environment or infrastructure | Many unrelated tests fail at once. Connection refused, DNS, TLS, 401 or 403 across the board, quota exceeded, a dependency down, a stale deploy. | Health checks, the deploy log, the same tests passing elsewhere at the same commit. | Report to the owner with evidence. Rerun after the fix. | Mark the tests flaky. |
| Data collision | Passes alone, fails in the suite or in parallel. Unique-constraint errors. Counts off by the number of other tests. | Isolated pass plus suite failure, and the shared record identified. | Isolate the data. | Serialize the whole suite to hide it. |
| Flaky | Same commit, mixed results, with counts. | A pass rate over N runs. | Flaky triage. | Rerun until green and move on. |
| Rig, fixture, or instrument | Failures follow a station, bench, fixture, or probe rather than a unit. The doctor check or golden unit fails. Calibration out of date. | Golden unit fails on that station and passes on another. Calibration record. | Repair or recalibrate. Rerun the affected units. | Count it against the product. |
| Unit or sample defect | One serial fails, others from the same build pass. Visible damage, assembly or component fault. | Failure analysis on the unit. Swap test (move the suspect part, see if the failure follows). | Failure analysis to root cause. Include it in the sample statistics. | Discard the unit and retest until it passes. |
| Build or configuration mismatch | Firmware hash, hardware revision, configuration, or dependency version on the target differs from the one under test. | Recorded identities against the expected ones. | Reflash or reconfigure, record identities, rerun. | Report results for the wrong artifact. |
| Known issue | Matches an open ticket. | The ticket link and matching signature. | Link it. Quarantine only with ticket, owner, and expiry. | Skip it silently. |

## Self-fix boundary

| Fix it yourself | Escalate |
|-----------------|----------|
| Typos, imports, assertion logic that contradicts its cited source | Credentials, access, VPN, allow-lists, environment configuration (to the operator) |
| A locator after verifying the UI changed on purpose | Spec and system disagreeing (to the spec owner) |
| Test-owned data isolation | A rewrite of the plan or design (to the operator) |
| Skip reasons that cite the wrong ticket | Quarantining or deleting tests on a shared branch (to the operator) |
