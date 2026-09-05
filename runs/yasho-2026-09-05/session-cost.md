# Session cost ledger — YASHO 2026-09-05 (Phase 1)

Per-stage token ledger. One line per subagent run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input-validation | orchestrator | - | - | - | - | - | 1 |
| 1 | gate-0 | claude-sonnet-5 | - | - | - | 112851 | 590s | 1 |
| 2 | notes-pass1 | claude-sonnet-5 | - | - | - | 153531 | 595s | 1 |
| 4 | business-model | claude-sonnet-5 | - | - | - | 114045 | 442s | 1 |
| 5 | concall | claude-sonnet-5 | - | - | - | 127250 | 374s | 1 |
| 8 | promoter | claude-sonnet-5 | - | - | - | 137136 | 478s | 1 |
| 2 | notes-pass2 | claude-sonnet-5 | - | - | - | 129047 | 352s | 2 |
| 6 | peers | claude-sonnet-5 | - | - | - | 174819 | 387s | 1 |
| 7 | emerging-moat | claude-sonnet-5 | - | - | - | 119886 | 468s | 1 |
| 2 | notes-pass3 | claude-sonnet-5 | - | - | - | 68092 | 188s | 3 |
| 9 | tam | claude-sonnet-5 | - | - | - | 103468 | 578s | 1 |
| 3 | ar-deep-dive | claude-sonnet-5 | - | - | - | 249892 | 1167s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5 | - | - | - | 67839 | 127s | 1 |
| 12c | verifier-c-framework | claude-opus-4-8 | - | - | - | 78066 | 237s | 1 |
| 12b | verifier-b-redflags | claude-opus-4-8 | - | - | - | 147625 | 359s | 1 |
| 12a | verifier-a-numerical | claude-haiku-4-5 | - | - | - | 213780 | 383s | 1+2(re-grade) |
| 13 | synthesis-lite | claude-opus-4-8 | - | - | - | 86109 | 226s | 1 |
| 09b | halt1-dossier | claude-sonnet-5 | - | - | - | 157543 | 423s | 1 |

## SESSION CLOSE-OUT

(a) TOP FIVE BY TOKENS (share of ~2.24M run total)
1. stage 2 notes triple-pass — 350,670 (15.6%)  [pass1 153,531 + pass2 129,047 + pass3 68,092]
2. stage 3 AR deep dive — 249,892 (11.2%)
3. verifier A numerical — 213,780 (9.5%)  [initial 95,673 + re-grade 118,107]
4. stage 6 peers — 174,819 (7.8%)
5. stage 09b dossier — 157,543 (7.0%)

(b) DOWNSHIFT FAILURES: none. The mechanical stages ran on their intended models — stage 0 validation was orchestrator-run; verifier A ran on claude-haiku-4-5; stage 10 assembly does not run in Phase 1.

(c) COST SPIKES: none. No prior YASHO run exists for a 1.5x comparison.

(d) OPERATOR SNAPSHOT: operator to run /cost and /usage now and paste the cache hit ratio and loop totals below.

## Operator snapshot
(pending operator paste)
