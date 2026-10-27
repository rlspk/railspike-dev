# Detailed effort estimate verification

This is a static instruction and example review of the optional extension, not a live-agent experiment or validation of effort prediction. Product base: `742d1d74f11fcf1b2e91eec9ecae7848489b0520`. [Approved plan](../../plans/detailed_effort_estimates/detailed_effort_estimates_step3_development_plan.md) · [Implementation summary](../../plans/detailed_effort_estimates/detailed_effort_estimates_step4_implementation_summary.md).

## Scenario walkthroughs

All rows passed by following the named product contracts through their examples/templates. Values in the product guide are explicitly fictional. Actual dates/rater/exposure for this cycle remain in its planning/summary artifacts.

| Scenario | Instruction trace and reviewed result |
| --- | --- |
| Unselected host, extension off | Root activation and guide leave the existing workflow unchanged. No added stage/option fields, enrollment, repeated mode question or score requirement. |
| Selected study, no extension request | Ordinary cycle checkpoints remain active. Study enrollment does not enable the extension; Step 3/4 optional template fields are explicitly omitted. |
| Explicit per-cycle enable | Selected study/reference established first → `Extended estimates: enabled` below study field → inherit through Steps 1–4. No additional work approval inferred. |
| Standing policy and resumption | Policy enables future selected cycles without another question. Restore explicit changes, current artifact state and applicable policy. Recorded disabled state is retained; missing field alone does not override an enabled policy. Unresolvable selected evidence conflicts stop only dependent estimation. |
| Explicit disable and debug independence | Current artifact records disable; earlier estimates remain. Debug mode does not control study or extended estimates. |
| Different option outcomes and combination | A 0.40 and B 0.75 cover explicit different scopes from common artifact metadata. Combined C is freshly judged 0.60 with its own driver/uncertainty; A/B remain. Recommended-cycle snapshot is separately identified. |
| Planned stages and shared work | Stage 1 owns parser/checks; Stage 2 owns integration/recovery and reuses those checks. Stage values 0.10/0.20 remain partial work judgments; independent cycle 0.45 is neither their sum nor a conversion to hours. |
| Entry and planning commit | Step 4 Before creates summary after the planning commit, then inherits approved identities, scopes, originals and uncertainty before implementation. Copies are not independent ratings. |
| Discovery without scope change | Guide retains original 0.20, appends entire-stage revision 0.30 before dependent work for already-approved recovery complexity, and separately reassesses the cycle. It does not say 0.30 remaining or calculate the cycle by a delta. |
| Changed scope | Root/Do retain normal renewed approvals. A corrected guide sentence makes a new scope version explicit, with original scope/starting point retained in history and each estimate tied to its recorded scope. No original observation is overwritten. |
| Stage completion | Do/After retain original/revised values and add retrospective 0.25 only with completed-scope verification. Measured work stays unknown; timestamps and retrospective differences are not labor. Stage record belongs in the stage-summary commit. |
| Missing or changed frozen source | Guide routes to exact-source recovery. Affected numeric values are unavailable with reason, not zero or guessed reference content. Earlier scores/gaps are preserved. |
| Late activation or resumed older work | Before/Do distinguish original missing estimate from a new current dated total-stage judgment, with exposure. Completed historical work may receive a current retrospective assessment only when scope/evidence support it. |
| Blocked, skipped or split stage | Keep status/reason/prior values; no zero or completion substitution. Original split stage remains superseded with its scope/estimates and fresh linked child identities, including deferred work. No additional independent cycle outcome. |
| Concise views and corrections | Current-value lines may link shared metadata and immutable revision history. A correction appends a dated entry identifying the superseded entry. Resumption alone does not duplicate a snapshot; per-stage diagnostics are not added. |

## Integrity and scope checks

- Product local links: passed for 15 Markdown files.
- Development local links: passed with the unchanged explicit historical baseline.
- Existing README Git-workflow fixture: passed; checker implementations unchanged.
- Frozen source verification: calibration report, implementation diff review and historical feedback retain all three expected SHA-256 values. Reference definition/version and source files are unchanged.
- Product diff: eleven scoped Markdown files only: root/README/effort guide, Step 1/2, Step 3 before/do/after and Step 4 before/do/after. No code, test, CI, dependency, installation or other file change. Stage 4's clarification is confined to estimate scope/version meaning.
- Development commits: planning artifact/log/index organization first, implementation summary only afterward, followed by one development summary/evidence commit per stage. Product stages are committed before their paired development stage records. Stage 4's final audit records exact IDs in the summary/debug handoff.
- Product/development whitespace and allowed-file checks passed. No new tooling or application test was introduced for these instruction-only changes.

## Limits and publication status

No application/runtime/UI, deployment, host upgrade, live-agent compliance or measured labor check is applicable to these documents. Stage-level calibration, predictive accuracy and maintainer comfortable-fit acceptance are not established. This cycle preserves its initial whole-cycle 0.60 projection and explicitly labels supplemental stage-work assessments. No merge, tag, beta release, push or host-copy update is part of this cycle.
