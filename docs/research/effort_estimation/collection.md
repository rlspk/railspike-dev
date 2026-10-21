# Continuing Railspike effort collection

Study ID: `railspike-effort`. Protocol P2 effective 2026-10-21. Reference R1 is unchanged. Maintainer instruction: “I want every future railspike to be part of the same data collection.”

Every future cycle in this development project is enrolled, including research and documentation. Existing cycles join at their next checkpoint; missing earlier scores remain missing. Collection is independent of debug mode. Use `railspike/<unique feature prefix>` here; the v3 project uses `v3/<unique feature prefix>` and retains legacy E01–E07. Copies in worktrees share the same cycle ID. Distinct follow-ups retain parent links. Ordinary tasks that do not use Railspike do not become cycles just to collect data.

Follow the reusable [checkpoint contract](../../../../railspike/RAILSPIKE.md#experimental-effort-estimation) and [R1/template](../../../../railspike/docs/effort-estimation.md). In a consuming installation, use its own installed instructions and host ledger; these local links are development-checkout links only.

Keep canonical snapshots in each feature's existing artifacts and index them below. Record scope/version, start revision, reference/protocol, UTC date, rater/exposure, total projection, change reason, approval context and evidence link. Preserve intake, handoffs, entry, revisions and retrospective closeout separately. Record unknowns instead of manufacturing history. Record actual verification, corrections versus additions, stage counts, related splits, final revisions, omissions and maintainer comfortable-fit/acceptance separately from size. Collection does not approve the work.

The v3 ledger remains at `docs/plans/effort_estimation_trial.md` in that project. Its records and this project's records belong to the same study, indexed by project/cycle identity. Integrate changes through normal Git review; compare cycle/checkpoint and content identity before aggregating. No background synchronization or upload is configured. A future review must rescan all available worktrees and retain conflicting revisions, rather than treating clones as extra trials. Six accepted outcomes are a review checkpoint, not a collection limit.

## Dataset index

| Project / record | Source | Status |
| --- | --- | --- |
| Historical calibration | [Report](./report.md), [diff review](./diff_review.md), [manifest](./source_manifest.json) | Ten purposefully selected retrospective references; not prospective outcomes |
| v3 / E01–E06 | `~/v3/docs/plans/effort_estimation_trial.md`, mirrored in `~/agent/v3-*` | Six proposals; no cycle outcomes |
| v3 / E07 | Same ledger; `docs/plans/fastmod_rubric_actions/` | Reduced v3 technically complete; 0.85 projection, 0.90 retrospective; maintainer acceptance pending |
| Collection administration | [2026-10-21 review](./2026-10-21-review.md) | Protocol/product integration, not an independently observed trial outcome |

Append one row per new development cycle with links to canonical snapshots; retain abandoned/replaced records. Keep this index within the cycle's documentation scope, respecting the planning-commit allowance and closeout cadence. Earlier source reports and frozen R1 bytes are preserved.
