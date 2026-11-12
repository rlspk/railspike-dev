> **Feature plan:** [Step 1](./plan_length_guidance_step1_solution_assessment.md) · [Step 2](./plan_length_guidance_step2_feature_description.md) · [Step 3](./plan_length_guidance_step3_development_plan.md) · [Step 4](./plan_length_guidance_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/plan_length_guidance`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md)

Extended estimates: enabled

**Cycle estimate: 0.30**

# Step 2: Feature Description — Plan length guidance

Step 1 approved 2026-11-12 ("Approved, step 1."); Option B selected.

## Problem

The "≤1 page" rule in Steps 1–3 has no definition and collides with required metadata. Agents in v3 justify going over it in 104 of 189 debug logs.

## User stories

- As a maintainer, I want each plan to say how long it should be in terms I can check, so that I review plans instead of length apologies.
- As an agent, I want required metadata kept out of the length goal, so that following one rule never breaks another.
- As a maintainer, I want a long Step 3 to prompt a split discussion, so that plan length warns me about scope instead of hiding it.
- As the effort study, I want the rule change dated in the ledger, so that score drift can be compared before and after.

## Core requirements

- Steps 1 and 2 replace "≤1 page" with one goal: a reviewer reads the artifact in about three minutes and knows what they are approving.
- Navigation, debug state, effort fields and attribution never count toward any length goal.
- Step 1 gets a soft target of about 100 words per option.
- Step 3 drops the whole-document limit. Each stage gets a short text budget, set in Step 3. A plan that runs long raises the existing split discussion.
- Stage work sizing ("about ≤1 hour or ≤50 lines") stays unchanged; this cycle changes only how long the plan text is.

## Delivery scope

- Work type: application change to Railspike instructions.
- Product: `docs/workflow/step1_solution_assessment.md`, `docs/workflow/step2_feature_description.md`, `docs/workflow/step3_development_plan_do.md`, `docs/workflow/step3_development_plan_after.md`, the Warning Signs in `RAILSPIKE.md`, and the plan-length line in `README.md`.
- Development: this cycle's plans and debug log, the plan index entry, and one dated ledger note in `docs/research/effort_estimation/collection.md`.
- Not in scope: rewriting existing plans, changing R1 or stage work sizing, the v3 ledger, and the before/after drift analysis.

## Completion boundary

- Normal entry: an agent starts any Step 1–3 artifact and reads its deliverable line.
- Outcome: the agent knows the length goal for that step and that metadata is excluded. No instruction still mentions a page.
- Recovery: revert the product stage commits; the ledger note stays as history.
- Handoff: product changes on an unmerged branch with the ledger note committed in `railspike-dev`.

## Risks

- **High risk:** "about three minutes" may read as vague as "one page". Earliest validation: Step 3 drafting. Mitigation: pair it with a rough word figure that agents can check.
- Per-stage budgets may push agents toward more, smaller stages and inflate Step 3 estimates. Earliest validation: the next few real cycles. Mitigation: the dated ledger note lets the study separate this effect.
- Codex reads targets literally and may cut evidence to fit. Mitigation: call the targets soft and say evidence comes first.

## Shared component inventory

- Length rules live in the four workflow files and two `RAILSPIKE.md`/`README.md` lines listed under Delivery scope; every occurrence of "page" in the product was found by search.
- Reuse the split discussion that [R1](../../../../railspike/docs/effort-estimation.md) already ties to scores above 1.0; no new escalation path.
- Reuse the [writing style](../../../../railspike/RAILSPIKE.md#writing-style) section as the place readers already look for prose rules.

## Concepts touched

None. The concept inventory has no entry for plan length.

## User flow

1. An agent opens a step's instruction file and reads the length goal.
2. The agent writes the artifact, leaving metadata out of the count.
3. For Step 3, the agent keeps each stage within its budget.
4. If the plan still runs long, the agent raises a split in the handoff.
5. The maintainer reviews the plan without length apologies.

## Success criteria

- No product file mentions a page limit for plans.
- Each Step 1–3 file states its length goal and the metadata exclusion.
- The ledger has a dated note before the first cycle that uses the new rule.
- Later v3 debug logs stop flagging the page limit; checked in a separate analysis.

## Study history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| Intake | unavailable | Missing. Scope was discussed and v3 logs inspected before any estimate. |
| 2026-11-11 — Step 1 handoff | unavailable | Missing. The Step 1 snapshot was not recorded; not reconstructed. |
| 2026-11-12 — Step 2 handoff | 0.30 | Option B: six product files, one ledger note. Exposed single Claude rater, R1/P2. |

*— Claude · 2026-11-12 UTC · Model: claude-opus-5-5*
