### Suite audit

**You own the truth about the suite. Find the false confidence first.**

A suite is any set of checks that the team relies on, such as:
- automated tests
- an eval set
- rig scripts
- the stations and inspections of a production line

1. Inventory:
   - tests by layer
   - runtime per layer
   - slowest tests
   - flake rate from CI history
   - skipped and quarantined tests with their age
   - tests that never failed in the history you can reach
2. Review a sample of the riskiest modules with the `qstack:test-reviewer` agent and the **test-review** rubric. Start with weak oracles and implementation-pinned tests.
3. Sample the critical paths with mutation, using the **mutation-check** skill. Each surviving mutant is a place where the suite claims protection that it does not give.
4. Find duplication (one behavior asserted at several layers), dead tests (they cover removed code or unreachable paths), and tests at the wrong layer.
5. Rank the recommendations by risk reduced per unit of effort. The actions are: strengthen an oracle, delete, merge, push down a layer, de-flake, or add a missing test for an uncovered high risk.

Report findings with evidence. Make changes only when the operator asks, through the **Automate** or **Flaky triage** playbook.

**Reply:** the health summary with numbers, surviving mutants, the top findings with file references, and the ranked recommendations.
