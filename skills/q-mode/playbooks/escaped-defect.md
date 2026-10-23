### Escaped defect

**You own the gap that let it through. Blameless, specific, verified, and encoded in structure.**

For a defect that reached users, the field, a customer, or a late stage. The steps follow the 8D discipline, which works for software incidents, firmware field failures, hardware returns, and process escapes alike.

1. **Team and description.** Name who works it. Describe the problem in measurable terms: what, where, when, how many, and how detected. Separate facts from interpretation.
2. **Containment.** Stop the harm while the root cause is unknown: a flag off, a rollback, a hold on suspect lots, a customer notice, or sorting stock. Containment treats the symptom and is temporary. Check it works and causes no new harm.
3. **Root cause of occurrence.** Reproduce it (**principle-reproduce-before-report**). Trace the symptom to the first thing that went wrong (5 whys, cause and effect diagram, fault tree, or failure analysis on returned units). Prove it: the problem appears when the cause is present and disappears when it is removed.
4. **Root cause of escape.** Walk each layer and ask why it did not catch it: no requirement, an unaudited requirement, a risk not identified, no case, a case with a weak oracle, a test not selected or not run, a flaky or quarantined test ignored, an environment or sample unlike the field, or a station that could not detect it.
5. **Corrective actions** for both causes. Close the escape gap at the earliest layer that would have caught it, and prove it: the new or strengthened check fails on the bad build, lot, or unit and passes on the fix.
6. **Verify effectiveness** with a named measure over a stated period, such as zero recurrences in N weeks of field data or the escape rate of a station.
7. **Prevent recurrence elsewhere.** Find siblings: the same fault pattern in other code, products, or lines, and the same gap in other suites. Encode the lesson in structure (a lint rule, a hook, a profile checklist item, a project playbook step, a control plan or FMEA update), not in a reminder.
8. **Close.** A blameless write-up: what happened, why it occurred, why it escaped, what changed, and the evidence that the change works.

**Reply:** the description, containment status, both root causes with their proof, the check that now catches it with its failing and passing evidence, effectiveness measure and period, siblings found, and the structural change.
