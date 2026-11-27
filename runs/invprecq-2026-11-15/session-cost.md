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
| 9 | stage-09-tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 121,255 | 6m 01s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 375,044 | 10m 52s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 590,885 | 25m 14s | 1 |
| 12c | verifier-c-framework (Gate 0 + EM scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 180,036 | 16m 35s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 77,851 | 2m 18s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 251,934 | 15m 32s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 209,340 | 9m 44s | 1 |

## SUMMARY (close-out, Phase 1)

Run total (sum of every ledger row with a figure; subagents only): 3,988,967 tokens.
Rows without a figure: 2 (stage 4 run 1 and stage 5 run 1, both stalled in the harness with no output).

### (a) TOP FIVE BY TOKENS (stage totals; loop and retry runs summed)
| rank | stage | total_tok | share |
|------|-------|-----------|-------|
| 1 | 12b verifier B (red flags, no-concall mode) | 590,885 | 14.8% |
| 2 | 3 AR deep dive | 389,948 | 9.8% |
| 3 | 12a verifier A (numerical) | 375,044 | 9.4% |
| 4 | 2 notes triple-pass (3 passes) | 373,516 | 9.4% |
| 5 | 6 peer concalls | 306,825 | 7.7% |

### (b) DOWNSHIFT FAILURES
none. stage-00-intake-check ran on claude-haiku-5-5 and verifier A on claude-sonnet-5-5, each its frontmatter model. verifier-a-shadow did not run in this session (the single shadow run belongs to the TD Power session).

### (c) COST SPIKES
none. No prior runs/invprecq-*/session-cost.md ledger exists for this ticker.
Note against LESSONS open action C2 (2026-10-04): stage 5 in no-concall mode cost 157,026 tokens on the completed run, above the 100k target (Kwick 254k).

### (d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


### (e) FRESH VS RE-READ
The harness exposes only total tokens per subagent. Input, cache-read, cache-write and output splits are n/a on all 23 ledger rows, so all 23 rows are left out of the sums.
Fresh tokens (cache write + output + uncached input): n/a
Re-read tokens (cache read): n/a
Re-read multiple (re-read / cache write): n/a
