---
name: principle-trust-the-instrument
description: "Apply before you trust any measurement, test harness, rig, fixture, grader, or monitor. Prove that the instrument can tell pass from fail: calibration and resolution for physical measurements, a known-bad input for test harnesses, a golden unit for production test, a labeled sample for graders. When a result surprises you, suspect the observation first."
user-invocable: false
---

# Trust the Instrument

A verdict is only as good as the thing that produced it. These all print confident numbers:
- a harness that cannot fail
- a probe out of calibration
- a fixture with a worn pogo pin
- an LLM judge that grades everything 4 out of 5

Prove the instrument before you trust its verdict:

- **Test harnesses and suites.** Show that the check fails when the behavior is broken. Use a known-bad build, a planted mutant (**mutation-check**), or a deliberately wrong expected value. A suite that never failed is unproven. It is not healthy.
- **Physical measurements.** The instrument must be calibrated (in date, traceable). Its resolution must be at least ten times finer than the tolerance that it judges. Measurement variation must be small next to the tolerance. A gauge R&R under 10% of tolerance or process variation is acceptable. At 10% to 30%, you need a reasoned decision. Over 30%, the instrument is not fit for accept or reject decisions.
- **Production and end-of-line test.** Verify the station each day with a golden unit (known good) and a limit sample or seeded fault (known bad). Correlate stations against each other. Track false-fail and escape rates.
- **Rigs, fixtures, and benches.** Do a doctor check before each campaign. Check that the controller has the right firmware, that the connections are verified, and that power and instruments are in the expected state. A fixture fault is its own failure class. It is not a product defect.
- **Graders and monitors.** Calibrate a model-graded rubric against human labels. Check that an alert fires on an injected fault. Check that sampling does not remove the logs and traces for the case that you care about.
- **Clocks and timestamps.** Synchronize them across the systems that you correlate, or state the skew.

When a result surprises you, or passes too easily, suspect the observation method before the system. When you cannot prove the instrument, the verdict is `INCONCLUSIVE`, whatever the instrument printed.
