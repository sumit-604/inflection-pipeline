# STAGE 3: ANNUAL REPORT DEEP DIVE, BACKWARD READ: Kwick Forensic Solutions Ltd (KWICK), run 2026-10-04

## 0. BASIS, UNITS, AND WHAT IS NOT AVAILABLE

- AR substitute: final Prospectus dated 31-Aug-2026 (AMAGI 2026-07-12 precedent). Cited as "p.N" = PDF page of `inputs/prospectus/KWICK-Prospectus-2026-08-31.txt`. Unit is **Rs lakh** as printed on the face (p.226 "Rs. In Lakhs"). Screener Data_Sheet is Rs Cr and is labelled "(screener, Rs Cr)". "Computed" means my arithmetic on printed figures. Accounting basis is Indian GAAP (AS), standalone, no subsidiaries (p.229, p.244 item vii).
- NOT AVAILABLE (no annual report exists, listed 03-Sep-2026): statutory auditor's report with KAMs, CARO 2020, directors' report, chairman's letter, board and committee attendance, prior-year ARs, AGM notice, whistleblower report, section 143(12) reporting. Each is flagged where a phase needs it, and the prospectus equivalent is used.
- Post-listing sources read: 6 BSE filings 24-30 Sep 2026, the 30-Sep-2026 investor deck (22 pp), the SEBI order of 18-Aug-2026 on the BRLM (19 pp).
- B02 inputs: `02-notes.md` (Top 15) and `B02-notes.yaml`. Phase 2 verifies them below.

---
## 0.1 FIRST VERIFICATION PRIORITIES (checked before my own work)

### LBF-1 Customer shift and non-government buyer identity: STILL OPEN on names, but the filing now supplies a mechanism

| Test | Result | Anchor |
|---|---|---|
| Government share of revenue | 86.98% / 78.91% / 55.22% FY24/FY25/FY26. Non-government Rs 393.03 / 1,371.18 / 4,733.92 lakh (13.02 / 21.09 / 44.78%) | RF10 p.29; business p.160 |
| Share of FY26 growth from non-government | 3,362.74 of 4,068.59 = 82.65% (computed). Government grew 705.85 only | p.29 |
| Buyer names | NOT FOUND. Top 10 anonymous (77.64% of FY26, 8,207.23) | pp.160-161 |
| Related-party sale or receivable | None in Annexure VIII. Group entities are not buyers per disclosure. Completeness untestable | pp.250-251; p.219 |
| **NEW: channel-shift disclosure** | "Strategic shift towards a collaborative execution model, wherein scientific and digital kits are supplied through local dealers and established vehicle manufacturers instead of directly supplying complete vehicles ... the investment in vehicles is transferred to local partners". FY26 kits for **95 Mobile CSI vehicles, revenue Rs 2,035.74 lakh** | p.150 |
| Where the 2,035.74 sits | NOT STATED. It is not in the Mobile CSI Vehicles line (1,056.76 for 25 direct vans, p.24, p.141). Ratio test: 2,035.74 is 99.2% of the Forensic Science and Physical Evidence line's FY26 growth (1,859.28 to 3,910.84 = +2,051.56) and 43.0% of FY26 non-government revenue; 60.5% of non-government growth (all computed) | p.24; p.150 |
| B2B and B2C table | **Exists** (B02 said "B2C definition NOT FOUND": the table exists, the definition does not). B2C 1,254.23 / 1,720.79 / 1,108.08 lakh = 41.55 / 26.46 / 10.48%. B2B 9,463.21 (89.52%) FY26 | p.160 |
| What B2C cannot mean | B2C exceeded non-government in FY24 (1,254.23 vs 393.03) and FY25 (1,720.79 vs 1,371.18). So B2C is not "private buyers". At least 861.20 (FY24) and 349.61 (FY25) of B2C is government (computed). At least 3,625.84 of FY26 non-government revenue is B2B (4,733.92 less 1,108.08, computed) | p.160 |
| Single-buyer arithmetic | Rental revenue equals one customer each year: 671.33 (FY24 Top 1), 840.03 (FY25 Top 2), 925.41 vs 925.42 (FY26 Top 3) (pp.24, 160). FY25 Top 3 customer 542.37 = Meghalaya revenue 542.37; FY25 Top 6 417.71 = Mizoram 417.71; FY26 Top 6 541.07 = Assam 541.07 (p.159). So several top customers are single state buyers | pp.24, 159, 160 |

**Most evidenced reading [INFERENCE]:** a large part of the non-government jump is a billing-channel change. The end buyer of the 95 vans is still a state police or forensic department, but the invoice now goes to a private dealer or vehicle builder, so the revenue is booked as "non-government". The filing does not say this outright. It says the kits went through dealers and vehicle manufacturers and gives the Rs 2,035.74 lakh figure, and it does not state the buyer class of that revenue.
**Other reading:** genuine private buyers (labs, universities, corporates) in Maharashtra (+1,140.09), Rajasthan (+818.19), Haryana (+616.99), Assam (+536.06) (state growth computed from p.159).
**Observation that separates them:** the top-10 names with end-user, and the ship-to or tender owner for the 95 vehicles. A tender list that names the vehicle builder as supplier with Kwick kits as sub-supply confirms the channel reading.
Consequence for LBF-2: dealer-billed receivables are only as good as the state payment that funds the dealer. The "private mix gives faster collection" claim (p.91) cannot be tested without the buyer split.

### LBF-2 Debtor days basis: RESOLVED (and ties to B01)

| Basis | FY24 | FY25 | FY26 | Anchor |
|---|---|---|---|---|
| Company "debtor days" | 83 | 89 | 74 | p.91, p.245 |
| Formula in the filing | 365 / (Net revenue / **average** receivables) | same | same | p.245 |
| Reproduction, average basis | 83.1 (opening FY23 receivables 181 lakh, screener Rs 1.81 Cr, scaled) | 89.0 | 73.7 | computed from p.226, screener |
| Year-end receivables / revenue x 365 | 144.3 | 111.1 | 79.0 | computed; the filing prints the same ratio as 39.54% / 30.43% / 21.64% (p.92-93) |
| Receivables > 6 months, % of gross | 12.32% | 16.97% | 11.85% | Note I.14 p.235, computed |

- Verdict: the improvement is real on both bases (year-end 144 to 79). The 74 headline is an average-basis number; year-end FY26 is 79. The FY27 working capital plan reuses "74 days" against a year-end receivable of Rs 3,000.00 lakh (p.95). That implies revenue of about Rs 14,797 lakh if 74 is read at year end (computed, 3,000 / 74 x 365), which is +40.0% on FY26. The filing does not state the revenue it assumes.
- Q4 loading: FY25 Q4 = 51% of annual sales (p.92). FY26 Q4 share NOT FOUND. MD&A says "business is not seasonal" (p.270). The two statements conflict.
- Operating working capital basis point (changes a B02 conclusion): see Phase 2 discrepancy 1.

### LBF-3 CFO vs PAT: VERIFIED against the restated cash flow (Annexure III p.228)

| Rs lakh | FY24 | FY25 | FY26 |
|---|---|---|---|
| CFO | (260.57) | 465.09 | 762.30 |
| PAT | 283.47 | 855.94 | 1,350.77 |
| CFO / PAT | -91.9% | 54.3% | 56.4% |
| CFO / EBITDA (EBITDA 544.51 / 1,224.89 / 1,906.49, p.248) | -47.9% | 38.0% | 40.0% |

Three-year CFO 966.82 = 38.8% of three-year PAT 2,490.18 (computed). Six-year cumulative from screener (Rs Cr): CFO 12.66 vs net profit 27.58 = 45.9% (FY21-FY26, screener Data_Sheet). B01 agrees (0.459).

### LBF-4 Disclosure conduct: FOUR items, one of them new

1. **Sequence (computed day of week):** BSE price-movement query by email Fri 25-Sep-2026; company reply Sat 26-Sep says it "is not aware of any information, event, development or impending announcement" and "no undisclosed price-sensitive information or material event" (announcement 26-Sep-2026); Reg 30 note Sun 27-Sep on a Rs 150 crore NFSU Varanasi campus, "emerging opportunities" (announcement 27-Sep-2026). The note names no order, tender, customer or amount for Kwick. Varanasi does not appear anywhere in the prospectus; NFIES "new NFSU campuses" is mentioned only generically (p.124). The trading window stayed open to 30-Sep and closed from 01-Oct-2026 (announcement 28-Sep-2026).
   - Reading 1 [INFERENCE]: price-supportive communication timed after a query. Reading 2: routine investor relations ahead of the 30-Sep Arihant conference (intimated 24-Sep, before the query). Separating observation: whether a filing ever ties an NFSU or MHA order to Kwick. None does today.
2. **Investor deck vs prospectus (30-Sep-2026):** deck says "130 total no. of customers served" (deck p.6) vs 95 / 124 / 128 in the prospectus (p.23, p.259). Deck income statement prints PBT 1,921.45 vs 1,821.45 in the restated P&L (deck p.20 vs p.227; the other lines sum to 1,821.45). Deck cash flow prints investing (273.14) vs (273.17) (p.228). Deck says "end-to-end development and manufacturing"; prospectus says "we are not a manufacturing unit ... do not own any major plant and machinery" (p.158), and inventory is traded goods only (p.235).
3. **BRLM:** SEBI order 18-Aug-2026 bars Corporate Capital Ventures Pvt Ltd from new assignments for one month on findings that include failure to exercise due diligence on another IPO (Uma Exports) (order paras 30-34). The order does not concern Kwick. SAT stayed it on 24-Aug-2026, appeal listed 17-Nov-2026 (RF15, p.33). Linked fact: CCV Emerging Opportunities Fund-I, whose unitholders include a director of the BRLM, took 35,153 shares (281,224 post bonus) in the Dec-2024 placement at Rs 569 and held 156,224 on 14-Aug-2026, i.e. sold 125,000 shares (44.4%, computed) before the IPO (RF16, p.34). Item 34 of Capital Structure says the lead manager and its associates hold no equity (p.85). That is not a contradiction on its face, but it needs the "associate" definition applied to the fund. Across the 17 placement allottees, 572,440 of 1,434,360 post-bonus shares (39.9%) were no longer held by the original allottee on 14-Aug-2026, and 7 of 17 held nil (computed, p.34). Sale prices and buyers NOT FOUND.
4. **NEW: governance record contradicts itself.** KPIs "have been approved by a resolution of our Audit Committee dated 25-05-2026" (p.256), but the Audit Committee was "constituted vide Board Resolution dated July 04, 2026" (p.196). The FY26 restated statements were approved on 25-05-2026 (p.222, p.226) with no audit committee in existence on the filing's own dates. The Nomination and Remuneration Committee is also dated 04-Jul-2026 (p.198). Either the 25-May date is wrong or the committee approval did not happen. This is a documentation defect in a regulated document, not a number.

---
# PHASE 1: AUDITOR'S REPORT AND CARO (limited visibility)

**Source actually available:** "Independent Auditor's Examination Report on Standalone Restated Financial Information" (pp.221-225). It is a restatement certificate for the offer document, not the statutory audit report. KAMs and CARO are NOT AVAILABLE.

### 1A Core opinion
| Item | Content | Anchor |
|---|---|---|
| Type | Examination report on restated information under s.26 Companies Act, ICDR 2018, ICAI Guidance Note 2020. No audit opinion paragraph | p.221 |
| Auditor | A B C D & Co LLP, FRN 016415S/S000188, partner Vinay Kumar Bachhawat, UDIN 26214520XQTXYD6606, 25-May-2026, Chennai | p.225 |
| Basis | Accounting Standards under s.133 | p.222 (5a) |
| Qualifications | "There were no qualifications in the Audit Reports ... which would require adjustments" | p.223 (7h) |
| Going concern | NONE in the report. The only "going concern" text in the document is the exchange eligibility table, not a company statement | p.223; B02 |
| Policy change | One: gratuity moved from cash to actuarial (AS 15), FY24 only | p.223 (7k), p.249 |

### 1B Key audit matters
NOT AVAILABLE. The table below is analyst-substituted (areas where an auditor would normally spend KAM effort), not auditor KAMs.

| Area (analyst-substituted) | Why key | Evidence | Risk |
|---|---|---|---|
| Revenue recognition | Two bases (delivery/commissioning or percentage of completion), POC contract value NOT FOUND, unearned revenue 166.50 new in FY26 | pp.229-230; I.7 p.234 | 🟡 |
| Receivable provisioning | No ECL or doubtful-debt rule; 130.54 at 2-3 years provided 27.00 (20.7%) | I.14 p.235 | 🟡 |
| Software capitalisation | CWIP 137.17 unamortised; policy lacks AS 26 research/development criteria | I.9 p.237; p.230 | 🟡 |
| Related-party transactions | Software and goods from promoter-group firms | pp.250-251 | 🟡 |
| Impairment | Software CWIP and 164.50 of scanners added FY26; no impairment indicators disclosed | p.237; p.230 | 🟢 |

### 1C Emphasis of matter and other matters
No emphasis of matter. Other matter: FY24 was audited by the previous auditor Ghewarchand Rathan Kumar (report dated 05-Sep-2024); ABCD relied on it for FY24 (p.222 para 6b). Reason for the auditor change NOT FOUND.

### 1D CARO 2020 clause by clause
NOT AVAILABLE. Substitutes from the prospectus:

| Clause | Substitute evidence | Anchor |
|---|---|---|
| ii inventory verification | NOT AVAILABLE. Physical stock sits at the registered office (p.31). Inventory is 100% traded goods (p.235) | p.31; p.235 |
| iii loans to related parties | None granted (Annexure V ii) | p.244 |
| vii statutory dues | Company admits 7 late TDS payments (to 91 days), 2 late TDS returns, 3 GST delays, advance tax shortfalls 43.24 + 129.80 + 18.37 = 191.42 lakh over FY24-FY26, EPF and ESI lapses. All stated as paid | RF5 pp.25-27 |
| ix borrowing default | None disclosed; borrowings nil at FY26 | p.254 |
| xi fraud | Nothing disclosed; section 143(12) NOT AVAILABLE | n/a |
| xvii cash losses | None (profit every year) | p.227 |
| xx CSR | 12.00 spent vs 11.55 required; no shortfall | p.240 |

### 1E Auditor continuity
| Item | Content | Flag |
|---|---|---|
| Firm and tenure | ABCD LLP since FY25 (two audits). ADT-1 was filed 29-Oct-2024, due 15-Oct-2024 | 🟡 late filing (p.38) |
| Statutory audit fee | 2.00 / 3.28 / 1.03 lakh FY26/FY25/FY24; FY26 fee fell 39% while revenue rose 62.6% (computed) | 🟡 low and falling: 0.019% of revenue (computed) |
| Other certifications | 0.91 lakh FY26 only; non-audit to audit 45.5% (computed). IPO certificates are numerous (dated 26-Jun to 06-Jul-2026) and may be charged outside the P&L | 🟢 below 100% |
| Reason for rotation | NOT FOUND | 🟡 |

Source: II.8a p.240.

### 1F Standalone vs consolidated
No subsidiaries, no parent (Annexure V vii p.244). Group entities (Extreme Covet, Gostocks Fintech, Gee Gee, The Style Salad, Shah Infotech, Shah Electronics, Shah Trading) are not consolidated (p.212).

**Phase 1 summary:** The auditor's work is a restatement certificate. It records one policy restatement and no qualification. It tells us nothing about KAMs or CARO.
**Phase Verdict: 🟡 Watch (limited visibility, not adverse).**
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because no qualification, going concern language or fraud reference appears; the gap is missing documents, not adverse content.

---
# PHASE 2: NOTES TO FINANCIAL STATEMENTS

## 2.0 Verification of the B02 Top 15 against the document

| Rank | B02 finding | My check | Status |
|---|---|---|---|
| 1 | CFO 762.30 = 56.4% of PAT 1,350.77; 3-yr 38.8% | 762.30 / 1,350.77 = 56.43%; 966.82 / 2,490.18 = 38.83% (p.228) | ✓ verified |
| 2 | Non-gov 4,733.92 unnamed; 82.7% of growth; two lines 99.97% | 82.65% (p.29); Forensic Science +2,051.56 plus Cyber +2,015.78 = 4,067.34 of 4,068.59 = 99.97% (p.24) | ✓ verified (new mechanism in 0.1) |
| 3 | 130.54 at 2-3 yrs; 20.7% provided; 4.76 collected; anomaly 26.27 | 27.00 / 130.54 = 20.7%; FY25 1-2y 135.30 less FY26 2-3y 130.54 = 4.76; anomaly reproduced: FY25 1-2y bucket 135.30 exceeds FY24 6m-1y bucket 109.03 by 26.27, which cannot happen by ageing alone (p.235). Unprovided 103.54 = 5.7% of PBT | ✓ verified |
| 4 | Days 83/89/74 average; year-end 144/111/79; ex-cash WC days 97/73/78, no improvement in FY26 | Days ✓. **Working capital days: basis problem** | ✗ discrepancy 1 |
| 5 | RPT stack 384.19 ex-loans; RPT payables 90.34 to 2.65 | Sum of FY26 lines = 281.35 + 1.24 + 67.00 + 0.18 + 23.00 + 7.88 + 2.04 + 1.50 = 384.19 (3.63% of revenue). Payables 0.28 + 27.47 + 36.82 + 10.80 + 14.94 + 0.03 = 90.34; FY26 2.65 (pp.250-251) | ✓ verified |
| 6 | Software capitalised share 0 / 59.6 / 82.6%; CWIP 137.17 | 72.70 / (72.70 + 49.25) = 59.6%; 75.47 / (75.47 + 15.85) = 82.6%; 75.47 / 1,821.45 = 4.1% of PBT (pp.237, 240). "Purpose NOT FOUND" is revised: p.152 names two outsourced prototypes | ✓ numbers; ✗ minor on "purpose" (discrepancy 4) |
| 7 | Gross margin 37.3 / 31.2 / 27.1%; lease cost 160.78 to 22.48 = 15.4% of EBITDA growth | (7,711.08 COGS FY26) 27.06%; (127.48 - 22.48 = 105.00) / (1,906.49 - 1,224.89 = 681.60) = 15.4% (pp.227, 239) | ✓ verified |
| 8 | Unearned revenue 166.50 first in FY26; advances 22.18 vs claim of 30-50% | Figures ✓ (p.234). The claim is worded two ways: "advance payments of 30% to 50% at delivery" (p.92) and "30% to 50% of receivables are collected at the time of delivery" (p.97). The second is a collection claim, not an advance liability | ✓ with framing note |
| 9 | Statutory defaults; advance tax 191.42; interest 10.21 and 1.89; Annexure IX blank | 43,24,387 + 1,29,80,286 + 18,37,147 = 1,91,41,820; interest 10,21,139 and 1,89,474; Annexure IX line M blank FY25/FY26; FY24 current tax 102.42 vs 97.90 (pp.25-27, 252) | ✓ verified |
| 10 | Promoters took ~89% of Rs 20 "placement"; 94,918 shares transferred FY25 at undisclosed price | The Rs 20 issue was a **rights issue (5:1) on 12-Mar-2024**, not a placement. Promoters took 10,15,300 + 3,12,500 + 1,23,750 = 14,51,550 of 16,00,050 = 90.7% (pp.80-81). The 94,918 transfers have disclosed terms: 31,639 sold for cash at **Rs 569**, 63,279 **gifted** (p.80-81) | ✗ discrepancy 2 |
| 11 | Guarantees incl. Bina and Saloni Shah; BG 592.85 = 14.3% of net worth; tax disputes 14.87 outside contingent table | BG 592.85 / 4,140.67 = 14.32% ✓. Litigation: **23 tax cases, 19.37 lakh** (IT 5 / 8.55, TDS 17 / 4.54, GST 1 / 6.28) in the legal section (p.274, RF17 p.35) vs 6 cases, 14.87 in Annexure V xiv (p.244) | ✗ discrepancy 3 |
| 12 | ROCE spot-year; cash 31.8% of equity | 1,858.15 / 4,140.67 = 44.87%; 1,188.57 / 3,115.51 = 38.15%; 511.65 / 1,309.70 = 39.07% (pp.245, 257). Cash 1,316.32 / 4,140.67 = 31.8%; ex-cash capital 2,824.35 gives 65.8% | ✓ verified |
| 13 | Contradiction cluster | MD&A "Ind AS" (p.264) vs AS (p.229); "proceeds from short-term borrowings 325.61" (p.268) vs repayment (p.228); "not seasonal" (p.270) vs 51% (p.92); "volume" growth (p.270) vs customers 128 to 95 (p.23); FD interest (p.265) vs no FD (p.236); PF sentence (p.231). All reproduced | ✓ verified |
| 14 | Zero debt; MD loans 1,249.73 over FY24-26; MSME interest nil; CSR met; intra-year interest 11.95 | 560.15 + 587.69 + 101.89 = 1,249.73 (p.250); interest 13.99 - 1.18 - 0.86 = 11.95 (p.239, p.250) | ✓ verified |
| 15 | AS, auditor change, FY24 restatement 287.16 to 283.47, no going concern | p.222, p.249 | ✓ verified |

**Triple-pass verification result: 12 of 15 verified clean; 3 with discrepancies (ranks 4, 10, 11), plus two minor corrections inside ranks 6 and 8.**

### Discrepancy 1 (rank 4): working capital days basis
- B02 uses total current liabilities including short-term borrowings as an operating liability. That gives ex-cash days 97.1 / 72.8 / 78.4 (FY24/FY25/FY26) and the statement "did not improve in FY26".
- Borrowings are financing, not operating liabilities. Ex-cash and ex-borrowings, year-end: current assets less cash 1,716.81 / 3,165.10 / 4,155.36; operating current liabilities 598.93 / 1,542.40 / 1,884.55; net 1,117.88 / 1,622.70 / 2,270.81; days on revenue **135.2 / 91.1 / 78.4** (computed, p.226, p.227). FY26 improved by 12.7 days on this basis.
- Company KPI "net working capital days" 98 / 141 / 124 (p.257) includes cash and uses total current liabilities, and also improves in FY26 (141 to 124).
- Conclusion: "operating working capital did not improve" is basis-dependent and should not be carried forward. What is true on every basis: working capital still absorbed 21.3% of incremental revenue in FY26 and 19.5% in FY25 (computed, p.228), and the FY27 plan needs 4,442.00 against 3,587.14 (p.89-90).

### Discrepancy 2 (rank 10): promoter share movements
- FY24 issue: rights issue 5:1 at Rs 20, 12-Mar-2024, 16,00,050 shares, 320.01 lakh (p.80, p.90). B02 called it a placement.
- FY25: promoters' 94,918 share transfers (Shah 84,372 + Hinduja 10,546) on **13-Jan-2025**: cash sales of 31,639 shares at Rs 569 (Rs 180.03 lakh, computed) to named transferees, and **gifts of 63,279 shares** by the MD, 21,093 each to Vishal Jain, Sangita Malay Mehta and Sunita A Shah (p.80-81). The sale price equals the Dec-2024 placement price (p.25, RF16).
- Vishal Jain became CFO on 01-Aug-2025 (p.201) and holds 1,68,744 shares post bonus (1.00%, p.203), worth Rs 151.87 lakh at the IPO price of Rs 90 (computed) against a stated fixed pay of Rs 30 lakh (p.201). See Phase 5.

### Discrepancy 3 (rank 11): litigation counts
Annexure V xiv lists 6 tax cases and 14.87 lakh (p.244). The legal section and RF17 list 23 tax cases and 19.37 lakh, including 17 TDS cases of 4.54 lakh that Annexure V omits, and income tax 8.55 vs 8.59 (p.274, p.35). The difference is small in rupees (0.47% of net worth, computed) and large as a controls signal: two tables in one document disagree on case count by a factor of four.

### Discrepancy 4 (rank 6 minor): software CWIP purpose and amortisation
- B02: "purpose NOT FOUND". p.152 names two software platforms started in FY26 and outsourced to a third party on Kwick's concept: AI-Powered Judicial Assistance Platform Rs 42.37 lakh and LIMS Rs 6.35 lakh (total 48.72). It does not say these are the CWIP lines.
- B02 amortisation "about 35.6 a year": the policy life is 10 years (p.230), which gives 13.7 per year (137.17 / 10, computed). B02's figure is not reproduced.
- Reconciliation attempt [INFERENCE]: CWIP 137.17 = Gostocks purchased software 78.70 (58.70 FY25 + 20.00 FY26, p.250) + outsourced prototypes 48.72 + 9.75 other (computed). FY25 CWIP of 61.70 is roughly Gostocks 58.70 plus 3.00, and it predates the stated FY26 start of the E-Forensics and platform development (p.151-152). So the oldest half of the asset is not the programme the prospectus describes. Confirming observation: the CWIP vendor and function schedule.

## 2A Accounting policy aggressiveness

| Area | Policy (anchor) | Assessment |
|---|---|---|
| Revenue | AS 9. Single performance obligation on delivery or commissioning; POC (cost-to-cost or milestone) where installation is essential (pp.229-230) | 🟡 Judgement left open; POC value NOT FOUND; no disclosure of which contracts use POC |
| Rental | Straight line over agreement (p.229) | 🟢 |
| Depreciation | WDV on Schedule II lives: computers 3, P&M 15, vehicle 8, intangible 10 (p.230) | 🟡 15-year life on handheld X-ray scanners (164.50 added FY26) and 10-year life on software are long for tech assets |
| Inventory | Lower of cost or NRV; no ageing provision (p.229) | 🟡 Inventory 1,043.71 insured for 470.00 (45.0%) (p.43) |
| Capitalisation | Intangible includes "any directly attributable expenditure"; no AS 26 research vs development test stated (p.230). Borrowing cost capitalised only for qualifying assets; none capitalised | 🟡 Prototype costs of an AI platform sit in CWIP |
| Impairment | Standard (p.230) | 🟢 |
| Doubtful debts | No ECL matrix (AS basis); provision 31.94 on 2,320.01 gross = 1.4% (p.235) | 🟡 |
| Lease | AS 19 basis (Indian GAAP). Machine lease cost 22.48 expensed in purchases. "Ind AS 116" is irrelevant here (p.264 wrongly cites Ind AS) | 🟡 Machine lease cost fell 160.78 to 22.48 while rental revenue rose 671.33 to 925.41 |
| Policy changes | Gratuity cash to AS 15, FY24 only, 4.93 (p.249). Provident fund sentence says "has not deducted any amount" (p.231) while 23.26 was charged | 🟡 |

## 2B Related-party map (Annexure VIII pp.250-251; Rs lakh; % of FY26 revenue 10,571.28)

| Counterparty and role | FY24 | FY25 | FY26 | FY26 % revenue | Signal |
|---|---|---|---|---|---|
| Managerial remuneration (6 persons) | 44.40 | 185.60 | 281.35 | 2.66% | +51.6% FY26; 20.8% of PAT (computed) |
| Sitting fees (Vaid, Venkatesh) | 0 | 0 | 1.24 | 0.01% | |
| Goods from Shah Infotech / Shah Electronics / Shah Trading / The Style Salad | 0.42 | 53.43 (incl. Extreme Covet 31.20) | 67.00 | 0.63% | 0.90% of FY26 purchases 7,446.06 (computed) |
| Gostocks Fintech: software asset + fees | 6.50 | 58.95 | 23.00 | 0.22% | Capitalised; see below |
| Rent to MD | 0 | 15.00 | 7.88 | 0.07% | FY26 = 4.5 months x 1.75 (ties, p.210); annualised 21.0 |
| Interest on loans from MD, wife, Extreme Covet, Gee Gee | 96.17 | 20.38 | 2.04 | 0.02% | FY24 = 81% of FY24 interest expense 118.33 (computed) |
| Commission to promoter's sister | 7.00 | 3.50 | 1.50 | 0.01% | Declining |
| Loans borrowed, MD / Sejal / Extreme Covet / Gee Gee | 795.38 | 684.81 | 114.46 | n/a | MD net borrowed 1,249.73 over 3 years; FY26 balance nil |
| Trade payables to related parties | 4.28 | 90.34 | 2.65 | n/a | Related parties financed FY25 stock build |

**Value-extraction and dependency tests (new, computed from group-entity financials p.213-219 against Kwick payments):**

| Group entity | Entity FY25 turnover incl. other income | Kwick FY25 payments | Kwick share of entity turnover |
|---|---|---|---|
| Gostocks Fintech (software for financial-market education, p.214) | 94.64 | 58.70 + 0.25 = 58.95 | **62.3%** |
| Extreme Covet (e-commerce beauty, p.212) | 64.57 (FY24: 11.70) | 31.20 goods | **48.3%** |
| The Style Salad (subscription boxes, p.216) | 95.50 | 7.97 + 2.90 = 10.87 | 11.4% |
| Shah Infotech | 206.68 | 13.91 + 0.02 = 13.93 | 6.7% |

- [INFERENCE] Kwick is the dominant customer of two promoter-group firms, and neither firm's stated business is forensic equipment. Two readings: genuine niche supply (a training-software house builds a simulator; an e-commerce firm supplies gifting or kit components), or a path for cash to reach promoter-group entities at prices that cannot be checked. Observation that separates them: what Gostocks built (the CWIP vendor schedule) and how Extreme Covet's goods were used.
- No arm's-length evidence is offered (RF32 p.42: "it is difficult to ascertain whether more favourable terms would have been achieved"). FY26 group financials NOT FOUND (group data stops at FY25).
- Guarantors Bina Sanjay Shah and Saloni Shah are not in the RPT list, though they personally guarantee the IOB facilities (p.234). They resigned as directors on 20-Aug-2025 "unable to devote adequate time" (p.194). Both are promoter-group holders of 4,75,200 shares each (p.79).

## 2C Contingent liabilities
| Item | Amount | % net worth 4,140.67 | % PAT 1,350.77 | Flag |
|---|---|---|---|---|
| Performance bank guarantees | 592.85 (FY25 394.20, FY24 119.82) | 14.32% | 43.89% | 🟡 above the 10% line, below 25% |
| Tax disputes (legal section) | 19.37 | 0.47% | 1.43% | 🟢 |
| Civil: independent director defamation suit (not a company claim) | 100.10 claimed | n/a | n/a | see Phase 5 |

- BG rose 4.9x in two years against revenue 3.5x (computed). Sanctioned LG limit is 800.00 (IOB, p.234, p.255): headroom 207.15 (25.9%). If BG scales with FY27 revenue (+40% implied), the need is about 830 and exceeds the limit (computed). This is not in any risk factor.

## 2D Receivables (Note I.14 p.235)
| Item | FY24 | FY25 | FY26 |
|---|---|---|---|
| Gross | 1,193.58 | 2,010.39 | 2,320.01 |
| Provision | 0 | 31.34 | 31.94 |
| Net | 1,193.58 | 1,979.05 | 2,288.07 |
| < 6 months | 1,046.53 | 1,669.30 | 2,045.06 |
| > 6 months share | 12.32% | 16.97% | 11.85% |
| 2-3 years bucket | 0.95 | 6.66 | 130.54 |
| Provided on 2-3 years | 0 | 6.66 (100%) | 27.00 (20.7%) |
| Days, average basis / year-end | 83 / 144 | 89 / 111 | 74 / 79 |
| Top customer share of revenue | 22.24% | 19.02% | 23.59% |
| Unbilled | NOT FOUND | NOT FOUND | NOT FOUND (unearned revenue 166.50 on the liability side) |

Receivables are 37.8% of FY26 total assets (2,288.07 / 6,053.09, computed). Receivable split by buyer type NOT FOUND.

## 2E Inventory
Inventory is "Traded Goods" only: 328.73 / 756.63 / 1,043.71 (I.13 p.235). No raw material, WIP or finished goods lines, although the business assembles kits and fabricates vehicles (fabrication charges 196.07, p.239). FY26 inventory +37.9% vs revenue +62.6%. Days: company 62 / 44 / 43 on average inventory (p.91); year-end 63.4 / 61.7 / 49.4 (computed). No write-down disclosed. FY25 build of "400 lakh for DNA equipment" (p.267).

## 2F Borrowings
| Item | FY24 | FY25 | FY26 |
|---|---|---|---|
| Total borrowings | 323.71 | 325.61 | 0 |
| of which related parties | 123.32 | 267.93 | 0 |
| Maturity wall | all current or on demand | all current or on demand | none |
| Covenants near breach | NOT FOUND | NOT FOUND | none (no debt) |
| Pledge of promoter shares | none (p.85 item 30; p.84) | | |
| ICDs given | none (Annexure V ix) | | |
| Facilities | IOB cash credit 200.00 undrawn; LG 800.00 drawn 592.85; NSIC term loan 150.00 sanctioned, nil | | p.255 |

Security: current assets hypothecated; collateral is a property owned by Sejal Shah and Shammer Shah, with personal guarantees of four family members (p.234). Peak intra-year borrowing NOT FOUND; finance cost 36.71 includes 22.72 "other borrowing cost" (BG commission and charges) (p.239).

## 2G Deferred tax
DTA 24.85 / 23.58 / 8.95. FY26 movement (1.28): gratuity (2.37), bad debt (0.15), depreciation 1.25 (p.241). Effective tax rate 25.13% / 23.65% / 25.84% (computed) against 25.17% statutory under s.115BAA (p.252). The FY25 rate is low because issue expenses of 72.22 were deducted in the tax computation (p.252).

## 2H Exceptional items, goodwill, ESOP, leases, post balance sheet
- Exceptional items: none in any year (p.227). Goodwill: none. ESOP: none (p.204).
- Leases: registered office 11 months from 21-Sep-2025 to 20-Aug-2026, renewed 11 months; branch office (R&D, demonstration centre, proof-of-concept lab) rented from the MD at 1.75 lakh per month to 30-Sep-2026 (pp.30-31, p.210). Both are short term. The renewal of the MD-owned branch lease was open when the prospectus was signed.
- Post balance sheet: none material (p.274). Items dated after 31-Mar-2026 that matter: RoC adjudication order 30-Jun-2026 penalty Rs 2.00 lakh on the company and Rs 0.50 lakh on the MD under s.450, paid in July 2026 (p.28); Audit Committee and NRC constituted 04-Jul-2026 (p.196, p.198); Dr Mukesh appointed 04-Jul-2026 (p.187); DPT-3 filed 17-Jun-2026, 352 days late (p.38).

**Phase 2 summary:** B02 holds up on 12 of 15 items. The three corrections are basis, share-transfer facts, and a litigation count. New material: promoter-group suppliers that depend on Kwick for 48% to 62% of their turnover, and software CWIP that is half a related-party purchase.
**Cross-reference with Phase 1 KAM areas:** revenue recognition, receivable provisioning and software capitalisation are the three judgement areas, and all three are 🟡 here. This agrees with the B02 score.
**Reconciliation with B02 accounting quality score 5/10:** I score 5/10 on the same dimensions. The software CWIP and promoter-group dependency findings pull down; the verified, uncontested cash flow statement and clean FY25-FY26 restatements pull up. No change.
**Phase Verdict: 🟡 Watch.**
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because no restated FY25 or FY26 number is adjusted and the issues are policy opacity and related-party structure, not misstatement.

---
# PHASE 3: FINANCIAL STATEMENTS (cash flow, then balance sheet, then P&L)

## 3A Cash flow (Annexure III p.228, Rs lakh)

| Line | FY24 | FY25 | FY26 |
|---|---|---|---|
| Operating profit before WC | 541.57 | 1,242.34 | 1,910.41 |
| Trade payables | 149.83 | 717.33 | (172.01) |
| Other current liabilities | 68.92 | 80.21 | 338.60 |
| Inventories | (9.40) | (427.90) | (287.08) |
| Trade receivables | (1,012.79) | (785.47) | (309.02) |
| Other current assets | 21.64 | (234.93) | (394.15) |
| Other non-current assets | 41.53 | (28.60) | (42.71) |
| Cash from operations | (198.70) | 562.98 | 1,044.04 |
| Tax paid | (61.87) | (97.90) | (281.74) |
| **CFO** | (260.57) | 465.09 | 762.30 |
| Purchase of tangibles + intangibles | (49.52) | (38.92) | (206.59) |
| Increase in CWIP (software) | 0 | (61.70) | (75.47) |
| Free cash flow after capex and CWIP | (310.09) | 364.47 | 480.24 |
| FCF before CWIP (B01 basis) | (310.09) | 426.17 | 555.71 |
| Interest paid (in financing) | (115.65) | (114.29) | (53.98) |
| CFO after interest | (376.22) | 350.80 | 708.32 |
| Equity raised, net | 320.01 | 947.97 | 0 |
| Borrowings net | (290.97) | 1.90 | (325.61) |
| Net change in cash | (387.40) | 1,203.28 | 109.54 |

- CFO / PAT 56.4%, CFO / EBITDA 40.0% (above). Capex (tangibles plus intangibles) to depreciation 1.51x / 1.07x / 4.27x; including software CWIP 1.51x / 2.77x / 5.83x (computed). No M&A.
- **CFO quality checks:**
  1. One-time inflators: other current liabilities +338.60 in FY26 includes statutory dues payable up from 38.91 to 183.03 (+144.12, GST on March sales per p.98) and unearned revenue +166.50 (p.234). The 144.12 reverses within a quarter. Without it CFO is 618.18, or 45.8% of PAT (computed).
  2. Payable stretching: FY25 CFO includes +717.33 from payables (MSME payables 20.00 to 587.50). Without it FY25 CFO is (252.24). FY26 unwound 172.01, so FY26 CFO is not inflated by payables. Related-party payables fell from 90.34 to 2.65.
  3. Inventory and receivable build absorbed 596.10 in FY26 and 1,213.37 in FY25 (computed).
  4. Interest classification: interest paid sits in financing, so CFO is before interest. After interest FY26 is 52.4% of PAT.
  5. Tax: B02's withdrawn "unpaid tax" claim stays withdrawn. FY26 tax paid 281.74 equals the FY25 provision 279.80 plus 1.93 earlier-year tax (computed). The FY26 advance tax sits in other current assets (balance with authorities 453.05 vs 218.60, p.236).
- Working capital absorbed 21.3% of incremental revenue in FY26 (866.37 / 4,068.59) and 19.5% in FY25 (679.36 / 3,484.36) (computed).
- Cash pile: 3.50 / 1,206.79 / 1,316.32, all in bank current accounts and cash (p.236). Interest income 8.94 on an average balance of 1,261.56 is a 0.71% yield (computed). [INFERENCE] The balance is either a year-end snapshot of collections or idle; MD&A calls the income "interest on fixed deposits" (p.265) but there are no fixed deposits. Observation: interest income and any FD line in H1 FY27.
- Financing: FY26 repaid 325.61 and paid interest 53.98 from CFO. External equity raised across FY24-FY25 was 1,267.98 against cumulative PAT of 2,490.18.

## 3B Balance sheet (Annexure I p.226) and ratios

| Rs lakh | FY24 | FY25 | FY26 | Comment |
|---|---|---|---|---|
| Net worth | 985.99 | 2,789.90 | 4,140.67 | Bonus 7:1 on 16-Sep-2025 used 386.50 of surplus and 1,090.05 of premium (p.233) |
| Borrowings | 323.71 | 325.61 | 0 | |
| Trade payables | 325.24 | 1,042.57 | 870.56 | MSME 402.30 |
| Other current liabilities | 166.60 | 199.97 | 521.29 | Statutory 183.03; unearned 166.50 |
| Short-term provisions | 107.09 | 299.86 | 492.69 | Tax 470.02 plus gratuity 22.68 |
| PPE net / CWIP / intangible | 143.77 / 0 / 0 | 136.58 / 61.70 / 9.38 | 293.45 / 137.17 / 6.95 | Scanners 164.50 added FY26 |
| Inventory | 328.73 | 756.63 | 1,043.71 | |
| Receivables | 1,193.58 | 1,979.05 | 2,288.07 | 37.8% of assets FY26 |
| Cash | 3.50 | 1,206.79 | 1,316.32 | 21.7% of assets |
| Other current assets | 194.49 | 429.42 | 823.58 | Balances with authorities 453.05; deposits 190.10 |
| Security deposits non-current | 41.48 | 70.08 | 112.79 | Counterparties NOT FOUND |
| Total assets | 1,918.77 | 4,678.96 | 6,053.09 | |

| Ratio | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|
| D/E | 0.33 | 0.12 | 0.00 | p.245 |
| Net debt / EBITDA | 0.59x | (0.72x) | (0.69x) | computed |
| Current ratio | 1.88 | 2.34 | 2.90 | p.245 |
| Quick ratio | 1.52 | 1.94 | 2.35 | computed |
| EBIT / finance cost | 3.85x | 17.62x | 50.62x | computed |
| ROCE (company) | 39.07% | 38.15% | 44.88% | p.245; reproduced on closing capital; spot-year |
| ROE (average equity) | 41.43% | 45.34% | 38.98% | p.245 |
| Return on net worth (closing) | 28.75% | 30.68% | 32.62% | p.248 |
| Goodwill / net worth | 0 | 0 | 0 | |

DuPont, FY26 (average balances, computed): PAT margin 12.78% x asset turnover 1.97 x equity multiplier 1.55 = 38.99%. FY25: 13.16% x 1.97 x 1.75 = 45.3%. ROE is operational and not leverage-driven. The FY26 fall is equity bloat from placement cash, and leverage fell. ROCE is a spot-year figure on a base where cash is 31.8% of equity. Per CLAUDE.md and B02, do not feed this to Section 1B as durable ROCE.

## 3C P&L (Annexure II p.227)

| Rs lakh | FY24 | FY25 | FY26 | YoY FY25 | YoY FY26 |
|---|---|---|---|---|---|
| Revenue | 3,018.33 | 6,502.69 | 10,571.28 | +115.4% | +62.6% |
| Other income | 7.87 | 4.86 | 9.06 | | |
| Materials consumed | 1,901.88 | 4,905.05 | 7,998.16 | +157.9% | +63.1% |
| Change in inventories | (9.40) | (427.90) | (287.08) | | |
| Employee benefit | 176.24 | 388.94 | 495.85 | +120.7% | +27.5% |
| Finance cost | 133.02 | 67.45 | 36.71 | -49.3% | -45.6% |
| Depreciation | 32.85 | 36.33 | 48.34 | | |
| Other expenses | 412.97 | 416.57 | 466.91 | +0.9% | +12.1% |
| PBT | 378.64 | 1,121.12 | 1,821.45 | +196.1% | +62.5% |
| Tax (current + deferred + earlier year) | 95.17 | 265.18 | 470.67 | | |
| PAT | 283.47 | 855.94 | 1,350.77 | +202.0% | +57.8% |
| Gross margin on revenue less COGS | 37.30% | 31.15% | 27.06% | | |
| EBITDA margin | 18.04% | 18.84% | 18.03% | | |
| PAT margin | 9.39% | 13.16% | 12.78% | | |
| Other expenses % revenue | 13.68% | 6.41% | 4.42% | | |

- Margin waterfall FY26: gross profit 2,860.20 (27.06%) less employee 495.85 and other 466.91 gives about 1,897.44, plus other income 9.06 gives EBITDA 1,906.49 less depreciation 48.34 less finance 36.71 gives PBT 1,821.45. The EBITDA margin held flat by operating leverage on other expenses (13.68% to 4.42% of revenue) while gross margin lost 10.2 points. MD&A attributes the cost lines to fixed overheads (p.266) but gives no reason for the gross margin fall; RF13 (p.32) attributes the purchase-ratio rise to the cyber mix (23.18% to 33.32% of revenue).
- Other income is 0.5% of PBT (9.06 / 1,821.45), far below the 20% flag.
- Employee cost: salaries and wages 165.33 (+2.2%) while managerial remuneration is 281.35 (+51.6%); managerial pay is 56.7% of employee cost (computed, p.239).
- Tax rate consistent with 25.17% except FY25 (issue-expense deduction).
- EPS: basic and diluted are equal (no dilutive securities, p.204). The face of the P&L prints 8.00 / 43.31 / 68.59 and "adjusted" 8.00 / 5.41 / 8.57 (p.227, p.242); the unadjusted FY24 and FY25 figures are not restated for the 7:1 bonus in the headline row. Post-IPO share count 2,14,35,951 gives FY26 EPS Rs 6.30 (computed); at the screener price of Rs 178.8 that is 28.4x, which ties to the screener P/E of 28.3 in the step-1 brief. At the pre-IPO share count the multiple is 22.4x (price non-anchored).
- Other expense items to chase: commission 111.22 (+103.5%, payees NOT FOUND, p.240); rates and taxes 18.65 vs 0.02; exhibition 31.62 vs 5.34; contract services 43.27 vs 10.32; R&D 6.98 (0.07% of revenue) against "DSIR-recognised R&D capabilities" in the deck (deck p.5).

**Phase 3 summary:** Profit is real in the books and grows. Cash does not follow at the same rate: 56% of PAT, 40% of EBITDA, with a GST timing item inside FY26. Balance sheet is clean at year end. Margin held by overhead leverage while product margin fell.
**Cross-reference:** Phase 1 and 2 flags on receivables, capitalisation and related parties all show up here. FY26 capex of 282.06 (tangibles plus CWIP) is 5.8x depreciation, and 164.50 of it is scanners whose rental revenue exists from FY24 (p.239), before the owned scanners arrived.
**Phase Verdict: 🟡 Watch. FLAG-CASH stays raised.**
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because cash conversion is weak but positive, borrowings are nil and no restatement affects FY25 or FY26; the reviewer would want the H1 FY27 CFO before sizing.

---
# PHASE 4: RISK FACTORS AND MD&A

## 4A Disclosed risks, real vs boilerplate

| RF | Subject | Assessment |
|---|---|---|
| 1 | Bihar and Gujarat concentration | REAL. Bihar 34.53 / 21.80 / 9.02%; Gujarat 22.77 / 20.07 / 29.39% (p.23). Top-two share 57.3% to 38.4% (computed) |
| 2 | No long-term agreements; LDs paid FY24 to AIG Police Odisha | REAL. Contradicted by RF30 (below) |
| 3 | Revenue from goods and services | BOILERPLATE with real table (p.24) |
| 5, 18, 20 | Late TDS, GST, EPF, ESI, RoC filings | REAL and detailed; cause stated as no CFO or CS and weak controls (pp.25-39) |
| 6 | Supplier concentration: top 1 = 3,268.40 (40.86%) FY26 vs 237.80 (12.50%) FY24 | REAL. Names withheld |
| 7 | Business run outside the main objects clause from 2015 to April 2025; RoC penalty | REAL. Not mentioned in the MD&A |
| 8 | Imports 34.58% to 8.65% of purchases | REAL, falling |
| 9 | Negative cash flows in the past | REAL; table shows positive FY25 and FY26 (p.29) |
| 10 | Government dependence 86.98% to 55.22% | REAL but silent on the dealer channel (see 4B) |
| 11 | Working capital intensity: need 3,587.14; FY27 4,442.00 | REAL (p.29-30) |
| 12 | Rented premises including MD-owned branch | REAL |
| 13 | Purchases 70.44% of revenue; cyber mix explains the rise | REAL |
| 14 | BG 592.85 | REAL but silent on limit headroom |
| 15, 16 | BRLM SEBI order; BRLM-linked pre-IPO fund | REAL, disclosed (pp.33-34) |
| 17 | Litigation: 23 tax cases, ID defamation suit, Gee Gee suit | REAL; counts conflict with Annexure V |
| 19 | No registered trademark | REAL; products developed in-house are not protected |
| 22, 23 | One director has no qualification; certificates unavailable for WTD, COO, CS, one senior manager | REAL; affidavits only |
| 24 | Attrition 6% / 6% / 27% (FY24/FY25/FY26) | REAL but text calls it "relatively low" while FY26 is 4.5x prior (p.40) |
| 32 | Related-party transactions | BOILERPLATE: no arm's-length evidence |
| 34 | Directors have no listed-company experience | REAL |
| 36 | Insurance: stock covered 45.03% | REAL |
| 38 | No comparable listed company | REAL |
| 4, 41, 43 | Promoter acquisition cost 1.14 / 2.29 / nil; bonus shares | REAL for pricing, not business |
| 21, 25-30, 37, 39-40, 42, 44-48, issue risks 1-4, external 5-16 | OEM, approvals, support, product development, regulation, transporters, execution delays, IP, inventory, growth, key persons, industry data, dividends, price volatility, macro | BOILERPLATE |

**Internal contradiction:** RF30 says "We have not in the past encountered any delays in relation to the completion of our orders" (p.42). RF2 says liquidated damages were paid in FY24 for a delayed supply to AIG Police, Odisha (p.23). Both cannot be true.

## 4B Missing risks (obvious from Phases 1-3, absent from the risk section)

| # | Missing risk | Evidence | Likely reason for omission |
|---|---|---|---|
| 1 | Dealer and vehicle-builder channel replacing direct state sales; Rs 2,035.74 lakh of kits for 95 vehicles | p.150; segment tables p.24 do not isolate it | Presented as a strategy win, not a risk |
| 2 | Q4 loading: 51% of FY25 sales in Q4; FY26 NOT FOUND; delivery-based recognition | p.92; p.270 "not seasonal" | MD&A says not seasonal |
| 3 | No ECL rule; 130.54 stuck at 2-3 years; 27.00 provided | p.235 | Provision looks adequate on the face |
| 4 | Single-customer rental line: 925.41 (8.75% of revenue) equals one customer, at an implied 97.6% direct margin (925.41 less 22.48 lease cost) | pp.24, 160, 239 | Rental is shown as a "service" |
| 5 | Promoter-group suppliers depend on Kwick for 48% to 62% of turnover | pp.213-219 vs pp.250-251 | Disclosed as RPT, dependency not computed |
| 6 | BG limit headroom 207.15 of 800.00 versus +40% implied FY27 growth | p.234, p.255, p.95 | Not analysed |
| 7 | Audit Committee constituted 04-Jul-2026 but cited as approving KPIs on 25-May-2026 | p.196 vs p.256 | Drafting error or process gap |
| 8 | Independent director turnover: Vasudevan (withdrew 07-Sep-2025), Panchi (resigned 16-Sep-2025), Latha Venkatesh (appointed 16-Sep-2025, resigned 05-Jul-2026); the surviving two are Vaid (appointed 16-Sep-2025) and Mukesh (04-Jul-2026) | p.194 | Not a listed risk |
| 9 | Independent director Dr Mukesh is a defendant in a Madras High Court defamation suit claiming Rs 100.10 lakh (hearing 19-Aug-2026, outcome absent from a 31-Aug document); he chairs the NRC and sits on the Audit Committee | p.272, p.196 | Shown only in the litigation section |
| 10 | Promoter gifted 1.00% to the future CFO (13-Jan-2025; CFO from 01-Aug-2025) | p.80, p.201, p.203 | Not a listed risk |
| 11 | Software CWIP half is a related-party purchase; policy lacks AS 26 test; prototype costs capitalised | pp.237, 250, 230, 152 | RF27 is generic |
| 12 | Gross margin compression 37.3% to 27.1% and no stated cause beyond cyber mix | p.257 vs p.265 | MD&A is silent |
| 13 | Listed-company disclosure conduct (Reg 30 note after a price query) | announcements 26-27 Sep | Post-prospectus |
| 14 | Headcount of 33 (p.156) or 34 (p.36) runs Rs 105.71 Cr revenue; six-person sales team, four R&D staff, GM tender paid Rs 6.00 lakh; "liaisoning" is named as a growth source (p.157) while commission payees are undisclosed | pp.31, 36, 156-157, 202, 240 | Cultural, not a number |
| 15 | Promoter-family guarantees and MD-owned lease as critical dependencies | pp.210, 234 | Disclosed as facts, not risks |

## 4C MD&A deep dive

**Industry claims.** Growth is credited to BNS, BNSS and BSA (mandatory forensic examination for offences with 7 or more years) and to a Rs 30,000 crore outlay over five years (p.265). Source cited: PIB release of 03-Jan-2026. **PENDING LIVE VERIFICATION** (this container cannot reach the PIB link). Deck figures (digital forensics market $0.19 bn in 2024 to $1.39 bn by 2030, ~40% CAGR; 433 mobile forensic vans across 23 States/UTs; NFSU outlay) are external and also PENDING LIVE VERIFICATION. The CAGR arithmetic ties (7.3x over six years is 39.3% a year, computed).

**Growth and margin explanations, credit and blame.** Revenue growth is credited to legislation (an external factor) and to segment growth of 2.10x and 2.34x (pp.265-266). Costs: "purchase of goods ... in line with revenue" (p.265); finance cost down because "improved collections and thereby repaid all existing borrowings" (p.266); other expenses "fixed costs and overheads which remain unaffected" (p.266). Not explained: the fall in gross margin, the machine lease cost drop, and the 51.6% rise in managerial pay beyond "industry standards" (p.266). The Mobile CSI fall of 35.6% is explained in the business section (p.150), not in the MD&A.

**Segment analysis (p.24):**

| Segment | FY24 | FY25 | FY26 | FY26 vs FY25 |
|---|---|---|---|---|
| Forensic Science and Physical Evidence | 1,178.74 | 1,859.28 | 3,910.84 | +110.3% |
| Mobile CSI Vehicles | 405.09 | 1,640.66 | 1,056.76 | -35.6% |
| Cyber and Digital Forensics | 642.42 | 1,507.05 | 3,522.83 | +133.8% |
| DNA Forensics | 42.66 | 615.72 | 1,137.57 | +84.8% |
| Rental | 671.33 | 840.03 | 925.41 | +10.2% |
| AMC and other | 78.10 | 39.95 | 17.87 | -55.3% |

Cross-check failures: p.141 prints FY24 CSI revenue 421.37 vs 405.09 on p.24; vans sold 12 to Nagaland in FY26 (p.141) but Nagaland is absent from the state revenue table (p.159), which still sums to the total (10,571.28, computed). Segment margins NOT FOUND. Top Supplier 1 (3,268.40) is 92.8% of Cyber revenue (3,522.83) in FY26 and 87.9% in FY25 (1,325.39 / 1,507.05), against 37.0% in FY24 (computed). [INFERENCE] Cyber may be largely a one-supplier pass-through at a thin margin (RF13 says cyber has lower margins). The prospectus does not state which segment the top supplier serves. Observation: supplier identity and segment margin.

**Forward guidance table (no formal guidance exists; implied items marked):**

| Claim | Number | Timeframe | Credibility check |
|---|---|---|---|
| FY27 working capital need | 4,442.00 (receivables 3,000; inventory 1,350; payables 700) | FY27 | History: need grew 992.29 to 2,561.57 to 3,587.14; plan adds 854.86 (computed). IPO funds 3,142.00, so about 2,287 of the "use" replaces existing internal funding (computed). Medium |
| Implied FY27 revenue | about 14,797 (3,000 / 74 days x 365; implied) | FY27 | +40.0% vs +62.6% FY26; implied, not stated. Medium |
| Debtor days stabilise at 74 | 74 | FY27 | Average-basis 74 vs year-end 79 in FY26; FY25 was 89. Medium |
| Reduce Bihar and Gujarat dependence | top-two 38.4% FY26 | ongoing | Bihar fell to 9.02%; Gujarat rose to 29.39%. Mixed |
| "Improving gross margins" via domestic sourcing | domestic share 65.42% to 91.35% | past | Gross margin fell 37.3% to 27.1% (p.153 vs p.257). Low |
| E-Forensics suite (10 apps) in development | no date, no budget | from FY26 | CWIP 137.17; commissioning date NOT FOUND. Low |
| Private forensic laboratory | no capex, no date | none | Not in objects of the issue (WC 3,142.00 and GCP 464.85, p.98). Low |
| KMP commission caps | Jhaveri 0.54% (cap 29), Hinduja 0.70% (cap 40) of turnover | FY27 | Caps already bind at FY26 revenue (0.54% x 10,571 = 57; 0.70% x 10,571 = 74), so no incentive above FY26 scale (computed) |
| FY27 managerial remuneration ceiling | 315.89 (computed from pp.191-203) vs FY26 281.35 | FY27 | MD terms fall to 94 from 126.72 paid. High |

## 4D Tone and credibility (1 low to 5 high)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3 | Full RPT table, dated statutory defaults, ageing, gratuity assumptions. Absent: customer names, buyer type by product, segment margins, POC, ECL rule |
| Consistency | 2 | "Not seasonal" vs 51% Q4; "no delays" vs LDs paid; 33 vs 34 employees (p.156 vs p.36); 130 vs 95 customers (deck vs p.23); WTD joining 01-Feb-2021 (p.192) vs 01-May-2023 (p.188); MD pay 94 (p.191) vs 126.72 paid (p.200, p.250); Audit Committee dates; 23 vs 6 tax cases |
| Specificity | 3 | Day counts and WC schedule are specific; no order book, no unit prices, no tender pipeline |
| Accountability | 2 | Growth credited to law and policy; margin fall unexplained; cause of late filings stated plainly (no CFO or CS) |
| Capital allocation sense | 3 | Debt repaid, equity raised at 569 per share; but 1,316.32 cash earning 0.71%, related-party software, undisclosed lab, MD pay |

**Phase 4 summary:** The risk section is long and mostly boilerplate, with real items on concentration, controls and the BRLM. The largest risks that a reader needs (channel shift, Q4 loading, BG headroom, group dependency, board record) sit outside it.
**Contradictions vs Phases 1-3:** MD&A "business is not seasonal" vs 51% Q4; "volume" vs customers down 26%; "improved collections" vs receivables up 15.6%.
**Phase Verdict: 🟡 Watch.**
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the omissions are of analysis and emphasis; no concealed liability shows up.

---
# PHASE 5: CORPORATE GOVERNANCE AND BOARD

## 5A Board composition (p.184-188, p.194)

| Director | Role | Since | Other boards | Flags |
|---|---|---|---|---|
| Shammer S Shah, 60 | Executive Chairman and MD, promoter | 04-Mar-2005; MD term 01-Aug-2025 to 31-Jul-2028 | Gostocks Financial Services Pvt Ltd, Extreme Covet Pvt Ltd, ThinkPad Advisors LLP; also "other directorship held": Mokka Kefi & Cabana, Esource Lighting LLP, Brrain Source, Archos Techno (p.206); partner in Shah Electronics and Shah Trading (p.218) | Promoter-group cross-boards; below 8 seats |
| Sejal S Shah, 55 | Non-executive, promoter, wife of MD | 05-Sep-2014 | Extreme Covet, ThinkPad LLP | No qualification disclosed (RF22); paid 8.40 lakh a year |
| Neeraj B Jhaveri, 42 | Whole-time director and CMO | director from 19-Aug-2025 (WTD 07-Sep-2025) | none | Distant relative of MD (sister's son-in-law, p.191); joining date conflict |
| Sonia Vaid, 33 | Independent | 16-Sep-2025; regularised 22-Jun-2026 | Wildnet Technologies, SVM Infraestate, Unimarck Healthcare, United Leasing and Industries (listed); CS at Diensten Tech (listed) | Four other boards; 4 years' experience; chairs Audit Committee |
| Dr Bheekamchand Mukesh, 58 | Independent (additional) | 04-Jul-2026; shareholder approval pending | Bal Pharma (listed) | Defamation suit, Rs 100.10 lakh claimed (p.272); chairs NRC |

- Independents above 10 years: none. Attendance below 75%: NOT AVAILABLE (no AR). Board meeting count NOT FOUND.
- Independents are 2 of 5 (40%). The Companies Act floor for a listed public company is one-third, so this complies. A promoter Executive Chairman would need half independent under LODR Reg 17 on a main board, but Reg 17 does not apply to this SME company (p.196). Benchmark only.
- Independent turnover: three independent appointments ended inside ten months (p.194).

## 5B Committees (pp.196-199)
| Committee | Constituted | Members | Note |
|---|---|---|---|
| Audit | 04-Jul-2026 | Vaid (chair), Mukesh, MD Shah | MD sits on it. Cited as approving KPIs on 25-May-2026 (p.256) |
| NRC | 04-Jul-2026 | Mukesh (chair), Vaid, Sejal Shah | Wife of MD is a member |
| Stakeholders Relationship | 16-Sep-2025 | Vaid (chair), Sejal Shah, Jhaveri | |
| CSR | none; board acts (obligation below Rs 50 lakh) | | CSR 12.00 spent vs 11.55 |
| RPT committee | none; Audit Committee approves RPTs | | |

One independent, Ms Vaid, sits on all three committees and chairs two.

## 5C Compensation (Rs lakh)

| Person | FY26 paid (RPT p.250) | FY27 terms (pp.191-201) | Note |
|---|---|---|---|
| MD Shah | 126.72 | 94.00 | FY26 terms stated as 94 (11 lakh x 4 months + 6.25 x 8 = 94.00, p.191); paid 126.72, which is 32.72 (34.8%) above. Year labels in the directors table are shifted by a year |
| Sejal Shah | 8.40 | 8.40 | |
| COO Hinduja (promoter) | 77.83 incl. 25.00 variable | 60.24 + 0.70% of turnover, cap 40.00 | |
| WTD Jhaveri | 49.15 incl. pre-appointment pay | 36.00 + 0.54% of turnover, cap 29.00 | |
| CFO Jain | 17.55 (from 01-Aug-2025) | 30.00 + 15.00 incentive | |
| CS Krithika | 1.70 | 3.25 | Annual pay of a listed-company CS is Rs 3.25 lakh |
| Total managerial | 281.35 | up to 315.89 | |

- Managerial pay is 20.8% of PAT and 2.66% of revenue (computed). Promoter payroll (Shah, Sejal, Hinduja) is 212.95, 15.8% of PAT. Directors' pay (Shah 126.72, Sejal 8.40, Jhaveri 49.15) is 184.27, 10.1% of PBT, against an 11% s.197 ceiling of 200.36 on PBT as a proxy (the s.198 net profit is not disclosed; computed).
- CEO-to-median: median NOT FOUND. Average salary and wages 165.33 / 33 employees = 5.01 lakh; MD pay is 25x that (computed, indicative; the 33 includes KMP).
- Commission on turnover for Jhaveri and Hinduja pays on revenue, not on profit or cash. [INFERENCE] The caps bind at FY26 revenue, so the marginal incentive above FY26 scale is nil; the incentive to reach the cap earlier still exists.
- ESOP: none. Equity gift: 21,093 shares (pre-bonus) from the MD to Vishal Jain on 13-Jan-2025; he became CFO on 01-Aug-2025 and holds 1,68,744 shares (1.00%), worth Rs 301.71 lakh at the screener price of Rs 178.8 (non-anchored) and Rs 151.87 lakh at the issue price, against Rs 30 lakh fixed pay. Reading 1: retention and alignment of a new finance head. Reading 2: a finance head who owes his personal stake to the MD is less independent of him. Separating observation: how the audit committee evaluates the CFO's independence when it reviews financial reporting.

## 5D Shareholding

| | FY24 | FY25 | FY26 | Anchor |
|---|---|---|---|---|
| Promoters (Shah, Sejal, Hinduja) | 90.25% | 78.08% | 78.08% | pp.232-233 |
| Promoters plus group, pre-offer | | | 88.53% | p.210 |
| Post-offer promoters plus group | | | 64.65% | RF35 p.42; p.79 |
| Pledge | none (p.85 item 30; p.84) | | | |

- Selling: FY25 cash sales 31,639 shares at Rs 569 = Rs 180.03 lakh; 63,279 gifted (pp.80-81). IPO OFS: 10,80,000 shares at Rs 90 = Rs 972.00 lakh (RF31 p.42, p.276), 71.96% of FY26 PAT (computed). Of OFS shares, Sejal sells 6,48,000 (21.6% of her holding), Hinduja 2,16,000 (19.57%), Shah 2,16,000 (2.38%) (p.276). The OFS is 19.1% of the Rs 50.77 Cr issue (computed). Rights issue at Rs 20 in Mar-2024 versus placement at Rs 569 in Dec-2024 is a 28.5x step in 9.5 months (computed).
- 20% promoter contribution is locked for three years (p.82).
- FII and DII trends NOT AVAILABLE (no filing; the screener figures in the step-1 brief are non-anchored).
- FLAG-PROMOTER-PRELIM: no pledge; a modest selling pattern (FY25 sale at the placement price, gifts, and an OFS of 6.4% of equity) set against a growth narrative. Full verdict comes from B08.

## 5E Governance red-flag checklist

| Item | Finding | Rating |
|---|---|---|
| Whistleblower complaints | NOT FOUND (no vigil mechanism text) | 🟡 |
| SEBI or exchange action on company, promoters | None (p.273) | 🟢 |
| Other regulator action | RoC s.450 penalty Rs 2.00 lakh (company) and Rs 0.50 lakh (MD), order 30-Jun-2026, for running forensic business outside the objects clause since 2015 (p.28) | 🟡 |
| Late statutory filings | 9 RoC filings late, DPT-3 352 days (pp.38-39); TDS, GST, EPF, ESI, advance tax (pp.25-27) | 🟡 |
| RPT committee | Audit Committee since 04-Jul-2026 | 🟡 |
| Auditor fee ratio and level | 45.5% non-audit ratio; statutory fee Rs 2.00 lakh | 🟡 |
| CSR | Compliant; 12.00 for "construction of the college building", beneficiary unnamed | 🟢 |
| Section 143(12) | NOT AVAILABLE | n/a |
| Material subsidiary auditor | n/a, no subsidiaries | n/a |
| Experience certificates | Unavailable for WTD, COO, CS and one senior manager; affidavits only. Senior manager Mahbubani's 25.8 years are "own restaurant or freelancing" (p.202) | 🟡 |
| ID litigation | Defamation suit against Dr Mukesh | 🟡 |
| Commission payees and "liaisoning" | Commission 111.22 (+103.5%); growth "fuelled by word-of-mouth marketing and liaisoning" (p.157); payees NOT FOUND | 🟡 |
| Name and object changes | Renamed 08-Jul-2024 and 16-Sep-2024; objects clause altered 07-Apr-2025 (pp.27, 277) | 🟡 |
| Board record conflicts | Audit Committee dates; MD pay vs terms; WTD joining date | 🟡 |

**Phase 5 summary:** Nothing here is a fraud signal and no pledge exists. The pattern is an immature governance machine (committees four weeks old at filing, two independents who are young or new, one under a defamation suit), a promoter-family web around the vendor base, and a record that contradicts itself in four places.
**Phase Verdict: 🟡 Watch (upper end).**
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because there is no pledge, no regulatory bar and no qualification, but the reviewer would want the four board-record conflicts and the MD pay variance answered before signing the Mental Model.

---
# PHASE 6: FRONT MATTER (chairman's letter NOT AVAILABLE; prospectus strategy, competitive strengths and MD&A opening used)

## 6A Narrative vs reality

| # | Claim (anchor) | What the financials show | |
|---|---|---|---|
| 1 | "Company has improved collections and thereby repaid all the existing borrowings" (p.266) | Borrowings 325.61 repaid; receivables +15.6%; >6m share fell to 11.85% (p.226, p.235) | ✅ for repayment; collections improved on year-end days (144 to 79) |
| 2 | Debtor days fell to 74 "by a strategic shift in the client mix" with 30-50% collected at delivery (p.91-92, p.97) | Days improved on both bases; the mix claim cannot be tested, no buyer split | ✅ outcome, unverifiable cause |
| 3 | "Business is not seasonal" (p.270) | Q4 = 51% of FY25 sales (p.92) | ❌ |
| 4 | Revenue growth is "by and large linked to increases in the volume of business" (p.270) | Customers 128 to 124 to 95; vans sold 21 / 47 / 25; no unit data elsewhere | ❌ unverifiable, partly contradicted |
| 5 | "No competitors in a listed space", niche with high barriers (p.149) | Gross margin fell 10.2 points; customers fell 26% in FY26 | ❌ on pricing power evidence |
| 6 | In-house development and "end-to-end development and manufacturing" (p.151; deck p.11) | R&D expense 6.98 (0.07% of revenue); 4 R&D staff; "not a manufacturing unit" (p.158); inventory is traded goods only | ❌ |
| 7 | Mobile CSI revenue fell by choice: "collaborative execution model" (p.150) | Vans 47 to 25, revenue -35.6%; Rs 2,035.74 lakh of kits for 95 vehicles is not visible in any segment line | ✅ stated, ❌ not reconcilable |

## 6B Strategic priorities
| Priority (pp.150-152) | Specific | Capital allocated | Execution evidence |
|---|---|---|---|
| Scale with government forensic outlay | Partly (states, vans) | WC 3,142.00 from IPO | Revenue +62.6% |
| In-house products (CSI Pro, multispectral tablet, comparator, fuming chambers) | Named | Not in objects; R&D 6.98 | "commercialised"; 4D and 8D handhelds not yet |
| E-Forensics, 10 apps, plus AI Judicial and LIMS | Named | CWIP 137.17 (Gostocks 78.70 + outsourced 48.72, inferred) | No date, no customer |
| Reduce Bihar and Gujarat share | Quantified | n/a | Top-two share 57.3% to 38.4% |
| Private forensic laboratory (proof of concept) | Described | None | Rented MD-owned premises, demo licences only (p.31) |

## 6C Metrics showcased vs absent
Showcased: growth multiples (2.10x, 2.34x, 14.43x), debt-free, ROCE 44.88%, debtor days 74, Make in India. Absent: gross margin and segment margins, cash conversion, order book (NOT FOUND, tender-led business), receivables by buyer, rental asset base and rental price, unit prices, customer names, Q4 share, attrition cause, any FY27 guidance.

## 6D Tone and priority drift
Prior-year AR NOT AVAILABLE. Within the prospectus, the FY25 explanation emphasises CSI vehicles (4.05x) and DNA (14.43x) (p.266-267); the FY26 explanation moves to Forensic Science and Cyber (2.10x, 2.34x) and recasts the vans decline as strategy (p.150, p.265). The story follows the segments that grew.

## 6E Quiet Abandonment Check

| Opening claim (quote) | Where it should show up | Class | Materiality |
|---|---|---|---|
| "Mobile CSI Vehicles" as one of four core segments and an engine of BNSS demand (p.256, p.265) | Segment revenue and units: revenue -35.6%, vans 25 vs 47; kits for 95 vehicles Rs 2,035.74 lakh not in any segment table (p.141, p.150) | (c) hedged retreat: scale-back is named in p.150 but the replacement revenue is unplaced | High: it is the LBF-1 mechanism |
| "services line for scanner rentals/AMCs ... backed by training and after-sales support" (p.256) | AMC and other: 78.10 / 39.95 / 17.87 lakh, 0.17% of FY26 revenue (p.24) | (c) hedged retreat: recurring service income disappears while the installed base grows | Medium: no annuity in the model |
| "Proposed private forensic laboratory" (p.31, deck p.5) | Objects of the issue (WC and GCP only), capex, PPE | (b) silent drop of funding and timeline: demonstration only, demo licences, "not used for commercial sample processing" | Medium: option value, not in the numbers |
| "End-to-end development and manufacturing" (deck p.11), "in-house products commercialised" (p.151) | R&D 6.98; inventory traded goods; "not a manufacturing unit" (p.158) | (a) implicit retraction | Medium: the margin story is resale and integration |
| "E-Forensics ... under development from the start of FY 2025-26" (p.151) | CWIP: 61.70 existed at 31-Mar-2025 (p.237) | (a) implicit retraction of dates: the oldest CWIP predates the stated start | Low to medium |

**Phase 6 summary:** The narrative is mostly consistent with growth and debt repayment. It overstates seasonality, manufacturing and R&D, and it hides the channel shift inside a strategy paragraph.
**Phase Verdict: 🟡 Watch.**
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the narrative gaps are of emphasis and each can be closed by one disclosure.

---
# PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

Operator mandate: transition alpha. Backward evidence only; forward judgement belongs to stages 4, 5, 11.

| Strategy | Call | Top 3 reasons |
|---|---|---|
| **GARP** | **WATCHLIST** | 1. PAT 283.47 to 1,350.77 (2-year CAGR 118%, computed), margin steady at 18.0% EBITDA; ROCE 44.88% spot. 2. The proof gate is not fired: buyers behind 82.7% of growth are unnamed, FY26 Q4 share unknown, gross margin down 10.2 points. 3. Screener-price multiple is 28.4x on post-IPO shares (non-anchored price, computed); the multiple prices in growth that is not yet verified |
| **Turnaround** | **FAIL** (not a turnaround) | 1. Profitable every year FY21-FY26 (screener, Rs Cr: 0.80, 0.14, 1.74, 2.83, 8.56, 13.51). 2. Revenue fell 66% in FY22 (11.61 to 3.96 Cr, screener), so history is lumpy, but it is not a recovery story. 3. Backward numbers show no rung migration: gross margin falling, in-house R&D 0.07% of revenue, AMC income shrinking. Whether a climb exists is a forward question for stages 4 and 11 |
| Value + Quality | FAIL | 1. CFO / PAT 56% (cumulative 0.46x over six years). 2. Accounting 5/10, governance 4/10. 3. ROCE is high mainly because the business is asset-light and cash-heavy |
| Capex-Led Growth | FAIL | 1. Asset-light: PPE net 293.45. 2. FY26 capex 282.06 is 5.8x depreciation but only 4.7% of assets. 3. Growth is funded by working capital, not capacity |
| Cash Flow Compounder | FAIL | 1. FCF after CWIP 480.24 on PAT 1,350.77. 2. Two negative CFO years in six (FY22, FY24). 3. Working capital absorbs 21.3% of incremental revenue |
| Contrarian | FAIL | 1. IPO subscribed 154.9x and price near double issue (step-1 brief, non-anchored). 2. No out-of-favour element. 3. No analyst coverage yet, but sentiment is hot |
| Insider Confidence | WATCHLIST | 1. No pledge; promoters keep 64.65% after offer. 2. OFS of Rs 972.00 lakh, FY25 sales at 569, gifts. 3. No open-market buying (listed a month); trading window closed from 01-Oct-2026 |
| Guidance Divergence | WATCHLIST (nothing to diverge from) | 1. No guidance filed. 2. Implied FY27 revenue about 14,797 from the WC plan (+40.0%), a slowdown from +62.6%. 3. First results (H1 FY27) will set the baseline |

Best-fit: GARP on the watchlist until the proof gate fires (named buyers, Q4 share, CFO conversion above 0.8).

---
# PHASE 8: FINAL VERDICT DASHBOARD

## Company snapshot (Rs lakh unless stated)
Forensic equipment reseller and integrator for state police and forensic labs; Chennai; Indian GAAP; BSE SME, listed 03-Sep-2026 at Rs 90. FY26 revenue 10,571.28 (+62.6%), EBITDA 1,906.49 (18.03%), PAT 1,350.77, CFO 762.30, cash 1,316.32, borrowings nil, net worth 4,140.67, 33 to 34 employees. Government share 55.22%. Top 10 customers 77.64%. IPO Rs 50.77 Cr (fresh 41.05, OFS 9.72); promoters 64.65% after.

## Phase verdict table
| Phase | Verdict | Note |
|---|---|---|
| 1 Auditor and CARO | 🟡 | Examination report only; no KAMs, no CARO |
| 2 Notes | 🟡 | B02 holds on 12 of 15; three corrections |
| 3 Financial statements | 🟡 | CFO 56% of PAT; GST timing inside FY26 |
| 4 Risks and MD&A | 🟡 | Real risks outside the risk section |
| 5 Governance | 🟡 (upper) | Four record conflicts; pay above terms |
| 6 Front matter | 🟡 | Channel shift, manufacturing claim, seasonality |
| 7 Strategies | GARP WATCHLIST | Proof gate not fired |

## Quality score: 5.3 / 10 (four equal components)
| Component | Score | Basis |
|---|---|---|
| Governance | 4 | Pay 34.8% above stated terms; Audit Committee date conflict; independent-director churn and litigation; objects-clause breach; group dependency; no pledge, full RPT list |
| Accounting quality | 5 | Matches B02. Policy opacity, software CWIP, no ECL rule; offsets: clean FY25-FY26 restatements, footing cash flow |
| Balance sheet | 7 | Zero debt, net cash, current ratio 2.90; offsets: receivables 37.8% of assets, BG 14.3% of net worth, cash earning 0.71% |
| Earnings quality | 5 | PAT real and growing; CFO 40% of EBITDA; gross margin 27.1%; 82.7% of growth from unnamed buyers |

## Top 3 strengths
1. Debt-free with net cash 1,316.32 and current ratio 2.90 (p.226, p.245); 325.61 repaid in FY26 from operations.
2. Year-end receivable days improved 144 to 111 to 79 while revenue grew 3.5x (computed); EBITDA margin held at 18.0%.
3. Granular disclosure where the law requires it: dated statutory defaults, full RPT table, ageing, and a small, fully repaid promoter loan book.

## Top 3 red flags
1. **Cash conversion 56.4% of PAT (40.0% of EBITDA), with 144.12 of FY26 CFO from GST timing.** FLAG-CASH.
2. **Buyers behind 82.7% of growth are unnamed, and the filing shows a dealer and vehicle-builder channel (Rs 2,035.74 lakh, 43.0% of non-government revenue) that is not placed in any segment.** FLAG-CUSTOMER-ID.
3. **Governance and disclosure record:** promoter-group vendors that rely on Kwick for 48% to 62% of turnover and supplied half of the software CWIP; Audit Committee approval dated before the committee existed; MD pay 34.8% above stated terms; a Reg 30 note one day after saying there was nothing to disclose.

## Key monitorables for next quarter (H1 FY27 results, due after the 01-Oct-2026 window closes)
| Metric | Threshold | Where | Why |
|---|---|---|---|
| H1 FY27 CFO / PAT | at or above 0.8 (FY26 0.56) | Cash flow statement in H1 results | Tests whether IPO money fixes conversion |
| Year-end style receivable days | at or below 80; share above 6 months at or below 12% | Receivables note, ageing | LBF-2 durability |
| Receivables 2-3 year bucket | falls below 130.54; provision rule disclosed | Ageing | Stuck dues and ECL |
| Named top-10 customers and buyer class of the 95-vehicle kit revenue | names, end user, state | Customer disclosure, tenders on GeM | LBF-1 |
| Gross margin on COGS | at or above 27% | P&L | Margin quality |
| Q4 or H2 share of sales | no quarter above 40% | Quarterly split | Timing risk |
| Bank guarantee outstanding vs IOB LG limit 800.00 | below 700 | Contingent liabilities | Limit headroom |
| Software CWIP and commissioning | commissioning date; amortisation at 10 years is 13.7 a year | Fixed asset note | Capitalisation test |
| Related-party purchases from Gostocks, Extreme Covet, Shah group | no growth; arm's-length basis disclosed | RPT note | Value extraction |
| Reg 30 filings tied to a named order or tender | any NFSU or MHA order stated | BSE announcements | LBF-4 |

## One-line verdict
Profit grew 4.8x in two years and the balance sheet is clean, but 56% cash conversion, unnamed buyers behind 82.7% of growth and a self-contradicting governance record keep this a GARP watchlist name until the proof gate fires.

---
```yaml
stage: B03-ardeep
company: "KWICK"
run_date: "2026-10-04"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "No annual report: AR substitute is the final Prospectus 31-Aug-2026 (restated FY24-FY26, Rs lakh, Indian GAAP, standalone). Statutory auditor's report with KAMs, CARO 2020, directors' report, chairman's letter, prior-year ARs, board attendance, whistleblower report, section 143(12) reporting are NOT AVAILABLE"
  - "Customer names, buyer type by product line, buyer class and segment placement of Rs 2,035.74 lakh of kits for 95 vehicles, receivable split by buyer type: NOT FOUND"
  - "FY26 Q4 share of sales, POC contract value, ECL rule, software CWIP vendor schedule, commission payees, FY26 group-entity financials, segment margins, order book: NOT FOUND"
  - "Live-web items PENDING LIVE VERIFICATION: PIB release 03-Jan-2026 (Rs 30,000 crore outlay), deck market-size figures, 433 mobile forensic vans, NFSU Varanasi campus Rs 150 crore"
flags:
  - {type: FLAG-CASH, reason: "CFO 762.30 vs PAT 1,350.77 lakh = 56.4% FY26 (54.3% FY25, -91.9% FY24); CFO/EBITDA 40.0%; FY26 CFO includes statutory dues +144.12 (GST timing), ex it 618.18 = 45.8% of PAT; FY25 CFO includes payables +717.33 (Annex III p.228; I.7 p.234)"}
  - {type: FLAG-PROMOTER-PRELIM, reason: "No pledge (p.85). FY25 promoter cash sales 31,639 shares at Rs 569 = Rs 180.03 lakh and 63,279 gifted, incl. 21,093 to Vishal Jain (CFO from 01-Aug-2025) (pp.80-81, 201); OFS 10,80,000 shares = Rs 972.00 lakh = 71.96% of FY26 PAT (p.276). Full verdict from B08"}
  - {type: FLAG-CUSTOMER-ID, reason: "Non-government 4,733.92 lakh (44.78%, 82.65% of growth) unnamed; filing shows kits for 95 vehicles sold via dealers and vehicle manufacturers, Rs 2,035.74 lakh = 43.0% of non-government revenue, segment placement not stated (p.29, p.150, p.160)"}
  - {type: FLAG-RPT, reason: "Gostocks Fintech sold 58.95 lakh to Kwick in FY25 = 62.3% of its FY25 turnover 94.64; Extreme Covet 31.20 = 48.3% of 64.57; software CWIP 137.17 about 57% Gostocks purchases; no arm's-length evidence (pp.213-215, 250, 237)"}
  - {type: FLAG-CAPITALISATION, reason: "Software CWIP 137.17 unamortised; capitalised share 0/59.6/82.6% of programming spend; policy lacks AS 26 research/development test; AI and LIMS prototype costs 48.72 outsourced; oldest CWIP 61.70 predates stated FY26 start (pp.230, 237, 240, 151-152)"}
  - {type: FLAG-DISCLOSURE-CONDUCT, reason: "Reg 30 NFSU Varanasi note 27-Sep-2026 one day after 26-Sep reply saying nothing to disclose; Audit Committee dated 04-Jul-2026 (p.196) vs KPI approval 25-May-2026 (p.256); deck 130 customers vs 95; deck PBT 1,921.45 vs 1,821.45; MD pay 126.72 paid vs 94.00 terms (p.191, p.250)"}
phase_verdicts: {p1: "YELLOW (examination report only; no KAMs, no CARO)", p2: "YELLOW", p3: "YELLOW", p4: "YELLOW", p5: "YELLOW (upper end)", p6: "YELLOW", p7_best_fit: "GARP WATCHLIST"}
overall_quality: 5.3
quality_components: {governance: 4, accounting: 5, balance_sheet: 7, earnings: 5}
kill_switch_notes:
  - "P3: a human reviewer would not have reason to stop; cash conversion weak but positive, borrowings nil; wants H1 FY27 CFO before sizing"
  - "P5: a human reviewer would not have reason to stop; wants the Audit Committee date conflict, MD pay 34.8% above stated terms, WTD joining date conflict and CFO share gift answered before signing the Mental Model"
triple_pass_verification:
  verified: 12
  discrepancies:
    - {finding_rank: 4, triple_pass_value: "ex-cash WC days 97.1/72.8/78.4 (borrowings counted as operating liability); FY26 did not improve", ar_value: "ex-cash and ex-borrowings 135.2/91.1/78.4, FY26 improved 12.7 days; company KPI 98/141/124 incl cash (computed from p.226-227; p.257)", note_ref: "Annex I p.226; KPI p.257"}
    - {finding_rank: 10, triple_pass_value: "Rs 20 'placement' about 89% promoter; 94,918 shares transferred FY25 at undisclosed price", ar_value: "Rs 20 was a 5:1 rights issue 12-Mar-2024, promoters 14,51,550 of 16,00,050 = 90.7%; of 94,918 transferred, 31,639 sold for cash at Rs 569 and 63,279 gifted (to Vishal Jain, Sangita Mehta, Sunita Shah)", note_ref: "Capital structure pp.80-81"}
    - {finding_rank: 11, triple_pass_value: "tax disputes 14.87 outside contingent table (6 cases)", ar_value: "23 tax cases, 19.37 lakh in legal section and RF17 (IT 5/8.55, TDS 17/4.54, GST 1/6.28); Annexure V xiv shows 6 cases, 14.87 and omits 17 TDS cases", note_ref: "p.274; RF17 p.35; Annex V xiv p.244"}
missing_risks:
  - {risk: "Dealer and vehicle-builder channel replacing direct state sales, Rs 2,035.74 lakh of kits for 95 vehicles", evidence: "p.150; absent from segment tables p.24 and RF10 p.29"}
  - {risk: "Q4 loading 51% of FY25 sales; FY26 not found; MD&A says not seasonal", evidence: "p.92; p.270"}
  - {risk: "No ECL rule; 130.54 lakh at 2-3 years provided 20.7%; ageing roll-forward anomaly 26.27", evidence: "Note I.14 p.235"}
  - {risk: "Single-customer rental line 925.41 lakh (8.75% of revenue) equals one customer; implied direct margin 97.6%", evidence: "pp.24, 160, 239"}
  - {risk: "Promoter-group suppliers depend on Kwick for 48% to 62% of their turnover", evidence: "pp.213-219 vs pp.250-251"}
  - {risk: "BG limit headroom 207.15 of 800.00 vs about +40% implied FY27 revenue growth", evidence: "p.234; p.255; p.95"}
  - {risk: "Audit Committee constituted 04-Jul-2026 but cited as approving KPIs 25-May-2026", evidence: "p.196 vs p.256"}
  - {risk: "Independent director turnover: three exits in ten months; two sitting independents are one 33-year-old with four other boards and one appointed 04-Jul-2026", evidence: "p.194; pp.186-187"}
  - {risk: "Independent director Dr Mukesh defendant in Madras HC defamation suit, Rs 100.10 lakh claimed; chairs NRC", evidence: "p.272"}
  - {risk: "Promoter gifted 1.00% to future CFO six months before appointment", evidence: "p.80; p.201; p.203"}
  - {risk: "Software CWIP about half related-party purchase; no AS 26 test; prototype costs capitalised", evidence: "pp.237, 250, 230, 152"}
  - {risk: "Gross margin 37.3% to 27.1% with no cause in MD&A beyond cyber mix", evidence: "p.257; p.265; RF13 p.32"}
  - {risk: "Reg 30 disclosure conduct after price query", evidence: "announcements 26-Sep and 27-Sep-2026"}
  - {risk: "Thin organisation and liaisoning: 33-34 staff, six-person sales team, commission payees undisclosed", evidence: "pp.36, 156-157, 240"}
  - {risk: "Top Supplier 1 is 92.8% of Cyber revenue FY26 (hypothesis: thin-margin pass-through)", evidence: "pp.24, 27"}
guidance_table:
  - {claim: "FY27 working capital need", number: "4,442.00 lakh (receivables 3,000; inventory 1,350; payables 700)", timeframe: "FY27", credibility: "Medium; plan adds 854.86 vs IPO 3,142.00, about 2,287 replaces existing funding"}
  - {claim: "Implied FY27 revenue (not stated)", number: "about 14,797 lakh (+40.0%)", timeframe: "FY27", credibility: "Medium; implied from 3,000 / 74 days x 365"}
  - {claim: "Debtor days stabilise", number: "74 days", timeframe: "FY27", credibility: "Medium; FY26 year-end basis is 79"}
  - {claim: "Reduce Bihar and Gujarat dependence", number: "top-two share 38.4% FY26 from 57.3%", timeframe: "ongoing", credibility: "Mixed; Gujarat rose to 29.39%"}
  - {claim: "Improve gross margin via domestic sourcing", number: "domestic share 65.42% to 91.35%", timeframe: "past", credibility: "Low; gross margin fell 37.3% to 27.1%"}
  - {claim: "E-Forensics suite and AI/LIMS platforms in development", number: "none; CWIP 137.17", timeframe: "none", credibility: "Low"}
  - {claim: "Private forensic laboratory", number: "none", timeframe: "none", credibility: "Low; not in objects of the issue"}
  - {claim: "FY27 managerial remuneration ceiling", number: "315.89 lakh vs 281.35 FY26", timeframe: "FY27", credibility: "High; terms stated"}
monitorables:
  - {metric: "H1 FY27 CFO/PAT", threshold: ">= 0.8 (FY26 0.56)", where: "H1 FY27 cash flow statement", why: "tests whether IPO money fixes conversion"}
  - {metric: "Year-end receivable days and >6m share", threshold: "<= 80 days and <= 12%", where: "receivables note and ageing", why: "LBF-2 durability"}
  - {metric: "2-3 year receivable bucket", threshold: "below 130.54 lakh; provision rule disclosed", where: "ageing note", why: "stuck dues"}
  - {metric: "Named top-10 customers and buyer class of 95-vehicle kit revenue", threshold: "names, end user, state", where: "customer disclosure, GeM tenders", why: "LBF-1"}
  - {metric: "Gross margin on COGS", threshold: ">= 27%", where: "P&L", why: "margin quality"}
  - {metric: "Q4 or H2 share of sales", threshold: "no quarter above 40%", where: "quarterly split", why: "timing risk"}
  - {metric: "BG outstanding vs IOB LG limit", threshold: "< 700 of 800 lakh", where: "contingent liabilities", why: "limit headroom"}
  - {metric: "Software CWIP commissioning", threshold: "commissioning date; amortisation 13.7 lakh a year at 10 years", where: "fixed asset note", why: "capitalisation test"}
  - {metric: "Related-party purchases from Gostocks, Extreme Covet, Shah group", threshold: "no growth; arm's-length basis stated", where: "RPT note", why: "value extraction"}
  - {metric: "Reg 30 filings tied to a named order or tender", threshold: "any NFSU or MHA order stated", where: "BSE announcements", why: "LBF-4"}
ar_new_downstream_entities:
  - {name: "Top Customer 1 (unnamed, 23.59% of FY26 revenue, 2,493.65 lakh)", where_in_ar: "RF2 p.24; business p.160", entity_type: "customer >10% of revenue, name not disclosed"}
  - {name: "Top Customer 2 (unnamed, 11.36%, 1,201.40 lakh)", where_in_ar: "RF2 p.24; business p.160", entity_type: "customer >10% of revenue, name not disclosed"}
  - {name: "Local dealers and established vehicle manufacturers (unnamed) buying kits for 95 Mobile CSI vehicles, 2,035.74 lakh", where_in_ar: "Business strategies p.150", entity_type: "channel partners, possibly the non-government buyers"}
  - {name: "Top Supplier 1 (unnamed, 3,268.40 lakh, 40.86% of cost of materials)", where_in_ar: "RF6 p.27; business p.161", entity_type: "supplier >10%"}
  - {name: "Gostocks Fintech Private Limited", where_in_ar: "Annexure VIII p.250; group entities p.214", entity_type: "RPT counterparty, software vendor, group entity"}
  - {name: "Extreme Covet Private Limited", where_in_ar: "Annexure VIII p.250; group entities p.212", entity_type: "RPT counterparty, goods supplier and past lender, group entity"}
  - {name: "Shah Infotech; Shah Electronics; Shah Trading & Co.; The Style Salad; Gee Gee Hire Purchase & Leasing Private Limited", where_in_ar: "Annexure VIII p.250; group entities pp.215-219", entity_type: "RPT counterparties, promoter-group firms"}
  - {name: "Sirchie (USA); Thermo Fisher Scientific; Invitrogen; Rapiscan Systems; Smallpond; MHC Hardware Software Trading LLC; Seratec", where_in_ar: "Competitive strengths p.149", entity_type: "OEM principals, non-exclusive"}
  - {name: "Corporate Capital Ventures Pvt Ltd; CCV Emerging Opportunities Fund-I; Chanakya Opportunities Fund I", where_in_ar: "RF15-16 pp.33-34", entity_type: "BRLM and pre-IPO investors"}
  - {name: "Indian Overseas Bank; National Small Industries Corporation (NSIC)", where_in_ar: "Statement of financial indebtedness p.255", entity_type: "lenders"}
  - {name: "GeM and e-procurement portals; National Forensic Sciences University (NFSU)", where_in_ar: "business p.157; Reg 30 note 27-Sep-2026", entity_type: "named platform and named third-party institution, no Kwick order disclosed"}
strengths_top3:
  - "Debt-free with net cash 1,316.32 lakh, current ratio 2.90, 325.61 repaid in FY26 (p.226, p.245)"
  - "Year-end receivable days 144 to 111 to 79 while revenue grew 3.5x; EBITDA margin steady at 18.0%"
  - "Granular disclosure of statutory defaults, related parties, ageing and fully repaid promoter loans"
red_flags_top3:
  - "Cash conversion 56.4% of PAT and 40.0% of EBITDA, with 144.12 lakh of FY26 CFO from GST timing"
  - "Buyers behind 82.7% of growth unnamed; undisclosed-segment dealer channel of Rs 2,035.74 lakh (43.0% of non-government revenue)"
  - "Governance and disclosure record: promoter-group vendors dependent on Kwick, Audit Committee date conflict, MD pay 34.8% above stated terms, Reg 30 note after a price query"
best_fit_strategy: "GARP (WATCHLIST); proof gate not fired"
one_line_verdict: "Profit grew 4.8x in two years and the balance sheet is clean, but 56% cash conversion, unnamed buyers behind 82.7% of growth and a self-contradicting governance record keep this a GARP watchlist name until the proof gate fires."
analyst_note: "Unit Rs lakh as printed. No AR exists: Phase 1 is an examination report (no KAMs, no CARO); Phase 6 uses prospectus strategy sections. Three findings a later stage cannot rebuild. One: the filing itself gives a mechanism for the non-government jump. p.150 says FY26 kits for 95 Mobile CSI vehicles went through dealers and vehicle builders for Rs 2,035.74 lakh, 43.0% of non-government revenue; segment placement not stated. LBF-1 stays open on names. Two: software CWIP 137.17 is about Gostocks 78.70 plus outsourced prototypes 48.72; Gostocks sells 62% of its FY25 turnover to Kwick. Three: rental revenue equals one customer each year, and Assam, Meghalaya and Mizoram top customers equal state totals. Corrections to B02: FY24 Rs 20 issue was a rights issue; FY25 promoter sales were at Rs 569 plus gifts (one to the later CFO); operating WC days improved on an ex-debt basis; legal section shows 23 tax cases, not 6. Quality 5.3."
```
