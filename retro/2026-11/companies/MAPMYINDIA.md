# MAPMYINDIA - C.E. Info Systems Ltd
## Sources read
- runs/mapmyindia-2026-07-13/manifest.yaml (311 branches, on_main yes)
- runs/mapmyindia-2026-07-13/outputs/final/gate-recommendation.md (on_main yes)
- runs/mapmyindia-2026-07-13/outputs/final/fttcp-draft.md (on_main yes)
- runs/mapmyindia-2026-07-13/outputs/final/fttcp-deliberation.md (on_main yes)
- runs/mapmyindia-2026-07-13/outputs/final/notion-payload.md (on_main yes)
- runs/mapmyindia-2026-07-13/outputs/final/verifier-summary.md (on_main yes)
- runs/mapmyindia-2026-07-13/outputs/blocks/B01-gate0.yaml (on_main yes)
- runs/mapmyindia-q1fy27/work/review_mapmyindia_q1fy27_v2.md (origin/claude/map-my-india-quarterly-analysis-43nbwc, on_main no; first 150 lines not read in full, grepped and read in parts)
- runs/mapmyindia-q1fy27/work/audit_mapmyindia_q1fy27_v2.md (same branch, on_main no)
- retro/2026-11/excerpts/sessions/MAPMYINDIA.md (session excerpts)
- retro/2026-11/excerpts/local/MAPMYINDIA.md (local-folder excerpts)
- Company memory file: NOT FOUND on any branch

## Company-level facts
- board: NOT FOUND ("Ticker: NSE MAPMYINDIA / BSE 543425" - retro/2026-11/excerpts/local/MAPMYINDIA.md:14; no file says main board or SME)
- reporting: "The company reports quarterly, so the standard windows apply." - fttcp-draft.md:13
- archetype: "classification: \"GOOD+\"" - B01-gate0.yaml:25; "EM Score 30, EM Classification: MOAT STRENGTHENING." - notion-payload.md:12; "Sector cap row. CORRECTED to Platform / SaaS / IT services, 45x." - fttcp-draft.md:19
- first analysis: "# CE Info Systems (MapmyIndia) — FY26 results + dividend ... **Filing date:** 19 May 2026" in analysis/.workspace/2026-05-20_morning_announcements - retro/2026-11/excerpts/local/MAPMYINDIA.md:3-9. First pipeline run: "run_date: 2026-07-13" - manifest.yaml:5; "First workup, no prior page existed." - notion-payload.md:3
- verdict: "## VERDICT: PROCEED WITH CAVEATS" - gate-recommendation.md:3; "AVOID on valuation at CMP Rs1,185." - notion-payload.md:28; "Decision Status: NOT SET. Recommended: WATCHLIST / AVOID." - notion-payload.md:16

## Q4 FY26
- base case: NOT FOUND (no analysis predates the FY26 result)
- guidance: "they deliberately do NOT use management's Rs1,000 Cr by FY28 target, which implies about 45% annual growth" - fttcp-draft.md:58; "FY27 and FY28 margin guidance declined (Feb 2026 p.4; Nov 2025 p.11)" - fttcp-deliberation.md:44
- catalysts: "an order book above Rs1,750 Cr, about 3.7 times revenue, plus the signed IOCL Rs110 Cr five-year contract and the Survey of India order in hand" - fttcp-draft.md:21
- actuals: "| Revenue from Operations | 121.61 | 145.04 | 139.72 | 474.10 |" (Q1 FY26 / Q4 FY26 / Q1 FY27 / FY26) - review_mapmyindia_q1fy27_v2.md:77; "| Q4 FY26 | 144.40 | 44.7% | 56.70 |" - review v2:201; "| **NPAT incl. assoc/JV** | **45.81** | **50.93** | **49.74** | **134.02** |" - review v2:97; "| FY26 | 35.6 | ACTUAL |" - fttcp-draft.md:68
- result vs base: NO BASELINE
- management's stated reason: "Management pins it on government fiscal-grant delays, state elections, and re-tenders" - fttcp-draft.md:58
- risk flagged before / by whom / overruled: NOT FOUND (no analysis predates)

## Q1 FY27
- base case: "| FY27 | 540 | +14 | EXPECTED, illustrative (order-book conversion path, not management's target) |" - fttcp-draft.md:52; "| FY27 | 36.5 | EXPECTED, illustrative (IoT SaaS mix rising, Q4 FY26 exit rate about 44%) |" - fttcp-draft.md:69; "| Base | 15% | 37.2 | 42.8 | Rs1,370 | Rs701 | Rs561 |" (PAT CAGR / FY29 EPS / FY30 EPS / exit fair value / entry / MoS) - fttcp-deliberation.md:63
- guidance: "| EBITDA margin band | **\"35% plus for the whole year\"** FY27 (T14/L38) |" - review v2:477; "| Revenue target (FY28 Rs1,000 Cr) | **Not mentioned** (A3-16) |" - review v2:476
- catalysts: "Government-tagged revenue growth back to 15-20% YoY | Q1-Q2 FY27" - fttcp-draft.md:141; "About Rs20 Cr FY27 IOCL revenue materialises" - fttcp-draft.md:147
- actuals: "| Q1 FY27 | 139.72 | 40.2% (underlying ~43.0%) | 46.79 (underlying ~50.79) | **Rs4 Cr govt write-off (T12/L34); geometry now known** |" - review v2:202; NPAT incl. assoc/JV 49.74 - review v2:97
- result vs base: "**No thesis-broken condition has formally FIRED.** The binding falsifier is unresolvable, not cleared." - review v2:363; "**Resolution: STILL UNRESOLVABLE (A3-01).** The concall explicitly confirmed no Q1 balance sheet was filed (T33/L78)." - review v2:291
- management's stated reason: "Management: \"instead of 40.2 it would have been 43 plus\" (T12/L34)." - review v2:206; [holding detail removed]
- risk flagged before / by whom / overruled: "Whether it is a transient government-collection lag or permanent structural leakage cannot be resolved without the missing credit rating rationale and the FY26 receivables ageing schedule." - fttcp-draft.md:25; "DA said management would evade the receivables number and the treasury plan — both proved correct on this call." - review v2:432; not overruled: "INDETERMINATE never silently resolves to PROCEED and caps the verdict at PROCEED WITH CAVEATS" - gate-recommendation.md:10

## Q2/H1 FY27
- base case: same as Q1 FY27 (fttcp-draft.md:52, 69; fttcp-deliberation.md:63). Tripwire: "Q1 FY27 consolidated trade receivables rising further above the ~Rs176 Cr FY26 close on flat or declining sequential revenue, with the >6 month ageing bucket expanding." - gate-recommendation.md:48
- guidance: "35% plus for the whole year" (Q1 FY27 call) - review v2:477
- catalysts: "The master gate is the Q2 FY27 H1 balance sheet, with two legs (Notion, 31-Aug note, \"Updated Q2 FY27 master gate\")" - retro/2026-11/excerpts/local/MAPMYINDIA.md:353
- actuals: "consolidated receivables ₹186.55 Cr at 30-Sep vs ₹176.4 Cr FY26 close (+5.7%, falsifier number breached) ... Q2 op EBITDA margin 34.1% (first breach of 38%); govt -37.5% Q2. Q2 PAT ₹35.3 Cr (+90.6% YoY, -29% QoQ)." - retro/2026-11/excerpts/local/MAPMYINDIA.md:325
- result vs base: "Negative. Receivables ₹186.6 Cr breach the ₹176.4 Cr falsifier; 96% of H1 growth is one-OEM hardware; margin 34.1% below 38%; CFO/PAT 0.92x is the offset." - retro/2026-11/excerpts/local/MAPMYINDIA.md:397
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: gate-recommendation.md:48 (quoted above), B13 falsification line; "Receivables rise above Rs176 Cr with over-six-month ageing widening | Q1 FY27 | Cash confirmed STRUCTURAL DECLINING" - fttcp-draft.md:143; open rulings: "Falsifier 'flat sequential revenue' leg: quarter-on-quarter (Q2 -5.7%, leg met) or half-on-half (H1 +13.7% vs H2 FY26, leg fails)?" - retro/2026-11/excerpts/local/MAPMYINDIA.md:400

## Not found
- board
- verdict of the 2026-05-20 local note (excerpt is header only)
- base_revenue / base_margin labelled as our base case (only "EXPECTED, illustrative" columns)
- base figures of any kind predating Q4 FY26
- Q2 FY27 revenue in Rs Cr
- management's stated reason for Q2 FY27
- FY27E PAT figure in the Base case (only FY29/FY30 EPS given)
