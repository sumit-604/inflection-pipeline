# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 1 (FULL EXTRACTION)
Company: Orchid Pharma Ltd (ORCHPHARMA) | Run date: 2026-09-06 | Pass 1 of 3

## SCOPE AND CORPUS CAVEAT

Source: Annual_Report_2025.pdf (FY2025, standalone and consolidated financial
statements, Notes 1-58 standalone / 1-52 consolidated), cross-checked against
Annual_Report_2024.pdf comparatives embedded in the FY2025 notes themselves.
FY2026 has no annual report in corpus (per orchestrator instruction; any
FY2026 note content is NOT FOUND, reason: "FY2026 primary filing absent from
corpus").

OCR QUALITY WARNING: the pre-extracted text is heavily corrupted in numeric
TABLE regions (columns flattened out of visual order, digits merged or
dropped, e.g. "It" for "11", "t3" for "13"). Narrative/policy text is legible.
Where a table cell could be reconstructed with high confidence (values sum to
a known total, or match a figure appearing independently elsewhere in the
statements), it is reported as a hard number with its anchor. Where it could
not be, the cell is marked NOT FOUND IN DOCUMENT (OCR extraction illegible)
rather than estimated. This is a corpus-freshness/extraction-quality issue,
not a company disclosure gap, and is called out explicitly wherever it
affects a rated finding.

All amounts below are as stated in the AR (INR lakhs unless converted to Cr
for readability; 1 Cr = 100 lakhs). Standalone note numbers 1-58 map as
verified against the face of the standalone balance sheet and P&L (Note
number column reconciled against known totals). Consolidated notes carry
similar but not identical numbering (offset by one from Note ~40 onward,
because consolidated splits income-tax/deferred-tax across two notes where
standalone combines them); consolidated note numbers are stated separately
where used.

---

## NOTE-BY-NOTE FINDINGS (STANDALONE, PRIMARY; CONSOLIDATED CROSS-REFS NOTED)

### Note 1 — Corporate Information
Orchid Pharma Ltd, Chennai-headquartered API/FDF/nutraceutical manufacturer,
exports to 40+ countries. Went through NCLT Corporate Insolvency Resolution
Process; Dhanuka Laboratories Ltd (DLL) was the successful Resolution
Applicant, implemented 31-Mar-2020 via a merged SPV (Dhanuka Pharmaceuticals
Pvt Ltd). Orchid has been a subsidiary of DLL since 31-Mar-2020.
(Annual_Report_2025.pdf, p.183, Note 1) 🟢 Clean, standard disclosure.

### Note 2 / 2A — Basis of Preparation, Critical Estimates
Ind AS compliant, historical cost basis except FVTOCI/FVTPL instruments.
Critical judgments named: PPE/intangible useful life and residual value
(technical team assessed), current tax positions, DTA recognition (see Note
25), fair value of unquoted instruments, ECL on trade receivables.
(p.183-184, Note 2/2A) 🟢 Clean, standard boilerplate.

### Note 3 — Material Accounting Policies
Revenue recognised point-in-time on dispatch/Incoterms (Ind AS 115); no
material financing component adjustment (short-term customer advances,
practical expedient used, reasonable for this industry). PPE depreciated
straight-line per Schedule II lives, EXCEPT certain assets where useful life
is internally assessed / externally technically evaluated and "differs from"
Schedule II Part C lives — the note does NOT quantify which assets or the
P&L impact of this deviation. 🟡 Watch: a disclosed but unquantified
departure from statutory useful lives is a standard but real judgment area;
no amount is given, so impact cannot be sized (NOT FOUND IN DOCUMENT: rupee
impact of useful-life deviation). Capitalisation threshold: additions ≤
Rs.5,000 fully depreciated immediately (not aggressive). Intangibles: DMF/ANDA
filing costs amortised over lesser of 5 years or cost-recovery period once
commercial value is established via third-party agreement — reasonable,
industry-standard. Inventory: lower of cost (weighted average) or NRV,
including variable/fixed overhead in WIP/finished goods cost — standard.
(p.184-194, Note 3) 🟢/🟡 Clean policy set, one unquantified judgment area.

Sub-note "28" (Recent accounting pronouncements, standalone numbering
oddity — this is a sub-item of Note 3, not a top-level note): Ind AS 117
(Insurance Contracts) and Ind AS 116 sale-and-leaseback amendments notified,
company assessed no significant impact. (p.184, "Note 28"/Note 3) 🟢 Clean.

### Notes 4-5 — PPE, Intangibles, CWIP, Intangible Assets Under Development
Depreciation and amortisation expense for the year: Rs.3,443.62 lakhs FY2025
vs Rs.3,321.90 lakhs FY2024 (Note 37/P&L). (p.178, Note 37)
CWIP (standalone): Rs.2,769.14 lakhs FY2025 vs Rs.1,018.27 lakhs FY2024 — up
172% YoY already within FY2025 itself, before any FY2026 move.
(Annual_Report_2025.pdf, p.197, Note 5) 🟡 Watch — a near-tripling of CWIP
within the audited FY2025 year is the leading edge of the capex ramp the
orchestrator's screener pointer describes for FY2026.
Gross block, additions, and disposals table for PPE could NOT be reliably
reconstructed from the OCR (table cells scrambled). NOT FOUND IN DOCUMENT
(OCR extraction illegible for PPE gross-block movement table); depreciation
expense and CWIP totals above are independently corroborated figures, so
high confidence.
CONSOLIDATED CWIP (Note 53(a) consolidated) is materially higher: projects in
progress Rs.5,542.26 lakhs (<1yr) + Rs.906.67 lakhs (1-2yr) = Rs.6,448.93
lakhs total as at 31-Mar-2025, vs standalone Rs.2,769.14 lakhs.
(Annual_Report_2025.pdf, p.273, consolidated Note 53(a)) 🔴 Red Flag — the
Rs.3,679.79 lakh (~Rs.36.8 Cr) gap between consolidated and standalone CWIP
sits at subsidiary level (Orchid Bio-Pharma Ltd, the KSM backward-integration
facility). This is the single clearest anchor for why group CWIP could move
sharply between FY2025 and FY2026: the subsidiary's own capex is already
running well ahead of the parent's.

### Note 6 — Non-current Investments
Investments in subsidiaries at cost (gross): Rs.19,404.71 lakhs FY2025 vs
Rs.19,409.89 lakhs FY2024. Less: provision for diminution Rs.(12,470.10)
lakhs BOTH years (unchanged) → net Rs.6,934.61 lakhs FY2025 / Rs.6,939.79
lakhs FY2024. (p.196-197, Note 6) 🟡 Watch — ~64% of the gross cost of the
subsidiary investment book is already provided for/written down (mainly the
loss-making US entities: Bexel Pharmaceuticals Inc., Orchid Pharmaceuticals
Inc., Diakron Pharmaceuticals Inc.). Orchid Pharmaceuticals SA (Proprietary)
Ltd, South Africa, was wound up 31-Jan-2024; investment fully provided but
not yet written off, "pending approval of RBI." (p.197, Note 6) 🟡 Watch —
open item awaiting regulatory approval, small (immaterial rupee amount, not
separately disclosed beyond being folded into the Rs.12,470.10 lakh
provision).
Investment in associate Orbion Pharmaceuticals Private Ltd: Rs.4,550.00
lakhs at cost (4,55,00,000 shares of Rs.10 each), unchanged both years.
Investment in Orchid Bio-Pharma Ltd (wholly owned subsidiary, the KSM/API
backward-integration vehicle): Rs.1,500.00 lakhs at cost (1,50,00,000 shares
of Rs.10 each), unchanged both years — i.e. the FY2025 funding of that
subsidiary's capex ramp did NOT come through fresh equity infusion; it came
through the intercompany LOAN (see Note 7 below).

### Note 7 — Loans to Subsidiaries (non-current)
Loan to Orchid Bio-Pharma Ltd: Rs.10,824.32 lakhs (Rs.108.24 Cr) as at
31-Mar-2025 vs Rs. NIL as at 31-Mar-2024. (p.197, Note 7) 🔴 Red Flag — this
is the single largest funding-flow finding in the notes: a Rs.108.24 Cr
intercompany loan to the subsidiary appeared from nothing within FY2025,
funding exactly the KSM/API capex programme that is driving the consolidated
CWIP gap identified under Notes 4-5. The note explicitly states this is the
ONLY loan the company has given to any related party without fixed
repayment terms or demand basis. No interest rate, tenure, or repayment
schedule is disclosed for this loan. NOT FOUND IN DOCUMENT: interest rate,
tenure, security, repayment terms on the Rs.108.24 Cr subsidiary loan —
this is a genuine, material disclosure gap, not an OCR artefact (the
narrative text is legible and simply does not state these terms).

### Note 8 — Other Non-current Financial Assets
Includes legacy "Loans to subsidiaries — credit impaired" Rs.5,229.36 lakhs,
fully provided (less allowance Rs.(5,432.02) lakhs against total doubtful
loans/deposits of Rs.5,432.02 lakhs — provisioned at effectively 100%),
carried from the pre-CIRP period. (p.197-198, Note 8) 🟢 Clean — fully
provided legacy exposure, no incremental P&L risk.

### Note 9-10 — Non-current Tax Assets / Other Non-current Assets
Advance income tax (net of provision) and capital advances. Figures legible
but not independently cross-checked against a second source; reported as
extracted: Advance tax Rs.5,130.15 lakhs (unchanged both years per the note);
Capital advances Rs.1,987.17 lakhs FY2025 vs Rs.235.89 lakhs FY2024 — a
~742% increase. (p.199, Notes 9-10) 🔴 Red Flag — capital advances (money
paid out ahead of capex execution) rising more than 8x in one year is a
second independent confirmation of the pre-FY2026 capex ramp, consistent
with the CWIP and capital-commitment findings above.

### Note 11 — Inventories
Total: Rs.32,637.15 lakhs (Rs.326.37 Cr) FY2025 vs Rs.26,422.61 lakhs
(Rs.264.23 Cr) FY2024, +23.5% YoY, against revenue growth of only +12.5%
(Rs.81,936.82 lakhs → Rs.92,192.59 lakhs). Category breakdown (reconstructed
and verified — FY2025 categories sum exactly to the reported total):
Raw Materials Rs.8,262.11 lakhs (Rs.6,601.01 lakhs FY24); Intermediates &
WIP Rs.12,819.36 lakhs (Rs.11,486.56 lakhs FY24); Finished Goods Rs.10,494.81
lakhs (Rs.7,442.50 lakhs FY24, +41.0% YoY); Traded Goods Rs.166.76 lakhs
(Rs.313.06 lakhs FY24); Stores & Spares Rs.321.32 lakhs (Rs.289.89 lakhs
FY24); Chemicals & Consumables Rs.278.84 lakhs (Rs.289.59 lakhs FY24);
Packing Materials Rs.293.95 lakhs (no separate FY24 comparative — the six
other FY24 categories sum exactly to the FY24 total, implying Packing
Materials was a new sub-category carved out in FY2025, immaterial in size).
(p.199, Note 11) 🔴 Red Flag — Finished Goods inventory grew 41% against
12.5% revenue growth; combined with the receivables finding below (Note 13),
this is a working-capital build running well ahead of sales, a genuine
cash-conversion concern (feeds FLAG-CASH). Physical verification note states
no discrepancy >10% found in any category (p.199, Note 11) 🟢 Clean on that
sub-point.

### Note 12 — Current Investments
Investment in mutual funds, fair valued through P&L. (p.199, Note 12) 🟢
Clean, standard treasury deployment.

### Note 13 — Trade Receivables
Gross: Rs.31,038.89 lakhs FY2025 vs Rs.27,124.23 lakhs FY2024 (+14.4%). ECL
allowance: Rs.(6,855.68) lakhs FY2025 vs Rs.(8,187.19) lakhs FY2024 — the
ABSOLUTE provision fell 16.3% even as gross receivables grew. Net: Rs.
24,183.21 lakhs FY2025 vs Rs.18,937.04 lakhs FY2024, +27.7% YoY — more than
double the revenue growth rate. ECL coverage ratio fell from 30.2% of gross
(FY2024) to 22.1% of gross (FY2025). (p.198, Note 13) 🔴 Red Flag — net
receivables growing at 2.2x the rate of revenue, driven partly by a
materially LOOSENED provisioning ratio, is a legitimate accounting-quality
and cash-conversion concern (feeds FLAG-CASH; receivables_trend:
deteriorating). No related-party receivable is unprovided-for beyond what is
disclosed in Note 50 (cross-ref confirmed).
Consolidated ageing (Note 53(d) consolidated, clearer OCR than standalone
equivalent): Undisputed, considered good — Not due Rs.16,668.30 lakhs, <6
months Rs.7,467.33 lakhs, 6mo-1yr Rs.47.58 lakhs, nothing older. Credit
impaired (legacy): Rs.3.23 + Rs.21.32 + Rs.0.64 + Rs.3,369.18 lakhs (>3
years) = Rs.3,394.37 lakhs, presumably substantially provided for via the
ECL allowance above. (p.273-274, consolidated Note 53) 🟢 Clean on the
CURRENT book (69% not yet due); 🟡 Watch on the stale >3yr credit-impaired
tail (Rs.33.7 Cr, legacy).

### Note 14 — Cash and Cash Equivalents
Rs.1,587.08 lakhs FY2025 vs Rs.29.47 lakhs FY2024 — up sharply, consistent
with the QIP proceeds still sitting partly unutilised (see Note 55).
(p.200, Note 14) 🟢 Clean.

### Notes 15-19 — Other Bank Balances / Current Loans to Subsidiary / Other
Current Financial Assets / Current Tax Assets / Other Current Assets
Other bank balances Rs.14,841.19 lakhs FY2025 vs Rs.25,693.26 lakhs FY2024
(includes QIP escrow/earmarked deposits, refer Note 55). Loan to Orchid Bio
Pharma Ltd (CURRENT portion) is explicitly Rs. NIL FY2025 vs Rs.788.97 lakhs
FY2024 — i.e. the FY2024 current loan was reclassified/rolled into the new
Rs.108.24 Cr NON-CURRENT loan disclosed at Note 7, not repaid.
(p.200, Notes 15-19) 🟢 Clean, consistent with Note 7 cross-reference.

### Note 20 — Equity Share Capital
Authorised capital anomaly: authorised share capital increased by 10,000
shares of Rs.10 each pursuant to a scheme of amalgamation, but "yet to be
updated in the records of the Registrar of Companies," company states it is
"closely following up for regularisation." (p.201, Note 20) 🟡 Watch — minor
but a genuine open compliance item, small in rupee terms (Rs.1 lakh face
value) but indicative of administrative lag around corporate-restructuring
paperwork, relevant context given the Note 56 NCLT amalgamation petition
below. Dhanuka Laboratories Ltd holds 3,54,19,957 shares = 69.84% of paid-up
capital, both years (down from 89.96% pre-QIP per the June-2023 QIP
disclosure elsewhere in the AR, outside notes scope). (p.202, Note 20) 🟢
Clean, consistent with known promoter structure.

### Note 21 — Other Equity
Standard reserve roll-forward (Capital Reserve, Capital Reserve on
Amalgamation, Securities Premium, Equity component of OCDs Rs.6,856.06 lakhs
unchanged, General Reserve, OCI, Retained Earnings). Retained earnings
remain deeply negative: Rs.(1,88,259.90) lakhs FY2025 vs Rs.(1,98,838.29)
lakhs FY2024 — accumulated losses of ~Rs.1,882.6 Cr still being worked down
by current profits. (p.201-203, Note 21) 🟡 Watch — a large accumulated
deficit is the legacy of the pre-CIRP insolvency; not a new finding, but
context for why the company reports NIL net deferred tax and NIL current
tax (Notes 25, 40 below) despite reported profit.

### Note 22 — Long-term Borrowings
Unsecured 0% Optionally Convertible Debentures (OCDs): 14,300 OCDs of
Rs.1,00,000 face value each issued in FY2020 (Rs.14,300 lakhs = Rs.143 Cr
face value), held by the promoter/holding company Dhanuka Laboratories Ltd
(cross-ref Note 50). If NOT converted, holders get a redemption premium of
at least 11% IRR annually, rising up to a cap of 16% IRR annually depending
on Board discretion and share price. Unlisted, transferable only with Board
permission. Carrying value (non-current) Rs.13,163.58 lakhs FY2025 vs
Rs.12,020.91 lakhs FY2024 (premium accreting). (p.208-209, Note 48
[terms cross-ref]; p.202-203, Note 22 [balance]) 🟡 Watch — a related-party
convertible instrument accruing an 11-16% IRR premium if unconverted is a
real economic cost to minority shareholders that is easy to overlook because
it carries a "0%" coupon label; the actual embedded cost is far from zero.
Diluted EPS shows NO dilutive effect from this instrument in either year
(Note 41 below) — NOT FOUND IN DOCUMENT: stated conversion ratio/conversion
price for the OCDs, which would explain the diluted-EPS treatment. This is a
question for management.

### Note 23-24 — Lease Liabilities (Non-current) / Provisions (Non-current)
Lease liabilities non-current Rs.3.67 lakhs FY2025 vs Rs.37.00 lakhs FY2024
(small). Provisions (non-current, employee benefits — gratuity Rs.40.74
lakhs, compensated absences Rs.297.98 lakhs) Rs.338.72 lakhs FY2025 vs
Rs.363.37 lakhs FY2024. (p.203-204, Notes 23-24) 🟢 Clean, immaterial
movements.

### Note 25 — Deferred Tax Asset/(Liability), Net
Net deferred tax is NIL in both years by construction: DTL on PPE/intangible
timing differences (Rs.(11,081.42) lakhs opening FY2025 → Rs.(12,255.95)
lakhs closing) is exactly offset by a DTA on unabsorbed depreciation, which
the company DELIBERATELY caps/scales down to match the DTL — "no deferred
tax asset has been created in respect of carry forward business losses in
the absence of convincing evidence that sufficient future taxable income
will be available." (p.206-207, Note 25) 🟢 Clean/conservative — this is
genuinely conservative accounting (no speculative DTA recognised on losses),
but it also means the company is NOT signalling near-term confidence in its
own future taxable profits, worth weighing against the FY2026 screener
pointer of pre-tax profit falling to near zero.

### Note 26 — Current Borrowings
Secured Cash Credit / Working Capital Demand Loan and Buyers' Credit:
Rs.4,260.33 lakhs FY2025 vs Rs.1,404.75 lakhs FY2024 (+203%). Security:
multiple first/second pari passu charges — hypothecation of current assets,
movable fixed assets, mortgage of immovable property, intangibles/goodwill,
uncalled capital, and letters of credit/guarantees. Lenders: HDFC Bank and
Yes Bank. Interest rate range 8.25%-9.60% p.a. (p.203, 210, Notes 26 & 48)
🟡 Watch — short-term secured borrowing more than tripled YoY within
FY2025, consistent with the working-capital build identified in Notes 11
and 13. NO covenant breach, default, or waiver disclosed anywhere in the
notes searched (no hits for "covenant"/"breach"/"default"/"waiver" tied to
Orchid's own facilities). (whole-document grep, cross-checked) 🟢 Clean on
that specific point — no covenant-breach evidence exists in this corpus, but
see the going-concern/qualified-opinion cross-reference under Note 3(c)
below, which is a different matter.

### Note 27-28 — Lease Liabilities (Current) / Trade Payables
Trade payables MSME dues: Rs.1,102.34 lakhs FY2025 vs Rs.866.53 lakhs FY2024
(+27.2%). Trade payables — others: Rs.15,945.55 lakhs FY2025 vs Rs.17,072.35
lakhs FY2024 (-6.6%). Total trade payables Rs.17,047.89 lakhs FY2025 vs
Rs.17,938.88 lakhs FY2024. (p.203-204, Note 28) 🟡 Watch — MSME dues rising
27% while total payables fall 6.6% shifts more of the payables mix onto
smaller suppliers; payable-days ageing bucket detail NOT FOUND IN DOCUMENT
(OCR extraction illegible for the ageing sub-table).

### Note 29-30 — Provisions (Current) / Other Current Liabilities
Provision for employee benefits (gratuity Rs.157.44 lakhs, compensated
absence Rs.79.16 lakhs) totalling Rs.236.60 lakhs FY2025 vs Rs.208.47 lakhs
FY2024. Other current liabilities Rs.2,169.31 lakhs FY2025 vs Rs.1,382.00
lakhs FY2024. (p.204, Notes 29-30) 🟢 Clean, modest movements.

### Notes 31-41 — Statement of Profit and Loss Notes
Revenue from operations Rs.92,192.59 lakhs (Rs.921.93 Cr) FY2025 vs
Rs.81,936.82 lakhs (Rs.819.37 Cr) FY2024, +12.5%. Other income Rs.3,192.91
lakhs vs Rs.3,038.94 lakhs. Cost of materials consumed Rs.58,546.06 lakhs vs
Rs.52,835.31 lakhs. Employee benefits Rs.8,636.06 lakhs vs Rs.6,964.17
lakhs (+24.0% — well ahead of revenue growth; NOT FOUND IN DOCUMENT: a
management explanation for the jump, beyond the general P&L presentation).
Depreciation Rs.3,443.62 lakhs vs Rs.3,321.90 lakhs. Finance costs
Rs.1,454.01 lakhs vs Rs.1,632.75 lakhs (down, despite current borrowings
tripling — consistent with OCD-related finance cost being non-cash/embedded
in equity rather than P&L). Other expenses Rs.16,781.21 lakhs vs Rs.15,458.70
lakhs. No exceptional items either year. Profit before tax = profit after
tax (income tax expense NIL both years, see Note 40). Basic = Diluted EPS
Rs.20.99 FY2025 vs Rs.19.59 FY2024 (weighted average shares 5,07,19,105 both
years; FY2024 weighted average differed at 4,83,65,183 due to the mid-year
June-2023 QIP allotment). (p.177-179, 205-208, Notes 31-41) 🟡 Watch on
employee cost growth outpacing revenue; 🟢 Clean on the rest.
Payment to auditors: Rs.33.08 lakhs FY2025 (statutory audit Rs.17.50 lakhs,
limited review Rs.10.50 lakhs, tax audit Rs.1.00 lakh, certificates/other
services Rs.3.00 lakhs, out-of-pocket Rs.0.08 lakhs) vs Rs.37.00 lakhs
FY2024. (p.205-206, Note 39) 🟢 Clean, reasonable audit fee.

### Note 40 — Income Tax Expense
No provision for current tax; company explicitly cites carried-forward
losses under taxation law as the reason. Deferred tax expense to P&L is NIL
both years (see Note 25 mechanism above). (p.206, Note 40) 🟢 Clean/
consistent with Note 25.

### Note 41 — Earnings Per Share
Covered above under Notes 31-41. Flag repeated here for the open question:
NOT FOUND IN DOCUMENT — conversion ratio for the OCDs (Note 22/48), which
would clarify why no dilutive effect is shown. 🟡 Watch — question for
management.

### Note 42 — Expenditure on Research and Development
R&D revenue expenditure disclosed (power and fuel, stores/spares/chemicals
consumption categories named); precise rupee total NOT independently
cross-verified in this pass (OCR table for the R&D cost breakup not fully
reconstructed) — carried forward to Pass 2 for a closer look.
(p.207-208, Note 42) — rating deferred.

### Note 43 — MSMED Disclosures
Principal amount remaining unpaid to MSME suppliers at year-end: Rs.1,102.34
lakhs FY2025 (matches Note 28 MSME trade payable). Interest actually paid
under Section 16 of the MSMED Act: NIL. Normal interest due and payable
during the year (unpaid): NOT FOUND as a clean standalone figure in this
pass (OCR ambiguous between the standalone and the clearer consolidated
Rs.4.56 lakhs "total interest accrued and remaining unpaid" figure quoted at
consolidated Note 44 — cross-referenced, standalone figure likely close but
not independently confirmed). (p.207-208, Note 43; consolidated Note 44,
p.262) 🟡 Watch — MSME payment delays exist and attract statutory interest,
even if the disclosed accrued-interest rupee amount is small.

### Note 44 — Commitments and Contingent Liabilities (HIGH PRIORITY per
orchestrator instruction)
STANDALONE, as at 31-Mar-2025 (Annual_Report_2025.pdf, p.208-209, Note 44):
- Income tax dispute pending before Chennai High Court: NIL
- GST tax dispute pending before jurisdictional authority: Rs.144.22 lakhs
- Electricity Department claim: Rs.112.44 lakhs (disputed, contingent from
  01.04.2020, pre-CIRP period per company's assessment)
- Other claims: NIL (standalone)
- Unexpired Letters of Credit and Bank Guarantees: Rs.373.20 lakhs
- Corporate Guarantees given for loans availed/to be availed by a wholly
  owned subsidiary: Rs.44,722.00 lakhs (Rs.447.22 Cr) 🔴 RED FLAG
- Capital commitments (contracts remaining to be executed on capital
  account, not provided for): Rs.9,024.80 lakhs (Rs.90.25 Cr) 🔴 RED FLAG

CONSOLIDATED, as at 31-Mar-2025 (Annual_Report_2025.pdf, p.264-265,
consolidated Note 45):
- Income tax dispute: NIL. GST dispute: Rs.144.22 lakhs. Electricity claim:
  Rs.112.44 lakhs. Other claims: Rs.379.78 lakhs (unchanged from previous
  year per an explicit footnote — "the Group has recognised the contingent
  liability... for certain claims made on one of subsidiary company").
  Unexpired LC/BG: Rs.373.20 lakhs.
- Capital commitments (contracts remaining to be executed on capital
  account, not provided for): Rs.29,642.89 lakhs (Rs.296.43 Cr) 🔴 RED FLAG
  — this is the single most important number extracted in this pass. It is
  3.3x the standalone figure; the Rs.206.18 Cr gap sits at subsidiary level.
  FY2024 consolidated comparative for this same line: Rs.3,096.11 lakhs
  (Rs.30.96 Cr) — i.e. consolidated capital commitments rose ~9.6x within
  FY2025 alone, BEFORE the FY2026 CWIP move the screener aggregate flags.

The FY2024 comparative column for the remaining consolidated sub-items (GST/
electricity/other-claims breakdown specifically) is NOT FOUND IN DOCUMENT
with confidence (OCR table cells do not reconcile cleanly against the
"other claims unchanged YoY" footnote — reported honestly as ambiguous
rather than forced to a number).

Lease dispute context (both standalone and consolidated, same note): company
settled a post-CIRP-period lease rent dispute via a Joint Memo of Compromise
dated 8-Apr-2025 (a subsequent event relative to the 31-Mar-2025 balance
sheet date), paying Rs.762 lakhs, fully provided for in these statements.
Pre-CIRP-period portion of the same dispute remains open; management's
position is that the NCLT-approved Resolution Plan extinguishes any
liability for the pre-CIRP period. (p.208-209 / p.264-265) 🟡 Watch — an
unresolved legacy dispute where the counterparty continues to press claims
management believes are time-barred by the resolution plan.

### Note 45 — Operating Segments
Single operating segment: "Pharmaceuticals" (Ind AS 108), no segment
reporting required. Geography split, standalone, FY2025: India Rs.18,091.22
lakhs, Rest of World Rs.12,823.17 lakhs, stated total Rs.90,914.39 lakhs.
🔴 OCR/arithmetic inconsistency flagged, not corrected: India + RoW as
extracted (Rs.30,914.39 lakhs) does not equal the stated total
(Rs.90,914.39 lakhs), and neither equals total revenue from operations
(Rs.92,192.59 lakhs, Note 31). This table is NOT FOUND IN DOCUMENT with
confidence beyond the "single segment" qualitative finding; the geography
split numbers are unreliable as extracted and should be re-pulled from the
source PDF directly in Pass 2 rather than trusted from this OCR.
(p.209, Note 45)

### Note 46 — CSR Expenditure
Amount required to be spent, FY2025: Rs.33.35 lakhs (FY2024: NIL — CSR
threshold not triggered in the prior year). Amount actually spent: Rs.11.40
lakhs (donation to an MCA-approved CSR trust; activities named: Environment
Sustainability & Animal Welfare, Healthcare). SHORTFALL: Rs.21.95 lakhs
(65.8% of the requirement unspent). (p.209-210, Note 46) 🔴 Red Flag — the
note's own footnote ("excess spent is available for set off during
subsequent years") is the WRONG footnote for a shortfall scenario; it does
not state whether the unspent Rs.21.95 lakhs was transferred to a specified
CSR fund as Section 135(5) requires for non-ongoing-project shortfalls. NOT
FOUND IN DOCUMENT: confirmation of statutory transfer of the unspent CSR
amount. This is a potential compliance gap, not merely a disclosure
omission.

### Note 47 — Operating Lease Arrangements
Cancellable operating leases for certain facilities; lease payments
recognised in P&L. Amount NOT independently reconstructed with confidence
in this pass (OCR table). (p.210, Note 47) — rating deferred to Pass 2.

### Note 48 — Terms and Conditions of Borrowings
Covered under Notes 22 and 26 above (OCD terms; cash credit/WCDL security
and rate). (p.209-210, Note 48)

### Note 49 — Financial Instruments
Capital management: Gearing ratio 8.74% FY2025 vs 9.84% FY2024 (net debt
Rs.11,574.91 lakhs / total equity Rs.1,32,404.91 lakhs FY2025). Fair value
hierarchy: nearly all financial assets/liabilities are Level 3 (unobservable
inputs) — investments Rs.6,050.00 lakhs Level 3, trade receivables, cash,
bank balances, loans to subsidiaries, borrowings, trade payables, lease
liabilities all Level 3; quoted equity investment Rs.20.09 lakhs Level 1.
Interest rate sensitivity: a 25bps move would swing FY2025 profit by
Rs.10.44 lakhs (FY2024: Rs.3.57 lakhs) — nearly 3x more rate-sensitive than
the prior year, consistent with the tripling of variable-rate current
borrowings (Note 26). No covenant breach, waiver, or going-concern language
found anywhere in this note. (p.210-213, Note 49) 🟡 Watch on rising rate
sensitivity; 🟢 Clean on covenant/going-concern language (none present).

### Note 50 — Related Party Disclosure (HIGH PRIORITY per orchestrator
instruction)
Ultimate/holding company: Dhanuka Laboratories Ltd (69.84% owner).
Subsidiaries: Orchid Pharmaceuticals Inc. USA (and its own subsidiaries
Orgenus Pharma Inc. and Orchid Pharma Inc./Karalex Pharma), Bexel
Pharmaceuticals Inc. USA, Diakron Pharmaceuticals Inc. USA, Orchid Bio-Pharma
Ltd (India). Associate: Orbion Pharmaceuticals Private Ltd. Enterprises with
KMP significant influence: Otsuka Chemicals (India) Pvt Ltd, Synmedic
Laboratories, Dhanuka Agritech Ltd, Invest Care Real Estate LLP, Golden
Overseas Private Ltd, M D Buildtech Private Ltd, Agrihawk Technologies
Private Ltd, Ster Living Infrastructure Advisors LLP, Dhanuka Chemicals
Private Ltd, H D Realtors Private Ltd, Turbo Advisers LLP. KMP: Ram Gopal
Agarwal (Chairman, Non-exec), Manish Dhanuka (MD), Mridul Dhanuka
(Wholetime Director), Mahendra Kumar Dhanuka, Arjun Kumar Dhanuka
(Director), Sunil Gupta (CFO), Kapil Dayya (Company Secretary), Marina Peter
(Company Secretary till Dec-2023).

Material RPT balances as at 31-Mar-2025 (standalone, p.213-216, Note 50):
- Loan given to Orchid Bio-Pharma Ltd: Rs.10,824.32 lakhs (Rs.NIL FY2024) —
  cross-ref Note 7. 🔴 Red Flag, already flagged above.
- Corporate guarantee given for Orchid Bio-Pharma Ltd borrowings: Rs.44,722
  lakhs — cross-ref Note 44. 🔴 Red Flag, already flagged above.
- 0% OCDs held by Dhanuka Laboratories Ltd: Rs.14,300.00 lakhs, unchanged
  both years — cross-ref Note 22. Confirmed identically at consolidated
  level (Note 51 consolidated, p.270-271). 🟡 Watch, already flagged above.
- Trade payable to Dhanuka Laboratories Ltd: Rs.5,182.78 lakhs FY2025
  (standalone) / Rs.5,782.78 lakhs (consolidated, small consolidation
  adjustment) vs Rs.6,213.56 lakhs (standalone FY2024, per the RPT-balance
  table) — a large, ongoing trade payable to the parent.
- Equity share capital held by Dhanuka Laboratories Ltd: Rs.3,542.00 lakhs,
  unchanged both years (consolidated Note 51 clean figure; standalone table
  ambiguous between Rs.3,542.00 and Rs.4,550.00 due to OCR row
  misalignment — consolidated figure taken as reliable).
- Receivables written off against Orchid Pharma Inc. (US subsidiary):
  Rs.1,337.52 lakhs, with a simultaneous exactly-offsetting reversal of ECL
  provision of Rs.(1,337.52) lakhs — P&L-neutral, since the balance was
  already 100% provided. (p.216, Note 50) 🟢 Clean mechanically, but a
  Rs.13.4 Cr related-party receivable write-off is still worth naming.
- Remuneration to KMP disclosed individually (Manish Dhanuka, Mridul
  Dhanuka, Sunil Gupta, Kapil Dayya, Marina Peter); specific per-person
  rupee figures partially legible (e.g. Rs.57.55 lakhs, Rs.15.71 lakhs for
  two individuals) but not fully reconstructed with confidence across all
  five names in this pass — carried to Pass 2.
- Sale of goods to Orchid Pharma Inc. (US subsidiary): Rs.23,072.00 lakhs
  FY2025 vs Rs.17,012.94 lakhs FY2024 (+35.6%) — a related party accounting
  for roughly a quarter of total revenue (Rs.230.72 Cr of Rs.921.93 Cr =
  25.0%). 🟡 Watch — significant related-party revenue concentration; this
  is intercompany trade with a subsidiary that itself has near-zero third
  party revenue per the auditor's qualification (see cross-reference below),
  raising a question of what the ultimate external destination of these
  goods is and at what margin they are transferred.

RPT as % of standalone revenue (sale of goods to Orchid Pharma Inc. alone):
~25.0% (Rs.230.72 Cr / Rs.921.93 Cr). This is the single largest related
party revenue line and warrants a question for management on transfer
pricing/arm's-length basis, given the US subsidiary itself has been
loss-making enough to require a Rs.124.70 Cr cumulative provision against
its and its group companies' carrying value (Note 6).

### Note 51 — Retirement Benefit Plans
Defined contribution total expense: Rs.419.93 lakhs FY2025 vs Rs.393.63
lakhs FY2024. Gratuity (defined benefit): current service cost Rs.118.85
lakhs, net interest expense Rs.113.16 lakhs less return on plan assets
Rs.(103.78) lakhs → recognised in Employee Benefits Expense (P&L). OCI
remeasurement loss Rs.69.95 lakhs FY2025 (this ties out exactly against the
Rs.(69.95) lakhs "remeasurement of post-employment benefit obligations"
line in the standalone P&L OCI section, Note 31-41 area — cross-check
passed). Discount rate basis: government bond market yields (rate itself
NOT independently extracted with confidence from OCR — actuarial assumption
TABLE not reliably reconstructed; qualitative description only).
(p.216-218, Note 51) 🟢 Clean, actuarial mechanics tie out; 🟡 Watch —
specific discount-rate/salary-growth assumption percentages NOT FOUND IN
DOCUMENT with confidence (OCR), carried to Pass 2 for a closer look at the
raw PDF if needed.

### Note 52 — Additional Regulatory and Other Information (Schedule III)
(a) CWIP ageing (standalone, as at 31-Mar-2025): Projects in progress <1yr
Rs.2,446.43 lakhs, 1-2yr Rs.322.71 lakhs, nothing older; total Rs.2,769.14
lakhs (ties exactly to the CWIP balance sheet figure, Notes 4-5). No
projects with overdue completion schedules, either year. (p.217-218)
(d) Trade receivables ageing: bucketed by considered-good / significant-
increase-in-credit-risk / credit-impaired, further split MSME vs Others vs
Disputed/Undisputed. Granular cell-level figures are OCR-garbled in the
standalone table; the CONSOLIDATED equivalent (Note 53(d) consolidated) was
legible and is reported above under Note 13. NOT FOUND IN DOCUMENT
(standalone ageing granularity) beyond what is captured via the consolidated
cross-reference.
(f) Benami property proceedings: NONE. (g) Not declared a wilful defaulter
by any bank/FI. (h) No transactions with struck-off companies. (i) Company
in compliance with the layers-of-companies restriction. (k) No Section
230-237 scheme of arrangement approved DURING the year (note: a scheme IS
pending before NCLT — see Note 56 below, filed but not yet approved as at
year-end, so technically consistent). (l) No funds advanced to/received
from intermediaries with round-tripping understanding. (m) No undisclosed
income surrendered in any tax assessment. (n) No title-deed mismatch on
immovable property. (o) No revaluation of PPE/intangibles during the year.
(p) No loans/advances to promoters/directors/KMPs EXCEPT the loan to Orchid
Bio-Pharma Ltd already flagged (Rs.10,824.32 lakhs, 100% of loans-and-
advances-in-the-nature-of-loans category). (q) No crypto/virtual currency
trading. (p.218-221, Note 52) 🟢 Clean across all these specific statutory
negative-assurance items — no hits on any of the classic Schedule III red
flags (Benami, struck-off companies, wilful defaulter, crypto, undisclosed
income).
Ratio commentary: Debt Service Coverage Ratio "significantly improved"
citing full repayment of term loans in the previous year. Net Capital
Turnover Ratio "decreased" due to increased working capital requirement
compared to the earlier year — company's OWN explanation corroborates the
working-capital build independently identified above (Notes 11, 13).
(p.219, Note 52)

### Note 53 — Disclosure of Leases
ROU asset and lease liability roll-forward (small balances, Rs.30-100 lakh
range); depreciation on ROU included in Note 37 depreciation expense.
(p.221, Note 53) 🟢 Clean, immaterial.

### Note 54 — Audit Trail
Accounting software has audit-trail (edit-log) feature enabled throughout
the year for all transactions, EXCEPT at the database level. Company states
shortcomings identified are "being reviewed" and corrective action is being
taken "wherever required." (p.221, Note 54) 🟡 Watch — a database-level
audit-trail gap is a specific, named control deficiency (common across many
Indian filers under this relatively new MCA requirement, not unique to
Orchid, but still a disclosed gap, not fully remediated as of the reporting
date).

### Note 55 — QIP Proceeds Utilisation (HIGH PRIORITY, directly explains the
capex/CWIP finding above)
FY2023-24: Company allotted 99,02,705 equity shares at Rs.10 face value via
QIP on 27-Jun-2023, raising net proceeds of Rs.39,180 lakhs (Rs.391.80 Cr,
net of Rs.805.79 lakhs share-issue expenses). As at 31-Mar-2025, entire net
proceeds received and monitored; utilisation as disclosed:
1. Investment in OBPL (Orchid Bio-Pharma Ltd, subsidiary) for setting up the
   Jamboo/Jambusar manufacturing facility: budgeted Rs.9,000 lakhs, utilised
   Rs.4,414 lakhs (49% utilised, Rs.45.86 Cr still to deploy from this
   bucket alone).
2. Repayment/prepayment of outstanding borrowings: budgeted Rs.14,100 lakhs,
   utilised Rs.14,100 lakhs (100% utilised).
3. Capex for a new block at the API facility in Alathur, Tamil Nadu:
   utilised Rs.8,294 lakhs against a budgeted figure that is OCR-illegible
   (NOT FOUND IN DOCUMENT: exact budgeted allocation for this line — the
   digit string is truncated/corrupted in extraction).
4. General corporate purposes: budgeted Rs.6,096 lakhs (originally, later
   revised to Rs.6,098 lakhs given a Rs.274 lakh surplus from a rounding/
   FX difference between proposed and actual net proceeds transferred),
   utilised Rs.637 lakhs.
Total: budgeted Rs.39,180 lakhs, utilised Rs.24,924 lakhs, UNUTILISED
balance Rs.14,530 lakhs (Rs.145.30 Cr) as at 31-Mar-2025, held in bank/fixed
deposits, earmarked. (p.222, Note 55) 🔴 Red Flag/High-value context — this
single note is the clearest documentary explanation for why consolidated
CWIP and capital commitments could move sharply in FY2026: Rs.145.30 Cr of
already-raised, already-in-hand QIP money remained undeployed as at the
FY2025 balance sheet date, earmarked substantially for the subsidiary's
manufacturing facility and the parent's own API facility expansion. This is
not a new capital raise required — the funding is already sitting on the
balance sheet, waiting to convert into CWIP.

### Note 56 — NCLT Amalgamation Petition (HIGH-VALUE STRUCTURAL FINDING)
Company has petitioned NCLT (Chennai bench) to amalgamate its OWN HOLDING
COMPANY, Dhanuka Laboratories Ltd, INTO itself (a reverse merger of parent
into listed subsidiary) under Sections 230-232 of the Companies Act.
Boards of both companies have approved the scheme. Stock exchanges (BSE,
NSE) have issued No-Objection observation letters. NCLT order dated
29-Apr-2025 (a subsequent event relative to the 31-Mar-2025 balance sheet
date) directs convening of meetings of equity shareholders and unsecured
creditors of Orchid, and dispenses with meetings for the Amalgamating
Company's shareholders and both companies' secured creditors (given their
consents already on file). Management is taking steps to comply with the
order. (p.222, Note 56) 🔴 Red Flag (structural, not a quality-of-earnings
flag) — a promoter/holding-company-into-listed-subsidiary reverse merger is
a major structural corporate action with real implications for RPT
treatment going forward (the DLL-related items flagged under Notes 22, 44,
50 above — the OCDs, the trade payables, the equity stake — would all
become intra-entity and disappear on consummation), for minority
shareholder swap-ratio fairness, and for the interpretation of every
DLL-related-party number in this pass once the scheme completes. This is
squarely a "flag prominently, decision stays human" item.

### Note 57-58 — Regrouping / Board Approval
Previous year figures regrouped/rearranged where necessary (standard,
no specifics quantified). Financial statements approved by the Board on
26-May-2025. (p.222, Notes 57-58) 🟢 Clean, standard closing notes.

---

## CROSS-REFERENCE: QUALIFIED AUDIT OPINION (NOT a "note," but directly
cited BY the notes and material to interpreting them)
The Independent Auditor's Report on the CONSOLIDATED financial statements
carries a QUALIFIED OPINION (not an emphasis of matter — a qualification).
Basis: the financial statements of four subsidiaries (Orchid Pharmaceuticals
Inc. USA, Bexel Pharmaceuticals Inc. USA, Orchid Pharmaceuticals SA
(Proprietary) Ltd South Africa up to 31-Jan-2025, Diakron Pharmaceuticals
Inc. USA) and the associate (Orbion Pharmaceuticals Private Ltd) are
UNAUDITED, furnished by management, and the auditor expresses NO opinion on
their completeness or true-and-fair view. Combined effect: total assets
Rs.349.09 lakhs, revenue from operations Rs.NIL, total comprehensive income
Rs.(634.35) lakhs for the year, cash flows Rs.NIL — all unaudited. The
report notes this SAME qualification has recurred across earlier years'
audits and limited-review reports, under the predecessor auditor too.
(Annual_Report_2025.pdf, p.225, Independent Auditor's Report on Consolidated
Financial Statements — "Qualified Opinion" / "Basis for Qualified Opinion")
🔴 Red Flag — a recurring, multi-year, unresolved audit qualification on
unaudited foreign subsidiary financial statements is a genuine corpus-level
red flag that the notes themselves reference (Note 3(c) revenue recognition
and Note 31 are cited as the linked Key Audit Matter). No SEBI order,
show-cause notice, or adjudication order text was found anywhere in either
annual report; the closest regulatory items found are two SMALL stock
exchange (BSE/NSE) fines disclosed in the corporate-governance section (not
the notes): Rs.44,000 each (Rs.88,000 total) for a 22-day delayed compliance
under Reg 17(1A) SEBI LODR concerning a non-executive director, and Rs.5,000
each (Rs.10,000 total) for delayed RPT-transaction filing under Reg 23(9)
SEBI LODR, both for FY2024-25, both paid. These are immaterial in rupee
terms but ARE the only regulatory-order-adjacent items in the corpus; no
SEBI adjudication order text itself is present (corpus-freshness gap per
orchestrator instruction 6).

---

## PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note Ref | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Consolidated capital commitments Rs.296.43 Cr (up ~9.6x from Rs.30.96 Cr FY2024); standalone only Rs.90.25 Cr — the Rs.206 Cr gap sits at subsidiary (Orchid Bio-Pharma) level | Note 44/45 (standalone p.208-209, consolidated p.264-265) | 🔴 Red Flag | Directly explains the screener-flagged FY2026 CWIP/borrowings surge; the capex programme is already committed, not speculative |
| 2 | Corporate guarantee of Rs.447.22 Cr given by parent for a wholly owned subsidiary's borrowings | Note 44, p.208-209 | 🔴 Red Flag | Large contingent exposure; if the subsidiary's capex-funded ramp underperforms, parent balance sheet absorbs the guarantee call risk |
| 3 | Intercompany loan to Orchid Bio-Pharma Ltd jumped from Rs.NIL to Rs.108.24 Cr within FY2025, with no disclosed interest rate, tenure, or repayment terms | Note 7 / Note 50, p.197, p.213-216 | 🔴 Red Flag | Material related-party funding flow with an undisclosed term structure; funds the same capex programme as findings 1-2 |
| 4 | QIP proceeds of Rs.391.80 Cr (raised Jun-2023): only Rs.249.24 Cr utilised by FY2025-end; Rs.145.30 Cr still undeployed, earmarked for the subsidiary facility and the Alathur API expansion | Note 55, p.222 | 🟡 Watch (positive context) | Explains funding source for the coming capex ramp — already-raised cash, not fresh dilution or fresh debt needed |
| 5 | NCLT petition to amalgamate the holding company (Dhanuka Laboratories Ltd) into the listed subsidiary (Orchid); NCLT order 29-Apr-2025 directing shareholder/creditor meetings | Note 56, p.222 | 🔴 Red Flag (structural) | Major corporate action that will collapse every DLL-related-party item (OCDs, trade payables, equity stake) on completion; swap-ratio fairness is a live minority-shareholder question |
| 6 | Qualified audit opinion on CONSOLIDATED financial statements — four foreign subsidiaries and one associate are unaudited, a recurring multi-year qualification | Auditor's Report, p.225 (cross-ref Note 3(c)/31) | 🔴 Red Flag | Unresolved audit scope limitation persisting across auditor changes; caps confidence in consolidated numbers |
| 7 | Net trade receivables grew 27.7% YoY against 12.5% revenue growth, while the ECL coverage ratio fell from 30.2% to 22.1% of gross receivables | Note 13, p.198 | 🔴 Red Flag | Cash-conversion deterioration plus simultaneously looser provisioning — feeds FLAG-CASH |
| 8 | Finished goods inventory grew 41.0% YoY against 12.5% revenue growth; total inventory +23.5% | Note 11, p.199 | 🔴 Red Flag | Second independent signal of a working-capital build running ahead of sales, consistent with company's own "Net Capital Turnover Ratio decreased" explanation in Note 52 |
| 9 | Related-party sale of goods to Orchid Pharma Inc. (US subsidiary, itself unaudited and near-zero third-party revenue per auditor's report) = ~25% of standalone revenue | Note 50, p.213-216 (cross-ref Auditor's Report p.225) | 🟡 Watch | Revenue quality question: a quarter of standalone revenue is intercompany with an entity whose own financials are unaudited and whose ultimate external sell-through is not disclosed |
| 10 | CSR shortfall: Rs.21.95 lakhs (65.8%) of the Rs.33.35 lakh FY2025 requirement unspent, with a mismatched footnote and no confirmation of statutory fund transfer | Note 46, p.209-210 | 🟡 Watch | Small in rupee terms but a named potential compliance gap under Section 135(5); also the first year CSR applied (threshold newly triggered), so a first-year miss is a governance signal to watch, not yet a pattern |

Honourable mentions not in the top 10 but flagged in-line above: the
0% OCD held by the holding company (11-16% IRR embedded cost, no stated
conversion ratio, no dilutive effect shown in EPS — a real question for
management); capital advances up ~742% YoY (second CWIP-ramp corroboration);
database-level audit-trail gap (Note 54); two small BSE/NSE compliance fines
(governance section, not notes, cross-referenced per orchestrator
instruction 6); the OCR-illegible standalone segment geography table
(Note 45) which should be re-pulled from source in Pass 2 rather than relied
upon as extracted.

---

```yaml
stage: B02-notes
company: "ORCHPHARMA"
run_date: "2026-09-06"
model: claude-sonnet-5
pass: 1
pass_status: complete
report_path: "/home/user/inflection-pipeline/runs/orchpharma-2026-09-06/outputs/reports/02-notes-pass1.md"
notes_covered: "Standalone Notes 1-58 (full); Consolidated Notes cross-referenced for 44/45/50/51/52/53 (capital commitments, borrowings, RPT, contingent liabilities, CWIP, receivables ageing) per orchestrator priority instruction"
ocr_quality_flag: "Numeric tables in both PDFs are heavily OCR-degraded (columns flattened, digits merged/dropped); narrative/policy text is legible. Cells not reconstructable with independent cross-check are marked NOT FOUND IN DOCUMENT rather than estimated, per the never-estimate rule. Pass 2/3 should re-pull the standalone segment geography table (Note 45) and PPE gross-block table (Notes 4-5) directly from source PDF pages if higher precision is required."
input_gaps:
  - "results: no quarterly or annual results filing in corpus"
  - "rating: no credit rating bulletin or rationale in corpus"
  - "announcements: no exchange / Reg 30 filings in corpus"
  - "shareholding: no quarterly shareholding pattern in corpus"
  - "research: no broker notes in corpus (non-anchored; no evidence effect)"
  - "screening: Profit_Loss, Balance_Sheet, Cash_Flow, Quarters CSVs are empty templates (collect_to_repo v3 defect); Data_Sheet used in their place"
  - "presentation: image-based, 3124 chars over 14 pages; treated as near-absent"
  - "FY2026 primary filings absent: no FY2026 annual report and no FY2026 audited annual results filing; FY2026 figures are screener aggregates only"
  - "regulatory: no SEBI order, show-cause notice, or adjudication order text found in either annual report; only two small BSE/NSE compliance fines (Rs.88,000 and Rs.10,000, both paid, both FY2024-25) found in the corporate-governance section, cross-referenced here per instruction but outside notes-to-accounts scope"
top_findings_count: 10
critical_flags_carried_forward:
  - "Consolidated capital commitments Rs.296.43 Cr vs standalone Rs.90.25 Cr (Note 44/45)"
  - "Corporate guarantee Rs.447.22 Cr for subsidiary borrowings (Note 44)"
  - "Intercompany loan to Orchid Bio-Pharma Ltd: Rs.NIL to Rs.108.24 Cr in one year, terms undisclosed (Note 7/50)"
  - "QIP proceeds Rs.145.30 Cr still undeployed at FY2025-end, earmarked for the capex ramp (Note 55)"
  - "NCLT petition to amalgamate holding company Dhanuka Laboratories Ltd into Orchid Pharma (Note 56)"
  - "Qualified audit opinion, consolidated FS, unaudited foreign subsidiaries, recurring multi-year (Auditor's Report p.225)"
  - "Receivables and finished-goods inventory both growing well ahead of revenue, provisioning loosening (Notes 11, 13) -> FLAG-CASH candidate"
receivables_trend: "deteriorating - net trade receivables +27.7% YoY vs revenue +12.5% YoY; ECL coverage fell from 30.2% to 22.1% of gross receivables (Note 13, Annual_Report_2025.pdf p.198)"
going_concern_language: "NONE found in either annual report's notes to financial statements"
```
