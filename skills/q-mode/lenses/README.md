# Lenses

The core loop and the playbooks are the same in every field. A lens supplies the parts that differ: eight slots, plus the typical risks, failure classes, and playbook adjustments of the domain. Lenses are data, not process. To add a field, add one lens file. Do not add a new playbook.

Choose lenses from `.qstack/profile.md`. If there is no profile, choose them from the task. Lenses stack: `firmware` plus `regulated`, `genai` plus `performance`, `manufacturing` plus `hardware`. When two lenses fill the same slot, apply both.

`genai` and `ml-training` split on who changes the weights. To judge if a fine-tuned checkpoint is better than its base, use `ml-training`. To judge the product feature built on that checkpoint, use `genai`. Fine-tuning for a feature usually needs both.

| Lens | Use for |
|------|---------|
| [software](software.md) | Applications, services, APIs, libraries, web and mobile |
| [firmware](firmware.md) | Embedded code, drivers, bootloaders, update paths, connected devices |
| [hardware](hardware.md) | Electronics, mechanics, devices, and products through build-phase gates |
| [manufacturing](manufacturing.md) | Production lines, assembly, inspection, end-of-line test, repeated processes |
| [performance](performance.md) | Load, stress, spike, soak, and capacity of any system |
| [genai](genai.md) | Use of a model inside a product: prompts, retrieval, agents, tools. Someone else owns the weights, or the weights are fixed |
| [ml-training](ml-training.md) | Changes to the weights of a model: training, fine-tuning, distillation, and the data they learn from, judged on held-out evaluation |
| [data](data.md) | Data pipelines, warehouses, analytics, and reporting |
| [security](security.md) | Security verification of any system, within authorized scope |
| [regulated](regulated.md) | Overlay for safety-related or regulated work in any field |

## Vocabulary across lenses

| Concept | Software | Firmware | Hardware | Manufacturing | ML and data |
|---------|----------|----------|----------|---------------|-------------|
| Artifact under test | Commit, build, image digest | Image hash, bootloader, configuration | Revision, build phase, serial | Lot, line, station | Dataset version, checkpoint, pipeline run |
| Environment | Local, preview, staging, production | Simulator, rig, device farm, field | Bench, chamber, lab | Line, station, fixture | Notebook, pipeline, warehouse, serving |
| A run | Test execution | Rig run, soak | Measurement, characterization | Inspection, end-of-line test | Eval run, validation run |
| Intermittent result | Flaky test | Intermittent fault | Marginal unit, drift | Out-of-control point | Drift, seed sensitivity |
| Defect | Bug | Field failure, brick | Nonconformance | Nonconformance, escape | Regression, data incident |
| Instrument | Harness, assertion, grader | Rig, probes, power control | Meter, scope, gauge, chamber | Station, gauge, fixture | Validation rules, graders, monitors |

## Writing a lens

Copy an existing lens. Keep every heading below, in this order. The qstack `validate.py` script fails a lens that has no one of them. If a slot does not apply, fill it with `n/a` and the reason.

1. `## Artifact identity`: how to identify a tested artifact, so that you can tie results to it.
2. `## Stimulus and observation`: how you can act on the artifact and what you can see.
3. `## Instruments and trust`: what measures the artifact, and how you prove that each instrument is fit.
4. `## Variation and sampling`: where results vary and how many trials, units, or samples a claim needs.
5. `## Cost and reversibility`: what a run costs, and which actions you cannot undo.
6. `## Oracle sources`: where expected results come from in this field.
7. `## Gates and standards`: the decision points and the standards that govern them.
8. `## Layer ladder`: the layers from cheapest to most realistic.
9. `## Typical risks`: the risks that most often cause harm in this field.
10. `## Failure classes`: domain classes to add to the failure taxonomy.
11. `## Playbook notes`: what changes in specific playbooks under this lens.
