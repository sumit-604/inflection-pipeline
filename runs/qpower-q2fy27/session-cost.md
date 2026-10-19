# Session cost: QPOWER Q2 FY27 (/run-quarterly, 2026-10-19/20 overnight batch)

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
---|---|---|---|---|---|---
QPOWER | 2026-10-20 | document review (2 one-off disclosures) | 5 (EGM 4, Turkiye 1) | ~3,126 (approx, chars/4 of all A1 fulltexts) | 1,310,123 | 2

## Per-agent ledger (one row per subagent run; a resumed agent's row counts its continuation only)
| agent | doc | model | total_tok | wall_s |
|---|---|---|---|---|
| A1 | egm | sonnet-5.5 | 43988 | 508 |
| A1 | turkiye | sonnet-5.5 | 37453 | 535 |
| A2 | egm | sonnet-5.5 | 41328 | 185 |
| A2 | turkiye | sonnet-5.5 | 32962 | 225 |
| A3 | turkiye | opus-5.5 | 56780 | 255 |
| A3 | egm | opus-5.5 | 76037 | 342 |
| A4 | document review | opus-5.5 | 111279 | 416 |
| A5 | audit | opus-5.5 | 178958 | 1134 |
| A2 | turkiye (loop 1, continuation) | sonnet-5.5 | 35323 | 97 |
| A3 | turkiye (loop 1, continuation) | opus-5.5 | 68723 | 108 |
| A4 | loop 1 fix (continuation) | opus-5.5 | 175213 | 390 |
| A5 | loop 1 re-audit | opus-5.5 | 139975 | 575 |
| A4 | loop 2 fix (continuation) | opus-5.5 | 221848 | 291 |
| A5 | loop 2 final re-audit | opus-5.5 | 90256 | 276 |

Loop rows are labelled "loop N". Orchestrator session tokens are not included (one orchestrator session ran the whole five-company batch).
