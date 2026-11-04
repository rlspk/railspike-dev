> **Feature plan:** [Step 1](./plain_language_plans_step1_solution_assessment.md) · [Step 2](./plain_language_plans_step2_feature_description.md) · [Step 3](./plain_language_plans_step3_development_plan.md) · [Step 4](./plain_language_plans_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/plain_language_plans`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.40**

## Entry and authority

2026-11-03T08:47:01Z — Step 3 explicitly approved; scope v1 (Option B), R1/P2. Entry projection **0.40 reaffirmed** by Claude Code (model claude-fable-5-1, single exposed rater); a scope judgment, not measured labor. Start: product `bc9e4319db18de4bd9a8dc3bd4fdc87ac8aa0574` (main), dev `d9426c184d7f8b67d413bfe1539e4da2acde5af1` (feat/durable-handoffs, unmerged predecessor branch used as base). Branch `feat/plain-language-plans` in both checkouts. Planning commit `d6e438c` in `railspike-dev`. Intake remains missing. Original stage work: S1 0.15 / S2 0.10 / S3 0.10, each scoped as in Step 3, not additive.

Documentation-only. Allowed product files: `RAILSPIKE.md`, `README.md` (optional sentence), the Step 1, 2, 3-do and 4-do workflow files and `one_shot.md`. Allowed dev files: this folder, the plan index, `docs/concepts/planning.md` and ledger rows. Runtime, UI, deployment, migration, website and release checks are inapplicable. Live agent compliance is not testable in this cycle and will be reported as unverified. No push, merge or release.

Enhancement requests: Option C (fielded snapshot template) remains deferred as separate work; no new requests.

*— Claude Code · 2026-11-03 UTC · Model: claude-fable-5-1*

## Stage 1 - Add the shared writing rule

**Original estimate: 0.15**

**Retrospective stage work: 0.15**

- Changes:
  - Added `## Writing style` to `RAILSPIKE.md` before Key Rules: six rules, one exemption sentence, and a before/after example built from the v3 evidence sentence.
  - Changed the Step 1 Warning Signs entry from "verbose explanations" to a link to the new section.
- Verification:
  - Word count: 5,116 before, net growth 148 words after two trims (first draft was 153, over the bound). Passed.
  - `grep -c verbose RAILSPIKE.md`: 0. Passed.
  - The ≤1 page lines in the Step 1, 2 and 3 files are untouched (3 of 3 present). Passed.
  - Example sentences: 14 and 14 words; no noun string over three words; both files named. Passed.
  - Markdown link checker on the product checkout: 18 files, local links valid. Passed. `git diff --check`: clean. Passed.
  - Runtime, UI, deployment, migration, website and release checks: inapplicable, documentation-only.
- Notes:
  - The first intro sentence was passive and broke rule six; rewritten before commit. The rule caught its own text.
  - The Warning Signs line uses a non-breaking space in "Step 1"; the first edit attempt missed it and changed nothing.
  - Product commit `57e2ce3` on `feat/plain-language-plans` in `railspike`.
- Estimate details: original scope: section plus warning-line edit and the word-count check; uncertainty: example cost; no revision; retrospective judged separately after completion, not measured time.

*— Claude Code · 2026-11-03 UTC · Model: claude-fable-5-1*

## Stage 2 - Link the rule from every artifact instruction

**Original estimate: 0.10**

**Retrospective stage work: 0.10**

- Changes:
  - `step1_solution_assessment.md` Guardrails: two bullets became one no-code bullet and one link.
  - `step2_feature_description.md` Guardrails: "verbose descriptions" became the link; "lightweight enough to consume at a glance" removed.
  - `step3_development_plan_do.md`: "Prefer bullets over prose" became the link; "verbose explanations" dropped from the no-code bullet.
  - `step4_implementation_do.md`: link appended to the header-plus-bullets paragraph.
  - `one_shot.md` Record template: one linking sentence added.
  - `README.md`: one sentence naming the rule in the plan-format description (the optional change, taken).
- Verification:
  - `grep -c verbose` on the five workflow files: 0, 0, 0, 0, 0. Passed.
  - No-code limits reread in the Step 1, 2 and 3 files after editing: all present. Passed.
  - Markdown link checker on the product checkout: 18 files, local links valid, so all six new relative links resolve. Passed. `git diff --check`: clean. Passed.
  - Diff: 6 files, 8 insertions, 9 deletions; only allowed files. Passed.
  - Runtime, UI, deployment, migration, website and release checks: inapplicable, documentation-only.
- Notes:
  - The one-shot link was kept; its record template paragraph had no brevity wording to replace, so the sentence is an addition.
  - Product commit `5d54e06` on `feat/plain-language-plans` in `railspike`.
- Estimate details: original scope: five small edits and the optional README sentence; uncertainty: the one-shot file; no revision; retrospective judged separately, not measured time.

*— Claude Code · 2026-11-03 UTC · Model: claude-fable-5-1*

## Stage 3 - Concept entry, replay and closeout

**Original estimate: 0.10**

**Retrospective stage work: 0.10**

- Changes:
  - `docs/concepts/planning.md`: the Planning record entry now says every artifact is written to the shared writing style and links the section.
  - Ledger rows for Steps 1–3 and this closeout appended to `docs/research/effort_estimation/collection.md`.
- Verification:
  - Manual replay of the evidence sentence, self-review by the implementing agent, not independent verification:

    | Rule | Before (v3 sentence) | After (example in the section) |
    | --- | --- | --- |
    | One idea, ≤25 words | Fails: 30 words, four ideas | Passes: 14 and 14 words, one idea each |
    | One term per thing | Fails: "result contract" elsewhere "result format", "result lifecycle" | Passes: "result", "name" |
    | Verb over nominalization | Fails: "retain", "score transfer" | Passes: "change", "keep" |
    | No noun string over three words | Fails: "shared result contract", "companion name" borderline | Passes |
    | Real name anchors a decision | Fails: four files hidden behind abstractions | Passes: two files named, no code |
    | Active voice, concrete subject | Passes (imperative) | Passes |

  - Known-user replay: the live check with Codex in the v3 project is **pending**; it needs a new Step 1 request after the updated Railspike is installed there. Manual recovery in the meantime: quote the failing sentence and the rule, ask for a revision.
  - Markdown link checker: product 18 files valid; dev concepts 3 files valid; this folder 5 files valid (the Step 4 link now resolves). Passed.
  - `git diff --check` in both checkouts: clean. Passed.
  - Scope review: product diff `bc9e431..HEAD` touches exactly the seven allowed files; dev diff `d9426c1..HEAD` plus this commit touches only this folder, the plan index, the concept entry and the ledger. Passed.
  - Runtime, UI, deployment, migration, website and release checks: inapplicable, documentation-only.
- Notes:
  - No product commit in this stage; product work ended with Stage 2.
  - Unrelated local work left untouched: `todo.txt`, two untracked research notes and the screenshot.
- Estimate details: original scope: concept entry, replay and bookkeeping; no revision; retrospective judged separately.

*— Claude Code · 2026-11-03 UTC · Model: claude-fable-5-1*

## Closeout

**Retrospective cycle scope: 0.40**

2026-11-03T08:49:29Z — R1/P2 v1; Claude Code (claude-fable-5-1), single exposed rater. Delivered scope matches Option B as approved. Planned stages 3, completed 3. Product commits `57e2ce3` (Stage 1) and `5d54e06` (Stage 2) on `feat/plain-language-plans` in `railspike`, from `bc9e4319db18de4bd9a8dc3bd4fdc87ac8aa0574`. Dev commits: planning `d6e438c`, stages `a38dd9c`, `0c2bd67`, and this one. Corrections versus additions: two word-count trims and one passive-voice fix inside Stage 1; no new requests. Omissions: live agent compliance unverified; the Codex-in-v3 replay pending. Original projection 0.40 retained; retrospective scope 0.40, a judgment, not measured labor. Maintainer comfortable-fit judgment and study acceptance: pending. Unmerged, unpushed, unpublished.

*— Claude Code · 2026-11-03 UTC · Model: claude-fable-5-1*

## Release follow-up — scope v2

2026-11-04T15:07:33.011072+00:00 — User requested: “please mint a beta from this branch.” This authorizes beta preparation and publication after the required exact-version confirmation; it does not authorize a main merge or host upgrade. Product candidate: `5d54e065fa5f9f6e2555977034b5073456dd104c` on `feat/plain-language-plans`; dev starting revision: `9bed7a55f2f29d4b0400b54ce91de7de21d7ea99`.

R1/P2; Codex, model/settings unverified, single exposed rater. All three frozen reference hashes verified. Intake for this follow-up is missing: source and checks were inspected before this snapshot. Original v1 projection and retrospective scope **0.40** remain unchanged. Revised whole-cycle v2 projection: **0.45**, including release preparation, verification and publication; this is a scope judgment, not hours or an additive stage total. Reason: user added release work to the completed documentation cycle.

Release scope: draft release notes, verify the exact product candidate, record version approval and publication evidence, and publish a beta from the non-default product branch. Development changes are limited to these appended summary/debug/ledger records and the release notes/evidence. Preserve the untracked work checklist and unrelated local work. No product edits, main merge, or installed-copy changes are needed.

Preparation checks: product links pass (18 files), README Git-workflow fixture passes, range whitespace check passes, product checkout clean, seven changed files reviewed, word growth 148. Remote tags/releases inspected: newest beta v0.6.0-beta.1; stable Latest v0.4.0. Proposed **v0.6.1-beta.1** is unused and classed as a patch clarification, with no change to approval/artifact/branch/commit requirements. Notes: `docs/maintainers/releases/v0.6.1-beta.1.md`. Live compliance and Codex-in-v3 replay remain pending.

Status: release prepared; exact-version confirmation pending. No tag created or release published. Publication closeout and retrospective v2 scope remain pending; maintainer comfortable-fit and study acceptance remain pending.
