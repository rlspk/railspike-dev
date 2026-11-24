# Planning record

**Purpose:** make the proposed outcome, scope, affected concepts, and verification reviewable before work proceeds.

**Operational principle:** in a staged cycle, the maintainer reviews the current plan and approves progression before the next step is drafted or executed. In a bounded one-shot cycle, the agent creates a feature branch, writes a plan recording the user's authorization and intended outcome, and commits it before implementation; the completion commit includes implementation and the same plan updated with decisions and outcomes (paired commits across repositories). Explicit no-commit instructions preserve the branch and written plan while leaving commits undone. Both forms identify concepts touched and proposed inventory changes, and carry source-backed reuse decisions, completion/recovery conditions, risks, and verification evidence under the shared implementation standards. Every artifact is written to the shared writing style: one idea per sentence, one term per thing, and real file names in place of abstractions.

**Where it lives:** [shared implementation standards](../../../railspike/docs/workflow/implementation_standards.md), [planning artifact rules](../../../railspike/RAILSPIKE.md#planning-artifacts), [writing style](../../../railspike/RAILSPIKE.md#writing-style), [Step 2](../../../railspike/docs/workflow/step2_feature_description.md), [Step 3](../../../railspike/docs/workflow/step3_development_plan_do.md), and [one-shot record](../../../railspike/docs/workflow/one_shot.md#record-template).

# Approval and scope boundary

**Purpose:** keep implementation within the work the user authorized.

**Operational principle:** approving a staged plan allows the next prescribed step; a bounded one-shot request permits execution within its recorded authority. If implementation requires expanded scope, the agent records the discovery and seeks the required renewed approval before dependent work. Updating a concept description does not authorize changing behavior. A handoff prompt request also authorizes committing and pushing the cycle's plans to its feature branch, with unapproved drafts in a separate commit labeled "draft, not approved"; it never approves a step.

**Where it lives:** [mode selection](../../../railspike/RAILSPIKE.md#choose-the-execution-mode), [enhancement requests](../../../railspike/RAILSPIKE.md#enhancement-requests), and [one-shot scope changes](../../../railspike/docs/workflow/one_shot.md#resumption-and-scope-changes), and [handoff prompts](../../../railspike/RAILSPIKE.md#handoff-prompts).

# Epic checklist

**Purpose:** coordinate one outcome delivered in several one-shot and staged cycles.

**Operational principle:** the checklist lists each cycle with a stable ID, a mode lean and a layered status, and opens with Resume here. It approves nothing; each item gets its own authorization when it starts. Cut and superseded items stay visible.

**Where it lives:** [epic checklist](../../../railspike/docs/workflow/epic_checklist.md).

# Handoff prompt

**Purpose:** carry a cycle or epic into a new chat without a long chat.

**Operational principle:** on request, the agent pushes the plans and gives one code block naming the branch, plan path, step and recorded approvals. The new chat restores state from the pushed record, which wins over the prompt.

**Where it lives:** [handoff prompts](../../../railspike/RAILSPIKE.md#handoff-prompts), [resume failure case](../../../railspike/docs/failure-modes.md#a-handoff-prompt-points-at-a-missing-or-stale-branch).
