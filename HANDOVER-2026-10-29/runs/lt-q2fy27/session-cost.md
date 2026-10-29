# Session cost: LT q2fy27 (/run-quarterly, batch 2026-10-28, batch 3)

## DOCUMENT REVIEW summary row (shared baseline)

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`LT | 2026-10-28/29 | results+presentation+concall(ASR)+order press release (A1 only) | 72 pages (33+36+3) + 823-line ASR transcript | ~66,374 (27,261 + 20,480 + 16,722 + 1,912; fulltext chars / 4) | 2,509,649 | 1`

- Base run (12 agent runs): 2,254,285 tokens.
- Pre-A4 targeted fixes (A1 and A2 presentation, A3 finding P-19): 29,710 tokens. These are not an A5 loop; they are logged as their own rows.
- Correction loop 1 (A4 fix + A5 re-audit): 225,654 tokens. Logged as its own rows below.
- Orchestrator session tokens: NOT MEASURED in-session (not included in total_run_tok).

## Per-agent ledger

Token figures are the harness `subagent_tokens` per agent run. Resumed agents report a cumulative counter, so each resume row is the counter after the resume minus the counter before it (A1 pres 160,834 - 138,711; A2 pres 92,870 - 85,283; A4 565,987 - 461,574; A5 458,723 - 337,482).

| Agent | Document / step | Model | total_tok | Wall | Run # | Gate / result |
|---|---|---|---|---|---|---|
| A1 | presentation | claude-sonnet-5-5 | 138,711 | 407s | 1 | GATE A1 pass, 36/36 pages, R001-R1490; scrambled table slides transcribed from renders (appendix L951-L977) |
| A1 | results | claude-sonnet-5-5 | 250,729 | 841s | 1 | GATE A1 pass, 33/33 pages, R001-R2511; hidden OCR layer; -raw for p9, p11-33; p14 cash flow from render; OCR slips in VERIFY_LOG |
| A1 | concall (ASR) | claude-sonnet-5-5 | 91,634 | 238s | 1 | GATE A1 pass, 823/823 source lines, 7 chunk pages, R001-R492; rows hand-authored |
| A1 | order press release (Dhaka Metro) | claude-sonnet-5-5 | 53,219 | 101s | 1 | GATE A1 pass, 3/3 pages, R001-R069; A1 only by coordinator instruction |
| A2 | presentation | claude-sonnet-5-5 | 85,283 | 239s | 1 | GATE A2 pass, 1490/1490 IDs; below A1 |
| A2 | results | claude-sonnet-5-5 | 174,669 | 655s | 1 | GATE A2 pass, 2511/2511 IDs, 3 MFS non-data rows; below A1 |
| A2 | concall | claude-sonnet-5-5 | 51,244 | 100s | 1 | GATE A2 pass, 492/492 IDs; mechanical sweep 5 MFS (below 15); below A1 |
| A3 | presentation | claude-opus-5-5 | 218,746 | 602s | 1 | GATE A3 pass, 29 findings P-01..P-29; P-19 flagged a label swap |
| A3 | concall | claude-opus-5-5 | 160,117 | 448s | 1 | GATE A3 pass, 26 findings C-01..C-26 |
| A3 | results | claude-opus-5-5 | 230,877 | 827s | 1 | GATE A3 pass, 33 findings R-01..R-33; p12 table foots 24/24 |
| A4 | merged review | claude-opus-5-5 | 461,574 | 1293s | 1 | PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION |
| A5 | audit (loop 0) | claude-opus-5-5 | 337,482 | 1025s | 1 | INCOMPLETE: 1 FACTUAL, 4 MISSING, 2 CONTRADICTION, 8 STYLE -> loop to A4 |
| A1 | presentation fix (P-19, pre-A4) | claude-sonnet-5-5 | 22,123 | 84s | 2 | Domestic/International swap confirmed from render; R244-R251, R264-R271 relabelled; R1491-R1498 added |
| A2 | presentation ledger update (pre-A4) | claude-sonnet-5-5 | 7,587 | 24s | 2 | 1498/1498 IDs, zero orphans |
| A4 | correction loop 1 | claude-opus-5-5 | 104,413 | 634s | loop 1 | F1-F7 fixed, S1-S8 applied; verdict and every Section E number unchanged |
| A5 | re-audit | claude-opus-5-5 | 121,241 | 365s | loop 1 | INCOMPLETE on 1 text item (N1, FACTUAL, review L876); F1-F7 closed; no drift; N2, N3 STYLE |

Concurrency: at most two subagents at once until the pause; one at a time after RESUME (operator session shared the machine).

## Loop decision
- A5 re-audit left one FACTUAL item, N1: the Step 7A finance-cost cell says standalone debt is not lower at Sep-26. Filed standalone D/E (0.26, 0.23, 0.19; RF L1051) and debt to total assets (0.10, 0.08, 0.07; RF L1058) show it is lower year on year and quarter on quarter, and higher only against Mar-26.
- N1 moves no verdict-card number (verdict, cash class, Section E PAT, EPS and PE all unchanged). Batch rule 4 allows a second loop only for an item that moves a verdict-card number. No second loop ran. N1 is an open item in the brief and the payload.

## Notes for the coordinator
- Cost check: every A2 came in below its A1 (concall 51,244 < 91,634 is the narrowest ratio in absolute terms; results 174,669 < 250,729).
- All three PDFs carry an Adobe Paper Capture hidden OCR layer. The deck's table slides and the results statement pages scrambled under -layout; A1 transcribed from renders or used -raw. A3 still caught one A1 label swap (deck p17-18) by testing it against the deck's own printed shares.
- The concall A1 hand-authored rows despite the instruction. A2's scripted sweep found only 5 misses, so the gap was small this time.
- Loop cost 225,654 = 10.0% of the base run.
- Fresh tokens / re-read tokens / re-read multiple: NOT MEASURED in-session (harness reports one total per subagent).
