# A3 FORENSIC NOTES — Sterlite Technologies Limited (STLTECH), Q1FY27 — DOCTYPE: results

Source: `extract_results_stltech_q1fy27.txt` (25 pages, 1586 lines, unit Crores).
Reconciliation contract: `ledger_results_stltech_q1fy27.md`. Every ledger row read verbatim at its
cited line before judging. Ledger reconciled 100% (all sections 1-16, all 200 line items / 24 notes /
27 auditor paras / 20 entities / 38 zero-standing rows / 14 signature blocks read at source).
Doctype rule applied: F1-F15 apply; F16 (presentation) and F17 (concall) are N.A. on a results filing.
Prior-quarter extract: none (first quarterly-pipeline run) — so F5 verbatim EoM-diff and F15 entity-diff
cannot be run against a prior; handled explicitly below, not fabricated.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| F2-01 | F2 | S2 r20 / S5 r20 | 221 vs 562 | consol "197" vs standalone "125" net profit | FORWARD-SIGNAL | Subsidiaries carry Rs 72 cr (37%) of consol PAT; gap vs standalone PAT swung from ~400% (Q1FY26) to 58% (Q1FY27); consolidated earnings quality is subsidiary-concentrated, not parent-driven. |
| F4-01 | F4 | S8 para7/para8 | 861-878 | "four subsidiaries reflect total revenues of Rs. 578 crores, total net profit after tax of Rs. 42 crores" | AMBIGUOUS | Rs 43 cr PAT (Rs 42 cr other-auditor + Rs 1 cr unreviewed) = ~21.8% of consol PAT rests on numbers PW did not review directly; the four Rs-578-cr-revenue subsidiaries are unnamed (aggregate only), and 4 of 20 entities are unaccounted for in paras 7/8. |
| F5-01 | F5 | S8 para6 / S9 para5 | 856-860 / 952-956 | "the possible financial impact of the litigation is currently not determinable" | FORWARD-SIGNAL | Litigation EoM (Prysmian vs STI): $101.25M confirmed award, $41.53M bond posted, Fourth Circuit appeal pending. Appeal outcome is a dated catalyst and maps directly to prior-thesis trigger #4 ("Prysmian full loss + appeal options exhausted"). |
| F6-01 | F6 | S4 note5 / S6 note6 | 364-370 / 640-646 | "The proceeds from the issue is to be utilised for (i) repayment...and (ii) general corporate purposes" | FORWARD-SIGNAL | Rs 1,500 cr QIP proceeds raised, deployment to debt repayment pending; "net debt-free" claim rests on undeployed cash sitting in Cash & Equivalents (Rs 1,777 cr standalone / Rs 2,021 cr consol). Track actual debt paydown next quarter. |
| F6-02 | F6 | S4 note8 / S6 note9 | 449-451 / 718-720 | "will seek necessary approval in their respective ensuing Annual General Meeting" | FORWARD-SIGNAL | Managerial remuneration paid above Schedule V limits (Rs 11 cr consol / Rs 3 cr standalone) requires post-facto shareholder ratification at the ensuing AGM — a scheduled governance event; AGM notice not in this filing. |
| F7-01 | F7 | S4 note5/note6 | 368 / 384 | "The management does not expect any material impact"; "cannot be ascertained at this stage" | AMBIGUOUS | Two pre-emptive hedges in the notes: reassurance on promoter dilution (44.44%->42.29%) and non-quantification of the $101.25M Prysmian award. Note-level hedging is legal cover; lean bear pending appeal clarity. |
| F8-01 | F8 | S5 r18/r19 / S4 note10 | 560-561 / 484-486 | standalone "Current tax 1" vs "Deferred tax 43"; "deferred tax assets to the extent of Rs. 41 crores were written-down" | FORWARD-SIGNAL | Standalone cash tax is negligible (Rs 1 cr current on Rs 169 cr PBT) while Rs 43 cr is deferred — carryforward/MAT shield in use. As shields deplete, cash tax steps up. STL Digital already wrote off Rs 41 cr DTA (does not expect to use its losses). |
| F9-01 | F9 | S5 r21 | 564 | standalone OCI "A.i) Items that will be reclassified to profit or loss 48" | FORWARD-SIGNAL | Single-quarter reclassifiable OCI of +Rs 48 cr (standalone) exceeds the full prior-year figure of -Rs 38 cr — a >100% swing in hedge/FCTR reserves that will recycle into future P&L. Actuarial (B.i) is immaterial/stable (Rs 1 cr); the swing is FX/hedge, not assumptions. |
| F10-01 | F10 | S2 r32/r33 | 238-239 | Basic EPS "4.03" vs Diluted EPS "3.71" | FORWARD-SIGNAL | Basic-diluted spread widened to ~8% (Q1FY27) from ~0% (Q1FY26) — new dilutive instruments: ~45M preferential warrants (Annexure II, allotted 30-Mar-26, 25% paid) plus 25.7M QIP shares (subsequent). Combined overhang ~14% of the 488M base is a forward EPS drag. |
| F11-01 | F11 | S2 r31 / S7 r16 | 236 vs 447 | consol "Other Equity 2,170"; "Net worth 1,966" (FY26) | AMBIGUOUS | Paid-up 98 + Other Equity 2,170 = 2,268 vs reported Reg-52 net worth 1,966 = Rs 302 cr (13.3%) gap, above 5%. Candidate reconciling items: FCTR (large for a 20-entity global group) and cash-flow-hedge reserve, both OCI-origin and excluded from the statutory net-worth definition. Confirm at AR. |

---

## CHECKLIST SCORECARD (all 17)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | PASS | All 38 ZERO_STANDING rows resolved: standard P&L template lines (Exceptional items l.216, Net impairment l.208, Purchase of stock-in-trade l.203 nil at consol = intra-group elimination, non-zero Rs 58 cr standalone l.542), Not-Applicable regulatory items (Annexure I C/D/E l.987-994), and Asset-cover NCD 9.35% dash in 3 of 4 periods (l.435) = that NCD series redeemed after Q1FY26 (deleveraging confirmation). None anticipate an undisclosed transaction class. |
| F2 | FINDING | S-vs-C PAT gap volatile and subsidiary-heavy: Rs 72 cr subsidiary PAT = 37% of consol; gap-as-%-of-standalone-PAT moved from ~400% (Q1FY26) to 58% (Q1FY27), far exceeding the 5pp trigger. See F2-01. |
| F3 | PASS | Cost lines differ materially standalone vs consol (Materials 386 vs 805 l.541/202; Employee 53 vs 195 l.546/207; Deprec. 46 vs 85 l.552/214) — subsidiaries have real operations, no shells. 12 unreviewed subs are small (Rs 94 cr rev) but operational; no Going Concern EoM anywhere. |
| F4 | FINDING | ~21.8% of consol PAT (Rs 43 cr) rests on numbers not reviewed by statutory auditor PW; four Rs-578-cr-revenue subsidiaries named by aggregate only; 4 of 20 entities unaccounted for in review paras 7/8. See F4-01. No prior period to trend the ratio (first run). |
| F5 | FINDING | One EoM in each report — the Prysmian/STI litigation (consol l.856-860, standalone l.952-956), "possible financial impact...currently not determinable." Live contingent liability with a pending appeal catalyst. Verbatim prior-quarter diff not runnable (first run) — baseline captured for next quarter. See F5-01. |
| F6 | FINDING | Three dateable commitments mined (QIP deployment, AGM remuneration ratification, Labour Codes accounting) plus the filed Prysmian appeal — see Commitment Register. F6-01, F6-02. |
| F7 | FINDING | Two note-level hedges: "does not expect any material impact" (promoter dilution, l.368) and "cannot be ascertained at this stage" (Prysmian, l.384). Pre-emptive legal cover. See F7-01. |
| F8 | FINDING | Standalone cash tax negligible (current Rs 1 cr vs deferred Rs 43 cr, l.560-561) = carryforward/MAT shield in use, future ETR step-up risk; STL Digital DTA write-down Rs 41 cr (l.484). Consol ETR 23.3%, standalone 26.0%, both near statutory; no "earlier-year" tax adjustment line. See F8-01. |
| F9 | FINDING | Standalone reclassifiable OCI +Rs 48 cr in one quarter (l.564) exceeds full prior-year -Rs 38 cr; hedge/FCTR reserves to recycle into P&L. Actuarial component (B.i) immaterial and stable. See F9-01. |
| F10 | FINDING | Basic-diluted EPS spread widened to ~8% (l.238-239) from ~0% a year ago; warrants (Annexure II) + QIP shares (Note 5) are the dilutive instruments. Paid-up unchanged Rs 98 cr; 35,097 ESOP shares (l.332) immaterial. See F10-01. |
| F11 | FINDING | Consol Other Equity + Paid-up (2,268) vs Reg-52 net worth (1,966) = 13.3% gap > 5%; candidate reconciling items FCTR + hedge reserve. Standalone gap 4.3% (within tolerance). See F11-01. |
| F12 | PASS | No anomalous segment pattern: Optical assets +Rs 1,424 cr YoY (4,523->5,947, l.291) matched by liabilities +Rs 842 cr (l.298) = order-ramp build, not equity-funded; Digital segment small/near-breakeven with liabilities>assets (no zero-liability build, no revenue-less asset). Unallocated-asset jump to 2,450 (l.295) reconciles to QIP cash. |
| F13 | PASS | Board Outcome is results-approval only — 9 agenda items (core + 8 enclosures, l.33-55); no AR approval, AGM notice, record date, dividend, director appointment, auditor change or capital-raising resolution in this letter. SIG_BEFORE_MEETING_CONCLUSION resolved: statement/auditor signatures 12:35-13:04 fall within the 11:50am-2:36pm meeting window (approval mid-meeting), only the CS cover-letter signature (14:39:55, l.64) post-dates conclusion — mechanically consistent, not a red flag. |
| F14 | PASS | No genuine note-vs-auditor contradiction (notes and letters both say "limited review / unmodified conclusion"). Apparent cross-table differences (NCD interest "24.66" l.352 vs "24.65" l.629; entity "STI" rendered "Sri" l.649) are OCR artifacts of a garbled scan, not source drafting errors; individually and cumulatively immaterial. |
| F15 | N.A. | Applicable to results doctype but not runnable: no prior-quarter consolidation list exists (first quarterly-pipeline run). 20 entities enumerated (11 subsidiaries + 9 step-down, l.824-847) as the baseline for next quarter's diff. Entity reconciliation gap (4 of 20) folded into F4-01. |
| F16 | N.A. | Presentation-specific check; this is a results filing (Investors Presentation is a separate doctype/run, l.40). |
| F17 | N.A. | Concall-specific silence audit; this is a results filing. Note for A4: the enclosed Press Release (l.90-171) already addresses several Section-8 monitorables (order book Rs 18,618 Cr l.94; reported EBITDA margin 20.8% l.104; net-debt-free/QIP l.96,110; $100Mn+ hyperscaler orders l.119; $1.11bn AI-DC order l.117) — carried to A4, not scored here. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Rs 1,500 cr QIP proceeds to be utilised for (i) repayment of borrowings and (ii) general corporate purposes | near-term (QIP allotted post-30-Jun-26; deployment pending) | consol Note 5 (l.364-370) / std Note 6 (l.640-646) | underway |
| Seek shareholder approval for excess managerial remuneration (Rs 11 cr consol / Rs 3 cr standalone) | ensuing AGM (FY27) | consol Note 8 (l.449-451) / std Note 9 (l.718-720) | initiated |
| Provide accounting effect for four Labour Codes as Rules are finalised / clarifications issued | on Government rule finalisation | consol Note 9(i) (l.455-461) / std Note 10 (l.723-729) | underway |
| Pursue Fourth Circuit appeal of Prysmian verdict; $41.53M bond deposited | appeal filed, outcome pending | consol Note 6 / std Note 7 (l.383-384 / 658-659) | underway |

---

## FLAG RESOLUTION MAP (A2 flags -> F-check disposition)

- ZERO_STANDING (38 rows) -> F1 PASS (all standard template / elimination / N.A.-regulatory lines; NCD 9.35% redemption noted).
- SIG_BEFORE_MEETING_CONCLUSION (12 of 14 blocks) -> F13 PASS (signatures within meeting window = mid-meeting approval; CS cover letter alone post-dates conclusion; consistent).
- UNAUDITED_ENTITIES (12 subs, Rs 94 cr rev / Rs 1 cr PAT) -> F4 FINDING (folded with other-auditor reliance; total 21.8% of PAT not PW-reviewed).
- CONTINGENT_LIABILITY_UNQUANTIFIED (Prysmian $101.25M) -> F5 FINDING (EoM/catalyst) + F7 FINDING (hedge language) + F6 register (appeal).
- GOVERNANCE_APPROVAL_PENDING (remuneration Rs 11cr/Rs 3cr) -> F6-02 FINDING + Commitment Register.
- OCR_TABLE_GARBLED (Security Cover Parts A/B, pages 22-25) -> data-quality limitation: constrains independent cross-check of security-cover asset/liability cells, but the Reg-52 ratio-table net worth used in F11 is legible (l.447/715); no F-finding depends on the garbled cells. Noted for next-quarter re-extract.

Data-quality note: F11 net-worth tie-out and F12 asset trends rely on the legible P&L/segment/ratio
tables, not the OCR-corrupted Security Cover statement; conclusions above are drawn only from
confidently-read values.

```yaml
stage: A3-forensics
company: "STLTECH"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/stltech-q1fy27/work/forensics_results_stltech_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: PASS
  F13: PASS
  F14: PASS
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F2-01", check: "F2", line: "221 vs 562", classification: "FORWARD-SIGNAL", implication: "Subsidiaries carry 37% of consol PAT; S-vs-C gap swung >5pp; consolidated earnings subsidiary-concentrated."}
  - {id: "F4-01", check: "F4", line: "861-878", classification: "AMBIGUOUS", implication: "~21.8% of consol PAT not reviewed by statutory auditor; four Rs-578cr-rev subs unnamed; 4 of 20 entities unreconciled in review paras."}
  - {id: "F5-01", check: "F5", line: "856-860", classification: "FORWARD-SIGNAL", implication: "Prysmian litigation EoM; $101.25M award, $41.53M bond, Fourth Circuit appeal pending = dated catalyst matching thesis trigger #4."}
  - {id: "F6-01", check: "F6", line: "364-370", classification: "FORWARD-SIGNAL", implication: "Rs 1,500cr QIP proceeds undeployed; net-debt-free claim rests on cash pending debt paydown; track actual repayment."}
  - {id: "F6-02", check: "F6", line: "449-451", classification: "FORWARD-SIGNAL", implication: "Excess managerial remuneration Rs 11cr/Rs 3cr needs AGM ratification; scheduled governance event, notice not yet filed."}
  - {id: "F7-01", check: "F7", line: "384", classification: "AMBIGUOUS", implication: "Note-level hedges on promoter dilution and unquantified Prysmian award = pre-emptive legal cover; lean bear pending appeal clarity."}
  - {id: "F8-01", check: "F8", line: "560-561", classification: "FORWARD-SIGNAL", implication: "Standalone near-zero cash tax (Rs 1cr current vs Rs 43cr deferred) = carryforward shield in use; future cash-tax step-up; STL Digital wrote off Rs 41cr DTA."}
  - {id: "F9-01", check: "F9", line: "564", classification: "FORWARD-SIGNAL", implication: "Single-quarter reclassifiable OCI +Rs 48cr exceeds full prior-year -Rs 38cr; hedge/FCTR reserves to recycle into future P&L."}
  - {id: "F10-01", check: "F10", line: "238-239", classification: "FORWARD-SIGNAL", implication: "Basic-diluted EPS spread widened to ~8% from ~0%; ~45M warrants + 25.7M QIP shares = ~14% dilution overhang, forward EPS drag."}
  - {id: "F11-01", check: "F11", line: "236 vs 447", classification: "AMBIGUOUS", implication: "Consol net-worth vs total-equity gap 13.3% >5%; candidate reconciling items FCTR + cash-flow-hedge reserve; confirm at AR."}
forward_signals: ["F2-01", "F5-01", "F6-01", "F6-02", "F8-01", "F9-01", "F10-01"]
ambiguous: ["F4-01", "F7-01", "F11-01"]
commitments:
  - {commitment: "Rs 1,500cr QIP proceeds to be utilised for debt repayment and general corporate purposes", implied_date: "near-term (post-30-Jun-26 allotment, deployment pending)", ref: "consol Note 5 l.364-370 / std Note 6 l.640-646", status_word: "underway"}
  - {commitment: "Seek shareholder approval for excess managerial remuneration (Rs 11cr consol / Rs 3cr standalone)", implied_date: "ensuing AGM FY27", ref: "consol Note 8 l.449-451 / std Note 9 l.718-720", status_word: "initiated"}
  - {commitment: "Provide accounting effect for four Labour Codes as Rules/clarifications finalised", implied_date: "on Government rule finalisation", ref: "consol Note 9(i) l.455-461 / std Note 10 l.723-729", status_word: "underway"}
  - {commitment: "Pursue Fourth Circuit appeal of Prysmian verdict; $41.53M bond deposited", implied_date: "appeal filed, outcome pending", ref: "consol Note 6 / std Note 7 l.383-384 / 658-659", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
