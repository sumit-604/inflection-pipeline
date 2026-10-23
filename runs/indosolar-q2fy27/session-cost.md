# Session cost: INDOSOLAR Q2 FY27 (/run-quarterly)

## Document review summary
| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| INDOSOLAR | 2026-10-23 | results + presentation (press release) | 6 + 3 | about 4,350 + 2,360 (fulltext chars / 4) | about 1,198,274 (sum of rows below with known totals, loop included; excludes two subagent runs killed by an app restart and a network drop, totals NOT FOUND) | 1 |

## Per-agent ledger
| agent | doc | model | total_tok | wall | run# |
|---|---|---|---|---|---|
| A1 extractor | results | claude-sonnet-5-5 | 97,342 | 5m 36s | 1 (pages 2-4 repaired from 300 dpi renders) |
| A2 enumerator | results | claude-sonnet-5-5 | 51,499 | 2m 49s | 1 |
| A3 forensics | results | claude-opus-5-5 | 109,000 | 6m 45s | 1 |
| A1 extractor | presentation (press release) | claude-sonnet-5-5 | 50,749 | 2m 04s | 1 (page-2 table repaired) |
| A2 enumerator | presentation (press release) | claude-sonnet-5-5 | 36,785 | 0m 57s | 1 |
| A3 forensics | presentation (press release) | claude-opus-5-5 | 91,422 | 4m 51s | 1 |
| A4 analyst | merged | claude-opus-5-5 | 245,525 | 34m 35s | 1 |
| A5 adversary | merged | claude-opus-5-5 | NOT FOUND (killed by app restart, wrote nothing) | NOT FOUND | 1 (mechanical) |
| A5 adversary | merged | claude-opus-5-5 | 231,981 | 17m 18s | 2 (mechanical re-run; INCOMPLETE: F1, M1, M2) |

Cost check: A2 below A1 on both documents (51,499 < 97,342; 36,785 < 50,749).

## Correction loop (iteration 1 of 1)
| agent | model | total_tok | wall | note |
|---|---|---|---|---|
| A4 analyst (fresh agent; original context lost in restart) | claude-opus-5-5 | 161,156 | 8m 54s | F1, M1, M2 fixed; S1-S5, S9 fixed |
| A5 adversary re-audit (resumed) | claude-opus-5-5 | NOT FOUND (killed by network drop about 18:47 IST, wrote nothing) | NOT FOUND | mechanical |
| A5 adversary re-audit (fresh) | claude-opus-5-5 | 122,815 | 4m 24s | COMPLETE |
| loop total (known) | | 283,971 | | |

Second-loop approval: operator standing approval relayed 2026-10-24 ("complete them fully"). Not used; A5 was COMPLETE after loop 1.

Base run (known): 914,303. Loop (known): 283,971. Total (known): 1,198,274.
Fresh tokens, re-read tokens and re-read multiple: NOT FOUND (the harness reports subagent totals only, not the cache split).
