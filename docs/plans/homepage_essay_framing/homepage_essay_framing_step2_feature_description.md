> **Feature plan:** [Step 1](./homepage_essay_framing_step1_solution_assessment.md) · [Step 2](./homepage_essay_framing_step2_feature_description.md) · [Step 3](./homepage_essay_framing_step3_development_plan.md) · [Step 4](./homepage_essay_framing_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/homepage_essay_framing`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.60**

Approved direction: Step 1 Option B (`Approved Step 1`, 2026-10-28).

## Problem

A visitor to railspike.dev has to read the whole essay before learning what the four steps are or reaching the install prompt. Neither the site nor the product explains how to uninstall Railspike.

## User stories

- As a first-time visitor, I want to see what Railspike does and its four steps on the first screen, so that I can decide whether to read on.
- As a returning visitor, I want to copy the install prompt without scrolling, so that I can add Railspike to a new project quickly.
- As a reader, I want the maintainer's essay exactly as written, so that I hear the real story rather than marketing copy.
- As an evaluator, I want to see a real plan excerpt and how to remove Railspike, so that I know what I am adopting and that I can back out.
- As an existing user, I want uninstall instructions inside my installed copy, so that I don't depend on the website.

## Core requirements

- **Essay text:** it is identical, word for word, to `index.html` at website revision `c8043fc`. Only the surrounding markup and styling may change.
- **First screen:** it shows the one-liner (the essay's first sentence), a compact install box with a copy button, and a four-step line diagram with labeled `Approved Step N` gates. The step names match the README's four steps.
- **After the essay:** a repeated install box, a short real Step 1 excerpt that links to its source at a published commit, one or two lines on one-shot mode, the uninstall prompt, and links (full installation, the four steps, failure modes, updating, GitHub). The footer has the license.
- **Product README:** it gains an "Uninstall" section with a copyable agent prompt that covers copied and submodule installations. The prompt keeps the user's own `docs/plans/` and leaves changes uncommitted for review. The homepage shows the same prompt text.
- **Unchanged qualities:** the page stays a single static file with no third-party requests, works without JavaScript (copy buttons are an enhancement), and supports light and dark themes.

## Delivery scope

- **Work type:** application change (website) with a product documentation change.
- **Allowed files:**
  - `rlspk.github.io/index.html`;
  - `railspike/README.md` (the new section, plus its entry in any in-page navigation);
  - this cycle's records in `railspike-dev` (plans, debug log, `docs/plans/README.md` entry, ledger row).
- **Not changed:** logo assets, slides, CI and Pages settings, product workflow instructions, and the Readings.
- **Out of scope:** Readings, ANSI logo, slide-deck link, essay edits, tags and releases.

## Completion boundary

- **Normal entry:** railspike.dev (local render before merge).
- **End-to-end outcome:** a visitor reads the diagram, copies the install prompt from either box, reads the essay, and follows reference links. A reader of the product README finds and copies the same uninstall prompt.
- **Recovery:** without JavaScript, both prompts remain selectable text. A mistaken uninstall leaves only uncommitted changes, so it can be reverted. The site itself can be reverted by restoring the previous `index.html`.
- **Release condition:** the maintainer reviews the rendered page in light, dark and phone widths. Merging the website (which publishes it) and the product branch are separate, explicit authorizations. No tag is created.

## Risks

- **Uninstall correctness.** Impact: an agent could delete user work or leave stale references. Validate early by testing the prompt against copied and submodule fixtures in disposable repositories before writing the homepage copy. Mitigation: the prompt names what to remove (`docs/railspike` including `RAILSPIKE_SOURCE.md`, the submodule entry, the optional Railspike section of `AGENTS.md`, the optional `.railspike_debug_on`), says what to keep (`docs/plans/`, local edits reported first), and stops on anything ambiguous.
- **Essay drift.** Impact: the core constraint would be broken silently. Validate with a script comparing extracted essay text to `c8043fc` at every stage.
- **Diagram legibility.** Impact: a busy diagram that doesn't fit at 360 px would undercut the first screen. Validate with an early render at 360 px, in both themes, before the other sections are added.
- **Example link availability.** Impact: a dead link to an unpublished `railspike-dev` commit. Validate by confirming that the chosen excerpt's commit is on `origin/main`; otherwise choose another one.

## Shared component inventory

- **Install box (textarea and copy button):** reuse it for both install instances and the uninstall prompt. Use one component, not three forks.
- **Install prompt text:** the canonical source is the README Quick start. The homepage copies it verbatim.
- **Four-step description:** the README table and mermaid flowchart are canonical. The new diagram is a separate rendering, because the site has no mermaid and no external scripts, but it uses the same names and gates.
- **Essay markup:** the existing paragraphs and list are reused unchanged.
- **Uninstall:** none exists today. The README section is new and canonical; the homepage mirrors it.

## User flow

1. A visitor opens railspike.dev and sees the one-liner, the install box and the four-step diagram.
2. They copy the install prompt, or scroll to read the essay.
3. After the essay, they see the repeated install box, the example, the one-shot note and the uninstall prompt.
4. They follow a link to the README for full details, including the matching Uninstall section.

## Success criteria

- The essay comparison script reports identical text against `c8043fc`.
- The diagram, one-liner and install box are visible without scrolling at 1280×720, and the page has no horizontal overflow at 360 px.
- Text contrast meets WCAG AA in both themes. The head and Open Graph metadata URLs are unchanged.
- The homepage install and uninstall prompts match the README text exactly.
- The uninstall prompt run in the copied and submodule fixtures leaves `docs/plans/` intact and removes only the listed items.
- The link checks pass for the product, and every homepage link resolves.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*

## Enhancement requests

| Request | Disposition and reason | Approval status | Outcome |
| --- | --- | --- | --- |
| Include the rewritten essay voices | Declined for now (see Step 1) | Maintainer decision | Excluded from v1 |
| Uninstall instructions (`todo.txt`) | In scope as Option B | Approved Step 1 | Requirements above |

## Scope and estimate history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| 2026-10-28 — Step 1 handoff, v1 | 0.60 | Option B recommended (retained from Step 1). |
| 2026-10-28 — Step 2 handoff, v1 | 0.60 | Reaffirmed. The scope is unchanged from Option B. Adding fixture-tested uninstall checks is new understanding of the required verification, not added scope; it remains within the 0.45–0.80 range. Single exposed Claude Code rater, R1/P2; not measured labor. |
