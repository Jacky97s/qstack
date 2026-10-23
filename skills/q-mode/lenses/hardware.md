# Lens: hardware

## Artifact identity
Hardware revision, build phase, serial numbers, lot, component suppliers, and the firmware on each unit.

## Stimulus and observation
Electrical stimulus (supply, signals, load), environment (temperature, humidity, vibration, shock, drop, ingress), and use cycles. Observe with meters, scopes, gauges, thermal cameras, and chamber logs.

## Instruments and trust
Calibrated instruments (in date, traceable), resolution at least one tenth of the tolerance, gauge R&R within limits, verified fixtures. See `../references/reliability-stats.md`.

## Variation and sampling
Unit-to-unit and lot-to-lot variation, component tolerance, environmental corners. A zero-failure reliability claim needs a success-run sample size. Destructive tests consume units, so allocate them before the build.

## Cost and reversibility
Units, chamber time, and lab time are expensive. Destructive tests are irreversible by design. Safety hazards (mains voltage, lithium cells under stress, lasers, moving parts) follow the lab's rules.

## Oracle sources
Product specification, component datasheets, derating rules, and test standards (environmental, EMC, safety).

## Gates and standards
Engineering validation (EVT): the design functions on early builds. Design validation (DVT): production-intent units meet every specification, including environmental, reliability, safety, and regulatory. Production validation (PVT): the line builds it consistently at rate and yield. Common standards: IEC 60068 (environmental), CISPR and IEC 61000 (EMC), IEC 62368-1 (safety), IP ratings (IEC 60529).

## Layer ladder
Simulation and design review → component characterization → board bring-up → system integration → environmental and reliability → certification → field returns analysis.

## Typical risks
Thin margins at temperature or voltage corners, thermal runaway, connector and solder fatigue, EMC failures late in the program, supplier substitutions, tolerance stack-up, ingress, drop damage, and wear-out.

## Failure classes
Unit or sample defect (assembly, component, handling damage), rig, fixture, or instrument fault, and test-method error (wrong profile or setup).

## Playbook notes
- **Test plan:** write the design verification plan and report as one table: requirement, method, standard, acceptance criteria, sample size and reason, unit allocation, owner, result.
- **Test campaign:** characterize margins before certifying. Run discovery tests to failure (HALT) where the design is new. HALT finds weak links and is not a pass or fail demonstration.
- **Gate review:** every failure has failure analysis to root cause, and its fix is verified on new units before the gate.
