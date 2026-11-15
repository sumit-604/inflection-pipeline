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
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 261,046 | 7m31s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | n/a | n/a (report written 19:12 IST; session ended before usage metadata arrived) | 1 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 118,971 | 4m57s | 1 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 471,250 | 17m43s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 130,293 | 4m30s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 159,956 | 5m58s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 216,093 | 8m53s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 280,372 | 7m28s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 293,741 | 11m37s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 210,820 | 10m58s | 1 |
