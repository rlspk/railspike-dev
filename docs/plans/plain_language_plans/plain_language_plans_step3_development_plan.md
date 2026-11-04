> **Feature plan:** [Step 1](./plain_language_plans_step1_solution_assessment.md) · [Step 2](./plain_language_plans_step2_feature_description.md) · [Step 3](./plain_language_plans_step3_development_plan.md) · [Step 4](./plain_language_plans_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/plain_language_plans`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.40**

## Completion Contract

- Documentation-only. Allowed product files in `railspike`: `RAILSPIKE.md`, `README.md` (one optional sentence), `docs/workflow/step1_solution_assessment.md`, `step2_feature_description.md`, `step3_development_plan_do.md`, `step4_implementation_do.md`, `one_shot.md`. Allowed dev files in `railspike-dev`: this cycle's `docs/plans/plain_language_plans*` artifacts and folder, its `docs/plans/README.md` entry, `docs/concepts/planning.md`, and append-only ledger rows.
- Outcome: an agent that opens any step or one-shot file reaches a `## Writing style` section in one link. The section holds six rules and one before/after example. The maintainer can check a draft against the six rules and name the failing one.
- Completion: all five workflow files link to the section and contain no "verbose"; `RAILSPIKE.md` grows by fewer than 150 words net from its 5,116-word baseline; the example passes all six rules; the concept entry matches; the link checker and `git diff --check` pass. Correction path: a wrong or confusing rule is fixed by a later cycle through review; nothing fails at runtime.
- Evidence boundary: document integrity, links, word count, and a manual replay of the evidence sentence. Live agent compliance is not testable here and is recorded as unverified. Runtime, UI, migration, deployment, website and release checks are inapplicable. Handoff is an unmerged branch in each checkout with paired commits recorded, not a merge or release.

## Key Risks

- Agents read "short sentences" as permission to write more sentences. Early validation: Stage 1 leaves every page limit and the one-paragraph-per-option structure untouched; Stage 3 greps that the ≤1 page lines survive. Mitigation: the rule text says sentence shape, not length.
- The section pushes `RAILSPIKE.md` past what agents hold. Early validation: Stage 1 counts words before and after. Mitigation: replace the Warning Signs wording and keep the section under 130 words; fail verification above 150 net.
- "Name the real file" collides with "no implementation details". Early validation: Stage 2 rereads each guardrail after editing. Mitigation: the rule says a name may anchor a decision and code never appears; the no-code limits stay.
- A live agent ignores the rule. Early validation: none possible in this cycle. Mitigation: Stage 3 records it as unverified and keeps the maintainer's revision request as the recovery path.

## Stage 1 — Add the shared writing rule

**Estimate: 0.15**

- Goal: one `## Writing style` section in `RAILSPIKE.md` that an agent can apply without further reading.
- Dependencies: Step 3 approval; feature branch in both checkouts; organized planning commit; Step 4 summary created with the entry snapshot.
- Expected changes: add the section after Planning Artifacts with the six rules from Step 2, a one-sentence scope note (artifacts and handoff messages; not the preserved Original Query, quoted sources, or fixed snapshot and attribution formats), and the before/after example built from the v3 evidence sentence. Change the Step 1 Warning Signs entry so "verbose explanations" becomes a link to the section.
- Verification approach: `wc -w` before and after, net under 150; link checker; `git diff --check`; count sentences in the example and confirm none exceeds 25 words; confirm the ≤1 page lines in Step 1, 2 and 3 files are untouched.
- Estimate details: driver: wording six rules so they are short, testable and do not read as a style guide; uncertainty: how many words the example costs; this stage owns the word-count check.
- Risks or open questions:
  - Impact: the rule reads as a licence to write at length.
  - Early warning / validation: the section itself exceeds 130 words.
  - Mitigation: cut the example before cutting a rule.
- Canonical components/API contracts touched: `RAILSPIKE.md` Planning Artifacts and Warning Signs sections; no new file.

## Stage 2 — Link the rule from every artifact instruction

**Estimate: 0.10**

- Goal: each file that tells an agent to write an artifact points at the rule and no longer says "verbose".
- Dependencies: Stage 1 verified, summary updated, committed.
- Expected changes: in `step1_solution_assessment.md` Guardrails replace the two bullets with one no-code bullet and one link; in `step2_feature_description.md` Guardrails replace "verbose descriptions" with the link and drop "Keep the doc lightweight enough to consume at a glance"; in `step3_development_plan_do.md` replace "Prefer bullets over prose paragraphs" and "verbose explanations" with the link, keeping the no-code and no-SQL limits; in `step4_implementation_do.md` add the link to the header-plus-bullets paragraph; in `one_shot.md` add the link beside the Record template. Optional: one sentence in `README.md` where the plan format is described.
- Verification approach: `grep -c verbose` returns 0 in the five workflow files; every new link resolves through the link checker; reread each edited guardrail to confirm the no-code limit survives; `git diff --check`.
- Estimate details: driver: five small edits with relative links from `docs/workflow/` to `../../RAILSPIKE.md#writing-style`; uncertainty: whether the one-shot file wants the link at all; drop it with a recorded reason if it adds noise.
- Risks or open questions:
  - Impact: a guardrail loses its no-code limit along with its brevity adjective.
  - Early warning / validation: the reread in verification.
  - Mitigation: edit one bullet at a time; keep the diff to the adjective and the link.
- Canonical components/API contracts touched: the five workflow files named above; `README.md` optional.

## Stage 3 — Concept entry, replay and closeout

**Estimate: 0.10**

- Goal: the concept inventory matches the delivered text, the known-user condition is replayed as far as the cycle allows, and the records close honestly.
- Dependencies: Stage 2 verified, summary updated, committed.
- Expected changes: update the Planning record entry in `docs/concepts/planning.md` with the writing-rule path; record the manual replay, verification table, omissions, paired product and dev commits, retrospective scope and pending maintainer acceptance in the Step 4 summary; append the closeout ledger row.
- Verification approach: replay the evidence sentence from the v3 screenshot through the six rules by hand and record pass or fail per rule; record the live Codex-in-v3 check as pending with the maintainer's revision request as manual recovery; run the link checker on both checkouts and `git diff --check`; inspect the full diff for files outside the allowed list.
- Estimate details: driver: closeout bookkeeping across two repositories; uncertainty: none material; this stage owns the final diff review.
- Risks or open questions:
  - Impact: the replay is agent self-review and could pass a sentence the maintainer still cannot read.
  - Early warning / validation: the maintainer reads the example in review.
  - Mitigation: label the replay as self-review, not independent verification.
- Canonical components/API contracts touched: `docs/concepts/planning.md`; the Step 4 summary and ledger; existing `scripts/check-markdown-links.py` reused unchanged.

## Execution discipline and study checkpoint

After approval, create a feature branch in each checkout, organize this cycle's artifacts into `docs/plans/plain_language_plans/`, repair links and add the index entry, and make the planning commit with only approved plans, the debug log and organization changes. Create the summary afterward. Each stage ends with verification, a summary update and a commit before the next starts. Minimum: one planning commit and three stage commits in `railspike-dev`, plus paired product commits recorded in the summary. No push, merge or release.

```text
Study / stable cycle ID: railspike-effort / railspike/plain_language_plans
Checkpoint / UTC recorded at / rater: Step 3 handoff / 2026-11-03T08:45:20Z / Claude Code, model claude-fable-5-1, single exposed rater
Scope version / starting revision / reference / protocol: v1 (Option B) / product bc9e4319db18de4bd9a8dc3bd4fdc87ac8aa0574, dev d9426c184d7f8b67d413bfe1539e4da2acde5af1 / R1, three hashes reverified today / P2
Cycle estimate: 0.40, reaffirmed; judged independently, not the stage sum
Stage work: S1 0.15 / S2 0.10 / S3 0.10, each covering its own checks and corrections; not additive, not hours
Prior exposure: intake missing; Step 1 option estimates retained
Reason: plan adds no scope; verification is as Step 2 defined it
Approval context: Steps 1 and 2 approved by user; Step 3 approval pending; no implementation, retrospective or accepted outcome; uncommitted
```

*— Claude Code · 2026-11-03 UTC · Model: claude-fable-5-1*

2026-11-03T08:46:29Z — User: “approved step 3.” Plan approved without changes; Step 4 begins with branch creation, plan organization and the planning commit.
