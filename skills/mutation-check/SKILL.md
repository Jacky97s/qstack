---
name: mutation-check
description: "Test the tests. Plant targeted faults in the behavior that a test or suite claims to protect, run the tests, and report which faults survive. Use before you call new or AI-generated tests done, when you audit the real strength of a suite, or when someone asks if tests can catch a bug. Never commits a mutant."
---

# Mutation check

A test earns trust when it fails after the behavior breaks. This skill breaks the behavior on purpose and observes the result. It follows the targeted approach that Meta reported for mutation-guided test generation (Foster et al., FSE 2025). Choose a few faults for the risk that you care about. Do not use every possible mutant.

## Safety

- Work in a separate git worktree or a stash-protected scratch branch. Do not leave a mutant in the working tree. Do not commit a mutant. Do not push a mutant.
- Restore the code after each mutant. Make sure `git diff` is clean before the next mutant.
- Hardware and firmware: mutate in simulation or on a rig unit that is allocated for it. Do not mutate units that other people are testing.

## Steps

1. **Pick the target.** Find the behavior that the tests claim to protect, the risk behind it, and the tests that must catch a break. Name the oracle that each test uses.
2. **Design 3 to 10 mutants** that model realistic faults for that risk:
   - boundary shifts (`<` to `<=`, off-by-one on limits)
   - wrong constant or unit (rounding mode, currency, timeout)
   - dropped side effect (skip the write, the event, the notification)
   - duplicated side effect (charge twice, send twice)
   - inverted or removed condition (permission check, validation, feature flag)
   - swallowed error or wrong error type
   - stale data (skip a cache invalidation, read before write)
   - for firmware: skipped watchdog kick, missing CRC check, wrong register bit
3. **For each mutant:** apply the mutant and run the tests that must catch it. Use the same command that CI uses. Record the result as killed (a test failed for the predicted reason) or survived. Then revert the mutant. A test that fails for an unrelated reason (a compile error, a crash in setup) has not killed the mutant.
4. **Judge survivors.** A survivor is a missing or weak test, or an equivalent mutant (the change does not alter the observable behavior). State the argument for equivalence explicitly. If you are not sure, treat it as a gap.
5. **Close the gaps** through the **Automate** playbook: strengthen the oracle or add the missing case. Then run that mutant again to show that a test now kills it.

Mutation testing tools (for example PIT, Stryker, mutmut, cargo-mutants) are a good engine for step 3 when the project already has one. Keep the targeting of step 2.

## Report

| Mutant | Location | Fault it models | Result | Killing test or gap |
|--------|----------|-----------------|--------|---------------------|

Add the kill ratio, the survivors that you judged equivalent (with the argument), and the tests that you added or strengthened.
