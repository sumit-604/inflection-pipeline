# TLL (Trident Lifeline Ltd): verifier summary, phase 1

Run: tll-2026-09-26. Phase 1 scope: Verifier A (numerical), Verifier B (red flags), Verifier C (Gate 0 and Emerging Moat portion only; valuation audit pending phase 3), Verifier D (peers).

## Confidence delta (phase 1)

| Component | Score | Basis |
|---|---|---|
| numerical_acceptance | 93 | B12a: 26 of 28 checked figures clean; material universe about 40 |
| redflag_coverage | 50 | B12b: 6 of 12 MATERIAL (2 CRITICAL, 10 MAJOR) caught upstream, partial counted as caught; full catches 3 of 12 (25%) |
| framework_adherence | 78.8 | B12c phase 1 only: 52 of 66 rules (Gate 0 35 of 43 = 81.4; Emerging Moat 17 of 23 = 73.9) |
| peer_utilisation | 91.7 | B06 coverage map: 11 of 12 peer quarter transcripts SUBSTANTIVE (B12d reports 92) |
| overall | 50 | set by redflag_coverage; not_applicable: none |

Band: FORCED REWORK (below 60). Orchestrator Section 4: any verifier acceptance rate below 60% makes the verdict REWORK regardless of company quality.

Acceptance rates: Verifier A 93; Verifier B 50; Verifier C 78.8 (phase 1); Verifier D 92.

Severity counts: Verifier A 1 CRITICAL (struck), 3 MAJOR, 24 MINOR. Verifier B 2 CRITICAL, 10 MAJOR, 11 MINOR. Verifier C 0 CRITICAL, 3 MAJOR, 8 MINOR. Verifier D 0 CRITICAL, 1 MAJOR, 2 MINOR.

## Verifier A identity check

Critical rows: 1. Struck: 1. Surviving CRITICAL: 0.

Struck row: B05 Section 1B revenue mismatch. The claimed value and source_truth hold the SAME value (Rs 10,607.05 lakh stated in the H2/FY26 deck p27 as "Revenue from Operations"). Stage 5 reported the company's own mislabel faithfully and flagged it. The row is a clerical error in the finding, not a misread figure. It was struck under the run-pipeline step 5 identity check. The company disclosure defect stays live (B05 FLAG-DISCLOSURE; B12b partially caught row).

Source fidelity flags live (confidence.yaml):
- B12a MAJOR: FY25 CFO minus Rs 10.24 Cr (FY25 AR) against minus Rs 3.99 Cr (FY26 AR comparative); swing unanchored to any restatement note. Both figures exist; the reclassification line is the issue.
- B12a MAJOR: segment note receivables Rs 4,947.50 lakh against consolidated Note 17 Rs 7,365.39 lakh, unreconciled.
- B12a MAJOR: Rs 500 lakh guarantees to non-consolidated director interest LLPs (disclosure cross link; B12a marks this row source_fidelity false).

## Verifier disagreements

none. The one Verifier A row struck was struck on the identity check (a clerical row), not cleared against a source. No downstream step has used a flagged number. No verifier-disagreement-log.md file is written this phase.

## Findings, CRITICAL

| # | Verifier | Location | Note |
|---|---|---|---|
| C1 | B (red flags) | Prospectus 2022 p220; AR FY25 p19; Reg 30 01 Sep 2025; FY26 results audit report | CA Ashish Bafna (M.No.106525) signed the IPO restated financials as Partner of A Bafna & Associates on 29 Jul 2022. CFO from 17 Jul 2025, Executive Director from 01 Sep 2025. The firm still signs the FY26 audit and Q1 FY27 review. Reg 30 profile and AGM notice omit the link. Follows the CFO/WTD exit (16 May 2025) and CS exit (30 May 2025). Upstream: MISSED by B05/B06; B08 raised it as UNRESOLVED although the corpus prospectus resolves it. |
| C2 | B (red flags) | Nov 2025 deck p31; Jan 2026 deck p31; May 2026 deck p30; FY26 results p8 | Bank working capital facilities moved into operating cash flow (FY25 545.38, FY26 920.49 lakh). FY25 CFO shown as minus 349.31 in two decks, then plus 197.07 in the May 2026 deck with no note. FY26 CFO 793.22 is about minus 127.27 on the prior basis. Upstream: CAUGHT (B05 carries B02/B03 finding); B05 calls it "not a deck matter", but the decks show the restatement. |
| C3 | A (numerical), STRUCK | B05 Section 1B revenue mismatch | H2/FY26 deck p27 states standalone "Revenue from Operations" Rs 10,607.05 lakh; the audited filing shows this is Total Income (Sales 10,189.95 + Other Income 417.10 lakh); about 4% overstatement. source_fidelity true. Struck on the identity check: claimed and source hold the same value. |

## Findings, MAJOR

| # | Verifier | Location | Note |
|---|---|---|---|
| M1 | A | B02 Finding #1 / B03 LBF1 | FY25 CFO minus 10.24 Cr per FY25 AR, minus 3.99 Cr in FY26 AR comparative, difference 6.26 Cr. Both figures exist as cited; the swing is UNANCHORED to any disclosed restatement note. source_fidelity true. |
| M2 | A | B02 Finding #3 | Segment note receivables 4,947.50 lakh against Note 17 consolidated 7,365.39 lakh (gap 2,417.89 lakh); standalone Note 17 4,934.11 lakh (gap 13.39 lakh). Unreconciled within the same consolidated statements. source_fidelity true. |
| M3 | A | B02 Top 15 Finding #2 | CARO clause iii: 2,355.00 lakh guarantees to subsidiaries plus 500.00 lakh to Others, named in Note 32 as Talon Healthcare LLP and Tench Lifesciences LLP. MATCHES; flagged for off balance sheet risk. source_fidelity false. |
| M4 | B | Nov 2025 deck p29; Jan 2026 deck p29; May 2026 deck p27 to 28; AR FY26 Board's Report p19 | Total income presented as "Revenue from Operations" in three decks and the Board's Report. EBITDA includes other income; May deck says margin "stable at 27%". Aug deck p33 shows operating EBITDA margin 25.8% to 23.9% (minus 187 bps). Upstream: PARTIALLY CAUGHT (May deck instance only, graded MINOR to MODERATE). |
| M5 | B | AR FY26 RPT note; AR FY26 MD&A p27 | Sales to promoter interest LLPs Tench 722.72 and Talon 848.91 lakh (15.4% of standalone revenue). Receivables from them 885.35 lakh. Loans to Talon 149.12, Tench 217.38, Trident Texofab 326.48 lakh. MD&A credits the domestic rise (30% to 49%) to wider reach and names none of this. Upstream: PARTIALLY CAUGHT. |
| M6 | B | Q1 FY27 results p3; Jan 2026 deck p27 to 28; Nov 2025 deck p28; FY26 results p7 | Q4 FY26 standalone D&A 4.15 lakh against 71.23 (Q3) and 69.81 (Q1 FY27). H2 D&A 75.38 against H1 110.55 while tangible assets rose 799.58 to 1,826.55. Jan deck 9M FY26 PBT 1,667.60 does not equal H1 1,110.46 plus Q3 592.39 (gap 35.25). Upstream: MISSED. |
| M7 | B | FY26 results p16 note 8; Q1 FY27 results p5, p8; FY26 results p14; AR FY26 p17 | Consolidation method said to change from proportionate to equity with no material impact; Q1 FY27 note still consolidates a portion of subsidiary assets; Q1 FY27 review cites Ind AS 34 on an Indian GAAP filer. Employee cost minus 10.8% and other expenses minus 5.5% at revenue plus 48.4% carry the 470 bps margin claim. Upstream: MISSED. |
| M8 | B | AR FY26 Note 22 consolidated; AR FY26 Chairman p17 and MD&A p27 | Claim Income 541.05 lakh FY26 and 522.17 lakh FY25 equal 19.9% and 38.4% of consolidated PBT; narrative says PBT doubled and never names it. Upstream: MISSED by B05 (B02 caught the disclosure gap). |
| M9 | B | AR FY26 Chairman p17; AR FY26 MD&A p27; Nov 2025 to May 2026 decks p4 | Registrations 64% Africa; export revenue Asia 57%, Africa 25%, South America 17%; domestic sales outside export registrations drove FY26 growth. Registered count rose 30 in six months (1,061 to 1,091). Upstream: PARTIALLY CAUGHT. |
| M10 | B | Nov 2025 deck p15; May 2026 deck p15; AR FY26 MD&A p27; Aug 2026 deck p30 | Product mix called "broadly stable"; toothpaste, mouthwash and ointments fell from 36% to about 1% of revenue; capsules 6.8 to 30.6 Cr (plus 350%); others 49.0 to 30.1 Cr. Upstream: MISSED. |
| M11 | B | Reg 30 01 Sep 2025 and 21 Nov 2025; Aug 2026 deck p21; AR FY26 p21 and RPT note | Promoter spouse recommended for reappointment, resigned two months later for personal reason, then shown as COO with no senior management Reg 30 filing in corpus. FY26 pay 18.00 lakh against 9.78. Upstream: MISSED by B05; B08 reads the exit as reduced family presence. |
| M12 | B | Aug 2026 deck p5, p11 to 15; AR FY26 MD&A p28 | Triple consolidated business in three years and subsidiary peak revenues appear only in the deck, not in the AR outlook filed weeks later. Upstream: CAUGHT. |
| M13 | B | Statement of Deviation 28 Jul 2025 line 99; AR FY26 Board's Report lines 1677 to 1681 | IPO registration allocation: 51.87 of 513.66 lakh used by Jun 2025, 75.81 by Mar 2026, while every deck claims substantial yearly outlay on registrations. Upstream: CAUGHT; B05 did not cite the Mar 2026 update. |
| M14 | C (Gate 0) | 01-gate0.md Block A lines 69 to 106; Block F M3 line 220; B01 data_notes[0] | EBIT computed excluding Other Income against a fixed formula. Rule literal EBIT (PBT plus Interest) gives ROCE 13.98% / 17.33% / 21.02%; A1 = 3, A2 = 3, Block A = 16; M3 = 3 (present). Carry the operating basis as a sensitivity. Classification unchanged (AVERAGE). |
| M15 | C (Gate 0) | 01-gate0.md Block F M4 lines 223 to 227; B01 data_notes[4] | M4 scored 1 by judgment; literal tier "max 1 decline year, fully recovered = 3" fits zero decline years. M4 = 3; moats confirmed 1 to 2 (3 with M14), moat class THIN to MODERATE. Classification unchanged. M10 = 0 correct. |
| M16 | C (Emerging Moat) | 07-emoat.md Section 2C lines 87 to 97; B07 capex_embedded_growth_pct | 2C not run. CWIP 17.50 Cr x FAT 2.12x = 37.2 Cr = 28.8% above FY26 revenue 129.02 Cr. The stated blocker is false and irrelevant to CWIP. em_score and classification unaffected; feeds the stage 11 CAPACITY basis. |
| M17 | D (peers) | B06 report Part 3 / B06-peers.yaml peer_coverage_map, SENORES Jan 2026 row | SENORES Jan 2026 transcript lines 1310 to 1315 give a quantified 90 to 94 day cycle; B06 tagged it CITED-ONLY. A second independent peer anchor for the debtor days contradiction was left unused. |

## Findings, MINOR

| # | Verifier | Location | Note |
|---|---|---|---|
| m1 | B | 20260507 results p7 line 347; AR FY26 Board's Report line 1601; AR FY26 MD&A p27 line 1259 | FY26 standalone EPS stated three ways: 15.50, 15.37, 15.73. Upstream: MISSED. |
| m2 | B | AR FY26 p18 to 19 vs p28 | KPI page and ratio table disagree: ROE 22.2% vs 0.31, ROCE 17.5% vs 0.21, net D/E 0.7 vs D/E 1.24. Upstream: MISSED. |
| m3 | B | AR FY25 Chairman p13; Reg 30 05 Mar 2025; AR FY26 | Vorinostat/NIPER promise has no FY26 status update. Upstream: MISSED by B05 (B07 tracks it as optionality). |
| m4 | B | Q1 FY27 results p3, p7; Aug 2026 deck p33 to 35 | Q1 FY27 revenue fell 16% standalone (2,684.23 vs 3,197.01) and 32% consolidated (3,371.8 vs 4,995.34) against Q4; Q4 stock in trade purchases 718.42 spike; deck shows YoY only. Upstream: MISSED. |
| m5 | B | Aug 2026 deck p17 to 18; May 2026 deck p14; AR FY26 SWOT | Registrations "intrinsic value" about 80 Cr; 3,625 "products in portfolio" counts applications; 1,091 are registered. Upstream: PARTIALLY CAUGHT. |
| m6 | B | Aug 2026 deck p12, p14 | Lorem ipsum placeholder text in a filed Reg 30 deck. Upstream: CAUGHT. |
| m7 | B | Nov 2025 and Jan 2026 decks p18 vs May 2026 deck p18 | Lead export market switches from South America to Asia with no explanation. Upstream: CAUGHT (as a fact). |
| m8 | B | 20241220 and 20251114 rectification letters | BSE flagged the same trade payable bifurcation defect two years running. Upstream: PARTIALLY CAUGHT (B05 graded the refilings Positive); B05 4C verdict OVERSTATED. |
| m9 | B | B05 1B and 4D | B05 says the mislabel was silently corrected; the FY26 Board's Report (lines 1609 to 1614) repeats "revenue from operations of 10607.05 Lacs". Pipeline accuracy; B05 flag OVERSTATED. |
| m10 | B | B05 2A row 2 | B05 calls H1 FY26 margin compression consolidated; the Nov 2025 deck p27 to 28 figures are standalone. Pipeline accuracy; OVERSTATED. |
| m11 | B | B06 Part 3 INNOVACAP Q1 FY27 row | The 65 to 70% utilisation over 4 to 5 years quote is from the Nov 2025 call, lines 712 to 714, not Aug 2026 (line 1022 repeats 65 to 70% only). TLL states capacity on a two shift basis; B06 does not compare the basis. Pipeline accuracy; SUPPORTED, misdated. |
| m12 | C (Gate 0) | 01-gate0.md Block B B2/B3 lines 113 to 121; B01 input_gaps[3] | FCF proxied as CFO plus net investing CF, but the AR carries Purchase of Fixed Assets 3,647.24 lakh (FY26) and 1,109.95 lakh (FY25) as a separate line. Defined FCF FY26 minus 31.78 Cr, FY25 minus 21.34 Cr. B2 and B3 stay 0. The false gap propagated into B07 Section 2C. |
| m13 | C (Gate 0) | 01-gate0.md A3 line 99, D3 lines 157 to 159, E4 lines 182 to 189 | Three net worth bases in one scorecard (100.40, 107.89, 96.68 Cr). E4 on the A3 basis = 4.98%, band 5 (not 3). Inconsistency not stated. Classification unchanged. |
| m14 | C (Gate 0) | 01-gate0.md Block F M5 line 228 | M5 marked PEER DATA NEEDED while peer Data_Sheets carry market caps (TLL 487.49, SENORES 6,241.18, INNOVACAP 7,330.51, CAPLIPOINT 21,550.08 Cr). Score 1 or state why the four name set is not the segment. Not a present moat either way. |
| m15 | C (Emerging Moat) | 07-emoat.md Section 5 lines 321 to 346 | Multiplier products rounded inconsistently (A4 0.5 shown 1; C1 0.7 shown 1; E1 2.1 shown 2). Unrounded total 7.3, not 8. Band unchanged (NONE). |
| m16 | C (Emerging Moat) | 07-emoat.md Section 3 E1 lines 176 to 184, recount line 281, Section 5 line 334 | E1 counted as documented in the recount but scored at the claim multiplier 0.7x. At 1.0x total = 8.2; band unchanged. |
| m17 | C (Emerging Moat) | B07-emoat.yaml capex_embedded_growth_pct | Numeric 0 emitted for a figure the report marks NOT FOUND; downstream reads 0% capacity growth. Emit the recomputed value or NOT FOUND. |
| m18 | C (Emerging Moat) | B07-emoat.yaml active_categories | Schema allows only Strong/Moderate rows; block lists six including four Weak or Weak-Moderate. A consumer counting active_categories reads 6, not 1. |
| m19 | C (Emerging Moat) | 07-emoat.md Optionality Register lines 364 to 375 | C1 (claim only cross sell) and A4 (inference only platform breadth) meet the register test and are absent. |
| m20 | D (peers) | B06 report Part 3, closing coverage count line | Prose says ten of twelve transcripts SUBSTANTIVE; the table lists eleven. No verdict or acceptance rate impact. |
| m21 | D (peers) | B06 report Part 1, Q2 net read paragraph | INNOVACAP utilisation quote (lines 712 to 714) not labelled with its Nov 2025 call date in the sentence; YAML anchor correct. Prose clarity only. |
| m22 | A | B01 ROCE table | ROCE (operating) FY26 14.80%; 22.04 / 148.94 = 14.78%. Rounding only. |
| m23 | A | B03 Standalone Balance Sheet | Standalone Share Capital 1,193.30 lakh FY26 (AR p54 to 55). MATCHES. |
| m24 | A | B01 Consolidated Balance Sheet Current Liabilities | FY24 Current Liabilities 20.26 Cr from AR; basis difference from screener correctly noted. Verified. |
| m25 | A | B02 Shareholders Funds vs Balance Sheet | The 749.02 lakh gap is Minority Interest on the same balance sheet; 8,474.26 + 1,193.30 + 749.02 = 10,416.58 matches. B03 corrected this finding. |
| m26 | A | B03 Goodwill jump | Goodwill 52.37 (FY25) and 555.15 lakh (FY26), Consolidated Balance Sheet p95. MATCHES; no explanatory note exists, as flagged. |
| m27 | A | B01 Block B Working Capital Days | FY24 151.1, FY26 202.8, change 51.7 days. Method consistent with AR data; FY24 trade payables 7.54 Cr from AR notes. |
| m28 | A | B03 Promoter shareholding Note 1.6 | 75,00,200 shares = 62.85% at 31 Mar 2026 (Note 1.6 p58 to 59). MATCHES. FY25 comparative repeats the same count and % against a 1,14,99,200 share base (should be 65.22%): stale copy error in the AR. |
| m29 | A | B04 revenue claims | TNS Pharma FY26 turnover 576.52 lakh = 5.77 Cr (AOC-1 p40). MATCHES. |
| m30 | A | B04 revenue claims | Trident Mediquip FY26 turnover 2,731.75 lakh = 27.32 Cr (AOC-1 p40 to 41). MATCHES. |
| m31 | A | B04 revenue claims | TLL Parenterals "Not commenced operations", turnover nil (AOC-1 p40). MATCHES. |
| m32 | A | B05 Registration pipeline | 1,091 registered, 2,534 in process (Aug 2026 deck p4 to 5). MATCHES the deck; a company claim, not third party verified. |
| m33 | A | B01 ROCE all-in table | FY26 21.03% shown 21.02%; FY25 17.31% shown 17.33%. Rounding; alternative basis correctly footnoted. |
| m34 | A | B01 Revenue CAGR | (129.02 / 21.77)^0.25 minus 1 = 56.05%. MATCHES. |
| m35 | A | B01 PAT CAGR | (19.04 / 3.95)^0.25 minus 1 = 48.16%. MATCHES. |
| m36 | A | B01 Block C4 | 48.16% minus 56.05% = minus 7.89 pp. MATCHES. |
| m37 | A | B01 ROE computed | Median ROE 23.10%; exact average not recalculated; order of magnitude consistent. |
| m38 | A | B01 Interest on tax | Interest on late payment of Income Tax FY26 34.56 lakh, FY25 13.90 lakh (Note 28.2 p111). MATCHES. |
| m39 | A | B02 Top 15 Finding #6 | TNS Pharma investment cost 153 to 255 lakh (Note 11); not re-verified at line level; deferred to prior stage accuracy. |
| m40 | A | B02 Top 15 Finding #9 | Warrant proceeds 2,657.34 lakh, utilised 1,526.57 lakh (57.5%), Statement of Deviation 28 Jul 2025 p2 to 3. MATCHES. |
| m41 | A | B02 Top 15 Finding #14 | Claim Income 541.05 (FY26), 522.17 lakh (FY25), plus 3.62% (Note 22 p110 to 111). MATCHES. |
| m42 | A | B03 Section 3C Standalone Revenue | Standalone FY26 revenue 10,189.95 lakh matches audited results; the 106.07 Cr in the H2/FY26 deck folded in other income (417.10 lakh). |
| m43 | A | B01 Block D Assets | Total Assets FY25 155.54 Cr (screener Data_Sheet). MATCHES. |
| m44 | A | B01 Cash Flow Statement | Purchase of Fixed Assets FY26 3,647.24 lakh (consolidated cash flow p96). MATCHES. |
| m45 | A | B03 ROE Ratio internal inconsistency | AR p19 KPI ROE 22.2% vs p28 ratio table 0.31; both correctly transcribed; inconsistency sits inside the AR. |

## Verifier B, other records

- Pipeline flags not supported: B05 "silently corrected" (OVERSTATED); B05 4C refilings Positive (OVERSTATED); B05 2A consolidated margin compression (OVERSTATED); B06 INNOVACAP ceiling attributed to Aug 2026 (SUPPORTED, misdated).
- Promise delivery spot checks: 5 checked, 5 confirmed, 0 wrong.
- Credibility grade concurrence: lower. "C holds only as the no-concall default; an undisclosed auditor-to-CFO move plus repeated income mislabelling and a silent CFO reclassification argue below C."

## Verifier C, recomputed figures (phase 1)

- Gate 0: blocks A 16, B 0, C 16, D 12, E 8; core 52; moat 14; moats confirmed 3; moat class MODERATE; grand total 66; classification AVERAGE (unchanged).
- Emerging Moat: em_score 7.3 (8.2 if E1 scored documented); classification NONE (unchanged); capex_embedded_growth_pct 28.8.
- Valuation, expectation ledger and recomputed destination PE: pending phase 3.

## Verifier D, other records

- Peers audited 12; substantive confirmed 7; substantive unsupported none; claims all addressed: true; verdict discipline fails: none.
