### Bug report

**You own the reproduction. A good report lets the fixer start at the cause.**

1. Reproduce it yourself on the closest surface (**principle-reproduce-before-report**). Record build or commit, environment, account and role, data, locale, device or browser, flags, and UTC timestamps.
2. Minimize: the fewest steps and the smallest data that still fail. Find the boundary between passing and failing inputs.
3. Measure frequency (n of m). Find the last good build or bisect when cheap.
4. Capture evidence: request and response, console and server logs, trace, screenshots or video, and IDs a developer can look up.
5. Assess impact: who is affected, how often, data or money at risk, workaround. Severity (impact) and priority (urgency) are separate fields.
6. Search for duplicates in the tracker and known-issue lists you can reach.
7. Write it in the tracker's format, or with these fields: title "[Area] what fails when condition", severity and priority with reasons, frequency, regression information, environment (build, environment, account and role, platform, flags, UTC time), minimal steps, expected, actual, evidence, and notes (boundary, workaround, labeled guess at cause, repro test). Expected behavior cites its oracle source. A guess at the cause is labeled as a guess.
8. Attach a failing regression test or an executable repro script when one is cheap. It is the fixer's first check.
9. Draft by default. File to the tracker only when the operator authorized filing.

When it will not reproduce, report `INCONCLUSIVE` with what you tried and what would help.

**Reply:** the report (or a link once filed), reproduction rate, severity and priority with reasons, and the attached repro.
