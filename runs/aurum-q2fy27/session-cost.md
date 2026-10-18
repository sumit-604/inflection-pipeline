# Session cost: AURUM Q2 FY27 (/run-quarterly, 2026-10-17)

## DOCUMENT REVIEW summary row

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| AURUM | 2026-10-17 | results + presentation + press release | 62 (20 + 38 + 4) | ~39,547 (bytes/4: results 72,419 B ~18,105; presentation 78,385 B ~19,596; press release 7,384 B ~1,846) | 3,071,525 | 2 |

## Per-agent ledger (one row per subagent run; figures from each task notification's subagent_tokens)

Accounting note: a resumed agent (SendMessage) reports its own invocation cost, which includes re-reading its full prior context. Loop rows are therefore additive, not cumulative.

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-results | claude-sonnet-5-5 | 178,108 | 653 s | 1 |
| A1-presentation | claude-sonnet-5-5 | 91,270 | 341 s | 1 |
| A1-pressrelease | claude-sonnet-5-5 | 48,160 | 171 s | 1 |
| A2-results | claude-sonnet-5-5 | 81,437 | 227 s | 1 |
| A2-presentation | claude-sonnet-5-5 | 43,027 | 78 s | 1 |
| A2-pressrelease | claude-sonnet-5-5 | 35,724 | 45 s | 1 |
| A3-results | claude-opus-5-5 | 188,941 | 609 s | 1 |
| A3-presentation | claude-opus-5-5 | 137,033 | 510 s | 1 |
| A3-pressrelease | claude-opus-5-5 | 65,159 | 254 s | 1 |
| A4 | claude-opus-5-5 | 252,276 | 708 s | 1 |
| A5 | claude-opus-5-5 | 305,862 | 1,002 s | 1 |
| **Base run subtotal** | | **1,426,997** | | |

## Correction loops (logged separately)

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| LOOP1-A2-results-fix (annotation) | claude-sonnet-5-5 | 82,482 | 14 s | loop 1 |
| LOOP1-A4-fix | claude-opus-5-5 | 322,753 | 384 s | loop 1 |
| LOOP1-A5-reaudit | claude-opus-5-5 | 404,733 | 486 s | loop 1 |
| **Loop 1 subtotal** | | **809,968** | | |
| LOOP2-A4-fix (operator-approved) | claude-opus-5-5 | 376,731 | 364 s | loop 2 |
| LOOP2-A5-reaudit (scoped) | claude-opus-5-5 | 457,829 | 322 s | loop 2 |
| **Loop 2 subtotal** | | **834,560** | | |
| **Loops total** (iterations: 2) | | **1,644,528** | | |

## Totals

- total_run_tok: 3,071,525 (base 1,426,997 + loops 1,644,528). Loops were 53.5% of the run.
- A3 forensics and A3 skip: loop 1 skipped A3 (no new rows or IDs). Not counted.
- Orchestrator session tokens: not in this ledger (subagent ledger only).

## Cost notes for the next run

- Resume re-reads drive loop cost: A5 re-audits cost 405k and 458k against a 306k first audit. A scoped re-audit (loop 2) still cost more than the full first audit, because the resumed context is re-read. A fresh A5 given only the review, the audit file and the changed-line list would likely be cheaper.
- A1-results ran OCR on pages 5-20 (zero-character scans): 178k, the largest A1.
- Change that would make the next run cheaper: send loop fixes to a fresh agent with the audit file path and the exact line list, not a resumed agent carrying its full prior context.

## ROLE 5 ADDENDUM (2026-10-18): concall machine transcript, A1-A5 plus correction loops

Source: faster-whisper medium.en transcript of the company recording (local CPU; transcription itself not in subagent tokens). Figures from each task notification; fresh agents throughout.

| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1-concall | claude-sonnet-5-5 | 76,807 | 182 s | R5-1 |
| A2-concall | claude-sonnet-5-5 | 70,986 | 143 s | R5-1 |
| A3-concall | claude-opus-5-5 | 151,371 | 548 s | R5-1 |
| A4-role5 (died in restart, no output) | claude-opus-5-5 | ND | ND | R5-1 (mechanical failure) |
| A4-role5 rerun (parts + merge spec; orchestrator spliced) | claude-opus-5-5 | 342,366 | 1,527 s | R5-1r |
| A5-role5-audit | claude-opus-5-5 | 333,089 | 1,216 s | R5-1 |
| **Role 5 base subtotal (known)** | | **974,619** | | |
| R5-LOOP1-A4-fix (53 edits) | claude-opus-5-5 | 190,975 | 483 s | R5 loop 1 |
| R5-LOOP1-A5-reaudit | claude-opus-5-5 | 292,896 | 976 s | R5 loop 1 |
| R5-LOOP2-A4-fix (5 edits; standing rule) | claude-opus-5-5 | 62,580 | 121 s | R5 loop 2 |
| R5-LOOP2-A5-reaudit (final) | claude-opus-5-5 | 177,342 | 652 s | R5 loop 2 |
| **Role 5 loops subtotal** (iterations: 2) | | **723,793** | | |
| **Role 5 addendum total (known)** | | **1,698,412** | | |

**total_run_tok (Role 4 + Role 5) = 4,769,937 known** (Role 4 3,071,525 + Role 5 1,698,412; one Role 5 row ND). Role 5 loop_iterations: 2. Final A5: INCOMPLETE on one minor open item (L2-F1), closed under the no-third-loop rule.
