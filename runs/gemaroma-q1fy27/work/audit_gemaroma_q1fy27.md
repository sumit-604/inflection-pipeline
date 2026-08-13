# A5 ADVERSARY / COMPLETENESS AUDIT — Gem Aromatics Limited (GEMAROMA), Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-08-13
**Under audit:** review_gemaroma_q1fy27.md (A4 analyst)
**Method:** fresh context. I re-derived every derived metric independently from the A1 extracts (results in Rs Millions, x0.1 → Rs Cr; deck/PR in Rs Cr), re-ran the A2 enumeration by my own read of the extracts, and did not defer to A4's or A3's cites.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF located at review L491-507. All four labelled parts present and carry real, non-placeholder content:

| Part | Heading | Line | Status |
|---|---|---|---|
| 1. Summary narrative | "1. SUMMARY NARRATIVE" | L493-495 | PRESENT (one dense ~25-line paragraph: standalone-vs-consol split, FY26 prior contraction, gross-margin break, depreciation, non-operational standalone PAT, INDETERMINATE cash, WATCHLIST verdict, next checkpoint) |
| 2. Sector intelligence | "2. SECTOR INTELLIGENCE" | L497-499 | PRESENT (specialty ingredients, Madagascar clove RM cyclicality, forward-integration tailwind, Frost & Sullivan provenance caveat, 15% tax claim) |
| 3. Business-model intelligence | "3. BUSINESS-MODEL INTELLIGENCE" | L501-503 | PRESENT (segment/geography mix, named customers, flat-ratio-but-shrinking-base qualification, consol<standalone inversion, non-disclosed metrics) |
| 4. Competition intelligence | "4. COMPETITION INTELLIGENCE" | L505-507 | PRESENT (leadership claims, small-cap vs global players, input-cost weakness, execution risk, thin institutional ownership per Amendment 3) |

**Gate 0: PASS.** No part missing or empty.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers, then A4 citation check)

I re-counted each category from the extracts directly. My fresh counts equal every A2 ledger count and every figure A4 restated in its ledger-reconciliation preamble (L16-18).

### Results ledger (Reg 33)
| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes (15 numbered + 2 EPS footnotes) | 17 | 17 (std L227/231/234/236/253/256/257 =7; con L425/428/431/435/437/452/455/457 =8; footnotes L219/L417 =2) | none | PASS — covered in Step 0D notes table |
| Line items (29 std + 30 con) | 59 | 59 (extra con row = FX-translation L400) | none | PASS — Steps 1A/1B |
| Zero-standing (std prior-yr tax L194) | 1 | 1 | none material | PASS — nil template row, reviewed no-finding |
| Agenda items | 1 | 1 | none | PASS — note N1 board approval |
| Auditor paras (5 std + 6 con) | 11 | 11 | none | PASS — auditor-opinion + FIND-02 EoM |
| Consolidation entities | 2 | 2 (LLC, Krystal) | none | PASS — Con N3 / FIND-04 |
| Signature blocks | 5 | 5 | none | PASS — FIND-05 drafting note |

### Presentation ledger (33-slide deck)
| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 33 | 33 | none | PASS |
| Financial-table line items | 88 (17×3 P&L + 24 BS + 13 CF) | 88 | none | PASS — Steps 1-5 |
| Slide KPIs | 95 | 95 | none material | PASS — sector/business/competition brief |
| Charts | 3 | 3 | none | PASS — geography, shareholding, dashboard |
| Guidance statements | 11 | 11 | none | PASS — Monitorables + Questions |
| Capex/capacity (incl 2 DATA_ABSENT) | 14 | 14 | none | PASS — capacity+order-book silences named in business-model brief |
| Strategic claims | 17 | 17 | none | PASS — competition brief + Step 7 |
| Footnotes | 13 | 13 | none | PASS |

### Press-release ledger (5-page Reg 30)
| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Pages/sections | 5 | 5 | none | PASS |
| Financial line items (9 std + 9 con) | 18 | 18 | none | PASS |
| Narrative facts | 21 | 21 | none | PASS — customers/certs/16,171 MTPA in brief |
| MD-quote paragraphs | 5 | 5 | none | PASS — Section B |
| Forward statements | 13 | 13 | none | PASS — Monitorables |
| Regulatory items | 8 | 8 | none | PASS — board/Brazil |
| Earnings-call detail | 12 | 12 | none | PASS — Section B participants/date |

**Coverage verdict: PASS — zero orphan rows, zero rows my fresh pass found that the ledger lacks.** Three immaterial A2 internal-consistency micro-notes were NOT individually restated by A4 but do not constitute orphaned substantive findings and change nothing: (i) deck consol Q1FY26 EBITDA-margin comparator 16.9% (p7) vs 17.0% (p10 table) — a 0.1pt rounding gap; A4 correctly used 17.0% (my recompute = 16.96%); (ii) Rest-of-World footnote lists Uganda/Switzerland not shown as map markers (p23); (iii) "Diamond Pass Link" with no captured URL (PR E12). All immaterial; reviewed, no finding.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw millions; x0.1 conversion applied)

Every raw line in the results extract converts cleanly (e.g. Rev 829.86M→82.99; PBT 97.31M→9.73; con Rev 988.50M→98.85). All A4 derived metrics recomputed independently. Representative recomputation (all periods checked; showing Q1FY27 unless noted):

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Std Gross Profit Q1FY27 | 14.69 | 82.99−(70.81+(−2.51))=14.69 | L168/175/177 | MATCH |
| Std Gross Margin Q1FY27 | 17.7% | 14.69/82.99=17.70% | " | MATCH |
| Std Op EBITDA Q1FY27 | 8.51 | 9.731+1.606+1.334−4.157=8.51 | L187/182/180/170 | MATCH |
| Std Core PBT ex-OI Q1FY27 | 5.57 | 9.73−4.16=5.57 | L187/170 | MATCH |
| Std ETR (all periods) | 25.3/25.8/25.5/25.5% | 2.21/8.73…2.48/9.73=25.3…25.5% | L196/187 | MATCH |
| Std Rev YoY | +8.6% | (82.99−76.40)/76.40=8.63% | L168 | MATCH |
| Std Gross Profit YoY | −23.2% | (14.69−19.13)/19.13=−23.2% | derived | MATCH |
| Std Core PBT YoY | −9.3% | (5.574−6.147)/6.147=−9.3% | derived | MATCH |
| Std PAT bridge (sum) | +0.73 | −2.00−0.17+1.59+1.58−0.27=+0.73 (=7.25−6.52) | L199 | MATCH |
| Con Gross Profit Q1FY27 | 16.51 | 98.85−(99.04+(−16.70))=16.51 | L370/376/377 | MATCH |
| Con Gross Margin Q1FY27 | 16.7% | 16.51/98.85=16.70% | " | MATCH |
| Con Op EBITDA Q1FY27 (dep 9.13) | 3.31 | −8.54+9.13+2.88−0.16=3.31 | L385/380*/379/371 | MATCH |
| Con Op EBITDA margin Q1FY27 | 3.3% | 3.31/98.85=3.35% | derived | MATCH |
| Con Gross Margin YoY | −1,282 bps | 29.52%→16.70% | derived | MATCH |
| Con Op EBITDA YoY | −77.7% | (3.31−14.86)/14.86=−77.7% | derived | MATCH |
| Con Dep YoY | +401% | (9.13−1.82)/1.82=+401.6% | reconciled/L380 | MATCH |
| Con PBT YoY | −179.2% | (−8.54−10.79)/10.79=−179.2% | L385 | MATCH |
| Con PAT YoY | −198.6% | (−7.87−7.98)/7.98=−198.7% | L395 | MATCH |
| Con ETR FY26 | 77.6% | 4.94/6.36=77.6% | L392/385 | MATCH |
| Con PAT bridge (sum) | −15.86 | −11.55−7.31+0.64−1.11+3.47=−15.86 (=−7.87−7.98) | L395 | MATCH |
| S→C PAT gap Q1FY27 | (15.13) | −7.874−7.252=−15.13 | L199/395 | MATCH |
| S→C gap % std PAT Q1FY27 | −208.6% | −15.126/7.252=−208.6% | derived | MATCH |
| FY26 walk: Rev/EBITDA/PAT | −27.3/−54/−97% | (366.5−504)/504=−27.3; (40.8−88.5)/88.5=−53.9; (1.4−53.4)/53.4=−97.4 | deck L922/929/938 | MATCH |
| Trailing P/E (con FY26 EPS 0.28) | ~625x | 174.90/0.28=624.6x | deck L1056/L940 | MATCH |

**Depreciation reconciliation independently verified (load-bearing):** the results extract L380 OCR-reads con Q1FY27 depreciation as "5127" (5.13 Cr) and BOTH the A1 extract and A2 results ledger (row 10, section 3) faithfully carry that misread. I balanced the stated con total expenses independently: 990.38 − 167.02 + 70.64 + 28.83 + **X** + 61.44 = 1,075.54 ⟹ X = **91.27M = 9.13 Cr**, not 51.27. A4's reconciliation to Rs 9.13 Cr is therefore ARITHMETICALLY CORRECT and confirmed three ways (balancing figure, deck p10 "9.1", cash-PAT bridge). PBT (−8.54) and PAT (−7.87) reconcile independently (Total income 990.11 − Total expenses 1,075.54 = −85.43M ✓). **This is an A1/A2 transcription defect that A4 caught and handled transparently (Q11), not an A4 arithmetic error.** Recommend A1 correct extract L380 and A2 update ledger row; does not affect this gate.

**Arithmetic verdict: PASS — zero mismatches above rounding.** Every derived cell ties to within ±0.01 Cr / ±0.1pt rounding.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims; strongest same-text bear counter each)

**Mandated-present prior counters — confirmed present and adequate (NOT re-raised):**
- Gross-margin-collapse-above-depreciation (loop 1): present and thorough — Steps 1C/1D/2A/2B/4B, flag 2, Q2/Q6/Q13, plain-language. Adequate.
- FY26 −27% rev / −54% EBITDA / −97% PAT contraction + consol(366.5)<standalone(370.9) inversion (loop 2): present — Step 3C, flag 3, Q14, business-model brief. Adequate.

### Positive claim 1 — "The parent made a profit, PAT +11% YoY on revenue +8.6%" (review L495, L389, Step 2A)
**Strongest bear counter:** strip the Rs 4.16 Cr Other Income (up +61% YoY, now 42.7% of PBT, source undisclosed) and the Rs 1.59 Cr finance-cost fall, and standalone CORE PBT ex-OI fell −9.3%; on OI reverting to Rs 2.58 Cr, standalone PBT ≈ Rs 8.15 Cr, below prior year.
**Survives?** NO — already fully stated by A4 (Step 2A diag 4-6, Step 4A, Q12, plain-language). Adequate; no graft needed.

### Positive claim 2 — "The Dahej depreciation step-up is genuinely transitional fixed-cost absorption, the legitimate transition-alpha portion utilisation will cure" (Step 4B Problem 2, Step 8 component 3)
**Strongest bear counter:** the "transitional" label presumes absorbing volume arrives, yet every absorbing vertical is pre-revenue and back-end-loaded with hedges — Cooling Agents revenue only Q3FY27, Safranal end-Q2/Q3FY27, Phenol commercial "subject to completion of required approvals and quality processes" with revenue only Q4FY27 (PR L138-148, deck L277-280); the in-year absorbing base is tiny (Phenol Rs 5 Cr/~1%, Citral-Other Rs 36 Cr/~10%, deck L542/572); and ~Rs 265 of Rs 270 Cr is already capitalised (deck L243), so the ~Rs 9.1 Cr/qtr depreciation is locked in NOW regardless of whether volumes land.
**Survives?** NO (substantially covered) — A4 conditions the transitional read on "if the Q3-Q4 FY27 Krystal volume ramp arrives," flags all three catalysts as hedged/undated (Monitorables 1-5, Q5/Q7/Q8), and states "nothing in the filing quantifies when" (Step 3). The "depreciation already 98% locked in" framing is a marginal sharpening, not a materially new counter. No mandatory graft.

### Positive claim 3 — "Finance costs fell (deleveraging / IPO); net debt fell ~Rs 86 Cr on IPO proceeds; adequate near-term liquidity" (Step 2A, Step 4A "+1.59 recurring post-deleveraging", Step 5)
**Strongest bear counter (SURVIVES):** the deleveraging read is too benign once interest is set against collapsed operating profit. At consolidated level this quarter operating EBIT is NEGATIVE (−5.82 Cr, A4's own Step 2B) and operating EBITDA is only Rs 3.31 Cr against finance cost Rs 2.88 Cr (L379) — interest cover ≈ 1.15x, i.e. operations did NOT cover interest this quarter. And gross finance cost actually ROSE +57% in FY26 (Rs 8.1 → Rs 12.7 Cr, deck L932) despite the Aug-2025 IPO, with short-term borrowings still Rs 128.1 Cr against cash of only Rs 15.9 Cr at Mar-26 (deck L965/L967) on a group that just swung to a loss. So finance-cost reduction is a recent, partial, quarterly move, not a structural de-risking, and the interest burden is now nearly (con) or fully (con operating EBIT) uncovered by operations.
**Survives?** YES. Materially supported by the extracts and NOT stated anywhere in A4 — A4 never computes interest coverage, never notes operations fail to cover interest at consol, and never surfaces the FY26 +57% finance-cost rise; it presents finance-cost reduction only as an unqualified recurring positive. **Must be grafted into A4** (Step 5 and the Step 2A/4A "post-deleveraging" framing, plus a flag), and it strengthens the bear case, so it loops back to A4 before save.

---

## VERDICT

**INCOMPLETE.**

- **Failing agent:** A4.
- **Exact gap:** one surviving bear counter is not incorporated. A4 must graft the interest-burden / interest-coverage counter to positive-claim 3: at consolidated Q1FY27, operating EBIT is −5.82 Cr and operating EBITDA (3.31) barely exceeds finance cost (2.88) → interest cover ≈1.15x, operations do not cover interest; and FY26 gross finance cost rose +57% (8.1→12.7 Cr, deck L932) despite the IPO, with ST borrowings 128.1 vs cash 15.9 at Mar-26 (deck L965/L967). A4 currently frames finance-cost reduction only as a clean recurring positive (Steps 2A/4A) and calls liquidity "adequate" (Step 5) without this qualification. Graft into Step 5 + qualify Steps 2A/4A + add a flag, then re-submit.

Audits 0 (deliverable), 1 (coverage) and 2 (arithmetic) all PASS. The only bar to save is the unincorporated surviving bear counter above. (Separately, non-gating: recommend A1 correct results extract L380 depreciation 51.27→91.27 and A2 update the results ledger row; A4 already reconciled the true 9.13 Cr correctly.)

```yaml
stage: A5-adversary
company: "GEMAROMA"
quarter: "Q1FY27"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Finance costs fell (deleveraging/IPO); net debt fell ~Rs 86 Cr; adequate near-term liquidity"
    counter: "Consolidated operating EBIT is negative (-5.82 Cr) and operating EBITDA (3.31) barely exceeds finance cost (2.88) -> interest cover ~1.15x; operations did not cover interest this quarter. FY26 gross finance cost ROSE +57% (8.1->12.7 Cr) despite the Aug-2025 IPO, with ST borrowings 128.1 vs cash 15.9 at Mar-26. Deleveraging is recent/partial, not structural; interest burden now near-uncovered by operations on a loss-making group."
    source_line: "results L379 (con finance cost 2.88); A4 Step 2B con EBIT -5.82; deck L932 (FY26 fin cost 12.7 vs FY25 8.1); deck L965/L967 (ST borrowings 128.1, cash 15.9)"
loop_back_to: "A4"
gap: "Unincorporated surviving bear counter: graft the interest-coverage/finance-burden counter (con operating EBIT -5.82 and op EBITDA 3.31 vs finance cost 2.88 = ~1.15x cover; FY26 finance cost +57% to 12.7 Cr despite IPO; ST borrowings 128.1 vs cash 15.9) into Step 5 and qualify the 'post-deleveraging positive' framing in Steps 2A/4A, add a flag, then re-submit. Non-gating: A1 fix results L380 dep 51.27->91.27 and A2 update ledger; A4's 9.13 Cr reconciliation is already correct."
```
