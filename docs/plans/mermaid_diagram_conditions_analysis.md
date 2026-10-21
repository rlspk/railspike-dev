# Conditions for useful Mermaid diagrams across Railspike steps

Status: analysis saved for future consideration; no workflow instruction changes adopted.

## Proposed rule

Add a Mermaid diagram when understanding a decision requires tracing relationships, branches, states, or ordering that are difficult to follow in prose. Use it to answer a specific review question.

## Evidence from high_traffic_mode

The high_traffic_mode diagram connects visitor requests, operator controls, and background refresh, showing where they share generation and publication safeguards. The numbered user flow alone does not make these interactions apparent. The user reported that drawing the diagram during Step 2 was helpful.

The debug log flags document-length pressure in Steps 2 and 3, but does not itself evaluate the diagram. This supports seeking concise presentation, rather than treating length alone as a reason to add a diagram.

Source artifacts in the local consuming project:

- [Step 1 assessment](../../../agent/v3-codex-2/docs/plans/high_traffic_mode/high_traffic_mode_step1_solution_assessment.md)
- [Step 2 feature description](../../../agent/v3-codex-2/docs/plans/high_traffic_mode/high_traffic_mode_step2_feature_description.md)
- [Step 3 development plan](../../../agent/v3-codex-2/docs/plans/high_traffic_mode/high_traffic_mode_step3_development_plan.md)
- [Debug log](../../../agent/v3-codex-2/docs/plans/high_traffic_mode/high_traffic_mode_debug_log.md)
- [Mermaid source](../../../agent/v3-codex-2/docs/plans/high_traffic_mode/high_traffic_mode_diagram.mmd)

## Conditions to consider

| Condition | What the diagram should clarify |
|---|---|
| Several paths produce different outcomes | Eligibility, bypasses, cache hits/misses, capacity rejection, and recovery |
| Multiple actors or processes interact | Who initiates work, who handles it, and where paths converge |
| Behavior depends on state or transitions | Enabling/disabling a mode, invalidating content, or moving through pending/failure states |
| Ordering or concurrency affects correctness | What must happen first, what can overlap, and where stale work must be rejected |
| An important boundary is easy to misunderstand | Apache versus PHP, shared versus personalized output, or current scope versus future automation |
| Review repeatedly requires reconstructing the same relationships | A stable shared picture for resolving questions and checking agreement |

Any one condition can justify a diagram when it makes a specific review question easier to answer. These are practical triggers, not a requirement to draw a diagram at every step.

## Use across the four steps

| Step | Useful diagram purpose |
|---|---|
| 1 — Solution assessment | Show how competing approaches differ in routing, responsibilities, or boundaries |
| 2 — Feature description | Explain intended behavior, user/system interactions, and meaningful alternate outcomes |
| 3 — Development plan | Clarify dependencies, sequencing, ownership, or coordination needed for correctness |
| 4 — Implementation | Explain a discovered failure/race, document recovery, or reconcile implemented behavior with the approved design |

Choose the form that fits the question: a flowchart for branches and boundaries, a sequence diagram for interactions and ordering, a state diagram for transitions, or a dependency graph for stage relationships.

## Limits

- Name the question the diagram answers, such as “How do requests and refresh jobs safely share the cache?”
- Skip it when a short list or table is equally clear. Complexity or document length alone is insufficient.
- Keep its detail appropriate to the step. Step 2 can show observable behavior without introducing classes, locks, or rewrite syntax.
- Keep requirements and approval boundaries in the plan. A diagram illustrates them; it does not introduce scope or establish approval.
- Reuse and update an existing diagram when it still answers the question; split it when unrelated concerns make it hard to read.
- Treat diagram storage and commit inclusion as a separate workflow question. The high_traffic_mode Step 3 plan explicitly treats its diagram/source as review aids outside the narrow initial planning commit, with handling assigned to its approved documentation stage.

## Diagram source and preview policy

Save the editable `.mmd` source beside the relevant plan and commit it when the diagram becomes maintained documentation, subject to the workflow's artifact and commit boundaries.

Continue generating a `.png` preview for convenient user review. Keep the preview locally, link it for review, and ignore it in Git so generated images do not accumulate in the repository. The committed Mermaid source remains reviewable and can regenerate the preview.

Exception: commit a rendered image when a documentation destination needs it and cannot render Mermaid.

This records the agreed policy for future workflow changes; it does not itself change generation behavior, ignore rules, or existing artifacts.
