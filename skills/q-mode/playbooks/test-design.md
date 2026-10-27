### Test design

**You own the cases. Every case earns its place with a risk, an oracle, and a reason it can fail differently from its siblings.**

1. Size the input. A full spec set that needs traceable cases runs the **Shift-left** playbook. Smaller work runs the steps below.
2. Name the behavior under test and its oracle source (**principle-oracle-first**). No oracle, no case. Record it as an open question instead.
3. Model the input and state space. Choose techniques by its shape with the **test-design-techniques** skill:
   - partitions and boundaries for ranges
   - decision tables for rule combinations
   - state transitions for lifecycles
   - pairwise for configuration matrices
   - CRUD and permission matrices for resources
   - error guessing from defect history
   - properties for invariants
4. Cover the lenses: positive, negative, boundary, cross-role, and data integrity. Every happy path gets at least one negative sibling and one boundary sibling. Every error that the contract names gets a case.
5. Write each case with these fields:
   - ID
   - purpose (the rule or risk)
   - preconditions and data
   - steps
   - expected result from the oracle
   - priority
   - layer
   - whether it is automatable

   Use Given/When/Then per `references/gwt-rules.md` when you will automate the cases or hand them to someone else.
6. Prune the cases that cannot fail differently from another case. Keep every boundary.
7. Build the coverage matrix: rules and risks against cases. Fill each empty row with a case, or accept it explicitly as a gap.
8. Get a fresh review: start `qstack:test-reviewer` on the cases with the oracle sources (**principle-author-is-not-approver**). Fix each confirmed finding.

**Reply:** the case table, the coverage matrix, reviewer findings and their dispositions, open questions, and what you deliberately do not cover and why.
