# VINYAS 2026-09-01 — Session Cost Ledger (PHASE 1)

Per-stage token ledger. One row per subagent run. Totals from subagent
result metadata (in/out split not exposed by the harness; total_tok and
wall recorded).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 2 | notes-pass (pass 1) | sonnet | default | - | - | 184432 | 377s | 1 |
| 2 | notes-pass (pass 2) | sonnet | default | - | - | 206944 | 308s | 2 |
| 1 | gate-0 | sonnet | default | - | - | 179488 | 649s | 1 |
| 2 | notes-pass (pass 3) | sonnet | default | - | - | 94906 | 228s | 3 |
| 7 | emerging-moat | sonnet | default | - | - | 191180 | 694s | 1 |
| 3 | ar-deep-dive | sonnet | default | - | - | 192056 | 1059s | 1 |
| 4 | business-model | sonnet | default | - | - | 205914 | 434s | 1 |
| 8 | promoter | sonnet | default | - | - | 232873 | 414s | 1 |
| 5 | concall | sonnet | default | - | - | 149328 | 459s | 1 |
| 9 | tam | sonnet | default | - | - | 164256 | 464s | 1 |
| 6 | peer-verification | sonnet | default | - | - | 181527 | 450s | 1 |
| 12a | verifier-numerical | haiku | default | - | - | 100524 | 126s | 1 |
| 12b | verifier-redflags | opus | default | - | - | 120546 | 304s | 1 |
| 12c | verifier-framework | opus | default | - | - | 80621 | 325s | 1 |
| 12d | verifier-peers | sonnet | default | - | - | 181627 | 319s | 1 |
| 13 | synthesis-lite | opus | default | - | - | 78031 | 244s | 1 |
| 09b | halt1-dossier | sonnet | default | - | - | 177031 | 440s | 1 |

## SESSION CLOSE-OUT (PHASE 1)

Run total (sum of all ledger rows): ~2,721,284 tokens.

### (a) TOP FIVE BY TOKENS (stage totals; loop runs summed)
| rank | stage | total_tok | share |
|------|-------|-----------|-------|
| 1 | 2 notes-pass (3 passes) | 486,282 | 17.9% |
| 2 | 8 promoter | 232,873 | 8.6% |
| 3 | 4 business-model | 205,914 | 7.6% |
| 4 | 3 ar-deep-dive | 192,056 | 7.1% |
| 5 | 7 emerging-moat | 191,180 | 7.0% |

### (b) DOWNSHIFT FAILURES
none. The only phase-1 mechanical stage routed to haiku is verifier A, which ran on claude-haiku-4-5 (B12a). Stage 0 validation was orchestrator-run; stage 10 assembly is phase 3.

### (c) COST SPIKES
none. No prior runs/vinyas-*/session-cost.md ledger exists for this ticker.

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and loop totals below. The orchestrator cannot read those interactive commands.

#### Operator snapshot
(pending operator paste)
