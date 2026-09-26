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
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 93666 | 3m42s | 1 |
| 12b | verifier B red flags (no-concall mode) | claude-opus-5-5 | default | n/a | n/a | 160700 | 6m57s | 1 |
| 12c | verifier C framework (phase-1 half) | claude-opus-5-5 | default | n/a | n/a | 120211 | 4m47s | 1 |
| 12d | verifier D peers | claude-sonnet-5 | default | n/a | n/a | 136506 | 4m18s | 1 |
| 13 | synthesis-lite (phase 1) | claude-opus-5-5 | default | n/a | n/a | 156520 | 4m50s | 1 |
| 9b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 134033 | 5m35s | 1 |

## CLOSE-OUT SUMMARY

Run total (sum of ledger rows with token counts): 2,534,312 tokens.

(a) TOP FIVE BY TOKENS (retries summed per stage)
| rank | stage | total_tok | share |
|---|---|---|---|
| 1 | 2 notes triple-pass (3 runs) | 419,786 | 16.6% |
| 2 | 6 peer concall verification | 211,783 | 8.4% |
| 3 | 7 emerging moat scan | 195,340 | 7.7% |
| 4 | 3 AR backward deep dive | 185,012 | 7.3% |
| 5 | 8 promoter check (web) | 166,102 | 6.6% |

No stage was re-run; no avoidable spend from intake defects this run.

(b) DOWNSHIFT FAILURES
- DOWNSHIFT FAILURE: stage 0 (input validation ran inline in the Opus orchestrator session, as run-pipeline step 1 directs "do this yourself"; no haiku stage-0 agent exists, so the downshift cannot take on this path). Verifier A ran on haiku as routed.

(c) COST SPIKES
- none (no prior AVIENCE run ledger exists).

(d) OPERATOR SNAPSHOT
- Operator: run /cost and /usage now and paste the cache hit ratio and loop totals under an "Operator snapshot" heading here.
