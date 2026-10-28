> **Feature plan:** [Step 2](./welcome_guidance_question_step2_feature_description.md) · [Step 3](./welcome_guidance_question_step3_development_plan.md) · [Step 4](./welcome_guidance_question_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/welcome_guidance_question`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md).

Extended estimates: enabled

**Cycle estimate: 0.30**

**Branches:**
- `railspike`: `feature/welcome-guidance-question`, from `main` `5952bfd` (= `v0.4.0-beta.2`).
- `railspike-dev`: `feature/welcome-guidance-question`, from the current unmerged `feature/homepage-essay-framing` (`4086417`). This is a stacked branch, so the ledger and release records from that branch aren't split apart. It is not a reuse of that branch.
- Each stage commits in the product first, then commits its summary in `railspike-dev` with the paired ID.

## Completion Contract

- **Allowed documentation file scope:** `railspike/WELCOME.md`, and the Quick start welcome sentences in `railspike/README.md`. In `railspike-dev`: this cycle's records and a scenario verification record. Release notes only if a release is requested later.
- **Audience and outcome:** an agent following the welcome asks the AGENTS.md question alone, handles yes, no, and non-answers, reports the outcome, and only then takes the first task. A reader of the README sees the same description.
- **Document completion and recovery:** both files are consistent, and no text remains that silently skips an unanswered offer. Corrections go through further document revisions; installed copies update through the reviewed upgrade process.
- **Evidence boundary:** a scenario walk-through against the final text, plus a replay of the maintainer's reported transcript. Live agent compliance stays pending the maintainer's reinstall.
- **Not applicable:** runtime, UI, deployment, and migration checks. Release checks become applicable only if a beta is requested.

## Key Risks

- **High risk: usability (over-blocking).**
  - Impact: users who just want to start feel stalled.
  - Early validation: Stage 1's task-instead scenario.
  - Mitigation: a single question; any non-answer proceeds at once with a one-line note.
- **Old rule survives.**
  - Impact: agents keep following "do not … block on the offer".
  - Early validation: a grep for "unanswered", "block", and "What would you like" after Stage 1.
  - Mitigation: replace the rule rather than adding to it.
- **Live behavior is unproven.**
  - Impact: the fix reads correctly but an agent still merges the turns.
  - Early validation: the Stage 2 transcript replay.
  - Mitigation: the question is the welcome's final line; record that a live reinstall is pending.

## Stage 1 — Welcome asks the guidance question alone

**Estimate: 0.15**

- Goal: `WELCOME.md` asks the AGENTS.md question in its own turn and handles every reply.
- Dependencies: approved plans; the product branch exists.
- Expected changes in `WELCOME.md`:
  - The opening "Agent instructions" says the welcome turn ends with the guidance question only.
  - "Offer optional project guidance": show the text, ask a yes/no question as the final line, and stop.
  - A new short "Handle the reply" section covers yes (the existing consent edit), no (honor it, don't repeat), task or other non-answer (don't edit; one-line "AGENTS.md: not added; ask any time"; don't re-ask this session), an existing section (propose an update), and the outcome line (added, declined, or not answered).
  - "Invite the first task" now runs after the reply; a task supplied with the install request is started then, without asking again.
  - The old "unanswered … do not repeat or block" sentence is removed.
- Verification approach:
  - Walk five scenarios through the final text: yes, no, task-instead, existing section, task supplied with the install request.
  - Grep for the obsolete phrasing.
  - Product link check, Git-workflow fixture, `git diff --check`, and the file-scope check.
- Estimate details: driver: rewording without changing consent rules; uncertainty: keeping the welcome short.
- Risks or open questions:
  - Impact: over-blocking.
  - Early warning / validation: the task-instead scenario.
  - Mitigation: proceed immediately on a non-answer.
- Canonical components/API contracts touched: the `WELCOME.md` sections. The guidance text block itself is unchanged.

## Stage 2 — README alignment and transcript replay

**Estimate: 0.10**

- Goal: the README matches, and the reported failure is replayed as acceptance evidence.
- Dependencies: Stage 1.
- Expected changes:
  - README Quick start step 1 (line 67) and step 2 (line 71): the welcome asks the guidance question first, and a task reply is noted as "not added".
  - In `railspike-dev`, a scenario verification record with the five scenarios and a replay of the maintainer's pasted transcript against the new text.
- Verification approach:
  - The replay shows the first turn ending with the guidance question and no task question.
  - The README and `WELCOME.md` are checked against each other.
  - Product link check, Git-workflow fixture, `git diff --check`, scope check, and the dev link check.
- Estimate details: driver: consistency between the two files; uncertainty: low.
- Risks or open questions:
  - Impact: live agents may still combine the two turns.
  - Early warning / validation: the maintainer's reinstall.
  - Mitigation: record it as pending; it is not a pass.
- Canonical components/API contracts touched: the README Quick start (no other sections; the uninstall wording stays as it is).

## Scope and estimate history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| 2026-10-28 — Step 2 handoff, v1 | 0.30 | Retained. |
| 2026-10-28 — Step 3 handoff, v1 | 0.30 | Reaffirmed. Two stages plus planning and records; a possible beta is included in the cycle total but has no stage, because it needs a separate request. The stage values are not additive. Single exposed Claude Code rater, R1/P2. |

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*
