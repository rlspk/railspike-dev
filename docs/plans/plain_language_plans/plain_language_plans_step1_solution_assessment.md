> **Feature plan:** [Step 1](./plain_language_plans_step1_solution_assessment.md) · [Step 2](./plain_language_plans_step2_feature_description.md) · [Step 3](./plain_language_plans_step3_development_plan.md) · [Step 4](./plain_language_plans_step4_implementation_summary.md)

Debug mode: enabled (host marker present).
Effort study: `railspike-effort` / `railspike/plain_language_plans`; [standing enrollment and ledger](../../research/effort_estimation/collection.md).
Extended estimates: enabled.

**Cycle estimate: 0.40**

## Original Query

Please take a look at the screenshot in this directory. My issue is that I don't understand a lot of the language. For example, what does "extend the shared result contract to retain its probability and companion name through sco... etc." mean? Do you think this can be improved? I recently read about ASD-STE100 and was wondering if that can be applied here somehow? Maybe not strictly, but its wisdom?

Follow-up: "Wait, please write Step 1, but don't commit it right away."

## Understood Intent

Plans that Railspike agents write should be readable by the maintainer without translation. Apply the writing rules of ASD-STE100 (Simplified Technical English) to Railspike's instructions for plan artifacts. Its controlled dictionary is out of scope. The evidence case is a v3 Step 1 written by Codex on 2026-11-03, where one 30-word sentence packs four ideas and names three things by invented abstractions ("shared result contract", "companion name", "score transfer"). This request authorizes Step 1 only, with no commit.

## Problem

Railspike asks for short, high-level plans but says nothing about plain words, so agents compress ideas into abstract noun phrases that the reader cannot decode.

## Option A — Reword the brevity guardrails in place

**Estimate: 0.20**

Replace "no verbose prose" and "avoid verbose descriptions" in the Step 1, Step 2 and Step 3 instruction files with two or three plain-writing rules each.

- Pros: smallest change; no new section; no new links.
- Cons: the same rules repeated in three files; Step 4 summaries, one-shot records and study snapshots stay uncovered.
- Driver/uncertainty: three small edits and a link check; the risk is drift between the three copies.

## Option B — One shared writing rule, referenced everywhere (recommended)

**Estimate: 0.40**

Add a short "Writing style" section to `RAILSPIKE.md` and point every artifact instruction at it. Delete the brevity guardrails it replaces. The rules are the STE rules that apply to any technical text:

- One idea per sentence. Keep sentences under about 25 words.
- Use one term for one thing in the whole artifact.
- Prefer a verb to a noun made from a verb ("change the format", not "format evolution").
- Do not build noun strings of more than three words.
- Name a file, function or setting by its real name when it anchors a decision. Do not describe it with an abstraction.
- Use the active voice with a concrete subject.

- Pros: one source of truth; covers Steps 1–4, one-shot records and the host-facing text that agents copy into chat; the deleted guardrails offset most of the added words.
- Cons: touches the largest instruction file; needs care so the rule does not read as permission to write long.
- Driver/uncertainty: wording the rule so an agent applies it, plus link repairs in six files; whether a live agent follows it is not testable inside this cycle.

## Option C — Option B plus fielded study and reuse sections

**Estimate: 0.60**

Do B, then require the labeled snapshot template already in `docs/effort-estimation.md` in place of the prose "study checkpoint" paragraph, and require bullets for "Concepts touched" and "Reuse decisions".

- Pros: fixes the densest paragraph in every enrolled artifact; the template already exists.
- Cons: changes effort-study presentation rules, which need their own verification; a wider diff for the same reader benefit.
- Driver/uncertainty: keeping score semantics unchanged while changing their layout; more files and more examples to update.

## Recommendation and completion boundary

Choose B as one vertical slice: an agent that reads any step or one-shot file finds the rule, applies it to option paragraphs and recommendations, and the maintainer can check a draft against six bullets. Work covers the instruction edits, link repairs, a before/after example built from the evidence case, documentation of the touched concept, and ordinary correction. Verification is documentation-only: document integrity, every changed link, `git diff --check`, and a word-count comparison of `RAILSPIKE.md` showing the rule replaced text rather than only adding it. Live agent compliance stays unverified, as in earlier instruction cycles. Excluded: the STE controlled dictionary, score semantics, rewriting existing plans, the website, and any release. Whether to fold C's snapshot template in is a Step 2 decision.

**Concepts touched:** [Planning record](../../concepts/planning.md), changed under all options because the readability rule becomes part of what a plan must be; [Approval and scope boundary](../../concepts/planning.md) and [Concept inventory](../../concepts/inventory.md) used unchanged. No new inventory entry proposed.

**Reuse decisions:** the existing brevity guardrails live in `docs/workflow/step1_solution_assessment.md` (Guardrails), `docs/workflow/step2_feature_description.md` (line "Avoid implementation details … verbose descriptions"), `docs/workflow/step3_development_plan_do.md` (two bullets), and the Warning Signs list in `RAILSPIKE.md`. No existing section states how to write; the Instruction Summaries section governs chat, not artifacts. B extends these surfaces; no new file is needed.

**Enhancement requests:** none.

## Study snapshot and approval state

```text
Study / stable cycle ID / legacy alias / parent or replacement: railspike-effort / railspike/plain_language_plans / none / none
Checkpoint / UTC recorded at / rater and verified model identity: Step 1 handoff / 2026-11-03T06:01:35Z / Claude Code, model claude-fable-5-1, single exposed rater
Scope version / starting revision / reference version / protocol version: v1 (Option B) / product bc9e4319db18de4bd9a8dc3bd4fdc87ac8aa0574 on main, dev d9426c184d7f8b67d413bfe1539e4da2acde5af1 / R1 (three frozen sources hash-verified) / P2
Outcome, normal entry, recovery and required evidence / dependencies: shared writing rule in RAILSPIKE.md, referenced from every artifact instruction; verified by document integrity, link and diff checks; no runtime dependency
Prior exposure (including source inspection and inherited scores): intake missing; the instruction files and the evidence case were inspected and discussed before this rating
Cycle estimate: 0.40
Option estimates: A 0.20 / B 0.40 / C 0.60, each a complete alternative from this starting point, not additive
Reason (scope change, new understanding, or reaffirmation): first projection
Approval context / artifact or immutable revision: Step 1 approval pending; no implementation, retrospective score or accepted outcome; artifact uncommitted by user instruction
```

*— Claude Code · 2026-11-03 UTC · Model: claude-fable-5-1*

2026-11-03T08:41:27Z — User: “approved step 1.” Option B approved; Step 2 drafted for review. Original scope and estimates retained. Approval authorizes the next planning step, not implementation or a commit.
