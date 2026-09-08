# SESSION COST — FRATELLI, run 2026-09-07

Per-stage token ledger. One line per subagent run, written and committed with
its own stage. Phase 1 (evidence) only; phases 2 and 3 append their own lines.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + freshness pair check | orchestrator inline | n/a | n/a | n/a | n/a | n/a | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 179264 | 9m45s | 1 |
| 1 | Gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 119552 | 11m52s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 133505 | 9m45s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 112538 | 6m21s | 3 |
| 3 | AR deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 234959 | 15m09s | 1 |
| 8 | promoter background check | claude-sonnet-5 | default | n/a | n/a | 173554 | 8m05s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 141903 | 9m07s | 1 |
| 5 | concall analysis (5 transcripts) | claude-sonnet-5 | default | n/a | n/a | 215133 | 10m42s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 258306 | 7m37s | 1 |
