# SESSION COST LEDGER — QMSMEDI 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~75m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 127333 | 11m10s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 168768 | 12m24s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 104171 | 7m11s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 82121 | 4m01s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 161862 | 10m12s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 96940 | 5m49s | 1 |
| 5 | concall analysis (Q2 FY26, Q4 FY26, Q1 FY27) | claude-sonnet-5 | default | n/a | n/a | 166615 | 6m20s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 168260 | 7m41s | 1 |
| 6 | peer concall verification (INDGN, ENTERO, POLYMED) | claude-sonnet-5 | default | n/a | n/a | 326189 | 6m04s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 153151 | 6m47s | 1 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | n/a | n/a | 123927 | 9m17s | 1 |
| 12a | verifier A numerical (21 numbers, B01 only; superseded on coverage) | claude-haiku-4-5 | default | n/a | n/a | 87284 | 3m41s | 1 |
| 12b | verifier B red flags | claude-opus-5-5 | default | n/a | n/a | 437736 | 10m29s | 1 |
| 12c | verifier C framework (phase-1 half) | claude-opus-5-5 | default | n/a | n/a | 108186 | 4m58s | 1 |
| 12d | verifier D peers | claude-sonnet-5 | default | n/a | n/a | 74801 | 2m28s | 1 |
| 12a | verifier A numerical (coverage addendum; governs) | claude-haiku-4-5 | default | n/a | n/a | 148793 | 2m49s | 2 |
| 13 | synthesis-lite (phase 1) | claude-opus-5-5 | default | n/a | n/a | 205889 | 9m50s | 1 |
