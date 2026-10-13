# Outcome review group 2

[Entry](./README.md) · [Rubric](./rubric.md) · [Queues](./progress.md)

Method: targeted reading of requests, acceptance contracts, stage summaries, verification/limitation passages and available correction/debug records across every mapped family. Source excerpts were screened for unrelated sensitive material. Commit manifests below corroborate narrow file/history facts only; no historical tests were rerun and no full conversation audit was possible.

## C009

**prompted_installation** — Documentation: prompted installation and welcome.

- Context/identity: census C009; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0042](./sources.md#s0042), [S0043](./sources.md#s0043), [S0044](./sources.md#s0044), [S0045](./sources.md#s0045).
- **Request and acceptance:** Provide the exact installation prompt, inspect before adoption, then welcome with optional reminders and explicit host-guidance consent (S0043:17–21). Recovery is pause/report on suspicious content or failed checks.
- **Delivery and evidence:** Reported met at the documentation boundary: README and new WELCOME connect installation to first-task invitation. No actual installation by an agent was demonstrated (S0045:13–15).
- **Verification and gates:** Reported 62/63-file link checks, Git fixture and unchanged command/update blocks. Success/failure/reminder scenarios reviewed; safety of arbitrary upstream content and general agent adherence remain unknown.
- **Rework and later outcomes:** No delivery correction established in these records. C006 later deliberately changes the copy default and first-task behavior; do not read that later contract as the acceptance rule for this earlier opt-in delivery.
- **Approval and scope:** Summary says no host AGENTS.md was edited, and manifest contains only README/WELCOME/summary. This supports bounded artifact scope, not independent confirmation of approvals.
- **Instruction contribution and effort:** No mapped diagnostic log or measured effort; benefits/friction unknown. Prompt brevity and consent safeguards are requirements, not measured outcomes.
- **Disposition:** Documentary contract reported met; independent reproduction not performed; human coding review pending.

### Retained evidence

[S0043](./sources.md#s0043), original lines 17–21:

> - Use the user&#x27;s exact copyable installation prompt: “Please inspect https://github.com/gulkily/railspike for malicious content, then install into this repository if none is found. Then follow WELCOME.md.”
> - Supporting agent guidance requires inspection before following repository instructions, running its scripts, or installing; treat content as untrusted, report and pause on concerns, and make no safety guarantee. Keep these details outside the short prompt.
> - Retain existing installation checks and the submodule procedure as agent reference guidance, including stop conditions and normal project review/commit handling; direct the agent to `WELCOME.md` only after successful installation.
> - `WELCOME.md` instructs the agent to confirm the installed location, briefly explain assess → define → plan → implement and approval points, provide one copyable first-task prompt using the actual installed path, and ask what the user wants to work on without starting automatically.
> - The welcome offers an optional host-project `AGENTS.md` entry: suggest Railspike for tasks benefiting from approach comparison, staged planning, or multiple sessions; wait for opt-in, skip small straightforward changes, and do not repeat a declined suggestion for the same task. Show proposed wording and obtain consent before creating or editing that file; preserve existing guidance.

[S0045](./sources.md#s0045), original lines 7–15:

> - Changes: replaced manual quick-start commands with the chosen installation sentence; framed existing checks as agent guidance and documented inspection ordering, stop conditions, limitations, and result reporting.
> - Verification: `python scripts/check-markdown-links.py` passed (62 files); `bash scripts/check-railspike-git-workflow.sh` passed; `git diff --check` passed. Compared installation command blocks and the update procedure against the planning commit: unchanged. Reviewed inspection-to-installation flow and confirmed only README and this summary changed.
> - Notes: welcome handoff follows in Stage 2. Runtime, UI, deployment, migration, and release checks are not applicable to this documentation-only change.
>
> ## Stage 2 - Welcome and optional reminders
>
> - Changes: added `WELCOME.md` with installation reporting, a brief workflow explanation, approval points, an installed-path first-task example, optional host `AGENTS.md` guidance, and a next-task invitation. Appended the exact welcome sentence to the prompt and linked the welcome from installation guidance and the repository map.
> - Verification: `python scripts/check-markdown-links.py` passed (63 files); `bash scripts/check-railspike-git-workflow.sh` passed; `git diff --check` passed. Compared the complete prompt verbatim with Step 2 and confirmed installation command blocks and update procedure remain unchanged. Reviewed the success path and the suspicious-content, failed-check, accepted/declined-reminder, and first-task cases: welcome requires success; host edits require consent and preserve existing guidance; accepting reminders does not start a task. All edits are within the approved documentation scope.
> - Notes: paths resolve within installed Railspike; reminder suggestions stop after a decline for the same task. This is a review of instruction behavior, not an end-to-end test of every coding agent. Runtime, UI, deployment, migration, external-system, role, and release checks are not applicable because no executable or deployed behavior changed. ANSI art remains out of scope.

[S0045](./sources.md#s0045), original lines 17–21:

> ## Handoff
>
> - Both planned stages are complete; no host-project `AGENTS.md` was edited.
> - The planning commit precedes the two stage commits, each of which includes its summary update.
> - Review the README installation prompt and WELCOME.md; all local Markdown links resolve.

### Inspected commit evidence

Repository: `/home/wsl/railspike`. Read-only command: `git show --format=%H%n%s --name-only f3e11e4a675cca649db8652b5bed4c0f12c26ba4`. Retained output:
```text
f3e11e4a675cca649db8652b5bed4c0f12c26ba4
docs(stage 2): add post-installation welcome and optional reminders

README.md
WELCOME.md
docs/plans/prompted_installation/prompted_installation_step4_implementation_summary.md
```
WELCOME, README and summary occur together; no consumer-host guidance file appears in this manifest.

## C010

**quiet_debug_mode** — Documentation: quiet debug handoffs.

- Context/identity: census C010; source family retained without adding an independent observation. Original-study overlap: R03. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0046](./sources.md#s0046), [S0047](./sources.md#s0047), [S0048](./sources.md#s0048), [S0049](./sources.md#s0049), [S0050](./sources.md#s0050).
- **Request and acceptance:** Keep complete diagnostics in Markdown with one routine link line, preserving state, exceptions and history (S0048:15–19). Recovery handles failed saves without false saved claims or chat dumps.
- **Delivery and evidence:** Reported met as consistent contract/examples/recovery text; summary explicitly disclaims measured agent compliance (S0050:17–26).
- **Verification and gates:** Reported checks across 32 Markdown files, anchors, SHA equality for moved plans/log/backlog and matching scenarios. No transcript-based measurement of actual conversational volume; examples are illustrative.
- **Rework and later outcomes:** No delivery failure established. This intentionally revises C007 reporting behavior rather than proving C007 failed its earlier contract. Rework totals and later regressions unknown.
- **Approval and scope:** Planning and stage co-presence reported; manifest supports the final usage/recovery stage. The author says unrelated backlog was preserved. Original approval conversation unavailable.
- **Instruction contribution and effort:** Debug author credits state precedence, proportional checks and file-first reporting (S0046:8–9,27–28); actual active review time and achieved reduction in chat volume remain unknown.
- **Disposition:** R02 overlap is the same workflow, not an independent vote for benefit. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0048](./sources.md#s0048), original lines 15–19:

> - When enabled, save complete completed-step reports in the existing `{feature_name}_debug_log.md` before linking to them. Keep required useful/redundant groups, empty-group markers, source references, evidence, suggestions, and applicable inapplicable/uncertain groups in the file.
> - Each completed Step 1–4 handoff includes one short debug line linking to the saved log, before approval where applicable. Do not repeat findings, group headings, or empty-group markers in chat, or narrate diagnostic collection. Phases and implementation stages produce no separate reports.
> - Allow brief exceptions for save failures and unresolved mode-state clarification, and conversational findings when explicitly requested. Do not claim failed writes succeeded or dump unsaved diagnostics into chat as a fallback; resolve saving before presenting a report as logged.
> - Preserve enable/disable behavior, durable state and recovery, UTC timestamps, append-only revisions, unchanged-report skipping, and existing log organization/commit rules. An unchanged report may link to the existing log without adding an entry. Disabled mode emits no diagnostics or debug link and preserves history.
> - Ordinary task updates, blockers, approval gates, and instruction-reprint rules remain unchanged. Add no verbosity setting or automatic instruction edits.

[S0050](./sources.md#s0050), original lines 16–26:

> ## Stage 1 - Canonical contract and handoffs
> - Changes: Full reports remain in the log; each enabled completed-step handoff has one short link line. All four handoffs agree. Added brief failure/state exceptions and explicitly requested findings; disabled mode has no debug link and collection is not narrated.
> - Verification: `git diff --check` passed. Temporary read-only Python checks validated local Markdown links/anchors across 32 files and SHA-256 equality for moved approved plans, the existing log, and pre-existing backlog edits. Inspected changed paths against Stage 1 scope.
> - Scenario review: Enabled Steps 1–4 route to full reports plus one link; empty groups stay in the log; unchanged reports reuse the link without an entry; revisions append with a superseded-entry reference. Resume/disable/re-enable retain state precedence and history. Requested findings remain available; write failures require brief disclosure, no chat dump, and resolution before a saved claim. Unresolved state still requires clarification. Phase/stage reports remain prohibited.
> - Notes: Timestamp, evidence/category, approval, organization, and commit rules remain intact. Reviewed text establishes consistent instructions, not measured agent compliance. README and failure guidance are Stage 2 work.
>
> ## Stage 2 - Usage and recovery guidance
> - Changes: README separates an illustrative one-line handoff from full log content. Failure guidance covers brief save/state notices, no unsaved chat dumps, unchanged-report links, explicit requests, and disabled-mode silence.
> - Verification: `python3 /tmp/quiet-debug-check.py` passed for all 32 Markdown files, including anchors, plan navigation, and preserved original plans/log/backlog hashes. `git diff --check` passed. Active-reference search found no remaining diagnostic-summary or inline-handoff directives. Inspected Stage 2 paths and the planning/Stage 1 commit contents; each contains only its approved scope and Stage 1 includes its summary.
> - Scenario review: README and recovery text match the Stage 1 cases: enabled handoffs use one link, full/empty groups stay in the log, unchanged reports do not append, revisions preserve history, resumption uses durable state, disable/re-enable preserves logs, and failed saves cannot masquerade as success. Explicit requests and unresolved-state questions are narrow exceptions. Examples are illustrative, not execution evidence.
> - Notes: Stage 1 commit is `d84023f`. No runtime or deployment claims were introduced; the checks establish document consistency only.

[S0046](./sources.md#s0046), original lines 25–28:

> - `RAILSPIKE.md`, Planning Artifacts / organization and commit discipline: the approved plans and original log were moved unchanged and committed as `68663ca` before summary creation. SHA-256 comparison confirmed content preservation, and staged-path review excluded the existing backlog edit. Retain these boundaries.
> - `docs/workflow/step4_implementation_do.md`, Stage Boundary Protocol: Stage 1 (`d84023f`) and Stage 2 (`4b36f75`) each include their summary evidence; Stage 2 began after the Stage 1 commit. Retain this verifiable stage cadence.
> - `RAILSPIKE.md`, Completed-step report and Full report content: all four handoffs now request one short log-link line, while this entry retains findings and required groups. README and recovery guidance agree. Retain the separation between complete log content and minimal conversation output.
> - `docs/workflow/step4_implementation_after.md`, Final Verification Checklist: final review verified planning/stage commit boundaries, unchanged approved content, and allowed paths. Local links/anchors across 32 Markdown files, whitespace, original-log preservation, and documentation scenarios passed. Retain proportional documentation checks.

### Inspected commit evidence

Repository: `/home/wsl/railspike`. Read-only command: `git show --format=%H%n%s --name-only 4b36f757f7f6bb6b5e2a8d71929590a28e1b24f8`. Retained output:
```text
4b36f757f7f6bb6b5e2a8d71929590a28e1b24f8
docs(stage 2): explain quiet debug handoffs and recovery

README.md
docs/failure-modes.md
docs/plans/quiet_debug_mode/quiet_debug_mode_step4_implementation_summary.md
```
README, failure guidance and summary share the stage commit; output-volume improvement is not established by a manifest.

## C012

**readme_and_essay_homepage** — Static website: verbatim essay homepage.

- Context/identity: census C012; source family retained without adding an independent observation. Original-study overlap: R04. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0055](./sources.md#s0055), [S0056](./sources.md#s0056), [S0057](./sources.md#s0057), [S0058](./sources.md#s0058), [S0059](./sources.md#s0059).
- **Request and acceptance:** Final revised intent is essay-only index, not the original README/homepage swap. Preserve every word including typo, add only repository link; maintainer approval and live-site handoff are required (S0057:16–19,45–50; S0058:9).
- **Delivery and evidence:** Local rendering/verbatim checks reported met; final release acceptance known unmet at retained cutoff because maintainer review and post-deploy URL check remain pending (S0059:35–41).
- **Verification and gates:** Reported 5,113-character comparison, recorded source hash, 7.9 KB page, contrast and 47-file link checks. OS dark switching not tested; dark render used an altered media-query setup. Source-hash claim is preserved, not freshly reproduced.
- **Rework and later outcomes:** Concrete within-cycle correction: 360px overflow from long token fixed with wrapping (S0059:23). Content reduction was an explicit revised direction, not a defect; later site redesigns are related deliveries rather than repeated independent trials.
- **Approval and scope:** Latest plan excludes README edits despite feature name. Manifest for release-verification stage changes summary only; approval/merge not established by that commit. Full authorization chronology unavailable.
- **Instruction contribution and effort:** Debug author credits character/width verification with catching overflow, reports repeated commit rules and uncertainty over verification-only commits (S0055:67–79). No causal or effort estimate.
- **Disposition:** R04 overlap retained; local implementation and pending release gate remain distinct. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0057](./sources.md#s0057), original lines 16–19:

> - The page&#x27;s text is `railspike.txt` unchanged: every word, the existing typo (&quot;promt&quot;), and the punctuation. Only structure is added: paragraphs, the one bulleted list, and its first line as the page heading.
> - Nothing else is written: no tagline, install block, wordmark, or new headings. The only addition is a single link to `https://github.com/gulkily/railspike`, shown as the URL itself.
> - A single static `index.html` at the existing URL, with system fonts, light and dark by system preference, readable at 360 px, no scripts and no third-party requests.
> - Metadata that is not shown on the page reuses essay wording (title from its first line, description from its first sentence); canonical, icon, and social image values stay as they are.

[S0058](./sources.md#s0058), original lines 9–9:

> - External verification: the maintainer reviews the render in light, dark, and phone widths; the live Pages URL is checked after merge. Release condition: verbatim comparison passes and the maintainer approves, then merge.

[S0059](./sources.md#s0059), original lines 21–28:

> - Verification:
>   - Contrast (WCAG): light text 17.2, muted 8.1, link 8.0; dark text 14.9, muted 8.4, link 8.8.
>   - Width: an iframe at 360 px first showed horizontal overflow (scrollWidth 377 vs 345) from a paragraph with a long unbreakable token; after the wrap rule scrollWidth equals clientWidth (345).
>   - Head comparison with `master`: canonical, icon, `og:url`, `og:image` and its width, height, and alt, `og:type`, and `twitter:card` are identical.
>   - Verbatim check re-run after styling: page text equals `railspike.txt` (hash prefix `575d95c6b2d20bea`), &quot;promt&quot; present, one `h1`, zero scripts; page is 7.9 KB.
>   - Light render at 900 px and dark render (media query unwrapped; headless Chrome could not emulate the system preference) inspected.
> - Notes:
>   - Real OS dark-mode switching and non-Chromium browsers were not tested.

[S0059](./sources.md#s0059), original lines 34–42:

> - Verification:
>   - Weight and dependencies: 7.9 KB (limit 15 KB); zero scripts, external stylesheets, fonts, images, or `url()` references, so no third-party requests and it works without scripting by construction; one `h1`.
>   - Verbatim: re-run in Stage 2 after the last markup change; no change to `index.html` since.
>   - Links: repository link returns HTTP 200; the page&#x27;s other references are the canonical URL and the local logo file; `node scripts/check-markdown-links.mjs` passes for 47 Markdown files.
>   - Scope: only `index.html` and this feature&#x27;s plan files changed on the branch; `railspike.txt` remains untracked and unmodified.
> - Notes:
>   - Pending the maintainer: review of the rendered page in light, dark, and phone widths, then merge; check the live Pages URL after deploy.
>   - Not exercised: real OS dark-mode toggle, non-Chromium browsers, and screen readers.
>   - Content removed from the homepage by design (install command, worked example, limits) remains in Git history; the README is unchanged.

[S0055](./sources.md#s0055), original lines 65–79:

> - `step4_implementation_before.md` § Planning Docs Commit Gate: produced a clean first commit while the untracked `railspike.txt` stayed out. Retain.
> - `step4_implementation_do.md` § Stage Boundary Protocol: `git status --short` before each commit kept the source file out of stage commits. Retain.
> - Step 3 per-stage \&quot;Early warning / validation\&quot;: made the character-level diff the gate, which caught no drift but did catch a real 360 px overflow in Stage 2 through the width check. Retain.
>
> ### Redundant/unnecessary instructions
> - One commit per stage with the summary update is restated in `RAILSPIKE.md` § Step 4 commit cadence, `step4_implementation_do.md` § Execution Rules and § Stage Boundary Protocol, and `step4_implementation_after.md` item 2. Suggest consolidating.
> - `step4_implementation_after.md` item 6 overlaps the per-stage summary rule. Suggest consolidating.
>
> ### Inapplicable instructions
> - Documentation-only verification clauses in the Do and After files: this was an application change.
> - Migration, role, and database dependency checks in `step4_implementation_after.md` item 5.
>
> ### Uncertain assessments
> - A verification-only final stage (Stage 3) needed its own commit carrying only the summary; the instructions do not say whether that is expected.
> - The instructions have no guidance for a source file that the work depends on but must not commit (`railspike.txt`); a recorded hash was used as the evidence anchor.

### Inspected commit evidence

Repository: `/home/wsl/railspike`. Read-only command: `git show --format=%H%n%s --name-only 87cc921f2a3647aa8960b9f2a4da0ca4e7a3702f`. Retained output:
```text
87cc921f2a3647aa8960b9f2a4da0ca4e7a3702f
feat(stage 3): record release verification

docs/plans/readme_and_essay_homepage/readme_and_essay_homepage_step4_implementation_summary.md
```
Verification-only commit adds summary evidence; it does not establish maintainer approval or deployment.

## C013

**repo_cleanup** — Documentation: repository cleanup and reorganization.

- Context/identity: census C013; source family retained without adding an independent observation. Original-study overlap: R05. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0060](./sources.md#s0060), [S0061](./sources.md#s0061), [S0062](./sources.md#s0062), [S0063](./sources.md#s0063), [S0064](./sources.md#s0064).
- **Request and acceptance:** Revised scope retains files inside docs/launch then docs/maintainers, repairs links and preserves untracked material; older external-archive proposal is superseded (S0062:57–68). Original completion boundary includes maintainer review/merge.
- **Delivery and evidence:** Layout and preservation reported met, but full handoff acceptance is unknown: final summary leaves a maintainer merge-related checklist action and does not establish review/merge (S0064:87–94). Census documented-completion label is not proof every release condition passed.
- **Verification and gates:** Reported three link checkers across 53 files, Git fixture, hashes and scope checks. Untracked preservation was reported, not reconstructed; global authorization/release evidence remains incomplete.
- **Rework and later outcomes:** Summary identifies checklist accidentally omitted from staging due to local ignore rule, then force-added in correction commit 9abcd20. Later docs/maintainers moves are separately requested scope revisions, not another failure (S0064:37–40,66–77).
- **Approval and scope:** Summary says renewed Approved Step 3 was interpreted as covering revised Step 2. Preserve this interpretation without declaring compliance or violation absent conversation. Correction manifest corroborates checklist/summary co-presence.
- **Instruction contribution and effort:** Debug author credits status/link checks, reports repeated cadence rules and ambiguity of renewed approvals (S0060:198–210). No measured effort or total rework count; R05 is the same original-study workflow.
- **Disposition:** Layout evidence is usable; do not assert complete reviewer/merge acceptance. This is a narrower outcome judgment, not an edit to census status. Independent reproduction not performed; human coding review pending.

### Retained evidence

[S0062](./sources.md#s0062), original lines 57–68:

> - **Core requirement 1:** move only the two root files, `HN_POST_DRAFT.md` and `HN_WRITEUP_READINESS_CHECKLIST.md`, into the new directory `docs/launch/`, keeping their names. `docs/case-study-candidates.md` and `docs/positioning-checklist.md` already sit outside the root and stay. No file leaves the repository; `~/railspike-archive/` is not used.
> - **Links:** all references are repaired, including `BACKLOG.md`, `docs/case-study-candidates.md` and the moved files&#x27; own relative links; the earlier &quot;leave the backlog file&quot; direction is superseded.
> - **Allowed files:** the two moves, `BACKLOG.md` (links and pending whitespace fix), `README.md` map, `docs/plans/README.md`, and this feature&#x27;s artifacts.
> - **Success criteria:** the root contains no HN drafts or checklists, the two files exist unmodified under `docs/launch/`, no Markdown link is broken, and `railspike.txt` and `temp/` are byte-identical.
> - **Risks:** dropped backlog items no longer apply since nothing is removed; broken relative links inside the moved files are the new risk, validated by the link checkers.
>
> ## Revision after Step 4 handoff (pending approval)
> The maintainer asked to move `BACKLOG.md` under `docs/` and to organize the `docs/` directory.
> - **Target layout:** `docs/failure-modes.md` (user-facing, stays), `docs/workflow/` and `docs/plans/` (unchanged), and a new `docs/maintainers/` holding `BACKLOG.md`, `RELEASES.md`, `positioning-checklist.md`, `case-study-candidates.md`, and `launch/` (the two HN files, moved from `docs/launch/`). A short `docs/README.md` indexes the four entries.
> - **Links to repair (found by search):** the moved files&#x27; own relative links, `README.md` (backlog link and repository map), and `docs/plans/README.md` wording if needed. `RAILSPIKE.md`, `docs/workflow/`, `scripts/`, `index.html`, and `CONTRIBUTING.md` contain no references and stay unchanged; historical plans mention these files only as text.
> - **Allowed files:** the moves above, the new `docs/README.md`, `README.md`, `docs/plans/README.md`, and this feature&#x27;s artifacts. Nothing else; content of moved files changes only in link paths.
> - **Success criteria:** root has no `BACKLOG.md`; every `docs/` entry is listed in `docs/README.md` and the README map; all three link checkers pass.

[S0064](./sources.md#s0064), original lines 37–40:

>   - Runtime, UI, deployment, and migration checks: not applicable.
> - Notes:
>   - `docs/case-study-candidates.md` and `docs/positioning-checklist.md` were already outside the root and are unchanged.
>   - **Correction:** commit `5be94c9` recorded the checklist as deleted because `.git/info/exclude` (local, line 7) ignores `HN_WRITEUP_READINESS_CHECKLIST.md` by bare name, so the moved file was not staged. The file is intact at `docs/launch/`; it was re-added with `git add -f` in the follow-up commit so it stays tracked as before. The exclude entry was left unchanged and is a maintainer decision.

[S0064](./sources.md#s0064), original lines 66–77:

> ## Revision after the Step 4 handoff
> - The maintainer asked to move `BACKLOG.md` under `docs/` and organize `docs/`. Recorded as pending revisions in Steps 2–3; `Approved Step 3` was given and taken as covering the Step 2 revision, as before. Layout: `docs/maintainers/` for backlog, releases, positioning, case-study candidates, and `launch/`; `docs/README.md` indexes it.
>
> ## Stage 5 - Move files and repair links
> - Changes:
>   - `git mv`: `BACKLOG.md`, `docs/RELEASES.md`, `docs/positioning-checklist.md`, `docs/case-study-candidates.md` into `docs/maintainers/`; `docs/launch/` files into `docs/maintainers/launch/`. No `rm`.
>   - Relative links in the moved backlog and positioning checklist rewritten; the checklist and case-study files needed none.
>   - New `docs/README.md` index; the `README.md` backlog link repointed (done here, not Stage 6, so this commit passes the link checkers).
> - Verification:
>   - Word-level comparison with `HEAD`: the backlog and positioning checklist differ from their previous versions only in link targets; the other four moved files are byte-identical (rename similarity 100%).
>   - Link checkers (Python, Perl, Node): 53 files valid; workflow fixture passed; `git diff --check` clean.
>   - The excluded checklist name stayed tracked because `git mv` moved a tracked file; `git ls-files docs/maintainers/launch` lists both HN files.

[S0064](./sources.md#s0064), original lines 87–94:

>   - Root: `.gitignore`, `.nojekyll`, `CONTRIBUTING.md`, `LICENSE`, `RAILSPIKE.md`, `README.md`, `docs/`, `index.html`, `railspike-logo.png`, `scripts/`, plus local-only `railspike.txt`, `temp/`, `.idea/`. `docs/`: `README.md`, `failure-modes.md`, `maintainers/`, `plans/`, `workflow/`.
>   - Every tracked root file and `docs/` area appears in the README map or `docs/README.md`.
>   - Python, Perl, and Node link checkers: 53 files valid; workflow fixture passed; `git diff --check` clean.
>   - Hashes: `railspike.txt` `575d95c6…` and `temp/` `db5080d1…` match the Stage 1 baseline; `HN_POST_DRAFT.md` `66293b50…` is unchanged.
>   - `docs/plans/` changed only by its index entry and this feature&#x27;s artifacts; `RAILSPIKE.md`, `docs/workflow/`, `scripts/`, `index.html`, and `CONTRIBUTING.md` are unchanged.
>   - Runtime, UI, deployment, and migration checks: not applicable.
> - Notes:
>   - Open for the maintainer: `.git/info/exclude` still ignores `HN_WRITEUP_READINESS_CHECKLIST.md` by name; the tracked file is unaffected. The &quot;Clean up the repo&quot; item in `docs/maintainers/BACKLOG.md` is left unchecked for the maintainer to tick on merge. `railspike.txt` remains untracked.

[S0060](./sources.md#s0060), original lines 198–210:

> - `step4_implementation_do.md` § Stage Boundary Protocol (git status before commit, link checks): confirmed the excluded checklist stayed tracked via `git mv` this time. Retain.
> - Documentation-only verification list (`git diff --check`, scope check, link validation): word-level comparison against `HEAD` proved moved files changed only in link targets. Retain.
>
> ### Redundant/unnecessary instructions
> - No supported findings.
>
> ### Inapplicable instructions
> - Step 4 After item 5 (deployment, release, migration): not applicable to this documentation-only work.
>
> ### Uncertain assessments
> - Stage 5 absorbed the `README.md` backlog link repair planned for Stage 6 so that its commit passed the link checkers; the plan&#x27;s stage boundary was adjusted, not its scope.
> - The instructions do not define how to treat an empty directory left by a move; it was removed with `rmdir`.
> - A second `Approved Step 3` alone was taken as covering the revised Step 2, as in the earlier revision.

### Inspected commit evidence

Repository: `/home/wsl/railspike`. Read-only command: `git show --format=%H%n%s --name-only 9abcd20e9a06d510525494afca31b0db6dab0eea`. Retained output:
```text
9abcd20e9a06d510525494afca31b0db6dab0eea
fix(stage 2): keep readiness checklist tracked at docs/launch

docs/launch/HN_WRITEUP_READINESS_CHECKLIST.md
docs/plans/repo_cleanup/repo_cleanup_step4_implementation_summary.md
```
The correction commit contains the readiness checklist and summary, corroborating a distinct repair event; this does not establish the entire cleanup release.

## C014

**separate_development_content** — Distribution/repository maintenance: separate development content.

- Context/identity: census C014; source family retained without adding an independent observation. Original-study overlap: No named canonical log match in the original study; related supporting references may exist. Workflow era: Railspike-named retained plans; exact instruction revision and execution model unverified. Active human effort unknown; no timed record inspected.
- Sources: [S0065](./sources.md#s0065), [S0066](./sources.md#s0066), [S0067](./sources.md#s0067), [S0068](./sources.md#s0068), [S0069](./sources.md#s0069).
- **Request and acceptance:** Users obtain lean product via copy/clone/submodule, start host plans without companion, and preserve edits through migration/rollback; release requires published repositories and website (S0068:6).
- **Delivery and evidence:** Reported met including remote installation and recovery fixtures; unlike prose-only changes, this record claims actual publication/file-operation checks. That is reported execution, not newly reproduced execution (S0069:20–23).
- **Verification and gates:** Reported same 16 product files across install forms, old-URL refusal, migration/rollback, local-edit/index preservation and HTTP 200 checks. Manual procedure fixtures are not automated-agent sessions; historical-link exceptions remain gaps.
- **Rework and later outcomes:** Initial fixture expected 18 files, corrected to actual 16; later fixture quoting and specific refusal assertion prevented false positives (S0069:18,23). These are test expectation/coverage repairs, not evidence of lost user files.
- **Approval and scope:** Paired product/dev/site commits are recorded; single-repository counts cannot establish or refute full cadence. Inspected development stage contains fixture and summary; prior user authorization remains transcript-dependent.
- **Instruction contribution and effort:** Debug author credits preservation-before-deletion and capability-specific checks, reports repeated reprint overhead and multi-repository bookkeeping ambiguity (S0065:61–76). Actual human minutes and causal contribution unknown.
- **Disposition:** Preserve stronger reported recovery coverage without upgrading it to independent reproduction. Human coding review pending; exact execution model and historical instruction version unverified.

### Retained evidence

[S0068](./sources.md#s0068), original lines 6–6:

> Copy/clone/submodule from `rlspk/railspike` yields the usable product; welcome creates host plans. `rlspk/railspike-dev` owns development records/checks/site. Release requires both published states, working links/site, installation/update/recovery evidence, and preserved local work. No history rewrite, automatic conversion, or new publishing system.

[S0069](./sources.md#s0069), original lines 15–23:

> ## Stage 3 - Deliver the lean product and source transition
> - Changes: Product commit `5985859` removes 73 tracked development/site files, leaving 16 product files. Updated product/development/website links, README inventory, contribution guidance, planning-workspace ownership, source URLs, and routine updates to `main`. Added deliberate migration guidance for legacy copies/submodules with ancestry, provenance, local-edit preservation, and rollback requirements. Product origin is now `rlspk/railspike`; the original origin is preserved as `legacy`.
> - Verification: All three link checkers passed on an isolated product snapshot (14 Markdown files); the adapted Git workflow fixture passed against the exact new README block. Actual local copy, clone, and submodule fixtures each contained the same 16 product files without development/site content. A manual welcome/instruction walkthrough wrote a Step 1 artifact under the host&#x27;s `docs/plans/` without the companion checkout. All seven unrelated untracked files matched their pre-migration hashes; `git diff --check` passed.
> - Notes: The initial inventory assertion expected 18 files; inspection established the correct 16-file list and the corrected assertion passed. This was a fixture expectation correction, not a removed requirement. The product stage commit removes its temporary summary as approved; this companion summary is canonical. Fresh remote verification and legacy migration/recovery exercises remain Stage 4 work.
>
> ## Stage 4 - Release and prove recovery
> - Changes: Published the lean product on `rlspk/railspike` main and feature branches at `59858599cf98d3d5e0502fc13e58a856e364df12`, preserving original history. Published development changes through `2154cfd`; website remains at `05aebc7`. Added a reproducible Python 3 fixture for actual remote installs and legacy migration/recovery; documented the release in the preservation record.
> - Verification: `python3 scripts/check-repository-separation.py https://github.com/rlspk/railspike.git b59f7df89842ba17f710ae1f2dc955bb361cc620` passed: fresh remote clone/submodule and complete copy contain 16 product files, old-source guards refuse routine updates for the expected URL reason, deliberate submodule migration preserves ancestry and supports subsequent routine updates, copy migration preserves local notes and a locally authored plan, failed-copy verification restores the exact prior contents/provenance, and submodule rollback restores URL/settings/revision and clean host state. Unrelated staged/unstaged host work stays intact. Separate all-runtime link checks and the Git workflow fixture passed; final public repository, workflow/welcome/contribution pages, new website/logo, and legacy website checks returned HTTP 200. The real product tracked tree/index are clean and all seven unrelated untracked files retain their original hashes.
> - Notes: During fixture review, quoted temporary paths and asserted the specific old-URL refusal to avoid a false positive from shell parsing; reran successfully. Copy-update and welcome fixtures exercise documented manual procedures, not a new installer or an automated agent session. No new application runtime, database, CI, or publishing system was introduced. The companion is the canonical plan/log workspace; local untracked drafts remain in the original checkout for the user&#x27;s later disposition.

[S0065](./sources.md#s0065), original lines 61–76:

> - `docs/workflow/step4_implementation_before.md`, Planning Docs Commit Gate: feature branch and planning commit `b59f7df` preceded implementation; inspection confirmed exactly the approved Steps 1–3, existing log, and plan-index update, with no Step 4 summary. Retain the explicit inspection gate.
> - `docs/workflow/step4_implementation_do.md`, Stage Boundary Protocol: preservation was published and verified through a fresh clone before any product deletion. Stage commits and corresponding summary records are present across the product, development, and website repositories. Retain verification and commit boundaries; the approved cross-repository convention made ownership explicit.
> - `docs/workflow/step3_development_plan_do.md`, material risks block dependents: actual checks distinguished working Git credentials from unavailable API authentication. The user then supplied a third repository with Pages already enabled; website publication and live asset verification resolved the hosting dependency before source removal. Retain capability-specific verification rather than treating one authentication failure as universal loss of access.
> - `RAILSPIKE.md`, Plan review / scope reconciliation: recorded the user&#x27;s third repository in the current plans and summary and assigned website ownership there. This was an explicit user direction, not an inferred expansion or an extra approval request. Retain durable recording of steering without repeating already granted authorization.
> - `docs/workflow/step4_implementation_after.md`, Completion Contract and external verification: checked actual remote copy/clone/submodule contents, the live website and legacy site, old-source refusal, deliberate source migration, local-edit preservation, and rollback. The canonical summary distinguishes manual-procedure fixtures from an automated installer/agent run. Retain this evidence boundary.
> - `RAILSPIKE.md`, Railspike Debug Mode / Persistent debug log: retained previous log entries through migration, inherited enabled mode into the summary, and saved this completed-step report only after stage completion in a separate log-only handoff commit. Retain append-only reporting and quiet handoffs.
>
> ### Redundant/unnecessary instructions
> - `RAILSPIKE.md`, How to Use This Chain / reprint and Step 4 phase instructions: three full phase reprints repeated requirements already read during execution, producing substantial conversational overhead relative to progress updates. The earlier finding remains supported by this step. Consolidate the duplicate requirement and consider linked acknowledgments for unchanged phases; required reprints were followed.
>
> ### Inapplicable instructions
> - `docs/workflow/step4_implementation_after.md`, documentation-only and application runtime checks: this was approved distribution/repository maintenance with live website publishing, so a blanket documentation-only exemption would be wrong. Database and application-runtime checks were inapplicable; real Git, file, migration, link, and website checks were performed. Retain checks proportional to the approved artifact.
>
> ### Uncertain assessments
> - `RAILSPIKE.md`, commit cadence and summary location: the source product intentionally removes its own temporary plans/summary, while development retains the canonical record. The approved plan&#x27;s paired-commit convention was followed: product preservation `0e845a1`, product separation `5985859`, development stage commits `ceefc04`/`171916e`, `cfa8268`, `2154cfd`, `69fb1b9`, and website stage commit `05aebc7`. A single-repository commit-count check would misdescribe this work; clarify the general multi-repository rule rather than relying on future ad hoc interpretations. Product repository-boundary guidance now identifies the separate development workspace as authorized by this feature.
> - `docs/workflow/step4_implementation_after.md`, verification gates: the baseline-aware link checks acknowledge 80 exact historical targets from preserved research and excluded untracked source files. New missing targets and stale baseline entries fail, but this is not proof that historical source links are navigable. Keep the explicit limitation and retain original evidence rather than silently editing quotations or broadly excluding the research directory.

### Inspected commit evidence

Repository: `/home/wsl/railspike-dev`. Read-only command: `git show --format=%H%n%s --name-only 69fb1b90a2d21b6f6e98ca69b89e81df1f3892da`. Retained output:
```text
69fb1b90a2d21b6f6e98ca69b89e81df1f3892da
test(stage 4): verify published split and migration recovery

README.md
docs/maintainers/REPOSITORY_SPLIT.md
docs/plans/separate_development_content/separate_development_content_step4_implementation_summary.md
scripts/check-repository-separation.py
```
The development release-stage manifest includes the separation fixture, preservation docs and summary; the tool was not executed during this analysis.
