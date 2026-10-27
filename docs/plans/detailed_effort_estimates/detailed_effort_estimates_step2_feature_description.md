> **Feature plan:** [Step 1](./detailed_effort_estimates_step1_solution_assessment.md) · [Step 2](./detailed_effort_estimates_step2_feature_description.md) · [Step 3](./detailed_effort_estimates_step3_development_plan.md) · [Step 4](./detailed_effort_estimates_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/detailed_effort_estimates`; standing R1/P2 enrollment; [ledger](../../research/effort_estimation/collection.md). Step 1 Option A explicitly approved on 2026-10-23.

## Problem and user stories

Cycle totals hide the effort differences between options and stages. Readers need comparable estimates and retained revisions without mistaking stage judgments for cycle forecasts or measured labor.

- As a maintainer, I want an effort estimate for every Step 1 option so that I can weigh cost alongside outcomes and risks.
- As a planner, I want every Step 3 stage estimated so that difficult work and uncertainty are visible before approval.
- As an implementer/reviewer, I want Step 4 to retain planned, revised and retrospective stage values so that discoveries remain understandable.

## Core requirements

- **Activation:** optional extended estimates, selected per cycle or through a standing host policy and inherited on resumption. No repeated selection question under standing policy; other hosts retain existing behavior. Work and scope approvals remain unchanged.
- **Options:** each Step 1 option has a complete scoped-cycle R1 point estimate or range, a short complexity driver and material uncertainty. Use comparable starting assumptions; identify different outcomes. Keep the recommended cycle's formal snapshot separate; re-estimate combinations rather than adding scores.
- **Stages:** every Step 3 stage has a scoped work estimate, uncertainty and driver using the R1 reference yardstick. Label it as **stage work**, distinct from the whole-cycle R1 projection. Cover the stage's changes, verification, documentation and ordinary correction; identify shared overhead without counting it again in each stage. Whole-cycle totals remain independently judged, not sums, stage fractions, hours or percentage-complete calculations.
- **Execution history:** Step 4 inherits each stage's original estimate and stable identity. Append material revisions with date, scope and reason before dependent work where possible; each revision estimates the stage's entire scoped work, not remaining work. At stage completion, add a separately labeled retrospective assessment. Unknown measured work stays unknown; unavailable, skipped, blocked and superseded records remain explicit rather than becoming zero or fabricated observations. Link replacements/splits and preserve the original stage record.
- **Evidence:** retain R1 source bytes, cycle snapshots and acceptance rules. Supplemental stage records do not count as independent cycle outcomes or validated forecasts. Present concise current values with linked history; include examples of an option comparison, planned/completed stage and discovery-driven revision. Resuming older work starts collection now and never invents missing earlier estimates.

## Delivery scope and completion boundary

**Documentation-only.** Allowed product files: `RAILSPIKE.md`, `README.md`, `docs/effort-estimation.md`, and estimation-related sections/templates/checklists of `docs/workflow/*.md`, all in `../railspike`. Extend the existing activation, checkpoint and stage-summary contracts; add no parallel workflow or application UI/API.

Allowed development files: this cycle's plans/debug/summary, its `docs/plans/README.md` entry, `docs/research/effort_estimation/collection.md`, and cycle-specific verification records under `docs/research/effort_estimation/`. Application/runtime, tests/CI/tooling changes, frozen-source edits, host-clone upgrades, beta publication and merges are outside scope.

Complete when an agent can follow the documented option → plan → stage revision → closeout flow, including missing-reference and resumed-history recovery, with consistent meanings and intact prior values. Correct mistakes through appended revisions. Product/development links, existing Git-workflow fixture, whitespace, file-scope checks and scenario walkthroughs must pass. Runtime/UI/deployment checks are inapplicable; document consistency does not establish live-agent compliance or predictive accuracy.

## Risks and flow

- **Scale ambiguity:** stage values could overwrite cycle semantics. Validate definitions before Step 3; mitigate with explicit stage-work labels, independent cycle totals and unchanged R1 sources.
- **History loss:** revisions or renumbering could erase original values. Validate a discovery/split example early; retain identities, scope versions and replacement links.
- **Overhead:** estimates could swamp concise plans. Validate a small multi-stage example early; use short current-value lines with linked append-only history.

Flow: enable/inherit extended mode → compare option totals → define stages and estimates → inherit originals in Step 4 → append discoveries and retrospective assessments. No new approval gates. Success requires consistent examples for ordinary, revised, resumed and unavailable-reference cases, and unchanged behavior when the extension is off.

## Study checkpoint and authorization

2026-10-23 UTC, scope v1 clarified, R1/P2 and original starting revisions unchanged; Codex, single exposed rater with prior study/source/instruction exposure. All three retained R1 hashes reverified. Step 2 projected total **0.60 reaffirmed**, including planning, documentation and verification; no new scope or measured effort. Step 1 approval is explicit; Step 2 and later implementation remain unapproved. No additional enhancement request.

Await **Approved Step 2** before the development plan.

### Approval received

2026-10-23 UTC: user explicitly replied “Approved Step 2.” Requirements above are approved unchanged; the preceding waiting state is historical. Step 3 drafting authorized; implementation awaits Step 3 approval.
