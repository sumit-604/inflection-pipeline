# SESSION COST LEDGER — DPABHUSHAN 2026-09-19 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~70m | 1 |
| 1 | gate 0 scorecard (layout text, superseded) | claude-sonnet-5 | default | n/a | n/a | 151657 | 11m39s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 192948 | 11m30s | 1 |
| 1 | gate 0 scorecard (table text, governs) | claude-sonnet-5 | default | n/a | n/a | 137514 | 10m07s | 2 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 181911 | 6m58s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 101923 | 4m00s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 309824 | 12m46s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 181924 | 7m49s | 1 |
| 5 | concall analysis (Q3 FY26-Q1 FY27) | claude-sonnet-5 | default | n/a | n/a | 177995 | 7m32s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 207740 | 10m14s | 1 |
| 6 | peer concall verification (RBZ mislabeled as MOTISONS, superseded) | claude-sonnet-5 | default | n/a | n/a | 228811 | 8m17s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 149572 | 7m57s | 1 |
| 6 | peer concall verification (SENCO, PNGJL, KALYANKJIL; governs) | claude-sonnet-5 | default | n/a | n/a | 375766 | 6m12s | 2 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | n/a | n/a | 183592 | 12m15s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 103851 | 2m39s | 1 |
| 12b | verifier B red flags | claude-opus-5 | default | n/a | n/a | 299717 | 10m28s | 1 |
| 12c | verifier C framework (phase-1 half) | claude-opus-5 | default | n/a | n/a | 124077 | 4m56s | 1 |
| 12d | verifier D peers | claude-sonnet-5 | default | n/a | n/a | 93143 | 2m44s | 1 |
| 13 | synthesis-lite (phase 1) | claude-opus-5 | default | n/a | n/a | 224835 | 8m44s | 1 |
| 9b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 184203 | 10m00s | 1 |

## CLOSE-OUT SUMMARY

Run total (sum of ledger rows with token counts): 3,611,003 tokens.

(a) TOP FIVE BY TOKENS (retries summed per stage)
| rank | stage | total_tok | share |
|---|---|---|---|
| 1 | 6 peer concall verification (2 runs; run 1 on mislabeled RBZ files) | 604,577 | 16.7% |
| 2 | 2 notes triple-pass (3 runs) | 476,782 | 13.2% |
| 3 | 3 AR backward deep dive | 309,824 | 8.6% |
| 4 | 12b verifier B red flags | 299,717 | 8.3% |
| 5 | 1 gate 0 scorecard (2 runs; run 1 on interleaved text) | 289,171 | 8.0% |

Avoidable spend: stage 6 run 1 (228,811) and stage 1 run 1 (151,657) = 380,468 tokens (10.5%), both caused by intake defects (wrong peer scrip code; -layout extraction of AR spreads).

(b) DOWNSHIFT FAILURES
- DOWNSHIFT FAILURE: stage 0 (input validation ran inline in the Opus orchestrator session, as run-pipeline step 1 directs "do this yourself"; no haiku stage-0 agent exists, so the downshift cannot take on this path). Verifier A ran on haiku as routed.

(c) COST SPIKES
- none (no prior DPABHUSHAN run ledger exists).

(d) OPERATOR SNAPSHOT
- Operator: run /cost and /usage now and paste the cache hit ratio and loop totals under an "Operator snapshot" heading here.
