# Session cost: HERITGFOOD Q2 FY27 (/run-quarterly, 2026-10-17)

## Document review baseline row
ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
HERITGFOOD | 2026-10-17 | results+presentation+pressrelease | 66 (16+45+5) | 38,350 approx (fulltext chars/4: results 77,738; presentation 63,737; pressrelease 11,925) | 2,625,523 | 2

## Base run (one row per subagent run)
| agent | doc | model | total_tok | wall | run# | note |
|---|---|---|---|---|---|---|
| A1 extractor | pressrelease | claude-sonnet-5-5 | 52,520 | 137s | 1 | text-only, 5/5 pp |
| A1 extractor | results | claude-sonnet-5-5 | 172,364 | 1,047s | 1+fix | cumulative: run 1 76,333 (215s) + fidelity re-read 96,031 (832s); pp2-6, 9-13 scan under OCR layer, 300 dpi, image-verified |
| A1 extractor | presentation | claude-sonnet-5-5 | 83,302 | 292s | 1 | text-only, 45/45 pp |
| A2 enumerator | pressrelease | claude-sonnet-5-5 | 39,993 | 53s | 1 | < A1, pass |
| A2 enumerator | presentation | claude-sonnet-5-5 | 51,595 | 72s | 1 | < A1, pass |
| A2 enumerator | results | claude-sonnet-5-5 | 49,303 | 89s | 1 | < A1, pass |
| A3 forensics | pressrelease | claude-opus-5-5 | 83,294 | 330s | 1 | |
| A3 forensics | presentation | claude-opus-5-5 | 149,427 | 474s | 1 | |
| A3 forensics | results | claude-opus-5-5 | 192,948 | 421s | 1 | |
| A4 analyst | merged | claude-opus-5-5 | 369,864 | 1,279s | 1 | |
| A5 adversary | merged | claude-opus-5-5 | 335,144 | 1,290s | 1 | INCOMPLETE |
| Base subtotal | | | 1,579,754 | | | |

## Loop iteration 1 (cap 1)
| agent | model | total_tok | wall | run# | note |
|---|---|---|---|---|---|
| A4 analyst (killed by laptop restart) | claude-opus-5-5 | ND | ND | loop1-a | no completion record; wrote nothing; mechanical re-run below |
| A4 analyst (fresh) | claude-opus-5-5 | 213,028 | 754s | loop1 | 13 findings applied |
| A5 adversary (fresh) | claude-opus-5-5 | 301,578 | 1,154s | loop1 | INCOMPLETE (2 FACTUAL) |
| Loop 1 subtotal | | 514,606 | | | |

## Loop iteration 2 (operator standing rule 2026-10-17)
| agent | model | total_tok | wall | run# | note |
|---|---|---|---|---|---|
| A4 analyst (fresh) | claude-opus-5-5 | 197,218 | 631s | loop2 | F1, F2, S9-S12 applied |
| A5 adversary (fresh) | claude-opus-5-5 | 333,945 | 1,131s | loop2 | COMPLETE |
| Loop 2 subtotal | | 531,163 | | | |

## Totals
- total_run_tok (subagents, base + loops): 2,625,523
- loop cost: 1,045,769 (39.8% of total)
- Orchestrator session tokens: ND (not metered in session).
- Fresh tokens / re-read tokens / re-read multiple: ND (subagent usage reports give totals only).

## Role 5 concall addendum (2026-10-19 to 2026-10-20)
Document review baseline row (concall): HERITGFOOD | 2026-10-19 | concall (ASR transcript) | 7 ten-minute blocks (66:25) | a1_extracted_text_tok ND (not measured) | 2,461,542 | 2

| agent | model | total_tok | wall | run# | note |
|---|---|---|---|---|---|
| A1 extractor (concall) | claude-sonnet-5-5 | 140,090 | 412s | r5-1 | 7/7 blocks, R001-R336 |
| A2 enumerator (concall) | claude-sonnet-5-5 | 75,775 | 148s | r5-1 | < A1, pass |
| A3 forensics (concall) | claude-opus-5-5 | 181,918 | 644s | r5-1 | F17 vs 34 questions |
| A4 analyst (Role 5 parts) | claude-opus-5-5 | 376,625 | 1,979s | r5-1 | 6 part files; orchestrator merged |
| A5 adversary (Role 5) | claude-opus-5-5 | 316,611 | 963s | r5-1 | INCOMPLETE |
| Role 5 base subtotal | | 1,091,019 | | | |
| A2 ledger addendum | claude-sonnet-5-5 | 50,172 | 74s | r5-loop1 | M01-M10 |
| A4 edit list (61 edits) | claude-opus-5-5 | 240,357 | 727s | r5-loop1 | |
| A5 re-audit | claude-opus-5-5 | 386,017 | 1,253s | r5-loop1 | INCOMPLETE |
| Role 5 loop 1 subtotal | | 676,546 | | | |
| A2 + A4 (killed by session restart) | | ND | ND | r5-loop2-a | wrote nothing; mechanical re-run |
| A2 ledger addendum (re-run) | claude-sonnet-5-5 | 120,636 | 342s | r5-loop2 | M11-M61, 397 rows |
| A4 edit list (44 edits, re-run) | claude-opus-5-5 | 197,101 | 601s | r5-loop2 | |
| A5 final re-audit | claude-opus-5-5 | 376,240 | 1,123s | r5-loop2 | INCOMPLETE; 6 open items flagged |
| Role 5 loop 2 subtotal | | 693,977 | | | |

- Role 5 total_run_tok: 2,461,542 (loop cost 1,370,523, 55.7%).
- Transcription (faster-whisper on local CPU, 1,938 s) used no model tokens.
- Grand total_run_tok (Role 4 run 2,625,523 + Role 5 addendum 2,461,542): 5,087,065.
