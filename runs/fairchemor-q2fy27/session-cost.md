# Session cost: FAIRCHEMOR Q2 FY27 (/run-quarterly)

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
FAIRCHEMOR | 2026-10-23/24 | results+presentation+concall | 11+24+8 chunks | NOT FOUND (harness reports agent totals only) | 2,735,711 (excludes pass-2 A5 iteration 0, NOT FOUND) | pre-concall pass 1; concall pass 2

## Pass 1 (results + presentation, 23-Oct, session local_dc7dc103): 1,383,844 tok (base 1,125,556 + loop 258,288). Detail in git history of this file at 1e175fc1.

## Pass 2 (concall added, session local_9677c018)

| agent | doc | model | total_tok | wall | run# |
|---|---|---|---|---|---|
| A1 extractor | concall (ASR txt) | claude-sonnet-5-5 | 75,261 | 349 s | 1 |
| A2 enumerator | concall | claude-sonnet-5-5 | 49,740 | 88 s | 1 |
| A3 forensics | concall | claude-opus-5-5 | 142,982 | 402 s | 1 |
| A4 analyst | merged | claude-opus-5-5 | 315,945 | 995 s | 1 |
| A5 adversary | merged | claude-opus-5-5 | NOT FOUND (hand-back arrived after a session drop) | about 40 min | 1 |
| Base subtotal (known) | | | 583,928 | | |

Correction loops (pass 2)

| agent | doc | model | total_tok | wall | run# |
|---|---|---|---|---|---|
| A3 forensics | results addendum | claude-opus-5-5 | 80,209 | 266 s | loop 1 |
| A4 analyst | merged | claude-opus-5-5 | 352,625 cumulative (loop 1 + loop 2, resumed) | 675 s (loop 2) | loop 1-2 |
| A5 adversary | merged | claude-opus-5-5 | 335,105 cumulative (iteration 1 273,452 + iteration 2 61,653, resumed) | 989 s + 321 s | loop 1-2 |
| Loop subtotal (known) | | | 767,939 | | |

Cost checks: A2 < A1 on the concall (49,740 < 75,261). PASS.
Lost time: two session drops (about 00:45 and 06:45 IST 24-Oct) left finished agent output unread for about 7 hours in total; no work was lost.
ASR: local CPU (faster-whisper small.en), no tokens.

## Orchestrator session
- Fresh tokens: NOT FOUND (not exposed in session)
- Re-read tokens: NOT FOUND
- Re-read multiple: NOT FOUND
