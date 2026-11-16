# MACPOWER - Macpower CNC Machines Ltd

## Sources read
- companies/MACPOWER.md (origin/claude/macpower-pipeline-g9ouq4, on_main no)
- runs/macpower-2026-07-30/manifest.yaml (258 branches, on_main yes)
- runs/macpower-2026-07-30/outputs/blocks/B11-valuation.yaml, B13-synthesis.yaml, B14-thesis.yaml, B15-devil.yaml, B10-valinputs.yaml (grep), B01-gate0.yaml (grep) (on_main yes)
- runs/macpower-2026-07-30/outputs/reports/11-valuation.md (lines 108-123 + grep), 05-concall.md (grep) (on_main yes)
- retro/2026-11/excerpts/sessions/MACPOWER.md (1 excerpt, read in full)
- retro/2026-11/excerpts/local/MACPOWER.md (retro/2026-11/excerpts/local/MACPOWER.md does not exist; grepped for the company name, key sections read)
- LESSONS.md / LESSONS_ARCHIVE.md: no MACPOWER hit in the first 20 name matches; not read further

## Company-level facts
- board: "Macpower CNC | results | SME concall invite" - retro/2026-11/excerpts/local/MACPOWER.md:34; "Macpower CNC (2 filings ...) | results | Q1FY27 results + analyst meet notice; SME machine tools" - retro/2026-11/excerpts/local/MACPOWER.md:68; "14 PDFs failed with HTTP 403 on the NSE SME / Emerge link ... also hit 403 on Macpower CNC" - retro/2026-11/excerpts/local/MACPOWER.md:889. No repo file states the board.
- reporting: quarterly. "Q1 FY27 results (₹95.24 cr revenue, +56.1% YoY, per inputs/results outcome PDF)" - runs/macpower-2026-07-30/outputs/reports/05-concall.md:194
- archetype: no archetype label found. "Sector cap row corrected Pharma/CDMO 38x to Cables/Industrial products 25x (collector auto-pick defect)." - companies/MACPOWER.md:17; "classification: \"AVOID\"" / "grand_total: 81" - B01-gate0.yaml:18,15
- first analysis: "run_date: 2026-07-30" - manifest.yaml:5
- verdict: "verdict: \"PROCEED WITH CAVEATS\"" / "valuation_decision: \"AVOID\"" - B13-synthesis.yaml:7,12
- projection basis: "Forward FY27 EPS not published; derived from revenue guidance x margin (Base Rs 43.0, band Rs 40.5-44.0)" - B11-valuation.yaml:7; "Earnings basis one-year-forward. Reasoning: fits an order-book-backed 28 to 30 percent grower" - companies/MACPOWER.md:16

## Q4 FY26
- base case: NOT FOUND (no analysis before 2026-07-30)
- guidance: NOT FOUND for the period before the result
- catalysts: "25% EBITDA margin achievable in \"2-3 years\" via new plant | Partial — reframed in Q4 FY26 call as specifically requiring the (still-undated) 60-acre land" - 05-concall.md:83
- actuals: "revenue_fy26_cr: 333.18" / "ebitda_fy26_cr: 53.90" / "pat_fy26_cr: 33.87" / "ebitda_margin_pct: 16.2" - B10-valinputs.yaml:31-33,38; order book "₹406 cr, +23% YoY (Q4 FY26 call)" - 05-concall.md:162
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NOT FOUND

## Q1 FY27
- base case: NOT FOUND (base written with Q1 already reported)
- guidance: "Q1 FY27 results (₹95.24 cr revenue, +56.1% YoY ...) run well ahead of the 28-30% FY27 guidance given in the Q4 FY26 call" - 05-concall.md:194
- catalysts: "60-acre govt greenfield (10,000 machines) -> converts on a binding signed lease/deed ... window undated (already slipped 3x)." - companies/MACPOWER.md:26; "13-acre Metoda plant phase 1+2 ... window 24-36m." - companies/MACPOWER.md:27
- actuals: revenue Rs 95.24 cr (05-concall.md:194); "PAT margin band: FY26 9.72% (B10 pat_margin_pct); Q1 FY27 ~10.1% (B10 note)." - 11-valuation.md:113; PAT amount NOT FOUND ("Q1 FY27 +110% YoY not sustainable run-rate" - B10-valinputs.yaml:7)
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NOT FOUND

## Q2/H1 FY27
- base case: "| Base | Rs 429.8 cr (+29%) | 10.0% | Rs 43.0 cr | **Rs 43.0** |" - 11-valuation.md:119
- guidance: "Guidance FY27 revenue growth +28-30% (B10 guidance_revenue_growth_fy27_pct) -> FY27 revenue Rs 426.5 cr (+28%) to Rs 433.1 cr (+30%)." - 11-valuation.md:112
- catalysts: companies/MACPOWER.md:26-30 (60-acre land; 13-acre Metoda; JV/technology transfer; defence/aero bid book; 25% EBITDA margin); "₹50 crore expansion planned" - retro/2026-11/excerpts/local/MACPOWER.md:598
- actuals: "Macpower CNC: Analysts/Institutional Investor Meet/Con. Call Updates (30 Oct) Q2/H1 FY27 transcript: revenue 120.33 Cr, PAT 13.47 Cr; order book 476 Cr." - retro/2026-11/excerpts/local/MACPOWER.md:962; "Q2/H1 FY27 results hit records; revenue rose 40.4%, PAT 43.7%" - retro/2026-11/excerpts/local/MACPOWER.md:598; "Positive on growth (+40% YoY, flat 16.5% margin); CFO ₹30 Cr mostly a one-time receivable release; inventory 234 days." - retro/2026-11/excerpts/local/MACPOWER.md:571
- result vs base: no file compares the print with our base. "Call transcript (no PDF): order book ₹476 Cr, between the ₹456 Cr bear and ₹500 Cr bull lines; site date still unknown." - retro/2026-11/excerpts/local/MACPOWER.md:1097
- management's stated reason: NOT FOUND
- risk flagged before: "Cash drag is likely STRUCTURAL not growth-induced (PSU/subsidy-financed customer payment lags; management said conversion will not improve rapidly; receivables +57.5% vs revenue +8.6% ..." - runs/macpower-2026-07-30/outputs/blocks/B15-devil.yaml:13
- by whom: Stage 15 devil's advocate; "flags_active: [FLAG-CASH, FLAG-GATE0]" / "flag_cash_determination: \"INDETERMINATE\"" - B13-synthesis.yaml:9-10
- overruled: NOT FOUND
- reading limits: "Macpower CNC: Q2 / H1 FY27 call (27-Oct). Download failed (HTTP 403); read from the Screener summary only. Needs a manual pull." - retro/2026-11/excerpts/local/MACPOWER.md:988; "Tracking note only; no thesis or levels on file." - retro/2026-11/excerpts/local/MACPOWER.md:572

## Not found
- archetype label
- board in any repo file (local pipeline labels only)
- Q4 FY26 quarter-only revenue, margin, PAT
- Q1 FY27 PAT amount and EBITDA margin
- whether Rs 120.33 Cr / Rs 13.47 Cr is the quarter or the half (summary does not say)
- management's reason for any outcome
- whether the cash flag was overruled
