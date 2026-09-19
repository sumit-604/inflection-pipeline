# SESSION COST LEDGER — CAPILLARY 2026-09-19 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~70m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 132485 | 11m58s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 223637 | 10m17s | 1 |
| 1 | gate 0 scorecard (rescore with peer Data_Sheets; orchestrator omitted them in run 1) | claude-sonnet-5 | default | n/a | n/a | 173165 | 3m29s | 2 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 110157 | 8m25s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 76439 | 3m20s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 212500 | 14m45s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 122636 | 7m29s | 1 |
| 5 | concall analysis (3 transcripts) | claude-sonnet-5 | default | n/a | n/a | 171704 | 8m32s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 232448 | 10m03s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 354991 | 10m13s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 219716 | 11m14s | 1 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | n/a | n/a | 189634 | 13m25s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 96287 | 3m53s | 1 |
| 12b | verifier B red flags | claude-opus-5 | default | n/a | n/a | 207309 | 8m58s | 1 |
| 12c | verifier C framework (phase-1 half) | claude-opus-5 | default | n/a | n/a | 142726 | 6m46s | 1 |
| 12d | verifier D peers | claude-sonnet-5 | default | n/a | n/a | 87416 | 4m19s | 1 |
| 13 | synthesis-lite (phase 1) | claude-opus-5 | default | n/a | n/a | 237436 | 8m17s | 1 |
| 9b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 236476 | 9m52s | 1 |
| 9b | Halt 1 dossier marker fix (em-dash in DRAFT marker; resumed same agent) | claude-sonnet-5 | default | n/a | n/a | n/a | ~2m | 2 |

## CLOSE-OUT SUMMARY

Run total (sum of ledger rows with token counts): 3,227,162 tokens.

(a) TOP FIVE BY TOKENS
| rank | stage | total_tok | share |
|---|---|---|---|
| 1 | 2 notes triple-pass (3 runs) | 410,233 | 12.7% |
| 2 | 6 peer concall verification | 354,991 | 11.0% |
| 3 | 1 gate 0 scorecard (2 runs) | 305,650 | 9.5% |
| 4 | 13 synthesis-lite | 237,436 | 7.4% |
| 5 | 9b Halt 1 dossier (2 runs; fix run untallied) | 236,476 | 7.3% |

(b) DOWNSHIFT FAILURES
- DOWNSHIFT FAILURE: stage 0 (input validation ran inline in the Opus orchestrator session, as run-pipeline step 1 directs "do this yourself"; no haiku stage-0 agent exists). Verifier A ran on haiku as routed.

(c) COST SPIKES
- none (no prior CAPILLARY run ledger exists).

(d) OPERATOR SNAPSHOT
- Operator: run /cost and /usage now and paste the cache hit ratio and loop totals under an "Operator snapshot" heading here.
