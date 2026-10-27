> **Feature plan:** [Step 2](./estimate_presentation_step2_feature_description.md) · [Step 3](./estimate_presentation_step3_development_plan.md) · [Step 4](./estimate_presentation_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/estimate_presentation`; standing R1/P2 enrollment; [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.25**

## Problem and user story

Estimates embedded in dense bullets are hard to find. As a plan reviewer, I want each option/stage estimate on its own prominent line so I can scan values immediately. The user reviewed the presentation in `~/agent/v3-kiro/docs/plans/viewer_tag_read_model_and_memoization/` and approved the version without approximation signs.

## Core requirements

- Put a standalone bold `Estimate: 0.35` line directly beneath each estimated option/stage heading, with an optional short comment. Put a distinct `Cycle estimate: 0.25` line near the top of each applicable artifact. Use plain numbers without approximation signs.
- Keep drivers, uncertainty and study metadata separate from the prominent value. Preserve meaningful ranges, unavailable reasons and explicit original/revised/retrospective labels; presentation must not imply precision or change scoring semantics.
- In estimate comparison/history tables, use a dedicated estimate column. Preserve original scores/scopes and append-only histories; do not fabricate or re-rate historical values to reformat them.
- Update canonical guidance, examples and applicable step templates consistently; disabled mode continues to omit estimate-only fields. Publish the next unused beta, currently `v0.3.0-beta.3`, with verified annotated tag and pre-release status.

## Delivery scope and completion boundary

Documentation-only product change plus authorized beta publication. Allowed product files: `../railspike/RAILSPIKE.md`, `README.md`, `docs/effort-estimation.md`, and estimation-related text/templates in `docs/workflow/*.md`. Reuse these canonical surfaces; no UI/API, runtime, tooling or dependency changes.

Allowed development records: this cycle's plans/log/summary, plan-index entry, collection ledger, cycle verification, and beta-3 notes/publication evidence under `docs/maintainers/releases/` and `docs/research/effort_estimation/`. No further v3 plan edits, host upgrades, frozen-source edits or merges.

Flow: agent reads guidance → drafts option/stage with prominent value → reviewer scans estimates → later revisions retain labeled history. Complete when examples match the approved preview, product/development links, Markdown/whitespace, file-scope review and existing Git-workflow checks pass, linked public evidence is published, and the exact tag/release body/pre-release status and unchanged stable Latest/default main are verified. Consumers deliberately update or restore their prior tag through existing guidance. Static checks establish consistency, not live-agent compliance or forecast accuracy; runtime/UI/deployment checks are inapplicable.

## Risks and success criteria

- **Ambiguous values:** a bare number could blur stage/cycle or retrospective meanings. Check cycle, option, stage, revision and unavailable examples before implementation; retain explicit context labels and separate metadata.
- **Documentation drift:** old templates could still bury estimates. Inspect all estimation instructions; ensure each applicable option/stage example has a prominent standalone value or a dedicated table column.
- **Publication errors:** recheck remote tags and exact commit before tagging; verify the annotated object and release readback. Preserve beta 2 and stable Latest; never reuse a published tag.

## Request and study history

User approved the preview and requested: “Please patch railspike and release a new beta.” Disposition: implement the reviewed presentation as reusable guidance and publish beta 3 after required planning gates. Step 1 skipped because the presentation is already chosen. Related predecessor: [default estimates](../extended_estimates_default/extended_estimates_default_step4_implementation_summary.md).

2026-10-25T00:31:47Z — Step 2 snapshot, scope v1, R1/P2; product start `14981be1a2b8944c481740cf683a96712e5c44f0`, development start `f53231833667fcb5bfeb431a24b3201633c9ab61`. All three frozen source hashes verified. Codex, single exposed rater, exact model identity unverified; exposure includes prior beta work and the reviewed v3 formatting preview. Intake before inspection was not captured and remains missing. Whole-cycle projection **0.25**, plausible 0.15–0.40, covering planning, coordinated instruction edits, checks and publication; uncertainty is template coverage and remote release work. Relative judgment, not measured labor; maintainer fit/acceptance pending.

Implementation/publication requested; Step 2/3 planning approvals remain pending. Await **Approved Step 2**. Publication authorization persists.

## Scope v2 and one-shot authorization — 2026-10-25

The user accepted combining the reviewed estimate presentation and agent signatures in one one-shot beta, then requested model name and settings when possible. This supersedes the pending staged-approval handoff above for this cycle only; publication remains authorized. Keep the prior v1 scope/score as history.

Additional requirement: agents sign beneath their authored/revised plan work with name and UTC date; include model name and relevant settings only when verified for that contribution. Omit unknown fields, preserve prior attribution and label revisions; do not guess runtime identity or treat a textual signature as cryptographic approval. Apply independently of estimate/debug mode across Steps 1–4. Scope now includes attribution-related sections/templates in the same product documentation files; no runtime/tooling or external-host changes. Validate known/unknown metadata, multi-author revisions and disabled estimate mode.

**Cycle estimate: 0.30**

2026-10-25T00:50:25Z — v2 projection, R1/P2, same start revisions and exposed rater. All R1 hashes reverified. Prior 0.25 retained; increase reflects attribution/template coverage, plausible 0.20–0.45. Exact model/settings unavailable for attribution; no new independent rating claimed. Maintainer acceptance pending.

*— Revised by Codex · 2026-10-25 UTC*
