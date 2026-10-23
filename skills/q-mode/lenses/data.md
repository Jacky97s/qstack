# Lens: data

## Artifact identity
Pipeline code version, run identifier, source snapshot or watermark, schema version, and output table or file versions.

## Stimulus and observation
Source data (real snapshots or synthetic fixtures), pipeline runs, and queries. Observe row counts, schema, null rates, distributions, uniqueness, referential integrity, freshness, and downstream reports.

## Instruments and trust
Validation rules and data tests are instruments. Prove that each one fails on a fixture that you corrupted on purpose. Check that monitors send an alert for an injected anomaly.

## Variation and sampling
Data varies with daily volume swings, seasonality, late-arriving data, and upstream changes. Set thresholds from observed history. Do not guess them.

## Cost and reversibility
Backfills and overwrites of shared tables can destroy history and break consumers. Treat each write to a shared dataset as a shared-environment operation.

## Oracle sources
Data contracts between producers and consumers, source-system reconciliation (counts and sums), business rules, and previous runs.

## Gates and standards
Contract checks at ingestion, tests on each transformation, reconciliation before publishing, and monitoring of freshness and quality. Privacy rules govern personal data in fixtures and logs.

## Layer ladder
Schema and contract checks at ingestion → unit tests of transformations → per-stage validation → reconciliation against sources → downstream report checks → production monitoring.

## Typical risks
These risks are typical:
- silent schema changes upstream
- duplicates from retries
- late data
- time zones and daylight saving
- unit or currency mix-ups
- joins that fan out or drop rows
- reports that look correct but are wrong

## Failure classes
Upstream contract break, late or missing source data, duplicate ingestion, transformation logic error, and reconciliation mismatch.

## Playbook notes
- **Test design:** properties fit data well. Row counts stay the same through joins. Sums agree with the sources. Keys are unique. Every foreign key resolves.
