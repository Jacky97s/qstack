# Lens: software

## Artifact identity
Commit SHA, build number, container image digest, package version, and the configuration and feature flags in effect. A result with no commit or digest is `INCONCLUSIVE`.

## Stimulus and observation
Act on the UI through browser or mobile automation. Act on APIs through clients, on CLIs through a PTY, and on events, messages, and files directly. Observe return values, persisted state, emitted events, logs, traces, metrics, and screenshots.

## Instruments and trust
The instruments are the test harness, assertions, fixtures, and CI. Prove that a test can fail. Use a known-bad build or a planted mutant (**mutation-check**). Make sure that sampling does not remove the traces and logs you need.

## Variation and sampling
Results vary with asynchrony, concurrency, order, time, randomness, network, and parallel workers. Run a new test at least 5 times before it counts as stable. Run end-to-end or parallel suites at least 20 times.

## Cost and reversibility
Runs are cheap and repeatable on a local machine. Shared environments, production, third parties, and real users are not cheap or repeatable (**principle-protect-shared-environments**).

## Oracle sources
Specs and acceptance criteria, API schemas and contracts, types, invariants, previous versions, and consistency heuristics.

## Gates and standards
Pull request checks, release candidates, and staged rollouts. Common standards: WCAG 2.2 for accessibility and OWASP ASVS for security (see the security lens).

## Layer ladder
Static checks → unit → component → contract → API and integration → end-to-end → exploratory → production monitoring.

## Typical risks
Contract drift between services, data migrations, permissions, concurrency on shared records, time zones and dates, money rounding, retries and idempotency, caching, feature-flag combinations, dependency upgrades.

## Failure classes
The base taxonomy in `../references/failure-taxonomy.md` applies without change.

## Playbook notes
- **Automate:** follow the existing conventions of the suite. Locate elements by role, label, or test id. Do not put assertions in page objects.
- **Change impact:** trace the consumers of changed APIs, events, and schemas. Do not trace only the callers.
