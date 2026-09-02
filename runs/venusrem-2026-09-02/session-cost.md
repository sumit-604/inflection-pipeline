# Session cost ledger — VENUSREM 2026-09-02 (Phase 1)

Per-stage token ledger. One row per subagent run. Stage 0 is orchestrator-inline
(no subagent metadata). Model/effort/tokens from each subagent's result metadata.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator-inline (opus) | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 148520 | 467s | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet-5 | default | n/a | n/a | 166659 | 690s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet-5 | default | n/a | n/a | 146503 | 461s | 2 |
| 2 | notes triple-pass (pass 3) | claude-sonnet-5 | default | n/a | n/a | 75230 | 184s | 3 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 132773 | 588s | 1 |
| 8 | promoter check | claude-sonnet-5 | default | n/a | n/a | 167854 | 690s | 1 |
| 8 | promoter check (FY25 AR follow-up) | claude-sonnet-5 | default | n/a | n/a | 241216 | 1188s | 2 |
