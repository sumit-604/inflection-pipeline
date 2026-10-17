# Session cost: TATACOMM Q2 FY27 (/run-quarterly, 2026-10-17)

## DOCUMENT REVIEW summary row

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| TATACOMM | 2026-10-17 | results + presentation | 42 (33 + 9) | ~31,540 (bytes/4: results 117,915 B ~29,479; presentation 8,243 B ~2,061) | 2,072,847 | 1 |

## Per-agent ledger (one row per subagent run; figures from each task notification's subagent_tokens)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-presentation | claude-sonnet-5-5 | 40,027 | 148 s | 1 |
| A2-presentation | claude-sonnet-5-5 | 36,356 | 104 s | 1 |
| A1-results | claude-sonnet-5-5 | 115,119 | 394 s | 1 |
| A3-presentation | claude-opus-5-5 | 67,515 | 314 s | 1 |
| A2-results | claude-sonnet-5-5 | 130,982 | 577 s | 1 |
| A3-results | claude-opus-5-5 | 270,427 | 613 s | 1 |
| A4 | claude-opus-5-5 | 346,211 | 975 s | 1 |
| A5 | claude-opus-5-5 | 285,689 | 1077 s | 1 |
| **Base run subtotal** | | **1,292,326** | | |

## Correction loop (logged separately)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| LOOP1-A4-fix | claude-opus-5-5 | 421,306 | 413 s | loop 1 |
| LOOP1-A5-reaudit | claude-opus-5-5 | 359,215 | 242 s | loop 1 |
| **Loop 1 subtotal** (iterations: 1) | | **780,521** | | |

**total_run_tok = 2,072,847** (base 1,292,326 + loop 780,521).

## Notes
- Loop rows are resumes of the same A4 and A5 agents (SendMessage). Each figure is the resume's own notification count; the resume re-reads the agent's prior context, which is why a 4-tool-use fix cost 421,306.
- Cost check: presentation A2 36,356 < A1 40,027 pass. Results A2 130,982 > A1 115,119 FAIL; diagnosed as structural (structured file 203,401 B is 1.7x the 117,915 B fulltext), no source re-ingestion; see work/run-log.md.
- Orchestrator session's own tokens are not in total_run_tok (read per session at close).
- Fresh tokens, re-read tokens, re-read multiple: NOT FOUND (task notifications report totals only, no cache split).
- Parallelism: at most 2 subagents at once after the parent's load cap (received mid-run; never exceeded).
