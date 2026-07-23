# A5 ADVERSARY / COMPLETENESS AUDIT — SONACOMS Q1 FY27 (RE-AUDIT)

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-23
Review under audit: `review_sona_q1fy27.md` (UPDATED A4 review)
Fresh context: re-derived independently from the three A1 extracts and three A2 ledgers; A4/A3 cites checked, not trusted.

**Re-audit scope:** Prior A5 pass returned INCOMPLETE on two gaps: (1) missing FX-neutral qualifier in the earnings-quality conclusion; (2) orphan coverage row — press-release stale "April 30, 2026" dateline (extract L64) absent from A4. This pass runs all three audits fresh and confirms closure of both without re-litigating settled items.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledgers)

Fresh grep/sweep counts re-derived from each extract, diffed against each A2 ledger count test.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| **Results — notes** | 14 | 14 (7 SA L235-286 + 7 C L534-583) | none | PASS |
| **Results — line items** | 65 | 65 (29 SA + 36 C) | none | PASS |
| **Results — zero-standing** | 8 | 8 (4 SA + 4 C: exceptional, prior-yr tax, OCI-tax, reserves) | none | PASS |
| **Results — agenda items** | 1 | 1 (board approval of results, L28-31) | none | PASS |
| **Results — auditor paras** | 9 | 9 (4 SA + 5 C; Other-Matters para 5 cited at review L64) | none | PASS |
| **Results — consolidation entities** | 17 | 17 (1 holding + 16 subs, Annexure 1 L427-447) | none | PASS |
| **Results — signature blocks** | 5 | 5 (Gupta 16:08:22; Tandon SA 14:40:58; Tandon C 14:11:24; SA results signatory OCR-gap; MD Vivek Vikram Singh) | none | PASS |
| **Presentation — slides** | 41 | 41 (page markers 1-41, sequential, no gaps) | none | PASS |
| **Presentation — numbers** | 365 | 365 (count-test methodology verified) | none | PASS |
| **Presentation — footnotes** | 27 | 27 | none | PASS |
| **Presentation — entities** | 39 | 39 | none | PASS |
| **Presentation — guidance statements** | 8 | 8 | none | PASS |
| **Press release — headline claims** | 4 | 4 (H1-H4, L56-60) | none | PASS |
| **Press release — financial figures** | 5 | 5 (F1-F5, L70-75) | none | PASS |
| **Press release — management quotes** | 1 | 1 (Q1, L80-91) | none | PASS |
| **Press release — operational highlights** | 2 | 2 (O1-O2) | none | PASS |
| **Press release — order-book entries** | 3 | 3 (B1-B3, L119-128) | none | PASS |
| **Press release — named entities** | 16 | 16 | none | PASS |
| **Press release — forward-looking** | 3 | 3 | none | PASS |
| **Press release — regulatory/admin** | 10 | 10 (incl. R1 dateline-mismatch note) | none | PASS |
| **Press release — signatories/contacts** | 3 | 3 | none | PASS |
| **Press release — footnotes** | 1 | 1 | none | PASS |
| **Press release — boilerplate** | 3 | 3 | none | PASS |
| **Press release — zero-standing** | 0 | 0 | none | PASS |

**Fresh-pass rows the ledger lacks:** none. My independent enumeration reproduces every A2 count exactly; no row surfaced that the ledger omits.

**Prior orphan (targeted re-check) — CLOSED.** The press-release "Gurgaon, India, April 30, 2026" dateline (extract L64; A2 press ledger DATE_MISMATCH / R1-note L155-161; A3 id PR-FD4) is now cited in the updated A4 review in three places: Step 8.5 Q10 (review L406, verbatim "press-release body dateline reads 'Gurgaon, India, April 30, 2026' (press-release extract L64)"), Section C governance cluster (review L465), and YAML flags (review L523). The A4 preamble (review L22) explicitly logs the graft. No longer an orphan.

**Coverage verdict: PASS — no orphan rows, no missing-from-ledger rows.**

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extract; results Rs mn x0.1)

Consolidated raw anchors (C L469-490, 506-507): Q1FY27 Rev 13,012.01 / forex 91.69 / OI 256.96 / PBET 2,409.42 / D&A 768.81 / FC 104.77 / tax 624.29 / PAT 1,785.13 / owners 1,804.68. Q1FY26 Rev 8,539.07 / forex (30.09) / OI 441.88 / PBET 1,744.13 / excep 91.74 / D&A 669.94 / FC 53.31 / tax 435.30 / PAT 1,217.09 / owners 1,247.13.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBET+D&A+FC−OI) | 302.60 | 240.94+76.88+10.48−25.70 = 302.60 | C L481/478/477/471 | MATCH |
| Op EBITDA Q1FY26 | 202.55 | 174.41+66.99+5.33−44.19 = 202.55 | C L481/478/477/471 | MATCH |
| Op EBITDA margin Q1FY27 (/rev ops) | 23.26% | 302.60/1301.20 = 23.26% | — | MATCH |
| Op EBITDA margin Q1FY26 | 23.72% | 202.55/853.91 = 23.72% | — | MATCH |
| Op EBITDA margin YoY | −46 bps | 23.26−23.72 = −0.46pp | — | MATCH |
| Op EBITDA YoY % | +49.40% | 100.05/202.55 = 49.40% | — | MATCH |
| Revenue YoY (rev ops) | +52.38% | 447.29/853.91 = 52.38% | C L469 | MATCH |
| Revenue incl forex YoY (deck basis) | +54.00% | (1310.37−850.90)/850.90 = 54.00% | C L469+470 | MATCH |
| Core PBT ex-OI Q1FY27 (PBET−OI) | 215.25 | 240.94−25.70 = 215.25 | C L481/471 | MATCH |
| Core PBT ex-OI Q1FY26 | 130.23 | 174.41−44.19 = 130.23 | C L481/471 | MATCH |
| Core PBT ex-OI YoY | +65.28% | 85.02/130.23 = 65.28% | — | MATCH |
| Net forex swing YoY | +Rs 12.18 Cr | 9.17−(−3.01) = 12.18 | C L470 | MATCH |
| Core PBT ex-OI ex-forex Q1FY27 | 206.08 | 240.94−25.70−9.17 = 206.077 → 206.08 | C L481/471/470 | MATCH (rounding) |
| Core PBT ex-OI ex-forex Q1FY26 | 133.24 | 174.41−44.19+3.01 = 133.234 → 133.23 | C L481/471/470 | MATCH (≤0.01 rounding) |
| Core PBT ex-forex YoY (~+55%) | +54.67% | 72.84/133.24 = 54.67% | — | MATCH |
| EBIT operating YoY | +66.51% | 90.16/135.56 = 66.51% | — | MATCH |
| D&A YoY | +14.76% | 9.887/66.994 = 14.76% | C L478 | MATCH |
| Finance costs YoY | +96.53% | 5.146/5.331 = 96.53% | C L477 | MATCH |
| Other Income YoY | −41.85% | −18.492/44.188 = −41.85% | C L471 | MATCH |
| ETR Q1FY27 (consol) | 25.91% | 62.43/240.94 = 25.91% | C L488/483 | MATCH |
| ETR Q1FY26 (consol) | 26.34% | 43.53/165.24 = 26.34% | C L488/483 | MATCH |
| PAT margin Q1FY27 (total/rev ops) | 13.72% | 178.51/1301.20 = 13.72% | C L490/469 | MATCH |
| PAT (owners) YoY | +44.71% | 55.76/124.71 = 44.71% | C L506 | MATCH |
| Reported PBT YoY | +45.82% | 75.70/165.24 = 45.82% | C L483 | MATCH |
| Reported PAT YoY change | +56.80 | 178.51−121.71 = 56.80 | C L490 | MATCH |
| Op EBITDA FY26 (consol) | 1,106.85 | 892.60+287.74+23.48−96.97 = 1106.85 | C L481/478/477/471 | MATCH |
| Std Op EBITDA Q1FY27 | 270.28 | 275.62+69.33+7.11−81.78 = 270.28 | SA L192/189/188/179 | MATCH |
| Std Op EBITDA margin Q1FY27 | 23.36% | 270.28/1157.24 = 23.36% | — | MATCH |
| Std ETR Q1FY27 (anomaly) | 20.14% | 55.52/275.62 = 20.14% | SA L200/194 | MATCH |
| Std OI/PBT Q1FY27 | 29.67% | 81.78/275.62 = 29.67% | SA L179/194 | MATCH |
| Std PAT margin Q1FY27 | 19.02% | 220.11/1157.24 = 19.02% | SA L202/177 | MATCH |
| S−C PAT gap Q1FY27 (/SA) | +18.90% | (220.11−178.51)/220.11 = 18.90% | SA L202 / C L490 | MATCH |
| S−C PAT gap Q1FY26 | −1.31% | (120.13−121.71)/120.13 = −1.31% | — | MATCH |
| S−C PAT gap Q4FY26 | +9.88% | (207.34−186.86)/207.34 = 9.88% | — | MATCH |
| S−C gap swing (Q1FY26→Q1FY27) | +20.2 pp | −1.31→18.90 = 20.21pp | — | MATCH |
| Revenue QoQ | +3.48% | (13012.01−12574.97)/12574.97 = 3.48% | C L469 | MATCH |
| Op EBITDA margin QoQ | −144 bps | 24.70%→23.26% = −144bps | — | MATCH |
| Core PBT ex-OI QoQ | −5.95% | (215.25−228.86)/228.86 = −5.95% | — | MATCH |
| Owners PAT QoQ | −5.97% | (180.47−191.92)/191.92 = −5.97% | C L506 | MATCH |
| Unreviewed-subs loss / consol PAT | −1.67% | 2.98/178.51 = 1.67% | C L490; auditor L373 | MATCH |
| Escorts consideration | 1,642.63 Cr | 16,426.32 mn x0.1 | SA L245 | MATCH |
| DENSO EV (49% stake) | 1,750 Cr | 17,500 mn x0.1 | SA L277 | MATCH |
| Intragroup dividend | 59.46 Cr | 594.63 mn x0.1 | SA L282 | MATCH |
| Paid-up QoQ increase | +Rs 1.88 mn | 6,220.35−6,218.47 = 1.88 mn (+188k sh) | SA L218 | MATCH |

**Arithmetic verdict: PASS — every derived metric reproduces within rounding (all discrepancies ≤ Rs 0.01 Cr, attributable to two-decimal presentation of raw mn/10). No mismatch above rounding.**

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest bear counter from the SAME extract)

**Positive claim 1 — "Core operating PBT ex-OI grew +65% YoY, faster than reported PAT (+45%); Other Income *fell*, so the print is operationally real, the opposite of treasury-flattered" (Step 2 diag 3; Section C).**
Bear counter (same text): the +65.28% retains the net-forex line, which swung +Rs 12.18 Cr YoY (−Rs 3.01 → +Rs 9.17 Cr, consolidated L470; deck L701 concedes forex sits inside revenue). Ex-forex, core PBT grows only ~+55% (54.67%), ~10 pp lower. Growth is also part-inorganic (full-quarter Escorts railway vs ~1 month in Q1FY26, Note 2) and margin-dilutive (−71 bps YoY).
**Survives? NO — already grafted.** A4 now nets the forex swing into the earnings-quality conclusion at diag 3 (review L194: "~+55%, ~10 pp lower"), Step 4B (L255), Section C (L457), and flags (L519). Inorganic/margin-dilutive cautions already present (diag 1, diag 2). No uncredited counter remains.

**Positive claim 2 — "Net cash ((1.06)x EBITDA), clean unmodified audit, no pledge; deleveraging corroborated by India Ratings facility cut Rs 925→725 Cr — balance-sheet strength intact" (Step 5; Section C).**
Bear counter (same text): consolidated finance costs doubled +96.53% YoY (L477); the deck discloses zero capex against four dated SOP commitments (P-A3-F17-01, CAPEX_NOT_DISCLOSED); no Q1 cash-flow statement, so CFO/PAT is untestable and cash conversion is INDETERMINATE; FY26 FCF/PAT was −0.61x (negative free cash per Notion). "Net cash" this quarter also coincides with the Rs 59.46 Cr intragroup dividend inflow (standalone), not demonstrated FCF.
**Survives? NO — already incorporated.** A4 flags capex silence, the INDETERMINATE cash cap (verdict capped at no better than PROCEED WITH CAVEATS), FCF/PAT −0.61x, and the finance-cost doubling (Step 5 L284-289; Step 2 diag 5; Section C L460). No uncredited counter remains.

**Positive claim 3 — "Revenue +52%/+54% YoY (highest ever), operating EBITDA +49%, owners PAT +45% — strong" (Step 2; Section C).**
Bear counter (same text): the growth is part-inorganic (railway full quarter vs ~1 month), the +54% headline is on the deck's forex-inclusive revenue basis (L470 forex embedded in the deck's "revenue"), single-segment reporting (Note 7) prevents isolating organic growth, and the print is margin-dilutive (−71 bps YoY, −144 bps QoQ, ~−160 bps vs FY26 24.7% baseline; tripwire 6).
**Survives? NO — already incorporated.** A4 states all four points explicitly (diag 1 inorganic + single-segment; diag 2 margin compression; Section C "part-inorganic... margin-dilutive"; deck-basis revenue labeled throughout). No uncredited counter remains.

**Adversarial verdict: PASS — no surviving bear counter. Every counter constructible from the extract is already grafted into A4; the FX-neutral counter that previously survived (~+55% core-PBT ex-forex vs +65% headline) is now netted into the quality conclusion, not left as a management question only.**

---

## VERDICT

**COMPLETE.** All three audits pass. Coverage: fresh enumeration reproduces every A2 count with zero orphan rows and zero missing-from-ledger rows; the prior orphan (press-release stale "April 30, 2026" dateline, extract L64 / PR-FD4) is now cited in A4 at Step 8.5 Q10, Section C, and the YAML flags. Arithmetic: every derived metric recomputes from raw within rounding (≤ Rs 0.01 Cr). Adversarial: no bear counter survives — the FX-neutral qualifier that previously survived (~+55% core-PBT ex-forex vs +65% headline) is now netted into the earnings-quality conclusion. Both prior gaps are closed; no new gap remains. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "SONACOMS"
quarter: "Q1 FY27"
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
