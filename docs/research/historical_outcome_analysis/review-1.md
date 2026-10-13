# Outcome review group 1

[Entry](./README.md) · [Rubric](./rubric.md) · [Queues](./progress.md)

Method: targeted reading of requests, acceptance contracts, stage summaries, verification/limitation passages and available correction/debug records across every mapped family. Source excerpts were screened for unrelated sensitive material. Commit manifests below corroborate narrow file/history facts only; no historical tests were rerun and no full conversation audit was possible.

## C002

**fdp_feature_integration** — Documentation: integrate FDP plan-organization rules.

- Context/identity: census C002; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0015](./sources.md#s0015), [S0016](./sources.md#s0016), [S0017](./sources.md#s0017), [S0018](./sources.md#s0018).
- **Request and acceptance:** Organize approved plans before implementation, preserving content/navigation and handling collisions; debug integration was explicitly split into another cycle (S0015:34–39; S0016:13–23). Recovery is documented conflict handling, not a runtime journey.
- **Delivery and evidence:** Reported met at the documentation boundary: summary covers both stages and manual organization/conflict scenarios (S0018:9–18). Artifact-supported: inspected requirements and changed-file manifest; no guarantee that agents follow the instructions.
- **Verification and gates:** Reported 23-file link check, existing Git fixture, rendered-copy checks and preservation scenarios. No required unresolved document gate is stated; actual tool outputs and original approvals were not captured here (S0018:11–18).
- **Rework and later outcomes:** Step 1 records a user-requested split into organization then debug work. This is scope refinement, not an observed implementation failure; total rework and later regressions are unknown. C007 is the separate follow-up, not a second account of the same delivery.
- **Approval and scope:** Plan contains an explicit bootstrap exception: older organization timing applies to this cycle (S0017:9). Summary reports approval preservation; manifest co-locates public-copy changes and summary. Complete authorization history is unavailable, so adherence is unassessable.
- **Instruction contribution and effort:** No diagnostic log is mapped for this workflow; no measured benefit/friction or human effort can be attributed. The existence of organized artifacts supports inspectability only.
- **Disposition:** Documentary delivery supported within its stated boundary; execution adherence unknown. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0015](./sources.md#s0015), original lines 34–39:

> Choose **Option B**, as requested during review, to keep the Git history readable. Deliver two sequential documentation-only cycles, each with its own approved requirements, plan, feature branch, planning commit, stage commits, and summary.
>
> - **First cycle — plan organization:** Make feature-folder organization part of Step 4 setup after approval and branching, before the planning commit. Preserve approved content; allow only the necessary moves, index entries, and reference repairs alongside approved plans. Create the summary afterward. Validate skipped Step 1, existing folders, navigation, and commit boundaries. This is independently useful without debug mode; exclude diagnostic state, reporting, and log exceptions from this cycle.
> - **Second cycle — debug mode:** Build on the completed organization rules. Cover durable enable/disable state, recovery, evidence-backed handoff reports, and append-only timestamped logs. Introduce the log-specific planning/stage/final-handoff commit allowances here. Validate disabled and resumed workflows, revisions, unchanged-report suppression, and write failures.
>
> Preserve explicit approvals, direct plan revision, and per-stage commits in both cycles; add no CLI, legacy aliases, unrelated history, or case studies. After Step 1 approval, Step 2 should scope only plan organization. Debug mode remains a separate follow-up requiring its own planning and approvals.

[S0016](./sources.md#s0016), original lines 13–17:

> - After explicit `Approved Step 3` and creation of the Step 4 branch, organize the current feature&#x27;s plans in `docs/plans/{feature_name}/` before its first commit or implementation, regardless of artifact count or skipped Step 1. Reuse an existing feature folder.
> - Preserve separate step files, filenames, and approved substantive content. Repair relative plan navigation, affected repository references, and the feature&#x27;s `docs/plans/README.md` entry; create the index if absent.
> - Limit the initial commit to approved Steps 1–3 (Steps 2–3 when Step 1 was skipped) plus necessary organization moves, index entries, and reference repairs. Exclude implementation, the Step 4 summary, unrelated plans, and unapproved auxiliary content.
> - Create the Step 4 summary afterward in the same folder. Retain existing approvals and stage-by-stage verification, summary updates, and commits.
> - If a destination conflicts or organization requires substantive changes, stop and resolve the issue before committing or implementing; never overwrite artifacts or silently revise approved scope.

[S0017](./sources.md#s0017), original lines 8–9:

> - Handoff requires consistent rules, valid navigation, reviewed scenarios, and stage evidence. Stop on collisions or substantive plan changes; correct references within scope or return for approval. Document checks establish consistency, not guaranteed agent compliance. Runtime/deployment checks are not applicable; review rendered copy if changed.
> - Bootstrap: this cycle starts under the existing rules with a branch and approved-plans-only commit. Stage 1 introduces the new rule and groups this cycle&#x27;s artifacts when its summary is created; do not retroactively amend the planning commit. Later workflows use the new organization timing.

[S0018](./sources.md#s0018), original lines 9–18:

> ## Stage 1 - Consistent plan organization
> - Changes: Added the canonical organization allowance and aligned setup, execution, final verification, README, and recovery guidance. Organized this cycle&#x27;s plans and added the index and summary.
> - Verification: Approved Steps 1–3 compared with planning commit `5fc7b22`; only navigation changed. Manual rule review covered root-level plans (move before commit), existing folders (reuse), skipped Step 1 (Steps 2–3 only), absent index (create), conflicting destinations (stop without overwriting), and substantive revisions (renew approval). Initial commit excludes summary, implementation, unrelated plans, and unapproved auxiliary content.
> - Verification checks: `python scripts/check-markdown-links.py` passed for 23 files; `git diff --check` passed. Changed files are within the approved scope, and the contract was compared with FDP commit `7f16579` while excluding debug additions.
> - Notes: This cycle uses the approved bootstrap: planning commit first under the old rule, then organization in Stage 1 when the fourth artifact is created. Future workflows organize before the initial planning commit. Debug mode is excluded. Runtime, deployment, UI, migration, and release checks are not applicable to these instruction-only changes; validation establishes documentation consistency, not agent adherence.
>
> ## Stage 2 - Public guidance and handoff
> - Changes: Website and HN draft now describe feature-folder organization and navigation repairs before implementation. Added a separate debug-mode backlog cycle, linked to the assessment.
> - Verification: All 23 Markdown files pass local link checks; the existing native Git workflow fixture and whitespace checks pass. Browser checks at 1280, 390, and 320 pixels show no page overflow and valid in-page anchors; the changed note was visually reviewed. Active guidance no longer uses the four-artifact threshold or an unqualified approved-documents-only restriction. Changes remain in the approved documentation/copy scope; no style, runtime, script, or debug implementation changes.
> - Notes: Runtime, deployment, migration, and release-environment checks are not applicable to this documentation change. Browser verification covers the changed explanatory copy only. Manual scenarios establish consistency of the instructions, not a live agent execution guarantee.

### Inspected commit evidence

Repository: `/home/wsl/railspike`. Read-only command: `git show --format=%H%n%s --name-only bd0abe00878f422074bd9e686055b85758ac37fd`. Retained output:
```text
bd0abe00878f422074bd9e686055b85758ac37fd
docs(stage 2): align public copy and record debug mode follow-up

BACKLOG.md
HN_POST_DRAFT.md
docs/plans/fdp_feature_integration/fdp_feature_integration_step4_implementation_summary.md
index.html
```
The public-copy stage includes its summary and copy/backlog files; the manifest alone does not validate prose accuracy or prior approval.

## C005

**homepage_from_scratch** — Static website: replacement homepage.

- Context/identity: census C005; source family retained without adding an independent observation. Original-study overlap: R01. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0023](./sources.md#s0023), [S0024](./sources.md#s0024), [S0025](./sources.md#s0025), [S0026](./sources.md#s0026), [S0027](./sources.md#s0027).
- **Request and acceptance:** Visitors should understand/install Railspike from the ordinary deployed URL; completion requires maintainer review plus merge, and source-backed examples (S0025:17–21,29–30). Recovery is restoring the prior index from history, not an observed recovery run.
- **Delivery and evidence:** Implementation is reported complete with local browser/layout/link checks, but release acceptance is known unmet at the retained cutoff: maintainer review, merge and live URL remain pending (S0027:77–90). Local rendering is not deployed visitor acceptance.
- **Verification and gates:** Reported 10.1 KB page, fetched repository links and 42-file Markdown check. Canonical site was explicitly not fetched; real OS dark toggle, other browsers and screen readers were not exercised. Required maintainer review remains outstanding; optional platform coverage is a separate limit.
- **Rework and later outcomes:** Summary records a later copy-in install sentence (S0027:93–99); this is a requested follow-up, not a measured regression. Debug log reports pre-planning deletion and instructions abbreviated during planning (S0023:19,32); no complete transcript supports a broader compliance verdict.
- **Approval and scope:** Allowed scope is index and feature artifacts; release commit changes only summary. Debug log says stage checks kept unrelated backlog work out. No complete approval chronology inspected; pending review is explicitly known, not inferred.
- **Instruction contribution and effort:** Debug author credits plan/commit gates with isolating unrelated work and preventing a blank-site commit, and reports repetition/stage-sizing friction (S0023:63–78). These are attributed opinions, not independently measured benefit or review cost.
- **Disposition:** Keep local implementation evidence separate from outstanding public-release acceptance. R01 is the same original-study workflow, not new corroboration. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0025](./sources.md#s0025), original lines 29–30:

> Normal entry is the existing site URL after merge to `master` for Pages. A visitor reads the claim, copies the install command, reads the worked example and the limits, and follows links into the repository. Recovery: restore the previous `index.html` from `master` history. Release condition: maintainer review of the rendered page in light, dark, and phone widths, plus a link check, then merge.

[S0027](./sources.md#s0027), original lines 77–90:

> ## Stage 6 - Release verification
> - Changes:
>   - None to `index.html`; verification only.
> - Verification:
>   - Weight and dependencies: 10.1 KB (limit 50 KB); no `&lt;script&gt;`, external stylesheet, font, image, or `url()` reference, so the page needs no third-party request and works with scripting disabled by construction.
>   - Excerpts: the request, Option A, option headings, and recommendation are exact substrings of `git show 68663ca:&lt;file&gt;`; the commit list equals `git log` for the feature folder.
>   - Links: 8 repository links fetched, all HTTP 200 (including the hash-pinned file, tree, and commit links); `node scripts/check-markdown-links.mjs` passes for 42 Markdown files. The canonical Pages URL is not fetched because it serves `master` until merge.
>   - Layout and contrast: first screen, overflow, and contrast results from Stages 4 and 5 stand; no markup has changed since.
>   - Scope: only `index.html` and this feature&#x27;s plan files changed on the branch; `BACKLOG.md` is an uncommitted maintainer edit outside any stage.
> - Notes:
>   - Pending the maintainer: review of copy and rendered page in light, dark, and phone widths, then merge to `master`; live-URL check after Pages deploys.
>   - Not exercised: real OS dark-mode toggle, non-Chromium browsers, and screen readers.
>   - Not done by design: the golden-glow logo and the paper are separate backlog features; the page links repository docs until the paper exists.

[S0027](./sources.md#s0027), original lines 93–99:

>   - One sentence added to the install section of `index.html`: the files can be copied into a project instead of using a submodule, a vendored directory works, RAILSPIKE.md covers path resolution, and the copy is updated by hand.
> - Verification:
>   - &quot;Vendored directory&quot; and path resolution are stated in `RAILSPIKE.md` § Repository Boundary; the README documents only the submodule route, so the copy-in option is the maintainer&#x27;s addition and the update-by-hand clause is an inference from not having a submodule pointer.
>   - Install command still ends at 581 px of 640 px at 360×640; anchor link returns HTTP 200; page unchanged otherwise.
> - Notes:
>   - Requested after Step 4 completed; treated as a one-sentence copy change inside the approved file scope, so no new plan cycle.
>   - The README still describes only the submodule route; aligning it is separate work.

[S0023](./sources.md#s0023), original lines 63–71:

> ### Necessary/useful instructions
> - `step4_implementation_before.md` § Planning Docs Commit Gate: gave a clean first commit (plans, log, index entry) and a base for stage commits while an unrelated `BACKLOG.md` edit and the `index.html` deletion stayed out. Retain.
> - `step4_implementation_do.md` § Stage Boundary Protocol: `git status --short` before each commit kept `BACKLOG.md` out of all six stage commits. Retain.
> - Step 3 § Key Risks with a high-risk entry for the deleted page: led to folding the deletion into the first working-page commit. Retain.
> - Step 3 per-stage \&quot;Early warning / validation\&quot;: made the verbatim-excerpt and first-screen checks concrete. Retain.
>
> ### Redundant/unnecessary instructions
> - One commit per stage with the summary update is restated in `RAILSPIKE.md` § Step 4 commit cadence, `step4_implementation_do.md` § Execution Rules and § Stage Boundary Protocol, and `step4_implementation_after.md` item 2. Suggest consolidating to the protocol with links.
> - `step4_implementation_after.md` item 6 (documentation updated, summary finalized) overlaps the per-stage summary rule. Suggest consolidating.

### Inspected commit evidence

Repository: `/home/wsl/railspike`. Read-only command: `git show --format=%H%n%s --name-only c4f9748cb3b10db2d3ec0d682058217c9cc72e2c`. Retained output:
```text
c4f9748cb3b10db2d3ec0d682058217c9cc72e2c
feat(stage 6): record release verification

docs/plans/homepage_from_scratch/homepage_from_scratch_step4_implementation_summary.md
```
The release-verification commit changes only the implementation summary. Its title does not establish a deployment or human approval.

## C006

**installation_process_improvements** — Documentation: installation and onboarding improvements.

- Context/identity: census C006; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0028](./sources.md#s0028), [S0029](./sources.md#s0029), [S0030](./sources.md#s0030), [S0031](./sources.md#s0031), [S0032](./sources.md#s0032).
- **Request and acceptance:** Improve installation from the supplied failure log: reviewed copy default preserves work, manual updates recover safely, and welcome starts planning without blanket implementation authorization (S0029:7,33–35; S0030). Acceptance is an instruction/checklist outcome, not a live install.
- **Delivery and evidence:** Reported met at that boundary: all three documentation stages and 13 checklist dispositions are recorded; no actual consumer installation or deployment was performed (S0032:19–21; S0028:78–80).
- **Verification and gates:** Scenario review covers dirty work, unsafe extraction, conflicts, provenance, partial-copy/update recovery and welcome. Existing Git fixture covers the retained submodule path, not new prose-only copy behavior. Unrelated repository link failures remain explicitly separated (S0032:8–15).
- **Rework and later outcomes:** The checklist records historic stash/prerequisite failures motivating this cycle, not failures of its new delivery. Source-log details are secondhand here; no raw-log reconstruction is claimed. Summary notes clarification of pointer restaging. Later live effectiveness and total rework remain unknown.
- **Approval and scope:** Checklist distinguishes stash consent from install-anyway authorization and unanswered guidance from consent (S0028:9,15–17); those are reported historical findings, not an independent conversation audit. Stage manifest shows documentation/checklist/summary co-presence.
- **Instruction contribution and effort:** No diagnostic log mapped. Failure checklist supports why recovery guidance was added, not a measured contribution of Railspike to this cycle. Active human effort and causal benefit remain unknown.
- **Disposition:** Documentation coverage reported complete; cross-agent installation/recovery effectiveness unverified by design. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0029](./sources.md#s0029), original lines 31–35:

> ## Recommendation
>
> Choose **Option A** first. Download and safely unpack once, inspect without executing or adopting source instructions, and copy that same reviewed snapshot without Git metadata. Keep unrelated project work and staging intact. Verify destination contents before welcome; report the installed path, source revision, and any remaining issue. Submodules remain an explicit alternative; existing installations require recognition rather than automatic conversion.
>
> Welcome should announce that the next suitable task will use Railspike unless the user opts out. Starting planning does not approve later steps or implementation; retain the small-task exception. Persistent project guidance is a separate choice and must preserve existing instructions.

[S0028](./sources.md#s0028), original lines 7–17:

> - &#91;x&#93; **Unrelated work blocks adoption.** Lines 14–48 show installation stopping because of existing untracked plans, samples, and a nested repository. Stopping followed the current rule, but the blanket clean-tree prerequisite introduced work unrelated to installation. Acceptance: default to copying reviewed files into a dedicated project directory without requiring a clean Git tree, staging changes, or touching unrelated work. Use submodules only on explicit request; verify destination conflicts separately.
>
> - &#91;x&#93; **A failed check is treated as passing after partial cleanup.** The user authorized “Stash” at line 54; lines 64–65 acknowledge that the nested repository remained untracked and the clean check was wrong, yet installation proceeded. Permission to stash did not by itself select the separately offered “install anyway” option. Acceptance: reevaluate every applicable prerequisite after remediation, distinguish command success from a satisfied condition, and stop or use an explicitly supported alternative when it still fails. Include a nested-repository case.
>
> - &#91;x&#93; **Stashing leaves the user&#x27;s working context unavailable.** Lines 63 and 83 leave files, including existing plans, in a stash and make restoration the user&#x27;s next job. No restoration is recorded. Acceptance: the default copy installation requires no stash or other relocation of unrelated work. If a user separately requests stashing, track the exact stash, skipped paths, and restoration ownership; preserve recovery data on conflicts.
>
> - &#91;x&#93; **Welcome proceeds despite an unresolved installation prerequisite.** Lines 58–97 report installation and introduce the workflow despite the admitted failed clean check; both README and WELCOME instructions at the time prohibited that transition. Acceptance: distinguish files added, installation verified, commit pending, and welcome completed. Enter welcome only after the chosen installation policy&#x27;s conditions pass; staged-but-uncommitted installation alone need not block welcome.
>
> - &#91;x&#93; **Optional guidance and the first-task choice are easily left unresolved.** Lines 85–97 combine an AGENTS.md offer with a request for the next task and whether to use Railspike. The reply at line 101 supplies only a task. Acceptance: announce Railspike as the default for the first suitable task during welcome, with an opt-out. Keep persistent project guidance a separate choice; an unanswered guidance offer must neither block the task nor authorize editing project instructions.
>
> - &#91;x&#93; **The first substantial task receives no Railspike suggestion.** The deployment request at line 101 leads to several categories of work at lines 105–157, then a requested manifest edit at lines 161–196, without a visible workflow offer. This is an onboarding gap, not proof that an approved workflow was bypassed: no opt-in or accepted reminder entry is recorded, and small direct changes are allowed. Acceptance under the revised direction: treat the first suitable task supplied during welcome as a request to begin Railspike planning unless the user opts out; retain step approvals and the small-task exception. This changes the current opt-in behavior rather than retroactively making the logged edit a violation.

[S0028](./sources.md#s0028), original lines 78–80:

> ### Final checklist disposition
>
> All 13 items are addressed at the approved documentation boundary: items 1–4 and 9–11 by Stage 1, items 7–8 by Stages 1–2, item 12 by Stage 2, and items 5–6 and 13 by Stage 3. For item 3, default-install stash restoration is inapplicable because installation never stashes; independently requested stash operations remain the host workflow&#x27;s responsibility. Evidence supports instruction coverage and the retained submodule fixture, not an end-to-end run across coding agents. No runtime/application change was made.

[S0032](./sources.md#s0032), original lines 13–21:

> - Changes: documented ordinary cloning of committed copies, manual updates against the recorded baseline, local-edit preservation, provenance ambiguity, recovery copies, and failed-replacement recovery. Labeled submodule initialization and updates separately; automatic conversion/updating remains excluded.
> - Verification: reviewed unchanged/edited copies, missing provenance, unavailable baseline, partial replacement, concurrent edits, and existing submodules. `bash scripts/check-railspike-git-workflow.sh` passed; the marked update block matches `master` byte for byte. Targeted document paths/anchor and `git diff --check` passed; only README, checklist, and this summary changed.
> - Notes: fixture coverage applies to the retained submodule update path; new copy-update behavior is instruction/scenario review. Runtime/UI/deployment/migration/release checks remain inapplicable. Stage 1&#x27;s repository-wide link limitations still apply.
>
> ## Stage 3 - Default first-task planning
>
> - Changes: README and WELCOME now announce planning for the first suitable task without a second opt-in. Persistent guidance remains a separate consented edit; unanswered/declined offers do not block a task. Added substantial-task, small-task, opt-out, later-session, and existing-workflow handling. Final review clarified re-staging only the submodule pointer if explicitly requested installation checks out a different reviewed revision.
> - Verification: reviewed the welcome scenarios recorded in the checklist, including the logged deployment request and follow-up correction. All 13 checklist items have documentation-review dispositions. Targeted paths and heading anchors pass across eight documents; `git diff --check`, allowed-file scope, and approved-plan preservation checks passed. Stage 2&#x27;s existing Git fixture passed and its marked update block remains unchanged.
> - Notes: no host AGENTS.md was edited and no actual consumer installation or deployment was performed. The documents define expected behavior; cross-agent execution remains unverified. Runtime/UI/deployment/migration/release checks are inapplicable. Repository-wide link checking remains blocked by the unrelated preexisting failures recorded in Stage 1; the supplied source log remains local and untracked.

### Inspected commit evidence

Repository: `/home/wsl/railspike`. Read-only command: `git show --format=%H%n%s --name-only bf5cd25e1235f8dc661c121c0e6cab5f07132299`. Retained output:
```text
bf5cd25e1235f8dc661c121c0e6cab5f07132299
docs(stage 3): begin first-task planning by default

README.md
WELCOME.md
docs/plans/installation_process_improvements/installation_process_improvements_failure_modes_checklist.md
docs/plans/installation_process_improvements/installation_process_improvements_step4_implementation_summary.md
```
The stage changes README/WELCOME, checklist and summary together; it contains no consumer installation execution evidence.

## C007

**instruction_debug_mode** — Documentation: durable instruction debug mode.

- Context/identity: census C007; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0033](./sources.md#s0033), [S0034](./sources.md#s0034), [S0035](./sources.md#s0035), [S0036](./sources.md#s0036).
- **Request and acceptance:** Deliver optional durable diagnostic state, append-only logs and completed-step handoffs while preserving approvals; resolve unknown state/write failures explicitly (S0034:13–17,23). This is the Railspike follow-up to C002, distinct from older FDP C019.
- **Delivery and evidence:** Reported met for documentation and scenario coverage; feature implemented while this workflow itself remained debug-disabled (S0036:12–24,34). An illustrative report is not evidence of a real diagnostic execution.
- **Verification and gates:** Reported 27-file link checks, Git fixture, shared-anchor coverage and state/log/commit recovery scenarios. Summary explicitly limits this to documentation/manual inspection; no live-agent adherence test (S0036:14–29).
- **Rework and later outcomes:** No delivery correction or later regression established in mapped artifacts. Separation from C002 is planned scope, not failed implementation; total rework unknown.
- **Approval and scope:** Summary reports approved-plan preservation against f0a252e and stage co-presence; inspected later stage manifest is consistent with the stated documentation scope. Conversation-level approvals remain unassessable.
- **Instruction contribution and effort:** No debug log exists because diagnostics were disabled for this workflow. Do not count its illustrative report as benefit/friction feedback or infer zero process cost.
- **Disposition:** Documented contract delivered; actual agent state/log reliability remains unknown. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0034](./sources.md#s0034), original lines 13–17:

> - **Durable mode:** New workflows default off; plain-language enable/disable requests control a visible field below the current artifact&#x27;s navigation bar. Inherit into subsequent artifacts, including Step 4. Restore state on entry, resumption, and handoff; the latest explicit request wins, historical fields remain snapshots, and unresolved missing/conflicting resumed state requires clarification rather than silent reset.
> - **Evidence-backed reports:** When enabled, each completed Step 1–4 handoff includes one concise diagnostic summary and log link before approval where applicable, never per phase or stage. Always include useful and redundant instruction groups, using “No supported findings” when empty. Each finding names its instruction source, observable evidence, and proposed retention or change; distinguish inapplicable and uncertain findings. Non-use alone does not establish redundancy. Disabled mode emits no diagnostics.
> - **Persistent history:** Save full diagnostic output before presenting it in `{feature_name}_debug_log.md` beside the plans. Append UTC-stamped, step-identified entries; corrections append labeled revisions identifying superseded entries, unchanged reports are skipped, and disabling preserves history. Disclose write failures rather than claiming the output was saved. Move the log with the feature&#x27;s plans and repair links.
> - **Bounded commits:** Keep planning logs uncommitted through Steps 1–3; explicitly allow this feature&#x27;s existing log in the initial planning commit. During Step 4, commit additions with the next authorized stage or a separate log-only handoff commit after the final stage. Record mode changes in the summary for the next authorized stage commit. Never amend completed commits or admit unrelated auxiliary content through this allowance.
> - **Advisory only:** Mode requests and findings neither approve steps nor authorize branching, commits, or instruction edits. Preserve required instructions, plan revision, organization, and stage gates; diagnose workflow instructions, not application bugs or hidden reasoning.

[S0036](./sources.md#s0036), original lines 12–24:

> - Changes: Added the shared Railspike contract for durable mode, evidence categories, completed-step reports, append-only logs, and bounded log commits. Wired all four step entry/resumption and completion paths while preserving approval and organization rules.
> - Notes: This workflow never enabled diagnostics. Disabled state is recorded here as approved in Step 3; historical approved plans are preserved apart from navigation. No diagnostic log was created. Runtime, UI, deployment, migration, and release checks are not applicable to this instruction-only change.
> - Verification: Local Markdown links passed for 27 files; whitespace and allowed-file-scope checks passed. All eight canonical step/phase files reference the shared debug anchor; the anchor exists. Approved Steps 1–3 match planning commit `f0a252e` apart from navigation.
> - Scenario review (manual inspection of the contract and handoffs):
>   - New/default-off: record disabled, emit no diagnostics, create no log; explicit enable overrides the default.
>   - Inheritance/resumption: use the current artifact or latest completed artifact, preserving historical snapshots; unresolved missing/conflicting state asks for clarification.
>   - Disable/re-enable: suppress reports while disabled and reuse preserved history when enabled again.
>   - Empty/inapplicable findings: required groups say “No supported findings”; inapplicable and uncertain findings remain separate, with no redundancy inferred from non-use.
>   - Revisions/unchanged output: append a timestamped correction identifying its superseded entry; skip unchanged reports without overwriting history.
>   - Write failures: disclose the failure and do not claim a saved report; resolve before presenting output as logged.
>   - Organization/initial commit: move and relink the feature log without altering state/history; include only that log alongside the existing approved-plan allowance.
>   - Stage/final handoff: no phase/stage reports; pending additions accompany authorized stage commits, while the final Step 4 report gets a log-only handoff commit without amendment.
> - Evidence boundary: These are documentation and manual scenario checks, not live agent execution tests or a claim that diagnostics ran during this workflow.

[S0036](./sources.md#s0036), original lines 26–35:

> ## Stage 2 - Usage, recovery, and final verification
> - Changes: Added README enable/disable prompts, durable-state explanation, an explicitly illustrative report, and log commit guidance. Added recovery for unresolved state, failed logging, and duplicate reports. Closed the separate backlog item.
> - Verification: All 27 Markdown files pass local link checks; debug/recovery anchors, whitespace, and complete-cycle allowed paths pass. The existing Git workflow fixture passes without script changes. Reviewed README examples and recovery instructions against the canonical contract, including initial-log inclusion and final log-only commits. All four completed-step handoffs link the shared contract; phase/stage instructions explicitly avoid reports.
> - Notes: This is documentation and manual scenario verification, not a live agent execution guarantee. No runtime, website, deployment, migration, or release changes were made, so those checks are not applicable. The illustrative report is not evidence that diagnostics ran in this workflow.
>
> ## Handoff
> - Planning commit: `f0a252e`, containing approved Steps 1–3 in their feature folder plus the index entry; no implementation or summary.
> - Stage 1 commit: `17d2028`; Stage 2 is the commit containing this completed checklist and summary. Each stage includes its summary update; no history was amended.
> - Debug mode is implemented and remains disabled for this workflow. No diagnostic log or log-only handoff commit is needed without diagnostic output.
> - Both stages complete; no remaining scope changes. Enable the feature in a workflow with “Enable Railspike debug mode for this workflow.”

### Inspected commit evidence

Repository: `/home/wsl/railspike`. Read-only command: `git show --format=%H%n%s --name-only 95c435b82bf66c25bde834cbedfed8c54c361863`. Retained output:
```text
95c435b82bf66c25bde834cbedfed8c54c361863
docs(stage 2): document debug usage and recovery

BACKLOG.md
README.md
docs/failure-modes.md
docs/plans/instruction_debug_mode/instruction_debug_mode_step4_implementation_summary.md
```
The final stage contains usage/recovery documentation, backlog and summary; no actual diagnostic log was produced for this workflow.

## C008

**project_debug_default** — Documentation: project-default debug marker.

- Context/identity: census C008; source family retained without adding an independent observation. Original-study overlap: R02. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0037](./sources.md#s0037), [S0038](./sources.md#s0038), [S0039](./sources.md#s0039), [S0040](./sources.md#s0040), [S0041](./sources.md#s0041).
- **Request and acceptance:** Allow consuming-project defaults without overriding explicit requests or existing workflow state. Step 3 fixes presence-only marker semantics; ambiguity requires clarification (S0039:15–19; S0040:7–10).
- **Delivery and evidence:** Reported met for the instruction contract, not executable settings behavior: 14 manual scenarios cover discovery, precedence, persistence and recovery (S0041:12–29). No actual marker was created.
- **Verification and gates:** Reported fixture, scope and affected-link checks pass; six unrelated future-plan link failures are disclosed. Empty/arbitrary/false/unreadable contents with known presence are reviewed as the same enabled default, not parsed (S0041:7–8,16–29).
- **Rework and later outcomes:** Debug revision explicitly replaces earlier preference-format discussion with the user-requested presence-only marker (S0037:69–76). This is design refinement before execution, not runtime regression; later outcomes unknown.
- **Approval and scope:** Planning/stage separation and approved-content preservation are reported; manifest contains canonical instructions, README, recovery guide and summary. No transcript-based approval audit; shared defaults are not blanket authorization.
- **Instruction contribution and effort:** Debug author credits precedence and stage verification, and flags ambiguous page limits/future-plan link checks (S0037:65–66,88–100). Those are self-reported contributions/friction without measured review burden.
- **Disposition:** Documentation acceptance reported met, live-agent adherence unknown. No unsupported runtime claim. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0040](./sources.md#s0040), original lines 7–10:

> - **Preference:** optional `.railspike_debug_on` file at the consuming-project root. Presence enables the project default; contents are ignored, including empty content or content saying “false.” Absence means no preference and preserves the disabled fallback. Do not read or validate contents. If file presence or project ownership cannot be established, clarify rather than assume absence. Do not create an actual marker file in this feature.
> - **Discovery:** use the consuming-project root established for the workflow and its `docs/plans/`, not the current shell directory or installed Railspike root. Standalone Railspike development uses this repository root; submodule/vendor installations use the host project root. Ask when project ownership is unclear; do not search ancestors or apply nested/global inheritance.
> - **Resolution:** latest explicit workflow request → existing workflow state → project preference for a new workflow → disabled. Consult the preference only when needed; never use it to repair unresolved resumed state. Snapshot resolved mode in the existing artifact field. Adding/removing the marker affects future workflows; overrides do not edit it. Preserve diagnostics, logs, and approvals.
> - **Handoff:** correct contradictions and broken affected links; record scenario results and document/scope checks in the Step 4 summary. Evidence establishes the instruction contract, not agent compliance. Runtime, UI, database, deployment, and external release checks are inapplicable; application/tests/scripts/CI/generated-artifact changes are prohibited.

[S0041](./sources.md#s0041), original lines 6–8:

> - Changes: Extended the canonical debug contract in `RAILSPIKE.md` with consuming-root discovery, presence-only `.railspike_debug_on` semantics, precedence, snapshots, and clarification on uncertain lookup. Added README creation/removal/override examples and aligned `docs/failure-modes.md` recovery. Workflow phase files already delegate to the canonical contract and needed no edits.
> - Verification: `bash scripts/check-railspike-git-workflow.sh` passed; `git diff --check` passed. `python scripts/check-markdown-links.py` reported only six pre-existing future-step links in unrelated `first_release` and `railspike_paper` Step 1 plans (Steps 2–4 for each); all affected local links and feature navigation resolve. Reviewed active debug/default references using `rg`, the implementation diff, and the scenario matrix below; no remaining contract contradictions found. Scoped path/link checks also verify allowed files and preservation of the approved plans/log history.
> - Notes: Planning commit `96e6236` precedes this stage and summary. Plans and the existing log were moved byte-for-byte into this folder; the plan index was updated. No actual marker was created. Runtime, UI, database/migration, deployment, and external release checks are not applicable because this change defines an instruction contract without executable behavior. Application, tests, scripts, CI, and generated artifacts were not changed. Evidence verifies documentation consistency, not guaranteed agent adherence.

[S0041](./sources.md#s0041), original lines 16–29:

> | New workflow, marker absent, no request | Disabled snapshot | Pass |
> | Marker present with empty, arbitrary, or “false” contents | Enabled snapshot in every case; no content read | Pass |
> | Marker present, contents unreadable | Enabled when file presence is established | Pass |
> | Consuming root or file presence uncertain; marker path is a directory | Clarify when lookup is needed; never assume absence | Pass |
> | Explicit disable with marker; explicit enable without marker | Explicit request wins; marker unchanged | Pass |
> | Explicit request with uncertain marker lookup | Request resolves mode without consulting marker | Pass |
> | Existing enabled workflow after marker removal | Remains enabled | Pass |
> | Existing disabled workflow after marker addition | Remains disabled | Pass |
> | Marker contents edited | No mode/default change | Pass |
> | Resumed state missing/conflicting and evidence insufficient | Clarify; marker does not repair state | Pass |
> | Standalone work on Railspike | Marker belongs at this repository root | Pass |
> | Submodule or vendored Railspike, including shell inside install | Marker belongs at host root; installed/ancestor defaults ignored | Pass |
> | Enabled completed-step handoff | Full saved report; one conversational debug link | Pass |
> | Disabled completed-step handoff | No diagnostics/link; existing log preserved | Pass |

[S0037](./sources.md#s0037), original lines 69–76:

> ## 2026-10-13T05:10:29Z — Step 3 — Revision: presence-only marker
>
> Supersedes the preference-format discussion in the 2026-10-13T05:02:03Z Step 3 entry. The user requested `.railspike_debug_on`, with presence alone enabling the default and contents ignored. The plan now specifies that marker, creation/removal examples, and verification for empty, arbitrary, “false,” and unreadable contents when presence is established. Earlier entries remain historical evidence.
>
> **Necessary/useful instructions**
> - `RAILSPIKE.md`, Plan review: revising the current artifact accommodates the user&#x27;s concrete format choice while retaining the approved documentation scope. No settings file or implementation was created. Retain the revision boundary.
> - `RAILSPIKE.md`, Railspike Debug Mode / Durable state and recovery: Step 3 remains enabled; adding/removing the proposed marker affects only future workflows, and content readability is no longer a mode-resolution dependency. Retain existing workflow precedence and snapshots.
> - `docs/workflow/step3_development_plan_do.md`, verification expectations: updating verification alongside the contract removed obsolete JSON-validation scenarios and explicitly checks that marker contents cannot disable debug. Retain contract-specific verification.

[S0037](./sources.md#s0037), original lines 88–100:

> - `docs/workflow/step4_implementation_before.md`, Planning Docs Commit Gate: branch `feature/project-debug-default` and planning commit `96e6236` captured only the approved plans, existing log, and plan-index entry. Byte comparison verified that organization preserved the approved artifacts and log history; the summary was created afterward. Retain this gate.
> - `docs/workflow/step4_implementation_do.md`, Stage Boundary Protocol: stage commit `86a9b65` includes the instruction contract, README examples, failure recovery, and corresponding summary together. Recorded evidence covers 14 manual documentation scenarios, 35 affected local links, allowed-file scope, whitespace, and the passing Git workflow fixture. Retain proportional documentation verification.
> - `RAILSPIKE.md`, Railspike Debug Mode / Durable state and recovery: inherited enabled state remained recorded in the summary while the marker contract was implemented. Explicit/current workflow state has priority over a new-project default; this workflow therefore required no actual marker file. Retain that distinction.
> - `docs/workflow/step4_implementation_after.md`, Final Verification Checklist: inspecting both commits confirmed the required planning/stage separation, complete feature navigation, and documented evidence boundary. Retain these checks.
>
> **Redundant/unnecessary instructions**
> - No supported findings.
>
> **Inapplicable instructions**
> - `docs/workflow/step4_implementation_after.md`, scoped deployment/release/migration dependencies: there is no application or executable setting parser in this approved change. The summary marks runtime, UI, migration, deployment, and external release checks inapplicable with reasons. Retain the scope qualification.
>
> **Uncertain assessments**
> - `README.md`, Documentation checks: the repository-wide Markdown checker fails on six pre-existing future-step links in unrelated untracked plans, while all 35 affected local links resolve. The stage summary records those failures without editing unrelated plans. Clarify treatment of intentionally incomplete plans if repository-wide checks are later automated; no checker change was needed or authorized here.

### Inspected commit evidence

Repository: `/home/wsl/railspike`. Read-only command: `git show --format=%H%n%s --name-only 86a9b65388efe672f1b6d6225906e773c442a9b9`. Retained output:
```text
86a9b65388efe672f1b6d6225906e773c442a9b9
docs(stage 1): enable project debug defaults with a marker file

RAILSPIKE.md
README.md
docs/failure-modes.md
docs/plans/project_debug_default/project_debug_default_step4_implementation_summary.md
```
Canonical contract, examples, recovery and summary occur in the same stage commit; this does not prove the manual scenarios executed as live agent tasks.
