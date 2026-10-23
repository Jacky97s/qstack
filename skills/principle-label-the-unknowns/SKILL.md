---
name: principle-label-the-unknowns
description: "Apply when requirements, plans, test cases, or reports contain gaps, assumptions, or open questions. Every unknown must have a type, a state, an owner, and what it blocks. A bare TBD is not allowed."
user-invocable: false
---

# Label the Unknowns

An unlabeled gap becomes a silent assumption. Or it becomes a list of "to be confirmed" items that blocks everything and nothing. A label tells what kind of unknown it is, who can resolve it, and what exactly waits for it.

Each unknown is an open question with these fields (the format of the spec audit in `../q-mode/references/spec-audit.md`):

- **type:** `contradiction`, `gap`, `ambiguity`, `tbd`, `type-mismatch`, or `implicit-assumption`.
- **source:** where it came from, with a citation (`doc §section` vs `doc §section`, `file:line`, schema path).
- **blocks:** the specific downstream step or artifact that cannot continue. Use `none` when the unknown is only informational.
- **owner:** the role that can decide.
- **status:** `open`, `confirmed`, `resolved` (with the decision, its source, and date), `accepted-risk` (with who accepted it), or `wontfix`.

How you resolve an unknown is as important as the fact that you resolve it:

- **Resolved by an artifact:** cite the artifact. A schema, a snapshot, or the code (`file:line`) can answer a question that the spec left open. Check them before you ask a person.
- **Resolved by a person:** record who and when.
- **Proceeding on an assumption:** say so in the artifact. Keep the assumption reversible. Keep the question open.

Only the items that an unknown blocks must wait for it. Everything else continues.
