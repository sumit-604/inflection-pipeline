# Session cost: 530077 (Puretrop Fruits) q2fy27 (/run-quarterly, batch 2026-10-28, batch 4)

## DOCUMENT REVIEW summary row (shared baseline)

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`530077 | 2026-10-29 | results (no deck, no release, no concall) | 6 | ~4,596 (18,382 fulltext chars / 4) | 827,168 | 1`

- Base run (6 agent runs, including one A1 line re-check): 671,453 tokens.
- Correction loop 1 (A2 annotation fix, A4 fix, A5 re-audit): 155,715 tokens. Logged as its own rows below.
- Orchestrator session tokens: NOT MEASURED in-session (not included in total_run_tok).

## Per-agent ledger

Token figures are the harness `subagent_tokens` per agent run. Resumed runs (A1 re-check and every loop row) continued the same agent, whose counter is cumulative. Each resumed row is the counter after that turn minus the counter before it; the raw counter is in brackets.

| Agent | Document / step | Model | total_tok | Wall | Run # | Gate / result |
|---|---|---|---|---|---|---|
| A1 | results | claude-sonnet-5-5 | 82,028 | 265s | 1 | GATE A1 pass, 6/6 pages, R001-R446, units Rs Lakhs; p1-2 text layer (p2 hidden OCR layer kept verbatim), p3-6 no text layer, transcribed from 200 dpi renders; tie-outs within 0.01-0.02 Lakh |
| A1 | re-check of L157/L188 (A3-05) | claude-sonnet-5-5 | 5,991 (88,019) | 37s | 1 (resume) | 300 dpi render confirms both lines as printed; no edit |
| A2 | results | claude-sonnet-5-5 | 48,070 | 74s | 1 | GATE A2 pass, 446/446 IDs, zero orphans; below A1 |
| A3 | results | claude-opus-5-5 | 129,556 | 493s | 1 | GATE A3 pass, F1-F17 statused, 19 findings (4 FORWARD-SIGNAL, 12 AMBIGUOUS) |
| A4 | merged review | claude-opus-5-5 | 172,868 | 556s | 1 | PROCEED WITH FLAGS; cash conversion INDETERMINATE-WITH-DIRECTION (adverse); 18 questions |
| A5 | audit | claude-opus-5-5 | 232,940 | 1,058s | 1 | INCOMPLETE: 4 FACTUAL, 4 MISSING, 0 CONTRADICTION, 8 STYLE -> loop to A4 (M4 to A2) |
| A2 | correction loop 1 (M4) | claude-sonnet-5-5 | 2,729 (50,799) | 17s | loop 1 | R367/R395 annotated with signature time; counts unchanged |
| A4 | correction loop 1 (F1-F4, M1-M3) | claude-opus-5-5 | 66,335 (239,203) | 329s | loop 1 | 7 items fixed; verdict and cash status unchanged; questions 19 |
| A5 | re-audit | claude-opus-5-5 | 86,651 (319,591) | 327s | loop 1 | COMPLETE; all 8 loop-0 findings closed; STYLE S9-S12 logged |

Concurrency: one subagent at a time (6 GB machine, sibling sessions running).

## Notes for the coordinator
- Cost check: A2 48,070 < A1 82,028.
- Pages 3-6 of the results PDF carry no text layer at all; page 2 carries a hidden OCR layer (HiddenHorzOCR) with letter errors. A1 transcribed pages 3-6 from page images; tesseract was not used.
- The A3 start was delayed: the orchestrator waited for A2's token notification before the cost check, and the coordinator's stall check prompted the A3 launch. No agent step stalled.
- Resuming A2, A4 and A5 for the loop kept loop cost at 155,715 tokens, about 23% of the base run.
- Not committed: work/a1_tmp/ (derived page renders, 7.3 MB, and A1 scratch script).
- Fresh tokens / re-read tokens / re-read multiple: NOT MEASURED in-session (harness reports one total per subagent).
