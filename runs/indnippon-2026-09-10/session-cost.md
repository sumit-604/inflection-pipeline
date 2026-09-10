# SESSION COST LEDGER — INDNIPPON 2026-09-10

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | input validation + freshness pair check | orchestrator-inline | n/a | n/a | n/a | n/a | n/a | 1 |
| 2 | notes triple-pass (pass 1 extraction) | claude-sonnet-5 | default | - | - | 152316 | 471s | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | - | - | 146812 | 956s | 1 |
| 2 | notes triple-pass (pass 2 gap-hunt) | claude-sonnet-5 | default | - | - | 135261 | 623s | 2 |
| 2 | notes triple-pass (pass 3 consolidation + B02) | claude-sonnet-5 | default | - | - | 82693 | 199s | 3 |
