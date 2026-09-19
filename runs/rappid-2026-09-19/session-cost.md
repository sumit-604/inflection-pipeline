# SESSION COST LEDGER — RAPPID phase 1 (evidence)

Run: runs/rappid-2026-09-19 | Phase 1 executed 2026-09-19 via /step1

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | input validation | orchestrator | - | - | - | - | - | 1 |
| 1 | gate 0 | sonnet | agent default | - | - | 117715 | 9m43s | 1 |
| 2.1 | notes pass 1 | sonnet | agent default | - | - | 133999 | 7m52s | 1 |
| 2.2 | notes pass 2 | sonnet | agent default | - | - | 122292 | 5m12s | 1 |
| 2.3 | notes pass 3 | sonnet | agent default | - | - | 90080 | 4m17s | 1 |
| 3 | AR deep dive | sonnet | agent default | - | - | 245930 | 13m56s | 1 |
| 4 | business model | sonnet | agent default | - | - | 127968 | 5m08s | 1 |
| 5 | concall (no-concall mode) | sonnet | agent default | - | - | 229571 | 7m44s | 1 |
| 8 | promoter | sonnet | agent default | - | - | 185080 | 9m20s | 1 |
| 6 | peer concalls | sonnet | agent default | - | - | 178576 | 7m40s | 1 |
| 7 | emerging moat | sonnet | agent default | - | - | 239916 | 10m16s | 1 |
| 9 | TAM | sonnet | agent default | - | - | 178863 | 15m28s | 1 |
| 12a | verifier A | haiku | agent default | - | - | 88441 | 3m39s | 1 |
| 12b | verifier B | opus | agent default | - | - | 204682 | 8m25s | 1 |
| 12c | verifier C (phase 1 scope) | opus | agent default | - | - | 120668 | 4m54s | 1 |
| 12d | verifier D | sonnet | agent default | - | - | 111919 | 6m04s | 1 |
| 1 | gate 0 (Verifier C correction) | sonnet | agent default | - | - | 101624 | 5m31s | 2 |
| 5 | concall (Verifier B correction) | sonnet | agent default | - | - | 231280 | 8m46s | 2 |
| 6 | peer concalls (Verifier B/D correction) | sonnet | agent default | - | - | 147339 | 8m40s | 2 |
| 12b | verifier B (round 2) | opus | agent default | - | - | 183483 | 6m14s | 2 |
| 12c | verifier C (round 2, phase 1 scope) | opus | agent default | - | - | 135214 | 6m18s | 2 |
| 12d | verifier D (round 2) | sonnet | agent default | - | - | 255099 | 5m10s | 2 |
| 7 | emerging moat (B01/B05 refresh, Verifier C correction) | sonnet | agent default | - | - | 167104 | 11m14s | 2 |
| 13 | synthesis-lite | opus | agent default | - | - | 201610 | 9m15s | 1 |
| 9b | Halt 1 dossier | sonnet | agent default | - | - | 199183 | 12m40s | 1 |

## CLOSE-OUT SUMMARY

Run total (ledger rows with token counts): 3,997,636 tokens. Stage 0 ran in the orchestrator (no subagent).

(a) TOP FIVE BY TOKENS (loop and retry runs summed per stage)

1. 5 concall: 460,851 tokens, 11.5% of run
2. 7 emerging moat: 407,020 tokens, 10.2% of run
3. 12b verifier B: 388,165 tokens, 9.7% of run
4. 12d verifier D: 367,018 tokens, 9.2% of run
5. 6 peer concalls: 325,915 tokens, 8.2% of run

(b) DOWNSHIFT FAILURES: none. Verifier A ran on haiku. Stage 0 validation ran inline in the orchestrator session, not as an Opus subagent. Stage 10 does not run in phase 1.

(c) COST SPIKES: none. No prior runs/rappid-* ledger exists.

(d) OPERATOR SNAPSHOT: the operator runs /cost and /usage now and pastes the cache hit ratio and the loop totals under an "Operator snapshot" heading below. The orchestrator cannot read those interactive commands.

Note: the token column is the subagent total reported per run; the in/out split was not reported by the harness. Correction rounds were fresh foreground agents (not SendMessage resumes): stages 1, 5, 6, 7 run 2 and verifiers B, C, D round 2.

## Operator snapshot

(pending operator)
