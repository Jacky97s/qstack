# Test smells

| Smell | What it looks like | Why it hurts | Fix |
|-------|--------------------|--------------|-----|
| Tautological oracle | `expected = compute(x); assert compute(x) == expected` | The test cannot fail | Derive the expected value from the requirement |
| Status-only assertion | `assert resp.status == 200` for an endpoint that promises a body and a state change | The test misses wrong data and missing effects | Assert the contract: body fields, persisted state, emitted events |
| Assertion on own setup | Asserting the fixture the test just built | The test tests itself | Assert what the code produced |
| Snapshot rubber stamp | Large snapshots updated whenever they differ | The snapshot locks in whatever happened | Use small, reviewed snapshots, or explicit assertions |
| Mock everything | The unit under test talks only to mocks that return the expected answer | The test tests the mocks | Mock only at boundaries that the product already isolates |
| Implementation pin | Asserting private method calls or call order | Breaks on every refactor and catches no bug | Assert observable behavior |
| Fixed sleep | `sleep(2)`, `waitForTimeout(2000)` | The test is flaky and slow | Wait for the condition |
| Hidden dependency | Passes only after another test, or with a seeded record that a person created by hand | Failures depend on test order | Create and clean the test's own data |
| Swallowed failure | `try: ... except: pass` around the act, or assertions in a callback that never runs | The test passes without a signal | Let failures show. Assert that the callback ran |
| Conditional assertion | `if element.visible: assert ...` | The test passes when the condition is false | Assert the precondition, then the outcome |
| Retry-to-green | Loops that retry the whole test until it passes | Hides flakiness and real races | Fix the cause. Count each retry as a flake |
| Mystery guest | Data that loads from an unnamed file or environment | The test is hard to read and brittle | Build the data in the test or in a named factory |
| Eager test | One test checks many behaviors | One failure hides the others and the cause is not clear | One behavior per test |
| Vague expectation | "works correctly", "as expected" in a manual case | Nobody can check it | Use a concrete fact that a person can check |
| Exact wording pin | Asserting full error text that no caller reads | Breaks when someone edits the text | Assert the error type or code that callers use |
| Skipped without reason | `skip`, `xit`, `@Disabled` with no reason | Coverage is lost without a signal | Add the reason on the same line. A quarantine also needs a ticket, an owner, and an expiry. Or delete the test |
