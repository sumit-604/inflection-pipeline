# DDEVPLSTIK - DDev Plastiks Industries Ltd
## Sources read
- companies/DDEVPLSTIK.md (origin/claude/run-pipeline-ddevplstik-405lmq, on_main no)
- runs/ddevplstik-2026-07-23/manifest.yaml, outputs/final/gate-recommendation.md (top + grep), outputs/reports/B11.md (grep + lines 108-147), B05.md (grep), B10.md (grep), B01.md (grep), B14.md (grep), B15.md (grep) (287 branches, on_main yes)
- runs/d-dev-q1fy27/work/review_d-dev_q1fy27.md (first 70 lines + grep) (origin/claude/d-dev-quarterly-analysis-jnyqb1, on_main no) - DIFFERENT COMPANY, see below; not used
- runs/deedev-2026-11-15/manifest.yaml (origin/run/deedev-2026-11-15, on_main no) - DIFFERENT COMPANY, see below; not used
- scratchpad sessions/DDEVPLSTIK.md (all 4 entries; all refer to "DEE Development")
- scratchpad retro/2026-11/excerpts/local/DDEVPLSTIK.md (1 excerpt, a 2026-05-17 _rejected list with no DDev Plastiks line in the excerpt)

## Packet mis-grouping (fact)
- "# Q1 FY27 MERGED QUARTERLY REVIEW — DEE Development Engineers Ltd" / "**Ticker:** D-DEV | NSE DEEDEV | BSE 544198" - runs/d-dev-q1fy27/work/review_d-dev_q1fy27.md:1-2
- "company: DEE Development Engineers Ltd" / "ticker: DEEDEV" - runs/deedev-2026-11-15/manifest.yaml:1-2
- "company: DDev Plastiks Industries Ltd" / "ticker: DDEVPLSTIK" - runs/ddevplstik-2026-07-23/manifest.yaml:1-2
- Only runs/ddevplstik-2026-07-23 concerns DDev Plastiks. No quarterly review folder for DDev Plastiks is in the packet.

## Company-level facts
- board: NOT FOUND
- reporting: quarterly. "TRANSCRIPT_3 (Concall_May_2026_Transcript.pdf) = **Q4 FY26 / full year** (quarter and year ended 31-Mar-2026), call held 26-May-2026." - runs/ddevplstik-2026-07-23/outputs/reports/B05.md:7; guidance history cites "Q2, Q3, Q4 FY26 calls" - B05.md:44
- archetype: "Approved destination exit PE base at 25x (Cables and Industrial products sector cap), declining the 35x specialty chemicals alternative. Reasoning: cost plus polymer compounder at an 11% EBITDA margin" - companies/DDEVPLSTIK.md:12; "manifest sector row auto-picked Pharma / CDMO 38x (wrong; corrected to Cables / Industrial products 25x)" - companies/DDEVPLSTIK.md:30; "Gate 0 Classification | GOOD (capped by Block B cash deal-breaker, Block B 7/20)" - runs/ddevplstik-2026-07-23/outputs/reports/B14.md:37
- first analysis: [holding detail removed]; `run_date: 2026-07-23` - manifest.yaml:5
- verdict: "PROCEED WITH CAVEATS" - runs/ddevplstik-2026-07-23/outputs/final/gate-recommendation.md:1; "VERDICT:     BUY (at the margin-of-safety floor)" - B14.md:133
- devil's advocate: `overall: "WEAKENED BUT ALIVE"` - runs/ddevplstik-2026-07-23/outputs/reports/B15.md:168; "the devil's honest alternative is WATCHLIST until the FY27 Q1 working-capital print" - companies/DDEVPLSTIK.md:9
- projection basis: "Base = lower of (mgmt +13% guidance discounted for grade B) and near-historical (~10-11%) → 11%." - runs/ddevplstik-2026-07-23/outputs/reports/B11.md:118; "Base 11% needs ~73% FY27 utilization (from ~64%); capacity ~315k MTPA already installed" - B11.md:158

## Q4 FY26
- base case: NOT FOUND (first workup 2026-07-23 is after this result)
- guidance: "FY26 volume 210,000–220,000 MT | ❌ **Missed** — FY26 production 201,370 MT" - B05.md:79; "FY26 revenue Rs2,850–2,950 Cr | ✅ **Delivered** — FY26 revenue ~Rs2,948–2,953 Cr" - B05.md:80; "FY26 EBITDA margin 10–12% | ✅ **Delivered** — ~11%" - B05.md:81
- catalysts: "BESS FY27 revenue | Rs300–500 Cr (Q3 call) → cut to Rs200–250 Cr (Q4 call)" - B05.md:48; "BESS Phase-1 capex | Rs150 Cr | Phase-1 | Q3 FY26 call; revised to ~Rs200 Cr, Q4 FY26 call" - B05.md:46; "Adani/UltraTech PVC offtake to begin Q1 CY2026 / worst case Q1 FY27 | **Unconfirmed**" - B05.md:85
- actuals (full year only): "Year 0 core revenue FY26 = **Rs 2,947.87 Cr** (Results Q4 FY26 p.7, via B10)." - B11.md:110; "PAT (Rs Cr) | 201.82 | ~224.1 | 276.17" - B11.md:137; "FY24 PAT margin 7.48%, FY25 7.13%, FY26 6.85% (B10)" - B11.md:130. Q4 FY26 quarter figures: NOT FOUND
- result vs base: NO BASELINE
- management's stated reason: "Israel-Iran conflict from 28-Feb-2026 disrupted exports/RM and dampened demand via price pass-through; management states volume growth "would have approached 10%" ex-shock vs. delivered 6%" - B05.md:79
- risk flagged before / by whom / overruled: NOT FOUND (no analysis predates the result)

## Q1 FY27
- base case: "Revenue (Rs Cr) | 2,947.87 | 3,272.14 | 4,031.68" - B11.md:136; "(FY27 base uses 11% CAGR: 2947.87×1.11 = 3272.14; PAT 3272.14×6.85% = 224.14; EPS 224.14/10.36 = 21.63." - B11.md:143; "PAT margin | 6.0% | 6.85% | 7.5%" - B11.md:126
- guidance: "FY27 core guidance | Volume 231,000 MT (~15%), revenue growth ~13%, EBITDA margin ~11%, utilization ~73% (BESS excluded) | FY27 | Q4 FY26 call" - B05.md:52; "**FY27 (Guided)** | +13% ≈ Rs 3,340 Cr core (ex-BESS) | ~11%" - runs/ddevplstik-2026-07-23/outputs/reports/B10.md:334
- catalysts: "BESS Phase-1 commissioning (guided H2 FY27) and FY27 revenue against the twice-cut Rs 200 to 250 Cr band." - gate-recommendation.md:51; "FY27 total capex | Rs175 Cr (~Rs100 Cr core + ~Rs70+ Cr BESS)" - B05.md:53; "FY30 core revenue target | Rs5,000 Cr | FY30" - B05.md:44; "220 kV XLPE | Targeted 2029/2030" - B05.md:43
- actuals: NOT FOUND (no DDev Plastiks Q1 FY27 result in the packet)
- result vs base: BASELINE NOT COMPARABLE (base exists, no actual found, no file states a comparison)
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NOT FOUND (no result to test). Risks on file before any FY27 print: "Net working capital days above 90 on flat or below-231,000 MT annualised volume for two consecutive quarters (structural cash drag confirmed) = thesis broken." - companies/DDEVPLSTIK.md:18; "DDev's claim that the raw-material shock "normalized by April 2026" is contradicted by Apcotex's own 7-May-2026 commentary" - gate-recommendation.md:43

## Q2/H1 FY27
- base case: same FY27E base as above - B11.md:136-143
- guidance: same Q4 FY26 call guidance - B05.md:52
- catalysts: "BESS pre-EBITDA-visibility (recognition starts H2 FY27, initial margins 5-8%)" - B11.md:20; gate-recommendation.md:51 as above
- actuals: NOT FOUND
- result vs base: BASELINE NOT COMPARABLE (base exists, no actual found, no file states a comparison)
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NOT FOUND

## Not found
- board (SME / main)
- Q4 FY26 quarter revenue, margin, PAT (only full-year FY26 found)
- Q1 FY27 and Q2/H1 FY27 actual revenue, margin, PAT for DDev Plastiks
- any quarterly review of DDev Plastiks (the two later folders in the packet are DEE Development Engineers)
- result-vs-base statement, management reason, risk flagged / flagged_by / overruled for Q1 and Q2
