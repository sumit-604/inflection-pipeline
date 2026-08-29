# SESSION COST LEDGER — SYSTANGO 2026-08-29 (Phase 1)

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input-validation | orchestrator-inline | - | - | - | - | - | 1 |
| 1 | gate-0-scorecard | claude-sonnet-5 | default | - | - | 203649 | 16.2m | 1 |
| 2 | notes-triple-pass | claude-sonnet-5 | default | - | - | 209101 | 22.1m | 1 |
| 2 | notes-triple-pass | claude-sonnet-5 | default | - | - | 238388 | 6.4m | 2 |
| 2 | notes-triple-pass | claude-sonnet-5 | default | - | - | 87566 | 3.7m | 3 |
| 3 | ar-deep-dive | claude-sonnet-5 | default | - | - | 228784 | 24.9m | 1 |
| 5 | concall-analysis | claude-sonnet-5 | default | - | - | 90706 | 5.3m | 1 |
| 8 | promoter-check | claude-sonnet-5 | default | - | - | 129735 | 9.0m | 1 |
| 4 | business-model | claude-sonnet-5 | default | - | - | 180923 | 15.0m | 1 |
| 6 | peer-concall | claude-sonnet-5 | default | - | - | 181655 | 11.2m | 1 |
| 7 | emerging-moat | claude-sonnet-5 | default | - | - | 202826 | 20.4m | 1 |
| 9 | tam-sam-som | claude-sonnet-5 | default | - | - | 199246 | 16.1m | 1 |
| 12a | verifier-a-numerical | claude-haiku-4-5 | default | - | - | 107447 | 2.9m | 1 |
| 12c | verifier-c-framework | claude-opus-4-8 | default | - | - | 84755 | 4.6m | 1 |
| 12b | verifier-b-redflags | claude-opus-4-8 | default | - | - | 111343 | 5.3m | 1 |
| 12d | verifier-d-peers | claude-sonnet-5 | default | - | - | 235798 | 8.5m | 1 |
| 13 | synthesis-lite | claude-opus-4-8 | default | - | - | 86254 | 3.5m | 1 |
| 9b | halt1-dossier | claude-sonnet-5 | default | - | - | 213765 | 8.2m | 1 |

## SESSION CLOSE-OUT SUMMARY (phase 1)

Run token total (sum of all ledger rows): ~2,791,941 tokens.

### (a) TOP FIVE BY TOKENS
| rank | stage | total_tok | share of run |
|------|-------|-----------|--------------|
| 1 | 2 notes-triple-pass (3 runs summed) | 535,055 | 19.2% |
| 2 | 12d verifier-d-peers | 235,798 | 8.4% |
| 3 | 3 ar-deep-dive | 228,784 | 8.2% |
| 4 | 9b halt1-dossier | 213,765 | 7.7% |
| 5 | 1 gate-0-scorecard | 203,649 | 7.3% |

### (b) DOWNSHIFT FAILURES
none. The only mechanical stage that ran as a subagent in phase 1 is verifier A, which ran on claude-haiku-4-5 as routed (stage 0 validation was orchestrator-inline; stage 10 assembly and verifier-A's sibling mechanical stages do not run in phase 1). No mechanical stage ran on Opus.

### (c) COST SPIKES
none. No prior runs/systango-<date>/session-cost.md ledger exists (this is the first SYSTANGO run), so no 1.5x prior-run comparison applies.

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and the loop totals below. The orchestrator cannot read those interactive commands.

#### Operator snapshot
- Cache hit ratio: [paste]
- Loop totals: [paste]
