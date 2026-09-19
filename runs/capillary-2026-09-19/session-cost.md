# SESSION COST LEDGER — CAPILLARY 2026-09-19 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~70m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 132485 | 11m58s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 223637 | 10m17s | 1 |
| 1 | gate 0 scorecard (rescore with peer Data_Sheets; orchestrator omitted them in run 1) | claude-sonnet-5 | default | n/a | n/a | 173165 | 3m29s | 2 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 110157 | 8m25s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 76439 | 3m20s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 212500 | 14m45s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 122636 | 7m29s | 1 |
| 5 | concall analysis (3 transcripts) | claude-sonnet-5 | default | n/a | n/a | 171704 | 8m32s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 232448 | 10m03s | 1 |
