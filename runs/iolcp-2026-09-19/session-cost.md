# IOLCP 2026-09-19 — Session Cost Ledger (PHASE 1, Step-1 intake)

Per-stage token ledger. One row per subagent run. The harness exposes
total tokens and wall time per subagent; the in/out split is not exposed.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator (opus session) | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | gate 0 | sonnet | agent default | n/a | n/a | 111094 | 7m18s | 1 |
| 2 | notes pass 1 | sonnet | agent default | n/a | n/a | 171341 | 5m44s | 1 |
| 2 | notes pass 2 | sonnet | agent default | n/a | n/a | 172510 | 4m25s | 2 |
| 2 | notes pass 3 | sonnet | agent default | n/a | n/a | 98302 | 4m11s | 3 |
| 3 | AR deep dive | sonnet | agent default | n/a | n/a | 249228 | 12m52s | 1 |
| 4 | business model | sonnet | agent default | n/a | n/a | 200965 | 8m29s | 1 |
| 5 | concall analysis | sonnet | agent default | n/a | n/a | 187051 | 7m46s | 1 |
| 8 | promoter check | sonnet | agent default | n/a | n/a | 275655 | 9m38s | 1 |
| 6 | peer concalls | sonnet | agent default | n/a | n/a | 160679 | 6m32s | 1 |
| 7 | emerging moat | sonnet | agent default | n/a | n/a | 174758 | 9m35s | 1 |
| 6 | peer concalls (YAML retry) | sonnet | agent default | n/a | n/a | 201517 | 3m01s | 2 |
| 9 | TAM/SAM/SOM | sonnet | agent default | n/a | n/a | 231089 | 9m08s | 1 |
| 12a | verifier A numerical | haiku | agent default | n/a | n/a | 91878 | 3m04s | 1 |
| 12b | verifier B red flags | opus | agent default | n/a | n/a | 214027 | 7m27s | 1 |
| 12c | verifier C phase-1 half | opus | agent default | n/a | n/a | 120061 | 4m34s | 1 |
| 12d | verifier D peers | sonnet | agent default | n/a | n/a | 96369 | 2m55s | 1 |
| 13 | synthesis-lite | opus | agent default | n/a | n/a | 153758 | 5m10s | 1 |
| 9b | Halt 1 dossier | sonnet | agent default | n/a | n/a | 200850 | 6m58s | 1 |

## Close-out summary

Run total across subagent ledger rows: 3,111,132 tokens (orchestrator session tokens not included).

(a) TOP FIVE BY TOKENS
1. Stage 2 notes, 3 passes: 442,153 (14.2%)
2. Stage 6 peers, 2 runs (YAML retry): 362,196 (11.6%)
3. Stage 8 promoter: 275,655 (8.9%)
4. Stage 3 AR deep dive: 249,228 (8.0%)
5. Stage 9 TAM: 231,089 (7.4%)

(b) DOWNSHIFT FAILURES: none. Verifier A ran on haiku. Stage 0 ran inline in the orchestrator session (no subagent). Stage 10 does not run in phase 1.

(c) COST SPIKES: none (no prior IOLCP run).

(d) OPERATOR SNAPSHOT: run /cost and /usage now and paste the cache hit ratio and the loop totals below under "Operator snapshot".

### Operator snapshot
(pending operator)
