# Step 3 attribution footer maintenance

2026-10-25 UTC. User requested extended estimates by default and clarified Step 3 attribution: one footer when one agent writes the whole plan in one pass; stage attribution only for stages subsequently authored or substantively revised separately; preserve earlier attribution.

Extended estimates already default to enabled for new enrolled cycles in beta 3. Verified the root contract and effort guide; no activation change was necessary. Existing explicit opt-outs and legacy cycle state remain intact.

Applied the attribution clarification to the product root contract, Step 3 generation instructions/template, Step 3 review checklist and the effort guide's two-stage example. Removed repeated stage signatures from the example and placed its one footer after all content. Model/settings remain optional and verified-only.

Product branch: `fix/step3-attribution-footer`; base `690c596307b2087515b7c258008e5835af89048b`. Four product Markdown files changed; no runtime, host-plan or release changes. Product local-link check passed (15 Markdown files), whitespace check passed, and diff/scenario review confirmed whole-plan attribution, later separate stage attribution and preserved history. Runtime tests are inapplicable to this text-only maintenance.

This small direct maintenance request is not a new staged Railspike cycle; no prospective score or study outcome was manufactured. Prior study records remain unchanged. Changes are local and uncommitted; no new beta publication was requested or performed.

*— Codex · 2026-10-25 UTC*

## Publication follow-up

2026-10-25T18:06:52.755988+00:00 — User explicitly requested minting the next beta. Committed the reviewed patch as `f8c8d2588a4a849a12acc7c425d99f533e218f8d` and published [v0.3.0-beta.4](https://github.com/rlspk/railspike/releases/tag/v0.3.0-beta.4) from the non-default product branch. The earlier uncommitted/unpublished statement is historical. Product/development links, Git-workflow fixture, whitespace and diff review passed. Exact tag/commit/body and pre-release status read back successfully; stable Latest and main unchanged. [Verification](./releases/v0.3.0-beta.4-verification.md) · [publication record](./releases/v0.3.0-beta.4-publication.json). No host upgrades or merges.

*— Revised by Codex · 2026-10-25 UTC*
