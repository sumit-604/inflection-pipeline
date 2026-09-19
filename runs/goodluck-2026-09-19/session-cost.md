# Session cost ledger — GOODLUCK 2026-09-19 (Phase 1, Step-1 intake)

Per-stage token ledger. One row per subagent run. Stage 0 is orchestrator-inline
(no subagent metadata). Tokens and wall time from each subagent's result metadata.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator-inline (claude-opus-5) | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 108915 | 498s | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet-5 | default | n/a | n/a | 153199 | 494s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet-5 | default | n/a | n/a | 182497 | 496s | 2 |
| 2 | notes triple-pass (pass 3) | claude-sonnet-5 | default | n/a | n/a | 108239 | 365s | 3 |
| 3 | AR deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 240280 | 696s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 167333 | 650s | 1 |
| 5 | concall analysis | claude-sonnet-5 | default | n/a | n/a | 185929 | 444s | 1 |
| 8 | promoter check | claude-sonnet-5 | default | n/a | n/a | 195455 | 634s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 223894 | 355s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 179781 | 565s | 1 |
| 9 | TAM/SAM/SOM sizing | claude-sonnet-5 | default | n/a | n/a | 174896 | 865s | 1 |
