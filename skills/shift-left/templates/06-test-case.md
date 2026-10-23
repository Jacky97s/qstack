# <scenario_id> — <short title>

- **case_id:** <TC-...>
- **traces:** scenario <G1-S1> → goal <G1> → spec_ac <...>
- **priority:** <P0/P1/P2/P3>
- **automatable:** <T / partial / F>

## Given
- <fully expanded, concrete, observable precondition>
- <...>

## When
```
W1: <verb> "<visible target>" = "<value>"     [Helper: <name>]
W2: <verb> "<visible target>"                  [Helper: <name>]
```
> verbs: click / input / select / check / scroll / wait / navigate / request

## Then
```
T1: <checkable fact>                            → <toHaveText / toBeVisible / ...>
T2: <computed value>                            → oracle == api == db
```
> no vague words: should, correct, works, as expected, normally (or their equivalents in the team's language)

## Teardown
- <restore state if needed>

## Proposed helpers (if any step lacked one)
- <proposed-helper-name> — <what it would do> (for the helpers-inventory.md owner)
