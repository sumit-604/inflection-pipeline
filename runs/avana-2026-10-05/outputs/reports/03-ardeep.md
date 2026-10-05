# AVANA Stage 3: AR Backward Deep Dive (eight phases)
Run date 2026-10-05. Model claude-sonnet-5-5. Company: Avana Electrosystems Ltd. Mode: NO-CONCALL (RECENTLY-LISTED PRIORITY: the RHP is the backward baseline).

## Conventions
- Unit: INR lakh as printed on every face (AR, RHP, results). Not converted; stage 10 converts once. "Derived" means arithmetic on printed figures with inputs shown.
- Anchors: "AR p<N>" = pdf page of AVANA-AR-FY2025-26-with-AGM-notice.txt (printed page = pdf - 11). "RHP p<N>" = pdf page of the RHP text (printed "x of 394" = pdf - 5). "RES p<N>" = pdf page of the 23-Jun-2026 results re-filing. "BO19Aug p<N>" = Board outcome 19-Aug-2026. "AGM p<N>" = AGM proceedings 28-Sep-2026. "Reg31(4) p<N>" = promoter encumbrance filing (transcribed).
- AR pp.99-127 (financial statements and notes) are image transcriptions (second-hand reading; a stray digit is possible). Every figure I used from them ties to a second printed figure (totals, cash flow, results re-filing), noted where it matters.
- [INFERENCE] marks a reasoned link not stated in a document. Tiering: filed document, derived, or inference.

## STEP 0. Load-bearing facts, checked first (B00 LBF1-LBF4)
| LBF | Status at 2026-10-05 | Evidence |
|---|---|---|
| LBF1 capex delivery | OPEN, red. Unit not reported commissioned. 21 days to the 26-Oct-2026 KIADB date. Management says commercial production "by the end of October 2026", "well before the extended timelines" (extended date not stated). RHP planned mid-May 2026. IPO capex used 275.83 of 1,155.38 (23.9%); the FY26 RHP deployment plan for capex was up to 850.00 (275.83 = 32.4% of it). CWIP 466.79, all under 1 year; commitments 1,094.99. | BO19Aug p2 item 7; RHP p106 (schedule), p102-103 (deployment), p36-37 (deadline); AR p107 (Note 2(iii)(b)), p112 (Note 10), p119 (Note 25 item 3), p125 (item 16) |
| LBF2 concentration and receivables | PARTLY ANSWERED. FY26 top-5 share and identities NOT FOUND in the AR (searched Board report, MD&A, Notes). RHP: top 5 = 36.01% (FY23), 22.76% (FY24), 22.42% (FY25), 38.79% (H1 FY26); top 10 = 52.00% (H1 FY26). Customers appear only as "Customer 1..10" in the RHP, so identity is NOT FOUND in the corpus. Receivables 2,221.29; days 96.7 vs 125.8; over 6 months 307.13 (13.8%); zero provision. | RHP p37-38, p171-172; AR p113 (Note 14) |
| LBF3 IPO working-capital use | ANSWERED (confirms B02). WC object used 123.03 of 860.00 (14.3%); the auditor certificate shows FY26 WC gap 2,438.93 = IPO 123.03 + internal accrual 2,315.90. The 772.30 inventory build was funded by operations, payables (+401.66) and cash, not issue money. New: the RHP planned the whole 860.00 in FY26; 736.97 is unspent against that schedule. FY26 inventory ended at 2,243.25 against an RHP projection of 1,646.94 (+596.31). | RES p4; AR p107, p101; RHP p103, p43 |
| LBF4 margin bridge | ANSWERED with caution (confirms B02, adds the gross-margin path). Gross margin 47.80% (FY25) to 45.99% (H1 FY26) to 40.61% (FY26) to 36.61% (H2). EBITDA margin excl other income 20.36% to 21.33% to 19.47% to 18.08% (H2). Other expenses fell from 13.0% to 8.5% of revenue and held the margin. | RHP p120; RES p10; AR p100 |

## PHASE 1. AUDITOR'S REPORT AND CARO

### 1A Core opinion
- Unmodified opinion, true and fair view under Accounting Standards (not Ind AS), balance sheet 31-Mar-2026, P&L and cash flow (AR p89). Report date 21-05-2026, signed N. Amarnath, Partner, M.No.510064, UDIN 26510064NTCNWX1388 (AR p92). IFC opinion unmodified (AR p91, p98).
- Going concern language: NONE in the auditor's report body. CARO xix gives the standard text: "nothing has come to our attention, which causes us to believe that any material uncertainty exists ... indicating that Company is not capable of meeting its liabilities existing at the date of balance sheet as and when they fall due within a period of one year" (AR p96). The Board report states no going-concern threat (AR p49).
- Section 197(16) remark: remuneration to directors is "in accordance with the provisions of Section 197" (AR p91). The AGM notice says the FY27 proposals exceed Section 197 limits and need special resolutions (AR p28). The FY26 approval basis is NOT FOUND.

### 1B Key Audit Matters
| Subject | Finding | Risk |
|---|---|---|
| KAM section | The report contains the standard KAM paragraph ("we determine those matters ... key audit matters. We describe these matters in our auditor's report", AR p91) but no KAM section and no matter described (AR p89-92). The company was listed at the balance sheet date (20-Jan-2026). Whether SA 701 binds an NSE Emerge entity is a legal reading NOT FOUND in the document. Conservative reading: the absence is a disclosure gap, not a clean bill. | 🟡 |
| Candidate matters a reader would expect (revenue recognition at acceptance, warranty provision 322.15, inventory 2,243.25 "as certified by management", CWIP 466.79, IPO utilisation) | None addressed by the auditor. Each is covered by B02 findings and rated there. | 🟡 |

### 1C Emphasis of Matter and Other Matters
None (AR p89-92). The results re-filing carries the half-year balancing-figure note only (RES p9).

### 1D CARO 2020, clause by clause (Annexure A, AR p93-96)
| Clause | Remark | Reading |
|---|---|---|
| i(a)-(e) PPE, title | Records proper; verification phased over 3 years; leasehold land held as lessee, lease documents in company name (i(c), AR p93) | 🟢. Note the lease-cum-sale term conflict inside the RHP (RHP p37 vs p179). |
| ii(a) inventory | Physically verified; no discrepancy of 10% or more (AR p93) | 🟢 |
| ii(b) bank returns | "quarterly returns ... are in agreement with the books of accounts ... no material discrepancies" (AR p93) | 🟡 Contradicted by Note 25 item 15: bank receivables above books in all four FY26 quarters (2.15% to 7.77%; 138.36 at 31-Mar-2026) and in all four FY25 quarters (1.16% to 4.55%) (AR p125). The note labels every variance "Not Material". |
| iii loans to parties | None given; clauses not applicable (AR p94) | 🟢 |
| vi cost records | Auditor: "Central Government has prescribed the maintenance of cost records ... prima facie ... maintained" (AR p94). Board report: "not required to maintain the cost records ... has not maintained" (AR p51) | 🟡 Direct contradiction, cause NOT FOUND |
| vii statutory dues | No arrears over 6 months; no disputed dues (AR p94) | 🟢 |
| ix defaults | No default; not wilful defaulter; ix(d) no short-term funds used for long term (AR p94-95) | 🟢 |
| x(a) IPO use | "utilized for the purposes for which they were raised", see Note 2(iii) (AR p95) | 🟡 Only 398.86 of the 2,015.38 capex and WC objects was used by 31-Mar-2026 (19.8%) (AR p107); no deviation of purpose is claimed. |
| xi fraud, whistle-blower | No fraud; no ADT-4; no whistle-blower complaint (AR p95) | 🟢 |
| xiii, xiv, xv | Compliant; internal audit commensurate; no non-cash dealings with directors (AR p95-96) | 🟢 |
| xvii cash losses | None in the year or the prior year (AR p96) | 🟢 |
| xix going concern | See 1A | 🟢 |
| xx CSR | "no unspent amounts ... requiring a transfer" and no ongoing projects (AR p96) | 🟡 The Board CSR annexure shows the 12.78 obligation was paid to PMCARES on 16-Jul-2026 (AR p59), and Note 14 shows a closing CSR balance of 12.78 at 31-Mar-2026 (AR p124). It was unspent at the balance sheet date. Annexure item 6(d) prints "NIL" for total spent while the table above it prints 12,78,175 (AR p59). |

### 1E Auditor continuity
- Vasanth and Co. (FRN 008204S), appointed at the AGM of 30-Sep-2024 for 5 years to the 19th AGM in 2029 (AR p50). RHP: no change of auditor in the three years before the RHP (RHP p77), so tenure runs earlier; first appointment year NOT FOUND. Three partners on the letterhead (RES p4).
- Fees: statutory audit 7.00, tax audit 1.50, other matters 1.50, total 10.00 in FY26 and in FY25 (AR p116, p118; Board report p50 confirms 10,00,000). Non-audit ratio: 1.50 / 8.50 = 17.6%, well below 100% (derived). The fee did not change after the IPO or on revenue +36.4%.
- The same firm certified the IPO utilisation, the working-capital requirement (RES p4), the KPIs and the WC projections in the RHP (RHP p120, p43). Whether those certificates sit inside the 1.50 "other matters" line is NOT FOUND. Peer-review status NOT FOUND.
- 🟡 Small firm, flat fee, certification roles on every IPO-linked number. No independence breach is stated.

### 1F Standalone vs consolidated
Standalone only. No subsidiary, associate or JV (AR p42, p49). No other-auditor reliance.

**Phase 1 summary table**
| Item | Result |
|---|---|
| Opinion | Unmodified, AS framework |
| KAMs | None reported; KAM paragraph present, section absent |
| CARO contradictions | ii(b) vs Note 25 item 15; vi vs Board report; xx vs CSR annexure |
| Auditor | Small firm, 10.00 flat fee, issues IPO certificates |
| Going concern | Clear |
**Phase 1 verdict: 🟡 Watch.** Kill switch (informational): based on phases so far, a human reviewer would not have reason to stop, because the opinion is unmodified and the three CARO contradictions are small; they do lower trust in review quality.

## PHASE 2. NOTES TO FINANCIAL STATEMENTS (verify, extend, summarise)

### 2.0 Verification of the triple-pass Top 15 against the document
| # | B02 finding | Check against AR/RHP/RES | Result |
|---|---|---|---|
| 1 | KIADB: CWIP 466.79; capex used 275.83 of 1,155.38; unspent 879.55; commitments 1,094.99; sum 1,561.78 vs 1,305.38 (+256.40); 215.44 above the IPO object | CWIP AR p99, p112; Note 2(iii)(b) AR p107; commitments AR p119; 466.79 + 1,094.99 = 1,561.78; 1,094.99 - 879.55 = 215.44. The RHP cost 1,305.38 is "excluding GST" (RHP p102); the GST treatment of CWIP and commitments is NOT FOUND, so the 256.40 is a comparison, not an overrun. | ✓ verified, with GST caveat. Also: the RHP is internally inconsistent on the KIADB date. Risk factor: extension letter 27-Oct-2025, commercial production by 26-Oct-2026, "no further extension" (RHP p36-37). Properties note: extension 23-May-2025, commercial production "within 3 years of May 23, 2025" (RHP p179). See 4B. |
| 2 | Warranty 41.81 vs 228.47; provision 431.99 to 322.15 (-109.84, -25.4%); revenue +36.4% | AR p124 (Note 25 item 11); AR p116 (Note 24); 8,385.88 / 6,148.58 = 1.364 | ✓ verified. New text fact: the footnote says the 151.65 "amount or material consumed during the year is included in Purchases of Raw Materials and Consumables" (AR p124). It supports gross inclusion in Purchases but does not name the credit side, so Reading A vs B is still unresolved. LT 257.72 + ST 64.43 = 322.15, a fixed 80/20 split (AR p110-111). The H2 split (0.13%, 93% of usage) needs H1 inputs not in the AR; not re-verified here. |
| 3 | H2 margin 18.1% vs H1 21.3%; net material 54.0% to 63.4%; other expenses 10.7% to 6.9% | RES p10: H2 revenue 4,811.17, materials 2,744.79, inventory change +304.98, other 331.44; H1 3,574.71, 2,565.24, (634.67), 381.39. EBITDA excl OI H2 = 845.84 + 38.46 + 29.42 - 43.61 = 870.11 = 18.08%; H1 762.61 = 21.33%. Full-year net material 59.39% vs 52.19% | ✓ verified. RES p10 is OCR text of a scan; the H1 and H2 columns sum to the audited full year (8,385.88; 1,579.63) |
| 4 | Inventory +52.5%; FG +108.8%; SIT 263.44; 42.5% outside bank statement; WC object 14.3% | AR p113; 2,243.25 / 1,470.95 = 1.525; FG 690.47 / 330.62 = 2.088; bank inventory 1,289.34 = RM 1,234.84 + WIP 54.50 exactly, so FG and SIT (953.91 = 42.5%) are outside by design (AR p125 footnote) | ✓ verified. Refinement: "outside the statement" is the stated practice, not a lapse. |
| 5 | Receivables over 6 months 307.13 (13.8% vs 11.4%); over 2 years 86.24 vs 46.26; no provision | AR p113: 171.10 + 49.79 + 55.14 + 31.10 = 307.13; 76.98 + 119.23 + 14.40 + 31.86 = 242.47; 55.14 + 31.10 = 86.24; 14.40 + 31.86 = 46.26 | ✓ verified. Ageing is "from due date" |
| 6 | Bank statement receivables above books each FY26 quarter | AR p125: 6.82%, 7.77%, 2.15%, 6.23%; FY25 Q4 inventory 65.00 below books | ✓ verified. Extension: FY25 receivables were also above books in all four quarters (2.91%, 1.16%, 3.28%, 4.55%) |
| 7 | CFO 795.44 = 48.7% of EBITDA; adjusted 742.39; free cash 45.21 / 174.96 | AR p101; EBITDA excl OI 1,729.94 - 97.21 = 1,632.73; 795.44 - 30.30 - 22.75 = 742.39; 742.39 / 1,632.73 = 45.5%; 45.21 + 129.75 = 174.96 | ✓ verified |
| 8 | IPO: 551.01 paid vs 498.09 booked; 89.13 recovered (+12.7 vs pro rata); 40.36 cash gap | AR p107, p109, p117-118: 22.66 x 3 + 21.15 = 89.13; fresh share 3,053.84 / 3,522.30 = 86.70%; implied total expenses 574.5, OFS share 76.4; 89.13 - 76.4 = 12.7; 1,702.00 FD + 361.62 (bank 84.17, CC 276.41, cash 1.04) = 2,063.62 vs 2,103.98 | ✓ verified |
| 9 | FY25 comparatives differ from RHP | RHP p120 KPI: PAT 831.23, CFO 676.66; AR p100-101: 847.08, 573.22; assets 4,942.12 vs 4,838.68 (103.44). New: the 23-Jun-2026 WC certificate shows the FY25 WC gap as 2,255.47 vs the RHP 1,850.92; the 404.55 difference equals FY25 long-term provisions (AR p110), so FY25 provisions moved from current (RHP) to long-term (AR) as well (RES p4; RHP p43). | ✓ verified, extended |
| 10 | Promoter pay 289.48 (-15.0%), fixed +56.1%, FY27 341.64 (+18.0%), 78.00 family fees | AR p117-118: 88.54 + 62.86 + 74.62 + 63.46 = 289.48; FY25 fixed 185.40 + incentives 155.00 = 340.40; 289.48 / 340.40 = 0.850; 185.40 to 289.48 = +56.1%; AR p37-38 proposals 99.96 + 74.52 + 92.04 + 75.12 = 341.64; 341.64 / 289.48 = 1.180; 18.00 x 4 + 6.00 = 78.00 | ✓ verified. Discrepancy found inside the AR: the CFO and CS pay is swapped between the Board report (CFO Ravikumar 4.05, CS Amrutha 8.18, AR p52) and Note 25 item 1 (Amrutha 4.05, Ravi Kumar 8.18, AR p117). Both served about 7 months. Size 4.13, low. |
| 11 | Funding mix: pure interest 29.83 (64.55); LC and charges 55.85 (26.70); payables +43.3%; purchases +65.0% | AR p116: 26.55 + 3.28; 59.38 + 5.17; 37.57 + 18.28; 17.37 + 9.33; AR p111, p115 | ✓ verified |
| 12 | Disclosure slips (payable turnover, 0.05x cover, ROCE basis, CARO vi, CSR "first year") | AR p127: payables turnover 2.55 = 5,752.65 / (927.17 + 1,328.84), the sum, not the average (average gives 5.10x). FY25 4.35 = 3,486.93 / average with FY24 payables 676.29 (RHP p43), so FY25 used an average and FY26 did not. MD&A states interest cover 0.05x (AR p74) while the Note 24 ratio table omits the ratio (AR p127); derived 1,665.31 / 85.68 = 19.4x. ROCE 27.98% = 1,665.31 / (5,908.03 + 55.60 - 11.91): long-term debt only; FY25 57.52% on 126.16 only; the stated definition gives 48.2% | ✓ verified |
| 13 | Thin notes | Confirmed by reading AR p110-127 | ✓ verified |
| 14 | Clean base | AR p89-98, p42, p54; debt 76.14 / 5,908.03 = 0.013; gratuity 108.41 / 116.25 = 93.3% (AR p119); advances 235.19 / 109.17 = +115.4% (AR p111) | ✓ verified |
| 15 | AS framework; OFS 7,94,000 sh (468.46); promoters 73.63% | AR p47, p103, p107; 7,94,000 x 59 = 468.46; promoters 1,66,75,320 / 2,26,45,408 = 73.64% (SHP and Reg 31(4) agree: 1,66,75,408 including 88 promoter-group shares, Reg31(4) p2) | ✓ verified; B02's 73.63% is a sum of rounded percentages, the correct value is 73.64% |
Verified: 15 of 15. Discrepancies: 3 minor (finding 15 rounding; finding 10 KMP pay swap; finding 1 RHP internal date conflict). None changes a B02 rating.

### 2A Accounting policy aggressiveness (extension)
| Policy | Text and amounts | Reading |
|---|---|---|
| Revenue | Recognised "at the time of delivery and acceptance", point in time, net of taxes (Note 1, AR p103) | Conservative. No percentage-of-completion; no unbilled line. |
| Depreciation | WDV, Schedule II; plant 15 yrs, car 8, computers 3, leasehold improvements 30 (AR p104). Charge 64.63 on closing gross 842.94 + 39.37 = 7.3%. Leasehold land 172.68 not depreciated (AR p112) | Neutral. Not amortising leasehold land over the lease term is immaterial at about 1.74 a year over 99 years (derived). |
| Inventory | Standard weighted average cost; raw material "excluding non-standard, non-moving and obsolete items" valued at lower of cost and NRV; WIP at raw material cost plus overhead "as certified by the management" (AR p106). No write-down line anywhere | 🟡 The carve-out for obsolete items does not say how they are valued. No obsolescence provision is disclosed on 2,243.25. |
| Capitalisation | Borrowing costs of qualifying assets capitalised (AR p106). CWIP 466.79 "direct cost and related incidental expenses" (AR p104). No capitalised interest visible | 🟢 |
| Impairment | No indication found (AS-28) (AR p104) | 🟢 |
| ECL | None. Receivables "unsecured, considered good" 2,221.29, doubtful rows nil (AR p113). Bad debts written off 3.76 (AR p116) | 🟡 The AS framework has no ECL; 86.24 over 2 years carries no provision. |
| Lease | Finance-lease policy only (AR p105). Operating leases expensed 61.83, 5% escalation (AR p122) | Ind AS 116 rate not applicable. |
| Warranty / installation | Estimated on history (AR p106). Net-of-usage line in FY25, gross additions in FY26 (AR p116, p124) | 🟡 Policy text unchanged while the presentation changed. See B02 #2. |
| Policy change | Text says policies applied "consistent with those in the previous year" (AR p103). No change quantified | 🟡 FY25 comparatives were regrouped, "impact not material" (AR p127 item 25) with no figures. |

### 2B Related party map (extension)
| Party | FY26 | FY25 | Anchor |
|---|---|---|---|
| Four promoter directors, remuneration | 289.48 | 185.40 | AR p117 |
| Performance incentives | nil | 155.00 | AR p117 |
| CFO and CS salary | 12.23 | nil | AR p117 (CFO and CS amounts swapped in the Board report, AR p52) |
| IPO issue-expense recovery from promoters | 89.13 | nil | AR p117 |
| Independent director sitting fees (booked to IPO expenses) | 7.20 | nil | AR p117-118 |
| Relatives of KMP, consultancy and professional fees | 78.00 | 78.00 | AR p118 |
| Total printed | 476.03 | 418.40 | AR p118 |
- Operating-cost related party spend (promoter pay + KMP + relatives, ex IPO items): 289.48 + 12.23 + 78.00 = 379.71 = 4.53% of revenue and 24.0% of PBT (derived). Promoter pay alone is 24.7% of PAT (derived).
- Value-extraction signals: four wives and one mother receive flat fees of 18.00 each (four) and 6.00, identical across the two years, scope NOT FOUND. Promoter pay: +56.1% fixed vs profit +38.4%. The Board report calls the increase "marginal" (AR p52) while its own table shows +45%, +58%, +65%, +64% against median employee pay +12.79% and an average employee increment of 15.23% (AR p52). The FY27 proposal of 341.64 (+18.0%) is 4% of turnover (AR p38) and needs special resolutions. Vote result NOT FOUND (AGM p4; the scrutiniser report is not in the corpus).
- The audit committee reviewed the MD/CFO arm's-length certificate (AR p28-31). No RPT loans (AR p42). AOC-2: nothing outside arm's length (AR p67).

### 2C Contingent liabilities and commitments
| Item | FY26 | FY25 | % net worth 5,908.03 | % PAT 1,172.28 |
|---|---|---|---|---|
| Bank guarantees (against FD) | 481.42 | 485.33 | 8.1% | 41.1% |
| Letters of credit | 196.16 | 509.51 | 3.3% | 16.7% |
| TDS defaults | 1.64 | 1.68 | 0.03% | 0.1% |
| Contingent total | 679.22 | 996.52 | 11.5% (below the 25% flag) | 57.9% |
| Capital commitments (factory) | 1,094.99 | nil | 18.5% | 93.4% |
| Contingent plus commitments | 1,774.21 | - | 30.0% (over 25%, but commitments are not contingent) | 151.3% |
Anchors: AR p119 (Note 25 item 3). Guarantees plus LCs of 677.58 sit against margin money of 719.17 (AR p114), covered 1.06x. The RHP items income tax 5.71 and GST 29.33 no longer appear (B02 P3-3; RHP p44 shows a 29.33 claim by the company). No pending litigation per the auditor and Note 25 item 21 (AR p92, p126).

### 2D Receivables
- Total 2,221.29 vs 2,119.08 (+4.8%) on revenue +36.4%. Days 96.7 vs 125.8 (derived, RHP definition). H1 FY26 days 93 (RHP p113). The RHP projected FY26 at 131 days and receivables of 2,720.65; the actual is 499.36 below (RES p4; RHP p43).
- Ageing: under 6 months 1,914.16 (86.2%); 6m-1y 171.10; 1-2y 49.79; 2-3y 55.14; over 3y 31.10 (AR p113). Over 6 months 13.8% vs 11.4%. The over-6-month balance rose 64.66 (+26.7%).
- Concentration, unbilled revenue: NOT FOUND. Retention money was 119.15 inside FY25 receivables per the RHP (RHP p113); the FY26 figure is NOT FOUND.
- Bank view 2,359.64 vs books 2,221.29 (AR p125).
- 🟡 Days improved; the tail aged; no provision; lender and book numbers differ.

### 2E Inventory
- 2,243.25 (+52.5%): raw material 1,234.84 (+17.0%), WIP 54.50 (-35.6%), FG 690.47 (+108.8%), stock in transit 263.44 new (AR p113).
- Days on the RHP definition (inventory / (materials consumed + change in inventory) x 365): 164.4 vs 167.3 (FY25); FY24 134 and FY23 173 (RHP p113); plan for FY26 150. Derived.
- FG and WIP moved from 415.28 to 1,049.95 in H1 and to 744.97 by March: the H2 column of "changes in inventory" is +304.98 (RES p10). Derived. [INFERENCE] The year-end FG build is an H1 event that partly reversed in H2; the nature of FG and SIT (263.44) is NOT FOUND.
- No write-down disclosed. Inventory "as valued and certified by the management" (AR p113).

### 2F Borrowings and maturity wall
- Total 76.14 (0.013x equity): four HDFC car loans 6.06 + 19.14 + 19.14 + 31.80 at 8.10% to 8.75% (AR p110). Current maturities 20.54; long term 55.60. Monthly instalments total 2.08 (0.21 + 0.65 + 0.65 + 0.57). The maturity wall is nil.
- Repaid in FY26: unsecured loans 196.86 (lender NOT FOUND; the RHP said NBFCs and third parties, RHP p50), the EEG term loan and one car loan; cash credit 279.36 to a positive 276.41 (AR p110, p114). Director personal guarantees closed in FY26 (AR p110).
- Covenants, CC limit and rate NOT FOUND. No pledge: the Reg 31(4) filing says no encumbrance (Reg31(4) p2; B01 SHP XBRL false). ICDs given: none (AR p42).
- Cash classification: the CC balance is counted inside cash and equivalents in FY26 (276.41) but sat in borrowings in FY25 (AR p102, p110). The company does not flag it. 🟡 comparability.

### 2G Deferred tax
One line: DTA 25.27 vs 7.39; deferred tax credit 17.88 (FY25 2.24) (AR p100, p113). No components and no rate reconciliation (NOT FOUND). Current tax 426.01 is 26.97% of PBT and the total tax charge is 25.79% (407.35 / 1,579.63), against 26.23% in FY25 (derived). The DTA rose while provisions fell 109.84; this cannot be reconciled without components. 🟡

### 2H Exceptional items, ESOP, leases, post balance sheet
- Exceptional: none in either year; FY25 prior-period charge 60.17 (RHP 76.02) (AR p100). Pattern: one in three years, and restated.
- ESOP: none; sweat equity none (AR p54). EPS basic = diluted 6.34 (AR p123).
- Bonus 21:1 on 19-Aug-2025: 1,66,75,344 shares from free reserves 1,658.94 + CRR 8.59 (AR p107, p109).
- Post balance sheet events: "no material events" (AR p122 item 5; Board report AR p54). Neither mentions KIADB, the 5.5-month slip, or lease expiry. See 4B.

**Phase 2 summary.** The notes verify cleanly against B02. The accounting-quality score in B02 is 6/10 (🟡). My Phase 2 verdict agrees: 🟡. The reasons are provisioning (warranty, no ECL), restated comparatives and slips in the ratio note. I add the SA 701 gap, the CARO contradictions and the FY25 provision reclassification.
**Cross-reference with Phase 1.** Phase 1 reports no KAM, so warranty, inventory certification and IPO reconciliation were never examined in the audit report; Phase 2 finds those are exactly the open items. CARO ii(b) and vi are contradicted by the notes and the Board report.
**Phase 2 verdict: 🟡 Watch.** Kill switch (informational): based on phases so far, a human reviewer would not have reason to stop, because there is no default, no qualification and no related-party lending; the flags should travel.

## PHASE 3. FINANCIAL STATEMENTS (cash flow, then balance sheet, then P&L)

### 3A Cash flow
| Line (AR p101) | FY26 | FY25 |
|---|---|---|
| PAT | 1,172.28 | 847.08 |
| EBITDA excl other income (derived) | 1,632.73 | 1,251.96 |
| Operating profit before WC changes | 1,644.01 | 1,307.39 |
| Inventory | (772.30) | (277.64) |
| Receivables | (102.20) | (635.44) |
| Payables | 401.66 | 250.88 |
| Provisions (ST + LT) | (121.90) | 173.42 |
| Taxes paid | (382.02) | (219.52) |
| CFO | 795.44 | 573.22 |
| CFO / PAT | 67.9% | 67.7% |
| CFO / EBITDA | 48.7% | 45.8% |
| Capex (incl CWIP) | (750.23) | (23.47) |
| Capex / depreciation | 11.6x (4.4x ex CWIP) | 0.3x |
| Free cash after capex | 45.21 | 549.75 |
| M&A | none | none |
| IPO net inflow | 2,555.75 | nil |
| Debt repaid (net) | 492.36 (525.06 repaid, 32.70 raised) | 358.78 |
| Cash and bank | 2,782.78 | 530.71 |
CFO quality checks:
- CFO / PAT is below 0.7 in both years. The flag threshold is met in both years (FLAG-CASH carried).
- One-time inflators: the deferred IPO expense of 30.30 and the accrued interest of 22.75 sit in the 48.96 other-current-asset inflow; CFO excluding them is 742.39. Taxes paid 382.02 vs current tax 426.01 less 0.78 prior-year credit less the provision rise 24.89 = 400.34; the gap is 18.32, cause NOT FOUND (B02).
- Interest classification: interest paid 85.68 is in financing and interest income 83.78 is in investing; the net effect on CFO is 1.90, immaterial.
- Payables stretch: payables funded 401.66 of the 772.30 inventory build (52.0%). CFO without the payables rise would be 393.78 (33.6% of PAT). Payable days are 84.3 vs 97.0 (FY25) and a plan of 76: not stretched against FY25. Balances are "subject to confirmation" (AR p122).
- Inventory run-down: none (inventory was built).
- Deterioration test: FCF fell from 549.75 to 45.21; CFO conversion is flat at 0.68. FLAG-CASH stands.
- Cash pile: 2,782.78, of which IPO unspent 2,103.98, margin money 719.17 not freely available, and FD over 3 months 200.00. Non-IPO cash of 678.80 is 40.37 below margin money (AR p114).

### 3B Balance sheet walk and ratios (AR p99)
Assets 8,476.53: PPE 520.10 (land 173.07, leasehold land 172.68, plant 46.24 net), intangibles 11.91, CWIP 466.79, DTA 25.27, deposits 32.80, inventory 2,243.25, receivables 2,221.29, cash and bank 2,782.78, ST loans and advances 124.96 (EMD 93.35; the FY25 KIADB advance of 165.23 converted to leasehold land), other current assets 47.38.
Liabilities: equity 5,908.03 (69.7%), borrowings 76.14, provisions 753.28 (LT 294.41 + ST 458.87), payables 1,328.84, other current 410.24.

| Ratio | FY26 | FY25 | Source/derivation |
|---|---|---|---|
| Debt / equity | 0.013x | 0.26x | 76.14 / 5,908.03; AR p127 prints 0.01 |
| Net debt / EBITDA | net cash 2,706.64; not meaningful | net debt 37.80 | cash 2,782.78 - 76.14 |
| Current ratio | 3.34x (2.40x excluding the unspent IPO cash 2,103.98) | 2.10x | AR p127; derived ex-IPO |
| Quick ratio (ex inventory) | 2.33x | 1.41x (derived) | (7,419.66 - 2,243.25) / 2,218.49; FY25 (4,471.80 - 1,470.95) / 2,127.97 |
| Interest coverage (EBIT / finance cost) | 19.4x | 14.5x | 1,665.31 / 85.68; 1,321.13 / 91.25. The MD&A prints 0.05x (wrong). |
| ROCE as printed | 27.98% | 57.52% | AR p127 (long-term debt only) |
| ROCE, stated definition | 27.9% | 48.2% | EBIT / (net worth + total debt - intangibles); derived |
| ROCE ex other income and ex unspent IPO cash | 40.5% | - | 1,568.10 / (5,972.26 - 2,103.98); CWIP 466.79 left in; derived |
| ROE | 28.99% | 29.73% | AR p127 |
| Goodwill / net worth | 0% | 0% | none |
DuPont FY26 (derived): net margin 13.98% x asset turnover 1.26x (8,385.88 / average assets 6,657.6) x equity multiplier 1.65x (6,657.6 / average equity 4,044.0) = 29.0%. ROE is operational, with leverage falling (assets / equity 2.22x at FY25 to 1.43x at FY26 year end). The FY25 ROE of 29.73% printed here differs from the RHP 47.11%; the RHP uses a different equity base (RHP p120).
AVANA is not a converter, so spot ROCE is usable, but the IPO cash and CWIP distort it. Stage 10 should use the stated-definition 27.9% and the ex-cash 40.5% side by side.

### 3C P&L line walk (AR p100, p115-116)
| Line | FY26 | FY25 | YoY | % revenue FY26 / FY25 |
|---|---|---|---|---|
| Revenue | 8,385.88 | 6,148.58 | +36.4% | - |
| Materials consumed less change in FG/WIP | 4,980.34 | 3,209.29 | +55.2% | 59.4% / 52.2% |
| Gross profit | 3,405.54 | 2,939.29 | +15.9% | 40.6% / 47.8% |
| Employee cost | 1,059.98 | 886.46 | +19.6% | 12.6% / 14.4% |
| Other expenses | 712.83 | 800.87 | -11.0% | 8.5% / 13.0% |
| EBITDA excl other income | 1,632.73 | 1,251.96 | +30.4% | 19.5% / 20.4% |
| Other income | 97.21 | 144.81 | -32.9% | 1.2% / 2.4% |
| Depreciation | 64.63 | 75.63 | -14.5% | |
| Finance cost | 85.68 | 91.25 | -6.1% | |
| PBT | 1,579.63 | 1,229.88 | +28.4% | 18.8% / 20.0% |
| Tax | 407.35 | 322.64 | +26.3% | ETR 25.79% / 26.23% |
| Prior-period charge | nil | 60.17 | | |
| PAT | 1,172.28 | 847.08 | +38.4% | 14.0% / 13.8% |
- Margin waterfall, FY25 to FY26 EBITDA margin (derived): gross margin -7.19 points, other expenses +4.52 points, employee cost +1.78 points, net -0.89 points. Other expenses ex warranty (800.87 - 122.97 = 677.90; 712.83 - 41.81 = 671.02) were flat (-1.0%) on revenue +36.4%; the warranty line alone fell 81.16. Marketing consultancy and exhibitions (-30.44), legal (-23.95), sales promotion (-20.19) and travel (-18.89) fell; freight (+47.45) and labour charges (+47.16) rose (AR p116).
- Other income 97.21 = 6.2% of PBT, below the 20% flag. Interest on deposits 83.78 is 86% of it. The FY25 other income of 115.60 (9.4% of PBT) is undescribed; FY26 "Other Income" is 11.29 (AR p115).
- PAT growth: +38.4% on the AR basis; +41.0% on the RHP FY25 base (831.23). The AR basis flatters FY25 by 15.85 (prior-period charge 60.17 vs 76.02).
- Exceptional items: none in 3 years. Basic = diluted EPS 6.34 (weighted shares 1,84,76,246) (AR p123).
- H2 vs H1: revenue 4,811.17 vs 3,574.71 (+34.6%); PBT 845.84 vs 733.79; PAT 611.53 vs 560.74; EBITDA margin 18.1% vs 21.3% (RES p10). Revenue accelerated while margin fell.
- Production, from AR p85: panels 886 (523 in FY25, +69%); relays 62,034 (65,840, -5.8%). With 313 panels and 33,650 relays in H1 (RHP p121), H2 was 573 panels (+83% on H1) and 28,384 relays (-15.6%). [INFERENCE] The H2 mix shifted to panels, which fits the H2 gross-margin fall to 36.6%; segment revenue and margin are NOT FOUND, so this stays a hypothesis. Separating observation: product-wise revenue and gross margin for H1 FY27.
- Capacity check: panels produced 886 against an RHP installed capacity of 600 (RHP p104), 148% of stated capacity; relays 62,034 against 70,000 (88.6%). The RHP said the units were at optimum capacity and could not expand (RHP p104). [INFERENCE] Either capacity was stated narrowly, or output units are not comparable, or work was outsourced (labour charges +38.7%). Cause NOT FOUND. This bears on how binding the old capacity really is.

**Phase 3 summary.** Cash conversion 0.68, FCF near nil after the KIADB spend, margin exit rate below the full year, gross margin down 7.2 points offset by cost lines. The balance sheet is net cash 2,706.64 with debt 76.14.
**Cross-reference with Phases 1-2.** Phase 1 ii(b) says bank returns agree; the note shows they do not. The Phase 2 provision fall (warranty -109.84) shows up here as the 81.16 fall in the warranty expense line that supports the margin.
**Phase 3 verdict: 🟡 Watch.** Kill switch (informational): based on phases so far, a human reviewer would not have reason to stop, because liquidity is strong and the weak points are cash conversion and margin quality, not solvency.

## PHASE 4. RISK FACTORS AND MD&A

### 4A Disclosed risks, real vs boilerplate (Board report p48-49; MD&A p79-82)
| Disclosed risk | Source | Assessment |
|---|---|---|
| Market and industry (demand, competition, material prices) | AR p48 | Boilerplate. No quantification. |
| Financial (interest, FX, timely receivables) | AR p48 | Boilerplate; FX exposure is 1.02% of consumption (AR p122), so low relevance. |
| Operational (key personnel, technology, supply chain, quality) | AR p48 | Partly real. Quality links to warranty (322.15 provision) but is not tied. |
| Regulatory and compliance | AR p48-49 | Boilerplate |
| MD&A threats: low productivity, quality, intense competition, copper and aluminium prices, imports, project execution, regulation, climate, logistics | AR p79-82 | Industry text; none is tied to the company's own numbers. Copper and aluminium "added cost pressures" is the only link to the 7.2 point gross-margin fall, and it is not drawn. |
| Mitigation claim: "expansion of the customer/supplier base to avoid concentration risk" | AR p49 | No evidence offered; FY26 concentration NOT FOUND. |
The company states no risk to going concern (AR p49).

### 4B Missing risks (obvious from Phases 1-3 and the RHP, absent from the AR risk text)
| Risk | Evidence anchor | Likely reason for omission |
|---|---|---|
| KIADB deadline and cancellation: "no further extension may be granted"; the lease cancels automatically on non-implementation; deadline 26-Oct-2026 | RHP p36-37; AR p107 and p119 (unit unbuilt, 1,094.99 committed). RHP p179 gives a different extension chronology (23-May-2025, 3 years) and BO19Aug p2 refers to "extended timelines". The true date needs the KIADB letters. | The company reports good news (progress photos, AR p6) and moves status to a Reg 30 filing. Omission from the MD&A and Board report is itself a signal. |
| Lease expiry of both operating units (Aug-2026 and Jul-2026) with relocation due only in Oct-2026 | RHP p43-44: the control and relay panel unit and registered office are leased for 3 years from 18-Aug-2023; the relay unit for 11 months from 11-Aug-2025. AR Note 25 item 7 says only that leases exist and rent is 61.83 (AR p122). Renewal status NOT FOUND. | A post-period event; the Board report (19-Aug-2026) says nothing. |
| Gap between IPO schedule and actual use: 23.3% of FY26 planned capex and WC deployment used (398.86 of 1,710.00); 2,103.98 idle in deposits | RHP p102-103; AR p107; the Board report says "no deviation" (AR p51) | The ICDR "deviation" test is about purpose, not timing. |
| Customer concentration (top 5 at 38.79% in H1 FY26) and three-state dependence (MP, Maharashtra, Karnataka 48.33% to 66.42%), private players 76.24% to 82.22% | RHP p37-39 | The AR gives none of it for FY26 (NOT FOUND). |
| Warranty and product defect exposure vs a falling accrual | AR p124; AR p80 mentions quality in general | See B02 #2. |
| Gross-margin compression from mix or input cost (40.6% vs 47.8%) | RHP p120; RES p10; AR p100 | The MD&A says "no significant change" for operating margin (AR p74). |
| Lender figure gaps (bank receivables above books) and drawing-power risk | AR p125 | Labelled "Not Material". |
| Retention money in receivables (119.15 in FY25) and receivables over 2 years doubling | RHP p113; AR p113 | Not covered. |
| Panel output above stated capacity (886 vs 600), which questions the capacity thesis | AR p85; RHP p104 | Unexplained. |
| Executive pay and family fees rising faster than profit | AR p37, p52, p117-118 | Called "marginal" in the Board report. |
| Board attendance of independents (see 5A) | AR p45-46 | Not discussed. |

### 4C MD&A deep dive (AR p68-83)
- Structure: about 14 of 16 pages are industry and policy text (power capacity 532.74 GW, peak demand 256.1 GW, control panel market US$486 million in 2025 to US$790 million by 2031 at 8.4%, RDSS, Union Budget 2026-27). The company's own performance is one paragraph repeating the Board report (AR p73), plus a ratio table (AR p74). External-factor pattern: credit-taking for sector tailwinds; no blame pattern; margin movement is not explained at all.
- Missing from the MD&A: the KIADB unit, IPO use, order book (the RHP gave 5,223.65 at 30-Nov-2025, RHP p171-172, about 62% of FY26 revenue, derived), customer concentration, product or segment split (single segment, RES p2), capacity utilisation, margin explanation, cash conversion, guidance.
- Ratio table errors: interest coverage "0.05 times ... due to lower operating earnings relative to the Company's interest obligations" (AR p74) is wrong; derived 19.4x, and operating profit is 19 times interest. Debtors turnover "3.86 times" sits under a heading "(in Days)" (AR p74). "Operating profit margin 19.86% vs 21.49%" is EBIT including other income (derived: 1,665.31 / 8,385.88 and 1,321.13 / 6,148.58), and "no significant change" hides the 1.63-point fall. The ROCE and ROI drops of -51.36% and -48.94% are blamed on IPO capital (AR p127), which is fair for the denominator but ignores that the printed FY25 base excludes short-term debt.
- Product development and exports: "evaluating" and "explore" language only (AR p74, p73). Exports 46.28 = 0.55% of revenue (AR p115).
- Segment analysis: none. NOT FOUND.

**Forward guidance table with credibility check**
| Claim | Number | Timeframe | Credibility |
|---|---|---|---|
| Commercial production at the integrated unit | End-October 2026 | Q3 FY27 | Low to medium. Management slipped from the RHP schedule of mid-May 2026 (RHP p106) by about 5.5 months; construction is 466.79 of an estimate of 1,305.38, with 1,094.99 committed; a KIADB date of 26-Oct-2026 stands in the RHP; no filing says it is done (BO19Aug p2). |
| New capacity 1,75,000 relays and 1,500 panels (+150%) | 1,76,500 units | After commissioning | Untested; the old panel capacity of 600 was already exceeded in FY26 (AR p85), so the baseline is unclear. |
| IPO deployment FY26 | Capex up to 850.00; WC 860.00 | FY26 | Missed. Actual 275.83 and 123.03 (AR p107). |
| FY26 working-capital cycle | 205 days | 31-Mar-2026 | Beaten. Actual 176.8 days derived (inventory 164.4, receivables 96.7, payables 84.3), but via a different mix: inventory 14 days worse than plan, receivables 34 days better, payables 8 days longer (RHP p113). |
| FY26 inventory and receivables | 1,646.94; 2,720.65 | 31-Mar-2026 | Inventory 596.31 above plan; receivables 499.36 below plan (RES p4; RHP p43). |
| Exports to restart | One Kuwait order in FY26 | FY26 | Delivered but small: 46.28 (AR p115; RHP p171). |
| Regional offices (west, east, north-east), dealer network | Not quantified | Not stated | Follow-up NOT FOUND in the AR. |
| FY27 managerial remuneration | 341.64 (+18.0%) | FY27 | A cost commitment, not a growth guide (AR p37-38). |
| Market growth | 8.4% CAGR to 2031 | 2025-2031 | Third-party estimate, not company guidance (AR p70). The company grew 36.4% in FY26 against it. |
The AR contains no company revenue, margin or capacity guidance.

### 4D Tone and credibility (1-5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | KIADB, order book, concentration, margin drivers and IPO pace are all absent from the MD&A. The strength: RPT, CSR and ratio tables are present. |
| Consistency | 2 | MD&A interest cover 0.05x vs 19.4x; CARO vi vs Board; KMP pay swapped; "marginal" pay increase vs +45% to +65%; CARO ii(b) vs Note 25 item 15. |
| Specificity | 2 | Industry numbers are specific; company numbers are not. |
| Accountability | 2 | No acknowledgement of the schedule slip or the margin decline; "no significant change" language. |
| Capital allocation sense | 3 | Debt cleared, 2,103.98 held in deposits, IPO partly parked; the capex remains the plan. |
**Phase 4 summary.** The MD&A is mostly sector text. It omits the single largest delivery risk and carries one factual error in its own ratio table.
**Contradictions vs Phases 1-3.** MD&A "no significant change" on margin vs the H2 exit rate; "improvement in liquidity" vs IPO-funded cash; "customer base expansion to avoid concentration" vs no data.
**Phase 4 verdict: 🔴 Red flag, on disclosure quality (not on integrity).** Kill switch (informational): based on phases so far, a human reviewer would not have reason to stop, because the omissions are of coverage and are cured by the filings (BO19Aug, RHP). The reviewer should treat the MD&A as non-evidence for the thesis.

## PHASE 5. CORPORATE GOVERNANCE AND BOARD

### 5A Board composition (AR p12, p43-46, p32-35)
| Director | Role | On Board since | Other boards | Tenure flag |
|---|---|---|---|---|
| Panish Anantharamaiah | MD, promoter (18.72%); also presides at the AGM as Chairman (AGM p3) | 16-Jul-2010 | None | 16 years |
| K N Sreenath | Executive Director, promoter (18.72%); CFO until 29-Aug-2025 | 16-Jul-2010 | None | 16 years |
| Gururaj Dambal | WTD, promoter (18.72%); retires by rotation | 16-Jul-2010 | None | 16 years |
| Vinod Kumar S | WTD, promoter (17.47%) | 16-Jul-2010 | None | 16 years |
| Kishore N S | Independent; chairs Audit and CSR committees | 4-Aug-2025 | NOT FOUND | none |
| Sheela Arvind | Independent; chairs NRC | 4-Aug-2025 | NOT FOUND | none |
| Shital Darak Mandhana | Independent; chairs SRC | 4-Aug-2025 | NOT FOUND | none |
- Attendance: the Board met 23 times (AR p45-46). Of the 19 meetings after the independents joined, 7 of 7 directors attended 9 and 4 of 7 attended 10 (derived from the table). The 4 are the executive directors, so all three independents missed the same 10 meetings: independent attendance 9 of 19 = 47%, below the 75% flag. Per-director attendance is NOT FOUND (the company is exempt from the corporate governance report under Reg 15(2), AR p54). The executive directors attended all 23 (AR p32-35). 🟡
- Promoter-group cross-boards: none disclosed. Seats: none above 8.
- The Board has 4 executive promoters of 7 (57%). The MD also chairs the AGM and leads sales, so the MD is Chair and CEO combined (AGM p3).

### 5B Committees (AR p46)
| Committee | Members | Meetings | Reading |
|---|---|---|---|
| Audit | 2 independents + 1 executive; independent chair | 3 (19-Sep-2025, 24-Sep-2025, 23-Dec-2025) | None after listing within the year; the results approval was 21-May-2026 (outside the year). 🟡 |
| NRC | 3 independents | 1 (23-Dec-2025) | Thin. |
| SRC | 2 independents + MD | 1 (3-Jan-2026) | Thin. |
| CSR | 1 independent + 2 WTDs | 0 | The 12.78 obligation was paid on 16-Jul-2026 with no committee meeting in the year (AR p59). 🟡 |

### 5C Compensation
| Item | FY26 | Flag |
|---|---|---|
| Four promoter directors | 289.48 (24.7% of PAT, 3.45% of revenue) | Pay up 56.1% fixed vs PAT +38.4%. |
| CEO-to-median | MD 23.26x; WTDs 16.5x to 19.6x; median employee 3.81 lakh (+12.79%) (AR p52) | Moderate. |
| Promoter family payroll | 78.00 flat, five relatives | Scope NOT FOUND. 🟡 |
| FY27 proposal | 341.64 (+18.0%); each director's gross 6.21 to 8.33 lakh a month with Board power to revise further (AR p14-16) | Special resolutions; vote NOT FOUND. |
| ESOP dilution | None | 🟢 |
| Statutory cap check | FY26 aggregate 289.48 is 18.3% of PBT 1,579.63; MD pay 88.54 is 5.6% of PBT. The aggregate and individual caps use net profit under s.198 (NOT FOUND) | The AGM notice itself says FY27 exceeds the limits. The FY26 approval basis is NOT FOUND. 🟡 |
Management changes: the CFO changed on 1-Sep-2025 (promoter Sreenath to Ravi Kumar S); the CS changed twice (Amrutha Naveen 29-Aug-2025 to 31-Mar-2026, then C R Nerajaa from 10-Apr-2026) (AR p43, p63). Churn in the compliance role in the listing year.

### 5D Shareholding
- Promoters: 100% before the IPO (RHP, per B01) to 73.64% (1,66,75,320 / 2,26,45,408), a fall of 26.36 points. The fall is the fresh issue (51,76,000 shares) plus the OFS of 7,94,000 shares (AR p107). Promoters did not sell beyond the OFS. Pledge: nil (Reg 31(4) filing: "have not made any encumbrance ... other than those already disclosed", Reg31(4) p2; SHP XBRL flag false per B01). The phrase "other than those already disclosed" is ambiguous, and no encumbrance is disclosed anywhere in the corpus.
- Public 26.36% = the IPO allottees; the FII/DII split is NOT FOUND (31-Mar-2026 SHP XBRL, not re-opened; the Sep-2026 SHP is due 21-Oct-2026). Public turnout at the AGM: 2 members (AGM p2).
- Promoter selling against a growth narrative: the OFS raised 468.46 for promoters, 13.3% of the 3,522.30 offer (derived); modest and disclosed.

### 5E Governance red-flag checklist
| Check | Result |
|---|---|
| Whistle-blower complaints | None (CARO xi(c), AR p95) |
| SEBI or exchange actions | None disclosed (Board report, AR p54) |
| RPT committee | Audit committee approves RPTs (AR p28-31) |
| Auditor fee ratio | 17.6% non-audit |
| CSR | Obligation met after year-end; committee never met |
| Section 143(12) fraud | None (CARO xi(b)) |
| Material subsidiary auditor | Not applicable |
| Independent attendance | 47% (derived) |
| Independent professional ties | Independents are a practising CS (two) and a CA; any fee relationship with the company is NOT FOUND |
| Corporate governance report | Exempt under Reg 15(2) (AR p54) |
| Insider code, vigil mechanism | Present (AR p47, p49) |
**Phase 5 summary.** No pledge, no loans, no fraud flags. Weak points: independents' attendance, promoter pay and family fees outpacing profit, KMP churn, thin committees.
**FLAG-PROMOTER-PRELIM:** not raised (no pledge or selling pattern); the full promoter verdict stays with B08.
**Phase 5 verdict: 🟡 Watch.** Kill switch (informational): based on phases so far, a human reviewer would not have reason to stop, because no integrity event appears; the independents' attendance should be put to management.

## PHASE 6. MD'S LETTER AND FRONT MATTER (read last)

### 6A Narrative vs reality
| Claim (anchor) | Reality | |
|---|---|---|
| "commendable financial performance", total income +34.79%, PAT +38.39% (AR p13) | Revenue +36.4% and PAT +38.4% verified. PBDIT +23.85% lags (AR p13). | ✅ |
| "resilience of our business model, our operational excellence" (AR p13) | Gross margin 47.8% to 40.6%; H2 EBITDA margin 18.1%; held by lower other expenses and a falling warranty line | ❌ in part |
| "stronger capital base" (AR p13) | Net worth 5,908.03 vs 2,180.00 | ✅ |
| "a clear strategic direction" (AR p13) | The letter states none; the MD&A has no plan or targets | ❌ |
| Borrowings fell 568.51 to 76.14 "mainly due to internal accruals from Operations" (AR p43) | CFO after capex was 45.21; net repayments 492.36. The IPO utilisation shows no debt repayment. Funding came from opening cash, CFO and the 129.75 advances recovery; not contradicted, but not shown | ✅ with caveat |
| "progressing with the establishment of a new integrated manufacturing facility" (AR p6) | CWIP 466.79; commissioning has slipped from mid-May 2026 to end-October 2026 | 🟡 partly |
| "Corporate governance ... at the core" (AR p13) | CSR committee 0 meetings; independents attend 47% of meetings | ❌ in part |
| "expansion of the customer/supplier base to avoid concentration risk" (AR p49) | No FY26 data | ❌ unverified |

### 6B Strategic priorities
Capacity consolidation is the one specific priority, with capital allocated (1,155.38 IPO + internal) and execution evidence only in CWIP. Other priorities (value-added products, distribution, exports) are one-paragraph intentions with no capital or target (AR p74, p78-79).

### 6C Metrics showcased vs absent
Showcased: total income, PBDIT, PAT growth, the listing, exhibitions, an employee day-out, a medical check-up (AR p5-10, p13). Absent: order book, customer concentration, product split, capacity utilisation, ROCE, cash conversion, IPO utilisation progress, KIADB status, margin explanation, receivable ageing commentary.

### 6D Tone and drift
The RHP was operational and risk-heavy (KIADB, concentration, order book). The AR is promotional: six picture pages (AR p5-10), about 14 pages of industry text, one paragraph of company results. Drift from risk-forward to sector-forward.

### 6E Quiet Abandonment Check
| # | Opening claim | Where it should show up | Class | Materiality |
|---|---|---|---|---|
| 1 | "progressing with the establishment of a new integrated manufacturing facility ... Enhanced capacity" (AR p6) | MD&A, Board report, Notes (events after balance sheet) | (b) silent drop in the MD&A and notes: no schedule, cost, status or risk in pdf pp.68-83 or Note 25 item 5 | High: thesis-level |
| 2 | RHP "Defined timelines ... Commercial production May 2026" (RHP p105-106) | AR or Reg 30 filing with an explicit revision | (c) hedged retreat: end-October 2026 given in BO19Aug p2 with "well before the extended timelines", no mention of the earlier date | High |
| 3 | RHP: regional offices in west, east and north-east and a wider dealer network (RHP p170-171) | MD&A "Changing distribution channels" (AR p78-79) | (b) silent drop: no office count, no dealer count; the MD&A says "continues to evaluate" | Low to moderate (dealers were 0.86% of H1 revenue) |
| 4 | "OUR GLOBAL CLIENTELE ... GLOBAL COMMITMENT", six-country map (AR p3-4); Nairobi expo (AR p8) | Revenue note | (c) hedged retreat: exports 46.28 = 0.55% of revenue (AR p115); the map lists Nigeria and Malawi, the MD&A lists Kenya (AR p68) | Noise to low |
| 5 | Risk mitigation by customer diversification (AR p49) | MD&A, notes | (b) silent drop: no customer data | Moderate |
No further abandonment found. 6E is separate from 4B: 4B lists absent coverage, 6E lists present claims that are withdrawn or unmatched.

**Phase 6 summary.** The narrative is mostly true on headline growth and weak on delivery and governance.
**Phase 6 verdict: 🟡 Watch.** Kill switch (informational): based on phases so far, a human reviewer would not have reason to stop; the narrative gaps can be cured by the 26-Oct-2026 event and H1 FY27 results.

## PHASE 7. MULTI-STRATEGY SIGNAL EXTRACTION
Price inputs: market cap 315.34 Cr from the screener Data_Sheet in B01 (price date NOT FOUND); P/E on FY26 PAT 11.72 Cr = 26.9x and P/B on net worth 59.08 Cr = 5.3x (derived, not a valuation; Role 1 owns that).

| Strategy | Call | Top reasons |
|---|---|---|
| Value + Quality | WATCHLIST | (1) ROE 29%, debt 0.01x, net cash 2,706.64; (2) P/E 26.9x and P/B 5.3x are not value; (3) accounting quality 6/10 and CFO/PAT 0.68 |
| GARP | WATCHLIST | See below |
| Turnaround | FAIL (not applicable) | (1) PAT positive in all 7 years (B01); (2) the transition is a capacity and margin climb, not a loss recovery; (3) the FY21-FY22 low ROCE of 7.1% to 7.5% is pre-FY23 (B01) |
| Capex-led growth | WATCHLIST | (1) 150% capacity plan; (2) unit unbuilt, 1,094.99 committed, 21 days to the KIADB date; (3) IPO capex used 23.9% |
| Cash flow compounder | FAIL | (1) CFO/PAT 0.68 in both years; (2) FCF 45.21; (3) restricted cash 719.17 |
| Contrarian | FAIL | (1) PAT +38.4%, no price dislocation shown; (2) no distress; (3) neglect is not evidenced beyond 2 public members at the AGM |
| Insider confidence | WATCHLIST | (1) no pledge, 73.64% held; (2) OFS sold 7.94 lakh shares; (3) promoter pay up 56.1% with no insider market buying documented |
| Guidance divergence | WATCHLIST | (1) May-2026 to Oct-2026 slip; (2) WC cycle beat; (3) IPO deployment 23.3% of the FY26 plan |

**GARP (fullest reasoning).** Growth is real and large: revenue CAGR FY23-FY26 43.4% (2,840.65 to 8,385.88, derived) and PAT 92.29 to 1,172.28 (RHP p120; AR p100). With P/E 26.9x on PAT growth of 38.4% the trailing growth-adjusted multiple is 0.7 (illustrative). Three reasons keep the call at WATCHLIST. (1) The earnings base is not yet clean: the H2 exit margin is 1.4 points below the full year (18.1% vs 19.5%); a warranty accrual at the Reading B cost (2.31% of revenue) takes 1.8 points off the full-year margin and at the FY25 additions rate (3.72%) takes 3.2 points off (identity arithmetic from B02 N3, not additive to H2). The observation that separates the two readings: whether Purchases of 5,752.65 is gross or net of the 151.65 usage (an evidence request for stage 5 or Role 1), and the H1 FY27 warranty accrual rate. (2) The growth driver (capacity) is not yet delivered, and the old panel capacity was exceeded. (3) The re-rating question (recognition gap) belongs to Stage 11; the AR gives no evidence for a higher rung: gross margin, the pricing-power proxy, fell 7.2 points. The doubt is answered with position size, not input shading (A26.3).
**Turnaround (fullest reasoning).** FAIL, not a turnaround: no loss year and ROCE already 27.9%; the only weak period in the record is FY21-FY22 (B01). A margin-reset reading would apply only if the H2 margin of 18.1% became the base, and even that is far above the FY23 EBITDA margin of 6.76% (RHP p120). The transition thesis, if any, sits in the new unit and the panel mix, which stage 11 tests.

## PHASE 8. FINAL VERDICT DASHBOARD

### Company snapshot
Avana Electrosystems Ltd, NSE Emerge, listed 20-Jan-2026. Customised control and relay panels (11-400 kV) and protection relays, single segment, Bengaluru. FY26: revenue 8,385.88 (+36.4%), EBITDA excl other income 1,632.73 (19.5%), PAT 1,172.28, net worth 5,908.03, debt 76.14, cash and bank 2,782.78 of which IPO unspent 2,103.98, headcount 154, no subsidiaries (AR p99-101, p42, p52).

### Phase-wise verdicts
| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | 🟡 |
| 2 Notes | 🟡 |
| 3 Financial statements | 🟡 |
| 4 Risk and MD&A | 🔴 (disclosure) |
| 5 Governance | 🟡 |
| 6 Front matter | 🟡 |
| 7 Best fit | Capex-led growth, on a GARP watchlist, proof gate pending |

### Overall quality score
| Component (25% each) | Score /10 | Basis |
|---|---|---|
| Governance | 5 | Clean on pledge, loans, fraud; weak on independents' attendance (47%), pay and family fees, KMP churn, thin committees |
| Accounting quality | 6 | B02 6/10, reconciled; no KAM section, three CARO contradictions |
| Balance sheet | 7 | Net cash 2,706.64, debt 76.14; but the cash is largely IPO money, the working capital cycle is 176.8 days and margin money is restricted |
| Earnings quality | 6 | Growth strong; margin exit rate lower; cash conversion 0.68; warranty swing; restated comparatives |
| Overall | 6.0 | |

### Top 3 strengths
1. Balance sheet: debt 76.14 (0.013x equity), net cash 2,706.64, current ratio 3.34x (2.40x ex IPO cash) (AR p99, p127).
2. Growth with high returns: revenue +36.4%, PAT +38.4%, ROE 28.99%, revenue CAGR FY23-26 43.4% (AR p100, p127; RHP p120).
3. Clean statutory base: unmodified opinion, no default, no related-party loans, no pledge; the working-capital cycle beat the RHP plan by 28 days (AR p89-96; Reg31(4) p2; derived).

### Top 3 red flags
1. Capacity delivery: unit unbuilt, 1,094.99 committed, KIADB date 26-Oct-2026, IPO capex used 23.9%, MD&A silent (AR p107, p119; RHP p36-37).
2. Margin quality: gross margin -7.2 points, H2 EBITDA 18.1%, held by a warranty line that fell to 0.50% of revenue (AR p116, p124; RES p10).
3. Cash and reconciliation: CFO/PAT 0.68, FCF 45.21, bank-statement receivables above books each quarter, comparatives restated (AR p101, p125).

### Key monitorables for the next reporting window
| Metric | Threshold | Where | Why |
|---|---|---|---|
| KIADB unit commercial production | Reg 30 filing on or before 26-Oct-2026; KIADB letter on extension | NSE announcements; KIADB letter via operator | LBF1; cancellation risk |
| IPO capex used (cumulative) | Above 275.83, trending to 1,155.38 | Next auditor utilisation certificate (H1 FY27 results) | Delivery pace |
| Warranty additions as % of revenue | Above 2.1% (midpoint of 0.50% and 3.72%) means reversion; below 0.75% for a second period means a lasting lower rate | H1 FY27 provision note | Separates Reading A from B |
| Gross margin | Not below 40.6% (FY26); H2 FY26 was 36.6% | H1 FY27 results | LBF4 |
| EBITDA margin excl other income | Not below 18.1% | H1 FY27 results | Exit rate |
| CFO / EBITDA | Above 70% (FY26 48.7%) | H1 FY27 cash flow | Conversion |
| Inventory days | At or below 150 (RHP plan; FY26 164.4); FG 690.47 and SIT 263.44 falling | H1 FY27 balance sheet | LBF3 |
| Receivables over 6 months | At or below 13.8% of receivables; any provision | H1 FY27 ageing | Tail |
| Customer concentration | Top 5 disclosed; at or below 38.79% | H1 FY27 or AR FY27; investor query | LBF2 |
| Lease renewal of both existing units | Renewal or relocation done | Reg 30 or management reply | Continuity |
| Promoter pay vote and independent attendance | Special resolutions result; attendance above 75% | Scrutiniser report; FY27 AR | Governance |
| Panel and relay output units | Panels vs 600; relays vs 62,034 | AR Annexure E FY27 | Mix and capacity |
Thresholds are analyst markers tied to the cited FY26, H2 FY26 or RHP figures, not company guidance.

### One-line verdict
A growing, net-cash relay and panel maker whose FY26 earnings lean on a falling warranty accrual and cost lines, with the capacity unit unproven; best fit is capex-led growth on a GARP watchlist until the KIADB unit starts and H1 FY27 margin holds.

## Anchor map for stage 5 (no-concall mode)
| Topic | Pages |
|---|---|
| MD&A | AR p68-83 (printed 57-72); ratio table p74; outlook p75-79 |
| Board report, risks, committees, pay | AR p41-56; risk framework p48-49; attendance p45-46; pay table p52 |
| AGM notice, RPT standard form, FY27 pay | AR p14-40 |
| Auditor report, CARO | AR p89-98 |
| IPO objects and use | AR p107 (Note 2(iii)); RHP p101-106 (objects, deployment, schedule, cost); RES p4 (WC certificate) |
| Capex status and commitments | AR p112, p119, p125; BO19Aug p2; RHP p36-37, p179 |
| Customer and region concentration | RHP p37-39 |
| Order book | RHP p171-172 |
| Working-capital plan and assumptions | RHP p42-43, p113-114 |
| KPIs, production | RHP p120-121; AR p85 |
| Results H1/H2 split | RES p10 |
| Warranty and installation | AR p124; Note 24 p116 |
| Bank stock statement | AR p125 |

## Input gaps carried (B00 and B02, unchanged) plus new NOT FOUND from this stage
- All B00 and B02 input gaps carry forward (see block).
- New: FY26 customer concentration (AR); KIADB extension letters and the true KIADB date (RHP internal conflict); lease renewal status for both units; per-director attendance; independents' other directorships; FY26 approval basis for director pay; vote result on Items 4-7; auditor peer-review status; SA 701 applicability reading; capacity basis for panels (886 vs 600); product-wise revenue and margin; whether the IPO certificates fall inside the 1.50 other-matters fee.

```yaml
stage: B03-ardeep
company: "AVANA"
run_date: "2026-10-05"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "B00: BSE scrip code absent (collector); repaired at /step1 from NSE API; NSE-only SME listing"
  - "B00: shareholding Sep-2026 not yet filed (due 21-Oct-2026); 31-Mar-2026 SHP held; FII/DII split not re-opened"
  - "B00: screener export sheets empty (P&L, Quarters, Balance Sheet, Cash Flow, Customization for AVANA and peers); Data_Sheet CSVs used"
  - "B00: original FY26 results PDF scanned; legible re-filing 2026-06-23 used (RES p10 is OCR text of a scan)"
  - "B00: no credit rating document; rating_wc_quote unresolved"
  - "B00: no concalls (NO-CONCALL MODE); presentation/ and research/ empty"
  - "B00: only FY2025-26 AR exists; FY23-FY25 from RHP restated financials; final prospectus (14-Jan-2026) not collected"
  - "B00: AR pdf pp.2-4 and 99-127 are image transcriptions (second-hand reading; stray digit possible); Reg 31(4) filing read from transcription"
  - "B00: peer transcripts only for DANISH; SPCL and MARINE presentations only; no listed protection-relay pure play"
  - "B02: NOT FOUND in AR notes: FY26 customer concentration and identity; product-wise revenue; order book; unsatisfied performance obligations; CC limit, rate, covenants, repayment schedule; lender of repaid unsecured loan 196.86; deferred tax components and rate reconciliation; leave encashment roll-forward; lease commitments; warranty period assumptions"
  - "B02: NOT FOUND: nature of stock in transit 263.44; description of FY25 other income 115.60; reason for lower warranty accrual rate; whether Purchases 5,752.65 is gross or net of 151.65 warranty usage (footnote says usage is included in Purchases, credit side not stated); FY26 revenue-authority balance netting; cause of 18.32 tax-roll gap"
  - "B03: KIADB deadline conflict inside RHP (26-Oct-2026 at RHP p36-37 vs 23-May-2025 plus 3 years at RHP p179) and BO19Aug 'extended timelines' undated; KIADB letters NOT FOUND"
  - "B03: lease renewal status of both operating units (RHP p43-44 expiry Jul/Aug-2026) NOT FOUND"
  - "B03: per-director board attendance, independents' other directorships, FY26 approval basis for director pay, AGM vote results on Items 4-7 NOT FOUND"
  - "B03: auditor peer-review status, SA 701 applicability reading, whether IPO certificates fall inside 1.50 other-matters fee NOT FOUND"
  - "B03: capacity basis for panel output (886 produced vs 600 installed, RHP p104) and product-wise revenue and margin NOT FOUND"
flags:
  - {type: FLAG-CASH, reason: "CFO 795.44 = 67.9% of PAT (FY25 67.7%) and 48.7% of EBITDA excl other income; FCF 45.21 vs 549.75; inventory +772.30; bank-statement receivables above books each quarter (AR p101, p113, p125)"}
  - {type: FLAG-CAPEX, reason: "KIADB unit unbuilt: CWIP 466.79, commitments 1,094.99, IPO capex used 275.83 of 1,155.38 (32.4% of FY26 plan 850.00); RHP date conflict (26-Oct-2026 vs 23-May-2028 on a 3-year reading); RHP schedule mid-May 2026 slipped to end-Oct 2026; MD&A silent (AR p107, p119; RHP p36-37, p106, p179; BO19Aug p2)"}
  - {type: FLAG-PROVISION, reason: "Warranty additions 41.81 (0.50% of revenue) vs 228.47 (3.72%); provision down 25.4%; footnote says usage 151.65 is included in Purchases, credit side not stated (AR p124)"}
  - {type: FLAG-MARGIN, reason: "Gross margin 47.80% to 40.61% (H2 36.61%); H2 EBITDA excl other income 18.08% vs H1 21.33%; held by other expenses falling from 13.0% to 8.5% of revenue (RHP p120; RES p10; AR p100)"}
  - {type: FLAG-GOVERNANCE, reason: "Independents attended 9 of 19 meetings (derived 47%); CSR committee 0 meetings; promoter pay +56.1% fixed vs PAT +38.4%, called marginal; family fees 78.00; CFO and CS churn (AR p45-46, p52, p117-118)"}
phase_verdicts: {p1: "yellow: unmodified opinion, no KAM section, CARO ii(b), vi, xx contradicted by notes/Board report", p2: "yellow: 15 of 15 verified; warranty, no ECL, restated comparatives, FY25 provisions reclassified", p3: "yellow: CFO/PAT 0.68, FCF 45.21, gross margin -7.2 pts, net cash 2,706.64", p4: "red (disclosure): MD&A silent on KIADB, order book, concentration, margin; interest cover 0.05x wrong vs 19.4x", p5: "yellow: no pledge or loans; independents 47% attendance, pay and family fees, KMP churn", p6: "yellow: headline growth true; delivery and governance claims weak; 5 quiet abandonments", p7_best_fit: "Capex-led growth on a GARP watchlist; proof gate pending (KIADB unit)"}
overall_quality: 6.0
quality_components: {governance: 5, accounting: 6, balance_sheet: 7, earnings: 6}
kill_switch_notes:
  - "P1: would not stop; unmodified opinion, contradictions are small but lower trust in review quality"
  - "P3: would not stop; solvency strong, weak points are cash conversion and margin quality"
  - "P4: would not stop; omissions are of coverage, cured by filings; treat MD&A as non-evidence"
  - "P5: would not stop; no integrity event; put independents' attendance to management"
triple_pass_verification:
  verified: 15
  discrepancies:
    - {finding_rank: 15, triple_pass_value: "promoters 73.63%", ar_value: "73.64% (1,66,75,320 / 2,26,45,408; SHP and Reg 31(4) agree)", note_ref: "AR p107-108 Note 2; sum of rounded percentages explains 73.63"}
    - {finding_rank: 10, triple_pass_value: "CFO/CS pay not cross-checked", ar_value: "Board report p52 lists CFO 4.05 and CS 8.18; Note 25 item 1 lists CS 4.05 and CFO 8.18 (swapped, 4.13)", note_ref: "AR p52 vs AR p117"}
    - {finding_rank: 1, triple_pass_value: "RHP deadline 26-Oct-2026, no further extension", ar_value: "RHP p36-37 matches; RHP p179 says extension 23-May-2025 with commercial production within 3 years of that date; BO19Aug says 'extended timelines' undated", note_ref: "RHP p36-37, p179; BO19Aug p2"}
missing_risks:
  - "KIADB deadline 26-Oct-2026, no further extension, automatic cancellation; absent from MD&A and Board risk text (RHP p36-37; AR p48-49, p68-83)"
  - "Lease expiry of both operating units Jul/Aug-2026 before relocation (RHP p43-44; AR p122)"
  - "IPO deployment 398.86 of 1,710.00 FY26 plan (23.3%), 2,103.98 idle (RHP p102-103; AR p107)"
  - "Customer concentration top 5 38.79% H1 FY26 and three-state dependence; FY26 not disclosed (RHP p37-39)"
  - "Gross margin compression 47.8% to 40.6% not explained; MD&A says no significant change (RHP p120; RES p10; AR p74)"
  - "Bank stock statement variances and drawing power (AR p125)"
  - "Panel output 886 above stated capacity 600 (AR p85; RHP p104)"
  - "Retention money in receivables 119.15 FY25 and over-2-year receivables doubling (RHP p113; AR p113)"
  - "Promoter pay and family fees outpacing profit; independents' attendance (AR p45-46, p52, p117-118)"
guidance_table:
  - {claim: "Commercial production at integrated KIADB unit", number: "end-October 2026", timeframe: "Q3 FY27", credibility: "Low to medium: slipped from RHP mid-May 2026; unit unbuilt at 466.79 CWIP plus 1,094.99 committed; no completion filing (BO19Aug p2; RHP p106)"}
  - {claim: "New capacity 1,75,000 relays and 1,500 panels", number: "+150%", timeframe: "post-commissioning", credibility: "Untested; panel baseline 600 already exceeded at 886 in FY26 (AR p85; RHP p104)"}
  - {claim: "IPO deployment FY26", number: "capex up to 850.00; WC 860.00", timeframe: "FY26", credibility: "Missed: 275.83 and 123.03 used (AR p107; RHP p102-103)"}
  - {claim: "FY26 working-capital cycle", number: "205 days", timeframe: "31-Mar-2026", credibility: "Beaten: 176.8 days derived; mix differs (inventory worse, receivables better) (RHP p113; AR p99, p100, p115)"}
  - {claim: "Exports restart", number: "one Kuwait order; actual 46.28", timeframe: "FY26", credibility: "Delivered but small, 0.55% of revenue (AR p115; RHP p171)"}
  - {claim: "Regional offices and dealer network expansion", number: "not quantified", timeframe: "not stated", credibility: "Follow-up NOT FOUND in AR (RHP p170-171)"}
  - {claim: "FY27 managerial remuneration", number: "341.64 (+18.0%)", timeframe: "FY27", credibility: "Cost commitment; special resolutions; vote NOT FOUND (AR p37-38)"}
monitorables:
  - {metric: "KIADB unit commercial production", threshold: "Reg 30 filing by 26-Oct-2026; KIADB extension letter", where: "NSE announcements; KIADB letters via operator", why: "LBF1; lease cancellation risk"}
  - {metric: "IPO capex used (cumulative)", threshold: "above 275.83 trending to 1,155.38", where: "Auditor utilisation certificate with H1 FY27 results", why: "Delivery pace"}
  - {metric: "Warranty additions % revenue", threshold: "above 2.1% = reversion; below 0.75% for a second period = lasting lower rate (analyst midpoint of 0.50% and 3.72%)", where: "H1 FY27 provision note", why: "Separates Reading A from B"}
  - {metric: "Gross margin", threshold: "not below 40.6% (FY26); H2 FY26 36.6%", where: "H1 FY27 results", why: "LBF4"}
  - {metric: "EBITDA margin excl other income", threshold: "not below 18.1%", where: "H1 FY27 results", why: "Exit rate"}
  - {metric: "CFO / EBITDA", threshold: "above 70% (FY26 48.7%)", where: "H1 FY27 cash flow", why: "Conversion"}
  - {metric: "Inventory days and FG", threshold: "at or below 150 days (FY26 164.4); FG 690.47 and SIT 263.44 falling", where: "H1 FY27 balance sheet", why: "LBF3"}
  - {metric: "Receivables over 6 months", threshold: "at or below 13.8%; any provision", where: "H1 FY27 ageing", why: "Tail ageing"}
  - {metric: "Customer concentration", threshold: "top 5 disclosed; at or below 38.79%", where: "H1 FY27 or AR FY27; investor query", why: "LBF2"}
  - {metric: "Lease renewal of both existing units", threshold: "renewed or relocation done", where: "Reg 30 or management reply", why: "Continuity before relocation"}
  - {metric: "Promoter pay vote and independent attendance", threshold: "special resolutions result; attendance above 75%", where: "Scrutiniser report; AR FY27", why: "Governance"}
  - {metric: "Panel and relay output", threshold: "panels vs 600 installed; relays vs 62,034", where: "AR FY27 Annexure E", why: "Mix and capacity"}
ar_new_downstream_entities:
  - name: "KIADB (Karnataka Industrial Areas Development Board)"
    where_in_ar: "AR p6 (facility page); Note 16 p114 (advance to KIADB 165.23 in FY25); also RHP and BO19Aug"
    entity_type: "land authority and project counterparty (lease terms and deadline)"
  - name: "Kuwait export customer (unnamed)"
    where_in_ar: "Note 18 p115 export sales 46.28; AR p4 map; MD&A p68"
    entity_type: "export customer"
  - name: "ELAsia 2026, BIEC Bengaluru, 14-17 May 2026"
    where_in_ar: "AR p7"
    entity_type: "named exhibition platform"
  - name: "Africa Power & Energy Expo 2026, Nairobi"
    where_in_ar: "AR p8"
    entity_type: "named exhibition platform"
strengths_top3:
  - "Balance sheet: debt 76.14 (0.013x), net cash 2,706.64, current ratio 3.34x (2.40x ex IPO cash)"
  - "Growth with returns: revenue +36.4%, PAT +38.4%, ROE 28.99%, revenue CAGR FY23-26 43.4%"
  - "Clean statutory base: unmodified opinion, no default, no related-party loans, no pledge; WC cycle 176.8 vs plan 205 days"
red_flags_top3:
  - "Capacity delivery: unit unbuilt, 1,094.99 committed, KIADB date 26-Oct-2026, IPO capex used 23.9%, MD&A silent"
  - "Margin quality: gross margin -7.2 pts, H2 EBITDA 18.1%, held by a warranty line at 0.50% of revenue"
  - "Cash and reconciliation: CFO/PAT 0.68, FCF 45.21, bank-statement receivables above books each quarter, comparatives restated"
best_fit_strategy: "Capex-led growth on a GARP watchlist; proof gate pending (KIADB unit and H1 FY27 margin)"
one_line_verdict: "A growing, net-cash relay and panel maker whose FY26 earnings lean on a falling warranty accrual and cost lines, with the capacity unit unproven; WATCHLIST until the KIADB unit starts and H1 FY27 margin holds."
analyst_note: "New beyond B02. (1) Note 25 item 11 footnote says the 151.65 warranty usage is 'included in Purchases' (AR p124); credit side still unstated, Reading A vs B open. (2) RHP is internally inconsistent on the KIADB date (26-Oct-2026 at RHP p36-37 vs 23-May-2025 plus 3 years at RHP p179); BO19Aug says 'extended timelines' undated. Get the KIADB letters. (3) RHP planned the whole 860.00 WC and 850.00 capex in FY26; used 123.03 and 275.83. (4) Production: panels 886 vs 600 installed capacity, relays -5.8%; H2 implied panels +83%, relays -15.6% on H1 [INFERENCE: mix drives H2 gross margin 36.6%; segment margin NOT FOUND]. (5) FY25 provisions moved from current (RHP) to long-term (AR); WC certificate gap 2,255.47 vs RHP 1,850.92, diff 404.55. (6) Independents attended 9 of 19 board meetings after 4-Aug-2025. (7) Both operating-unit leases expire Jul/Aug-2026 per RHP; renewal NOT FOUND."
```
