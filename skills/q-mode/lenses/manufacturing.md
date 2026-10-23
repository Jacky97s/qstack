# Lens: manufacturing

## Artifact identity
Serial, lot, line, station, fixture, operator or shift, material lots, and the firmware or program loaded at each step.

## Stimulus and observation
In-process measurements, end-of-line functional test, visual and automated optical inspection, and audits of finished goods. Observe through station logs, measurement records, and yield data.

## Instruments and trust
Stations, gauges, and fixtures. Verify each station daily with a golden unit and a known-bad sample, correlate stations against each other, and track false-fail and escape rates. Gauge R&R within limits.

## Variation and sampling
Process variation over time, shifts, material lots, and tool wear. Use control charts and capability (`Cpk`) for variables, and attribute sampling plans (AQL, ISO 2859-1) for lots.

## Cost and reversibility
Stopping a line, scrapping material, and recalling shipped units are expensive. Containment holds and customer notices are outward-facing decisions for the operator.

## Oracle sources
Drawings and specifications, control plans, work instructions, golden units, and limit samples.

## Gates and standards
First article inspection, production part approval, lot release, outgoing quality audit. Common standards: ISO 9001, IATF 16949 (automotive), ISO 13485 (medical), ISO 2859-1 (sampling).

## Layer ladder
Supplier quality and incoming inspection → in-process controls and SPC → end-of-line test → outgoing quality audit → field returns.

## Typical risks
End-of-line test that cannot see a defect source, station drift, supplier changes, untraceable rework, operator-dependent steps, and processes running with `Cpk < 1.33`.

## Failure classes
Station or fixture fault, measurement system error, material or supplier lot defect, process out of control, and handling damage.

## Playbook notes
- **Risk analysis:** use a process FMEA over the process map, from incoming material to shipment.
- **Suite audit:** for a production line, the suite is the set of stations and inspections. Audit what each step covers against the defect sources, and what nothing covers.
- **Escaped defect:** trace each field return to its lot and to the step that should have caught it. Containment of suspect lots comes first.
