# session-cost: RAYMONDREL Q2 FY27 (/run-quarterly, 2026-10-28)

DOCUMENT REVIEW summary row (shared baseline):

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`RAYMONDREL | 2026-10-28 | results(incl. PR)+presentation+corpaction+concall(ASR) | 15+46+3 pages + 600 transcript lines | ~46,500 (fulltext chars / 4: results 12,240; deck 18,900; corpaction 2,060; call 13,280) | 3,122,093 | 1`

Token figures are the harness `subagent_tokens` per agent run. Loop rows are resumed agents (SendMessage). Their figure is what the harness reported for the resumed run. It may include the re-read of the agent's own prior context. The orchestrator session's own tokens are not in this ledger (NOT FOUND: the harness gives no per-session figure in-session). At most two subagents ran at once (6 GB machine, three sibling sessions).

## Per-agent ledger, base run

| Agent | Doc | Model | total_tok | Wall | Run # | Gate / note |
|---|---|---|---|---|---|---|
| A1 | presentation | claude-sonnet-5-5 | 125,535 | 338 s | 1 | PASS 46/46 pages, R001-R1082; p5, p29-44 values from renders |
| A1 | results (incl. press release) | claude-sonnet-5-5 | 143,171 | 364 s | 1 | PASS 15/15 pages, R001-R874; OCR text layer; p3-5, p9-11, p13 re-read from 150 dpi renders |
| A1 | concall (ASR .txt) | claude-sonnet-5-5 | 80,598 | 319 s | 1 | PASS 600/600 lines, R001-R320; 11 ASR_SUSPECT |
| A1 | corpaction (ICICI Pru agreement) | claude-sonnet-5-5 | 46,526 | 87 s | 1 | PASS 3/3 pages, R001-R063; no A2/A3 by design |
| A2 | presentation | claude-sonnet-5-5 | 62,322 | 167 s | 1 | PASS 1082/1082, 0 orphans; fulltext sweep second method; below A1 |
| A2 | results | claude-sonnet-5-5 | 102,814 | 290 s | 1 | PASS 874/874, 0 orphans; below A1 |
| A2 | concall | claude-sonnet-5-5 | 54,066 | 92 s | 1 | PASS 320/320, 0 orphans; below A1 (line/turn columns later found broken by A5, C2) |
| A3 | presentation | claude-opus-5-5 | 243,153 | 847 s | 1 | PASS 17/17, 35 findings |
| A3 | results | claude-opus-5-5 | 186,811 | 536 s | 1 | PASS 17/17, 23 findings |
| A3 | concall | claude-opus-5-5 | 131,612 | 412 s | 1 | PASS 17/17, 23 findings |
| A4 | merged (4 docs) | claude-opus-5-5 | 467,934 | 1,335 s | 1 | PROCEED WITH FLAGS; 25 questions |
| A5 | audit | claude-opus-5-5 | 372,568 | 1,116 s | 1 | INCOMPLETE (F1-F4, M1-M4, C1, C2) |
| **Base subtotal** | | | **2,017,110** | | | |

## Correction loop ledger (iteration 1 of 1)

| Agent | Doc | Model | total_tok | Wall | Run # | Note |
|---|---|---|---|---|---|---|
| A2 | concall (resumed) | claude-sonnet-5-5 | 58,988 | 35 s | loop 1 | C2: line and turn columns rebuilt from A1 (awk split bug); 10 DRIFT rows marked |
| A4 | patch (resumed) | claude-opus-5-5 | 564,512 | 546 s | loop 1 | F1-F4, M1-M4, C1 fixed; S1-S5 applied; whole-file rewrite (agent has no Edit tool) |
| A5 | re-audit (resumed) | claude-opus-5-5 | 481,483 | 259 s | loop 1 | COMPLETE; drift check clean; style S6-S8 |
| **Loop subtotal** | | | **1,104,983** | | | |

**total_run_tok = 2,017,110 + 1,104,983 = 3,122,093.** Loop share 35.4%.

## By model

| Model | Runs | Tokens |
|---|---|---|
| claude-sonnet-5-5 | 8 | 674,020 |
| claude-opus-5-5 | 7 | 2,448,073 |

## What drove cost

- A4 and A5 together took 1,886,497 tokens (60.4%), base and loop combined. The resumed loop runs re-read their own large prior context, so a resumed patch costs more than its edits.
- A3 presentation (243,153) was the largest A3. The deck has 1,082 rows, and 16 project slides needed render-mapped reads.
- A1 on the results file paid for six statement-page renders. The text layer is an OCR layer with scrambled columns.
- The ICICI filing ran A1 only (46,526). Skipping its A2/A3 chain saved an estimated 150-200k tokens [INFERENCE from the A2/A3 ratios above].

## Fresh vs re-read tokens

Fresh tokens, re-read tokens and the re-read multiple: NOT FOUND. The harness reports one `subagent_tokens` figure per run, with no cache split.
