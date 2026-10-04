# TITANBIO: operator extraction, 2026-10-04

Run: runs/titanbio-2026-09-10 | Branch: run/titanbio-phase1-2026-09-16
Mode: corpus only. Quote, then comment. Every number carries its page anchor.
NOT DISCLOSED where the corpus is silent, with the place it would be found.

Page convention. "PDF p." is the page of the PDF file in inputs/. The annual
report's printed folio runs two lower than its PDF page (AR FY26 PDF p.117 prints as
115). Results filings carry no printed folio; the PDF page is the only anchor.

Figures read from the page images, not the OCR text layer, which garbles the
results filings. All figures are standalone, Rs lakh, unless marked.

---

## 1. Two cash flow resolutions

### 1(a) Operating cash flow: Rs 3,042.08 lakh, not Rs 3,896.91 lakh

Quote, FY26 results filing, standalone cash flow statement (2026-05-30_FY26_audited_results.pdf, PDF p.10):

> "Cash generation from operation 3,896.91 | 2,611.28"
> "Less: Income tax paid (854.83) | (598.95)"
> "Net Cash generated/ (used) - Operating Activities 3,042.08 | 2,012.33"

The consolidated statement carries the same three lines (same file, PDF p.18). The
annual report repeats them (AR FY26 PDF p.117 standalone, PDF p.162 consolidated).

Quote, FY26 MD&A (AR FY26 PDF p.104):

> "The data given in Table A, Cash generated from operating activities in FY 2026 was Rs. 3,896.91 Lacs."
> "i. Operating Activities 3,896.91 2,611.28"

Comment. RESOLVED. Audited net cash from operating activities is Rs 3,042.08 lakh in
FY26 and Rs 2,012.33 lakh in FY25. The MD&A Table A row labelled "Operating
Activities" carries the PRE-TAX line "Cash generation from operation", Rs 3,896.91
lakh, before income tax paid of Rs 854.83 lakh. It is a mislabel, not a second
number. The FY25 MD&A did the same for FY24 (Verifier B: AR FY2025 p.100 shows
Rs 2,901.66 lakh against AR FY2024's Rs 2,114.63 lakh), so the mislabel is a repeat.

Effect on the run. Verifier B's CRITICAL is resolved as a disclosure defect in the
MD&A, not an unknown in the cash flow. Every downstream stage uses Rs 3,042.08 lakh.
CFO over PAT is 3,042.08 / 2,744.72 = 1.11x in FY26 and 2,012.33 / 1,827.11 = 1.10x
in FY25 (PAT, results filing PDF p.7), so the stage claim "CFO over PAT above 1.0x
both years" stands.

### 1(b) The Rs 186.90 lakh investing gap is a non-cash right-of-use addition

Quote, results filing standalone cash flow (PDF p.10), investing section:

> "(Addition) in right of use assets (186.90) | (2.13)"
> "Net Cash Generated/ (Used) - Investing Activities (3,441.49) | (987.47)"

and financing section:

> "Repayment of Lease Liabilities 134.19 | (43.75)"
> "Net cash (used) - financing activities 34.39 | (796.08)"

Quote, annual report standalone cash flow (AR FY26 PDF p.117):

> "Net cash (used) - investing activities (3,254.59) (985.34)"
> "Repayment of Lease Liabilities (52.71) (43.75)"
> "Net cash (used) - financing activities (152.51) (798.21)"

Quote, AR FY26 Note 3, Right-of-use assets (PDF p.127):

> "Office premises (Commercial) 229.03 186.90 186.30 229.63"

(gross opening, additions, disposals, gross closing; the disposed Rs 186.30 lakh was
fully amortised, so it is a lease renewal on the same office premises)

Quote, AR FY26 Note 42 maturity table (PDF p.150): lease liabilities Rs 69.45 lakh
at 31-Mar-2025 and Rs 203.65 lakh at 31-Mar-2026.

Comment. RESOLVED. Neither filing is wrong on totals; they present one non-cash event
two ways.
- The results filing grosses the new office lease through cash flow: Rs 186.90 lakh
  out under investing, and a net Rs 134.19 lakh IN under financing (new lease
  liability 186.90 less cash repaid 52.71).
- The annual report excludes the non-cash lease addition from both sections and shows
  only the Rs 52.71 lakh cash repaid.
- Arithmetic proof: 3,441.49 less 3,254.59 = 186.90 on investing; 34.39 less
  (152.51) = 186.90 on financing. Both statements close at a net decrease of
  Rs 365.02 lakh and closing cash of Rs 147.77 lakh.
- Lease liability roll: 69.45 opening + 186.90 new lease less 52.71 repaid = 203.64,
  against 203.65 closing. Rounding only.

The annual report treatment is the correct Ind AS 7 one: a lease addition financed by
a lease liability is non-cash. Use Rs 3,254.59 lakh as FY26 cash investing outflow.
The MD&A again quotes the results-filing figure (Rs 3,441.49 lakh) and the
results-filing financing figure ("Cash inflow from financing activities was Rs. 34.39
Lakhs", PDF p.104) inside an annual report whose own audited statement says otherwise.
That is the third MD&A-versus-audited mismatch on the same page.

Verifier disagreement log and gate recommendation updated in this commit.

---

## 2. The Rs 2,515.67 lakh investment line, split

Quote, results filing standalone cash flow (PDF p.10):

> "Investments in debt instruments quoted and unquoted equity instruments (2,515.67) | (131.66)"

Quote, AR FY26 Note 5, Investments (PDF p.128):

> Associates, fully paid-up: "Peptech Biosciences Limited 10.00 44,24,990 1230.01 12,74,940 127.49"; "Titan Media Limited 10.00 100 0.02 100 0.02"
> Associates, partly paid-up: "Peptech Biosciences Limited 10.00 - - 31,50,050 1,102.52"; "Titan Media Limited 10.00 33,90,510 406.86 33,90,510 406.86"
> Equity total: "78,15,600 1636.89 78,15,600 1,636.89"
> FVTPL: "Investments in debt instruments quoted, fully paid up 3,328.78 813.10"

| Line | 31-Mar-2025 | 31-Mar-2026 | Change | Anchor |
|---|---|---|---|---|
| Equity, Peptech Biosciences (associate, at cost) | 1,230.01 | 1,230.01 | NIL | AR FY26 PDF p.128 |
| Equity, Titan Media Ltd (associate, at cost) | 406.88 | 406.88 | NIL | AR FY26 PDF p.128 |
| Equity total at cost | 1,636.89 | 1,636.89 | 0.00 | AR FY26 PDF p.128 |
| Debt instruments, quoted, FVTPL | 813.10 | 3,328.78 | +2,515.68 | AR FY26 PDF p.128 |
| **Cash flow line** | | | **(2,515.67)** | Results PDF p.10; AR PDF p.117 |

Comment.
- DEBT: Rs 2,515.67 lakh, all of it. EQUITY: NIL. The equity book at cost is
  Rs 1,636.89 lakh at both year ends, so no rupee of the FY26 line went into equity.
- PEPTECH: 31,50,050 partly paid shares moved into the fully paid line in FY26 at an
  unchanged Rs 1,102.52 lakh. The call money was paid in FY25: the same holding stood
  at Rs 551.26 lakh on 31-Mar-2024 and Rs 1,102.52 lakh on 31-Mar-2025 (AR FY25 PDF
  p.123). FY26 is a reclassification, not a payment.
- TITAN MEDIA calls paid in FY26: NIL. The 33,90,510 partly paid shares stand at
  Rs 406.86 lakh at both FY26 year ends. The first call was paid in FY25: Rs 203.43
  lakh on 31-Mar-2024, Rs 406.86 lakh on 31-Mar-2025 (AR FY25 PDF p.123; AR FY24 PDF
  p.129). Quote, Reg 30 filing of 28-Feb-2025 (filed in the corpus under the wrong
  name 2025-02-28_arbitration-update.pdf, PDF p.1): "Investee Company has called the
  1st call ("Tranches 2") on remaining capital. The Company has paid the 1st call
  money. Resulting, the Company's voting right in Investee Company stands increased
  to 48.44% (from 32.29% at the time of our investment in February 2024)."
- UNCALLED LIABILITY: "Uncalled liability on partly paid-up shares 406.86 682.49"
  (AR FY26 Note 36(II) Commitments, PDF p.142). With Peptech now fully paid, the
  Rs 406.86 lakh at 31-Mar-2026 can only sit on the Titan Media partly paid shares.
  That is a future cash call on the company, not yet paid.
- The FY25 line (131.66) nets two flows: equity calls of Rs 754.69 lakh (Peptech
  551.26 + Titan Media 203.43) against a debt reduction of Rs 623.03 lakh
  (1,436.13 less 813.10). Arithmetic: 754.69 less 623.03 = 131.66.
- Every equity investee in the book: Peptech Biosciences Ltd and Titan Media Ltd.
  There is no other equity investment, quoted or unquoted, in Note 5.

Two limits, stated rather than estimated.
- The Rs 2,515.67 lakh equals the change in the debt book's CARRYING value. FY26
  other income includes a "Net gain or (losses) on fair value changes" of Rs 116.96
  lakh (AR FY26 Note 24, PDF p.136), and the operating section adds no adjustment for
  it (PDF p.117). If that gain sits inside the closing Rs 3,328.78 lakh, cash bought
  is lower than Rs 2,515.67 lakh by up to Rs 116.96 lakh. The realised versus
  unrealised split is NOT DISCLOSED. It would be found in a fair value hierarchy
  roll-forward or an investment movement schedule, neither of which the AR prints.
- The debt issuers are NOT DISCLOSED. Note 5 gives one line, "quoted, fully paid
  up". They would be found in the company's investment register, or as a direct
  question to the company.

---

## 3. When freight entered revenue, and whether Q1 FY26 was regrouped

Quote, Q3 FY25 results, the integrated filing of 13-Feb-2025
(announcements/2025-02-13_integrated-filing-financial.pdf), standalone extract,
PDF p.4, note 5:

> "Freight amount has been added in revenue from operations for the purpose of calculation of sales including GST in current year. Freight also added in total in other expenses to neutralise the impact of its addition in revenue in current year."

The same sentence is note 7 of the full consolidated statement on PDF p.5 of the same
filing, dated 12-Feb-2025, for the quarter and nine months ended 31-Dec-2024.

The same sentence appears, word for word, in every later results filing in the corpus:
Q2 FY26 (PDF p.4, note 6), Q3 FY26 (PDF p.4, note 6), FY26 (PDF p.7, note 6),
Q1 FY27 (PDF p.4, note 5). It appears in none of the three annual reports (a search of
AR FY24, FY25 and FY26 finds it nowhere).

Answer to "which quarter did freight first enter": the corpus cannot pin the quarter.
The EARLIEST filing in the corpus that carries the note is the Q3 FY25 filing,
covering the quarter ended 31-Dec-2024, and its "current year" is FY2024-25. Freight
was therefore inside reported revenue no later than FY25, and on the note's own words
for the whole of FY25. Whether it entered in Q1 FY25 or earlier is NOT DISCLOSED in
the corpus. It would be found in the Q1 FY25 and Q2 FY25 results filings (Aug-2024 and
Nov-2024) and the FY24 audited results (May-2024), none of which the corpus holds.

Answer to "was Q1 FY26 regrouped": no regrouping is visible between filings. Q1 FY26
reads identically in both filings that carry it:

| Line, quarter ended 30-Jun-2025 | Q2 FY26 filing, PDF p.4 | Q1 FY27 filing, PDF p.4 |
|---|---|---|
| Revenue from operations | 4,649.64 | 4,649.64 |
| Cost of materials consumed | 1,855.28 | 1,855.28 |
| Changes in inventories | 539.67 | 539.67 |
| Other expenses | 679.66 | 679.66 |
| Profit for the period | 616.08 | 616.08 |

The FY25 comparatives also carry forward unchanged. Q2 FY25 total income reads
4,020.97 and Q3 FY25 3,986.53 in the 13-Feb-2025 filing (PDF p.4) and in the Q2 FY26
and Q3 FY26 filings (PDF p.4 each). Q2 FY25 and Q3 FY25 revenue from operations read
3,989.11 and 3,827.58 in the consolidated statement of the 13-Feb-2025 filing (PDF
p.5) and in both later filings.

The Q1 FY26 figure as FIRST published, in the results filing of 13-Aug-2025, is not
in the corpus. NOT DISCLOSED in corpus; it is BSE attachment
aa5cb05e-a85a-426b-b094-69afc1810339.pdf. That filing is the one document that would
show whether the Nov-2025 column differs from the original.

Comment, and it reverses a run finding.
- The run's FLAG-REVENUE-BASIS rested on one premise: freight entered revenue in FY26
  and FY25 was not restated, so reported FY26 growth of 31.79% was really 28.06% like
  for like. The Feb-2025 filing breaks the premise. The same freight note governed
  FY25. FY25 and FY26 sit on the same presentation, and the FY25 figures in the FY26
  filings match the FY25 figures as first filed.
- On the corpus evidence, reported FY26 growth of 31.79% is the like-for-like figure.
  The 28.06% figure and the Rs 200.35 cr "like-for-like" FY26 base have no basis.
- The Rs 5.84 cr figure was never a disclosed gross-up amount. It is the whole FY26
  "Cartage & Freight outward" expense line (AR FY26 Note 30, PDF p.138), which already
  ran at Rs 426.95 lakh in FY25. The size of the gross-up in any year is NOT
  DISCLOSED. Note 23 has one revenue line, "Sale of Products (Net of Discount)" (AR
  FY26 PDF p.135), and no freight-recovery line exists in revenue or expenses.
- What survives of the disclosure finding: the policy sits in every results filing and
  in no annual report note. That gap is real and narrower than first stated.
- Q1 FY27 growth of 27.2% (5,916.66 against 4,649.64) is also like for like on the
  filings' presentation.
- Downstream items that rested on 200.35 / 28.06% and must be re-scored: Gate 0
  growth tests in Block C (B01), the stage 5 trigger 1 threshold, and the stage 9
  growth base. Recorded as an open item in LESSONS_ARCHIVE.md. NOT re-run in this
  commit.

Side finding in the same filing, recorded: the Q1 FY27 filing prints Q1 FY26 EPS as
7.46 under a column header of "face value of Rs. 2/- each" (PDF p.4). 7.46 is the
pre-split Rs 10 figure: profit of Rs 616.08 lakh over 82,63,700 shares. On the Rs 2
base it is 1.49. The Q4 FY26 and FY26 columns are split-adjusted (1.59 and 6.64);
the Q1 FY26 comparative is not.

---

## 4. Material cost ratio, rebuilt

Basis: (cost of materials consumed + changes in inventories of finished goods, stock
in trade and work in progress) / revenue from operations. Standalone. In the P&L a
positive change in inventories is a drawdown that adds to cost; a negative change is
a build that reduces it.

| Quarter | Revenue | Materials consumed | Change in inventories | Materials + change | Adjusted ratio | Plain ratio | Adjusted, trailing 4Q | Source |
|---|---|---|---|---|---|---|---|---|
| Q1 FY25 (derived) | 4,311.46 | 2,234.58 | (57.87) | 2,176.71 | 50.49% | 51.83% | n/a | H1 FY25 less Q2 FY25, Q2 FY26 filing PDF p.4 |
| Q2 FY25 | 3,989.11 | 1,619.24 | 131.86 | 1,751.10 | 43.90% | 40.59% | n/a | Q2 FY26 filing PDF p.4 |
| Q3 FY25 | 3,827.58 | 1,963.82 | (130.08) | 1,833.74 | 47.91% | 51.31% | n/a | Q3 FY26 filing PDF p.4 |
| Q4 FY25 | 3,516.93 | 1,730.44 | (229.18) | 1,501.26 | 42.69% | 49.20% | 46.42% | FY26 filing PDF p.7 |
| Q1 FY26 | 4,649.64 | 1,855.28 | 539.67 | 2,394.95 | 51.51% | 39.90% | 46.81% | Q2 FY26 / Q1 FY27 filings PDF p.4 |
| Q2 FY26 | 5,435.47 | 2,742.73 | (137.86) | 2,604.87 | 47.92% | 50.46% | 47.82% | Q2 FY26 filing PDF p.4 |
| Q3 FY26 | 5,650.57 | 2,727.66 | 9.12 | 2,736.78 | 48.43% | 48.27% | 47.98% | Q3 FY26 filing PDF p.4 |
| Q4 FY26 | 4,883.35 | 2,590.68 | (707.75) | 1,882.93 | 38.56% | 53.05% | 46.65% | FY26 filing PDF p.7 |
| Q1 FY27 | 5,916.66 | 2,992.80 | (203.91) | 2,788.89 | 47.14% | 50.58% | 45.75% | Q1 FY27 filing PDF p.4 |
| **FY25** | 15,645.08 | 7,548.08 | (285.27) | 7,262.81 | **46.42%** | 48.25% | | FY26 filing PDF p.7 |
| **FY26** | 20,619.03 | 9,916.35 | (296.82) | 9,619.53 | **46.65%** | 48.09% | | FY26 filing PDF p.7 |

Q1 FY25 is not in a filing in the corpus. It is derived as the six months to
30-Sep-2024 (revenue 8,300.57, materials 3,853.82, change in inventories 73.99; Q2
FY26 filing PDF p.4) less Q2 FY25. Cross-check: the nine months to 31-Dec-2024
(12,128.15 / 5,817.64 / (56.09); Q3 FY26 filing PDF p.4) less Q2 and Q3 FY25 gives the
same three figures. The four FY25 quarters sum to the audited FY25 year on all three
lines; the four FY26 quarters sum to FY26.

Comment.
- On the adjusted basis the year is flat: 46.42% in FY25, 46.65% in FY26, a rise of
  0.23 points. The run's conclusion holds on the new basis. Material cost did not
  fall as a share of revenue while revenue grew 31.79%. The peer signature of a mix
  climb, a falling ratio, is still absent.
- The quarterly series is noisy, from 38.56% to 51.51%. The swing comes from the
  inventory line, not from materials. Q4 FY26 reads 38.56% only because Rs 707.75 lakh
  went into inventory; Q1 FY26 reads 51.51% because Rs 539.67 lakh came out.
- One limit of the basis: changes in finished goods and work in progress are valued at
  full production cost, which includes labour, power and overhead, not material alone.
  The adjusted ratio is "materials plus inventory movement at cost". It is the right
  correction for timing. It is not a pure material ratio.

Proof gate, restated on this basis (the draft Mental Model, Part B3):

> Materials consumed plus change in inventories, as a share of revenue from
> operations, falls below the FY26 level of 46.65% for two consecutive quarters,
> while revenue growth year on year holds at high single digits or better.

Two readings of "two consecutive quarters", and the observation that separates them,
for the operator to choose at sign-off:
- Single quarter. Q4 FY26 at 38.56% is already below the line and Q1 FY27 at 47.14%
  is above it, so the gate has not fired. On this reading the gate fires on inventory
  timing as easily as on mix. Every quarter since Q1 FY25 has moved 3 to 13 points
  from the one before it.
- Trailing four quarters. 46.65% at Q4 FY26 (the FY26 year), 45.75% at Q1 FY27. One
  reading below the line so far. That reading rides on the Q4 FY26 inventory build of
  Rs 707.75 lakh, which will roll out of the window by Q4 FY27.
- The separating observation: the Q2 FY27 filing (due Nov-2026). A trailing ratio below
  46.65% with the change-in-inventories line at or near zero would be a material-cost
  fall. A trailing ratio below the line with another large inventory build would be
  timing.

The gate recommendation's falsification line and monitorable 2 move to the same basis
in this commit. The dossier's draft Part B3 and dominant variable 1 move too.

---

## Correction found while answering, outside the four questions

Related-party purchases. The run's final files state Rs 3,877.14 lakh, 39.1% of cost
of materials consumed, on Verifier A's re-run. That figure is wrong. The stage figure
it replaced, Rs 3,683.61 lakh and 37.1%, is right.

Quote, AR FY26 Note 41 related-party transactions (PDF p.145), cost-of-materials block:

> "Cost of Materials Consumed: Peptech Biosciences Ltd Associate 44.79 36.25; Phoenix Bio Sciences Private Ltd Other related parties 2,574.32 1,482.50; Stalwart Nutritions Private Ltd. Other related parties 986.20 821.79; Titan Media Limited Associate - 0.53; Titan Animal Nutrition Private Limited Other related parties 78.30 -"
> "Other Expenses: Stalwart Nutritions Private Ltd. - 2.09; Peptech Biosciences Ltd Associate 132.96 69.45"
> "3,877.14 2,454.93"

Comment. Rs 3,877.14 lakh is a sub-total for the whole expense block, not for
materials:
- materials 3,683.61
- plus other expenses 132.96
- plus fixed assets bought 18.57 (Phoenix 1.20, Stalwart 17.37)
- plus rent 42.00
- total 3,877.14.

The FY25 column proves the pattern: 2,341.07 + 71.54 + 42.00 + 0.32 = 2,454.93.
Verifier A's own itemisation in its finding (44.79 + 2,574.32 + 986.20 + 78.30)
adds to 3,683.61, not to 3,877.14. Related-party materials are Rs 3,683.61 lakh,
37.15% of Rs 9,916.35 lakh. Phoenix Bio Sciences is 25.96% (2,574.32 / 9,916.35),
up 73.65% (from 1,482.50). The FLAG-RPT-CONCENTRATION finding stands at 37.1%. The
earlier statement that the audited figure "strengthens" the finding is withdrawn.

Logged in verifier-disagreement-log.md as FLAG CLEARED, re-checked by the orchestrator
on 2026-10-04. Aligned in the gate recommendation, the business narrative and the
dossier in this commit.

---

## Files and pages used

| File | Pages | Used for |
|---|---|---|
| inputs/results/2026-05-30_FY26_audited_results.pdf | PDF p.7 (standalone P&L), p.10 (standalone cash flow), p.18 (consolidated cash flow) | 1(a), 1(b), 2, 4 |
| inputs/results/2025-11-11_Q2FY26_unaudited_results.pdf | PDF p.4 (standalone P&L, note 6) | 3, 4 |
| inputs/results/2026-02-12_Q3FY26_unaudited_results.pdf | PDF p.4 (standalone P&L, note 6) | 3, 4 |
| inputs/results/2026-08-13_Q1FY27_unaudited_results.pdf | PDF p.4 (standalone P&L, note 5) | 3, 4, EPS side finding |
| inputs/announcements/2025-02-13_integrated-filing-financial.pdf | PDF p.4 (standalone extract, note 5), p.5 (consolidated full, note 7) | 3 |
| inputs/announcements/2025-02-28_arbitration-update.pdf (misnamed; Titan Media call intimation) | PDF p.1 | 2 |
| inputs/annual-report/AR_FY2026.pdf | PDF p.104 (MD&A Table A), p.117 (standalone cash flow), p.127 (Note 3 ROU), p.128 (Note 5 investments), p.134 (Note 17 leases), p.135 (Note 23 revenue), p.136 (Note 24 other income), p.138 (Note 30 other expenses), p.142 (Note 36(II) commitments), p.145 (Note 41 RPT), p.150 (Note 42 maturities), p.162 (consolidated cash flow) | 1, 2, 3, correction |
| inputs/annual-report/AR_FY2025.pdf | PDF p.123 (Note 5 investments) | 2 |
| inputs/annual-report/AR_FY2024.pdf | PDF p.129 (Note 5 investments) | 2 |
| text search of AR_FY2024, AR_FY2025, AR_FY2026 extractions | whole documents | 3, freight note absent from every AR |

NOT IN CORPUS, named for collection: the Q1 FY26 results filing of 13-Aug-2025
(BSE attachment aa5cb05e-a85a-426b-b094-69afc1810339.pdf); the Q1 FY25 and Q2 FY25
results filings (Aug-2024, Nov-2024); the FY24 audited results (May-2024).
