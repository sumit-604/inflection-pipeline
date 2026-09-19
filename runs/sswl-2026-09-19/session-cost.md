# SESSION COST LEDGER — SSWL 2026-09-19 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~90m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 139227 | 8m16s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 214498 | 8m29s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 157871 | 6m24s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 123355 | 5m53s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 271183 | 9m21s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 198311 | 9m22s | 1 |
| 5 | concall analysis (main) | claude-sonnet-5 | default | n/a | n/a | 170434 | 7m00s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 193917 | 7m51s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 314975 | 6m21s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 178074 | 9m19s | 1 |
