# PITTIENG - Pitti Engineering Ltd
## Sources read
- companies/PITTIENG.md (origin/main, on_main yes)
- runs/pittieng-2026-09-05/manifest.yaml (155 branches, on_main yes)
- runs/pittieng-2026-09-05/outputs/blocks/B13-synthesis-lite.yaml (on_main yes)
- runs/pittieng-2026-09-05/outputs/final/gate-recommendation.md (on_main yes)
- runs/pittieng-2026-09-05/step1-business-brief.md (on_main yes)
- runs/pittieng-2026-09-05/outputs/reports/05-concall.md (on_main yes; grepped)
- runs/pittieng-q2fy27/notion-payload.md (origin/claude/quarterly-pittieng-q2fy27-3fc1e6, on_main no)
- runs/pittieng-q2fy27/operator_brief_pittieng_q2fy27.md (same branch, on_main no)
- runs/pittieng-q2fy27/work/notion-context.md (same branch, on_main no)
- runs/pittieng-q2fy27/work/review_pittieng_q2fy27.md (same branch, on_main no; over 60 KB, grepped)
- retro/2026-11/excerpts/sessions/PITTIENG.md (session excerpts, lines 1-362)
- retro/2026-11/excerpts/local/PITTIENG.md (local-folder excerpts)

## Company-level facts
- board: NOT FOUND ("NSE PITTIENG / BSE 513519." - companies/PITTIENG.md:3; no file says main board or SME)
- reporting: quarterly - "Q1 FY27 print. Revenue Rs 529 Cr, up 16% YoY." - step1-business-brief.md:30; "Results date: 22-Oct-2026 (Q2 FY27, quarter ended 30-Sep-2026)" - sessions/PITTIENG.md:62
- archetype: "- Archetype: two businesses. Loose-lamination tier = steel converter (~59% of tonnage). Qualified tier = Tier-1 platform supplier (locomotives, gensets, large motors)" - notion-context.md:23-24; "GATE 0 FLAG: classification AVERAGE." - gate-recommendation.md:98; "sector_cap_row: \"Cables / Industrial products\"" - manifest.yaml:8
- first analysis: "# Pitti Engineering — ₹290 cr greenfield + Q4/FY26 results" in analysis/.workspace/2026-05-14_evening_announcements - retro/2026-11/excerpts/local/PITTIENG.md:44-46. First pipeline run: "run_date: 2026-09-05" - manifest.yaml:5
- verdict: "REWORK" - gate-recommendation.md:1; "REWORK judges this analysis, not this company." - gate-recommendation.md:7; "- Halt 1 decision (KILL/SHALLOW/PROCEED): pending" - companies/PITTIENG.md:43; "DRAFT — Step-1 intake only, 2026-09-05. No decision. No entry zone." - companies/PITTIENG.md:13

## Q4 FY26
- base case: NOT FOUND
- guidance: "- FY26 revenue: Rs1,900-2,000 Cr (~Rs1,950 Cr midpoint), reaffirmed Q3 FY26 call" - 05-concall.md:48; "| Q3 FY26 call (PDF p.10) | FY27 EBITDA margin ~17% midpoint, +/-50 bps band |" - 05-concall.md:102
- catalysts: "Greenfield machined-components capex of Rs 290 Cr (Rs 60 Cr spent), casting capacity to 36,000 MT, both commissioning by Q1 FY29." - step1-business-brief.md:37-39; "Capex commissioning is Q1 FY30 per the AR (PDF p.14) and all three calls, Q1 FY29 per Investor Presentation slide 11, unreconciled." - gate-recommendation.md:79-81
- actuals: "- FY26 full year: revenue Rs1,953 Cr (+12%), adjusted EBITDA Rs326 Cr (+20%, margin 17% up from 15.9%)" - 05-concall.md:56; "Q4 FY26 actual 16.6% (Rs84.2 Cr EBITDA on Rs506 Cr revenue, derived from FY26 Rs326 Cr minus 9M Rs241.8 Cr)" - 05-concall.md:102; "PAT Rs 117.8 Cr, DOWN year on year." - step1-business-brief.md:24
- result vs base: NO BASELINE
- management's stated reason: "Q4 FY26: unexecuted Rs20 Cr sales + energy \"Black Swan\" cost spike (Q4 FY26 call, PDF p.8-9)" - 05-concall.md:102
- risk flagged before / by whom / overruled: NOT FOUND

## Q1 FY27
- base case: NOT FOUND
- guidance: "FY28 turnover above Rs 2,500 cr at 90,000 tons with EBITDA margin 17-17.2%, and FY27 EBITDA near Rs 370 cr vs Q1 FY27 Rs 89 cr." - companies/PITTIENG.md:21-22
- catalysts: as Q4 FY26; "Caterpillar data-centre housings in sampling, commercial production guided from Q3 FY27." - notion-context.md:35-36
- actuals: "Revenue is stepping up: 456.56, 477.73, 489.26 (H2 average), 529.09, 578.44. Operating margin is dipping: 16.61% (H2 FY26 average) to 16.32% to 15.36%." - review_pittieng_q2fy27.md:251; "Adjusted EBITDA Rs 89 Cr, up 14%, margin 16.8%. PBT flat at Rs 36.2 Cr. Adjusted PAT Rs 32 Cr vs Rs 26 Cr." - step1-business-brief.md:30-31
- result vs base: NO BASELINE
- management's stated reason: "Q1 FY27: manpower cost front-loaded ahead of capex-driven operating leverage (Q1 FY27 call, Akshay Pitti, PDF p.7)" - 05-concall.md:102
- risk flagged before / by whom / overruled: NOT FOUND. Recorded after the result: "Record that the stated margin mechanism failed in Q1 FY27. Realisation per tonne fell and margin still fell to 16.8%; manpower cost was blamed instead." - gate-recommendation.md:36

## Q2/H1 FY27
- base case: "- FY27E on file: revenue ~Rs 2,300 Cr [MGMT]; EBITDA ~Rs 370 Cr [MGMT]; PAT own build Rs 135-150 Cr, brokers Rs 156-176 Cr" - notion-context.md:32-33. Tripwire: "Q2 FY27 consolidated net debt printing above Rs 491 Cr." - gate-recommendation.md:173; "Falsifier: \"Q2 FY27 castings and machined components volume comes in well under ~4,600 MT.\"" - notion-context.md:45-46
- post-result estimate (not a base case): "| FY27E | 2,215 (run-rate); guide 2,350-2,400 | ... | 126.8 | [FILED, derived] H1 PAT 63.39 x 2 = 126.78 (L209) |" - operator_brief_pittieng_q2fy27.md:38 (written 2026-10-24)
- guidance: [holding detail removed]; export share guided stable to down." - notion-payload.md:17
- catalysts: "approved a capex of ₹450 crores ... The project is proposed to be implemented in phases up to FY 2030-31." - retro/2026-11/excerpts/local/PITTIENG.md:128; "no recovery in FY27, ~Rs 40 Cr/yr from FY28" - notion-payload.md:50
- actuals: "revenue Rs 578.4 Cr (+21.1%), core PBT ex OI +32.6%, PAT Rs 33.9 Cr (-15.5%) on lower other income" - notion-payload.md:17; "H1 operating EBITDA 175.25 / revenue 1,107.53 = 15.82%" - operator_brief:30; "| Q2 FY27 | 578.44 | 15.36% | 43.16 | 41.4 |" - review_pittieng_q2fy27.md:248
- result vs base: "Net debt Rs 538.7 Cr vs Rs 491 Cr = falsifier met ... Castings 3,086 MT vs ~4,600 = falsifier met" - notion-payload.md:17; "Net debt is Rs 539 Cr, above the Rs 491 Cr line we set. That test fails." - operator_brief:17; "**Protocol verdict: PROCEED WITH FLAGS.** Unchanged by the call." - review:480
- management's stated reason: "Maharashtra incentive: no recovery FY27, ~Rs 40 Cr/yr from FY28 per call" - notion-payload.md:17; "Management said this supplier credit will stay and will help pay for four years of new plants." - operator_brief:17
- risk flagged before / by whom / overruled: gate-recommendation.md:173 (B13 Falsification, quoted above); "Watch consolidated net debt every quarter against Rs 491 Cr at 30-Jun-2026." - gate-recommendation.md:162; carried, not overruled: "1. Net debt vs Rs 491 Cr (Company Filing-Event; Signal Health Neutral)." - notion-context.md:40

## Not found
- board
- verdict of the 2026-05-14 local note (excerpt is header only)
- any base case predating Q4 FY26 or Q1 FY27
- base_revenue and base_margin as our own figures (on file only as [MGMT])
- projection_basis for the "PAT own build Rs 135-150 Cr"
- Q4 FY26 quarter PAT
- thesis-broken conditions and Bear/Base/Bull: "ND 'not passed' (no Role 1 / no signed thesis)" - notion-context.md:64-65
