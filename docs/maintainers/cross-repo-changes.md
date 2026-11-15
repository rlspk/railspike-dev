# Changing Railspike and a consuming project together

Some workflow rules need two homes. One is the consuming project's `AGENTS.md`, which every agent reads whether or not it runs Railspike. The other is the Railspike product, which turns the rule into a checkpoint and makes sure it gets recorded. This runbook covers what goes where, which repository gets which commit, and the order to do them in.

Worked example used throughout: **tests that fail on the base commit get fixed, not just reported.** It came up when a test in a consuming project failed before any changes on the branch were applied.

## What goes where

| Layer | Repository | What it holds | Example change |
| --- | --- | --- | --- |
| Rule | Consuming project (`AGENTS.md` at its root) | The standing norm, written for any agent, plus project specifics (how to run one test, how to re-run it on base) | "If a test fails on the base commit, fix it as part of the work." |
| Checkpoint | `rlspk/railspike` (product) | Workflow instructions that make the rule happen and leave evidence | Step 4 check: confirm the failure on base, fix it in its own commit, note it in the stage summary |
| Template (optional) | `rlspk/railspike` (product) | Suggested `AGENTS.md` lines a host project can adopt | A one-line baseline-failure rule offered during installation/welcome |
| Records | `rlspk/railspike-dev` (this repo) | The plan, stage summaries, paired commit IDs, this runbook | `docs/plans/<feature>/…` |
| Installation | Consuming project (`docs/railspike`) | The installed Railspike revision (a copy or a submodule pointer) | Update to the product revision containing the checkpoint |
| Website | `rlspk/rlspk.github.io` | Public copy | Usually untouched; only if the change is user-visible enough to describe |

Ask which layer a sentence belongs to: should it hold even when no Railspike cycle is running? If yes, it goes in the project's `AGENTS.md`. Is it about *when* something is checked and *where it is recorded* during a cycle? Then it goes in the product.

## Order of work

1. **Plan here.** Start the cycle in `railspike-dev/docs/plans/<feature>/` like any Railspike work on Railspike itself (see the [README](../../README.md#working-on-railspike)). Step 1/2 should state which layers the change touches. The continuing effort study applies (see [AGENTS.md](../../AGENTS.md)).
2. **Project rule first.** Commit the `AGENTS.md` change in the consuming project on its own. It works with any Railspike version, and with none, so nothing needs to wait for it.
   - Commit message: `AGENTS.md: fix tests that fail on the base commit`
   - Keep it to the rule plus project-specific commands. Don't copy Railspike workflow text into it.
3. **Product change on a branch.** In a separate `railspike` checkout, branch (for example `feat/fix-baseline-failures`) and edit the instruction files. For the worked example, the current text only asks agents to *identify* baseline failures:
   - `docs/workflow/implementation_standards.md`: "identifying reproduced baseline failures"
   - `docs/workflow/step4_implementation_after.md`, item 7: "Identify reproduced baseline failures."

   Change those into the checkpoint, and touch the matching concept entry if one exists. Run the product checks from the [README](../../README.md#checks) (`check-markdown-links.py ../railspike`, `check-railspike-git-workflow.sh ../railspike`, `git diff --check`).
4. **Record the pairing here.** Commit the stage summary in `railspike-dev` with both commit IDs: the project's `AGENTS.md` commit and the product commit (repository + full SHA each). The [CONTRIBUTING](../../CONTRIBUTING.md) rule "record paired commit IDs" means this.
5. **Release, only if asked.** Publishing a beta follows [RELEASES.md](./RELEASES.md). Propose an exact version and stop for confirmation before tagging.
6. **Update the project's installation.** Once the product revision exists (merged, or a named tag), update `docs/railspike` in the consuming project using the product README's update procedure for its installation type (copy or submodule). Commit that update separately from the `AGENTS.md` commit. For a submodule it's just the pointer change, e.g. `Update Railspike to <tag or short SHA>`.
7. **Close out here.** Add the installation-update commit to the summary. List the projects that haven't been updated yet as pending, not done.

## Commits at a glance

| Repository | Commit | When |
| --- | --- | --- |
| `railspike-dev` | Step docs (one per approved step) | As each step is approved |
| Consuming project | `AGENTS.md` rule | Step 2 above, any time after approval |
| `railspike` | Instruction checkpoint (branch) | Step 3 above |
| `railspike-dev` | Stage summary with paired SHAs | After each product/project commit |
| Consuming project | Railspike installation update | After the product revision exists |

Never put development records in the product or the project, and never put product instruction edits in `railspike-dev`. That's the same separation as [REPOSITORY_SPLIT.md](./REPOSITORY_SPLIT.md).

## Wording to reuse for the worked example

For a consuming project's `AGENTS.md`:

```markdown
## Failing tests

If a test fails on the base commit, before our changes, fix it as part of the current work. Confirm it fails on base first, then fix the test or the code it covers, and commit that fix separately from the feature. If the fix needs a decision (flaky infrastructure, an external service, a large rewrite), stop and ask; don't skip it silently.
```

Add the project's own command for running a single test under that heading.

*— Claude · 2026-11-15 UTC*
