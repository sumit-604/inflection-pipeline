# A5 ADVERSARY / COMPLETENESS AUDIT — Sharika Enterprises Limited (SHARIKA), Q1FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Verdict:** COMPLETE (re-run after A4 arithmetic correction)
**Under audit:** `review_sharika_q1fy27.md` (updated in place) | **Re-derived from:** `extract_results_sharika_q1fy27.txt` (597 lines), `ledger_results_sharika_q1fy27.md`
Fresh context; A4/A3 cites checked, not trusted. All ₹ Cr figures independently recomputed from raw ₹-lakh source lines (×0.01).

**Re-run note:** prior pass returned INCOMPLETE on a single Step 4 PAT-bridge arithmetic slip (GP uplift ₹4.45/+2.18 vs correct ₹4.49/+2.22; bridge did not foot). A4 has corrected it. This pass re-derives the bridge independently, confirms it now foots, and re-verifies Gate 0 / Coverage / Adversarial did not regress.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF (review l.465-483) — all four parts present and non-empty:

| Part | Location | Present? |
|---|---|---|
| (1) Summary narrative | l.467-468 | **PRESENT** (~18 lines, numbers-first, symmetric, AVOID maintained) |
| (2) Sector intelligence | l.470-473 | **PRESENT** (Power EPC / smart-grid, copper pass-through, scheme tailwinds) |
| (3) Business-model intelligence | l.475-478 | **PRESENT** (B2B EPC + Spintech pivot, pre-revenue subs, no b/s buffer) |
| (4) Competition intelligence | l.480-483 | **PRESENT** (Rajesh Power, Viviana; ICR/margin/CAGR contrast) |

**GATE 0: PASS** (unchanged — brief untouched by the correction).

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Agenda items | 1 | 1 | 0 | PASS |
| Notes | 20 | 20 (SA 10 l.297-336 + CA 10 l.560-588) | 0 | PASS |
| Line items | 61 | 61 (SA 26 l.251-293 + CA 35 l.504-555) | 0 | PASS |
| Auditor paras | 28 | 28 (SA 14 + CA 14) | 0 | PASS |
| Signature blocks | 24 | 24 (5 groups) | 0 | PASS |
| Zero-standing | 8 | 8 (SA 3 + CA 5) | 0 | PASS |
| Entities | 4 | 4 (Holding + 3 subs; JV Electromeccanica excluded, Note 10) | 0 | PASS |

Fresh count matches the ledger exactly on all seven categories; no orphan rows, none missing from ledger. Every certified ledger row is cited or reviewed-no-finding in A4 (notes → Step 0D; line items → Step 1; auditor paras → Step 0D opinion check; signatures → preamble + T4; zero-standing → Step 1; entities → Step 5B/F15-a; agenda → F13-a; 514.63/514.68 inconsistency → flags/F14-a). **COVERAGE: PASS** (unchanged — enumeration untouched by the correction).

---

## AUDIT 2 — ARITHMETIC (Step 4 bridge re-derived; all other metrics re-verified unchanged)

### Step 4 standalone PAT bridge — INDEPENDENT RE-DERIVATION (the corrected item)

Unrounded ₹-lakh deltas from the cited lines, summed to the reported PAT change:

| Component | Raw lakh delta | A4 (₹ Cr) | My recompute | Status |
|---|---|---|---|---|
| Combined gross-profit uplift (GP 226.57→448.96) | +222.39 | +2.22 | 448.96−226.57 = +222.39 → +2.22 | **PASS (corrected)** |
| Employee cost (145.05−125.03) | −20.02 | (0.20) | −0.20 | PASS |
| Other expenses (175.80−169.28) | −6.52 | (0.07) | −0.07 | PASS |
| Depreciation (22.60−17.18) | −5.42 | (0.05) | −0.05 | **PASS (corrected from 0.06)** |
| Finance cost (88.67−47.81) | −40.86 | (0.41) | −0.41 | PASS |
| Other Income (15.04−3.75) | +11.29 | +0.11 | +0.11 | PASS |
| Deferred-tax swing (−28.01→+9.02) | −37.03 | (0.37) | −0.37 | PASS |
| Exceptional | 0 | 0.00 | 0 | PASS |
| **Reported PAT YoY change** | **+123.83** | **+1.24** | 22.86−(−100.97) = +123.83 → +1.24 | **FOOTS** |

**Sum of components: 222.39 − 20.02 − 6.52 − 5.42 − 40.86 + 11.29 − 37.03 + 0 = +123.83 lakh = +₹1.24 Cr**, which equals the Reported PAT YoY change exactly. **The bridge now foots.** A4 also added the reconciliation note (l.228, l.242) stating the unrounded components sum to +123.83 lakh — confirmed correct. GP memo now reads ₹2.27→₹4.49 Cr (l.234) and narrative answer +₹2.22 Cr (l.245), both consistent.

### Other derived metrics — re-verified, no regression

Spot-re-checked the full derived set that surrounds the edit and downstream:
- SA Op EBITDA Q1FY27 1.28, margin 5.77%, core PBT 0.17, ETR 28.3% — PASS
- CA Op EBITDA 1.48, margin 6.66%, core PBT 0.29, ETR 27.1% — PASS
- SA Rev YoY +31.5%, CA +26.7%; margin +978bps / +1307bps; finance +85.5% / +82.5% — PASS
- Gross margin 13.4%→20.2% (material-cost ratio 86.6%→79.8%) — PASS
- SA-vs-CA gap Q1FY27 +0.07 (+30.6%), FY26 −1.20 (15.5%), Q4FY26 +0.24, Q1FY26 −0.67 — PASS (Step 5B untouched, l.285-290 unchanged)
- ICR ~1.19x (EBIT 105.51 / FC 88.67); receivables ∆ −5.56; advances 2.11; inventory 1.49 — PASS

**ARITHMETIC: PASS.** The single flagged mismatch is resolved; nothing else regressed.

---

## AUDIT 3 — ADVERSARIAL READ (re-confirmed)

The three most-positive claims and their strongest bear counters from the same extract are unchanged by the correction:

1. **"First positive operating quarter is genuine core signal, not treasury"** — bear: no disclosed pass-through clause, comparator Q4FY26 is a Note 4 balancing figure, one un-audited quarter. Survives; **already grafted** (sector intel l.472; Step 3; Step 6D).
2. **"Subsidiaries additive (consol PAT > parent)"** — bear: elimination/accounting effect (₹0.34 Cr inventory credit, l.510), subs pre-revenue cost centres. Survives; **already grafted** (Step 5B l.292, F2-a/F3-a).
3. **"Revenue +31.5% YoY strong"** — bear: distressed base, QoQ only +2.2%, no order book/guidance. Survives; **already grafted** (Step 2C #1, Step 3, competition intel).

No surviving bear counter is absent from A4. **ADVERSARIAL: PASS** (unchanged — A4 remains bear-complete).

---

## VERDICT

**COMPLETE.**
- Gate 0 (deliverable brief): PASS.
- Coverage (A2 enumeration / A3 review): PASS — zero orphans, zero missing rows.
- Arithmetic: PASS — the Step 4 PAT bridge now foots independently to +123.83 lakh = +₹1.24 Cr; GP uplift corrected to ₹2.27→₹4.49 Cr / +₹2.22, depreciation to (0.05). No other metric regressed.
- Adversarial: PASS — all three strongest bear counters already incorporated; none to graft.

Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "SHARIKA"
quarter: "Q1FY27"
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
