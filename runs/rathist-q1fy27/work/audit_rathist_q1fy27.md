# A5 ADVERSARY / COMPLETENESS AUDIT — Rathi Steel and Power Ltd (RATHIST, BSE 504903) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Audit date: 2026-08-13
Target audited: `review_rathist_q1fy27.md` (A4 ANALYST). Fresh context: I saw only the A4 review, the two A1 extracts, and the two A2 ledgers. Every number below was re-derived independently from the raw Lakhs extract; I did not defer to A4's or A3's cites, I checked them.

OCR handling per task note: the results PDF carries isolated digit garbles the A2 ledger already flags (GARBLE_SUSPECT). Where a raw cell was garbled I reconciled by internal arithmetic and against the clean press-release figures before deciding pass/fail. A FAIL is reserved for a genuine A4 computation error, never for an OCR artifact the ledger already flagged.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The PLAIN-LANGUAGE BRIEF exists at review L298 with all four labelled parts present and carrying real, non-placeholder content:

| Part | Heading | Line(s) | Present? | Content check |
|---|---|---|---|---|
| 1. Summary narrative | "## 1. Summary narrative" | L300-301 | PRESENT | ~20-line narrative; numbers-first; states verdict PROCEED WITH CAVEATS |
| 2. SECTOR intelligence | "## 2. Sector intelligence" | L303-304 | PRESENT | Secondary steel re-roller, NCR cluster, capacity, seasonality, RM drivers |
| 3. BUSINESS-MODEL intelligence | "## 3. Business-model intelligence" | L306-307 | PRESENT | Conversion-spread model, unit economics, mix drift, accounting flatterers |
| 4. COMPETITION intelligence | "## 4. Competition intelligence" | L309-310 | PRESENT | Honest "thin" disclosure, peer set, niche-vs-commodity risk |

GATE 0 = PASS. All four brief parts present and non-empty.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Fresh grep/sweep pass over each A1 extract, diffed against each A2 ledger.

### Results extract (`extract_results_...txt`, 268 lines)

| Category | A2 count | My fresh count | Basis for my count | Orphan rows | Status |
|---|---|---|---|---|---|
| Notes | 5 | 5 | L237, L238-240, L241, L247, L253-257 (five paragraph blocks; markers 3/4/5 garble-displaced, content boundaries clear) | none | PASS |
| Line items | 35 | 35 | L188-223 populated rows minus blank spacer L215 | none | PASS |
| Zero-standing | 10 | 10 | L193,201,203,205,206,207,208,210,211,212 | none | PASS |
| Agenda items | 5 | 5 | L63,67,72,74,81 (single-item board meeting) | none | PASS |
| Auditor paras | 11 | 11 | L96-168, incl. 3 run-together dual-paragraph blocks | none | PASS |
| Entities | 1 | 1 | L241 only hit for subsidiary/associate/JV (none exists) | none | PASS |

### Press-release extract (`extract_presentation_...txt`, 179 lines)

| Category | A2 count | My fresh count | Basis for my count | Orphan rows | Status |
|---|---|---|---|---|---|
| Pages (slides) | 4 | 4 | `^\[page N\]` = L15,56,75,129 | none | PASS |
| Table cells | 18 | 18 | 6 rows (L88-93) x 3 columns | none | PASS |
| Footnotes | 2 | 2 | L95, L96 | none | PASS |
| Section headers | 6 | 6 | L99 + L101,106,111,117,123 | none | PASS |
| Numeric claims (non-table) | 23 | 23 | headline + volume/capacity/FY26 tokens L77,102-107,153-164 | none | PASS |
| Forward/hedge phrases | 6 | 6 | F3-F8 (L137-146) | none | PASS |
| Identifier items | 14 | 14 | H1-H14 | none | PASS |

### Orphan / unreviewed-row check (every ledger row cited in A4 OR marked reviewed-no-finding)

- All 5 notes: cited in A4 Step 0D notes table (L44-50). Reviewed.
- All 35 financial line items incl. garbled cells: carried into A4 Step 1 data table and derived-metrics table (L63-102); OCI sub-line L216 correctly carried as **ND** (unrecoverable), not estimated. Reviewed.
- 10 zero-standing rows (tax/exceptional/discontinuing/purchase): shown nil in A4 Step 1 (L69, L77) and used in bridge (exceptional nil L167). Reviewed.
- 5 agenda items + auditor 11 paras + EoM (L137-143): cited in A4 Step 0D auditor check (L52) and Section C. Reviewed.
- Entity row (Note 3): drives A4's Standalone-vs-Consolidated section (L200-204). Reviewed.
- PR table (18 cells), volume claims (E1-E17), mgmt comment (F1-F8), About block (G1-G11), UNVERIFIED_SUPERLATIVE (G8): reflected in A4 Step 2, Questions table, and the sector/business/competition briefs. Reviewed.
- **Two boilerplate PR blocks — Disclaimer (Slide 12, ledger Table I) and IR-contact/Kirin Advisors (Slide 13, ledger Table J/H12-14)** — are not individually cited by A4 but carry no analytical finding; covered by A4's blanket "No ledger row is unreviewed" (review L20) and are correctly treated as reviewed-no-finding. Not orphans; no material content lost.

**Coverage result: PASS.** My fresh counts equal the A2 ledger counts on every category (no row my pass found that the ledger lacks → nothing back to A2). No ledger row is absent from A4's treatment → nothing back to A3. No orphan rows.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw Lakhs)

All values recomputed from the raw extract cells (OCR-reconciled where the ledger flagged garble; reconciliation confirmed by internal arithmetic + press release). Cr = Lakhs x0.01.

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| TotExp Q1FY27 (sum of expense rows) | 19,019.26 L | 16,074.74+167.02+431.19+208.70+220.70+1,916.91 = 19,019.26 L | l.192-198 | MATCH |
| PBT Q1FY27 (TotRev−TotExp) | 347.99 L (3.48 Cr) | 19,367.25−19,019.26 = 347.99 L | l.190,199 | MATCH (l.204 "341.99" is the flagged OCR garble; 347.99 confirmed 4 ways) |
| Op EBITDA Q1FY27 | 7.51 Cr | 347.99+220.70+208.70−26.21 = 751.18 L | l.204,197,196,189 | MATCH |
| Op EBITDA Q1FY26 | 6.12 Cr | 188.55+259.26+174.93−10.71 = 612.03 L | l.204,197,196,189 | MATCH |
| Op EBITDA Q4FY26 / FY26 | 9.71 / 28.46 Cr | 970.52 L / 2,845.60 L | l.204,197,196,189 | MATCH |
| Op EBITDA margin Q1FY27 / Q1FY26 | 3.88% / 3.94% | 751.18/19,341.04=3.88%; 612.03/15,529.43=3.94% | l.188 | MATCH (−6 bps) |
| Reported EBITDA Q1FY27 | 7.77 Cr | 347.99+220.70+208.70 = 777.39 L | l.204,197,196 | MATCH; ties to PR EBITDA 7.77 (PR L89) |
| Reported EBITDA FY26 | 28.90 Cr | 1,286.49+861.25+742.06 = 2,889.80 L | l.204,197,196 | MATCH; ties to PR FY26 EBITDA 28.90 (PR L164) |
| Reported EBITDA margin (Tot Inc) all periods | 4.01/4.02/4.01/4.03% | 4.014/4.019/4.007/4.033% | l.190 | MATCH |
| Core PBT ex-OI Q1FY27/Q1FY26 | 3.22 / 1.78 Cr | 321.78 / 177.84 L | l.204,189 | MATCH |
| OI/PBT Q1FY27 | 7.53% | 26.21/347.99 = 7.53% | l.189,204 | MATCH |
| Effective tax rate (all) | 0.0% | nil tax / positive PBT | l.205-208 | MATCH |
| PAT margin on Rev-ops Q1FY27/Q1FY26 | 1.80% / 1.21% | 347.99/19,341.04=1.80%; 188.55/15,529.43=1.21% | l.209,188 | MATCH |
| Revenue YoY | +24.55% | (193.41−155.29)/155.29 = 24.55% | l.188 | MATCH |
| Op EBITDA YoY | +22.73% | 139.15/612.03 = 22.73% | derived | MATCH |
| Depreciation YoY | −14.86% | −38.56/259.26 = −14.87% | l.197 | MATCH (rounding) |
| Finance cost YoY | +19.30% | 33.77/174.93 = 19.30% | l.196 | MATCH |
| Operating EBIT YoY | +50.4% | 177.71/352.77 = 50.38% | derived | MATCH |
| Other Income YoY | +144.7% | 15.50/10.71 = 144.72% | l.189 | MATCH |
| Core Op PBT YoY | +80.9% | 143.94/177.84 = 80.94% | l.204,189 | MATCH |
| Reported PBT/PAT YoY | +84.56% | 159.44/188.55 = 84.56% | l.204 | MATCH; ties PR (PR L91) |
| EPS YoY | +81.82% | (0.40−0.22)/0.22 = 81.82% | l.222-223 | MATCH; ties PR (PR L93) |
| EBITDA YoY (reported, diag 4) | +24.83% | 154.65/622.74 = 24.83% | derived | MATCH; ties PR (PR L89) |
| PAT bridge total | +159.44 L | 139.15(op)+15.50(OI)+38.56(dep)−33.77(fin) = 159.44 L | l.188-198 | MATCH; every component re-derived, all tie |
| Operating subtotal in bridge | +139.15 L | 3,811.61−3,194.66−562.75−59.98+144.93 = 139.15 L | l.188-198 | MATCH |
| Recurring-core share of PAT uplift | ~87% | 139.15/159.44 = 87.3% | derived | MATCH |
| Tax-normalised PAT (25.17%) | ~2.60 Cr | 3.48 x 0.7483 = 2.60 Cr | l.204 | MATCH |
| Tax+dep-normalised PAT | ~2.32 Cr | (3.48−0.38) x 0.7483 = 2.32 Cr | l.197,204 | MATCH |
| OCI derived (TCI−PAT) all periods | +0.13/+0.10/+0.13/−0.80 Cr | 12.79/9.72/12.84/−80.28 L | l.217,213 | MATCH |
| Implied Q2+Q3 FY26 OCI | ≈ −102.8 L | −80.28−12.84−9.72 = −102.84 L | l.217 | MATCH |
| Implied Q2+Q3 FY26 depreciation | ~5.31 Cr (~2.65/qtr) | 861.25−259.26−71.04 = 530.95 L | l.197 | MATCH |
| Net worth (equity+reserves) | ~139.09 Cr | 8,636.30+5,273.00 = 13,909.30 L | l.218,220 | MATCH |
| Volume growth YoY | +29.76% | (28,372−21,864)/21,864 = 29.76% | PR L102 | MATCH |
| TMT mix share Q1FY27 | 65.8% | 18,677/28,372 = 65.83% | PR L107,102 | MATCH |
| Non-TMT (stainless) volume Q1FY27/Q1FY26 | 9,695 / 13,569 MT | 28,372−18,677 / 21,864−8,295 | PR L102,107 | MATCH |
| Stainless volume decline | ~28.5% | −3,874/13,569 = −28.55% | PR L102,107 | MATCH |
| QoQ revenue Q1FY27 vs Q4FY26 | −20.9% | (193.41−244.44)/244.44 = −20.87% | l.188 | MATCH |
| PAT margin delta (PR) | 58 bps | 1.797%−1.216% = 58 bps | PR L92 | MATCH |
| Total Income YoY (PR) | 24.63% | 38.27/155.40 = 24.63% | PR L88 | MATCH |

**No arithmetic mismatch above rounding. AUDIT 2 = PASS.**

One methodology note (not a FAIL): the blended-realisation figures A4 quotes (Rs 71,076/MT → Rs 68,260/MT, diagnostic 1 L125) reconcile against **Total Income** (155.40/193.67 Cr ÷ volume), not the Revenue-from-Operations that the same sentence names as the numerator. Computed strictly on Revenue-from-Ops the figures are Rs 71,028 → 68,169/MT. The gap is ~0.07% (the Rs 0.11/0.26 Cr of Other Income) and the "~4% realisation decline" conclusion is identical under either basis (−4.03% vs −3.96%). Immaterial; the headline claim survives. Flagged for A4 tidiness only, does not fail the gate.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to the 3 most-positive claims, from the same extract)

| # | A4's most-positive claim | Strongest bear counter (from the extract) | Counter supported? | Already in A4? |
|---|---|---|---|---|
| 1 | Revenue +24.55% YoY = "strong top-line growth", "genuine volume-led growth" (L112, L229) | Volume rose 29.76% but revenue only 24.55% → realisation fell ~4%; the "strengthened product mix" is a mix-DOWN — TMT doubled to 65.8% while stainless volume fell 28.5% (PR L102,107). Growth is commodity tonnage at a falling price, cannibalising the differentiated niche. | SURVIVES (fully supported) | YES — grafted: diagnostic 1 (L125), F16-MIX, Step 8C (L235), competition brief (L310), Q1 (L245) |
| 2 | Core operating PBT +80.9% / PAT +84.56% "largely real" (L119, L127) | PAT is flattered by two non-durable items in the extract: depreciation fell −14.86% (l.197) and ETR = 0% vs 25.17% statutory (l.205-208). Normalising both → PAT ~2.32 Cr, not 3.48 Cr — roughly a third of headline PAT is tax/depreciation-driven. | SURVIVES (fully supported) | YES — grafted: Step 4 (L171-174), flags 2-3 (L355-356) |
| 3 | "Clean numbers that reconcile in every direction… Filing wins on substance" (L272, L274) | The reconciliation leans on OCR-reconciled cells and on the Q4 FY26 column the auditor expressly flags as **balancing figures, not independently reviewed** (l.137-143); plus governance gaps in the same filing — illegible FRN (l.160), unparseable UDIN (l.166), absent results-page signatory name (l.262), undefined asterisk on Q1FY26 PBT (l.200). "Clean" overstates disclosure rigour. | SURVIVES (fully supported) | YES — grafted: Step 0D auditor check (L52), EoM treatment, governance flag 6 (L359), Q9 (L253) |

All three strongest bear counters are supported by the extract AND are already incorporated into A4's review (A4 is symmetric and already carries each counter with its own line anchor). **No surviving bear counter is missing from A4; nothing new needs grafting.** AUDIT 3 = PASS.

---

## VERDICT

**COMPLETE.** Deliverable gate passes (all four brief parts present). Coverage passes (my fresh enumeration equals the A2 ledgers on all 13 categories; no orphan rows, nothing missing from the ledgers, every row cited or reviewed-no-finding). Arithmetic passes (every derived metric — Operating/Reported EBITDA and margins, ETR, core PBT, YoY/QoQ percentages, the full PAT bridge, OCI derivation, realisation and mix math — reconciles to the raw extract within rounding; the one l.204 "341.99" discrepancy is the ledger-flagged OCR garble, correctly reconciled to 347.99, not an A4 error). Adversarial read passes (the three strongest bear counters all survive but are already incorporated into A4). Only non-blocking note: A4's per-MT realisation uses Total Income rather than the Revenue-from-Ops it names — immaterial (~0.07%), conclusion unchanged.

Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "RATHIST"
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
