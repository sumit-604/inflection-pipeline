# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 2 (WHAT WAS MISSED)
Company: Orchid Pharma Ltd (ORCHPHARMA) | Run date: 2026-09-06 | Pass 2 of 3

## SCOPE AND METHOD

Re-read Standalone Notes 1-58 and the cross-referenced Consolidated Notes
against the Pass 1 report in full. Per the mandatory orchestrator
instructions, every one of Pass 1's seven carried-forward items and the two
stage-8 related-party items were re-verified directly against the source
PDF (not the OCR text layer) wherever the underlying page carries an
[OCR:embedded-CORRUPT] tag. That direct-PDF re-read is the source of every
figure below; page citations are PDF page-index numbers (matching the
convention Pass 1 and the text-extraction pipeline both use — note this
differs by exactly one from the printed footer number on every page checked,
e.g. PDF index 208 carries the printed footer "207 | Page"; this offset is
internally consistent and is not itself an error, just a reading note).

This pass surfaces two classes of finding: (A) genuinely NEW items Pass 1
did not report, and (B) CORRECTIONS to Pass 1 figures that do not survive
verification against the source PDF. Per the orchestrator's instruction to
"say so plainly rather than repeating" an unverifiable figure, corrections
are reported with the same weight as new findings, since several affect
numbers the orchestrator has already carried into cross-stage corrections
language.

---

## A. CORRECTIONS TO PASS 1 (verified against source PDF, not the corrupt OCR layer)

### A1. 🔴 MAJOR MISATTRIBUTION — the "Rs 230.72 Cr related-party revenue" is not
revenue, not a sale, and not to Orchid Pharma Inc.
Pass 1's Rank 9 finding and its Note 50 write-up state a "Related-party sale
of goods to Orchid Pharma Inc. (US subsidiary)... ~25% of standalone
revenue," Rs.23,072.00 lakhs FY2025 / Rs.17,012.94 lakhs FY2024.
Verified directly against Note 50(c) and 50(e) (Annual_Report_2025.pdf,
p.213-214, standalone; p.271 consolidated — all [OCR:embedded-CORRUPT] in
the text layer, confirmed by direct PDF read): this line is **Purchase of
goods from Otsuka Chemical (India) Pvt Ltd**, Rs.23,072.00 lakhs FY2025
(Rs.230.72 Cr) vs Rs.16,990.24 lakhs FY2024 (Rs.169.90 Cr), +35.8% YoY.
Otsuka is listed under "Enterprises in which the KMPs are having control/
significant influence" — Managing Director Manish Dhanuka and Wholetime
Director Mridul Dhanuka are Director/Member respectively of Otsuka
(cross-ref governance-section AGM Notice text, p.293-295, same corpus,
outside notes scope but directly explaining the relationship). Sale of
goods to **Orchid Pharma Inc. is Rs.NIL in both years** (Note 50(e), p.214).
This is exactly the Otsuka RPT the orchestrator flagged in instruction 3
(stage 8's Rs.230.72 Cr GCLE figure) — Pass 1 found the right rupee number
but attached it to the wrong counterparty and the wrong transaction
direction (purchase of a raw material the company is dependent on, not a
sale of finished goods). 🔴 Red Flag, corrected — Orchid buys its key raw
material GCLE (Otsuka is the sole approved source) from a KMP-controlled
entity at a value equal to ~25% of standalone revenue and rising 36% YoY,
against a business that itself declined ~12% on a like-for-like basis per
the orchestrator's Correction 1. Board approval was sought for RPTs with
Otsuka up to Rs.400 Cr for FY2025-26 (governance section, p.293-295 —
outside notes scope, cited for context only). The notes themselves state
only the transaction amount and relationship, no pricing basis; "arm's
length" and "competitive price" assertions live only in the AGM
Explanatory Statement (governance section), not in Note 50 itself — NOT
FOUND IN DOCUMENT: any fair-value or benchmarking disclosure for the
Otsuka purchase price within the notes to accounts.

### A2. 🟡 Trade payable of Rs.5,782.78 lakhs / Rs.6,212.93 lakhs belongs to
Otsuka, not Dhanuka Laboratories Ltd.
Pass 1 attributed this balance to "Trade payable to Dhanuka Laboratories
Ltd." Verified (Note 50(f), p.215 standalone / p.270 consolidated): the
actual Dhanuka Laboratories Ltd trade payable is Rs.264.36 lakhs FY2025 /
Rs.632.84 lakhs FY2024 — small. The Rs.5,782.78 lakhs (Rs.57.83 Cr) balance
is owed to Otsuka Chemical (India) Pvt Ltd, consistent with the large GCLE
purchase volume in A1 above and roughly 3 months of purchase value
outstanding. Same correction applies wherever Pass 1 cited "Rs.5,182.78
lakhs standalone / Rs.5,782.78 lakhs consolidated... trade payable to
Dhanuka Laboratories Ltd" — the Rs.5,782.78 lakhs figure is Otsuka's, the
Dhanuka Labs figure is Rs.264.36 lakhs (standalone, FY2025).

### A3. 🔴 Note 55 QIP utilisation table — two of four line items were misread.
Verified directly (Annual_Report_2025.pdf, PDF p.223 — printed footer
"222," [OCR:embedded-CORRUPT] in text layer):
| Bucket | Budgeted | Utilised (verified) | Utilised (Pass 1 said) | Balance |
|---|---|---|---|---|
| 1. OBPL Jamboo/Jambusar facility | Rs.9,000 lakhs | Rs.4,416 lakhs | Rs.4,414 lakhs (close) | Rs.4,584 lakhs |
| 2. Debt repayment | Rs.14,100 lakhs | Rs.14,100 lakhs | Rs.14,100 lakhs (correct) | Rs.NIL |
| 3. Alathur API block capex | Rs.9,982 lakhs | **Rs.36.00 lakhs** | Rs.8,294 lakhs (WRONG) | **Rs.9,946 lakhs** |
| 4. General corporate purposes | Rs.6,098 lakhs (revised) | **Rs.6,372 lakhs** | Rs.637 lakhs (WRONG) | Rs.NIL |
| Total | Rs.39,180 lakhs | Rs.24,924 lakhs | — | Rs.14,530 lakhs |
The total unutilised figure Rs.14,530 lakhs (Rs.145.30 Cr) that Pass 1 and
the orchestrator's carried-forward item both cite is CORRECT at the total
level. But the composition is materially different from what Pass 1
reported: the Alathur API-facility expansion — the parent company's OWN
capex line, not the subsidiary's — has barely been touched (0.36%
utilised, Rs.99.46 Cr of the Rs.145.30 Cr unspent balance sits here alone),
while general corporate purposes is fully spent (not barely touched, as
Pass 1's Rs.637 lakh reading implied). This changes the read on where the
FY2026 capex ramp is actually funded from: predominantly the untouched
Alathur bucket plus the still-49%-utilised OBPL bucket, not a broadly
spread partial utilisation. 🔴 Red Flag, corrected — same overall
"cash in hand, not fresh capital needed" conclusion holds, but the specific
funding-readiness story per line does not match Pass 1's numbers.

### A4. 🟡 Consolidated capital commitments: Rs.298.43 Cr, not Rs.296.43 Cr.
Verified directly (Annual_Report_2025.pdf, PDF p.263 — printed footer
"263," this specific line was legible enough to read with confidence
despite the page's [OCR:embedded-CORRUPT] tag): "Estimated amount of
contracts remaining to be executed on capital account and not provided"
= **Rs.29,842.89 lakhs** (Rs.298.43 Cr) as at 31-Mar-2025, vs Rs.3,096.11
lakhs (Rs.30.96 Cr) FY2024. Pass 1 (and the orchestrator's own
cross-stage corrections memo) cite Rs.29,642.89 lakhs / Rs.296.43 Cr — a
single-digit OCR misread (642 vs 842) on the orchestrator's own priority-1
number. The YoY multiple (~9.64x) and the qualitative story (subsidiary-
level capex commitment dwarfing the standalone Rs.90.25 Cr figure) are
unaffected; only the absolute rupee figure changes, by Rs.2 Cr. Gap versus
standalone (Rs.9,024.80 lakhs, confirmed correct) is Rs.20,818.09 lakhs
(Rs.208.18 Cr), not Rs.206 Cr. 🟡 Watch, corrected — small in absolute terms
but this is the exact number multiple later-stage reports and the
orchestrator's own corrections file already carry forward; downstream
stages citing "Rs.296.43 Cr" should be pointed to the corrected Rs.298.43 Cr.

### A5. 🟡 Note 48 OCD redemption premium: range is 11%-18% IRR, not
11%-16% IRR.
Verified directly (Annual_Report_2025.pdf, PDF p.210, printed footer
"209," [OCR:embedded] this specific page rendered legibly on direct read):
"...shall not exceed beyond **18%** IRR on an annual basis." Pass 1 stated
a 16% cap. Also confirmed: the conversion basis stated in the notes
themselves is only "on the basis of face value of each of the OCD" — the
notes do NOT state a per-equity-share conversion price or ratio anywhere
in Note 22, 48, or 50. NOT FOUND IN DOCUMENT (unchanged from Pass 1):
the specific conversion ratio / per-share price. The "Rs.10 per share"
figure the orchestrator's Correction 4 carries must therefore trace to a
document outside the FY2025 notes (likely the original 2020 issuance
terms), not to anything in this annual report's notes to accounts.

### A6. 🟢 Note 44 standalone commitments/contingencies — FY2024 comparatives
now confirmed (Pass 1 reported several as absent or NIL).
Verified directly (Annual_Report_2025.pdf, PDF p.208, printed footer "207"):
- Electricity Department claim: Rs.112.44 lakhs FY2025 vs **Rs.80.93 lakhs
  FY2024** (Pass 1 said FY2024 was NIL — it was not; the claim grew ~39%
  YoY, both years disputed from 01.04.2020).
- Unexpired LC/BG: Rs.373.20 lakhs FY2025 vs **Rs.964.65 lakhs FY2024**
  (down 61% YoY — new comparative Pass 1 lacked).
- Capital commitments: Rs.9,024.80 lakhs FY2025 vs **Rs.1,006.11 lakhs
  FY2024** — standalone capital commitments rose **~797% YoY within
  FY2025 itself**, a figure Pass 1 could not compute because it lacked the
  comparator. This is a second, independent (standalone-level, not just
  consolidated) confirmation of the capex ramp already flagged.
- Corporate Guarantee for the wholly owned subsidiary: **Rs.44,722.00
  lakhs FY2025 vs Rs.NIL FY2024** — confirmed brand-new this year, not
  merely "given" as Pass 1's phrasing suggested. Zero to Rs.447.22 Cr of
  contingent exposure in a single reporting year.
See finding B3 below for the "Other claims" line, which is new, not a
correction.

---

## B. NEW FINDINGS (not reported in Pass 1)

### B1. 🔴 A Rs.38.72 Cr standalone contingent claim vanished from disclosure
between FY2024 and FY2025 on management's own legal opinion, while the
counterparty is still actively disputing part of the same matter.
Note 44 standalone, "Other claims **" line: Rs.NIL FY2025 vs **Rs.3,871.68
lakhs FY2024** (Rs.38.72 Cr) (Annual_Report_2025.pdf, PDF p.208-209,
printed footer 207-208). The "**" footnote is the SAME footnote covering
the pre-CIRP land lease dispute described elsewhere in Note 44 (already
flagged by Pass 1): a Joint Memo of Compromise dated 8-Apr-2025 (a
subsequent event) settled the POST-CIRP portion for Rs.762 lakhs, fully
provided for. The PRE-CIRP portion — where "the Lessor continues to
dispute and claim the Lease Rent" — management asserts is extinguished by
the NCLT-approved Resolution Plan and is NOT carried as a contingent
liability at all in FY2025, down from Rs.3,871.68 lakhs disclosed as
"Other claims" the prior year. Only Rs.762 lakhs was actually paid/
provided; the remaining ~Rs.31 Cr of previously disclosed exposure is
removed from the accounts on management's own reading of the resolution
plan, not by a court ruling or a second settlement. The consolidated
figures corroborate the arithmetic cleanly: consolidated "Other claims"
Rs.4,251.46 lakhs FY2024 = Rs.3,871.68 lakhs (this standalone item,
resolved to NIL) + Rs.379.78 lakhs (a flat, unchanged subsidiary-level
claim per the consolidated footnote, "Rs.379.78 Lakhs (Previous year
Rs.379.78 Lakhs)" — Annual_Report_2025.pdf, PDF p.263) = consolidated
"Other claims" of Rs.379.78 lakhs FY2025. 🔴 Red Flag — a large legacy
contingent liability was removed from disclosure based on the company's
own legal position on an actively disputed matter; the note nowhere
states an independent legal opinion was obtained, and the counterparty's
active dispute is acknowledged in the company's own text.

### B2. 🟡 Interest income and guarantee-commission income on the Orchid
Bio-Pharma related-party exposures — the loan and the guarantee are not
free of charge, even though no rate is disclosed.
Note 50(e), Annual_Report_2025.pdf, PDF p.214 (printed footer "213"):
- **Interest received** on the loan to Orchid Bio-Pharma Ltd: **Rs.466.35
  lakhs FY2025** vs Rs.13.33 lakhs FY2024.
- **Corporate guarantee commission received** from Orchid Bio-Pharma Ltd
  for the Rs.44,722.00 lakh guarantee: **Rs.527.72 lakhs FY2025** vs
  Rs.NIL FY2024 (~1.18% of guarantee face value).
- "Loan Given" during the year (disbursement, distinct from closing
  balance): Rs.10,035.35 lakhs — reconciles against the Rs.108.24 Cr
  closing balance less the Rs.7.89 Cr FY2024 current-portion carryover
  Pass 1 already identified.
This corrects the IMPLICATION (not the literal statement) in Pass 1's
Note 7 write-up that the loan carries no economic terms at all. The rate
itself is still NOT FOUND IN DOCUMENT (no % stated anywhere), but interest
IS being charged and received, and the guarantee IS being compensated.
🟡 Watch, upgraded from Pass 1's framing — worth a rough sanity check for
management: Rs.466.35 lakhs of interest on an opening-to-closing balance
that built from Rs.7.89 Cr to Rs.108.24 Cr over the year implies a
plausible commercial rate if the bulk of the Rs.100.35 Cr disbursement
landed early in the year, but the notes give no drawdown-date detail to
confirm this — NOT FOUND IN DOCUMENT: disbursement dates.

### B3. 🟡 The financial guarantee (Rs.447.22 Cr) has no visible Ind AS 109
fair-value treatment.
Ind AS 109 ordinarily requires a financial guarantee contract to be
initially recognised at fair value, with a corresponding liability
amortised over the guarantee period. No such liability appears in Notes
23/24 (Provisions) or elsewhere in the standalone balance sheet notes;
the Rs.527.72 lakhs guarantee commission (B2 above) reads as commission
income recognised on receipt/accrual rather than an amortising fair-value
liability being unwound. Note 3 (Material Accounting Policies,
Annual_Report_2025.pdf, p.184-194) does not separately address financial
guarantee contracts as a policy category. 🟡 Watch — NOT FOUND IN DOCUMENT:
initial fair-value recognition or amortisation policy for the guarantee;
worth a question for management, particularly given the guarantee is
~34% of standalone total equity (Rs.44,722.00 lakhs / Rs.1,32,404.91
lakhs, Note 49).

### B4. 🟡 Note 45 standalone segment geography table: the "OCR/arithmetic
inconsistency" Pass 1 flagged is RESOLVED, not a real inconsistency —
but a smaller genuine gap survives.
Verified directly (Annual_Report_2025.pdf, PDF p.209, printed footer
"208"): India Rs.18,091.22 lakhs, Rest of World **Rs.72,823.17 lakhs**
(not Rs.12,823.17 lakhs as the OCR extraction gave Pass 1), total
Rs.90,914.39 lakhs. 18,091.22 + 72,823.17 = 90,914.39 — the table
reconciles exactly once read from source; Pass 1's flagged inconsistency
was an OCR artefact, not a company error, and should be retracted rather
than carried forward as a red flag. A smaller, GENUINE gap remains
unexplained: segment/geography revenue totals Rs.909.14 Cr against total
revenue from operations of Rs.921.93 Cr (Note 31) — a Rs.12.78 Cr
difference, most likely export incentives or other operating income not
geographically allocated, but NOT FOUND IN DOCUMENT as a stated
reconciling item. Consolidated Note 46 carries the identical India/RoW
split (Annual_Report_2025.pdf, PDF p.264), confirming the geography note
is parent-entity-only regardless of consolidation scope, consistent with
Note 46's own single-segment / single-entity manufacturing-location
statement.

### B5. 🟢 Note 51 actuarial assumptions, now found (Pass 1 flagged as
OCR-illegible and deferred).
Verified directly (Annual_Report_2025.pdf, PDF p.217, printed footer
"216"): Discount rate 6.70% FY2025 vs 7.19% FY2024 (down 49bps, tracking
government bond yields); salary growth 7.00% both years; attrition rate
15.00% both years; mortality Indian Assured Lives Mortality (2012-14)
Ultimate, both years. Routine, no red flag; closes Pass 1's open item.

### B6. 🟡 Consolidated income tax and EPS are NOT the clean NIL/flat picture
Pass 1's blanket statement implied — and the gap bridges cleanly to the
qualified-audit-opinion subsidiaries.
Pass 1 stated "Profit before tax = profit after tax (income tax expense
NIL both years)" without separately flagging that this is a STANDALONE-
only fact. Consolidated Note 40/41 (Annual_Report_2025.pdf, PDF p.263,
printed footer "262"): income tax expense Rs.NIL FY2025 / Rs.10.71 lakhs
FY2024, plus "Income tax for earlier years" Rs.(9.23) lakhs FY2025 (a
credit) / Rs.NIL FY2024 — net Rs.(9.23) lakhs FY2025 / Rs.10.71 lakhs
FY2024, immaterial but not literally NIL both years at consolidated
level. Consolidated Basic = Diluted EPS Rs.19.65 FY2025 / Rs.19.06 FY2024
(Note 42 consolidated, same page) versus standalone Basic = Diluted EPS
Rs.20.99 FY2025 / Rs.19.59 FY2024 (Note 41 standalone, already in Pass 1).
Cross-checking the two disclosed numbers (both independently sourced, not
estimated): standalone retained-earnings roll-forward (Note 21,
Rs.(1,98,838.29) lakhs opening less Rs.(1,88,259.90) lakhs closing =
Rs.10,578.39 lakhs implied standalone FY2025 profit) against consolidated
profit attributable to owners of Rs.9,965.68 lakhs (Note 42 consolidated)
leaves a **Rs.612.71 lakh gap** — close to, though not identical to, the
Rs.634.35 lakhs total comprehensive loss the auditor's qualified opinion
attributes to the four unaudited foreign subsidiaries plus the associate
combined (Annual_Report_2025.pdf, p.225, already flagged by Pass 1 as a
red flag in isolation). This is a computed cross-check across two
disclosed figures, not a number stated anywhere in the document as a
bridge — flagged as [INFERENCE, not a filed reconciliation] — but it is
the first time in this pass sequence that the qualified-opinion
subsidiaries' loss is connected quantitatively to the consolidated
earnings gap. 🟡 Watch.

### B7. 🟢 Quant Mutual Fund is the only disclosed non-promoter shareholder
above 5%, unchanged both years.
Note 20(c), Annual_Report_2025.pdf, PDF p.202 (printed footer "201"):
Quant Mutual Fund holds 34,65,947 shares = 6.83% of paid-up capital,
identical FY2025 and FY2024. This partially fills the input_gaps
"shareholding: no quarterly shareholding pattern in corpus" note with a
static annual-report-date data point (not a substitute for a quarterly
pattern). 🟢 Clean, informational.

### B8. 🟡 A materially larger, resolved regulatory action than Pass 1's two
small fines — and an internal inconsistency in how the annual report
itself discloses penalties.
Outside the notes to accounts strictly, but directly responsive to
orchestrator instruction 4 ("confirm or extend" the regulatory-order
finding). Corporate Governance Report (Annual_Report_2025.pdf, text-extract
lines ~5900-5953, [OCR:embedded], legible): following CIRP, promoter
shareholding stood at 90% (10% public) against a 25% Minimum Public
Shareholding requirement. Stock Exchanges, acting under a SEBI circular,
**froze promoter shareholding** and barred the promoter, promoter group
and directors from taking new directorships at any other listed entity
until compliance, effective from a letter dated 20-Apr-2023. Penalties
levied and paid: Rs.5,000 + GST (period to 31-Mar-2023) and **Rs.5,19,200**
(1-Apr-2023 to 26-Jun-2023) — an order of magnitude larger than the two
Reg 17(1A)/Reg 23(9) fines (Rs.88,000 and Rs.10,000) Pass 1 already found
for FY2024-25. Compliance was restored only via the Jun-2023 QIP
allotment (the same QIP whose unutilised Rs.145.30 Cr balance is Pass 1's
Rank 4 finding). This is HISTORICAL (FY2023, resolved before the FY2025
reporting year) and not a live compliance gap, but it is the correct
"largest regulatory action in the corpus" answer to the orchestrator's
question, and Pass 1's "no SEBI order... found" framing should be
qualified: no SEBI *adjudication order text* is present (still true), but
a SEBI-circular-driven shareholding freeze is disclosed and is materially
larger than what Pass 1 reported. Separately, and still within this same
annual report: the Business Responsibility and Sustainability Report
(BRSR) section's own standard "Penalty/Fine" disclosure table states
**"Nil"** for monetary penalties (text-extract line ~7407), which is
inconsistent with the Corporate Governance Report's own disclosure of
Rs.88,000 + Rs.10,000 in FY2024-25 stock-exchange fines in the SAME
annual report. 🟡 Watch — an internal disclosure inconsistency between two
sections of the same filing, worth naming even though neither individual
figure is large.

---

## PASS 2 NEW FINDINGS SUMMARY

Eight new findings (B1-B8) and six corrections to Pass 1 figures (A1-A6),
all sourced from direct PDF reads where the underlying page carries an
[OCR:embedded-CORRUPT] tag, per the mandatory orchestrator instruction.
The single most consequential item is A1/A2: Pass 1's Rank 9 finding
described a related-party SALE to a loss-making US subsidiary; the
verified fact is a related-party PURCHASE of the company's sole-sourced
key raw material from a KMP-controlled domestic entity, equal to ~25% of
standalone revenue and growing 36% YoY against a business that itself
declined ~12% (orchestrator Correction 1). This changes the character of
the RPT concern from "revenue quality" to "cost-side dependency and
related-party pricing on an unsubstitutable input," and should replace
Pass 1's Rank 9 item in the Pass 3 consolidated top-15, not sit alongside
it as a separate line.

The two carry-forward items independently re-verified as correct at
source, unchanged from Pass 1: the Rs.108.24 Cr intercompany loan (already
independently confirmed per the orchestrator's own instruction 2), and the
Rs.145.30 Cr unutilised QIP balance at the TOTAL level (though its
composition is corrected in A3). The one carry-forward item corrected at
the digit level is the consolidated capital commitments figure: Rs.298.43
Cr, not Rs.296.43 Cr — downstream stages and the orchestrator's own
corrections file should be pointed to the corrected figure.

---

```yaml
stage: B02-notes
company: "ORCHPHARMA"
run_date: "2026-09-06"
model: claude-sonnet-5
pass: 2
pass_status: complete
pass_2_empty: false
report_path: "/home/user/inflection-pipeline/runs/orchpharma-2026-09-06/outputs/reports/02-notes-pass2.md"
verification_method: "Direct source-PDF read (Read tool, pages parameter) for every page underlying a Pass 1 finding that carried an [OCR:embedded-CORRUPT] tag, per mandatory orchestrator instruction; page anchors below are PDF page-index numbers, which run one higher than the printed footer number on every page checked in this pass (internally consistent, not an error)."
new_findings_count: 8
corrections_to_pass1_count: 6
major_correction:
  finding: "Pass 1 Rank 9 misattributed a Rs.230.72 Cr FY2025 related-party transaction as a SALE of goods to Orchid Pharma Inc (US subsidiary). Verified at source (Note 50(e), Annual_Report_2025.pdf p.213-214): it is a PURCHASE of GCLE (sole-sourced key raw material) from Otsuka Chemical (India) Pvt Ltd, an entity where MD Manish Dhanuka and WTD Mridul Dhanuka hold director/member positions. Sale of goods to Orchid Pharma Inc is Rs.NIL both years. The associated Rs.5,782.78 lakhs / Rs.6,212.93 lakhs trade payable Pass 1 attributed to Dhanuka Laboratories Ltd also belongs to Otsuka; Dhanuka Labs' actual trade payable is Rs.264.36 lakhs FY2025."
  rating: "RED FLAG, corrected"
carried_forward_items_status:
  - {item: "Consolidated capital commitments", pass1_figure: "Rs.296.43 Cr", verified_figure: "Rs.298.43 Cr (Rs.29,842.89 lakhs)", status: "corrected, digit-level OCR error"}
  - {item: "Corporate guarantee Rs.447.22 Cr for subsidiary borrowings", pass1_figure: "given", verified_figure: "Rs.NIL FY2024 to Rs.44,722.00 lakhs FY2025 -- confirmed brand new this year", status: "confirmed, sharpened"}
  - {item: "Intercompany loan to Orchid Bio-Pharma Ltd, Rs.NIL to Rs.108.24 Cr", pass1_figure: "no interest rate disclosed", verified_figure: "rate still not stated, but interest RECEIVED Rs.466.35 lakhs FY2025 (Rs.13.33 lakhs FY2024) and guarantee commission Rs.527.72 lakhs FY2025 are both disclosed", status: "confirmed, qualified"}
  - {item: "QIP proceeds Rs.145.30 Cr still undeployed at FY2025 close", pass1_figure: "total confirmed, component split partly illegible", verified_figure: "total confirmed correct; Alathur API-block bucket (Rs.99.46 Cr of the Rs.145.30 Cr) barely touched at 0.36% utilised, not ~83% utilised as Pass 1's misread implied", status: "total confirmed, composition corrected"}
  - {item: "NCLT petition to amalgamate Dhanuka Laboratories into Orchid Pharma", pass1_figure: "confirmed", verified_figure: "confirmed unchanged", status: "confirmed"}
  - {item: "Qualified audit opinion on consolidated statements over unaudited foreign subsidiaries", pass1_figure: "confirmed", verified_figure: "confirmed; new B6 finding computes a Rs.612.71 lakh standalone-vs-consolidated PAT gap that plausibly bridges to the Rs.634.35 lakh combined loss of the unaudited entities [INFERENCE, not a filed reconciliation]", status: "confirmed, extended"}
  - {item: "Receivables and finished goods growing ahead of revenue, ECL coverage 30.2% to 22.1%", pass1_figure: "confirmed at source in this pass (Note 13, Note 11 both directly re-read)", verified_figure: "unchanged", status: "confirmed"}
regulatory_extension: "A FY2023 Minimum Public Shareholding non-compliance drove a stock-exchange freeze on promoter shareholding and a Rs.5,19,200 penalty (plus Rs.5,000+GST), materially larger than the two FY2024-25 fines Pass 1 found; historical and resolved, not a live gap. Separately, the annual report's own BRSR Penalty/Fine table states Nil, inconsistent with the Corporate Governance Report's own disclosure of Rs.88,000+Rs.10,000 FY2024-25 fines in the same filing. Still NOT FOUND IN DOCUMENT: any SEBI adjudication-order text itself."
receivables_trend: "deteriorating - unchanged from Pass 1, re-confirmed at source: net trade receivables +27.7% YoY vs revenue +12.5% YoY; ECL coverage fell from 30.2% to 22.1% of gross receivables (Note 13, Annual_Report_2025.pdf PDF p.199, printed footer 198)"
going_concern_language: "NONE found in either annual report's notes to financial statements or auditor's reports, re-confirmed by direct read of the standalone auditor's-responsibilities paragraphs and the Director's Report 'Significant and Material Orders' section (both boilerplate, no qualification, no emphasis of matter)"
```
