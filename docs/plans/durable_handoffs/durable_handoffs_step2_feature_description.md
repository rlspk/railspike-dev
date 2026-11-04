> **Feature plan:** [Step 1](./durable_handoffs_step1_solution_assessment.md) · [Step 2](./durable_handoffs_step2_feature_description.md) · [Step 3](./durable_handoffs_step3_development_plan.md) · [Step 4](./durable_handoffs_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/durable_handoffs`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.65**

## Problem and intended outcome

Plans can preserve information across coding sessions, but their existence does not establish that someone else can resume correctly. Deliver an engaging, evidence-backed blog post that helps technical readers assess a handoff and distinguishes documentary evidence from untested benefits.

## User stories

- As a developer inheriting agent work, I want to identify decisions, permissions, and unfinished verification so that I can choose a defensible next action.
- As a skeptical reader, I want traceable examples and limitations so that I can assess the argument without accepting Railspike's claims on trust.
- As the maintainer, I want a reviewable article and reusable evidence so that a later paper can build on documented questions.

## Core requirements

- Write a standalone article, working title **“The chat is gone. Can someone else finish the work?”**, with a concrete opening, three case discussions, a practical checklist, limitations, and a concise future-study proposal. Target 1,500–2,500 words, excluding the appendix.
- Before extraction, record a bounded candidate pool, selection criteria, and cutoff. Inspect three existing artifact chains; record selection reasons and relationships, retain gaps and counterevidence, and never substitute a favorable case for an incomplete one.
- For each case, trace intent, decisions, authorized scope, verification, and unfinished work to identified source versions. Mark absent evidence unknown; distinguish reported authorization from independently established authorization. Inspection demonstrates what the records contain, not what an unseen successor understood.
- Keep a compact source/claim appendix with paths, revisions or hashes, relevant excerpts, interpretation, and disclosure suitability. Verify related-work citations; do not claim novelty from the preliminary search or present local-only references as publicly accessible.
- Separate observations, design advice, and hypotheses. The future-study sketch compares conversation history, concise handoffs, and durable plans while addressing information budgets, task/model controls, and independent outcome review; it does not run that study.

## Delivery scope and completion boundary

**Documentation-only.** Allowed: `docs/research/durable_handoffs/` (article and evidence/source appendix); this cycle's `docs/plans/durable_handoffs_*` artifacts and eventual organized folder; its entry in `docs/plans/README.md`; its append-only collection-ledger entries and required organization link repairs. Existing sources and unrelated work stay intact. Application/runtime, tests, CI, product, website, generated publication files, experiments, recruitment, uploads, and publication are excluded.

Reader flow: **1.** Open the article. **2.** Follow concrete cases to their evidence. **3.** Apply the checklist to a handoff. **4.** Understand what remains untested. Completion means a locally reviewable draft and appendix with checked claims/links, explicit limitations, and maintainer-review status. Unsupported or unsuitable material is qualified, redacted, or removed with a correction record; unresolved essential evidence blocks the dependent claim. Handoff is for review, not publication or academic acceptance.

## Risks and early validation

| Risk / impact | Early validation and mitigation |
| --- | --- |
| Selecting persuasive examples could overstate usefulness. | Fix the bounded selection rule before extraction; record prior exposure, related cases, exclusions, and unfavorable evidence. No prevalence estimates. |
| Source gaps could invite invented reconstruction. | Check chain availability first; preserve missingness and distinguish inspected artifacts from reports. Label any illustration explicitly. |
| Private or unstable sources could make examples unsuitable. | Check disclosure suitability and source identity before quoting; retain local provenance and use safe paraphrases or omit sensitive detail. |
| Readers could mistake the article for an efficacy study. | Check the framing before drafting and every conclusion afterward; no measured speedup, successful-handoff, or general human-performance claims. |

These controls are requirements for Step 3; case availability and disclosure remain pending source review, not established findings.

## Reuse and concepts

Reuse the [existing exploratory findings](../../research/railspike_paper/findings.md) and [outcome report](../../research/historical_outcome_analysis/report.md) as source leads and evidence-labeling precedents; inspect underlying artifacts before using a case. The [candidate assessment](../../research/railspike-paper-candidates.md) and [title options](../../research/railspike-paper-title-candidates.md) supply framing. A new focused article is needed because those documents do not analyze handoff reconstruction.

**Concepts touched:** [Planning record and approval/scope boundary](../../concepts/planning.md), used unchanged; existing entries suffice, no inventory additions or behavior changes. **Enhancement requests:** none.

## Success criteria and study checkpoint

Three cases each cover the five evidence dimensions or explicit unknowns; factual claims map to sources; the article contains an actionable checklist and unrun-study proposal; local links and whitespace pass; no unresolved unsupported claim remains presented as fact. Independent human review remains pending unless actually performed.

2026-10-30T20:33:27Z — Step 2, scope v1, R1/P2, starting revision `7620f119577bd52f1204c38f159319ee9a2e3b0b`; Codex, single exposed rater. **0.65 reaffirmed** for the entire Option B cycle, including planning, source review, writing, verification, and corrections; clarified requirements do not expand the selected outcome. Earlier intake remains missing; original option estimates and verified frozen references remain in Step 1. This is relative scope, not hours or measured labor. Step 1 approved; Step 2 approval pending; no implementation or accepted study outcome.

*— Codex · 2026-10-30 UTC*

2026-10-30T20:35:30Z — User: “approved step 2.” Scope v1 approved without additions; Step 3 drafted for review. Original estimates retained; implementation and publication remain unauthorized.
