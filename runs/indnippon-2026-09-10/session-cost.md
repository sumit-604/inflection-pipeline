# SESSION COST LEDGER — INDNIPPON 2026-09-10

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | input validation + freshness pair check | orchestrator-inline | n/a | n/a | n/a | n/a | n/a | 1 |
| 2 | notes triple-pass (pass 1 extraction) | claude-sonnet-5 | default | - | - | 152316 | 471s | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | - | - | 146812 | 956s | 1 |
| 2 | notes triple-pass (pass 2 gap-hunt) | claude-sonnet-5 | default | - | - | 135261 | 623s | 2 |
| 2 | notes triple-pass (pass 3 consolidation + B02) | claude-sonnet-5 | default | - | - | 82693 | 199s | 3 |
| 7 | emerging moat 22-category scan | claude-sonnet-5 | default | - | - | 146687 | 673s | 1 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | - | - | 312251 | 1321s | 1 |
| 5 | management commentary (NO-CONCALL degraded) | claude-sonnet-5 | default | - | - | 172120 | 479s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | - | - | 135165 | 561s | 1 |
| 8 | promoter background check | claude-sonnet-5 | default | - | - | 151791 | 714s | 1 (status partial: WebSearch unavailable all attempts) |
| 6 | peer concall verification (12 transcripts) | claude-sonnet-5 | default | - | - | 271100 | 318s | 1 |
| 9 | TAM SAM SOM market sizing | claude-sonnet-5 | default | - | - | 158793 | 907s | 1 (status partial: WebSearch unavailable) |
| 12a | verifier A numerical (pass 1) | claude-haiku-4-5 | default | - | - | 110489 | 223s | 1 |
| 12c | verifier C framework (phase-1 scope) | claude-opus-4-8 | default | - | - | 134264 | 520s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | - | - | 154972 | 498s | 1 |
| 12a | verifier A numerical (re-invocation, 180 claims) | claude-haiku-4-5 | default | - | - | 86209 | 320s | 2 |
| 12b | verifier B red flags (independent) | claude-opus-4-8 | default | - | - | 257852 | 1117s | 1 |
| 13 | synthesis-lite (phase 1, 3 files) | claude-opus-4-8 | default | - | - | 162742 | 361s | 1 (run#0 lost to session end, wrote nothing) |
| 09b | Halt 1 understanding dossier | claude-sonnet-5 | default | - | - | 261844 | 669s | 1 |

## CLOSE-OUT SUMMARY (run-pipeline step 6c)

Run total across all ledger rows: 3,033,361 subagent tokens. Stage 0 ran inline in the orchestrator and carries no subagent tokens.

### (a) Top five by tokens (loops and retries summed per stage)

| rank | stage | total_tok | share of run |
|---|---|---|---|
| 1 | 2 notes triple-pass | 370,270 | 12.2% |
| 2 | 3 AR backward deep dive | 312,251 | 10.3% |
| 3 | 6 peer concall verification | 271,100 | 8.9% |
| 4 | 09b Halt 1 understanding dossier | 261,844 | 8.6% |
| 5 | 12b verifier B red flags | 257,852 | 8.5% |

### (b) Downshift failures

none. The mechanical stages are stage 0 (ran inline, no subagent), stage 10 (not run in phase 1) and verifier A, which ran on claude-haiku-4-5 on both passes.

### (c) Cost spikes

none. No prior runs/indnippon-*/session-cost.md exists, so there is no baseline to compare against.

### (d) Operator snapshot

Reminder: run /cost and /usage now and paste the cache hit ratio and the loop totals below this heading. The orchestrator cannot read those interactive commands.

Operator snapshot:

(pending)

### Run notes

- Stage 13 run#0 was lost when the session ended mid-call. It wrote nothing and consumed no ledgered tokens that could be measured; run#1 is the ledgered run.
- Stage 2 is the single largest cost at three sequential passes. Stage 6 read twelve peer transcripts in one call.

