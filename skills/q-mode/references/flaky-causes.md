# Flaky test causes

The categories follow the empirical literature that starts with Luo et al., "An Empirical Analysis of Flaky Tests" (FSE 2014). Asynchronous wait, concurrency, and test order dependency are always the most common causes. UI suites also have environment and runner issues near the top.

| Cause | Signature | Fix at the cause |
|-------|-----------|------------------|
| Asynchronous wait | Fails on fast machines, or is slower on loaded CI. Examples: "Element not found", a stale element, or an assertion before the request settles. | Wait for the condition that the assertion needs (web-first assertions, awaited events, polling with a deadline). Remove fixed sleeps. |
| Concurrency | Failures depend on interleaving. Examples: lost updates, deadlocks, partial state. | If the race is the subject of the test, make the interleaving explicit with latches or barriers. If it is not, remove shared mutable state. Check if the product has the race. |
| Test order dependency | Passes alone, fails after a specific test, or the reverse. | Remove the dependency. Each test sets up and tears down its own state. Run the tests in random order to find the other dependencies. |
| Data collision | Fails only in parallel. Examples: unique-key errors, wrong counts. | Use unique data for each test and worker. Use disposable stores. |
| Time | Fails at midnight, at month end, at DST changes, or in another timezone. | Inject or fake the clock. Fix the timezone and locale. |
| Randomness | Fails for some seeds. | Set the seed and log it. Inject the generator. |
| Network or third party | Timeouts, rate limits, sandbox outages. | Stub at the system boundary. Use live calls only in dedicated integration tests on a controlled dependency. |
| Resource limits and timeouts | Fails under parallel load, on small runners, or near memory limits. | Measure before you increase a timeout. Reduce parallelism for that resource, or give it its own pool. |
| Platform | Fails on one OS, browser, viewport, or font set. | Fix the platform that the assertion depends on, or assert on facts that do not depend on the platform. |
| Runner or infrastructure | Examples: worker crashes, artifact upload failures, cache corruption. | Fix or report the infrastructure. Do not change the test. |
| Marginal hardware | Fails at temperature or voltage corners, on specific serials, after warm-up, or when a cable moves. | Log the conditions and serials of each run. Characterize across corners. Inspect connectors and fixtures. Fix the margin in the design or in the fixture. |
| Power integrity and noise | Resets or corruption under load, during radio transmit, or at motor start. | Measure the supply rails during the event. Fix the decoupling, grounding, or sequencing. |
| Real product race | The product also misbehaves intermittently for users. | File a bug report. This is the most valuable flake that you can find. |

## Confirmation protocol

1. Use the same commit and N runs (at least 20, or the repeat option of the runner).
2. Use these modes: alone, full suite, parallel, random order.
3. Record the pass rate for each mode and the failure signature of each failing run.
4. Compare a failing trace with a passing trace before you form a hypothesis.
5. After the fix, repeat the same protocol with the same N. Report both rates.
