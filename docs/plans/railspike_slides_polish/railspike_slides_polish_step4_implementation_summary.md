> **Feature plan:** [Step 2](./railspike_slides_polish_step2_feature_description.md) · [Step 3](./railspike_slides_polish_step3_development_plan.md) · [Step 4](./railspike_slides_polish_step4_implementation_summary.md)

Debug mode: enabled

## Cycle and branches
- Follow-up to [Railspike slides](../railspike_slides/railspike_slides_step4_implementation_summary.md), whose records are unchanged.
- Reused branches (confirmed unmerged): `feature/railspike-slides` in `railspike-dev` and in `rlspk.github.io`. Planning commit `2aa20ea`. Deck: `slides/index.html`, still not linked or published.
- Website commits per stage: Stage 1 `c2a989e`.

## Stage 1 - Sans-serif type
- Changes:
  - Body font stack changed from a serif stack to `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`; code stays monospace.
- Verification:
  - Slide 3 (longest prompt) in a 390px frame: no clipping or horizontal scroll; prompt box unchanged.
  - Print-to-PDF: still 10 pages.
  - Rendered in the sandbox's `system-ui` fallback (DejaVu Sans); other platforms will use their own system font and were not checked.
- Notes:
  - Slide 8 wrapping is re-checked when its bullets change in Stage 3.
