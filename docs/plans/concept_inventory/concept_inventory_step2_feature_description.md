> **Feature plan:** [Step 2](./concept_inventory_step2_feature_description.md) · [Step 3](./concept_inventory_step3_development_plan.md) · [Step 4](./concept_inventory_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/concept_inventory`; standing enrollment under AGENTS.md; [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.40**

Step 1 skipped: the user selected the direction after the conversational review. Step 2 was subsequently approved explicitly; see the appended approval record. Implementation awaits Step 3 approval.

## Request and problem

“Maintain and update concise concept inventory in docs/concepts/, spanning multiple files if necessary. No feature flag. List concepts touched in the plan files. That's it for the first iteration.” Railspike needs a small, maintained description of project concepts and a clear connection between those concepts and planned work.

## User stories

- As a maintainer, I want concise descriptions of the concepts encountered during work so that later cycles can reuse that understanding.
- As a reviewer, I want plans to name the concepts they touch so that I can see which behaviors are affected.

## Core requirements

- Maintain the consuming project's inventory under `docs/concepts/` as ordinary Railspike work, with no flag, activation test, opt-in prompt, or refusal marker. Create entries lazily for concepts touched by the cycle; preserve existing material and split files only when useful. No whole-project survey or historical-plan backfill.
- Keep entries short: name, purpose, a brief behavioral scenario (operational principle), and relevant source/instruction paths. Describe current behavior; mark uncertainty or proposed behavior explicitly. Concepts are a planning lens, not a required code architecture.
- Include a concise **Concepts touched** section in new or revised plan artifacts: names/links and whether each is created, changed, or used unchanged. Step 1 may identify candidates by option; Steps 2 and 3 refine the chosen scope. A one-shot record carries the equivalent list. State “none” when appropriate rather than inventing concepts.
- Planning identifies proposed inventory additions/changes; implementation updates the affected entries with the corresponding authorized work and verifies them against the resulting code or instructions. Keep existing approval and commit rules, including paired commits for separate repositories. Inventory edits do not authorize behavior changes.

## Delivery scope and completion boundary

Documentation-only product change for agents and maintainers. Allowed product paths: `../railspike/RAILSPIKE.md`, `../railspike/docs/workflow/*.md`, `../railspike/docs/concepts.md` (compact shared guidance if needed), and `../railspike/docs/README.md`. Host paths: this cycle's plans/debug/verification records, `docs/plans/README.md`, its study-ledger entry, and concise touched-concept entries under `docs/concepts/`. Host inventory and installed guidance are distinct.

Complete when the instructions consistently describe creation, planning references, maintenance, and verification. Correct mismatches in the affected documents; hand off reviewed local changes and evidence. No application/runtime, tooling, dependency, website, merge, or publication work. Earlier ideas about concept-based stage boundaries, new drift gates, feature flags, and a comprehensive Railspike self-model are deferred outside this iteration.

## Concepts touched and shared surfaces

- **Concept inventory — created:** persistent, concise descriptions tied to the consuming project's implementation.
- **Planning record — changed:** lists the concepts relevant to the proposed work; existing staged files and the one-shot record remain canonical.
- **Approval/scope boundary — used unchanged:** governs both inventory edits and product edits.
- Reuse the existing step instructions, completion checks, and one-shot lifecycle; reference shared concept guidance without duplicating it. UI/API inventory is inapplicable to this instruction-only change.

## Risks

- **Prompt growth:** duplicated guidance could obscure existing rules. Review wording before Step 3; keep the shared definition in one place and step additions brief.
- **Stale or speculative entries:** plans could be mistaken for implemented behavior. Check a proposed-to-completed scenario; keep proposals labeled until verified and update only touched entries.
- **Forced classification:** ordinary code may lack clean concept boundaries. Review a small maintenance example; permit short descriptions, uncertainty, or no concepts without requiring architectural changes.

## Flow and success criteria

1. Read existing relevant entries and list concepts touched in the current plan; identify missing entries and proposed changes.
2. Follow normal approvals, then deliver the scoped work and matching inventory updates.
3. Verify touched entries and links against the delivered behavior; retain unrelated inventory content.

Acceptance evidence: walkthroughs for an absent inventory, an existing multi-file inventory, a changed concept, work with no relevant concept, and one-shot execution; consistent host-relative paths, concise guidance, and passing Markdown/link and existing workflow checks. Live agent compliance remains unverified unless actually exercised. Runtime/deployment checks are inapplicable.

## Scope and estimate history

- **2026-10-28 — Intake:** missing before detailed inspection. Prior conversational review and workflow inspection are disclosed; no retrospective prospective score is fabricated. Step 1 is not applicable.
- **2026-10-28T23:01:26Z — Step 2 handoff, scope v1:** 0.40 projected total, single exposed Codex rater, R1/P2. All three frozen-source hashes verified. Covers inspection, planning, instruction integration, touched host entries, verification, records, and ordinary corrections; not hours or measured labor. Driver: consistent inventory lifecycle across staged and one-shot instructions; uncertainty: instruction/check compatibility. Compared with R1's modest integrated changes (0.25–0.35), this adds several workflow handoffs but no runtime subsystem. Starting revisions: development `0ea4e734bce73b7b7a18de119d5770107f5d4b08`; product `ea1ad5b524c2b447d3e61b15ccd3cd412ce6ecef`. User selected scope; Step 2 approval pending. No implementation, release, or acceptance claimed.

*— Codex · 2026-10-28 UTC*

## Approval record

2026-10-28: the user confirmed lazy maintenance rather than a comprehensive project sweep, then explicitly replied “Approved Step 2.” Scope v1 is unchanged. The intervening “Approved Step 1” was clarified and was not treated as Step 2 approval. Step 3 planning is authorized; implementation remains pending.

*— Codex · 2026-10-28 UTC*
