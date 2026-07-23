# FTTCP v1.2 Handoff Dossier: Aye Finance Limited (AYE)

Machine anchored audit trail for a separate FTTCP deliberation session that will NOT hold the source PDFs. Every figure carries its (source, page/note). Block references (B04 etc.) are expected here. Run date 2026-07-22. Model claude-opus-4-8.

## Run identity and deliberation confirmed inputs

- Company: Aye Finance Limited (formerly Aye Finance Private Limited). MSME and micro enterprise NBFC-ML balance sheet lender (secured plus unsecured business loans) (B00; B04 business_type lending).
- Listed BSE 544699 / NSE AYE, about Feb-2026; recently listed under 3 years, so the 614 page IPO Prospectus is the foundational filing (misfiled in annual-report/1770879625663.pdf) (B00 doc_routing).
- No identifiable promoter: Prospectus "OUR COMPANY DOES NOT HAVE AN IDENTIFIABLE PROMOTER", PE and VC backed (B00 line 10; B08).
- CMP Rs 183.22 (NSE, 2026-07-22, cmp_note.md line 7). Market cap about Rs 4,614 Cr (cmp_note.md line 8). Shares about 25.2 Cr (cmp_note.md line 9). 52 week range Rs 88.22 low to Rs 197.29 high; Rs 88.22 is the since listing low (cmp_note.md lines 12-13). Record high Rs 197.29 hit 2026-07-21.
- Deliberation confirmed overrides and settings (fttcp-deliberation.md, authoritative for Phase 3):
  - Approved DESTINATION (exit) PE base 15.0x by FY29, within the 18x cap and the pillar derived additive band (lines 27-29, 56).
  - Approved EARNINGS BASIS FORWARD (one year forward P/E on forward EPS), horizon FY29, operator reason "since the growth is strong" (lines 33-35, 57).
  - Pillar 2 lender Asset Quality Multiplier 1.00x (Sound), operator approved via the 15x, overriding the drafted 0.80x (lines 29, 51).
  - Sector cap 18x, Banks / NBFCs / MFIs, absolute; corrected from the manifest's Pharma/CDMO (lines 12, 55).
  - Pillar 1 normalization Route A governs, Route B suppressed per single credit rule (lines 18, 50).
  - Route A (post IPO excess capital denominator fix) governs the ROE normalization (line 50).
  - Tier A, hurdle 25% (lines 21, 58).
  - Undiscovered Alpha NOT applied (FII+DII about 35%, far above the 3% institutional absence test) (line 54).
  - Composite +4 out of 8, DEEP WATCH leaning BUY-ON-DIPS, not contested by the operator (line 19).
  - Cash determination STRUCTURAL for the lender CFO signal, with a residual INDETERMINATE element on earnings quality (gain on derecognition rising to 3.65% of income); keeps the Phase 1 gate at PROCEED WITH CAVEATS (line 17).
  - Cross family FTTCP grader did NOT run (no Gemini/GPT key); FTTCP confidence treated one notch lower, on top of the single collected concall reduction (line 43).
- Roles: Role 1 valuation = B11; Role 1 inputs assembly = B10; Role 2 thesis = B14; Role 3 devil's advocate = B15. First workup; Role 1 derived fields N/A (deliberation line 11).

## 1. Transition data series (lender variant)

Manufacturing rows that do not apply to a balance sheet lender are marked NOT APPLICABLE; unfilled anchored cells are NOT FOUND, never estimated.

### 1a. Topline

| FY | Total income / revenue (Rs Cr) | Growth | Anchor |
|---|---|---|---|
| FY23 | NOT FOUND (total income not separately anchored in the restated window) | NOT FOUND | restated PAT anchored, revenue line not isolated (B02 Annexure VI p.404/614) |
| FY24 | 1,325.96 (Prospectus restated) | NOT FOUND (FY23 base NOT FOUND) | B10 line 69 (Prospectus restated) |
| FY25 | 1,504.99 (total income) | +13.5% over FY24 (computed) | B04 line 54 (Results/AR); gain on derecognition Rs 37.59 Cr = 2.50% of Rs 1,504.99 Cr |
| FY26 | 1,814.73 revenue from ops / 1,863.24 total income | +20.6% ops / +23.8% total income over FY25 (computed) | B10 (results__edbf1e94 p.6 line 378); B04 line 76 (total income) |
| Q1FY27 | NOT FOUND (full P&L OCR garbled) | NOT FOUND | only Annexure-1 ratio block reconstructable (B01 line 48) |

3 year revenue CAGR FY24 to FY26 = 16.9% (B10 line 69). Interest income on loans = 83.6% of FY26 total income (Rs 1,557.43 Cr, Results FY26 p.6, B04 line 34).

### 1b. Margin

| FY | Gross margin | EBITDA margin | Net (PAT) margin | Anchor |
|---|---|---|---|---|
| FY23 | NOT APPLICABLE (lender; NIM/spread is the analog) | NOT APPLICABLE | NOT FOUND (total income NOT FOUND) | B04 3A |
| FY24 | NOT APPLICABLE | NOT APPLICABLE | 12.95% (171.68 / 1,325.96, computed) | PAT B02 line 53, revenue B10 line 69 |
| FY25 | NOT APPLICABLE | NOT APPLICABLE | 11.65% (175.25 / 1,504.99, computed) | PAT B02 line 54, revenue B04 line 54 |
| FY26 | NOT APPLICABLE | NOT APPLICABLE | 11.39% (Reg 52(4) net profit margin) | results__edbf1e94 Annexure 1 p.11 line 852 (B10) |
| Q1FY27 | NOT APPLICABLE | NOT APPLICABLE | 15.22% (Reg 52(4)) | B01 line 48 |

Lender margin analog (NIM on ATA): FY26 actual 14.38% (Inv. Pres. slide 37, B04 line 220); FY27 guidance 14.25 to 14.75% (Inv. Pres. slide 32, B05 line 46 digest cross check). Average yield 21.95 to 22.95% on ATA; incremental cost of borrowing 10.20 to 10.78% Q1FY27, down from 11.80% FY23 (Inv. Pres. slide 8, 18-19, B04).

### 1c. Cash conversion

| FY | OCF (Rs Cr) | OCF/EBITDA | CFO/PAT | Debtor days | WC % of sales | Anchor |
|---|---|---|---|---|---|---|
| FY23 | -720.39 (-7,203.90mn) | NOT APPLICABLE | -18.1x | NOT APPLICABLE (lender) | NOT APPLICABLE | B03 line 19; B01 line 49 |
| FY24 | NOT FOUND | NOT APPLICABLE | NOT FOUND (interim -4.6x band from FY25) | NOT APPLICABLE | NOT APPLICABLE | B01 line 49 |
| FY25 | NOT FOUND | NOT APPLICABLE | -4.6x to -4.7x | NOT APPLICABLE | NOT APPLICABLE | B01 line 49 |
| H1FY26 | -454.88 (-4,548.76mn) | NOT APPLICABLE | NOT FOUND | NOT APPLICABLE | NOT APPLICABLE | B03 line 19 |
| FY26 | -1,354.64 | NOT APPLICABLE | -7.0x latest; -7.25x cumulative 4yr | NOT APPLICABLE | NOT APPLICABLE | B10 (results__edbf1e94 p.8 line 584); B01 line 36 |

CFO is structurally negative every year: loan disbursements are an operating outflow under Ind AS 7 for a growing balance sheet lender; not an earnings quality or going concern signal (B01 line 42, B03 line 19). Block B trend deteriorating on ratio but growth scale driven (B01 line 49).

Rating agency working capital / liquidity commentary, VERBATIM (ICRA, rating__138929 p.2-3 lines 100-105, via B10 wc_commentary_verbatim): "Liquidity position: Adequate. The company's liquidity profile is adequate with unencumbered on-book liquidity of Rs. 1,078 crore as on June 30, 2025. This, along with the scheduled collections of Rs. 2,360 crore till June 30, 2026, is sufficient to meet the scheduled debt obligations of Rs. 2,108 crore during this period in a timely manner. The presence of Rs. 704 crore of sanctioned unutilised funding lines, as on June 30, 2025, also supports the liquidity profile. As per Aye Finance's asset-liability management (ALM) statement as on June 30, 2025, there were no cumulative mismatches across buckets."

### 1d. ROCE and ROE

| FY | ROCE | ROE | ROA | Capital employed basis | Anchor |
|---|---|---|---|---|---|
| FY24 | NOT APPLICABLE (lender; ROE/ROA used) | 17.28% | 3.7% (rating) / 4.29% (DuPont) | ROE on net worth; DuPont verified | B03 line 24; rating__138929 p.1 (B10 line 74) |
| FY25 | NOT APPLICABLE | NOT FOUND (exact) | 2.8% | ROE on net worth | rating__138929 p.1 (B10 line 75) |
| H1FY26 | NOT APPLICABLE | 7.63% annualized | 1.92% annualized | closing net worth basis | B03 line 24 (B10 line 73) |
| FY26 | NOT APPLICABLE | 9.26% (post IPO dilution) | 3.08% on AUM basis | post infusion net worth | Inv. Pres. slide 37 (B04 line 224) |
| Q1FY27 | NOT APPLICABLE | about 16.0% (post infusion basis) | 3.71% on assets | post infusion net worth | Inv. Pres. slide 8 (B04 line 295) |

ROCE NOT APPLICABLE and NOT FOUND for a balance sheet lender (B10 lines 77-78). Pillar 1 operational ROE anchor for valuation = 11.7 to 13% after Route A strips post IPO excess capital (fttcp-deliberation.md line 50). Credit cost ratio: 2.70% FY23, 5.15% FY25, 5.14% H1FY26 annualized, guided down to 3.5 to 4.0% FY27 (B03 line 15; B05 line 42).

## 2. Catalyst inventory

From B05.triggers (7) and B07.catalysts_12m (5). Tier: documented / claim / inference.

B05 triggers:
1. Credit cost normalisation toward 3.25 to 3.75% comfort range. Tier documented (anchored ratios). Window near-medium. Conviction M. Confirm: anchored Gross/Net Stage III keep improving (already 4.77% to 4.49% GNPA). Kill: GNPA/NNPA reverses upward in next anchored filing. (B05)
2. AUM growth reacceleration toward 29 to 30%+ (missed in FY26). Tier documented. Window near-medium. Conviction L-M. Confirm: on book loan growth closes toward or exceeds 29 to 30% YoY. Kill: growth stays materially below guidance a second consecutive period. (B05)
3. Mortgage mix build toward about 30% of portfolio. Tier documented. Window medium (3yr). Conviction M. Confirm: mortgage mix visibly increases beyond the flat 22 to 23%. Kill: flat or declining for multiple quarters despite continued headcount investment. (B05)
4. Hypothecation approval rate normalisation (40 to 43% back toward 55%). Tier documented. Window near-medium (FY27). Conviction M. Confirm: loan growth reaccelerates specifically in the hypothecation book. Kill: approval rates stay suppressed, growth stays mortgage dependent only. (B05)
5. Operating leverage from mortgage team cost absorption. Tier documented. Window medium. Conviction M. Confirm: opex ratio trends toward the 7 to 7.5% target once disclosed. Kill: opex ratio stays elevated as mortgage AUM lags headcount. (B05)
6. Post IPO capital base and funding cost decline supporting NIM/RoA. Tier documented. Window near-medium. Conviction M-H. Confirm: PAT/EPS continues the Q3 to Q4 FY26 step up. Kill: finance cost fails to decline despite lower incremental CoB and higher net worth. (B05)
7. Bihar / MFI bill regulatory containment. Tier claim (geography split digest only). Window near. Conviction M. Confirm: aggregate anchored asset quality keeps improving despite 15.5% Bihar AUM concentration. Kill: a visible break in the GNPA/collection trend coincident with Bihar news flow. (B05)

B07 12 month catalysts:
8. Generative AI underwriting pilot quantified disclosure. Tier claim (operator digest, NON-ANCHORED). Window 6 to 18m. Confirm: quantified pilot results (% of underwriting volume, approval/turnaround impact) in a filed concall or deck. Kill: no disclosure or negligible volumes. (B07)
9. Mortgage/LAP mix crossing about 25% en route to 30 to 35% target. Tier documented. Window 12m. Confirm/Kill as trigger 3 above. Anchor Inv. Pres. slide 14/31/32; Prospectus p.237. (B07)
10. FY27 delivery vs guided NIM 14.25 to 14.75% / RoA 4.0 to 4.5% / credit cost 3.5 to 4.0% / opex 8.25 to 8.75%. Tier documented. Window 12m. Primary 12m catalyst. Anchor Inv. Pres. slide 31. (B07)
11. Further rating action / cost of borrowing trajectory below 10.78%. Tier documented. Window 6 to 12m. Anchor Inv. Pres. slide 18; digest only for the Jun-2026 India Ratings A+ upgrade. (B07)
12. Bihar MFI ordinance resolution and read through to the about 17% of AUM Bihar book. Tier claim. Window 6 to 12m. Anchor Q3 FY26 call p.9-10. (B07)

## 3. Flags with complete underlying findings

FLAG-PROMOTER: NOT ACTIVE. B08 verdict TRUSTWORTHY; scorecard clean 8, caution 2, red 0. Deal breaker recorded not enforced: 3 independent directors resigned same day 2023-09-02, disclosed RBI conflict reason, one re appointed Aug-2024 (Prospectus p.289). Adverse findings (all VERIFIED unless noted): RBI FY23 inspection observations remediated by 2024-09-19 (Risk Factor 16 p.51-52); RBI late submission fee Rs 17.5 lakh 2019 (p.52); CFO seat changed twice in about 4 months around listing, Krishan Gopal resigned Jan-2026, interim Sovan Satyaprakash, permanent Gaurav Seth 2026-04-28 (MEDIA REPORTED, operator digest plus exchange filings); pending tax proceedings 5 matters Rs 158.83mn (p.32, Note 33); BSE fine Rs 1,48,680 for delayed Dec-2025 debt segment results (MEDIA REPORTED); immaterial RPT relative of MD about 0.01% of income (p.27). Transition evidence list: external professional CFO Gaurav Seth (ex IIFL Home Finance, ex Airtel Payments Bank); all institutional nominee director rights terminated on listing (Prospectus p.303); 2023-24 governance overhaul with ex NABARD chair, ex RBI CGM, ex MD PNB Housing, ex GM SBI on the board; auditor upgrade to MSKA & Associates LLP (BDO network); India Ratings IND A to IND A+ (Stable) 2026-06-24; fresh primary capital Rs 710 Cr at the IPO, CRAR to 42.2% from 31.45% pre IPO (digest only). Pledge NOT APPLICABLE (no promoter). (B08)

FLAG-CASH: determination STRUCTURAL with residual INDETERMINATE earnings quality element. CFO negative every year by design (FY23 -Rs 720.39 Cr through FY26 -Rs 1,354.64 Cr, Ind AS 7); not a going concern signal (B01, B03, B10). INDETERMINATE element: net gain on derecognition (securitisation / direct assignment), a day one non cash upfront gain, rising 1.94% (FY23) to 2.50% (FY25) to 3.65% (FY26) of total income / 5.8% of revenue FY26 (Rs 67.97 Cr, Results FY26 p.6, B04 line 54). Add net gain on fair value changes 5.68% of FY26 total income (Rs 105.79 Cr, market driven) so about 9.3% of FY26 income is outside recurring spread (B04). Rating agency verbatim liquidity quote reproduced in section 1c (ICRA p.2-3 lines 100-105). Capex commissioning timeline NOT APPLICABLE for a lender (capex Rs 11.66 Cr FY26, immaterial, results p.8 line 586). Receivables composition NOT APPLICABLE (no trade receivables); loan book Rs 6,266 Cr = 80.6% of total assets (Results FY26 p.5). Missing evidence to clear: normalized PAT ex derecognition by product line (B10 unresolved), FY27 audited PAT. Determination caps the gate at PROCEED WITH CAVEATS (CLAUDE.md NEVER rule).

FLAG-GATE0: Gate 0 grand total 59, core 52, moat 7, moats confirmed 1, classification AVOID, THIN moat, 4 data years FY23 to FY26 (B01). Depressor detail: classification AVOID is driven by NBFC metric scale mismatch under manufacturing calibrated bands (Block B cash generation scored 0 because CFO is structurally negative for a lender; Block A ROCE to ROA substitution scores near zero for any NBFC) plus the LIMITED history one tier downgrade (4 FY periods, IPO Feb-2026), not by demonstrated fundamental deterioration. Deal breakers: (1) Block A 5 < 8 cap GOOD non binding; (2) Block B 0 < 8 cap GOOD non binding; (3) median ROA 2.94% < 10% ROCE substitute cap AVERAGE binding but non differentiating (median ROE 10.68% would not trigger); (4) cumulative CFO/PAT -7.25x < 0.50 cap AVERAGE binding, tied to Block B INDETERMINATE. Counter signals: ICRA anchored CRAR 42%, historical ROE 16.1% FY24, 25% AUM CAGR (rating p.1). Flagged for human synthesis, not a stop. (B01)

FLAG-ASSET-QUALITY: Gross Stage III (GNPA) 3.2% (Mar-24), 4.2% (Mar-25), 4.6% (Jun-25), 4.85% (Sep-25 peak), 4.77% (Mar-26 audited), 4.49% (Jun-26 latest). Net Stage III 1.67% Q1FY27; PCR 63.80% Q1FY27. Notes level detail: Stage 3 rising 4 consecutive periods 2.49% to 4.85% (Note 53.13.4 p.385/614); Stage 2 ECL on core book roughly tripled FY23 to FY24 13.90% to 40.73% unexplained (Note 49.1.8(c) p.369/614); write offs quadrupled Rs 500.00mn to Rs 2,034.89mn FY23 to FY25 (Note 28 p.347/614); restructured book +66% within H1FY26 (Note 46.1). Transition forward STARTING (+1). (B01, B02, B10)

FLAG-EARNINGS-QUALITY: RoE 17.28% (FY24) to 7.63% (H1FY26 annualized); RoA 4.29% to 1.92%; PBT margin 20.10% to 9.57% (H1FY25 to H1FY26); credit cost 2.70% (FY23) to 5.15% (FY25), not yet peaking through H1FY26. DuPont verified: fall is profitability driven, leverage flat about 3.7x to 4.0x. Credit cycle reached realised earnings, not just provisioning notes. (B03, B10)

FLAG-DATA: recurring tax expense restatement across 4 of 5 presented periods. FY23 PAT down 25.9% (Rs 537.96mn to Rs 398.73mn); FY24 up 6.5% (Rs 1,611.27mn to Rs 1,716.79mn); FY25 up 2.3% (Rs 1,712.72mn to Rs 1,752.52mn); H1FY26 down 0.8%. Equity restated down at FY23 (-Rs 140.11mn) and April-01-2022 opening. (B01, B02 Annexure VI p.404/614)

FLAG-DISCLOSURE-GAP: covenant breach severity (23 instances / Rs 12,344.12mn = 23.6% of total borrowings, majority unwaived at Sep-25, Note 53.36 p.401-402/614) materially understated in Risk Factor 9 (p.45-47/614), described only as "certain instances of delay... on account of technical issues" with no count, amount or waiver status. Tax restatement pattern has no dedicated risk factor. Front matter claim "expertise... has enabled us to maintain stable credit costs" (p.219/614) contradicted by credit cost roughly doubling. (B03)

Carried verifier flags: verifier B MAJOR over lending / per borrower leverage (39% repeat loans + 60% branch deepening, transcript p.7, B12b); verifier C MAJOR SOM cross check optimism (B11 s4, B12c). Both detailed in section 5 peer/valuation and in verifier-summary.md.

## 4. Credibility grade

Grade C (Mixed). promise_delivery_score: delivered 3, partial 3, missed 1 (B05). repeated_evasions: [] (none logged). excuse_pattern balanced. Single collected AYE transcript (Q3 FY26 maiden call, 06-Mar-2026), so the standard three call methodology was substituted with a two point promise vs anchored delivery test; Q4 FY26 and Q1 FY27 calls not collected (digest only). Basis: the most repeated, most confident guidance (29 to 30% AUM growth for FY26) missed on the anchored proxy (26.6% YoY on book loan growth); credit cost delivery ambiguous on a metric basis mismatch; set against genuine anchored delivery on asset quality ratios and PAT.

Guidance vs delivery table (promise, delivered, quarter anchors):
- AUM growth 29 to 30% FY26 (promised Q3 FY26 call 06-Mar-2026) -> MISSED, on book loans grew 26.6% YoY (FY26 audited BS, filed 27-Apr-2026); digest AUM +26 to 27%. (B05)
- Credit cost <4% annualised exiting Q4 FY26 (Q3 FY26 call) -> PARTIAL/ambiguous, not in anchored filings; digest Q4FY26 credit cost 4.30% on ATA basis (denominator mismatch vs management's AUM basis). (B05)
- Exit FY26 with a fairly normalised credit book (Q3 FY26 call) -> DELIVERED, Gross Stage III 4.77% / Net 1.79% / PCR 63.66% at 31-Mar-2026, improving to 4.49% / 1.67% / 63.80% at 30-Jun-2026. (B05)
- Robust improvement in profits from Q4 FY26 (Q3 FY26 call) -> DELIVERED, PAT Rs 42.60 Cr (Q3FY26) to Rs 85.91 Cr (Q4FY26, +102% QoQ); FY26 PAT Rs 193.63 Cr. (B05)
- Mortgage mix toward about 30% (3yr target from 22%) -> PARTIAL/too early, digest mix about 23% (FY26 end) to about 21.8% (30-Jun-2026), essentially flat. (B05)
- FY27 NIM guidance to be given next call (timing promise) -> PARTIAL/not independently verifiable; digest reports 14.25 to 14.75% given at the uncollected Q4FY26 call. (B05)
- Bihar/MFI bill exposure immaterial to collections (Q3 FY26 call) -> DELIVERED directionally, digest "minimal impact"; anchored aggregate asset quality kept improving. (B05)

Guidance items with numbers (B05.guidance): AUM growth 29 to 30% FY26; AUM CAGR about 30% 3yr; credit cost exit <4% Q4FY26; credit cost comfort 3.25 to 3.75% 3yr; opex ratio 7 to 7.5% 3yr; RoA 4 to 4.5% 3yr; mortgage mix about 30% (from 22%); FY27 NIM deferred. Verifier B concurs grade C (B12b).

## 5. Scorecards and market sizing

Gate 0 (B01): grand 59/160; core_score 52/100; moat_score 7/60; Blocks A 5, B 0, C 20, D 16, E 11; moats_confirmed 1/12; classification AVOID (one tier LIMITED history downgrade from core implied AVERAGE); deal breakers as listed in FLAG-GATE0 above.

Emerging Moat (B07): em_score 19.6/80; em_classification MODEST (below 25 premium threshold); combined_assessment AVERAGE. active_categories with evidence: D1 proprietary data asset (cluster + AI/ML underwriting) Strong / documented; G1 war chest / funding access Strong / documented; C1 customer ecosystem / repeat loan stickiness Moderate / documented; A3 process innovation (cost to income, productivity) Moderate / documented. evidence_mix documented 20, claim 4, inference 2. capex_embedded_growth_pct 84.

Accounting quality (B02): accounting_quality 5.5/10. Top notes findings with note_ref and rating:
1. Covenant breaches 23.6% of borrowings (Rs 12,344.12mn of Rs 52,184.98mn) Sep-25, 9 of 23 waived (Note 53.36 p.401-402) RED.
2. Recurring tax restatement, FY23 PAT cut 25.9%, 4 of 5 periods (Annexure VI p.404; Note 40(b) p.358) RED.
3. Stage 3/GNPA rising 4 periods 2.49% to 4.85% (Note 53.13.4 p.385) RED.
4. Stage 2 ECL rate on core book tripled 13.90% to 40.73% FY23 to FY24, unexplained (Note 49.1.8(c) p.369) RED.
5. Write offs quadrupled Rs 500.00mn to Rs 2,034.89mn FY23 to FY25 (Note 28 p.347) RED.
6. Restructured book +66% borrowers within H1FY26 (401 to 665) (Note 46/46.1 p.361-364) RED.
7. CRAR fell 37.61% (Sep-24) to 32.27% (Sep-25); Tier I flat despite profit (Note 48 p.365) YELLOW, mitigated by IPO (pro forma post offer CRAR 47.48%).
8. Rs 290.51mn ARC security receipt impairment (12.9% of FY25 PBT) not a distinct P&L line (Note 6 p.329; Annexure III p.315; Note 28; Note 30) RED.
9. NPA to ARC sales reconciled: FY25 Rs 2,593.70mn transfer 100% already written off; only FY23 Rs 321.10mn fits original GNPA understatement concern (Note 53.27.1(d)(i) p.393-394) YELLOW.
10. Ind AS 109 ECL exceeds RBI IRACP floor by Rs 1,678.02mn (Sep-25), 3.4x floor, grown about 5x since FY23 (Note 52 p.382-384) GREEN.
11. Credit rating improving: IndRa A/Stable (Jul-2024), ICRA reaffirmed A/Stable expanded limits (Nov-2025) (Note 53.11.4 p.390) GREEN.
12. Customer and Ombudsman complaints rising faster than book in places (FY24 +113% vs about 58% AUM growth) (Note 53.16/53.16.1 p.386-390) YELLOW.
13. Auditor identified ITGC gap: audit trail not enabled part of FY24, remediated from 19-Sep-2024, no tampering (Examination Report p.311-312) YELLOW.
14. Unsecured loan mix rose 31.3% (FY23) to 41.0% (Sep-25) of gross loans (Note 5 p.328) YELLOW.
15. Gain on derecognition income grew Rs 125.10mn (FY23) to Rs 375.93mn (FY25), front loaded and growing share of profit (Note 25/53.27 p.346, 393-394) YELLOW.
going_concern_language: NONE (standard boilerplate only, no material uncertainty paragraph). B03 overall_quality 5.6; components governance 6.5, accounting 5.5, balance_sheet 6.0, earnings 4.5; phase verdicts p1 Clean, p2 Watch, p3 Red Flag, p4 Watch, p5 Watch, p6 Watch, best fit GARP (Watchlist).

Market sizing (B09): tam_cr conservative 4,08,000 / realistic 9,12,000; sam_cr 1,20,400 (29.5% of TAM); som_3yr_cr 12,140; som_5yr_cr 14,540; runway_class STRONG; som_implied_revenue_cagr yr3 18.3% / yr5 14.7%; current_sam_share_pct 6.1; revenue_headroom_x 66.3; tam_growth_pct 19; mgmt_claim_cr 34,00,000; mgmt_claim_ratio 8.3 (read inflated). Capacity: sufficient at 3yr (Rs 1,336 Cr headroom); 5yr SOM Rs 14,540 Cr exceeds B07's static 84% headroom ceiling Rs 13,476 Cr by Rs 1,064 Cr absent net worth accretion or a raise. Four TAM flags: company commissioned CRISIL source; method divergence; SAM customer filter unsourced (70% estimate); capacity 5yr gap.

Peer triangulation (B06): 11 peers, 10 substantive plus rated fair.
- Verified: peer rated NBFC-MSME lenders show comparable incremental cost of borrowing declines (MASFIN, NORTHARC, SBFC; 6 anchors).
- Partially verified: sector wide credit cost normalisation; sector wide over lending tightening with FY27 approval reversal; collection efficiency recovery specific to business loan segments; independent MSME/hypothecation TAM benchmark.
- Contradicted: (a) "minimal spillover from a state MFI ordinance into non MFI business loan books" (Bihar parallel), by SBFC Jul-2025, Aseem Dhru, p.7, "the ordinance, which had nothing to do with us, brought our collection numbers down sharply... it is not about geography so much... it is more about ticket sizes"; (b) "sub 2% mortgage/micro LAP credit cost aspiration supported by peer seasoning", by SBFC Nov-2025, Mahesh Dayani, p.9, sub Rs 7 lakh secured MSME carries "enhanced credit cost" and SARFAESI timelines "almost twice" the book average.
- Unverifiable: about 67 million unorganized micro enterprise TAM figure; near no alternate supplier hypothecation claim; Bihar ordinance spillover tested directly. net_narrative_effect complicates. Risks peers raise: political/ordinance risk as structural recurring (SBFC Nov-2025 p.3); borrower level multi lender over leverage invisible to bureau checks (SBFC Jul-2025 p.9-10); household debt outpacing financial assets (SBFC Jan-2026 p.6); sub Rs 10 lakh MSME NPAs deteriorating 70bp (SBFC Jul-2025 p.9); HFC vs NBFC SARFAESI access gap (SBFC Nov-2025 p.11).

## 6. Valuation pillar detail (stage 11 ran; B11)

Framework versions Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2. pe_basis forward. exit_pe_base_approved 15.0x. Tier A, hurdle 25%, divisor 1.953.

Primary method (lender): theoretical P/B = ROE / CoE. CoE 14.5% (analyst input: rf about 6.7% + beta about 1.15 x ERP about 6.5%). Static P/B on approved ROE anchor 11.7 to 13% against BVPS Rs 100.32 (Q1FY27): fair P/B 0.81 to 0.90x, fair value Rs 81 to 90 (mid Rs 86), versus current 1.83x. Growth adjusted Gordon: on suppressed anchor (ROE 13%, g 8%) 0.77x; on recovered ROE 16%, g 10% only 1.33x, still below current. Primary read: fully to richly valued at CMP.

Destination PE dual track (secondary cross check):
- track1_rrm (Track 1): low 9.6x, mid 10.4x, high 11.2x; r_used 15.5%, rrm 0.76. RRM = 1 + (13.5 - r) x 0.12, bounded 0.70 to 1.60. Fundamental base PE 13.7x x RRM. Divergence about 31% below the approved 15x; on RRM AVOID on valuation at CMP.
- track2_additive (Track 2, governing via operator approval): low 15.4x, mid 15.7x, high 16.0x. Build: Pillar 1 ROE base PE = 0.5 x ROE + 7.5 = 13.4x (ROE 11.7%) to 14.0x (ROE 13.0%), mid 13.7x (ROE 12.35%); Pillar 2 Asset Quality Multiplier x 1.00x (Sound); Pillar 3 +2x (3a growth +2 on about 26% AUM machinery capped at +2 by grade C; 3b moat +0, EM 19.6 MODEST; 3c duration +0); Strategic +0 (barred single credit); UA not applied; sector cap 18x not binding. Additive floor 15.4x; operator approved 15.0x sits at/just below it (conservative).
- divergence_pct 31. governing_track operator approved 15x (additive consistent), RRM shown for transparency, does not override.

pillar_detail: roce_used 12.35 (ROE mid), roce_base 7.63 (H1FY26 annualized statutory), roce_recovery_route pillar1-midpoint, pillar1_normalization_route A-governs-B-suppressed, cash_multiplier 1.00, growth_offset 0, growth_premium 2, strategic_premium 0, shared_catalyst_flag true, ua_applied false, sector_cap_used 18, structural_or_growth lender AQ multiplier 1.00x (Sound); FTTCP cash STRUCTURAL with residual INDETERMINATE earnings quality.

Forward EPS (LABELLED PROJECTION, not an anchor): FY26 PAT Rs 193.63 Cr / EPS Rs 9.73 (results__edbf1e94 p.6); Q1FY27 PAT Rs 74.5 Cr annualized about Rs 300 Cr, FY27E EPS about Rs 11.90 (Rs 300 Cr / 25.2 Cr). Stress note: if Q1 was a peak, FY27 could land Rs 270 to 290 Cr. Scenario 3yr EPS CAGR: bear 15%, base 22%, bull 28%.

hurdle_ratio: base 1.77 (FAIL vs 1.953), bull_used true (grade C capped at base+5% = 27%, HR 2.00 PASS), verdict CONDITIONAL. Current forward PE (FY27E) 15.4x; de rating term 15/15.4 = 0.975.

fair_values: track1 (RRM 10.4x) bear 188 / base 225 / bull 260; track2 (approved 15x) bear 272 / base 324 / bull 375. entry_range low 133 / high 166 (base 324 / 1.953 = 166). mos_price 133 (20% below entry). expected_cagr_prob_weighted 19.7% (weights 35/45/20: price CAGR bear 14.1%, base 20.9%, bull 27.0%). upside_downside_ratio 1.45. Reward = base 324 - CMP 183.22 = +Rs 141 (+76.8% over 3yr); risk = CMP - static P/B floor about Rs 86 = -Rs 97 (-53%). decision WATCHLIST (BUY-ON-DIPS), on valuation, accumulate Rs 133 to 166, not a buy at CMP (base hurdle fails, prob weighted CAGR 19.7% < 25%). som_cagr_crosscheck recorded "consistent" (this is the verifier C MAJOR: base about 25% AUM exceeds the 18.3% SOM ceiling). One line thesis: recovering micro enterprise NBFC priced at fair value on the approved 15x forward; 25% returns need >26% forward EPS CAGR a grade C record and rising derecognition gains have not yet earned; watch, buy below Rs 166. Position size Small (B14). Devil's advocate (B15): WEAKENED BUT ALIVE, all four dimensions weakened; sharpest counter is the entry rests on the most generous of three lenses while P/B (Rs 81-90) and RRM (entry Rs 115) point to Rs 86 to 115.

## 7. Gaps ledger

| Item | Stage/block needing it | Where to obtain |
|---|---|---|
| Forward EPS / FY27 audited PAT | B10 unresolved, B11 forward hurdle | Next FY27 results filing (BSE/NSE); Q4FY26 concall transcript if collected |
| Normalized PAT ex derecognition by product line | B10 unresolved, FLAG-CASH clearance | Full FY26 P&L notes (Note 25 / Note 53.27, Prospectus p.346, 393-394) |
| Peer P/E, P/B, ROCE/RoA medians | B10, B11 secondary cross check | Independent calculation from the peer screening CSVs at /inputs/screening/ |
| Q1FY27 full P&L / balance sheet line items | B01, B05 (OCR garbled extract) | First post listing Annual Report; Q2FY27 results filing |
| Dividend per share | B10 | First AGM (about Sep-2026) |
| NIM / spread / AUM / credit cost % of AUM anchored | B01, B05 (digest only currently) | FY27 results filings and investor presentations (anchored) |
| Q4 FY26 and Q1 FY27 concall transcripts | B05, B07 (single maiden call only) | Company IR / exchange filed concall transcripts |
| Bihar geography level asset quality split | B05, B06 | Investor presentation state level AUM/asset quality slides |
| Peer benchmark for the about 67 million TAM and no alternate supplier claim | B06, B09 (unverifiable) | Independent industry data (SIDBI/CRISIL non commissioned), peer disclosures |
| Full CFO/PAT history >4 years | B10 | First post listing Annual Report (may include 5 year history) |
| Q4FY26 Interest income reconciliation (Rs 440.16 Cr vs Rs 426.80 Cr) | B05, B10 conflicts | Management clarification / next filing footnotes |
| ITGC remediation confirmation, covenant waiver status of the 14 unwaived instances | B02, B03 | First post listing quarterly/annual filing, borrowings/covenant note |
| Cross family FTTCP grade | Deliberation (grader SKIPPED, no Gemini/GPT key) | Re run verifiers/fttcp_crossgrade.py with a provider key configured |

Cross family grader did not run; FTTCP confidence treated one notch lower per protocol (deliberation line 43). No publish candidate this analysis.
