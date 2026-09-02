# A4 ANALYST — DOCUMENT REVIEW (single standalone document)
# Man Industries (India) Ltd (MANINDS) | Corporate Presentation dated 01-Sep-2026 | Quarter tag 2026-09
# Protocol: Document Review Protocol v1.0 (loaded alone). Role 4/5, Master, FTTCP, Section 1B, RDE NOT loaded.
# Framing: THESIS CHECK (live Notion thesis exists). Decision Status verified BEFORE any position framing.
# CORRECTION-LOOP iteration 1: fixes A5 findings ARI-1 (clean-margin sign), COV-1 (order-book qualifier),
# COV-2 (guided-accretion bear counter), plus the mandatory NPC purchase-multiple point. All else preserved.

---

## STEP 1 — LEDGER RECONCILIATION PREAMBLE

Ledger contains 37 slides / 335 structured claims (R001-R335) / 10 MISSING_FROM_STRUCTURED units
(MF01-MF10). All reviewed. A2 GATE passes (count test match on slides, numbers, entities, forward,
dates, footnotes; zero_standing re-swept and reconciled to 3 units after adding MF10). A3 ledger
reconciliation 100% (335/335 + MF01-MF10 read at cited lines). No unreviewed row. No source PDF opened.

A3 findings incorporated: A1 (F2), A2 (F6), A3 (F10), A4 (F12), A5 (F14), A6 (F16), A7 (F16).
A2 material misses folded in: MF02 / MF04 (EBITDA "inclusive of Other Income" qualifier on both
standalone R153 and consolidated R165), MF07 / MF09 (Total Income inclusive of Other Income),
MF10 (Greenfield Nil order book, folded into A3 F1). MF01/MF03/MF05/MF06/MF08 are unit disclaimers
(INR Millions) with no analytical effect beyond confirming the reporting unit.

Standing gap carried forward: no prior-quarter deck supplied. DROPPED_SLIDE and cross-deck drop
tests are NOT runnable this run (A2 §1, A3 F15/F16). Slide-set completeness vs last quarter is unverified.

DOCTYPE NOTE: this is a corporate presentation, not a results filing and not a concall. Role 4 PAT
bridge and Role 5 promise-tracker are downstream; this pass FEEDS them. No cash-flow statement is
present, so cash conversion is INDETERMINATE by construction (Step 5). Financials shown are FY26 vs
FY25 full-year (slides 28-31) plus a Q1FY27 quarterly-trend chart (slide 32). The most recent period
is Q1 FY27 (Apr-Jun 2026), which carries only 40 days of NPC (R220, acquired 21-May-2026 per R333).

---

## STEP 2 — EXTRACTION TABLES (every cell a line-anchored number or ND)

### 2.1 Standalone annual P&L (slide 28, INR Mn) — MF02: EBITDA* includes Other Income

| Line | FY26 | FY25 | YoY | Anchor |
|---|---|---|---|---|
| Revenue from Operations | 34,552 | 31,182 | +10.8% | R149 |
| Other Income | 531 | 542 | -2.0% | R150 |
| Total Income | 35,083 | 31,724 | +10.6% | R151 |
| Operating expenses | 30,155 | 28,415 | +6.1% | R152 |
| EBITDA* (incl Other Income, MF02) | 4,928 | 3,309 | +48.9% | R153 |
| EBITDA Margin (on Total Income) | 14.0% | 10.4% | +360bps | R154 |
| Depreciation & amortization | 756 | 433 | +74.6% | R155 |
| Finance costs | 1,542 | 1,022 | +50.9% | R156 |
| PBT | 2,630 | 1,854 | +41.8% | R157 |
| Tax | 672 | 484 | +39.0% | R158 |
| PAT | 1,958 | 1,370 | +42.8% | R159 |
| PAT Margin | 5.6% | 4.3% | +130bps | R160 |

### 2.2 Consolidated annual P&L (slide 29, INR Mn) — MF04: EBITDA* includes Other Income

| Line | FY26 | FY25 | YoY | Anchor |
|---|---|---|---|---|
| Revenue from Operations | 35,639 | 35,054 | +1.7% | R161 |
| Other Income | 286 | 200 | +43.2% | R162 |
| Total Income | 35,925 | 35,253 | +1.9% | R163 |
| Operating expenses | 31,246 | 31,690 | -1.4% | R164 |
| EBITDA* (incl Other Income, MF04) | 4,679 | 3,563 | +31.3% | R165 |
| EBITDA Margin (on Total Income) | 13.0% | 10.1% | +290bps | R166 |
| Depreciation & amortization | 789 | 453 | +74.4% | R167 |
| Finance costs | 1,520 | 1,027 | +48.1% | R168 |
| PBT | 2,370 | 2,084 | +13.7% | R169 |
| Tax | 665 | 552 | +20.4% | R170 |
| PAT | 1,705 | 1,532 | +11.3% | R171 |
| PAT Margin | 4.7% | 4.3% | +40bps | R172 |

### 2.3 Clean EBITDA (ex Other Income) — A4-derived from anchored rows, NOT from the deck

| Basis | Reported EBITDA* | less Other Income | Clean EBITDA | on Rev-from-Ops | Reported margin | Notion 13% floor |
|---|---|---|---|---|---|---|
| Standalone FY26 | 4,928 (R153) | 531 (R150) | 4,397 | 34,552 (R149) = 12.7% | 14.0% (R154) | BELOW 13% floor by 0.3pp (clean) |
| Consolidated FY26 | 4,679 (R165) | 286 (R162) | 4,393 | 35,639 (R161) = 12.3% | 13.0% (R166) | BELOW 13% floor by 0.7pp (clean) |
| Standalone FY25 | 3,309 (R153) | 542 (R150) | 2,767 | 31,182 = 8.9% | 10.4% | — |
| Consolidated FY25 | 3,563 (R165) | 200 (R162) | 3,363 | 35,054 = 9.6% | 10.1% | — |

Read (CORRECTED, ARI-1): on the reported basis the standalone FY26 EBITDA margin is 14.0% and the
consolidated 13.0% (exactly at the Notion tripwire floor). On a CLEAN basis (ex Other Income, per
MF02/MF04) BOTH sides sit BELOW the 13% floor: standalone 12.7% (below by 0.3pp) and consolidated
12.3% (below by 0.7pp). The prior pass mislabelled the standalone clean margin as "above floor by
0.3pp"; the sign is inverted here. 12.7% is 0.3pp UNDER 13.0%, not over. Neither clean margin clears
the floor, and both are far from the 15% five-year target (R222). The Notion tripwire "EBITDA margin
ex-other-income vs 13% floor" is BREACHED on both the standalone and consolidated read. FLAG. Not a
formal auto-fire trigger; the human decides.

### 2.4 Consolidated balance sheet — working-capital and capex lines (slide 30, INR Mn)

| Line | FY24 | FY25 | FY26 | FY26/FY24 | Anchor |
|---|---|---|---|---|---|
| Property, Plant & Equipment | 5,234 | 5,539 | 6,546 | 1.25x | R189 |
| Right-of-use Assets | 163 | 186 | 1,389 | 8.52x | R190 |
| Capital WIP | 305 | 1,334 | 3,258 | 10.68x | R191 |
| Goodwill on Consolidation | 639 | 688 | 688 | 1.08x | R192 |
| Intangible assets | - (ZERO) | 5 | 3 | ND FY24 | R194 |
| Inventories | 6,456 | 12,685 | 15,350 | 2.38x | R199 |
| Trade Receivables (current) | 3,551 | 8,959 | 10,098 | 2.84x | R201 |
| Trade Receivables (non-current) | 967 | 973 | 2,385 | 2.47x | R195 |
| Cash & Bank Balances | 2,549 | 3,792 | 6,572 | 2.58x | R202 |
| Investments | 2,280 | 260 | 708 | 0.31x | R200 |
| Trade payables | 5,028 | 12,002 | 14,712 | 2.93x | R183 |
| Other financial liabilities | 278 | 301 | 5,797 | 20.85x | R185 |
| Current Tax Assets | - | - | - | ZERO all yrs | R206 |
| Long-term Borrowings | 1,363 | 1,385 | 2,402 | 1.76x | R176 |
| Short-term Borrowings | 1,722 | 3,175 | 2,595 | 1.51x | R181 |
| Lease Liabilities (non-current) | 141 | 156 | 610 | 4.33x | R177 |
| Lease Liabilities (current) | 34 | 47 | 674 | 19.82x | R182 |
| Shareholders Fund | 14,049 | 16,073 | 20,865 | 1.49x | R175 |
| Total Assets | 24,152 | 37,792 | 50,206 | 2.08x | R188 |

### 2.5 Equity structure (slide 30) — A3 F10 dilution

| Line | FY24 | FY25 | FY26 | Anchor |
|---|---|---|---|---|
| Equity Share Capital | 324 | 324 | 375 | R173 |
| Other Equity | 13,725 | 15,749 | 20,490 | R174 |

Read: paid-up capital +15.7% in FY26 (324->375, ~10M new shares at Rs5 face). Other Equity +4,741
(15,749->20,490) exceeds retained PAT ~1,705 (R171), so ~3,036 is share premium: a premium raise,
likely NPC / capex funding. Deck discloses NO basic-vs-diluted EPS split. Dilution flag; cross-check
the Notion warrant / dilution register downstream (out of scope here).

### 2.6 Headline metrics (slide 4, page-4 card)

| Metric | FY22 | FY26 | CAGR | Anchor |
|---|---|---|---|---|
| Revenue (INR Cr) | 2,178 | 3,592 | 13.4% | R005/R006/R007 |
| EBITDA (INR Cr) | 218 | 468 | 21.0% | R010/R011/R012 |
| PAT (INR Cr) | 102 | 171 | 13.8% | R015/R016/R017 |
| ROCE FY26 | — | 18.4% | — | R018 |
| ROE FY26 | — | 9.2% | — | R019 |
| Networth FY26 | — | 2,087 Cr | — | R020 |
| Capacity | — | 1.6Mn+ MTPA* | — | R004 (incl NPC 0.43Mn, R021) |

Note on ROCE 18.4% (R018): the numerator EBIT rides the same "inclusive of Other Income" EBITDA
(MF02/MF04). A3 A6 flags ROCE as likely inflated on a clean basis. The Notion tripwire "ROCE on a
clean basis vs headline" cannot be resolved from this deck: no clean-EBIT or capital-employed
breakdown is disclosed. ND on clean ROCE; FLAG for the downstream Section 1B clean-basis test.

### 2.7 Historical consolidated trend (slide 31, INR Mn) — MF07: Total Income incl Other Income

| Line | FY23 | FY24 | FY25 | FY26 | Anchor |
|---|---|---|---|---|---|
| Total Income* | 22,703 | 31,942 | 35,253 | 35,925 | R209 |
| Gross Profit | 4,973 | 7,907 | 7,905 | 13,639 | R210 |
| Gross Profit Margin | 21.9% | 24.8% | 22.4% | 38.0% | R211 |
| EBITDA | 1,760 | 2,932 | 3,563 | 4,679 | R212 |
| EBITDA Margin | 7.8% | 9.2% | 10.1% | 13.0% | R213 |
| PAT | 670 | 1,051 | 1,532 | 1,705 | R214 |
| PAT Margin | 3.0% | 3.3% | 4.3% | 4.7% | R215 |

Anomaly: Gross Profit jumps +72.5% (7,905->13,639) and GP margin from 22.4% to 38.0% in FY26, while
Total Income is roughly flat (+1.9%). A step-change of 15.6pp in gross margin with flat revenue is not
explained by the deck. Candidate cause: a cost reclassification between "cost of materials" and
"operating expenses" (consistent with the +290bps reported EBITDA margin gain), not a real pricing
gain. A7 flags related chart-data opacity. QfM raised.

### 2.8 Quarterly consolidated trend (slide 32, INR Mn) — per-quarter mapping UNRESOLVABLE (A1 caveat, A7)

| Metric | five bar values (order Q1FY26 -> Q1FY27 as printed) | margins | Anchor |
|---|---|---|---|
| Total Income | 7,736 / 8,148 / 8,386 / 11,655 / 10,650 | — | R216 |
| Gross Profit | 6,269 / 3,820 / 3,409 / 1,833 / 2,128 | 53.8% / 40.6% / 35.9% / 23.7% / 26.1% | R217 |
| EBITDA | 806 / 1,018 / 1,376 / 1,480 / 1,553 | 10.4% / 12.5% / 16.4% / 12.7% / 14.6% | R218 |
| PAT | 276 / 370 / 550 / 509 / 614 | 3.6% / 4.5% / 6.6% / 4.4% / 5.8% | R219 |

Do NOT rely on per-quarter GP bars (R217): the implied 53.8% single-quarter GP margin is
irreconcilable with the FY26 annual GP margin 38.0% (R211) and with Total-Income ordering. A1 flagged
the flattened-layout mapping unresolvable; A3 A7 confirms. Total Income and EBITDA/PAT bars are
usable directionally only. Q1FY27 Total Income 10,650 is +37.7% vs Q1FY26 7,736, the first period with
NPC (40 days, R220).

### 2.9 NPC (National Pipe Company, KSA) CY2025 standalone (slide 26) — the acquisition target

| Line | SAR M | USD M | INR (disclosed / derived) | Margin | Anchor |
|---|---|---|---|---|---|
| Revenue | 792.7 | 211.4 | ~1,898.9 Cr | — | R120/R147 |
| Gross Profit | 214.1 | 57.1 | ND | 27.0% | R121/R122 |
| EBITDA | 196.7 | 52.5 | ND | 24.8% | R123/R124 |
| EBIT | 164.9 | 44.0 | ND | 20.8% | R126/R127 |
| PBT | 162.0 | 43.2 | ND | 20.4% | R130/R131 |
| Tax & Zakat | 18.5 | 4.9 | ND | 11.4% rate | R132/R133 |
| PAT | 143.5 | 38.3 | ~343.6 Cr | 18.1% | R134/R135/R148 |
| ROE / ROCE / ROA | — | — | — | 25.7% / 29.5% / 22.5% | R141/R142/R143 |
| Cash & liquid assets (Apr'26) | 311.3 | 83.0 | ND | — | R139 |
| Net worth (Apr'26) | 594.9 | 158.6 | ND | — | R140 |
| Consideration | — | 102.0 | ~1,000 Cr | — | R091/R041 |
| Order book at acquisition (incl executed to date) | — | 120.0 | 1,130-1,150 Cr | — | R144 |
| Acquire-route EBITDA / PAT margin guidance | — | — | — | 15-18% / 11-14% | R115/R116 |
| Financing | — | 70 debt + 32 equity | — | — | R092/R093 |

FX disclosed: SAR/INR 23.955, SAR/USD 3.75 pegged (R145/R146).

ORDER-BOOK QUALIFIER (CORRECTED, COV-1): the USD 120 Mn order book is stated in the source as "an
order position of USD 120 Million (INR 1,130-1,150 crore) (including executed to date), with L1 status
secured in certain additional orders" (fulltext L729-731, anchors R144). The "(including executed to
date)" clause is load-bearing and was dropped in the prior pass. It means the USD 120 Mn is NOT a pure
forward backlog: it INCLUDES orders already executed. The genuine forward book that lands in group
revenue from Q2 FY27 is SMALLER than the "immediate US$120 Mn order book" framing on slide 25 (R119/
R285). Do not read USD 120 Mn as clean forward backlog. QfM raised.

GUIDED-ACCRETION BEAR COUNTER (CORRECTED, COV-2): the deck's OWN Acquire-route accretion guidance is
15-18% EBITDA margin and 11-14% PAT margin (R115/R116, fulltext L643, page-24 "Earnings Accretive"
row). That guided range is MATERIALLY BELOW NPC's CY2025 trailing print of 24.8% EBITDA (R124) and
18.1% PAT (R135). The re-rating case must be underwritten on the 15-18% EBITDA / 11-14% PAT GUIDED
range, not the 24.8% / 18.1% peak print. The deck itself signals that CY2025 may be a cycle peak: if
management expected the trailing margins to hold, it would not guide accretion 700-900bps lower. On
the guided EBITDA range (15-18%) NPC still lifts the group's clean 12.3% mix, but by far less than the
24.8% print implies, and the PAT-margin guide (11-14%) is only ~2-3x the parent's thin 4.7% consol
PAT margin, not the ~4x the peak print suggests. Underwrite the guide. FLAG.

NPC PURCHASE MULTIPLE (mandatory acquisition-economics point):
- Consideration USD 102 Mn / ~Rs 1,000 Cr (R091/R041), financed USD 70 Mn debt + USD 32 Mn equity
  (R092/R093).
- Against NPC CY2025 PAT of USD 38.3 Mn / SAR 143.5 Mn / ~Rs 343.6 Cr (R134/R135/R148), the GROSS
  purchase multiple is USD 102 / 38.3 = ~2.7x earnings (INR basis Rs 1,000 Cr / Rs 343.6 Cr = ~2.9x,
  round ~3x). On EBITDA USD 52.5 Mn (R123) the multiple is 102 / 52.5 = ~1.9x.
- The deck states the money ALSO buys USD 83 Mn of cash & liquid assets (fulltext L633-635, R113/R118)
  and a zero-debt balance sheet at closing (R284). Net of that acquired cash the effective outlay is
  ~USD 102 - 83 = ~19 Mn for a business earning USD 38.3 Mn PAT: a cash-adjusted ~0.5x earnings.
- This is a 29.5% ROCE (R142), zero-debt (R284), USD 83 Mn cash (R139), 40-year Saudi-Aramco-tenured
  asset (R110/R264) bought at ~2.7x gross / ~0.5x net earnings. A price that low on numbers that good
  is itself the question: WHY is a debt-free, 29.5%-ROCE, Aramco-approved asset available at ~3x
  earnings, and is CY2025 a representative year or a cycle PEAK the seller is cashing out of? The
  deck's own 15-18% EBITDA / 11-14% PAT accretion guide (below the CY2025 print) is a partial answer:
  management itself is not underwriting the trailing margins forward. QfM raised.

NPC EBITDA margin 24.8% (CY2025 print) and ROCE 29.5% are roughly double the parent's clean 12.3% /
headline 18.4%, but the deck's forward accretion guide (15-18% EBITDA) is the number to carry, not the
print. NPC is the entire re-rating case and it consolidates only from Q2 FY27 (R286/R334). Every
full-year FY26 number in 2.1-2.7 is the OLD business.

---

## STEP 3 — YoY / QoQ WALKS and PAT BRIDGE

No prior full presentation and no per-quarter results filing are in scope, so a formal Role 4 PAT
bridge (volume / price / mix / cost / other) cannot be built. The deck gives full-year YoY only. The
PAT walk below is descriptive, from anchored rows.

### 3.1 Consolidated PAT walk FY25 -> FY26 (INR Mn)

| Step | Delta | Note | Anchor |
|---|---|---|---|
| PAT FY25 | 1,532 | base | R171 |
| + Revenue-from-Ops growth (+585, +1.7%) | small | flat top line | R161 |
| + Gross margin / opex mix (opex -1.4% on +1.7% rev) | positive | drives EBITDA +1,116 | R164/R165 |
| + Other Income (+86) | small | 200 -> 286 | R162 |
| - Depreciation (+336 higher) | negative | +74.4%, new assets on-lining | R167 |
| - Finance costs (+493 higher) | negative | +48.1%, borrowings + leases up | R168 |
| = PBT FY26 | 2,370 | +13.7% | R169 |
| - Tax (+113) | — | 20.4% | R170 |
| = PAT FY26 | 1,705 | +11.3% | R171 |

The consolidated EBITDA gain (+31.3%) is largely eaten by depreciation (+74.4%) and finance cost
(+48.1%), so PAT grows only +11.3%. Standalone PAT grows +42.8% because standalone revenue grew +10.8%
(vs consolidated +1.7%) and standalone carries less of the depreciation/finance drag proportionally.
The gap between the two is Step 4.

### 3.2 Q1FY27 QoQ / YoY

Only Total Income is reliably mappable (2.8). Q1FY27 Total Income 10,650 vs Q4FY26 11,655 = -8.6% QoQ;
vs Q1FY26 7,736 = +37.7% YoY (first NPC period, 40 days, R220). EBITDA/PAT per-quarter bars are
directional only; GP bars unusable (A7). No PAT bridge for the quarter is possible from a chart.

---

## STEP 4 — STANDALONE-vs-CONSOLIDATED GAP (first-class metric, A3 F2 / finding A1)

| Period | Standalone PAT | Consolidated PAT | Consol - SA (subsidiary net) | as % of SA PAT | Anchor |
|---|---|---|---|---|---|
| FY25 | 1,370 | 1,532 | +162 (subs profitable) | +11.8% | R159/R171 |
| FY26 | 1,958 | 1,705 | -253 (subs net loss) | -12.9% | R159/R171 |
| Swing FY25->FY26 | — | — | -415 | -21.2% of FY26 SA PAT | derived |

Decomposition available from the deck:
- Revenue: standalone +10.8% (R149) vs consolidated +1.7% (R161). The subsidiaries' revenue SHRANK
  in aggregate: consol rev-from-ops 35,639 minus standalone 34,552 = 1,087 subsidiary revenue in FY26,
  vs 35,054 - 31,182 = 3,872 in FY25. Subsidiary revenue fell ~72% YoY (3,872 -> 1,087).
- PAT: subsidiaries swung from +162 to -253, a -415 flip, 4.2x the 5pp materiality gate on SA PAT.
- This is PRE-NPC. NPC consolidates only from Q2 FY27 (R286/R334); it is not in any FY26 figure. The
  loss-making, shrinking subsidiaries are the EXISTING non-NPC subs (Merino Shelters, MISIC pre-NPC,
  overseas entities). The deck names no per-subsidiary P&L, so the identity of the loss maker is ND.

The Notion tripwire "consolidated vs standalone PAT divergence" is TOUCHED and moving the wrong way:
subs went from additive to dilutive. FLAG. QfM raised (which subsidiaries, what drove the loss).

---

## STEP 5 — CASH-QUALITY NOTE (INDETERMINATE, caps verdict at PROCEED WITH CAVEATS)

The presentation carries NO cash-flow statement. Operating cash flow, capex outflow, and free cash
flow are all absent. Cash conversion is therefore INDETERMINATE and MUST NOT resolve silently to
PROCEED (house rule). Missing evidence named:
- No CFO, no OCF/EBITDA ratio, no working-capital cash impact.
- The balance sheet (2.4) shows working capital ballooning FASTER than revenue: inventories 2.38x,
  current receivables 2.84x, payables 2.93x over FY24->FY26 while consolidated revenue is flat (+1.7%).
  Rising WC intensity on flat revenue is a negative cash-conversion signal, but without a CFO statement
  it cannot be quantified. Cash & Bank did rise (2,549 -> 6,572, R202), but that coincides with the
  equity raise (2.5) and higher borrowings (R176/R181), so the cash build is financed, not operating-proven.
- The "Other financial liabilities" line jumped 301 -> 5,797 at FY26 close (R185), a +5,496 spike,
  candidate NPC-consideration payable. If debt-like, it materially changes the net-cash reading.

Net cash / net debt (Notion tripwire): borrowings only = LT 2,402 (R176) + ST 2,595 (R181) = 4,997;
cash & bank 6,572 (R202) -> net CASH ~1,575. But add lease liabilities 610 + 674 = 1,284 (R177/R182)
and the 5,797 other-financial-liability (R185, likely acquisition payable) and the position flips to
net DEBT. The deck's "net cash" impression rests on excluding the 5,797 item. ND on true net position
until the 5,797 is identified. FLAG.

CASH CONVERSION VERDICT: INDETERMINATE. Missing evidence: full cash-flow statement, identity of the
5,797 other-financial-liability, per-subsidiary cash generation.

---

## STEP 6 — THESIS / DECISION-STATUS RECONCILIATION

DECISION STATUS VERIFIED (Notion, passed inline): **WATCHLIST.** CMP Rs714. Entry zone Rs412-589. MoS
Rs412. Position size Small. No pre-committed trigger fired to date.

Framing rule honoured: this is a WATCHLIST name, not held. No HOLD/ADD/TRIM/EXIT framing applies. The
document is read as a thesis check against the watch tripwires. No pre-committed trigger formally fires
on this deck; nothing here moves the Decision Status. Flags below are for the human, per house rule.

Tripwire-by-tripwire reconciliation:

| Notion tripwire | This deck's read | Status |
|---|---|---|
| Consolidated vs standalone PAT divergence | Subs flipped +162 -> -253, -21% of SA PAT (Step 4) | TOUCHED, adverse |
| EBITDA margin ex-other-income vs 13% floor | Clean standalone 12.7% AND consolidated 12.3%, BOTH below floor (2.3) | BREACHED, adverse |
| ROCE on clean basis vs headline | Headline 18.4%; clean ND (rides incl-OI EBIT) | UNRESOLVED, flag |
| Net-debt vs net-cash reading | Net cash only if 5,797 excluded (Step 5) | UNRESOLVED, flag |
| NPC acquisition economics & integration | Bought ~2.7x gross / ~0.5x net PAT; but ACCRETION GUIDED 15-18% EBITDA / 11-14% PAT (R115/R116), below the 24.8%/18.1% print; order book USD 120 Mn incl executed-to-date; consolidates Q2FY27 | MIXED, unproven; underwrite the guide not the peak |
| Jammu / Dammam commissioning by Mar 2027 | Both "Production Targeted Mar'2027" (R273/R274) | ON TRACK, dated |
| India order book split | Not disclosed in this deck | ND, not addressed |
| Working-capital direction | Inv 2.38x, recv 2.84x on flat revenue (2.4) | TOUCHED, adverse |

Thesis read: the deck confirms the transition ARCHITECTURE (NPC bought, Jammu SS and Dammam coating
for higher-margin mix, 20-25% revenue and 15% EBITDA targets) but the FY26 numbers are the old,
margin-thin, WC-heavy business, and the margin tripwire is now BREACHED on both standalone and
consolidated clean bases. The re-rating case (NPC) is real but must be underwritten on the deck's OWN
guided accretion (15-18% EBITDA / 11-14% PAT), NOT the 24.8% / 18.1% CY2025 peak print; and the USD
120 Mn order book includes executed-to-date, so the true forward backlog is smaller. NPC appears in
group numbers only from Q2 FY27. Entry discipline holds: CMP Rs714 is above the Rs412-589 entry zone;
nothing here argues to buy above the zone.

---

## STEP 7 — FORWARD-TARGET REGISTER (dated management commitments, from A3 F6 + A1 FORWARD rows)

| # | Commitment | Implied date | Status word | Anchor |
|---|---|---|---|---|
| 1 | Dammam Coating Plant (KSA) production | Mar 2027 | targeted / underway | R273/R300 |
| 2 | Jammu SS seamless plant production (Rs350Cr of Rs600Cr spent) | Mar 2027 | underway | R274/R277/R318/R079/R080 |
| 3 | NPC full earnings contribution to consolidated | Q2 FY27 | underway (100% acquired 21-May-2026) | R286/R334/R333 |
| 4 | Merino Shelters project launch | Mid-Sep 2026 (~2 wks post-deck) | on track / imminent | R280/R321 |
| 5 | Merino Shelters cashflow Rs35-50 Cr | FY27 | expected | R281 |
| 6 | Merino Shelters annual cashflow Rs80-120 Cr | from FY28 | planned | R278/R320/R084 |
| 7 | Merino Shelters revenue Rs700-800 Cr | next 5-6 yrs | projected | R279 |
| 8 | NPC HSAW OD upgrade 88" -> 120" | no date | will be upgraded | R107 |
| 9 | NPC value-added coating-mill expansion (post-acq) | no date | planned | slide 21 (R290) |
| 10 | Group Revenue CAGR 20-25% | next 5 yrs | target | R221/R291 |
| 11 | Group EBITDA margin to 15% stable | next 5 yrs | target | R222/R292 |
| 12 | NPC Acquire-route accretion 15-18% EBITDA / 11-14% PAT | on consolidation (Q2 FY27+) | guided | R115/R116 |

---

## STEP 8 — QUESTIONS FOR MANAGEMENT
(EVERY A3 FORWARD-SIGNAL and AMBIGUOUS finding produces at least one row.)

| # | Question | From finding |
|---|---|---|
| Q1 | Which subsidiaries drove the FY26 consolidated PAT (1,705) falling BELOW standalone PAT (1,958), a -253 subsidiary net loss vs +162 profit in FY25? What caused subsidiary revenue to fall ~72% (3,872 -> 1,087)? | A1 (F2, FORWARD-SIGNAL) |
| Q2 | Both Jammu SS and Dammam coating are "Production Targeted Mar 2027". Are both on the Mar-2027 timeline, and what is the Rs250Cr of remaining Jammu capex (Rs600Cr planned less Rs350Cr spent) phasing? | A2 (F6, FORWARD-SIGNAL) |
| Q3 | From what quarter does full NPC earnings contribution land, and what FY27 group revenue/EBITDA-margin uplift should we underwrite on the deck's OWN Acquire-route guide of 15-18% EBITDA / 11-14% PAT (R115/R116), not the 24.8%/18.1% CY2025 print? | A2 (F6, FORWARD-SIGNAL) |
| Q4 | Headline EBITDA (standalone 14.0%, consolidated 13.0%) is "inclusive of Other Income". On a clean, ex-Other-Income basis BOTH FY26 margins are below 13% (standalone 12.7%, consolidated 12.3%). What is the clean-margin path to the stated 15% target, and does headline ROCE 18.4% hold on a clean-EBIT basis? | A6 (F16, FORWARD-SIGNAL) |
| Q5 | Capital WIP rose 10.7x (305 -> 3,258) and working capital ballooned (inventories 2.4x, current receivables 2.8x, payables 2.9x) while consolidated revenue was flat (+1.7%). What is the FY27 working-capital direction and the peak capex still to be funded? | A4 (F12, AMBIGUOUS) |
| Q6 | "Other financial liabilities" jumped from 301 to 5,797 at FY26 close, pre-NPC consolidation. What is this Rs5,797 Mn item, and is it the NPC-consideration payable (i.e. debt-like)? It determines whether the group is net cash or net debt. | A4 (F12, AMBIGUOUS) |
| Q7 | The Saudi Aramco relationship is stated three ways: "2+ decades", "since 2005", and "40+ years". What is the actual approved-vendor tenure? It underwrites the buy-vs-greenfield moat claim. | A5 (F14, AMBIGUOUS) |
| Q8 | The Q1FY27 quarterly Gross-Profit chart implies a 53.8% single-quarter GP margin, irreconcilable with the FY26 annual GP margin of 38.0%. Can management republish the per-quarter GP figures with a clear period mapping? | A7 (F16, AMBIGUOUS) |
| Q9 | Consolidated Gross-Profit margin stepped from 22.4% (FY25) to 38.0% (FY26) on flat revenue. Is this a cost reclassification (materials vs opex) or a genuine mix/pricing gain? | A7 (F16, AMBIGUOUS) |
| Q10 | Paid-up capital rose 15.7% in FY26 (324 -> 375) with Other Equity up 4,741, exceeding retained PAT. What was the equity issuance (size, price, purpose), and what is the diluted share count and diluted EPS? | A3 (F10, NEUTRAL-FACT; dilution not left unprocessed) |
| Q11 | NPC was bought for USD 102 Mn / ~Rs 1,000 Cr, ~2.7x CY2025 PAT (~0.5x net of the USD 83 Mn cash it carries), for a 29.5%-ROCE, zero-debt, 40-year-Aramco asset. Why was a business this good available this cheap, and is CY2025 a representative year or a cycle PEAK? | A2 (F6, FORWARD-SIGNAL) / mandatory acq-economics |
| Q12 | The USD 120 Mn order book is stated "(including executed to date)". What is the actual FORWARD backlog (net of executed) that converts to revenue from Q2 FY27, and what is the bid-pipeline / L1 conversion behind it? | A2 (F6, FORWARD-SIGNAL) / COV-1 |

---

## STEP 9 — MONITORABLES / CATALYST LIST (seeded by A3 commitment register F6)

| Monitorable | Implied date | Source ref | Watch for |
|---|---|---|---|
| Merino Shelters project launch | Mid-Sep 2026 | R280/R321 | launch confirmation ~2 weeks after this deck |
| Merino Shelters FY27 cashflow Rs35-50 Cr | FY27 | R281 | first real-estate cash into P&L |
| NPC full earnings contribution (first clean quarter) | Q2 FY27 | R286/R334 | group EBITDA-margin lift; test vs GUIDED 15-18% EBITDA (R115) not the 24.8% print |
| NPC forward order book (net of executed-to-date) | Q2 FY27 onward | R144/R119 | true backlog conversion vs the USD 120 Mn incl-executed headline |
| Q1 FY27 detailed results (40-day NPC) | already reported in deck | R220/R333 | reconcile the 10,650 Total Income base |
| Merino Shelters annual cashflow Rs80-120 Cr | from FY28 | R278/R320/R084 | recurring real-estate cash |
| Jammu SS seamless plant production | Mar 2027 | R274/R277/R318 | commissioning + higher-margin SS mix |
| Dammam Coating Plant (KSA) production | Mar 2027 | R273/R300 | value-added coating layer live |
| NPC HSAW OD upgrade to 120" | no date | R107 | capacity/mix upgrade completion |
| NPC value-added coating-mill expansion | no date | slide 21 (R290) | KSA value-added capacity |
| Group Revenue CAGR 20-25% | 5 yrs (to ~FY31) | R221/R291 | annual delivery vs target |
| Group EBITDA margin to 15% stable | 5 yrs | R222/R292 | clean-margin trajectory vs 12.3% now |
| Rs5,797 Mn other-financial-liability resolution | next filing | R185 | net-cash vs net-debt clarity |
| Working-capital direction | next filing | R199/R201/R183 | reversal of the FY24->FY26 build |

---

## VERDICT (Document Review verdict set)

**PROCEED WITH FLAGS**, capped by INDETERMINATE cash conversion (Step 5). No STOP; company quality
never halts. Decision Status stays WATCHLIST; no pre-committed trigger formally fired.

Flags to the human (all sourced above):
1. Clean EBITDA margin breaches the Notion 13% floor on BOTH bases: standalone 12.7% (below by 0.3pp)
   and consolidated 12.3% (below by 0.7pp) (Step 2.3, corrected).
2. Subsidiaries flipped from +162 to -253 PAT, -21% of standalone PAT, and subsidiary revenue fell
   ~72% (Step 4). This is the pre-NPC old business.
3. Working capital and CWIP ballooned on flat consolidated revenue; cash conversion INDETERMINATE
   (no cash-flow statement) (Step 5).
4. Rs5,797 Mn other-financial-liability unidentified; net-cash vs net-debt read unresolved (Step 5).
5. Equity dilution +15.7% with no diluted-EPS disclosure (Step 2.5).
6. Gross-margin step 22.4% -> 38.0% on flat revenue unexplained; quarterly GP chart unusable (2.7/2.8).
7. Headline ROCE 18.4% likely rides incl-Other-Income EBIT; clean ROCE ND.
8. NPC re-rating must be underwritten on the deck's OWN guided accretion (15-18% EBITDA / 11-14% PAT,
   R115/R116), which is 700-900bps below the 24.8% / 18.1% CY2025 print the case has leaned on (2.9).
9. The USD 120 Mn NPC order book is "(including executed to date)" (R144, L730); the true forward
   backlog is smaller than the "immediate order book" framing (2.9).
10. NPC bought at ~2.7x gross / ~0.5x net-of-cash CY2025 PAT for a 29.5%-ROCE, zero-debt asset: a
    price that low is itself a question on whether CY2025 is a peak (2.9).
11. No prior-quarter deck: DROPPED_SLIDE / cross-deck drop test not runnable.

Valuation-relevant facts FLAGGED for the downstream chain (NOT computed here, out of scope): the
Section 1B destination PE, the exit multiple, FV CAGR / Amendment 19 entry-zone work, FTTCP verdict,
and Role 1 valuation. Load-bearing downstream input: NPC's GUIDED 15-18% EBITDA / 11-14% PAT accretion
(not the 24.8% / 18.1% print) vs the parent's clean 12.3% / 18.4%, whether the blended clean group
margin actually reaches 15%, and whether the ~2.7x purchase multiple signals a peak-cycle print.

---

## PLAIN-LANGUAGE BRIEF (mandatory; final narrative section)

### 1. SUMMARY NARRATIVE

Man Industries makes large-diameter line pipe (LSAW, HSAW, ERW) and pipe coating. This is a corporate
presentation dated 01-Sep-2026, not a results filing. The name sits on WATCHLIST at CMP Rs714, above
the Rs412-589 entry zone. Nothing in the deck fires a trigger, so it stays on watch.

The full-year FY26 numbers are the OLD business, before the Saudi acquisition consolidates. They are
mixed. Standalone revenue grew 10.8% and standalone profit grew 42.8%. But CONSOLIDATED revenue was
flat, up only 1.7%, and consolidated profit grew just 11.3% (Rs1,705 Mn, all figures from filings).
The subsidiaries lost money: consolidated profit fell BELOW standalone profit by Rs253 Mn, a swing of
Rs415 Mn from a Rs162 Mn profit the year before. Subsidiary revenue fell about 72%.

The headline EBITDA margins include Other Income. Strip it out and BOTH clean margins fall below the
13% level the thesis watches: standalone 12.7% and consolidated 12.3%. Neither clears the floor, and
both are far from the 15% target. Working capital grew far faster than sales: inventories 2.4x,
receivables 2.8x over two years on flat revenue. Capital work-in-progress rose almost 11x for the
Jammu and Dammam plants, which earn nothing yet. The deck carries no cash-flow statement, so cash
quality cannot be proven. One balance-sheet line, "other financial liabilities", jumped from Rs301 Mn
to Rs5,797 Mn; if that is the acquisition payable, the company is net debt, not net cash. The company
also raised equity (paid-up capital up 15.7%) and did not disclose diluted EPS.

The whole re-rating case is the Saudi target, National Pipe Company. Its CY2025 print is strong: 24.8%
EBITDA margin, 29.5% ROCE. But the deck's OWN forward accretion guide is lower, 15-18% EBITDA and
11-14% PAT, so we underwrite the guide, not the peak print. The USD 120 Mn order book is stated
"(including executed to date)", so the real forward backlog is smaller than the "immediate order book"
framing. NPC was bought for USD 102 Mn / ~Rs 1,000 Cr, about 2.7x its CY2025 profit, and only ~0.5x
after the USD 83 Mn of cash it carries. A debt-free, 29.5%-ROCE, 40-year-Aramco asset at that price is
almost too cheap: the question is whether CY2025 is a peak year. NPC consolidates only from Q2 FY27;
the June-2026 quarter carried just 40 days of it. So the good business is not yet in the group numbers,
and the group numbers today are thin-margin and working-capital heavy. Verdict: PROCEED WITH FLAGS,
capped by indeterminate cash conversion. Stay on watch, below the entry zone.

Provenance: CMP, entry zone, tripwires from prior Notion work. All financials from THIS deck (slides
26-32). Clean margins, purchase multiple, net-debt reading, and subsidiary decomposition are
A4-derived from anchored rows.

### 2. SECTOR INTELLIGENCE

Line pipe is a project-driven, order-book business tied to oil, gas, and water infrastructure capex.
Demand is lumpy and tender-led; revenue can be flat for a year then jump on a large award (the FY26
flat consolidated top line, R161, fits this). The structural pull the company leans on is Gulf and
water-pipeline spend: Saudi Aramco, KOC, Qatar, and Saudi water authorities appear as clients
(R264/R265, prior Notion peer context). The Saudi acquisition buys a local, Aramco-approved producer
inside that spend pool, which shortens the approval cycle the deck contrasts with a 1-2 year greenfield
audit (R283). Input cost is steel; the business is a spread and conversion play, so steel-price swings
move margins. Because margins ride the steel spread, a single strong CY2025 print at NPC (24.8% EBITDA)
may reflect a favourable cycle, which is why the deck's forward guide sits lower at 15-18% (R115).
Regulation and payer mix are not consumer-style factors here; the "payer" is national oil companies
and utilities, and the risk is tender timing and receivable cycles, both visible in the 2.8x receivable
build (R201). Metric the deck did NOT disclose: India order-book split and book-to-bill.

### 3. BUSINESS-MODEL INTELLIGENCE

The company converts steel coil and plate into welded pipe, then adds coating. It earns a conversion
spread, not brand pricing. On the quality ladder that is a cost-advantaged converter to value-added
supplier, roughly R2-R3, with a stated CLIMB toward higher-margin stainless-steel seamless pipe
(Jammu, R276) and value-added coating (Dammam, R275). Both FY26 clean EBITDA margins (standalone
12.7%, consolidated 12.3%, A4-derived from R153/R150/R149 and R165/R162/R161) are consistent with a
converter, not a franchise. The transition thesis rests on three mix shifts: buy the higher-margin
Saudi plant (NPC, guided to add at 15-18% EBITDA / 11-14% PAT per R115/R116, above the group's 12.3%
but below NPC's own 24.8% print), add stainless seamless (Jammu, targeted Mar 2027, R274), and add
coating (Dammam, targeted Mar 2027, R273). This quarter's model drift signal is adverse on the base
business: working capital rose faster than revenue and the non-NPC subsidiaries turned loss-making
(Step 4). The model only re-rates if NPC's GUIDED economics survive consolidation AND the clean group
margin actually climbs to 15% (R222). Metric NOT disclosed: per-subsidiary and per-product-line P&L,
so the mix shift cannot yet be verified in the numbers.

### 4. COMPETITION INTELLIGENCE

Where the company wins: Aramco-approved vendor status held (the deck says since 2005, R324; tenure is
a QfM, A5), 80-inch export capability (R034), and a rare Indian footprint inside Saudi via NPC. That
approval is a real switching barrier in Gulf tenders and is the load-bearing moat claim. NPC came
cheap (~2.7x CY2025 PAT, ~0.5x net of its USD 83 Mn cash, R091/R134/R139), a zero-debt, 29.5%-ROCE
asset, which is either a strategic bargain or a signal the seller sold at a cycle peak. Where the group
is structurally weaker: it is a price-taking converter exposed to steel input costs, with a lumpy order
book and heavy working capital, and it competes against larger global pipe makers (Welspun, Jindal
SAW, and international mills) on price and delivery in the same tenders (peer set from prior Notion
work, not named in this deck). The competitive risk to watch: if the Saudi and water-pipeline capex
cycle slows, or if steel spreads compress, the thin ~12.5% clean margin has little cushion, and the
receivable and inventory build (R201/R199) becomes a cash trap. The NPC acquisition is the edge; if
its economics land at the guided 15-18% EBITDA rather than the 24.8% print, and if the forward book
net of executed-to-date is small, the competitive case reverts to a margin-thin converter. Metric NOT
disclosed: market share and win-rate vs named peers.

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
  a3_findings_incorporated: ["A1", "A2", "A3", "A4", "A5", "A6", "A7"]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST"
position_branch: "n/a"
sc_gap_pat_pct:
  - {period: "FY26", standalone_pat: 1958, consolidated_pat: 1705, gap_pct: -12.9}
  - {period: "FY25", standalone_pat: 1370, consolidated_pat: 1532, gap_pct: 11.8}
  - {period: "swing_FY25_to_FY26", subsidiary_pat_flip: -415, pct_of_fy26_sa_pat: -21.2}
questions_for_management:
  - {q: "Which subsidiaries drove FY26 consol PAT (1,705) below standalone (1,958), a -253 subsidiary net loss vs +162 in FY25; why did subsidiary revenue fall ~72%?", from_finding_id: "A1"}
  - {q: "Are Jammu SS and Dammam coating both on the Mar-2027 timeline, and what is the phasing of the remaining ~Rs250Cr Jammu capex?", from_finding_id: "A2"}
  - {q: "From which quarter does full NPC earnings land, and what FY27 group revenue/EBITDA-margin uplift should be underwritten on the deck's OWN guide of 15-18% EBITDA / 11-14% PAT (R115/R116), not the 24.8%/18.1% CY2025 print?", from_finding_id: "A2"}
  - {q: "Headline EBITDA includes Other Income; BOTH clean FY26 margins are below 13% (standalone 12.7%, consolidated 12.3%). What is the clean-margin path to 15%, and does ROCE 18.4% hold on a clean-EBIT basis?", from_finding_id: "A6"}
  - {q: "CWIP rose 10.7x and working capital ballooned on flat revenue; what is FY27 WC direction and the peak capex still to fund?", from_finding_id: "A4"}
  - {q: "What is the Rs5,797 Mn other-financial-liability at FY26 close, and is it the NPC-consideration payable (debt-like), which decides net cash vs net debt?", from_finding_id: "A4"}
  - {q: "Saudi Aramco tenure is stated as 2+ decades / since 2005 / 40+ years; what is the actual approved-vendor tenure that underwrites the moat claim?", from_finding_id: "A5"}
  - {q: "The Q1FY27 quarterly GP chart implies a 53.8% margin vs 38.0% annual; can management republish per-quarter GP with a clear period mapping?", from_finding_id: "A7"}
  - {q: "Consol GP margin stepped 22.4% to 38.0% on flat revenue; is this a materials-vs-opex reclassification or a genuine mix/pricing gain?", from_finding_id: "A7"}
  - {q: "Paid-up capital rose 15.7% with Other Equity up 4,741; what was the issuance (size/price/purpose) and the diluted share count and diluted EPS?", from_finding_id: "A3"}
  - {q: "NPC cost USD 102 Mn / ~Rs 1,000 Cr, ~2.7x CY2025 PAT (~0.5x net of its USD 83 Mn cash), for a 29.5%-ROCE zero-debt 40-yr-Aramco asset. Why so cheap, and is CY2025 representative or a cycle peak?", from_finding_id: "A2"}
  - {q: "The USD 120 Mn NPC order book is stated '(including executed to date)'; what is the actual FORWARD backlog net of executed, and the bid-pipeline/L1 conversion behind it?", from_finding_id: "A2"}
monitorables:
  - {item: "Merino Shelters project launch", implied_date: "Mid-Sep 2026", source_ref: "R280/R321"}
  - {item: "Merino Shelters FY27 cashflow Rs35-50Cr", implied_date: "FY27", source_ref: "R281"}
  - {item: "NPC full earnings contribution; test vs GUIDED 15-18% EBITDA (R115) not the 24.8% print", implied_date: "Q2 FY27", source_ref: "R286/R334/R115"}
  - {item: "NPC forward order book net of executed-to-date (vs USD 120 Mn incl-executed headline)", implied_date: "Q2 FY27 onward", source_ref: "R144/R119"}
  - {item: "Merino Shelters annual cashflow Rs80-120Cr", implied_date: "FY28", source_ref: "R278/R320/R084"}
  - {item: "Jammu SS seamless plant production", implied_date: "Mar 2027", source_ref: "R274/R277/R318"}
  - {item: "Dammam Coating Plant (KSA) production", implied_date: "Mar 2027", source_ref: "R273/R300"}
  - {item: "NPC HSAW OD upgrade to 120\"", implied_date: "no date", source_ref: "R107"}
  - {item: "NPC value-added coating-mill expansion", implied_date: "no date", source_ref: "slide21/R290"}
  - {item: "Group Revenue CAGR 20-25%", implied_date: "5 yrs (~FY31)", source_ref: "R221/R291"}
  - {item: "Group EBITDA margin to 15% stable", implied_date: "5 yrs", source_ref: "R222/R292"}
  - {item: "Rs5,797 other-financial-liability resolution (net-cash vs net-debt)", implied_date: "next filing", source_ref: "R185"}
  - {item: "Working-capital direction reversal", implied_date: "next filing", source_ref: "R199/R201/R183"}
flags:
  - "Clean EBITDA margin BELOW Notion 13% floor on BOTH bases: standalone 12.7% (-0.3pp), consolidated 12.3% (-0.7pp) [ARI-1 corrected]"
  - "NPC re-rating must be underwritten on the deck's OWN guided 15-18% EBITDA / 11-14% PAT (R115/R116), 700-900bps below the 24.8%/18.1% CY2025 print [COV-2]"
  - "USD 120 Mn NPC order book is '(including executed to date)' (R144/L730); true forward backlog is smaller than the 'immediate order book' framing [COV-1]"
  - "NPC bought at ~2.7x gross / ~0.5x net-of-cash CY2025 PAT for a 29.5%-ROCE zero-debt asset; price that low questions whether CY2025 is a peak"
  - "Subsidiaries flipped +162 to -253 PAT, -21% of SA PAT; subsidiary revenue fell ~72% (pre-NPC)"
  - "Working capital and CWIP ballooned on flat consol revenue; cash conversion INDETERMINATE (no CF statement)"
  - "Rs5,797 Mn other-financial-liability unidentified; net-cash vs net-debt unresolved"
  - "Equity dilution +15.7% with no diluted-EPS disclosure"
  - "GP margin step 22.4% to 38.0% on flat revenue unexplained; quarterly GP chart unusable (A7)"
  - "Headline ROCE 18.4% likely rides incl-Other-Income EBIT; clean ROCE ND"
  - "No prior-quarter deck: DROPPED_SLIDE / cross-deck drop test not runnable"
plain_language_brief_included: true
analyst_note: "Loop-1 fixes: (ARI-1) standalone clean EBITDA is 12.7%, BELOW the 13% floor by 0.3pp, not above; both clean margins (SA 12.7%, consol 12.3%) breach the floor. (COV-2) underwrite NPC on the deck's OWN Acquire-route guide 15-18% EBITDA / 11-14% PAT (R115/R116, L643), not the 24.8%/18.1% CY2025 print. (COV-1) the USD 120 Mn order book is '(including executed to date)' (R144, L730), so forward backlog is smaller than the 'immediate order book' framing. Acq-economics: NPC cost USD 102 Mn / ~Rs 1,000 Cr = ~2.7x CY2025 PAT (~0.5x net of USD 83 Mn cash), for a 29.5%-ROCE, zero-debt, 40-yr-Aramco asset; a price that low asks whether CY2025 is a peak (QfM Q11). All else preserved: FY26 is the pre-NPC old business, WC-heavy and margin-thin; NPC consolidates Q2 FY27. Verdict PROCEED WITH FLAGS, capped by INDETERMINATE cash conversion. WATCHLIST; CMP Rs714 above Rs412-589 zone; no trigger fired."
review_path: "runs/maninds-corppres-2026-09/work/final-gate/loop1/review_maninds_2026-09.md"
```
