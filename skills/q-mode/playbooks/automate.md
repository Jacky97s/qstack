### Automate

**You own trust in the suite. A test is done when it has been seen to fail, reviewed fresh, and proven stable.**

For new or changed automated tests, AI-generated batches, and exploratory paths graduating into scripts.

1. Read `.qstack/profile.md` and the existing suite: runner, fixtures, page objects or screen models, factories, markers or tags, naming, folder layout, and CI configuration. Follow them. Introduce a new framework, pattern, or dependency only with a stated reason.
2. Pick the layer for each risk (**principle-cheapest-layer-that-catches-it**).
3. Write the oracle first: assertions derived from the spec or contract (**principle-oracle-first**). Then the steps. Locate elements by role, label, or test id. Wait on conditions. Create and clean up the test's own data (**principle-deterministic-tests**, **principle-isolate-test-data**). Keep assertions out of page objects.
4. Run it for real, with the same command CI uses. Collect-only is `NOT RUN`.
5. Watch it fail. Run it against the original bug, or plant a mutant in the behavior it protects with the **mutation-check** skill. A test that stays green against a broken version gets a stronger oracle or gets deleted.
6. Prove stability. Run it N times (at least 5, at least 20 for end-to-end or anything parallel), in isolation and inside the full suite, in the parallel mode CI uses. Any non-pass goes to the **Flaky triage** playbook before merge.
7. Get a fresh review: spawn `qstack:test-reviewer` on the diff with the oracle sources. Fix each confirmed finding and rerun steps 4 to 6 for changed tests.
8. Hand off: the command to run, artifact paths, the stability counts, the mutants caught, and the cases left manual with the reason.

For AI-generated batches, every test passes steps 4 to 7 individually (**principle-author-is-not-approver**). For an exploratory path, graduate only steps that were stable across the session and carry the oracle the session used.

**Reply:** tests added or changed, oracle per test, stability counts, mutants caught and survived, reviewer findings and their dispositions, and the rerun command.
