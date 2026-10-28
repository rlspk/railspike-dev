# Welcome guidance question: scenario verification

Date: 2026-10-28 UTC. Product reviewed: `railspike` `feature/welcome-guidance-question`, `WELCOME.md` at `a35f0d5`, with the Stage 2 README change. Baseline: `5952bfd` (`v0.4.0-beta.2`). Cycle: `railspike/welcome_guidance_question`.

## Evidence boundary

These are manual walk-throughs of the written instructions. They show that the text gives one consistent next action for each reply. They do not show that a live agent follows it. The maintainer's reinstall in a disposable project is still **pending**.

## Replay of the reported transcript

The maintainer installed `v0.4.0-beta.2` into another project on 2026-10-28. The relevant end of that welcome turn was:

> Would you like that persistent guidance? WELCOME.md (docs/railspike/WELCOME.md) explicitly requires consent for this optional edit; installation is already complete.
>
> What would you like to work on first?

The old text caused this. It said to "continue with their task" when the offer is "unanswered" and to "not repeat or block on the offer", and "Invite the first task" began with "Ask what the user wants to work on" in the same welcome. Both questions therefore arrived in one turn, and the task question came last.

Under the revised text:

- The agent instructions say to "end the welcome turn with only the project-guidance question below. Ask for a task after the user replies to it."
- "Offer optional project guidance" says to end the turn with one yes/no question as its final line, and to not ask for a task or add anything after it.
- "Invite the first task" begins "After handling the guidance reply".

The same session would therefore end at "Add this to AGENTS.md? (yes/no)", without "What would you like to work on first?". **Result: the failure no longer follows from the text.** Live confirmation is pending.

## Scenarios

| Reply to the guidance question | Required next action under the revised text | Source | Result |
| --- | --- | --- | --- |
| "yes" | Inspect `AGENTS.md`, preserve unrelated guidance, create or update with consent, report the edit; state `AGENTS.md: added`; then ask for a task | Handle the guidance reply: Yes; outcome line; Invite the first task | Pass |
| "no" | Leave the file unchanged, don't offer again; state `AGENTS.md: declined`; then ask for a task. The first-task default still applies | Handle: No; outcome line; decline sentence | Pass |
| A task (e.g. "fix the login bug") | Leave the file unchanged; one-line note that it wasn't added and can be requested later; `AGENTS.md: not answered`; no re-ask this session; start Railspike planning for the task without asking for a task again | Handle: Anything else; outcome line; Invite: "unless the reply already gave a task" | Pass |
| "yes", where `AGENTS.md` already has a Railspike section | Propose an update to the existing entry instead of a duplicate; stop on conflicts | Handle: Yes | Pass |
| Install request already included a task; the user then replies "no" | The welcome turn still ends with the question. After the reply, start the supplied task without asking for it again | Agent instructions; Invite the first task | Pass |
| "later" or a question about the guidance | Treated as "anything else": no edit, one-line note, `not answered`, answer the question; the task question follows | Handle: Anything else; Invite the first task | Pass |
| "don't use Railspike" | Explicit opt-out takes precedence; honor it without repeated suggestions | Decline sentence; Invite the first task | Pass |

## README consistency

- Quick start step 1 now says the welcome "asks one yes/no question" about adding the optional guidance to `AGENTS.md`.
- Step 2 says to describe a task "after you answer the guidance question", and that replying with a task instead leaves `AGENTS.md` unchanged, reports that the guidance was not added, and starts the task. This matches `WELCOME.md`.
- No "unanswered" or "block your task" phrasing remains in either file.

*— Claude Code · 2026-10-28 UTC · Model: Claude Opus 5.5 (claude-opus-5-5)*
