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
