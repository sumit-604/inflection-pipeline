# Session cost ledger — KABRAEXTRU 2026-09-05 (Phase 1)

Per-stage token ledger. One row per subagent run. Stage 0 is orchestrator-inline
(no subagent metadata). Model/effort/tokens from each subagent's result metadata.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator-inline (fable) | n/a | n/a | n/a | n/a | n/a | 1 |
| 8 | promoter check | claude-sonnet-5 | default | n/a | n/a | 178598 | 830s | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet-5 | default | n/a | n/a | 229345 | 791s | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 171467 | 1031s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet-5 | default | n/a | n/a | 180031 | 823s | 2 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 243831 | 973s | 1 |
| 2 | notes triple-pass (pass 3 + consolidation) | claude-sonnet-5 | default | n/a | n/a | 116854 | 457s | 3 |
| 3 | AR deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 305649 | 730s | 1 |
| 5 | concall (NO-CONCALL: AR guidance vs delivery) | claude-sonnet-5 | default | n/a | n/a | 185340 | 792s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 172321 | 955s | 1 |
| 6 | peer concall verification (FAILED: API 429 session rate limit, aborted mid-read, no report written) | claude-sonnet-5 | default | n/a | n/a | n/a | n/a | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 168103 | 553s | 2 |
| 12c | verifier C framework (phase-1 scope) | claude-opus-4-8 | default | n/a | n/a | 130352 | 562s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 185059 | 475s | 1 |
| 9 | TAM/SAM/SOM sizing | claude-sonnet-5 | default | n/a | n/a | 193951 | 1197s | 1 |
| 12b | verifier B red-flags (NO-CONCALL: AR sources) | claude-opus-4-8 | default | n/a | n/a | 362059 | 944s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 120887 | 263s | 1 |
