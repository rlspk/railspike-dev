> **Feature plan:** [Step 1](./approved_plan_commits_step1_solution_assessment.md) · [Step 2](./approved_plan_commits_step2_feature_description.md) · [Step 3](./approved_plan_commits_step3_development_plan.md) · [Step 4](./approved_plan_commits_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/approved_plan_commits`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.50**

## Entry and authority

2026-11-04T22:52:03.774870+00:00 — Steps 1–3 explicitly approved; R1/P2 scope v1 Option A. Codex, single exposed rater; model/settings unavailable. Entry projection **0.50 reaffirmed**; original stage work S1 0.20 / S2 0.15 / S3 0.10 retained, not additive or hours. Intake remains missing; all three frozen R1 hashes verified. Start: dev `4c64dd52b354807842e611c0b3c67be84aa2c94f`, product `5d54e065fa5f9f6e2555977034b5073456dd104c`. New branch `feat/approved-plan-commits` in both checkouts; planning commit `2b1c24c` inspected: approved Steps 1–3, existing debug log and plan-index entry only. Ledger and this summary excluded. This cycle uses the old late-planning-commit rule and does not invent earlier approval commits.

Documentation-only within Step 2/3 allowed paths. Product scripts/tests/runtime, CI, website and release publication excluded. Live agent compliance unverified; maintainer fit and study acceptance pending. Unrelated todo.txt edits and the work checklist remain untouched. No new enhancement requests.

*— Codex · 2026-11-04 UTC*

## Stage 1 - Shared approval commit gate

**Original estimate: 0.20**

**Retrospective stage work: 0.20**

- Changes: added the shared approval commit gate; moved branch/folder setup to first approval; bounded checkpoint log/ledger contents; defined revisions, failures, explicit waivers, older-cycle recovery and split-repository behavior. Step 4 verifies planning history without duplicate commits. Product commit `2fea4193de3a5ae9bcfcc1c8b89a6b56c176777e`.
- Verification: product links passed (18 files), product whitespace passed; diff limited to RAILSPIKE.md. Manual contract review passed: ordinary 1/2/3 approvals yield three commits, skipped Step 1 yields two; revisions require renewed approval/new commit; failure blocks advancement; explicit no-commit preserves authority/branch/plan; older cycles disclose missing history and commit only current approved content. Follow-ups require fresh approvals and eligible branch reuse. Staged-content rule explicitly excludes unapproved plans and unrelated shared-ledger hunks.
- Notes: consumer step instructions still carry old rules until Stage 2; this intermediate product commit is not a completed release. Live adherence unverified. No scope or estimate revisions; retrospective judged separately, not measured labor.

*— Codex · 2026-11-04 UTC*

## Stage 2 - Step handoffs and recovery guidance

**Original estimate: 0.15**

**Retrospective stage work: 0.15**

- Changes: connected Step 1/2 approval handoffs and Step 2/3 resumption to the gate; Step 4 now verifies existing planning commits and permits disclosed recovery/waivers. Reconciled README, welcome/host proposal, failure guide, one-shot transition and effort snapshot references. Kept the historical Step 4 gate anchor so existing links remain valid. Product commit `3cd8580569cc6665bcdd21ca2e85422182a724e0`.
- Verification: product links passed (18 files); README Git-workflow fixture passed; product whitespace passed. Scan found three stale README passages and one snapshot reference; corrected them and reran checks. No remaining late-organization/duplicate-Step-4/minimum-four-commit instructions found in live product Markdown. Manual entry review covers approved Step 1 then verified commit before Step 2; approved Step 2 before Step 3; approved Step 3 before summary; split repository host plan commits and product branch before implementation. One-shot transition retains prior record/implementation, saves each new approved staged plan and avoids duplicate planning commits.
- Notes: only approved documentation paths changed; installation/update block and all checkers unchanged. Earlier stage dev commit `c1673e1`; Stage 1 product `2fea419`. No scope/estimate revision; self-review and fixture passes do not establish live agent compliance.

*— Codex · 2026-11-04 UTC*

## Stage 3 - Concepts and final verification

**Original estimate: 0.10**

**Retrospective stage work: 0.10**

- Changes: updated Planning record and Approval and scope boundary in `docs/concepts/planning.md`; recorded final scenario review and append-only study closeout. Stage 2 dev commit `1e9922d`; final product revision `3cd8580`.
- Verification: product Markdown links passed (18 files), unchanged README Git-workflow fixture passed, touched concept links passed (3 files), cycle links passed (5 files). Working-tree and full change-range whitespace checks passed in both repositories. Allowed-path review passed: 14 product documentation files; dev changes limited to this cycle, plan index, touched concept file and study ledger. No product scripts, tests, installation commands, runtime, CI or website changes.
- Notes: no product change in Stage 3. Runtime/UI/deployment/migration/publication checks are inapplicable to this documentation-only outcome. Live agent adherence remains unverified.

### Final scenario review

Manual instruction tracing, by the implementing agent; these are coverage checks, not live behavioral experiments.

| Case | Expected sequence and inspected source | Result |
| --- | --- | --- |
| Ordinary Steps 1–3 | Step 1 handoff → shared gate creates host branch/folder and commits approved Step 1 → Step 2; Step 2 handoff/Step 3 Before verify Step 2 commit; Step 3 After saves approved Step 3 before Step 4 setup. | Passed |
| Skipped Step 1 | Step 2 starts as an uncommitted top-level draft; approval creates branch/folder and commits Step 2; Step 3 follows in that folder. Step 2 guidance and shared organization rule agree. | Passed |
| Unapproved artifacts and shared ledger | Shared gate excludes later drafts, substantive unapproved revisions, implementation and concept edits. Only authorized checkpoint ledger hunks and the cycle's existing log enter the approval commit. | Passed |
| Renewed approval | Shared gate keeps substantive revisions uncommitted until approved, then creates a new commit before dependent work without amending history or approving later steps. | Passed |
| Failed commit | Shared gate and failure guide stop dependent progression; repair and verify the commit, or obtain an explicit waiver. Attempted commits are insufficient. | Passed |
| Explicit no-commit | Shared gate retains branch, written plans, actual approvals and recorded override; Step 4 retains verification/summary requirements and discloses waived commits. | Passed |
| Older or interrupted cycle | Shared recovery and Step 4 Before inspect approved content/history, reuse valid commits, save missing current approved plans, and disclose omissions without fabricating approval commits. | Passed |
| Branch reuse | Shared follow-up rules require an unmerged branch, explicit reuse request, fresh cycle identity/approvals and cycle-specific commits. Merged branches remain ineligible. | Passed |
| Separate repositories | Shared gate saves plans in host; Step 4 Before establishes product branch before product edits. No empty product planning commit. Stage summaries record paired product commits. | Passed |
| One-shot transition | One-shot recovery retains record, authority and existing implementation; each new staged approval follows the shared gate. Normal one-shot plan/implementation sequence stays unchanged. | Passed |
| Folder conflict or future navigation | Shared organization/failure guidance stops collisions and substantive changes; missing future-step links are reported pending rather than creating unapproved artifacts. Existing links pass after summary creation. | Passed |

## Closeout

**Retrospective cycle scope: 0.50**

2026-11-04T22:54:56.771771+00:00 — R1/P2 v1; Codex, single exposed rater, model/settings unavailable. Original and entry projection **0.50** retained; separately judged retrospective scope **0.50**, not measured labor. Three planned stages, three completed. Original/retrospective stage work S1 **0.20/0.20**, S2 **0.15/0.15**, S3 **0.10/0.10** retained. Intake remains missing. Starts: product `5d54e065fa5f9f6e2555977034b5073456dd104c`, dev `4c64dd52b354807842e611c0b3c67be84aa2c94f`. Planning commit `2b1c24c`; product stages `2fea419`, `3cd8580`; dev stages `c1673e1`, `1e9922d`, and this Stage 3 commit (recorded in final debug handoff after creation). No new scope, splits or added requests; corrections were stale README rules and the shared snapshot wording found during Stage 2. Maintainer comfortable-fit and study acceptance pending.

Documentation implementation and required verification complete on `feat/approved-plan-commits` in both repositories; unmerged and unpublished. Live behavior unverified. Existing todo.txt edits and untracked work checklist preserved. No earlier approval commits were fabricated for this cycle, which began under the previous contract.

*— Codex · 2026-11-04 UTC*

## Release follow-up — scope v2

2026-11-05T00:34:48.779126+00:00 — User requested “please mint beta.2.” Release preparation is authorized; exact-version confirmation is pending. No main merge or host upgrade requested. Product candidate `3cd8580569cc6665bcdd21ca2e85422182a724e0` on `feat/approved-plan-commits`; dev follow-up start `2fa28080c2bebf67c65acdfb9a07649ccf0ffc49`.

R1/P2, all three frozen hashes verified; Codex, single exposed rater, model/settings unavailable. Follow-up intake missing: candidate/status/release inspection preceded this snapshot. Original v1 projection/retrospective **0.50** retained. V2 whole-cycle projection **0.55**, including release checks, notes and publication; scope judgment, not hours or a stage sum. New scope is release work only: notes/evidence, appended summary/debug/ledger records, and beta publication after exact-version confirmation. No product edits, main merge, host updates or unrelated changes.

Product links (18 files), unchanged Git-workflow fixture and change-range whitespace pass; clean product candidate and 14-file documentation diff verified. Published tags/releases checked: latest beta v0.6.1-beta.1. Proposed **v1.0.0-beta.2** is unused. Policy requires a major increment for changed branch/commit requirements; beta.2 preserves the user's requested suffix, without implying a published 1.0.0-beta.1. [Prepared notes](../../maintainers/releases/v0.6.1-beta.2.md) include migration, evidence limits and beta exit criteria. Live compliance remains unverified.

Status: release prepared; exact version awaits confirmation. No tag created or release published. Publication closeout, retrospective v2 scope, maintainer fit and study acceptance pending.

### Version correction and policy — scope v3

2026-11-05T05:36:53.337760+00:00 — User rejected the proposed v1.0.0-beta.2 and directed: “NEVER update the major version unless I specifically ask you. AVOID updating the minor version unless I specifically ask you. Only update the revision if there is a new functionality addition.” The earlier major-version proposal and automatic policy rationale above are superseded. No tag or release was created. Corrected prepared candidate: **v0.6.1-beta.2**, continuing the requested beta series; exact-version confirmation still pending. Renamed the draft notes and repaired their links, preserving the original proposal here as history.

User directly authorized the persistent version policy correction, added to AGENTS.md and docs/maintainers/RELEASES.md. This extends the release follow-up documentation scope (v3) to those two policy files; no product changes or publication authorized by this correction. R1/P2 whole-cycle projection **0.55 reaffirmed** for v3; original v1 0.50 and v2 0.55 histories retained. Rater Codex, single exposed; no retrospective release scope or maintainer acceptance claimed. Product candidate and previous verification unchanged.

### Release v3 closeout

2026-11-05T05:38:00.880044+00:00 — User explicitly confirmed **v0.6.1-beta.2** after the exact-version prompt. Pushed the product feature branch and unsigned annotated tag `48991d1e35dad0f1a2c6664dc87ac42079492fc0`, pointing to verified product `3cd8580569cc6665bcdd21ca2e85422182a724e0`. Published GitHub prerelease [v0.6.1-beta.2](https://github.com/rlspk/railspike/releases/tag/v0.6.1-beta.2); API readback confirms non-draft/prerelease and body identical to prepared notes. Remote main remains `5d54e065fa5f9f6e2555977034b5073456dd104c`; stable Latest remains v0.4.0. No main merge or host upgrade. Evidence: [publication record](../../maintainers/releases/v0.6.1-beta.2-publication.json).

R1/P2; Codex, single exposed rater, model/settings unavailable. V3 projection **0.55** preserved; retrospective whole-cycle scope **0.55**, a scope judgment rather than measured labor. Original v1 projection/retrospective **0.50**, v2 projection **0.55**, and rejected-version history retained. Release follow-up complete. Correction versus addition: user-directed persistent version-policy correction and release-note rename, no product changes. Live adherence, maintainer comfortable-fit and study acceptance pending. Unrelated todo.txt edits and untracked checklist preserved.
