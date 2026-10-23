# Lens: ml-training

## Artifact identity
Record these items:
- dataset versions and hashes for train, validation, and test splits
- the split procedure and seed
- preprocessing code version
- training code version
- hyperparameters
- seeds
- hardware
- framework versions
- the checkpoint

A model result without these is not reproducible and counts as `INCONCLUSIVE`.

## Stimulus and observation
Training data, evaluation sets, and inference inputs. Observe loss and metric curves, evaluation metrics overall and by slice, calibration, predictions on probe sets, and resource use.

## Instruments and trust
Evaluation code and metrics are instruments. Check the metric implementation against a hand-computed example. Check that the evaluation pipeline gives a low score to a known-bad model and a high score to a known-good model. Compare with a simple baseline (majority class, previous model, a linear model). If a model only just beats the baseline, you have not shown that it learns the task.

## Variation and sampling
Results vary with random seeds, data order, nondeterministic kernels, and sampling of the evaluation set. Report metrics over several seeds with the spread. Report confidence intervals for evaluation metrics. A difference smaller than the seed-to-seed spread is noise.

## Cost and reversibility
Training runs cost compute and time. It is hard to undo the release of a model that learned from data it must not use (personal data, licensed content, test labels).

## Oracle sources
Held-out labels that the model and every tuning decision never saw, human-labeled gold sets, task definitions with acceptance thresholds, and domain experts for judgment tasks.

## Gates and standards
Data acceptance before training, evaluation gates before promotion, launch review, and post-deployment monitoring. The Google ML Test Score rubric lists tests across data, model, infrastructure, and monitoring. High-risk uses under the EU AI Act carry obligations for data governance, accuracy, robustness, and documentation (see the regulated lens).

## Layer ladder
Use these layers in this order:
- data validation (schema, ranges, nulls, duplicates, label distribution)
- unit tests of preprocessing and features
- overfit-a-tiny-batch sanity check
- small-scale training run
- full training with evaluation by slice
- shadow or A/B evaluation online
- drift and performance monitoring in production

## Typical risks
- **Leakage:** test information that reaches training, through:
  - overlapping or duplicate records
  - preprocessing fitted on all data
  - features that proxy the label
  - time-travel (future data that predicts the past)

  Deduplicate on content before you split. Fit preprocessing on training data only. Split by time or entity when the use case needs it.
- **Contamination:** evaluation or benchmark examples in pretraining or fine-tuning data.
- **Slices:** an excellent overall score that hides failure on a group, language, region, device, or time period that the users care about.
- **Labels:** noisy or inconsistent labels. Measure them with inter-annotator agreement.
- **Training-serving skew:** features that training and production compute in different ways.
- **Drift:** input or concept drift after deployment.

## Failure classes
Data leakage, contamination, label noise, training-serving skew, distribution shift, metric implementation error, and seed sensitivity.

## Playbook notes
- **Requirements review:** define the task, the slices that matter, and the acceptance thresholds before training. Do not define them after you see the results.
- **Test campaign:** compare the candidate and the baseline on the same evaluation sets, seeds, and metrics. Report by slice.
- **Escaped defect:** for a bad prediction in production, check the data, features, and skew before you blame the model.
