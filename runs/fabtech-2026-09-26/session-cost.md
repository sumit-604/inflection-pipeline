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
| 13 | synthesis-lite (phase 1) | claude-opus-5-5 | default | n/a | n/a | 212616 | 9m11s | 1 |
| 9b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 161841 | 5m51s | 1 |
| 9b | Halt 1 dossier re-run (mechanical check: sign-off marker em-dash; incremental tokens) | claude-sonnet-5 | default | n/a | n/a | 47715 | 3m06s | 2 |

## CLOSE-OUT SUMMARY

Run total (sum of ledger rows with token counts): 2,889,811 tokens.

(a) TOP FIVE BY TOKENS (retries summed per stage)
| rank | stage | total_tok | share |
|---|---|---|---|
| 1 | 2 notes triple-pass (3 runs) | 387,398 | 13.4% |
| 2 | 12b verifier B red flags | 299,026 | 10.3% |
| 3 | 3 AR backward deep dive | 267,827 | 9.3% |
| 4 | 13 synthesis-lite | 212,616 | 7.4% |
| 5 | 8 promoter check (web) | 210,579 | 7.3% |

Avoidable spend: verifier A run 2 (46,121) caused by the verifier's own 10x lakh-to-crore conversion; 09b run 2 (47,715) caused by an em-dash in the sign-off marker. 93,836 tokens (3.2%).

(b) DOWNSHIFT FAILURES
- DOWNSHIFT FAILURE: stage 0 (input validation ran inline in the Opus orchestrator session, as run-pipeline step 1 directs "do this yourself"; no haiku stage-0 agent exists). Structural, as in DPABHUSHAN 2026-09-19. Verifier A ran on haiku as routed.

(c) COST SPIKES
- none (no prior FABTECH run ledger exists).

(d) OPERATOR SNAPSHOT
- Operator: run /cost and /usage now and paste the cache hit ratio and loop totals under an "Operator snapshot" heading here.
