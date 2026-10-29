> **Feature plan:** [Step 1](./shared_implementation_standards_step1_solution_assessment.md) · [Step 2](./shared_implementation_standards_step2_feature_description.md) · [Step 3](./shared_implementation_standards_step3_development_plan.md) · [Step 4](./shared_implementation_standards_step4_implementation_summary.md)

Debug mode: enabled (host marker present at intake).
Effort study: `railspike-effort` / `railspike/shared_implementation_standards`; [standing enrollment and ledger](../../research/effort_estimation/collection.md).
Extended estimates: enabled.

**Cycle estimate: 0.50**

## Original Query

Great, please write step 1 for these changes.

## Understood Intent

Make implementation standards equivalent across staged and one-shot Railspike while preserving their different planning handoffs and commit cadence. Recommend host-owned engineering guidance for work outside Railspike. The preceding review found that v3's Users/person-page incident was explicitly Direct (no Railspike), while Railspike's own one-shot instructions also lack the staged path's concrete reuse checks. This request authorizes Step 1 only.

## Problem

Substantive implementation safeguards are mixed into staged instructions, making them easier to miss in one-shot work and unavailable to Direct work unless adopted by the host.

## Option A — Repeat the safeguards in each workflow

**Estimate: 0.35**

Add explicit reuse, completion, risk, verification, and final-review requirements to one-shot guidance, retaining the staged versions; recommend host-owned rules for Direct work in installation guidance.

- Pros: small change; each execution path is self-contained.
- Cons: duplicated requirements can drift; future corrections must reach both paths.
- Driver/uncertainty: bounded instruction and template edits, but reconciling existing differences may increase scope.

*— Codex · 2026-10-29 UTC*

## Option B — One shared implementation contract (recommended)

**Estimate: 0.50**

Give both modes one authoritative contract, with explicit entry and closeout references. Move common substantive requirements there; keep mode-specific planning, approval, record, and commit rules in their workflows. Installation guidance recommends durable host rules for tasks outside Railspike.

- Pros: one maintained standard; compact one-shot evidence; addresses both the product gap and the incident's opt-out boundary.
- Cons: another required reading dependency; careless extraction could weaken staged requirements or import staged ceremony into one-shot.
- Driver/uncertainty: reconciling all entry points and verifying parity costs more than duplication; live agent compliance cannot be established by document checks alone.

*— Codex · 2026-10-29 UTC*

## Recommendation and boundary

Choose B as one documentation-focused, end-to-end slice: agents entering either mode can find, apply, and verify the same implementation standard. Cover inspection and reuse decisions (with reasons for new equivalents), normal-entry completion and recovery, material risks before dependent work, relevant shared-consumer/environment/dependency verification, and final diff review for duplication, scope, and documentation. Use proportionate fields in existing records rather than another artifact. Validate both reading paths, reported-failure scenarios, documentation-only applicability, and preserved mode exceptions; report live compliance separately.

Host guidance should survive a Railspike opt-out without silently converting Direct work into Railspike or enrolling it in the study. Exclude mandatory component catalogs, application/CSS refactors, changes to approval or commit cadence, website work, consumer updates, and release publication. Product documentation belongs in `../railspike`; plans, verification evidence/checks, and authorized ledger bookkeeping belong here. No implementation is authorized yet.

**Concepts touched:** [Planning record](../../concepts/planning.md#planning-record) changed; [Approval and scope boundary](../../concepts/planning.md#approval-and-scope-boundary) used unchanged. Proposed addition: shared implementation standards, describing reuse and completion evidence in both modes. Inventory changes wait for implementation.

## Study history and status

2026-10-29T02:23:48Z — scope v1, R1/P2, Codex single exposed rater; model/settings unavailable. Intake is missing: the preceding review already inspected instructions and incident evidence. First recorded projection is this Step 1 handoff: A 0.35; B/recommended cycle 0.50. Both cover their whole alternative, including planning, documentation, checks, and ordinary correction, from development `dbae1e6ea6164de3d2ce063b516814629e55f165` / product `583e69da722e37d6993dfc017b140473d143c554`. All three [frozen R1 sources](../../research/effort_estimation/references/R1/manifest.json) hash-verified; cross-workflow reconciliation places B above small integration references and below R1 composer decluttering (0.60). Values are scope judgments, not time or summed work units. Approval pending; no implementation, retrospective, or accepted outcome. Prior host guidance edit is completed context, not implementation of this cycle.

*— Codex · 2026-10-29 UTC*

2026-10-29T02:32:00Z — User: “Approved Step 1.” Option B selected; [Step 2](./shared_implementation_standards_step2_feature_description.md) drafted for review. Earlier scope and estimates retained.
