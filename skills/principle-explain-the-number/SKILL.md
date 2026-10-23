---
name: principle-explain-the-number
description: "Apply before you trust, report, or act on a measured number: latency, throughput, capacity, a speedup or regression, a yield, a reliability figure, an eval score, a coverage percentage. Name what limits it, and rule out that it measured something other than what you think."
user-invocable: false
---

# Explain the Number

A number without an explanation is a rumor with decimals. Before the number goes into a report or a decision, answer two questions.

**What limits it?** Name the bottleneck or the dominant factor. Use evidence that you took during the run. Possible limiters are:
- CPU
- memory
- a lock
- a connection pool
- the disk
- the network
- the rate limit of a dependency
- the load generator itself
- a thermal limit
- the cycle time of a station
- the ceiling of a grader

A guess from the code or the schematic is not a limiter. If you cannot say why the number is not twice as good, you do not know what you measured.

**What else can it measure?** List the alternatives. Use evidence to rule out each one:

- errors counted as fast responses, or failures counted as passes
- cached, skipped, or short-circuited work
- code, hardware, or a path that never ran
- warm-up, cold start, or one-time effects
- the limit of the instrument (generator saturation, gauge resolution, grader leniency)
- an untuned or unfair comparison (one side on defaults, different data, different conditions)
- noise: run-to-run, seed-to-seed, or unit-to-unit spread that is larger than the difference
- a piece that is too small to matter end to end

**Keep the evidence with the number:** sample size, spread, conditions, the limiter, and how to rerun it.

You skipped this step in two cases. In the first case, a reported number has no sample size, no spread, or no named limiter. In the second case, a claimed improvement is larger than the share of time or cost that the changed piece accounts for.

This principle is different from **principle-evidence-not-claims**. That principle checks that a result is real. This principle checks that you understand the result. Adapted from the principle of the same name in pstack. See `NOTICE`.
