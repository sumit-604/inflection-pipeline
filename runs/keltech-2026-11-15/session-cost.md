# Session cost: keltech-2026-11-15 (Phase 1)

Per-stage token ledger. The harness exposes only each subagent's total tokens and wall time. Input,
cache-read, cache-write and output splits are not exposed and are written n/a, never estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| S1-BCD | step1 brief, peers, cap row | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 129211 | 6m11s | 1 |
| S1-F | step1 corpus collection | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 157297 | 20m23s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 91806 | 3m10s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 104114 | 4m48s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 158208 | 6m34s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 179403 | 6m22s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 93551 | 2m57s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 337017 | 12m14s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 132499 | 5m32s | 1 |
| 5 | stage-05-concall (no-concall mode) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 174554 | 6m33s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 191749 | 8m31s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 127303 | 5m56s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 123869 | 4m58s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 202805 | 6m36s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 81575 | 2m19s | 1 |
| 12a | verifier-a-numerical (stalled, no output) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | n/a | stalled >10m | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 329096 | 8m29s | 2 |
| 12c | verifier-c-framework (stalled, no output) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | n/a | stalled >10m | 1 |
| 12c | verifier-c-framework (phase-1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 158958 | 13m33s | 2 |
| 12b | verifier-b-redflags (stalled, no output) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | n/a | stalled >10m | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 320666 | 18m38s | 2 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 188048 | 10m01s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 199508 | 8m57s | 1 |

## Close-out summary (2026-11-16)

Run total over every ledger row with a figure: 3,481,237 tokens (23 rows; 3 stalled verifier rows carry n/a).
total_tok is the harness figure reported per subagent at completion (subagent_tokens). The harness exposes no input, cache or output split.

### (a) TOP FIVE BY TOKENS

| rank | stage | total_tok | share of run |
|---|---|---|---|
| 1 | 2 stage-02-notes-pass (3 passes) | 431,162 | 12.4% |
| 2 | 3 stage-03-ardeep | 337,017 | 9.7% |
| 3 | 12a verifier-a-numerical | 329,096 | 9.5% |
| 4 | 12b verifier-b-redflags | 320,666 | 9.2% |
| 5 | 6 stage-06-peers | 202,805 | 5.8% |

### (b) DOWNSHIFT FAILURES

none. stage-00-intake-check ran on claude-haiku-5-5 and verifier A on claude-sonnet-5-5, per the model field of their blocks and the agent frontmatter. verifier-a-shadow did not run in this session (batch instruction: the single shadow run belongs to the TD Power session).

### (c) COST SPIKES

none. No prior run exists for this ticker.
Note for LESSONS open action C2: stage 5 in no-concall mode used 174,554 tokens against the 100k target.

### (d) OPERATOR SNAPSHOT

SESSION TOTAL (/cost)

(paste /cost output here)

### (e) FRESH VS RE-READ

All 21 ledger rows carry n/a in the in_tok, cache_read and cache_write columns, so all 21 rows are left out of the sums.
Fresh tokens (cache write + output + uncached input): n/a (21 rows left out)
Re-read tokens (cache read): n/a (21 rows left out)
Re-read multiple (re-read / cache write): n/a (21 rows left out)
