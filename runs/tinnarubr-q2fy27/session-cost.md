# Session cost: TINNARUBR Q2 FY27 (/run-quarterly)

## Document review summary
| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| TINNARUBR | 2026-10-23 | results + presentation (press release) | 13 + 3 | about 24,500 + 1,600 (fulltext chars / 4; results fulltext holds embedded plus OCR text) | about 1,376,000 (sum of rows below, loop included; excludes two runs lost to the machine restart) | 1 |

## Per-agent ledger
Token figures are harness subagent totals where reported; "est" marks the agent's own estimate.

| agent | doc | model | total_tok | wall | run# |
|---|---|---|---|---|---|
| A1 extractor | presentation | claude-sonnet-5-5 | 52,750 | 2m 15s | 1 |
| A2 enumerator | presentation | claude-sonnet-5-5 | 37,534 | 1m 51s | 1 |
| A3 forensics | presentation | claude-opus-5-5 | about 45,000 (est; harness total lost in restart) | NOT FOUND | 1 |
| A1 extractor | results | claude-sonnet-5-5 | 88,349 | 5m 13s | 1 (text-only; statement pages corrupt OCR layer) |
| A1 extractor | results | claude-sonnet-5-5 | NOT FOUND (killed by machine restart, wrote nothing) | NOT FOUND | 2 (mechanical) |
| A1 extractor | results | claude-sonnet-5-5 | 182,770 | 13m 20s | 3 (OCR repair; mechanical re-run) |
| A2 enumerator | results | claude-sonnet-5-5 | 68,056 | 2m 36s | 1 |
| A3 forensics | results | claude-opus-5-5 | 190,294 | 8m 33s | 1 |
| A4 analyst | merged | claude-opus-5-5 | 285,147 | 16m 51s | 1 |
| A5 adversary | merged | claude-opus-5-5 | 302,934 | 17m 52s | 1 (INCOMPLETE) |

## Correction loop (iteration 1 of 1)
| agent | model | total_tok | wall | note |
|---|---|---|---|---|
| A4 analyst (resumed) | claude-opus-5-5 | 59,009 (cumulative 344,156 less 285,147) | 6m 50s | F1-F6 fixed |
| A5 adversary (resumed) | claude-opus-5-5 | 63,935 (cumulative 366,869 less 302,934) | 3m 24s | re-audit COMPLETE |
| loop total | | 122,944 | | |

## Notes
- Cost check A2 < A1: presentation 37,534 < 52,750; results 68,056 < 182,770. PASS.
- The results A1 cost is high because the embedded text layer was corrupt OCR. The extractor re-OCR'd six pages and read 692 cells from page images.
- Orchestrator session tokens: NOT FOUND (not exposed to this session).

Fresh tokens: NOT FOUND. Re-read tokens: NOT FOUND. Re-read multiple: NOT FOUND.
