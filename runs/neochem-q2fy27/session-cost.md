# Session cost — NEOCHEM q2fy27 (H1 FY27) (/run-quarterly, batch 2026-10-28, batch 4)

## DOCUMENT REVIEW summary row (shared baseline)

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`NEOCHEM | 2026-10-29 | results (connector-rebuilt copy) + call intimation (A1 only), no concall | 12 (10+2) | ~5,846 (5,054 + 792; fulltext chars / 4) | 857,156 | 1`

- Base run (6 agent runs): 679,039 tokens.
- Correction loop 1 (A3 dispositions + A4 grafts + A5 re-audit): 178,117 tokens. Logged as its own rows below.
- Orchestrator session tokens: NOT MEASURED in-session (not included in total_run_tok).

## Per-agent ledger

Token figures are the harness `subagent_tokens` per agent run. The three loop rows resumed the same agent, whose counter is cumulative; the loop row is the counter after the loop minus the base run.

| Agent | Document / step | Model | total_tok | Wall | Run # | Gate / result |
|---|---|---|---|---|---|---|
| A1 | results | claude-sonnet-5-5 | 55,532 | 116s | 1 | GATE A1 pass, 10/10 pages, R001-R363; text layer (ArialMT); p8 render spot check, 5 values matched |
| A1 | intimation (call notice) | claude-sonnet-5-5 | 36,305 | 41s | 1 | GATE A1 pass, 2/2 pages, I001-I033; A1 only by coordinator instruction |
| A2 | results | claude-sonnet-5-5 | 78,656 | 164s | 1 | GATE A2 pass, 363/363 IDs, zero orphans; ABOVE A1 (diagnosed, see notes) |
| A3 | results | claude-opus-5-5 | 115,213 | 458s | 1 | GATE A3 pass, F1-F17 statused, 20 findings (7 FORWARD-SIGNAL, 11 AMBIGUOUS) |
| A4 | merged review | claude-opus-5-5 | 162,364 | 503s | 1 | PROCEED WITH FLAGS; PRE-THESIS READ; branch 8A-W; 21 questions |
| A5 | audit | claude-opus-5-5 | 230,969 | 1,097s | 1 | INCOMPLETE: 1 FACTUAL, 4 MISSING, 1 CONTRADICTION, 12 STYLE -> loop to A3 then A4 |
| A3 | correction loop 1 | claude-opus-5-5 | 19,400 | 131s | loop 1 | 3 orphan row groups dispositioned |
| A4 | correction loop 1 | claude-opus-5-5 | 76,830 | 401s | loop 1 | F1-F6 accepted and patched; verdict unchanged |
| A5 | re-audit | claude-opus-5-5 | 81,887 | 357s | loop 1 | COMPLETE (4 new STYLE notes S13-S16; drift clean) |

Concurrency: one subagent at a time (6 GB machine, three sibling sessions).

## Notes for the coordinator
- Cost check: A2 (78,656) came in above A1 (55,532). I diagnosed it before A3. A2's task message carried no inputs/ path. The structured file (43,408 bytes) is 2.1x the fulltext (20,216 bytes), so A2's source is larger than the document. AEQUS showed the same pattern. No re-ingestion found. The agent transcript file was empty, so the tool trace could not be read.
- The document is small (10 pages, about 5,000 tokens of text). Fixed agent overhead dominates every row.
- Resuming the A3, A4 and A5 agents for the loop kept the loop at 178,117 tokens, about 26% of the base run.
- Fresh tokens / re-read tokens / re-read multiple: NOT MEASURED in-session (harness reports one total per subagent).
