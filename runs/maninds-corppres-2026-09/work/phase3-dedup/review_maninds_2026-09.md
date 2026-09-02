# MANINDS — Document Review (Corporate Presentation, 01 Sep 2026)

Agent: A4 ANALYST | Protocol: Document Review Protocol v1.0 (loaded alone) |
Model: claude-opus-4-8 | Quarter tag: 2026-09
Doctype: single standalone investor presentation (Reg-30 intimation + deck, 37 pages).
Inputs consumed: A1 structured (R001-R335), A1 fulltext (verbatim reads at cited lines),
A2 ledger, A3 forensics. No source PDF, no inputs/ opened.

Framing: THESIS CHECK. A live Notion thesis exists. Decision Status verified below
BEFORE any position framing.

---

## STEP 1 — LEDGER RECONCILIATION PREAMBLE

Ledger contains 335 structured disclosure units across 37 slides (34 data-bearing,
3 dividers). All 335 reviewed. Category tie-out from A2: NUMBER 223, ENTITY 49,
FORWARD 20, DATE 43; slides 37; footnotes 4 logical units; zero-standing 2. Count
test gate_a2: pass. No orphan IDs.

A3 findings incorporated: A3-01, A3-02, A3-03, A3-04, A3-05, A3-06.
A3 checklist FINDINGs incorporated: F2, F6, F10, F14, F15, F16. PASS: F1, F7, F8, F11.
N.A. (not runnable on a presentation): F3, F4, F5, F9, F12, F13, F17.

No prior-quarter deck supplied. A3 F15/F16 dropped-disclosure and prior-list diffs
are NOT runnable this run; that limit is carried forward, not silently closed.

All ledger rows reviewed. Proceeding.

---

## STEP 2 — EXTRACTION TABLES (every cell line-anchored or ND)

### 2.1 Growth-trajectory headline (slide 4, FY22 vs FY26)

| Metric | FY22 | FY26 | CAGR | anchor |
|---|---|---|---|---|
| Revenue (Rs Cr) | 2,178 | 3,592 | 13.4% | R005/R006/R007 |
| EBITDA (Rs Cr) | 218 | 468 | 21.0% | R010/R011/R012 |
| PAT (Rs Cr) | 102 | 171 | 13.8% | R015/R016/R017 |
| ROCE | ND | 18.4% | n/a | R018 |
| ROE | ND | 9.2% | n/a | R019 |
| Networth (Rs Cr) | ND | 2,087 | n/a | R020 |

Note: slide-4 Rs-Cr headline is the STANDALONE-scale trajectory (FY26 revenue Rs3,592 Cr
approximates standalone Rs34,552 Mn at R149, not consolidated Rs35,639 Mn at R161).
ROCE 18.4% is a headline figure; no clean-basis build is disclosed (see Step 5).

### 2.2 Standalone P&L, FY26 vs FY25 (slide 28, INR Mn)

| Line | FY26 | FY25 | YoY | anchor |
|---|---|---|---|---|
| Revenue from Operations | 34,552 | 31,182 | 10.8% | R149 |
| Other Income | 531 | 542 | (2.0)% | R150 |
| Total Income | 35,083 | 31,724 | 10.6% | R151 |
| Operating expenses | 30,155 | 28,415 | 6.1% | R152 |
| EBITDA* (incl. Other Income) | 4,928 | 3,309 | 48.9% | R153 |
| EBITDA Margin | 14.0% | 10.4% | +360 bps | R154 |
| Depreciation & amortization | 756 | 433 | 74.6% | R155 |
| Finance costs | 1,542 | 1,022 | 50.9% | R156 |
| PBT | 2,630 | 1,854 | 41.8% | R157 |
| Tax | 672 | 484 | 39.0% | R158 |
| PAT | 1,958 | 1,370 | 42.8% | R159 |
| PAT Margin | 5.6% | 4.3% | +130 bps | R160 |

*Footnote (line 775): "EBITDA is inclusive of Other Income, since it's operational in nature."

### 2.3 Consolidated P&L, FY26 vs FY25 (slide 29, INR Mn)

| Line | FY26 | FY25 | YoY | anchor |
|---|---|---|---|---|
| Revenue from Operations | 35,639 | 35,054 | 1.7% | R161 |
| Other Income | 286 | 200 | 43.2% | R162 |
| Total Income | 35,925 | 35,253 | 1.9% | R163 |
| Operating expenses | 31,246 | 31,690 | (1.4)% | R164 |
| EBITDA* (incl. Other Income) | 4,679 | 3,563 | 31.3% | R165 |
| EBITDA Margin | 13.0% | 10.1% | +290 bps | R166 |
| Depreciation & amortization | 789 | 453 | 74.4% | R167 |
| Finance costs | 1,520 | 1,027 | 48.1% | R168 |
| PBT | 2,370 | 2,084 | 13.7% | R169 |
| Tax | 665 | 552 | 20.4% | R170 |
| PAT | 1,705 | 1,532 | 11.3% | R171 |
| PAT Margin | 4.7% | 4.3% | +40 bps | R172 |

*Footnote (line 812): identical wording to standalone.

### 2.4 Margin normalisation ex-other-income (A3-01; inputs line-anchored, arithmetic shown)

| Basis | EBITDA* | less Other Income | ex-OI EBITDA | Revenue from Ops | ex-OI margin | headline margin |
|---|---|---|---|---|---|---|
| Standalone FY26 | 4,928 (R153) | 531 (R150) | 4,397 | 34,552 (R149) | 12.7% | 14.0% (R154) |
| Standalone FY25 | 3,309 (R153) | 542 (R150) | 2,767 | 31,182 (R149) | 8.9% | 10.4% (R154) |
| Consolidated FY26 | 4,679 (R165) | 286 (R162) | 4,393 | 35,639 (R161) | 12.3% | 13.0% (R166) |
| Consolidated FY25 | 3,563 (R165) | 200 (R162) | 3,363 | 35,054 (R161) | 9.6% | 10.1% (R166) |

FLAG (Notion tripwire "EBITDA margin ex-other-income vs 13% floor"): consolidated FY26
ex-OI EBITDA margin = 12.3%, BELOW the 13% floor. The 13.0% headline clears the floor
only because Rs286 Mn other income is folded into EBITDA. The deck's own note reclassifies
other income as operational; on a clean basis the floor is not met.

### 2.5 Historical consolidated (slide 31, INR Mn)

| Metric | FY23 | FY24 | FY25 | FY26 | anchor |
|---|---|---|---|---|---|
| Total Income (incl. OI) | 22,703 | 31,942 | 35,253 | 35,925 | R209 |
| Gross Profit | 4,973 | 7,907 | 7,905 | 13,639 | R210 |
| Gross Profit Margin | 21.9% | 24.8% | 22.4% | 38.0% | R211 |
| EBITDA | 1,760 | 2,932 | 3,563 | 4,679 | R212 |
| EBITDA Margin | 7.8% | 9.2% | 10.1% | 13.0% | R213 |
| PAT | 670 | 1,051 | 1,532 | 1,705 | R214 |
| PAT Margin | 3.0% | 3.3% | 4.3% | 4.7% | R215 |

FLAG (A3-02): gross-profit margin jumps 1,560 bps (22.4% -> 38.0%) in one year on
+1.9% total income, while EBITDA margin rises only 290 bps. Gross profit +5,734 Mn
(7,905 -> 13,639) but EBITDA only +1,116 Mn. A COGS/opex reclassification between the
gross-profit line and operating expenses is the mechanical read, not a real gross-margin
gain. The historical gross-margin baseline is not comparable across the FY25/FY26 break.

### 2.6 Consolidated balance sheet (slide 30, INR Mn)

| Line | FY24 | FY25 | FY26 | anchor |
|---|---|---|---|---|
| Equity Share Capital | 324 | 324 | 375 | R173 |
| Other Equity | 13,725 | 15,749 | 20,490 | R174 |
| Shareholders Fund | 14,049 | 16,073 | 20,865 | R175 |
| Long-term Borrowings | 1,363 | 1,385 | 2,402 | R176 |
| Lease Liabilities (non-current) | 141 | 156 | 610 | R177 |
| Deferred tax liabilities (net) | 258 | 276 | 258 | R178 |
| Total Non-current Liabilities | 1,803 | 1,890 | 3,367 | R180 |
| Short-term Borrowings | 1,722 | 3,175 | 2,595 | R181 |
| Lease Liabilities (current) | 34 | 47 | 674 | R182 |
| Trade payables | 5,028 | 12,002 | 14,712 | R183 |
| Current tax liabilities | 54 | 21 | 275 | R184 |
| Other financial liabilities | 278 | 301 | 5,797 | R185 |
| Other current liabilities | 1,184 | 4,283 | 1,921 | R186 |
| Total Current Liabilities | 8,300 | 19,829 | 25,974 | R187 |
| Property, Plant & Equipment | 5,234 | 5,539 | 6,546 | R189 |
| Right-of-use Assets | 163 | 186 | 1,389 | R190 |
| Capital WIP | 305 | 1,334 | 3,258 | R191 |
| Goodwill on Consolidation | 639 | 688 | 688 | R192 |
| Intangible assets | ND (FY24 nil) | 5 | 3 | R194 |
| Trade Receivables (non-current) | 967 | 973 | 2,385 | R195 |
| Total non-current assets | 8,154 | 10,286 | 14,875 | R198 |
| Inventories | 6,456 | 12,685 | 15,350 | R199 |
| Investments | 2,280 | 260 | 708 | R200 |
| Trade Receivables (current) | 3,551 | 8,959 | 10,098 | R201 |
| Cash & Bank Balances | 2,549 | 3,792 | 6,572 | R202 |
| Loans | 22 | 2 | 157 | R203 |
| Current Tax Assets | ND (nil all yrs) | ND (nil) | ND (nil) | R206 |
| Total Current Assets | 15,998 | 27,506 | 35,331 | R207 |
| Total Assets | 24,152 | 37,792 | 50,206 | R208 |

Net-debt vs net-cash reading (Notion tripwire), consolidated FY26:
- Gross borrowings ex-lease = 2,402 + 2,595 = 4,997 (R176+R181).
- Cash & Bank 6,572 (R202) + Investments 708 (R200) = 7,280.
- Net CASH ex-lease = 7,280 - 4,997 = +2,283 Mn.
- Add lease liabilities 610 + 674 = 1,284 (R177+R182): net cash incl. leases = +999 Mn.
Reading: the group is net cash on borrowings, thin net cash after lease liabilities. The
tripwire resolves benign on the debt line, but see working-capital direction below.

### 2.7 NPC (National Pipe Company, KSA) standalone, CY2025 (slide 26)

| Metric | SAR M | USD M | margin/ratio | anchor |
|---|---|---|---|---|
| Revenue | 792.7 | 211.4 | — | R120 |
| Gross Profit | 214.1 | 57.1 | 27.0% | R121/R122 |
| EBITDA | 196.7 | 52.5 | 24.8% | R123/R124 |
| EBIT | 164.9 | 44.0 | 20.8% | R126/R127 |
| PBT | 162.0 | 43.2 | 20.4% | R130/R131 |
| Tax & Zakat | 18.5 | 4.9 | 11.4% | R132/R133 |
| PAT | 143.5 | 38.3 | 18.1% | R134/R135 |
| ROE | — | — | 25.7% | R141 |
| ROCE | — | — | 29.5% | R142 |
| ROA | — | — | 22.5% | R143 |
| Cash & liquid assets (Apr'26) | 311.3 | 83.0 | — | R139 |
| Net worth (Apr'26) | 594.9 | 158.6 | — | R140 |
| Order book at acquisition | — | 120.0 | Rs1,130-1,150 Cr | R144 |

Consideration USD 102 M (USD 70 M debt + USD 32 M equity), R091/R092/R093. FX SAR/USD 3.75
pegged, SAR/INR 23.955 (R145/R146). CY2025 revenue Rs~1,898.9 Cr, PAT Rs~343.6 Cr (R147/R148).
Implied purchase multiple: USD 102 M / USD 38.3 M PAT = ~2.7x; net of USD 83 M cash the
enterprise outlay is ~USD 19 M against USD 52.5 M EBITDA. VALUATION-RELEVANT: this reads
cheap on a single CY2025 snapshot. Whether CY2025 is a peak/representative year is not
answerable from the deck. FLAGGED for the downstream valuation chain (Section 1B / Role 1);
this pass sets no price.

### 2.8 Quarterly consolidated trend (slide 32, INR Mn)

| Series | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | Q1FY27 | anchor |
|---|---|---|---|---|---|---|
| Total Income | 7,736 | 8,148 | 8,386 | 11,655 | 10,650 | R216 |
| Gross Profit (values) | 6,269; 3,820; 3,409; 1,833; 2,128 (per-quarter mapping ND) | | | | | R217 |
| Gross Profit Margin | 53.8%; 40.6%; 35.9%; 23.7%; 26.1% (mapping ND) | | | | | R217 |
| EBITDA (values) | 806; 1,018; 1,376; 1,480; 1,553 (mapping ND) | | | | | R218 |
| EBITDA Margin | 10.4%; 12.5%; 16.4%; 12.7%; 14.6% (mapping ND) | | | | | R218 |
| PAT (values) | 276; 370; 550; 509; 614 (mapping ND) | | | | | R219 |
| PAT Margin | 3.6%; 4.5%; 6.6%; 4.4%; 5.8% (mapping ND) | | | | | R219 |

Per-quarter mapping for R217/R218/R219 is NOT resolvable from the flattened bar-chart
layout (A1 caveat carried). Total Income (R216) IS resolvable in order. Q1FY27 income
10,650 includes only 40 days of NPC (R220); full NPC contribution from Q2FY27 (R286/R334).
Do not read the Q1FY27 gross-margin bars as a clean run-rate.

---

## STEP 3 — YoY / QoQ WALKS AND PAT BRIDGE

### 3.1 Standalone PAT bridge, FY25 -> FY26 (INR Mn)

| Step | Amount | anchor |
|---|---|---|
| EBITDA FY25 | 3,309 | R153 |
| + EBITDA growth | +1,619 | R153 |
| EBITDA FY26 | 4,928 | R153 |
| - Depreciation increase | -323 (433 -> 756) | R155 |
| - Finance-cost increase | -520 (1,022 -> 1,542) | R156 |
| = PBT increase | +776 (1,854 -> 2,630) | R157 |
| - Tax increase | -188 (484 -> 672) | R158 |
| = PAT increase | +588 (1,370 -> 1,958) | R159 |

Standalone PAT +42.8%. Revenue +10.8% with EBITDA +48.9%: operating-margin gain drives
most of the profit, but Rs531 Mn other income sits inside that EBITDA (Step 2.4). D&A +74.6%
and finance +50.9% reflect the Jammu/capex build and higher borrowings.

### 3.2 Consolidated PAT bridge, FY25 -> FY26 (INR Mn)

| Step | Amount | anchor |
|---|---|---|
| EBITDA FY25 | 3,563 | R165 |
| + EBITDA growth | +1,116 | R165 |
| EBITDA FY26 | 4,679 | R165 |
| - Depreciation increase | -336 (453 -> 789) | R167 |
| - Finance-cost increase | -493 (1,027 -> 1,520) | R168 |
| = PBT increase | +286 (2,084 -> 2,370) | R169 |
| - Tax increase | -113 (552 -> 665) | R170 |
| = PAT increase | +173 (1,532 -> 1,705) | R171 |

Consolidated PAT +11.3% on revenue +1.7%. EBITDA rose Rs1,116 Mn but D&A (+336) and
finance costs (+493) consumed 74% of it. The consolidated growth engine is far weaker
than the standalone optic: consol revenue is near-flat while standalone grew double digits.

---

## STEP 4 — STANDALONE-vs-CONSOLIDATED GAP (A3-03 / F2, first-class metric)

| Period | Standalone PAT | Consolidated PAT | Gap (C - S) | Gap % of standalone | anchor |
|---|---|---|---|---|---|
| FY25 | 1,370 | 1,532 | +162 | +11.8% (accretive) | R159/R171 |
| FY26 | 1,958 | 1,705 | -253 | -12.9% (dilutive) | R159/R171 |
| Swing | — | — | -415 | -21.2% of FY26 std PAT | derived |

Revenue decomposition:
- Standalone revenue +10.8% (31,182 -> 34,552); consolidated +1.7% (35,054 -> 35,639).
- Implied subsidiary/elimination revenue (consol minus standalone): FY25 = 3,872 Mn;
  FY26 = 1,087 Mn. Non-standalone revenue FELL Rs2,785 Mn (-72%).

FLAG (Notion tripwire "consolidated vs standalone PAT divergence"): the gap REVERSED sign.
FY25 subsidiaries added Rs162 Mn; FY26 they subtracted Rs253 Mn. The 415 Mn swing is 21% of
standalone PAT, far above a 5-point materiality threshold. The consolidation drag arrives
BEFORE NPC enters the base (NPC = 40 days of Q1FY27 only). The pre-NPC subsidiary carry
(the Jammu SS build, Merino Shelters, MISIC set-up, other subs) turned dilutive on falling
subsidiary revenue. This must be decomposed by entity before Q2FY27 NPC consolidation
restructures the base and hides the trend. The deck gives no entity-level P&L split, so the
named-subsidiary attribution is NOT answerable from this document (Question Q3).

---

## STEP 5 — CASH-QUALITY NOTE

The deck carries NO cash-flow statement. Per protocol, cash conversion is INDETERMINATE and
the verdict caps at PROCEED WITH CAVEATS on this axis. It does NOT resolve silently to PROCEED.

Balance-sheet working-capital direction (Notion tripwire "working-capital direction"),
consolidated, FY24 -> FY25 -> FY26:
- Inventories: 6,456 -> 12,685 -> 15,350 (R199). Up +138% over two years; +21% FY26.
- Trade Receivables (current): 3,551 -> 8,959 -> 10,098 (R201). Up +184%; +13% FY26.
- Trade Receivables (non-current): 967 -> 973 -> 2,385 (R195). +145% FY26.
- Trade payables: 5,028 -> 12,002 -> 14,712 (R183). Up +193%; +23% FY26.

Reading: gross working capital ballooned. On consolidated revenue that is near-flat (+1.7%),
inventory +21% and total receivables rising is a cash-quality warning. Payables (+23%) fund
much of the build, which is why net debt stays benign (Step 2.6), but the group is financing
growth in inventory and receivables through its supply chain, not through operating cash the
deck can evidence. Net-working-capital direction: DETERIORATING in absolute terms; the deck
gives no cash generated from operations to confirm conversion. Cash conversion: INDETERMINATE.

ROCE clean basis (Notion tripwire "ROCE on a clean basis vs headline"): the deck reports
ROCE 18.4% headline (R018) with no build. Because EBITDA/operating profit folds in other
income (Step 2.4), any ROCE derived on the deck's operating-profit basis is inflated. A
clean-basis ROCE (operating profit ex-other-income over capital employed) is NOT computable
from the deck. NPC's own ROCE is 29.5% CY2025 (R142), a future consolidated tailwind, not a
clean read of the existing India business. Clean ROCE: NOT ANSWERABLE from this document.

---

## STEP 6 — THESIS / DECISION-STATUS RECONCILIATION

Decision Status VERIFIED: WATCHLIST. CMP Rs714. Entry zone Rs412-589. MoS Rs412. Position
size Small. No pre-committed trigger fired to date. This review is framed against WATCHLIST.
No HOLD/ADD/TRIM/EXIT framing applies; this is a watch name, not a held position.

Thesis line: "HSAW/LSAW line-pipe maker attempting a transition via the NPC Saudi Arabia
acquisition and value-added (stainless, coating) mix shift; watch whether consolidated
economics and ROCE clean basis support the re-rating."

Tripwire-by-tripwire reconciliation against the deck:

| Notion tripwire | This deck's read | Status |
|---|---|---|
| Consol vs standalone PAT divergence | Gap reversed to -253 Mn (FY26) from +162 Mn (FY25); 21% swing | ADVERSE (Step 4) |
| EBITDA margin ex-OI vs 13% floor | Consol ex-OI = 12.3%, below floor; headline 13.0% only via OI | ADVERSE (Step 2.4) |
| ROCE clean basis vs headline | Headline 18.4%; clean basis not computable; OI inflates operating profit | UNVERIFIABLE, leaning adverse |
| Net-debt vs net-cash | Net cash ex-lease +2,283 Mn; thin net cash incl. leases | BENIGN on debt line |
| NPC acquisition economics/integration | ~2.7x PAT, USD 120 M order book, ROCE 29.5%; 40-day Q1FY27 stub | CONSTRUCTIVE but unverified |
| Jammu/Dammam commissioning by Mar 2027 | Both targeted Mar 2027; Jammu Rs350 Cr of Rs600 Cr spent | ON TRACK per deck |
| India order-book split | NOT disclosed in deck (only NPC USD 120 M order book) | ND |
| Working-capital direction | Inventory +21%, receivables rising on flat consol revenue | ADVERSE (Step 5) |

Net: the deck ADVANCES the transition narrative (NPC economics, Jammu/Dammam on track,
value-added mix) while three load-bearing quality tripwires read adverse (S-vs-C reversal,
ex-OI margin below floor, working capital). The re-rating case the thesis watches for is NOT
confirmed by consolidated economics this period. No trigger fired; Decision Status stays
WATCHLIST. The deck does not move the name toward the entry zone; CMP Rs714 sits above the
Rs412-589 zone. Flag, human decides.

---

## STEP 7 — FORWARD-TARGET REGISTER (from A3 F6 commitment register + A1 FORWARD rows)

| Commitment | Implied date | Status word | anchor |
|---|---|---|---|
| Dammam Coating Plant (KSA) production | Mar 2027 | targeted | R273/R300 |
| Jammu SS Plant production (Rs350 Cr of Rs600 Cr spent) | Mar 2027 | underway | R274/R277/R318 |
| Merino Shelters project launch | Mid-Sep 2026 | on track | R280/R321 |
| Merino cashflow Rs35-50 Cr | FY27 | expected | R281 |
| Merino annual cashflow starts | FY28 | expected | R278/R320 |
| Merino revenue Rs700-800 Cr | next 5-6 years | expected | R279 |
| NPC full earnings contribution | Q2 FY27 | expected | R286/R334 |
| NPC 100% stake acquisition | 21 May 2026 | completed | R333 |
| NPC HSAW OD upgrade to 120" | no date | will upgrade | R107 |
| Revenue CAGR 20-25% | next 5 years | goal | R291/R221 |
| EBITDA margin to 15% long-term | 5-year horizon | goal | R292/R222 |

The 20-25% revenue CAGR goal (R291) sits against consolidated revenue +1.7% this year; it
depends on capacity relocation and new geographies (R287-R289), not the existing order book.
The 15% EBITDA goal (R292) is measured against a headline that already includes other income;
on a clean basis the FY26 base is 12.3% (Step 2.4). All 11 targets sit under the deck-wide
safe-harbour disclaimer (R269).

---

## STEP 8 — QUESTIONS FOR MANAGEMENT

Every A3 FORWARD-SIGNAL and AMBIGUOUS finding generates at least one question.

| # | Question | from finding |
|---|---|---|
| Q1 | The FY26 EBITDA note states other income is "operational in nature." Provide EBITDA on a clean basis (ex-other-income) for standalone and consolidated FY25 and FY26. On that basis consolidated FY26 is 12.3%. How does the 15% long-term goal reconcile against the clean base rather than the 13.0% headline? | A3-01 (AMBIGUOUS) |
| Q2 | Consolidated gross-profit margin moved 22.4% (FY25) to 38.0% (FY26) on +1.9% total income while EBITDA margin rose only 290 bps. What cost lines moved between the gross-profit build and operating expenses? Restate FY23-FY25 gross profit on the FY26 definition. | A3-02 (AMBIGUOUS) |
| Q3 | Consolidated PAT (1,705) fell below standalone (1,958) in FY26, reversed from FY25 (1,532 vs 1,370). Which subsidiaries turned dilutive, and by how much each? Non-standalone revenue fell from Rs3,872 Mn to Rs1,087 Mn; what drove that drop? | A3-03 (FORWARD-SIGNAL) |
| Q4 | Paid-up capital rose 15.7% (Rs324 Mn to Rs375 Mn) and other equity rose Rs4,741 Mn in FY26. State the instrument (the USD 32 M NPC equity component?), the share count issued, the issue price, and diluted EPS. The tables say "except EPS" but no EPS is shown. | A3-04 (AMBIGUOUS) |
| Q5 | The deck dates the NPC-Saudi Aramco relationship as "2+ decades / since 2005" (pages 19/21/24/25) and "40+ Years" (page 22, twice). Which is the approved-vendor certification date and which is NPC's founding-era relationship? Confirm the load-bearing date for the durability claim. | A3-05 (AMBIGUOUS) |
| Q6 | NPC consolidated for 40 days in Q1FY27, full contribution from Q2FY27. Provide NPC's standalone quarterly P&L for FY27 as it consolidates, and the pre-NPC vs post-NPC split, so the FY27 consolidated base stays reconcilable to FY26. | A3-06 (FORWARD-SIGNAL) |
| Q7 | On flat consolidated revenue (+1.7%), inventory rose 21% and receivables rose. Provide the FY26 consolidated cash flow from operations and the cash conversion cycle. Is the payables build (+23%) sustainable supplier financing or a stretch? | A3-03 / F2 working-capital extension |
| Q8 | NPC was bought for USD 102 M against CY2025 PAT of USD 38.3 M (~2.7x) with USD 83 M cash on its books. Why was it available so cheaply, and is CY2025 a representative or peak year for NPC margins (EBITDA 24.8%)? | NPC economics (Notion tripwire) |

---

## STEP 9 — MONITORABLES / CATALYST LIST

Seeded by the A3 commitment register (F6). Each item carries its implied date and source ref.

| Monitorable | Implied date | Watch for | source ref |
|---|---|---|---|
| Merino Shelters project launch | Mid-Sep 2026 | launch confirmed; first cash | R280/R321 |
| Q1FY27 already reported (40-day NPC stub) | reported | clean run-rate distortion | R220/R286 |
| Merino cashflow Rs35-50 Cr | FY27 | actual vs guidance | R281 |
| NPC full earnings contribution | Q2 FY27 | first full-quarter NPC economics; margin hold | R286/R334 |
| Q2FY27 consolidated restatement | Q2 FY27 | S-vs-C gap post-NPC; base reconciliation | Step 4 / A3-06 |
| Dammam Coating Plant production | Mar 2027 | commissioning; value-added margin layer | R273/R300 |
| Jammu SS Plant production (Rs250 Cr capex left) | Mar 2027 | commissioning; higher-margin SS mix | R274/R277/R318 |
| Merino annual cashflow starts | FY28 | recurring cash confirmed | R278/R320 |
| Revenue CAGR 20-25% | rolling, next 5 yrs | delivery vs +1.7% FY26 consol | R291 |
| EBITDA margin to 15% | 5-year | clean-basis progress vs 12.3% base | R292 |
| Merino revenue Rs700-800 Cr | next 5-6 yrs | monetisation milestones | R279 |
| Working-capital direction | each result | inventory/receivables vs revenue | Step 5 |
| Clean-basis ROCE and ex-OI EBITDA | each result | quality vs headline | Step 5 / Step 2.4 |

---

## VERDICT

PROCEED WITH FLAGS. Cash conversion INDETERMINATE (no cash-flow statement; caps the
cash-quality axis at PROCEED WITH CAVEATS, named). Three quality flags raised above caveat
level: (1) consolidated ex-OI EBITDA margin 12.3% sits below the 13% floor, cleared in the
headline only by reclassifying other income as operational; (2) standalone-vs-consolidated
PAT gap reversed to -253 Mn, a 21% swing, before NPC enters the base; (3) undisclosed equity
dilution (+15.7% paid-up capital, no share count or EPS). Company quality never halts the
run; these flags propagate, the human decides. Decision Status UNCHANGED (WATCHLIST); no
pre-committed trigger fired.

OUT OF SCOPE, flagged to the downstream chain (Section 1B / FTTCP / Role 1, not computed
here): NPC purchase multiple (~2.7x CY2025 PAT), the exit multiple, FV CAGR, and any entry-
zone re-work. The NPC economics and the gross-margin redefinition are valuation-relevant and
must be resolved before any re-rating case is priced.

---

## PLAIN-LANGUAGE BRIEF

### 1. SUMMARY NARRATIVE

Man Industries makes large steel line pipe (HSAW and LSAW) for oil, gas and water
projects. This deck (01 Sep 2026) reports FY26 results and pushes a transition story: the
NPC Saudi Arabia buy, a new Jammu stainless-steel plant, a Dammam coating plant, and a mix
shift to higher-margin products [this document].

The headline looks strong. Standalone revenue grew 10.8% to Rs34,552 Mn and standalone PAT
grew 42.8% to Rs1,958 Mn [this document, R149/R159]. But the consolidated picture is weaker.
Consolidated revenue grew only 1.7% to Rs35,639 Mn and consolidated PAT grew 11.3% to
Rs1,705 Mn [R161/R171]. For the first time, consolidated PAT sits below standalone PAT. Last
year subsidiaries added Rs162 Mn; this year they subtracted Rs253 Mn [R159/R171]. That
reversal is 21% of standalone profit and it happened before NPC even joined the accounts.

Two accounting choices flatter the numbers. EBITDA now includes other income, "since it's
operational in nature" [line 812]. Strip other income and consolidated EBITDA margin is 12.3%,
below the deck's 13.0% headline and below the 13% floor this thesis watches [derived from
R161/R162/R165]. Separately, consolidated gross-profit margin jumped from 22.4% to 38.0% in
one year on flat revenue [R211], which reads as a cost reclassification, not a real gain.

Working capital ballooned. Inventory rose 21% and receivables rose on near-flat revenue;
payables rose 23% and fund most of it [R183/R199/R201]. The deck carries no cash-flow
statement, so cash conversion cannot be judged. NPC itself looks bought cheap: USD 102 M for
a business earning USD 38.3 M PAT with USD 83 M of cash on its books [R091/R134/R139]. Whether
CY2025 is a normal year for NPC is unknown from the deck.

Decision Status stays WATCHLIST. CMP Rs714 is above the Rs412-589 entry zone. No trigger
fired. The transition narrative advanced; the consolidated economics did not confirm it.

### 2. SECTOR INTELLIGENCE

Man Industries fishes in the global oil, gas and water pipeline market. Demand is
project-driven and lumpy: large orders from national oil companies, water authorities and
EPC contractors, not steady repeat volume [this document, R265/R266 client and EPC rosters].
The Saudi and wider GCC market is the structural tailwind the thesis rests on. NPC gives
direct Aramco-approved vendor status and a USD 120 M order book on day one [prior Notion
thesis; this document R144]. Aramco approval normally takes 1-2 years of audits for a
greenfield entrant; buying NPC skips that wait [this document, R283].

The regulatory and tax backdrop in Saudi is favourable: NPC's effective tax-and-Zakat rate
is 11.4%, well below India's ~25% [this document, R133]. That is a future consolidated tax
tailwind once NPC earnings flow from Q2FY27 [R286].

The India demand cycle (water pipeline schemes, oil and gas capex, city gas) is not quantified
in this deck [not disclosed]. The India order-book split, a named thesis tripwire, is not
disclosed here [not disclosed]. Steel input cost, the main swing factor for a pipe converter's
spread, is also not broken out [not disclosed]. Sector read: the Saudi structural opportunity
is real and now owned; the India cycle detail this quarter is absent.

### 3. BUSINESS-MODEL INTELLIGENCE

The company converts steel plate and coil into welded line pipe, then adds coating (anti-
corrosion, concrete weight). Value rises as it moves from bare pipe to coated, delivered pipe,
and now toward stainless-steel seamless pipe from the Jammu plant [this document, R275/R276].
It is a build-to-spec / order-book converter: margin comes from spec, approvals and the
spread between steel input and pipe output, not from brand pricing power.

Unit economics this quarter: consolidated EBITDA margin 13.0% headline, 12.3% clean of other
income [this document; derived]. That is a converter-level margin, consistent with the
business model, not a franchise margin. The 15% long-term EBITDA goal [R292] depends on higher
utilisation, more stainless-steel share and more coating [R290]. NPC lifts the group's average:
NPC's own EBITDA margin is 24.8% and ROCE 29.5% [this document, R124/R142], far above the
India base. So the model drift the deck argues is mix upgrade via Saudi and stainless steel.

The model risk this quarter is quality drift, not model change. Other income folded into
EBITDA, a gross-margin line that jumped on flat revenue, working capital rising on flat sales,
and consolidated subsidiaries turning loss-making before NPC arrives [this document, Steps
2.4/2.5/4/5]. The business still makes money by converting steel; how cleanly it converts that
profit to cash is the open question the deck does not answer.

### 4. COMPETITION INTELLIGENCE

Man Industries competes in large-diameter line pipe. The deck names no direct listed peer;
the thesis peer set (Indian SAW pipe makers such as Welspun Corp, Jindal SAW, and regional
Gulf mills) is prior Notion / peer work [prior Notion thesis], not this document. Where Man
wins: it holds Aramco approval directly through NPC, a barrier that takes years to earn, and
it has a broad OD range (HSAW 12"-120" post-upgrade, LSAW 16"-56") and in-house coating
[this document, R060/R056/R107]. The NPC buy adds Saudi local manufacturing, which matters
for in-Kingdom content rules.

Where it is structurally weaker: scale and balance-sheet size sit below the largest Indian SAW
peers [prior peer work, not quantified in this deck]. As a price-taker converter, it has
limited pricing power; margins ride the steel spread and order timing, which is why
consolidated revenue can go flat in a year [this document, R161]. Client concentration risk is
visible in the reliance on a handful of large national buyers (Aramco, KOC, Qatar Energy,
water authorities) [this document, R265].

Competitive risk to watch: whether the NPC order book and Saudi content advantage convert to
durable share, or whether local and global mills compete the USD 120 M pipeline down on price.
The deck gives no win-rate, bid-pipeline conversion, or market-share figure to judge this
[not disclosed]. Competition read: a real approval moat at NPC, but scale and pricing power
remain the structural gaps versus larger peers.

---

```yaml
stage: A4-analyst
company: "MANINDS"
quarter: "2026-09"
model: claude-opus-4-8
status: complete
docs_merged: [presentation]
ledger_reconciliation:
  notes: 0
  turns: 0
  slides: 37
  all_reviewed: true
  a3_findings_incorporated: [A3-01, A3-02, A3-03, A3-04, A3-05, A3-06]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST"
position_branch: "n/a"
sc_gap_pat_pct: ["FY25 +11.8% (consol above standalone)", "FY26 -12.9% (consol below standalone)", "swing -21.2% of FY26 standalone PAT"]
questions_for_management:
  - {q: "Provide clean-basis EBITDA (ex-other-income) standalone and consolidated FY25/FY26; consol FY26 is 12.3% not 13.0%; reconcile the 15% goal to the clean base", from_finding_id: A3-01}
  - {q: "Consolidated gross margin moved 22.4% to 38.0% on flat income; what cost lines moved COGS-to-opex; restate FY23-FY25 on FY26 definition", from_finding_id: A3-02}
  - {q: "Which subsidiaries turned dilutive (consol PAT 1,705 below standalone 1,958); why did non-standalone revenue fall from 3,872 to 1,087 Mn", from_finding_id: A3-03}
  - {q: "State instrument, share count, issue price and diluted EPS behind the 15.7% paid-up capital rise; no EPS shown despite 'except EPS' headers", from_finding_id: A3-04}
  - {q: "Reconcile the NPC-Aramco relationship dated '2+ decades/since 2005' vs '40+ Years'; confirm the load-bearing durability date", from_finding_id: A3-05}
  - {q: "Provide NPC standalone quarterly P&L through FY27 and pre-NPC vs post-NPC split so the consolidated base stays reconcilable to FY26", from_finding_id: A3-06}
  - {q: "Provide FY26 consolidated cash flow from operations and cash-conversion cycle; inventory +21% and receivables up on flat revenue; is the +23% payables build sustainable", from_finding_id: A3-03}
  - {q: "Why was NPC available at ~2.7x CY2025 PAT with USD 83 M cash on its books; is CY2025 a representative or peak year for NPC's 24.8% EBITDA margin", from_finding_id: A3-06}
monitorables:
  - {item: "Merino Shelters project launch", implied_date: "Mid-Sep 2026", source_ref: "R280/R321"}
  - {item: "Merino cashflow Rs35-50 Cr", implied_date: "FY27", source_ref: "R281"}
  - {item: "NPC first full-quarter earnings contribution", implied_date: "Q2 FY27", source_ref: "R286/R334"}
  - {item: "Q2FY27 consolidated restatement and S-vs-C gap post-NPC", implied_date: "Q2 FY27", source_ref: "A3-06"}
  - {item: "Dammam Coating Plant production", implied_date: "Mar 2027", source_ref: "R273/R300"}
  - {item: "Jammu SS Plant production (Rs250 Cr capex left)", implied_date: "Mar 2027", source_ref: "R274/R277/R318"}
  - {item: "Merino annual cashflow starts", implied_date: "FY28", source_ref: "R278/R320"}
  - {item: "Revenue CAGR 20-25% vs +1.7% FY26 consol", implied_date: "next 5 years", source_ref: "R291"}
  - {item: "EBITDA margin to 15% vs 12.3% clean base", implied_date: "5-year", source_ref: "R292"}
  - {item: "Merino revenue Rs700-800 Cr", implied_date: "next 5-6 years", source_ref: "R279"}
  - {item: "Working-capital direction (inventory/receivables vs revenue)", implied_date: "each result", source_ref: "Step 5 / R183/R199/R201"}
  - {item: "Clean-basis ROCE and ex-OI EBITDA disclosure", implied_date: "each result", source_ref: "R018 / Step 2.4"}
flags:
  - "Consolidated ex-OI EBITDA margin 12.3% below 13% floor; headline 13.0% only via other income reclassified as operational (A3-01)"
  - "Standalone-vs-consolidated PAT gap reversed to -253 Mn (FY26) from +162 Mn (FY25); 21% swing before NPC enters base (A3-03)"
  - "Gross-profit margin 22.4% to 38.0% on flat revenue; likely COGS/opex reclassification; historical baseline not comparable (A3-02)"
  - "Undisclosed equity dilution: paid-up capital +15.7%, no share count or EPS despite 'except EPS' headers (A3-04)"
  - "No cash-flow statement; cash conversion INDETERMINATE; working capital ballooning on flat consol revenue"
  - "NPC purchase multiple ~2.7x CY2025 PAT is valuation-relevant; flagged to downstream chain, not priced here"
  - "Aramco relationship duration internally inconsistent (20 vs 40 years); do not anchor durability claim (A3-05)"
  - "India order-book split not disclosed (named thesis tripwire, ND)"
plain_language_brief_included: true
analyst_note: "Deck advances the transition story while three quality tripwires read adverse. The load-bearing item is margin definition: EBITDA folds in other income, so clean consol FY26 EBITDA is 12.3%, under the 13% floor; the 15% goal is measured off an inflated base. The gross-margin jump (22.4->38.0 on flat revenue) is a reclassification, not a real gain, so the FY25/FY26 baseline breaks. Consolidated PAT fell below standalone (-253 Mn) before NPC consolidates, so the Q2FY27 NPC ramp will bury the pre-NPC subsidiary drag unless decomposed now. NPC looks cheaply bought (~2.7x PAT, USD 83 M cash) but CY2025 representativeness is unverifiable from the deck; flagged to the valuation chain, not priced. Cash conversion INDETERMINATE (no cash-flow statement) with working capital ballooning on flat revenue caps the cash axis at CAVEATS. Verdict PROCEED WITH FLAGS. Decision Status unchanged: WATCHLIST, no trigger fired, CMP Rs714 above the Rs412-589 zone."
review_path: "runs/maninds-corppres-2026-09/work/phase3-dedup/review_maninds_2026-09.md"
```
