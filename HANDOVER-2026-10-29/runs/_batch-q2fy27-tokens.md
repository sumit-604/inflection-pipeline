# Q2 FY27 quarterly batch: token ledger

Started 2026-10-17. 12 companies. Parallel from about 13:20 IST.
Skipped by operator: Paushak, Tejas Networks, Urban Company, E2E Networks.

## Plan usage baseline (before parallel start)
- 5-hour window: 14% used (resets 17:20 IST)
- Weekly, all models: 42% used (resets 2026-10-19 19:30 IST)

## Per company (filled from each run's session-cost.md total_run_tok)

| # | Company | Session | Run folder | total_run_tok | Loops | A5 verdict (commit) |
|---|---|---|---|---|---|---|
| 04 | Aurum Proptech | local_cb52177b | runs/aurum-q2fy27 | 3,071,525 | 2 | COMPLETE (7918b8fa) |
| 06 | Cyient DLM | local_cb52177b | runs/cyientdlm-q2fy27 | 1,998,261 (floor, 2 rows ND) | 2 | INCOMPLETE, 1 item flagged (1e6f9f35) |
| 07 | Fedbank Financial | local_0c061ad4 | runs/fedfina-q2fy27 | 2,948,983 | 2 | INCOMPLETE, 1 wording item flagged (35b80e30) |
| 08 | Tata Communications | local_13b64936 | runs/tatacomm-q2fy27 | 2,072,847 | 1 | COMPLETE (4c53546e) |
| 09 | Heritage Foods | local_403c24fa | runs/heritgfood-q2fy27 | 2,625,523 | 2 | COMPLETE (34c41b58) |
| 10 | Indo Rama | local_46090183 | runs/indorama-q2fy27 | 2,539,688 | 2 | COMPLETE (e79d1561) |
| 11 | Supreme Power | local_756d8382 | runs/supremepwr-h1fy27 | 2,098,717 | 2 | INCOMPLETE, 2 items flagged (b06575bb) |
| 12 | Karnika Industries | local_6e7939b1 | runs/karnika-h1fy27 | 2,861,410 (floor, 1 row not recorded) | 2 | INCOMPLETE, 3 items flagged (0a56a73d) |
| 13 | Eimco Elecon | local_d1828036 | runs/eimcoeleco-q2fy27 | 2,468,930 | 2 | INCOMPLETE, 3 items flagged (0ea5640e) |
| 14 | Premier Polyfilm | local_b45964b3 | runs/premierpol-q2fy27 | 1,565,666 | 2 | INCOMPLETE, 2 items flagged (b2f20e6d) |
| 15 | G M Breweries | local_42086b67, local_45cfd2f8 | runs/gmbrew-q2fy27 | 1,837,603 | 2 | COMPLETE (50383e13) |
| 16 | Poonawalla Fincorp | local_2319d21e | runs/poonawalla-q2fy27 | 2,346,535 (excl. killed A5) | 1 | INCOMPLETE, 4 items flagged (b82585a6) |
| | TOTAL, 12 closed | | | 28,435,688 (floor) | | 5 COMPLETE, 7 closed with flags |

Nothing written to Notion; payloads saved as notion-payload.md per run, waiting for operator approval.

Aurum interim (A1-A3 only): about 868k tokens. Estimate per company about 1.2M.
Orchestrator sessions' own tokens are not in total_run_tok; read them per session at close.
