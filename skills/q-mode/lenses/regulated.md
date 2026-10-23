# Lens: regulated

This lens is an overlay for safety-related or regulated work. Stack it on top of the lens for the field of the product. This lens shows where to look. It does not restate any standard. Before you decide what a level requires, read the applicable clauses and the safety or regulatory plan of the project.

## Artifact identity
Configuration identities for every artifact: requirements, design, code, builds, test procedures, tools and their versions, and results. Keep tool qualification records where the standard requires them.

## Stimulus and observation
As in the underlying lens, plus reviews and analyses. In most regimes, these are verification activities.

## Instruments and trust
Use qualified or validated tools where the standard requires them. Use calibrated instruments. Keep the author and the verifier independent, at the level that the standard sets (**principle-author-is-not-approver**).

## Variation and sampling
As in the underlying lens. The standard or the notified body often prescribes sample sizes and statistical methods. Use theirs.

## Cost and reversibility
Evidence gaps that you find late delay certification. A change after verification needs an impact analysis and re-verification.

## Oracle sources
Requirements from the safety or risk analysis, the clauses of the standard, and the assigned integrity level.

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

Under the Digital Omnibus agreement of May 2026, EU AI Act obligations for standalone high-risk systems (Annex III) apply from 2 December 2027. For product-embedded systems (Annex I), they apply from 2 August 2028. Transparency obligations stayed on 2 August 2026. Confirm the dates in force before you rely on them. Sources also disagree on details, such as where MC/DC is mandatory and where it is recommended. The standard has priority. The safety plan of the project decides how the team applies it.

## Layer ladder
As in the underlying lens, with reviews and analyses at each level and the coverage criterion the level requires.

## Typical risks
These risks are typical:
- orphan requirements and orphan tests
- evidence tied to the wrong configuration
- missing independence
- unqualified tools
- changes without impact analysis
- anomalies that someone closed without a risk assessment

## Failure classes
Evidence gap, traceability break, configuration mismatch between evidence and the shipped artifact.

## Playbook notes
- **Gate review:** assemble the evidence package. It contains:
  - the plan
  - bidirectional traceability (requirement → design → verification → result → artifact)
  - results tied to configuration identities
  - coverage reports to the criterion of the level
  - review records
  - open anomalies with risk assessment
  - impact analyses for every change after verification

  Every claim must point at an artifact. Record each gap as a finding with an owner.
- **Test design:** keep verification (built right, against the specification) separate from validation (right thing, for the intended use). Both need evidence.
- For the testing part, the traceability table of the **Shift-left** playbook and `qa_status.py rtm --full` can hold the requirement-to-case chain.
