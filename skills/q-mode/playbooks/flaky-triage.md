### Flaky triage

**You own the source of nondeterminism. Prove it, find it, fix it at the cause, prove the fix.**

1. Confirm it. Run the test N times on one commit (at least 20, or the runner's repeat option), in isolation, in the full suite, in parallel, and in random order when supported. Record the pass rate for each mode. No counts, no "flaky".
2. Compare a failing run with a passing run: traces, timestamps, network logs, console output, the order of tests before it, and worker assignment.
3. Locate the source in `references/flaky-causes.md`: asynchronous wait, concurrency, order dependency, data collision, time or timezone, randomness, network or third party, resource limits and timeouts, platform, the runner, or a real product race.
4. Rule out a product race before touching the test. When the product is at fault, run the **Bug report** playbook.
5. Fix at the cause (**principle-flaky-is-a-bug**): condition waits, isolated data, a seeded or injected random source, a fake clock, a boundary stub, or explicit ordering. Never a sleep, a blind timeout increase, retry-until-pass, or a weaker assertion.
6. Prove it with the same protocol and N. Report before and after rates.
7. When it cannot be fixed now: quarantine with a ticket, an owner, and an expiry date, and keep it running outside the gate.

**Reply:** the before and after pass rates with N and mode, the root cause with its evidence, the fix, and any product defect found.
