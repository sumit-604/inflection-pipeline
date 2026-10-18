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

## ROLE 5 ADDENDUM (2026-10-18): concall machine transcript, A1-A5 plus correction loops

Source: faster-whisper medium.en transcript of the company recording (local CPU; transcription itself not in subagent tokens). Figures from each task notification; fresh agents throughout.

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-concall | claude-sonnet-5-5 | 97,816 | 317 s | R5-1 |
| A2-concall | claude-sonnet-5-5 | 51,632 | 79 s | R5-1 |
| A3-concall | claude-opus-5-5 | 114,061 | 319 s | R5-1 |
| A4-role5-merge | claude-opus-5-5 | 307,000 | 1,218 s | R5-1 |
| A5-role5-audit | claude-opus-5-5 | 317,801 | 1,258 s | R5-1 |
| **Role 5 base subtotal** | | **888,310** | | |
| R5-LOOP1-A4-fix (77 edits) | claude-opus-5-5 | 182,139 | 532 s | R5 loop 1 |
| R5-LOOP1-A5-reaudit | claude-opus-5-5 | 279,111 | 1,070 s | R5 loop 1 |
| R5-LOOP2-A4-fix (30 edits; standing rule) | claude-opus-5-5 | 134,845 | 330 s | R5 loop 2 |
| R5-LOOP2-A5-reaudit (final) | claude-opus-5-5 | 246,844 | 812 s | R5 loop 2 |
| **Role 5 loops subtotal** (iterations: 2) | | **842,939** | | |
| **Role 5 addendum total** | | **1,731,249** | | |

**total_run_tok (Role 4 + Role 5) = 3,804,096** (Role 4 2,072,847 + Role 5 1,731,249). Role 5 loop_iterations: 2. Final A5: INCOMPLETE on one minor open item (L2-C1), closed under the no-third-loop rule.
- Edits were applied by the orchestrator with a strict-anchor script (each FIND unique), not by rewriting the review.
- Change that would make the next run cheaper: give A4 a scoped edit tool for addenda, so the parts-and-spec splice step is not needed.
