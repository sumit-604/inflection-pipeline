# Q1 FY27 RESULTS + PRESENTATION REVIEW — Macfos Limited (MCFOS / BSE: ROBU, 543787)

Agent: A4 ANALYST | Protocol: Role 4 Quarterly Results Review v1.2 (full step sequence) | Role 5 Concall: **N.A. this run** (no transcript; the Reg 30 investor presentation is analysed under Role 4 with A3 F16 deck-lens findings feeding the step sequence).
Reviewed: 2026-08-12 | **MERGED review — SUPERSEDES the earlier results-only review at this same path.** Now covers TWO filings dated 11-Aug-2026: the **Reg 33 results** (board meeting 11-Aug-2026) and the **Reg 30 investor presentation** (uploaded 11-Aug-2026, 20:42 IST).
Sources: results extract `extract_results_mcfos_q1fy27.txt` / ledger `ledger_results_mcfos_q1fy27.md` / forensics `forensics_mcfos_q1fy27.md`; presentation extract `extract_presentation_mcfos_q1fy27.txt` / ledger `ledger_presentation_mcfos_q1fy27.md` / forensics `forensics_presentation_mcfos_q1fy27.md`.

**Unit convention (Step 0B):** results filing is in **Rs Lakhs** (x0.01 = Rs Cr). Presentation is **MIXED**: P&L (slide 16) and KPI charts (slides 12/14/15) in **Rs Lakhs** (x0.01); FY-history figures (slides 6, 8) printed in **Rs Crores** verbatim (x1, unconverted). All analytical figures in **Rs Cr** unless a table states otherwise (KPI counts and per-order values are in absolute Nos./Rs). Native-text results pages (1,2,5,9,10,11,12) glyph-space-rendered; deck P&L (slide 16) is OCR-recovered but cross-check clean.

**Provenance convention:** every extraction cell is a filing number carrying its anchor — `(line N)` into the results extract, or `(sN / LN)` = slide N, line N into the presentation extract — or the literal **ND**. Numbers carried from the Notion thesis are labelled **PRIOR NOTION** and are never mixed into a filing-anchored cell. Derived-metric cells show their formula and are computed only from anchored inputs. No cell is estimated. Where a deck chart's period-to-value pairing is OCR-ambiguous, the cell is **ND** unless the pairing is resolvable by exact arithmetic (noted inline).

---

## LEDGER RECONCILIATION PREAMBLE (contractual — covers BOTH ledgers, stated before Step 1)

**Results ledger** contains **8 notes** (6 numbered markers 1,2,4,6,7,8 + 2 orphan note-fragments where markers 3 and 5 are absent) / **0 turns** / **0 slides**. Supporting enumerated rows: 13 agenda items, 98 line items, 25 zero-standing rows, 14 auditor paragraphs (6 standalone + 8 consolidated), 3 entities, 6 signature blocks, 1 director profile. **All rows reviewed at their cited line numbers.**

**Presentation ledger** contains **0 notes** / **0 turns** / **24 slides**, plus **25 line_items** (18-row standalone P&L on slide 16 + 7-row FY revenue-history table on slide 8), **118 slide_numbers**, **9 footnotes**, **2 zero-standing rows** (Exceptional Item nil all periods; OCI nil both quarter columns). **All 24 slides and every enumerated row reviewed at their cited slide/line numbers.** A2 confirmed the deck's slide-16 P&L ties **EXACTLY** to the results standalone P&L (18 non-nil values across 3 period columns, CROSS_CHECK_PASS); the deck's single "Tax expenses" line is a clean aggregation of the results filing's three tax sub-lines.

**Combined: 8 notes / 24 slides / 0 turns. No ledger row in either document is unreviewed — the protocol may proceed.**

**Findings incorporated — results (10):** F3-01, F6-01, F7-01, F8-01, F11-01, F12-01, F13-01, F13-02, F14-01, F15-01.
**Findings incorporated — presentation (12):** F6-01(pres), F7-01(pres), F14-01(pres), F16-01, F16-02, F16-03, F16-04, F16-05, F16-06, F16-07, F16-08, F16-09.
Every A3 FORWARD-SIGNAL and AMBIGUOUS finding from BOTH documents generates at least one Questions-for-Management row (Step 8.5); the `from_finding` column shows full coverage. Deck resolution of results forward-signals: **F11-01 CONFIRMED and sharpened** (deck prints ROCE/RoNW ratios, proving the balance sheet exists, yet withholds CFO/borrowings/net worth → F16-05); **F12-01 CONFIRMED** (B2B and Robu 2.0 shares still hidden even in a marketing deck → F16-02/03); **F15-01 PARTIALLY RESOLVED on purpose** (Robu 2.0 own-product/drone/defence vertical is the likely reason for Macfos Electronics, but the entity is never named → F16-06).

---

## STEP 0 — PRE-FLIGHT

**0A. Notion thesis / Decision Status (verified BEFORE any framing).**
Decision Status = **WATCHLIST**. Entry zone **Rs 477–596**; Margin of Safety Rs 477; 25% CAGR entry Rs 596; **AVOID at CMP (~Rs 1,033)**. Current holding: **3% MOMENTUM TRADE ONLY @ Rs 998 cost**; first technical trim Rs 1,164; no fundamental add above Rs 596. One-line thesis: buy at Rs 477–596 as EPS compounds Rs 25 → Rs 53 over three years on B2B corporate ecosystem deepening plus gradual Robu 2.0 mix shift; destination PE ~22x (20.8–23.2x). Key risk: cash conversion fails to normalise. Thesis-break: ROCE <20% for 2yr OR cumulative CFO/PAT <0.30x by FY28 OR Robu 2.0 abandoned. Convert-to-invest (1.5/4 met): revenue ≥35%, PAT margin ≥9% FY, CFO/PAT ≥0.70x, Robu 2.0 share ≥5% disclosed. Mainboard listing = single most important unpriced catalyst; red line no announcement by Q2 FY27.

**0B. Unit convention:** stated in header (results Lakhs x0.01; deck MIXED).

**0C. Share-count changes:** Bonus issue **941,682 shares, 1:10, 11-Mar-2026** (Note 6, L541). Paid-up 941.68 → 1,035.85 Lakhs (+94.17), tracing exactly to the bonus (F10 PASS). Prior-period EPS restated post-bonus to 1,03,58,503 (standalone) / 1,03,58,504 (consolidated) across all columns (L281, L501). All EPS comparisons are share-adjusted and directly comparable. **The deck's P&L stops at Total Comprehensive Income and carries NO EPS row and no share count** (A3 pres F10 N.A.), so it adds nothing to the dilution picture.

**0D. Numbered-notes extraction (results filing — built BEFORE any growth metric):**

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|--------|---------|---------------------------|--------------|-----------------|----------------------|
| 1 (L519-523) | Reg 33 / approval | Results per Reg 33, Audit-Committee-reviewed, Board-approved 11-Aug-2026 | ND | Q1 FY27 | None |
| 2 (L524-530) | **First-time Ind AS** | First interim results under Ind AS (34 + 101 first-time adoption) | See Annexure I | All periods | **HIGH — accounting-basis change** |
| 3-orphan (L531-533) | Comparatives restated | Q1 FY26 and FY26 comparatives restated by management per Ind AS 101 | See Annexure I | Q1 FY26, FY26 | HIGH — management-converted; unreviewed (F7-01) |
| 4-orphan (L534-536) | **Single segment** | "Engaged in only one business"; no Ind AS 108 segment disclosure | ND | All | **Suppresses B2B share & Robu 2.0 share (F12-01)** |
| 4 (L537-540) | Limited review / regroup | Current quarter limited-reviewed; prior period regrouped | ND | Q1 FY27 + comparatives | Low |
| 6 (L541-547) | Bonus issue | 941,682 bonus 1:10 on 11-Mar-2026; EPS restated | +94.17 (paid-up) | Share capital | None to EPS (restated) |
| 7 (L548-549) | Annexure I ref | Reconciliation of TCI (S & C) at Annexure I | See Annexure I | Q4 FY26, Q1 FY26, FY26 | Basis-change quantum |
| 8 (L551-557) | Investor complaints | Opening/received/disposed/unresolved all Nil | 0 | Q1 FY27 | None |

Missing markers 3 and 5 (F14-01). Exceptional Item nil all periods (L245/457). **The deck carries the same three Ind AS footnotes verbatim (3x: sL455-456, L488-489, L523-524)**, confirming the basis change and stating "Ind AS figures for the full year FY 2024-25 have not been presented" — so the deck's 3-year CAGR claims (below) rest on a **different, non-restated base** than its YoY optics (F7-01 pres).

**Auditor opinion check:** **Unmodified (clean) limited-review conclusion**, standalone (L168-176) and consolidated (L345-355). Reviewer Kishor Gujar & Associates, FRN 116747W. **Two "Other Matter" paragraphs** (not modifications) carry three AMBER-for-reliance disclosures: (i) first-time Ind AS; (ii) Q1 FY26/FY26 Ind AS comparatives management-converted and NOT limited-reviewed (F7-01); (iii) subsidiary **Nuo Zhan Technologies not reviewed by any auditor** (F3-01). The presentation is a marketing document with no audit opinion (A3 pres F4/F5 N.A.).

**0E. Business type:** Standard operating business (specialty-electronics e-commerce, Robu.in). Steps 1/5 apply; 1L/5L skipped.

STOP cleared.

---

## STEP 1 — DATA EXTRACTION (standard business) — STANDALONE and CONSOLIDATED (both, always)

### 1A. STANDALONE P&L (Rs Cr; results page 5) — deck slide 16 ties exactly

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 | Deck (s16) cross-check |
|-----------|---------|---------|---------|------|------------------------|
| Revenue from Operations | 59.2680 (L226) | 102.1112 (L226) | 81.3387 (L226) | 308.7484 (L226) | 81.3387 / 59.2680 / 308.7484 (s16/L501) ✓ |
| Other Income | 0.6054 (L229) | 0.7945 (L228) | 1.1204 (L229) | 3.0505 (L228) | 1.1204 / 0.6054 / 3.0505 (s16/L502) ✓ |
| Total Income | 59.8734 (L230) | 102.9057 (L230) | 82.4591 (L230) | 311.7989 (L230) | 82.4591 / 59.8734 / 311.7989 (s16/L503) ✓ |
| Cost of Materials Consumed | 0.1018 (L233) | 0.3010 (L233) | 0.2871 (L233) | 0.7521 (L233) | ✓ (s16/L505) |
| Purchase of Stock-in-Trade | 50.1504 (L234) | 77.8562 (L234) | 79.5300 (L234) | 260.3207 (L234) | ✓ (s16/L506) |
| Change in Inventories | (5.2303) (L235) | (0.6777) (L235) | (17.9136) (L235) | (23.9738) (L235) | ✓ (s16/L507) |
| Employee Benefits Expense | 2.5498 (L237) | 3.6806 (L236) | 3.6868 (L236) | 12.4684 (L237) | ✓ (s16/L508) |
| Finance Costs | 0.5605 (L238) | 1.1719 (L238) | 1.0040 (L238) | 3.6172 (L238) | ✓ (s16/L509) |
| Depreciation & Amortisation | 0.7502 (L240) | 0.8992 (L240) | 0.8309 (L240) | 3.2513 (L240) | ✓ (s16/L510) |
| Other Expenses | 4.2783 (L241) | 6.3393 (L241) | 7.1127 (L241) | 21.0078 (L241) | ✓ (s16/L511) |
| Total Expenses | 53.1607 (L242) | 89.5705 (L242) | 74.5378 (L242) | 277.4437 (L242) | ✓ (s16/L512) |
| Profit Before Tax | 6.7127 (L246) | 13.3352 (L246) | 7.9213 (L246) | 34.3552 (L246) | ✓ (s16/L516) |
| Tax Expense (total) | 1.7450 (L253) | 3.3695 (L253) | 2.1018 (L253) | 8.7455 (L253) | 2.1018 / 1.7450 / 8.7455 (s16/L517, aggregated) ✓ |
| PAT | 4.9677 (L256) | 9.9656 (L256) | 5.8195 (L256) | 25.6097 (L256) | 5.8195 / 4.9677 / 25.6097 (s16/L518) ✓ |
| Total Comprehensive Income | 4.9677 (L266) | 9.8009 (L266) | 5.8195 (L266) | 25.4450 (L266) | 5.8195 / 4.9677 / 25.4450 (s16/L520-521) ✓ |
| EPS reported (Basic=Diluted, Rs) | 4.80 (L274) | 9.62 (L274) | 5.62 (L274) | 24.72 (L274) | ND (deck carries no EPS row) |
| Shares for EPS (Nos.) | 1,03,58,503 (L281) | 1,03,58,503 (L281) | 1,03,58,503 (L281) | 1,03,58,503 (L281) | ND (deck) |

### 1B. CONSOLIDATED P&L (Rs Cr; results page 9) — NOT reproduced in the deck (F16-04)

| Line Item | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|-----------|---------|---------|---------|------|
| Revenue from Operations | 59.2680 (L432) | 102.1361 (L432) | 81.3401 (L432) | 308.7733 (L432) |
| Other Income | 0.6049 (L434) | 0.7946 (L434) | 1.1204 (L434) | 3.0528 (L434) |
| Total Income | 59.8729 (L435) | 102.9307 (L435) | 82.4605 (L435) | 311.8261 (L435) |
| Finance Costs | 0.5605 (L447) | 1.1719 (L447) | 1.0040 (L447) | 3.6172 (L447) |
| Depreciation & Amortisation | 0.7518 (L450) | 0.9008 (L450) | 0.8351 (L450) | 3.2576 (L450) |
| Profit Before Tax | 6.7086 (L459) | 13.3523 (L459) | 7.9141 (L459) | 34.3492 (L459) |
| Tax Expense (total) | 1.7471 (L465) | 3.3720 (L465) | 2.1025 (L465) | 8.7486 (L465) |
| PAT (Profit for period) | 4.9615 (L467) | 9.9802 (L467) | 5.8116 (L467) | 25.6006 (L467) |
| Total Comprehensive Income | 4.9615 (L478) | 9.8154 (L478) | 5.8116 (L478) | 25.4354 (L478) |
| PAT attributable to owners | 4.9615 (L482) | 9.9802 (L482) | 5.8116 (L482) | 25.6006 (L482) |
| Non-Controlling Interest | ND (L483, nil) | ND (L483, nil) | ND (L483, nil) | ND (L483, nil) |
| EPS reported (Basic=Diluted, Rs) | 4.79 (L496) | 9.63 (L496) | 5.61 (L496) | 24.71 (L496) |
| Shares for EPS (Nos.) | 1,03,58,504 (L501) | 1,03,58,504 (L501) | 1,03,58,504 (L501) | 1,03,58,504 (L501) |

*Consolidated share count 1 higher than standalone (F14-01 hygiene, immaterial). **The deck's cover letter (s1/L30-32) promises "Unaudited Standalone and consolidated Financial Statement" but reproduces the STANDALONE P&L only** — F16-04, carried to Questions.*

### 1C. Derived metrics (computed from anchored inputs)

**STANDALONE (Rs Cr / %):**

| Derived Metric | Formula | Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|----------------|---------|---------|---------|---------|------|
| Operating EBITDA | PBT + D + FinCost − OI | 7.4180 | 14.6118 | 8.6358 | 38.1732 |
| Operating EBITDA Margin (on Rev-from-Ops) | OpEBITDA / Rev | 12.52% | 14.31% | 10.62% | 12.36% |
| Reported EBITDA | PBT + D + FinCost | 8.0234 | 15.4063 | 9.7562 | 41.2237 |
| Reported EBITDA Margin (on Rev-from-Ops) | RepEBITDA / Rev | 13.54% | 15.09% | 11.99% | 13.35% |
| Core PBT (ex-OI) | PBT − OI | 6.1073 | 12.5407 | 6.8009 | 31.3047 |
| Other Income / PBT | OI / PBT | 9.02% | 5.96% | 14.14% | 8.88% |
| Effective Tax Rate | Tax / PBT | 25.99% | 25.27% | 26.53% | 25.46% |
| PAT Margin (on Rev-from-Ops) | PAT / Rev | 8.38% | 9.76% | 7.16% | 8.29% |
| Gross Profit | Rev − (CoM+Purch+ΔInv) | 14.2461 | 24.6317 | 19.4352 | 71.6494 |
| Gross Margin | GP / Rev | 24.04% | 24.12% | 23.89% | 23.21% |

**CONSOLIDATED (Rs Cr / %):** Operating EBITDA 7.4160 / 14.6304 / 8.6328 / 38.1712; Op EBITDA margin 12.51% / 14.32% / 10.61% / 12.36%; Core PBT ex-OI 6.1037 / 12.5577 / 6.7937 / 31.2964; ETR 26.04% / 25.25% / 26.57% / 25.47%; PAT margin 8.37% / 9.77% / 7.15% / 8.29%. Near-identical to standalone (subsidiaries immaterial — see S-vs-C section).

**Deck's own margins (computed on TOTAL INCOME, slide 15):** Reported EBITDA margin 13.40% (Q1FY26) → 11.83% (Q1FY27), FY26 13.17%; PAT margin 8.30% → 7.06%, FY26 8.21%; RoNW 6.88% → 5.94%, FY26 6.95%; ROCE 27.42% / 31.08% (period pairing OCR-ambiguous, third bar garbled). **These are reconciled against the Rev-from-Ops basis in the METRIC-INTEGRITY section below — do not silently adopt the deck's Total-Income denominator.**

STOP cleared: every extraction cell filing/slide-anchored or ND.

---

## PRESENTATION INTEGRATION — OPERATING-KPI TABLE (deck-only disclosures; slide-anchored; ND where OCR pairing unresolved)

These KPIs were **ND in the results-only review** — the results filing does not disclose them. All from the Reg 30 deck.

| Operating KPI | Q1 FY26 | Q1 FY27 | YoY | FY period | Source | Note |
|---------------|---------|---------|-----|-----------|--------|------|
| Total orders served (Nos.) | 1,14,066 (s11/L365-366) | 1,19,661 (s11/L365) | **+4.90%** | FY25-26 5,05,250 (s10/L290, chart-ambiguous, corroborated by AOV arithmetic) | slide 10/11 | order-count growth far below revenue +37.24% |
| Unique customers served (Nos.) | 59,771 (s11/L374) | 67,480 (s11/L373) | **+12.90%** | ND (FY not on slide 11) | slide 11 | customer base outgrew order count |
| Avg order value (Rs) | 5,196 (s10/L294) | 6,797 (s10/L290) | **+30.81%** | FY24-25 4,632 (s10/L295); FY25-26 6,111 (s10/L292) | slide 10 | **pairing resolved by exact arithmetic: AOV = Rev-from-Ops / Orders (6,797×1,19,661 = Rs 81.33 Cr = Rev-from-Ops; 5,196×1,14,066 = Rs 59.27 Cr)** |
| Revenue per customer (Rs, derived) | 9,916 | 12,053 | **+21.55%** | ND | derived (Rev-from-Ops / customers) | rising basket, fewer orders/customer |
| Orders per customer (derived) | 1.909 | 1.773 | −7.1% | ND | derived | more customers, each ordering slightly less often but far larger |
| Avg monthly website+app visitors (Nos.) | ND (chart-ambiguous) | ND (chart-ambiguous) | ND | ND | slide 10 | candidate bars 6,02,470 / 5,85,917 / 5,30,418 / 9,78,555 / 3,96,366 (s10) — period pairing OCR-ambiguous, not asserted |
| Total visitors, June-26 (point) | — | 10,02,382 (s10/L314, footnote) | — | — | slide 10 footnote | single clean anchored figure (crossed the 10-lakh/month mark) |
| Total SKUs (Nos.) | (Mar-25) 71,054 (s10/L295) | (Jun-26) 1,06,981 (s10/L289) | — | (Mar-26) 1,05,775 (s10/L289); Mar-24 18,349; Mar-23 12,759 | slide 10 | ~1,00,000+ (s6/L150); +1.14% Mar-26→Jun-26; growth "primarily small/low-cost items" (s10/L356) |
| Very slow-moving inventory % | (Mar-26) 6.21% (s12/L405) | (Jun-26) **5.52%** (s12/L403) | **−69 bps QoQ** | — | slide 12 | def: inventory/material >9 months (s12/L407); "not perishable, not obsolete, primarily low-cost SKUs" (s12/L408-409) |
| Return/replacement cost (Rs Lakh) | — | 23.88 (s12/L416) | — | FY24-25 58.19 (s12/L414); FY25-26 109.89 (s12/L415) | slide 12 | Q1 run-rate ~95.5L annualised, below FY26 109.89L; ~0.29% of Q1 Rev vs FY26 0.36% |

**Robu 2.0 per-vertical SKU adds (slide 23; qualitative counts only, NO revenue share):** Own Electronics 295 SKUs across 5 categories to Mar-26 (major launch TFT & HMI Displays, Raspberry Pi Neo Dev Board) (s23/L643-650); Own Mechanical / Drone Frames 6 new SKUs (s23/L646-647); Own Drone 7 SKUs in 2 categories (Agri-Drone Frame, Ready-to-Fly FPV, Drone RC Remote) (s23/L641-651); OEM 650 SKUs during the year (s23/L642-643). Simplify brand (s19/L573). Government & Defense customized-development engagements (s19/L574-575).

**Deck 3-year CAGR claims (slide 6, non-restated turnover basis):** Turnover 58%, EBITDA 53%, PAT 53% (s6/L156); FY revenue history (Crore, slide 8): 16.22 / 27.12 / 55.51 / 80.80 / 126.36 / 257.68 / 311.74 for FY19-20 → FY25-26 (s8/L237-238). **Caveat (F7-01):** these CAGRs run off a pre-Ind-AS, Total-Income-labelled base (FY23-24 126.36), a different basis than the restated Ind AS YoY optics.

**The single most valuable new signal from the deck:** order count grew only **+4.90%** YoY while revenue grew **+37.24%** — the entire top-line delta is carried by **average order value +30.81%** (Rs 5,196 → 6,797). Customers grew faster (+12.90%) than orders (+4.90%), so orders-per-customer fell 7.1% while value-per-order rose ~31%. This is the fingerprint of a **mix shift toward larger, fewer, higher-value baskets** — consistent with (though NOT proof of, since the split is withheld) the thesis's B2B/corporate-deepening engine. It is the first hard, if indirect, corroboration of the mix thesis the results-only filing could not provide.

---

## METRIC-INTEGRITY RECONCILIATION (Rev-from-Ops vs Total-Income basis; deck 38/22/18% vs true 37.24/…/17.15%)

The deck labels **Total Income** (Rs 82.46 Cr = 8,245.91 L, s16/L503) as "**Revenue**" on **four slides** (s6, s8, s14, s18) and states its growth/margins on that denominator. True **Revenue from Operations is Rs 81.34 Cr** (8,133.87 L). Other Income spiked **+85.07%** YoY (0.6054 → 1.1204 Cr), so the Total-Income relabel both lifts the top line and flatters the growth rate (F16-01). Both bases reconciled explicitly:

| Metric | Deck basis (Total-Income denom) | True basis (Rev-from-Ops) | Read |
|--------|----------------------------------|----------------------------|------|
| Q1 FY27 top line | "Revenue" **82.46 Cr** (= Total Income, s18/L541, s16/L503) | Revenue from Ops **81.34 Cr** (s16/L501) | Rs 1.12 Cr Other Income folded into "Revenue" |
| Revenue growth YoY | **38%** stated (37.72% on Total Income: 8245.91/5987.34−1) (s18/L542) | **+37.24%** (8133.87/5926.80−1) | +48 bps optical lift from OI + rounding |
| EBITDA growth YoY | **22%** stated (reported EBITDA +21.59%: 975.62/802.34−1) (s18/L542) | reported EBITDA +21.60%; **operating EBITDA (ex-OI) only +16.42%** (863.58/741.80−1) | the "22%" is OI-inclusive; core operating EBITDA grew ~6 pts slower |
| PAT growth YoY | **18%** stated (s18/L542) | **+17.15%** (581.95/496.77−1) | deck rounds 17.15% UP to 18% (F14-01; every rounding runs favourable) |
| EBITDA margin Q1 FY27 | **11.83%** (reported EBITDA / Total Income, s15) | operating **10.62%** / reported **11.99%** (on Rev-from-Ops) | denominator swap + OI; core operating margin is the −190 bps YoY story |
| PAT margin Q1 FY27 | **7.06%** (PAT / Total Income, s15) | **7.16%** (PAT / Rev-from-Ops) | deck's larger denominator makes PAT margin look 10 bps WORSE here; both below Notion green 7.5% and below FY26 (deck 8.21% / results 8.29%) → **AMBER either way** |
| FY25-26 "Revenue" | 311.74 Cr (s8) / 31,179.89 L (s16/L503) = Total Income | Rev-from-Ops 308.75 Cr | deck's 311.74 ties to Total Income, confirming the labeling pattern across the FY history too |

**Verdict:** the deck consistently prefers the more-flattering Total-Income denominator and rounds the one un-flattering figure (PAT growth) up. None of it is a misstatement (every number cross-checks to the audited-basis P&L), but the **presentation optics run one-directionally favourable** — logged as a governance-hygiene pattern (F14-01) and surfaced as a management question (F16-01). This review anchors all analysis to the **Revenue-from-Operations** basis.

---

## STEP 2 — Q1 FY27 YoY COMPARISON (the most important step) — STANDALONE

Base: **Q1 FY27 (ended 30-Jun-2026) vs Q1 FY26 (ended 30-Jun-2025).** Comparative Q1 FY26 is Ind AS, management-converted, NOT limited-reviewed (F7-01, confirmed by the deck's own footnote) — YoY deltas are directionally reliable but not audit-grade.

| Metric | Q1 FY26 | Q1 FY27 | YoY % Change | Verdict |
|--------|---------|---------|--------------|---------|
| Revenue from Operations | 59.2680 | 81.3387 | **+37.24%** | Strong; GREEN vs Notion ≥30% |
| Operating EBITDA | 7.4180 | 8.6358 | **+16.42%** | Lagging revenue badly |
| Operating EBITDA Margin (pp) | 12.52% | 10.62% | **−190 bps** | Contraction |
| Depreciation | 0.7502 | 0.8309 | +10.76% | Below revenue growth |
| Finance Costs | 0.5605 | 1.0040 | **+79.13%** | Far outpacing revenue (F11-01/F16-05) |
| EBIT (operating) = OpEBITDA − D | 6.6678 | 7.8049 | +17.05% | — |
| Other Income | 0.6054 | 1.1204 | **+85.07%** | Spike; drove PAT (Step 4) |
| **Core Operating PBT (PBT − OI)** | 6.1073 | 6.8009 | **+11.36%** | Cleanest health read; modest |
| Reported PBT | 6.7127 | 7.9213 | +18.00% | Flattered by OI |
| PAT | 4.9677 | 5.8195 | +17.15% | Flattered by OI |
| EPS share-adjusted (Rs) | 4.80 | 5.62 | +17.08% | Post-bonus, comparable |

**Consolidated YoY (mirror):** Revenue +37.24%, Operating EBITDA +16.41%, Core PBT ex-OI +11.30%, PAT +17.13%. No divergence.

**Six mandatory diagnostics:**
1. **Revenue grew YoY?** Yes, **+37.24%** — clears Notion green (≥30%) and the convert-to-invest revenue criterion (≥35%) on a single quarter. Above FY26's ~21% full-year rate — acceleration. Deck states "38%" on Total Income (F16-01).
2. **Operating EBITDA margin YoY?** **Contracted 10.62% vs 12.52% = −190 bps** (reported 11.99% vs 13.54% = −155 bps). Real compression. The deck's own reported-EBITDA margin on Total Income confirms the direction (13.40% → 11.83%, −157 bps, F16-08).
3. **Core operating PBT ex-OI grew YoY?** Yes but only **+11.36%** — one-third the revenue rate. Reported PBT (+18.00%) and PAT (+17.15%) grew FASTER than core → **headline PAT growth is partly non-operational.**
4. **What drove the gap?** Other Income +0.5150 Cr (+85.07%) lifted reported PBT above core; finance cost +0.4435 Cr (+79.13%) a drag; tax +0.3568 Cr (ETR 25.99%→26.53%). Other Income is the single largest swing, ~60% of the +0.8518 Cr PAT increase (Step 4).
5. **D&A / finance scaling faster than revenue?** D&A +10.76% (slower — no absorption gap). **Finance cost +79.13% is more than double revenue growth** — working-capital-funded borrowing, consistent with the Rs 17.9 Cr inventory build (ΔInv −17.9136, L235). ROCE pressure not measurable from the results filing; the DECK now discloses ROCE ~27-31% (F16-05, see Step 6).
6. **Other Income concentration changing?** Yes — OI/PBT jumped to 14.14% (from 9.02% YoY, 5.96% QoQ). Quarterly OI is lumpy; stripped, core PBT grew only +11.36%. **Quality of this quarter's growth is lower than the headline.**

**Where did the margin go?** Gross margin near-flat (23.89% vs 24.04%, −15 bps) — compression is below gross, in opex: Other Expenses +66.25% YoY (4.2783→7.1127) and Employee Benefits +44.59% YoY (2.5498→3.6868), both outrunning revenue. Negative operating leverage this quarter. Flat gross margin also means **no visible Robu 2.0 (~34% GM PRIOR NOTION) mix uplift at the gross line** — either mix has not moved materially or it is masked by single-segment reporting (F12-01), and the deck's SKU-count-only Robu 2.0 disclosure (F16-03) does not resolve it.

STOP cleared.

---

## STEP 3 — SEQUENTIAL QoQ TRAJECTORY

Results filing discloses only Q1 FY27, Q4 FY26, Q1 FY26 columns. Q2/Q3 FY26 = ND for filing-anchored cells.

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT ex-OI (Rs Cr) | PAT (Rs Cr) | One-offs flagged | QoQ run-rate |
|---------|-----------------|------------------|------------------------|-------------|------------------|--------------|
| Q1 FY26 | 59.2680 (L226) | 12.52% | 6.1073 | 4.9677 (L256) | Gratuity OCI −0.2201 in comparative (immaterial) | base |
| Q2 FY26 | ND | ND | ND | ND | — | ND |
| Q3 FY26 | ND | ND | ND | ND | — | ND |
| Q4 FY26 | 102.1112 (L226) | 14.31% | 12.5407 | 9.9656 (L256) | none | seasonal peak |
| Q1 FY27 | 81.3387 (L226) | 10.62% | 6.8009 | 5.8195 (L256) | OI +85% YoY; Rs 17.9Cr inventory build | −20.3% vs Q4 |

**PRIOR NOTION context:** Q3 FY26 standalone Revenue Rs 78.89 Cr, PAT Rs 5.63 Cr. **Deck FY revenue history (slide 8)** now gives the annual sequence on a Total-Income basis (16.22 → 311.74 Cr FY19-20 → FY25-26) but still NO intra-FY26 quarterly split — Q2/Q3 FY26 remain ND.

**Diagnostics:** Run-rate steps up YoY (+37%) but sequentially DOWN from the Q4 peak (−20.3%) — the normal fiscal reset (Q4 seasonal high, Q1 low). Q1 FY27 is the strongest Q1 on record and exceeds Q3 FY26 (PRIOR NOTION 78.89). PAT inflated by the OI spike; no exceptional items. Implied Q2 FY27 ≈ Rs 93.8 Cr to hold +37% YoY (illustrative; Q2 FY26 not filing-anchored).

STOP cleared.

---

## STEP 4 — OPERATIONAL DECOMPOSITION (PAT bridge, STANDALONE, Q1 FY26 → Q1 FY27)

Reported PAT change = 5.8195 − 4.9677 = **+0.8518 Cr (+17.15%)**. Bridge (ties exactly):

| Component | YoY Change (Rs Cr) | Recurring? |
|-----------|--------------------|------------|
| Gross profit — revenue/volume effect (ΔRev 22.0707 × prior GM 24.04%) | +5.3058 | Recurring |
| Gross profit — margin effect ((23.89%−24.04%) × 81.3387) | −0.1167 | Recurring |
| Employee Benefits increase | −1.1370 | Recurring |
| Other Expenses increase | −2.8344 | Recurring |
| Depreciation increase | −0.0807 | Recurring (post-capex) |
| Finance Cost increase | −0.4435 | Recurring (post-debt) |
| Other Income increase | +0.5150 | **NON-RECURRING typically** |
| Tax expense increase (ETR 25.99%→26.53%) | −0.3568 | Mixed |
| **Reported PAT YoY change** | **+0.8518** | — |

**Mandatory questions:**
- **Recurring vs non-recurring:** Other Income (+0.5150) = **~60% of the +0.8518 Cr PAT increase.** Core operations contributed ~+0.6936 Cr pre-tax (core PBT ex-OI grew 6.1073 → 6.8009). Growth is real but **thin at the operating line, disproportionately helped by treasury/other income.**
- **If OI reverts to prior-year (0.6054):** removing the +0.5150 OI increase gives PBT 7.9213 − 0.5150 = 7.4063 Cr; taxed at the Q1 FY27 ETR 26.53%, PAT ≈ 5.44 Cr → run-rate PAT growth only **~+9.5% YoY** (vs Q1 FY26 PAT 4.9677) rather than +17.15%. Other Income is still doing meaningful lifting; ex-OI growth ~9.5% is well below the headline.
- **D&A/finance at steady state?** D&A modest (+10.76%). **Finance cost NOT steady (+79.13%)**; if borrowings persist to fund the inventory build, this line keeps rising.
- **Tax distortion?** Deferred tax flipped from −0.0246 credit to +0.0044 charge (F8-01, immaterial). ETR ~26.5% ≈ statutory. No tax-driven distortion.

STOP cleared.

---

## STEP 5 — CASH QUALITY & BALANCE SHEET (standard business)

**Data-availability rule (v1.2):** Reg 33 mandates cash flow + balance sheet at HALF-YEAR (Q2) and full-year (Q4) only. **This is a Q1 filing — no balance sheet, no cash-flow statement; none required at Q1.** Those rows are legitimately ND. **BUT** per CLAUDE.md this makes cash conversion **INDETERMINATE**, never resolving silently to PROCEED.

**Deck escalation (F16-05):** the presentation PRINTS balance-sheet-DERIVED ratios — **ROCE 27.42% / 31.08% and RoNW 6.88%→5.94%** (slide 15) — which is only possible if management holds the balance sheet and net worth. Yet the deck **still withholds** CFO, borrowings, working capital and absolute net worth, while finance cost is +79% YoY and inventory built Rs 17.9 Cr. **The omission is therefore a disclosure CHOICE, not a Q1-convention gap** — sharpened from "not required at Q1" to "demonstrably held and not shown."

| Metric | Prior period | Current period | Change | Verdict |
|--------|--------------|----------------|--------|---------|
| CFO | ND (not filed) | ND (not filed) | ND | INDETERMINATE |
| CFO/PAT ratio | −0.31x (PRIOR NOTION, FY26) | ND | ND | INDETERMINATE — deal-breaker metric dark |
| Capex (PPE + CWIP) | ND | ND | ND | ND |
| FCF (CFO − Capex) | ND | ND | ND | ND |
| Working-capital change | ND | Inventory build ≈ +17.9136 (L235) | partial | Inventory rose sharply |
| Receivable days | 15.66 (PRIOR NOTION) | ND | ND | UNVERIFIABLE |
| Inventory days | 94.06 (PRIOR NOTION) | ND (only 5.52% slow-moving disclosed, s12) | ND | UNVERIFIABLE — red >90 tripwire untestable |
| Payable days | 19.62 (PRIOR NOTION) | ND | ND | UNVERIFIABLE |
| Cash Conversion Cycle | 90.1 days (PRIOR NOTION) | ND | ND | UNVERIFIABLE |
| PPE / CWIP | ND | ND | ND | ND |
| Net Debt / (Net Cash) | ST borrowings 35.38 (PRIOR NOTION) | ND | ND | UNVERIFIABLE; Fin cost +79% infers rise |
| Promoter Pledge | Zero (PRIOR NOTION) | ND (not disclosed either doc) | ND | No pledge disclosed; prior zero |
| **ROCE (deck-disclosed, NEW)** | FY26 28.30% (PRIOR NOTION) | **27.42% / 31.08%** (s15, mgmt-computed, period-ambiguous) | ~flat/healthy | **LIT (was dark) — supports prior assumption** |
| **RoNW (deck-disclosed, NEW)** | — | **6.88% → 5.94%** quarterly (s15) | −94 bps YoY | Declining with margins |

**Mandatory questions:**
- **CFO/PAT meeting the Pillar 2 assumption?** **Cannot be tested** — no cash-flow statement in either document. FY26 CFO/PAT was −0.31x (PRIOR NOTION), the Gate-0 Block-B deal-breaker. **This is exactly the metric that went dark while the two signals that would worsen it — finance cost +79% YoY and a Rs 17.9 Cr inventory build — are both flashing, and the deck proved the data exists yet withheld it (F16-05).**
- **Structural or growth-induced WC drag?** Unverifiable. Inventory build is consistent with +37% revenue growth, but FY26 inventory days at 94 (worst in peer group) leave the structural-vs-growth question unresolved until the Q2 half-year balance sheet. The deck's **very-slow-moving inventory 5.52% (from 6.21%, −69 bps QoQ)** is a favourable, newly disclosed sub-signal, but it measures ageing >9 months, NOT total inventory days.
- **CWIP capitalise?** ND. **Net debt within range?** ND; finance cost +79% infers higher borrowings; revenue IS accelerating (+37%), classifying any rise as growth-induced.

**Cash-conversion classification: INDETERMINATE.** Missing evidence named: (1) cash-flow statement (CFO); (2) balance sheet (inventory/receivable/payable days, CCC, ST borrowings, net debt, PPE/CWIP, absolute net worth). Per CLAUDE.md this caps the verdict at **PROCEED WITH CAVEATS** — it does not resolve to PROCEED. The deck's ROCE/RoNW do NOT lift the cap: they are management-computed ratios without the underlying cash statement.

STOP cleared.

---

## STANDALONE-vs-CONSOLIDATED PAT GAP (first-class metric, per A3 F2)

| Period | Standalone PAT (Rs Cr) | Consolidated PAT (Rs Cr) | Gap C−S (Rs Lakh) | Gap as % of Standalone |
|--------|------------------------|--------------------------|-------------------|------------------------|
| Q1 FY27 | 5.8195 (L256) | 5.8116 (L467) | −0.79 | **−0.136%** |
| Q4 FY26 | 9.9656 (L256) | 9.9802 (L467) | +1.46 | **+0.147%** |
| Q1 FY26 | 4.9677 (L256) | 4.9615 (L467) | −0.62 | **−0.125%** |
| FY26 | 25.6097 (L256) | 25.6006 (L467) | −0.91 | **−0.036%** |

**Read:** the gap is **trivially small in every period (|gap| ≤ 0.15%)**. Subsidiaries are immaterial: **Nuo Zhan Technologies** (Rs 0.99 Lakh assets, Nil revenue, unaudited, L383-394) and **Macfos Electronics Pvt Ltd** (Rs 12.23 Lakh assets, Rs 1.16 Lakh revenue, limited-reviewed, L396-398). No earnings parked in or leaked through subsidiaries at any material scale. The forward concern is the *purpose* of the entities (F3-01, F15-01), not the gap size. **The deck withholds the consolidated view entirely (F16-04)** — the one statement that would surface both entities — despite its cover letter promising consolidated scope; this makes the S-vs-C transparency question sharper, not the gap larger.

---

## IND AS FIRST-TIME ADOPTION — ANNEXURE I RECONCILIATION WALK (results filing)

First Ind AS quarter (Note 2, L524-530). Q1 FY27 is native Ind AS; Annexure I (page 11) reconciles Total Comprehensive Income from previous-GAAP to Ind AS for the three comparatives, **management-converted and NOT limited-reviewed (F7-01)** — informative, not audit-assured. The deck reproduces the same Ind AS caveat three times.

### STANDALONE reconciliation (Rs Lakh; page 11, L581-606)

| Particulars | Ind AS ref | Q4 FY26 | Q1 FY26 | FY26 |
|-------------|-----------|---------|---------|------|
| (1) As per Ind AS (TCI) | | 980.09 (L581) | 496.77 (L581) | 2,544.50 (L581) |
| (2) As per AS (TCI) | | 985.40 (L582) | 504.34 (L582) | 2,564.88 (L582) |
| **A) Difference (1)−(2)** | | **(5.32)** (L584) | **(7.57)** (L584) | **(20.39)** (L584) |
| a) Lease Impact | Ind AS 116 | (7.32) (L587) | (7.86) (L587) | (25.51) (L587) |
| b) Interest income on security deposits | Ind AS 109 | +1.45 (L588) | +1.31 (L588) | +5.45 (L588) |
| c) Depreciation on lease land | Ind AS 16 | (1.79) (L590) | (1.79) (L590) | (7.15) (L590) |
| d) Other adjustments | NA | +0.86 (L591) | +0.86 (L591) | +3.45 (L591) |
| e) Deferred tax on Ind AS adj | Ind AS 12 | +1.48 (L592) | (0.09) (L592) | +3.38 (L592) |
| f) Gratuity — OCI reclass | Ind AS 19 | ND (L594) | 22.01 (L594) | 22.01 (L594) |
| g) Deferred tax — OCI | Ind AS 12 | ND (L596) | (5.54) (L596) | (5.54) (L596) |
| h)i) Remeasurement loss DBP | Ind AS 19 | ND (L598) | (22.01) (L598) | (22.01) (L598) |
| h)ii) Tax on non-reclassified | Ind AS 12 | ND (L600) | +5.54 (L600) | +5.54 (L600) |
| **B) Total difference** | | **(5.32)** (L604) | **(7.57)** (L604) | **(20.39)** (L604) |
| (A)−(B) tie-out | | 0.00 (L606) | (0.00) (L606) | (0.00) (L606) |

### CONSOLIDATED reconciliation (Rs Lakh; page 11, L615-638)

FY26 consolidated: Ind AS TCI 2,543.54 (L615), AS TCI 2,563.96 (L616), difference **(20.42)** (L617), tie-out 0.00 (L637). Drivers mirror standalone (Lease 116 −25.51, security-deposit interest +5.45, lease-land depn −7.15, deferred tax +3.38, other +3.41); gratuity/OCI lines net to nil within TCI.

**Walk read:** Ind AS reduces reported TCI vs previous GAAP by a **small, consistent margin** — FY26 standalone −20.39 Lakh (−0.79%), consolidated −20.42 Lakh (−0.80%). Dominant driver: **lease accounting (Ind AS 116)**. Gratuity/OCI nets to zero within TCI (reclass, not value). **Thesis impact minimal:** Ind AS FY26 EPS 24.72 / 24.71 (L274/496) vs PRIOR NOTION 24.75 (IGAAP) — the Rs 25 → Rs 53 path is undisturbed. **Material caveat is assurance, not quantum:** the entire reconciliation is management-prepared and unreviewed (F7-01), so every YoY figure inherits weaker-than-audit assurance — a point the deck's headline 38/22/18% growth optics silently rely on.

---

## STEP 6 — RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections

Quarterly Bear/Base/Bull projections were not passed → projection cells ND. Comparison run against the FY26 baseline and monitoring thresholds (6B).

| Metric | Bear | Base | Bull | Actual (Q1 FY27) | Lands in |
|--------|------|------|------|-------------------|----------|
| Revenue | ND | ND | ND | 81.3387 Cr (+37.24% YoY) | Above FY26 growth rate; on/ahead of a ≥30% base |
| Op EBITDA Margin | ND | ND | ND | 10.62% | At the ≥10% green line, below FY26 12.36% |
| PAT | ND | ND | ND | 5.8195 Cr (+17.15% YoY) | Positive but OI-flattered |
| EPS | ND | ND | ND | 5.62 (Rs) | On the Rs 25→53 path (FY26 base 24.72) |
| Net Debt | ND | ND | ND | ND (no balance sheet) | Cannot place |
| ROCE | ND | ND | ND | **27.42–31.08% (deck s15)** | **Now placeable — healthy, ≥ the 20% red, near/above 28% green** |

**Probability re-weighting rule:** cannot trigger — actuals do not land BELOW BEAR (no bear passed; revenue strong). No re-weighting.

### 6B. Watchlist item status (Notion monitoring checklist walked in full — REFRESHED with deck KPIs)

| # | Watchlist Item | Green | Red | This Quarter Reading (results + deck) | Status | vs results-only |
|---|----------------|-------|-----|----------------------|--------|-----------------|
| 1 | Revenue growth YoY | ≥30% | <20% | +37.24% (Rev-from-Ops); deck states 38% (Total Income) | **GREEN** | unchanged |
| 2 | EBITDA margin | ≥10% | <9% x2q | Operating 10.62%; reported 11.99% (deck 11.83% on TI, −157 bps YoY) | **GREEN** (thin; watch) | unchanged (deck-confirmed) |
| 3 | PAT margin | ≥7.5% | <6.5% | 7.16% (Rev-from-Ops) / 7.06% (deck, TI); down from 8.38% YoY | **AMBER** | unchanged (deck-confirmed) |
| 4 | CFO/PAT | toward 0.5x+ | still <−0.5x | ND (no cash flow, either doc) | **UNKNOWN** | unchanged (deck DARK, F16-05) |
| 5 | Inventory days | — | >90 | ND (no balance sheet); Rs 17.9Cr build | **UNKNOWN** | unchanged |
| 6 | ROCE TTM | ≥28% | <20% x2yr | **27.42% / 31.08% (deck s15, mgmt-computed)** | **LIT — GREEN/AMBER band (27–31%), well above 20% red** | **FLIPPED: UNKNOWN → LIT** |
| 7 | B2B corporate share | 50–60% | <45% | ND (single-segment; deck touts "corporate traction" but no %, F16-02) | **UNKNOWN (confirmed dark)** | unchanged (deck confirms opacity) |
| 8 | Robu 2.0 revenue share | any >5% disclosed | mgmt stops discussing | ND (SKU counts only, no revenue %, F16-03); mgmt still discussing | **UNKNOWN (amber — not red; still discussed)** | unchanged (deck confirms opacity) |
| 9 | Slow-moving inventory | <5% | >8% | **5.52% Jun-26 vs 6.21% Mar-26 (deck s12), −69 bps QoQ** | **LIT — AMBER, improving** | **FLIPPED: UNKNOWN → LIT (amber, improving)** |
| 10 | Promoter pledge | none | any | No pledge disclosed either doc; prior zero (PRIOR NOTION) | **GREEN** (prior basis) | unchanged |
| 11 | Mainboard listing | announced | no announcement by Q2 FY27 | No migration mention in EITHER document (deck silent, F16-07) | **AMBER** (red line next quarter) | unchanged (deck confirms silence) |
| 12 | ST borrowings | — | >Rs 50 Cr w/o rev accel | ND; Fin cost +79% infers rise, but rev IS accelerating | **UNKNOWN / AMBER** | unchanged |
| 13 | Receivable days | — | >20 x2q | ND (no balance sheet) | **UNKNOWN** | unchanged |

**Two monitors flipped from UNKNOWN to LIT this pass — both from the deck: #6 ROCE (27–31%, healthy) and #9 slow-moving inventory (5.52%, amber but improving 69 bps QoQ).** The instrument panel improved from 7-of-13 dark to **5-of-13 dark** (CFO/PAT, inventory days, receivable days, ST borrowings, B2B share still dark; net worth absolute still dark). Critically, the deck LIT the two *favourable* monitors (ROCE, slow-moving) while leaving the *deal-breaker* (CFO/PAT) and the thesis-engine monitors (B2B share, Robu 2.0 share) dark — the selective-disclosure pattern of F16-05/F16-02/F16-03.

### 6C. Thesis-broken trigger check

| Condition | Threshold | Current Reading | FIRED? |
|-----------|-----------|-----------------|--------|
| ROCE below 20% for 2 consecutive years | <20% x2yr | **Deck 27.42–31.08% (s15); FY26 28.30% (PRIOR NOTION)** | **NO** (now LIT and clearly healthy — the deck materially de-risks this trigger) |
| Cumulative CFO/PAT <0.30x by FY28 | <0.30x by FY28 | ND this quarter; FY26 −0.31x (PRIOR NOTION); deck withheld CFO (F16-05) | **NO** (test date FY28; on a failing trajectory; metric deliberately dark) |
| Robu 2.0 abandoned / de-emphasised | qualitative | Deck actively promotes Robu 2.0 (slides 19/21/23) — clearly NOT abandoned | **NO** (deck de-risks this: management is doubling down) |

**No thesis-broken trigger FIRED.** The deck actively strengthens two of the three (ROCE healthy; Robu 2.0 emphasised, not abandoned). The CFO/PAT condition remains the live danger and the one the deck deliberately would not illuminate.

### 6D. Growth-trigger status (CONVERT-TO-INVEST, ~1.5 of 4)

| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---------|---------------------|---------------------|------------------|----------------|
| Revenue growth ≥35% | partial | Q1 FY27 +37.24% YoY | Single quarter, Q1 seasonal low | **ON TRACK** (needs FY confirmation) |
| PAT margin ≥9% full year | not met | — | 7.06–7.16%, below 9%, down YoY (deck confirms) | **WEAKENED** |
| CFO/PAT ≥0.70x | not met | — | ND; FY26 −0.31x; deck withheld (F16-05) | **DELAYED / UNVERIFIABLE** |
| Robu 2.0 share ≥5% disclosed | not met | Deck discusses Robu 2.0 extensively | Still NO revenue-share % (SKU counts only, F16-03) | **DELAYED** (disclosure still blocked) |

Conversion count unchanged (~1.5 of 4). The deck's ROCE/slow-moving disclosures do not touch any of the four convert triggers; the one trigger the deck *could* have advanced (Robu 2.0 share ≥5% disclosed) it explicitly did NOT — SKU counts are not a revenue share. **No bookable progress toward CONVERT-TO-INVEST.**

STOP cleared.

---

## STEP 7 — FOUR-PILLAR DESTINATION PE RE-VALIDATION

Destination PE ~22x (20.8–23.2x) set under Section 1B v3.3. This is a Q1 filing with no balance sheet; the deck adds a management-computed ROCE but no cash statement.

| Pillar / Input | Original Assumption | Current Reading | Action |
|----------------|---------------------|-----------------|--------|
| ROCE base (0.5×ROCE+7.5, floor 9x, cap 24x) | FY26 ROCE 28.30% (PRIOR NOTION) | **Deck ROCE 27.42–31.08% (s15, mgmt-computed, period-ambiguous, unaudited)** | **HOLD** — deck corroborates the ~28% assumption but is not audited/period-clean; FTTCP verdict stays the sole Pillar 1 authority; re-run at Q2 half-year balance sheet |
| Cash multiplier | per Section 1B | FY26 CFO/PAT −0.31x; **INDETERMINATE this quarter** (deck withheld CFO) | **HOLD** — cannot revise on missing evidence; deal-breaker dark |
| Growth Visibility Premium | + per EM | Revenue +37%; AOV +31% corroborates basket-mix; catalyst (mainboard) unpriced, red line next quarter | **HOLD** |
| Strategic Premium | + per moat status | Robu 2.0 actively pushed (drone/defence, own-brand); single-credit rule state: "ROCE recovery credited via: N/A — ROCE assumption merely corroborated, not re-rated" | **HOLD** |
| UA Multiplier | N/A (FII+DII 6.69%) | N/A unchanged | **N/A** |
| Sector Cap | per e-commerce/distribution | No reclassification | **HOLD** |
| Hurdle Ratio recheck | HR ≥ 1.953 | EPS CAGR path intact (Ind AS base 24.72 ≈ prior 24.75); current PE at CMP Rs 1,033 ≈ 41.8x on FY26 EPS >> destination 22x → HR fails at CMP | **HOLD** — confirms CMP unattractive, consistent with WATCHLIST/AVOID |

**No pillar changed → destination PE unchanged at ~22x (20.8–23.2x). No fair-value recompute.** Entry zone Rs 477–596 stands. The deck's ROCE disclosure is corroborative comfort, not a re-rating input.

STOP cleared.

---

## STEP 8 — POSITION DECISION

**Decision Status verified (Step 0A): WATCHLIST, with a 3% MOMENTUM-TRADE-ONLY sleeve @ Rs 998 cost.** Two branches apply.

### 8A (momentum sleeve — the 3% held position)
Per 8A momentum-bucket logic: **HOLD unless the chandelier/technical exit is triggered.** Nothing in either document triggers the chandelier (first technical trim Rs 1,164; CMP ~Rs 1,033). Fundamental analysis informs FUTURE re-entry sizing only. **Do NOT convert the sleeve to a value position** — margin compression, OI-flattered PAT, and a deliberately-dark cash-conversion deal-breaker do not justify it, and the deck's favourable KPI polish (ROCE, slow-moving, AOV) does not offset the withheld balance sheet.

### 8A-W (WATCHLIST — the fundamental name)
- No thesis-broken condition FIRED → not reclassified to AVOID-permanent (the deck de-risks the ROCE and Robu 2.0 triggers).
- Actuals do not land BELOW BEAR (revenue strong) → no forced downward projection reset.
- Revenue on/above a ≥30% base; PAT margin below the ≥9% conversion criterion; cash conversion INDETERMINATE.
- **Output: entry zone and Decision Status UNCHANGED.** Entry zone Rs 477–596; MoS Rs 477; 25% CAGR entry Rs 596. **AVOID at CMP** (~Rs 1,033 ≈ 1.7x the top of the entry zone; Hurdle Ratio fails). No fundamental add above Rs 596. The master decision gate is pushed to the **Q2 FY27 half-year filing**, when the balance sheet and H1 cash-flow finally allow the cash-conversion and ROCE tests — AND the mainboard-listing red line comes due.

### 8B. Add-back / trim trigger refinement
- Original: no fundamental add above Rs 596; BUY below Rs 496; MoS Rs 477. **Unchanged.**
- Refinement: **explicit evidence gate** — no fundamental re-rating until the Q2 half-year filing discloses H1 CFO/PAT and inventory/receivable days, because the deal-breaker (Block B cash generation) is currently untestable AND the deck proved management can produce balance-sheet metrics selectively (F16-05).
- Trim ladder (momentum sleeve): first technical trim Rs 1,164. **Unchanged.**

### 8C. Single cleanest metric for next quarter
**H1 FY27 CFO/PAT (cash conversion), disclosed in the Q2 half-year filing.** The thesis crux (Gate-0 Block-B deal-breaker) and exactly what BOTH this Q1 filing and the deck would not show. Q2 is mandatorily a half-year under Reg 33.
- **Bull threshold:** H1 FY27 CFO/PAT ≥ 0.50x with inventory days ≤ 90.
- **Bear threshold:** H1 FY27 CFO/PAT still negative (or <0.30x) with inventory days >90 — confirms structural WC drag, keeps the cash deal-breaker live.

STOP cleared.

---

## STEP 8.5 — QUESTIONS FOR MANAGEMENT (MERGED — results + presentation)

Contract: every A3 FORWARD-SIGNAL and AMBIGUOUS finding from BOTH documents generates ≥1 question. Coverage below. Results forward/ambiguous: F6-01, F11-01, F12-01, F13-01, F15-01, F3-01, F13-02. Presentation forward/ambiguous: F6-01(pres), F16-01, F16-02, F16-03, F16-04, F16-05, F16-06, F16-07, F16-08. Eleven questions; duplicative asks merged with full `from_finding` coverage retained.

| # | Question | Why it matters | Bull answer | Bear answer | From finding |
|---|----------|----------------|-------------|-------------|--------------|
| 1 | The deck prints ROCE (27–31%) and RoNW, so the balance sheet exists — yet no cash flow, borrowings or net worth was shown. Finance cost rose 79% YoY (Rs 0.56→1.00 Cr) and inventory built ~Rs 17.9 Cr. What were closing ST borrowings, closing inventory and net worth at 30-Jun-2026, and what is expected H1 FY27 CFO/PAT? | The deal-breaker (CFO/PAT) went dark exactly as the two metrics that would worsen it flashed, AND management demonstrably holds the balance sheet (it derived ROCE from it) but chose not to disclose it | Specific figures; ST borrowings <Rs 50 Cr; CFO turning positive on H1 | Refuses figures or ST borrowings >Rs 50 Cr with negative CFO | **F11-01, F16-05** |
| 2 | The cover letter promised a consolidated statement but the deck showed only standalone. What is the business purpose of Nuo Zhan Technologies (nil revenue, Rs 0.99 Lakh assets, unaudited), are any China-import related-party flows routed/planned through it, and why was the consolidated view omitted? | The withheld consolidated is the one statement that surfaces both subsidiaries; an unaudited HK shell in a China-import business is a live related-party conduit candidate | Clear purpose; no related-party sourcing; consolidated in the AR imminently | Vague purpose; confirms related-party flows through an unaudited shell | **F3-01, F16-04** |
| 3 | Under single-segment reporting, and given the deck explicitly cites "increasing traction from corporate customers," what were the B2B-corporate revenue share and the Robu 2.0 revenue share this quarter (a % of revenue, not SKU counts)? | Two core thesis monitors (B2B 50–60%; Robu 2.0 >5%) stayed dark even in a marketing deck that touted both qualitatively | B2B 50–60% held; Robu 2.0 >5% and rising | Declines to quantify; implies Robu 2.0 immaterial or B2B slipping | **F12-01, F16-02, F16-03** |
| 4 | The Robu 2.0 narrative describes own-brand/drone/Government-Defence productisation. Is the new Macfos Electronics Pvt Ltd subsidiary (Rs 12.23 Lakh assets, Rs 1.16 Lakh revenue) the manufacturing/assembly vehicle for this, and what capex/revenue is planned over FY27–28? | An "Electronics" manufacturing entity changes the capital-intensity and margin profile of an asset-light distribution model; the deck describes the activity but never names the entity | Defined, capital-light, margin-accretive assembly of Robu 2.0 SKUs | Open-ended capex into low-return manufacturing that lifts WC and finance cost | **F15-01, F16-06** |
| 5 | Please confirm actual figures or explicit Nil for: statutory dues overdue >3 months; MSME invoices unpaid >45 days; litigation with amounts >Rs 1 Lakh; and any statutory-return delays. | Four board agenda items were phrased "if any" with no value and no explicit Nil; only investor complaints were confirmed Nil | Explicit Nil across all four | Continued silence or non-trivial exposures | **F13-02** |
| 6 | What are the record date, e-voting window and special resolutions for the 9th AGM and the FY26 Annual Report release date; and can you attach dated, numeric milestones to the "next 5–10 year" drone/OEM/ERP commitments (which are currently all undated and qualitative)? | The AR is the Role 6 deep-dive input and may carry the withheld balance sheet; every deck commitment is soft and horizon-distant with no near-term dated milestone | Prompt AGM/AR dates; specific dated targets for drone SKUs/OEM/ERP | Delays; commitments stay open-ended and unmeasurable | **F6-01 (results), F6-01 (pres)** |
| 7 | The retiring-by-rotation director (N. P. Chavhan, 23.04% holder, DIN 07936897) is proposed for re-appointment. What is the current board composition and independent-director count, and are any independent-director renewals due? | Governance bandwidth through the growth/mainboard window; three 23%+ holders concentrate control | Adequate independent oversight; compliant board | Founder-dominated board, thin independent oversight ahead of mainboard | **F13-01** |
| 8 | Operating EBITDA margin fell 190 bps YoY (12.52%→10.62%) on Other Expenses +66% and Employee +45% while gross margin stayed flat (~24%); the shareholder letter reframes this as "22% EBITDA / 18% PAT growth." Please walk the margin bridge — what is one-off vs structural, and where is the Robu 2.0 gross-margin uplift? | The thesis relies on Robu 2.0 mix lifting margins, which is invisible; the letter's absolute-growth framing masks the margin compression | Named one-off opex (listing/AGM/AR costs); Robu 2.0 GM uplift building | Structural opex step-up with no mix uplift; negative operating leverage persists | **F16-08, supporting (Step 2/4)** |
| 9 | The mainboard-migration red line is "no announcement by Q2 FY27." This Q1 deck — the natural venue to trail a migration — is silent. What is the current status and expected timeline of the BSE mainboard migration? | Mainboard listing is the single most important unpriced catalyst; the red line is next quarter and both documents are silent | Concrete filing timeline within Q2 FY27 | No timeline; red line breached at Q2 | **F16-07, supporting (catalyst)** |
| 10 | The deck labels Total Income (Rs 82.46 Cr) as "Revenue" on four slides, though Revenue from Operations is Rs 81.34 Cr; Other Income rose 85% YoY (Rs 0.61→1.12 Cr). What drove the Other-Income jump, is it recurring at this magnitude, and will future decks report Revenue from Operations? | The relabel flatters the top line and lifts stated growth (38% vs 37.24%); ~60% of PAT growth came from this Other Income | Named recurring treasury source; deck to adopt Rev-from-Ops labelling | Lumpy/one-off OI that will reverse; continued Total-Income framing | **F16-01** |
| 11 | Very-slow-moving inventory improved to 5.52% (from 6.21% at Mar-26). What are the absolute total inventory days at 30-Jun-2026 (the deck gave the ageing % but not days), and do you expect slow-moving to cross under the 5% mark this year? | The deck disclosed the favourable ageing % but withheld total inventory days — the metric that actually tests the 94-day structural WC concern | Inventory days ≤90 and slow-moving trending under 5% | Refuses days; slow-moving % improves while total inventory days stay >90 | **F16-09** |

**Top 3 by likelihood of producing thesis-changing information:**
1. **Q1 (H1 CFO/PAT + closing borrowings/inventory/net worth)** — tests the cash-conversion deal-breaker; sharpened because the deck proved the data exists and withheld it.
2. **Q3 (B2B + Robu 2.0 revenue share)** — resolves whether the mix-shift engine is real; the AOV +31% signal makes a specific % answer highly diagnostic.
3. **Q2 (consolidated statement + Nuo Zhan purpose)** — a transparency test; an evasive answer on an unaudited HK shell in a China-import business, plus the omitted consolidated view, is itself a governance red flag.

**Channel recommendation:** MCFOS is SME-listed, hosts no concall (Role 5 N.A.). Channel = **formal IR letter/email with all eleven questions verbatim, plus AGM Q&A** (9th AGM imminent per F6-01). Submit before the AGM record date. Log each as a pre-committed watchpoint; check answer status (ANSWERED / PARTIAL / EVADED / NOT ADDRESSED) at the Q2 FY27 review.

---

## MONITORABLES / CATALYST LIST (seeded by F6 commitment registers + F13 board items + deck KPIs)

| Item | Implied date | Source ref | Status word |
|------|--------------|------------|-------------|
| Ind AS adoption live (first Ind AS financials) | FY27 (live) | Agenda 1 (L52-54); Note 2 (L524); deck footnotes | Commenced / done |
| **Q2 FY27 half-year filing — balance sheet + H1 cash-flow (CFO/PAT, inventory/receivable days, ST borrowings, ROCE, net worth)** | ~Nov 2026 | Reg 33; Step 5 / F11-01 / F16-05 | Awaited — decision gate |
| **Mainboard migration announcement — RED LINE if none by Q2 FY27** | By Q2 FY27 | Notion catalyst; F16-07 (deck silent) | No filing referenced — AMBER, due next quarter |
| FY26 Annual Report release (Role 6 deep-dive; may carry withheld balance sheet) | Within weeks | Agenda 3 (L58-60); F6-01 | Board approved |
| 9th AGM — record date, e-voting, special resolutions | Imminent | Agenda 3,4 (L58-63); F13-01 | Board approved; scrutinizer CZ & Associates LLP |
| Director re-appointment (N. P. Chavhan, 23.04%) | At 9th AGM | Agenda 5 (L64-66); F13-01 | Proposed, subject to AGM |
| Macfos Electronics Pvt Ltd trajectory (trading vs assembly / Robu 2.0 vehicle) | Ongoing; FY27 diffs | Entity list (L343, 396-398); F15-01 / F16-06 | New subsidiary — baseline set |
| Nuo Zhan Technologies — related-party flows / audit status | Ongoing | Entity list (L342, 383-394); F3-01 / F16-04 | Unaudited shell — watch |
| **Very-slow-moving inventory % (deck-disclosed)** | Quarterly (deck) | s12/L403-405; F16-09 | 5.52% Jun-26, improving 69 bps QoQ — watch for cross under 5% green |
| **B2B / Robu 2.0 revenue share disclosure** | Awaited (AGM / next deck) | F16-02 / F16-03 | Still qualitative only — press for a % |
| **Avg order value / order count split** | Quarterly (deck) | s10/11; derived | AOV +31%, orders +4.9% — watch whether basket-mix shift persists |
| Robu 2.0 SKU build (drone 7, electronics 295, OEM 650) → disclosed revenue | Ongoing | s23/L641-650; F6-01 pres | SKU baseline set; revenue conversion unproven |
| Return/replacement cost as % of revenue | Quarterly (deck) | s12/L414-416 | Q1FY27 23.88L (~0.29% of Rev), below FY26 0.36% — improving |
| Special Purpose Independent Auditor Report on Ind AS FY26 | 11-Aug-2026 (issued) | LRR Other Matter (L194-195, 373-374) | Completed |

---

## PLAIN-LANGUAGE BRIEF (mandatory standing deliverable — final narrative section)

### 1. SUMMARY NARRATIVE

Macfos grew Q1 FY27 revenue 37% year on year to Rs 81.3 Cr (THIS FILING, standalone; from Rs 59.3 Cr), its strongest first quarter on record and above the 30% the thesis wants (PRIOR NOTION green line). The investor deck (THIS DECK) reproduces the exact same P&L and adds the operating detail the filing lacked. Profit after tax rose 17% to Rs 5.8 Cr (THIS FILING), which the deck rounds up to 18% (THIS DECK). But the quality is thinner than the headline: operating margin, stripping other income, fell from 12.5% to 10.6% (THIS FILING), a 190 basis point drop, because staff costs rose 45% and other expenses 66% while gross margin stayed flat near 24%. Roughly 60% of the profit increase came from other income (up 85% to Rs 1.1 Cr), not core operations (THIS FILING). Finance cost rose 79% and inventory built about Rs 17.9 Cr (THIS FILING), pointing to more borrowing to hold stock. The deck's most useful new fact: orders served grew only 4.9% (1,14,066 to 1,19,661) while revenue grew 37%, so the average order value jumped about 31% to Rs 6,797 (THIS DECK) — growth is carried by bigger baskets, consistent with, though not proof of, the B2B/corporate deepening the thesis relies on. The deck also newly discloses ROCE of 27 to 31% (healthy) and very-slow-moving inventory improving to 5.52% from 6.21% (THIS DECK), which lit up two monitors that were dark last pass. The core problem is unchanged and now sharper: neither document shows a balance sheet or cash-flow statement, so cash conversion (CFO/PAT), the thesis deal-breaker (FY26 about minus 0.31x, PRIOR NOTION), cannot be measured — and the deck proved management holds the balance sheet (it derived ROCE from it) yet still would not show the cash statement, borrowings or net worth (THIS DECK). The deck also labels total income as "revenue" on four slides and reframes the margin compression as "22% EBITDA / 18% PAT growth" (THIS DECK); every rounding runs favourable. This is the first Ind AS quarter; the accounting change barely moves profit (FY26 EPS Rs 24.72 Ind AS vs Rs 24.75 IGAAP), so the earnings path holds, but the comparatives are management-converted and not auditor-reviewed. No thesis-broken trigger fired; the deck actively de-risks two of them (ROCE healthy, Robu 2.0 emphasised). Decision Status stays WATCHLIST: AVOID at about Rs 1,033 (PRIOR NOTION), roughly 1.7x the top of the Rs 477 to Rs 596 entry zone; the 3% momentum sleeve is held on technical rules only. The real test is the Q2 half-year filing, when the balance sheet and cash-flow finally appear and the mainboard red line comes due.

### 2. SECTOR INTELLIGENCE

Macfos operates in Indian specialty-electronics and robotics-components e-commerce through Robu.in (PRIOR NOTION), which the deck describes as a specialised store for robotic, drone, e-bike, IoT, 3D-printer, development-board and sensor parts, 1,00,000+ SKUs, 150+ brands, 210+ vendor tie-ups, a 50,000+ sq ft warehouse and 300+ staff (THIS DECK, s6). The structural tailwind is the deepening of India's electronics/robotics/embedded ecosystem across education, R&D, industrial automation and a growing corporate base, which this quarter delivered (+37% YoY, THIS FILING; total visitors crossed 10,02,382 in June-26, THIS DECK). It is a distribution model, so it carries the sector's classic weakness, working-capital intensity: FY26 inventory days ~94, worst in the peer group, cash-conversion cycle ~90 days (PRIOR NOTION); nothing in either document refutes that, and the Rs 17.9 Cr inventory build with 79% higher finance cost (THIS FILING) sits on it. The deck offers one favourable sector-hygiene read: very-slow-moving stock (older than 9 months) is only 5.52% and falling (THIS DECK), described as low-cost, non-perishable SKUs. Regulation matters two ways: Ind AS is now live (BOTH), and a mainboard migration off the SME platform is the single most important unpriced catalyst, red line no announcement by Q2 FY27 (PRIOR NOTION) — on which both documents are silent (THIS DECK, F16-07). China sourcing is a live sector feature (PRIOR NOTION), which is why the dormant Hong Kong subsidiary is worth pressing. Metrics the documents did NOT disclose for sector context: B2B share, Robu 2.0 share, inventory days, receivable days (all ND).

### 3. BUSINESS-MODEL INTELLIGENCE

Macfos makes money by buying electronics/robotics components and reselling them online; purchases of stock-in-trade (Rs 79.5 Cr this quarter, THIS FILING) dominate the cost base, confirming an asset-light trading model. Gross margin is ~24% on core products (THIS FILING), with proprietary Robu 2.0 brands (Simplify / SmartElex / EasyMech / SimplyFly / ProRange) carrying ~34% (PRIOR NOTION) and meant to lift blended margins; this quarter blended gross margin did NOT rise (flat ~24%, THIS FILING), and the deck disclosed Robu 2.0 only as SKU counts (own electronics 295, own drone 7, OEM 650; THIS DECK, s23), never a revenue share, so the mix uplift stays invisible. The deck's KPIs sharpen how the model actually scaled this quarter: customers grew 12.9% (59,771 to 67,480) and orders only 4.9% (1,14,066 to 1,19,661), while average order value rose ~31% (Rs 5,196 to 6,797) and revenue per customer rose ~22% (THIS DECK, derived) — more customers, each ordering slightly less often but with far larger baskets. That is the signature of a shift toward bigger corporate/bulk orders. Two model-drift signals: a new subsidiary, Macfos Electronics Pvt Ltd (Rs 12.23 Lakh assets, THIS FILING), which the deck's own-brand/drone/defence narrative suggests is the Robu 2.0 productisation vehicle (THIS DECK, F16-06), potentially raising capital intensity; and negative operating leverage this quarter (revenue +37%, operating EBITDA +16%, THIS FILING). The model's Achilles heel remains cash: FY26 CFO/PAT ~minus 0.31x (PRIOR NOTION), with no update in either document (THIS FILING and THIS DECK both withhold the cash-flow statement). Unit economics the documents DID disclose (THIS DECK): orders, customers, AOV, SKUs, visitors, slow-moving inventory; those they did NOT: CFO, inventory days, receivable days, B2B share, Robu 2.0 revenue share.

### 4. COMPETITION INTELLIGENCE

Against imperfect listed peers (Dixon, Centum, IntraSoft, Digidrive — PRIOR NOTION), Macfos wins on profitability: EBITDA margin ~10–12% (THIS FILING Q1 operating 10.6%, reported 12.0%; deck 11.83% on total income) is well above Dixon 3.9%, Centum 8.4%, IntraSoft 3.5% (PRIOR NOTION), reflecting a curated higher-margin niche catalogue and proprietary Robu 2.0 range rather than commoditised contract volume; the deck's ROCE of 27–31% (THIS DECK) corroborates a capital-efficient niche. Where it is structurally weaker is working capital: ~90-day cash-conversion cycle and ~94 inventory days, worst in the peer set (PRIOR NOTION), and this quarter's Rs 17.9 Cr inventory build plus 79% higher finance cost (THIS FILING) sit on that weak point; the deck's favourable slow-moving-inventory read (5.52%, THIS DECK) softens but does not resolve it, because it withheld total inventory days. The competitive risk to watch is that the niche is defensible on margin but capital-hungry: if growth keeps requiring inventory and borrowing, the superior margin is partly given back through financing cost and poor cash conversion — the thesis's key risk. Robu 2.0's proprietary brands and drone/Government-Defence optionality (THIS DECK, s19/23) are the differentiators that could widen the moat, but revenue traction is still undisclosed (SKU counts only). Competitive metrics the documents did NOT disclose: Robu 2.0 revenue share, B2B share, defence-engagement scale (all ND).

---

```yaml
stage: A4-analyst
company: "MCFOS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
docs_merged: [results, presentation]
ledger_reconciliation:
  notes: 8
  turns: 0
  slides: 24
  all_reviewed: true
  a3_findings_incorporated: ["F3-01","F6-01","F7-01","F8-01","F11-01","F12-01","F13-01","F13-02","F14-01","F15-01","F16-01","F16-02","F16-03","F16-04","F16-05","F16-06","F16-07","F16-08","F16-09"]
protocol_verdict: "PROCEED WITH CAVEATS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q1 FY27", gap_pct: -0.136}
  - {period: "Q4 FY26", gap_pct: 0.147}
  - {period: "Q1 FY26", gap_pct: -0.125}
  - {period: "FY26", gap_pct: -0.036}
monitors_flipped_vs_results_only:
  - {monitor: "ROCE TTM", from: "UNKNOWN", to: "LIT (GREEN/AMBER band 27.42-31.08%, deck s15)"}
  - {monitor: "Slow-moving inventory %", from: "UNKNOWN", to: "LIT (AMBER 5.52%, improving 69bps QoQ, deck s12)"}
questions_for_management:
  - {q: "Closing ST borrowings, inventory and net worth at 30-Jun-2026 and expected H1 FY27 CFO/PAT, given the deck derived ROCE from a balance sheet it withheld while finance cost +79% YoY and ~Rs17.9Cr inventory build", from_finding_id: "F11-01,F16-05"}
  - {q: "Nuo Zhan HK shell purpose, China-import related-party flows, and why the promised consolidated statement was omitted from the deck", from_finding_id: "F3-01,F16-04"}
  - {q: "B2B corporate revenue share and Robu 2.0 revenue share as a % (not SKU counts), both touted but never quantified", from_finding_id: "F12-01,F16-02,F16-03"}
  - {q: "Is Macfos Electronics Pvt Ltd the Robu 2.0 manufacturing/assembly vehicle (own-brand/drone/defence) and what FY27-28 capex/revenue is planned", from_finding_id: "F15-01,F16-06"}
  - {q: "Explicit figures or Nil for overdue statutory dues >3m, MSME unpaid >45d, litigation >Rs1L, statutory-return delays", from_finding_id: "F13-02"}
  - {q: "9th AGM record date/e-voting/resolutions, FY26 AR release, and dated numeric milestones for the undated 5-10yr drone/OEM/ERP commitments", from_finding_id: "F6-01,F6-01-pres"}
  - {q: "Board composition and independent-director count given re-appointment of 23.04%-holder director N. P. Chavhan", from_finding_id: "F13-01"}
  - {q: "Margin bridge: operating EBITDA margin -190bps YoY (opex +45%/+66%, gross margin flat) reframed as 22%/18% growth; one-off vs structural and where is Robu 2.0 GM uplift", from_finding_id: "F16-08,supporting-step2-4"}
  - {q: "Mainboard migration status and timeline before the Q2 FY27 red line; the deck was the natural venue and was silent", from_finding_id: "F16-07,supporting-catalyst"}
  - {q: "Why is Total Income (82.46 Cr) labelled Revenue on 4 slides vs Rev-from-Ops 81.34 Cr, what drove Other Income +85% YoY, and is it recurring", from_finding_id: "F16-01"}
  - {q: "Absolute total inventory days at 30-Jun-2026 (deck gave slow-moving % 5.52 but not days) and whether slow-moving crosses under 5% this year", from_finding_id: "F16-09"}
monitorables:
  - {item: "Q2 FY27 half-year filing: balance sheet + H1 cash flow (CFO/PAT, inventory/receivable days, ST borrowings, ROCE, net worth) - decision gate", implied_date: "~Nov 2026", source_ref: "Reg 33 / F11-01 / F16-05 / Step 5"}
  - {item: "Mainboard migration announcement - RED LINE if none by Q2 FY27", implied_date: "Q2 FY27", source_ref: "Notion catalyst / F16-07 (deck silent)"}
  - {item: "FY26 Annual Report release (Role 6 deep-dive; may carry withheld balance sheet)", implied_date: "within weeks", source_ref: "Agenda 3 L58-60 / F6-01"}
  - {item: "9th AGM record date, e-voting, special resolutions", implied_date: "imminent", source_ref: "Agenda 3-4 L58-63 / F13-01"}
  - {item: "Director re-appointment N. P. Chavhan (23.04%)", implied_date: "at 9th AGM", source_ref: "Agenda 5 L64-66 / F13-01"}
  - {item: "Macfos Electronics Pvt Ltd trajectory (trading vs assembly / Robu 2.0 vehicle)", implied_date: "ongoing FY27", source_ref: "Entity list L343,396-398 / F15-01 / F16-06"}
  - {item: "Nuo Zhan Technologies related-party flows / audit status / consolidated disclosure", implied_date: "ongoing", source_ref: "Entity list L342,383-394 / F3-01 / F16-04"}
  - {item: "Very-slow-moving inventory % (deck) - watch for cross under 5% green", implied_date: "quarterly (deck)", source_ref: "s12/L403-405 / F16-09"}
  - {item: "B2B / Robu 2.0 revenue share disclosure (still qualitative)", implied_date: "AGM / next deck", source_ref: "F16-02 / F16-03"}
  - {item: "Avg order value vs order-count split (AOV +31%, orders +4.9%) - basket-mix shift persistence", implied_date: "quarterly (deck)", source_ref: "s10/11 derived"}
protocol_verdict_basis: "Revenue GREEN (+37.24% YoY) but PAT margin AMBER (7.06-7.16%), OI-flattered PAT (~60% of PAT growth), operating margin -190bps, finance cost +79% YoY, Rs17.9Cr inventory build; deck lit ROCE (27-31%) and slow-moving inventory (5.52%, improving) but STILL no cash flow/balance sheet in either document -> cash conversion INDETERMINATE caps verdict at PROCEED WITH CAVEATS; deck proved BS exists yet withheld it (F16-05); no thesis-broken trigger fired (deck de-risks ROCE and Robu 2.0 triggers); unmodified audit with two Other-Matter paras"
flags:
  - "INDETERMINATE cash conversion: no cash-flow statement in EITHER document (Q1 not mandated); CFO/PAT deal-breaker untestable; deck derived ROCE from a balance sheet it withheld (F16-05)"
  - "Selective disclosure: deck LIT the favourable monitors (ROCE 27-31%, slow-moving inventory 5.52%) but left the deal-breaker (CFO/PAT) and thesis-engine monitors (B2B share, Robu 2.0 revenue share) dark"
  - "Metric-integrity: deck labels Total Income (82.46 Cr) as Revenue on 4 slides vs Rev-from-Ops 81.34 Cr; states 38/22/18% growth (true 37.24%/op-EBITDA 16.42%/17.15%); all roundings favourable (F16-01, F14-01)"
  - "AOV bridge: orders served +4.90% YoY vs revenue +37.24% -> avg order value +30.81% (deck); growth carried by basket size, indirect B2B-mix corroboration"
  - "Single-segment reporting still suppresses B2B share and Robu 2.0 revenue share even in a marketing deck (F12-01, F16-02, F16-03)"
  - "Q1FY26/FY26 Ind AS comparatives management-converted, NOT limited-reviewed (F7-01); deck's 38/22/18% optics rest on the same unreviewed base"
  - "Consolidated P&L promised in cover letter but absent from deck (F16-04); Nuo Zhan HK nil-revenue unaudited shell (F3-01)"
  - "New subsidiary Macfos Electronics Pvt Ltd - likely Robu 2.0 assembly vehicle, never named in deck (F15-01, F16-06); possible trading-to-assembly drift"
  - "PAT quality: ~60% of YoY PAT growth from Other Income +85%; core operating PBT +11.36% vs reported PAT +17.15%"
  - "Mainboard listing red line due Q2 FY27 - no announcement in EITHER document (F16-07)"
  - "Governance hygiene: 256 vs 257.68 Cr FY24-25 turnover, 18% vs 17.15% PAT growth, Q1 TY-not-FY title typo, asterisk inconsistencies (F14-01); statutory-liability/MSME/litigation items no values, no explicit Nil (F13-02)"
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/review_mcfos_q1fy27.md"
```
