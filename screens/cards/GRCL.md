# GRCL: Gayatri Rubbers and Chemicals Ltd

Shallow Analysis Framework v1.0. Screened 2026-11-04 by Claude Code. Rewrite of
the blind card of the same date.
NSE GRCL | BSE code: none recorded | ISIN: not recorded (MANIFEST.md, identity line).
Corpus: `screens/corpus/GRCL/`. Status: PARTIAL. One secondary source only.

**Citation key.** "DS n" means `inputs/screening/Financials.txt`, sheet "Data
Sheet", line n. The file is a screener.in export. It has no pages, so lines
stand in for pages. It is a secondary source, not a filing. The P&L, Quarters,
Balance Sheet and Cash Flow sheets in the dump are empty formula templates
(Financials.txt, lines 1 to 62). Only the Data Sheet carries values (lines 76
to 138). The dump holds no ratios sheet and no shareholding sheet.

---

## Business Understanding Narrative

**What does it do, and how does it make money?** The corpus holds no business
description. The name points to rubber and chemicals. The cost structure fits a
light-asset converter. Material cost was 88% of sales in the period to December
2022 and 64% in FY2026 (DS 86, 87, 88). Net block is Rs 5.47 crore against
Rs 41.79 crore of sales, so each rupee of plant turns 7.6 rupees of revenue
(DS 86, 119). Employees cost 4% of sales (DS 92). That is a small processor
buying a commodity input and selling a converted product.

**What is changing?** The spread. Revenue grew 31% in each of FY2025 and FY2026,
to Rs 41.79 crore (DS 86). Operating margin rose from 7.8% in FY2023 to 21.1%
in FY2026. Profit after tax rose from Rs 0.91 crore to Rs 5.59 crore (DS 99).
The cause is not in the corpus.

**Why now?** FY2026 is the step. Material cost fell to 63.7% of sales from
75.5% in FY2025. Net block doubled from Rs 2.48 crore to Rs 5.47 crore in the
same year (DS 119). New capacity and a wider spread landed together.

**What must be true for the thesis to work?** The 21% margin must be a real
spread, from product mix or input cost, and it must repeat. The inventory
build must be growth stock, not stuck or revalued stock.

**What breaks it?** Cash. Operating cash flow was negative in three of the last
four years (DS 132). Inventory rose from 42 days of sales in FY2023 to 134 days
in FY2026. If the profit is sitting in the warehouse, the margin is not real.
The second breaker is input cost: a natural rubber or chemical price swing
against a small converter.

---

## 1. Corpus ledger

| Held | Readable | Weakens if thin |
|---|---|---|
| Financials.xlsx, screener.in export, 31 KB (collect.log, line 8) | Through Financials.txt only | Secondary source for steps 5, 8, 13 |
| Financials.txt, text dump of the above | Yes, Data Sheet only | Steps 5, 13 usable |

Missing, per MANIFEST.md:
- Annual report: NOT FOUND (collect.log, line 14). Weakens steps 2, 3, 4, 6, 9.
- Concall transcripts and presentations: none (collect.log, lines 16 to 18).
  Weakens steps 6, 7, 13.
- Quarterly or half-year results: NOT FETCHED. The Quarters block in the Data
  Sheet is empty (DS 101 to 111). Weakens steps 5, 8, 13.
- Credit rating: NOT FETCHED. Kills step 10.
- Shareholding: NOT COLLECTED. The task said the dump would carry it. It does
  not. Kills step 4.

## 2. Business model and archetype

Segments, products, customers and revenue mix: NOT FOUND. Looked for in the
corpus ledger, which holds no narrative document.

The numbers describe the engine. Margin comes from the gap between the selling
price and the material bill. Gross spread (sales less material consumed) was
11.7% in the December 2022 period, 13.2% in FY2023, 17.1% in FY2024, 24.5% in
FY2025 and 36.3% in FY2026 (DS 86 to 88). Other manufacturing expense jumped
from Rs 0.07 crore to Rs 2.41 crore in FY2026 (DS 90). Part of the material
drop may be a reclassification into that line, such as job work. Combined, the
two lines fell from 75.7% to 69.4% of sales. The spread still widened by six
points after that adjustment.

**Archetype: commodity converter, provisional.** Assigned from cost structure
and name, not from a business description. Section 1B v3.7 Amendment 17 binds
if confirmed. `/step1` must confirm it from the annual report.

## 3. Competitive advantages

Unknown, with one signal. Return on capital employed reached about 38% in
FY2026 on average capital (computed, DS 97, 96, 114 to 116). A pure price-taker
does not usually earn that. Either the company has a niche product, or FY2026
caught a cheap input. Pricing power, switching costs and customers are NOT
FOUND. Scale is absent: Rs 41.79 crore of revenue. Moat status: not shown.

## 4. The promoters

NOT FOUND. Holding, pledge, board, group and related-party dependence were
looked for in Financials.txt and MANIFEST.md. Neither carries them.

One capital fact is held. The share count rose from 42.10 lakh to 57.38 lakh,
up 36%, in the period ended March 2023 (DS 127). Financing cash inflow that
year was Rs 8.60 crore (DS 134). With an NSE-only listing and no BSE code, this
pattern fits a public issue, possibly on the SME platform. Unverified. No
dividend is recorded (DS 100).

## 5. Financial trajectory

| Rs crore | Dec-2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Sales (DS 86) | 16.65 | 22.21 | 24.41 | 31.91 | 41.79 |
| Operating profit (computed) | 1.06 | 1.73 | 2.73 | 4.69 | 8.81 |
| Operating margin | 6.4% | 7.8% | 11.2% | 14.7% | 21.1% |
| Profit before tax (DS 97) | 0.71 | 1.24 | 2.09 | 3.83 | 7.55 |
| Profit after tax (DS 99) | 0.55 | 0.91 | 1.56 | 2.85 | 5.59 |
| Tax rate (DS 98) | 22.5% | 25.8% | 25.4% | 25.6% | 26.1% |
| Borrowings (DS 116) | 1.86 | nil | 0.52 | 2.67 | 6.93 |
| Net worth (DS 114, 115) | 4.62 | 9.71 | 11.27 | 14.12 | 19.70 |
| Cash from operations (DS 132) | 1.55 | (5.21) | (0.31) | (1.47) | 0.16 |
| Inventory, days of sales (DS 125) | n/a | 42 | 70 | 114 | 134 |
| Receivable days (DS 124) | n/a | 74 | 75 | 76 | 82 |

Operating profit is sales less expenses, rebuilt from the cost lines (DS 87 to
93). It reconciles to reported profit before tax in every column. The
December 2022 column sits three months before the March 2023 column. Its
period length is not stated, so this card does not use it for growth.

Return on average capital employed, computed: 22% in FY2024, 30% in FY2025,
38% in FY2026. Return on average equity was 33% in FY2026. Net debt is Rs 6.37
crore, 0.7 times operating profit (DS 116, 126). Interest cover is 12 times.

Tax is normal at 26%. The profit is taxed profit, not a shelter.

Cash conversion is the problem. Profit after tax across FY2024 to FY2026 was
Rs 10.00 crore. Operating cash flow across the same years was minus Rs 1.62
crore. Receivables plus inventory rose from Rs 7.04 crore to Rs 24.71 crore
since FY2023 (DS 124, 125). That rise is larger than all profit earned. Debt
and capex both rose in FY2026: borrowings up Rs 4.26 crore, investing outflow
Rs 3.61 crore (DS 116, 133).

**Classification: margin-led.** FY2026 revenue rose 31% and profit after tax
rose 96%. The six-point spread gain carries most of it. An asset event sits
behind it: net block doubled.

**The observation that separates the readings** is the FY2026 inventory note.
If the build is raw material bought ahead for new capacity, the margin is a
spread gain. If finished stock is rising and valued at cost, the margin is
stock build, and cash will not follow.

## 6. The transition and the quality ladder

No management claim exists in the corpus to quote. Looked for in: the corpus
ledger, which holds no annual report, transcript or presentation.

The numbers alone read as FROM R1 commodity price-taker (FY2023: 7.8% margin,
87% material cost) TO a return profile near R3 (FY2026: 38% ROCE). That is two
rungs in three years. The ladder base rate is one rung per two to three years.
A two-rung leap needs extraordinary proof and is itself a red flag. One year of
ROCE with negative cash flow is not that proof.

## 7. Growth-trigger register

| Trigger | Date | Source | Status |
|---|---|---|---|
| Net block doubled, Rs 2.48 crore to Rs 5.47 crore | FY2026 | DS 119, 133 | Delivered in the numbers, purpose not stated |
| Revenue growth of 31% for two years | FY2025, FY2026 | DS 86 | Delivered |
| Material cost down to 63.7% of sales | FY2026 | DS 87, 88 | Delivered, cause NOT FOUND |
| Any stated plan, product, customer or capacity target | n/a | No narrative document held | NOT FOUND |

## 8. Proof check

No proof point exists. No quarter or half-year after March 2026 is held (DS
101 to 111 empty). No trigger is stated, so nothing can be tested against it.
The annual numbers move the right way. The cash line moves the wrong way.

## 9. Flags from the documents

- **Cash conversion.** Operating cash flow negative in FY2023, FY2024 and
  FY2025, and Rs 0.16 crore in FY2026 against Rs 5.59 crore of profit (DS 132,
  99).
- **Inventory.** Up from Rs 2.53 crore to Rs 15.32 crore in three years, six
  times, while sales rose 1.9 times (DS 125, 86).
- **Cost reclassification risk.** Other manufacturing expense rose 34 times in
  FY2026 as material cost fell (DS 87, 90).
- **Debt funding growth.** Borrowings rose from nil in FY2023 to Rs 6.93 crore
  (DS 116).
- **Dilution.** Share count up 36% in the period to March 2023 (DS 127).
- **Disclosure.** No quarterly data, a blank company-name parse (collect.log,
  line 10), no annual report found. Likely half-yearly reporting. Unverified.
- **Price.** Shares trade at Rs 632.85 (DS 82) against Rs 379.0 at 31 March
  2026 (DS 136), up 67% since the year end.
- Related-party, auditor emphasis, litigation, concentration: NOT FOUND. No
  document that carries them is held.

## 10. Independent check: the credit rating

**NOT FOUND.** Not fetched (MANIFEST.md, known gaps). A company this size with
Rs 6.93 crore of debt may hold a bank-loan rating. If one exists, its rationale
is the fastest way to learn what the company makes. There is no independent
view on this card.

## 11. Posture: the Transition Decision Matrix

- **Proof gate: NOT FIRED.** The P&L shows a step. No transition is named, no
  cause is known, and no period after FY2026 is held. Delivery without a
  mechanism and without cash does not fire the gate.
- **Ugliness: ARTIFACT-OF-CLIMB, provisional.** The ugly optic is cash.
  Thirty-one percent growth, new plant and a stock build for new capacity would
  all absorb cash. That reading holds only if inventory days stop rising. If
  they keep rising, the reading turns STRUCTURAL.
- **Recognition gap: CLOSED.** Price basis is the Bull AI company record,
  market capitalisation Rs 363.1 crore, 2026-11-04, a service record, not a
  filed document. The Data Sheet agrees at Rs 363.13 crore (DS 83). Trailing
  PE is 65 times FY2026 profit. The R3 neighbourhood is about 19 times. Even R5
  sits near 24 times plus a premium. The market prices this above the top of
  the ladder. Year-end PE, computed from DS 136 and DS 127, was 88 times in
  FY2024, 93 times in FY2025 and 39 times in FY2026. The market has never
  priced it as a converter.

**Posture: PRICED NARRATIVE (TRAP).** Proof not fired, ugliness provisionally
an artifact, gap closed. If the inventory reading turns structural, the cell
becomes AVOID.

## 12. Verdict card

**WATCH, hard, no position case.**

The earnings line is real enough not to PASS on. Profit doubled, tax is
normal, and capital returns are high. But the multiple already exceeds every
rung, the cash does not follow the profit, and the corpus cannot say what the
company sells. A `/step1` run would spend its budget on a price that has
nothing left to recognise.

**Load-bearing facts to verify first**
1. The FY2026 inventory and materials notes. Is the 21.1% margin a real spread
   or stock build and reclassification?
2. The first FY2027 half-year or quarter result. Does the margin hold above
   20%, and does operating cash turn positive?
3. What the company makes, for whom, and why the spread widened, from the
   FY2026 annual report.
4. Promoter holding and pledge, from the latest shareholding pattern.
5. Listing segment and reporting frequency.

**What would change the view**
- Margin above 20% in H1 FY2027 with positive operating cash and flat inventory
  days moves it to a full look, at a lower price.
- A price that falls toward 25 to 30 times earnings while the margin holds
  reopens the gap.
- Inventory days above 134 or another year of negative cash moves it to PASS.

No Role 1 valuation was run and no target price is set. This verdict decides
only whether the name earns a full `/step1`, and it is not a position.

## 13. Forward view

Operator ruling 2026-09-21. A screening metric, not a valuation. Read it with
steps 5, 8, 9 and 11, never instead of them.

| | |
|---|---|
| Market capitalisation (Bull AI company record, 2026-11-04, not a filed document) | Rs 363.1 crore |
| Last reported full-year profit after tax, FY2026 (DS 99) | Rs 5.59 crore |
| FY2027 expected profit after tax | Rs 7.3 crore |
| Growth | +31% |
| **Forward price-to-earnings** | **49.7x** |
| Basis tier | C, trend. No guidance and no quarter exist. FY2027E applies the delivered two-year revenue growth rate of 30.8% to FY2026 sales and holds the FY2026 profit margin of 13.4%. The mechanism is the doubled net block. The source is secondary. |

**Built on the weakest tier, from a secondary source.** The estimate does not
extrapolate the margin. Profit grew 83% a year from FY2023 to FY2026, and
projecting that rate would assume the spread keeps widening. If the margin
falls back to FY2025's 8.9%, FY2027 profit is Rs 4.9 crore, below FY2026. The
forward multiple then becomes 74 times. Even the central case sits at 50 times
for 31% growth. The screen does not favour this name.

Word count: about 2,100, tables included. Over the 1,900 target. The tables
and citations carry the load; the card is not padded.
