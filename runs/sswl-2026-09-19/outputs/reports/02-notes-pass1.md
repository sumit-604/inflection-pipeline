# Stage 2 — Notes to Financial Statements, Triple Pass: PASS 1 (Full Extraction)

Company: Steel Strips Wheels Ltd (SSWL) | Run date: 2026-09-19
Source: inputs/annual-report/SSWL-AR-FY26-Reg34-2026-09-03.txt (page-marked text of the 245-page PDF; "AR p.N" below cites the PDF page)
Unit as printed on the face of every note: **₹ in Lakhs**. This report states every figure as "Rs X lakh (₹Y.YY Cr)" — 100 lakh = 1 Cr, applied once, never silently. FY26 = year ended 31-Mar-2026 (current); FY25 = year ended 31-Mar-2025 (comparative, restated where noted).

Scope: standalone notes 1–54 (AR p.144–183) and consolidated notes 1–56 (AR p.196–239), plus the Form AOC-1 subsidiary/associate schedule immediately following the consolidated notes (AR p.239–240). Nothing outside the notes (Board's Report, MD&A, corporate governance) was read for this pass.

COMPANY MEMORY LOAD-BEARING FACTS CHECKED AGAINST THE NOTES FIRST (per task instructions):
- **LBF3 (cash conversion / factoring / CFO)**: CONFIRMED and EXPANDED. Standalone Note 12+13 cash+other bank balances at FY26 close = Rs 151.25 lakh + Rs 500.89 lakh = Rs 652.14 lakh (₹6.52 Cr) — matches the "~Rs 6.5 Cr" load-bearing fact almost exactly (Note 12–13, AR p.161–162). The factoring/bill-discounting mechanism is Note 25's **Supplier Finance Arrangement** disclosure (reverse factoring on the payables side, not a receivables-side facility) — see Finding 2 below. This is the most load-bearing note-level discovery of the pass.
- **LBF4 (AMW NCLT gain, subsidiary status, carrying value)**: CONFIRMED AMW is 100% wholly owned (Note 52C consolidated, AR p.236; AOC-1, AR p.239) and PARTIALLY VERIFIED on the gain's downstream trail (retained-earnings/reserve movements now visible — Finding 1) but the FY24 gain itself is outside this AR's two-year comparative window (FY25/FY26 shown) and no note explains the Rs 364.52 Cr "Transfer to Capital Reserves" booked in FY26. See Finding 1 and Finding 5.

---

## 1. ACCOUNTING POLICIES & CHANGES

- **Basis of preparation**: Ind AS, historical cost except fair-valued financial instruments, assets held for sale, defined-benefit plan assets, share-based payments (Note 2.01, standalone AR p.144). 🟢
- **Revenue recognition (Ind AS 115)**: point-in-time on delivery for goods; standard variable-consideration/rebate/right-of-return language; no unusual acceleration language (Note 2.03, AR p.144–145). 🟢
- **Leases (Ind AS 116)**: incremental borrowing rate used, 9.00%–10.00% (Note 2.05 policy AR p.147; quantified in Note 5(a) AR p.159/214). ROU asset net carrying value grew from Rs 89.80 lakh to Rs 323.07 lakh (FY26 addition Rs 247.92 lakh); lease liability grew from Rs 20.20 lakh to Rs 246.81 lakh. Immaterial in absolute size. 🟢
- **Depreciation useful lives** (Note 2.11, AR p.148–149): Buildings 30–60 yrs, Plant & machinery 15–28 yrs, Furniture 3–10 yrs, Office equipment 3–10 yrs, Vehicles 5–8 yrs. Within Schedule II norms for an auto-ancillary manufacturer; residual value 5%. No useful-life change disclosed this year. 🟢
- **Capitalisation of R&D**: Note 3(4) and Note 5(5) (AR p.152–153/213): R&D capital expenditure (Dappar + Mehsana) fell sharply — Rs 27.45 lakh total FY26 vs Rs 3,162.87 lakh FY25 vs Rs 1,079.83 lakh FY24 — while R&D *revenue* expenditure kept rising (Rs 2,052.64 lakh FY26 vs Rs 1,868.52 lakh FY25). The FY25 spike was the Mehsana plant build-out; FY26 normalises. No capitalisation-threshold change disclosed. 🟢
- **Impairment (non-financial assets)**: standard value-in-use language; explicitly flags climate-risk (emission-reduction legislation cost) as a key assumption where material (Note 2.07, AR p.149–150). 🟢 (unusually explicit climate disclosure for this issuer class — noted, not a flag)
- **Segment reporting (Ind AS 108)**: "The Company deals in only one business segment of manufacturing and sale of auto ancillary equipment's" — no reportable segments (Note 2.18 policy AR p.155; quantified Note 44 standalone AR p.173–174, consol AR p.228–229). Only a domestic-vs-export geographic split is given (see Finding 9). 🟡
- **First-time adoption this year**: Ind AS 7/Ind AS 107 amendment on **Supplier Finance Arrangements** — first year of the new disclosure, transitional relief taken so FY25 comparative is not restated (Note 25, standalone AR p.166–167, consol AR p.221–222). See Finding 2. 🔴
- **ECL matrix**: standard "simplified approach" / provision matrix on trade receivables, no numeric matrix disclosed (policy only, Note 2.10, AR p.150). Actual provision is tiny — Rs 20.26 lakh against Rs 60,916.00 lakh gross receivables (0.03%) — unchanged both years despite receivables growing 25%. 🟡 (provision not scaled to growth — see Finding 7)
- **No revaluation of PPE/intangibles** either year, both standalone and consolidated (Note 53(X) AR p.182, Note 55(X) AR p.237). 🟢
- **No policy changes with quantified P&L impact** were found anywhere in the notes. 🟢

## 2. RELATED PARTY TRANSACTIONS

Full table, standalone (Note 41, AR p.170–172) — FY26 vs FY25, ₹ lakh:

| Nature | KMP | Relatives/NEDs | Enterprises (KMP control) | Associate (CMAPL) | Subsidiary (AMW) | Others | FY26 Total | FY25 Total | YoY % |
|---|---|---|---|---|---|---|---|---|---|
| CSR contribution | – | – | 315.00 | – | – | – | 315.00 | 319.00 | -1.3% |
| Rent paid | – | – | – | – | 147.44 | – | 147.44 | 42.15 | +249.8% |
| Sitting fee | – | 15.90 | – | – | – | – | 15.90 | 16.90 | -5.9% |
| Salary incl. commission | 1,568.90 | – | – | – | – | – | 1,568.90 | 1,637.18 | -4.2% |
| ESOP perquisite value | 162.77 | – | – | – | – | – | 162.77 | – | new |
| Equity shares issued incl. premium | 13.68 | – | – | – | – | – | 13.68 | – | new |
| Dividend paid | 582.40 | 120.02 | 502.51 | – | – | – | 1,204.93 | 959.63 | +25.6% |
| Interest received (on loan to AMW) | – | – | – | – | 870.64 | – | 870.64 | 1,027.15 | -15.2% |
| Purchase of power | – | – | – | 584.30 | – | 97.59 | 681.89 | 504.70 | +35.1% |
| Purchase of machinery/equipment | – | – | – | – | 168.45 | – | 168.45 | 640.10 | -73.7% |
| Security deposit paid | – | – | – | – | 270.00 | – | 270.00 | – | new |
| Advance for machinery (net of refund) | – | – | – | – | 28.32 | – | 28.32 | – | new |
| **Total** | 2,327.75 | 135.92 | 817.51 | 584.30 | 1,533.17 | 97.59 | **5,496.24** | **5,885.61** | -6.6% |

Outstanding balances at FY26 close, standalone (Note 41, AR p.171–172):
- **Loan to Subsidiary (AMW): Rs 13,315.00 lakh (₹133.15 Cr) — unchanged both years**, unsecured but interest-bearing. Interest accrued on this loan Rs 826.53 lakh FY26 vs Rs 584.33 lakh FY25 (accrual > cash received in FY26: cash received Rs 870.64 lakh vs accrual Rs 826.53 lakh, i.e. some FY25 accrual was collected in FY26).
- Payables for purchase of power to CMAPL (associate): Rs 135.24 lakh (FY26) vs Rs 79.16 lakh (FY25).
- Security deposit to AMW: Rs 270.00 lakh (new this year).
- Salary payable to KMP: Rs 853.57 lakh vs Rs 851.51 lakh.

RPT as % of standalone revenue (Rs 5,18,280.25 lakh, Note 30): 1.06% (FY26) vs 1.33% (FY25, on Rs 4,42,899.83 lakh revenue). Not a concentration concern in absolute terms, but the **Rs 133.15 Cr unsecured loan to a subsidiary that lost Rs 16.82 Cr in FY26** (AOC-1, AR p.239) is a support commitment worth naming (Finding 6).

Consolidated related-party table (Note 41, AR p.226–227) **excludes** the AMW loan and interest (eliminated on consolidation, as expected) and **excludes** the "Rent paid" line to AMW (also intragroup, eliminated) and the "Purchase of machinery" / "Security deposit paid" lines to AMW. Consolidated RPT total for FY26 = Rs 3,963.07 lakh vs Rs 4,147.53 lakh FY25 (-4.4%). No new related parties this year beyond the ESOP allotment mechanics. Non-arm's-length signal: none disclosed; Note 41(I) both statements assert arm's-length terms. 🟢/🟡 (loan to loss-making subsidiary is the one item worth watching, not the RPT quantum itself)

## 3. CONTINGENT LIABILITIES

Standalone and consolidated Note 40 (AR p.170 standalone, p.226 consolidated) are **identical in figures** (AMW carries none of its own):

| Item | FY26 | FY25 | YoY |
|---|---|---|---|
| LC/BG outstanding for import/purchase of RM, spares, P&M | Rs 6,022.11 lakh (₹60.22 Cr) | Rs 9,201.74 lakh (₹92.02 Cr) | -34.6% |
| Capital commitments (contracts remaining, net of advances) | Rs 15,510.57 lakh (₹155.11 Cr) | Rs 9,913.74 lakh (₹99.14 Cr) | +56.5% |

Net worth (standalone, per Other Equity + share capital, Note 18+19): Rs 1,71,906.87 lakh + Rs 1,571.80 lakh ≈ Rs 1,73,478.67 lakh (₹1,734.79 Cr). Contingent LC/BG of Rs 60.22 Cr is 3.5% of net worth — below the 10% single-item threshold. No tax dispute contingent liability is disclosed in either statement (the 17-Jun-2026 Customs show-cause notice, filed as a Reg 30 announcement, is NOT referenced anywhere in the notes — checked by full-text search; amount involved per the SCN itself is Rs 1.70 Cr already paid before the SCN issued, so its absence from Note 40 is consistent with immateriality, not an omission). No guarantees for subsidiary debt are disclosed (AMW's borrowings, if any, are not separately itemised in the notes — see Finding 5 gap). 🟢 on quantum; 🟡 the 56% jump in capital commitments is a capex-ramp signal worth carrying into Stage 3/5.

## 4. TRADE RECEIVABLES

Standalone = Consolidated (AMW contributes ~nil receivables; both notes show identical totals). Note 11, AR p.161 standalone / p.217 consolidated.

Ageing schedule, FY26 (₹ lakh):

| | Not due | <6mo | 6mo-1yr | 1-2yr | 2-3yr | >3yr | Total |
|---|---|---|---|---|---|---|---|
| Undisputed, good | 52,339.27 | 8,376.05 | 118.31 | 39.74 | 15.35 | 7.02 | 60,895.74 |
| Undisputed, doubtful | – | – | – | – | – | 20.26 | 20.26 |
| **Total** | **52,339.27** | **8,376.05** | **118.31** | **39.74** | **15.35** | **27.28** | **60,916.00** |

FY25 comparative total: Rs 48,657.64 lakh (Not due Rs 35,006.46 lakh; <6mo Rs 13,105.02 lakh).

- **Gross receivables grew 25.2% YoY** (Rs 48,657.64 lakh → Rs 60,916.00 lakh) against revenue growth of 17.0% (Note 30 total revenue Rs 4,42,899.83 lakh → Rs 5,18,280.25 lakh) or 11.4% on Note 44's gross sale revenue basis (Rs 5,47,160.90 lakh → Rs 6,09,477.00 lakh). Receivables outpacing revenue either way.
- Overdue book (>6 months) shrank in absolute terms (Rs 176.30 lakh FY26 vs Rs 546.75 lakh FY25) — the growth is concentrated in "not due" (Rs 52,339.27 lakh, +49.5% YoY) and, to a lesser extent, "<6 months" (Rs 8,376.05 lakh, -36.1% YoY). This is a **mix shift toward current receivables, not a deterioration in ageing quality** — worth stating precisely because it cuts against a naive "receivables are getting worse" read.
- ECL provision: flat Rs 20.26 lakh both years, i.e. it has not scaled with the 25% receivables growth — provision as % of gross receivables fell from 0.042% to 0.033%. Immaterial in absolute Rs terms either way. 🟡
- No customer concentration (>10%) is disclosed in the notes (not required to be, and not volunteered).
- No related-party receivables disclosed in Note 11 itself (the AMW-related receivable, if any working-capital in nature beyond the loan, is not separately shown).
- **Trade Receivable ratio (days)**, standalone Note 52 (AR p.181): 32.80 days FY26 vs 30.89 days FY25 (+6.18%).

🟡 Receivables growth outpacing revenue growth, generalized across the "not due" bucket rather than concentrated in overdue ageing — flagged for Stage 3/5 to cross-check against Q4 FY26 / Q1 FY27 results and the factoring note (Finding 2) for full cash-conversion picture.

## 5. INVENTORY

Standalone Note 10 (AR p.161) vs Consolidated Note 10 (AR p.216–217) — near-identical, small AMW contribution to Stores & Spares only (standalone Rs 32,100.73 lakh vs consolidated Rs 32,063.57 lakh — a *negative* Rs 37.16 lakh AMW contribution, i.e. consolidation adjustment/elimination, not additive; total inventory consolidated Rs 95,215.55 lakh is actually Rs 37.16 lakh *lower* than standalone Rs 95,252.71 lakh).

| Category | FY26 | FY25 | YoY |
|---|---|---|---|
| Raw material (hand) | 24,089.79 | 17,936.79 | +34.3% |
| Raw material (in transit) | 13,313.60 | 11,556.81 | +15.2% |
| WIP | 12,185.97 | 8,410.52 | +44.9% |
| Finished goods | 8,326.27 | 8,681.18 | -4.1% |
| Stores & spares | 32,100.73 | 25,534.17 | +25.7% |
| Scrap | 5,236.35 | 2,193.87 | +138.7% |
| **Total (standalone)** | **95,252.71** | **74,313.34** | **+28.2%** |

- Inventory grew 28.2% against revenue growth of 11–17% — outpacing revenue, driven mainly by raw material, WIP and stores/spares build-up (consistent with the capex ramp seen in Finding 10's capital commitments jump), and a **139% jump in scrap** (Rs 2,193.87 lakh → Rs 5,236.35 lakh) which is unexplained in the notes — no write-down or obsolescence note accompanies it. 🟡
- **Inventory turnover ratio (days)**, standalone Note 52: 59.71 days FY26 vs 59.34 days FY25 — nearly flat (+0.62%), so the Rs-value growth is a raw-material-price/volume effect more than a days-of-cover deterioration.
- No write-downs, no obsolete-inventory disclosure beyond the boilerplate policy language (Note 2.09(b)(v)). 🟢 on write-downs specifically, 🟡 on the unexplained scrap jump.

## 6. INVESTMENTS

**Standalone Note 6** (AR p.160): Investment in AMW Autocomponent Ltd (100%, wholly owned subsidiary) carried at **cost, Rs 500.00 lakh (₹5.00 Cr)** — unchanged both years, 50,00,000 equity shares of Rs 10 FV. Investment in Clean Max Astria Pvt Ltd (associate, 26%) Rs 1,089.11 lakh — unchanged, carried at cost standalone. Other unquoted equity (Nimbua Greenfield, Echanda Urja) Rs 19.40 lakh. **No impairment recognised on the AMW investment at standalone level despite AMW's continuing losses** (see Finding 5) — standalone accounts for subsidiaries at cost per Ind AS 27, so this is not itself irregular, but it means the standalone balance sheet carries a Rs 5 Cr investment against a subsidiary whose own net assets (per AOC-1, AR p.239) are Rs 22,450.99 lakh assets less Rs 14,852.67 lakh liabilities = Rs 7,598.32 lakh net assets (i.e. investment is carried far below AMW's own book net worth — conservative, not aggressive).

**Consolidated Note 6** (AR p.215–216): Associate investment carried at Rs 1,030.62 lakh (equity method, down from cost due to accumulated equity-method losses — opening Rs 350.22 lakh in FY24, plus Rs 693.09 lakh further investment in FY25, plus small profit shares). Consolidated Note 6(II) explicitly states: "the group has identified the investments where indicators of impairment exists and performed an impairment assessment... to ascertain the recoverable amount... Refer Note 52(C)" — **this is a management-judgment flag**: impairment indicators were identified (on the associate investment) even though no impairment was ultimately booked. 🟡

**Note 7 Loans** (standalone & consolidated, AR p.160/216): Rs 35.00 lakh advance for Panchkula land purchase, fully provided for (under litigation) — unchanged both years, fully provided, no incremental risk.

No ICDs/loans given to other entities beyond the AMW subsidiary loan (captured under RPT, Finding above). No unrealised gains/losses on other investments disclosed (all at cost, no FVTOCI equity elections evident in the notes).

**AMW Autocomponent Ltd standalone financials** (Form AOC-1, AR p.239): Share capital Rs 500.00 lakh; Reserves & surplus Rs 7,098.32 lakh; Total assets Rs 22,450.99 lakh; Total liabilities Rs 14,852.67 lakh; Turnover Rs 0 (nil — AMW has **no standalone turnover disclosed** in the AOC-1 line item, which is unusual for an operating subsidiary and should be checked against AMW's own financial statements if filed separately); PBT and PAT both Rs (1,681.78) lakh (₹-16.82 Cr) loss; 100% shareholding. 🔴 **AMW shows "Turnover: 0" in the statutory AOC-1 format** — either a disclosure artifact of the format (Schedule to Companies Act often nets or the field is populated differently) or a genuine finding that AMW earned no third-party turnover this year while still losing Rs 16.82 Cr. Needs verification in Stage 3/5.

## 7. BORROWINGS

Standalone Note 20/24/46 (AR p.165–166, p.174–180) vs Consolidated Note 20/24/46 (AR p.220–221, p.230) — figures are near-identical (AMW contributes negligible incremental debt):

| Instrument | FY26 | FY25 |
|---|---|---|
| Rupee term loans from banks (non-current) | 27,593.18 | 26,669.21 |
| Foreign currency term loans (non-current) | – | 1,192.94 |
| Rupee demand loans (current) | 20,536.45 | 18,307.20 |
| Buyers'/suppliers' credit FX loan for RM (current) | 12,822.40 | 17,291.28 |
| Current maturities of long-term borrowings | 10,626.39 | 9,246.43 |
| Unsecured, from banks | 11,011.70 | 10,036.31 |
| **Total borrowings** | **82,590.12** | **82,743.37** |

- Security: 1st pari passu charge on current assets (RM, WIP, FG, book debts, receivables); 2nd pari passu on fixed assets other than exclusively charged; term loans secured by title-deed mortgage on Dappar/Oragadam/Seraikella (and Mehsana getting first charge). All secured loans further secured by **personal guarantee of the Managing Director** — unusual but disclosed consistently both years (Note 46(1), AR p.174–175 standalone / p.230 consolidated). 🟡 (personal guarantee dependency, not a red flag on its own but a governance data point)
- **No covenant breaches or waivers** — explicit compliance statement both years (Note 46 / Note 49(b)).
- **Fixed vs floating**: 100% variable rate (Rs 27,593.18 lakh, Note 48(b)) — full exposure to rate moves; 50bp sensitivity = Rs 138 lakh (₹1.38 Cr) PBT impact.
- **5-year term-loan repayment schedule** (Note 46(2)): Yr1 Rs 10,626.39 lakh, Yr2 Rs 9,381.12 lakh, Yr3 Rs 7,817.84 lakh, Yr4 Rs 4,923.55 lakh, Yr5 Rs 3,781.21 lakh.
- **Interest capitalised**: Rs 6.71 lakh FY26 vs Rs 1,256.05 lakh FY25 — the FY25 figure reflects the Mehsana capex ramp (consistent with the R&D capex spike noted in Section 1); FY26's near-zero capitalisation signals the Mehsana project has substantially come out of construction.
- **No related-party borrowings** disclosed.
- **Net Debt/EBITDA**: standalone 1.57x FY26 vs 1.65x FY25 (Note 49, AR p.180); consolidated 1.59x FY26 vs 1.68x FY25 (Note 49, AR p.235) — mild deleveraging on this metric, despite the receivables/inventory growth noted above (the metric benefits from EBITDA growth: Rs 52,295.60 lakh FY26 vs Rs 50,025.36 lakh FY25 standalone). 🟢

## 8. TRADE PAYABLES

Standalone Note 25 (AR p.166–167); Consolidated Note 25 (AR p.221–222) — near-identical, AMW contributes a small incremental Rs 12.67 lakh to consolidated "Others" payables.

| | FY26 | FY25 | YoY |
|---|---|---|---|
| MSME | 5,078.92 | 3,586.68 | +41.6% |
| Others | 95,098.31 | 71,620.85 | +32.8% |
| **Total (standalone)** | **1,00,177.23** | **75,207.53** | **+33.2%** |

MSMED Act disclosure (Note 25, standalone AR p.167):

| | FY26 | FY25 |
|---|---|---|
| Principal amount due and remaining unpaid at year-end | 373.43 | 197.00 |
| Interest due on the above, unpaid | 5.52 | 2.91 |
| Interest paid during the year | – | – |
| Payment made beyond appointed day | – | – |

**Principal overdue-and-unpaid to MSME suppliers nearly doubled** (Rs 197.00 lakh → Rs 373.43 lakh, +89.6%), and the associated unpaid interest also nearly doubled (Rs 2.91 lakh → Rs 5.52 lakh). Small in absolute rupee terms (Rs 3.73 Cr) but the **direction and magnitude of change** (a near-doubling) is a vendor-payment-stress signal worth naming, especially alongside the Trade Payable Turnover ratio (below). 🟡

- **Trade Payable Turnover ratio (days)**, standalone Note 52: 75.64 days FY26 vs 69.29 days FY25 (+9.16%) — payment cycle stretching out.
- **Supplier Finance Arrangement** (reverse factoring) — see Finding 2, the single most important disclosure in Note 25. 🔴

## 9. PROVISIONS

- **Gratuity** (defined benefit, funded via LIC-managed trust): Note 43, standalone/consolidated identical (AMW is presumably on a separate/immaterial gratuity arrangement not consolidated in this note, or consolidated post-elimination equals standalone — AR p.172–174 standalone, p.227–228 consolidated).
  - PVO: Rs 3,325.55 lakh FY26 vs Rs 3,607.60 lakh FY25 (obligation *fell*, driven by a large actuarial gain: -Rs 564.39 lakh experience adjustment + -Rs 110.54 lakh financial-assumption change).
  - Plan assets: Rs 3,323.81 lakh FY26 vs Rs 3,088.92 lakh FY25 — **zero employer contribution in FY26** (vs Rs 750.00 lakh contributed in FY25) yet plan assets still grew via investment return, because the obligation itself shrank.
  - Net liability: Rs 1.73 lakh FY26 (near fully funded) vs Rs 518.67 lakh FY25 — funding status **improved sharply**, driven almost entirely by the actuarial gain, not by contributions.
  - Discount rate 7.25% FY26 vs 6.69% FY25 (up 56bp — this alone explains much of the PVO reduction); salary escalation flat 5.96%; attrition flat 10%; mortality table unchanged (IALM 2012-14).
  - Sensitivity: 1% discount-rate move = ±Rs 182–204 lakh on PVO; 1% salary-escalation move = ±Rs 177–194 lakh.
  - 🟢 Standard defined-benefit mechanics, no red flags; the swing from Rs 518.67 lakh net liability to Rs 1.73 lakh is a favourable actuarial (discount-rate) effect, correctly disclosed and reconciled.
- **Leave encashment**: Rs 374.39 lakh (non-current) + Rs 141.73 lakh (current) FY26 vs Rs 30.28 lakh + Rs 95.23 lakh FY25 — non-current leave provision jumped **12.4x** (Rs 30.28 lakh → Rs 374.39 lakh). No note explains this reclassification/re-estimate. 🟡
- **No warranty provision movement table** is disclosed (policy exists — Note 2.15/assumption (g) — but no separate warranty provision line appears in Note 22/28, implying either warranty is immaterial or embedded in "Other Payables"/expenses without a dedicated roll-forward). Given this is an auto-component OEM supplier, the absence of a warranty provision note is a **disclosure gap**, not necessarily a red flag on substance. 🟡
- **No onerous contracts, no decommissioning provisions** disclosed.
- **No litigation provisions** disclosed beyond the Note 7 land-advance provision (already covered).

## 10. DEFERRED TAX

**Standalone** (Note 51, AR p.180–181): Net DTL Rs 15,197.33 lakh FY26 vs Rs 15,266.07 lakh FY25 vs Rs 14,686.00 lakh FY24 — driven almost entirely by PPE/fixed-asset timing differences (Rs 15,763.74 lakh DTL on PPE). Effective tax rate 25.42% FY26 vs 25.55% FY25, close to the statutory 25.17% — clean reconciliation, no unusual permanent differences (Note 50C, AR p.180). 🟢

**Consolidated** (Note 51, AR p.236): Net DTL Rs 9,266.22 lakh FY26 vs Rs 9,828.59 lakh FY25 vs Rs 10,084.25 lakh FY24 — materially *lower* than standalone's DTL because of a consolidation-only DTA line: **"Carried forward tax losses and unabsorbed depreciation" — Rs 5,931.31 lakh FY26 vs Rs 5,437.68 lakh FY25 vs Rs 4,601.95 lakh FY24 ("on acquisition of Subsidiary")**. This is the DTA recognised on AMW's brought-forward tax losses at acquisition, and it has **grown every year since acquisition despite AMW continuing to post losses every year** (FY24 NCLT year, FY25 loss Rs 1,452.66 lakh consol share, FY26 loss Rs 1,188.15 lakh consol share — Note 53 consolidated, AR p.237). 🔴 **DTA realism risk**: recognising and growing a Rs 59.31 Cr deferred tax asset against carried-forward losses of a unit that has not yet turned profitable in three years under SSWL ownership requires "reasonable certainty of sufficient future taxable income" per the stated policy (Note 2.06) — the notes do not disclose the basis for that certainty (no forecast, no expiry-timeline disclosure for the underlying losses). Consolidated effective tax rate is correspondingly lower: 25.15% FY26 (24.59% FY25) vs standalone's 25.42%/25.55% — the "Tax impact of difference of tax rate of group companies" reconciling line (-Rs 493.63 lakh FY26, -Rs 268.99 lakh FY25, Note 50C consolidated) is the visible P&L benefit of this DTA build.

MAT credit: no MAT credit entitlement asset is separately disclosed in either Note 51 (policy exists at Note 2.06 but no line item appears, implying nil balance / not applicable — company is a regular taxpayer, not under MAT).

## 11. REVENUE DETAILS

Note 30 (Revenue from operations) + Note 44 (Segment reporting), standalone AR p.168/173–174, consolidated AR p.223/228–229. Standalone and consolidated revenue are **identical** (AMW has zero disclosed turnover per AOC-1 — see Finding 5/Section 6 above).

| | FY26 | FY25 | YoY |
|---|---|---|---|
| Export | 45,351.35 | 56,117.09 | -19.2% |
| Domestic | 4,72,143.14 | 3,85,359.37 | +22.5% |
| Sale of products | 5,17,494.49 | 4,41,476.46 | +17.2% |
| Duty drawback income | 495.37 | 1,169.70 | -57.6% |
| Job work income | 290.39 | 253.67 | +14.5% |
| **Total revenue from operations** | **5,18,280.25** | **4,42,899.83** | **+17.0%** |

- **Exports fell 19.2%** while domestic revenue grew 22.5% — a material geographic mix shift toward the domestic market this year. This runs counter to LBF1's export-growth guidance framing (which is a Stage-3/5 verification item, not resolved by the notes alone) but the notes confirm the *direction*: exports were Rs 561.17 Cr FY25 → Rs 453.51 Cr FY26, a decline, not the growth the guidance context implies.
- **Duty drawback income (other operating revenue) fell 57.6%** (Rs 1,169.70 lakh → Rs 495.37 lakh) — consistent with the export decline, and relevant background to the Customs SCN (Section 3) which specifically concerned duty drawback/RoDTEP claims (though the SCN's Rs 1.70 Cr quantum is immaterial next to this Rs 674 lakh YoY swing).
- **No product-level disaggregation** (steel wheel vs alloy wheel vs steering knuckle) anywhere in the notes — single business segment (Note 44). See Finding 9.
- **No contract assets/contract liabilities** balances are disclosed as separate line items (policy describes them in Note 2.03 but no balance-sheet line or note table shows a contract-asset/contract-liability balance — implying nil or immaterial, consistent with point-in-time delivery recognition and no significant advance-billing practice, aside from "Advances from customers" Rs 44.14 lakh appearing new in consolidated Note 29 FY26, AR p.223).
- **No top-customer revenue concentration** disclosed (not required; OEM-industry norm to withhold this).
- Geographic segment: domestic Rs 5,64,125.65 lakh (92.6%) vs export Rs 45,351.35 lakh (7.4%) FY26, using the Note 44 gross-sale-revenue basis (which differs slightly from Note 30's Sale-of-Products figure due to classification — both are presented verbatim from the AR without reconciliation in the notes themselves).

## 12. OTHER CRITICAL NOTES

- **Exceptional items**: NIL both years, both statements (Note 38, standalone AR p.170, consolidated AR p.225–226). The FY24 AMW NCLT gain (LBF4) is therefore **outside this AR's disclosed P&L window** — it would have appeared as an FY24 exceptional item in the FY25 AR, not here. 🟢 (consistent with company memory, not a fresh finding)
- **Goodwill**: no goodwill balance or impairment-sensitivity note appears anywhere in the consolidated notes — implying the AMW acquisition (an NCLT resolution-plan acquisition) generated no goodwill (likely a bargain purchase / capital reserve outcome instead, consistent with Finding 1's unexplained Capital Reserve movement, though the notes never use the words "bargain purchase" or connect the two).
- **Intangibles**: Note 5, immaterial (Rs 63.00 lakh net carrying value FY26, fully legacy, no additions either year).
- **Capital commitments**: Rs 155.11 Cr FY26 vs Rs 99.14 Cr FY25, +56.5% (Note 40, Section 3 above).
- **Foreign currency exposure and hedging**: Note 48(c), standalone AR p.178–179, consolidated AR p.233–234 — see Finding 3. Forward/option notional: USD sell 596.95 lakh (USD 59.7mn), EUR sell 0.38 lakh, EUR buy 182.76 lakh, USD buy 0.34 lakh, **Put & Call Options against USD/INR notional 250.00 lakh (USD 25mn)**. **Mark-to-market loss Rs 3,241.87 lakh (₹32.42 Cr) as at 31-Mar-2026** — no FY25 comparative is shown for this specific MTM line (first appearance in this disclosure format). 🔴
- **Segment reporting**: single segment, geographic split only (Section 11 above / Finding 9).
- **Basic vs diluted EPS gap**: standalone Basic Rs 12.86 vs Diluted Rs 12.82 (FY26); Rs 13.38 vs Rs 13.32 (FY25) — dilution source is the ESOP scheme (weighted average diluted shares 15,75,81,542 vs basic 15,71,23,326 FY26). Consolidated Basic Rs 12.11 vs Diluted Rs 12.07 (FY26); Rs 12.44 vs Rs 12.39 (FY25). Gap is small (~0.3–0.4%) and fully explained by ESOP (Note 47). 🟢
- **Events after balance sheet date**: **no subsequent-events note appears anywhere** in either the standalone or consolidated notes (confirmed by full-text search across the entire AR text for "subsequent", "events after", "Customs", "show cause" — zero hits). The AR was board-approved 29-May-2026 and filed 03-Sep-2026; the Customs SCN (17-Jun-2026, ~Rs 1.70 Cr, already paid) falls in that window but is immaterial and its absence is not itself irregular. Worth noting as a **process observation**: this AR carries no subsequent-events note format at all (not even a "no material subsequent events" boilerplate line), which is a disclosure-completeness gap regardless of whether anything material needed disclosing. 🟡
- **CSR**: Note 45 both statements, identical. Required Rs 552.67 lakh (after Rs 78.37 lakh prior-year carry-forward set-off — gross obligation before set-off would be higher), spent Rs 634.95 lakh (over-spent by Rs 160.65 lakh, carried forward for future set-off). CSR contribution routed through Hansraj Trust (a related party, per Section 2) — Rs 315.00 lakh contributed, but HRT itself only spent Rs 314.68 lakh, with the company "considering" the trust's actual spend as its own CSR spend (Note 45D) — a related-party CSR-routing structure worth naming, though the shortfall (Rs 0.32 lakh) is trivial. 🟡 (structure, not quantum)
- **ESOP dilution**: Note 47, three tranches under ESOS 2021, 2,51,100 shares allotted in FY26 at Rs 20 exercise price against a market price of Rs 171.86–257.65 at grant/exercise — meaningful intrinsic value transfer to employees but fair-value expensed (Rs 730.32 lakh FY26 P&L charge, Note 34) so no EPS distortion beyond the disclosed dilution.
- **Share capital changes**: 2,51,100 new equity shares issued (ESOP exercise) — the only capital change; no bonus, no rights issue, no scheme of arrangement (Note 53(V)/55(V) explicitly confirm no scheme of arrangement with accounting impact).
- **Direct debits/credits to reserves bypassing P&L**: **the Rs 364.52 Cr "Transfer to Capital Reserves" in consolidated Other Equity (Note 19) is exactly this** — a direct equity-to-equity reserve movement with zero explanatory note anywhere in the document. This is Finding 1, the single most significant item in this pass.

---

## PASS 1 SUMMARY — TOP 10 FINDINGS RANKED BY INVESTOR IMPORTANCE

| # | Finding | Note anchor | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Consolidated Other Equity shows a **Rs 364.52 Cr "Transfer to Capital Reserves"** in FY26 (Rs 0 in FY25), driving consolidated Retained Earnings to **-Rs 826.70 Cr**. No note anywhere explains the source, the accounting basis, or its connection to the AMW acquisition. | Note 19, consol AR p.219–220 | 🔴 Red Flag | The largest unexplained equity movement in the filing; directly touches LBF4 (AMW/NCLT gain trail). A Rs 364.52 Cr reserve reclassification with zero disclosure is a material transparency gap that Stage 3/5/8 must chase via the Board's Report, prior-year (FY25) AR, or a direct management question. |
| 2 | **Supplier Finance Arrangement (reverse factoring)**: Rs 676.50 Cr of trade payables (67.6% of the Rs 1,001.77 Cr standalone total) sit under a third-party financial-institution arrangement; Rs 494.84 Cr of that was already paid to suppliers by the institution at year-end. First year of Ind AS 7/107 disclosure — no FY25 comparative provided (transitional relief). | Note 25, standalone AR p.166–167, consol AR p.221–222 | 🔴 Red Flag | This is the mechanism behind LBF3. It classifies what is economically short-term financing as an operating trade payable, which (a) keeps the debt off the borrowings note, (b) flatters the current ratio and Net Debt/EBITDA, and (c) routes the cash effect through operating (not financing) cash flow per the note's own statement. Cash-conversion quality assessment in Stage 3/5 must treat this Rs 676.50 Cr as debt-like. |
| 3 | **Mark-to-market loss on FX forwards/options of Rs 32.42 Cr** at FY26 close, including a USD 25mn notional **Put & Call Options** position (not a plain forward hedge). No FY25 comparative shown; no note states which P&L line absorbed it. | Note 48(c), standalone AR p.178–179, consol AR p.233–234 | 🔴 Red Flag | Rs 32.42 Cr is ~16% of standalone FY26 PAT (Rs 202.09 Cr). Options positions (vs forwards) suggest a more speculative hedge structure than "natural hedge" language in the same note implies. The P&L/OCI treatment is not traceable from the notes alone — needs reconciliation against Note 37's Rs 8.62 Cr disclosed FX loss, which does not explain the gap. |
| 4 | **"Interest Others" of Rs 69.85 Cr** within finance costs — 1.4x the combined disclosed bank interest (term loan + WC loan + FX loan = Rs 50.31 Cr) — with no sub-note breaking it down. | Note 35, standalone AR p.169, consol AR p.224 | 🟡 Watch | Likely includes SCF/bill-discounting charges (Finding 2) and/or the FX derivative cost (Finding 3), but the note offers no breakdown. Opacity on a Rs 69.85 Cr line (10.1% of FY26 revenue's interest burden) limits verifiability of true borrowing cost and cash-conversion quality. |
| 5 | **AMW Autocomponent Ltd (100% subsidiary)**: third consecutive year of losses (FY26 standalone loss Rs 16.82 Cr per AOC-1; consol share -Rs 11.88 Cr), net assets falling (Rs 82.49 Cr → Rs 70.61 Cr consol basis), **Turnover disclosed as "0"** in the AOC-1 schedule, and a growing **Rs 59.31 Cr deferred tax asset on AMW's carried-forward tax losses** recognised despite continuing losses. | Note 51/52/53 consol AR p.236–238; AOC-1 AR p.239 | 🔴 Red Flag | Combines three concerns: (a) DTA realism — recognising and *growing* a DTA against a loss-making unit's carried-forward losses needs disclosed forecast support that is absent; (b) a wholly-owned operating subsidiary reporting zero turnover is either a disclosure artifact or a going-concern-adjacent signal; (c) directly resolves/extends LBF4. |
| 6 | SSWL carries an **unsecured, interest-bearing Rs 133.15 Cr loan to AMW**, unchanged for two years, while AMW continues to lose money. Interest accrued Rs 8.27 Cr FY26. | Note 41, standalone AR p.171–172 | 🟡 Watch | A related-party support commitment to a loss-making subsidiary, eliminated on consolidation so it is invisible in the consolidated statements — visible only in the standalone notes. Position-sizing and downside-scenario work (Stage 11/FTTCP) should treat this as a contingent capital commitment to AMW, not a risk-free intercompany asset. |
| 7 | **Working capital deterioration**: trade receivables +25.2% YoY vs revenue +11–17%; Net Capital Turnover ratio (working capital days) worsened 59.4% (11.24 → 17.93 days); Trade Payable days stretched 69.29 → 75.64; inventory +28.2% YoY. | Notes 11, 25, 10, 52 standalone AR p.161/166–167/161/181–182 | 🟡 Watch | Every working-capital line moved the wrong direction simultaneously (receivables up, payables stretching, inventory up) even as headline profitability metrics (ROE 15.08%→12.74%, ROCE 20.85%→18.62%, net margin 4.74%→3.90%, all Note 52) also compressed. This is a coherent, multi-note cash-conversion-quality signal, not an isolated line item — directly resolves LBF3's core question. |
| 8 | **MSME payables overdue-and-unpaid nearly doubled** (Rs 1.97 Cr → Rs 3.73 Cr); unpaid interest on delayed MSME payments also nearly doubled (Rs 2.91 lakh → Rs 5.52 lakh). | Note 25, standalone AR p.166–167 | 🟡 Watch | Small in absolute Rs terms but the rate of change (a near-doubling) is a vendor-payment-stress signal that corroborates Finding 7's broader working-capital read. |
| 9 | **No product-level segment disclosure anywhere in the notes** — single business segment under Ind AS 108, geography-only split. | Note 44, standalone AR p.173–174, consol AR p.228–229 | 🟡 Watch | LBF2 (mix-shift margin, alloy ~35% of revenue, EBITDA/wheel by product) **cannot be verified or cross-checked from the AR notes at all** — this evidence gap must be closed via investor decks/concalls/results (outside this pass's scope), and Stage 3/5/8 should not treat any AR-notes-derived figure as corroborating or refuting LBF2. |
| 10 | **Capital commitments up 56.5%** (Rs 99.14 Cr → Rs 155.11 Cr) while contingent LC/BG exposure fell 34.6% (Rs 92.02 Cr → Rs 60.22 Cr); Net Debt/EBITDA improved mildly (1.65x→1.57x standalone, 1.68x→1.59x consol). | Note 40, 49 | 🟢/🟡 | A capex-ramp signal (consistent with declining interest capitalisation elsewhere, Section 7) sitting alongside stable leverage — not alarming on its own, but should be read together with Finding 7's working-capital strain when Stage 5/11 model near-term free cash flow. |

**Notes not yet separately flagged that Pass 2 should re-check**: the R&D capex/opex split (Section 1), the leave-encashment 12.4x provision jump (Section 9), the CSR-routing-through-related-party structure (Section 12), the missing warranty provision roll-forward (Section 9), and the complete absence of any subsequent-events note format (Section 12).

PASS 1 rating tally: 🔴 Red Flag = 5 (Findings 1, 2, 3, 5, and the MTM/DTA items); 🟡 Watch = 5 (Findings 4, 6, 7, 8, 9); 🟢 Clean = policies, gratuity mechanics, deferred tax reconciliation quality (standalone), EPS dilution, leverage trend.
