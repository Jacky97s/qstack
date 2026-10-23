### Gate review

**You own the evidence. A human owns the decision.**

Use for any decision point, such as:
- a software release
- an EVT, DVT, or PVT gate
- a firmware rollout stage
- a lot release
- a model launch
- a certification submission

1. Name the gate, the decision owner, and the criteria. Take the criteria from the plan, the gates of the active lenses, and the governing standards.
2. Gather the evidence: results, open defects by severity, quarantined or skipped checks, planned checks that did not run, and non-functional results.
3. Prove that the evidence is about the artifact under decision: commit, digest, image hash, hardware revision, serials, lot, dataset, and checkpoint. Results for a different artifact do not count.
4. Evaluate each criterion as `MET`, `NOT MET`, or `UNKNOWN`, with evidence.
5. List the residual risk:
   - what you did not test
   - accepted known issues
   - quarantined checks and what they guard
   - the mitigations in place (flags, staged rollout, rollback, containment, monitoring)
6. Recommend `GO`, `GO WITH CONDITIONS`, or `NO-GO`, with reasons. Each condition of `GO WITH CONDITIONS` must be checkable, and you must say who verifies it. The decision owner decides.
7. Define the after-gate checks: read-only production smoke, monitors and thresholds, early field or line data to watch, and who watches.

Under the regulated lens, also assemble the evidence package that its playbook notes describe.

**Reply:** the recommendation first, then the criteria table, residual risk, and the after-gate checks.
