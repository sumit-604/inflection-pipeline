# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 2 (WHAT WAS MISSED)
Company: Pitti Engineering Ltd (PITTIENG) | Run: pittieng-2026-09-05 | FY2025-26 Annual Report
Source: runs/pittieng-2026-09-05/inputs/annual-report/Annual_Report_2026_2.pdf (sidecar: inputs/_text/annual-report__Annual_Report_2026_2.txt)
Method: re-read Notes 1-25 (both statement sets) against the Pass 1 report note by note; new findings only, Pass 1 not repeated.
Rating key: 🟢 Clean | 🟡 Watch | 🔴 Red Flag

---

## NEW FINDINGS BY NOTE

### Note 25.21 Key Ratios (standalone, PDF p.90) — variance-disclosure methodology masks a >25% ROE decline
The note's own "reason for variance >25%" column is populated only for Net Capital Turnover Ratio
(-41.73%). For ratio-type rows (current ratio, debt-equity, DSCR, inventory/receivables/payables
turnover) the "Variance" column is computed as a genuine **relative % change**: e.g. Current Ratio
1.33 vs 1.17 = +13.68%, matching (1.33-1.17)/1.17. But for the three rows already expressed as a
percentage — Return on Equity (10.63% vs 15.75%), Net Profit Ratio (6.13% vs 7.01%), Return on
Capital Employed (14.72% vs 16.24%) — the same "Variance" column instead shows the simple
**percentage-POINT difference** (-5.12%, -0.88%, -1.52%), not the relative change. Recomputed on the
same relative basis the note uses everywhere else, ROE fell **-32.5%** [(10.63-15.75)/15.75], comfortably
past the company's own 25% explanation threshold — yet no reason is given, because the point-difference
figure (-5.12%) reads as sub-threshold. Net Profit Ratio's relative fall is -12.6% and ROCE's is -9.4%,
both genuinely sub-threshold, so only ROE is affected, but it is the single most decision-relevant metric
in the table. This is a disclosure-integrity finding, not merely a rounding quirk: a mechanically
inconsistent formula, applied only to the percentage-denominated rows, is the reason the steepest
profitability decline in the table carries no explanation. (Note 25.21, PDF p.90 standalone) 🔴

### Note 25.9A/25.9B Deferred Tax — the mechanism behind the effective-tax-rate jump Pass 1 flagged as unexplained
Pass 1 correctly noted the reconciliation table ties only to current tax and does not extend to the full
effective rate. The mechanism is traceable in Note 25.9B's deferred-tax movement table: the deferred
tax LIABILITY for "Depreciation as per Companies Act vs IT Act" increased by ₹922.36L in the P&L
column (standalone: 2,980.33→3,902.69) and by ₹1,028.45L consolidated (4,285.34→5,313.79) during
FY26. Adding this deferred-tax swing to the current-tax charge reproduces the reported effective rate:
standalone current tax ₹3,496.47L + net deferred tax expense ₹888.41L = ₹4,384.88L / PBT ₹14,030.79L
≈ 31.3%; consolidated ₹4,204.11L + ₹893.23L = ₹5,097.34L / ₹16,758.11L ≈ 30.4% — both close to the
23.96%→30.49% (standalone) and 24.33%→29.70% (consolidated) rate jump Pass 1 identified. In plain
terms: accelerated tax depreciation from the capex ramp is now reversing/normalising, and that reversal
— not a change in cash tax planning — is the arithmetic driver of the FY26 PAT decline. This is a timing
item, expected to recur as the depreciation gap continues to close, and is a fair basis for a management
question on the multi-year glide path of this DTL. (Note 25.9B, PDF p.89 standalone / p.120 consolidated) 🟡

### Consolidated Auditor's Report "OTHER MATTERS" (PDF p.92) — both subsidiaries audited by a different firm, not named
The consolidated auditor's report states: "We did not audit the financial statements of 2 (two)
subsidiaries, whose financial statements reflect total assets of Rs. 23,633.30 Lakhs... total revenues of
Rs. 38,224.79 Lakhs, total comprehensive income... of Rs. 2,115.37 Lakhs and net cash inflows...
Rs. 1,409.08 Lakhs... audited by other auditors whose reports have been furnished to us... our opinion...
is based solely on the reports of the other auditors." Rs. 38,224.79L is ~20% of consolidated revenue
from operations (₹1,91,280.36L). Neither the identity of the other audit firm(s) nor any qualification in
their reports is stated in this paragraph. Talati & Talati's own "no key audit matters" conclusion
(Pass 1, Section 12) therefore covers only the parent's ~80% of revenue at first hand; roughly a fifth of
group revenue and the bulk of subsidiary PAT (cross-checks to AOC-1's PIPL ₹800.67L + DFPL
₹1,270.93L = ₹2,071.60L, close to the ₹2,115.37L total comprehensive income cited here) rests on
unnamed component auditors' work. Not a qualification or red flag on its own — standard practice for a
multi-entity group — but a gap Pass 1 did not surface. (Consolidated Independent Auditor's Report,
"Other Matters," PDF p.92) 🟡

### Note 25.7(B) Supplier Finance Arrangement (TReDS) — embedded in trade payables, nearly doubled YoY
A disclosure Pass 1 did not pick up: the Company (identical figures standalone and consolidated,
confirming it sits wholly at parent level) has supplier finance arrangements via the TReDS platform and
banks. Carrying amount of financial liabilities under these arrangements, presented within Trade
Payables: **₹9,402.53L**, of which **₹8,385.28L** already paid to suppliers by the financier (i.e., already
bank-funded, awaiting the Company's payment to the bank on revised terms of 90-120 days). This
balance grew from an opening ₹4,436.16L to closing ₹8,385.28L (+89.0%) during the year via
₹3,949.12L of net cash inflow through the arrangement. Practical implication: part of the trade-payables
book Pass 1 flagged as "down 25.7%... single largest driver of the FY26 working-capital reversal" is
economically closer to short-term bank financing dressed as trade credit, extending the true payment
period on ~₹83.85 Cr of purchases beyond ordinary vendor terms (0-120 days) to 90-120 days from
invoice/discounting date. This does not change the Note 13C/13D headline numbers Pass 1 reported, but
it changes their interpretation: the payables reduction and the payables-turnover ratio understate the
Company's reliance on financier-intermediated trade credit, which nearly doubled in absolute terms
this year. (Note 25.7(B), PDF p.84-85 standalone / p.115-116 consolidated) 🔴

### Note 2A Property, Plant & Equipment — gross capex evidence for the machined-components/castings programme (LBF-4), and interest capitalisation stopped
Pass 1's capital-commitments discussion (Section 3) found no cumulative programme figure but did not
report the underlying capex movement schedule. Note 2A shows gross PP&E additions of **₹17,535.61L**
(standalone) / **₹20,015.77L** (consolidated) during FY26 — the actual capex landing on the balance
sheet this year, evidencing progress on the machined-components/castings expansion the company memory
flags (LBF-4), even though no cumulative "₹290 Cr programme" figure appears anywhere in the notes.
CWIP fell from ₹6,047.06L to ₹4,184.32L standalone (₹6,297.31L→₹4,981.23L consolidated) as
₹20,382.11L (standalone) / ₹20,632.36L (consolidated) of CWIP was capitalised into completed assets
during the year. The CWIP ageing schedule shows 100% of the year-end balance aged under 2 years
(₹3,644.39L <1yr / ₹505.62L 1-2yr standalone; nothing beyond 2-3yr, nothing "temporarily suspended")
— no stalled or overrun projects, a clean signal on execution pace. Separately: interest capitalised on
qualifying-asset borrowings fell to **₹Nil** in FY26 from **₹410.81L** in FY25 (identical footnote both
statement sets) — meaning finance costs that would previously have been added to asset cost are now
flowing through the P&L interest line instead, a mechanical tailwind to reported finance costs that Pass 1's
borrowings review (which focused on rates and net debt) did not surface. (Note 2A, PDF p.72 standalone /
p.104 consolidated) 🟡

### Note 25.2 Contingent Liabilities — full YoY comparison shows a 37.6% increase, concentrated in bank guarantees, not visible in Pass 1's single-year table
Pass 1's contingent-liability table (Section 3) presented FY26 figures only. The note itself carries FY25
comparatives for every line, and the totals move as follows: **Total contingent liabilities ₹5,448.68L
(FY25) → ₹7,498.91L (FY26), +37.6%**. The increase is concentrated in: Bank guarantees ₹1,430.07L→
₹3,311.96L (**+131.6%**); Advance License non-performance duty ₹6.21L→₹302.97L (**+4,778%**, small
absolute base); the new GST appeal FY2018-2023 ₹0→₹491.14L (already flagged by Pass 1 as
subsidiary-only); partially offset by the AY2017-18 favourable resolution (-₹923.08L). Cross-referencing
Note 6D: the Term Deposits held as margin money for non-fund-based (NFB) limits — the collateral
typically backing bank guarantees — **fell** from ₹4,065.17L to ₹2,712.54L (**-33.3%**) over the same
period. Guarantee exposure roughly doubled while the margin cushion behind it shrank by a third; the
company's own explanation for either move is NOT FOUND IN DOCUMENT. Total contingent liabilities
remain a modest 7.6% of net worth per Pass 1's calculation, so this is a trend to monitor rather than an
acute concern, but the direction (both metrics) is worth a management question. (Note 25.2, PDF p.112
consolidated; Note 6D, PDF p.75 standalone / p.106 consolidated) 🟡

### Note 25.4C ESOP — options granted at a discount to the grant-date market price
Pass 1 flagged the ESOP expense jump and future unrecognised pool but did not examine the grant
economics. The fair-value table discloses: exercise price ₹736.72 vs **share price at the grant date
₹920.90** — the 7,87,500 options (13-Mar-2025 grant) were struck roughly **20% below** the then-market
price, not at-the-money. A discount grant is more generous to option holders than a standard at-market
ESOP and, combined with the long 8-year vesting/2-year cliff Pass 1 already noted, adds a further reason
the ~₹3,700L remaining expense pool (Pass 1 Finding #4) is a genuine, non-trivial future dilution/cost
item rather than a routine retention grant. Also on record in this note: 17,500 of the 7,87,500 options went
to Pitti Industries Pvt Ltd employees and 22,500 to Dakshin Foundry Pvt Ltd employees — parent-company
share dilution funding subsidiary-level retention. (Note 25.4C, PDF p.83 standalone / p.114 consolidated) 🟡

### Note 25.4 Employee Benefits — actuarial "Guaranteed Rate of Return" on gratuity plan assets collapsed
A new assumption line Pass 1 did not extract: "Guaranteed Rate of Return" on gratuity plan assets fell
from **6.83% (FY25) to 4.60% (FY26)** at the standalone (parent-only) level, and the consolidated
disclosure shows an even wider FY26 range of **1.60%-4.80%** (vs 6.83%-6.89% FY25) — implying at
least one subsidiary's insurer-managed fund now guarantees as little as 1.60%. This happens even as the
funded status improved (plan assets ₹835.94L→₹1,099.32L per Pass 1). A materially lower guaranteed
return on a growing asset base means slower future compounding of plan assets and, all else equal, higher
required employer cash contributions in later years to keep pace with the discount-rate-linked obligation
(itself up ~90bps this year per Pass 1). Likely reflects a shift in the underlying LIC/insurer fund product
mix rather than an error, but the magnitude of the drop (attributable rate roughly a third of last year's at
the low end) is disclosure-worthy and unexplained in the notes. (Note 25.4, PDF p.82 standalone / p.113
consolidated) 🟡

### Note 3B / 6E (standalone only) — a second, faster-growing ICD tranche to the wholly owned subsidiary
Pass 1's related-party section (Section 2) cited the CARO/Note 25.8 aggregate ICD figures (₹16,885.00L
given, ₹15,265.00L received back, ₹3,900.00L closing) but did not decompose the closing balance. It
splits across two separate notes: a **non-current** Inter Corporate Deposit Receivable from Related Party
(Note 3B) of ₹1,000.00L (FY26) vs ₹500.00L (FY25) — **+100% YoY** — and a **current** ICD Receivable
from Related Party (Note 6E) of ₹2,900.00L (FY26) vs ₹1,780.00L (FY25) — **+62.9% YoY**. These sum
exactly to the ₹3,900.00L CARO closing balance Pass 1 already anchored. The interest rate is still NOT
FOUND IN DOCUMENT for either tranche (consistent with Pass 1's finding), but the non-current portion
doubling — i.e., a growing share of subsidiary funding is now structured as longer-duration rather than
short-tenure rolling credit — is a new data point on how the parent is financing its wholly owned
subsidiary. Eliminated on consolidation; standalone-only. (Note 3B, PDF p.73 standalone; Note 6E, PDF
p.75 standalone) 🟡

### Note 25.7(B) Financial Risk Management — unhedged JPY borrowing exposure and quantified hedge ineffectiveness
Two granular items inside the note Pass 1 already flagged qualitatively (hedge accounting adoption):
(a) Foreign currency exposure "not covered by derivative instruments or otherwise" includes a **JPY
4,250.79 Lakhs borrowing (₹2,518.59L)** — a yen-denominated loan carried fully unhedged at FY26
year-end (down from JPY 5,188.44L/₹2,944.44L FY25, also unhedged). This JPY funding line was not
mentioned in Pass 1's borrowings review, which covered only the INR-denominated bank/other-lender
splits. (b) The first-year hedge-effectiveness disclosure quantifies: Changes in fair value of cash-flow-hedge
instruments recognised in OCI **-₹372.68L**, plus **hedge ineffectiveness recognised in profit or loss
-₹25.88L (cash flow hedge) and -₹7.20L (fair value hedge)** — a combined ₹33.08L direct P&L hit in the
adoption year, in addition to the -₹278.88L/-₹275.03L OCI reserve Pass 1 already reported. Also newly
noted: 1% FX move sensitivity on PBT rose sharply to ₹111.98L (FY26) from ₹18.92L (FY25), a ~5.9x
increase in disclosed currency-risk sensitivity Pass 1 did not quantify. (Note 25.7(B), PDF p.85-86
standalone / p.116-117 consolidated) 🟡

---

## MINOR / SUPPORTING (not separately ranked)
- Note 13A(a) shows the new ₹5,000L WCTL tranche and part of the "other lenders" term loan carry
  **7.30%-7.85% p.a.**, actually cheaper than the regular bank term-loan band (8.14%-8.65%) Pass 1 cited
  — the WCTL is the lowest-cost tranche in the new borrowing mix, not merely "at bank rates" as Pass 1's
  phrasing implied. (Note 10A, PDF p.77 standalone)
- Note 13D "Interest accrued" on borrowings rose ₹101.30L→₹244.86L (+141.7%), consistent with but not
  previously quantified alongside the higher gross debt base. (Note 13D, PDF p.78 standalone)
- Note 13C Trade Payables ageing: MSME dues are **100% "not due"** both years (₹483.60L FY26 /
  ₹350.48L FY25, zero in any overdue bucket) — a cleaner confirmation than Pass 1's general "~3% of
  total, compliant" framing. (Note 13C, PDF p.77 standalone)
- Note 25.9A's prior-year statutory-rate parenthetical is internally inconsistent: standalone reads
  "(2022-23: 25.168%)" and consolidated reads "(2023-24: 25.168%)" where both should read "2024-25" —
  an immaterial drafting/typo issue in the source document, not a numbers error (the 25.168% rate itself is
  correct and consistent both years). (Note 25.9A, PDF p.89 standalone / p.120 consolidated)
- Note 25.21 sensitivity-style disclosures for gratuity (Note 25.4) also give attrition-rate (±50%) and
  mortality-rate (±10%) sensitivities beyond the discount-rate figure Pass 1 cited: PBO moves to
  ₹2,159.81L/₹2,293.62L (attrition) and ₹2,216.11L/₹2,239.75L (mortality) — both modest relative to the
  discount-rate sensitivity, supporting rather than changing Pass 1's "appropriately sized" conclusion.

---

## PASS 2 NEW FINDINGS SUMMARY (ranked by investor importance)

1. **Note 25.21's own variance-disclosure formula is applied inconsistently, and the inconsistency happens
   to exempt the year's steepest profitability decline from explanation.** ROE fell 15.75%→10.63%, a
   -32.5% relative decline by the same formula the note uses for every other ratio row, comfortably past
   the company's stated 25% explanation threshold — yet the note reports only a -5.12 percentage-point
   change and gives no reason, because percentage-denominated rows are computed differently from
   ratio rows in the same table. (Note 25.21, PDF p.90 standalone) 🔴

2. **The FY26 effective-tax-rate jump (Pass 1 Finding #1) is mechanically explained by a ₹922-1,028L
   swing in the "book vs tax depreciation" deferred tax liability** — accelerated tax depreciation from the
   capex ramp is reversing, and that reversal (not cash tax strategy) drives the PAT decline. A timing item,
   but the multi-year unwind path is now a fair management question. (Note 25.9B, PDF p.89 standalone /
   p.120 consolidated) 🟡

3. **A supplier-finance/TReDS arrangement embedded in trade payables nearly doubled YoY to ₹83.85 Cr
   (of ₹94.03 Cr total under the arrangement)** — part of the FY26 "payables decline" narrative coexists
   with growing financier-intermediated trade credit that functions economically closer to short-term bank
   debt than ordinary vendor terms. (Note 25.7(B), PDF p.84-85 standalone / p.115-116 consolidated) 🔴

4. **Both subsidiaries — ~20% of consolidated revenue and the bulk of subsidiary profit — were audited by
   an unnamed "other auditor," not Talati & Talati**, with the group opinion resting solely on those
   unidentified reports. (Consolidated Auditor's Report, Other Matters, PDF p.92) 🟡

5. **Bank guarantee contingent liabilities more than doubled YoY (+131.6%, ₹14.3 Cr→₹33.1 Cr) while the
   margin money collateralising non-fund-based limits fell 33.3%** (₹40.7 Cr→₹27.1 Cr); total contingent
   liabilities grew 37.6% YoY, a trend invisible in Pass 1's single-year table. (Note 25.2, PDF p.112
   consolidated; Note 6D, PDF p.75 standalone / p.106 consolidated) 🟡

6. **Gross PP&E additions of ₹175-200 Cr in FY26 alone evidence real progress on the capex programme**
   (LBF-4), with a clean CWIP ageing profile (no project over 2 years, none suspended) — but interest
   capitalisation on qualifying assets dropped to Nil from ₹4.1 Cr FY25, pushing more finance cost through
   the P&L directly. (Note 2A, PDF p.72 standalone / p.104 consolidated) 🟡

7. **ESOP options were granted at ~20% below the grant-date market price** (exercise ₹736.72 vs share
   price ₹920.90), a more generous-than-at-market award structure underlying the ~₹37 Cr remaining
   expense pool Pass 1 already flagged. (Note 25.4C, PDF p.83 standalone / p.114 consolidated) 🟡

8. **The actuarial "Guaranteed Rate of Return" on gratuity plan assets collapsed from 6.83% to 4.60%
   (standalone) / as low as 1.60% (consolidated range) even as funded assets grew** — implies slower
   future compounding and likely higher required cash contributions ahead. (Note 25.4, PDF p.82
   standalone / p.113 consolidated) 🟡

9. **A second, non-current ICD tranche to the wholly owned subsidiary doubled YoY (₹5.0 Cr→₹10.0 Cr)**,
   alongside the current tranche (₹17.8 Cr→₹29.0 Cr, +62.9%), together reconciling to the ₹39.0 Cr CARO
   figure Pass 1 already cited but had not decomposed; interest rate still not disclosed. (Note 3B/6E,
   PDF p.73/75 standalone) 🟡

10. **An unhedged JPY 4,250.79 Lakh (₹25.19 Cr) borrowing sits outside derivative coverage**, and
    first-year hedge accounting recognised ₹33.08L of ineffectiveness directly in P&L plus a -₹372.68L OCI
    swing on cash-flow-hedge instruments — quantifying volatility Pass 1 flagged only qualitatively.
    (Note 25.7(B), PDF p.85-86 standalone / p.116-117 consolidated) 🟡

Count of new findings: **10 ranked + 5 minor/supporting = 15 total new items** (10 independently rated
findings above; 5 additional supporting/minor items listed in that section, not separately ranked).

---
Note numbering re-covered in Pass 2: STANDALONE Notes 2A, 3B, 6D, 6E, 10A, 13A, 13C, 13D, 25.2,
25.4, 25.4C, 25.7(B), 25.9A, 25.9B, 25.21; CONSOLIDATED equivalents plus the Consolidated
Independent Auditor's Report (Other Matters paragraph, PDF p.92) and CARO Annexure A (standalone,
PDF p.62-64, re-read, no new items beyond Pass 1).
