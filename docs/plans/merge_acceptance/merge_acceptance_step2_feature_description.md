> **Feature plan:** [Step 1](./merge_acceptance_step1_solution_assessment.md) · [Step 2](./merge_acceptance_step2_feature_description.md) · [Step 3](./merge_acceptance_step3_development_plan.md) · [Step 4](./merge_acceptance_step4_implementation_summary.md)

Debug mode: enabled (host marker present).
Effort study: `railspike-effort` / `railspike/merge_acceptance`; [standing enrollment and ledger](../../research/effort_estimation/collection.md). No parent cycle.
Extended estimates: enabled.

**Cycle estimate: 0.45**

## Problem

The effort study counts a cycle as an accepted outcome only after the maintainer records a fit judgment and an acceptance. No step asks for them, so almost every cycle stays pending and the six-outcome review never happens.

Concepts touched: none in the [concept inventory](../../concepts/inventory.md); this cycle adds none.

## User stories

- As a maintainer, I want my ordinary merge or release to count as acceptance, so that I never have to remember a separate study step.
- As an implementing agent, I want a clear rule for writing the fit judgment at closeout, so that I can finish the record without waiting for the maintainer.
- As a maintainer, I want to override an agent's fit judgment in one line, so that I can still correct it when I disagree.
- As a study reviewer, I want to tell agent judgments from maintainer judgments, so that I can weigh them differently.

## Core requirements

- The implementing agent records the comfortable-fit judgment at closeout and labels it as an agent judgment. It is never presented as the maintainer's.
- A cycle counts as accepted once its delivered work is merged into the host's main branch or published in a release. The record names the merge or release.
- Closeout usually happens before the merge. Until acceptance evidence exists, the record says "acceptance: awaiting merge", not "maintainer acceptance pending".
- Any later agent that touches the ledger, and any study review, records the merge evidence for earlier cycles it can check. A closed, unmerged or replaced cycle is recorded as not accepted, with its reason. The maintainer is never asked to do this.
- A maintainer judgment, when given, is recorded beside the agent judgment and wins for counting. Existing P2 records keep their wording.

## Delivery scope

- Work type: documentation-only.
- Product files in the separate `railspike` checkout: `RAILSPIKE.md` (checkpoint table and closeout paragraph), `docs/effort-estimation.md` (checkpoint table and closeout guidance) and `docs/workflow/step4_implementation_after.md` (effort paragraph). `docs/workflow/one_shot.md` changes only if its closeout wording names the maintainer judgment.
- Development files in this repository: protocol P3 in `docs/research/effort_estimation/collection.md`, and this cycle's plans and debug log.
- Audience and outcome: agents running enrolled cycles follow the new closeout rule without the maintainer's help; the maintainer sees accepted outcomes accumulate.
- No scripts, checks or website files change. Updating existing pending records in this project and in v3 is a separate follow-up cycle.
- No release is part of this cycle. Publishing a beta needs the maintainer's separate confirmation of an exact version.

## Completion boundary

- Document completion: the four product passages state the new rule in plain wording, with no remaining instruction to wait for the maintainer judgment.
- Audience outcome: an agent reading only the product contract can close out a cycle and later record its acceptance from merge evidence.
- Correction path: the maintainer reviews the product branch before merge; a wrong rule is fixed in the same cycle.
- Handoff: product commits on a feature branch in `railspike`, paired commits recorded here, link checks passing in both repositories.

## Risks

- **Merge is not always review.** Impact: in hosts that merge without reading, a merge says little. Earliest validation: Step 3 wording review. Mitigation: call it "accepted by merge", keep the agent's fit judgment separate, and let a host protocol require more.
- **Agent bias.** Impact: the agent that estimated also judges fit, and may favor its own estimate. Validation: the study review compares agent judgments with any maintainer overrides. Mitigation: label every agent judgment and keep the maintainer override.
- **Cycles without a merge.** Impact: research or release-only cycles have no merge to point to. Validation: check this project's index for such cycles in Step 3. Mitigation: a published release, or an explicit maintainer instruction to keep the work, also counts as acceptance evidence.
- **Push access to the product.** Impact: this session cannot push to `rlspk/railspike` yet. Validation: a test push at Step 4 entry. Mitigation: the maintainer grants access, or pushes the product branch locally.

## Shared component inventory

- `RAILSPIKE.md`, Experimental Effort Estimation → Checkpoints: the "Step 4 closeout" table row and the closeout paragraph. Change in place; no new section.
- `docs/effort-estimation.md`: the "Closeout, including incomplete outcomes" row of the one-shot checkpoint table, and the closeout paragraph after the record template. Change in place.
- `docs/workflow/step4_implementation_after.md`: the effort paragraph. Change in place.
- `docs/research/effort_estimation/collection.md` (this repository): add a dated P3 section; leave P2 text and index rows unchanged.
- No new component. The rule fits into existing closeout guidance.

## Simple user flow

1. An agent closes out an enrolled cycle and writes its retrospective assessment and its own fit judgment.
2. The record says "acceptance: awaiting merge".
3. The maintainer merges the work or publishes a release, as usual.
4. The next agent that updates the ledger finds the merge and records "accepted by merge" with its commit.
5. After six accepted outcomes, an agent proposes the study review.

## Success criteria

- No product instruction tells an agent to wait for, or ask for, a maintainer judgment at closeout.
- Each record shows who made the fit judgment and what evidence accepted the cycle.
- A test reading: following only the changed product text, the `v3/instance_image_import` cycle comes out "accepted by merge" (gulkily/v3#35) with an agent fit judgment.

*— Claude · 2026-11-06 UTC*

## Study checkpoint

2026-11-06T16:51:41Z, `railspike-effort` / `railspike/merge_acceptance`, Step 2 handoff. Step 1 Option A explicitly approved. Scope v1/A. Starting revisions `4c64dd5` (railspike-dev) and `5d54e06` = `v0.6.1-beta.1` (railspike). Reference R1, protocol P2; frozen R1 hashes not re-verified. Single exposed Claude rater. Projected total 0.40 → **0.45**, from new understanding, not changed scope: closeout happens before the merge, so the rule also needs a later step that records merge evidence. Step 1 values preserved. No implementation, measured labor or accepted outcome.

## Enhancement Requests

None yet.
