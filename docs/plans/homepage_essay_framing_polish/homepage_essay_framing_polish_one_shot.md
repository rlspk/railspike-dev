Cycle: `railspike/homepage_essay_framing_polish`; Mode: one-shot; Record/index: [plan index](../README.md); predecessor [homepage_essay_framing Step 4](../homepage_essay_framing/homepage_essay_framing_step4_implementation_summary.md)

Debug mode: enabled

Effort study: `railspike-effort / railspike/homepage_essay_framing_polish`; standing enrollment (AGENTS.md, 2026-10-21); [ledger](../../research/effort_estimation/collection.md)

Extended estimates: enabled (no real alternatives or work units, so there are no option or unit estimates)

**Cycle estimate: 0.20**

Status: technically complete; committed on unmerged branches; next permitted action: maintainer review (merge, push and publication are not authorized).

## Original request

> This looks great, I want to make a few small modifications:
>
> - Move the copy button into the bottom right corner of the prompt text area.
> - Add some kind of stronger way to divide the essay from the top part.
> - Add a formatted version of the markdown prompt and display it by default.

## Authorization

- 2026-10-28: the maintainer chose **"One-shot (Recommended)"**. The question offered this as authorizing the three changes now as a bounded one-shot on the same unmerged branches, with one record, a branch commit, and nothing merged.
- On the third request, the maintainer confirmed the interpretation **"Yes, formatted + raw toggle"**: the plan-prompt example after the essay is shown as rendered Markdown by default, with a "Show raw Markdown" toggle that works without JavaScript.
- Exclusions: no merge, push, tag, or publication. No essay text changes. No product README changes. No other page changes.

## Outcome and work type

- Application change to `rlspk.github.io/index.html` only, plus this record, the debug log, the plan index entry, and the ledger row in `railspike-dev`.
- Branch reuse: `rlspk.github.io` `feature/homepage-essay-framing` (unmerged, at `d219728`) and `railspike-dev` `feature/homepage-essay-framing` (unmerged, at `cb17253`). Both were confirmed unmerged before reuse. `railspike` is untouched.

## Approach and risks

- **Copy button in the corner.** Put the button back as an overlay at the bottom right of each prompt field, keeping the shared `.prompt` pattern. The field reserves bottom padding for the button, so the text never runs under it.
  - Risk: this reintroduces the predecessor's Stage 2 overlap at 360 px.
  - Mitigation: reserve the space with padding while the field sizes to its content, then verify at 360 px.
- **Stronger divider.** Add a full-width divider drawn as a rail track (two rails with ties) between the four-step section and the essay, plus a short label above the essay title. The label sits outside `<article id="essay">`, so the essay text stays unchanged.
- **Formatted excerpt.** At build time, render the same verbatim excerpt from the limited Markdown it uses (headings, blockquote, bold, bullets, paragraphs) into HTML. Show it by default, with the raw `<pre>` inside a `<details>` toggle labeled "Show raw Markdown".
  - Risk: the rendered text diverges from the source.
  - Mitigation: a check script compares the rendered text against the Markdown with only the syntax markers removed.

## Verification and recovery plan

- Re-run the essay check against `c8043fc` and the prompt, excerpt, and anchor parity checks.
- Add a rendered-excerpt fidelity check.
- Renders at 1280×720 and narrow widths in both themes; overflow check in a 360 px iframe.
- With JavaScript off, the copy buttons stay hidden and the raw toggle still works (`<details>` needs no script).
- Recovery: revert the polish commit on the branch, which restores `d219728`.

## Starting revisions

- `rlspk.github.io` `d219728`
- `railspike-dev` `cb17253`
- `railspike` `5952bfd` (unchanged)

## Study history

| Checkpoint (UTC) | Estimate | Scope, rater and reason |
| --- | ---: | --- |
| 2026-10-28 — Intake | 0.20 | Three visual changes to one page, plus verification. The rater was exposed to the full predecessor implementation, so this is not a pre-inspection rating. Single Claude Code rater, R1/P2. The R1 hashes were verified this session. |
| 2026-10-28 — Execution entry | 0.20 | Reaffirmed against the recorded approach. The rendered-excerpt fidelity check is the main uncertainty. Plausible range 0.15–0.30. |

## Execution history

- 2026-10-28: Record created before implementation. The three requests were also logged as pending in the predecessor's Step 4 summary, which now links here.
- 2026-10-28: Implemented in `rlspk.github.io` `ae7c95f` (`index.html` only):
  - **Copy buttons.** Each prompt field and its button are wrapped in `.prompt-field`; the button sits at the bottom right with a "Copy" label (accessible name "Copy prompt"). The field reserves 3.6rem of bottom padding and a minimum height of 8rem, and sizes to its content. The status line moved under the field.
  - **Divider.** `<hr class="track">` is drawn as two rails (`--rail`, the muted gray) with amber ties (`--line`), followed by a "The story" kicker above the essay title. Both sit outside `<article id="essay">`.
  - **Example.** A formatted rendering is shown by default (headings as `h3`, blockquote, bold, bullets, `[…]` muted), generated at build time from the same verbatim excerpt. The raw Markdown is inside `<details>` with the summary "Show raw Markdown". The intro now says "as the agent wrote it in Markdown".
  - Correction versus addition: all three are additions requested by the maintainer; no corrections were needed.
- 2026-10-28: New request while executing: *"I typically perform upgrades also using the agent. There should be instructions for this too, maybe not on the homepage, but definitely in the repo."*
  - Disposition: already satisfied in the repo. The product README has "Ask your agent to upgrade Railspike" (`README.md` line 287 at `5952bfd`), with a copyable upgrade prompt, a tagged-release example, rollback guidance, and separate copy and submodule procedures.
  - Possible homepage follow-up (not done; outside this one-shot's bounds): retarget the "Updating an installation" link from `#reusing-across-projects` to `#ask-your-agent-to-upgrade-railspike` and rename it "Upgrade with your agent".
  - Approval status: pending maintainer choice.
- 2026-10-28: Renewed authorization. The maintainer replied: *"Is there an upgrade prompt already? Either way, I trust you to do it right."* This is read as authorizing the proposed homepage link change only: retarget and rename the existing link. No new homepage prompt box, since the maintainer said "maybe not on the homepage". Execution follows below.
- 2026-10-28: Implemented in `rlspk.github.io` `7bed800`. In the "Read more" list, "Updating an installation" (`#reusing-across-projects`) is now "Upgrade with your agent" (`#ask-your-agent-to-upgrade-railspike`). Verification: the essay is identical; the prompt and excerpt checks pass; the new anchor exists in the README heading "Ask your agent to upgrade Railspike"; `git diff --check` is clean. This is an addition, not a correction. The cycle estimate is unchanged at 0.20: a one-line link change is within the original estimate's range.

## Outcome

- All three authorized changes were delivered. The upgrade request was already satisfied by the README; the homepage link now points directly at that README section (renewed authorization).

## Verification

All passed unless stated otherwise:

- Essay check: identical to `c8043fc`, 4,970 characters.
- Parity check: install ×2 and uninstall prompts match the README; the raw excerpt sections are verbatim from `8e89733` (on `origin/main`); the README anchors exist.
- New fidelity check: the rendered excerpt text equals the Markdown with only the syntax markers removed (1,188 characters).
- 360 px iframe overflow: none (345/345).
- Renders, saved to the scratchpad `renders/polish/`:
  - 1280 light top: the button sits in the corner with no text overlap; the track divider and "The story" label are visible.
  - 360 px light top: the button sits below the last prompt line, inside the field.
  - 500 dark example: formatted rendering.
- With JavaScript off: the buttons stay hidden, and `<details>` toggles natively.
- Pending: the open state of the raw toggle was not captured in a render; contrast is unchanged because no new text colors were added (rail and tie colors are decorative).
- `git diff --check`: clean.

## Commit/merge/publication status

- `rlspk.github.io` `ae7c95f` and `7bed800` on `feature/homepage-essay-framing` (unmerged, unpushed).
- `railspike-dev` record commits: `6d030f6`, plus this update (hash reported in the handoff).
- `railspike`: unchanged at `5952bfd`.
- Release order is unchanged: product first, then website, each with explicit authorization.

## Study closeout

**Retrospective cycle scope: 0.20**

- Judged separately; not measured labor. The delivered scope matched the authorization, and the fidelity check went in without trouble. Single exposed Claude Code rater, R1/P2.
- Maintainer fit/acceptance: pending.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*
