# SESSION COST — SHAREINDIA 2026-09-19

Per-stage token ledger (one line per subagent run).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation (inline, orchestrator) | opus (orchestrator session) | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | gate 0 | sonnet | default | not reported | not reported | 109293 | 8m14s | 1 |
| 2.1 | notes pass 1 | sonnet | default | not reported | not reported | 291095 | 11m42s | 1 |
| 2.2 | notes pass 2 | sonnet | default | not reported | not reported | 234887 | 5m46s | 1 |
| 2.3 | notes pass 3 (final) | sonnet | default | not reported | not reported | 106906 | 5m22s | 1 |
| 3 | AR deep dive | sonnet | default | not reported | not reported | 239990 | 11m04s | 1 |
| 4 | business model | sonnet | default | not reported | not reported | 125495 | 5m21s | 1 |
| 5 | concall analysis | sonnet | default | not reported | not reported | 184488 | 8m56s | 1 |
| 8 | promoter check | sonnet | default | not reported | not reported | 274636 | 14m18s | 1 |
| 6 | peer concalls | sonnet | default | not reported | not reported | 139005 | 10m14s | 1 |
| 7 | emerging moat | sonnet | default | not reported | not reported | 167911 | 9m02s | 1 |
| 9 | TAM | sonnet | default | not reported | not reported | 168060 | 11m47s | 1 |
| 12a | verifier A numerical | haiku | default | not reported | not reported | 92063 | 3m16s | 1 |
| 12b | verifier B red flags | opus | default | not reported | not reported | 216051 | 7m32s | 1 |
| 12c | verifier C (gate0+EM half) | opus | default | not reported | not reported | 111946 | 4m23s | 1 |
| 12d | verifier D peers | sonnet | default | not reported | not reported | 123712 | 6m37s | 1 |
| 13L | synthesis-lite | opus | default | not reported | not reported | 185693 | 6m02s | 1 |
| 09b | Halt 1 dossier | sonnet | default | not reported | not reported | 173916 | 8m48s | 1 |
| 09b | Halt 1 dossier (marker fix, SendMessage resume) | sonnet | default | not reported | not reported | 57300 | 3m58s | 2 |

## CLOSE-OUT SUMMARY
Run total (subagents, ledger rows): 3,002,447 tokens (09b run# 2 = 231,216 cumulative agent total minus 173,916 from run# 1). The subagent result metadata reports total tokens only; the in/out split is not reported.

(a) TOP FIVE BY TOKENS
- notes: 632,888 (21.5%)
- promoter check: 274,636 (9.3%)
- AR deep dive: 239,990 (8.1%)
- verifier B red flags: 216,051 (7.3%)
- synthesis-lite: 185,693 (6.3%)

(b) DOWNSHIFT FAILURES
- none. Stage 0 ran inline in the orchestrator session (no subagent); verifier A ran on haiku; stage 10 does not run in phase 1.

(c) COST SPIKES
- none (no prior SHAREINDIA run).

(d) OPERATOR SNAPSHOT
- Operator: run /cost and /usage now and paste the cache hit ratio and loop totals below under 'Operator snapshot'.

### Operator snapshot
(pending)
