# SESSION COST LEDGER — TOTEM 2026-09-09 (phase 1)

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | input validation + corpus repair | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~40m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 216482 | 11m49s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 177757 | 7m39s | 1 |
| 1 | gate 0 scorecard (peer-data correction) | claude-sonnet-5 | default | n/a | n/a | 85032 | 5m52s | 2 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 171774 | 7m56s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 81282 | 3m58s | 3 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 266678 | 15m55s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 141064 | 8m14s | 1 |
| 5 | management/guidance analysis (no-concall mode) | claude-sonnet-5 | default | n/a | n/a | 189078 | 7m30s | 1 |
| 8 | promoter background check (web) | claude-sonnet-5 | default | n/a | n/a | 200094 | 12m51s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 236781 | 6m58s | 1 |
| 7 | emerging moat scan (22 categories) | claude-sonnet-5 | default | n/a | n/a | 136343 | 10m26s | 1 |
| 9 | TAM SAM SOM market sizing (web) | claude-sonnet-5 | default | n/a | n/a | 151834 | 13m21s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 95540 | 3m45s | 1 |
| 12b | verifier B red flags | claude-opus-4-8 | default | n/a | n/a | 287138 | 15m43s | 1 |
| 12c | verifier C framework (phase-1 scope) | claude-opus-4-8 | default | n/a | n/a | 126016 | 8m20s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 208088 | 6m24s | 1 |
| 1 | gate 0 scorecard (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 120757 | 8m26s | 3 |
| 5 | management/guidance analysis (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 233523 | 12m34s | 2 |
| 6 | peer concall verification (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 195260 | 7m36s | 2 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 114957 | 5m11s | 2 |
| 12b | verifier B red flags | claude-opus-4-8 | default | n/a | n/a | 391615 | 18m45s | 2 |
| 12c | verifier C framework (phase-1 scope) | claude-opus-4-8 | default | n/a | n/a | 139778 | 9m06s | 2 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 216060 | 9m25s | 2 |
| 5 | management/guidance analysis (audit cycle 2) | claude-sonnet-5 | default | n/a | n/a | 176881 | 10m13s | 3 |
| 6 | peer concall verification (audit cycle 2) | claude-sonnet-5 | default | n/a | n/a | 223393 | 7m28s | 3 |
| 12a | verifier A numerical (final) | claude-haiku-4-5 | default | n/a | n/a | 109706 | 5m57s | 3 |
| 12b | verifier B red flags (final) | claude-opus-4-8 | default | n/a | n/a | 395319 | 20m55s | 3 |
| 12d | verifier D peer coverage (final) | claude-sonnet-5 | default | n/a | n/a | 190875 | 9m40s | 3 |
| 13 | synthesis-lite (phase 1, three files) | claude-opus-4-8 | default | n/a | n/a | 108990 | 4m55s | 1 |
| 09b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 188336 | 7m19s | 1 |

---

## SESSION CLOSE-OUT — TOTEM 2026-09-09, phase 1

Run total across every subagent invocation: **5,576,431 tokens** over 25 subagent
runs. Stage 0 ran inline on the orchestrator and is not counted.

### (a) TOP FIVE BY TOKENS

| # | Stage | Total tokens | Share of run | Runs |
|---|---|---|---|---|
| 1 | Verifier B, concall/disclosure red flags | 1,074,072 | 19.3% | 3 |
| 2 | Stage 6, peer concall verification | 655,434 | 11.8% | 3 |
| 3 | Verifier D, peer coverage | 615,023 | 11.0% | 3 |
| 4 | Stage 5, management and guidance analysis | 599,482 | 10.8% | 3 |
| 5 | Stage 2, notes triple-pass | 430,813 | 7.7% | 3 |

The top five are 60.6% of the run, and four of the five are the stage 5 and stage 6
pair plus the two verifiers that audit them. That concentration is the run's real
story: this is where three verification cycles were spent and where the gate verdict
was ultimately decided.

### (b) DOWNSHIFT FAILURES

**none.** Verifier A ran on claude-haiku-4-5 in all three cycles, as DISPATCH
requires. Stage 10 assembly does not run in phase 1. Stage 0 input validation ran
inline on the orchestrator session rather than on haiku, which is what
run-pipeline.md step 1 instructs ("VALIDATE (stage 0, do this yourself)"), so it is
by design and not a failed downshift.

### (c) COST SPIKES

**none.** No prior run folder exists for this ticker, so there is no earlier ledger
to compare against. This run's ledger becomes the baseline for the next TOTEM run.

Worth recording for that comparison, though it is not a spike against a prior run:
stage 1 ran 3 times, stages 5 and 6 ran 3 times each, and the verifier layer ran 3
full cycles where the pipeline specifies one. Roughly 2.9 million tokens, about 52%
of the run, went to the second and third correction and verification cycles. They
earned it: they reversed two conclusions that would otherwise have shipped wrong
(the materials-cost pass-through finding, and the external support for the
raw-material half of the inventory question) and withdrew a false peer claim.

### (d) OPERATOR SNAPSHOT

The orchestrator cannot read the interactive cost commands. Keerti: run `/cost` and
`/usage` now and paste the cache hit ratio and the loop totals below.

**Operator snapshot**

    cache hit ratio:
    loop totals:
    notes:
