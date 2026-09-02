# MANINDS Corporate Presentation 2026-09-01 — Session Cost Ledger (DOCUMENT REVIEW)

Document-review token ledger. One row per subagent run. Totals from subagent
result metadata (total_tok and wall recorded; in/out split not exposed).

## DOCUMENT REVIEW SUMMARY ROW (the shared baseline)
| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|--------|------|---------|-------|-----------------------|---------------|-----------------|
| MANINDS | 2026-09-01 | presentation | 37 | 19,194 | 604,081 | 1 |

`a1_extracted_text_tok` = A1 fulltext size (the document's own text, ~19k;
the ~9k-word deck the prior run inflated to ~60k with page images). This run
rasterised nothing (text layer present, text-only).

## PER-AGENT LEDGER (base run)
| # | agent | model | total_tok | wall | run# |
|---|-------|-------|-----------|------|------|
| A1 | extractor | sonnet | 41,188 | 113s | 1 |
| A2 | enumerator | sonnet | 91,300 | 345s | 1 |
| A3 | forensics | opus | 85,430 | 266s | 1 |
| A4 | analyst (doc-review protocol) | opus | 76,005 | 311s | 1 |
| A5 | adversary | opus | 109,647 | 347s | 1 |
| | BASE SUBTOTAL | | 403,570 | | |

## CORRECTION LOOP (Point 9; logged separately)
| # | agent | model | total_tok | wall | iter |
|---|-------|-------|-----------|------|------|
| A4 | analyst (loop-1 fix) | opus | 99,729 | 314s | 1 |
| A5 | adversary (loop-1 re-audit) | opus | 100,782 | 176s | 1 |
| | LOOP SUBTOTAL | | 200,511 | | |

A5 base verdict INCOMPLETE (1 FACTUAL sign error + 2 MISSING items, all bearish);
one loop iteration fixed them; A5 re-audit COMPLETE. STYLE finding logged, no loop.

## RUN TOTAL
BASE 403,570 + LOOP 200,511 = **604,081 tokens** (1 loop iteration).
Prior run (same deck, with 1 loop): ~775,000. This run: ~22% lower.

## NOTES FOR THE BASELINE
- A1 ran lean this pass (41,188) and under-captured 10 footnote/qualifier units;
  A2 recovered every one via MISSING_FROM_STRUCTURED (MF01-MF10, zero orphan
  IDs), which is why A2 (91,300) exceeded A1 — the A2<A1 cost-check tripwire
  firing. A thorough A1 pass elsewhere ran ~145k with A2 then ~65k. A1
  thoroughness varies run to run; the chain preserves completeness either way.
- Structural cuts measured in isolation (A3+A4+A5): framework scoping -60,339;
  ledger row-ID de-dup -53,413; combined 353,905 -> 240,153.
- Completeness held: 5/5 gate data points captured, every prior red flag
  preserved, NPC ~2.7x acquisition-economics question raised, every A1 row ID
  (R001-R335) referenced, zero orphans.
