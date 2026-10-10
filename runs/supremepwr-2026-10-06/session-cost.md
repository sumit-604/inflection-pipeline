# Session cost: SUPREMEPWR 2026-10-06 (/step1 intake, phase 1)

Per-stage token ledger. Figures from subagent result metadata; the harness exposes only a total token count and wall time, so the split columns are n/a (never estimated).

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | inputs (inline) | claude-opus-5-5 (session) | session | n/a | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 87580 | 3m06s | 1 |
| 2 | notes pass 1 | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 219300 | 8m11s | 1 |
| 2 | notes pass 2 | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 255153 | 12m07s | 1 |
| 2 | notes pass 3 | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 92224 | 2m08s | 1 |
| 3 | ardeep | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 423126 | 17m20s | 1 |
| 4 | bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 176057 | 7m39s | 1 |
| 5 | concall | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 199949 | 8m54s | 1 |
| 8 | promoter | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 213813 | 8m07s | 1 |
| 6 | peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 195532 | 4m10s | 1 |
| 7 | emoat | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 318365 | 12m55s | 1 |
| 9 | tam | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 112666 | 5m08s | 1 |
| 12a | verifier A | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 508317 | 13m18s | 1 |
| 12b | verifier B | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 373298 | 19m21s | 1 |
| 12c | verifier C (phase-1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 188328 | 14m29s | 1 |
| 12d | verifier D | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 67110 | 1m28s | 1 |
| 13 | synthesis-lite | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 264998 | 11m44s | 1 |
| 9b | dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 231301 | 9m18s | 1 |

## CLOSE-OUT SUMMARY

Ledger total (subagents only): 3,927,117 tokens.

(a) TOP FIVE BY TOKENS
- 2 notes: 566,677 (14.4%)
- 12a verifier A: 508,317 (12.9%)
- 3 ardeep: 423,126 (10.8%)
- 12b verifier B: 373,298 (9.5%)
- 7 emoat: 318,365 (8.1%)

(b) DOWNSHIFT FAILURES: none (verifier A ran on its frontmatter model, claude-sonnet-5-5).

(c) COST SPIKES: none (no prior SUPREMEPWR run).

(d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)

