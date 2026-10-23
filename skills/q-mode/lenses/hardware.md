# Lens: hardware

## Artifact identity
Hardware revision, build phase, serial numbers, lot, component suppliers, and the firmware on each unit.

## Stimulus and observation
Electrical stimulus (supply, signals, load), environment (temperature, humidity, vibration, shock, drop, ingress), and use cycles. Observe with meters, scopes, gauges, thermal cameras, and chamber logs.

## Instruments and trust
Use calibrated instruments (in date, traceable). Instrument resolution must be at least one tenth of the tolerance. Gauge R&R must be within limits. Verify the fixtures. See `../references/reliability-stats.md`.

## Variation and sampling
Results vary with unit-to-unit and lot-to-lot variation, component tolerance, and environmental corners. A zero-failure reliability claim needs a success-run sample size. Destructive tests use up units, so allocate the units before the build.

## Cost and reversibility
Units, chamber time, and lab time are expensive. Destructive tests are irreversible by design. For safety hazards (mains voltage, lithium cells under stress, lasers, moving parts), follow the rules of the lab.

## Oracle sources
Product specification, component datasheets, derating rules, and test standards (environmental, EMC, safety).

## Gates and standards
Engineering validation (EVT): the design works on early builds. Design validation (DVT): production-intent units meet every specification, including environmental, reliability, safety, and regulatory specifications. Production validation (PVT): the line builds the product consistently at rate and yield. Common standards: IEC 60068 (environmental), CISPR and IEC 61000 (EMC), IEC 62368-1 (safety), IP ratings (IEC 60529).

## Layer ladder
Simulation and design review → component characterization → board bring-up → system integration → environmental and reliability → certification → field returns analysis.

## Typical risks
These risks are typical:
- thin margins at temperature or voltage corners
- thermal runaway
- connector and solder fatigue
- EMC failures late in the program
- supplier substitutions
- tolerance stack-up
- ingress
- drop damage
- wear-out

## Failure classes
Unit or sample defect (assembly, component, handling damage), rig, fixture, or instrument fault, and test-method error (wrong profile or setup).

## Playbook notes
- **Test plan:** write the design verification plan and report as one table. The columns are: requirement, method, standard, acceptance criteria, sample size and reason, unit allocation, owner, result.
- **Test campaign:** characterize margins before you certify. Where the design is new, run discovery tests to failure (HALT). HALT finds weak links. It is not a pass or fail demonstration.
- **Gate review:** do failure analysis to root cause for every failure. Verify its fix on new units before the gate.
