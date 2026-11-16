# SMRUTHI - Smruthi Organics Ltd
## Sources read
- Company memory file: NOT FOUND on any branch (per packet)
- runs/smruthi-2026-07-09/manifest.yaml (315 branches, on_main yes)
- runs/smruthi-2026-07-09/outputs/blocks/B01.yaml, B05.yaml (lines 9-36), B11.yaml; B00/B10 by grep (on_main yes)
- runs/smruthi-2026-07-09/outputs/reports/11-valuation.md (lines 138-193 plus grep), 05-concall.md (grep) (on_main yes)
- runs/smruthi-2026-07-09/outputs/final/fttcp-recommendation.md (on_main yes)
- retro/2026-11/excerpts/sessions/SMRUTHI.md (one excerpt, 2026-09-15, prompt-audit mention only)
- retro/2026-11/excerpts/local/SMRUTHI.md (local-folder excerpts; retro/2026-11/excerpts/local/SMRUTHI.md does not exist)

## Company-level facts
- board: NOT FOUND (no file states SME or main board; local notes refer to a "BSE feed" only)
- reporting (quarterly): "Smruthi Organics | Board meeting intimation | Board meeting 10 Aug for Q1 unaudited results — scheduling only" - C:/ConcallPipeline/Daily Concall Intelligence\analysis\.workspace\feed_2026-07-30_1323\_rejected.md (retro/2026-11/excerpts/local/SMRUTHI.md:28)
- archetype: `sector_cap_row: "Pharma / CDMO"` - runs/smruthi-2026-07-09/manifest.yaml:8; `classification: "AVOID"` - outputs/blocks/B01.yaml:16; "FTTCP ROCE forward verdict not carried by B10 (NO-CONCALL MODE) -> conservative DECLINING" - outputs/blocks/B11.yaml:9
- first analysis: `run_date: 2026-07-09` - manifest.yaml:5
- verdict: "PROCEED WITH FLAGS" - outputs/final/fttcp-recommendation.md:1; "Decision: AVOID (on valuation)." - fttcp-recommendation.md:7

## Q4 FY26
- base case: NOT FOUND (first analysis 2026-07-09 is after the FY26 result)
- guidance: `promise: "Stronger revenue contributions from China/Russia, continued export momentum, growth should improve", outcome: "MISSED - revenue fell ~19.1% YoY FY26 (Rs.10,196.71L vs Rs.12,600.79L), decline worsened through the year (9M -17.1%, Q4 alone -23.6%)"` - outputs/blocks/B05.yaml:29
- catalysts: `promise: "ANVISA (Brazil)/EDQM (Europe) inspections in FY25-26, critical milestones", outcome: "NOT VERIFIABLE - no status update in Q3 or Q4 FY26 results filings"` - outputs/blocks/B05.yaml:32
- actuals: "| Revenue (Cr) | 101.97 | 107.07 | 112.42 | 118.05 |", "| EBITDA (Cr) | 11.46 | ...", "| EBITDA margin | 11.25% | ...", "| PAT (Cr) | 3.43 | ..." (Year 0 = FY26) - outputs/reports/11-valuation.md:167-170; "Tests monitor #1 (green ≥₹27 Cr, red <₹23 Cr; Q1 ₹29.30 Cr, Q4 ₹29.1 Cr)" - C:/ConcallPipeline/Daily Concall Intelligence\announcements\2026-11-04_0500_to_2026-11-05_0405\REVIEW.md (retro/2026-11/excerpts/local/SMRUTHI.md:174). Q4 quarter margin and PAT: NOT FOUND
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND. `explanation: "None given in any FY26 results filing"` - outputs/blocks/B05.yaml:29
- risk flagged before / by whom / overruled: NOT FOUND (no analysis predates the result)

## Q1 FY27
- base case: "| Revenue (Cr) | 101.97 | 107.07 | ...", "| EBITDA margin | 11.25% | 11.5% | ...", "| PAT (Cr) | 3.43 | 3.7 | ..." (Year 1) - outputs/reports/11-valuation.md:167-170; "| Revenue CAGR | **-8%** | **+5%** | **+9%** (= SOM ceiling) |" - 11-valuation.md:147; base logic "Partial stabilisation, cost-rationalisation holds, no new export ramp" - 11-valuation.md:146
- guidance: NOT FOUND
- catalysts: `name: "Revenue recovery - China/Russia export momentum" ... confirm_signal: "Reversal of ~19% FY26 revenue decline in FY27 results; management finally explains the miss"` - outputs/blocks/B05.yaml:11
- actuals: "Q1 FY27 sales of ₹29.30 Cr cleared the ₹27 Cr green line (Notion, 08-Oct review)." - C:/ConcallPipeline/Daily Concall Intelligence\announcements\2026-11-12_0500_to_2026-11-13_0500\REVIEW.md (retro/2026-11/excerpts/local/SMRUTHI.md:279). Q1 margin and PAT: NOT FOUND
- result vs base: BEAT, file-stated (quote above). Arithmetic share: Rs 29.30 Cr = 27.4% of FY27E Rs 107.07 Cr
- management's stated reason: NOT FOUND
- risk flagged before: YES (as the confirm signal for the revenue monitor). "Revenue trend, China and Russia export line. Threshold: any reversal of the negative 19.1% FY26 decline confirms, continued or deeper decline kills." - runs/smruthi-2026-07-09/outputs/final/fttcp-recommendation.md:50
- by whom: Stage 13 synthesis monitorable 1 (from B05 trigger 1)
- overruled: NOT FOUND

## Q2/H1 FY27
- base case: same FY27E (Year 1) lines - outputs/reports/11-valuation.md:167-170
- guidance: NOT FOUND
- catalysts: "CBPF issued under RE No. 4,179 of 22-Oct-2026, published 26-Oct-2026, valid to 26-Oct-2028" - C:/ConcallPipeline/Daily Concall Intelligence\announcements\2026-11-12_0500_to_2026-11-13_0500\deep\out\T19.md (retro/2026-11/excerpts/local/SMRUTHI.md:347); "Smruthi now holds two regulated-market approvals, the EU CEP (09-Mar-2026) and the ANVISA CBPF." - announcements\2026-11-12_0500_to_2026-11-13_0500\REVIEW.md (retro/2026-11/excerpts/local/SMRUTHI.md:279)
- actuals: "Q2 FY27 revenue ₹30.71 Cr, PBILDT 14.2%; H1 ₹60.01 Cr, 17.0%." - C:/ConcallPipeline/Daily Concall Intelligence\announcements\2026-11-13_0500_to_2026-11-14_1524\deep\out\T18.md (retro/2026-11/excerpts/local/SMRUTHI.md:498). PAT: NOT FOUND
- result vs base: BEAT, file-stated. "H1 clears monitors #1, #2 and CARE line; Q2 weaker; Notion \"net cash ₹14 Cr\" is a lakh/crore error, actual net debt ~₹7.3 Cr." - same T18.md (retro/2026-11/excerpts/local/SMRUTHI.md:494). Arithmetic share: H1 Rs 60.01 Cr = 56.0% of FY27E Rs 107.07 Cr
- management's stated reason: NOT FOUND
- risk flagged before: YES. "a confirmed ANVISA or EDQM regulated market approval accompanied by disclosed first regulated market export revenue. That is the one catalyst B11 names as the risk to AVOID." - runs/smruthi-2026-07-09/outputs/final/fttcp-recommendation.md:61
- by whom: Stage 11 valuation (B11) and Stage 13 synthesis falsification line
- overruled: NO. Carried in the final recommendation (line 61); "ANVISA/EDQM outcomes unresolved -> no regulatory catalyst credited" - outputs/blocks/B11.yaml:13
- related later facts: "Smruthi's 09-Jul file said the ANVISA inspection was \"never scheduled\" four weeks after it ended." - announcements\2026-10-21_0500_to_2026-10-22_0500\REVIEW.md (retro/2026-11/excerpts/local/SMRUTHI.md:58); "Smruthi Organic: Mar-26 cash and investments were ₹2.47 Cr, not ₹22.29 Cr; the record's \"net cash ₹14 Cr\" is a lakh/crore error." - announcements\2026-11-13_0500_to_2026-11-14_1524\REVIEW.md (retro/2026-11/excerpts/local/SMRUTHI.md:416)

## Not found
- board
- company memory file
- mgmt_guidance for Q1 FY27 and Q2/H1 FY27
- Q4 FY26 quarter-only margin and PAT
- Q1 FY27 margin and PAT; Q2/H1 FY27 PAT
- mgmt_reason (all periods)
