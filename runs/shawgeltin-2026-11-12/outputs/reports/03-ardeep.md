# Stage 3: Annual Report Deep Dive (backward read), Narmada Gelatines Ltd (SHAWGELTIN)

Run date 2026-11-12. Model claude-sonnet-5-5. Source: NGL Annual Report FY2025-26 (65th AGM), scanned image PDF, OCR text beside it.
Units: the AR and the results filings print Rs LAKH; screener and CARE print Rs crore. Nothing is converted silently; "(= Rs X Cr)" marks a computed conversion.
Anchors: "p.N" = PDF page of the AR. Printed page = PDF page minus 3. Load-bearing numbers were checked against the page image (PDF pp.12, 20, 50, 51).
Labels: [COMPUTED] arithmetic on printed figures. [INFERENCE] reasoning beyond the printed text. Filed text outranks inference.

## 0. Verification of the four load-bearing facts (first priority)

### Fact 1. Margin reset split, FY25 13% to FY26 19%
Confirmed. Operating profit before other income: FY26 4,130.63 lakh = 19.18% of revenue 21,541.15; FY25 2,457.99 lakh = 13.01% of 18,892.07 [COMPUTED from P&L, p.50]. Screener shows 13% and 19% (screener standalone P&L).

| Line, % of revenue | FY26 | FY25 | Move | Anchor |
|---|---|---|---|---|
| Materials consumed plus inventory change | 53.03% (11,423.41) | 58.14% (10,983.41) | -511 bp | Notes 28, 29, p.68-69 |
| Power and fuel | 10.83% (2,333.26) | 13.00% (2,455.65) | -217 bp | P&L p.50 |
| Employee benefits | 9.32% (2,007.70) | 8.57% (1,618.21) | +75 bp | Note 30, p.69 |
| Other expenses | 7.64% (1,646.15) | 7.29% (1,376.81) | +35 bp | Note 33, p.69 |
| Operating margin | 19.18% | 13.01% | +617 bp | computed |

What the AR says drove it (MD&A, PDF p.12, image checked):
- Gelatine volume +16.17%, average selling price -5.20%. DCP volume +11.35%, average selling price +17.17%.
- Mix of turnover: gelatine 70.77%, DCP 29.15% (computed from Note 26: 70.62% and 29.08%).
- Power and fuel -4.98% "due to decrease in the coal prices and consumption" (ties: 2,333.26 vs 2,455.65 = -4.98%).
- Profit "led by better yield and lower consumption of power and fuel". No yield percentage, tonnage, capacity utilisation or raw-material price is given anywhere in the AR.
- Annexure III (p.19): UF plant replaced the old evaporator to save steam and electricity; solar plant commissioned, capital investment Rs 8.89 Crores. The MD&A does not credit solar or the UF plant for the power saving.

Price and volume bridge [COMPUTED from MD&A rates and Note 26]:
| Item | Lakh | Basis |
|---|---|---|
| DCP price effect | +918 | 6,264.24 less 6,264.24/1.1717 |
| Gelatine price effect | -834 | 15,212.47 less 15,212.47/0.948 |
| Net price effect | about +84 | 0.4% of revenue |
| PBT rise FY25 to FY26 | +1,540 | 3,819.16 less 2,278.96 |
| Gelatine revenue not explained by the printed volume and price rates | about -237 | actual +8.44%; rates imply +10.13% |
| DCP revenue vs rates | ties within 0.2% | +30.25% actual vs +30.47% implied |

Reading: net price is close to flat. The reset is cost-led plus volume leverage, not price-led.

Test against the industry (Note 39B, p.74, IGCL, a group-controlled competitor) [COMPUTED]:
| Ratio to income | NGL change | IGCL change | Reading |
|---|---|---|---|
| Materials plus inventory change | -511 bp | -727 bp (47.07% to 39.80%) | Same direction, IGCL larger: points to an industry cost effect [INFERENCE] |
| Power and fuel | -217 bp | +87 bp (13.51% to 14.38%) | Opposite: points to an NGL-specific cause such as solar [INFERENCE] |
| Employee | +75 bp | -149 bp | Opposite |
| Pre-tax margin | 11.96% to 17.67% | 10.98% to 18.30% | Both up 6 to 7 points |
IGCL total income fell 13.6% (20,619.59 to 17,819.38) while NGL revenue rose 14.0%. IGCL is promoter-group controlled, so it is not an independent control.

Most evidenced path: the largest reset line (materials) is at least partly an industry effect; the power-and-fuel line is company-specific. Two readings: (A) structural, group know-how, solar, yield; (B) cyclical, bone and global gelatine price deflation (MD&A p.11: "price of Raw Material globally reduced significantly during the second half"). One separating observation: Q2 FY27 materials-plus-inventory ratio at or under 52% while IGCL's does not rebound.

Quarterly persistence (results filings, Rs lakh, standalone; FY26 quarters from Q3 FY26 and Q1 FY27 results tables, derived by difference where noted):
| Quarter | Revenue | Materials + inv chg % | Power and fuel % | Employee % | Other % | Operating margin |
|---|---|---|---|---|---|---|
| Q4 FY25 (derived) | 4,977 | 56.0% | 11.4% | 8.5% | 9.1% | 15.03% |
| Q1 FY26 | 4,577 | 52.6% | 12.7% | 9.7% | 8.5% | 16.43% |
| Q2 FY26 | 5,121 | 53.2% | 12.2% | 9.7% | 6.6% | 18.26% |
| Q3 FY26 | 5,673 | 52.5% | 10.1% | 10.5% | 8.1% | 18.81% |
| Q4 FY26 | 6,170 | 53.7% | 8.9% | 7.7% | 7.4% | 22.30% |
| Q1 FY27 | 5,637 | 50.6% | 11.9% | 9.1% | 7.6% | 20.79% |
Q4 FY26 power and fuel (8.9%) was the low point; Q1 FY27 returned to 11.9%, so part of the 22.3% peak was not repeatable. Q1 FY27 vs Q1 FY26: operating margin +436 bp, from materials +200 bp, power and fuel +80 bp, employee +60 bp, other +90 bp. Q2 FY27 is not filed (due 12-Nov-2026).

Labour Code: found. Q3 FY26 results note 4 (results PDF p.4): incremental liability Rs 82.56 lakh recognised in employee expense for the nine months to 31-Dec-2025. That is 21% of the 389.49 lakh employee-cost rise. Normalised FY26 operating margin = 19.56% [COMPUTED]. Employee cost per quarter was 443, 496, 594 (incl 82.56), 475, then 511 (Q1 FY27): the rise is run-rate, from about 400 a quarter in FY25 to about 500 [COMPUTED from 9M FY25 1,194 and FY25 1,618].

### Fact 2. Pioneer Jellice flows and the IGCL 14.14% stake
Confirmed from Note 37 (p.73), Note 39 (p.74), AOC-1 (p.21), Note 17a (p.64). Detail in Phase 2B and 5. Pioneer Jellice holds 40.06% (2,423,321 shares), promoter, no change. Flows 1,517.52 lakh = 7.04% of revenue. IGCL stake: 1,003,000 shares at cost 4,115.31 lakh (= Rs 410.3 a share) [COMPUTED], share of IGCL net worth 2,737.02, cost 1.50x. Who benefits: NGL and its promoters together hold more than 20% of IGCL (Board's Report p.6); the AR gives no valuation basis. NOT FOUND: pricing method for Pioneer Jellice, IGCL market value, nature of the "raw material" bought.

### Fact 3. Capex Rs 33 Cr, term loan, Jan-2027
NOT FOUND in the Board's Report (pp.5-10), MD&A (pp.11-12), Annexures (pp.13-21) or Corporate Governance Report. Searches for expansion, capacity, commissioning, capex and outlook return nothing beyond the Annexure III solar line. The plan exists only in the CARE press release of 06-Mar-2026 (announcements file): Rs 33.00 crore over two years, Rs 25 crore term loan, +600 MT gelatine, +1,500 MT DCP, commercial production from Jan 2027.
What the AR notes show [COMPUTED]:
| Item | Lakh | Anchor |
|---|---|---|
| CWIP, all under one year, "no cost overrun / time delay in the project" | 528.97 (FY25 678.29) | Note 4, p.61 |
| Intangibles under development | 24.50 | Note 5, p.62 |
| Capital commitments net of advances | 1,194.06 (gross 1,205.00) | Note 35, p.72 |
| CWIP plus net commitments | 1,723.03 = Rs 17.2 Cr = 52% of Rs 33 Cr | computed |
| Not yet spent or contracted if scope is Rs 33 Cr | about 1,577 | computed |
| Gross block additions FY26 | 1,096.52, of which plant 1,007.61 | Note 3, p.61 |
| Solar plant capital investment (Annexure III) | 889 | p.19 |
| Term loan outstanding | 728.65 at 7.95% to 8.20%; current maturity 320.56 | Note 18, p.65 |
| Implied FY26 draw | about 125.57 (728.65 less 603.08), netted in the short-term line of the cash flow | computed, p.51 |
Most of FY26 additions look like the solar plant; the expansion CWIP is therefore about 5.3 Cr at March 2026. The Q1 FY27 filing shows P&L only, so progress since March is NOT FOUND. CARO ix(c) says the term loan was applied for its purpose (p.46). Covenants NOT FOUND.

### Fact 4. Cash conversion and payout
CFO 2,455.67 vs PAT 2,843.82 = 86.4% (FY25 99.0%) (cash flow p.51). Detail in Phase 3A. Inventory 156 days holds on materials cost only (see Phase 2E). Dividend record: FY26 Rs 10 paid (604.96 lakh) and Rs 11 recommended (665.45 lakh); FY23 Rs 100 a share = 6,049.59 lakh, "Interim Dividend and Final Dividend paid", against PAT of about Rs 15 Cr (screener) (AR p.37). Screener: FY23 reserves 139 to 88 Rs Cr, investments 48 to 4, investing inflow +44, financing outflow -67. The board that paid it was replaced on 14-Jul-2023 (new directors' dates, p.42). The payout was funded by selling the investment book [INFERENCE from screener rows]. Cumulative FY15-FY26 dividends are about 70% of cumulative PAT, about 36% without FY23 [COMPUTED from screener payout % and PAT, rounded Rs Cr].

## PHASE 1: AUDITOR'S REPORT AND CARO

### 1A Core opinion
Unmodified. Standalone (p.43): statements "give a true and fair view in conformity with the Indian Accounting Standards". Consolidated (p.81): "true and fair view"; the text does not name Ind AS (minor). Going concern: no material-uncertainty paragraph; management and auditor use responsibility language only (p.43, p.44); CARO xix says nothing indicates the company cannot meet liabilities falling due within one year (p.47). Directors' Report: "no significant and material orders ... impacting the going concern status" (p.9).

### 1B Key audit matters
| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| None | "We have determined that there are no key audit matters to communicate" (standalone p.43) | n/a | YELLOW: silence is allowed, but the IGCL carrying value (29.1% of equity), related-party purchases and revenue cut-off were candidates |
| Consolidated report | no KAM section at all (p.81) | n/a | YELLOW |

### 1C Emphasis of Matter and Other Matters
No Emphasis of Matter. Other Matter (consolidated, p.82): share of associate profit 354.93 lakh and total comprehensive income 362.11 lakh audited by another auditor; the AR does not name that auditor (NOT FOUND). Difference 7.18 = 14.14% of 50.83, which supports the Note 39B reading that 50.83 is IGCL other comprehensive income [INFERENCE].

### 1D CARO 2020 clause by clause (standalone, pp.45-47)
| Clause | Finding | Risk |
|---|---|---|
| i | Records proper; phased verification, no material discrepancy; titles in company name; no revaluation | GREEN |
| ii(a) | Inventory verified, no 10% discrepancy | GREEN |
| ii(b) | Quarterly bank statements agree with books | GREEN |
| iii | No loans, guarantees or security given; investment "not prejudicial" | GREEN |
| iv | Sections 185 and 186 complied | GREEN |
| v, vi | No deposits; cost records not prescribed | GREEN |
| vii(a) | Regular in statutory dues; none over 6 months | GREEN |
| vii(b) | Disputed: excise 240.88 lakh (2000-03, High Court Jabalpur); MP VAT 3.76 (2012-13, Deputy Commissioner); income tax 7.85 (AY 2013-14, Commissioner Appeals) | YELLOW: excise dispute is 23 years old, stage not stated |
| viii | No undisclosed income surrendered | GREEN |
| ix(a), (b), (d) | No default, no wilful defaulter, no short-term funds used long | GREEN |
| ix(c) | Term loan applied for purpose | GREEN |
| ix(e), (f) | Text says "the provisions ... is applicable" where "not applicable" is meant (p.47) | drafting slip |
| x | No IPO or preferential issue | GREEN |
| xi | No fraud; no ADT-4; no whistle-blower complaint | GREEN |
| xiii | Related parties comply with Sections 177 and 188 | GREEN |
| xiv, xv | Internal audit commensurate; no non-cash transactions | GREEN |
| xvii | No cash losses current or preceding year | GREEN |
| xix | No material uncertainty on liabilities due within one year | GREEN |
| xx | No unspent CSR | GREEN |

### 1E Auditor continuity
Lodha & Co LLP, Mumbai, partner R. P. Baradiya (UDIN 26044101UXBXOP3319). Appointed at the 61st AGM for five years to the 66th AGM in 2027 (Board's Report p.9); FY26 is year four, so rotation falls at the 2027 AGM. The firm was kept after the June 2023 ownership change. Fees (Note 33, p.69-70): statutory audit including limited reviews 7.50 (FY25 4.00, +87.5%), tax audit 1.50, other certification nil (0.07), out-of-pocket 1.56; total 10.55 (6.17). Non-audit to audit ratio: 0 (FY25 0.07 of 4.00). Fee revision approved at the 64th AGM (p.9).

### 1F Standalone vs consolidated
The consolidated statements add one associate (IGCL, audited by another auditor). Differences: associate carried at 4,509.26 consolidated vs 4,115.31 standalone (consol p.85); consolidated tax equals standalone, associate profit treated as tax-free; CARO consolidated clause cites no adverse remark in either set (p.83). Consolidated FY25 cash flow does not foot (see Phase 2 item 7).

Phase 1 verdict: GREEN. Kill switch (informational): based on phases so far, a human reviewer would not have reason to stop, because the opinion is unmodified, CARO has no adverse remark, and no fraud, default or going-concern language appears.

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

### Verification of the triple-pass Top 15 (all checked against the AR text and, for key rows, the images)
| Rank | Triple-pass claim | AR check | Mark |
|---|---|---|---|
| 1 | IGCL at cost 4,115.31; 29.1% of equity; 1,378.29 above 2,737.02 | 4,115.31/14,130.66 = 29.12%; 4,115.31 less 2,737.02 = 1,378.29 (Note 6 p.62; AOC-1 p.21; Note 39 p.74) | verified |
| 2 | Pioneer Jellice 1,481.92 = 12.7% of purchases; 24.00; 11.60; 1,517.52 = 7.04% | 1,481.92/11,669.25 = 12.70%; total/21,541.15 = 7.04%; rent share 11.60/11.89 = 97.6% (Notes 37, 28, 33) | verified |
| 3 | Margin lines -511, -217, +75, +35 bp; only driver coal | Lines verified (Section 0). MD&A p.12 also gives volume, price, yield, raw-material claims | verified, with discrepancy (see block) |
| 4 | Staff welfare 715.25 vs 53.43; absences 1.41 to 36.97 | verified Note 30 p.69, Note 34 p.72. Labour Code amount found elsewhere: 82.56 lakh (Q3 FY26 results note 4) | verified, with discrepancy |
| 5 | CFO/PAT 86.4% (99.0%); payables 483.31 | 2,455.67/2,843.82; 1,704.25/1,720.94 (p.51) | verified |
| 6 | Inventory 156 days; RM +47.8%; Note 48 says 72 | 4,879.49/11,423.41 x 365 = 155.9; RM 1,265.65 vs 856.24 = +47.8%; FG 1,619.81 vs 1,895.74 = -14.6% (Notes 10, 29, 48) | verified, basis clarified |
| 7 | Consolidated FY25 cash flow off by 96.89; receivables line 163.22 above standalone | consol CFO 1,607.85 vs standalone 1,704.25 (diff 96.40); receivables (361.41) vs (198.19) (consol p.87, p.51) | verified |
| 8 | Note 39B "TCI 50.83" probably OCI | printed as TCI 50.83 / 75.17 against OCI "-" (p.74); auditor's 362.11 less 354.93 = 7.18 = 14.14% x 50.83 (p.82) | verified, inference strengthened |
| 9 | Receivables +16.9%; overdue 13.4% (23.1%); ECL 2.81; write-offs 46.44 vs 3.99 | 2,902.73/2,484.20; overdue 388.08/2,902.73; Notes 11, 43, 33 (pp.62-63, 76, 69) | verified |
| 10 | Gross debt 789.08; net 380.60; draw about 125.57 | 408.09 + 380.99; 789.08 less 408.48; 728.65 less 603.08 (Notes 18, 21, 44) | verified |
| 11 | CWIP 528.97; commitments 1,205.00; 1,747.53 | 528.97 + 1,194.06 + 24.50 (Notes 3-5, 35) | verified |
| 12 | Note 48 DSCR 7.71 on mixed bases; variance 100% | (4,123.93 + 101.87 + 287.11)/(101.87 + 483.13) = 7.71 uses consolidated PBT and short-term repayments; debt-equity 0.056 vs 0.107 is -47% not 100% (Note 48 p.79) | verified |
| 13 | Gratuity funded 69%; losses 86.13, 44.36; rate gain 31.88 | 320.67/463.47 = 69.2%; Note 34 pp.70-71 | verified |
| 14 | Contingent 244.64 = 1.73% of net worth | 244.64/14,130.66; CARO vii(b) lists the same excise item (Note 36 p.72; p.46) | verified |
| 15 | No policy change; EPS 47.01; Rs 10 paid, Rs 11 proposed | Note 2(i) p.53; Note 38 p.73; Note 44(c) p.78 | verified |
Result: 15 of 15 verified; three carry a discrepancy or a clarification (ranks 3, 4, 6), listed in the block. Reconciliation with the triple-pass score of 7/10: my accounting component is 6.5 because the front sections add contradictions that the notes stage did not read (below).

### New findings outside the triple-pass (front sections vs notes)
| Item | Printed | Check | Anchor |
|---|---|---|---|
| MD&A on materials | "Material consumed ... increased by 1.29%" | Note 28: 11,407.13 to 11,259.84 = -1.29% | p.12 vs p.68 |
| EBITDA | 40.88 Cr (FY25 26.23 Cr); growth 55.81% (Board's Report) and 59.58% (MD&A) | FY26 operating profit 4,130.63 plus other income 77.51 = 4,208.14 (42.08 Cr); FY25 same basis 26.23 ties; implied growth 60.4% | p.5, p.12, p.50 |
| Other expenses | 8.94% of revenue | 1,646.15/21,541.15 = 7.64% | p.12 vs p.69 |
| Employee cost | 9.26% | 9.32% | p.12 vs p.69 |
| MD remuneration | +10.41% (Annexure IV) | Note 37: 66.26 to 99.16 lakh = +49.7% | p.20 vs p.73 |
| Total KMP remuneration | +4.52% | 87.12 to 125.35 lakh = +43.9% | p.20 vs p.73 |
| MD pay revision date | "13th August 2026" | board met 13-Aug-2025; the NRC met 13.08.2025; date is a typo | p.30, p.29 |
| MD&A on imports of raw material | "being utilized to import/purchase raw material" | Annexure III foreign-exchange outgo has no raw-material line; imports through traders NOT FOUND | p.11 vs p.19 |

### 2A Accounting policy aggressiveness
| Area | Policy | View |
|---|---|---|
| Revenue | Control passes at dispatch or delivery; net of rebates; export incentives on sale of licence; duty drawback on receipt (pp.54-55) | Standard; GREEN |
| Depreciation | Straight line; plant 5 to 25 years vs Schedule II 5 to 30; assets up to Rs 75,000 expensed fully (p.54) | Conservative or neutral |
| Inventory | Lower of cost and NRV, weighted average; provision "where necessary", no amounts (p.54) | Unevidenced |
| Capitalisation | Borrowing costs capitalised on qualifying assets (p.60); finance cost 101.87 equals cash paid, so none capitalised | Conservative |
| Impairment, ECL | Provision matrix unpublished; ECL 2.81 lakh static two years | Token (YELLOW) |
| Leases | Note 2(xv) says no lease contracts, yet Note 37 shows lease rent 11.60 to Pioneer Jellice | Inconsistent (YELLOW) |
| Policy change | None; "consistent with the previous year" (p.53) | GREEN |
Verdict on aggressiveness: not aggressive; the weakness is disclosure.

### 2B RPT map
| Counterparty | FY26 | FY25 | % of revenue | Note |
|---|---|---|---|---|
| Pioneer Jellice, raw material incl GST | 1,481.92 | 1,524.64 | 6.88% | 12.7% of purchases, upper bound because of GST |
| Pioneer Jellice, technical consultancy | 24.00 | nil | 0.11% | new |
| Pioneer Jellice, lease rent | 11.60 | nil | 0.05% | new; 97.6% of all rent |
| Pioneer Jellice, sales commission | nil | 6.72 | 0 | dropped |
| Pioneer Jellice payable | 83.53 | 99.21 | | about 21 days of purchases |
| Total Pioneer Jellice flows | 1,517.52 | | 7.04% | |
| MD remuneration | 99.16 | 66.26 | | |
| KMP total | 125.35 | 87.12 | | |
| Sitting fees | 9.70 | 8.66 | | ties to Note 33 |
| IGCL dividend received | 50.15 | nil | | absent from the RPT table |
Value-extraction signals: no loans, guarantees or advances to related parties (CARO iii); no sales to promoter entities shown; two new Pioneer Jellice lines with no tenure or pricing; arm's length asserted only (p.73; Board's Report p.8). AOC-2 is said to be "set out in the Notes" but the Notes hold no AOC-2 terms.

### 2C Contingent liabilities
244.64 lakh = 1.73% of net worth 14,130.66 and 8.6% of PAT 2,843.82 [COMPUTED]; below the 25% and 100% flags. Excise 240.88 (2000-03), sales tax 3.76; land revenue cess 14.14 removed without reason (Note 36 p.72). Income tax 7.85 lakh is not shown as contingent (management confident). Capital commitments 1,205.00 are a larger obligation (8.5% of net worth).

### 2D Receivables
2,902.73 lakh (+16.9% vs revenue +14.0%); 49.2 days on closing balance [COMPUTED]. Not due 2,514.65 (86.6%); under 6 months 359.45; 6 to 12 months 28.63 (FY25 2.03); over 1 year nil; credit impaired 2.81 in the over-3-years bucket (Note 11 p.63). Overdue share 13.4% vs 23.1%. Concentration: AR says "low" with no percentage (p.76); CARE gives top 10 at about 42%. Credit period 30 to 120 days (p.76). Unbilled: none shown. Write-offs 46.44 lakh bypassed the ECL allowance; nature NOT FOUND. The gap between the FY26 receivables rise and write-offs is a lead, not a finding.

### 2E Inventory
4,879.49 lakh: raw materials 1,265.65 (+47.8%, 41.0 days vs 27.4), WIP 1,589.97 (FY25 1,477.61; Note 10's FY25 OCR "177.61" does not sum, Note 29 and the total confirm 1,477.61), finished goods 1,619.81 (-14.6%), stores 404.05 (p.62, p.69). Days: 155.9 on materials cost, 82.7 on sales, 102.0 on total operating cost [COMPUTED]. The raw-material build matches the MD&A statement that raw material is being bought while cheap. Finished goods fell while sales grew: inventory change cost +163.57 vs -423.72 in FY25. No write-down or NRV amount disclosed.

### 2F Borrowings
Gross 789.08: term loan 728.65 (first charge on assets created; 60 monthly instalments; 7.95% to 8.20%), cash credit 60.43 (limit Rs 20 Cr per CARE, rate 7.70% to 8.15%), overdraft nil (Notes 18, 21 pp.65-66). Maturity ladder: 320.56 in year 2, 195.00, 171.87, 41.22 (p.65); current maturity 320.56 sits in current borrowings. Wall: 41% of term loan falls in the first year; at CFO 2,455.67 it is covered 7.7 times. Covenants, rate type (fixed or floating) and sanction amount NOT FOUND; Note 44(a) mentions covenants only generically. Pledge: NOT FOUND IN DOCUMENT. ICDs given: nil.

### 2G Deferred tax
DTL 508.17 (FY25 409.89), almost all accelerated depreciation (534.08). Tax reconciliation: enacted 25.17%; expense 969.08 on PBT 3,819.16 = 25.37% (Note 20 p.66). Tax adjustment for earlier years 6.26 and interest on income tax 13.67 in finance cost.

### 2H Exceptional items, ESOP, leases, post balance sheet
No exceptional items in FY26 or FY25 (p.50). No goodwill. No ESOP or dilution; EPS basic equals diluted 47.01 (p.73). No post-balance-sheet event other than the Rs 11 dividend (p.78); Board's Report: no material changes (p.10). Labour Codes: impact "accounted" with no amount in the AR (p.78); 82.56 lakh in Q3 results. Note 50: prior-year figures regrouped with no amounts (p.80), consistent with the staff welfare versus salaries swing (715.25 vs 53.43; 1,147.35 vs 1,360.72). R&D: Note 41 15.29 vs Note 33 20.18 vs Annexure III 15.29 (p.19, p.69, p.74).

Phase 2 verdict: YELLOW. Cross-reference with Phase 1: the absence of any KAM sits oddly beside an associate premium with no test and two new related-party lines. Kill switch (informational): a human reviewer would not have reason to stop, because no policy change, no exceptional item and no red item exist; the reviewer would require the IGCL valuation basis before sizing.

## PHASE 3: FINANCIAL STATEMENTS

### 3A Cash flow (standalone, p.51, Rs lakh)
| Item | FY26 | FY25 |
|---|---|---|
| PBT | 3,819.16 | 2,278.96 |
| Operating profit before working capital | 4,123.44 | 2,384.86 |
| Working capital change | (846.85) | (126.62) |
| of which receivables | (463.80) | (198.19) |
| of which inventories | (222.12) | (6.94) |
| of which payables | (483.31) | +254.07 |
| Cash from operations | 3,276.57 | 2,258.24 |
| Taxes paid | (820.90) | (553.99) |
| CFO | 2,455.67 | 1,704.25 |
| CFO / PAT | 86.4% | 99.0% |
| CFO / operating profit (post-tax) | 59.5% | 69.3% |
| CFO pre-tax / operating profit (screener basis) | 79.3% | 91.9% |
| Capex (incl CWIP and advances) | (971.71) | (1,470.01) |
| FCF | 1,483.96 | 234.24 |
| Capex / depreciation | 3.38x | 6.61x |
| Investments bought | nil | (4,115.31) |
| Investments sold | nil | 960.48 |
| Bank deposits placed or released | (370.80) | +1,529.03 |
| Dividend paid | (604.96) | (604.96) |
| Debt repaid (long term and short term) | (483.13) | net draw +1,272.20 |
| Cash and equivalents, year end | 11.32 | 19.03 |
Cash plus bank balances: about 2,217 at March 2024 [COMPUTED from 661.74 and 26.36 + 1,529.03], 45.39 at March 2025, 408.48 at March 2026. The IGCL purchase and capex used the stored cash in FY25.
CFO quality checks [COMPUTED]:
- One-time inflators: customer advances rose 135.18 (112.37 to 247.55, Note 23 p.67) and the working-capital line includes the unpaid capex payable of 53.07 (arithmetic inference). Removing both: CFO about 2,267 = 79.7% of PAT, FCF about 1,431.
- Payables stretching: the opposite. MSME payables fell 951.86 to 477.18; payable days 56 to 39 (screener). FY25 payables looked stretched; FY26 normalised.
- Inventory rundown: none; inventory built 222.12.
- Interest classification: finance cost in financing; interest and dividend received in investing. Fine.
- Presentation slip: the actuarial loss (52.46) is deducted from PBT although it never passed through PBT; the provision rise offsets it, so CFO is not misstated.
- History (screener, Rs Cr): 12-year CFO 122 vs PAT 156 = 0.78; FY24-FY26 57 vs 60 = 0.95. CFO/PAT was below 0.7 in FY15, FY20, FY21, FY22.

### 3B Balance sheet (p.49, Rs lakh)
Assets 17,497.05: PPE 4,107.03, CWIP 528.97, intangibles under development 24.50, investment in associate 4,115.31, loans and other financial 184.88, tax and other 32.63; inventories 4,879.49, receivables 2,902.73, cash 11.32, bank balances 397.16, other current 314.03. Equity 14,130.66; non-current liabilities 999.00 (borrowings 408.09, provisions 82.74, DTL 508.17); current 2,367.39 (borrowings 380.99, payables 1,235.40, other financial 344.50, other 217.91, provisions 127.74, tax 60.85). Check: 14,130.66 + 999.00 + 2,367.39 = 17,497.05. Associate is 23.5% of assets; inventory plus receivables 44.5%.

| Ratio | FY26 | FY25 |
|---|---|---|
| Debt / equity (gross) | 0.056 | 0.107 |
| Net debt / operating profit | 0.09x | 0.50x |
| Current ratio | 3.59 | 2.55 |
| Quick ratio | 1.53 | 0.98 |
| Interest cover (PBT + finance cost) / finance cost | 38.5x | 19.7x |
| ROCE (EBIT / average equity plus debt) | 27.9% | NOT FOUND (FY24 balances not in AR) |
| ROCE operating, excluding associate and cash (year-end base) | 37.0% | 24.7% |
| ROE (average equity) | 21.8% | 15.1% (Note 48) |
| Goodwill / net worth | nil | nil |
Per Amendment 17 the spot-year ROCE is informational only; it is not an input for converter treatment.
DuPont FY26 [COMPUTED]: net margin 13.2% x asset turnover 1.29x x equity multiplier 1.28x = ROE 21.8%. Note 48 shows net margin 13.15% vs 9.03%; turnover and leverage barely moved (leverage fell), so ROE is operational, not leverage-driven.

### 3C P&L (p.50)
| Line | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue | 21,541.15 | 18,892.07 | +14.0% |
| Other income | 77.51 | 165.25 | -53.1% |
| Materials consumed | 11,259.84 | 11,407.13 | -1.3% |
| Inventory change | 163.57 | (423.72) | swing +587.29 |
| Employee | 2,007.70 | 1,618.21 | +24.1% |
| Power and fuel | 2,333.26 | 2,455.65 | -5.0% |
| Other expenses | 1,646.15 | 1,376.81 | +19.6% |
| Depreciation | 287.11 | 222.23 | +29.2% |
| Finance cost | 101.87 | 122.05 | -16.5% |
| PBT | 3,819.16 | 2,278.96 | +67.6% |
| Tax | 975.34 | 558.01 | +74.8% |
| PAT | 2,843.82 | 1,720.94 | +65.2% |
Margin waterfall, % of revenue: gross margin after materials 46.97; less employee 9.32, power and fuel 10.83, other 7.64 = operating margin 19.18; less depreciation 1.33, finance cost 0.47, plus other income 0.36 = PBT 17.73; tax 4.53; PAT 13.20.
Other income is 2.0% of PBT (FY25 7.3%), below the 20% flag; 50.15 of it (65%) is the IGCL dividend and 20.30 interest. Exceptional items: none, FY26 and FY25 (FY24 NOT FOUND in AR). Tax: 25.37% effective vs 25.17% enacted. EPS basic equals diluted 47.01 (FY25 28.45).

Phase 3 verdict: YELLOW (FLAG-CASH, mild). Cross-reference: Phase 2 note 22 and Note 30 explain the cash gap and the cost step; Phase 4 supplies no explanation for either. Kill switch (informational): a human reviewer would not have reason to stop, because CFO is positive and 86% of PAT with net debt near nil; the reviewer would want H1 FY27 CFO/PAT at or above 90% before treating the profit as cash.

## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks
The AR has no risk-factor section. Disclosed: vegan and plant-based substitutes (MD&A p.11, real but generic); Risk Management Committee described (p.6, p.32) with the promise that "key business risks identified and mitigation plans are set out in the Corporate Governance Report", but the report lists none; Note 43 (p.76-77) names credit, liquidity, interest rate, foreign exchange and commodity risk; the commodity paragraph names crushed bone, HCl, lime and coal and states "Demand and supply are external factors on which company has no control". The cautionary statement lists raw material availability, imports and exports, taxation and natural calamities (p.12). All are boilerplate; the commodity risk is real but unquantified.

### 4B Missing risks
| Missing risk | Evidence | Likely reason for omission |
|---|---|---|
| Bone price and sourcing: 511 bp of margin | Note 28 p.68; Note 43(V) p.77 | Reset looks better if cause is credited to management |
| One site | Note 1 p.53; plant location p.39 | Habit |
| Capex execution and funding | Notes 4, 18, 35; MD&A silent | Capex not announced in the AR; CARE announced it |
| Pioneer Jellice dependency | Note 37 | Treated as arm's length |
| IGCL capital and conflict | Notes 6, 39 | Treated as investment |
| Customer concentration | Note 43 says low; CARE says top 10 about 42% | Ind AS 108 customer disclosure absent |
| DCP price reversal, gelatine price fall | MD&A p.12 | Reported as results, not as risk |
| Key person and succession | AGM notice p.128, p.130 | Not raised |
| ERP go-live | Annexure III p.19 | Positive framing |
| Effluent and pollution | Note 33 p.69 | Routine |

### 4C MD&A deep dive
- Industry claims: global market USD 3.40 bn (2025) to USD 6.58 bn by 2034 at 7.83% (arithmetic from 3.60 in 2026 ties); India about 7.5%; no source, no base (p.11). Company 10-year sales CAGR 5%, five-year 10% (screener).
- Growth and margin explanations: volume growth credited to the company; coal price credited to external factors; "better yield" credited to the company without data. Price and volume are reported honestly (gelatine price down 5.20%).
- Blame and credit: the 1.29% materials line is mis-stated in direction and attributed to "lower cost of Raw material". Net, the MD&A credits external factors for costs and internal factors for yield.
- Segment: one segment under Ind AS 108 (p.11, Note 45 p.78); product split only in Note 26.
- Outlook: the section titled "Outlook" gives no company outlook; PLI schemes and pharma exports (+2% in FY26) are cited with no link to NGL.
- Exports: FOB 214.93 lakh vs 47.99, about 1.0% of revenue (p.19); CARE credits "improved access to export markets", but the AR shows exports at 1%.

Forward guidance table: see block (`guidance_table`); no company numbers exist. The credibility check against history: only industry growth claims, which exceed the company's own 10-year record.

### 4D Tone and credibility (1 to 5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | No capex, tonnage, yield, utilisation, covenants or margin split; Ratio notes wrong |
| Consistency | 2 | MD&A vs Note 28, EBITDA, Annexure IV vs Note 37, other expenses 8.94% vs 7.64% |
| Specificity | 2 | "Better yield", "optimum capacity utilization" with no metric; price and volume rates are specific |
| Accountability | 3 | Price decline stated plainly; costs credited to coal; no admission of cyclical help |
| Capital allocation sense | 3 | Retains 77% of profit, near debt-free, but 4,115.31 lakh parked in a promoter-group associate and expansion unannounced |

Phase 4 verdict: YELLOW. Contradictions with Phases 1-3: MD&A direction error on materials; MD&A silence on capex and solar; Note 48 reasons call for explanation of debt-equity and DSCR variances but print none. Kill switch (informational): a human reviewer would not have reason to stop, because the numbers are in the audited statements; the reviewer would stop to ask management for the margin decomposition and the capex timetable.

## PHASE 5: CORPORATE GOVERNANCE AND BOARD

### 5A Board (pp.24-25, 42)
| Director | Category | Since | Board attendance | Public-company seats | Note |
|---|---|---|---|---|---|
| S Annamalai | Chairman, non-executive, promoter side | 14-Jul-2023 | 6/6 | 5 | Brother of Maheswaran |
| S Maheswaran | Non-executive, promoter side | 14-Jul-2023 | 5/6 = 83% (table prints 80%) | 3 | Age 77; sits on about 20 boards including Pioneer Jellice and IGCL |
| K Krishnamoorthy | Independent | 21-Sep-2021 | 6/6 | 1 | Age 75; second term proposed to 2031 |
| B Vijayadurai | Independent, audit chair | 14-Jul-2023 | 6/6 | 2 (NGL and IGCL) | Independent director of IGCL |
| Manimegalai Thangamani | Independent | 14-Jul-2023 | 6/6 | 1 | |
| Ashok K Kapur | Managing Director | 01-Jun-2009 | 6/6 | 1 | Age 78; holds 1,050 shares |
Flags: no independent over 10 years; no attendance below 75%; promoter-group cross-boards (Annamalai and Maheswaran on IGCL; Vijayadurai on IGCL); no one above eight seats on public companies. All non-executive directors attended every Board and committee meeting by video; only the MD attended in person (pp.24, 29, 31, 32). Half the board is independent (3 of 6), as required.

### 5B Committees
Audit (three independents, four meetings, 100%); NRC (two meetings, 100%); Stakeholders (one meeting; two complaints, resolved); CSR (two meetings); Risk Management (one meeting, 20-Mar-2026, chaired by Annamalai, with three plant managers); Complaints Committee. The audit committee chair is an independent director of IGCL, the entity whose carrying value the committee should test.

### 5C Compensation
| Person | FY26 | FY25 | Note |
|---|---|---|---|
| MD Ashok K Kapur | 99.16 | 66.26 | +49.7% [COMPUTED]; Annexure IV prints +10.41% |
| CFO Arun Jaiswal | 20.45 | 0.91 | joined 15-Mar-2025 |
| Company Secretary | 5.74 | 2.93 | joined 07-Aug-2024 |
| Sitting fees, five directors | 9.70 | 8.66 | |
MD pay is 2.6% of PBT and 25.29x the median employee (median 3.92 lakh, +5.38%; 192 permanent employees, p.20). Bonus formula under the 2025 revision: Rs 5 lakh at EBITDA of Rs 20 Cr plus 1% above (p.30), about 26 lakh at FY26 operating profit [COMPUTED]. New term from 1-Jun-2026: fixed gross Rs 73.94 lakh a year, Rs 5 lakh bonus at Operating EBITDA of Rs 25 Cr plus 1% above Rs 25 Cr, 10% annual increment (p.128). The hurdle rises 5 Cr, bonus falls about 5 lakh at FY26 profit [COMPUTED]. Promoter family on payroll: none shown. ESOP: none. Employee cost average 10.5 lakh per permanent employee (2,007.70/192) vs median 3.92 [COMPUTED], consistent with contract labour or other staff inside employee cost; the split is NOT FOUND.

### 5D Shareholding
Promoters 75.00% (4,537,191 shares: Pioneer Jellice 40.06%, Ashok Matches and Timber 34.94%), no change in the year (Note 17a p.64; p.39). Public 21.82%, one institution holding 350 shares (0.01%), no FII line, 7,312 holders after PAN merging (p.39). Pledge: NOT FOUND IN DOCUMENT. The promoter is at 75%, the minimum public shareholding limit, so the promoter cannot add shares without selling down elsewhere. Promoter selling: none. Low institutional ownership is not a risk (Amendment 3). FY23 payout: see Fact 4.

### 5E Governance checklist
| Item | Finding |
|---|---|
| Whistle-blower complaints | None (p.6, p.35) |
| SEBI or exchange action | None in three years (p.34) |
| RPT committee | Audit committee approves RPTs before the transaction (p.34) |
| Auditor fee ratio | Non-audit nil |
| CSR | 40.81 spent vs 40.48 required; excess 0.33 (p.14-15) |
| Section 143(12) fraud | None (p.6, p.47) |
| Material subsidiary auditor | No subsidiary; associate audited by an unnamed other auditor |
| Secretarial audit | No qualification (p.17-18) |
| Postal ballot | Krishnamoorthy continuation beyond 75 passed 99.9998% (p.34) |
| Drafting slips | "13th August 2026" (p.30); Annexure IV percentages; table attendance 80% |

Phase 5 verdict: YELLOW. No pledge or selling pattern, so no FLAG-PROMOTER-PRELIM. Watch: promoter-side cross-holdings, remote oversight, key-person age. Kill switch (informational): a human reviewer would not have reason to stop, because statutory governance is clean; the reviewer would note the audit chair sits on the IGCL board.

## PHASE 6: FRONT MATTER (read last)
No Chairman's letter exists. The opening sections used are the Board's Report (pp.5-10), Financial Highlights (p.3) and MD&A (pp.11-12).

### 6A Narrative vs reality
| Claim | Reality | Mark |
|---|---|---|
| Revenue +14.02% | Note 26: 21,541.15 vs 18,892.07 | ✅ |
| PAT +65.24% | 2,843.82 vs 1,720.94 | ✅ |
| Growth "led by better yield and lower consumption of power and fuel" | Power and fuel -4.98% confirmed; yield has no metric; materials ratio fell at IGCL too | ✅ fuel, ❌ yield unproven |
| "Material consumed ... increased by 1.29%" | Fell 1.29% | ❌ |
| EBITDA 40.88 Cr, +55.81% (Board) and +59.58% (MD&A) | 42.08 Cr, +60.4% | ❌ |
| Other expenses 8.94% | 7.64% | ❌ |
| ISO, EDQM, DNV, Kosher, Halal certificates retained (p.5) | No contrary text | ✅ (unverifiable) |
| Solar plant commissioned (Annexure III) | Depreciation rose 29% and power and fuel fell; MD&A does not credit it | ✅ |
| "no complaint ... no fraud" | CARO xi and p.35 agree | ✅ |
| PE 7.28 vs 11.20 (Annexure IV) | 20,696/2,843.82 = 7.28 | ✅ |

### 6B Strategic priorities
Specific enough: solar, UF plant, SAP. Not specific: capacity, expansion, export, product mix ("improvement in product mix giving better realization", p.19). Capital allocated: Rs 8.89 Cr solar (Annexure III) and 1,723 lakh in CWIP and commitments; not stated as strategy. Execution evidence: power and fuel ratio and Q4 FY26 margin; capex delivery untested.

### 6C Metrics showcased vs absent
Showcased: revenue, PAT, EPS, dividend, net worth, market cap, PE (p.3). Absent: tonnage, utilisation, yield, ROCE, cash flow, capex, order or customer data, export share, raw-material cost per tonne.

### 6D Tone and drift
No prior AR is consumed (the FY2024-25 AR is preserved only), so drift versus prior year is NOT FOUND.

### 6E Quiet abandonment check
| Opening claim | Where it should appear | Class | Materiality |
|---|---|---|---|
| "Key business risks identified and mitigation plans are set out in the Corporate Governance Report" (p.6) | Corporate Governance Report p.32 describes the committee and lists no risk | (b) silent drop | Framework noise; links to the Phase 4B gaps |
| MD&A section "Opportunities and Threats, Outlook, Risks and Concerns" (p.11) | Operations review p.12 gives no outlook or numbers | (b) silent drop | Thesis-relevant: no forward evidence from the company |
| "Growth led by better yield" (p.12) and Note 48 "Better Yield, Optimum Capacity Utilization" (p.79) | No yield or utilisation number in any operational section | (c) hedged retreat | Thesis-relevant: the structural reading rests on yield |
| Power and fuel savings "due to coal prices and consumption" (p.12) | Annexure III solar plant (8.89 Cr) and UF plant (p.19) | (b) silent drop of the company-specific lever | Thesis-relevant; the credit goes to an external factor |
| "Raw material ... imported" (p.11) | Foreign exchange outgo has no raw-material line (p.19) | (c) hedged retreat | Framework noise until imports appear |
Capex and expansion are not claimed in any opening section, so that is a Phase 4 omission, not a 6E item.

Phase 6 verdict: YELLOW.

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION
| Strategy | Mark | Top reasons |
|---|---|---|
| Turnaround (fullest) | WATCHLIST, leaning PASS | (1) Six quarters of rising margin, 12.2% (Jun-24) to 22.3% (Mar-26), 20.79% in Q1 FY27 persistence test passed. (2) ROCE 4-12% in FY16-FY22 to 27.9%. (3) Cause undecomposed: materials line looks industry-wide (IGCL -727 bp), fuel line company-specific; Q4 power-and-fuel low point did not repeat. Ownership change June 2023 plus board change 14-Jul-2023 date the start of the climb [INFERENCE: causality not shown]. |
| GARP (fullest) | WATCHLIST | (1) Trailing P/E 9.06 at Rs 474 (screener) and 7.28 at 31-Mar-2026 (p.20) vs 10.2 to 13.2 in FY22-FY25 (p.3). (2) Growth basis is forward evidence only if the 600 MT expansion arrives, and the AR gives no company outlook; 3-year sales CAGR 4%, TTM +18%. (3) PEG cannot be set without a forward-growth basis; capital tied up 29% in IGCL lowers growth capital. |
| Value + Quality | WATCHLIST | P/E 9; ROCE 27.9%; but 12-year history weak (B01 moat THIN, deal-breaker DB1) and disclosure weak. |
| Capex-Led Growth | WATCHLIST | Rs 33 Cr plan absent from AR; 52% spent or contracted; term loan 125.57 lakh drawn; Jan-2027 untested. |
| Cash Flow Compounder | WATCHLIST | FCF positive 11 of 12 years (B01); CFO/PAT 0.78 over 12 years; FY26 86%. |
| Contrarian | PASS | Valuation below its four-year range, no institutions, no coverage, no concalls. |
| Insider Confidence | WATCHLIST | Promoter 75% at the limit; MD holds 1,050 shares; no insider buying can be shown. |
| Guidance Divergence | FAIL | No company guidance exists. |

## PHASE 8: FINAL VERDICT DASHBOARD

Snapshot: Narmada Gelatines Ltd, Jabalpur, one plant; gelatine 70.8%, DCP 29.1% of FY26 revenue 21,541.15 lakh; PAT 2,843.82; EPS 47.01; net worth 14,130.66; market cap Rs 20,696 lakh at 31-Mar-2026 (p.20); promoter 75.00%; capacity 2,400 MT gelatine and 10,600 MT DCP (CARE, not in AR).

| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | GREEN |
| 2 Notes | YELLOW |
| 3 Financial statements | YELLOW |
| 4 Risks and MD&A | YELLOW |
| 5 Governance | YELLOW |
| 6 Front matter | YELLOW |

Quality score /10, four components at 25% each:
| Component | Score | Basis |
|---|---|---|
| Governance | 6 | Clean statutory record; cross-boards, remote board, audit chair on IGCL board, KMP numbers inconsistent |
| Accounting quality | 6.5 | B02 gave 7; front-section contradictions and token ECL pull it to 6.5 |
| Balance sheet | 8 | Net debt 0.09x operating profit, current ratio 3.59, associate 23.5% of assets is idle capital |
| Earnings quality | 6.5 | Reset real but undecomposed; CFO/PAT 86%; Q4 power-and-fuel peak not repeated |
| Overall | 6.8 (6.75) | |

Top 3 strengths: reset persists (19.18% and 20.79%); near debt-free with ROCE 27.9%; clean statutory record.
Top 3 red flags: undecomposed reset with MD&A contradictions; capital in IGCL and Pioneer Jellice flows without evidence; capex absent from the AR and cash conversion drifting.

Key monitorables: see block (`monitorables`). The first test is Q2 FY27 (12-Nov-2026): operating margin at or above 18% and materials ratio at or below 52%.

One line: a cheap, clean margin reset the company does not explain; best fit is Turnaround with GARP as the exit lens, on WATCHLIST.

## Anchor index for Stage 5 (no-concall mode)
| Topic | PDF page (printed) |
|---|---|
| MD&A: industry, price and volume, ratios | pp.11-12 (8-9) |
| Board's Report: highlights, associate status, dividend | pp.5-7 (2-4) |
| Capex-related: solar, UF plant, SAP, R&D, exports, foreign exchange | p.19 (16) |
| Working capital: Notes 10, 11, 22, 23 | pp.62-63, 67 (59-60, 64) |
| Cost lines Notes 26-33 | pp.68-69 (65-66) |
| Cash flow, balance sheet, P&L | pp.51, 49, 50 (48, 46, 47) |
| RPT Note 37, associate Note 39 | pp.73-74 (70-71) |
| Remuneration Annexure IV, MD terms | p.20, p.30, pp.128-129 |
| Shareholding, dividend history | pp.37, 39, 64 |
| Results: Q3 FY26 Labour Code note | results file 20260212, PDF p.4 |

## Anchors not found in the AR
Capex plan, tonnage, utilisation, yield percentage, raw-material price, customer concentration, pledge, IGCL market value, IGCL auditor name, FY24 balance sheet, Q1 FY27 balance sheet, covenants.

```yaml
stage: B03-ardeep
company: "SHAWGELTIN"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "No concalls, no presentation (NO-CONCALL MODE); Q2 FY27 results not yet filed; Q1 FY27 filing carries P&L only, no balance sheet or cash flow (results PDF p.2), so CWIP, term-loan draw and capex progress after 31-Mar-2026 are NOT FOUND"
  - "AR is a scanned image PDF; OCR faults in printed figures were corrected against page images (PDF pp.12, 20, 50, 51); amounts in Rs LAKH as printed, not converted"
  - "AR carries FY26 and FY25 only; FY24 and earlier balances come from screener (screening data, whole Rs Cr, standalone); FY23 dividend payout 396% is anchored to AR p.37 (Rs 6,049.59 lakh) and screener"
  - "NOT FOUND IN AR: Rs 33 Cr capex project, +600 MT gelatine, Jan-2027 commissioning, Rs 25 Cr term loan plan (none appears in Board's Report, MD&A or Annexures; source is CARE 06-Mar-2026 only); tonnage, capacity utilisation, yield %, customer concentration, IGCL market value, name of IGCL's auditor, pledge statement, headcount for FY25"
  - "No Chairman's letter exists in this AR; Phase 6 uses Board's Report, MD&A and Annexures as the opening sections"
flags:
  - {type: FLAG-CASH, reason: "CFO/PAT fell 99.0% to 86.4%; CFO/operating profit after tax 69.3% to 59.5%; working-capital outflow 846.85 vs 126.62 lakh (cash flow PDF p.51). Adjusted for customer advances up 135.18 and unpaid capex payable 53.07 sitting in the WC line (computed, arithmetic inference) CFO is about 2,267 lakh = 79.7% of PAT. Mild, not below 0.7, driven by payables normalisation (MSME 951.86 to 477.18) and receivables +16.9%. Carries B02 FLAG-WC."}
  - {type: FLAG-ASSOCIATE, reason: "Carried from B02. IGCL stake at cost 4,115.31 lakh (29.1% of equity), 1,378.29 lakh above share of net worth 2,737.02, no impairment test, no market value; audit committee chair B Vijayadurai is also an independent director of IGCL (AR PDF p.24); dividend 50.15 lakh = 1.2% cash yield on cost (PDF p.51, p.68)."}
  - {type: FLAG-DISCLOSURE-CONSISTENCY, reason: "AR front sections contradict the audited notes: MD&A says material consumed 'increased by 1.29%' but Note 28 shows a 1.29% fall (PDF p.12 vs p.68); EBITDA printed 40.88 Cr vs 42.08 Cr computed incl other income, with growth printed as 55.81% (PDF p.5) and 59.58% (PDF p.12); Annexure IV prints MD remuneration +10.41% and total KMP +4.52% while Note 37 gives 66.26 to 99.16 lakh (+49.7%) and KMP total 87.12 to 125.35 lakh (+43.9%) (PDF pp.20, 73); other expenses printed 8.94% of revenue vs 7.64% computed."}
  - {type: FLAG-CAPEX-UNDISCLOSED, reason: "No capex plan, size, funding or commissioning date in Board's Report or MD&A although CWIP 528.97, capital commitments 1,205.00 and a term-loan draw of about 125.57 lakh sit in the notes (PDF pp.61, 65, 72); capex guidance exists only in CARE press release 06-Mar-2026."}
phase_verdicts: {p1: "GREEN: unmodified opinion, no KAM, clean CARO; watch that no KAM is reported with a 29% associate stake", p2: "YELLOW: clean policies, weak disclosure, token ECL, untested associate premium", p3: "YELLOW: ROCE 28% and near-nil net debt, but CFO/PAT 86.4% and a 846.85 lakh working-capital outflow", p4: "YELLOW: no outlook, no capex disclosure, MD&A contradicts Note 28, margin drivers named but not quantified", p5: "YELLOW: promoter 75.00%, no pledge shown; promoter-group cross-boards, audit chair sits on IGCL board, MD aged 78, remote board", p6: "YELLOW: three silent drops and one hedged retreat, none breaks the thesis alone", p7_best_fit: "Turnaround (margin reset), GARP as the exit lens, WATCHLIST until Q2 FY27 and capex delivery"}
overall_quality: 6.8
quality_components: {governance: 6, accounting: 6.5, balance_sheet: 8, earnings: 6.5}
triple_pass_verification:
  verified: 15
  discrepancies: 3
best_fit_strategy: "Turnaround (margin reset) with GARP as the exit lens; WATCHLIST"
one_line_verdict: "A clean, cheap (8-9x trailing) margin reset whose cause the company does not explain; the largest line looks industry-wide, the fuel line looks company-specific, and capex, IGCL and related-party pricing are untested."
note: "Full block, with all list fields, is in outputs/blocks/B03-ardeep.yaml"
```

---
ERRATA (recorded by the orchestrator from the stage's own hand-back, 2026-11-12; the stage could not patch the report):
- Phase 2F: "41% of the term loan falls due in the first year" should read 44% (320.56 / 728.65 lakh). CFO still covers it about 7.7 times.
- The YAML at the end of this report is a short summary; the full block is outputs/blocks/B03-ardeep.yaml.
