---
name: principle-measure-variation
description: "Apply whenever results vary: LLM and agent outputs, distributed timing, unit-to-unit differences in hardware, environmental conditions, or a production process. Run enough trials or samples, report rates and spreads with their sample size, and never decide from a single run or a single unit."
user-invocable: false
---

# Measure Variation

When the thing under test varies, one run or one unit is an anecdote. The test becomes a measurement, and a measurement needs a sample size, a spread, and a decision rule chosen before looking.

**Nondeterministic software (LLMs, agents, ranking, timing).**

- Run each task k times and state k.
- pass@k (at least one of k succeeds) answers "can it do this?". pass^k (all k succeed) answers "can users count on it?". They diverge fast as k grows. Use pass^k for anything a user relies on every time.
- Grade with code what code can check. Use model-graded rubrics only for the rest, calibrated against human labels. Read transcripts, because scores hide broken graders.
- Detail in `../q-mode/references/ai-evals.md`.

**Physical units and environments (firmware on devices, boards, products).**

- One passing unit proves the design can work, not that the product does. Test enough units across builds, lots, and suppliers to see unit-to-unit spread.
- Test across the corners that matter: temperature, supply voltage, humidity, load, and process or component tolerance. The nominal bench is the least informative condition.
- A zero-failure reliability claim needs a success-run sample size: `n ≥ ln(1 − C) / ln(R)` for confidence C and reliability R (22 units for R = 0.90 at C = 0.90, 45 for R = 0.95). Accelerated tests convert test time to use time through a stated model, such as Arrhenius for temperature. State the model and its assumptions.

**Processes (production lines, services, pipelines).**

- Track variation with control charts and capability (`Cpk`) against the specification, not with pass counts alone. A process that passes today with `Cpk < 1` will ship defects tomorrow.

**For all of them.**

- Report rate, sample size, and spread, per condition. "8/10 at 25 °C, 5/10 at 60 °C" beats "mostly passes".
- Compare like with like: same task set or test profile, same sample plan, same grader or instrument, against a baseline. The change you see when nothing changed is your noise floor.
- Gate on a threshold with tolerance, chosen before the run.
- Trust the instrument first (**principle-trust-the-instrument**). Measurement variation masquerades as product variation.

Formulas and tables are in `../q-mode/references/reliability-stats.md`.
