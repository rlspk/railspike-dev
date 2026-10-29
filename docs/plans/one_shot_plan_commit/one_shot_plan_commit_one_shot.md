# One-shot plan commit

Cycle: `railspike/one_shot_plan_commit`; Mode: one-shot; [index](../README.md).
Debug mode: enabled (host marker).
Effort study: `railspike-effort`, R1/P2; [ledger](../../research/effort_estimation/collection.md).
Extended estimates: enabled.

**Cycle estimate: 0.30**

Status: technically complete; next action: maintainer review, publication not authorized.

## Request, authorization and scope

User: “OK, please update our process”, following the explicit requested sequence: branch, write plan, commit plan, implement, commit implementation with updated plan. Bounded execution authorized; no extra planning approvals requested. This record is the plan before implementation and the outcome record afterward.

Documentation-only scope: product one-shot workflow, README, entrypoint, welcome, effort checkpoints and failure guidance; development this record/debug log/index/ledger and touched concept descriptions. No application, checker, website, consumer, release or push work. Related prior cycle: shared implementation standards. Preserve the separately committed Step 1 reminder.

## Approach, reuse and completion

Reuse the existing one-shot record path/template, scope rules, debug/study policies and split-repository commit handling. Replace contradictory planning-commit exceptions across entry/readme/workflow/recovery guidance. Require branch creation before writing the plan, a planning-only commit before implementation, then implementation plus updated plan committed together (paired commits across repositories). Preserve no-commit user overrides, explicit eligible branch reuse, and no fabricated history for old/resumed cycles. No numbered planning stages or intermediate approval gates.

Risks: stale exceptions permit bypass (search all product instructions); unrelated files enter the plan commit (inspect staged paths); migration invents chronology (explicit recovery for already-started work); split repositories lose paired evidence (confirm hashes). Verification: product/development links, diff checks, Git-workflow fixture, and document scenarios for new/resumed/no-commit/split-repository work. Required missing plan commits must block new implementation unless an explicit override applies; preexisting mistakes remain disclosed. Recovery: correct scoped documentation and repeat affected checks; report live compliance unverified.

Concepts touched: [Planning record](../../concepts/planning.md#planning-record) changed; [Approval and scope boundary](../../concepts/planning.md#approval-and-scope-boundary) and [Shared implementation standards](../../concepts/implementation.md) used unchanged and checked. Only the planning entry needs editing.

Starting revisions: development `99f2918717abb634bc056e75ff37714548609d35`; product `df980a0aeeb717bdba434000ff46030f3559cbed`. Fresh branches: `feat/one-shot-plan-commit` in both repositories. Plan commit: `9b682fb`, confirmed before any product edits.

## Study history

2026-10-29T22:46:32.697612+00:00 — Scope v1/R1/P2; Codex, single exposed rater, model/settings unavailable. Intake missing: inspection occurred before recording. Execution-entry whole-cycle projection 0.30, including documentation alignment, verification and correction; all three frozen R1 hashes verified. Comparable to modest integration references; uncertainty in recovery/compatibility wording. No artificial work units. Not measured labor; no retrospective or maintainer acceptance yet.

*— Codex · 2026-10-29 UTC*

## Outcome and verification — 2026-10-29T22:47:50.999237+00:00

Implemented branch → plan → planning-only commit → implementation/verification → implementation plus updated plan commit. Updated six product instruction surfaces, including no-commit overrides, old-cycle recovery, split-repository pairing, template evidence and the default README example. Planning concept updated; approval/scope and shared-standards entries verified unchanged. No additions beyond authorized scope.

- Passed: `python scripts/check-markdown-links.py ../railspike` (18 files), development equivalent with historical baseline (221 files, 80 known targets), `bash scripts/check-railspike-git-workflow.sh ../railspike`, product/development diff checks.
- Passed: product-wide search finds no obsolete “no planning commit”/single-completion-commit exceptions. Reviewed new-cycle ordering, commit-failure blocking, explicit no-commit override, historical missing-plan recovery, paired repositories, and unchanged staged-transition approval gates.
- Planning commit `9b682fb` contains only this plan and its index. Product implementation `bc9e4319db18de4bd9a8dc3bd4fdc87ac8aa0574` follows it; host completion commit includes this updated plan and touched concept/ledger/debug evidence. No unrelated files staged.
- Inapplicable: application runtime/UI/migration checks; no installation mechanics or checker code changed. Live agent adherence unverified; no consumer updates, pushes, merges or releases.
- Compatibility: this intentionally changes a required commit contract; under `docs/maintainers/RELEASES.md`, future version selection must account for the major-change policy rather than silently publish it as a patch. No version/tag selected here.

**Retrospective cycle scope: 0.30**

R1/P2 v1, Codex single exposed rater; original projection 0.30 retained, no scope/score revisions. Not measured labor. Maintainer comfortable-fit/acceptance pending. Recovery: review or revert this feature's local commits under normal authorization; preserve unrelated history. Host completion hash pending creation; confirm in the next record-only handoff update.

*— Codex · 2026-10-29 UTC*

Confirmed completion references: product `bc9e431`, paired host completion `5b2477e`; host planning commit `9b682fb` precedes both. This record-only handoff preserves those references without amending implementation history.
