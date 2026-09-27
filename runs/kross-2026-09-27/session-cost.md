# SESSION COST LEDGER — KROSS 2026-09-27 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~40m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 111540 | 7m22s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 133955 | 5m57s | 1 |
| 1 | gate 0 scorecard (peer rescore, resumed) | claude-sonnet-5 | default | n/a | n/a | 42469 | 4m02s | 2 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 161252 | 4m18s | 2 |
| 2 | notes triple-pass, pass 3 (consolidation) | claude-sonnet-5 | default | n/a | n/a | 69933 | 4m01s | 3 |
| 3 | AR deep dive | claude-sonnet-5 | default | n/a | n/a | 225702 | 11m13s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 133964 | 6m34s | 1 |
| 5 | concall analysis | claude-sonnet-5 | default | n/a | n/a | 145141 | 6m53s | 1 |
| 8 | promoter check | claude-sonnet-5 | default | n/a | n/a | 191619 | 7m00s | 1 |
| 4 | business model decoder (anchor fix, resumed) | claude-sonnet-5 | default | n/a | n/a | 56565 | ~4m | 2 |
| 8 | promoter check (anchor + DII fix, resumed) | claude-sonnet-5 | default | n/a | n/a | 86149 | ~9m | 2 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 187195 | 5m33s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 122699 | 6m01s | 1 |
| 9 | TAM/SAM/SOM | claude-sonnet-5 | default | n/a | n/a | 167602 | 9m56s | 1 |
