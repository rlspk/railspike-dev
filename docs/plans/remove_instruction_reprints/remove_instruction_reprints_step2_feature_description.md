> **Feature plan:** [Step 1](./remove_instruction_reprints_step1_solution_assessment.md) · [Step 2](./remove_instruction_reprints_step2_feature_description.md) · [Step 3](./remove_instruction_reprints_step3_development_plan.md) · [Step 4](./remove_instruction_reprints_step4_implementation_summary.md)

Debug mode: disabled

# Task-relevant instruction summaries

## Problem
Required instruction-file reprints duplicate content without demonstrating understanding or adherence. Users need a concise view of the agent's interpretation before work proceeds.

## User stories
- As a workflow user, I want a brief summary of the upcoming action, relevant constraints, and approval gate so that I can spot misunderstandings before work proceeds.
- As a returning user, I want instructions reread and state restored without repeating an unchanged summary so that resumption stays useful and concise.

## Core requirements
- Replace automatic full reprints with a brief task-relevant summary after reading the applicable instructions and before acting. Cover the next action, relevant constraints, and any approval gate; do not summarize the entire file or add a separate reading acknowledgment.
- Summarize again only when the next action, relevant constraints, or approval gate changes. An unchanged step/phase entry or resumption does not itself require repetition. When prior summary context cannot be recovered, establish a fresh summary after restoring the applicable instructions and state.
- Original instructions remain authoritative, including exceptions omitted from summaries. Preserve required reading, step/phase order, state restoration, approval gates, and commit rules. Missing or unreadable instructions require a clear blocker; a summary cannot substitute for reading.
- Preserve useful progress/handoff updates, explicit requests to show instructions, and relevant quotations needed to explain a concrete decision or blocker. The policy governs assistant-authored repetition, not ordinary tool-output rendering.
- Apply the same summary contract with debug enabled or disabled; preserve diagnostic logging and recovery behavior without treating summaries as debug reports.

## Delivery scope and shared surfaces
**Work type:** documentation-only, for Railspike users and agents. Allowed product files are `RAILSPIKE.md`, `README.md`, `docs/workflow/step3_development_plan_before.md`, and `docs/failure-modes.md` in `~/railspike`. Extend the canonical instruction contract and align setup, troubleshooting, debug, and recovery references. No UI/API surfaces apply.

Workflow bookkeeping in `railspike-dev` is limited to this feature's plans, implementation summary, optional debug log, organization under `docs/plans/remove_instruction_reprints/`, its plans-index entry, and necessary reference repairs. Preserve historical plans/logs. Application/runtime, tests, CI, deployment, generated-artifact, and website changes are not permitted.

## Risks
- **Lost constraints:** Compression could obscure exceptions or approval gates. Review representative summaries before Step 3; retain source authority and require relevant constraints and gates before acting.
- **Conflicting guidance:** Existing reprint advice could restore duplication. The Step 2 reference scan identifies the four allowed product files; recheck coverage before Step 3 and align every active reference with the canonical policy.
- **Repetition or skipped recovery:** Resumption could trigger needless summaries or encourage reliance on stale context. Validate unchanged, changed, and unavailable prior-context scenarios before Step 3; preserve rereading/state restoration and use a fresh summary when prior context is unavailable.

## Simple user flow
1. Enter a step or phase; the agent reads applicable instructions and restores workflow state.
2. Before acting, the agent briefly summarizes the next action, relevant constraints, and approval gate when new or changed, then performs only authorized work.
3. Resume or transition with the same rules; correct misunderstandings and honor existing approval gates.

## Completion boundary and success criteria
Deliver consistent active guidance across the allowed files. Scenario checks must cover first entry, changed and unchanged transitions/resumptions, unavailable prior context, missing/unreadable instructions, explicit reprint requests, necessary rule quotations, and both debug modes. Routine cases produce zero full assistant-authored reprints, a brief summary before new or changed work, and zero redundant summaries for unchanged recoverable context. Verify unchanged approval/commit obligations, document integrity, links, and allowed file scope; record evidence in Step 4. Correct conflicting guidance or broken links before handoff. These checks establish the instruction contract, not guaranteed compliance by every agent.
