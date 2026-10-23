### Requirements review

**You own testability. Find the defects in the spec before they become defects in code.**

Input is a story, PRD, SRS, API document, design, or change request.

1. Size the input. A full spec set (several documents, a data model, flows) runs the spec audit in `references/spec-audit.md`, the **Shift-left** playbook's Stage 0, with its three layers and script-verified coverage, and stops at its gate. A single story or small change runs the steps below.
2. Cross-check against every artifact that exists before reasoning about intent: the API schema or snapshot, the data model, existing code, existing tests, and past defects in the area. Confirm each claim the requirement makes about the system (method, path, field, enum, existing behavior). A requirement that contradicts the system is a finding, not an assumption to pick a side on.
3. Map rules and examples. For each rule write at least one concrete example, then the questions it raises (example mapping).
4. Probe each rule for testability: an observable outcome, a named oracle, explicit boundaries and limits, defined error behavior, complete states and transitions, roles and permissions, concurrency, data constraints (type, length, nullability, uniqueness, encryption at rest), time and timezone, and non-functional targets with numbers.
5. Record every finding as an open question with type, source, blocks, owner, and status (**principle-label-the-unknowns**). Resolve what an artifact can answer and cite it.
6. Rank the questions by what they block and by risk. Give each blocking question your recommended answer and why. In an interactive session, walk them with the **grill-the-plan** skill, one at a time.

**Reply:** testability verdict (ready, ready with open questions, not ready), the rules and examples table, open questions ranked with recommendations, and which ones block test design.
