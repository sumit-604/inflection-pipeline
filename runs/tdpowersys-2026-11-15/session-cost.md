# Session cost: tdpowersys 2026-11-15 (Phase 1)

Per-stage token ledger, from subagent result metadata. This harness exposes only total tokens and wall time per subagent; the split columns are n/a, never estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | step1-brief-peers-cap (Steps B-D) | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 138613 | 7m15s | 1 |
| S1 | step1-corpus-collection (Step F) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 225467 | 34m43s | 1 |
| 1 | gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 88054 | 4m33s | 1 |
| 0 | intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 152132 | 4m53s | 1 |
| 2 | notes-pass1 | claude-sonnet-5-5 | default-high | n/a | n/a | n/a | n/a | 268688 | 9m46s | 1 |
| 2 | notes-pass2 | claude-sonnet-5-5 | default-high | n/a | n/a | n/a | n/a | 244582 | 8m02s | 2 |
| 2 | notes-pass3 | claude-sonnet-5-5 | default-high | n/a | n/a | n/a | n/a | 133455 | 4m07s | 3 |
| 3 | ardeep | claude-sonnet-5-5 | default-high | n/a | n/a | n/a | n/a | 455522 | 19m15s | 1 |
| 8 | promoter | claude-sonnet-5-5 | default-high | n/a | n/a | n/a | n/a | 257013 | 7m00s | 1 |
| 4 | bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 236256 | 10m27s | 1 |
| 5 | concall | claude-sonnet-5-5 | default-high | n/a | n/a | n/a | n/a | 268432 | 15m26s | 1 |
