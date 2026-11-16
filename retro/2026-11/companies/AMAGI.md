# AMAGI - Amagi Media Labs Ltd

## Sources read
- companies/AMAGI.md (origin/main, on_main yes)
- runs/amagi-2026-07-12/manifest.yaml; outputs/blocks/B01-gate0.yaml (grep), B05-concall.yaml (grep), B11-valuation.yaml, B13-synthesis.yaml, B14-thesis.yaml, B15-devil.yaml; outputs/reports/B11.md (Section 2 + grep) (312 branches, on_main yes)
- runs/amagi-q1fy27/work/review_amagi_q1fy27.md (lines 1-130, 234-273 + grep) (origin/claude/quarterly-results-analysis-rnbvw5, on_main no)
- retro/2026-11/excerpts/sessions/AMAGI.md (first 60 lines; framework-check and KWICK precedent mentions only)
- retro/2026-11/excerpts/local/AMAGI.md (local Concall-pipeline excerpts, grep + targeted reads)
- LESSONS.md / LESSONS_ARCHIVE.md (grep; matching lines too long to display, not used)

## Company-level facts
- board: NOT FOUND. Only: "Fresh issue Rs 8,160.00 Mn + OFS Rs 9,726.19 Mn; listed BSE/NSE 21-Jan-2026" - runs/amagi-q1fy27/work/review_amagi_q1fy27.md:41
- reporting: quarterly. "## Q1 FY27 (three months ended 30 June 2026)" - review:2
- archetype: `classification: "AVERAGE"` - runs/amagi-2026-07-12/outputs/blocks/B01-gate0.yaml:27; "Media/SaaS: cloud broadcast-to-streaming, FAST channels, connected-TV ad monetization. Asset light, debt free" - companies/AMAGI.md:3; `sector_cap_row: "Pharma / CDMO"` - manifest.yaml:8; `sector_cap_used: 45` - B11-valuation.yaml:33
- first analysis: "run_date: 2026-07-12" - runs/amagi-2026-07-12/manifest.yaml:5
- verdict: `verdict: "PROCEED WITH FLAGS"` / `valuation_decision: "AVOID"` - B13-synthesis.yaml:7-8; `verdict: "WATCHLIST"                 # AVOID at CMP; DEEP WATCH leaning BUY-ON-DIPS per authoritative FTTCP` - B14-thesis.yaml:6; `devil_overall: "WEAKENED BUT ALIVE"` - B13-synthesis.yaml:16

## Q4 FY26
- base case: NOT FOUND (first run 2026-07-12 postdates the result; "| FY26 (actual) | 1,505.61 | 1,505.61 | 1,505.61 |" - outputs/reports/B11.md:132)
- guidance: `{item: "Steady-state adjusted EBITDA margin", number: "~10%", timeframe: "near-term run rate", stated_in: "Q3 FY26 call"}` and `{item: "Underlying revenue growth ex-timing effects", number: "25-30% constant currency", ...}` - B05-concall.yaml:19-20
- catalysts: "NEWSPULSE / agentic AI monetization → converts on disclosed revenue or customer count, first appears B07/B05, window FY27." - companies/AMAGI.md:25
- actuals: "| Revenue from Operations | 330.06 | 396.97 | 436.88 | 1,505.61 |" (cols Q1 FY26, Q4 FY26, Q1 FY27, FY26) - review:87; "| Operating EBITDA margin | (0.36%) | 6.01% | 6.83% | 3.35% |" - review:107; "| PAT | 3.94 | 34.26 | 33.91 | 71.67 |" - review:99; "Adjusted EBITDA Rs 156 Cr (10.4%) | PAT Rs 71.67 Cr (4.76%)" - B11.md:116
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NOT FOUND (no analysis predates this result)

## Q1 FY27
- base case: "| FY27 | 1,731.5 | 1,882.0 | 1,957.3 |" (Bear / Base / Bull revenue, Rs Cr) - B11.md:133; "| FY27 | 6.0% | 112.9 | 5.22 |" (base PAT margin / PAT Cr / EPS) - B11.md:142
- projection basis: "| Revenue growth (FY26→FY30) | 15% | 25% (guidance floor, cc) | 30% (guidance top, cc) |" - B11.md:124; "guidance discounted to floor; ESOP normalizes; margin creep" - B11.md:125
- guidance: `{item: "Q1 FY27 seasonality", number: "~22% of full-year revenue, ~11% of full-year EBITDA", timeframe: "Q1 FY27", stated_in: "Q4 FY26 call"}` - B05-concall.yaml:30
- catalysts: "NEWSPULSE/agentic AI and marketplace revenue disclosed as a separated line by FY27 (RED: continued non-disclosure through FY27)" - B14-thesis.yaml:25
- actuals: revenue 436.88, op EBITDA margin 6.83%, PAT 33.91 (review:87,107,99); "Revenue ₹437 Cr (+32% Y/Y; CC +21%); Adj. EBITDA ₹50 Cr (+201%, 11.5% margin); PAT ₹34 Cr (+760%, 7.5% margin)" - retro/2026-11/excerpts/local/AMAGI.md:84 (source ...\analysis\.workspace\feed_2026-08-13_1722\Amagi_Media_Labs_results.md)
- result vs base: "| Revenue growth YoY (consol) | ND | ~30% ("real 30% grower") | ND | **+32.4%** | At/above Base (reported; CC ND) |" - review:241; "This is the **first** quarterly print under the pipeline and revenue lands **at/above base** — the rule does **not** fire." - review:248; "**No thesis-broken condition has fired.**" - review:269
- management's stated reason: NOT FOUND
- risk flagged before: "Growth quality decays beneath the headline: cc 23% below the 25% guided floor, NRR 127->126, net logo adds 67->29, top-10 concentration 33.7%->40.2% (B05; B10)" - B15-devil.yaml:17
- by whom: Stage 15 devil's advocate; Stage 14 thesis checklist "Constant-currency revenue growth >=25% and NRR >=120% (RED: cc <20% or NRR <120%)" - B14-thesis.yaml:21
- overruled: NOT FOUND for this flag. (Separate operator ruling on ROCE: "[Devil's advocate flagged this may flatter a ~5% real return since the cash is undeployed; recorded as a live caveat, override stands.]" - companies/AMAGI.md:14)

## Q2/H1 FY27
- base case: same FY27E base as above (B11.md:133,142)
- guidance: standing Q3 FY26-call figures (B05-concall.yaml:19-20); newer numeric guidance NOT FOUND
- catalysts: "| Amagi Media Labs | Fri 6-Nov-2026, 10:00 am IST | Q2 / H1 FY27 earnings call after the 5-Nov results board meeting. First concall on record. |" - retro/2026-11/excerpts/local/AMAGI.md:252
- actuals: "Q2: revenue ₹475.82 Cr (+8.9% QoQ), op EBITDA ₹63.74 Cr (13.4%), core PBT ex-OI ₹56.52 Cr, ETR 9.4%, PAT ₹74.84 Cr" - retro/2026-11/excerpts/local/AMAGI.md:517 (source ...\announcements\2026-11-05_0405_to_2026-11-06_0253\REVIEW.md)
- result vs tripwires: "MASTER CASH GATE PASSES: H1 reported OCF +₹68.78 Cr (H1 FY26 −₹200.60 Cr); receivables ₹427.55 Cr vs ₹382 Cr a year ago (+12%) against revenue +29.5% H1" - retro/2026-11/excerpts/local/AMAGI.md:517; "TRIPWIRE 2 CONTESTED: CC growth Q2 +15%, H1 +18% (fires on reported CC), Q2 CC ex-base +21% (passes); NRR 125%+ passes" - retro/2026-11/excerpts/local/AMAGI.md:517
- management's stated reason: "Mgmt: H1 15.3% adj EBITDA margin is the baseline; Q2 had hiring-timing benefit" - retro/2026-11/excerpts/local/AMAGI.md:517; "Base effect isolated to H1; Q3 onward is a clean compare [MGMT]" - retro/2026-11/excerpts/local/AMAGI.md:879
- risk flagged before: "Revenue: constant-currency growth falls below 20% for two consecutive quarters, or NRR falls below 120%" - B14-thesis.yaml:15; B15-devil.yaml:17 (as above)
- by whom: Stage 14 thesis thesis_broken_conditions; Stage 15 devil's advocate
- overruled: NOT FOUND

## Not found
- board
- base_revenue / base_margin / base_profit for Q4 FY26
- mgmt_reason for Q4 FY26 and Q1 FY27
- risk_flagged_before / flagged_by / overruled for Q4 FY26
- overruled (all periods, for the growth-quality flag)
- H1 FY27 revenue and PAT totals as file-stated figures; FY27E EBITDA-margin base figure
