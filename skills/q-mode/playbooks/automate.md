### Automate

**You own trust in the suite. A test is done when you have seen it fail, a fresh reviewer has reviewed it, and you have proven it stable.**

Use for new or changed automated tests, AI-generated batches, and exploratory paths that become scripts.

1. Read `.qstack/profile.md` and the existing suite: runner, fixtures, page objects or screen models, factories, markers or tags, naming, folder layout, and CI configuration. Follow them. Add a new framework, pattern, or dependency only with a stated reason.
2. Pick the layer for each risk (**principle-cheapest-layer-that-catches-it**).
3. Write the oracle first: assertions that come from the spec or contract (**principle-oracle-first**). Then write the steps. Wait on conditions. Create and clean up the own data of the test (**principle-deterministic-tests**, **principle-isolate-test-data**).
4. Run it for real, with the same command that CI uses. Collect-only is `NOT RUN`.
5. Watch it fail. Run it against the original bug, or plant a mutant in the behavior it protects with the **mutation-check** skill. When a test stays green against a broken version, give it a stronger oracle or delete it.
6. Prove stability. Run it N times (at least 5, and at least 20 for end-to-end tests or anything parallel). Run it in isolation and inside the full suite, in the parallel mode that CI uses. Send any non-pass to the **Flaky triage** playbook before merge.
7. Get a fresh review: start `qstack:test-reviewer` on the diff with the oracle sources. Fix each confirmed finding. Rerun steps 4 to 6 for the changed tests.
8. Hand off: the command to run, the artifact paths, the stability counts, the mutants caught, and the cases left manual with the reason.

For AI-generated batches, every test must pass steps 4 to 7 individually (**principle-author-is-not-approver**). For an exploratory path, convert only the steps that were stable across the session. Give them the oracle that the session used.

**Reply:** tests added or changed, oracle per test, stability counts, mutants caught and survived, reviewer findings and their dispositions, and the rerun command.
