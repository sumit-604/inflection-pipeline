# SESSION COST LEDGER — AWFIS 2026-09-19 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~75m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 146267 | 12m34s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 261064 | 13m21s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 161682 | 7m53s | 2 |
