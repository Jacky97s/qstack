---
name: principle-reproduce-before-report
description: "Apply before you claim that a defect exists, file or draft a bug report, or declare a bug fixed. Reproduce it yourself on the closest surface, minimize it, and record the exact conditions. A defect that you cannot reproduce is a lead, not a bug."
user-invocable: false
---

# Reproduce Before Report

A report that nobody can reproduce makes the team guess. It also reduces trust in every later report.

- **Reproduce it yourself** on the surface where you saw it (the UI, the API, the CLI). Drive the surface. Do not only read code. Ask someone else to reproduce it only when you cannot reach the surface, and state the reason.
- **Record the conditions exactly.** Record the build or commit, environment, account and role, data, locale, device or browser, feature flags, and time in UTC.
- **Minimize.** Remove steps and data until the defect disappears if you remove anything more. Find the boundary: works with X, fails with Y.
- **Measure frequency.** Record n of m attempts. Use the flaky protocol for intermittent defects.
- **Find when it started** when this is cheap: the last good build, or a bisect.
- **Separate observation from interpretation.** Give the actual behavior, the expected behavior with its oracle source, and a labeled guess at the cause.
- **When it does not reproduce,** report `INCONCLUSIVE`. Give everything that you tried and what can make it reproducible. Do not file it as confirmed.
- **Verify a fix with the original repro,** run on the same surface. A new unit test alone is not enough.
