> **Feature plan:** [Step 1](./historical_outcome_analysis_step1_solution_assessment.md) · [Step 2](./historical_outcome_analysis_step2_feature_description.md) · [Step 3](./historical_outcome_analysis_step3_development_plan.md) · [Step 4](./historical_outcome_analysis_step4_implementation_summary.md)

Debug mode: disabled

## Original Query
Please go ahead and write Step 1.

## Understood Intent
Begin `historical_outcome_analysis` following the completed census: define consistent evidence and outcome criteria for the 216 eligible candidates, drawing on the original study, while retaining the 95 uncertain or unfinished candidates in a separate adjudication queue.

## Problem
The census establishes retained-document identities and completion classifications, but does not yet consistently assess whether the evidence supports the initiating user outcomes or reported contributions of Railspike/FDP.

## Evidence and Boundary
The [census handoff](../../research/historical_cycle_expansion/coverage.md) identifies 216 eligible candidates, including completion with unmet gates; eligibility is not success. Preserve its cutoff, [corrections](../../research/historical_cycle_expansion/corrections.md), research exclusions and duplicate mappings. Extend the [original protocol](../../research/railspike_paper/protocol.md) and [findings](../../research/railspike_paper/findings.md) without overwriting them or treating overlapping workflows as new independent observations.

## Option A — Summarize completion reports
Extract a common set of outcomes directly from all eligible summaries, adding debug observations where available.

- **Pros:** Fast broad coverage; straightforward descriptive tables.
- **Cons:** Repeats self-reports; weak checks of initiating acceptance criteria, recovery, contradictions and later corrections.

## Option B — Analyze evidence in bounded batches
Apply one shared rubric to every eligible candidate over successive batches, comparing requests/plans with retained verification, summaries, corrections and relevant commit evidence.

- **Pros:** Traceable outcome judgments; consistent missing-data treatment; preserves full-coverage intent and enables review before synthesis.
- **Cons:** Requires multiple cycles; document availability varies; retrospective evidence cannot establish causal benefit or recover unmeasured effort.

## Option C — Reconstruct every execution
Audit full available histories, diffs and conversations for every candidate before reporting outcomes.

- **Pros:** Strongest historical corroboration and contradiction checking where records survive.
- **Cons:** Unbounded effort and incomplete transcripts; still cannot establish a controlled comparison or independently reproduce runtime outcomes.

## Recommendation
Choose **Option B**, using deeper reconstruction for contradictions that could change an outcome judgment.

- **Common criteria:** Separate claimed completion, ordinary-entry/recovery acceptance evidence, verification coverage and unmet gates, rework/later regressions, approval/scope assessability, and reported instruction benefits/friction. Distinguish reports, inspected artifacts, independent reproduction and human coding review; missing evidence stays unknown. Historical model/instruction versions and human effort require explicit evidence.
- **First complete slice:** Fix a dated rubric and analyze the first 25 candidates in the existing eligible-analysis queue, producing source-linked judgments, an evidence-gap report and reconciled progress toward all 216. Use queue order rather than selecting favorable or dramatic cases. Confirm this fits one day/eight stages during planning; reduce the declared first batch before approval if necessary, retaining every deferred ID.
- **Evidence integrity:** Preserve source versions/excerpts supporting judgments and flag drift from the census cutoff. Append corrections; keep disputed cases visible and block dependent conclusions. Related workflows and repeated incident accounts are not independent trials; report denominators and missingness explicitly.
- **Scope:** Documentation-only, local research. Keep the 95-case adjudication queue visible but defer its resolution; do not silently add uncertain cases to outcome totals. Preserve historical sources and the original study. Later batches, cross-corpus synthesis, human review, runtime reproduction, prospective experiments, workflow changes and publication require separate scope.
