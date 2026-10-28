# Given/When/Then contract + self-check

Strict GWT removes interpretation. A machine can run a test case without a guess. A human also reads the same test case in the same way every time. These rules make "automate this later" a formatting change and not a rewrite.

## Given — preconditions

- **Fully expand.** Do not refer to other cases ("same as TC-3"). A reader must get the full starting state from this case alone.
- **Concrete UI/data state, not intent.** Write the observable state. For example, write "logged in as role A; the list shows 1 order #1234 with status=pending". Do not write "user is ready to confirm".
- **Omit backend-invisible state** that the tester cannot see or set. If it matters, put it in the environment and data plan of the scenario. Provision it there.

## When — operations

- **One step = one interaction.** Do not combine interactions ("enter credentials and log in" is three steps).
- **Approved verbs only.** A step must start with one of these verbs:
  `click / input / select / check / scroll / wait / navigate`
  For API-level cases, add: `request`.
  Each verb maps to a deterministic action. Any other verb hides ambiguity.
- Name the target by its visible label/role. State the value explicitly.

**Correct decomposition example:**
```
When:
  W1: input "Username" = "demo_user_a"        [Helper: form-input]
  W2: input "Password" = "[masked]"           [Helper: form-input]
  W3: click "Log in" button                  [Helper: login]
```

## Then — assertions

- **No vague words.** Ban: should / correct / works / as expected / normally, and their equivalents in the language of the team. `gwt_lint.py --banned` adds more.
  A machine cannot check these words, and they hide what "pass" means.
- **Map to an assertion.** Each `Then` states a fact that a person can check and the
  assertion that it maps to in the framework of the project (or, for API, status + JSON path).
- **Oracle for computed values.** Money/bonus/commission/quota assertions compare with the output of an oracle tool, three-way (`oracle == api == db`). Do not use a number that you typed by hand.

**Example:**
```
Then:
  T1: "Orders" list shows 1 row              → toHaveCount(1)
  T2: "Confirm" button visible              → toBeVisible
  T3: API total == calc_expected(#1234)     → oracle==api==db
```

## [Helper] labels

- Each `When`/`Then` step can have `[Helper: name]` from `<project>/helpers-inventory.md`.
- A labeled step is automatable now. An unlabeled step is honest natural language that waits for a helper. This gives partial automation, by design.
- Do not invent skill names. If a needed helper does not exist, leave the step unlabeled. List the proposed helper under "Proposed helpers" at the bottom of the case. The owner of the inventory adds it.

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

`gwt_lint.py` checks the mechanical subset (1, 2, 4, 5, 8). Items 3, 6, 7, 9, 10 need your judgment. Do them by hand before you present the case.
