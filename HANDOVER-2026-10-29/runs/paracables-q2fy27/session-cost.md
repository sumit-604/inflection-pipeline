# Session cost: PARACABLES Q2 FY27 (/run-quarterly)

## Document review summary
| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| PARACABLES | 2026-10-28 | results + concall (ASR) + presentation + press release | 13 + 595 transcript lines + 37 + 3 | about 37,365 (fulltext chars / 4: results 10,298; concall 12,786; deck 12,222; release 2,059) | about 2,361,285 (base 1,992,409 + A1 fixes 21,599 + loop 347,277) | 1 |

## Per-agent ledger
Token figures are harness subagent totals. A resumed agent reports a cumulative total; its row shows the increment (cumulative less the earlier run).

| agent | doc | model | total_tok | wall | run# |
|---|---|---|---|---|---|
| A1 extractor | results | claude-sonnet-5-5 | 124,715 | 8m 28s | 1 (scan-ocr; garbled third-party OCR layer discarded; 38 corrections) |
| A1 extractor | presentation | claude-sonnet-5-5 | 76,710 | 4m 19s | 1 (text-only) |
| A1 extractor | pressrelease | claude-sonnet-5-5 | 63,647 | 3m 16s | 1 (scan-ocr; 7 corrections) |
| A1 extractor | concall (ASR .txt) | claude-sonnet-5-5 | 96,149 | 5m 32s | 1 |
| A2 enumerator | results | claude-sonnet-5-5 | 113,537 | 5m 38s | 1 |
| A2 enumerator | presentation | claude-sonnet-5-5 | 53,378 | 2m 11s | 1 |
| A2 enumerator | pressrelease | claude-sonnet-5-5 | 39,502 | 1m 01s | 1 |
| A2 enumerator | concall | claude-sonnet-5-5 | 42,853 | 1m 28s | 1 |
| A1 fix (resumed) | results: page 11 rows R990-R993 found by A2 | claude-sonnet-5-5 | 6,322 (131,037 less 124,715) | 0m 58s | 2 (pre-A3, gap named by A2) |
| A3 forensics | pressrelease | claude-opus-5-5 | 80,124 | 4m 37s | 1 |
| A3 forensics | concall | claude-opus-5-5 | 152,280 | 6m 45s | 1 |
| A3 forensics | presentation | claude-opus-5-5 | 164,829 | 9m 20s | 1 |
| A1 fix (resumed) | presentation: four structured defects named by A3 | claude-sonnet-5-5 | 15,277 (91,987 less 76,710) | 1m 29s | 2 (pre-A4) |
| A3 forensics | results | claude-opus-5-5 | 197,552 | 6m 56s | 1 |
| A4 analyst | merged | claude-opus-5-5 | 472,141 | 18m 32s | 1 |
| A5 adversary | merged | claude-opus-5-5 | 314,992 | 17m 22s | 1 (INCOMPLETE: 1 FACTUAL, 4 MISSING, 2 CONTRADICTION, 12 STYLE) |

## Correction loop (iteration 1 of 1)
| agent | model | total_tok | wall | note |
|---|---|---|---|---|
| A2 enumerator, concall (resumed) | claude-sonnet-5-5 | 3,402 (46,255 less 42,853) | 0m 28s | X1: five turns re-flagged, 32 of 35 substantive |
| A2 enumerator, presentation (resumed) | claude-sonnet-5-5 | 13,242 (66,620 less 53,378) | 1m 52s | M1: R523-R525 added, 525/525 IDs |
| A4 analyst (fresh, targeted) | claude-opus-5-5 | 217,595 | 11m 33s | X1, X2, M2, M3, F1, M4 fixed; verdict unchanged |
| A5 adversary (resumed) | claude-opus-5-5 | 113,038 (428,030 less 314,992) | 8m 00s | re-audit INCOMPLETE: 1 item C1 (deck ledger slide-index cells) |
| loop total | | 347,277 | | |

No second loop. Batch rule 4 allows one only for a FACTUAL or CONTRADICTION item that moves a verdict-card number. C1 moves none. It goes to the operator.

## Notes
- Cost check A2 < A1: results 113,537 < 124,715; presentation 53,378 < 76,710; pressrelease 39,502 < 63,647; concall 42,853 < 96,149. PASS.
- The results A1 cost is high because the filed PDF carried a garbled hidden OCR layer (labels one row off their values, digit misreads). A1 re-OCR'd all 13 pages at 300 dpi and checked statement pages against the images.
- The loop A4 ran as a fresh instance, not resumed. Resuming would have re-read a 472k-token context for six targeted fixes.
- The Notion page (74k chars) was saved to work/notion_snapshot_paracables_2026-10-28.md and passed by path to A3 x4 and A4. Each read only named sections.
- Subagents launched as background tasks by the harness despite foreground intent; the orchestrator waited on each notification before the next gate. At most four ran at once (the four A1s).
- Orchestrator session tokens: NOT FOUND (not exposed to this session).

Fresh tokens: NOT FOUND. Re-read tokens: NOT FOUND. Re-read multiple: NOT FOUND.
