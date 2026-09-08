# SESSION COST — BORANA, run 2026-09-07 (Phase 1)

Per-stage token ledger. One line per subagent run, written and committed
with its own stage. Loop or retry runs get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 1 | Gate 0 scorecard | claude-sonnet-5 | default | 152183 | 10940 | 163123 | 8m40s | 1 |
| 2 | Notes triple-pass, pass 1 | claude-sonnet-5 | default | 193900 | 9895 | 203795 | 9m39s | 1 |
| 2 | Notes triple-pass, pass 2 | claude-sonnet-5 | default | 118500 | 6907 | 125407 | 7m22s | 2 |
| 2 | Notes triple-pass, pass 3 (consolidation) | claude-sonnet-5 | default | 108100 | 5089 | 113189 | 5m59s | 3 |
| 3 | AR backward deep dive | claude-sonnet-5 | default | 218400 | 11509 | 229909 | 12m60s | 1 |
| 5 | Concall analysis (NO-CONCALL MODE) | claude-sonnet-5 | default | 117200 | 6727 | 123927 | 8m36s | 1 |
| 4 | Business model decoder | claude-sonnet-5 | default | 141400 | 7921 | 149321 | 11m34s | 1 |
| 8 | Promoter check (web search) | claude-sonnet-5 | default | 190200 | 10484 | 200684 | 9m22s | 1 |
| 6 | Peer concall verification | claude-sonnet-5 | default | 150500 | 9160 | 159660 | 11m01s | 1 |
| 7 | Emerging moat scan (22 categories) | claude-sonnet-5 | default | 137100 | 8724 | 145824 | 8m48s | 1 |
| 9 | TAM SAM SOM (web search) | claude-sonnet-5 | default | 220800 | 10866 | 231666 | 17m59s | 1 |
| 12a | Verifier A numerical | claude-haiku-4-5 | default | 101800 | 3870 | 105670 | 2m18s | 1 |
| 12a | Verifier A numerical (coverage addendum) | claude-haiku-4-5 | default | 121500 | 4828 | 126328 | 3m38s | 2 |
| 12c | Verifier C framework (phase-1 scope) | claude-opus-4-8 | default | 103400 | 4920 | 108320 | 7m48s | 1 |
| 12d | Verifier D peer coverage | claude-sonnet-5 | default | 355800 | 11405 | 367205 | 6m44s | 1 |
