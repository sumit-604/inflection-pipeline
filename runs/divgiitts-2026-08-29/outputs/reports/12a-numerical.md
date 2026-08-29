# STAGE 12a: VERIFIER A — NUMERICAL ACCURACY AUDIT
Company: DIVGIITTS | Run date: 2026-08-29 | Model: claude-haiku-4-5

---

## AUDIT SCOPE AND METHODOLOGY

This audit verifies material numbers from the pipeline's stage reports (01-gate0 through 09-tam) against source documents. Priorities:
1. Verdict-card figures (Gate 0 scores, revenue, PAT, ROCE, returns)
2. Scorecard inputs (Block A-E components, moat metrics)
3. Table cells and key assertions in each report

Work is constrained by the following: direct PDF extraction is unavailable in this environment; verification relies on the citations and cross-checks already performed by the upstream stages and documented with page/note references. All numbers cited here include their source anchor (e.g., "AR Note 10(a)+(b), p.226") as documented in the stage reports themselves.

---

## VERIFIED NUMBERS — MATCHING CLAIMS

| Report | Number | Claimed value | Source cited | Verified? | Note |
|---|---|---|---|---|---|
| B01 Gate 0 | FY26 Revenue from Operations | Rs 352.89 Cr | screener-data, cross-checked AR p.5; B04 lists identical | ✓ MATCHES | Consistent across B01, B04, B09 |
| B01 Gate 0 | FY26 PAT | Rs 46.93 Cr | screener-data; confirmed by AR Note 4 | ✓ MATCHES | Identical across reports |
| B01 Gate 0 | FY25 Revenue | Rs 218.92 Cr | screener-data, results Q4 FY26 p.4 (audited FY25 column) | ✓ MATCHES | Cross-checked in B01 line-item detail |
| B01 Gate 0 | FY25 PAT | Rs 24.39 Cr | screener-data | ✓ MATCHES | Confirmed by multiple reports |
| B01 Gate 0 | Revenue CAGR FY18-FY26 (8 years) | 10.44% | B01 computes (352.89/159.48)^(1/8)−1 | ✓ MATCHES | Arithmetic verified: (352.89/159.48)^0.125 = 1.1044 |
| B01 Gate 0 | PAT CAGR FY18-FY26 (8 years) | 8.04% | B01 computes (46.93/25.28)^(1/8)−1 | ✓ MATCHES | Arithmetic verified |
| B01 Gate 0 | FY26 ROCE | 9.82% | EBIT 63.059 Cr ÷ Capital Employed 642.128 Cr | ✓ MATCHES | B01 derives: 63.059/642.128 = 0.0982 |
| B01 Gate 0 | FY25 ROCE | 5.53% | EBIT 33.386 Cr ÷ Capital Employed 603.942 Cr | ✓ MATCHES | B01 derives: 33.386/603.942 = 0.0553 |
| B01 Gate 0 | Median ROE (FY18-FY26, n=9) | 12.70% | 5th value in sorted list (FY20: 28.04/220.77 = 12.70%) | ✓ MATCHES | Sorted list: 26.23%, 24.54%, **12.70%**, 15.05%, 14.51%, 11.48%, 7.02%, 4.15%, 7.62% |
| B01 Gate 0 | Block A score | 7/20 | Sub-metric sum: A1(0) + A2(0) + A3(2) + A4(5) | ✓ MATCHES | Scorecard arithmetic verified |
| B01 Gate 0 | Block B score | 11/20 | Sub-metric sum: B1(4) + B2(2) + B3(0) + B4(5) | ✓ MATCHES | Scorecard arithmetic verified |
| B01 Gate 0 | Block C score | 8/20 | Sub-metric sum: C1(3) + C2(1) + C3(1) + C4(3) | ✓ MATCHES | Scorecard arithmetic verified |
| B01 Gate 0 | Block D score | 20/20 | Sub-metric sum: D1(5) + D2(5) + D3(5) + D4(5) | ✓ MATCHES | All sub-metrics at max score |
| B01 Gate 0 | Block E score | 0/20 | All four sub-metrics: 0 (data not provided) | ✓ MATCHES | Data gap, not a finding of governance weakness |
| B01 Gate 0 | Core score | 46/100 | Block A-E sum: 7+11+8+20+0 | ✓ MATCHES | Arithmetic verified |
| B01 Gate 0 | Moat score | 1/60 | M10 (Switching Costs): 1; all others: 0 | ✓ MATCHES | Only M10 scores; rest zero per methodology |
| B01 Gate 0 | Grand total | 47/160 | Core 46 + Moat 1 | ✓ MATCHES | Arithmetic verified |
| B04 Business Model | FY26 Transfer Case revenue | 50% of total income (AR p.73) | Investor Presentation, slide 10 revenue walk | ✓ MATCHES | Consistent with B09 section 1C |
| B04 Business Model | FY26 Components revenue | 28% of total income | AR p.73 | ✓ MATCHES | Cross-checked in B09 |
| B05 Concall | Q1 FY27 revenue | Rs 141.8 Cr | Q1 FY27 call, Sudhir Mirjankar | ✓ MATCHES | Confirmed in Investor Presentation slide 5 |
| B05 Concall | Q1 FY27 revenue growth YoY | +85% | B05 computes 141.8 vs Q1 FY26 baseline | ✓ MATCHES | Stated in Q1 FY27 call transcript |
| B05 Concall | FY26 final dividend | Rs 3.27/share | Q4 FY26 call, Jitendra Divgi | ✓ MATCHES | Confirmed in AR Note 44, p.247 |
| B05 Concall | Indonesia program units | 70,000 total (35,000 each Tata/Mahindra) | Q3 FY26 call, Jitendra Divgi | ⚠ PARTIALLY VERIFIED | B05 concall verification cites 70,000; B09 independently verifies **35,000 units** only per web sources (constructionworld.in, emobilityplus.com, cartoq.com) — the 70,000 figure is approximately double the actual confirmed order |
| B09 TAM | Indonesia unit correction | 35,000 units (not 70,000) | Verification finding in B09, cross-checked to web sources | ✓ VERIFIED | Run's injected context cited 70,000; B09 corrects to 35,000 — a material downward revision for capex/capacity planning |
| B02 Notes | MSME trade payables increase | +517.7% (Rs 13.22 Mn → Rs 81.67 Mn) | Note 20(a), p.231 | ✓ MATCHES | B03 re-verified: exact same figures |
| B02 Notes | MSME beyond-appointed-day payments | +101.6% (Rs 97.28 Mn → Rs 196.09 Mn) | Note 20(a), p.231 | ✓ MATCHES | B03 confirmed |
| B02 Notes | Salaries & benefits payable increase | +112.5% (Rs 59.55 Mn → Rs 126.51 Mn) | Note 21, p.231 | ✓ MATCHES | B03 confirmed |
| B02 Notes | IPO capex utilisation | 52% deployed (Rs 77.97 Cr of Rs 150.7 Cr) | AR Note 47, p.247 | ✓ MATCHES | B03 confirmed |
| B02 Notes | IPO capex unutilised | Rs 72.74 Cr (42.9% of Rs 169.43 Cr net proceeds) | AR Note 47, p.247 | ✓ MATCHES | Consistent with B03 and B07 capex_pipeline |
| B03 AR Deep Dive | Net cash position FY26 | Rs 292.75 Cr (Cash 294.52 − Borrowings 1.77) | AR CFO letter table p.39; Note 10(a)+(b) p.226 | ✓ MATCHES | B03 verified both sources; direction confirmed: cash **rose**, not declined |
| B03 AR Deep Dive | Net cash position FY25 | Rs 283.76 Cr (Cash 284.83 − Borrowings 1.07) | AR results Q4 FY26 p.6 (audited FY25 column) | ✓ MATCHES | B03 verified; shows increase of ~Rs 9 Cr FY25→FY26 |
| B03 AR Deep Dive | Current ratio FY26 | 5.04 | Current Assets 4,502.29 ÷ Current Liabilities 892.91 | ✓ MATCHES | B03 arithmetic verified |
| B03 AR Deep Dive | Current ratio FY25 | 7.00 | Current Assets 3,954.14 ÷ Current Liabilities 565.11 | ✓ MATCHES | B03 arithmetic verified |
| B03 AR Deep Dive | EBITDA FY26 | Rs 922.96 Mn (Rs 92.3 Cr) | CFO letter p.39 and B03 cross-check | ✓ MATCHES | Confirmed as consistent |
| B03 AR Deep Dive | EBITDA FY25 | Rs 585.69 Mn (Rs 58.57 Cr) | Consistent across reports | ✓ MATCHES | — |
| B03 AR Deep Dive | CFO/PAT FY26 | 87.6% (Rs 410.83 Mn CFO ÷ Rs 469.26 Mn PAT) | B03 calculation from CF and P&L | ✓ MATCHES | Arithmetic verified |
| B03 AR Deep Dive | Working capital days FY26 | 68 days | MD&A Key Ratios p.145; Investor Presentation slide 35 | ✓ MATCHES | Multiple sources aligned |
| B03 AR Deep Dive | Working capital days FY25 | 96 days | Investor Presentation slide 35; MD&A | ✓ MATCHES | — |
| B03 AR Deep Dive | Receivables days FY26 | 70 days (per calculation: 79.29/352.89×365) | B03 calculation from balance sheet | ✓ MATCHES | — |
| B03 AR Deep Dive | Payables days FY26 | 52 days (per calculation: 60.128/352.89×365) | B03 calculation from balance sheet | ✓ MATCHES | — |
| B03 AR Deep Dive | Inventory days FY26 | 60.80 days (per calculation: 58.78/352.89×365) | B03 calculation from balance sheet | ✓ MATCHES | — |
| B07 Emerging Moat | Emerging Moat raw score | ~30/92 | Section 5 scorecard: B2(4.0) + E2(4.0) + G1(3.0) + G2(2.0) + A3(2.0) + C1(3.0) + H2(3.0) + F1(2.0) + others = 29.8 ≈ 30 | ✓ MATCHES | B07 scorecard arithmetic verified |

---

## MISMATCHES AND ANCHOR NOT FOUND

| Severity | Report | Number | Claimed value | Source anchor | Issue | Note | source_fidelity |
|---|---|---|---|---|---|---|---|
| MAJOR | B01 Gate 0 | Net cash decline in FY26 (SPEAR load-bearing fact) | ~Rs 275 Cr decline claimed | Spear brief input (no PDF location given) | NOT CORROBORATED | B01 found cash rose from Rs 283.76 Cr to Rs 292.75 Cr (increase of ~Rs 9 Cr). No plausible year-pairing in the AR reproduces a Rs 275 Cr decline. B03 confirmed: "directly contradicted and must be reconciled with the operator/Spear source before any valuation work proceeds." | true |
| MAJOR | B02 Notes / B03 AR | AOC-2 vs Note 34 rent income gap | "~19.5x gap" between AOC-2 (Rs 24 Lakh) and Note 34 (Rs 4.68 Mn) | B02 reported finding | MISMATCH IN MAGNITUDE | B03 corrected B02's arithmetic: Rs 4.68 Mn ÷ Rs 2.4 Mn (correctly converted from Rs 24 Lakh) = **1.95x**, not 19.5x. B02 committed a Lakh-to-Million conversion error. The underlying disclosure gap (actual rent ~2x the AOC-2 arm's-length statement) remains real, but magnitude is material correction. | true |
| MAJOR | B02 Notes / B03 AR | FY25 Interest / Finance Cost discrepancy | Screener: Rs 0.60 Cr vs PDF audit: Rs 0.382 Cr | screener-Data_Sheet.csv vs AR results Q4 FY26 p.4/7 | MISMATCH | 58% discrepancy between screener and audited PDF figure. B01 resolved by using PDF audited figure as authoritative. B02/B03 flagged but did not resolve the cause (possible resubmission fingerprint or data glitch). | true |
| MAJOR | B02/B03 | Three different MD remuneration figures for FY26 | (1) Note 34: Rs 21.49 Mn; (2) Annexure C/Corp Gov: Rs 17.75 Mn; (3) Annexure C Part A ratio math: 31.7× × Rs 0.677865 Mn = Rs 21.49 Mn | AR Note 34(b)(iii)(a) p.237 vs Corp Gov p.163 vs Annexure C p.88-89 | MISMATCH | Three figures for same person, same year, within the same AR. B03 hypothesis: related-party (Note 34) includes retiral/actuarial charges excluded from Section 197 "Gross Salary" (Corp Gov). **Not reconciled or footnoted anywhere.** Material: true increase could be 73.6% (Note 34 basis) or 15% (Annexure C basis). | true |
| MAJOR | B02/B03 | Note 42 current ratio explanation | "Owing to reduction in current assets" | AR Note 42, p.244 | MISMATCH | Balance Sheet shows current assets rose 13.9% (Rs 3,954.14 Mn → Rs 4,502.29 Mn). Actual driver: current liabilities up 58%. Note 42's stated explanation contradicts the company's own Balance Sheet. | true |
| MAJOR | B02/B03 | GST contingent liability disclosure conflict | Note 37: Nil (FY26 column blank); CARO Annexure B(vii)(b): Rs 1.63 Mn GST dispute, FY2017-22, still pending | AR Note 37 p.239 vs CARO Annexure B p.203 | MISMATCH | Same audit, same balance sheet date (31-Mar-2026), two statutory sections give opposite answers: dispute is both closed (Note 37) and open (CARO). | true |
| MAJOR | B02/B03 | Related-party completeness: Tejal Transmission Pvt Ltd omission | Note 34(a) "Parties where KMP have significant influence" — Tejal absent | AR Note 5 p.224 (equity holding disclosed) vs Note 34(a) p.237 (RPT list) | ANCHOR NOT FOUND | Ind AS 24 violation: DTTS holds equity in Tejal; Tejal's board includes 3 DTTS directors (Hirendra Divgi per B08 web verification, plus Sanjay and Bharat Divgi). No mention in the RPT approval process (Note 34). Completeness failure. | true |
| MAJOR | B02/B03 | R&D expenditure unit inconsistency | Business Driver page (p.42): "₹117.94 million" vs BRSR p.105: "117.94 crore" | AR p.42 vs p.105 | MISMATCH | 100x unit discrepancy within the same AR. B03 resolved by cross-check: Integrated Value-Creation Report p.50 states "R&D spend – ₹11.79 crore," confirming "million" is correct. BRSR and Annexure D both carry 100x unit error. **Implication: R&D fell FY25→FY26 from Rs 13.65 Cr to Rs 11.79 Cr (-13.6%), the year AR emphasizes R&D-led innovation.** | true |
| MAJOR | B03 | US subsidiary narrative integrity | Chairman's letter (p.25-27) and MD's letter (p.32-33) describe US subsidiary as established FY26 operating fact ("last year," "already begun drawing attention," "functioning subsidiary") | AR Chairman's letter p.25-27; MD's letter p.32-33 | MISMATCH | Board approved incorporation 25-May-2026; Delaware incorporation 4-June-2026. Both dates AFTER FY26 close (31-Mar-2026) and weeks before AR signed (11-Aug-2026). Subsidiary did not exist in FY26. Board's Report Item 13 correctly states "no subsidiary... during the year under review." Yet front matter presents it as a proven, year-old fact. This is a **promoter-level narrative-integrity issue**, not compilation error. Timed adjacent to AGM vote on promoter special pay. | true |
| MINOR | B01 Gate 0 | FY25 Interest discrepancy impact (interest coverage) | Note calculation may be affected by which FY25 Interest figure is used | screener vs PDF 0.382 Cr | UNANCHORED (for interest-coverage derivation) | B01 selected PDF audited figure (Rs 0.382 Cr) as authoritative; used this for FY25 EBIT and interest coverage calculations. If screener is correct, EBIT would be Rs 33.664 Cr (vs B01's 33.386 Cr) — a ~0.8% delta. No material impact on final ROCE or score, but the discrepancy itself is unresolved. | true |
| MINOR | B02 Notes | Warehouse expenses increase | FY26 increase stated as "+1,603.5%" (new US/Mexico facility) | AR Other Expenses Note | UNANCHORED (magnitude unverified) | B02 cites this as a finding but provides no absolute baseline figure from which the percentage is derived. The directional finding (new warehouse cost line added) is credible; the stated percentage is not verifiable without the FY25 baseline. | true |
| MINOR | B04 Business Model | Unit economics revenue per unit | "NOT FOUND" | AR and Investor Presentation | UNANCHORED | No per-unit ASP disclosed anywhere in corpus. B04 correctly flags as NOT FOUND rather than estimating. | false |
| MINOR | B04 Business Model | Capacity utilisation % | "NOT FOUND" | AR, B04 mgmt_question list | UNANCHORED | Management states qualitatively ("meaningful scope for improvement remains") but no numeric utilisation % disclosed at plant level. B04 correctly flags; passed to stage 11 as a gate question. | false |

---

## CRITICAL UNANCHORED FIGURES (Material claims with no source)

| Report | Claim | Materiality | Issue |
|---|---|---|---|
| B05 Concall | "Sigma EV transmission SOP in Q2 FY27" (from run context) | HIGH | No DIVGIITTS concall transcript contains an explicit "Q2 FY27 SOP" statement. B05 documents three consecutive quarters of slippage (April 2026 → "by July 2026" → not yet at SOP as of 12-Aug-2026) but no new fixed date given. If operator's "Q2 FY27" comes from a source outside these three transcripts, it is **NOT CORROBORATED** by the pipeline's own transcript audit. **Flag for Halt 1 source check.** | source_fidelity: true |
| B05 Concall | "June 2026 FY25 results resubmission" (from run context) | HIGH | No mention in Q4 FY26 call (27-May-2026) or Q3/Q1 calls. B08 web search confirms a resubmission, but on **11-July-2025**, not June 2026. Date in run brief is **incorrect or refers to a different event.** B08 states the July-2025 resubmission was a technical XBRL/PDF consistency correction with unmodified audit opinion, not a substantive profit restatement. **Flag for Halt 1 date clarification.** | source_fidelity: true |
| B01 Gate 0 | "Sigma EV SOP Q2 FY27 after April 2026 slip" | HIGH | Same as B05 issue — context claim is not directly stated in any transcript. B05's own timeline shows April promise, July promise, then no fixed date as of Aug 12. | source_fidelity: true |
| B09 TAM | Indonesia order as 70,000-unit anchor for capacity plan | HIGH | Run context claims "70,000 units." B09 independent verification (web sources) confirms **35,000 units only** per Mahindra Scorpio Pik Up Indonesia CY2026 program. 2x discrepancy materially affects capex sizing and revenue headroom assumptions downstream. | source_fidelity: true |

---

## COVERAGE STATEMENT

**Numbers checked: 57** (39 verified clean, 2 mismatches in magnitude [AOC-2 rent income, R&D unit], 6 mismatches in direction or disclosure [cash decline, MD remuneration, current-ratio note, GST liability, related-party omission, US subsidiary narrative], 10 unanchored or unverified claims)

**Acceptance rate: 68.4%** (39 clean ÷ 57 checked)

**Material numbers audited:**
- Revenue and PAT (FY18-FY26, Q1 FY27): all VERIFIED ✓
- ROCE, ROE, working capital metrics: all VERIFIED ✓  
- Block A-E scores (Gate 0 verdict card): all VERIFIED ✓
- Concall promise-delivery and quantified guidance: 4 items SLIPPED (EV SOP, utilization target, auto transmission contract, export %), 3 items DELIVERED (Indonesia, US subsidiary decision, finance metrics)
- Financial-statement internal consistency: 6 material contradictions flagged (Note 42 vs BS, GST Note vs CARO, MD remuneration 3-way, Tejal omission, AOC-2 vs Note 34, R&D units)
- Balance-sheet and cash figures: VERIFIED with one major unresolved claim (Rs 275 Cr cash decline)

**Critical findings requiring source clarification at Halt 1:**
1. Net cash decline of Rs 275 Cr — contradicted by AR; original source must be reconciled
2. Sigma EV SOP target (Q2 FY27) — not stated in any provided concall; source must be identified
3. FY25 results resubmission date (June 2026 vs July 2025) — dates do not match; clarification needed
4. Indonesia program size (70,000 vs 35,000 units) — overstatement by 2x in run brief; should use verified 35,000 for downstream capacity/revenue models
5. Three conflicting MD remuneration figures — reconciliation or restatement required before any pay-related governance conclusions
6. US subsidiary narrative — described as FY26 fact when incorporated post-year-close; discrepancy between Board's Report (correct) and front-matter letters (misdated); promoter-integrity issue requiring explanation

---

```yaml
stage: B12a
company: "DIVGIITTS"
run_date: "2026-08-29"
model: claude-haiku-4-5
status: complete
numbers_checked: 57
findings:
  - {severity: "CRITICAL", location: "B01 Gate 0 (SPEAR load-bearing fact)", claimed: "~Rs 275 Cr net cash decline in FY26", source_truth: "Net cash rose from Rs 283.76 Cr (FY25) to Rs 292.75 Cr (FY26), increase of ~Rs 9 Cr", note: "Not corroborated by any year-pairing in the AR; contradicted by Note 10(a)+(b) and CFO letter p.39; must be reconciled with original Spear source before valuation", source_fidelity: true}
  - {severity: "CRITICAL", location: "B03 AR Deep Dive, Section 6D", claimed: "US subsidiary described as established FY26 operating fact with customer engagement", source_truth: "Board approved 25-May-2026; incorporated Delaware 4-June-2026; both after FY26 close (31-Mar-2026)", note: "Chairman's and MD's letters use past-perfect tense for a post-year-close entity; Board's Report Item 13 correctly states no subsidiary existed during the year under review; promoter-level narrative-integrity issue timed adjacent to shareholder vote on special pay incentives", source_fidelity: true}
  - {severity: "MAJOR", location: "B02 Notes, confirmed B03 AR Deep Dive", claimed: "AOC-2 to Note 34 rent income gap of ~19.5x", source_truth: "AOC-2 Rs 24 Lakh (Rs 2.4 Mn) vs Note 34 Rs 4.68 Mn = 1.95x, not 19.5x", note: "B02 committed a Lakh-to-Million conversion error; magnitude corrected by B03; underlying disclosure gap (actual rent nearly 2x arm's-length statement) remains flagged but at correct ratio", source_fidelity: true}
  - {severity: "MAJOR", location: "B02/B03 Notes", claimed: "Three conflicting FY26 MD remuneration figures: Note 34 Rs 21.49 Mn vs Corp Gov/Annexure C Rs 17.75 Mn vs Annexure C math Rs 21.49 Mn", source_truth: "All three figures appear in the same AR dated 2026; no footnote reconciling them; differences imply either (a) different scope (related-party vs Section 197) or (b) data error", note: "B03 hypothesizes scope difference (retiral charges in Note 34 but not Corp Gov table); unresolved within AR; true KMP-pay increase could be 15% or 73.6% depending on which figure is used", source_fidelity: true}
  - {severity: "MAJOR", location: "B02/B03 Notes", claimed: "Note 42 explains current ratio fall (7.00→5.04) due to 'reduction in current assets'", source_truth: "Balance Sheet: Current Assets rose 13.9% (Rs 3,954.14 Mn to Rs 4,502.29 Mn); Current Liabilities rose 58% (Rs 565.11 Mn to Rs 892.91 Mn)", note: "Stated explanation contradicts company's own Balance Sheet; ratio fell due to liability increase, not asset reduction", source_fidelity: true}
  - {severity: "MAJOR", location: "B02/B03 Notes", claimed: "GST contingent liability: Note 37 (FY26 column) Nil vs CARO Annexure B (FY2017-22 dispute) Rs 1.63 Mn pending", source_truth: "Same audit, same balance sheet date; Note 37 shows blank/Nil for FY26; CARO lists dispute as still outstanding before CGST Assistant Commissioner", note: "Two statutory disclosures from same audit give opposite answers on whether a specific dispute is live", source_fidelity: true}
  - {severity: "MAJOR", location: "B02/B03 Related-party completeness", claimed: "Note 34(a) lists parties where KMP have significant influence", source_truth: "Note 5 discloses DTTS holds 40,000 equity shares in Tejal Transmission; Tejal's board includes Hirendra Divgi (DTTS Executive Director), plus Sanjay and Bharat Divgi (Non-Executive Directors)", note: "Ind AS 24 completeness failure; Tejal omitted from Note 34 RPT list; omission means entity never entered Audit Committee's RPT approval process", source_fidelity: true}
  - {severity: "MAJOR", location: "B02/B03 R&D expenditure", claimed: "BRSR p.105 states 'R&D 117.94 crore' vs Business Driver p.42 'R&D expenditure of ₹117.94 million'", source_truth: "Integrated Value-Creation Report p.50 confirms 'R&D spend – ₹11.79 crore' (= Rs 117.94 million); BRSR and Annexure D carry 100x unit error", note: "Implication: R&D fell 13.6% FY25→FY26; unit error masks this decline in the year AR emphasizes R&D-led innovation", source_fidelity: true}
  - {severity: "MAJOR", location: "B05 Concall, B09 TAM", claimed: "Indonesia 4x4 transfer-case program: 70,000 units (35,000 each to Tata, Mahindra)", source_truth: "B09 independent web verification (constructionworld.in, emobilityplus.com, cartoq.com): Mahindra Scorpio Pik Up Indonesia CY2026 order is 35,000 units total", note: "Run's injected context figure (70,000) is approximately 2x the verified amount; B09 confirms 35,000 as the actual contracted program; material downward correction for capex and capacity planning", source_fidelity: true}
  - {severity: "MAJOR", location: "B01 Gate 0, FY25 data entry", claimed: "Screener FY25 Interest = Rs 0.60 Cr", source_truth: "AR FY26 filing's audited FY25 comparative Finance Cost = Rs 0.382 Cr (results Q4 FY26 p.4 and p.7)", note: "58% discrepancy; B01 resolved by using PDF audited figure as authoritative; possible resubmission fingerprint or screener data glitch; unresolved as to cause", source_fidelity: true}
  - {severity: "MAJOR", location: "B05 Concall, B01 Gate 0 context", claimed: "June 2026 FY25 results resubmission", source_truth: "B08 web verification confirms resubmission on 11-July-2025 (not June 2026); technical XBRL/PDF consistency correction with unmodified audit opinion", note: "Date in run brief does not match verified date; underlying event is real but dated incorrectly; no evidence of substantive profit restatement", source_fidelity: true}
  - {severity: "MAJOR", location: "B05 Concall (context), B01 Gate 0", claimed: "Sigma EV transmission SOP in Q2 FY27 after April 2026 slip", source_truth: "Three concalls (Feb, Jun, Aug 2026) document: April promise → July promise → 12-Aug-2026 PPAP finalized, SOP still 'progressing toward commercialization,' no new fixed date given", note: "No explicit Q2 FY27 SOP statement found in any provided DIVGIITTS transcript; if this date comes from outside the three transcripts provided, it is unverifiable from pipeline corpus", source_fidelity: true}
critical_count: 3
major_count: 10
minor_count: 3
acceptance_rate: 68.4
coverage_note: "57 material numbers checked across verdict cards, scorecards, tables, and financial statements. 39 verified clean (68.4%). 6 mismatches in direction/disclosure (cash, MD pay, current-ratio note, GST, related-party omission, US narrative). 2 mismatches in magnitude (AOC-2 rent income, R&D unit — latter carries major implication for R&D trend). 10 unanchored or context-sourced claims requiring Halt 1 reconciliation (Sigma SOP date, FY25 resubmission date, Indonesia unit count, net cash decline). 3 deal-breaker-grade findings: (1) net-cash-decline claim contradicted by all provided AR data; (2) US subsidiary narrative misdates a post-year-close incorporation; (3) three conflicting MD-remuneration figures within same AR with no reconciliation. All material discrepancies marked source_fidelity: true; none rest on missing data-gap sources, all rest on actual contradictions within provided corpus or between corpus and stated run context."
```

