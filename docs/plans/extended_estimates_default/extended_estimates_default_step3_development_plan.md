> **Feature plan:** [Step 2](./extended_estimates_default_step2_feature_description.md) · [Step 3](./extended_estimates_default_step3_development_plan.md) · [Step 4](./extended_estimates_default_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/extended_estimates_default`; standing R1/P2 enrollment; [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

## Completion Contract

Deliver approved [Step 2](./extended_estimates_default_step2_feature_description.md) scope v1: new enrolled cycles default to option/stage estimates, explicit opt-outs and existing state survive, and `v0.3.0-beta.2` is published from the verified non-default product branch. Allowed product documentation: `RAILSPIKE.md`, `README.md`, `docs/effort-estimation.md`, estimation sections in `docs/workflow/*.md`. Allowed development records: this cycle's plans/log/summary, plan-index entry, collection ledger, cycle verification and beta-2 release records. Preserve frozen sources and histories; no application, tooling, CI, host upgrades or merges. Recovery: explicit mode changes apply prospectively; consumers can restore their prior installed tag. Evidence covers documentation and fixtures, not predictive accuracy or live-agent compliance. Runtime/UI/deployment checks are inapplicable; GitHub publication verification is required.

## Key Risks

- **High risk:** resetting existing settings or enrolling users unintentionally. Validate precedence and legacy cases before release; apply the fallback only to new enrolled cycles.
- Conflicting guidance: check all canonical estimation surfaces together and resolve contradictions before publication.
- **High risk:** wrong tag or stable publication. Recheck remote availability, exact reviewed commit and annotated tag; publish as pre-release with Latest unchanged and inspect remote state before any retry.

## Stage 1

- Goal: consistent default-on activation and migration guidance.
- Dependencies: Step 3 approval; new feature branches in both checkouts; organize this cycle and commit approved plans before creating the summary or implementing.
- Expected changes: update canonical default/recovery wording and affected step guidance; preserve existing scoring semantics; record scenario evidence and ledger state.
- Verification approach: scenarios for new enrolled/unselected cycles, explicit user override, host opt-out, recorded enabled/disabled state, older missing-state cycles, conflicting evidence and late activation without backfill. Run product/development link checks, existing Git-workflow fixture, whitespace and allowed-file review. Owns shared documentation/scenario checks.
- Stage work estimate: S1 v1 **0.15**, plausible 0.10–0.25; driver: coordinated activation wording; uncertainty: legacy-state clarity.
- Risks or open questions: ambiguous legacy state could reset behavior; check cases early, retain established behavior and clarify genuinely unresolved evidence before dependent estimates.
- Canonical components/API contracts touched: root activation contract, effort guide, README and estimation-related workflow references; no application APIs.

## Stage 2

- Goal: publish and verify beta 2 with reviewable evidence and recovery instructions.
- Dependencies: Stage 1 checks, summary and paired product/development commits complete.
- Expected changes: release notes, verification/publication records, summary/ledger closeout; publish reviewed product branch and linked development evidence, then unused annotated tag and GitHub pre-release. Record unsigned status unless a signing identity is established.
- Verification approach: verify clean exact candidate, tag object/peeled commit and remote identity; run installation/migration fixture against published candidate for update/rollback claims; check release-note links and whitespace. Read back release tag, body, pre-release status and unchanged stable Latest/default branch. Record stage commits without amending history.
- Stage work estimate: S2 v1 **0.10**, plausible 0.05–0.20; driver: existing release process; uncertainty: remote publication/recovery. Owns release-specific checks; repeat Stage 1 checks only if candidate changes.
- Risks or open questions: interrupted publication may leave partial state; inspect tag/release before retry, never move a published tag, and report an external blocker without claiming completion.
- Canonical components/API contracts touched: release policy, existing installation guidance, Git annotated tags and GitHub Releases; default installation remains main.

## Study history and approval

2026-10-24 UTC — Step 3 snapshot: scope v1, starting revisions and R1/P2 inherited from Step 2; all three frozen hashes reverified. Codex, single exposed rater, model identity unverified; additional exposure includes planning instructions and beta-1 release notes. Whole-cycle projection **0.35 reaffirmed**, plausible 0.25–0.50, independently judged including planning and publication. S1/S2 above are original whole-stage judgments recorded at this checkpoint, not additive totals or measured labor; preserve them through revisions and separate retrospectives. Intake remains missing; maintainer acceptance pending.

Step 2 approved; no new scope requests. Await **Approved Step 3**. Keep planning documents uncommitted until then; publication authorization is already present.

### Approval received

2026-10-24 UTC: user replied “Approved Step 3.” Implementation and the previously authorized beta-2 publication may proceed.
