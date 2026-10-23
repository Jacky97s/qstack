### Suite audit

**You own the truth about the suite. Find the false confidence first.**

1. Inventory: tests by layer, runtime per layer, slowest tests, flake rate from CI history, skipped and quarantined tests with their age, and tests that never failed in the history you can reach.
2. Sample review on the riskiest modules with the `qstack:test-reviewer` agent and the **test-review** rubric. Weak oracles and implementation-pinned tests come first.
3. Mutation sampling on the critical paths with the **mutation-check** skill. Each surviving mutant is a place the suite claims protection it does not give.
4. Find duplication (one behavior asserted at several layers), dead tests (covering removed code or unreachable paths), and tests at the wrong layer.
5. Rank recommendations by risk reduced per unit of effort: strengthen an oracle, delete, merge, push down a layer, de-flake, or add a missing test for an uncovered high risk.

Report findings with evidence. Make changes only when the operator asks, through the **Automate** or **Flaky triage** playbook.

**Reply:** the health summary with numbers, surviving mutants, the top findings with file references, and the ranked recommendations.
