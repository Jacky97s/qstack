### Escaped defect

**You own the gap that let it through. Be blameless, specific, and verified, and encode the lesson in structure.**

Use for a defect that reached users, the field, a customer, or a late stage. The steps follow the 8D discipline. It works for software incidents, firmware field failures, hardware returns, and process escapes.

1. **Team and description.** Name who works on it. Describe the problem in measurable terms: what, where, when, how many, and how you detected it. Separate facts from interpretation.
2. **Containment.** Stop the harm while the root cause is unknown. Use a flag off, a rollback, a hold on suspect lots, a customer notice, or sorting of stock. Containment treats the symptom and is temporary. Check that it works and causes no new harm.
3. **Root cause of occurrence.** Reproduce it (**principle-reproduce-before-report**). Trace the symptom to the first thing that went wrong. Use 5 whys, a cause and effect diagram, a fault tree, or failure analysis on returned units. Prove it: the problem appears when the cause is present, and it disappears when you remove the cause.
4. **Root cause of escape.** Walk each layer and ask why it did not catch the defect. The reasons can be:
   - no requirement
   - an unaudited requirement
   - a risk not identified
   - no case
   - a case with a weak oracle
   - a test not selected or not run
   - a flaky or quarantined test that people ignored
   - an environment or sample unlike the field
   - a station that cannot detect it
5. **Corrective actions** for both causes. Close the escape gap at the earliest layer that can catch the defect. Prove it: the new or strengthened check fails on the bad build, lot, or unit, and passes on the fix.
6. **Verify effectiveness** with a named measure over a stated period. Examples are zero recurrences in N weeks of field data, or the escape rate of a station.
7. **Prevent recurrence elsewhere.** Find siblings: the same fault pattern in other code, products, or lines, and the same gap in other suites. Encode the lesson in structure, not in a reminder. Structure can be a lint rule, a hook, a profile checklist item, a project playbook step, or a control plan or FMEA update.
8. **Close.** Write a blameless report: what happened, why it occurred, why it escaped, what changed, and the evidence that the change works.

**Reply:** the description, containment status, both root causes with their proof, the check that now catches it with its failing and passing evidence, effectiveness measure and period, siblings found, and the structural change.
