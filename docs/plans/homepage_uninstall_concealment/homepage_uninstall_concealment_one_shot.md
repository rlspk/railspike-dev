Cycle: `railspike/homepage_uninstall_concealment`; Mode: one-shot; Record/index: [plan index](../README.md); predecessor [homepage_essay_framing_polish](../homepage_essay_framing_polish/homepage_essay_framing_polish_one_shot.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/homepage_uninstall_concealment`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md)

Extended estimates: enabled (no real alternatives or work units)

**Cycle estimate: 0.10**

Status: technically complete on `feature/uninstall-prompt-concealed` (unmerged, unpushed); next permitted action: publish only on the maintainer's explicit request.

## Original request

> One more thing: I want to conceal the uninstall prompt, because I think people can copy it accidentally instead of the install one. Or, perhaps, there's a better way to distinguish it?

## Authorization

- 2026-10-28: The maintainer stated the change they wanted (conceal the uninstall prompt) and asked for a better alternative. I recommended combining the two in conversation: conceal the prompt and distinguish its copy button. That combined approach includes the requested concealment, so it is executed under that instruction.
- Exclusions:
  - Publication. The previous "release to the live site" covered the earlier state only, so I ask again before pushing `main`.
  - Changes to the prompt text, the README, or other sections.

## Outcome and work type

- Application change to `rlspk.github.io/index.html` on the new branch `feature/uninstall-prompt-concealed`, created from `main` `711ad38`. The previous feature branch is merged and therefore ineligible for reuse.
- Plus this record, its debug log, the plan index entry, and the ledger row in `railspike-dev`.

## Approach and risks

- Wrap the uninstall prompt box in a `<details>` element that starts closed, with the summary "Show the uninstall prompt". The prompt text stays in the page and still matches the README.
- Give the uninstall copy button an outline style and the label "Copy uninstall prompt", plus its own confirmation message. The install buttons stay filled blue and labeled "Copy".
- Risk: the corner button must still not cover text once the box is opened. Verify the open state at a narrow width.

## Verification and recovery plan

- Essay and parity checks.
- Renders of the closed and open states.
- With JavaScript off, the toggle still works natively.
- Overflow check at 360 px.
- Recovery: delete the branch, or revert the commit.

## Starting revisions

- `rlspk.github.io` `711ad38` (live)
- `railspike-dev` `ca6dc13`
- `railspike` `5952bfd`

## Study history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| 2026-10-28 — Intake | 0.10 | One component change plus checks. Exposed rater with full knowledge of the page; single Claude Code rater, R1/P2. |
| 2026-10-28 — Execution entry | 0.10 | Reaffirmed. |

## Execution history

- 2026-10-28: Record created before implementation.
- 2026-10-28: Implemented in `rlspk.github.io` `189733b`:
  - The "Removing Railspike is one prompt too…" note is now a plain line above a closed `<details class="reveal">` with the summary "Show the uninstall prompt" and a ▸/▾ marker. The native marker is hidden because the summary's flex layout had removed it; it was put back as an addition during verification.
  - Inside: the new label "Paste this into your coding agent to remove Railspike:", the same prompt text, and an outline `.copy-button.secondary` labeled "Copy uninstall prompt", with `data-copied` set to "Copied the uninstall prompt." The shared script now uses `data-copied` when present. Install buttons are unchanged.
- Verification (all passed):
  - Essay identical to `c8043fc`; prompt, excerpt, and anchor parity checks pass. The uninstall prompt is still in the page and matches the README.
  - Renders: closed at 1280 light, showing only the toggle and the marker; open at 360 light and 500 dark, with the outline button in the corner and no text overlap.
  - 360 px iframe with the toggle open: no overflow (345/345).
  - Without JavaScript, `<details>` is native.
  - `git diff --check` is clean.
  - Not verified: the copy confirmation text in a real browser clipboard (headless only).

## Outcome

- Delivered as authorized.
- Publication pending: the live site still serves `711ad38`, which shows the uninstall prompt openly.

## Commit/merge/publication status

- `rlspk.github.io` `189733b` on `feature/uninstall-prompt-concealed`, created from `main` `711ad38`; not merged or pushed.
- `railspike-dev`: this record commit (hash in the handoff).

## Study closeout

**Retrospective cycle scope: 0.10**

- Judged separately; not measured labor. Single exposed Claude Code rater, R1/P2.
- Maintainer fit/acceptance: pending.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*
