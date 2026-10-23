---
name: principle-explain-the-number
description: "Apply before you trust, report, or act on a measured number: latency, throughput, capacity, a speedup or regression, a yield, a reliability figure, an eval score, a coverage percentage. Name what limits it, and rule out that it measured something other than what you think."
user-invocable: false
---

# Explain the Number

A number without an explanation is a rumor with decimals. Before it goes into a report or a decision, answer two questions.

**What limits it?** Name the bottleneck or the dominant factor with evidence taken during the run: CPU, memory, a lock, a connection pool, the disk, the network, a dependency's rate limit, the load generator itself, a thermal limit, a station's cycle time, a grader's ceiling. A guess from reading the code or the schematic is not a limiter. If you cannot say why the number is not twice as good, you do not know what you measured.

**What else could it be measuring?** List the alternatives and rule each out with evidence:

- errors counted as fast responses, or failures counted as passes
- cached, skipped, or short-circuited work
- code, hardware, or a path that never ran
- warm-up, cold start, or one-time effects
- the instrument's limit (generator saturation, gauge resolution, grader leniency)
- an untuned or unfair comparison (one side on defaults, different data, different conditions)
- noise: run-to-run, seed-to-seed, or unit-to-unit spread larger than the difference
- a piece too small to matter end to end

**Keep the evidence with the number:** sample size, spread, conditions, the limiter, and how to rerun it.

You skipped this when a reported number has no sample size, no spread, or no named limiter, or when a claimed improvement is larger than the share of time or cost the changed piece accounts for.

Distinct from **principle-evidence-not-claims**, which checks that a result is real. This checks that you understand it. Adapted from pstack's principle of the same name. See `NOTICE`.
