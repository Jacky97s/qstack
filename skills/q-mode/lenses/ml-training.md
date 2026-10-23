# Lens: ml-training

## Artifact identity
Dataset versions and hashes for train, validation, and test splits, the split procedure and seed, preprocessing code version, training code version, hyperparameters, seeds, hardware, framework versions, and the checkpoint. A model result without these is not reproducible and counts as `INCONCLUSIVE`.

## Stimulus and observation
Training data, evaluation sets, and inference inputs. Observe loss and metric curves, evaluation metrics overall and by slice, calibration, predictions on probe sets, and resource use.

## Instruments and trust
Evaluation code and metrics are instruments. Check the metric implementation against a hand-computed example, check that the evaluation pipeline scores a known-bad model low and a known-good model high, and compare with a simple baseline (majority class, previous model, a linear model). A model that barely beats the baseline has not been shown to learn the task.

## Variation and sampling
Random seeds, data order, nondeterministic kernels, and sampling of the evaluation set. Report metrics over several seeds with spread, and confidence intervals for evaluation metrics. A difference smaller than seed-to-seed spread is noise.

## Cost and reversibility
Training runs cost compute and time. Releasing a model that learned from data it should not have (personal data, licensed content, test labels) is hard to undo.

## Oracle sources
Held-out labels that the model and every tuning decision never saw, human-labeled gold sets, task definitions with acceptance thresholds, and domain experts for judgment tasks.

## Gates and standards
Data acceptance before training, evaluation gates before promotion, launch review, and post-deployment monitoring. Google's ML Test Score rubric lists tests across data, model, infrastructure, and monitoring. High-risk uses under the EU AI Act carry data-governance, accuracy, robustness, and documentation obligations (see the regulated lens).

## Layer ladder
Data validation (schema, ranges, nulls, duplicates, label distribution) → unit tests of preprocessing and features → overfit-a-tiny-batch sanity check → small-scale training run → full training with evaluation by slice → shadow or A/B evaluation online → drift and performance monitoring in production.

## Typical risks
- **Leakage:** test information reaching training, through overlapping or duplicate records, preprocessing fitted on all data, features that proxy the label, or time-travel (future data predicting the past). Deduplicate on content before splitting, fit preprocessing on training data only, and split by time or entity when the use case does.
- **Contamination:** evaluation or benchmark examples present in pretraining or fine-tuning data.
- **Slices:** an excellent overall score that hides failure on a group, language, region, device, or time period the users care about.
- **Labels:** noisy or inconsistent labels, measured with inter-annotator agreement.
- **Training-serving skew:** features computed differently in training and in production.
- **Drift:** input or concept drift after deployment.

## Failure classes
Data leakage, contamination, label noise, training-serving skew, distribution shift, metric implementation error, and seed sensitivity.

## Playbook notes
- **Requirements review:** define the task, the slices that matter, and acceptance thresholds before training, not after seeing results.
- **Test campaign:** compare candidate and baseline on the same evaluation sets, seeds, and metrics. Report by slice.
- **Escaped defect:** for a bad prediction in production, check data, features, and skew before blaming the model.
