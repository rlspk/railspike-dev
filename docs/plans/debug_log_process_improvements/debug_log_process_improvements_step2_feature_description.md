> **Feature plan:** [Step 1](./debug_log_process_improvements_step1_solution_assessment.md) · [Step 2](./debug_log_process_improvements_step2_feature_description.md) · [Step 3](./debug_log_process_improvements_step3_development_plan.md) · [Step 4](./debug_log_process_improvements_step4_implementation_summary.md)

Debug mode: enabled

## Problem
Installer tests passed on the supported platform while a known user's recovery remained unusable, and completion claims did not separate verified outcomes from blocked or pending checks. Railspike's instructions need to make a known user's ordinary-entry recovery an acceptance condition and require honest, qualified completion reports.

## Scope selection
- **Approved direction:** Step 1 Option B, first cycle only. Instruction consolidation (Option A) and prospective comparison (Option C) are separate follow-ups.
- **Debug state:** disabled at Step 1 (snapshot); enabled by the user's explicit request alongside `Approved Step 2`. The project marker applies only to new workflows. Step 2 itself was handed off with diagnostics disabled, so its first diagnostic report is the Step 3 entry in the debug log.

## User stories
- As a maintainer, I want requirements that name a known user's environment to carry a concrete recovery acceptance condition so that a pass on a different platform cannot justify completion.
- As a user in an unsupported or mismatched environment, I want the ordinary entry point to name the mismatch, the next action, and how to retry so that I can recover without maintainers.
- As a reviewer, I want completion reports to separate passed, failed, blocked, pending, and inapplicable checks so that I can judge what was actually verified.
- As a Railspike developer, I want intentional support limits and existing gates preserved so that this fix does not become a broad workflow rewrite.

## Core requirements
- **Step 2 guidance:** when the request involves a known user or environment, the feature description states that user's ordinary entry point and recovery condition.
- **Step 3/4 acceptance:** such a condition is replayed against each reported failure; a pass only on the installer or supported platform cannot satisfy it.
- **Completion claims:** the Step 4 handoff distinguishes passed, failed, blocked, pending, and inapplicable checks, and identifies reproduced baseline failures; a focused pass is never reported as an unqualified full-suite or user-outcome result.
- **Preserved rules:** approval gates, scope boundaries, stage commits, durable state, append-only corrections, and deliberate support boundaries are unchanged.
- **Validation:** the new wording is exercised against the two dependency-recovery transcripts and the supported/unsupported environment mismatch before approval of Step 3.

## Delivery scope
- **Work type:** documentation-only (instruction contract).
- **Allowed documentation files:** in the product checkout `railspike`: `RAILSPIKE.md`, `docs/workflow/step2_feature_description.md`, `docs/workflow/step3_development_plan_do.md`, `docs/workflow/step3_development_plan_after.md`, `docs/workflow/step4_implementation_after.md`, and `docs/failure-modes.md`. In `railspike-dev`: this feature's plans, summary, and review ledger.
- **Intended audience/outcome:** agents following Railspike and the maintainers who review their handoffs.
- **Not permitted:** application, installer, or CI changes; changes to v3 platform support; edits to completed plans; changes to the debug-log contract.

## Completion boundary
The allowed files carry the new guidance with consistent wording and working cross-links; the wording is shown, in the Step 4 summary, to turn both recorded failures into explicit, non-satisfiable-by-other-platform acceptance conditions; and an honest handoff report format is defined. Correction path: revert the product commit for the changed instruction files. Handoff: reviewed product branch with paired `railspike-dev` records; merging and releasing are separate decisions.

## Risks
- **Instruction growth:** more rules lengthen files already criticized for repetition. Validate by comparing line counts before and after in the first stage; mitigate by amending existing sections instead of adding new ones.
- **Over-application:** the rule may burden work with no known user or environment. Validate against a documentation-only and a small-fix example; mitigate with an explicit applicability condition.
- **Wording not tested against the failure:** an instruction can read well and still miss the incident. Validate by replaying both transcripts against the draft text before Step 3 approval.
- **Weakening recall after context loss:** moved or condensed text could remove a gate reminder. Mitigate by keeping local reminders and re-reading the changed files end to end.

## Shared component inventory
- **`RAILSPIKE.md` Key Rules and Step guide:** extend in place with the applicability condition and report categories.
- **Step 2, Step 3 do/after, and Step 4 after workflow files:** extend the existing checklists; no new step files.
- **`docs/failure-modes.md`:** add the incident as a recorded failure mode if it lacks one; reuse the ledger rows for evidence.
- **README step table and `WELCOME.md`:** read-only; unchanged unless a wording conflict is found, which would return to this step.

## Simple user flow
1. A request names a known user, environment, or recovery condition.
2. Step 2 states that user's ordinary entry point and the recovery condition.
3. Step 3 stages replay each reported failure as acceptance evidence.
4. Step 4 reports each check as passed, failed, blocked, pending, or inapplicable.
5. The reviewer approves or returns the work with a precise account of what was verified.

## Success criteria
- Replaying the two dependency-recovery transcripts against the new guidance makes each fail the acceptance condition unless the user's recovery is shown to work.
- A sample handoff with one blocked and one pending check cannot be read as an unqualified success under the new wording.
- All changed files stay within the allowed list; `git diff --check` and the link checkers show no new findings beyond the known future-step links.
- Net added instruction length is recorded, and removed duplicates are listed.

## Enhancement Requests
None recorded.
