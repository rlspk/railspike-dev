> **Feature plan:** [Step 1](./one_shot_cycles_step1_solution_assessment.md) · [Step 2](./one_shot_cycles_step2_feature_description.md) · [Step 3](./one_shot_cycles_step3_development_plan.md) · Step 4 (pending)

Debug mode: enabled

Effort study: `railspike-effort / railspike/one_shot_cycles`; standing enrollment; [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.65**

## Original Query

> Railspike currently lacks a way to document one-shot small fixes and implementations, right?
>
> I think this has been a problem in that any one-shot things I do are not documented on the same level as Railspike cycles...
>
> This is good, please write Step 1.

## Understood Intent

Support explicitly authorized one-shot work with the same substantive development evidence as staged Railspike cycles. Reduce approval handoffs and duplicated artifacts without reducing documentation quality. This request authorizes the assessment, not execution of the proposed mode.

## Problem

Railspike's staged artifact contract leaves one-shot work dependent on exceptions or informal records, weakening traceability and effort-study coverage.

## Option A — One-shot authorization with separate step artifacts

**Estimate: 0.50**

Retain separate scope, plan, and implementation artifacts, but define bounded upfront authorization that permits their sequential preparation and execution without intermediate approval pauses.

- Pros: reuses existing evidence structure and most recovery conventions; easy comparison with staged cycles.
- Cons: retains paperwork overhead; must distinguish agent-authored planning from actual user approval.
- Driver/uncertainty: authorization and checkpoint integration across existing guidance; total-cycle plausible range 0.40–0.70.

## Option B — One evolving record with equivalent evidence

**Estimate: 0.65**

Introduce a supported one-shot cycle mode with one record capturing request, authorization, scope, intended outcome, and proportionate approach before implementation, then decisions, discoveries, changes, verification, and outcome as work proceeds.

- Pros: separates authorization cadence from evidence quality; preserves history and recovery without duplicate artifacts.
- Cons: needs clear applicability, commit, checkpoint, and escalation rules; consolidated records can blur chronology unless original scope and later changes remain distinct.
- Driver/uncertainty: a new artifact lifecycle integrated with existing study/debug conventions; total-cycle plausible range 0.50–0.85.

## Recommendation

Choose **Option B**. Deliver a complete documented path from explicit bounded authorization through execution, verification, and closeout, including resumption, failure, and transition to staged planning when work exceeds its authorization. Evidence parity means the same substantive facts, with detail proportional to the work; it does not require manufacturing alternatives or retrospective plans.

Require traceable authorization: questions and plan references confer no new authority. Preserve existing authorized work when a question is asked. Keep original scope and append later decisions; identify corrections separately from additions. Record verification limits, incomplete/abandoned outcomes, and commit references or an explicit uncommitted status. Define commit behavior deliberately rather than silently inheriting or discarding staged cadence.

Enroll supported one-shot cycles under the host's existing study policy from intake, preserving R1, append-only estimates/scope, and honest missing checkpoints. Keep ordinary non-cycle tasks possible. Validate examples for success, interruption, scope expansion, questions without approval, and unavailable checks. Documentation consistency checks establish the contract, not runtime enforcement.

Scope v1 includes product guidance/templates, development records, study integration, and applicable verification. Excludes historical backfill, host migration, publication, a full STE rewrite, and runtime gates. The [earlier gating discussion](../../research/2026-10-26-instruction-clarity-and-approval-gating.md) is related context, not an approved dependency; formal enforcement remains separate follow-up work.

## Scope and estimate history

- **2026-10-27 UTC — Intake:** no pre-inspection estimate captured; remains missing. Prior exposure includes this conversation, workflow inspection, and earlier one-shot records.
- **2026-10-27 UTC — Step 1 handoff, v1:** recommended whole-cycle projection **0.65**, R1/P2; single exposed Codex rater, not an independent rating or measured labor. Options A/B are alternative full-cycle projections from the same starting point, including inspection, planning, changes, verification, documentation, and ordinary correction; do not sum them. All three frozen R1 hashes verified against the host manifest. The 0.60 composer and 1.00 recovery anchors inform relative scope; uncertainty is lifecycle/checkpoint compatibility.
- **Starting revisions:** product `f8c8d2588a4a849a12acc7c425d99f533e218f8d`; development `6bdb0293cf80b5996118abed344ea8595a9779d5`. Existing uncommitted discussion note preserved. No parent cycle; related discussion linked above.
- **Approval/outcome:** Step 1 requested; recommendation awaiting review. Implementation, stage counts, final revisions, retrospective assessment, and maintainer fit/acceptance pending. Model/settings unavailable. Subsequent scope and score changes must append history.

*— Codex · 2026-10-27 UTC*

## Approval update

2026-10-27 UTC — User replied **Approved Step 1**. Recommendation B approved for Step 2 definition; earlier pending status is retained as history. No implementation authorization inferred.

*— Updated by Codex · 2026-10-27 UTC*
