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
