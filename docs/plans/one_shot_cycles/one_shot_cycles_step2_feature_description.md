> **Feature plan:** [Step 1](./one_shot_cycles_step1_solution_assessment.md) · [Step 2](./one_shot_cycles_step2_feature_description.md) · [Step 3](./one_shot_cycles_step3_development_plan.md) · [Step 4](./one_shot_cycles_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/one_shot_cycles`; standing R1/P2 enrollment; [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.65**

## Problem and user stories

One-shot work lacks a supported record comparable to staged Railspike cycles. Authorization cadence currently determines documentation quality.

- As the maintainer, I want to authorize a bounded fix once so that it can proceed without repeated handoffs while retaining its rationale and evidence.
- As a resuming agent or reviewer, I want original scope, authorization, changes, and verification preserved so that I can distinguish permitted work from new requests and incomplete work from completion.

## Core requirements

- **Explicit mode and authority:** support one-shot cycles for bounded work with a clear outcome and proportionate verification. Record the user's execution authorization and its scope before implementation; the agent cannot approve its own interpretation. Questions, references, and requests to write plans grant no implementation authority. Questions do not automatically revoke existing authorization; ambiguity blocks only dependent work. Staged execution remains available and ordinary tasks need not become cycles.
- **Equivalent evidence:** use one evolving host-owned record for the original request, authorization, outcome, scope/exclusions, approach and risks before implementation, followed by decisions, changes, actual verification/omissions, recovery, status, and revision/commit references. Preserve original scope and append dated changes, separating corrections from additions. Do not invent alternatives, prior approvals, or retrospective plans to fill fields.
- **Lifecycle and recovery:** recover current state and authority after interruption; retain paused, failed, abandoned, and superseded outcomes. Scope expansion requires renewed authorization before dependent implementation or transition to staged planning. Link the retained one-shot record and successor artifacts without erasing history or double-counting one observation.
- **Repository and commit discipline:** retain branch and unrelated-work protections. For this proposed mode, allow one completion commit containing the bounded changes and record, without requiring a separate planning commit; allow additional meaningful commits. Honor explicit no-commit requests and report uncommitted status. Preserve existing staged cadence and distinguish technical completion from commit, merge, and publication status; one-shot authorization does not imply release permission.
- **Study and diagnostics:** apply existing host enrollment and debug policies. Capture enrolled-cycle intake before detailed inspection where possible, execution entry, material revisions, and closeout in the consolidated record; preserve R1, original values, attribution, missing checkpoints, and separate retrospective assessments. Estimate alternatives/work units only when present; do not invent stages or sum estimates. Keep full enabled diagnostics in the existing separate debug-log mechanism, with concise handoffs.

## Delivery scope and shared surfaces

Documentation-only product change for maintainers and coding agents. Allowed product scope: `RAILSPIKE.md`, `README.md`, `WELCOME.md`, `docs/README.md`, `docs/failure-modes.md`, `docs/effort-estimation.md`, and `docs/workflow/` in `../railspike`. Extend canonical entry, recovery, study, and workflow guidance; add the one-shot instructions/template there. No UI/API surfaces apply.

Allowed development scope: this cycle's plans/log/summary and verification records, its plan-index entry, and the collection ledger. Application/runtime changes, scripts, tests, CI, deployment, generated artifacts, website changes, historical backfill, host upgrades, STE rewrite, programmatic gating, and publication are excluded. The cycle developing this feature remains staged.

## User flow and completion boundary

1. User explicitly authorizes bounded one-shot execution; agent records intent, scope, authority, approach, and applicable study state.
2. Agent implements and maintains evidence; resumes from the record or stops dependent work when authority/scope is unresolved.
3. Agent verifies the outcome and records completion, limitations, recovery, and commit status; expanded work receives renewed authorization or a linked staged plan.

The maintainer's entry is an ordinary one-shot request, including in Kiro Web or CLI. On interruption or scope mismatch, the record must make the next permitted action and required clarification apparent without reconstructing chat history. Completion requires coherent guidance/template, reviewed scenario evidence, valid links, scope/whitespace checks, and existing applicable product checks. Static evidence supports documentation consistency only; live Kiro compliance and runtime enforcement remain unverified. Handoff is reviewable documentation, with release decisions separate.

## Risks and success criteria

- **Authorization ambiguity:** could permit unintended implementation. Before finalizing Step 3, review examples of explicit execution, plan references, questions before/after authorization, and changed scope; require an unambiguous permitted next action in each.
- **Evidence loss or excess ceremony:** could recreate informal records or full staged overhead. Map every substantive staged evidence category to the consolidated record before Step 3; mark genuine non-applicability and preserve prospective versus retrospective chronology.
- **Contract conflicts:** new cadence/checkpoints could contradict existing mandatory rules or distort study outcomes. Before Step 3, review the affected canonical surfaces and map mode-specific exceptions, transition identity, enrolled/unenrolled and debug on/off behavior. Later validation must demonstrate those cases plus success, interruption, abandonment, no-commit requests, and unavailable verification.

## Approval and estimate history

2026-10-27 UTC — User explicitly supplied **Approved Step 1**, selecting the recommended Option B. No additional feature request; this artifact defines that option's boundaries. Step 2 approval and implementation remain pending.

2026-10-27 UTC — Step 2 handoff, scope v1, R1/P2: **0.65 reaffirmed**, plausible range 0.50–0.85. Same whole-cycle outcome and starting revisions as [Step 1](./one_shot_cycles_step1_solution_assessment.md#scope-and-estimate-history); lifecycle and checkpoint integration remain the main uncertainty. Codex is the same single exposed rater; all three frozen R1 hashes reverified. Missing intake remains missing, earlier scores retained; model/settings and measured labor unavailable. Maintainer fit/acceptance pending.

*— Codex · 2026-10-27 UTC*

## Approval update

2026-10-27 UTC — User replied **Approved Step 2**. Scope v1 approved for development planning; the earlier pending status remains historical. Step 3 approval is still required before implementation.

*— Updated by Codex · 2026-10-27 UTC*
