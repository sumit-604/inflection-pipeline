# SESSION COST LEDGER — CYIENTDLM 2026-09-06 (PHASE 1)

Per-stage token ledger, one line per subagent run, written at the moment each
stage returns and committed with that stage.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit + PDF pre-extraction | orchestrator-inline | n/a | n/a | n/a | n/a | n/a | 1 |
| 2 | notes triple-pass, pass 1 of 3 | claude-sonnet-5 | default | n/a | n/a | 154100 | 8m11s | 1 |
| 1 | Gate 0 quantitative scorecard | claude-sonnet-5 | default | n/a | n/a | 121289 | 10m49s | 1 |
| 2 | notes triple-pass, pass 2 of 3 | claude-sonnet-5 | default | n/a | n/a | 119743 | 7m24s | 2 |
| 8 | promoter background check | claude-sonnet-5 | default | n/a | n/a | 164995 | 7m55s | 1 |
| 5 | concall analysis, main company | claude-sonnet-5 | default | n/a | n/a | 156702 | 9m14s | 1 |
| 2 | notes triple-pass, pass 3 of 3 (consolidation, emits B02) | claude-sonnet-5 | default | n/a | n/a | 68098 | 3m17s | 3 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 317321 | 6m33s | 1 |
| 7 | emerging moat 22-category scan | claude-sonnet-5 | default | n/a | n/a | 189274 | 8m32s | 1 |
| 3 | AR backward deep dive, 8 phases | claude-sonnet-5 | default | n/a | n/a | 283226 | 12m34s | 1 |
