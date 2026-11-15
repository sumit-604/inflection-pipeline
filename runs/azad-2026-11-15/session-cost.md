# session-cost: runs/azad-2026-11-15 (Phase 1, /step1 intake)

Token figures come from subagent result metadata. The harness exposes one total per subagent run and wall time; the input, cache-read, cache-write and output split is not exposed, so those cells are n/a, never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| S1-BCD | step1 brief, peers, cap row | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 120630 | 6m31s | 1 |
| S1-F | step1 corpus collection | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 193318 | 22m13s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 118812 | 3m48s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 105065 | 5m08s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 148544 | 5m40s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 129627 | 5m39s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 79101 | 2m21s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 418728 | 19m18s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 252182 | 10m14s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 228709 | 11m13s | 1 |
