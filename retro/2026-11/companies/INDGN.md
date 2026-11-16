# INDGN extraction excerpts

## Identity & first analysis
### origin/main:runs/indgn-2026-08-03/manifest.yaml
run_date: 2026-08-03 / run_type: full / sector_cap_row: "Pharma / CDMO" ("Sector row auto-picked; verify.")
### origin/main:runs/indgn-2026-08-03/outputs/final/gate-recommendation.md:1,5
PROCEED WITH FLAGS ... Verdict selection rule 3 fired: FLAG-CASH is active, and its determination is GROWTH-INDUCED, which permits PROCEED and carries a single falsifying metric.
### origin/main:companies/INDGN.md:11-20 (origin/main:companies/INDGN.md)
the whole BUY turns on one print, whether operating margin expands sequentially from 16.4% toward ~20% by H2 FY27
2026-08-03: BUY (on-dips) on the operator-approved base; evidence gate PROCEED WITH FLAGS, confidence overall 79. Entry Rs 534-668 (additive) / Rs 477-596 (RRM), MoS Rs 534. ... sector cap Platform/SaaS/IT services 45x

## Our base case
### origin/main:runs/indgn-2026-08-03/outputs/final/fttcp-draft.md:203-206
The FY27 to FY31 columns are illustrative, built from the Q1 FY27 run rate and the market sizing work, not from guidance. Management gives no revenue guidance as a stated policy
### QuarterlyReviewer/reviews/2026-10-30_1025/INDGN/REVIEW.md:427-432 (Step 6A)
| Revenue | 4,250 | 4,400 | 4,600 | H1 2,185.4; x2 = 4,371 | Base to Bull, but FX-aided.
| EBITDA margin (deck basis) | 16.9% | 17.2% | 17.5% | 16.78% ... | **Below Bear**
| PAT | 445 | 490 | 540 | 228.5; x2 = 457 | Bear to Base
### origin/claude/run-pipeline-indgn-6wej1t:runs/indgn-q1fy27/work/review_indgn_q1fy27.md:226
The injected thesis supplies the destination-PE / entry / MoS spine and the qualitative FY27 path ... but not numeric Bear/Base/Bull revenue/margin/PAT bands -> those cells ND (not estimated).

## Guidance & catalysts
### QuarterlyReviewer/reviews/2026-10-30_1025/INDGN/NARRATIVE.md
Our thesis says the story rests on one thing: operating margin recovering to 19-20% by Q4 FY27 ("the margin print is the whole thesis"). Our FY27 base case was revenue 4,400 Cr, EBITDA margin 17.2% and profit 490 Cr.
8. The 19-20% target was not repeated. None of the three documents state it in text.
### origin/claude/run-pipeline-indgn-6wej1t:runs/indgn-q1fy27/work/review_indgn_q1fy27.md:476
Margin timeline hardened to exactly 6 qtrs / 19-20% by Q4 FY27 | Forward guidance

## Actuals by period
### Q4 FY26 - origin/claude/run-pipeline-indgn-6wej1t:runs/indgn-q1fy27/work/review_indgn_q1fy27.md:68,84,173
| Revenue from Operations | 760.8 | 1,003.4 | 1,063.1 | 3,510.5 |  (Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26)
| PAT | 116.4 | 79.7 | 116.2 | 401.1 |
| Q4 FY26 | 1,003.4 | 16.31% | 16.4% | 94.3 | -240 bps MTM drag (Turn 4); Rs 20.3 cr TCPA exceptional
### Q1 FY27 - origin/claude/run-pipeline-indgn-6wej1t:runs/indgn-q1fy27/work/review_indgn_q1fy27.md:103,144-153
Q1 FY27 EBITDA margin reads as 16.9% (management/deck, +50 bps QoQ), 16.4% (operating, ex-all-other-income, +8 bps QoQ), and ~190 bps DOWN on the honest ex-MTM basis the CFO himself [conceded]
| Revenue from Operations | 760.8 | 1,063.1 | +39.7% |  /  | PAT | 116.4 | 116.2 | -0.2% |
### Q2 FY27 - QuarterlyReviewer/reviews/2026-10-30_1025/INDGN/NARRATIVE.md
Revenue was 1,122 Cr, up 39.6%... Operating EBITDA margin ... was 16.55%, against 16.39% last quarter ... A year ago it was 17.48%. Net profit was 112 Cr, up 10% on last year but down 3.4% on last quarter.
Cash from operations for the first half was minus 13.3 Cr, against plus 203 Cr a year ago.

## Risk flags & rulings
### origin/main:runs/indgn-2026-08-03/outputs/final/fttcp-recommendation.md:86
a Hurdle Ratio can PASS while double-crediting a single assumed improvement ... the 2.12 PASS becomes a 1.56 FAIL the moment the Hurdle is rebuilt on the no-recovery bear FY27 EPS of Rs 17.51.
### origin/claude/run-pipeline-indgn-6wej1t:runs/indgn-q1fy27/work/run_log.md (tripwires)
3. Consolidated OCF/PAT below 1.0x with receivables ex-BioPharm outgrowing revenue ex-acquisition (FLAG-CASH growth-induced -> structural).
### origin/claude/run-pipeline-indgn-6wej1t:runs/indgn-q1fy27/work/review_indgn_q1fy27.md:600
Decision Status: UNCHANGED (BLANK / BUY-on-dips, Tier B). Flag only - no change.
### origin/main:runs/indgn-2026-08-03/outputs/final/fttcp-deliberation.md:12-13
The operator engaged the valuation base and did not dispute any transition verdict or the composite, so the transition rulings stand

## Session-history excerpts
### session:2026-10-30|C--QuarterlyReviewer-QuarterlyReviewer-reviews-2026-10-30-1025\717bb050-7f4a-4c0b-8574-29f1232c65fd.jsonl
Our base case for FY27 was revenue of Rs4,400 Cr, EBITDA margin of 17.2% and profit of Rs490 Cr. The test for this quarter was a margin of at least 16.4% to count as bull, and below 16.0% counted as bad.
### session:2026-10-30|...786fa239-e49a-48d5-b472-a43ffe897891.jsonl
INDGN is the clearest worry. It just passed its margin test at 16.55%, but only because of a small side unit and currency gains. The core businesses lost margin, and cash flow for the half-year was negative.
