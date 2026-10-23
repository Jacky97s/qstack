---
name: principle-cheapest-layer-that-catches-it
description: "Apply when you choose where a test lives. Put each check at the lowest layer where you can observe the failure: static, unit, component or contract, API or integration, end-to-end, then manual or exploratory. Do not repeat one assertion across layers."
user-invocable: false
---

# Cheapest Layer That Catches It

Lower layers run faster, fail closer to the cause, cost less per run, and break less often. Some failures are visible only at higher layers. This is true for software, firmware, hardware, and processes. Examples are a simulation before a bench, a bench before a chamber, and a process control before final inspection. Choose the layer by where you can observe the failure. Do not choose by habit.

| The risk lives in | Cheapest layer |
|-------------------|----------------|
| Types, nullability, obvious misuse | Static analysis, the type system, lint |
| Pure logic, calculations, parsing, rules | Unit tests, property-based tests |
| The states and accessibility of a UI component | Component tests |
| An agreement between services | Contract tests (consumer-driven) |
| Persistence, queries, migrations, auth wiring, the API of one service | API or integration tests against real dependencies where this is cheap |
| A user journey where the risk is in the integration of UI, backend, and data | A small number of end-to-end tests |
| Usability, visual judgment, unknown unknowns | Exploratory sessions, human review |
| Firmware logic that does not depend on hardware | Host unit tests, model-in-the-loop and software-in-the-loop simulation |
| Firmware timing, drivers, peripherals, power modes | Processor-in-the-loop, then hardware-in-the-loop on a rig |
| Electrical and mechanical design margins | Component and board-level characterization across corners |
| Environmental and reliability risk | Environmental, stress, and accelerated life tests on production-intent units |
| Process escapes on a production line | In-process controls and statistical process control before end-of-line test |

Rules:

- Give each behavior one owning layer. A higher-layer test of the same journey must assert the integration. It must not assert every rule again.
- End-to-end tests cover critical journeys and seams. Put business-rule permutations in lower layers.
- When a test at a high layer keeps finding one class of bug, add the cheaper test that finds it. Keep the high-layer test thin.
- To fix a slow or flaky suite, you can move a test down one layer. Do this only when you can still observe the risk at the lower layer.
