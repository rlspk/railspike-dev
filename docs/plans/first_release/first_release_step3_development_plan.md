> **Feature plan:** [Step 1](./first_release_step1_solution_assessment.md) · [Step 2](./first_release_step2_feature_description.md) · [Step 3](./first_release_step3_development_plan.md) · [Step 4](./first_release_step4_implementation_summary.md)

Debug mode: disabled

## Completion Contract
- Release maintenance: verify a reviewed revision on published product `main`, publish its signed annotated `v0.1.0` tag and matching GitHub release, and retain public notes plus adoption/recovery guidance. Inspect partial publication before retrying; never move a published tag.
- Scope: `docs/maintainers/releases/v0.1.0.md`, this feature's records and required plan organization/index links, the release backlog entry, and product tag/release operations. No product/website repairs, unrelated merges, or runtime changes. Public linked evidence must be available before publication; all required checks must pass.
- After Step 3 approval, create a dedicated development feature branch, organize and commit approved plans first, then create the summary. Each stage takes at most one hour and ends with verification, summary update, and its own commit before the next stage. Tag the verified published product revision independently of the development branch.

## Key Risks
- **Candidate drift:** remote `main` was `579c0c13956be36c308e50df60b1849f9e213da6` on 2026-10-14; the local product checkout is on a different branch. Refresh and select published `main` in a clean isolated checkout, record its full ID, and recheck before tagging; changed candidates require renewed verification.
- **Signing/access:** GPG secret-key material exists, but signing is unproven and GitHub CLI is unauthenticated. Validate signing and authorized publication access in Stage 1; unresolved access blocks publication without weakening the signed-tag requirement.
- **High risk: publication/recovery:** no remote tags or public releases were found on 2026-10-14; retries or concurrent publication can conflict. Inspect again before mutation, record object/commit identities, and resume only matching states; stop on conflicts.
- **Readiness:** historical completion does not verify current links/installations. Validate the exact candidate and public evidence in Stage 2; failures block release and substantial repairs require separate work.

## Stage 1
- Goal: establish a usable candidate and release capabilities.
- Dependencies: approved Step 3 and initial planning commit.
- Expected changes: summary records candidate ID, clean isolated checkout, version availability, signing verification method, and repository permissions; preserve existing worktrees.
- Verification approach: refresh remote main/tags and inspect releases, test signing in disposable local material, and confirm authenticated product/development write access without publishing.
- Risks or open questions: missing credentials or unusable keys block dependents; resolve through existing authorized credentials or maintainer setup, never expose secrets or create an unsigned substitute.
- Canonical components/API contracts touched: product Git refs, existing signing tools, GitHub authentication and release metadata.

## Stage 2
- Goal: prepare a verified candidate and reviewable release notes.
- Dependencies: Stage 1 committed; candidate and capabilities established.
- Expected changes: create version-specific notes with workflow contract, limitations, migration, deliberate updates/recovery, and candidate evidence; record check results in the summary.
- Verification approach: run product Markdown, Git-workflow, whitespace, and published-candidate installation/separation fixtures; review README examples and rename/website readiness; verify public note/evidence destinations and relevant development links. Report unrelated draft/historical link failures separately without suppressing them.
- Risks or open questions: broken evidence or failed checks block Stage 3; defer substantial repairs and reverify any changed candidate. Publish required development evidence before the release; keep notes consistent with its exact revision.
- Canonical components/API contracts touched: existing release policy/checkers, product README/welcome/recovery guidance, website, and release-notes document.

## Stage 3
- Goal: publish and verify the complete consumer release.
- Dependencies: Stage 2 committed; candidate and notes reviewed; required evidence public and blockers resolved.
- Expected changes: verified signed annotated product tag and matching public GitHub release, completed backlog entry, and summary recording final URLs, tag object, full product commit, signing result, and paired development commits.
- Verification approach: recheck candidate/version/remote state, verify the signature and peeled commit before pushing, create the release from the existing remote tag, then independently read back tag/release identities and public notes/links. Commit the stage summary and backlog outcome.
- Risks or open questions: if interrupted, record actual remote state; resume a matching tag without recreating it, complete a missing release, or verify an already matching release. Conflicting identities block completion; published-revision corrections need a new version and renewed scope approval.
- Canonical components/API contracts touched: signed Git tags, GitHub release surface, existing release policy, development notes/backlog/summary.

## Maintainer-authorized signing policy revision
The maintainer explicitly requested an unsigned annotated tag and deferred maintainer signing setup to `todo.txt`. This supersedes the signed-tag/signing-capability requirements above: verify the annotated tag object and exact peeled product commit, record that it is unsigned, and do not claim signer authentication. Stage 1 needs repository access and tag capability, not a signing key; Stage 3 uses an unsigned annotated tag. Scope additionally permits updating the canonical release policy, its backlog wording, and the requested signing follow-up in `todo.txt`. Prior approvals and completed records remain in history; this explicit instruction authorizes the revision and continuation.
