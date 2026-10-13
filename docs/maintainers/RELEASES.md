# Releases and Versioning

Railspike uses semantic versioning for published releases.

Current ownership: releases and tags belong to `rlspk/railspike`; development records/checks live in `rlspk/railspike-dev`; the website is `https://railspike.dev/`. The rename note below is historical; current installation is a reviewed copy by default, with submodules on explicit request.

- **Patch:** clarifications, examples, and fixes that do not change the workflow contract.
- **Minor:** backwards-compatible new guidance, templates, or optional workflow capabilities.
- **Major:** a changed approval, artifact, branch, or commit requirement that requires consumers to alter their process.

Publish a signed annotated Git tag as `vMAJOR.MINOR.PATCH` after the README links, examples, and Markdown checks pass. Create a GitHub release from that tag with a concise list of workflow-contract changes and any migration note. Consumers pinned through a submodule choose when to update; they should review release notes before updating.

At the repository separation on 2026-10-13, no public release tags existed. Check the remote tags before choosing a version; the first release requires the public repository and its linked evidence to be available to readers.

## Where development happens

Start planning in `~/railspike-dev`, then edit the actual product files directly in a feature branch of `~/railspike`. An agent working from the development directory can edit `../railspike`; this is a workspace split, not a build or export pipeline.

| Checkout | What belongs here |
| --- | --- |
| `~/railspike-dev` | Plans, debug logs, research, test scripts, verification records, and release notes. |
| `~/railspike` | The shipped workflow instructions, welcome, user documentation, and license. Make and review product changes here. |
| `~/rlspk.github.io` | Website source and assets. |

Do not maintain a second copy of the product files in `railspike-dev` and copy it over at release time. The product feature branch is where unreleased product changes are developed. Editing that branch locally does not publish a release; review, merge, and release are separate actions. Development-tool changes are made directly in `railspike-dev`.

Keep each repository's changes in its own commits. Store the feature summary in `railspike-dev` and record the corresponding product or website commit IDs. Retain the Railspike planning approvals and stage-commit requirements.

## Publishing a product update

1. Plan the change in `railspike-dev`; implement the approved product changes on a feature branch in `railspike`. Keep plans, logs, and tooling out of the product tree.
2. Run the product checks from `railspike-dev`, review the changes, and merge the product branch into `rlspk/railspike`'s `main`. Commit the associated development records separately. Publish any development evidence linked from the release notes before releasing.
3. Check out the merged product revision and verify it before tagging. From a clean product checkout, the following brings local `main` up to date; if local `main` does not yet exist, `git switch main` normally creates it from `origin/main`.

   ```bash
   cd ~/railspike
   git fetch origin --tags
   git switch main
   git pull --ff-only origin main
   git status --short
   git log -1 --oneline

   cd ~/railspike-dev
   python scripts/check-markdown-links.py ../railspike
   bash scripts/check-railspike-git-workflow.sh ../railspike
   git -C ../railspike diff --check
   ```

   Resolve failures and confirm the product checkout is clean. When shared checker behavior changes, also run all three runtime variants as documented in the [development README](../../README.md#checks). For installation or source-migration changes, run the repository-separation fixture documented there against the published candidate revision. These checks do not require copying development files into the product.

4. Choose the version using the policy above and write release notes in `railspike-dev` describing user-visible changes, compatibility, and any migration steps. Tag the exact product commit that passed verification with a signed annotated tag. For example, **only if `v0.1.0` is the chosen, unused version** and signing is configured:

   ```bash
   cd ~/railspike
   git tag -s v0.1.0 HEAD -m "Railspike v0.1.0"
   git tag -v v0.1.0
   git push origin v0.1.0
   ```

   Confirm `HEAD` is still the reviewed commit on published `main` before tagging. Do not reuse or move a published tag; publish a new version for corrections. If publication is interrupted, inspect the remote tag and release before retrying.

5. In **`rlspk/railspike` → Releases**, create a release using the existing tag and the prepared notes. Review it before publishing. See [GitHub's release instructions](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository). If using the CLI, authenticate it separately and use `gh release create --verify-tag` so it requires the already-pushed tag; see the [CLI reference](https://cli.github.com/manual/gh_release_create).

Tags and releases belong to the product repository. Copied installations and submodule pins do not update automatically: consumers deliberately review and update their installed revision using the product README. Website updates are committed to `rlspk.github.io`; its configured Pages deployment publishes changes to `main` independently of product tags.

## Historical Railspike rename note (unreleased at the time)

Feature Development Process (FDP) is now Railspike. This is a breaking rename with no backwards compatibility: the maintainer is the only known user. The canonical repository is `gulkily/railspike`, host installations use `docs/railspike`, the main instructions are `RAILSPIKE.md`, and per-step instructions live in `docs/workflow/`. The agent shorthand is `@railspike`; select `@RAILSPIKE.md` when available. Legacy entrypoints and aliases are not provided.

The four-step workflow and approval rules are unchanged. Installation remains one `git submodule add` command. An agent handles Git updates, outlines the changes, and asks whether to commit the pointer or leave it for review. The proposed `rsp` utility was abandoned.

Publish the first release only after the rename and GitHub Pages website are ready. Version selection, the signed annotated tag, and GitHub release are follow-up work; no release is declared by this note.
