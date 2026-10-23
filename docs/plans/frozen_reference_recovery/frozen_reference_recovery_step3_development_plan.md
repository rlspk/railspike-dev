> **Feature plan:** [Step 2](./frozen_reference_recovery_step2_feature_description.md) · [Step 3](./frozen_reference_recovery_step3_development_plan.md) · [Step 4](./frozen_reference_recovery_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/frozen_reference_recovery`, standing R1/P2; [ledger](../../research/effort_estimation/collection.md).

## Completion Contract

Documentation-only, within Step 2's named files and eight host reference/ledger destinations. Agents follow their ordinary ledger to three exact R1 sources retained in their host, verify identities and continue from a new checkpoint without changing historical missing values. Product guidance covers relocation, changed current content and unrecoverable sources. Verify each host and an isolated relocated copy; no application/UI/deployment, installation upgrade or release is claimed. JSON manifests are provenance documentation only. The user's renewed “Please fix what you can” authorizes direct maintenance; no literal step-approval tokens are inferred.

## Key Risks

- **High risk: source/data integrity.** Wrong bytes change R1; verify all three hashes before writing, use exclusive creation and retain changed current feedback.
- **High risk: concurrent edits.** Replacing a ledger could discard active work; use guarded narrow edits and append recovery entries, preserving cycle sections. Skip and report conflicting destinations.
- **Interpretation.** Recovery may look like historical score backfill; keep original gaps, guessed supplement and new ratings separate.

## Stage 1

- Goal: make exact-source recovery explicit and locally reproducible.
- Dependencies: matching report, diff and historical-feedback hashes; feature branches and planning commit.
- Expected changes: retain a development-workspace reference set/manifest; extend the two named product documents with host-owned source recovery and failure guidance.
- Verification approach: source hashes, product links/Git fixture, documentation scope and whitespace.
- Risks or open questions: historical reads must never reset a checkout; validate exact Git object/path and keep copied Markdown bytes as text evidence rather than rewriting their relative links.
- Canonical components/API contracts touched: root activation/recovery contract, effort guide and host provenance manifest; no API.

## Stage 2

- Goal: repair actual ledger recovery in all eight known host checkouts.
- Dependencies: Stage 1 verified and committed.
- Expected changes: exact local reference copies/manifest and a current recovery notice/link table in each ledger, leaving historical source tables and cycle records intact.
- Verification approach: per-host hashes and ledger targets; original ledger minus the inserted recovery text must remain byte-identical; current feedback and pre-existing changes preserved.
- Risks or open questions: active ledgers may change; guarded update or skip, no automatic stash, branch movement or host commit.
- Canonical components/API contracts touched: existing study ledger and host-owned reference documents.

## Stage 3

- Goal: prove relocated/offline recovery and close out honestly.
- Dependencies: Stage 2 verified and committed.
- Expected changes: cycle verification record, collection closeout row and stage summary with pending maintainer acceptance.
- Verification approach: relocated-copy manifest/hash checks, missing/tampered-source detection, rerun idempotence, product/development links, Git-workflow fixture, whitespace and authorized-file review.
- Risks or open questions: a recovery pass is not predictive validation; no guessed checkpoint becomes prospective and no study outcome acceptance is inferred.
- Canonical components/API contracts touched: collection index and retained evidence.

## Study checkpoint

2026-10-23T17:43:04Z, scope v1/R1/P2, original development/product revisions and prior exposure unchanged. Codex, single exposed rater. Total **0.65 reaffirmed** for source recovery, product documentation and eight-host verification. Later user direction authorizes direct execution; earlier pending approval records remain historical. Runtime dependencies added: zero. Step 1 inapplicable; no historical estimate reconstructed.
