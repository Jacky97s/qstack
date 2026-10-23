# Domains

qstack's principles hold in any field where something must meet a requirement and evidence decides whether it does. What changes between fields is the vocabulary, the layer ladder, and the instruments. Record the project's domain in `.qstack/profile.md`.

## Vocabulary

| Concept | Software | Firmware and devices | Hardware | Manufacturing and processes | Data and ML |
|---------|----------|----------------------|----------|-----------------------------|-------------|
| Artifact under test | Commit, build, image digest | Image hash, bootloader, configuration | Revision, build phase, serial | Lot, batch, line, station | Dataset version, model version, pipeline run |
| Environment | Local, preview, staging, production | Simulator, rig, device farm, field | Bench, chamber, test lab | Line, station, fixture | Notebook, pipeline, warehouse |
| Test run | Test execution | Rig run, soak | Measurement, characterization | Inspection, end-of-line test | Validation run, eval |
| Intermittent result | Flaky test | Intermittent fault | Marginal unit, drift | Out-of-control point | Drift, nondeterministic training |
| Defect | Bug | Field failure, brick | Nonconformance, failure | Nonconformance, escape | Data quality incident, model regression |
| Instrument | Test harness, assertion, grader | Rig, probes, power control | Meter, scope, gauge, chamber | Station, gauge, fixture | Validation rules, monitors, graders |

## Layer ladders

Cheapest first. Move up only for risks the lower layer cannot see (**principle-cheapest-layer-that-catches-it**).

- **Software:** static checks → unit → component → contract → API and integration → end-to-end → exploratory → production monitoring.
- **Firmware:** host unit tests → model-in-the-loop → software-in-the-loop → processor-in-the-loop → hardware-in-the-loop → system on real units → field telemetry.
- **Hardware:** simulation and design review → component characterization → board bring-up → system integration → environmental and reliability → certification → field returns analysis.
- **Manufacturing:** supplier quality and incoming inspection → in-process controls and SPC → end-of-line test → outgoing quality audit → field returns.
- **Data and ML:** schema and contract checks at ingestion → per-stage validation (nulls, ranges, volumes, uniqueness, referential integrity) → feature checks → model evaluation on held-out and sliced data → drift monitoring (distribution tests such as KS or PSI) in production.
- **Services and operational processes:** procedure review → dry run or tabletop → pilot with a small group → audit of records → outcome metrics.

## Playbooks by domain

| Domain | Start with |
|--------|-----------|
| Software | Test plan, Test design, Automate, Failure triage, Flaky triage |
| LLM and agent features | AI feature testing |
| Firmware | Firmware testing, Risk analysis |
| Hardware | Hardware validation, Risk analysis |
| Manufacturing | Production quality, Risk analysis (process FMEA), Escaped defect (8D) |
| Regulated or safety-related | Compliance evidence, Risk analysis |
| Any field, before work starts | Requirements review, or the **shift-left** skill for a full spec set |
