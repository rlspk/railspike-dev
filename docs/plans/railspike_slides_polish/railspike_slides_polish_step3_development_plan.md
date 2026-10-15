> **Feature plan:** [Step 2](./railspike_slides_polish_step2_feature_description.md) · [Step 3](./railspike_slides_polish_step3_development_plan.md) · [Step 4](./railspike_slides_polish_step4_implementation_summary.md)

Debug mode: enabled

## Completion Contract
- **Normal entry:** a reviewer opens `slides/index.html` directly by its path; nothing links to it.
- **Outcome:** 11 slides in a keynote voice, in the order: promise opener, statement titles, links at slide 10, conclusion at slide 11; sans-serif type; prints to 11 pages; offline; no horizontal scroll at 390px.
- **Recovery:** revert the stage commit(s) in `rlspk.github.io`; the single file is the only artifact.
- **Deployment/external verification:** loads from the checkout without a server; link checkers report no new findings. Merging and publishing are not part of this plan.
- **Release condition:** reviewed on the existing `feature/railspike-slides` branches, with paired commits recorded in this cycle's summary; linking and publication stay deferred.

## Key Risks
- **Voice overclaims:** superlatives imply enforcement or guarantees. Each rewritten slide is checked against the source map; the two caveats stay in plain words (stages 2–4).
- **High risk: attribution:** the deck must not name, quote, or imply endorsement by a real person. Searched for names and quote marks in stage 5.
- **Font change shifts wrapping or print:** re-verify at 390px and in print preview in stage 1, before copy changes.
- **Slide numbering:** slides 1–9 keep their numbers; only slide 11 is new, so earlier source-map entries hold. Recorded in stage 5.

## Stage 1
- Goal: Switch body type to a sans-serif system stack without changing layout.
- Dependencies: Approved Steps 2–3; reused branches confirmed unmerged; planning commit made.
- Expected changes: one font-family declaration for body and code remaining monospace.
- Verification approach: computed font in headless Chrome; 390px frame wrapping on the longest slide; print page count unchanged at 10.
- Risks or open questions:
  - Impact: wider glyphs wrap the install prompt or titles differently.
  - Early warning / validation: view slides 3 and 8 at 390px.
  - Mitigation: adjust size clamp in this stage.
- Canonical components/API contracts touched: deck page styles; homepage tokens unchanged.

## Stage 2
- Goal: Rewrite slides 1–5 in the voice, with the promise line and statement titles for slides 4 and 5.
- Dependencies: Stage 1.
- Expected changes: slide text only; slide 1 keeps the name and tagline plus one promise line.
- Verification approach: compare each claim to the source map; grep for the caveat "instructions" and "guarantee" wording; 390px view of changed slides.
- Risks or open questions:
  - Impact: the gate slide reads as a hard lock.
  - Early warning / validation: reread slide 5 against README caveat.
  - Mitigation: state it plainly as an instruction the agent follows.
- Canonical components/API contracts touched: README wording via the predecessor source map (read-only).

## Stage 3
- Goal: Rewrite slides 6–9, with slide 8 bullets reduced to one line each.
- Dependencies: Stage 2.
- Expected changes: slide text only; sample prompts remain verbatim where they are quoted from the README.
- Verification approach: confirm quoted prompts match the README; each bullet fits one line at projector width; 390px check.
- Risks or open questions:
  - Impact: a paraphrased prompt no longer matches what the product accepts.
  - Early warning / validation: diff prompts against README text.
  - Mitigation: restore verbatim wording.
- Canonical components/API contracts touched: README sample prompts (read-only).

## Stage 4
- Goal: Rewrite the links slide as slide 10 and add the conclusion as slide 11.
- Dependencies: Stage 3.
- Expected changes: slide 10 voice copy keeping its three links; new final slide "Write it down, approve it, build in checkpoints".
- Verification approach: counter reads `11 / 11` at `#11`; print gives 11 pages; external links still return 200; no new claims beyond mapped ones.
- Risks or open questions:
  - Impact: the conclusion implies results the README doesn't claim.
  - Early warning / validation: restate each phrase as a source-map row.
  - Mitigation: reuse existing wording only.
- Canonical components/API contracts touched: deck navigation counter and print rules (existing).

## Stage 5
- Goal: Record the updated source map and run final checks; no linking or publishing.
- Dependencies: Stage 4.
- Expected changes: summary updates only (source map for slide 11, slide mapping note); no file changes in `rlspk.github.io`.
- Verification approach: three link checkers on both checkouts; search the deck for personal names and quotation attributions; confirm nothing references `slides/`; open each `#1`–`#11` from a lone saved copy.
- Risks or open questions:
  - Impact: a stale map or an unnoticed attribution survives.
  - Early warning / validation: the searches above, recorded with results.
  - Mitigation: fix in the deck and re-run before handoff.
- Canonical components/API contracts touched: none.

## Enhancement Requests
- **Request:** Write all the slides in the voice of Steve Jobs.
- **Disposition and reason:** Planned in stages 2–4 as style only, with no attribution.
- **Approval status:** Approved with `Approved Step 2`; this plan awaits `Approved Step 3`.
- **Outcome or follow-up link:** [Step 2](./railspike_slides_polish_step2_feature_description.md).
