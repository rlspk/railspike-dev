> **Feature plan:** [Step 1](./merge_acceptance_step1_solution_assessment.md) · [Step 2](./merge_acceptance_step2_feature_description.md) · [Step 3](./merge_acceptance_step3_development_plan.md) · [Step 4](./merge_acceptance_step4_implementation_summary.md)

Debug mode: enabled (host marker present).
Effort study: `railspike-effort` / `railspike/merge_acceptance`; [standing enrollment and ledger](../research/effort_estimation/collection.md). No parent cycle.
Extended estimates: enabled.

**Cycle estimate: 0.45**

Concepts touched: none in the [concept inventory](../concepts/inventory.md); this cycle adds none.

## Completion Contract

- Work type: documentation-only, as approved in Step 2.
- Allowed files, product (`railspike` checkout): `RAILSPIKE.md`, `docs/effort-estimation.md`, `docs/workflow/step4_implementation_after.md`. `docs/workflow/one_shot.md` was checked and does not mention the maintainer judgment, so it does not change.
- Allowed files, this repository: `docs/research/effort_estimation/collection.md` and this cycle's plans and debug log.
- Audience outcome: an agent reading only the product contract records its own fit judgment at closeout, marks acceptance as awaiting merge, and later records "accepted by merge" from merge or release evidence. No product text asks the agent to wait for the maintainer.
- Correction path: the maintainer reviews the product branch before merge.
- Evidence boundary: the test reading of `v3/instance_image_import`, link checks in both repositories, and `git diff --check`. Runtime, deployment and release checks do not apply: no scripts, website or release change.
- Handoff: product commits on branch `claude/merge-acceptance` in `railspike`, paired commit IDs recorded in the Step 4 summary here. No merge or release in this cycle.

## Key Risks

- Push access to `rlspk/railspike`. Impact: the product branch cannot reach GitHub from this session. Early validation: a test push at Step 4 entry, before Stage 1 edits. Mitigation: the maintainer allows attaching the repository, or pushes a prepared branch locally.
- Cycles with no merge. Checked in this project's index: several cycles were released as betas from unmerged branches, and research cycles end in this repository's own main branch. Mitigation: the rule counts a merge into the host's main branch or a published release, whichever comes first.
- **High risk:** agent judgments read as maintainer judgments. Impact: the study would overstate human agreement. Mitigation: the product text requires the judge to be named in every record, and the P3 section keeps agent and maintainer judgments in separate counts.

## Stage 1

**Estimate: 0.20**

- Goal: the product contract states the merge-as-acceptance rule.
- Dependencies: push access check passed or a local-push fallback agreed.
- Expected changes:
  - `RAILSPIKE.md`, Checkpoints table, "Step 4 closeout" row: the implementing agent's labeled fit judgment replaces "maintainer comfortable-fit judgment".
  - `RAILSPIKE.md`, closeout paragraph: replace "the maintainer judgment … mark study acceptance pending" with the three acceptance states (awaiting merge, accepted by merge or release, not accepted) and the rule that later ledger updates record merge evidence. A maintainer judgment, when given, is recorded beside the agent's and wins.
  - `docs/effort-estimation.md`, one-shot "Closeout" row and closeout paragraph: the same rule in the same terms.
  - `docs/workflow/step4_implementation_after.md`, effort paragraph: record the agent's fit judgment and "acceptance: awaiting merge"; never ask the maintainer for it.
- Verification approach: search the product for "maintainer comfortable-fit", "fit/acceptance pending" and "acceptance pending" and confirm none remain; product link check; `git diff --check`; writing-style read.
- Estimate details: driver: keeping four passages consistent in plain words; uncertainty: low.
- Risks or open questions: none beyond Key Risks.
- Canonical components/API contracts touched: the effort-estimation contract in `RAILSPIKE.md` and `docs/effort-estimation.md`, changed in place.

## Stage 2

**Estimate: 0.15**

- Goal: this project records protocol P3 and proves the rule on a real cycle.
- Dependencies: Stage 1.
- Expected changes:
  - `collection.md`: a dated "Protocol P3" section stating the rule, its effective date, that P2 records keep their wording, and that agent and maintainer judgments are counted separately. Index row for this cycle's closeout.
  - Step 4 summary: the test reading, which applies only the new product text to `v3/instance_image_import` and checks that it comes out "accepted by merge" (gulkily/v3#35) with an agent fit judgment.
- Verification approach: the test reading above; link checks in this repository (Python, Perl and Node checkers) and in the product checkout; `git diff --check`; paired commits recorded.
- Estimate details: driver: the P3 wording and link checks; uncertainty: low.
- Risks or open questions: none beyond Key Risks.
- Canonical components/API contracts touched: `docs/research/effort_estimation/collection.md`, extended with a section.

## Study checkpoint

2026-11-06T20:08:21Z, `railspike-effort` / `railspike/merge_acceptance`, Step 3 handoff. Step 2 explicitly approved. Scope v1/A unchanged. Starting revisions `4c64dd5` (railspike-dev) and `5d54e06` = `v0.6.1-beta.1` (railspike). Reference R1, protocol P2; frozen R1 hashes not re-verified. Single exposed Claude rater. Whole-cycle projection **0.45** reaffirmed. Stage work S1 0.20 and S2 0.15 are separate judgments and do not add up to the cycle estimate. No implementation, measured labor or accepted outcome.

*— Claude · 2026-11-06 UTC*
