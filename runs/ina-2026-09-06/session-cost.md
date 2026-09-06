# SESSION COST LEDGER — INA (Insolation Energy Ltd), run 2026-09-06

Per-stage token ledger. One line per subagent run; loops and retries get their
own line with a run counter. Written and committed with each stage, never
deferred to the end of the run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | orchestrator-inline (opus-5) | default | n/a | n/a | n/a | ~12m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 151,819 | 15m33s | 1 |
| 2a | notes pass 1 of 3 | claude-sonnet-5 | default | n/a | n/a | 212,865 | 14m14s | 1 |
