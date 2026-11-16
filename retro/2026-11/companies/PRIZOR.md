# PRIZOR - Prizor Viztech Ltd
## Sources read
- companies/PRIZOR.md (origin/main, on_main yes)
- runs/prizor-2026-07-12/manifest.yaml (313 branches, on_main yes)
- runs/prizor-2026-07-12/outputs/reports/11-valuation.md (grep + lines 126-157; on_main yes)
- runs/prizor-2026-07-12/outputs/reports/14-thesis.md (grep; on_main yes)
- runs/prizor-2026-07-12/outputs/reports/15-devil.md (grep; on_main yes)
- runs/prizor-2026-07-12/outputs/reports/10-valinputs.md (grep; on_main yes)
- runs/prizor-2026-07-12/outputs/final/gate-recommendation.md (lines 1-6; on_main yes)
- retro/2026-11/excerpts/sessions/PRIZOR.md (3 session excerpts, 2026-10-31 and 2026-11-02)
- retro/2026-11/excerpts/local/PRIZOR.md (70 local-file excerpts; read lines 1-340, targeted reads/greps to line 784)

## Company-level facts
- board / reporting: "NSE SME, listed July 2024. Reports half yearly." - companies/PRIZOR.md:3 ; "SECTION 8: MONITORING CHECKLIST (half-yearly — Prizor reports H1/H2 on NSE SME, no quarterly print exists)" - 14-thesis.md:167
- archetype: no "archetype" string in the run folder (grep). Sector row: "sector cap row corrected from manifest \"Pharma / CDMO\" (38x) to Manufacturing / Industrial products (25x)" - companies/PRIZOR.md:13
- first analysis: "run_date: 2026-07-12" - manifest.yaml:5
- verdict: "2026-07-12: AVOID / DEEP WATCH (not actionable WATCHLIST). CMP Rs 825. Entry zone Rs 63-79, MoS Rs 63." - companies/PRIZOR.md:9 ; "PROCEED WITH FLAGS" - gate-recommendation.md:1
- projection basis: "SECTION 2 — PROJECTIONS (Year 0 = FY25 audited; conservative bias)" - 11-valuation.md:130 ; "base revenue CAGR 14% < SOM-implied ceiling 17% -> **CONSISTENT.** (FY26 unaudited ~99% growth is NOT used to set base; SOM ceiling and structural cash negativity govern.)" - 11-valuation.md:142

## Q4 FY26
- base case: NOT FOUND (no projection predates the FY26 result)
- guidance: NOT FOUND - "| Guidance: Revenue (FY26, Rs Cr) | NOT FOUND | (AR MD&A Outlook p.53-58 contains no quantified guidance; B05) |" - 10-valinputs.md:69
- catalysts: NOT FOUND
- actuals (FY26 full year, unaudited at run date): "only unaudited investor presentation figures exist (₹148 Cr disclosed)" - 10-valinputs.md:174 ; "only investor presentation figure (₹20.76 Cr unaudited) available" - 10-valinputs.md:175 ; "Prizor claims 21-23% EBITDA, contradicted" - 10-valinputs.md:126 ; later: "Deck prints FY26 CFO ₹0.29 Cr on PAT ₹20.76 Cr (0.014x); reopen line fails" - retro/2026-11/excerpts/local/PRIZOR.md:549. H2 FY26 split: NOT FOUND.
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NO (first analysis postdates the result) / NOT FOUND / NOT FOUND

## Q1 FY27
- NOT APPLICABLE (half-yearly reporter): "Prizor reports H1/H2 on NSE SME, no quarterly print exists" - 14-thesis.md:167
- base case / guidance / catalysts / actuals / reason: NOT APPLICABLE / NOT FOUND
- result vs base: BASELINE NOT COMPARABLE (no Q1 print exists)

## Q2/H1 FY27
- base case: "| Revenue CAGR | 8% | 14% | 18% |" - 11-valuation.md:136 ; "| Revenue (Cr) | 70.98 | 105.2 |" - 11-valuation.md:148 ; "| EBITDA (Cr) | 15.077 (21.42%) | 18.9 (18%) |" - 11-valuation.md:149 ; "| PAT (Cr) | 10.15 (14.29%) | 13.68 (13%) |" - 11-valuation.md:150 (Year 0 = FY25, Year 3 base; FY27E not stated)
- guidance: none before the result. After: "First transcript: CFO calls -₹4.57 Cr CFO \"+₹4.6 Cr\"; WC \"longer, 120-150 days\"; guide implies H2 growth 23-37%." - retro/2026-11/excerpts/local/PRIZOR.md:752 ; "The FY27 guide of 60-70% implies H2 growth of on" (truncated) - retro/2026-11/excerpts/local/PRIZOR.md:758
- catalysts / tripwires: "FY26 audited operating cash flow at or below zero for a third straight year while PAT > Rs 20 Cr = structural cash burn confirmed, AVOID hardens." - companies/PRIZOR.md:16 ; "Reopen to WATCH (never BUY at Rs 825) only if FY26 audited operating CFO reaches >= 40% of PAT." - companies/PRIZOR.md:17
- actuals: "H1 FY27 results (board 30-Oct, read via Bull AI, NSE PRIZOR_30102026134154 pp.4-8) ... Revenue ₹106.50 Cr (+153.5% YoY, +0.5% vs H2 FY26); PAT ₹15.34 Cr (+159%); EBITDA ~23.5%" - retro/2026-11/excerpts/local/PRIZOR.md:373 ; "Prizor Viztech: H1 CFO -₹4.57 Cr vs PAT ₹15.34 Cr." - retro/2026-11/excerpts/local/PRIZOR.md:309 ; "test monitorable 4 (EBITDA >= 18%) before or after the ~₹6.1 Cr of H1 capitalised development (17.8% if expensed)?" - retro/2026-11/excerpts/local/PRIZOR.md:469
- result vs base: BASELINE NOT COMPARABLE (base is a Year-3 annual figure off FY25; actual is a half year). File statement on the cash test: "| Prizor Viztech | AVOID | ₹79 / ₹63 | ₹1,216 (screener.in, 03-Nov-2026 01:38 IST) | Negative. H1 CFO -₹4.57 Cr on PAT ₹15.34 Cr (-0.30x). The bear branch of the 07-Oct separator is confirmed. First concall 4-Nov. |" - retro/2026-11/excerpts/local/PRIZOR.md:353 ; open ruling: "Does H1 CFO/PAT of -0.30x confirm the 07-Oct bear branch? The written trigger names FY26 audited CFO. The call is on 4-Nov." - session 2026-11-02 7102fd48-ea11-43ba-8a53-9d9b6f27dca5.jsonl (sessions/PRIZOR.md:18)
- management's stated reason: "WC \"longer, 120-150 days\"" - retro/2026-11/excerpts/local/PRIZOR.md:752 ; "Objects of the ₹119.45 Cr raise stated [MGMT]: cut ST borrowing, WC, capacity/certification/backward integration" - retro/2026-11/excerpts/local/PRIZOR.md:756
- risk flagged before / by whom / overruled: YES - "| 2 | Cash conversion structurally negative (cumulative CFO/PAT -1.02x); peer cohort treats this as multi-year structural | H | H |" - 14-thesis.md:120 (Stage 14 thesis risk matrix) ; "Tripled paper profit that produces no cash, alongside a ballooning finished-goods build, is the textbook sell-in / channel-loading signature." - 15-devil.md:42 (Stage 15 devil's advocate). Overruled: NO - "B01/B02/B03 win. The hardest verdict rules: ROCE without cash is accounting. Cash determination INDETERMINATE leaning structural (fttcp)" - 14-thesis.md:83

## Not found
- archetype label
- H2 FY26 half-year figures; audited FY26 revenue / EBITDA margin in the files read
- FY27E base-case line (only Year-3 base off FY25)
- quantified management guidance before the H1 FY27 result
- source text of the "07-Oct separator"
- any file statement comparing H1 FY27 P&L with our base case
- quarterly review folder in the repo
