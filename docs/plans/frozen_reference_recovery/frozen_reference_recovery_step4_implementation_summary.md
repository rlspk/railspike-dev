> **Feature plan:** [Step 2](./frozen_reference_recovery_step2_feature_description.md) · [Step 3](./frozen_reference_recovery_step3_development_plan.md) · [Step 4](./frozen_reference_recovery_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/frozen_reference_recovery`, standing R1/P2; [ledger](../../research/effort_estimation/collection.md).

## Execution and authorization

Branch in both product and development: `fix/frozen-reference-recovery`. Planning commit `f1076bc`. The user's renewed “Please fix what you can” authorizes direct narrow recovery; no literal Step 2/3 approval is claimed. Earlier pending states are historical. Product changes remain local, without merge/tag/push/publication. Host edits remain uncommitted for their normal integration workflows.

Step 4 entry, 2026-10-23T17:44:40Z: scope v1/R1/P2, original start revisions and exposure unchanged; Codex single exposed rater. **0.65 total reaffirmed** before implementation, not remaining effort or measured labor. Initial sources were already read/hash-verified. No missing historical checkpoint is backfilled; no runtime dependency added.

## Stage 1 - Exact recovery and reusable guidance

- Changes: retained three exact source documents as text snapshots with relative cached paths and full revision/hash provenance in `docs/research/effort_estimation/references/R1/`. Product root links to the recovery procedure; the effort guide covers wrong paths, changed current documents, historical reads, offline reuse, failure and preserved historical checkpoints.
- Verification: all three snapshots match the frozen expected SHA-256 values; historical feedback came from the exact local v3 revision without branch movement. Product links passed for 15 Markdown files; README Git-workflow fixture and product whitespace passed. Only the two scoped product documents changed. No new runtime dependency or installation behavior.
- Notes: product commit `742d1d74f11fcf1b2e91eec9ecae7848489b0520`. Source snapshots are documentation evidence, not executable components. Application/UI/deployment, installation migration and release checks are inapplicable; no such outcomes are claimed. Eight-host repair remains Stage 2.

## Stage 2 - Eight host ledgers repaired

- Changes: installed three exact local source snapshots and a portable manifest in main v3, six agent clones and v3-test-kris. Replaced only the three frozen-source link targets and inserted one dated recovery notice per ledger. Original source targets remain in each manifest.
- Verification: 24 source hashes match R1. After removing the new notice and reversing the three link substitutions, every ledger is byte-identical to its pre-repair content. Current feedback hashes are unchanged in every host. Existing destination conflicts and changed-ledger guards were checked before writes; none blocked recovery. Per-host verification is retained in `docs/research/effort_estimation/2026-10-23-reference-recovery-verification.json`.
- Notes: Stage 1 development commit `50399b2`; product commit is recorded above. Host changes remain uncommitted; host branches and installed product files were not changed. Stage 2 only writes the scoped ledger and four reference/provenance files per host. No application/runtime/UI/deployment or installation-upgrade outcome is claimed. Relocation/failure/idempotence checks remain Stage 3.
