# Repository separation

- Product: https://github.com/rlspk/railspike — user instructions, installation/update guidance, license.
- Development: https://github.com/rlspk/railspike-dev — plans, logs, research, maintainer records, and checks.
- Website: https://github.com/rlspk/rlspk.github.io — static source published at https://rlspk.github.io/.

## Preservation

The [manifest](./separation_manifest.json) records SHA-256 hashes and source revision `b59f7df89842ba17f710ae1f2dc955bb361cc620`. Companion commit `ceefc041a847b252d1a9a97175912937a745ea06` preserves those original files, verified through a fresh remote clone. Later link repairs and tooling changes are separate commits. Original product history is retained in the product repository; no history was rewritten. The old `gulkily/railspike` repository/site are left intact.

Unrelated untracked planning drafts, `installation_log.txt`, `railspike.txt`, `todo.txt`, and ignored workspace files stay in the original local checkout. They were not included in this publication. Recovery bundle, inventories, and untracked backups are recorded in the [implementation summary](../plans/separate_development_content/separate_development_content_step4_implementation_summary.md).

## Historical references

[Exact historical link exceptions](./historical-link-baseline.txt) acknowledge preserved research transcripts whose relative links refer to other projects, and three references to untracked local source documents. Those are evidence, not live navigation or new broken-link exemptions. The checker reports the acknowledged count and rejects stale exceptions. Fix live links normally; never broadly exclude the research tree.

## Ownership and recovery

Future Railspike plans/logs live only in this development repository. Product and website edits go to their own checkouts; summaries record their revisions. There is no runtime or installation dependency on this checkout.

Before removing or replacing content, verify its preservation commit and retain the previous usable revision. On partial publication, inspect all remote revisions and restore only owned, unchanged paths from that revision; preserve later edits for reconciliation. Do not reset or force-push a repository to recover. Existing consuming projects use the source-migration and update instructions in the product README.

## Published result

The product distribution at `59858599cf98d3d5e0502fc13e58a856e364df12` contains 16 files. Website commit `05aebc7` is live at `https://rlspk.github.io/`. The development README documents the actual-history installation/migration/recovery fixture; it uses temporary repositories and never modifies the supplied product source. The archived local recovery bundle remains available; historical source documents excluded from publication remain with the original owner.
