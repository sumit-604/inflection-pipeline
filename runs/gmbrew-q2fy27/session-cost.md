# Session cost: GMBREW Q2 FY27 (/run-quarterly, 2026-10-17)

## DOCUMENT REVIEW summary row

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| GMBREW | 2026-10-17 | results | 14 | ~8,288 (bytes/4: fulltext 33,153 B) | 1,837,603 | 2 |

## Per-agent ledger (one row per subagent run; figures from each task notification's subagent_tokens)

Accounting note: the run spanned two sessions. A1 and A2 ran in session local_42086b67 (stopped after A2); A3 onward ran in the resume session. A2's figure comes from that session's task notification. All loop agents were FRESH agents (not resumed), given the audit path and the exact item list.

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-results | claude-sonnet-5-5 | 104,725 | 566 s | 1 |
| A2-results | claude-sonnet-5-5 | 90,933 | 258 s | 1 |
| A3-results | claude-opus-5-5 | 169,053 | 550 s | 1 |
| A4 | claude-opus-5-5 | 233,673 | 740 s | 1 |
| A5 | claude-opus-5-5 | 264,838 | 1,048 s | 1 |
| **Base run subtotal** | | **863,222** | | |

## Correction loops (logged separately)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| LOOP1-A2-results-fix (M2-M4 rows) | claude-sonnet-5-5 | 42,724 | 55 s | loop 1 |
| LOOP1-A3-addendum (FN-12..FN-14; FN-05/09/10 revised) | claude-opus-5-5 | 147,834 | 626 s | loop 1 |
| LOOP1-A4-fix | claude-opus-5-5 | 189,142 | 646 s | loop 1 |
| LOOP1-A5-reaudit | claude-opus-5-5 | 221,921 | 787 s | loop 1 |
| **Loop 1 subtotal** | | **601,621** | | |
| LOOP2-A4-fix (A5-C1; operator standing ruling) | claude-opus-5-5 | 152,726 | 488 s | loop 2 |
| LOOP2-A5-reaudit (scoped) | claude-opus-5-5 | 220,034 | 925 s | loop 2 |
| **Loop 2 subtotal** | | **372,760** | | |
| **Loops total** (iterations: 2) | | **974,381** | | |

## Totals

- total_run_tok: 1,837,603 (base 863,222 + loops 974,381). Loops were 53.0% of the run.
- Cost check A2 < A1: pass (90,933 < 104,725).
- Orchestrator session tokens: not in this ledger (subagent ledger only).

## Cost notes for the next run

- Fresh loop agents ran cheaper than A5 run 1 (222k and 220k vs 265k), against the Aurum resumed re-audits (405k, 458k). Fresh agents with the audit path and item list are the cheaper route.
- The loop-2 A5 re-audit was scoped, yet still cost 220k, because it re-reads the 830-line review and the fulltext to recompute.
- The run-1 coverage miss started at A2: its auditor_paras count test counted A1 rows, not fulltext paragraphs.
- Change that would make the next run cheaper: have A2 run its count tests against fulltext paragraphs, and have A4 carry every material ledger row group (RPT rows, all balance-sheet lines). The loop-1 items would not exist, and that saves about 600k tokens.
