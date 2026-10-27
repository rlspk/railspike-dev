# Agent guidance and skills for Railspike

Assessment date: 2026-10-21. This is a recommendation, not an installed skill or a change to the Railspike workflow.

## Recommendation

Yes. Railspike has enough recurring, project-specific behavior to justify agent guidance. The highest-value first addition is a short root `AGENTS.md`; a focused Railspike skill is a useful second addition.

If by “skills.md” you mean a file explaining how an agent should work in this project, `AGENTS.md` is the better fit. If you mean a reusable capability that an agent can select for a particular task, use a skill directory containing `SKILL.md` (singular). A root `skills.md` would be ordinary documentation rather than the standard Codex skill entry point. Codex reads repository instructions at startup and discovers repo-local skills under `.agents/skills/`. See the official [repository instruction documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [skill documentation](https://learn.chatgpt.com/docs/build-skills).

My suggested order:

1. Add a concise `AGENTS.md` to make the repository boundaries and canonical sources easy to find.
2. Add one instruction-only `railspike-development` skill for starting and resuming work on Railspike itself, if you want a selectable workflow entry point.
3. Consider a separately scoped consumer-facing Railspike skill later. Treat that as a product integration with installation and compatibility requirements, rather than shipping the development skill to consumers.

## Why this project benefits

The [README](../../README.md), [contribution guidance](../../CONTRIBUTING.md), and [release procedure](./RELEASES.md) already contain useful instructions. The challenge is finding and applying the right ones consistently:

- Work spans three repositories. Plans and debug logs belong in `railspike-dev`, shipped instructions in `railspike`, and website sources in `rlspk.github.io`.
- Railspike already has a detailed, staged workflow in the product's `RAILSPIKE.md` and `docs/workflow/`. A new agent needs a reliable way to locate it without creating a competing copy.
- Resuming work requires identifying the current cycle, approved step, branch, debug state, and existing evidence.
- Verification depends on the change. Shared checker changes require equivalent Python, Perl, and Node.js behavior; product links must not use the development repository's historical baseline.
- Historical documents include earlier repository names and installation policies. They are useful evidence, but an agent should not mistake them for current operating instructions.

These are concrete coordination problems. More general advice about writing good code would add little value here.

## What belongs in AGENTS.md

Aim for roughly one page, mostly routing and stable constraints:

| Topic | Suggested content |
| --- | --- |
| Repository purpose | This checkout holds development records, research, and checks; it is not the installable product. |
| File ownership | A compact map of the development, product, and website repositories. Discover actual checkout locations rather than assuming a particular home directory. |
| Starting points | Read the README and contribution guidance; use the product's `RAILSPIKE.md` when entering its workflow; read release instructions for release work. |
| Existing work | Inspect the working tree and current feature artifacts; preserve unrelated edits and established cycle identity. |
| Workflow authority | Keep the product workflow canonical. Point to its approval, branch, artifact, and stage-commit rules rather than paraphrasing the full contract. |
| Verification | Link to the README's checks. State that shared checker changes require all three implementations and that the historical baseline is development-only. |
| Evidence | Distinguish observed results from assumptions and historical claims. Record paired implementation commits in the development summary as required. |
| Publication | Identify the release procedure and repository ownership; local implementation work does not itself authorize publishing. |

Avoid using this file to silently make every question, research note, or small advisory request enter a full feature cycle. State deliberately which work requires the Railspike workflow, preserving the existing contract and the user's instructions.

## What belongs in the skill

Suggested development-only location:

```text
.agents/skills/railspike-development/
  SKILL.md
```

The skill should explain when it applies, what state to recover, which authoritative instructions to read, and what a successful handoff contains. A useful outline is:

1. **Trigger and scope.** Start or resume a requested Railspike development cycle across the development, product, or website checkouts. Exclude ordinary questions about Railspike and consumer-project work.
2. **Locate the workspace.** Establish the development root and relevant implementation checkout. Check repository identity and working-tree state before edits. Do not automatically clone or rearrange checkouts just to satisfy a hard-coded layout.
3. **Restore the cycle.** Find the relevant feature artifacts, current step and phase, approval evidence, branch, completion contract, pending requests, and debug state. An existing plan is not evidence of approval by itself.
4. **Read the canonical instructions.** Open `RAILSPIKE.md` and the applicable step/phase files as directed there. Load only what the current task needs. If required files are missing, resolve that rather than reconstructing rules from memory.
5. **Apply the repository split.** Keep plans and logs in the development repository while editing implementation files in their owning checkout. Preserve paired commit records.
6. **Choose verification.** Use the README and approved plan to select checks. Keep documentation, shared tooling, installation, and release verification proportional to the actual change.
7. **Leave recoverable state.** Update the applicable artifact and report checks, unresolved blockers, and the next permitted action. Follow the canonical approval and commit requirements.

Keep this as a thin entry point. Do not copy the four step guides, all debug rules, release commands, or historical research into it. References to living sources reduce the chance of conflicting instructions after a product update.

Start without scripts or bundled templates. Add a helper only when repeated work demonstrates a need for deterministic validation, and reuse the existing checkers where possible.

## Development skill versus product skill

A development skill can know about the three-repository arrangement. A consumer skill must instead find the host project's installed Railspike instructions and keep that project's plans in its own `docs/plans/`.

A skill checked into `railspike-dev` also does not automatically become available when Codex starts in a sibling product checkout. Plan discovery and installation explicitly if cross-checkout invocation matters. The official documentation describes repository discovery under `.agents/skills/` from the current directory toward the Git root; it does not imply sibling-repository discovery.

For a future consumer integration, verify that the skill follows the installed Railspike revision, supports the documented installation modes, and preserves existing approval behavior. Keep the portable Markdown workflow usable by agents that do not support skills.

## How to decide whether it helped

Try a few representative tasks before expanding it:

- Start a new product change while working from the development checkout.
- Resume an existing cycle after losing conversational context.
- Change shared link-checker behavior and select all required runtime checks.
- Work on website content while keeping development artifacts here.
- Answer a simple advisory question without accidentally triggering a feature cycle.

Success means correct file placement, reliable state recovery, appropriate verification, and fewer repeated explanations. If the skill mostly repeats material already read through `AGENTS.md`, keep the simpler arrangement. The strongest initial improvement is making the existing sources discoverable; the skill earns its place by making a recurring workflow easier to invoke and resume.
