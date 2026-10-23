---
name: principle-oracle-first
description: "Apply before writing any test, test case, or bug report. Name where the expected result comes from (a contract, an invariant, a comparable, or a consistency heuristic) before writing a single step, and derive expected values from that source, never from running the code under test."
user-invocable: false
---

# Oracle First

An oracle is how you decide that an observed result is right. A test without one only proves the code did not crash. Name the oracle first, then write the steps that reach it.

Sources, strongest first:

1. **An explicit contract.** A spec clause, acceptance criterion, API schema, type, published default, or regulation. Cite it.
2. **An invariant the result must satisfy.** Round trip (`decode(encode(x)) == x`), idempotence, conservation (debits equal credits), ordering, monotonicity, permission (role R never sees field F). Invariants catch bugs on inputs nobody listed.
3. **An independent computation.** A reference implementation, a spreadsheet, a separate oracle function. For computed values such as money, quotas, and balances, compare three ways: `oracle == api == db`.
4. **A comparable.** The previous version, a competitor, another platform of the same product. A difference is a question, not automatically a bug.
5. **A consistency heuristic** when nothing above exists. Use HICCUPPS-F (`../q-mode/references/heuristics.md`): history, image, comparable products, claims, user expectations, product, purpose, statutes, familiar problems.

Rules:

- **Never derive the expected value by running the code under test.** A snapshot of current behavior locks in today's bugs. It is acceptable only as a labeled characterization test that pins behavior before a refactor.
- **Assert as strongly as the contract promises.** `status == 200` alone is not an oracle when the contract promises a body, a state change, and a side effect.
- **When no oracle can be named,** the case is a requirements question. Record it as an open question (**principle-label-the-unknowns**) instead of guessing an expected value.
- **Write the oracle source into the test or case** (`spec_ac`, a comment naming the invariant, or the oracle function), so a reviewer can check the expectation without asking you.
