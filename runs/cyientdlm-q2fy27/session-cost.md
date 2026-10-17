# Session cost: CYIENTDLM Q2 FY27 (/run-quarterly, 2026-10-17)

## DOCUMENT REVIEW summary row

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| CYIENTDLM | 2026-10-17 | results + presentation + press release | 30 (9 + 18 + 3) | ~22,662 (bytes/4: results 56,349 B ~14,087; presentation 27,398 B ~6,850; press release 6,901 B ~1,725) | 1,998,261 (lower bound; 2 rows ND, see below) | 2 |

## Per-agent ledger (one row per subagent run; figures from each task notification's subagent_tokens)

Accounting note: a resumed or continued agent reports its own invocation cost (it re-reads its prior context), so rows are additive. Two runs died in the laptop restart before a completion record: their tokens are ND and are NOT in total_run_tok.

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-results | claude-sonnet-5-5 | 81,444 | 235 s | 1 |
| A1-results page-2 scan re-extraction (continued) | claude-sonnet-5-5 | 121,417 | 529 s | 1b (orchestrator decision; mechanical) |
| A1-presentation | claude-sonnet-5-5 | 68,544 | 244 s | 1 |
| A1-pressrelease | claude-sonnet-5-5 | 51,530 | 167 s | 1 |
| A2-results | claude-sonnet-5-5 | 87,400 | 451 s | 1 |
| A2-presentation | claude-sonnet-5-5 | 60,048 | 111 s | 1 |
| A2-pressrelease | claude-sonnet-5-5 | 33,252 | 31 s | 1 |
| A3-results | claude-opus-5-5 | ND | ND | 1 (outputs complete; process exited before completion record) |
| A3-presentation | claude-opus-5-5 | 107,240 | 473 s | 1 |
| A3-pressrelease | claude-opus-5-5 | 60,135 | 259 s | 1 |
| A4 | claude-opus-5-5 | 317,838 | 1,099 s | 1 |
| A5 (died in restart, no output) | claude-opus-5-5 | ND | ND | 1 (mechanical failure) |
| A5 (fresh mechanical re-run) | claude-opus-5-5 | 250,514 | 1,028 s | 1r |
| **Base run subtotal (known)** | | **1,239,362** | | |

## Correction loops (logged separately; fresh agents, not resumed)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| LOOP1-A4-fix (fresh) | claude-opus-5-5 | 165,491 | 497 s | loop 1 |
| LOOP1-A5-reaudit (fresh, scoped + adversarial) | claude-opus-5-5 | 224,756 | 1,014 s | loop 1 |
| **Loop 1 subtotal** | | **390,247** | | |
| LOOP2-A4-fix (fresh; operator standing rule) | claude-opus-5-5 | 173,697 | 543 s | loop 2 |
| LOOP2-A5-reaudit (fresh, closure only) | claude-opus-5-5 | 194,955 | 633 s | loop 2 |
| **Loop 2 subtotal** | | **368,652** | | |
| **Loops total** (iterations: 2) | | **758,899** | | |

## Totals

- total_run_tok: 1,998,261 known (base 1,239,362 + loops 758,899). Lower bound: A3-results and the dead A5 run 1 are ND.
- Loops were 38.0% of the known run.

## Cost notes for the next run

- Fresh agents for loop fixes (given the audit path and exact gap list) cost 165-195k per row here, against 323-458k for resumed agents in the Aurum run.
- Page 2 of the results carried a corrupted embedded OCR layer. It passed the text-layer gate and needed a second A1 pass (121k). A1 could check character quality on the primary statement pages, not only character count.
- Change that would make the next run cheaper: have A1 flag a garbled-glyph ratio on statement pages in its first pass, so the scan re-extraction happens in one run.
