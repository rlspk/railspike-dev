> **Feature plan:** [Step 1](./epic_checklists_step1_solution_assessment.md) · [Step 2](./epic_checklists_step2_feature_description.md) · [Step 3](./epic_checklists_step3_development_plan.md) · [Step 4](./epic_checklists_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/epic_checklists`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.60** (revised from 0.55)

## Problem

Railspike never says how to move a cycle into a new chat, so the maintainer asks for "a prompt block" and each agent improvises it. Epics need this most, and Railspike has no record type for them, so v3 has improvised six epic checklists in six slightly different ways.

## User stories

- As the maintainer, I want to end a long chat with one copyable prompt so that a new chat continues the same cycle without my re-explaining it.
- As an agent in a new chat, I want the prompt to point at a pushed record so that I restore state from files, not from the prompt's claims.
- As the maintainer running an epic, I want one checklist format so that I can see which cycle is next, in which mode, and how far each cycle has got.
- As an agent starting an epic item, I want to know that the checklist's mode mark is a lean so that I still get real authorization for that cycle.

## Core requirements

- **Handoff prompt, any cycle.** On request, the agent commits and pushes the cycle's current plans to its feature branch. It then gives one fenced code block. The block names the repository, branch, base commit, plan or checklist path, cycle, step and mode, and what is approved and what is not. It tells the new chat to read `AGENTS.md` and the plan, check the branch against `origin/main`, and continue. "A prompt block" and "a prompt to continue in a new chat" count as the same request.
- **Approval stays in the record.** The prompt repeats only approvals the record shows and never grants one. An unapproved draft may be pushed in a separate commit whose message says "draft, not approved". The approval commit gate still applies when approval arrives.
- **Epic checklist file.** `docs/workflow/epic_checklist.md` defines a coordination record that approves nothing. Its template has: preamble, Resume here, reuse inventory, items, decisions, open questions, later. Each item has a stable ID, a mode lean, a status line in layers (merged, deployed, checked, accepted) and links both ways. The checklist also has one field for who approves steps, an MVP line, and rules for added, cut and superseded items. Estimates carry a "do not sum" note.
- **Step 1 decisions settled here.**
  - An agent suggests an epic when a Step 1 estimate goes above 1.0, and creates one only on request.
  - Each epic cycle counts as its own study outcome, linked to the epic; the split rule for one cycle stays unchanged.
  - Writing the checklist is a documentation-only one-shot.
  - A request for a handoff prompt authorizes the commit and the push to the feature branch only, never to `main`, a merge or a PR.
- **Short.** `RAILSPIKE.md` grows by no more than 150 words. The epic file stays under one page plus its template.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Delivery scope and completion boundary

**Documentation-only.** Allowed in `railspike`: `RAILSPIKE.md` (a short Handoff prompts section and an Epics pointer), new `docs/workflow/epic_checklist.md`, `docs/workflow/step1_solution_assessment.md` (the /new reminder and the 1.0 split note), `docs/workflow/one_shot.md`, `docs/effort-estimation.md` (epic counting), `docs/failure-modes.md` (one resume case), `README.md` and `docs/README.md` (index lines). Allowed in `railspike-dev`: this cycle's folder, its `docs/plans/README.md` entry, `docs/concepts/planning.md`, and append-only ledger rows. No application, CI, website, release or v3 change is permitted. Updating old v3 checklists is out of scope.

Reader outcome: an agent asked for a handoff prompt produces a correct, pushed handoff, and an agent asked for an epic writes a checklist from the template. Completion means every allowed file is edited, all changed links resolve, `git diff --check` passes, and the word bound holds. Replays against the hn_theme handoff and the notifications, pledges and backlog checklists show the rules cover them. Wrong rules get corrected in a later cycle; nothing breaks at runtime. Handoff is a reviewed branch, not a merge or release.

## Known user and environment

The maintainer, in a Claude chat working on v3, types "please write a prompt block to continue this in a new chat". The block is pasted into a new Claude or Codex chat. The failure to handle: the new chat finds no pushed branch, or a branch behind `origin/main`. Its unaided next action is to say which, and to fetch or rebase as the record allows before continuing. Success shows as the new chat naming the right next step. One real v3 handoff after release is the evidence; it stays pending at closeout.

## Risks and early validation

| Risk / impact | Early validation and mitigation |
| --- | --- |
| Pushing unapproved drafts blurs the approval commit gate. | Draft commits are separate and labeled; check the gate text still requires its own approval commit. |
| The prompt states an approval the record lacks, and a new chat acts on it. | The rule says the record wins; the replay checks that a prompt built from each sample record claims nothing extra. |
| The epic template is too heavy for a three-cycle epic. | Mark only Resume here and items as required; replay against the three-cycle backlog checklist. |
| Agents miss the new file. | Link it from `RAILSPIKE.md`, Step 1 and `one_shot.md`; verify each link. |

## Shared instruction surfaces and reuse

- `RAILSPIKE.md` Follow-up Cycles Before Merge and the approval commit gate: reused for branch and commit rules; the handoff rule adds push only.
- `one_shot.md` resumption rules and `failure-modes.md` resumed-state cases: reused for what a new chat restores.
- Step 1 "/new or /clear" reminder: gains one clause pointing at handoff prompts.
- `effort-estimation.md` split rules: unchanged; epic counting is one added sentence.
- v3 `notifications_checklist.md`, `pledges_checklist.md`, `backlog_checklist.md`: the template's source, read at `2d7805c8`.

**Concepts touched:** [Planning record](../../concepts/planning.md#planning-record) changed; [Approval and scope boundary](../../concepts/planning.md#approval-and-scope-boundary) changed (push for handoff prompts, labeled draft commits). Added: epic checklist; handoff prompt.

## Simple user flow

1. The maintainer asks for a handoff prompt at any point in a cycle.
2. The agent commits and pushes the plans, then gives one code block.
3. The maintainer pastes it into a new chat.
4. The new chat reads `AGENTS.md` and the plan or epic checklist, checks the branch, and names the next action.
5. For an epic, the new chat starts the next item as its own cycle with its own authorization.

## Success criteria

- A replay of the hn_theme handoff produces a prompt that has every required field and no unrecorded approval.
- The notifications, pledges and backlog checklists each fit the template without losing information, and each gap from the Step 1 review has a rule.
- All four Step 1 decisions appear in the product text.
- Net `RAILSPIKE.md` growth is 150 words or fewer, by `wc -w`.

## Study history and status

2026-11-24T17:30:00Z — Step 2 handoff, scope v3, R1/P2, Claude single exposed rater. Step 1 approved by the maintainer ("approved step 1") and committed as `9f8f994` on `feat/epic-checklists`. Scope adds labeled draft commits and settles the four Step 1 decisions. Projection revised 0.55 → 0.60: the draft-commit exception touches the approval commit gate. Earlier values retained in Step 1. Approval pending; no implementation.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*
