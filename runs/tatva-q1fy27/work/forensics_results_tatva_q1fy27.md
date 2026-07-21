# A3 FORENSIC NOTES — TATVA CHINTAN PHARMA CHEM (TATVA) — Q1 FY27 — doctype: RESULTS

Source A1 extract: `runs/tatva-q1fy27/work/extract_results_tatva_q1fy27.txt` (563 lines, unit convention Rs Millions; x0.1 = Rs Cr)
Reconciliation contract (A2 ledger): `runs/tatva-q1fy27/work/ledger_results_tatva_q1fy27.md`
Ledger reconciliation: 13 notes + 65 line items + 6 zero-standing + 6 agenda + 12 annexure rows + 10 auditor paras + 3 entities + 5 signature blocks — ALL read verbatim at cited lines. **100% reconciled.**
Prior-quarter extract: none (first run under this pipeline). F5 EoM and F15 entity diffs assessed on current-quarter language only, marked accordingly.

All Rs values below are as-reported (millions) unless " Cr" is stated.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-a | F1 | Consol Sr6 / Std Sr6 exceptional items | 301, 499 | "Exceptional items ... 13.18" | AMBIGUOUS | A line that was zero-standing in Q4FY26/Q1FY26/FY26 fired at 13.18 (Rs 1.318 Cr) this quarter, identical in consol and standalone (so it originates at parent), with NO explanatory note anywhere. Charge (PBT before 224.29 less 13.18 = 211.11). Nature unknown -> A4 question. |
| F1-b | F1 | Std "Purchases of stock-in-trade" ZERO_STANDING | 490 vs 291 | "Purchases of stock-in-trade" (standalone nil; consolidated 14.03 / 22.43 / 12.89 / 64.94) | NEUTRAL-FACT | Resale/trading occurs only at group level via the two foreign WOS, never at the parent — confirms the subsidiaries are the distribution arms. Ties to F2/F3. |
| F2-a | F2 | Consol Sr9 307 / Std Sr9 505; attributable 322 | 307, 505, 322 | "Profit for the period/year (7-8) ... 159.81" (consol) vs "104.46" (standalone) | AMBIGUOUS | Subsidiary PAT contribution = 55.35 (34.6% of consol PAT). Gap as % of standalone PAT jumped 14.4% (Q4FY26) -> 53.0% (Q1FY27), a 38.6pp swing vs the 5pp FINDING threshold. Directly on Notion monitor #7 (parent profit share). Durability unknown -> A4. |
| F2-b | F2 | Consol Sr1 286 / Std Sr1 484 | 286, 484 | "Revenue from operations ... 1,670.55" (consol) vs "1,467.02" (standalone) | FORWARD-SIGNAL | Subsidiary external revenue = 203.53 (12.2% of consol) vs only 14.79 in Q4FY26 and 76.84 in Q1FY26. A step-change in exports routed through USA Inc / Europe B.V. — candidate SDA/semiconductor channel emerging (Notion monitor #3/#5). |
| F3-a | F3 | Cost lines consol vs standalone | 290/489, 294/493, 296/495 | "Cost of materials consumed 1,054.07" (consol) vs "1,054.06" (std); "Employee benefits expense 167.36" both; "Depreciation ... 105.66" vs "105.65" | AMBIGUOUS | Subsidiaries carry ~zero materials, zero incremental employee cost, ~zero depreciation, yet deliver 203.53 revenue and 55.35 PAT (27.2% net margin; ~40.6% EBITDA margin on their revenue). Non-operating distribution shells earning a large resale/transfer-pricing markup. Quality-of-earnings and durability -> A4. |
| F4-a | F4 | Consol auditor para 5 & 6 | 226-231, 246-251 | "The Statement includes the results of the following entities ... Tatva Chintan USA Inc. – Wholly Owned Subsidiary; Tatva Chintan Europe B.V. – Wholly Owned Subsidiary" | AMBIGUOUS | Two FOREIGN subsidiaries now supply 34.6% of consol PAT, yet the review report carries NO Other Matters paragraph and NO "based on unaudited financials certified by management / reviewed by other auditors" carve-out. The audit assurance status of a third of consol profit is undisclosed. Contribution >10% AND a YoY jump (7.1% FY26 -> 34.6%) = two F4 triggers -> A4. |
| F6-a | F6 | Board item 5 + Annexure 5B | 64-68, 179-182 | "The Board has approved the proposed capacity expansion (addition) ... at the new greenfield unit at Dahej - III" ; "344 kilolitres" ; "21 months (approximately)" ; "200 Crores (approximately)" ; "Combination of Internal Accruals and Debt" | FORWARD-SIGNAL | Dahej-III formally approved: 344 KL, Rs 200 Cr, ~21 months (implied ready ~Apr 2028). This is the Notion SHARED CATALYST (drives Pillar-1 ROCE and Pillar-3 growth) and monitor #5 (no 4th slip). Debt-financed in part -> leverage. |
| F6-b | F6 | Board item 6 | 71-74 | "increase in the borrowing limits ... from Rs. 300,00,00,000 ... to Rs. 1,000,00,00,000 ... subject to approval of the Members" | FORWARD-SIGNAL | Borrowing headroom raised 3.3x (Rs 300 Cr -> Rs 1,000 Cr). Finance cost already up 5x YoY (20.81 vs 4.13, line 295). Foreshadows material debt draw for Dahej-III; watch Notion monitor #6 (net debt/EBITDA <0.65x). |
| F8-a | F8 | Std current/deferred tax 502-504; consol 304-306 | 502, 503, 304 | "Current tax" (standalone Q1FY27 blank/nil; Q4FY26 25.70; FY26 100.67); "Deferred tax ... 36.48" | AMBIGUOUS | Standalone current tax is NIL this quarter while deferred tax charge is 36.48 (100% of the tax line). Consol current tax only 10.10 (down from 30.14 / 119.68) — the entire consol current tax is effectively the foreign subs. Near-zero cash tax at parent flatters cash flow (Notion monitor #1) but the deferred charge is future crystallising tax = ETR/cash-tax step-up risk. Why nil current tax -> A4. |
| F13-a | F13 | Board items 2/3/4 + Annexure 5A | 46-62, 119-131 | "re-appointment ... for a further period of three (3) years from 01 February 2027 to 31 January 2030" | FORWARD-SIGNAL | All three founder-promoter executives (MD Shah, WTDs Patel & Somani) locked in through 31-Jan-2030, straddling the Dahej-III commissioning window (~Apr 2028). Domain-expert continuity through the catalyst = governance positive. No independent-director non-renewal disclosed. |
| F13-b | F13 | Board items 2/3/4/6 | 49-50, 73-74 | "subject to approval of the Members at the ensuing Annual General Meeting" | FORWARD-SIGNAL | "Ensuing AGM" referenced 4x -> AGM notice + record date incoming, carrying special resolutions (Sec 180(1)(c) borrowing limit + three re-appointments). A capital-enabling resolution (3.3x borrowing) foreshadows a funding round; schedule the AGM-notice pull. No AGM date/record date/dividend disclosed in this filing. |
| F14-a | F14 | Annexure 5A director profiles | 139-142 | "He has over 31 years of experience" (Patel) vs "over 30 years" (Shah, Somani) — all three "joined the Company in the year 1996" | NEUTRAL-FACT | Patel's 31 years is internally inconsistent with a shared 1996 join year (30 years to 2026). Immaterial alone; a drafting-care data point. |
| F14-b | F14 | Annexure labelling | 110, 171 | "Annexure A" (director disclosure) and "Annexure A" (capacity disclosure) | NEUTRAL-FACT | Two physically distinct tables share one annexure letter; covering letter (line 78) cites a single "Annexure A" for items 2,3,4,5. Labelling oversight; cumulative governance-care note with F14-a. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING | **FINDING** | Exceptional-items line (zero-standing prior periods) fired 13.18 unexplained (301/499); standalone stock-in-trade nil vs consol live (490) = subs are the traders. NCI rows nil throughout (wholly-owned, structural); other-equity rows annual-only by convention. |
| F2 STANDALONE vs CONSOL DECOMP | **FINDING** | Subsidiary PAT share jumped to 34.6% of consol (gap = 53.0% of std PAT vs 14.4% in Q4FY26, >5pp threshold); subsidiary revenue leapt 14.79 -> 203.53 QoQ. |
| F3 SHELL-ENTITY DETECTION | **FINDING** | Subs have ~zero materials/employees/depreciation (identical to standalone) yet earn 55.35 PAT — non-operating distribution shells with a large resale markup; no going-concern EoM to reconcile. |
| F4 UNAUDITED CONTRIB RATIO | **FINDING** | 34.6% of consol PAT from two foreign WOS; no Other Matters para and no component-auditor / management-certified carve-out disclosed. >10% and YoY jump = two triggers. |
| F5 GOING CONCERN / EoM | **PASS** | No EoM or going-concern language in either review report (lines 246-251 consol, 438-444 std). No prior-quarter extract, QoQ diff N.A. this run; current language clean. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | Dahej-III (344 KL, Rs 200 Cr, 21 months, accruals+debt); borrowing limit Rs 300->1,000 Cr; three re-appointments; ensuing AGM. See commitment register. |
| F7 HEDGE PHRASE MINING | **PASS** | Only "subject to" appears, in the AGM-approval governance sense (49-50, 73-74), not as a risk hedge. No newly-added note hedge on revenue lumpiness or 61% customer concentration despite the exposure. |
| F8 TAX FORENSICS | **FINDING** | Standalone current tax NIL Q1FY27 vs deferred charge 36.48; consol current tax 10.10 (foreign subs). Persistent deferred CHARGES (DTL build), near-zero parent cash tax = future ETR step-up risk. No "earlier years" adjustment line present. |
| F9 OCI FORENSICS | **PASS** | Actuarial (non-reclassifiable) line tiny (0.61 vs FY26 2.45). FX-translation (reclassifiable) flipped +12.59 -> (3.65), a 16.24 swing, below the full-prior-year 30.46 threshold. OCI totals partly OCR-garbled (315-317) but reconstruct from TCI-PAT = (3.19); no threshold breach. |
| F10 SHARE COUNT / DILUTION | **PASS** | Paid-up capital 233.92 flat across all periods, both statements (341/520) — no corporate action. Basic = Diluted EPS in every period (6.83/6.83; 4.47/4.47) — zero dilutive overhang; no warrants/ESOP spread. |
| F11 RESERVES / NET WORTH TIE-OUT | **PASS** | Consol NW FY26 = 7,583.67 + 233.92 = 7,817.59 (Rs 781.76 Cr); std = 7,348.37 + 233.92 = 7,582.29. Consol exceeds std by 235.30 (~3%, subs reserves + FX). No in-document third-party number to reconcile; quarterly other-equity columns blank so no Q1 NW. No >5% gap detectable. |
| F12 SEGMENT FORENSICS | **N.A.** | Single reportable segment "specialty chemicals" (note 4, lines 373/552) -> no segment asset/liability disclosure exists to trend. Note: single-segment reporting masks SDA vs pharma vs PTC mix (Notion monitor #3). |
| F13 BOARD OUTCOME BEYOND RESULTS | **FINDING** | Three promoter execs re-appointed through 31-Jan-2030 across the Dahej-III window; ensuing AGM with special resolutions (borrowing 3.3x). Capital-enabling resolution + Role 6 AGM-notice event flagged. |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | Patel "31 years" vs peers "30 years" same 1996 join year (139-142); two tables both headed "Annexure A" (110, 171). Individually immaterial, cumulatively a governance-care point. |
| F15 ENTITY LIST DIFFS | **N.A.** | No prior-quarter extract, diff N.A. this run. Current list (Holding + Tatva Chintan USA Inc. WOS + Tatva Chintan Europe B.V. WOS, lines 228-230) internally consistent with director-profile affiliations. |
| F16 PRESENTATION-SPECIFIC | **N.A.** | Doctype = results (no presentation deck). |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Doctype = results (no transcript). Notion monitor items carried forward for the concall/A4 run: cash conversion/receivable days, ROCE 8%, SDA revenue mix, EBITDA margin, Dahej-III/semiconductor dispatch, credit rating, standalone PBT/parent share, peer demand tone. |

Scorecard: 8 FINDING / 5 PASS / 4 N.A. = 17 marked, no blanks. **GATE A3 = PASS.**

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/item ref | status word |
|---|---|---|---|
| Dahej-III greenfield capacity: 344 KL reactor capacity | ~Apr 2028 (21 months from 17-Jul-2026 approval) | Board item 5 (64-68); Annexure 5B (179-182) | board has approved / initiated |
| Dahej-III investment Rs 200 Cr, financed by internal accruals + debt | over the 21-month build | Annexure 5B (181-182) | proposes to |
| Increase borrowing limit Sec 180(1)(c) Rs 300 Cr -> Rs 1,000 Cr | at ensuing AGM | Board item 6 (71-74) | board has approved, subject to member approval |
| Re-appoint MD Chintan N. Shah, 3 yrs | 01-Feb-2027 to 31-Jan-2030 | Board item 2 (46-50) | board has approved, subject to member approval |
| Re-appoint WTD Ajaykumar M. Patel, 3 yrs | 01-Feb-2027 to 31-Jan-2030 | Board item 3 (52-56) | board has approved, subject to member approval |
| Re-appoint WTD Shekhar R. Somani, 3 yrs | 01-Feb-2027 to 31-Jan-2030 | Board item 4 (58-62) | board has approved, subject to member approval |
| Ensuing AGM (record date, notice, special resolutions) | FY27, date not yet disclosed | items 2,3,4,6 (49-50, 73-74) | subject to / upcoming |
| Results + reports available on BSE/NSE/company website | immediate | note 6 consol (386-388) / note 5 std (556-557) | shall be |

Note: no AGM date, record date, dividend, ESOP grant, scrutinizer, or auditor-change item is present in this filing (confirmed absent, not merely unlisted). No AR/Board's-Report approval here (Q1 results), so no Role 6 AR Deep Dive trigger yet; the ensuing-AGM references warrant an AGM-notice watch event.

---

## FLAGGED FOR A4 (convert to management questions)

FORWARD-SIGNAL: F2-b, F6-a, F6-b, F13-a, F13-b
AMBIGUOUS (lean-bear, resolve via question): F1-a, F2-a, F3-a, F4-a, F8-a

Priority questions the decomposition raises (A4 to formalise):
1. What drove subsidiary revenue from 14.79 (Q4FY26) to 203.53 and subsidiary PAT to 55.35 (34.6% of consol) in one quarter — is this recurring SDA/semiconductor export demand or a one-off, and at what transfer price? (F2, F3)
2. Were the two foreign WOS figures reviewed by component auditors or management-certified, given no Other Matters carve-out? (F4)
3. Nature of the Rs 1.318 Cr exceptional charge (unexplained, first appearance)? (F1)
4. Why nil standalone current tax this quarter alongside a 36.48 deferred charge, and when does cash tax normalise? (F8)
5. Expected debt draw and peak net debt/EBITDA under the 3.3x borrowing headroom for Dahej-III? (F6)

---

```yaml
stage: A3-forensics
company: "TATVA"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/tatva-q1fy27/work/forensics_results_tatva_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-a", check: "F1", line: "301,499", classification: "AMBIGUOUS", implication: "Exceptional charge 13.18 fired this quarter, unexplained, identical consol/standalone"}
  - {id: "F1-b", check: "F1", line: "490", classification: "NEUTRAL-FACT", implication: "Standalone stock-in-trade nil vs consol live = foreign subs are the traders"}
  - {id: "F2-a", check: "F2", line: "307,505", classification: "AMBIGUOUS", implication: "Subsidiary PAT share jumped to 34.6% of consol; gap 53.0% of std PAT vs 14.4% Q4, >5pp"}
  - {id: "F2-b", check: "F2", line: "286,484", classification: "FORWARD-SIGNAL", implication: "Subsidiary revenue leapt 14.79 to 203.53 QoQ; export channel emerging"}
  - {id: "F3-a", check: "F3", line: "290,294,296", classification: "AMBIGUOUS", implication: "Subs have ~zero materials/employees/depreciation yet 27% net margin = distribution shells, QoE question"}
  - {id: "F4-a", check: "F4", line: "226,246", classification: "AMBIGUOUS", implication: "34.6% of consol PAT from foreign WOS with no Other Matters / audit-status carve-out"}
  - {id: "F6-a", check: "F6", line: "64,179", classification: "FORWARD-SIGNAL", implication: "Dahej-III approved 344 KL Rs 200 Cr 21 months; shared catalyst, ~Apr 2028"}
  - {id: "F6-b", check: "F6", line: "71", classification: "FORWARD-SIGNAL", implication: "Borrowing limit 3.3x to Rs 1,000 Cr; leverage for capex, watch net debt/EBITDA"}
  - {id: "F8-a", check: "F8", line: "502,304", classification: "AMBIGUOUS", implication: "Nil standalone current tax vs 36.48 deferred charge; future cash-tax step-up risk"}
  - {id: "F13-a", check: "F13", line: "46,119", classification: "FORWARD-SIGNAL", implication: "Three promoter execs locked in to 31-Jan-2030 across Dahej-III commissioning window"}
  - {id: "F13-b", check: "F13", line: "49,73", classification: "FORWARD-SIGNAL", implication: "Ensuing AGM with special resolutions incl 3.3x borrowing; capital-enabling, AGM-notice watch"}
  - {id: "F14-a", check: "F14", line: "139", classification: "NEUTRAL-FACT", implication: "Patel 31 yrs vs peers 30 yrs same 1996 join year; drafting-care point"}
  - {id: "F14-b", check: "F14", line: "110,171", classification: "NEUTRAL-FACT", implication: "Two distinct tables both headed Annexure A; labelling oversight"}
forward_signals: ["F2-b", "F6-a", "F6-b", "F13-a", "F13-b"]
ambiguous: ["F1-a", "F2-a", "F3-a", "F4-a", "F8-a"]
commitments:
  - {commitment: "Dahej-III greenfield 344 KL reactor capacity", implied_date: "~Apr 2028 (21 months from 17-Jul-2026)", ref: "item 5 / Annexure 5B (64-68,179-182)", status_word: "board has approved / initiated"}
  - {commitment: "Dahej-III Rs 200 Cr, internal accruals + debt", implied_date: "over 21-month build", ref: "Annexure 5B (181-182)", status_word: "proposes to"}
  - {commitment: "Borrowing limit Rs 300 Cr to Rs 1,000 Cr", implied_date: "at ensuing AGM FY27", ref: "item 6 (71-74)", status_word: "board approved, subject to member approval"}
  - {commitment: "Re-appoint MD Chintan N. Shah 3 yrs", implied_date: "01-Feb-2027 to 31-Jan-2030", ref: "item 2 (46-50)", status_word: "board approved, subject to member approval"}
  - {commitment: "Re-appoint WTD Ajaykumar M. Patel 3 yrs", implied_date: "01-Feb-2027 to 31-Jan-2030", ref: "item 3 (52-56)", status_word: "board approved, subject to member approval"}
  - {commitment: "Re-appoint WTD Shekhar R. Somani 3 yrs", implied_date: "01-Feb-2027 to 31-Jan-2030", ref: "item 4 (58-62)", status_word: "board approved, subject to member approval"}
  - {commitment: "Ensuing AGM notice / record date / special resolutions", implied_date: "FY27, date not disclosed", ref: "items 2,3,4,6 (49-50,73-74)", status_word: "subject to / upcoming"}
gate_a3: pass
blank_checks: []
```
