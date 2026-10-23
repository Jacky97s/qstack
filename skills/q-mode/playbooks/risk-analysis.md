### Risk analysis

**You own the failure modes. Find how it can fail before choosing what to test.**

For a design, a feature, a process, or a system where structured risk analysis pays: anything safety-related, regulated, expensive to recall, or new. Produces an FMEA, a fault tree, or a hazard list that feeds the test plan.

1. Frame the scope: the item, its boundary, its interfaces, and the team that knows it. Choose the form: design FMEA for a product or software design, process FMEA for a manufacturing or operational process, a fault tree for one top-level event worth tracing downward, and hazard analysis when harm to people is possible.
2. Structure: break the item into elements (subsystems, components, software modules, or process steps) and the interfaces between them.
3. Functions: state what each element must do, with its requirement or specification.
4. Failure analysis: for each function, list failure modes (no function, partial, intermittent, unintended, degraded over time), their effects at the item and the user level, and their causes. Include software modes (wrong output, hang, crash, race, stale data, unsafe default) and human modes (misuse, wrong setup).
5. Risk: rate severity of the effect, occurrence of the cause given current prevention controls, and detection given current detection controls. Prioritize with the AIAG-VDA Action Priority logic (`references/reliability-stats.md`), severity first, rather than ranking by a multiplied RPN alone.
6. Optimization: for every high-priority row, choose a prevention action first and a detection action second. Each detection action becomes a planned test, inspection, or monitor with an owner, which goes into the **Test plan** playbook.
7. Close the loop: re-rate after actions are verified with evidence, and keep the analysis alive when the design, process, or field data changes.

**Reply:** the analysis table (element, function, failure mode, effect, cause, S/O/D, priority, action, owner), the high-priority rows first, and the tests and controls it adds to the plan.
