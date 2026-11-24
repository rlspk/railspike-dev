# epic_checklists verification

Stage 4 replays for [`railspike/epic_checklists`](./epic_checklists_step4_implementation_summary.md). Sources: v3 at `2d7805c8`, product `feat/epic-checklists` at `a6e96e2`. These are self-review against recorded artifacts, not a live new-chat test.

## Handoff prompts built from four records

Each prompt below follows [Handoff prompts](../../../../railspike/RAILSPIKE.md#handoff-prompts). "Fields" means repository, branch, base commit, plan or checklist path, cycle, step, mode, approved and not approved, and the new chat's checks.

### 1. hn_theme, after Step 1 (the original "prompt block" case)

```text
Continue Railspike cycle v3/hn_theme in gulkily/v3.
Branch: <the cycle's branch>, base origin/main 7d9b4b4d.
Plan: docs/plans/hn_theme_step1_solution_assessment.md (staged, Step 1).
Approved: nothing yet. Not approved: Step 1. The Step 1 commit is labeled "draft, not approved".
Read AGENTS.md and the plan, check the branch against origin/main, then wait for "Approved Step 1".
```

- Fields: all present. The Step 1 record does not name its branch, so the replay leaves a placeholder; the agent knows it at handoff. Finding: the first artifact could record the branch, but that is outside this cycle. Passed.
- The maintainer asked for Step 1 "committed and pushed" before approval. The labeled draft commit now covers this; before this cycle it broke the approval commit gate. Passed.
- Claims: none beyond the record. Passed.

### 2. notifications checklist

```text
Continue the v3 notifications epic in gulkily/v3.
Branch: main at 2d7805c8. Checklist: docs/plans/notifications_checklist.md.
Next: item 2 push_subscribe (staged lean), Step 1 not written.
Approved: items 0 and 1 merged. Not approved: any step of item 2.
Read AGENTS.md and the checklist, check the branch against origin/main, then start item 2 as its own cycle.
```

- Fields: all present. Passed.
- Claims: push_subscribe Steps 1–3 were approved in a later session, but the checklist at `2d7805c8` marks it only "next". The prompt follows the record and claims nothing. This is the case the "record wins" rule exists for. Passed.
- Template fit: preamble, reuse inventory, items with modes and estimates, MVP line, after-MVP, open questions all map. Resume here is missing today; "next" on item 2 holds its content. Item 1's merged, deployed and real-phone lines match the status layers. No information lost. Passed.

### 3. pledges checklist

```text
Continue the v3 pledges epic in gulkily/v3.
Branch: main at 2d7805c8. Checklist: docs/plans/pledges_checklist.md.
Next: none planned. Items 1–3, 5, 8–12 built; 4 and 7 cut; 6 parked.
Approved: the maintainer approves every step. Not approved: anything for item 6.
Read AGENTS.md and the checklist, check the branch against origin/main, then ask which release checks to run.
```

- Fields: all present. Passed.
- Template fit: item 8 between 3 and 4 matches "stable IDs"; struck items 4 and 7 match "keep history"; the 2026-11-17 replan with the maintainer's words matches; cycle 1's one-time delegation matches the approver line. The dated session log has no template section; "add the other sections when they have content" allows it. No information lost. Passed.
- Finding: the session log is long because Resume here does not exist; the next session had to read it to find its place. Resume here addresses this.

### 4. backlog checklist

```text
Continue the v3 backlog epic in gulkily/v3.
Branch: main at 2d7805c8. Checklist: docs/plans/backlog_checklist.md.
Next: item 2 backlog_claims (staged), Step 1 to write. Item 1 merged and deployed; acceptance pending.
Approved: item 1 Steps 1–3. Not approved: any step of item 2.
Read AGENTS.md and the checklist, check the branch against origin/main, then write item 2 Step 1.
```

- Fields: all present. Passed.
- Claims: item 2 Steps 1–2 were approved in a later session; the checklist at `2d7805c8` shows them unchecked, so the prompt claims nothing. Passed.
- Template fit: three items fit; the two follow-up one-shots under item 1 match "follow-ups nest"; "Maintainer accepts" matches the accepted layer. No information lost. Passed.

## Known-user failure replays

| Case | Instruction that applies | Next action stated | Result |
| --- | --- | --- | --- |
| New chat given prompt 1, branch never pushed | [Failure modes: missing or stale branch](../../../../railspike/docs/failure-modes.md#a-handoff-prompt-points-at-a-missing-or-stale-branch) | Say the branch is missing; ask the user to push it or paste the plan | Passed |
| New chat given prompt 2, branch behind `origin/main` | Same | Say it is behind; fetch and rebase only when the record allows, otherwise ask | Passed |
| Prompt claims an approval the record lacks | Same, and "the record wins" | Treat the approval as absent and ask for it | Passed |

## Gaps from the Step 1 review

| Gap | Rule in `epic_checklist.md` | Result |
| --- | --- | --- |
| 1 Mode per item, authorization | Mode is a lean; `one_shot.md` line | Covered |
| 2 Status layers | Status in layers | Covered |
| 3 Approval delegation | Approver | Covered |
| 4 Stable numbering | Stable IDs | Covered |
| 5 Cuts, replans, supersession | Keep history | Covered |
| 6 Nested follow-ups | Follow-ups nest | Covered |
| 7 Estimates not summed | Estimates | Covered |
| 8 MVP line | MVP line | Covered |
| 9 Backlinks | Links both ways | Covered |
| Resume in a new chat | Resume here; Handoff prompts | Covered |

## Not verified

- A live handoff: a new Claude or Codex chat given a real handoff prompt after release. Pending.
- Push: this session has read-only access, so no branch was pushed and the push step was not exercised.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*
