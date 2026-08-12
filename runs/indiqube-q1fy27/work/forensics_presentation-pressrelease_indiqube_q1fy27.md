# A3 FORENSIC NOTES — IndiQube Spaces Limited (INDIQUBE), Q1 FY27 — doctype: presentation (press release / Reg 30 filing)

Source: extract_presentation-pressrelease_indiqube_q1fy27.txt (176 lines, 4 pages).
Ledger: ledger_presentation-pressrelease_indiqube_q1fy27.md (18 categories, gate_a2 pass).
Prior-quarter extract: NONE (first pipeline run) — no verbatim EoM / entity / dropped-slide diff possible.
Ledger reconciliation: 100% — every row in ledger sections 1-16, all 16 reconciliation-table rows and 96 cells, read at cited line before judging. One ledger-vs-extract annotation discrepancy noted at F14-3 (does not reduce reconciled count).

Central forensic frame: management publishes a two-basis reconciliation. STATUTORY Ind AS = Revenue ₹423 Cr, net LOSS ₹(24) Cr (lines 118, 135; ties to results filing Rev ₹422.7 Cr, PAT ₹(23.9) Cr). The IGAAP-EQUIVALENT column (Revenue ₹428 Cr, PAT +₹35 Cr) is a MANAGEMENT-CONSTRUCTED bridge; every headline superlative ("Highest Ever Quarterly Revenue ₹428 Cr", "PAT Up 91% to ₹35 Cr") rests on that non-auditor-reviewed basis. Variance driver is Ind AS 116 (ROU depreciation ₹148 Cr line 130 + lease interest ₹116 Cr line 125).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------|----------------|---------------------|
| F4-1 | F4 | sec3 r1-4; sec11 r1,r16 | 55-56, 63, 118, 135 | "highest ever quarterly revenue of ₹428 crore" (63); "PAT Up 91% to ₹35 Cr" (56); table Ind AS PAT "(24)" (135) | AMBIGUOUS | 100% of the headline "profit" rests on a management-constructed IGAAP-equivalent bridge that is NOT auditor-reviewed; statutory Ind AS is a ₹24 Cr loss. A4 to ask whether the IGAAP-eq bridge is reviewed by the statutory auditor and which basis future guidance will use. |
| F6-1 | F6 | sec14 r1,r6 | 154, 158-159 | "will be held on Thursday, Aug 13, 2026, at 2:00 PM (IST)"; "presentation will be submitted to Stock Exchanges" | FORWARD-SIGNAL | Concall + Investor Presentation (Aug 13, 2026) is the pending venue where the 7 DROPPED Notion forward numerics could be restated; Management Grade-A "held pending" resolves there, one day after this release. |
| F6-2 | F6 | sec4-6, sec9 | 78-79, 88, 92, 96 | "contribution to operating revenue increasing from 11% to 17%"; "EBITDA Margin: 20%"; "PAT Margin: 8%"; "Increased by 1.91 Mn sq. ft. YoY" | FORWARD-SIGNAL | NONE of the 7 dropped FY27 numerics is restated as guidance. Some trailing actuals fall in-range (VAS 17%, AUM +1.91M sqft, PAT margin 8%, EBITDA margin 20%) but are presented as historicals, not reaffirmed guidance; solar 30-35MW/₹125-150Cr and fit-out ₹1,650/sqft are entirely ABSENT. Guidance-restatement test still open going into the call. |
| F7-1 | F7 | sec8 r1; sec12 r1 | 111-112, 137-138 | "primarily due to Ind AS accounting adjustments" (111); "arises mainly from non-cash accounting impacts, primarily on account of Ind AS 116" (137-138) | AMBIGUOUS | "mainly/primarily" leaves an unquantified residual: the bridge's Other income (₹18 Cr adj) and Other expenses (₹178 Cr adj, line 131) are not fully explained by ROU dep + lease interest alone. A4 to ask management to quantify every bridge component, not just the two Ind AS 116 bullets. |
| F7-2 | F7 | sec9 r1 | 110-111 | "estimated current tax expense of ₹8.14 Cr" | NEUTRAL-FACT | Hedge word "estimated" on the current-tax figure that anchors the IGAAP-eq PAT; a computed statutory current tax should not be an estimate. Minor pre-emptive cover. |
| F8-1 | F8 | sec11 r15; sec9 r1 | 134, 111 | table Tax expense IGAAP-eq "8" on PBT "43"; Ind AS Tax "(7)" on PBT "(30)" | NEUTRAL-FACT | IGAAP-eq ETR ≈ 18.6-18.9% vs statutory 25.17% (~630-660 bps shield); Ind AS books a tax CREDIT (7) on a pre-tax loss = deferred-tax-asset recognition. As IGAAP profits normalise, DTA drawdown implies future ETR step-up. Whole-crore rounding limits precision; verify at results filing. |
| F14-1 | F14 | sec11 r1,r14,r15,r16; sec3 r3 | 56, 118, 133-135 | headline "PAT Up 91%" (56); table "423 (6) 428" (118); "(24)" PAT (135); Q1FY26 IGAAP-eq PAT "19" (135) | AMBIGUOUS | Internal-arithmetic inconsistencies: Ind AS 423 -> IGAAP-eq 428 is +5 but the Ind AS Adj. cell shows (6); PBT (30) less tax credit (7) implies PAT (23) vs shown (24); headline +91% implies a base ~₹18.3 Cr, but the comparative table shows Q1FY26 IGAAP-eq PAT = ₹19 Cr, which yields only +84%. Rounding-driven but material to the headline; ask management for unrounded bridge and the exact PAT-growth base. |
| F14-2 | F14 | sec1 r11; sec16 r3; sec2 r1; sec15 r1 | 49, 59-60, 164, 174 | "vinfo@indiqube.com" (49) vs "cs.compliance@indiqube.com" (174); "Managed Spaces Platform" (59-60) vs "managed spaces platforms" (164) | NEUTRAL-FACT | Individually immaterial drafting inconsistencies (two IR emails, singular/plural platform, IndiQube/Indiqube casing). Cumulatively a low-severity governance/consistency data point on a young listed issuer's disclosure hygiene. |
| F14-3 | F14 | sec1 r7 | 30-32 | ledger row 7 records "quarter ended June 30, 2026 (restated)"; extract lines 30-32 read "...for the quarter ended June 30, 2026" | NEUTRAL-FACT | The word "restated" appears NOWHERE in the extract; the A2 ledger annotation "(restated)" is not verbatim-supported, and the press release discloses no restatement note or bridge. The Q1FY26 IGAAP-eq comparative (PAT ₹19 Cr) is presented as a plain comparative, not a labelled restatement. Do not treat prior-period figures as restated without the results filing. |
| F16-1 | F16 | sec4b r3-5 | 78-79 | "VAS revenue reaching ₹72 crore and its contribution to operating revenue increasing from 11% to 17%" | FORWARD-SIGNAL | VAS 17% crosses Notion GREEN tripwire #6 (VAS 15%+). Positive thesis signal. Note: ₹72 Cr / 17% is a QUOTE_ONLY_NUMBER (not restated as an operational bullet) — corroborate the ₹72 Cr and the 17% denominator basis (of operating revenue vs total) at the concall. |
| F16-2 | F16 | sec4b r1-2; sec6 r5 | 74-75, 104 | "Steady state occupancy strengthened to 90% and overall occupancy improved to 86%" | AMBIGUOUS | Notion checklist #1 is RPA-basis occupancy >83%. The labels here ("steady state" 90% / "overall" 86%) are a DIFFERENT basis; do not assume equivalence to RPA. A4 to ask management to reconcile steady-state/overall to the RPA occupancy definition before crediting checklist #1. |
| F16-3 | F16 | sec9 r2-3; sec5 r2 | 113, 88 | "EBITDA margin of 61% (₹258 Cr)" [Ind AS] (113) vs "EBITDA: ₹87 Cr ... EBITDA Margin: 20%" [IGAAP-eq] (88) | CONFIRMATORY-NEGATIVE | Basis cherry-picking: management touts the flattering Ind AS EBITDA margin (61%, inflated because Ind AS excludes rent from opex) AND the IGAAP-eq positive PAT (₹35 Cr) — selecting whichever basis flatters each line. Treat every headline metric with an explicit basis tag; the two bases are not interchangeable. |
| F16-4 | F16 | sec11 r2 | 119 | "Other income 26 [Ind AS] ... 8 [IGAAP-eq]"; Q1FY26 IGAAP-eq "0" | AMBIGUOUS | ₹18 Cr Other-income reclassification (Adj 18; Q1FY26 Adj 15, IGAAP-eq 0 ZERO_STANDING). A4 to ask what the Ind AS "other income" of ₹26 Cr (FY27) / ₹15 Cr (FY26) comprises (lease-related notional / interest unwind) and why the IGAAP-eq strips it to ₹8 Cr / ₹0. Non-trivial to the "notional loss" narrative. |
| F16-5 | F16 | sec7 r1 | 106 | "CRISIL 'A+' (Stable) rating, reaffirming financial strength" | NEUTRAL-FACT | Reaffirmation (not upgrade); no prior rating, rationale, or leverage figure cited. Supports checklist #4 (clean/stable) but checklist #5 (net debt IGAAP ex-lease <0.5x / >1.5x) CANNOT be tested — this release carries no net-debt or leverage number. Pull the CRISIL rationale and the results-filing balance sheet before scoring #5. |

---

## CHECKLIST SCORECARD (all 17; one status each)

| # | Status | Basis |
|---|--------|-------|
| F1 | PASS | 13 ZERO_STANDING cells (ledger sec11 rows 2,4,5,7,8,10,11) all read at lines 119-135. Every zero is a mechanical Ind AS 116 split artifact (IGAAP carries no separate lease-interest/ROU line; several Ind AS Adj. cells are zero for lines IGAAP does not adjust). None anticipates a hidden transaction class (no exceptional/discontinued/impairment/profit-on-sale line exists). Nothing forensic. |
| F2 | N.A. | No standalone-vs-consolidated split in this press release; the two columns are Ind AS vs IGAAP-equivalent, not S vs C. |
| F3 | N.A. | No entity-level cost lines; no subsidiary/JV disclosure to test for shells. |
| F4 | FINDING | F4-1. No auditor Other Matters para exists, but the check's purpose (reliance on non-auditor-reviewed numbers) is squarely engaged: 100% of the headline PAT (₹35 Cr) rests on a management-constructed IGAAP-eq bridge; statutory Ind AS is a ₹24 Cr loss. |
| F5 | N.A. | No going-concern / Emphasis-of-Matter paragraph in a press release; no prior-quarter extract to verbatim-diff. |
| F6 | FINDING | F6-1, F6-2. Dated commitments (concall Aug 13, IP submission) captured; and zero of the 7 dropped FY27 forward numerics is restated as guidance here. |
| F7 | FINDING | F7-1, F7-2. "mainly/primarily" hedges leave the non-Ind AS 116 bridge residual unquantified; "estimated" hedges the current-tax anchor. |
| F8 | FINDING | F8-1. IGAAP-eq ETR ≈18.6-18.9% vs statutory 25.17%; Ind AS tax credit on a loss = DTA recognition / future ETR step-up. Rounding caveat noted. |
| F9 | N.A. | No OCI / actuarial disclosure in this press release. |
| F10 | N.A. | No paid-up capital, share count, or basic/diluted EPS disclosed. |
| F11 | N.A. | No balance sheet, reserves, or net-worth figure to tie out (CRISIL A+ cited without a net-worth number). |
| F12 | N.A. | Segment results referenced (line 148) but NOT present in this extract; no segment assets/liabilities to trend. |
| F13 | N.A. | Reg 30 press release, not a board-outcome letter; no AR/AGM/record-date/director-term disclosure. |
| F14 | FINDING | F14-1, F14-2, F14-3. Internal-arithmetic inconsistencies (revenue bridge (6) vs +5; PAT (24) vs implied (23); +91% vs 19->35 = +84%); minor entity-name/email inconsistencies; ledger "(restated)" annotation not verbatim in extract. |
| F15 | N.A. | No consolidation entity list and no prior-quarter ledger to diff; former-names disclosure (line 48-49) is name history, not an entity-list change. |
| F16 | FINDING | F16-1..F16-5. VAS crosses GREEN tripwire; occupancy basis-label mismatch vs RPA; Ind AS/IGAAP basis cherry-picking; ₹18 Cr other-income reclass; CRISIL A+ reaffirmed (checklist #5 untestable). |
| F17 | N.A. | Concall-specific silence audit requires a transcript; the call is on Aug 13, 2026 (one day after this release). No transcript exists yet — silence audit deferred to the concall document. The press-release-level check on the 7 dropped numerics is handled under F6-2. |

Scorecard tally: PASS 1 (F1); FINDING 5 (F4, F6, F7, F8, F14, F16 = 6 — see below); N.A. 10. Correction: FINDING = F4, F6, F7, F8, F14, F16 (6); PASS = F1 (1); N.A. = F2, F3, F5, F9, F10, F11, F12, F13, F15, F17 (10). Total 17, no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|------------|--------------|-----|-------------|
| Earnings conference call to discuss Q1 FY27 results | Thu Aug 13, 2026, 2:00 PM IST | line 154 | scheduled/upcoming ("will be held") |
| Analyst/institutional investor presentation submitted to Stock Exchanges and hosted on website | on/around Aug 13, 2026 | lines 158-159 | underway ("will be submitted / shall also be hosted") |
| Detailed Ind AS <-> IGAAP-equivalent reconciliation available in the Investor Presentation | at IP release (Aug 13, 2026) | lines 143-144 | deferred (pointer) |
| Ind AS results + segment results available in IR section of website | at/after filing | lines 148-150 | available ("are available") |

---

## NOTES FOR A4 (routing)

- AMBIGUOUS -> convert to management questions: F4-1 (auditor review of IGAAP-eq bridge; guidance basis), F7-1 (full quantification of non-Ind AS 116 bridge residual), F14-1 (unrounded bridge; exact +91% PAT base), F16-2 (reconcile steady-state/overall occupancy to RPA basis), F16-4 (composition of Ind AS "other income" and the ₹18 Cr strip).
- FORWARD-SIGNAL -> catalyst/tracker: F6-1 (Aug 13 concall as grade-A restatement venue), F6-2 (7 dropped numerics not restated — watchlist for the call), F16-1 (VAS GREEN tripwire #6 crossed at 17%).
- CONFIRMATORY-NEGATIVE: F16-3 (basis cherry-picking across Ind AS 61% EBITDA margin vs IGAAP-eq PAT).
- Checklist tie-ins surfaced: #1 occupancy basis unresolved (F16-2), #2 IGAAP-adj PAT positive but non-statutory (F4-1, and IGAAP-eq PAT ₹35 Cr is positive+growing), #4 CRISIL clean/stable held (F16-5), #5 leverage UNTESTABLE from this doc (F16-5), #6 VAS GREEN crossed (F16-1).

---

```yaml
stage: A3-forensics
company: "INDIQUBE"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/indiqube-q1fy27/work/forensics_presentation-pressrelease_indiqube_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: FINDING
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F4-1", check: "F4", line: "55-56,63,118,135", classification: "AMBIGUOUS", implication: "Headline profit rests 100% on management-constructed, non-auditor-reviewed IGAAP-eq bridge; statutory Ind AS is a Rs24Cr loss."}
  - {id: "F6-1", check: "F6", line: "154,158-159", classification: "FORWARD-SIGNAL", implication: "Aug 13 concall + Investor Presentation is the pending venue for the 7 dropped FY27 numerics; grade-A hold resolves there."}
  - {id: "F6-2", check: "F6", line: "78-79,88,92,96", classification: "FORWARD-SIGNAL", implication: "None of the 7 dropped FY27 forward numerics restated as guidance; solar and fit-out entirely absent; test still open."}
  - {id: "F7-1", check: "F7", line: "111-112,137-138", classification: "AMBIGUOUS", implication: "'mainly/primarily' leaves non-Ind AS 116 bridge residual (other income 18, other expenses 178) unquantified."}
  - {id: "F7-2", check: "F7", line: "110-111", classification: "NEUTRAL-FACT", implication: "'estimated' current tax anchors the IGAAP-eq PAT; minor pre-emptive hedge."}
  - {id: "F8-1", check: "F8", line: "134,111", classification: "NEUTRAL-FACT", implication: "IGAAP-eq ETR ~18.6-18.9% vs 25.17% (~650bps shield); Ind AS tax credit on loss = DTA build, future ETR step-up."}
  - {id: "F14-1", check: "F14", line: "56,118,133-135", classification: "AMBIGUOUS", implication: "Bridge arithmetic inconsistencies: rev adj (6) vs +5; PAT (24) vs implied (23); +91% vs 19->35 = +84%."}
  - {id: "F14-2", check: "F14", line: "49,59-60,164,174", classification: "NEUTRAL-FACT", implication: "Minor disclosure-hygiene inconsistencies (two IR emails, singular/plural platform, casing)."}
  - {id: "F14-3", check: "F14", line: "30-32", classification: "NEUTRAL-FACT", implication: "Ledger '(restated)' annotation not verbatim in extract; no restatement note disclosed in-doc."}
  - {id: "F16-1", check: "F16", line: "78-79", classification: "FORWARD-SIGNAL", implication: "VAS 17% crosses Notion GREEN tripwire #6; quote-only number, corroborate at concall."}
  - {id: "F16-2", check: "F16", line: "74-75,104", classification: "AMBIGUOUS", implication: "Occupancy labels steady-state 90%/overall 86% differ from Notion RPA-basis #1; do not assume equivalence."}
  - {id: "F16-3", check: "F16", line: "113,88", classification: "CONFIRMATORY-NEGATIVE", implication: "Basis cherry-picking: Ind AS 61% EBITDA margin touted alongside IGAAP-eq positive PAT."}
  - {id: "F16-4", check: "F16", line: "119", classification: "AMBIGUOUS", implication: "Rs18Cr other-income reclassification (IndAS 26 vs IGAAP-eq 8; FY26 IGAAP-eq 0); composition undisclosed."}
  - {id: "F16-5", check: "F16", line: "106", classification: "NEUTRAL-FACT", implication: "CRISIL A+ reaffirmed (checklist #4); checklist #5 leverage untestable, no net-debt figure in doc."}
forward_signals: ["F6-1", "F6-2", "F16-1"]
ambiguous: ["F4-1", "F7-1", "F14-1", "F16-2", "F16-4"]
commitments:
  - {commitment: "Earnings conference call for Q1 FY27 results", implied_date: "2026-08-13T14:00+05:30", ref: "line 154", status_word: "scheduled"}
  - {commitment: "Analyst/institutional presentation submitted to exchanges and hosted on website", implied_date: "2026-08-13", ref: "lines 158-159", status_word: "underway"}
  - {commitment: "Detailed Ind AS<->IGAAP reconciliation in Investor Presentation", implied_date: "2026-08-13", ref: "lines 143-144", status_word: "deferred"}
  - {commitment: "Ind AS results + segment results available on IR website", implied_date: "2026-08-12", ref: "lines 148-150", status_word: "available"}
gate_a3: pass
blank_checks: []
```
