# SESSION COST — BALUFORGE 2026-09-06 (Phase 1)

Per-stage token ledger, written as each stage returns.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus extraction | orchestrator-inline | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | Gate 0 scorecard | claude-sonnet-5 | default | n/r | n/r | 130,317 | 11m37s | 1 |
| 2 | Notes triple-pass, pass 1 | claude-sonnet-5 | default | n/r | n/r | 183,568 | 8m51s | 1 |
| 2 | Notes triple-pass, pass 2 | claude-sonnet-5 | default | n/r | n/r | 141,426 | 9m44s | 2 |
| 2 | Notes triple-pass, pass 3 + consolidation | claude-sonnet-5 | default | n/r | n/r | 82,839 | 3m47s | 3 |
| 3 | AR deep dive | claude-sonnet-5 | default | n/r | n/r | 213,267 | 10m02s | 1 |
| 4 | Business model decoder | claude-sonnet-5 | default | n/r | n/r | 153,006 | 10m38s | 1 |
| 5 | Concall analysis (NO-CONCALL MODE) | claude-sonnet-5 | default | n/r | n/r | 182,796 | 8m59s | 1 |
| 6 | Peer concall verification | claude-sonnet-5 | default | n/r | n/r | 301,616 | 6m32s | 1 |
| 8 | Promoter background check | claude-sonnet-5 | default | n/r | n/r | 132,378 | 10m00s | 1 |

n/r = the subagent result reported a single total-token figure, not an input/output split.

