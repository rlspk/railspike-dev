# The chat is gone. Can someone else finish the work?

A development plan says that an activity feed should display the last commit that changed each source file. Farther down, all five implementation stages are marked complete. Near the bottom, a hotfix note says that full rebuilds now use the repository's current commit instead.

Both descriptions remain in the same file.

Imagine opening that plan in a fresh coding session. If you follow its original specification, you might restore the per-file Git queries that the hotfix removed. If you notice the correction, you can see why someone changed course: the note says those queries held a global execution lock during rebuilds. The document preserves the reason for leaving the original design behind. It also makes you reconcile two descriptions of what the software should do.

That is a more interesting test of a saved plan than whether the file exists.

Railspike puts coding-agent requirements, plans, and implementation records in a repository. Its planning records are meant to remain available after the conversation ends. To examine what that actually leaves behind, this review follows three existing development records: a workflow change, a replacement homepage, and the activity-feed change above. They come from one maintainer's development context, selected by a fixed ordering rule from an earlier 25-record review. The [evidence appendix](./evidence.md) records the selection, source versions, and qualifications.

Nobody was handed these records and observed trying to resume the work. This is a review of the information they preserve. It asks what a successor could look up, which questions would remain open, and where a seemingly useful document could still mislead. The activity-feed record uses a different, single-file format; its execution under Railspike is unknown.

## A scope change worth keeping

The first case began with a request to integrate two additions from an earlier workflow project. One concerned organizing plan files. The other concerned diagnostic reports about the workflow instructions.

The assessment considered doing both together, separating them, or importing the earlier commits and repairing conflicts. Its recorded recommendation was to separate the work so the Git history would be easier to read. The requirements for the first cycle then explicitly excluded diagnostics. The implementation summary closed the organization work and left diagnostics for a separate cycle with its own planning and approvals. [Case C002](./evidence.md#c002--a-request-divided-into-two-cycles).

A successor reading only the original request could reasonably wonder why half the requested functionality was absent. Reading through the requirements and summary supplies an answer: it had been deliberately deferred. That distinction matters when deciding what to do next. An omitted requirement might need a correction; a separately scoped feature needs its own authorization.

There is another small detail in the plan. The cycle that introduced the new organization rule had to begin under the old rule. Its development plan documented that bootstrap exception, and the summary described how it was used. Without the exception, the recorded sequence could appear to violate the very instructions being introduced.

These are useful things for a document to retain: a rejected approach, a reason for splitting the request, a boundary around the approved slice, and a temporary exception. They would be difficult to recover from the final organization rule alone.

But the chain does not establish every approval. The summary reports that approved content was preserved; this review did not inspect a complete authorization transcript. The available commit manifest confirms that public-copy changes and the summary appeared together. It cannot establish who approved them or whether the reported checks passed. A well-organized folder still needs evidence behind its status labels.

## The homepage had more than one finish line

The homepage case provides a different kind of handoff. Its records describe a replacement page for skeptical technical readers: a plain explanation, an install path, an example from actual plans, and candid limits.

The implementation summary reports local layout checks, source comparisons, and link checks. It also leaves the maintainer's copy and visual review, the merge, and a check of the deployed URL pending. The commit titled “record release verification” changes the summary alone. It does not establish that the page was released. [Case C005](./evidence.md#c005--a-locally-checked-page-with-an-open-release-boundary).

The summary records that distinction beside the positive results. A reader does not have to infer deployment from the last stage's name. The record says which boundary the work had reached.

For a new session, the sensible next question would be whether those remaining gates were subsequently closed. Starting more implementation might duplicate finished work; publishing immediately would assume authority the record does not supply. This is a proposed reading of the evidence, not a report that an agent actually made either mistake. The review did not investigate today's deployment state.

The same case exposes a limit of keeping plans in Git. The homepage included an example of another development cycle. Its summary says the example's approval reply was typed in conversation and was not stored. The written artifacts preserved the proposal and the resulting work, but that particular authorization event was absent from the retained example.

There is no contradiction in a handoff saying both “these checks passed” and “this review remains open.” That combination is exactly what someone taking over needs. Trouble begins when a broad label such as “complete” erases the distinction, or when an old pending item survives without any indication of whether it is still current.

## The correction at the bottom of the file

The activity-feed plan is more compact. It describes a data contract, implementation stages, reported verification, risks, and an approval gate in one evolving document.

The original requirement was quite specific: display a canonical filename and the commit that last touched it. Store that information during indexing so the page would not invoke Git on every request. Later, a production-hotfix note changed full rebuilds to use repository HEAD. Incremental writes would still use their exact write commit. [Case C024](./evidence.md#c024--a-field-whose-meaning-changed).

The distinction is substantive. The most recent repository commit can contain an unchanged file; it does not necessarily identify the commit that last modified that file. A link to the file at a revision and a claim about its last modification answer different questions.

Here, the correction has support beyond another sentence in the plan. The inspected hotfix diff removes the per-path Git lookup and replaces it with a repository-head value cached for the rebuild. That corroborates the implementation change. It does not measure the performance improvement claimed as its motivation, and the earlier test-success statement does not by itself establish acceptance of the revised meaning.

The document ends with an instruction to pause until approval, even though the preceding sections describe implemented stages. Without the approval conversation, that leftover gate cannot prove unauthorized execution. It does show that a successor has to interpret the document's chronology rather than treat every sentence as current instruction.

Appending a correction has a real advantage: the earlier intention is not silently erased. In this case, however, the original description and the replacement both remain prominent enough to be followed. A short current-state note could identify the governing behavior and point back to the superseded decision. That is a design recommendation arising from the record, not a repair tested in this study.

This problem predates coding agents. Michael Nygard's description of architecture decision records recommends keeping reversed decisions while marking them superseded, with a reference to their replacement. It also records context and consequences so a later developer can understand the decision. That is a useful precedent for handling the hotfix here; putting decisions in Markdown is not a new invention. [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).

## What I would ask of a handoff

These cases suggest a modest checklist. It is a proposal for organizing a review, not a validated instrument. Before resuming work, try to answer the following from the retained material:

1. **What outcome is currently wanted?** Find the latest scoped requirement and its relationship to the original request. In the organization case, that means seeing that diagnostics were deferred.
2. **Which decisions still apply?** Identify the chosen approach, its rationale, and anything superseded. In the activity case, the rebuild hotfix changes the meaning of a field.
3. **What action is authorized next?** Look for approval tied to the relevant scope or revision. If the record only reports approval, say so. A plan file or an agent-written status cannot independently grant permission.
4. **What has actually been checked?** Separate the command or observation from a summary of its result. Record the revision and environment when available. The homepage's local rendering evidence does not establish a deployed visitor's experience.
5. **What remains unresolved?** Name pending checks, deliberately deferred work, missing evidence, and who must decide. Give the next reader a concrete question to resolve.

A compact current-state section could answer those questions and link to the longer history. The history still matters: it explains why the current state looks the way it does. Repeating the entire conversation would make the successor do the selection work again; an aggressively shortened summary could discard the exception or correction that matters most.

A practical check is to choose a plausible next action and trace its justification. For example: “May I merge this homepage?” The documents should lead to the release condition and its evidence. If the trail ends at an unstored conversational approval, the missing link should remain visible. That is a useful finding even when it prevents immediate progress.

There is also work for the person receiving the handoff. They must judge the relevance and strength of the evidence. An exploratory interview study by Dhanorkar, Passi, and Vorvoreanu describes oversight activities including planning and review, and reports developers using test results as assurances of correctness. It offers context for taking that judgment seriously, but it does not evaluate Railspike or this checklist. [Human oversight of agentic systems in practice](https://arxiv.org/abs/2606.05391).

## The experiment still to run

The claim people understandably want is that durable plans make handoffs better. These records cannot settle it. A successor might find the answer quickly, ignore the files, follow a superseded instruction, or spend longer reconciling them than they would have spent reading the conversation.

A useful comparison would stop several tasks at defined points and give fresh agents the same repository snapshot with different context packages: the conversation history, a concise handoff, or a set of durable plans and stage records. The tasks should include an ordinary unfinished implementation, a changed decision, and a pending approval or verification boundary. Define the acceptable next actions before seeing the continuations.

Measure whether the successor reconstructs the active scope, makes an authorized next move, repeats completed investigation, or introduces a mistake. Keep the model, tools, time budget, and task difficulty controlled. Use independent assessment of outcomes where practical, with reviewers unaware of which package produced a result. Repeat across tasks and runs; one convincing continuation would be a demonstration, not a reliable estimate.

Information quantity needs its own treatment. If the plan package includes facts omitted from the handoff, a better result may simply reflect having those facts. A matched-information comparison could test presentation and organization, while a separate realistic comparison could include the full packages people actually maintain. Preparation and update costs belong in that second comparison too. For example, a document might save its receiver ten minutes after taking its author twenty minutes to maintain; those are illustrative numbers, not measurements from these cases.

Human handoffs would require a separate human study. Results from fresh agents should not be presented as evidence about how quickly another developer can understand the work. None of these comparisons has been run here, and the three historical cases are too selected and related to support a general failure rate.

For now, the strongest thing these records offer is inspectable unfinished business. The organization plan explains why part of a request was set aside. The homepage summary names the release work it does not establish. The activity plan preserves a correction that changes how its original requirement should be read. A successor still has to notice those facts and act on them. That is the next thing worth testing.

---

*Local draft, October 30, 2026. Written and source-checked by Codex from the maintainer's development records; independent human review is pending. The [evidence appendix](./evidence.md) distinguishes inspected artifacts, reported results, and interpretation. Local source availability is not a claim of public access. No publication has been authorized.*
