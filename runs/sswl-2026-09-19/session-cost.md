# SESSION COST LEDGER — SSWL 2026-09-19 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~90m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 139227 | 8m16s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 214498 | 8m29s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 157871 | 6m24s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 123355 | 5m53s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 271183 | 9m21s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 198311 | 9m22s | 1 |
| 5 | concall analysis (main) | claude-sonnet-5 | default | n/a | n/a | 170434 | 7m00s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | n/a | n/a | 193917 | 7m51s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 314975 | 6m21s | 1 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 178074 | 9m19s | 1 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | n/a | n/a | 169330 | 11m00s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 108620 | 2m22s | 1 |
| 12b | verifier B red flags | claude-opus-5 | default | n/a | n/a | 266960 | 13m42s | 1 |
| 12c | verifier C framework (phase-1 half) | claude-opus-5 | default | n/a | n/a | 110569 | 5m05s | 1 |
| 12d | verifier D peers | claude-sonnet-5 | default | n/a | n/a | 114550 | 6m05s | 1 |
| 13 | synthesis-lite (phase 1) | claude-opus-5 | default | n/a | n/a | 189286 | 8m38s | 1 |
| 9b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 191182 | 9m28s | 1 |

## CLOSE-OUT SUMMARY

Run total (sum of ledger rows with token counts): 3,112,342 tokens.

(a) TOP FIVE BY TOKENS
| rank | stage | total_tok | share |
|---|---|---|---|
| 1 | 2 notes triple-pass | 495,724 | 15.9% |
| 2 | 6 peer concall verification | 314,975 | 10.1% |
| 3 | 3 AR backward deep dive (8 phases) | 271,183 | 8.7% |
| 4 | 12b verifier B red flags | 266,960 | 8.6% |
| 5 | 4 business model decoder | 198,311 | 6.4% |

(b) DOWNSHIFT FAILURES
- DOWNSHIFT FAILURE: stage 0 (input validation ran inline in the Opus orchestrator session, as run-pipeline step 1 directs "do this yourself"; no haiku stage-0 agent exists, so the downshift cannot take on this path). Verifier A ran on haiku as routed.

(c) COST SPIKES
- none (no prior SSWL run ledger exists).

(d) OPERATOR SNAPSHOT
- Operator: run /cost and /usage now and paste the cache hit ratio and loop totals under an "Operator snapshot" heading here.
