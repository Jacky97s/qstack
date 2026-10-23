---
name: grill-the-plan
description: "Interview the operator about a test plan, test strategy, quality process, release decision, or validation plan. Ask one question at a time until every branch ends in a decision. Each question has a recommended answer and its reason. Use for 'grill me', to stress-test a QA plan or process proposal, or before you commit to a release-critical plan."
---

# Grill the plan

The direction of the plan is usually correct. The holes are in the parts that nobody checked to the end. These parts are: who does it, how it is checked, what happens when it fails, and who maintains it in six months. Find the holes before the plan reaches the team.

## How to ask

- **One question at a time.** When you ask several questions together, the hard question disappears. The hard question is usually the real one.
- **Every question has your recommended answer and the reason.** "Should we pilot it?" gives the work back to the operator. "I recommend a three-week pilot on the checkout suite, because it has the highest flake rate and a clear owner. Agree?" helps. The operator can answer "yes" and continue.
- **Do not ask again** a question that the operator already answered in this conversation or that the project profile records.
- **Ask for more detail when an answer is vague.** "The team will run it" is not an answer. "Who, how often, triggered by what, recorded where" is an answer.
- **Stop when the operator tells you to stop.** "I have thought this through, next" means ask the next question. The goal is a plan that holds. The goal is not to win.

## Dimensions to probe

Pick the three to five dimensions that are most likely to break this plan.

1. **Oracle.** For each item that the plan checks, how can anyone know that the result is correct?
2. **Risk and scope.** What is the riskiest part, and does the effort match it? What is out of scope, and who accepted that?
3. **Exit criteria.** Can someone check the conditions, and what happens when the team does not meet one on release day?
4. **Environments, rigs, and data.** Can someone provision them, who does it, and how long does it take? What is shared, and what can break for other people?
5. **Ownership and maintenance.** Who owns the tests, the rig, the station, and the eval set after the first month? What happens when that person leaves?
6. **Cost against value.** What does a run cost in time, money, units, or compute, and which decision does its result change?
7. **Failure handling.** When a check fails at the worst moment, who decides, with which information, and what is the default?
8. **Evidence.** Which artifact proves each claim later, to an auditor, a customer, or the next engineer?
9. **Pilot and exit.** How does the team try it on a small scale first, and which specific condition starts the full rollout or stops it?

## Closing

When the operator says enough, or every branch has reached an end, stop and summarize:

```
## Decided
- <decision>: <choice> because <one line>

## Still open
- <question>: <what blocks it>

## Next step
- <the first concrete action>
```

Do not build the artifacts of the plan here. That is a separate request.
