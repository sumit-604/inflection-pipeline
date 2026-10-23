# Session cost: CYBERTECH q2fy27 (/run-quarterly)

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
CYBERTECH | 2026-10-23 | results | 10 | NOT FOUND (A1 fulltext token count not reported; fulltext 443 lines, 30,848 bytes) | 863,957 (counted runs only; A3 and failed runs NOT FOUND) | 1

## Per-agent ledger
| agent | model | total_tok | wall | run# | note |
|---|---|---|---|---|---|
| A1 extractor | claude-sonnet-5-5 | 120,680 | 492 s | 1 | pages 2-10 image-only, rendered and transcribed |
| A2 enumerator | claude-sonnet-5-5 | 65,550 | 175 s | 1 | below A1, cost check pass |
| A3 forensics | claude-opus-5-5 | NOT FOUND | NOT FOUND | 1 | completed; usage lost in app restart |
| A4 analyst | claude-opus-5-5 | NOT FOUND | NOT FOUND | 1 (failed) | stream stall then app restart; nothing written; mechanical, not counted |
| A4 analyst | claude-opus-5-5 | 216,334 | 908 s | 2 | base review |
| A5 adversary | claude-opus-5-5 | NOT FOUND | NOT FOUND | 1 (failed) | network drop (ENOTFOUND ~18:47); mechanical, not counted |
| A5 adversary | claude-opus-5-5 | 324,823 | 1,616 s | 2 | INCOMPLETE: F1 F2 F3 C1 M1 M2 to A4 |

## Correction loop (logged separately)
| loop | agent | model | total_tok | wall | note |
|---|---|---|---|---|---|
| 1 | A4 analyst (resumed) | claude-opus-5-5 | 72,919 | 374 s | delta from cumulative 289,253 |
| 1 | A5 adversary (resumed) | claude-opus-5-5 | 63,651 | 216 s | delta from cumulative 388,474; COMPLETE |
Loop cost: 136,570 tokens, 1 iteration.

Operator standing approval 2026-10-24 ("complete them fully"): a second loop was allowed if needed. Not used; A5 was COMPLETE after loop 1.

## Orchestrator notes
- Base run (counted): 727,387. Loop: 136,570. Orchestrator session tokens not included.
- Session re-reads: A4 and A5 were resumed by SendMessage for the loop, so their cumulative counts include prompt re-reads of their own context.
- Fresh tokens / re-read tokens / re-read multiple: NOT FOUND (harness does not report the split for subagents).
- Change that would make the next run cheaper: write review and audit files in parts from the first turn, so a crash does not force a full re-run.
