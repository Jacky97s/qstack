# Lens: regulated

An overlay for safety-related or regulated work. Stack it on top of the lens for the product's field. This lens points at where to look. It does not restate any standard. Read the applicable clauses and the project's safety or regulatory plan before deciding what a level requires.

## Artifact identity
Configuration identities for every artifact: requirements, design, code, builds, test procedures, tools and their versions, and results. Tool qualification records where the standard requires them.

## Stimulus and observation
As in the underlying lens, plus reviews and analyses, which count as verification activities in most regimes.

## Instruments and trust
Qualified or validated tools where required, calibrated instruments, and independence between author and verifier at the level the standard sets (**principle-author-is-not-approver**).

## Variation and sampling
As in the underlying lens. Sample sizes and statistical methods are often prescribed by the standard or the notified body. Use theirs.

## Cost and reversibility
Late evidence gaps delay certification. Changes after verification trigger impact analysis and re-verification.

## Oracle sources
Requirements derived from the safety or risk analysis, the standard's clauses, and the assigned integrity level.

## Gates and standards
| Field | Common standards | Levels | Usually matters for testing |
|-------|------------------|--------|-----------------------------|
| Automotive | ISO 26262, ISO 21448 (SOTIF), ISO/SAE 21434, Automotive SPICE | ASIL QM, A to D | Requirements-based testing, structural coverage rising with ASIL, fault injection, independence of confirmation measures |
| Aerospace | DO-178C, DO-254, DO-330 | DAL A to E | Requirements-based tests, structural coverage up to MC/DC at Level A, independent verification, tool qualification |
| Medical devices | IEC 62304, ISO 14971, IEC 60601, ISO 13485 | Software safety class A, B, C | Traceability from risk controls to verification, verification by class, software of unknown provenance, change control |
| Industrial | IEC 61508 and sector derivatives | SIL 1 to 4 | Technique tables by SIL, proof testing, diagnostic coverage |
| Rail | EN 50128, EN 50129 | SIL 0 to 4 | Independence of tester and verifier roles |
| AI systems | EU AI Act, NIST AI RMF, ISO/IEC 42001 | Risk categories | Risk management, data governance, accuracy and robustness, documentation, human oversight, post-market monitoring |
| Accessibility | WCAG 2.2, EN 301 549 | A, AA, AAA | Automated checks plus manual audit with assistive technology |
| Privacy | GDPR and sector rules | n/a | Data minimization in test data, consent, deletion and export rights |

Under the Digital Omnibus agreement of May 2026, EU AI Act obligations for standalone high-risk systems (Annex III) apply from 2 December 2027, and for product-embedded systems (Annex I) from 2 August 2028, while transparency obligations stayed on 2 August 2026. Confirm the dates in force before relying on them. Sources also disagree on details such as where MC/DC is mandatory versus recommended. The standard wins, and the project's safety plan decides how the team applies it.

## Layer ladder
As in the underlying lens, with reviews and analyses at each level and the coverage criterion the level requires.

## Typical risks
Orphan requirements and orphan tests, evidence tied to the wrong configuration, missing independence, unqualified tools, changes without impact analysis, and anomalies closed without risk assessment.

## Failure classes
Evidence gap, traceability break, configuration mismatch between evidence and the shipped artifact.

## Playbook notes
- **Gate review:** assemble the evidence package: the plan, bidirectional traceability (requirement → design → verification → result → artifact), results tied to configuration identities, coverage reports to the level's criterion, review records, open anomalies with risk assessment, and impact analyses for every change after verification. Every claim points at an artifact. Gaps are findings with owners.
- **Test design:** separate verification (built right, against the specification) from validation (right thing, for the intended use). Both need evidence.
- The **Shift-left** playbook's traceability table and `qa_status.py rtm --full` can carry the requirement-to-case chain for the testing part.
