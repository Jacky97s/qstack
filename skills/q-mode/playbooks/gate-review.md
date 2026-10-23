### Gate review

**You own the evidence. A human owns the decision.**

For any decision point: a software release, an EVT, DVT, or PVT gate, a firmware rollout stage, a lot release, a model launch, or a certification submission.

1. Name the gate, the decision owner, and the criteria. Take the criteria from the plan, the active lenses' gates, and the governing standards.
2. Gather the evidence: results, open defects by severity, quarantined or skipped checks, planned checks that did not run, and non-functional results.
3. Prove the evidence is about the artifact being decided: commit, digest, image hash, hardware revision, serials, lot, dataset and checkpoint. Results for a different artifact do not count.
4. Evaluate each criterion as `MET`, `NOT MET`, or `UNKNOWN`, with evidence.
5. List residual risk: what was not tested, accepted known issues, quarantined checks and what they guard, and the mitigations in place (flags, staged rollout, rollback, containment, monitoring).
6. Recommend `GO`, `GO WITH CONDITIONS` (each condition checkable, with who verifies it), or `NO-GO`, with reasons. The decision owner decides.
7. Define the after-gate checks: read-only production smoke, monitors and thresholds, early field or line data to watch, and who watches.

Under the regulated lens, also assemble the evidence package its playbook notes describe.

**Reply:** the recommendation first, then the criteria table, residual risk, and the after-gate checks.
