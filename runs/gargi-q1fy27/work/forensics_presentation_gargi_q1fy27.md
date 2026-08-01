# A3 FORENSIC NOTES — Investor Presentation (Reg 30, Q1 FY27)
Company: PNGS Gargi Fashion Jewellery Ltd (GARGI, BSE 543709) | Quarter: Q1 FY27 (qtr ended 30-Jun-2026)
Doctype: **presentation** (33 slides) | Model: claude-opus-4-8
Source extract: extract_presentation_gargi_q1fy27.txt | Ledger: ledger_presentation_gargi_q1fy27.md
Ledger reconciliation: **221 / 221 rows read verbatim at cited lines = 100%**

Unit convention honoured: tabulated "Rs Mn" x0.1 -> Cr; slide 20 prose already Cr/Lakh; slide 25 bridge is Rs Crore with no label (UNIT_LABEL_MISSING). Prior-quarter deck NOT supplied (PRIOR_LEDGER_UNAVAILABLE) -> verbatim QoQ dropped-slide diff not possible; within-deck selective disclosure assessed instead.

---

## 1. FINDINGS TABLE

| id | check | ledger row | slide/line | verbatim quote | classification | forward implication |
|----|-------|-----------|-----------|----------------|----------------|---------------------|
| FN01 | F1 | U42/U165/U70 | s9 L242; s26 L837; s12 L327 | "Exceptional Items 0.0 / 0.0 / 0.0 / 1.5"; footnote "FY25 had an Exceptional Sales (one-time sale of inventory to the P. N. Gadgil & Sons Ltd. SIS ...) of Rs 26 Cr" | AMBIGUOUS | Exceptional-items line stands at nil across every quarter and FY23-25, but the FY25 Rs 26 Cr related-party inventory sale was routed through **Revenue**, inflating the FY25 base; the FY26 "1.5" exceptional is unexplained. Ask what the FY26 Rs 1.5 Mn exceptional is and why the 26 Cr sale was not isolated. |
| FN02 | F6 | U71/U76/U77 | s13 L333, L337, L342 | "Target of accelerating footprint with 20+ Point of Sales additions annually"; "~35% Revenue CAGR through disciplined execution" | FORWARD-SIGNAL | Dated management commitments -> promise-vs-delivery tracker. 35% CAGR is a hard, quotable target. |
| FN03 | F6 | U77/U127/U31 | s13 L342; s22 L673; s9 L220 | "~35% Revenue CAGR" vs "CAGR of ~5.3% over 2026-2034" vs actual "Net Revenue ... 10.6%" YoY | FORWARD-SIGNAL | 35% target sits against a 5.3% industry CAGR and an actual +10.6% Q1 print -> implies large share gains; the gap is a management question. |
| FN04 | F6 | U25 | s7 L167 | "we remain confident of stronger momentum as the festive and wedding season unfolds" | FORWARD-SIGNAL | H2-weighted outlook; sets up an H2 delivery test after a soft H1. |
| FN05 | F7 | U24 | s7 L157-158 | "While the first half of the year is seasonally softer, consumer demand remained healthy" | AMBIGUOUS | Pre-emptive seasonality hedge appearing in the same deck where EBITDA/PAT margins compressed ~300/274 bps -> pre-frames a soft H1. Confirm whether H1 softness is seasonal or channel-driven. |
| FN06 | F10 | U170/U171 | s26 L847; s27 L858 | "Diluted EPS (Rs per share) 10.2 / 8.8 / 28.6 / 30.1"; "Share Capital 96.3 / 96.3 / 103.6 / 104.7" | AMBIGUOUS | FY23 EPS Rs 10.2 is inconsistent with Mar-23 share capital Rs 96.3 Mn (9.63 M shares -> implied EPS ~Rs 4.9, which is what FY24 8.8 confirms at 84.6/9.63). ~2x gap points to an un-restated pre-bonus/split FY23 EPS or an unexplained share-count change. Also: pref issue at Rs 970/share vs CMP Rs 632 (s32 L1025). |
| FN07 | F14 | U208/U192 | s28 L940; s27 L882 | "Cash & Cash equivalents at the end of the period ... 8.6"; balance-sheet "Cash and Cash equivalents ... 727.5" | AMBIGUOUS (HIGH) | FY26 cash-flow closing cash Rs 8.6 Mn vs Mar-26 balance-sheet cash Rs 727.5 Mn = Rs 718.9 Mn unreconciled. Most likely a narrow CF "cash & equivalents" definition (deposits/liquid funds sit in Financial Assets 31.0 / Other Financial Assets 77.7 — but those do not bridge 719 Mn). Must be reconciled; a genuine error here would undermine the entire cash-flow slide. |
| FN08 | F14 | U91 | s15 L447-448 | "All retail outlets of the parent company, P. N. Gadgil & Sons Ltd., have achieved profitability from their first year of operations, with no store closures to date" | AMBIGUOUS | Attribution risk: the "no store closures / first-year profitability" halo describes the **parent**, not listed GARGI. Ask directly whether GARGI's own EBO/SIS base has had any closures or loss-making first-year stores (ties to FN13). |
| FN09 | F14 | U153/U142-U153b | s25 L773-L795 | bridge values "149.4 ... 64.1 ... 39.6 ... 31.3" (= FY26 Rs Mn table / 10) with no "(Rs Cr)" label | NEUTRAL-FACT | Slide 25 bridge is in Rs Crore but unlabeled while s8/9/24/26 label "(Rs Mn)". Drafting inconsistency; values tie out, low severity. Confirm axis label in source PDF. |
| FN10 | F16 | U29/U30/U37/U45 | s8 L185 vs L206-207; s9 L232, L248 | charts label "11%" and "15%" only; EBITDA (64->60) and PAT (53->51) bars carry **no** YoY%; table shows EBITDA -5.9%, PAT -5.0% | CONFIRMATORY-NEGATIVE | Selective framing: growth % printed only on the two rising metrics; the two declining metrics are shown bare. The decline is real (buried on slide 9). |
| FN11 | F16 | U23/U16 | s7 L162; s5 L135 | "EBO sales increasing by 186% YoY"; "Rs 69 Mn EBO Sales in Q1FY27" | CONFIRMATORY-NEGATIVE | Deck headlines EBO +186% and EBO Rs 69 Mn (22.8% of Rs 302.2 Mn) but never discloses non-EBO (SIS+franchise) revenue, which per operator context **declined ~5.3% YoY** (Rs 24.89 -> 23.58 Cr). The PNGS SIS shelf-space-squeeze risk is hidden by the EBO-only story. |
| FN12 | F16 | U141 (hist only) | s24 L743-756; s9 (absent) | "Cash Flow from Operations (Rs Mn) ... 147 ... 110" (FY-only) | CONFIRMATORY-NEGATIVE (HIGH) | **Most critical Notion metric (CFO/PAT binary test) omitted for the quarter.** No Q1FY27 cash-flow statement and no quarterly balance sheet in the deck; only annual CFO through FY26. Deliberate or not, the binary-test print is unavailable. |
| FN13 | F16 | U86/U85 | s14 L396, L395 | "Strengthened retail footprint to 135 Points of Sale ... with 9 new additions during Q1FY27" | CONFIRMATORY-NEGATIVE | "9 new additions" is **gross**; net adds were 5 (135 POS per operator context) -> ~4 removals/closures undisclosed, sitting directly under the parent "no store closures" halo (FN08). Ask for gross vs net store movement. |
| FN14 | F16 | U12-U15/U85/U112 | s5 L128, L141; s14 L395; s20 L594 | "138* Point of Sales" + "*Post Q1FY27 One New Store opened" vs "135 Points of Sale" | AMBIGUOUS | Glossy summary slide 5 uses a **post-period-inflated** 138 POS; slides 14/20 use 135 as of Q1FY27. Footnote cites only ONE post-period store (135+1=136), leaving a 2-store gap. Reconcile the POS count basis. |
| FN15 | F16 | U96 | s17 L497 | "~ 67% of in Q1FY27" / "~ 22% ..." / "~ 6% ..." | NEUTRAL-FACT | Product revenue share sums to 95%; 5% unaccounted, no residual/"Others" category. Rounding or an undisclosed category. Minor; ask for the missing 5%. |
| FN16 | F16 | U139 | s24 L748-753 | "ROE (%) & ROCE (%) ... 38 37 31 25 / 29 29 23 22" | CONFIRMATORY-NEGATIVE | ROE and ROCE **decline** FY23->FY26 (ROE 38->25), shown in the one chart with no independent tie-out table (unlike EBITDA/PAT/CFO which tie to s26/28). Deteriorating returns placed in the least verifiable panel. |
| FN17 | F16 | U61/U70 | s12 L304, L327 | "49% YoY** growth in Revenue for FY26"; footnote ** = FY25 Rs 26 Cr one-time | AMBIGUOUS | Reported FY26 growth is +18.2% (1494.0/1263.5). The headline "49%" is an ex-one-time-base figure (1494.0 / (1263.5-260) = +48.9%) — a flattering base reframing. Present it against the +18% reported number. |
| FN18 | F16 | U71/U76 | s13 L333, L337 | "20+ Point of Sales additions annually"; "20+ New Point of Sales annually" | FORWARD-SIGNAL | Deck guides "20+" POS/yr; per operator Notion, prior concall guidance was **30-35 stores/yr** -> apparent downward revision. A4 to verify against the prior transcript; softened guidance is a signal. |
| FN19 | F16 | U41/U40/U84/U115 | s9 L240, L238; s14 L396, L398; s20 L597 | "Depreciation 7.5 / 2.7"; "Finance cost 3.1 / 1.4"; "debt-free balance sheet ... asset-light"; "minimal depreciation (~1.06% of revenue)" | CONFIRMATORY-NEGATIVE | Narrative ("asset-light, debt-free, minimal depreciation") vs numbers: Q1 depreciation +178% YoY (7.5 vs 2.7) = 2.5% of revenue (not 1.06%), finance cost +121% YoY (3.1) on a "debt-free" sheet (lease interest, Ind AS 116). PPE also jumped 18.5->53.0 (Mar-25->26). A fixed-cost base is building -> future margin pressure. |
| FN20 | F16 | U74/U81/U88/U87 | s13 L350; s14 L371, L418; s21 | (omissions — no quote) | AMBIGUOUS | Notion silence audit: **online revenue %** (RED watch 4-5%), **PNGS-channel revenue mix** (RED >78%), **North-India store revenue**, and **mainboard-migration** status are all undisclosed. Deck claims "aligned with mainboard-listed company practices" (s14 L418) but names no migration application/timeline. Each is a management question. |
| FN21 | F16 | U31/U38/U46 | s9 L220, L234, L250 | "10.6%"; "EBITDA Margin (%) 19.8%"; "PAT Margin (%) 16.7%" | CONFIRMATORY-NEGATIVE | The deck's own numbers trip three Notion REDs this quarter: revenue +10.6% YoY (<20% RED), EBITDA margin 19.8% (<22% RED), PAT margin 16.7% (<18% RED). Not yet thesis-broken (PAT margin >15%, single quarter), but three simultaneous REDs. |

**FINDINGs = 21 rows across 6 flagged checks (F1, F6, F7, F10, F14, F16).**

Flags attacked and resolved as NON-findings (documented, not counted):
- **AMBIGUOUS_LAYOUT (s14, U89, L375-417):** unlabeled cluster 0,11,51,21,6,1,31,41,81,718. Native (non-OCR) extraction of a decorative hexagon-diagram text layer; maps to no labeled metric. NEUTRAL. Note: the "718" coincidentally resembles the 718.9 Mn cash gap in FN07 — confirmed coincidence, not a hidden reconciliation.
- **OCR_GARBLE (s2,6,11,23,29,30,31; U8,U21,U49,U135,U209-U212):** section dividers + photo/promo galleries. Slides 30/31 near-unreadable but carry no financial data (showrooms; "FLAT 15% OFF" promo). DROPPED_CONTENT is immaterial to financial forensics.

---

## 2. CHECKLIST SCORECARD (all 17, one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1  ZERO-VALUE STANDING ITEMS | **FINDING** | Exceptional-items line nil every period; FY25 Rs 26 Cr related-party sale routed through revenue, FY26 Rs 1.5 Mn exceptional unexplained (FN01). |
| F2  STANDALONE vs CONSOLIDATED | **N.A.** | Standalone SME; no consolidated financials presented in the deck. |
| F3  SHELL-ENTITY DETECTION | **N.A.** | No subsidiaries / no consolidation to compare cost lines against. |
| F4  UNAUDITED CONTRIBUTION | **N.A.** | Reg 30 presentation carries no auditor's report / Other Matters paragraph. |
| F5  GOING CONCERN / EoM | **N.A.** | No auditor EoM or going-concern language in a presentation. |
| F6  FORWARD-COMMITMENT MINING | **FINDING** | 20+ POS/yr, ~35% revenue CAGR, festive-momentum outlook (FN02-FN04). |
| F7  HEDGE-PHRASE MINING | **FINDING** | "first half seasonally softer" pre-emptive hedge amid margin compression (FN05); disclaimer boilerplate otherwise standard. |
| F8  TAX FORENSICS | **PASS** | ETR ~25-26% near statutory 25.17% each period (Q1FY27 25.6%, FY26 26.1%); Q4FY26 29.7% within true-up range; no deferred-tax / prior-year-adjustment lines disclosed to flag. |
| F9  OCI FORENSICS | **N.A.** | No OCI / actuarial statement in the deck. |
| F10 SHARE COUNT & DILUTION | **FINDING** | FY23 EPS Rs 10.2 inconsistent with Mar-23 share capital Rs 96.3 Mn (~2x gap); unexplained share-count history (FN06). |
| F11 RESERVES / NET WORTH TIE-OUT | **PASS** | Reserves+Capital = Shareholders' Funds exactly each period (e.g., Mar-26 1314.3+104.7=1419.0); Mar-23/24/25 also tie. |
| F12 SEGMENT FORENSICS | **N.A.** | Single reportable segment; no segment asset/liability disclosure in the deck. |
| F13 BOARD OUTCOME BEYOND RESULTS | **N.A.** | IR presentation only; no board-meeting outcome, AGM notice, or director-appointment terms. |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | Cash BS-vs-CF Rs 718.9 Mn gap; parent-vs-listed "no store closures" attribution; slide-25 missing Rs Cr label (FN07-FN09). |
| F15 ENTITY LIST DIFFS | **N.A.** | Single entity; no consolidation list; prior ledger unavailable. |
| F16 PRESENTATION-SPECIFIC (dropped/reframed) | **FINDING** | Selective YoY labels, non-EBO decline & Q1 CFO omitted, gross-vs-net store adds, POS 138-vs-135, ROE/ROCE decline, 49% base framing, softened store guide, asset-light-vs-rising-cost, Notion silences & RED trips (FN10-FN21). |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Not a concall. Notion-checklist silence audit performed and routed into F16 (FN20/FN21). |

No blank checks. GATE A3: **pass**.

---

## 3. COMMITMENT REGISTER (from F6 / guidance)

| commitment | implied date | ref | status word |
|-----------|--------------|-----|-------------|
| 20+ Point of Sales additions annually | FY27 & beyond (annual) | s13 L333/337 | target (stated) |
| ~35% Revenue CAGR through disciplined execution | FY27 & beyond | s13 L342 | target (stated) |
| Expand footprint to "truly Pan-India" | FY27 & beyond | s13 L348 | intended |
| Deepen South India (Hyderabad, Bengaluru) | ongoing | s13 L337-341 | underway ("now focusing on") |
| Stronger momentum on festive/wedding season | H2 FY27 | s7 L167 | forward outlook |
| Mithila Palkar brand partnership renewed | 2026 | s14 L385; s18 L523-524 | renewed (completed/ongoing) |
| 'Utsaav' bridal range | launched | s12 L311; s13 L345 | launched (ongoing rollout) |

---

## 4. FOR A4 (management questions)
FORWARD-SIGNAL: FN02, FN03, FN04, FN18. AMBIGUOUS: FN01, FN05, FN06, FN07, FN08, FN14, FN17, FN20.
Priority questions: (1) FN07 cash BS-vs-CF Rs 718.9 Mn — reconcile; (2) FN12/FN11 disclose Q1FY27 CFO and non-EBO channel revenue — is SIS revenue shrinking under PNGS shelf pressure?; (3) FN18 confirm store-add guidance 30-35 -> 20+ softening; (4) FN08/FN13 GARGI's own closures vs parent halo.
