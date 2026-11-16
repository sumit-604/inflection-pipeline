# CYIENTDLM - Cyient DLM Ltd
## Sources read
- companies/CYIENTDLM.md (origin/claude/baluforge-2026-09-06-runs-ah784w, on_main no)
- runs/cyientdlm-2026-09-06/manifest.yaml, outputs/final/gate-recommendation.md, outputs/reports/05-concall.md (lines 44-89, grep), outputs/reports/01-gate0.md (grep) (153 branches incl. origin/claude/baluforge-2026-09-06-runs-ah784w; on_main yes)
- runs/cyientdlm-q2fy27/notion-payload.md, work/notion-thesis.md, work/narrative_cyientdlm_q2fy27.md, work/run-log.md, work/review_cyientdlm_q2fy27.md (lines 100-129, grep) (origin/run/quarterly-q2fy27-2026-10-17; on_main no)
- retro/2026-11/excerpts/sessions/CYIENTDLM.md (grep)
- retro/2026-11/excerpts/local/CYIENTDLM.md (lines 34-45, header grep)

## Company-level facts
- board: NOT FOUND. Nearest: "Company listed 2023 (recently listed): IPO prospectus is a HIGH-priority gap" - runs/cyientdlm-2026-09-06/manifest.yaml:10; "Sector: EMS / Aerospace and Defence electronics (BSE 543933)." - runs/cyientdlm-q2fy27/work/notion-thesis.md:14
- reporting: quarterly. "| Revenue from Operations (res L538) | 310.63 | 373.80 | 393.09 | 589.06 | 766.89 | 1,261.49 | ND |" (Q2 FY26 / Q1 FY27 / Q2 FY27 columns) - runs/cyientdlm-q2fy27/work/review_cyientdlm_q2fy27.md:106
- archetype: `sector_cap_row: "Cables / Industrial products"` - manifest.yaml:8; "Classification AVOID. Grand total 47 of 160 as reported" - gate-recommendation.md:107; "archetype rung (R2 vs QUALIFIED CAPACITY PROVIDER at R1/R2)" (open ruling) - notion-thesis.md:37
- first analysis: "# Cyient DLM (CYIENTDLM) — Q1FY27 Call Transcript — Filed 24-Jul-2026 (call 21-Jul)" in analysis\.workspace\feed_2026-07-24_1722\Cyient_DLM_results.md - retro/2026-11/excerpts/local/CYIENTDLM.md:39-41; pipeline "run_date: 2026-09-06" - manifest.yaml:5
- verdict: gate file line 1 "REWORK"; "REWORK judges the analysis. It does not judge the company." - gate-recommendation.md:11; "## HALT 1 GATE / Not reached." - companies/CYIENTDLM.md:28-29

## Q4 FY26
- base case: NOT FOUND. "Stages 10 and 11 did not run. There is no valuation in this run." - gate-recommendation.md:5
- guidance: "| Revenue YoY growth resumption | positive YoY growth | Q4 FY26 | Q2 FY26 call p.5-6; reaffirmed Q3 FY26 call p.9,16 |" - runs/cyientdlm-2026-09-06/outputs/reports/05-concall.md:49; "| NWC normalisation | \"better NWC levels\" | by end of Q4 FY26 | Q3 FY26 call, 20-Jan-2026, p.8 |" - :50
- catalysts: as guidance; "Q4 FY26 order intake to rebound to the ~Rs500cr/quarter level seen in Q1-Q2 FY26" - 05-concall.md:88
- actuals: "Q4 FY26 revenue INR3,691mn, DOWN 13.8% YoY (Q4 FY26 call p.6-7) | MISSED" - 05-concall.md:85; "Deck Q3 + Q4 EBITDA 309 + 431 = 740 Mn" - review_cyientdlm_q2fy27.md:277; "the deck PAT chart gives Q3 FY26 138 and Q4 FY26 224 (pres L269, L271, positional read)" - :278; FY26 revenue 1,261.49, PAT 73.28 - :106, :120
- result vs base: NO BASELINE
- management's stated reason: "West Asia war delaying materials/approvals, NPA approvals from customers delayed, memory-component lead times (Q4 FY26 call p.11) — three external factors, no internal-planning admission" - 05-concall.md:85
- risk flagged before / by whom / overruled: NO (no analysis of ours predates the result)

## Q1 FY27
- base case: NOT FOUND
- guidance: "| FY27 revenue growth | 20%-25%, \"no doubt\" | FY27 | Q3 FY26 call p.15 (Deepak Lalwani exchange) |" - 05-concall.md:52; "Q4 FY26 (Disha, p.13: \"25%-50% fair assumption?\" — RMS: \"we will not be giving any guidance\")" - :123
- catalysts: "| BTS revenue share FY27 | double-digit % | FY27 | Q3 FY26 call p.16; reaffirmed Q4 FY26 call p.14 |" - :54; "| NWC target (restated after the Q4 miss) | 100-120 days | \"a couple of years\" | Q4 FY26 call, 21-Apr-2026, p.16 |" - :51
- actuals: revenue 373.80, PAT 16.29 - review_cyientdlm_q2fy27.md:106, :120; "late, in Q1 FY27 (+34.3% YoY, 10.5% EBITDA margin, PAT +118% YoY)" - 05-concall.md:222; "normalized EBITDA margin 10.5% (4th straight double-digit quarter)" - retro/2026-11/excerpts/local/CYIENTDLM.md:42
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NO (no analysis of ours predates the result)

## Q2/H1 FY27
- base case: NOT FOUND. "Thesis-broken conditions: ND (none signed). Bear/Base/Bull projections: ND." - notion-thesis.md:40; "| Revenue (Q2 FY27 / H1 FY27, Rs Cr) | ND | ND | ND | 393.09 / 766.89 (res L538) | ND (no projections) |" - review_cyientdlm_q2fy27.md:435
- our falsification line (not a revenue base): "Q2 FY27 consolidated net working capital days printing above 161 alongside negative operating cash flow for the quarter." - gate-recommendation.md:174
- named tests: "Cash falsifier: consolidated NWC days <=120 by Q4 FY27 disclosure with positive CFO falsifies STRUCTURAL; \"any print above 161 days confirms it\"." - notion-thesis.md:27
- guidance: 05-concall.md:123 (no guidance); after the result: "Guidance: FY27 EBITDA \"close to 9%\" / \"9-10%\" ... FY27 revenue 30-35%, H2 >30%" - runs/cyientdlm-q2fy27/notion-payload.md:64
- catalysts: "| BTS margin uplift | +250-300 bps consolidated EBITDA | next 12-18 months | Q1 FY27 call, 21-Jul-2026, p.14 |" - 05-concall.md:55; "| Semiconductor capital-equipment vertical revenue | material P&L contribution in 6-12 months | from Q1 FY27 |" - :63; "| Aerospace OEM ramp (Honeywell) | ramp-up within 18 months | from Q1 FY27 |" - :62
- actuals: "revenue Rs393.09 Cr +26.5% YoY; op EBITDA margin 8.69% (-135 bps); gross margin 37.41% (-381 bps YoY, third compression on the Notion count ...). Reported PAT Rs34.01 Cr, of which Rs18.20 Cr (53.5%) is an earnout write-back" - notion-payload.md:15; H1 766.89 / PAT 50.30 - review_cyientdlm_q2fy27.md:106, :120; "| EBITDA Margin (operating) | ND | ND | ND | 8.69% Q2 / 9.56% H1 | ND |" - :436
- result vs base: NO BASELINE. Tests as stated: "Cash falsifier: needs NWC basis ruling (filing 189.0 days, deck 153, Notion 169 not reproducible). Tests: 2 RED (prov), 4 margin leg RED, 6 US leg RED, 3 GREEN, 1 AMBER, 5 UNKNOWN. Verdict PROCEED WITH FLAGS." - notion-payload.md:15
- management's stated reason: "| 52 | Margin causes: \"revenue mix and certain product development related costs\"; employee cost for sales | Backward | NO | cc L158-L159 |" - review_cyientdlm_q2fy27.md:778; "mgmt cause mix + product development, no component-cost answer" - notion-payload.md:15
- risk flagged before / by whom / overruled: YES. "8. Watch the gross margin explanation on the next call. Peers disclosed a component and PCB cost shock in the same January to June 2026 window and the company did not ... This is the CRITICAL item stage 5 missed." - gate-recommendation.md:170; by Verifier B: "One of the eleven is CRITICAL: a repeated evasion on gross margin compression across more than two quarters" - gate-recommendation.md:24. Not overruled (carried as monitorable 8).

## Not found
- board (SME / main)
- verdict of the 2026-07-24 call note (headline-only excerpt)
- any base case, projection basis (all three periods): "Bear/Base/Bull projections: ND"
- Q4 FY26 margin %; Q1 FY27 management reason
