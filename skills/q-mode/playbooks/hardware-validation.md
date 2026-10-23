### Hardware validation

**You own the evidence that a physical design meets its requirements, at its maturity gate, across its conditions.**

For electronics, mechanical parts, devices, and complete products moving through build phases.

1. Name the gate and what it must prove. Engineering validation (EVT): the design functions as intended on early builds. Design validation (DVT): production-intent units meet every specification, including environmental, reliability, safety, and regulatory requirements. Production validation (PVT): the line builds it consistently at rate and yield. Adapt the names to the team's own phases.
2. Write the design verification plan before the build: one row per requirement with the test method, standard referenced, acceptance criteria, sample size and its reasoning (**principle-measure-variation**), unit allocation (destructive tests consume units), and owner. The report is the same table with results, so plan and report stay one artifact.
3. Characterize before you certify: measure margins across corners (temperature, voltage, load, humidity, component tolerance) and find where it breaks. A pass at nominal is not a margin.
4. Run discovery tests to failure where the design is new: highly accelerated life testing finds weak links. It is a discovery tool, not a pass or fail demonstration.
5. Run the compliance tests to their standards: environmental (thermal, cycling, humidity, vibration, shock, drop, ingress), electrical (ESD, EMC, safety), and life or reliability with a stated acceleration model.
6. Prove the instruments and fixtures (**principle-trust-the-instrument**): calibration status, resolution against tolerance, and fixture verification.
7. Record identities: hardware revision, build, serials, lot, and the firmware on each unit.
8. Every failure gets failure analysis to root cause, and a fix verified on new units. A failure on one unit is data, not noise.
9. Decide at the gate: each requirement `MET`, `NOT MET`, or `UNKNOWN` with evidence, open issues with their risk, and a go, conditional, or no-go recommendation. The gate owner decides.

**Reply:** the gate, the requirement table with results and sample sizes, margins found, failures with their root causes, and the gate recommendation.
