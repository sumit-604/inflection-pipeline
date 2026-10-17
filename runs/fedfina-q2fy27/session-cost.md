# Session cost: FEDFINA Q2 FY27 (/run-quarterly, 2026-10-17)

## DOCUMENT REVIEW summary row

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| FEDFINA | 2026-10-17 | results + presentation + press release | 60 (15 + 42 + 3) | ~45,621 (bytes/4: results 93,788 B ~23,447; presentation 78,529 B ~19,632; press release 10,167 B ~2,542) | 2,948,983 | 2 |

## Per-agent ledger (one row per subagent run; figures from each task result's subagent_tokens)

Accounting note: a resumed agent (SendMessage) reports its own invocation cost, which includes re-reading its full prior context. Loop rows are therefore additive, not cumulative.

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-results | claude-sonnet-5-5 | 88,024 | 340 s | 1 |
| A1-presentation | claude-sonnet-5-5 | 106,689 | 467 s | 1 |
| A1-pressrelease | claude-sonnet-5-5 | 50,591 | 303 s | 1 |
| A2-results | claude-sonnet-5-5 | 73,255 | 247 s | 1 |
| A2-presentation | claude-sonnet-5-5 | 51,715 | 138 s | 1 |
| A2-pressrelease | claude-sonnet-5-5 | 42,064 | 64 s | 1 |
| A3-results | claude-opus-5-5 | 166,179 | 446 s | 1 |
| A3-presentation | claude-opus-5-5 | 179,555 | 648 s | 1 |
| A3-pressrelease | claude-opus-5-5 | 75,361 | 280 s | 1 |
| A4 | claude-opus-5-5 | 319,476 | 1,070 s | 1 |
| A5 | claude-opus-5-5 | 381,867 | 1,098 s | 1 |
| **Base run subtotal** | | **1,534,776** | | |

## Correction loops (logged separately)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| LOOP1-A2-results-fix (resumed) | claude-sonnet-5-5 | 77,468 | 25 s | loop 1 |
| LOOP1-A3-results-addendum (resumed) | claude-opus-5-5 | 185,940 | 141 s | loop 1 |
| LOOP1-A4-fix (resumed) | claude-opus-5-5 | 396,064 | 411 s | loop 1 |
| LOOP1-A5-reaudit (resumed) | claude-opus-5-5 | 474,761 | 346 s | loop 1 |
| **Loop 1 subtotal** | | **1,134,233** | | |
| LOOP2-A4-fix, resumed agent killed by laptop restart (no output; mechanical, no completion record) | claude-opus-5-5 | NOT FOUND | NOT FOUND | loop 2 (void) |
| LOOP2-A4-fix (fresh, operator-approved) | claude-opus-5-5 | 140,625 | 477 s | loop 2 |
| LOOP2-A5-reaudit (fresh, scoped) | claude-opus-5-5 | 139,349 | 549 s | loop 2 |
| **Loop 2 subtotal** | | **279,974** | | |
| **Loops total** (iterations: 2) | | **1,414,207** | | |

## Totals

- total_run_tok: 2,948,983 (base 1,534,776 + loops 1,414,207). Loops were 48.0% of the run.
- The killed loop-2 resumed A4 reported no token count; it is NOT FOUND and not in the total.
- Cost check A2 < A1 held for all three documents.
- Orchestrator session tokens: not in this ledger (subagent ledger only). Orchestrator image checks (results p5, deck slides 22 and 25) ran inline.

## Cost notes for the next run

- Fresh scoped loop agents were cheaper than resumed ones: loop-2 A4 141k and A5 139k, against loop-1 resumed A4 396k and A5 475k. Resumed agents re-read their whole prior context.
- A3 caught A1 sign misreads on an OCR-noisy text layer (results p5). A quick orchestrator image check of contested cells settled them without an A1 re-run.

Change that would make the next run cheaper: send every loop fix to a fresh agent with the audit path and the exact line list, never a resumed agent.
