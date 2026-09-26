# SESSION COST LEDGER — TLL 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~95m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 123710 | 11m07s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 189099 | 9m06s | 1 |
