# Clone evidence and suggested Railspike improvements

The strongest next improvement is dependable recovery of the effort references, followed by per-option Step 1 estimates. A live assessment already demonstrates the value of comparing alternatives on the R1 scale. The broader records also support clearer plan status, approval provenance, and practical sizing guidance.

This is the requested research review and suggestion list. Product changes remain a separate cycle. The evidence retains R1, original estimates, incomplete work and conflicting checkout records.

## Coverage and evidence

The [captured evidence](./2026-10-23-clone-evidence.json) records checkout heads, source hashes, file-version identities, eight ledger snapshots, 25 selected source snapshots and the current product instructions used for comparison. Source IDs S01–S25 below refer to its `evidence` entries. Paths identify the observed source; retained text supports the findings if a live file moves.

Nine v3 checkouts were inventoried: main, six `agent/v3-*` clones, `v3-test` and `v3-test-kris`. Eight contain planning material: 10,641 Markdown file copies collapse to 1,398 distinct byte versions. Those are inventory counts, not independent observations or a claim that every file received close reading. Review concentrated on the effort ledgers, diagnostic suggestions, option comparisons, scope revisions and implementation summaries. The two prayerwheel checkouts were screened as additional hosts; their eight plan files apiece provide no additional effort ledger. The `agent/forum-private` and Railspike separation-recovery directories had no `docs/plans` material at the checked location. Unreachable Git objects, remote-only clones and unrelated repositories were outside this review.

The v3 ledger union contains **18 distinct P2 cycle headings**, in addition to E01–E07 history. These are a mixture of planning, partial and delivered work, not 18 accepted outcomes. Eight ledgers now have different complete-file contents. Section-level reconciliation finds differences for `v3/concurrent_checkouts` and `v3/markdown_dependency_removal`; the other shared cycle sections match at capture. Clone-specific records include rename collision, unsigned attribution, renderer extension/list structure, key revocation, reply continuation and feedback management. No latest-checkout-wins merge was performed.

Active sessions changed nine previously inventoried paths during collection, including renames of unsigned-attribution plans. The manifest retains initial hashes and later observed hashes or absence. The captured ledgers and source texts are later observations, not an atomic snapshot of all clones. Scope versions and checkpoint dates must be used when integrating them.

## Suggested improvements in priority order

### 1 Make frozen effort references reliably recoverable

Several cycles cannot produce scores because the report, diff review or exact historical feedback is missing or changed. Other agents recover the same material successfully. The rename assessment even reports ledger links with incorrect directory depth (S21); concurrent checkout work remains unscored through closeout (S09–S11).

Add a portable reference manifest and a clear recovery procedure: resolve host-relative paths, verify hashes, recover the recorded historical revision into a separate retained location, and preserve the original reference identity. Distinguish unavailable files, broken paths and changed bytes. Keep unavailable estimates unavailable until recovery succeeds; recovery now must not backfill earlier prospective checkpoints.

The report and diff hashes match R1 here. Reading the feedback from `4f6cfe2b:docs/plans/zenmemes_meta_feedback_2026-10-18_summary.md` also reproduces the frozen feedback hash exactly. This is a demonstrated recovery route, not a reason to replace R1 or overwrite current feedback. New installations can use bundled references, but that does not waive an existing host's frozen-source contract.

### 2 Include comparable effort estimates for each Step 1 option

The rename-collision assessment already compares A at approximately **0.25**, B at **0.40**, and C at **1.10**, with the higher score prompting a split discussion (S21). Its explanations distinguish two write-path checks from a change to canonical approval semantics and recovery. That is useful decision support, although it is one exposed rater's proposal rather than a validated forecast.

Give each viable option one compact line: total effort estimate or range, main complexity driver, and material uncertainty. Use the same baseline and explicit outcome assumptions; show when options deliver different outcomes. Keep technical complexity descriptive and R1 numeric values labeled as effort. An unavailable estimate should carry its reason. Non-enrolled cycles should not acquire mandatory study bookkeeping merely to compare options.

Keep the recommended scope's formal handoff snapshot separate. Re-estimate combinations and splits rather than adding scores. Preserve alternative estimates under option and scope identities when the recommendation changes. The exact uncertainty format remains a design choice; these records do not establish calibrated numerical ranges.

### 3 Make the current plan and approval state obvious

The effort-trial diagnostic records a reader encountering an older Step 2 after Step 1 changed; its draft labels did not make the reconciliation state clear enough (S18). Concurrent checkout assessment versions change direction substantially (S10), while the unsigned-attribution ledger records restarts and superseded plans. Active renames during this review reinforce the recovery problem.

Add a compact current-state block: active scope version, current step, approved version, superseded artifacts, next authorized action and pending reconciliation. Put it near the top and link retained history below. When an upstream plan changes, mark downstream documents as awaiting reconciliation immediately. Retain historical approval context without presenting it as approval of the new scope.

### 4 Record approval provenance and reconsider exact wording

The toolbar log records an extra confirmation after “Approve Step 3”; other logs discuss “Continue to Step 4” or explicit authorization taking precedence over literal-token guidance (S04, S06, S11, S14). A resumed approval-safety cycle could recover implementation context but could not independently attest to the original wording (S15).

Record the user's actual approval wording, approved artifact/scope version, step and any explicit process override. Separately consider allowing unambiguous approval of the identified step and scope in natural language. Direction selection, general enthusiasm and revision requests must remain distinct from implementation approval. This is a workflow-contract decision requiring its own review; under the release policy, an approval-requirement change needs evaluation as a major change.

### 5 Size stages by coherent work and verification

Backup fixtures, Docs UI work and moved template markup expose limitations of the approximate 50-line rule (S01, S03, S16). Current Step 3 guidance still pairs approximately one hour or 50 lines with a split requirement, while overview warning signs mention stages over two hours.

Choose one consistent sizing rule. Treat changed-line counts as a warning signal, explaining how moved code, generated material and test fixtures affect the judgment. Keep stages scoped to a reviewable outcome with explicit verification and dependencies. Preserve the cycle-level split discussion around 1.0 R1 without converting R1 into hours or deriving it from stage counts.

### 6 Replace physical page limits with a usable concision target

Independent feature logs repeatedly point out that Markdown has no fixed printed page size, and required original queries, risk inventories and stage fields compete with a one-page limit (S07, S08 and the initial diagnostic scan). Current Steps 1–3 still use page limits.

Define an approximate word budget or a short decision summary with linked evidence. Exclude preserved original requests and append-only study history from the summary budget. Keep required recovery and verification detail available rather than deleting it to meet pagination. This also creates room for per-option estimates without making the visible comparison unwieldy.

### 7 Compare options against established constraints

The fastmod meta-score diagnostic says the initial comparison assumed downstream aggregation, while the intended architecture used a shared multi-score call and reusable rubric snippets (S05). Concurrent checkout revisions likewise move from folder identity to persistent IDE sessions and then synchronization as the user's goal becomes clearer (S10).

Before selecting comparison axes, inspect the relevant existing path and separate known constraints from assumptions. Compare unresolved choices and identify what would change the recommendation. Keep this lightweight: do not turn Step 1 into detailed implementation planning or require questions whose answers are already in the available evidence.

### 8 Define closeout for conditional stops and partial delivery

A scripture evaluation stopped before dependent stages became eligible (S06). Phone-site and dependency-removal records distinguish local delivery from external or historical-removal acceptance (S19, S13, S24). Current Step 4 already requires honest verification statuses, but also asks to confirm all planned stages completed and checks a minimum commit count against stage count.

Explicitly support a stopped or partial closeout: completed, blocked, deliberately unrun and superseded stages; the failed gate; retained work; and the next decision. Apply commit expectations to executed stages and avoid empty commits for ineligible stages. Keep technical completion, release readiness, maintainer outcome acceptance and study acceptance distinct.

### 9 Make shared documentation edits preserve unrelated work

The composer diagnostic describes updating one todo line while preserving pre-existing user edits through selective staging (S16). Parallel ledger sections now diverge, and the feedback-management cycle uses permanent aliases, redirects and separate source/delivery evidence successfully (S25).

Add a concise example for editing and committing a cycle's own changes in a shared ledger, index or todo file without sweeping in another session's work. For cross-clone review, compare cycle/checkpoint/scope and content identity, surface conflicts and retain both observations. The product already requires worktree deduplication and preservation; a worked example or optional read-only audit tool would make that contract easier to execute.

## Older findings already addressed

- **Full instruction reprints:** many historical logs report this overhead. Current product instructions explicitly prohibit automatic reprints and require concise action/constraint summaries. Verify installed revision and adoption before proposing the same change again.
- **Debug marker semantics:** S16's old uncertainty is resolved by the current presence-only marker contract and durable state recovery rules.
- **Focused tests versus full verification:** current Step 4 already requires baseline-failure identification and distinct passed/failed/blocked/pending/inapplicable results. S02 remains evidence for keeping those rules, rather than silently treating baseline failures as a globally green suite.
- **Follow-ups and scope changes:** current instructions already distinguish in-scope refinements, changed scope and separate work. Improve status visibility and examples rather than remove those boundaries.

## Suggested implementation sequence

First, reconcile reference recovery and ledger navigation as a focused reliability cycle. Then implement per-option Step 1 estimates together with only the concise presentation guidance needed to accommodate them. Treat approval semantics, state recovery and stage/closeout policy as separate proposals with their own compatibility review. Preserve R1 until stronger evidence warrants an explicitly versioned replacement.

The new records add useful examples, especially comparative estimates and incomplete outcomes. They do not establish independent rater agreement, measured labor, calibrated uncertainty intervals or a new maintainer-accepted outcome series. No application tests were rerun; this review checks recorded evidence and instruction contracts. Product and clone worktrees were read only. Research records remain uncommitted, with no upload, merge or release.

## Collection administration

Record `railspike/clone-review-2026-10-23` belongs to `railspike-effort`, R1/P2. This ordinary requested review did not initiate a staged Railspike cycle merely for collection. No prospective cycle estimate was recorded and none is reconstructed after inspection. Prior review/calibration exposure is disclosed in the evidence record. This administrative review is excluded from independent accepted-outcome counts; maintainer acceptance of the suggestions remains pending.
