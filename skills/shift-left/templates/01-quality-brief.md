# Quality Brief — <release>

> One page. QR = why / what we test. QV = how / with what we test.
> Source spec (read-only): <list the docs/*.md you used>

## QR — Quality requirements (why / what)

| Business goal | Quality risk if broken | Priority |
|---------------|------------------------|----------|
| <goal> | <what hurts the business> | P0/P1/P2 |

**In scope:** <what this release's testing covers>

**Out of scope:** <explicitly excluded, with the reason>

## QV — Quality verification (how / resources)

- **Environments:** <non-production environments and URLs>
- **Accounts / roles:** <roles the spec distinguishes>
- **Devices / browsers / locales / markets:** <...>
- **External dependencies:** <third parties, messaging, payments, hardware, and how real sends or charges are avoided (mock, sandbox, read-back)>

### This release's focus and QA alerts

> The 2 to 5 things that most deserve attention this cycle. Stages 2 to 4 read
> these to keep local detail aligned with the global strategy.

1. <focus / alert>
2. ...

## Spec gaps and ambiguities

### From the Stage 0 spec audit (if run)

| OQ-ID | Title | Type | Status | Blocks |
|-------|-------|------|--------|--------|
| OQ-001 | <title> | <type> | open/resolved | <stage> |

### Additional findings during intake

- <gap> — <where in the spec>
