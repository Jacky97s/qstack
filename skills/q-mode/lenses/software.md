# Lens: software

## Artifact identity
Commit SHA, build number, container image digest, package version, and the configuration and feature flags in effect. Results without a commit or digest are `INCONCLUSIVE`.

## Stimulus and observation
UI through browser or mobile automation, APIs through clients, CLIs through a PTY, events and messages, files. Observe return values, persisted state, emitted events, logs, traces, metrics, and screenshots.

## Instruments and trust
The test harness, assertions, fixtures, and CI. Prove a test can fail with a known-bad build or a planted mutant (**mutation-check**). Check that traces and logs are not sampled away for the cases you rely on.

## Variation and sampling
Asynchrony, concurrency, order, time, randomness, network, and parallel workers. A new test runs at least 5 times, at least 20 for end-to-end or parallel suites, before it counts as stable.

## Cost and reversibility
Runs are cheap and repeatable locally. Shared environments, production, third parties, and real users are not (**principle-protect-shared-environments**).

## Oracle sources
Specs and acceptance criteria, API schemas and contracts, types, invariants, previous versions, and consistency heuristics.

## Gates and standards
Pull request checks, release candidates, staged rollouts. Common standards: WCAG 2.2 for accessibility, OWASP ASVS for security (see the security lens).

## Layer ladder
Static checks → unit → component → contract → API and integration → end-to-end → exploratory → production monitoring.

## Typical risks
Contract drift between services, data migrations, permissions, concurrency on shared records, time zones and dates, money rounding, retries and idempotency, caching, feature-flag combinations, dependency upgrades.

## Failure classes
The base taxonomy in `../references/failure-taxonomy.md` applies as is.

## Playbook notes
- **Automate:** follow the suite's existing conventions. Locate by role, label, or test id. No assertions in page objects.
- **Change impact:** trace consumers of changed APIs, events, and schemas, not only callers.
