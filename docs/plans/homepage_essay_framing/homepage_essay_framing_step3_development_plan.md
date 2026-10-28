> **Feature plan:** [Step 1](./homepage_essay_framing_step1_solution_assessment.md) · [Step 2](./homepage_essay_framing_step2_feature_description.md) · [Step 3](./homepage_essay_framing_step3_development_plan.md) · [Step 4](./homepage_essay_framing_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/homepage_essay_framing`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.60**

**Branches:** `feature/homepage-essay-framing` in `railspike-dev` (planning commit and stage summaries), `railspike` (README) and `rlspk.github.io` (site). Each stage commits in its implementation repository first, then commits its summary in `railspike-dev` with the paired commit ID.

## Completion Contract

- **Normal entry:** railspike.dev, rendered locally from the feature branch before merge.
- **End-to-end outcome:**
  - The first screen shows the one-liner, the install box and the four-step diagram.
  - The essay follows, unchanged.
  - After the essay come the repeated install box, a real Step 1 excerpt, the one-shot note, the uninstall prompt, the links and the license.
  - The README carries the canonical Uninstall section, and the homepage shows the same prompt.
- **Required recovery:**
  - Both prompts stay selectable text without JavaScript.
  - The uninstall prompt leaves uncommitted, revertible changes and stops on ambiguity.
  - The site reverts by restoring the previous `index.html`.
- **Deployment/external verification:** Pages publishes only after the maintainer authorizes a merge to `rlspk.github.io` `main`. A post-merge live check is then performed, or recorded as pending.
- **Release condition:** the maintainer reviews the light, dark and 360 px renders. Website merge and product merge are separate authorizations. No tag.

## Key Risks

- **High risk: uninstall correctness.**
  - Impact: user work is deleted or stale references are left.
  - Early validation: Stage 1 fixtures (copy, submodule, customized copy, `AGENTS.md` with unrelated content) run before any homepage copy is written.
  - Mitigation: the prompt names exact targets, preserves `docs/plans/`, reports local edits before removing anything, and stops when the installation type is unclear.
- **Essay drift.**
  - Impact: the core constraint breaks.
  - Early validation: a script extracts the essay's text and compares it with `git show c8043fc:index.html` in Stages 2–4.
  - Mitigation: the essay block is moved, never retyped.
- **Diagram fit.**
  - Impact: the first screen fails at phone width.
  - Early validation: Stage 2 renders at 360 px and 1280×720 in both themes before Stage 3 starts.
  - Mitigation: a vertical layout below a breakpoint.
- **Example link.**
  - Impact: a dead link.
  - Early validation: the excerpt source is `one_shot_cycles` Step 1, confirmed to be on `railspike-dev` `origin/main` (`8e89733`).
  - Mitigation: link to that exact commit.

## Stage 1 — Canonical uninstall section

**Estimate: 0.15**

- Goal: the product README carries a tested, copyable uninstall prompt.
- Dependencies: approved plans; `railspike` branch created from `main` `0dcab22`.
- Expected changes: a `## Uninstall` section after "Reusing across projects", with a short lead and a copyable agent prompt covering copied and submodule installations, the optional `AGENTS.md` section, the optional debug marker, kept plans and uncommitted results. A link from Quick start.
- Verification approach:
  - Follow the prompt step by step against disposable fixtures: copied, submodule, customized copy, `AGENTS.md` with unrelated text. Confirm only the listed items are removed, `docs/plans/` survives, and local edits are reported first.
  - Run `check-markdown-links.py ../railspike`, `check-railspike-git-workflow.sh ../railspike` and `git diff --check`.
- Estimate details: driver: correctly handling the two installation types; uncertainty: how to clean up submodule metadata (`.git/modules`).
- Risks or open questions:
  - Impact: an incorrect removal step.
  - Early warning / validation: a fixture shows unexpected deletions.
  - Mitigation: revise the wording before Stage 3 copies it.
- Canonical components/API contracts touched: README Quick start and Reusing sections (read only; the update block is not touched).

## Stage 2 — First screen, typography and diagram

**Estimate: 0.20**

- Goal: a working first screen above the unchanged essay.
- Dependencies: Stage 1 is not required.
- Expected changes in `index.html`:
  - Refactor the prompt box into one reusable pattern (multiple instances, one script).
  - Add the one-liner and the compact install box.
  - Add the inline four-step line diagram (Assess, Define, Plan, Build, with `Approved Step N` gates; Assess marked optional).
  - Refine the typography (measure, scale, rhythm).
  - Add a heading or anchor for the essay. The essay's paragraphs are moved intact.
- Verification approach: essay comparison script; renders at 1280×720 and 360 px in light and dark; check `scrollWidth` at 360 px; confirm the prompt is selectable without JavaScript.
- Estimate details: driver: the diagram, which must stay legible in both themes and at narrow widths; uncertainty: the vertical fallback.
- Risks or open questions:
  - Impact: the diagram is crowded at 360 px.
  - Early warning / validation: the first 360 px render.
  - Mitigation: stack the steps vertically on narrow screens.
- Canonical components/API contracts touched: the install prompt text (verbatim from the README Quick start); the four-step names from the README table.

## Stage 3 — After the essay

**Estimate: 0.15**

- Goal: the reference material after the essay.
- Dependencies: Stage 1 (uninstall text) and Stage 2 (prompt box pattern).
- Expected changes in `index.html`:
  - The repeated install box.
  - An excerpt of the `one_shot_cycles` Step 1 (Original Query plus one option, with omissions marked), linked at `8e89733`.
  - One or two lines on one-shot mode, with a README link.
  - The uninstall box, with the prompt verbatim from Stage 1 and a link to the README section.
  - The links list and the footer license.
- Verification approach:
  - Essay comparison script.
  - Script check of the excerpt against `git show 8e89733:<path>`.
  - Exact prompt parity with the README.
  - All homepage links resolve (product anchors on the branch; the dev commit on `origin`).
  - Renders at 360 px and 1280×720.
- Estimate details: driver: excerpt fidelity and prompt parity; uncertainty: low.
- Risks or open questions:
  - Impact: the README anchor `#uninstall` doesn't exist on product `main` until the product merge.
  - Early warning / validation: the link check.
  - Mitigation: merge the product before the website, or record the dependency in the release condition.
- Canonical components/API contracts touched: the shared prompt box; the README Uninstall section.

## Stage 4 — Final verification and records

**Estimate: 0.10**

- Goal: evidence for the maintainer's review and closed-out records.
- Dependencies: Stages 1–3.
- Expected changes: no page changes except fixes found here. Add the `docs/plans/README.md` entry and the ledger row update, with the Step 4 closeout and retrospective.
- Verification approach:
  - WCAG AA contrast in both themes.
  - Head and Open Graph metadata URLs unchanged against `c8043fc`.
  - No third-party requests.
  - No horizontal overflow at 360 px.
  - Final essay and prompt-parity checks.
  - Dev link checks.
  - Renders saved for the maintainer.
- Estimate details: driver: the checklist; uncertainty: fixes for contrast or overflow.
- Risks or open questions:
  - Impact: a merge order mistake publishes a dead `#uninstall` link.
  - Early warning / validation: the closeout records the required merge order.
  - Mitigation: no merges without explicit authorization.
- Canonical components/API contracts touched: none new.

## Scope and estimate history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| 2026-10-28 — Step 2 handoff, v1 | 0.60 | Retained. |
| 2026-10-28 — Step 3 handoff, v1 | 0.60 | Reaffirmed. The four stages cover the Completion Contract, including fixture-tested uninstall and the merge-order dependency. The stage values are not additive. Single exposed Claude Code rater, R1/P2; not measured labor. |

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*
