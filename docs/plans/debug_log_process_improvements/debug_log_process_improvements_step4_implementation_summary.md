> **Feature plan:** [Step 1](./debug_log_process_improvements_step1_solution_assessment.md) · [Step 2](./debug_log_process_improvements_step2_feature_description.md) · [Step 3](./debug_log_process_improvements_step3_development_plan.md) · [Step 4](./debug_log_process_improvements_step4_implementation_summary.md)

Debug mode: enabled

## Branches and commits
- `railspike-dev`: `feature/debug-log-process-improvements` from `main` (which was one local commit ahead of `origin/main`). Planning commit `bbe87cf`.
- `railspike` (product): `feature/known-user-recovery` from `main`, verified equal to `origin/main` at `579c0c1` after fetch; the previously checked-out `feature/mid-process-enhancements` was already merged.
- Allowed product files (Step 3 contract): `RAILSPIKE.md`, `docs/workflow/step2_feature_description.md`, `step3_development_plan_do.md`, `step3_development_plan_after.md`, `step4_implementation_after.md`, `docs/failure-modes.md`.
- Product commits per stage: Stage 2 `0dcf862`.

## Stage 1 - Baseline and replay cases
- Changes:
  - Baseline line counts of the six allowed product files at `579c0c1`:

    | File | Lines |
    |---|---:|
    | `RAILSPIKE.md` | 165 |
    | `docs/workflow/step2_feature_description.md` | 41 |
    | `docs/workflow/step3_development_plan_do.md` | 60 |
    | `docs/workflow/step3_development_plan_after.md` | 17 |
    | `docs/workflow/step4_implementation_after.md` | 21 |
    | `docs/failure-modes.md` | 61 |
    | **Total** | **365** |

  - Replay cases (from `v3/docs/plans/local_server_dependency_recovery_railspike_failure_report.md`, "F01", and the V04 revision entry of 2026-10-13 05:21:44 UTC):

    | Case | Known environment | Supported-path result | User outcome missed |
    |---|---|---|---|
    | A: missing PHP | Ubuntu 22.04, PHP CLI absent | Installer tested on Ubuntu 24.04; Step 4 reported complete | `./v3 start` said "Install PHP CLI ... using your system's package manager"; no concrete next action for this OS |
    | B: missing extensions | Ubuntu 22.04, PHP 8.1.2 | Same | Messages stayed "Install/enable ... for the selected PHP CLI"; no package names or enable path |
    | C: completion handoff | Same user | 39 disposable-environment cases and 31 runtime checks passed | Handoff led with "Step 4 is complete" without stating the user's machine still lacked recovery |
    | D: pending live checks | Static website cycles (ledger rows R01, R04, R06) | Local verification passed | Live deployment checks remained pending in logs; completion text did not always separate them |

  - Decisive source sentences (quoted from F01, "Where the process failed"):
    - A: "A known environment mismatch was handled only as a testing constraint."
    - B: "'Actionable manual guidance' appeared in Step 2. Step 3 retained 'manual recovery' without specifying what a usable message must contain."
    - C: "Coverage concentrated on the new install entry point."
- Verification:
  - Counts match `wc -l` on the product checkout at `579c0c1`.
  - Case sentences were copied from F01 and checked against the source file; case D is attributed to the ledger's recorded dispositions, not a separate quotation, because its source texts are frozen archives rather than verbatim transcripts.
  - No product files were edited in this stage; product working tree clean.
- Notes:
  - The `railspike-dev` `main` branch was one commit ahead of `origin/main` (`3c58f0c`, the user's explanations commit); it is included in this branch's base and has not been pushed.

## Stage 2 - Step 2 guidance
- Changes:
  - `docs/workflow/step2_feature_description.md`: new "Known user or environment" structure item (entry point, mismatch or failure, unaided next action, verify/retry, evidence); evidence from a different supported platform is stated not to satisfy it; omitted when no user or environment is named.
  - `RAILSPIKE.md`: one matching Key Rules line.
  - Net: +2 lines (`RAILSPIKE.md` 165 to 166, Step 2 file 41 to 42); no existing text removed or moved.
- Verification:
  - Replay of case A and B against the new text: V04's Step 2 said only "Unsupported platforms receive actionable manual guidance". The item now requires naming the Ubuntu 22.04 user's entry (`./v3 start`), the missing-PHP failure, the next action with an observable package-level step, how to retry, and evidence, so the quoted sentence alone no longer satisfies Step 2.
  - Applicability check: for "fix a typo in the README" no user or environment is named, so the item is omitted and adds no section.
  - `git diff --check` clean; changed files are exactly the two allowed files.
- Notes:
  - The word "mismatch" is used for the Step 2 item; the Stage 3 acceptance wording reuses it.
  - Replay used the case text recorded in Stage 1, not a fresh run of an agent.
