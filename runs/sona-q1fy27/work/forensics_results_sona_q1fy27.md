# A3 FORENSIC NOTES — SONACOMS Q1 FY27 — DOCTYPE: RESULTS

Source extract: `extract_results_sona_q1fy27.txt` (593 lines, 10 pages, Reg 33 Board Outcome + standalone + consolidated).
Ledger reconciled: `ledger_results_sona_q1fy27.md` — 100% of rows read at cited lines before judging (65 line items, 14 notes, 8 zero-standing, 17 entities, 9 auditor paras, 5 signature blocks, 1 agenda item).
Units: Rs Million, x0.1 to Crores. Note wording cross-checked against `results_sona_q1fy27_layout.txt` where OCR garbled.
Prior-quarter extract: **NONE** (first pipeline run for SONACOMS). F5 verbatim EoM diff and F15 entity diff CANNOT be run against a prior quarter; absence noted explicitly at each, not skipped. All "new" items are FIRST_RUN_BASELINE.

Doctype applicability: F1-F15 apply; F16 and F17 are N.A. (results filing, no deck / no transcript).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-F1-01 | F1 | LI#13 SA/C (Exceptional items); LI#16 (Tax prior yrs) | 193 / 482; 198 / 486 | "Exceptional items (Refer Note No. 3)" [blank Q1FY27; 91.74 Q1FY26; 507.91 SA / 509.81 C FY26] | FORWARD-SIGNAL | Exceptional-items line is a live template, not dead. DENSO slump sale of the 100% EV subsidiary at independent-valuer fair value (Note 5) is exactly the transaction class that repopulates this line. Expect an exceptional gain/charge in a coming quarter. |
| A3-F2-01 | F2 | LI#19 SA (2,201.06) vs LI#19 C (1,785.13) | 202 / 490 | "Profit for the period/year ... 2,201.06 [SA] ... 1,785.13 [C]" | FORWARD-SIGNAL | Consolidated PAT is Rs 415.93mn BELOW standalone this quarter. Subsidiary stack (Comstar/Novelic/eDrive) is a net drag AND standalone is inflated by a Rs 594.63mn intragroup dividend (Note 6) that eliminates on consolidation. S-vs-C PAT gap swung from -1.3% (Q1FY26) to +18.9% (Q1FY27) = 20.2pp move, far above the 5pp trigger. |
| A3-F6-01 | F6 | Note 5 SA/C | 270-278 / 571-579 | "the Company will slump sell its existing EV Motors and controllers business in its 100% subsidiary at fair market value ... DENSO will buy 49% equity stake in this subsidiary at an Enterprise Value of Rs.17,500 million" | FORWARD-SIGNAL | Dated, dateable management commitment. Sale of 49% of a 100% subsidiary at fair value = a profit-recognition vector and a subsidiary-stake sale. Entity is Sona Comstar eDrive Pvt Ltd (Annexure line 438). Feeds Role 5 promise-vs-delivery tracker. |
| A3-F7-01 | F7 | Note 5 SA/C | 275-277 / 576-578 | "subject to fulfilment of customary conditions, the Company will slump sell ... at fair market value based on an independent valuer's report" | AMBIGUOUS | Pre-emptive hedge inside the note: the Rs 17,500mn EV and any gain are conditional on closing conditions AND a not-yet-final independent valuation. Timing/quantum of the gain is undefined. A4 question: closing timeline, valuation status, expected P&L geography. |
| A3-F8-01 | F8 | LI#20 SA tax (555.15/2,756.21) vs C (624.29/2,409.42) | 200 / 488 | "Total tax expense ... 555.15 [SA] ... 624.29 [C]" | AMBIGUOUS | Standalone ETR Q1FY27 = 20.14% vs statutory 25.17% (~503bps / Rs 138.6mn shield); consolidated ETR is a normal 25.91%. The standalone shield is consistent with the Rs 594.63mn intragroup dividend attracting an 80M-type deduction. Shield is dividend-dependent and unwinds when the dividend stream stops = future ETR step-up. |
| A3-F10-01 | F10 | LI#26 Paid-up (6,220.35 / 6,218.47 / 6,217.21); Note 4 | 218 / 514; 262-268 / 563-569 | "Paid up equity share capital ... 6,220.35" ; "an allotment of 1,70,747 equity shares to him at face value" | NEUTRAL-FACT | Paid-up rose Rs 1.88mn QoQ (+188,000 shares), traceable to the Note 4b PSP allotment of 1,70,747 shares. Basic = Diluted EPS (3.54/3.54 SA; 2.90/2.90 C) so zero disclosed dilutive spread despite 1,00,000 ESOP options granted 16-Jun-2026 at Rs 596.35 (Note 4a). ESOP overhang to watch. |
| A3-F12-01 | F12 | Note 7 SA/C | 284 / 583 | "The Company operates in a single reportable business segment viz, 'Mobility components, systems and sub-systems'" | NEUTRAL-FACT | Single-segment reporting folds the Escorts Kubota Railway business (acquired 01-Jun-2025, Note 2) and Novelic radar into one line. No segment assets/liabilities/revenue split disclosed, so tripwire #8 (railway delivery) and #9 (BEV mix) are NOT auditable from this filing. Disclosure limitation. |
| A3-F13-01 | F13 | Agenda item 1; Note 5; Note 6 | 28-31; 270 / 571; 280 / 581 | "considered and approved the Unaudited Financial Results (Standalone and Consolidated)" [sole agenda item] | FORWARD-SIGNAL | The material DENSO JV / stake-sale (signed 22-Jul, one day before the board) is disclosed via Note 5 only, NOT as a Board Outcome agenda item. AGM already held 15-Jul-2026 approving the Rs 1.80 dividend (Note 6) — full FY26 Annual Report exists now; schedule Role 6 AR deep dive. |
| A3-F14-01 | F14 | Sig blocks 2 & 3 vs board window | 140-144 / 397-401 vs 43-44 | consolidated report signed "2026.07.23 14:11:24"; standalone "14:40:58"; board "commenced at 2:15 p.m. ... concluded at 4:03 p.m." | AMBIGUOUS | The consolidated limited-review report was digitally signed at 14:11:24 — 4 min BEFORE the board even commenced (14:15) and 112 min before it concluded (16:03); the standalone at 14:40:58, also mid-meeting. The more material report was signed earliest of all three signature events. Could be innocent PDF-signing-vs-finalisation, but sequencing inverts the expected approve-then-sign order. A4 question. |
| A3-F14-02 | F14 | Entity #1 Annexure 1 | 427 | "Sona BLW Precisions Forgings Limited" | NEUTRAL-FACT | Holding-company name mis-spelled "Precisions" (plural) in Annexure 1 vs correct "Precision" everywhere else (lines 83, 162, 315). Individually immaterial; cumulative governance data point with the OCR-corrupted note numerals and the illegible standalone signatory. |
| A3-F15-01 | F15 | Entity #17 Annexure 1 | 445-447 | "Novelic India Private Limited* ... * incorporated as on 28 November 2025" | FORWARD-SIGNAL | Newest subsidiary in the 17-entity baseline; ties directly to Notion tripwire #3 (Novelic KAM impairment > Rs 350 Cr; FY26 loss Rs 19 Cr). No prior-quarter ledger exists, so this is flagged as FIRST_RUN_BASELINE, not a QoQ addition — future quarters diff against this list. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 Zero-value standing lines | FINDING | All 8 zero-standing rows read; Exceptional items (193/482) + Tax-prior-years (198/486) are live template lines, exceptional item primed by pending DENSO slump sale. |
| F2 Standalone vs Consolidated | FINDING | S-vs-C PAT gap swung -1.3% -> +18.9% (20.2pp); consolidated PAT Rs 415.93mn below standalone; driver = subsidiary drag + eliminated Rs 594.63mn intragroup dividend. |
| F3 Shell-entity detection | PASS | SA vs C cost lines differ materially (materials +697.20mn, employees +249.31mn, deprn +75.49mn at consolidated); subsidiaries have real operations; no shells; no going-concern EoM. |
| F4 Unaudited contribution ratio | PASS | Other Matters para 5 (372-389): 5 unreviewed subs = Rs 178.61mn revenue and a NET LOSS of Rs 29.75mn = -1.67% of consolidated PAT, well below 10%; no JV/associate share yet; baseline set (no prior to trend). |
| F5 Going concern / EoM tracking | PASS | No EoM, no Other-Matters-EoM, no going-concern para in either report (rows 78-80, 95). Note 2 "as a going concern on a slump sale basis" is the acquired-business legal descriptor, not an auditor flag. No prior quarter to verbatim-diff — noted, not skipped. |
| F6 Forward-commitment phrase mining | FINDING | "will slump sell" / "DENSO will buy" (Note 5); "approved an allotment" (Note 4b); "granted 1,00,000 ... Options" (Note 4a); "have approved a final dividend" (Note 6); "completed acquisition" (Note 2). See Commitment Register. |
| F7 Hedge phrase mining | FINDING | Note 5: "subject to fulfilment of customary conditions ... based on an independent valuer's report" (275-277/576-578) — pre-emptive cover on timing and quantum of the DENSO stake-sale gain. |
| F8 Tax forensics | FINDING | Standalone ETR 20.14% vs statutory 25.17% (~503bps shield), dividend-driven; consolidated ETR normal 25.91%. Tax-prior-year line zero in Q1FY27 but non-zero in FY26 comparatives (9.13 SA / 8.26 C). |
| F9 OCI forensics | PASS | Actuarial remeasurement negligible (SA (0.03), C (0.04)); no single-quarter OCI swing exceeds prior full year (Q1FY27 SA OCI 178.38 < FY26 263.69). Q1FY27 hedge-reserve reversal of +238.42 is MTM, not an actuarial assumption change; noted, no finding. |
| F10 Share count and dilution | FINDING | Paid-up +Rs 1.88mn QoQ traced to PSP allotment (Note 4b, 1,70,747 shares); Basic=Diluted EPS (zero spread) despite 1,00,000 ESOP options at Rs 596.35 — ongoing dilution overhang flagged. |
| F11 Reserves / net-worth tie-out | PASS | Consolidated net worth FY26 = reserves 53,610.75 + paid-up 6,218.47 = Rs 59,829mn (~Rs 5,983 Cr). No third-party number (rating/slide) in this filing to reconcile against. Standalone Total reserves blank in all columns (see F1) — cannot compute standalone net worth; noted. |
| F12 Segment forensics | FINDING | Note 7 (284/583): single reportable segment; no segment assets/liabilities/revenue split; railway (tripwire #8) and BEV mix (tripwire #9) not separately trackable from this filing. |
| F13 Board outcome beyond results | FINDING | Sole agenda item = results approval; DENSO JV disclosed via Note 5 only, not as a board-outcome item; AGM already held 15-Jul-2026 (Note 6) -> FY26 AR exists, schedule Role 6 AR deep dive. |
| F14 Note-drafting inconsistencies | FINDING | Auditor timestamp anomaly (consolidated signed 14:11:24, before 14:15 board start; standalone 14:40:58, mid-meeting) + holding-company name "Precisions Forgings" typo in Annexure 1 (427). Cumulative governance data point. |
| F15 Entity-list diffs | FINDING | No prior-quarter ledger -> no QoQ diff possible (noted, not skipped); 17-entity FIRST_RUN_BASELINE set; Novelic India Pvt Ltd (incorporated 28-Nov-2025) flagged for tripwire #3. |
| F16 Presentation-specific | N.A. | Results filing, no investor deck in scope. |
| F17 Concall silence audit | N.A. | Results filing, no transcript in scope. F6 commitments + Notion checklist carried forward to the concall run for the silence audit. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Two DENSO JVs (51:49) for EV traction motors/controllers; slump-sale of EV motors & controllers business in 100% subsidiary; DENSO buys 49% at EV Rs 17,500mn | subject to customary conditions; expected FY27 | Note 5 (L270-278 / L571-579) | initiated (signed 22-Jul-2026, "will slump sell") |
| Allotment of 1,70,747 equity shares to MD & Group CEO under Performance Share Plan 2025 | approved 05-May-2026; allotment in progress | Note 4b (L266-268 / L567-569) | underway (approved, being allotted) |
| Grant of 1,00,000 ESOP options at FMV Rs 596.35 | granted 16-Jun-2026; vesting future | Note 4a (L263-265 / L564-566) | completed (grant); vesting pending |
| Final dividend Rs 1.80/share for FY26 | approved at AGM 15-Jul-2026; payment pending | Note 6 (L280-282 / L581-582) | approved (payment pending) |
| Acquisition of Railway Business of Escorts Kubota (slump sale, Rs 16,426.32mn) | completed 01-Jun-2025 | Note 2 (L244-246 / L542-544) | completed |

---

## FOR A4 (management questions to draft)

- FORWARD-SIGNAL: A3-F1-01, A3-F2-01, A3-F6-01, A3-F13-01, A3-F15-01.
- AMBIGUOUS (convert to questions per conservative bias): A3-F7-01 (DENSO closing timeline / valuation status / P&L geography), A3-F8-01 (standalone ETR shield durability and dividend dependence), A3-F14-01 (auditor sign-off timestamp preceding board approval).

```yaml
stage: A3-forensics
company: "SONACOMS"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sona-q1fy27/work/forensics_results_sona_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F1-01", check: "F1", line: "193 / 482", classification: "FORWARD-SIGNAL", implication: "Exceptional-items line is live; DENSO slump sale is the transaction class that repopulates it"}
  - {id: "A3-F2-01", check: "F2", line: "202 / 490", classification: "FORWARD-SIGNAL", implication: "Consolidated PAT Rs 415.93mn below standalone; S-vs-C gap swung 20.2pp; subsidiary drag + eliminated intragroup dividend"}
  - {id: "A3-F6-01", check: "F6", line: "270 / 571", classification: "FORWARD-SIGNAL", implication: "Dated commitment to sell 49% of 100% EV subsidiary at valuer fair value; profit-recognition vector"}
  - {id: "A3-F7-01", check: "F7", line: "275 / 576", classification: "AMBIGUOUS", implication: "Gain on DENSO stake sale conditional on closing conditions and pending valuation; timing/quantum undefined"}
  - {id: "A3-F8-01", check: "F8", line: "200 / 488", classification: "AMBIGUOUS", implication: "Standalone ETR 20.14% vs 25.17% statutory (~503bps), dividend-dependent shield that unwinds = future ETR step-up"}
  - {id: "A3-F10-01", check: "F10", line: "218 / 514", classification: "NEUTRAL-FACT", implication: "Paid-up +Rs 1.88mn traced to PSP allotment; zero EPS spread despite 1,00,000 ESOP options at Rs 596.35 overhang"}
  - {id: "A3-F12-01", check: "F12", line: "284 / 583", classification: "NEUTRAL-FACT", implication: "Single-segment reporting hides railway (tripwire 8) and BEV mix (tripwire 9); not auditable here"}
  - {id: "A3-F13-01", check: "F13", line: "270 / 571", classification: "FORWARD-SIGNAL", implication: "Material DENSO JV disclosed via Note 5 only, not a board agenda item; AGM/dividend done -> FY26 AR exists, schedule Role 6"}
  - {id: "A3-F14-01", check: "F14", line: "140 / 397 vs 43-44", classification: "AMBIGUOUS", implication: "Consolidated auditor report signed 14:11:24, before 14:15 board start; sign-off inverts approve-then-sign sequence"}
  - {id: "A3-F14-02", check: "F14", line: "427", classification: "NEUTRAL-FACT", implication: "Holding-company name typo 'Precisions Forgings' in Annexure 1; cumulative governance data point"}
  - {id: "A3-F15-01", check: "F15", line: "445-447", classification: "FORWARD-SIGNAL", implication: "Novelic India Pvt Ltd (inc. 28-Nov-2025) baselined; ties to KAM impairment tripwire 3; no prior-quarter diff possible"}
forward_signals: ["A3-F1-01", "A3-F2-01", "A3-F6-01", "A3-F13-01", "A3-F15-01"]
ambiguous: ["A3-F7-01", "A3-F8-01", "A3-F14-01"]
commitments:
  - {commitment: "Two DENSO JVs (51:49) + slump-sale of EV motors/controllers business in 100% subsidiary; DENSO buys 49% at EV Rs 17,500mn", implied_date: "FY27, subject to customary conditions", ref: "Note 5 (L270/571)", status_word: "initiated"}
  - {commitment: "Allotment of 1,70,747 shares to MD & Group CEO under PSP 2025", implied_date: "approved 05-May-2026, allotment underway", ref: "Note 4b (L266/567)", status_word: "underway"}
  - {commitment: "Grant of 1,00,000 ESOP options at FMV Rs 596.35", implied_date: "granted 16-Jun-2026, vesting pending", ref: "Note 4a (L263/564)", status_word: "completed"}
  - {commitment: "Final dividend Rs 1.80/share FY26", implied_date: "approved AGM 15-Jul-2026, payment pending", ref: "Note 6 (L280/581)", status_word: "approved"}
  - {commitment: "Acquisition of Railway Business of Escorts Kubota (Rs 16,426.32mn slump sale)", implied_date: "completed 01-Jun-2025", ref: "Note 2 (L244/542)", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
