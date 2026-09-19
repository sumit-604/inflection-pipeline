# Session cost ledger — GOODLUCK 2026-09-19 (Phase 1, Step-1 intake)

Per-stage token ledger. One row per subagent run. Stage 0 is orchestrator-inline
(no subagent metadata). Tokens and wall time from each subagent's result metadata.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator-inline (claude-opus-5) | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 108915 | 498s | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet-5 | default | n/a | n/a | 153199 | 494s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet-5 | default | n/a | n/a | 182497 | 496s | 2 |
