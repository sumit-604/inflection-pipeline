# Session cost: SUPREMEPWR H1 FY27 (/run-quarterly, 2026-10-17)

## DOCUMENT REVIEW summary row

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| SUPREMEPWR | 2026-10-17 | results (H1 FY27, SME half-year) | 15 | ~20,607 (bytes/4: fulltext 82,428 B) | 2,098,717 | 2 |

## Per-agent ledger (one row per subagent run; figures from each task notification's subagent_tokens)

Every run below is a fresh agent (no SendMessage resumes).

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-results | claude-sonnet-5-5 | 109,578 | 587 s | 1 |
| A2-results | claude-sonnet-5-5 | 76,630 | 211 s | 1 |
| A3-results | claude-opus-5-5 | 150,593 | 538 s | 1 |
| A4 | claude-opus-5-5 | 185,423 | 1,060 s | 1 |
| A5 | claude-opus-5-5 | 257,520 | 1,122 s | 1 |
| **Base run subtotal** | | **779,744** | | |

## Correction loops (logged separately)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| LOOP1-A2-fix (M12-M18) | claude-sonnet-5-5 | 46,159 | 41 s | loop 1 |
| LOOP1-A3-fix (register, A3-17) | claude-opus-5-5 | 185,773 | 718 s | loop 1 |
| LOOP1-A4-fix | claude-opus-5-5 | 171,443 | 596 s | loop 1 |
| LOOP1-A5-reaudit (killed by laptop restart) | claude-opus-5-5 | ND (no notification; tokens not reported) | ND | loop 1 |
| LOOP1-A5-reaudit (mechanical re-run) | claude-opus-5-5 | 268,727 | 1,132 s | loop 1 |
| **Loop 1 subtotal** | | **672,102** | | |
| LOOP2-A2-fix (M19-M35) | claude-sonnet-5-5 | 60,151 | 133 s | loop 2 |
| LOOP2-A3-fix (A3-18) | claude-opus-5-5 | 139,401 | 379 s | loop 2 |
| LOOP2-A4-fix | claude-opus-5-5 | 160,264 | 529 s | loop 2 |
| LOOP2-A5-reaudit | claude-opus-5-5 | 287,055 | 1,165 s | loop 2 |
| **Loop 2 subtotal** | | **646,871** | | |
| **Loops total** (iterations: 2) | | **1,318,973** | | |

## Totals

- total_run_tok: 2,098,717 (base 779,744 + loops 1,318,973). Loops were 62.8% of the run.
- Excluded: the killed loop-1 A5 (tokens never reported, ND) and the orchestrator session's own tokens (subagent ledger only).
- Cost check A2 < A1: pass (76,630 < 109,578).
- Loop 2 ran under the batch loop rule relayed by the parent session (operator 2026-10-17: finish without waiting). A5 still INCOMPLETE after loop 2; no third loop; open items flagged in the report.

## Cost notes for the next run

- A5 is the largest single cost: 258k, 269k, 287k across three audits. Each audit found new, smaller gaps (loop 2 gaps were bookkeeping plus one inference error).
- The laptop restart cost one full A5 run (tokens unknown, about 19 minutes).
- Change that would make the next run cheaper: give A1 a mandatory independent date and qualifier sweep of its own fulltext, so A2 does not discover header and signing-date rows across two loops.
