# The chat is gone. Can someone else finish the work?

You are halfway through a feature when the agent stops. You hit the usage limit, or the provider is down. So you open a different agent, point it at the same repository, and type "keep going."

It has never seen the conversation. It has the files.

In my experience that is the most common handoff in agent-assisted development, and it is completely mundane. No new hire, no team transfer. Same person, same repo, different tool, zero memory. Whatever the first agent and I agreed on in chat is gone unless it was written down somewhere in the repo.

Railspike is a workflow for coding agents that writes it down. Each round of work, called a cycle, leaves four files in the repository: an assessment of the options, the agreed requirements, a development plan, and an implementation summary. The bet is that the second agent can read those four files and continue correctly.

This article tests that bet the cheap way. I took three real sets of plan files and asked what a fresh agent would learn from them, where it would go wrong, and what the files cannot tell it.

**What this is and is not.** I read files. Nobody handed them to a fresh agent and watched what happened. The three cases come from the Railspike maintainer's own projects, chosen by a fixed rule (the lowest ID in each category of an earlier 25-record review) so that weak cases could not be swapped for flattering ones. One case comes from a different project that kept a single plan file instead of Railspike's four, and whether Railspike ran it at all is unknown. Every claim below maps to a source in the [evidence appendix](./evidence.md), with hashes and limits.

## Case 1: half the feature is missing, on purpose

**What happened.** The request was one sentence: two features had been built in another project, fold them into this one. Feature one groups each feature's plan files into their own folder. Feature two is a "debug mode" that writes diagnostic reports about how the workflow instructions performed.

The assessment file weighed three paths: do both at once, split them, or import the old commits and repair the conflicts. Its recorded recommendation was to split, so the Git history would stay readable. The requirements file for the first cycle then excluded debug mode outright. The implementation summary closed the folder work and said debug mode would get its own cycle with its own approvals. [Evidence: case C002](./evidence.md#c002--a-request-divided-into-two-cycles).

**What the new agent sees.** If it reads only the original request, half the feature is missing and the obvious move is to build it. If it reads the requirements and summary, it learns the half was deferred on purpose, and the obvious move is to ask first. Same repo, opposite actions. A forgotten requirement is a bug to fix. A deliberately split feature needs its own permission.

There is a smaller trap in the same files. The folder rule's own plan files were written before the folder rule existed, so they could not follow it. The development plan says so explicitly and calls it a bootstrap exception. Delete that one line and the history looks like the rule was broken by the very cycle that introduced it.

**What the files cannot tell you.** Who said yes. The summary reports that approved content was preserved, but I did not inspect an approval transcript. The commit shows the public-copy changes and the summary landed together. It does not show who approved them or whether the reported checks actually passed. A tidy folder of plans still needs evidence behind its status labels.

## Case 2: the page that was finished and not released

**What happened.** The second case is a replacement homepage aimed at skeptical technical readers: plain explanation, install path, a worked example drawn from real plans, honest limits. The implementation summary reports that local checks passed: the layout measurements, the example excerpts against their source plans, the links.

The same summary lists what was still open: the maintainer's review of the copy and the rendered page, the merge, and a check of the live URL after deployment. The commit that recorded all this is titled "record release verification," and it changes only the summary file. It does not show the page was released. [Evidence: case C005](./evidence.md#c005--a-locally-checked-page-with-an-open-release-boundary).

**What the new agent sees.** The question it will face is "do I merge this?" The files answer clearly: not yet, these three gates are open. Without that list, there are two tempting wrong moves. Redo work that is already finished, or publish on an authority nobody granted. To be clear, this is my reading of the files, not a report that an agent made either mistake, and I did not check whether the gates were closed later.

A summary that says "these checks passed" and "this review is still open" in the same breath is not contradicting itself. That pairing is exactly what the next agent needs. The damage happens when one word like "complete" flattens it, or when an old pending item sits there with no hint of whether it is still pending.

**What the files cannot tell you.** Here the repo shows its one real blind spot. The worked example on the homepage came from an earlier cycle, and its summary notes that the approval for that example was typed in chat and never stored. The proposal survived. The result survived. The sentence "yes, go ahead" did not, because it lived in the conversation and the conversation is gone.

## Case 3: the field that changed meaning at the bottom of the file

**What happened.** The third case is from a separate application. Its activity page lists recently changed source files, each with the commit that last touched the file, stored during indexing so the page never runs Git on a request. One plan file carries the data contract, five implementation stages marked complete, the reported tests, the risks, and an approval gate.

Then, at the bottom, a production hotfix note: full rebuilds now use the repository's current commit instead of looking up each file's last commit, because the per-file lookups held a global execution lock during rebuilds. Incremental writes keep using the exact commit that wrote them. [Evidence: case C024](./evidence.md#c024--a-field-whose-meaning-changed).

**Why that matters.** The repository's latest commit may not have touched a given file at all. So after the hotfix, the same column no longer means "the commit that last changed this file." It means "a commit at which this file existed." Linking to a file at a revision and claiming when it last changed are different promises. The field kept its name and changed its meaning.

**What the new agent sees.** The top of the file says one thing, the bottom says another, and nothing is crossed out. Below the five completed stages, the last line still reads: pause here until this plan is approved. An agent that treats every sentence as a live instruction could restore the per-file lookups and bring the lock problem back. An agent that reads the file as a chronology gets it right. The file rewards the second reading but does nothing to force it.

**What the files cannot tell you.** Whether the hotfix was worth it, and whether anyone signed off on the new meaning. The committed diff does remove the per-file Git lookup and cache a single repository-head value, so the change is real. Nothing measures the speedup that motivated it. The test-success note predates the hotfix, so it says nothing about the revised meaning. And the stale approval gate is not proof that anything ran without permission. It is just a sentence nobody deleted.

Appending the correction instead of overwriting the plan did one valuable thing: it kept the reason for the change. The cost is that the old contract and the new one are equally prominent. A two-line current-state note at the top, naming which behavior governs and pointing down to the superseded decision, would fix that. I have not tested that fix. It is also not new. Michael Nygard's architecture decision records have recommended keeping reversed decisions marked "superseded," with a pointer to their replacement, since 2011. [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).

## Five things to find before you type "keep going"

These cases suggest a short checklist. It is a proposal, not a validated instrument. Before resuming work from files alone, find each of these:

1. **The outcome currently wanted.** The latest scoped requirement, and how it differs from the original request. In case 1, that is the line deferring debug mode.
2. **The decisions still in force.** The chosen approach, its reason, and anything superseded. In case 3, that is the hotfix note.
3. **The action actually authorized next.** An approval tied to this scope at this revision. If the file only reports that approval happened, say so. A plan file, or a status an agent wrote about itself, cannot grant permission.
4. **What was actually checked.** The command or observation, separate from the summary of its result, with the revision and environment if you have them. In case 2, local rendering says nothing about the deployed page.
5. **What is still open.** Pending checks, deferred work, missing evidence, and who has to decide. Leave the next reader a concrete question, not a vague worry.

A short current-state section at the top of each plan could answer all five and link down to the history. The history still earns its place, because it explains why the current state looks the way it does. Replaying the entire chat would make the new agent redo the selection work. Compressing too hard would drop the exception or correction that matters most.

One practical test: pick the next action you are tempted to take and trace its justification through the files. "May I merge this homepage?" should lead to the release condition and the evidence behind it. If the trail ends at an approval that lived only in a chat window, the gap should stay visible. That is a useful answer even when the answer is "not yet."

The reader has work to do as well, judging how strong each piece of evidence is. An interview study by Dhanorkar, Passi, and Vorvoreanu describes developers overseeing agents through planning and review, and treating test results as assurance of correctness. It is context for taking that judgment seriously; it did not evaluate Railspike or this checklist. [Human oversight of agentic systems in practice](https://arxiv.org/abs/2606.05391).

## How you would actually test this

The claim everyone wants is that durable plans make handoffs better. Three files from one maintainer cannot settle it. A new agent might find the answer in a minute, ignore the files entirely, follow the superseded instruction, or spend longer reconciling the documents than it would have spent reading the chat.

The test that could settle it looks like this. Stop several tasks at defined points. Give fresh agents the same repository snapshot plus one of three context packages: the full conversation, a short handoff note, or the durable plan files. Include an ordinary unfinished implementation, a reversed decision, and an open approval gate. Write down the acceptable next actions before anyone sees a continuation. Then score each continuation on four things: did it reconstruct the current scope, make an authorized move, repeat finished investigation, or introduce a mistake. Hold the model, tools, time budget, and task difficulty constant, have reviewers score without knowing which package produced the result, and repeat enough times that one lucky continuation does not carry the conclusion.

Two controls matter. If the plan package simply contains facts the handoff note left out, it will win for that reason alone, so one comparison should hold information constant and vary only organization. And a realistic comparison should count what the files cost to maintain. A plan that saves its reader ten minutes after costing its author twenty is a trade, not a win. Those numbers are made up to illustrate the point; nothing in these three cases was timed.

Human handoffs would need a separate human study. Nothing measured on fresh agents should be presented as evidence about how fast another developer gets up to speed. None of this has been run.

For now, what these files offer is inspectable unfinished business. Case 1 explains why half a request was set aside. Case 2 names the release work it does not establish. Case 3 preserves a correction that changes how its own requirement should be read. The chat is gone. The files are still there. Whether the next agent notices what they say, and acts on it, is the thing worth testing.

---

*Draft of October 30, 2026. Written and source-checked by Codex from the maintainer's development records, with a same-day editorial revision for readability; independent human review is pending. The [evidence appendix](./evidence.md) distinguishes inspected artifacts, reported results, and interpretation. Local source availability is not a claim of public access. The maintainer authorized posting this article to zenmemes.com on October 30, 2026.*
