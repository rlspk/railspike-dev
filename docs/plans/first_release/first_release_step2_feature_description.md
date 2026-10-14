> **Feature plan:** [Step 1](./first_release_step1_solution_assessment.md) · [Step 2](./first_release_step2_feature_description.md) · [Step 3](./first_release_step3_development_plan.md) · [Step 4](./first_release_step4_implementation_summary.md)

Debug mode: disabled

## Problem
Railspike needs its first verified release so consumers can deliberately install or pin a documented baseline. Approved Step 1 selects **v0.1.0**, communicating an evolving workflow contract without declaring v1.0.0 stability.

## User stories
- As maintainer, I want to release a reviewed product revision so that the first public version has traceable verification and compatibility notes.
- As a consumer, I want a verifiable version and clear update guidance so that I can adopt Railspike and recover from an unsuitable update.

## Core requirements
- Release `v0.1.0` in `rlspk/railspike` only if that version remains unused; select an exact reviewed revision on published `main` and record its full commit ID.
- Verify current rename/website readiness, public access to linked evidence, README links/examples, product Markdown integrity, and applicable installation/Git-workflow checks before publication; unresolved failures block release.
- Create and verify a signed annotated tag for the checked revision, then publish a matching GitHub release using that existing tag; record signing verification and the published tag/release identities.
- Keep concise release notes in `railspike-dev`: initial workflow guarantees and limitations, evolving compatibility, FDP/repository migration guidance where applicable, and deliberate copy/submodule update and recovery guidance.
- Preserve published tags. On interruption, inspect remote tag and release state, resume only matching publication, and escalate conflicting state; corrections to a published revision require a new version.

## Delivery scope
**Work type: application change**, specifically release/distribution maintenance with no application runtime changes. Scope is one product tag and GitHub release, release notes under `docs/maintainers/releases/`, this feature's planning/verification records, and the completed release entry in `docs/maintainers/BACKLOG.md`. Reuse existing checks and policy. Product/workflow redesign, website repairs, automation, unrelated backlog work, and merging unrelated feature branches are excluded; required substantial repairs block this cycle and become separate work.

## Completion boundary
Start with the selected product candidate and release access; finish with a publicly readable release whose signed tag resolves to the verified revision and whose notes explain adoption and recovery. Record each publication outcome so a pushed tag without a release can be completed safely. Readiness, signing, access, or identity conflicts block dependent publication; no partial publication counts as complete. Prepare the candidate and notes for review before publishing.

## Risks
- **Candidate drift:** releasing unchecked or unmerged work invalidates evidence. Before Step 3, inspect candidate/branch state; pin the reviewed revision and recheck its identity before tagging.
- **Signing/access:** unavailable credentials or signing prevent a verifiable release. Before Step 3, establish available signing and repository access without exposing secrets; resolve missing capability before publication, never substitute an unsigned tag.
- **Readiness/evidence:** stale website, examples, or inaccessible links can mislead consumers. Before Step 3, identify required checks and linked evidence; verify the current candidate and public destinations before release, deferring substantial repairs.
- **Partial/conflicting publication:** retries can replace a consumer's pin or duplicate a release. Before Step 3, inspect existing tags/releases and define resumable states; retain published identities and stop on mismatches.

## Shared component inventory
Reuse the canonical [release policy](../../maintainers/RELEASES.md), product README/`RAILSPIKE.md`/welcome and recovery guidance, existing development checkers, and GitHub's tag/release surfaces. Add one version-specific release-notes document; no new UI, API, or release engine is needed.

## Simple user flow
1. Maintainer reviews the exact candidate, verification evidence, and `v0.1.0` notes.
2. Maintainer publishes the verified signed tag and matching release, recovering any interrupted publication against the recorded identities.
3. Consumer reads compatibility/update guidance and deliberately installs or pins the released revision.

## Success criteria
One published `v0.1.0` release references one verified signed annotated tag resolving to the recorded full product commit ID. Required readiness checks pass for that revision, all release-note evidence links are public, adoption/recovery guidance is present, and the development summary records final publication identities and verification with no unresolved release blockers.
