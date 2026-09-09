# Verifier summary, KABRAEXTRU, run 2026-09-05 (phase 1)

## Phase 1 confidence delta

| Component | Acceptance rate | Verifier | Model | Basis |
|---|---|---|---|---|
| Numerical acceptance | 93.3 | B12a | claude-haiku-4-5 | 45 figures checked, 0 CRITICAL, 0 MAJOR, 3 MINOR, 0 source fidelity findings |
| Red flag coverage | 23.0 | B12b | claude-opus-4-8 | 30 independent flags found, 7 caught, 9 partially caught, 15 missed; 1 CRITICAL, 12 MAJOR, 13 MINOR; credibility grade D concurred |
| Framework adherence | 93.8 | B12c | claude-opus-4-8 | Phase 1 scope only: 58 Gate 0 rules and 38 Emerging Moat rules; 0 CRITICAL, 0 MAJOR, 6 MINOR; valuation half deferred to phase 3 |
| Peer utilisation | 83.0 | B12d | claude-sonnet-5 | 6 peers audited, 5 substantive confirmed, 0 CRITICAL, 1 MAJOR, 7 MINOR |
| **Overall** | **23.0** | min of four | | Band: FORCED REWORK (below 60) |

Rework triggers recorded: any verifier acceptance below 60 is true (B12b at 23.0); B12a CRITICAL is false; overall below 60 is true.

Verifier A coverage scope: 45 material figures across 01-gate0, 02-notes (all passes) and 03-ardeep, plus the annual report internal consistency items. Sources opened: screener Data_Sheet, AR FY26, AR FY25. Peer transcript page anchors in 06-peers were audited by verifier D. Figures in stages 07, 08 and 09 were not separately enumerated by verifier A.

Verifier C scope note (recorded as INFO, not a defect): valuation adherence (B10 and B11) and the Business Understanding Narrative are pending phase 3. Neither artifact existed at verification time, so no rule was failed against them. Both must be audited in the phase 3 pass.

---

## CRITICAL (1)

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| 1 | B12b | 05-concall report, Sections 2D and 4D; source AR FY26 Note 23, p.95; loss at AR FY26 p.17 | MISSED: unexplained Rs 1,668.41 lakh "Other" line inside other income (FY25: Rs 22.91 lakh), unlabelled and unexplained, which determines the size of the reported FY26 standalone pre tax loss of Rs 423.21 lakh. Without it the loss is roughly 8 times larger. Neither 05-concall nor 06-peers opens the other income note. |

---

## MAJOR (13)

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| 2 | B12b | 05-concall report, Section 2C/4D; source AR FY25 p.38 and p.4 | MISSED: the FY25 report states three different PAT figures for FY25, two of them on the same page. Table PAT Rs 34 Cr at 7.2 percent margin, prose "PAT stood at Rs 32 crores. PAT margin stood at 6.8%", chairman's letter Rs 33.9 Cr at 7.2 percent. Stage 5 caught only the analogous FY26 EBITDA inconsistency. |
| 3 | B12b | 05-concall report, Section 2A/2D; source AR FY25 p.19 (Notes 26, 29) against AR FY26 p.17 and standalone Note 47 | MISSED: silent restatement of FY25 comparatives, an exactly offsetting Rs 421.14 lakh reclassification between standalone employee benefits expense (5,907.53 to 6,328.67 lakh) and other expenses (7,473.91 to 7,052.77 lakh), in both standalone and consolidated columns, covered only by boilerplate "regrouped wherever considered necessary". |
| 4 | B12b | 05-concall report, Section 3D; source AR FY26 Note 9 ageing tables, p.88; MD&A ratio table p.37 | MISSED: Rs 4,428.68 lakh of Rs 9,052.43 lakh gross receivables, 48.9 percent, more than one year overdue at 31-Mar-2026, up from 41.8 percent. Rs 1,935.36 lakh over three years carried at Rs 455.13 lakh provision, 23.5 percent cover. The MD&A reports only "Debtors Turnover 5.20%" with no reason. |
| 5 | B12b | 05-concall report, Section 2A row 4; source AR FY26 p.36 against Note 38, p.105-106 | MISSED: the "Technology-Agnostic and Asset-Light Approach in Energy Business" Key Strength is contradicted by the company's own segment note. Battery Division segment assets Rs 36,437.25 lakh, 50.1 percent of total segment assets, on segment revenue Rs 13,610.84 lakh, 0.37 times asset turn, with a Rs 4,334.64 lakh segment loss and about Rs 250 Cr stated as invested. |
| 6 | B12b | 05-concall report, Section 2C/4D; source AR FY26 p.37 and p.17 | MISSED: the Key Financial Ratios table is internally unreconcilable and incomplete. Interest Coverage Ratio reported as plus 39.20 percent in a year the same report shows EBIT falling Rs 45 Cr to Rs 7.16 Cr and finance cost rising from 1,117.31 to 1,139.25 lakh. Both Interest Coverage (plus 39.20 percent) and ROCE (minus 86.50 percent) exceed the 25 percent threshold and carry blank "Reasons for Variation". |
| 7 | B12b | 05-concall report, dropped_triggers list; source AOC-1 at AR FY25 p.25 and AR FY26 p.23; claim at AR FY25 p.37 and deck p.17 | MISSED: Varos Technology Pvt Ltd, the subsidiary carrying the battery management system capability claim, collapsed. Turnover 372.99 to 17.84 lakh, down 95 percent; loss 221.24 to 291.49 lakh; reserves negative 557.17 lakh against Rs 1.00 lakh capital, so negative net worth. Named a Key Strength in AR FY25 and in the Dec 2023 deck, absent from all AR FY26 narrative. |
| 8 | B12b | 05-concall report, Section 2A row 3; source AR FY25 p.19 and p.4 | MISSED: FY25 profit was flattered by a Rs 848.98 lakh exceptional gain on the Penta divestment (PBT before exceptional 3,343.28 lakh against reported 4,192.26 lakh). The chairman's letter reports PAT Rs 33.9 Cr at 7.2 percent margin without mentioning that about 25 percent of pre tax profit was a one off, and FY26 is then measured against that base throughout. |
| 9 | B12b | 06-peers report, Part 1 claim set; source RAJOOENG Q2 FY24, 6-Nov-2023, PDF p.10, p.11, p.12; AR FY26 Note 9 p.88 | MISSED: no claim tests working capital, where the peer corpus supplies a direct quantified contrast. Rajoo takes 35 to 40 percent advance on order finalisation, states "95% cases there are always 100% payment before we dispatch", and reports 22 receivable days, against the main company carrying 48.9 percent of receivables more than one year overdue. |
| 10 | B12b | 05-concall report, Section 3B, second bullet; source AR FY25 p.4-5, p.35; AR FY26 p.33 | INCORRECT SUB-FINDING: stage 5 states the FY25 and FY26 plastic pipe market citations are "internally consistent". They differ by roughly 2.7 times for the same market in the same year, Rs 500 bn against USD 2.10 bn, roughly Rs 185 bn, with the source switched to IMARC and no reconciliation. |
| 11 | B12b | 06-peers report, Claim 3 verdict; source RAJOOENG Q4 FY24 PDF p.7, p.11 and Q2 FY25 PDF p.6, p.11-12 | UNDER-CALLED: Claim 3 ruled UNVERIFIABLE although the peer supplies quantified domestic market sizing of Rs 1,500 to 2,000 Cr, which puts KABRAEXTRU's Rs 314.89 Cr extrusion revenue at 16 to 21 percent share, not about 40 percent. The verdict should be PARTIALLY CONTRADICTED. |
| 12 | B12b | 05-concall report, Section 1C and 3B; source AR FY26 p.34 against Note 38, p.105 | PARTIALLY CAUGHT: the roughly 100 times EV battery pack TAM swing was found, but not that the FY26 figure cited (USD 53.76 mn for all India in 2026) is smaller than Geon's own revenue implies, at roughly 28 percent of that market. |
| 13 | B12b | 05-concall report, Section 2D and 4D; source AR FY26 p.51 and p.20, AR FY25 p.49 | PARTIALLY CAUGHT: the FY26 downgrade silence was found. Missed that the 13-May-2026 downgrade contradicts the 28-May-2026 Director's Report item 12 "no material changes" statement, and that the FY25 downgrade was equally undiscussed, making it a repeated omission across two reporting periods. |
| 14 | B12d | 06-peers report, Part 3 coverage map, WINDMACHIN row; anchor inputs/screening/WINDMACHIN-Data_Sheet.csv rows 10-11 (FY26 column) and rows 27-28 (quarterly columns through 2026-06-30) | Claimed "WINDMACHIN listed UNUSED, no transcript in corpus". True but incomplete: the Windsor screening CSV in corpus reaches the FY26 window and the June 2026 quarter, the only peer data source in this corpus that does, and was never mentioned, even to caveat it out of scope. It shows FY26 sales up 72.9 percent to Rs 566.52 Cr against Rs 327.6 Cr, with net profit still negative and an equity capital and investments spike suggesting the growth may be acquisition driven. It bears directly on Claims 1, 5 and 6 and on the report's own central staleness limitation. |

---

## MINOR (29)

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| 15 | B12a | 02-notes Rank 8 / 03-ardeep; source AR FY26 Note 3 subsidiary disclosure | Claimed Varos net worth Rs (6.96) Cr. Loss magnitude and negative net worth status confirmed through consolidated loss attribution (54.32 percent of the Rs 5.37 Cr loss, Rs 2.91 Cr). The exact negative net worth figure was not independently located in the PDF snapshots reviewed. Not load bearing to any Gate 0 decision. source_fidelity: false. |
| 16 | B12a | 02-notes Rank 12 / 03-ardeep; source Directors' Report Annexure-4 FX flow data, AR FY26 p.28 | Claimed FX exposure Rs 38.21 Cr unhedged, 6.8 times growth from Rs 5.61 Cr. Gross flows confirmed: FX earnings Rs 57.52 Cr down from Rs 64.21 Cr, outgo Rs 107.68 Cr down from Rs 138.67 Cr. Net unhedged direction confirmed; the exact Rs 38.21 Cr figure from Note 34.3(c) was not independently verified in this pass and is not contradicted. source_fidelity: false. |
| 17 | B12a | 01-gate0 Block E2 / Note 14.4; source AR FY25 Note 14.4 p.89 and AR FY26 Note 14.4 | Claimed promoter holding change FY23 of about 0.26pp, derived as FY24 60.24 percent minus the 0.01 percent stated change. Derivation logic is correct: FY23 = 60.23 percent, FY25 = 60.24 percent, FY26 = 60.49 percent with change plus 0.25 percent. The FY23 figure is derived, not directly stated in corpus. FY24 and FY26 directly verified. source_fidelity: false. |
| 18 | B12b | 05-concall report, Section 4D; source AR FY26 p.37 and Note 7, p.87; AR FY25 p.38 | MISSED: the mandatory inventory turnover explanation is factually wrong. "Due to increase in inventory and Lower sale" when Note 7 shows inventory fell from 29,014.77 to 28,538.08 lakh. The sentence is copied verbatim from the FY25 table where it was true. |
| 19 | B12b | 05-concall report, dropped_triggers; source AR FY25 p.36 against AR FY26 p.35 and p.5 | MISSED: heritage and scale claims quietly shrunk and self contradictory. "Over six decades of industry experience, a track record of more than 15,000 successful installations" (AR FY25) becomes "a legacy of over four decades" with no installation count (AR FY26), while the FY26 chairman's letter in the same report says "its 60-year journey". |
| 20 | B12b | 05-concall report, dropped_triggers; source deck p.24; AR FY25 p.37, p.21, p.25; AR FY26 p.36 | MISSED: the Penta JV, listed as one of three technical collaboration "Pillars of Strength" in the Dec 2023 deck as a "50:50 JV with Penta SRL, Italy", was removed from the AR FY25 collaboration table with no narrative comment. AOC-1 records the holding as 49.94 percent, not 50:50. AR FY26 drops the whole collaboration table including the 1983 Battenfeld-Cincinnati tie up. |
| 21 | B12b | 05-concall report, Sections 2B and 2D; source AR FY26 MR-3, p.24; Director's Report item 23, p.21 | MISSED: FY26 secretarial audit exception not recorded by the pipeline. Shares for FY2017-18 unclaimed dividend were transferred to IEPF on 31-Oct-2025, "beyond the timelines prescribed under Section 124". A genuine volunteered negative that also evidences a compliance lapse. |
| 22 | B12b | 05-concall report, Section 2D; source AR FY26 p.18, p.25, p.39-40 | MISSED: governance optics. Mr Bajrang Lal Bagra completed his second five year Independent Director term on 26-Aug-2025 and was appointed Non-Executive Non-Independent Director with effect from 11-Sep-2025, sixteen days later. The FY26 board composition table lists him twice, once under each category. |
| 23 | B12b | 05-concall report, Section 2C transparency row; source AR FY26 p.4 | PARTIALLY CAUGHT: the EBITDA inconsistency was found but under rated at MEDIUM. The FY26 chairman's letter also drops PAT entirely after giving it in FY25, and never uses the word loss. |
| 24 | B12b | 05-concall report, Sections 2D and 3D; source AR FY26 Note 38, p.106 | PARTIALLY CAUGHT: concentration was reported and the Hero Electric risk section omission was reported, but the two were not joined into the finding that neither year's Risks and Challenges section names customer or customer credit risk at all. |
| 25 | B12b | 05-concall report, Sections 1A and 1B; source AR FY26 p.37, p.36, p.5 | PARTIALLY CAUGHT: the Rs 150 Cr order and the Rs 1,500 Cr plus ceiling were flagged as unanchored, but never tested against each other or against the claimed roughly 7 GWh capacity, which they do not fit. |
| 26 | B12b | 06-peers report, Claims 7 and 8; source HBLENGINE AGM PDF p.4, p.17; AR FY26 p.36 and Note 38 p.105 | PARTIALLY CAUGHT: the segment mismatch reasoning is fair for cell economics, but the peer's "perhaps 200 crores or less ... profit from year one" against Geon's roughly Rs 250 Cr and Rs 43.35 Cr loss needs no segment match and was left undrawn. |
| 27 | B12b | 05-concall report, Section 2A row 3; source deck p.7, AR FY25 p.37, AR FY26 p.37 | PARTIALLY CAUGHT: the FY26 decline is covered, but neither report states that revenue has now fallen three years running: minus 9.7 percent, minus 21.5 percent, minus 5.4 percent from the deck's FY23 base. |
| 28 | B12b | 05-concall report, Section 2D and 4D, HEVPL row | OVERSTATED WORDING: stage 5 says the Hero Electric note is "identical, word-for-word" across both reports. The FY26 version adds a warranty reversal sentence. The core finding, still dated "As at March 31, 2025" with balance and case status not refreshed, is SUPPORTED. |
| 29 | B12b | 05-concall report, Section 2A row 5 and row 3 anchors | ANCHOR IMPRECISION: the "accelerated its R&D" phrase is at AR FY26 p.28, cited as p.29. The nil dividend statement is at AR FY26 p.17, cited as p.18. Neither slip changes a finding. |
| 30 | B12b | Sub-threshold observations, B12b report Part 1 closing section | RECORDED, NOT SCORED: dormant Kabra Mecanor JV with nil turnover two years; FY25 FADA EV figures restated between the two reports from the same source; CSR set off and preceding year table arithmetic inconsistencies. |
| 31 | B12c | 01-gate0 Formula Notes / Block A; rule G-06 | ROCE denominator substituted (Net Worth plus Borrowings) for the fixed Total Assets less Current Liabilities. The literal denominator is not computable from screener-Data_Sheet.csv (no ROCE row, no current and non current split). Claimed median ROCE 10.31 percent giving A1 = 1, Block A = 1, core 22. Strict N/A reading gives A1 = 0, Block A = 0, core 21, grand total 24. Classification AVOID under both. Disclosed twice by the maker and cross validated against AR Note 43 (FY26 0.62 percent against 0.61 percent; FY25 8.63 percent against 8.67 percent). Deal breaker 3 sits 0.31pp away and depends on this basis, but it caps at AVERAGE and cannot bind an AVOID. |
| 32 | B12c | 01-gate0 Block F, M8; rule G-41 | Band language does not describe the evidence. Claimed M8 = 1 under the "mentioned unquantified" band, though the report states reach is quantified but static. No band fits; the strict alternative M8 = 0 moves moat 3 to 2 and grand total 25 to 24. Rubric gap for quantified but static reach. No change to moats confirmed, moat class, or classification. |
| 33 | B12c | 07-emoat mode note / catalysts_12m; rule E-13 | Evidence tier outside the three tier taxonomy: a fourth "media-reported" tier introduced for the 2026 preferential issue. em_score unaffected because the item scores 0 and is held in the optionality register. Phase 3 guard: stage 11 must exclude this catalyst from Pillar 3 or carry the MODERATE cap. It is not pipeline verified evidence. |
| 34 | B12c | 07-emoat block, evidence_mix; rule E-32 | Item counts not substantiated in the report body. Claimed {documented: 25, claim: 10, inference: 6}. Not verifiable; only the recount line, 9 documented items across 4 categories, is auditable. A hedged "roughly 25" in prose became an exact integer in a structured field. No score impact. |
| 35 | B12c | 07-emoat block, catalysts_12m entry 4; rule E-33 | Window exceeds the field scope and contradicts Section 6A. Claimed a 12 to 24 month window inside catalysts_12m. Recomputed as 0 to 12 months for the CWIP appearance, or move the commissioning test out of the field. Pillar 3 scores catalyst proximity, so a 12 to 24 month item inside a 12 month field overstates proximity. |
| 36 | B12c | 07-emoat Section 3 summary and active_categories; rule E-35 | Time to materialise contradicts the stated evidence. Claimed A4 "HV e-bus packs 12-24m". Recomputed as "ongoing (RESS live now; HV e-bus packs NOT FOUND)". Section 1A records the same product's expected launch as NOT FOUND, and NOT FOUND is the only valid fill for a missing date. No score impact. |
| 37 | B12d | 06-peers Claim 4, RAJOOENG Q2 FY24 back to back procurement quote | Cited p.9. The quote is real and accurately transcribed but sits on PDF page 10. |
| 38 | B12d | 06-peers Claim 3 / Part 2D, RAJOOENG Q4 FY24 "Windsor machines and carbon extrusion" quote | Cited p.8. The quote is real and accurately transcribed but sits on PDF page 9. |
| 39 | B12d | 06-peers Claim 5, RAJOOENG Q4 FY24 45 percent FY24 export share | Cited p.11. The figure is real but sits on PDF page 12. |
| 40 | B12d | 06-peers Claim 3, RAJOOENG Q2 FY25 33 percent PVC and 55 to 60 percent blown films market share quotes | Cited p.9-10. The quotes are real and accurately transcribed but sit on PDF pages 11 and 12 respectively. |
| 41 | B12d | 06-peers Claim 1 net read, RAJOOENG Q2 FY25 "domestic is not really encouraging margin" and 73 percent export quote | Cited p.11. The quote is real but sits on PDF page 12. |
| 42 | B12d | 06-peers Claim 8, HBLENGINE p.17 nickel cadmium quote | Claimed "everybody can import cells". The transcript literally reads "everybody can import sales". Substance intact, wording not verbatim. |
| 43 | B12d | 06-peers Part 4 Triangulation Summary, CONTRADICTED verdict labels | The label alone, read outside its caveat, risks reading stronger than the framing only scope the report consistently states. Presentational note, not a discipline failure. |

---

## INFO (1)

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| 44 | B12c | scope | Phase 1 scope note, not a defect. Valuation adherence (B10 and B11) and the Business Understanding Narrative (stage 13) are pending phase 3. Neither artifact exists yet, so no rule was failed against them. Both must be audited in the phase 3 pass. |

---

## Counts

| Verifier | CRITICAL | MAJOR | MINOR | Acceptance |
|---|---|---|---|---|
| B12a numerical | 0 | 0 | 3 | 93.3 |
| B12b red flags | 1 | 12 | 13 | 23.0 |
| B12c framework (Gate 0 and Emerging Moat only) | 0 | 0 | 6 | 93.8 |
| B12d peers | 0 | 1 | 7 | 83.0 |
| **Total** | **1** | **13** | **29** | overall 23.0 |

Other verifier positions recorded without a severity row: B12b concurs with credibility grade D and states its independent read finds more against management than stage 5 did, not less. B12b logged no pipeline flags as unsupported. B12b spot checked 5 promise delivery rows and confirmed 5. B12d found all claims addressed and no verdict discipline failures.

Verifier disagreement log: none this run (B12a carries no source_fidelity finding)
