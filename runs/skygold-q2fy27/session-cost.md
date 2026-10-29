# Session cost: SKYGOLD Q2 FY27 (/run-quarterly)

DOCUMENT REVIEW summary row (shared baseline):

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`SKYGOLD | 2026-10-28 | results + presentation + pressrelease (+ egm, esop supporting) | 16 + 41 + 3 (+ 21 + 4) = 85 | ~65,100 (260,354 fulltext chars / 4, all five files; results 106,926 chars ~26,700) | 2,305,779 (A5 loop-1 re-audit not counted, see note) | 1`

Basis: filed documents only. No call transcript (call on Saturday 31-Oct-2026 11:00, after this run).

## Per-agent ledger, base run

| agent | doc | model | total_tok | tool_uses | wall_s | run# |
|---|---|---|---|---|---|---|
| A1 | results | sonnet-5-5 | 132,976 | 30 | 356 | 1 |
| A1 | presentation | sonnet-5-5 | 135,616 | 25 | 305 | 1 |
| A1 | pressrelease | sonnet-5-5 | 52,487 | 10 | 102 | 1 |
| A1 | egm (supporting) | sonnet-5-5 | 76,408 | 12 | 145 | 1 |
| A1 | esop (supporting) | sonnet-5-5 | 54,211 | 15 | 113 | 1 |
| A1 addendum | presentation p17/p27 render check | sonnet-5-5 | 34,255 | 5 | 30 | 1 |
| A2 | results | sonnet-5-5 | 85,498 | 20 | 206 | 1 |
| A2 | presentation | sonnet-5-5 | 46,203 | 13 | 95 | 1 |
| A2 | pressrelease | sonnet-5-5 | 40,801 | 6 | 38 | 1 |
| A3 | results | opus-5-5 | 162,292 | 12 | 542 | 1 |
| A3 | presentation | opus-5-5 | 175,251 | 10 | 442 | 1 |
| A3 | pressrelease | opus-5-5 | 63,460 | 7 | 209 | 1 |
| A4 | merged | opus-5-5 | 388,239 | 24 | 925 | 1 |
| A5 | audit | opus-5-5 | 313,262 | 34 | 1,097 | 1 |
| **Base total** | | | **1,760,959** | | | |

## Correction loop 1 (own rows; loop_iterations = 1)

| agent | doc | model | total_tok | tool_uses | wall_s | run# |
|---|---|---|---|---|---|---|
| A2 (resumed) | presentation, M005-M017 | sonnet-5-5 | 65,692 | 7 | 59 | loop 1 |
| A4 (resumed) | merged, F1 F2 M2 M3 M4 | opus-5-5 | 479,128 | 10 | 500 | loop 1 |
| A5 (resumed) | loop-1 re-audit | opus-5-5 | NOT REPORTED | NOT REPORTED | NOT REPORTED | loop 1 |
| **Loop total (reported rows)** | | | **544,820** | | | |

Note on the A5 re-audit row: the agent returned its report and wrote its files (audit section "LOOP 1 RE-AUDIT", work/blocks/a5.yaml loop: 1, verdict COMPLETE). The session process restarted after a coordinator pause, so the harness never delivered the usage record. The figure is NOT REPORTED, not estimated. The loop-0 A5 run cost 313,262 for scale.

## Checks

- Cost order: every A2 below its A1 (results 85k < 133k; deck 46k < 136k; press release 41k < 52k). No source re-ingestion signature.
- Input discipline: no A2-A5 task message carried a path under inputs/. No agent reported reading a source PDF.
- Loop share of reported cost: 544,820 / 2,305,779 = 23.6%. Resumed A4 cost 479k, mostly re-read context (matches the batch lesson).
- Parallelism: at most two subagents at once until the coordinator pause; one at a time after RESUME.
- Pause: coordinator PAUSE after the loop-1 A4 return (no agent running during the pause); RESUME on 29-Oct-2026.
