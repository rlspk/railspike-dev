> **Feature plan:** [Step 1](./merge_acceptance_step1_solution_assessment.md) · [Step 2](./merge_acceptance_step2_feature_description.md) · [Step 3](./merge_acceptance_step3_development_plan.md) · [Step 4](./merge_acceptance_step4_implementation_summary.md)

Debug mode: enabled (host marker present).
Effort study: `railspike-effort` / `railspike/merge_acceptance`; [standing enrollment and ledger](../research/effort_estimation/collection.md). No parent cycle.
Extended estimates: enabled.

**Cycle estimate: 0.40**

## Original Query

Are there a lot of open effort assessments? I did not realize I was supposed to be doing that for the current process. If so, we should probably change the process.

Follow-up, after a proposal in the same conversation: "Let's do it on railspike-dev."

## Understood Intent

The effort study asks the maintainer for a comfortable-fit judgment and an acceptance at every cycle closeout. Nobody asks at that moment, so the judgments never arrive. In the v3 ledger, 85 cycles are recorded and one is accepted. About 60 more say acceptance is pending, and most of the rest record no outcome. This project's own index says "maintainer fit/acceptance pending" on nearly every row. The six accepted outcomes that trigger a study review can therefore never be reached.

The maintainer wants the study rules changed so that collection works without a separate judgment step. The proposal discussed was: a merge counts as acceptance, and the implementing agent records the fit judgment. The change belongs in Railspike itself, because the rule lives in the product's effort-estimation contract, not in one host.

Problem: The study's outcome rule depends on a maintainer step that never happens, so no cycle reaches an accepted outcome.

Concepts touched: none in the [concept inventory](../concepts/inventory.md); this cycle adds none. Terms used: *accepted outcome*, *comfortable-fit judgment*, *study review checkpoint*.

## Option A — The merge accepts; the agent judges fit (recommended)

**Estimate: 0.40**

Change the closeout rule in `RAILSPIKE.md` and `docs/effort-estimation.md`. The maintainer's normal merge or release decision counts as acceptance. The implementing agent writes the comfortable-fit judgment at closeout and labels it as its own. The maintainer adds a judgment only to disagree. Record the new rule as protocol P3 in this project's `collection.md`, keeping P2 records as they are.

- Pro: no extra step for the maintainer; every merged cycle becomes an outcome.
- Pro: keeps fit as a separate field from size, so the study still asks "did this fit one cycle?"
- Con: the fit judgment comes from the agent that did the work and also gave the estimate. That rater is not independent.
- Con: in projects that merge without review, a merge says little about acceptance.
- Driver/uncertainty: two product files and one protocol file. Medium uncertainty in how hosts that publish without a merge, such as release-only cycles, signal acceptance.

## Option B — Drop acceptance; count completed cycles

**Estimate: 0.30**

Remove the maintainer judgment and acceptance from the study. An outcome is any technically complete cycle with a retrospective scope assessment. The review checkpoint counts completed cycles.

- Pro: simplest rule; no dependence on merge habits.
- Con: loses the only signal that the size felt right to a human. The study then compares agent estimates only with agent retrospectives.
- Con: abandoned or rejected work looks the same as accepted work.

## Option C — Keep the maintainer judgment, collected in batches

**Estimate: 0.45**

Keep the current fields. At closeout, the agent adds the cycle to a pending list. When the list reaches six, the next agent asks the maintainer for all six judgments in one short question.

- Pro: keeps an independent human judgment.
- Con: still a step the maintainer must remember to answer; the backlog shows it is easy to skip.
- Con: judgments made weeks later are less reliable than judgments made at the time.

## Recommendation

Choose Option A. It fits how the maintainer already works: the merge is the real decision. It keeps the fit question, and it is honest about who answered it. Option C's batch question could be added later if agent-only judgments turn out to be too generous.

This is a vertical slice in two places: the product rule and this project's protocol. Updating the existing pending records in both projects is separate work. It needs a merge-history check per cycle, and the v3 ledger alone has 85 cycles. Plan it as a follow-up cycle after this one.

*— Claude · 2026-11-06 UTC*

## Study checkpoint

2026-11-06T16:39:22Z, `railspike-effort` / `railspike/merge_acceptance`, intake and Step 1 handoff. Scope v1: Option A as recommended. Starting revision `4c64dd5` (railspike-dev) and product `v0.6.1-beta.1`. Reference R1, protocol P2; frozen R1 hashes not re-verified for this checkpoint. Single exposed Claude rater, exposed to the v3 ledger, this project's `collection.md` and the product's effort-estimation contract before rating. Pristine intake missing. Intake and Step 1 projected total **0.40**. Option estimates 0.40, 0.30 and 0.45 are alternatives and do not add up. No implementation, measured labor or accepted outcome.

## Enhancement Requests

None yet.
