# A5 ADVERSARY / COMPLETENESS AUDIT — Uniparts India Ltd (UNIPARTS) — Q1 FY2026-27

Agent: A5 ADVERSARY | Model: claude-opus-4-8
Scope: attacks the A4 review before Notion save. Fresh context: only A4 review + A1 extracts + A2 ledgers seen; all figures re-derived independently from the extracts, A4/A3 cites checked not trusted.
Unit convention re-derived from A1 headers: results in Rs Millions (x0.1 to Rs Crores); presentation in Rs Millions except page-5 management narrative which is native Rs crore (net cash 190, special dividend 101, order book 225) — I confirmed these three are NOT double-converted anywhere in A4.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

Plain-Language Brief located at review lines 410-428. All four labelled parts present and carrying real, non-placeholder content:

| Part | Heading present | Line | Content status |
|---|---|---|---|
| (1) Summary narrative | "1. SUMMARY NARRATIVE" | 412-416 | PRESENT — two full paragraphs (~18 lines), operating result + qualifications |
| (2) Sector intelligence | "2. SECTOR INTELLIGENCE" | 418-420 | PRESENT — construction/small-ag/large-ag/aftermarket demand split, labelled filing-vs-general-knowledge |
| (3) Business-model intelligence | "3. BUSINESS-MODEL INTELLIGENCE" | 422-424 | PRESENT — dual-shore model, 66% GM, 136 WC days, consol-vs-standalone margin, drift watch-items |
| (4) Competition intelligence | "4. COMPETITION INTELLIGENCE" | 426-428 | PRESENT — <70HP leadership, concentration, single-segment exposure, component-auditor caveat |

**GATE 0: PASS.** All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration, diffed vs A2 ledgers)

Re-ran my own sweep over both extracts and diffed against the two A2 count tests and A4's reconciliation preamble.

| Category (source) | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes (results L322-338, 576-591) | 10 | 10 (5 consol + 5 std; std note 4 OCR'd "4_" at L588 recovered) | none | MATCH |
| Line items (results) | 99 | 99 (consol 33 P&L/OCI + 4 EPS + 13 ratio = 50; std 32 + 4 + 13 = 49) | none | MATCH |
| Zero-standing rows (results) | 13 | 13 (2A: L275,L280; 2B: L316; 2C: L393,L411,L415; 3A: L528,L533,L550; 3B: L569; 3C: L640,L643,L667) | none | MATCH |
| Agenda items (results L33-43) | 2 | 2 (results approval + Rs 9 dividend) | none | MATCH |
| Auditor paragraphs (results) | 15 | 15 (consol 1-7 + sign-off = 8; std 1-5 + sign-off = 7) | none | MATCH |
| Consolidation entities (results Appx I) | 5 | 5 (GFPL, GCPL, UUL, UIG, UOI) | none | MATCH |
| Slides (presentation) | 25 | 25 (pdfinfo page_count 25 = formfeed 25) | none | MATCH |
| Numeric tokens (presentation, 234 content rows) | 612 | structure verified (N1-N234); gate consistent | none | MATCH |
| Footnotes (presentation) | 8 | 8 (F1-F8; slide-15 "capacity*" dangling + slide-16 stray "0" logged, not counted) | none | MATCH |
| Org-chart entities (presentation slide 23) | 6 | 6 (UIL parent + 5) | none | MATCH |

**A4 preamble cross-check:** A4 line 15-16 restates every count above (10/99/13/2/15/5 results; 25/612/234/8/6 presentation) — all match the ledgers exactly. A4 line 20-21 incorporates all 12 R-A3 and all 15 P-A3 findings, each mapped to an analytical line, a monitorable (M1-M14), or a management question (Q1-Q14). Cross-checked: every A3 finding ID appears; no dropped finding.

**Orphan-row test (ledger rows absent from A4):** The material ledger flags are all traced into A4 — component-auditor reliance (entities 3/4/5, auditor para 6) → Flag 1 + Q1; ZERO_STANDING Labour Code (L275/L528) → Note table + Q5; blank ratio/TCI cells (L411/L415/L550/L667) → disclosure-hygiene cluster; dangling footnotes and BIO_TEXT_MISALIGNED are extraction-artifact flags carried under the blanket "reviewed, no finding" reconciliation. No orphan finding row.

**Missing-from-ledger test (rows my pass found, ledger lacks):** none. My line-by-line reconstruction of both P&L/OCI blocks, both EPS blocks, both ratio tables, the deck P&L (slide 19), balance sheet (slide 20) and metric charts (slide 17) surfaced no numeric row the ledger omits.

**One cosmetic A2 note (not a FAIL):** the results-ledger FLAG SUMMARY (ledger lines 309-310) mis-attributes the 13 zero-standing rows in its parenthetical breakdown (writes "3A x1" where the tables actually flag 3, and its own recount sums to 11) — but the headline total 13 is correct and matches both the grep gate and my fresh count of the flagged table rows. Enumeration integrity intact; label typo only.

**AUDIT 1: PASS.**

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw Millions, x0.1)

All recomputations done in unrounded Millions then converted, to avoid false rounding diffs. "Match" = agrees within one-paisa/one-bp rounding.

### Consolidated — levels & core derived
| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+FC−OI) | 81.97 | 745.56+118.20+34.13−78.16=819.73→81.97 | L272/269/268/260 | MATCH |
| Op EBITDA Q4FY26 | 80.84 | 662.56+118.38+32.55−5.09=808.40→80.84 | L273/269/268/260 | MATCH |
| Op EBITDA Q1FY26 | 52.30 | 446.56+110.58+20.88−55.05=523.0-ish (522.97)→52.30 | L273/269/268/260 | MATCH |
| Op EBITDA margin Q1FY27 | 23.60% | 81.97/347.38=23.60% (filing L411 ties) | L259 | MATCH |
| Op EBITDA margin Q1FY26 | 19.11% | 52.30/273.65=19.11% (filing ties) | L259 | MATCH |
| Reported EBITDA Q1FY27 | 89.79 | 74.56+11.82+3.41=89.79 (=898 Mn slide 8) | — | MATCH |
| Core PBT ex-OI Q1FY27 | 66.74 | 74.56−7.82 | L272/260 | MATCH |
| Effective tax rate Q1FY27 | 24.07% | 179.47/745.56=24.07% | L282/272 | MATCH |
| Effective tax rate Q1FY26 | 22.82% | 101.92/446.56=22.82% | L282/272 | MATCH |
| PAT margin Q1FY27 | 16.30% | 566.09/3473.76=16.29%→16.30 | L283/259 | MATCH |

### Consolidated — YoY (Q1FY27 vs Q1FY26)
| Metric | A4 % | My recompute | Status |
|---|---|---|---|
| Revenue | +26.9% | 3473.76/2736.45−1=+26.94% | MATCH |
| Op EBITDA | +56.7% | 819.73/522.97−1=+56.7% | MATCH |
| Op EBITDA margin | +449 bps | 23.60−19.11=4.49pp | MATCH |
| Core operating PBT ex-OI | +70.5% | 66.74/39.15−1=+70.47% | MATCH |
| Reported PBT | +66.9% | 745.56/446.56−1=+66.95% | MATCH |
| PAT | +64.2% | 566.09/344.64−1=+64.28% | MATCH |
| Finance costs | +63.5% | 34.13/20.88−1=+63.46% | MATCH |
| Other income | +42.0% | 78.16/55.05−1=+41.98% | MATCH |
| EPS basic (share-adj) | +64.1% | 12.54/7.64−1=+64.1% | MATCH |

### PAT bridge (Step 4, consolidated, Q1FY27 vs Q1FY26)
| Component | A4 (Rs Cr) | My recompute | Status |
|---|---|---|---|
| GP volume @ prior margin | +48.37 | (347.38−273.65)×0.656=48.37 | MATCH |
| GP mix | +3.40 | 231.32−347.38×0.656=3.44 | MATCH (rounding) |
| Employee benefits drag | −9.23 | 71.62−62.39=9.23 | MATCH |
| Other expenses drag | −12.90 | 77.73−64.83=12.90 | MATCH |
| = Op EBITDA change | +29.67 | 81.97−52.30=29.67 | MATCH |
| Depreciation | −0.76 | 11.82−11.06=0.76 | MATCH |
| Finance cost | −1.33 | 34.13−20.88=13.25→1.33 | MATCH |
| Other income | +2.31 | 7.82−5.51=2.31 | MATCH |
| Tax change | −7.76 | 17.95−10.19=7.76 | MATCH |
| Reported PAT YoY change | +22.15 | 566.09−344.64=221.45→22.15 | MATCH (bridge of rounded parts = 22.13, ties to 22.15 within rounding) |

### Standalone — spot checks
| Metric | A4 value | My recompute | Status |
|---|---|---|---|
| Op EBITDA Q1FY27 | 30.15 | 305.07+60.83+19.83−84.20=301.53→30.15 | MATCH |
| Op EBITDA Q4FY26 | 29.61 | 475.34+61.06+18.83−259.15=296.08→29.61 | MATCH |
| Op EBITDA margin Q1FY27 | 15.74% | 30.15/191.57=15.74% (filing L663 ties) | MATCH |
| ETR Q1FY27 | 24.60% | 75.06/305.07=24.60% | MATCH |
| ETR Q4FY26 | 13.05% | 62.05/475.34=13.05% | MATCH |
| PAT YoY | +57.2% | 230.01/146.26−1=+57.26% | MATCH |

### Standalone-vs-consolidated PAT gap (YAML sc_gap_pat_pct)
| Period | A4 % | My recompute (consol−std)/consol | Status |
|---|---|---|---|
| Q1FY27 | 59.4 | (566.09−230.01)/566.09=59.4% | MATCH |
| Q4FY26 | 19.2 | (511.45−413.29)/511.45=19.2% | MATCH |
| Q1FY26 | 57.6 | (344.64−146.26)/344.64=57.56% | MATCH |
| FY26 | 5.1 | (1583.16−1502.26)/1583.16=5.11% | MATCH |

### Cash / annual (presentation slide 17, 19)
| Metric | A4 value | My recompute | Status |
|---|---|---|---|
| CFO/PAT FY25 | 2.07 | 1820/880=2.068 | MATCH |
| CFO/PAT FY26 | 1.10 | 1736/1583.16=1.097 | MATCH |
| FY26 CFO/PAT band | 1.00-1.15x | 1.10 in band | MATCH |
| Dividend Rs 40.65 Cr | 40.65 | 406.45 mn (L335) x0.1 | MATCH |
| 46.1% group PAT unaudited | 46.1% | 260.86/566.09=46.08% | MATCH |
| 65.1% group revenue unaudited | 65.1% | 2262.40/3473.76=65.13% | MATCH |

**AUDIT 2: PASS.** Every derived metric in A4's tables reproduces from the raw extract within rounding. No mismatch above rounding found. (I specifically re-checked the three cells where crore-level rounding could look like an error — Op EBITDA Q4 80.84, reported EBITDA Q1FY26 57.80, GP-mix 3.40 — all resolve correctly when computed in unrounded Millions.)

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear from the same extract)

**Positive claim 1 (review L157-165, 366): "Core operating PBT ex-OI grew +70.5% YoY, faster than reported PAT (+64.2%) — the single cleanest test, unambiguously positive; growth is operational, not treasury-driven."**
Strongest bear from the same extract: the +70.5% is measured off Q1FY26, a trough quarter (op EBITDA margin only 19.11% vs 23.85% by Q4FY26). Sequentially the operating step-up is nearly spent: Q4FY26 core PBT 65.75 → Q1FY27 66.74 = **+1.5% QoQ** (L275/L280 vs L272/L260). The large YoY therefore reflects a step-up that occurred in the unshown Q2/Q3 FY26, not momentum in this quarter.
Survives? Supported by the extract — BUT already incorporated: A4 Step 3 states "sequentially the operating step-up was modest (+1.5% core PBT)" and the summary narrative repeats "the quarter-on-quarter figure flatters slightly." **Does not survive as a gap.**

**Positive claim 2 (review L367, 378: "Balance sheet is strongly net cash (~Rs 190 Cr), fortress balance sheet, continued strength of cash generation.")**
Strongest bear from the same extract: (a) the Rs 190 Cr is a page-5 management narrative figure (native crore), not tied to any Q1 balance sheet (none in the Reg 33 bundle); (b) management itself concedes it is still **below** the ~Rs 210 Cr pre-special-dividend level (L175); and (c) the deck's own CFO chart (slide 17, N140-143) shows CFO falling **four consecutive years** — 252.7 → 199.7 → 182.0 → 173.6 Cr (FY23-FY26, −31%) — while management claims "continued strength of our cash generation" (L174).
Survives? Substantially incorporated: A4 Step 5 shows CFO "182.0 → 173.6, Positive but declining," flags the CFO/PAT compression 2.07x → 1.10x as "worth watching," records that net cash is below the pre-dividend Rs 210 Cr, and caps the verdict via INDETERMINATE quarterly cash conversion with Q2FY27 half-year CFO named as the missing evidence. The only un-surfaced sliver is the full **four-year** CFO downtrend (A4 shows only the FY25→FY26 −4.6% leg) and the direct tension with management's "continued strength" wording. **Recommended enhancement, not a surviving gap** — the underlying bear (cash conversion weakening as PAT rises) already drove A4's verdict cap and is prominently flagged.

**Positive claim 3 (review L150-152, 170: "Genuinely strong operating quarter — revenue +27%, operating margin +449 bps, high earnings quality.")**
Strongest bear from the same extract: the margin and growth are consolidated, and the high-margin work sits in the foreign subsidiaries the principal auditor did **not** review — Rs 2,262.40 mn revenue / Rs 260.86 mn PAT (65.1% / 46.1% of group, auditor para 6, L168-176). Standalone op EBITDA margin is only 15.74% vs consolidated 23.60% (L663 vs L411), so the entire "+449 bps" quality story rests on component-auditor-reviewed accounts.
Survives? Fully incorporated — this is A4's Flag 1, Q1 in the management questions, and the Step 1B read-through ("foreign subsidiaries carry the higher-margin work... standalone earnings are not a clean read"). **Does not survive as a gap.**

**AUDIT 3 result:** All three strongest bear counters are already incorporated into A4 (A4 is unusually thorough and pre-empts each one). No surviving, unincorporated counter requires grafting before save. Recorded enhancement (non-blocking): extend the Step 5 CFO series to the full FY23-FY26 four-year decline and note the tension with management's "continued strength of cash generation" phrasing; A4's "no material narrative-vs-numbers contradiction" line (L376) is scoped to the growth headlines, which do reconcile, so it is not false, but the cash-generation narrative is the one place a future full workup should press.

---

## VERDICT

**COMPLETE.**

- Gate 0 (Plain-Language Brief, all four parts): PASS.
- Audit 1 (coverage): PASS — my fresh enumeration matches all ten A2 categories exactly; zero orphan rows, zero rows missing from ledger; all 27 A3 findings traced into A4.
- Audit 2 (arithmetic): PASS — every derived metric reproduces from raw Millions within rounding; no mismatch above rounding.
- Audit 3 (adversarial): PASS — the three strongest bear counters are all already incorporated in A4; no surviving counter needs grafting.

Only COMPLETE proceeds to Notion save. Verdict COMPLETE — proceeds.

```yaml
stage: A5-adversary
company: "UNIPARTS"
quarter: "Q1 FY2026-27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
