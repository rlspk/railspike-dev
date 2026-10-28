# homepage_essay_framing debug log

## 2026-10-28T03:40Z — Step 1

### Necessary/useful instructions
- **RAILSPIKE.md, Step Guide / step1 `Original Query`**: preserving all five conversational turns kept the agreed material and the Readings decision visible in the artifact. Retain.
- **RAILSPIKE.md, Repository Boundary**: separated plan location (`railspike-dev`) from website and product edits. That mattered because Option B touches two implementation repositories. Retain.
- **effort-estimation.md, Recovering frozen references, step 3**: hash verification against the host manifest before rating was quick and unambiguous. Retain.
- **RAILSPIKE.md, Enhancement Requests**: gave the declined Readings request a durable record. A previous cycle had shipped the Readings, so this record matters. Retain.

### Redundant/unnecessary instructions
- **RAILSPIKE.md, Experimental Effort Estimation, plus effort-estimation.md, Estimate presentation**: the rules for cycle-estimate placement, option-estimate placement and "no approximation signs" are stated in both files and again in step1_solution_assessment.md. Suggest consolidating them into the guide and linking to it.

### Inapplicable instructions
- **Extended estimates legacy recovery**: not applicable to a new cycle.
- **Debug project marker lookup**: applied once; no conflict.

### Uncertain assessments
- **Intake checkpoint timing**: under standing enrollment, the user's first message ("familiarize yourself") came before any scope existed, so a prospective intake was not possible without a task. It is unclear whether intake should be captured at the first scoped request (here, the material list). Suggest clarifying when intake applies to conversations that begin with exploration.

## 2026-10-28T03:55Z — Step 2

### Necessary/useful instructions
- **step2_feature_description.md, Shared component inventory**: this surfaced that the README already has canonical install text and a four-step flowchart, so the homepage must mirror them rather than invent labels. Retain.
- **step2, Risks (impact / early validation / mitigation)**: this forced an uninstall fixture test before writing homepage copy, which is the main correctness hazard. Retain.

### Redundant/unnecessary instructions
- **step2, Known user or environment**: the clause is long, and it is inapplicable whenever no user or environment is named. Suggest moving the detail behind a link; keep a one-line pointer.

### Inapplicable instructions
- **Documentation-only scope rules**: the work type is an application change.

### Uncertain assessments
- **Work type for mixed website plus product README changes**: "application change" vs "documentation-only" doesn't cleanly describe a product README edit that ships alongside a website change. I classified the whole cycle as an application change and named the allowed files explicitly.

## 2026-10-28T04:05Z — Step 3

### Necessary/useful instructions
- **step3_development_plan_do.md, "Resolve each material risk before dependent work begins"**: this put the uninstall fixtures in Stage 1, ahead of the homepage copy that depends on them. Retain.
- **RAILSPIKE.md, Repository Boundary ("record paired implementation commits")**: this was needed to define the three-branch commit pattern. Retain, but see the uncertain item below.

### Redundant/unnecessary instructions
- **step3_development_plan_after.md, Effort estimation paragraph**: it restates the extended-estimate checks from step3_do and RAILSPIKE.md almost verbatim. Suggest a one-line pointer.

### Inapplicable instructions
- **Known user/environment replay stage**: no user or environment is named.
- **Database change documentation**: no database.

### Uncertain assessments
- **Multi-repository cycles**: the commit cadence ("1 + stages commits on the branch") assumes one branch. With a dev planning branch plus two implementation repositories, it is unclear whether a paired dev summary commit per stage satisfies "stage commit with its Step 4 summary update". I planned for the implementation commit first, then the dev summary commit that records its ID, matching prior website cycles.
- **Merge-order dependencies across repositories** (the website links to an anchor that only exists after the product merge) aren't addressed by the Completion Contract template.

## 2026-10-28T04:50Z — Step 4

### Necessary/useful instructions
- **step4_implementation_before.md, Planning Docs Commit Gate**: the organization rule moved the `docs/plans/README.md` entry into the planning commit, earlier than Step 3 had placed it. That was correct and easy to record. Retain.
- **step4_implementation_do.md, Stage Boundary Protocol**: verification before each commit caught three real defects (submodule leftovers, the copy button overlapping the prompt, the number alignment) before they were committed. Retain.
- **RAILSPIKE.md, Key Rules ("Prefer shared components")** and **the Step 2 shared component inventory**: these led to one prompt-box pattern and to prompts generated from the README, which made exact parity checkable. Retain.
- **step4_implementation_after.md, item 7 (report unverified items first)**: this kept the live-agent uninstall gap and the browser-coverage gap visible. Retain.

### Redundant/unnecessary instructions
- **step4_implementation_after.md, Effort estimation paragraph** and **step4_implementation_do.md, Effort estimation**: they overlap heavily with RAILSPIKE.md and the guide's presentation rules. Suggest one pointer each.

### Inapplicable instructions
- **Documentation-only verification items**: the work type is an application change.
- **Database/migration checks**: no database.

### Uncertain assessments
- **Multi-repository stage commits**: each stage produced an implementation commit plus a paired dev summary commit. Stage 4 had no implementation change, so its stage commit is dev-only. The instructions don't say whether "stage commit including the summary update" means the same commit, which is impossible across repositories. I used paired commits that record the IDs. Suggest stating this pattern explicitly for website and product work driven from `railspike-dev`.
- **Headless rendering limits** (minimum window width of 485 px; anchor-scrolled screenshots coming out blank) needed workarounds (an iframe, a probe copy). This is not a Railspike instruction issue, but a short note on render verification could help future website cycles.
