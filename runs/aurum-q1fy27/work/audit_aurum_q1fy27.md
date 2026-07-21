# A5 ADVERSARY / COMPLETENESS AUDIT — Aurum PropTech, Q1 FY27 (presentation)

Agent: A5 ADVERSARY (Opus 4.8) | Run: aurum-q1fy27 | Audit date: 2026-07-21
Artifacts audited: review_aurum_q1fy27.md (A4) against extract_presentation_aurum_q1fy27.txt (A1) and ledger_presentation_aurum_q1fy27.md (A2).
Independence note: I re-derived every count and metric from the A1 extract with my own grep/sweep pass. I did not defer to A4's or A3's cites. Filing-sourced numbers (companion Reg-33, reviewed 2026-07-20) are outside this extract by design and are audited only for correct quarantine, not for value.

---

## AUDIT 1 — COVERAGE (fresh grep pass vs A2 ledger, then ledger vs A4)

Fresh enumeration method: `^\[page ` returns 41 lines = 34 true page headers + 7 `[page N text-layer residual]` lines for the 7 OCR pages; `OCR page` returns exactly 7 (pages 3,10,14,18,23,25,27) matching the A1 header. All sub-counts re-swept by hand against the cited line spans.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 34 | 34 | none | PASS |
| OCR slides | 7 | 7 (l.62,307,436,567,725,766,816) | none | PASS |
| Footnotes / source lines | 8 | 8 (l.55,128,167,205,370,405,491,811) | none | PASS |
| P&L build-up rows (slide 26) | 17 | 17 (l.785-809) | none | PASS |
| Board directors | 8 | 8 (slides 30-31, 4+4) | none | PASS |
| Leadership bios | 12 | 12 (slides 32-33, 6+6) | none | PASS |
| Digital signature blocks | 1 | 1 (l.44-52) | none | PASS |

Ledger-row-vs-A4 accountability: every A2 slide carrying a flagged finding is engaged in A4 — slide 4 RECONCILE_CHECK → C5/C6; slide 5 RECONCILE_CHECK + ₹6.24 Cr footnote → C4/C6; slide 6 KPIs → C9/Step 2 (but see Audit 3); slide 9 MATERIAL_TRANSACTION/RPT_WATCH → C8, QfM 2 and 6; slide 26 CORE_FINANCIAL_TABLE/ZERO_STANDING → Step 1/Table 1A; slide 33 DUAL_LISTING → C9; DATA_GAP_PRIOR_LEDGER → flagged in C4/flags. The pure-marketing / section-divider slides (10-25 opportunity decks, 28-32 fundamentals/board/leadership) carry no monitored metric and are covered by A4's blanket "all 34 reviewed" (l.11-14) consistent with the doctype adaptation. No orphan slide-row; my fresh pass surfaced no enumerable category the ledger lacks.

**Coverage verdict: PASS.** No orphan rows (A3 clean); nothing missing from the ledger (A2 clean).

---

## AUDIT 2 — ARITHMETIC (recompute every derived metric from raw extract lines)

All deck figures re-read at their cited lines (l.785-809). All ties confirmed.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| EBITDA margin Q1FY27 | 31.9% | 38.56/120.79 = 31.92% | l.797/795 | PASS |
| PBT margin Q1FY27 | 1.9% | 2.35/120.79 = 1.95% | l.809/795 | PASS |
| Adj EBITDA margin Q1FY27 | 10.2% | 12.07/117.80 = 10.25% | l.804/792 | PASS |
| Adj EBITDA build (fwd) | 12.07 | 38.56+0.81−2.99−24.31 = 12.07 | l.797,800,801,803 | PASS |
| PBT build (fwd) | 2.35 (≈2.34) | 12.07−0.81−1.06−6.39−1.47 = 2.34 | l.804-808 | PASS (rounding) |
| Q1FY26 EBITDAr tie | −2.23 | 21.87+1.22−3.71−21.61 = −2.23 | l.797,800,801,803 | PASS |
| Q1FY26 PBT tie | −10.78 | −2.23−1.22−1.66−5.67 = −10.78 | l.804-807 | PASS |
| Total Income tie Q1FY27 | 120.79 | 117.80+2.99 = 120.79 | l.792/793 | PASS |
| Total Income YoY | +56.9% | (120.79−76.96)/76.96 = +56.95% | l.795 | PASS (deck "57%") |
| Adjusted Income YoY | +60.8% | (117.80−73.26)/73.26 = +60.80% | l.792 | PASS |
| EBITDA YoY | +76.3% | (38.56−21.87)/21.87 = +76.31% | l.797 | PASS |
| Adj EBITDA swing | +14.30 | 12.07−(−2.23) = 14.30 | l.804 | PASS |
| Adj EBITDA bps | +1320 | 10.2−(−3.0) = 13.2pp | l.787 | PASS |
| Finance costs YoY | −36.1% | (1.06−1.66)/1.66 = −36.14% | l.806 | PASS |
| Depreciation YoY | +12.7% | (6.39−5.67)/5.67 = +12.70% | l.807 | PASS |
| PBT swing | +13.13 | 2.35−(−10.78) = 13.13 | l.809 | PASS |
| PBT margin bps | +1590 | 1.9−(−14.0) = 15.9pp | l.785 | PASS |
| PAT bridge: PBT-after-assoc | +1.30 | 2.35−1.01 = 1.34 (filing states 1.30) | filing | PASS (assoc/rounding, filing-anchored) |
| PAT bridge: tax balancer | −1.64 | 1.30−(−0.34) = 1.64 | filing (derived) | PASS (internally consistent) |
| PAT bridge: reported PAT | +45.18 | −0.34+45.52 = 45.18 | filing | PASS (internally consistent) |
| Q-of-E gap (Step 5.5) | ~45.52 | 45.18−(−0.34) = 45.52 | filing | PASS (internally consistent) |

**Arithmetic verdict: PASS.** No mismatch above rounding on any deck-derived metric. The filing-derived rows (Table 1B, PAT bridge, Step 5.5) cannot be re-verified from this extract — grep confirms `Navi Mumbai`, `52.35`, `receivable`, `MSKA`, `discontinued` are all ABSENT from the deck — but A4 correctly quarantines them as companion-filing anchors (ND-by-doctype), attributes none of them to the deck, and they are internally arithmetically consistent. Correct doctype adaptation, not a fail.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims, strongest bear from the same extract)

**Positive claim 1 — "Revenue grew +56.9% Total Income / +71% continuing" (Step 2 diagnostic 1, l.108/795).**
Bear from extract: growth is inorganic — full-quarter PropTiger consolidation vs zero PropTiger in the base; organic ex-PropTiger withheld. **Already grafted** (A3-13, diagnostic 1, C5, QfM 7). Does NOT survive as new.

**Positive claim 2 — "EBITDA expanded +76.3%, margin 28.4%→31.9%; Adjusted-EBITDA margin +1320 bps to 10.2%" (Step 2, l.797/804).**
Bear from extract: EBITDA folds in Rs.2.99 Cr RoU other income (l.793/801) and is struck before Rs.24.31 Cr of long-term lease payments (l.803), a real recurring cash cost; the "adjusted" margin adds those back. **Already grafted** (A3-12, C3, diagnostic 2, QfM 3). Does NOT survive as new.

**Positive claim 3 — Rental item graded GREEN: "Rental segment breakeven … GREEN on filing basis" and the deck's own "Continued growth" headline (6B item 5; l.104).**
Bear from the SAME extract: slide 6 (l.187-188), the deck's own KPI grid, discloses that the two core Rental volume metrics are CONTRACTING year on year — **Number of Signed Units 9,278 (−28%)** and **No. of Beds under Management 16,463 (−8%)** — while only the Distribution-side metrics grow (Projects +20%, Active Licenses +41%, Leads +77%). A quarter in which the Rental franchise's signed-unit flow falls 28% and its managed-bed stock falls 8% is not "continued growth" of the Rental pillar, and it materially qualifies any GREEN read on Rental: the ₹2 Cr Rental "segment profit" (l.143) is being earned on a shrinking book. This decline is on the deck itself, contradicts the l.104 headline, and reinforces (rather than merely repeats) the thesis frame "Distribution scaling profitably, Rental not."
**This counter SURVIVES.** A4 cites slide 6 only for the 16,463-vs-16,460+ data-hygiene point (C9) and for the +57%/+1320 bps consolidated line; it nowhere surfaces the −28% signed-units and −8% beds YoY declines. It must be grafted into A4 before save — as a new contradiction-log row (deck "Continued growth" l.104 vs deck's own Rental KPIs −28%/−8% l.187), into 6B item 5 (downgrade the Rental read / add the volume-contraction caveat), and ideally a QfM row asking management to reconcile Rental volume contraction with the growth headline and the ₹2 Cr segment profit.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

Gap: one surviving bear counter is unincorporated. A4's Rental "GREEN" / "Continued growth" framing (6B item 5; deck l.104) omits the deck's own disclosed Rental volume contraction — Signed Units 9,278 **−28%** and Beds under Management 16,463 **−8%** YoY at extract l.187-188. Supported directly by the extract, it materially qualifies a positive Rental read and must be added to A4's contradiction log, item-5 status, and Questions-for-Management before Notion save.

Coverage (A2/A3) and arithmetic (A4) both PASS; the standing AVOID was correctly respected (flag, not decide). The sole blocker is the ungrafted surviving counter above.

```yaml
stage: A5-adversary
company: "aurum"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Rental graded GREEN / deck headline 'Continued growth' (6B item 5; l.104)"
    counter: "Deck's own KPI grid shows Rental volume contracting YoY: Signed Units 9,278 (-28%) and Beds under Management 16,463 (-8%); only Distribution metrics grow. Rental 'segment profit' Rs.2 Cr (l.143) earned on a shrinking book. A4 cited slide 6 only for data-hygiene, dropping the declines."
    source_line: "l.187-188 (declines); l.104 (growth headline); l.143 (Rental segment profit)"
loop_back_to: "A4"
gap: "A4 dropped the deck's own disclosed Rental volume contraction (Signed Units -28%, Beds -8% YoY, l.187-188). This surviving bear counter must be grafted into the contradiction log, 6B item-5 status, and the Questions-for-Management table before save."
```
