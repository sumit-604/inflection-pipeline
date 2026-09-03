# MPSLTD 2026-09-03 — Phase 1 session cost

Per-stage token ledger (written and committed with each stage).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 1 | gate0 | claude-sonnet-5 | default | n/a | n/a | 93078 | 335s | 1 |
| 2 | notes-pass1 | claude-sonnet-5 | default | n/a | n/a | 185271 | 449s | 1 |
| 2 | notes-pass2 | claude-sonnet-5 | default | n/a | n/a | 233412 | 748s | 2 |
| 2 | notes-pass3 | claude-sonnet-5 | default | n/a | n/a | 124931 | 302s | 3 |
| 3 | ardeep | claude-sonnet-5 | default | n/a | n/a | 240655 | 976s | 1 |
| 4 | bizmodel | claude-sonnet-5 | default | n/a | n/a | 200411 | 397s | 1 |
| 5 | concall | claude-sonnet-5 | default | n/a | n/a | 156768 | 490s | 1 |
| 8 | promoter | claude-sonnet-5 | default | n/a | n/a | 240781 | 800s | 1 |
| 7 | emoat | claude-sonnet-5 | default | n/a | n/a | 204904 | 633s | 1 |
| 6 | peers | claude-sonnet-5 | default | n/a | n/a | 227989 | 711s | 1 |
| 9 | tam | claude-sonnet-5 | default | n/a | n/a | 188715 | 765s | 1 |
| 12a | verifier-a-numerical | claude-haiku-4-5 | default | n/a | n/a | 133868 | 215s | 1 |
| 12c | verifier-c-framework | claude-opus-4-8 | default | n/a | n/a | 80001 | 240s | 1 |
| 12b | verifier-b-redflags | claude-opus-4-8 | default | n/a | n/a | 176095 | 437s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5 | default | n/a | n/a | 237392 | 492s | 1 |
| 13 | synthesis-lite | claude-opus-4-8 | default | n/a | n/a | 102116 | 374s | 1 |
| 09b | dossier | claude-sonnet-5 | default | n/a | n/a | 165017 | 505s | 1 |

## SESSION CLOSE-OUT (phase 1)

Run token total across all ledger rows: 2,991,404.

### (a) TOP FIVE BY TOKENS (stage loop/retry runs summed)
| rank | stage | total_tok | share of run |
|------|-------|-----------|--------------|
| 1 | 2 notes triple-pass (3 runs) | 543,614 | 18.2% |
| 2 | 8 promoter | 240,781 | 8.0% |
| 3 | 3 ardeep | 240,655 | 8.0% |
| 4 | 12d verifier-d-peers | 237,392 | 7.9% |
| 5 | 6 peers | 227,989 | 7.6% |

### (b) DOWNSHIFT FAILURES
none. The mechanical stages present in phase 1 ran on haiku as routed: verifier A on claude-haiku-4-5. (Stage 0 validation was done by the orchestrator, not a subagent; stage 10 assembly is a phase-3 stage, not run here.)

### (c) COST SPIKES
none. No prior runs/mpsltd-<date> session-cost.md exists (MPSLTD is a new name), so there is no 1.5x baseline to cross.

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and the loop totals here under an "Operator snapshot" heading. The orchestrator cannot read those interactive commands.
