# Dated review corrections

[Catalog](./README.md) · [Effective coverage](./coverage.md)

## 2026-10-13T21:51:02.527163+00:00 — Final contract audit

The original batch records remain intact. The rows below supersede only their status/rationale for aggregate reporting; source evidence is unchanged. A reported baseline failure is not a feature regression, but it still leaves an explicit all-tests-pass gate unmet unless the retained record changes that gate. Missing acceptance evidence is uncertainty, not proof a test failed.

| Candidate | Original status | Effective status | Reason |
| --- | --- | --- | --- |
| [C101](./batch-2.md#c101--sqlite_download_with_query_webui_query_catalog) | Documented completion | Indeterminate | The Stage 3 verification includes a manual browser pass; the retained summary lists generation/tests but does not establish that pass. Completion evidence is therefore indeterminate, not proof of a failed browser check. |
| [C162](./batch-3.md#c162--event_feature_gating) | Documented completion | Completion with unmet gates | The explicit release gate requires ./v3 test to pass; two reported baseline failures remain. No-new-regressions does not satisfy that literal gate. |
| [C163](./batch-3.md#c163--event_time) | Documented completion | Completion with unmet gates | The explicit full-suite passing gate is unmet: final verification reports 946/950 passing. |
| [C171](./batch-3.md#c171--feature_flag_lock_explanation) | Documented completion | Completion with unmet gates | The plan says new/updated tests must pass alongside the full suite; the summary retains five failures. |
| [C174](./batch-3.md#c174--feature_flags_redesign) | Documented completion | Completion with unmet gates | The plan explicitly requires a green full project suite; its final report retains six baseline failures. |
| [C177](./batch-3.md#c177--forte_dark_theme) | Documented completion | Completion with unmet gates | The plan requires the visual matrix across all Forte pages; three dark surfaces were explicitly not inspected despite narrower release completion language. |
| [C204](./batch-4.md#c204--mitrapclub_media_embeds) | Documented completion | Completion with unmet gates | The release condition requires a green full suite; baseline failures remain in the final run. |
| [C205](./batch-4.md#c205--mitrapclub_media_embeds_fetched_titles) | Documented completion | Completion with unmet gates | The release condition requires a green full suite; the final report retains two failures, despite successful later live title checks. |
| [C230](./batch-4.md#c230--offline_snapshot_initialization) | Documented completion | Completion with unmet gates | The completion contract includes clean-public-deployment URL verification; the summary says no live public endpoint was available and a prelaunch check remains. |
| [C268](./batch-5.md#c268--prepared_thread_event_fields) | Documented completion | Completion with unmet gates | The full-suite passing gate is explicit; the final report retains four baseline failures. |
| [C298](./batch-5.md#c298--qdb_quote_id_authoring_scope) | Documented completion | Completion with unmet gates | Existing quote permalink/listing coverage must stay green; the full-suite report includes the quote-permalink existing-vote failure. A focused authoring-path pass does not close that regression gate. |

### C101 correction evidence

> - Verification approach: Run focused tests, full relevant PHP/JavaScript checks, clean generation, direct artifact inspection, and a manual browser pass covering load, default query, selection, editing, errors, and local downloads.
>
> — [S0410](./sources.md#s0410), line 56

> - The full suite retains four unrelated baseline failures in `LocalAppSmokeTest`: missing `pages/profile.php`, a core-route `Public key` assertion, a missing `profiles` fixture table, and an existing undefined `$css` assertion. Focused query-catalog and SQLite download tests pass.
>
> — [S0411](./sources.md#s0411), line 73


### C162 correction evidence

> - **Release condition:** `./v3 test` passes, with coverage for default, site-enabled, direct disabled submission, and disable/re-enable behavior.
>
> — [S0528](./sources.md#s0528), line 9

> - `./v3 test` — 882 run, 880 passed, 2 failed: the known unrelated `WriteApiSmokeTest::testTaskQueueProcessesQueuedAgentReplyOnce` and `::testQdbPermalinkShowsViewersExistingUpvoteAsPressedAndDisabled` failures.
>
> — [S0529](./sources.md#s0529), line 47


### C163 correction evidence

> - **Release condition:** full test suite (`php tests/run.php`) passes; rendered board/thread output for existing fixture threads (none with a time) is unchanged on every profile.
>
> — [S0532](./sources.md#s0532), line 9

> - `php tests/run.php` full suite: 946/950 passed, same 4 pre-existing failures, no new ones.
>
> — [S0533](./sources.md#s0533), line 58


### C171 correction evidence

> - Verification approach: Run the project&#x27;s existing test suite and confirm the new/updated tests pass alongside the full suite.
>
> — [S0565](./sources.md#s0565), line 42

> - `./v3 test LocalAppSmokeTest WriteApiSmokeTest` — 202/207 passed, same 5 pre-existing failures, no regressions.
>
> — [S0566](./sources.md#s0566), line 59


### C174 correction evidence

> - Verification approach: full project test suite green; repeat the width/theme manual check from Stages 4–5 as a final confirmation.
>
> — [S0577](./sources.md#s0577), line 61

> - Full suite: `php tests/run.php` — 564 run, 558 passed. The 6 remaining failures are pre-existing and unrelated (activity-manifest tests failing since 2026-09-25, a Node-helper compose-signing test failing since 2026-09-25 — both tracked separately, predating this feature). Confirmed one additional failure (`WriteApiSmokeTest::testIncrementalApprovalMatchesFreshRebuildForTransitiveApprovalAndScoreRefresh`, an approval/read-model parity test with no relation to feature flags) was flaky, not a regression — it failed once and passed twice on immediate reruns with no code changes in between.
>
> — [S0578](./sources.md#s0578), line 95


### C177 correction evidence

> - Release condition: visual check passes on all Forte pages for Auto/dark system, Auto/light system, Light, Dark, and one dark named theme; no light patches or paint flash; existing Forte, theme, and presentation tests pass.
>
> — [S0586](./sources.md#s0586), line 9

> - Not visually exercised in dark: a media-embed card inside a Forte thread, the content-summary dialog, and the username page. They use the same tokens, but they were not inspected.
>
> — [S0587](./sources.md#s0587), line 53


### C204 correction evidence

> - **Release condition:** Flag ships defaulted off on every site; full test suite green; Stage 5 manual verification complete.
>
> — [S0663](./sources.md#s0663), line 9

> - `php tests/run.php` (full suite) re-run after Stage 4&#x27;s wiring, with zero code changes in between — the same two pre-existing failures reappeared, plus one additional flaky failure (`WriteApiSmokeTest::testApprovalIncrementalFailureFallsBackToFullRebuildAndKeepsReadModelHealthy`); re-running that test alone passed immediately, confirming it&#x27;s a pre-existing timing-sensitive flake unrelated to this feature (no source files changed between the Stage 4 run and this one).
>
> — [S0664](./sources.md#s0664), line 54


### C205 correction evidence

> - **Release condition:** Flag stays off everywhere per existing posture; full test suite green; Stage 8&#x27;s manual verification (title Untitled → real, embed rendering throughout, write path round-trip) complete.
>
> — [S0667](./sources.md#s0667), line 9

> - Full suite: 939 run, 937 passed (same 2 pre-existing, unrelated long-standing failures: `testFeatureFlagsPageShowsLockedBadgeWithReasonForNonMutableFlags`, `testTaskQueueProcessesQueuedAgentReplyOnce`).
>
> — [S0668](./sources.md#s0668), line 83


### C230 correction evidence

> - Deployment/external verification: clean public deployment returns the valid
>
> — [S0761](./sources.md#s0761), line 13

> - A live public endpoint was not available in this checkout; operators must run
>
> — [S0762](./sources.md#s0762), line 64


### C268 correction evidence

> - **Release condition:** full test suite (`php tests/run.php`) passes, including new tests for this fix; the anonymous-submit path and `createThread()`&#x27;s own tests are unchanged.
>
> — [S0818](./sources.md#s0818), line 9

> - `php tests/run.php` full suite: 955 run (2 more than Stage 1), 951 passed, same 4 pre-existing failures, no new ones.
>
> — [S0819](./sources.md#s0819), line 30


### C298 correction evidence

> - Release condition: direct, signed, and UI authoring-path coverage passes; existing quote permalink/listing coverage remains green; the implementation summary records verification.
>
> — [S0914](./sources.md#s0914), line 9

> - `php tests/run.php` — 888 run, 885 passed, 3 failed; all failures are classified by the runner as long-standing: the QDB Welcome assertion above, `WriteApiSmokeTest::testTaskQueueProcessesQueuedAgentReplyOnce`, and `WriteApiSmokeTest::testQdbPermalinkShowsViewersExistingUpvoteAsPressedAndDisabled`.
>
> — [S0915](./sources.md#s0915), line 36


## Interpretation and supporting-source clarifications

- C262 is the companion slice plan for C088, not an extra completed cycle: all seven distinctive stage subjects and order align. This is a content-based identity judgment, unlike the six installed-copy matches whose four numbered artifacts are byte-identical. The exact source IDs/fingerprints remain available for challenge.
- C155 is an in-progress umbrella audit; its completed extraction subplan C025 is a separate scoped slice. Do not sum umbrella scope as another completed delivery. C106/C107 have related tag-scoring intent but no verified execution identity; both remain unresolved rather than guessing a merge.
- C190 is an intake inventory, supported by its title and request-list contents; its title quotation is identification evidence, not a completion claim.
- The cutoff excludes this census’s later results. C004 remains in-progress at that cutoff and excluded from its own outcome analysis. S0022 changes only by the authorized Stage 1 sizing addendum; all other captured source bytes and the original study remain unchanged at final audit.
