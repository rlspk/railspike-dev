> **Feature plan:** [Step 1](./railspike_slides_step1_solution_assessment.md) · [Step 2](./railspike_slides_step2_feature_description.md) · [Step 3](./railspike_slides_step3_development_plan.md) · [Step 4](./railspike_slides_step4_implementation_summary.md)

Debug mode: enabled

## Branches and commits
- `railspike-dev`: `feature/railspike-slides`, created from `main` (the stale `feature/first-release` was already merged). Planning commit `7a00aa9`.
- `rlspk.github.io`: `feature/railspike-slides`, created from `main`. Deck path: `slides/index.html`. Not linked, not published.

## Stage 1 - Deck shell
- Changes:
  - New `slides/index.html` in `rlspk.github.io`: three placeholder slides, one visible at a time, a counter, and navigation by arrow/space/page/home/end keys and horizontal swipe.
  - Without JavaScript, all slides display stacked.
  - Slide position is mirrored in the URL hash.
- Verification:
  - Script parses under `node`; the file contains no `http` references, so no network requests.
  - Headless Chrome opened the file via `file://…#2` with no server: slide 2 was current and the counter read `2 / 3`.
  - Swipe and key handling were not exercised interactively; they are to be checked by hand in Stage 2.
  - Website tree listed before creation: no collision at `slides/`.
- Notes:
  - Homepage `index.html` was read for style tokens only and not modified.
  - The logo will use a relative path; a saved single-file copy would show alt text only, so offline logo handling is to be decided in Stage 2.
