# Corrections and census qualifications

[Entry](./README.md) · [Batch report](./report.md)

## 2026-10-14T00:05:18.200717+00:00 — Final reconciliation

Original review groups and the census remain unchanged. Apply these corrections when reading them; neither changes the batch's acceptance category totals.

- **C010 original-study mapping:** its review's final Disposition mistakenly says R02. The correct overlap is **R03**, already correctly stated in that record's Context/identity field and the census. R02 belongs to C008. Evidence: [census C010](../historical_cycle_expansion/batch-1.md#c010--quiet_debug_mode), [original study](../railspike_paper/findings.md). One overlapping workflow remains one observation.
- **C028 and C029 era wording:** their generated context fields say “Railspike-named retained plans,” which is too specific. Use **numbered historical workflow artifacts; exact FDP/Railspike instruction revision and execution model unverified**. C029's initiating query explicitly references FDP ([S0151](./sources.md#s0151), line 7); C028's request ([S0147](./sources.md#s0147), line 7) establishes the operator objective, not an instruction version. Current paths or labels cannot pin a historical execution configuration.

## Qualifications discovered during deeper outcome review

The census measures retained completion status, while this analysis asks whether the full acceptance contract is evidenced. Do not silently change the census or treat these as extra candidates:

| Record | Census status | Deeper acceptance finding | Evidence |
| --- | --- | --- | --- |
| [C028](./review-4.md#c028) | Documented completion | Known unmet: literal passing full-suite gate, plus target-environment verification outstanding | S0149:11; S0150:60–62 |
| [C030](./review-5.md#c030) | Documented completion | Known unmet: mandatory manual browser/theme pass not run | S0157:10,49; S0158:29–33 |
| [C032](./review-5.md#c032) | Documented completion | Known unmet: final human browser acceptance pending, with no later closure recorded | S0164:53–55; S0166:39–45 and later stages |

C005, C012 and C015 already had unmet gates in the census. C013/C016/C017/C018/C020/C024 now carry an unknown full-acceptance judgment for the specific evidence gaps described in their reviews; missing evidence is not proof of a failed outcome. No change to the 216 eligible or 95 adjudication IDs is made. A later census-maintenance cycle can apply evidence-backed dated status corrections there.

## Relationship check

C024's rebuild hotfix precedes C036's manifest-parity change. Read-only `git -C /home/wsl/v3 merge-base --is-ancestor 31956831e0e742564e3b6aec80a06c42e060b08a df4bdc77c82addd23767c50b22475c5878378e77` exited 0. This establishes ancestry, not that the later implementation eliminates the earlier performance risk. Preserve the two scoped deliveries and their relationship; do not count their related accounts as independent failure replications.

## Future correction procedure

Append a UTC-dated entry identifying record/field, old and new interpretation, source version or immutable commit, and affected totals/queues. Preserve contradictory evidence and unresolved alternatives. Rubric revisions require rechecking every affected completed record before comparison; do not overwrite original excerpts or earlier study/census cutoffs.
