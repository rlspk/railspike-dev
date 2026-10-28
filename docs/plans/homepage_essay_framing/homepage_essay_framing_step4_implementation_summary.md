> **Feature plan:** [Step 1](./homepage_essay_framing_step1_solution_assessment.md) · [Step 2](./homepage_essay_framing_step2_feature_description.md) · [Step 3](./homepage_essay_framing_step3_development_plan.md) · [Step 4](./homepage_essay_framing_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/homepage_essay_framing`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.60**

## Setup

- `Approved Step 3` received 2026-10-28. The maintainer asked whether they could review before release (yes; no merge without explicit authorization) and declined an extra pause after Stage 2.
- Branch `feature/homepage-essay-framing` was created in each repository:
  - `railspike-dev` from `d696751`;
  - `railspike` from `main` `0dcab22`;
  - `rlspk.github.io` from `main` `946438e`.
- Planning commit `0d78557` (`railspike-dev`) contains Steps 1–3, the debug log, and the `docs/plans/README.md` entry. The index entry was required by the organization rule at the planning commit, so it moved from the Stage 4 plan to there.
- The ledger row stays uncommitted until the Stage 4 closeout, as the planning-commit gate requires.

## Estimate history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| 2026-10-28 — Step 3 handoff, v1 | 0.60 | Four stages; see Step 3. |
| 2026-10-28 — Step 4 entry | 0.60 | Step 3 projection reaffirmed after the planning commit; scope unchanged. Single exposed Claude Code rater, R1/P2; not measured labor. |

Original stage-work estimates were copied from Step 3 (not new ratings): Stage 1 0.15, Stage 2 0.20, Stage 3 0.15, Stage 4 0.10.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*

## Stage 1 - Canonical uninstall section

**Original estimate: 0.15**

**Retrospective stage work: 0.15**

- Changes (`railspike` `5952bfd`):
  - `README.md`: a new `## Uninstall` section after "Reusing across projects", with a copyable prompt and a five-step agent reference (identify, report local edits, remove, edit `AGENTS.md`, keep and report).
  - The Quick start now links to it.
- Verification:
  - Ran the agent reference step by step against disposable fixtures (scratchpad, not committed):
    - copy, customized copy, and copy without a Railspike section in `AGENTS.md`: only `docs/railspike`, `.railspike_debug_on` and the `## Railspike` section were removed; `docs/plans/`, `src/` and the other `AGENTS.md` sections were kept; the customized step file was detected as a local edit by comparing against the recorded revision; the removals were left unstaged.
    - submodule, and submodule plus an unrelated `vendor/extra` submodule with a local edit: the edit was reported by `git -C docs/railspike status`; the gitlink was removed and staged; `.git/modules/docs/railspike` was removed; the unrelated submodule and its `.gitmodules` entry were kept.
  - The first submodule run exposed an empty `.gitmodules` and an empty `.git/modules/docs` left behind. The wording was revised before commit (remove empty parents; `git rm` an empty `.gitmodules`), and the revised steps were rerun and passed.
  - `check-markdown-links.py ../railspike`: 16 files valid. `check-railspike-git-workflow.sh ../railspike`: passed (update block untouched). `git diff --check`: clean.
- Notes:
  - The fixtures executed the documented procedure as shell commands. A live agent following the prompt was not exercised; that remains unverified.
  - Subtree installations are deliberately treated as ambiguous (stop and ask).
- Estimate details: original scope unchanged; no revision. The retrospective matches the original, because the fixture correction was ordinary correction within the stage.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*
