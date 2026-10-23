# Regulated and safety-related work

This page points at where to look. It does not restate any standard. Read the applicable clauses and the project's safety or regulatory plan before deciding what a level requires.

| Field | Common standards | Levels | Things that usually matter for testing |
|-------|------------------|--------|---------------------------------------|
| Automotive | ISO 26262 (functional safety), ISO 21448 (SOTIF), ISO/SAE 21434 (cybersecurity), Automotive SPICE | ASIL QM, A to D | Requirements-based testing, structural coverage rising with ASIL, fault injection, back-to-back testing of models and code, independence of confirmation measures |
| Aerospace | DO-178C (software), DO-254 (hardware), DO-330 (tools) | DAL A to E | Requirements-based tests, structural coverage up to MC/DC at Level A, independence of verification, tool qualification |
| Medical devices | IEC 62304 (software lifecycle), ISO 14971 (risk management), IEC 60601 (electrical safety), ISO 13485 (quality system), FDA guidance | Software safety class A, B, C | Traceability from risk controls to verification, unit and integration verification by class, software of unknown provenance, change control |
| Industrial | IEC 61508 and its sector derivatives | SIL 1 to 4 | Techniques tables by SIL, proof testing, diagnostic coverage |
| Rail | EN 50128, EN 50129 | SIL 0 to 4 | Independence of tester and verifier roles by SIL |
| Accessibility | WCAG 2.2, EN 301 549 | A, AA, AAA | Automated checks plus manual audit, assistive technology testing |
| Privacy and data | GDPR, sector rules | n/a | Data minimization in test data, consent flows, deletion and export rights |

Sources disagree on details such as where MC/DC is mandatory versus recommended. When a source and the standard disagree, the standard wins, and the project's safety plan decides how the team applies it.

## Evidence an auditor expects in most regimes

- A plan that states methods, levels, tools, and independence.
- Bidirectional traceability between requirements, design, tests, and results.
- Results tied to configuration identities of every artifact.
- Coverage reports to the criterion the level requires.
- Review and analysis records, not only test results.
- Anomaly records with risk assessment and disposition.
- Impact analysis and re-verification for every change after verification.
