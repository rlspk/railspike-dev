# Outcome review group 5

[Entry](./README.md) · [Rubric](./rubric.md) · [Queues](./progress.md)

Method: targeted reading of requests, acceptance contracts, stage summaries, verification/limitation passages and available correction/debug records across every mapped family. Source excerpts were screened for unrelated sensitive material. Commit manifests below corroborate narrow file/history facts only; no historical tests were rerun and no full conversation audit was possible.

## C030

**agent_response_dropdown_viewport_fit** — Browser UI: response dropdown viewport fit.

- Context/identity: census C030; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Numbered workflow artifacts retained; exact historical FDP/Railspike instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0155](./sources.md#s0155), [S0156](./sources.md#s0156), [S0157](./sources.md#s0157), [S0158](./sources.md#s0158).
- **Request and acceptance:** Menu should remain usable/anchored while scrolling, flip/scroll within short viewports and close safely. Release requires desktop and short/narrow manual checks in every shipped theme (S0156:15–19,25–28; S0157:10).
- **Delivery and evidence:** Implementation and simulated placement reported complete; acceptance known unmet because required browser/theme/reply pass was not run (S0158:29–33). Fixed-header overlap remains an explicit concern.
- **Verification and gates:** Node syntax and four placement simulations pass; two PHP test files exit zero, which is not a recorded assertion count or proof the normal runner executed tests. No browser scroll-follow, auto-close, theme or end-to-end reply verification retained.
- **Rework and later outcomes:** No theme-specific correction made because none identified without browser. This does not establish absence of a defect. Related chooser C032 supplies context, not independent validation of viewport behavior.
- **Approval and scope:** Final commit is summary-only. Code and simulation claims do not establish browser release approval; conversation history absent.
- **Instruction contribution and effort:** No mapped diagnostic log or measured human effort. Placement simulations are engineering checks, not proof that the workflow improved usability.
- **Disposition:** Qualify census documented completion with explicit unmet manual gate; preserve both. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0156](./sources.md#s0156), original lines 25–28:

> - Normal entry: a reader clicks &quot;request agent reply&quot; on a post or thread root at any scroll position.
> - End-to-end outcome: the full menu is visible and attached to its button, and picking a mode submits the request as it does today.
> - Recovery: closing the menu (Escape, outside click, close button, or button leaving the viewport) returns the page to its prior state; no data is affected.
> - Release condition: verified on desktop and a narrow/short viewport in each shipped theme.

[S0157](./sources.md#s0157), original lines 10–10:

> - Release condition: manual check on desktop and a short/narrow viewport in each shipped theme, plus no regression in existing PHP tests.

[S0157](./sources.md#s0157), original lines 49–49:

> - Verification approach: manual pass in each shipped theme on desktop and narrow/short viewports; request a reply end to end; run the existing PHP test suite.

[S0158](./sources.md#s0158), original lines 25–33:

> ## Stage 3 - Cross-viewport verification and regression guard
> - Changes:
>   - None; no theme-specific margin or z-index tweak was identified, so the shared placement rule is unchanged.
> - Verification:
>   - Placement math simulated in Node for four cases: room below, near the bottom (flips above), short viewport with a tall menu, and a very short viewport. All stay within an 8px gutter; the menu scrolls internally and never drops below the 120px minimum.
>   - `php tests/LocalAppSmokeTest.php` and `php tests/WriteApiSmokeTest.php` (both reference `post_analysis.js`) exit 0.
>   - Not run: manual in-browser check of scroll-follow, auto-close and each shipped theme (no browser available in this environment).
> - Notes:
>   - Fixed headers in a theme could still overlap the menu; this needs a manual theme pass by a reviewer before release.

### Inspected commit evidence

Repository: `/home/wsl/v3`. Read-only command: `git show --format=%H%n%s --name-only 4a363632ecd7b6d95d0e7c44cee04c06f83c96fa`. Retained output:
```text
4a363632ecd7b6d95d0e7c44cee04c06f83c96fa
feat(stage 3): record cross-viewport verification for agent response menu

docs/plans/agent_response_dropdown_viewport_fit_step4_implementation_summary.md
```
Summary-only cross-viewport commit cannot establish manual viewport verification that its own summary says was not run.

## C031

**agent_response_harness_simplification** — Application: separate plain-text response harness.

- Context/identity: census C031; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Numbered workflow artifacts retained; exact historical FDP/Railspike instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0159](./sources.md#s0159), [S0160](./sources.md#s0160), [S0161](./sources.md#s0161), [S0162](./sources.md#s0162).
- **Request and acceptance:** Existing approved-user control should queue default text task, publish attributed response, preserve analysis/legacy behavior and avoid duplicate or false-success outcomes (S0160:17–21,25–28).
- **Delivery and evidence:** Reported met through request/worker smoke and live text-provider probe. The live probe creates no forum post, so it is narrower than a live production end-to-end publication (S0162:70–76).
- **Verification and gates:** Reported API suite 134 passes, worker/CLI seven passes and full run 708 passes with seven longstanding failures. Live provider text probe succeeds after budget increase. Retain failure limits; contract does not explicitly demand a green entire suite.
- **Rework and later outcomes:** Initial 200-token live probe exhausted reasoning budget without text; 2,000-token retry succeeded. This is concrete within-cycle recovery, not a measurement of coding-agent cost. Legacy/default shared publication slot remains reported test coverage.
- **Approval and scope:** Final manifest contains generator, provider-probe script, tests, docs and summary; scope aligns with operational verification. Full approval transcript unassessable.
- **Instruction contribution and effort:** No diagnostic log or human timing. gpt-5-nano identifies the application provider used in the reported probe, not the coding agent; do not use it as workflow model attribution.
- **Disposition:** Reported task/compatibility acceptance retained with limited live evidence. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0160](./sources.md#s0160), original lines 25–28:

> - **Normal entry:** an approved user selects the existing Request agent response control.
> - **End-to-end outcome:** the default task is queued, safely fulfilled by the simplified harness, and published as the normal attributed reply-agent response.
> - **Recovery:** a failed, rejected, or duplicate task reports its existing-style status and creates no extra reply; legacy behavior remains available during rollout.
> - **Release condition:** the default task and legacy path coexist without regression, duplicate publication, or loss of analysis-dependent safeguards.

[S0162](./sources.md#s0162), original lines 53–63:

> ## Stage 5 - Default manual request routing
>
> - Changes:
>   - Routed newly created `/api/generate_agent_reply` requests to `default_text_reply` without changing the request payload, controls, statuses, or feedback UI.
>   - Added configured text-provider construction, including the existing stub path, and passed it into the shared fulfillment service.
>   - Added API assertions that the default task is persisted and that its published body is independent of structured `suggested_response`.
> - Verification:
>   - `php tests/run.php PostAnalyzerFactoryTest WriteApiSmokeTest AgentReplyGenerationTest AgentResponseGeneratorTest` — 134 passed.
>   - `php -l` on `PostAnalyzerFactory` and `PostWorkflowService` — no syntax errors.
> - Notes:
>   - The response-type selector is intentionally out of scope; it can later supply additional named tasks through this same request and fulfillment path.

[S0162](./sources.md#s0162), original lines 65–77:

> ## Stage 6 - Operations and completion verification
>
> - Changes:
>   - Changed `./v3 agent-reply test` from a structured JSON probe to a labeled plain-text task probe and updated its CLI and README reference.
>   - Set the plain-text task completion budget to 2,000 tokens so configured reasoning models can produce a response before exhausting their reasoning budget.
> - Verification:
>   - `php tests/run.php AgentReplyCommandTest OpenAiCompatibleStructuredChatProviderTest AnthropicStructuredChatProviderTest AgentResponseGeneratorTest` — 17 passed.
>   - `php tests/run.php WriteApiSmokeTest::testAgentReplyRequestCommandProcessesQueuedRequestOnce AgentReplyCommandTest` — 7 passed, including a temporary-database queued-worker smoke flow.
>   - `./v3 test` — 708 passed; 7 documented long-standing unrelated browser/local-app/docs failures remained.
>   - `./v3 agent-reply test --timeout=30` — live OpenAI plain-text task succeeded and created no forum post.
> - Notes:
>   - The initial live 200-token probe exhausted the reasoning budget without text; the 2,000-token retry succeeded with `gpt-5-nano`.
>   - No response selector, new queue, or database migration was introduced.

### Inspected commit evidence

Repository: `/home/wsl/v3`. Read-only command: `git show --format=%H%n%s --name-only 0250af16687c935702aa84750360d3ef87aee10e`. Retained output:
```text
0250af16687c935702aa84750360d3ef87aee10e
feat(stage 6): verify plain text agent response tasks

README.md
docs/plans/agent_response_harness_simplification_step4_implementation_summary.md
docs/reference/v3_cli.md
scripts/test_agent_reply_provider.php
src/ForumRewrite/Agent/AgentResponseGenerator.php
tests/AgentReplyCommandTest.php
```
Generator/probe/test/docs changes accompany summary; the commit manifest does not independently establish a successful provider call.

## C032

**agent_response_modes** — Browser/application: selectable response modes.

- Context/identity: census C032; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Numbered workflow artifacts retained; exact historical FDP/Railspike instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0163](./sources.md#s0163), [S0164](./sources.md#s0164), [S0165](./sources.md#s0165), [S0166](./sources.md#s0166).
- **Request and acceptance:** Five named modes from root/reply cards must queue/publish labeled replies with safe lifecycle feedback; manual acceptance on both surfaces required (S0164:17–21,25–28,53–55).
- **Delivery and evidence:** Catalog, API and chooser implementation reported complete, but mandatory final human browser pass remains pending in retained summary and no later stage closes it (S0166:39–45). Full acceptance known unmet; qualitative reasoning quality also lacks recorded acceptance examples.
- **Verification and gates:** Focused tests pass; broad run 712/720 with eight longstanding failures. Later modal/dropdown/flag/prompt changes have uneven verification detail, and final prompt/flag stages do not record a renewed browser acceptance run.
- **Rework and later outcomes:** Summary preserves modal refinement, correction to dropdown, feature flag, logic-analysis replacement, external prompts and automatic-flag separation across ten stages. Those are recorded changes; cannot assign all to defects versus authorized new scope without conversations.
- **Approval and scope:** Current Step 3 has three stages while summary has ten. Preserve mismatch and reported changes rather than infer approval violations from absent transcript. Sampled dropdown manifest corroborates UI/test/summary change only.
- **Instruction contribution and effort:** No mapped instruction diagnostics or measured human effort. Several related response workflows share lifecycle and changes; they are not independent effectiveness trials.
- **Disposition:** Qualify census completion with unresolved manual release gate. Preserve original and flag discrepancy. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0164](./sources.md#s0164), original lines 53–55:

> - A manual acceptance pass can select each of the five modes from both root and reply cards and observe the matching labelled response task through publication.
> - Logic-analysis acceptance examples consistently identify reasoning structure and potential gaps without becoming dismissive or personal.
> - Existing eligibility, duplicate-request, agent-loop-prevention, queued, posted, and failure behaviors continue to pass for both card surfaces.

[S0166](./sources.md#s0166), original lines 39–45:

> - Verification:
>   - `node --check public/assets/post_analysis.js`
>   - Focused smoke checks rendered one shared catalog and response chooser on both root and reply cards, hid only the requested card’s chooser, and displayed the selected-mode completion label.
>   - `./v3 test AgentReplyGenerationTest AgentResponseTaskTest AgentResponseGeneratorTest WriteApiSmokeTest` — passed.
>   - `./v3 test` — 720 run, 712 passed; the 8 failures are all classified by the suite as long-standing and outside this slice.
> - Notes:
>   - The chooser uses the browser’s native dialog focus and Escape behavior. A final human browser pass at desktop and narrow viewport remains the release handoff check.

[S0166](./sources.md#s0166), original lines 59–68:

> ## Stage 5 - Dropdown chooser correction
>
> - Changes:
>   - Replaced the modal with an anchored, non-modal dropdown menu.
>   - Retained label-only choices and added Escape and outside-click dismissal with trigger state restoration.
> - Verification:
>   - `node --check public/assets/post_analysis.js`
>   - `./v3 test AgentResponseTaskTest AgentResponseGeneratorTest WriteApiSmokeTest::testApprovedViewerSeesAgentReplyRequestButtonUntilRequestExists WriteApiSmokeTest::testPostAnalysisScriptDoesNotExposeInProgressReplyGeneration` — 11 passed.
> - Notes:
>   - No request, fulfillment, or safety behavior changed.

[S0166](./sources.md#s0166), original lines 81–111:

> ## Stage 7 - Logic analysis replacement
>
> - Changes:
>   - Replaced the selectable `facts_analysis` mode with `logic_analysis`, labelled “Logic analysis.”
>   - Replaced evidence-verification instructions with a charitable analysis of premises, conclusions, assumptions, and logical gaps.
>   - Removed the dropdown’s facts-analysis disclaimer and its unused styling.
>   - Kept the old task identifier readable and fulfillable solely for requests already stored before this change; new API requests accept only selectable current modes.
> - Verification:
>   - Focused task, generator, request API, and feature-flag tests cover the new mode, rejection of no-longer-selectable modes, and legacy fulfillment compatibility.
>
> ## Stage 8 - External response-mode prompts
>
> - Changes:
>   - Moved the shared system prompt and every response-task instruction into individually reviewable files under `prompts/`.
>   - The generator now loads, trims, validates, and caches those files using the same repository-root convention as other prompt-backed features.
> - Verification:
>   - Generator coverage exercises every selectable task and verifies each loaded instruction.
>
> ## Stage 9 - Readable plain-text task prompts
>
> - Changes:
>   - Replaced the dense all-caps/delimiter layout with readable plain-text headings for the task, response instructions, and forum context.
>   - Kept each supplied forum field explicitly enclosed in `forum-content` markers and stated that those sections are untrusted text, preserving the prompt-injection boundary.
>
> ## Stage 10 - Legacy automatic-response flag separation
>
> - Changes:
>   - Made `DEDALUS_AGENT_REPLIES_AUTOMATIC_ENABLED` the complete gate for the legacy analysis-suggested response path, including direct analysis requests as well as page-triggered work.
>   - Clarified in the private feature-flag catalog that it is independent from `AGENT_RESPONSE_REQUESTS_ENABLED`, which controls reader-selected response tasks.
> - Operational note:
>   - Set `DEDALUS_AGENT_REPLIES_AUTOMATIC_ENABLED=false` to disable legacy automatic replies while retaining the “Request agent response” feature.

### Inspected commit evidence

Repository: `/home/wsl/v3`. Read-only command: `git show --format=%H%n%s --name-only 0c88e078b5d5e737fe701422eb16e8f1aeebe86b`. Retained output:
```text
0c88e078b5d5e737fe701422eb16e8f1aeebe86b
feat(stage 5): use response mode dropdown

docs/plans/agent_response_modes_step4_implementation_summary.md
public/assets/content-interactions.css
public/assets/post_analysis.js
tests/WriteApiSmokeTest.php
```
Dropdown correction changes UI assets, smoke test and summary. It does not establish approval of ten stages or the unperformed browser pass.

## C035

**approval_seed_immediate_refresh** — Application/CLI: immediate approval-seed refresh.

- Context/identity: census C035; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Numbered workflow artifacts retained; exact historical FDP/Railspike instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0169](./sources.md#s0169), [S0170](./sources.md#s0170), [S0171](./sources.md#s0171), [S0172](./sources.md#s0172).
- **Request and acceptance:** Both seed command aliases must refresh approval effects before success without routine rebuild, with parity, cached next-request visibility and accurate persistence/retry recovery (S0171:5–7). Production writes/deployment expressly excluded.
- **Delivery and evidence:** Reported met in isolated real front-controller/CLI fixtures, including atomic persistence, concurrency, invalidation failure and repaired retry. Live host/proxy state remains an acknowledged boundary, not an unmet production gate (S0172:18–26,34).
- **Verification and gates:** Reported focused 17/17 and serving/auth 28/28; broader 267/270 and 29/31 with five failures reproduced on baseline under matching configuration. Synthetic five-run alternating timing reports median 2993.76 to 419.09 ms; this is application latency, not development effort or Railspike effectiveness.
- **Rework and later outcomes:** Timing exposed repeated label/reaction scans; grouping scans addressed quadratic reads. Earlier abandoned timing run excluded; retain method and synthetic limitations. No new observed feature regression claimed, not a guarantee none exists.
- **Approval and scope:** Manifest supports CLI/updater/docs/summary changes. Summary says no production approval writes; historical task authorization cannot be independently established from this artifact.
- **Instruction contribution and effort:** No mapped diagnostic log or active human timing. Detailed fault/latency tests support reported engineering checks; they do not causally attribute quality to a workflow instruction.
- **Disposition:** Preserve reported local parity/recovery acceptance and baseline/live-environment limits. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0171](./sources.md#s0171), original lines 5–7:

> - Both CLI commands synchronously persist seeds and refresh approval, attribution, access, activity, scores, and served output before success, with zero full rebuilds. Preserve arguments, instance overrides, seed semantics, and approval-reply behavior; no schema change.
> - Reject unready models before mutation where possible. Later failures return nonzero with persistence/commit status, stale-state protection, and repair guidance. Matching-seed retries after repair neither duplicate writes nor change reasons; conflicting reasons fail.
> - Release requires parity, recovery/concurrency, cached next-request visibility, and representative timing checks. Verify configured artifact roots and deployment-equivalent routing locally; record live-environment limitations. Production writes/deployment are outside this plan.

[S0172](./sources.md#s0172), original lines 18–26:

> - Changes: Seed persistence is atomic and respects the existing umask. Diagnostics distinguish no seed, persisted/uncommitted seed, and persisted/committed seed, with instance-specific repair commands. Matching retries can commit a previously persisted seed after repair; seed-only commits retain unrelated staged work. Unready models fail before mutation, and refresh failures retain stale protection.
> - Verification: `php tests/run.php ApprovalSeedCommandTest` — 10 passed. Cases cover missing/stale/incompatible/wrong-root/behind models, dirty canonical records, non-Git drift, atomic-write failure, Git-hook failure, transaction rollback, preserved unrelated staging, conflicting reasons, repeated retries, and two contending CLI processes producing one seed commit. Lint and `git diff --check` passed.
> - Notes: Fault tests use disposable repositories, real failing Git hooks/SQLite triggers, and explicit repair before retry. Cached-output failure injection follows in Stage 4, when strict invalidation is introduced. No automatic rebuild occurs on these failure paths.
>
> ## Stage 4 - Complete Served Visibility
>
> - Changes: Added strict seed-specific invalidation to the existing invalidator. Retires active release links, generated route-family HTML (including legacy/detail/QDB aliases), and served offline snapshot/update copies across configured roots; preserves archived releases, assets, PHP, and source documents. Repeats invalidation on retries even with no approval-state delta. Failure blocks success and retains stale protection. Timings distinguish incremental refresh, invalidation, and total write time.
> - Verification: `php tests/run.php ApprovalSeedCommandTest OfflineSnapshotLocatorTest PrivateSiteAuthTest` — 28 passed. New tests exercise cached pages plus active releases, transitive profile/thread API state, public directory/content/activity routes, preserved anonymous pending-directory denial, an existing authenticated member gaining board/pending-directory access, and offline snapshot regeneration on the next request without read-model rebuild. Malformed release pointers and filesystem deletion denial return failure; repaired retries remove remaining stale pages. Lint and diff checks passed.
> - Notes: Invalidation is deliberately broader than individual changed identities because approval affects directory membership, older reactions, and multiple cached representations. Existing PHP/snapshot fallback serves current state; no static rebuild or background publication is required. Already-downloaded/offline browser copies are outside the next-request contract. Live host root configuration and reverse-proxy caches have not been exercised; integration uses the actual front controller with isolated roots.

[S0172](./sources.md#s0172), original lines 30–34:

> - Changes: Documented normal approval and exceptional repair/retry in README and CLI help. Representative timing exposed repeated label/reaction scans per affected target; grouped each sorted record family once per refresh, preserving derivation semantics while removing quadratic file reads. Kept empty non-Git repositories compatible with content-evidence recording.
> - Verification: Final focused run: `php tests/run.php ApprovalSeedCommandTest WriteApiSmokeTest::testIncrementalApprovalMatchesFreshRebuildForTransitiveApprovalAndScoreRefresh WriteApiSmokeTest::testApprovalIncrementalFailureFallsBackToFullRebuildAndKeepsReadModelHealthy WriteApiSmokeTest::testApprovalWriteMarksDerivedStateStaleWhenIncrementalAndFallbackRefreshFail` — **17/17 passed**. Earlier serving/authentication run — **28/28 passed**. All changed PHP files passed lint; `bash -n v3`, diff whitespace, and plan-link checks passed.
> - Verification: Required broader run `php tests/run.php LocalAppSmokeTest WriteApiSmokeTest` — **267/270 passed**. Additional approval/offline/presentation/authentication suites — **29/31 passed**. All five failures reproduce on unchanged baseline `ed6570ee`: core-route Account-button expectation, QDB disabled-vote captions, task-queue agent-reply output, and two offline-bootstrap fixtures missing `author_identity_id`. The queue reproduction required the same `FORUM_SECRETS_PATH` as this checkout; with different configuration it passed. These are existing failures, not fixed or hidden by this feature.
> - Timing: Five alternating complete CLI runs per implementation on a fresh disposable Git fixture, restoring the same canonical HEAD and warm database before every run. Fixture: **2,102 posts, 100 identities with a dormant approval chain, 502 thread labels, 500 post reactions, and 2,000 cached HTML pages**. Compared the original seed script from `ed6570ee` against the new `./v3 approve`, including PHP startup, Git commit, refresh, and (for the new path) cache invalidation. Old samples: **2463.96, 3133.07, 3488.38, 2993.76, 2929.48 ms**; new: **392.23, 419.09, 446.42, 315.18, 452.65 ms**. Median **2993.76 → 419.09 ms**, about **86% lower / 7.1× faster**. These synthetic local timings establish direction, not a production latency guarantee; the abandoned pre-optimization run is excluded.
> - Notes: No production approvals, deployment, migration, or new UI/API were performed. Live host/proxy configuration remains an operational verification boundary. Full rebuild is retained only as explicit repair when readiness or refresh fails; ordinary command success requires no additional action. All five planned stages are complete, with stage-scoped commits and no new observed regressions.

### Inspected commit evidence

Repository: `/home/wsl/v3`. Read-only command: `git show --format=%H%n%s --name-only ef27ecaae803acdddb02000b971bcff4993295fa`. Retained output:
```text
ef27ecaae803acdddb02000b971bcff4993295fa
perf(stage 5): verify and document immediate seed approval

README.md
docs/plans/approval_seed_immediate_refresh/approval_seed_immediate_refresh_step4_implementation_summary.md
scripts/inject_approval.php
src/ForumRewrite/ReadModel/IncrementalReadModelUpdater.php
src/ForumRewrite/ReadModel/ReadModelMetadata.php
v3
```
Performance-stage manifest records updater/CLI/docs/summary changes; timing numbers remain author-reported, not reproduced.

## C036

**activity_commit_file_manifest** — Application: shared activity commit-file manifest.

- Context/identity: census C036; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Numbered workflow artifacts retained; exact historical FDP/Railspike instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0173](./sources.md#s0173), [S0174](./sources.md#s0174), [S0175](./sources.md#s0175), [S0176](./sources.md#s0176).
- **Request and acceptance:** Classic and Forte activity must show all changed paths/statuses/roles and signer key associations; deleted/unavailable/private paths must remain understandable without unsafe links (S0174:15–19,38–41).
- **Delivery and evidence:** Reported met in shared rendering/Git-backed tests and normal local route smoke. Same component serves both views; source-commit semantics restored to latest-touching commit for rebuild parity (S0176:48–58).
- **Verification and gates:** Reported local-app/write-API suites pass including parity; curl to both routes returns Commit files entries. Five existing browser-reaction failures remain in full run. No explicit all-suite-green gate in this plan; visual usability beyond markup is not established.
- **Rework and later outcomes:** Rebuild/latest-touch correction is significant alongside earlier C024 HEAD hotfix; retain this related design evolution without counting it as two independent incidents or claiming the prior performance problem cannot recur.
- **Approval and scope:** Final manifest changes read-model builder, smoke tests and summary. Exact approval conversation and all revision boundaries unassessable; no inference of approval from stale planning gate text.
- **Instruction contribution and effort:** No mapped diagnostics or measured human effort. Shared component reuse is observable in reported design, not evidence of a causal process benefit.
- **Disposition:** Reported functional/route acceptance retained with visual and broad-suite limits. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0174](./sources.md#s0174), original lines 15–19:

> - For every activity item with an available source commit—regardless of activity kind—enumerate every changed file exactly once, including additions, modifications, deletions, and renames.
> - Show each file&#x27;s repository path, change status, and a concise observable canonical role; link only files permitted by existing source-access rules.
> - When the manifest includes a detached signature, show its signer identity and canonical public-key link independently of whether the public-key file changed in that commit; show an explicit unavailable state when no key can be resolved.
> - Classic Activity and Forte Activity must expose the same manifest information for the same event.
> - Preserve existing activity links, source metadata, approval gating, and graceful behavior for missing/unavailable commits.

[S0174](./sources.md#s0174), original lines 38–41:

> - Representative multi-file commits across activity kinds show all changed paths in both Activity views, not only each event&#x27;s source path.
> - Both views show identical paths, statuses, roles, and signature/public-key associations for the same commit.
> - A signature whose public key predates the commit still exposes that key&#x27;s link.
> - Missing commits, deleted files, and unresolved keys remain understandable and do not break either feed.

[S0176](./sources.md#s0176), original lines 37–58:

> ## Stage 4 - Shared Activity rendering
> - Changes:
>   - Added one Activity-only commit-manifest partial listing each changed file&#x27;s status, role, path, and allowed source link.
>   - Detached-signature entries show signer identity and its public-key link or an explicit unavailable state.
>   - Rendered the same partial in Classic Activity cards and Forte Activity detail panes; added compact shared styling.
> - Verification:
>   - PHP syntax checks passed for the new partial and both consumers.
>   - `php tests/run.php LocalAppSmokeTest` passed, including the Classic/Forte manifest parity check.
> - Notes:
>   - Individual post pages retain their existing source metadata unchanged.
>
> ## Stage 5 - Cross-kind verification and rebuild parity
> - Changes:
>   - Ensured full read-model rebuilds retain each source file&#x27;s latest-touching commit, matching incremental activity writes and preserving correct atomic manifests.
>   - Added normal-route coverage for signer-key rendering in both Activity views and generic coverage for every activity row with a source commit.
> - Verification:
>   - `php tests/run.php LocalAppSmokeTest` passed.
>   - `php tests/run.php WriteApiSmokeTest` passed, including incremental/full-rebuild parity tests.
>   - Manual local-server smoke: `curl` to `/activity/?view=content` and `/forte/activity/?view=content` both returned `Commit files (...)` entries.
>   - Full `php tests/run.php` now fails only the five pre-existing browser reaction tests reporting `clickHandler is not a function`.
> - Notes:
>   - The source-commit cache is per rebuild path, so each canonical source path is resolved once per rebuild.

### Inspected commit evidence

Repository: `/home/wsl/v3`. Read-only command: `git show --format=%H%n%s --name-only df4bdc77c82addd23767c50b22475c5878378e77`. Retained output:
```text
df4bdc77c82addd23767c50b22475c5878378e77
feat(stage 5): preserve activity commit context

docs/plans/activity_commit_file_manifest_step4_implementation_summary.md
src/ForumRewrite/ReadModel/ReadModelBuilder.php
tests/LocalAppSmokeTest.php
```
Read-model/test/summary stage supports the reported rebuild-context change; it does not establish test results or performance under production data.
