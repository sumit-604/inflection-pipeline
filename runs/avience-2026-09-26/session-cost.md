# SESSION COST LEDGER — AVIENCE 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only where the harness
does not split input/output; in_tok/out_tok then read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~75m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 112663 | 7m42s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 157306 | 8m03s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 146916 | 9m42s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 115564 | 7m34s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 185012 | 10m59s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 159733 | 5m58s | 1 |
| 5 | concall analysis (no-concall mode, 1 transcript) | claude-sonnet-5 | default | n/a | n/a | 128005 | 6m27s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 166102 | 8m20s | 1 |
| 6 | peer concall verification (QLINE, MOLBIO, TARSONS; 6 transcripts) | claude-sonnet-5 | default | n/a | n/a | 211783 | 4m32s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 195340 | 8m19s | 1 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | n/a | n/a | 154252 | 10m38s | 1 |
