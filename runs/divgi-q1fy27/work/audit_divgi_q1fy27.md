# A5 ADVERSARY / COMPLETENESS AUDIT — DIVGI TORQTRANSFER, Q1 FY27
# Model: Opus 4.8 | Fresh context: A4 review + A1 extracts + A2 ledgers only.
# Independent re-derivation. I do not defer to A3/A4 cites; I check them.

Review under audit: `review_divgi_q1fy27.md`
Evidence spine: `extract_results_*`, `extract_presentation_*`, `ledger_results_*`, `ledger_presentation_*`.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF present as a labelled final section (review lines 364-396). All four parts present and carry real, non-placeholder content:

| Brief part | Location | Present? | Content check |
|---|---|---|---|
| 1. Summary narrative | L366-370 | PRESENT | ~15 lines; numbers-first; both bull and three tempering items |
| 2. SECTOR intelligence | L372-378 | PRESENT | Provenance-labelled (this-quarter vs general knowledge); exports 6.2x, ₹80cr target, un-disclosed metrics named |
| 3. BUSINESS-MODEL intelligence | L380-387 | PRESENT | Provenance-labelled; unit economics, model drift (EV + US legs), un-disclosed WC named |
| 4. COMPETITION intelligence | L389-396 | PRESENT | Provenance-labelled; named partners/peers, structural-weakness bear side, un-disclosed market share named |

Gate 0 result: PASS. All four provenance-labelled intelligence blocks present.

---

## AUDIT 1 — COVERAGE (fresh grep pass diffed against A2 ledgers)

Fresh enumeration (my own pass over the two extracts) vs A2 counts:

| Category | A2 count | My fresh count | Method | Orphan/missing | Status |
|---|---|---|---|---|---|
| Results notes | 7 | 7 | numbered notes L344-383 | none | PASS |
| Board agenda items | 5 | 5 | L58/65/69/87/96 | none | PASS |
| Annexure I rows | 4 | 4 | Sr 1-4, L114-168 | none | PASS |
| Auditor paras | 4 | 4 | paras 1-4, L191-217 | none | PASS |
| P&L line-item rows | 29 | 29 | table L254-304 | none | PASS |
| Entities | 2 | 2 | reporting co + Foreign Entity | none | PASS |
| Signatory blocks | 4 | 4 | Kokane/Mahadik/Divgi x2 | none | PASS |
| Zero-standing (results) | 1 | 1 | Other equity L297 | none | PASS |
| Presentation slides | 41 | 41 | grep `^\[page` = 41 | none | PASS |

No row my fresh pass found is absent from the ledger. No count mismatch. GATE A2 independently reconfirmed.

Every ledgered disclosure UNIT addressed in the A4 review (orphan-row check):

- 7 notes: Step 0D-Table addresses all seven individually (review L51-57). Covered.
- 5 agenda items: 1 (results, Section A throughout); 2 (AGM 18-Sep, Q12 + monitorable 8); 4 (dividend ₹3.27 / record 10-Sep, Q12 + monitorable 8); 5 (auditor change, Step 0D L59 + Q11 + monitorable 9). Agenda 3 (Scrutinizer appointment, CS Sathaye) not individually discussed but is routine e-voting boilerplate; carried by the preamble's explicit "5 board-agenda items … every enumerated row read" reconciliation (L16) as reviewed/no-finding. Covered (no-finding).
- 4 annexure rows: auditor-appointment substance in Step 0D L59 and Q11; row 4 (director-relationship N/A) is the zero-standing template row, acknowledged. Covered.
- 4 auditor paras: Step 0 "Auditor opinion" (L44) covers scope/responsibility/SRE-2410/conclusion and affirmatively records absence of EoM / Other Matters / Going Concern. Covered.
- 29 P&L rows: Step 1 data table. Zero-standing "Other equity" (₹620.2 Cr FY26-only) acknowledged via preamble "1 zero-standing row"; ties to slide-39 Other Equity 620.2. Covered.
- 2 entities + standalone-only fact: Note 7 in Step 0D, Q1/Q2/Q13, and the STANDALONE-vs-CONSOLIDATED preamble (L30). Covered.
- 41 slides: all quantitative/forward slides (5-14, 16-18, 20-21, 28, 33-40) cited; descriptive/roster/divider slides (15,19,22-27,29-32,41) carried by the 41-slide reconciliation (L17) as reviewed/no-finding. Covered.

STANDALONE-ONLY and FRESH-COMPANY handling (specifically checked per task):
- Review states STANDALONE-ONLY plainly (L30) and does NOT invent a standalone-vs-consolidated gap: `sc_gap_pat_pct = ND` for every period, on the correct ground that no consolidated baseline exists in the filing. Correct.
- Review states FIRST-COVERAGE plainly (L7, L40, L255) and does NOT invent a prior Decision Status, entry zone, or thesis. Step 6/7/8 run as fresh-baseline, annotated. Correct.

COVERAGE result: PASS. No orphan ledger rows; no rows missing from ledger.

---

## AUDIT 2 — ARITHMETIC (independent re-foot from raw extract line values)

Units: results filing in ₹ million (L248), ×0.1 to ₹ Cr. Presentation in ₹ Cr (×1).
All raw values below taken from `extract_results_*` lines 229-278 (physical file lines 255-303 per ledger mapping).

### 2a. Headline P&L re-foot (raw millions → Cr), Q1 FY27 / Q1 FY26 / Q4 FY26 / FY26

| Metric | A4 value | My recompute (source) | Status |
|---|---|---|---|
| Revenue Q1FY27 | 137.14 | 1,371.42m ×0.1 = 137.14 (L255) | PASS |
| Revenue Q1FY26 | 71.68 | 716.76m = 71.68 | PASS |
| Revenue Q4FY26 | 107.62 | 1,076.22m = 107.62 | PASS |
| PBT Q1FY27 | 33.75 | 337.51m = 33.75 (L270) | PASS |
| PAT Q1FY27 | 25.24 | 252.40m = 25.24 (L277) | PASS |
| EPS Q1FY27 | 8.25 | 8.25 (L303) | PASS |
| EPS Q4FY26 | 5.06 | A3-corrected 5.06 (raw OCR "506") | PASS — A3 corr applied |
| FY26 Δ inventories | (8.08) | A3-corrected (80.76)m = (8.08), NOT (807.60) | PASS — A3 corr applied |
| Deferred tax Q1FY27 | (0.07) | (0.65)m = (0.07) (A3 series -0.65/-17.43/4.11/-1.21) | PASS — A3 corr applied |

FY26 total-expenses footing proof (independently re-run with corrected inventory):
1,448.73 − 80.76 + 415.41 + 3.10 + 292.37 + 1,045.37 = 3,124.22m = printed total (L268). Confirms (80.76) not (807.60). A3 CORRECTION 1 is arithmetically correct and applied throughout.

### 2b. Derived metrics (recomputed from the re-footed Cr values)

| Metric | A4 value | My recompute | Status |
|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 37.02 | 33.75+7.82+0.07−4.62 = 37.02 | PASS |
| Op EBITDA margin Q1FY27 | 27.0% | 37.02/137.14 = 26.99% | PASS |
| Op EBITDA margin Q1FY26 | 19.5% | 14.00/71.68 = 19.53% | PASS |
| Op EBITDA margin YoY | +745 bps | 26.99−19.53 = 746 bps (raw-precise 747 bps) | PASS (within rounding; 745/746/747 all rounding-band) |
| Reported EBITDA Q1FY27 | 41.64 | 33.75+7.82+0.07 = 41.64 | PASS |
| Rep EBITDA margin on Total Inc Q1FY27 | 29.4% | 41.64/141.76 = 29.37% | PASS (ties deck slide 12/14) |
| Core PBT ex-OI Q1FY27 | 29.13 | 33.75−4.62 = 29.13 | PASS |
| Core PBT ex-OI Q1FY26 | 6.99 | 12.08−5.09 = 6.99 | PASS |
| OI/PBT Q1FY27 | 13.7% | 4.62/33.75 = 13.69% | PASS |
| Effective tax rate Q1FY27 | 25.2% | 8.51/33.75 = 25.21% | PASS |
| PAT margin Q1FY27 | 18.4% | 25.24/137.14 = 18.40% | PASS |
| Revenue YoY | +91.3% | 65.46/71.68 = 91.32% | PASS |
| Op EBITDA YoY | +164.4% | 23.02/14.00 = 164.4% | PASS |
| Core PBT ex-OI YoY | +316.7% | 22.14/6.99 = 316.7% | PASS |
| Reported PBT YoY | +179.4% | 21.67/12.08 = 179.4% | PASS |
| PAT YoY | +182.6% | 16.31/8.93 = 182.6% | PASS |
| EPS YoY | +182.5% | 5.33/2.92 = 182.5% | PASS |
| Revenue QoQ | +27.4% | 29.52/107.62 = 27.43% | PASS |
| Core PBT ex-OI QoQ | +107.6% | 15.10/14.03 = 107.6% | PASS |
| PAT QoQ | +63.0% | 9.76/15.48 = 63.05% | PASS |

### 2c. PAT bridge (Step 4) re-foot
Core PBT +22.14 (29.13−6.99); OI change −0.47 (4.62−5.09); tax drag −5.36 (8.51−3.15).
Cross-check: 22.14 − 0.47 − 5.36 = 16.31 = reported PAT change (25.24−8.93). PASS.
Reported-PBT tie: 22.14 + (−0.47) = 21.67 = 33.75−12.08. PASS.

### 2d. Cash / balance-sheet metrics (deck slides 36/37/39/40, ₹ Cr, ×1)

| Metric | A4 value | My recompute (source) | Status |
|---|---|---|---|
| CFO FY26 / FY25 | 41.1 / 35.2 | 41.1 / 35.2 (s40 L1299) | PASS |
| CFO/PAT FY26 | 0.88x | 41.1/46.9 = 0.876 | PASS |
| CFO/PAT FY25 | 1.44x | 35.2/24.4 = 1.443 | PASS |
| Inventory Δ | +51.9% | 20.1/38.7 = 51.94% (s39) | PASS |
| Receivables Δ | +42.9% | 23.8/55.5 = 42.88% | PASS |
| Payables Δ | +49.1% | 19.8/40.3 = 49.13% | PASS |
| Net cash Mar-26 | 232.6 | (232.6) net debt (s36 L1156) | PASS |
| Capex FY25 / FY26 | 44 / 27 | A3-corrected series (s37) | PASS — A3 corr applied |
| IPO capex deployed | 60.7% | 915.27/1,507.07 = 60.73% (Note 3) | PASS |
| Dividend outlay | ~₹10.0 Cr | ₹3.27 × 30.582m sh = ₹10.0 Cr | PASS |

### 2e. A3 CORRECTION 2 (presentation) — applied check
- Slide 35 PAT FY21-FY26 = 38/46/51/40/24/47: independently ties to slide-38 table PAT (38.3/46.2/51.2/39.7/24.4/46.9 rounded). Applied. PASS.
- Slide 37 Cash Reserves reorder (FY23=311 ties Mar-23 BS bank 306.6+cash 4.8=311.4): consistent; not headline-bearing. Applied. PASS.
- Slide 11 mix Q1FY27 = TC 53 / Components 24 / Others 18 / E-Gear 4: internally consistent (E-Gear 5.7/141.8 ≈ 4%; TC 76/141.8 ≈ 53%). Review Step 8.5b adopts corrected ordering. Applied. PASS.

### 2f. ARITHMETIC MISMATCH FOUND — 1

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| RoCE trajectory, **FY24** (Step 7 baseline table, review L243) | **12.5%** | **9.3%** | slide 37, extract L1179 (RoCE FY21-FY26 = 17.8/18.3/12.5/9.3/5.6/9.9). 12.5% is the **FY23** value; FY24 = 9.3% | **FAIL** |

The review states the RoCE recovery arc as "FY24 12.5% → FY25 5.6% → FY26 9.9% (recovering off a trough)." Slide 37 maps 12.5% to FY23 and 9.3% to FY24. The stated FY24 figure is wrong by 3.2 pp — above rounding. The substantive claim (FY25 5.6% trough, FY26 9.9% recovery) is correct and the FY26 baseline recorded in Step 6A (9.9% / RoIC 12.7%) is correct; but the FY24 label carries an unsupported value into a table explicitly recorded as a "fresh baseline input … for that future Role 1 valuation" (review L239-243), i.e. it would persist into durable Notion memory. Responsible agent: A4 (transcription; the A2 presentation ledger Table 2e L196 carries the correct RoCE series, and A3 issued no RoCE correction).

ARITHMETIC result: FAIL on one cell (Step 7 RoCE FY24). All headline P&L, margins, tax rate, YoY/QoQ, PAT bridge, and cash metrics re-foot exactly; all A3 corrections correctly applied.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from the SAME extract)

Findings-to-questions completeness (checked independently against review Step 8.5 + Coverage Map L402-418): all 13 AMBIGUOUS/FORWARD-SIGNAL findings map to ≥1 question — A3-F2→Q2, A3-F6a→Q2, A3-F6b→Q5, A3-F13a→Q11, A3-F13b→Q12, A3-F15→Q1/Q13, A3-01→Q4, A3-02→Q8/Q9/Q10, A3-03→Q8, A3-04→Q4, A3-05→Q1/Q3, A3-06→Q6, A3-07→Q7. 13/13 mapped; every question exists in the Step 8.5 table. No unmapped finding. PASS.

Positive claim 1 — "Revenue +91.3% YoY, Op EBITDA margin +745 bps, growth is operational not treasury."
Bear counter (same text): the +91% sits on a single weak Q1FY26 base (₹71.68 Cr) with no independently-filed prior trend, and the QoQ base (Q4FY26) is a Note-6 balancing figure; the 27.0% Op EBITDA margin is a single-quarter high above every historical annual EBITDA%. SURVIVES? No — the review already flags the Note-6 balancing caveat (Step 3), the fresh-baseline low-base problem, and sets the Q2 ≥₹137 Cr / ≥27% plateau test (Step 3 L154). Incorporated.

Positive claim 2 — "Net cash ₹232.6 Cr, zero leverage, funds EV/US without debt."
Bear counter (same text): the balance sheet is Mar-26 not Jun-26 (A3-07); FY26 CFO/PAT fell to 0.88x on a ₹20.8 Cr WC build (inventory +51.9%, receivables +42.9%); the cash pile is about to be drawn by US-subsidiary remittance and ₹591.8m undeployed IPO capex, so headline net-cash overstates free liquidity and conversion is deteriorating. SURVIVES? No — review flags INDETERMINATE Q1 cash conversion (capped at PROCEED WITH CAVEATS), the WC drag, the Mar-26 staleness, and the US-capital outflow (Steps 5/8, Q4/Q7). Incorporated.

Positive claim 3 — "Core operating PBT +316.7%, ~100% recurring, not treasury or tax."
Bear counter (same text): the Transfer-Case engine (53% of mix, +93%) leans on the single Indonesia 4x4 program (concentration); EV/E-Gear is contracting (−20%) on a slipped flagship; "Others +229%" is off a ~₹6.5 Cr base; and D&A up only 12.7% while ₹591.8m capex + the US build are still ahead means future depreciation will compress the very margin celebrated. SURVIVES? No — review flags single-program EV timing risk (Step 8C, sector brief), the undeployed capex, and explicitly warns "steady-state D&A will rise" (Step 4 L175). Incorporated.

ADVERSARIAL result: no surviving bear counter requiring graft. The review is symmetric; the bear side is already carried in its five named caveats.

---

## VERDICT

INCOMPLETE.

- loop_back_to: A4
- gap: Step 7 "Four-Pillar Destination PE" baseline table (review L243) mislabels the RoCE recovery arc — states "FY24 12.5%" where slide 37 (extract L1179) gives FY24 = 9.3% (12.5% is the FY23 value). 3.2 pp mismatch, above rounding, in a table explicitly recorded as a fresh baseline input for the future Role 1 valuation and destined for Notion memory. Fix: relabel to FY23 12.5% → FY24 9.3% → FY25 5.6% → FY26 9.9%, or state FY24 9.3% directly. All other audits pass (deliverable gate PASS; coverage clean; all headline P&L / margins / YoY-QoQ / PAT-bridge / cash metrics re-foot exactly; all A3 corrections applied; 13/13 findings mapped; no surviving bear counter). This is a single-cell correction; on its remediation the review is otherwise save-ready.

```yaml
stage: A5-adversary
company: "divgi"
quarter: "q1fy27"
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
  - metric: "Step 7 RoCE trajectory, FY24"
    a4_value: "12.5%"
    recomputed: "9.3%"
    source_line: "presentation extract L1179 (slide 37 RoCE FY21-FY26 = 17.8/18.3/12.5/9.3/5.6/9.9; 12.5% is FY23, FY24 = 9.3%)"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Step 7 baseline table (review L243) states RoCE FY24 = 12.5%; slide 37 (extract L1179) gives FY24 = 9.3% (12.5% is FY23). 3.2pp mismatch above rounding in a fresh-baseline input recorded for the future Role 1 valuation. Relabel FY23 12.5% -> FY24 9.3% -> FY25 5.6% -> FY26 9.9%."
```
