# A5 ADVERSARY / COMPLETENESS AUDIT — Macfos Limited (MCFOS), Q1 FY27

Agent: A5 ADVERSARY | Fresh context (A4 review + A1 extract + A2 ledger only; A3 reasoning not consulted).
Every number below re-derived independently from the A1 extract (`extract_results_mcfos_q1fy27.txt`), raw values in Rs Lakhs, converted at x0.01 to Rs Cr. Line numbers are extract lines unless prefixed "review L".

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The PLAIN-LANGUAGE BRIEF exists at review L468 with all four labelled sub-headings present and carrying real, non-placeholder content:

| Part | Heading | Location | Content check | Status |
|------|---------|----------|---------------|--------|
| 1 | SUMMARY NARRATIVE | review L470-472 | ~18-line narrative: +37% rev, +17% PAT, −190bps op margin, OI ~60% of PAT growth, cash conversion dark, Ind AS immaterial, WATCHLIST/AVOID | PRESENT |
| 2 | SECTOR INTELLIGENCE | review L474-476 | specialty-electronics/robotics e-commerce, WC intensity, mainboard red line, China sourcing, ND disclosures named | PRESENT |
| 3 | BUSINESS-MODEL INTELLIGENCE | review L478-480 | asset-light reselling, ~24% GM vs ~34% Robu 2.0, Macfos Electronics drift, cash Achilles heel, undisclosed unit econ named | PRESENT |
| 4 | COMPETITION INTELLIGENCE | review L482-484 | peer margin comparison (Dixon/Centum/IntraSoft), WC weakness, moat/defence optionality, ND items named | PRESENT |

**Gate result: PASS.** All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Fresh grep/row-by-row re-count over the extract, diffed against the A2 gate counts:

| Category | A2 count | My fresh count | Basis of my count | Orphan/missing | Status |
|----------|----------|----------------|-------------------|----------------|--------|
| agenda_items | 13 | 13 | items 1-13 at L53,56,59,62,65,71,77,80,83,88,92,96,98 | none | PASS |
| notes | 8 | 8 | numbered 1,2,4,6,7,8 (L521,529,538,543,549,553) + 2 orphans (L531-533, L534-536) | none | PASS |
| line_items | 98 | 98 | S-P&L 29 + C-P&L 35 + recon-S 15 + recon-C 15 + investor-complaint 4 | none | PASS |
| zero_standing | 25 | 25 | dash/nil rows across both P&Ls, recon blanks, investor-complaint nils, exceptional-item nil | none | PASS |
| auditor_paras | 14 | 14 | standalone LRR 6 (L139-209) + consolidated LRR 8 (L312-413) | none | PASS |
| entities | 3 | 3 | Macfos Ltd (L341), Nuo Zhan (L342), Macfos Electronics (L343) | none | PASS |
| signature_blocks | 6 | 6 | L110, L205, L289, L409, L509, L565 | none | PASS |
| director_profiles | 1 | 1 | N.P. Chavhan (L651-666) | none | PASS |
| turns / slides / questions | 0 | 0 | no transcript, no presentation supplied | none | PASS |

**Fresh count matches A2 on every category → no row found that the ledger lacks (nothing to return to A2).**

**Ledger-row → A4 citation check** (every ledger row must be cited in A4 OR reviewed-no-finding):
- All 8 notes cited in A4 Step 0D table (review L34-41).
- Agenda 1,2 → Ind AS / results (Step 0-1); 3,4 → AGM/scrutinizer CZ & Associates (monitorables L458, Q6); 5 → Q7 + monitorables; 6,8,9,11 → Q5 (L436); 7,12 → duplicate-agenda flag (review L537); 10 → Note 8 investor complaints; 13 → ROC e-forms monitorable (L464). All 13 covered.
- Both LRRs, both Other-Matter paragraphs, UDIN_GARBLED → review L45. Entities → S-vs-C section L270 + Q2/Q4. Director profile → Q7/monitorables/23.04%. Signature blocks incl. Sagar timing → covered/no-finding.
- 25 zero-standing rows: Exceptional Item nil (L43), investor-complaint nils (Note 8 table), OCI/recasting template nils reviewed-no-finding under the L15 blanket ("All rows reviewed at their cited line numbers").

**No orphan row (no ledger row absent from A4). COVERAGE PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract, not from A4's figures)

All recomputed independently in Lakhs then converted. STANDALONE unless marked C.

| Metric (period) | A4 value | My recompute | Source lines (raw Lakhs) | Status |
|-----------------|----------|--------------|--------------------------|--------|
| Op EBITDA Q1FY27 = PBT+D+FC−OI | 8.6358 | 792.13+83.09+100.40−112.04 = 863.58 → 8.6358 | L246,240,238,229 | MATCH |
| Op EBITDA Q1FY26 | 7.4180 | 671.27+75.02+56.05−60.54 = 741.80 | L246,240,238,229 | MATCH |
| Op EBITDA FY26 | 38.1732 | 3435.52+325.13+361.72−305.05 = 3817.32 | L246,240,238,228 | MATCH |
| Op EBITDA margin Q1FY27 | 10.62% | 863.58/8133.87 = 10.617% | L226 | MATCH |
| Op EBITDA margin Q1FY26 | 12.52% | 741.80/5926.80 = 12.516% | L226 | MATCH |
| Reported EBITDA Q1FY27 | 9.7562 | 792.13+83.09+100.40 = 975.62 | L246,240,238 | MATCH |
| Core PBT ex-OI Q1FY27 | 6.8009 | 792.13−112.04 = 680.09 | L246,229 | MATCH |
| Core PBT ex-OI Q1FY26 | 6.1073 | 671.27−60.54 = 610.73 | L246,229 | MATCH |
| Effective tax rate Q1FY27 | 26.53% | 210.18/792.13 = 26.534% | L253,246 | MATCH |
| Effective tax rate Q1FY26 | 25.99% | 174.50/671.27 = 25.996% | L253,246 | MATCH |
| Effective tax rate FY26 | 25.46% | 874.55/3435.52 = 25.456% | L253,246 | MATCH |
| Gross Profit Q1FY27 | 19.4352 | 8133.87−(28.71+7953.00−1791.36) = 1943.52 | L226,233,234,235 | MATCH |
| Gross Margin Q1FY27 | 23.89% | 1943.52/8133.87 = 23.895% | — | MATCH |
| Gross Margin Q1FY26 | 24.04% | 1424.61/5926.80 = 24.036% | — | MATCH |
| Revenue YoY | +37.24% | 2207.07/5926.80 = 37.239% | L226 | MATCH |
| Op EBITDA YoY | +16.42% | 121.78/741.80 = 16.417% | — | MATCH |
| Op EBITDA margin ΔYoY | −190bps | 10.617−12.516 = −1.899pp | — | MATCH |
| Finance cost YoY | +79.13% | 44.35/56.05 = 79.13% | L238 | MATCH |
| Other income YoY | +85.07% | 51.50/60.54 = 85.07% | L229 | MATCH |
| Core PBT ex-OI YoY | +11.36% | 69.36/610.73 = 11.357% | — | MATCH |
| Reported PBT YoY | +18.00% | 120.86/671.27 = 18.004% | L246 | MATCH |
| PAT YoY | +17.15% | 85.18/496.77 = 17.147% | L256 | MATCH |
| EPS YoY | +17.08% | 0.82/4.80 = 17.083% | L274 | MATCH |
| PAT bridge total | +0.8518 | 581.95−496.77 = 85.18 → +0.8518; component sum ties to 0.8517 | L256 | MATCH (ties) |
| Bridge: Employee/OthExp/Dep/FC/OI/Tax deltas | −1.1370/−2.8344/−0.0807/−0.4435/+0.5150/−0.3568 | 113.70/283.44/8.07/44.35/51.50/35.68 | L236,241,240,238,229,253 | MATCH |
| C Op EBITDA Q1FY27 | 8.6328 | 791.41+83.51+100.40−112.04 = 863.28 | L459,450,447,434 | MATCH |
| C Core PBT ex-OI Q1FY27 | 6.7937 | 791.41−112.04 = 679.37 | L459,434 | MATCH |
| C Revenue YoY | +37.24% | 2207.21/5926.80 = 37.241% | L432 | MATCH |
| C PAT YoY | +17.13% | 85.01/496.15 = 17.134% | L467 | MATCH |
| S-vs-C PAT gap Q1FY27 | −0.136% | −0.79/581.95 = −0.1358% | L256,467 | MATCH |
| S-vs-C PAT gap Q4FY26 | +0.147% | +1.46/996.56 = +0.1465% | L256,467 | MATCH |
| Ind AS recon FY26 diff (S) | −20.39 Lakh | 2544.50−2564.88 = −20.38→−20.39 (rounding of components) | L581,582,584 | MATCH |

**Two trivial rounding observations (NOT failures — each ≤0.01pp, within 2-decimal rounding tolerance):**
- PAT margin Q1FY27 standalone: A4 = 7.16%; my recompute 581.95/8133.87 = 7.1547% → rounds to 7.15% (review L123, L340). Delta 0.005pp.
- PAT margin Q1FY27 consolidated: A4 = 7.15%; my recompute 581.16/8134.01 = 7.1448% → rounds to 7.14% (review L136). Delta 0.005pp.

Both sit on the rounding boundary and do not affect any verdict, threshold classification (AMBER band 6.5–7.5% either way), or downstream number. **Not FAIL-worthy.** ARITHMETIC PASS.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear counter to the three most positive claims, from the same extract)

**Positive claim 1 — "Revenue +37.24% YoY, strongest Q1 on record, clears the ≥30% green and ≥35% convert-to-invest lines" (review L150, L166).**
Strongest bear counter from the same text: (a) it is a single quarter and Q1 is the seasonal trough — revenue is DOWN −20.3% sequentially from the Q4 peak (102.11→81.34, review L189); (b) the Q1 FY26 comparator is management-converted, NOT limited-reviewed (F7-01, extract L183-189/362-368), so the +37% is not audit-grade.
Survives? **NO — already incorporated.** Step 2 preamble labels YoY "weakly assured... directionally reliable but not audit-grade" (review L146); Step 3 states the −20.3% QoQ reset; 6D marks the revenue trigger "ON TRACK (needs full-year confirmation)."

**Positive claim 2 — "PAT +17.15% YoY" (review L159).**
Strongest bear counter: ~60% of the +0.8518 Cr PAT increase is Other Income (+85% YoY, +0.5150 Cr, extract L229), which is non-recurring; core operating PBT grew only +11.36%; strip OI to prior level and run-rate PAT growth collapses to ~+2.4%.
Survives? **NO — already incorporated.** Step 4 states this verbatim (review L220-221); PAT-quality flag at review L536.

**Positive claim 3 — "No thesis-broken trigger fired; destination PE unchanged ~22x; entry zone Rs 477–596 stands" (review L362, L393).**
Strongest bear counter: the CFO/PAT deal-breaker (FY26 −0.31x, on a failing trajectory) just went DARK exactly as the two metrics that would worsen it are flashing — finance cost +79% YoY and a Rs 17.9 Cr inventory build (extract L238, L235) — and operating margin contracted −190bps with PAT margin AMBER (7.16→ my 7.15%, below the 7.5% green). "No trigger fired" reflects untestability, not health.
Survives? **NO — already incorporated.** Step 5 (review L250), Step 6C (L359 "on a failing trajectory"), Step 7 HOLD rationale, and flags L530-531 all carry it; verdict capped at PROCEED WITH CAVEATS with missing evidence named.

**All three strongest bear counters are already present in A4's review. No surviving un-incorporated counter → nothing to graft back into A4.**

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four plain-language brief parts present).
- Coverage: PASS (fresh counts match A2 on all categories; zero orphan rows; zero rows missing from ledger).
- Arithmetic: PASS (every derived metric reproduces from raw extract; two ≤0.01pp PAT-margin rounding nits noted, within tolerance, not failures).
- Adversarial: PASS (three strongest bear counters all already incorporated; none survives as a new required addition).

No loop-back required. This review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "MCFOS"
quarter: "Q1 FY27"
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
