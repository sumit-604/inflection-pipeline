# SESSION COST — BORANA, run 2026-09-07 (Phase 1)

Per-stage token ledger. One line per subagent run, written and committed
with its own stage. Loop or retry runs get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 1 | Gate 0 scorecard | claude-sonnet-5 | default | 152183 | 10940 | 163123 | 8m40s | 1 |
| 2 | Notes triple-pass, pass 1 | claude-sonnet-5 | default | 193900 | 9895 | 203795 | 9m39s | 1 |
| 2 | Notes triple-pass, pass 2 | claude-sonnet-5 | default | 118500 | 6907 | 125407 | 7m22s | 2 |
| 2 | Notes triple-pass, pass 3 (consolidation) | claude-sonnet-5 | default | 108100 | 5089 | 113189 | 5m59s | 3 |
| 3 | AR backward deep dive | claude-sonnet-5 | default | 218400 | 11509 | 229909 | 12m60s | 1 |
| 5 | Concall analysis (NO-CONCALL MODE) | claude-sonnet-5 | default | 117200 | 6727 | 123927 | 8m36s | 1 |
| 4 | Business model decoder | claude-sonnet-5 | default | 141400 | 7921 | 149321 | 11m34s | 1 |
| 8 | Promoter check (web search) | claude-sonnet-5 | default | 190200 | 10484 | 200684 | 9m22s | 1 |
| 6 | Peer concall verification | claude-sonnet-5 | default | 150500 | 9160 | 159660 | 11m01s | 1 |
| 7 | Emerging moat scan (22 categories) | claude-sonnet-5 | default | 137100 | 8724 | 145824 | 8m48s | 1 |
| 9 | TAM SAM SOM (web search) | claude-sonnet-5 | default | 220800 | 10866 | 231666 | 17m59s | 1 |
| 12a | Verifier A numerical | claude-haiku-4-5 | default | 101800 | 3870 | 105670 | 2m18s | 1 |
| 12a | Verifier A numerical (coverage addendum) | claude-haiku-4-5 | default | 121500 | 4828 | 126328 | 3m38s | 2 |
| 12c | Verifier C framework (phase-1 scope) | claude-opus-4-8 | default | 103400 | 4920 | 108320 | 7m48s | 1 |
| 12d | Verifier D peer coverage | claude-sonnet-5 | default | 355800 | 11405 | 367205 | 6m44s | 1 |
| 12b | Verifier B red flags | claude-opus-4-8 | default | 251100 | 12067 | 263167 | 18m48s | 1 |
| 13 | Synthesis-lite (phase 1) | claude-opus-5 | default | 136700 | 6601 | 143301 | 7m51s | 1 |
| 09b | Halt 1 understanding dossier | claude-sonnet-5 | default | 187600 | 6450 | 194050 | 6m01s | 1 |

---

## SESSION CLOSE-OUT SUMMARY

Run total: 3,154,546 tokens across 18 subagent runs (stages 1-9, four
verifiers, synthesis-lite, Halt 1 dossier). Stage 0 ran inline in the
orchestrator and has no ledger row.

### (a) TOP FIVE BY TOKENS

| rank | stage | model | total_tok | share of run |
|---|---|---|---|---|
| 1 | 2 Notes triple-pass (3 runs summed) | claude-sonnet-5 | 442,391 | 14.0% |
| 2 | 12d Verifier D peer coverage | claude-sonnet-5 | 367,205 | 11.6% |
| 3 | 12b Verifier B red flags | claude-opus-4-8 | 263,167 | 8.3% |
| 4 | 12a Verifier A numerical (2 runs summed) | claude-haiku-4-5 | 231,998 | 7.4% |
| 5 | 9 TAM SAM SOM | claude-sonnet-5 | 231,666 | 7.3% |

The verification layer is three of the top five and 27.3% of the run. It
earned that this run: verifier B produced the three CRITICAL findings no
stage reached, verifier D overturned stage 6's central absence claim, and
verifier A's second pass held the source-fidelity gate. On a quieter name
the same spend would look heavy.

Stage 2 tops the table because the triple pass is three sequential reads of
a 130-page annual report plus a 417-page prospectus. Pass 2 and pass 3 cost
less than pass 1 (125k and 113k against 204k), so the sequence is working
as designed: each pass narrows.

### (b) DOWNSHIFT FAILURES

**none.** The mechanical stages DISPATCH routes to haiku are stage 0
validation, stage 10 assembly and verifier A. Stage 0 ran inline in the
orchestrator. Stage 10 does not run in phase 1. Verifier A ran on
claude-haiku-4-5 on both its runs. No mechanical stage ran on Opus.

### (c) COST SPIKES

**none.** No prior runs/borana-*/session-cost.md ledger exists; this is the
first BORANA run, so there is no baseline to measure 1.5x against. The next
BORANA run measures against this one.

One item for that future comparison, so it is not misread as a spike:
verifier A ran TWICE by design. Run 1 checked 15 figures and returned zero
findings, which was too thin for the sole source-fidelity authority, so it
was re-invoked once with a coverage addendum per the standing LESSONS
pattern. Run 2 checked 47. Treat 231,998 as the honest verifier A cost of a
run that needed the addendum, not as a baseline for one that does not.

### (d) OPERATOR SNAPSHOT

Keerti: run `/cost` and `/usage` now and paste the cache hit ratio and the
loop totals below. The orchestrator cannot read those interactive commands,
so this section stays empty until you fill it.

#### Operator snapshot

_(paste /cost and /usage output here)_
