> **Feature plan:** [Step 2](./frozen_reference_recovery_step2_feature_description.md) · [Step 3](./frozen_reference_recovery_step3_development_plan.md) · Step 4 (not yet started)

Debug mode: enabled

Effort study: `railspike-effort / railspike/frozen_reference_recovery`; standing R1/P2 enrollment; [ledger](../../research/effort_estimation/collection.md). Optional Step 1 skipped: recover the existing reference rather than choose a replacement scale.

## Problem and user stories

Frozen R1 sources exist, but broken external-checkout links and changed current feedback repeatedly prevent host cycles from scoring. Recovery needs a durable host-owned destination and verifiable provenance.

- As an enrolled maintainer, I want a cycle to recover the exact frozen reference so that relocated or offline clones can continue rating.
- As a reviewer, I want retained source identities and historical missing values so that recovery does not rewrite the study.

## Core requirements

- Recover the original report, diff review and historical feedback by recorded identity; verify every source hash before using it. Distinguish broken paths, unavailable sources and changed content.
- Retain exact source bytes and a portable provenance manifest inside the host project, outside installed Railspike. Recoverable local history is sufficient; never reset a checkout or overwrite current feedback to retrieve historical content.
- Restore usable ledger navigation and record recovery as a new event. Preserve R1, original scope/score histories and missing checkpoints; a recovered source enables new dated ratings, not fabricated historical projections.
- Give reusable product guidance for recovery, verification, offline reuse, failure and an explicitly accepted versioned replacement when exact recovery is impossible.
- Keep the requested [retrospective guesses](../../research/effort_estimation/2026-10-23-retrospective-guesses.md) separate from observed checkpoints, measured effort and acceptance. They are already delivered as independently authorized research administration.

## Delivery scope and completion boundary

**Documentation-only.** Product files: `../railspike/RAILSPIKE.md` and `../railspike/docs/effort-estimation.md`. Development files: this cycle's plans/debug/summary, `docs/plans/README.md`, collection index and cycle-specific verification records under `docs/research/effort_estimation/`. Host files: only `docs/plans/effort_estimation_trial.md` and retained reference documents/provenance under `docs/research/effort_estimation/references/R1/` in main v3, six `agent/v3-*` clones and `v3-test-kris`.

The audience is agents and maintainers resuming enrolled cycles. Complete when the reusable procedure and host records recover all three exact sources, a relocated isolated copy verifies them without the original checkout, and missing/mismatched-source walkthroughs give a concrete retry or stop. Retain unrelated local work. Application/runtime changes, tooling features, study re-rating, per-option estimates, synchronization, pushes and releases are outside implementation scope. Allowed JSON manifests are documentation/provenance records, not application configuration.

**Known environment:** affected local v3 clones enter through their normal effort checkpoint and host ledger. Today links fail or current feedback differs. After recovery, follow the ledger's host-owned references, verify hashes and resume a new dated rating. If verification fails, retain the prior record and report the source needing recovery; another clone's pass is insufficient. Check all eight destinations separately.

## Risks and shared components

- **Wrong reference:** silently changes R1. Earliest validation: compare all three frozen hashes; mitigation: exact historical reads and retained bytes, never edited reference text.
- **Concurrent host edits:** can lose another cycle's ledger work. Earliest validation: inspect each target's current content/state; mitigation: narrow patches, content rechecks and no bulk replacement or automatic stashing.
- **Recovery mistaken for backfill:** contaminates prospective analysis. Earliest validation: review original gaps and supplement labels; mitigation: append recovery events and separate current ratings from historical missing values.

Reuse the root activation/recovery contract, bundled R1/template, host ledger and Git's historical source reader. No UI/API or new scoring scale. The recovery manifest records original source identity and destination without embedding machine-specific host paths in reusable instructions.

## Flow and success criteria

1. Resolve study, reference version and expected source identities from the host ledger.
2. Recover and verify exact sources into the host's retained reference location; append provenance and repair navigation.
3. Resume rating from the current checkpoint; verify integrity and offline/relocated recovery, while retaining earlier missing records.

All three hashes must match in every targeted host; current feedback, original numeric histories and unrelated edits remain intact. Product links, Git-workflow fixture, local manifest/navigation checks and whitespace checks pass. Application/UI/deployment and release checks are inapplicable to this documentation change; no new release is claimed.

## Effort snapshots and authorization

Recorded 2026-10-23T15:38:30Z; R1/P2, scope v1; starting development revision `557f9a0a178a4661e5c3de1c839df9ff33330c3b`, product `b6c399424f75dc2e94af496411467480487cc319`. Codex, single exposed rater; prior clone review, source recovery checks, instructions and inherited scores already inspected. Intake total **0.65**; Step 2 **0.65 reaffirmed** for documentation, eight host recoveries and verification, excluding the separately completed retrospective-guess supplement. This is a disclosed post-inspection projection, not pristine intake or measured labor. All three exact R1 sources have been read and hash-verified.

Request: fix reference recovery / disposition: scoped documentation recovery cycle / authorization: user requested the fix; Step 2/3 workflow approvals still pending under the release policy / outcome: scope prepared, product and host implementation not begun.

Request: guess missing study values / disposition: separately labeled retrospective research supplement / authorization: explicitly requested / outcome: 23 scope-level guesses for 13 cycles, with original gaps preserved; no acceptance or measured-time values inferred.

Await **Approved Step 2** before the development plan.

### 2026-10-23 direct maintenance authorization

After the approval request and explanation of frozen R1 sources, the user instructed: “Please fix what you can.” Treat this renewed direct request as authorization to carry out the narrow source-recovery maintenance in this scope without another approval round trip. No literal Step 2/3 approval is claimed. Preserve the earlier authorization history, feature-branch isolation, planning/stage commit cadence and release boundaries; no publishing or unrelated workflow redesign is authorized.
