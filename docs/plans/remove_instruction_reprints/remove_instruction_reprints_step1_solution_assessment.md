> **Feature plan:** [Step 1](./remove_instruction_reprints_step1_solution_assessment.md) · [Step 2](./remove_instruction_reprints_step2_feature_description.md) · [Step 3](./remove_instruction_reprints_step3_development_plan.md) · [Step 4](./remove_instruction_reprints_step4_implementation_summary.md)

Debug mode: disabled

## Original Query
Let's pause this and implement a smaller feature. I want to stop redundant echoing back of a file we just read. Please write Step 1 for that, after necessary git operations.

## Understood Intent
Replace Railspike's required instruction-file reprints with brief task-relevant summaries of the next action, relevant constraints, and any approval gate. Repeat a summary only when those change. Keep the actual reading, step/phase order, approval gates and useful task updates. The exploratory paper is paused on its own branch before implementation.

## Problem
Railspike repeatedly requires instruction reprints, adding conversational duplication without establishing that the agent understood or followed the file.

## Evidence and Boundary
- `RAILSPIKE.md` requires reprinting in both “How to Use This Chain” and “Key Rules”; Step 3 Before repeats the requirement.
- README troubleshooting recommends making the agent reprint, while README/debug/recovery guidance preserves instruction reprints as a separate behavior. These references need a consistent policy.
- Product changes belong in `~/railspike`; plans and verification belong here. Historical plans/logs remain evidence, not active instructions to rewrite. No website or application behavior change is needed.

## Option A — Read without mandatory repetition
Require reading and following the relevant instruction file, but do not automatically echo it or substitute a compulsory summary. Explain or quote relevant instructions when requested or when needed for a concrete decision or blocker.

- **Pros:** Directly removes the duplication; simplest policy; preserves useful explanations and approval handling.
- **Cons:** The conversation no longer displays the entire source as a visible reading receipt; adherence must be judged from actions and artifacts.

## Option B — Replace reprints with a required acknowledgment
After reading, emit a short file link and confirmation before each step or phase.

- **Pros:** Makes the active instruction source visible with less output.
- **Cons:** Still adds repetitive ceremony; acknowledgment does not prove comprehension or adherence.

## Option C — Reprint once, then suppress repeats
Keep the first reprint of each file and omit later ones unless its contents change.

- **Pros:** Retains an initial conversational copy while reducing repetition.
- **Cons:** Still duplicates freshly read files; adds tracking and resumption ambiguity without meeting the request as directly.

## Option D — Brief task-relevant summary
After reading the applicable instructions, briefly identify the next action, relevant constraints, and any approval gate. Summarize again only when those change. The original instructions remain authoritative; a summary never substitutes for reading them.

- **Pros:** Reduces output while making the agent's interpretation visible for correction before work proceeds; more informative than a reading acknowledgment.
- **Cons:** Adds some conversational overhead; compression can omit exceptions or blur approval rules, and a summary does not prove adherence. Summarizing the whole file at every transition would recreate much of the repetition.

## Recommendation
Choose **Option D**, as selected by the user, as one small documentation-only cycle.

Keep summaries focused on the upcoming action rather than compressing the entire instruction file. Provide the initial summary after reading and before acting; summarize again only when the next action, relevant constraints, or approval gate change. The original instructions remain authoritative, including exceptions omitted from the summary.

- Align canonical workflow rules, Step 3 setup, README advice and recovery/debug references. Preserve reading and state restoration on entry/resumption; missing or unreadable instructions still require a clear blocker, not pretending they were read.
- Verify a normal step transition and resumption: read the applicable instructions, provide a brief task-relevant summary before acting when it is new or changed, do the authorized work, and provide useful progress/handoff. Confirm that an unchanged context does not trigger another summary and that changed actions, constraints, or approval gates are surfaced before proceeding. No automatic full reprint or separate reading acknowledgment is required. Explicit requests to show instructions remain supported; necessary approval explanations may quote the relevant rule.
- Distinguish ordinary tool output used to read a file from an additional assistant-authored echo. This change governs Railspike's instructions; it does not change tool-output rendering or suppress requested file contents.
- Handoff requires consistent active guidance, valid links, unchanged approval/commit rules and documented scenario checks. These establish the instruction contract, not guaranteed compliance by every agent.
