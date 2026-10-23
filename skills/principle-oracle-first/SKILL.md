---
name: principle-oracle-first
description: "Apply before you write any test, test case, or bug report. Name where the expected result comes from (a contract, an invariant, a comparable, or a consistency heuristic) before you write a single step. Derive expected values from that source. Do not derive them by running the code under test."
user-invocable: false
---

# Oracle First

An oracle is how you decide that an observed result is right. A test without an oracle proves only that the code did not crash. Name the oracle first. Then write the steps that reach it.

Sources, strongest first:

1. **An explicit contract.** A spec clause, acceptance criterion, API schema, type, published default, or regulation. Cite it.
2. **An invariant that the result must satisfy.** Examples are:
   - round trip (`decode(encode(x)) == x`)
   - idempotence
   - conservation (debits equal credits)
   - ordering
   - monotonicity
   - permission (role R never sees field F)

   Invariants find bugs on inputs that nobody listed.
3. **An independent computation.** A reference implementation, a spreadsheet, or a separate oracle function. For computed values such as money, quotas, and balances, compare three ways: `oracle == api == db`.
4. **A comparable.** The previous version, a competitor, or another platform of the same product. A difference is a question. It is not automatically a bug.
5. **A consistency heuristic** when none of the above exists. Use HICCUPPS-F (`../q-mode/references/heuristics.md`): history, image, comparable products, claims, user expectations, product, purpose, statutes, familiar problems.

Rules:

- **Do not derive the expected value by running the code under test.** A snapshot of the current behavior locks in today's bugs. You can accept it only as a labeled characterization test that pins behavior before a refactor.
- **Assert as strongly as the contract promises.** `status == 200` alone is not an oracle when the contract promises more. The contract can promise a body, a state change, and a side effect.
- **When you cannot name an oracle,** the case is a requirements question. Record it as an open question (**principle-label-the-unknowns**). Do not guess an expected value.
- **Write the oracle source into the test or case** (`spec_ac`, a comment that names the invariant, or the oracle function). Then a reviewer can check the expectation without asking you.
