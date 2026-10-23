---
name: mutation-check
description: "Test the tests. Plant targeted faults in the behavior a test or suite claims to protect, run the tests, and report which faults survive. Use before calling new or AI-generated tests done, when auditing a suite's real strength, or when asked whether tests would actually catch a bug. Never commits a mutant."
---

# Mutation check

A test earns trust by failing when the behavior breaks. This skill breaks the behavior on purpose and watches. It follows the targeted approach Meta reported for mutation-guided test generation (Foster et al., FSE 2025): a few faults chosen for the risk you care about, not every possible mutant.

## Safety

- Work in a separate git worktree or a stash-protected scratch branch. Never leave a mutant in the working tree, never commit one, and never push one.
- Restore after each mutant and confirm `git diff` is clean before the next one.
- Hardware and firmware: mutate in simulation or on a rig unit allocated for it, never on units others are testing.

## Steps

1. **Pick the target.** The behavior the tests claim to protect, the risk behind it, and the tests that should catch a break. Name the oracle each test uses.
2. **Design 3 to 10 mutants** that model realistic faults for that risk:
   - boundary shifts (`<` to `<=`, off-by-one on limits)
   - wrong constant or unit (rounding mode, currency, timeout)
   - dropped side effect (skip the write, the event, the notification)
   - duplicated side effect (charge twice, send twice)
   - inverted or removed condition (permission check, validation, feature flag)
   - swallowed error or wrong error type
   - stale data (skip a cache invalidation, read before write)
   - for firmware: skipped watchdog kick, missing CRC check, wrong register bit
3. **For each mutant:** apply it, run the tests that should catch it with the same command CI uses, record killed (a test failed for the predicted reason) or survived, and revert. A test that fails for an unrelated reason (a compile error, a crash in setup) has not killed the mutant.
4. **Judge survivors.** A survivor is either a missing or weak test, or an equivalent mutant (the change does not alter observable behavior). Argue equivalence explicitly. When in doubt, it is a gap.
5. **Close the gaps** through the **Automate** playbook: strengthen the oracle or add the missing case, then rerun that mutant to show it is now killed.

Mutation testing tools (for example PIT, Stryker, mutmut, cargo-mutants) are a fine engine for step 3 when the project already has one. Keep the targeting of step 2.

## Report

| Mutant | Location | Fault it models | Result | Killing test or gap |
|--------|----------|-----------------|--------|---------------------|

Plus the kill ratio, the survivors judged equivalent with the argument, and the tests added or strengthened.
