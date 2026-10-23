# Lens: security

## Artifact identity
Build or image digest, dependency lockfiles and SBOM, configuration, and the deployed environment.

## Stimulus and observation
Inputs at every trust boundary: requests, files, messages, authentication flows, and configuration. Observe responses, authorization decisions, logs, and data exposure.

## Instruments and trust
The instruments are static analysis (SAST), dynamic scanning (DAST), dependency and composition analysis (SCA), secret scanning, and manual testing. Each tool has false positives and blind spots. Reproduce a finding before you report it. To confirm that a scanner works, point it at a known-vulnerable fixture.

## Variation and sampling
n/a: you reproduce each security finding individually. Scanner coverage varies with configuration, so record what each run covered.

## Cost and reversibility
Active testing can damage data, lock accounts, trigger incident response, and break the law. Every active test needs written authorization: target, scope, time window, allowed techniques, and contacts. If you do not have it, plan the test and stop.

## Oracle sources
OWASP ASVS requirements (verification levels 1 to 3), OWASP WSTG test cases, the threat model, and the access-control rules of the system.

## Gates and standards
Run SAST, SCA, and secret scanning on every change. Run DAST against preview or staging. Do manual or penetration testing before major releases. Standards: OWASP ASVS and WSTG, and sector rules where they apply.

## Layer ladder
Use these layers in this order:
- threat model and design review
- SAST, SCA, and secret scanning
- unit and API tests for authorization rules
- DAST
- manual testing
- penetration test
- production detection and response

## Typical risks
These risks are typical:
- broken access control (including indirect reads through exports, search, and notifications)
- injection
- authentication and session flaws
- secrets in code or logs
- vulnerable dependencies
- server-side request forgery
- insecure defaults
- over-broad permissions for agents and service accounts

## Failure classes
Scanner false positive, environment that differs from production (WAF, configuration), and a real vulnerability.

## Playbook notes
- **Bug report:** send a security finding to the owner through the private channel that the project names. Do not put it in a public tracker.
- **Test design:** for every resource, test the denied cells of the role matrix with the same care as the allowed cells.
