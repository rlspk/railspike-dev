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

## Stage 2 - First screen, typography and diagram

**Original estimate: 0.20**

**Retrospective stage work: 0.20**

- Changes (`rlspk.github.io` `26f8bf4`, `index.html`):
  - New header with the logo and a "Railspike" `h1`, plus a lede using the essay's first sentence.
  - The compact install box comes first, followed by the "Four steps, three approvals" line diagram: an ordered list of Assess (dashed and optional), Define, Plan and Build, with the `Approved Step N` gates on the segments. The line is horizontal from 34rem up and vertical, drawn per segment, below that. The line color is the logo's spike amber (`#c47a02` light, `#e09a2a` dark). Below it is a one-sentence note about `docs/plans/` and approvals.
  - The essay is wrapped in `<article id="essay">`. Its title is now an `h2`, and its paragraphs were moved by script, not retyped.
  - One shared prompt pattern (`.prompt`) with one script loop now serves every prompt box. The copy button moved under the field with a "Copy prompt" label, because at 360 px the old overlaid button covered prompt text. The field sizes itself to its content (`field-sizing`, with a min-height fallback).
  - System sans is used for the UI and diagram, and the serif is kept for prose. The head metadata block was copied unchanged.
  - The old after-essay install section was kept, on the shared pattern, until Stage 3.
- Verification:
  - Essay check (`essay_check.py`, scratchpad): text identical to `c8043fc`, 4,970 characters.
  - Prompt text was built from the README Quick start block (`railspike` `5952bfd`) and is identical.
  - Renders: 1280×720 light, and 360 px light and dark. The first render showed the step numbers sitting high in their circles and the copy button overlapping the prompt text at 360 px; both were fixed and re-rendered. Dark mode was emulated with `--blink-settings=preferredColorScheme=0`.
  - Fold: at 1280×720 the diagram note ends at 622 px, so the one-liner, install box and diagram are all above the fold.
  - Overflow: inside a 360 px iframe, `scrollWidth` equals `clientWidth` (345/345). A headless window can't go below 485 px, so the iframe method was used.
  - Without JavaScript, the copy buttons stay `hidden` and the prompt remains selectable text in the markup. With JavaScript, two buttons are shown.
  - External references: only the logo, GitHub links and the canonical URL; no third-party requests.
  - `git diff --check`: clean.
- Notes:
  - The scratchpad build script assembles the page from the preserved head, the template, the extracted essay and the README prompts. It is a development aid and is not committed to the site.
  - Contrast and metadata checks are owned by Stage 4.
- Estimate details: original scope unchanged; no revision.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*

## Stage 3 - After the essay

**Original estimate: 0.15**

**Retrospective stage work: 0.15**

- Changes (`rlspk.github.io` `d219728`, `index.html`):
  - Replaced the old after-essay install section. In order, the page now has:
    - "Get started": the repeated install box, a one-line note on what the agent does, and a link to the full instructions.
    - "What a plan-prompt looks like": the Original Query, Problem and Option B of `one_shot_cycles` Step 1 as raw Markdown, with `[…]` marking omissions and a link to the full file at `8e89733`.
    - "Small tasks": one-shot mode in two sentences, linking to the README.
    - "Uninstall": the shared prompt box with the README prompt and a link to `README#uninstall`.
    - "Read more": full installation, the four steps, failure modes, updating, and GitHub.
  - Footer: MIT License link and the GitHub link.
  - All three prompt boxes use the shared `.prompt` pattern; no new script.
- Verification:
  - Essay check: identical to `c8043fc`, 4,970 characters.
  - `parity_check.py` (scratchpad):
    - The two install prompts and one uninstall prompt match the README blocks on `railspike` `5952bfd` exactly.
    - The excerpt's three sections are verbatim from `git show 8e89733:…`, and `8e89733` is an ancestor of `origin/main`.
    - All five README anchors exist (`quick-start`, `the-four-steps`, `reusing-across-projects`, `one-shot-work-with-a-development-record`, `uninstall`).
    - `docs/failure-modes.md` and `LICENSE` exist on product `main`.
  - Renders of the after-essay sections: 1280 px light, and 500 px dark. The note under each copy button sat too close to it; spacing was added and the page re-checked. Anchor-scrolled headless screenshots came out blank, so a probe copy hiding the earlier sections was rendered instead.
  - 360 px iframe: `scrollWidth` 345 equals `clientWidth` 345. `git diff --check`: clean.
- Notes:
  - `README#uninstall` exists only on the unmerged `railspike` branch. If the website were merged first, that link would land on the top of the README. The product must therefore be merged first; this is recorded for closeout.
  - The prompts keep the README's hard line breaks, so they wrap raggedly in narrow boxes. Parity with the README took priority over reflowing the text.
- Estimate details: original scope unchanged; no revision.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*
