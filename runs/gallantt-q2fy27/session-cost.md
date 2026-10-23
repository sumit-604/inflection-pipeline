# Session cost: GALLANTT Q2 FY27 (/run-quarterly, 2026-10-19/20 overnight batch)

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
---|---|---|---|---|---|---
GALLANTT | 2026-10-20 | results (consolidated only) | 15 | ~21,305 (approx, chars/4 of all A1 fulltexts) | 1,700,250 | 2

## Per-agent ledger (one row per subagent run; a resumed agent's row counts its continuation only)
| agent | doc | model | total_tok | wall_s |
|---|---|---|---|---|
| A1 | results (run 1) | sonnet-5.5 | 113501 | 535 |
| A1 | results (verify continuation) | sonnet-5.5 | 132132 | 736 |
| A2 | results | sonnet-5.5 | 70789 | 231 |
| A3 | results | opus-5.5 | 141876 | 463 |
| A4 | Role 4 review | opus-5.5 | 204006 | 1213 |
| A5 | audit | opus-5.5 | 193828 | 860 |
| A4 | loop 1 fix (continuation) | opus-5.5 | 270238 | 435 |
| A5 | loop 1 re-audit | opus-5.5 | 142296 | 469 |
| A4 | loop 2 fix (continuation) | opus-5.5 | 326471 | 308 |
| A5 | loop 2 final re-audit | opus-5.5 | 105113 | 167 |

Loop rows are labelled "loop N". Orchestrator session tokens are not included (one orchestrator session ran the whole five-company batch).

---
# Session cost: GALLANTT Q2 FY27 call update (/run-quarterly, 2026-10-23, branch claude/quarterly-gallantt-call-q2fy27-7b3ed0)

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
---|---|---|---|---|---|---
GALLANTT | 2026-10-23 | resultsrev + presentation + concall (ASR) | 15 + 38 + 419 segments | ~44,594 (approx, chars/4 of the three new A1 fulltexts, 178,376 chars) | 2,609,654 | 1

## Per-agent ledger (one row per subagent run; a resumed agent's row counts its continuation only = reported cumulative minus its prior report)
| agent | doc | model | total_tok | wall_s |
|---|---|---|---|---|
| web-fetch | gallantt.com audio page (refused) | default | 7532 | 32 |
| A1 | presentation (run 1) | sonnet-5.5 | 80044 | 246 |
| A2 | presentation | sonnet-5.5 | 41760 | 73 |
| A3 | presentation | opus-5.5 | 197169 | 830 |
| A1 | presentation render check pp6,12,16,18,19,22,23,24 (continuation) | sonnet-5.5 | 68505 | 307 |
| A2 | presentation R761-R1489 (continuation) | sonnet-5.5 | 10764 | 115 |
| A3 | presentation reconcile with cell map (continuation) | opus-5.5 | 87417 | 365 |
| A1 | resultsrev (run 1) | sonnet-5.5 | 126735 | 442 |
| A2 | resultsrev | sonnet-5.5 | 62774 | 172 |
| A3 | resultsrev | opus-5.5 | 189856 | 465 |
| A1 | resultsrev stale-row fix R744 (continuation) | sonnet-5.5 | 3125 | 36 |
| A1 | concall ASR text | sonnet-5.5 | 80309 | 263 |
| A2 | concall | sonnet-5.5 | 68765 | 188 |
| A3 | concall | opus-5.5 | 187430 | 596 |
| A4 | merged review, four documents | opus-5.5 | 447425 | 1677 |
| A5 | audit | opus-5.5 | 390392 | 1643 |
| A2 | loop 1: resultsrev M1 (continuation) | sonnet-5.5 | 3240 | 27 |
| A1 | loop 1: presentation M2 p17 (continuation) | sonnet-5.5 | 5153 | 30 |
| A3 | loop 1: resultsrev M3 (continuation) | opus-5.5 | 30486 | 243 |
| A2 | loop 1: presentation M2 (continuation) | sonnet-5.5 | 2863 | 24 |
| A3 | loop 1: presentation M4, M9 (continuation) | opus-5.5 | 35676 | 259 |
| A4 | loop 1: grafts M3-M9 (continuation) | opus-5.5 | 136932 | 717 |
| A5 | loop 1: fresh re-audit | opus-5.5 | 345302 | 1143 |

Base run 2,050,002; loop 1 559,652 (21.4% of total). Local ASR (faster-whisper small, CPU) took about 1h50m wall under memory pressure (62-177 MB free on a 6 GB machine with four ASR jobs from parallel sessions); no tokens.
Fresh tokens: NOT FOUND (not exposed in session). Re-read tokens: NOT FOUND. Re-read multiple: NOT FOUND.
