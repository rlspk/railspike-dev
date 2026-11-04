# Railspike research: 60 title candidates

Companion to the [six paper proposals](railspike-paper-candidates.md). These are reader-facing titles for articles introducing the research, suitable in tone for Hacker News, Tildes, and Lobsters; the eventual academic papers may use more descriptive subtitles. Bold entries are the strongest editorial picks. Questions remain open research questions, not implied findings.

## 1. Approval integrity

How agents preserve authorization across conversation, changed plans, and interrupted sessions.

1. **I asked a question. The coding agent started implementing.**
2. What, exactly, did you approve?
3. Can a coding agent remember what it has permission to do?
4. The plan changed. Does the approval still count?
5. “Ask before proceeding” needs an implementation
6. A state machine for human approval in coding agents
7. When a coding agent mistakes discussion for permission
8. Can we enforce approval without interrupting every action?
9. Recovering authorization after an agent loses context
10. Who gets to write the agent’s permission state?

Title 1 would introduce the maintainer-reported incident, with that attribution clear in the article. It should not imply a newly reproduced experiment.

## 2. Completion versus user acceptance

What completion reports and verification evidence actually establish about the requested outcome.

1. **The coding agent said “done.” What did that establish?**
2. Done according to whom?
3. Passing tests, unfinished work
4. What a green test suite leaves unanswered
5. Following an agent’s completion claim back to the evidence
6. Where verification ends and user acceptance begins
7. The feature was implemented. Was the request fulfilled?
8. Reading 25 development records for evidence of completion
9. How should a coding agent report work it could not verify?
10. What would convince you that an agent’s work is finished?

Title 8 refers to the existing 25-record analysis. It does not describe 25 independent experiments or independently verified outcomes.

## 3. The cost of human oversight

Whether plans and checkpoints reduce total human work or change where it occurs.

1. **How much work is it to supervise a coding agent?**
2. Does planning with an agent save debugging later?
3. Who measures the time spent reading AI-generated code?
4. The human work behind an autonomous coding task
5. When does another approval checkpoint pay for itself?
6. Less typing, more reviewing: how should we measure the tradeoff?
7. Counting the clarifications, reviews, and corrections
8. What does it cost to stay in control of a coding agent?
9. Can a faster agent create more work for its reviewer?
10. Measuring agent productivity through the human’s working day

## 4. Durable plans and handoffs

Whether another developer or agent can reconstruct the work and resume it correctly.

1. **The chat is gone. Can someone else finish the work?**
2. Can a Markdown plan survive a change of coding agent?
3. What should a coding agent leave for the next developer?
4. Resuming an agent’s work without replaying the conversation
5. Is the reason for this change anywhere in the repository?
6. How much context does the next developer actually need?
7. Can a fresh agent tell what was decided and what is still open?
8. Testing a development plan by handing it to someone else
9. Would you rather inherit the chat log or the plan?
10. What survives when a coding session ends?

## 5. How much process is enough?

Separating useful workflow requirements from repetition and overhead.

1. **Which instructions in your agent workflow are doing useful work?**
2. How much process does a coding agent need?
3. What happens if we remove one workflow rule at a time?
4. Can shorter agent instructions preserve the same safeguards?
5. Plans, checkpoints, and commits: which parts help?
6. Is the agent following the process or just producing the paperwork?
7. When does a coding workflow become too much ceremony?
8. Does repeating an instruction make an agent more likely to follow it?
9. How would we find the smallest useful agent workflow?
10. Testing the rules we give our coding agents

## 6. Scope estimation and task splitting

Whether agents can identify work that should be divided into smaller, reviewable cycles.

1. **Can a coding agent tell when a task is too big?**
2. When should an agent stop planning and split the task?
3. “One small change” and the recovery paths it brings along
4. Can past work help an agent recognize an oversized task?
5. What is a coding agent actually estimating?
6. Predicting which tasks will need a second development cycle
7. Can an agent forecast scope before it starts editing?
8. How much work fits in one reviewable change?
9. Does the agent’s estimate predict anything beyond its final estimate?
10. Estimating the whole task, including the parts that might go wrong

## Suggested first article

**The coding agent said “done.” What did that establish?**

Optional subtitle: *A case study of completion claims, verification limits, and unresolved acceptance gates in 25 development records.*

This is the strongest immediate pairing of an accessible title with evidence already available. The article should make clear that the records are retrospective, related in some cases, and not independently reproduced; human review of the research coding remains pending.
