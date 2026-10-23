# Session cost: FAIRCHEMOR Q2 FY27 (/run-quarterly)

ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
FAIRCHEMOR | 2026-10-23 | results+presentation | 11+24 | NOT FOUND (harness reports agent totals only; fulltext bytes 42,471 + 51,975) | 1,383,844 | 1

## Per-agent ledger (subagent_tokens as reported by the harness)

| agent | doc | model | total_tok | wall | run# |
|---|---|---|---|---|---|
| A1 extractor | results | claude-sonnet-5-5 | 88,093 | 251 s | 1 |
| A2 enumerator | results | claude-sonnet-5-5 | 70,217 | 146 s | 1 |
| A3 forensics | results | claude-opus-5-5 | 117,513 | 356 s | 1 |
| A1 extractor | presentation | claude-sonnet-5-5 | 106,738 | 378 s | 1 |
| A2 enumerator | presentation | claude-sonnet-5-5 | 62,196 | 107 s | 1 |
| A3 forensics | presentation | claude-opus-5-5 | 166,605 | 447 s | 1 |
| A4 analyst | merged | claude-opus-5-5 | 253,793 | 776 s | 1 |
| A5 adversary | merged | claude-opus-5-5 | 260,401 | 801 s | 1 |
| Base run subtotal | | | 1,125,556 | | |

## Correction loop (iteration 1; resumed agents, delta = cumulative after loop minus base)

| agent | doc | model | total_tok (delta) | cumulative reported | wall | run# |
|---|---|---|---|---|---|---|
| A1 extractor | presentation | claude-sonnet-5-5 | 9,517 | 116,255 | 61 s | loop 1 |
| A2 enumerator | presentation | claude-sonnet-5-5 | 12,145 | 74,341 | 50 s | loop 1 |
| A3 forensics | presentation | claude-opus-5-5 | 44,429 | 211,034 | 300 s | loop 1 |
| A4 analyst | merged | claude-opus-5-5 | 84,193 | 337,986 | 392 s | loop 1 |
| A5 adversary | merged | claude-opus-5-5 | 108,004 | 368,405 | 462 s | loop 1 |
| Loop subtotal | | | 258,288 | | | |

Cost checks: A2 < A1 on both documents (70,217 < 88,093; 62,196 < 106,738). PASS.
Loop outcome: M1-M4 closed; N1 opened; loop cap reached, second iteration not run (operator away).

## Orchestrator session
- Fresh tokens: NOT FOUND (not exposed in session)
- Re-read tokens: NOT FOUND
- Re-read multiple: NOT FOUND
