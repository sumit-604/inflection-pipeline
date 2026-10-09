# KISSHT EXTRACTION ANNEX 2, 2026-10-03

Answering the second Claude web extraction request of 2026-10-03 against the
committed corpus of runs/kissht-2026-09-19 (branch run/kissht-2026-09-19).

Sources: `inputs/prospectus/OnEMI_RHP_2026-04-25.pdf` (RHP, 464 pp) and
`inputs/annual-report/Annual_Report_2026.pdf` (AR, 138 pp).

CITATION KEY. Pages are the PDF page from the `[page N]` marker in the page-marked
text extract. For the RHP the printed page is the PDF page minus 6; both are given.
AR pages are PDF pages only (the AR footers print two-page spreads).

UNITS. Rs million throughout, as both filings state on the face of the statements.
No conversion. Where this annex subtracts two quoted figures, it says so and labels
the result as arithmetic, not as a disclosed number.

---

## 1. Restated consolidated Other Expenses: the off-book loss lines, four periods

QUOTE (RHP PDF p.309 / printed p.303, restated consolidated Note, "Other expenses";
columns are period ended 31-Dec-2025, year ended 31-Mar-2025, 31-Mar-2024,
31-Mar-2023, Rs million):

> "Impairment allowances on trade receivables(Net) 2.70 8.18 20.79 -
> Expected credit loss on off balance sheet exposure 1271.51 619.22 740.49 1,940.27
> Net loss on foreign currency transaction 1.09 0.70 0.52 1.20
> Loss on sale of fixed assets 0.36 - - -
> Office & miscellaneous expenses 72.6 38.67 76.35 109.51
> 5,635.26 4,292.50 5,394.37 4,887.22"

FLDG LINE IN THE RESTATED CONSOLIDATED NOTE: NOT DISCLOSED, and not because it was
omitted. The restated consolidated Other Expenses note has NO "First loan default
guarantee cost" row in any of the four periods. The full row list of that note is
rent, rates and taxes, electricity, travelling, repair and maintenance, bank and
payment gateway charges, server and communication cost, business support service
expenses, outsourcing and back office expenses, branding and marketing, CIBIL and
other verification, CSR, legal and professional, director's sitting fees, auditors'
remuneration, customer incentive cost, impairment allowances on trade receivables,
expected credit loss on off balance sheet exposure, net loss on foreign currency,
loss on sale of fixed assets, and office and miscellaneous. At consolidated level
the single off-book loss line is "Expected credit loss on off balance sheet
exposure". Compare the AR's consolidated Note 29 for FY26, which carries the same
single line plus a new "Credit Guarantee fees 19.93".

### The Q4 FY26 derivation the request asked for

| Period | Consolidated off-book ECL | Source |
|---|---|---|
| FY23 | 1,940.27 | RHP PDF p.309 / printed p.303 |
| FY24 | 740.49 | RHP PDF p.309 / printed p.303 |
| FY25 | 619.22 | RHP PDF p.309 / printed p.303, and AR PDF p.119 comparative |
| 9M FY26 (to 31-Dec-2025) | 1,271.51 | RHP PDF p.309 / printed p.303 |
| FY26 (full year) | 1,546.85 | AR PDF p.119-120, consolidated Note 29 |
| **Q4 FY26, by subtraction** | **275.34** | my arithmetic: 1,546.85 minus 1,271.51 |

COMMENT.
- The derivation holds on one basis: both figures are consolidated, both come from
  the identically named line, and the 9M figure is restated-for-IPO while the FY26
  figure is the audited annual. The AR does not publish a quarterly split, so
  275.34 is a subtraction, not a disclosure.
- What it says: the off-book provision charge ran at an average of 423.84 a quarter
  through the first nine months of FY26 (1,271.51 over 3, my arithmetic) and then
  275.34 in Q4. The line decelerated into the fourth quarter even as off-book AUM
  kept rising.
- The FY23 figure of 1,940.27 is the largest in the series, above FY24, FY25 and
  9M FY26. The MD&A confirms the shape. QUOTE (RHP PDF p.360 / printed p.354):
  "These increases were offset by a decrease in expected credit loss on off balance
  sheet exposure from Rs1,940.27 million in Fiscal". And QUOTE (RHP PDF p.358 /
  printed p.352): "decrease in credit loss on off balance sheet exposure by 16.38%
  from Rs740.49 million in Fiscal 2024 to Rs619.22 million".
- The off-book provision BALANCE across periods is also disclosed. QUOTE (RHP PDF
  p.306 / printed p.300, restated consolidated other financial liabilities):
  "Provision on off balance sheet exposure - - 428.57 304.17 295.18". And QUOTE
  (RHP PDF p.363 / printed p.357, MD&A): "decrease in provision on off balance sheet
  exposure from Rs1,638.14 million as of March 31, 2023 to Rs304.17 million as of".

## 2. AR Note 41: stage EAD and ECL, and the movement rows

### Year-end credit quality of loans

QUOTE (AR PDF p.127, "Credit quality of Loans: As at 31 March 2026"):

> "Stage 1 Loans and Advances 33,972.48 1,027.99
> Stage 2 836.20 632.05
> Stage 3 753.87 649.52
> Total 35,562.55 2,309.56
> Note: Management overlay of Rs1,359.53 million is not included in the expected
> credit loss (Ind AS 109) amount above."

QUOTE (AR PDF p.128, "As at 31 March 2025"):

> "Stage 1 Loans and Advances 23,156.96 646.90
> Stage 2 872.37 516.15
> Stage 3 716.25 655.20
> Total 24,745.58 1,818.25
> Note: Management overlay of Rs1349.89 million is not included in the expected
> credit loss(Ind AS 109) amount above."

(Columns: estimated gross carrying amount at default, then expected credit losses
under Ind AS 109.)

### FY26 movement table, verbatim

QUOTE (AR PDF p.127; columns are Stage 1 EAD, Stage 1 ECL, Stage 2 EAD, Stage 2
ECL, Stage 3 EAD, Stage 3 ECL, Total EAD, Total ECL):

> "As at 01 April 2025 23,631.17 646.90 882.28 516.15 723.53 655.20 25,236.98 1,818.25
> New credit exposures during the year, net of repayments 13,970.95 551.26 622.33 494.84 1,089.74 979.89 15,683.02 2,025.99
> Assets written off during the year - - - - (4,725.95) (4,725.95) (4,725.95) (4,725.95)
> Movement between stages
> Transfer to Stage 1 2.90 1.81 (2.74) (1.66) (0.16) (0.15) - -
> Transfer to Stage 2 (126.77) (2.82) 126.78 2.83 (0.01) (0.01) - -
> Transfer to Stage 3 (2,890.14) (214.84) (782.09) (461.03) 3,672.23 675.87 - -
> Impact on ECL on account of movement between stages / updates to the ECL model - 45.68 - 80.92 - 3,064.67 - 3,191.27
> As at 31 March 2026 34,588.11 1,027.99 846.56 632.05 759.38 649.52 36,194.05 2,309.56
> Less: Consolidation Adjustment of EIR on Loans (615.63) - (10.36) - (5.51) - (631.50) -
> As at 31 March 2026 (Net of EIR) 33,972.48 1,027.99 836.20 632.05 753.87 649.52 35,562.55 2,309.56"

### FY25 movement table, verbatim

QUOTE (AR PDF p.127-128):

> "As at 01 April 2024 13,415.56 1,731.95 1,457.40 1,082.55 116.83 116.83 14,989.79 2,931.33
> New credit exposures during the year, net of repayments 11,981.42 (475.74) 503.34 223.17 2,029.17 1,826.25 14,513.93 1,573.68
> Assets written off during the year - - - - (4,271.16) (4,271.16) (4,271.16) (4,271.16)
> Movement between stages
> Transfer to Stage 1 2.12 1.73 (1.56) (1.17) (0.56) (0.56) - -
> Transfer to Stage 2 (67.01) (8.15) 67.42 8.56 (0.41) (0.41) - -
> Transfer to Stage 3 (1,705.34) (601.25) (1,144.32) (831.61) 2,849.66 1,432.86 - -
> Impact on ECL on account of movement between stages / updates to the ECL model - (1.64) - 34.65 - 1,551.39 - 1,584.40
> As at 31 March 2025 23,626.75 646.90 882.28 516.15 723.53 655.20 25,232.56 1,818.25
> Less: Consolidation Adjustment of EIR on Loans (469.79) - (9.91) - (7.28) - (486.98) -
> As at 31 March 2025 (Net of EIR) 23,156.96 646.90 872.37 516.15 716.25 655.20 24,745.58 1,818.25"

RECOVERIES ROW: NOT DISCLOSED. The movement table has no recoveries line. Repayments
are netted inside "New credit exposures during the year, net of repayments", so
gross originations and gross repayments cannot be separated from this note. The only
recoveries disclosure is a policy sentence. QUOTE (AR PDF p.101): "(ix) Recoveries
of financial assets written off: The Group recognises income on recoveries of
financial assets written off on realisation basis." No amount is given for FY26 or
FY25, in either statement. Where it would sit: inside consolidated Note 23 Other
income, which does not break it out, or a separate recoveries disclosure, which does
not exist.

COMMENT on what the movement rows show.
- Gross inflow into Stage 3 during FY26: new credit exposures already in Stage 3 of
  1,089.74 plus transfers into Stage 3 of 3,672.23, which is 4,761.97 of fresh
  default exposure (my addition of two quoted figures). Write-offs of 4,725.95
  removed almost exactly that amount. Stage 3 EAD therefore ended at 759.38 against
  723.53 at the start, up 4.96%, while the flow through it was more than six times
  the closing balance.
- Transfer to Stage 3 in FY26 of 3,672.23 against FY25 of 2,849.66: inflow by
  transfer rose 28.9%, which is the figure phase 1 quoted.
- The ECL on Stage 3 transfers is the load-bearing judgment: "Impact on ECL on
  account of movement between stages / updates to the ECL model" adds 3,064.67 in
  Stage 3 ECL in FY26 against 1,551.39 in FY25. The note does not separate the
  stage-movement effect from the model-update effect. NOT DISCLOSED, and material,
  because one is mechanical and the other is discretionary.
- Opening Stage 1 ECL dropped from 1,731.95 (01-Apr-2024) to 646.90 (01-Apr-2025)
  while Stage 1 EAD nearly doubled, and the FY25 row "New credit exposures ... net of
  repayments" carries a NEGATIVE Stage 1 ECL of (475.74). The note gives no
  explanation. NOT DISCLOSED.
- The management overlay sits outside all of this: 1,359.53 at FY26 against 1,349.89
  at FY25, up 0.7% while Ind AS 109 ECL rose from 1,818.25 to 2,309.56.

## 3. Vintage, cohort, static-pool and first-EMI series

FINDING: there is no vintage table, no cohort table and no static-pool table in
either document. What exists is three point-to-point delinquency series inside the
business section, each with dates, and all at group level.

QUOTE (RHP PDF p.200 / printed p.194):

> "Our sustained efforts in strengthening the underwriting framework have enables us
> to materially improve the quality of our credit decisions. Our 90 DPD risk for
> first EMI, a critical early delinquency metric, has declined from 6.83% to 0.83%
> between June 30, 2023 and December 31, 2025. This reduction is accompanied with
> significant AUM growth, highlighting the strength of our risk models, data-led
> underwriting and credit governance."

QUOTE (RHP PDF p.207 / printed p.201, "Late delinquency (31-90 DPD)"):

> "This structured process has contributed to a consistent improvement in recovery
> efficiency, with over 90 DPD collection efficiency increasing from 94.19% in the
> first quarter of Fiscal 2023 to 98.75% in the last quarter of Fiscal 2025. In the
> nine months ended December 31, 2025, our 90 DPD collection efficiency was 97.64%."

QUOTE (RHP PDF p.200 / printed p.194, rejection-reason split for repeat applicants):

> "Key reasons for rejection at this stage include factors related to model scores
> 15.54%, leverage 5.97%, device 2.97%, geography-specific risks 0.21%, repayment
> history with other lenders 1.32%, and banking transaction variables 0.45%."

QUOTE (RHP PDF p.199 / printed p.193):

> "...resulting in an underwriting approval rate of 11.20% for new applicants and
> 73.54% for repeat customers in the nine months ended December 31, 2025."

COMMENT.
- The first-EMI series is two points, 30-Jun-2023 and 31-Dec-2025, with nothing in
  between. It is a first-payment-default proxy, not a vintage curve. A vintage series
  would show each disbursement cohort's loss path by months-on-book; nothing of the
  kind is in the RHP or the AR.
- Note the internal tension in the collection-efficiency series: it improves from
  94.19% (Q1 FY23) to 98.75% (Q4 FY25), then reads 97.64% for 9M FY26, which is
  below the Q4 FY25 end point. The RHP presents both without reconciling them. The
  phase 1 corpus also carries the Q1 FY27 collection efficiency at 96.82% from the
  press release, on a DPD-30 basis, which is a third basis again. Three bases, three
  trends, and only the first two sit in the RHP.
- Where a vintage or static-pool table would sit if it existed: the RHP's "Our
  Business - Risk management" section (PDF p.201 onward / printed p.195 onward), or
  a credit-quality annexure to the restated financial information. Neither carries
  one. Si Creva's own ALM and asset-quality returns to the RBI would hold it; they
  are not public and not in the corpus.

## 4. Where the standalone Rs 1,009.47 mn FLDG cost lands on consolidation

ANSWER: the AR never states the mapping. NOT DISCLOSED. But four quoted figures
constrain it tightly, and the constraint is informative.

The four disclosures:

QUOTE (AR PDF p.85, standalone other expenses): "Expected credit loss on off balance
sheet exposure 239.57 138.01 / First loan default guarantee cost 1,009.47 4.65"

QUOTE (AR PDF p.119-120, consolidated Note 29): "Expected credit loss on off balance
sheet exposure 1,546.85 619.22" and "Credit Guarantee fees 19.93 -"

QUOTE (AR PDF p.67, standalone cash flow, non-cash adjustments): "Provision on off
balance sheet exposure 239.57 138.01"

QUOTE (AR PDF p.99, consolidated cash flow, non-cash adjustments): "Provision on off
balance sheet exposure 169.67 8.99"

And the balance-sheet lines:

QUOTE (AR PDF p.83, standalone Note 17): "Provision on off balance sheet exposure -
- 377.58 138.01" (non-current FY26, non-current FY25, current FY26, current FY25)

QUOTE (AR PDF p.118, consolidated Note 20): "Provision on off balance sheet exposure
- 473.84 304.17"

### What the arithmetic forces

All subtractions below are mine, on quoted figures.

| Test | Standalone | Consolidated |
|---|---|---|
| Off-book provision balance, FY26 | 377.58 | 473.84 |
| Off-book provision balance, FY25 | 138.01 | 304.17 |
| Movement in the balance | +239.57 | +169.67 |
| Non-cash add-back in the cash flow | 239.57 | 169.67 |
| P&L charge on the off-book line | 239.57 | 1,546.85 |
| P&L charge above the provision movement | nil | 1,377.18 |

- Standalone ties perfectly: the 239.57 ECL charge equals the provision movement
  equals the cash-flow add-back. So the standalone "Expected credit loss on off
  balance sheet exposure" is a pure provision build.
- The standalone "First loan default guarantee cost" of 1,009.47 does NOT pass
  through the provision account at all. It is absent from the standalone cash-flow
  add-backs, which means it is not a non-cash provision movement. On the face of the
  statements it is a settled cost of the year.
- Consolidated carries ONE off-book line at 1,546.85 while its provision moved only
  169.67. The gap of 1,377.18 is charge that did not build a provision.
- Those two facts are consistent with exactly one reading: the parent's 1,009.47
  settled FLDG cost is inside the consolidated 1,546.85 line rather than eliminated,
  with the remaining 367.71 (my subtraction: 1,377.18 minus 1,009.47) arising at the
  subsidiary or from parent provision utilisation. The AR states none of this. It is
  an inference the figures constrain, not a disclosure, and it should be put to
  management as such.
- It also disposes of the elimination question the request raised: a guarantee cost
  paid to third-party lending partners is an external cost, so there is no
  intra-group transaction to eliminate. What IS eliminated is the intra-group
  guarantee FEE: "Corporate Guarantee Fees Income 394.06 155.52" sits in the
  standalone related-party note (AR PDF p.89) and appears nowhere in the
  consolidated P&L.
- Consequence for the phase 1 "about Rs 2.5 bn" figure, restated once more: the
  group off-book cost for FY26 is best read as the consolidated 1,546.85 plus credit
  guarantee fees 19.93, with the parent's 1,009.47 inside the former, not added to
  it.

## 5. Off-book delinquency and FLDG utilisation by partner

### The decisive definition

QUOTE (RHP PDF p.133 / printed p.127, KPI note 24, and repeated at RHP PDF p.17 /
printed p.11 in the definitions section):

> "(24) Gross NPA ("GNPA") represents ratio of Gross Stage 3 On-book loans to gross
> carrying amount of total gross On-book loans as at the last day of the relevant
> period.
> (25) Net NPA ("NNPA") represents ratio of Net NPA to total gross On-book loans as
> at the last day of the relevant period. Net NPA is gross stage 3 On-book loans
> reduced by impairment allowances provided on stage 3 On-book loans as at the last
> day of relevant period.
> (26) Provisioning Coverage Ratio ("PCR") is calculated as impairment loss allowance
> on stage 3 loans as a percentage of gross carrying value of stage 3 loans as on the
> last day of the relevant period."

COMMENT, and this is the most consequential line in either extraction.
- GNPA, NNPA and PCR are ON-BOOK ratios by definition. Off-book loans, which were
  48.87% of AUM at 31-Dec-2025 and 53.6% at 30-Jun-2026, are excluded from both the
  numerator and the denominator.
- So every headline asset-quality number in the corpus, including the 2.12% at FY26
  and the 2.25% at Q1 FY27, describes slightly under half the managed book. No stage
  of phase 1 established this. Any statement that "GNPA is 2.25%" needs the words
  "on the on-book portfolio" attached.
- Off-book 90+ DPD, off-book Stage 3, or any delinquency measure on the co-lent,
  100-0 or BC portfolio: NOT DISCLOSED anywhere in the RHP or the AR, for any period.
- FLDG utilisation by partner: NOT DISCLOSED. The partner-wise disclosure that does
  exist is AUM only, by number not name. QUOTE (RHP PDF p.32 / printed p.26, risk
  factor 14, 31-Dec-2025 column): "- Partner 1 11,342.26 19.04% / - Partner 2
  7,390.73 12.41% / - Partner 3 8,517.67 14.30% / - Partner 4 528.26 0.89% / -
  Partner 5 891.03 1.50% / - Partner 6 436.17 0.73% / - Partner 7 0.08 0.00%".

### The nearest thing to an FLDG utilisation series

QUOTE (RHP PDF p.123 / printed p.117, Si Creva's regulatory capital computation;
columns are 31-Dec-2025, 31-Mar-2025, 31-Mar-2024, 31-Mar-2023):

> "Cred enhancement & FLDG cover (249.74) (479.07) (30.17) -"
> "Credit enhancement (161.97) (338.94) (30.17) -" (within Tier-II Capital)
> "Negative amount transferred from Tier - II Capital - (30.32) - -"

COMMENT.
- This is a deduction from Si Creva's Tier-I capital for credit enhancement and FLDG
  cover, and a matching Tier-II line. It is the only place either filing puts a
  number on FLDG exposure outside the parent's own guarantee and provision lines.
- Read it with care: it is a regulatory capital deduction at the SUBSIDIARY, while
  the FLDG the group gives to partners is disclosed at the PARENT (outstanding
  Rs 737.80 mn at FY26, per AR PDF p.88). The two are not the same exposure and the
  filings never bridge them.
- The series falls from 479.07 (FY25) to 249.74 (Dec-2025) while off-book AUM rose
  from 16,120.80 to 29,106.20 over the same span (RHP PDF p.132 / printed p.126).
  Exposure down, book up. The RHP offers no explanation. Worth a management question.

### What the business section says about which arrangements carry FLDG

QUOTE (RHP PDF p.194 / printed p.188):

> "Our associations with our lending partners comprise three distinct arrangements,
> i.e., 100-0 arrangement, co-lending arrangement and DA. Under the 100-0
> arrangement, we act as a sourcing and technology partner, with all loans being
> recorded directly and entirely on the balance sheet of our lending partners. In the
> co-lending model, loans originate jointly with our lending partners and a
> pre-agreed portion of each loan is retained on our Subsidiary, Si Creva's balance
> sheet, while the remaining portion is held by our lending partners. Further, under
> the DA model, we originate loans and subsequently assign them to our lending
> partners shortly after disbursement, which results in minimal balance sheet
> exposure for our Subsidiary. ... We provide first loss default guarantees ("FLDG")
> on our 100-0 and co-lending arrangements in relation to our off-book loans in
> accordance with applicable RBI guidelines."

COMMENT. FLDG attaches to the 100-0 and co-lending arrangements, not to direct
assignment. The split of off-book AUM between those three arrangements, and therefore
the share of off-book AUM that carries FLDG at all, is NOT DISCLOSED. The AR gives
only an arrangement-wise percentage chart on AR PDF p.19 whose values do not extract
from the slide graphics.

---

# VERIFICATION: every file and date quoted above

| Document | File in the corpus | Document date | Pages quoted (PDF page / RHP printed page) |
|---|---|---|---|
| Red Herring Prospectus | `inputs/prospectus/OnEMI_RHP_2026-04-25.pdf` | 25-Apr-2026 | 17/11, 32/26, 123/117, 132/126, 133/127, 194/188, 199/193, 200/194, 207/201, 306/300, 309/303, 358/352, 360/354, 363/357 |
| Annual Report 2025-26 | `inputs/annual-report/Annual_Report_2026.pdf` | FY ended 31-Mar-2026, AGM 22-Sep-2026 | 19, 67, 83, 85, 88, 89, 99, 101, 118, 119, 120, 127, 128 |

Figures quoted carry these period labels: nine months ended 31-Dec-2025; years ended
31-Mar-2026, 31-Mar-2025, 31-Mar-2024, 31-Mar-2023; and the dated delinquency points
30-Jun-2023, Q1 FY23, Q4 FY25 and 31-Dec-2025.

Documents named above but NOT in the corpus, so not quoted:
- Si Creva Capital Services' own annual report, audit report and RBI returns (would hold off-book or product-level asset quality, the ALM ladder, FLDG utilisation by partner).
- The final Prospectus dated 05-May-2026.
- Any partner-wise FLDG schedule or co-lending agreement.

Derived numbers in this annex, each my arithmetic on quoted figures, none disclosed:
Q4 FY26 off-book ECL 275.34; 9M FY26 quarterly average 423.84; FY26 gross Stage 3
inflow 4,761.97; consolidated charge above provision movement 1,377.18; residual
after the standalone FLDG cost 367.71.

Corpus commit: 41c184117c002f3ecd9fbabfd7e4e717ba780a3a (branch run/kissht-2026-09-19).
Extraction run by Claude Code, 2026-10-03.
