> **Feature plan:** [Step 1](./historical_cycle_expansion_step1_solution_assessment.md) · [Step 2](./historical_cycle_expansion_step2_feature_description.md) · [Step 3](./historical_cycle_expansion_step3_development_plan.md) · [Step 4](./historical_cycle_expansion_step4_implementation_summary.md)

Debug mode: disabled

## Problem
The existing debug-led study omits much of Railspike/FDP development history. A traceable census is needed before expanding outcome analysis without selecting only well-documented successes.

## User stories
- As maintainer, I want a catalog of historical cycles so that I can choose analysis batches covering the full eligible population.
- As reviewer, I want evidence, exclusions, and uncertainty attached to each classification so that I can challenge conclusions without reconstructing the census.

## Core requirements
- Inventory identifiable cycles in `~/railspike-dev` and `~/v3` at a recorded cutoff, including archived/FDP artifacts, incomplete cycles, and work without debug logs. Record discovery boundaries and inaccessible evidence; linked history may resolve identities, but exhaustive reconstruction of every Git revision is outside this cycle.
- Give every candidate a disposition; group copies, renames, and related documents under canonical cycle identities with reasons. Retain research cycles in the inventory but exclude them from their own outcome analysis. Unresolved identities remain visible.
- Classify canonical cycles as documented completion, completion with unmet gates, in-progress, explicitly abandoned/superseded, or indeterminate, citing evidence. Missing Step 4 does not prove abandonment; a summary does not prove success; skipped optional Step 1 is not incompleteness. Record later regressions separately.
- Record source provenance and fingerprints, task type, supported workflow era/version or unknown, evidence availability, and overlap with the original study. Distinguish reported claims from corroborated evidence and unknowns; preserve source documents and the original study cutoff.
- Deliver a dated catalog and reconciled coverage/gap report, with an explicit queue for subsequent analysis of all eligible completed cycles. This census does not substitute a sample or claim causal effectiveness, measured effort, or independently verified application outcomes.

## Delivery scope
**Documentation-only**, for maintainers and research reviewers. Allowed writes: Markdown under `docs/research/historical_cycle_expansion/`, this feature's `docs/plans/historical_cycle_expansion*` artifacts and eventual feature folder, and its entry in `docs/plans/README.md`. Existing research and both repositories' source evidence are read-only. Application/runtime, workflow-instruction, tooling, CI, deployment, generated-artifact, and paper/PDF changes are not permitted. Detailed outcome analysis, experiments, and publication are later cycles.

## Completion boundary
The maintainer can enter through the catalog, inspect each disposition and supporting evidence, reconcile totals, and select defensible analysis batches. Handoff requires document/link integrity and accounted-for candidates, including unresolved cases. Corrections append dated revisions with affected classifications/counts; retain the frozen baseline and never silently overwrite evidence.

## Risks
- **Duplicate or missed cycles distort coverage:** before Step 3, check representative archive/FDP/installed-copy naming; define discovery and identity rules with an explicit unresolved category.
- **Completion claims exceed evidence:** before Step 3, compare representative summaries with their supporting records; fix status definitions and missing-data treatment before collection.
- **Corpus size or drift prevents a reproducible handoff:** before Step 3, refresh candidate counts and confirm a feasible census boundary; record cutoff/provenance and defer deep analysis. Rescope for approval if a complete census cannot fit the stage budget.

## Shared component inventory
Reuse the existing [protocol](../../research/railspike_paper/protocol.md), [evidence register](../../research/railspike_paper/evidence.md), and [findings](../../research/railspike_paper/findings.md) as immutable references. Extend research coverage in the separate census documents; use the existing plan index for discovery. No UI/API surface is involved.

## Simple user flow
1. Open the census and read its boundary and classification rules.
2. Inspect canonical cycles, source mappings, exclusions, and unresolved cases.
3. Review reconciled totals and gaps; request a recorded correction or select the next analysis batch.

## Success criteria
Every discovered candidate has a disposition; every canonical cycle has a status, provenance, and evidence/unknown rationale. Totals reconcile across candidates, duplicates, exclusions, and canonical cycles. Prior-study overlaps and all unresolved cases are explicit; no source or original-study bytes change. The handoff identifies the complete eligible analysis queue without claiming that its analysis is already finished.
