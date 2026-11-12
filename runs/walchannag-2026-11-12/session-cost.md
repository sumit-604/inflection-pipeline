# SESSION COST: walchannag 2026-11-12 (Phase 1, /step1)

Per-stage token ledger. Subagents run async in this app; the result metadata gives totals only where shown, otherwise n/a. Never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 77142 | 245s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 182902 | 352s | 1 |
| 2 | notes-pass (pass 1) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 178867 | 425s | 1 |
| 2 | notes-pass (pass 2) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 210016 | 429s | 2 |
| 7 | emoat | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 234524 | 660s | 1 |
| 2 | notes-pass (pass 3) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 98831 | 177s | 3 |
| 3 | ardeep | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 380928 | 944s | 1 |
| 5 | concall (no-call mode) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 128358 | 314s | 1 |
| 4 | bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 154529 | 343s | 1 |
| 8 | promoter | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 183503 | 495s | 1 |
| 6 | peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 294826 | 307s | 1 |
| 9 | tam | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 136757 | 406s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 348290 | 838s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 303327 | 1085s | 1 |
| 12c | verifier-c-framework (phase 1) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 162793 | 785s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 58477 | 156s | 1 |
| 13 | synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 178503 | 535s | 1 |
| 9b | halt1 dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 262781 | 794s | 1 |

## SUMMARY (close-out)

Run total across 18 ledger rows (subagents only): 3,575,354 tokens.

### (a) TOP FIVE BY TOKENS
- notes-pass: 487,714 (13.6%)
- ardeep: 380,928 (10.7%)
- verifier-a-numerical: 348,290 (9.7%)
- verifier-b-redflags: 303,327 (8.5%)
- peers: 294,826 (8.2%)

### (b) DOWNSHIFT FAILURES
none. stage-00-intake-check ran on claude-haiku-5-5 and verifier-a-numerical on claude-sonnet-5-5 (block model fields match the agent frontmatter). verifier-a-shadow did not run (see below).

### (c) COST SPIKES
none. No prior run exists for this ticker.

### NOTES
- Stage 5 (no-call mode) used 128,358 tokens against the 100k target (LESSONS open action C2, 2026-10-04).
- Verifier A shadow NOT RUN: .claude/shadow.yaml is armed on main, ten /step1 sessions ran in parallel on 2026-11-12, and the one-run slot was claimed by runs/kusumgar-2026-11-12. This session did not touch the switch.
- The app runs subagents async and exposes only total tokens and wall time per subagent. Input, cache-read, cache-write and output splits are n/a for every row.
- Model and effort columns are the agent frontmatter values.

### (d) SESSION TOTAL (/cost)

(operator: run /cost in the terminal and paste the result here)

### (e) FRESH VS RE-READ
Fresh tokens (cache write + output + uncached input): n/a
Re-read tokens (cache read): n/a
Re-read multiple (re-read / cache write): n/a (all 18 rows left out: the token split is not exposed for any row)
