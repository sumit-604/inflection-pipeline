# SESSION COST — BALUFORGE 2026-09-06 (Phase 1)

Per-stage token ledger, written as each stage returns.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus extraction | orchestrator-inline | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | Gate 0 scorecard | claude-sonnet-5 | default | n/r | n/r | 130,317 | 11m37s | 1 |
| 2 | Notes triple-pass, pass 1 | claude-sonnet-5 | default | n/r | n/r | 183,568 | 8m51s | 1 |

n/r = the subagent result reported a single total-token figure, not an input/output split.

