# A3 FORENSIC NOTES — HCP Plastene Bulkpack Ltd (526717), Q1FY27

Doctype: results (Regulation 30 event disclosure — ESOP 2022 allotment of 16,780 equity shares + Annexure A; 3 pages, doc lines 1-131)
Source extract: extract_reg30esop_526717_q1fy27.txt
Ledger: ledger_reg30esop_526717_q1fy27.md
Ledger reconciliation: 24/24 rows read verbatim at cited lines (Table 1: 11 disclosure fields; Table 2: 12 Annexure rows; Table 3: 1 signature block) = 100%.

This is a single-event corporate-action disclosure, not a periodic financial statement. F1-F15 are in scope by doctype; the balance-sheet / auditor / consolidation / segment checks (F2-F5, F8-F9, F11-F12, F15) return N.A. for absence of the underlying data, each noted below. F16/F17 are N.A. (not a presentation, not a concall). Every check carries an explicit status.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| FN-01 | F10 / F14 | T1 row 9 (ARITHMETIC_FLAG) | 41-42 | "shall stand increased from Rupees 106748370 ( 10674837 shares of rupees 10 each) to Rupees 106916170 (106916170 shares of rupees 10 each )" | CONFIRMATORY-NEGATIVE | Post-allotment share count is misprinted as 106,916,170 shares (should be 10,691,617). The rupee capital (Rs 106,916,170) and the money realized are arithmetically correct; the defect is a drafting error in a statutory capital figure. Reinforces the live FLAG-DISCLOSURE watch (repeat SEBI/BSE disclosure-quality lapse) amid the CS/auditor/CFO exit sequence. |
| FN-02 | F10 | T1 row 6; T2 row 4 | 34, 106-107 | "at exercise price of Rupees 10 per option"; "The exercise price is Rupees 10 ( Rupee Ten Only) per Option" | FORWARD-SIGNAL | Exercise price equals face value (Rs 10) — options struck at par, zero premium. Entire Rs 167,800 realized goes to share capital, nothing to securities premium. Signals ESOP 2022 grants are priced at par; future exercises dilute at par with no premium cushion. |
| FN-03 | F10 | T2 rows 3, 9, 12 | 103-105, 121-122, 129-130 | "Total 2,50,000 options covered in the scheme out of that 16780 ... exercised"; "Options lapsed 29450" | FORWARD-SIGNAL | Of the 250,000-option pool, only 16,780 exercised and 29,450 lapsed to date; ~203,770 options (≈1.9% of post-allotment capital) remain as unexercised overhang. Future dilution pipeline; scheme is early in its life. Vested-but-unexercised = 900 (17,680 vested − 16,780 exercised), immediately exercisable. |
| FN-04 | F13 | T3 row 1 | 76-78 | "Rishabh Kumar Jain / Company Secretary and Compliance Officer / Membership Number: F7271" | AMBIGUOUS | Filing is signed 12 Aug 2026 by a seated CS & Compliance Officer, yet the Notion monitor records a CS resignation in Jan-2026. Either a replacement CS (F7271) was appointed (seat filled — mildly positive) or a role/timeline inconsistency exists. Reconcile appointment date of current CS against the Jan-2026 exit → A4 question. |
| FN-05 | F14 | T1 row 2; T2 row 3 | 15, 103-105 | "Mumbeai - 400 001"; "Total 2,50,000 options covered in the scheme out of that 16780, equity shares ... are exercised for the current allotment" | CONFIRMATORY-NEGATIVE | Drafting/quality inconsistencies: addressee typo ("Mumbeai"); row 3 conflates "options" with "equity shares ... exercised"; website rendered both "www.hpbl.in" and "www.hpbLin" (lines 61/83). Individually immaterial, but a cumulative disclosure-hygiene data point that supports the FLAG-DISCLOSURE watch. (Some are OCR-origin per ledger; the row-3 conflation and the FN-01 capital misprint are drafting, not OCR.) |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | PASS | Both ZERO_STANDING rows examined (T2 row 1 line 96-98 "Brief details of options granted — Not Applicable"; T2 row 7 line 115-117 "Subsequent changes ... — Not Applicable"). Standard SEBI SBEB template fields, correctly N/A for an exercise-not-grant event; no hidden transaction class anticipated. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No financial statements in this event disclosure; no S/C figures to decompose. |
| F3 SHELL-ENTITY | N.A. | No consolidation or cost lines present. |
| F4 UNAUDITED CONTRIBUTION | N.A. | No auditor report / Other Matters paragraph. |
| F5 GOING CONCERN / EoM | N.A. | No auditor report / EoM language; no prior-quarter EoM to diff. |
| F6 FORWARD-COMMITMENT MINING | PASS | Lexicon sweep hit only administrative future-tense: "shall stand increased" (41), "shall rank pari-passu" (37), "will be made available on the Company's website" (61). No dateable business catalyst; nothing for the FTTCP timeline. See Commitment Register. |
| F7 HEDGE PHRASE MINING | PASS | Only boilerplate deferral hedges: "(if applicable)" (99-102), "As per ESOP scheme" (109-110), "As per ESOP Scheme of the Company" (112-113). No new hedge on revenue/customer concentration. |
| F8 TAX FORENSICS | N.A. | No P&L / tax line / ETR data. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial data. |
| F10 SHARE COUNT & DILUTION | FINDING | FN-01 (capital reconciliation misprint), FN-02 (par exercise price), FN-03 (203,770-option overhang). Capital arithmetic verified: pre 10,674,837×10=106,748,370; post 10,691,617×10=106,916,170; money realized 16,780×10=167,800 — all internally correct except the printed post-allotment share COUNT. This-tranche dilution 0.157%. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No Other Equity / net-worth figure disclosed to reconcile (note: par exercise adds no securities premium — captured in FN-02). |
| F12 SEGMENT FORENSICS | N.A. | No segment data. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | FN-04 — CS signatory (F7271) seated on a filing dated after the Notion-recorded Jan-2026 CS resignation; reconcile. Note: action is a Stakeholders Relationship Committee approval, not a full-Board outcome; no AR/AGM/dividend/director-term/auditor items to schedule. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | FN-05 (typos, options/shares conflation, website variants) + FN-01 (capital-figure misprint). Cumulative disclosure-hygiene signal. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list. |
| F16 PRESENTATION DROPPED/REFRAMED | N.A. | Not a presentation/deck. |
| F17 CONCALL SILENCE AUDIT | N.A. | Not a concall; no transcript. Cross-doc note (not a finding here): the Notion monitor records a same-day (12-Aug-2026) CFO resignation filed separately — this ESOP letter neither references nor is expected to reference it; hand to A4 for the governance-sequence question. |

Scorecard: PASS ×3 (F1, F6, F7) | FINDING ×3 (F10, F13, F14) | N.A. ×11 (F2, F3, F4, F5, F8, F9, F11, F12, F15, F16, F17). All 17 marked; no blanks — GATE A3 pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Paid-up capital to stand increased to Rs 106,916,170 on allotment | 12 Aug 2026 (event date) | line 41-42 | completed (allotment approved same day) |
| Allotment details to be made available on Company website (www.hpbl.in) | on/after 12 Aug 2026 | line 61 | underway (administrative) |

No catalyst-quality (business/operational) commitments present. Neither entry feeds the FTTCP catalyst timeline; both are administrative.

---

## RECONCILIATION AGAINST A2 FLAGS

- ARITHMETIC_FLAG (T1 row 9): CONFIRMED as an internal inconsistency. The rupee capital figure Rs 106,916,170 is correct (10,691,617 shares × Rs 10); the parenthetical "106916170 shares" is a 10× misprint of the true 10,691,617-share count. See FN-01. Share-count-times-face-value arithmetic is otherwise sound throughout (pre-capital, post-capital, money realized all tie).
- ZERO_STANDING (T2 rows 1, 7): CONFIRMED benign — standard SEBI template fields answered "Not Applicable" for an exercise (not grant) event. See F1.
- Completeness gap noted by A2 (250,000 pool vs disclosed movements): CONFIRMED and quantified — ~203,770-option unexercised overhang, carried as FN-03 (FORWARD-SIGNAL), not a document omission.

---

## FORWARD IMPLICATIONS FOR A4

- FN-02, FN-03 (FORWARD-SIGNAL): at-par ESOP pricing plus a ~1.9% unexercised overhang → future dilution with no premium; quantify remaining vesting schedule.
- FN-04 (AMBIGUOUS): reconcile current CS (F7271) appointment date against the Jan-2026 CS resignation on the Notion monitor → management question.
- FN-01, FN-05 (CONFIRMATORY-NEGATIVE): disclosure-quality defects support the standing FLAG-DISCLOSURE watch during the CS/internal-auditor/CFO exit sequence.

```yaml
stage: A3-forensics
company: "526717"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/526717-q1fy27/work/forensics_reg30esop_526717_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: PASS
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FN-01", check: "F10", line: "41-42", classification: "CONFIRMATORY-NEGATIVE", implication: "Post-allotment share count misprinted as 106,916,170 (correct 10,691,617); rupee capital and money realized arithmetically sound. Statutory-figure drafting error; supports FLAG-DISCLOSURE watch."}
  - {id: "FN-02", check: "F10", line: "34,106-107", classification: "FORWARD-SIGNAL", implication: "Exercise price Rs 10 = face value; options struck at par, zero premium. Future exercises dilute at par with no securities-premium cushion."}
  - {id: "FN-03", check: "F10", line: "103-105,121-122,129-130", classification: "FORWARD-SIGNAL", implication: "~203,770 of 250,000-option pool unexercised (~1.9% of post capital) = future dilution overhang; scheme early in life."}
  - {id: "FN-04", check: "F13", line: "76-78", classification: "AMBIGUOUS", implication: "CS (F7271) seated on 12-Aug-2026 filing despite Notion-recorded Jan-2026 CS resignation; reconcile appointment date -> A4 question."}
  - {id: "FN-05", check: "F14", line: "15,103-105", classification: "CONFIRMATORY-NEGATIVE", implication: "Cumulative drafting-hygiene defects (typos, options/shares conflation, website variants) alongside FN-01; supports FLAG-DISCLOSURE watch."}
forward_signals: ["FN-02", "FN-03"]
ambiguous: ["FN-04"]
commitments:
  - {commitment: "Paid-up capital to stand increased to Rs 106,916,170 on allotment", implied_date: "2026-08-12", ref: "line 41-42", status_word: "completed"}
  - {commitment: "Allotment details to be made available on Company website www.hpbl.in", implied_date: "2026-08-12", ref: "line 61", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
