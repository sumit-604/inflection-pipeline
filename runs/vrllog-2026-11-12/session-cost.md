# SESSION COST: vrllog-2026-11-12 (Phase 1)

Per-stage token ledger. Subagents in this desktop session run asynchronously.
The harness exposes one total-token figure and a wall time per run, and no
input, cache or output split. Split columns read n/a. No figure is estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 121,589 | 3m35s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 120,660 | 4m55s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 168,394 | 7m43s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 143,805 | 5m26s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 75,196 | 2m12s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 343,587 | 18m08s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 157,649 | 5m48s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 130,250 | 6m35s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 187,845 | 7m51s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 107,937 | 4m40s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 136,048 | 6m19s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 262,500 | 9m36s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 56,336 | 2m27s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 349,963 | 13m27s | 1 |
| 12c | verifier-c-framework (phase 1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 158,278 | 14m49s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 362,895 | 20m17s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 210,065 | 11m31s | 1 |
