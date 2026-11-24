> **Feature plan:** [Step 1](./epic_checklists_step1_solution_assessment.md) · [Step 2](./epic_checklists_step2_feature_description.md) · [Step 3](./epic_checklists_step3_development_plan.md) · [Step 4](./epic_checklists_step4_implementation_summary.md)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/epic_checklists`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.60**

## Completion Contract

- **Work type:** documentation-only. Allowed files are exactly those in [Step 2](./epic_checklists_step2_feature_description.md#delivery-scope-and-completion-boundary). No application, CI, website, release or v3 change.
- **Branches:** `feat/epic-checklists` in `railspike-dev` (exists) and a new `feat/epic-checklists` in `railspike` from `main` at `3cd85805`. Each stage commits product files in `railspike` and its summary update in `railspike-dev`, linking the pair.
- **Reader outcome:** an agent asked for a handoff prompt pushes the plans and gives one correct code block. An agent asked for an epic writes a checklist from the template.
- **Completion:** all allowed files edited; links resolve; `git diff --check` passes; `RAILSPIKE.md` grows by 150 words or fewer; the Stage 4 replays pass.
- **Recovery:** a wrong rule gets fixed in a later cycle; nothing breaks at runtime.
- **Evidence boundary:** replays are self-review against recorded artifacts. A live v3 handoff in a new chat stays pending at closeout.
- **Not applicable:** runtime, UI, deployment, migration and release checks.

## Key Risks

- **Labeled draft commits weaken the approval commit gate.** Early validation: Stage 1 rereads the gate after the edit. Mitigation: the exception allows only a separate commit labeled "draft, not approved" and never counts as the approval commit.
- **A prompt claims an approval the record lacks.** Early validation: Stage 4 builds prompts from four sample records and compares each claim. Mitigation: the rule says the record wins over the prompt.
- **The template is too heavy for small epics.** Early validation: Stage 4 fits the three-cycle backlog checklist. Mitigation: only Resume here and items are required.

## Stage 1

**Estimate: 0.20**

- Goal: any cycle can be handed to a new chat with one handoff prompt.
- Dependencies: product branch created.
- Expected changes: a short `## Handoff prompts` section in `RAILSPIKE.md` (request phrasings, push and commit rule, required fields, one code block, the record wins, the new chat's first checks). The approval commit gate gains the labeled draft-commit exception. Step 1's "/new or /clear" reminder gains a clause pointing at handoff prompts. `failure-modes.md` gains a case for a missing or stale branch on resume.
- Verification approach: word count before and after; gate text still requires its own approval commit; links resolve.
- Estimate details: driver: wording the gate exception without loosening it; uncertainty: low.
- Risks or open questions: draft-commit exception, above.
- Canonical components/API contracts touched: approval commit gate, Follow-up Cycles Before Merge, `one_shot.md` resumption rules (reused).

## Stage 2

**Estimate: 0.20**

- Goal: an agent can write an epic checklist from one file.
- Dependencies: Stage 1, since the Resume here section links to handoff prompts.
- Expected changes: new `docs/workflow/epic_checklist.md`. It covers when to suggest an epic and when to create one, and that the record approves nothing. It covers writing the checklist as a documentation-only one-shot, the item fields, the status layers, the approver field and the MVP line. It covers added, cut and superseded items, and backlinks from each cycle's first artifact. A short template follows.
- Verification approach: under one page before the template; every Step 1 review gap maps to a rule.
- Estimate details: driver: keeping the template short; uncertainty: which fields to mark optional.
- Risks or open questions: template weight, above.
- Canonical components/API contracts touched: v3 checklist format at `2d7805c8` (source); `effort-estimation.md` "do not sum" rule (reused).

## Stage 3

**Estimate: 0.10**

- Goal: agents find the new rules from the places they already read.
- Dependencies: Stage 2.
- Expected changes: an Epics pointer in `RAILSPIKE.md`; Step 1's split note for estimates above 1.0; a `one_shot.md` line that an epic's mode lean is not authorization; one `effort-estimation.md` sentence that each epic cycle is its own outcome; index lines in `README.md` and `docs/README.md`. In `railspike-dev`, epic checklist and handoff prompt entries in `docs/concepts/planning.md`, and the change to approval and scope boundary.
- Verification approach: each new link resolves; the split rule text is unchanged.
- Estimate details: driver: several small edits; uncertainty: low.
- Risks or open questions: none.
- Canonical components/API contracts touched: concept inventory (`docs/concepts/planning.md`).

## Stage 4

**Estimate: 0.10**

- Goal: show the rules cover real cases before handoff.
- Dependencies: Stages 1–3.
- Expected changes: `epic_checklists_verification.md` in this cycle's folder. It replays the hn_theme handoff and builds handoff prompts from four records: hn_theme Step 1, and the notifications, pledges and backlog checklists. It fits those three checklists to the template. It replays the known-user failure: a new chat given a prompt for an unpushed branch, and one for a branch behind `origin/main`.
- Verification approach: every prompt has all required fields and no unrecorded approval; no checklist loses information; each failure case has a stated next action; final diff review across both repositories against the allowed list; `git diff --check`.
- Estimate details: driver: four replays; uncertainty: replays are self-review.
- Risks or open questions: prompt claims, above.
- Canonical components/API contracts touched: none new.

**Concepts touched:** [Planning record](../../concepts/planning.md#planning-record) and [Approval and scope boundary](../../concepts/planning.md#approval-and-scope-boundary) changed in Stage 3; epic checklist and handoff prompt added in Stage 3.

## Study history and status

2026-11-24T17:40:00Z — Step 3 handoff, scope v3, R1/P2, Claude single exposed rater. Step 2 approved and committed as `1fba406`. Cycle projection 0.60 reaffirmed. Stage work S1 0.20, S2 0.20, S3 0.10, S4 0.10 is supplemental and not summed. Approval pending; no implementation.

*— Claude · 2026-11-24 UTC · Model: claude-opus-5-5*
