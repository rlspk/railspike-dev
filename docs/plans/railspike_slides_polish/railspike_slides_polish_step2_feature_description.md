> **Feature plan:** [Step 2](./railspike_slides_polish_step2_feature_description.md) · [Step 3](./railspike_slides_polish_step3_development_plan.md) · [Step 4](./railspike_slides_polish_step4_implementation_summary.md)

Debug mode: enabled

## Cycle
- **Predecessor:** [Railspike slides](../railspike_slides/railspike_slides_step4_implementation_summary.md), complete and unmerged. Its content is unchanged by this cycle.
- **Cycle identity:** `railspike_slides_polish`. Step 1 skipped; the approach (edit the existing deck) is already settled.
- **Branches reused (requested, confirmed unmerged):** `feature/railspike-slides` in `railspike-dev` and in `rlspk.github.io`.
- **Source of changes:** the review in the talk-notes file (Winston, "How to Speak"; Ernst, "How to give a technical presentation"). The user confirmed sans-serif type is acceptable.

## Problem
The deck explains Railspike well but is weak as a talk: it lacks an up-front promise, several titles are labels, and it ends on links instead of a conclusion.

## User stories
- As a presenter, I want the deck to open with a promise of what the audience will know so that listeners know why to follow along.
- As an audience member, I want each slide title to state its point so that I can follow the argument from titles alone.
- As a presenter, I want a closing conclusion slide that stays up during questions so that the talk ends on the main message.
- As a viewer in a room or on a phone, I want sans-serif type so that text reads clearly at a distance.

## Core requirements
- Slide 1 keeps the name and tagline and adds one promise line stating what the audience will know by the end.
- Titles that are labels become statements: slide 4 "Four steps, and you approve each one"; slide 5 "The agent stops until you say so".
- The deck ends on a new conclusion slide, "Write it down, approve it, build in checkpoints", placed after the links slide, which becomes slide 10 of 11.
- Slide 8 bullets shorten to one line each; body type changes to a sans-serif system stack.
- **Voice (approved with Step 2):** all slide copy is rewritten in a keynote voice modeled on Steve Jobs: short declarative sentences, plain words, concrete contrasts, and a single idea per slide. Voice is style only: the deck does not name, quote, or attribute anything to him, and every claim keeps its README-backed meaning.
- All existing behavior is preserved: navigation, offline use, print with one slide per page, and no new links to the deck from anywhere.

## Delivery scope
- **Work type:** application change (static page edits); not documentation-only.
- **Allowed files:** `slides/index.html` in `rlspk.github.io`; plan and record files in `railspike-dev`.
- **Not permitted:** naming, quoting, or implying endorsement by a real person; edits to existing site pages, the product repository, new assets, scripts, linking or publishing the deck, and speaker notes inside the deck.

## Completion boundary
A reviewer opens the page directly and steps through 11 slides in the new order; it prints to 11 pages. Recovery: the single file is reverted by commit. Handoff condition: reviewed on the existing branch; linking and publishing remain deferred.

## Risks
- **New claims on the conclusion slide:** impact is overstatement. Validate each phrase against the predecessor's source map in the first stage; reuse existing wording only.
- **Font change breaks layout or print:** wrapping and page count may shift. Re-verify at 390px and in print preview in the same stage.
- **Voice overclaims:** punchy keynote copy tends toward superlatives ("revolutionary", "never") that could imply enforcement or guarantees the README disclaims. Validate each rewritten slide against the source map in the copy stage; keep the "instructions, not enforcement" and "inspection is not a guarantee" caveats in plain words.
- **Slide numbering drift:** anything citing slide numbers (the predecessor's source map and the talk notes) goes stale. Record a mapping in the summary.

## Shared component inventory
- **Deck page:** extended in place; no new component.
- **Homepage styles and logo:** unchanged, reused as before.
- **Predecessor source map:** read-only; this cycle records changed slide numbers beside it.

## Simple user flow
1. Reviewer opens the deck page directly.
2. Reviewer sees the promise on slide 1 and reads statement titles through slide 9.
3. Reviewer reaches links (slide 10), then the conclusion (slide 11) that stays up for questions.
4. Reviewer prints to PDF and gets 11 pages.

## Success criteria
- Slide 1 contains the promise; no label-only titles remain among the changed slides.
- The final slide is the conclusion; the deck has 11 slides and prints to 11 pages.
- No horizontal scroll at 390px; no network requests; no existing page changed or linked to the deck.
- Body font computes as sans-serif in headless Chrome.
- Every slide's claims still map to the predecessor's source map, and the two caveats (agent instructions, not enforcement; inspection is not a guarantee) remain on the deck in plain words.
- No name, quote, or attribution to a real person appears in the deck.

## Enhancement Requests
- **Request:** Start a new cycle for the deck review changes; sans-serif is fine.
- **Disposition and reason:** Accepted as this cycle's scope.
- **Approval status:** Approved with `Approved Step 2`.
- **Outcome or follow-up link:** Planned in [Step 3](./railspike_slides_polish_step3_development_plan.md).
- **Request:** Write all the slides in the voice of Steve Jobs.
- **Disposition and reason:** Accepted as a copy-style change within the same deck file; recorded as pending, and it replaces the wording of the changes above, not their structure. Style only, with no attribution.
- **Approval status:** Approved with `Approved Step 2`.
- **Outcome or follow-up link:** Planned in [Step 3](./railspike_slides_polish_step3_development_plan.md).
