---
name: principle-reproduce-before-report
description: "Apply before claiming a defect exists, filing or drafting a bug report, or declaring a bug fixed. Reproduce it yourself on the closest surface, minimize it, and record the exact conditions. A defect you cannot reproduce is a lead, not a bug."
user-invocable: false
---

# Reproduce Before Report

An unreproducible report costs the team a guessing game and erodes trust in every later report.

- **Reproduce it yourself** on the surface where it was seen (the UI, the API, the CLI) by driving it, not by reading code. Asking someone else to reproduce is for when you cannot reach the surface, with the reason stated.
- **Record the conditions exactly.** Build or commit, environment, account and role, data, locale, device or browser, feature flags, and time in UTC.
- **Minimize.** Remove steps and data until removing anything more makes it disappear. Find the boundary: works with X, fails with Y.
- **Measure frequency.** n of m attempts. Intermittent defects get the flaky protocol.
- **Find when it started** when it is cheap: the last good build, or a bisect.
- **Separate observation from interpretation.** Actual behavior, expected behavior with its oracle source, and a labeled guess at cause.
- **When it will not reproduce,** report `INCONCLUSIVE` with everything you tried and what would make it reproducible. Do not file it as confirmed.
- **A fix is verified by the original repro,** run on the same surface, not by a new unit test alone.
