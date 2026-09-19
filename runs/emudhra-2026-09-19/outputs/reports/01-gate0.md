# Stage 1 — Gate 0 Scorecard: eMudhra Ltd (EMUDHRA)

Run date: 2026-09-19
Data available: 8 years (FY19 to FY26). Scoring adapted to 8-year history.
Units: screener Data_Sheet figures are INR Cr. AR/results figures cited
separately are INR Million (source states unit on the face of the
document; no silent conversion — Mn values are marked Mn throughout).

## CORRECTION 2 (Verifier C), 2026-09-19

Verifier C (phase-1 framework audit, 12c-verifier-c-phase1.md) found one
CRITICAL and several MINOR/MAJOR issues in the corrected-1 draft. Each
item below was re-checked against the source directly (mupdf extraction
of the AR) before being applied.

**1. CRITICAL — B4/M12, consolidated trade payables.** Verified: AR
p.216 (consolidated balance sheet, mupdf, clean) and Note 18, AR p.255
(mupdf, clean) both print Trade payables Total = **Rs 600.92 Mn (FY26)
/ Rs 314.34 Mn (FY25)**. The prior draft's claim that this figure was
"not reliably extractable" was WRONG — it was extractable, just not
from the pdftotext-layout extraction this stage used; the mupdf
extraction resolves it cleanly. Retracted. WC days now computed (see
Block B):
- FY26: Receivable days 98.44d (1,892.13/7,015.8×365) + Inventory days
  2.03d (39.00/7,015.8×365) − Payable days 31.26d (600.92/7,015.8×365)
  = **69.21d**
- FY25: Receivable days 102.23d (1,454.67/5,193.9×365) + Inventory days
  0.98d (13.99/5,193.9×365) − Payable days 22.09d (314.34/5,193.9×365)
  = **81.12d**
- Change FY25→FY26 = **-11.91 days** ("decreased >5 days") → **B4 = 5**
  (was 0, N/A)
- M12: both years >45d, majority >45d → **M12 = 0** (score unchanged;
  label corrected from N/A to a real computed value)

**2. WINDOW CONVENTION (B2, B3, B4).** The prior draft accepted a
two-year window (FY25-FY26) for B2/B3 but rejected it for B4 on the
retracted "not extractable" premise — an inconsistent application, per
Verifier C correctly flagged as decision-changing. prompts/01 is silent
on whether a Block B sub-metric may score on fewer than 3 years when the
full 8-year window is not extractable; **this needs an operator
ruling.** Per the coordinator's instruction, this report FILES the score
under the two-year-window-accepted convention (applied consistently to
B2, B3 AND B4 alike) and separately states the alternative (window
rejected for all three) as pending ruling:

| Reading | B1 | B2 | B3 | B4 | Block B | Core | Classification |
|---|---|---|---|---|---|---|---|
| **FILED: n=2 window accepted for B2-B4** | 5 | 2 | 0 | 5 | **12** | **74** | **GOOD+** |
| ALTERNATIVE: n=2 window rejected for B2-B4 alike (pending operator ruling) | 5 | 0 | 0 | 0 | 5 | 67 | GOOD (deal-breaker #2) |

**3. MAJOR — A2 min ROCE, mixed basis.** The prior draft used computed
ROCE for FY19-FY23 and AR-disclosed ROCE (AR p.57) for FY24-FY26, and
the minimum landed exactly on the disclosed FY26 figure (15.0%), right
on the ≥15% score-5 edge. Corrected to ONE basis, computed, for all 8
years (Capital Employed = Equity + Reserves + Borrowings, screener-data,
same method throughout): FY24 ROCE = 14.41%, FY25 = 14.56%, FY26 =
14.51%. Minimum = **14.41% (FY24)** → band 12-14.9% → **A2 = 3** (was
5). A1 median on the consistent basis is unchanged at 18.05% → still
3. A3 median ROE on the consistent computed basis is unchanged at
18.675% → still 4 (computed FY24-26 ROE 14.33/12.08/13.01% gives the
same median as the disclosed figures did). A4 trend on the consistent
basis: 14.51% (FY26) vs 20.99% (FY19) = -6.48pp (was -5.99pp) → still
band >5pp decline → still 0. **Block A: 3+3+4+0 = 10** (was 12).
AR-disclosed ROCE/RoE (p.57) are kept in the table below as a
cross-check only, not scored.

**4. MINOR items, all verified, scores unchanged, inputs corrected:**
- **D1**: prior draft used screener-data Cash & Bank Rs 107.31 Cr for
  FY26 — that is actually the **FY25** column (screener row is 8 values
  FY19→FY26; position 7 = FY25 = 107.31, position 8 = FY26 = 65.20,
  confirmed against AR p.216: Cash and cash equivalents 582.33 Mn + Bank
  balances 69.71 Mn = 652.04 Mn = Rs 65.20 Cr). Corrected: Net cash =
  Borrowings 28.78 − Cash 65.20 = **-36.42 Cr (net cash)**, was -78.53
  Cr. Still net cash → **D1 = 5, unchanged.**
- **D4**: prior draft used the standalone current ratio (2.90x, AR Note
  50) because the consolidated split was believed unextractable — same
  false premise as B4. Consolidated is clean (AR p.216, mupdf): Total
  current assets 4,355.64 Mn / Total current liabilities 1,578.00 Mn =
  **2.76x**. Still ≥2.0x → **D4 = 5, unchanged; basis corrected to
  consolidated.**
- **M1/M2/M5 EBITDA**: prior draft's EBITDA formula had the Change in
  Inventory sign reversed. Cross-check (EBITDA + Other Income −
  Depreciation − Interest must equal PBT) confirms the correct
  convention subtracts Change in Inventory as reported, not adds it.
  Corrected FY19 EBITDA = Rs 32.21 Cr (31.72% margin, cross-checks
  exactly to PBT Rs 21.65 Cr); FY26 EBITDA = **Rs 159.12 Cr (22.68%
  margin**, was 21.97%; cross-checks exactly to PBT Rs 131.31 Cr).
  Decline FY19→FY26 = 9.04pp (was 9.86pp) — still exceeds the 2-5pp
  band → **M1 = 0, unchanged.** Peer median EBITDA margin recomputed
  with the same fix (QUICKHEAL FY26 -11.25%, was -11.54%; NEWGEN/PROTEAN
  unaffected, both report zero Change in Inventory) → median still
  11.58% (PROTEAN, middle of three) → eMudhra +11.10pp above → **M2 = 5,
  unchanged.** eMudhra still ranks 2nd of 4 on margin → **M5 = 3,
  unchanged.**

Net effect of Correction 2: Block A 12→10, Block B 13→12 (filed
reading), F unchanged at 17 (M1/M12 relabelled/refigured, scores
unchanged). Core 71→74 (filed reading). Grand total 88→91. Deal-breaker
#2 no longer triggers under the filed reading (Block B = 12, above the
8-point floor). **Classification: GOOD+ (filed reading), GOOD if the
operator rules against the two-year window for B2-B4 (see table above).**

## CORRECTION 1, 2026-09-19 (superseded in part by Correction 2 above)

The original draft of this report misread FY26 capex. It used Rs 814.21
Mn — the MD&A prose's "mainly includes" subset (product development Rs
124.62 Mn + new product development Rs 476.38 Mn + Data Center/Server Rs
213.21 Mn, AR p.156) — as if it were the FULL "Purchase of Property,
plant and equipment and Intangible assets" line from the cash flow
statement. It is not; it is a partial narrative breakdown of a larger
line.

The clean mupdf extraction of the Consolidated Cash Flow Statement, AR
p.218, gives the actual line:
- Purchase of Property, plant and equipment and Intangible assets:
  **Rs 1,853.68 Mn (FY26) / Rs 832.02 Mn (FY25)**
- Payment towards acquisition of business (net of assets acquired), a
  SEPARATE line, correctly excluded from capex per the FCF formula:
  Rs 629.03 Mn (FY26) / Rs 743.23 Mn (FY25)
- Net cash from operating activities: Rs 1,328.49 Mn (FY26) / Rs
  1,016.16 Mn (FY25) — matches screener-data exactly.

**Corrected FY26 FCF = 1,328.49 − 1,853.68 = -Rs 525.19 Mn (-Rs 52.52
Cr)**, was reported as +Rs 51.43 Cr. **Corrected FY25 FCF = 1,016.16 −
832.02 = +Rs 184.14 Mn (+Rs 18.41 Cr).** This matches the operator's
original load-bearing fact (-Rs 52 Cr) and Stage 3's independent
reading. B2/B3 figures from Correction 1 remain the correct FCF
readings; Correction 2 above only changes whether B2/B3's two-year
window is also applied to B4, and fixes A2/D1/D4/M1 on separate issues.

## LOAD-BEARING FACTS CHECK (companies/EMUDHRA.md, first verification priority)

1. **ORGANIC GROWTH vs GUIDANCE** — out of scope for this quantitative
   scorecard (needs segment/organic-vs-acquired revenue split not present
   in the screener Data_Sheet or Block A-F formulas). Flagged for stage 2+.
2. **CASH CONVERSION** ("FY26 FCF Rs -52 Cr; days payable 420 vs debtor
   days 98") — FCF CONFIRMED (FY26 -Rs 52.52 Cr, matches). Payable days:
   CONFIRMED via Note 18 (AR p.255, consolidated) at Rs 600.92 Mn FY26 →
   **31.26 payable days** (Receivables/Sales×365 basis) — NOT 420 days.
   The "420 days" load-bearing claim does not reproduce on the trade
   payables balance and most likely conflated trade payables with the
   Rs 881.16 Mn non-current "payable for acquisition of business —
   contingent consideration" (AR p.216/255, a Cryptas-related earn-out
   liability, not a trade payable). Debtor days (98.44d FY26 on this
   formula, close to the load-bearing fact's "98") DO reproduce cleanly.
   Flag for downstream: the "420 days payable" claim should be corrected
   or retracted in company memory.
3. **3i INFOTECH CLAIM** — AR Note 36 (Contingent Liabilities, p.264-265,
   consolidated) quantifies contingent liabilities at only Rs 34.55 Mn
   (Rs 3.46 Cr: income-tax appeal Rs 32.29 Mn + GST appeal Rs 1.48 Mn).
   The 3i Infotech claim (>Rs 128 Cr) is disclosed only as narrative Note
   36(f), NOT included in the quantified total — the company disputes it
   in full. E4 (contingent liabilities/net worth) is scored on the
   quantified figure per the standard note, which structurally excludes
   this disputed claim; see the E4 flag below.
4. **ASSET BUILD** (fixed assets Rs 419 Cr to Rs 727 Cr) — confirmed
   directionally (screener Net Block + CWIP). The full FY26 capex line
   is confirmed clean at Rs 1,853.68 Mn (AR p.218, see Correction 1
   above). The MD&A prose (AR p.156) itemises only Rs 814.21 Mn of that
   total (product development + Data Center/Server); the remaining ~Rs
   1,039 Mn is not broken out in the narrative and could not be split
   between acquired intangibles, goodwill-adjacent capitalisation, and
   other PPE/intangible additions from the provided corpus. Separately,
   the Rs 629.03 Mn (FY26) acquisition-of-business payment (net of
   assets acquired) is its own line, correctly excluded from capex.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 10/20 (was 12/20, CORRECTED, see Correction 2 item 3)

Methodology note: screener's own ROCE/ROE ratios were not in the
provided data (Customization sheet came out empty per B00). Computed
for ALL 8 years — one consistent basis, per Verifier C — using Capital
Employed = Equity Share Capital + Reserves + Borrowings (screener's
4-bucket Data_Sheet model; Total Assets − Other Liabilities, since a
reliable current/non-current liability split from the balance sheet
alone, independent of the borrowings/equity buckets, was not attempted
here — see data_notes). AR-disclosed consolidated ROCE/RoE (AR p.57,
"Return ratios" chart, FY24-FY26 only) is shown as a cross-check, NOT
scored, to keep one basis across the full 8-year series.

| Year | EBIT (PBT+Interest, Cr) | Capital Employed (Cr) | ROCE (computed, scored) | ROCE (AR-disclosed, cross-check only) |
|---|---|---|---|---|
| FY19 | 21.91 | 104.37 | 20.99% | — |
| FY20 | 23.69 | 133.92 | 17.69% | — |
| FY21 | 32.02 | 158.68 | 20.18% | — |
| FY22 | 55.02 | 219.94 | 25.02% | — |
| FY23 | 76.76 | 416.92 | 18.41% | — |
| FY24 | 95.67 | 663.93 | 14.41% | 19.5% (AR p.57) |
| FY25 | 108.55 | 745.32 | 14.56% | 18.2% (AR p.57) |
| FY26 | 136.38 | 939.91 | 14.51% | 15.0% (AR p.57) |

**A1 Median ROCE** = 18.05% (avg of 4th/5th of 8 sorted computed values:
17.69, 18.41) → band 15-19.9% → **score 3**
**A2 Minimum single-year ROCE** = **14.41% (FY24, computed)** → band
12-14.9% → **score 3** (was 5 on the mixed-basis 15.0% AR-disclosed
figure)
**A3 Median ROE** = 18.675% (see table below) → band 15-19.9% → **score
4**
**A4 ROCE trend, latest vs earliest** = 14.51% (FY26, computed) vs
20.99% (FY19, computed) = decline of 6.48pp → band decline >5pp →
**score 0**

ROE table (Net Worth = Equity Capital + Reserves, screener-data; FY19
uses closing net worth only, opening not available, stated per
protocol; all 8 years computed, one basis):

| Year | PAT (Cr) | Avg Net Worth (Cr) | ROE (computed) |
|---|---|---|---|
| FY19 | 17.44 | 75.64 (closing only) | 23.06% |
| FY20 | 16.65 | 83.89 | 19.85% |
| FY21 | 17.46 | 99.75 | 17.50% |
| FY22 | 41.40 | 130.09 | 31.83% |
| FY23 | 61.68 | 272.21 | 22.66% |
| FY24 | 75.06 | 523.95 | 14.33% |
| FY25 | 84.64 | 700.81 | 12.08% |
| FY26 | 107.79 | 828.23 | 13.01% |

A total: 3+3+4+0 = **10/20**

## BLOCK B: CASH GENERATION QUALITY (Max 20) — FILED Score: 12/20 (was 7/20; see window-convention table above)

CFO (screener-data, Cr): FY19 16.79, FY20 23.24, FY21 40.94, FY22 21.61,
FY23 33.57, FY24 72.52, FY25 101.62, FY26 132.85. Cumulative = 443.14 Cr.
PAT cumulative (screener-data) = 422.12 Cr.

**B1 Cumulative CFO ÷ Cumulative PAT** = 443.14/422.12 = 1.05x → band
≥1.00 → **score 5**

**FCF — n=2 years (FY25, FY26), AR p.218 mupdf, capex excludes the
acquisition-of-business line per the formula's own instruction:**

| Year | CFO (Mn) | Capex (Mn) | Acquisition payment excluded (Mn) | FCF (Mn) | FCF (Cr) |
|---|---|---|---|---|---|
| FY25 | 1,016.16 | (832.02) | (743.23) | +184.14 | +18.41 |
| FY26 | 1,328.49 | (1,853.68) | (629.03) | -525.19 | -52.52 |

**B2 FCF-positive years as proportion** = 1/2 → 50% → band 50-74% →
**score 2**
**B3 Cumulative FCF ÷ Cumulative PAT** (FY25+FY26 only) =
(184.14-525.19)/(846.4+1077.9) = -341.05/1924.3 Mn = **-17.7%** → band
<0.20 or negative → **score 0**

**B4 Change in WC Days, latest vs earliest (of the two years available)**
— corrected per Correction 2 item 1, consolidated Trade Payables Note 18
(AR p.255, mupdf): Total Rs 600.92 Mn (FY26) / Rs 314.34 Mn (FY25).

| Year | Receivable days | Inventory days | Payable days | WC days |
|---|---|---|---|---|
| FY25 | 102.23 (1,454.67/5,193.9×365) | 0.98 (13.99/5,193.9×365) | 22.09 (314.34/5,193.9×365) | **81.12** |
| FY26 | 98.44 (1,892.13/7,015.8×365) | 2.03 (39.00/7,015.8×365) | 31.26 (600.92/7,015.8×365) | **69.21** |

Change FY25→FY26 = **-11.91 days** → band "decreased >5 days" →
**score 5** (was 0, N/A on a retracted premise — see Correction 2)

Block B total (FILED, two-year window applied consistently to B2-B4):
5+2+0+5 = **12/20**

Block B total (ALTERNATIVE, window rejected for B2-B4 alike, pending
operator ruling): 5+0+0+0 = **5/20**

**block_b_trend: mixed, two numbers.** FCF swung from +Rs 18.41 Cr
(FY25) to -Rs 52.52 Cr (FY26), AR p.218, on capex nearly doubling (Rs
832.02 Mn to Rs 1,853.68 Mn) while CFO grew ~31%. In the SAME year, WC
days IMPROVED by 11.91 days (81.12d FY25 → 69.21d FY26, AR p.216/255) —
the capex spend did not come with a working-capital deterioration; it
looks like a discrete infrastructure/product-development outlay, not a
receivables or payables slippage. CFO/PAT (accrual quality) also kept
improving: 0.54x (FY23) to 1.23x (FY26, screener-data). Net read: FCF
worsened on capex timing, but the underlying cash-conversion mechanics
(WC days, CFO/PAT) both improved in the same year — a more benign
picture than "deteriorating" alone would suggest. Overall label:
**improving-underlying / FCF-negative-on-capex-timing.**

## BLOCK C: GROWTH (Max 20) — Score: 18/20 (unchanged)

Revenue (screener-data, Cr): FY19 101.58 → FY26 701.58, 7-year span, all
7 YoY comparisons positive (101.58→116.45→131.59→182.64→248.76→
373.12→519.39→701.58).
PAT (screener-data, Cr): FY19 17.44 → FY26 107.79.

**C1 Revenue CAGR** = (701.58/101.58)^(1/7)−1 = **31.8%** → band ≥20% →
**score 5**
**C2 PAT CAGR** = (107.79/17.44)^(1/7)−1 = **29.7%** → band ≥20% →
**score 5**
**C3 Positive YoY revenue years** = 7/7 = 100% → **score 5**
**C4 PAT CAGR − Revenue CAGR** = 29.7 − 31.8 = **−2.1pp** → band ±3pp →
**score 3**

C total: 5+5+5+3 = **18/20**

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 20/20 (unchanged; inputs corrected, see Correction 2 item 4)

FY26 (screener-data, Cr, corrected): Borrowings 28.78, Cash & Bank
**65.20** (was 107.31, that was the FY25 column — see Correction 2),
Reserves 870.11, Equity Share Capital 41.02 (Net Worth 911.13), Interest
5.07, EBIT (computed, PBT+Interest) 136.38.

**D1 Net Debt ÷ EBITDA** = Borrowings 28.78 − Cash 65.20 = **net cash
(-36.42 Cr)** → **score 5** (was -78.53 Cr net cash on the wrong cash
figure; still net cash, score unchanged)
**D2 Interest Coverage** = EBIT 136.38 / Interest 5.07 = **26.9x** →
band ≥10x → **score 5**
**D3 Debt ÷ Equity** = 28.78/911.13 = **0.032x** → band <0.1 →
**score 5**
**D4 Current Ratio** = **2.76x (FY26), CONSOLIDATED** (AR p.216, mupdf:
Total current assets 4,355.64 Mn / Total current liabilities 1,578.00
Mn) — corrected from the standalone 2.90x used previously (Correction 2
item 4; the consolidated split is in fact clean via mupdf). Band ≥2.0 →
**score 5, unchanged.**

D total: 5+5+5+5 = **20/20**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 14/20 (unchanged)

**E1 Promoter holding (latest quarter)** = **54.40%** (BSE Reg 31
summary, scrip 543533, quarter ending June 2026, retrieved 2026-09-19)
→ band 50-59.9% → **score 4**
**E2 Promoter holding change over 3 years** = **N/A (not in provided
data), score 0.** Only two data points exist: BSE summaries for Mar-2026
and Jun-2026 (both 54.40%, unchanged) and the AR's FY26-vs-FY25
promoter-holding note (p.251), which shows FY25→FY26 change of 0% for
most holders (one intra-family transfer between Mythili Srinivasan and
Taarav Pte Ltd, net promoter total unchanged: 54.41%→54.40%). No
data point from ~3 years before run date (circa Sep-2023) is in the
provided corpus.
**E3 Promoter pledge (latest)** = **0%** (BSE Reg 31 summary, Jun-2026:
"Whether any shares held by promoters are pledge or otherwise
encumbered? No") → **score 5**
**E4 Contingent liabilities ÷ Net Worth (latest)** = Rs 34.55 Mn (Rs 3.46
Cr, AR Note 36, p.264, consolidated, FY26) / Rs 911.13 Cr net worth
(screener-data) = **0.38%** → band <5% → **score 5**. **FLAG: this
figure structurally excludes the disputed 3i Infotech claim (>Rs 128
Cr, ~14% of FY26 net worth if it were included — AR Note 36(f) states
management believes there will not be any economic outflow), which sits
only in narrative disclosure, not the quantified total.** If it were
included, E4 would band to 5-15% → score 3, Block E 12, with no
classification-level effect under either filed or alternative reading.

E total: 4+0+5+5 = **14/20**

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 17/60 (unchanged total; M1 and M12 figures corrected, see Correction 2)

EBITDA computed as Sales − (Raw Material + Power&Fuel + Other Mfr. Exp +
Employee Cost + Selling&Admin + Other Expenses − Change in Inventory),
all screener-data, Cr — sign on Change in Inventory corrected per
Correction 2 item 4 (cross-checked exactly against PBT: EBITDA + Other
Income − Depreciation − Interest = PBT for both FY19 and FY26). FY19
EBITDA margin **31.72%** (32.21/101.58, was 31.83% on the wrong sign);
FY26 EBITDA margin **22.68%** (159.12/701.58, was 21.97%) — a 9.04pp
decline over the period (was 9.86pp), still concentrated in "Other Mfr.
Exp" rising from Rs 11.9 Cr (FY19) to Rs 280.91 Cr (FY26), consistent
with scale-up of trust-services/hardware cost lines and the Cryptas
acquisition; not independently decomposable from provided data.

**M1 Pricing Power** — margin declined 9.04pp (FY19→FY26) despite 31.8%
revenue CAGR; decline exceeds the 2-5pp "declined despite growth" band →
**score 0** (unchanged)

**M2 Cost Advantage vs peer median EBITDA margin** — peer FY26 EBITDA
margins (screener-data, same sign correction applied): NEWGEN 25.78%
(unaffected, Change in Inventory blank), QUICKHEAL -11.25% (was -11.54%),
PROTEAN 11.58% (unaffected, blank). Peer median = 11.58% (PROTEAN,
middle of three, unaffected by the QUICKHEAL shift). eMudhra 22.68% is
+11.10pp above (was +10.39pp) → band ≥5pp above → **score 5** (unchanged)

**M3 Capital Efficiency** — FAT (Sales/Net Block, screener-data) =
701.58/726.86 = 0.97x (<1x) with ROCE 14.51% computed (was cited as
15.0% disclosed; either way <20% and <15% bands) → fails all bands →
**score 0** (unchanged)

**M4 Customer Stickiness** — zero revenue-decline years (7/7 positive)
satisfies the "max 1 decline year, fully recovered" tier on decline-year
count alone; the top tier additionally needs receivable days stable
±10, which fails on the full-period screener-computed basis (76.7d FY19
→ 98.4d FY26, computed as Receivables÷Sales×365, screener-data — a
21.7-day lengthening; unaffected by the payables fix, receivables-only
metric). Company-disclosed net-of-GST/VAT receivable days (AR p.57)
show a materially flatter recent window: 94d (FY24), 96d (FY25), 92d
(FY26). Scored on the stricter full-period formula-consistent basis →
**score 3** (unchanged)

**M5 Scale & Dominance** — among the four names in this run's peer set
(mcap, screener-data): NEWGEN Rs 7,087 Cr > EMUDHRA Rs 5,080 Cr > PROTEAN
Rs 1,999 Cr > QUICKHEAL Rs 827 Cr. EMUDHRA ranks 2nd by mcap and 2nd by
FY26 EBITDA margin (22.68%, corrected, behind NEWGEN's 25.78%) → "top 3
mcap AND margin top 2" → **score 3** (unchanged). Caveat: this is the
run's 3 auto-selected peers only (B00), not a verified exhaustive
competitive-segment universe.

**M6 Technology / R&D** — **N/A (not in provided data), score 0.**
No R&D-to-revenue % is disclosed on a comparable multi-year basis; the
BRSR disclosure (AR p.148 area) marks the specific "sustainable R&D
capex %" question "NA." AR narrative states an "R&D team of over 200+
people" (headcount only, not spend). FY26 capitalised product
development (Rs 814.21 Mn, AR p.156, a subset of the Rs 1,853.68 Mn full
capex line per Correction 1) is 8.6% of FY26 revenue for one year only —
suggestive but does not satisfy "consistently."

**M7 Regulatory / License** — eMudhra holds a Controller of Certifying
Authorities (CCA) license (Trust Services, ~20% of FY26 revenue per
B00). Listed-player count within the licensed Certifying Authority
segment specifically is not in the provided data. **PEER DATA NEEDED →
score 0**

**M8 Distribution** — channel mix is quantified for one year (AR p.55:
Direct 60% / Partner-led 40%) but no partner-count growth trend or
"revenue per outlet" metric exists in the provided data → **score 1**

**M9 Brand** — Gross margin proxy (Revenue − Material Cost)/Revenue,
screener-data: eMudhra FY26 91.84% (material cost Rs 57.25 Cr = Raw
Material 54.75 + Δ Inventory 2.5; this proxy is unaffected by the
EBITDA sign correction, it uses Raw Material Cost directly, not the
derived EBITDA). Peers: NEWGEN and PROTEAN report zero in the Raw
Material Cost line for all years (blank field, a data-structure
artifact, not a real advantage), producing a distorted "100%" GM proxy;
QUICKHEAL 98.08%. This comparison is not meaningful. **PEER DATA NEEDED
(comparable COGS/GM basis) → score 0**

**M10 Switching Costs** — revenue grew every year (7/7), but receivable
days rose 21.7 days over the full period on the formula-consistent
screener basis (see M4), which fails both the top-tier "≤10 days" test
and the "stable" qualifier on the next tier down → **score 0**
(unaffected by this correction; receivables-only metric)

**M11 Network Effects** — 8 years available (≥6 required). Latest 3-year
window (FY23→FY26) revenue CAGR = 41.3%; prior 3-year window (FY20→FY23)
= 28.8% (accelerating). Selling & admin expense as % of revenue declined
from 12.77% (FY23: 31.77/248.76) to 8.86% (FY26: 62.17/701.58). Both
conditions met → **score 5** (unchanged)

**M12 Negative WC / Float** — corrected per Correction 2 item 1:
consolidated WC days now computed at **81.12d (FY25) and 69.21d (FY26)**
(AR p.216/255, mupdf), both >45 days, majority (2/2) >45 → **score 0**
(unchanged from the prior N/A-labelled 0, but now a real computed value,
not a placeholder).

F total: 0+5+0+3+3+0+0+1+0+0+5+0 = **17/60** (unchanged)

**Moats present (score ≥3):** M2 (5), M4 (3), M5 (3), M11 (5) = **4
confirmed** (unchanged)
**Moat classification:** 4 present → **STRONG** (unchanged)

---

## SCORECARD SUMMARY (CORRECTION 2)

| Block | Score (FILED) | Score (ALTERNATIVE, pending ruling) | Max |
|---|---|---|---|
| A — Return on Capital | 10 | 10 | 20 |
| B — Cash Generation Quality | 12 | 5 | 20 |
| C — Growth | 18 | 18 | 20 |
| D — Balance Sheet Strength | 20 | 20 | 20 |
| E — Shareholder Alignment | 14 | 14 | 20 |
| **Core Score** | **74** | **67** | **100** |
| F — Quantitative Moat | 17 | 17 | 60 |
| **Grand Total** | **91** | **84** | **160** |

Moats confirmed: 4 (M2 Cost Advantage, M4 Customer Stickiness, M5 Scale
& Dominance, M11 Network Effects). Moat classification: **STRONG**.
Both identical across readings.

Data confidence: 8 years (FY19-FY26) → **moderate** tier (7-9 band, no
downgrade required).

Deal-breaker check:

| # | Rule | FILED (n=2 accepted) | ALTERNATIVE (n=2 rejected) |
|---|---|---|---|
| 1 | Block A <8 | Block A=10, not triggered | Block A=10, not triggered |
| 2 | Block B <8 | Block B=12, **not triggered** | Block B=5, **TRIGGERED → max GOOD** |
| 3 | Median ROCE <10% | 18.05%, not triggered | 18.05%, not triggered |
| 4 | Cumulative CFO/PAT <0.50 | 1.05x, not triggered | 1.05x, not triggered |
| 5 | Pledge >15% | 0%, not triggered | 0%, not triggered |
| 6 | ND/EBITDA >3x AND IC <3x | net cash / 26.9x, not triggered | net cash / 26.9x, not triggered |
| 7 | Revenue declined majority of years | 7/7 grew, not triggered | 7/7 grew, not triggered |
| 8 | PAT negative in any of last 3 years | all positive, not triggered | all positive, not triggered |
| 9 | History <3 years | 8 years, not triggered | 8 years, not triggered |

**Classification matrix:**
- **FILED (two-year window accepted for B2-B4 alike):** Core 74 (60-79
  band) + Moat STRONG, no deal-breaker triggered → **GOOD+**
- **ALTERNATIVE (window rejected for B2-B4 alike, PENDING OPERATOR
  RULING):** Core 67 (60-79 band) + Moat STRONG, but deal-breaker #2
  caps it → **GOOD**

**Strongest block:** D — Balance Sheet Strength (20/20; net cash, 26.9x
interest coverage, 0.03x D/E, 2.76x consolidated current ratio).
**Weakest block:** A — Return on Capital (10/20) under the filed reading
(B is now stronger at 12/20); A2's minimum single-year ROCE of 14.41%
(FY24, computed, one consistent basis) is the binding constraint.

**Decision line:** **GOOD+ on the filed two-year-window convention; GOOD
if the operator rules against extending that window to B4** (the
alternative reading). This is the one open methodological question left
in this stage: prompts/01 does not say whether a sub-metric may score on
fewer years than the full history when the full window is not
extractable. Separately and independent of that ruling: FY26 FCF is
confirmed negative (-Rs 52.5 Cr) even as WC days improved 11.9 days in
the same year (a more benign combination than "cash conversion is
broadly deteriorating" would suggest); the 420-day payables claim in
company memory does not reproduce (actual: 31.3 payable days FY26) and
should be corrected; and E4's clean 0.38% contingent-liability ratio
still does not carry the Rs 128 Cr+ disputed 3i Infotech claim. Flag all
for stage 2+ and for the operator ruling.

---

## DATA NOTES

- No loss-to-profit PAT swing in FY19-FY26 (PAT positive throughout);
  CAGR edge rules not triggered.
- **ROCE/ROE now computed on ONE basis for all 8 years** (Correction 2
  item 3): Capital Employed = Equity Share Capital + Reserves +
  Borrowings (screener's 4-bucket Data_Sheet model). AR-disclosed
  consolidated ROCE/RoE (AR p.57, FY24-26) is shown as a cross-check
  only, not scored, to avoid mixing bases within one metric's min/median.
- **RETRACTED**: the prior claim that consolidated Trade Payables and
  consolidated current assets/liabilities were "not reliably
  extractable" from the AR. They are extractable cleanly via the mupdf
  text route (Annual_Report_2026.mupdf.txt), which this stage had not
  used in the first two drafts (it had only tried the pdftotext-layout
  extraction, which genuinely does scramble these specific pages). AR
  p.216 (consolidated balance sheet) and Note 18, p.255 (Trade payables)
  and Note 50, p.364 (standalone ratios, used previously as a fallback)
  are now all cited from the clean mupdf source. Recommend this stage
  and downstream stages default to the .mupdf.txt file when the
  pdftotext-layout .txt produces scrambled tables, rather than marking
  N/A.
- FCF (B2/B3) computed for FY25 and FY26 (n=2) using the clean AR p.218
  mupdf extraction (Correction 1). FY19-FY24 capex remains not
  extractable from provided data (screener Data_Sheet has no capex
  line; no earlier-year AR cash-flow statement in this corpus).
- **WINDOW CONVENTION open item**: whether B2, B3 and B4 may score on a
  2-year window when the full 8-year window is not extractable is not
  addressed by prompts/01-gate-0-pipeline.md. This report files the
  2-year-window-accepted reading (applied consistently across B2, B3,
  B4) per the coordinator's routing instruction, and states the
  2-year-window-rejected alternative for the operator to rule on. The
  ruling changes classification (GOOD+ vs GOOD).
- M9 Gross-margin peer comparison is a proxy — GM = (Revenue − Material
  Cost)/Revenue — and is distorted because 2 of 3 peers (NEWGEN, PROTEAN)
  report zero in the Raw Material Cost line for every year in the
  screener Data_Sheet (a cost-classification artifact, not a real 100%
  gross margin). Not used as a scored signal beyond the 0 assigned.
- E2 (promoter holding, 3-year change) marked N/A: only ~1-2 years of
  data points exist in the provided corpus (see Block E).
- Consolidated CFO/CFI cross-checks (AR p.155-156 MD&A table and AR
  p.218 mupdf) both confirm CFO Rs 1,328.49 Mn FY26 (= Rs 132.85 Cr,
  matches screener-data exactly). Consolidated CFI Rs -2,250.53 Mn (= Rs
  -225.05 Cr) vs screener-data Rs -197.76 Cr — a ~Rs 27 Cr gap,
  immaterial to sign/direction, not reconciled further in this stage.
- input_gaps carried from B00 (stage 0): FRESHNESS FAIL — ICRA June-2026
  rating rationale absent (only the reaffirmation letter is held; latest
  full rationale on file is dated 02-Jun-2025). Gate recommendation caps
  at PROCEED WITH CAVEATS per B00. Not scored by this stage.

## ANALYST NOTE

GOOD+ under the filed two-year-window convention (was GOOD after
Correction 1, GOOD+ before Correction 1's FCF fix; Correction 2 both
fixes a mixed-basis ROCE error that lowered Block A and confirms trade
payables/current ratio that raise Block B and D4's basis). Growth
remains excellent (C=18/20) and the balance sheet is genuinely clean
(D=20/20, net cash even after the FY26 cash column fix, 27x interest
cover, 2.76x consolidated current ratio). The corrected picture on cash
is more nuanced than either prior draft suggested: FY26 FCF is
confirmed negative (-Rs 52.5 Cr) on a near-doubling of capex, but WC
days improved 11.9 days the same year and CFO/PAT (accrual quality)
kept climbing — this reads more like a discrete capex/infrastructure
outlay than a broad cash-conversion breakdown. The "420 days payable"
figure in company memory does not reproduce (actual 31.3 days FY26) and
should be corrected downstream. One open item remains genuinely
undecided: whether a Block B sub-metric may score on a 2-year window
when the full 8-year window is not extractable (prompts/01 is silent);
this stage files the 2-year-accepted reading (GOOD+) and states the
2-year-rejected alternative (GOOD) for an operator ruling. E4's clean
0.38% contingent-liability score still cannot carry the disputed Rs 128
Cr+ 3i Infotech claim (narrative-only, AR Note 36(f)).
