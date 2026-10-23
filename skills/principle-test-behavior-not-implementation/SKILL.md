---
name: principle-test-behavior-not-implementation
description: "Apply when you write, change, review, or keep a test. Assert what users of the code can observe, so the test fails when that behavior breaks and keeps passing when only the internals change."
user-invocable: false
---

# Test Behavior, Not Implementation

A test is a claim about what the code does for its users: a caller, an end user, or another service. Behavior is what those users can observe through the interface they use: return values, errors, state they can read back, and effects on systems outside the code, such as a request sent, a row written, or a message emitted. Implementation is everything they cannot observe: private helpers, internal call order, intermediate data, and which collaborator did the work.

Judge each test against two imagined edits:

- **Break the behavior.** Make the code return a wrong value, skip an effect, or do the effect twice. If the test still passes, it proves nothing. The usual causes are an assertion looser than the contract, an expected value computed by the code under test, and an assertion on data the test built itself.
- **Change the internals.** Keep every observable result and restructure the code underneath. If the test now fails, it is pinned to the implementation and will need a rewrite on every refactor while catching no bug.

Keep a test that catches the first edit and survives the second. Rewrite or delete the rest. Drive the code through its users' interface with concrete input, derive the expected value from the requirement, and assert what the contract promises, no less and no more.

The contract decides, not the assertion's shape. The payload a mocked external service receives is behavior, because that service observes it. A call to an internal helper is implementation. An exact error message pins wording no caller reads, while the error type callers branch on is the contract.

The **mutation-check** skill turns the first imagined edit into a real one.

Adapted from pstack's principle of the same name (MIT). See `NOTICE`.
