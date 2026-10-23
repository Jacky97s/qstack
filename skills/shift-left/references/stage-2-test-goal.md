# Stage 2 — Test Goals

**Goal:** distill the spec into a list of **Goals** — the business capabilities
and quality attributes worth verifying this release. This is *what we test*,
not yet *how*. Scenarios and objectives are decomposed later in Stage 4; here
we only name the goals, tie each to the spec, and rank them by risk. Output
`02-test-goals/test-goals.md`.

## The Goal concept

A **Goal** is a business capability or quality attribute worth verifying, drawn
from the Quality Brief's QR (Quality Requirements). One goal per meaningful
requirement cluster — not one per AC (too fine), not one per feature area (too
coarse). ID: `G1, G2, ...`.

A good goal names something whose breakage would *hurt the business* — the same
lens the Quality Brief used. Stage 4 will break each goal into concrete
scenarios; if a goal can't be decomposed into a happy path plus a negative and
a boundary, it is probably too narrow to be a goal.

## Process

1. Read `01-quality-brief/quality-brief.md`, especially its QR half (business
   goals → quality risks) and the focus + QA alerts. Pull the relevant
   acceptance criteria from the spec sections the brief points at.
2. Identify the goals: cluster the QR's business goals and risks into
   verification targets. Every QR goal in the brief must map to at least one
   test goal — no QR goal left without coverage intent.
3. For each goal, write its entry (format below): an ID, a name, the spec
   references it traces to, the quality-risk description (what hurts the
   business if it breaks), and a priority.
4. Assign `priority` (P0 blocker / P1 / P2 / P3) tied to the Quality Brief's
   risk framing — the riskier the surface the brief flagged, the higher the
   priority.

## Goal entry format

```markdown
## G1 — <business capability or quality attribute>

- **Spec:** <doc#section / AC id>
- **Quality risk:** <what hurts the business if this breaks>
- **Priority:** P0/P1/P2/P3
```

## Goal completeness check (self-check before the gate)

- Every QR goal in the Quality Brief has a corresponding test goal (no orphan
  requirement).
- Every goal traces to a spec AC / section.
- Every goal carries a quality-risk description and a priority.
- No goal is so narrow it can't later yield a happy + negative + boundary set
  (that is a sign it should fold into a broader goal).

## Human gate

Present the goal list with priorities and the completeness self-check, then
ask: **"Are the test goals complete — any missing business capability, and are
the risk descriptions and priorities right?"** Stop. Scenario decomposition is
Stage 4; do not start it until the goal set and priorities are confirmed —
everything downstream inherits them.

## Definition of done

- `02-test-goals/test-goals.md` lists every goal with an ID, name, `spec_ac`,
  quality-risk description, and priority.
- Every QR goal from the Quality Brief has a corresponding test goal.
- No scenarios, no `test-index.csv` — those are seeded in Stage 4.
