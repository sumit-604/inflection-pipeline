# Session cost ledger — KABRAEXTRU 2026-09-05 (Phase 1)

Per-stage token ledger. One row per subagent run. Stage 0 is orchestrator-inline
(no subagent metadata). Model/effort/tokens from each subagent's result metadata.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator-inline (fable) | n/a | n/a | n/a | n/a | n/a | 1 |
| 8 | promoter check | claude-sonnet-5 | default | n/a | n/a | 178598 | 830s | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet-5 | default | n/a | n/a | 229345 | 791s | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 171467 | 1031s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet-5 | default | n/a | n/a | 180031 | 823s | 2 |
