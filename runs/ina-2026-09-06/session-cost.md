# SESSION COST LEDGER — INA (Insolation Energy Ltd), run 2026-09-06

Per-stage token ledger. One line per subagent run; loops and retries get their
own line with a run counter. Written and committed with each stage, never
deferred to the end of the run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | orchestrator-inline (opus-5) | default | n/a | n/a | n/a | ~12m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 151,819 | 15m33s | 1 |
| 2a | notes pass 1 of 3 | claude-sonnet-5 | default | n/a | n/a | 212,865 | 14m14s | 1 |
| 2b | notes pass 2 of 3 | claude-sonnet-5 | default | n/a | n/a | 171,711 | 12m54s | 1 |
| 2c | notes pass 3 of 3 (consolidation) | claude-sonnet-5 | default | n/a | n/a | 78,204 | 4m42s | 1 |
| 3 | AR deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 239,778 | 15m43s | 1 |
| 3 | AR deep dive: append B03 block | claude-sonnet-5 | default | n/a | n/a | 305,046 | 4m41s | 2 |
| 5 | concall analysis (3 transcripts) | claude-sonnet-5 | default | n/a | n/a | 132,368 | 8m58s | 1 |
| 3 | AR deep dive: add monitorables[] | claude-sonnet-5 | default | n/a | n/a | 353,331 | 10m43s | 3 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 117,544 | 9m60s | 1 |
| 8 | promoter background check (web) | claude-sonnet-5 + web | default | n/a | n/a | 178,847 | 10m15s | 1 |
| 6 | peer concall verification (11) | claude-sonnet-5 | default | n/a | n/a | 327,257 | 10m57s | 1 |
| 7 | emerging moat 22-category scan | claude-sonnet-5 | default | n/a | n/a | 195,140 | 11m45s | 1 |
| 9 | TAM SAM SOM (web) | claude-sonnet-5 + web | default | n/a | n/a | 131,322 | 10m18s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 95,756 | 3m19s | 1 |
