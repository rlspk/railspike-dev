> **Feature plan:** [Step 2](./welcome_guidance_question_step2_feature_description.md) · [Step 3](./welcome_guidance_question_step3_development_plan.md) · [Step 4](./welcome_guidance_question_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/welcome_guidance_question`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.30**

Step 1 skipped: the maintainer chose the approach ("1") from three options offered in conversation on 2026-10-28.

- **Option 1 (chosen):** ask the AGENTS.md question on its own first.
- **Option 2:** combine both questions and require both answers.
- **Option 3:** keep the current flow and add one later reminder.

The options are not reproduced as a Step 1 artifact. Related earlier work: [prompted installation](../prompted_installation/prompted_installation_step1_solution_assessment.md), which introduced the welcome.

## Problem

After installation, the welcome puts the optional AGENTS.md offer in the same turn as "What would you like to work on first?". Users answer the task question, and the offer silently counts as declined, so the persistent default is lost by being overlooked rather than by an explicit choice. The maintainer saw this when installing `v0.4.0-beta.2` (`5952bfd`) into another project.

## User stories

- As a new user, I want the AGENTS.md question asked on its own, so that I make a real choice instead of missing it.
- As a new user who answers with a task anyway, I want to be told that the guidance wasn't added and how to add it later, so that I'm not surprised when a later session doesn't use Railspike.
- As a user who already gave a task in the install request, I want that task kept and started right after I answer, so that I don't have to repeat it.

## Core requirements

- The welcome ends its first turn with only the AGENTS.md yes/no question. The first-task question waits until that question has been answered or bypassed.
- A clear yes leads to the existing consent-based edit. A clear no is honored, with no repeated offer.
- If the user replies with a task or anything else that doesn't answer the question, the agent treats it as "not now": it does not edit AGENTS.md, says so in one line ("AGENTS.md: not added; ask any time to add it"), and continues with the task. It does not ask again in that session.
- The welcome reports the outcome explicitly as one of: added, declined, or not answered.
- A task supplied with the installation request is preserved. It is acted on after the guidance question, without asking for the task again.
- An existing Railspike section in AGENTS.md still leads to an update proposal, not a duplicate. Accepting the guidance still supplies neither a task nor a step approval.

## Delivery scope

- **Work type:** documentation-only product change. The product is Markdown instructions.
- **Allowed files:**
  - `railspike/WELCOME.md`;
  - `railspike/README.md`, limited to the Quick start welcome sentences (currently lines 67 and 71);
  - this cycle's `railspike-dev` records (plans, debug log, plan index, ledger row, scenario verification record);
  - `v0.4.0-beta.3` release notes and publication record, if a release is requested.
- **Audience and outcome:** coding agents that follow the welcome, and users reading the Quick start. Every new install then asks the guidance question on its own.
- **Not permitted:** runtime, script, or other workflow-file changes. Installation, update, and uninstall procedures are not changed.

## Completion boundary

- **Document completion:** `WELCOME.md` and the README sentences state the new order and the three outcomes consistently.
- **Correction path:** revise the documents; installed copies update through the existing reviewed upgrade process.
- **Handoff:** product branch with stage commits. Merge, tag, and release require separate explicit requests.

## Known user and environment

- **User and environment:** the maintainer installs Railspike into another project with their coding agent, using the homepage install prompt.
- **Failure to handle:** the guidance offer and the task question arrive in the same turn, and the offer is overlooked.
- **Unaided next action:** after the fix, the user sees one question ("Add this to AGENTS.md? yes/no"). If they answer with a task instead, they are told the guidance was not added and how to add it later.
- **Verification and retry:**
  - a scenario walk-through of the revised instructions covering yes, no, task-instead, an existing AGENTS.md section, and a task supplied with the install request;
  - then a live reinstall by the maintainer in a disposable project.
- **Evidence:** the scenario record now, plus the maintainer's live transcript when it is available. Until then, live agent compliance stays unverified.

## Risks

- **Over-blocking.** Impact: users who just want to start feel stalled. Early validation: the task-instead scenario. Mitigation: only one question, and any non-answer proceeds immediately with a one-line note.
- **Contradiction with the existing "do not block" text.** Impact: agents follow the old rule. Early validation: a grep of `WELCOME.md` and the README for "unanswered" and "block" after editing. Mitigation: replace the rule rather than add to it.
- **Welcome length.** Impact: the question gets buried again. Early validation: count the lines in the revised first turn. Mitigation: the question is the welcome's final line, with nothing after it.

## Shared component inventory

- `WELCOME.md` "Offer optional project guidance" and "Invite the first task" are the canonical sections. They are edited in place and their order is restructured; no new file.
- README Quick start steps 1 and 2 describe the welcome. They are updated to match and do not copy the instructions.
- The uninstall section's reference to "the `## Railspike` section that welcome offered" is unchanged; the guidance text itself is unchanged.

## User flow

1. Installation completes and the agent gives the brief welcome.
2. The agent shows the proposed AGENTS.md text and asks only whether to add it.
3. The user replies yes, no, or something else, such as a task.
4. The agent acts on that reply (edits, honors the decline, or notes "not added") and reports the outcome in one line.
5. The agent asks for the first task, or starts the task the user already gave.

## Success criteria

- No path in the revised `WELCOME.md` asks for a task in the same turn as the guidance question.
- The scenario record covers yes, no, task-instead, an existing section, and a task supplied with the install request, with a pass for each.
- No remaining text says that an unanswered offer is silently skipped without reporting the outcome.
- The product link check and the Git-workflow fixture still pass.

## Scope and estimate history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| 2026-10-28 — Intake | 0.30 | Restructure the welcome's guidance offer, update the README sentences, scenario verification, and a likely beta. Exposed rater: `WELCOME.md` was read during earlier work, and the problem was analyzed in conversation before scope was fixed. Single Claude Code rater, R1/P2; R1 hashes verified this session. |
| 2026-10-28 — Step 2 handoff, v1 | 0.30 | Reaffirmed. Comparable to the 0.25–0.35 R1 references (a small surface change with preserved behavior). Release work, if requested, is included. |

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*
