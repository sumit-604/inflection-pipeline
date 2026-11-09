# Session cost ledger: southwest-2026-11-09

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0a | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 174861 | 338s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 92266 | 196s | 1 |
| 2a | stage-02-notes-pass (CALL 1) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 209849 | 395s | 1 |
| 2b | stage-02-notes-pass (CALL 2) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 229186 | 420s | 1 |
| 2c | stage-02-notes-pass (CALL 3) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 115023 | 188s | 1 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 316305 | 632s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 146113 | 316s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 188236 | 434s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 286608 | 600s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 152167 | 295s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 331597 | 502s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 143779 | 354s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 56995 | 67s | 1 |
| 12a-s | verifier-a-shadow | claude-haiku-5-5 | high | n/a | n/a | n/a | n/a | 234829 | 476s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 311670 | 600s | 1 |
| 12c | verifier-c-framework (phase 1) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 148156 | 662s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 496184 | 1232s | 1 |
| 13 | stage-13-synthesis (lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 214421 | 548s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 210869 | 543s | 1 |

## SESSION CLOSE-OUT

(a) TOP FIVE BY TOKENS (run total 4059114 over 19 ledger rows)
- stage-02-notes-pass: 554058 (13.6%)
- verifier-b-redflags: 496184 (12.2%)
- stage-06-peers: 331597 (8.2%)
- stage-03-ardeep: 316305 (7.8%)
- verifier-a-numerical: 311670 (7.7%)

(b) DOWNSHIFT FAILURES: none. stage-00-intake-check and verifier-a-shadow ran on claude-haiku-5-5; verifier A ran on claude-sonnet-5-5, per frontmatter.

(c) COST SPIKES: none (no prior run for this ticker).

(d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


Fresh and cache token splits are n/a: the subagent notification in this app exposes only total tokens, tool uses and wall time.

(e) FRESH VS RE-READ (subagents only)
Fresh tokens (cache write + output + uncached input): n/a (all 19 rows left out)
Re-read tokens (cache read): n/a (all 19 rows left out)
Re-read multiple (re-read / cache write): n/a (all 19 rows left out)
