# SESSION COST, INDIAMART q2fy27 (/run-quarterly, batch q2fy27-1028, batch 2)

## DOCUMENT REVIEW summary row (shared baseline)

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
---|---|---|---|---|---|---
INDIAMART | 2026-10-28 | results + presentation + pressrelease + concall (ASR) + fullstatements (targeted notes) | 18 + 69 + 5 + 808 lines + 62 | about 67,100 for the four core fulltexts (330,405 chars / 4); about 119,900 more for the full-statements fulltext (479,717 chars / 4); chars/4 estimate, not a tokenizer count | 3,779,541 | 1

- Base run: 2,622,017 tokens (17 agent runs, including the A1 concall gate-fix resume and the supplementary full-statements A1 and A3).
- Correction loop 1: 1,157,524 tokens (4 agent runs). A5 verdict after the loop: COMPLETE.
- Cost check, A2 below A1 for every document: results 75,342 < 95,785; presentation 43,600 < 162,123; pressrelease 42,488 < 49,072; concall 59,859 < 151,907 (both A1 passes). PASS.

## Per-agent token ledger

| Agent | Document | Model | total_tok | wall | run# | ledger |
|---|---|---|---|---|---|---|
| A1 | results | claude-sonnet-5-5 | 95,785 | 205s | 1 | base |
| A2 | results | claude-sonnet-5-5 | 75,342 | 182s | 1 | base |
| A1 | presentation | claude-sonnet-5-5 | 162,123 | 489s | 1 | base |
| A2 | presentation | claude-sonnet-5-5 | 43,600 | 80s | 1 | base |
| A1 | pressrelease | claude-sonnet-5-5 | 49,072 | 93s | 1 | base |
| A1 | concall | claude-sonnet-5-5 | 74,043 | 193s | 1 | base (hand-picked rows; sent back) |
| A1 | concall (resume: exhaustive sweep) | claude-sonnet-5-5 | 77,864 | 230s | 2 | base, gate fix |
| A3 | results | claude-opus-5-5 | 197,723 | 523s | 1 | base |
| A2 | pressrelease | claude-sonnet-5-5 | 42,488 | 49s | 1 | base |
| A2 | concall | claude-sonnet-5-5 | 59,859 | 122s | 1 | base |
| A1 | fullstatements (targeted notes) | claude-sonnet-5-5 | 171,225 | 464s | 1 | base, supplementary |
| A3 | presentation | claude-opus-5-5 | 257,201 | 656s | 1 | base |
| A3 | fullstatements addendum | claude-opus-5-5 | 233,339 | 701s | 1 | base, supplementary |
| A3 | concall | claude-opus-5-5 | 212,745 | 588s | 1 | base |
| A3 | pressrelease | claude-opus-5-5 | 115,913 | 355s | 1 | base |
| A4 | merged review | claude-opus-5-5 | 389,892 | 1,021s | 1 | base |
| A5 | audit (loop 0) | claude-opus-5-5 | 363,803 | 1,077s | 1 | base |
| A2 | presentation (loop 1, resume) | claude-sonnet-5-5 | 45,919 | 12s | 2 | loop 1 |
| A3 | fullstatements note 7 addendum (loop 1) | claude-opus-5-5 | 164,189 | 543s | 2 | loop 1 |
| A4 | merged review rewrite (loop 1, resume) | claude-opus-5-5 | 497,951 | 553s | 2 | loop 1 (harness figure for the resumed run; includes re-read of prior context) |
| A5 | re-audit (loop 1, resume) | claude-opus-5-5 | 449,465 | 295s | 2 | loop 1 (harness figure for the resumed run; includes re-read of prior context) |

Token figures are the harness's subagent_tokens per run. For a resumed agent (A1 concall resume, A2 presentation loop, A4 loop, A5 loop) the figure covers the resumed run and includes the re-read of the agent's earlier context.

## Notes

- Mechanical re-run, not a loop: A1 concall first built its structured file from a hand-picked row list (its own caveat). The orchestrator sent it back under Gate A1. The resume added R265-R614 by a mechanical sweep.
- Supplementary scope: A3 results named five notes the 18-page filing lacks. Per the session brief, a targeted A1 extracted the 62-page full statements (rows only on those notes), and an A3 addendum answered them. No A2 ran on that file; its rows are exempt from the orphan-ID gate (run-log).
- Loop 1 fired on A5 loop 0: FACTUAL 3, MISSING 3, CONTRADICTION 1 (STYLE 8 logged). Routed A2 (M1), A3 (M2), A4 (F1, F2, F3, C1, M3). A5 re-audit: all seven RESOLVED, no drift, two new STYLE notes (S9, S10).
- Orchestrator session tokens: NOT FOUND (the harness gives no per-session counter in this session).
- Fresh tokens, re-read tokens and re-read multiple: NOT FOUND as separate figures. The four resumed runs (1,071,199 tokens) are the visible re-read cost.
- Concurrency: at most two subagents at once, per the batch rule for the 6 GB machine.
