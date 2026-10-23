# Stage 1 — Intake & Quality Brief

**Goal:** read the spec and produce a one-page `01-quality-brief.md` that frames
*why we test* and *how we'll test*, so every downstream goal and case inherits a
clear purpose. This is a lightweight QR + QV one-pager.

## Inputs

- The spec, read-only: `<project>/docs/` — typically `PRD.md`, `SRS.md`,
  `SAD.md`, and optionally `Feature.md`, `DB.md` (whichever exist).
- **`<project>/00-open-questions.md`** from Stage 0 (if it exists). Resolved
  OQs inform test boundaries; unresolved OQs with `blocks: stage-1` must be
  addressed before this stage can complete.
- The release name and, if it exists, the previous release's quality brief
  (carry forward standing risks and the helper inventory).

## Process

1. Create `<project>/` if absent and copy `templates/01-quality-brief.md`.
2. Skim the spec for: business goals, the riskiest changes this release,
   money/permission/data-integrity surfaces, external dependencies (SMS, 3rd
   party, hardware), and anything explicitly out of scope.
3. Fill the template. Two halves:
   - **QR — Quality Requirements (why / what):** map each business goal to the
     quality risk it carries and the scope in/out. A reader should understand
     *what would hurt the business if it broke*.
   - **QV — Quality Verification (how / resources):** environments (staging
     URLs, never production), test accounts and roles, devices/browsers,
     cross-market or cross-role concerns, and **this release's focus + QA
     alerts** — the 2-5 things that most deserve attention this cycle. Stage 2
     reads these "alerts" to keep local detail aligned with global strategy.
4. **Import OQs from Stage 0.** If `00-open-questions.md` exists, incorporate its
   findings into the "Spec gaps / ambiguities found" section. Resolved OQs
   become boundary conditions for test design. Unresolved OQs are listed with
   their OQ-ID for traceability. If Stage 0 was skipped, flag anything
   ambiguous or contradictory you notice during the skim — but note that a
   dedicated spec audit would catch more systematically.

## Human gate

Present the brief and ask the QA lead one focused question: **"Is the risk
framing and the in/out scope right, and did I miss a high-risk surface?"** Stop.
Do not start stage 2 until scope is confirmed — everything downstream inherits it.

## Definition of done

- `01-quality-brief.md` exists, one page, both QR and QV filled (no `TBD`).
- Out-of-scope is explicit.
- Spec ambiguities, if any, are listed for the team.
