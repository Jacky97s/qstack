### Release readiness

**You own the evidence. A human owns the decision.**

1. Gather the exit criteria from the plan, the test results, open defects by severity, quarantined and skipped tests, planned tests that did not run, and non-functional results.
2. Prove the tested artifact is the shipping artifact: commit SHA, build number, or image digest for every result you count. Results against a different build do not count.
3. Evaluate each exit criterion as `MET`, `NOT MET`, or `UNKNOWN`, with evidence.
4. List residual risk: untested areas, accepted known issues, quarantined tests and what they guard, and the mitigations in place (feature flags, staged rollout, rollback plan, monitoring).
5. Recommend `GO`, `GO WITH CONDITIONS` (each condition checkable), or `NO-GO`, with reasons. The release owner decides.
6. Define post-release checks: read-only production smoke for the critical journeys, the monitors and thresholds to watch, and who watches.

Use `references/templates/release-readiness.md`.

**Reply:** the recommendation first, then the criteria table, residual risk, and the post-release checks.
