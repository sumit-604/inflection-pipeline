# Session cost: KARNIKA H1 FY27 (/run-quarterly, 2026-10-17)

## DOCUMENT REVIEW summary row

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| KARNIKA | 2026-10-17 | results + concall + presentation | 64 (14 + 18 + 32) | ~36,277 (bytes/4: results 39,715 B ~9,929; concall 57,021 B ~14,255; presentation 48,371 B ~12,093) | 2,861,410 recorded (floor: excludes the loop-1 A4 row, NOT RECORDED) | 2 |

## Per-agent ledger (one row per subagent run; figures from each task notification's subagent_tokens)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-results | claude-sonnet-5-5 | 134,793 | 838 s | 1 |
| A1-concall | claude-sonnet-5-5 | 73,965 | 279 s | 1 |
| A1-presentation | claude-sonnet-5-5 | 81,538 | 346 s | 1 |
| A2-results | claude-sonnet-5-5 | 98,091 | 208 s | 1 |
| A2-concall | claude-sonnet-5-5 | 75,251 | 292 s | 1 |
| A2-presentation | claude-sonnet-5-5 | 47,302 | 155 s | 1 |
| A3-results | claude-opus-5-5 | 169,153 | 570 s | 1 |
| A3-concall | claude-opus-5-5 | 123,574 | 407 s | 1 |
| A3-presentation | claude-opus-5-5 | 148,718 | 585 s | 1 |
| A4 | claude-opus-5-5 | 430,343 | 1,289 s | 1 |
| A5 | claude-opus-5-5 | 320,689 | 1,108 s | 1 |
| **Base run subtotal** | | **1,703,417** | | |

Cost check: A2-concall 75,251 exceeded A1-concall 73,965 (+1.7%). Diagnosed in work/run-log.md: A1 concall has no turn IDs, so A2 read the fulltext once to build 167 turns. No source re-ingestion.

## Correction loops (logged separately)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A2-concall delta | claude-sonnet-5-5 | 39,791 | 64 s | loop 1 |
| A3-concall delta | claude-opus-5-5 | 84,659 | 254 s | loop 1 |
| A4 delta | claude-opus-5-5 | NOT RECORDED | NOT RECORDED | loop 1 |
| A5 re-audit | claude-opus-5-5 | 339,051 | 1,158 s | loop 1 |
| **Loop 1 subtotal (recorded)** | | **463,501** | | |
| A2-concall append | claude-sonnet-5-5 | 71,802 | 198 s | loop 2 |
| A4 delta | claude-opus-5-5 | 238,198 | 839 s | loop 2 |
| A5 final audit | claude-opus-5-5 | 384,492 | 1,080 s | loop 2 |
| **Loop 2 subtotal** | | **694,492** | | |

Loop-1 A4 row: the agent finished (block a4-loop1.yaml and the review written 15:24-15:25), but the laptop restart killed this session before its usage notice arrived. Its token count is lost and is not estimated.

## Totals
- Base run: 1,703,417
- Loops (recorded): 1,157,993
- **total_run_tok: 2,861,410 (recorded floor; one loop-1 A4 row NOT RECORDED)**
- loop_iterations: 2 (loop 2 under the operator batch rule, 2026-10-17; final A5 still INCOMPLETE, closed with open items flagged; no third loop)
- Orchestrator session tokens: not measured here.
