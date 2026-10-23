---
name: principle-deterministic-tests
description: "Apply to any test that touches time, randomness, ordering, network, concurrency, or asynchronous UI. Same code and same inputs must give the same result. Wait on conditions, never on fixed sleeps."
user-invocable: false
---

# Deterministic Tests

A test that can pass and fail on the same code measures luck. Control every source of variation the test does not intend to measure.

- **Time.** Inject or fake the clock. Pin the timezone and locale. Never assert on "now" without control.
- **Randomness.** Seed it and log the seed on failure, or inject the generator.
- **Waiting.** Wait for a condition with a deadline: web-first assertions, polling with a timeout, an awaited event. Fixed sleeps are banned (`sleep`, `waitForTimeout`, `Thread.sleep`, `cy.wait(<ms>)`). A sleep is either too short on a slow machine or wasted time on a fast one.
- **Order.** Every test passes alone, in any order, and in parallel with the others. No test depends on state another test left.
- **Network and third parties.** Stub at the system boundary the product already isolates. Keep real calls for the tests whose purpose is that integration, and run those where the dependency is controlled.
- **Concurrency.** Make the interleaving explicit (latches, barriers, deterministic schedulers) when the race is the subject, and remove it when it is not.
- **Environment.** Pin versions, viewports, fonts, and feature flags the assertion depends on.

When the system itself is nondeterministic, such as an LLM or agent, the test cannot be made deterministic. Measure it instead (**principle-measure-variation**).

The guard hook blocks new fixed sleeps in test files. A deliberate exception carries `qstack: allow-sleep <reason>` on the same line.
