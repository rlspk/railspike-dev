> **Feature plan:** [Step 1](./historical_outcome_analysis_step1_solution_assessment.md) · [Step 2](./historical_outcome_analysis_step2_feature_description.md) · [Step 3](./historical_outcome_analysis_step3_development_plan.md) · [Step 4](./historical_outcome_analysis_step4_implementation_summary.md)

Debug mode: enabled

## Problem
The census classifies retained completion records without consistently assessing evidence of the initiating user outcome. Maintainers need comparable, traceable judgments before interpreting Railspike/FDP results.

## User stories
- As maintainer, I want consistent outcome records so that I can distinguish delivered acceptance evidence from completion claims.
- As reviewer, I want sources, uncertainty and corrections beside each judgment so that I can challenge it and identify remaining research.

## Core requirements
- Analyze exactly the 25 candidates in the census's [eligible-analysis batch 1](../../research/historical_cycle_expansion/coverage.md#complete-eligible-analysis-queue), C002 through C036 with the listed gaps. Preserve canonical IDs, duplicate/incident relationships, research exclusions and prior-study overlaps; retain the remaining 191 eligible IDs and separate 95-case adjudication queue without analyzing them here.
- Fix a dated common rubric before coding: claimed completion; ordinary-entry and required-recovery acceptance; verification coverage/unmet gates; rework versus later regressions; approval/scope assessability; reported instruction benefits/friction. Record task/context and evidenced workflow/model versions and human effort, otherwise unknown. Separate reported, artifact-supported, independently reproduced and human-reviewed evidence; absence is not success, failure or zero.
- Inspect initiating requests/plans alongside summaries, retained verification, corrections and relevant available commit evidence. Give every judgment source attribution or an explicit unknown rationale; investigate material contradictions or leave them unresolved. Another agent's summary is not independent validation. New tests and human review are not performed by this slice.
- Capture dated provenance, fingerprints and sufficient exact excerpts to inspect judgments; identify changed/unavailable census sources and distinguish later evidence from the earlier cutoff. Preserve originals, screen excerpts for secrets/unrelated personal data, and append corrections with old/new interpretations and affected totals.
- Deliver a linked batch report, evidence gaps and full progress queue. Reconcile denominators and missingness; related cycles are not independent trials. No causal, population success-rate or time-saving claims, and no cross-corpus conclusion from this first batch.

## Delivery scope
**Documentation-only**, for maintainers/research reviewers. Allowed writes: Markdown under `docs/research/historical_outcome_analysis/`, this feature's planning/debug artifacts and eventual `docs/plans/historical_outcome_analysis/` folder, and its plan-index entry. Existing census, original study and historical sources remain read-only. Application/runtime, tooling, CI, deployment and generated-artifact changes are prohibited. Later batches, adjudication, experiments, human review and publication are separate work.

## Completion boundary
A reviewer can navigate the entry page → rubric → all 25 evidence-backed records → gaps/progress queue. Handoff requires reconciled coverage and document-integrity checks, not favorable outcomes. Disputes receive dated corrections; unresolved evidence blocks dependent conclusions without erasing the record.

## Risks
- **Self-report overstatement:** before Step 3, compare ordinary completion and unmet-gate examples; require claim/evidence separation and unknowns.
- **Drift or duplicate evidence:** before Step 3, check source availability and overlap mappings; preserve cutoff differences and canonical attribution.
- **Capacity:** before Step 3, estimate first-batch source volume/deep-review needs; fit one day/eight stages or revise this boundary for approval, retaining deferred IDs.

## Shared component inventory
Reuse the census [register](../../research/historical_cycle_expansion/sources.md), [corrections](../../research/historical_cycle_expansion/corrections.md) and queues, plus the original [protocol](../../research/railspike_paper/protocol.md). Extend through separate research documents and existing plan navigation; no UI/API surface applies.

## Simple user flow
1. Read scope and rubric; inspect each candidate's claims and evidence.
2. Review uncertainty, contradictions and dated corrections.
3. Reconcile batch coverage and select subsequent work from the remaining queue.

## Success criteria
25/25 records contain every rubric field with evidence or unknown rationale; 25 reviewed + 191 pending = 216 eligible, with 95 adjudication cases separate. All active links/citations and scoped writes validate; source preservation/drift is accounted for. Human review remains explicitly pending.
