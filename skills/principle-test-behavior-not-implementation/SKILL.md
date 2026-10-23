---
name: principle-test-behavior-not-implementation
description: "Apply when you write, change, review, or keep a test. Assert what the users of the code can observe. Then the test fails when that behavior breaks and keeps passing when only the internals change."
user-invocable: false
---

# Test Behavior, Not Implementation

A test is a claim about what the code does for its users. A user is a caller, an end user, or another service. Behavior is what those users can observe through the interface they use. This includes:
- return values
- errors
- state that they can read back
- effects on systems outside the code, such as a request sent, a row written, or a message emitted

Implementation is everything that they cannot observe: private helpers, internal call order, intermediate data, and which collaborator did the work.

Judge each test against two imagined edits:

- **Break the behavior.** Make the code return a wrong value, skip an effect, or do the effect twice. If the test still passes, it proves nothing. The usual causes are:
  - an assertion that is looser than the contract
  - an expected value that the code under test computed
  - an assertion on data that the test built itself
- **Change the internals.** Keep every observable result and restructure the code underneath. If the test now fails, it is pinned to the implementation. It will need a rewrite at every refactor and it finds no bug.

Keep a test that catches the first edit and survives the second edit. Rewrite or delete the other tests. Drive the code through the interface of its users with concrete input. Derive the expected value from the requirement. Assert what the contract promises, no less and no more.

The contract decides. The shape of the assertion does not decide. The payload that a mocked external service receives is behavior, because that service observes it. A call to an internal helper is implementation. An exact error message pins wording that no caller reads. The error type that callers branch on is the contract.

The **mutation-check** skill turns the first imagined edit into a real edit.

Adapted from the principle of the same name in pstack (MIT). See `NOTICE`.
