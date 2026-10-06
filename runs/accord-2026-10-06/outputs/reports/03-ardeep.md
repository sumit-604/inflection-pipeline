# Stage 3: AR backward deep dive (B03-ardeep)
Company: Accord Transformer & Switchgear Ltd (ACCORD, BSE SME 544710). Run date 2026-10-06. Model claude-sonnet-5-5.

## 0. Conventions, sources, anchor index

Sources read: FY2025-26 AR (12th AR, Rs lakh on the face, p.77); Prospectus 2026-02-26 by targeted reads (restated figures in Rs THOUSAND on its face; converted here to Rs lakh by dividing by 100, stated at each use); B02 notes report and block; B00, B01; Jun-2026 transcript (read only to test operator claims); filings 20260624 (UGVCL), 20260706 (Aditya Birla), 20260703 (land). Results scan pages p03-p19 were not used (FY26 figures come from the audited statements in the AR).

Unit rule: all AR figures are Rs lakh unless the cell says Cr. 100 lakh = 1 Cr. No figure is converted silently.

Page rule: "AR p.N" is the text marker "[page N]" of Annual_Report_2026.txt (same rule as B02). Printed folio = N + 18 from marker 22 onward (example: balance sheet is AR p.77, printed "95"). "Pros. p.N" is the "[page N]" marker of the prospectus text. "Tr." is the Jun-2026 transcript text.

"calc" = derived by me from filed figures. "[INFERENCE]" = my reading, not a filed fact.

### 0.1 Anchor index for stage 5 (no-concall fallback is NOT active; stage 5 uses these)
| Topic | Where | What it holds |
|---|---|---|
| MD&A | AR p.60-66 (printed 78-84) | Industry p.60-61; company overview p.61-62; operations p.62-63; financial highlights and revenue mix chart p.63; P&L summary and 10-ratio table p.64; ratio commentary and outlook p.65; risk, internal control, HR p.65-66 |
| Objects of the issue, use of proceeds | AR p.22-23 (Notice item 3 table); AR p.32-34 (explanatory statement: table p.32-33, reason p.33, new-object risks p.34); AR p.68 (KAM 2, IPO utilisation); AR p.73 (CARO x(a)); Pros. p.74-75 (objects, schedule), p.76-79 (machinery, working capital) | Rs 2,558.52 lakh raised; Rs 1,187.44 lakh used to 2-Sep-26; Rs 1,371.08 lakh unused; Rs 700.00 lakh moved from machinery to building |
| Capacity and utilisation | AR p.6, p.13, p.21, p.62 ("1,200+ MVA"; no production or utilisation figure anywhere in the AR); Pros. p.76 and p.123 (installed 900.36 MVA, FY26 utilisation 69.78%, extrapolated); Tr. lines 480-491 (management: 75-80%) | AR utilisation: NOT FOUND IN DOCUMENT |
| Order book | AR p.37 ("healthy order book", no number); Pros. p.79 (Rs 1,642,575.62 thousand = Rs 164.26 Cr at 18-Jan-26), p.114-115 (67 PO lines) | AR order book number: NOT FOUND IN DOCUMENT |
| Customer concentration | AR p.65 (generic risk text only); Pros. p.31 (risk factor 3), p.111 (top 5 and top 10 table) | AR customer table, customers over 10%: NOT FOUND IN DOCUMENT |
| Statements | Balance sheet p.77; P&L p.78; cash flow p.79; notes p.80-95; CARO p.72-74; IFC p.75-76 | |
| Related parties | Note 2.3 p.81-82; AOC-2 p.54 | |
| Governance | Directors' Report p.37-48; secretarial audit p.49-53; remuneration annexure p.58-59 | |

## 1. Operator context verified against filings (cite as (operator, 2026-10-06) where it is only operator text)
| Operator claim | Result | Evidence |
|---|---|---|
| FY26 revenue 70.07, other income 0.29, D&A 0.63, finance cost 0.55, PBT 6.06, PAT 4.50 (Cr) | HOLDS | Revenue 7,006.92; OI 28.78; dep 62.60; fin cost 55.04; PBT 605.75; PAT 450.43 lakh (AR p.78) |
| Operating EBITDA 6.95 Cr (9.9%) | HOLDS | 723.39 - other income 28.78 = 694.61 lakh = 9.91% of revenue (calc; AR p.64 shows EBITDA 723.39 incl. other income) |
| CFO 8.70, cash 22.3 Cr | HOLDS, with a qualifier | CFO 869.50 (AR p.79); cash 2,232.80 (AR p.77) of which 2,040.21 is unspent IPO money (AR p.73) |
| Shares 2.057 Cr | HOLDS | 2,05,73,289 shares (AR p.85) |
| L&A 0.64 to 8.90 Cr | HOLDS | 63.86 to 890.45 lakh (AR p.77, Note 17 p.90) |
| ~Rs 31 Cr order deferred, Maharashtra site dispute, 25 of 35 sets made | NOT FOUND IN AR; HOLDS in the transcript | AR never names it: MD&A says "calibrated business approach amid evolving market conditions" (AR p.63). CFO on the call: "supply orders worth around INR31 crores ... Out of 35, we have manufactured around 25 sets, valuing around INR21 crores or INR22 crores ... dispute from their end with the Maharashtra Government" (Tr. p.5, lines 200-205). The prospectus order list has one order of Rs 31.50 Cr in three ratings of 35 units each (LPPL-02, 17-Jan-26, Pros. p.115): 223,300 + 76,300 + 15,400 = 315,000 thousand. [INFERENCE] This is the same order (size, 35 count, 25/35 x 31.5 = 22.5 Cr all fit). The Maharashtra link to LPPL is NOT FOUND in any filed document. |
| FY27 guidance Rs 120-180 Cr, EBITDA 13-15%, PAT 9-11% | NOT FOUND IN AR; HOLDS in transcript | Tr. lines 480-491 (PAT 9-11%; "targeting around more than INR120 crores") |
| Plant ceiling Rs 150-200 Cr | NOT FOUND IN AR; does not reconcile | See Backward baseline (section 2). At FY25 revenue per MVA it equals 100% fill of 900-1,200 MVA (900.36 x 16.69 lakh = Rs 150 Cr; 1,200 x 16.69 = Rs 200 Cr, calc). Management also says Rs 120 Cr = "around 90% of our capacity" (Tr. line 490), which implies about Rs 133 Cr at 100%. The two statements conflict. |
| FY26 utilisation 75-80% | NOT FOUND IN AR; does not reconcile | CFO on call (Tr. line 488). Prospectus FY26 utilisation is 69.78% on 900.36 MVA and is extrapolated from 400.50 MVA for nine months (Pros. p.123). 75-80% of 1,200 MVA would mean 900-960 MVA made, above every prospectus production figure. |
| Inventory days 179 | DOES NOT HOLD on the AR's own ratio | AR p.64 turnover 2.51 = 145 days. 179-180 reproduces only as closing inventory over raw material consumed (B01). Basis mismatch is explained in Phase 2, Extension A. |
| Land Khairthal-Tijara 20,300 sq m, Rs 8.85 Cr + 1.82 Cr | HOLDS in the filing; AR gives no price | Filing 3-Jul-26; AR p.13, p.38 give area only. It is a FY27 event; the AR presents it as FY26 (see Phase 6). |
| NHEV EV-charging LOI | NOT FOUND IN AR | Zero mentions of NHEV in the AR. The prospectus names a "collaboration with NHEV" with no agreement or value (Pros. p.117). Revenue mix p.63 has no EV line. |
| Aditya Birla orders Rs 37 Cr | NOT FOUND IN AR | AR shows only a vendor approval, filed 6-Jul-26 |

## 2. Backward baseline FY23 to FY26 (restated prospectus plus AR)
Prospectus figures are Rs thousand on its face, shown here in Rs lakh (calc). FY26 is the AR.
| Metric | FY23 | FY24 | FY25 | FY26 | Anchor |
|---|---|---|---|---|---|
| Revenue from operations | 4,078.17 | 4,853.69 | 7,902.25 | 7,006.92 | Pros. p.110; AR p.78 |
| Growth | n/a | +19.0% | +62.8% | -11.3% | Pros. p.110; calc |
| EBITDA (PBT + interest + dep, incl. other income) | 153.77 | 267.28 | 910.14 (AR basis 925.31) | 723.39 | Pros. p.110; AR p.64 |
| EBITDA margin on revenue | 3.77% | 5.51% | 11.52% | 10.32% | calc (AR p.64 prints 10.39% for FY26; it ties to neither revenue nor total income, which give 10.32% and 10.28%) |
| PAT | 87.81 | 160.67 | 605.36 restated (594.37 AR comparative) | 450.43 | Pros. p.110, p.169; AR p.78 |
| Net worth | 443.24 | 603.91 | 2,154.11 | 4,886.85 | Pros. p.166; AR p.77 |
| Debt/equity | 0.52 | 1.51 | 0.55 printed (0.81 on AR balance sheet) | 0.18 | Pros. p.110; AR p.64, p.77 |
| ROE (on average equity) | 21.99% | 30.69% | 43.90% (AR 42.93%) | 12.79% | Pros. p.110; AR p.64 |
| ROCE, prospectus basis (EBIT / equity + debt + DTL) | 20.49% | 16.47% | 26.09% | 11.44% (calc) | Pros. p.110; calc |
| Employee cost / revenue | 4.74% | 6.49% | 4.58% | 8.26% | Pros. p.124; AR p.91 |
| Installed capacity, MVA | 721.56 | 789.84 | 847.56 | 900.36 (certified to 31-Dec-25) vs "1,200+" in AR | Pros. p.123; AR p.21 |
| Production, MVA | 250.52 | 254.96 | 473.62 | 400.50 for nine months; 628.30 extrapolated | Pros. p.123 |
| Utilisation | 34.72% | 32.28% | 55.88% | 69.78% (extrapolated) | Pros. p.123 |
| Revenue per MVA made, Rs lakh | 16.28 | 19.04 | 16.69 | 11.29 for nine months (4,521.63 / 400.50) | calc |
| Top 5 customers % of revenue | 79.60% | 58.29% | 73.62% | 48.10% (nine months) | Pros. p.111 |
| Top 10 customers % | 89.09% | 71.32% | 84.16% | 66.74% (nine months) | Pros. p.111 |
| CFO (restated, as carried in B01) | 1.88 | (4.82 Cr) | (8.18 Cr) | 8.70 Cr | B01; AR p.79 |
| Capex (Rs Cr) | 0.40 | 2.34 | 3.13 | 1.46 | B01; AR p.79 |

Reading: revenue CAGR FY23-FY26 is 19.8% (calc). The FY24-FY25 step came from production almost doubling (254.96 to 473.62 MVA, +85.8%) against revenue +62.8%. FY26 revenue per MVA made fell from 16.69 to 11.29 lakh, so more MVA was made per rupee sold. That fits the inventory build. The AR shows no capacity addition and no production figure, so the "1,200+ MVA" step up from the certified 900.36 MVA has no filed support.

## PHASE 1: AUDITOR'S REPORT AND CARO

### 1A Core opinion
Unmodified. Opinion: financial statements "give a true and fair view in conformity with the applicable accounting standards" (Auditor's Report, AR p.67). Basis: SAs under s.143(10) (p.67). Framework: Indian GAAP / AS, not Ind AS (SME exemption, Directors' Report item 35, AR p.45). Report dated 29-May-2026, UDIN 26584258LBKEWA9611 (AR p.71). Going concern language: NONE in the opinion; Management's duty paragraph is boilerplate (p.69). CARO xix reports no material uncertainty on meeting liabilities for one year and adds "this is not an assurance as to the future viability" (AR p.74). No emphasis of matter, no qualified paragraph. Note the odd title: the report is headed as a Reg 33 report on "annual financial results" (p.67), which is a results-format heading on an AR audit report. Cosmetic.

### 1B Key Audit Matters
| # | Subject | Why key | How addressed | Risk |
|---|---|---|---|---|
| 1 | Revenue recognition (AR p.67-68) | Size, volume, multiple locations, year-end cut-off, management override | Controls testing, sample of orders, invoices, challans, cut-off, post-year-end receipts. Conclusion: revenue "considerably in accordance" with policies (p.68) | YELLOW. "Considerably" is a hedge, not a clean "in accordance". The KAM says recognition occurs "upon dispatch or delivery"; the policy note (AS-9, p.80) does not say when control passes. Q4 was 35.5% of the year (B02). Rs 619.50 lakh stock in transit shows revenue was not booked on some dispatched goods, which points to delivery-based recognition [INFERENCE]. |
| 2 | IPO fund utilisation (AR p.68) | Materiality, compliance, judgement on eligible use, disclosure of unused balances | Read prospectus, reconciled utilisation to books and bank, test of vouchers, checked balances held per board approvals. Conclusion: "considerably consistent with the stated objects" (p.68) | YELLOW. An auditor rarely lists IPO use as a KAM unless it was a live judgement. CARO x(a) reports Rs 2,040.21 (no unit printed) lying in FDs and current accounts (p.73). The same 2,040.21 is 91.4% of cash. The object change came 3 months after this report (AR p.32). |

### 1C Emphasis of Matter and Other Matters
None issued. "Other information" paragraph: nothing to report (AR p.69).

### 1D CARO 2020 clause by clause (AR p.72-74)
| Clause | Finding | Remark |
|---|---|---|
| i PPE | Records kept, all PPE verified, title deeds in company name, no revaluation (p.72) | Clean. Note 12 (PPE schedule) is missing from the printed notes (AR p.88; B02), so the clause cannot be tied to a gross block. |
| ii(a) inventory | Verified at intervals, no 10% discrepancy (p.72) | Clean. Rs 619.50 lakh stock in transit cannot have been counted physically; no mention. |
| ii(b) WC limits over Rs 5 Cr on current-asset security; returns compared with books; "no material discrepancies" (p.72) | Confirms current-asset-secured limits | CONTRADICTS Note 2.11(b) "no borrowings ... on the basis of Security of current assets" (AR p.84). The Note is wrong; CARO is right (HDFC cash credit 621.37 is secured on stock and book debts, Pros. p.177). |
| iii loans, guarantees | Table printed "(Rs in Thousands)"; every cell Nil; (iii)(b) refers to "31st March, 2025" (p.72-73) | Stale template. Note 17 shows "Loan & Advances 15.23" (AR p.90) with no counterparty. Vendor advances 624.41 are trade advances, probably outside "advances in the nature of loans", but the line is not explained. |
| iv, v, vi | Not applicable; no deposits; cost records not applicable (p.73) | Clean |
| vii(a) statutory dues | Regular; no arrears over 6 months (p.73) | Note 28 shows interest on delayed TDS/TCS/income tax 4.40 (FY25 7.71) and a GST demand 2.01 (AR p.92): small late payments recur. |
| vii(b) disputed dues | None (p.73) | Contingent note shows CST 2.23 deposited and cleared (AR p.83). |
| viii | No undisclosed income (p.73) | Clean |
| ix(a)-(d) | No default; term loans applied to purpose; no short-term funds for long-term use (p.73) | Clean. Land of Rs 10.67 Cr bought after year end (3-Jul-26 filing) is outside this period. |
| x(a) | Rs 2,040.21 unspent IPO money in FDs and current accounts (p.73) | Unit missing; ties to lakh (2,558.52 - 518.31 used by 31-Mar, calc). |
| xi fraud | No fraud noticed or reported; no whistle-blower complaint (p.73-74) | Clean |
| xiii | s.177 and s.188 complied (p.74) | Clean. Note: RPT table omits former CFO pay and ABL reimbursement (B02). |
| xiv(a) internal audit | "adequate Internal Audit System" (p.74) | CONTRADICTS Directors' Report item 43, which says the auditors "observed in their report under [CARO] that the internal audit system of the Company needs to be strengthened" (AR p.47). The CARO text printed says the opposite. One of the two documents is wrong. [RED for reliability of the Board's account of the audit report.] |
| xv, xvi | Not applicable | Clean |
| xvii cash losses | None in the year or the year before (p.74) | Clean |
| xviii auditor resignation | None in the year (p.74) | Clean. A resignation did occur on 7-Aug-24 (see 1E). |
| xix | No material uncertainty for one year (p.74) | Cannot test: DSCR 0.81 (AR p.64) is below 1.0 |
| xx CSR | Required 7.7 lakh, spent (p.74); CSR annexure: required 7,70,431, spent 7,71,000 (AR p.56-57) | Clean. P&L shows 7.70 (AR p.92). |

### 1E Auditor continuity
| Item | Fact | Anchor |
|---|---|---|
| Firm | P.K. Lakhani & Co., FRN 014682N; partner Bhavay Lakhani, M.No 584258 | AR p.71 |
| Appointed | 2-Sep-24 on casual vacancy; re-appointed 30-Sep-24 for 5 years to the 15th AGM | Pros. p.57; AR p.44 |
| Predecessor | Kumar Vijay Gupta & Co, FRN 007814N, resigned 7-Aug-24 "due to pre-occupation in other assignment" | Pros. p.57 |
| Same address and email | Both firms list "879-Basement, Sector-40, Gurgaon" and the same email (pradeep.lakhani@gmail.com) | Pros. p.57 |
| Tenure | FY25 and FY26 are the first two audits. Rotation due after FY29. | AR p.44 |
| Audit fees | Statutory audit 1.39 (FY25 0.45, +209%); tax audit 0.11 (0.15); total 1.50 vs 0.60 | Note 28, AR p.92 |
| Non-audit fees | NOT FOUND IN DOCUMENT. The same firm certified the prospectus working-capital table, holding days and the order-book list (certificates dated 6-Feb-26, Pros. p.79-80, p.115). Fee for that work is not shown. Ratio audit : non-audit cannot be computed. | Pros. p.79, p.115 |
Flag: a mid-year auditor switch with the outgoing and incoming firm sharing one address and email is a structural independence question. It is not a proven problem. Two readings: (a) one practice reorganised under a new firm name after a partner exit; (b) a pliant auditor replaced one who left before an IPO audit. Observation that separates them: ICAI/MCA records for the two FRNs, and the ADT-3 resignation filing text. NOT FOUND IN DOCUMENT.

### 1F Standalone vs consolidated
No subsidiary, JV or associate (Directors' Report item 13, AR p.39). Standalone only. No other-auditor reliance.

### Phase 1 summary
| Item | Result |
|---|---|
| Opinion | Unmodified, no EOM, IFC adequate (p.76) |
| CARO | Clean on dues, defaults, fraud. Three internal contradictions: ii(b) vs Note 2.11(b); xiv(a) vs Directors' Report item 43; iii template remnants |
| KAMs | Two; both hedged with "considerably" |
| Auditor | Switched Aug-Sep 2024; shared address; fees tripled; non-audit fees not shown |
Phase 1 verdict: YELLOW (Watch).
Kill Switch (informational): Based on phases so far, a human reviewer would not have reason to stop, because the opinion is unmodified and CARO is clean on defaults and fraud. The reviewer would want the auditor-switch facts checked.

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

### Triple-pass verification (B02 Top 15, re-footed to the AR)
| Rank | B02 finding | Check against AR | Result |
|---|---|---|---|
| 1 | CFO 869.50; receivable release 1,349.33; ex-release (479.83); two-year CFO +51.40 vs PAT 1,044.80 (4.9%) | CFO 869.50 and release 1,349.33 (AR p.79); 869.50 - 1,349.33 = -479.83 (negative, as B02's brackets mean); 869.50 + (818.10 negative) = 51.40; PAT 450.43 + 594.37 = 1,044.80; 51.40/1,044.80 = 4.9%. The "about (505.35) on consistent overdraft basis" is B02's inference; I did not re-derive it. | ✓ verified |
| 2 | L&A 63.86 to 890.45; vendor advance 624.41; CARO iii nil | AR p.77, Note 17 p.90, CARO p.72. 624.41/4,886.85 = 12.8% of net worth. | ✓ |
| 3 | Stock in transit 619.50 | Note 14 p.89. Notes 21 and 23 closing stocks exclude it (see Phase 3C). | ✓ |
| 4 | Cash 2,232.80; unspent IPO 2,040.21 = 91.4%; free cash 192.59; cash credit +453.95 in Q4 | AR p.77, p.73, Note 8 p.87. Dec-25 cash credit 167.42 is confirmed at Pros. p.177 (16,742.44 thousand). | ✓ |
| 5 | Inventory +34.7%, FG +252%, turnover 5.51 to 2.51 | 2,434.87/1,808.05 = +34.7%; FG 329.07/93.51 = +251.9%; AR p.64, p.95. See extension below: the two turnovers sit on different bases. | ✓ with extension |
| 6 | Q4 cluster, eight lines | Year-end values tie to AR notes. Dec-25 stub values for receivables 1,018.36, payables 559.64 and inventory 1,418.88 are confirmed at Pros. p.79 (1,01,836.18; 55,963.63; 1,41,888.25 thousand). The vendor-advance and transit-stock Dec-25 values were not re-read. | ✓ partly re-read |
| 7 | FY25 comparatives restated with no amounts; D/E 0.55 on old basis | Debt FY25 = 79.32 + 1,670.79 = 1,750.11; /2,154.10 = 0.81. Excluding the 569.38 overdraft: 1,180.73/2,154.10 = 0.548. Overdraft = Pros. cash credit 947.48 vs AR 1,516.86 (calc 569.38). | ✓ |
| 8 | Promoter-linked funding 182.78; ABL FY25 column fails arithmetic | Note 8 p.87; Note 2.3 p.82: 0 + 117.60 - 146.47 = -28.87. FY26: 0 + 150.00 - 80.36 = 69.64 closing ✓. 54.42 + 58.71 + 69.64 = 182.77 ≈ 182.78. | ✓ |
| 9 | Template errors | Note 2.11(b) p.84; Note 2.7 p.83; no Note 12 (p.88); two "Note 28" (p.92, p.93); Antelp Note 2.3 B "NIL" vs AOC-2 (p.54); promoter 84.94% printed vs 61.97% (p.85) | ✓ |
| 10 | Receivables over 6 months 83.08 (+214%); retention 499.86; bill-discount interest +350% | 57.28 + 23.73 + 2.07 = 83.08 (Note 15 p.89); 83.08/26.45 = 3.14x; 443.69 + 56.17 = 499.86; 7.74/1.72 = 4.5x (Note 25 p.91) | ✓ |
| 11 | MSME payables 1,494.94 (80.5%); +135% | Note 9 p.87: 1,494.94/1,856.77 = 80.5%; 1,494.94/637.28 = 2.35x | ✓ |
| 12 | BG 532.46 (+158%); 10.9% of net worth | Note 2.5 p.83: 532.46/205.99 = 2.58x; 532.46/4,886.85 = 10.9%. The 101.4% of Dec-25 sanction was not re-derived. | ✓ (sanction ratio not re-derived) |
| 13 | Land 1,067 lakh (21.8% of net worth); object shift 700 | Filing 3-Jul-26; AR p.32-33; 1,067/4,886.85 = 21.8% | ✓ |
| 14 | Employee cost +59.9%; promoter pay +78% on PBT -24.1% | 578.46/361.86 = +59.9%; 64.00/36.00 = +77.8% (AR p.58); 605.75/798.05 = -24.1% | ✓ |
| 15 | Segment note has no segment profit; export 97.15 lakh first appears (9M) | AR p.83; Pros. p.179 (9,715.35 thousand) | ✓ |
Result: 15 of 15 verified; 0 discrepancies. Two extensions below.

Extension A: basis mismatch in the AR inventory turnover (new). FY25 5.51 = revenue / average inventory (7,902.25 / 1,435.42 = 5.51, calc). FY26 2.51 = cost of goods / average inventory ((4,930.72 + 360.27 + 28.67) / 2,121.46 = 2.51, calc). The AR compares the two without saying so (AR p.64). Like for like: revenue basis 5.51 to 3.30 (66 to 111 days); cost basis 4.37 to 2.51 (83.5 to 145.6 days). The cost-basis FY25 figure of 83 days matches the prospectus's own 83 days (Pros. p.80). Either way days rose 45% to 75%. Stage 10 must fix one basis.

Extension B: DSCR 0.81 is not reproducible from filed figures. Interest cover is 12.0x (EBIT 660.79 / 55.04, calc). A 0.81 DSCR in a year when debt fell 49.5% means the AR's denominator probably counts net repayment of the revolving cash credit (834.55, AR p.79) [INFERENCE]. The formula is NOT FOUND IN DOCUMENT. The MD&A calls this "comfortable" (AR p.65).

### 2A Accounting policy aggressiveness (AR p.80)
| Area | What the AR says | Assessment |
|---|---|---|
| Revenue | AS-9, one paragraph; "to the extent that it is probable ... flow" (p.80) | Thin. Does not say when control passes. KAM 1 says "dispatch or delivery" (p.67). |
| Depreciation | Schedule II lives; "reviewed periodically" (p.80) | Conservative on paper; lives untestable because Note 12 is absent. Depreciation 62.60 on average PPE and intangibles of 750.7 = 8.3% (calc). |
| Inventory valuation | NOT FOUND IN DOCUMENT. No policy for cost method or NRV anywhere in Note 1 (p.80) | Gap for a company where inventory is 29% of assets. |
| Capitalisation | "capitalizes all costs relating to acquisition and installation" (p.80). No borrowing-cost policy. | No capitalised costs flagged; PPE bridge ties (794.62 = 711.03 + 146.19 - 62.60, calc) |
| Impairment | Generic (p.80) | No test described |
| Receivables provision | None. Nil bad-debt provision on 83.08 over six months (Note 15 p.89) | Aggressive by omission |
| Warranty | No provision; Rs 532.46 lakh BGs given "to cover the warranty period" (p.83) | Aggressive by omission |
| Foreign currency | No policy, yet translation loss 4.32 booked (Note 28 p.92) | Gap |
| Employee benefits | Actuarial, unfunded gratuity (Note 28 p.93). Salary escalation 8% (p.93) while salaries and wages rose 56.7% (293.13 to 459.32) | The assumption is far below experience. Gratuity restated in FY23 for earlier non-recognition (Pros. p.166). |
| Lease | AS-19 style; rent 79.37 flat in both years; lease equalisation reserve 11.12 (Note 10 p.88, Note 28 p.92) | Lessor NOT FOUND IN DOCUMENT |
| Policy change | None quantified | |
| ECL | None (AS, not Ind AS) | |

### 2B Related-party map (Note 2.3 p.81-82; AOC-2 p.54)
| Party | Relationship | FY26 transaction | % of revenue (calc) | Outstanding 31-Mar-26 |
|---|---|---|---|---|
| P.K. Verma | MD, promoter | Remuneration 32.00 (FY25 18.00); loan repaid 4.50 | n/a | Loan 54.42; remuneration due 0.39 |
| Shalini Singh | WTD, promoter, spouse | Remuneration 32.00 (18.00); loan repaid 7.50 | n/a | Loan 58.71; remuneration due 29.52 |
| ABL Electricals | Proprietorship of MD | Loan taken 150.00 (FY25 117.60); repaid 80.36; purchases 64.15 (24.25); sales nil (40.63) | Purchases 0.92% of revenue; 1.29% of RM purchases | Loan 69.64; creditor 67.59 |
| Antelp Corporation Pvt Ltd | "KMP relative has an interest" (AOC-2) | Sale 29.44 (first time) | 0.42% | Debtor 29.44 |
| Accord Global Infra Pvt Ltd | Listed in Note 2.3 C as KMP-influenced | No transaction shown | n/a | n/a |
| CFO Nitin Gupta | KMP | Pay 12.00; reimbursement 0.38 | n/a | 2.98 |
| CS Tulsi Sharma | KMP | 1.51 | n/a | 0.22 |
| Independent and non-executive directors | Sitting fees 0.80 + 0.80 + 0.70 = 2.30 | n/a | n/a | same |
Totals: trade RPT 93.59 = 1.34% of revenue. Promoter-linked borrowing 182.78 = 20.7% of total debt 883.46 and 3.7% of net worth (calc). ABL is lender, supplier and personal guarantor of the HDFC facilities (Pros. p.177-178) all at once. The former CFO's pay and the 11.68 reimbursement to ABL are not in the table (B02). Value-extraction signal: interest-free promoter money favours the company, not the promoter. The signal that stays: the same family firm supplies goods, lends, and guarantees, and its FY25 loan column does not foot. Arm's-length evidence: NOT FOUND IN DOCUMENT.

### 2C Contingent liabilities (Note 2.5 p.83)
| Item | Amount | % of net worth (4,886.85) | % of PAT (450.43) | Flag |
|---|---|---|---|---|
| Bank guarantees for warranty | 532.46 (FY25 205.99); margin FDR 181.96 | 10.9% | 118.2% | Over 100% of PAT |
| CST demand | Nil (FY25 2.23, paid) | 0% | 0% | none |
| Discounted bills with recourse | NOT FOUND IN DOCUMENT (bill-discount interest 7.74) | | | possible hidden |
| Capital commitments | NOT FOUND IN DOCUMENT | | | |
No claim is acknowledged as debt. The BGs are a warranty-period exposure, not a claim. They are unprovided.

### 2D Receivables (Note 15 p.89)
| Item | FY26 | FY25 |
|---|---|---|
| Total | 1,501.48 | 2,850.81 (-47.3%) |
| Not due | 1,029.32 (68.6%) | 2,454.22 (86.1%) |
| Less than 6 months | 389.08 | 370.14 |
| Over 6 months | 83.08 (5.53%) | 26.45 (0.93%) |
| Provision | nil | nil |
| Unbilled | nil | nil |
| Retention money, current and non-current | 499.86 (7.1% of revenue), no ageing | 402.52 |
| Days (average basis) | 113 (turnover 3.22) | 81 (4.48) |
| Customer concentration | NOT FOUND IN DOCUMENT in the AR; Pros. p.111 shows top 10 at 66.74% of nine-month revenue | |
The year-end balance fell because FY25's Rs 28.5 Cr was collected, not because credit tightened. Ageing quality got worse at the edges.

### 2E Inventory (Note 14 p.89)
| | FY26 | FY25 | Change |
|---|---|---|---|
| Raw material | 665.36 | 629.36 | +5.7% |
| Work in progress | 820.94 | 1,085.17 | -24.3% |
| Finished goods | 329.07 | 93.51 | +251.9% |
| Stock in transit | 619.50 | nil | new |
| Total | 2,434.87 | 1,808.05 | +34.7% |
Revenue fell 11.3%. No NRV or write-down disclosure. Stock in transit sits in the balance sheet only: Notes 21 and 23 closing balances (665.36 for RM; 329.07 and 820.94 for FG and WIP) exclude it, so no P&L credit is visible for it (see Phase 3C).

### 2F Borrowings (Notes 5 and 8, AR p.86-87; terms from Pros. p.177-178)
| Item | 31-Mar-26 | Due | Terms |
|---|---|---|---|
| HDFC inventory funding and cash credit | 621.37 | on demand, renewed yearly | Sanction Rs 1,100 lakh (1,10,000 thousand), REPO + 2.50%; primary security stock, book debts; collateral industrial and two office properties; personal guarantees of both promoters and ABL (Pros. p.177-178). The AR gives no rate, limit or security. |
| Director and ABL loans | 182.78 | on demand | Interest-free; no sanction letter produced (Pros. p.178 note) |
| HDFC term loan, current + long-term | 8.13 + 30.02 | to ~2030 | EMI loan, REPO + 2.50% |
| Mercedes-Benz Financial Services vehicle loan | 23.97 + 17.20 | 36 EMIs, 8.99% | Charge not filed (CHG-1), see Phase 5 |
| Total | 883.46 (FY25 1,750.11 on AR basis) | | |
Maturity wall: 94.7% of debt (836.24) is due within a year, but 804.15 of it is demand money (cash credit 621.37 and promoter loans 182.78) and only 32.10 is term repayment. No covenant disclosure. Pledge: none shown. ICDs given: none (CARO iii, p.72). Cash ex-IPO 192.59 against 836.24 short-term debt: coverage depends on bank renewal and on the Rs 22.3 Cr IPO cash.

### 2G Deferred tax (Note 2.1 and Note 6, AR p.81, p.86)
DTL 4.74 (FY25 3.25). One timing item only: depreciation difference. Effective tax rate 25.64% (155.33/605.75) vs 25.52% FY25; statutory rate 25.17%. Disallowed items explain the gap: CSR 7.70, interest on late tax 4.40, MSME interest 1.40, GST demand 2.01 (calc). No rate reconciliation is given. Note 2.1 sign conventions are muddled (Note 6 labels a liability as "Gross deferred tax assets") but net 4.74 ties to the balance sheet.

### 2H Exceptional items, ESOP, leases, post-balance-sheet events
Exceptional: FY25 prior-period expenses 19.39; FY26 none (AR p.78). Goodwill: none. ESOP: none granted; ESOP 2026 of 5,00,000 options (2.43% of 2,05,73,289 shares, calc) is a special resolution of 26-Sep-26 with exercise price "not less than face value" Rs 10, set by the NRC, against a market price near Rs 86 (operator, 2026-10-06) (AR p.35). The discount to market has no cap in the text. Maximum per employee below 1% a year. Directors other than independent directors and promoters are eligible. Leases: rent 79.37 flat; AS-19 style. Post-balance-sheet events: no note exists. Items that sit after 31-Mar-26: land purchase (3-Jul-26 filing), object change (board 3-Sep-26, AR p.32), vendor approvals (UGVCL 24-Jun-26, Aditya Birla 6-Jul-26), ESOP plan. The Directors' Report item 11 says "no material changes and commitments affecting the financial position ... between the end of the financial year and the date of the report" (AR p.39). The report is dated 3-Sep-26 (AR p.48). A Rs 10.67 Cr land purchase is a material commitment. [RED for the report's reliability on this one sentence; the land itself is a filed fact.]

### Phase 2 reconciliation with B02
B02 scores accounting quality 5/10. My Phase 2 verdict agrees: numbers reconcile (statements tie, CFS to BS tie, AS-15 ties) and the weakness is disclosure and provisioning. I add three points B02 did not carry: the inventory turnover basis mismatch (Extension A), DSCR irreproducible (Extension B), and the auditor-continuity facts in 1E. These do not move the score.

### Phase 2 cross-reference with Phase 1 KAMs
KAM 1 (revenue): Note 19 gives only goods and services; no product, geography, customer; Rs 619.50 lakh in transit unrecognised. KAM 2 (IPO): Notes 4 and 16 and CFS tie: 2,558.52 gross - 276.20 expenses = 2,282.32 = CFS line (AR p.79, p.86). Note 4 expenses 276.20 vs AR p.33 utilised issue expenses 255.85: gap 20.35, unexplained (calc).
Phase 2 verdict: YELLOW (Watch). Kill Switch (informational): a human reviewer would not have reason to stop, because no mismatch that moves profit is proven; the reviewer would want the vendor ledger for Rs 624.41 lakh before sizing.

## PHASE 3: FINANCIAL STATEMENTS

### 3A Cash flow (AR p.79)
| Item | FY26 | FY25 |
|---|---|---|
| PBT | 605.75 | 798.05 |
| Operating profit before WC | 705.54 | 900.23 |
| Inventories | (626.82) | (745.26) |
| Receivables | +1,349.33 | (2,173.28) |
| Loans and advances | (909.34) | (114.64) |
| Provisions | +19.95 | +31.15 |
| Payables | +345.37 | +739.86 |
| Other current liabilities | +239.23 | +717.17 |
| Net working capital effect | +417.72 | (1,545.00) |
| Cash from operations | 1,123.27 | (644.77) |
| Tax paid | (253.77) | (173.33) |
| CFO | 869.50 | (818.10) |
| Capex (PPE) | (146.19) | (312.55) |
| FD investments | (766.90) | (63.49) |
| Net proceeds of share issue | 2,282.32 | 944.84 |
| Repayment of short-term borrowings | (834.55) | +214.94 |
| Finance cost paid | (45.05) | (59.14) |
Footing checks: 869.50 - 900.90 + 1,370.64 = 1,339.24 ✓; CFS closing cash 1,342.70 + FD 890.11 = 2,232.81 ≈ balance sheet 2,232.80 ✓ (AR p.77). Finance cost add-back is 45.05 against P&L 55.04: the 9.99 gap is bank charges left inside CFO (calc).
| Metric | FY26 | FY25 |
|---|---|---|
| CFO/PAT | 1.93 | negative |
| CFO/EBITDA | 1.20 | negative |
| FCF (CFO - capex) | 723.31 | (1,130.65) |
| Capex/depreciation | 2.34x | 7.72x |
| Two-year CFO / two-year PAT | 51.40 / 1,044.80 = 4.9% | |
CFO quality: (1) One-time inflator: the receivable release is +1,349.33, larger than CFO. Without it CFO is -479.83. (2) Payable stretch: +345.37 payables and +239.23 other current liabilities, of which customer advances +200.94 (449.36 vs 248.42, Note 10 p.88). MSME payables 1,494.94 are 80.5% of payables and are probably beyond the 45-day statutory window [INFERENCE: payable days 136 on purchases, calc]. (3) Inventory build -626.82 and vendor advance build absorb the cash. (4) Interest is classed as financing and interest income as investing, which lifts CFO by 45.05 less 12.18 (calc). (5) Cash pile: 2,232.80, of which 91.4% is IPO money; FD investment 766.90 sits in investing.
Verdict on 3A: CFO is a receivable unwind, not a run-rate. Over the full cycle FY23-FY26, cumulative CFO/PAT is -0.18 (B01). FLAG-CASH stands.

### 3B Balance sheet (AR p.77)
| Line | FY26 | FY25 | Change |
|---|---|---|---|
| Net worth | 4,886.85 | 2,154.10 | +126.9% (IPO net 2,282.32 + PAT 450.43 = 2,732.75 ✓) |
| Borrowings | 883.46 | 1,750.11 | -49.5% (on a like-for-like basis -25.2%, B02) |
| Trade payables | 1,856.77 | 1,511.40 | +22.8% |
| Other current liabilities | 682.65 | 439.09 | +55.5% |
| PPE + intangibles | 794.62 | 706.80 (+4.23 under development) | +12.4% |
| Inventories | 2,434.87 | 1,808.05 | +34.7% |
| Receivables | 1,501.48 | 2,850.81 | -47.3% |
| Cash and bank | 2,232.80 | 126.67 | 17.6x |
| Short-term L&A | 890.45 | 63.86 | 13.9x |
| Other current assets (mostly retention) | 469.83 | 413.78 | +13.5% |
| Total assets | 8,365.58 | 5,989.03 | +39.7% |
| Ratio | FY26 | FY25 |
|---|---|---|
| D/E | 0.18 | 0.81 AR basis (0.55 printed) |
| Net debt / EBITDA | net cash 1,349.34 incl. IPO cash; ex-IPO net debt 690.87 (883.46 - 192.59), 0.95x EBITDA | 1.75x ((1,750.11 - 126.67)/925.31) |
| Current ratio | 2.23 | 1.41 |
| Quick ratio (calc) | 1.51 | 0.93 |
| Interest coverage (EBIT/finance cost) | 12.0x | 14.5x |
| ROCE (EBIT / total assets - current liabilities) | 13.25% | 37.8% |
| ROE | 12.79% | 42.93% |
| Goodwill / net worth | nil | nil |
DuPont FY26 (calc): net margin 6.43% x asset turnover 0.976 (7,006.92 / 7,177.31 average assets) x equity multiplier 2.039 = 12.79% ✓. ROE is operational, not leverage-driven: leverage fell and the multiplier is falling. FY26 ROE fell because (a) equity more than doubled on IPO cash earning almost nothing for five weeks, (b) margin fell, (c) asset turnover fell. Ex-IPO cash ROCE is about 24.0% (B01 memo, not scored).

### 3C P&L (AR p.78; notes p.90-92)
| Line | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue | 7,006.92 | 7,902.25 | -11.3% |
| Other income | 28.78 | 16.94 | +69.9% |
| Raw material consumed | 4,930.72 | 6,836.42 | -27.9% |
| Direct expenses | 360.27 | 236.60 | +52.3% |
| Change in FG and WIP | 28.67 | (797.77) | swing |
| Employee | 578.46 | 361.86 | +59.9% |
| Finance cost | 55.04 | 59.14 | -6.9% |
| Depreciation | 62.60 | 40.50 | +54.6% |
| CSR | 7.70 | nil | new |
| Other expenses | 406.49 | 365.01 | +11.4% |
| PBT | 605.75 | 798.05 | -24.1% |
| Tax (rate) | 155.33 (25.64%) | 203.68 (25.52%) | |
| PAT | 450.43 | 594.37 | -24.2% |
| EPS basic = diluted | 2.90 | 4.27 | no gap; no ESOP yet |
Margin waterfall, % of revenue (calc): gross margin after materials, direct costs and inventory change 24.1% (FY25 20.6%, +3.5 pp); employee 8.3% (4.6%); other expenses 5.8% (4.6%); EBITDA 10.3% (11.7%); PBT 8.6% (10.1%); PAT 6.4% (7.5%). Gross margin improved; operating margin fell because fixed costs (employee +216.6 lakh, other +41.5) were built ahead of revenue. Operating leverage cuts both ways: a revenue rebound at constant fixed cost would lift margin. That is the bull path. The same fixed-cost base is what hurt FY26.
Other income 28.78 is 4.75% of PBT (below the 20% flag). It holds warehouse charges 12.96, FD interest 11.25, sundry write-backs 2.02 (Note 20 p.90).
Exceptional items, 3 years: FY24 none; FY25 prior-period expense 19.39; FY26 none. Tax rate steady at about 25.5%.
Stock in transit and the P&L: Note 21 shows RM closing 665.36 and Note 23 shows FG 329.07 and WIP 820.94; the balance sheet inventory of 2,434.87 includes 619.50 of transit stock that appears in neither note. A debit of 619.50 on the balance sheet needs a credit somewhere. Two readings: (a) goods in transit were bought and booked against payables (title passed), which explains part of the +1,297 Q4 payables move (B02) and the rise in revenue-authority balances (+172.35, of which 18% of 619.50 = 111.51 would be GST input, calc); (b) the item inflates assets. The observation that separates them is the Q1 FY27 goods-receipt and payment trail. NOT FOUND IN DOCUMENT. The sum equals 102% of PBT, so a mislabel would matter.

### Phase 3 summary and cross-reference
Cross-reference with Phases 1-2: the contradiction between "disciplined working capital practices" (MD&A, AR p.63) and the ratio table (p.64) is repeated in Phase 4. KAM 1's cut-off risk and the Q4 35.5% concentration of revenue stay open.
Phase 3 verdict: YELLOW (Watch) with a RED sub-flag on cash repeatability.
Kill Switch (informational): a human reviewer would have reason to pause, not stop, because FY26 CFO is an unwind and two-year CFO is 4.9% of PAT. The pause is cleared by H1 FY27 cash flow.

## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (MD&A, AR p.65; no separate risk-factor section)
| Disclosed risk | Real or boilerplate | Evidence |
|---|---|---|
| Raw material price changes | Real, generic | No pass-through clause shown; materials moved 68.0% to 75.8% of revenue between nine months and Q4 (B02) |
| Government policy | Boilerplate | |
| Project execution | Real | 25 of 35 sets of the Rs 31 Cr order stuck (Tr. p.5) |
| Supply chain disruption | Boilerplate | |
| Competition | Boilerplate | Prospectus names Voltamp, Indo Tech, T&R (Pros. p.125) |
| Customer concentration | Real but no number | Top 10 at 84.16% of FY25 revenue (Pros. p.111) |
| Technology | Boilerplate | R&D spend is NIL (AR p.55) |
| Macro, geopolitics, commodity | Boilerplate | |
The AR text says the company "focuses on diversifying its customer base" and "maintaining prudent inventory levels" as mitigants (AR p.65). Inventory turnover halved (p.64), so the second mitigant reads against the numbers.

### 4B Missing risks (each with evidence and likely reason)
| # | Missing risk | Evidence | Likely reason for omission |
|---|---|---|---|
| 1 | Order-book concentration and counterparty approval gap. About 53% of the Rs 164.26 Cr book (UGVCL ROBUST 2.0-X, Rs 87.50 Cr, 100/200/315/500 kVA) was ordered on 17-Jan-26; the UGVCL registration is dated 24-Jun-26 and covers 500 kVA only. 500 kVA is Rs 20.12 Cr (23%) of the Rs 87.50 Cr. | Pros. p.115 items 62-65; filing 20260624 | Order-book numbers were left out of the AR altogether. Counterparty on the PO (UGVCL itself or a scheme contractor) NOT FOUND IN DOCUMENT. |
| 2 | Customer concentration numbers | Pros. p.31, p.111 | Number is unflattering |
| 3 | Customer-site delay and revenue deferral (Rs 31 Cr order, 25 of 35 sets made) | Tr. p.5; AR p.63 calls it "calibrated business approach" | The cause is external to Accord, so omission is not self-serving, but the investor cannot see it in the AR |
| 4 | Working-capital intensity: vendor advance 624.41, transit stock 619.50, MSME payables 1,494.94, receivables over 6 months +214% | AR p.88-90 | Not a risk in management's frame |
| 5 | Warranty exposure: BGs 532.46 against nil warranty provision | AR p.83 | Not a policy item |
| 6 | IPO money idle and object change; machinery spend nil at 2-Sep-26 against Rs 1,302.67 lakh planned | AR p.32-33, p.73 | Disclosed in the AGM notice, not in MD&A |
| 7 | Finance and control churn: CFO changed twice (21-Jun-25, 16-Jan-26); internal auditor was the CFO who left; head of tax and audit, head of accounts and design manager all joined 13-Sep-25; GM operations left 21-Nov-25 | Pros. p.148; AR p.40, p.45 | Staffing is outside MD&A |
| 8 | Capacity claim unsupported: "1,200+ MVA" vs certified 900.36 MVA | AR p.6; Pros. p.123 | Marketing language |
| 9 | Single-site operations and site construction risk | AR p.34 covers only the new object | |
| 10 | Related-party dependence (ABL as lender, supplier, guarantor) | AR p.82; Pros. p.177-178 | |
| 11 | Compliance record: CHG-1 not filed on Mercedes charge (repeated in secretarial audit); MD's DIN disqualification 2016-2021; board-meeting date discrepancies; consideration for 2015 rights shares not traced | AR p.44, p.50; Pros. p.33 | History predates listing; the prospectus listed it as risk, the AR does not |
| 12 | Section 43B(h) MSME deduction risk | MSME note AR p.88 | Tax-technical |
| 13 | Export and FX claims against nil FX earnings | AR p.55 vs p.6; Pros. p.179 | Marketing |
| 14 | Interest and statutory late payment pattern (TDS/TCS interest 7.71 then 4.40; MSME interest 0.53 then 1.40) | AR p.92 | Small |

### 4C MD&A deep dive
Industry claims: IEA 3.6% electricity demand CAGR 2026-30, India installed capacity 520.51 GW (Jan-26), transmission capex Rs 9 trillion through 2032 (AR p.60-61, sources named). No share, price or demand datum specific to distribution transformers, solar or inverter-duty transformers appears. Credit-taking and blaming pattern: the decline is described as "a calibrated business approach amid evolving market conditions" (AR p.63): no cause given; no credit-taking either. Growth and margin explanation: ratio table reasons (AR p.64).
MD&A contradictions found (new, inside the same pages):
1. Current ratio reason: "increase in current assets, particularly trade receivables" (AR p.64). Trade receivables fell 47.3% (AR p.77). The rise came from cash +2,106 and inventory +627.
2. Receivables: the p.64 table says turnover fell because receivables rose ("relatively slower conversion"). The p.65 summary says "the improvement in receivables turnover indicates better working capital management". Same two pages, opposite words.
3. "Debt-equity 0.55 to 0.18" (p.64) compares an old-basis FY25 with FY26; on the AR balance sheet it is 0.81 to 0.18.
4. "Comfortable debt servicing capability" (p.65) with DSCR 0.81 (p.64).
5. "Disciplined working capital practices" (p.63) vs inventory turnover 5.51 to 2.51 and net capital turnover 9.21 to 2.46 (p.64).
6. EBITDA margin printed 10.39% (p.64) ties to neither basis (calc 10.32% or 10.28%).
Forward guidance table (AR holds no number; see YAML for rows):
| Claim | Number | Timeframe | Credibility |
|---|---|---|---|
| "supported by a healthy order book" (AR p.37) | none in AR; Pros. Rs 164.26 Cr at 18-Jan-26 | FY27 | Unquantified in AR. FY26 revenue fell 11.3% with a Rs 164 Cr book at January. |
| IPO working-capital use | FY26 Rs 275.00 lakh, FY27 Rs 725.00 lakh (Pros. p.75) | FY26-27 | By 31-Mar-26 Rs 242-262 lakh used (calc); by 2-Sep-26 Rs 931.59 lakh, 93.2% of the object, in 5 months of FY27 vs a 12-month plan. Delivered early, funded debt repayment [INFERENCE]. |
| IPO machinery spend | Rs 1,302.67 lakh, all FY27 (Pros. p.75) | FY27 | nil to 2-Sep-26; Rs 700.00 lakh moved to building (AR p.32). Slipped. |
| Prospectus FY26 working-capital table | receivable days 96, inventory days 83, payables 56; implied FY26 revenue about Rs 119 Cr (calc below) | FY26 | Delivered receivable days 113 (average basis), inventory 146 (cost basis), revenue Rs 70.07 Cr. Missed. |
| Construction of building | 9-10 months from 26-Sep-26 AGM approval (AR p.33) | to about Jul-27 | No history; first build-out for this company. |
Implied revenue in the prospectus table (calc and [INFERENCE]). The days method reproduces FY24 and FY25 on average balances (FY25: average receivables 1,765.53 / revenue 7,902.25 x 365 = 81.6, printed 82; FY24: 39.2, printed 39). Applied to FY26 estimated receivables 3,420.97 (Pros. p.79) and 96 days, revenue works out to about Rs 119 Cr ((2,850.81 + 3,420.97)/2 x 365 / 96 = 11,923 lakh). Inventory days of 83 give the same order of size. The December-25 stub (52 days) does not reproduce, so treat the figure as indicative. The statement certified by the auditor on 6-Feb-26 therefore assumed roughly 1.7x the revenue actually reported, when nine-month revenue was already 4,521.63 lakh (Pros. p.110). FY27 projected receivables 4,549.89 at 98 days give about Rs 148 Cr, inside management's Rs 120-180 Cr range.
Segment analysis (AR p.63 chart; Note 19 p.90): Transformers 82.7% (5,794.7 lakh), CSS and PSS 11.3% (791.8), Panels 1.2% (84.1), Service 1.8% (126.1; Note 19 shows 123.75), "Raw material and others" 3.0% (210.2) (calc from chart percentages). No EV line. No prior-year chart; mix shift NOT FOUND IN DOCUMENT. Note 2.4 segments are Manufacturing and Service only; service "segment result" is 114.40 on revenue 123.75 (92%), which is a treasury allocation, not an operating margin (B02).

### 4D Tone and credibility (1 to 5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | No order book, utilisation, concentration, export share or cause of decline; Note 12 missing; vendor advance unexplained |
| Consistency | 2 | Six MD&A contradictions; CARO vs Directors' Report; ratio basis mix |
| Specificity | 2 | Generic industry copy; a few real facts (CPRI test, 17.6 MVA, 20,300 sq m) |
| Accountability | 2 | Fall in profit not owned or explained; Board report calls internal audit "adequate" in one place and "needs to be strengthened" in another |
| Capital allocation sense | 3 | Debt cut 49.5%; IPO money held rather than spent; but WC object used up in five months and machinery plan dropped for land and civil work |
Phase 4 verdict: YELLOW (Watch), close to RED on consistency.
Kill Switch (informational): a human reviewer would not have reason to stop, because the contradictions are disclosure sloppiness, not hidden mismatch; the reviewer would downgrade trust in all narrative text and lean on filed numbers.

## PHASE 5: GOVERNANCE AND BOARD

### 5A Board (AR p.40-41; Pros. p.137-139, p.146-147)
| Director | Role | Since | Other boards | Independent? | Attendance |
|---|---|---|---|---|---|
| Pradeep Kumar Verma | Chairman and MD, promoter | director since 2019 (re-designated 14-Jul-25; 5-year term from 21-Jun-25) | Accord Global Infra Pvt Ltd | No | Board marks lost in text extraction (p.40-41); audit committee 7 of 7 |
| Shalini Singh | WTD, promoter, spouse of MD | 18-Feb-15 | none | No | "All meeting attended" (AR p.31) |
| Amrendra Nath Shukla | Non-executive | 14-Jul-25 | none | No per prospectus and committee tables; AR p.40 text calls him "Non-Executive Independent" (inconsistent) | NRC 3 of 3; SRC 1 of 1; CSR 1 of 1 |
| Neelam | Independent | 14-Jul-25 (under 1 year at FY26) | none | Yes | Audit committee 7 of 7 |
| Dipakkumar C. Thakkar | Independent | 22-Oct-24 | Etsec Energy Pvt Ltd | Yes | Audit committee 6 of 7 (85.7%); NRC 2 of 3 (66.7%, below 75%) |
19 board meetings in FY26 (AR p.40-41), 12 of them by 16-Jan-26. Attendance marks did not survive text extraction on p.40-41 and no page image is staged for them: board attendance NOT FOUND IN DOCUMENT. Two executive directors are spouses. Independent directors are 2 of 5 (40%). No independent director has tenure over 10 years. No promoter-group member sits on another listed board. The audit committee chair has under a year on the board.
Fact to verify: the prospectus says the MD was disqualified under s.164(2)(a) from 1-Nov-16 to 31-Oct-21 after a company he directed (Inorbit Technofab) was struck off (Pros. p.33), and also that he has been a director of Accord "since 2019" (Pros. p.137). 2019 is inside the disqualification window. [INFERENCE] If both facts are right, his 2019 appointment fell in a period of disqualification. The prospectus says the supporting order could not be traced. The observation that separates the readings is the MCA DIN history. NOT FOUND IN DOCUMENT.

### 5B Committees (AR p.42-43)
Audit committee: Neelam (chair), Thakkar, Verma (MD); 7 meetings; 2 of 3 independent; the MD is a member. NRC: Thakkar (chair), Neelam, Shukla; 3 meetings. SRC: Shukla (chair), Singh, Neelam; 1 meeting. CSR: Singh (chair), Neelam, Shukla; 1 meeting. The board has full corporate-governance exemption as an SME-listed company (AR p.45). Whistle-blower policy exists; no complaint in the year (AR p.46).

### 5C Compensation (AR p.58; Note 2.3 p.82; Note 24 p.91)
| Item | Value |
|---|---|
| MD + WTD remuneration | 32.00 + 32.00 = 64.00 (FY25 36.00), +77.8% |
| As % of PAT, of PBT | 14.2%, 10.6% |
| Statutory headroom | 11% of net profit = about 66.6 lakh on PBT (calc; s.198 profit differs) |
| Ratio to median employee pay | 18.61 : 1 each; implied median about Rs 1.72 lakh a year (calc) |
| Non-managerial pay rise | average 74.06% vs managers 77.78%; median pay +10.45% (AR p.58) |
| KMP | CFO Gupta 12.00 (6.98 : 1); former CFO Samal 4.07 : 1; CS Sharma 0.88 : 1 |
| Headcount | 114 permanent on 31-Mar-26 (AR p.58). The prospectus counted 114 in total on 31-Dec-25: 104 permanent plus 10 contract (Pros. p.123). Same count a quarter apart, different definition. |
| Employee cost | 578.46 = 8.26% of revenue (FY25 4.58%) |
| Promoter family on payroll | Spouses only; no other relatives named |
| Director pay unpaid | Shalini Singh 29.52 of 32.00 accrued at year end (Note 2.3 p.82) |
Pay is concentrated in the two promoter directors and rose 77.8% in a year when PAT fell 24.2%. Headroom against the 11% cap is thin (calc, indicative). No special resolution for the pay appears in the AGM notice.

### 5D Shareholding
Promoters: 63,75,000 shares each, 30.98% each, 61.97% together (AR p.31; Note 3 p.85). The Note 3(c) total row prints 84.94% for 31-Mar-26, which is the pre-IPO figure (calc 127.5 / 205.73 = 61.97%). Promoters were 100% before FY25, 84.94% after the FY25 private round (44,339 shares, 15.06%), and 61.97% after the fresh IPO issue of 55,62,000 shares (AR p.39, p.85; Pros. p.167-168). There is no offer for sale and no promoter sale in any filing read. Dilution is not selling. Pledge: NOT FOUND IN DOCUMENT in the AR; the prospectus says none (B01). FII, DII and public split: NOT FOUND IN DOCUMENT (shareholding pattern absent, B00). No FLAG-PROMOTER-PRELIM on pledge or sale. The FY25 private round raised 999.84 lakh gross for 44,339 shares, about Rs 2,255 a share before the 50:1 bonus, or about Rs 44 a share after it (calc), 4% below the IPO price of Rs 46 (AR p.86, p.79).

### 5E Governance red-flag checklist
| Check | Result | Anchor |
|---|---|---|
| Whistle-blower complaints | None | AR p.46, p.74 |
| SEBI or regulator actions | None | AR p.48 |
| RPT committee | Audit committee approves RPTs | AR p.45 |
| Auditor fee ratio | Audit 1.50 vs non-audit NOT FOUND | AR p.92 |
| CSR compliance | Spent 7.71 vs required 7.70 | AR p.56-57 |
| s.143(12) fraud | None | AR p.45, p.73 |
| Material subsidiary auditor | n/a | AR p.39 |
| Secretarial observation | CHG-1 not filed on a Mercedes-Benz GLE vehicle charge; GNL-1 and adjudication filed. The prospectus disclosed the same lapse (Pros. p.33). The default was not cured in the six months between prospectus and secretarial audit (26-Aug-26). | AR p.44, p.50 |
| Secretarial report errors | "listing w.e.f. 01.04.2026" (AR p.52) vs listing 2-Mar-26; resolution-copy discrepancy language that fits another matter (AR p.50) | AR p.50-52 |
| Past compliance | Board-meeting date discrepancies in Board report vs MGT-7; no transfer list in FY15 MGT-7; rights-issue consideration records missing | Pros. p.33 |
| Promoter vehicle on company books | Mercedes-Benz GLE 300d on company finance (Note 5, Note 8) | AR p.86-87 |
| Internal audit | Done by the Finance Head and CFO until he left on 16-Jan-26; successor NOT FOUND IN DOCUMENT. Directors' Report says the function "needs to be strengthened" (p.47). | AR p.45, p.47 |
| Disclosure hygiene | AGM e-voting text still cites COVID-19 circulars (AR p.26); Antelp relationship and promoter % errors | AR p.26, p.82, p.85 |
Phase 5 verdict: YELLOW (Watch). The structure is promoter-couple, SME exemption, short-tenure independents, finance team under a year old. Positives: no pledge in filings, no promoter selling, CSR met, audit committee majority independent.
Kill Switch (informational): a human reviewer would not have reason to stop, because no fraud, pledge or selling is found; the reviewer would pause on the DIN timeline and the auditor switch.

## PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER (read last)

### 6A Narrative vs reality
| # | Claim (anchor) | Reality | |
|---|---|---|---|
| 1 | "FY2025-26 has been a landmark year ... successfully completed our IPO" (AR p.21) | Listed 2-Mar-26 at Rs 46, 357.37x subscribed (AR p.9); raised Rs 2,558.52 lakh | ✅ |
| 2 | "Our operating performance ... reflects the resilience of our business model and disciplined execution" (AR p.21) | Revenue -11.3%, PAT -24.2%, ROCE 35% to 13%, ROE 42.9% to 12.8% (AR p.64) | ❌ |
| 3 | "installed manufacturing capacity of over 1,200 MVA, serving more than 1,000 customers across India, the Middle East, the USA, Africa" (AR p.21) | Certified 900.36 MVA to 31-Dec-25 (Pros. p.123); top 10 customers 66.74% of nine-month revenue (Pros. p.111); FX earnings nil (AR p.55); export 97.15 lakh in nine months (Pros. p.179) | ❌ |
| 4 | "healthy financial position ... prudent cost management, disciplined working capital practices and a robust balance sheet" (AR p.63) | D/E 0.18 and current ratio 2.23 are real, helped by IPO money. Employee cost +59.9%, inventory days up, CFO from unwind | ✅ balance sheet, ❌ working capital and cost |
| 5 | Vendor approvals from UGVCL and Aditya Birla "During the year" (AR p.14, p.38) | UGVCL filed 24-Jun-26; Aditya Birla filed 6-Jul-26; both after year end and after the 29-May-26 audit report | ❌ timing |
| 6 | "Acquired 20,300 sq m of land" listed as FY26 milestone (AR p.13, p.14, p.38, p.63) | Filing 3-Jul-26; no land in PPE at 31-Mar-26 (AR p.77, Note 12 absent) | ❌ timing |
| 7 | "supported by a healthy order book" (AR p.37) | Rs 164.26 Cr at 18-Jan-26 is real (Pros. p.114), but 53% sits in one UGVCL PO and 19% in one LPPL PO, and no number is in the AR | partial |

### 6B Strategic priorities ("Future Roadmap", AR p.19)
Six priorities: manufacturing expansion, utility and infrastructure, renewable energy, global expansion, sustainable growth, innovation (AR p.19). Specific enough: one (expansion on the new land; 9-10 month build per AR p.33). Capital allocated: Rs 700.00 lakh of IPO money to the building, Rs 602.67 lakh to machinery, land from non-IPO sources (funding NOT FOUND IN DOCUMENT). Execution evidence in FY26: capex 146.19 lakh (AR p.79); IPO capex spend nil to 2-Sep-26 (AR p.32). The rest are directions with no number or date.

### 6C Metrics showcased vs absent
Showcased: 1,200+ MVA, 1,000+ customers, 357.37x subscription, 12+ years, ISO certificates, CPRI test of a 17.6 MVA inverter-duty transformer, UGVCL and Aditya Birla approvals, Moscow MoU, 20,300 sq m. Absent: order book, utilisation, production, customer concentration, export share, EBITDA by product, cash conversion, capex budget, the Rs 31 Cr deferral, guidance, return targets.

### 6D Tone and priority drift vs the prospectus
The prospectus led with a Rs 164.26 Cr order book, niche focus, 220kV/315 MVA capability through machinery capex, NHEV EV-charging, and named technology partners SGB-SMIT, Lucy Electric and Schneider (Pros. p.114, p.117, p.124). The AR leads with land, approvals, a Moscow MoU and generic industry text.

### 6E Quiet Abandonment Check
| # | Opening claim (quote) | Where it should show up | Class | Materiality |
|---|---|---|---|---|
| 1 | "Integrated Portfolio of ... EV Solutions" (AR p.6); "EV charging solutions" in every portfolio list | Revenue mix chart (p.63) has no EV line; segment note (p.83) has none; zero mention of NHEV (prospectus: "collaboration with NHEV for a pan-India network", Pros. p.117) | (b) silent drop of the NHEV link; EV is a label, not a line | Moderate if any value is credited to EV; B00 treats EV as claim-tier |
| 2 | "Presence across India, Middle East, USA, Africa & Asia" (AR p.6, p.17) | Annexure III: foreign exchange earnings "Nil" (AR p.55); Note 19 has no geography; prospectus says "we do not have any export operations" (Pros. p.123) yet shows export 97.15 lakh for nine months (Pros. p.179) | (a) implicit retraction: operations say nil | Moderate |
| 3 | Prospectus: capex "to manufacture up to 220kV, 315MVA power transformers" at the existing plant, with 700 sq m of the existing plant's 1,424 sq m free area to be used (Pros. p.76, p.117) | AR roadmap (p.19) names no EHV; AGM notice defers machinery, moves 700 lakh to civil work at a new site (AR p.32-33) | (c) hedged retreat: "defer and phase" is named, the EHV goal is dropped | High for the capacity and ladder thesis |
| 4 | "continues to enhance its production capabilities" and "1,200+ MVA" (AR p.62) | Capex 146.19 lakh in FY26 (p.79); nil machinery use of IPO money to 2-Sep-26 (p.32) | (c) hedged retreat | High |
| 5 | "technology collaborations and strategic partnerships" (AR p.8) | Named partners SGB-SMIT, Lucy Electric (to 28-Sep-27), Schneider EcoXpert (to 31-Dec-26) absent from the AR (Pros. p.124) | (b) silent drop of names and expiry dates | Low to moderate |
| 6 | "supported by a healthy order book" (AR p.37) | No order-book number in MD&A or notes | (b) silent drop of the metric the prospectus led with | Moderate |
| 7 | "disciplined working capital practices" (AR p.63) | Ratio table (p.64): inventory turnover 5.51 to 2.51; net capital turnover 9.21 to 2.46 | (a) implicit retraction | High |
| 8 | MD&A: "Independent internal audits are conducted periodically" and "internal control systems adequate" (AR p.65) | Directors' Report: "the internal audit system ... needs to be strengthened" (AR p.47); former CFO was the internal auditor (p.45) | (a) implicit retraction | Moderate |
| 9 | Revenue "moderation" described as "a calibrated business approach" (AR p.63) | The CFO's cause is a delayed customer project (Tr. p.5); the AR never says so | (b) silent drop of the explanation | High, because it decides whether FY26 is a pause or a loss of demand |

### Phase 6 summary
The narrative is mostly forward, thin on numbers, and blurs the year boundary: three of the "FY26 highlights" (UGVCL, Aditya Birla, land) happened in FY27. The prospectus promises that carry the thesis (EHV capability, NHEV, named partners, order-book emphasis) are not repeated.
Phase 6 verdict: YELLOW (Watch).

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION
| Strategy | Call | Top reasons |
|---|---|---|
| Value + Quality | FAIL | ROCE 13.3% FY26 (about 24% ex-cash, B01 memo); accounting score 5/10; cumulative CFO/PAT FY23-FY26 -0.18 (B01); strengths: D/E 0.18, unmodified audit |
| GARP | WATCHLIST (fullest) | For: revenue CAGR FY23-FY26 19.8%; ROE was 43% in FY25; Rs 164 Cr book at January and Rs 173 Cr at 30-Sep-26 (B00) against FY26 revenue Rs 70.07 Cr; operating leverage on a fixed-cost base built in FY26; D/E 0.18. Against: FY26 revenue -11.3%, PAT -24.2%; the AR holds no forward number; the prospectus FY26 working-capital table implied about Rs 119 Cr against Rs 70.07 Cr reported; 53% of the Jan-26 book is one UGVCL PO whose counterparty and approval status is unresolved. Separating observation: H1 FY27 audited results and cash flow (due Nov-26), and the billing pace of the UGVCL and LPPL orders. Position size, not shaded inputs, carries the caution (A25/OR-31). |
| Turnaround | WATCHLIST (fullest) | The business never lost money (PAT positive FY21-FY26, B01), so this is a dip-and-recovery, not a distress turnaround. For recovery: FY26 shortfall is attributed to a deferred Rs 31 Cr order of which 25 of 35 sets were already built (Tr. p.5) and gross margin rose 3.5 pp. Against: the AR does not state the cause; inventory and advances (Rs 17.7 Cr in WIP, FG and transit; Rs 6.24 Cr vendor advances) must convert; employee cost rose 59.9%. Test: revenue booked on those 25 sets in H1 FY27 and the Q1-Q2 FY27 unwind of advance and cash credit. |
| Capex-Led Growth | WATCHLIST | Land bought Jul-26 for Rs 10.67 Cr; Rs 700 lakh of IPO money redirected to civil work; machinery nil spent; plan 9-10 months; FY26 capex only 146.19 lakh; capacity claim unsupported (1,200 vs 900.36 MVA) |
| Cash Flow Compounder | FAIL | CFO FY24 and FY25 negative; FY26 positive only on the receivable release |
| Contrarian | FAIL | Price about Rs 86 vs IPO Rs 46 (operator, 2026-10-06); sentiment is not depressed |
| Insider Confidence | WATCHLIST | Promoters hold 61.97%, no sale, no pledge in filings; but no insider buying evidence, ESOP floor at face value, and finance team churn |
| Guidance Divergence | WATCHLIST | Management guides Rs 120-180 Cr (Tr.); the prospectus implied about Rs 119 Cr for FY26 and delivered Rs 70.07 Cr; the AR guides nothing. Credibility of the next guide rests on H1 FY27. |
Best-fit strategy: GARP with a capex-led, transition framing, as a WATCHLIST. No strategy gives a clean PASS from the backward evidence.

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot
Transformers, panels and compact substations maker (Bhiwadi, two units); listed 2-Mar-26 on BSE SME; FY26 revenue Rs 7,006.92 lakh (-11.3%), PAT 450.43 (-24.2%), net worth 4,886.85, cash 2,232.80 (91.4% IPO), borrowings 883.46, market price about Rs 86 (operator, 2026-10-06).

### Phase verdicts
| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | YELLOW |
| 2 Notes | YELLOW |
| 3 Financials | YELLOW (RED sub-flag on cash repeatability) |
| 4 Risk and MD&A | YELLOW (near RED on consistency) |
| 5 Governance | YELLOW |
| 6 Narrative | YELLOW |

### Quality score: 5.0 / 10
| Component (25% each) | Score /10 | Basis |
|---|---|---|
| Governance | 4 | Promoter-couple board; short-tenure independents; CFO twice replaced; internal auditor was the CFO; auditor switch with shared address; MD DIN timeline to verify; CHG-1 lapse repeated. Offsets: no fraud, no pledge, no promoter sale, CSR met |
| Accounting quality | 5 | B02 5/10; statements foot; provisioning and disclosure weak; Note 12 missing; vendor advance unexplained |
| Balance sheet | 6 | D/E 0.18, current ratio 2.23, ICR 12.0x; but cash is IPO money, net debt ex-IPO 690.87, demand-loan structure, inventory 29% of assets, BGs 118% of PAT |
| Earnings quality | 5 | Gross margin up 3.5 pp but EBITDA margin down 1.4 pp; CFO is an unwind; other income is only 4.75% of PBT (clean); revenue and profit fell |
Average: (4 + 5 + 6 + 5) / 4 = 5.0.

### Top 3 strengths
1. Balance sheet after the IPO: D/E 0.18, current ratio 2.23, debt down 49.5% (25.2% like-for-like) (AR p.64, p.77, B02).
2. Gross margin up 3.5 pp to 24.1% on lower revenue, with an unmodified audit, clean CARO on defaults and fraud, and statements that foot (AR p.78; p.72-74).
3. Real order evidence at the IPO (Rs 164.26 Cr, Pros. p.114) and a stated cause for the FY26 shortfall that fits the notes in scale (WIP, FG and transit 1,769.51 lakh, calc) [INFERENCE on fit].

### Top 3 red flags
1. Q4 cluster with thin disclosure: vendor advance 624.41 (counterparty NOT FOUND IN DOCUMENT), stock in transit 619.50 with no visible P&L offset, cash credit drawn while Rs 20.4 Cr of IPO money sat idle (AR p.87, p.89-90, p.73).
2. Cash conversion is a receivable unwind: CFO 869.50 vs -479.83 without the release; two-year CFO 4.9% of PAT (AR p.79).
3. Narrative reliability: six MD&A contradictions, CARO vs Directors' Report on internal audit, FY27 events presented as FY26, "1,200+ MVA" against a certified 900.36 MVA, and an order book whose largest line (UGVCL, Rs 87.50 Cr) predates the vendor registration by five months and is only partly covered by it.

### Key monitorables for next quarter (details in YAML)
H1 FY27 results (Nov-26): vendor advance and transit stock unwind; receivable days; cash credit and IPO unused balance; BG level; employee cost; inventory days on one stated basis; first spend on the building; clarity on the UGVCL PO counterparty.

### Load-bearing facts: what the AR does and does not settle
| LBF | AR evidence | Status |
|---|---|---|
| 1 Guidance vs delivery | AR carries no guidance and no order-book figure. Guidance sits only in the transcript. Prospectus FY26 working-capital table implied about Rs 119 Cr FY26 revenue (calc, [INFERENCE]). Order book Rs 164.26 Cr (18-Jan-26) is dominated by UGVCL 87.50 + LPPL 31.50 + one 5,600 kVA line 15.23 = Rs 134.23 Cr, 81.7% (calc, Pros. p.115). | Open: bridge 164.25 to 159 to 173 and H1 inflow 77 belong to stage 5; AR adds the concentration and approval-date facts |
| 2 Loans and advances | 890.45 = vendor advances 624.41 (70.1%), revenue authorities 194.64, retention 56.17, other loans and advances 15.23. No vendor named; no related-party advance (Note 2.3 shows none; AOC-2 advance column "-"); CARO iii nil. | Counterparty and purpose: NOT FOUND IN DOCUMENT. Related-party link: none evidenced. |
| 3 IPO use and conduct | Rs 700.00 lakh machinery to building, at a new site (AR p.32-33). Machinery nil used; WC 931.59 used (93.2%) by 2-Sep-26. ESOP 5,00,000 options, price floor Rs 10 (AR p.35). Customer names withheld on two orders: not in the AR. Tipco document and SRIGEE code: not in the AR. | Issue-expense mismatch 276.20 vs 255.85 found. Funding source for the land NOT FOUND IN DOCUMENT. |
| 4 Cash conversion | Repeatable: no. CFO is the release; inventory days 146 (cost basis) or 111 (revenue basis), not 179. | Resolved against repeatability from the AR; H1 FY27 decides |

## ```yaml block
See the block below and runs/accord-2026-10-06/outputs/blocks/B03-ardeep.yaml.

```yaml
stage: B03-ardeep
company: "ACCORD"
run_date: "2026-10-06"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "rating ABSENT"
  - "shareholding ABSENT: promoter pledge, FII/DII split NOT FOUND IN DOCUMENT; AR gives 61.97% promoters only (AR p.85)"
  - "results pp3-19 scan-only (not used; AR audited statements used)"
  - "listing-period announcements not staged"
  - "VOLTAMP no transcripts; one concall only"
  - "AR Note 12 (PPE schedule) absent from the printed document (AR p.88): gross block and useful lives NOT FOUND IN DOCUMENT"
  - "AR holds no order-book number, no production or utilisation figure, no customer concentration table: NOT FOUND IN DOCUMENT (prospectus supplies Pros. p.114-115, p.123, p.111)"
  - "board attendance marks on AR p.40-41 lost in text extraction and no page image staged: board attendance NOT FOUND IN DOCUMENT"
  - "vendor-advance counterparty, ageing and purpose NOT FOUND IN DOCUMENT (LBF-2)"
  - "non-audit fees paid to the auditor NOT FOUND IN DOCUMENT; internal auditor after 16-Jan-26 NOT FOUND IN DOCUMENT"
  - "funding source of Rs 1,067 lakh land NOT FOUND IN DOCUMENT; counterparty on UGVCL ROBUST 2.0-X PO (Rs 87.50 Cr) NOT FOUND IN DOCUMENT"
flags:
  - {type: FLAG-CASH, reason: "FY26 CFO 869.50 lakh is a receivable release (+1,349.33); without it CFO is -479.83; two-year CFO 51.40 vs PAT 1,044.80 (4.9%); 91.4% of cash 2,232.80 is unspent IPO money; inventory days 146 on cost basis, 111 on revenue basis (AR p.79, p.73, p.64)"}
  - {type: FLAG-OPERATOR-FIGURE, reason: "Operator plant ceiling Rs 150-200 Cr, utilisation 75-80% and inventory days 179 are not in the AR and do not reconcile to filed figures: prospectus utilisation 69.78% on 900.36 MVA (extrapolated), AR claims 1,200+ MVA; AR inventory turnover 2.51 = 145 days (Pros. p.123; AR p.64)"}
  - {type: FLAG-TIMING, reason: "AR presents UGVCL approval (filed 24-Jun-26, 500 kVA only), Aditya Birla approval (filed 6-Jul-26) and the Tijara land (filed 3-Jul-26) as FY26 events; UGVCL PO of Rs 87.50 Cr (53% of the Jan-26 order book) is dated 17-Jan-26, before the registration (AR p.14, p.38, p.63; Pros. p.115)"}
phase_verdicts: {p1: "YELLOW", p2: "YELLOW", p3: "YELLOW (RED sub-flag: cash repeatability)", p4: "YELLOW (near RED on consistency)", p5: "YELLOW", p6: "YELLOW", p7_best_fit: "GARP with capex-led transition framing: WATCHLIST, no clean PASS"}
overall_quality: 5.0
quality_components: {governance: 4, accounting: 5, balance_sheet: 6, earnings: 5}
kill_switch_notes:
  - "P1: a human reviewer would not have reason to stop, because the opinion is unmodified and CARO is clean on defaults and fraud; would want the 2024 auditor switch (shared address and email) checked"
  - "P2: would not have reason to stop, because no profit-moving mismatch is proven; would want the vendor ledger for the Rs 624.41 lakh advance before sizing"
  - "P3: would have reason to pause, not stop, because FY26 CFO is a receivable unwind and two-year CFO is 4.9% of PAT; cleared or confirmed by H1 FY27 cash flow"
  - "P4: would not have reason to stop, because six MD&A contradictions are disclosure sloppiness; would discount narrative text and lean on filed numbers"
  - "P5: would not have reason to stop, because no fraud, pledge or promoter sale is found; would pause on the MD's DIN disqualification window (2016-2021) overlapping his 2019 board entry"
triple_pass_verification:
  verified: 15
  discrepancies: []
  extensions:
    - "inventory turnover FY25 5.51 is revenue/average inventory while FY26 2.51 is cost/average inventory; like-for-like 5.51 to 3.30 (revenue basis) or 4.37 to 2.51 (cost basis) (AR p.64; calc)"
    - "DSCR 0.81 not reproducible; interest cover 12.0x; formula NOT FOUND IN DOCUMENT (AR p.64)"
missing_risks:
  - "Order-book concentration and approval gap: UGVCL ROBUST 2.0-X Rs 87.50 Cr (53% of Rs 164.26 Cr) ordered 17-Jan-26, registration 24-Jun-26 for 500 kVA only (Pros. p.115; filing 20260624)"
  - "Customer concentration: top 5 73.62% and top 10 84.16% of FY25 revenue; 48.10% and 66.74% for nine months FY26, none in AR (Pros. p.111)"
  - "Customer-site delay and deferral of a Rs 31 Cr order (25 of 35 sets built); AR calls the fall a 'calibrated business approach' (Tr. p.5; AR p.63)"
  - "Working-capital intensity: vendor advance 624.41, transit stock 619.50, MSME payables 1,494.94, receivables over 6 months +214% (AR p.88-90)"
  - "Warranty exposure: bank guarantees 532.46 (118% of PAT) with no warranty provision (AR p.83)"
  - "IPO money idle and objects changed: machinery nil used against 1,302.67, WC 93.2% used in five months, 700 moved to civil work (AR p.32-33)"
  - "Finance and control churn: CFO replaced twice, internal auditor was the departed CFO, finance heads joined 13-Sep-25 (Pros. p.148; AR p.40, p.45)"
  - "Capacity claim 1,200+ MVA against certified 900.36 MVA (AR p.6; Pros. p.123)"
  - "Related-party dependence: ABL Electricals is lender, supplier and personal guarantor (AR p.82; Pros. p.177-178)"
  - "Compliance history: CHG-1 not filed (repeated in secretarial audit), MD DIN disqualification 2016-2021 vs director since 2019, board-meeting discrepancies (AR p.44, p.50; Pros. p.33, p.137)"
  - "Section 43B(h) MSME payment-window risk on 1,494.94 (AR p.88)"
  - "Export and FX claims against nil FX earnings (AR p.55 vs p.6; Pros. p.179)"
guidance_table:
  - {claim: "supported by a healthy order book", number: "none in AR; Rs 164.26 Cr at 18-Jan-26 in prospectus (Pros. p.114)", timeframe: "FY27", credibility: "unquantified in AR; FY26 revenue fell 11.3% with a Rs 164 Cr book at January"}
  - {claim: "IPO working-capital use", number: "Rs 275.00 lakh FY26, Rs 725.00 lakh FY27 (Pros. p.75)", timeframe: "FY26-FY27", credibility: "Rs 242-262 lakh used by 31-Mar-26; 931.59 lakh (93.2%) by 2-Sep-26 (AR p.32); delivered early"}
  - {claim: "IPO machinery spend", number: "Rs 1,302.67 lakh, all FY27 (Pros. p.75)", timeframe: "FY27", credibility: "nil used to 2-Sep-26; 700.00 lakh moved to building (AR p.32); slipped"}
  - {claim: "Prospectus FY26 working-capital table: receivable days 96, inventory days 83, payable days 56", number: "implied FY26 revenue about Rs 119 Cr (calc, INFERENCE)", timeframe: "FY26", credibility: "delivered receivable days 113, inventory days 146 (cost basis), revenue Rs 70.07 Cr; missed"}
  - {claim: "Construction of building/civil structure at Tijara", number: "9-10 months from 26-Sep-26 approval (AR p.33)", timeframe: "to about Jul-27", credibility: "no build history; risks named by company (AR p.34)"}
  - {claim: "Installed capacity over 1,200 MVA", number: "1,200+ MVA (AR p.6, p.21)", timeframe: "FY26", credibility: "certified 900.36 MVA to 31-Dec-25 (Pros. p.123); no filed support for the step up"}
  - {claim: "FY27 revenue guidance (transcript only, not in AR)", number: "Rs 120-180 Cr; PAT 9-11% (Tr. lines 480-491)", timeframe: "FY27", credibility: "not testable in AR; stage 5"}
monitorables:
  - {metric: "Vendor advances (Note 17)", threshold: "below Rs 300 lakh at 30-Sep-26 with matching inventory inflow; above Rs 600 lakh unexplained = unresolved", where: "H1 FY27 balance sheet, Nov-26 results", why: "LBF-2: 624.41 lakh, 70% of L&A, counterparty unknown"}
  - {metric: "Stock in transit (Note 14)", threshold: "nil or converted to RM/FG by 30-Sep-26; payable cleared", where: "H1 FY27 inventory note", why: "619.50 lakh with no visible P&L offset; separates payable-funded transit stock from inflated assets"}
  - {metric: "Receivable days on H1 revenue", threshold: "closing receivables at or below Rs 28.9 Cr (100 days on Rs 52.68 Cr H1 revenue annualised, calc)", where: "H1 FY27 results", why: "H1 revenue +90% will rebuild receivables; FY26 CFO was the unwind"}
  - {metric: "Operating cash flow H1 FY27", threshold: "positive and above 50% of H1 PAT", where: "H1 FY27 cash flow statement", why: "two-year CFO 4.9% of PAT; FLAG-CASH"}
  - {metric: "Inventory days, one stated basis", threshold: "cost basis at or below 120 days (FY26 146; FY25 83)", where: "H1 FY27 inventory note and ratios", why: "turnover basis mismatch in the AR; days rose 45% to 75%"}
  - {metric: "IPO unused balance and building spend", threshold: "at least Rs 350 lakh of the 700 lakh building budget spent by 31-Mar-27; no second object change", where: "quarterly IPO utilisation statement; AR FY27", why: "unused 1,371.08 lakh at 2-Sep-26; machinery nil; 9-10 month build"}
  - {metric: "Cash credit drawn while IPO cash idle", threshold: "cash credit below Rs 300 lakh at 30-Sep-26 (31-Mar-26: 621.37; 31-Dec-25: 167.42)", where: "H1 FY27 Note on borrowings", why: "cost of carry; Q4 draw of 453.95 lakh"}
  - {metric: "Bank guarantees and warranty claims", threshold: "BG growth no faster than revenue; any warranty provision booked", where: "contingent liability note", why: "532.46 lakh, 118% of PAT, nil provision"}
  - {metric: "UGVCL ROBUST 2.0-X PO (Rs 87.50 Cr): counterparty, ratings covered, billing", threshold: "at least 25% billed by 31-Mar-27; counterparty named", where: "order filings, Q3-Q4 FY27 updates", why: "53% of Jan-26 book; registration of 24-Jun-26 covers 500 kVA only"}
  - {metric: "Employee cost / revenue", threshold: "at or below 8.3% as revenue rises (FY26 8.26%, FY25 4.58%)", where: "H1 FY27 P&L", why: "fixed-cost base built ahead of revenue; operating leverage test"}
  - {metric: "Related-party loans and ABL balance", threshold: "ABL loan at or below 69.64 lakh; no new interest-free promoter money beyond 182.78", where: "RPT note H1 FY27", why: "promoter funds repayable on demand; arm's-length support NOT FOUND"}
  - {metric: "Governance items", threshold: "independent internal auditor named; MD DIN history confirmed; CHG-1 filed", where: "Reg 30 filings; MCA", why: "internal auditor was the departed CFO; 2019 board entry inside 2016-2021 disqualification window"}
ar_new_downstream_entities:
  - {name: "Antelp Corporation Private Limited", where_in_ar: "Note 2.3 D and E p.82; AOC-2 p.54 (sale of goods 29.44 lakh; debtor 29.44; described as 'KMP relative has an interest')", entity_type: "related-party customer"}
  - {name: "Aditya Birla Renewables Limited", where_in_ar: "Recent Business Highlights p.14; Chairman's letter p.21; Directors' Report p.38; MD&A p.62 (vendor approval; filed 6-Jul-26)", entity_type: "customer vendor approval, renewable developer"}
  - {name: "Western Administrative District of the City of Moscow", where_in_ar: "p.14, p.21, p.38, p.62 (MoU, no value or date)", entity_type: "foreign government MoU counterparty"}
  - {name: "Great Value Institute of Education (CSR00009173)", where_in_ar: "CSR annexure p.57 (Rs 7.71 lakh; implementing agency)", entity_type: "CSR implementing agency"}
  # customers over 10% of revenue: NOT FOUND IN DOCUMENT in the AR (prospectus gives only unnamed top 5 and top 10 percentages, Pros. p.111)
strengths_top3:
  - "Post-IPO balance sheet: D/E 0.18, current ratio 2.23, interest cover 12.0x, debt down 49.5% (25.2% like-for-like) (AR p.64, p.77)"
  - "Gross margin up 3.5 pp to 24.1% on lower revenue; unmodified audit; CARO clean on defaults and fraud; statements foot and cash flow ties to balance sheet (AR p.78-79, p.72-74)"
  - "Order evidence at IPO Rs 164.26 Cr (Pros. p.114) and a stated cause of the FY26 shortfall (deferred Rs 31 Cr order, 25 of 35 sets built, Tr. p.5) that fits balance-sheet scale (WIP+FG+transit 1,769.51 lakh) [INFERENCE on fit]"
red_flags_top3:
  - "Q4 cluster with thin disclosure: vendor advance 624.41 lakh with no counterparty, stock in transit 619.50 with no visible P&L offset, cash credit drawn while 2,040.21 of IPO money sat unspent (AR p.87, p.89-90, p.73)"
  - "Cash conversion is a receivable unwind: CFO 869.50 vs -479.83 without the 1,349.33 release; two-year CFO 4.9% of PAT (AR p.79)"
  - "Narrative reliability: six MD&A contradictions, CARO vs Directors' Report on internal audit, FY27 events shown as FY26, 1,200+ MVA vs certified 900.36 MVA, and a 53% order-book line (UGVCL) dated before the registration that only partly covers it (AR p.63-65, p.47, p.74; Pros. p.115, p.123)"
best_fit_strategy: "GARP with capex-led transition framing (WATCHLIST); Turnaround is a dip-and-recovery reading only"
one_line_verdict: "Statements foot and the post-IPO balance sheet is clean, but FY26 cash flow is a receivable unwind, Rs 12.4 Cr of Q4 advances and transit stock are unexplained, and the AR narrative carries no order book, no utilisation and FY27 events labelled FY26: best fit GARP WATCHLIST, size small until H1 FY27 cash flow and the vendor-advance unwind are seen."
analyst_note: "Three facts stage 5 needs from this report. (1) Order-book quality: of the Rs 164.26 Cr January book, UGVCL ROBUST 2.0-X is Rs 87.50 Cr (53%), LPPL-02 Rs 31.50 Cr (19%, size and 35-count match the Rs 31 Cr deferred order [INFERENCE]), one 5,600 kVA line Rs 15.23 Cr; UGVCL registration (24-Jun-26) is 500 kVA only. (2) Capacity: AR says 1,200+ MVA; certified 900.36 MVA; FY26 utilisation 69.78% is extrapolated; management's 75-80% and Rs 150-200 Cr ceiling do not reconcile to each other. (3) The prospectus WC table implied about Rs 119 Cr FY26 revenue (calc); reported Rs 70.07 Cr. Inventory turnover 5.51 to 2.51 mixes bases; use cost basis 83 to 146 days. All AR figures Rs lakh; prospectus Rs thousand converted by /100."
```
