# First-batch outcome report

[Entry](./README.md) · [Rubric](./rubric.md) · [Evidence register](./sources.md) · [All queues](./progress.md) · [Corrections](./corrections.md)

Review reconciled: `2026-10-14T00:05:18.200717+00:00`. Capture began `2026-10-13T23:54:33.714843+00:00`. This is a retrospective, agent-produced analysis of the first 25 entries in a path-ordered queue, not a representative sample, experiment or independent software verification.

## Coverage and interpretation

All 25 assigned records have the common fields and source evidence or explicit unknowns. They use 102 mapped documents (5,665 lines), targeted immutable commit inspections, and two supplemental excerpts. Every record has an inspected stage/correction commit manifest; a manifest establishes file/history facts, not test execution or prior authorization. Targeted reading is not a forensic audit of every conversation, diff or historical runtime result.

| Documentary acceptance category | Records | Meaning |
| --- | ---: | --- |
| Reported met within the stated boundary | 13 | Author reports cover the applicable outcome; limitations remain. No independent pass certification. |
| Known unmet gate | 6 | A required acceptance or release condition is explicitly unmet/unperformed. This is not necessarily a product defect. |
| Unknown full acceptance | 6 | Partial delivery evidence exists, but the complete contract is not established or changed semantics remain unresolved. |

These counts describe evidence in this batch, not a success rate. Criteria vary by task: documentation consistency, UI acceptance, operational recovery and test coverage must not be collapsed into a single software-quality score.

## Record index

| Record | Task | Acceptance category |
| --- | --- | --- |
| [C002](./review-1.md#c002) | Documentation: integrate FDP plan-organization rules | reported met |
| [C005](./review-1.md#c005) | Static website: replacement homepage | known unmet |
| [C006](./review-1.md#c006) | Documentation: installation and onboarding improvements | reported met |
| [C007](./review-1.md#c007) | Documentation: durable instruction debug mode | reported met |
| [C008](./review-1.md#c008) | Documentation: project-default debug marker | reported met |
| [C009](./review-2.md#c009) | Documentation: prompted installation and welcome | reported met |
| [C010](./review-2.md#c010) | Documentation: quiet debug handoffs | reported met |
| [C012](./review-2.md#c012) | Static website: verbatim essay homepage | known unmet |
| [C013](./review-2.md#c013) | Documentation: repository cleanup and reorganization | unknown |
| [C014](./review-2.md#c014) | Distribution/repository maintenance: separate development content | reported met |
| [C015](./review-3.md#c015) | Static website: branded design and voice selector | known unmet |
| [C016](./review-3.md#c016) | Documentation: public examples hub and three cases | unknown |
| [C017](./review-3.md#c017) | Git distribution workflow: retire mutating bootstrap | unknown |
| [C018](./review-3.md#c018) | Bash installer: submodule install and sync | unknown |
| [C019](./review-3.md#c019) | Documentation: original FDP instruction diagnostics | reported met |
| [C020](./review-4.md#c020) | Documentation/visual: compact Mermaid diagrams | unknown |
| [C024](./review-4.md#c024) | Application: activity source filename/commit metadata | unknown |
| [C025](./review-4.md#c025) | Internal refactor: activity subsystem extraction | reported met |
| [C028](./review-4.md#c028) | Application/operations: merge agent-reply queue | known unmet |
| [C029](./review-4.md#c029) | Application: direct selected-response preflight | reported met |
| [C030](./review-5.md#c030) | Browser UI: response dropdown viewport fit | known unmet |
| [C031](./review-5.md#c031) | Application: separate plain-text response harness | reported met |
| [C032](./review-5.md#c032) | Browser/application: selectable response modes | known unmet |
| [C035](./review-5.md#c035) | Application/CLI: immediate approval-seed refresh | reported met |
| [C036](./review-5.md#c036) | Application: shared activity commit-file manifest | reported met |

## Findings and counterevidence

- **Completion and acceptance diverge.** [C028](./review-4.md#c028), [C030](./review-5.md#c030) and [C032](./review-5.md#c032) expose explicit required gates not closed by retained summaries, despite census completion labels. The three site records already carried pending release review. These findings justify recording gates separately, not claiming all implemented features failed.
- **Verification scope matters.** [C017](./review-3.md#c017) has a real fixture whose dirty-state check does not attempt an update/refusal. [C030](./review-5.md#c030) has placement simulation and zero-exit PHP invocations rather than required browser/theme checks. Conversely, [C035](./review-5.md#c035) reports isolated fault injection and repaired retries, and [C014](./review-2.md#c014) reports migration/rollback exercises. Different evidence strengths and environments remain explicit; none was rerun here.
- **Corrections are informative, but not effort measurements.** [C012](./review-2.md#c012) records a narrow-screen overflow fix; [C013](./review-2.md#c013) records a tracked-file staging repair; [C025](./review-4.md#c025) records dependency-analysis and lazy-connection corrections; [C031](./review-5.md#c031) records a failed then successful text probe. Preserve these events and requested scope changes separately. Incomplete histories cannot establish total rework.
- **Related work must stay related.** Website redesigns and successive installation/response changes share code, requirements and authorship. [C024](./review-4.md#c024) and [C036](./review-5.md#c036) change related commit semantics; [C025](./review-4.md#c025) is a subplan of an incomplete umbrella. IDs are administrative units, not independent trials.
- **Instruction opinions remain hypotheses.** Seven records have mapped debug logs: C005, C008, C010, C012, C013, C014 and C015. They attribute value to scope/risk/commit checks and report repeated-instruction or review friction. Six overlap the original R01–R06 study; repetition is not new independent corroboration. The other **18/25** records have no mapped debug log, not evidence of no benefits or no friction.

## Missingness and limits

- Independent reproduction performed in this research: **0/25**. Human review of this coding: **0/25**, all pending. Complete authorization transcripts were not inspected for any record; quoted approvals remain source-author reports.
- Measured active human effort: **0/25**. Exact historical execution model/instruction revision is unverified throughout. C025 has commit co-author attribution; C031 names an application provider, not its coding agent. Neither pins runtime identity.
- Application timing in C035 is a reported synthetic product benchmark. It cannot estimate developer time saved or Railspike efficacy. Likewise, counts of tests, source lines or commits are not effort or causal measures.
- Source capture uses fingerprints and relevant exact excerpts, not complete archival copies of all mapped texts. Full recovery of mutable/uncommitted sources is not guaranteed. Source secrecy/disclosure checks applied to retained excerpts; this package stays local and is not approved for publication.
- Source families were read through goal/contract/verification/correction passages, with targeted deeper checks. Undiscovered contradictions may remain; the unknown/qualification fields and append-only correction path are part of the deliverable.

## Remaining work

This slice completes **25 + 191 pending = 216 eligible candidates**. All 191 remaining eligible IDs and all **95 separate adjudication IDs** are preserved in the progress document. Research, duplicates and context remain excluded as in the 349-candidate census. No candidate is replaced because its evidence is weak.

The next bounded cycle should take the next administrative queue segment (census analysis batch 2), retain this rubric or explicitly version/recheck changes, and reconcile cumulative coverage. These later cycles remain unapproved work. The 95-case adjudication queue and cross-corpus synthesis are separate scope. An identified human should review judgments and the highlighted discrepancies before findings are treated as independently reviewed; no external review has been requested or claimed.

## Integrity verification

Record memberships, all required fields, selected source-line excerpts, commit identities, queues and local paths/heading anchors were checked. All 102 mapped source fingerprints still match capture and census; original study/census bytes are unchanged. Allowed file scope and per-stage summary/commit cadence were checked. No runtime test, deployment, publication or source modification was performed.
