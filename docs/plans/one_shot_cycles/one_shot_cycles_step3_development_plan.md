> **Feature plan:** [Step 1](./one_shot_cycles_step1_solution_assessment.md) · [Step 2](./one_shot_cycles_step2_feature_description.md) · [Step 3](./one_shot_cycles_step3_development_plan.md) · Step 4 (pending)

Debug mode: enabled

Effort study: `railspike-effort / railspike/one_shot_cycles`; standing R1/P2 enrollment; [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.65**

## Completion Contract

- Deliver documentation for maintainers and agents to enter an explicitly authorized one-shot cycle, record intent before implementation, execute within scope, verify, and close out with comparable substantive evidence. Preserve records and authority on resumption, failure, abandonment, and transition to staged planning.
- Allowed product documentation: `RAILSPIKE.md`, `README.md`, `WELCOME.md`, `docs/README.md`, `docs/failure-modes.md`, `docs/effort-estimation.md`, and `docs/workflow/` in `../railspike`. Allowed development records: this cycle's plans/log/summary/verification, its plan-index entry, and the collection ledger. Reuse canonical contracts and add `docs/workflow/one_shot.md` with the consolidated record template; no duplicate product copy in this repository.
- Complete when entry/recovery instructions agree, scenario and evidence mappings below pass document review, local links and whitespace pass, changed files stay in scope, and the existing product Git-workflow fixture passes. Preserve failed/blocked/pending/inapplicable outcomes explicitly. Correct inconsistent guidance before dependent work; scope expansion returns to Step 2.
- Kiro Web/CLI acceptance here is actionable manual guidance and documented scenario replay, not live execution or enforcement. Application/runtime, UI, deployment, migration, and release verification are inapplicable to this documentation-only scope. Runtime gates, scripts/tests/CI changes, host upgrades, historical backfill, website work, merge, and publication remain excluded.

## Key Risks

- **High risk: authority confusion.** A mode label or an agent-written scope could become fictitious approval. Entry and question scenarios below establish the permitted action before implementation; keep explicit user authority separate from agent-authored records.
- **High risk: lost recovery evidence.** Consolidation or escalation could erase original scope or duplicate study outcomes. Preserve dated history and cycle identity; resolve transition rules before scenario validation.
- **Contract drift:** entry, approval recovery, planning commits, and debug handoffs currently assume staged execution. Qualify these assumptions together and preserve existing staged behavior; an unresolved contradiction blocks completion.

## Planning validation and evidence mapping

- Authorization cases reviewed: “implement this bounded fix as a one-shot” permits only that work; referencing a Step 1 plan permits no advancement; asking about implementation before authorization permits an answer only; asking during authorized execution leaves authority unchanged; expanded scope blocks dependent work until renewed authorization or staged approval.
- Evidence parity: original query → request; requirements/completion boundary → outcome and scope; approach/tradeoffs/risks → proportionate pre-execution approach; planning authority → actual user authorization; implementation summaries → dated changes/decisions; checks/recovery → verification and limitations; branch/commits → revision and delivery status; debug/attribution/study → existing policies with one-shot checkpoints. Genuine non-applicability is explicit; alternatives and stages are not fabricated.
- Compatibility map: `RAILSPIKE.md` owns mode routing, authority, artifacts and commit exceptions; `one_shot.md` owns the lifecycle/template; `WELCOME.md` and README explain deliberate entry without converting all small tasks into cycles; failure guidance distinguishes staged violations from valid one-shot execution; study guidance maps intake/entry/revisions/closeout without requiring fictitious Step 1–3 snapshots.
- Mode transition retains the same cycle identity and original record when the same work moves into staged planning. Distinct additional work gets a linked identity; neither superseded records nor worktree copies count as additional outcomes. Enrolled/unenrolled and debug on/off states remain independent, including resumption; enabled debug keeps its separate log.

## Stage 1 — Define one-shot entry and the core record

**Estimate: 0.20**

- Goal: provide a usable authorization-to-closeout path for ordinary bounded work.
- Dependencies: Step 3 approval, feature branches and this cycle's planning commit under the existing staged rules.
- Expected changes: add the concise lifecycle/template in `docs/workflow/one_shot.md`; route explicit one-shot requests from `RAILSPIKE.md`; distinguish mode, user authority, and record state; specify host artifact location, branch protections, one completion commit, extra meaningful commits, and no-commit status. Keep this cycle's staged cadence unchanged.
- Verification approach: walk explicit authorization, plan reference, question-before/after-authorization, success, and no-commit cases; check local product links, whitespace, and scoped diff before committing.
- Risks or open questions: agent prose must not establish authority; review entry wording before drafting examples and retain a clear stop for unresolved scope.
- Canonical components/API contracts touched: workflow entry, artifact and commit contracts; no application/API changes.
- Estimate details: stage work 0.20, plausible 0.15–0.30; driver is concise lifecycle integration, uncertainty is conflicts with universal staged wording. Includes this stage's review and summary.

## Stage 2 — Complete recovery and study behavior

**Estimate: 0.15**

- Goal: preserve evidence and authority through interruption, expanded scope, and incomplete outcomes.
- Dependencies: Stage 1 verified and committed; its authority rules settled.
- Expected changes: complete one-shot recovery and staged-transition guidance; adapt `docs/failure-modes.md`, `docs/effort-estimation.md`, and relevant central debug/study clauses. Define intake, execution-entry, revision, and closeout snapshots; keep original estimates, honest missing history, attribution and separate retrospective judgments. Record own commit IDs after creation without amendment, using a later authorized record update when needed; cross-repository records identify paired commits.
- Verification approach: review interruption, missing authority, scope expansion, abandonment, unavailable checks, mode transition, and enrolled/unenrolled × debug on/off cases against retained history and identity rules.
- Risks or open questions: avoid duplicate observations and circular commit references; resolve identity and post-commit recording wording before acceptance examples depend on it.
- Canonical components/API contracts touched: recovery, debug, effort collection, and one-shot record lifecycle.
- Estimate details: stage work 0.15, plausible 0.10–0.25; driver is checkpoint/recovery compatibility, uncertainty is exception coverage. Includes focused checks and summary.

## Stage 3 — Align discovery and user guidance

**Estimate: 0.10**

- Goal: let the maintainer select the mode through ordinary project entry points without hidden defaults or contradictory instructions.
- Dependencies: Stage 2 verified and committed.
- Expected changes: update README, WELCOME, documentation index, and only necessary staged workflow cross-references to distinguish staged, one-shot, and ordinary non-cycle work. Provide explicit-use and recovery examples; preserve installation/update procedures and consent for host guidance edits.
- Verification approach: trace each entry to the canonical contract, audit universal Step N/commit claims for proper scope, and confirm examples neither infer execution approval nor imply merge/publication permission.
- Risks or open questions: “small changes proceed directly” must not silently enroll every task; make selection and existing-cycle behavior explicit before handoff.
- Canonical components/API contracts touched: user entry/discovery and existing staged guidance; no host configuration changes.
- Estimate details: stage work 0.10, plausible 0.05–0.15; driver is cross-document consistency, uncertainty is stray universal wording. Includes focused checks and summary.

## Stage 4 — Validate the complete documentation contract

**Estimate: 0.15**

- Goal: retain reviewable acceptance evidence and finish the cycle within approved documentation scope.
- Dependencies: Stage 3 verified and committed; all material contract conflicts resolved.
- Expected changes: save `one_shot_cycles_verification.md` beside this cycle's artifacts, correct scoped documentation defects, complete implementation/study records, and retain omitted/live-runtime checks as unavailable or inapplicable with reasons.
- Verification approach: replay the scenario set above against final instructions; additionally cover missing/unreadable applicable `AGENTS.md` as a documented stop/recovery requirement, not proven runtime interception. For all three reported Kiro failures, record input, expected permitted action, instruction source, and manual review result separately from unperformed Web/CLI runs. Check every evidence category and all local plan links; run `python3 scripts/check-markdown-links.py ../railspike`, `bash scripts/check-railspike-git-workflow.sh ../railspike`, and `git diff --check` in both repositories. Review changed-file scope and paired stage commits. No new executable tests or checker changes.
- Risks or open questions: static passes cannot prove agent compliance; state that evidence boundary in the report and final summary. A failed check blocks closeout until corrected or explicitly replanned.
- Canonical components/API contracts touched: final product documentation and development verification/study records.
- Estimate details: stage work 0.15, plausible 0.10–0.25; owns shared end-to-end document review, existing regression checks and closeout. Uncertainty is corrective documentation work; does not repeat cycle planning overhead.

## Execution and estimate history

- This feature remains a staged cycle: after explicit Step 3 approval, organize approved plans and existing log in `docs/plans/one_shot_cycles/`, repair links/index, create the permitted planning commit, then create the implementation summary. Ledger and unrelated discussion-note changes are outside the initial planning-commit allowance; retain them unstaged for their appropriate authorized handling. Each stage verifies, updates the summary and commits before the next stage; record paired product/development revisions. No history rewriting.
- 2026-10-27 UTC — User explicitly supplied **Approved Step 2**. Scope v1 retained; no added feature requests. Step 3 and implementation await approval.
- 2026-10-27 UTC — Step 3 snapshot: **0.65 reaffirmed**, plausible 0.50–0.85, R1/P2; starting revisions unchanged from [Step 1](./one_shot_cycles_step1_solution_assessment.md#scope-and-estimate-history). All three frozen R1 hashes verified. Codex, same single exposed rater; prior conversation and artifact exposure retained, missing intake unchanged, model/settings and measured labor unavailable. Lifecycle integration remains the driver. Stage values cover each whole stage, are supplemental and non-additive; the cycle total includes shared inspection/planning independently. Preserve these v1 originals and append revisions/retrospectives in Step 4. Maintainer fit/acceptance pending.

*— Codex · 2026-10-27 UTC*
