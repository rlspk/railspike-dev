> **Feature plan:** [Step 1](./remove_instruction_reprints_step1_solution_assessment.md) · [Step 2](./remove_instruction_reprints_step2_feature_description.md) · [Step 3](./remove_instruction_reprints_step3_development_plan.md) · [Step 4](./remove_instruction_reprints_step4_implementation_summary.md)

Debug mode: disabled

# Task-relevant instruction summaries

## Completion Contract
- **Work type and scope:** Documentation-only. Product edits are limited to `~/railspike/RAILSPIKE.md`, `README.md`, `docs/workflow/step3_development_plan_before.md`, and `docs/failure-modes.md`. Development bookkeeping is limited to this feature's plans, summary, optional debug log, organization under `docs/plans/remove_instruction_reprints/`, plans-index entry, and necessary reference repairs. Preserve historical records and unrelated work.
- **Outcome and recovery:** Users receive a brief next-action, relevant-constraints, and approval-gate summary after required reading and before acting; repeat only for changed context. Restore instructions and state on resumption, omit unchanged recoverable summaries, and establish a fresh summary when prior context is unavailable. Missing/unreadable instructions remain blockers; original instructions retain authority.
- **Handoff and evidence:** Consistent active guidance, verified links and file scope, and recorded scenario outcomes establish the documentation contract, not guaranteed agent compliance. Correct contradictions or newly broken links before handoff; distinguish existing unrelated failures. Runtime, UI/API, database, deployment, and external release checks are not applicable; application, tests, CI, generated-artifact, and website edits are prohibited.

## Key Risks
- **Lost constraints:** Summaries could conceal exceptions or approvals. Early review confirms that a summary must state relevant gates and cannot override source instructions; preserve reading and all existing approval/commit obligations.
- **Conflicting advice:** Old guidance could restore reprints. The pre-draft scan found seven references across the four approved product files; update them together and rescan before completion.
- **Faulty resumption:** Repetition suppression could skip recovery. Early scenario review distinguishes unchanged recoverable context (reread/restore, no repeat), changed context (updated summary), and unavailable prior context (restore, then fresh summary). Resolve any contradiction before implementation proceeds.

## Step 4 setup
- After `Approved Step 3`, inspect both worktrees and create feature branches without including unrelated changes. Organize approved plans and repair this feature's navigation/index references; commit only the approved planning bundle in `railspike-dev` before product edits or creation of the Step 4 summary.
- Create the summary with inherited debug state. Keep the product stage commit and corresponding development summary commit paired, record the product commit in the summary, and report both commit IDs at handoff. Do not amend completed commits.

## Stage 1
- **Goal:** Deliver the complete summary policy across normal entry, transitions, troubleshooting, and recovery in one documentation stage (about one hour; target at most 50 changed product lines).
- **Dependencies:** Approved Steps 1–3, Step 4 setup and planning commit complete, and key risks resolved within the approved scope.
- **Expected changes:** Define the canonical summary contract in `RAILSPIKE.md`; replace mandatory reprints and align Step 3 setup, README troubleshooting/debug advice, and failure-mode recovery wording. Preserve explicit content requests, necessary rule quotations, useful updates, tool-output rendering, debug logging, and approval/commit rules.
- **Verification approach:** Review first entry; changed and unchanged transitions/resumptions; unavailable prior context; missing/unreadable instructions; explicit reprint requests; necessary quotations; and both debug modes. Expect no routine full reprints, summaries before new/changed work, no repeated unchanged recoverable summaries, and no work past unresolved blockers or approval gates. Record expected/observed contract outcomes in the summary. Rescan active guidance, compare preserved obligations, run Markdown link checks for both repositories and `git diff --check`, and inspect changed-file scope. Record existing unrelated link failures separately; future-step links must resolve once the summary exists.
- **Risks or open questions:** Compression or conflicting guidance could weaken the contract; validate all scenarios against the final wording and correct contradictions before committing. No unresolved scope questions; return to planning if another product file needs changes.
- **Canonical components/API contracts touched:** Reuse the instruction contract in `RAILSPIKE.md` and align its three approved consumers; no UI/API components or new settings.
- **Completion:** Commit verified product changes, then commit the stage summary and evidence in `railspike-dev`; retain the initial planning commit and record paired stage commits before the completed-step handoff.
