# SESSION COST LEDGER — INA (Insolation Energy Ltd), run 2026-09-06

Per-stage token ledger. One line per subagent run; loops and retries get their
own line with a run counter. Written and committed with each stage, never
deferred to the end of the run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | orchestrator-inline (opus-5) | default | n/a | n/a | n/a | ~12m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 151,819 | 15m33s | 1 |
| 2a | notes pass 1 of 3 | claude-sonnet-5 | default | n/a | n/a | 212,865 | 14m14s | 1 |
| 2b | notes pass 2 of 3 | claude-sonnet-5 | default | n/a | n/a | 171,711 | 12m54s | 1 |
| 2c | notes pass 3 of 3 (consolidation) | claude-sonnet-5 | default | n/a | n/a | 78,204 | 4m42s | 1 |
| 3 | AR deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 239,778 | 15m43s | 1 |
| 3 | AR deep dive: append B03 block | claude-sonnet-5 | default | n/a | n/a | 305,046 | 4m41s | 2 |
| 5 | concall analysis (3 transcripts) | claude-sonnet-5 | default | n/a | n/a | 132,368 | 8m58s | 1 |
| 3 | AR deep dive: add monitorables[] | claude-sonnet-5 | default | n/a | n/a | 353,331 | 10m43s | 3 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 117,544 | 9m60s | 1 |
| 8 | promoter background check (web) | claude-sonnet-5 + web | default | n/a | n/a | 178,847 | 10m15s | 1 |
| 6 | peer concall verification (11) | claude-sonnet-5 | default | n/a | n/a | 327,257 | 10m57s | 1 |
| 7 | emerging moat 22-category scan | claude-sonnet-5 | default | n/a | n/a | 195,140 | 11m45s | 1 |
| 9 | TAM SAM SOM (web) | claude-sonnet-5 + web | default | n/a | n/a | 131,322 | 10m18s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 95,756 | 3m19s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 243,053 | 6m54s | 1 |
| 12c | verifier C framework (phase 1 scope) | claude-opus-4-8 | default | n/a | n/a | 118,538 | 8m43s | 1 |
| 12b | verifier B red flags | claude-opus-4-8 | default | n/a | n/a | 350,100 | 18m04s | 1 |
| 13 | synthesis-lite (3 files) | claude-opus-4-8 | default | n/a | n/a | 143,702 | 7m49s | 1 |
| 09b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 221,301 | 13m07s | 1 |

## SESSION CLOSE-OUT

Total subagent tokens across 19 runs: 3,767,682. Stage 0 ran inline in the
orchestrator session and reports no subagent metering, so it is absent from the
ranking below.

### (a) TOP FIVE BY TOKENS

| rank | # | stage | runs | total_tok | share of run |
|---|---|-------|------|-----------|--------------|
| 1 | 3 | AR deep dive (8 phases) | 3 | 898,155 | 23.8% |
| 2 | 12b | verifier B red flags | 1 | 350,100 | 9.3% |
| 3 | 6 | peer concall verification (11) | 1 | 327,257 | 8.7% |
| 4 | 12d | verifier D peer coverage | 1 | 243,053 | 6.5% |
| 5 | 09b | Halt 1 understanding dossier | 1 | 221,301 | 5.9% |
Stage 3 is 23.8% of the run on its own because it ran three times: the analysis
pass, then a block-append, then a monitorables fix. Two of those three runs
produced no new analysis. Each resume re-read the stage's own context, so the
two schema-repair runs cost 658,377 tokens, 17.5% of the entire run, to add one
YAML field and move a table into a block. That is the single largest avoidable
cost here and it belongs in LESSONS_ARCHIVE.

### (b) DOWNSHIFT FAILURES

DOWNSHIFT FAILURE: stage 0 input validation. DISPATCH routes stage 0 to Haiku
4.5 as a mechanical stage; it ran on the orchestrator session model (Opus 5).

This is a designed conflict, not a routing accident: run-pipeline.md step 1
instructs "VALIDATE (stage 0, do this yourself)", which puts stage 0 in the
orchestrator session, where the session model governs and cannot be changed
mid-session without busting the prompt cache. Recorded as a failure because the
rule says to record it. The fix is a prompt decision for the operator: either
route stage 0 to a haiku subagent, or amend DISPATCH to stop listing stage 0 as
a haiku stage.

Verifier A ran on claude-haiku-4-5 as routed. Stage 10 assembly does not run in
phase 1.

### (c) COST SPIKES

None. This is the first pipeline run on INA, so no prior session-cost.md ledger
exists for this ticker and the 1.5x test has no baseline.

### (d) OPERATOR SNAPSHOT

Keerti: run /cost and /usage now and paste the cache hit ratio and the loop
totals below. The orchestrator cannot read those interactive commands.

#### Operator snapshot

(paste /cost and /usage output here)
