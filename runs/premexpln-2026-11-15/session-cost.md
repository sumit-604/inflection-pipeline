# Session cost — premexpln 2026-11-15 (/step1 intake + Phase 1)

Per-subagent token ledger. The harness exposes only total tokens and wall time per subagent; the input, cache and output split is n/a (never estimated).

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| S1-BCD | step1 brief, peers, cap row | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 122,910 | 7m05s | 1 |
| S1-F | step1 corpus collection and repair | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 213,923 | 30m13s | 1 |
| 1 | gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 61,365 | 2m48s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 211,120 | 6m08s | 1 |
| 2 | notes pass 1 | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 178,733 | 6m34s | 1 |
| 2 | notes pass 2 | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 190,758 | 6m38s | 2 |
| 2 | notes pass 3 | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 75,137 | 1m59s | 3 |
| 3 | ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 430,121 | 15m22s | 1 |
| 4 | bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 93,759 | 2m50s | 1 |
| 8 | promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 144,946 | 7m06s | 1 |
| 5 | concall | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 178,621 | 7m47s | 1 |
| 6 | peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | n/a | n/a (stalled after writing files) | 1 |
| 7 | emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | n/a | n/a (stalled, nothing written) | 1 |
| 7 | emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 180,937 | 6m43s | 2 |
| 9 | tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 126,499 | 5m57s | 1 |
| 12d | verifier D peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 53,722 | 0m58s | 1 |
| 12a | verifier A numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 254,888 | 8m57s | 1 |
| 12b | verifier B redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 345,724 | 13m56s | 1 |
| 12c | verifier C framework (phase 1) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 159,062 | 13m59s | 1 |
| 13 | synthesis-lite | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 188,660 | 10m50s | 1 |
| 9b | halt 1 dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 330,197 | 17m37s | 1 |

## SUMMARY (close-out, step 6c)

Run total over ledger rows with a reported figure: 3,541,082 tokens (20 rows; 2 rows n/a: stage 6 run 1 and stage 7 run 1, both stalled before usage was reported). /step1 intake rows (S1-BCD, S1-F) are inside the total: 336,833. Phase 1 rows: 3,204,249.

(a) TOP FIVE BY TOKENS
1. Stage 2 notes triple-pass (3 passes summed): 444,628 = 12.6%
2. Stage 3 AR deep dive: 430,121 = 12.1%
3. Verifier B red flags: 345,724 = 9.8%
4. Stage 9b Halt 1 dossier: 330,197 = 9.3%
5. Verifier A numerical: 254,888 = 7.2%

(b) DOWNSHIFT FAILURES: none. stage-00-intake-check ran on claude-haiku-5-5; verifier A ran on claude-sonnet-5-5; verifier-a-shadow did not run (the single shadow run belongs to the TD Power session).

(c) COST SPIKES: none (no prior run for PREMEXPLN).

(d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


(e) FRESH VS RE-READ
The harness reports only total tokens and wall time per subagent. The input, cache-read, cache-write and output split is n/a on every row, so all 22 rows are left out of the three sums.
Fresh tokens (cache write + output + uncached input): n/a (22 rows left out)
Re-read tokens (cache read): n/a (22 rows left out)
Re-read multiple (re-read / cache write): n/a (22 rows left out)
