# SESSION COST: credent-2026-11-12 (Phase 1)

Per-stage token ledger. Token figures come from subagent result metadata. This harness exposes only each subagent's total tokens and wall time. The input, cache-read, cache-write and output split reads n/a, never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 68063 | 2m18s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 175796 | 2m41s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 203800 | 7m54s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 254894 | 11m48s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 93411 | 3m13s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 303242 | 12m11s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 108590 | 4m40s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 156287 | 5m55s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 173409 | 7m24s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 66085 | 2m25s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 92932 | 3m52s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 215649 | 6m53s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 400928 | 9m33s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 52261 | 1m48s | 1 |
| 12c | verifier-c-framework (phase 1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 134524 | 12m04s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 408969 | 15m02s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 200956 | 11m28s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 298488 | 13m46s | 1 |

## SUMMARY (close-out, run-pipeline step 6c)

Ledger total: 3,408,284 tokens over 18 subagent runs (16 stages; stage 2 ran as three passes). Orchestrator usage is not in this ledger.

(a) TOP FIVE BY TOKENS
| rank | stage | total_tok | share of run |
|---|---|---|---|
| 1 | stage-02-notes-pass (3 passes summed) | 552,105 | 16.2% |
| 2 | verifier-b-redflags | 408,969 | 12.0% |
| 3 | verifier-a-numerical | 400,928 | 11.8% |
| 4 | stage-03-ardeep | 303,242 | 8.9% |
| 5 | stage-09b-dossier | 298,488 | 8.8% |

(b) DOWNSHIFT FAILURES: none. stage-00-intake-check reported claude-haiku-5-5 and verifier-a-numerical reported claude-sonnet-5-5, each its frontmatter model. verifier-a-shadow did not run (see B00.verifier_a_shadow), so there is nothing to check for it.

(c) COST SPIKES: none. No prior run exists for CREDENT.

(d) OPERATOR SNAPSHOT

SESSION TOTAL (/cost)


(e) FRESH VS RE-READ
The harness exposed only total tokens per subagent. Every one of the 18 ledger rows has n/a in the cache-read, cache-write and output columns, so all 18 rows are left out of the three sums below. No figure is estimated.
Fresh tokens (cache write + output + uncached input): n/a (18 of 18 rows left out)
Re-read tokens (cache read): n/a (18 of 18 rows left out)
Re-read multiple (re-read / cache write): n/a (18 of 18 rows left out)
