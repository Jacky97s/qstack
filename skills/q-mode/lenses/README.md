# Lenses

The core loop and the playbooks are the same in every field. A lens supplies the parts that differ: eight slots, plus the domain's typical risks, failure classes, and playbook adjustments. Lenses are data, not process. Adding a field means adding one lens file, never a new playbook.

Choose lenses from `.qstack/profile.md`, or from the task when there is no profile. Lenses stack: `firmware` plus `regulated`, `genai` plus `performance`, `manufacturing` plus `hardware`. When two lenses fill the same slot, apply both.

`genai` and `ml-training` split on who changes the weights. Judging whether a fine-tuned checkpoint beats its base is `ml-training`. Judging the product feature built on that checkpoint is `genai`. Fine-tuning for a feature usually needs both.

| Lens | Use for |
|------|---------|
| [software](software.md) | Applications, services, APIs, libraries, web and mobile |
| [firmware](firmware.md) | Embedded code, drivers, bootloaders, update paths, connected devices |
| [hardware](hardware.md) | Electronics, mechanics, devices, and products through build-phase gates |
| [manufacturing](manufacturing.md) | Production lines, assembly, inspection, end-of-line test, repeated processes |
| [performance](performance.md) | Load, stress, spike, soak, and capacity of any system |
| [genai](genai.md) | Using a model inside a product: prompts, retrieval, agents, tools. The weights are someone else's or fixed |
| [ml-training](ml-training.md) | Changing a model's weights: training, fine-tuning, distillation, and the data they learn from, judged on held-out evaluation |
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

Copy an existing lens. Keep every heading below in this order. qstack's `validate.py` fails a lens that misses one. Fill a slot that does not apply with `n/a` and the reason.

1. `## Artifact identity`: how a tested artifact is identified, so results can be tied to it.
2. `## Stimulus and observation`: how you can act on it and what you can see.
3. `## Instruments and trust`: what measures it, and how each instrument is proven fit.
4. `## Variation and sampling`: where results vary and how many trials, units, or samples a claim needs.
5. `## Cost and reversibility`: what a run costs, and which actions cannot be undone.
6. `## Oracle sources`: where expected results come from in this field.
7. `## Gates and standards`: the decision points and the standards that govern them.
8. `## Layer ladder`: cheapest to most realistic.
9. `## Typical risks`: the risks that most often hurt in this field.
10. `## Failure classes`: domain classes to add to the failure taxonomy.
11. `## Playbook notes`: what changes in specific playbooks under this lens.
