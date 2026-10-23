### Test design

**You own the cases. Every case earns its place with a risk, an oracle, and a reason it can fail differently from its siblings.**

1. Size the input. Spec-driven work with goals already set runs the **shift-left** skill's Stages 4 to 6 (scenarios, environment and data, Given/When/Then cases with the lint), each stopping at its gate. Smaller work runs the steps below.
2. Name the behavior under test and its oracle source (**principle-oracle-first**). No oracle, no case. Record it as an open question instead.
3. Model the input and state space, and choose techniques by its shape with the **test-design-techniques** skill: partitions and boundaries for ranges, decision tables for rule combinations, state transitions for lifecycles, pairwise for configuration matrices, CRUD and permission matrices for resources, error guessing from defect history, and properties for invariants.
4. Cover the lenses: positive, negative, boundary, cross-role, and data integrity. Every happy path gets at least one negative and one boundary sibling. Every error the contract names gets a case.
5. Write each case with ID, purpose (the rule or risk), preconditions and data, steps, expected result from the oracle, priority, layer, and whether it is automatable. Use `references/templates/test-case.md` or the shift-left Given/When/Then format.
6. Prune cases that cannot fail differently from another case. Keep every boundary.
7. Build the coverage matrix: rules and risks against cases. Empty rows are gaps to fill or to accept explicitly.

**Reply:** the case table, the coverage matrix, open questions, and what is deliberately not covered and why.
