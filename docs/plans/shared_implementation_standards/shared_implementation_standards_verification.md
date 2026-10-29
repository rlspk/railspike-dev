# Shared implementation standards verification

## Source obligation map (before extraction)

| Existing source | Obligation retained in common standard | Mode-specific remainder |
| --- | --- | --- |
| Step 2 shared inventory; Step 4 Do reuse check; Key Rules | Inspect existing surfaces/components/contracts, reuse/extend, justify new equivalents | Step 2 inventory field |
| Step 3 Completion Contract; Step 4 Do/After | Normal entry, end-to-end result, recovery and release condition; documentation alternative | Approved staged contract and plan fields |
| Step 2/3 risks and named environment | Impact, early validation, mitigation; resolve material risk before dependent work; replay reported failure in relevant environment | Planning handoffs |
| Step 4 Do simplest implementation; Key Rules schema preference | Simplest viable change; existing models/fields where possible | Stage sizing |
| Step 4 Do/After verification | Document integrity/scope; roles, migrations, deployment/external dependencies; status labels; baseline failures; no overstated passes | Stage checks/commits |
| Key Rules/enhancement policy and one-shot scope rules | Authorized boundary, no silent expansion, preserve unrelated work | Each mode's approval/transition rules |
| New explicit final-review requirement | Review duplication, file scope and documentation before completion | Existing commit cadence |

This map is documentation review, not live agent compliance. Shared scope, concept, study, debug and attribution policies retain their own authoritative homes.

## Stage 1 results

Passed: staged entry Before → shared contract → Do and After references; one-shot entry → execution → resumption → closeout references. The common contract retains every mapped substantive obligation, including missing required recovery as pending/blocked rather than inapplicable. Staged commit and approval text remains in its existing locations. Documentation scope/verification has an explicit alternative. Product and development link commands passed (18 / 218 files, development baseline 80); diff checks passed after correcting planning hard-break spaces. Source paths in the new concept resolve. No runtime claim.
