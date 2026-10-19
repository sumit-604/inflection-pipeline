# Session cost: GOCL Q2 FY27 (/run-quarterly, 2026-10-19/20 overnight batch)

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
---|---|---|---|---|---|---
GOCL | 2026-10-20 | results | 16 | ~29,010 (approx, chars/4 of all A1 fulltexts) | 1,606,834 | 1

## Per-agent ledger (one row per subagent run; a resumed agent's row counts its continuation only)
| agent | doc | model | total_tok | wall_s |
|---|---|---|---|---|
| A1 | results (run 1) | sonnet-5.5 | 71569 | 897 |
| A1 | results (render continuation) | sonnet-5.5 | 122582 | 1585 |
| A2 | results | sonnet-5.5 | 85005 | 1359 |
| A3 | results | opus-5.5 | 234999 | 768 |
| A4 | Role 4 review | opus-5.5 | 265794 | 1183 |
| A5 | audit | opus-5.5 | 302305 | 1264 |
| A4 | loop 1 fix (continuation) | opus-5.5 | 346372 | 482 |
| A5 | loop 1 re-audit | opus-5.5 | 178208 | 563 |

Loop rows are labelled "loop N". Orchestrator session tokens are not included (one orchestrator session ran the whole five-company batch).
