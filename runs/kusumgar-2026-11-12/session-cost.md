# Session cost — KUSUMGAR 2026-11-12 (Phase 1, /step1)

Per-stage token ledger. One row per subagent run, from the subagent result
metadata. n/a where the harness does not expose the figure; never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 84778 | 152s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 112016 | 286s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 232562 | 556s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 148383 | 362s | 1 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 87001 | 173s | 1 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 407088 | 943s | 1 |
| 5 | stage-05-concall (no-concall mode + 1 transcript) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 129853 | 229s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 224870 | 407s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 237511 | 479s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 159000 | 236s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 198808 | 401s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 172204 | 433s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 442844 | 763s | 1 |
| 12a-shadow | verifier-a-shadow | claude-haiku-5-5 | high | n/a | n/a | n/a | n/a | 259439 | 642s | 1 |
| 12c | verifier-c-framework (Gate 0 + EM scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 161273 | 744s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 41110 | 58s | 1 |
| 12b | verifier-b-redflags (no-concall mode) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 341056 | 1185s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 175054 | 544s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 286101 | 820s | 1 |

## Close-out summary

Ledger rows: 19. Sum of total_tok over all rows: 3,900,951. The harness exposed only each subagent's total tokens and wall time; input, cache-read, cache-write and output splits are n/a.

### (a) Top five by tokens
1. stage-02-notes-pass: 467,946 (12.0%)
2. verifier-a-numerical: 442,844 (11.4%)
3. stage-03-ardeep: 407,088 (10.4%)
4. verifier-b-redflags: 341,056 (8.7%)
5. stage-09b-dossier: 286,101 (7.3%)

### (b) Downshift failures
none. stage-00-intake-check and verifier-a-shadow ran on claude-haiku-5-5; verifier-a-numerical ran on claude-sonnet-5-5 (frontmatter models; block model fields agree).

### (c) Cost spikes
none. No prior run exists for KUSUMGAR.

### (d) Operator snapshot
SESSION TOTAL (/cost)


### (e) Fresh vs re-read
Rows left out of the sums below: 19 of 19 (every row has n/a in the cache columns).
Fresh tokens (cache write + output + uncached input): n/a
Re-read tokens (cache read): n/a
Re-read multiple (re-read / cache write): n/a
