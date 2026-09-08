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
| 7 | emerging moat 22-category scan | claude-sonnet-5 | default | n/a | n/a | 184820 | 11m44s | 1 |
| 9 | TAM SAM SOM market sizing | claude-sonnet-5 | default | n/a | n/a | 138438 | 13m36s | 1 |
| 12a | verifier A numerical (run 1, severity re-check ordered) | claude-haiku-4-5 | default | n/a | n/a | 88559 | 3m46s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 107025 | 7m26s | 1 |
| 12c | verifier C framework (phase 1 scope) | claude-opus-4-8 | default | n/a | n/a | 107398 | 8m29s | 1 |
| 12a | verifier A numerical (run 2, re-decided + widened) | claude-haiku-4-5 | default | n/a | n/a | 85402 | 5m06s | 2 |
| 12b | verifier B concall red flags | claude-opus-4-8 | default | n/a | n/a | 255696 | 17m54s | 1 |
| 13 | synthesis-lite (phase 1, three files) | claude-opus-5 | default | n/a | n/a | 132686 | 6m49s | 1 |
| 5 | concall analysis (5 transcripts) | claude-sonnet-5 | default | n/a | n/a | 310453 | 13m46s | 2 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 202894 | 15m09s | 2 |
| 12d | verifier D peer coverage (re-measure of stage 6 run 2) | claude-sonnet-5 | default | n/a | n/a | 140532 | 10m11s | 2 |
| 12b | verifier B concall red flags (re-measure) | claude-opus-4-8 | default | n/a | n/a | 345247 | 19m34s | 2 |
