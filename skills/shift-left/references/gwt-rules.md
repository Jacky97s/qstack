# Given/When/Then contract + self-check

The whole point of strict GWT is to remove interpretation. A test case that a
machine can run without guessing is also a test case a human reads the same way
every time. These rules exist so that "automate this later" is a formatting
change, not a rewrite.

## Given — preconditions

- **Fully expand.** No cross-references to other cases ("same as TC-3"). A
  reader must get the full starting state from this case alone.
- **Concrete UI/data state, not intent.** Write the observable state, e.g.
  "logged in as role A; the list shows 1 order #1234 with status=pending" — not "user is ready
  to confirm".
- **Omit backend-invisible state** the tester can't see or set. If it matters,
  it belongs in stage-3 test data and is provisioned there.

## When — operations

- **One step = one interaction.** Never bundle ("enter credentials and log in" is three steps).
- **Approved verbs only.** A step must start with one of:
  `click / input / select / check / scroll / wait / navigate`
  Plus, for API-level cases: `request`.
  Each maps to a deterministic action; anything else hides ambiguity.
- Reference the target by its visible label/role, and the value explicitly.

**Correct decomposition example:**
```
When:
  W1: input "Username" = "demo_user_a"        [Helper: form-input]
  W2: input "Password" = "[masked]"           [Helper: form-input]
  W3: click "Log in" button                  [Helper: login]
```

## Then — assertions

- **No vague words.** Ban: should / correct / works / as expected / normally, and their equivalents in the team's language (`gwt_lint.py --banned` adds more).
  These can't be checked mechanically and hide what "pass" means.
- **Map to an assertion.** Each `Then` states the checkable fact and the
  Playwright-style assertion it maps to: `toHaveText / toBeVisible /
  toBeChecked / toHaveURL / toHaveCount` (or, for API, status + JSON path).
- **Oracle for computed values.** Money/bonus/commission/quota assertions
  compare against an oracle tool's output, three-way (`oracle == api == db`),
  never a hand-typed number.

**Example:**
```
Then:
  T1: "Orders" list shows 1 row              → toHaveCount(1)
  T2: "Confirm" button visible              → toBeVisible
  T3: API total == calc_expected(#1234)     → oracle==api==db
```

## [Helper] labels

- Each `When`/`Then` step may carry `[Helper: name]` from `<project>/helpers-inventory.md`.
- A labeled step is automatable now; an unlabeled step is honest natural
  language pending a helper — partial automation, by design.
- Don't invent skill names. If a needed helper doesn't exist, leave the step
  unlabeled and list the proposed helper under "Proposed helpers" at the case
  bottom for the inventory owner to add.

## Self-check (run before lint, then `gwt_lint.py` confirms mechanically)

1. Does every `When` step contain exactly one interaction?
2. Does every `When` step start with an approved verb?
3. Is every `When` target referenced by a visible label, with an explicit value?
4. Does every `Then` avoid the banned vague words?
5. Does every `Then` map to a concrete assertion?
6. Are computed-value `Then`s tied to an oracle (not a literal number)?
7. Is `Given` free of cross-references and backend-invisible state?
8. Are all `[Helper]` labels present in `helpers-inventory.md`?
9. Does the case trace to its `scenario_id` / `goal_id` / `spec_ac`?
10. Is `automatable` set honestly (T only if every step is labeled)?

`gwt_lint.py` checks the mechanical subset (1, 2, 4, 5, 8). Items 3, 6, 7, 9, 10
need your judgment — do them by hand before presenting.
