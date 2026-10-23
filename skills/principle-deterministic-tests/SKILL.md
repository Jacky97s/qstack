---
name: principle-deterministic-tests
description: "Apply to any test that uses time, randomness, ordering, network, concurrency, or asynchronous UI. The same code and the same inputs must give the same result. Wait on conditions. Do not use fixed sleeps."
user-invocable: false
---

# Deterministic Tests

A test that can pass and fail on the same code measures luck. Control every source of variation that the test does not intend to measure.

- **Time.** Inject or fake the clock. Pin the timezone and locale. Do not assert on "now" without control.
- **Randomness.** Seed it and log the seed on failure, or inject the generator.
- **Waiting.** Wait for a condition with a deadline. Use web-first assertions, polling with a timeout, or an awaited event. Do not use fixed sleeps (`sleep`, `waitForTimeout`, `Thread.sleep`, `cy.wait(<ms>)`). A sleep is too short on a slow machine. On a fast machine it wastes time.
- **Order.** Every test must pass alone, in any order, and in parallel with the others. No test can depend on state that another test left.
- **Network and third parties.** Stub at the system boundary that the product already isolates. Keep real calls for the tests whose purpose is that integration. Run those tests where the dependency is controlled.
- **Concurrency.** When the race is the subject, make the interleaving explicit (latches, barriers, deterministic schedulers). When it is not the subject, remove the race.
- **Environment.** Pin the versions, viewports, fonts, and feature flags that the assertion depends on.

Some systems are nondeterministic, such as an LLM or an agent. You cannot make a test of such a system deterministic. Measure it instead (**principle-measure-variation**).

The guard hook blocks new fixed sleeps in test files. For a deliberate exception, put `qstack: allow-sleep <reason>` on the same line.
