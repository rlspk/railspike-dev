> **Feature plan:** [Step 1](./plan_length_guidance_step1_solution_assessment.md) · [Step 2](./plan_length_guidance_step2_feature_description.md) · [Step 3](./plan_length_guidance_step3_development_plan.md) · [Step 4](./plan_length_guidance_step4_implementation_summary.md)

Debug mode: enabled

# Step 1: Solution Assessment — Plan length guidance

## Original Query

How would the word budgets work? Does it make sense to even have them? Is this where the Railspike unit really comes from? Like the size of the Railspike unit, I mean. […] Is there a correlation between word count and complexity score? […] Do you think going from page size to word count limitations or suggested limitations, or like suggestions, will affect our Railspike scoring? […] Okay, just for clarity's sake and to make it easier for me to just handle cognitively, can you please do this as two separate changes?

## Understood Intent

Replace the "≤1 page" rule in Steps 1–3 with length guidance that agents can follow without apologizing for it. Keep the effort study clean while the rule changes. The debug-log agent field is a separate cycle.

## Problem Statement

The "≤1 page" rule has no definition, collides with required metadata and penalizes the cycles we already judge acceptable.

## Evidence

- 104 of 189 debug logs in v3 flag the page limit, mostly to justify going over it.
- Median v3 plan length is 500 words for Step 1, 660 for Step 2 and 719 for Step 3. Most Step 2 and Step 3 plans already exceed a printed page.
- Across 74 effort-scored v3 cycles, Step 3 length tracks the cycle estimate (correlation about 0.6). Step 1 length barely does (about 0.2).
- Median Step 3 length rises from 755 words below 0.3 to 1,531 words at 0.9 and above.
- The effort unit R1 never mentions length. Length is a scope signal, not the definition of 1.0.

## Concepts touched

- Step length rule: changed in every option.
- Step 3 stage sizing: unchanged in Options A and C; changed in Option B.
- Effort study ledger: gains one dated note in every option.

## Option A — One reading-time target for every step

Replace "≤1 page" with one goal: a reviewer reads the artifact in about three minutes and knows what they are approving. Navigation, debug state, attribution and effort fields do not count toward it.

- Pro: one simple rule, and it states the purpose instead of a unit.
- Pro: required metadata stops causing overruns.
- Con: a large Step 3 still cannot fit, so agents keep apologizing at the top of the scale.

## Option B — Targets by step, with Step 3 sized per stage

Steps 1 and 2 get the reading-time target from Option A. Step 1 also gets a soft target of about 100 words per option. Step 3 has no whole-document target. Each stage gets a short budget instead, and a long plan becomes a reason to raise the existing split discussion.

- Pro: matches the data; Step 3 length grows with real scope.
- Pro: reuses the split discussion that scores above 1.0 already trigger.
- Con: per-stage budgets may push agents toward more, smaller stages.
- Con: two rules to explain instead of one.

## Option C — Hard word limits per step

Set fixed word caps, such as 400 for Step 1, 600 for Step 2 and 900 for Step 3.

- Pro: measurable, and agents can check it themselves.
- Con: moves the friction to a new number instead of removing it.
- Con: Codex follows caps literally and would cut evidence to fit.

## Effort study handling (all options)

Record the rule change and its UTC date in the effort ledger before the first cycle that uses it. Original estimates come before Step 3 exists, so they act as a control. Compare how far cycle estimates drift from original estimates before and after the change. Optionally re-score two or three R1 reference cycles under the new rule without showing earlier scores.

## Recommendation

Option B as the vertical slice. It removes the contradiction agents report most and keeps Step 3 honest about scope. The change touches only instruction text in Railspike plus one ledger note; no existing plans are rewritten.

*— Claude · 2026-11-11 UTC · Model: claude-opus-5-5*
