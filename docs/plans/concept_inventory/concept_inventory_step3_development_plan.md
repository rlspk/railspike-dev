> **Feature plan:** [Step 2](./concept_inventory_step2_feature_description.md) · [Step 3](./concept_inventory_step3_development_plan.md) · [Step 4](./concept_inventory_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/concept_inventory`; [ledger](../../research/effort_estimation/collection.md). Extended estimates: enabled.

**Cycle estimate: 0.40**

## Completion Contract

- Step 2 approved explicitly in conversation; the preceding lazy-maintenance clarification reaffirms its scope. Step 1 was skipped. Step 3 approval is pending.
- Documentation-only: agents following Railspike maintain concise host `docs/concepts/` entries for touched concepts and list them in plans. No project sweep, full-inventory audit, flag, new approval gate, or architecture requirement.
- Allowed product files: `RAILSPIKE.md`, `docs/concepts.md`, `docs/README.md`, and `docs/workflow/*.md` in `../railspike`. Host scope: touched `docs/concepts/` entries, this cycle's records, plan index, and ledger entry. Application/runtime, tooling, website, merge, and publication changes are excluded.
- Complete when staged and one-shot instructions support planning through inventory update and verification. Correct document mismatches before handoff. Evidence is document checks and scenario walkthroughs; live agent compliance remains unverified. Runtime/deployment checks are inapplicable to this Markdown change.

## Key Risks

- Prompt growth: duplication obscures rules; review references in Stage 1 and keep definitions in one shared guide.
- Stale entries: proposed behavior could appear implemented; inspect a changed-concept scenario before finalization, labeling proposals and verifying only touched entries.
- Forced classification: weak boundaries could trigger unwanted surveys; check a no-concept maintenance case and permit “none” or explicit uncertainty.

## Concepts touched

Concept inventory — created; Planning record — changed; Approval/scope boundary — used unchanged. Inventory entries for these three will be added lazily in Stage 3, after the relevant instructions exist. No wider Railspike self-model.

## Stage 1

**Estimate: 0.12**

- Goal: complete the staged workflow's inventory lifecycle.
- Dependencies: Step 3 approval, new feature branches, and the approved planning-only commit with organization/reference repairs; ledger and inventory edits stay outside that initial commit.
- Expected changes: add compact shared guidance in product `docs/concepts.md`; link it from `RAILSPIKE.md` and `docs/README.md`. Add short references in Step 1, Step 2, Step 3 Do, and Step 4 Do/After for concepts-touched lists, proposed entry changes, coordinated updates, and touched-entry verification. Resolve inventory paths from the host, guidance paths from the installed product; allow one or several inventory files.
- Verification approach: walkthrough absent-inventory and changed-concept staged flows; check product links, diff whitespace, allowed paths, and guidance length; record evidence in this cycle's verification record.
- Risks or open questions: premature inventory creation or duplicate rules; inspect planning/implementation boundaries and keep behavior definitions solely in the shared guide.
- Canonical components/API contracts touched: shared workflow guidance and existing staged artifacts; no APIs.
- Estimate details: stage work, including its checks/records/corrections; driver: brief references across existing steps; uncertainty: wording consistency. Target: about one hour.

## Stage 2

**Estimate: 0.07**

- Goal: provide the same behavior in one-shot cycles.
- Dependencies: Stage 1 verified and committed with its summary.
- Expected changes: update `docs/workflow/one_shot.md` entry, execution/verification guidance, and compact record template to reference the shared guide and list concepts touched. Preserve bounded authorization and existing commit rules.
- Verification approach: walkthrough one-shot creation/update and work with no relevant concept; check links, whitespace, allowed paths, and agreement with staged guidance.
- Risks or open questions: inventory rules might imply extra permission or fabricated stages; compare with existing one-shot authority and lifecycle before committing.
- Canonical components/API contracts touched: one-shot record and shared inventory guidance; no APIs.
- Estimate details: stage work; driver: adapting an existing record; uncertainty: avoiding repeated guidance. Target: under one hour.

## Stage 3

**Estimate: 0.10**

- Goal: exercise lazy maintenance locally and finish verification.
- Dependencies: Stage 2 verified and committed with its summary.
- Expected changes: add concise host entries for the three listed concepts, with purposes, behavioral scenarios, and source paths; link them from this cycle's plans. Finalize scenario evidence, summary, study closeout, and ledger. Correct only in-scope document inconsistencies found by verification.
- Verification approach: verify these entries against product instructions; walkthrough an existing multi-file inventory and preservation of unrelated entries. Run `python scripts/check-markdown-links.py ../railspike`, `bash scripts/check-railspike-git-workflow.sh ../railspike`, host plan/inventory link checks, and `git diff --check` in both repositories; inspect allowed paths. This stage owns the final shared regression checks.
- Risks or open questions: walkthroughs cannot establish live compliance; report that limitation and retain unrelated files. No whole-project inventory scan.
- Canonical components/API contracts touched: host inventory, plan references, verification/summary and study ledger; no APIs.
- Estimate details: stage work; driver: source-backed entries and five required scenarios; uncertainty: pre-existing checker failures, which must be distinguished from regressions. Target: about one hour.

## Evidence and estimate history

- 2026-10-28T23:42:12Z — Step 3 handoff, v1: **0.40 reaffirmed**, single exposed Codex rater, R1/P2; all three R1 hashes reverified. Scope and starting revisions remain those in Step 2. Intake remains missing; Step 2's 0.40 is preserved. Stage figures cover only their stated work, checks, records, and ordinary corrections; the cycle projection includes inspection/planning and is independently judged, not a sum or time estimate.
- Commit each completed stage with its host summary before proceeding; pair product and development commits where both change. Preserve append-only scope/score history. At closeout record actual checks, omissions, revisions, and retrospective assessments; maintainer fit/acceptance stays pending unless supplied. No merge or release is authorized.

*— Codex · 2026-10-28 UTC*
