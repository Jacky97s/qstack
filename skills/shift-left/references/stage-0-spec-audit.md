# Stage 0 — Spec Audit & Open Questions

**Goal:** systematically hunt for spec defects *before* writing any test
artifact. Every ambiguity, contradiction, gap, or TBD found here is one fewer
surprise in test design — and one fewer bug that ships. This is the purest
form of shift-left: finding defects in the spec itself, not in code.

## Inputs

- The spec snapshot at `<project>/docs/` — this is a **local read-only copy**
  synced by the orchestrator (see SKILL.md step 1). Provenance and the
  audit-scope triage (`include` / `exclude` lists with reasons) are recorded
  in `<project>/docs/.source`. **The audit scope is the `include` list** —
  every file in it must be covered, including files in subdirectories
  (e.g. `design-system/*.md`). Typical files: `PRD.md`, `SRS.md`, `SAD.md`,
  and optionally `Feature.md`, `DB.md`, TODO or known-issue lists, UI guidelines.
  Not every project has all of these; adapt the Layer 1 checks to the docs
  that are present. When there is no standalone `DB.md`, the data model is
  often embedded in SRS (e.g. a "Data Model" or "Data Contract" chapter).
- **Pre-check:** if `<project>/docs/` is empty or missing, **stop** and tell
  the user to run the doc snapshot procedure first (SKILL.md step 1). If
  `.source` exists but has no `audit-scope` section (legacy snapshot), run
  the triage now: list every file in `docs/`, propose include/exclude,
  confirm with the user, and update `.source` before auditing. Do not
  proceed with an audit against docs in `/tmp/` or any external path — all
  stages must read from the local snapshot for reproducibility.
- The release name.

## Output

- `<project>/00-open-questions/open-questions.md` — every finding as a numbered
  OQ entry, plus the Section Coverage Matrix appendix.
- A summary table for the human gate.

---

## Pre-audit: Document Inventory & Section Registry

**Before** starting the three audit layers, build a complete map of every
section in every spec doc. This map is the mechanism that prevents sections
from being silently skipped.

### Steps

1. Run `python3 <skill>/scripts/audit_coverage.py inventory <project>/docs/` to
   automatically scan all `.md` files and extract every section heading and
   every DB column definition. The script handles any number of files —
   it discovers dynamically, not from a hardcoded list.
2. Copy the script's output (two markdown tables) into the **Appendix A** and
   **Appendix B** sections of `open-questions.md`.
3. Verify the inventory looks complete (quick eyeball — does every doc appear?
   does the column count match the data model?). If a doc uses non-standard
   heading formats the script may miss sections — add them manually.

The registries are working artifacts — you mark each entry as you go. At the
end, the Post-audit step uses `audit_coverage.py verify` to mechanically

**Table continuity rule:** The Section Coverage Matrix and Column Coverage
Matrix are each a *single* markdown table spanning all spec docs (PRD, SRS,
SAD, etc.). Do **not** insert blank lines between doc sections within the
table — a blank line breaks the table in markdown renderers, causing
subsequent rows (e.g. the SRS section) to render as raw pipe-delimited text
instead of a table. Keep all rows continuous from header to last row.
confirm nothing was skipped.

---

## The three audit layers

Work through all three layers in order. Each layer catches a different class
of defect. **As you process each layer, mark the relevant sections and columns
in the coverage matrix** — either by recording an OQ number against them, or
by marking them `✓ clean`.

### Layer 1 — Mechanical cross-reference (structured, exhaustible)

Compare documents pairwise. For each check, scan the *entire* relevant section
— do not sample.

| Check ID | Compare | What to find | Example |
|----------|---------|--------------|---------|
| L1-NUM | PRD vs SRS | Numeric spec values that differ for the same feature (counts, limits, timeouts, sizes, digit lengths) | PRD "max 10 photos" vs SRS "min 7, max 10" — lower bound missing from PRD |
| L1-TYPE | SRS vs DB | Display-format requirements vs column types. Any SRS field needing time-of-day → DB column must be DATETIME not DATE | `confirmed_at` DATE vs display YYYY/MM/DD HH:mm:ss |
| L1-SECURITY | PRD security reqs vs DB | For every field PRD/SRS marks as sensitive (PII, encrypted at rest, hashed, tokenized), verify the DB column type+length can hold the **transformed** value, not just the plaintext. Ciphertext, hashes, and tokens are always longer than plaintext. | `id_number varchar(10)` holds plaintext exactly, but the PRD requires encryption at rest — AES-256-GCM ciphertext ≈ 44+ chars, SHA-256 = 64 hex chars, neither fits in 10 |
| L1-COLSCAN | DB schema vs all docs | **Per-column deep scan.** Walk every table, every column. For each column check: (a) type vs all stated business rules, (b) length vs all possible values including Unicode/encrypted/edge-case, (c) NOT NULL / DEFAULT vs business flow (can this field legitimately be empty at any stage?), (d) FK targets exist, (e) UNIQUE constraints match business uniqueness rules. | `campaign_id FK` (single) but business rule says "can stack multiple" — structural contradiction |
| L1-TBD | All docs | Grep for `TBD`, `TODO`, `N/A`, `pending`, `to be confirmed`, `not yet`, and their equivalents in the spec's language — each is an unresolved decision | PRD §7 "third-party API whitelist TBD" |
| L1-ENDPOINT | SRS flow tables vs SAD / Swagger | Every endpoint referenced in a user flow must exist in the API doc | SRS §5.4 references an endpoint not in SAD |
| L1-STATE | SRS status enums vs DB | Every status value used in business rules must exist as a DB enum value, and vice versa | Does `order_status=3` appear in DB enum? |
| L1-AC-ORPHAN | Feature.md AC list vs SRS functional sections | AC codes not referenced by any SRS section = orphan (likely unimplemented or mis-labeled) | AC-FEAT-001 not in any SRS flow |
| L1-AC-MISSING | SRS functional sections vs Feature.md | SRS business rules without an AC code = untraceable to acceptance criteria | SRS §5.5.1 rounding rule has no AC |
| L1-COMPAT | SRS new routes vs SRS legacy mentions | New URL formats must note whether old formats remain supported | `/resource/{id}` vs legacy `/resource?id=` |

#### L1-COLSCAN execution guide

This is the most exhaustive check. For projects with a large data model, work
table-by-table:

1. Read the table definition (columns, types, constraints, FKs).
2. For **each column**, grep all spec docs for references to that field name
   (or its business-language equivalent). Collect every stated requirement:
   format, length, encryption, nullability, uniqueness, valid values.
3. Compare the collected requirements against the declared type/constraints.
   Any mismatch → OQ entry.
4. Mark the column `✓ clean` or record the OQ number in the column registry.

Do not skip columns that "look fine" — the point is exhaustive coverage.
Columns with no cross-reference in any spec doc are themselves a finding
(type: `gap` — orphan column with no traceability).

### Layer 2 — Semantic conflict probes (LLM judgment required)

For each major business flow identified in the spec, ask these probe
questions and record any finding:

1. **Trigger consistency** — Is the triggering condition described identically
   across PRD, SRS, and Feature.md? Or does one say "automatic" and another
   say "manual"?
2. **Boundary exhaustiveness** — Are all boundary values explicitly listed?
   (e.g., rounding: what happens at exactly 50? at 0? at negative after
   deductions?)
3. **Cross-variant coverage** — For each rule, is the behavior defined for
   every variant axis? (e.g. different channels, roles, device types)
4. **Dependency chain alignment** — If rule A's output feeds rule B's input,
   are the data type, precision, and timing aligned?
5. **State machine completeness** — For each status field, is every legal
   transition explicitly defined? Are there dead-end states?
6. **Error path specification** — What happens when a 3rd-party call fails?
   Is retry/fallback defined, or only the happy path?
7. **Concurrency / race conditions** — Can two users (or the same user on
   two tabs) hit the same resource? Is the spec silent on locking?
8. **Security-at-rest alignment** — For every field that passes through
   encryption/hash/tokenize in any doc, is the transformation consistent
   across storage, API response, and display? Does the column size
   accommodate it? (This probe catches what L1-SECURITY finds mechanically,
   but from the business-flow perspective.)

### Layer 3 — Implicit assumptions (the hardest class)

Look for things the spec *doesn't say* but the system *must decide*:

- Timezone handling (stored UTC? displayed in which timezone?)
- Character encoding for 3rd-party integrations (legacy encoding vs system UTF-8)
- File size / type limits for upload (spec says count, not size)
- Session / token expiry during a multi-step flow
- What happens to in-progress data if the user closes the browser mid-flow?
- External service timeout — what if a downstream call takes > N seconds?
- Data-at-rest encryption scheme — which algorithm? key rotation? field-level
  or volume-level? (If PRD says "encrypt" but doesn't specify how, the DB
  column design can't be validated.)

---

## Post-audit: Coverage Verification

**After** all three layers are complete, perform this mandatory verification
step before writing the summary table.

### Steps

1. Run `python3 <skill>/scripts/audit_coverage.py verify <project>/docs/ <project>/00-open-questions/open-questions.md`.
   The script mechanically reports:
   - Sections present in docs but missing from the matrix.
   - Columns present in docs but missing from the matrix.
   - Matrix entries with blank status (not yet audited).
2. For every item the script flags as **MISSING** or **BLANK STATUS**:
   re-read that section/column now and either generate a finding or mark it
   `✓ clean` with a one-line rationale (e.g. "✓ clean — glossary
   definitions only, no testable assertions").
3. Re-run `audit_coverage.py verify` until it reports **PASS**.
4. Count the sections/columns that required re-read in this step. If > 20%
   of total sections were missed, **log a warning** in the summary:
   `⚠ Coverage gap: {n}/{total} sections required post-audit re-read.`
   This is a signal that the audit pass was too shallow.

The audit is **not done** until every row in both matrices has a status.

---

## OQ entry format

Every finding becomes one entry. Use the template in
`templates/00-open-questions.md`. The format:

```markdown
### OQ-{NNN}: {one-line title}

- **type**: contradiction | gap | ambiguity | tbd | type-mismatch | implicit-assumption
- **source**: {doc A §section} vs {doc B §section}
- **detail**: {what exactly is wrong or missing}
- **impact**: {which test stage / business flow is blocked or degraded}
- **blocks**: stage-1 | stage-2 | stage-3 | stage-4 | none (informational)
- **suggested-owner**: <role that can decide: product, backend, data, frontend, ops, QA>
- **status**: open
```

## Severity heuristic

Assign `blocks` based on impact:

- **blocks: stage-1** — The in/out scope of testing can't be decided (e.g., a
  feature is marked both "in scope" and "deferred" in different docs).
- **blocks: stage-2** — Test goals can't be written because the expected
  behavior is undefined (e.g., TBD endpoint, contradictory business rule).
- **blocks: stage-3** — Test data can't be prepared because value ranges or
  formats are ambiguous.
- **blocks: stage-4** — Test steps can't be written because UI flow or API
  contract is unclear.
- **blocks: none** — Informational; good to resolve but won't stall the
  pipeline.

## Process

1. Create `<project>/` if absent.
2. Copy `templates/00-open-questions.md` to
   `<project>/00-open-questions/open-questions.md`.
3. **Pre-audit:** Build the Document Inventory — section registry and column
   registry. Write them as the Coverage Matrix appendix.
4. Execute Layer 1 checks (including L1-COLSCAN). For each finding, append an
   OQ entry. Mark covered sections/columns in the matrix.
5. Execute Layer 2 probes per business flow. Append findings. Mark sections.
6. Execute Layer 3 implicit-assumption scan. Append findings. Mark sections.
7. **Post-audit:** Run Coverage Verification. Re-read any uncovered sections.
   Append any new findings. Finalize all matrix entries.
8. Write the summary table at the top of `open-questions.md`.
9. Stop at the human gate.

## Human gate

Present:

```
Spec Audit complete for <release>.
Found {N} open questions: {n_contradiction} contradictions, {n_gap} gaps,
{n_ambiguity} ambiguities, {n_tbd} TBDs, {n_type} type mismatches,
{n_implicit} implicit assumptions.

Blocking stage-1: {count} | stage-2: {count} | stage-3: {count} | stage-4: {count}

Section coverage: {covered}/{total} sections audited ({pct}%).
Column coverage: {covered}/{total} columns audited ({pct}%).
Post-audit re-reads: {n} sections, {m} columns.

→ Review 00-open-questions.md. Resolve or acknowledge each blocking OQ before
  proceeding to Stage 1.
```

**The gate question:** "Are there any blocking OQs that need PM/backend
resolution before we can frame the test scope in Stage 1?"

## Definition of done

- `00-open-questions.md` exists with all findings numbered and typed.
- Summary table is populated.
- Section Coverage Matrix: 100% of sections have a status (OQ ref or ✓ clean).
- Column Coverage Matrix: 100% of columns have a status (OQ ref or ✓ clean).
- No `blocks: stage-1` OQ is left unaddressed (resolved or explicitly
  accepted as a known risk).
