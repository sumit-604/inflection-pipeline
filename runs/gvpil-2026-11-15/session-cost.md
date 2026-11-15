# Session cost ledger: GVPIL 2026-11-15 (Phase 1)

Token figures come from the subagent result metadata. This harness exposes only the total tokens and the wall time per subagent. Input, cache-read, cache-write and output splits are not exposed and are written n/a, never estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| S1-BCD | step1 brief, peers, cap row | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 121963 | 7m58s | 1 |
| S1-F | step1 corpus collection | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 175252 | 26m38s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 78049 | 3m52s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 131344 | 4m10s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 234786 | 9m13s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 230701 | 11m43s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 119300 | 4m30s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 394268 | 16m25s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | n/a | stalled 600s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 167437 | 6m09s | 2 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | n/a | stalled 600s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 139531 | 6m29s | 2 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | n/a | stalled 600s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 145292 | 6m43s | 2 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 182742 | 4m54s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 195762 | 7m18s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 82127 | 3m17s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 339295 | 10m19s | 1 |
| 12c | verifier-c-framework (phase-1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 163087 | 13m23s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 61926 | 1m26s | 1 |
