# SYSTANGO - Systango Technologies Ltd
## Sources read
- companies/SYSTANGO.md (origin/main, on_main yes)
- runs/systango-2026-08-29/manifest.yaml (166 branches, on_main yes)
- runs/systango-2026-08-29/outputs/blocks/11-valuation.yaml, 14-thesis.yaml, 15-devil.yaml; 00-inputs, 01-gate0, 05-concall, 10-valinputs by grep (on_main yes)
- runs/systango-2026-08-29/outputs/reports/11-valuation.md (lines 222-266, 512-521 plus grep) (on_main yes)
- retro/2026-11/excerpts/sessions/SYSTANGO.md (one excerpt, 2026-09-16, skill-file mention only)
- retro/2026-11/excerpts/local/SYSTANGO.md (local-folder excerpts; retro/2026-11/excerpts/local/SYSTANGO.md does not exist)

## Company-level facts
- board (SME): "prospectus (MEDIUM; SME listed ~Mar-2023, ~3.4y ago; ..." - runs/systango-2026-08-29/outputs/blocks/00-inputs.yaml:11; `promoter_stake: "72.07% (stable, no pledge found; SME Emerge lighter regime)"` - outputs/blocks/10-valinputs.yaml:53; "undercovered SME-Emerge micro-cap" - outputs/reports/11-valuation.md:519
- reporting (half-yearly): "First run misread the consolidated FY26 revenue as Rs 44.89 cr (the H2 half-year column)" - outputs/blocks/10-valinputs.yaml:6; "Two dated resolution points: FY26 AR (Sep-2026), H1 FY27 (Nov-2026)." - companies/SYSTANGO.md:11
- archetype: `sector_cap_row: "Platform / SaaS / IT services"` - manifest.yaml:8; "FROM rung -> TO rung: R2 COST-ADVANTAGED CONVERTER -> R3 VALUE-ADDED / SPEC'D SUPPLIER" - companies/SYSTANGO.md:23; "Posture VALUE-TRAP RISK" - companies/SYSTANGO.md:7; "Amendment 17: NON CONVERTER" - companies/SYSTANGO.md:42
- first analysis: `run_date: 2026-08-29` - manifest.yaml:5
- verdict: "Spear: HIT 2026-08-29 - entry <= Rs 210" - companies/SYSTANGO.md:14; "Halt 1 decision (KILL/SHALLOW/PROCEED): 2026-08-29 PROCEED under explicit operator promoter-override." - companies/SYSTANGO.md:31; `verdict: "WATCHLIST"` - outputs/blocks/14-thesis.yaml:6; "As of 2026-08-29: WATCHLIST, capped at DEEP WATCH, leaning AVOID." - companies/SYSTANGO.md:7

## Q4 FY26 (H2 FY26 / full-year FY26; half-yearly reporter)
- base case: NOT FOUND (first analysis 2026-08-29 is after the FY26 result)
- guidance: `{item: "FY26 revenue target", number: "Rs 250 crore+ / $25M", timeframe: "3 years from Jul 2023 (FY26)", stated_in: "Q_FY23 call, Jul 2023; reaffirmed H1FY24 call, Nov 2023"}` - outputs/blocks/05-concall.yaml:28
- catalysts: "Tech Alchemy UK acquisition (GBP1.5M MoT 19-Jun-2025 with St Topco, converts on a filed close, Rs8cr IPO bucket at 0% utilisation)" - companies/SYSTANGO.md:74
- actuals: `revenue_fy26: "Rs 90.38 cr (audited, results p.17, Year ended 31-Mar-2026 column, 9037.86 lakh)"` - outputs/blocks/10-valinputs.yaml:18; H2 "Rs 44.89 cr (the H2 half-year column)" - 10-valinputs.yaml:6; `pat_fy26: "Rs 31.88 cr after minority (results p.17)"` - 10-valinputs.yaml:20; "delivered 37.66% FY26 EBITDA margin ex-other-income" - 10-valinputs.yaml:50; "H2FY26 EBITDA margin fell back to 33.1%" - companies/SYSTANGO.md:14; "H2 revenue marginally below H1; PAT -23% h/h" - companies/SYSTANGO.md:26. H2 FY26 PAT in Rs Cr: NOT FOUND
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND. `explanation: "No post-Nov-2023 call exists to source management's own explanation; delivery evidence only"` - outputs/blocks/05-concall.yaml:44
- risk flagged before / by whom / overruled: NOT FOUND (no analysis predates the result)

## Q1 FY27
- NOT APPLICABLE (half-yearly reporter); no Q1 result exists in any file
- base case on file for the year: "| Y1 | FY27 | 105.74 | 21.56 | 99.42 | 20.27 | SEZ active (18.43 base) |" - outputs/reports/11-valuation.md:252
- result vs base: BASELINE NOT COMPARABLE (no Q1 result)

## Q2/H1 FY27
- base case: "| Y1 | FY27 | 105.74 | 21.56 | 99.42 | 20.27 | SEZ active (18.43 base) |" - outputs/reports/11-valuation.md:252; [holding detail removed]; B10). Tax at the FY26 effective 18.64%." - 11-valuation.md:230-231; "H1 FY27 revenue (Nov-2026): green > Rs 52 cr on the 17% base path; red < Rs 45 cr below the 10% downside path" - outputs/blocks/14-thesis.yaml:12
- guidance: NOT FOUND. "Guidance credibility D: revenue-side 0 of 5 delivered; only EBITDA margin promise kept. Investor calls silent 33 months." - companies/SYSTANGO.md:63
- catalysts: "watch H1 FY27 and the FY26 AR before any position." - outputs/blocks/11-valuation.yaml:64
- actuals: "H1 FY27 consolidated revenue ₹42.01 Cr, PAT ₹16.31 Cr, CFO ₹6.36 Cr (pp.11-12)" - C:/ConcallPipeline/Daily Concall Intelligence\announcements\2026-11-12_0500_to_2026-11-13_0500\deep\out\T24.md (retro/2026-11/excerpts/local/SYSTANGO.md:201). EBITDA margin: NOT FOUND
- result vs base: MISS, file-stated. "H1 FY27 revenue ₹42.0 Cr, below the ₹44 Cr 'something broke' line; CFO/PAT 0.39x, DSO ~85 days. Proof gate failed." - same T24.md (retro/2026-11/excerpts/local/SYSTANGO.md:197). Arithmetic: Rs 42.01 Cr = 81% of the Rs 52 Cr green line; 39.7% of FY27E Rs 105.74 Cr
- management's stated reason: NOT FOUND
- risk flagged before: YES. "Growth already stalled inside FY26: H2 revenue below H1, EBITDA margin -916 bps to 33.1%, 64% guidance miss, top-3 concentration rose into the surge (38 to 42%). The 17% base and even the 10% downside path are generous" - runs/systango-2026-08-29/outputs/blocks/15-devil.yaml:16; `thesis_broken_if: "H1 FY27 revenue < Rs 45 cr OR ..."` - outputs/blocks/14-thesis.yaml:10
- by whom: Stage 15 devil's advocate (`growth_triggers: "destroyed"` - 15-devil.yaml:7); Stage 14 thesis tripwire
- overruled: NO. "THESIS-BROKEN if: H1 FY27 revenue < Rs 45 cr (breaks the 10% downside path) OR ..." - companies/SYSTANGO.md:56; `overall: "WEAKENED BUT ALIVE"` - 15-devil.yaml:11
- open ruling after the result: "Proof gate printed in the 'below ₹44 Cr = something broke' band (₹42.01 Cr) on top of the half-failed September governance tests: move from DEEP WATCH to AVOID?" - T24.md (retro/2026-11/excerpts/local/SYSTANGO.md:200)

## Not found
- H2 FY26 PAT in Rs Cr
- FY27E base PAT in Rs Cr (operating EPS only)
- H1 FY27 EBITDA margin
- mgmt_guidance for FY27 / H1 FY27
- mgmt_reason (all periods)
