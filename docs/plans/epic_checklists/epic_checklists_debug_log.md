# epic_checklists debug log

## 2026-11-24T17:10:00Z — Step 1

### Necessary/useful instructions

- `docs/workflow/step1_solution_assessment.md`, Original Query rule: the request arrived as a question and a later "yes". Keeping both preserved the actual ask rather than a paraphrase. Retain.
- `RAILSPIKE.md`, Experimental Effort Estimation, split rule ("do not silently count child cycles as independent observations"): this is the rule an epic most strains, so it shaped a Step 2 question. Retain.
- `docs/workflow/one_shot.md`, entry step 2 ("a reference to a plan ... cannot" authorize): it exposed the gap that an epic item marked "(one-shot)" has no defined authority. Retain.

### Redundant/unnecessary instructions

No supported findings.

### Inapplicable instructions

- Plan folder organization and approval commit gate: apply at approval, not yet.
- Branch reuse under Follow-up Cycles Before Merge: new cycle.

### Uncertain assessments

- `README.md` "Split anything over eight stages into a second Step 2/3 cycle" and `RAILSPIKE.md` "Scores above 1.0 prompt a split discussion" both lead to multi-cycle work but say nothing about tracking it. Whether the epic file should be linked from both, or only from Step 1, is for Step 2.
- The model field is from session metadata; reasoning effort was not verified and is omitted.

## 2026-11-24T17:20:00Z — Step 1 (Revision)

Revises the 17:10 entry; earlier findings stand.

### Necessary/useful instructions

- `step1_solution_assessment.md`, Review and revision: kept the Original Query whole and recorded the new direction separately. Retain.

### Uncertain assessments

- No Railspike file covers handing a cycle to a new chat. The Step 1 "/new or /clear" reminder suggests a reset but not how to carry state. The revised Option B would fill this; whether the reminder should then mention prompt blocks is for Step 2.
- Push permission: Railspike defines commits but never push; one-shot authority excludes it. A user request for a prompt block may need to authorize it.

## 2026-11-24T17:25:00Z — Step 1 (Revision)

Wording-only rename ("prompt block" → "handoff prompt"). No new instruction findings; earlier entries stand.
