> **Feature plan:** [Step 1](./shared_implementation_standards_step1_solution_assessment.md) · [Step 2](./shared_implementation_standards_step2_feature_description.md) · [Step 3](./shared_implementation_standards_step3_development_plan.md) · Step 4 (pending)

Debug mode: enabled (inherited).  
Effort study: `railspike-effort` / `railspike/shared_implementation_standards`; [ledger](../../research/effort_estimation/collection.md).  
Extended estimates: enabled.

**Cycle estimate: 0.50**

## Problem and user stories

Staged instructions contain concrete implementation safeguards that one-shot guidance does not consistently expose; Direct work can miss rules held only inside Railspike.

- As an implementing agent, I want one shared standard so that skipping planning handoffs does not skip reuse, recovery, or verification.
- As a maintainer, I want compact evidence and durable host guidance so that I can review quality across workflows without imposing staged planning on Direct tasks.

## Core requirements

- One authoritative implementation contract applies to staged and one-shot execution, explicitly reached before dependent work and at closeout. Reuse existing substantive rules rather than maintain competing copies.
- Before creating equivalents, inspect existing components, styles, helpers, and API contracts; record relevant paths, reuse/extension decisions, and reasons for necessary new components in existing task records.
- Define normal-entry, end-to-end completion and failure/retry recovery; resolve material risks before dependent work. Preserve scope protection and use documentation-specific outcomes/checks where runtime behavior is inapplicable.
- Verify affected consumers and applicable roles, environments, migrations, deployment, and external dependencies; replay reported failures in the relevant environment or disclose the missing evidence. Review the final diff for duplication, scope, and documentation. Distinguish focused checks from full-suite or user-outcome evidence.
- Preserve each mode's approvals, artifacts, and commit cadence. Keep one-shot records proportionate. Installation guidance recommends host-owned engineering rules that apply outside Railspike, using existing consent/conflict handling; Direct work remains outside Railspike and its study unless separately selected.

## Delivery scope and shared inventory

Documentation-only; audience: implementing agents and maintainers. Allowed product scope: `../railspike/RAILSPIKE.md`, `docs/workflow/`, `README.md`, `WELCOME.md`, and `docs/README.md`. Allowed development scope: this cycle's plans/debug/verification records, its `docs/plans/README.md` entry, its study-ledger updates, and touched entries in `docs/concepts/`. Application/runtime, tests/checker source, CI, deployment, generated files, website changes, consumer updates, and publication are excluded. Existing checkers may be run.

Reuse/extend mode selection and Key Rules, staged component inventories and completion/risk/verification guidance, the one-shot lifecycle/template, and installation/welcome host-guidance offers. These are documentation surfaces; UI/API inventory is inapplicable. Add a shared contract because neither mode-specific location provides a neutral authoritative home. No mandatory component catalog or application/CSS refactor.

**Concepts touched:** [Planning record](../../concepts/planning.md#planning-record) changed; [Approval and scope boundary](../../concepts/planning.md#approval-and-scope-boundary) used unchanged and verified; shared implementation standards proposed as a new entry. Update only touched inventory during implementation.

## Risks

- Lost staged safeguards: compare current obligations against the proposed contract during Step 3 planning; preserve substantive coverage and mode-specific gates.
- Missed shared reading or excess ceremony: trace both entry/closeout paths before finalizing the plan; require explicit references and compact evidence in existing records.
- Opt-out conflation: review installation wording before Step 3; preserve consent and distinguish host rules from Railspike lifecycle/study enrollment.

## Flow, completion, and success criteria

1. An agent enters staged or one-shot work, reaches the common contract, inspects reusable implementations, and records completion/risk expectations.
2. The agent works within authority, verifies the relevant outcome and recovery, and records limitations before closeout under that mode's existing rules.
3. During installation, a maintainer can adopt durable host guidance; later Direct work retains those host standards without Railspike planning gates.

Complete when both reading paths cover every requirement above, the one-shot template captures reuse/completion/verification evidence, and installation guidance retains consent and existing-rule preservation. Record a parity review covering both modes, documentation-only work, and a reported-environment failure; validate links, evidence, touched concepts, and allowed file scope. Replay the v3 Direct incident as a documented instruction-path scenario, not a claim that application behavior was retested. Missing obligations or broken paths require correction and rechecking before handoff. Delivery is reviewed documentation with verification limits; live agent compliance stays unverified unless observed separately. Merge/release are separate authorizations.

## Approval and estimate history

2026-10-29T02:32:00Z — User explicitly approved Step 1; Option B selected. Scope v1/R1/P2 unchanged; **0.50 total projection reaffirmed** at Step 2 by Codex, single exposed rater, model/settings unavailable. Starting revisions and original option estimates remain in [Step 1](./shared_implementation_standards_step1_solution_assessment.md); all three frozen R1 hashes reverified. Intake remains missing; no retrospective, measured labor, or study acceptance inferred. Step 2 approval pending; no implementation authorized.

*— Codex · 2026-10-29 UTC*

2026-10-29T18:17:48Z — User: “Approved Step 2.” Scope unchanged; [Step 3](./shared_implementation_standards_step3_development_plan.md) prepared for approval.
