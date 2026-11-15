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
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 493,633 | 14m12s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 303,729 | 17m01s | 1 |
| 12c | verifier-c-framework (phase 1: Gate 0 + EM) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 188,989 | 15m24s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 65,289 | 1m32s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 212,410 | 10m25s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 298,494 | 13m41s | 1 |

## SUMMARY (close-out, step 6c)

Run total over the ledger rows with a figure: 4,236,868 tokens (20 rows; the
stage 2 pass 2 row is n/a and is left out). Phase 1 stages and verifiers alone
(without S1 and S2): 3,909,505 tokens.

### (a) TOP FIVE BY TOKENS
| rank | stage | total_tok | share of run total |
|---|---|---|---|
| 1 | verifier-a-numerical | 493,633 | 11.7% |
| 2 | stage-03-ardeep | 471,250 | 11.1% |
| 3 | stage-02-notes-pass (3 passes; pass 2 n/a, so a floor) | 380,017 | 9.0% |
| 4 | verifier-b-redflags | 303,729 | 7.2% |
| 5 | stage-09b-dossier | 298,494 | 7.0% |

### (b) DOWNSHIFT FAILURES
none. stage-00-intake-check ran on claude-haiku-5-5 and verifier A on
claude-sonnet-5-5, their frontmatter models. verifier-a-shadow did not run in
this session (it belongs to the TD Power session of the same batch).

### (c) COST SPIKES
none. No prior run exists for ASTRAMICRO.

### (d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


### (e) FRESH VS RE-READ
The harness exposed only total tokens per subagent in this session, so every
row carries n/a in the split columns and all 21 rows are left out of these sums.
Fresh tokens (cache write + output + uncached input): n/a (21 of 21 rows left out)
Re-read tokens (cache read): n/a (21 of 21 rows left out)
Re-read multiple (re-read / cache write): n/a (21 of 21 rows left out)
