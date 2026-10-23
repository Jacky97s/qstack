---
name: principle-evidence-not-claims
description: "Apply before reporting any test status, coverage, fix, or readiness. Verdicts rest on an executed run against the artifact under test, quoted and rerunnable. Proxies such as collect-only, compiling, a dry run, or green CI on another commit are NOT RUN."
user-invocable: false
---

# Evidence, Not Claims

A verdict is a claim someone will act on. Make it checkable.

**Vocabulary.** Use exactly these:

- `VERIFIED`: the check ran on the artifact under test and passed, and the check is known to detect the failure it targets.
- `FAILED`: the check ran and showed the predicted disagreement.
- `INCONCLUSIVE`: it ran, but the result does not decide the question (wrong environment, partial run, failure for an unrelated reason).
- `BLOCKED`: it could not run, and the blocker is named.
- `NOT RUN`: nothing executed. Collect-only, compiling, type-checking, linting, a dry run, "the test exists", and a subagent's say-so all land here.

**What counts as evidence.**

- The command, the commit or build identifier, the environment, the exit code, and the trimmed output showing counts and the decisive assertion.
- For a failure, the failure content: the diff between expected and actual. An exception, an empty result, and a real mismatch all print red, and only the predicted mismatch shows the test measures the bug.
- Proof of what was tested: commit SHA or image digest for software, firmware image hash and bootloader version for devices, hardware revision, serial numbers, and lot for physical units.
- Proof the instrument was fit: calibration status and date for physical measurements, and the station or rig identifier (**principle-trust-the-instrument**).
- Artifacts at a named path: traces, screenshots, videos, logs, reports.

**What does not.** Green CI on a different commit. A rerun that passed after a failure (that is a flake signal, see **principle-flaky-is-a-bug**). A screenshot without the state it claims. "Should work". Your own echo or a truncated `| tail -1`.

When verification itself fails, suspect the observation method before the system. Keep every claim's label in the same sentence: measured, inferred, or guess.
