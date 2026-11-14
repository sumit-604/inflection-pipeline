# Session cost: cnl-2026-11-11 (Phase 1, /step1)

Per-stage token ledger. Figures come from the subagent result metadata; n/a where the harness does not expose a figure (never an estimate).

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 100930 | 202s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 78539 | 247s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 191282 | 484s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 226950 | 634s | 1 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 81994 | 165s | 1 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 414308 | 830s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 118082 | 308s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 143757 | 354s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 170950 | 557s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 168051 | 343s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 199264 | 355s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 83357 | 240s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 49400 | 87s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 277776 | 489s | 1 |
| 12c | verifier-c-framework (phase-1 half) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 125245 | 611s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 387821 | 961s | 1 |
| 13 | stage-13-synthesis (phase-1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 159611 | 576s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 247409 | 642s | 1 |

## Close-out summary

(a) TOP FIVE BY TOKENS (stage total; share of 3224726 ledger tokens)
- stage-02-notes-pass: 500226 (15.5%)
- stage-03-ardeep: 414308 (12.8%)
- verifier-b-redflags: 387821 (12.0%)
- verifier-a-numerical: 277776 (8.6%)
- stage-09b-dossier: 247409 (7.7%)

(b) DOWNSHIFT FAILURES: none. stage-00-intake-check ran on claude-haiku-5-5; verifier-a-numerical ran on claude-sonnet-5-5 (its frontmatter model). verifier-a-shadow did not run (switch spent by runs/southwest-2026-11-09 per HANDOFF.md).

(c) COST SPIKES: none (no prior CNL run ledger exists).

(d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


(e) FRESH VS RE-READ (subagent rows only)
Fresh tokens (cache write + output + uncached input): n/a (all 18 rows left out: the harness exposes only total tokens per subagent, not the split)
Re-read tokens (cache read): n/a (all 18 rows left out)
Re-read multiple (re-read / cache write): n/a (all 18 rows left out)
