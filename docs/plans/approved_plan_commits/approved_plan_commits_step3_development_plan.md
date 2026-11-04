> **Feature plan:** [Step 1](./approved_plan_commits_step1_solution_assessment.md) · [Step 2](./approved_plan_commits_step2_feature_description.md) · [Step 3](./approved_plan_commits_step3_development_plan.md) · [Step 4](./approved_plan_commits_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/approved_plan_commits`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.50**

## Completion Contract

Documentation-only. Implement Option A from approved Step 2: save each approved planning step before drafting the next, with branch/folder setup at the first approval. Keep approval and implementation authority distinct. Require commit verification, scoped contents and honest recovery; retain explicit no-commit overrides and one-shot behavior.

Allowed product paths: `RAILSPIKE.md`, `README.md`, `WELCOME.md`, `docs/workflow/*.md`, `docs/effort-estimation.md`, `docs/concepts.md`, `docs/failure-modes.md`; edit only affected passages. Allowed dev paths: this cycle's artifacts/folder, plan index, `docs/concepts/planning.md`, append-only study ledger rows. No scripts, tests, runtime, CI, website, release publication or unrelated records.

Done means coherent instructions, passing product links, existing Git-workflow fixture and whitespace checks, plus a recorded scenario review. Handoff is unmerged feature branches with paired commits. Live agent compliance remains unverified. Fix in-scope wording defects; return for approval if correction expands scope. Runtime/UI/deployment/migration checks are inapplicable.

**Concepts touched:** [Planning record and Approval and scope boundary](../../concepts/planning.md), both changed.

## Key Risks

- Old late-commit rules may contradict the new gate. Search live guidance before editing and at closeout; reconcile conflicts before advancing.
- Log or study allowances may include unrelated changes. Inspect staged paths and content per checkpoint; scope ledger hunks to this cycle.
- Recovery could imply approval that never happened. Preserve actual chronology, existing commits and missing checkpoints; never rewrite history to manufacture compliance.

## Stage 1 — Shared approval commit gate

**Estimate: 0.20**

- Goal: define approval commits and recovery in the canonical contract.
- Dependencies: Step 3 approval; new branches; current-rule planning commit, then summary creation.
- Expected changes: revise `RAILSPIKE.md` organization, commit cadence, branch reuse and debug/study allowances. Cover first approval, revisions, waivers, failures and older cycles; replace duplicate Step 4 planning commits with verification.
- Verification: trace ordinary, skipped-Step-1 and recovery cases; check links, whitespace and staged scope; update summary before commit.
- Estimate details: stage work; driver: related contract passages; uncertainty: commit counts under recovery/waivers.
- Risk: unrelated changes enter approval commits; validate staged-content examples; enumerate allowed checkpoint records.
- Canonical contract: existing Planning Artifacts, Commit discipline, study/debug and Follow-up Cycles sections.

## Stage 2 — Step handoffs and recovery guidance

**Estimate: 0.15**

- Goal: connect every affected entry/resumption path to the shared gate.
- Dependencies: Stage 1 checks, summary and commits complete.
- Expected changes: reconcile step handoffs/setup, one-shot transitions and affected onboarding/failure/study/concept references. Keep one-shot sequencing; planning commits stay in the host, with the product branch established before product edits.
- Verification: scan contradictory rules; trace split-repository and transition cases; run product links, unchanged Git-workflow fixture and whitespace checks.
- Estimate details: stage work; driver: distributed references; uncertainty: affected passage count.
- Risk: an entry path skips verification; trace each handoff/resumption and link the shared rule.
- Canonical contracts: existing approved product documentation paths; preserve public anchors and installation procedures.

## Stage 3 — Concepts and final verification

**Estimate: 0.10**

- Goal: align concept descriptions and record complete evidence.
- Dependencies: Stage 2 checks, summary and commits complete.
- Expected changes: update both touched concept entries; record scenario results, omissions, revisions, retrospective estimates and pending acceptance in summary/ledger.
- Verification: review ordinary, skipped-Step-1, renewed approval, failed commit, no-commit, older-cycle, branch-reuse and split-repository cases. Exclude unapproved artifacts from approval commits. Run product links/fixture, touched dev links, whitespace and allowed-file review.
- Estimate details: stage work; driver: evidence and concept alignment; uncertainty: none material; owns final review/bookkeeping.
- Risk: document review overstates compliance; inspect evidence labels and keep live behavior unverified.
- Canonical contracts: existing concept entries, summary/debug log and append-only ledger; checkers unchanged.

## Execution and study checkpoint

This cycle follows the current contract: after Step 3 approval, create new branches, organize plans, repair navigation/index links, and commit approved Steps 1–3 plus the existing debug log and organization allowance. Keep the ledger out of that initial commit under the current rule. Create the summary afterward. Each stage ends with checks, summary update and stage commit before the next begins; preserve unrelated `todo.txt` edits and the checklist. Do not retroactively create early approval commits for this cycle.

2026-11-04T22:30:18.885816+00:00 — R1/P2 v1, Option A; Codex, single exposed rater, model/settings unavailable. Frozen R1 hashes verified. Start: dev `4c64dd52b354807842e611c0b3c67be84aa2c94f`, product `5d54e065fa5f9f6e2555977034b5073456dd104c`. Whole-cycle projection **0.50 reaffirmed**; stage work S1 **0.20**, S2 **0.15**, S3 **0.10**, separately scoped and not additive or hours. Original A 0.50 / B 0.55 and missing intake retained. Steps 1–2 explicitly approved; Step 3 approval pending. No implementation, merge or publication authorized for this cycle. Maintainer fit/study acceptance pending.

*— Codex · 2026-11-04 UTC*

2026-11-04T22:51:09.497887+00:00 — User: “approved step 3.” Implementation authorized within the approved documentation scope.
