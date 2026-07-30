# A5 ADVERSARY / COMPLETENESS AUDIT — PNGS Reva Diamond Jewellery (PNGSREVA) — Q1 FY27 (merged, THREE documents)

Independent audit of the three-document merged A4 review
(`review_pngs_q1fy27_merged.md`). Fresh context: re-derived from the A1 extracts
(results / presentation / concall) and diffed against the A2 ledgers. A4's and A3's
cites were checked, not trusted. This OVERWRITES the earlier two-document audit.
Units: filing/deck Rs Mn x0.1 = Rs Cr; concall mixed (P&L Rs Cr shorthand, finance-cost
split Rs Mn, AOV Rs Lakh, turn a ratio).

Role 5 is LIVE this run; the seven targeted concall verifications requested are in
Section 4.

---

## 1. COVERAGE AUDIT (fresh enumeration vs A2 ledgers; then ledger-row → A4 tie-out)

### 1a. Fresh count vs A2 counts

| Doc | Category | A2 count | My fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|---|
| Results | Notes | 7 | 7 (l.242,246,251,257,259,261,281) | none | PASS |
| Results | P&L value rows | 24 | 24 (l.178–223; 2 label fragments l.192/215 correctly excluded) | none | PASS |
| Results | P&L structural rows | 6 | 6 | none | PASS |
| Results | Auditor paras | 4 | 4 (l.82,88,97,125) | none | PASS |
| Results | Agenda items | 1 | 1 (l.15–46, single "approved") | none | PASS |
| Results | IPO-utilisation rows (+footnote) | 4 (+1) | 4 (+1) (l.273,274,277,278,279) | none | PASS |
| Results | Mgmt-comment items | 4 | 4 (l.309,333,338,342) | see 1b | PASS (minor note) |
| Results | Revenue sub-table | 3 | 3 (l.318,319,320) | none | PASS |
| Results | Signature blocks | 4 | 4 | none | PASS |
| Results | Entities | 1 | 1 (standalone) | none | PASS |
| Results | ZERO_STANDING | 2 | 2 (Earlier-year tax l.200; Other equity l.219) | none | PASS |
| Presentation | Slides | 33 | 33 (grep=sweep=pdfinfo) | none | PASS |
| Presentation | Fin-stmt line items | 48 | 48 (P&L 15 + BS 26 + CF 7) | none | PASS |
| Presentation | KPI/chart datapoints | 121 | 121 (per-slide subtotals reconcile) | none | PASS |
| Presentation | Footnotes | 6 | 6 | none | PASS |
| Presentation | Identifiers | 8 | 8 | none | PASS |
| Presentation | Personnel roster | 9 | 9 | none | PASS |
| Presentation | ZERO_STANDING | 6 | 6 | none | PASS |
| Concall | Turns | 103 | 103 (counted speaker segments l.40→264; my tally = 103) | none | PASS |
| Concall | Questions | 35 | 35 (Q1–Q35, incl. Q20 interrupted, multi-part per-part) | none | PASS |
| Concall | Mgmt quantified claims | 76 | 76 (73 + 3 ZERO_STANDING MN34/66/76) | none | PASS |
| Concall | ZERO_STANDING | 3 | 3 (MN34 EBO SSG nil; MN66 no ambassador; MN76 undrawn gold-loan/no MCX) | none | PASS |

**Concall turn re-count (independent):** counting every distinct speaker segment from
l.40 to l.264 yields exactly 103, matching the ledger's line-anchored T1–T103 table
(groups: 5+7+10+10+4+4+1+12+9+6+8+6+4+14+3 = 103). No missing-from-ledger row surfaced on
any of the three documents. No count mismatch.

### 1b. Ledger-row → A4 tie-out (orphan check)

Every A3 finding the A4 preamble claims to incorporate (8 results FN, 16 presentation
A3-F, 25 concall F/R) is present and cited in the body. Spot-audited the discrepancy
rows that MUST reach the verdict — all land:

- Gross margin 35% vs 36% waterfall (A3-F14-01) → flags list. Cited.
- Store count 37 vs 33 (A3-F14-02) → monitoring #1, Q5. Cited.
- CF cash 1,142 vs BS 3,242 = Rs210 Cr gap (A3-F14-03) → Step 5.2, Q7, flag. Cited.
- ROCE/ROE stale FY26 under Q1 header (A3-F16-03) → Step 6A, Q15. Cited.
- PNGS Gargi Rs150 Cr other-entity (A3-F16-04) → 6C trigger 6, Q18. Cited.
- Cost-line YoY/QoQ % suppressed (A3-F16-05) → Step 1 note, Q3. Cited.
- Deck P&L ties to filing (A3-F16-06) → Step 0.5. Cited.
- Finance-cost split impossible (F14.1), AOV decline (F14.2), OI=FD interest (R1),
  turn 1.29x FY26 basis (R2), 95% dependency (F17.2), cash dismissal (F17.1),
  CEO/CFO absence (F17.4) → all cited and carried to the verdict.

**One minor observation (NOT an orphan FAIL):** results Mgmt-comment item #4 —
"Rs30.00mn advance tax paid for TY2026-27 up to 29-Jul" (l.342–343) — is enumerated in
the results ledger (§6 item 4) and category-marked "reviewed" in the A4 preamble, but is
not individually cited in A4's body. It is a routine, immaterial disclosure (Rs3 Cr
advance tax) with no thesis bearing; it is covered at category level by the preamble's
"reviewed" assertion, so it does NOT rise to an orphan requiring an A3 loop-back. Logged
for record only.

**COVERAGE AUDIT: PASS.** Fresh counts equal A2 on all three documents; no
missing-from-ledger row; no material orphan row.

---

## 2. ARITHMETIC AUDIT (recomputed from raw filing/deck numbers)

All recomputed from filing raw Rs Mn (l.178–223) ÷10, deck raw (slides 10/29/30), and
concall spoken figures. "MATCH" = within rounding.

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Cost of materials Q1FY27 | 76.141 | 106.619 + (−30.478) = 76.141 | f.183+184 | MATCH |
| Gross Profit Q1FY27 | 41.832 | 117.973 − 76.141 = 41.832 | derived | MATCH |
| Gross Margin Q1FY27 | 35.46% | 41.832/117.973 = 35.46% | derived | MATCH (=MN8) |
| Operating EBITDA Q1FY27 | 33.927 | 36.398+0.357+2.748−5.576 = 33.927 | PBT+D+FC−OI | MATCH (=MN9) |
| Op EBITDA margin Q1FY27 | 28.76% | 33.927/117.973 = 28.76% | derived | MATCH (=MN11) |
| Op EBITDA margin Q1FY26 | 21.55% | 11.583/53.749 = 21.55% | derived | MATCH |
| Op EBITDA margin bps YoY | +721 bps | 28.76 − 21.55 = 7.21pp | derived | MATCH |
| Reported EBITDA margin Q1FY27 | 33.49% | 39.503/117.973 = 33.49% | derived | MATCH |
| Reported EBITDA bps YoY | +1141 bps | 33.49 − 22.08 = 11.41pp | derived | MATCH |
| Core PBT ex-OI Q1FY27 | 30.822 | 36.398 − 5.576 = 30.822 | derived | MATCH |
| Core PBT ex-OI YoY | +222.41% | (30.822−9.560)/9.560 | derived | MATCH |
| OI/PBT Q1FY27 | 15.32% | 5.576/36.398 = 15.32% | derived | MATCH |
| Effective tax rate Q1FY27 | 25.24% | 9.188/36.398 = 25.24% | f.201/195 | MATCH |
| PAT margin Q1FY27 | 23.06% | 27.210/117.973 = 23.06% | derived | MATCH (=MN14) |
| Revenue YoY | +119.49% | (117.973−53.749)/53.749 | f.178 | MATCH (MN5 "119.5") |
| Op EBITDA YoY | +192.90% | (33.927−11.583)/11.583 | derived | MATCH |
| Depreciation YoY | +839.47% | (0.357−0.038)/0.038 | f.187 | MATCH |
| Finance cost YoY | +38.44% | (2.748−1.985)/1.985 | f.186 | MATCH |
| Other Income YoY | +1842.86% | (5.576−0.287)/0.287 | f.179 | MATCH |
| Reported PBT YoY | +269.64% | (36.398−9.847)/9.847 | f.195 | MATCH |
| PAT YoY | +265.33% | (27.210−7.448)/7.448 | f.203 | MATCH (=MN13) |
| EPS YoY | +151.61% | (8.58−3.41)/3.41 | f.222 | MATCH |
| Revenue QoQ | −14.59% | (117.973−138.126)/138.126 | f.178 | MATCH |
| Core PBT ex-OI QoQ | +13.23% | (30.822−27.220)/27.220 | derived | MATCH |
| PAT QoQ | +27.10% | (27.210−21.409)/21.409 | f.203 | MATCH |
| PAT bridge (pre-tax) | +26.551 | 24.914−0.821−0.319−0.763−1.749+5.289 | Step 4 | MATCH = PBT Δ |
| PAT bridge (post-tax) | +19.762 | 26.551 − 6.789 (tax Δ) | derived | MATCH |
| Vol@prior-GM contribution | +20.218 | 64.224 × 31.48% | Step 4 | MATCH |
| Margin-mix contribution | +4.695 | 117.973 × 3.98pp | Step 4 | MATCH |
| OI after-tax as % of PAT Δ | ≈20.0% | 5.289×0.7476 = 3.954; /19.762 | Step 4 | MATCH |
| Ex-excess-OI PBT / PAT | 31.109 / 23.257 (+212%) | 36.398−5.289=31.109; ×0.7476=23.257 | Step 2/4/5 | MATCH (see note) |
| FY26 CFO/PAT | −1.62x | −104.8 / 64.655 = −1.621x | d.931 / f.203 | MATCH |
| FY26 inventory turn | ≈1.23x | 317.568 / ((179.4+335.6)/2) = 1.233x | deck BS/CF | MATCH |
| Mar-26 cash gap | ~Rs210 Cr | 324.2 − 114.2 = 210.0 | d.907 vs d.943 | MATCH |
| FY26 net cash (BS basis) | 158.3 | 324.2 − 165.9 = 158.3 | d.907/d.903 | MATCH |
| FY26 ROCE (incl idle) | 14.1% | (86.472+9.867)/681.1 = 14.14% | EBIT/CapEmp | MATCH (~audited 14.16%) |
| Trailing PE | 13.19x | 374.8 / 28.41 = 13.19x | CMP/EPS | MATCH |
| Hurdle: Dest/Current | 1.44x | 19 / 13.19 = 1.44x | Step 7 | MATCH |
| Hurdle: req (1+CAGR)³ | ≥1.356 → CAGR ≥10.7% | 1.953/1.44=1.356; ^(1/3)−1=10.7% | Step 7 | MATCH |
| Q1 as % of FY26 rev / PAT / EPS | 26.9% / 42.1% / 30.2% | 26.87% / 42.09% / 30.2% | derived | MATCH |
| Materials/Employee/Other YoY | +106.7 / +55.9 / +45.2% | 106.7 / 55.9 / 45.2% | derived | MATCH |
| AOV YoY (deck) | +8% (F14.2) | (100,232−92,624)/92,624 = 8.21% | C37/C38 | MATCH |
| Finance-cost split | impossible; Rs95mn misstated | 26.53+95=121.53≠27; **26.53+0.95=27.48**=filing | c.l.130 / f.186 | MATCH (see below) |

**Note (ex-OI labelling):** two ex-OI figures coexist — "Core PBT ex-OI 30.822 /
+222.41%" (removes ALL OI both years) and "ex-OI run-rate PBT 31.109 / PAT 23.257 /
+212%" (removes only the +5.289 EXCESS OI vs the retained Q1FY26 base 0.287). Both are
arithmetically correct; the labels are loose but there is no computation error. Not a
mismatch.

**Finance-cost split (verifies task item b):** the stated split is arithmetically
impossible (Rs26.53mn + Rs95mn = Rs121.53mn ≠ Rs27mn total; Rs95mn alone > Rs27mn). The
filing finance cost is Rs27.48mn (l.186). Rs26.53mn + **Rs0.95mn = Rs27.48mn** ties
EXACTLY to the filing, so the misstatement is specifically Rs95mn → Rs0.95mn, and the
filing total is intact. A4's read (filing total intact; Rs95mn is the misstatement;
data-quality signal, not a restatement; routed to management as Q8) is CORRECT. A4 offers
"likely Rs9.5mn / Rs0.95mn"; the exact tie proves Rs0.95mn — a marginal under-precision,
not an error.

**ARITHMETIC AUDIT: PASS.** Zero mismatches above rounding across the full data table,
derived metrics, YoY/QoQ set, PAT bridge, cash-quality ratios, ROCE, and the hurdle math.

---

## 3. ADVERSARIAL READ — three most positive claims, strongest bear counter each

The device: build the strongest bear counter FROM THE SAME EXTRACTED TEXT and test
whether it survives and must be grafted into A4.

**Positive claim 1 — Revenue +119.49% YoY, 2nd consecutive >100% quarter, volume-led
(>50% carats, MN32), operating thesis STRENGTHENING (at/above base-bull).**
- Bear counter (from extract): the base is a low, special-purpose-audited Q1FY26 (Note 5)
  in the SMALLEST seasonal quarter (~15% of annual, MN56/59); revenue actually DECLINED
  −14.59% QoQ (f.178); and ~95% of sales flow through the parent P.N. Gadgil & Sons SIS
  channel (MN45) while the parent-group sister PJS Gadgil grew only ~11% (analyst-stated,
  l.139) — raising a related-party channel-loading question the print may be flattering.
- Survives? YES (all extract-supported). **Already incorporated in A4** — Step 2
  diagnostic 1 (low/seasonal base), Step 3 (−14.59% QoQ), Step 6C (95% dependency + PJS
  divergence reconciliation), Q4. No grafting needed.

**Positive claim 2 — Operating EBITDA margin 28.76% (+721 bps), GM 35.46%: margin
expansion.**
- Bear counter (from extract): management itself does NOT underwrite 28.76% — it guides
  full-year DOWN to 25-27% EBITDA / 20-23% PAT with a 200-300 bps H2 marketing dent
  (MN26/27/72); GM was lifted by "better carat price realization" in a favourable
  Akshaya-Tritiya quarter (+268%, MN15-17); and the deck SUPPRESSED YoY/QoQ % on all
  three cost lines (SELECTIVE_DISCLOSURE, A3-F16-05), obscuring cost scaling. Durability
  unverified (FN7).
- Survives? YES. **Already incorporated** — Step 2 diagnostic 2, FN7, growth trigger
  "CONFIRMED-TO-MODERATE," Q3. No grafting needed.

**Positive claim 3 — Core operating PBT ex-OI +222.41%; "≈80% recurring core":
high earnings quality.**
- Bear counter (from extract): the "recurring core" is an accrual-P&L construct unbacked
  by cash — the Rs30.478 Cr FG inventory build (f.184) ≈ full-quarter PAT was dismissed as
  "routine" with NO CFO number (l.116, F17.1); FY26 CFO/PAT was −1.62x (d.931); Q1 cash
  conversion is INDETERMINATE; and Rs5.576 Cr OI (15.3% of PBT) is transient IPO-FD
  interest that erodes as cash deploys (R1).
- Survives? YES. **Already incorporated** — Step 5 headline + 5.3, Step 4 answers, Step 2
  diagnostic 6, verdict flags 1/2/4. No grafting needed.

**ADVERSARIAL READ result:** all three strongest bear counters are extract-supported AND
already present in A4 with symmetric weight. **No surviving un-incorporated counter →
no A4 loop-back on adversarial grounds.** The merged review is symmetric bull-bear.

---

## 4. TARGETED ROLE-5 VERIFICATIONS (task items a–g)

| # | Claim to verify | My finding | Verdict |
|---|---|---|---|
| a | Concall gave NO Q1 cash flow → cash conversion INDETERMINATE | FG build Rs30 Cr called "routine, sales up" (l.116, MN37); no CFO figure anywhere in transcript; no Jun-26 BS in any doc | SUPPORTED — correct |
| b | Finance-cost split impossible (26.53+95 vs 27; filing 27.48mn) | 26.53+95=121.53≠27; 95>27; but 26.53+0.95=27.48=filing exactly. Filing total intact; Rs95mn is the misstatement | SUPPORTED — correct (Rs0.95mn precise) |
| c | AOV Rs1.29L→1.12L→1.00L; deck "+8% YoY" AND concall QoQ-decline both true | Deck 92,624→100,232 = +8.21% YoY (C37/C38); concall 1.29L(Mar-26)→1.12L(last qtr,MN63)→1.00L(Q1,MN64), ~7-8% dent (MN65). Both true; the 1.29 vs 1.12 for Mar-26 is an unreconciled AOV_FIGURE_DISCREPANCY, correctly flagged and routed (Q9) | SUPPORTED — correct |
| d | Other Income confirmed as IPO-FD interest | l.99/103 (MN36/R1): "IPO proceeds parked in our bank yielding interest... entirely interest income treasury income" ties Rs5.576 Cr (f.179) | SUPPORTED — correct |
| e | ~95% parent-dependency vs 10.77% customer reconciled; trigger #8 correctly NOT fired | Note 3 (<10% single customer/group, reported-revenue/end-customer basis) vs ~95% CHANNEL throughput via parent SIS (MN45). Distinct metrics; trigger #8 (single customer >20% reported revenue) does not fire; "undisclosed" limb also not met (now volunteered). A4 escalates to monitoring and preserves the open related-party question (Q4) rather than declaring it resolved | SUPPORTED — reconciliation sound; non-fire defensible |
| f | Role 5 credibility ratio / grade / archetype supported, not overstated | Trailing-4Q ratio N/A (first call) — correct; interim answer-engagement 26/32 = 81% — arithmetically correct and explicitly caveated as overstating quality on the load-bearing cash item; grade B− provisional; archetype "COMMITTED & CREDIBLE (candidate)" carries an explicit OVERPROMISER-RISK flag and defers to Q2/H1 delivery. Credibility is NOT awarded on a first call | SUPPORTED — appropriately hedged, not overstated |
| g | Inventory turn 1.29x is deck's FY26 basis; Q1 turn NOT independently computable | Deck footnote D2 "Inventory Turn calculated on annualized basis" (C5); concall "1.29X during the quarter" (MN1/54) repeats it; no Jun-26 BS. A4 treats Q1 turn as NOT independently computable, marks monitoring #7 GREEN-on-stated-figure/UNVERIFIED-for-Q1, trigger #2 NOT computable — does NOT treat 1.29x as a clean Q1 resolution | SUPPORTED — correct |

All seven targeted verifications pass.

---

## 5. VERDICT

**COMPLETE.**

- COVERAGE: fresh enumeration equals A2 on all three documents (7 notes / 33 slides /
  103 turns and every sub-category); no missing-from-ledger row; no material orphan row
  (one immaterial routine row — Rs30mn advance tax — is category-reviewed and logged, not
  an orphan FAIL).
- ARITHMETIC: every derived metric recomputed from raw numbers ties within rounding; zero
  mismatches, including the PAT bridge, cash-quality ratios, ROCE, the hurdle math, and
  the finance-cost impossibility (which A4 diagnosed correctly).
- ADVERSARIAL: the three strongest bear counters are all extract-supported AND already
  incorporated in A4 with symmetric weight; no surviving un-incorporated counter.
- All seven Role-5 targeted verifications (a–g) confirmed.

No loop-back to A2, A3, or A4 is required. Cleared to proceed to Notion save.

```yaml
stage: A5-adversary
company: "PNGSREVA"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
