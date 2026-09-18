# SESSION COST LEDGER — TRUALT phase 1 (evidence)

Run: runs/trualt-2026-09-18 | Phase 1 executed 2026-09-18 via /step1

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | input validation | orchestrator | - | - | - | - | - | 1 |
| 2.1 | notes pass 1 | sonnet | agent default | - | - | 238777 | 8m48s | 1 |
| 2.1 | notes pass 1 (YAML retry) | sonnet | agent default | - | - | 264260 | 1m31s | 2 |
| 1 | gate 0 | sonnet | agent default | - | - | 159465 | 8m14s | 1 |
| 1 | gate 0 (peer rescore) | sonnet | agent default | - | - | 200373 | 3m09s | 2 |
| 2.2 | notes pass 2 | sonnet | agent default | - | - | 177464 | 7m03s | 1 |
| 2.3 | notes pass 3 | sonnet | agent default | - | - | 106851 | 3m51s | 1 |
| 3 | AR deep dive | sonnet | agent default | - | - | 247023 | 12m01s | 1 |
| 4 | business model | sonnet | agent default | - | - | 177997 | 6m33s | 1 |
| 5 | concall | sonnet | agent default | - | - | 192506 | 5m47s | 1 |
| 8 | promoter | sonnet | agent default | - | - | 224877 | 9m02s | 1 |
| 6 | peer concalls | sonnet | agent default | - | - | 294683 | 5m26s | 1 |
| 7 | emerging moat | sonnet | agent default | - | - | 196444 | 10m09s | 1 |
| 9 | TAM | sonnet | agent default | - | - | 197434 | 9m10s | 1 |
| 12a | verifier A | haiku | agent default | - | - | 100103 | 2m46s | 1 |
| 12b | verifier B | opus | agent default | - | - | 272401 | 9m51s | 1 |
| 12c | verifier C (phase 1 scope) | opus | agent default | - | - | 127033 | 5m40s | 1 |
| 12d | verifier D | sonnet | agent default | - | - | 134544 | 5m41s | 1 |
| 5 | concall (REWORK) | sonnet | agent default | - | - | 245814 | 8m28s | 2 |
| 6 | peer concalls (REWORK) | sonnet | agent default | - | - | 325956 | 8m01s | 2 |
| 12b | verifier B (round 2) | opus | agent default | - | - | 415871 | 11m04s | 2 |
| 12d | verifier D (round 2) | sonnet | agent default | - | - | 139070 | 6m50s | 2 |
| 13 | synthesis-lite | opus | agent default | - | - | 239039 | 9m39s | 1 |
| 9b | Halt 1 dossier | sonnet | agent default | - | - | 231407 | 9m35s | 1 |
| 9b | Halt 1 dossier (marker re-run) | sonnet | agent default | - | - | 261983 | 2m43s | 2 |

Token note: the subagent result metadata reports one total per run (subagent_tokens), not an input/output split, so in_tok and out_tok read "-". Wall times from duration_ms.

## CLOSE-OUT SUMMARY

(a) TOP FIVE BY TOKENS (retries and loops summed per stage; run total 5,171,375 over 22 subagent runs)
| rank | stage | total_tok | share |
|---|---|---|---|
| 1 | 2 notes triple-pass (3 passes + 1 YAML retry) | 787,352 | 15.2% |
| 2 | 12b verifier B (round 1 + round 2) | 688,272 | 13.3% |
| 3 | 6 peer concalls (run + rework) | 620,639 | 12.0% |
| 4 | 9b Halt 1 dossier (run + marker re-run) | 493,390 | 9.5% |
| 5 | 5 concall (run + rework) | 438,320 | 8.5% |

The REWORK cycle (stage 5 and 6 reruns, verifier B and D round 2) cost 1,126,711 tokens, 21.8% of the run.

(b) DOWNSHIFT FAILURES: none. Verifier A ran on haiku. Stage 0 ran inside the orchestrator session (Opus 5) as run-pipeline step 1 directs ("do this yourself"); it was not a dispatched stage. Stage 10 does not run in phase 1.

(c) COST SPIKES: none. No prior run exists for TRUALT.

(d) OPERATOR SNAPSHOT: run /cost and /usage now and paste the cache hit ratio and the loop totals below.

### Operator snapshot
(pending operator)
