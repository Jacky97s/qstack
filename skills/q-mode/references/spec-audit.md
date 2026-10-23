# Spec audit and open questions

Stage 0 of the **Shift-left** playbook (`../playbooks/shift-left.md`), and the full-spec path of **Requirements review**.

**Goal:** Hunt for spec defects in a systematic way *before* you write any test artifact. Each ambiguity, contradiction, gap, or TBD that you find here removes one surprise from test design. It also removes one bug that can ship. This is the purest form of shift-left: you find defects in the spec itself, not in code.

## Inputs

- The spec files in scope, read-only, at `<spec-dir>/`. The include list comes from the scope step of the Shift-left playbook. You must cover every file in it, including files in subdirectories.
  - Typical files: PRD, SRS, architecture, feature specs, data model, API contracts, UI guidelines, and TODO or known-issue lists.
  - Not every project has all of these files. Adapt the Layer 1 checks to the documents that exist.
  - If there is no standalone data-model document, the data model is often a chapter of the SRS.
- **Pre-check:** if nobody fixed the scope, fix it first (Shift-left step 1). Audit the files at their recorded version. Then you can reproduce the result.
- The release name.

## Output

- `<open-questions.md>`: every finding as a numbered OQ entry, plus the Section Coverage Matrix appendix.
- A summary table for the human gate.

---

## Pre-audit: Document Inventory & Section Registry

**Before** you start the three audit layers, build a complete map of every section in every spec doc. This map prevents sections from being skipped without notice.

### Steps

1. Run `python3 <q-mode>/scripts/audit_coverage.py inventory <spec-dir>/`. The script scans all `.md` files and extracts every section heading and every DB column definition. It handles any number of files. It finds the files dynamically, not from a hardcoded list.
2. Copy the output of the script (two markdown tables) into the **Appendix A** and **Appendix B** sections of `open-questions.md`.
3. Verify that the inventory is complete. Do a quick visual check: does every doc appear? Does the column count match the data model? If a doc uses non-standard heading formats, the script can miss sections. Add them manually.

The registries are working artifacts. Mark each entry as you go. At the end, the Post-audit step uses `audit_coverage.py verify` to confirm mechanically that nothing was skipped.

**Table continuity rule:** The Section Coverage Matrix and the Column Coverage Matrix are each a *single* markdown table. Each table spans all spec docs (PRD, SRS, SAD, and others). Do **not** insert blank lines between doc sections in the table. A blank line breaks the table in markdown renderers. Then the next rows (for example the SRS section) render as raw pipe-delimited text and not as a table. Keep all rows continuous from the header to the last row.

---

## The three audit layers

Work through all three layers in order. Each layer catches a different class of defect. **As you process each layer, mark the relevant sections and columns in the coverage matrix.** Record an OQ number against them, or mark them `✓ clean`.

### Layer 1 — Mechanical cross-reference (structured, exhaustible)

Compare documents in pairs. For each check, scan the *entire* relevant section. Do not sample.

| Check ID | Compare | What to find | Example |
|----------|---------|--------------|---------|
| L1-NUM | PRD vs SRS | Numeric spec values that differ for the same feature (counts, limits, timeouts, sizes, digit lengths) | PRD "max 10 photos" vs SRS "min 7, max 10": the lower bound is missing from the PRD |
| L1-TYPE | SRS vs DB | Display-format requirements vs column types. Any SRS field that needs time-of-day: the DB column must be DATETIME, not DATE | `confirmed_at` DATE vs display YYYY/MM/DD HH:mm:ss |
| L1-SECURITY | PRD security reqs vs DB | For every field that the PRD or SRS marks as sensitive (PII, encrypted at rest, hashed, tokenized), verify that the DB column type and length can hold the **transformed** value, not only the plaintext. Ciphertext, hashes, and tokens are always longer than plaintext. | `id_number varchar(10)` holds plaintext exactly, but the PRD requires encryption at rest. AES-256-GCM ciphertext is about 44+ chars and SHA-256 is 64 hex chars. Neither fits in 10 |
| L1-COLSCAN | DB schema vs all docs | **Per-column deep scan.** Walk every table and every column. For each column, check: (a) type vs all stated business rules, (b) length vs all possible values, including Unicode, encrypted, and edge-case values, (c) NOT NULL / DEFAULT vs business flow (can this field be empty at any stage?), (d) FK targets exist, (e) UNIQUE constraints match business uniqueness rules. | `campaign_id FK` (single) but the business rule says "can stack multiple": a structural contradiction |
| L1-TBD | All docs | Grep for `TBD`, `TODO`, `N/A`, `pending`, `to be confirmed`, `not yet`, and their equivalents in the language of the spec. Each one is an unresolved decision | PRD §7 "third-party API whitelist TBD" |
| L1-ENDPOINT | SRS flow tables vs SAD / Swagger | Every endpoint that a user flow references must exist in the API doc | SRS §5.4 references an endpoint that is not in the SAD |
| L1-STATE | SRS status enums vs DB | Every status value in the business rules must exist as a DB enum value, and the reverse | Does `order_status=3` appear in the DB enum? |
| L1-AC-ORPHAN | Feature.md AC list vs SRS functional sections | An AC code that no SRS section references is an orphan (probably not implemented, or labeled in error) | AC-FEAT-001 is not in any SRS flow |
| L1-AC-MISSING | SRS functional sections vs Feature.md | An SRS business rule without an AC code has no trace to the acceptance criteria | The SRS §5.5.1 rounding rule has no AC |
| L1-COMPAT | SRS new routes vs SRS legacy mentions | New URL formats must say if the old formats stay supported | `/resource/{id}` vs legacy `/resource?id=` |

#### L1-COLSCAN execution guide

This is the most exhaustive check. For projects with a large data model, work table by table:

1. Read the table definition (columns, types, constraints, FKs).
2. For **each column**, grep all spec docs for references to that field name (or its business-language equivalent). Collect every stated requirement: format, length, encryption, nullability, uniqueness, valid values.
3. Compare the collected requirements with the declared type and constraints. Write an OQ entry for each mismatch.
4. Mark the column `✓ clean` or record the OQ number in the column registry.

Do not skip columns that "look fine". The point is exhaustive coverage. A column that no spec doc references is itself a finding (type: `gap`, an orphan column with no traceability).

### Layer 2 — Semantic conflict probes (LLM judgment required)

For each major business flow in the spec, ask these probe questions. Record each finding.

1. **Trigger consistency** — Do PRD, SRS, and Feature.md describe the triggering condition in the same way? Or does one say "automatic" and another say "manual"?
2. **Boundary exhaustiveness** — Does the spec list all boundary values explicitly? (For example, rounding: what happens at exactly 50? at 0? at a negative value after deductions?)
3. **Cross-variant coverage** — For each rule, is the behavior defined for every variant axis? (For example, different channels, roles, device types.)
4. **Dependency chain alignment** — If the output of rule A is the input of rule B, do the data type, precision, and timing match?
5. **State machine completeness** — For each status field, does the spec define every legal transition explicitly? Are there dead-end states?
6. **Error path specification** — What happens when a 3rd-party call fails? Does the spec define retry or fallback, or only the happy path?
7. **Concurrency / race conditions** — Can two users (or the same user on two tabs) use the same resource at the same time? Is the spec silent on locking?
8. **Security-at-rest alignment:** Look at every field that goes through encryption, hash, or tokenization in any doc. Is the transformation the same across storage, API response, and display? Is the column size large enough for it? (This probe catches what L1-SECURITY finds mechanically, but from the business-flow perspective.)

### Layer 3 — Implicit assumptions (the hardest class)

Look for items that the spec *does not state* but that the system *must decide*:

- Timezone handling (stored as UTC? displayed in which timezone?)
- Character encoding for 3rd-party integrations (legacy encoding vs system UTF-8)
- File size and type limits for upload (the spec gives a count, not a size)
- Session or token expiry during a multi-step flow
- What happens to in-progress data if the user closes the browser in the middle of a flow?
- External service timeout: what if a downstream call takes more than N seconds?
- Data-at-rest encryption scheme: which algorithm? key rotation? field-level or volume-level? (If the PRD says "encrypt" but does not say how, you cannot validate the DB column design.)

---

## Post-audit: Coverage Verification

**After** you complete all three layers, do this mandatory verification step before you write the summary table.

### Steps

1. Run `python3 <q-mode>/scripts/audit_coverage.py verify <spec-dir>/ <open-questions.md>`. The script reports these items mechanically:
   - Sections that are in the docs but not in the matrix.
   - Columns that are in the docs but not in the matrix.
   - Matrix entries with a blank status (not yet audited).
2. For every item that the script flags as **MISSING** or **BLANK STATUS**: read that section or column again now. Then generate a finding, or mark it `✓ clean` with a one-line rationale (for example "✓ clean — glossary definitions only, no testable assertions").
3. Run `audit_coverage.py verify` again until it reports **PASS**.
4. Count the sections and columns that needed a re-read in this step. If more than 20% of all sections were missed, **log a warning** in the summary. Use this text: `⚠ Coverage gap: {n}/{total} sections required post-audit re-read.` This warning shows that the audit pass was too shallow.

The audit is **not done** until every row in both matrices has a status.

---

## OQ entry format

Every finding becomes one entry in this format:

```markdown
### OQ-{NNN}: {one-line title}

- **type**: contradiction | gap | ambiguity | tbd | type-mismatch | implicit-assumption
- **source**: {doc A §section} vs {doc B §section}
- **detail**: {what exactly is wrong or missing}
- **impact**: {which test stage / business flow is blocked or degraded}
- **blocks**: plan | cases | none (informational)
- **suggested-owner**: <role that can decide: product, backend, data, frontend, ops, QA>
- **status**: open
```

## Severity heuristic

Assign `blocks` based on impact:

- **blocks: plan** — Stage 1 cannot continue. Nobody can decide the in/out scope (a feature is both "in scope" and "deferred"). Or nobody can write goals because the expected behavior is undefined (a TBD endpoint, a contradictory business rule).
- **blocks: cases** — Stage 2 cannot continue for the affected scenarios. Nobody can prepare data because ranges or formats are ambiguous. Or nobody can write steps because the flow or contract is unclear. Only the dependent scenarios wait.
- **blocks: none** — Informational. It is good to resolve it, but it does not stop the pipeline.

## Process

1. Start the open-question list where the tester wants it (the reply by default).
2. Put a summary table at the top of it: counts by type and by `blocks`.
3. **Pre-audit:** Build the Document Inventory (section registry and column registry). Write them as the Coverage Matrix appendix.
4. Run the Layer 1 checks (including L1-COLSCAN). For each finding, append an OQ entry. Mark the covered sections and columns in the matrix.
5. Run the Layer 2 probes for each business flow. Append the findings. Mark the sections.
6. Run the Layer 3 implicit-assumption scan. Append the findings. Mark the sections.
7. **Post-audit:** Run Coverage Verification. Read again any section that is not covered. Append any new findings. Finalize all matrix entries.
8. Write the summary table at the top of `open-questions.md`.
9. Stop at the human gate.

## Human gate

Present:

```
Spec Audit complete for <release>.
Found {N} open questions: {n_contradiction} contradictions, {n_gap} gaps,
{n_ambiguity} ambiguities, {n_tbd} TBDs, {n_type} type mismatches,
{n_implicit} implicit assumptions.

Blocking plan: {count} | cases: {count}

Section coverage: {covered}/{total} sections audited ({pct}%).
Column coverage: {covered}/{total} columns audited ({pct}%).
Post-audit re-reads: {n} sections, {m} columns.

→ Review the open questions. Resolve or acknowledge each blocking OQ before
  proceeding to Stage 1.
```

**The gate question:** "Are there any blocking OQs that need PM/backend
resolution before we can frame the test scope in Stage 1?"

## Definition of done

- The open-question list exists with all findings numbered and typed.
- The summary table is filled in.
- Section Coverage Matrix: 100% of sections have a status (OQ ref or ✓ clean).
- Column Coverage Matrix: 100% of columns have a status (OQ ref or ✓ clean).
- No `blocks: plan` OQ stays unaddressed. Each one is resolved or explicitly accepted as a known risk.
