# Test Environment & Data Plan — <release>

> One review answers one question: can we provision all of this?

## Test environment

| Item | Value |
|------|-------|
| Environment under test | <URL; never production> |
| Build / version | <expected build or commit> |
| Data stores | <host or role reference, schema version> |
| Cache / queues | <...> |

### Tool chain

| Tool | Purpose | Version |
|------|---------|---------|
| <runner / client / mock / oracle> | <...> | <...> |

### Access

- <pointer to where credentials live (vault path, secret name). Never the secret itself.>

### Device / browser matrix

| Device / browser | OS | Notes |
|------------------|----|-------|
| <...> | <...> | |

---

## Test data

### Shared fixtures

| Name | Role / type | Values (real schema fields) | Provisioned by |
|------|-------------|-----------------------------|----------------|
| acct_role_a | <role> | <relevant fields> | seed script |

### Per-scenario data

#### G1-S1
- **Pre-state:** <rows or UI state, real fields>
- **Inputs:** <...>
- **Provisioned by:** seed script | DB insert | UI setup | API setup
- **Oracle:** none

#### G1-S4 (oracle-backed)
- **Pre-state:** <...>
- **Inputs:** <...>
- **Oracle:** `<tool or function>` → expected value; Then compares oracle == api == db
- **External sends:** <mock or read-back path; never a live SMS, email, or charge>
