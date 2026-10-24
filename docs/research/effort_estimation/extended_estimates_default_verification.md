# Default-on extended estimates verification

Static document review on 2026-10-24T23:21:31.000439+00:00. Product base: `c336536f88d1ce471b4f582a7d87203864f8526e`. Scope: four product Markdown files; no runtime, tooling, frozen-reference or host installation changes. This is document consistency evidence, not a live-agent experiment or validated effort forecasting.

| Scenario | Reviewed outcome |
| --- | --- |
| New enrolled cycle, no override/policy | Enabled; record mode and estimate options/stages. |
| Unselected cycle | No estimates, mode fields or extra selection question. |
| Explicit disable on new enrolled cycle | Disabled overrides fallback and host policy. |
| Explicit enable on recorded disabled cycle | Enabled prospectively; prior history retained. |
| New enrolled cycle, host opt-out | Disabled; host policy precedes fallback. |
| Recorded enabled cycle, host policy later disabled | Recorded enabled state survives. |
| Recorded disabled cycle after upgrade | Disabled state survives. |
| Older missing field, prior enable request/policy | Recover enabled state; no backfill. |
| Older missing field, no enablement under old rules | Retain disabled behavior; record now. |
| Older missing field, conflicting/unknown evidence | Clarify before dependent estimation; continue independent work. |
| Late activation | Current dated estimates only; missing originals remain missing. |
| No debug mode | Same estimation behavior; debug remains independent. |
| Scoring/revisions | Original R1 semantics and append-only histories retained; stage totals never summed. |

Passed: product link checker (15 Markdown files); development link checker (164 Markdown files, 80 acknowledged baseline targets); existing Git-workflow fixture; whitespace and four-file product scope review. Search found no remaining obsolete study-enrollment-alone/extra-opt-in default claims in the product. Reviewed README, root, effort guide and all estimation-related workflow references for consistent precedence. Frozen R1 hashes verified at entry. Installation/migration and release verification belong to Stage 2 and remain pending here.
