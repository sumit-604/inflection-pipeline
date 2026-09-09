# SESSION COST LEDGER — TOTEM 2026-09-09 (phase 1)

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | input validation + corpus repair | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~40m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 216482 | 11m49s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 177757 | 7m39s | 1 |
| 1 | gate 0 scorecard (peer-data correction) | claude-sonnet-5 | default | n/a | n/a | 85032 | 5m52s | 2 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 171774 | 7m56s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 81282 | 3m58s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 266678 | 15m55s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 141064 | 8m14s | 1 |
| 5 | management/guidance analysis (no-concall mode) | claude-sonnet-5 | default | n/a | n/a | 189078 | 7m30s | 1 |
| 8 | promoter background check (web) | claude-sonnet-5 | default | n/a | n/a | 200094 | 12m51s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 236781 | 6m58s | 1 |
| 7 | emerging moat scan (22 categories) | claude-sonnet-5 | default | n/a | n/a | 136343 | 10m26s | 1 |
| 9 | TAM SAM SOM market sizing (web) | claude-sonnet-5 | default | n/a | n/a | 151834 | 13m21s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 95540 | 3m45s | 1 |
| 12b | verifier B red flags | claude-opus-4-8 | default | n/a | n/a | 287138 | 15m43s | 1 |
| 12c | verifier C framework (phase-1 scope) | claude-opus-4-8 | default | n/a | n/a | 126016 | 8m20s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 208088 | 6m24s | 1 |
| 1 | gate 0 scorecard (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 120757 | 8m26s | 3 |
| 5 | management/guidance analysis (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 233523 | 12m34s | 2 |
| 6 | peer concall verification (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 195260 | 7m36s | 2 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 114957 | 5m11s | 2 |
| 12b | verifier B red flags | claude-opus-4-8 | default | n/a | n/a | 391615 | 18m45s | 2 |
| 12c | verifier C framework (phase-1 scope) | claude-opus-4-8 | default | n/a | n/a | 139778 | 9m06s | 2 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 216060 | 9m25s | 2 |
| 5 | management/guidance analysis (audit cycle 2) | claude-sonnet-5 | default | n/a | n/a | 176881 | 10m13s | 3 |
| 6 | peer concall verification (audit cycle 2) | claude-sonnet-5 | default | n/a | n/a | 223393 | 7m28s | 3 |
| 12a | verifier A numerical (final) | claude-haiku-4-5 | default | n/a | n/a | 109706 | 5m57s | 3 |
| 12b | verifier B red flags (final) | claude-opus-4-8 | default | n/a | n/a | 395319 | 20m55s | 3 |
| 12d | verifier D peer coverage (final) | claude-sonnet-5 | default | n/a | n/a | 190875 | 9m40s | 3 |
