# A4 ANALYST REVIEW — Man Industries (India) Ltd (MANINDS)
## Document Review: Corporate Presentation, 01 Sep 2026

Protocol: Document Review Protocol v1.0 (loaded alone; no Master, Role 4/5,
FTTCP, Section 1B, or RDE manual).
Doctype: standalone investor/corporate presentation. No results filing, no
concall in this run.
Framing: THESIS CHECK. A live Notion thesis exists (Decision Status WATCHLIST).
Inputs consumed: A1 structured extraction + fulltext, A2 ledger, A3 forensics.
Source PDF and `inputs/` never opened (A1 is sole source reader).

---

## STEP 1 — LEDGER RECONCILIATION PREAMBLE

Ledger contains 37 slides / 335 disclosure units (223 NUMBER + 49 ENTITY +
20 FORWARD + 43 DATE) + 4 footnote rows. All reviewed. A2 GATE: pass
(count test 37/223/49/20/43/2 all match). A3 GATE: pass (17 checks, 0 blank).

A3 findings incorporated: A1, A2, A3, A4, A5, A6, A7, A8, A9
(checklist F2, F6, F8, F10, F12, F14, F15, F16 = FINDING; F1, F7, F11 = PASS;
F3, F4, F5, F9, F13, F17 = N.A. for a presentation doctype).

No ledger row is unreviewed. Proceeding.

Two structural notes carried forward:
- A3 CLOSED the A2 `EBITDA*` FOOTNOTE_UNRESOLVED gap (rows 153/165). Fulltext
  L775 / L812 define it: "* EBITDA is inclusive of Other Income, since it's
  operational in nature." Load-bearing for the margin floor (A9).
- No prior-quarter deck supplied. DROPPED_SLIDE (F16) and ENTITY_CHANGE diffs
  not runnable. NPC consolidation-scope change is evidenced inside this deck
  (A7), not by diff.

---

## STEP 2 — EXTRACTION TABLES (every cell a line-anchored number or ND)

### 2.1 Standalone P&L, FY26 vs FY25 (INR Mn) — slide 28

| Line | FY26 | FY25 | YoY | Anchor |
|---|---|---|---|---|
| Revenue from Operations | 34,552 | 31,182 | +10.8% | p28 L749 |
| Other Income | 531 | 542 | (2.0)% | p28 L751 |
| Total Income | 35,083 | 31,724 | +10.6% | p28 L753 |
| Operating expenses | 30,155 | 28,415 | +6.1% | p28 L755 |
| EBITDA* (incl. Other Income) | 4,928 | 3,309 | +48.9% | p28 L757 |
| EBITDA Margin % | 14.0% | 10.4% | +360 bps | p28 L759 |
| Depreciation & amortization | 756 | 433 | +74.6% | p28 L761 |
| Finance costs | 1,542 | 1,022 | +50.9% | p28 L763 |
| PBT | 2,630 | 1,854 | +41.8% | p28 L765 |
| Tax | 672 | 484 | +39.0% | p28 L767 |
| PAT | 1,958 | 1,370 | +42.8% | p28 L769 |
| PAT Margin % | 5.6% | 4.3% | +130 bps | p28 L771 |
| EPS | ND | ND | ND | not disclosed (deck header says "except EPS" but no EPS line rendered) |

### 2.2 Consolidated P&L, FY26 vs FY25 (INR Mn) — slide 29

| Line | FY26 | FY25 | YoY | Anchor |
|---|---|---|---|---|
| Revenue from Operations | 35,639 | 35,054 | +1.7% | p29 L786 |
| Other Income | 286 | 200 | +43.2% | p29 L788 |
| Total Income | 35,925 | 35,253 | +1.9% | p29 L790 |
| Operating expenses | 31,246 | 31,690 | (1.4)% | p29 L792 |
| EBITDA* (incl. Other Income) | 4,679 | 3,563 | +31.3% | p29 L794 |
| EBITDA Margin % | 13.0% | 10.1% | +290 bps | p29 L796 |
| Depreciation & amortization | 789 | 453 | +74.4% | p29 L798 |
| Finance costs | 1,520 | 1,027 | +48.1% | p29 L800 |
| PBT | 2,370 | 2,084 | +13.7% | p29 L802 |
| Tax | 665 | 552 | +20.4% | p29 L804 |
| PAT | 1,705 | 1,532 | +11.3% | p29 L806 |
| PAT Margin % | 4.7% | 4.3% | +40 bps | p29 L808 |
| EPS | ND | ND | ND | not disclosed |

### 2.3 Slide-4 headline vs the audited tables (label check, A6)

| Slide-4 headline | Value | Ties to | Anchor |
|---|---|---|---|
| FY26 Revenue | Rs 3,592 Cr | Consolidated TOTAL INCOME 35,925 Mn (incl. Other Income), NOT Revenue from Operations 35,639 | p4 L65 vs p29 L790/L786 |
| FY26 EBITDA | Rs 468 Cr | Consolidated EBITDA 4,679 Mn | p4 L72 vs p29 L794 |
| FY26 PAT | Rs 171 Cr | Consolidated PAT 1,705 Mn | p4 L80 vs p29 L806 |
| FY26 Networth | Rs 2,087 Cr | Shareholders Fund 20,865 Mn | p4 L86 vs p30 L827 |
| FY26 ROCE | 18.4% | basis not shown (clean vs headline unverifiable) | p4 L86 |
| FY26 ROE | 9.2% | basis not shown | p4 L86 |

Label finding: the headline "Revenue" tag sits on Total Income, so it counts
Other Income as topline. Flag, not an error.

### 2.4 Historical summary, FY23-FY26 (INR Mn) — slide 31

| Line | FY23 | FY24 | FY25 | FY26 | Anchor |
|---|---|---|---|---|---|
| Total Income | 22,703 | 31,942 | 35,253 | 35,925 | p31 L867 |
| Gross Profit | 4,973 | 7,907 | 7,905 | 13,639 | p31 L866-869 |
| Gross Profit Margin % | 21.9% | 24.8% | 22.4% | 38.0% | p31 L869-870 |
| EBITDA | 1,760 | 2,932 | 3,563 | 4,679 | p31 L881-883 |
| EBITDA Margin % | 7.8% | 9.2% | 10.1% | 13.0% | p31 L883-885 |
| PAT | 670 | 1,051 | 1,532 | 1,705 | p31 L879-882 |
| PAT Margin % | 3.0% | 3.3% | 4.3% | 4.7% | p31 L885-886 |

Note: FY26 Gross Profit Margin jumps to 38.0% from 22.4% (FY25) while EBITDA
margin only reaches 13.0%. A ~15pt gross-margin step with a ~3pt EBITDA step
signals a cost-line reclassification into gross profit or an accounting
change; the deck does not narrate it. Carried as a monitorable, not a Q
(the deck gives no line detail to frame a specific question beyond A6).

### 2.5 Quarterly consolidated trend, Q1FY26-Q1FY27 (INR Mn) — slide 32

Ordering resolvable left-to-right for Total Income, EBITDA, PAT (each series
ascends with the disclosed quarter columns and the margins tie out). Gross
Profit series mapping is NOT resolvable from the flattened layout (A1 note);
carried as an unmapped set.

| Metric | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | Q1FY27 | Anchor |
|---|---|---|---|---|---|---|
| Total Income | 7,736 | 8,148 | 8,386 | 11,655 | 10,650 | p32 L900-903 |
| EBITDA | 806 | 1,018 | 1,376 | 1,480 | 1,553 | p32 L917-927 |
| EBITDA Margin % | 10.4% | 12.5% | 16.4% | 12.7% | 14.6% | p32 L917-927 |
| PAT | 276 | 370 | 550 | 509 | 614 | p32 L917-927 |
| PAT Margin % | 3.6% | 4.5% | 6.6% | 4.4% | 5.8% | p32 L917-927 |
| Gross Profit (unmapped set) | {6,269; 3,820; 3,409; 1,833; 2,128} | | | | | p32 L899-909 |
| GP Margin (unmapped set) | {53.8%; 40.6%; 35.9%; 23.7%; 26.1%} | | | | | p32 L904-909 |

Q1FY27 carries only 40 days of NPC (p32 L935-938; acquisition completed
21 May 2026, p32 L938). QoQ (Q1FY27 vs Q4FY26): Total Income -8.6% (10,650 vs
11,655), EBITDA +4.9% (1,553 vs 1,480), PAT +20.6% (614 vs 509). YoY (Q1FY27
vs Q1FY26): Total Income +37.7%, EBITDA +92.7%, PAT +122.5%.

### 2.6 Consolidated Balance Sheet, FY24-FY26 (INR Mn) — slide 30

| Line | FY24 | FY25 | FY26 | Anchor |
|---|---|---|---|---|
| Equity Share Capital | 324 | 324 | 375 | p30 L823 |
| Other Equity | 13,725 | 15,749 | 20,490 | p30 L825 |
| Shareholders Fund | 14,049 | 16,073 | 20,865 | p30 L827 |
| Long-term Borrowings | 1,363 | 1,385 | 2,402 | p30 L831 |
| Lease Liabilities (non-current) | 141 | 156 | 610 | p30 L832 |
| Deferred tax liabilities (net) | 258 | 276 | 258 | p30 L833 |
| Other long term liabilities | 42 | 73 | 97 | p30 L835 |
| Total Non-current Liabilities | 1,803 | 1,890 | 3,367 | p30 L837 |
| Short-term Borrowings | 1,722 | 3,175 | 2,595 | p30 L841 |
| Lease Liabilities (current) | 34 | 47 | 674 | p30 L842 |
| Trade payables | 5,028 | 12,002 | 14,712 | p30 L843 |
| Current tax liabilities | 54 | 21 | 275 | p30 L845 |
| Other financial liabilities (current) | 278 | 301 | 5,797 | p30 L847 |
| Other current liabilities | 1,184 | 4,283 | 1,921 | p30 L849 |
| Total Current Liabilities | 8,300 | 19,829 | 25,974 | p30 L851 |
| Total Equity & Liabilities | 24,152 | 37,792 | 50,206 | p30 L852 |
| Property, Plant & Equipment | 5,234 | 5,539 | 6,546 | p30 L824 |
| Right-of-use Assets | 163 | 186 | 1,389 | p30 L826 |
| Capital WIP | 305 | 1,334 | 3,258 | p30 L828 |
| Goodwill on Consolidation | 639 | 688 | 688 | p30 L829 |
| Investment Properties | 14 | 14 | 14 | p30 L830 |
| Intangible assets | ND (—) | 5 | 3 | p30 L831 (FY24 ZERO_STANDING) |
| Trade Receivables (non-current) | 967 | 973 | 2,385 | p30 L832 |
| Other Financial Assets (non-current) | 173 | 524 | 154 | p30 L833 |
| Other Non-current Assets | 658 | 1,023 | 438 | p30 L834 |
| Total non-current assets | 8,154 | 10,286 | 14,875 | p30 L836 |
| Inventories | 6,456 | 12,685 | 15,350 | p30 L840 |
| Investments | 2,280 | 260 | 708 | p30 L841 |
| Trade Receivables (current) | 3,551 | 8,959 | 10,098 | p30 L842 |
| Cash & Bank Balances | 2,549 | 3,792 | 6,572 | p30 L843 |
| Loans | 22 | 2 | 157 | p30 L844 |
| Other Financial Assets (current) | 105 | 98 | 201 | p30 L846 |
| Other Current Assets | 1,035 | 1,710 | 2,245 | p30 L848 |
| Current Tax Assets | ND (—) | ND (—) | ND (—) | p30 L850 (ZERO_STANDING all 3 yrs) |
| Total Current Assets | 15,998 | 27,506 | 35,331 | p30 L851 |
| Total Assets | 24,152 | 37,792 | 50,206 | p30 L852 |

### 2.7 NPC (National Pipe Company, KSA) CY2025 standalone — slide 26

| Line | SAR M | USD M | Margin | Anchor |
|---|---|---|---|---|
| Revenue | 792.7 | 211.4 | — | p26 L711 |
| Gross Profit | 214.1 | 57.1 | 27.0% | p26 L712-713 |
| EBITDA | 196.7 | 52.5 | 24.8% | p26 L714-715 |
| EBIT | 164.9 | 44.0 | 20.8% | p26 L717-719 |
| Finance Cost | 3.7 | 1.0 | — | p26 L720 |
| Other Income | 0.8 | 0.2 | — | p26 L721 |
| PBT | 162.0 | 43.2 | 20.4% | p26 L723-725 |
| Tax & Zakat | 18.5 | 4.9 | 11.4% rate | p26 L727-728 |
| PAT | 143.5 | 38.3 | 18.1% | p26 L730-732 |
| ROE / ROCE / ROA | — | — | 25.7% / 29.5% / 22.5% | p26 L722/724/726 |

NPC balance items as of Apr'2026: Total Cash & Liquid Assets USD 83.0 M
(p26 L715); Net Worth USD 158.6 M (p26 L716). FX disclosed: SAR/USD 3.75
(pegged), SAR/INR 23.955 (p26 L736). INR equivalents: Revenue ~Rs 1,898.9 Cr,
PAT ~Rs 343.6 Cr (p26 L736).

### 2.8 NPC acquisition terms

| Item | Value | Anchor |
|---|---|---|
| Stake acquired | 100% | p19 L466-468 / p20 L509-510 |
| Total consideration | USD 102 Mn (~Rs 1,000 Cr) | p19 L487 / p7 L159 |
| Debt financing | USD 70 Mn | p19 L489 / p20 L521 |
| Equity financing | USD 32 Mn | p19 L489 / p20 L521 |
| Acquisition vehicle | MISIC (wholly owned subsidiary) | p19 L476-477 |
| Completion date | 21 May 2026 | p32 L938 |
| NPC debt at closing | Zero debt at closing | p25 L699 (FORWARD) |
| Order book at acquisition | USD 120 Mn (Rs 1,130-1,150 Cr), incl. executed to date | p26 L729-730 |

---

## STEP 3 — YoY WALKS AND THE PAT BRIDGE

No QoQ P&L walk available (deck gives annual P&L only; the quarterly slide is
a chart, not a full P&L). YoY walks below.

### 3.1 Standalone PAT bridge, FY25 -> FY26 (INR Mn)

| Driver | Delta | Note |
|---|---|---|
| PAT FY25 | 1,370 | p28 L769 |
| Revenue from Ops +3,370 (31,182->34,552) | + | +10.8% topline |
| Opex +1,740 (28,415->30,155) | - | +6.1% only; opex grew slower than revenue |
| Other Income -11 (542->531) | - | flat |
| = EBITDA +1,619 (3,309->4,928) | + | +48.9%; margin +360 bps to 14.0% |
| Depreciation +323 (433->756) | - | +74.6%, new-asset ramp |
| Finance costs +520 (1,022->1,542) | - | +50.9%, debt-funded build |
| = PBT +776 (1,854->2,630) | + | +41.8% |
| Tax +188 (484->672) | - | ETR 25.6% |
| PAT FY26 | 1,958 | +42.8% (+588) |

### 3.2 Consolidated PAT bridge, FY25 -> FY26 (INR Mn)

| Driver | Delta | Note |
|---|---|---|
| PAT FY25 | 1,532 | p29 L806 |
| Revenue from Ops +585 (35,054->35,639) | + | only +1.7% |
| Opex -444 (31,690->31,246) | + | opex FELL |
| Other Income +86 (200->286) | + | +43.2% |
| = EBITDA +1,116 (3,563->4,679) | + | +31.3%; margin +290 bps to 13.0% |
| Depreciation +336 (453->789) | - | +74.4% |
| Finance costs +493 (1,027->1,520) | - | +48.1% |
| = PBT +286 (2,084->2,370) | + | +13.7% |
| Tax +113 (552->665) | - | ETR 28.1% |
| PAT FY26 | 1,705 | +11.3% (+173) |

The gap between the two bridges is the whole story: standalone PAT grew +42.8%
(+588 Mn); consolidated grew +11.3% (+173 Mn). The subsidiary layer absorbed
~415 Mn of the standalone gain. See Step 4.

---

## STEP 4 — STANDALONE vs CONSOLIDATED GAP (first-class metric, A3 F2/A1)

| Period | Standalone PAT | Consolidated PAT | Gap (Cons - SA) | Gap % of SA | Direction |
|---|---|---|---|---|---|
| FY25 | 1,370 | 1,532 | +162 | +11.8% | subsidiaries ADD |
| FY26 | 1,958 | 1,705 | -253 | -12.9% | subsidiaries DRAG |

Swing FY25->FY26: ~415 Mn, ~24-25 pts of standalone PAT. Far above the 5pt
materiality gate. This is a FLIP: the subsidiary layer moved from accretive to
dilutive in one year while consolidated revenue is HIGHER than standalone
(35,639 vs 34,552 Revenue from Ops).

Decomposition (deck gives no per-entity P&L, so this is directional, from BS
and register evidence):
- MISIC / Dammam carrying cost: Capital WIP +1,924 Mn YoY and Right-of-use
  assets +1,203 Mn YoY (p30 L828/L826) are pre-revenue builds. Depreciation
  and finance cost on them hit consolidated P&L with no matching revenue until
  Mar 2027. This is the most likely single drag.
- NPC 40-day stub (from 21 May 2026): sits in Q1FY27, i.e. NOT in the FY26
  (year-ended Mar 2026) consolidated P&L. NPC is therefore NOT the FY26 drag.
  Directional error to avoid: the FY26 consolidated numbers predate NPC.
- Merino Shelters (real-estate WOS): pre-launch (launch Mid-Sep 2026), so
  likely a small carrying drag, not yet a revenue contributor.

This directly hits the Notion tripwire "consolidated vs standalone PAT
divergence." The tripwire condition is met on the data; whether it FIRES as a
formal trigger is a human decision (Step 6). Per-subsidiary attribution is the
first management question (Q1).

---

## STEP 5 — CASH-QUALITY NOTE

The presentation carries NO cash-flow statement. Cash conversion is
INDETERMINATE. Per protocol Step 5 and house rules, an INDETERMINATE cash
read never resolves silently to PROCEED; it caps the upside of the verdict at
PROCEED WITH CAVEATS with the missing evidence named.

Missing evidence needed to resolve cash conversion:
1. Operating cash flow vs EBITDA (no CFO line anywhere in the deck).
2. Working-capital movement. From the BS: Inventories 12,685 -> 15,350
   (+2,665), Trade Receivables current 8,959 -> 10,098 (+1,139), non-current
   receivables 973 -> 2,385 (+1,412), against Trade payables 12,002 -> 14,712
   (+2,710). Net working capital direction cannot be signed without the cash
   statement, but receivables and inventory both grew faster than revenue
   (+1.7% consolidated), a red flag on cash quality. Notion tripwire
   "working-capital direction" is engaged and unresolved.
3. Interest cover / debt schedule. Finance costs +48% YoY; no maturity
   schedule.

Net-cash vs net-debt (Notion tripwire), FY26 consolidated:
- Named borrowings: Long-term 2,402 + Short-term 2,595 = 4,997 Mn.
- Cash & Bank 6,572 + Investments 708 = 7,280 Mn.
- On named borrowings alone: NET CASH ~ +2,283 Mn.
- BUT "Other financial liabilities (current)" jumped 301 -> 5,797 Mn
  (p30 L847). A3/A5: USD 70 Mn NPC acquisition debt at ~83.6 INR ~= 5,850 Mn,
  a near-exact match. If that 5,797 is the acquisition debt sitting in CURRENT
  liabilities, total debt ~ 10,847 Mn and the reading flips to NET DEBT
  ~ -3,567 Mn (before adding lease liabilities of 1,284 Mn).
- Verdict on the tripwire: the net-cash-vs-net-debt reading is INDETERMINATE
  and hinges on the classification of the 5,797 Mn line. This is a
  first-order management question (Q5).

Cash conversion classification: INDETERMINATE. Verdict capped at PROCEED WITH
CAVEATS on this axis; overall verdict carries FLAGS (Step 8A).

---

## STEP 6 — THESIS / DECISION-STATUS RECONCILIATION

Notion Decision Status (passed inline, verified): **WATCHLIST**. CMP Rs 714.
Entry zone Rs 412-589. MoS Rs 412. Position size Small. No pre-committed
trigger fired to date.

Position framing is therefore a WATCHLIST reconciliation, not a HOLD/ADD/TRIM.
No position is held; nothing to trim or add. The question this deck answers:
does it move any tripwire toward or away from the entry zone / a trigger.

Tripwire-by-tripwire reconciliation against this deck:

| Notion tripwire | This deck's evidence | Reading |
|---|---|---|
| Consolidated vs standalone PAT divergence | FY26 flip: Cons 1,705 < SA 1,958; -12.9% gap, ~25pt swing | ENGAGED, adverse. Subsidiary drag unexplained (A1). |
| EBITDA margin ex-other-income vs 13% floor | Cons EBITDA ex-OI = (4,679-286)/35,639 = 12.3%; SA ex-OI = (4,928-531)/34,552 = 12.7% | BREACHES 13% floor once OI stripped. Headline clears floor ONLY because EBITDA is defined to include OI (A9). Adverse. |
| ROCE on clean basis vs headline | Headline 18.4% (p4 L86); no computation shown | UNVERIFIABLE. Clean-basis ROCE not derivable from deck. Flag. |
| Net-debt vs net-cash reading | Net cash +2,283 on named debt; net debt ~-3,567 if 5,797 is acquisition debt | INDETERMINATE (A5). Adverse skew. |
| NPC acquisition economics & integration | NPC CY2025: 24.8% EBITDA, 18.1% PAT, 29.5% ROCE, zero debt at closing; USD 120 Mn order book (incl. executed) | Constructive on standalone NPC economics; order-book definition soft (A8). |
| Jammu/Dammam commissioning by Mar 2027 | Both targeted Mar 2027; Jammu Rs 350 Cr of ~Rs 600 Cr spent (p16 L418) | On-track per deck; unverified. Monitorable. |
| India order book split | Not disclosed in deck | ND. Gap. |
| Working-capital direction | Inventory +21% and receivables +13% vs revenue +1.7%; no CFO | ENGAGED, adverse skew; unresolved without cash statement. |

Net thesis read: the deck ADDS to the WATCHLIST caution rather than clearing
it. Three tripwires (S-vs-C PAT, EBITDA-floor-ex-OI, net-debt reading) skew
adverse; the NPC standalone economics are the constructive offset but arrive
with a soft order-book definition and an undisclosed dilution to fund them.
No pre-committed trigger formally fires on a presentation. Decision Status
stays WATCHLIST. Flags surfaced; the human decides.

---

## STEP 7 — FORWARD-TARGET REGISTER (dated / dateable commitments)

| Commitment | Implied date | Ref | Status word |
|---|---|---|---|
| Dammam Coating Plant (KSA) production | Mar 2027 | p5 L125 | targeted |
| Jammu Stainless Steel Plant production | Mar 2027 | p5 L125 / p16 L418 | underway (Rs 350 Cr of ~Rs 600 Cr spent) |
| Merino Shelters project launch | Mid-Sep 2026 | p17 L445 | on track (within days of deck) |
| Merino Shelters cashflow Rs 35-50 Cr | FY27 | p17 L446 | expected |
| Merino Shelters annual cashflow Rs 80-120 Cr | from FY28 | p17 L433 | expected |
| Merino Shelters revenue Rs 700-800 Cr | next 5-6 years | p17 L440 | projected |
| NPC full earnings contribution | Q2 FY27 onwards | p32 L941 | expected |
| NPC HSAW OD upgrade 88" -> 120" | undated | p21 L559 | "Will be Upgraded" |
| Revenue CAGR 20-25% | next 5 years | p34 L965 | targeted |
| EBITDA margin to stable 15% | long-term | p34 L970 | targeted |

---

## STEP 8 — QUESTIONS FOR MANAGEMENT

Every A3 FORWARD-SIGNAL and AMBIGUOUS finding produces at least one question.

| # | Question | From finding | Class |
|---|---|---|---|
| Q1 | FY26 consolidated PAT (1,705) is BELOW standalone (1,958) though consolidated revenue is higher. Which subsidiary drives the ~415 Mn swing from +162 Mn (FY25) to -253 Mn (FY26): Dammam/MISIC carrying cost, Merino, or elsewhere? Give per-entity PAT. | A1 | AMBIGUOUS |
| Q2 | Paid-up capital rose 324->375 Mn (+15.7%) and Other Equity rose +4,741 Mn against 1,705 Mn PAT, implying ~3,036 Mn securities premium and a ~Rs 300 Cr equity raise. What instrument (shares / warrants / preferential)? What are the terms, the dilution %, and the EPS impact the deck omits? | A4 | AMBIGUOUS |
| Q3 | The Aramco relationship is stated as "40+ Years" (p22), "since 2005 / ~20 years" AVL (p24), and "2+ Decades" (p21). Which tenure is the direct MANINDS/NPC approved-vendor relationship vs an industry association? | A6 | AMBIGUOUS |
| Q4 | The build-vs-buy slide models NPC at 15-18% EBITDA margin (p24), but NPC's actual CY2025 EBITDA margin is 24.8% (p26). Is 15-18% a conservative post-integration blended figure, and what steady-state NPC margin do you underwrite? | A6 | AMBIGUOUS |
| Q5 | Current "Other financial liabilities" jumped 301 -> 5,797 Mn, close to the USD 70 Mn NPC acquisition debt (~5,850 Mn). Does this line hold the acquisition debt, and if so why is it current (near-term repayment/refinance)? Give the debt maturity schedule and the true net-debt position. | A5 | FORWARD-SIGNAL |
| Q6 | Capital WIP rose 305 -> 3,258 Mn (10.7x in two years) and Right-of-use assets 163 -> 1,389 Mn with no revenue until Mar 2027. What is the remaining capex to commission Jammu and Dammam, and the funding split (equity vs debt)? | A5 | FORWARD-SIGNAL |
| Q7 | The USD 120 Mn NPC "order book" is stated to INCLUDE orders already executed to date (p26). Split executed vs pending: what is the true forward backlog and its execution timeline? | A8 | AMBIGUOUS |
| Q8 | EBITDA is defined to include Other Income "since it's operational in nature." Stripping Other Income, consolidated EBITDA margin is 12.3%, below the 13.0% reported. What is the operating EBITDA margin excluding Other Income, and what drives the classification? | A9 | AMBIGUOUS |
| Q9 | NPC entered the group on 21 May 2026 via MISIC; Q1FY27 carries 40 days; full contribution from Q2FY27. What consolidated revenue, EBITDA margin, and net debt do you guide for the first full-quarter NPC consolidation (Q2FY27)? | A7 | FORWARD-SIGNAL |
| Q10 | Consolidated ETR is 28.1% (above the 25.17% statutory rate and above standalone 25.6%) because subsidiary losses carry no tax shield. Once NPC (11.4% Zakat) consolidates fully, what blended group ETR do you expect? | A3 | CONFIRMATORY-NEGATIVE (asked for completeness) |
| Q11 | FY26 Gross Profit Margin jumped to 38.0% from 22.4% (FY25) on slide 31, while EBITDA margin rose only ~3pts. What reclassification or accounting change drives the ~15pt gross-margin step? | A6 | AMBIGUOUS |

---

## STEP 9 — MONITORABLES / CATALYST LIST

Seeded by the A3 commitment register (F6). Each with implied date and source.

| # | Monitorable | Implied date | Source |
|---|---|---|---|
| M1 | Merino Shelters project launch (test of "on track") | Mid-Sep 2026 | p17 L445 |
| M2 | Merino Shelters FY27 cashflow Rs 35-50 Cr | FY27 | p17 L446 |
| M3 | NPC first full-quarter consolidation (Q2FY27 P&L, margin, debt) | Q2 FY27 | p32 L941 |
| M4 | Jammu SS plant commissioning (Rs ~250 Cr capex still to spend) | Mar 2027 | p16 L418 |
| M5 | Dammam coating plant commissioning | Mar 2027 | p5 L125 |
| M6 | NPC HSAW OD upgrade 88"->120" (capex, timeline) | undated | p21 L559 |
| M7 | 5-yr Revenue CAGR 20-25% delivery vs the FY22-26 actual 13.4% | next 5 yrs | p34 L965 vs p4 L64 |
| M8 | EBITDA margin path to stable 15% (vs FY26 13.0% incl. OI) | long-term | p34 L970 |
| M9 | Merino annual cashflow Rs 80-120 Cr | from FY28 | p17 L433 |
| M10 | Working-capital direction and CFO (first cash statement post-deck) | next filing | Step 5 gap |

---

## STEP 10 — PLAIN-LANGUAGE BRIEF (mandatory)

### 1. SUMMARY NARRATIVE

Man Industries ran an investor meeting on 01 Sep 2026 and put out a
presentation. It is a deck, not a results filing. It carries full-year FY26
numbers, a balance sheet, a quarterly chart, and a large section on the Saudi
NPC acquisition.

The headline growth looks strong. Standalone FY26 PAT rose 42.8% to Rs 195.8
Cr [this deck]. But consolidated PAT rose only 11.3% to Rs 170.5 Cr [this
deck]. For the first time consolidated profit sits BELOW standalone profit. The
subsidiary layer swung by about Rs 41.5 Cr against the company, a 25-point
swing on standalone profit [derived, this deck]. The deck does not say which
subsidiary caused it. The most likely cause is the pre-revenue build at Dammam
and the Jammu plant, both funded now and earning nothing until March 2027.

The margin story has a catch. Reported consolidated EBITDA margin is 13.0%,
which clears the 13% floor in the thesis [this deck]. But the deck defines
EBITDA to include Other Income. Strip Other Income and the margin is 12.3%,
below the floor [derived, this deck]. The floor is cleared only by the
definition.

The balance sheet grew fast. Capital work in progress rose more than tenfold
in two years. A current liability line jumped from Rs 30 Cr to Rs 580 Cr,
which matches the USD 70 Mn of debt raised to buy NPC [this deck]. Whether the
group is net cash or net debt now depends entirely on how that line is read.
The deck carries no cash-flow statement, so cash quality cannot be judged.
Inventory and receivables both grew far faster than revenue, which is an early
warning on cash.

Paid-up capital rose 15.7% and reserves rose far more than profit, which points
to an equity raise of about Rs 300 Cr to fund the Saudi deal [derived, this
deck]. The deck never explains the instrument, the dilution, or the EPS effect.

NPC itself looks like a good business on its own numbers: 24.8% EBITDA margin,
29.5% ROCE, zero debt at purchase [this deck]. But the deck models it at a
lower 15-18% margin elsewhere and calls its USD 120 Mn order book one that
already includes executed work.

Decision status stays WATCHLIST. No trigger fired. The deck adds caution more
than it clears it. CMP Rs 714 is above the Rs 412-589 entry zone [prior
Notion], so there is no action, only more questions for management.

### 2. SECTOR INTELLIGENCE

Man Industries makes large-diameter line pipe (LSAW and HSAW) for oil, gas,
and water transport, plus coating and now stainless seamless pipe. Demand is
project-driven and lumpy: it rides oil and gas capex, water infrastructure,
and cross-country pipeline awards, mostly from national oil companies and
water authorities [this deck; sector read prior Notion]. Revenue can swing on
a few large orders, which the deck's own safe-harbor language flags as normal.

The Saudi and GCC market is the structural tailwind the company is buying into.
NPC's client list names Saudi Aramco (40+ year association), KOC, Qatar Energy,
Bapco, and Saudi water bodies [this deck]. Aramco approval is a multi-year, hard
to win credential; owning an already-approved Saudi vendor short-cuts a 1-2
year audit path a greenfield plant would face [this deck]. Gulf pipeline and
water capex is the demand pool the strategy targets.

The regulation and payer mix is favourable in one way: NPC pays only 11.4% tax
and Zakat in Saudi Arabia, well below India's ~25% [this deck]. Once NPC
consolidates fully, the group tax rate should fall. The headwind is input cost:
this is a steel-conversion business, so hot-rolled coil and plate prices set
the spread. The deck gives no steel-cost or spread detail, which a converter
read needs. Metric not disclosed: pipe realisation per tonne, utilisation, and
order-book split by geography.

### 3. BUSINESS-MODEL INTELLIGENCE

The company buys steel plate and coil, forms and welds it into large pipe, then
coats it, and sells to pipeline and water projects. Value add sits in
certifications (API, Aramco approval), large-diameter capability, and coating.
It is closer to a spec'd converter than a price-taker, but margins are thin: FY26
consolidated PAT margin is 4.7% and EBITDA margin 13.0% including Other Income
[this deck]. That is a low-margin, working-capital-heavy model.

This quarter shows model drift toward two higher-margin adds: stainless
seamless pipe (Jammu, Rs ~600 Cr capex, live March 2027) and coating (Dammam,
March 2027), plus a Saudi manufacturing base (NPC). The intent is to climb from
a mid-margin converter toward a value-added supplier: the stated goal is 20-25%
revenue CAGR and a 15% stable EBITDA margin [this deck]. The FY22-26 actual
revenue CAGR was 13.4% [this deck], so the 20-25% target is a step-up the deck
has not yet demonstrated.

The model's weak point this quarter is cash and consolidation. Reserves and
capital rose from an equity raise, debt rose to buy NPC, and Capital WIP
ballooned, all before the new plants earn anything. The subsidiary layer now
drags profit. The business is spending ahead of the transition it promises;
whether the spend converts to the promised margin is the open question. Metric
not disclosed: segment margins, capacity utilisation, EPS.

### 4. COMPETITION INTELLIGENCE

Man Industries competits in large-diameter line pipe with Welspun Corp, Jindal
SAW, and PSL-type players, plus regional Gulf pipe makers [peer set prior
Notion; not named in this deck]. It wins on Aramco and Gulf approvals, large
80-inch-plus diameter capability, and now a Saudi manufacturing footprint that
few Indian peers hold. The NPC purchase gives it inside-the-Gulf capacity and a
40+ year Aramco-linked client web, a real edge for Saudi water and pipeline
tenders [this deck].

Where it is structurally weaker: scale and balance-sheet strength. It is a
small-cap converter with a 4.7% net margin and a working-capital-heavy book,
against larger peers with deeper balance sheets and broader product ranges. Its
FY26 consolidated ROE is 9.2% [this deck], modest for the capital deployed. The
transition adds execution risk on two greenfields and one cross-border
integration at once.

The competitive risk to watch: the NPC order book is defined to include
executed work, so the true forward backlog against Gulf peers is smaller than
the USD 120 Mn headline [this deck]. If Gulf pipe pricing tightens or Aramco
award timing slips, a thin-margin converter with fresh acquisition debt has
little cushion. The edge is the Saudi approval moat; the exposure is scale and
cash. Metric not disclosed: peer-relative pricing, market share, backlog
quality.

---

```yaml
stage: A4-analyst
company: "MANINDS"
quarter: "2026-09"
model: claude-opus-4-8
status: complete
docs_merged: [presentation]
ledger_reconciliation:
  notes: 335
  turns: 0
  slides: 37
  all_reviewed: true
  a3_findings_incorporated: [A1, A2, A3, A4, A5, A6, A7, A8, A9]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST"
position_branch: "8A"
sc_gap_pat_pct: ["FY25 +11.8% (cons above SA)", "FY26 -12.9% (cons below SA)"]
questions_for_management:
  - {q: "Which subsidiary drives the FY26 consolidated-below-standalone PAT swing (~415 Mn)? Per-entity PAT.", from_finding_id: A1}
  - {q: "Equity raise: capital +15.7%, ~3,036 Mn premium, ~Rs 300 Cr. Instrument, warrant terms, dilution %, EPS impact?", from_finding_id: A4}
  - {q: "Aramco tenure: 40+ yrs vs since-2005 vs 2+ decades. Which is the direct approved-vendor relationship?", from_finding_id: A6}
  - {q: "Build-vs-buy models NPC at 15-18% EBITDA but actual CY2025 is 24.8%. Which is steady state?", from_finding_id: A6}
  - {q: "Other financial liabilities jumped 301->5,797 Mn (~USD70Mn NPC debt). Is acquisition debt current? Give maturity schedule and true net debt.", from_finding_id: A5}
  - {q: "Capital WIP 10.7x, no revenue to Mar 2027. Remaining Jammu/Dammam capex and equity-vs-debt funding split?", from_finding_id: A5}
  - {q: "USD 120 Mn NPC order book includes executed work. Split executed vs pending forward backlog.", from_finding_id: A8}
  - {q: "EBITDA includes Other Income; ex-OI margin is 12.3% (below 13.0% reported). Give operating EBITDA margin ex-OI.", from_finding_id: A9}
  - {q: "NPC full consolidation from Q2FY27. Guide consolidated revenue, EBITDA margin, net debt for that quarter.", from_finding_id: A7}
  - {q: "Consolidated ETR 28.1% > statutory 25.17%. Blended group ETR once NPC (11.4%) consolidates?", from_finding_id: A3}
  - {q: "FY26 gross margin jumped to 38.0% from 22.4% while EBITDA rose ~3pts. What reclassification drives it?", from_finding_id: A6}
monitorables:
  - {item: "Merino Shelters project launch", implied_date: "Mid-Sep 2026", source_ref: "p17 L445"}
  - {item: "Merino Shelters FY27 cashflow Rs 35-50 Cr", implied_date: "FY27", source_ref: "p17 L446"}
  - {item: "NPC first full-quarter consolidation", implied_date: "Q2 FY27", source_ref: "p32 L941"}
  - {item: "Jammu SS plant commissioning (Rs ~250 Cr capex remaining)", implied_date: "Mar 2027", source_ref: "p16 L418"}
  - {item: "Dammam coating plant commissioning", implied_date: "Mar 2027", source_ref: "p5 L125"}
  - {item: "NPC HSAW OD upgrade 88->120 inch", implied_date: "undated", source_ref: "p21 L559"}
  - {item: "5-yr Revenue CAGR 20-25% vs FY22-26 actual 13.4%", implied_date: "next 5 yrs", source_ref: "p34 L965"}
  - {item: "EBITDA margin to stable 15% vs FY26 13.0% incl OI", implied_date: "long-term", source_ref: "p34 L970"}
  - {item: "Merino annual cashflow Rs 80-120 Cr", implied_date: "from FY28", source_ref: "p17 L433"}
  - {item: "Working-capital direction and first CFO statement", implied_date: "next filing", source_ref: "Step 5 gap"}
flags:
  - "S-vs-C PAT flip: FY26 consolidated (1,705) below standalone (1,958), ~25pt swing, subsidiary drag unexplained (A1)."
  - "EBITDA margin clears 13% floor only because EBITDA is defined to include Other Income; ex-OI cons margin 12.3% (A9)."
  - "Undisclosed equity raise: capital +15.7%, ~Rs 300 Cr, no instrument/dilution/EPS narration; EPS omitted (A4)."
  - "USD 70 Mn NPC acquisition debt appears in CURRENT liabilities (5,797 Mn); net-cash-vs-net-debt reading INDETERMINATE (A5)."
  - "No cash-flow statement; cash conversion INDETERMINATE; inventory/receivables grew far faster than revenue."
  - "NPC USD 120 Mn order book includes executed-to-date work; true forward backlog lower (A8)."
  - "ROCE clean basis vs headline 18.4% unverifiable from deck; Notion tripwire unresolved."
  - "FY26 gross margin step to 38.0% from 22.4% unnarrated (A6)."
  - "Slide-4 headline Revenue Rs 3,592 Cr equals consolidated Total Income (incl. Other Income), not Revenue from Operations (A6)."
plain_language_brief_included: true
analyst_note: "Doc review of a single deck; no results filing/concall, so docs_merged=[presentation], turns=0. FY26 consolidated P&L PREDATES NPC (completed 21 May 2026, in Q1FY27), so NPC is NOT the FY26 S-vs-C drag; Dammam/Jammu pre-revenue carrying cost is the likely cause. Verdict PROCEED WITH FLAGS: INDETERMINATE cash caps upside at CAVEATS, but multiple material flags (S-vs-C flip, EBITDA-ex-OI below floor, undisclosed dilution, acquisition debt in current liabilities) justify FLAGS. Decision Status stays WATCHLIST; no trigger fires on a deck; CMP 714 above entry 412-589. Quarterly Gross Profit series unmappable from flattened layout; Total Income/EBITDA/PAT series are ordered and reliable."
review_path: "runs/maninds-corppres-2026-09/work/phase3-p7/review_maninds_2026-09.md"
```
