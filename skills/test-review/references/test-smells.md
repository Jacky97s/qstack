# Test smells

| Smell | What it looks like | Why it hurts | Fix |
|-------|--------------------|--------------|-----|
| Tautological oracle | `expected = compute(x); assert compute(x) == expected` | Cannot fail | Derive the expected value from the requirement |
| Status-only assertion | `assert resp.status == 200` for an endpoint that promises a body and a state change | Misses wrong data and missing effects | Assert the contract: body fields, persisted state, emitted events |
| Assertion on own setup | Asserting the fixture the test just built | Tests the test | Assert what the code produced |
| Snapshot rubber stamp | Large snapshots updated whenever they differ | Locks in whatever happened | Small, reviewed snapshots, or explicit assertions |
| Mock everything | The unit under test talks only to mocks configured to return the answer | Tests the mocks | Mock only at boundaries the product already isolates |
| Implementation pin | Asserting private method calls or call order | Breaks on every refactor, catches no bug | Assert observable behavior |
| Fixed sleep | `sleep(2)`, `waitForTimeout(2000)` | Flaky and slow | Wait for the condition |
| Hidden dependency | Passes only after another test, or with a seeded record someone created by hand | Order-dependent failures | Create and clean own data |
| Swallowed failure | `try: ... except: pass` around the act, or assertions in a callback that never runs | Silent pass | Let failures surface, assert the callback ran |
| Conditional assertion | `if element.visible: assert ...` | Passes when the condition is false | Assert the precondition, then the outcome |
| Retry-to-green | Loops that retry the whole test until it passes | Hides flakiness and real races | Fix the cause, count retries as flakes |
| Mystery guest | Data loaded from an unnamed file or environment | Unreadable, brittle | Build data in the test or a named factory |
| Eager test | One test checks many behaviors | One failure hides the others, unclear cause | One behavior per test |
| Vague expectation | "works correctly", "as expected" in a manual case | Cannot be checked | A concrete, checkable fact |
| Exact wording pin | Asserting full error text no caller reads | Breaks on copy edits | Assert the error type or code callers use |
| Skipped without reason | `skip`, `xit`, `@Disabled` with no ticket | Silent coverage loss | Reason and ticket, or delete |
