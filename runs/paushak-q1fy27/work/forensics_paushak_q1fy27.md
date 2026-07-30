# A3 FORENSIC NOTES — Paushak Limited (PAUSHAK) — Q1 FY27 — Doctype: RESULTS

Source extract: `extract_results_paushak_q1fy27.txt` (4 pages, 235 lines, units Rs
lacs, x0.01 -> Rs Cr, ocr_pages none, coverage 100%).
Ledger: `ledger_results_paushak_q1fy27.md`. Rows read verbatim at cited lines: 40/40
categories (1 agenda + 26 line items + 5 notes + 5 auditor paras + 1 entity + 2
signature blocks). Ledger reconciliation: 100%.
Prior-quarter extract: NONE SUPPLIED. Verbatim EoM/entity/note diffs against the
prior quarter cannot be performed — flagged as a limitation on F5 and F15, not
reconstructed from memory.
Column map: 30.06.2026 = Q1FY27 (Unaudited) | 31.03.2026 = Q4FY26 (Audited) |
30.06.2025 = Q1FY26 (Unaudited) | 31.03.2026 (YE) = FY26 (Audited).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-a | F1 | Sec2 row 7B(i)/7B(ii); Other Income row 2 | 119, 90 | "B (i) Item that will be reclassified to profit or loss   -   (785)" | AMBIGUOUS | The reclassifiable-OCI standing line fired Rs (7.85) Cr in Q4FY26 and reverts to a dash in Q1FY27; it coincides with the Q4 Other Income spike (Rs 8.21 Cr -> Rs 3.15 Cr in Q1). Points to a one-off FVOCI instrument derecognition (candidate: Nirayu preference redemption) whose income and reclassification do not recur. A4 must establish the recurring Other-Income base (~Rs 3 Cr/qtr). |
| F4-a | F4 | Sec4 para 5 (Other Matter); Sec6 sig block 2 | 216-221, 224 | "reviewed by the predecessor auditor, whose limited review reports dated 31st July, 2025 expressed an unmodified opinion" | AMBIGUOUS | Not a JV/associate unaudited-contribution issue (single standalone entity, 0% unreviewed). The Other Matter instead discloses a statutory-auditor transition to CNK & Associates LLP; the Q1FY26 comparative rests on the predecessor's review. A4 question: reason and timing of the auditor change (rotation vs resignation). |
| F8-a | F8 | Sec2 rows 4, 5(a), 5(b) | 106, 109, 110 | "(a) Current Tax  249 ... (b) Deferred Tax  142" | FORWARD-SIGNAL | ETR Q1FY27 = 391/1,902 = 20.56% vs statutory 25.17% (~461 bps shield). FY26 current tax only Rs 3.50 Cr on PBT Rs 50.41 Cr (6.9%) with Rs 7.59 Cr deferred CHARGE = accelerated-depreciation timing differences building a DTL on recent capex. As the shield reverses, cash (current) tax steps up toward statutory. No "earlier-years" tax adjustment line present. |
| F13-a | F13 | Sec1 agenda row 1 (INTER_ALIA_UNITEMIZED) | 30-31 | "has inter alia approved the Unaudited Financial Results" | AMBIGUOUS | Board Outcome itemizes only the results yet uses "inter alia," while the thesis flags a live management change (COO Gosaliya exit 31-Mar-26; Jain Parkash WTD). A4 question: was any board item (e.g., WTD regularization) transacted this meeting but not itemized in this Reg 30 letter? |
| F17-a | F17 | Sec2 rows 1, 3(a), 3(b), 3(e), 3(d) | 89, 95, 96-98, 101, 100 | "Cost of Materials consumed  2,899 ... 1,086" | FORWARD-SIGNAL / CONFIRMATORY-NEGATIVE | Structural P&L step-change consistent with MPP-8 commissioning + RM inflation. Material cost % of revenue jumped 19.4% (Q1FY26) -> 34.7% (Q1FY27); gross margin compressed ~1,380 bps (82.4% -> 68.6%). Depreciation +107% (Rs 4.06 -> 8.42 Cr). Finance cost Rs 1.36 Cr in ONE quarter EXCEEDS the entire FY26 finance cost of Rs 1.11 Cr (debt-funded capex now live). Corroborates Notion items 1 (RM spike) and 4 (MPP-8). |
| F17-b | F17 | Sec2 rows 1, 4, 3(e), 3(d), 2 | 89, 106, 101, 100, 90 | "Revenue from Operations  8,355" | AMBIGUOUS | Add-back trigger: 3 of 5 conditions numerically met from the face of the filing — revenue Rs 83.55 Cr (>65), core Op PBT ~Rs 15.87 Cr (>13), operating EBITDA margin ~30.7% (>=28%). Conditions (b) utilization >50% and (e) named customer/contract are NOT disclosable in a bare Reg 33 filing, so the trigger does NOT fully fire. A4 must source utilization + named-customer evidence before any add-back. |

---

## CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | Basis |
|---|---|---|
| F1 ZERO-VALUE STANDING | FINDING | 3 ZERO_STANDING rows read (7B(i) L119, 7B(ii) L120-122, Other Equity L130). Other Equity blank is standard annual-only disclosure; the 7B reclassifiable-OCI line is a live signal — fired Rs (7.85) Cr in Q4FY26, dash now, tied to Other-Income one-off (F1-a). No exceptional-items/subsidiary-sale line exists in the template. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Single standalone entity, no consolidated column; no subsidiaries/JV/associate. Confirmed at L161-169 (auditor reviews one entity) and Sec5 ledger. No S-vs-C gap to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No subsidiaries; no consolidated cost lines to compare. Not applicable to a single-entity filing. |
| F4 UNAUDITED CONTRIBUTION | FINDING | Other Matter (L216-221) read: 0% of PAT rests on JV/associate/component numbers (none exist). The Other Matter instead reveals a statutory-auditor transition to CNK & Associates LLP (F4-a). |
| F5 GOING CONCERN / EoM SCOPE | PASS | No Going Concern or Emphasis-of-Matter paragraph anywhere (auditor conclusion L190-196 clean/unmodified; ledger Sec4 confirms none). LIMITATION: verbatim QoQ EoM diff not performable — no prior-quarter extract supplied. |
| F6 FORWARD-COMMITMENT MINING | PASS | Notes L137-145 swept for the full lexicon. Only administrative language present ("were reviewed", "has been restated", "are the balancing figures", "regrouped/rearranged"). No forward-dated management commitment. Commitment register empty. |
| F7 HEDGE PHRASE MINING | PASS | No "subject to", "no assurance", "evaluating", "exploring", "in discussions", "endeavour" in the notes. Bare Reg 33 filing; no pre-emptive hedge on revenue lumpiness or customer concentration. |
| F8 TAX FORENSICS | FINDING | Sub-statutory ETR 20.56% Q1FY27 (~461 bps shield); FY26 current tax 6.9% of PBT with Rs 7.59 Cr deferred charge building DTL — cash-tax step-up ahead (F8-a). No "earlier-years" tax-adjustment line (that sub-test passes). |
| F9 OCI FORENSICS | PASS | Actuarial (non-reclassifiable 7A(i), L115) = Rs 0.02 Cr in Q1FY27, immaterial; no single-quarter swing exceeding prior year. Note: Q4FY26 7A(i) Rs (1.14) Cr exceeds FY26 full Rs (1.03) Cr, but that is a prior period and FY25 comparatives are unavailable to test — carried as a limitation, not a current-quarter finding. |
| F10 SHARE COUNT / DILUTION | PASS | Paid-up stable at Rs 12.33 Cr across recent quarters (L127); Q1FY26 Rs 3.08 Cr is the pre-subdivision/bonus base per Note 3 (L140-141, corporate action disclosed and traced). Basic & Diluted EPS identical at Rs 6.13 (L133) — zero spread, no dilutive instruments. |
| F11 RESERVES / NET WORTH | PASS | Net worth 31.03.2026 = Other Equity 38,363 + paid-up 1,233 = 39,596 lakh (Rs 395.96 Cr), internally consistent. No third-party figure (rating/slide) in the filing to test a 5% gap. Quarter-end Other Equity not disclosed (standard). |
| F12 SEGMENT FORENSICS | N.A. | Single reportable segment (Speciality Chemicals) per Note 2 (L139). No segment assets/liabilities table to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Only the results were itemized; no AR/AGM/dividend/director/capital-raise item. "inter alia approved" with nothing else itemized while a management change is live in the thesis (F13-a). 35-minute meeting (3:30-4:05, L37-38) consistent with results-only. |
| F14 NOTE DRAFTING INCONSISTENCIES | PASS | No genuine note-vs-letter contradiction: Note 1 says "reviewed" (not audited), consistent with the limited review. Q1FY26 paid-up shown at old base (308) while its EPS is restated (4.88) is CORRECT Ind AS 33 treatment (EPS restated retrospectively for bonus/split; face-of-statement capital is not), not an inconsistency. OCR artifacts ("3Qth June", "5327 42") are extraction-side, not filing-side. |
| F15 ENTITY LIST DIFFS | N.A. | Standalone single-entity filing; no consolidation list to diff. LIMITATION: prior-quarter extract unavailable, so an ENTITY_CHANGE cross-check could not be run regardless. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is a results filing, not an investor presentation. |
| F17 SILENCE / EXPECTATION AUDIT | FINDING | Task directs a monitoring-checklist expectation audit ("whether the filing addresses it"). The face numbers corroborate the RM/gross-margin headwind (item 1) and MPP-8 go-live (item 4) — F17-a — and partially fire the add-back trigger (F17-b). Narrative catalysts (exports, utilization, governance, holdings, China+1) are structurally absent from a bare Reg 33 filing; cross-reference below carries them to A4. No concall transcript exists, so the classic per-turn silence audit is not run. |

Scorecard tally: FINDING x6 (F1, F4, F8, F13, F17-two findings), PASS x6 (F5, F6, F7,
F9, F10, F11, F14 = 7), N.A. x5 (F2, F3, F12, F15, F16). Every check carries exactly
one status. GATE A3: pass (no blanks).

---

## COMMITMENT REGISTER (from F6)

None. The Notes (L137-145) contain no forward-dated management commitment; every note
is administrative (statutory review, EPS restatement, Q4 balancing-figure derivation,
regrouping). No "expected to", "will be", "commenc", "underway", "proposes to",
"board has approved [a future action]", or "intends to" language present. Register empty.

---

## MONITORING CHECKLIST CROSS-REFERENCE (for A4)

| # | Thesis expectation | Filing addresses? | Evidence / line | Note |
|---|---|---|---|---|
| 1 | West Asia RM spike unabsorbed -> gross-margin headwind | YES — corroborated | L95, L89, L96-98 | Material cost % 19.4% -> 34.7% YoY; gross margin ~82.4% -> ~68.6% (~-1,380 bps). CONFIRMATORY-NEGATIVE (F17-a). |
| 2 | Add-back trigger (5 conditions) | PARTIAL — 3 of 5 met | L89, L106, L101, L100 | Rev Rs 83.55 Cr (>65) yes; core Op PBT ~Rs 15.87 Cr (>13) yes; op EBITDA margin ~30.7% (>=28%) yes; utilization and named-customer NOT disclosable in Reg 33 -> trigger not fully firing (F17-b). |
| 3 | Exports inflection sustaining | NO — silent (expected) | Note 2 L139 | Single reportable segment; no geography/export split in a Reg 33 filing. Carry to A4. |
| 4 | MPP-8 utilization ramp / new capex | INDIRECT | L101, L100 | Depreciation +107% YoY and finance cost > full FY26 signal the plant is capitalised, depreciating and debt-funded. No utilization figure disclosed. |
| 5 | Other Income quality / RPT | YES — normalized | L90, L119 | Other Income Rs 8.21 Cr (Q4) -> Rs 3.15 Cr (Q1); paired OCI reclassification Rs (7.85) Cr in Q4 -> dash. One-off (Nirayu-type) redemption did not recur (F1-a). No RPT line disclosed this quarter. |
| 6 | Governance / management-change item | NO — silent | L27-32 | Board Outcome itemizes only the results; "inter alia" unitemized (F13-a). |
| 7 | Institutional holding trend | NO — N/A to doctype | — | Shareholding pattern is a separate filing; not in this results release. |
| 8 | China+1 named-contract narrative (dropped tracker) | Silent (expected) | — | Confirmed silent; consistent with dropped-tracker status. |

Consecutive-quarter silence counts cannot be tallied — no prior-quarter extract in
this run folder (limitation).

---

## LIMITATIONS

- No prior-quarter extract: F5 EoM verbatim diff, F15 entity diff, F9 Q4-swing test
  vs FY25, and F17 silence-streak counts are all limited by this absence. Noted, not
  reconstructed.
- Signatory names on both signature blocks not resolved in extracted text
  (image signatures; SIGNATORY_NAME_NOT_FOUND per ledger Sec6) — not a mechanical
  failure.

```yaml
stage: A3-forensics
company: "PAUSHAK"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/paushak-q1fy27/work/forensics_paushak_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: FINDING
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: PASS
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F1-a", check: "F1", line: "119", classification: "AMBIGUOUS", implication: "Reclassifiable-OCI line fired Rs(7.85)Cr in Q4FY26, dash now; tied to Q4 Other Income Rs8.21Cr->Rs3.15Cr one-off (Nirayu-type FVOCI redemption). Establish recurring Other-Income base."}
  - {id: "F4-a", check: "F4", line: "216-221", classification: "AMBIGUOUS", implication: "Other Matter reveals statutory-auditor transition to CNK & Associates LLP; Q1FY26 comparative rests on predecessor review. Confirm reason/timing (rotation vs resignation)."}
  - {id: "F8-a", check: "F8", line: "106", classification: "FORWARD-SIGNAL", implication: "ETR 20.56% vs 25.17% (~461 bps shield); FY26 current tax 6.9% of PBT with Rs7.59Cr deferred charge building DTL on capex depreciation. Cash-tax step-up ahead."}
  - {id: "F13-a", check: "F13", line: "30-31", classification: "AMBIGUOUS", implication: "'inter alia approved' with only results itemized while a management change (COO exit / WTD appointment) is live in the thesis. Check for undisclosed board business."}
  - {id: "F17-a", check: "F17", line: "95", classification: "FORWARD-SIGNAL", implication: "Material cost % 19.4%->34.7% YoY, gross margin ~-1,380bps; depreciation +107%; finance cost Rs1.36Cr > full FY26 Rs1.11Cr. MPP-8 commissioning + RM inflation reshape the P&L. Corroborates Notion items 1 and 4."}
  - {id: "F17-b", check: "F17", line: "89", classification: "AMBIGUOUS", implication: "Add-back trigger 3/5 met on the face (rev Rs83.55Cr, core Op PBT ~Rs15.87Cr, EBITDA margin ~30.7%); utilization and named-customer undisclosed in Reg 33 -> trigger not fully firing. A4 must source both before any add-back."}
forward_signals: ["F8-a", "F17-a"]
ambiguous: ["F1-a", "F4-a", "F13-a", "F17-b"]
commitments: []
gate_a3: pass
blank_checks: []
```
