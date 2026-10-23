---
name: principle-trust-the-instrument
description: "Apply before trusting any measurement, test harness, rig, fixture, grader, or monitor. Prove the instrument can tell pass from fail: calibration and resolution for physical measurements, a known-bad input for test harnesses, a golden unit for production test, a labeled sample for graders. When a result surprises you, suspect the observation first."
user-invocable: false
---

# Trust the Instrument

Every verdict is only as good as the thing that produced it. A harness that cannot fail, a probe out of calibration, a fixture with a worn pogo pin, and an LLM judge that grades everything 4 out of 5 all print confident numbers.

Prove the instrument before you trust its verdict:

- **Test harnesses and suites.** Show the check fails when the behavior is broken: a known-bad build, a planted mutant (**mutation-check**), or a deliberately wrong expected value. A suite that has never failed is unproven, not healthy.
- **Physical measurements.** The instrument is calibrated (in date, traceable) and its resolution is at least ten times finer than the tolerance it judges. Measurement variation is small next to the tolerance: a gauge R&R under 10% of tolerance or process variation is acceptable, 10% to 30% needs a reasoned decision, over 30% is not fit for accept or reject decisions.
- **Production and end-of-line test.** Verify the station daily with a golden unit (known good) and a limit sample or seeded fault (known bad). Correlate stations against each other. Track false-fail and escape rates.
- **Rigs, fixtures, and benches.** A doctor check before each campaign: right firmware on the controller, connections verified, power and instruments in expected state. A fixture fault is its own failure class, not a product defect.
- **Graders and monitors.** Calibrate a model-graded rubric against human labels. Check that an alert fires on an injected fault. Check that logs and traces are not sampled away for the case you care about.
- **Clocks and timestamps.** Synchronize them across the systems you correlate, or state the skew.

When a result surprises you, or passes too easily, suspect the observation method before the system. When the instrument cannot be proven, the verdict is `INCONCLUSIVE`, whatever it printed.
