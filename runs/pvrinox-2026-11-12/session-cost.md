# Session cost — runs/pvrinox-2026-11-12 (Phase 1, /step1)

Subagents ran through the desktop Agent tool. It exposes one total token figure
and wall time per subagent run. The input, cache-read, cache-write and output
split is not exposed, so those columns read n/a. Nothing is estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 96,806 | 2m32s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 185,419 | 5m46s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 124,963 | 6m33s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 271,988 | 9m43s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 86,314 | 2m47s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 410,226 | 22m59s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 149,957 | 6m46s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 195,489 | 9m14s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 219,423 | 9m59s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 184,507 | 5m19s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 125,016 | 5m55s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 146,205 | 8m44s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 322,120 | 12m25s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 350,980 | 14m51s | 1 |
| 12c | verifier-c-framework (phase 1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 167,880 | 15m16s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 82,450 | 3m01s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 170,763 | 8m39s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 269,373 | 14m52s | 1 |

Run total, subagents only: 3,559,879 tokens over 18 subagent runs.

## Summary block (run-pipeline step 6c)

(a) TOP FIVE BY TOKENS
1. stage 2 notes triple-pass (3 runs): 543,721 (15.3%)
2. stage 3 AR deep dive: 410,226 (11.5%)
3. verifier B red flags: 350,980 (9.9%)
4. verifier A numerical: 322,120 (9.0%)
5. stage 09b dossier: 269,373 (7.6%)

(b) DOWNSHIFT FAILURES
none. stage-00-intake-check reports claude-haiku-5-5 and verifier A reports
claude-sonnet-5-5 in their blocks, matching the agent frontmatter. The
Verifier A shadow did not run in this folder (claimed by
runs/kusumgar-2026-11-12), so there is no shadow row.

(c) COST SPIKES
none. No prior run exists for PVRINOX.

(d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


(e) FRESH VS RE-READ
Fresh tokens (cache write + output + uncached input): n/a
Re-read tokens (cache read): n/a
Re-read multiple (re-read / cache write): n/a
All 18 ledger rows were left out of these sums: the Agent tool exposed one total per subagent run and no input, cache or output split.
