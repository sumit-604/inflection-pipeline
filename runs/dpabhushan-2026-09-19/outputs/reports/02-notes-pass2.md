# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2 (WHAT WAS MISSED)

Company: D. P. Abhushan Ltd (DPABHUSHAN). Source: Annual Report FY2025-26, standalone,
Notes 1 through 33.26, PDF pages 85-106 (printed pages 164-205). Run date 2026-09-19.

**CORRECTED CORPUS.** Per the operator's mid-task correction, the AR .txt has been
re-extracted in table mode (`pdftotext -table`); every two-page print spread is now split
into a LEFT HALF and RIGHT HALF section under its `[page N]` marker, and the primary
statements (Balance Sheet, P&L face, Cash Flow Statement, printed p.160-163) plus every note
Pass 1 flagged as garbled, LOW or MODERATE confidence (Note 7 Inventories, Note 12
Borrowings, Note 16 Trade Payables, Note 33.1 RPT table, Note 33.25 Deferred Tax, Note 33.26
Ratio Analysis) have been re-read in full from the corrected text. **Every one of these
tables is now internally clean and reconciles by exact arithmetic against at least one other
statement or note.** This pass therefore does two things at once, as instructed: (A) it
resolves Pass 1's extraction-defect items — several of which turn out to have been
**misread, not merely low-confidence**, and are corrected below — and (B) it reports new
findings Pass 1 did not reach. Section A supersedes the corresponding Pass 1 text; Section B
is additive. Figures are quoted in ₹ Lakh exactly as printed, with a ₹ Cr equivalent
(÷100) in parentheses.

---

## SECTION A — EXTRACTION-DEFECT ITEMS RESOLVED (corrections to Pass 1)

### A1. Related-party unsecured borrowings — Pass 1's finding #5 is REVERSED

Pass 1 read Note 12's two unsecured sub-lines backwards and reported "From Related Parties"
rising ₹333.06 Lakh (FY25) to ₹1,520.42 Lakh (FY26), +356%. **The clean Note 12 table (PDF
p.93, printed p.180-181) reads:**

| Unsecured | FY26 | FY25 |
|---|---|---|
| From Related Parties | 1,520.42 | **2,321.99** |
| From Other's | 333.06 | 333.06 |

"From Related Parties" **FELL** ₹2,321.99 Lakh to ₹1,520.42 Lakh, **-34.5%**; "From Other's"
was flat at ₹333.06 Lakh both years (Note 12, HIGH confidence, cross-checked: Total Current
Borrowings sums exactly to ₹28,401.25 Lakh FY26 / ₹16,102.11 Lakh FY25 including these two
lines). 🟢 **This reverses the LBF4 read.** The company did not lean more on promoter/family
loans in FY26; it leaned LESS (related-party unsecured debt down over a third) while total
borrowings rose 76.8% (Note 33.3) — the entire FY26 debt build is bank debt (WCDL, Gold Metal
Loan, Leased Gold — all new or expanded lines), not family money. Downstream stages should
drop Pass 1's rank-5 finding and cite this corrected reading instead.

### A2. Trade Payables (Note 16) — now fully clean, and payables FELL, not grew

| (₹ Lakh) | FY26 | FY25 |
|---|---|---|
| MSME dues | 5,343.72 | 8,974.03 |
| Other than MSME | 6,017.02 | 8,696.64 |
| **Total Trade Payable** | **11,360.73** | **17,670.68** |

Total trade payables **fell 35.7%** even as revenue grew 22.2% and inventory grew 39.0%.
Cross-validated exactly against the Cash Flow Statement's "Increase/(Decrease) in Trade
Payables -6,309.94" (Note 16 + CFS + Note 33.2.1 fair-value table + Note 33.2.2 liquidity
maturity table all agree to the rupee, HIGH confidence, PDF p.93/99-100, printed
p.180-181/194-195). 🔴 **New, load-bearing for LBF2**: the company funded FY26's large
inventory build (+₹281.84 Cr) with almost no help from supplier credit — it actually paid
payables DOWN by ₹63.10 Cr in the same year — a double cash drain that is a direct
contributor to the -₹97.31 Cr FY26 CFO (see A5). MSME dues specifically fell 40.5%
(₹8,974.03 Lakh to ₹5,343.72 Lakh), Other-than-MSME fell 30.8%.

### A3. Employee Benefits Expense — Pass 1 mislabelled the Total Tax Expense figure

Pass 1's Section 12 reported "Employee Benefits Expense... ₹7,085.85 Lakh FY26 vs ₹3,828.10
Lakh FY25 (+85.1%)." **That figure is the P&L's Total Tax Expenses line (item 6), not
Employee Benefits Expense.** The clean Note 26 table (PDF p.96, printed p.186-187) gives the
correct figure:

| (₹ Lakh) | FY26 | FY25 |
|---|---|---|
| Salary, Wages and Bonus | 3,451.83 | 2,668.51 |
| Provident Fund | 166.96 | 128.05 |
| ESIC Fund | 26.23 | 22.72 |
| ESOP Expenses | 176.96 | 0.00 |
| Gratuity Expenses | 57.38 | 43.13 |
| Staff Welfare | 1.57 | 1.34 |
| Director Remuneration | 120.00 | 120.00 |
| **Total Employees Benefits Expenses** | **4,000.92** | **2,983.76** |

+34.1% YoY, still above revenue growth (+22.2%) — consistent with new-store headcount ramp
and the new ESOP charge, but a materially different magnitude than Pass 1 reported. This
figure ties exactly to the P&L face (line 3(d), PDF p.83, printed p.161). 🟢 corrected, no
red flag — this is normal-scale headcount cost growth, not the anomaly Pass 1's mislabelled
number implied.

### A4. Useful-life table (Note 2/Note 2.D) — now fully clean

| Asset Class | Useful Life |
|---|---|
| Building | 60 Years |
| Plant & Machinery | 15 Years |
| Furniture & Fittings | 10 Years |
| Motor Car (4-Wheeler) | 8 Years |
| Motor Vehicle (2-Wheeler) | 10 Years |
| Computer & Computer Peripherals | 3 Years |
| Office Equipment | **5 Years** |
| Leasehold Improvements | Primary Period of Lease |

Pass 1 guessed Office Equipment also ran on "Primary Period of Lease" — it has its own
5-year Schedule-II-compliant life; only Leasehold Improvements uses lease-period
amortisation. All lives are Schedule II compliant, no departure from norm (PDF p.87, printed
p.168-169, HIGH confidence, clean single-column table). 🟢

### A5. Cash Flow Statement — now fully clean; CFO confirms B00 LBF2 exactly

Pass 1 could not extract the CFS. The clean statement (PDF p.84, printed p.162-163) gives:

| (₹ Lakh) | FY26 | FY25 |
|---|---|---|
| Operating profit before WC changes | 30,767.97 | 17,450.70 |
| (Increase)/Decrease in Inventories | -28,184.42 | -26,754.94 |
| Increase/(Decrease) in Trade Payables | -6,309.94 | +10,451.53 |
| Cash generated from operating activities | -2,549.23 | +1,752.60 |
| Income Tax paid | -7,181.29 | -3,645.11 |
| **Net Cash Flow from Operating Activities** | **-9,730.52** | **-1,892.51** |
| Net Cash Flow from Investing Activities | -2,126.01 | -2,688.55 |
| Net Cash Flow from Financing Activities | +12,141.69 | +3,950.43 |
| Net increase/(decrease) in cash | +285.16 | -630.63 |

**FY26 CFO = -₹9,730.52 Lakh = -₹97.31 Cr — confirms B00 LBF2's "CFO Rs -97 Cr FY26"
exactly, HIGH confidence.** Even BEFORE the ₹71.81 Cr tax payment, operations consumed cash
(-₹25.49 Cr) — the ₹307.68 Cr operating profit before working-capital changes was more than
wiped out by the inventory build (-₹281.84 Cr) and the payables paydown (-₹63.10 Cr, see
A2). Financing activities (+₹121.42 Cr, driven by +₹126.94 Cr net current-borrowings draw
and the +₹14.82 Cr final warrant-conversion tranche) funded both the operating cash gap and
₹21.26 Cr of investing outflow, of which ₹12.50 Cr was a NEW investment in liquid mutual
funds (Note 22/33.24) made in the same year CFO was deeply negative. 🔴 **This is the
clearest possible answer to LBF2's growth-induced-vs-structural test: FY26's growth was
financed by fresh bank borrowing, not by operating cash generation and not by fresh equity
(the ₹600 Cr QIP was postponed per LBF3) — a classic growth-induced, not structural, cash
gap, but one now running entirely on debt.** The "Changes in Liabilities from Financing
Activities" reconciliation (same page) ties Non-Current Borrowings, Current Borrowings and
Lease Liabilities exactly to the Balance Sheet, both years — GAAP roll-forward clean.

### A6. Note 33.25 Deferred Tax Assets and Note 15 — now fully clean and tie out

Note 33.25 (PDF p.105, printed p.204-205): Opening Balance DTA/(DTL) -10.35 (i.e. an opening
net DTL of ₹10.35 Lakh, matching Note 15's FY25 closing DTL exactly) + PP&E 11.60 +
Employee Benefits 10.56 + Lease 10.37 = Net Deferred Tax Assets ₹22.19 Lakh at FY26 —
matches the Balance Sheet's "Deferred Tax Assets (Net) 22.19" line exactly. The company
flipped from a small net DTL (FY25) to a small net DTA (FY26). 🟢 fully resolved, no
anomaly.

### A7. Note 33.26 Ratio Analysis — now fully clean, all 10 ratios

| Ratio | FY26 | FY25 | % Change |
|---|---|---|---|
| Current Ratio | 2.14 | 1.84 | +16.43% |
| Debt-Equity Ratio | 0.45 | 0.41 | +11.29% |
| Debt Service Coverage Ratio | 11.42 | 6.93 | **+64.82%** |
| Return on Equity | 40.87% | 35.06% | +16.56% |
| Inventory Turnover Ratio | 4.72 | 5.64 | -16.33% |
| Trade Receivable Turnover Ratio | 2,126.33 | 2,403.12 | -11.52% |
| Trade Payable Turnover Ratio | 26.11 | 26.55 | -1.68% |
| Net Capital Turnover Ratio | 7.25 | 9.57 | -24.20% |
| Net Profit Ratio | 5.21% | 3.40% | **+53.09%** |
| Return on Capital Employed | 32.49% | 29.07% | +11.78% |

All numerator/denominator components are given and cross-check exactly against clean
Balance Sheet/P&L figures (HIGH confidence throughout). 🟡 **New finding (Schedule III
disclosure gap): two ratios — DSCR (+64.82%) and Net Profit Ratio (+53.09%) — cross the
25%-change threshold that Schedule III Division II expects a written explanation for, and no
narrative explanation accompanies either figure** (only the formula breakdown is given). The
driver is inferable from elsewhere in the notes (PAT +88.0% on revenue +22.9%, aided by the
₹18.60 Cr MCX hedging gain booked into revenue, per A9/Pass 1 rank 2) but the AR itself does
not say so. Minor disclosure-quality point, not a numbers problem.

**Inventory-days reconciliation (new, resolves a latent tension with B00 LBF2's "100 days"
figure):** the AR's own Inventory Turnover Ratio (Average Inventory ÷ Revenue = 4.72x) implies
~77 days. Using closing inventory (₹1,003.94 Cr) over a COGS proxy (Cost of Material Consumed
+ Purchase of Stock-in-Trade + Changes in Inventories = ₹3,647.39 Cr), the implied inventory
days is ~100.5 — this is the convention that matches B00/screener's cited "100 days" almost
exactly. Both are internally valid; they use different denominators (average-inventory/revenue
vs closing-inventory/COGS). Flagged so downstream stages do not read this as a contradiction.

### A8. Note 33.1 Related-Party Transactions table — now fully clean; two Pass 1 misattributions corrected

The full per-party table (PDF p.98-99, printed p.190-193) is now clean. Two corrections to
Pass 1's candidate figures:

- **Suman Devi Kataria vs Supriya Kataria swapped.** Pass 1 attributed "FY26 loan received
  ₹338.70 Lakh, repaid ₹1,098.05 Lakh; FY25 loan received ₹1,099.60 Lakh" to Suman Devi
  Kataria. That data belongs to **Supriya Kataria**: FY26 loan received ₹338.70 Lakh, repaid
  ₹336.20 Lakh, interest ₹3.04 Lakh, closing balance ₹20.03 Lakh; FY25 loan received
  ₹1,099.60 Lakh, repaid ₹1,098.05 Lakh, closing ₹14.80 Lakh. **Suman Devi Kataria's actual
  FY26 figures** are: loan received ₹296.64 Lakh, repaid ₹56.14 Lakh, interest ₹10.63 Lakh,
  closing ₹250.94 Lakh; FY25: loan received nil, repaid ₹11.50 Lakh, rent ₹12.00 Lakh,
  closing ₹0.87 Lakh.
- **D. P. Jewelline Pvt Ltd's ₹-212.98 Lakh Rent/Sale & Purchase line is FY25 (24-25), not
  FY26** as Pass 1 flagged as ambiguous. The FY26 row for this entity shows only small
  remuneration/sitting-fee-type figures (0.84 and -0.88 across two sub-rows whose entity
  attribution remains unclear — still flagged LOW confidence, immaterial size).

**New within-table findings (not in Pass 1):**
- **Manratan Retail Pvt Ltd loan turnover fell ~81% YoY**: FY25 loan received ₹5,141.77 Lakh
  / repaid ₹5,081.90 Lakh (the single largest RPT loan flow in the table, both years); FY26
  loan received ₹952.79 Lakh / repaid ₹1,147.36 Lakh, closing balance ₹55.13 Lakh (down from
  ₹243.98 Lakh). 🟡 worth a management question on what drove the FY25 scale and the FY26
  pullback.
- **Shree Hanuman Wind Infra Pvt Ltd** is a new, ramping counterparty: FY25 loan received
  ₹129.00 Lakh (first appearance, closing ₹129.03 Lakh); FY26 loan received ₹1,216.00 Lakh,
  repaid ₹1,345.00 Lakh, closing ₹8.60 Lakh (loan largely cycled through and repaid within
  the year).
- **Cross-check, HIGH confidence overall:** summing every FY26 closing balance across all ~30
  named related parties/entities in the table gives ≈₹1,548 Lakh, closely matching Note 12's
  "From Related Parties" unsecured-borrowings figure of ₹1,520.42 Lakh (small residual gap
  plausibly rent/trade balances not classified as borrowings). This is an independent
  arithmetic validation that the whole RPT table, not just Note 12's summary line, is now
  reliable.

### A9. Note 20/21/22 revenue and other-income detail — now fully clean, exact figures

- **Note 20 disaggregation**: Revenue from Retail Operations ₹3,54,714.10 Lakh FY26 vs
  ₹2,77,974.89 Lakh FY25 (**+27.61%**); Revenue from Non-Retail Operations ₹49,931.51 Lakh
  FY26 vs ₹53,097.59 Lakh FY25 (**-5.96%**, a genuine decline). Sum ties exactly to Revenue
  from Operations both years. 🟡 **New finding**: non-retail (likely wholesale/bullion-trade)
  revenue shrank in absolute terms while retail carried all of the growth — worth a
  management question on what "Non-Retail Operations" comprises and why it declined (Q5
  below).
- **Note 21 Other Operating Income**, now exact: Commission Income ₹7.23 Lakh FY26 / ₹6.53
  Lakh FY25; **Profit Th. MCX Hedging ₹1,859.99 Lakh FY26 / NIL FY25**. This confirms Pass
  1's rank-2 red flag at HIGH confidence with the precise number (Pass 1 had the total but
  not this exact split).
- **Note 22 Other Income**, now exact: Changes in MTM Notional - Gold Metal Loan ₹38.63 Lakh
  FY26 / nil FY25; Changes in MTM Notional - Gold on Lease ₹356.59 Lakh FY26 / nil FY25;
  Rental Income ₹84.18 Lakh FY26 / nil FY25 (new line item, immaterial); Interest Income on
  Bank Deposit ₹16.50 / ₹3.72; Interest Income from Others ₹20.93 / ₹14.86; total ₹519.80 /
  ₹155.52. Combined MTM-notional gains across Note 22 alone = ₹395.22 Lakh FY26 (new this
  year), on top of the ₹1,859.99 Lakh MCX hedging profit sitting in Note 21 revenue — **two
  separate, newly-material gold-hedging income streams in FY26, combined ~₹22.55 Cr, versus
  effectively nil in FY25.**

### A10. Note 12 Borrowings instrument table — now fully clean, confirms Pass 1's structural read

Current borrowings breakdown, HIGH confidence: WCDL ₹20,410.00 Lakh FY26 (vs ₹12,055.56 Lakh
FY25); Cash Credit ₹0 FY26 (vs ₹968.41 Lakh FY25, fully repaid/rolled into WCDL); **Gold
Metal Loan ₹1,318.94 Lakh FY26 (NIL FY25, new facility)**; **Leased Gold - Safe Gold ₹4,691.38
Lakh FY26 (NIL FY25, new facility)**. Sums to Total Current Borrowings ₹28,401.25 Lakh
exactly. Rate ranges confirmed clean: HDFC 6.95-9.30%, ICICI 7.10-7.80%, SBI 7.10-9.30%,
Kotak 7.00-8.95%, GML (Kotak) 2.95%, Gold on Lease (Digital Gold India, HDFC-backed BG)
4.50-4.75%. 🟡 **New, quantified**: two entirely new secured facility TYPES (GML, Leased
Gold) worth ₹6,010.32 Lakh combined appeared in FY26 with zero FY25 balance — this is the
same GML/lease mechanism flagged for the raw-material reconciliation in Section B below.

---

## SECTION B — NEW FINDINGS (not reached by Pass 1)

### B1. 🔴 Raw material inventory (Note 7) does not reconcile against the Cost of Material Consumed roll-forward (Note 23) — a quantified, load-bearing gap for LBF1

Note 7 (Balance Sheet inventories) shows Raw Material closing ₹19,284.21 Lakh FY26 (up from
₹5,367.62 Lakh FY25, +259.3%). Note 23 (Cost of Material Consumed, PDF p.95-96, printed
p.185-186) independently rolls forward: Opening ₹5,367.62 Lakh (ties to Note 7's FY25
closing exactly) + Purchase ₹86,679.20 Lakh − Closing ₹**14,250.98** Lakh = Cost of Material
Consumed ₹77,795.84 Lakh (ties exactly to the P&L face). **Note 23's own implied FY26
raw-material closing balance (₹14,250.98 Lakh) is ₹5,033.23 Lakh LOWER than Note 7's FY26
raw-material closing balance (₹19,284.21 Lakh)** — two audited notes in the same financial
statements, describing the same balance-sheet line, disagree by ₹50.33 Cr. Both are
internally clean (each closes its own arithmetic exactly); the gap is between them, not
within either.

**[INFERENCE, clearly flagged as inference, not fact]**: the accounting policy for Gold
Metal Loan and Gold-on-Lease inventory (Note 2, Section 1 of Pass 1) states such gold "is
recognised as inventory with a corresponding liability at the prevailing gold price on the
date of receipt" — i.e., it enters inventory WITHOUT flowing through a conventional cash
"Purchase" line. Note 12 shows GML + Leased Gold liabilities grew from ₹0 (FY25) to
₹6,010.32 Lakh combined (FY26, see A10) — the same order of magnitude as the ₹5,033.23 Lakh
gap. It is plausible that a material share of the FY26 raw-material inventory increase is
GML/gold-lease stock recognised directly as inventory against a liability, bypassing Note
23's purchase-and-consumption tracking — which would mean Note 23's "Cost of Material
Consumed" UNDERSTATES the true gold throughput financed via GML/lease. This is not
confirmed from the Notes alone; it is the most important open question this pass raises for
LBF1 and should be put to management or cross-checked against the quarterly concall gram
data at stage 5/6, alongside the already-flagged gold-gram-versus-rupee-value question (Pass
1 rank 1).

### B2. 🟡 Note 18 "Other Current Liabilities" — customer scheme dues growing faster than revenue

Not examined by Pass 1. Customer Dues under Schemes/Advance ₹8,163.95 Lakh FY26 vs ₹6,239.30
Lakh FY25, **+30.8%**, above revenue growth of +22.2% (PDF p.94-95, printed p.184-185,
HIGH confidence clean table). This is the jewellery-sector gold-savings/instalment-scheme
liability (customers pre-pay toward a future purchase) — a normal industry float mechanism,
not inherently a red flag, but a growing liability the company owes customers in kind/value
that is worth tracking as part of working-capital and cash-conversion analysis (it is
effectively interest-free customer financing of future inventory sales). 🟢 not a red flag
on its own; flagged for completeness given its size (₹81.64 Cr, larger than total trade
payables' MSME component).

### B3. 🟡 Right-of-Use asset additions decelerated sharply even as PP&E additions accelerated

Note 4 (PDF p.91, printed p.176-177): ROU asset additions were ₹106.77 Lakh FY26 vs
₹1,124.34 Lakh FY25 — a **-90.5%** deceleration in new store-lease signings. Over the same
period, Note 3A PP&E gross additions rose to ₹1,863.30 Lakh FY26 from ₹1,502.85 Lakh FY25
(+24.0%), and Capital WIP shows ₹54.62 Lakh of new showroom capex was added and fully
absorbed in-year (Note 3B, no overdue projects). This pattern — capex up, new-lease signing
down — is consistent with FY26 store additions leaning toward owned/leasehold-improved space
rather than newly-leased premises, or with the pace of NEW leases slowing relative to the
prior year. Worth a direct cross-check against LBF3's store-count guidance (~6/year to 51 by
FY30) and the announcements-folder showroom openings (Dhar, Dahod, Jabalpur, Jodhpur) at
stage 5/6 — the Notes alone cannot resolve store count, only lease-liability additions.

### B4. 🟡 Note 3A PP&E — a quantified prior-year (FY25) inter-category regrouping, net-zero

The clean PP&E roll-forward (PDF p.90-91, printed p.174-175) shows an "Adjustment due to
Regrouping" row in the FY25 column only (both cost and depreciation): Building ₹0, Leasehold
Improvements +₹330.98 (cost), Plant & Machinery -₹314.90, Computer +₹18.21, Furniture &
Fittings -₹297.37, Office Equipment +₹263.08 — net zero across the Total column. This is a
specific, quantified instance of the generic "regrouped wherever necessary" boilerplate in
Note 33.7/33.22 (Pass 1 Section 12) — money moved BETWEEN PP&E sub-categories in FY25 with
no P&L or Total-PP&E effect. Not a current-year (FY26) item, and immaterial to valuation
since Total PP&E is unaffected; noted because Pass 3's pattern pass is instructed to look
for exactly this kind of reclassification.

### B5. 🟢 Capital commitments correction — Pass 1's "₹40.90 Lakh candidate" was the FY25 GST contingent-liability comparative, not a commitment

Pass 1 flagged a "candidate prior-year figure (₹40.90 Lakh)" adjacent to the nil Commitments
row as possibly a capital commitment. The clean Note 33.10 table (PDF p.101-102, printed
p.197-198) shows this is unrelated: "Disputed demand of VAT/Sales Tax Appeal/GST" reads
₹60.77 Lakh FY26 / **₹40.90 Lakh FY25** — the ₹40.90 Lakh is the prior-year contingent tax
dispute total (already captured in Pass 1's contingent-liabilities section), not a capital
commitment. **Capital commitments (Estimated amount of contracts remaining unexecuted on
capital account) are confirmed NIL both FY26 and FY25** (the "Commitments" row reads "-"/"-"
for both years). 🟢 minor correction, no valuation impact.

### B6. 🟢 Unutilised bank credit limits disclosed (liquidity headroom)

Note 33.2.2(B), PDF p.100, printed p.195, HIGH confidence, clean prose: "As of 31 March 2026
and 31 March 2025 the Company had unutilized credit limits from banks of ₹7,240.00 lacs and
₹7,874.04 lacs [respectively]." Headroom fell slightly (-8.1%) even as utilised borrowings
rose sharply — consistent with the company drawing down more of its sanctioned lines rather
than expanding them proportionally. Not examined by Pass 1.

### B7. 🟢 Financial-instruments fair-value hierarchy tables — fully clean, no Level 3 exposure

Note 33.2.1 (PDF p.99-100, printed p.192-195) is now fully legible both years: all financial
assets/liabilities are Amortised Cost/Level 2 (borrowings, trade payables) with no Level 3
(unobservable-input) instrument at material balance either year. Confirms Pass 1's
directional read at HIGH rather than MODERATE confidence; no new concern.

---

## UPDATED LOAD-BEARING-FACT STATUS AFTER PASS 2

- **LBF1 (margin source)**: unchanged direction from Pass 1 (bearish-leaning: gold grams flat
  while rupee value grew; MCX hedging gain of ₹18.60 Cr sits inside revenue), PLUS a new,
  independently-derived open question (B1): up to ~₹50 Cr of FY26 raw-material inventory
  growth may be GML/gold-lease stock recognised without flowing through the normal purchase
  cycle — sharpens, does not resolve, the "price appreciation vs real volume" question.
  Quarterly gram data remains outside AR scope (stage 5/6).
- **LBF2 (cash conversion)**: NOW FULLY CONFIRMED FROM THE AR. CFO = -₹97.31 Cr FY26 (exact
  match to B00's citation). Inventory +39.0% to ₹1,003.94 Cr; payables FELL 35.7% to ₹113.61
  Cr in the same year (A2, a finding Pass 1 did not have at all); borrowings +76.8% to
  ₹290.91 Cr (Note 33.3, already HIGH in Pass 1). Growth-induced classification is now
  strongly supported: financing activities (+₹121.42 Cr, almost entirely fresh bank
  borrowing) funded the operating cash gap; there is no structural red flag distinct from
  the leverage build itself.
- **LBF3 (guidance vs delivery)**: still not directly addressable from Notes; B3's
  ROU-addition deceleration is a new data point for the store-count cross-check at stage 5/6.
- **LBF4 (promoter/related parties)**: **materially revised**. Related-party unsecured
  borrowings FELL 34.5% (not +356% as Pass 1 reported, A1) — the promoter-family loan book
  shrank in the same year total debt rose; the debt build is 100% bank-sourced. Per-party RPT
  figures are now HIGH confidence (A8) with two misattributions corrected. Personal-guarantee
  and pledged-property findings (Pass 1 Section 7) are unchanged and remain a legitimate
  watch item independent of this correction.

---

## PASS 2 NEW FINDINGS SUMMARY

Pass 2 is not empty. It resolves every Pass 1 extraction-defect item (the corrected
table-mode text closes all of them at HIGH confidence) and, in doing so, **reverses one
Pass 1 top-10 finding (related-party borrowings, A1)**, **corrects one mislabelled figure**
(Employee Benefits Expense, A3), **corrects two RPT misattributions** (A8), and adds **seven
new findings** not reached in Pass 1, the most significant being the raw-material
Note-7-vs-Note-23 reconciliation gap (B1, 🔴) and the trade-payables paydown that sharpens
the LBF2 cash-conversion story (A2, folded into that section but new to this pass). The
systemic extraction-defect flag that was Pass 1's own rank-4 finding is now CLOSED: no
material table in Notes 1-33.26 remains unreliable. Pass 3 (pattern pass) should treat this
report, not Pass 1's, as the reliable baseline for cross-note contradictions, and should
give first attention to the B1 raw-material gap and to whether Note 20's non-retail revenue
decline connects to anything else in the corpus.

**End of Pass 2.** Pass 3 (pattern pass + consolidation) proceeds as a separate call against
Pass 1 + Pass 2 combined.
