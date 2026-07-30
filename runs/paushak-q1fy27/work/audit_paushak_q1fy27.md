# A5 ADVERSARY / COMPLETENESS AUDIT — Paushak Limited (PAUSHAK) — Q1 FY27

Quarter ended 30 June 2026 | Audited 2026-07-30 | Agent A5 (Adversary)
Fresh context: A4 review + A1 extract + A2 ledger only. All counts re-derived by
independent grep; all metrics recomputed from raw lakhs (x0.01 to Cr). I do not
defer to A4's or A3's cites.

---

## AUDIT 1 — COVERAGE (independent grep re-enumeration vs A2 ledger)

Fresh grep passes run over `extract_results_paushak_q1fy27.txt`:
- Sr-numbered statement rows (L89-132): **11** (rows 1-11; four are non-value headers: 3 Expenses, 5 Tax, 7 OCI, 11 EPS).
- Lettered/roman sub-rows: expenses (a)-(f) = 6 (L95-102), tax (a)(b) = 2 (L109-110), OCI A(i)/A(ii)/B(i)/B(ii) = 4 (L115-122) → **12**.
- EPS Basic & Diluted sub-row (L133) = **1**.
- Subtotals Total Income (L92) + Total Expenses (L104) = **2**.
- Notes (L137-145, restricted to Notes block) = **5**. (My raw `^\s+[0-9]+` grep also caught L221 "2025 expressed…" — a continuation line of the Other-Matter para, correctly NOT a note; ledger properly excluded it.)
- Auditor paras: 1-4 (L165/171/179/190) + Other Matter "5." (L216) = **5**.
- Agenda item (Board Outcome, L27-32) = **1**. Entity (standalone, L81/161-169) = **1**. Signature blocks (L44-50, L224-235) = **2**.

Line-item total = 11 + 12 + 1 + 2 = **26**. Every category matches the ledger exactly.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| agenda_items | 1 | 1 | none | PASS |
| line_items | 26 | 26 | none | PASS |
| notes | 5 | 5 | none | PASS |
| auditor_paras | 5 | 5 | none | PASS |
| entities | 1 | 1 | none | PASS |
| signature_blocks | 2 | 2 | none | PASS |
| **TOTAL** | **40** | **40** | **none** | **PASS** |

**Orphan-row check (ledger rows absent from A4).** All material rows are cited in
A4: OCI reclassifiable line 7B(i) at L119 (Step 2 diag 6, Step 3), Other Equity row
10 (Step 5 net-worth Rs 395.96 Cr), Note 4 balancing-figure (Step 0D, Step 3), Other
Matter para (Step 0D, Q5), single-entity scope (S-vs-C section). The immaterial
non-reclassifiable OCI lines 7A(i)/7A(ii) (Rs 2 lac / Rs 0 lac) and Total
Comprehensive Income (row 8) are not individually discussed but are covered by A4's
explicit blanket "**All 40 reviewed**" (review L18) plus the substantive OCI-block
discussion — they carry zero P&L or thesis impact, so this is a valid
"reviewed, no finding" disposition, not an orphan. **No orphan row. No fresh row the
ledger lacks. Coverage COMPLETE.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw lakhs; every A4 derived metric)

Raw source values (lakhs, x0.01 → Cr) taken from L89-133. Spot-recompute of every
derived cell in A4 Steps 1-6:

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 25.65 | 19.02+8.42+1.36−3.15 = 25.65 | L106/101/100/90 | PASS |
| Op EBITDA Q1FY26 | 17.85 | 15.63+4.06+0.04−1.88 = 17.85 | L106/101/100/90 | PASS |
| Op EBITDA Margin Q1FY27 | 30.70% | 25.65/83.55 = 30.70% | L89 | PASS |
| Op EBITDA Margin Q1FY26 | 31.94% | 17.85/55.88 = 31.94% | L89 | PASS |
| Reported EBITDA Q1FY27 | 28.80 | 19.02+8.42+1.36 = 28.80 | L106/101/100 | PASS |
| Core PBT ex-OI Q1FY27 | 15.87 | 19.02−3.15 = 15.87 | L106/90 | PASS |
| Core PBT ex-OI Q1FY26 | 13.75 | 15.63−1.88 = 13.75 | L106/90 | PASS |
| OI/PBT Q4FY26 | 51.25% | 8.21/16.02 = 51.25% | L90/106 | PASS |
| Effective Tax Rate Q1FY27 | 20.56% | 3.91/19.02 = 20.56% | L109-110/106 | PASS |
| Effective Tax Rate Q1FY26 | 23.03% | 3.60/15.63 = 23.03% | L109-110/106 | PASS |
| ETR FY26 | 22.00% | 11.09/50.41 = 21.99% | L109-110/106 | PASS |
| PAT Margin Q1FY27 | 18.07% | 15.10/83.55 = 18.07% | L112/89 | PASS |
| Gross Profit Q1FY27 (Rev−(Mat+ChgInv)) | 57.36 | 83.55−(28.99−2.80) = 57.36 | L89/95/96 | PASS |
| Gross Margin Q1FY27 | 68.65% | 57.36/83.55 = 68.65% | L89 | PASS |
| Gross Margin Q1FY26 | 82.39% | 46.04/55.88 = 82.39% | L89 | PASS |
| Revenue YoY | +49.52% | (83.55−55.88)/55.88 = 49.52% | L89 | PASS |
| Op EBITDA YoY | +43.70% | (25.65−17.85)/17.85 = 43.70% | derived | PASS |
| Op EBITDA Margin YoY | −124 bps | 30.70−31.94 = −1.24 pp | derived | PASS |
| Gross Margin YoY | −1,374 bps | 68.65−82.39 = −13.74 pp | derived | PASS |
| Depreciation YoY | +107.39% | (8.42−4.06)/4.06 = 107.39% | L101 | PASS |
| Finance Cost YoY | +3,300% | (1.36−0.04)/0.04 = 3,300% | L100 | PASS |
| EBIT-op YoY | +24.94% | (17.23−13.79)/13.79 = 24.94% | derived | PASS |
| Core Op PBT YoY | +15.42% | (15.87−13.75)/13.75 = 15.42% | derived | PASS |
| PAT YoY | +25.52% | (15.10−12.03)/12.03 = 25.52% | L112 | PASS |
| EPS YoY | +25.61% | (6.13−4.88)/4.88 = 25.61% | L133 | PASS |
| QoQ revenue step | +51.5% | (83.55−55.14)/55.14 = 51.52% | L89 | PASS |
| Q2+Q3 FY26 agg revenue | 107.58 | 218.60−55.88−55.14 = 107.58 | L89 | PASS |
| Q2+Q3 FY26 agg core PBT | 16.74 | 38.30−13.75−7.81 = 16.74 | derived | PASS |
| PAT bridge: GP revenue effect | +22.80 | 27.67×0.8239 = 22.80 | derived | PASS |
| PAT bridge: GP margin effect | −11.48 | −0.1374×83.55 = −11.48 | derived | PASS |
| PAT bridge total | +3.10→+3.07 | Σ = +3.10 vs actual +3.07 | L112 | PASS (rounding, disclosed) |
| Statutory-rate tax shield | ~461 bps | 25.17−20.56 = 4.61 pp | derived | PASS |
| Annualized EPS (naive 4x) | 24.52 | 6.13×4 = 24.52 | L133 | PASS |
| FY26 net worth | 395.96 | 383.63+12.33 = 395.96 | L130/127 | PASS |
| OI-reverts PAT sensitivity | +14.9% | (13.83−12.03)/12.03 = 14.96% | derived | PASS |
| Recurring PAT share | ~59% / ~41% | 1.80/3.07 / 1.27/3.07 = 58.6/41.4% | derived | PASS |

**No arithmetic mismatch above rounding.** The only imperfect reconciliation is the
PAT bridge (Σ components = +3.10 vs reported ΔPAT +3.07); the 0.03 Cr = 3-lakh gap is
accumulated two-decimal rounding across nine components, and A4 discloses it verbatim
("+3.10 (rounding to +3.07)"). Not a FAIL.

**One narrative-precision note (not an arithmetic FAIL, not looped back).** At review
L162-163 A4 says the lower tax rate was "worth ~Rs 0.31 Cr" and "flattered PAT"; the
bridge table row for tax is correctly **−0.31** (absolute tax rose 55.88→… i.e. tax
went 3.60→3.91, a drag). The isolated rate-decline benefit vs a constant base is
~Rs 0.47 Cr (4.38 hypothetical − 3.91 actual). The 0.31 figure is the absolute change,
loosely labelled; the table value is correct, so no metric fails. Flagged for A4
polish only, does not gate save.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from same extract)

**Claim 1 (review L130, L195-205).** "Revenue +49.52% YoY / +51.5% QoQ; MPP-8 volume
lifting the run-rate above the ~Rs 55 Cr plateau — clear run-rate step-change."
- **Bear counter from the extract:** the QoQ step is measured off Q4FY26, which Note 4
  (L142-143) states is a **balancing figure** (derived, not independently reported), and
  the "plateaued near Rs 55 Cr for **four quarters**" phrasing (L195) is not supported —
  only two quarters are disclosed near 55 (Q1FY26 55.88, Q4FY26 55.14); Q2FY26 and Q3FY26
  per-quarter revenue is ND (only the 2-qtr avg 53.79 is derivable). A single high quarter
  above a two-point line could be order-timing, not sustained utilization; utilization %
  is undisclosed (Reg 33).
- **Survives?** NO — already incorporated. A4 flags Q2/Q3 as ND (L183-184, L190), flags
  Q4 as a lower-confidence balancing figure (L198-201), and states the reversion test
  explicitly (L206-208: "a reversion toward Rs 55 would signal the Q1 step was
  order-timing"). The "four quarters" wording overstates, but the substantive caveat is
  present. No graft required.

**Claim 2 (review L138, L156-159).** "Core operating PBT ex-OI grew +15.42% YoY = real
operational growth, positive."
- **Bear counter from the extract:** +15.42% core-PBT growth was delivered on +49.52%
  revenue growth — core pre-tax profit grew at less than one-third the rate of revenue,
  i.e. **incremental operating leverage is deeply negative** because gross margin fell
  1,374 bps and depreciation (+107%) plus finance cost (+3,300%) now fully load the P&L.
  The "real growth" is real but decelerating per rupee of revenue.
- **Survives?** NO — already incorporated. A4 states headline "overstates operational
  momentum by ~10 pp" (L159) and the Step-4 decomposition shows the +Rs 22.80 Cr volume
  effect "almost entirely consumed" by margin/dep/other-expense/finance drags (L231-234),
  and Growth Trigger "Pricing power" is marked WEAKENED (L358). No graft required.

**Claim 3 (review L172-176, tripwire 5 GREEN L327).** "Other-Income one-off did not
recur; OI/PBT fell to 16.56%; this quarter's PAT is not treasury-inflated."
- **Bear counter from the extract:** Other Income still rose **+67.55% YoY** (1.88→3.15,
  L90) and in the PAT bridge **+Rs 1.27 Cr — 41% of the entire +Rs 3.07 Cr PAT gain — is
  the Other-Income increase**, which the bridge itself labels "NON-recurring/treasury"
  (L224). There is an internal tension: A4 calls OI "clean ~Rs 3 Cr recurring base" in
  Step 2 yet "non-recurring/treasury" in the Step 4 bridge. Either way, a meaningful slice
  of the PAT step-up is non-operating.
- **Survives?** NO — already incorporated. A4 quantifies the 41% non-recurring share
  explicitly (L229), runs the OI-normalized sensitivity (PAT still +14.9%, L235-238), and
  raises the recurring-base ambiguity as Question 3 to management (L441). The
  recurring-vs-treasury tension is surfaced, not buried. No graft required.

**Result:** all three strongest bear counters are already present in A4's review (as
caveats, sensitivities, weakened-trigger calls, or management questions). **No surviving
bear counter needs grafting.**

---

## VERDICT

**COMPLETE.** Coverage: 40/40 rows re-enumerated by independent grep, exact match, no
orphan row, no missing row. Arithmetic: every derived metric recomputed from raw lakhs,
no mismatch above rounding (the +3.10/+3.07 bridge gap is disclosed rounding).
Adversarial: the three most-positive claims each have a real bear counter, but all three
are already incorporated in A4. One minor narrative-precision note (tax "0.31" labelling,
L162) is flagged for polish and does not gate the save. Nothing loops back to A2, A3, or
A4. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "PAUSHAK"
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
