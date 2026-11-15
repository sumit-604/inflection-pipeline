# Session cost: ASTRAMICRO 2026-11-15 (/step1 intake + Phase 1)

Per-stage token ledger. Figures come from each subagent's result metadata. The
harness in this session exposes only a total token count and wall time per
subagent, so the split columns are n/a, never estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| S1 | step1 B/C/D brief, peers, cap row | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 152,913 | 6m39s | 1 |
| S2 | step1 F corpus collection and repair | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 174,450 | 24m07s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 117,169 | 3m01s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 87,250 | 3m59s | 1 |
