# GSM FOILS LIMITED — STAGE 2 NOTES TO FINANCIAL STATEMENTS — PASS 1 (FULL EXTRACTION)
Run: gsmfoils-2026-07-24 | Source: Annual Report FY25 (year ended 31-Mar-2025), 113pp text extract
All figures converted from the source's ₹ Lakhs to ₹ Crores (÷100) per house convention; source figure in Lakhs
shown in parentheses on first use of each note. Company reports under Indian GAAP (AS), NOT Ind AS — it is an
SME-platform listed company (NSE Emerge), 2nd annual report, converted from GSM Foils LLP to GSM Foils Limited
in FY24.

## EXTRACTION-QUALITY CAVEAT (read before the findings below)
A large part of "Note 1 — Notes forming part of the financial statements" (accounting policies, related-party
disclosures, forex earnings/outgo, the Schedule III mandatory ratio table, and the Part IV balance sheet
abstract) was rendered in the source PDF using an embedded font whose character codes do not map to standard
Unicode. Narrative text was recoverable via a consistent Caesar-shift decode (+29 on ASCII code point, verified
against multiple decoded phrases matching known headings e.g. "Related Party Transactions", "Ensuring...").
However, wherever an actual NUMBER sat inside that same font (the RPT remuneration table's rupee columns, the
forex earnings/outgo table, the CIF import value, the full Schedule-III ratio-disclosure table with variances),
the digits did not survive extraction and appear as blank cells in the source text. The original PDF could not
be re-rendered as an image in this environment (pdftoppm unavailable) to visually recover them. These specific
cells are marked NOT FOUND IN DOCUMENT (extraction failure) below, distinct from items genuinely absent from
the filing. A small second table (Annexure I / Form AOC-2, p.45 of report, and Annexure II remuneration ratios,
p.46-47) used a DIFFERENT substitute-glyph font (Greek/Coptic numeral look-alikes) that WAS decodable digit by
digit (cross-checked: AOC-2's two KMP remuneration lines of ₹47.00 lakh + ₹43.00 lakh sum exactly to the ₹90.00
lakh "Directors Salary" figure in Note 5.2 — internally consistent, treated as reliable).

═══════════════════════════════════════════════════════════
NOTE-BY-NOTE EXTRACTION
═══════════════════════════════════════════════════════════

## Note 1.0 — Significant Accounting Policies and Notes on Accounts (p.75-84 and duplicated in fuller form p.96-110)
🟡 **Basis of preparation**: Indian GAAP (AS), NOT Ind AS, historical cost, accrual, going concern (Note 1,
p.78/p.99, decoded). This is a small SME-platform company so IGAAP is permitted; but it means no Ind AS 116
lease/ROU disclosure, no ECL matrix, no fair-value hierarchy — several of this pipeline's standard extraction
asks (points 1, 6, 9) are structurally NOT APPLICABLE rather than omitted.
🟡 **Revenue recognition policy is stale/boilerplate**: "Sales include excise duty but exclude sales tax and
value added tax" (Note 1, p.78/p.99, decoded) — excise duty was abolished with GST in July 2017. The company's
own revenue recognition policy note has not been updated for the GST regime in eight years of drafting. No
mention of GST treatment at all. Minor disclosure-diligence flag, not a valuation issue, but signals the
policy note is copy-pasted rather than tailored.
🟢 **Depreciation**: WDV method per Schedule II useful lives, "consistent with those specified under the Act"
(p.78/99). No explicit useful-life table or capitalisation threshold disclosed — NOT FOUND IN DOCUMENT.
🔴 **No impairment testing disclosure**: Impairment policy is boilerplate (value-in-use, pre-tax discount rate)
but NO actual impairment assessment, growth-rate or discount-rate assumption is disclosed for FY25 — not
unusual given the company has no goodwill/intangibles (Note 3.4 = nil both years) but worth noting for
completeness.
⚪ NOT APPLICABLE: Ind AS 116 ROU/lease liability (IGAAP company, operating leases expensed — "FACTORY RENT
EXP." ₹0.51 Cr FY25 / ₹0.31 Cr FY24 per Note 5.5, p.94) — no lease liability on balance sheet.
⚪ NOT APPLICABLE: ECL matrix (IGAAP, no Ind AS 109 ECL model used) — receivables carried at "unsecured,
considered good", no provisioning policy for doubtful debts disclosed. Given receivables trend below (Finding
#1), the ABSENCE of any bad-debt/ECL provisioning policy alongside a 4.7x YoY receivables jump is itself a
flag — see Note 4.3.
🟡 **First-time standard adoption / conversion accounting**: Company converted from GSM Foils LLP to GSM Foils
Limited during FY24 (previous year); "all assets, liabilities, contracts and obligations of the LLP were
transferred to GSM Foils Limited at the time of conversion" (Note 1, p.78/99, decoded). FY24 is therefore the
first full year as a company; FY23 comparatives for the LLP period are not restated/shown — standard for a
conversion, but means only 2 years of comparable P&L exist (as flagged in this run's brief).
🔴 **Unresolved legacy tax liability via directors' personal accounts** (Note 1, "Additional Regulatory
Information", p.108, decoded): "the income tax liability of GSM Foils LLP was settled from the account of the
LLP which is later merged to the newly incorporated company GSM Foils Limited. As informed to us, the said
transaction will be settled in the current financial year by the directors of GSM Foils Limited, who were
previously partners in GSM Foils LLP, through their personal accounts. The necessary adjustments will be made
accordingly in the books of account." This is a live, unquantified, unsettled related-party fund flow through
promoter-director personal accounts, carried over from the pre-IPO LLP structure and still open as of the FY25
signing date (08-May-2025). Amount: NOT FOUND IN DOCUMENT. This is a governance flag worth monitoring to
resolution.
🟢 **Other remarks** (Note 1, p.80/103, decoded): company states it has "generally been regular in depositing
undisputed statutory dues" and made "certain reclassifications and regroupings of accounts... without any
impact on the overall financial position or performance" in the current period — presentation-only
reclassification, no quantified P&L impact disclosed (cross-check: director remuneration DID move categories
between years — see Note 5.2/5.5 below — which is the kind of reclassification this remark likely covers).

## Note 2.1 — Share Capital (p.83, clean text)
🟢 Authorised: ₹18.00 Cr (1,80,00,000 shares × ₹10 par), unchanged YoY.
🟢 Paid-up: ₹12.81 Cr (1,28,11,649 shares) at 31-Mar-25 vs ₹9.37 Cr (93,71,649 shares) at 31-Mar-24 — the
increase of 34,40,000 shares is the IPO fresh issue, allotted 29-May-2024 at ₹32/share (Directors' Report,
p.32, clean text — cross-checked against Note 2.1/2.2 math below).
🟡 **Promoter shareholding diluted materially post-IPO**: Mohansingh Parmar 52.31% → 38.27% (-14.04pp); Sagar
Bhanushali 47.67% → 34.87% (-12.79pp) (Note 2.1, p.83). Combined promoter holding fell from 100.0% to 73.1% of
expanded capital. Expected mechanically from the IPO (new public shares diluted %, not a sale by promoters —
no promoter share sale disclosed) but the magnitude (>26pp combined dilution in one IPO) is worth noting for
any lock-in/promoter-commitment analysis.
🟢 No ESOP scheme, no differential voting rights, no bonus/rights issue completed in FY25 (rights issue was
only board-approved post year-end — see subsequent events below).

## Note 2.2 — Reserves and Surplus (p.84, clean text)
🟢 Securities premium: opening ₹0.29 Cr, IPO addition ₹7.57 Cr, less IPO-expense write-off ₹0.45 Cr, closing
₹7.41 Cr. Prior year had a bonus-share adjustment of ₹(8.96) Cr against securities premium (FY24, pre-IPO
capital restructuring).
🔴 **IPO expenses split across two accounting treatments** (Notes 2.2 + 5.3, p.84 & p.93, clean text): ₹0.45 Cr
written off directly against Securities Premium (bypasses P&L, Note 2.2) while a separate ₹0.09 Cr "IPO
EXPENSES" line sits inside Finance Costs in the P&L (Note 5.3, p.93). Total IPO cost ≈ ₹0.54 Cr against ₹11.01
Cr gross proceeds (≈4.9%, plausible for an SME IPO) but the split treatment of what should be one homogeneous
cost category, with no policy note explaining the split, is an accounting-quality observation (point 12: direct
credits/debits to reserves bypassing P&L).
🟢 P&L reserve: opening ₹1.37 Cr, FY25 profit transferred ₹9.65 Cr, closing ₹11.02 Cr. Total Reserves &
Surplus ₹18.43 Cr (FY25) vs ₹1.66 Cr (FY24) — entirely organic (IPO premium + retained profit), no revaluation
reserve, no other comprehensive income line (IGAAP, none expected).

## Note 2.3 / 2.4 — Share warrants / share application money pending: NIL both years. 🟢

## Note 2.5 — Long-Term Borrowings (p.84-85, clean text)
🟢 FY25: **NIL** long-term borrowings (fully reclassified to current maturities, Note 2.9). FY24: ₹0.91 Cr,
comprising Aditya Birla Finance ₹0.35 Cr, Bajaj Finance Business Loan ₹0.28 Cr, L&T Finance-SME ₹0.23 Cr, and
**two unsecured director loans**: Mohansingh Parmar ₹0.01 Cr and Sagar Bhanushali ₹0.04 Cr.
🟡 **Related-party loans repaid to nil in FY25**: the two promoter-director loans (Mohansingh Parmar ₹1.03
lakh, Sagar Bhanushali ₹4.38 lakh, FY24) are fully repaid/nil at FY25 (Note 2.5, cross-checked against Note 2.9
FY25 column showing no director-loan line). No interest rate/tenure disclosed for these loans (NOT FOUND IN
DOCUMENT) — standard omission risk for related-party loans, though the amounts are immaterial (<₹5 lakh each).

## Note 2.6 — Deferred Tax Liabilities (net) (p.85, clean text)
🟢 FY25 ₹0.014 Cr, FY24 ₹0.0035 Cr — solely a depreciation timing difference. Immaterial. No effective-vs-
statutory tax rate reconciliation is disclosed anywhere in the document (point 10 of the extraction brief) —
NOT FOUND IN DOCUMENT, though under IGAAP/AS-22 this level of reconciliation disclosure is not mandatory for a
company this size, so this is a low-severity gap. Computed effective tax rate (author calculation from Notes
4.7 P&L figures, not company-disclosed): FY25 = ₹3.98 Cr tax / ₹13.63 Cr PBT = 29.2%; FY24 = ₹0.48 Cr / ₹1.85
Cr = 26.2%. No MAT credit entitlement recognised either year (Note 2.6 shows no MAT credit asset line).

## Note 2.7 / 2.8 — Other long-term liabilities / long-term provisions: NIL both years. 🟢 No employee benefit
(gratuity/leave encashment) provision is recognised in either year despite 31 permanent employees on roll
(Annexure II, p.46, clean text) and "Compensated absences" being named in the Employee Benefits accounting
policy (Note 1, p.79/100, decoded). NOT FOUND IN DOCUMENT — no actuarial valuation, no funded-status table, no
gratuity provision anywhere in the balance sheet or provisions notes. 🟡 Watch: this could mean the company is
below AS-15's short-service-cost threshold, or it could mean gratuity liability is simply unprovided/unfunded —
document does not clarify which, and Payment of Gratuity Act coverage would normally apply once ≥10 employees
with ≥5 years continuous service exists, plausible for a company only in its 2nd year of corporate existence
(and formerly an LLP) — flag as a question for management rather than a confirmed gap.

## Note 2.9 — Short-Term Borrowings (p.85, clean text)
🔴 **Short-term borrowings up 295% YoY**: ₹17.82 Cr (FY25) vs ₹4.51 Cr (FY24). Composition FY25: DBS Bank
working-capital CC/OD ₹13.34 Cr (secured — CARO Annexure A confirms DBS sanctioned >₹5 Cr against current-asset
security, p.69, decoded) + current maturities of long-term debt ₹4.48 Cr (Aditya Birla Finance ₹0.18 Cr, Bajaj
Finance ₹0.11 Cr, L&T Finance-SME ₹0.11 Cr, Tata Capital ₹4.07 Cr — a large new Tata Capital facility appears
in FY25 with no FY24 balance). FY24 composition: Bank of India CC ~nil / DBS ₹4.24 Cr + smaller current
maturities (SMC Finance, DigiCredit Urgo, HDFC, ICICI, Axis — all repaid/nil by FY25). This is the funding
source for the receivables and inventory build discussed under Note 4.3/4.2 below — flagged together as the
single most important finding of this pass.

## Note 3.0 — Trade Payables (ageing) (p.86, clean text)
🟡 **Zero MSME dues disclosed in either year** (both FY25 and FY24, all four ageing buckets and both "MSME"
rows show ₹0.00). Total payables ₹7.36 Cr (FY25) / ₹2.62 Cr (FY24), 100% classified under "Others" (non-MSME).
For a mid-size aluminium-foil manufacturer sourcing raw material and packaging services in India, zero MSME
supplier exposure across two consecutive years is unusual and typically indicates either (a) all suppliers are
large/organised-sector, plausible given aluminium foil stock is a commodity-grade input usually sourced from
large rolling mills, or (b) MSME registration status of vendors was not obtained/verified. No boilerplate
MSMED-Act interest disclosure ("no interest paid/payable to any MSME supplier") appears anywhere in the
document, which is itself slightly unusual since most Indian companies include this standard note even when
the answer is nil. Rated Watch rather than Red because payable magnitude is genuinely small and commodity input
sourcing from large mills is plausible.
🟢 Ageing: FY25 — <1yr ₹7.11 Cr, 1-2yr ₹0.26 Cr, no dues >2yr, no disputed dues. FY24 — <1yr ₹2.62 Cr entirely,
no aged balances. Payable days (author calculation, Cost of Materials Consumed as proxy denominator): FY25 =
23.2 days; FY24 = 26.9 days — improving/stable, not a red flag on its own.

## Note 3.1 — Other Current Liabilities (p.86, clean text)
🟢 FY25 ₹0.36 Cr (expenses payable ₹0.21 Cr + advance from customer ₹0.15 Cr) vs FY24 ₹0.16 Cr. Advance from
customer is new in FY25 (nil FY24) — consistent with revenue scale-up, not a concern.

## Note 3.2 — Short-Term Provisions (p.86, clean text)
🟢 FY25 ₹4.60 Cr (income tax ₹3.97 Cr + GST payable ₹0.44 Cr + TDS ₹0.19 Cr + ESIC/PF ~nil) vs FY24 ₹0.73 Cr.
Scales with profit growth, no anomalies.

## Note 3.3 — Property, Plant & Equipment (p.87, clean text)
🟢 Gross block: ₹1.33 Cr (FY24) → ₹2.90 Cr (FY25), i.e. Plant & Machinery additions of ₹1.52 Cr in FY25 (vs
₹0.02 Cr in FY24) — nearly tripling gross P&M block, consistent with Directors' Report statement that IPO
proceeds funded "capital expenditure for plant and machinery" (p.69/72, decoded, CARO Annexure A). Net block
₹2.12 Cr (FY25) vs ₹0.84 Cr (FY24). Depreciation charge ₹0.28 Cr (FY25) vs ₹0.13 Cr (FY24), WDV method. No
revaluation in either year (confirmed explicitly, CARO Annexure A clause (i)(d), p.68, decoded, and Additional
Regulatory Info, p.107, decoded — both state PPE has not been revalued). No impairment recognised. 🟢 Clean —
capex is real, traceable to fresh capital raised, and depreciation scales sensibly with the asset base.

## Note 3.4 — Intangible Assets: NIL both years (gross, accumulated amortisation, and net all zero). 🟢 No
goodwill on the balance sheet — company has no subsidiaries/associates/JVs (Directors' Report, p.39, clean
text, confirms explicitly: "During the year under review, the Company does not have any Subsidiaries" / "does
not have any Associate or Joint Venture"). Point 6 of the extraction brief (subsidiaries/JVs with ownership %,
loss-making subsidiaries, ICDs given) is therefore NOT APPLICABLE.

## Note 3.5 / 3.6 — CWIP / Intangibles under development: NIL both years. 🟢

## Note 3.7 — Non-Current Investments (p.89, clean text)
🟢 FY25 ₹2.99 Cr in a Fixed Deposit (new — nil FY24). No purpose stated but almost certainly a lien/margin FD
against the DBS working-capital facility (standard practice; CARO confirms borrowings are secured against
current assets, and separately banks commonly require FD margin for CC/OD limits) — NOT FOUND IN DOCUMENT
explicitly, inferred, flagged as inference not fact.

## Note 3.9 / 4.0 — Long-term loans & advances (nil both years) / Other non-current assets (p.89, clean text)
🟢 Other non-current assets FY25 ₹0.23 Cr — a new security deposit (nil FY24), consistent with the new leased
factory/premises scale-up implied by the PPE additions.

## Note 4.1 — Current Investments: NIL both years. 🟢

## Note 4.2 — Inventories (p.89-90, clean text)
🟡 Total inventory ₹18.86 Cr (FY25) vs ₹10.23 Cr (FY24), +84.3% YoY vs revenue growth of +227.7% — inventory
growing SLOWER than revenue, a genuinely healthy signal on its face. Split: Raw material ₹7.25 Cr (FY25) vs
₹2.60 Cr (FY24), +178.2%, roughly tracking the +215.9% growth in cost of materials consumed (COGS ₹115.86 Cr
vs ₹35.57 Cr) — sensible. Finished goods ₹11.61 Cr (FY25) vs ₹7.63 Cr (FY24), +52.2% — growing well below
revenue, i.e. finished-goods turnover improved. Inventory days (author calculation vs COGS): FY25 = 59.4 days;
FY24 = 105.0 days — a meaningful improvement. No write-downs, no obsolete-inventory disclosure, no NRV
adjustment disclosed (NOT FOUND IN DOCUMENT — but inventory policy states lower-of-cost-or-NRV is applied, so
absence of a write-down note is consistent with no NRV issues rather than a gap). Rated Watch only because
inventory data quality (no ageing/category granularity beyond raw material vs finished goods) is thin, not
because the trend itself is concerning.

## Note 4.3 — Trade Receivables (p.90, clean text) — ⭐ TOP FINDING OF THIS PASS
🔴 **Receivables grew 4.67x while revenue grew 3.28x — debtor days worsened from ~65 to ~92 in one year.**
Trade receivables: ₹33.77 Cr (FY25) vs ₹7.23 Cr (FY24), +366.7% YoY. Revenue from operations grew +227.7% over
the same period (₹133.80 Cr vs ₹40.83 Cr, Note 4.7). Receivables as % of revenue: 25.2% (FY25) vs 17.7% (FY24).
Debtor days (author calculation): FY25 = (33.77/133.80)×365 = 92.1 days; FY24 = (7.23/40.83)×365 = 64.6 days —
a ~28-day deterioration. The ageing disclosure itself is thin: only two buckets given ("within six months" ₹
33.60 Cr / "exceeding six months" ₹0.17 Cr for FY25; ₹7.12 Cr / ₹0.11 Cr for FY24) rather than the fuller 0-6m /
6m-1y / 1-2y / 2-3y / >3y schedule that Schedule III companies typically present — a disclosure-granularity gap
(point 4 of the brief). No ECL/doubtful-debt provision exists against this balance (IGAAP, "unsecured,
considered good" throughout, no provisioning policy disclosed at all — see Note 1 above). No single-customer
concentration % is disclosed anywhere in the document (point 4 / point 11 both ask for this) — NOT FOUND IN
DOCUMENT. This receivables build is funded by the 295% surge in short-term borrowings (Note 2.9) and coincides
with cash and cash equivalents actually FALLING (₹0.24 Cr FY25 vs ₹0.40 Cr FY24, Note 4.4) despite profit
almost 7x-ing — i.e. profit is not converting to cash; working capital absorbed essentially all of it plus new
debt. This is exactly the pattern FLAG-CASH is designed to catch. No related-party receivables are separately
disclosed (would be NOT FOUND if any existed as a distinct line — none shown).

## Note 4.4 — Cash and Cash Equivalents (p.90, clean text)
🔴 Cash fell to ₹0.24 Cr (FY25) from ₹0.40 Cr (FY24) despite revenue +227.7% and PAT growing from ₹1.37 Cr to
₹9.65 Cr — see Note 4.3 discussion; cash in hand actually rose slightly (₹0.19→₹0.19 Cr, roughly flat) while
bank balances fell (₹0.20 Cr → ₹0.05 Cr). Company is running on a very thin cash buffer relative to its now
much larger revenue base, offset partly by the new ₹2.99 Cr FD (Note 3.7) which is presumably lien-marked
against borrowings rather than freely available liquidity.

## Note 4.5 — Short-Term Loans & Advances (p.90, clean text)
🟢 FY25 ₹0.38 Cr (loans & advances ₹0.10 Cr, prepaid insurance ₹0.05 Cr, prepaid interest ₹0.14 Cr, TDS ₹0.09
Cr) vs FY24 ₹0.86 Cr (nearly all "loans & advances to others" — composition NOT FOUND IN DOCUMENT for FY24
beyond the single aggregate line). No related-party loans/advances disclosed in this note.

## Note 4.6 — Other Current Assets (p.90, clean text)
🟡 FY25 ₹2.81 Cr, entirely "Advance to Supplier" (new — nil FY24). FY24 ₹0.41 Cr was deposits (₹0.21 Cr) +
advance tax (₹0.20 Cr). A ₹2.81 Cr supplier advance appearing from nothing is a meaningful new working-capital
line — no explanation of which supplier(s) or why advances (rather than normal credit terms) were needed is
given. Combined with the receivables build (Note 4.3) and the new short-term debt (Note 2.9), this reinforces
the working-capital deterioration picture, though a large raw-material supplier advance ahead of a capacity
ramp-up is also a plausible, benign explanation. NOT FOUND IN DOCUMENT: counterparty identity, whether related
party.

## Note 4.7 — Revenue from Operations (p.92, clean text)
🟢 ₹133.80 Cr (FY25) vs ₹40.83 Cr (FY24), single undifferentiated line "SALES A/C" — **no product-wise,
segment-wise, or geography-wise disaggregation is disclosed** (point 11 of the brief) despite the "About
Company" section describing multiple product variants (blister foils, strip foils, Alu-Alu foils, 0.020-0.040
micron range) and the CARO report separately disclosing exports exist (see forex section below). No contract
assets/liabilities, no unsatisfied performance obligations, no top-customer revenue %. All NOT FOUND IN
DOCUMENT — a real disclosure gap for an investor trying to assess revenue mix/customer concentration risk,
though again this is IGAAP not Ind AS 115, so full disaggregation is not mandatory the way it would be for a
larger Ind AS filer.

## Note 4.8 — Other Income (p.92, clean text)
🟢 FY25 ₹0.02 Cr (FD interest) vs FY24 ₹0.00. Immaterial, non-recurring in nature (grows with the new FD), no
quality-of-earnings concern (other income is <0.02% of PBT).

## Note 4.9 — Cost of Materials Consumed (p.92, clean text)
🟢 FY25 ₹115.86 Cr vs FY24 ₹35.57 Cr, +225.8% — tracks revenue growth (+227.7%) almost exactly; raw material
cost as % of revenue: 86.6% (FY25) vs 87.1% (FY24) — stable, gross margin on materials essentially flat. No
red flags; single "RAW MATERIALS" line, no further break-down by input type (aluminium foil stock, coating
chemicals etc. not separately disclosed) — NOT FOUND IN DOCUMENT at that granularity.

## Note 5.0 — Purchases of Stock-in-Trade: NIL both years. 🟢 (Manufacturer, not trader — consistent.)

## Note 5.1 — Changes in Inventories (p.92-93, clean text)
🟢 (₹3.98 Cr) FY25 vs (₹2.50 Cr) FY24 — increase in finished-goods stock reduced reported expense/boosted
profit in both years, standard mechanical effect of inventory build, not unusual given growth phase. Cross-
checked and consistent with Note 4.2 finished-goods movement.

## Note 5.2 — Employee Benefits Expense (p.93, clean text)
🔴 **Director remuneration reclassified between expense categories year over year** — a genuine presentation-
consistency flag. FY25: "Salary to staff" ₹1.67 Cr + "Directors Salary etc" ₹0.90 Cr = ₹2.57 Cr total employee
benefits expense. FY24: "Salary to staff" ₹0.98 Cr, and Directors Salary shows ₹0.00 in THIS note — because in
FY24 director remuneration of ₹0.19 Cr was instead booked under Note 5.5 Other Expenses → "Managerial
Remuneration: Salary To Director". In other words, the FY24 comparative in Note 5.2 (Employee Benefits) is NOT
like-for-like with FY25: total combined director remuneration was actually ₹0.19 Cr (FY24) vs ₹0.90 Cr (FY25)
— a genuine +373.7% increase in KMP pay in the IPO year, but the increase is understated if an investor reads
only Note 5.2's YoY comparison in isolation, since the FY24 figure sitting in Note 5.2 (₹0.00) is not the true
prior-year comparable. Cross-checked against Note 5.5 (below) and AOC-2 Annexure I (₹0.47 Cr + ₹0.43 Cr = ₹0.90
Cr for the two executive directors, approved 23-Apr-2024) and Annexure II (79.79% and 77.91% remuneration
increases disclosed for the Chairman/WTD and MD respectively, p.47, clean text) — all three sources are
internally consistent on the ₹0.90 Cr FY25 total, so the underlying number is reliable; only the note
presentation obscures the YoY comparison.
🟢 32.6% of total employee cost is director remuneration in FY25 (₹0.90 Cr / ₹2.57 Cr) — high but not unusual
for a small, founder-run company with 31 employees.

## Note 5.3 — Finance Costs (p.93, clean text)
🟡 FY25 ₹1.31 Cr vs FY24 ₹0.72 Cr, +84.6%, below the growth in short-term borrowings (+295%, Note 2.9) —
plausible given the borrowing build was back-loaded through the year and CC/OD interest is drawn-balance based
not peak-balance based. Composition: term loan interest ₹0.29 Cr, CC/OD interest ₹0.50 Cr (new in FY25, nil
FY24 — confirms CC/OD facility was drawn for the first time this year), bank charges ₹0.40 Cr (large jump,
processing fees likely tied to the new Tata Capital facility, Note 2.9), interest on income tax/TDS ₹0.05 Cr,
and the previously-flagged IPO expense ₹0.09 Cr (see Note 2.2 discussion — questionable classification as a
finance cost rather than a capital-raising cost against securities premium).

## Note 5.4 — Depreciation & Amortisation: ₹0.28 Cr (FY25) vs ₹0.13 Cr (FY24). 🟢 Ties to Note 3.3 PPE
schedule exactly, no separate amortisation (no intangibles).

## Note 5.5 — Other Expenses (p.93-94, clean text)
🟢 FY25 ₹4.15 Cr vs FY24 ₹4.08 Cr — nearly flat despite revenue +227.7%, i.e. strong operating leverage on this
line (other expenses fell from 10.0% of revenue to 3.1% of revenue). Composition shifted materially: power/fuel
up (₹0.52+₹0.99=₹1.51 Cr FY25 vs ₹0.24+₹0.37=₹0.61 Cr FY24, scaling with higher production volume), freight
down (₹0.55+₹0.04=₹0.59 Cr FY25 vs ₹1.38+₹0.04+₹0.41=₹1.82 Cr FY24 — freight fell in absolute terms despite
revenue tripling, a genuinely favourable and slightly surprising trend worth a management question), a new
₹0.16 Cr commission-paid line (nil FY24, sales-linked, consistent with a bigger customer base), consultancy
fees ₹0.36 Cr (new, IPO/listing related likely), listing expenses ₹0.01 Cr, and the previously-noted stamp
duty for loan ₹0.17 Cr (new — ties to the new borrowing facilities in Note 2.9). "Managerial Remuneration:
Salary to Director" line is ₹0.00 FY25 / ₹0.19 Cr FY24 — this is the reclassified item discussed under Note 5.2
above. Auditor remuneration: ₹0.01 Cr FY25 (audit fees only) vs ₹0.0019 Cr FY24 — immaterial in both years but
first year an actual audit fee is separately shown (auditors were reappointed as a new, peer-reviewed firm in
FY25 per CARO Annexure A clause (xviii), decoded — "previously appointed firm was non-peer reviewed").

## Note 5.6 / 5.7 / 5.8 — Exceptional / Extraordinary / Prior Period items: NIL both years. 🟢 No one-time or
non-recurring items disguised as ordinary operating items were identified in the P&L breakdown (Note 5.5) other
than the IPO-related costs already discussed, which ARE clearly one-time in nature (IPO expenses, stamp duty
for new loan, consultancy fees) but are NOT separately called out as "exceptional" — they are buried in ordinary
Other Expenses / Finance Costs. This means FY25's reported PBT of ₹13.63 Cr is depressed by roughly ₹0.7-0.8 Cr
of one-time IPO/listing-related costs (IPO expense ₹0.09 Cr + stamp duty for loan ₹0.17 Cr + consultancy fees
₹0.36 Cr + listing exp ₹0.01 Cr ≈ ₹0.63 Cr, author aggregation from Note 5.3/5.5 line items, not a company-
labelled "exceptional items" figure) — i.e. normalised PBT for FY25 run-rate purposes would be modestly HIGHER
than reported, the opposite direction of typical earnings-management concern, so this is a neutral-to-positive
quality observation, not a red flag.

## Note 5.9 — Tax Expense (p.95, clean text)
🟢 Current tax ₹3.97 Cr + deferred tax ₹0.01 Cr = ₹3.98 Cr (FY25) vs ₹0.48 Cr (FY24). Ties to P&L and Note 3.2
provision balance. See Note 2.6 above for effective-rate calculation (29.2% FY25).

## Note 6.0 — Discontinued operations: NIL. 🟢

## Note 6.2 — EPS (p.95, clean text)
🟢 Basic = Diluted = ₹7.53 (FY25) vs ₹1.46 (FY24), +415.8%. No dilutive instruments (no ESOP, no warrants, no
convertibles) so basic = diluted in both years — clean, no dilution-gap concern (point 12 of the brief, not
applicable here). Weighted-average share count is not separately disclosed (NOT FOUND IN DOCUMENT) — EPS was
presumably computed on a weighted-average basis given the mid-year IPO allotment (29-May-2024), but the
document does not show the reconciliation.

## Part IV — Balance Sheet Abstract & Company's General Business Profile (p.96-97, decoded, numbers not
recoverable — see extraction-quality caveat). This is a standard Schedule VI-legacy filing requirement;
content duplicates the Balance Sheet already captured above. No new information.

## "Other Disclosures" — Related Party Transactions (p.104, decoded text; rupee figures per-row NOT recoverable
except where cross-checked against AOC-2/Note 5.2/2.5 above)
🔴 **Related party list** (p.104, decoded): Sagar Bhanushali (KMP — Chairman & WTD & CFO), Mohansingh Parmar
(KMP — MD), Mahesh V. Mehta / Vijay V. Pandya / Swati D. Mirani (Non-Executive Independent Directors), **Sanjiya
Metal Corporation — "KMP is Proprietor"** (i.e. a proprietorship owned by one of the KMPs is a disclosed related
party), and Pratik Makwana (Company Secretary). The nature and value of transactions with Sanjiya Metal
Corporation specifically are NOT FOUND IN DOCUMENT (numeric extraction failure, see caveat) — given the company
name ("Metal Corporation") and GSM Foils' raw-material input being aluminium, this related party could plausibly
be a raw-material supplier or trading counterparty, which would be a materially more significant RPT than KMP
remuneration if so. This is flagged as the single most important unresolved item from this pass and should be
verified against the source PDF pages ~107-108 (report pagination) / re-extraction with OCR, since related-party
sourcing arrangements in a promoter-controlled small-cap are a standard governance risk vector.
🟢 Executive director remuneration table structure confirmed (Sagar Bhanushali, Mohansingh Parmar, Pratik
Makwana rows) but individual salary/bonus/PF/perquisite column splits are NOT FOUND IN DOCUMENT (extraction
failure) — totals reliably cross-checked via Note 5.2 + AOC-2 as ₹0.90 Cr combined (see Note 5.2 above).
🟢 Director loan table (p.104) structurally confirms the same two related-party loans already captured cleanly
in Note 2.5 (Sagar Bhanushali, Mohansingh Parmar) — no new information, both nil at FY25.
🟢 **AOC-2 (Annexure I, p.45 of report, Greek-glyph-decoded)**: Section 1 (transactions NOT at arm's length) =
Nil. Section 2 (material contracts at arm's length) lists three rows, all "Remuneration", all approved by the
Board on 23-Apr-2024: ₹47.00 lakh, ₹43.00 lakh, ₹5.40 lakh. First two rows sum exactly to the ₹90.00 lakh
KMP remuneration total (Note 5.2) and are almost certainly Sagar Bhanushali and Mohansingh Parmar respectively.
The third row (₹5.40 lakh) does not reconcile to any other disclosed figure — its recipient could be a third
KMP role (e.g. Sagar Bhanushali's separate CFO capacity) or the Company Secretary; Directors' Report Annexure II
states no salary was paid to CS Pratik Makwana yet shows a non-nil remuneration ratio (2.02) for him — an
internal inconsistency in the document that could not be resolved from available text. Flagged as a question
for management. Directors' Report AOC-2 covering note (p.42, clean text) states "All Related Party Transactions
entered into during the financial year were on an Arm's Length basis and in the Ordinary Course of Business."

## Foreign Currency / Forex Earnings & Expenditure (p.105-106, decoded; amounts NOT recoverable — extraction
failure per caveat)
🟡 Company confirms it has foreign exchange earnings (exports) and foreign exchange outgo (raw material
imports) in both FY25 and FY24 (narrative confirmed: "the Company has reported foreign exchange earnings of
Rs. [X] Million... foreign exchange outgo on account of import of raw materials amounted to Rs. [X] Million")
but every actual number in this section — forex earnings, forex outgo, professional/consultant fees in forex,
royalty in forex, stock-in-trade imports, CIF value of imports — is NOT FOUND IN DOCUMENT (extraction failure).
A "Royalty" line item is listed in the Expenditure in Foreign Currency table structure (p.105) — worth flagging
that a royalty payment in foreign currency is contemplated/disclosed as a category even though FY25's actual
amount could not be recovered; if non-nil and paid to a foreign related party this would be a related-party
item not otherwise captured in the RPT list above (the RPT list, p.104, shows only domestic individuals/entity —
no foreign related party named). This inconsistency (a "Royalty" expenditure category disclosed in forex note,
but no foreign related party in the RPT list) could not be resolved and is flagged as a question for
management / re-verification item.
⚪ Derivatives/commodity hedging: policy note exists (p.105-106, decoded) stating the company "enters into
forward, option and other derivative financial instruments" to hedge forex/commodity price risk and "neither
holds nor issues any derivative financial instruments for speculative purposes" — but no actual derivative
position, notional amount, or mark-to-market is disclosed anywhere in the balance sheet or notes (no separate
derivative asset/liability line in the Balance Sheet). Either boilerplate policy language with no FY25
transactions, or an unrecoverable numeric disclosure (extraction failure). Given no derivative balance appears
on the Balance Sheet (Notes 2.1-4.6 fully captured, no such line), the more likely read is boilerplate with nil
FY25 activity — rated informational, not a flag.

## Schedule III mandatory Ratio Disclosure table (p.106, decoded; ALL VALUES NOT FOUND IN DOCUMENT — extraction
failure per caveat)
🔴 The company's own disclosure of Current Ratio, Debt-Equity Ratio, Debt Service Coverage Ratio, Return on
Equity, Inventory Turnover, Trade Receivables Turnover, Trade Payables Turnover, Net Capital Turnover, Net
Profit Ratio, Return on Capital Employed, and Return on Investment — together with the mandatory explanation
for any variance >25% YoY — could not be extracted (blank numeric cells, same root cause as the RPT table).
This is a real gap since Schedule III specifically requires companies to EXPLAIN large ratio movements, and
several of the ratios computed independently in this pass (debtor days, inventory days) show a >25% movement
that the company's own filing may or may not have flagged and explained — that explanation is unavailable.
Recommend re-extraction from the source PDF (pages ~109 of report pagination) via OCR or manual read before
Stage 11 valuation locks in working-capital assumptions.

## Undisclosed income / Crypto currency disclosures (p.106-107, decoded, clean narrative)
🟢 No undisclosed income surrendered in tax assessments (standard nil disclosure). No crypto/virtual currency
trading or investment during the year (standard nil disclosure).

## Additional Regulatory Information — Schedule III Para Y (p.107-108, decoded, clean narrative)
🟢 No immovable property held other than leasehold (lessee) premises with title deeds not in company's name —
standard for a leased-facility manufacturer, not a red flag.
🟢 No revaluation of PPE (cross-checked, consistent with Note 3.3).
🟢 No loans/advances in the nature of loans granted to promoters, directors, KMPs or related parties that are
either repayable on demand or without specified repayment terms (a specific anti-abuse disclosure) — clean.
🟢 No benami property proceedings.
🟢 Borrowings secured against current assets, and quarterly returns/statements filed with banks are "subject
to confirmation by the bank" — i.e., the company has NOT independently confirmed no discrepancy exists between
its own current-asset records and what was reported to the lender for drawing-power purposes; standard
boilerplate caveat but worth noting given the receivables/inventory build discussed above — any overstatement
in quarterly stock/debtor statements to the bank versus books would not necessarily be caught by this
disclosure. Rated informational, not an active flag, since no discrepancy is alleged.
🟢 No transactions with companies struck off under Sec 248 of the Companies Act.
🟢 No scheme of arrangement under Sections 230-237.
🟢 No investments requiring layers-of-subsidiaries compliance (no subsidiaries).
🔴 Already covered above under Note 1.0 — the unresolved LLP tax liability settlement via directors' personal
accounts is disclosed here as the SOLE exception to the standard "no funds advanced to intermediaries /
ultimate beneficiaries" declaration (p.108, decoded) — repeating the flag from Note 1.0 for completeness since
it appears in this section verbatim as well.
🟢 No funds received from "Funding Parties" for ultimate-beneficiary lending/investing (standard clean
declaration).

═══════════════════════════════════════════════════════════
CROSS-DOCUMENT ITEMS (Directors' Report / CARO / IFC — read because Note 1 explicitly cross-references them
and an investor would care; anchored to their own pages)
═══════════════════════════════════════════════════════════

🟢 **Auditor's opinion**: Unmodified/unqualified (Independent Auditor's Report, p.63, decoded — "In our opinion
... give a true and fair view"). No emphasis-of-matter paragraph. No going-concern qualification — auditor
explicitly states nothing came to their attention indicating material uncertainty about the company's ability
to meet liabilities falling due within one year (CARO Annexure A, clause (xix), p.72, decoded). No Key Audit
Matters section present in the extracted text (small-company audit report format, KAM reporting is a listed-
company-in-Ind AS convention typically; IGAAP SME filings often omit it) — NOT FOUND IN DOCUMENT / not
applicable.
🟢 **New statutory auditor appointed for FY25** replacing a "non-peer reviewed firm", "no issue or objection
raised by outgoing auditor" (CARO Annexure A clause (xviii), p.74-75, decoded) — clean auditor transition,
common/mandatory for a company moving from private to listed status (peer-review requirement kicks in).
🟢 **IFC report**: unmodified opinion, adequate and operating-effective internal financial controls (Annexure
B, p.73-74, decoded).
🟢 **No fraud reported by auditors** under Sec 143(12); no ADT-4 filed; no whistleblower complaints (CARO
Annexure A clause (xi), p.71, decoded).
🟢 **No related-party non-compliance flagged by auditor**: "transactions with related parties are in compliance
with the provisions of section 177 and 188... details have been disclosed in the financial statements... as
required by the applicable accounting standards" (CARO Annexure A clause (xiii), p.71, decoded) — auditor sign-
off on RPT compliance, though this doesn't resolve the Sanjiya Metal Corporation value-recovery gap flagged
above.
🟢 **No cash losses** in FY25 or the immediately preceding year (CARO clause (xvii), p.71-72, decoded).
🟡 **Subsequent event — Rights Issue approved post year-end**: Board approved on 07-Aug-2025 a rights issue of
up to ₹23.10 Cr (Directors' Report, p.31-32, clean text), NSE in-principle approval received 21-Aug-2025, no
shares allotted as of the report signing date. ₹23.10 Cr is larger than the entire FY25 net worth (₹31.24 Cr)
addition base and roughly 2x the ₹11.01 Cr raised at IPO five months into listed life — a materially dilutive
subsequent capital raise that is directly relevant to per-share valuation work in later pipeline stages. This
should be explicitly flagged forward to Stage 11 (valuation) as a known near-term dilution event.
🟢 **IPO mechanics** (Directors' Report p.32, clean text, cross-checked against Notes 2.1/2.2): 34,40,000 fresh
equity shares at ₹32.00/share (author calculation, ties exactly: ₹3.44 Cr face value + ₹7.57 Cr securities
premium addition = ₹11.01 Cr gross, ÷ 34.40 lakh shares = ₹32.00/share), listed on NSE Emerge from 31-May-2024.
No OFS component disclosed — fresh issue only.
🟢 CSR: not applicable (Directors' Report p.39, clean text — company below the Sec 135 net-profit/turnover/net-
worth thresholds, consistent with only its 2nd year of scaled operations).
🟢 No dividend declared or recommended (Directors' Report p.31 and CARO clause, both clean text) — retained
100% of profit, consistent with a young, capital-intensive growth-stage company.
🔴 **No Cash Flow Statement or Statement of Changes in Equity found anywhere in the extracted document**,
despite the Independent Auditor's Report explicitly stating in its opinion paragraph that it audited "the
balance sheet... the statement of profit and loss, statement of changes in equity and statement of cash flows
for the year then ended" (p.63, decoded) and Note 1's "Other Accounting Standard Compliances" section stating
"The Cash Flow statement is prepared by the indirect method set out in the accounting standard on cash flow
statement" (p.106-107, decoded). A page-by-page read of the entire extracted text from the Balance Sheet
(p.85/report-p.82) through the final page (p.113/report-p.109-110) found Balance Sheet, P&L, and Notes only —
no primary Cash Flow Statement table and no Statement of Changes in Equity table appear. This could be (a) a
genuine extraction failure specific to these two statements (most likely, given the broader extraction issues
documented in the caveat above — they may have been formatted as complex multi-column tables that failed to
extract as text entirely, rather than partially like the RPT/ratio tables), or (b) these statements were
genuinely not included in the filed annual report, which would itself be a compliance gap. This cannot be
resolved without re-rendering the source PDF (pdftoppm was unavailable in this environment) and should be
escalated as a mechanical follow-up before the numbers here are used to model cash conversion in later stages
— it directly affects verification of the receivables/cash divergence flagged in Note 4.3/4.4 above.

═══════════════════════════════════════════════════════════
PASS 1 SUMMARY
═══════════════════════════════════════════════════════════
GSM Foils is a 2nd-year listed micro-cap (NSE Emerge, IGAAP reporter) that converted from an LLP to a company
in FY24 and completed its SME IPO (₹11.01 Cr fresh issue at ₹32/share) in May 2024. FY25 shows strong headline
growth (revenue +227.7%, PAT +605.5%) funded partly by fresh capital (PPE nearly tripled) but the balance sheet
shows clear signs of working-capital strain building underneath the growth: trade receivables grew 4.67x
(faster than revenue), debtor days rose from ~65 to ~92, cash fell even as profit surged nearly 7x, and short-
term borrowings rose 295% to fund the gap. Auditor's opinion is clean/unqualified with no going-concern
language and CARO/IFC reports raise no red flags on their own. Governance-adjacent items worth carrying forward:
an unresolved legacy LLP tax liability being settled through directors' personal accounts, a related party
("Sanjiya Metal Corporation") whose transaction nature/value could not be recovered from this document, a
disclosed-but-unquantified foreign-currency royalty expenditure category with no foreign related party
identified, and a large (₹23.10 Cr) rights issue approved just after year-end that is directly relevant to
dilution modelling. A significant PORTION of Note 1's numeric disclosures (RPT rupee amounts, forex
earnings/outgo, the full Schedule III ratio table, and — most importantly — the Cash Flow Statement and
Statement of Changes in Equity in their entirety) could not be recovered from this text extraction and should
be re-verified against the source PDF before later pipeline stages rely on them.

### TOP 10 FINDINGS RANKED BY INVESTOR IMPORTANCE

| Rank | Finding | Note/Anchor | Rating |
|---|---|---|---|
| 1 | Trade receivables +366.7% YoY vs revenue +227.7%; debtor days ~65→~92; cash fell to ₹0.24 Cr despite PAT nearly 7x-ing; funded by short-term borrowings +295% to ₹17.82 Cr | Notes 4.3, 4.4, 2.9 (p.90, p.85) | 🔴 Red Flag |
| 2 | Cash Flow Statement and Statement of Changes in Equity — both stated as audited in the Auditor's Report — do not appear anywhere in the extracted document; cannot verify cash generation independently | Auditor's Report opinion para (p.63); absent throughout p.85-113 | 🔴 Red Flag (mechanical — needs source PDF re-check) |
| 3 | Unresolved legacy GSM Foils LLP income-tax liability being settled through directors' (promoters') personal bank accounts, amount unquantified, still open as of FY25 sign-off | Note 1, Additional Regulatory Info (p.108, decoded) | 🔴 Red Flag |
| 4 | Related party "Sanjiya Metal Corporation" (KMP-proprietorship) transaction nature/value unrecoverable from extraction — potential supplier/RPT exposure given aluminium input business | Related Party list (p.104, decoded) | 🔴 Red Flag (data gap, needs re-verification) |
| 5 | ₹23.10 Cr rights issue board-approved 07-Aug-2025 (post year-end), NSE in-principle approval received, not yet allotted — materially dilutive, larger than IPO raise | Directors' Report, Material Changes (p.31-32, clean text) | 🟡 Watch — carry to Stage 11 valuation |
| 6 | Director/KMP remuneration up 373.7% YoY (₹0.19 Cr → ₹0.90 Cr) reclassified between "Other Expenses" (FY24) and "Employee Benefits" (FY25), obscuring like-for-like comparison in Note 5.2 alone | Notes 5.2, 5.5, AOC-2 (p.93-94, p.45) | 🟡 Watch |
| 7 | Schedule III mandatory ratio-disclosure table (Current Ratio, D/E, DSCR, ROE, turnover ratios, ROCE, ROI + variance explanations) entirely unrecoverable from extraction | Note 1, Ratio Disclosure (p.106, decoded) | 🟡 Watch (data gap) |
| 8 | Zero MSME trade payables disclosed in both years despite ₹7.36 Cr total payables and no standard MSMED-Act interest boilerplate present | Note 3.0 (p.86) | 🟡 Watch |
| 9 | No gratuity/employee-benefit actuarial provision anywhere despite 31 employees and an accounting policy naming "gratuity fund and compensated absences" | Note 1 policy (p.79/100); Notes 2.7/2.8 (nil) | 🟡 Watch |
| 10 | Revenue recognition policy still references abolished "excise duty" with no GST treatment mentioned; no revenue disaggregation by product/customer/geography despite multi-product description elsewhere in report | Note 1 (p.78/99); Note 4.7 (p.92) | 🟡 Watch |
