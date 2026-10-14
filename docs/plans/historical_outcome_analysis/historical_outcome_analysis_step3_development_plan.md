> **Feature plan:** [Step 1](./historical_outcome_analysis_step1_solution_assessment.md) · [Step 2](./historical_outcome_analysis_step2_feature_description.md) · [Step 3](./historical_outcome_analysis_step3_development_plan.md) · [Step 4](./historical_outcome_analysis_step4_implementation_summary.md)

Debug mode: enabled

## Completion Contract
- Documentation-only writes: Markdown under `docs/research/historical_outcome_analysis/`, this feature's planning/debug artifacts and eventual folder, and its plan-index entry. Reviewer entry → rubric → 25 source-linked outcome records → gaps and full queues; 191 eligible candidates remain pending and 95 adjudication cases stay separate. No representative-sample claim.
- Preserve historical sources, census and original study. Freeze provenance/excerpts; distinguish later evidence and append dated corrections. Unresolved claims block dependent conclusions. Runtime, deployment, release, experiments, publication and independent human review are outside scope.
- Seven stages, each estimated <=1 hour. After Step 3 approval: branch, organize plans/debug log and commit approved plans plus organization first; verify, summarize and commit each stage before advancing. If eight stages/one day becomes infeasible, return to Step 2 before reducing coverage.

## Key Risks
- **High risk: evidence overstatement.** C002 reports checks without independent reproduction; C005 explicitly leaves review/live verification pending; C025 retains older unfinished text beneath a later completion update. Compare claims, acceptance and dated corrections; never infer approvals, effort or success from missing evidence.
- **High risk: provenance/identity drift.** Preflight: all 102 mapped sources (5,665 lines) exist and match census fingerprints; overlap mappings retain original-study IDs. Capture supporting sources separately, recheck at handoff, preserve duplicate/incident relationships and label unavailable evidence.
- Capacity: five groups contain 942–1,328 mapped lines each, excluding supplemental history. Bound targeted corroboration; unresolved contradictions remain visible. Validate actual capacity during Stage 1; do not silently sample or omit fields.

## Stage 1
- Goal: frozen evidence boundary and usable rubric.
- Dependencies: approved-plan organization commit.
- Expected changes: entry, dated rubric, provenance and exact 25-ID assignment; retain full queues.
- Verification approach: reconcile census IDs, fingerprints and overlaps; trial rubric against completion/unmet-gate/nonstandard examples before coding; check links/scope.
- Risks or open questions: ambiguous definitions or excessive volume block review; clarify or rescope first.
- Canonical components/API contracts touched: new research entry/rubric/register; existing census/protocol read-only; no API.

## Stage 2
- Goal: five reviewable outcome records: C002, C005–C008.
- Dependencies: Stage 1 verified/committed; fixed rubric.
- Expected changes: complete rubric fields, source excerpts and evidence/unknown rationales; update progress.
- Verification approach: compare requests/plans, summaries, corrections and available relevant commit evidence; check all fields/citations, identities, links and scope.
- Risks or open questions: self-report versus observed acceptance; inspect counterevidence and preserve unresolved judgments. Base volume: 1,104 lines.
- Canonical components/API contracts touched: shared rubric/register and batch records; sources read-only.

## Stage 3
- Goal: five reviewable outcome records: C009, C010, C012–C014.
- Dependencies: Stage 2 verified/committed; fixed rubric.
- Expected changes: complete rubric fields, source excerpts and evidence/unknown rationales; update progress.
- Verification approach: compare requests/plans, summaries, corrections and available relevant commit evidence; check all fields/citations, identities, links and scope.
- Risks or open questions: original-study overlap and repeated claims; inspect counterevidence and preserve unresolved judgments. Base volume: 1,328 lines.
- Canonical components/API contracts touched: shared rubric/register and batch records; sources read-only.

## Stage 4
- Goal: five reviewable outcome records: C015–C019.
- Dependencies: Stage 3 verified/committed; fixed rubric.
- Expected changes: complete rubric fields, source excerpts and evidence/unknown rationales; update progress.
- Verification approach: compare requests/plans, summaries, corrections and available relevant commit evidence; check all fields/citations, identities, links and scope.
- Risks or open questions: website gates and distinct FDP-era identities; inspect counterevidence and preserve unresolved judgments. Base volume: 1,171 lines.
- Canonical components/API contracts touched: shared rubric/register and batch records; sources read-only.

## Stage 5
- Goal: five reviewable outcome records: C020, C024, C025, C028, C029.
- Dependencies: Stage 4 verified/committed; fixed rubric.
- Expected changes: complete rubric fields, source excerpts and evidence/unknown rationales; update progress.
- Verification approach: compare requests/plans, summaries, corrections and available relevant commit evidence; check all fields/citations, identities, links and scope.
- Risks or open questions: nonstandard records and superseded status passages; inspect counterevidence and preserve unresolved judgments. Base volume: 942 lines.
- Canonical components/API contracts touched: shared rubric/register and batch records; sources read-only.

## Stage 6
- Goal: five reviewable outcome records: C030–C032, C035, C036.
- Dependencies: Stage 5 verified/committed; fixed rubric.
- Expected changes: complete rubric fields, source excerpts and evidence/unknown rationales; update progress.
- Verification approach: compare requests/plans, summaries, corrections and available relevant commit evidence; check all fields/citations, identities, links and scope.
- Risks or open questions: verification limits and related incident accounts; inspect counterevidence and preserve unresolved judgments. Base volume: 1,120 lines.
- Canonical components/API contracts touched: shared rubric/register and batch records; sources read-only.

## Stage 7
- Goal: reconciled reviewer handoff.
- Dependencies: all 25 records verified/committed.
- Expected changes: batch report, gaps, dated corrections, complete pending/adjudication queues and final summary.
- Verification approach: audit field coverage, citations and claim strength; reconcile 25 + 191 = 216 and separate 95; check links/anchors, fingerprints, allowed writes and stage commits.
- Risks or open questions: partial coverage is not representative; report missingness and related cases, preserve disputed conclusions and human-review-pending status.
- Canonical components/API contracts touched: research entry/report/queues, feature summary and debug log; baseline research unchanged.
