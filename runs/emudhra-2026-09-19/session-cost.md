# SESSION COST LEDGER — EMUDHRA phase 1 (evidence)

Run: runs/emudhra-2026-09-19 | Phase 1 executed 2026-09-19 via /step1

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | input validation | orchestrator | - | - | - | - | - | 1 |
| 1 | gate 0 | sonnet | agent default | - | - | 168736 | 14m14s | 1 |
| 2.1 | notes pass 1 | sonnet | agent default | - | - | 255426 | 11m22s | 1 |
| 2.2 | notes pass 2 | sonnet | agent default | - | - | 139386 | 8m06s | 1 |
| 2.3 | notes pass 3 | sonnet | agent default | - | - | 96271 | 3m53s | 1 |
| 3 | AR deep dive | sonnet | agent default | - | - | 221183 | 11m55s | 1 |
| 1 | gate 0 (FCF correction) | sonnet | agent default | - | - | 204248 | 3m09s | 2 |
| 4 | business model | sonnet | agent default | - | - | 167712 | 8m07s | 1 |
| 5 | concall | sonnet | agent default | - | - | 150898 | 7m34s | 1 |
| 8 | promoter | sonnet | agent default | - | - | 216767 | 8m54s | 1 |
| 6 | peer concalls | sonnet | agent default | - | - | 281441 | 6m12s | 1 |
| 7 | emerging moat | sonnet | agent default | - | - | 223578 | 12m02s | 1 |
| 9 | TAM | sonnet | agent default | - | - | 158223 | 11m29s | 1 |
| 12a | verifier A | haiku | agent default | - | - | 89272 | 2m57s | 1 |
| 12b | verifier B | opus | agent default | - | - | 189076 | 6m16s | 1 |
| 12c | verifier C (phase 1 scope) | opus | agent default | - | - | 140612 | 5m03s | 1 |
| 12d | verifier D | sonnet | agent default | - | - | 286279 | 4m47s | 1 |
| 1 | gate 0 (Verifier C rework) | sonnet | agent default | - | - | 262863 | 5m04s | 3 |
| 6 | peer concalls (Verifier B/D correction) | sonnet | agent default | - | - | 367735 | 6m45s | 2 |
| 7 | emerging moat (Verifier C correction) | sonnet | agent default | - | - | 317236 | 7m05s | 2 |
| 5 | concall (Verifier B correction) | sonnet | agent default | - | - | 208696 | 7m48s | 2 |
| 7 | emerging moat (combined-label update) | sonnet | agent default | - | - | 395434 | 12m25s | 3 |
| 12b | verifier B (round 2) | opus | agent default | - | - | 245149 | 5m59s | 2 |
| 12c | verifier C (round 2, phase 1 scope) | opus | agent default | - | - | 134246 | 4m39s | 2 |
| 12d | verifier D (round 2) | sonnet | agent default | - | - | 138399 | 6m23s | 2 |
| 13 | synthesis-lite | opus | agent default | - | - | 190510 | 6m33s | 1 |
| 9b | Halt 1 dossier | sonnet | agent default | - | - | 167926 | 8m06s | 1 |

## CLOSE-OUT SUMMARY

Run total (ledger rows with token counts): 5417302 tokens. Stage 0 ran in the orchestrator (no subagent).

(a) TOP FIVE BY TOKENS (loop and retry runs summed per stage)

1. 7 emerging moat: 936,248 tokens, 17.3% of run
2. 6 peer concalls: 649,176 tokens, 12.0% of run
3. 1 gate 0: 635,847 tokens, 11.7% of run
4. 12b verifier B: 434,225 tokens, 8.0% of run
5. 12d verifier D: 424,678 tokens, 7.8% of run

(b) DOWNSHIFT FAILURES: none. Verifier A ran on haiku. Stage 0 validation ran inline in the orchestrator session, not as an Opus subagent. Stage 10 does not run in phase 1.

(c) COST SPIKES: none. No prior runs/emudhra-* ledger exists.

(d) OPERATOR SNAPSHOT: the operator runs /cost and /usage now and pastes the cache hit ratio and the loop totals under an "Operator snapshot" heading below. The orchestrator cannot read those interactive commands.

Note: the token column is the subagent total reported per run; in/out split was not reported by the harness. Correction rounds (stages 1, 5, 6, 7 and verifiers B, C, D round 2) account for the run# 2 and 3 rows.

## Operator snapshot

(pending operator)
| 9b | Halt 1 dossier (marker fix) | sonnet | agent default | - | - | 200012 | 2m49s | 2 |
