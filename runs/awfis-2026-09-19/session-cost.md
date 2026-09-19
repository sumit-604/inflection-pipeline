# SESSION COST LEDGER — AWFIS 2026-09-19 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~75m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 146267 | 12m34s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 261064 | 13m21s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 161682 | 7m53s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 108357 | 4m34s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 215916 | 13m30s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 338642 | 6m14s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 170648 | 9m01s | 1 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | n/a | n/a | 187974 | 13m50s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 103756 | 3m34s | 1 |
| 12b | verifier B red flags | claude-opus-5 | default | n/a | n/a | 385137 | 9m33s | 1 |
| 12c | verifier C framework (phase-1 half) | claude-opus-5 | default | n/a | n/a | 140049 | 7m06s | 1 |
| 12d | verifier D peers | claude-sonnet-5 | default | n/a | n/a | 100186 | 4m14s | 1 |
| 13 | synthesis-lite (phase 1) | claude-opus-5 | default | n/a | n/a | 190381 | 7m46s | 1 |
| 9b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 222921 | 9m10s | 1 |

## CLOSE-OUT SUMMARY

Run total (sum of ledger rows with token counts): 3,327,366 tokens.

(a) TOP FIVE BY TOKENS
| rank | stage | total_tok | share |
|---|---|---|---|
| 1 | 2 notes triple-pass (3 runs) | 531,103 | 16.0% |
| 2 | 12b verifier B red flags | 385,137 | 11.6% |
| 3 | 6 peer concall verification | 338,642 | 10.2% |
| 4 | 8 promoter check (web) | 263,265 | 7.9% |
| 5 | 9b Halt 1 dossier | 222,921 | 6.7% |

(b) DOWNSHIFT FAILURES
- DOWNSHIFT FAILURE: stage 0 (input validation ran inline in the Opus orchestrator session, as run-pipeline step 1 directs "do this yourself"; no haiku stage-0 agent exists, so the downshift cannot take on this path). Verifier A ran on haiku as routed.

(c) COST SPIKES
- none (no prior AWFIS run ledger exists).

(d) OPERATOR SNAPSHOT
- Operator: run /cost and /usage now and paste the cache hit ratio and loop totals under an "Operator snapshot" heading here.
