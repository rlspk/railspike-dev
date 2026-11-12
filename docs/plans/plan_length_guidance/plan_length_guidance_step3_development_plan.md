> **Feature plan:** [Step 1](./plan_length_guidance_step1_solution_assessment.md) · [Step 2](./plan_length_guidance_step2_feature_description.md) · [Step 3](./plan_length_guidance_step3_development_plan.md) · [Step 4](./plan_length_guidance_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/plan_length_guidance`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md)

Extended estimates: enabled

**Cycle estimate: 0.30**

# Step 3: Development Plan — Plan length guidance

Step 2 approved 2026-11-12 ("approved step 2").

## Completion Contract

- Normal entry: an agent opens a Step 1, 2 or 3 instruction file and reads its deliverable line.
- Outcome: the agent finds a length goal it can check, knows metadata is excluded, and finds no page limit anywhere in the product.
- Recovery: revert the two product stage commits. The ledger note stays as history.
- Deployment and external checks: none; Railspike ships as Markdown. Live agent behavior is checked in later cycles, not here.
- Release condition: product changes on an unmerged branch, the ledger note committed in `railspike-dev`, and maintainer review.

## Key Risks

- **High risk:** "about three minutes" stays as vague as "one page". Impact: agents keep apologizing for length. Early validation: Stage 1 review of the new wording. Mitigation: pair the reading time with "about 600 words".
- Per-stage budgets push agents toward more, smaller stages. Impact: Step 3 estimates drift up. Early validation: the next few real cycles. Mitigation: Stage 3 dates the change in the ledger.
- Codex cuts evidence to fit a number. Impact: thinner plans. Early validation: the first Codex cycle after release. Mitigation: call every target soft and say required content comes first.

## Concepts touched

None. The concept inventory has no entry for plan length.

## Stage 1 — Shared length rule and Steps 1–2

**Estimate: 0.10**

- Goal: one shared length rule exists, and Steps 1 and 2 point to it.
- Dependencies: none.
- Expected changes:
  - `RAILSPIKE.md` Writing style gains a short "Plan length" paragraph: reading time and word figures are soft targets, metadata never counts, and required content wins over any target.
  - `docs/workflow/step1_solution_assessment.md` and `docs/workflow/step2_feature_description.md` replace "≤1 page" with "about a three-minute read (about 600 words)", linked to the new paragraph. Step 1 adds about 100 words per option.
  - `RAILSPIKE.md` Warning Signs for Steps 1 and 2 replace ">1 page" with "well past the length goal".
- Verification approach: search the touched files for "page"; read each changed line in context; product link check; `git diff --check`.
- Estimate details: driver: three files, wording judgment; uncertainty: low.
- Risks or open questions:
  - Impact: a new paragraph could duplicate attribution or metadata rules.
  - Early warning / validation: diff review against Agent attribution and Debug mode.
  - Mitigation: list metadata by name and link, never restate those rules.
- Canonical components/API contracts touched: Writing style section, reused as the home for prose rules; no new section elsewhere.

## Stage 2 — Step 3 per-stage budget and README

**Estimate: 0.10**

- Goal: Step 3 sizes text by stage, and a long plan raises a split.
- Dependencies: Stage 1, for the shared paragraph.
- Expected changes:
  - `docs/workflow/step3_development_plan_do.md` drops "(<=1 page)" and adds a soft budget of about 200 words per stage. A stage that cannot fit its required fields in that budget becomes a split candidate, raised like the existing eight-stage rule.
  - `docs/workflow/step3_development_plan_after.md` checklist item 1 replaces "Verify <=1 page" with the per-stage check.
  - `RAILSPIKE.md` Warning Signs for Step 3 replace ">1 page" with "stages well past their text budget".
  - `README.md` replaces the one-page sentence with the new goals in plain words.
  - Stage work sizing ("about <=1 hour or <=50 lines") stays as it is.
- Verification approach: search the whole product for "page"; read each changed line in context; product link check; `git diff --check`.
- Estimate details: driver: four files, one new escalation sentence; uncertainty: low.
- Risks or open questions:
  - Impact: readers confuse text budget with stage work sizing.
  - Early warning / validation: read both rules side by side in the Do file.
  - Mitigation: name them differently, "text budget" and "stage size".
- Canonical components/API contracts touched: existing eight-stage split rule and Step 3 After checklist, both extended; no new escalation path.

## Stage 3 — Ledger note and closeout

**Estimate: 0.05**

- Goal: the effort study can tell scores before and after the rule change.
- Dependencies: Stage 2.
- Expected changes:
  - `docs/research/effort_estimation/collection.md` gains a dated protocol note naming the product commit. It states that R1 and stage size are unchanged.
  - The plan index entry, the Step 4 summary and the debug log close out the cycle.
- Verification approach: `railspike-dev` link check, with failures from missing sibling checkouts identified; `git diff --check`.
- Estimate details: driver: one note and closeout records; uncertainty: low.
- Risks or open questions: none beyond Key Risks.
- Canonical components/API contracts touched: effort ledger, existing note format.

## Study history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| Intake | unavailable | Missing; see Step 2. |
| 2026-11-11 — Step 1 handoff | unavailable | Missing; see Step 2. |
| 2026-11-12 — Step 2 handoff | 0.30 | Option B: six product files, one ledger note. |
| 2026-11-12 — Step 3 handoff | 0.30 | Reaffirmed; the shared paragraph adds little. Exposed single Claude rater, R1/P2. |

*— Claude · 2026-11-12 UTC · Model: claude-opus-5-5*
