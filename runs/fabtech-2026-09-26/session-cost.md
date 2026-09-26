# SESSION COST LEDGER — FABTECH 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation (incl. AR OCR) | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~90m | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 216527 | 5m47s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 83532 | 2m39s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 87339 | 3m44s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 267827 | 11m25s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 131986 | 7m06s | 1 |
| 5 | concall analysis (Q3 FY26-Q1 FY27) | claude-sonnet-5 | default | n/a | n/a | 171309 | 6m19s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 210579 | 11m01s | 1 |
| 6 | peer concall verification (SETL, HLEGLAS, PRAJIND) | claude-sonnet-5 | default | n/a | n/a | 117014 | 4m09s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 198452 | 7m09s | 1 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | n/a | n/a | 145618 | 8m31s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 102635 | 3m56s | 1 |
| 12b | verifier B red flags | claude-opus-5-5 | default | n/a | n/a | 299026 | 10m03s | 1 |
| 12c | verifier C framework (phase-1 half) | claude-opus-5-5 | default | n/a | n/a | 143272 | 7m38s | 1 |
| 12d | verifier D peers | claude-sonnet-5 | default | n/a | n/a | 127233 | 2m53s | 1 |
| 12a | verifier A numerical (re-invoked with severity addendum; incremental tokens) | claude-haiku-4-5 | default | n/a | n/a | 46121 | 4m19s | 2 |
