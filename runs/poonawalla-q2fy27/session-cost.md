# Session cost: POONAWALLA Q2 FY27 (/run-quarterly, 2026-10-17)

## Document review summary row
ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
POONAWALLA | 2026-10-17 | results + concall + presentation + pressrelease | 30 + 19 + 42 + 3 = 94 | not measured; fulltext 336,053 chars (results 156,863; concall 66,549; presentation 106,938; pressrelease 5,703) | 2,346,535 | 1

## Per-agent ledger (base run)
| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1 results | claude-sonnet-5-5 | 147,185 | 489s | 1 |
| A1 concall | claude-sonnet-5-5 | 74,910 | 185s | 1 |
| A1 presentation | claude-sonnet-5-5 | 86,603 | 364s | 1 |
| A1 pressrelease | claude-sonnet-5-5 | 47,824 | 90s | 1 |
| A2 results | claude-sonnet-5-5 | 123,450 | 436s | 1 |
| A2 concall | claude-sonnet-5-5 | 69,885 | 177s | 1 |
| A2 presentation | claude-sonnet-5-5 | 52,268 | 94s | 1 |
| A2 pressrelease | claude-sonnet-5-5 | 34,320 | 30s | 1 |
| A3 results | claude-opus-5-5 | 255,203 | 585s | 1 |
| A3 concall | claude-opus-5-5 | 115,280 | 349s | 1 |
| A3 presentation | claude-opus-5-5 | 159,932 | 467s | 1 |
| A3 pressrelease | claude-opus-5-5 | 62,892 | 248s | 1 |
| A4 analyst | claude-opus-5-5 | 398,983 | 1234s | 1 |
| A5 adversary | claude-opus-5-5 | 320,363 | 852s | 1 |
| **Base run subtotal** | | **1,949,098** | | |

Cost checks: A2 below A1 on every document (results 123,450 < 147,185; concall 69,885 < 74,910; presentation 52,268 < 86,603; pressrelease 34,320 < 47,824).

## Correction loop ledger (loop_iterations = 1)
| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| LOOP 1: A4 graft (fresh agent) | claude-opus-5-5 | 186,924 | 607s | loop 1 |
| LOOP 1: A5 re-audit (killed by laptop restart, no output) | claude-opus-5-5 | NOT FOUND | NOT FOUND | loop 1, mechanical |
| LOOP 1: A5 re-audit (re-run, fresh agent) | claude-opus-5-5 | 210,513 | 783s | loop 1 |
| **Loop subtotal (known)** | | **397,437** | | |

## Total
total_run_tok: 2,346,535 (base 1,949,098 + loop 397,437). Excludes the killed A5 re-audit (tokens NOT FOUND) and the orchestrator session itself (not metered per stage).
Loop 2: not run (no operator approval in this session). Run closed with 4 open A5 items flagged.
