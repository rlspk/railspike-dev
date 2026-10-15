> **Feature plan:** [Step 2](./railspike_slides_polish_step2_feature_description.md) · [Step 3](./railspike_slides_polish_step3_development_plan.md) · [Step 4](./railspike_slides_polish_step4_implementation_summary.md)

Debug mode: enabled

## Cycle and branches
- Follow-up to [Railspike slides](../railspike_slides/railspike_slides_step4_implementation_summary.md), whose records are unchanged.
- Reused branches (confirmed unmerged): `feature/railspike-slides` in `railspike-dev` and in `rlspk.github.io`. Planning commit `2aa20ea`. Deck: `slides/index.html`, still not linked or published.
- Website commits per stage: Stage 1 `c2a989e`, Stage 2 `0a3efa0`, Stage 3 `19e6eb6`, Stage 4 `ffc6b8c`.

## Stage 1 - Sans-serif type
- Changes:
  - Body font stack changed from a serif stack to `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`; code stays monospace.
- Verification:
  - Slide 3 (longest prompt) in a 390px frame: no clipping or horizontal scroll; prompt box unchanged.
  - Print-to-PDF: still 10 pages.
  - Rendered in the sandbox's `system-ui` fallback (DejaVu Sans); other platforms will use their own system font and were not checked.
- Notes:
  - Slide 8 wrapping is re-checked when its bullets change in Stage 3.

## Stage 2 - Slides 1-5 in voice
- Changes:
  - Slide 1 gains a promise line ("In a few minutes you'll know how to make that happen, and exactly where you say yes.") and a short tagline-style opener.
  - Slide titles now state points: "Plans belong in your repo, not in a chat", "One prompt installs it", "Four steps, and you approve each one", "The agent stops until you say so".
  - Copy uses short declarative sentences; the install prompt is unchanged and verbatim.
- Verification:
  - Each claim was checked against the predecessor's source map: no new claims; "probably too big" and the "Approved Step 3 before building" rule are kept as in the README.
  - Caveats present in plain words: "Inspection is not a guarantee" (slide 3) and "instructions the agent follows... not a technical lock" (slide 5).
  - Slides 1 and 5 rendered in a 390px frame: text wraps with no clipping; slide 5's inner scrollbar is ordinary vertical scrolling in a short frame.
  - Script parses; deck still has 10 slides.
- Notes:
  - Slide 1 says "Your coding agent writes the plan first. Then it waits for you.": consistent with the README's "stops until you approve each one".

## Stage 3 - Slides 6-9 in voice
- Changes:
  - Rewrote slides 6-9 in short declarative sentences; titles: "Say what you want. Read what comes back.", "You shape the plan", "Every stage is a checkpoint", "Debug mode is optional".
  - Slide 8 bullets are one short line each; slide 9 states the marker file's presence-only rule.
- Verification:
  - All four quoted prompts (export request, option A/B reply, scope line, debug-mode request) were checked by exact string match against both the README and the deck: all match.
  - Slide 8 at 1280px: each bullet on one line; slide 6 and 8 at 390px: no clipping.
  - Caveat kept: "A stage commit records evidence. It doesn't prove deployment or rollback is safe."
  - Deck still 10 slides; script parses.
- Notes:
  - "Approve Step 3, and the plans get committed" compresses the README's branch-then-planning-commit sequence; the branch creation is not stated on the slide.

## Stage 4 - Links slide and conclusion
- Changes:
  - Slide 10 "Read the real thing" keeps the three links in the new voice.
  - New slide 11 "Write it down. Approve it. Build in checkpoints." with three bullets: the plan is a file you own; the agent stops until you approve; every stage leaves a record.
- Verification:
  - `#11` shows counter `11 / 11`; print-to-PDF gives 11 pages; script parses.
  - All three closing URLs returned 200. The `RAILSPIKE.md` blob URL returned a single transient 503 on the first request and 200 on three retries and via the raw URL.
  - Each conclusion bullet restates an existing source-map row (slides 1, 2/5 and 8); no new claims.
- Notes:
  - Per Ernst and Winston the deck now ends on the conclusion, not links; the slide has no "questions" or "thank you" line.

## Stage 5 - Source map, attribution and link checks
- Changes:
  - No site files changed in this stage; nothing links to the deck.
  - Slide mapping against the predecessor's source map: slides 1-9 keep their numbers; old slide 10 (links) remains slide 10; slide 11 (conclusion) is new. The predecessor's table still applies by slide number, with these additions:

    | Slide | Claim | Source |
    |---|---|---|
    | 1 | Promise: the agent writes the plan first and waits; builds after approval | README intro ("stops until you approve each one") |
    | 11 | Plan is a file; agent stops until approval; each stage leaves a record | README "Why we built this", "How commits work", "Finish and verify each stage" |
- Verification:
  - Attribution search of the deck for names and quotation markers (`jobs`, `steve`, `winston`, `ernst`, `said`, `quote`, curly quotes): no matches. The one hit for `apple` is `-apple-system` in the font stack.
  - Search of both checkouts for references to `slides/`: none outside the deck.
  - Python, Perl and Node link checkers: "Checked 1 Markdown files: local links are valid" on `rlspk.github.io`; with the historical baseline on this repo, no findings mention the slides files.
  - Opened `#1` to `#11` from a lone copy of `index.html` in a scratch directory: every title matched its slide (11 of 11).
  - `git diff main --stat` in `rlspk.github.io`: one file, `slides/index.html`, 171 insertions.
  - Deployment, publication and live-path checks: not applicable, because publication is deferred by the approved scope.
- Notes:
  - Correction to Stage 4: its first record had shell substitution drop two inline code spans; the text was repaired in this commit without amending the Stage 4 commit.
  - Not exercised by hand: real touch swipe and dark mode on devices; fonts other than the sandbox's `system-ui` fallback.
  - Deferred: linking from homepage/README, merge and publication, optional `.pptx` export.
