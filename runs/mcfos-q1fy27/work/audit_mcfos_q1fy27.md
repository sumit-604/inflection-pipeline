# A5 ADVERSARY / COMPLETENESS AUDIT — Macfos Limited (MCFOS), Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context (A4 review + BOTH A1 extracts + BOTH A2 ledgers only; A3 reasoning NOT seen; all figures re-derived independently).
Review under audit: `review_mcfos_q1fy27.md` (MERGED — results filing + investor presentation).
Loop history: loop-0 = INCOMPLETE (two Step-4 prose figures failed); **loop-1 re-audit = COMPLETE** (A4 applied the exact two corrections; re-verified below).
Verdict: **COMPLETE.** Proceeds to Notion save.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

PLAIN-LANGUAGE BRIEF located at review L486. All four labelled parts present and carrying real, non-placeholder content:

| Part | Heading | Line | Present? | Content check |
|------|---------|------|----------|---------------|
| 1 | SUMMARY NARRATIVE | L488 | **present** | ~1 dense paragraph (>15 sentences); anchored THIS FILING/THIS DECK/PRIOR NOTION tags |
| 2 | SECTOR INTELLIGENCE | L492 | **present** | real content (e-com distribution, WC intensity, Ind AS, mainboard catalyst, China sourcing) |
| 3 | BUSINESS-MODEL INTELLIGENCE | L496 | **present** | real content (asset-light trading, Robu 2.0, AOV/customer bridge, cash Achilles heel) |
| 4 | COMPETITION INTELLIGENCE | L500 | **present** | real content (peer margins, WC weakness, moat/optionality) |

**GATE 0: PASS.** No part missing or empty.

---

## AUDIT 1 — COVERAGE (fresh grep pass, diffed against BOTH ledgers)

Independent grep counts vs the A2 ledgers:

| Category | Doc | A2 count | My fresh count | Orphan rows | Status |
|----------|-----|----------|----------------|-------------|--------|
| slides (`^\[page N\]$`) | pres | 24 | 24 | none | MATCH |
| line_items (P&L 18 + FY hist 7) | pres | 25 | 25 | none | MATCH |
| footnotes | pres | 9 | 9 (Note x3 L455/488/523; **/*** clusters L310/312/314/354/356/407-409) | none | MATCH |
| slide_numbers | pres | 118 | 118 (accepted; incl. flagged garbled/OCR-noise rows, none dropped) | none | MATCH |
| agenda_items | results | 13 | 13 (items 1-13, pages 1-2) | none | MATCH |
| notes | results | 8 (6 markers 1,2,4,6,7,8 + 2 orphan frags) | 8 (L519-557) | none | MATCH |
| line_items (P&L+recon+complaints) | results | 98 | 98 (row-by-row; glyph-spaced pages defeat grep, manual per A2) | none | MATCH |
| zero_standing | results | 25 | 25 | none | MATCH |
| auditor_paras | results | 14 (SA 6 + Cons 8) | 14 | none | MATCH |
| entities | results | 3 (L341-343; Nuo Zhan, Macfos Electronics, Parent) | 3 | none | MATCH |
| signature_blocks | results | 6 | 6 | none | MATCH |
| director_profiles | results | 1 | 1 (L646-666) | none | MATCH |

No orphan rows (ledger row absent from A4) and no rows my pass found that a ledger lacks. A4's preamble (L15-19) blanket-states "All rows reviewed at their cited line numbers," and every material flag traces into the review body:

- Results flags → coverage confirmed: NOTE_NUMBER_GAP→F14-01 (L48); UNAUDITED_ENTITY Nuo Zhan→F3-01; SHAREHOLDING_CONCENTRATION 23.04%→Q7/F13-01; COMPARATIVES_UNREVIEWED→F7-01; ZERO_STANDING/EXTRACTION_ARTIFACT/OCR_NOISE→mechanical, immaterial, correctly not a finding.
- Pres flags → coverage confirmed: EXPECTED_DISCLOSURE_ABSENT x3→F16-02/03/04; LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME→F16-01; NUMBER_DISCREPANCY_MINOR (18% vs 17.15%)→F14-01; INTERNAL_INCONSISTENCY (256 vs 257.68)→F14-01; SOURCE_TYPO / asterisk / footnote→F14-01 governance-hygiene; CHART_OCR_AMBIGUOUS→handled via ND / period-pairing caveats.

**Deliverable sub-check (task-specified): every A3 forward-signal/ambiguous finding from BOTH forensics → ≥1 Questions-for-Management row.** Re-derived against the Step 8.5 `from_finding` column (L442-454):

| Finding | QfM row | Covered |
|---------|---------|---------|
| F11-01, F16-05 | Q1 | yes |
| F3-01, F16-04 | Q2 | yes |
| F12-01, F16-02, F16-03 | Q3 | yes |
| F15-01, F16-06 | Q4 | yes |
| F13-02 | Q5 | yes |
| F6-01 (results), F6-01 (pres) | Q6 | yes |
| F13-01 | Q7 | yes |
| F16-08 | Q8 | yes |
| F16-07 | Q9 | yes |
| F16-01 | Q10 | yes |
| F16-09 | Q11 | yes |

Every enumerated forward/ambiguous finding from both documents maps to at least one question. **COVERAGE: PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs; standalone unless noted)

Raw inputs used (extract_results, Lakhs): Q1FY26 Rev 5926.80 / OI 60.54 / PBT 671.27 / Tax 174.50 / PAT 496.77 / Fin 56.05 / D&A 75.02; Q4FY26 Rev 10211.12 / OI 79.45 / PBT 1333.52 / Tax 336.95 / PAT 996.56 / Fin 117.19 / D&A 89.92; Q1FY27 Rev 8133.87 / OI 112.04 / PBT 792.13 / Tax 210.18 / PAT 581.95 / Fin 100.40 / D&A 83.09; FY26 Rev 30874.84 / OI 305.05 / PBT 3435.52 / Tax 874.55 / PAT 2560.97 / Fin 361.72 / D&A 325.13.

### 2A. Every derived-metric TABLE recomputes clean

| Metric (period) | A4 value | My recompute | Source | Status |
|-----------------|----------|--------------|--------|--------|
| Operating EBITDA (PBT+D+Fin−OI), all 4 cols | 7.4180 / 14.6118 / 8.6358 / 38.1732 | 741.80 / 1461.18 / 863.58 / 3817.32 L | extract L226-256 | MATCH |
| Op EBITDA margin /Rev | 12.52 / 14.31 / 10.62 / 12.36% | 12.516 / 14.31 / 10.617 / 12.364% | — | MATCH |
| Reported EBITDA (PBT+D+Fin) | 8.0234 / 15.4063 / 9.7562 / 41.2237 | 802.34 / 1540.63 / 975.62 / 4122.37 L | — | MATCH |
| Effective Tax Rate (Tax/PBT) | 25.99 / 25.27 / 26.53 / 25.46% | 25.995 / 25.27 / 26.534 / 25.456% | — | MATCH |
| PAT margin /Rev | 8.38 / 9.76 / 7.16 / 8.29% | 8.382 / 9.76 / 7.155 / 8.294% | — | MATCH |
| Gross Profit (Rev−CoM−Purch−ΔInv) | 14.2461 / 24.6317 / 19.4352 / 71.6494 | 1424.61 / 2463.17 / 1943.52 / 7164.94 L | L233-235 | MATCH |
| Gross Margin | 24.04 / 24.12 / 23.89 / 23.21% | 24.036 / 24.122 / 23.894 / 23.207% | — | MATCH |
| Core PBT ex-OI (PBT−OI) | 6.1073 / 12.5407 / 6.8009 / 31.3047 | 610.73 / 1254.07 / 680.09 / 3130.47 L | — | MATCH |
| OI/PBT | 9.02 / 5.96 / 14.14 / 8.88% | 9.02 / 5.958 / 14.144 / 8.879% | — | MATCH |
| Revenue YoY | +37.24% | +37.238% | — | MATCH |
| Op EBITDA YoY | +16.42% | +16.416% | — | MATCH |
| Finance cost YoY | +79.13% | +79.13% | — | MATCH |
| Other Income YoY | +85.07% | +85.07% | — | MATCH |
| Core PBT ex-OI YoY | +11.36% | +11.357% | — | MATCH |
| Reported PBT YoY | +18.00% | +18.006% | — | MATCH |
| PAT YoY | +17.15% | +17.147% | — | MATCH |
| EPS YoY (5.62/4.80) | +17.08% | +17.08% | L274 | MATCH |
| QoQ Rev (Q1FY27/Q4FY26) | −20.3% | −20.34% | — | MATCH |
| Rev growth on Total Income | 37.72% | 37.72% | L230 | MATCH |
| Reported EBITDA YoY on TI basis | +21.59/21.60% | 21.596% | — | MATCH |
| EBITDA margin /TI Q1FY27 | 11.83% | 975.62/8245.91=11.831% | — | MATCH |
| PAT margin /TI Q1FY27 | 7.06% | 581.95/8245.91=7.057% | — | MATCH |
| **PAT BRIDGE** (8 components) | ties to +0.8518 | 5.3058/−0.1167/−1.1370/−2.8344/−0.0807/−0.4435/+0.5150/−0.3568 sum **+0.8517≈+0.8518** | Step 4 | **MATCH (ties exactly)** |
| S−C PAT gap % (4 periods) | −0.136 / +0.147 / −0.125 / −0.036% | −0.1358 / +0.1465 / −0.1248 / −0.0355% | L256/L467 | MATCH |
| Consol Op EBITDA / ETR / PAT-margin Q1FY27 | 8.6328 / 26.57 / 7.15% | 863.28 L / 26.567 / 7.145% | L431-467 | MATCH |
| Annexure I Ind AS diff FY26 SA / Cons | −20.39 / −20.42 | −20.39 / −20.42 | L584/L617 | MATCH |
| Bonus/paid-up (941.68→1035.85) | +94.17 | 941,682×Rs10=94.17 L | L541/L270 | MATCH |

### 2B. Step-4 operational-decomposition prose — RESOLVED at loop-1

The two figures flagged FAIL at loop-0 have been corrected by A4 and now recompute clean and agree with the tying PAT bridge:

| Metric | A4 value (loop-1, L242-243) | My re-derivation | Status |
|--------|------------------------------|------------------|--------|
| Core-operations pre-tax contribution to PAT change | **+0.6936 Cr** (was +0.6102) | core PBT ex-OI 6.8009 − 6.1073 = **0.6936** (= reported PBT change 1.2086 − OI change 0.5150) | **FIXED — MATCH** |
| Ex-OI sensitivity (OI reverts to prior 0.6054) | **≈5.44 Cr → ~+9.5% YoY** (was 5.086 / +2.4%) | PBT 7.9213 − 0.5150 = 7.4063 Cr; ×(1−0.2653) = **5.4415 Cr**; 5.4415/4.9677 − 1 = **+9.54%** | **FIXED — MATCH** |

Consistency re-check: the corrected +9.5% ex-OI growth now agrees with A4's own PAT bridge (Other Income = 0.5150 of the 0.8518 increase; after-tax OI effect 0.3784 ⇒ residual PAT growth 0.4734/4.9677 = +9.5%). No new internal inconsistency introduced. The surrounding narrative ("Other Income still doing meaningful lifting; ex-OI growth ~9.5% well below the headline +17.15%") is now internally coherent and the qualitative read is unchanged.

Regression scan: coordinator confirms every other cell/monitor/question/verdict/brief line and the closing YAML are byte-for-byte identical to the loop-0 review; spot re-verification of L242-243 confirms the edit is confined to exactly the two flagged figures (PBT stated in Cr as 7.9213, ETR 26.53%, prior PAT 4.9677 all correct). No downstream monitor (ROCE LIT, slow-moving LIT, PAT-margin AMBER, CFO/PAT UNKNOWN), no verdict (PROCEED WITH CAVEATS), no decision (WATCHLIST / 8A-W), and no brief line depends on the two edited figures, so nothing regressed.

### 2C. Deck-quirk not surfaced by A4 (informational, not an A4 error — unchanged)

Deck slide-14 FY25-26 EBITDA prints 4,106.13 L (pres L437) vs raw-derived reported EBITDA 4,122.37 L (Q1 bars 802.34 / 975.62 tie exactly). A4 correctly used its own raw-derived figure; the deck's own FY26 bar is internally inconsistent and left un-noted. Minor; not a gate failure.

**ARITHMETIC: PASS.** All tables tie; both loop-0 failures corrected and re-verified.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear counter from the SAME extract)

**Claim 1 — "Revenue +37.24% YoY, GREEN, acceleration above FY26 ~21%" (L177, L192).**
Bear from extract: (a) Q1FY26 comparative is management-converted, NOT limited-reviewed (results L183-189; pres L455); (b) deck's own FY revenue history (pres L238) shows YoY growth DECELERATING multi-year (+56%→+104%→+21%), so a single seasonal-low Q1 at +37% is not "acceleration"; (c) op EBITDA only +16.42%, ~60% of PAT growth is OI.
Survives? **Partially — already incorporated.** A4 flags the unreviewed comparative (F7-01), single-quarter/seasonal caveat (L219), OI-flattering (Step 4). Multi-year-deceleration nuance does not overturn GREEN; not material enough to graft.

**Claim 2 — "Deck ROCE 27.42–31.08% healthy; de-risks the ROCE thesis-break trigger" (L271, L342, L370, L397).**
Bear from extract: mgmt-computed, unaudited, OCR-ambiguous period pairing with a garbled third bar (5.59%, pres L261); RoNW simultaneously DECLINED 6.88→5.94% (pres L477-478); no cash statement, so ROCE cannot lift the cap.
Survives? **No (fully incorporated).** A4 caveats mgmt-computed/period-ambiguous, refuses Pillar-1 re-rate (L397), holds ROCE does NOT lift the cap (L279).

**Claim 3 — "AOV +30.81% = first hard corroboration of B2B/corporate-deepening mix thesis" (L149, L498).**
Bear from extract: (a) SKU growth is "primarily… small and low-cost items" (pres L356-358), in tension with a bigger-basket corporate story; (b) gross margin FLAT ~24% (L199) → no visible mix uplift; (c) orders-per-customer fell 7.1% and the split is withheld (single-segment, F12-01), so AOV could be price/unit-cost, not corporate mix.
Survives? **No (already hedged).** A4 states "consistent with, though NOT proof of" (L149), flags flat gross margin as no Robu-2.0 uplift (L199), keeps B2B share UNKNOWN.

**Adversarial verdict: NO new surviving bear counter requiring insertion.** All three strongest counters already grafted.

---

## VERDICT

**COMPLETE.** Proceeds to Notion save.

- GATE 0 (deliverable brief, 4 parts): PASS.
- COVERAGE (both ledgers, both forensics' forward/ambiguous → QfM): PASS, zero orphans.
- ARITHMETIC: PASS — all mandated tables tie; the two loop-0 Step-4 failures are corrected and re-verified (core pre-tax +0.6936 Cr; ex-OI PAT ≈5.44 Cr / +9.5%), now consistent with the tying PAT bridge; no regression elsewhere.
- ADVERSARIAL: no new surviving bear counter.

No gap remains.

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
