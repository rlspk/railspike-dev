# Railspike development guidance

Product changes belong in `../railspike`; development records belong here. Preserve unrelated local work. Follow the release policy in `docs/maintainers/RELEASES.md`.

Before minting any beta or stable release, finish preparation, propose the exact version number, and stop for the user's explicit confirmation before creating a tag or publishing. A generic request for a new release or a version increment is not confirmation of an exact version.

Never increment the major version unless the user specifically asks. Avoid incrementing the minor version unless the user specifically asks. Increment the revision (patch component) only for a new functionality addition. Continue the current beta series by changing its beta suffix when requested; workflow-contract changes alone do not authorize a major or minor increment.

## Continuing effort study

The maintainer enrolled every future Railspike cycle in the same `railspike-effort` data collection on 2026-10-21. Follow [the collection protocol](docs/research/effort_estimation/collection.md), retaining R1 and append-only score/scope histories. Collect independently of debug mode and include incomplete, paused and abandoned cycles. No per-cycle study selection question is needed. This authorizes collection, not implementation, uploads or release publication.
