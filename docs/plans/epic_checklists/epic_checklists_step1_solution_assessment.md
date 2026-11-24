> **Feature plan:** [Step 1](./epic_checklists_step1_solution_assessment.md) · [Step 2](./epic_checklists_step2_feature_description.md) · [Step 3](./epic_checklists_step3_development_plan.md) · [Step 4](./epic_checklists_step4_implementation_summary.md)

Debug mode: enabled (host marker present at intake).
Effort study: `railspike-effort` / `railspike/epic_checklists`; [standing enrollment and ledger](../../research/effort_estimation/collection.md).
Extended estimates: enabled.

**Cycle estimate: 0.55** (revised from 0.45)

## Original Query

Hi Claude, I want to check how Railspike currently handles epics that have more than one cycle that may have combinations of one-shot and full cycles. We've done a few of these in v3 now, but I don't think Railspike explicitly codifies how to do it, and maybe it should?

[After the review below:] Yes, write Step 1 please.

[After Step 1:] So one of the main use cases for epics so far has been being able to resume the epic in a new chat, avoiding long chats. I typically do this by saying, "please write a prompt block to continue this in a new chat". Does our plan so far cover that? [After the answer:] Please revise.

[After the revision:] Is there a better name we can use for the prompt block? It seems confusing because of the word block, but I use the word block to ensure the agent puts it as a code block that's easy to copy. [After the suggestions:] Please rename.

## Understood Intent

Decide whether and how Railspike should define work that spans several cycles, some one-shot and some staged. The review found no such rule in the product. Railspike has splitting hints, a follow-up rule for one reused branch, and split-counting rules for the effort study. v3 has invented a working pattern: at least six `docs/plans/*_checklist.md` files (notifications, pledges, backlog, browsing tree, nav speed, read-model rebuild). Their shared parts work well. Their differences cause ambiguity. A main reason for an epic is to resume it in a new chat and keep chats short. The maintainer asks for "a prompt block to continue this in a new chat", and the pledges session log shows what each resume needed: a pushed plan, a branch check against `origin/main`, and a stated next action. Railspike says nothing about this prompt, called a **handoff prompt** below. Single cycles use them too, such as after hn_theme Step 1. This request authorizes Step 1 only.

## Problem

Railspike defines one cycle at a time and never says how to hand work to a new chat. So each v3 epic has improvised how it tracks cycles and how a new chat picks it up.

## Option A — Keep the rules in v3 for a trial

**Estimate: 0.15**

Write the epic rules into v3's `AGENTS.md` and adjust its existing checklists, as we did with quickfix. Railspike stays unchanged until the trial settles.

- Pros: smallest change; no product release needed.
- Cons: v3 has already run six epics, so another trial teaches little. Handoff prompts would stay a v3 habit. Other host projects still get nothing. The one-shot authorization question is a Railspike rule, so a host-only answer stays unofficial.
- Driver/uncertainty: bounded editing; reconciling six old checklists could grow scope.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Option B — A handoff rule for every cycle, plus an epic checklist file (recommended)

**Estimate: 0.55** (revised from 0.45)

First, add a handoff rule for any cycle. When the user asks for a handoff prompt, the agent commits and pushes the current plans. Then it writes a short prompt that names the repository, branch, base commit and plan path. The prompt names the cycle, its step and mode, and what is approved and what is not. It tells the new chat to read `AGENTS.md` and the plan, check the branch against `origin/main`, then continue. The prompt repeats only approvals the record shows, so it never grants approval itself. The agent always delivers it as one fenced code block, so it copies cleanly. Requests for "a prompt block" or "a prompt to continue in a new chat" count as the same request.

Second, add `docs/workflow/epic_checklist.md` with the rules and a short template, taken from what the v3 checklists already agree on. The template opens with a "Resume here" section: the next cycle and step, what it waits on, the branch, and the last session date. An epic's handoff prompt points to the checklist first. An epic checklist is a coordination record. It approves nothing, and each item stays its own cycle. Link it from `RAILSPIKE.md`, the Step 1 split guidance and `one_shot.md`. Fill the gaps the review found: a mode lean per item that is not authorization; a stable item ID; status kept in separate layers (merged, deployed, checked, accepted); one field for who approves steps; an MVP line; rules that keep cut, added and superseded cycles visible; backlinks from each cycle's first artifact; estimates marked as not to be summed; how the effort study counts epic cycles.

- Pros: one written pattern for every host. New chats resume from the record instead of a long chat. It answers the authorization question where it belongs. Its rules come from six real epics.
- Cons: another file for agents to find. Too many required fields would make small epics heavy. Old v3 checklists would not match until updated.
- Driver/uncertainty: the effort-study counting rule, the push rule, and keeping both templates short. Live agent compliance cannot be proved by document checks.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Option C — A gated epic artifact

**Estimate: 0.85**

Make the epic a planning step of its own, with an `Approved Epic` gate and a commit. Its approval would cover the cycle list and order. Cycles would then inherit scope from it.

- Pros: strongest record; clear authority over the cycle list.
- Cons: more ceremony than v3 needed. It conflicts with the "approves nothing" rule that kept v3 epics flexible, such as the pledges replan. Inherited scope blurs per-cycle approval.
- Driver/uncertainty: new gate rules touch approval, commit and study instructions in many places.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Recommendation and boundary

Choose B as one documentation-only slice. A user can end any chat with a handoff prompt, and a new chat continues correctly from the pushed record. An agent can write an epic checklist from the template and apply the same rules to every item. Step 2 should settle four choices. First, when to offer an epic: on request, or when a Step 1 estimate goes above 1.0. Second, whether each epic cycle counts as an independent study outcome. Unlike a split, each epic cycle has its own scope and approvals. Third, whether writing the checklist is itself a cycle. v3 writes it as a documentation-only one-shot. Fourth, whether a request for a handoff prompt authorizes the push. Today one-shot authority excludes push.

Exclude a gate for epics, automatic handoff prompts the user did not ask for, changes to cycle approval or commit cadence, updates to the old v3 checklists, website work and release publication. Product edits belong in `../railspike`; plans and study records belong here. No implementation is authorized yet.

**Concepts touched:** [Planning record](../../concepts/planning.md#planning-record) changed; [Approval and scope boundary](../../concepts/planning.md#approval-and-scope-boundary) used unchanged. Proposed additions: epic checklist, a record that coordinates several cycles and approves none of them; handoff prompt, a pasteable prompt in one code block that points a new chat at the record. "Handoff" here means this prompt, not the agent's end-of-step message.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

## Study history and status

2026-11-24T17:10:00Z — scope v1, R1/P2, Claude single exposed rater. Intake is missing: the review of Railspike and six v3 checklists came first. First recorded projection is this Step 1 handoff: A 0.15; B (recommended cycle) 0.45; C 0.85. Each covers its whole alternative, including planning, documentation, checks and ordinary correction. Starting revisions: development `dd45cb9c7b38951885f6153c2ed1602a7dddb247`, product `3cd8580569cc6665bcdd21ca2e85422182a724e0`, v3 evidence `2d7805c8b6d63b0f2ff6ecdd264ec257eaece23b`. All three [frozen R1 sources](../../research/effort_estimation/references/R1/manifest.json) hash-verified. B sits just below `shared_implementation_standards` (0.50), a comparable new workflow file with links across entry points. Values are scope judgments, not time; do not sum them. Approval pending; no implementation.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

2026-11-24T17:20:00Z — Revision, scope v2, same rater and references, exposed. The maintainer said resuming in a new chat is a main use of epics and asked to revise. B now adds a prompt-block handoff for every cycle and a "Resume here" section in the epic template. A 0.15 and C 0.85 reaffirmed; B and the cycle revised 0.45 → 0.55 for the added handoff rule and push question. v1 values retained above. Approval pending; no implementation.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*

2026-11-24T17:25:00Z — Revision, scope v2 unchanged. The maintainer found "prompt block" confusing and asked to rename it. Renamed to **handoff prompt**; the code-block format is now a rule, and the old phrasings still count as the request. Wording only; all estimates reaffirmed (A 0.15, B 0.55, C 0.85). Approval pending; no implementation.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*
