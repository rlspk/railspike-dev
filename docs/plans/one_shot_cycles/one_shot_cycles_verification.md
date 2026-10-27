# One-shot cycle verification

Date: 2026-10-27 UTC. Product reviewed: `3e79249400b99efc60741972c42b81d55d4e53c3`, compared with `f8c8d2588a4a849a12acc7c425d99f533e218f8d`. Development evidence belongs to `railspike/one_shot_cycles`, R1/P2 scope v1.

## Evidence boundary

These are manual document scenarios and local integrity/regression checks. They establish consistent written instructions and preserved update behavior, not agent compliance, trusted approval storage, or runtime enforcement. Kiro Web and CLI sessions were not run. The accepted outcome is actionable guidance for those environments, not a claim that either runtime now enforces it.

## Scenario review

Each row was traced against the final product clauses. **Pass** means the written next action and evidence requirement match the approved contract.

| Scenario/input | Required next action and retained evidence | Source in product | Result |
| --- | --- | --- | --- |
| Kiro ignores applicable AGENTS.md | Read applicable instructions before work; if required files cannot be read/found, resolve before dependent action. No assertion that prose forces delivery. | RAILSPIKE mode selection; one-shot Entry 1 | Pass, manual guidance; Web/CLI unverified |
| User references a Step 1 plan | Reference supplies no implementation or step approval; retain current authority. | RAILSPIKE mode selection; one-shot Entry 2–3 | Pass, manual guidance; Web/CLI unverified |
| User asks about implementation before authorization | Answer the question, do not implement on that basis; clarify actual scope/authority if needed. | one-shot Entry 2; Execution and evidence | Pass, manual guidance; Web/CLI unverified |
| User asks during authorized execution | Answer without expanding or automatically revoking existing authority. | one-shot Execution and evidence | Pass |
| Explicit bounded one-shot request | Record request, actual authority, scope, approach/checks before implementation, establish branch, proceed without redundant approval. | one-shot Entry 1–5 | Pass |
| Mode requested but execution boundary ambiguous | Resolve dependent ambiguity; agent-written scope is not user approval. | mode selection; one-shot Entry 2 and Execution | Pass |
| Ordinary small task | No automatic mode or study selection; existing staged work remains subject to its gates. | mode selection; README one-shot section; WELCOME | Pass |
| Successful one-shot | Deliver outcome, record actual verification/recovery, then completion commit or explicit uncommitted status. | one-shot Commits and closeout | Pass |
| User says leave uncommitted | Do not commit changes, logs, or reference updates; report status. | one-shot Study/debug and Commits | Pass |
| Interrupted session with recoverable record | Restore identity, mode, scope, authority, branch, pending requests, checks, study/debug; compare working tree without discarding unknown changes. | one-shot Resumption | Pass |
| Interrupted session with missing authority | Preserve work, identify missing evidence, stop dependent implementation until clarified. | one-shot Resumption; failure modes | Pass |
| In-scope correction versus new capability | Record classification, preserve originals; new scope requires actual renewed authority before implementation. | one-shot Execution; shared Enhancement Requests | Pass |
| Scope expands but remains bounded | Append new scope and user authorization; retain original score/scope and re-estimate when warranted. | one-shot Resumption; effort checkpoints | Pass |
| Transition to staged review | Link retained one-shot record and new plans; same cycle identity and history, fresh staged approvals, unmerged branch continuation, planning-only commit excludes previous implementation. | one-shot Resumption; Step 4 Before gate; central Commit discipline | Pass |
| Separate additional cycle | Distinct identity/authority and predecessor link; host counting rules apply to related splits. | one-shot Resumption; effort checkpoints | Pass |
| Failed, paused or abandoned work | Retain outcome and unresolved work; retrospective unavailable when evidence is insufficient, never zero by default. | one-shot Execution/Resumption; effort closeout | Pass |
| Required check unavailable | Mark blocked/pending/omitted honestly; no full-pass or technical completion claim while required work remains. | one-shot Execution and closeout; failure modes | Pass |
| Unrelated dirty files or destination collision | Preserve local changes; inspect and resolve collisions, do not overwrite. | one-shot Entry 1/4; Resumption; Commits | Pass |
| Follow-up branch reuse | Explicit request and unmerged eligibility; new cycle/record; no inherited approval or automatic publication. | one-shot Entry 5; central Follow-up Cycles | Pass |
| Documentation-only authority | Identify allowed documentation paths and reader outcome; runtime changes are excluded. | one-shot Entry documentation paragraph | Pass |
| Completion commit reference | Pending before creation; confirm afterward, next authorized update or bounded record-only handoff, no amendment or infinite self-reference. | one-shot Commits | Pass |
| Product/development split | Separate commits and host record linked to paired implementation revisions. | one-shot Commits | Pass |
| Publication not requested | Report separate commit/merge/publication states; no publication implied. | one-shot Commits; README | Pass |

## Study and diagnostic combinations

| Enrollment | Debug | Expected behavior | Result |
| --- | --- | --- | --- |
| Enrolled | Enabled | Intake/entry/revisions/closeout in record and host ledger; separate full diagnostic log and one concise handoff link | Pass, source review |
| Enrolled | Disabled | Same study collection, no diagnostics/link; preserve existing logs | Pass, source review |
| Unselected | Enabled | No scores/ledger entry; enabled diagnostic lifecycle applies | Pass, source review |
| Unselected | Disabled | No study fields or diagnostics; core evidence still required | Pass, source review |

Resumption preserves recorded state and resolves explicit overrides under shared precedence; a new marker lookup cannot overwrite uncertain resumed debug state. Standing study enrollment includes supported one-shot cycles. Missing historical intake stays missing; unused staged checkpoints are inapplicable. Actual alternatives/work units alone receive extended estimates; cycle totals are independent and non-additive. Transition records and clones are not additional outcomes. All traced to the one-shot Study/debug section and effort guide's One-shot checkpoints.

## Evidence parity review

| Staged evidence | Consolidated record equivalent | Result |
| --- | --- | --- |
| Original query and intent | Original request; bounded outcome | Pass |
| Requirements, exclusions and completion contract | Authorization, work type, allowed boundary, outcome and verification/recovery plan | Pass |
| Approach, dependencies and risks | Proportionate approach/shared components/mitigations; material uncertainty returns to planning | Pass |
| Planning approvals | Actual user instruction/evidence with scope/date; no fabricated Step N approvals | Pass |
| Implementation summary | Dated execution decisions/discoveries/changes; corrections versus additions | Pass |
| Enhancement dispositions | Request, reason, authority, outcome/follow-up | Pass |
| Verification and omissions | Commands/results, evidence/environment limits and next action | Pass |
| Branch, revision and delivery status | Starting revisions/branch, implementation references, separate technical/commit/publication status | Pass |
| Study, diagnostics and authorship | Same policies, mode-specific checkpoints, retained log and verified-only attribution | Pass |
| Interrupted/superseded work | Recovery state, linked history and original identity/scope preserved | Pass |

## Executed checks

- `python3 scripts/check-markdown-links.py ../railspike`: passed, 16 Markdown files, including final Stage 4 corrections.
- `python3 scripts/check-markdown-links.py . docs/maintainers/historical-link-baseline.txt`: passed before adding this report, 182 Markdown files; 80 explicitly acknowledged historical targets. Final development readback is recorded in the summary.
- `bash scripts/check-railspike-git-workflow.sh ../railspike`: passed; disposable local fixture covers the existing README update behavior. README update command block is byte-identical to the starting product revision.
- `git diff --check` in both repositories: passed. Product diff scope from start to final revision: exactly eight approved documentation files; no runtime, script, test, CI or deployment changes.
- Local cycle navigation/path checks: passed after moving plans and adding the implementation summary. All frozen R1 source hashes verified at entry; references unchanged.
- Product stages each have a separate commit; development planning commit precedes the summary and each stage has its own record commit. Final development commit is identified at handoff rather than self-embedded.

## Corrections and omissions

Stage 4 review corrected two documentation inconsistencies: the template's cycle estimate now uses the required bold presentation, and the staged branch gate explicitly recognizes same-cycle continuation from one-shot execution. Both are corrections within approved v1 scope; no new feature request or estimate revision.

Live Kiro runs, automatic instruction delivery, trusted approval verification, and tool interception were not performed or claimed. Runtime/UI/deployment/migration/release checks are inapplicable. This work does not publish a release, upgrade a consuming project, backfill historical cycles, or change frozen references.

*— Codex · 2026-10-27 UTC*
