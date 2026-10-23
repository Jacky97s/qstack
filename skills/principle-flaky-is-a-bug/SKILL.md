---
name: principle-flaky-is-a-bug
description: "Apply to any intermittent result: a test that passes and fails on the same code, a retry that changed red to green, or a suite that fails only in CI. Find the source of the nondeterminism. Retries and longer timeouts hide it."
user-invocable: false
---

# Flaky Is a Bug

A flaky test is a bug in the test, the environment, or the product. Each rerun to green deletes the evidence. It also teaches the team to ignore red.

- **Prove it before you name it.** "Flaky" requires N runs of the same commit and a pass rate. Without counts, it is an unclassified failure.
- **Find the source.** These are the common causes, in rough order of frequency in published studies:
  - asynchronous waits
  - concurrency
  - test order dependency
  - shared or colliding data
  - time and timezone
  - unseeded randomness
  - network and external services
  - resource limits
  - platform differences
  - the runner itself

  `../q-mode/references/flaky-causes.md` gives the signature and fix of each cause.
- **Intermittent hardware is real.** A marginal connector, thermal drift, power-supply droop, marginal timing at a voltage or temperature corner, and electrical noise all look flaky. Log the conditions (temperature, voltage, unit serial, fixture) with every run. Then the pattern can show.
- **Suspect the product too.** A race that makes a test flaky can make the checkout of a user flaky. Rule out a product race before you fix the test.
- **Forbidden fixes.** Do not add a sleep. Do not raise a timeout without a measured reason. Do not wrap the test in retry-until-pass. Do not loosen or delete the assertion. Do not mark the test optional.
- **Quarantine is a ticketed state.** It needs an owner, a ticket, and an expiry. A quarantined test must keep running outside the gate. Then data keeps accumulating.
- **Prove the fix with the same protocol.** Report the pass rate before and after over the same N.

You can keep framework-level retries on as a signal collector. Report every retried pass as a flake and count it.
