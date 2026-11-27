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
| 5 | stage-05-concall | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 285278 | 12m13s | 1 |
| 7 | stage-07-emoat (stalled, resumed from transcript; wall includes the stall) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 115601 | 378m17s | 1 |
| 6 | stage-06-peers (stalled, resumed from transcript; wall includes the stall) | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 278702 | 380m40s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 192611 | 10m44s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 288042 | 9m27s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 308243 | 16m16s | 1 |
| 12c | verifier-c-framework (phase 1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 165581 | 14m03s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 67331 | 2m08s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 237402 | 13m04s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 308034 | 13m02s | 1 |

## SUMMARY (close-out, 2026-11-16)

Ledger total (subagents only): 4,041,541 tokens over 20 runs.

### (a) TOP FIVE BY TOKENS
- stage-03-ardeep: 418,728 (10.4%)
- stage-02-notes-pass: 357,272 (8.8%)
- verifier-b-redflags: 308,243 (7.6%)
- stage-09b-dossier: 308,034 (7.6%)
- verifier-a-numerical: 288,042 (7.1%)

### (b) DOWNSHIFT FAILURES
none. stage-00-intake-check ran on claude-haiku-5-5 and verifier A on claude-sonnet-5-5, their frontmatter models. verifier-a-shadow did not run in this session (the single shadow run belongs to the TD Power session of the 2026-11-15 batch).

### (c) COST SPIKES
none. The prior run runs/azad-2026-07-12 has no session-cost.md ledger to compare with.

### (d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


### (e) FRESH VS RE-READ
All 20 ledger rows carry n/a in the in_tok, cache_read, cache_write and out_tok columns (the harness exposes one total per subagent run), so all 20 rows are left out of the three sums below. Nothing is estimated.
Fresh tokens (cache write + output + uncached input): n/a
Re-read tokens (cache read): n/a
Re-read multiple (re-read / cache write): n/a
