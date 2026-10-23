### Production quality

**You own whether the line ships good units. Control the process, and prove the test station can catch a bad one.**

For manufacturing lines, assembly, end-of-line test, incoming inspection, and any repeated process with a specification.

1. Map the process from incoming material to shipment: each step, its specification, its controls, and where defects can enter. Use a process FMEA (the **Risk analysis** playbook) when none exists.
2. Incoming inspection: sampling plans by attribute (AQL tables, ISO 2859-1 or equivalent) for supplier lots, with the inspection level and AQL chosen by risk. AQL accepts or rejects lots. It does not prove every unit is good.
3. In-process control: control charts on the parameters that predict defects, and capability (`Cpk`) against specification. React to out-of-control signals before units fail.
4. End-of-line test: list what it covers against the defect sources from step 1, and what it cannot see. Prove each station daily with a golden unit and a known-bad sample, correlate stations, and track false fails and escapes (**principle-trust-the-instrument**).
5. Traceability: serial, lot, station, operator or fixture, firmware image, and test results recorded for every unit, so a field failure can be traced to its batch.
6. Yield and escapes: first-pass yield per step, top failure modes by Pareto, and field returns traced back to the step that should have caught them.
7. Nonconformance: contain suspect units, analyze, correct, and verify the correction with data over a stated period (the **Escaped defect** playbook's 8D steps).

**Reply:** the process map with controls, capability and yield numbers with sample sizes, station verification status, coverage gaps of end-of-line test, and actions.
