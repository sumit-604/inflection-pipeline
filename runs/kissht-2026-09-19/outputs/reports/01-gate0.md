# STAGE 1 — GATE 0 SCORECARD: KISSHT (OnEMI Technology Solutions Ltd)

Run date: 2026-09-19
Data available: 6 years (FY21 to FY26). Scoring adapted to 6-year history.
Archetype: Lender (NBFC-ML, digital unsecured personal loans, subsidiary Si Creva Capital Services Pvt Ltd). Consolidated basis used throughout unless stated (screener CFO figures cross-checked exactly against AR/RHP consolidated cash flow statements — see Data Basis Note).

## DATA BASIS NOTE (read before the scores)

1. **Units.** Screener CSV is in Rs Cr. Results/AR/RHP statements are in Rs million (10 million = 1 crore). Every million figure below is shown converted to Cr with the conversion visible.
2. **Consolidation check.** Screener CFO for FY26 (-460.82 Cr) and FY25 (-661.43 Cr) match the AR/RHP consolidated cash flow statements exactly (-4,608.21 million and -6,614.26 million respectively). Screener FY24 CFO (-637.43 Cr) matches RHP restated consolidated FY24 (-6,374.33 million) exactly. **Screener FY23 CFO (48.36 Cr) does NOT match RHP restated consolidated FY23 (111.478 Cr / 1,114.78 million)** — a 2.3x gap, source unreconciled in the provided corpus. Treated as an open data-quality flag (see FLAG-DATA-CONFLICT below); screener's own FY23 figure is retained for the 6-year B1 cumulative calc (single consistent source), while the matched RHP CFO+capex pair is used for the FY23 FCF calc in B2/B3 (see there).
3. **ROCE for a lender.** The prompt's fixed formula is EBIT ÷ (Total Assets − Current Liabilities). For a lender, "Finance cost" (cost of borrowed funds) is the core cost of the lending business, not an overhead layer sitting below EBIT the way it is for a manufacturer — the framework's own Block D already recognises this by swapping CAR/PCR in for Net-Debt/EBITDA and Interest-Coverage. Block A carries no such explicit swap for A1/A2/A4. Per the run instruction ("score what the evidence supports, state the adaptation, never estimate"), ROCE is computed literally (EBIT = PBT + Finance cost; Capital Employed = Total Assets − Current Liabilities, both taken from the AR/RHP consolidated balance sheets, which carry a genuine current/non-current split) for the four years where that split exists (FY23-FY26; FY21-FY22 balance sheets in the screener do not split current liabilities, so ROCE for those two years is NOT FOUND). **Caveat: because Finance cost is added back, this ROCE overstates capital efficiency in the way a manufacturer's ROCE would not, since AUM growth mechanically inflates the "EBIT" numerator. Treat A1/A2/A4 as directional, not comparable outside the lender archetype.**
4. **"EBITDA margin" for moat tests M1/M2/M9.** The naive (PBT+Interest+Depreciation)/Sales proxy suffers the identical distortion as (3) above and was checked against the AR's own disclosed Cost-to-Income Ratio (a like-for-like lender efficiency metric, FY24-FY26 only). The two series point in OPPOSITE directions (naive margin "improves" 23.1%→33.5%; Cost-to-Income actually WORSENS 45.54%→56.64%, i.e. real margin proxy falls 45.46%→43.36%). The Cost-to-Income basis is used for M1 as the more evidenced measure; this is itself a finding, not just a methodology footnote.
5. **Working-capital-days tests (B4, M10, M12)** are weak proxies for a lender: the loan book, the actual balance-sheet driver, sits outside trade receivables/payables. Scored per the literal formula and available data, with the archetype mismatch stated at each line.

---

## [BLOCK A: RETURN ON CAPITAL] — 18 / 20

| Metric | Value | Score | Anchor |
|---|---|---|---|
| A1 Median ROCE (FY23-FY26, computed) | 30.93% | 5 | computed: EBIT=PBT+Finance cost, Capital Employed=TA-CL. FY23 12.67%, FY25 28.93%, FY24 33.12%, FY26 32.93% (AR consolidated BS p.98 [FY26/FY25]; RHP restated consolidated BS p.267 [FY24/FY23]; PBT & Finance cost from AR consolidated CF p.99 and RHP restated consolidated CF p.271) |
| A2 Minimum single-year ROCE | 12.67% (FY23) | 3 | same anchors as A1 |
| A3 Median ROE (FY21-FY26) | 20.86% | 5 | FY23 6.93%, FY24 28.78%, FY25 17.74% (company-reported, AR p.10 KPI table & RHP p.132/p.43 restated KPI table); FY26 23.97% (AR p.10); FY21 -36.39%, FY22 31.66% computed from screener PAT/net worth (screener-data; FY21 uses closing net worth, opening unavailable) |
| A4 ROCE trend, latest (FY26 32.93%) vs earliest available (FY23 12.67%) | +20.3pp | 5 | same anchors as A1 |

Note: A1/A2/A4 data years are FY23-FY26 only (FY21-FY22 lack a current/non-current balance-sheet split in any provided source — NOT FOUND). A3 uses all 6 years. See Data Basis Note (3) on the ROCE caveat for a lender.

## [BLOCK B: CASH GENERATION QUALITY] — 0 / 20

| Metric | Value | Score | Anchor |
|---|---|---|---|
| B1 Cumulative CFO ÷ Cumulative PAT (FY21-FY26) | -1,648.00 Cr ÷ 671.20 Cr = -2.46x | 0 | screener-data (CFO: 78.95, -15.63, 48.36, -637.43, -661.43, -460.82 Cr FY21-26; PAT: -58.45, 62.62, 27.67, 197.29, 160.62, 281.45 Cr FY21-26) |
| B2 FCF-positive years ÷ years with data | 1 of 4 (25%), FY23-FY26 only | 0 | FCF = CFO - Capex. Capex NOT in screener; capex FY23 -9.105 Cr, FY24 -3.042 Cr, FY25 -7.746 Cr, FY26 -10.237 Cr (RHP restated consolidated CF p.271 for FY23-25; AR consolidated CF p.99 for FY26). FY23 FCF +102.37 Cr (RHP's own matched CFO 111.48 Cr, not screener's 48.36 Cr — see Data Basis Note 2); FY24 -640.48 Cr; FY25 -669.17 Cr; FY26 -471.06 Cr. FY21-FY22 capex NOT FOUND (RHP restated data starts FY23) |
| B3 Cumulative FCF ÷ Cumulative PAT (FY23-FY26 window, the only years with matched FCF data) | -1,678.33 Cr ÷ 667.03 Cr = -2.52x | 0 | same FCF figures as B2; PAT FY23-26 screener-data 27.67+197.29+160.62+281.45=667.03 Cr |
| B4 Change in WC Days, latest vs earliest | NOT FOUND (archetype/data gap) | 0 | Trade Payables not in screener at all; AR/RHP payables data starts FY25 (AR consolidated BS p.98) / partially FY23 onward — no FY21 payables anywhere, so the required latest-vs-earliest comparison cannot be built. WC days are also a weak proxy for a lender (the loan book, not trade receivables/payables, is the real balance-sheet driver) — see Data Basis Note (5) |

**block_b_trend: improving but still deeply negative.** CFO narrowed from -661.43 Cr (FY25) to -460.82 Cr (FY26) (screener-data), a 30% reduction in cash burn, consistent with AUM growth normalising post-listing. This is a structural feature of a growing lender (loan disbursals classify as operating cash outflow under Ind AS 7, indirect method — visible in the AR/RHP cash flow statements as the "(Increase)/decrease in loans & advances" working-capital line, e.g. -15,621.28 million in FY26 alone, AR consolidated CF p.99) — not, on its own, a going-concern cash-quality failure the way it would be for a manufacturer. The mechanical score does not distinguish the two; this note is the distinguishing context for downstream stages.

## [BLOCK C: GROWTH] — 8 / 20

| Metric | Value | Score | Anchor |
|---|---|---|---|
| C1 Revenue CAGR (FY21-FY26, 5yr) | 66.02% (175.02 Cr → 2,208.81 Cr) | 5 | screener-data |
| C2 PAT CAGR (FY21-FY26) | N/M (negative endpoint) | 0 | screener-data; FY21 PAT -58.45 Cr is negative. Loss-to-profit swing, FY21 to FY22 (-58.45 Cr → +62.62 Cr) |
| C3 Positive YoY revenue years | 4 of 5 (80%) | 3 | screener-data. FY21→22 +195%, FY22→23 +94%, FY23→24 +70%, FY24→25 **-20.4%** (1,700.0→1,352.49 Cr), FY25→26 +63.3% |
| C4 PAT CAGR minus Revenue CAGR | N/M → 0 per rule (C2 is N/M) | 0 | per CAGR edge rule: "For C4 when PAT CAGR is N/M, score C4=0" |

## [BLOCK D: BALANCE SHEET STRENGTH] (financials variant) — 17 / 20

| Metric | Value | Score | Anchor |
|---|---|---|---|
| D1 CRAR (NBFC substitute for Net Debt/EBITDA) | 25.28% (FY26) | 5 | AR p.10 KPI table (line "Capital to Risk Weighted Asset Ratio (%) 25.28% / 25.18% / 25.77%" FY26/FY25/FY24); AR p.35 MD&A narrative confirms "CRAR stood at 25.28%, Tier-I 24.40%" |
| D2 PCR (NBFC substitute for Interest Coverage) | 86.15% (FY26) | 5 | AR p.10 KPI table ("Provisioning Coverage Ratio (%) 86.15% / 91.48% / 100.00%" FY26/FY25/FY24) |
| D3 Debt/Equity — financials default | 3 (rule default) | 3 | rule: "Financials: default 3." Actual FY26 D/E = 1.78x (AR p.10 and p.35, up from 1.50x FY25, 0.97x FY24) shown for context, not scored |
| D4 Current Ratio (latest, FY26) | 1.572x (Rs 31,251.23m current assets ÷ Rs 19,876.56m current liabilities) | 4 | AR consolidated balance sheet p.98 (this NBFC presents a classified current/non-current balance sheet, so the literal test is computable) |

## [BLOCK E: SHAREHOLDER ALIGNMENT] — 8 / 20

| Metric | Value | Score | Anchor |
|---|---|---|---|
| E1 Promoter holding (latest quarter, Jun-2026) | 24.80% | 0 | BSE shareholding summary, Jun-2026 (inputs/shareholding/BSE-shareholding-summary-Jun2026.txt); Promoter & Promoter Group, 2 holders, 4,17,85,126 shares = 24.80% |
| E2 Promoter holding change over 3 years | NOT FOUND | 0 | Company listed 08-May-2026; only one post-listing shareholding statement exists (Jun-2026). No 3-year listed trend is constructible; pre-IPO holding is not like-for-like (different share base, private company) |
| E3 Promoter pledge (latest) | 0% | 5 | BSE shareholding summary, Jun-2026: "Whether any shares held by promoters are pledge or otherwise encumbered? No" |
| E4 Contingent Liabilities ÷ Net Worth (latest, FY26) | 103.29 Cr ÷ 1,342.78 Cr = 7.69% | 3 | AR Note 36, consolidated, p.123 (sum of: income tax appeals/demands 71.46m, GST appeals/demands 135.94m, guarantee under BC arrangements 825.49m = 1,032.89m total; capital commitments of 12.39m excluded as not a contingent liability); Net worth FY26 1,343 Cr per AR p.10 KPI table |

Note: the corporate guarantee of Rs 21,982.06 million the Holding Company has given for subsidiary borrowings is NOT added to E4's numerator — the AR note states it is "recognised in the consolidated financial statements," i.e. already on the consolidated balance sheet, not an off-balance-sheet contingent item at the group level (AR Note 36, p.123).

FII/DII split: NOT FOUND (BSE shareholding summary does not break out FII/DII within "Public"; carried forward from B00 input gaps as an open UA institutional-ownership qualifier for a later stage, not scored here).

---

## CORE SCORE: 51 / 100

Block totals: A=18, B=0, C=8, D=17, E=8.
**Strongest block: A (Return on Capital), 18/20 (90%).**
**Weakest block: B (Cash Generation Quality), 0/20 (0%).**

---

## [BLOCK F: QUANTITATIVE MOAT SCORING] — 4 / 60

| Test | Score | Basis / Anchor |
|---|---|---|
| M1 Pricing Power | 0 | Using Cost-to-Income Ratio (100% minus C/I) as the evidenced margin proxy for a lender (see Data Basis Note 4): margin FELL from 54.46% (FY24) to 43.36% (FY26), a decline of 11.1pp — worse than the -5pp floor for even the "1" tier. Revenue CAGR FY24-26 was 14.01% (screener-data), ≥10% but margin direction fails every tier except "else 0." AR p.10 KPI table (Cost to Income Ratio 56.64%/54.30%/45.54% FY26/FY25/FY24) |
| M2 Cost Advantage vs peer median | 0 | Proxy margin (PBT+Interest+Depreciation)/Sales, FY26: KISSHT 33.46% vs peer median 58.74% (POONAWALLA 52.79%, UGROCAP 64.69% — screener-data for both). KISSHT sits 25.3pp BELOW peer median → "below" tier. Caveat: business mix differs materially (Poonawalla/UGRO are secured SME/consumer NBFCs; KISSHT is unsecured digital personal loans); UGROCAP peer data is one year only (FY26) |
| M3 Capital Efficiency (FAT x ROCE) | 0 | Fixed Asset Turnover is not a meaningful capital-efficiency measure for a lender (capital employed is the loan book, not PP&E — Net Block is only Rs 43.01 Cr against Rs 2,208.81 Cr revenue, screener-data, which would produce a nonsensical 51x FAT). Archetype mismatch, scored 0 |
| M4 Customer Stickiness | 3 | 1 revenue-decline year (FY24→FY25) out of 5 YoY periods, fully recovered by FY26 (2,208.81 Cr > 1,700.0 Cr) — matches "max 1 decline year, fully recovered = 3" tier exactly; no receivable-days sub-condition required at this tier |
| M5 Scale & Dominance | 0 (PEER DATA NEEDED) | KISSHT mcap Rs 6,311.67 Cr (screener-data) vs POONAWALLA Rs 42,214.8 Cr and UGROCAP Rs 1,300.38 Cr (screener-data); SBICARD mcap NOT FOUND (no Data_Sheet CSV, per B00 input gaps). The RHP's own competitive set (Bajaj Finance, Cholamandalam, HDB Financial, SBI Cards) is broader than the 3 peers with any screening data here — insufficient to rank KISSHT's true segment position |
| M6 Technology / R&D | 0 | R&D/Revenue NOT FOUND — no R&D line exists in the screener P&L template, and no segregated technology-spend % is disclosed in AR/RHP/results for this run |
| M7 Regulatory / License | 1 | NBFC-ML is RBI-regulated (real licence requirement), but more than 10 listed NBFC/digital-lending peers exist in India (Bajaj Finance, Poonawalla, UGRO, Chola, L&T Finance, IIFL Finance, Piramal, Aditya Birla Capital, SBI Cards, Muthoot, Manappuram, HDB Financial, MAS Financial, Fusion, CreditAccess Grameen, Five Star, Aavas, Home First — named per RHP's own competitive benchmarking, p.132 area, and general market knowledge) → "regulated but >10 players = 1" tier |
| M8 Distribution | 0 | Business is described as a digital lender, no physical branch/outlet network in the provided evidence → "none or purely digital = 0" per the test's own explicit tier |
| M9 Brand (GM proxy) | 0 | Same proxy-margin basis as M2: KISSHT 33.46% vs peer median 58.74%, at/below → 0 |
| M10 Switching Costs | 0 | Revenue growth in 4 of 5 years (1 decline year), but receivable days ROSE from 1.71 (FY21) to 17.24 (FY26) (+15.5 days, screener-data receivables ÷ revenue × 365) — fails the "AND stable" condition needed for the 3-tier; does not reach the "2+ decline years" needed for the 1-tier either → else 0. Caveat: trade receivables are not the loan book for a lender (Data Basis Note 5) |
| M11 Network Effects (6-year two-window test available) | 0 | Prior 3yr-window revenue CAGR (FY21→FY23, 2yr span) = 139.0%; latest 3yr-window (FY24→FY26, 2yr span) = 14.01% (screener-data) — latest is NOT greater than prior (deceleration off a much larger base), and latest CAGR is below the 15%/20% thresholds for the lower tiers. Selling & admin expense as % of sales also ROSE FY25→FY26 (23.32%→26.19%, screener-data), reinforcing 0 either way |
| M12 Negative WC / Float | 0 | WC days computable only for FY25-FY26 (Trade Payables first appears in AR p.98 for those two years: FY26 104.84 Cr, FY25 52.20 Cr); no consistent 6-year series exists, and this is a weak float proxy for a lender regardless (Data Basis Note 5) — archetype mismatch, scored 0 |

**Moat classification: 1 test present (M4, score ≥3) → THIN.**

---

## CLASSIFICATION

**Core score: 51/100** (band: 40-59)
**Moat class: THIN**
**Data confidence: 6 years (FY21-FY26) → "5-6, lower — may not have seen a full credit cycle."** No tier downgrade applies (downgrade rule triggers only at 3-4 years); this is a flag, not a score adjustment. The company listed 08-May-2026 and this run has never seen it through a full credit-cost or funding-cost cycle as a standalone listed entity.

**Classification matrix: Core 40-59 → AVERAGE** (moat tier does not further split this band).

**Deal-breaker overrides fired (both recorded; neither changes the outcome below AVERAGE, since AVERAGE already sits at the classification matrix's floor for this Core band):**
1. Block A <8 → max GOOD: **did NOT fire** (Block A = 18)
2. Block B <8 → max GOOD: **FIRED** (Block B = 0)
3. Median ROCE <10% → max AVERAGE: **did NOT fire** (median ROCE = 30.93%)
4. Cumulative CFO/PAT <0.50 → max AVERAGE: **FIRED** (ratio = -2.46x)
5. Pledge >15% → max AVERAGE: **did NOT fire** (pledge = 0%)
6. ND/EBITDA >3x AND IC <3x → AVOID: **did NOT fire** (NBFC substitutes CAR 25.28% and PCR 86.15% are both healthy; the literal ND/EBITDA test does not apply to this archetype)
7. Revenue declined in majority of years → max AVERAGE: **did NOT fire** (1 of 5 YoY periods declined, not a majority)
8. PAT negative in any of last 3 years → max AVERAGE: **did NOT fire** (FY24/25/26 PAT all positive: 197.29/160.62/281.45 Cr)
9. History <3 years → AVERAGE: **did NOT fire** (6 years of data)

## CLASSIFICATION: **AVERAGE**

## DECISION LINE

Gate 0 mechanical score is AVERAGE (Core 51/100, moat THIN). The two active depressors are both archetype-driven, not evidence of operating decay: Block B (cash generation) scores 0 because a fast-growing lender's loan disbursals classify as operating cash outflow under Ind AS 7, and Block A's headline strength (18/20) is itself inflated by the same lender mechanic working in the other direction on the ROCE numerator (Finance cost added back). The one clean red flag independent of archetype mechanics is the Cost-to-Income deterioration (45.54%→56.64%, FY24-26) sitting underneath a rising PAT — a genuine efficiency question for later stages, not explainable by the accounting-classification issues above. Gate 0 does not halt; flags propagate per CLAUDE.md.

---

```yaml
stage: B01-gate0
company: "KISSHT"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
input_gaps:
  - "A1/A2/A4 ROCE: FY21-FY22 NOT FOUND (screener balance sheet does not split current/non-current liabilities for those years; AR/RHP restated data starts FY23)"
  - "B2/B3 FCF: FY21-FY22 capex NOT FOUND (RHP restated cash flow data starts FY23; screener carries no capex/PPE-purchase line at all)"
  - "B4 WC days change: NOT FOUND (no FY21 trade payables anywhere in the corpus; AR/RHP payables data starts FY23 at the earliest, full breakout only FY25-26)"
  - "E2 promoter holding change over 3 years: NOT FOUND (company listed 08-May-2026; only one post-listing shareholding statement, Jun-2026, exists)"
  - "E1 FII/DII split within Public shareholding: NOT FOUND (BSE shareholding summary gives Promoter 24.80% / Public 75.20% only, no institutional sub-split)"
  - "M5 scale/dominance: SBICARD market cap NOT FOUND (no Data_Sheet CSV collected for this peer)"
  - "M6 R&D/Revenue: NOT FOUND (no R&D line in any provided source for this company)"
  - "FY23 CFO conflict unresolved: screener 48.36 Cr vs RHP restated consolidated 111.48 Cr (2.3x apart); no source in the corpus reconciles the two"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVERAGE (Core 51/100). Historical depressors are archetype-driven: Block B (cash generation, 0/20) is depressed because AUM growth classifies as operating cash outflow under Ind AS 7 for a fast-growing lender, not going-concern distress. Block A (18/20) is inflated by the same mechanic in reverse (Finance cost added back into the ROCE numerator). Net effect roughly cancels at the Core-score level but both should be read through the lender lens downstream, not at face value."}
  - {type: FLAG-CASH, reason: "Cumulative CFO FY21-26 -1,648.00 Cr vs cumulative PAT +671.20 Cr (screener-data), ratio -2.46x. Trend improving FY25->FY26 (-661.43 Cr to -460.82 Cr) but still deeply negative. Needs the Section 1B lender cash-conversion protocol at a later stage, not a manufacturer cash-quality read."}
  - {type: FLAG-DATA-CONFLICT, reason: "FY23 consolidated CFO: screener shows 48.36 Cr, RHP restated consolidated cash flow statement (p.271) shows 111.48 Cr (1,114.78 million). All other years (FY24-26) reconcile exactly between screener and RHP/AR. Unresolved in the provided corpus; flagged for verification."}
  - {type: FLAG-QUALITY, reason: "Cost-to-Income Ratio worsened from 45.54% (FY24) to 56.64% (FY26) even as PAT grew (AR p.10 KPI table) — a genuine operating-efficiency question, independent of the cash-flow-classification and ROCE-inflation mechanics named above. Not explainable by archetype accounting quirks; worth a direct look at opex/credit-cost drivers downstream."}
data_years: 6
fy_range: "FY21 to FY26"
blocks: {A: 18, B: 0, C: 8, D: 17, E: 8}
core_score: 51
moat_score: 4
grand_total: 55
moats_confirmed: 1
moat_class: "THIN"
classification: "AVERAGE"
deal_breakers:
  - "Block B <8 -> max GOOD (fired; Block B = 0; superseded by the stricter cap below)"
  - "Cumulative CFO/PAT <0.50 -> max AVERAGE (fired; ratio = -2.46x; this is the binding cap, though the Core-score band (40-59) already places the run at AVERAGE independent of this deal-breaker)"
history_downgrade: false
data_notes:
  - "Loss-to-profit swing, FY21 to FY22 (PAT -58.45 Cr to +62.62 Cr, screener-data); no synthetic PAT CAGR attempted (C2/C4 = 0 per the CAGR edge rule)."
  - "ROCE (A1/A2/A4) computed as EBIT (PBT + Finance cost) / (Total Assets - Current Liabilities) from AR/RHP consolidated balance sheets, FY23-FY26 only. Caveat: Finance cost is the core cost of funds for a lender, not overhead; this measure is directionally useful but structurally inflated relative to a manufacturer's ROCE and should not be compared across archetypes."
  - "Moat tests M1/M2/M9 initially computed with a naive (PBT+Interest+Depreciation)/Sales margin proxy, which is inflated by the same mechanic as the ROCE caveat above. Cross-checked against the AR's own disclosed Cost-to-Income Ratio (FY24-26): the two series point in opposite directions. M1 uses the Cost-to-Income basis as the more evidenced measure; M2/M9 retain the naive proxy only for the peer cross-section (POONAWALLA, UGROCAP) since no peer discloses Cost-to-Income in the data provided, and note the resulting basis mismatch explicitly."
  - "Promoter & Promoter Group is 2 identified holders at 24.80% (BSE shareholding, Jun-2026) - not a 'no identified promoter' company, so the professionally-managed FII+DII>50% alternate for E1 does not apply."
  - "WC-days-based tests (B4, M10, M12) are weak proxies for a lender since the loan book, not trade receivables/payables, is the real balance-sheet driver; scored per the literal formula and available data with the mismatch stated at each line."
block_b_trend: "improving (CFO -661.43 Cr FY25 to -460.82 Cr FY26, screener-data; still deeply net negative, driven by loan-book growth classified as an operating outflow under Ind AS 7, not by a cash-quality failure in the manufacturer sense)"
analyst_note: >
  Core 51/AVERAGE is a real mechanical outcome, but two of its drivers point
  the same direction for the same reason and roughly cancel: Block A's 18/20
  and Block B's 0/20 both trace to Finance cost/loan-disbursal accounting
  quirks unique to a fast-growing lender, not to independent evidence of
  quality or distress. Downstream stages should not read Block A as proof
  of strong capital efficiency, nor Block B as proof of cash-quality failure,
  without the Section 1B lender variant re-testing both. The one flag that
  is NOT an archetype artefact is the Cost-to-Income deterioration
  (45.54% to 56.64%, FY24-26) under a rising PAT - that is worth a direct
  look. Deal-breaker 4 (cumulative CFO/PAT) and deal-breaker 2 (Block B<8)
  both fired but are non-binding here since the Core-score band (40-59)
  already floors the classification at AVERAGE. FY23 CFO has an unresolved
  2.3x conflict between screener and the RHP restated statement; every other
  year reconciles exactly.
```
