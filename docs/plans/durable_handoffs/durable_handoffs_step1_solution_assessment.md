> **Feature plan:** [Step 1](./durable_handoffs_step1_solution_assessment.md) · [Step 2](./durable_handoffs_step2_feature_description.md) · [Step 3](./durable_handoffs_step3_development_plan.md) · Step 4 (pending)

Debug mode: enabled (host marker present).
Effort study: `railspike-effort` / `railspike/durable_handoffs`; [standing enrollment and ledger](../../research/effort_estimation/collection.md).
Extended estimates: enabled.

**Cycle estimate: 0.65**

## Original Query

Let's work on durable plans and handoffs. Please write Step 1 for writing this paper/blog post.

## Understood Intent

Develop [proposal 4](../../research/railspike-paper-candidates.md) into engaging, credible writing for technical readers, with a path toward an academic contribution. Working title: **“The chat is gone. Can someone else finish the work?”** This request authorizes Step 1 only.

## Problem

Railspike retains plans and decisions, but our existing records do not establish whether those artifacts help a fresh developer or agent resume work correctly.

## Option A — Practical design essay

**Estimate: 0.35**

Write an accessible essay explaining what a useful handoff should preserve, with a clearly illustrative example and a short checklist.

- Pros: focused, immediately useful, no experiment required.
- Cons: limited empirical contribution; examples cannot establish effectiveness.
- Driver/uncertainty: writing and source checks; novelty beyond existing planning practices needs examination.

## Option B — Evidence-backed blog post with a research question (recommended)

**Estimate: 0.65**

Write a standalone article using a bounded review of three existing artifact chains to show what a successor can and cannot reconstruct: intent, decisions, authorized scope, verification, and unfinished work. Include gaps or contradictions, a practical handoff checklist, and a concise proposal for testing actual resumption.

- Pros: concrete Railspike examples; useful article now; reusable evidence for a later paper.
- Cons: document inspection cannot establish successful handoffs or time saved.
- Driver/uncertainty: source tracing, related work, excerpt suitability, and claim checking; missing history remains a finding rather than being reconstructed as fact.

## Option C — Experiment-led paper and companion blog

**Estimate: 1.50**

Compare fresh-agent resumptions using conversation history, concise handoffs, and durable plans, then write a paper and accessible companion article. Evaluate correct next actions, scope mistakes, and duplicated investigation with independent outcome review.

- Pros: direct evidence about handoff performance; stronger empirical contribution.
- Cons: exceeds one comfortable cycle; needs a separately approved pilot, evaluation, and writing sequence. Human-developer claims require human participants.
- Driver/uncertainty: fair information budgets, task selection, model configuration, repeated runs, and reviewer availability; feasibility is untested.

## Recommendation and boundary

Choose B: one complete, locally reviewable article plus a compact evidence/source appendix under `docs/research/durable_handoffs/`. Readers should leave with a usable handoff checklist and a clear distinction between information preserved and successful resumption. Fix case-selection criteria before extraction; retain unfavorable cases, distinguish reports from inspected evidence, and label any illustrative reconstruction. Verify citations and excerpt suitability; remove or qualify unsupported claims during correction. Hand off the draft for maintainer review; publication remains separate.

This slice includes planning, source review, writing, verification, and ordinary corrections. It excludes new agent experiments, recruitment, product changes, website deployment, and submission/publication. An academic efficacy claim waits for later evaluation. Reuse the [existing findings](../../research/railspike_paper/findings.md) as leads, not proof of handoff success.

**Concepts touched:** [Planning record and approval/scope boundary](../../concepts/planning.md), used unchanged in all options; no behavior or inventory change proposed. **Enhancement requests:** none beyond this writing proposal.

## Study snapshot and approval state

2026-10-30T20:31:21Z — R1/P2, scope v1, start `7620f119577bd52f1204c38f159319ee9a2e3b0b`; Codex, single exposed rater. Intake missing: earlier candidate/evidence discussions preceded this cycle. First Step 1 projections: A 0.35; B/recommended whole cycle 0.65; C 1.50 (split required for comfortable fit). All cover their complete alternative from this starting point, not remaining work or hours. B's evidence reconciliation exceeds a small documentation edit; C adds an untested evaluation. All three [frozen R1 sources](../../research/effort_estimation/references/R1/manifest.json) hash-verified. Standing enrollment applies; estimates are not independent ratings. Step 1 approval pending; no implementation, retrospective score, or accepted outcome. Preserve this snapshot on revision.

*— Codex · 2026-10-30 UTC*

2026-10-30T20:33:27Z — User: “approved step 1.” Option B approved; Step 2 drafted for review. Original scope and estimates retained. Approval authorizes the next planning step, not article implementation or publication.
