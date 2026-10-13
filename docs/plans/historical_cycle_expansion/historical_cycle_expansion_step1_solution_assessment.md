> **Feature plan:** [Step 1](./historical_cycle_expansion_step1_solution_assessment.md) · [Step 2](./historical_cycle_expansion_step2_feature_description.md) · [Step 3](./historical_cycle_expansion_step3_development_plan.md) · [Step 4](./historical_cycle_expansion_step4_implementation_summary.md)

Debug mode: disabled

## Original Query
OK, please write Step 1 for that expansion.

## Understood Intent
Expand the existing empirical-whitepaper research to all available completed Railspike and FDP (its former name) cycles in this repository and `~/v3`, including cycles without debug logs. Inventory incomplete work too, preserve the original study snapshot, and exclude research cycles from their own outcome analysis.

## Problem
The debug-led study covers only a small, selected subset of development history, limiting what it can describe about actual workflow use and outcomes.

## Evidence and Boundary
- Initial inventory found nine Step 4 summaries here and 190 in `~/v3`, including this study; only six in each repository have matching debug logs. These are candidate documents, not 199 verified completed cycles.
- The [existing protocol](../../research/railspike_paper/protocol.md) and [findings](../../research/railspike_paper/findings.md) distinguish claims, artifacts, and independently verified outcomes. Preserve those distinctions and the original cutoff; add a separately dated expansion with links to overlapping records.

## Option A — Add completed-cycle summaries only
Extract outcomes from every available Step 4 summary, attaching debug observations where present.

- **Pros:** Broadens coverage quickly; straightforward descriptive comparison across tasks.
- **Cons:** Completion labels may conceal unmet gates; omits abandoned work and loses decisions/rework visible in earlier plans or commits.

## Option B — Census cycles, then analyze completion evidence
Inventory all identifiable cycles, classify their status, and analyze every completed cycle using its request, plans, summary, and available verification/commit evidence; debug logs provide an additional perspective.

- **Pros:** Covers work without diagnostics; preserves an incomplete-work denominator; supports traceable comparisons by task type and workflow era.
- **Cons:** Requires careful cycle matching, status definitions, and missing-data handling; likely needs several bounded research cycles.

## Option C — Full forensic reconstruction
Reconstruct every candidate's entire decision and implementation history, checking claims against detailed diffs, retained transcripts, and original verification artifacts.

- **Pros:** Strongest available historical attribution and contradiction checking.
- **Cons:** Missing conversations/results remain unrecoverable; substantial effort; still lacks an experimental baseline or measured human effort.

## Recommendation
Choose **Option B**, using Option C's deeper review for disputed claims rather than requiring exhaustive reconstruction everywhere.

- **Coverage:** Include archived and differently named FDP artifacts; deduplicate installed copies, renames, revisions, and related accounts. Record workflow version when supported, otherwise unknown. Skipped optional Step 1 is not incompleteness.
- **Classification:** Distinguish documented completion, completion with unmet gates, in-progress, explicitly abandoned/superseded, and indeterminate. Missing Step 4 does not prove abandonment; a Step 4 file does not prove success. Record later regressions separately from original completion evidence.
- **First complete slice:** Deliver a frozen cycle catalog, provenance, explicit inclusion/status decisions, links to existing study records, and coverage/gap findings. The maintainer can inspect the population and choose defensible analysis batches. Unresolved identities/statuses remain visible for correction rather than silently disappearing.
- **Expansion path:** Scope this census in Step 2; analyze all eligible completed cycles in subsequent bounded batches, then synthesize. Every completed cycle receives the same core fields; deeper case selection needs stated criteria. Do not silently substitute a sample for full coverage or force roughly 200 histories into one day's work.
- **Limits:** Keep both repositories' source evidence unchanged; preserve negative cases and unknown measurements. The expansion strengthens descriptive evidence, not causal effectiveness claims. New experiments, workflow changes, and paper/PDF publication remain separate work.
