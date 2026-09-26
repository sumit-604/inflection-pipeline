# SESSION COST LEDGER — TLL 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~95m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 123710 | 11m07s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 189099 | 9m06s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 132881 | 5m31s | 2 |
| 2 | notes triple-pass, pass 3 (consolidation) | claude-sonnet-5 | default | n/a | n/a | 72124 | 3m10s | 3 |
| 3 | AR deep dive | claude-sonnet-5 | default | n/a | n/a | 192393 | 10m09s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 101159 | 7m01s | 1 |
| 5 | concall analysis (NO-CONCALL MODE) | claude-sonnet-5 | default | n/a | n/a | 210031 | 7m19s | 1 |
| 8 | promoter check | claude-sonnet-5 | default | n/a | n/a | 152939 | 7m00s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 153600 | 5m08s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 126665 | 6m39s | 1 |
| 9 | TAM/SAM/SOM | claude-sonnet-5 | default | n/a | n/a | 117746 | 8m47s | 1 |
