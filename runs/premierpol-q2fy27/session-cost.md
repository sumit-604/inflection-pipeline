# Session cost: PREMIERPOL Q2 FY27 (/run-quarterly, 2026-10-17)

DOCUMENT REVIEW SUMMARY
ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
PREMIERPOL | 2026-10-17 | results | 8 | ~11,600 (fulltext 46,356 bytes / 4; A1 reported no token count) | 1,188,067 | 1

## Base run
| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A1 extractor (results) | claude-sonnet-5-5 | 63,240 | 287s | 1 |
| A2 enumerator (results) | claude-sonnet-5-5 | 63,929 | 199s | 1 |
| A2 cost-check diagnostic (resumed A2, 3-line answer) | claude-sonnet-5-5 | 65,856 | 15s | 1 (mechanical, not a re-run) |
| A3 forensics (results) | claude-opus-5-5 | 97,979 | 325s | 1 |
| A4 analyst | claude-opus-5-5 | 195,334 | 790s | 1 |
| A5 adversary | claude-opus-5-5 | 212,735 | 1,013s | 1 |
| base subtotal | | 699,073 | 2,629s | |

## Correction loop 1 (own rows)
| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A2 enumerator, loop fix A5-M1 | claude-sonnet-5-5 | 40,102 | 59s | loop 1 |
| A3 forensics, loop fix A5-M2 | claude-opus-5-5 | 77,074 | 206s | loop 1 |
| A4 analyst, re-merge | claude-opus-5-5 | 161,641 | 483s | loop 1 |
| A5 adversary, re-audit | claude-opus-5-5 | 210,177 | 904s | loop 1 |
| loop subtotal | | 488,994 | 1,652s | |

total_run_tok (base + loop, subagents): 1,188,067
loop_iterations: 1 (cap reached; A5 still INCOMPLETE, operator asked before a second)
Not counted: the orchestrator session's own tokens.

Notes
- A2 base came in 689 tokens above A1 (cost check). Diagnosed: no source access; one truncated cat forced a re-read of the structured file. A1 is cheap here because extraction is pdftotext over 8 pages.
- The diagnostic row is the resumed A2 call as reported by the harness; it includes the reloaded transcript.
