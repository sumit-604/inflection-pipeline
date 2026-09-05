# VISAKAIND 2026-09-05 — Phase 1 session cost ledger

Per-stage token ledger. One row per subagent run. Token counts come from the
subagent result metadata where the harness reports them; "n/a" where it does
not. Stage 0 ran inline in the orchestrator session (no subagent).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | stage-00-inputs (inline) | orchestrator | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | stage-02-notes (pass 1) | sonnet | n/a | n/a | n/a | 217786 | 7m48s | 1 |
| 2 | stage-02-notes (pass 2) | sonnet | n/a | n/a | n/a | 186770 | 7m37s | 2 |
| 3 | stage-01-gate0 | sonnet | n/a | n/a | n/a | 184608 | 18m14s | 1 |
