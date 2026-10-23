---
name: test-review
description: "Review test code, test cases, or a test plan for whether it deserves trust: oracle strength, behavior versus implementation, determinism, data isolation, layer choice, readability, and evidence. Use for reviewing tests in a diff, reviewing AI-generated tests, auditing a suite sample, or when the qstack:test-reviewer agent runs. Reports findings with severity and file references, and does not edit."
---

# Test review

Review in a fresh context, as someone who did not write the tests. The question for every test is one sentence: would this fail if the behavior it names broke, and pass when only the internals change?

## Inputs

The diff or files, the requirement or contract each test claims to cover, and the oracle sources. When the author did not provide oracle sources, finding them is part of the review.

## Rubric

Work through each test. `references/test-smells.md` lists the smells with examples.

1. **Oracle.** Is the expected value derived from a named source, or copied from running the code? Is the assertion as strong as the contract (status, body, state change, side effect)? Snapshot or golden files reviewed for intent, not just accepted?
2. **Would it catch a break?** Imagine the behavior broken: wrong value, missing effect, double effect, wrong permission. When the test would still pass, that is a blocking finding. Run a **mutation-check** when you can.
3. **Implementation coupling.** Assertions on private calls, call order, internal data, or exact wording nobody reads.
4. **Determinism.** Fixed sleeps, unseeded randomness, wall-clock time, order dependence, real network where a boundary stub belongs, missing waits on asynchronous state.
5. **Isolation.** Shared mutable data, records it did not create, cleanup that can mask failure, collisions under parallel runs.
6. **Layer.** Could a cheaper layer catch the same risk? Is a rule permutation sitting in an end-to-end test?
7. **Coverage of the claim.** Negative, boundary, and error cases the contract names. Roles. A happy path alone is not coverage of a rule.
8. **Readability.** The name states the behavior and condition. Arrange, act, assert are visible. Helpers hide noise, not the assertion.
9. **Evidence.** Was it run, and seen to fail? Commands and counts reported?
10. **Safety.** Destructive operations against shared environments, real people contacted, secrets in code or logs.

## Severity

- **Blocking:** the test cannot detect the failure it claims to cover, or it is unsafe.
- **Major:** it will flake, couple to internals, or miss a named case of the contract.
- **Minor:** readability, naming, layer placement with low cost.

Do not report style preferences as findings. Do not inflate severity: an over-reported review gets ignored.

## Output

One table: test, finding, severity, evidence (`file:line` and the reasoning or the mutant that survived), and the suggested fix. Then a one-paragraph verdict: trust as is, trust after fixes, or do not trust. Do not edit files.
