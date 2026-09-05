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
