# Lens: security

## Artifact identity
Build or image digest, dependency lockfiles and SBOM, configuration, and the deployed environment.

## Stimulus and observation
Inputs at every trust boundary: requests, files, messages, authentication flows, and configuration. Observe responses, authorization decisions, logs, and data exposure.

## Instruments and trust
Static analysis (SAST), dynamic scanning (DAST), dependency and composition analysis (SCA), secret scanning, and manual testing. Each tool has false positives and blind spots. Confirm a finding by reproducing it before reporting, and confirm a scanner works by pointing it at a known-vulnerable fixture.

## Variation and sampling
n/a: security findings are reproduced individually. Scanner coverage varies by configuration, so record what each run covered.

## Cost and reversibility
Active testing can damage data, lock accounts, trigger incident response, and breach law. Every active test needs written authorization: target, scope, time window, techniques allowed, and contacts. Without it, plan the test and stop.

## Oracle sources
OWASP ASVS requirements (verification levels 1 to 3), OWASP WSTG test cases, the threat model, and the system's own access-control rules.

## Gates and standards
SAST, SCA, and secret scanning on every change. DAST against preview or staging. Manual or penetration testing before major releases. Standards: OWASP ASVS and WSTG, and sector rules where they apply.

## Layer ladder
Threat model and design review → SAST, SCA, and secret scanning → unit and API tests for authorization rules → DAST → manual testing → penetration test → production detection and response.

## Typical risks
Broken access control (including indirect reads through exports, search, and notifications), injection, authentication and session flaws, secrets in code or logs, vulnerable dependencies, server-side request forgery, insecure defaults, and over-broad permissions for agents and service accounts.

## Failure classes
Scanner false positive, environment differs from production (WAF, configuration), and a real vulnerability.

## Playbook notes
- **Bug report:** a security finding goes to the owner through the private channel the project names, never into a public tracker.
- **Test design:** for every resource, test the denied cells of the role matrix as carefully as the allowed ones.
