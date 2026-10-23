# Lens: performance

## Artifact identity
The build or image under test, its configuration (pool sizes, limits, instance types, replicas), the dataset size and shape, and the load generator version and script.

## Stimulus and observation
Generated load: arrival rate or concurrency, request mix, payload sizes, user think time. Observe latency distributions (p50, p95, p99, p99.9, max), throughput, error rate by type, saturation of CPU, memory, disk, network, connection pools, queues, and locks, on both the system and the load generator.

## Instruments and trust
The load generator is an instrument. Check that it is not the bottleneck (its own CPU, network, and connection limits). Record latency with full histograms rather than averages. Prefer open models (fixed arrival rate) when the question is user-facing latency, because closed models (a fixed number of users waiting for responses) send less load as the system slows and hide the slow tail. This bias is called coordinated omission. Measure response time including queueing, not only service time.

## Variation and sampling
Warm-up, caches, JIT compilation, garbage collection, autoscaling, noisy neighbors, and background jobs. Discard warm-up explicitly, run several repetitions, and report spread. Compare against a baseline measured the same way.

## Cost and reversibility
Load against shared environments can take down other people's work and trigger alerts, rate limits, and third-party bills. Load or stress testing any shared or external system needs written authorization of target, time window, and rate.

## Oracle sources
Service level objectives (for example p99 under 300 ms at 500 requests per second with under 0.1% errors), capacity requirements, and the previous release's baseline.

## Gates and standards
Performance budgets in CI for critical paths, a load test before releases that change capacity-relevant code, and capacity reviews before peak events.

## Layer ladder
Micro-benchmarks of hot code → single-service load → end-to-end system load in a production-like environment → shadow or replayed production traffic → production monitoring.

## Typical risks
Unbounded queues, connection pool exhaustion, lock contention, N+1 queries, cache stampedes, retry storms, memory leaks visible only in soak, and dependencies with lower limits than the system under test.

## Failure classes
Load generator saturation, environment not representative (size, data volume, network), warm-up contamination, measurement artifacts (averaging, coordinated omission), and a real capacity limit.

## Playbook notes
- **Test campaign:** run the scenario types the question needs. Load: expected traffic. Stress: step up until it breaks, and record how it fails and recovers. Spike: sudden bursts. Soak: hours at steady load, for leaks and drift. Capacity: the highest load that still meets the SLO.
- **Every number:** apply **principle-explain-the-number**: name the bottleneck with evidence, and rule out the generator, errors, and caching.
