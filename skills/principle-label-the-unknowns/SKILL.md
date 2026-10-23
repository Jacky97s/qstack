---
name: principle-label-the-unknowns
description: "Apply when requirements, plans, test cases, or reports contain gaps, assumptions, or open questions. Every unknown carries a type, a state, an owner, and what it blocks. A bare TBD is not allowed."
user-invocable: false
---

# Label the Unknowns

An unlabeled gap turns into either a silent assumption or a list of "to be confirmed" items that blocks everything and nothing. A label says what kind of unknown it is, who can resolve it, and exactly what waits on it.

Each unknown is an open question with these fields (the format of the spec audit in `../q-mode/references/spec-audit.md`):

- **type:** `contradiction`, `gap`, `ambiguity`, `tbd`, `type-mismatch`, or `implicit-assumption`.
- **source:** where it came from, cited (`doc §section` vs `doc §section`, `file:line`, schema path).
- **blocks:** the specific downstream step or artifact that cannot proceed, or `none` when it is informational.
- **owner:** the role that can decide.
- **status:** `open`, `confirmed`, `resolved` (with the decision, its source, and date), `accepted-risk` (with who accepted it), or `wontfix`.

How it is resolved matters as much as that it is resolved:

- **Resolved by an artifact:** cite it. A schema, a snapshot, or the code (`file:line`) can answer a question the spec left open. Check them before asking a person.
- **Resolved by a person:** record who and when.
- **Proceeding on an assumption:** say so in the artifact, keep it reversible, and keep the question open.

Only the items an unknown blocks wait for it. Everything else proceeds.
