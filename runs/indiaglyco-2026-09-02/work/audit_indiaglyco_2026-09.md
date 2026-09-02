# A5 ADVERSARY / COMPLETENESS AUDIT — India Glycols Limited (INDIAGLYCO) | 2026-09
## Merged three-deck demerger review (residual IGL "corp" + IGL Spirits + Ennature Biopharma)

Inputs read: A4 review; A1 fulltexts (3) and structured extractions (3, R-ranges
corp R001-R291 / spirits R001-R355 / eb R001-R152); A2 ledgers (3). Source PDFs and
`inputs/` NOT opened. Coverage re-run greps the FULLTEXT spines. Re-derived
independently; A4/A3 cites checked, not trusted.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

A4 STEP 11 PLAIN-LANGUAGE BRIEF, four labelled parts:

| Part | Present? | Evidence |
|---|---|---|
| 1. SUMMARY NARRATIVE | present | review L441-475, ~30 lines, real content |
| 2. SECTOR INTELLIGENCE | present | review L477-489, three regulatory regimes, anchored |
| 3. BUSINESS-MODEL INTELLIGENCE | present | review L491-503, all three entities, anchored |
| 4. COMPETITION INTELLIGENCE | present | review L505-517, per-entity, anchored |

Gate: PASS. All four present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep pass over the fulltext spines; diff vs A2 ledgers)

Independent counts:

| Deck | My fulltext `^[page ` count | A2 slides | My structured R-id count | A2 rows | orphan (ledger) | orphan (fresh-vs-ledger) | status |
|---|---|---|---|---|---|---|---|
| corp | 32 | 32 | 291 | 291 | none | none | PASS |
| spirits | 31 | 31 | 355 | 355 | none | none | PASS |
| eb | 15 | 15 | 152 | 152 | none | none | PASS |
| TOTAL | 78 | 78 | 798 | 798 | none | none | PASS |

All three A2 ledgers report `orphan_ids: []` with full ID accountability
(291/355/152 referenced = present). A4 STEP 1 confirms all 798 disclosure units
reviewed and lists the incorporated A3 finding IDs (corp A1-A7; spirits FND-01..08;
eb A3-F6-01/02/03, F14-01/02, F16-01/02). My fresh page-marker and R-id sweeps
reproduce every count exactly. No orphan row (ledger present, A4 absent). No
fresh-pass unit missing from any structured file. COVERAGE: PASS. (A3 reasoning is
out of my input scope; ledger-to-A4 accountability is fully satisfied.)

---

## AUDIT 2 — ARITHMETIC (recompute every derived metric from raw extracted numbers)

Priority tie-outs requested by the launcher, plus a full sweep of A4's tables.

### 2a. Residual-IGL Adj.EBITDA-vs-unadjusted reconciliation (priority 1) — TIES

| FY | Net Rev | Unadj EBITDA (p7) | Adj EBITDA (p31) | gap | my recompute |
|---|---|---|---|---|---|
| FY24 | 1,581 (R137) | 139 (R032) | 247 (R140) | 108 | 247-139 = 108 OK |
| FY25 | 1,291 (R138) | 130 (R035) | 312 (R141) | 182 | 312-130 = 182 OK |
| FY26 | 1,164 (R139) | 169 (R038) | 330 (R142) | 161 | 330-169 = 161 OK |

- JV PAT FY26 = 95 (R136); split 51:49 (R133); IGL 49% = 46.55. OK.
- 169 + 46.5 = 215.5 (not 330); 169 + 95 = 264 (not 330). Residual FY26 add-back
  = 66 (full-PAT basis) to 114 (49%-share basis). OK, matches A4 "66-114 Cr".
- FY25 gap 182 exceeds the entire FY26 JV PAT of 95. A4's "182 Cr unexplained" OK.
- Adj margins: 247/1581 = 15.6%, 312/1291 = 24.2%, 330/1164 = 28.35% ≈ 28.4%. OK.
- Unadj margins: 139/1581 = 8.8%, 130/1291 = 10.1%, 169/1164 = 14.5%. OK.
A4 4.1 and the 28.4% headline reconciliation are arithmetically correct.

### 2b. IGL Spirits net-debt trend + RoCE tie-out (priority 1) — TIES / correctly flagged

- Net debt 728/900/767 (R145-R147): rose 172 (900-728), fell 133 (900-767). OK.
- Net-debt/cash-profit: 728/159 = 4.58≈4.6; 900/248 = 3.63≈3.6; 767/395 = 1.94≈1.9. OK.
- Cash profit 159/248/395 rising. OK.
- RoCE 13.0/17.9/20.5 (R151-R153): cannot be independently tied out — net worth is
  undisclosed and RoCE denominator (R355: Net Worth + Term Loan) is unverifiable.
  A4 correctly flags this as un-tie-outable rather than asserting it. OK.

### 2c. Combined-group and p12 cross-foots — TIE

- FY26 segment rev 246+1,164+2,801 = 4,211 (R018). FY24 250+1,581+1,460 = 3,291.
  FY25 257+1,291+2,219 = 3,767. EBITDA FY26 29+169+492 = 690; FY24 423; FY25 521. OK.
- Rev CAGR (4211/3291)^.5-1 = 13.1%≈"c.13%"; EBITDA CAGR (690/423)^.5-1 = 27.7%≈"c.28%". OK.
- p12 shares: 2801/4211 = 66.5%≈67%; 1163/4211 = 27.6%≈28%; 247/4211 = 5.9%≈6%. OK.
- Spirits: PAT margins 88/1459=6.0%, 151/2219=6.8%, 244/2801=8.7%. Potable GM Cr
  341/947=36.0%, 493/1176=41.9%, 611/1331=45.9%. Bio-fuels 512->1470 = +187%. OK.
- Residual YoY 1164/1581 = -26.4%; Spirits 2801/1459 = +92%. OK.
- EB: 29/246 = 11.8%≈11.9% (R052). OK.

### 2d. ARITHMETIC MISMATCH FOUND (FACTUAL)

| Metric | A4 value | recomputed | source line |
|---|---|---|---|
| Spirits Potable realisation/case FY24 | Rs ~3,788 | Rs ~379 (947 Cr / 25.0 mn) | review L125-126; R113/R110 |
| Spirits Potable realisation/case FY25 | Rs ~3,907 | Rs ~391 (1,176 Cr / 30.1 mn) | review L125-126; R114/R111 |
| Spirits Potable realisation/case FY26 | Rs ~4,437 | Rs ~444 (1,331 Cr / 30.0 mn) | review L125-126; R115/R112 |

A4's derived per-case realisation is overstated by 10x. 947/25.0 = 37.88; the
per-case value in rupees is (947 x 10^7)/(25 x 10^6) = 378.8, not 3,788. Same 10x
scale error each year. The equation A4 prints ("947/25.0 = Rs ~3,788") is false on
its face. This is a "Derived (not in deck)" scratch figure that feeds NO headline,
table cell, cash-quality classification, thesis trigger, or verdict; the directional
conclusion A4 draws from it ("cases flat FY25->FY26; realisation per case rose ~14%")
is scale-invariant and SURVIVES (391 -> 444 = +13.6% ≈ 14%). But it is a real
arithmetic error above rounding, so per the arithmetic-audit rule it is a FAIL.
TYPE: FACTUAL. Loop: A4. Fix: restate the three per-case figures as ~Rs 379 / 391 /
444 (or drop the absolute figures and keep the +14% growth statement).

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest same-text bear)

Note: this is a DEMERGER, not an acquisition. No deck discloses a purchase price or
target earnings. The spirits deck names one brand "acquired" (Prestige Green Classic,
R226) but discloses no consideration and no target PAT, so the mandatory acquisition-
economics multiple cannot be computed and the probe DOES NOT FIRE. Per the launcher,
the SOTP / value-unlock narrative is stressed instead.

### Claim 1 — Residual IGL "value unlock" and the 28.4% Adj.EBITDA headline
Bear (same text): the 28.4% margin is JV-adjusted; the unadjusted margin is 14.5%
(R045) on a core top line that FELL 26% in two years (1,581 -> 1,164, R137/R139). The
Rs 330 Cr Adj.EBITDA rests on 66-114 Cr of add-backs the deck itemises only as a
one-line JV footnote (R291) that is arithmetically insufficient every year (FY25 gap
182 > full JV PAT 95). No cash-flow statement, no balance sheet, no net debt for the
residual entity (Step 5). A three-way SOTP "unlock" re-rates only if each standalone
earns a higher multiple; two of three pieces have INDETERMINATE cash conversion, so
the decks give no cash backing for a re-rating. "Value unlock" reads equally as "value
fragmentation" exposing three individually thinner disclosures.
SURVIVES. Already grafted in A4 (Steps 4.1, 5, 10, brief). Reconciles with thesis:
confirms WATCHLIST/AVOID (DEEP WATCH); the discount is not demonstrably closing
because the "quality" is adjustment-driven. No new graft required.

### Claim 2 — IGL Spirits: EBITDA >550 FY27 / 1,000 Cr / debt-free FY28 / 2x IMFL
Bear (same text): FY26 EBITDA is 492 (R135); >550 by FY27 is +12% and plausible, but
Rs 1,000 Cr requires doubling on a horizon the deck states TWO ways (3-4 yrs ~FY29-30,
R285, vs FY31E chart, R155 — conflict). "2x IMFL volume by FY27" is asserted while
total cases were FLAT FY25->FY26 (30.1 -> 30.0, R111/R112); growth to date came from
regulated Bio-fuels (+187%), not IMFL volume. "Debt-free by FY28" from net debt 767
(R147) has no cash-flow statement behind it, and net debt EXCLUDES non-fund-based
LC/BG (R355), a possible understatement. Gross margin 36.0 -> 45.9% on flat cases
points to state-set price rises, not durable premiumisation; the margin engine is
policy and reversible.
SURVIVES. Already grafted in A4 (Steps 4.4, 5, 6.2, 7, 8, brief). No new graft.

### Claim 3 — Ennature's growth
Bear (same text): Ennature discloses ONLY FY26 (Rs 246 Cr rev, 11.9% EBITDA margin,
R049/R052) and it INCLUDES the guar biopolymer added at demerger (R066). No FY24/FY25
comparatives, no segment rupee split, so "growth" is neither quantifiable nor
separable from the guar contribution. An 11.9% EBITDA margin is thin for a "high-value
branded ingredient" story; the branded push is 5 ingredients + 2 planned (R032/R033)
with customer/product concentration undisclosed (only counts 150+/23+/90+). The growth
claim is narrative only.
SURVIVES. Already grafted in A4 (Steps 2.6, 6.2, 10, brief). No new graft.

All three surviving bear counters are ALREADY present in the A4 review; no
NEW surviving counter is absent from A4, so the adversarial read triggers no loop.

---

## FINDINGS BY TYPE

FACTUAL (loops):
- F1. Spirits Potable realisation/case overstated 10x (Rs 3,788/3,907/4,437 should be
  ~Rs 379/391/444). review L125-126; source R113/R110, R114/R111, R115/R112. Loop A4.
  Non-load-bearing (growth +14% conclusion survives) but a real arithmetic error.

MISSING (loops): none.
CONTRADICTION (loops): none. (The corp p7 vs p12/standalone transposition and the
FND-08 Rs 1,000 Cr horizon conflict are DECK contradictions A4 already surfaced and
flagged, not agent-level contradictions in the review.)

STYLE (logged, no loop):
- S1. A4 Step 2.3 prints India Glycols p12 Net Rev as "1,163" while p7/p31 use 1,164;
  A4 reports both faithfully but does not explicitly label the 1 Cr as p12/p31 source
  rounding. Cosmetic; changes no conclusion.
- S2. A4 asserts "IGL 49% share" of the JV from R133's "51:49" without stating the
  ownership-order assumption; the 66-114 Cr reconciliation is robust to it (A4 shows
  both 49%-share 46.5 and full-PAT 95 bounds), so no number changes. Cosmetic.

---

## VERDICT

INCOMPLETE.

Failing agent: A4. Gap: one FACTUAL arithmetic error — the derived IGL Spirits
Potable-Spirits realisation-per-case is overstated by 10x (A4 Rs ~3,788/3,907/4,437;
correct ~Rs 379/391/444). Fix the three figures (or drop the absolute values and keep
the scale-invariant "+~14% FY25->FY26, cases flat" statement), then re-emit.

Everything else passes: deliverable gate (all four brief parts present), coverage
(798/798 units, zero orphans across three decks, independently re-counted), the
priority-1 Adj.EBITDA reconciliation and the Spirits net-debt/RoCE tie-outs, the p7
Spirits/Ennature transposition (independently confirmed from the fulltext p7 legend:
FY26 bars 246/1,164/2,801 rev and 29/169/492 EBITDA in IGL-Spirits/India-Glycols/
Ennature legend order, margins 11.9/14.5/17.6, all matching the standalone decks with
the two outer columns swapped), and all three surviving bear counters (already grafted
in A4). The Decision Status WATCHLIST/AVOID is unaffected; no thesis trigger fires.

```yaml
stage: A5-adversary
company: "INDIAGLYCO"
quarter: "2026-09"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "IGL Spirits Potable realisation/case FY24", a4_value: "Rs ~3,788", recomputed: "Rs ~379 (947 Cr / 25.0 mn)", source_line: "review L125-126; R113/R110"}
  - {metric: "IGL Spirits Potable realisation/case FY25", a4_value: "Rs ~3,907", recomputed: "Rs ~391 (1,176 Cr / 30.1 mn)", source_line: "review L125-126; R114/R111"}
  - {metric: "IGL Spirits Potable realisation/case FY26", a4_value: "Rs ~4,437", recomputed: "Rs ~444 (1,331 Cr / 30.0 mn)", source_line: "review L125-126; R115/R112"}
surviving_bear_counters:
  - {claim: "Residual IGL value-unlock / 28.4% Adj.EBITDA headline", counter: "28.4% is JV-adjusted (unadj 14.5%) on a core top line down 26%; 66-114 Cr of add-backs un-itemised beyond an insufficient JV footnote; no cash flow / BS; SOTP re-rating unbacked", source_line: "R045/R137/R139/R291/R136; review 4.1/5/10", type: MISSING}
  - {claim: "IGL Spirits EBITDA>550 FY27 / 1,000 Cr / debt-free FY28 / 2x IMFL", counter: "1,000 Cr horizon stated two ways (FND-08); 2x IMFL asserted on FLAT cases 30.1->30.0; debt-free unbacked by cash flow, net debt excludes LC/BG; 36->45.9% GM on flat volume = state-set price, not premiumisation", source_line: "R135/R155/R285/R111/R112/R147/R355/R119; review 4.4/5/6.2/7/8", type: MISSING}
  - {claim: "Ennature growth", counter: "only FY26 disclosed, guar-contaminated, no FY24/25 comparatives or rupee split; 11.9% margin thin; concentration undisclosed; growth is narrative only", source_line: "R049/R052/R066/R032/R033; review 2.6/6.2/10", type: MISSING}
findings_by_type:
  factual:
    - "IGL Spirits Potable realisation/case overstated 10x (Rs 3,788/3,907/4,437 vs correct ~379/391/444); review L125-126; source R113/R110, R114/R111, R115/R112; loop A4; non-load-bearing but a real arithmetic error above rounding"
  missing: []
  contradiction: []
  style:
    - "A4 2.3 prints India Glycols p12 Net Rev 1,163 vs p7/p31 1,164 without labelling the 1 Cr as source rounding; no conclusion change"
    - "A4 assumes IGL 49% JV share from R133 '51:49' without stating the ownership-order assumption; reconciliation robust (shows 46.5 and 95 bounds); no number changes"
surviving_bear_counters_note: "all three counters already grafted in A4; none absent, so adversarial read triggers no loop"
loop_back_to: "A4"
gap: "One FACTUAL arithmetic error: derived IGL Spirits Potable realisation/case overstated 10x (A4 Rs ~3,788/3,907/4,437; correct ~Rs 379/391/444, = 947/25.0, 1176/30.1, 1331/30.0). Restate the three figures or drop the absolute values and keep the scale-invariant '+~14% FY25->FY26, cases flat' statement, then re-emit."
style_notes:
  - "India Glycols p12 Net Rev 1,163 vs 1,164 elsewhere: label as source rounding"
  - "State the JV 49%/51% ownership-order assumption behind the Clariant share"
analyst_note: "Deliverable gate, coverage (798/798 units across 3 decks, zero orphans, independently re-counted 32/291, 31/355, 15/152), and every priority tie-out PASS. Adj.EBITDA reconciliation is correct: FY26 gap 161, JV add-back 46.5-95 leaves 66-114 Cr un-itemised; FY25 gap 182 > full JV PAT 95. Net-debt 728/900/767 and ND/cash-profit 4.6/3.6/1.9 tie; RoCE 20.5% correctly flagged un-tie-outable (net worth undisclosed). p7 transposition independently confirmed from the fulltext legend, not just A1 labels. All three bear counters survive and are already in A4. Only defect: A4's 'Derived (not in deck)' Potable realisation/case is 10x too high (947/25.0 = 37.88 -> per-case ~Rs 379, not 3,788). It feeds no headline or verdict and the +14% growth read is scale-invariant, so it is cosmetic in impact but a genuine arithmetic error, which under the strict arithmetic-audit rule fails the gate. Single-line fix at A4; no re-enumeration, no A2/A3 loop. Decision Status WATCHLIST/AVOID unaffected."
```
