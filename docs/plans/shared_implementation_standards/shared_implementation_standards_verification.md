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

## Stage 2 record scenarios

- Existing component: Step 2 inventory and one-shot Reuse decisions require its source path and reuse/extension disposition; Step 3 carries it into stage fields. Passed.
- New equivalent: the same fields and common contract require explaining why existing code does not fit; neither mode treats the mockup as sufficient inspection. Passed.
- Named-environment failure: one-shot Verification and recovery plan names the replay/unaided action; shared verification rejects another-platform pass as proof. Staged Step 3 retains explicit replay coverage. Required missing evidence stays pending/blocked. Passed.
- Documentation-only: inventory identifies instruction/evidence surfaces; completion conditions select the document outcome and allowed scope; inapplicable runtime checks require reasons. Passed.
- Artifact/approval/commit parity: original staged fields, planning/stage gates, one-shot no-planning-commit rule, and scope transitions remain. Only evidence fields changed. Passed.
- Both link checkers (Python product/development) and diff checks passed; Planning and approval/scope concept paths checked. No application behavior tested.

## Stage 3 and final evidence — 2026-10-29T18:44:22Z

| Scenario | Evidence and result |
| --- | --- |
| Staged ordinary entry | RAILSPIKE mode selection → Step 2/3 planning fields → Step 4 Before/Do shared contract → After final review. Passed. |
| One-shot ordinary entry/resumption/closeout | Explicit shared reading at entry/resumption, operational execution link, named record fields, and closeout review link. Passed; no extra planning gate/commit required. |
| Direct incident replay | WELCOME's proposed host Implementation standards section requires inspection before markup/styles, including source paths and reuse/extension or justification. An agent starting from a mockup must inspect existing components. It applies outside Railspike without importing its lifecycle/study; passed as an instruction scenario, not a v3 browser test. |
| Consent accepted | Both sections are shown in the proposed text before the existing yes/no question. Yes preserves existing engineering/Railspike guidance and checks conflicts; edits beyond the proposal need authorization. Passed. |
| Consent declined/unanswered | No/anything-else branches leave host guidance unchanged, do not reoffer, and report declined/not answered. README explicitly says updating Railspike alone does not install host rules. Passed. |
| Existing-rule conflict / opt-out | Conflicts require clarification rather than replacement. A task opt-out honors Direct execution; adopted host engineering rules still apply. Existing approval/branch/study policies stay separate. Passed. |
| Named-environment recovery | Common standard requires relevant failure replay or appropriate manual recovery; another-platform pass cannot establish success; required missing evidence remains pending/blocked. Passed. |
| Documentation-only | Allowed file boundaries and document evidence checks explicit; runtime only applicable if claims require it. Passed. |

Commands/results:

- `python scripts/check-markdown-links.py ../railspike`: passed, 18 Markdown files.
- `python scripts/check-markdown-links.py . docs/maintainers/historical-link-baseline.txt`: passed, 218 Markdown files, 80 acknowledged historical targets; baseline unchanged.
- `bash scripts/check-railspike-git-workflow.sh ../railspike`: passed. This fixture exercises documented Git update behavior in temporary repositories, not agent adherence.
- `git -C ../railspike diff --check` and `git diff --check`: passed after recorded corrections; staged checks also required before each stage commit.
- Product diff from `583e69d`: only approved Markdown paths. Development changes: this cycle's records/index/ledger and touched concepts only. No checker implementation changed, so extra runtime variants are inapplicable; installation source/copy/update mechanics unchanged, so source-migration fixture inapplicable.
- Source map reconciled against final instructions; required staged approval/planning/stage-commit rules retained, one-shot exceptions retained, and touched concept descriptions/paths match. Common substantive authority lives in one file; remaining staged fields/checkpoints place its evidence rather than define another contract.

Limits: document review establishes coverage and link integrity, not live agent compliance or v3 UI correctness. No deployment, external publication, release or consumer update was performed or claimed.
