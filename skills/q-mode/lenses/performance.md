# Lens: performance

## Artifact identity
Record these items:
- the build or image under test
- its configuration (pool sizes, limits, instance types, replicas)
- the dataset size and shape
- the load generator version and script

## Stimulus and observation
Generated load: arrival rate or concurrency, request mix, payload sizes, user think time. Observe latency distributions (p50, p95, p99, p99.9, max), throughput, and error rate by type. Observe saturation of CPU, memory, disk, network, connection pools, queues, and locks, on both the system and the load generator.

## Instruments and trust
The load generator is an instrument. Check that it is not the bottleneck (its own CPU, network, and connection limits). Record latency with full histograms. Do not use averages. When the question is user-facing latency, prefer open models (fixed arrival rate). A closed model has a fixed number of users who wait for responses. It sends less load as the system slows and hides the slow tail. This bias is called coordinated omission. Measure response time including queueing, not only service time.

## Variation and sampling
Results vary with warm-up, caches, JIT compilation, garbage collection, autoscaling, noisy neighbors, and background jobs. Discard warm-up explicitly, run several repetitions, and report the spread. Compare against a baseline that you measured in the same way.

## Cost and reversibility
Load against shared environments can stop the work of other people. It can also trigger alerts and rate limits, and cause third-party bills. Load or stress testing of any shared or external system needs written authorization of the target, time window, and rate.

## Oracle sources
Oracle sources are:
- service level objectives (for example p99 under 300 ms at 500 requests per second with under 0.1% errors)
- capacity requirements
- the baseline of the previous release

## Gates and standards
Performance budgets in CI for critical paths, a load test before releases that change capacity-relevant code, and capacity reviews before peak events.

## Layer ladder
Micro-benchmarks of hot code → single-service load → end-to-end system load in a production-like environment → shadow or replayed production traffic → production monitoring.

## Typical risks
These risks are typical:
- unbounded queues
- connection pool exhaustion
- lock contention
- N+1 queries
- cache stampedes
- retry storms
- memory leaks that you can see only in a soak
- dependencies with lower limits than the system under test

## Failure classes
Load generator saturation, environment that is not representative (size, data volume, network), warm-up contamination, measurement artifacts (averaging, coordinated omission), and a real capacity limit.

## Playbook notes
- **Test campaign:** run the scenario types that the question needs. Load: expected traffic. Stress: step up the load until the system breaks, and record how it fails and recovers. Spike: sudden bursts. Soak: hours at steady load, to find leaks and drift. Capacity: the highest load that still meets the SLO.
- **Every number:** apply **principle-explain-the-number**. Name the bottleneck with evidence. Rule out the generator, errors, and caching.
