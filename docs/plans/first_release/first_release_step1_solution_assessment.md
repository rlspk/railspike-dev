> **Feature plan:** [Step 1](./first_release_step1_solution_assessment.md) · [Step 2](./first_release_step2_feature_description.md) · [Step 3](./first_release_step3_development_plan.md) · [Step 4](./first_release_step4_implementation_summary.md)

Debug mode: disabled

## Original Query
As maintainer, I want to choose and tag the first release version. Please write Step 1 of railspike.md.

## Understood Intent
Assess the first Railspike release using the existing [release policy](../../maintainers/RELEASES.md): semantic versioning, a signed annotated tag, and a corresponding GitHub release. This step selects a proposed direction; release execution belongs to later approved work.

## Problem
Railspike needs a first version that communicates its intended stability and gives consumers a verified revision to pin without overstating release readiness.

## Option A — Start with v0.1.0
Publish an initial release that explicitly leaves room to refine the workflow contract, with concise release notes explaining its current guarantees and limitations.

- **Pros:** Establishes a useful baseline now; fits a workflow still gathering installation and agent-compatibility evidence.
- **Cons:** Signals an evolving contract; consumers need clear notes about changes even before v1.0.0.

## Option B — Start with v1.0.0
Declare the current approval, artifact, branch, and commit requirements the stable baseline, applying the existing major/minor/patch policy to subsequent releases.

- **Pros:** Makes a clear stability commitment; gives consumers a straightforward compatibility baseline.
- **Cons:** Requires confidence in the contract and supported usage; future required process changes warrant major releases under the repository policy.

## Recommendation
Choose **Option A, v0.1.0**, retaining the documented version-change categories and explicitly describing the evolving contract. The [backlog](../../maintainers/BACKLOG.md) marks website and installation verification complete; these historical checks support readiness but do not establish a stable contract for the current revision. Recent workflow changes and limited compatibility evidence favor an initial baseline before a v1.0.0 commitment. The unreleased FDP rename does not by itself establish a prior public version to increment.

- **Release conditions:** Confirm rename and website readiness for the current revision, public access to linked evidence, README links and examples, and repository checks before release. No local or remote product tags were found on 2026-10-14 (`git ls-remote --tags origin` succeeded); recheck version availability and signing capability before creating the signed annotated tag. Select the reviewed, merged product revision, not an unmerged feature-branch tip.
- **Complete slice:** Maintainer selects the version and reviewed revision; consumers receive a verifiable tag and matching GitHub release with workflow-contract and migration notes. Keep the tag fixed once published; record and recover any partial publication without silently replacing it.
- **Scope:** One release cycle, feasible within a day if readiness checks pass. Substantial website, example, or workflow repairs become separate work that blocks publication; release automation and unrelated backlog work are excluded.

## Maintainer-authorized signing policy revision
The maintainer explicitly requested an unsigned annotated tag and deferred maintainer signing setup to `todo.txt`. This supersedes the signed-tag/signing-capability requirements above: verify the annotated tag object and exact peeled product commit, record that it is unsigned, and do not claim signer authentication. Stage 1 needs repository access and tag capability, not a signing key; Stage 3 uses an unsigned annotated tag. Scope additionally permits updating the canonical release policy, its backlog wording, and the requested signing follow-up in `todo.txt`. Prior approvals and completed records remain in history; this explicit instruction authorizes the revision and continuation.
