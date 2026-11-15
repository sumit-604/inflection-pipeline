# SESSION COST: deedev 2026-11-15 (Phase 1, /step1)

Per-stage token ledger. Subagents run async in this app; the result metadata gives a total token figure and wall time only, so the split columns are n/a. Never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 127408 | 254s | 1 |
| 1 | gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 97582 | 246s | 1 |
| 2 | notes-pass (pass 1) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 214092 | 410s | 1 |
| 2 | notes-pass (pass 2) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 174123 | 383s | 2 |
| 2 | notes-pass (pass 3) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 82097 | 146s | 3 |
| 3 | ardeep | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 289405 | 676s | 1 |
| 4 | bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 165562 | 358s | 1 |
| 8 | promoter | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 210001 | 501s | 1 |
| 5 | concall | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 202584 | 613s | 1 |
| 6 | peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 188142 | 316s | 1 |
| 7 | emoat | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | n/a | n/a | 1 |
| 9 | tam | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 177297 | 627s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 394817 | 883s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 422288 | 1001s | 1 |
| 12c | verifier-c-framework (phase 1) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 167460 | 775s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 48534 | 65s | 1 |
| 13 | synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 202633 | 668s | 1 |
| 9b | halt1 dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 305969 | 819s | 1 |

## SUMMARY (close-out)

Run total across 18 ledger rows (subagents only): 3,469,994 tokens. One row (stage 7 emoat) carries n/a: its agent stalled after writing the report and the failed notification gave no usage figure, so the true total is higher by that stage.

Intake rows outside the Phase 1 stage ledger: Steps B, C, D on claude-opus-5-5, 174,664 tokens, 481 s; Step F corpus collection on claude-sonnet-5-5, 179,931 tokens, 1,392 s.

### (a) TOP FIVE BY TOKENS

| rank | stage | total_tok | share of run total |
|---|---|---|---|
| 1 | notes-pass | 470,312 | 13.6% |
| 2 | verifier-b-redflags | 422,288 | 12.2% |
| 3 | verifier-a-numerical | 394,817 | 11.4% |
| 4 | halt1 dossier | 305,969 | 8.8% |
| 5 | ardeep | 289,405 | 8.3% |

The three notes passes are summed into one stage total (470,312).

### (b) DOWNSHIFT FAILURES

none. stage-00-intake-check ran on claude-haiku-5-5; verifier A ran on claude-sonnet-5-5. verifier-a-shadow did not run in this session (the single shadow run belongs to the TD Power session, operator batch instruction 2026-11-15).

### (c) COST SPIKES

none. No prior run exists for DEEDEV.

### (d) OPERATOR SNAPSHOT

SESSION TOTAL (/cost)


### (e) FRESH VS RE-READ

The app gives one total token figure per subagent, not the split. All 18 ledger rows carry n/a in the in_tok, cache_read, cache_write and out_tok columns, so all 18 rows are left out of the sums below. Nothing is estimated.

Fresh tokens (cache write + output + uncached input): n/a (18 rows left out)
Re-read tokens (cache read): n/a (18 rows left out)
Re-read multiple (re-read / cache write): n/a (18 rows left out)
