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
