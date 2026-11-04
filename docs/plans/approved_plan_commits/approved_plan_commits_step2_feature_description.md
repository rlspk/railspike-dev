> **Feature plan:** [Step 1](./approved_plan_commits_step1_solution_assessment.md) · [Step 2](./approved_plan_commits_step2_feature_description.md) · [Step 3](./approved_plan_commits_step3_development_plan.md) · [Step 4](./approved_plan_commits_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/approved_plan_commits`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.50**

## Problem and user stories

Approved Steps 1 and 2 currently remain uncommitted until Step 4. As a maintainer, I want each approved plan saved before further planning so interruptions preserve what I approved. As an agent, I want clear commit boundaries so saving approval never includes an unapproved draft.

## Core requirements

- After each explicit Step 1, 2 or 3 approval, commit that approved step before drafting the next deliverable. At the first approval, establish the feature branch and feature folder; if Step 1 is skipped, begin at Step 2 approval.
- Limit each approval commit to the approved step, necessary organization/navigation changes, this cycle's existing debug log, and authorized study records for that checkpoint. Exclude unapproved plans, unrelated work and implementation. Verify the commit succeeded and contains only allowed changes.
- Reuse the cycle's branch for later approvals and Step 4; retain existing eligibility rules for related cycles. In separate repositories, planning commits belong in the host; establish the product branch before product implementation. Step 4 verifies approved planning commits instead of demanding another identical planning commit; stage commits still include summary updates.
- Keep drafts and substantive revisions uncommitted until their required approval; renewed approval saves revisions in a new commit. A failed commit blocks dependent progression until repaired or explicitly waived. Explicit no-commit requests take precedence and preserve written plans, approvals and the disclosed waiver.
- Resume older cycles honestly: preserve existing commits, record missing history, and save the currently approved plan before advancing without fabricating earlier commits. One-shot rules and all implementation approval gates remain unchanged.

## Delivery scope and reuse

Documentation-only, for agents and maintainers using staged Railspike. Allowed product paths: `RAILSPIKE.md`, `README.md`, `WELCOME.md`, `docs/workflow/*.md`, `docs/effort-estimation.md`, `docs/concepts.md`, and `docs/failure-modes.md` if present. Edit only passages affected by the new sequence. Allowed development paths: this cycle's artifacts/folder, `docs/plans/README.md`, `docs/concepts/planning.md`, and append-only rows in `docs/research/effort_estimation/collection.md`.

Reuse the existing Planning Artifacts/Commit discipline contract, step handoffs, debug-log and study-record allowances, onboarding, and one-shot transition rules. Extend these surfaces rather than add a second workflow. Existing link checkers and Git-workflow fixture remain unchanged. Application/runtime code, scripts, tests, CI, website, release publication and unrelated records are excluded.

**Concepts touched:** [Planning record and Approval and scope boundary](../../concepts/planning.md), both updated to describe approval commits without expanding implementation authority.

## Flow and completion boundary

1. Draft the current step; the maintainer reviews and approves it.
2. Establish or reuse the branch/folder, inspect allowed changes, commit and verify; disclose any explicit waiver.
3. Draft the next step only after that gate. After Step 3 approval, verify planning history before creating the implementation summary and beginning stages.

Completion is a consistent instruction diff, valid local links, passing existing fixture/whitespace checks, and a recorded manual scenario review. Cover ordinary and skipped-Step-1 flows, revisions, failed commits, no-commit overrides, older cycles, branch reuse and separate repositories. Check that later unapproved artifacts never enter an approval commit. Report future navigation targets as pending rather than create later deliverables early. Handoff is verified, unmerged feature branches with paired revisions recorded. Live agent adherence remains unverified; confusing guidance returns for revision and renewed approval where scope changes.

## Risks

- Conflicting old rules could restore the late commit gate. Validate affected references before editing; reconcile every live statement and retain stage-summary commits.
- Broad log/study allowances could admit unrelated changes. Review staged paths and content against the cycle/checkpoint boundary; preserve unrelated hunks.
- Resume/revision handling could imply historical approval or implementation permission. Review those scenarios explicitly; keep actual approvals and missing history visible.

## Study snapshot and authority

2026-11-04T15:40:57.751313+00:00 — R1/P2 scope v1, Option A; Codex, single exposed rater, model/settings unavailable. Starting revisions unchanged: dev `4c64dd52b354807842e611c0b3c67be84aa2c94f`, product `5d54e065fa5f9f6e2555977034b5073456dd104c`. Frozen R1 hashes reverified. Whole-cycle projection **0.50 reaffirmed**: scope defines the already selected approach and its verification, excluding publication. Intake remains missing with prior exposure disclosed; original A 0.50 / B 0.55 retained. Step 1 explicitly approved; Step 2 approval pending, no implementation. This cycle follows the current commit rules until the replacement contract is implemented; no early approval commits are claimed. Maintainer fit and study acceptance pending.

*— Codex · 2026-11-04 UTC*

2026-11-04T22:30:18.885816+00:00 — User: “approved step 2.” Scope approved unchanged; Step 3 authorized.
