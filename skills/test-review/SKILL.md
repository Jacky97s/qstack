---
name: test-review
description: "Review test code, test cases, or a test plan to decide if it deserves trust. Checks oracle strength, behavior versus implementation, determinism, data isolation, layer choice, readability, and evidence. Use to review tests in a diff, review AI-generated tests, audit a suite sample, or when the qstack:test-reviewer agent runs. Reports findings with severity and file references. Does not edit."
---

# Test review

Review in a fresh context, as a person who did not write the tests. Ask one question for every test. Does the test fail when the behavior that it names breaks, and pass when only the internals change?

## Inputs

The inputs are the diff or files, the requirement or contract that each test claims to cover, and the oracle sources. If the author did not give oracle sources, you must find them. This is part of the review.

## Rubric

Check each test. `references/test-smells.md` lists the smells with examples.

1. **Oracle.** Does the expected value come from a named source, or did the author copy it from a run of the code? Is the assertion as strong as the contract (status, body, state change, side effect)? Did a person review the snapshot or golden files for intent, or did they only accept them?
2. **Can it catch a break?** Imagine the behavior is broken: wrong value, missing effect, double effect, wrong permission. If the test still passes, that is a blocking finding. Run a **mutation-check** when you can.
3. **Implementation coupling.** Look for assertions on private calls, call order, internal data, or exact wording that nobody reads.
4. **Determinism.** Look for fixed sleeps, unseeded randomness, wall-clock time, order dependence, real network where a boundary stub belongs, and missing waits on asynchronous state.
5. **Isolation.** Look for shared mutable data, records that the test did not create, cleanup that can hide a failure, and collisions in parallel runs.
6. **Layer.** Can a cheaper layer catch the same risk? Does an end-to-end test hold a rule permutation?
7. **Coverage of the claim.** Check the negative, boundary, and error cases that the contract names. Check the roles. A happy path alone does not cover a rule.
8. **Readability.** The name states the behavior and the condition. The arrange, act, and assert steps are visible. Helpers hide noise, not the assertion.
9. **Evidence.** Did the author run the test and see it fail? Did the author report the commands and counts?
10. **Safety.** Look for destructive operations against shared environments, contact with real people, and secrets in code or logs.

## Severity

- **Blocking:** the test cannot detect the failure it claims to cover, or it is unsafe.
- **Major:** the test can flake, couples to internals, or misses a named case of the contract.
- **Minor:** readability, naming, or layer placement with low cost.

Do not report style preferences as findings. Do not make the severity higher than it is. People ignore an over-reported review.

## Output

Write one table with these columns: test, finding, severity, evidence (`file:line` and the reasoning or the mutant that survived), and the suggested fix. Then write a one-paragraph verdict: trust as is, trust after fixes, or do not trust. Do not edit files.
