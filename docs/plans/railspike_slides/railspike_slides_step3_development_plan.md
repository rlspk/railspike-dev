> **Feature plan:** [Step 1](./railspike_slides_step1_solution_assessment.md) · [Step 2](./railspike_slides_step2_feature_description.md) · [Step 3](./railspike_slides_step3_development_plan.md) · [Step 4](./railspike_slides_step4_implementation_summary.md)

Debug mode: enabled

## Completion Contract
- **Normal entry:** a visitor opens the deck page directly by its path; no homepage, README, or other link points to it yet.
- **Outcome:** about ten slides navigable by keyboard, tap, or swipe; works offline from the single file; prints one slide per page.
- **Recovery:** a bad slide is fixed by editing the single file; removing the page reverts the feature cleanly.
- **Deployment/external verification:** the page loads from the website checkout without a server; link checkers report no new broken links. Merging or publishing is not part of this plan.
- **Release condition:** reviewed on the website feature branch, with paired website and `railspike-dev` commits recorded; publication and linking are deferred.

## Key Risks
- **Drift from product wording:** each slide gets a source-map entry (stage 5) before release.
- **Overclaiming enforcement:** gates are described as agent instructions, not technical enforcement; checked in stages 3–4.
- **Unlinked page is easy to forget:** record in the summary that linking and publishing remain deferred.
- **High risk: unreadable on phone or in print:** validate layout in stage 2 before any content is written.
- **Wrong location assumption:** confirm the website path in stage 1 before building.

## Stage 1
- Goal: Create a navigable empty deck shell at an agreed website path.
- Dependencies: Approved Steps 1–3; feature branches in `railspike-dev` and `rlspk.github.io`.
- Expected changes: new `slides/index.html` with a few placeholder slides, slide container, and keyboard/touch navigation with a slide counter.
- Verification approach: open the file directly (no server) and step through placeholders by arrow key and swipe; confirm no network requests.
- Risks or open questions:
  - Impact: a path that collides with existing site files.
  - Early warning / validation: list the website tree before creating the file.
  - Mitigation: choose another path and update the plan notes.
- Canonical components/API contracts touched: none; homepage `index.html` is read for style tokens only.

## Stage 2
- Goal: Apply Railspike styling and make layout responsive and printable.
- Dependencies: Stage 1.
- Expected changes: inline styles reusing the homepage's colors and the logo, phone-width layout, print rules giving one slide per page, readable type sizes.
- Verification approach: check at phone and projector widths and in print preview; confirm no horizontal scroll and light/dark legibility.
- Risks or open questions:
  - Impact: clipped text on small screens or merged print pages.
  - Early warning / validation: placeholder slides with the longest planned text.
  - Mitigation: adjust sizing rules before content stages.
- Canonical components/API contracts touched: website logo asset and homepage visual tokens (reused, unmodified).

## Stage 3
- Goal: Write slides 1–5: what it is, why plans live in the repo, install, the four steps, the approval gate.
- Dependencies: Stage 2.
- Expected changes: slide content using README and `RAILSPIKE.md` wording; one idea and a short line per slide.
- Verification approach: compare each claim to its source section; confirm the gate is described as instructions, not enforcement.
- Risks or open questions:
  - Impact: paraphrase that overstates guarantees.
  - Early warning / validation: reread README caveats against slide text.
  - Mitigation: quote or tighten the wording.
- Canonical components/API contracts touched: README and `RAILSPIKE.md` wording (read-only).

## Stage 4
- Goal: Write slides 6–10: the worked approval exchange, shaping the plan, debug and branches, and next links.
- Dependencies: Stage 3.
- Expected changes: remaining slides and closing links to README, `RAILSPIKE.md`, and the website.
- Verification approach: walk the full deck end to end; confirm slide count, order, and that closing links resolve.
- Risks or open questions:
  - Impact: example drifts from the actual `Approved Step N` flow.
  - Early warning / validation: check the example against `WELCOME.md`.
  - Mitigation: reuse its sample phrasing.
- Canonical components/API contracts touched: `WELCOME.md` example text (read-only).

## Stage 5
- Goal: Record the claim-to-source map and run link checks; add no links to the deck.
- Dependencies: Stage 4.
- Expected changes: source map in the implementation summary; no edits to homepage, README, or other existing pages.
- Verification approach: run the three link checkers on both checkouts; confirm no new broken links, that every slide maps to a source section, and that `grep` finds no references to the deck path outside the deck.
- Risks or open questions:
  - Impact: the deck's own closing links to README and `RAILSPIKE.md` break.
  - Early warning / validation: link checker output for the deck file.
  - Mitigation: fix targets within the deck file only.
- Canonical components/API contracts touched: none.

## Stage 6
- Goal: Review the finished deck on the website feature branch and record evidence; do not merge or publish.
- Dependencies: Stage 5.
- Expected changes: summary entry recording both commits, results, and the deferred link/publish decision.
- Verification approach: open the file locally, step through every slide, print to PDF, and test offline from a saved copy.
- Risks or open questions:
  - Impact: an unmerged branch is mistaken for a release.
  - Early warning / validation: summary states "not published, not linked".
  - Mitigation: a later cycle handles linking and publication.
- Canonical components/API contracts touched: none.

## Enhancement Requests
- **Request:** Do not link the deck from anywhere yet; just create it.
- **Disposition and reason:** Accepted; narrows scope. Stage 5 no longer edits the homepage or README, and Stage 6 no longer publishes. Step 2's link requirements are superseded as recorded there.
- **Approval status:** Pending renewed `Approved Step 3`.
- **Outcome or follow-up link:** Linking and publication deferred to a later cycle.
