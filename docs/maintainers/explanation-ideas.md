# Ideas for explaining Railspike

Candidate ways to explain what Railspike is, its benefits, and how to use it. Written 2026-10-14, after the slide deck (`rlspk.github.io/slides/`) was merged but not yet linked. Each idea is a candidate for its own Railspike cycle; none is approved or scheduled. See the [backlog](./BACKLOG.md) for scheduled work.

## Highest value, lowest effort

1. **Link the deck.** The deck is merged but unlinked. Add a homepage line and a README line so it can be found. Check that `https://railspike.dev/slides/` is live first; it returned 404 immediately after the first push, probably while Pages built.
2. **A real "see it in action" page.** Use a completed cycle (for example the slides cycle) and show the actual Step 1–3 files, the approval messages, the stage commits, and the summary. The README tells the story, but nothing lets a skeptic click through a real one.
3. **A one-page cheat sheet.** Printable. Contents: the install prompt, the `Approved Step N` phrases, starting at Step 2, enabling debug mode, and what each step produces.

## Answering "is it for me?"

4. **When to use it and when to skip it.** A short decision guide: small fixes go straight through, substantial or ambiguous work gets planned. Builds trust by being honest about overhead.
5. **FAQ and limits.** Is it enforced (no: the agent follows instructions)? What does it cost in tokens? Does it work with my agent? How do I uninstall it? Uninstall instructions are already in `todo.txt`.
6. **How it compares.** Where it sits next to an agent's own plan mode and to ad-hoc prompting. Factual only; avoid claims about other tools that cannot be verified.

## Showing the benefits with evidence

7. **Outcome evidence.** Build on the exploratory debug data and the whitepaper backlog item. Even a small, honest table (cycles, scope changes caught at planning, rework) is stronger than assertions. Debug reports are agent observations, so label them that way and avoid claims of causation.
8. **Before/after example.** The same task done with a free-form prompt and with Railspike, showing the plan file and what would have been caught at review.

## Other formats

9. **A 60-second screen recording or GIF** of the approve-and-build loop, for the homepage and README.
10. **An interactive walkthrough page** that simulates a session and lets visitors click `Approved Step 1` to advance, reusing the deck's single-file, no-dependency approach.
11. **Talk materials.** Speaker script and review against Winston's "How to Speak" and Ernst's technical-talk guide, drafted in session; could become a short presenter guide.

## Suggested order

- **Quick wins:** items 1 and 3.
- **Main piece:** item 2, the most convincing and built from work that already exists. Items 2 and 4 together would make a natural single cycle.
- **Wait:** item 7 until the evidence is thicker, so claims stay proportional.
