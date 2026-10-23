### Design the verification

**You own the method. When no playbook fits, design one from the core loop, write it down, then run it.**

Use for work that no other playbook covers, such as:
- a new kind of product
- an unusual quality question
- a mixed campaign across several fields
- a verification program that spans weeks

1. Frame the claim: what must be true, for whom, under which conditions, and what decision depends on it. Write the done condition as a falsifiable predicate.
2. Pick the lenses that apply. Fill each slot that no lens covers by answering it for this task. The slots are:
   - artifact identity
   - stimulus and observation
   - instruments and their trust
   - variation and sampling
   - cost and reversibility
   - oracle sources
   - gates and standards
   - the layer ladder
3. Rank the risks (**principle-risk-before-coverage**). Name the oracle for each (**principle-oracle-first**). Make each unknown a labeled open question (**principle-label-the-unknowns**).
4. Choose the cheapest layer that can show each risk (**principle-cheapest-layer-that-catches-it**). Choose the technique from the **test-design-techniques** skill.
5. Build or prove the instruments before the work:
   - the harness (the **create-harness** skill)
   - the baseline, captured from the current state
   - a known-bad case that each check must catch
6. Sequence the work into units that each end in a check. Do the riskiest unknowns first. Write the designed steps into the todolist. The operator reviews that list.
7. Run each unit as an experiment: hypothesis, smallest action, measure on the real artifact, keep or revert. Verdicts use the standard vocabulary. Inconclusive is not a pass.
8. When the same design is likely to recur, propose it as a project playbook in `.qstack/playbooks/`. When it is a new field, propose a new lens.

**Reply:** the claim and done predicate, the lenses and filled slots, the designed steps, results per unit with evidence, open questions, and whether the design must become a playbook or lens.
