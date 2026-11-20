# STAGE 2 NOTES, PASS 1 OF 3 (FULL EXTRACTION): Kwality Pharmaceuticals Ltd (KPL)

Run: kpl-2026-11-15 | Model: claude-sonnet-5-5 | Source: Annual_Report_2026.pdf (AR FY2025-26, 242 pages) via the page-marked .txt.

## READING BASIS AND UNITS

- UNIT: every AR figure is in INR LAKHS (face of each statement: "(₹ in lakhs)", consolidated BS p.184, P&L p.187, notes p.194; standalone BS p.113). No figure here is converted. 100 lakhs = 1 Cr. Percentages and ratios are unit-free. Items marked "derived" are my arithmetic on AR figures; the inputs are anchored.
- Page anchors are the PDF page markers in the .txt ("[page N]" starts page N). The printed page number is 3 lower for the consolidated block and 3 lower for the standalone block (e.g. PDF p.211 = printed 208). Anchors read "(Note N, p.PDF)".
- Scope: consolidated notes (Notes 1-41, p.194-240) read in full. Standalone notes (p.123-173) were read where they differ. Standalone-only differences are named in each section and listed in Section 13.
- Prior-year references (AR FY2025 .txt, line numbers given) are used only to build 3-year trends. FY24 figures come from AR FY2025 comparatives.
- Group = KPL + one 51% foreign subsidiary (Kwality Pharmaceuticals Africa Limitada, Mozambique). Single segment (Note 2.2(d), p.197).

Statement anchors used throughout (consolidated, ₹ lakhs):
- Revenue 50,308.34 (FY25 37,019.70; FY24 30,717.18). PBT 8,949.21 (5,413.99; 3,109.89). PAT 6,734.60 (3,980.27; 2,361.59). Net worth (total equity) 32,992.09 (26,239.59). (P&L p.187-189; BS p.185; AR FY25 consol P&L lines 10130, 10179.)
- CFO 1,658.62 (5,271.78; 4,298.28) (CFS p.190-191; AR FY25 line 10312).

---

## 1. ACCOUNTING POLICIES AND CHANGES

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1.1 | Depreciation: written-down-value method, "rates arrived at based on the useful life ... prescribed under Schedule II". Plant & Machinery 20 years; Building 20-30; Furniture 10; Vehicles 8; Computers 3; Laboratory equipment 10-20; Office equipment 5-10; Lift 8; Electric fittings 10. Freehold land not depreciated. No change in lives disclosed this year. The 20-year P&M life is longer than the 15-year general P&M life I recall from Schedule II (external recollection, NOT in the document; verifier to check). | Note 2.2(g), p.198 | 🟡 |
| 1.2 | New policy line: Intangible "Bioequivalence Study" acquired in FY26, amortised over 5 years straight-line. Gross 433.89 added; amortisation charged only 2.96 in the year (about 0.4 months of a 5-year life; run-rate 86.78 a year, derived). Technical know-how 171.00 (FY25) charged 17.10 (10-year life, derived). Policy text does not state the Ind AS 38 research/development test used to capitalise a bioequivalence study. | Note 2.2(g) p.198; Note 4 p.208; Note 4(a) p.209 | 🟡 |
| 1.3 | Ind AS 116 lease accounting recognised for the first time in FY26 as a PRIOR-PERIOD ADJUSTMENT under Ind AS 8, "opening balances ... as at 1 April 2025 adjusted". Net credit to opening retained earnings 4.47 (= unamortised ROU asset on upfront lease 10.03 less excess lease liability over ROU 5.56). FY25 comparatives were not restated (FY25 BS and P&L show no lease items). A direct credit to reserves bypassing P&L. ROU asset: cost 28.56, depreciation 0.52, net 28.04; lease liability 23.99 non-current + 0.06 current; lease interest 2.11. Lease discount rate: NOT FOUND IN DOCUMENT. | Note 2.2(n) p.201-202; Note 3 p.206; Note 18 p.218; Note 22 p.221; Note 31 p.224; SOCE p.193 | 🟡 |
| 1.4 | Revenue recognition: sale recognised on dispatch/hand-over to transporter (domestic) and on shipped-on-board per bill of lading (export). Policy cites "substantial risk and rewards of ownership" (old IAS 18 wording), not the Ind AS 115 five-step or control-transfer test. Export recognition at shipment is standard FOB-type timing; Incoterms NOT FOUND IN DOCUMENT. Revenue is net of returns, trade allowances, rebates, discounts. | Note 2.2(o), p.202 | 🟡 |
| 1.5 | Impairment of financial assets policy reads "objective evidence ... impaired" (incurred-loss wording). No Expected Credit Loss (ECL) model, matrix or provision rate is described anywhere in the notes. Zero provision on receivables in both years (see Section 4). | Note 2.2(p), p.202-203 | 🔴 |
| 1.6 | Inventory at lower of cost and NRV, weighted average cost; allowance factors listed (shelf life, ageing, discontinuances) but no allowance amount; "Stock written off" line is nil in both years. | Note 2.2(h), p.198-199; Note 8 p.211 | 🟡 |
| 1.7 | Deferred tax: Note 6 footnote states the company "changed its method of calculating deferred tax from the Profit and Loss (P&L) approach to the Balance Sheet approach in accordance with the requirements of [specify applicable accounting standard, e.g., Ind AS 12 ..." The bracketed template text is unfilled in a signed audited note. Effective FY2024-25. | Note 6, p.210 | 🟡 |
| 1.8 | Operating cycle declared as twelve months. Receivable days at year end are 203 (derived, Section 4), and 1,566.38 of receivables are over one year old (derived: 1-2y 1,002.09 + 2-3y 89.74 + >3y 474.55 + 6m-1y bucket is NOT included; see Section 4 for buckets), yet all receivables sit in current assets. | Note 2.2(b), p.197; Note 9(a) p.212 | 🟡 |
| 1.9 | Policy for exceptional items cites the Labour Codes (notified 21 Nov 2025) and a quantified incremental charge of 82.94 for past service cost on gratuity. Quantified P&L impact. See cross-note conflict on cause in Section 12. | Note 2.2(m), p.201; Note 33 p.226 | 🟡 |
| 1.10 | Judgement note: lists gratuity AND leave encashment as defined benefit judgements, but only gratuity is disclosed (leave-encashment liability and actuarial table NOT FOUND IN DOCUMENT). Impairment-test assumptions (growth, discount rate): NOT FOUND IN DOCUMENT; no goodwill on the balance sheet. Capitalisation threshold: NOT FOUND IN DOCUMENT. | Note 2.2(s), p.204-205 | 🟡 |
| 1.11 | Standalone-only: investment in subsidiary held at cost less impairment ("elected to recognize ... at cost"). | Standalone policy g, p.126 | 🟢 |

Segment: single segment, pharmaceutical formulations (Note 2.2(d), p.197). No entity-wide geography or customer disclosure beyond export/domestic split.

---

## 2. RELATED PARTY TRANSACTIONS (Note 40 consolidated p.237-239; standalone Note 41 p.170-171 is identical)

All figures ₹ lakhs.

| Party | Relationship | Nature | FY26 | FY25 | YoY |
|---|---|---|---|---|---|
| Ramesh Kumar | MD (promoter) | Remuneration | 84.00 | 72.00 | +16.7% |
| Ajay Kumar Arora | WTD (promoter) | Remuneration | 84.00 | 72.00 | +16.7% |
| Aditya Arora | WTD and CFO | Remuneration | 54.00 | 48.00 | +12.5% |
| Geeta Arora | WTD | Remuneration | 36.00 | 30.00 | +20.0% |
| Anju Arora | WTD | Remuneration | 36.00 | 30.00 | +20.0% |
| Kanika Arora | Relative of director | Remuneration | 3.00 | 3.00 | 0% |
| Aastha Seth | Relative of director | Remuneration | 4.20 | 4.20 | 0% |
| Geetika Thukral (Arora) | Relative of director | Remuneration | 6.00 | 6.00 | 0% |
| Ramesh Kumar | MD | Rent | 1.08 | 1.08 | 0% |
| Ajay Kumar Arora | WTD | Rent | 1.08 | 1.08 | 0% |
| Independent directors (8 names) | IDs | Sitting fees | 7.50 | 4.37 | +71.6% |
| Iair Infocom Pvt Ltd | "Director interested" | Purchase of services | 20.25 | nil | NEW |
| Iair Infocom Pvt Ltd | "Director interested" | Sale of machine and spares | 6.40 | nil | NEW |
| Kaler Biopharmachem Pvt Ltd | "Director interested" | Sale of goods | 121.48 | nil | NEW |
| Kaler Biopharmachem Pvt Ltd | "Director interested" | Sale return | 262.75 | nil | NEW |
| Kwality Pharmaceuticals Africa Limitada | Subsidiary (51%) | Sale of goods | 26.68 | nil | NEW |
| Same subsidiary | Subsidiary | Investment balance | 354.78 | 354.78 | 0% |
| Same subsidiary | Subsidiary | Debtors balance | 116.73 | 159.42 | -26.8% |

Derived totals and checks:
- Key-person remuneration to executive directors: 84+84+54+36+36 = 294.00 (FY25 252.00) = equals Note 30 "Directors Remuneration" 294.00 (p.224). Relatives' pay 13.20 both years sits in salaries. Total promoter-family pay 307.20 vs 265.20 (+15.8%) = 3.43% of PBT (FY25 4.90%) = 0.61% of revenue. 🟢 on level; the family holds five whole-time/relative pay lines.
- Sitting fees 7.50 ties to Note 32 "Director's Sitting Fees" 7.50 (p.225). 🟢
- Rent paid to promoters 2.16 a year in total (derived). The audit report (CARO) says the registered office and main Amritsar factory are on leased premises owned by the promoters Mr Ramesh Arora and Mr Ajay Arora, initial lease term 49 years. Rent of 2.16 a year for the main plant site looks nominal against 1,960.97 of FY26 PPE depreciation; fair-value basis NOT FOUND IN DOCUMENT. 🟡 (CARO (i)(c) p.104; Note 40 p.239)
- RPTs other than remuneration, rent and fees: gross 20.25 + 6.40 + 121.48 + 262.75 = 410.88 = 0.82% of revenue (derived). Net sale to Kaler is negative: 121.48 - 262.75 = -141.27. The return exceeds the sale in a year when the prior-year comparative is nil. Cause, return dates and credit notes NOT FOUND IN DOCUMENT. 🟡
- New related parties this year: Iair Infocom, Kaler Biopharmachem (both nil in FY25). Their ownership and which director is "interested" NOT FOUND IN DOCUMENT. 🟡
- Collateral from promoters: bank facilities are "collaterally secured by Equitable mortgage" of an industrial property (killa no. 152/5) and a residential property (House No. 32, Amritsar) "owned by Mr. Ramesh Arora and Mr. Ajay Arora, directors of the Company". Promoter-provided security is not shown in the RPT table (no guarantee fee or counter-guarantee line). 🟡 (Note 17 p.148-149, standalone)
- Loans to promoter entities: none ("Loans & Advances to Related Parties" nil, Note 7 p.210-211; CARO (iii) no loans or guarantees given, p.105).
- Related party borrowings: nil (Note 16 p.217; Note 19 p.219).
- Subsidiary: Note 1 says the company "invested in the share capital and granted loans to the foreign subsidiary" (p.194), yet no loan balance appears in the RPT table (only investment 354.78 and debtors 116.73). Loan amount NOT FOUND IN DOCUMENT. 🟡
- Consolidated-statement carry-over: Note 40 in the CONSOLIDATED set still shows the subsidiary investment (354.78) and subsidiary debtors (116.73) and the 26.68 intra-group sale, which are eliminated on consolidation (consolidated receivables 28,005.24 vs standalone 28,121.97; difference 116.73). The consolidated RPT note is a copy of the standalone one. 🟡 (Note 40 p.238-239; BS p.184; standalone BS p.114)
- CARO (xiii): auditor states all RPT comply with Sections 177 and 188 (p.108). 🟢
- Auditor item (fact 2): auditor Vijay Mehra & Co (FRN 001051N), partner CA Amit Handa. Opinion on standalone and consolidated statements unmodified; no KAM section found in either report; CARO states "There has been no resignation of the statutory auditors during the year" (clause xviii, p.108). The 12 Nov 2026 resignation in the web brief falls after this AR (19 May 2026 report date) and is not in the document. Audit fee 8.00; other services 5.42 (FY25 8.00; 4.50) (Note 32 p.225). 🟢 on fee level. CARO (vii)(a): "there were delays in the deposit of certain GST and TDS dues and in filing the related statutory returns ... regularised ... through payment of the applicable interest and late fees" (p.105) 🟡. Consolidated report Other Matters: the subsidiary was NOT audited by the group auditor; the auditor relied on "unaudited Financial Results" supplied by the Board and called the subsidiary "not material to the group" (p.178) 🟡.

---

## 3. CONTINGENT LIABILITIES (Note 34 consolidated p.226-227; standalone Note 35 p.158-159)

| Item | Amount (₹ lakhs) | Stage | Company assessment |
|---|---|---|---|
| 1. Order 14/GST/ADC/JAL/2024-25 under S.74(9) CGST: alleged erroneous IGST refund FY18-FY23. Tax 315.02758 + penalty 315.02758 = 630.06 (₹6,30,05,516). Interest levied, not quantified | 630.06 plus unquantified interest | Commissioner (Appeals) DISMISSED the appeal against the company; writ CWP-12033-2026 filed in Punjab and Haryana High Court seeking stay | No provision shown; described as "under litigation" |
| 2. Show Cause Notice AE/51/2024-25 under S.74 and 122 CGST: ITC alleged wrongly availed FY18-FY23. ITC 1,513.03 + penalty 1,513.03 = 3,026.07 (₹30,26,06,840) | 3,026.07 | Writ CWP-34165-2024; High Court STAYED passing of adjudication order | No provision |
| 3. Three DRC-07 orders dated 30/12/2024 (FY18 penalty 2.81; FY20 tax 6.75 + penalty 6.75; FY21 tax 12.62 + penalty 12.70) | 41.64 (derived: 2.81+6.75+6.75+12.62+12.70 = 41.63; rounding) | Appeals pending | No provision |
| TOTAL disclosed | 3,697.75 (FY25 3,697.75; FY24 34.93) | | |

Computation checks (derived): items 1+2+3 = 630.06 + 3,026.07 + 41.64 = 3,697.77, ties to 3,697.75 within rounding.
- Total as % of consolidated net worth 32,992.09 = 11.2%; of standalone net worth 33,337.24 = 11.1%; of FY26 PAT 6,734.60 = 54.9%.
- Single item above 10% of net worth: none (largest, 3,026.07 = 9.2%). Combined GST items are 11.2%. 🟡
- The total of 3,697.75 was identical at 31 Mar 2025 and 2026. FY24 was 34.93, so ~3,662.82 of exposure appeared in FY25 (AR FY25 Note 33, line 8815-8820). Both periods show the same cumulative disclosure even though item 1 has since moved to an adverse appellate order. 🟡
- Company keeps an IGST-refund receivable of 852.37 (Note 12, p.213; FY25 1,279.37) and balances with revenue authorities of 1,785.21 (FY25 995.03) (Note 13, p.214). Item 1 alleges "erroneous refund of IGST" for FY18-FY23. Link between the dispute and the 852.37 asset NOT FOUND IN DOCUMENT. 🟡
- Income-tax, customs, excise disputes: none disclosed. Guarantees for subsidiary: none (CARO (iii) p.105). Capital commitments: NOT FOUND IN DOCUMENT. Litigation provisions: none (provisions in Notes 17 and 23 are gratuity only).
- Companies' Rule 11(a) statement by auditor: impact of pending litigations disclosed (p.102).

---

## 4. TRADE RECEIVABLES (load-bearing fact 3)

Note 9 consolidated p.211-212 (₹ lakhs). Standalone Note 10 p.140-141.

| Bucket (from due date) | FY26 | FY25 | FY24 (AR FY25 Note 9(b) p.221) |
|---|---|---|---|
| Less than 6 months | 24,974.95 | 12,547.50 | 8,232.97 |
| 6 months to 1 year | 1,463.91 | 1,152.47 | 539.35 |
| 1-2 years | 1,002.09 | 566.17 | 1,768.15 |
| 2-3 years | 89.74 | 517.50 | 648.46 |
| More than 3 years | 474.55 | 646.94 | 249.65 |
| TOTAL | 28,005.24 | 15,430.58 | 11,438.57 |
| Provision (doubtful/ECL) | nil | nil | nil |
| Credit-impaired / significant increase in credit risk | nil | nil | nil |

Derived metrics:
- Over 6 months: FY26 3,030.29 = 10.82% of total; FY25 2,883.08 = 18.69%; FY24 3,205.61 = 28.02%. Over-6-month dues are flat in rupees (+5.1% vs FY25) but the under-6-month bucket doubled (+99.1%) while revenue grew 35.9%. The share of old debt fell because the new-debt denominator exploded, not because old debt cleared. 🟡
- Over 2 years: FY26 564.29 (2-3y 89.74 + >3y 474.55); FY25 1,164.44; FY24 898.11. About 600 of old balances disappeared between FY25 and FY26 with no provision, no write-off line in Note 32, and no ECL charge (collection or write-off route NOT FOUND IN DOCUMENT). 🟡
- Year-end receivable days on revenue (derived, 365-day): FY26 28,005.24 / 50,308.34 x 365 = 203.2; FY25 15,430.58 / 37,019.70 x 365 = 152.1; FY24 11,438.57 / 30,717.18 x 365 = 135.9. Trend: DETERIORATING (three straight years; +51 days in FY26). 🔴
- Company's own ratio: Trade Receivables Turnover 2.32 (FY25 2.76), -15.94%, "affected due to increase in receivable in comparison to turnover" (Note 39 p.236). Based on average receivables 21,717.91. Management labels the cause but gives no collection plan.
- Receivables +81.5% (28,005.24 vs 15,430.58) against revenue +35.9%.
- Single customer above 10%: customer-level concentration NOT FOUND IN DOCUMENT. No major-customer disclosure (single segment). 🟡
- Related-party receivables: consolidated none disclosed except via copy of standalone note (116.73 from subsidiary). STANDALONE ONLY: standalone total 28,121.97; ">3 years" 591.28 (consolidated 474.55); the 116.73 difference equals the subsidiary debtor, which has been outstanding more than 3 years (FY25 standalone >3y 790.60 vs consolidated 646.94; 2-3y 533.26 vs 517.50; difference 143.66 + 15.76 = 159.42 = subsidiary debtors). The subsidiary has negative net assets (Section 6). No provision held. (Note 10(a) p.141; Note 10(b) p.141; Note 40 p.239) 🔴
- Foreign currency component: unhedged USD receivables 164.28 lakh USD = 15,550.18 (₹ lakhs); EUR 0.05 = 5.45; AED 1.69 = 43.42 (Note 37 p.229). Total 15,599.05 = 55.7% of receivables (derived). Implied USD rate 15,550.18 / 164.28 = 94.66. Country split (Middle East) NOT FOUND IN DOCUMENT. The brief's "Rs 60-70 Cr Middle East debtors" cannot be verified in the notes. 🟡
- CFO link (load-bearing): increase in trade receivables of 12,574.66 (CFS p.190) is 7.6x consolidated CFO of 1,658.62. See Section 12 for the CFO vs PAT bridge.
- ECL adequacy: no ECL policy, matrix or provision on a 28,005.24 book (Note 9 p.211-212; Note 2.2(p) p.202-203). With 3,030.29 over six months and zero credit-impaired balances, the "Unsecured, considered good" classification of 100% is a judgement the notes do not support with a disclosed loss-rate study. 🔴

---

## 5. INVENTORY (Note 8, p.211; ₹ lakhs)

| Category | FY26 | FY25 | Change |
|---|---|---|---|
| Raw material | 4,799.12 | 5,239.29 | -8.4% |
| Finished goods | 932.31 | 968.88 | -3.8% |
| Packing material | 1,836.41 | 1,894.64 | -3.1% |
| Work-in-progress | 226.77 | 217.97 | +4.0% |
| Consumable stores and spares | 30.61 | 25.79 | +18.7% |
| Stock written off | nil | nil | |
| TOTAL | 7,825.23 | 8,346.57 | -6.2% |

- FY24 total 7,838.73 (AR FY25 consolidated BS line 10007). Finished goods fell 3.8% while revenue grew 35.9%. 🟢
- Year-end inventory days on revenue (derived): FY26 56.8; FY25 82.3; FY24 93.1. Improving. Company ratio: Inventory Turnover 2.98 vs 2.04 (+45.7%), computed on cost of materials consumed 24,081.02 over average inventory 8,085.90 (Note 39 p.235-236). 🟢
- Write-downs and obsolete stock: nil, "Stock Written off during the period" blank both years; no NRV provision amount disclosed. Finished goods of 932.31 are 1.85% of revenue (derived), about 6.8 days of revenue. 🟢
- Cross-check: Note 29 change in inventories (FG+WIP) 27.77 (FY25 117.24) ties to Note 8 movements (FG -36.57, WIP +8.80, net -27.77). 🟢
- Interpretation caution: the inventory cut from 8,346.57 to 7,825.23 contributed +521.34 to CFO (CFS p.190), so the weak CFO was not driven by stock.

---

## 6. INVESTMENTS, SUBSIDIARY AND LOANS

- Consolidated investments: nil (BS p.184; Note 7 "Other Non Current Investments" nil p.211). Standalone investment in the subsidiary 354.78 at cost, unchanged (standalone BS p.113; Note 40 p.239). No impairment recorded. 🟡
- Subsidiary: Kwality Pharmaceuticals Africa Limitada, Maputo; KPL 51%, Mr Rajendra Singh Golan 49% (Note 14(a) p.215). Intended for import, export and marketing of company products (Note 1 p.194).
- AOC-1 (amounts in Rs, converted here to lakhs, derived): share capital 88.68; reserves and surplus (345.35) negative; total assets 126.36; total outside liabilities 383.04; turnover 29.12; PBT/PAT (0.06) loss; 1 MZN = 1.47 INR (p.241). Net worth = 88.68 - 345.35 = (256.68), i.e. liabilities exceed assets by 256.68 (derived). Auditor: PY loss 8.71; total assets 169.34 -> 126.36; net cash outflow 41.37 (p.178). The subsidiary is loss-making with negative net worth; no going-concern, support or letter-of-comfort statement for it in the notes (NOT FOUND IN DOCUMENT). 🟡
- Non-controlling interest is NEGATIVE: (167.47) at 31 Mar 2026, (165.24) FY25 (BS p.185). 49% of subsidiary net deficit (256.68) would be 125.77 (derived); the reported (167.47) differs by 41.70, probably translation or pre-consolidation effects; reconciliation NOT FOUND IN DOCUMENT. Note 15 (p.216) adds NCI of 167.67 into retained earnings (31,030.66 + 167.67 = 31,198.33), which differs from the BS NCI of 167.47 by 0.20. 🟡 (minor)
- Revenue test: consolidated Note 25 shows "Sale at Mozambique Subsidiary" 2.44 (p.222) = AOC turnover 29.12 less intra-group 26.68 (derived). Immaterial.
- ICDs, loans given, corporate guarantees: none (Note 7 loans nil p.210-211; CARO (iii) p.105). Unrealised gains/losses on investments: none.
- Interest on FDR: 12.54 (FY25 16.17) on bank FDs of 285.59 (Note 11 p.213; Note 26 p.222). FDs are margin money lien status NOT FOUND IN DOCUMENT (policy mentions "FDR margin" in borrowing security, p.219).

---

## 7. BORROWINGS (Notes 16 and 19 consolidated p.217-219; terms from standalone Note 17 p.146-149)

| Instrument (₹ lakhs) | Amount | Terms disclosed |
|---|---|---|
| Term loans (banks), total 31 Mar 2026 | 4,499.89 (FY25 2,911.28) | Secured; ties to Note 17 list of 20 loans (sum of listed outstanding = 4,499.81, derived) |
| of which current maturities | 1,559.87 (FY25 1,399.39) | Shown in short-term borrowings |
| of which non-current | 2,940.02 (FY25 1,511.89) | |
| HDFC BBG-WC term loan 1 | outstanding 529.52 | 32 instalments of 79.17 from Feb 2024; financed 2,245.00 |
| HDFC BBG-WC term loan 2 | outstanding 1,112.71 | No schedule disclosed |
| HDFC term loan A/C 802210241 | outstanding 2,141.51 | No schedule disclosed (largest single loan) |
| GECL extension | 119.53 | 61 instalments of 8.68 from sanction May 2022 |
| Vehicle loans (HDFC/ICICI): 2 Mercedes cars 92.97 and 122.75, BMW 35.86, Range Rover 228.71, Mercedes 5.82, others ~ 87 | about 486.11 on five luxury cars (derived: 35.86+5.82+92.97+228.71+122.75) | EMIs 2.37 to 5.08 a month each |
| Working capital limits (EPC ICICI 1,256.72 of 1,500.00; CC HDFC 5,331.30 of 7,185.00; CC Axis 1,958.12 of 4,000.00) | 8,546.14 utilised (Note 19: 8,546.17) of 12,685.00 sanctioned = 67.4% (derived); undrawn 4,138.86 | |
| TOTAL borrowings | 13,046.06 (FY25 11,244.53) | Debt/equity 0.40 (Note 39 p.235) |

- Interest rates, floating/fixed split, maturity profile beyond current maturities, covenants, covenant breaches or waivers: NOT FOUND IN DOCUMENT. The 5-year repayment schedule: NOT FOUND IN DOCUMENT (only current maturities 1,559.87).
- Related party borrowings: nil.
- Security: stock, book debts, plant and machinery, FDR margin hypothecated; equitable mortgage on six properties, including promoter-owned industrial (Nag Kalan) and residential (House 32) properties, Company-owned Wakia property, Kangra leased plot, and Hadbast 334 and Bal Kalan properties (Note 17 p.148-149; standalone). 🟡
- Implied interest rate on average debt (derived): 1,097.04 / ((13,046.06+11,244.53)/2 = 12,145.30) = 9.03%. Finance cost 1,097.04 (Note 31 p.224) includes MSME interest 10.60 and lease interest 2.11.
- DSCR 3.98 (FY25 2.92) per Note 39 p.236, management-computed.
- Working-capital debt barely rose (8,546.17 vs 8,333.24, +2.6%) while receivables rose 12,574.66. The gap was funded by payables (Section 8) and term debt (proceeds 3,169.31 gross; repayments 1,368.31, CFS p.191).
- Borrower classification point: all bank debt is mapped to "current" for WC, and term debt current maturities is shown inside short-term borrowings. 🟢
- Vehicles: five luxury vehicles financed in FY23-FY26 with outstanding 486.11; user and ownership of the vehicles NOT FOUND IN DOCUMENT; vehicles gross block 1,635.46 (Note 3 p.206). Flagged as a perquisite-type question for management. 🟡

---

## 8. TRADE PAYABLES (Note 20 p.219-220; ₹ lakhs)

| | FY26 | FY25 | FY24 |
|---|---|---|---|
| MSME | 1,916.25 | 2,117.99 | 2,121.55 |
| Others | 8,252.41 | 3,461.35 | 2,310.17 |
| TOTAL | 10,168.66 | 5,579.34 | 4,431.72 |

(FY24 from AR FY25 Note 19/20 lines 10057-10060, 11902-11910.)
- Total payables +82.3%; "Others" +138.4%.
- Ageing FY26: under 1 year 10,094.83; 1-2y 20.97; 2-3y 44.89; over 3y 7.97. All MSME payables are in the "less than 1 year" column (1,916.25). Ageing is from due date, so how much is past the 45-day MSME limit is NOT FOUND IN DOCUMENT. No disputed dues. (Note 20, p.220)
- MSME interest: accrued and unpaid 11.02 (FY25 0.42); interest charged in finance cost 10.60 (Note 31 p.224; Note 22 p.221; Note 36 p.227-228). Note 36 shows "Interest due on above" and "interest due and payable for the period of delay" as nil, while the next line shows 11.02 accrued; the two do not agree on their face. Section 43B(h) DTA of 31.21 booked for MSME dues (Note 6 p.210). 🟡
- Payable days on purchases (derived): purchases = raw material 15,741.57 + packing 7,841.05 + stock-in-trade 1,734.63 = 25,317.25 (ties to Note 39 numerator, p.236). FY26: 10,168.66 / 25,317.25 x 365 = 146.6 days. FY25: 5,579.34 / 18,755.87 (10,287.79 + 6,877.92 + 1,590.16) x 365 = 108.6 days. FY24: purchases not in this AR, NOT COMPUTED. Company ratio: Trade Payables Turnover 3.22 vs 3.75 (-14.19%) (p.236).
- Payables financed the receivable build. Without the 4,589.31 payable increase, CFO would have been -2,930.69 (derived: 1,658.62 - 4,589.31). 🟡

---

## 9. PROVISIONS AND EMPLOYEE BENEFITS (Notes 17, 23, 38; consolidated p.218, 221, 230-235; ₹ lakhs)

- Provisions are gratuity only: non-current 118.32 (FY25 25.17); current 39.30 (16.49); total 157.62 (41.66). No warranty, decommissioning, onerous-contract or litigation provisions. (Note 17 p.218; Note 23 p.221)
- Gratuity: DBO 283.52 (FY25 159.11, +78.2%); plan assets 125.90 (117.45); net liability 157.62 (41.66). Funded ratio 44.4% (derived). The note labels the DBO "Unfunded" in one line while describing an LIC-administered trust. (Note 38 p.231)
- DBO movement: opening 159.11 + service cost 41.94 + interest 13.20 + past service cost 82.94 - actuarial gain 13.67 = 283.52 (ties). Benefits paid: nil in both years. Employer contribution only 0.50 (FY25 20.29). (p.232-233) 🟡
- P&L charge 130.13 = service 41.94 + net interest 5.24 + past service 82.94. Of this 82.94 is in the exceptional line (Note 33), the rest in employee cost (Note 30 p.224).
- Actuarial assumptions: only demographic items disclosed (withdrawal 20% for service up to 3 years, 10% thereafter; IALM 2012-14; retirement age 60). Discount rate and salary escalation rate: NOT FOUND IN DOCUMENT. Sensitivity (+/-100bp): discount rate +100bp -15.91, -100bp +17.88; salary +100bp +19.65, -100bp -17.76 (p.234). That is -5.6% and +6.3% of DBO. (Note 38 p.234-235) 🟡
- Plan asset mix: 100% insurer-managed funds (p.235).
- Defined contribution: PF 139.58 (95.30); ESI 32.92 (26.66) (Note 38 p.230). Note 30 shows "Contributions to provident and other funds" 172.50 which includes more than PF + ESI (139.58+32.92 = 172.50 ties). 🟢
- Leave encashment: referenced in judgements but no liability disclosed. NOT FOUND IN DOCUMENT. 🟡
- Labour Code: the 82.94 is called an "incremental impact ... using the best information currently available", with Central and State rules still being finalised, so more cost is possible. (Note 2.2(m) p.201) 🟡
- Litigation provisions: none.

---

## 10. DEFERRED TAX AND TAX (Note 6 p.210; P&L p.188; CFS p.191)

- DTA 250.18 (FY25 161.48) = opening 161.48 + current-year fixed-asset difference 57.49 + MSME s.43B(h) 31.21 (ties). P&L deferred tax credit 88.70 (= 57.49+31.21) (FY25 credit 158.94). The note header says "Tax effect of items constituting deferred tax liability" but the result is an asset.
- Tax expense FY26: current 2,280.03 + deferred (88.70) + earlier years 23.29 = 2,214.62; effective rate 24.7% on PBT 8,949.21 (derived). FY25: 1,469.47 - 158.94 + 123.19 = 1,433.72; 26.5% (derived). FY24 PBT 3,109.89, PAT 2,361.59: 24.1%.
- Statutory-to-effective rate reconciliation: NOT FOUND IN DOCUMENT. Statutory rate applied: NOT FOUND IN DOCUMENT.
- Tax payable 819.73 (593.08) net of advance tax (Note 24 p.221). Tax paid per CFS 2,076.67 vs current tax 2,280.03: gap 203.36; plus 23.29 prior-year = 226.65 = movement in current tax liability (ties).
- MAT credit: nil (P&L line "MAT credit" 0.00). Unrecognised DTA: none disclosed. DTA realism: arises from timing items only; no carry-forward loss DTA. 🟢
- Prior-year tax 123.19 in FY25 vs 23.29 in FY26. 🟢

---

## 11. REVENUE DETAILS (Note 25 p.222)

| ₹ lakhs | FY26 | FY25 | Growth | Share FY26 / FY25 |
|---|---|---|---|---|
| Export turnover | 24,979.72 | 19,543.82 | +27.8% | 49.7% / 52.8% |
| Domestic turnover | 25,326.18 | 17,475.88 | +44.9% | 50.3% / 47.2% |
| Sale at Mozambique subsidiary | 2.44 | nil | | |
| Total | 50,308.34 | 37,019.70 | +35.9% | |

- Product, therapy, geography (country), channel, own-registration versus partner-held registration split: NOT FOUND IN DOCUMENT. Load-bearing fact 4 (own-registration 28-32% EBITDA vs partner-held 24-26%) cannot be verified from the notes. Top customer revenue and customers above 10%: NOT FOUND IN DOCUMENT (single segment, no Ind AS 108 entity-wide disclosure). 🟡
- Contract assets: none disclosed. Contract liabilities: "Advances from Customers" 879.23 (497.03; +76.9%) (Note 22 p.221). Unsatisfied performance obligations: NOT FOUND IN DOCUMENT.
- Other income 285.86: duty drawback 202.10 (144.55), gain on sale of assets 71.22 (2.84), FDR interest 12.54 (16.17). The asset-sale gain is 24.9% of other income and 0.8% of PBT (derived). Duty drawback is 0.81% of export turnover (derived). (Note 26 p.222)
- Revenue is net of returns, which include the related-party return of 262.75 from Kaler (Section 2). Sales-return amounts total: NOT FOUND IN DOCUMENT.
- Standalone revenue 50,305.89 (consolidated 50,308.34); the 2.44 difference is the subsidiary's external sale (P&L p.116 standalone).

---

## 12. OTHER CRITICAL NOTES

12.1 CASH FLOW QUALITY, CFO vs PAT (load-bearing fact 3), consolidated, ₹ lakhs (CFS p.190-192):
- PBT 8,949.21 + depreciation 1,981.04 + other non-cash 132.23 + finance cost 1,097.04 - gain on asset sale 71.22 - interest 12.54 = operating profit before WC changes 12,075.77. Working capital change -8,340.48 (receivables -12,574.66; inventories +521.34; payables +4,589.31; other items). Cash from operations 3,735.30; tax paid 2,076.67; CFO 1,658.62.
- CFO / PAT: FY26 24.6%; FY25 132.4% (5,271.78 / 3,980.27); FY24 182.0% (4,298.28 / 2,361.59) (derived). Three-year cumulative CFO 11,228.68 vs PAT 13,076.46 = 85.9% (derived). FY26 is the break. Standalone CFO 1,699.99 (standalone CFS p.120). The brief's CFO "Rs 17 Cr" matches standalone 16.99 Cr and consolidated 16.59 Cr; vs PAT 67 Cr. Confirmed. 🔴
- Investing: purchase of PPE 4,460.15 and intangibles 433.89 = 4,894.04 (FY25 2,500.27). Free cash flow (CFO - capex), derived: -3,235.42 (FY25 +2,771.51). Financing +703.96 (net borrowing 3,169.31 - 1,368.31 = +1,801.00, interest -1,097.04). Cash fell 1,202.02 -> 73.64.
- Other non-cash items 132.23 are unexplained in the notes (composition NOT FOUND IN DOCUMENT). 🟡
- Labels in the CFS are swapped: "Decrease/(Increase) in Other Current Assets" shows +397.36 and "Other Financial Assets, Current" shows -1,650.34, but the BS shows other current assets up 1,650.34 and other financial assets down 397.36. Net effect nil; presentation error. 🟡
- Investing section includes "Increase in other long-term liability" +592.81, which is the "Capital Advances" liability of 594.50 in Note 18 (p.218): an advance RECEIVED against a capital item, nature unexplained. Same line "Proceeds from disposal of PPE" 324.20 (Note 3: property disposed at book 252.98 gives gain 71.22). Whether the 594.50 relates to a further property sale: NOT FOUND IN DOCUMENT. 🟡
- Cash and cash equivalents FY25 1,202.02 included "Cheque in hand" 1,050.00 (87% of the balance) (Note 10 p.213). FY26 cash is 73.64 including 46.97 in hand. 🟡

12.2 Exceptional item (Note 33, p.226; Note 2.2(m), p.201): 82.94 past service cost, first occurrence (FY25 nil). CONFLICT: Note 2.2(m) attributes it to the four Labour Codes notified 21 November 2025 ("change in wage definition"); the footnote under Note 30 (p.224) says the "Additional labour dues (Past Service Cost) ... aris[e] pursuant to a court order". Two explanations for one number. 🟡 Recurrence: Labour Code rules not final, so more charges are possible.

12.3 Capital items: PPE gross 25,520.70, additions 2,788.09, disposal 252.98; net PPE 14,972.59 (14,398.45). CWIP 1,700.62 (nil FY25), all added in FY26; CWIP ageing and completion schedule NOT FOUND IN DOCUMENT. Capital advances 1,012.78 (1,152.96). Row "Property" (no depreciation) 1,875.00 -> additions 362.52, disposal 252.98 -> 1,984.54 net, 13.3% of net PPE (derived); nature of this row NOT FOUND IN DOCUMENT (zero depreciation is consistent with the freehold land policy). Depreciation 1,960.97 on PPE + 20.06 intangibles = 1,981.04 ties to P&L. Building revaluation reserve 80.00 unchanged (auditor says no revaluation this year, CARO (i)(d) p.104). (Notes 3-5, p.206-209)
- Capex ramp fits the Board's capacity story, but the capex cash (4,894.04) is 2.0x FY25 and 2.9x CFO (derived). 🟡
- Capital commitments disclosure: NOT FOUND IN DOCUMENT.

12.4 Other expense movements worth attention (Note 32 p.225; ₹ lakhs): commission 363.97 (157.25; +131.5%); advertising 324.52 (168.10; +93.1%); travelling 173.79 (57.27; +203.5%); administrative 376.32 (240.29; +56.6%); testing and laboratory 132.97 (273.91; -51.5%); distribution 1,415.15 (1,496.78; -5.5% while revenue +35.9%); CSR 74.30 (152.03); power and fuel 2,669.12 (2,337.31; +14.2%); repairs 755.23 (572.54; +31.9%). No bad-debt or ECL line exists. Distribution cost falling 5.5% while volume rises needs a reason (NOT FOUND IN DOCUMENT). 🟡

12.5 CSR (standalone Note 42(g) p.172-173): required 74.30 (FY25 145.94); spent 15.75 on asset construction + 58.55 other = 74.30; no shortfall. Also used 30.93 from unspent CSR account of FY24. Audit CARO (xx) no unspent amount (p.109). Note 22 shows unspent CSR nil (30.93). 🟢

12.6 EPS, share capital, dilution (Notes 14, 35; p.214-216, 227): 10,376,198 shares of ₹10; no issue in FY26 or FY25; basic = diluted EPS 64.90 (FY25 38.36; standalone 38.44). No ESOP, convertibles or warrants. Holdings above 5%: Ramesh Kumar 26.03% (26.01%); Ajay Kumar Arora 13.60% (13.59%); Aditya Arora 11.96% (11.95%); Deepak Bansal 9.24% (10.63%), down 144,428 shares (derived: 1,103,174 - 958,746); relationship of Deepak Bansal to promoters NOT FOUND IN DOCUMENT. Total 60.83% (62.19%). Promoter pledge: NOT FOUND IN DOCUMENT. 🟢

12.7 Financial risk and fair value: credit risk is dismissed by cross-reference ("It is evident from Note No. 9 ... that company is managing its credit risk efficiently", p.228) while the ageing schedule is the only evidence. Liquidity risk: pointed to the current ratio 1.80 (1.67) (p.228, 235). No maturity table, no interest-rate sensitivity, no FX sensitivity (a 1% INR move on 15,599 unhedged net exposure is about 156, derived). Fair value hierarchy: policy text only (Levels 1-3), no instruments disclosed. No derivatives or hedging (auditor, CARO/Rule 11(b) p.102). 🟡

12.8 Ratios note (Note 39 p.235-237): ROE 20.41% (15.17%); ROCE 21.94% (17.15%); "Return on Investment" shows identical numbers to ROCE (10,046.25 / 45,787.97); net profit ratio 13.39% (10.75%); current ratio 1.80; working capital turnover 2.79 (3.24). The identical ROCE and ROI rows suggest a copy-paste. 🟡

12.9 Events after balance sheet date: no Ind AS 10 note in the notes (NOT FOUND IN DOCUMENT). The Board's report says no material changes or commitments affecting financial position (Board report item 32, outside the notes). Going concern: Directors prepared accounts on a going-concern basis; auditor CARO (xix) finds "no material uncertainty" (p.108-109). No going-concern doubt in the notes. 🟢

12.10 Direct reserve entries bypassing P&L: (a) FY26 lease prior-period adjustment +4.47 (SOCE p.193; Note 15 p.216); (b) FY25 "Reclassification adjustment" +1.94 to retained earnings (standalone SOCE p.122; Note 15 p.216); (c) OCI remeasurement +13.67 (FY25 -0.97). Immaterial in size. 🟢

---

## 13. STANDALONE-ONLY DIFFERENCES (₹ lakhs)

| Item | Standalone | Consolidated | Source |
|---|---|---|---|
| Revenue | 50,305.89 | 50,308.34 | P&L p.116; p.187 |
| PAT | 6,734.66 (FY25 3,988.97) | 6,734.60 (3,980.27) | p.117; p.188 |
| Trade receivables | 28,121.97 (15,590.00) | 28,005.24 (15,430.58) | p.113; Note 10 p.140 |
| >3 year receivables | 591.28 (790.60) | 474.55 (646.94) | p.141 / p.212 |
| Investment in subsidiary | 354.78 | nil (eliminated) | p.113 |
| PPE net | 14,851.59 | 14,972.59 | p.113; p.184 (Mozambique 121.00) |
| Cash | 68.28 (1,155.29) | 73.64 (1,202.02) | p.113 |
| CFO | 1,699.99 (5,277.37) | 1,658.62 (5,271.78) | p.120; p.191 |
| Net worth | 33,337.24 (26,584.44) | 32,992.09 (26,239.59) | p.114; p.185 |
| Total assets | 59,566.06 | 59,220.91 | p.114; p.185 |
| CSR table, borrowing terms (20 loans), property list | present | absent in the consolidated set | p.147-149, 172 |

Borrowing terms, collateral and CSR detail exist only in the standalone notes. No other material difference.

---

## EXPECTED DISCLOSURES NOT FOUND IN THE DOCUMENT
Customer concentration; country or product split; own versus partner-registration revenue; ECL model or any loss rate; collection or write-off route for about 600 of receivables over two years in FY25; interest rates and covenants on all debt; borrowing maturity beyond one year; gratuity discount and salary-escalation rates; leave-encashment liability; tax reconciliation; lease discount rate; CWIP ageing; capital commitments; Ind AS 10 events note; nature of "Property" row, 594.50 capital-advance liability and 132.23 other non-cash items; ownership of Iair Infocom and Kaler Biopharmachem; reason for Kaler sale return; loans to the subsidiary; subsidiary going-concern support; FX sensitivity.

---

## PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Cash conversion break. CFO 1,658.62 vs PAT 6,734.60 (24.6%); receivables +12,574.66 (+81.5%) against revenue +35.9%; year-end receivable days 135.9 -> 152.1 -> 203.2 (derived); FCF -3,235.42 after 4,894.04 capex. Three-year CFO/PAT 85.9%. | CFS p.190-191; Note 9 p.211; Note 39 p.236 | 🔴 |
| 2 | No ECL or doubtful-debt provision on 28,005.24 of receivables; 3,030.29 over six months (10.8%), 564.29 over two years; "objective evidence" impairment wording; standalone also carries 116.73 owed by the loss-making, negative-net-worth subsidiary for over three years with no provision. | Note 9(a) p.212; Note 2.2(p) p.202; standalone Note 10(a) p.141 | 🔴 |
| 3 | Unhedged FX receivables 15,599.05 = 55.7% of receivables (USD 164.28 lakh = 15,550.18); no sensitivity or country split; Middle East exposure in the brief not verifiable here. | Note 37 p.229 | 🟡 |
| 4 | GST contingencies 3,697.75 (11.2% of net worth, 54.9% of PAT), no provision; the 630.06 IGST-refund order already lost at Commissioner (Appeals), writ pending; 3,026.07 SCN stayed by High Court. Related IGST receivable 852.37 and revenue-authority balances 1,785.21 on the balance sheet. Auditor also notes delays in GST/TDS deposits (CARO (vii)(a)). | Note 34 p.226-227; Note 12-13 p.213-214; CARO p.105 | 🟡 |
| 5 | Payables stretched: 5,579.34 -> 10,168.66 (+82.3%); payable days on purchases 108.6 -> 146.6 (derived); MSME interest accrued 11.02 (from 0.42); without payables CFO would be -2,930.69. | Note 20 p.219-220; Note 36 p.227 | 🟡 |
| 6 | Liquidity thin: cash 73.64 (FY25 1,202.02, of which 1,050.00 was a cheque in hand); gross debt 13,046.06; net debt 12,686.83 (derived); WC lines 67.4% drawn; term debt up to 4,499.89; rates and covenants not disclosed. | Note 10 p.213; Notes 16, 19 p.217-219; standalone Note 17 p.147-148 | 🟡 |
| 7 | New related parties with unexplained flows: Kaler Biopharmachem sale 121.48 vs return 262.75 (net -141.27); Iair Infocom 20.25 + 6.40; both nil in FY25; ownership not disclosed. Promoter-owned factory leased at 2.16 a year rent; promoter properties pledged as bank collateral. | Note 40 p.238-239; CARO (i)(c) p.104; standalone Note 17 p.149 | 🟡 |
| 8 | Capex ramp with unexplained items: PPE+intangible cash capex 4,894.04 (2.0x FY25); CWIP 1,700.62; capital advances 1,012.78; capital-advance liability 594.50 received; capitalised bioequivalence study 433.89; asset-sale gain 71.22 (24.9% of other income). | Notes 3-5 p.206-209; Note 18 p.218; CFS p.191 | 🟡 |
| 9 | Disclosure and consistency defects: exceptional item cause given two ways (Labour Code vs court order); unfilled template text in Note 6; CFS asset labels swapped; consolidated RPT note not eliminated; ROCE equals "ROI" in Note 39; tax reconciliation, discount rate, covenants absent; Ind AS 116 recognised through opening reserves with FY25 not restated. | Note 2.2(m) p.201; Note 30 p.224; Note 6 p.210; CFS p.190-191; Note 39 p.237 | 🟡 |
| 10 | Subsidiary: unaudited by group auditor, net liabilities 256.68, negative NCI (167.47), no support statement; standalone investment 354.78 not impaired. Gratuity DBO +78% to 283.52 on a first-time 82.94 past service cost with more Labour Code cost possible. | AOC-1 p.241; auditor Other Matters p.178; Note 38 p.231 | 🟡 |

Clean points worth recording: inventory down 6.2% with revenue up 35.9% (inventory days 93.1 -> 82.3 -> 56.8); no covenant breach or default stated by auditor (CARO (ix)(a) p.107); no dividend, no ESOP, no share issue; related party pay at 3.4% of PBT and tied to Note 30; CSR fully spent; auditor opinions unmodified.

(Pass 1 emits no final B02 block. Sibling file B02-notes-pass1.yaml is a pass marker only.)

```yaml
stage: B02-notes-pass1
company: "KPL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
pass: 1
input_gaps: []
report_path: runs/kpl-2026-11-15/outputs/reports/02-notes-pass1.md
unit: "INR lakhs (AR face); derived percentages and ratios unit-free"
headline_findings:
  - "CFO 1,658.62 vs PAT 6,734.60 (24.6%); receivable days 135.9 -> 152.1 -> 203.2 (derived); Note 9, p.211; CFS p.190"
  - "Zero ECL/doubtful provision on 28,005.24 receivables; 3,030.29 over 6 months; Note 9(a), p.212"
  - "Contingent liabilities 3,697.75 = 11.2% of net worth, no provision; Note 34, p.226-227"
receivables_trend_preliminary: "deteriorating (over 6m share 28.0% -> 18.7% -> 10.8%, but total receivables +81.5% vs revenue +35.9%, days 203.2)"
going_concern_language_preliminary: "NONE in notes; CARO (xix) finds no material uncertainty (p.108-109)"
```
