# AEQUS 2026-09-05 — Session Cost Ledger (PHASE 1)

Per-stage token ledger. One row per subagent run. Totals from subagent
result metadata (in/out split not exposed by the harness; total_tok and
wall recorded). Stage 0 ran in the orchestrator session, no subagent row.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 2 | notes-pass (pass 1) | sonnet | default | - | - | 227569 | 792s | 1 |
| 1 | gate-0 | sonnet | default | - | - | 169237 | 1059s | 1 |
| 2 | notes-pass (pass 2) | sonnet | default | - | - | 177662 | 689s | 2 |
| 2 | notes-pass (pass 3) | sonnet | default | - | - | 142220 | 582s | 3 |
| 3 | ar-deep-dive | sonnet | default | - | - | 338448 | 1379s | 1 |
| 4 | business-model | sonnet | default | - | - | 188309 | 761s | 1 |
| 5 | concall | sonnet | default | - | - | 182556 | 829s | 1 |
| 8 | promoter | sonnet | default | - | - | 275992 | 852s | 1 |
| 6 | peer-verification | sonnet | default | - | - | 0 | aborted (API 429 session limit, no output) | 1 |
| 7 | emerging-moat | sonnet | default | - | - | 0 | aborted (API 429 session limit, no output) | 1 |
| 6 | peer-verification | sonnet | default | - | - | 273591 | 447s | 2 |
| 7 | emerging-moat | sonnet | default | - | - | 253145 | 764s | 2 |
| 12d | verifier-peers | sonnet | default | - | - | 263465 | 346s | 1 |
| 12c | verifier-framework (phase-1 scope) | opus | default | - | - | 137381 | 728s | 1 |
| 12b | verifier-redflags | opus | default | - | - | 358756 | 873s | 1 |
| 9 | tam | sonnet | default | - | - | 168715 | 934s | 1 |
| 12a | verifier-numerical | haiku | default | - | - | 121063 | 159s | 1 |
| 13 | synthesis-lite | opus | default | - | - | 178004 | 823s | 1 |
