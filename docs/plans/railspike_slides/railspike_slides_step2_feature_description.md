> **Feature plan:** [Step 1](./railspike_slides_step1_solution_assessment.md) · [Step 2](./railspike_slides_step2_feature_description.md) · [Step 3](./railspike_slides_step3_development_plan.md) · [Step 4](./railspike_slides_step4_implementation_summary.md)

Debug mode: enabled

## Problem
Railspike is explained only in prose, so there is no engaging, presentable walkthrough for talks, demos, or first-time readers. Per the approved Option A, a self-contained HTML deck fills that gap.

## Assumptions (answers to Step 1 open questions; correct before approving)
- **Audience:** developers evaluating Railspike who have not used it; onboarding teammates are served secondarily.
- **Location:** website checkout `rlspk.github.io`, served at a stable path beside the homepage; plans and records stay in this repo.
- **Offline:** the deck works from a single saved file with no network or external assets.

## User stories
- As an evaluating developer, I want a short visual walkthrough so that I understand what Railspike is and whether it fits my workflow.
- As a presenter, I want one linkable, keyboard-driven deck so that I can run a talk or demo without extra tooling.
- As a maintainer, I want slide wording drawn from the README and `RAILSPIKE.md` so that the deck matches the product and is easy to update.

## Core requirements
- Roughly ten slides covering: what Railspike is, why plans live in the repo, install, the four steps, the `Approved Step N` gate, a worked example, and where to go next.
- One idea per slide; keyboard and touch navigation; readable on a laptop projector and a phone.
- No runtime dependencies or network requests; printable to PDF with one slide per page.
- Claims match current product behavior, including that approval gates are instructions the agent follows, not technical enforcement.
- Uses the existing Railspike logo and website visual style.

## Delivery scope
- **Work type:** application change (new static page in the website repository); not documentation-only.
- **Allowed files:** one new deck page (and its print styles) in `rlspk.github.io`, and plan/record files in `railspike-dev`. No existing page may link to the deck yet.
- **Not permitted:** edits to workflow instructions in `railspike`, build tooling, third-party scripts, or `.pptx` export.

## Completion boundary
A reviewer opens the deck page directly, steps through all slides by keyboard or touch, and can print it to PDF. Recovery: a broken slide is fixed by editing the single file; the page is removable without affecting the site. Release condition: reviewed on the website feature branch; linking and publishing are deferred.

## Risks
- **Drift from the product:** wording goes stale when instructions change. Validate in Step 3 by tying each slide to a source section; mitigate with a source map in the implementation summary.
- **Overclaiming enforcement or results:** slides may imply guarantees. Check each claim against README caveats before approval of Step 3.
- **Accessibility and print layout:** fixed-size slides can clip on small screens or print badly. Verify at phone width and in print preview during the first stage.
- **Wrong location or audience assumption:** rework if the assumptions above are rejected; confirm now.

## Shared component inventory
- **README, `WELCOME.md`, `RAILSPIKE.md`, website `index.html`:** existing surfaces describing the same content; the deck reuses their wording and does not alter them.
- **Website logo and homepage styles:** reuse existing assets and visual tokens; no new shared component is needed.
- **Deck page:** new, because no existing surface presents sequenced slides.

## Simple user flow
1. Visitor opens the deck page directly by its path (no site link yet).
2. Visitor advances slide by slide with arrow keys, tap, or swipe.
3. Visitor reaches the install and example slides and copies the install prompt.
4. Visitor follows the closing links to the README and `RAILSPIKE.md`, or prints the deck to PDF.

## Success criteria
- All planned slides render and navigate on desktop and phone widths without horizontal scrolling.
- The page works offline with zero network requests.
- Every factual claim traces to a README or `RAILSPIKE.md` section in the source map.
- Print preview yields one slide per page.
- No existing page references the deck; the link checkers report no new broken links.

## Enhancement Requests
- **Request:** Do not link the deck from anywhere yet; just create it.
- **Disposition and reason:** Accepted after Step 2 approval; narrows scope (removes the homepage/README links and publishing). Revised here and in Step 3 for consistency.
- **Approval status:** Pending renewed approval via `Approved Step 3`.
- **Outcome or follow-up link:** [Step 3](./railspike_slides_step3_development_plan.md).
