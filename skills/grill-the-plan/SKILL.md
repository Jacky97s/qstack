---
name: grill-the-plan
description: "Interview the operator one question at a time about a test plan, test strategy, quality process, release decision, or validation plan until every branch resolves into a decision. Each question comes with a recommended answer and its reason. Use for 'grill me', stress-testing a QA plan or process proposal, or before committing to a release-critical plan."
---

# Grill the plan

The plan's direction is usually right. The holes are in the parts nobody walked through to the end: who does it, how it is checked, what happens when it fails, and who maintains it in six months. Find them before the plan meets the team.

## How to ask

- **One question at a time.** Several at once lets the hard one disappear, and the hard one is usually the real one.
- **Every question carries your recommended answer and why.** "Should we pilot it?" hands work back. "I recommend a three-week pilot on the checkout suite, because it has the highest flake rate and a clear owner. Agree?" helps. The operator can answer "yes" and move on.
- **Do not re-ask** what the operator already answered in this conversation or what the project profile records.
- **Chase vague answers down one level.** "The team will run it" is not an answer. "Who, how often, triggered by what, recorded where" is.
- **Yield when told.** "I have thought this through, next" means next. The goal is a plan that stands up, not winning.

## Dimensions to probe

Pick the three to five most likely to break this plan.

1. **Oracle.** For each thing the plan checks, how will anyone know the result is right?
2. **Risk and scope.** What is the riskiest part, and is effort proportional to it? What is out of scope, and who accepted that?
3. **Exit criteria.** Are they checkable conditions, and what happens when one is not met on release day?
4. **Environments, rigs, and data.** Can they be provisioned, by whom, and how long does it take? What is shared, and what can break for others?
5. **Ownership and maintenance.** Who owns the tests, the rig, the station, the eval set after the first month? What happens when they leave?
6. **Cost against value.** What does a run cost in time, money, units, or compute, and what decision does its result change?
7. **Failure handling.** When a check goes red at the worst moment, who decides, with what information, and what is the default?
8. **Evidence.** What artifact proves each claim later, to an auditor, a customer, or the next engineer?
9. **Pilot and exit.** How is it tried small first, and what specific condition rolls it out or shuts it down?

## Closing

When the operator says enough, or every branch has converged, stop and summarize:

```
## Decided
- <decision>: <choice> because <one line>

## Still open
- <question>: <what blocks it>

## Next step
- <the first concrete action>
```

Do not start building the plan's artifacts here. That is a separate request.
