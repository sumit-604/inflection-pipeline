# SESSION COST — ORCHPHARMA 2026-09-06 (Phase 1)

Per-stage token ledger. One line per subagent run, written and committed with
its own stage. Loops and retries each get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | opus-5 (orchestrator, inline) | default | n/a | n/a | n/a | n/a | 1 |
| 1 | gate 0 scorecard | sonnet-5 | default | n/a | n/a | 131,843 | 12m26s | 1 |
| 2 | notes triple-pass, pass 1 | sonnet-5 | default | n/a | n/a | 164,215 | 12m15s | 1 |
