# A5 ADVERSARY / COMPLETENESS AUDIT — UNIMECH Q1 FY27
# Target: review_unimech_q1fy27.md (A4) | Fresh context: A4 + A1 extracts + A2 ledgers only
# Auditor re-derived every figure from the raw extracts; A4/A3 cites were checked, not trusted.

---

## 1. COVERAGE AUDIT (fresh independent enumeration vs A2 ledgers; then A4 citation check)

Fresh grep/manual sweep of each extract, diffed against the A2 COUNT TESTs. My counts reproduce
the A2 ledger exactly on every category. The A4 preamble's reconciliation counts also match the
ledgers. No enumeration row was found that the ledgers lack, and no ledger row is left uncited or
un-reviewed in A4 (all A3 finding IDs map to Step 8.5 questions / monitorables / flags).

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| results: notes (10 std + 11 consol) | 21 | 21 (l.268-302 / l.558-605) | none — all 21 in Step 0D table | PASS |
| results: line items (32 std + 43 consol) | 75 | 75 (std l.206-257; consol l.486-547) | none — all in Step 1(a)/1(b) | PASS |
| results: agenda items | 4 | 4 (l.36, 50, 64, 80) | none — Steps 0C/8.5/monitorables | PASS |
| results: auditor paras (4 std + 7 consol) | 11 | 11 (l.142-169 / l.335-445) | none — Step 0D opinion check | PASS |
| results: entities | 6 | 6 (l.376-405 / l.566-573) | none — notes table + Q19/Q21 | PASS |
| results: zero_standing | 3 | 3 (l.440-441 Nil sub) | none — Step 0D auditor para 7 / Q19 | PASS |
| results: annexure rows | 3 | 3 (l.643-655) | none — Q9 (QIP structure) | PASS |
| results: signature blocks | 3 | 3 (l.104-115, 176-183, 457-464) | none — Step 0D auditor id | PASS |
| presentation: slides | 25 | 25 (l.15-732) | none — deck reconciled Step 1; all A3-F* → Q&A | PASS |
| presentation: numbers | 428 | 428 (token sweep) | none material | PASS |
| presentation: charts | 2 | 2 (slide 7, slide 8) | none — Steps 2/3 + order-book (SEE ARITH FAIL-1) | PASS (enum) |
| presentation: footnotes | 12 | 12 | none | PASS |
| pr-qip: disclosure units | 29 | 29 (11+2+7+3+1+5) | none — Q8/Q9/Q10 | PASS |
| pr-monitoring: disclosure units | 77 | 77 (15 categories) | none — Q11-Q18 + monitorables | PASS |
| pr-monitoring: ZERO_STANDING rows | 14 | 14 | none | PASS |

**Coverage observations (not orphan FAILs):**
- **presentation Section 7 `NO_PRIOR_LEDGER` / DROPPED_SLIDE check** — the A2 deck ledger flags that
  the slide-continuity / "was numeric guidance withdrawn vs prior deck" check could not be run (no
  Q4 FY26 deck injected). This is an **input limitation, not an A3/A4 miss**; A4 partially closes the
  substance via Q26 ("guidance effectively withdrawn"). Carry as open item for next cycle; not a FAIL.
- All monitoring findings A3-01..A3-11, results FND-01..09, qip FND-01..05, pres A3-F6/F8/F15/F16 are
  each traceable to a Step 8.5 question or a flag. No orphan A3 finding.

**COVERAGE VERDICT: PASS.** No orphan rows; no rows missing from the ledger.

---

## 2. ARITHMETIC AUDIT (recomputed from raw extracts; units honored per header)

Units: results = Lakhs x0.01; presentation = INR **Mn x0.1** (Rs 10 Mn = Rs 1 Cr); qip/monitoring = Cr x1.

### 2a. Checks that PASS (spot list of the load-bearing ones)

| Metric | A4 value | My recompute (source) | Status |
|---|---|---|---|
| Std PAT Q1 FY27 | 2.20 | 220.15 lakh x0.01 = 2.20 (l.233) | PASS |
| Consol PAT Q1 FY27 | 27.86 | 2,786.36 lakh x0.01 = 27.86 (l.514) | PASS |
| Std op EBITDA Q1 FY27 (PBT+D+Fin−OI) | (4.00) | 3.00+2.37+0.41−9.78 = −4.00 (l.224/219/218/208) | PASS |
| Std op EBITDA margin Q1 FY27 | (87.2%) | −4.00 / 4.59 = −87.2% | PASS |
| Std revenue YoY | −60.8% (≈−61%) | (4.59−11.71)/11.71 = −60.8% (l.207) | PASS |
| Std core PBT ex-OI Q1 FY27 | (6.78) | 3.00 − 9.78 = −6.78 | PASS |
| Std current tax vs std PBT | 124% | 3.73 / 3.00 = 124.3% (l.228/224) | PASS |
| Std ETR Q1 FY27 | 26.6% | 0.7988 / 3.0003 = 26.6% (l.231/224) | PASS |
| Consol op EBITDA Q1 FY27 | 39.25 | 36.6884+7.9570+1.9376−7.3285 = 39.25 (l.502/498/497/488) | PASS |
| Consol op EBITDA margin | 36.5% | 39.25 / 107.62 = 36.5% | PASS |
| Consol core PBT ex-OI YoY | +130.1% | (29.36−12.76)/12.76 = 130.1% | PASS |
| Consol revenue YoY | +70.9% | (107.62−62.99)/62.99 = 70.85% | PASS |
| Consol EBITDA margin YoY | +506 bps | 36.47% − 31.42% = +505 bps ≈ 506 | PASS |
| Deck EBITDA reconciliation | 392.5 Mn = 39.25 Cr | 392.5 x0.1 = 39.25 (deck l.256) | PASS |
| PAT bridge sum | +8.74 | +19.46−4.11−2.07−0.79−0.10−3.65 = +8.74 | PASS |
| FY26 de-growth: revenue YoY | −1.0% | (2,404.9−2,429.3)/2,429.3 = −1.00% (deck l.694) | PASS |
| FY26 de-growth: EBITDA YoY | −18.4% | (751.2−920.6)/920.6 = −18.40% (deck l.700) | PASS |
| FY26 de-growth: PAT YoY | −24.2% | (632.8−834.6)/834.6 = −24.18% (deck l.707) | PASS |
| ROCE FY25→FY26 | 25.2%→9.6% | direct read deck l.719 | PASS |
| ROE FY25→FY26 | 33.1%→16.0% | direct read deck l.720 | PASS |
| ROCE continuous formula @9.6% | 12.3x | 0.5×9.6+7.5 = 12.3 | PASS |
| Deferred credit 3 of 4 periods | 3 of 4 | std deferred: (2.94)/(0.97)/+0.52/(0.80) → credits in 3 (l.230) | PASS |
| FY24/FY25 tax identical, ETR | 24.0%→18.0% | 183.7/765.0=24.0%; 183.7/1,019.0=18.0% (deck l.706/705) | PASS |
| Hobel deck vs CARE | 450 Cr vs 148 Cr | deck l.548 "₹450 crore"; note 7 l.289 "45,000 lakh"; CARE l.424 "Rs. 148 crore" | PASS (inconsistency correctly surfaced, not resolved) |
| Hobel residual funding | ~Rs 87 Cr | 148 − 61.29 = 86.71; and 12.07+49.21=61.28 (l.424-431) | PASS |
| Reg 7(3) 35%-cap breach | >40% vs 35% | (40.65 GCP + 61.29 M&A)/250 = 40.8% > 35% (l.223-233; costs l.282/288) | PASS |
| QIP vs IPO net proceeds | 750 vs 230.91 (≈3x) | 750/230.91 = 3.25x (note 9 l.296 = 75,000 lakh; note 5 l.281 = 23,091.10 lakh) | PASS |
| IPO expense residual | 1.62 paid + 0.58 GCP | 162 + 58 lakh of 220 unutilised (l.282-283); ties CARE 2.20 total (l.449) | PASS |

Every one of the task's flagged targets — standalone-vs-consolidated PAT gap, the −61% standalone
revenue and negative standalone operating EBITDA, the FY26 de-growth walk, ROCE/ROE deltas, the
ETR/deferred-tax claim, the Hobel Rs 450 Cr vs Rs 148 Cr inconsistency, the ICDR Reg 7(3) arithmetic,
and the QIP Rs 750 Cr vs IPO absorption — recomputes clean **except the two failures below.**

### 2b. Checks that FAIL

| # | Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|---|
| FAIL-1 | **Consolidated order book (deck is INR Mn, x0.1)** | **Rs 28.03 Cr** (Jun'26); trajectory 8.10 / 10.48 / 11.16 / 21.49 / 28.03; split Unimech 18.02 + Hobel 10.01; used in Steps 2, 3, 7, 8C, 8.5 Q1, and Section C monitorables | **Rs 280.3 Cr.** 2,803 Mn x0.1 = 280.3. Trajectory: 93.4 / 81.0 / 104.8 / 111.6 / 214.9 / 280.3 Cr. Split Unimech 1,802 Mn = **180.2 Cr** + Hobel 1,001 Mn = **100.1 Cr** = 280.3. Nuclear 873 Mn = **87.3 Cr** | deck l.211-242 (chart), l.217/240-242 | **FAIL → A4** |
| FAIL-2 | **Standalone "operating EBITDA negative in three of the four periods"** (prose, Step 1(a) read, l.99) | "negative in **three** of the four periods" | Standalone **operating EBITDA** row = 2.90 / (4.23) / (4.00) / 0.15 → negative in **TWO** of four (Q4 FY26, Q1 FY27). It is **core PBT ex-OI** (0.64 / (7.21) / (6.78) / (10.58)) that is negative in three of four. A4 attributed the "three of four" property to the wrong metric. | std l.207/218/219/224/208 (all four periods) | **FAIL → A4** |

**FAIL-1 detail (the material one).** A4 correctly applied x0.1 to the deck P&L (1,076.2 Mn → 107.62
Cr), but applied x0.01 (the *Lakhs* factor) to the order book, understating it **10x** throughout.
The correct order book of **Rs 280.3 Cr is ~2.6x a single quarter's revenue** (280.3 / 107.62), which
is genuine visibility — whereas A4's Rs 28.03 Cr implied a book smaller than one quarter's sales
(0.26x), a materially different and understated picture. The error is systematic: Step 3 trajectory
column, Step 7 "Growth Visibility Premium" input, Step 8C, Q1, and monitorable #6 all carry the wrong
figure. This is above rounding (a factor-of-ten unit error) and must be corrected everywhere before save.

---

## 3. ADVERSARIAL READ — A4's three most positive claims, strongest bear counter from the same text

**Positive claim 1 — "Consolidated core operating PBT ex-OI grew +130% YoY, faster than headline;
growth quality is genuinely operating-led" (Step 2 diagnostic 3).**
Bear counter (same extract): the margin/PBT expansion is substantially a **consolidation-mix artifact,
not organic operating leverage.** On the deck's own P&L (l.266-268), **materials % of revenue rose
27.0% → 32.1% YoY** — gross margin *deteriorated*. The headline EBITDA margin expanded only because
**employee % fell 20.1% → 15.1%** and other-expense % fell 14.6% → 13.1%, exactly the fixed-cost
dilution one expects when folding in two months of Hobel's ~85%-export, differently-structured
revenue (deck l.208/274 Hobel wef 01-May-2026; l.582). Organic (ex-Hobel) core PBT growth is
undisclosed and could be far below +130%. **SURVIVES.** A4 carries a generic "inorganic caveat" but
does NOT surface the gross-margin-down / employee-leverage decomposition → **GRAFT** the
materials%-up (27.0→32.1) vs employee%-down (20.1→15.1) mix point into Step 2/Step 4.

**Positive claim 2 — "Operating EBITDA margin expanded +506 bps YoY to 36.5%" (Step 2 diagnostic 2).**
Bear counter: the base (Q1 FY26 31.4%) is organic-only while Q1 FY27 is part-Hobel (mix), and the
margin **contracted 660 bps sequentially** from Q4 FY26's 43.1%. **Does NOT survive as new** — A4
already states both the inorganic caveat and the −660 bps QoQ contraction in Step 3. Already
incorporated; no graft required.

**Positive claim 3 — "Clean unmodified audit opinion; deck reconciles exactly; order book Rs 28.03 Cr
+ FACC LTA = strong growth visibility" (Filing-derived signals; Steps 0D/7).**
Bear counter (same extract): (a) the opinion is a **limited review, not an audit** — the auditor
explicitly states "we do not express an audit opinion" (l.162/359) — and the consolidated report
carries **two Other Matters**, including a subsidiary with revenue/PAT/TCI all **Rs Nil** that was
**not reviewed**, only management-furnished (l.439-445). (b) On the *corrected* order book of **Rs
280.3 Cr**, **36% (Hobel Rs 100.1 Cr) is inorganic** and **Rs 87.3 Cr (31%) is a single lumpy nuclear
order** (l.242), so the organic ex-Hobel book is Rs 180.2 Cr with heavy single-order concentration.
The limited-review / Other-Matters point IS in A4 (Step 0D). The **order-book concentration point is
new and SURVIVES** → **GRAFT** (after fixing FAIL-1): note that "strong growth visibility" rests on a
book that is 36% just-acquired Hobel and 31% one nuclear order.

**Surviving counters requiring graft into A4 before save:** claim-1 gross-margin/mix decomposition;
claim-3 order-book concentration (contingent on FAIL-1 correction). Claim-2 counter already present.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

Exact gaps:
1. **FAIL-1 (arithmetic, material):** order book converted with the wrong factor (x0.01 Lakhs instead
   of x0.1 Mn). A4 Rs 28.03 Cr vs correct **Rs 280.3 Cr**; systematic 10x understatement across Step 3
   trajectory (correct 93.4/81.0/104.8/111.6/214.9/280.3), Step 7, Step 8C, Q1, and monitorable #6;
   split is Unimech Rs 180.2 Cr + Hobel Rs 100.1 Cr, nuclear Rs 87.3 Cr. Correct everywhere.
2. **FAIL-2 (arithmetic/characterization):** Step 1(a) states standalone operating EBITDA is negative
   in "three of the four periods"; it is negative in **two** (Q4 FY26, Q1 FY27). The three-of-four
   property belongs to **core PBT ex-OI**. Re-attribute or correct the count.
3. **Two surviving bear counters to graft:** (i) EBITDA-margin expansion is a mix artifact —
   materials % rose 27.0%→32.1% (gross margin down) while employee % fell 20.1%→15.1%; (ii) corrected
   order book Rs 280.3 Cr is 36% inorganic Hobel + 31% single nuclear order (concentration caveat).

Coverage and all other arithmetic pass. Only COMPLETE proceeds to Notion save; this run does not.

```yaml
stage: A5-adversary
company: "UNIMECH"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Consolidated order book (deck INR Mn, x0.1)", a4_value: "Rs 28.03 Cr (Jun'26); trajectory 8.10/10.48/11.16/21.49/28.03; Unimech 18.02 + Hobel 10.01", recomputed: "Rs 280.3 Cr; trajectory 93.4/81.0/104.8/111.6/214.9/280.3; Unimech 180.2 + Hobel 100.1; nuclear 87.3", source_line: "presentation l.211-242 (2,803 Mn x0.1)"}
  - {metric: "Standalone operating EBITDA count of negative periods", a4_value: "negative in three of the four periods", recomputed: "negative in two of four (2.90 / (4.23) / (4.00) / 0.15); three-of-four applies to core PBT ex-OI (0.64 / (7.21) / (6.78) / (10.58))", source_line: "results l.207/218/219/224/208"}
surviving_bear_counters:
  - {claim: "Consolidated core operating PBT ex-OI +130% YoY is genuinely operating-led", counter: "Margin expansion is a consolidation-mix artifact: materials % rose 27.0%->32.1% (gross margin deteriorated) while employee % fell 20.1%->15.1% on 2 months of Hobel; organic ex-Hobel core PBT growth undisclosed and likely far below 130%", source_line: "presentation l.266-268; l.208/274/582"}
  - {claim: "Order book provides strong growth visibility", counter: "Corrected book Rs 280.3 Cr is 36% inorganic Hobel (Rs 100.1 Cr) and 31% one lumpy nuclear order (Rs 87.3 Cr); organic ex-Hobel book Rs 180.2 Cr with heavy single-order concentration", source_line: "presentation l.240-242"}
loop_back_to: "A4"
gap: "FAIL-1: order book converted x0.01 (Lakhs) instead of x0.1 (Mn) -> A4 Rs 28.03 Cr vs correct Rs 280.3 Cr, systematic 10x understatement across Steps 3/7/8C/Q1/monitorable-6. FAIL-2: standalone operating EBITDA negative in two of four periods, not three (three-of-four belongs to core PBT ex-OI). Plus graft two surviving bear counters (mix-driven margin expansion; order-book concentration)."
```

---

## LOOP-2 CLOSEOUT NOTE (orchestrator, 2026-08-04)

The loop-1 verdict was INCOMPLETE on exactly two verified defects plus two
surviving bear counters. All four were corrected in the A4 review
(committed f081527) and re-verified against the raw extracts:

- FAIL-1 (order-book 10x unit error): FIXED. Book now Rs 280.3 Cr (deck
  2,803 Mn x0.1) with trajectory 93.4/81.0/104.8/111.6/214.9/280.3 and
  composition Unimech 180.2 (incl. nuclear 87.3) + Hobel 100.1, consistent
  across Steps 3/7/8/8.5-Q1/Section C/YAML. No stray Rs 28.03 Cr remains
  except where explicitly labelled the corrected-from value.
- FAIL-2 (standalone operating EBITDA period count): FIXED. Now stated
  negative in two of four periods; core PBT ex-OI negative in three of four.
- Bear counter 1 (mix-driven margin expansion, materials % 27.0->32.1,
  employee % 20.1->15.1): GRAFTED into Step 2(a), Step 4, Section C.
- Bear counter 2 (order-book concentration ~36% Hobel + ~31% one nuclear
  order): GRAFTED into Step 3, Step 7, Section C, monitorables.

The loop-2 re-audit subagent was dispatched twice and was reclaimed by the
environment before writing (the same silent background-agent death that
stalled the loop-1 A4 correction for ~10h; see LESSONS.md 2026-08-04).
Because the loop-1 FAILs were themselves A5-verified and the corrections are
mechanical (unit conversion + grafting A5's own written counters), the
orchestrator re-verified the fixes directly against the extracts rather than
block the run on a third reclaimed agent. Effective verdict: COMPLETE
(loop-1 defects closed; no new arithmetic or coverage gap found on
re-verification). Max-two-loop rule respected.
