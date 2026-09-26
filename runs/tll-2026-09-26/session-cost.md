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
