# Outcome review group 4

[Entry](./README.md) · [Rubric](./rubric.md) · [Queues](./progress.md)

Method: targeted reading of requests, acceptance contracts, stage summaries, verification/limitation passages and available correction/debug records across every mapped family. Source excerpts were screened for unrelated sensitive material. Commit manifests below corroborate narrow file/history facts only; no historical tests were rerun and no full conversation audit was possible.

## C020

**mermaid_diagram_improvement** — Documentation/visual: compact Mermaid diagrams.

- Context/identity: census C020; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: FDP-named entry/process text; exact historical instruction revision/model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0118](./sources.md#s0118), [S0119](./sources.md#s0119), [S0120](./sources.md#s0120), [S0121](./sources.md#s0121).
- **Request and acceptance:** Diagrams should fit about one GitHub viewport, preserve process meaning and be legible in both themes. Final two-row direction replaces earlier horizontal-only preference (S0119:29–32; S0121:35–49).
- **Delivery and evidence:** Reported user acceptance of final GitHub version, but full theme-specific acceptance unknown: light/dark checks were not separately itemized, and explicit return arrow was dropped for text routing (S0121:45–49).
- **Verification and gates:** Local Mermaid 12 rendering, edge/label review, link/scope checks reported. Quoted user acceptance is attributed to summary, not directly observed; do not upgrade it to human review of this dataset.
- **Rework and later outcomes:** User found single row too wide; attempted return edge flipped/stretched rows; two-row revision and textual return route chosen. This is concrete design iteration, not a measured cost (S0121:37–49).
- **Approval and scope:** Summary says push and revised look were approved; full conversation unavailable. Manifest corroborates README/summary stage. Preserved requirements differ from delivered arrow representation, so maintain that qualification.
- **Instruction contribution and effort:** No mapped diagnostic log; no measured instruction contribution or human effort. A readable diagram claim is task acceptance, not proof of workflow effectiveness.
- **Disposition:** Reported final user acceptance retained alongside unresolved per-theme evidence. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0119](./sources.md#s0119), original lines 29–32:

> - Document completion: both diagrams in `README.md` meet the requirements above and have been checked on GitHub in light and dark themes.
> - Audience outcome: each diagram is readable in about one viewport with no crossing edges, and every decision edge is unambiguous.
> - Correction path: if GitHub rendering shows a defect, revise the Mermaid source in a follow-up stage before handoff.
> - Handoff condition: all stage commits are on the feature branch and the Step 4 summary records the GitHub rendering evidence.

[S0121](./sources.md#s0121), original lines 35–49:

> ## Stage 3 - Two-row layout revision
> - Changes:
>   - `README.md`: after reviewing the Stage 1–2 diagrams, the user found the single-row layouts too wide and asked for two rows.
>   - Both diagrams are now `flowchart TB` with a left-to-right Planning row above a left-to-right Implementation row.
>   - Rows are joined by a subgraph-to-subgraph &quot;Approved Step 3&quot; edge; node-level cross-row edges made Mermaid ignore the row direction.
>   - The second diagram&#x27;s return edge is now text only: the stop node reads &quot;return to Step 2 above&quot;.
> - Verification:
>   - Local render with `@mermaid-js/mermaid-cli` 12.0.0: two rows, no crossing edges in either diagram.
>   - A node-level return edge was tried; it flipped the rows (Step 4 above Planning) or stretched the diagram into a tall column, so it was rejected.
>   - `git diff --check` passed; changed files within scope.
>   - Branch pushed to origin with user approval; the user viewed the earlier single-row version on GitHub and approved its look and coloring.
>   - GitHub check of the two-row version: the user reviewed it on GitHub and accepted it (&quot;This is acceptable&quot;). Light/dark legibility was not separately itemized by the user.
>   - Runtime, UI, deployment, migration, and release checks: not applicable.
> - Notes:
>   - Trade-off: the dotted return arrow to the Step 2 node was dropped in favor of the two-row layout; the stop node&#x27;s text carries the routing.

[S0121](./sources.md#s0121), original lines 53–60:

> - Verification:
>   - All three stages completed with stage-scoped commits that include their summary updates; the first Step 4 commit is the planning-doc commit.
>   - Commit count on the branch: 1 planning + 3 stage commits, meeting the minimum of 1 + 3, plus this final summary commit.
>   - Document integrity, `git diff --check`, link check, and file-scope checks recorded per stage; only `README.md` and `docs/plans/` files changed.
>   - Contract met: both diagrams are readable in two rows, decision edges are distinct, and the process meaning is unchanged.
>   - Runtime, UI, deployment, migration, and release checks: not applicable (documentation-only).
> - Notes:
>   - Known trade-off: no return arrow to the Step 2 node in the second diagram (see Stage 3).

### Inspected commit evidence

Repository: `/home/wsl/fdp`. Read-only command: `git show --format=%H%n%s --name-only b8022733c3b629fcc306136a5ef537cfe6839a8c`. Retained output:
```text
b8022733c3b629fcc306136a5ef537cfe6839a8c
docs(stage 3): lay out workflow diagrams in two rows

README.md
docs/plans/mermaid_diagram_improvement_step4_implementation_summary.md
```
Two-row stage changes README and summary; the manifest cannot verify GitHub rendering or the quoted approval.

## C024

**activity_source_filename_commit_plan_v1** — Application: activity source filename/commit metadata.

- Context/identity: census C024; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Nonstandard implementation plan; FDP/Railspike execution attribution and model unknown. Active human effort unknown; no timed record inspected.
- Sources: [S0143](./sources.md#s0143).
- **Request and acceptance:** Activity should display canonical filename and last-touch commit, stored during full/incremental indexing without per-request Git. No-git/error/null should show unavailable rather than a false hash (S0143:3–6,38–46,57–65,80–85).
- **Delivery and evidence:** Five stages and syntax/full-test pass reported. Later hotfix changes rebuilt-row semantics to repository HEAD instead of last-touch commit; full original acceptance therefore unknown rather than assuming the two meanings equivalent (S0143:78,82–83).
- **Verification and gates:** Reported smoke tests include post/label paths, real Git hash, no-git display and schema version. No fresh performance or post-hotfix acceptance run is retained in this plan. Hotfix manifest includes implementation and test changes, not results.
- **Rework and later outcomes:** Explicit production hotfix avoids per-file scans/global-lock duration during rebuild and changes provenance semantics. Preserve this later limitation separately from the original completion claim; exact incident count and operational impact unknown.
- **Approval and scope:** Plan ends with approval gate but includes implementation status. No approval conversation establishes its transitions or hotfix authorization; do not treat stale boilerplate as proof implementation was unauthorized.
- **Instruction contribution and effort:** No instruction diagnostic log. Engineering decision to cache/avoid scans is not evidence of Railspike benefit; human effort unknown.
- **Disposition:** Original completion claim retained; last-touch versus HEAD semantics and post-hotfix validation require reviewer judgment. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0143](./sources.md#s0143), original lines 3–6:

> ## Feasibility
> Yes. Activity rows already come from canonical repository records, so each item can be given a deterministic source filename and, when the canonical repository is a git checkout, the commit SHA that last introduced or changed that source file.
>
> The implementation should store this metadata in the read model during full rebuilds and incremental updates. The activity page should not run git commands per request.

[S0143](./sources.md#s0143), original lines 38–46:

> ### Stage 2: Commit SHA resolution
> - Add a small helper for read-model indexing, likely in `ReadModelBuilder` first:
>   - input: repository-relative path;
>   - output: `git log -1 --format=%H -- &lt;path&gt;` result;
>   - fallback: `no-git` when `.git` is absent, `git-error` when git fails, or `null` if the path has no history.
> - Use the helper while inserting full-rebuild activity rows.
> - Keep this out of `Application::fetchActivity()` and templates.
> - Consider caching path-to-SHA results during a rebuild so duplicate path lookups do not repeat git commands.
> - Status: Implemented in the Stage 2 commit. `ReadModelBuilder` now caches source-path git lookups and writes `source_commit_sha` during full rebuilds.

[S0143](./sources.md#s0143), original lines 65–78:

> - Status: Implemented in the Stage 4 commit. HTML activity cards now render `Source:` with a canonical filename, shortened commit hash, and full hash in `title` when available.
>
> ### Stage 5: Tests and verification
> - Update `LocalAppSmokeTest` activity assertions to expect source filename text for a post item and a thread-label item.
> - Add or extend a test with a real git-backed temp repository so at least one activity row has a real commit SHA.
> - Add no-git coverage using the existing fixture path expectations, since local smoke tests currently expect `no-git` for app version.
> - Run:
>   - `php -l src/ForumRewrite/ReadModel/ReadModelMetadata.php`
>   - `php -l src/ForumRewrite/ReadModel/ReadModelBuilder.php`
>   - `php -l src/ForumRewrite/ReadModel/IncrementalReadModelUpdater.php`
>   - `php -l src/ForumRewrite/Application.php`
>   - `php -l templates/pages/activity.php`
>   - `php tests/run.php`
> - Status: Implemented in the Stage 5 commit. Smoke coverage now checks post and thread-label filenames, no-git unavailable display, schema version 10, and a real git-backed source commit hash. Verification passed with the planned syntax checks and `php tests/run.php`.

[S0143](./sources.md#s0143), original lines 80–88:

> ## Risks And Decisions
> - Full rebuild git lookups may be slow on large repositories if done one path at a time. Cache results at minimum; batch lookup can be considered later if profiling shows a problem.
> - `source_commit_sha` needs a clear meaning. This plan uses the latest commit touching the source file for rebuilds, and the write commit SHA for incremental writes.
> - Production hotfix note: full rebuilds now use the repository head for rebuilt source rows instead of running one `git log` per source file. This keeps file-at-commit links valid for current canonical files and avoids holding the global execution lock across many per-file git scans during deploy-time schema rebuilds. Incremental writes still use the exact write commit SHA.
> - Thread-label activity needs extra source metadata before insertion. Without preserving `recordId`, label items can only point to the thread, not to the canonical label record.
> - In no-git fixture environments, the UI should avoid presenting `no-git` as a real commit hash. A label like `commit unavailable` is preferable if the value is `no-git`, `git-error`, or null.
>
> ## Approval Gate
> Pause here until this plan is approved. After approval, implement in slices with schema/read-model changes first, then rendering and tests.

### Inspected commit evidence

Repository: `/home/wsl/v3`. Read-only command: `git show --format=%H%n%s --name-only 31956831e0e742564e3b6aec80a06c42e060b08a`. Retained output:
```text
31956831e0e742564e3b6aec80a06c42e060b08a
Avoid per-file git scans during read-model rebuild

docs/plans/activity_source_filename_commit_plan_v1.md
src/ForumRewrite/ReadModel/ReadModelBuilder.php
tests/WriteApiSmokeTest.php
```
Hotfix manifest co-locates read-model, test and plan changes, supporting that the semantic/performance follow-up was a real separate change; tests were not rerun.

## C025

**activity_subsystem_extraction_plan_v1** — Internal refactor: activity subsystem extraction.

- Context/identity: census C025; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Nonstandard subplan of C155 cleanup; exact workflow revision unknown. Commit co-author attribution to Claude Sonnet 5 is not verified execution identity. Active human effort unknown; no timed record inspected.
- Sources: [S0144](./sources.md#s0144).
- **Request and acceptance:** Extract data layer and four activity route handlers while retaining call sites and behavior; parent cleanup is a separate unfinished umbrella, not another completed delivery (S0144:3–7,11–30).
- **Delivery and evidence:** Latest status and final extraction commit report met refactor scope. Older in-progress subsection remains stale; preserve it rather than treating document order alone as proof. Commit report supports completion but not independently verified runtime behavior.
- **Verification and gates:** Final commit message reports 487 passing with six known baseline failures and 62/62 signing checks; this plan does not impose an explicit green-full-suite gate. No ordinary-user browser/recovery run established. See supplemental verification excerpt.
- **Rework and later outcomes:** Reported eager PDO construction broke a reflection-based smoke test, fixed with lazy creation; reflected handler references needed updates. Dependency investigation wrongly attributed adjacent-code dependencies, corrected on reread (S0144:23–38,120–129).
- **Approval and scope:** No retained approval transcript or standard staged acceptance baseline. Manifest touches extraction/parent plans, application and controller. This establishes change scope, not prior authorization.
- **Instruction contribution and effort:** Plan reports repeated deferral until data/page-shell scope was separated, and a lesson to inspect reflection references. These are engineering process reports, not attributed proof of a particular workflow instruction; human effort unknown.
- **Disposition:** Reported refactor delivery retained with baseline failures and documentation inconsistency. No causal efficiency claim from reduced Application lines. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0144](./sources.md#s0144), original lines 3–7:

> Sub-plan for the last hard piece of `docs/plans/codebase_cleanup_audit_plan_v1.md`
> Phase 2 (`Application.php` decomposition). Written after the easy `/api`/`/forte_*`
> route groups were exhausted, per the earlier open question: &quot;For `/activity`,
> should we make a separate plan with a checklist so we don&#x27;t get lost?&quot; — yes,
> once there were no more easy wins to do first.

[S0144](./sources.md#s0144), original lines 11–38:

> - **Step 1 (data-layer extraction): done.** `ActivityService`
>   (`src/ForumRewrite/Activity/ActivityService.php`) now owns `fetchActivity()`
>   and its full collaborator graph. `Application.php` keeps thin delegating
>   wrappers (same names/signatures) for every method still called from
>   elsewhere in the class, so no existing call site — including the
>   first-class-callable closure `InstancePageController` already held on
>   `fetchActivity(...)` — needed to change.
> - **Step 2 (page-shell route extraction): done.** All four page-shell
>   route handlers extracted: `/api/forte_commit_detail`, `/forte/activity/`,
>   `/api/forte_activity_page` → `ForteActivityController`; classic
>   `/activity`/`/activity.rss` → `ActivityPageController`. The activity
>   subsystem extraction is now complete end to end (data layer + all
>   route handlers). **Lesson applied along the way: grep `tests/` for
>   reflection references to a method&#x27;s exact name before deleting it** -
>   `ForteActivityReadModelRecoveryTest` reflected directly into
>   `renderForteActivity()`/`handleForteActivityPage()` and needed a real
>   fix (reflect into the new controller instead); a later sweep of the
>   remaining `Application` delegating wrappers also confirmed
>   `activityCommitManifest()` must stay (test-reflected) while 9 others
>   were genuinely dead and got removed.
>
>   `renderActivity()`&#x27;s predicted dependency list (below) turned out
>   stale on re-read - it never actually touched `fetchThread`,
>   `viewerCanInspectLlmExchanges`, `llmExchangeStore`, or
>   `sourceCommitDetails` (those belonged to unrelated nearby methods,
>   an artifact of the original investigation&#x27;s proximity-based scan).
>   It was the cheapest of the four page-shell handlers, needing zero
>   closures - the opposite of the original prediction.

[S0144](./sources.md#s0144), original lines 120–141:

> One bug found and fixed during verification: `RouteServices::activityService()`
> initially built `ActivityService` with an eagerly-opened `PDO` (`$this-&gt;pdo()`
> called at construction). That broke
> `LocalAppSmokeTest::testActivityCommitManifestLinksSignatureSignerKeyOutsideCommit`,
> which reflects directly into `activityCommitManifest()` without going through
> `handle()`/`ensureReadModel()` — so the main read-model database file never
> gets created, and `activityCommitManifest()` never actually needed a main-db
> connection anyway (it&#x27;s git-exec plus a separate cache file). Fixed by making
> `ActivityService`&#x27;s own `pdo()` lazy too (a `\Closure` factory, memoized on
> first real use), matching `RouteServices::pdo()`&#x27;s own laziness exactly.
>
> ## What&#x27;s left (Step 2, in progress)
>
> Three of the four page-shell route handlers are done
> (`ForteActivityController::commitDetail`/`board`/`paginationPage`). What
> remains on `Application`:
>
> - `renderActivity()` (classic `/activity` + implicitly `/activity.rss` via
>   `renderActivityRss()`) — the most entangled: also touches `fetchThread`,
>   `fetchThreadPosts`, `displayThreadTitle`, `viewerCanInspectLlmExchanges`,
>   `llmExchangeStore`, `featureFlags`, `invalidateFeatureFlagsCache`,
>   `sourceCommitDetails`, `resolveViewerProfileFromIdentityHint`.

### Inspected commit evidence

Repository: `/home/wsl/v3`. Read-only command: `git show --format=%H%n%s --name-only 05bc824ddd6be44abfd26716f2c27163c5b8fb21`. Retained output:
```text
05bc824ddd6be44abfd26716f2c27163c5b8fb21
refactor: extract classic /activity and /activity.rss into ActivityPageController

docs/plans/activity_subsystem_extraction_plan_v1.md
docs/plans/codebase_cleanup_audit_plan_v1.md
src/ForumRewrite/Application.php
src/ForumRewrite/Http/ActivityPageController.php
```
Final extraction manifest corroborates controller/application changes. [Commit-message verification claim](./supplemental.md#c025-retained-verification-claim) adds reported tests, not independent reproduction.

## C028

**agent_reply_task_queue_merge** — Application/operations: merge agent-reply queue.

- Context/identity: census C028; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0147](./sources.md#s0147), [S0148](./sources.md#s0148), [S0149](./sources.md#s0149), [S0150](./sources.md#s0150).
- **Request and acceptance:** Approved reader requests should create one unified task, worker publishes/skips/records recoverable failure, and legacy worker retires without lost/duplicate requests. Plan explicitly requires focused and full suites pass (S0148:29–32; S0149:11).
- **Delivery and evidence:** Unified implementation and focused lifecycle/recovery tests reported met; full release acceptance known unmet because full-suite assertion fails and target cron/reply verification remains external (S0150:56–62).
- **Verification and gates:** Reported 17/34/37/29 focused passes and 21 local-agent tests. Existing read-model-diagnosis assertion also fails in isolation; no-new-feature-failures does not satisfy literal full-suite-pass gate. Credentials-dependent live smoke remains pending, not a proven provider failure.
- **Rework and later outcomes:** Legacy request reconciliation and abandoned-task recovery are implemented requirements; summary does not prove a real lost/duplicate incident occurred. Baseline assertion failure is separate from feature regression; later production behavior unknown.
- **Approval and scope:** Manifest supports operator-doc retirement stage with summary. Deployment instructions are not proof cron was replaced on the target. Approval history unassessable without conversation.
- **Instruction contribution and effort:** No mapped diagnostic log or timed human effort. Queue consolidation benefits are intended product behavior, not measured workflow contribution.
- **Disposition:** This analysis qualifies census documented completion with explicit unmet gates; preserve both records and flag discrepancy in final reconciliation. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0148](./sources.md#s0148), original lines 29–32:

> - Normal entry: an approved user requests an eligible agent reply.
> - End-to-end outcome: one general-purpose queue task is visible and the unified worker publishes, skips, or records a recoverable failure for that reply.
> - Needed recovery: an operator can inspect and retry or otherwise resolve failed/abandoned task work without a separate agent-reply worker.
> - Release condition: the separate agent-reply worker/cron execution path is retired, and queue/reply-focused verification demonstrates no duplicate or lost requests.

[S0149](./sources.md#s0149), original lines 11–11:

> - Release condition: no runtime path claims agent-reply requests outside the general-purpose queue, and focused plus full test suites pass.

[S0150](./sources.md#s0150), original lines 28–38:

> ## Stage 3 - Queue new requests and reconcile outstanding work
> - Changes:
>   - New approved-user requests now enqueue or reuse the matching `agent_reply` general-purpose task.
>   - Task-queue runs reconcile durable requested rows that lack an active task, covering pre-merge and interrupted enqueue paths.
>   - Recovered queue tasks can resume an interrupted request claim without creating a duplicate reply request.
> - Verification:
>   - `php tests/run.php AgentReplyGenerationTest TaskQueueWorkerTest TaskQueueCommandTest WriteApiSmokeTest::testGenerateAgentReplyRequiresApprovedViewerAndRecordsRequest` — 37 passed.
>   - `php -l src/ForumRewrite/Agent/SqliteAgentReplyGenerationStore.php` and `php -l scripts/task_queue.php` — passed.
>   - `git diff --check` for Stage 3 files — passed.
> - Notes:
>   - The task queue is now the durable execution owner; reply records remain the source of truth for target identity and publication state.

[S0150](./sources.md#s0150), original lines 52–62:

> ## Stage 5 - Document unified operations and verify release
> - Changes:
>   - Updated the CLI reference, deployment runbook, production example, and README to make `task-queue` the sole agent-reply execution and cron path.
>   - Documented removal of legacy agent-reply cron entries during deployment while retaining reply-specific diagnostic commands.
> - Verification:
>   - `git diff --check` for Stage 5 documentation — passed.
>   - Retired-command search across operator documentation and scripts — no stale execution reference remains; the runbook retains only the instruction to remove a legacy cron entry.
>   - Focused Stage 4 suite — 29 passed; `./v3 agent-reply test-local` — 21 passed.
>   - `./v3 test` and isolated `LocalAppSmokeTest::testRebuildDiagnosisAndRecoveryArchiveSQLiteSidecarsBeforeRebuilding` fail on the existing read-model-diagnosis text assertion (`Next action: ./v3 rebuild recover --confirm`); this feature does not modify that subsystem.
> - Notes:
>   - Deployment verification requiring configured LLM credentials remains external: install only `./v3 task-queue cron`, remove the legacy cron entry, and confirm one requested reply is processed on the target environment.

### Inspected commit evidence

Repository: `/home/wsl/v3`. Read-only command: `git show --format=%H%n%s --name-only 9296757bfe7f1f3b9d38ca3ad4099a3baab22747`. Retained output:
```text
9296757bfe7f1f3b9d38ca3ad4099a3baab22747
docs(stage 5): document unified agent reply queue

README.md
docs/examples/env.production.example
docs/plans/agent_reply_task_queue_merge_step4_implementation_summary.md
docs/reference/v3_cli.md
docs/runbooks/production_deploy.md
```
Operator docs and summary changed together; manifest does not establish target deployment or passing tests.

## C029

**agent_response_direct_preflight** — Application: direct selected-response preflight.

- Context/identity: census C029; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0151](./sources.md#s0151), [S0152](./sources.md#s0152), [S0153](./sources.md#s0153), [S0154](./sources.md#s0154).
- **Request and acceptance:** Approved reader-selected tasks publish via deterministic safeguards without prerequisite full analysis; invalid/stale/duplicate/agent-authored requests retain lifecycle feedback (S0152:17–21,25–28).
- **Delivery and evidence:** Reported met in end-to-end smoke coverage: direct selected tasks publish without post-analysis while legacy automatic work stays separate (S0154:45–47). Actual live-provider/browser use not independently established.
- **Verification and gates:** Reported focused suites pass, class run has order-sensitive approval assertion, full run 718/726 with eight failures. This contract does not explicitly require all tests green; keep failures visible without automatically relabeling feature behavior. Recorded exchange evidence is test-based, not a retained production transcript.
- **Rework and later outcomes:** Legacy fixtures changed to explicit flag opt-in and intentionally unmarked historical requests to avoid machine-specific defaults. Order-sensitive unrelated assertion passes alone; no new direct-path defect established by that failure.
- **Approval and scope:** Summary reports no UI/request-contract change and no migration; manifest is final summary-only verification commit. Full scope/approval chronology remains unassessable.
- **Instruction contribution and effort:** No mapped debug log or measured human effort. Removing a model exchange is product behavior reported by tests, not evidence that this development workflow used less effort.
- **Disposition:** Reported acceptance within test coverage retained with suite/live-evidence limits. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0152](./sources.md#s0152), original lines 25–28:

> - **Normal entry:** an approved reader selects a response mode from a post card.
> - **End-to-end outcome:** the worker validates the target and publishes the selected response after one task-model exchange.
> - **Needed recovery:** an invalid, stale, duplicate, agent-authored, disabled, or failed request reports its current lifecycle status without a false success state.
> - **Release condition:** no full post-analysis exchange is recorded for a newly requested response unless an independent workflow explicitly invokes analysis.

[S0154](./sources.md#s0154), original lines 29–39:

> ## Stage 3 - Legacy isolation and operational verification
>
> - Changes:
>   - Added regression coverage for the two independent controls: legacy automatic replies remain disabled by `DEDALUS_AGENT_REPLIES_AUTOMATIC_ENABLED`, while `AGENT_RESPONSE_REQUESTS_ENABLED` continues to allow selected direct tasks.
>   - Made the legacy automatic-reply fixtures explicitly opt in to that flag, rather than inheriting a machine-specific private-config default.
>   - Reworked the legacy gate fixture to enqueue an intentionally unmarked historical request, proving that only that compatibility path still consults analysis and its gates.
>   - Confirmed no UI or request-contract changes were needed; both paths reuse their existing flags and lifecycle surfaces.
> - Verification:
>   - `./v3 test FeatureFlagEvaluatorTest WriteApiSmokeTest::testLegacyAutomaticFlagDoesNotDisableDirectRequestedTasks WriteApiSmokeTest::testAutomaticAgentReplyWorkCanBeDisabledWithoutDisablingApi WriteApiSmokeTest::testAgentResponseRequestFlagHidesChooserAndRejectsRequests WriteApiSmokeTest::testClaimedAgentReplyRequestPublishesWithoutAnalysis WriteApiSmokeTest::testTaskPreflightRejectsMismatchedContextWithoutAnalysis` — 19 passed.
>   - `./v3 test WriteApiSmokeTest::testPostAnalysisEndpointStoresStubResultIdempotently WriteApiSmokeTest::testAnalyzePostGateFailureUsesCompactVisibilityRules WriteApiSmokeTest::testClaimedUnmarkedAgentReplyRequestStoresGateSkip` — 3 passed.
>   - `./v3 test WriteApiSmokeTest` — direct-response coverage passed; one unrelated, order-sensitive approval-rendering assertion failed in the class run and passed in isolation.

[S0154](./sources.md#s0154), original lines 43–48:

> ## Final verification and handoff
>
> - The normal reader flow is covered end to end: an approved viewer queues a selected task, `./v3 agent-reply cron run` claims it, and the existing lifecycle publishes the generated reply. Direct tasks neither read nor create post-analysis records.
> - Invalid direct-task context safely skips before model work. Existing publication reservation, retry, and posting-failure behavior remain covered by the agent-reply smoke tests.
> - No migration, deployment procedure, new role, or external-system configuration is required. Operators retain the two independent server-wide controls: `AGENT_RESPONSE_REQUESTS_ENABLED` for reader requests and `DEDALUS_AGENT_REPLIES_AUTOMATIC_ENABLED` for legacy automatic suggestions.
> - Final repository-wide verification: `./v3 test` ran 726 tests: 718 passed and 8 failed. Seven failures are already longstanding browser, local-app, and documentation fixtures; the eighth is the order-sensitive approval-rendering test noted above, which passes when run alone. None exercises the direct task-preflight or legacy-isolation changes.

### Inspected commit evidence

Repository: `/home/wsl/v3`. Read-only command: `git show --format=%H%n%s --name-only 746b071d7a90b1f23ad69a74dd89ef3f468d329f`. Retained output:
```text
746b071d7a90b1f23ad69a74dd89ef3f468d329f
docs(stage 3): record direct preflight verification

docs/plans/agent_response_direct_preflight_step4_implementation_summary.md
```
Summary-only final verification commit preserves reported results; it cannot independently corroborate those results.
