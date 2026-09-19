# Session cost — SUSAN 2026-09-19 (phase 1)

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | inputs (inline) | orchestrator | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | gate0 | sonnet | agent default | n/a | n/a | 128467 | 7m49s | 1 |
| 2a | notes pass 1 | sonnet | agent default | n/a | n/a | 173917 | 8m35s | 1 |
| 2b | notes pass 2 | sonnet | agent default | n/a | n/a | 151856 | 9m03s | 1 |
| 2c | notes pass 3 | sonnet | agent default | n/a | n/a | 103035 | 4m34s | 1 |
| 3 | ardeep | sonnet | agent default | n/a | n/a | 209061 | 10m32s | 1 |
| 4 | bizmodel | sonnet | agent default | n/a | n/a | 174500 | 7m16s | 1 |
| 5 | concall | sonnet | agent default | n/a | n/a | 162448 | 7m37s | 1 |
| 8 | promoter | sonnet | agent default | n/a | n/a | 217365 | 10m50s | 1 |
| 6 | peers | sonnet | agent default | n/a | n/a | 189241 | 5m58s | 1 |
| 7 | emoat | sonnet | agent default | n/a | n/a | 174678 | 7m29s | 1 |
| 9 | tam | sonnet | agent default | n/a | n/a | 209880 | 16m40s | 1 |
| 12a | verifier A | haiku | agent default | n/a | n/a | 82833 | 3m12s | 1 |
| 12b | verifier B | opus | agent default | n/a | n/a | 237882 | 7m12s | 1 |
| 12c | verifier C (phase 1) | opus | agent default | n/a | n/a | 110121 | 4m29s | 1 |
| 12d | verifier D | sonnet | agent default | n/a | n/a | 203594 | 5m19s | 1 |
| 13 | synthesis-lite | opus | agent default | n/a | n/a | 225883 | 8m36s | 1 |
| 9b | dossier | sonnet | agent default | n/a | n/a | 204873 | 10m01s | 1 |
| 9b | dossier fix (marker dash, listing months) | sonnet | agent default | n/a | n/a | 265725 | 4m23s | 2 |

Notes: in_tok / out_tok are not split in the subagent result metadata this session; total_tok is the subagent_tokens figure. Stage 0 ran inline.

## CLOSE-OUT SUMMARY (phase 1)

Run total across ledger rows: 3,225,359 tokens (sum of total_tok).

(a) TOP FIVE BY TOKENS
1. dossier, stage 9b (sonnet, 2 runs: 204,873 + 265,725 fix): 470,598 (14.6%)
2. verifier B (opus): 237,882 (7.4%)
3. synthesis-lite (opus): 225,883 (7.0%)
4. promoter, stage 8 (sonnet): 217,365 (6.7%)
5. tam, stage 9 (sonnet): 209,880 (6.5%)

(b) DOWNSHIFT FAILURES
none. Verifier A ran on haiku. Stage 0 ran inline in the orchestrator session (Opus 5 session model), as run-pipeline.md step 1 directs ("do this yourself"); stage 10 does not run in phase 1.

(c) COST SPIKES
none. No prior runs/susan-* ledger exists.

(d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and the loop totals below.

### Operator snapshot
(pending)
