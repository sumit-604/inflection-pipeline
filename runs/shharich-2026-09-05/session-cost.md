# SHHARICH 2026-09-05 — Session Cost Ledger (PHASE 1)

Per-stage token ledger. One row per subagent run. Totals from subagent
result metadata (in/out split not exposed by the harness; total_tok and
wall recorded). Stage 0 was orchestrator-run (no subagent row).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 1 | gate-0 | sonnet | default | - | - | 153998 | 778s | 1 |
| 2 | notes-pass (pass 1) | sonnet | default | - | - | 206204 | 877s | 1 |
| 2 | notes-pass (pass 2) | sonnet | default | - | - | 157747 | 544s | 2 |
| 2 | notes-pass (pass 3) | sonnet | default | - | - | 116274 | 447s | 3 |
| 3 | ar-deep-dive | sonnet | default | - | - | 305731 | 876s | 1 |
| 4 | business-model | sonnet | default | - | - | 180908 | 512s | 1 |
| 8 | promoter | sonnet | default | - | - | 243672 | 610s | 1 |
| 5 | concall (no-concall mode) | sonnet | default | - | - | 177190 | 640s | 1 |
| 6 | peer-verification | sonnet | default | - | - | n/a (HTTP 429 session limit mid-run; partial draft, no block; discarded) | ~15m | 1 |
| 7 | emerging-moat | sonnet | default | - | - | n/a (HTTP 429 session limit on final reply; report + block complete on disk, accepted) | ~15m | 1 |
| 6 | peer-verification | sonnet | default | - | - | 215760 | 513s | 2 |
| 12c | verifier-framework (phase-1 scope) | opus | default | - | - | 119537 | 582s | 1 |
| 12d | verifier-peers | sonnet | default | - | - | 235676 | 511s | 1 |
| 9 | tam | sonnet | default | - | - | 195542 | 985s | 1 |
| 12a | verifier-numerical | haiku | default | - | - | 110444 | 146s | 1 |
| 12b | verifier-redflags (no-concall mode) | opus | default | - | - | 353556 | 1121s | 1 |
| 12a | verifier-numerical | haiku | default | - | - | 85152 | 224s | 2 |
| 13 | synthesis-lite | opus | default | - | - | 142631 | 495s | 1 |
| 09b | halt1-dossier | sonnet | default | - | - | 39084 | 1429s | 1 |

## SESSION CLOSE-OUT (PHASE 1)

Run total (sum of all numeric ledger rows): ~3,039,106 tokens. Two rows carry n/a (stage 6 run 1 and stage 7 run 1, terminated by an HTTP 429 session limit; the harness reported no usage) and are excluded from the total, which therefore understates true spend.

### (a) TOP FIVE BY TOKENS (stage totals; loop and retry runs summed)
| rank | stage | total_tok | share |
|------|-------|-----------|-------|
| 1 | 2 notes-pass | 480,225 | 15.8% |
| 2 | 12b verifier-redflags (no-concall mode) | 353,556 | 11.6% |
| 3 | 3 ar-deep-dive | 305,731 | 10.1% |
| 4 | 8 promoter | 243,672 | 8.0% |
| 5 | 12d verifier-peers | 235,676 | 7.8% |

### (b) DOWNSHIFT FAILURES
none. The only phase-1 mechanical stage routed to haiku is verifier A, which ran on haiku (B12a). Stage 0 validation was run by the orchestrator session itself per run-pipeline.md step 1 (no subagent, no Opus); stage 10 assembly is phase 3.

### (c) COST SPIKES
none. No prior runs/shharich-*/session-cost.md ledger exists for this ticker (first run).

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and loop totals below. The orchestrator cannot read those interactive commands.

#### Operator snapshot
(pending operator paste)
