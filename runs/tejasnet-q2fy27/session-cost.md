# Session cost: /run-quarterly TEJASNET Q2 FY27

DOCUMENT REVIEW summary row:

| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|---|---|---|---|---|---|---|
| TEJASNET | 2026-10-23/24 | results + concall + presentation | 12 + 13 + 13 = 38 | NOT MEASURED (fulltext chars: results 39,362; concall 43,037; presentation 18,544; total 100,943) | 3,808,980 (harness-reported subagent tokens, all rows below) | 2 (loop 2 under relayed operator approval, 2026-10-24) |

Token figures are the harness `subagent_tokens` per agent stop. For a resumed agent the figure is that agent's whole transcript at its stop, so it counts earlier context again. Treat resumed rows as an upper bound, not incremental cost.

## Per-agent ledger

| agent | model | total_tok | wall_s | run# | note |
|---|---|---|---|---|---|
| notion-digest (extraction helper) | sonnet | 153,359 | 177 | 1 | verbatim digest of the live Notion page |
| A1 results | claude-sonnet-5-5 | 76,813 | 282 | 1 | pages 2-12 OCR |
| A2 results | claude-sonnet-5-5 | 75,336 | 257 | 1 | below A1 |
| A3 results | claude-opus-5-5 | 188,089 | 498 | 1 | |
| A1 concall | claude-sonnet-5-5 | 81,533 | 279 | 1 | |
| A2 concall | claude-sonnet-5-5 | 62,064 | 180 | 1 | below A1 |
| A3 concall | claude-opus-5-5 | 174,732 | 868 | 1 | |
| A1 presentation | claude-sonnet-5-5 | 66,694 | 187 | 1 | |
| A2 presentation | claude-sonnet-5-5 | 55,592 | 416 | 1 | below A1 |
| A3 presentation | claude-opus-5-5 | 96,702 | 349 | 1 | |
| A4 merged | claude-opus-5-5 | 322,135 | 962 | 1 | stopped at app restart, resumed (mechanical) |
| A5 audit | claude-opus-5-5 | 366,091 | 576 | 1 | stopped at network drop, resumed (mechanical); INCOMPLETE |
| Base run subtotal | | 1,719,140 | | | |

## Correction loop rows (loop_iterations = 2)

| agent | model | total_tok | wall_s | loop | note |
|---|---|---|---|---|---|
| A2 results fix | claude-sonnet-5-5 | 87,385 | 57 | 1 | R852-R864 |
| A2 concall fix | claude-sonnet-5-5 | 67,193 | 41 | 1 | R325-R327 |
| A3 results addendum | claude-opus-5-5 | 213,888 | 187 | 1 | no new finding |
| A3 concall addendum | claude-opus-5-5 | 164,040 | 178 | 1 | no new finding |
| A4 fix pass | claude-opus-5-5 | 492,058 | 924 | 1 | 8 fixes |
| A5 re-audit | claude-opus-5-5 | 471,222 | 515 | 1 | INCOMPLETE (M1b) |
| Loop 1 subtotal | | 1,495,786 | | | |
| A2 results header fix | claude-sonnet-5-5 | 90,681 | 24 | 2 | relayed operator approval 2026-10-24 |
| A5 re-audit | claude-opus-5-5 | 503,373 | 208 | 2 | COMPLETE |
| Loop 2 subtotal | | 594,054 | | | |

Total: 1,719,140 + 1,495,786 + 594,054 = 3,808,980.

Orchestrator session tokens: NOT MEASURED.
Fresh tokens: NOT MEASURED. Re-read tokens: NOT MEASURED. Re-read multiple: NOT MEASURED (the harness exposes no per-call cache split to this session).
