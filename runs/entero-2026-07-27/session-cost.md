# Session Cost Ledger — ENTERO 2026-07-27 (Phase 1)

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input-validation | orchestrator | - | - | - | - | manual | 1 |
| 1 | gate-0-scorecard | claude-sonnet-5 | - | - | - | 120469 | 8m20s | 1 |
| 2 | notes-pass-1 | claude-sonnet-5 | - | - | - | 157823 | 8m30s | 1 |
| 2 | notes-pass-2 | claude-sonnet-5 | - | - | - | 155125 | 6m35s | 2 |
| 2 | notes-pass-3 | claude-sonnet-5 | - | - | - | 85653 | 4m24s | 3 |
| 3 | ar-deep-dive | claude-sonnet-5 | - | - | - | 203991 | 16m17s | 1 |
| 5 | concall-analysis | claude-sonnet-5 | - | - | - | 122533 | 6m38s | 1 |
| 8 | promoter-check | claude-sonnet-5 | - | - | - | 173602 | 11m13s | 1 |
| 4 | business-model | claude-sonnet-5 | - | - | - | 173064 | 14m05s | 1 |
| 7 | emerging-moat | claude-sonnet-5 | - | - | - | 262248 | 9m38s | 1 |
| 6 | peer-concalls | claude-sonnet-5 | - | - | - | 191671 | 10m41s | 1 |
| 9 | tam-sam-som | claude-sonnet-5 | - | - | - | 174824 | 11m53s | 1 |
| 12a | verifier-a-numerical | claude-haiku-4-5 | - | - | - | 126604 | 3m29s | 1 |
| 12b | verifier-b-redflags | claude-opus-4-8 | - | - | - | 138118 | 5m38s | 1 |
| 12c | verifier-c-framework | claude-opus-4-8 | - | - | - | 84989 | 4m01s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5 | - | - | - | 201108 | 9m14s | 1 |
| 13 | synthesis-lite | claude-opus-4-8 | - | - | - | 93670 | 6m01s | 1 |
| 9b | halt1-dossier | claude-sonnet-5 | - | - | - | 161605 | 12m17s | 1 |

## SESSION CLOSE-OUT (Phase 1)

Run total (sum of subagent totals, stage 0 orchestrator-manual excluded): ~2,627,097 tokens.

### (a) TOP FIVE BY TOKENS
| rank | stage | total_tok | share of run |
|------|-------|-----------|--------------|
| 1 | 2 notes triple-pass (3 runs: 157823+155125+85653) | 398,601 | 15.2% |
| 2 | 7 emerging-moat | 262,248 | 10.0% |
| 3 | 3 ar-deep-dive | 203,991 | 7.8% |
| 4 | 12d verifier-d-peers | 201,108 | 7.7% |
| 5 | 6 peer-concalls | 191,671 | 7.3% |

### (b) DOWNSHIFT FAILURES
none. Mechanical stages in phase 1: stage 0 validation (orchestrator-manual, no subagent) and verifier A (ran on claude-haiku-4-5, correct). Stage 10 assembly does not run in phase 1.

### (c) COST SPIKES
none. No prior accessible session-cost.md ledger for ENTERO (this folder's ledger was created fresh this run; the 2026-07-27 prior run on branch claude/entero-pipeline-run-ndqp3v is not present in this checkout).

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and the loop totals below under "Operator snapshot". The orchestrator cannot read those interactive commands.

#### Operator snapshot
(_to be filled by operator_)
| 10 | input-assembly | claude-haiku-4-5 | - | - | - | 66061 | 5m00s | 1 |
| 11 | valuation-role1 | claude-opus-4-8 | - | - | - | 140280 | 8m05s | 1 |
