# SESSION COST LEDGER — AVIENCE 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only where the harness
does not split input/output; in_tok/out_tok then read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~75m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 112663 | 7m42s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 157306 | 8m03s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 146916 | 9m42s | 2 |
