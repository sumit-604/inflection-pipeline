# SESSION COST — runs/rkforge-2026-11-12 (Phase 1, /step1)

Subagents ran as async agents in the desktop app. The harness exposes one total-token figure per subagent run. The input / cache / output split is not exposed and is written n/a, never estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 140,762 | 3m17s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 93,617 | 4m13s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 252,528 | 7m07s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 232,756 | 7m16s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 85,891 | 2m46s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 539,172 | 23m13s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 154,562 | 6m39s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 136,121 | 8m55s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 174,756 | 9m38s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 125,791 | 4m18s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 298,741 | 7m41s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 192,590 | 8m55s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 404,581 | 20m13s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 319,880 | 18m29s | 1 |
| 12c | verifier-c-framework (Gate 0 + EM) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 169,698 | 15m30s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 59,842 | 4m39s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 207,370 | 13m01s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 278,841 | 15m46s | 1 |

Ledger total (17 subagent runs): 3,867,499 tokens. Verifier A shadow: not run (see B00-inputs.yaml), so it has no row.

## CLOSE-OUT SUMMARY

### (a) TOP FIVE BY TOKENS
| rank | stage | total_tok | share of run |
|---|---|---|---|
| 1 | stage 2 notes triple-pass (3 runs) | 571,175 | 14.8% |
| 2 | stage 3 AR deep dive | 539,172 | 13.9% |
| 3 | verifier A numerical | 404,581 | 10.5% |
| 4 | verifier B red flags | 319,880 | 8.3% |
| 5 | stage 6 peers | 298,741 | 7.7% |

### (b) DOWNSHIFT FAILURES
none. stage-00-intake-check reported claude-haiku-5-5 and verifier A reported claude-sonnet-5-5 in their blocks. verifier-a-shadow did not run.

### (c) COST SPIKES
none. No prior run exists for RKFORGE.

### (d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


### (e) FRESH VS RE-READ
The harness exposed only a total per subagent run. All 17 ledger rows carry n/a in the input, cache-read and cache-write columns, so all 17 rows are left out of the sums.
Fresh tokens (cache write + output + uncached input): n/a (17 rows left out)
Re-read tokens (cache read): n/a (17 rows left out)
Re-read multiple (re-read / cache write): n/a (17 rows left out)
