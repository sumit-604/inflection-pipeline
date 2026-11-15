# Session cost ledger: kpl-2026-11-15 (Phase 1)

Token columns: the harness exposes one total per subagent run (subagent_tokens), tool uses and wall time. The in / cache_read / cache_write / out split is not exposed, so those cells are n/a, never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| pre | step1 B/C/D brief (general-purpose) | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 134250 | 473s | 1 |
| pre | step1 F corpus (general-purpose) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 147234 | 576s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 87149 | 178s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 75888 | 203s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 184862 | 410s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 183402 | 526s | 2 |
