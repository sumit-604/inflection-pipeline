# Session cost: shawgeltin-2026-11-12 (Phase 1, /step1)

Per-stage token ledger. Figures come from the subagent result metadata; n/a where the harness does not expose a figure (never an estimate).

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 88351 | 135s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 63475 | 105s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 181145 | 414s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 183423 | 421s | 1 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 68060 | 111s | 1 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 339226 | 739s | 1 |
| 5 | stage-05-concall (no-concall mode) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 107375 | 216s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 106498 | 265s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 115375 | 156s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 100988 | 239s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 222749 | 576s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 83818 | 219s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 38579 | 55s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 301093 | 613s | 1 |
| 12b | verifier-b-redflags (no-concall mode) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 252330 | 870s | 1 |
| 12c | verifier-c-framework (phase-1 half) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 177829 | 1078s | 1 |
| 13 | stage-13-synthesis (phase-1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 183624 | 558s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 230213 | 558s | 1 |

## Close-out summary

(a) TOP FIVE BY TOKENS (stage total; share of 2844151 ledger tokens, 18 rows)
- stage-02-notes-pass (3 passes): 432628 (15.2%)
- stage-03-ardeep: 339226 (11.9%)
- verifier-a-numerical: 301093 (10.6%)
- verifier-b-redflags: 252330 (8.9%)
- stage-09b-dossier: 230213 (8.1%)

(b) DOWNSHIFT FAILURES: none. stage-00-intake-check ran on claude-haiku-5-5; verifier-a-numerical ran on claude-sonnet-5-5 (its frontmatter model). verifier-a-shadow did not run (.claude/shadow.yaml reads armed on main, but LESSONS_ARCHIVE 2026-11-11 CNL records it spent by runs/southwest-2026-11-09 on an unmerged branch; CNL precedent).

(c) COST SPIKES: none (no prior SHAWGELTIN run ledger exists).

Stage 5 no-concall bounded dispatch: 107375 tokens against the 100k target (OPEN 2026-10-04 C2 measurement; Kwick 254k).

(d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)


(e) FRESH VS RE-READ (subagents only)
Fresh tokens (cache write + output + uncached input): n/a (18 of 18 rows left out: the harness exposes only total tokens per subagent)
Re-read tokens (cache read): n/a (18 of 18 rows left out)
Re-read multiple (re-read / cache write): n/a (18 of 18 rows left out)
