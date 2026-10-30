> **Feature plan:** [Step 1](./durable_handoffs_step1_solution_assessment.md) · [Step 2](./durable_handoffs_step2_feature_description.md) · [Step 3](./durable_handoffs_step3_development_plan.md) · Step 4 (pending)

Debug mode: enabled.
Effort study: `railspike-effort` / `railspike/durable_handoffs`; [ledger](../../research/effort_estimation/collection.md), standing enrollment.
Extended estimates: enabled.

**Cycle estimate: 0.65**

## Completion Contract

- Deliver `docs/research/durable_handoffs/article.md` (1,500–2,500 words) and `evidence.md`: a standalone article with three artifact-chain cases, a usable handoff checklist, limitations, and an explicitly unrun study proposal. Entry is the article; readers can follow claims into the appendix and distinguish preserved information from demonstrated resumption.
- Allowed writes: those research documents; this cycle's planning/debug/summary records and eventual `docs/plans/durable_handoffs/` folder; its planning-index entry, collection-ledger history, and organization link repairs. Existing sources and the two candidate/title documents remain unchanged and outside this cycle's commits.
- Correct unsupported claims by qualification, removal, or documented correction. Missing evidence stays missing. Essential unresolved claims block completion; independent human review stays pending unless performed. The handoff is a local draft for maintainer review, not publication or a proven handoff benefit.
- Documentation-only: no product, application, tests, CI, website, generated PDF, experiments, recruitment, upload, or submission. Runtime/deployment/migration checks are inapplicable; source checks and related-work verification are required.

## Key Risks

- Selection bias could turn examples into promotion: fix the pool and ordering before extraction; disclose prior exposure, preserve negative findings, and make no prevalence claim.
- **High risk:** unsuitable source excerpts could disclose private material. Check suitability before copying; paraphrase safely or omit with a reason. Do not publish sources.
- Incomplete or drifting records could imply false authorization or outcomes: retain source identities and explicit unknowns, then recheck hashes before final handoff.
- Polished prose could overstate evidence: audit factual claims and distinguish documentary inspection, agent report, design advice, and hypotheses before completion.

## Stage 1 — Establish the three-case evidence appendix

**Estimate: 0.25**

- Goal: produce a reviewable evidence foundation before drafting conclusions.
- Dependencies: Step 3 approval, feature branch, organized planning commit, then implementation summary with entry snapshot.
- Expected changes: create `evidence.md`; freeze the candidate pool as the 25 records in the existing outcome report and record capture cutoff/source identities. Select the lowest-ID documentation, static-site, and application record respectively, one per category, using the report's classifications. Freeze identities before detailed extraction; retain selected cases even if incomplete. This purposeful spread is not representative or preregistered unseen data.
- Verification approach: confirm three distinct IDs and category selection; inspect linked plans, summaries, and relevant history within each selected chain. Record all five dimensions—intent, decisions, authorization, verification, unfinished work—with citations or unknowns; label relationships, exposure, source availability, and excerpt suitability. Record hashes/revisions and narrow quotations or paraphrases sufficient to audit claims.
- Risks or open questions: missing records may prevent reconstruction; show the boundary, never replace the case for a better story. If the three-case review cannot fit this scope, stop and rescope before expanding the corpus.
- Canonical components/API contracts touched: reuse `docs/research/historical_outcome_analysis/report.md` and its linked reviews for the pool; `docs/research/railspike_paper/findings.md` for evidence-labeling precedent. No API changes.
- Estimate details: stage work covers bounded extraction, provenance, and checks; uncertainty is source availability and contradictory history. Owns shared source capture, not whole-cycle planning.

## Stage 2 — Write the complete article

**Estimate: 0.20**

- Goal: deliver an engaging argument grounded in Stage 1's actual findings.
- Dependencies: Stage 1 evidence checks, summary update, and stage commit; suitability resolved before quoting.
- Expected changes: draft `article.md` with a concrete opening, all three cases, practical checklist, limitations, and future comparison of conversation history, concise handoffs, and durable plans. Address information budgets, task/model controls, and independent review without running an evaluation. Update appendix claim mappings and verified primary related-work citations.
- Verification approach: check word target, case coverage, five-dimension traceability, distinction between local and public references, and citations against original sources. Keep Railspike's role concrete without claims of superiority or measured savings.
- Risks or open questions: available evidence may support only modest conclusions; narrow the argument, label illustrative reconstructions, and retain counterevidence rather than inventing a successful handoff.
- Canonical components/API contracts touched: Stage 1 appendix; existing candidate/title documents supply framing only. Article is a new reader-facing synthesis, not a replacement for source reports.
- Estimate details: stage work covers writing, related-work checking, and ordinary corrections; uncertainty is how much contextual explanation the cases require.

## Stage 3 — Audit, correct, and hand off

**Estimate: 0.10**

- Goal: deliver a coherent local draft with an auditable evidence boundary.
- Dependencies: Stage 2 verification, summary update, and commit.
- Expected changes: correct article/appendix discrepancies; record verification, omissions, source drift, and human-review status in the summary; append retrospective scope and pending maintainer acceptance to study records.
- Verification approach: read article-to-appendix as a new reader; audit each material factual claim, case count, citations, five dimensions, checklist, and unrun-study language. Recheck retained source hashes; distinguish changed paths from changed content. Run the existing Markdown link checker with historical baseline and `git diff --check`; inspect allowed-file diff. Recheck the existing planning concepts against unchanged instructions; no inventory edit is expected.
- Risks or open questions: drift or unsupported claims block dependent conclusions; preserve earlier capture and append corrections. Agent self-review does not count as independent human review.
- Canonical components/API contracts touched: article/appendix, cycle summary and ledger; existing link checker reused unchanged. Owns final cross-document checks.
- Estimate details: stage work covers final audit and correction, not measured review time; substantial new evidence needs rescoping rather than silent expansion.

## Execution discipline and study checkpoint

After approval, create a feature branch and organize only this cycle's artifacts, repairing links and its index entry. Commit approved plans plus debug log and permitted organization changes first; exclude substantive ledger history and unrelated untracked candidate documents from that planning commit. Create the summary afterward. Each stage ends with verified changes and summary committed before the next starts; record ledger additions with authorized implementation/closeout work. Minimum: one planning commit and three stage commits. No push or publication.

2026-10-30T20:35:30Z — Step 3, R1/P2 scope v1, start `7620f119577bd52f1204c38f159319ee9a2e3b0b`; Codex, single exposed rater. Whole-cycle **0.65 reaffirmed**; original stage-work estimates S1 0.25 / S2 0.20 / S3 0.10 share this metadata and include each stage's checks/corrections. Cycle total is independently judged, not their sum; values are not hours. All three frozen R1 hashes reverified; missing intake and earlier option scores retained. User approved Step 2; no new enhancement requests or scope change. Step 3 approval pending; no implementation, retrospective, or accepted study outcome.

*— Codex · 2026-10-30 UTC*

Step 3 approval recorded 2026-10-30: user “approved step 3.” The requested editorial pass is an in-scope writing refinement; no new study or publication authority.
