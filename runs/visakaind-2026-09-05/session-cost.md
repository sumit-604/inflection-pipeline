# VISAKAIND 2026-09-05 — Phase 1 session cost ledger

Per-stage token ledger. One row per subagent run. Token counts come from the
subagent result metadata where the harness reports them; "n/a" where it does
not. Stage 0 ran inline in the orchestrator session (no subagent).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | stage-00-inputs (inline) | orchestrator | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | stage-02-notes (pass 1) | sonnet | n/a | n/a | n/a | 217786 | 7m48s | 1 |
| 2 | stage-02-notes (pass 2) | sonnet | n/a | n/a | n/a | 186770 | 7m37s | 2 |
| 3 | stage-01-gate0 | sonnet | n/a | n/a | n/a | 184608 | 18m14s | 1 |
| 4 | stage-02-notes (pass 3) | sonnet | n/a | n/a | n/a | 147148 | 12m16s | 3 |
| 5 | stage-03-ardeep | sonnet | n/a | n/a | n/a | 383079 | 19m43s | 1 |
| 6 | stage-04-bizmodel | sonnet | n/a | n/a | n/a | 190888 | 10m58s | 1 |
| 7 | stage-05-concall | sonnet | n/a | n/a | n/a | 192647 | 13m16s | 1 |
| 8 | stage-06-peers | sonnet | n/a | n/a | n/a | n/a | ~11m, cut off HTTP 429 session limit ~16:52 UTC (report on disk, YAML block missing) | 1 |
| 9 | stage-07-emoat | sonnet | n/a | n/a | n/a | 60870 | 0m46s, cut off HTTP 429 (no report written) | 1 |
| 10 | stage-08-promoter | sonnet | n/a | n/a | n/a | n/a | ~22m, HTTP 429 after report + valid block were written to disk; ACCEPTED as complete (status partial: 6 egress-blocked searches) | 1 |
| 11 | stage-06-peers (resumed) | sonnet | n/a | n/a | n/a | 188319 | 2m49s (resume) | 2 |
| 12 | stage-07-emoat (resumed) | sonnet | n/a | n/a | n/a | 264919 | 12m08s (resume) | 2 |
