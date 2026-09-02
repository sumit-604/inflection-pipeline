# INDIAGLYCO Demerger Document Review 2026-09-02 — Session Cost Ledger

Three-deck document review (India Glycols three-way demerger). Totals from
subagent result metadata (total_tok, wall).

## DOCUMENT REVIEW SUMMARY ROW (shared baseline)
| ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations |
|--------|------|---------|-------|-----------------------|---------------|-----------------|
| INDIAGLYCO | 2026-09-02 | presentation x3 (demerger) | 78 | 42,358 | 1,212,068 | 1 |

Three presentations reviewed as one merged object: corporate (residual India
Glycols, 32p), IGL Spirits (31p), Ennature Biopharma (15p). `a1_extracted_text_tok`
is the sum of the three A1 fulltexts (corp ~16,710 + spirits ~18,107 + eb ~7,540).
All text-layer, text-only, zero pages rendered.

## PER-AGENT LEDGER (base run)
| agent | doc | model | total_tok | wall |
|-------|-----|-------|-----------|------|
| A1 extractor | corp | sonnet | 142,788 | 700s |
| A1 extractor | spirits | sonnet | 135,296 | 1145s |
| A1 extractor | eb | sonnet | 105,151 | 537s |
| A2 enumerator | corp | sonnet | 76,244 | 241s |
| A2 enumerator | spirits | sonnet | 61,426 | 174s |
| A2 enumerator | eb | sonnet | 51,170 | 182s |
| A3 forensics | corp | opus | 79,607 | 266s |
| A3 forensics | spirits | opus | 79,721 | 233s |
| A3 forensics | eb | opus | 58,874 | 192s |
| A4 analyst (merged, Document Review Protocol v1.1) | all | opus | 125,874 | 425s |
| A5 adversary (merged) | all | opus | 140,860 | 399s |
| | | BASE SUBTOTAL | 1,057,011 | |

## CORRECTION LOOP (Point 9; logged separately)
| agent | model | total_tok | wall | iter |
|-------|-------|-----------|------|------|
| A4 analyst (loop-1 fix) | opus | 66,688 | 246s | 1 |
| A5 adversary (loop-1 re-audit) | opus | 88,369 | 158s | 1 |
| | LOOP SUBTOTAL | 155,057 | | |

A5 base verdict INCOMPLETE on one FACTUAL arithmetic error (IGL Spirits
realisation/case 10x, non-load-bearing); one loop iteration fixed it; A5
re-audit COMPLETE.

## RUN TOTAL
BASE 1,057,011 + LOOP 155,057 = **1,212,068 tokens** (1 loop iteration).
~404k per deck on a merged three-entity thesis check. Extraction text-only,
row-ID de-dup, framework scoped to Document Review Protocol v1.1.

## OUTCOME
Process verdict PROCEED WITH FLAGS; Decision Status holds WATCHLIST / AVOID
(DEEP WATCH), no thesis-broken trigger fires. Coverage 798/798 disclosure units,
zero orphans across three ledgers. Load-bearing findings: residual-IGL Adj.
EBITDA bridge insufficient by 66-114 Cr; corp page-7 Spirits/Ennature
transposition; 8 of 9 thesis variables remain open (real evidence = filed
opening balance sheets Oct-Nov 2026 and Ennature guar-free Q2 FY27).
