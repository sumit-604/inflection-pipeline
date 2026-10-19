# Session cost: TATVA Q2 FY27 (/run-quarterly, 2026-10-19/20 overnight batch)

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
---|---|---|---|---|---|---
TATVA | 2026-10-20 | results + presentation + notice | 57 (results 14, deck 42, notice 1) | ~38,808 (approx, chars/4 of all A1 fulltexts) | 2,791,647 | 1

## Per-agent ledger (one row per subagent run; a resumed agent's row counts its continuation only)
| agent | doc | model | total_tok | wall_s |
|---|---|---|---|---|
| A1 | notice | sonnet-5.5 | 37594 | 508 |
| A2 | notice | sonnet-5.5 | 32495 | 211 |
| A1 | results (scan) | sonnet-5.5 | 135575 | 1192 |
| A3 | notice | opus-5.5 | 58995 | 308 |
| A1 | presentation (run 1) | sonnet-5.5 | 106793 | 1517 |
| A1 | presentation (render continuation) | sonnet-5.5 | 128876 | 239 |
| A2 | presentation | sonnet-5.5 | 69583 | 750 |
| A2 | results | sonnet-5.5 | 112725 | 1372 |
| A1 | results (loop-back continuation) | sonnet-5.5 | 137519 | 271 |
| A2 | results (loop-back continuation) | sonnet-5.5 | 117890 | 84 |
| A3 | presentation | opus-5.5 | 217764 | 971 |
| A3 | results | opus-5.5 | 183831 | 595 |
| A4 | Role 4 review | opus-5.5 | 449068 | 1840 |
| A5 | audit | opus-5.5 | 321442 | 1326 |
| A4 | loop 1 fix (continuation) | opus-5.5 | 531004 | 500 |
| A5 | loop 1 re-audit | opus-5.5 | 150493 | 486 |

Loop rows are labelled "loop N". Orchestrator session tokens are not included (one orchestrator session ran the whole five-company batch).
