> **Feature plan:** [Step 1](./exploratory_paper_step1_solution_assessment.md) · [Step 2](./exploratory_paper_step2_feature_description.md) · [Step 3](./exploratory_paper_step3_development_plan.md) · [Step 4](./exploratory_paper_step4_implementation_summary.md)

Debug mode: disabled

## Problem
Historical review has produced evidence but no coherent paper. The maintainer needs an early, revisable manuscript and complete eligible-record coverage without restarting planning for every batch.

## User stories
- As maintainer, I want a readable paper early so that I can review its argument while analysis continues.
- As research reviewer, I want every claim linked to evidence and limitations so that I can distinguish reported results from demonstrated effectiveness.

## Core requirements
- Deliver a complete provisional manuscript before the remaining review batches: abstract, motivation/workflow, research questions, methods, current results, discussion, limitations, future work and references. Initially label coverage as 25/216; do not present queued reviews as results. Keep it readable as a paper, with detailed records in supporting documents.
- Review all remaining 191 eligible IDs in existing queue order, in seven batches of 30/30/30/30/30/30/11. Reuse the first 25 with their corrections and the shared rubric; update cumulative evidence and manuscript after each batch. One approval cycle covers the work, with verified stage commits and resumable checkpoints. The approved exception permits exceeding one day/eight stages; material scope/method changes still require review.
- Preserve canonical identities, related incidents, prior-study overlaps, source provenance/excerpts and missing-data rules. Distinguish reports, inspected artifacts, independent reproduction and human review. Version rubric changes and recheck affected earlier records before combining results; append corrections without overwriting originals. All 95 adjudication IDs remain visible outside the fixed 216-record cohort.
- Trace empirical claims and tables to reviewed records and reconciled denominators; include counterevidence and selection, dependence, authorship and missingness limits. Verify cited literature against primary sources; limit related work to contextualizing this descriptive study. No unsupported novelty, causal effectiveness, population success-rate or developer-time-saving claims.
- Finish with a reconciled manuscript, complete coverage index and focused review/refinement checklist identifying central/disputed claims and excerpt suitability. Human coding review remains pending until actually performed; neither it nor exhaustive adjudication blocks the local draft. Public release remains a separate decision.

## Delivery scope
**Documentation-only**, for the maintainer and research reviewers. Allowed writes: Markdown under `docs/research/exploratory_paper/` (manuscript, continued analysis, provenance, references and review checklist), this feature's planning/debug artifacts and eventual feature folder, and its plan-index entry. Existing census, first-batch analysis, original study and source repositories remain read-only. No application/runtime, workflow-instruction, tooling, CI, deployment or generated-artifact changes. PDF production, publication, experiments and resolution of the 95-case queue are deferred.

## Completion boundary
Entry page → readable manuscript → claims/records/sources → remaining uncertainties and review checklist. Handoff requires 216 accounted-for eligible records and consistent final manuscript totals. Correct disputed claims through dated revisions, preserving source versions and earlier interpretations; unavailable evidence yields explicit uncertainty, not replacement candidates.

## Risks
- **Overclaiming or denominator drift:** before Step 3, check first-batch qualifications and queue membership; carry limitations into abstract/results and require reconciled totals after each batch.
- **Uneven evidence or oversized batches:** before Step 3, measure remaining source volume and access; allocate internal checkpoints without dropping records or restarting the four-step cycle. Unresolved evidence stays visible.
- **Source drift or disclosure:** before Step 3, inspect source/citation boundaries; preserve fingerprints and safe excerpts, distinguish later evidence, and flag public-release review needs.

## Shared component inventory
Reuse the [census](../../research/historical_cycle_expansion/coverage.md), [rubric](../../research/historical_outcome_analysis/rubric.md), [first-batch report/corrections](../../research/historical_outcome_analysis/README.md) and [complete queues](../../research/historical_outcome_analysis/progress.md). Add a separate manuscript/evidence continuation rather than rewriting prior studies. No UI/API surface applies.

## Simple user flow
1. Read the provisional paper and inspect its evidence and coverage label.
2. Follow batch updates as the same manuscript gains reviewed results.
3. Review the reconciled paper, qualifications and checklist before deciding on refinement or release.

## Success criteria
A coherent draft exists before batch review; seven completed batches cover 191 new records exactly once. Final coverage is 25 + 191 = 216, with 95 separate adjudication cases. Every empirical claim/table is traceable, citations and local links validate, originals remain unchanged, and no independent review or publication is falsely claimed.
