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

## ADDENDUM 2026-10-24: press release and deck added (filed 23-Oct 17:18 IST, after first fetch)
ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
CYBERTECH | 2026-10-24 | pressrelease+presentation, merged | 4+16 | NOT FOUND | 1,237,570 (addendum counted runs incl. loop) | 1

| agent | model | total_tok | wall | run# | note |
|---|---|---|---|---|---|
| A1 press release | claude-sonnet-5-5 | 64,589 | 212 s | 1 (+fix) | cumulative incl. p3 YoY-offset fix (58,678 base) |
| A2 press release | claude-sonnet-5-5 | 49,183 | 103 s | 1 (+fix) | cumulative (43,890 base) |
| A3 press release | claude-opus-5-5 | 110,237 | 610 s | 1 (+fix) | cumulative (84,557 base) |
| A1 deck | claude-sonnet-5-5 | 72,626 | 179 s | 1 | slides 12, 13, 15 rendered |
| A2 deck | claude-sonnet-5-5 | 55,734 | 105 s | 1 | below A1 |
| A3 deck | claude-opus-5-5 | 105,126 | 355 s | 1 | |
| A4 merged | claude-opus-5-5 | 308,942 | 1,187 s | 1 | fresh run over 3 docs |
| A5 merged | claude-opus-5-5 | 274,340 | 939 s | 1 | INCOMPLETE: C-1, F-1, M-1 |

| loop | agent | model | total_tok | wall | note |
|---|---|---|---|---|---|
| merged 1 | A4 (resumed) | claude-opus-5-5 | 116,729 | 688 s | delta from 425,671 cumulative |
| merged 1 | A5 (resumed) | claude-opus-5-5 | 80,064 | 169 s | delta; COMPLETE |
Merged loop cost: 196,793 tokens, 1 iteration. Second loop (approved 2026-10-24) not needed.
Extraction-fix cost (press release p3 offset, A1-A3 resumed): about 37,000 tokens, logged inside the cumulative rows above.
Change that would make the next run cheaper: re-query BSE for late Reg 30 filings (press release, deck) just before A4, so one merged A4/A5 pass covers all documents.
