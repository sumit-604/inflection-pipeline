# Session cost: ghvinfra q2fy27 (/run-quarterly)

DOCUMENT REVIEW summary row:

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| GHVINFRA | 2026-10-23 | results | 17 | NOT FOUND (fulltext 67,406 bytes, 843 lines; no token count recorded) | NOT FOUND (two agent usage records lost in restarts); recorded subtotal 1,451,263 | 2 |

Per-agent ledger (subagent_tokens from task notifications):

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1 extractor (results, 13 pages OCR) | claude-sonnet-5-5 | 124,743 | 9.0 min | 1 |
| A2 enumerator | claude-sonnet-5-5 | 111,758 | 5.0 min | 1 |
| A3 forensics | claude-opus-5-5 | 181,965 | 9.7 min | 1 |
| A1 page-image re-check (warrant count, pages 10 and 16) | claude-sonnet-5-5 | 131,365 (cumulative resume figure) | 2.0 min | 1 |
| A4 analyst | claude-opus-5-5 | NOT FOUND (usage lost in machine restart; files complete) | NOT FOUND | 1 |
| A5 adversary (base) | claude-opus-5-5 | NOT FOUND (usage lost in machine restart; files complete) | NOT FOUND | 1 |

Correction loop rows (kept apart from the base run):

| agent | model | total_tok | wall | loop iteration |
|---|---|---|---|---|
| A3 addendum FN26-FN31 | claude-opus-5-5 | 153,129 | 15.4 min | 1 |
| A4 fixes (M1 M4 M5 F1 F2, Q29-Q34) | claude-opus-5-5 | 178,897 | 10.5 min | 1 |
| A5 re-audit (iteration 2) | claude-opus-5-5 | 225,053 | 22.5 min | 1 |
| A4 fixes (F-A F-B F-C M-A M-B) | claude-opus-5-5 | 202,751 | 16.1 min | 2 |
| A5 re-audit (iteration 3), attempt 1 stalled (watchdog), attempt 2 lost in app restart | claude-opus-5-5 | NOT FOUND | NOT FOUND | 2 (mechanical, not counted) |
| A5 re-audit (iteration 3), audit of record | claude-opus-5-5 | 141,602 | 8.5 min | 2 |

Loop 2 approval: operator standing approval for this batch dated 2026-10-24 ("complete them fully"), relayed by the coordinating session; recorded in work/run_log.md.

Loop cost (recorded rows): loop 1 = 557,079; loop 2 = 344,353. Base run recorded = 549,831.

Fresh tokens: NOT FOUND. Re-read tokens: NOT FOUND. Re-read multiple: NOT FOUND (the orchestrator session has no per-turn cache figures in view).
