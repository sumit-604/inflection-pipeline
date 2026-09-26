# SESSION COST LEDGER — QUALITEK 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~60m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 127050 | 8m43s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 196032 | 8m52s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 111718 | 9m06s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 102220 | 5m42s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 231648 | 12m51s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 111369 | 5m59s | 1 |
| 5 | concall analysis (NO-CONCALL MODE, MD&A/decks FY24-FY26) | claude-sonnet-5 | default | n/a | n/a | 178710 | 7m45s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 156366 | 8m15s | 1 |
