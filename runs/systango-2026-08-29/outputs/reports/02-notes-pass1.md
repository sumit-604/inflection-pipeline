# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 1 OF 3 (FULL EXTRACTION)
Company: SYSTANGO (Systango Technologies Limited) | Run date: 2026-08-29 | Model: claude-sonnet-5

---

## CRITICAL ANCHOR ISSUE — READ FIRST

The file supplied as `inputs/annual-report/Annual_Report_2023.pdf` (121 pages) is labelled
"FY2023 Annual Report" in the task brief, but its actual content is Systango Technologies
Limited's **21st Annual Report, for FY2024-25 (year ended 31 March 2025)** — AGM notice,
Board's Report, and financial statements for FY25 with FY24 comparatives. There is **no
FY2023 annual report anywhere in this document**. Every figure below is FY25 (current, year
ended 31-Mar-2025) vs FY24 (prior, year ended 31-Mar-2024), taken from this single document.
This is a corpus identity/freshness gap, not a company finding — but it means every
downstream stage referencing "the FY2023 AR" is actually referencing FY2024-25 data. Flagged
as **CORPUS-MISLABELLED**.

The Annual Report contains TWO complete note sets: **Standalone** (parent company only,
Notes 1–22, pages 76–94 printed / "21st ANNUAL REPORT" footer) and **Consolidated** (Group,
Notes 1–22, pages 108–118 printed). Both were read; findings below are tagged [STANDALONE] or
[CONSOLIDATED] where the two diverge, or [BOTH] where materially identical.

Company: Systango Technologies Limited, CIN L51109MP2004PLC016959, incorporated 2004
(originally "Bushcare Overseas Pvt Ltd"), converted to public company Dec-2022, IPO'd and
listed on NSE Emerge Platform 15-Mar-2023 at ₹90/share premium (₹10 FV + ₹80 premium),
38,68,800 shares, ₹34.82 Cr raised. Registered office Indore. Principal business: "supplying
Software and Development Services" (Note 21A, p.85). Auditor: Anil Kamal Garg & Company,
Chartered Accountants (ICAI FRN 004186C), partner Aayush Garg — unqualified opinion, both
standalone and consolidated, dated 26-May-2025.

All amounts ₹ Lakhs unless stated. Rating key: 🟢 Clean | 🟡 Watch | 🔴 Red Flag.

---

## SPEAR PRIORITY ITEMS — RESOLVED

### [1] Loans/advances to unnamed "Others" — CONFIRMED, RED FLAG
**Note 14 — Short-Term Loans and Advances [STANDALONE, p.83; CONSOLIDATED, p.114 — same
₹529.55L figure appears at parent level only]:**
"Other Loans and Advances" = ₹529.55L (FY25) vs ₹454.71L (FY24), classified "Unsecured,
considered good." Note 14.1 (Additional Regulatory Information required by Companies Act,
2013 re: Loans or Advances) shows **100% of this balance sits under "Others"** — explicitly
NOT Promoters (NIL), NOT Directors (NIL), NOT KMPs (NIL), NOT Related Parties (NIL).
Verbatim note beneath the table: *"The loans and advances have been granted without
stipulating any terms or period of repayment and the same are repayble [sic] on Demand along
with interest."*

Corroborated independently by the **standalone Auditor's Report CARO Annexure, clause (iii)
[p.66]**, which reproduces the same ₹529.55L balance and states the terms "are, prima facie,
not prejudicial to the interest of the company," while confirming no schedule of repayment
exists and interest is charged. 🔴 **RED FLAG**: an IT-services company carrying zero bank
debt and a ₹13+ Cr investment portfolio (see Investments below) is simultaneously running
₹5.3 Cr of unsecured, open-ended, interest-bearing loans to counterparties the company itself
declines to identify beyond "Others." Counterparty identity is not disclosed anywhere in the
119 pages read. This is a first-tier question for management.

### [3] Employee benefit accounting — CONFIRMED, RED FLAG, PAYMENT BASIS
**Note 21, Part 21B.7 "Retirement Benefits" [STANDALONE, p.86]** — verbatim:
*"Contributions to defined contribution schemes such as Provident Fund, ESIC and NPS are
charged to the Statement of Profit and Loss as incurred. However, for payment of Gratuity and
Leave Encashment no provision has been made by the company and the same are accounted for on
actual payments basis only."*

🔴 **RED FLAG**: Gratuity is a statutory defined-benefit obligation under the Payment of
Gratuity Act, 1972 for any establishment with 10+ employees (Systango's Salary & Allowances
line of ₹3,215–3,414L implies a headcount well above this threshold). AS-15 (Employee
Benefits) requires actuarial valuation and provisioning of the accrued defined-benefit
liability; Systango instead expenses gratuity/leave encashment only when actually paid out.
Consequences: (a) no gratuity/leave-encashment liability appears on the balance sheet at all
— NOT FOUND anywhere in the notes; (b) reported profit is systematically *higher* than under
accrual accounting in any year where the unprovided obligation is growing (rising headcount,
rising wages, rising tenure); (c) no actuarial assumptions (discount rate, salary escalation,
attrition, mortality) are disclosed — NOT FOUND, consistent with no valuation being performed.
Neither the standalone nor the consolidated auditor's report qualifies or draws attention to
this policy (Emphasis of Matter section: NIL disclosed) — worth noting as an audit-scope
question in its own right. This finding directly matches the SPEAR hypothesis: **profits are
overstated relative to what accrual-basis employee-benefit accounting would show.**

---

## SECTION-BY-SECTION EXTRACTION (Pass 1 categories 1–12)

### 1. Accounting Policies & Changes [STANDALONE Note 21A/21B, p.85–87]
- Note 21B.1 Accounting Convention (p.85): Indian GAAP (IGAAP) under Companies Act s.133/
  Companies (Accounts) Rules 2014; historical cost; going concern; mercantile/accrual system.
  🟢 Company reports under **IGAAP, not Ind AS**, despite listed status — no explicit note
  found explaining Ind AS non-applicability (likely SME-platform / net-worth threshold
  exemption). NOT FOUND: explicit Ind-AS-applicability statement. 🟡
- Note 21B.2 Use of Estimates (p.85): standard boilerplate. 🟢
- Note 21B.3 PPE & Intangibles (p.85): cost less depreciation/impairment; CWIP for assets not
  ready for use; intangibles at cost less amortisation/impairment. No capitalisation
  *threshold* (₹ minimum) disclosed — NOT FOUND.
- Note 21B.4 Investments (p.86): current at lower of cost/FV; non-current at cost less
  diminution provision. 🟢
- Note 21B.5 Taxes on Income (p.86): current tax per Income-Tax Act 1961; deferred tax on
  timing differences, DTA recognised only on virtual certainty; **SEZ deduction u/s 10AA**
  available (100% for 5 years, 50% for next 5) — company holds an SEZ unit; MAT applies during
  holiday period, MAT credit carried forward for post-holiday use. 🟢, tax-holiday-dependent
  profitability worth noting for downstream margin-sustainability analysis (holiday is
  time-bound).
- Note 21B.6 Depreciation (p.86): SLM per Schedule II useful lives; no asset-class useful-life
  table found in the pages read — NOT FOUND (rates/lives per category).
- Note 21B.7 Retirement Benefits (p.86): 🔴 see SPEAR section above — payment-basis gratuity/
  leave encashment, no actuarial provision.
- Note 21B.8 Revenue Recognition (p.86): AS-9, accrual, periodic per contract terms,
  uncertain items excluded, net of taxes/cess. 🟢 conventional.
- Note 21B.9 Provisions & Contingent Liabilities (p.86): standard AS-29 recognition criteria.
  🟢
- Note 21B.10 Impairment of Assets (p.86): standard. 🟢
- Note 21B.11 Cash Flow Statement (p.86): indirect method, AS-3. 🟢
- Note 21B.12 Foreign Currency (p.87): monetary items retranslated at closing rate; exchange
  differences to P&L except where capitalised to qualifying assets. 🟢
- Note 21B.13 Earnings Per Share (p.87): AS-20, basic = profit ÷ weighted avg shares. 🟢
- No first-time-adoption disclosures (not applicable — IGAAP, no standard transition this
  year). No Ind AS 116 lease/ROU/discount-rate disclosures — NOT APPLICABLE under IGAAP;
  however, **Note 7B.2 "Right to Use Holiday Home and Recreation Center"** (₹135.65L net,
  p.111 consolidated / equivalent standalone) is capitalised as an *intangible asset* under
  IGAAP even though it is functionally an operating lease right for staff welfare — an
  atypical capitalisation call. 🟡
- No impairment-test growth/discount-rate assumptions found — NOT APPLICABLE (no goodwill on
  either balance sheet).
- No formal ECL-matrix narrative found beyond mechanical ageing-based doubtful-debt
  provisioning (see Trade Receivables, below). NOT FOUND: qualitative ECL policy text.

### 2. Related Party Transactions [STANDALONE Note 21C.8, p.89–91]
**List of related parties:**
- Wholly owned subsidiaries: Isystango Ltd, UK; Systango Account Aggregator Services Pvt Ltd
  (**converted to Systango Account Aggregator Services LLP w.e.f. 10-04-2024**); Systango LLC,
  USA (**liquidated w.e.f. 19-12-2024**); Systango INC, USA.
- Subsidiary of subsidiary: Systango Ltd, UK.
- Related parties: Shri Nilesh Rathi HUF; M/s NV Agro (partnership firm); **DBX Holdings
  Ltd.**
- Directors: Vinita Rathi, Nilesh Rathi, Narender Tulsidas Kabra, Vikas Jain, Sarita Devi
  Khandelwal.

**Transactions (₹L, FY25 / FY24):**
| Item | FY25 | FY24 | YoY |
|---|---|---|---|
| Sales/services — Systango LLC USA | 160.88 | 1,803.13 | −91.1% |
| Sales/services — Isystango Ltd UK | 131.42 | 194.47 | −32.4% |
| Sales/services — Systango Ltd UK | 521.92 | 65.03 | +702.7% |
| Sales/services — DBX Holdings Ltd | – | 156.98 | −100% |
| Sales/services — Systango INC USA | 1,157.81 | – | new |
| **Total RPT sales** | **1,972.03** | **2,219.61** | −11.2% |
| Directors' remuneration (total) | 179.72 | 136.94 | +31.2% |
| Independent director sitting fees (total) | 0.80 | 2.20 | −63.6% |
| Rent — Nilesh Rathi HUF (office) | 17.25 | 19.50 | −11.5% |
| Rent — NV Agro (lease) | 1.00 | 1.00 | 0% |

RPT sales as % of standalone revenue: **32.2% (FY25)** vs **42.1% (FY24)** (Note 16 revenue
6,132.96 / 5,267.91). 🟡 **WATCH** — nearly a third of standalone topline is billed to the
company's own wholly-owned subsidiaries, and the *mix between billing entities swung sharply*
(LLC USA down 91%, Ltd UK up 703%, INC USA appearing from zero) in the same year the USA LLC
was liquidated. Worth a management question on why billing was re-routed between subsidiary
entities rather than remaining stable.

**Loan transactions:** Loans taken from Systango Account Aggregator Services Pvt Ltd —
opening 0.28, repaid 0.28, closing NIL (FY25); FY24 received 50.76, repaid 50.48, closing
0.28 — small, resolved. Loans/advances *given* to related parties: NIL both years, consistent
with Note 22(iii) ("no loans to promoters/directors/KMPs/related parties"). 🟢

**Outstanding balances at year-end:**
- Non-current investment in Systango Account Aggregator Services LLP: ₹32.64L (new, post
  LLP conversion).
- **Receivables from subsidiaries: Systango Ltd UK 121.81 + DBX Holdings 32.05 + Isystango UK
  110.74 + Systango INC USA 353.46 = ₹618.06L total (FY25)**, vs ₹324.62L (FY24: Systango LLC
  167.64 + DBX 156.98). This is **~38.7% of total standalone net trade receivables
  (₹1,598.47L)** owed by related parties. 🟡
- Payables to related parties: NV Agro 0.90/0.90; Narender Kabra 0.18/–; Vikas Jain 0.18/– —
  small, director sitting-fee payables.

**Non-arm's-length / opacity signal:** **DBX Holdings Ltd** is classified as a "Related
Party" (not a subsidiary) yet the company both (a) holds an *equity investment* in it
(₹166.11L unquoted equity, Note 8, new this year) and (b) trades with it (₹156.98L sales in
FY24, ₹32.05L receivable at FY25 year-end) — its exact control/influence relationship (why
not associate/JV-classified given equity + trading + related-party status) is not disclosed.
🟡 flag for management clarification.

New related party this year: Systango INC USA (₹1,157.81L sales + ₹353.46L receivable — a
sizeable new relationship appearing from zero).

### 3. Contingent Liabilities [STANDALONE Note 21C.4, p.88]
Claims against company: NIL. Guarantees: NIL. Other contingent liabilities: NIL. Capital
commitments: NIL. Uncalled liability on partly-paid investments: NIL. Other commitments: NIL.
**All items NIL, both FY25 and FY24.** 🟢 Clean, 0% of net worth (net worth ₹10,048.92L per
Note 22(b) standalone).

🔴 **DISCLOSURE GAP — CONSOLIDATED**: the Consolidated Balance Sheet/P&L cross-reference
"Note 22" for both "Significant Accounting Policies & Practices" and for EPS (P&L line XII,
"[Refer note 22]"). As printed, **Consolidated Note 22 is titled "Additional Regulatory
Information" only** (p.117–118) and contains title-deed/benami/wilful-defaulter/ratio
disclosures — it does **not** contain a contingent liabilities table, an RPT table, an
employee-benefit/gratuity policy note, a revenue-recognition policy, or an EPS working. None
of this content appears anywhere else in the consolidated note set (Notes 1–22 read in full,
p.108–118). This is a genuine disclosure inconsistency: a reader of the consolidated
financials alone cannot verify Group-level contingent liabilities or see the consolidated EPS
computation. 🔴

### 4. Trade Receivables [STANDALONE Note 12/12.1/12.2, p.82–83; CONSOLIDATED Note 12, p.113]
| | FY25 | FY24 | YoY |
|---|---|---|---|
| Unsecured, considered good | 1,546.57 | 836.03 | +85.0% |
| Doubtful | 97.54 | 112.72 | −13.5% |
| Less: provision for doubtful debts | (45.65) | (42.06) | +8.5% |
| **Net (standalone)** | **1,598.47** | **906.69** | **+76.3%** |
| Net (consolidated) | 1,546.66 | 1,074.24 | +44.0% |

Revenue grew only +16.4% (standalone) / +18.7% (consolidated) over the same period —
**receivables grew 4.6x faster than revenue on a standalone basis.** 🔴

Ageing (standalone, net, FY25): <6mo 1,463.41; 6mo–1yr 26.07; 1–2yr 108.99; nothing beyond
2 years. FY24: <6mo 836.03; 6mo–1yr 70.67; nothing beyond 1 year net. **The 1–2 year bucket
went from ₹0 to ₹108.99L** — genuine ageing deterioration, not just top-line-proportionate
growth. 🟡

**Note 22(f) Trade Receivable Turnover Ratio [standalone, p.93]**: fell from **7.81x (FY24)
to 4.90x (FY25), a −37.32% decline** — this exceeds the Annual Report's own >25%-variance
disclosure threshold, and management's own remark reads: *"Due to increase in Revenue from
Operations during the year, in comparison to preceding financial year and increase in Trade
receivables during the year."* Implied DSO: ~47 days (FY24) → ~75 days (FY25). 🔴

Single-customer concentration >10%: NOT FOUND (no customer-level disclosure located).
Receivables from related parties: ₹618.06L (~38.7% of standalone net receivables) — see
Related Party section. Bad debts written off: ₹18.50L (FY25) vs NIL (FY24) — first
write-off disclosed in the two years shown (Note 20C standalone / Note 21C consolidated).
Provision for doubtful debts *expensed* fell to ₹3.59L (FY25) from ₹28.33L (FY24) even as
gross receivables and the doubtful-debts stock both grew — a mild under-provisioning signal
worth watching. 🟡

**→ FLAG-CASH driver: receivables trend is DETERIORATING (standalone +76% vs revenue +16%;
turnover ratio −37%; new 1–2yr ageing bucket appearing).**

### 5. Inventory — NOT APPLICABLE
Software/IT-services business; Note 22(e) Inventory Turnover Ratio explicit "N.A." both
years; no inventory notes exist in either note set. 🟢 consistent with business model.

### 6. Investments [STANDALONE/CONSOLIDATED Note 8/8.1/11/11.1, p.79 & p.112–113]
Subsidiaries confirmed (see RPT section for list); % ownership figures not disclosed in the
pages read — NOT FOUND (holding percentages per subsidiary). Systango LLC USA liquidated
19-12-2024 mid-year — a structural wind-down of the US operating entity, worth a management
question on rationale.

**Non-current investments (consolidated) rose 11.4x: ₹115.91L (FY24) → ₹1,325.25L (FY25).**
Composition (FY25): quoted equity portfolio ₹502.02L across seven unrelated listed names
(Gujarat Narmada Valley Fertilizers, Mahindra Logistics, TCI Express, Mafatlal Industries,
Mahindra Holidays & Resorts, Reliance Chemotex, Advanced Enzyme Technologies — several new
positions opened in FY25); unquoted equity ₹201.99L (GreenLeaf TDG Ltd UK ₹35.88L, **DBX
Holding Ltd ₹166.11L, new**); fixed deposits >12mo maturity ₹621.25L (up from ₹20.29L). 🟡
**WATCH** — an operating software company is running a sizeable (~₹13.25 Cr non-current +
~₹46.5 Cr current-investment) treasury/equity portfolio funded from IPO proceeds and
operating cash surplus, rather than reinvesting in the core business or distributing to
shareholders. Worth probing treasury policy and risk appetite (return on investment ratio
disclosed at 15.46% FY25 vs 4.29% FY24 on the mutual-fund sleeve — Note 22(k) — driven by
"substantial increase in gain on investments," itself a volatility signal).

Current investments (standalone, Note 11): mutual funds ₹2,072.45L (FY25) / ₹2,620.10L
(FY24); FDs (3–12mo) ₹2,529.92L/₹2,742.10L; quoted equity NIL/₹30.78L. Aggregate impairment
in mutual fund holdings ₹2.55L (FY25) vs ₹0.12L (FY24). 🟢 immaterial impairment.

No ICDs or loans given to subsidiaries/third parties beyond the Note 14 "Others" balance
(loans given to related parties explicitly NIL both years, Note 21C.8.B.vii.b).

### 7. Borrowings [BOTH, Note 3, p.77 standalone / p.109 consolidated]
Standalone: "Loans and Advances from Related Parties — From Body Corporates" NIL (FY25) vs
₹0.28L (FY24). Consolidated: "From Directors" ₹3.10L (FY25) vs ₹9.22L (FY24) — informal
director advances at subsidiary level, no rate/tenure/security disclosed. 🟢 immaterial.

**Company carries no bank debt, no term loans, no working-capital facility anywhere in the
Group** — explicitly confirmed at Note 22(v) consolidated: "The Group Companies has not
availed any working capital facilities and accordingly, it is not required to furnish any
quarterly returns or statements with the banks or financial institutions." Debt-Equity ratio
effectively zero (standalone Note 22(b): Total Debts NIL, shown "N.A."). 🟢 Debt-free balance
sheet, clean.

### 8. Trade Payables [Note 4/4.1/4.2/4.3, p.78 standalone / p.110 consolidated]
**Standalone trade payables = ZERO (NIL) at both 31-Mar-2025 and 31-Mar-2024** — both MSME
and non-MSME categories, all ageing buckets NIL. 🔴 **RED FLAG / ANOMALY** — highly unusual
for an operating company with ₹61 Cr standalone revenue to show literally no trade payables
in either year end. Possible explanations: (a) genuinely near-100% advance/immediate vendor
settlement, or (b) vendor dues are being captured under "Other Current Liabilities → Creditors
for Expenses" (Note 5: ₹7.15L FY25 / ₹61.55L FY24) rather than labelled "Trade Payables" —
neither is confirmed by the notes. Direct management question warranted.

Consolidated trade payables are NOT nil: ₹39.56L (FY25) vs ₹13.93L (FY24), entirely
"Other than MSME," entirely <1 year — meaning payables exist only at subsidiary level. 🟡

No MSME interest/delay disclosures (Note 4.1: all items NIL) — consistent with, but not very
informative given, the near-zero payables base.

### 9. Provisions [Note 6, consolidated p.111 — standalone Note 6 not independently confirmed
in a rendered image; treated as a coverage gap below]
Consolidated Short-Term Provisions: For Taxation ₹521.42L (FY25)/₹373.20L (FY24); **For
Employee Benefits ₹255.14L (FY25)/₹258.67L (FY24)**; For Others ₹172.18L/₹64.66L. Total
₹948.74L/₹696.53L.

🔴 **INTERNAL INCONSISTENCY FLAG**: a "For Employee Benefits" provision of ₹255.14L exists on
the balance sheet even though Note 21B.7 states gratuity and leave encashment are **not**
provided (cash-payment basis only). The notes do not disaggregate what this ₹255.14L
provision actually represents (bonus? accrued current-period leave payable? statutory dues?).
Either the provision genuinely excludes gratuity/leave (in which case its composition should
be disclosed) or there is an inconsistency between the stated accounting policy and the
balance sheet — **cannot be resolved from the notes as disclosed; NOT FOUND: provision
breakdown.**

No warranty, decommissioning, onerous-contract, or litigation provisions found — consistent
with all-NIL contingent liabilities.

### 10. Deferred Tax [STANDALONE Note 21C.7, p.89; CONSOLIDATED Note 9, p.112]
Standalone: DTA (net) closing ₹5.55L (FY25) vs ₹18.18L opening, reversal of ₹12.64L during
the year; rate applied 29.120%. Composition: DTA on depreciation timing difference ₹4.50L +
other items (mainly doubtful-debt provision) ₹1.05L = ₹5.55L; no DTL recognised. Consolidated
mirrors this almost exactly (₹18.18 opening → ₹5.54 closing, −12.64 reversal) — subsidiaries
carry no material DTA of their own. 🟢 small, well-reconciled, no realism concerns given the
small absolute size.

No full effective-vs-statutory-rate reconciliation table found (only the DTA build-up shown)
— NOT FOUND. MAT credit entitlement/utilisation timeline: Tax Expense table shows a
"(Less): MAT Credit" line at NIL both years — no separate MAT credit asset balance disclosed
— NOT FOUND (entitlement balance). Unrecognised DTA and reasons: NOT FOUND (not disclosed;
none appears to exist given the small overall DTA).

### 11. Revenue Details [Note 16, p.83 standalone / p.115 consolidated]
Standalone: single line, "Software & Development Charges" ₹6,132.96L (FY25) vs ₹5,267.91L
(FY24), +16.4%. Consolidated: "Software, Website Development & Hosting Charges" ₹6,714.44L
vs ₹5,657.21L, +18.7% — consolidated exceeds standalone by ₹581.48L (FY25), implying ~8.7% of
Group revenue originates outside the Indian parent post-elimination.

No disaggregation by product/segment/geography, no customer-concentration disclosure, and no
formal AS-17 segment note located anywhere in the 22 notes read for either entity — NOT
FOUND. No contract-asset/liability (unbilled/deferred revenue) note found — NOT FOUND (also
not mandated under IGAAP/AS-9, unlike Ind AS 115).

**Note 21C.9.iii Earnings in Foreign Currency [standalone, p.92]**: "Royalty, Know how,
professional & consultation fees" ₹6,117.06L (FY25) vs ₹5,247.37L (FY24) — this is **~99.7%
of standalone revenue**, confirming the business is almost entirely export/foreign-currency
billed, but booked under a "royalty/consultation fees" head rather than "Export of goods"
(shown NIL). Likely just the fixed AS-format category label for a services exporter, not a
red flag in itself, but a notable classification choice. 🟢 informational.

### 12. Other Critical Notes
- **Exceptional/extraordinary items**: NIL both years (P&L lines VI, VIII). 🟢
- **Goodwill**: no goodwill line on either balance sheet — subsidiaries appear
  incorporated/organic, not acquired at premium. NOT FOUND (implies none).
- **Intangibles [Note 7B, p.111 consolidated]**: Software ₹11.84L net; "Right to Use Holiday
  Home and Recreation Center" ₹135.65L net (see Accounting Policies flag above — unusual
  capitalisation of a staff-welfare lease right as an intangible); **"Intelligent Document
  Processing Platform" ₹134.68L net**, a newly capitalised internally-developed software
  product (₹140.80L gross addition FY25, fully transferred from "Intangible Assets under
  Development" which itself shows ₹101.67L → ₹0 fully transferred, Note 7D). No explicit
  capitalisation criteria/threshold disclosed for internally generated software — NOT FOUND.
  🟡 Watch — capitalising internal product development rather than expensing it as R&D
  directly lifts reported profit; the criteria used should be probed.
- **Capital commitments**: NIL (Note 21C.4.B). 🟢
- **FX hedging**: "Foreign Currency Hedging Charges" expensed ₹9.70L (FY25)/₹13.81L (FY24)
  (Note 20A) confirms hedging activity exists, but no derivative/notional/MTM note found —
  NOT FOUND.
- **Segment reporting**: NOT FOUND (see Revenue Details).
- **EPS [Note 21C.13, standalone, p.87]**: Basic = Diluted (no dilutive instruments) — 15.82
  (FY25) vs 11.07 (FY24), +42.9% YoY. **Consolidated EPS working not located** (P&L
  cross-references Note 22, which does not contain it — see Contingent Liabilities /
  disclosure-gap flag above). 🔴
- **Events after balance sheet date**: NOT FOUND — no such note located in either note set.
- **CSR [Note 21C.6, standalone, p.88]**: required ₹29.29L (FY25)/₹19.92L (FY24); spent in
  full both years; brought-forward/carried-forward excess (₹0.04L) both years (immaterial);
  no shortfall; explicit statement "No CSR amount has been paid to any related party of the
  Company." 🟢 Clean, fully compliant.
- **ESOP dilution**: NOT FOUND — no ESOP/stock-option note located; EPS note shows "Add:
  Dilutive Potential Equity Shares" = NIL both years, consistent with no scheme outstanding.
- **Share capital changes**: none in FY25 (14,668,800 shares constant); historical bonus
  issues disclosed (2020 ×2, 2022); no issuance since the Mar-2023 IPO. 🟢
- **Direct debits/credits to reserves bypassing P&L**: ₹25.11L of IPO-related expenses were
  adjusted directly against Securities Premium in FY24 (none in FY25) — standard practice
  under Companies Act s.52 for share-issue costs, not a red flag, but noted per instruction.
  🟢
- **Restatements**: Note 21C.2 (standalone, generic): "Figures for the previous year has been
  regrouped and/or rearranged wherever considered necessary" — no specific line items or
  amounts quantified. NOT FOUND (specifics). 🟡 minor, boilerplate.
- **Going concern**: Note 21B.1.2 states statements are prepared "on the accounting principle
  of a going concern" — standard boilerplate assumption, **no substantive going-concern doubt
  language found anywhere.** NONE.
- **Audit trail (edit-log) non-compliance [Consolidated Auditor's Report Annexure,
  p.~102-103]**: auditors report that for the subsidiary companies, the accounting software
  used for FY25 books did not have the audit-trail (edit-log) feature mandated by the proviso
  to Rule 3(1), Companies (Accounts) Rules, 2014. 🔴 **RED FLAG** — statutory IT-controls
  non-compliance at subsidiary level; a governance finding directly relevant to accounting
  quality even though it sits in the auditor's report rather than a numbered note.
- **CARO clause (iii), standalone [p.66]**: independently corroborates the Note 14 loan
  figures (see SPEAR section). Other CARO clauses (iv–xxi) reviewed [p.67–69]: no fraud
  reported, no material uncertainty on going concern, statutory dues "generally regular"
  with minor delays noted in a few cases (not quantified), no wilful-defaulter declaration,
  clean overall. 🟢 for the rest of CARO.

---

## NOTE-BY-NOTE COVERAGE MAP (transparency on what was directly viewed)

**STANDALONE (Notes 1–22):** 1 (Share Capital) ✅ p.76 | 2 (Reserves & Surplus) ✅ p.77 |
3 (Long-Term Borrowings) ✅ p.77 | 4 (Trade Payables) ✅ p.78 | 5 (Other Current Liabilities)
✅ p.78 | 6 (Short-Term Provisions) — not independently confirmed in a rendered standalone
image; consolidated Note 6 used as proxy, flagged as GAP | 7 (PPE & Intangibles) — not
independently confirmed for standalone; consolidated Note 7 used as proxy, flagged as GAP |
8 (Non-Current Investments) — not independently confirmed for standalone in isolation;
consolidated Note 8 (near-identical composition) used, flagged as GAP | 9 (Deferred Tax
Assets, BS line) — covered via Note 21C.7 narrative, p.89 ✅ | 10 (Other Non-Current Assets) —
not independently confirmed for standalone; consolidated proxy used, GAP | 11 (Current
Investments) ✅ p.79/82 (partial) | 12 (Trade Receivables) ✅ p.82–83 | 13 (Cash & Cash
Equivalents) ✅ p.83 | 14 (Short-Term Loans and Advances) ✅ p.83 | 15 (Other Current Assets)
✅ p.83 (via consolidated proxy, near-identical) | 16 (Revenue from Operations) ✅ p.83 |
17 (Other Income) ✅ p.84 | 18 (Employee Benefits Expense) ✅ p.84/73 | 19 (Finance Cost) ✅
p.84 | 20 (Other Expenses) ✅ p.84–85 | 21 (Significant Accounting Policies & Other Notes,
Parts A/B/C, sub-notes 1–13 + Part C items 1–9) ✅ FULL, p.85–92 | 22 (Additional Regulatory
Information incl. ratios) ✅ FULL, p.92–94.

**CONSOLIDATED (Notes 1–22):** all 22 notes read directly and in full, p.108–118, plus
Independent Auditor's Report (incl. CARO-equivalent and audit-trail finding) p.95–103.

Gaps (Notes 6, 7, 8, 10 standalone not independently viewed in isolation) are judged low
incremental risk since the consolidated equivalents were read in full and standalone/
consolidated figures track closely elsewhere in the document (e.g., Note 14 identical, Note
12 receivables close, Note 16 revenue close) — but per pipeline discipline this gap is named
explicitly, not silently filled.

---

## PASS 1 SUMMARY — TOP 10 FINDINGS RANKED BY INVESTOR IMPORTANCE

1. **Gratuity/leave encashment on payment basis, not accrual — no actuarial provision at
   all.** (Note 21, Part 21B.7, p.86) 🔴 — profits overstated vs accrual accounting; no
   liability on balance sheet; no actuarial assumptions disclosed. SPEAR-confirmed.
2. **₹529.55L unsecured, open-ended, interest-bearing loans to undisclosed "Others"
   counterparties, repayable on demand.** (Note 14/14.1, p.83; corroborated CARO clause iii,
   p.66) 🔴 — opaque capital allocation; counterparty identity never named.
3. **Standalone trade receivables +76.3% YoY vs revenue +16.4%; turnover ratio −37.3% YoY
   (company's own mandatory variance disclosure); DSO ~47→~75 days; new 1–2yr ageing bucket
   appearing from zero.** (Note 12/12.1, Note 22(f), p.82–83, 93) 🔴 — cash-conversion
   deterioration.
4. **Standalone trade payables are NIL in both FY25 and FY24** despite ₹61 Cr revenue. (Note
   4, p.78) 🔴 — unexplained anomaly; either near-100% advance vendor payment or payables
   mislabelled elsewhere.
5. **Consolidated notes appear to omit the Significant Accounting Policies content
   (contingent liabilities table, RPT table, gratuity policy, EPS working) despite the
   Consolidated P&L cross-referencing "Note 22" for it; printed Note 22 contains only
   Additional Regulatory Information.** (p.117–118 vs P&L p.104–105) 🔴 — consolidated-FS
   disclosure gap.
6. **Consolidated auditor reports subsidiary accounting software lacked the mandatory
   audit-trail (edit-log) feature for FY25.** (Auditor's Report Annexure, p.~102–103) 🔴 —
   statutory IT-controls non-compliance, governance flag.
7. **"For Employee Benefits" provision of ₹255.14L on the balance sheet is inconsistent with
   the stated no-provision (cash-basis) gratuity/leave-encashment policy; composition
   undisclosed.** (Note 6 consolidated, p.111, vs Note 21B.7) 🔴 — needs management
   clarification.
8. **Related-party sales to wholly-owned subsidiaries = 32.2% of standalone revenue (FY25) /
   42.1% (FY24), with sharp re-routing between billing entities and 38.7% of standalone
   receivables owed by subsidiaries; DBX Holdings Ltd relationship (equity + trading, not
   subsidiary) undisclosed in nature.** (Note 21C.8, p.89–91) 🟡 — high RPT concentration,
   intercompany but opaque.
9. **Non-current investments jumped 11.4x (₹115.91L→₹1,325.25L) as the company built a
   listed-equity + FD treasury portfolio unrelated to core operations.** (Note 8, p.79/112)
   🟡 — capital-allocation and opportunity-cost question.
10. **Corpus/document identity mismatch: file labelled "FY2023 Annual Report" is actually
    the FY2024-25 (21st) Annual Report; no FY2023 AR exists in this corpus.** (whole
    document) 🔴 — pipeline data-integrity flag, not a company finding.

**Balancing positives (for context, not in the top-10 ranking):** clean/unqualified audit
opinion both standalone and consolidated 🟢; company is entirely debt-free, no bank borrowing
or working-capital facility anywhere in the Group 🟢; contingent liabilities NIL across all
categories both years 🟢; CSR fully compliant with no related-party CSR spend 🟢; no
promoter/director/KMP loans of any kind 🟢; DTA small and well-reconciled 🟢.
