> **Feature plan:** [Step 1](./detailed_effort_estimates_step1_solution_assessment.md) · [Step 2](./detailed_effort_estimates_step2_feature_description.md) · [Step 3](./detailed_effort_estimates_step3_development_plan.md) · Step 4 (not yet started)

Debug mode: enabled

Effort study: `railspike-effort / railspike/detailed_effort_estimates`; standing R1/P2 enrollment; [ledger](../../research/effort_estimation/collection.md). Steps 1–2 explicitly approved. Stage estimates below are prospective pilot annotations for this requested extension; the product capability is not implemented yet.

## Completion Contract

Documentation-only within [Step 2's allowed files](./detailed_effort_estimates_step2_feature_description.md#delivery-scope-and-completion-boundary). Deliver optional/inheritable activation → whole-cycle estimates for every Step 1 option → scoped stage-work estimates in Step 3 → inherited originals, appended revisions and separate retrospective assessments in Step 4. Keep formal cycle totals independently judged and R1 unchanged. Provide concise examples and missing-source/resumed-history recovery. Verify document integrity, local links, existing Git-workflow fixture, file scope and scenario walkthroughs; application/UI/deployment, host upgrades, beta publication and merges are inapplicable or excluded. Source snapshots, application code, tests and tooling remain untouched.

After **Approved Step 3**, create `feature/detailed-effort-estimates` branches from the current development/product revisions; organize these plans/log into their feature folder, repair navigation/index references and make the development planning commit first. Create the summary only afterward. Commit each product stage, then its paired development evidence/summary, before advancing; Stage 4 needs no empty product commit.

## Key Risks

- **High risk: scale confusion.** Impact: stage annotations contaminate cycle observations. Validate the definitions/example in Stage 1; mitigate with explicit stage-work labels, unchanged R1 and no summation, hours or independent-outcome claims.
- **High risk: history loss.** Impact: revision or splitting erases original scope/estimate. Validate the original 0.20 → revised whole-stage 0.30 → retrospective 0.25 walkthrough in Stage 1; retain all values, dates and identities before dependent work.
- **Overhead:** required fields overwhelm concise plans. Validate a compact two-stage example in Stage 1; use one current-value line and linked history, without redesigning global length or approval policy.

## Stage 1

- Goal: define consistent activation and estimate meanings.
- Dependencies: approved plans/planning commit; verified R1 sources.
- Expected changes: root contract, effort guide and README entry describing optional cycle/host activation, separate option/cycle/stage values, shared overhead and history; distinguish standing study enrollment from opting into the extension.
- Verification approach: definitions and compact example review; unchanged frozen hashes; product/development links, whitespace and scoped-file check.
- Risks or open questions: impact/early validation as above; settle stage-versus-cycle labels and revision meaning before changing templates.
- Canonical components/API contracts touched: existing root activation/checkpoints and effort guide; no API.
- Stage work estimate: **0.15**, plausible **0.10–0.25**, using R1 as a yardstick; driver: clear supplemental semantics. Includes this stage's verification/docs, not the cycle's planning again.

## Stage 2

- Goal: make option and planned-stage estimates visible where readers decide.
- Dependencies: Stage 1 verified and committed.
- Expected changes: Step 1 comparison guidance and Step 3 before/do/after templates/checklists, plus compact guide examples; inherit activation through Step 2 if needed. Every option includes its total/driver/uncertainty; every stage includes scoped work/driver/uncertainty and identity.
- Verification approach: compare differing option outcomes and a combined option freshly estimated; review a two-stage plan with shared overhead; verify off-mode behavior, links, scope and whitespace.
- Risks or open questions: adding numbers must not create new study selection or approval prompts; check unchanged unselected behavior and separate recommended-cycle snapshot.
- Canonical components/API contracts touched: existing option structure and stage-field template; no parallel format.
- Stage work estimate: **0.20**, plausible **0.10–0.30**; driver: consistency across planning hooks and examples. Shared definitions stay in Stage 1.

## Stage 3

- Goal: retain stage estimates through execution, discovery and completion.
- Dependencies: Stage 2 verified and committed.
- Expected changes: Step 4 before/do/after hooks and summary template, with linked effort-guide examples for inherited originals, whole-stage revisions, retrospective assessments, unavailable/skipped/blocked/superseded states and split/replacement identities.
- Verification approach: trace original → discovery → revised total-stage estimate → separately labeled retrospective; resume older work without invented originals; check missing references, nonzero semantics and preserved approvals/commits.
- Risks or open questions: a later rating must not appear prospective or measured; check dates, scope/reasons and status in the example before completing this stage.
- Canonical components/API contracts touched: existing Step 4 entry, stage-boundary, summary and closeout contracts.
- Stage work estimate: **0.20**, plausible **0.15–0.35**; driver: historical state transitions. Includes its verification/docs; no inferred actual hours.

## Stage 4

- Goal: validate the complete documented flow and close out this cycle.
- Dependencies: Stage 3 verified and committed.
- Expected changes: cycle-specific scenario/verification record, final summary and collection closeout; correct only estimation inconsistencies within the approved documentation boundary.
- Verification approach: off mode; study without extension; per-cycle/standing extension; options/combination; shared overhead; inherited entry; revision; retrospective completion; missing source; old-cycle resumption; blocked/skipped/split history. Run both link checks, existing Git-workflow fixture, whitespace, scope and per-stage commit audit; reverify frozen hashes.
- Risks or open questions: static traces prove document consistency, not agent compliance or predictive accuracy. Retain limitations and pending maintainer acceptance; do not publish or upgrade hosts.
- Canonical components/API contracts touched: existing collection index and this cycle's summary/evidence; no new checker or application test.
- Stage work estimate: **0.15**, plausible **0.10–0.25**; driver: cross-document scenario coverage and corrections.

## Study checkpoint and handoff

2026-10-23T19:56:02Z; scope v1/R1/P2, original start revisions and prior exposure retained; Codex single exposed rater. Step 3 whole-cycle total **0.60 reaffirmed** after accounting for stages/verification; it is not the sum of the supplemental stage values. Their ranges are subjective, not calibrated intervals. Preserve originals if later revised; actual work time unknown. All three retained reference hashes reverified. Requests reconciled with approved Step 2; no new scope. Plans/ledger remain uncommitted; Step 4 has not started.

Await **Approved Step 3** before branching, planning commit and implementation.

### Approval received

User explicitly replied “Approved Step 3.” Approved scope and four-stage plan remain unchanged; branching, organization, planning commit and implementation are authorized. Earlier pending state is historical. Beta publication, host upgrades and merges remain excluded.
