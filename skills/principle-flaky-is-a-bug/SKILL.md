---
name: principle-flaky-is-a-bug
description: "Apply to any intermittent result: a test that passes and fails on the same code, a retry that turned red to green, or a suite that only fails in CI. Find the source of nondeterminism. Retries and longer timeouts hide it."
user-invocable: false
---

# Flaky Is a Bug

A flaky test is a bug in the test, the environment, or the product. Each rerun-to-green deletes the evidence and teaches the team to ignore red.

- **Prove it before naming it.** "Flaky" requires the same commit run N times with a pass rate. Without counts it is an unclassified failure.
- **Find the source.** The common causes, in rough order of frequency in published studies: asynchronous waits, concurrency, test order dependency, shared or colliding data, time and timezone, unseeded randomness, network and external services, resource limits, platform differences, and the runner itself. `../q-mode/references/flaky-causes.md` maps each to its signature and fix.
- **Intermittent hardware is real.** A marginal connector, thermal drift, power-supply droop, marginal timing at a voltage or temperature corner, and electrical noise all look flaky. Log the conditions (temperature, voltage, unit serial, fixture) with every run so the pattern can surface.
- **Suspect the product too.** A race that makes a test flaky can make a user's checkout flaky. Rule out a product race before fixing the test.
- **Forbidden fixes.** Adding a sleep, raising a timeout without a measured reason, wrapping in retry-until-pass, loosening or deleting the assertion, and marking the test optional.
- **Quarantine is a ticketed state.** It needs an owner, a ticket, and an expiry. A quarantined test keeps running outside the gate so data keeps accumulating.
- **Prove the fix with the same protocol.** Report the pass rate before and after over the same N.

Framework-level retries can stay on as a signal collector, as long as every retried pass is reported as a flake and counted.
