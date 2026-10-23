### Flaky triage

**You own the source of nondeterminism. Prove it, find it, fix it at the cause, and prove the fix.**

1. Confirm it. Run the test N times on one commit (at least 20, or use the repeat option of the runner). Run it in isolation, in the full suite, in parallel, and in random order when the runner supports it. Record the pass rate for each mode. No counts, no "flaky".
2. Compare a failing run with a passing run: traces, timestamps, network logs, console output, the order of the tests before it, and worker assignment.
3. Find the source in `references/flaky-causes.md`. The causes are:
   - asynchronous wait
   - concurrency
   - order dependency
   - data collision
   - time or timezone
   - randomness
   - network or third party
   - resource limits and timeouts
   - platform
   - the runner
   - a real product race
4. Rule out a product race before you touch the test. When the product is at fault, run the **Bug report** playbook.
5. Fix at the cause (**principle-flaky-is-a-bug**). Use condition waits, isolated data, a seeded or injected random source, a fake clock, a boundary stub, or explicit ordering. Never use a sleep, a blind timeout increase, retry-until-pass, or a weaker assertion.
6. Prove the fix with the same protocol and N. Report the rates before and after.
7. When you cannot fix it now, quarantine it with a ticket, an owner, and an expiry date. Keep it running outside the gate.

**Reply:** the before and after pass rates with N and mode, the root cause with its evidence, the fix, and any product defect found.
