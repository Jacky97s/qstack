### Compliance evidence

**You own an evidence package an auditor can follow from any requirement to its proof and back.**

For regulated or safety-related work: automotive, medical devices, aerospace, industrial safety, rail, finance, privacy, accessibility, or any domain with a standard the product must meet.

1. Identify the standards and the assigned integrity or safety level from the project's own safety or regulatory plan. Read the applicable clauses yourself. Do not rely on summaries for what a level requires. `references/regulated.md` lists where to look and what usually differs between standards.
2. Build the traceability chain: requirement → design element → verification activity → result → evidence artifact, in both directions. Every requirement has verification. Every test traces to a requirement. Orphans on either side are findings.
3. Separate verification (built right, against the specification) from validation (right thing, for the user and the intended use). Both need evidence.
4. Meet the method requirements of the level: requirements-based tests, the structural coverage criterion the standard sets (statement, branch, MC/DC), reviews and analyses, and the independence required between author and verifier (**principle-author-is-not-approver**).
5. Control what was verified: configuration identities of every artifact, tool versions, and tool qualification where the standard requires it.
6. Manage change: for every change after verification, an impact analysis that names what must be re-verified, and the re-verification evidence.
7. Package it: the plan, the traceability matrix, results, coverage reports, review records, open anomalies with their risk assessment, and the summary. Every claim points at an artifact.
8. Gaps are reported, not smoothed over. A missing piece of evidence is a finding with an owner (**principle-label-the-unknowns**).

The **shift-left** skill's `test-index.csv` and generated RTM can carry the traceability chain for the testing part.

**Reply:** the standards and levels, the traceability matrix summary with orphans, the method and coverage status against the level's requirements, open anomalies, and gaps.
