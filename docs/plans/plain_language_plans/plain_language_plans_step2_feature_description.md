> **Feature plan:** [Step 1](./plain_language_plans_step1_solution_assessment.md) · [Step 2](./plain_language_plans_step2_feature_description.md) · [Step 3](./plain_language_plans_step3_development_plan.md) · [Step 4](./plain_language_plans_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/plain_language_plans`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.40**

## Problem

Railspike tells agents to keep plans short and high-level but never tells them to write plainly. Agents answer by packing several ideas into one sentence and naming real files with invented abstractions, so the maintainer cannot read the plan without translating it.

## User stories

- As the maintainer, I want each option paragraph to use short sentences and real names so that I can judge it on first reading.
- As an agent writing a plan, I want one short rule I can find from any step file so that I do not have to guess what "not verbose" means.
- As a later reader of a plan, I want one term per thing so that I can follow a decision from Step 1 to Step 4 without a glossary.

## Core requirements

- Add one `## Writing style` section to `RAILSPIKE.md` with six rules: one idea per sentence and about 25 words at most; one term for one thing in an artifact; a verb instead of a noun made from a verb; no noun string over three words; the real name of a file, function or setting when it anchors a decision; active voice with a concrete subject.
- Link that section from the Step 1, 2, 3 and 4 instruction files and from the one-shot workflow. Replace the brevity wording those files use today ("verbose prose", "verbose descriptions", "verbose explanations", "prefer bullets over prose") with the link. Keep their non-writing limits: no code, schema, mockups or SQL.
- Include one before/after example built from the evidence case, two sentences each at most, so an agent sees the target.
- State where the rule does not apply: the preserved Original Query, quoted sources, and the snapshot and attribution formats that other sections fix.
- Replace text rather than add it. Net growth of `RAILSPIKE.md` stays under 150 words, measured by `wc -w` before and after.

## Delivery scope and completion boundary

**Documentation-only.** Allowed in the product checkout `railspike`: `RAILSPIKE.md`, `README.md` (one sentence in the plan-format description, optional), `docs/workflow/step1_solution_assessment.md`, `docs/workflow/step2_feature_description.md`, `docs/workflow/step3_development_plan_do.md`, `docs/workflow/step4_implementation_do.md`, `docs/workflow/one_shot.md`. Allowed in `railspike-dev`: this cycle's `docs/plans/plain_language_plans_*` artifacts and their organized folder, its entry in `docs/plans/README.md`, `docs/concepts/planning.md`, and this cycle's append-only ledger rows. No application, runtime, CI, website, generated file or release change is permitted. The STE controlled dictionary, score semantics and rewriting of existing plans are out of scope.

Reader outcome: an agent that opens any step file reaches the rule in one link and writes to it; the maintainer checks a draft against six bullets and names the failing rule when asking for a revision. Completion means the seven product files and the concept entry are edited, every changed link resolves, `git diff --check` passes, the word-count bound holds, and the example sentence passes all six rules. A wrong or confusing rule is corrected in a later cycle through normal review; nothing breaks at runtime. Handoff is a reviewed branch, not a merge or release.

## Known user and environment

The request names the maintainer reading a Codex-written Step 1 in the v3 project. The ordinary entry is a Step 1 request to an agent with the updated Railspike installed. The mismatch to handle is a sentence that still fails a rule. The maintainer's unaided next action is to quote the sentence and the failing rule and ask for a revision; success shows as a revised artifact that passes. The evidence will be that artifact. This cycle cannot run a live Codex session in v3, so that check stays pending after the cycle; the rule text is the manual recovery guidance in the meantime.

## Risks and early validation

| Risk / impact | Early validation and mitigation |
| --- | --- |
| Agents read "short sentences" as permission to write more sentences, and plans grow past a page. | Keep every existing page limit and the one-paragraph-per-option structure unchanged; the rule changes sentence shape, not artifact length. Check the Step 1 file still carries the ≤1 page line. |
| The rule adds words to a 5,100-word file that agents already struggle to hold. | Count words before and after; the replaced guardrails and the Step 1 Warning Signs wording offset the section. Fail the cycle's verification if net growth exceeds 150 words. |
| "Name the real file" conflicts with "no implementation details". | Write the rule so a name anchors a decision and code never appears; verify the three guardrail files keep their no-code limits. |
| A live agent ignores the rule. | Not testable inside this cycle. Record it as unverified at closeout; the maintainer's revision request is the recovery path. |

## Shared instruction surfaces and reuse

- `RAILSPIKE.md`: Key Rules and Warning Signs already set page and option limits; no section states how to write. Add the new section near Planning Artifacts and adjust the Step 1 warning line to point at it.
- `docs/workflow/step1_solution_assessment.md` Guardrails, `step2_feature_description.md` Guardrails, `step3_development_plan_do.md` Guardrails and stage bullets, `step4_implementation_do.md` "Prefer this header-plus-bullets structure" paragraph, `one_shot.md` Record template: each gets one link and loses its brevity adjective.
- `docs/effort-estimation.md` Snapshot and outcome template: reused as-is; the fielded template is already the readable form. Requiring it over prose is deferred (see below).
- No new file. The rules are reworded from ASD-STE100's general writing rules, not copied; no dictionary is vendored.

**Concepts touched:** [Planning record](../../concepts/planning.md), changed: its operational principle gains "written to the shared writing rule" and a path to the new section. [Approval and scope boundary](../../concepts/planning.md) and [Concept inventory](../../concepts/inventory.md) used unchanged.

**Enhancement requests:** Option C (require the fielded snapshot template and bulleted Concepts/Reuse sections) — Disposition: separate work, because it changes effort-study presentation rules that need their own verification. Approval: not requested. Outcome: candidate for a follow-up cycle after this one closes.

## Simple user flow

1. The maintainer asks an agent for a Step 1.
2. The agent opens the Step 1 file, follows the link, and reads six rules and one example.
3. The agent writes each option in short sentences with real names.
4. The maintainer reads the plan once. If a sentence fails, the maintainer quotes it and the rule, and the agent revises.

## Success criteria

- `RAILSPIKE.md` has a `## Writing style` section with six rules and one example; its net word growth is under 150.
- Five workflow files link to the section and no longer contain "verbose".
- The evidence-case sentence, rewritten in the example, has no sentence over 25 words, no noun string over three words, and names the files it means.
- All changed links resolve; `git diff --check` passes; the concept entry matches the delivered text.
- Live agent compliance is recorded as unverified, not claimed.

## Study checkpoint

```text
Study / stable cycle ID: railspike-effort / railspike/plain_language_plans
Checkpoint / UTC recorded at / rater: Step 2 handoff / 2026-11-03T08:42:44Z / Claude Code, model claude-fable-5-1, single exposed rater
Scope version / starting revision / reference / protocol: v1 (Option B, Step 1 approved) / product bc9e4319db18de4bd9a8dc3bd4fdc87ac8aa0574, dev d9426c184d7f8b67d413bfe1539e4da2acde5af1 / R1 verified at Step 1 / P2
Outcome and evidence: seven product instruction files and one concept entry edited; link, whitespace and word-count checks
Prior exposure: intake missing; Step 1 estimates retained
Cycle estimate: 0.40, reaffirmed
Reason: requirements clarified without changing the selected outcome; Option C deferred as separate work
Approval context: Step 1 approved by user; Step 2 approval pending; no implementation or commit
```

*— Claude Code · 2026-11-03 UTC · Model: claude-fable-5-1*

2026-11-03T08:44:02Z — User: “approved step 2.” Scope v1 approved without additions; Step 3 drafted for review. Original estimates retained; implementation and commits remain unauthorized.
