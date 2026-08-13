# A5 ADVERSARY / COMPLETENESS AUDIT — Gem Aromatics Limited (GEMAROMA), Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-08-13
**Under audit:** review_gemaroma_q1fy27.md (A4, loop 1 of 2)
**Method:** fresh context — re-derived independently from the three A1 extracts and diffed against the three A2 ledgers; A4's and A3's cites were checked, not trusted. Results extract is in **Rs Millions, x0.1 → Rs Cr**; deck and press release already in Rs Cr.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

| Brief part | Location | Present / Empty | Note |
|---|---|---|---|
| (1) Summary narrative | L470-472 | **PRESENT** | ~22 lines, substantive; carries the two-problem split, INDETERMINATE cash, WATCHLIST call |
| (2) SECTOR intelligence | L474-476 | **PRESENT** | provenance-flagged (Frost & Sullivan company-commissioned), Madagascar clove RM, positioning shares |
| (3) BUSINESS-MODEL intelligence | L478-480 | **PRESENT** | feedstock→derivative model, FY26 mix, named customers, undisclosed-metric list |
| (4) COMPETITION intelligence | L482-484 | **PRESENT** | integration edge, small-cap scale weakness, input-cost non-control, thin institutional ownership (not a risk) |

**Gate 0 = PASS.** All four labelled parts present and non-placeholder.

---

## AUDIT 1 — COVERAGE (fresh grep re-enumeration vs A2 ledgers)

### Results ledger (Reg 33 filing)
| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| Notes (numbered + asterisk footnotes) | 17 | 17 (std 7+1, con 8+1) | none | PASS |
| Line items (std 29 + con 30) | 59 | 59 | none | PASS |
| Zero-standing rows | 1 | 1 (std "tax relating to prior years", L194) | none | PASS |
| Agenda items | 1 | 1 (results approval) | none | PASS |
| Auditor paragraphs (std 5 + con 6) | 11 | 11 | none | PASS |
| Consolidation entities | 2 | 2 (Gem Aromatics LLC, Krystal Ingredients) | none | PASS |
| Signature blocks | 5 | 5 | none | PASS |

### Presentation ledger (33-slide deck)
| Category | A2 count | My fresh count | Status |
|---|---|---|---|
| Slides / OCR pages | 33 / 7 | 33 / 7 | PASS |
| Financial-table line items | 88 | 88 (51 P&L + 24 BS + 13 CF) | PASS |
| Slide KPIs / charts / footnotes | 95 / 3 / 13 | 95 / 3 / 13 | PASS |
| Guidance / capex-capacity / strategic | 11 / 14 / 17 | 11 / 14 / 17 | PASS |

### Press-release ledger (Reg 30 release)
| Category | A2 count | My fresh count | Status |
|---|---|---|---|
| Pages/sections | 5 | 5 | PASS |
| Financial line items / narrative facts | 18 / 21 | 18 / 21 | PASS |
| MD quotes / forward stmts / regulatory / call-detail | 5 / 13 / 8 / 12 | 5 / 13 / 8 / 12 | PASS |

**Orphan-row test (ledger row present, A4 absent):** every materially-flagged ledger row is cited in A4 — FIFO/EoM (FIND-02), balancing figures (N5, Step 3), consol Notes 1-2 mis-headed "Standalone" (FIND-05), consol depreciation OCR line (A4 data-integrity flag/Q11), blank standalone partner name vs "Abhinav Chhajed" (FIND-05), 15% tax "till perpetuity" (A3-04/Q4), DATA_ABSENT capacity + order book (business-model brief), 9% vs 8.6% revenue reframe (A3-07), 199%-YoY framing (F16-1/Q10), three-vs-two facilities / Daman & Diu label (F14-2), Brazil WOS new entity (flag 10/Q9). Immaterial rows (Diamond Pass link with no URL; Rest-of-World footnote listing Uganda/Switzerland absent from the map; the zero-standing prior-year-tax template row; the 16.9% vs 17.0% Q1FY26 consol-EBITDA-margin deck rounding) are covered by A4's blanket "All reviewed. No ledger row is unreviewed" (L22) as reviewed-no-finding, and my recompute confirms each is immaterial (see Audit 2 on 16.9/17.0).

**Missing-from-ledger test (my fresh pass found, ledger lacks):** none. My enumeration reproduced every A2 count 1:1.

**Coverage verdict: PASS — no orphan rows, no missing rows.**

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw; Millions x0.1 applied)

All figures below recomputed from the raw extract lines. "✓" = ties within rounding.

### Standalone (source: results extract L167-218, x0.1)
| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Gross Profit Q1FY27 = Rev − (Mat+ΔInv) | 14.69 | 82.99 − (70.81 + (−2.51)) = 14.69 | L168/175/177 | ✓ |
| Gross Margin Q1FY27 | 17.7% | 14.69/82.99 = 17.70% | — | ✓ |
| Gross Margin Q1FY26 / YoY | 25.0% / −734 bps | 19.13/76.40 = 25.04%; Δ = −734 bps | L168/175/177 | ✓ |
| Operating EBITDA Q1FY27 = PBT+D+Fin−OI | 8.51 | 9.73+1.61+1.33−4.16 = 8.51 | L187/182/180/170 | ✓ |
| Operating EBITDA Q1FY26 | 10.51 | 8.729+1.439+2.928−2.582 = 10.51 | — | ✓ |
| Op EBITDA margin YoY | −350 bps | 10.25% − 13.76% = −351 bps | — | ✓ |
| Effective Tax Rate Q1FY27 | 25.5% | 2.48/9.73 = 25.49% | L196/187 | ✓ |
| Core PBT ex-OI Q1FY27 / YoY | 5.57 / −9.3% | 9.73−4.16 = 5.57; 5.574/6.147−1 = −9.3% | — | ✓ |
| Reported PBT / PAT YoY | +11.5% / +11.2% | 9.731/8.729−1 = +11.5%; 7.252/6.523−1 = +11.2% | — | ✓ |
| PAT bridge (GP −4.44 / opex +2.44 / D −0.17 / Fin +1.59 / OI +1.58 / tax −0.27 → PAT +0.73) | as stated | each leg reproduced; subtotal PBT +1.00, PAT +0.73 | — | ✓ |

### Consolidated (source: results extract L369-416, x0.1; depreciation reconciled — see below)
| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Gross Profit Q1FY27 | 16.51 | 98.85 − (99.04 + (−16.70)) = 16.51 | L370/376/377 | ✓ |
| Gross Margin Q1FY27 / YoY | 16.7% / −1,282 bps | 16.51/98.85 = 16.70%; vs 29.52% = −1,282 bps | — | ✓ |
| COGS-materials > revenue | 99.04 > 98.85 | 990.38 Mn vs 988.50 Mn — confirmed | L376/370 | ✓ |
| Operating EBITDA Q1FY27 (D=9.13) | 3.31 | −8.54+9.13+2.88−0.16 = 3.31 | L385/380*/379/371 | ✓ |
| Op EBITDA margin YoY | −1,361 bps | 3.35% − 16.96% = −1,361 bps | — | ✓ |
| Effective Tax Rate FY26 | 77.6% | 4.939/6.364 = 77.6% | L392/385 | ✓ |
| Reported PBT / PAT YoY | −179.2% / −198.6% | −19.33/10.79 = −179.2%; −15.85/7.98 = −198.6% | — | ✓ |
| PAT bridge (GP −9.36 / opex −2.18 / D −7.31 / Fin +0.64 / OI −1.11 → PBT −19.33; tax +3.47 → PAT −15.86) | as stated | each leg reproduced | — | ✓ |
| S→C PAT gap Q1FY27 / % of std | −15.13 / −208.6% | −7.874−7.252 = −15.13; /7.252 = −208.6% | L199/395 | ✓ |

**Depreciation reconciliation (A4 data-integrity flag) — independently verified.** The consol Q1FY27 depreciation line (L380) reads "5127" (Rs 5.13 Cr). My check: summing the six expense lines with D=5.127 gives Rs 103.55 Cr, but the printed Total Expenses is Rs 107.55 Cr (L382) — a gap of **exactly Rs 4.00 Cr**, which is 9.127 − 5.127. With D=**9.13 Cr (91.27 Mn)** the expense stack ties to 107.55 and PBT ties to −8.54. Third confirmation: the deck's own **Cash PAT of Rs 1.3 Cr** (L366) = PAT (−7.87) + D; this requires D = +9.13 (with 5.13, Cash PAT would be −2.7). A4's reconciliation to 9.13 is correct; the "5127" is an OCR "9"→"5" misread. PBT/PAT unaffected. **No arithmetic FAIL** — but this remains an A1-source correction item, correctly routed (Q11).

**Minor rounding notes (within tolerance, not FAILs):** (a) A4 L207 states standalone gross margin "down 570 bps QoQ"; precise is 17.70% − 23.35% = −565 bps (deck prints −566). ~4-5 bps, immaterial. (b) A4 uses consol Q1FY26 EBITDA margin 17.0% (table L348); raw = 14.86/87.63 = 16.96% → 17.0%; the deck's page-7 "16.9%" is its own rounding. A4 is correct.

**Arithmetic verdict: PASS — every derived metric ties within rounding; the depreciation reconciliation is well-founded on three independent cross-checks.**

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest bear counter each, same extract)

**Claim 1 (most bullish thread).** "The depreciation step-up (~Rs 9.1 Cr/qtr) is a genuine transitional fixed-cost-absorption story — the legitimate transition-alpha portion — which higher utilisation absorbs" (Step 4B Problem 2; Step 8).
- **Bear counter (same extract):** the only two quarters carrying full Dahej depreciation both go the wrong way. Q4FY26 carried Rs 9.0 Cr depreciation on Rs 110.41 Cr consol revenue and still made only Rs 1.0 Cr PAT; Q1FY27 revenue (98.85) is **below** Q4FY26 (110.41). Two data points, both with the fixed cost live, show revenue *falling*, not utilisation rising — the "utilisation will absorb it" thesis has zero corroborating evidence in the filing.
- **Survives?** **NO — already incorporated.** A4 Step 3 (L223) states verbatim the plant "commissioned but NOT lifted the run-rate above pre-commissioning levels… consolidated revenue Q1FY27 (98.85) is BELOW Q4FY26 (110.41)."

**Claim 2.** "Standalone revenue grew +8.6% and PAT +11%; the parent stayed profitable throughout" (Step 2A; Step 8).
- **Bear counter:** strip Other Income (+Rs 1.58 Cr) and finance-cost relief (+Rs 1.59 Cr) and standalone core PBT ex-OI **fell 9.3%**; the +Rs 1.00 Cr PBT gain is entirely treasury + deleveraging; if OI reverts to the prior Rs 2.58 Cr, standalone PBT is ~Rs 8.15 Cr, below last year.
- **Survives?** **NO — already incorporated.** Fully built into Step 2A diagnostics 4-6, Step 4A, and Q12.

**Claim 3.** "Unit economics historically were sound and, importantly, STABLE at the gross line — group gross margin held 24.6-25.3% across FY23-FY26 — so the Q1FY27 drop to 16.7% is a fresh break, not a long decline" (Step 3 L219; Business-Model brief L480).
- **Bear counter (same extract, deck p27 L922-938):** the gross-margin *ratio* held, but the business under it had **already broken a full year before Q1FY27**: consolidated revenue fell from Rs 504.0 Cr (FY25) to Rs 366.5 Cr (FY26), **−27.3%**; EBITDA Rs 88.5 → 40.8 Cr (−54%); PAT Rs 53.4 → 1.4 Cr (−97%). A "stable gross margin" sitting on a top line that contracted 27% is not a healthy base, and the FY26 revenue fall **cannot be explained by the Dahej depreciation** to which A4's brief attributes the FY26 break (depreciation sits below both the revenue and EBITDA lines). Q1FY27's gross-margin collapse therefore compounds an already-shrinking business rather than interrupting a stable one. Supporting: FY26 consolidated revenue (366.47) is itself **below standalone** revenue (370.94) — the subsidiary layer was net-negative to consolidated top line in FY26 while net-positive in Q1FY27, a swing A4 does not diagnose.
- **Survives?** **YES.** A4 lists the FY26 annual figures (L219) but never diagnoses the −27% FY26 revenue contraction, and the Business-Model brief (L480) attributes the FY26 break solely to Dahej depreciation — leaving the top-line collapse unaddressed and the "sound / stable base" framing un-qualified. **Must be grafted into A4.**

**Surviving bear counters: 1.** → loop back to A4.

---

## VERDICT

**INCOMPLETE.** Gates 0 (deliverable), 1 (coverage) and 2 (arithmetic) all PASS — the brief is complete, my fresh enumeration reproduces every A2 count with no orphan or missing rows, and every derived metric (including the 9.13 depreciation reconciliation) ties within rounding. Audit 3 surfaces **one surviving bear counter** that is not yet in the review.

- **Failing agent:** **A4.**
- **Exact gap:** graft the surviving counter to the "historically sound / stable gross margin = fresh break" framing (Step 3 L219; Business-Model brief L480): the FY26 consolidated top line already contracted **−27.3% (Rs 504.0 → 366.5 Cr)** with EBITDA −54% and PAT −97%, so Q1FY27 compounds an already-broken base rather than interrupting a stable one, and the FY26 break is **not** attributable to Dahej depreciation alone. Add the supporting fact that FY26 consolidated revenue (366.47) sits **below** standalone (370.94), inverting the Q1FY27 relationship, and carry the point into the flags/Questions-for-Management. Re-emit for A5 loop 2.

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
  - claim: "Historically sound / STABLE gross margin (24.6-25.3% FY23-FY26) so Q1FY27 drop to 16.7% is a fresh break, not a long decline (Step 3 L219; Business-Model brief L480)"
    counter: "The gross-margin ratio held, but the business under it already broke in FY26: consolidated revenue -27.3% (Rs 504.0 -> 366.5 Cr), EBITDA -54% (88.5 -> 40.8), PAT -97% (53.4 -> 1.4). The FY26 revenue collapse is not explained by Dahej depreciation (below the revenue and EBITDA lines), so Q1FY27 compounds an already-shrinking base rather than interrupting a stable one. Supporting: FY26 consol revenue 366.47 < standalone 370.94, inverting the Q1FY27 relationship - undiagnosed."
    source_line: "deck p27 L922 / L925-938 (extract_presentation); results L370/L168"
loop_back_to: "A4"
gap: "A4 states the FY26 annual figures but never diagnoses the -27.3% FY26 consolidated revenue contraction; the Business-Model brief attributes the FY26 break solely to Dahej depreciation, leaving the 'sound/stable base = fresh break' framing un-qualified. Graft the surviving bear counter (FY26 -27% revenue / -54% EBITDA / -97% PAT, plus the FY26 consol<standalone revenue inversion) into Step 3, the flags, and the Questions-for-Management table, then re-emit for A5 loop 2."
```
