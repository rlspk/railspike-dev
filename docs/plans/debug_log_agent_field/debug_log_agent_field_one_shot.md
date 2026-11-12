Cycle: `railspike/debug_log_agent_field`; Mode: one-shot; Record/index: [plan index](../README.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/debug_log_agent_field`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md)

Extended estimates: enabled (no real alternatives or work units)

**Cycle estimate: 0.10**

Status: planning commit pending; next permitted action: commit this record, then edit the product.

## Original request

> Also, for at least a few days now, the agents should have been reporting which agent it is in the plans themselves. And yes, we should definitely add that to the debug log.

> We can probably one-shot the agent logging in debug, right? It's a pretty straightforward, simple change.

## Authorization

- 2026-11-12: "go ahead with the plan length guidance change, please", then corrected: "sorry, that was for the one-shot. i have not reviewed the plan yet." This authorizes the debug-log agent field as a one-shot.
- Exclusions:
  - The plan length guidance cycle, whose Step 1 awaits review.
  - Merge, push, tagging and release.
  - Rewriting existing debug logs.

## Outcome and work type

- Application change to Railspike instructions: each new debug log entry carries one attribution line under its timestamp and step identifier.
- Product files: `RAILSPIKE.md` (Persistent debug log) and `docs/workflow/one_shot.md` (Study and debug state).
- Development files: this record, its debug log, the plan index entry and the ledger row.

## Approach and risks

- Reuse the existing [agent attribution](../../../../railspike/RAILSPIKE.md#agent-attribution) format and its verified-metadata rule. No new naming rules.
- Risk: agents may treat the line as a second, competing attribution rule. Mitigation: link to the existing section instead of restating it.
- Risk: agents may backfill attribution into old entries. Mitigation: state that the line applies to new entries only.

## Reuse decisions

- Reuse the attribution section in `RAILSPIKE.md` unchanged.
- Extend the one sentence in each file that already lists required entry fields.

## Completion conditions

- An agent reading either file knows to add one attribution line to each new debug log entry.
- Plans are unaffected. Old logs stay as they are.
- Recovery: revert the product commit.

## Concepts touched

None. The concept inventory has no entry for debug mode or attribution.

## Verification and recovery plan

- Read both changed sentences in context and check the anchor link resolves.
- Check the diff touches only the two product files.
- Live agent compliance is not tested in this cycle.

## Starting revisions and branch

- `railspike` `5d54e06` on `main`; branch `feat/debug-log-agent-field`
- `railspike-dev` `4e2c538` on `main`; branch `feat/debug-log-agent-field`

Planning commit: pending

## Study history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| 2026-11-12 — Intake | 0.10 | Two-sentence instruction change plus checks. Exposed rater: the scope was discussed and v3 debug logs were inspected first. Single Claude rater, R1/P2. |
| 2026-11-12 — Execution entry | 0.10 | Reaffirmed. |

## Execution history

- 2026-11-12: Record created before implementation.

*— Claude · 2026-11-12 UTC · Model: claude-opus-5-5*
