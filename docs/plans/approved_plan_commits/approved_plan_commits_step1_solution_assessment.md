> **Feature plan:** [Step 1](./approved_plan_commits_step1_solution_assessment.md) · [Step 2](./approved_plan_commits_step2_feature_description.md) · [Step 3](./approved_plan_commits_step3_development_plan.md) · [Step 4](./approved_plan_commits_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/approved_plan_commits`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.50**

## Original Query

“Commit Steps 1 and 2 immediately after approval.”

“Start the workflow change, merge feat/plain-language-plans into main.”

## Understood Intent

Save each approved planning step in Git before drafting the next one. The requested predecessor merge is complete in both repositories.

## Problem

The current instructions leave approved Steps 1 and 2 uncommitted until Step 4 begins.

## Option A — Organize at the first approval

**Estimate: 0.50**

At the first planning approval, create the feature branch and feature folder, then commit the approved step before drafting the next. Commit later approved steps on that branch. If Step 1 is skipped, start this sequence at Step 2 approval.

- Benefit: approved plans have durable history and stable paths early.
- Cost: branch and folder setup moves earlier; Step 4 must verify existing planning commits rather than repeat them.
- Driver/uncertainty: reconcile organization, debug logs, study records, resumed cycles and separate repositories across existing instructions.

## Option B — Keep plans at the top level until Step 3 approval

**Estimate: 0.55**

Create the branch and commit each approved step immediately, but keep plans in `docs/plans/` until the existing Step 4 organization gate. Move them into the feature folder with the approved Step 3 commit.

- Benefit: retains the current timing for folder organization.
- Cost: approved plan paths change later; links and navigation need a second pass.
- Driver/uncertainty: the same commit-rule reconciliation as A, plus later moves and reference repairs.

## Recommendation and scope

Choose A. It delivers a complete documentation workflow from approval through a verified commit and safe continuation. Keep unapproved drafts out of approval commits. Preserve existing approval gates and one-shot behavior. Define safe handling for failed commits, explicit no-commit requests, revisions needing renewed approval, older cycles, and branch reuse. Never invent missing historical commits.

Use existing instruction surfaces in `RAILSPIKE.md`, step guidance, debug/study guidance, onboarding, and the Git workflow fixture. Refine exact allowed paths and proportional checks in Steps 2 and 3. Product work belongs in `../railspike`; development records stay here. Publication is separate and requires exact-version confirmation.

**Concepts touched:** [Planning record and Approval and scope boundary](../../concepts/planning.md), proposed changes for both options.

## Study snapshot and authority

2026-11-04T15:23:36.813151+00:00 — R1/P2 scope v1; Codex, single exposed rater, model/settings unavailable. Starting revisions: dev `4c64dd52b354807842e611c0b3c67be84aa2c94f`, product `5d54e065fa5f9f6e2555977034b5073456dd104c`. All three frozen R1 hashes verified. Intake is missing: related source and predecessor records were inspected before rating. Step 1 projection **0.50** for A; B **0.55**. These cover the whole cycle through documentation verification and handoff, exclude publication, and are scope judgments rather than hours. Main uncertainty is reconciling existing commit rules; no implementation or accepted outcome yet. User authorized starting the change; Step 1 approval is pending. Under current rules these planning files remain uncommitted. The advisory context-reset reminder is due once at this handoff.

*— Codex · 2026-11-04 UTC*

2026-11-04T15:40:57.751313+00:00 — User: “approved step 1.” Option A approved; Step 2 authorized. Original estimates retained. Context-reset reminder delivered at the original handoff; do not repeat it.
