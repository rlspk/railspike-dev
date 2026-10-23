> **Feature plan:** [Step 1](./detailed_effort_estimates_step1_solution_assessment.md) · [Step 2](./detailed_effort_estimates_step2_feature_description.md) · [Step 3](./detailed_effort_estimates_step3_development_plan.md) · [Step 4](./detailed_effort_estimates_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/detailed_effort_estimates`; standing R1/P2 enrollment; [ledger](../../research/effort_estimation/collection.md).

## Original Query

Let's proceed with implementing this; we may have already written a Step 1?

## Understood Intent

Extend effort estimation to every Step 1 option and every stage in Steps 3 and 4. Earlier conversation and the clone review recommended per-option estimates, but no dedicated Step 1 was found in the current development tree or local/remote-tracking branch histories. The completed reference-recovery cycle explicitly excluded this work.

## Problem

Whole-cycle checkpoint scores leave the relative cost of alternatives and individual stages implicit.

## Option A — Explicit scoped effort estimates

In an opt-in extension, estimate each Step 1 option's complete scoped cycle on R1. Estimate each Step 3 stage's own work, including its verification and documentation, in relative effort units using the same reference yardstick. Keep those stage annotations distinct from formal whole-cycle projections. Step 4 inherits the original stage estimates, appends material revisions before dependent work, and records separately labeled retrospective assessments at stage completion.

- Pros: directly compares alternatives and stage difficulty; preserves estimates through discoveries; uncertainty ranges and a short complexity driver make the numbers interpretable.
- Cons: stage-level judgments lack dedicated calibration; shared work makes stage totals non-additive. Stage annotations must not become extra cycle observations or silently replace the whole-cycle score.
- Estimated effort for implementing this option: **0.60 R1**, plausible **0.45–0.85**; main uncertainty is clear stage-versus-cycle semantics and concise revision examples.

## Option B — Cycle scores with stage work shares

Estimate every Step 1 option's whole-cycle total on R1, then allocate an explicit stage-work budget across Step 3 stages as percentages. Step 4 preserves the original allocation and records revised shares and retrospective judgments separately; the cycle's planning/inspection overhead remains separately identified.

- Pros: makes the distribution of work easy to scan; avoids presenting partial stages as full-cycle scores.
- Cons: shares describe allocation rather than absolute stage difficulty; scope changes force redistribution, and percentage precision can imply an unsupported additive forecast. Shares cannot be treated as measured time or percentage complete.
- Estimated effort for implementing this option: **0.50 R1**, plausible **0.35–0.75**; main uncertainty is avoiding misleading normalization and handling shared work.

## Recommendation and vertical slice

Choose **A**: option comparison → scoped requirements → estimated stages → inherited/revised/completed stage records. Retain an independently judged whole-cycle total; do not sum stages, multiply a score into hours, or add alternative/combined-option scores. Re-estimate combined approaches. Label unavailable values and uncertainty honestly; stage completion without reliable time measurements yields a retrospective judgment, not “actual effort.”

Make the extension optional and inheritable through host policy; preserve existing non-enrolled behavior, R1 sources and approval/commit rules. Supply compact examples for an option, a stage and a discovery-driven revision. Treat length as a concise decision summary with linked estimate history; do not redesign unrelated workflow policies. Verify document consistency and scenario walkthroughs. Beta preparation/publication is a later explicitly scoped action, not accomplished by drafting this assessment.

## Effort snapshots and requests

Recorded 2026-10-23T19:21:20Z; scope v1, R1/P2; starting development `2bf34ea1fd0821078b4aada9746929154ff11e54`, product `742d1d74f11fcf1b2e91eec9ecae7848489b0520`. Codex, single exposed rater. Prior clone review, recovery work, inherited scores and current instructions were already read; the branch/plan search preceded intake, so no pristine intake is claimed. All three frozen source hashes verified. Post-inspection intake **0.60**, Step 1 **0.60 reaffirmed** for A, including planning, documentation and verification; ranges are subjective, not calibrated confidence intervals.

Request: implement extended option/stage estimates and find prior Step 1 / disposition: new linked cycle, existing recommendation reused / authorization: assessment and implementation intent received; staged planning review remains applicable / outcome: Step 1 drafted; no product change, later deliverable or beta publication.

Await **Approved Step 1** before defining Step 2.

### Approval received

2026-10-23 UTC: user explicitly replied “Approved Step 1.” Option A is approved; the preceding waiting state is historical. Step 2 drafting authorized; development-plan approval and implementation remain pending.
