---
name: principle-measure-variation
description: "Apply when results vary: LLM and agent outputs, distributed timing, unit-to-unit differences in hardware, environmental conditions, or a production process. Run enough trials or samples. Report rates and spreads with their sample size. Do not decide from a single run or a single unit."
user-invocable: false
---

# Measure Variation

When the thing under test varies, one run or one unit is an anecdote. The test becomes a measurement. A measurement needs a sample size, a spread, and a decision rule that you choose before you look at the results.

**Nondeterministic software (LLMs, agents, ranking, timing).**

- Run each task k times and state k.
- pass@k (at least one of k succeeds) answers "can it do this?". pass^k (all k succeed) answers "can users count on it?". They diverge fast as k grows. Use pass^k for anything that a user relies on every time.
- Grade with code what code can check. Use model-graded rubrics only for the rest, and calibrate them against human labels. Read the transcripts, because scores can hide broken graders.
- Details are in `../q-mode/references/ai-evals.md`.

**Physical units and environments (firmware on devices, boards, products).**

- One passing unit proves that the design can work. It does not prove that the product works. Test enough units across builds, lots, and suppliers to see the unit-to-unit spread.
- Test across the corners that matter: temperature, supply voltage, humidity, load, and process or component tolerance. The nominal bench gives the least information.
- A zero-failure reliability claim needs a success-run sample size. Use `n ≥ ln(1 − C) / ln(R)` for confidence C and reliability R. For example, you need 22 units for R = 0.90 at C = 0.90, and 45 units for R = 0.95. Accelerated tests use a stated model to convert test time to use time, such as Arrhenius for temperature. State the model and its assumptions.

**Processes (production lines, services, pipelines).**

- Track variation with control charts and capability (`Cpk`) against the specification. Do not use pass counts alone. A process that passes today with `Cpk < 1` will ship defects tomorrow.

**For all of them.**

- Report rate, sample size, and spread, for each condition. "8/10 at 25 °C, 5/10 at 60 °C" is better than "mostly passes".
- Compare like with like: the same task set or test profile, the same sample plan, and the same grader or instrument, against a baseline. The change that you see when nothing changed is your noise floor.
- Gate on a threshold with tolerance. Choose it before the run.
- Trust the instrument first (**principle-trust-the-instrument**). Measurement variation looks like product variation.

Formulas and tables are in `../q-mode/references/reliability-stats.md`.
