# Review batch 6

[Catalog](./README.md) · [Rules](./protocol.md) · [Assignments](./candidates.md) · [Sources](./sources.md)

Review method: tool-assisted screening of each assigned family’s goal, numbered-stage coverage, summary verification/limitations and correction passages, with targeted rereads for disputed classifications. Supporting excerpts below are documentary evidence, not rerun application tests or proof of unrecorded approvals. “Documented completion” does not certify that every historical gate was independently audited.

## C326 — thread_card_remove_preview
- Identity: **canonical cycle**; root/family: `v3:docs/plans/thread_card_remove_preview/thread_card_remove_preview`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1007](./sources.md#s1007), [S1008](./sources.md#s1008), [S1009](./sources.md#s1009), [S1010](./sources.md#s1010). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - `php tests/run.php` (full suite) — 584 run, 578 passed, 6 failed; all 6 failures are pre-existing/long-standing (tracked failing since 2026-09-25, before this branch existed), unrelated to this feature — no new failures introduced
>
> — [S1010](./sources.md#s1010), line 23

## C327 — thread_compact_view
- Identity: **canonical cycle**; root/family: `v3:docs/plans/thread_compact_view/thread_compact_view`.
- Status: **Documented completion**. The planning artifact contains implementation/verification statuses and later corrections for the stages; stale approval boilerplate does not erase those recorded outcomes.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1011](./sources.md#s1011), [S1012](./sources.md#s1012). Steps 3 present. No separately numbered Step 4 summary in this family; do not infer abandonment.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Status: Implemented. Extracted `templates/partials/thread_card.php` (with `showPinnedMarker`/`showLabels` params covering the board-vs-tag differences), added the `thread-card__preview` class on the body-preview paragraph, added `thread-list` to the wrapping `&lt;section class=&quot;stack&quot;&gt;` in both `board.php` and `tag.php`. Full test suite (`php tests/run.php`) passes.
>
> — [S1012](./sources.md#s1012), line 16

> - Verification approach: Run `php -l` on all changed PHP files and the full local smoke/test suite (`php tests/run.php` or equivalent); manually re-run the Stage 4 browser walkthrough end to end (toggle, reload persistence, `?density=` override, clean `localStorage` first-visit behavior).
>
> — [S1012](./sources.md#s1012), line 55

## C328 — thread_continuation_merge
- Identity: **canonical cycle**; root/family: `v3:docs/plans/thread_continuation_merge/thread_continuation_merge`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1013](./sources.md#s1013), [S1014](./sources.md#s1014), [S1015](./sources.md#s1015), [S1016](./sources.md#s1016), [S1017](./sources.md#s1017). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - This completes the acceptance-check items from `improve_thread_view.txt`: merged card with one byline/action row, hover-revealed time/actions per piece, separate agent-reply card, decluttered single-line header, working deep links — verified directly against the example thread shape (root + 6 quick same-author replies + trailing agent-style gap reply) across light theme, phone width, and (by code inspection, per Stage 2/3 notes) dark/other themes via the same CSS custom properties.
>
> — [S1017](./sources.md#s1017), line 58

> - `php tests/run.php` (full suite): 591 run (590 + this new test), 585 passed, 6 failed — same 5 long-tracked pre-existing failures plus the already-known `WriteApiSmokeTest` timestamp-tie-break flake from Stage 1 (this particular run happened to land on the &quot;passing&quot; side of that flake, hence &quot;Newly recovered&quot; in the run&#x27;s own diff-against-last-run bookkeeping — not related to this stage&#x27;s change). No new failures introduced.
>
> — [S1017](./sources.md#s1017), line 66

## C329 — thread_inline_reply_form_plan_v1
- Identity: **canonical cycle**; root/family: `v3:docs/plans/thread_inline_reply_form_plan_v1`.
- Status: **Documented completion**. The retained implementation log records the composer changes and a passing full-suite verification.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1018](./sources.md#s1018). Nonstandard planning record(s). No separately numbered Step 4 summary in this family; do not infer abandonment.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Status: complete.
>
> — [S1018](./sources.md#s1018), line 90

> - `php tests/run.php` passed.
>
> — [S1018](./sources.md#s1018), line 157

## C330 — thread_root_card_consolidation_plan_v1
- Identity: **canonical cycle**; root/family: `v3:docs/plans/thread_root_card_consolidation_plan_v1`.
- Status: **Documented completion**. The execution log records all implementation steps and explicitly says all tests passed.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1019](./sources.md#s1019). Nonstandard planning record(s). No separately numbered Step 4 summary in this family; do not infer abandonment.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Step 3: Verified the implementation with `php tests/run.php`; all tests passed.
>
> — [S1019](./sources.md#s1019), line 118

## C331 — thread_root_card_dedupe_title_first_line
- Identity: **canonical cycle**; root/family: `v3:docs/plans/thread_root_card_dedupe_title_first_line/thread_root_card_dedupe_title_first_line`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1020](./sources.md#s1020), [S1021](./sources.md#s1021), [S1022](./sources.md#s1022), [S1023](./sources.md#s1023). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - `php tests/run.php` (full suite) — 577 run, 571 passed, 6 failed; all 6 failures are pre-existing/long-standing (tracked failing since 2026-09-25, before this branch existed), unrelated to this feature — no new failures introduced
>
> — [S1023](./sources.md#s1023), line 22

## C332 — thread_root_card_meta_reorder
- Identity: **canonical cycle**; root/family: `v3:docs/plans/thread_root_card_meta_reorder/thread_root_card_meta_reorder`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1024](./sources.md#s1024), [S1025](./sources.md#s1025), [S1026](./sources.md#s1026). Steps 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - `php tests/run.php LocalAppSmokeTest` — 95 run, 90 passed, 5 failed; same 5 pre-existing/long-standing failures as before this change (tracked failing since 2026-09-25), no new failures — existing thread-page assertions (title/body ordering, byline text, labels, reply count) all still pass unchanged
>
> — [S1026](./sources.md#s1026), line 11

## C333 — thread_root_card_remove_reply_count
- Identity: **canonical cycle**; root/family: `v3:docs/plans/thread_root_card_remove_reply_count/thread_root_card_remove_reply_count`.
- Status: **Indeterminate**. Only Step 2 is retained; it does not establish delivered removal or current execution.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1027](./sources.md#s1027). Steps 2 present. No separately numbered Step 4 summary in this family; do not infer abandonment.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **adjudication queue; no confirmed completed outcome**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> The root post&#x27;s reply count (`N replies`/`1 reply`) on the thread page adds a metadata line that isn&#x27;t needed there — the actual replies are visible right below on the same page.
>
> — [S1027](./sources.md#s1027), line 6

> - As a reader viewing a thread page, I don&#x27;t need a reply count restated above the reply list I&#x27;m already looking at, so removing it reduces clutter in the root post&#x27;s metadata block.
>
> — [S1027](./sources.md#s1027), line 9

## C334 — toolbar_identity_status
- Identity: **canonical cycle**; root/family: `v3:docs/plans/toolbar_identity_status/toolbar_identity_status`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1028](./sources.md#s1028), [S1029](./sources.md#s1029), [S1030](./sources.md#s1030), [S1031](./sources.md#s1031). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Notes: This completes the Step 3 Completion Contract — the toolbar&#x27;s right-hand side now shows accurate, self-correcting, live-updating logged-in/guest status on all three Forte views through the normal page-load flow.
>
> — [S1031](./sources.md#s1031), line 42

> - `php tests/run.php LocalAppSmokeTest` — same 112 passed / 3 pre-existing failures; no new failures.
>
> — [S1031](./sources.md#s1031), line 51

## C335 — unintended_one_time_lobby_redirect_investigation
- Identity: **canonical cycle**; root/family: `v3:docs/plans/unintended_one_time_lobby_redirect_investigation`.
- Status: **In-progress**. The investigation records a fix and test coverage but ends Ready for UAT; final user acceptance is not established.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1032](./sources.md#s1032). Nonstandard planning record(s). No separately numbered Step 4 summary in this family; do not infer abandonment.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **adjudication queue; no confirmed completed outcome**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> After clearing a browser identity and setting up a new one, the first navbar navigation can redirect to `/lobby/` even when approved-members-only mode is disabled. The page says the new identity is awaiting approval. Repeating the same navigation works normally.
>
> — [S1032](./sources.md#s1032), line 7

> 1. Open the Account page and use **Clear identity**, when available.
>
> — [S1032](./sources.md#s1032), line 11

## C336 — user_specific_archives
- Identity: **canonical cycle**; root/family: `v3:docs/plans/user_specific_archives/user_specific_archives`.
- Status: **Indeterminate**. A Step 1 assessment proposes bounded archives without establishing delivered implementation.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1033](./sources.md#s1033). Steps 1 present. No separately numbered Step 4 summary in this family; do not infer abandonment.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **adjudication queue; no confirmed completed outcome**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> Users need downloadable archives of their own visible forum contributions without making bespoke archive generation cheap to spam.
>
> — [S1033](./sources.md#s1033), line 7

> Pros:
>
> — [S1033](./sources.md#s1033), line 11

## C337 — username_page_approver_attribution
- Identity: **canonical cycle**; root/family: `v3:docs/plans/username_page_approver_attribution/username_page_approver_attribution`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1034](./sources.md#s1034), [S1035](./sources.md#s1035), [S1036](./sources.md#s1036), [S1037](./sources.md#s1037). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Changes:
>
> — [S1037](./sources.md#s1037), line 4

> - `src/ForumRewrite/Http/ProfilePageController.php::username()` now computes `ownIdentityIds` from all of this username&#x27;s profiles (approved + unapproved) and passes a new `approverUsernames` key to the `username.php` render array
>
> — [S1037](./sources.md#s1037), line 5

## C338 — v3_status_command
- Identity: **canonical cycle**; root/family: `v3:docs/plans/v3_status_command/v3_status_command`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1038](./sources.md#s1038), [S1039](./sources.md#s1039), [S1040](./sources.md#s1040), [S1041](./sources.md#s1041). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - `./v3 test` — 569 passed; 6 long-standing failures reported by test history in unrelated activity/compose coverage.
>
> — [S1041](./sources.md#s1041), line 35

## C339 — visitor_statistics
- Identity: **canonical cycle**; root/family: `v3:docs/plans/visitor_statistics/visitor_statistics`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1042](./sources.md#s1042), [S1043](./sources.md#s1043), [S1044](./sources.md#s1044), [S1045](./sources.md#s1045). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - `git diff --check` — passed.
>
> — [S1045](./sources.md#s1045), line 57

## C340 — visitor_statistics_aggregate_dashboard
- Identity: **canonical cycle**; root/family: `v3:docs/plans/visitor_statistics_aggregate_dashboard/visitor_statistics_aggregate_dashboard`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: FDP reference in retained text; exact instruction revision unknown.
- Sources/evidence availability: [S1046](./sources.md#s1046), [S1047](./sources.md#s1047), [S1048](./sources.md#s1048), [S1049](./sources.md#s1049). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - `git diff --check` — passed.
>
> — [S1049](./sources.md#s1049), line 67

## C341 — vote_identity_readiness
- Identity: **canonical cycle**; root/family: `v3:docs/plans/vote_identity_readiness/vote_identity_readiness`.
- Status: **Documented completion**. Retained plan/summary records describe implemented stages and verification entries; no outstanding mandatory condition was identified in the reviewed excerpts.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1050](./sources.md#s1050), [S1051](./sources.md#s1051), [S1052](./sources.md#s1052), [S1053](./sources.md#s1053). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - `./v3 test BrowserSigningNormalizationTest LazyComposeSigningTest LocalAppSmokeTest::testAssetFingerprintPathsUseContentHashFilenames LocalAppSmokeTest::testApplicationRendersCoreRoutes QuoteCardDisplayNumberTest::testQdbListingPagesLoadTheVoteButtonAndIdentityLoaderScripts` — 80 passed.
>
> — [S1053](./sources.md#s1053), line 50

## C342 — word97_theme_improvements_plan_v1
- Identity: **canonical cycle**; root/family: `v3:docs/plans/word97_theme_improvements_plan_v1`.
- Status: **In-progress**. Five slices are checked and verified; slices 6–8 remain unchecked, with slice 8 blocked on confirmation/asset; stretch work is separately deferred.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1054](./sources.md#s1054). Nonstandard planning record(s). No separately numbered Step 4 summary in this family; do not infer abandonment.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **adjudication queue; no confirmed completed outcome**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - &#91;x&#93; Slice 5 — Gray inactive surfaces (user request 2026-07-08: card/panel interiors go Win95 dialog silver; white reserved for text inputs and key viewers; --panel/--feedback vars, card frame fill, tags-section-card, and the word97 menu-row garnish all moved to #c0c0c0; verified on board + thread after artifact rebuild) + follow-up: post bodies and classless card paragraphs render as light-gray #e3e3e3 wells matching the tag-group look the user liked (each paragraph its own well; merging with dividers looked worse)
>
> — [S1054](./sources.md#s1054), line 9

> - &#91; &#93; Slice 6 — Word detail pass (end-of-document marker, squiggles, highlighter)
>
> — [S1054](./sources.md#s1054), line 10

> - &#91; &#93; Slice 8 — Clippy easter egg (blocked on user confirmation + asset clip)
>
> — [S1054](./sources.md#s1054), line 12

## C343 — youtube_embed_layout
- Identity: **canonical cycle**; root/family: `v3:docs/plans/youtube_embed_layout/youtube_embed_layout`.
- Status: **Completion with unmet gates**. The summary explicitly leaves the cross-theme/360px browser visual check as a remaining release condition.
- Task: application/operations planning or change. Era: Unknown; step naming alone does not establish instruction version.
- Sources/evidence availability: [S1055](./sources.md#s1055), [S1056](./sources.md#s1056), [S1057](./sources.md#s1057), [S1058](./sources.md#s1058). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **eligible for later outcome analysis**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Visual check in a browser across themes and at 360px: not performed in this session; it is the remaining release-condition item for the reviewer.
>
> — [S1058](./sources.md#s1058), line 28

## C344 — fdp_feature_integration
- Identity: **duplicate/variant of C002**; root/family: `v3:docs/railspike/docs/plans/fdp_feature_integration/fdp_feature_integration`.
- Status: **Duplicate/variant**. Installed Railspike copy shares 4 exact source hashes with C002, including all four numbered plans/summary; it contributes no independent outcome.
- Task: documentation/research. Era: Railspike reference in retained text; exact instruction revision unknown.
- Sources/evidence availability: [S1072](./sources.md#s1072), [S1073](./sources.md#s1073), [S1074](./sources.md#s1074), [S1075](./sources.md#s1075). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **duplicate; counted with canonical**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Verification checks: `python scripts/check-markdown-links.py` passed for 23 files; `git diff --check` passed. Changed files are within the approved scope, and the contract was compared with FDP commit `7f16579` while excluding debug additions.
>
> — [S1075](./sources.md#s1075), line 12

## C345 — homepage_from_scratch
- Identity: **duplicate/variant of C005**; root/family: `v3:docs/railspike/docs/plans/homepage_from_scratch/homepage_from_scratch`.
- Status: **Duplicate/variant**. Installed Railspike copy shares 5 exact source hashes with C005, including all four numbered plans/summary; it contributes no independent outcome.
- Task: documentation/research. Era: Railspike reference in retained text; exact instruction revision unknown.
- Sources/evidence availability: [S1076](./sources.md#s1076), [S1077](./sources.md#s1077), [S1078](./sources.md#s1078), [S1079](./sources.md#s1079), [S1080](./sources.md#s1080). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: R01. Analysis disposition: **duplicate; counted with canonical**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Pending the maintainer: review of copy and rendered page in light, dark, and phone widths, then merge to `master`; live-URL check after Pages deploys.
>
> — [S1080](./sources.md#s1080), line 87

## C346 — instruction_debug_mode
- Identity: **duplicate/variant of C007**; root/family: `v3:docs/railspike/docs/plans/instruction_debug_mode/instruction_debug_mode`.
- Status: **Duplicate/variant**. Installed Railspike copy shares 4 exact source hashes with C007, including all four numbered plans/summary; it contributes no independent outcome.
- Task: documentation/research. Era: Railspike reference in retained text; exact instruction revision unknown.
- Sources/evidence availability: [S1081](./sources.md#s1081), [S1082](./sources.md#s1082), [S1083](./sources.md#s1083), [S1084](./sources.md#s1084). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: No named canonical log match in the original study; related supporting references may exist. Analysis disposition: **duplicate; counted with canonical**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Verification: All 27 Markdown files pass local link checks; debug/recovery anchors, whitespace, and complete-cycle allowed paths pass. The existing Git workflow fixture passes without script changes. Reviewed README examples and recovery instructions against the canonical contract, including initial-log inclusion and final log-only commits. All four completed-step handoffs link the shared contract; phase/stage instructions explicitly avoid reports.
>
> — [S1084](./sources.md#s1084), line 28

> - Verification: Local Markdown links passed for 27 files; whitespace and allowed-file-scope checks passed. All eight canonical step/phase files reference the shared debug anchor; the anchor exists. Approved Steps 1–3 match planning commit `f0a252e` apart from navigation.
>
> — [S1084](./sources.md#s1084), line 14

> - Notes: This workflow never enabled diagnostics. Disabled state is recorded here as approved in Step 3; historical approved plans are preserved apart from navigation. No diagnostic log was created. Runtime, UI, deployment, migration, and release checks are not applicable to this instruction-only change.
>
> — [S1084](./sources.md#s1084), line 13

## C347 — quiet_debug_mode
- Identity: **duplicate/variant of C010**; root/family: `v3:docs/railspike/docs/plans/quiet_debug_mode/quiet_debug_mode`.
- Status: **Duplicate/variant**. Installed Railspike copy shares 5 exact source hashes with C010, including all four numbered plans/summary; it contributes no independent outcome.
- Task: documentation/research. Era: Railspike reference in retained text; exact instruction revision unknown.
- Sources/evidence availability: [S1085](./sources.md#s1085), [S1086](./sources.md#s1086), [S1087](./sources.md#s1087), [S1088](./sources.md#s1088), [S1089](./sources.md#s1089). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: R03. Analysis disposition: **duplicate; counted with canonical**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Verification: `python3 /tmp/quiet-debug-check.py` passed for all 32 Markdown files, including anchors, plan navigation, and preserved original plans/log/backlog hashes. `git diff --check` passed. Active-reference search found no remaining diagnostic-summary or inline-handoff directives. Inspected Stage 2 paths and the planning/Stage 1 commit contents; each contains only its approved scope and Stage 1 includes its summary.
>
> — [S1089](./sources.md#s1089), line 24

## C348 — readme_and_essay_homepage
- Identity: **duplicate/variant of C012**; root/family: `v3:docs/railspike/docs/plans/readme_and_essay_homepage/readme_and_essay_homepage`.
- Status: **Duplicate/variant**. Installed Railspike copy shares 5 exact source hashes with C012, including all four numbered plans/summary; it contributes no independent outcome.
- Task: documentation/research. Era: Railspike reference in retained text; exact instruction revision unknown.
- Sources/evidence availability: [S1090](./sources.md#s1090), [S1091](./sources.md#s1091), [S1092](./sources.md#s1092), [S1093](./sources.md#s1093), [S1094](./sources.md#s1094). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: R04. Analysis disposition: **duplicate; counted with canonical**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Pending the maintainer: review of the rendered page in light, dark, and phone widths, then merge; check the live Pages URL after deploy.
>
> — [S1094](./sources.md#s1094), line 40

## C349 — website_redesign
- Identity: **duplicate/variant of C015**; root/family: `v3:docs/railspike/docs/plans/website_redesign/website_redesign`.
- Status: **Duplicate/variant**. Installed Railspike copy shares 5 exact source hashes with C015, including all four numbered plans/summary; it contributes no independent outcome.
- Task: documentation/research. Era: Railspike reference in retained text; exact instruction revision unknown.
- Sources/evidence availability: [S1095](./sources.md#s1095), [S1096](./sources.md#s1096), [S1097](./sources.md#s1097), [S1098](./sources.md#s1098), [S1099](./sources.md#s1099). Steps 1, 2, 3, 4 present. Source summary reports verification; no runtime checks rerun here.
- Prior-study overlap: R06. Analysis disposition: **duplicate; counted with canonical**.
- Later regressions/limitations: No independent regression search or approval audit performed; retain any limitations in quoted evidence below.

> - Repository checks: `check-markdown-links.py`, `.pl`, and `.mjs` each report 37 Markdown files with valid local links; `check-railspike-git-workflow.sh` passed.
>
> — [S1099](./sources.md#s1099), line 75

> - `.gitignore` now ignores `/temp/` at the maintainer&#x27;s request; it is outside this feature&#x27;s allowed files and is left uncommitted pending the maintainer&#x27;s call.
>
> — [S1099](./sources.md#s1099), line 8
