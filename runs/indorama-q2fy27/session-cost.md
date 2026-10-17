# Session cost: INDORAMA Q2 FY27 (/run-quarterly, 2026-10-17)

DOCUMENT REVIEW summary row:
ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
INDORAMA | 2026-10-17 | results + pressrelease (presentation) + capex (results) | 12 + 3 + 1 = 16 | 14,052 (56,206 fulltext chars / 4; results 11,066, pressrelease 2,220, capex 766) | 1,811,269 | 1

## Per-agent ledger (base run)
| agent | doc | model | total_tok | wall | run# |
|---|---|---|---|---|---|
| A1 extractor | results | claude-sonnet-5-5 | 101,148 | 378 s | 1 (text layer garbled; superseded) |
| A1 extractor | results | claude-sonnet-5-5 | 164,806 | 253 s | 2 (mechanical re-run, scan branch; resumed context) |
| A1 extractor | pressrelease | claude-sonnet-5-5 | 51,640 | 177 s | 1 |
| A1 extractor | capex | claude-sonnet-5-5 | 42,484 | 51 s | 1 |
| A2 enumerator | pressrelease | claude-sonnet-5-5 | 36,974 | 38 s | 1 |
| A2 enumerator | capex | claude-sonnet-5-5 | 31,241 | 26 s | 1 |
| A2 enumerator | results | claude-sonnet-5-5 | 53,057 | 68 s | 1 |
| A3 forensics | pressrelease | claude-opus-5-5 | 60,555 | 194 s | 1 |
| A3 forensics | capex | claude-opus-5-5 | 45,793 | 128 s | 1 |
| A3 forensics | results | claude-opus-5-5 | 145,976 | 364 s | 1 |
| A4 analyst | merged | claude-opus-5-5 | 231,866 | 706 s | 1 |
| A5 adversary | merged | claude-opus-5-5 | 223,553 | 792 s | 1 |
Base run subtotal: 1,189,093

## Correction loop rows (iteration 1 of cap 1)
| agent | model | total_tok | wall | run# |
|---|---|---|---|---|
| A4 analyst (loop 1 fixes, resumed) | claude-opus-5-5 | 306,123 | 412 s | loop 1 |
| A5 adversary (loop 1 re-audit, resumed) | claude-opus-5-5 | 316,053 | 361 s | loop 1 |
Loop subtotal: 622,176

total_run_tok: 1,811,269 (base 1,189,093 + loop 622,176). Orchestrator session tokens not included.
Note: resumed-agent rows are the harness subagent_tokens figure for that invocation, which re-reads the agent's earlier context.
Cost check: every A2 below its A1. No A2-A5 agent read inputs/ (each reported so).
Status at close: A5 INCOMPLETE after loop 1 (F5, M6 open); second iteration awaits operator ruling.
