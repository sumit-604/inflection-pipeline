# SESSION COST — ORCHPHARMA 2026-09-06 (Phase 1)

Per-stage token ledger. One line per subagent run, written and committed with
its own stage. Loops and retries each get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | opus-5 (orchestrator, inline) | default | n/a | n/a | n/a | n/a | 1 |
| 1 | gate 0 scorecard | sonnet-5 | default | n/a | n/a | 131,843 | 12m26s | 1 |
| 2 | notes triple-pass, pass 1 | sonnet-5 | default | n/a | n/a | 164,215 | 12m15s | 1 |
| 5 | concall analysis (4 calls) | sonnet-5 | default | n/a | n/a | 149,182 | 9m41s | 1 |
| 8 | promoter check (web) | sonnet-5 | default | n/a | n/a | 161,595 | 12m03s | 1 |
| 6 | peer concall verification | sonnet-5 | default | n/a | n/a | 141,996 | 6m58s | 1 |
| 4 | business model decoder | sonnet-5 | default | n/a | n/a | 145,220 | 10m17s | 1 |
| 7 | emerging moat scan | sonnet-5 | default | n/a | n/a | 152,541 | 11m14s | 1 |
| 9 | TAM SAM SOM (web) | sonnet-5 | default | n/a | n/a | 180,888 | 15m53s | 1 |
| 2 | notes triple-pass, pass 2 | sonnet-5 | default | n/a | n/a | 182,321 | 7m33s | 1 |
| 3 | AR backward deep dive | sonnet-5 | default | n/a | n/a | 287,774 | 11m31s | 1 |
| 2 | notes triple-pass, pass 3 | sonnet-5 | default | n/a | n/a | n/a | n/a | 1 |
| 12d | verifier D peer coverage | sonnet-5 | default | n/a | n/a | 122,156 | 5m56s | 1 |
| 12c | verifier C framework (phase 1 scope) | opus-4.8 | default | n/a | n/a | n/a | n/a | 1 |
| 12a | verifier A numerical | haiku-4.5 | default | n/a | n/a | 116,842 | 2m53s | 1 |
| 12a | verifier A numerical, re-run with coverage addendum | haiku-4.5 | default | n/a | n/a | 117,347 | 6m13s | 2 |
