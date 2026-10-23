# Open Questions — <release>

> Spec defects found by Stage 0 Spec Audit. Each OQ is a shift-left win:
> a defect caught in the spec before it becomes a bug in code or a gap in tests.
>
> Source spec (read-only): <list the docs/*.md audited>
> Audit date: <YYYY-MM-DD>

## Summary

| Type | Count | Blocking |
|------|-------|----------|
| contradiction | 0 | — |
| gap | 0 | — |
| ambiguity | 0 | — |
| tbd | 0 | — |
| type-mismatch | 0 | — |
| implicit-assumption | 0 | — |
| **Total** | **0** | **0** |

### Blocking breakdown

- blocks stage-1: <count>
- blocks stage-2: <count>
- blocks stage-3: <count>
- blocks stage-4: <count>
- informational (none): <count>

---

## Findings

<!-- Copy this template for each finding. Number sequentially. -->

### OQ-001: <one-line title>

- **type**: contradiction | gap | ambiguity | tbd | type-mismatch | implicit-assumption
- **source**: <doc A §section> vs <doc B §section>
- **detail**: <what exactly is wrong or missing>
- **impact**: <which test stage / business flow is blocked or degraded>
- **blocks**: stage-1 | stage-2 | stage-3 | stage-4 | none
- **suggested-owner**: <role that can decide: product, backend, data, frontend, ops, QA>
- **status**: open

---

<!-- Status lifecycle: open → confirmed → resolved | accepted-risk | wontfix -->
<!-- When resolved, add a **resolution** line with the decision and date. -->

---

## Appendix A: Section Coverage Matrix

> Every section of every spec doc must appear below. Status is either an OQ
> number (e.g. `OQ-003`) or `✓ clean` with a one-line rationale. **No blank
> status allowed** — the audit is not done until every row is filled.

| Doc | Section | Title | Status | Notes |
|-----|---------|-------|--------|-------|
| _doc.md_ | _§x.x_ | _example_ | ✓ clean | definitions only |
| _doc.md_ | _§x.x_ | _example_ | OQ-001 | |

<!-- Populate from the Pre-audit Document Inventory. -->
<!-- Sections with no findings must be explicitly marked ✓ clean. -->
<!-- IMPORTANT: Do NOT insert blank lines between doc sections (e.g. between -->
<!-- the last PRD row and the first SRS row). Blank lines break the table in -->
<!-- markdown renderers. Keep all rows continuous from header to last row. -->

---

## Appendix B: Column Coverage Matrix

> Every table and column in the data model must appear below. For each column,
> verify type, length, constraints, and security requirements against all spec
> docs. Status is an OQ number or `✓ clean`.

| Table | Column | Type | Status | Notes |
|-------|--------|------|--------|-------|
| _table_ | _id_ | _bigint_ | ✓ clean | PK, auto-increment |
| _table_ | _status_ | _varchar(40)_ | OQ-022 | string vs int conflict |

<!-- Populate from the Pre-audit column registry (DB.md or SRS data model). -->
<!-- Columns with no cross-reference in any spec doc → type: gap (orphan column). -->
