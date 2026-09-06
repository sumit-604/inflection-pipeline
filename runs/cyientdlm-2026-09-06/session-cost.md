# SESSION COST LEDGER — CYIENTDLM 2026-09-06 (PHASE 1)

Per-stage token ledger, one line per subagent run, written at the moment each
stage returns and committed with that stage.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit + PDF pre-extraction | orchestrator-inline | n/a | n/a | n/a | n/a | n/a | 1 |
| 2 | notes triple-pass, pass 1 of 3 | claude-sonnet-5 | default | n/a | n/a | 154100 | 8m11s | 1 |
| 1 | Gate 0 quantitative scorecard | claude-sonnet-5 | default | n/a | n/a | 121289 | 10m49s | 1 |
| 2 | notes triple-pass, pass 2 of 3 | claude-sonnet-5 | default | n/a | n/a | 119743 | 7m24s | 2 |
| 8 | promoter background check | claude-sonnet-5 | default | n/a | n/a | 164995 | 7m55s | 1 |
| 5 | concall analysis, main company | claude-sonnet-5 | default | n/a | n/a | 156702 | 9m14s | 1 |
| 2 | notes triple-pass, pass 3 of 3 (consolidation, emits B02) | claude-sonnet-5 | default | n/a | n/a | 68098 | 3m17s | 3 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 317321 | 6m33s | 1 |
| 7 | emerging moat 22-category scan | claude-sonnet-5 | default | n/a | n/a | 189274 | 8m32s | 1 |
| 3 | AR backward deep dive, 8 phases | claude-sonnet-5 | default | n/a | n/a | 283226 | 12m34s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 155052 | 7m30s | 1 |
| 9 | TAM SAM SOM market sizing | claude-sonnet-5 | default | n/a | n/a | 208001 | 12m54s | 1 |
| 12a | verifier A numerical audit | claude-haiku-4-5 | default | n/a | n/a | 84244 | 3m21s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 329374 | 6m26s | 1 |
| 12c | verifier C framework adherence (phase 1 scope) | claude-opus-4-8 | default | n/a | n/a | 109967 | 9m03s | 1 |
| 12a | verifier A numerical audit (re-run, addendum) | claude-haiku-4-5 | default | n/a | n/a | 102160 | 7m16s | 2 |
| 12b | verifier B concall red flags | claude-opus-5 | default | n/a | n/a | 459016 | 13m59s | 1 |
| 13 | synthesis-lite (phase 1, three files) | claude-opus-5 | default | n/a | n/a | 120858 | 5m37s | 1 |
| 9b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 187415 | 8m54s | 1 |

## SESSION CLOSE-OUT

### (a) TOP FIVE BY TOKENS

| rank | stage | model | total_tok | share of run | runs |
|---|---|---|---|---|---|
| 1 | verifier B concall red flags | claude-opus-5 | 459016 | 13.8% | 1 |
| 2 | notes triple-pass | claude-sonnet-5 | 341941 | 10.3% | 3 |
| 3 | verifier D peer coverage | claude-sonnet-5 | 329374 | 9.9% | 1 |
| 4 | peer concall verification | claude-sonnet-5 | 317321 | 9.5% | 1 |
| 5 | AR backward deep dive | claude-sonnet-5 | 283226 | 8.5% | 1 |

Run total across all ledger rows: 3330835 tokens.

### (b) DOWNSHIFT FAILURES

none. Verifier A ran on claude-haiku-4-5 in both runs, as DISPATCH requires. Stage 0 validation ran inline in the orchestrator session and consumed no subagent tokens. Stage 10 assembly does not run in phase 1.

### (c) COST SPIKES

none. This is the first run for CYIENTDLM; no prior runs/cyientdlm-<date>/session-cost.md ledger exists to compare against, so the 1.5x test has no baseline.

### (d) OPERATOR SNAPSHOT

Keerti: run /cost and /usage now and paste the cache hit ratio and the loop totals below, under an "Operator snapshot" heading. The orchestrator cannot read those interactive commands, so this section stays empty until you fill it.

#### Operator snapshot

(to be filled by the operator)

### NOTE ON THE LEDGER

The subagent result metadata exposes a single total-token figure per run, not an input/output split, so in_tok and out_tok are recorded n/a throughout. total_tok and wall time are taken verbatim from each subagent result. Stage 0 ran inline in the orchestrator session and has no subagent metadata.

