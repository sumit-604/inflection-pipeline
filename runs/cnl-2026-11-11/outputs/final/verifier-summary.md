# CNL (Creative Newtech Ltd): verifier summary, Phase 1, run 2026-11-11

## Confidence delta

| Component | Value | Verifier | Basis |
|---|---|---|---|
| Numerical acceptance | 99 | A (B12a) | 517 numbers checked; mandatory 180 of 180; 0 CRITICAL; 5 false positives struck |
| Red flag coverage | 92.3 | B (B12b) | material caught 12 of 13 (caught plus partially caught); strict full catch 61.5% |
| Framework adherence, Phase 1 | 86.0 | C (B12c) | 37 of 43 rules (Gate 0 19 of 22; emerging moat 18 of 21); valuation half pending Phase 3 |
| Peer utilisation | 100 | D (B12d) | substantive confirmed 12 of 12 peers audited |
| Overall | 86.0 | | set by framework adherence; band 75 to 89 normal, note specifics |

Rework: false. Basis: no CONFIRMED Verifier A CRITICAL; no acceptance rate below 60% on a denominator of 4 or more (OR-29).

Acceptance rates: A 99 | B 92.3 | C 86.0 (Phase 1 scope) | D 100.

Severity counts: CRITICAL 0 | MAJOR 3 (B 1, C 2) | MINOR 24 (A 5, B 12, C 4, D 3).

Verifier disagreement log: none. No downstream step relied on or cleared a Verifier A source fidelity row. The one source fidelity row (B07 F1 anchor) is corrected to AR p.41 and confirmed by Verifier A.

Verifier C scope: Gate 0 and emerging moat only. Valuation rules, expectation ledger and business understanding narrative checks are pending Phase 3.

## CRITICAL

None.

## MAJOR

| Verifier | Location anchor | Note |
|---|---|---|
| B | B05 3C finance cost row ("unverifiable"); source Q4 FY26 call p.17 to 18, p.27 (Thakur, to Sonia Keswani and Bharat Aggarwal); Q4 FY26 results p.16 audited consolidated balance sheet | MISSED. CFO debt bridge 83.72 + 171 = 254.72 Cr vs audited current borrowings 324.25 Cr (32,424.88 vs 6,953.06 lakh); bank debt rose 83.72 Cr, not "only increased by INR14 crores"; 69.53 + 83.72 + 171.00 = 324.25 |
| C (C-G1) | Gate 0; framework 01 L27 to 31 fixed ROCE formula, L13 no judgments | ROCE formula substituted (proxy CE = Eq + Res + Borr) vs fixed EBIT/(TA minus CL). Recomputed A 18, core 56, M3 5, moats 4, STRONG, grand 71 (FY25 to FY26 reading) or A 4, core 42, DB1 non binding (strict); filed A 11, core 49, MODERATE. Decision effect none: AVERAGE in all readings (core 40 to 59, DB4 cap); moat_class may read STRONG |
| C (C-E1) | Emerging moat C1; framework 07 L172 to 173 multiplier by tier; verifier rule 3 | C1 scored documented 1.0x on claim only substance (Zicom recurring benefit; the documented item is H1's acquisition action). Recomputed C1 1 x 0.7 = 0.7; em_score 12.5 (stage filed 12.8); MODEST unchanged; margin to 12.0 floor 0.5; C2 regrade then gives 11.6, NONE |

## MINOR

| Verifier | Location anchor | Note |
|---|---|---|
| A (source fidelity: true) | B07 report F1 Talent density, "FY26: no options in operation (AR p.43-44)" | Claim true but the cited page does not contain it. Correct anchor AR p.41 (Directors' Report item iii: "During FY 2025-26, no Employee Stock Option Scheme was in operation and no stock options were granted"). Erratum appended by the orchestrator gives p.41; corrected anchor used downstream |
| A | B01 report section 0 item 2, "Borrowings repaid net 154.85 (p.13)" | Gross vs net label trap. Q2 FY27 results p.13 prints repayment 15,485.04 lakh (154.85 Cr) and separate proceeds +2,458.85 lakh (24.59 Cr); net 130.26 Cr. 154.85 is the gross line. Not a Gate 0 scorecard input; no score changes |
| A | B05 report 2A row 7, 2D, 2B and B05 block input_gaps | FY26 CFO -273.10 Cr (Q4 FY26 results, -27,310.01 lakh) confirmed; but audited AR p.98 prints (27,188.34) lakh = -271.88 Cr and Q2 FY27 deck p.7, p.9 also print 271.88 (deck p.8 prints 273.10). Both exist at their anchors; label each to its source, do not merge. Sign and decision unaffected |
| A | B03 report 3A cash flow table, CON EBITDA incl other income 10,400.13 lakh; 6A row 1 | Basis unlabelled: 10,400.13 uses PBT before associate share (8,181.60, AR p.97); after associate 8,176.20 + 2,066.43 + 152.10 = 10,394.73 lakh (management Rs 103.95 Cr, AR p.7). Difference 5.40 lakh, 0.05%; CFO/EBITDA 2.61x unchanged |
| A | B07 report 1C arithmetic, implied brand CAGR 380.86 to 2,400 over 3 years | 85.5% stated; (2,400/380.86)^(1/3) minus 1 = 84.7%. Already corrected by the erratum appended to the B07 report; body text still reads 85.5%. No block field affected |
| B | B06 Q8; B05 2B, 4D; source Q2 FY27 p.15, p.17 (Patel); REDINGTON Q2 FY27 (Hariharan) | PARTIALLY CAUGHT. Middle East: CNL "almost negligible" vs REDINGTON ME +41%, UAE +39% in Jul to Sep 2026; only in B06 net read, verdict tests a misframed "normalised" claim, no red flag carries it |
| B | B06 Q9, 2A; source Q2 FY27 p.20 (Patel); Q2 FY27 results p.15; REDINGTON Q2 FY27 | PARTIALLY CAUGHT. Diwali explanation graded PARTIALLY VERIFIED despite REDINGTON Q2 +48% (India distribution +67%); CNL market entry revenue +6.7% YoY in Q2 FY27 not quantified; no flag |
| B | B05 4D, 1B, 2E, 4A; source Q2 FY26 p.23; Q4 FY26 p.16, p.27 (Patel) | PARTIALLY CAUGHT. Honeywell renewal is the P1 trigger but only a MEDIUM red flag; slipped split precondition (Q1 2026, then Jul to Aug 2026, then silence) and unreconciled expiry (end 2027 vs March 2027) not noted; B05 anchor p.15 should be p.16 |
| B | B05 3B; B06 Q1; source Q2 FY26 p.6 (Patel); CPPLUS Q3 FY26 (Khemka) | PARTIALLY CAUGHT. Railway coach CCTV "INR24,000 crores plus" (CNL) vs CPPLUS "INR2,000 to INR3,000 crores worth of supplies in the coming two years" not tested; 30,000 Cr market caught |
| B | B06 Q2, Part 4; source Q4 FY26 p.8, p.11, p.22 (Patel) | OVERSTATED. Q2b "without demand loss" CONTRADICTED, labelled most consequential: the phrase came from B05's question; CNL MD said consumption is decreasing and consumers cannot digest 30 to 40% hikes; only the p.8 3 to 4 year demand remark supports a contradiction |
| B | B05 2D, 4D; source Q2 FY27 p.11 (Thakur); Q2 FY27 results p.15 | OVERSTATED. Brand GP 40 to 42% vs segment result 32.7 to 34.2% graded MEDIUM HIGH; segment result is "after deducting allocable cost", at or below GP by construction; non reconciliation, not evidence the claim is wrong |
| B | B05 2B, 4D; source Q2 FY26 p.5; Q4 FY26 p.15, p.16, p.22, p.26 | OVERSTATED. "Chairman mis-statements": "guidance 359-360" defensible from "close to INR360 crores, INR370 crores"; "turnover has got doubled" was CFO Thakur, not the Chairman; "March 700 Cr" stands |
| B | B05 3C; source Q2 FY26 p.12 to 14 (Pulwani; Kanvinde) | PARTIALLY CAUGHT. CFO gave one analyst incompatible answers (ex brand EBITDA ~0.2% "absolutely on the right" vs standalone distribution EBITDA 2.58%); read by B05 as "thin core margin" |
| B | B05 3A; B06 Q1; source Q2 FY26 p.6; Q4 FY26 p.13; CPPLUS Q2 FY26, Q3 FY26, Q4 FY26 (Khemka), Q1 FY27 (Nair) | PARTIALLY CAUGHT. CNL "only four to five" STQC firms and "never allow a foreign company" vs CPPLUS "over a dozen", "about 30 ... a dozen global", "40 plus"; CPPLUS calls partner Matrix "more of a regional player"; not tied back to CNL's moat framing |
| B | B05 3A, 4A P4; source Q2 FY27 p.8 (Patel) | PARTIALLY CAUGHT. Infinova: "share buyback of a foreign national" and Chinese beneficiary STQC condition met only on transfer; not called out |
| B | B05 3D, 2B; source Q2 FY26 p.5, p.15; Q4 FY26 p.15; REDINGTON Q4 FY26 (Hariharan) | PARTIALLY CAUGHT. Honeywell overseas fell from ~82 Cr (H1 FY26) to ~55.6 Cr (H2, derived) after "good traction" claim; conflict began 28 Feb 2026, so most of the drop predates the war it is attributed to; untested |
| B | B05 0; source Q2 FY27 p.7, p.16 to 17 (Patel) | PARTIALLY CAUGHT. WOZOYO: MD answered "Yes" to an analyst's 80 Cr in three to four months before restating 48 to 50 Cr; three first year ranges (45 to 50, 48 to 50, 40 to 50) in one call |
| C (C-G2) | Gate 0 B3, DB2; framework 01 L14 show every number | B3 ratio not shown, bound garbled; correct cum FCF at or below -334.83, B3 at or below -1.55, score 0; DB2 typo "Block B 8 < 8". Decision effect none |
| C (C-G3) | Gate 0 M11; framework 01 L15 to 18 anchors, L189 to 190 proxy in data_notes | M11 inputs unanchored; S&A as selling proxy absent from data_notes. M11 3 unchanged |
| C (C-E2) | Emerging moat Section 5 table; framework 07 L171 to 174 all 23 rows | Table collapses 15 zero rows and miscounts them as "other 14 + I1, I2" (should be 13 + I1, I2): A1 A2 A3 B1 B2 B3 D1 D2 E1 E2 F2 G1 H3 I1 I2. Total unchanged |
| C (C-E3) | Emerging moat G2 row 2, G1, F2, H2, 1C; framework 07 L35 to 36 source anchors | Evidence items anchored to upstream stages (B01/B05), not source documents. No score effect |
| D | B06 Q10b; source RPTECH_2026-08 l.605 (Pansari); RPTECH_2025-11 l.772 | B06 states Super Micro is not in any transcript; it appears in RPTECH Nov-25 and Aug-26 as OEM partner in neo cloud and DC bids. Q10b verdict (UNVERIFIABLE) unchanged |
| D | B06 Q10a | Q10a VERIFIED: current revenue conversion rests on REDINGTON alone; RPTECH did no AI DC project in FY26 |
| D | B06 Q1, Q7; source CPPLUS_2025-11 l.638 to 650 (Khemka) | CPPLUS Honeywell commentary under used for the Q1/Q7 share risk read: Honeywell type global brands certified but no products, slow to cover mass distribution, sourcing only brands not a share play |

## Verifier notes carried as written

- Verifier A coverage: every B01 value re-derived from CNL-Data_Sheet.csv and traced to AR p.97 to 98, p.104 to 105, p.109 and Q2 FY27 results p.5, p.11 to 13, p.15; zero mismatches. Sample tier 337 of 455 material numbers in B02 to B09 checked. Stage 8 and 9 web citations (aggregators, third party market sizes) were marked unanchored web and not verified; B09 arithmetic on those inputs was recomputed and holds.
- Verifier A on FY26 CFO: -271.88 Cr prints in the audited AR (p.98) and the Q2 FY27 deck; -273.10 Cr prints in the Q4 FY26 results. Both are carried faithfully by the stages that cite them.
- Verifier B: credibility grade concur "lower: C fits the 6/5/8 tally, but two explanations it files as external (Middle East, Diwali) fail peer tests and the CFO's debt bridge to analysts does not reconcile to the audited balance sheet; C toward D". Promise delivery spot checks 5 of 5 confirmed. Pipeline flags not supported: none.
- Verifier C: recomputed decision concurs with Gate 0 AVERAGE (pinned by DB4) and the combined AVERAGE. On em_score the stage filed 12.8; Verifier C recomputes 12.5 because C1 rests on claim only substance. Both read MODEST.
- Verifier D: claims all addressed; no substantive use unsupported; no verdict discipline fails.
