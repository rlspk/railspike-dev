> **Feature plan:** [Step 1](./first_release_step1_solution_assessment.md) · [Step 2](./first_release_step2_feature_description.md) · [Step 3](./first_release_step3_development_plan.md) · [Step 4](./first_release_step4_implementation_summary.md)

Debug mode: disabled

## Cycle
- Development branch: `feature/first-release`; planning commit: `c195ad9`.
- Work type: release/distribution maintenance under approved Steps 2–3. No product or website changes, unrelated merges, or runtime changes.
- Approved plans organized here with their substantive content preserved; maintainer links and plan index repaired. Unrelated local edits/untracked drafts remain outside this cycle's commits.
- Status: Stage 1 complete following the maintainer-authorized policy revision permitting an unsigned annotated tag. Stages 2–3 pending; no product tags or GitHub releases created or published.

## Stage 1 - Candidate and release capabilities
- Changes: fetched product `origin/main` and tags; created clean detached worktree `/tmp/railspike-first-release-candidate` at `579c0c13956be36c308e50df60b1849f9e213da6`. The existing product branch/worktree was preserved.
- Verification: remote main matches the candidate; remote tags and public GitHub releases are empty on 2026-10-14. Both product and development repositories are publicly readable. Candidate worktree is clean.
- Signing: the first probe selected an expired key and failed without producing a release artifact. Both nonexpired secret keys successfully signed disposable probe files, and both detached signatures verified. Available signing fingerprints: `A3ADDCAD53A2CBCF6747161BEFD536972F21CC35` and `C2109D4C7F97938300FF78A984FDC6728427104D`. Git signing key is not configured; explicitly select and record the appropriate maintainer key for the eventual tag. Temporary probes were removed.
- Access: initially unavailable (checkpoint `8173562`); after maintainer authentication, GitHub CLI identifies `gulkily`, and authenticated repository API checks confirm admin/push permissions for both product and development repositories. Remote main remains the selected candidate; no tags/releases appeared. No secrets were displayed or changed.
- Signing identity blocker: both keys also passed signed annotated Git-tag creation and `git tag -v` in a disposable repository. Their UIDs are `testing` and `forum-user`; neither is configured as the maintainer Git signing key, and the account's public GPG/SSH signing-key lists are empty. Requested an explicit maintainer key selection rather than inferring identity from secret-key availability. No key registration or account settings changed.
- Notes: the maintainer subsequently identified both usable local keys as throwaway keys and declined their use. Neither may sign this release. Establish an appropriate maintainer key before finishing Stage 1; then recheck remote candidate/version/release state. Do not begin Stage 2 before Stage 1 verification and its completion commit.
- Checks: planning commit and summary are limited to authorized files; whitespace and feature-local Markdown links pass. Product readiness, fixtures, public evidence verification, and release operations remain pending in their approved stages.
- Resolution: the maintainer explicitly authorized revising the release policy to allow an unsigned annotated tag and requested future signing setup in `todo.txt`. Updated `RELEASES.md`, active backlog wording, and appended superseding requirements to Steps 1–3 without removing their historical approved text. Both throwaway keys remain excluded.
- Final verification: a disposable unsigned annotated Git tag had object type `tag` and peeled to its expected commit; repository push permissions remain confirmed, candidate worktree is clean, remote main remains the recorded ID, and no tags/releases exist. Stage 1's signing blocker is resolved by the authorized requirement change. Signing status and exact tag/commit identities remain required release evidence.
- Stage commits: initial checkpoint `8173562`, access checkpoint `1b0d730`, throwaway-key exclusion `7a64e21`; the commit containing this resolution completes Stage 1.

## Requests
- Request: exclude the `testing` and `forum-user` throwaway keys from release signing. Disposition: in-scope signing-identity refinement; accepted on explicit maintainer instruction. Outcome: both excluded; maintainer key setup remains pending. The signed-tag requirement is unchanged; no keys were created, deleted, or registered.
- Request: revise the policy to permit an unsigned annotated release tag and add signing setup to `todo.txt`. Disposition: changed requirement explicitly authorized by the maintainer; signing requirements and allowed file scope superseded in Steps 1–3. Outcome: policy, backlog, and future signing task updated; Stage 1 complete. Verification: disposable annotated-tag identity checks, whitespace, and feature links. No keys or account settings changed; previously published tags must remain fixed.
