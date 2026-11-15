# Session cost: invprecq-2026-11-15 (Phase 1)

Per-stage token ledger. Figures from subagent result metadata. This harness
exposes only total tokens and wall time per subagent; input, cache and output
splits are n/a (never estimated).

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| S1-BCD | step1 brief, peers, cap row | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 143,564 | 7m 25s | 1 |
| S1-F | step1 corpus collection and repair | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 192,920 | 25m 27s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 105,818 | 3m 25s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 87,880 | 3m 11s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 147,210 | 6m 31s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 155,407 | 6m 46s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 70,899 | 1m 43s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 389,948 | 16m 55s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 110,066 | 4m 03s | 1 |
| 4 | stage-04-bizmodel (stalled, stream watchdog 600s; no output) | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | n/a | n/a | 1 |
| 5 | stage-05-concall (stalled, stream watchdog 600s; no output) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | n/a | n/a | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 82,388 | 3m 05s | 2 |
| 5 | stage-05-concall (no-concall mode) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 157,026 | 5m 13s | 2 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 306,825 | 6m 19s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 232,671 | 9m 44s | 1 |
