> **Feature plan:** [Step 1](./epic_checklists_step1_solution_assessment.md) · [Step 2](./epic_checklists_step2_feature_description.md) · [Step 3](./epic_checklists_step3_development_plan.md) · [Step 4](./epic_checklists_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/epic_checklists`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.60**

## Entry and authority

2026-11-24T17:45:00Z — Step 3 explicitly approved ("approved step 3"); scope v3, R1/P2. Entry projection **0.60 reaffirmed** by Claude (single exposed rater), a scope judgment, not measured labor. Planning commits in `railspike-dev` on `feat/epic-checklists`: Step 1 `9f8f994`, Step 2 `1fba406`, Step 3 `fc996e9`, each inspected. Product branch `feat/epic-checklists` in `railspike` from `main` at `3cd85805`. Original stage work: S1 0.20 / S2 0.20 / S3 0.10 / S4 0.10, scoped as in Step 3, not additive.

Documentation-only, within the Step 2 file list. Runtime, UI, deployment, migration, website and release checks are inapplicable. This session has read-only access to both remotes, so nothing is pushed; that is disclosed, not waived. No merge or release. No enhancement requests.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Stage 1 - Handoff prompts for any cycle

**Original estimate: 0.20**

**Retrospective stage work: 0.20**

- Changes:
  - `RAILSPIKE.md`: new `## Handoff prompts` section before Enhancement Requests (request phrasings, push limits, one code block, required fields, the new chat's first checks, the record wins).
  - `RAILSPIKE.md` approval commit gate: labeled "draft, not approved" commit allowed for a handoff prompt; never the approval commit.
  - `docs/workflow/step1_solution_assessment.md`: the /new reminder paragraph points at handoff prompts.
  - `docs/failure-modes.md`: new case for a missing or stale branch, or an unrecorded approval, on resume.
- Verification:
  - `wc -w RAILSPIKE.md`: 5,420 before, 5,543 after; 123 of the 150-word budget used. Passed.
  - The gate still says each approval needs its own commit, and the exception names itself as not the approval commit. Passed.
  - `check-markdown-links.mjs`: 18 files, local links valid. Passed. `git diff --check`: clean. Passed.
  - Changed files are within the Step 2 list. Passed.
  - Runtime, UI, deployment, migration and release checks: inapplicable, documentation-only.
- Notes:
  - The first draft linked `docs/workflow/epic_checklist.md`, which Stage 2 creates; the link failed the checker, so it moves to Stage 3.
  - Stage 3 has 27 words left for the Epics pointer.
  - Product commit `f32c7aa`.
- Estimate details: original scope as in Step 3; uncertainty: gate wording; no revision; retrospective judged after completion, not measured time.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Stage 2 - Epic checklist file

**Original estimate: 0.20**

**Retrospective stage work: 0.20**

- Changes:
  - New `docs/workflow/epic_checklist.md` in `railspike`: what an epic is, when to suggest and create one, eleven rules, and a template.
- Verification:
  - Text before the template: 424 words, under one page. Passed.
  - Every gap from the Step 1 review maps to a rule: mode lean, stable IDs (gap 4), status layers, approver, cut/superseded/replan, follow-ups nest (gap 6), estimates not summed, MVP line, backlinks, effort-study counting. Passed.
  - Only Resume here and Items are required. Passed.
  - Link checker: 19 files valid. `git diff --check`: clean. File within the Step 2 list. Passed.
  - Runtime, UI, deployment, migration and release checks: inapplicable.
- Notes:
  - "Follow-ups nest" was added during the gap check; the first draft missed gap 6.
  - Product commit `95c29f6`.
- Estimate details: original scope as in Step 3; no revision; retrospective judged after completion, not measured time.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Stage 3 - Wiring

**Original estimate: 0.10**

**Retrospective stage work: 0.10**

- Changes:
  - `railspike`: `RAILSPIKE.md` handoff section links the epic checklist, and Workflows gains an Epic line; Step 1's Recommendation bullet suggests an epic above 1.0 and creates one only on request; `one_shot.md` says an epic's mode mark is a lean; `effort-estimation.md` counts each epic cycle as its own outcome; index lines in `README.md` and `docs/README.md`.
  - `railspike-dev`: `docs/concepts/planning.md` gains Epic checklist and Handoff prompt entries; Approval and scope boundary gains the handoff push and labeled-draft rule.
- Verification:
  - `wc -w RAILSPIKE.md`: 5,557, net growth 137 of 150. Passed.
  - The split rule in `RAILSPIKE.md` ("do not silently count child cycles") is unchanged. Passed.
  - Link checker: product 19 files valid; `docs/concepts` 3 files valid (sibling checkout linked as `../railspike`). Passed.
  - `git diff --check`: clean in both, after removing a trailing blank line in `planning.md`. Passed.
  - Changed files within the Step 2 list. Passed.
  - Runtime, UI, deployment, migration and release checks: inapplicable.
- Notes:
  - Product commit `a6e96e2`.
- Estimate details: original scope as in Step 3; no revision; retrospective judged after completion, not measured time.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Stage 4 - Replays and final review

**Original estimate: 0.10**

**Retrospective stage work: 0.10**

- Changes:
  - New [`epic_checklists_verification.md`](./epic_checklists_verification.md): four handoff prompts built from hn_theme Step 1 and the notifications, pledges and backlog checklists; template fit for the three checklists; three failure replays; the gap table.
- Verification:
  - Every prompt has all required fields and claims no approval its record lacks. In two cases a later session had approved more than the record at `2d7805c8` shows; the prompts follow the record. Passed.
  - All three checklists fit the template without losing information. Passed.
  - Unpushed branch, stale branch and unrecorded approval each have a stated next action in `failure-modes.md`. Passed.
  - Every Step 1 gap maps to a rule. Passed.
  - Final diff review: `railspike` `main..HEAD` changes 8 files, all in the Step 2 list; `railspike-dev` changes only this folder, `docs/plans/README.md`, `docs/concepts/planning.md` and ledger rows. No duplicate rule text; the split rule is unchanged. Passed.
  - Link checker: product 19 files, this folder 6 files, concepts 3 files, all valid. `git diff --check` clean in both. Passed.
  - Live handoff in a new chat: pending, not testable here. Push: not exercised; this session has read-only access to both remotes.
  - Runtime, UI, deployment, migration and release checks: inapplicable.
- Notes:
  - Finding: the hn_theme Step 1 record does not name its branch. A future cycle could have first artifacts record it.
  - No product commit in this stage; product head `a6e96e2`.
- Estimate details: original scope as in Step 3; no revision; retrospective judged after completion, not measured time.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Closeout

**Retrospective cycle scope: 0.60**

All four stages complete. Planning commits `9f8f994`, `1fba406`, `fc996e9`; stage pairs (product / dev): `f32c7aa` / `3635de5`, `95c29f6` / `22123ac`, `a6e96e2` / `040968a`, and this stage in `railspike-dev` only. `RAILSPIKE.md` grew 137 words. Unverified: a live handoff in a new chat, and the push step. Nothing pushed, merged or released. The retrospective matches the 0.60 projection as a scope judgment, not measured labor. Maintainer comfortable-fit judgment and study acceptance: pending.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*
