# Session Cost Ledger — DIVGIITTS 2026-08-29 (phase 1)

Per-stage token ledger. One line per subagent run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input-validation | orchestrator | - | - | - | - | - | 1 |
| 1 | gate-0-scorecard | claude-sonnet-5 | default | - | - | 118960 | 9.0m | 1 |
| 2 | notes-pass1 | claude-sonnet-5 | default | - | - | 692810 | 7.8m | 1 |
| 2 | notes-pass2 | claude-sonnet-5 | default | - | - | 720012 | 9.1m | 2 |
| 2 | notes-pass3-consol | claude-sonnet-5 | default | - | - | 57277 | 3.0m | 3 |
| 3 | ar-deep-dive | claude-sonnet-5 | default | - | - | 739001 | 24.7m | 1 |
| 4 | business-model | claude-sonnet-5 | default | - | - | 774274 | 7.6m | 1 |
| 5 | concall-analysis | claude-sonnet-5 | default | - | - | 220502 | 7.2m | 1 |
| 8 | promoter-check | claude-sonnet-5 | default | - | - | 30307 | 14.5m | 1 |
| 6 | peer-verification | claude-sonnet-5 | default | - | - | 23402 | 8.5m | 1 |
| 7 | emerging-moat | claude-sonnet-5 | default | - | - | 25319 | 13.7m | 1 |
| 9 | tam-sam-som | claude-sonnet-5 | default | - | - | 62989 | 15.4m | 1 |
| 12a | verifier-a-numerical | claude-haiku-4-5 | default | - | - | 125630 | 2.3m | 1 |
| 12c | verifier-c-framework-p1 | claude-opus-4-8 | default | - | - | 78437 | 3.3m | 1 |
| 12b | verifier-b-redflags | claude-opus-4-8 | default | - | - | 234240 | 4.5m | 1 |
| 12d | verifier-d-peers | claude-sonnet-5 | default | - | - | 732085 | 4.8m | 1 |
| 13 | synthesis-lite-p1 | claude-opus-4-8 | default | - | - | 104344 | 6.8m | 1 |
| 09b | halt1-dossier | claude-sonnet-5 | default | - | - | 186614 | 6.8m | 1 |

## SESSION CLOSE-OUT (phase 1)

Run token total across all ledger rows: ~4,926,203 tokens.

### (a) TOP FIVE BY TOKENS (stage total, loop/retry runs summed)
1. Stage 2 notes triple-pass (3 runs)  1,470,099  (29.8%)
2. Stage 4 business model                 774,274  (15.7%)
3. Stage 3 AR deep dive                    739,001  (15.0%)
4. Verifier D peer coverage                732,085  (14.9%)
5. Verifier B concall red-flags            234,240  ( 4.8%)

### (b) DOWNSHIFT FAILURES
none. The one MECHANICAL stage that ran in phase 1 as a subagent (verifier A) ran on
claude-haiku-4-5 as routed. Stage 0 validation ran inline in the orchestrator (no subagent);
stage 10 assembly is a phase-3 stage and did not run here.

### (c) COST SPIKES
none. No prior runs/divgiitts-*/session-cost.md ledger exists (this is the first DIVGIITTS run),
so no 1.5x stage-over-stage comparison is possible.

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and the loop totals below
under "Operator snapshot". The orchestrator cannot read those interactive commands.

#### Operator snapshot
(paste /cost + /usage output here)
| 10 | input-assembly | claude-haiku-4-5 | default | - | - | 96340 | 3.8m | 1 |
| 11 | valuation-role1 | claude-opus-4-8 | default | - | - | 133413 | 9.3m | 1 |
