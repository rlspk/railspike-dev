> **Feature plan:** [Step 1](./homepage_essay_framing_step1_solution_assessment.md) · [Step 2](./homepage_essay_framing_step2_feature_description.md) · [Step 3](./homepage_essay_framing_step3_development_plan.md) · [Step 4](./homepage_essay_framing_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/homepage_essay_framing`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.60**

## Original Query

> Let's work on the railspike homepage. Please familiarize yourself with the project and tell me when you're ready to update it.
>
> Who are the best designers to emulate/use for inspiration for a homepage for railspike?
>
> What material would you include in the home page redesign? I want the essay to still be part of it unedited.
>
> I agree with you on all points. One more thing: Do you see the "rewritten" versions of the essay? Would you include those?
>
> Let's keep them off for now. Write Step 1

## Understood Intent

Redesign railspike.dev around the existing essay, using the content the maintainer agreed to in conversation:

- **Above the essay:** the essay's first sentence as the one-liner, a compact install box with a copy button, and a four-step line diagram with `Approved Step N` gates.
- **The essay:** the full text, unchanged.
- **After the essay:** the install box repeated, a short real Step 1 excerpt, one or two lines on one-shot mode, uninstall instructions, and reference links (install, four steps, failure modes, updates, GitHub).
- **Footer:** license.

The agreed design direction:

- Shape Up for structure.
- Butterick for typography.
- One Vignelli-style transit diagram.
- No SaaS-style hero.

"Unedited" means the essay's text at `rlspk.github.io` `index.html` revision `c8043fc` stays exactly as it is, word for word. Only the markup around it may change.

## Problem

A newcomer has to read the whole essay before learning what the four steps are or finding the install prompt, and the site gives no way to uninstall.

## Option A — Website-only redesign

**Estimate: 0.45**

Restructure `index.html` alone. Add the diagram and the sections around the essay. The homepage carries its own short uninstall prompt.

- Pros: one repository and one branch; no product release involved.
- Cons: the homepage would become the only source for an uninstall procedure, so installed copies and the README would not have it, and it could drift from the actual install footprint (`docs/railspike`, `RAILSPIKE_SOURCE.md`, optional `AGENTS.md` section, submodule variant).
- Driver/uncertainty: the diagram and the verification (essay check, themes, 360 px, metadata) dominate the work. Plausible range 0.35–0.60.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*

## Option B — Redesign plus product README uninstall section

**Estimate: 0.60**

Do everything in Option A. Also add a short "Uninstall" section, with a copyable agent prompt, to the product README on a `railspike` feature branch. The homepage then shows that same prompt and links to the section.

- Pros: one canonical uninstall procedure that installed copies also carry; fully covers the todo item.
- Cons: the change spans two repositories; the product change needs a separate merge/release decision, and the README link checks must still pass.
- Driver/uncertainty: getting the uninstall wording right for both copied and submodule installs; plausible range 0.45–0.80.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*

## Option C — Homepage plus separate reference page

**Estimate: 0.55**

The homepage keeps the essay, the diagram and the install box. The example, one-shot note, uninstall and links move to a second page (for example `/start`).

- Pros: a shorter homepage.
- Cons: it scatters the material the maintainer wanted on the homepage; two pages to style and verify; uninstall still has no product source.
- Driver/uncertainty: shared styling across two pages; plausible range 0.45–0.70.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*

## Recommendation

**Option B.** It delivers the agreed page as one vertical slice:

- **Entry:** a visitor understands the four steps from the first screen and copies the install prompt.
- **End-to-end outcome:** they can read the essay and find links to the full reference.
- **Recovery:** they can uninstall using a procedure that is defined in the product, not only on the website.

Merging and publishing both repositories remain separate maintainer decisions, and each repository's changes stay in its own commits. The cycle estimate above covers the scope of Option B.

**Scope v1 excludes:**
- the Readings rewrites (the maintainer decided on 2026-10-28 to keep them off for now);
- ANSI-art logo;
- slide-deck linking;
- edits to the essay text;
- release tagging.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*

## Enhancement requests

| Request | Disposition and reason | Approval status | Outcome |
| --- | --- | --- | --- |
| Include the rewritten essay voices (`temp/Railspike Readings.html`) | Declined for now. Most voices imitate named, living people, which could read as endorsement, and they would distract from the page's job. A separate `/readings` page is a possible follow-up. | Maintainer: "keep them off for now" | Excluded from v1 |
| Uninstall instructions (`todo.txt`) | In scope as part of the agreed material; Option B gives it a product source. | Pending Step 1 | — |

## Scope and estimate history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| 2026-10-28 — Intake | missing | No estimate was captured before inspection; the website, product, earlier homepage cycles and Readings were inspected before scope was stated. |
| 2026-10-28 — Step 1 handoff, v1 | 0.60 | Recommended Option B, R1/P2. Single exposed Claude Code rater; not an independent rating and not measured labor. The three option values are alternative full-cycle projections from the same start; they are not additive. Comparable to the 0.60 composer anchor (a visible surface redesign with required verification), and below the 1.00 recovery anchor. Starting revisions: `railspike-dev` `d696751`, `railspike` `main` `0dcab22`, `rlspk.github.io` `main` `946438e`. All three frozen R1 hashes were verified against the host manifest. |
