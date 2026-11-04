# Railspike academic paper candidates

Date: 2026-10-30

Status: Candidate discussion, not an approved study or implementation plan. The literature check is preliminary.

Railspike has several credible paper candidates, with approval integrity and the gap between “completed” and “actually worked” offering the strongest starting points. For a strong academic contribution, we need a precise question, a contribution beyond Railspike itself, and evidence that could support an unfavorable result.

Existing groundwork includes the [exploratory study](railspike_paper/findings.md), the [25-record outcome analysis](historical_outcome_analysis/report.md), and the [continuing effort collection](effort_estimation/collection.md). These are overlapping, maintainer-local records; they provide hypotheses and cases, not independent proof that Railspike improves development.

## 1. Approval Is a State, Not a Sentence: Preserving Human Authority in Coding Agents

**Question:** Can an agent preserve the exact scope of its authorization across questions, revised plans, interruptions, and context loss?

Railspike has concrete motivating cases: references to plans interpreted as approvals, implementation questions treated as permission, and approval state lost after resumption.

The study would compare current instructions, simplified instructions, durable authorization records, and externally enforced gates. Crucially, we would measure both unauthorized actions and unnecessary blocking of authorized work.

The contribution would be an authorization model, a reusable scenario benchmark, and an evaluated implementation. Recent work already documents agents acting through human accounts, so our distinction should be preserving and enforcing authorization through changing conversational state. [Related approval-provenance study](https://arxiv.org/abs/2610.28683).

**Assessment:** Strongest technical candidate; substantial new implementation and evaluation required.

## 2. Done According to Whom? The Gap Between Agent Completion and User Acceptance

**Question:** How often does evidence supporting an agent’s completion report fail to establish the user’s requested outcome—and what verification practices catch that gap?

Our records already distinguish implementation completion, passing checks, environment limitations, deployment, and user acceptance. The first outcome batch contains explicit examples of required gates left unresolved. Those are documentary findings, not a measured software failure rate.

We could independently review selected historical cases, then run a prospective comparison between ordinary verification and acceptance cases written around the actual user entry point, action, and recovery path.

The contribution would be a reproducible classification of completion claims, an adjudicated case collection, and evidence about which checks detect meaningful omissions. This connects to existing research documenting developers’ reliance on test results during oversight. [Related oversight study](https://arxiv.org/abs/2606.05391).

**Assessment:** Best use of existing evidence and the most practical first paper. A descriptive case study is nearer than a causal effectiveness paper.

## 3. The Cost of Staying in Control: Measuring Human Oversight in Agentic Development

**Question:** Do explicit plans and checkpoints reduce total human work, or move it from debugging into reviewing?

Compare native agent planning, Railspike staged mode, and bounded one-shot mode on comparable tasks. Measure active review time, clarification, corrections, missed requirements, and accepted outcomes—not just elapsed agent time or token use.

The interesting result could be conditional: checkpoints might help with ambiguous features while adding overhead to small fixes.

The contribution would be an experimentally supported account of when structured oversight pays for itself. Measurement needs care: METR’s follow-up describes selection bias and difficulties measuring time when developers run agents concurrently. [METR’s measurement discussion](https://metr.org/blog/2026-02-24-uplift-update/).

**Assessment:** Broad appeal, but the largest participant-recruitment and measurement burden.

## 4. Can Another Developer Pick Up the Work? Evaluating Durable Plans as Handoff Artifacts

**Question:** Do repository-based plans and decision histories help a different developer or agent resume work correctly?

We could interrupt tasks at fixed points and hand them to fresh participants with different artifact packages: conversation history, a concise handoff, or Railspike’s plans and stage records. Match information budgets where possible so we can distinguish useful structure from simply supplying more information.

Measure reconstruction of requirements and authorization, time to a correct next action, duplicated investigation, and scope mistakes.

The contribution would be a handoff benchmark and evidence about which durable artifacts actually help.

**Assessment:** A focused, tractable experiment closely aligned with Railspike’s core design.

## 5. How Much Process Is Enough? An Ablation Study of Coding-Agent Workflow Instructions

**Question:** Which workflow requirements improve outcomes, and which mainly increase reading and generation?

Railspike’s records suggest specific components to test: staged approvals, persistent plans, stage verification, instruction repetition, and compact versus detailed guidance. Change components systematically while holding tasks, agent configuration, and outcome assessment constant.

The contribution would be evidence about individual mechanisms rather than an undifferentiated “Railspike versus no Railspike” result. Nearby research already compares structured agent workflows, so simply proposing another staged process would be insufficient. [Related workflow comparison](https://arxiv.org/abs/2610.09995).

**Assessment:** Useful for both publication and product decisions; requires tight scope to avoid an unmanageable experiment.

## 6. Can Coding Agents Recognize Work That Should Be Split?

**Question:** Can reference-based scope estimates predict which tasks exceed a manageable development cycle?

The existing `railspike-effort` study gives us preserved forecasts, revisions, and a frozen reference. A credible evaluation would compare those estimates with simpler baselines and independently recorded outcomes such as required splitting, corrective work, and maintainer assessments.

The central limitation is that the current ratings are judgments about relative scope. Agreement between an agent’s forecast and its retrospective rating does not establish accuracy, and the ratings cannot be treated as measured hours.

**Assessment:** A worthwhile longer-term candidate, but the measurement target needs sharpening before it becomes a strong paper.

## Recommendation

Candidate 2 is the recommended first publication path, with candidate 1 as the flagship technical project. Candidate 4 is the best alternative if a clean experiment is preferable to extending the historical analysis.

For attention, the most valuable output would be something other researchers and agent builders can use: a benchmark, reviewed dataset, or evaluation harness associated with Railspike. That gives people a reason to cite and investigate the project even if they never adopt its workflow. These are promising directions, but the literature check here is preliminary; establish the precise novelty of the chosen candidate before committing to a full study.
