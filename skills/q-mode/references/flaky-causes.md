# Flaky test causes

The categories follow the empirical literature that starts with Luo et al., "An Empirical Analysis of Flaky Tests" (FSE 2014). Asynchronous wait, concurrency, and test order dependency are consistently the most common causes. UI suites add environment and runner issues near the top.

| Cause | Signature | Fix at the cause |
|-------|-----------|------------------|
| Asynchronous wait | Fails faster on fast machines or slower on loaded CI. "Element not found", stale element, assertion before the request settles. | Wait for the condition the assertion needs (web-first assertions, awaited events, polling with a deadline). Remove fixed sleeps. |
| Concurrency | Failures depend on interleaving. Lost updates, deadlocks, partial state. | Make the interleaving explicit with latches or barriers when the race is the subject. Remove shared mutable state when it is not. Check whether the product has the race. |
| Test order dependency | Passes alone, fails after a specific test, or the reverse. | Remove the dependency. Each test sets up and tears down its own state. Run in random order to find the others. |
| Data collision | Fails only in parallel. Unique-key errors, counts off. | Unique data per test and worker. Disposable stores. |
| Time | Fails at midnight, month end, DST changes, or in another timezone. | Inject or fake the clock. Pin the timezone and locale. |
| Randomness | Fails for some seeds. | Seed and log the seed. Inject the generator. |
| Network or third party | Timeouts, rate limits, sandbox outages. | Stub at the system boundary. Keep live calls for dedicated integration tests on a controlled dependency. |
| Resource limits and timeouts | Fails under parallel load, on small runners, near memory limits. | Measure before raising a timeout. Reduce parallelism for that resource or give it its own pool. |
| Platform | Fails on one OS, browser, viewport, or font set. | Pin the platform the assertion depends on, or assert on platform-independent facts. |
| Runner or infrastructure | Worker crashes, artifact upload failures, cache corruption. | Fix or report the infrastructure. Do not change the test. |
| Marginal hardware | Fails at temperature or voltage corners, on specific serials, after warm-up, or when a cable moves. | Log conditions and serials per run. Characterize across corners. Inspect connectors and fixtures. Fix the margin in the design, or the fixture. |
| Power integrity and noise | Resets or corruption under load, radio transmit, or motor start. | Measure supply rails during the event. Fix decoupling, grounding, or sequencing. |
| Real product race | The product misbehaves intermittently for users too. | Bug report. This is the most valuable flake you will find. |

## Confirmation protocol

1. Same commit, N runs (at least 20, or the runner's repeat option).
2. Modes: alone, full suite, parallel, random order.
3. Record pass rate per mode and the failure signature of each failing run.
4. Compare a failing trace with a passing trace before forming a hypothesis.
5. After the fix, repeat the same protocol with the same N and report both rates.
