# SESSION COST LEDGER — DPABHUSHAN 2026-09-19 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~70m | 1 |
| 1 | gate 0 scorecard (layout text, superseded) | claude-sonnet-5 | default | n/a | n/a | 151657 | 11m39s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 192948 | 11m30s | 1 |
| 1 | gate 0 scorecard (table text, governs) | claude-sonnet-5 | default | n/a | n/a | 137514 | 10m07s | 2 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 181911 | 6m58s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 101923 | 4m00s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 309824 | 12m46s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 181924 | 7m49s | 1 |
| 5 | concall analysis (Q3 FY26-Q1 FY27) | claude-sonnet-5 | default | n/a | n/a | 177995 | 7m32s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 207740 | 10m14s | 1 |
| 6 | peer concall verification (RBZ mislabeled as MOTISONS, superseded) | claude-sonnet-5 | default | n/a | n/a | 228811 | 8m17s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 149572 | 7m57s | 1 |
