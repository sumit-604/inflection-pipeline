# Session cost ledger — MODISONLTD 2026-09-03 (Phase 1 evidence)

Per-stage token ledger. One line per subagent run, written and committed with
its own stage. Loop/retry runs get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input-validation | orchestrator-opus-4-8 (inline) | - | - | - | - | - | 1 |
| 2 | notes-pass1 | claude-sonnet | - | - | - | 139801 | 7m40s | 1 |
| 1 | gate0 | claude-sonnet | - | - | - | 111941 | 11m32s | 1 |
| 2 | notes-pass2 | claude-sonnet | - | - | - | 100796 | 6m12s | 2 |
| 2 | notes-pass3 | claude-sonnet | - | - | - | 65166 | 3m15s | 3 |
| 3 | ar-deep-dive | claude-sonnet | - | - | - | 222338 | 12m18s | 1 |
| 4 | bizmodel | claude-sonnet | - | - | - | 114320 | 7m29s | 1 |
| 5 | concall-agm | claude-sonnet | - | - | - | 119204 | 7m40s | 1 |
| 8 | promoter | claude-sonnet | - | - | - | 142517 | 10m35s | 1 |
| 6 | peers | claude-sonnet | - | - | - | 216616 | 4m01s | 1 |
| 7 | emerging-moat | claude-sonnet | - | - | - | 168715 | 10m07s | 1 |
| 9 | tam-sam-som | claude-sonnet | - | - | - | 117127 | 11m33s | 1 |
| 12a | verifier-numerical | claude-haiku | - | - | - | 110862 | 3m34s | 1 |
| 12b | verifier-redflags | claude-opus | - | - | - | 218715 | 4m43s | 1 |
| 12c | verifier-framework | claude-opus | - | - | - | 90251 | 4m19s | 1 |
| 12d | verifier-peers | claude-sonnet | - | - | - | 79339 | 4m40s | 1 |
| 13 | synthesis-lite | claude-opus | - | - | - | 108174 | 7m39s | 1 |

## SESSION CLOSE-OUT (phase 1)

Run token total across all ledger rows: ~2,285,829 tokens (stage 0 inline, not metered).

### (a) TOP FIVE BY TOKENS (loop/retry runs summed into the stage)
1. stage 2 notes (3 passes) - 305,763 - 13.4%
2. stage 3 ar-deep-dive     - 222,338 -  9.7%
3. verifier 12b red-flags   - 218,715 -  9.6%
4. stage 6 peers            - 216,616 -  9.5%
5. stage 7 emerging-moat    - 168,715 -  7.4%

### (b) DOWNSHIFT FAILURES
none. Verifier A (mechanical) ran on haiku as routed. Stage 10 assembly does not run in phase 1. Stage 0 validation is done inline by the orchestrator session (opus) by design, not as a routed haiku subagent, so it is not a downshift failure.

### (c) COST SPIKES
none. No prior runs/modisonltd-<date>/session-cost.md exists (first run for this ticker), so no 1.5x baseline to cross.

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and the loop totals below.

#### Operator snapshot
(to be filled by operator)

<!-- late ledger row (dossier ran after close-out header was drafted) -->
| 09b | halt1-dossier | claude-sonnet | - | - | - | 159947 | 9m22s | 1 |
