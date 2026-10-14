> **Feature plan:** [Step 1](./remove_instruction_reprints_step1_solution_assessment.md) · [Step 2](./remove_instruction_reprints_step2_feature_description.md) · [Step 3](./remove_instruction_reprints_step3_development_plan.md) · [Step 4](./remove_instruction_reprints_step4_implementation_summary.md)

Debug mode: disabled

# Task-relevant instruction summaries

## Stage 1 - Summary contract and aligned guidance
- Changes: Added the canonical Instruction Summaries contract in product `RAILSPIKE.md`; aligned chain/key rules, Step 3 setup, README troubleshooting/debug advice, and failure-mode recovery. All four product files are within approved scope (17 insertions, 7 deletions). Organized approved plans and added the feature index entry before implementation.
- Verification: Product Markdown check passed for all 14 files (`python3 scripts/check-markdown-links.py /home/wsl/railspike`). Development check with the historical baseline has no missing targets for this feature; nine existing unrelated failures remain: six future-step links in debug-log-process-improvements/first-release drafts, two references to `installation_log.txt`, and one to `railspike.txt`. No baseline changes made for this feature.
- Verification: `git diff --check` passed in both repositories; reviewed product diff and file scope, and scanned active guidance for reprint/echo/reproduction references. Only the explicit prohibition of automatic reprints remains. Existing phase order, approval gates, planning/stage commit discipline, and debug state/logging obligations retain their substance.
- Verification: Manual documentation scenario review below passes the approved contract. Runtime, UI/API, database, deployment, and external release checks are not applicable to these documentation-only changes; no automated agent-behavior claim is made.
- Notes: Planning commit `7a6931b`; product stage commit `f6d29335125d28c27e638064dc01642b836c18c8`. The development stage commit containing this summary is paired with that product commit; its ID is reported at handoff. Both repositories use `feature/remove-instruction-reprints`. Existing unrelated development changes are excluded.

## Scenario evidence
These outcomes are observed requirements in the final wording, not execution tests of an agent. Canonical references are to product `RAILSPIKE.md`, Instruction Summaries, paragraphs 1–4.

| Scenario | Expected contract | Observed wording / result |
| --- | --- | --- |
| First entry | Read, then summarize action, constraints, and gate before acting; no routine reprint | Paragraphs 1 and 4 require this; pass. |
| Changed transition or resumption | Update summary when any relevant action, constraint, or gate changes | Paragraph 2 names all three triggers; pass. |
| Unchanged transition or recoverable resumption | Preserve required reading/restoration without redundant summary | Paragraph 2 explicitly excludes transition alone and requires rereading/restoration on resumption; pass. |
| Prior summary context unavailable | Restore state, then establish fresh summary | Paragraph 2 states this fallback; pass. |
| Instructions missing or unreadable | Report blocker and resolve before proceeding; no implied reading | Paragraph 3 states both conditions; pass. |
| Approval gate or omitted exception | Source remains authoritative; summary grants no additional authorization | Paragraph 3 preserves exceptions, approvals, order, and commit rules; pass. |
| Explicit request for instructions | Requested contents remain available | Paragraph 4 allows explicit requests; failure-mode guidance agrees; pass. |
| Decision/blocker explanation | Relevant quotations and useful progress/handoff remain available | Paragraph 4 explicitly preserves them; pass. |
| Debug enabled / disabled | Same summary contract, existing diagnostics preserved | Paragraph 4 separates summaries from diagnostics; aligned debug references preserve logging and recovery; pass. |
| Tool read output | Policy does not suppress ordinary tool rendering | Paragraph 4 limits the contract to assistant-authored repetition; pass. |
