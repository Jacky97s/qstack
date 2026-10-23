---
name: principle-evidence-not-claims
description: "Apply before you report any test status, coverage, fix, or readiness. A verdict must rest on an executed run against the artifact under test, quoted and rerunnable. Proxies such as collect-only, compiling, a dry run, or green CI on another commit are NOT RUN."
user-invocable: false
---

# Evidence, Not Claims

A verdict is a claim that someone will act on. Make it checkable.

**Vocabulary.** Use exactly these terms:

- `VERIFIED`: the check ran on the artifact under test and passed. The check is known to detect the failure it targets.
- `FAILED`: the check ran and showed the predicted disagreement.
- `INCONCLUSIVE`: the check ran, but the result does not decide the question. Examples are a wrong environment, a partial run, or a failure for an unrelated reason.
- `BLOCKED`: the check did not run because of a blocker. Name the blocker.
- `NOT RUN`: nothing executed. These all belong here: collect-only, compiling, type-checking, linting, a dry run, "the test exists", and the say-so of a subagent.

**What counts as evidence.**

- The command, the commit or build identifier, the environment, the exit code, and the trimmed output. The output must show the counts and the decisive assertion.
- For a failure, the content of the failure: the diff between expected and actual. An exception, an empty result, and a real mismatch all print red. Only the predicted mismatch shows that the test measures the bug.
- Proof of what you tested. Use the commit SHA or image digest for software. Use the firmware image hash and bootloader version for devices. For physical units, use the hardware revision, serial numbers, and lot.
- Proof that the instrument was fit. Give the calibration status and date for physical measurements. Give the station or rig identifier (**principle-trust-the-instrument**).
- Artifacts at a named path: traces, screenshots, videos, logs, reports.

**What does not count.** Green CI on a different commit does not count. A rerun that passed after a failure does not count (it is a flake signal, see **principle-flaky-is-a-bug**). A screenshot without the state it claims does not count. "Should work" does not count. Your own echo or a truncated `| tail -1` does not count.

When verification itself fails, suspect the observation method before the system. Keep the label of every claim in the same sentence: measured, inferred, or guess.
