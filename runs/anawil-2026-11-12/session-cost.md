# session-cost: runs/anawil-2026-11-12 (Phase 1, /step1 intake)

Per-stage token ledger. Figures come from subagent result metadata. This harness exposes total tokens and wall time per subagent only; the input, cache-read, cache-write and output split is not exposed, so those columns read n/a (never an estimate).

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 102517 | 5m34s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 167539 | 6m18s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 195586 | 8m22s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 257758 | 13m15s | 2 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 126178 | 3m16s | 1 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 297982 | 13m27s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 486004 | 23m11s | 1 |
| 5 | stage-05-concall (no-concall mode) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 204433 | 7m59s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 199117 | 9m01s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 237220 | 11m24s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 352289 | 8m28s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 75725 | 2m36s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 220485 | 11m28s | 1 |
| 12c | verifier-c-framework (phase 1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 162760 | 14m14s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 329575 | 13m52s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 357071 | 21m09s | 1 |
| 1 | stage-01-gate0 (remediation) | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 88726 | 4m55s | 2 |
| 4 | stage-04-bizmodel (remediation) | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 111045 | 6m40s | 2 |
| 5 | stage-05-concall (remediation) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 189283 | 11m18s | 2 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 244803 | 13m13s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 350559 | 18m24s | 1 |

## Close-out summary (Phase 1)

Ledger rows: 21. Subagent total: 4,756,655 tokens. The orchestrator session itself is not in the ledger.

### (a) TOP FIVE BY TOKENS (loop and retry runs summed per stage)
- stage-02-notes-pass: 723,279 (15.2% of the run total)
- stage-03-ardeep: 486,004 (10.2% of the run total)
- stage-05-concall: 393,716 (8.3% of the run total)
- verifier-b-redflags: 357,071 (7.5% of the run total)
- stage-06-peers: 352,289 (7.4% of the run total)

### (b) DOWNSHIFT FAILURES
none. stage-00-intake-check ran on claude-haiku-5-5 and verifier-a-numerical on claude-sonnet-5-5, each per its agent frontmatter (model as reported in each block; the harness does not expose a separate model field). verifier-a-shadow did not run (the single shadow run was claimed by runs/kusumgar-2026-11-12).

### (c) COST SPIKES
none. No prior run exists for ANAWIL.

Notes that are not spikes by the rule: stage 5 run 1 used 204,433 tokens against the 100k no-concall target (LESSONS open action C2; Kwick was 254k). One remediation cycle added 389,054 tokens (stages 1, 4, 5).

### (d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


### (e) FRESH VS RE-READ (subagents only)
All 21 ledger rows were left out of these sums: this harness reports one total per subagent and no input, cache-read, cache-write or output split. No figure is estimated.
Fresh tokens (cache write + output + uncached input): n/a
Re-read tokens (cache read): n/a
Re-read multiple (re-read / cache write): n/a
