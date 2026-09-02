# CLEANMAX — HALT 1 EXTRACTION 01 (Claude Code → Claude web)

Run folder: runs/cleanmax-2026-09-01. Requested by Claude web 2026-09-02, produced by Claude Code 2026-09-02.
Purpose: close the open corpus questions between the draft Mental Model Declaration and operator sign-off. This is an EXTRACTION, not an analysis: quote-then-comment, corpus only, no new conclusions, no stage re-run.

**Unit convention:** source financial figures are in Rs million; converted to Rs Crore by dividing by 10 (Rs Cr = Rs mn / 10). Every table states its unit.
**Page-anchor convention:** each source has a page-tagged text twin (.txt) with "===== PAGE N =====" markers, where N is the exact PDF page. Anchors below cite the twin PAGE number; where a document's own printed page/slide/footer number differs, both are given. The AR segment note is **Note 55** (not Note 38; Note 38 is Contingent Liabilities) — a correction to earlier stage anchors.
**Provenance:** every quote is from a FILED document (AR, RHP, concalls, investor presentation, CARE press releases, results filings). No figure in Blocks A-I is taken from an operator-ferried SECONDARY file. See Block V.

## OPEN DISCREPANCIES FLAGGED (per Standing Rule 5; presented, not resolved)

These are points where the corpus disagrees with itself or with an earlier stage anchor. Each is flagged inside its block; this is an index only.
1. **FY26 operating-profit crossover reverses on rebuild** (Block A5): reported Adjusted PBT +Rs 22.02 Cr flips to -Rs 207.72 Cr at the FY25 capitalisation ratio, and -Rs 219.16 Cr with 25-yr depreciation restored. [COMPUTED, corpus-anchored inputs]
2. **Interest-capitalisation ratio** FY25 7.51% -> FY26 28.43% (Block A1). Q1 FY27 NOT DISCLOSED.
3. **CARE PAT differs across the two press releases** (Blocks B1, F7): FY24 +5 vs -38 Cr; FY25 +52 vs +19 Cr. The May-2026 PR matches the restated AR.
4. **Consolidated net-debt gap Rs 1,524.80 Cr** (Block F1): AR-derived Rs 11,208.80 Cr vs management-stated Rs 9,684 Cr at 31-Mar-2026; no corpus bridge.
5. **Useful-life change is "new technology" assets only, not the whole fleet** (Block A2); covered asset base NOT DISCLOSED.
6. **FY28 Rs 3,000 Cr guidance labelled both "reported" and "run-rate"** on the same slide; other-income treatment NOT DISCLOSED (Block B4).
7. **Operational-capacity base** 3,088 MW (nameplate) vs 3,643.94 MW/MWp (C&I operational) at 31-Mar-2026 (Blocks C2/C3); per-MW EBITDA computed on both.
8. **Koppal capacity** 529 MW (AR) vs 543 MW (Aug call) (Block E5); connectivity CTU confirmed.
9. **RHP carries a top-10 customer table (34.95%-45.39%)** (Block I1) against the consolidated "no single customer >10%" statement — closes an earlier NOT DISCLOSED.
10. **Rating label** AA- (call p.5) vs AA (call p.10) internal discrepancy (Block H1).
11. **NCI put-option cumulative liability IS disclosed** (Rs 19.20 Cr, Note 22) (Block D2) — corrects the earlier "cumulative not disclosed" note.
12. **BGTF share gap** of 39,223 shares between RHP post-Offer and AR 31-Mar-2026 (Block G4).

---
## BLOCK A — REBUILD THE OPERATING PROFIT CROSSOVER

### A1. Interest capitalisation, by period (consolidated)

Source, Note 36 (Finance costs), AR PAGE 431:

> *"Interest expense - on financial liabilities not classified at FVTPL ... 7,293.31 / 6,290.10
> ... - on lease liabilities ... 57.16 / 90.38 ... 7,378.86 / 6,391.15. Other borrowing costs
> ... 480.36 / 237.72 ... 7,859.22 / 6,628.87"*
> — AR twin PAGE 431, Note 36.

> *"36(b) Interest expenses of I1,685.78 Million (31st March, 2025: I334.17 Million) being directly
> attributable to construction of capital work-in-progress have been capitalised..."*
> — AR PAGE 431, footnote 36(b).

> *"36(c) Letter of Credit (LC) and Bank Guarantee charges of I1,267.55 Million (31st March, 2025:
> I204.45 Million) being directly attributable to construction of capital work-in-progress have been
> capitalised..."*
> — AR PAGE 431, footnote 36(c).

> *"36(e) Interest expenses on lease liabilities of I169.33 Million for the year ended 31st March,
> 2026 being directly attributable to construction of capital work-in-progress have been capitalised..."*
> — AR PAGE 431, footnote 36(e).

> *"(i) Interest expenses of I1,855.11 Million capitalised during the year ended 31st March, 2026
> (31st March, 2025: I334.17 Million)."*
> — AR PAGE 401, Note 3 (CWIP) footnote (i).

`Comment:` The CWIP footnote (i) figure 1,855.11 = 36(b) borrowing interest 1,685.78 + 36(e)
lease interest 169.33 [COMPUTED]. FY25 has no separate lease-interest capitalisation disclosed
(36(e) states an FY26 figure only), so FY25 capitalised interest = 334.17.

**Table A1 — Interest / borrowing cost capitalisation (Rs Crore, consolidated)**

| Item | FY25 | FY26 | Q1 FY27 |
|---|---|---|---|
| Interest expense charged to P&L (Note 36 subtotal) | 639.115 | 737.886 | **NOT DISCLOSED** (only total finance cost given) |
| Other borrowing costs charged to P&L | 23.772 | 48.036 | **NOT DISCLOSED** |
| **Finance cost charged to P&L (total)** | **662.887** | **785.922** | **254.711** |
| Interest capitalised to CWIP — borrowings (36b) | 33.417 | 168.578 | **NOT DISCLOSED** |
| Lease interest capitalised (36e) | **NOT DISCLOSED** (nil stated) | 16.933 | **NOT DISCLOSED** |
| Interest capitalised total (CWIP footnote i) | 33.417 | 185.511 | **NOT DISCLOSED** |
| LC / BG charges capitalised (36c) | 20.445 | 126.755 | **NOT DISCLOSED** |
| **Total borrowing cost capitalised** | **53.862** | **312.266** | **NOT DISCLOSED** |
| **Total borrowing cost incurred (P&L + capitalised)** | **716.749** | **1,098.188** | **NOT DISCLOSED** |
| **Capitalisation ratio = capitalised / total incurred** | **7.51%** | **28.43%** | **NOT DISCLOSED** |

Arithmetic [COMPUTED], Rs Crore:
- FY25 total incurred = 662.887 + 53.862 = 716.749; ratio = 53.862 / 716.749 = **7.51%**
- FY26 total incurred = 785.922 + 312.266 = 1,098.188; ratio = 312.266 / 1,098.188 = **28.43%**
- FY26 capitalised = interest 185.511 (168.578 + 16.933) + LC/BG 126.755 = 312.266
- FY25 capitalised = interest 33.417 + LC/BG 20.445 = 53.862

`Comment:` RE-VERIFY CONFIRMED. The FY25 capitalisation ratio 7.5% sits inside the flagged
7-10% band; the FY26 ratio 28.4% sits inside the flagged 28-30% band. Capitalisation as a share
of borrowing cost incurred nearly **quadrupled** year on year. Q1 FY27 discloses only the total
finance cost charged to P&L (254.711 Cr); neither the capitalised amount nor the total incurred
is disclosed, so the Q1 ratio cannot be computed and is not estimated.

---

### A2. Useful-life change (consolidated Note 2, footnote (vii))

> *"(vii) During the year ended 31st March, 2026, the Group conducted an operational efficiency
> review of its solar and wind assets. Based on the review, with effect from 1st January, 2026 the
> expected useful life of new technology solar and wind assets has been revised from 25 years to 30
> years. This change has been considered as change in estimate as per Ind AS 8 ... and has been
> accounted for prospectively in the Consolidated Financial Statements."*
> — AR twin PAGE 400, Note 2 footnote (vii).

> *"The effect of these changes on actual and expected depreciation expense (net of taxes) is as
> follows: ... Decrease in depreciation expense* 114.41 / 425.41 / 425.04 / 431.87 / 457.94 / 486.56
> ... Deferred tax impact (28.80)/(107.08)/(106.98)/(108.70)/(115.26)/(122.47) ... Net depreciation
> expense 85.61 / 318.33 / 318.06 / 323.17 / 342.68 / 364.09"*
> — AR twin PAGE 401 (quantification table).

**Table A2 — Useful-life change effect (Rs Crore, consolidated)**

| | FY26 | FY27 | FY28 | FY29 | FY30 | FY31 |
|---|---|---|---|---|---|---|
| Gross decrease in depreciation | 11.441 | 42.541 | 42.504 | 43.187 | 45.794 | 48.656 |
| Deferred tax impact | (2.880) | (10.708) | (10.698) | (10.870) | (11.526) | (12.247) |
| Net (after-tax) decrease | 8.561 | 31.833 | 31.806 | 32.317 | 34.268 | 36.409 |

- Effective date: **1st January, 2026** (change in estimate, Ind AS 8, prospective).
- Asset classes covered: **"new technology solar and wind assets"** only, NOT the whole fleet.
- Prior life: **25 years**. New life: **30 years**.
- FY26 depreciation reduction (gross): **11.441 Cr** (114.41 Mn).
- Stated annual reduction FY27-FY31 (gross): **42.541 / 42.504 / 43.187 / 45.794 / 48.656 Cr**.

`Comment:` The reduction applies to "new technology" assets only, not the whole fleet. The AR
does **NOT** quantify the covered asset base (no gross-block value of the "new technology solar
and wind assets" is disclosed in footnote (vii) or the table). Effective 1-Jan-2026 means the
FY26 benefit captures only one quarter (Q4 FY26) of a full year, which is why the FY26 gross
decrease (11.441 Cr) is roughly one-quarter of the FY27 run-rate (~42.5 Cr). Note the table row
labelled "Net depreciation expense" is the after-tax decrease, not a level. The standalone
version of the same change (AR PAGE ~470, footnote (vi)) is far smaller: FY26 gross decrease
7.75 Mn (0.775 Cr), FY27 onward 32.93 Mn (3.293 Cr) per year, and cites "Plant and Machinery."

---

### A3. Impairment discount-rate change (consolidated Note 2, footnote (iii))

> *"(iii) The Group and its joint ventures assessed Property, Plant and Equipment and capital work
> in progress for impairment ... Recoverable amount is determined as value-in-use, estimated using a
> discounted cash flow model based on internal projections of future revenues and operating costs,
> applying discount rates of 8%-11% (31st March, 2025: 10.5%) (based on WACC of market benchmarks).
> ... Depreciation for the year includes impairment of I17.45 Million (31st March, 2025: INil)."*
> — AR twin PAGE 400, Note 2 footnote (iii).

- Prior methodology: **single point-estimate discount rate of 10.5%** (as at 31 March 2025).
- New methodology: **discount-rate range of 8%-11%** (as at 31 March 2026), based on WACC of
  market benchmarks.
- Quantified effect of the rate change on the impairment charge: **NOT DISCLOSED** (the AR does
  not isolate the impact of moving from a 10.5% point estimate to an 8%-11% range).
- Impairment charge itself: **FY26 1.745 Cr (17.45 Mn), included within depreciation; FY25 Nil.**

`Comment:` The impairment charge is immaterial either way (1.745 Cr FY26 against depreciation of
379.912 Cr). The move to a rate *range* whose low end (8%) is below the prior point estimate (10.5%)
would, other things equal, raise recoverable values and suppress impairment, but the AR quantifies
no such effect. Documents checked: consolidated Note 2 footnote (iii) PAGE 400; consolidated Note 3
(CWIP) footnote (v) PAGE 401 (cross-refers to Note 2 footnote (iii), no separate quantum).

---

### A4. Other income decomposition (Note 31 consolidated; Q1 FY27 filing)

> *"Note 31 Other income ... Gain on investments in mutual funds (net) 63.31 / 72.25 ... Interest
> income: - on deposits with banks 490.32 / 384.89 - on loans given to related parties 12.47 / 9.03
> - on employee loans 1.31 / 0.77 - amortisation of financial liability 0.31 / 1.98 - income tax
> refund 2.69 / 4.57 ... Gain on modification of borrowing terms - / 241.36 ... Net foreign exchange
> gain 86.83 / 15.38 ... Sundry balances written back 0.10 / 2.59 ... Gain on sale of property, plant
> and equipment (net) 54.74 / 26.81 ... Gain on change of ownership interest in subsidiary - / 275.00
> ... Profit on derecognition of ROU 1.53 / - ... Cash flow hedges - ineffective portion of changes
> in fair value 715.35 / - ... Other non-operating income 194.45 / 111.78 ... 1,623.41 / 1,146.41"*
> — AR twin PAGE 428, Note 31.

> *"31(b) Includes insurance claim settlement amounting to I82.13 Million (31st March, 2025: I73.37
> Million). 31(c) Includes unrealised mark to market income of I11.13 Million for the year ended 31st
> March 2026."*
> — AR twin PAGE 429, footnotes 31(b), 31(c).

**Table A4 — Other income lines and classification (Rs Crore, consolidated)**

| Line | FY25 | FY26 | Class | Basis |
|---|---|---|---|---|
| Mutual fund gain (net) | 7.225 | 6.331 | RECURRING (treasury) | Deployment of surplus; FY26 includes 1.113 non-cash MTM (31(c)) |
| Interest on bank deposits | 38.489 | 49.032 | RECURRING | Cash interest on deposits |
| Interest on RP loans | 0.903 | 1.247 | RECURRING | Cash interest |
| Interest on employee loans | 0.077 | 0.131 | RECURRING | Cash interest |
| Amortisation of financial liability | 0.198 | 0.031 | NON-CASH | EIR unwind, no cash |
| Interest on income-tax refund | 0.457 | 0.269 | ONE-OFF | Non-operating, event-driven |
| Gain on modification of borrowing terms | 24.136 | 0.000 | ONE-OFF / NON-CASH | FY25 only; refinancing gain |
| Net foreign exchange gain | 1.538 | 8.683 | ONE-OFF | Volatile, non-operating |
| Sundry balances written back | 0.259 | 0.010 | ONE-OFF | Provision reversal |
| Gain on sale of PPE (net) | 2.681 | 5.474 | ONE-OFF | Asset disposal |
| Gain on change of ownership in subsidiary | 27.500 | 0.000 | ONE-OFF / NON-CASH | FY25 only; step-acquisition fair-value gain (31(a)) |
| Profit on derecognition of ROU | 0.000 | 0.153 | ONE-OFF / NON-CASH | Lease derecognition |
| Cash flow hedges - ineffective portion | 0.000 | 71.535 | NON-CASH | MTM on hedge ineffectiveness |
| Other non-operating income | 11.178 | 19.445 | MIXED | Incl. insurance claim 8.213 (FY26) one-off (31(b)); balance unspecified |
| **Total other income** | **114.641** | **162.341** | | matches P&L |

**Class sums, FY26 (Rs Crore) [COMPUTED]:**
- RECURRING (cash interest + realised treasury) = 49.032 + 1.247 + 0.131 + (6.331 - 1.113 MTM = 5.218) = **55.628**
- NON-CASH = amortisation 0.031 + hedge 71.535 + ROU 0.153 + MTM 1.113 = **72.832**
- ONE-OFF = tax refund 0.269 + FX 8.683 + sundry 0.010 + PPE 5.474 + insurance 8.213 = **22.649**
- Ambiguous "other non-operating" ex-insurance = 19.445 - 8.213 = **11.232**
- One-off + non-cash (excl. ambiguous) = 72.832 + 22.649 = **95.481 = 58.8% of 162.341**
- The single cash-flow-hedge line alone = 71.535 / 162.341 = **44.1%**

`Comment:` RE-VERIFY of the "~45% one-off-or-non-cash" claim: **CONFIRMED, and it is a floor.**
The non-cash cash-flow-hedge ineffectiveness line (71.535 Cr) by itself is 44.1% of FY26 other
income. A full classification puts one-off-plus-non-cash at 58.8% (excluding the 11.232 Cr
ambiguous "other non-operating" remainder) or 65.7% including it. FY25 one-off-plus-non-cash was
~39.5% (excl. ambiguous), driven by the borrowing-modification gain (24.136 Cr) and the
step-acquisition gain (27.500 Cr).

**Q1 FY27 other income:** the Q1 FY27 filing reports other income as a **single line of 41.946 Cr
(419.46 Mn)** with **NO Note-31 breakdown** (Statement of Unaudited Consolidated Financial Results,
results twin PAGE 22, line item "Other income"). The recurring / one-off / non-cash split for
Q1 FY27 is therefore **NOT DISCLOSED** and is not estimated.

---

### A5. THE REBUILD TABLE (Rs Crore, consolidated)

Columns: **(a)** As reported | **(b)** capitalisation restated to the FY25 ratio (7.51%) |
**(c)** depreciation restated to 25-year lives | **(d)** both (b) and (c).

Adjustment mechanics [COMPUTED]:
- Column (b), FY26: capitalised at FY25 ratio = 7.51% x 1,098.188 = 82.53 Cr; additional finance
  cost pushed to P&L = actual capitalised 312.266 - 82.53 = **229.74 Cr**; restated finance cost =
  785.922 + 229.74 = **1,015.66 Cr**. FY25 is the reference year, so (b) = (a) for FY25.
- Column (c): add back the useful-life-change depreciation decrease. FY26 add-back = **11.441 Cr**
  (A2 gross). FY25 unaffected (change effective 1-Jan-2026, after FY25 year-end), so (c) = (a) for FY25.
- Recurring other income added (A4): FY25 **46.69 Cr**, FY26 **55.63 Cr**.

**FY25 (Rs Crore)**

| Row | (a) As reported | (b) cap @ FY25 ratio | (c) dep @ 25-yr | (d) both |
|---|---|---|---|---|
| Operating profit (EBITDA ex other income) | 900.431 | 900.431 | 900.431 | 900.431 |
| less finance cost | (662.887) | (662.887) | (662.887) | (662.887) |
| less depreciation | (299.990) | (299.990) | (299.990) | (299.990) |
| Operating PBT before other income | (62.446) | (62.446) | (62.446) | (62.446) |
| add recurring other income only | 46.690 | 46.690 | 46.690 | 46.690 |
| **Adjusted PBT** | **(15.76)** | **(15.76)** | **(15.76)** | **(15.76)** |

`Comment:` FY25 is the reference year for both adjustments, so all four columns are identical.

**FY26 (Rs Crore)**

| Row | (a) As reported | (b) cap @ FY25 ratio | (c) dep @ 25-yr | (d) both |
|---|---|---|---|---|
| Operating profit (EBITDA ex other income) | 1,132.222 | 1,132.222 | 1,132.222 | 1,132.222 |
| less finance cost | (785.922) | (1,015.66) | (785.922) | (1,015.66) |
| less depreciation | (379.912) | (379.912) | (391.353) | (391.353) |
| Operating PBT before other income | (33.612) | (263.35) | (45.05) | (274.79) |
| add recurring other income only | 55.630 | 55.630 | 55.630 | 55.630 |
| **Adjusted PBT** | **22.02** | **(207.72)** | **10.58** | **(219.16)** |

`Comment:` The reported FY26 crossover to a positive operating PBT-plus-recurring-income
(Adjusted PBT 22.02 Cr, column a) is fragile. Restating capitalisation alone to the prior-year
ratio (column b) moves finance cost up 229.74 Cr and Adjusted PBT to -207.72 Cr. Restating
depreciation alone to 25-year lives (column c) still leaves Adjusted PBT marginally positive
(10.58 Cr). Both together (column d) give -219.16 Cr. The capitalisation-ratio step is the larger
lever by an order of magnitude.

**Q1 FY27 (Rs Crore)**

| Row | (a) As reported | (b) cap @ FY25 ratio | (c) dep @ 25-yr | (d) both |
|---|---|---|---|---|
| Operating profit (EBITDA ex other income) | 420.916 | cannot build | 420.916 | cannot build |
| less finance cost | (254.711) | cannot build | (254.711) | cannot build |
| less depreciation | (114.634) | cannot build | (125.269)* | cannot build |
| Operating PBT before other income | 51.571 | cannot build | 40.94 | cannot build |
| add recurring other income only | NOT DISCLOSED | cannot build | NOT DISCLOSED | cannot build |
| **Adjusted PBT** | **NOT DISCLOSED** (recurring split) | **cannot build** | **NOT DISCLOSED** | **cannot build** |

*Q1 FY27 column (c) depreciation add-back = one-quarter of the FY27 annual useful-life-change
decrease = 42.541 / 4 = 10.635 Cr [COMPUTED, proration]. The AR discloses the FY27 effect on an
annual basis only; the quarterly split is a straight proration, not a disclosed figure.

`Comment:` Column (b) for Q1 FY27 **cannot be built**: Q1 FY27 interest capitalisation is
NOT DISCLOSED (A1), so the FY25-ratio restatement has no capitalised base to redistribute. Column
(d) likewise cannot be built. No figure is estimated. The recurring-other-income add for Q1 FY27
is NOT DISCLOSED because the Q1 filing gives other income as a single line with no breakdown (A4).
The Operating-PBT-before-other-income row (51.571 Cr reported, 40.94 Cr at 25-year lives) is the
furthest the rebuild can go for Q1 FY27 on disclosed data.

---

---

## BLOCK B — EBITDA BASIS RECONCILIATION

### B1. Every EBITDA figure in the corpus

**Table B1 (Rs Crore unless the source labels otherwise)**

| Label used | Value | Period | Document | Page/anchor |
|---|---|---|---|---|
| EBITDA (A-B, reported, incl. other income) | 1,015.072 | FY25 | AR consol P&L | twin PAGE 374 |
| EBITDA (A-B, reported, incl. other income) | 1,294.563 | FY26 | AR consol P&L | twin PAGE 374 |
| EBITDA (A-B, reported, incl. other income) | 462.862 | Q1 FY27 | Results (consol) | results twin PAGE 22 |
| EBITDA (A-B, reported, incl. other income) | 274.899 | Q1 FY26 | Results (consol) | results twin PAGE 22 |
| EBITDA (A-B, reported, incl. other income) | 349.742 | Q4 FY26 | Results (consol) | results twin PAGE 22 |
| Reported EBITDA | 742 | FY24 | Presentation | pres PAGE 10, line "Reported EBITDA" |
| Reported EBITDA | 1,015 | FY25 | Presentation | pres PAGE 10 |
| Reported EBITDA | 1,295 | FY26 | Presentation | pres PAGE 10; AR highlights PAGE ~247; May-2026 call |
| EBITDA (highlights strip) | ~1,295 (vs ~1,015 FY25) | FY26 | AR highlights | twin PAGE ~247 |
| EBITDA "C. Earnings before interest, tax, deprec... (A-B)" | 741.573 | FY24 | RHP restated | pros twin PAGE 108-109 |
| EBITDA "C. ... (A-B)" | 405.919 | FY23 | RHP restated | pros twin PAGE 108-109 |
| EBITDA(1) (Non-GAAP, glossary defn ex other income) | 1,015.072 (tabled) | FY25 | RHP | pros twin PAGE 50 (defn), footnote (1) |
| Adjusted EBITDA | 494 (4,940 Mn) | Q1 FY27 | Presentation | pres PAGE 9 (line 220), PAGE 6 (line 135) |
| Adjusted EBITDA | 284 (2,839 Mn) | Q1 FY26 | Presentation | pres PAGE 9 (line 220) |
| Cash EBITDA (basis) | 494 (74% YoY) | Q1 FY27 | Aug-2026 call | concall Aug line 451 |
| Adjusted reported EBITDA | 494 | Q1 FY27 | Aug-2026 call | concall Aug line 464 |
| Run-Rate EBITDA (RE Power Sales) | 1,870 | as of 31-Mar-2026 / 1-Apr-2026 | AR + Presentation + May/Mar calls | AR PAGE 249 & 355; pres PAGE 10; May-2026 call line 228 |
| Run-Rate EBITDA (RE Power Sales) | 1,140 | as of 1-Apr-2025 | Presentation | pres PAGE 10 (line 254) |
| Run-Rate EBITDA (RE Power Sales) | 950 | as of 1-Apr-2024 | Presentation | pres PAGE 10 (line 254) |
| CARE PBILDT | 706 | FY24 (A) | CARE PR 12-Oct-2025 | rating Oct twin, line 301 |
| CARE PBILDT | 900 | FY25 (A) | CARE PR 12-Oct-2025 | rating Oct twin, line 301 |
| CARE PBILDT* | 706 / 900 / 1,132 | FY24 / FY25 / FY26 (A) | CARE PR 12-May-2026 | rating May twin, lines 257-258 |
| Operating profit per P&L (revenue less operating expenses, before other income / deprec / finance) | 706.101 | FY24 | RHP restated (13,898.37 - 6,837.36) | pros twin PAGE 108-109 [COMPUTED] |
| Operating profit per P&L | 900.431 | FY25 | AR (14,957.01 - 5,952.70) | twin PAGE 374 [COMPUTED] |
| Operating profit per P&L | 1,132.222 | FY26 | AR (19,128.73 - 7,806.51) | twin PAGE 374 [COMPUTED] |
| Operating profit per P&L | 420.916 | Q1 FY27 | Results (8,321.56 - 4,112.40) | results twin PAGE 22 [COMPUTED] |

`Comment:` Three distinct "EBITDA" bases run through the corpus. (1) The **P&L-format "EBITDA
(A-B)"** in the AR, RHP and results filings is Total income minus expenses, so it **includes
other income** (1,015 / 1,295 Cr for FY25/FY26). (2) **CARE PBILDT** is struck on Total Operating
Income and **excludes other income**, equalling the P&L operating profit (706 / 900 / 1,132 Cr).
(3) **Run-rate EBITDA** (1,870 Cr) is a forward, estimated, RE-Power-Sales-only figure, not an
actual result (see B5). A fourth, **Adjusted EBITDA** (494 Cr Q1 FY27), is defined as gross margin
minus cash SG&A. Note the definitional inconsistency: the RHP glossary (PAGE 50, footnote 1) and
the presentation footnote (pres PAGE 9, note 2) both **define** EBITDA as revenue minus operating
costs **excluding other income**, yet the numbers each document tabulates under "EBITDA" are the
A-B figures that **include** other income (e.g. presentation Q1 FY27 EBITDA 4,629 Mn = the A-B
figure, not 4,209 Mn ex other income). The stated definition and the tabulated number diverge by
exactly other income.

---

### B2. Reconcile reported EBITDA to operating profit — FY24, FY25, FY26

> *"C. Earnings before interest, tax, depreciation, impairment and amortisation (EBITDA) (A - B)"*
> — RHP restated P&L, pros twin PAGE 108-109; AR consol P&L, twin PAGE 374.

Reported EBITDA (A-B) less operating profit (revenue less operating expenses) [COMPUTED, Rs Crore]:

| | Reported EBITDA (A-B) | Operating profit (rev - opex) | Difference | Other income | Match? |
|---|---|---|---|---|---|
| FY24 | 741.573 | 706.101 | 35.472 | 35.472 | YES |
| FY25 | 1,015.072 | 900.431 | 114.641 | 114.641 | YES |
| FY26 | 1,294.563 | 1,132.222 | 162.341 | 162.341 | YES |

Arithmetic:
- FY24: EBITDA 741.573 - operating profit (1,389.837 - 683.736) 706.101 = 35.472 = other income
  (total income 1,425.309 - revenue 1,389.837 = 35.472).
- FY25: 1,015.072 - (1,495.701 - 595.270) 900.431 = 114.641 = other income (1,610.342 - 1,495.701).
- FY26: 1,294.563 - (1,912.873 - 780.651) 1,132.222 = 162.341 = other income (2,075.214 - 1,912.873).

`Comment:` **CONFIRMED.** In each of FY24, FY25 and FY26 the company's reported "EBITDA (A-B)"
equals operating profit plus other income exactly. The company's reported EBITDA therefore
**includes other income**. This is visible in the P&L structure itself: the AR/RHP compute
"C. EBITDA = A (Total income, which is revenue + other income) minus B (expenses)". CARE's PBILDT
(706 / 900 / 1,132 Cr) equals the operating profit and confirms the same reconciliation from the
other side: reported EBITDA - CARE PBILDT = other income (35 / 115 / 162 Cr). The RHP/presentation
footnote definition of EBITDA (excluding other income) is not the number they tabulate.

---

### B3. The Aug-2026 (Q1 FY27) call EBITDA bridge

> *"We are also delighted that our EBITDA has increased about 74% to about INR494 crores for this
> quarter."* — Concall Aug-2026, line 254.

> *"The EBITDA given the mix of the two segments has grown 74% on a cash EBITDA basis, and on a
> reported basis, it's a 68% increase to INR462 crores compared to INR274 crores."*
> — Concall Aug-2026, line 451-452.

> *"...what is the breakup of EBITDA? It's INR494 crores is the adjusted reported EBITDA. But in our
> business, there are projects which are operational, as the start of the year, has already been fully
> stabilized and been operating. So that represent close to INR334 crores of EBITDA come from that out
> of INR494. 7% EBITDA comes from the RE services business, and the remaining, which is INR125 crores
> of the EBITDA in the quarter is primarily from the project which is commissioned in the last 12
> months..."* — Concall Aug-2026, lines 464-471.

Labels and figures:
- **Rs494 Cr** = "adjusted reported EBITDA" (line 464), also stated as EBITDA up "74%" (line 254)
  and "74% on a cash EBITDA basis" (line 451). Equals presentation Adjusted EBITDA 4,940 Mn.
- **Rs462 Cr** = reported EBITDA, "68% increase ... compared to INR274 crores" (line 452). Equals
  the P&L A-B figure 462.862 Cr and prior-year 274.899 Cr.
- **Rs494 Cr decomposition** (by asset cohort): Rs334 Cr from assets stabilised at start of year +
  ~7% / ~Rs35 Cr from RE Services + Rs125 Cr from assets commissioned in the last 12 months.
  334 + 35 + 125 = 494 [COMPUTED].

Does the transcript bridge Rs494 to Rs462? **NOT DISCLOSED in the transcript.** The call
decomposes the Rs494 Cr adjusted figure by asset cohort (334 + 35 + 125) but does **not** verbally
state the reconciling items between adjusted Rs494 Cr and reported Rs462 Cr. It points listeners to
the slide: *"the next slide, which is Page number 17"* (line 462-463). That slide (Presentation
PAGE 18, "EBITDA breakdown by Cohort", in Rs million) supplies the bridge:

> *"...3,349 ... 1,255 ... 336 ... 4,940 ... -311 ... 4,629 ... Projects operational > 1 year /
> Projects operational < 1 year / RE Services / Adjusted EBITDA* / Non Cash expense* / Reported EBITDA
> ... Non Cash expense of 311 Mil consists of net unrealized foreign exchange loss, ESOP amortization
> expenses and such other notional expenses."* — Presentation PAGE 18 (lines 469-492).

`Comment:` The 494-to-462 bridge exists **only in the presentation, not in the transcript**:
Adjusted EBITDA 4,940 Mn (= 3,349 + 1,255 + 336) less a Non-Cash expense of 311 Mn = Reported
EBITDA 4,629 Mn [COMPUTED]. In Rs Crore: 494 - 31 (non-cash) = 463 (~462). The Rs31 Cr non-cash
plug is net unrealised FX loss + ESOP amortisation + other notional items, computed at SPV level.
The call's 334 + 35 + 125 split is a decomposition **of the Rs494 Cr adjusted figure**, not a
reconciliation to the Rs462 Cr reported figure.

---

### B4. The FY28 guidance basis

> *"...we will have a minimum EBITDA of INR3,000 crores in FY28, which is nearly 2.4x the EBITDA in
> FY26."* — Concall Aug-2026, lines 148-149.

> *"...we will have a minimum reported EBITDA in FY28 of about INR3,000 crore."*
> — Concall Aug-2026, line 324.

> *"FY28 Guidance ... Based on Minimum 4.6 GW Capacity (Opex Sales) as of 1 April 2027 ... Reported
> EBITDA (FY28) Min. INR 3,000 Cr ... Steady State Net Debt INR 16,000 Cr ... Run-rate EBITDA of INR
> 3,000 crore ... Represents 2.3x growth over FY26 reported EBITDA of INR 1,295 crore."*
> — Presentation PAGE 10, lines 306-311.

> *"3. Reported EBITDA = full-year run-rate assets + partial-year ramp-up from new commissioning;
> this ratio has averaged ~1.1x prior-year Run-Rate EBITDA ... for FY28, we expect a minimum Reported
> EBITDA of INR3,000 Cr."* — Presentation PAGE 10, notes, lines 314-317.

> *Questioner: "...INR3,000 crores EBITDA for FY28. This is from renewable power sale only, right? Or
> is it including the renewable energy service as well?"* / *Kuldeep Jain: "Yeah, we give a
> corporate-level EBITDA guidance, which obviously includes both."* — Concall Aug-2026, lines 1050-1055.

From the quotes only:
- **(i) Labelled?** Primarily **"reported EBITDA"** (call line 324; presentation "Reported EBITDA
  (FY28) Min. INR 3,000 Cr"). The SAME presentation slide **also** calls it "Run-rate EBITDA of INR
  3,000 crore" (line 310). Labelling is **mixed / inconsistent within the same slide**; "reported"
  is the dominant and more recent label.
- **(ii) Includes RE Services?** **YES.** *"we give a corporate-level EBITDA guidance, which
  obviously includes both"* (line 1055).
- **(iii) Includes other income?** **NOT DISCLOSED.** Neither the call nor the slide states whether
  the Rs3,000 Cr is struck on the A-B basis (which includes other income) or ex other income.
- **(iv) Tied to what capacity base, as of what date?** **"Minimum 4.6 GW Capacity (Opex Sales) as
  of 1 April 2027"** (presentation PAGE 10, line 307-308), with corresponding steady-state net debt
  of Rs16,000 Cr.

`Comment:` The FY28 Rs3,000 Cr figure is anchored to 4.6 GW of opex-sales capacity as of 1-Apr-2027
and is stated to include both segments. It carries two different labels ("reported EBITDA" and
"run-rate EBITDA") on the same slide, and its treatment of other income is not disclosed. Growth
multiple quoted as 2.3x over FY26 reported EBITDA 1,295 Cr (presentation) or "nearly 2.4x the EBITDA
in FY26" (call) [both source-stated].

---

### B5. Run-rate EBITDA Rs1,870 Cr

> *"Following our successful public listing, run-rate EBITDA grew 64% to INR1,870 Crore, supported by
> strategic partnerships, such as with Osaka Gas, and a reduced project debt cost of 8.5%."*
> — AR MD&A, twin PAGE 355 (lines 21031-21033).

> *"...5.7 GW Contracted RE Power Sales Capacity ... 1.4 GW Commissioned in FY 2026 ... INR1,870 Crore
> Run-Rate EBITDA..."* — AR business-overview metrics strip, twin PAGE 249 (lines 12900-12902).

> *"~1,870 Cr Run-Rate EBITDA from capacity commissioned ... Run Rate EBITDA and Net Debt for capacity
> commissioned ... As of March 31, 2026 ... RE Power Sales Capacity 3,088 MW (2,442 Solar, 646 Wind)
> ... Run-Rate EBITDA1 (RE Power Sales) ... 1,870 Cr (+730 Cr) ... Note: 1. Based on estimated
> generation (P90 wind, P75 solar) applied on contracted capacity and standard EBITDA margins."*
> — Presentation PAGE 10 (lines 244-268).

> *"Run-rate EBITDA means as of that point in the financials, in this case 31st [March 2026] ... That
> run-rate EBITDA number is about INR1,870 crore. This grew from a starting point run-rate EBITDA of
> about INR1,140 crores as of 1st April 2025 ... what we have historically seen is that the reported
> EBITDA is about 1.1x the run-rate EBITDA."* — Concall May-2026 (Q4 FY26), lines 225-233.

Answer from the quotes:
- **Capacity:** RE Power Sales operational/commissioned capacity of **3,088 MW as of 31-Mar-2026**
  (2,442 solar, 646 wind); the AR strip ties it to 1.4 GW commissioned in FY26 and 5.7 GW contracted.
- **As of what date:** **31 March 2026 / 1 April 2026** (start of FY27).
- **What "run-rate" includes:** the presentation defines the calculation as **estimated generation
  (P90 wind, P75 solar) applied to capacity, multiplied by standard EBITDA margins, for the RE Power
  Sales segment only.** It is a forward, modelled, annualised figure, **not** an actual reported
  result, and it **excludes RE Services**.

`Comment:` The AR itself (PAGE 249, 355) gives the Rs1,870 Cr figure and the "grew 64%" framing but
does **NOT** define what run-rate includes; the definition ("estimated generation P90/P75 x standard
margins, RE Power Sales only") comes from the **presentation** (PAGE 10, note 1) and the **May-2026
call** ("EBITDA from all operational assets as on that [date]"). Two internal inconsistencies to
flag: (a) the presentation header says "capacity **commissioned**" while its own footnote 1 says
"**contracted** capacity" as the base; (b) run-rate EBITDA is RE-Power-Sales-only, whereas the FY28
Rs3,000 Cr guidance (B4) is corporate-level including RE Services, so the two are not like-for-like.
Management's stated rule of thumb is that reported EBITDA runs at ~1.0x to 1.1x the prior-year-end
run-rate EBITDA (FY25 reported 1,015 = ~1.1x of 950; FY26 reported 1,295 = ~1.1x of 1,140).

---

## BLOCK C — PER-MEGAWATT ECONOMICS

### C1. RE Power Sales segment P&L (revenue and segment EBITDA / segment result)

Two anchored authorities. The AR segment note (labelled **Note 55**, not Note 38; Note 38 in the consolidated statements is Contingent Liabilities) carries only FY26 and FY25. FY24 comes from the investor presentation and the RHP.

*"Segment revenue ... (a) Segment A - Renewable Energy Power Sales 13,994.50 [FY26] ... 11,072.48 [FY25]"* and *"Segment EBITDA ... (a) Segment A - Renewable Energy Power Sales 12,322.24 [FY26] ... 9,552.70 [FY25]"* and *"Segment results ... (a) Segment A - Renewable Energy Power Sales 5,457.72 [FY26] ... 3,247.74 [FY25]"* — AR twin PAGE 682-683 (printed AR p.468-469), Note 55.
Comment: AR "Segment EBITDA" for RE Power Sales = the segment operating EBITDA before unallocable. "Segment results" = EBITDA less depreciation/finance treatment per the note. AR gives no FY24 in this note.

*"Revenue from Operations -RE Power Sales segment ₹ million 5,282.57 [Q1 FY27] 3,581.73 [Q1 FY26] 13,994.50 [FY26] 11,072.48 [FY25] 8,663.33 [FY24] ... Adjusted EBITDA -RE Power Sales segment ₹ million 4,604.21 [Q1 FY27] 2,802.65 [Q1 FY26] 12,322.25 [FY26] 9,552.70 [FY25] 6,670.92 [FY24]"* — Investor_Presentation_1.txt twin PAGE 28 (printed slide 27).
Comment: Presentation labels the metric "Adjusted EBITDA - RE Power Sales segment". Its FY26 value 12,322.25 matches AR Note 55 Segment EBITDA 12,322.24 (rounding). FY25 9,552.70 matches exactly. So AR "Segment EBITDA" and presentation "Adjusted EBITDA of the segment" are the same series. FY24 segment adjusted EBITDA = 6,670.92 Mn is disclosed only here (and RHP), not in AR Note 55.

RHP confirms FY24 restated RE Power Sales revenue: *"- Renewable Energy Power Sales ₹ million 7,192.15 [H1 FY26] 5,736.14 [H1 FY25] 11,072.48 [FY25] 8,663.33 [FY24] 4,748.15 [FY23]"* — RHP_Prospectus_2026-02-25.txt line ~1636 / ~4194.
Comment: RHP FY24 RE Power Sales revenue 8,663.33 Mn matches the presentation. RHP restated total revenue from operations FY24 = 13,898.37 Mn (note this differs from the presentation "Total income" FY24 of 14,253.09 Mn, which includes other income; not a segment-level discrepancy).

**RE Power Sales segment P&L (Rs Crore; source Rs million / 10)**

| Period | Segment revenue (Cr) | Segment EBITDA / Adj. EBITDA (Cr) | Segment result (Cr) | Anchor |
|---|---|---|---|---|
| FY24 | 866.33 | 667.09 | **NOT DISCLOSED** (AR Note 55 lacks FY24; RHP gives revenue only in this table) | Pres. twin PAGE 28 |
| FY25 | 1,107.25 | 955.27 | 324.77 | AR twin PAGE 682-683 (Note 55); Pres. twin PAGE 28 |
| FY26 | 1,399.45 | 1,232.22 (AR) / 1,232.23 (Pres.) | 545.77 | AR twin PAGE 682-683 (Note 55); Pres. twin PAGE 28 |
| Q1 FY26 (Jun-25) | 358.17 | 280.27 | **NOT DISCLOSED** (segment result not split quarterly) | Pres. twin PAGE 28 |
| Q1 FY27 (Jun-26) | 528.26 | 460.42 | **NOT DISCLOSED** (segment result not split quarterly) | Pres. twin PAGE 28 |

Comment: Q1 figures are from management "Summary of financial performance" (presentation), footnoted *"Numbers for Jun'25 are indicative, based on draft management financials"* (Pres. twin PAGE 28). Segment result (EBIT-like) is disclosed only annually in AR Note 55; quarterly segment result is NOT DISCLOSED (docs checked: presentation twin PAGE 28, AR Note 55 twin PAGE 682-683).

### C2. Operational RE Power Sales capacity at period end

Two disclosed bases that do NOT agree. Both are shown; the difference is definitional (nameplate/AC MW vs MWp/DC), flagged per standing rule 5.

**Basis A — "RE Power Sales Capacity" (nameplate/AC MW; used in the state-wise and run-rate slides).**
*"RE Power Sales Capacity ... 1,341 MW [1-Apr-24] ... 1,712 MW (1,276 Solar, 436 Wind) [1-Apr-25] ... 3,088 MW (2,442 Solar, 646 Wind) [31-Mar-26]"* — Investor_Presentation_1.txt twin PAGE 10 (printed slide 9).
*"Total 3,088 [1-Apr-26] ... 3,493 [30-Jun-26] ... 3,493 MW as of June 30, 2026 comprises 2,791 MWp solar (80%) (DC Capacity) and 701 MW wind (20%)"* — twin PAGE 7 (printed slide 6). (1-Apr-2026 = 31-Mar-2026 close.)
RHP confirms: *"Total Renewable Energy Power Sales Capacity 2,310.32 [Sep-25] 1,508.42 [Sep-24] 1,712.79 [FY25] 1,342.26 [FY24] 754.51 [FY23]"* — RHP line ~4216.

**Basis B — "C&I Operational Capacity" (MWp DC for solar; the KPI slide and the 13 GW table).**
*"C&I Operational Capacity MW 4,174.43 [Jun-26] 2,213.32 [Jun-25] 3,643.94 [FY26] 2,177.99 [FY25] 1,755.21 [FY24]; Solar (Onsite) MWp 535.74 / 462.76 / 515.64 / 448.57 / 396.09; Solar (Offsite) MWp 2,795.84 / 1,192.59 / 2,340.72 / 1,171.44 / 850.64; Wind MW 842.85 / 557.98 / 787.58 / 557.98 / 508.48"* — Investor_Presentation_1.txt twin PAGE 26 (printed slide 25).

**Operational capacity by period end and split (MW / MWp as labelled)**

| Period end | Basis A total (MW) | Basis B total (MW/MWp) | Onsite solar (MWp) | Offsite solar (MWp) | Wind (MW) | CTU solar (MWp) |
|---|---|---|---|---|---|---|
| 31-Mar-2024 | 1,341 / 1,342.26 (RHP) | 1,755.21 | 396.09 | 850.64 | 508.48 | NA |
| 31-Mar-2025 | 1,712 / 1,712.79 (RHP) | 2,177.99 | 448.57 | 1,171.44 | 557.98 | NA |
| 31-Mar-2026 | 3,088 | 3,643.94 | 515.64 | 2,340.72 | 787.58 | 525 |
| 30-Jun-2025 | ~1,743 TTM add ref only | 2,213.32 | 462.76 | 1,192.59 | 557.98 | NA |
| 30-Jun-2026 | 3,493 | 4,174.43 | 535.74 | 2,795.84 | 842.85 | 525 |

Hybrid split: the KPI table folds hybrid into offsite solar + wind (twin PAGE 26 notes 17-19). Discrete operational hybrid MW is **NOT DISCLOSED** as a standalone line; only hybrid PLF is given (see C7). Docs checked: presentation twin PAGE 7/10/26/34/35, AR MD&A twin PAGE 355.

**DISCREPANCY FLAG (Basis A vs Basis B).** For 31-Mar-2026, Basis A = 3,088 MW (2,442 solar + 646 wind) vs Basis B = 3,643.94 MW/MWp (2,856.36 solar MWp + 787.58 wind). Solar differs by ~414 (AC-vs-MWp/DC convention) and wind differs by ~142 (Basis B includes the wind component of hybrid). Same company, same date, two conventions. The 13 GW table (twin PAGE 35, printed slide 34) and the KPI table (twin PAGE 26) agree with each other (both Basis B); the state-wise and run-rate slides (twin PAGE 7/10) are Basis A. This denominator choice materially changes the per-MW ratios in C3.

Connectivity split of operational capacity (Q1 FY27, Basis-B MW): *"STU – Group Captive 48% 1,995 MW; STU – Third Party Open Access 13% 554 MW; CTU 13% 525 MW; Onsite Solar 10% 419 MWp; Capex (STU + Onsite) 16% 682 MW"* against *"Q1 FY27 4,174 MW"* — twin PAGE 34 (printed slide 33). (Carried into E2.)

### C3. EBITDA per average operational MW [COMPUTED]

Average MW = (opening + closing) / 2, per instruction. Segment EBITDA from C1 (Rs Crore). Computed both denominators because C2 discloses two capacity bases; both shown, arithmetic explicit.

Segment adjusted EBITDA used (Cr): FY25 = 955.27; FY26 = 1,232.22; Q1 FY27 = 460.42, annualised x4 = 1,841.68.

**Denominator Basis A (RE Power Sales nameplate MW):** opening/closing 1,341 → 1,712 → 3,088; Jun-26 = 3,493.
- FY25 avg MW = (1,341 + 1,712) / 2 = 1,526.50. EBITDA/avg MW = 955.27 / 1,526.50 = 0.6258 Cr/MW = **Rs 62.6 Lakh/MW** [COMPUTED]
- FY26 avg MW = (1,712 + 3,088) / 2 = 2,400.00. EBITDA/avg MW = 1,232.22 / 2,400.00 = 0.5134 Cr/MW = **Rs 51.3 Lakh/MW** [COMPUTED]
- Q1 FY27 annualised, in-quarter avg MW = (3,088 + 3,493) / 2 = 3,290.50. Annualised EBITDA/avg MW = 1,841.68 / 3,290.50 = 0.5597 Cr/MW = **Rs 56.0 Lakh/MW** [COMPUTED]

**Denominator Basis B (C&I Operational Capacity MW/MWp):** 1,755.21 → 2,177.99 → 3,643.94; Jun-26 = 4,174.43.
- FY25 avg = (1,755.21 + 2,177.99) / 2 = 1,966.60. 955.27 / 1,966.60 = 0.4858 Cr/MW = **Rs 48.6 Lakh/MW** [COMPUTED]
- FY26 avg = (2,177.99 + 3,643.94) / 2 = 2,910.97. 1,232.22 / 2,910.97 = 0.4233 Cr/MW = **Rs 42.3 Lakh/MW** [COMPUTED]
- Q1 FY27 annualised, in-quarter avg = (3,643.94 + 4,174.43) / 2 = 3,909.19. 1,841.68 / 3,909.19 = 0.4711 Cr/MW = **Rs 47.1 Lakh/MW** [COMPUTED]

Comment: the ratio is denominator-sensitive. Basis A (nameplate) yields Rs 51-62 Lakh/MW, which sits near the blended steady-state neighbourhood. Basis B (MWp DC) yields Rs 42-49 Lakh/MW because MWp inflates the solar denominator. This is a factual sensitivity, not a conclusion; Block V/valuation must pick the denominator that matches the EBITDA basis. Note also the ratios are un-adjusted for the ramp lag (C6) and for Bikaner curtailment (Block E), both of which depress realised MW-productivity below steady state.

**B04 steady-state derivation (as reported by B04).** *"Per-MW/MWp run-rate EBITDA by technology ... Solar ₹50-55 Lakh/MWp; Wind ₹100-110 Lakh/MW (Inv. Pres. p.10)"* and *"margin_per_unit: portfolio EBITDA margin 83-84%; Solar Rs50-55 Lakh/MWp, Wind Rs100-110 Lakh/MW run-rate EBITDA"* — outputs/reports/04-bizmodel.md lines 138, 369.
How B04 got there: B04 took the figures directly off the presentation "Key Unit Economics" slide (Investor_Presentation_1.txt twin PAGE 11, printed slide 10) — *"EBITDA SOLAR 50 - 55 INR Lakhs / MWp; WIND 100 - 110 INR Lakhs / MW"* — no independent computation; it is a transcription of management's stated steady-state unit economics, not a derived value. B04 flags the read-across test: *"Below guided range signals PLF shortfall or tariff erosion"* (04-bizmodel.md line 138).
Comment: management's steady-state solar figure (50-55 Lakh/MWp) is per MWp DC (Basis B units). The blended Basis-B computed FY26 figure (Rs 42.3 Lakh/MW) sits below the solar-only steady-state band, consistent with (a) a wind share pulling the blend, (b) the ramp lag, and (c) curtailment drag. Stated as arithmetic reconciliation only.

### C4. Tariff series

| Label | Value | Period / basket | Anchor |
|---|---|---|---|
| Wtd-avg tariff, PPAs commissioned during year (TTM) — FY24 | Rs 4.12 /kWh | FY24 | Pres. twin PAGE 27 (printed slide 26), row (15) |
| — FY25 | Rs 3.76 /kWh | FY25 | Pres. twin PAGE 27 |
| — FY26 | Rs 3.57 /kWh | FY26 | Pres. twin PAGE 27 |
| — Q1 FY27 (TTM to Jun-26) | Rs 3.59 /kWh | TTM Jun-26 | Pres. twin PAGE 27 |
| — Q1 FY26 (TTM to Jun-25) | Rs 3.77 /kWh | TTM Jun-25 | Pres. twin PAGE 27 |
| Wtd-avg realised tariff (portfolio, revenue ÷ generation) | Rs 4.06 / 4.14 / 4.20 / 4.28 / 4.47 | Jun-26 / Jun-25 / FY26 / FY25 / FY24 | Pres. twin PAGE 27, row (14) |
| Operational portfolio tariff (3.5 GW) | Rs 3.93 /kWh | as of Q1 FY27 | Pres. twin PAGE 11 (slide 10); Aug call printed p.5-6 |
| Contracted-under-execution tariff (2.6 GW basket) | Rs 3.85 /kWh | as of 31-Mar-2026 | AR twin PAGE 249 (printed AR p.16-17); May call printed p.6 |
| Contracted-under-execution tariff (2.5 GW basket) | Rs 4.00 /kWh | as of 30-Jun-2026 | Pres. twin PAGE 11 & 15 (slides 10, 14); Aug call printed p.6 |

Anchored quotes:
*"Weighted average tariff for PPAs commissioned during year (trailing 12 months)(15) Rs / kWH 3.59 [Jun-26] 3.77 [Jun-25] 3.57 [FY26] 3.76 [FY25] 4.12 [FY24]"* — Pres. twin PAGE 27.
*"the operational portfolio tariff is about INR3.93 per unit of power. This is for the existing capacity of 3.5 gigawatt, and what is under execution, so ... 2.5 gigawatt is contracted under execution, that is at a tariff level of INR4"* — Concall_Aug_2026, printed p.5 (twin PAGE 6). Repeated printed p.6: *"We have a great tariff locked in for the next 2.5 gigawatt, it's about INR4 or so"* (twin PAGE 7).
*"₹3.85/kWh Weighted Average Tariff for Contracted Under Execution Capacity"* set against *"5.7 GW Contracted RE Power Sales Capacity"* and *"1.4 GW Commissioned in FY 2026"* — AR twin PAGE 249 (printed AR p.16-17).
*"if you look at our tariff for 2,600 MW which is contracted and under execution ... contracted at an average tariff of about INR3.85 per unit of power and this is about 70% solar, 30% wind"* — Concall_May_2026, printed p.6 (twin PAGE 7).
*"INR 4.00/kWh Tariff for 2.5 GW contracted (under execution) capacity"* against *"2.5 GW RE Power Sales Capacity Contracted under execution (as of June 30, 2026)"* — Pres. twin PAGE 15 (printed slide 14).

**Reconciliation of Rs 3.85 vs Rs 4.00 (same basket? date? definition?).** Same definition (weighted-average tariff of the contracted-yet-to-execute book, 70% solar / 30% wind, negligible storage). Different snapshot date and different basket size: Rs 3.85 is the 2.6 GW book as of 31-Mar-2026 (AR FY26 and the May-2026 call); Rs 4.00 is the 2.5 GW book as of 30-Jun-2026 (Q1 FY27 presentation and Aug-2026 call). The book shrank 2.6 → 2.5 GW as projects executed out, and management states tariff levels are *"stabilizing to rising"* (Aug call twin PAGE 6), so the residual/newer basket carries the higher Rs 4.00 average. NOT the same basket; the pair is reconciled by date and basket composition, not a contradiction.

### C5. Capex per MW

*"Capital Expenditure SOLAR 3.5 INR Cr / MWp | WIND 7.8 INR Cr / MW"* and footnote *"Note: 1. Excluding soft cost which is ~5-7% of the overall capital expenditure. 2. Typical solar - wind capacity split is 70% solar and 30% wind."* — Investor_Presentation_1.txt twin PAGE 11 (printed slide 10).
Comment: task's "presentation p.10" = printed slide 10 = twin PAGE 11. Soft cost is additive on top of the Rs 3.5 / Rs 7.8 hardware capex, at ~5-7%.

Historical capex-per-MW actuals for commissioned projects: **NOT DISCLOSED** as a per-MW rupee actual. The only actual-vs-budget disclosure is a ratio, not a per-MW figure: *"Budget vs Actual costs 95.54% [FY24] 95.24% [FY25] 97.20% [FY26] 97.89% [Current]"* — Pres. twin PAGE 15 (printed slide 14), where *"Actual cost refers to the construction cost incurred towards projects commissioned in the respective fiscals (excluding the cost of land); Budgeted cost refers to cost ... at the inception of the project"*. Consolidated gross block is disclosed (₹1,28,232 Mn FY26 per 04-bizmodel.md line 44) but not divided per MW in the corpus. Aug call declines a Q1 capex figure: *"No, we can't ... we don't have a breakup of fixed assets growth, but we can maybe get back to you offline"* (Aug printed p.13, twin PAGE 15). Docs checked: presentation twin PAGE 11/15, AR MD&A, Aug concall.

### C6. Stabilisation lag

*"First is post any COD, like you have achieved a commissioning, or you are ready to begin operations, it takes about three to six months for revenue stabilization."* — Concall_May_2026, printed p.4 (twin PAGE 5).
Continuation: *"This happens due to various factors, technical plant stabilization, some documentation may happen, some regulatory final-final approval may take time, there may be a ramp-up phase."* — May printed p.4-6 (twin PAGE 6).

Corroborating / additional ramp-up statements:
*"Post COD, STU Projects takes 3-6 months for revenue stabilization due to technical plant stabilization, customer open access documentation and other regulatory approvals"* and *"In our 525 MW CTU project in Rajasthan – grid backdowns expected over next 6-12 months due to ongoing transmission system upgradation"* — Investor_Presentation_1.txt twin PAGE 10 (printed slide 9).
*"STU projects typically take 3–6 months to stabilize post-commissioning (open access/regulatory approvals), while CTU projects like Bikaner-II - Initial grid evacuation availability will have a limited impact on ramp-up"* — Pres. twin PAGE 11 (printed slide 10, footer text).
Debt-seasoning (a different, longer clock, not revenue stabilisation): *"stabilized which typically takes a 9 months to 12 months, then the debt against it becomes fully"* and *"for the project which are stabilized and been operating for more than 12 months"* — Concall_May_2026 printed p.15-16 area (twin PAGE ~15-16). Reported in Aug: *"close to INR334 crores of EBITDA"* tied to assets *"operating ... some are still maybe stabilizing"* — Aug printed p.7 (twin PAGE 8).
Comment: two distinct clocks disclosed. Revenue stabilisation = 3-6 months post-COD (STU). Debt/full financial stabilisation = 9-12 months. Both anchored above.

### C7. PLF series

TTM PLF by technology (twin PAGE 26, printed slide 25; the fullest table):
*"Plant Load Factor (trailing 12 months): Solar Onsite (DC PLF) 16.16% [Jun-26] 15.66% [Jun-25] 14.41% [FY26] 14.86% [FY25] 15.11% [FY24]; Solar Offsite (AC(DC PLF)) 25.43% (17.33%) [Jun-26] 24.17% (16.66%) [Jun-25] 24.60% (16.80%) [FY26] 24.65% (16.98%) [FY25] 23.06% (16.19%) [FY24]; Wind 35.42% / 34.04% / 35.10% / 31.60% / 34.52%; Hybrid 47.60% / 47.61% / 45.18% / 45.90% / 39.18%"* — Investor_Presentation_1.txt twin PAGE 26.

TTM PLF at Jun-2025 and Jun-2026 (task-requested cut), also shown rounded on twin PAGE 15 (printed slide 14: Wind 34%/35%, Solar Offsite 24%/25%, Hybrid 48%/48%):

| Technology | TTM to 30-Jun-2025 | TTM to 30-Jun-2026 | Anchor |
|---|---|---|---|
| Solar Onsite (DC PLF) | 15.66% | 16.16% | Pres. twin PAGE 26 |
| Solar Offsite (AC / (DC)) | 24.17% (16.66%) | 25.43% (17.33%) | Pres. twin PAGE 26 |
| Wind | 34.04% | 35.42% | Pres. twin PAGE 26 |
| Hybrid | 47.61% | 47.60% | Pres. twin PAGE 26 |

Quarterly (single-quarter) PLF by technology: **NOT DISCLOSED**. Management explicitly reports PLF on a TTM basis only and declined a single-quarter cut: *"in our KPI, we referred to PLF on a trailing 12 months basis, because of seasonality, that's the right way to evaluate rather than within one quarter"* — Concall_Aug_2026 printed p.13 (twin PAGE 15).

Generation figures (disclosed, quarterly-equivalent): *"Generation Exported(1) Mn kWH 1,302.36 [Q1 FY27] 852.16 [Q1 FY26] 3,343.42 [FY26] 2,615.92 [FY25] 1,932.68 [FY24]"* — Pres. twin PAGE 26. Solar-wind split of quarterly generation is **NOT DISCLOSED** (offered offline only: Aug printed p.13, twin PAGE 15).

Mar-2026 promise to provide the missing quarterly data (task-referenced):
*"Maybe we will ... provide that in due course on our website ... on a continued basis every quarter in terms of million units of generation."* — Concall_Mar_2026, printed p.9-10 area (twin PAGE ~11), in reply to a request for quarterly generation Q3 FY25–Q3 FY26.
*"I acknowledge though to the participant who pointed it out previously that that data is not split on a quarter-by-quarter basis and going forward we will provide that."* — Concall_Mar_2026, printed p.17-18 area (twin PAGE ~20), referring to the slide-23 PLF/generation table.
Comment: task cited "Mar-2026 p.11/p.17". The two promise statements sit at twin PAGE ~11 and ~20 (printed p.9-10 and p.17-18). Both concern the same gap: quarterly (non-TTM) generation and PLF. As of the Aug-2026 call the quarterly PLF split remained undisclosed.

---

---

## BLOCK D — The Minority / SPV Cohort

### D1. Non-controlling interest (Note 20(B))

FY25 and FY26 are from AR Note 20(B) (page 422). FY24 is from the RHP Restated Consolidated financials (the AR shows only FY26 and FY25 columns).

Source quote FY26/FY25, *"(B) Non-controlling interests ... Balance at the beginning of the year 6,412.93 / 4,005.11 ... Profit for the year attributable to NCI (85.55) / (84.14) ... Change in NCI due to additional investments 3,492.86 / 3,264.02 ... Balance at the end of the year 8,852.69 / 6,412.93"* (AR twin p.422).

Source quotes FY24 (RHP restated): NCI profit share *"Non-controlling interests ... (84.14) (66.55) 57.96"* (RHP twin p.110, columns FY25 / FY24 / FY23); closing balance *"(c) Non-controlling interests 7,325.22 3,537.61 6,412.93 4,005.11 2,580.13"* (RHP twin p.107, columns Sep-25 / Sep-24 / FY25 / FY24 / FY23); NCI capital injected *"Proceeds from issue of shares to Non-Controlling Interests (NCI) in subsidiaries ... 3,264.02 1,763.67 1,445.95"* (RHP twin p.111, columns FY25 / FY24 / FY23).

| Item (₹ million) | FY24 (RHP restated) | FY25 (AR) | FY26 (AR) |
|---|---|---|---|
| NCI share of profit/(loss) | (66.55) | (84.14) | (85.55) |
| NCI capital injected during year | 1,763.67 | 3,264.02 | 3,492.86 |
| Closing NCI balance | 4,005.11 | 6,412.93 | 8,852.69 |

| Item (₹ Crore) `[COMPUTED ÷10]` | FY24 | FY25 | FY26 |
|---|---|---|---|
| NCI share of profit/(loss) | (6.66) | (8.41) | (8.56) |
| NCI capital injected during year | 176.37 | 326.40 | 349.29 |
| Closing NCI balance | 400.51 | 641.29 | 885.27 |

`Comment:` NCI loses money at the profit line in all three years (a loss attributable to minorities each year), yet minorities injected fresh capital every year (Rs 176.37 Cr FY24, Rs 326.40 Cr FY25, Rs 349.29 Cr FY26) and the closing NCI balance more than doubled FY24 to FY26. FY25 labels differ across the two docs but agree on the number: the AR calls the injection *"Change in NCI due to additional investments"* (3,264.02) and the RHP calls it *"Proceeds from issue of shares to NCI in subsidiaries"* (3,264.02). The FY24 injection figure (1,763.67) is the RHP cash-flow line; the AR does not carry an FY24 column.

### D2. Put option liability to minorities (Note 38 / redemption liability)

The put option itself is a qualitative commitment in Note 38(ii) *"Other commitments"* (AR p.442): *"In respect of few subsidiaries of the Parent Company, the Parent Company has put option obligations in respect of 26% shareholding held by the other non-controlling interest shareholders of those subsidiaries which are exercisable at the termination of the contract, completion of the power purchase agreement or the breach of performance obligation by the Parent Company, as applicable. These put options are exercisable at fair market value of the underlying shares of such subsidiaries at the time of the exercise of the option by the non-controlling interest shareholder of those respective subsidiaries."* (AR twin p.442).

The recognised liability sits in **Note 22, Other non-current financial liabilities**, as *"Redemption liability [Refer footnote 22(a)] 191.98 / 91.06"* (AR twin p.424), with footnote 22(a): *"The Parent Company has contractual obligation to purchase shares issued to non controlling interest shareholders, to be settled in cash by the Parent Company, is recognised at present value of the redemption amount as a financial liability and is reclassified from equity."* (AR twin p.424).

Accounting policy (z), AR p.397: *"The Parent Company is writer of the put option to the non-controlling interest (NCI) shareholders in specific subsidiaries to acquire the entire shareholding at a predetermined fixed exercise price where the right to exercise is with NCI shareholders. ... The present value of the amount payable under this contract is recorded under financial liability, reflecting the Parent Company's obligation to purchase the shares of the NCI shareholders. The difference between the present value and the amount paid by NCI has been recognized under Other equity."* (AR twin p.397-398).

The annual transfer is in the NCI reconciliation: *"Transfer to other financial liabilities (85.23) / (91.06)"* (AR Note 20B, twin p.422). Rs 85.23 million = **Rs 8.52 Cr** `[COMPUTED ÷10]` for FY26.

**Cumulative liability: STATED.** The cumulative put/redemption liability carried on the balance sheet is **Rs 191.98 million = Rs 19.20 Cr** `[COMPUTED ÷10]` at 31-Mar-2026 (FY25: Rs 91.06 million = Rs 9.11 Cr).

`Comment:` The question asked whether only the annual transfer (Rs 8.52 Cr) is stated or the cumulative liability. The corpus discloses **both**: the FY26 transfer of Rs 8.52 Cr (Note 20B) and the cumulative closing balance of Rs 19.20 Cr (Note 22). The two do not sum cleanly (FY25 close 91.06 + FY26 transfer 85.23 = 176.29 vs FY26 close 191.98; the Rs 15.69 million gap is unexplained in the note, plausibly discount unwinding or fair-value re-measurement, but the AR does **NOT DISCLOSED** the reconciling movement). The put is struck at fair market value / predetermined price on the NCI's 26% blocks; the recognised Rs 19.20 Cr is the present value the Parent has booked, not the gross fair-value exposure of those blocks.

### D3. Ownership structure of operational capacity

Disclosed ownership data in the corpus:

**(a) Material-NCI subsidiaries (Note 51, AR p.481).** *"Clean Max Eliora Private Limited India 26% 26% ... Clean Max Sapphire Private Limited India 26% 26% ... Clean Max Alpha LeaseCo FZCO* United Arab Emirates 50% 50%"* — these are the **NCI** percentages, so parent economic interest is 74%, 74% and 50% respectively (AR twin p.481).

**(b) Related-party ownership annexure (AGM Notice, Annexure A1, AR p.64).** A 13-name list of material-RPT subsidiaries with *"% Shareholding of the listed entity"*:

| Entity | % held by CMEESL |
|---|---|
| Clean Max Ajanta Private Limited | 74% |
| Clean Max Terra Private Limited | 74% |
| Clean Max Vayu Private Limited | 80% |
| Clean Max Ahhope Private Limited | 100% (Wholly Owned) |
| Clean Max Astria Private Limited | 74% |
| Clean Max BIAL Renewable Energy Private Limited | N/A (Step-down) |
| Clean Max Como Private Limited | 74% |
| Clean Max Eliora Private Limited | N/A (Step-down) |
| Clean Max Kenai Private Limited | 51% |
| Clean Max Ni Private Limited | 100% (Wholly Owned) |
| Clean Max Prithvi Private Limited | 51% |
| Clean Max Scorpius Private Limited | N/A (Step-down) |
| Kanoo Cleanmax Renewables Assetco WLL | N/A (Joint Venture, Bahrain) |

(AR twin p.64). Also seen in the RPT explanatory schedule: Clean Max Patagonia 74% (AR twin p.64, Sr. 10).

`Comment:` The corpus confirms the ownership ladder the question named — the recurring parent stakes are **100%, 80%, 74%, 51%** — and 74% is the modal structure (the 26% NCI put block). But this list is the **material-RPT subset**, not the full subsidiary universe (the CARO Annexure alone names 103 Indian entities, D4). The AR does **not** publish a complete subsidiary-by-subsidiary ownership schedule with AOC-1-style percentages in the text twin.

**Capacity-weighted average parent economic interest: NOT DISCLOSED (cannot compute).** The corpus does not map operational MW to individual subsidiaries. Note 51 gives MW/ownership for only three material-NCI names; the AGM annexure gives ownership for 13 names with no MW; the investor presentation twin (`inputs/presentation/Investor_Presentation_1.txt`, 37 pages) gives segment MW splits but no per-subsidiary ownership. The "44% Group Captive" figure the prompt cites (presentation p.33 / block B07) is a **business-model / offtake-structure split of RE Power Sales MW, not an ownership percentage**, and this twin does not contain that page. A capacity-weighted parent economic interest therefore cannot be built from the filed corpus without estimating the missing MW-to-entity map. Docs checked: AR Notes 50 & 51, AGM Annexures A1/A2, `Investor_Presentation_1.txt`.

### D4. CARO Annexure A (consolidated), AR p.365-370

This is the auditor's clause (xxi) consolidation of subsidiary CARO qualifications (B S R & Co. LLP, dated 15 May 2026).

- **Total entities listed: 103** (Sr. No. 1 to 103, AR twin p.365-370), plus the Holding Company itself as entry 1.
- **Entities flagged under Clause (xvii): 93** `[COMPUTED — count]`. Tally of the "Clause number ... which is unfavourable or qualified or adverse" column across the table: 92 rows read "Clause (xvii)" plus 1 typo row "Cluase (xvii)" (Sr. 6, Clean Max Energy Ventures) = 93. Two of the 93 carry (xvii) alongside a second clause — Sr. 8 CMES Jupiter (*"Clause (xvii) and Clause (i)(c)"*) and Sr. 101 Clean Max Sapphire (*"Clause (i)(c) and Clause (xvii)"*). Other clause counts in the same table: Clause (i)(c) 8, Clause (ix)(d) 2, Clause (xix) 1, Clause (vii)(a) 1 (all AR twin p.365-370).

`Comment:` Clause (xvii) under CARO 2020 = whether the company incurred cash losses in the financial year **and** in the immediately preceding financial year. The consolidated Annexure cites clause **numbers only**; it does **NOT DISCLOSED** the restated clause text or the rupee cash-loss amount per entity. 93 of the ~103 listed entities carrying the two-year cash-loss flag is consistent with a fleet of freshly commissioned / under-construction SPVs (many CINs are 2024 and 2025 incorporations). One data quirk in the AR itself: "Clean Max Ilgohp" appears twice (Sr. 89 and Sr. 92, same CIN PTC459619) — counted as listed.

- **Clean Max Patagonia, Clause (xix) — verbatim row:** *"62 Clean Max Patagonia Private Limited U35105MH2024 PTC425532 Subsidiary Clause (xix)"* (AR twin p.368). Patagonia is the **only** entity in the entire consolidated Annexure flagged under Clause (xix), and it is **not** on the (xvii) list.

`Comment:` CARO 2020 Clause (xix) = the auditor's opinion on whether any material uncertainty exists about the company meeting its liabilities within one year of the balance-sheet date (a liquidity / going-concern-adjacent flag). The Annexure states the clause number only; the underlying uncertainty language is **NOT DISCLOSED** in the consolidated report (it would sit in Patagonia's own component CARO). Patagonia is separately the Rs 216.25 Cr RPT counterparty (D6).

- **Four entities whose component auditor CARO reports were not issued at the report date** (AR p.370): *"The above does not include comments, if any, in respect of the following entities as the CARO report relating to them has not been issued by its auditor till the date of principal auditor's report."* — the four named:
  1. Clean Max Celestial Private Limited (U35105MH2024PTC416964)
  2. Clean Max Yamuna Private Limited (U35105MH2024PTC436005)
  3. Clean Max Tasman Private Limited (U35105MH2025PTC446402)
  4. Clean Max Polar Private Limited (U35105MH2025PTC446419)
  (AR twin p.370).

- **FY25 comparable count: NOT DISCLOSED.** The RHP twin carries no CARO clause-level count or clause (xvii) enumeration (grep for "CARO" / "clause (xvii)" / "cash losses" in `RHP_Prospectus_2026-02-25.txt` returns nothing). Docs checked: RHP twin, AR CARO consolidated Annexure (FY26 only).

### D5. Covenant breach

**Consolidated — Note 37.1 Capital Management, quoted in full** (AR twin p.432):

*"37.1 Capital Management. The Group and its joint ventures manages its capital to ensure that it will be able to continue as a Going Concern while maximising the return to stakeholders through the optimisation of debt and equity balance."*

*"Gearing Ratio — The Capital structure of the Group consists of net debt and total equity. The gearing ratio at the end of the year is as follows: Total Debt (i) 1,24,107.64 / 79,736.98 ; Less: Cash and cash equivalents 12,019.60 / 3,285.85 ; Net Debt (A) 1,12,088.04 / 76,451.13 ; Total Equity 55,235.35 / 32,047.73 ; Less: Cash flow hedge reserve 4,109.74 / - ; Total adjusted equity (B) 51,125.61 / 32,047.73 ; Net debt to adjusted equity ratio [A/B] 2.19 / 2.39. (i) Total Debt is defined as sum of current & non-current borrowings (including current maturities). (ii) Capital is defined as Equity share capital, other equity including non controlling interest and excluding cash flow hedge reserve."*

*"No changes were made in the objectives, policies or processes for managing capital during the year ended 31st March, 2026. In order to achieve this overall objective, the Group and its joint ventures's capital management, amongst other things, aims to ensure that it meets financial covenants attached to the interest-bearing loans and borrowings that define capital structure requirements. Breaches in meeting the financial covenants would permit the lender to immediately call loans and borrowings. In FY 2025-2026, there were certain financial loan covenants that were triggered, however the same were rectified during the year. The financial covenant for any interest-bearing loans and borrowings is tested as per the contractual agreements with lenders and management expects to meet all covenants till 31st March, 2027."* (AR twin p.432).

**Standalone — Note 37 Capital Management (parent complied)** (AR twin p.793): *"... the Company's capital management, amongst other things, aims to ensure that it meets financial covenants attached to the interest-bearing loans and borrowings that define capital structure requirements. Breaches in meeting the financial covenants would permit the lender to immediately call loans and borrowings. The financial covenant for any interest-bearing loans and borrowings is tested as per the contractual agreements with lenders. As at March 31, 2026, the Company has outstanding term loan classified as non current borrowings. In accordance with the terms of the agreement, the Company is required to make principle and interest payments on specified due dates subsequent to the reporting date and to comply with certain quantitative and qualitative covenants. The Company has complied with all principle and interest payments and covenants as at March 31, 2026, and based on its current cash flow forecasts, expects to continue to comply with these requirements going forward."* (AR twin p.793).

**Named facility / lender / SPV with an FY26 covenant breach or waiver: NOT DISCLOSED.** The consolidated note says *"certain financial loan covenants ... were triggered ... rectified during the year"* without naming any facility, lender, or subsidiary. The RHP twin discloses no named FY26 breach/waiver either (searches for "covenant" in the RHP return only sanction-letter boilerplate and going-concern policy text, no named breach). Docs checked: AR consolidated Note 37.1, AR standalone Note 37, full AR grep for "covenant"/"waiver"/"breach", RHP grep for "covenant".

`Comment:` The breach is real and admitted, but it is a **consolidated (SPV-level) event, not a parent event** — the parent standalone note asserts full compliance. The AR positions it as triggered-then-rectified within FY26, with forward comfort only to 31-Mar-2027. The specific SPVs and lenders are not named; the 93-entity clause (xvii) cash-loss cohort (D4) is the population where such triggers would arise.

### D6. Patagonia RPT ceiling (AGM Notice, Resolution 31)

*"31. To approve Material Related Party Transactions with Clean Max Patagonia Private Limited a Subsidiary of the Company ... approval of the members of the Company be and is hereby accorded to the Company to continue with the existing contract(s)/arrangement(s)/ transaction(s) more specifically set out in the explanatory statement ... between the Company and Clean Max Patagonia Private Limited a Subsidiary, for an aggregate value up to INR 216.25 crore, subject to such contract(s)/arrangement(s)/transaction(s) being carried out at arm's length and in the ordinary course of business of the Company."* (AR twin p.19, AGM Notice Resolution 31).

**Nature of transactions** (AGM explanatory RPT schedule, AR twin p. mid-Notice): *"10 Clean Max Enviro Energy Solutions Limited | Clean Max Patagonia Private Limited | 1. EPC 2. O&M 3. ICL 4. Guarantee | Refer Note (a) | 216.25"*.

`Comment:` The Rs 216.25 Cr ceiling covers four transaction types with the 74%-held Patagonia SPV: **EPC** (engineering, procurement, construction of the project), **O&M** (operations and maintenance), **ICL** (inter-corporate loan) and **Guarantee**. It is an approval *ceiling* to continue existing arrangements at arm's length, not a booked FY26 amount. Patagonia is also the sole Clause (xix) liquidity flag in the CARO Annexure (D4).

---

---

## BLOCK E — GRID CONNECTIVITY

### E1. Evacuation capacity table (presentation, full quote)

Source: Investor_Presentation_1.txt twin PAGE 35 (printed slide 34), title *"13 GW Portfolio as of Jun'2026 continued momentum on commissioning & contracting"*. Columns are As-on Mar-31-2025 / Mar-31-2026 / Jun-30-2026, each split Solar MWp / Wind MW / Total MW. Full quote of the Evacuation rows and the totals:

*"Evacuation Available4 — STU - Connected: 487 [Mar25 solar] 120 [Mar25 wind] | 1,687 [Mar26 solar] 652 [Mar26 wind] | 1,703 [Jun26 solar] 430 [Jun26 wind]; CTU - Connected: 232 301 | 677 616 | 677 615. [Evacuation Available totals: 1,140 (Mar25) / 3,632 (Mar26) / 3,424 (Jun26)]"*
*"Evacuation Applied5 — STU - Connected: 704 270 | 466 189 | 669 254; CTU - Connected: - 700 | - 1,045 | - 1,745. [Evacuation Applied totals: 1,674 (Mar25) / 1,700 (Mar26) / 2,668 (Jun26)]"*
*"Total 5,001 [solar Mar25] 2,761 [wind Mar25] 7,762 | 7,317 4,471 11,788 | 7,776 5,148 12,924"*
Footnotes: *"4 Advance Stage Capacity refers to projects which have received evacuation approvals as of June 30, 2025 or June 30, 2026; 5 Under Development Capacity refers to projects with evacuation approval applied for"* and *"STU – State Transmission Utility; CTU – Central Transmission Utility"* — twin PAGE 35.

Contracted portfolio these are set against (same slide, upper rows):
*"Operational Capacity2 total 2,178 [Mar25] / 3,644 [Mar26] / 4,174 [Jun26]; Contracted Capacity3 total 2,770 [Mar25] / 2,812 [Mar26] / 2,657 [Jun26]"* — twin PAGE 35. Total 13 GW portfolio = operational + contracted-under-development + advance-stage + under-development (footnote 1).

Corroborating single-line evacuation figure in the KPI table: *"Evacuation Capacity Available at end of Period(5) MW 5,972.67 [Jun-26] 4,259.89 [Jun-25] 6,016.61 [FY26] 3,411.36 [FY25] 1,567.40 [FY24]"* — Pres. twin PAGE 26.
Comment: the twin PAGE 26 "Evacuation Available" total (6,016.61 FY26) and the twin PAGE 35 "Evacuation Available" total (3,632 Mar26) differ because twin PAGE 35 splits Available (advance-stage, approvals received) from Applied (under-development, approvals applied-for), while twin PAGE 26 reports a single available figure on a different scope. Both anchored; definitional difference flagged.

### E2. Operational capacity by connectivity type (MW and % of run-rate EBITDA)

Operational connectivity split (Q1 FY27, MW share vs run-rate EBITDA share):
*"STU – Group Captive 48% 1,995 MW; STU – Third Party Open Access 13% 554 MW; CTU 13% 525 MW; Onsite Solar 10% 419 MWp; Capex (STU + Onsite) 16% 682 MW"* against *"Q1 FY27 4,174 MW"* — Investor_Presentation_1.txt twin PAGE 34 (printed slide 33).
*"our grid uptime has generally been quite good. So STUs is most of our capacity, is about 87% of our EBITDA is STU plus rooftop ... CTU is also is a problem area for us"* — Concall_Aug_2026, printed p.6-7 (twin PAGE 8).
*"Represents 13% (INR 239 Cr) of FY27 Run-Rate EBITDA"* (CTU), on the grid-uptime STU/CTU panel — Pres. twin PAGE 15 (printed slide 14).

| Connectivity type | Operational MW (Q1 FY27) | % of run-rate EBITDA | Anchor |
|---|---|---|---|
| STU (Group Captive + Third Party OA) | 2,549 MW (1,995 + 554) | part of the 87% STU+rooftop | Pres. twin PAGE 34; Aug p.6 |
| Onsite / rooftop (incl. Capex STU+Onsite) | 419 MWp + 682 MW capex | part of the 87% | Pres. twin PAGE 34 |
| STU + rooftop combined | — | ~87% | Concall_Aug_2026 printed p.6 (twin PAGE 8) |
| CTU | 525 MW | ~13% (≈ Rs 239 Cr of FY27 run-rate EBITDA) | Pres. twin PAGE 15 & 34; Aug p.6 |

Comment: the 87% (STU + rooftop) and 13% (CTU) EBITDA shares reconcile with the twin PAGE 34 MW shares (STU-GC 48% + STU-TPOA 13% + Onsite 10% + Capex 16% = 87%; CTU 13%). Management equates the MW share with the run-rate-EBITDA share. The Rs 239 Cr (twin PAGE 15) vs the Aug-call "about INR240 crores" (E4) are the same CTU run-rate EBITDA figure rounded.

### E3. Contracted-yet-to-execute pipeline by connectivity type

The 2,656.66 MW book IS split by connectivity (task's "if not split, NOT DISCLOSED" does not bind; it is disclosed):
*"Yet to be Executed — STU – Group Captive 38% 1,005 MW; STU – Third Party Open Access 1% 38 MW; CTU 51% 1,346 MW; Onsite Solar 5% 120 MWp; Capex (STU + Onsite) 6% 147 MW"* against *"Q1 FY27 2,657 MW"* — Investor_Presentation_1.txt twin PAGE 34 (printed slide 33).
Cross-check to the KPI total: *"Contracted yet to be executed Capacity(3) MW 2,656.66 [Jun-26]"* — Pres. twin PAGE 26.

| Connectivity type | Contracted-under-execution MW (Jun-26) | Share | Anchor |
|---|---|---|---|
| CTU | 1,346 MW | 51% | Pres. twin PAGE 34 |
| STU (Group Captive + Third Party OA) | 1,043 MW (1,005 + 38) | 39% | Pres. twin PAGE 34 |
| Onsite Solar | 120 MWp | 5% | Pres. twin PAGE 34 |
| Capex (STU + Onsite) | 147 MW | 6% | Pres. twin PAGE 34 |

Comment: CTU is the majority of the under-execution book (1,346 MW, 51%), the reverse of the operational book (CTU only 13%). The pipeline is CTU-weighted; the grid-curtailment exposure (E4) therefore rises as the book executes.

### E4. Bikaner — verbatim quotes

TGNA exchange (Mar call):
*"Kuldeep Jain: So the Bikaner 2 connectivity status update that we have from CTU and their estimate is that - the grid itself is connected, the substation is connected, but there are transmission bottleneck more north of the substation which are causing some backdown issues. They estimate that somewhere in the quarter between October to December 2026 is by when they expect to resolve the same, but this is a matter outside our sphere of control. ... So that is on the 525 MW in Bikaner 2. Puneet Gulati: And you have a TGNA there at this time. Kuldeep Jain: Yes, we would get a - that standard process would apply."* — Concall_Mar_2026, printed p.18 (twin PAGE 18).

No-pay-for-curtailed-power (May call):
*"Kuldeep Jain: Do the PPAs provide protection for that? As in no, not in the way that if the grid is curtailed, I'll still pay you ... Because obviously corporate customers do not have pay-for-performance contracts and if for whatever reason internal or external you are unable to generate the power, they are not liable to pay."* — Concall_May_2026, printed p.10-11 (twin PAGE 11-12).

30% figure (May call):
*"Kuldeep Jain: In that substation, the curtailment number is about 30% today, Puneet. There's a substation of Bikaner 2. Puneet Gulati: 30% of power produced? Kuldeep Jain: Yes, power injected, 30% of that is being curtailed in Bikaner 2. That is the, and it's not just our number, we know the number for the substation and everyone else in it."* — Concall_May_2026, printed p.16 (twin PAGE 17). Also restated: *"just around that cusp of that fiscal we've commissioned our plant in Bikaner, and I cannot give you specific to us but that substation has roughly 30% curtailment. Again, it's not a projection but it's a fact we know."* — May printed p.20 area (twin PAGE 21).

70% figure (Aug call):
*"We have a project commissioning in Bikaner at the end of last fiscal, start of this fiscal, where we have about 70% curtailment, and expect that curtailment to actually continue throughout the duration of the current financial year."* — Concall_Aug_2026, printed p.7 (twin PAGE 8).
*"you have mentioned that curtailment of 70% in June ... project where the curtailment problem is there accounts for about 13% of this run rate EBITDA ... And in that, we are currently facing a curtailment of about 70%."* — Aug printed p.13 (twin PAGE 15).

Rs 170 Cr / "8% or 9%" impact (Aug call):
*"if you assume the curtailment continues for the whole year ... INR1,870 crores into roughly 13% is your EBITDA from the project, which is about INR240 crores and if you take a 70% curtailment that's about INR170 crores on a full year basis."* — Concall_Aug_2026, printed p.13 (twin PAGE 15).
*"someone earlier today asked a question, 'Yes, our EBITDA would have been higher by maybe 8% or 9% if we did not have this curtailment,' but that's the extent of the impact."* — Aug printed p.7 (twin PAGE 8).
Comment: the "8% or 9%" impact sits on printed p.7 (twin PAGE 8), the Rs 170 Cr build-up on printed p.13 (twin PAGE 15); task cited both as "Aug p.12-13". Both anchored above; the two statements are consistent (Rs 170 Cr ≈ 8-9% of the ~Rs 1,870 Cr run-rate EBITDA base; note management applies the 8-9% loosely to the aggregate, while the Rs 170 Cr is 70% of the ~Rs 240 Cr CTU slice).

Grid-resolution dates given (evolving, each anchored):
- Mar-2026 call: *"somewhere in the quarter between October to December 2026"* — printed p.18 (twin PAGE 18).
- May-2026 call: *"The grid has forecasted the end of back down by September of this year but it's their number ... an externality beyond our control."* — printed p.16 (twin PAGE 17).
- Aug-2026 call: *"We don't know, honestly, and this number keeps changing, and therefore, we think we should all be prudent and assume that there is heavy curtailment for the rest of the financial year ... to be conservative, we should assume it continues for the rest of the fiscal."* — printed p.20 (twin PAGE 21-22).
Comment: the resolution estimate slipped from Oct-Dec 2026 (Mar call) to "September" (May call) to "no firm date; assume heavy curtailment the rest of FY27" (Aug call). Curtailment worsened from ~30% (May) to ~70% (Aug). Task cited the Aug resolution date at "p.22"; located at printed p.20 (twin PAGE 21-22).

### E5. Koppal — every mention

Capacity and connectivity type (CTU):
*"The second plant that we ... the CTU connected plant we are intending to commission in this fiscal is about 450 MW of wind coupled with, I think about 110 or 100 odd MWp of solar in Karnataka and there the grid expects ... a CTU connectivity is - I think we should think about it as December 2026 is our estimate."* — Concall_Mar_2026, printed p.18 (twin PAGE 18). (Karnataka CTU plant = Koppal; named explicitly in Aug and AR below.)
*"we are expanding our CTU-connected portfolio, including the 529 MW Koppal hybrid plant"* — AR MD&A, twin PAGE 355 (printed AR p.142).
*"543 of this 1.5 gigawatt will be contributed by the CTU project at Koppal, where two bays have been allocated and they commission by October '26 and March '27."* — Concall_Aug_2026, printed p.9 (twin PAGE 11).
Curtailment-exposure statement specific to Koppal: management flags CTU curtailment risk generally but says wind-profile South-India curtailment has been lighter: *"this is 450 MW of wind and about 80 MW of solar in a substation called Koppal ... in generating profile of wind hours in South India I think curtailment has been relatively [less] ... the curtailment issue is much more CTU"* — Concall_May_2026, printed p.14 area (twin PAGE 15). No Koppal-specific curtailment percentage is given (unlike Bikaner's 70%).

| Attribute | Value | Anchor |
|---|---|---|
| Connectivity type | CTU (Central Transmission Utility) | Mar p.18; AR twin PAGE 355; Aug p.9 |
| Location | Koppal substation, Karnataka | May p.14; AR twin PAGE 355 |
| Capacity | 529 MW (AR) / 543 MW (Aug call) / "450 MW wind + ~80-110 MWp solar" (Mar & May calls) | see discrepancy flag |
| Technology | Wind-solar hybrid | AR twin PAGE 355; Mar/May calls |
| Bay commissioning | Two bays; October '26 and March '27 | Concall_Aug_2026 printed p.9 (twin PAGE 11) |
| Curtailment % | **NOT DISCLOSED** (no Koppal-specific figure; management expects South-India wind curtailment lighter than Bikaner) | May p.14 |

**DISCREPANCY FLAG (Koppal capacity).** AR MD&A says 529 MW hybrid; Aug call says 543 MW; Mar/May calls describe ~450 MW wind + ~80-110 MWp solar (≈530-560 MW). Same project, three different totals across docs. Not reconciled in the corpus; flagged.

### E6. Other CTU-connected projects beyond Bikaner and Koppal

Operational CTU book = 525 MW, all Bikaner (Rajasthan): *"CTU 13% 525 MW"* operational, and *"Rajasthan (CTU)"* single site — Pres. twin PAGE 34; twin PAGE 7 note 1 *"Rajasthan CTU project caters to 3 different Environmental Attribute Purchase Agreements (EAPAs) with global technology companies"*. Only Bikaner is CTU-operational.
Contracted-under-execution CTU book = 1,346 MW (Pres. twin PAGE 34). Of this, Koppal accounts for ~543 MW (Aug p.9). The residual ~800 MW of contracted CTU capacity is **NOT DISCLOSED by project name** in the corpus. Management describes the future CTU cadence as *"one CTU site a year, so about 500 megawatt a year"* (Aug printed p.7, twin PAGE 8), implying further un-named CTU sites beyond Bikaner and Koppal, but no third project is named.
Comment: named CTU projects in the corpus = Bikaner (525 MW, operational, Rajasthan) and Koppal (~529-543 MW, under execution, Karnataka). Any additional CTU capacity inside the 1,346 MW under-execution CTU book is unnamed: **NOT DISCLOSED**. Docs checked: presentation twin PAGE 7/34/35/36, AR MD&A twin PAGE 355, all three concalls.

---

## BLOCK F — Debt, Hedging, Cash

### F1. Borrowings at 31-Mar-2026 (consolidated) and net-debt reconciliation

**AR-derived (Note 37.1 + Notes 21 / 26A):**

| Component (₹ million) | FY26 | ₹ Crore `[COMPUTED ÷10]` |
|---|---|---|
| Total Debt (Note 37.1) | 1,24,107.64 | 12,410.76 |
| — Non-current borrowings, net of current maturities (Note 21) | 1,13,124.22 | 11,312.42 |
| — Current borrowings incl. current maturities (Note 26A) | 10,983.42 | 1,098.34 |
| Less: Cash and cash equivalents | 12,019.60 | 1,201.96 |
| **Net Debt (Note 37.1)** | **1,12,088.04** | **11,208.80** |

(AR twin p.432 for totals; p.396/424 Note 21 non-current; p.426 Note 26A current.) Total Debt Rs 12,410.76 Cr matches the figure the prompt names.

**Secured / unsecured split.** Non-current (Note 21, incl. current maturities): secured term loans from banks 55,198.50 + from others 58,566.18 + vehicle loans 12.25 = 1,13,776.93 secured; NCD (Unsecured) 3,961.73 (AR twin p.423). Current (Note 26A): secured current maturities 4,614.44; **unsecured** NCD 5,787.10; WCDL from banks 477.62; interest accrued 104.26 (AR twin p.426). Total unsecured NCD across the book = 3,961.73 + 5,787.10 = **9,748.83 million (Rs 974.88 Cr)** `[COMPUTED]`; the balance is secured. Footnote 21(a)/26(A)(i): post the amended debenture trust deed dated 12-Jan-2026 the NCDs are *"not ... considered as secured debentures for the purposes of the Companies Act, 2013"* though charge is retained for IBC purposes (AR twin p.423/426).

**INR / foreign split.** Foreign-currency (USD) borrowing principal = **14,403.06 million (Rs 1,440.31 Cr)** per the unhedged FX table, *"Borrowings - USD 152.72 14,403.06"* (AR twin p.439, Note 37.4B). INR balance = 1,24,107.64 − 14,403.06 = **1,09,704.58 million (Rs 10,970.46 Cr)** `[COMPUTED]`. The AR does not print a single INR-vs-foreign borrowings table; the USD figure is taken from the FX-exposure note.

**Fixed / floating split (Note 37.4C, interest-rate risk, AR p.440):** *"Financial liabilities — Variable rate instruments 86,512.87 / 69,140.25 ... Fixed rate instruments 39,523.89 / 22,227.91"* (AR twin p.440). Floating = **Rs 8,651.29 Cr** `[COMPUTED ÷10]` (matches the prompt's Rs 8,651.29 Cr); fixed = **Rs 3,952.39 Cr** `[COMPUTED ÷10]`.

`Comment:` The variable + fixed instruments sum to 1,26,036.76 million, Rs 1,929.12 million above Total Debt (1,24,107.64). Flag: the interest-rate-risk table base is *"financial liabilities"* and is wider than the Note 37.1 borrowings base (it picks up items such as the redemption liability and OCD). I present both anchored; the AR does not reconcile the two bases.

**Management net-debt (Aug-2026 concall, Q1 FY27, twin p.9):** *"the net debt number is INR11,809 crores compared to the INR9,684 crores last quarter, which is 31st March 2026."* And on the asset-status split (twin p.9): *"out of the total INR11,800 crores net debt, approximately 44% of the debt is against the project which has been operational at the 12 months prior to the start of the year, which is INR5,154 crores. And ... 38% of the total debt, which is INR4,483 crores, is against the under-construction asset."*

| Net debt, management basis (₹ Crore) | Value |
|---|---|
| 31-Mar-2026 (FY26-end) | 9,684 |
| 30-Jun-2026 (Q1 FY27-end) | 11,809 |
| — 44% against ≥12-month-operational assets | 5,154 |
| — 38% against under-construction assets | 4,483 |

`Comment:` The 44% / 38% split is applied to the **30-Jun-2026** net debt of Rs 11,809 Cr (44% ≈ 5,196, 38% ≈ 4,487; management rounds to 5,154 and 4,483), not to the 31-Mar figure. The remaining ~18% sits against assets commissioned in the trailing 12 months (still stabilising) — the concall separates that EBITDA bucket (Rs 125 Cr of the Rs 494 Cr quarterly EBITDA) but does not give its debt rupee-figure.

**Reconciliation, AR-derived vs management (both at 31-Mar-2026):**
- AR Note 37.1 net debt = **Rs 11,208.80 Cr**.
- Management (Aug concall) net debt = **Rs 9,684 Cr**.
- **Gap = Rs 1,524.80 Cr** `[COMPUTED: 11,208.80 − 9,684]`.

`Comment — FLAG:` The two net-debt figures for the same date differ by Rs 1,524.80 Cr, and the corpus does **NOT DISCLOSED** a bridge. The AR net debt nets only *"Cash and cash equivalents"* (Rs 1,201.96 Cr) against Total Debt. Management's lower figure would net additional liquid balances the AR carries outside cash-and-equivalents — *"Bank balances other than cash and cash equivalents"* Rs 1,085.99 Cr (Note 37.2, AR twin p.432) and current investments / lien-marked mutual funds Rs 1,021.08 Cr (Note 37.2) — but those two alone (Rs 2,107.07 Cr) over-close the gap, so the management definition is not a clean "AR net debt less other bank balances". I do not resolve it; the precise management net-debt definition is NOT DISCLOSED. This gap should be a Halt-1 verification target.

### F2. Reverse factoring (Note 26(B))

*"Note 26(B) — Acceptances against capital and other creditors ... Measured at amortised cost — Acceptances against capital and other creditors 17,309.19 / 4,230.14"* (AR twin p.426). = **Rs 1,730.92 Cr** FY26 (matches prompt), FY25 comparative **Rs 423.01 Cr** `[COMPUTED ÷10]`.

Footnote 26(B)(ii) *"Supplier finance arrangements"*: *"The Group has entered into supplier finance arrangements with certain banks and financial institutions ('the finance providers') to facilitate the early payment of dues on its behalf to the Group's vendors who may elect to factor their invoice from the Group. ... By virtue of commercial agreement with the finance providers, the Group gets additional credit period of 60-180 days to settle the payment with the finance providers ... The Group has derecognised the original trade payables and disclosed the related supplier financial liabilities towards the finance providers separately on the face of the Balance Sheet as 'Acceptances against capital and other creditors'."* (AR twin p.426).

**Cash-flow classification (accounting-policy statement, AR p.427):** *"The payments to the bank are included within investing cash flows because these payable pertains to capital goods and continue to be part of the normal operating cycle of the Group and its joint ventures. The payments to supplier by the bank of I17,309.19 Million are considered non-cash transactions."* Disclosure table (AR twin p.427): *"Presented as Acceptances against capital and other creditors 17,309.19 ; Of which suppliers have received payment from the finance provider 17,309.19 ; Range of payment due dates ... Liabilities that are part of the arrangement 60 to 270 days ; Comparable trade payables that are not part of an arrangement 60 to 270 days. There were no significant non-cash changes ..."* (AR twin p.426-427).

`Comment:` The full Rs 1,730.92 Cr (up 4.1x from Rs 423.01 Cr) is a supplier-finance / reverse-factoring liability that has been reclassified off trade payables onto its own balance-sheet line. Two features to weigh at Halt 1: (i) the entire balance is treated as a **non-cash** item and the related bank settlements are routed through **investing** (not operating) cash flow, on the argument the underlying payables are for capital goods — this keeps them out of operating working-capital movements; (ii) the arrangement's due-date range (60-270 days) equals that of non-participating payables, so the AR argues terms are not materially extended. The classification choice materially affects reported operating cash flow (F5) and is a candidate reconciling item behind the F1 net-debt gap.

### F3. Hedging (Note 37.4)

**Interest-rate swaps (Note 37.4C, AR p.440):** *"The Group and its joint ventures uses interest rate swaps to hedge the variability in interest cash flows attributable to movements in interest rates arising from foreign currency borrowings. The Group applies a hedge ratio of 1:1."* Exposure table: *"Variable rate instruments 86,512.87 ; Effect of interest rate swaps (10,267.80) ; 76,245.07 ... Fixed rate instruments 39,523.89 ; Effect of interest rate swaps 10,267.80 ; 49,791.69"* (AR twin p.440).

**Forward cover (Note 37.4A, AR p.438):** *"Forward cover to purchase: - USD 5.34 [foreign M] 501.10 [notional ₹ M] ; Forward cover for foreign currency borrowings: - USD 7.08 667.74"* (AR twin p.438).

**USD borrowing principal / net exposure (Note 37.4B unhedged table, AR p.439):** *"Borrowings - USD 152.72 14,403.06 ; Net balance sheet exposure - USD (151.76) (14,313.68)"* (AR twin p.439).

| Metric | ₹ million | ₹ Crore `[COMPUTED ÷10]` |
|---|---|---|
| Interest-rate-swap notional | 10,267.80 | 1,026.78 |
| Variable-rate (floating) debt | 86,512.87 | 8,651.29 |
| USD-denominated borrowing principal | 14,403.06 | 1,440.31 |
| Forward cover for FC borrowings (USD) | 667.74 | 66.77 |
| Forward cover to purchase (USD) | 501.10 | 50.11 |

**Hedge ratios `[COMPUTED]`:**
- Accounting hedge ratio (stated designation) = **1:1** (per note).
- IRS notional / floating debt = 10,267.80 / 86,512.87 = **11.9%** of variable-rate debt carries an interest-rate swap.
- FX forward cover for borrowings / USD borrowing principal = 667.74 / 14,403.06 = **4.6%** of the USD principal is forward-covered.
- Unhedged USD net balance-sheet exposure = Rs 1,431.37 Cr (14,313.68 million), i.e. essentially the whole USD borrowing sits FX-open.

`Comment:` The 1:1 "hedge ratio" in the note is the Ind AS 109 designation (notional of swap matched to hedged item), not economic coverage. Economically the hedge book is thin: only ~11.9% of floating-rate debt is interest-rate-swapped and only ~4.6% of the Rs 1,440.31 Cr USD principal is forward-covered, leaving ~Rs 1,431 Cr of USD borrowings exposed to rupee depreciation. CARE separately flags a ~Rs 1,200 Cr FCNR(B) 20-year loan due for renewal Sep-2028 (F7). This currency-and-rate openness is a live risk item for Halt 1.

### F4. Deferred tax asset (Notes 24, 48/49)

**Note 24 (AR p.425) — DTA carried on the balance sheet.** The consolidation nets to a **Deferred Tax Asset (net) of 5,455.30 / 2,545.34** (FY26 / FY25) for the net-DTA entities (AR twin p.425), with the DTA driver *"Unabsorbed depreciation and business losses 7,875.06 / 4,691.46"* (net-DTA entity block) and, in the net-DTL entity block, *"Unabsorbed depreciation and business losses 4,282.65 / 4,528.80"* (AR twin p.425).

**Aggregate DTA on tax losses (Note 48/49 area, AR p.464):** *"Deferred tax asset of I12,157.71 Million (31st March, 2025: I9,220.26 Million) has been recognised by the Group and its joint ventures on unabsorbed depreciation and unused business tax losses."* (AR twin p.464). = **Rs 1,215.77 Cr FY26 vs Rs 922.03 Cr FY25** `[COMPUTED ÷10]` (this equals 7,875.06 + 4,282.65 = 12,157.71).

**Recognition-basis language (verbatim, AR p.464):** *"The recoverability of the deferred tax assets has been assessed based on: − Internal budgets, profit forecasts prepared by management, − applying tax principles to those forecasts; and − following the methodology required by Ind AS 12 – Income Taxes. Based on the assessments as above, the management determines that deferred tax assets created on unused tax losses (business losses and unabsorbed depreciation) should reverse well within the statutory time limit. These losses can be fully set-off against future taxable profits earned by the respective Companies/LLPs ... and accordingly based on the reasonable certainty that sufficient future taxable income would be generated considering the size of the Company/LLPs, its growth trajectory and past performance history during normal times, appropriate amount of deferred tax asset has been created during the year."* (AR twin p.464).

**Unrecognised DTA (AR p.464):** *"Deferred tax asset amounting to I147.73 Million (31st March, 2025: I36.17 Million) in respect of unused tax losses have not been recognised by the Group. The total tax loss carry forwards of I586.91 Million (31st March, 2025: I143.70 Million), relates to certain subsidiaries on which deferred tax asset has not been recognised ... because there is a lack of reasonable certainty that these subsidiaries may generate future taxable profits."* (AR twin p.464).

| Item | FY25 | FY26 | ₹ Crore FY26 `[COMPUTED ÷10]` |
|---|---|---|---|
| Recognised DTA on unabsorbed depreciation + business losses (₹ mn) | 9,220.26 | 12,157.71 | 1,215.77 |
| Unrecognised DTA on unused losses (₹ mn) | 36.17 | 147.73 | 14.77 |
| Gross tax-loss carry-forwards not recognised (₹ mn) | 143.70 | 586.91 | 58.69 |

`Comment:` The recognised DTA on tax losses rose from Rs 922.03 Cr to Rs 1,215.77 Cr, a Rs 293.74 Cr build in one year, recognised on a *"reasonable certainty"* basis anchored to management forecasts, group size and growth trajectory — a forward-looking judgement, not a booked recovery. **Unabsorbed depreciation carried forward as a standalone gross figure is NOT DISCLOSED**: the note combines *"unabsorbed depreciation and business losses"* and reports the DTA on them, not the gross depreciation-only carry-forward. The unrecognised piece is small (Rs 14.77 Cr DTA on Rs 58.69 Cr of losses). Docs checked: AR Note 24, AR Note 48/49 deferred-tax disclosure.

### F5. Consolidated cash flow statement — FY24 (RHP restated), FY25, FY26

FY25 and FY26 are from the AR Consolidated Statement of Cash Flows (twin p.379). FY24 is from the RHP Summary of Restated Consolidated Statement of Cash Flows (twin p.107-112). All ₹ million.

| Line (₹ million) | FY24 (RHP restated) | FY25 | FY26 |
|---|---|---|---|
| Cash generated from operations | 1,862.41 | 14,861.44 | 18,065.39 |
| Income taxes paid (net) | (999.65) | (819.48) | (753.02) |
| **Net cash from operating activities (A)** | **862.76** | **14,041.96** | **17,312.37** |
| Capex — PPE + CWIP (+ intangibles + capital advances) | (18,661.34) | (29,106.17) | (57,543.18)¹ |
| Net cash used in investing (B) | (19,386.03) | (36,170.50) | (59,574.67) |
| **Net cash from financing (C)** | **17,887.78** | **24,812.43** | **50,953.98** |
| Net increase/(decrease) in cash (A+B+C) | (635.49) | 2,683.89 | 8,691.68 |

¹ FY26 capex = PPE/CWIP/capital advances (56,871.87) + other intangibles (671.31) = 57,543.18 (AR twin p.379). FY24/FY25 RHP presents PPE/CWIP/intangibles/capital advances as a single line.

**Free cash flow `[COMPUTED = CFO − capex]` (₹ million / ₹ Crore):**
- FY24: 862.76 − 18,661.34 = **(17,798.58) mn = Rs (1,779.86) Cr**.
- FY25: 14,041.96 − 29,106.17 = **(15,064.21) mn = Rs (1,506.42) Cr**.
- FY26: 17,312.37 − 57,543.18 = **(40,230.81) mn = Rs (4,023.08) Cr**.

Sources: AR twin p.379 (FY26/FY25); RHP twin p.107 (op), p.111 (invest/finance), p.112 (net change), FY24 column.

**Capitalised interest — sits in INVESTING, not operating.** Note 36(b): *"Interest expenses of I1,685.78 Million (31st March, 2025: I334.17 Million) being directly attributable to construction of capital work-in-progress have been capitalised and above interest expense is presented net of such capitalisation."* Note 36(c): LC/BG charges of *"I1,267.55 Million (31st March, 2025: I204.45 Million)"* likewise capitalised to CWIP; Note 36(e): lease-liability interest of *"I169.33 Million"* capitalised to CWIP (AR twin p.431).

`Comment:` Capitalised borrowing cost (Rs 168.58 Cr interest + Rs 126.76 Cr LC/BG + Rs 16.93 Cr lease interest in FY26) is embedded inside the **investing** capex line as part of CWIP additions; the P&L finance cost and the operating-section add-back are shown **net** of that capitalisation, and cash finance-costs-paid of Rs 850.77 Cr (8,507.67 mn) sit in **financing**. FCF is deeply negative and worsening in absolute terms across all three years, driven by a capex ramp (Rs 5,754.32 Cr FY26 vs Rs 1,866.13 Cr FY24), funded by the Rs 5,095.40 Cr FY26 financing inflow. Operating cash flow itself turned strongly positive (Rs 1,731.24 Cr FY26 vs Rs 86.28 Cr FY24) — but note the F2 reverse-factoring reclassification lifts operating cash by keeping capital-goods supplier settlements in investing/non-cash. This is a build-phase cash profile: growth is entirely debt-and-equity funded, not self-funded.

### F6. NCD prepayment (Note 45)

*"Note 45: Events occurring after reporting date. i. Subsequent to 31st March, 2026, the Parent Company prepaid its 11.50% Listed, Rated, Redeemable, Non-Convertible Debentures and 11.50% Unlisted, Rated, Redeemable, Non-Convertible Debentures, which were originally due on 08th June, 2027. On 2nd April, 2026, the outstanding principal amount aggregating to I5,990 Million was prepaid in full out of the IPO proceeds. ... Pursuant to Ind AS 10 ... these debentures have been classified under current borrowings in the Consolidated Financial Statements as at 31st March, 2026."* (AR twin p.450).

- Principal prepaid = 5,990 million = **Rs 599 Cr** `[COMPUTED ÷10]` (matches prompt) at **11.50%**, prepaid **2-Apr-2026** from IPO proceeds, originally due 08-Jun-2027.
- **Annual interest saving `[COMPUTED]` = Rs 599 Cr × 11.50% = Rs 68.89 Cr per year** (688.85 million).

`Comment:` The Rs 599 Cr 11.50% NCD block was already reclassified into current borrowings at FY26-end (the underlying prepayment condition existed at the reporting date), so it sits inside the Rs 12,410.76 Cr Total Debt (F1) at 31-Mar-2026 but is retired two days later out of IPO cash. The Rs 68.89 Cr annual interest saving is a clean forward reduction in finance cost. Cross-reference: standalone Note 45 carries the identical event (AR twin p.813); the two 11.50% NCD lines also appear in the borrowings schedule as Loan 21 (Listed, 49,990-face) and Loan 22 (Unlisted).

### F7. CARE definitions (both PRs)

**CARE PR dated 12-Oct-2025** (`...202510121005...txt`), Brief Financials – CMEESL Consolidated, ₹ crore (twin p.5-6):

*"Total operating income 1,390 / 1,496 ; PBILDT 706 / 900 ; PAT 5 / 52 ; Overall gearing (times) 2.5 / 2.5 ; Interest coverage (times) 1.4 / 1.4"* (FY24(A) / FY25(A)).

Leverage: *"CMEESL's capital structure is leveraged ... reflected by Net Debt/(1-year forward EBITDA) ratio of 4.8x as on FY25 end. ... net debt/(1-year EBITDA) for the company is expected to be ~4.9x – 5.5x over FY26 and FY27."* (twin p.6). Downgrade trigger: *"Slower than expected deleveraging ... resulting in net debt/1 year forward EBITDA breaching 6.0x on a sustained"* basis (twin p.2).

**CARE PR dated 12-May-2026** (`...202605120525...txt`), Brief Financials – CMEESL Consolidated, ₹ crore (twin p.4):

*"Total operating income 1,390 / 1,496 / 1,913 ; PBILDT* 706 / 900 / 1,132 ; Profit after tax (PAT) -38 / 19 / 86 ; Overall gearing (x) 2.5 / 2.5 / 2.3 ; Interest coverage (x) 1.4 / 1.4 / 1.4"* (FY24(A) / FY25(A) / FY26(A)), with *"*PBILDT: Profit before interest, lease rentals, depreciation and tax"* (twin p.4).

Leverage forward statement: *"opening net debt/ earnings before interest, taxation, depreciation, and amortisation (EBITDA) for the company is expected to be ~5.0x – 5.3x for FY27 and FY28"* (twin p.4); and *"reflected by Opening Net Debt/ EBITDA ratio of 5.7x as on FY26-end. ... opening net debt/ EBITDA for the company is expected to be ~5.0x – 5.3x FY27 and FY28."* (twin p.9). Downgrade trigger: *"Slower-than-expected deleveraging ... resulting in opening net debt/ EBITDA breaching 5.5x on a sustained basis."* (twin p.3).

| CARE metric (₹ crore) | FY24(A) | FY25(A) | FY26(A) |
|---|---|---|---|
| PBILDT | 706 | 900 | 1,132 |
| Overall gearing (x) | 2.5 | 2.5 | 2.3 |
| Interest coverage (x) | 1.4 | 1.4 | 1.4 |
| PAT — Oct-2025 PR | 5 | 52 | — |
| PAT — May-2026 PR | (38) | 19 | 86 |

**CARE leverage ratio, forward:**
- Oct-2025 PR: Net Debt/(1-yr forward EBITDA) 4.8x at FY25-end; expected ~4.9x-5.5x FY26-FY27; sensitivity trigger 6.0x.
- May-2026 PR: Opening Net Debt/EBITDA 5.7x at FY26-end; expected **~5.0x-5.3x FY27 and FY28**; sensitivity trigger 5.5x.

**CARE definition of net debt: NOT DISCLOSED as a rupee formula.** Both PRs express leverage only as a ratio (*"Net Debt/(1-year forward EBITDA)"* / *"Opening Net Debt/ EBITDA"*) and define PBILDT (*"Profit before interest, lease rentals, depreciation and tax"*) but give no rupee build-up of the net-debt numerator or its component definition. The word *"Opening"* signals net debt measured at the start of the forward year against that year's EBITDA. Docs checked: both CARE PR twins in full.

`Comment — FLAG (discrepancy, standing rule 5):` The two CARE PRs disagree on PAT for the same audited years. Oct-2025 PR: FY24 PAT **+5**, FY25 PAT **+52**. May-2026 PR: FY24 PAT **(38)**, FY25 PAT **+19**. Both are marked "(A) Audited". TOI, PBILDT, gearing and interest coverage are identical across the two PRs; only PAT was restated downward between October and May (FY24 by Rs 43 Cr, FY25 by Rs 33 Cr). This aligns directionally with the RHP restated owners'-PAT being negative in earlier years (D1 / RHP twin p.105: restated profit attributable to owners FY24 (309.88) mn). Present both anchored; do not reconcile. Separately, CARE's forward leverage guide tightened between the two PRs (trigger cut from 6.0x to 5.5x; the forward band re-based to 5.0x-5.3x on FY27-FY28 opening net debt/EBITDA), while the FY26-end starting point (5.7x) is above both the prior 4.8x FY25-end reading and the forward target — the deleveraging is a plan, not yet an achieved trajectory.

---

END Blocks D and F. Block V not written (per instruction).

---

## BLOCK G — PROMOTER, PLEDGE, SHAREHOLDING

### G1. Pledge chronology

**AR Note 19(g), FY26 and FY25 positions.**

*"19 (g) Details of equity shares of the Parent Company pledged: ... 1 Kuldeep
Jain [pledged] As at 31st March, 2026: 2,76,898 | As at 31st March, 2025:
1,21,728 ... 2 KEMPINC LLP: 1,13,20,968 | 83,676"* (AR twin p.420)

*"As at 31st March, 2026, Kuldeep Jain and KEMPINC LLP ("Pledger") have pledged
in aggregate, 11,597,866 Equity Shares ("Pledged Shares") held by them in
favour of 360 One Prime Limited, in accordance with the terms of the pledge
agreement dated July 22, 2025 entered into by the Pledgers with 360 One Prime
Limited, in relation to certain borrowings availed by KEMPINC LLP."* (AR twin
p.420)

*"As at 31st March, 2025, Kuldeep Jain and KEMPINC LLP have pledged in
aggregate, 205,404 Equity Shares against the issue of non-convertible
debentures."* (AR twin p.420)

Comment: Note 19(g) line items (2,76,898 + 1,13,20,968 = 1,15,97,866) reconcile
to the aggregate 11,597,866 stated. [COMPUTED] Pledgee changed between years:
FY25 pledge was against NCDs; FY26 pledge is to 360 One Prime Limited under the
July 22, 2025 agreement.

**RHP pledge schedule (twin p.54-55, printed p.50-51).**

*"Out of a total of 25,855,617 Equity Shares held by Kuldeep Jain, Nidhi Jain
and KEMPINC LLP, 10,731,094 Equity Shares ("Pledged Shares") (amounting to
10.09% of the pre-Offer share capital of our Company on a fully diluted basis)
are pledged in favour of 360 One Prime Limited pursuant to an unattested deed of
pledge dated July 22, 2025 ... The pledge was created in relation to a loan
amounting up to ₹ 6,700.00 million availed by KEMPINC LLP from 360 One Prime
Limited, pursuant to the master facility agreement dated July 22, 2025 ... read
with sanction letter dated July 22, 2025 ..."* (RHP twin p.54)

Stated purpose: *"The loan has been availed towards purchase of Equity Shares by
KEMPINC LLP through secondary transactions, permissible investments and general
purposes."* (RHP twin p.54). The pledge-schedule "Purpose" column reads:
*"Acquisition of Equity Shares of our Company, other permissible investment and
general corporate purposes."* (RHP twin p.54-55).

Facility amount: **Rs 6,700.00 million (Rs 670.00 Cr)** [COMPUTED /10]; lender
**360 One Prime Limited**; security cover **2.25x** with a 7-business-day
margin-call/top-up (RHP twin p.55).

Pledgor-wise (RHP twin p.54-55): Kuldeep Jain — 2,384,118 pledged (2.24% pre-
Offer); Nidhi Jain — 198,916 (0.19%); KEMPINC LLP — 8,148,060 (7.66%); **Total
10,731,094 (10.09%)**.

Release statement: *"As on date of the Red Herring Prospectus, all the Pledged
Shares had been released."* (RHP twin p.54)

Re-pledge statement: *"Except for the Offered Shares of the Promoter Selling
Shareholders which will be transferred and allotted to Allottees in the Offer
for Sale, all or a portion of the remaining Pledged Shares will be re-pledged
post creation of statutory lock-in in accordance with Regulation 16(1)(b) of the
SEBI ICDR Regulations."* (RHP twin p.54)

Comment: AR (as at 31-Mar-2026) shows 11,597,866 pledged to 360 One; the RHP (as
at Feb 2026, pre-Offer) shows 10,731,094 pledged then released before the RHP.
Different snapshot dates. **Discrepancy flag:** the two pledged-share counts
differ (11,597,866 vs 10,731,094) because the AR is a later, post-listing date;
present both anchored.

**Promoter-group total behind 20.02%.** The AR shareholding-pattern table gives:
*"Promoter and Promoter Group 5,79,30,860 [shares] 49.48 [% of total equity]"*
(AR twin p.351). [COMPUTED] 11,597,866 / 5,79,30,860 = 0.2002 = **20.02%** of the
promoter-group holding is pledged. Promoter-group share total used = **5,79,30,860
(49.48% of equity)**.

### G2. Personal guarantee of Kuldeep Jain (Note 54, sampled)

Note 54 (AR twin p.487-503) names an unconditional personal guarantee of Mr.
Kuldeep Jain as security at **six** facility entries (verbatim "Personal
guarantee of Mr. Kuldeep Jain" / "personal Guarantee of Mr. Kuldeep Jain"). A
seventh-through-N set of Note-54 rows explicitly records *"Personal Guarantee:
Nil"* (AR twin p.503, p.510, p.523, p.545 area). Facilities carrying the
personal guarantee:

| # (Note 54 Sr.) | Borrower SPV | Lender named? | Amount as at 31-Mar-2026 (Rs mn) | Rs Cr [COMPUTED /10] | Parent-equity pledge in the SPV | Anchor |
|---|---|---|---|---|---|---|
| 6 | Clean Max IPP 1 Private Limited | No (rate "linked to Lender's MCLR + 0.50%") | 194.16 | 19.42 | 30% pledged + 21% irrevocable non-disposal undertaking | AR twin p.489 |
| 7 | Clean Max IPP 1 Private Limited | No ("Lender's MCLR + 0.50%") | 333.52 | 33.35 | 30% + 21% NDU | AR twin p.489 |
| 8 | Clean Max IPP 1 Private Limited | No ("Lender's 1Y MCLR + 0.45%") | 661.21 | 66.12 | 30% + 21% NDU | AR twin p.490 |
| 9 | Clean Max IPP 1 Private Limited | No ("Lender's 1Y MCLR + 0.45%") | 70.10 | 7.01 | 30% + 21% NDU | AR twin p.490 |
| 16 | Clean Max Aditya Power Private Limited | No ("Lender's 6M-MCLR + 1.40%") | 426.54 | 42.65 | 51% (collateral pledge of 51% of Borrower held by Sponsor/Promoter) | AR twin p.497 |
| 17 | Clean Max Aditya Power Private Limited | No ("Lender's 6M-MCLR + 1.40%") | 241.42 | 24.14 | 51% (collateral pledge of 51% of Borrower) | AR twin p.497-498 |

Verbatim, entries 6-9: *"(6) Pledge of 30% of Clean Max Enviro Energy Solutions
Limited ... (parent company) stake in the borrowing entity on pari passu basis
and irrevocable non disposal undertaking for another 21% of the stake held by
the parent company ... (7) Personal guarantee of Mr. Kuldeep Jain. (8) Corporate
Guarantee of Clean Max Enviro Energy Solutions Limited ..."* (AR twin p.489-490).

Verbatim, entries 16-17: *"(ii) Collateral Security Pledge of 51% shares in the
shareholding of the Borrower held by the Sponsor/Promoter; and (iii) Guarantees
(a) Unconditional and irrevocable personal Guarantee of Mr. Kuldeep Jain. (b)
Unconditional and irrevocable corporate guarantee of the Sponsor/Promoter i.e.,
Clean Max Enviro Energy Solutions ..."* (AR twin p.497-498).

Comment: entries 6-9 (Clean Max IPP 1) carry the 30%+21% structure (51%
effective); entries 16-17 (Clean Max Aditya Power) carry a direct 51% pledge.
No lender is named against these rows in Note 54; only the interest-rate
benchmark. [COMPUTED] Sum of the six sampled facility balances = 194.16 + 333.52
+ 661.21 + 70.10 + 426.54 + 241.42 = 1,926.95 Rs mn = 192.70 Rs Cr as at
31-Mar-2026 (this is a book-balance sum of the sampled rows, not a guarantee
cap).

**Aggregate promoter personal-guarantee disclosure:** searched AR Note 54 (twin
p.487-503) and the full RHP. No aggregate rupee figure for promoter personal
guarantees is stated in either document. Nearest RHP mentions: one facility
carries *"Unconditional and Irrevocable Personal Guarantee of Mr. Kuldeep Jain"*
(RHP twin p.821), and two "Deed of personal guarantee dated July 22, 2025"
entries relate to the 360 One pledge, not to a corporate borrowing guarantee
(RHP twin p.972). No summed total. Aggregate promoter personal guarantee:
**NOT DISCLOSED**.

### G3. Rikhab Investments B.V.

**Shareholding.** *"6 Rikhab Investments B.V. 97,95,900 8.37% ..."* (AR Note
19(e), twin p.420); classified under *"Promoter Group ... Rikhab Investments
B.V"* (AR related-party note, twin p.454). RHP: *"Rikhab Investments B.V.
9,795,900 [shares] 9.21 [% pre-Offer, fully diluted] 9,795,900 8.32 [% post-
Offer]"* (RHP twin p.150); *"The Promoter Group shareholder is Rikhab
Investments B.V."* (RHP twin p.28).

**Date of entry (secondary transfers).** RHP history-of-shareholding table (twin
p.215):
- Aug 6, 2025: 1,379,391 shares transferred from Augment India I Holdings, LLC
  at Rs 1,225.00/share (Rs 1,689.75 mn).
- Aug 13, 2025: 528,938 shares from DSDG Holding APS at Rs 612.50 (Rs 323.97 mn).
- Aug 13, 2025: 6,508,180 shares from BGTF One Holdings (DIFC) Limited at Rs
  612.50 (Rs 3,986.26 mn).

Comment: [COMPUTED] the three transfers sum to 8,416,509 shares, below the
9,795,900 held; the RHP transfer register lists additional lines for Rikhab
that are not fully reproduced here (retrieval sampled the capital-structure
table). Present the anchored transfer rows; do not force a reconciliation.

**Role in the July / November 2025 shareholders' agreements.** *"Amended and
restated shareholders' agreement dated July 30, 2025 entered into amongst our
Company, Kuldeep Jain, Pratap Jain, Nidhi Jain and KEMPINC LLP ("Promoter
Block"), BGTF One Holdings (DIFC) Limited ("Investor 1"), Augment India I
Holdings, LLC ("Investor 2"), DSDG HOLDING APS ("Investor 3"), and Rikhab
Investments B.V. ("Rikhab") as amended by the amended and restated shareholders'
agreement dated November 4, 2025 ..."* (RHP twin p.374). *"The SHA also provides
certain inspection and information rights to the relevant parties, including the
Promoter Block, Rikhab and the Investors."* (RHP twin p.374). Board-nomination
rights under the SHA sit with the Promoter Block (two directors) and Investor 1
(two directors); Rikhab is not named among the nominating parties (RHP twin
p.374). Rikhab is also party to a non-disposal undertaking dated July 30, 2025
with Catalyst Trusteeship Limited, tied to borrowings from BGTF Loans Aggregator
LP (RHP twin p.141).

**Beneficial owner / control statement.** The RHP shareholding table's ultimate-
beneficial-owner footnote ("**") attaches to KEMPINC LLP (*"Kuldeep Jain is the
ultimate beneficial owner"*, RHP twin p.150), **not** to Rikhab. Rikhab's own
beneficial owner is not stated. Dheer Jain (named in the promoter family tree as
a son of Kuldeep Jain and Nidhi Jain, RHP twin p.551) is a party to
Rikhab's facility agreement dated July 30, 2025 with BGTF Loans Aggregator LP
(RHP twin p.141). No express beneficial-ownership or control statement for
Rikhab. Rikhab beneficial owner: **NOT DISCLOSED**.

### G4. Brookfield / BGTF holding series

| Snapshot | Shares | % | Anchor |
|---|---|---|---|
| 31-Mar-2025 | 25,31,780 | 49.92% | AR Note 19(e), twin p.420 |
| Pre-Offer (RHP, Feb 2026) | 33,417,101 | 31.42% (fully diluted) | RHP twin p.150 |
| OFS shares sold in the IPO | 8,510,959 | Rs 8,962.04 mn (Rs 896.20 Cr) at Rs 1,053 | RHP cover, twin p.3 |
| Post-Offer (RHP) | 24,906,142 | 21.15% | RHP twin p.150 |
| 31-Mar-2026 | 2,49,45,365 | 21.31% | AR Note 19(e), twin p.420 |

*"... 8,510,959 Equity Shares of face value of ₹ 1 each aggregating to ₹
8,962.04 million by BGTF One Holdings (DIFC) Limited ..."* (RHP cover, twin p.3).

Control change: *"Ultimate Parent Company: Brookfield Corporation (upto 14th
August, 2025)"*; *"Entity having immediate control over [Company]: BGTF One
Holding (DIFC) Limited (upto 14th August, 2025)"*; from 15th August 2025 both
Brookfield Corporation and BGTF One become entities *"having significant
influence over"* the Company (AR twin p.454). *"With effect from 14th August,
2025, BGTF One Holdings (DIFC) Limited ceases to be Holding company."* (AR twin
p.419).

**Discrepancy flag:** RHP post-Offer BGTF One = 24,906,142 (21.15%); AR
31-Mar-2026 = 2,49,45,365 (21.31%). Difference 39,223 shares. Different snapshot
dates (RHP Feb 2026 vs AR 31-Mar-2026); both anchored above.

**Lock-in expiry date for BGTF residual.** No calendar expiry date is given in
the RHP. Lock-in is stated as periods (RHP twin p.148-149): *"the 20% of the
post-Offer shareholding of our Company held by our Promoters and locked in for 3
years ... and the remaining post-Offer shareholding by our Promoters ... which
is locked in for one year, in terms of Regulation 16(1)(b) ... the entire pre-
Offer equity share capital ... will be locked-in for a period of six months from
the date of Allotment ..."*. A specific lock-in expiry date for BGTF's residual
holding: **NOT DISCLOSED** (RHP states periods from Allotment, no dates).

### G5. Green Earth litigation (RHP twin p.875, printed 871; and twin p.883, printed 879)

Full disclosure (RHP twin p.875, printed 871):

*"M/s. Green Earth ("Green Earth") had executed (i) memorandum of understanding
dated September 19, 2018, with our Company; (ii) memorandum of understanding
dated October 10, 2018, with Strawberry Sunrays Energy Private Limited; and (iii)
memorandum of understanding dated October 4, 2018, with Sun Q Private Limited
(collectively, the "MoUs"), in relation to proposed acquisition of project land
in Sirsa. Subsequently, the MoUs were terminated due to commercial reasons."*

- Complaint date / court / IPC sections / respondents: *"Green Earth filed a
  criminal complaint dated August 5, 2020 ("Complaint") before the Court of Duty
  Magistrate, Sirsa ("Trial Court") against our Company, one of our Promoters,
  Kuldeep Jain, and certain other representatives and clients of our Company
  ("Respondents") under Sections 406, 420, 467, 468, 471, 120B and 506 of the
  Indian Penal Code, 1860. In the Complaint, Green Earth alleged that the
  commission amounts due and payable to it as per the terms of the memorandum of
  understanding dated October 10, 2018, have not been paid."* Summons issued by
  the JMFC, Sirsa, per order dated October 1, 2020.
- Quashing petition status: *"Our Company filed a petition dated February 9, 2021
  ("Quashing Petition") under Section 482 of the Criminal Procedure Code, 1973
  before the Punjab and Haryana High Court, for quashing of (i) the Complaint;
  and (ii) the summons ..."*
- HC stay date: *"Pursuant to its order dated February 12, 2021, the Punjab and
  Haryana High Court has ordered a stay on proceedings before the Trial Court
  pending determination of the Quashing Petition."*
- Mediation referral date: *"the matter has been referred to the 'Mediation and
  Conciliation Centre' of the Punjab and Haryana High Court vide the order dated
  January 12, 2026."*
- Second complaint / revision: *"Green Earth also filed another criminal
  complaint against the Respondents, before the JMFC. The JMFC declined to order
  a police investigation in the matter vide its order dated March 4, 2022
  ("Order"). Green Earth filed a revision petition dated March 12, 2022 before
  the District and Sessions Court, Sirsa, against the Order. The matters are
  currently pending."*

Promoter-section cross-reference (RHP twin p.883, printed 879), under *"Kuldeep
Jain — Criminal proceedings"*: same Complaint restated, *"The matter is currently
pending. For details, see '– Litigation involving our Company' on page 871."*

### G6. Temasek / Bain entries (AR twin p.343; RHP)

**Jongsong preferential allotment (Pre-IPO placement).** AR: *"28,19,548 equity
shares of face value of INR 1 each were allotted on 06 February 2026 to Jongsong
Investments Pte. Ltd. The shares were issued at a price of INR 1,053 per share,
including a premium of INR 1,052 per share, aggregating to a total consideration
of INR 2,96,89,84,044."* (AR twin p.343). RHP cover restates: 2,819,548 Equity
Shares at Rs 1,053 (premium Rs 1,052), aggregating **Rs 2,968.98 million (Rs
296.90 Cr)** (RHP twin p.3). Shares 28,19,548 = 2,819,548; both docs agree.

**Jongsong secondary purchase from BGTF One Holdings.** RHP history table (twin
p.215): *"February 6, 2026 | Jongsong Investments Pte. Ltd. | BGTF One Holdings
(DIFC) Limited | 4,397,926 | 1.00 | 1,053.00 | Cash | 4,631.02"* = **4,397,926
shares at Rs 1,053, Rs 4,631.02 million (Rs 463.10 Cr)**.

Comment: [COMPUTED] 2,819,548 (primary) + 4,397,926 (secondary) = 7,217,474 =
Jongsong's total holding shown at RHP twin p.26 and AR Note 19(e) twin p.420.

**Temasek identification.** *"Jongsong Investments Pte. Ltd. (an indirect wholly
owned subsidiary of Temasek Holdings Private Limited)"* (RHP twin p.372; also
twin p.27: *"An indirect wholly owned subsidiary of Temasek Holdings Private
Limited."*).

**Bain secondary (in filed document).** RHP history table (twin p.215):
*"February 6, 2026 | GSS India Opportunities AIF Scheme I | BGTF One Holdings
(DIFC) Limited | 2,687,559 | 1.00 | 1,053.00 | Cash | 2,830.00"* = **2,687,559
shares at Rs 1,053, Rs 2,830.00 million (Rs 283.00 Cr)**. Identity: *"GSS India
Opportunities AIF Scheme I (an affiliate of Bain Capital Special Situations,
LP)"* (RHP twin p.372). Bain entry IS in the filed RHP (not media only).

---

---

## BLOCK H — GUIDANCE AND PROMISE LEDGER

### H1. Forward-statement ledger

Status key: DELIVERED / PARTIAL / MISSED / PENDING / DROPPED. "PENDING" = period
not yet elapsed as of run date 2026-09-02. Concall pages are twin-marker pages.

| # | Statement (verbatim / near-verbatim) | Document + page | Period | Status | Evidence for status + anchor |
|---|---|---|---|---|---|
| 1 | *"we will ... build and commission upwards of 1.5 GW in fiscal 26-27. That's the guidance we have given"* | Mar call p.11 | FY27 | PENDING | Reaffirmed: *"minimum of 1,500 MW"* May call p.7; *"guidance of 1.5 gigawatt of minimum new capacity addition"* / *"stick to it, that we will add over 1.5 gigawatt in the current [fiscal]"* Aug call p.3, p.7 |
| 2 | *"4,600 megawatt of opex capacity minimum by 1st April 2027"* (= 3,100 MW at 1-Apr-2026 + ~1,500 MW added FY27) | Aug call p.6 | by 1-Apr-2027 | PENDING | New guidance introduced Aug call; not present in Mar/May (grep). Anchor Aug call p.6 |
| 3 | *"we will have a minimum EBITDA of INR3,000 crores in FY28, which is nearly 2.4x the EBITDA in FY26 ... from about INR1,290 crores in FY26"* | Aug call p.4 (also p.7) | FY28 | PENDING | New guidance Aug call; *"minimum reported EBITDA in FY28 of about INR3,000 crore ... nearly 2.3 times growth in 2 years"* Aug call p.7. Internal 2.3x vs 2.4x wording (both stated) |
| 4 | *"the steady-state net debt corresponding to this INR3,000 crores EBITDA will be INR16,000 [crores]"* | Aug call p.18 | steady-state (FY28 basis) | PENDING | New Aug call; *"the debt will be about INR16,000 crores for assets corresponding there"* Aug call p.18 |
| 5 | *"it goes up to 85%, 86% in 2 to 3 years"* (RE Power Sales EBITDA margin) | Mar call p.9 | 2-3 years | PENDING | Reaffirmed: *"EBITDA margin goes from about 83% today on RE power sales to nearly 86%"* May call p.16. Current level 83% (Mar/May), so not yet reached |
| 6 | Cost of debt to fall: *"continuously refinance as assets stabilize and bring the cost of debt down"* | Mar call p.8 | ongoing | PARTIAL (progressing) | *"weighted average rate of interest was 9.4% in ... April 2025 ... has fallen about 100 basis points to 8.4% ... as of June 2026"* Aug call p.3 |
| 7 | Credit-rating upgrade to AA | (aspiration implicit; achieved) | achieved Q1 FY27 | DELIVERED | *"recently our credit rating also got upgraded to a AA minus threshold"* Aug call p.5; *"our credit rating now is AA, which was a A+ for the last quarter same period"* Aug call p.10. **Discrepancy:** AA minus (p.5) vs AA (p.10) in the same call; prior rating stated A+ |
| 8 | Maiden domestic bond issuance: *"looking to tap the domestic credit market, so the bond markets, for the first ever corporate bond issuance by us"* | Aug call p.5 | near-term ("soon") | PENDING | *"we'll be coming up with a first domestic bond for CleanMax hopefully soon"* Aug call p.10 |
| 9 | *"you would have 100% of the land in place, for the capacity building in March 27, latest by September 2026"* | Mar call p.17 | by Sep-2026 | PENDING | Stated Mar call (then ">80% in place"). Not re-mentioned in May/Aug calls (grep). Deadline coincides with run date |
| 10 | Osaka Gas JV: *"our intention is to build about 400 MW or more in this joint venture over three years"* (CleanMax 51% / Osaka Gas 49%) | Mar call p.7 | 3 years | PENDING | *"already received in the third quarter of FY26 equity contribution of INR 176 crores from Osaka Gas"* Mar call p.7. Target not re-mentioned in May/Aug calls (grep) |
| 11 | Apple JV #2: *"This is our second joint venture with Apple ... CleanMax owns 51% and Apple India Private Limited owns 49%. Apple is investing INR104 crores of equity for a 49% equity stake in 150 MW of projects"* | May call p.9 | announced Q4 FY26 | DELIVERED | JV structure and INR104 cr investment stated as done; *"three different projects ... financial investments in projects with us"* May call p.9 |
| 12 | BESS / storage strategy announcement: *"we expect that in three or four months' time we will be able to make a proper announcement to investors in terms of what we are doing in storage and what that impact is on both DSM, curtailment, and revenue side"* | May call p.12 | ~3-4 months (by ~Aug/Sep 2026) | PARTIAL | By Aug: *"greenlit our first BESS investment already ... our STU project in Rajasthan"* Aug call p.12; two BESS at Koppal referenced (Aug p.11). A full quantified storage/DSM/revenue-impact announcement not evidenced in the Aug transcript |
| 13 | DSM revenue-impact figure | May call p.12 | pending decision | NOT DISCLOSED / PENDING | *"our own internal calculations of impact are not mature enough to share with an external investing audience yet"* May call p.12. No DSM impact figure quantified in Aug call (grep). Bikaner curtailment cited at *"30%"* (May call p.19), but a company-level DSM rupee/percent impact is **NOT DISCLOSED** |
| 14 | Quarterly generation disclosure "going forward": *"we'll provide that on a continued basis every quarter in terms of million units of generation"* (on website) | Mar call p.11 | every quarter, going forward | PENDING | Commitment made Mar call in response to analyst; publication is to the website, which the corpus cannot confirm. Not restated in May/Aug transcripts (grep) |
| 15 | Bikaner 2 (525 MW CTU) curtailment resolution: *"somewhere in the quarter between October to December 2026 is by when they expect to resolve the same"* | Mar call p.18 | Oct-Dec 2026 | MISSED / SLIPPED | By Aug: *"We don't know, honestly, and this number keeps changing ... to be conservative, we should assume it continues for the rest of the fiscal"* Aug call p.21. The Oct-Dec 2026 estimate is withdrawn to "rest of FY27" |
| 16 | Koppal CTU bays: two bays *"commission by October '26 and March '27"* (543 MW of the 1.5 GW) | Aug call p.11 | Oct-2026 and Mar-2027 | PENDING | *"where two bays have been allocated and they commission by October '26 and March '27"* Aug call p.11; *"even if the second one gets slightly delayed, we'll still meet our [1.5 GW] target"* Aug call p.11. May call described the same CTU project as *"530 MW ... 450 MW of wind and about 80 MW of solar in a substation called Koppal"* (May call p.11) |

Supporting presentation forward statements (Investor_Presentation_1, twin p.8):
*"6.0 GW RE Power Sales contracted capacity; ~31% YoY growth in operational power
sales capacity"*; *"Commissioning in FY 27: Min 1,500 MW"*; *"3x growth in
contracted capacity (~ 2 years); 1.6 GW contracted in 12 months"*.

**Intra-guidance discrepancies flagged:** (a) AA minus vs AA rating within the
Aug call (rows 7); (b) Koppal CTU capacity 530 MW (May) vs 543 MW (Aug) (row 16);
(c) FY28 EBITDA growth stated as 2.4x (Aug p.4) and 2.3x (Aug p.7) (row 3).

### H2. Dropped items (stated once, not re-mentioned in later calls)

Absence confirmed by page-search (grep) of the subsequent transcript(s).

- **100% land by September 2026.** Last appeared: Mar call p.17. Absent from May
  and Aug transcripts (no "land"/"September 2026" land-completion mention).
- **Osaka Gas JV "400 MW or more over three years."** Last appeared: Mar call
  p.7. Absent from May and Aug transcripts (no Osaka Gas target restated; Aug's
  "400 megawatt" p.7 refers to total opex added in the half, not the Osaka JV).
- **DSM quantified impact figure.** Introduced (and declined to quantify) May
  call p.12. Never quantified in the Aug call. Remains unquantified.
- **The "three or four months" storage/DSM/revenue announcement (May call
  p.12).** By the Aug call the company reported a first BESS greenlit (STU
  Rajasthan) but did not deliver the promised quantified storage-plus-DSM-plus-
  revenue announcement; the specific promise itself was not restated.
- **Quarterly generation disclosure (Mar call p.11).** Commitment not restated in
  May or Aug transcripts; delivery is to the website, outside this corpus.

---

---

## BLOCK I — CUSTOMER CONCENTRATION

### I1. Note 38 "no single customer >10%" and RHP top-N table

**Consolidated Note 38 (AR twin p.683):** *"Information about major customers:-
There is no single customers from whom the Group has earned more than 10% of its
total revenue."*

**RHP customer table — present.** Risk-factor line: *"Our top 10 customers, all
of whom are based in India, contributed 34.95%, 38.55%, 36.16%, 45.39% and 44.32%
of our Revenue [from operations for the periods indicated]"* (RHP twin p.30). Full
table (RHP twin p.51):

| | 6M ended 30-Sep-2025 | 6M ended 30-Sep-2024 | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|---|
| Revenue from top 10 customers (Rs mn) | 3,260.67 | 2,607.63 | 5,408.58 | 6,309.05 | 4,120.05 |
| Revenue from operations (Rs mn) | 9,329.53 | 6,764.66 | 14,957.01 | 13,898.37 | 9,295.82 |
| Top 10 as % of revenue from operations | 34.95% | 38.55% | 36.16% | 45.39% | 44.32% |

Comment: the RHP top-10 table (twin p.51) is extracted in full above; the AR
consolidated Note 38 states no single customer exceeds 10% of Group revenue.

### I2. Data & AI share of contracted capacity (14% and 42%)

- AR (twin p.241): *"42% of our contracted renewable energy sales capacity comes
  from the Data and AI segment. We did not follow this shift. We anticipated
  it."* And (twin p.244): *"~42% of our contracted portfolio comprises Data and
  AI customers. This is almost a tenfold jump in two years."*
- AR (twin p.257): Data & AI contracted share *"from a mere 14% in April 2024."*
- Presentation (twin p.6, slide "Data & AI"): *"42% ... OF CONTRACTED RE POWER
  SALES CAPACITY Is with Data & AI customers which is the major growth driver."*
- May call (p.3): *"about 42% is for Data and AI ... on 1st April 2024, this
  number was about 14%."*; (p.7): *"42% of our total contracted capacity up from
  14% two years ago ... grown from about 260 MW to 2,400 MW."*
- Aug call (p.4): *"We had 42% of our capacity in Data and AI in terms of our
  contracted capacity ... we have about 10x growth"*; (p.7): *"maintained its
  position at about 42% of our aggregate contracted [capacity]."*

Summary (anchored): **14%** on 1-April-2024 rising to **~42%** now (contracted RE
power-sales capacity in Data & AI); ~260 MW to ~2,400 MW, ~10x in two years.

### I3. Standalone Note on Customer A (18.49% FY26, 10.00% FY25)

Standalone Note 38 (AR twin p.811): *"Information about major customers:- The
details of the customers from whom the Company has earned more than 10% of its
total revenue are as under:- ... Customer A [% of total revenue] For the year
ended 31st March, 2026: 18.49% | For the year ended 31st March, 2025: 10.00%."*

Is Customer A identified as a subsidiary or related party? The standalone note
names the customer only as "Customer A" and gives no identity, no relationship,
no subsidiary/related-party tag. No cross-reference to the related-party note
(Note 54-series RPT disclosures) identifies Customer A. Identity / related-party
status of Customer A: **NOT DISCLOSED** (docs checked: AR standalone Note 38 twin
p.811; AR consolidated Note 38 twin p.683). Anchored fact recorded, no
inference drawn: the consolidated Group reports no single customer above 10%
(twin p.683) while the standalone Company reports Customer A at 18.49% (twin
p.811).

### I4. Credit-quality mix series (AA/AAA/MNC + A-rated), each call

| Call | AA / AAA / MNC share | A-rated share | A-and-above | Anchor |
|---|---|---|---|---|
| Mar 2026 (Q3 FY26) | ~83% | 14% | ~97% | *"about 83% of the MWs contracted are with AA, AAA, or multinationals, 14% is with A rated, so about 97% of our volumes are with A rated or above"* Mar call p.6 |
| May 2026 (Q4 FY26) | 82% | 14% | 96% | *"82% of our volumes are with clients who are credit rated AA, AAA, or multinationals, another 14% is in A rated, and therefore 96% is with credit rated A and above and 82% is AA, AAA, MNCs"* May call p.8 |
| Aug 2026 (Q1 FY27) | "well above 80%" | (not split) | (not split) | *"how much of our customers are rated AA, AAA or multinational subsidiaries in India ... that number has been well above 80% and continues to be"* Aug call p.5; *"80% share of volumes with clients who are rated AA, AAA or multinational, so that continues"* Aug call p.7 |

Comment: the AA/AAA/MNC share reads 83% (Mar) then 82% (May) then "above 80%"
(Aug), matching the B05 record of 83% -> 82% -> "above 80%". The Aug call gives
the top tier only ("above 80%") and does not restate the separate A-rated slice.

---

*End of Part 4 (Blocks G, H, I). Block V not written, per instruction.*

---

## BLOCK V — VERIFICATION

Every document quoted in Blocks A-I above, with the filename in the run folder, the date printed on the document, the text-twin page count, and the corpus commit hash read from.

| Document | Filename (under runs/cleanmax-2026-09-01/) | Date on document | Twin pages |
|---|---|---|---|
| Annual Report FY2025-26 (16th AGM) | inputs/annual-report/0da3293c-ae05-4b6d-b21f-0b3793bfecbc.txt | 30-Jun-2026 (FY2025-26) | 859 |
| Red Herring / Prospectus | inputs/prospectus/RHP_Prospectus_2026-02-25.txt | 25-Feb-2026 | 994 |
| Earnings call, Q3 FY26 | inputs/concalls/Concall_Mar_2026_Transcript.txt | Mar-2026 (qe 31-Dec-2025) | 21 |
| Earnings call, Q4 FY26 / FY26 | inputs/concalls/Concall_May_2026_Transcript.txt | May-2026 (ye 31-Mar-2026) | 23 |
| Earnings call, Q1 FY27 | inputs/concalls/Concall_Aug_2026_Transcript.txt | 03-Aug-2026 (qe 30-Jun-2026) | 24 |
| Results filing, Q1 FY27 (unaudited consol) | inputs/results/666b6d73-407a-49cf-b2f1-36cb7a4c4661.txt | board 31-Jul-2026 | 32 |
| Results filing, Q4 FY26 + FY26 (audited) | inputs/results/abfeff84-1562-4ad7-9de1-d08394ad566a.txt | board 12-May-2026 | 36 |
| CARE rating press release | inputs/rating/202510121005_Clean_Max_Enviro_Energy_Solutions_Limited.txt | 12-Oct-2025 (A+ Positive) | 12 |
| CARE rating press release | inputs/rating/202605120525_Clean_Max_Enviro_Energy_Solutions_Limited.txt | 12-May-2026 (AA- Stable, upgrade) | 11 |
| Investor Presentation, Q1 FY27 | inputs/presentation/Investor_Presentation_1.txt | Q1 FY27 | 37 |

**Corpus commit hash read from:** `8b5bc8b942b3d79418abe381e44d5defcc60e0be` (working-tree state at extraction; the CLEANMAX corpus content was established at the corpus-prep commit 9069a048 and is unchanged since).

**SECONDARY-tier usage:** No figure in Blocks A-I was taken from an operator-ferried SECONDARY file. The operator-ferried announcements summary and the Screener shareholding rendering were NOT quoted anywhere in this extraction; all quotes are from the filed documents listed above. Where a value could only come from a filed quarterly shareholding-pattern PDF (e.g. a full 12-quarter pledge/holding series, Block G) and that PDF is absent, the item is marked NOT DISCLOSED rather than filled from the SECONDARY summary.
