# SESSION COST LEDGER — QUALITEK 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~60m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 127050 | 8m43s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 196032 | 8m52s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 111718 | 9m06s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 102220 | 5m42s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 231648 | 12m51s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 111369 | 5m59s | 1 |
| 5 | concall analysis (NO-CONCALL MODE, MD&A/decks FY24-FY26) | claude-sonnet-5 | default | n/a | n/a | 178710 | 7m45s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 156366 | 8m15s | 1 |
| 6 | peer concall verification (VIMTALABS, METROPOLIS, KRSNAA) | claude-sonnet-5 | default | n/a | n/a | 343516 | 4m25s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 129655 | 6m43s | 1 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | n/a | n/a | 117596 | 7m57s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 93966 | 3m43s | 1 |
| 12b | verifier B red flags (no-concall mode) | claude-opus-5-5 | default | n/a | n/a | 221189 | 8m36s | 1 |
| 12c | verifier C framework (phase-1 half) | claude-opus-5-5 | default | n/a | n/a | 113444 | 4m25s | 1 |
| 12d | verifier D peers | claude-sonnet-5 | default | n/a | n/a | 353830 | 4m15s | 1 |
| 5 | concall analysis rework (cycle 1, B12b findings) | claude-sonnet-5 | default | n/a | n/a | 189126 | 9m57s | 2 |
| 6 | peer concall verification rework (cycle 1, B12b/B12d findings) | claude-sonnet-5 | default | n/a | n/a | 132266 | 5m59s | 2 |
| 12a | verifier A numerical (cycle 2) | claude-haiku-4-5 | default | n/a | n/a | 114858 | 4m16s | 2 |
| 12b | verifier B red flags (cycle 2, no-concall mode) | claude-opus-5-5 | default | n/a | n/a | 299202 | 11m14s | 2 |
| 12d | verifier D peers (cycle 2) | claude-sonnet-5 | default | n/a | n/a | 82620 | 2m15s | 2 |
| 13 | synthesis-lite (phase 1) | claude-opus-5-5 | default | n/a | n/a | 222317 | 8m47s | 1 |
