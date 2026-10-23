---
name: principle-cheapest-layer-that-catches-it
description: "Apply when choosing where a test lives. Put each check at the lowest layer where the failure is observable: static, unit, component or contract, API or integration, end-to-end, then manual or exploratory. Do not repeat one assertion across layers."
user-invocable: false
---

# Cheapest Layer That Catches It

Lower layers run faster, fail closer to the cause, cost less per run, and break less often. Higher layers are the only place some failures are visible. This holds for software, firmware, hardware, and processes alike: a simulation before a bench, a bench before a chamber, a process control before final inspection. Choose by where the failure can be observed, not by habit.

| The risk lives in | Cheapest layer |
|-------------------|----------------|
| Types, nullability, obvious misuse | Static analysis, the type system, lint |
| Pure logic, calculations, parsing, rules | Unit tests, property-based tests |
| A UI component's states and accessibility | Component tests |
| An agreement between services | Contract tests (consumer-driven) |
| Persistence, queries, migrations, auth wiring, one service's API | API or integration tests against real dependencies where cheap |
| A user journey whose risk is in the integration of UI, backend, and data | A small number of end-to-end tests |
| Usability, visual judgment, unknown unknowns | Exploratory sessions, human review |
| Firmware logic independent of hardware | Host unit tests, model-in-the-loop and software-in-the-loop simulation |
| Firmware timing, drivers, peripherals, power modes | Processor-in-the-loop, then hardware-in-the-loop on a rig |
| Electrical and mechanical design margins | Component and board-level characterization across corners |
| Environmental and reliability risk | Environmental, stress, and accelerated life tests on production-intent units |
| Process escapes on a production line | In-process controls and statistical process control before end-of-line test |

Rules:

- One behavior, one owning layer. A higher-layer test of the same journey asserts the integration, not every rule again.
- End-to-end tests cover critical journeys and seams. Business-rule permutations belong below them.
- When a test at a high layer keeps finding a class of bug, add the cheaper test that would have caught it and let the high-layer test stay thin.
- Moving a test down a layer is a valid fix for a slow or flaky suite when the risk is still observable there.
