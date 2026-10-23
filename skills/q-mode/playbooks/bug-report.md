### Bug report

**You own the reproduction. A good report lets the fixer start at the cause.**

1. Reproduce it yourself on the closest surface (**principle-reproduce-before-report**). Record the build or commit, environment, account and role, data, locale, device or browser, flags, and UTC timestamps.
2. Minimize: use the fewest steps and the smallest data that still fail. Find the boundary between passing and failing inputs.
3. Measure the frequency (n of m). Find the last good build, or bisect when it is cheap.
4. Capture evidence: request and response, console and server logs, trace, screenshots or video, and IDs that a developer can look up.
5. Assess the impact: who is affected, how often, what data or money is at risk, and the workaround. Severity (impact) and priority (urgency) are separate fields.
6. Search for duplicates in the tracker and in the known-issue lists you can reach.
7. Write it in the format of the tracker, or with these fields:
   - title: "[Area] what fails when condition"
   - severity and priority, with reasons
   - frequency
   - regression information
   - environment (build, environment, account and role, platform, flags, UTC time)
   - minimal steps
   - expected result
   - actual result
   - evidence
   - notes (boundary, workaround, labeled guess at cause, repro test)

   The expected behavior cites its oracle source. Label a guess at the cause as a guess.
8. Attach a failing regression test or an executable repro script when it is cheap. It is the first check of the fixer.
9. Make a draft by default. File to the tracker only when the operator authorized filing.

When the defect does not reproduce, report `INCONCLUSIVE`. Say what you tried and what can help.

**Reply:** the report (or a link once filed), reproduction rate, severity and priority with reasons, and the attached repro.
