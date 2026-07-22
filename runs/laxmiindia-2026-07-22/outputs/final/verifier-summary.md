# Verifier summary (Phase 1)

Confidence delta: overall 83. Numerical acceptance 83 (B12a), red-flag coverage 94 (B12b), framework adherence 94.5 Gate 0 + EM portion (B12c, valuation component pending phase 3), peer utilisation 100 (B12d).

Acceptance rates: Verifier A 83, Verifier B 65 (fully-caught share; coverage 94), Verifier C 94.5 (Gate 0 + EM only), Verifier D 100.

Source-fidelity gate: HELD. Verifier A found 0 source-fidelity failures on any verdict-card or scorecard input. The 4 ANCHOR-NOT-FOUND items are evidence gaps, not fabricated or misread verdict inputs. REWORK not triggered.

Findings sorted CRITICAL first, then MAJOR, then MINOR. Only what the verifiers wrote.

## CRITICAL

| Verifier | Location | Finding |
|---|---|---|
| A | B01 Gate 0, Block C | Revenue CAGR 34.75% VERIFIED (DRHP p.76 Rs 130.668 Cr FY23; AR26 Rs 319.590 Cr FY26). All components confirmed. Clean. |
| A | B01 Gate 0, Block C | PAT CAGR 45.81% VERIFIED (DRHP p.76 Rs 16.028 Cr FY23; AR26 Reg.52(4) Rs 49.676 Cr FY26). Exact match. |
| A | B01 Gate 0, Block A | Median ROCE 16.28% VERIFIED (median of 15.55/16.37/16.46/16.19 exact; ROCE adaptation sourced to DRHP Note 34/IP ALM). |
| A | B01 Gate 0, Block D | CRAR FY26 26.12% VERIFIED (AR26 Reg.52(4); IP p.10). Clean. |
| A | B02 Notes | DA/ARC gain FY23 76.1% of PAT VERIFIED (Note 52.2/98(a), DRHP p.355,379). Core earnings-quality finding, corroborated at UGRO (B06). |
| A | B02 Notes | Stressed-loan transfers to ARC jump >36x FY24-FY25 (Rs 7.27 Cr to Rs 264.8 Cr, Note 98(c) p.379) VERIFIED (36.4x). Includes SMA pre-NPA accounts first time in FY25. |
| A | B02 Notes | FY25 NPA-to-ARC ~180x gap VERIFIED (Note 98(c) Rs 109.54 Cr vs Note 75 Rs 0.61 Cr = 178.7x). No reconciling note; accounting-treatment ambiguity stands. |
| A | B02 Notes | Gross Stage-3 trend 0.58%/0.73%/1.07% FY23-FY25 VERIFIED. Deterioration pre-dates the Up Money FY26 spike to 2.13%. |

## MAJOR

| Verifier | Location | Finding |
|---|---|---|
| D | 06-peers.md Q2 verdict + verified[] | Verdict-label discipline: "DA/securitization gain-on-sale materially drives NBFC PAT/NIM quality" labeled VERIFIED on one peer (UGROCAP, 3 anchors, one call); Rule 4 requires >=2 independent peers, so it should read PARTIALLY VERIFIED. Underlying UGRO evidence checked out verbatim (PAT Rs 43 Cr to Rs 6 Cr, "50-60% of ROA", derecognition-gain quotes). Discipline issue, not a fabrication. |
| A | B01 Gate 0, Block A | Median ROE 13.25%: median arithmetic correct, but FY26 component selection unexplained (report carries 13.73% audited yet derives 13.75%, 0.02pp gap). Minor precision issue on a MAJOR line. |
| A | B01 Gate 0, Block D | PCR FY26 49.43% VERIFIED (IP p.11). Consistent with GNPA rise including Up Money. |
| A | B01 Gate 0, Block E | Promoter holding post-Offer 70.22% VERIFIED (DRHP p.99); ~10pp gap vs first post-listing screener 60.45% unexplained, no SHP filing to reconcile. Flagged. |
| A | B02 Notes | FY26 ARC SR investments 5.4x (Rs 29.27 Cr to Rs 158.91 Cr) VERIFIED (5.43x). Loan book grew 31% same period; disproportion real. |
| A | B04 Business Model | Total Income FY26 Rs 319.590 Cr, Interest Income Rs 299.12 Cr, Fee & commission Rs 15.53 Cr all VERIFIED to AR26 P&L. Clean. |
| A | B05 Concalls | AUM 35-40% promise VERIFIED; DELIVERY MISS +27% (Rs 1,277 Cr to Rs 1,626 Cr). Correctly flagged. |
| A | B05 Concalls | Branches 35-44 promise VERIFIED; MISS +18 (159 to 176), guidance cut twice. Correctly flagged. |
| A | B05 Concalls | Cost of borrowing -100/125bps promise VERIFIED; SHORTFALL -68bps (11.48% to 10.80%). Correctly flagged. |
| A | B05 Concalls | Rating "at least two-notch" promise VERIFIED; delivered one notch (A-/Positive to A/Stable). Correctly flagged. |
| A | B05 Concalls | PAT ~50% promise VERIFIED; delivered +38.2% (Rs 36 Cr to Rs 49.76 Cr). Partial miss. |
| A | B05 Concalls | Q4 DA pool upfront profit Rs 8.66 Cr from Rs 41 Cr pool VERIFIED (IP slide 6). Clean. |
| A | B05 Concalls | Q1 NIM 9.66% restated to 10.43% (Q2 call): ANCHOR NOT FOUND in transcript pages reviewed; "misprint" cited, no reconciliation. Core finding sound, exact page anchor unconfirmed. |
| A | B05 Concalls | Q3 FY26 collection efficiency 89%: WEAK ANCHOR, cited but not independently verified in transcript. Direction sound (below FY25 96.76%). |
| A | B07 Emoat | Branches FY23 119 to FY26 176 VERIFIED; AUM per branch Rs 57.7 mn to Rs 92.4 mn VERIFIED. Clean. |
| A | B07 Emoat | Yield on avg loans FY23 21.34% / FY25 21.92%: ANCHOR NOT FOUND at page level; direction consistent. |
| A | B07 Emoat | Gross Stage-3 1.07% FY25 VERIFIED (12.183/1,140.24). Clean. |
| A | B08 Promoter | Director DOBs (Deepak/Prem Devi/Aneesha Baid): ANCHOR NOT FOUND in prospectus pages reviewed; ages arithmetically consistent, not independently verified. Evidence gaps. |
| A | B08 Promoter | Aneesha Baid FIR 19-Sep-2024, No. 0380 (IPC 406/420, land dispute) VERIFIED (PROSPECTUS p.426). Governance red flag properly sourced. |
| A | B08 Promoter | Deepak Baid FIR 26-Nov-2003 (Baid Finance truck matter, pending 22+ yrs) VERIFIED (pp.426-427). |
| A | B08 Promoter | Hirak Vinimay shareholding (Ananya/Hunar/Vivan BFT + Prem Devi) VERIFIED (pp.270-273). Clean. |
| A | B09 TAM | NBFC MSME AUM Rs 3.3 lakh Cr VERIFIED (DRHP p.151, CareEdge, Mar-24E). Management TAM Rs 26 lakh Cr VERIFIED as all-lender full-penetration demand, correctly flagged not NBFC-only. |
| A | B01 Gate 0 | CFO/PAT FY23-FY26 -10.57x/-9.89x/-8.67x/-5.63x VERIFIED. Structural NBFC pattern, not per se cash-quality red flag. |
| A | B01 Gate 0 | PBT FY26 Rs 66.047 Cr, Finance Costs Rs 137.34 Cr, Total Assets Rs 1,817.78 Cr, Net Loans Rs 1,480.10 Cr (0.04% rounding), Interest coverage 1.48x, D/E 2.87-2.88x all VERIFIED to AR26. Clean. |
| A | B02 Notes | Cumulative CFO -Rs 984.42 Cr, Capex -Rs 17.79 Cr FY23-FY26 VERIFIED. Clean. |
| A | B01 Gate 0 | FY26 current liabilities Rs 561.10 Cr: ANCHOR NOT FOUND from IP ALM table; source basis shifts DRHP Note 34 to IP, consistency break noted. |
| D | 06-peers.md ARMANFIN rows | ARMANFIN GNPA/NNPA labeled "on-book" in B06 narrative where Q1 source says "consolidated level" and Q4 basis unstated; values match transcripts exactly. (MINOR per D, listed here for the peer set.) |

## MINOR

| Verifier | Location | Finding |
|---|---|---|
| C | B01 Block A / A4 ROCE trend | 0.27pp ROCE decline falls in an unspecified band gap; maker scored 3 (conservative), 5 arguable; immaterial to classification (AVOID either way). |
| C | B01 deal-breaker #6 | ND/EBITDA ~6.3x AND IC ~1.48x FY26 literally triggers deal-breaker #6 to AVOID but not applied; maker cites duplication with D1 CRAR redirection; outcome-neutral; no NBFC carve-out in prompt text; flagged for operator ruling. |
| C | B07 scorecard / D1 multiplier | Search-tier D1 multiplied at 0.7x instead of the mandated 0.5x, inflating em_score to 29.4 vs strict 29.2; STRENGTHENING band unchanged. |
| B | B05 red-flag table 4D | Q2 sequential disbursement drop (~Rs 166 Cr to Rs 145 Cr, conceded under Anmol Das) not flagged despite contradicting "healthy disbursement" framing. |
| B | B05 2D/3B | Own-sourced-vs-DA-purchase business-model contradiction not drawn out (100% own-sourced claim vs buying third-party pools, Q3 p.18). |
| B | B05 2A promise #8 | Collection-efficiency decline 94.92% to 89% under-weighted; collections framed as the one DELIVERED positive. |
| B | B05 4D | Low PCR (~47-49%) vs rising NNPA to 1.4% noted only as a Q4 "real risk", not carried into the red-flag table. |
| B | B05 header note line 10 | Q3 "Knowledge Session" format for the quarter the Up Money default surfaced noted neutrally, not weighted as an optics/governance concern. |
| B | B05 Section 2 | Intra-Q1 numeric inconsistencies (NIM 9.99% MD vs 9.66% CFO same call; rating wording) not surfaced (Verifier A domain). |
| A | B01 Gate 0, Block E | Promoter holding change 29.2pp (99.41% to 70.22%) VERIFIED; cause documented as dilutive raises + IPO OFS. Clean. |

## Verifier count summary

Verifier A (numerical): 5 CRITICAL, 38 MAJOR, 2 MINOR across 47 numbers; 39 clean, 4 ANCHOR-NOT-FOUND evidence gaps, 2 weak anchors, 0 critical mismatches on verdict/scorecard inputs.
Verifier B (red-flags): 0 CRITICAL, 0 MAJOR, 6 MINOR; 17 independent flags, 11 caught + 5 partial (94% coverage); 5/5 promise-delivery spot checks confirmed; concurs credibility grade D.
Verifier C (framework, Gate 0 + EM only): 0 CRITICAL, 0 MAJOR, 3 MINOR; 52/55 rules passed; valuation audit deferred to phase 3.
Verifier D (peers): 0 CRITICAL, 1 MAJOR, 1 MINOR; 4/4 peers used substantively; two headline findings confirmed verbatim.
