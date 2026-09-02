# DOCUMENT REVIEW — India Glycols Limited (INDIAGLYCO) | 2026-09
## Merged three-deck review of the demerger investor presentations (A4 ANALYST) — LOOP 1 (correction pass)

Protocol: Document Review Protocol v1.1 (loaded alone; no Master, Role 4/5,
FTTCP, Section 1B, or RDE manual). Framing: THESIS CHECK against a live Notion
thesis. Inputs: A1 structured (three decks) + A1 fulltext at cited lines + A2
ledgers + A3 forensics + the prior A4 review. Source PDFs and `inputs/` NOT
opened.

Three decks reviewed as one merged object because they describe one corporate
action: the three-way demerger of India Glycols Limited, NCLT Allahabad
sanction 17-Jul-2026, effective 1-Sep-2026, record date 2-Sep-2026, appointed
date 1-Apr-2026.
- Entity A — residual India Glycols Ltd (corporate deck, R001-R291).
- Entity B — IGL Spirits Ltd (spirits deck, R001-R355).
- Entity C — Ennature Biopharma Ltd (EB deck, R001-R152).

---

## LOOP 1 — CORRECTION LOG (what changed vs the prior pass, and why)

This pass regenerates the review whole so it stays self-contained. The edits are
surgical. Every change traces to a named A5 finding; no unchallenged step was
reworked (protocol v1.1 LOOP BEHAVIOR).

- **A5 FACTUAL (arithmetic), Step 2.5 "Derived (not in deck)" realisation per
  case.** The prior review stated IGL Spirits Potable realisation per case as Rs
  ~3,788 / 3,907 / 4,437 (FY24/25/26). That is 10x too high: a Cr-to-rupee
  conversion error (Rs 1 Cr = 100 lakh = Rs 10,000,000; cases are in millions, so
  Cr / mn-cases = hundreds of rupees, not thousands). Restated to Rs ~379 (947
  Cr / 25.0 mn), Rs ~391 (1,176 Cr / 30.1 mn), Rs ~444 (1,331 Cr / 30.0 mn).
  Lands at Step 2.5 note (below the extraction table). The +14% FY25->FY26
  realisation read and every downstream conclusion (regulated-pricing vs
  premiumisation, Q13, thesis variable B) are UNCHANGED — the growth rate is
  scale-invariant and was computed off the correct ratio, not the mislabelled
  absolute.
- **A5 STYLE (logged, no substantive change), India Glycols p12 Net Rev.** Step
  2.3 shows India Glycols FY26 Net Rev as Rs 1,163 Cr (p12, R056) while p7 and
  p31 carry Rs 1,164 Cr (R026 / R139). The 1 Cr difference is source rounding
  between two slides of the same deck, not a data conflict. Labelled inline at
  Step 2.3. No number changed.
- **A5 STYLE (logged, no substantive change), Clariant JV share assumption.**
  Step 4.1 derives IGL's ~Rs 46.5 Cr JV share as 49% x Rs 95 Cr JV PAT. The
  ownership-order assumption is now stated: the 51:49 split (R133) is read as
  Clariant 51% / IGL 49%, so IGL takes the 49% slice. Stated inline at Step 4.1.
  No number changed; the ~46.5 Cr figure and its thesis match (Rs 46.4 Cr) stand.

A5 verified the following unchanged and they carry forward verbatim: the Adj.
EBITDA reconciliation (Step 4.1), the corp page-7 IGL Spirits / Ennature
transposition (Step 4.2), the Entity B net-debt trend and cash-quality direction
(Step 5), and the coverage / ledger reconciliation (Step 1).

---

## STEP 1 — LEDGER RECONCILIATION PREAMBLE

**Entity A (corp).** Ledger contains 32 slides / 291 disclosure units
(R001-R291). All 291 reviewed. A2 gate: pass (orphan_ids empty). A3 findings
incorporated: A1, A2, A3, A4, A5, A6, A7.

**Entity B (spirits).** Ledger contains 31 slides / 355 disclosure units
(R001-R355). All 355 reviewed. A2 gate: pass (orphan_ids empty). A3 findings
incorporated: FND-01, FND-02, FND-03, FND-04, FND-05, FND-06, FND-07, FND-08.

**Entity C (EB).** Ledger contains 15 pages (1 cover letter + 14 slides) / 152
disclosure units (R001-R152). All 152 reviewed. A2 gate: pass (orphan_ids
empty). A3 findings incorporated: A3-F6-01, A3-F6-02, A3-F6-03, A3-F14-01,
A3-F14-02, A3-F16-01, A3-F16-02.

Total: 78 slide-units, 798 disclosure units, all reviewed. No unreviewed rows.
Proceeding.

---

## STEP 2 — EXTRACTION TABLES (every cell a line-anchored number or ND)

### 2.1 Combined pre-demerger group — corp deck page 7 "Key Financials" (INR Cr)

| Metric | FY24 | FY25 | FY26 | anchor |
|---|---|---|---|---|
| Net Revenue, total | 3,291 | 3,767 | 4,211 | R016 / R017 / R018 |
| EBITDA, total | 423 | 521 | 690 | R028 / R029 / R030 |
| Net Revenue CAGR FY24-26 | — | — | c.13% | R014 |
| EBITDA CAGR FY24-26 | — | — | c.28% | R015 |

### 2.2 Combined group segment split — corp deck page 7 (INR Cr) — CONTAINS A TRANSPOSITION (see Step 4.2)

| Segment / metric | FY24 | FY25 | FY26 | anchor |
|---|---|---|---|---|
| Net Rev — "IGL Spirits" (as labelled p7) | 250 | 257 | 246 | R019 / R022 / R025 |
| Net Rev — India Glycols | 1,581 | 1,291 | 1,164 | R020 / R023 / R026 |
| Net Rev — "Ennature" (as labelled p7) | 1,460 | 2,219 | 2,801 | R021 / R024 / R027 |
| EBITDA — "IGL Spirits" (as labelled p7) | 60 | 41 | 29 | R031 / R034 / R037 |
| EBITDA — India Glycols | 139 | 130 | 169 | R032 / R035 / R038 |
| EBITDA — "Ennature" (as labelled p7) | 224 | 350 | 492 | R033 / R036 / R039 |
| EBITDA margin — "IGL Spirits" (p7) | 24.1% | 16.0% | 11.9% | R040 / R041 / R042 |
| EBITDA margin — India Glycols | 8.8% | 10.1% | 14.5% | R043 / R044 / R045 |
| EBITDA margin — "Ennature" (p7) | 15.4% | 15.8% | 17.6% | R046 / R047 / R048 |

The "IGL Spirits" and "Ennature" labels on page 7 are transposed against the
standalone decks and against corp page 12 (Step 4.2). Values are shown as
labelled in the source; the correct entity assignment is given below.

### 2.3 Demerged-structure revenue split — corp deck page 12 (FY26, INR Cr)

| Entity | Gross Rev | Net Rev | share | anchor |
|---|---|---|---|---|
| IGL Spirits | INR 8,416 | 2,801 | 67% | R052 / R053 / R054 |
| India Glycols | INR 1,163 | 1,163 | 28% | R055 / R056 / R057 |
| Ennature | INR 247 | 247 | 6% | R058 / R059 / R060 |
| Swap ratio — IGL Spirits | 1 IGL Spirits per 1 IGL share | | | R061 |
| Swap ratio — Ennature | 1 Ennature per 3 IGL shares | | | R062 |

Note (A5 STYLE, logged): India Glycols FY26 Net Rev reads Rs 1,163 Cr here on
p12 (R056) versus Rs 1,164 Cr on p7 (R026) and p31 (R139). The 1 Cr difference
is source rounding between slides of the same deck, not a data conflict. Entity A
analysis uses the p31 figure (1,164).

### 2.4 Residual India Glycols post-demerger — corp deck pages 14 + 31 (INR Cr)

| Metric | FY24 | FY25 | FY26 | anchor |
|---|---|---|---|---|
| Net Sales Value | 1,581 | 1,291 | 1,164 | R137 / R138 / R139 |
| Adj. EBITDA | 247 | 312 | 330 | R140 / R141 / R142 |
| Adj. EBITDA margin | 15.6% | 24.2% | 28.4% | R143 / R144 / R145 |
| Unadjusted EBITDA (p7) | 139 | 130 | 169 | R032 / R035 / R038 |
| Unadjusted EBITDA margin (p7) | 8.8% | 10.1% | 14.5% | R043 / R044 / R045 |
| Segment rev — Bio-based Specialty Materials | ND | ND | 546 | R063 |
| — of which Bio-Glycols | ND | ND | 325 | R066 |
| — of which Glycol Ether & GE Esters | ND | ND | 221 | R067 |
| Segment rev — Sustainable & Performance Chemicals | ND | ND | 474 | R064 |
| — of which Performance Chemicals | ND | ND | 56 | R068 |
| — of which Clariant JV (IGL-side sales) | ND | ND | 419 | R069 |
| Segment rev — Gases | ND | ND | 50 | R065 |
| Gases (restated p28) | ND | ND | 47 | R131 |
| Clariant JV PAT (100%) | ND | ND | 95 | R136 |
| Bio-Glycols volume | ND | ND | ~28,750 MT | R118 |
| Bio-Glycols export share | ND | ND | 63% | R120 |
| Performance Chemicals volume | ND | ND | ~2,800 MT | R127 |
| Industrial Gases volume | ND | ND | ~67,000 MT | R130 |

Note: page-14 segment build (546 + 474 + 50 = 1,070) does not tie to the
page-31 total (1,164). Gap ~94 Cr unexplained; Novel Tech segment (R177) carries
no revenue. Flagged Step 4.3.

### 2.5 IGL Spirits (Entity B) — standalone deck (INR Cr unless noted)

| Metric | FY24 | FY25 | FY26 | anchor |
|---|---|---|---|---|
| Net Revenue, total | 1,459 | 2,219 | 2,801 | R123 / R124 / R125 |
| — Potable Spirits | 947 | 1,176 | 1,331 | R126 / R127 / R128 |
| — Bio-fuels | 512 | 1,044 | 1,470 | R129 / R130 / R131 |
| EBITDA | 224 | 350 | 492 | R133 / R134 / R135 |
| EBITDA margin | 15.4% | 15.8% | 17.6% | R136 / R137 / R138 |
| PAT (post-bifurcation basis) | 88 | 151 | 244 | R139 / R140 / R141 |
| PAT margin | 6.0% | 6.8% | 8.7% | R142 / R143 / R144 |
| Potable Spirits cases (Mn) | 25.0 | 30.1 | 30.0 | R110 / R111 / R112 |
| Potable Spirits gross margin | 36.0% | 41.9% | 45.9% | R117 / R118 / R119 |
| Potable Spirits gross margin (INR Cr) | 341 | 493 | 611 | R120 / R121 / R122 |
| Net Debt | 728 | 900 | 767 | R145 / R146 / R147 |
| Cash Profit | 159 | 248 | 395 | R148 / R149 / R150 |
| RoCE | 13.0% | 17.9% | 20.5% | R151 / R152 / R153 |
| ESY 2025-26 ethanol allocation | — | — | 220 mn L / Rs 1,450 Cr | R100 / R101 |
| ESY 2026-27 ethanol allocation | ND | ND | ND | not disclosed |

Derived (not in deck): Potable Spirits realisation per case = 947 Cr / 25.0 mn
cases = Rs ~379 (FY24); 1,176 Cr / 30.1 mn = Rs ~391 (FY25); 1,331 Cr / 30.0 mn
= Rs ~444 (FY26).
[CORRECTION — loop1, A5 FACTUAL. The prior pass stated Rs ~3,788 / 3,907 / 4,437,
a 10x arithmetic error (Cr-to-rupee conversion: 1 Cr = Rs 10,000,000, so
Cr / million-cases is in the hundreds of rupees, not thousands). Restated to the
correct Rs ~379 / 391 / 444. The interpretive read is unchanged: cases flat
FY25->FY26 (30.1 -> 30.0) while realisation per case rose ~+14% (391 -> 444). A
+14% price-per-case rise on flat volume is consistent with UP/Uttarakhand
government-set (regulated) pricing, not premiumisation. Growth rate is
scale-invariant, so Q13, thesis variable B, and the brief stand.]
Cases flat FY25->FY26; realisation per case rose ~14%.

### 2.6 Ennature Biopharma (Entity C) — standalone deck (INR Cr, FY26 only)

| Metric | FY26 | anchor |
|---|---|---|
| Revenue | 246 | R049 |
| Gross Margin | 40.1% | R050 |
| EBITDA | 29 | R051 |
| EBITDA margin | 11.9% | R052 |
| Sales mix — Plant-based APIs | 67% | R019 |
| Sales mix — Biopolymers (guar) | 16% | R020 |
| Sales mix — Nutraceuticals | 17% | R021 |
| API export revenue share | 54% | R028 |
| Biopolymer export revenue share | 69% | R031 |
| Nutraceuticals export revenue share | 83% | R036 |
| Dehradun capacity | 1,600 MT | R047 |
| Kashipur capacity | 24,000 MT | R048 |
| Prior-year comparatives (FY24/FY25) | ND | not disclosed |
| Segment rupee split | ND | not disclosed |
| Thiocolchicoside share / price | ND | not disclosed |

---

## STEP 3 — YoY / QoQ WALKS AND PAT BRIDGE

No quarterly data in any deck. All figures are annual FY24-FY26 (Entity A, B) or
single-period FY26 (Entity C). QoQ walk: NOT POSSIBLE. PAT bridge: only Entity B
discloses PAT (88/151/244, R139-R141), on a "post Group's bifurcation" carve-out
basis (R354), so a clean YoY PAT bridge is not reliable. Entities A and C
disclose no PAT. PAT bridge: NOT CONSTRUCTIBLE from these decks.

YoY revenue walk (annual):
- Entity A residual India Glycols: 1,581 -> 1,291 -> 1,164, down 26.4% over two
  years (R137-R139). Management label: "revenue moderation" (A3 corp A4). This is
  a decline, not moderation.
- Entity B IGL Spirits: 1,459 -> 2,219 -> 2,801, up 92% over two years
  (R123-R125), Bio-fuels the faster leg (512 -> 1,470, up 187%, R129-R131).
- Entity C Ennature: single period only; no walk.

---

## STEP 4 — STANDALONE-vs-CONSOLIDATED / ADJUSTED-vs-UNADJUSTED GAP (first-class metric)

These decks carry no formal standalone-vs-consolidated columns (A3 F2 is N.A. for
spirits and EB). The first-class gap here is the corp deck's ADJUSTED-vs-
UNADJUSTED EBITDA basis break and a cross-deck entity transposition.

### 4.1 Residual India Glycols Adj. EBITDA does not reconcile (corp A3 finding A1, AMBIGUOUS)

Same revenue base, two EBITDA bases, one deck:

| FY | Net Rev | Unadj. EBITDA (p7) | Adj. EBITDA (p31) | gap |
|---|---|---|---|---|
| FY24 | 1,581 | 139 | 247 | 108 |
| FY25 | 1,291 | 130 | 312 | 182 |
| FY26 | 1,164 | 169 | 330 | 161 |

Footnote R291: "Adjusted EBITDA adds back IGL's share of the Clariant JV
profits." That single add-back cannot bridge the gap:
- IGL 49% share of JV PAT 95 (R136) = ~46.5 Cr. Ownership-order assumption
  (A5 STYLE, logged): the 51:49 JV split (R133) is read as Clariant 51% / IGL
  49%, so IGL takes the 49% slice; 49% x 95 = ~46.5 Cr, which matches the thesis
  figure of Rs 46.4 Cr and so validates the read.
- 169 + 46.5 = 215.5, not 330.
- Even adding back the FULL JV PAT 95: 169 + 95 = 264, still not 330.
- Residual undisclosed add-back FY26 = 66 Cr (full-PAT basis) to 114 Cr (49%-
  share basis).

FY25 is worse: the 182 Cr gap exceeds the entire FY26 JV PAT of 95 Cr. The
footnote is arithmetically insufficient for every year. The headline "INR 330 Cr
/ 28.4% margin / strong earnings profile" rests on 66-114 Cr of adjustments the
deck does not itemise. The bridge is a management question (Step 8).

Both bases improve, but the level doubles under adjustment (14.5% -> 28.4% FY26),
and both sit on a revenue base that fell 26%. "Strong margin expansion more than
offset revenue moderation" (A3 corp A4) is JV-adjusted margin on a shrinking core
top line.

### 4.2 Cross-deck transposition — corp page 7 swaps IGL Spirits and Ennature (new merged-review finding)

Corp page 7 "Key Financials" and corp page 12 "Demerged Structure" contradict
each other on which demerged business is which:

| Source | IGL Spirits FY26 Net Rev | Ennature FY26 Net Rev | IGL Spirits FY26 EBITDA | Ennature FY26 EBITDA |
|---|---|---|---|---|
| Corp p7 (R025/R027/R037/R039) | 246 | 2,801 | 29 | 492 |
| Corp p12 (R053/R059) | 2,801 | 247 | ND | ND |
| Spirits standalone (R125/R135) | 2,801 | — | 492 | — |
| EB standalone (R049/R051) | — | 246 | — | 29 |

The two standalone decks — each an entity's own filing — settle it: IGL Spirits
FY26 is Rs 2,801 Cr revenue / Rs 492 Cr EBITDA; Ennature FY26 is Rs 246 Cr
revenue / Rs 29 Cr EBITDA. Corp page 7 therefore has the IGL Spirits and Ennature
rows TRANSPOSED across all three years (revenue, EBITDA and margin move together,
so the whole two columns are swapped). A reader taking corp page 7 at face value
sees IGL Spirits as a Rs 246 Cr / Rs 29 Cr minnow and Ennature as a Rs 2,801 Cr /
Rs 492 Cr engine — exactly backwards.

Materiality: the India Glycols column on page 7 (1,164 rev, 169 EBITDA) is NOT
affected and matches page 12 and page 31, so Entity A analysis stands. The
transposition is a drafting/governance defect in the combined-group slide of a
Reg. 30 investor deck. Per input discipline this is FLAGGED, not resolved by
reopening the source. Management question raised (Step 8).

### 4.3 Segment build does not tie to total (corp, minor)

Residual India Glycols page-14 segments 546 + 474 + 50 = 1,070 vs page-31 total
1,164; ~94 Cr gap (R063-R065 vs R139). Plus Gases 50 (R065) vs 47 (R131), a 3 Cr
intra-deck mismatch (A3 corp A5). Individually small; together low-grade
governance noise.

### 4.4 Entity B / C: no S-vs-C split disclosed

Spirits and EB present as single post-demerger entities. No JV/associate,
subsidiary, or elimination decomposition. S-vs-C gap: NOT DISCLOSED (ND).

---

## STEP 5 — CASH-QUALITY NOTE (per protocol 5a / 5b)

**Entity A (corp).** No cash-flow statement AND no balance sheet for residual
India Glycols (no net debt, no working capital, no net worth). Cash conversion =
INDETERMINATE. The Adj. EBITDA headline (Step 4.1) is unbacked by any cash or
balance-sheet line. Verdict for this entity caps at PROCEED WITH CAVEATS; missing
evidence: cash-flow statement, net debt, working-capital trend.

**Entity B (spirits).** No cash-flow statement, but a partial balance sheet
exists (net debt, cash profit, RoCE). Protocol 5b applies: compute the direction.
- Net debt: 728 (FY24) -> 900 (FY25) -> 767 (FY26) (R145-R147). Rose 172 Cr in
  FY25 on the bio-fuel scale-up, then fell 133 Cr in FY26 while revenue grew
  2,219 -> 2,801.
- Cash Profit: 159 -> 248 -> 395 (R148-R150), rising.
- Net-debt-to-cash-profit: ~4.6x -> ~3.6x -> ~1.9x, improving.
- Working-capital days, inventory and receivables vs revenue: NOT DISCLOSED —
  cannot test.
Classification: INDETERMINATE-WITH-DIRECTION (improving on the disclosed net-
debt / cash-profit axis), resting on R145-R150. Caveat: net debt is defined as
Term Loan + Fund-Based WC minus Cash (R355); it EXCLUDES non-fund-based LC/BG,
a possible understatement, and net worth is not disclosed, so the 20.5% RoCE
denominator cannot be tied out (A3 spirits FND-03). Net debt 767 sits below the
~Rs 1,050 Cr thesis-broken trigger, but on a narrow definition and a pre-demerger
carve-out basis, not the filed opening balance sheet (due Oct-Nov 2026). Verdict
caps at PROCEED WITH CAVEATS.

**Entity C (EB).** No cash-flow statement AND no balance sheet; only a single
FY26 Revenue / Gross Margin / EBITDA line, guar-contaminated. Cash conversion =
INDETERMINATE. Verdict caps at PROCEED WITH CAVEATS; missing evidence: any
balance sheet, any prior-year comparative.

Merged cash-conversion classification: INDETERMINATE (two of three entities), one
INDETERMINATE-WITH-DIRECTION (improving). This does NOT resolve to PROCEED.

---

## STEP 6 — THESIS RECONCILIATION (verify Decision Status FIRST)

**Decision Status verified: WATCHLIST / AVOID (DEEP WATCH, not actionable),
finalized 2026-08-25.** No position framing beyond this status. Nothing in these
three decks fires a pre-committed trigger; the status is unchanged. This review
flags; the human decides.

### 6.1 Thesis-broken triggers — do any fire?

| Trigger | Deck evidence | anchor | Fires? |
|---|---|---|---|
| Entity B net debt materially > ~Rs 1,050 Cr | 767 (FY26), narrow definition, carve-out basis | R147 | NO (below trigger; awaits filed opening BS) |
| Entity A net debt > ~Rs 813 Cr | not disclosed | — | UNTESTABLE from deck |
| Bio-glycol realisation/MT falls while Asia MEG flat/rising | Bio-Glycols FY26 325 Cr / ~28,750 MT single period; no prior-year, no MEG index | R066 / R118 | UNTESTABLE (one period only) |
| Clariant JV share toward ~Rs 30 Cr floor or dividend interrupted | JV PAT 95 -> IGL 49% = ~46.5 Cr, matches thesis Rs 46.4 Cr | R136 | NO (above floor; confirms thesis) |

No thesis-broken trigger fires. Decision Status holds.

### 6.2 Which thesis gaps do the decks resolve vs leave open?

| Entity | Dominant variable | Deck outcome | anchor |
|---|---|---|---|
| A | Bio premium ratio (BSPC realisation/MT vs APAC MEG) | OPEN — only FY26 Bio-Glycols 325 Cr / ~28,750 MT; no prior-year, no index | R066 / R118 |
| A | NSU revenue (Rs 150 Cr aspiration) | OPEN — capacity-only (7,500 MTPA); Perf Chem FY26 56 Cr / ~2,800 MT, no NSU revenue line | R010 / R126 / R128 |
| A | Clariant JV share of profit; 24% stake sale FY28-29 | PARTIAL — current-year share confirmed (~46.5 Cr); stake-sale plan SILENT | R136 |
| B | UP/Uttarakhand excise; regulated pricing vs premiumisation | OPEN — gross margin 36.0->45.9% narrated as premiumisation, but cases flat (30.1->30.0); driver not disclosed | R117-R119 / R111-R112 |
| B | IMFL realisation/case (thesis Q1 FY27 realisation -19%) | OPEN — only FY24-26 annual (realisation rising ~+14% to Rs ~444/case); Q1 FY27 not disclosed | R110-R115 |
| B | ESY 2026-27 OMC allocation (68% oversupply) | OPEN — only ESY 2025-26 (220 mn L / Rs 1,450 Cr); current allocation absent | R100 / R101 |
| C | Thiocolchicoside share / price | OPEN — qualitative "gain share" only | R119 (EB) |
| C | Nicotine end-market split | OPEN — directional "shift to pharma / NRT presence" only | R121 (EB) |
| C | Product / customer concentration | OPEN — counts (150+/23+/90+), no concentration % | R027/R030/R035 (EB) |

Of nine dominant thesis variables, the decks resolve essentially ONE (Clariant JV
current-year share, which confirms the thesis's Rs 46.4 Cr), leave eight open,
and fire no trigger. The presentations are a marketing narrative, not the
disclosure the thesis waits on (filed standalone opening balance sheets Oct-Nov
2026; Ennature's first guar-free quarter Q2 FY27, Nov 2026).

---

## STEP 7 — FORWARD-TARGET REGISTER (from A3 F6 + A1 FORWARD rows)

| Entity | Commitment / target | Implied date | anchor | status word |
|---|---|---|---|---|
| A | Demerger effective | 1-Sep-2026 | R268 | completed |
| A | Demerger concluded | 24-Oct-2026 | R229 / R269 | underway |
| A | Assets/liabilities/contracts/employees transferred | by 24-Oct-2026 | R227 | underway |
| A | Rs 2,000 Cr net revenue & Rs 400 Cr EBITDA | next 4-5 yrs (~FY30-31) | R100 / R101 / R235 | aspiration |
| A | 10X sales and profits | ten years (~FY36) | R099 / R234 | aspiration |
| A | NPDI projects in performance chemicals | near/medium-term | R220 | intended |
| A | CCUS / novel catalysis / CO2 valorisation | undated, development-stage | R236 | in discussion |
| B | EBITDA over Rs 550 Cr | FY27 | R156 / R280 | aspire |
| B | 2x IMFL volumes via new brand launches | FY27 | R157 / R281 | planned |
| B | Debt-free balance sheet | FY28 | R284 | target |
| B | Rs 1,000 Cr EBITDA | "3-4 yrs" (~FY29-30) AND FY31E on pathway chart — CONFLICT | R155 / R158 / R285 | target (horizon conflict, FND-08) |
| B | Amazing & Zumba across 8 states | FY27-end | R087 / R254 | underway |
| B | White spirits 1Mn+ cases, 3 states | undated | R083 / R253 | targeting |
| C | Launch 1 new API product per year | annual, next test FY27 | R108 / R118 | planned |
| C | US local office for coverage/stocking | done (FY26) | R114 | established |
| C | Berbisol clinical trials | ongoing, readout NOT DISCLOSED | R116 | underway |
| C | Scale to 6-8 branded ingredients (5 now + 2 planned) | unspecified | R032 / R033 / R128 | planned |
| C | Establish NRT presence in pharma | unspecified | R121 | initiated |

---

## STEP 8 — QUESTIONS FOR MANAGEMENT (every FORWARD-SIGNAL / AMBIGUOUS A3 finding generates >=1)

| # | Question | From finding |
|---|---|---|
| Q1 | Provide the full Adj. EBITDA bridge for residual India Glycols FY24-26. The Clariant JV add-back (~46.5 Cr, or 95 Cr at full PAT) leaves 66-114 Cr of the FY26 gap and 182 Cr of the FY25 gap unexplained. What else is added back? | corp A1 (AMBIGUOUS) |
| Q2 | On corp page 7 the IGL Spirits and Ennature revenue and EBITDA rows contradict page 12 and both standalone decks (Spirits FY26 = 2,801/492; Ennature FY26 = 246/29). Confirm which is correct and reissue the corrected slide. | merged Step 4.2 (new) |
| Q3 | Which residual-IGL headline metrics are Clariant-JV-inclusive and which are ex-JV? Export mix is shown "Excluding Clariant JV sale" (R275) while Adj. EBITDA adds the JV back. State the scope per metric. | corp A3 (AMBIGUOUS) |
| Q4 | Give the residual India Glycols opening standalone net debt, working-capital days and net worth. The deck discloses none for Entity A. | corp A1 / Step 5 |
| Q5 | Confirm the demerger conclusion date (24-Oct-2026) and the first standalone-reporting quarter for each resulting company. | corp A2 (FORWARD-SIGNAL) |
| Q6 | The residual entity is one legal person carrying two EBITDA bases (unadjusted p7 169 / adjusted p31 330). Which basis will the filed standalone accounts use? | corp A7 (AMBIGUOUS) |
| Q7 | Post-demerger, what is each resulting company's opening balance sheet and CARE rating? (A- RWD pre-demerger.) | corp A6 (FORWARD-SIGNAL) |
| Q8 | IGL Spirits: test the FY27 targets — EBITDA > Rs 550 Cr and 2x IMFL volume by FY27, debt-free by FY28. What Q1 FY27 run-rate supports them? | spirits FND-01 (FORWARD-SIGNAL) |
| Q9 | Disclose the ESY 2026-27 ethanol allocation (volume and value). Only ESY 2025-26 (220 mn L / Rs 1,450 Cr) is shown, yet the EBITDA guide leans on bio-fuel demand. | spirits FND-02 (FORWARD-SIGNAL) |
| Q10 | IGL Spirits net debt (767) excludes non-fund-based LC/BG and net worth is undisclosed. Give gross debt, LC/BG exposure and net worth so RoCE (20.5%) can be tied out. | spirits FND-03 (AMBIGUOUS) |
| Q11 | Restate FY24-26 PAT on a like-for-like basis. The disclosed 88/151/244 is a "post Group's bifurcation" carve-out; period comparability is limited. | spirits FND-05 (AMBIGUOUS) |
| Q12 | Which Kashipur potable capacity is live today (FY26 actual vs FY27E projection are mixed under one headline)? | spirits FND-06 (AMBIGUOUS) |
| Q13 | Potable Spirits gross margin rose 36.0% -> 45.9% while cases were flat (30.1 -> 30.0) and realisation per case rose ~+14% (Rs ~391 -> ~444). How much of the value growth is premiumisation (mix) versus UP/Uttarakhand government-set price rises? Disclose Q1 FY27 volume and realisation per case. | spirits FND-07 (AMBIGUOUS) |
| Q14 | Is the Rs 1,000 Cr EBITDA target "next 3-4 years" (~FY29-30) or FY31E? The deck states both. | spirits FND-08 (AMBIGUOUS) |
| Q15 | Ennature: give the FY24 and FY25 comparatives and the segment rupee split. Only FY26 (guar-contaminated) is shown; growth and the guar effect cannot be isolated. | EB A3-F16-01 (AMBIGUOUS) |
| Q16 | Ennature: disclose Thiocolchicoside revenue share and price, the nicotine end-market split, and product/customer concentration %. All three thesis variables are absent. | EB A3-F16-02 (AMBIGUOUS) |
| Q17 | Ennature: 20 total clinical trials but only 17 name a product (10/5/2). What are the other 3? | EB A3-F14-01 (AMBIGUOUS) |
| Q18 | Ennature: which bucket (filed / granted / under review) are the "2 US patents" in? | EB A3-F14-02 (AMBIGUOUS) |
| Q19 | Ennature: schedule the Berbisol trial readout and confirm the 1-new-API-per-year cadence delivery and US-office revenue ramp. | EB A3-F6-01/02/03 (FORWARD-SIGNAL) |

Every A3 FORWARD-SIGNAL and AMBIGUOUS finding across the three decks maps to at
least one question above. NEUTRAL-FACT drafting items (corp A5 Gases 50/47;
spirits FND-04 "Portable"/"Non-IFML"/"MaQintosh") are logged, not raised as
management questions; they feed the governance-noise note in the brief.

---

## STEP 9 — MONITORABLES / CATALYST LIST (seeded by A3 F6 commitment registers)

| Item | Implied date | Source | Watch |
|---|---|---|---|
| Demerger conclusion; first standalone-reporting quarter | 24-Oct-2026 | R229 / R269 | corp-action completion |
| Filed standalone opening balance sheets (all 3 entities) | Oct-Nov 2026 | thesis monitor; Q4 | Entity B <= ~1,050; Entity A ~813 net debt |
| Ennature first guar-free quarter (Q2 FY27) | Nov 2026 | EB A3-F16-01 | isolates guar effect; falsifier becomes testable |
| CARE rating post-demerger | post 1-Sep-2026 | thesis monitor | A- RWD resolution |
| IGL Spirits EBITDA > Rs 550 Cr; 2x IMFL volume | FY27 | R156 / R157 / R280 / R281 | promise-vs-delivery |
| IGL Spirits debt-free balance sheet | FY28 | R284 | leverage path; watch LC/BG |
| ESY 2026-27 ethanol allocation | ESY runs Nov 1 - Oct 31 | R351 / FND-02 | oversupply risk to bio-fuel leg |
| Clariant JV quarterly share >= ~46 Cr + 24% stake-sale agreement | FY28-29 for sale | R136 | Entity A's main asset |
| Bio-glycol realisation/MT vs Asia MEG | ongoing | R066 / R118 | Entity A falsifier |
| Berbisol clinical-trial readout | NOT DISCLOSED | R116 | Ennature catalyst |
| Rs 2,000 Cr rev / Rs 400 Cr EBITDA (Entity A) | ~FY30-31 | R100 / R101 | aspiration tracking |

---

## STEP 10 — SILENCE AUDIT (what each deck type would carry but omits)

### Entity A — residual India Glycols (corp deck)
| Omission | Verdict |
|---|---|
| Cash-flow statement | ROUTINE for a deck; SIGNAL here — the Adj. EBITDA headline has no cash backing |
| Balance sheet / net debt / net worth for residual IGL | SILENCE SIGNAL — Entity B discloses net debt, Entity A discloses none; asymmetric, blocks the ~813 trigger |
| Full Adj. EBITDA bridge (only a one-line footnote) | SILENCE SIGNAL — 66-114 Cr unexplained |
| Prior-year Bio-Glycol realisation / volume (only FY26) | SILENCE SIGNAL — blocks the bio-premium falsifier |
| Clariant JV 24% stake-sale plan | SILENCE — the thesis names it as Entity A's main value event |
| Page-14 segment build (1,070) vs total (1,164), ~94 Cr | SILENCE SIGNAL — segments do not tie |
| EPS / share count | ROUTINE |
| Novel Tech / Block 3 revenue or forecast | ROUTINE (disclaimed development-stage) but it is one of three 10X pillars |
| Prior-deck comparative for the EBITDA -> "Adj. EBITDA" reframe | NOT RUNNABLE (no prior deck); obtain next quarter |

### Entity B — IGL Spirits (spirits deck)
| Omission | Verdict |
|---|---|
| Cash-flow statement | SIGNAL — the debt-free-by-FY28 claim rests on cash generation |
| Net worth (RoCE denominator) | SILENCE SIGNAL — RoCE 20.5% not verifiable |
| Current ESY 2026-27 ethanol allocation | SILENCE SIGNAL — only ESY 2025-26 shown; the guide leans on bio-fuel tailwinds |
| Q1 FY27 volume / realisation per case | SILENCE SIGNAL — favourable annual actuals shown instead |
| Regulated-pricing driver of gross margin | SILENCE SIGNAL — never named though cases are flat |
| Non-fund-based LC/BG in net-debt definition | SILENCE SIGNAL — possible understatement vs the 1,050 trigger |
| Segment assets / liabilities | ROUTINE for a deck |

### Entity C — Ennature Biopharma (EB deck)
| Omission | Verdict |
|---|---|
| FY24 / FY25 comparatives (only FY26) | SILENCE SIGNAL — guar-contaminated single period, growth not isolable |
| Segment rupee split (only % mix) | SILENCE SIGNAL |
| Thiocolchicoside revenue share / price | SILENCE SIGNAL — thesis variable, falsifier untestable |
| Nicotine end-market split | SILENCE SIGNAL — thesis variable |
| Customer / product concentration % | SILENCE SIGNAL — only counts |
| Net debt / balance sheet | SILENCE — opening BS due Oct-Nov 2026 |
| Safe-harbor / forward-looking disclaimer (26 forward statements, only a confidentiality legend) | noted; governance data point |

Sustained silence on the deteriorating or thesis-critical metrics (Entity A core
revenue, bio-glycol realisation; Entity B regulated-pricing driver and current
ethanol allocation; Entity C the three concentration/product gaps) is
confirmatory, not neutral. Cross-quarter dropped-disclosure diffs (A3 F16) are
not runnable this pass — no prior deck supplied; run next quarter once these
become the baseline.

---

## STEP 11 — PLAIN-LANGUAGE BRIEF (mandatory; provenance five-tier: FILED / AGENCY / MGMT / SECONDARY / INFERENCE)

### 1. SUMMARY NARRATIVE

India Glycols splits into three listed companies on 1 September 2026. Three
investor decks tell each company's story. They are marketing, not the filings the
thesis waits for. The decks resolve one of nine thesis questions and leave eight
open [INFERENCE, this review].

Residual India Glycols shows a Rs 330 Cr adjusted EBITDA on Rs 1,164 Cr revenue,
a 28.4% margin [MGMT, R142/R145]. The unadjusted figure is Rs 169 Cr, a 14.5%
margin [MGMT, R038/R045]. The footnote says the gap is the Clariant joint-venture
profit share [MGMT, R291]. It is not. That share is about Rs 46.5 Cr [INFERENCE
from R136]. Even the full JV profit of Rs 95 Cr [MGMT, R136] leaves 66 to 114 Cr
of the gap unexplained. The core business revenue fell 26% in two years, from
Rs 1,581 Cr to Rs 1,164 Cr [MGMT, R137/R139]. Management calls this "revenue
moderation."

The corporate deck also contradicts itself. Page 7 labels IGL Spirits at Rs 246
Cr and Ennature at Rs 2,801 Cr [MGMT, R025/R027]. Page 12 and both standalone
decks show the opposite: IGL Spirits Rs 2,801 Cr, Ennature Rs 246 Cr [MGMT,
R053/R059, R125, R049]. Page 7 swapped the two businesses.

IGL Spirits looks the strongest of the three. Revenue nearly doubled to Rs 2,801
Cr [MGMT, R125], EBITDA reached Rs 492 Cr [MGMT, R135], net debt fell to Rs 767
Cr [MGMT, R147], below the Rs 1,050 Cr trigger. But cases were flat while gross
margin jumped to 45.9% [MGMT, R112/R119]. Revenue per case rose about 14% to
Rs 444 [INFERENCE from R128/R112]. The deck credits premiumisation. Flat volume
and a higher price per case point to government-set price rises. The deck never
says which.

Ennature shows only one year, Rs 246 Cr revenue at an 11.9% EBITDA margin [MGMT,
R049/R052], and it includes the guar business added at demerger. Growth cannot be
read from it.

No thesis-broken trigger fires. The Decision Status stays WATCHLIST / AVOID (DEEP
WATCH). The real evidence is the filed opening balance sheets in October to
November 2026 and Ennature's first guar-free quarter in November 2026.

### 2. SECTOR INTELLIGENCE

Three sectors, three regulatory regimes. Bio-based chemicals: the deck cites a
US$100bn market growing to US$208bn by 2032, 9.6% CAGR [MGMT/SECONDARY, RCI
Carbon, R070-R072]. Real but a price-taker rung for MEG; Amendment 17 binds the
converter slice [prior Notion]. Spirits: alcohol is state-regulated; UP and
Uttarakhand set both licences and prices [prior Notion]. The margin engine is
regulated pricing, not brand [INFERENCE]. Bio-fuel ethanol runs on the OMC quota;
blending is at 20% in 2026, targeted 21% by 2030 [MGMT, R067/R068], but the
current ESY 2026-27 allocation is undisclosed and the sector is oversupplied
[prior Notion, ~68%]. Nutraceuticals/APIs: a US$450bn global nutraceutical market
[MGMT/SECONDARY, R017]; Ennature is a single-product outsourcing supplier exposed
to Thiocolchicoside and nicotine demand [prior Notion].

### 3. BUSINESS-MODEL INTELLIGENCE

Entity A earns from selling bio-glycols and specialty chemicals and from a 49%
Clariant JV whose profit share (~Rs 46.5 Cr [INFERENCE, R136]) is its main asset.
Core chemical revenue is shrinking; the reported margin strength is JV-adjusted
[MGMT, R291; this review]. Entity B earns from potable spirits (Rs 1,331 Cr) and
bio-fuel ethanol (Rs 1,470 Cr) [MGMT, R128/R131]; bio-fuel is now the larger,
regulated-quota leg, so growth is policy-driven, not premiumisation [INFERENCE,
FND-02]. Potable realisation is about Rs 444 per case, up ~14% on flat volume
[INFERENCE from R128/R112]. Entity C earns from plant APIs, nutraceuticals and
guar biopolymer at an 11.9% EBITDA margin [MGMT, R052], a thin single-product
outsourcing model. This quarter shows model drift in one direction across all
three: the reported quality rests on adjustments, JV share and regulated price,
not on core volume or pricing power [INFERENCE].

### 4. COMPETITION INTELLIGENCE

Entity A claims to be the only maker of bio-ethylene glycols and the world's
largest bio-EO producer [MGMT, R179/R181]; the scarcity is real but the product
still clears at a commodity index, so pricing power is limited [INFERENCE].
Partners named — BASF, L'Oreal, Clariant, Bacardi [MGMT, R188] — show reach, not
captured wallet. Entity B ranks top-5 in Indian spirits by volume and #1 in
non-IMFL in UP and Uttarakhand [MGMT, R009/R010]; the moat is the excise licence
and captive ENA, not brand. Entity C competes in fragmented plant-API and
nutraceutical niches; concentration is undisclosed, so competitive durability
cannot be judged [SILENCE, EB]. The competitive risk to watch: Entity B's margin
depends on state excise policy staying favourable, and Entity A's earnings depend
on the Clariant JV holding its ~Rs 46 Cr share and completing the 24% stake sale.

---

## PROCESS VERDICT

**PROCEED WITH FLAGS.** The review is mechanically complete (798/798 disclosure
units reviewed, all three A2 gates pass, all A3 findings incorporated). No
mechanical failure. Flags that propagate: (1) the residual-IGL Adj. EBITDA bridge
is arithmetically insufficient by 66-114 Cr; (2) corp page 7 transposes IGL
Spirits and Ennature; (3) cash conversion is INDETERMINATE for Entity A and C,
INDETERMINATE-WITH-DIRECTION (improving) for Entity B, which caps the verdict
below a clean PROCEED; (4) eight of nine thesis variables remain open. This is a
PROCESS verdict on the review, not an investment Decision Status. The Decision
Status stays WATCHLIST / AVOID (DEEP WATCH); no trigger fired.

Loop 1 note: the one A5 FACTUAL finding (realisation-per-case 10x error) is
corrected at Step 2.5; two A5 STYLE items are logged (Step 2.3 p12 rounding;
Step 4.1 JV ownership-order assumption). No unchallenged step was reworked. The
process verdict is unchanged from the prior pass.

```yaml
stage: A4-analyst
company: "INDIAGLYCO"
quarter: "2026-09"
model: claude-opus-4-8
status: complete
docs_merged: [presentation-corp, presentation-spirits, presentation-eb]
ledger_reconciliation:
  notes: 0
  turns: 0
  slides: 78          # corp 32 + spirits 31 + EB 15 (798 disclosure units total)
  all_reviewed: true
  a3_findings_incorporated: [corp-A1, corp-A2, corp-A3, corp-A4, corp-A5, corp-A6, corp-A7, spirits-FND-01, spirits-FND-02, spirits-FND-03, spirits-FND-04, spirits-FND-05, spirits-FND-06, spirits-FND-07, spirits-FND-08, eb-A3-F6-01, eb-A3-F6-02, eb-A3-F6-03, eb-A3-F14-01, eb-A3-F14-02, eb-A3-F16-01, eb-A3-F16-02]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE"   # A + C INDETERMINATE; B INDETERMINATE-WITH-DIRECTION (improving)
decision_status_verified: "WATCHLIST / AVOID (DEEP WATCH, not actionable)"
position_branch: "8A"
sc_gap_pat_pct: []   # no S-vs-C PAT split in any deck (ND). Corp adj-vs-unadj EBITDA gap: FY24 108, FY25 182, FY26 161 Cr (not PAT)
questions_for_management:
  - {q: "Full Adj. EBITDA bridge for residual IGL; 66-114 Cr FY26 / 182 Cr FY25 unexplained by JV add-back", from_finding_id: corp-A1}
  - {q: "Corp p7 transposes IGL Spirits and Ennature vs p12 and standalone decks; confirm and reissue", from_finding_id: merged-4.2}
  - {q: "Which residual-IGL headline metrics are JV-inclusive vs ex-JV", from_finding_id: corp-A3}
  - {q: "Residual IGL opening net debt, working-capital days, net worth (none disclosed)", from_finding_id: corp-A1}
  - {q: "Confirm 24-Oct-2026 conclusion and first standalone-reporting quarter per entity", from_finding_id: corp-A2}
  - {q: "Which EBITDA basis (169 unadj vs 330 adj) will filed standalone accounts use", from_finding_id: corp-A7}
  - {q: "Opening balance sheet and CARE rating per resulting company", from_finding_id: corp-A6}
  - {q: "IGL Spirits: Q1 FY27 run-rate vs FY27 EBITDA>550 / 2x IMFL / FY28 debt-free", from_finding_id: spirits-FND-01}
  - {q: "Disclose ESY 2026-27 ethanol allocation (volume and value)", from_finding_id: spirits-FND-02}
  - {q: "IGL Spirits gross debt, LC/BG exposure, net worth to tie out 20.5% RoCE", from_finding_id: spirits-FND-03}
  - {q: "Restate FY24-26 PAT on a like-for-like (pre-bifurcation) basis", from_finding_id: spirits-FND-05}
  - {q: "Which Kashipur potable capacity is live today (FY26 actual vs FY27E mixed)", from_finding_id: spirits-FND-06}
  - {q: "Gross margin 36->45.9% on flat cases, realisation/case Rs ~391->444 (+14%): premiumisation or govt-set price? Disclose Q1 FY27 volume/realisation", from_finding_id: spirits-FND-07}
  - {q: "Rs 1,000 Cr EBITDA target: 3-4 years or FY31E?", from_finding_id: spirits-FND-08}
  - {q: "Ennature: FY24/FY25 comparatives and segment rupee split (only FY26, guar-contaminated)", from_finding_id: eb-A3-F16-01}
  - {q: "Ennature: Thiocolchicoside share/price, nicotine end-market split, concentration %", from_finding_id: eb-A3-F16-02}
  - {q: "Ennature: 20 total trials vs 17 named (10/5/2) - the other 3?", from_finding_id: eb-A3-F14-01}
  - {q: "Ennature: which bucket are the 2 US patents in?", from_finding_id: eb-A3-F14-02}
  - {q: "Ennature: Berbisol readout date, 1-API/year cadence, US-office revenue ramp", from_finding_id: eb-A3-F6-01}
monitorables:
  - {item: "Demerger conclusion; first standalone-reporting quarter", implied_date: "2026-10-24", source_ref: "R229/R269"}
  - {item: "Filed standalone opening balance sheets (B<=~1050, A~813 net debt)", implied_date: "2026-11", source_ref: "thesis-monitor"}
  - {item: "Ennature first guar-free quarter (Q2 FY27)", implied_date: "2026-11", source_ref: "eb-A3-F16-01"}
  - {item: "CARE rating post-demerger (A- RWD)", implied_date: "2026-09", source_ref: "thesis-monitor"}
  - {item: "IGL Spirits EBITDA>Rs550Cr / 2x IMFL volume", implied_date: "FY27", source_ref: "R156/R157"}
  - {item: "IGL Spirits debt-free balance sheet", implied_date: "FY28", source_ref: "R284"}
  - {item: "ESY 2026-27 ethanol allocation", implied_date: "2026-11 (ESY start)", source_ref: "R351/FND-02"}
  - {item: "Clariant JV quarterly share >=~46 Cr + 24% stake-sale agreement", implied_date: "FY28-29", source_ref: "R136"}
  - {item: "Bio-glycol realisation/MT vs Asia MEG", implied_date: "ongoing", source_ref: "R066/R118"}
  - {item: "Berbisol clinical-trial readout", implied_date: "NOT DISCLOSED", source_ref: "R116"}
flags: [FLAG-ADJ-EBITDA-UNRECONCILED-66-114CR, FLAG-P7-SPIRITS-ENNATURE-TRANSPOSED, FLAG-CASH-INDETERMINATE-A-AND-C, FLAG-EIGHT-OF-NINE-THESIS-GAPS-OPEN, FLAG-ENTITY-A-NETDEBT-UNTESTABLE, FLAG-SPIRITS-REGULATED-PRICING-UNNAMED, FLAG-ESY-2026-27-ABSENT, FLAG-STRUCTURAL-DEMERGER]
plain_language_brief_included: true
analyst_note: "Loop1 correction pass. A5 FACTUAL fixed: IGL Spirits potable realisation/case was 10x too high (Rs 3,788/3,907/4,437); restated Rs ~379/391/444 (947 Cr/25.0mn; 1,176/30.1; 1,331/30.0) at Step 2.5. +14% FY25->FY26 read and all conclusions unchanged (scale-invariant). Two A5 STYLE items logged, no substantive change: (1) India Glycols p12 Net Rev 1,163 vs 1,164 p7/p31 = source rounding; (2) Clariant share ~46.5 Cr assumes 51:49 = Clariant 51/IGL 49, IGL takes 49% x 95 Cr JV PAT. All A5-verified content carried forward verbatim: Adj.EBITDA reconciliation (330 vs 169, JV add-back leaves 66-114 Cr FY26 / 182 Cr FY25), corp p7 Spirits/Ennature transposition, Entity B net-debt trend 728/900/767, cash-quality direction. No thesis-broken trigger fires; Decision Status holds WATCHLIST/AVOID. Verdict unchanged PROCEED WITH FLAGS."
review_path: "runs/indiaglyco-2026-09-02/work/loop1/review_indiaglyco_2026-09.md"
```
