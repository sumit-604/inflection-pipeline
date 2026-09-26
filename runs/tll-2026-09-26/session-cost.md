# SESSION COST LEDGER — TLL 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~95m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 123710 | 11m07s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 189099 | 9m06s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 132881 | 5m31s | 2 |
| 2 | notes triple-pass, pass 3 (consolidation) | claude-sonnet-5 | default | n/a | n/a | 72124 | 3m10s | 3 |
| 3 | AR deep dive | claude-sonnet-5 | default | n/a | n/a | 192393 | 10m09s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 101159 | 7m01s | 1 |
| 5 | concall analysis (NO-CONCALL MODE) | claude-sonnet-5 | default | n/a | n/a | 210031 | 7m19s | 1 |
| 8 | promoter check | claude-sonnet-5 | default | n/a | n/a | 152939 | 7m00s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 153600 | 5m08s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 126665 | 6m39s | 1 |
| 9 | TAM/SAM/SOM | claude-sonnet-5 | default | n/a | n/a | 117746 | 8m47s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 84923 | 2m57s | 1 |
| 12b | verifier B red flags | claude-opus-5-5 | default | n/a | n/a | 314564 | 10m01s | 1 |
| 12c | verifier C framework (phase 1 half) | claude-opus-5-5 | default | n/a | n/a | 123277 | 5m55s | 1 |
| 12d | verifier D peers | claude-sonnet-5 | default | n/a | n/a | 71122 | 2m53s | 1 |
| 13 | synthesis-lite (phase 1) | claude-opus-5-5 | default | n/a | n/a | 169582 | 6m26s | 1 |
| 1 | gate 0 scorecard (rework) | claude-sonnet-5 | default | n/a | n/a | 164494 | 8m19s | 2 |
| 5 | concall analysis, NO-CONCALL (rework) | claude-sonnet-5 | default | n/a | n/a | 160607 | 9m26s | 2 |
| 6 | peer concall verification (rework) | claude-sonnet-5 | default | n/a | n/a | 96407 | 6m15s | 2 |
| 8 | promoter check (rework) | claude-sonnet-5 | default | n/a | n/a | 141306 | 6m52s | 2 |
| 7 | emerging moat scan (rework) | claude-sonnet-5 | default | n/a | n/a | 127724 | 7m15s | 2 |
| 12a | verifier A numerical (re-run) | claude-haiku-4-5 | default | n/a | n/a | 157313 | 4m38s | 2 |
| 12b | verifier B red flags (re-run) | claude-opus-5-5 | default | n/a | n/a | 272746 | 9m40s | 2 |
| 12c | verifier C framework, phase 1 half (re-run) | claude-opus-5-5 | default | n/a | n/a | 144445 | 6m27s | 2 |
| 12d | verifier D peers (re-run) | claude-sonnet-5 | default | n/a | n/a | 93350 | 11m57s | 2 |
