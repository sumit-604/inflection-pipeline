# Session cost ledger: QLL 2026-11-15 (/step1 intake + Phase 1)

Token figures come from subagent result metadata. This harness exposes only total tokens and wall time per subagent; the split columns are n/a, never estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | step1-BCD brief/peers/cap | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 115644 | 5m06s | 1 |
| S1 | step1-F corpus collection | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 197414 | 23m53s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 154227 | 5m06s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 153162 | 6m42s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 232236 | 6m41s | 1 |
