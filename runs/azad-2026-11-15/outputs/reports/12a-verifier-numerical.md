# Verifier A, Numerical Accuracy: AZAD, 2026-11-15

Model: claude-sonnet-5-5. Inputs: stage reports 01 to 09 (with 02 pass 1, pass 2 and ERRATA appendices) and the source PDFs and page-marked .txt extractions in inputs/. Units: filings and ARs in INR million, screener and CARE in INR crore; conversions checked each time.

## Result in four lines
1. Mandatory tier: 78 of 78 Gate 0 scorecard inputs checked. All match their sources.
2. Sample tier: about 322 further numbers checked across stages 2 to 9. All match except three rows below.
3. Three findings: 0 CRITICAL, 1 MAJOR, 2 MINOR. Two carry `source_fidelity: true`.
4. No verdict-card or Section 1B pillar inputs exist in stages 1 to 9, so none were in scope.

## Findings table

| Severity | Report location | Claimed value and anchor | Source truth and location | Note | source_fidelity |
|---|---|---|---|---|---|
| MAJOR | 02-notes.md Top-15 rank 9 and yaml top_findings rank 9: "5% rupee recovery costs 104.04", cited to Note 34 PDF pp.244-245 (consolidated) | 104.04 | Consolidated Note 34 USD sensitivity is 104.07 (AR2026 p.245, text line 12680). 104.04 is the standalone USD figure (text line 9061). | MISMATCH of basis: the standalone value is cited as the consolidated note's figure, and 02-notes names no basis. 0.03 apart. No verdict input depends on it. 03-ardeep.md rank 9 row already corrects to 104.07. Severity MAJOR by rule 5 (mismatch outside the mandatory tier). | true |
| MINOR | 02-notes.md P3-1 (standalone OCF, also in the B02 FLAG-CASH text) | Standalone OCF (1,232.63) vs 628.85, "[page 156] cash flow area" | Values correct. They are on AR2026 PDF page 123 (standalone cash flow statement, line "Net cash (used in)/ flow from operating activities A", text line 6437). Page 156 is standalone Note 17, trade payables. | ANCHOR NOT FOUND at the cited page; the number exists at p.123. The stage's ERRATA and 03-ardeep.md correction 2 already name p.123. Not a mandatory-tier input. | true |
| MINOR | 03-ardeep.md Phase 1B, KAM row: "Q4 revenue was 1,573.9 Rs Mn, 26.1% of the year [calc] (AR26 [p.13])" | 26.1% = 1,573.9 / consolidated 6,029.75; Q4 basis not named | AR26 p.13 prints "H1,573.9 million" for Q4, so the quote is faithful. Q4 FY26 results p.10 print consolidated Q4 revenue 1,615.39 Mn (26.8% of 6,029.75). The AR figure matches neither the consolidated Q4 nor the standalone Q4 column. | UNANCHORED basis. An unlabelled-basis quarter is divided by a consolidated year, and the 41.5 Mn gap to the filed consolidated quarter is not named. No verdict input depends on it. | false |

CRITICAL 0, MAJOR 1, MINOR 2. Rows struck under rule 5b: 3.

## Mandatory tier (OR-32): Gate 0 scorecard inputs, 78 of 78 checked

| Group | Count | Source tested | Result |
|---|---|---|---|
| Sales, PBT, Interest, PAT, CFO FY21 to FY26 (screener) | 30 | screener-Data_Sheet.csv rows 11, 21, 22, 24, 57; spot-tied to Prospectus p.72-73 (FY21 to FY23 Mn) and AR2026 p.192-193 | MATCH |
| Net worth FY21 to FY26 (share capital + reserves) | 6 | CSV rows 39-40: 90.89, 120.00, 203.99, 645.06, 1,393.79, 1,528.90 | MATCH |
| Capex FY21 to FY26 | 6 | Prospectus p.73 (203.84, 1,171.47, 856.22 Mn); AR2025 (753.40); AR2026 cash flow (2,932.52; 5,724.80) | MATCH |
| EBITDA FY21, FY25, FY26 | 3 | Rebuilt from CSV expense rows: 28.15, 161.31, 225.32. Four-quarter Operating Profit sums: FY25 161.31, FY26 225.31 (0.01 rounding) | MATCH |
| Total assets and current liabilities FY21 to FY26 | 12 | CSV row 43; Prospectus p.71 (1,125.20; 1,478.76; 1,482.08 Mn); AR2025 (982.22); AR2026 p.191 (2,301.14; 3,026.71) | MATCH |
| Receivables, inventory, payables FY21 and FY26 | 6 | CSV rows 49-50; payables 373.05 Mn (Prospectus p.71), 852.74 Mn (AR2026 p.191: 181.12 + 671.62) | MATCH |
| FY26 borrowings 474.32, cash and bank 184.59, other income 45.65, current assets 9,892.99, net block 779.34 | 5 | CSV rows 41, 51, 19, 44; AR2026 p.191 | MATCH (474.32 = 4,566.39 borrowings + 176.84 leases; 184.59 = 245.92 + 1,599.99) |
| Selling and admin FY21 and FY26; R&D "NIL" | 3 | CSV row 17 (7.68; 22.38); AR2026 text line 2456 | MATCH |
| Promoter 55.84% (Sep 2026), 64.84% (post-IPO), pledge false | 3 | Shareholding XBRL 0.5584 and pledge flag false; Prospectus p.92 (38,330,255 shares, 64.84%) | MATCH. The report labels the 55.84% as promoter plus group; the promoter alone is 54.88%. Basis correctly named. |
| Contingent liabilities 19.67, 2.13, 220.94, 50.59 | 4 | AR2026 note 28(a), p.232 (sum 293.33; 1.92% of equity 15,288.36) | MATCH |

Derived scorecard values recomputed and tied: ROCE series 15.04, 20.96, 14.86, 18.32, 8.73, 11.50 and median 14.95; ROE series and median 10.87; revenue CAGR 37.5%; PAT CAGR 63.1%; cumulative CFO -56.75, PAT 328.21, FCF -1,220.97; net debt 289.73 and 1.29x; interest cover 7.08x and 5.60x; debt/equity 0.31; current ratio 3.27; WC days FY21 147.4 and FY26 336.3; Sep 2026 annualised 369.3; M1 to M12 inputs.

Verdict-card inputs: none exist (stage 13 not run). Section 1B pillar inputs: none exist (stage 11 not run). Neither was in scope; no figure was skipped.

## Sample tier (about 322 further numbers; universe about 900)

Materiality rule: a number counts as material if it feeds a flag, a score, a verdict input, a tripwire or a handoff field. Headline P&L, balance sheet, cash flow, QIP, customer, guidance, peer, market and ownership figures qualify. Table cells that restate a checked figure were counted once. The universe of 900 is my count; the checked count of about 322 is approximate for the same reason.

What was checked, by report:
- B01 load-bearing facts: QIP 7,000/6,217.60/782.40, capex object 4,494.60 of 5,250.00 and 3,686.65 at Mar 2026 (Q2 FY27 results p.6, Q4 FY26 results p.13); H1 OCF (436.24) vs (758.90) (p.11); current ratio 10,932.99 / 4,390.33 (p.10); borrowings 5,616.25 and 4,566.39; CWIP and PPE; H1 capex 1,397.51 vs 3,067.88; customer note 1,123.97, 1,711.10, 648.81, 631.30; quarterly growth rates; consolidated Q2 revenue 1,909.35 and H1 3,635.34.
- B02: standalone vs consolidated OCF, PBT, tax, DTL, comprehensive income; working-capital drain 3,034.45 rebuilt line by line; borrowings, net cash to net debt; receivable ageing buckets and cover ratios; government balance 1,102.51 vs 554.83; QIP table, auditor idle funds 1,600.06; commitments 1,182.77; FX 214.01, 158.16; Atlas Fasteners 17.19 vs 2.24; promoter 59.35% to 54.88% and 28,85,267 shares; capitalised borrowing cost 20.20; PPE additions 3,961.55; CWIP ageing; pass 1 lines 1 to 60. The FX sensitivity found the MAJOR row.
- B03: Chairman's letter working-capital days 244 vs 202 (p.7); build-out 70% to 80%; guidance ">25%" (p.36) and "~30%" (AR2025 p.40); delivered 31.84% and 30.35% (p.38); segment table 4,811.3 / 3,586.3 / 1,012.6 / 807.4; ROCE 10.7% vs 8.7%; EPS 20.57 vs 14.66; shareholding table 14.75%, 10.19%, 5.48% and 94,58,699 shares; AOC-1 16.68 and (2.69); order-book split; MHI 13,870; GE Steam 53.5; DIN conflict 03132157 vs 03132757; attendance; pay 528 lakh; employees 2,168; non-managerial pay +47.52%; the 104.07 USD correction (confirmed correct).
- B04: standalone and consolidated revenue bridge (1,878.03; 3,583.22; 1,909.35; 3,635.34; total income 1,924.58; 1,951.05); CARE 344/287 days with 262/163/80; H1 unit economics (EBITDA 1,366.35, EBIT 955.04, other income 77.19 vs 209.36); deck figures (1,366.4; 44,800 sq m = 7,600 + 7,200 + 7,600 + 7,200 + 2 x 7,600; domestic 430.3 vs 168.2; segment 2,904.6 and 603.7); concall figures (80.8 Cr, 423.8 Cr net debt, 1,169 Cr, 5.8x, 45.2% vs 43.7%, USD 4.5 Mn); Prospectus peer table (revenue, EBITDA, ROCE).
- B05: standalone OCF (458.16) vs (765.25) and its decomposition (operating profit 1,305.57 vs 1,010.56; tax 188.37 vs 245.55; payables 103.32; other financial liabilities 239.74; MSME 436.72); standalone receivables 4,016.18 and inventories 4,248.03; Q2 call OCF (45.8) and 76.5 (these are the standalone figures, 458.16 and 765.25 Mn), QIP 621.8 / 78.2, capex 139.3, capitalised 251, export 88%, 85%; Q4 call quotes (closer to 200 days, 160 to 170, 96%, 180 to 190 crores, O&G under 10 crores); Q1 call 200 days and debtors to 90 days; net debt gap 470.6 and 474.1 vs 423.8 Cr; PAT figures 363.52, 299.94, 671.73, 660.87; employee cost 502.93 vs 406.56; Q2 other income 46.55 vs 127.23; CARE order book 3,966 and 1,834; deck USD contract values.
- B06: MTAR 260, 172, 59 and 50 days; USD 1 million discounted; 30%, 40% advances; 15 of 16 fungible units; order book 650 and 820 Cr; reconciled to the transcript text.
- B07: QIP Cr conversions, GE Vernova 22,800 of 44,800 sq m = 50.9%, segment growth 28.3%, 0.790x turnover and 27.8% capex-embedded growth.
- B08: shareholding XBRL (Rakesh 35,444,988 = 54.88%; Jyoti 441,300; Satwik 148,650; lock-in 11,827,600 = 33.37%; FPI 9.84% + 2.86% = 12.70%; domestic institutions 10.40%); IPO OFS 3,911,545 shares at Rs 524 and Rs 2,049.65 Mn; Prospectus p.249 education line; pay and rent figures.
- B09: Prospectus energy turbine table (4,862 / 5,094; 15,814 / 16,568; 364 / 536; 5,523 / 3,969; 1,157 / 1,216; totals 28,325 and 28,270; 27,167 and 27,054); Prospectus p.200 A&D 99k to 153k Cr and 7% CAGR; deck 1,190 / 2,190 / 310 / 930 bn, 75% gas OEM share, USD 40 Mn and USD 16 Mn, 96%+; market cap 15,860.63 and CMP 2,455.9 from the screener sheet; concall domestic INR 43 crores; SOM and TAM arithmetic.

Not checked (named): most of 02-notes-pass1 beyond line 60 and 02-notes-pass2; 03 board and compensation tables beyond samples; 06 peer figures beyond about a dozen; 07 narrative items and web-sourced claims; 08 MEDIA items (bulk-deal price Rs 1,623.78, 48 lakh share block, Rs 780 Cr); 09 live-web figures (GE Vernova 122 GW and USD 21.8 bn orders, Siemens Energy EUR 164 bn, Howmet USD 1,451 Mn, MHI, Baker Hughes, USD 93.70 FX). Those web figures are outside the PDF corpus and cannot be source-checked here; 09 itself marks several PENDING LIVE VERIFICATION.

## Rule 5b self-check
Candidate rows struck: 3.
1. FY26 EBITDA 225.32 (expense-row build) vs 225.31 (sum of four quarterly operating profit rows). Gate 0 says they tie. The 0.01 gap is rounding of a matched figure. Struck.
2. H1 consolidated revenue written as 3,635.4 in places and 3,635.34 elsewhere. Same value, different formatting. Struck.
3. B09 "37.4% FY21-25 standalone CAGR (Q2P p.16)". The deck header says "CAGR (FY21-25)" but the columns run FY21 to FY26; (5,903.8 / 1,205.1)^(1/5) - 1 = 37.4% is right. A faithfully transcribed anomaly in the company's slide. Struck.

The three retained rows were tested against the three 5a classes. Row 1 (104.04 vs 104.07) has two different values and no named basis. Row 2 is a page that does not hold the figure, number correct. Row 3 is an unlabelled basis difference, which rule 5a says is a finding.

## Notes for the orchestrator (not findings)
- Stage 3 corrected stage 2 on the p.123 anchor and on 104.04 to 104.07. Both corrections are right on the page.
- Gate 0's "top-5 28.4% (inclusive reading)" was ruled out by stage 3 on arithmetic. No source number is wrong. The AR consolidated note prints "Revenue from top 5 customers 1,711.10" without the qualifier; the standalone note adds "(other than above customer)". Stages 2 and 3 record both.

```yaml
stage: B12a
company: "AZAD"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
numbers_checked: 400
mandatory_checked: 78
mandatory_total: 78
findings:
  - {severity: "MAJOR", location: "02-notes.md Top-15 rank 9 and yaml top_findings rank 9: '5% rupee recovery costs 104.04' (Note 34, PDF pp.244-245, consolidated notes)", claimed: "104.04", source_truth: "Consolidated Note 34 USD sensitivity is 104.07 (AR2026 p.245, text line 12680). 104.04 is the STANDALONE USD figure (text line 9061).", note: "MISMATCH on basis: standalone value cited as the consolidated note's figure. 0.03 apart; no verdict input depends on it. 03-ardeep.md rank 9 row already corrects to 104.07. Struck neither as matched (values differ) nor as a labelled basis difference (02-notes names no basis).", source_fidelity: true}
  - {severity: "MINOR", location: "02-notes.md P3-1 (and carried in B02 flag text): standalone operating cash flow (1,232.63) vs 628.85 cited as '[page 156] cash flow area'", claimed: "AR2026 [page 156]", source_truth: "Values are correct. They sit on AR2026 PDF page 123 (standalone cash flow, line 'Net cash (used in)/ flow from operating activities A'). Page 156 is the standalone Note 17 trade payables page.", note: "ANCHOR NOT FOUND at the cited page; number exists at p.123. The stage's own errata and 03-ardeep.md correction 2 already give p.123. Not a Gate 0 input; consolidated OCF (1,189.66, p.193) is correct. MINOR because the figure is not a mandatory-tier input and the report self-disclosed the anchor as unverified.", source_fidelity: true}
  - {severity: "MINOR", location: "03-ardeep.md Phase 1B: 'Q4 revenue was 1,573.9 Rs Mn, 26.1% of the year [calc] (AR26 [p.13])'", claimed: "26.1% (1,573.9 / consolidated 6,029.75 Mn); Q4 basis not labelled", source_truth: "AR26 p.13 does print 'H1,573.9 million' for Q4, so the quote is faithful. The filed Q4 FY26 consolidated revenue is 1,615.39 Mn (Q4 FY26 results p.10), which is 26.8% of 6,029.75; the AR figure matches neither the consolidated Q4 nor the Q4 FY26 standalone column.", note: "UNANCHORED basis: the report divides an unlabelled-basis quarterly figure by a consolidated annual figure and does not name the 41.5 Mn gap to the filed consolidated quarter. Not material to any verdict input.", source_fidelity: false}
critical_count: 0
major_count: 1
minor_count: 2
false_positives_struck: 3
material_universe: 900
acceptance_rate: 99.3
coverage_note: "Mandatory tier 78 of 78 checked: every Gate 0 scorecard input (Sales x6, PBT x6, Interest x6, PAT x6, CFO x6, Capex x6, Net worth x6, EBITDA x3, current liabilities x6, total assets x6, receivables/inventory/payables FY21 and FY26 x6, FY26 borrowings, cash, other income, current assets, net block x5, selling-and-admin x2, R&D NIL, promoter 55.84% and 64.84%, pledge flag, contingent-liability lines x4). All tie to screener-Data_Sheet.csv, AR2026 pp.123/191/193/232/242, AR2025, Prospectus pp.71/73/92, Q2 FY27 results pp.6/10/11, Q4 FY26 results p.13 and the shareholding XBRL. No verdict-card or Section 1B pillar inputs exist in stages 1 to 9 (stages 11 and 13 have not run), so none were in scope. Sample tier: about 900 material numbers counted (headline financials, ratios, balance sheet and cash flow lines, QIP, customer, guidance, peer, market and ownership figures; decided by whether the number feeds a flag, score or verdict); about 322 checked beyond the mandatory tier across B02, B03, B04, B05, B06, B07, B08, B09 plus pass 1 lines 1 to 60. NOT checked: most of 02-notes-pass1 beyond line 60 and 02-notes-pass2; 03 board/compensation tables beyond attendance, DIN and pay samples; 06-peers peer-concall figures beyond about a dozen spot checks (MTAR WC days, advances, fungible units, order book); 07-emoat narrative items; 08 web-sourced (MEDIA) items such as the 31,67,702 share block sale price, bulk-deal values and the GE Vernova 8-K, Howmet, Siemens Energy, MHI, Baker Hughes figures in 09, which live outside the PDF corpus and cannot be source-checked here. Rule 5b: three candidate rows struck (FY26 EBITDA 225.32 vs four-quarter sum 225.31 is a 0.01 rounding of a matched figure; H1 revenue 3,635.4 vs 3,635.34 is formatting; the 37.4% 'FY21-25' standalone CAGR label is a faithfully transcribed deck anomaly, the computed 37.4% FY21-FY26 is right). Loose anchors disclosed by the stage itself and not re-rated: 02-notes P3-7 '[page 120-area ...]' (no number attached; consolidated going-concern policy is on p.196)."
```
