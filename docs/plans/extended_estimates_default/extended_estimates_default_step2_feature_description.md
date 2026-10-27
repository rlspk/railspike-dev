> **Feature plan:** [Step 2](./extended_estimates_default_step2_feature_description.md) · [Step 3](./extended_estimates_default_step3_development_plan.md) · [Step 4](./extended_estimates_default_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/extended_estimates_default`; standing R1/P2 enrollment; [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled (user's default-on request applied to this new cycle).

## Problem and user stories

Extended estimates currently require a separate opt-in after study enrollment. As a maintainer, I want option and stage estimates included by default so that planning consistently exposes their relative work without another activation request.

## Core requirements

- Enable extended estimates by default for new enrolled effort-study cycles. Study enrollment itself remains optional; debug mode stays independent.
- Preserve explicit user overrides, recorded cycle state, and host policy ahead of the new fallback default. Preserve existing disabled cycles; for older cycles with no recorded state, recover the prior behavior without inventing historical estimates. Explain how to enable them prospectively.
- Retain existing option/stage semantics, uncertainty, independent cycle totals, immutable originals and append-only revisions; keep frozen R1 unchanged.
- Publish `v0.3.0-beta.2` from a verified non-default product branch as a GitHub pre-release, with an annotated tag, migration notes, evidence boundary and beta exit criterion. Preserve stable Latest and default installation behavior.

## Delivery scope and completion boundary

**Documentation-only product change with explicitly authorized beta publication.** Allowed product files: `../railspike/RAILSPIKE.md`, `README.md`, `docs/effort-estimation.md`, and estimation-related text in `docs/workflow/*.md`. Reuse their canonical activation/recovery contracts; no UI/API surfaces or application/runtime changes.

Allowed development files: this cycle's separate plans, debug log and summary; its entry in `docs/plans/README.md`; `docs/research/effort_estimation/collection.md`; cycle-specific verification records and beta-2 release notes/publication evidence in `docs/research/effort_estimation/` and `docs/maintainers/releases/`. No frozen-source changes, host-clone upgrades, merges or tooling changes.

Flow: start an enrolled cycle → inherit default-on estimates → retain option/stage history → explicitly disable if desired. Existing consumers deliberately update to the beta tag and may roll back to their previous tag. Complete when documentation and activation/recovery scenarios pass, product links/examples/Markdown and existing workflow checks pass, and the exact reviewed commit/tag and published pre-release are verified. Publish any linked development evidence first. Documentation checks do not establish predictive accuracy or live-agent compliance; those remain beta evaluation limits.

## Risks and success criteria

- **Accidental enrollment or reset:** validate new, unselected, host-disabled, explicitly disabled and resumed cycles; use explicit precedence and distinguish a new-cycle default from historical state.
- **Inconsistent activation text:** inspect README, root contract, guide and step instructions before implementation; require consistent scenario outcomes across all surfaces.
- **Wrong publication target:** remote tags confirm beta 1 at `c336536f88d1ce471b4f582a7d87203864f8526e`; recheck beta-2 availability before tagging, verify annotated object and exact commit, and read back pre-release/Latest state. Never reuse a published tag.

## Request, study history and authorization

Request: “Please make it on by default, and release to beta2 of the current beta release.” Disposition: new follow-up to [detailed effort estimates](../detailed_effort_estimates/detailed_effort_estimates_step4_implementation_summary.md), scoped above. Implementation and publication requested; required staged planning approvals remain pending. Step 1 skipped because the requested direction is concrete.

Scope v1; product start `c336536f88d1ce471b4f582a7d87203864f8526e`; development start `eae2f767160887f4fd7ce402b5cd6e51b168b2d1`. R1/P2, Codex single rater; exact model identity unverified. All three frozen source hashes verified. Prior exposure: prior cycle documents, source instructions, release policy and remote tags. Intake before inspection was not captured and remains missing.

- 2026-10-24T23:14:54Z — Step 2 projected whole-cycle work **0.35**, plausible 0.25–0.50, including planning, coordinated documentation, scenario checks, release preparation/publication and ordinary correction. Main uncertainty: migration wording and publication verification. This is a relative judgment, not measured labor. Maintainer fit/acceptance pending.

Await **Approved Step 2** before drafting Step 3. Publication authorization persists through the planning gates.

### Approval received

2026-10-24 UTC: user replied “Approved Step 2.” Scope v1 approved unchanged; Step 3 drafting authorized. Implementation awaits Step 3 approval; publication authorization remains recorded above.
