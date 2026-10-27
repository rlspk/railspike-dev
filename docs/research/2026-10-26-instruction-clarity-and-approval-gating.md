# Railspike instruction clarity and approval gating

Date: 2026-10-26

Status: Discussion conclusions and proposed direction. Saving this note does not approve implementation or a workflow-contract change.

Railspike should explore programmatic validation and action gating, with approval integrity as the preferred first scope. STE-inspired writing can improve clarity, but a full ASD-STE100 rewrite is not the recommended starting point. Clear wording alone cannot prevent an agent from skipping instructions or inferring permission that the user did not give.

## Reported Kiro failures

The maintainer used both Kiro's web interface with its own runtime environment and Kiro CLI. The three most consequential reported failures were:

1. The agent did not consult `AGENTS.md`.
2. The agent treated a reference to a Step 1 plan as approval of that plan.
3. The agent answered a question about implementation details and then proceeded with implementation without confirming that implementation was authorized.

These are user-reported incidents; their distribution between Web and CLI and the precise session configurations have not been established. They provide concrete scenarios for future regression tests.

## Instruction clarity

ASD-STE100 is a controlled language for technical documentation, with writing rules and a controlled vocabulary. Full compliance requires more than short sentences. Its relevance to clear instructions does not establish improved coding-agent compliance. See the [official STE overview](https://www.asd-ste100.org/about_STE.html).

A focused STE-inspired revision would use:

- One action per instruction.
- Consistent names for steps, stages, approvals, and artifacts.
- Explicit prerequisites and conditions.
- Clear distinctions between requirements, recommendations, and examples.
- Exceptions beside the rules they modify.

Keep familiar software terminology. Describe the result as STE-inspired unless compliance is actually validated.

The inspected `RAILSPIKE.md` contained approximately 4,700 words, with another 4,400 in the workflow files. Railspike already loads detailed instructions by phase and clearly states important stage-boundary rules. The hypothesis to test is that essential obligations compete with supporting detail, rather than all failures arising from ambiguous wording.

## Proposed controls

| Failure | Proposed control | Boundary |
| --- | --- | --- |
| Instructions not consulted | Load applicable `AGENTS.md` instructions before enabling workflow actions; block those actions when required instructions cannot be loaded | Delivery can be enforced; model understanding cannot be proved mechanically |
| Plan reference treated as approval | Require an explicit user approval event identifying the cycle, step, and artifact revision | Mentioning, opening, or summarizing a plan does not approve it |
| Question treated as implementation permission | Keep authorization unchanged when answering questions | A question does not grant new authority or automatically revoke existing authority |

The central invariant is that conversation must not silently increase the agent's authority. During already-approved implementation, an ordinary question need not revoke existing approval. Before implementation is approved, answering a question cannot supply that approval.

## Validation and enforcement

Artifact validation can check required sections, approved scope boundaries, artifact revisions, verification records, and stage commits. It improves the reliability of workflow records and detects some violations.

Action gating checks authorization before an operation executes. This is necessary to prevent unauthorized implementation; checks performed afterward can only detect it.

A conceptual state sequence is:

```text
Draft -> Awaiting approval -> Approved -> Executing -> Verified
```

Each transition would have explicit prerequisites. Approval would bind to a cycle, step, and artifact revision. Material plan changes would require renewed approval, while routine authorized progress would not. This sequence is a design sketch, not a complete transition specification.

An agent-editable `approved: true` field is bookkeeping, not strong enforcement. The agent must not be able to grant itself permission. Stronger enforcement requires a trusted user interaction and controls outside the agent's writable authority. Blocking an editor tool is insufficient if a shell command can perform the same write; alternative write paths and modification of the gate itself must be considered.

## Proposed architecture

1. **Essential instructions:** a short, always-loaded contract containing critical gates and pointers to applicable detailed instructions.
2. **Current state:** a compact record of approved scope, current step and stage, approval evidence, and the next permitted action, recoverable after interruption or context loss.
3. **Enforcement:** checks before consequential operations, supplemented by artifact and Git validation.

Keep the workflow contract portable and assess enforcement separately for each runtime. Equivalent guarantees for Kiro Web and CLI depend on what each environment permits Railspike to intercept and protect.

Kiro's documentation describes always-included steering and says custom agents require steering resources to be configured explicitly. Establish which instructions were actually loaded in the affected sessions. See [Kiro steering](https://kiro.dev/docs/steering/).

Kiro also documents shell hooks whose failures can block Pre Tool Use invocations. These are a candidate enforcement mechanism; prompt hooks supply instructions rather than deterministic authorization checks. Applicability and coverage require verification in the actual Web and CLI versions used. See [Kiro hook actions](https://kiro.dev/docs/hooks/actions/).

## Proposed first experiment

Prioritize approval integrity: explicit approval events, revision binding, and prevention of implementation without the required approval. Compare:

- Current instructions.
- Simplified instructions.
- Simplified instructions with programmatic checks.

Use the three reported incidents as regression scenarios, including paraphrases, resumed sessions, changed plan revisions, and questions during already-authorized implementation. Measure skipped approvals, missing stage commits, scope overruns, and unnecessary interruptions. Test both prohibited actions and legitimate progress to expose gates that block too much.

Resolve how trusted approval is captured, which actions each runtime can intercept, how approval survives resumption, and which artifact changes invalidate approval before choosing an implementation. Use the results to decide whether a broader language rewrite is worthwhile.

## Development status

This is an ordinary discussion record, not an initiated staged Railspike cycle. No prospective effort score has been reconstructed. A subsequent Railspike cycle remains subject to the standing `railspike-effort` enrollment and collection protocol, retaining R1 and append-only score and scope histories.

The maintainer requested that this file remain uncommitted.
