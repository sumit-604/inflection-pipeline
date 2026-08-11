# A3 FORENSIC NOTES — SPAPPAREL Q1FY27 (doctype: results)

Company: SP Apparels Limited (BSE 540048 / NSE SPAL)
Quarter: q1fy27 (quarter ended 30.06.2026)
Units: Rs in Millions as filed (x0.1 to Rs Crores)
Source extract: `extract_results_spapparel_q1fy27.txt` (reconciled 100% against `ledger_results_spapparel_q1fy27.md`)
Prior-quarter ledger: NOT SUPPLIED — every cross-quarter check is flagged NO_PRIOR_LEDGER, never asserted.
Thesis / Notion monitoring checklist: NONE AVAILABLE (uncovered name, no companies/SPAPPAREL.md, connector unreachable). F17 and any thesis-referencing sub-test noted explicitly, not fabricated.

Ledger reconciliation: all A2 tables (Tables 1-11), all 57 line items, 12 notes, 11 auditor paragraphs, 9 entities, 7 agenda items, 4 signature blocks read verbatim at their cited lines. 100% reconciled. All 16 A2 flags independently re-verified against the extract; findings below stand on in-document evidence, not on A2's assertion.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | Table 6a, standalone tax (b) | 357 | "(b) Short / (Excess) provision for tax relating to prior years  -  -  -  -" | NEUTRAL-FACT | Standing template line for prior-year tax true-ups; standalone booked none, but the consolidated twin (line 545) is NON-zero — subsidiaries carry prior-year tax adjustments. Cross-ref A3-08. |
| A3-02 | F2 | Table 6a L360 vs Table 8a L548 | 360 / 548 | SA PAT "26537" vs CONSOL PAT "248.74" | FORWARD-SIGNAL | Consolidated PAT is BELOW standalone in Q1FY27 (-16.63) but was ABOVE in Q1FY26 (+7.65). S-vs-C PAT gap swung ~10.1pp of standalone PAT YoY: subsidiaries + associate flipped from accretive to net dilutive. A4 question. |
| A3-03 | F4 | Table 4 para 5 & 6 | 464 / 475 | "not been reviewed by their auditor... total net loss... of Rs 74.84 million... are not material to the Group" | FORWARD-SIGNAL / AMBIGUOUS | Rs 74.84m loss NOT reviewed by any auditor = 30.1% of consolidated PAT (248.74) in magnitude; Rs 452.55m unreviewed revenue = 11.3% of consol revenue. A further Rs 201.84m rev / Rs 4.77m loss reviewed only by OTHER auditors (para 5). Management asserts immateriality on a loss = 30% of group PAT. A4 question. |
| A3-04 | F6 | Table 1 items 2-7; Table 2 row 7 | 39 / 44 / 148 / 581 | "Expected time of completion; Tentatively within 2 (two) months"; "has acquired Ritz Clothing Yapahuwa" | FORWARD-SIGNAL | Dated management commitments: split completion ~2 months post-AGM, dividend payment within 30 days of AGM, AGM 21 Sep 2026. Ritz acquisition already stated completed ("has acquired"). See Commitment Register. |
| A3-05 | F7 | Table 4 para 6 | 483 | "this interim financial results/financial information are not material to the Group" | AMBIGUOUS | Pre-emptive management hedge asserting immateriality of Rs 74.84m of UNREVIEWED subsidiary/associate losses. Legal-cover language sitting on the largest single loss item in the group. A4 question. Ties to A3-03. |
| A3-06 | F8 | Table 8a L545, L547 | 545 / 547 | "(b) Short/ (Excess) provision for tax relating to prior years  3  002  E  (3.86)" | FORWARD-SIGNAL | Consolidated carries NON-zero prior-year tax adjustments (FY26 (3.86) credit + quarterly amounts) while standalone shows all dashes (line 357). Consolidated ETR runs 29-33% (Q1FY27 30.6%) vs 25.17% statutory — subsidiary losses generate no tax shield, structurally inflating group ETR. If subsidiary losses persist, group ETR stays elevated. A4 question. |
| A3-07 | F9 | Table 8b L561, L565 | 561 / 565 | consol cash-flow-hedge "11051"; Total OCI "81.88" | FORWARD-SIGNAL | Single-quarter consolidated OCI +81.88 (driven by cash-flow-hedge effective portion +110.51) nearly equals FY26 full-year OCI of (86.48) in magnitude and reverses its sign. Actuarial component is stable (small), so the swing is forex-hedge MTM: large open hedge book, OCI can whipsaw back next quarter. Verify hedge notional/assumptions at AR. |
| A3-08 | F10 | Table 6b L387 vs Table 8b L569 | 387 / 569 | SA Q1FY26 paid-up "260.93" vs CONSOL "250.03" | NEUTRAL-FACT | Same parent, same date, paid-up capital must match. Standalone EPS 7.93 (L388) implies 198.90/7.93 = 25.08m shares = ~250.8 paid-up, matching the consolidated 250.03, NOT the standalone printed 260.93. Root cause reconciled: the standalone Q1FY26 260.93 is a "6"-for-"0" transcription error; EPS is internally correct. Resolves BOTH A2's INTER_STATEMENT_MISMATCH and its EPS ARITHMETIC_MISMATCH as one data-quality item. Low forward relevance (comparative period). |
| A3-09 | F13 | Table 1 items 2-7; Table 2 | 39 / 44 / 71 / 85 | "final dividend of Rs.3.00 per Share (30%)"; "sub-divided/split into 5 (five) equity shares... face value of Rs. 2/-"; "Alteration of SPAL Employee Stock Option Plan 2024" | FORWARD-SIGNAL | 21st AGM 21 Sep 2026 with special resolutions: 1:5 split (FV 10->2, 5x EPS/share-count restatement), MOA capital-clause alteration, ESOP scheme alteration. Dividend Rs 3 = 30% on FV. No capital-raise resolution. FY26 dividend => FY26 Annual Report drops within weeks — schedule Role 6 AR Deep Dive. A4 question. |
| A3-10 | F14 | Tables 2/8a/8b/5, headers | 69 / 124 / 547 / 567 | "given as Annexure-I" (L69) vs header "Annexure – A" (L124); "(16 = a+b+c)" beside S.No "15" (L547); "(18 =16 plus 17 plus 18)" beside S.No "19" (L567) | CONFIRMATORY-NEGATIVE | Cluster of source-document drafting inconsistencies (each immaterial, cumulatively a governance data point): annexure label mismatch; two consolidated rows where the printed formula S.No != the S.No column; entity-name variant "S.P. Apparels (International) Private Limited" (L581) vs "S.P. Apparels International (Private) Limited" (L453); CIN variant L18101TZ2005PLC012295 (L325) vs 18101TZ2005PLC012205 (L510). |
| A3-11 | F14 | Table 6a L348, L353 | 348 / 353 | unlabeled subtotal "964.50"; Total Expenses "2,413.68" | AMBIGUOUS | Standalone P&L: unlabeled subtotal (L348) computes to 954.50 vs printed 964.50, and Total Expenses (L353) computes to 2,403.68 vs printed 2,413.68 — BOTH off by exactly +10.00, same direction. Consolidated twin (L529) ties exactly, so this is not generic OCR noise: the standalone statement carries a consistent +10.00 that reconciles to no visible line item. Candidate: a dropped/omitted ~10.00 expense line. A4 question. |
| A3-12 | F15 | Table 5 row h; Note 4 | 454 / 581 | "During the quarter, SP Apparels (International) Private Limited, a subsidiary in Sri Lanka, has acquired Ritz Clothing Yapahuwa (Private) Limited" | FORWARD-SIGNAL | New step-down subsidiary this quarter via the Sri Lanka arm (2,100,004 shares at LKR 10). Expands consolidation scope/complexity; plausibly among the unreviewed loss-making entities in A3-03 (verify). Foreign-currency and component-auditor exposure rising. A4 question. |

---

## CHECKLIST SCORECARD (all 17, one status each — GATE A3)

| # | Status | Basis |
|---|---|---|
| F1 | FINDING | Standalone zero-standing prior-year tax line (L357) all dashes; exists to absorb prior-year tax true-ups; consolidated twin (L545) is non-zero. A3-01. |
| F2 | FINDING | S-vs-C PAT gap swung ~10.1pp of standalone PAT YoY (consol went from +7.65 above SA to -16.63 below SA); >5pp threshold. A3-02. |
| F3 | PASS | Not shells: COGS SA 894.79 vs CONSOL 1,340.77; Employee SA 725.37 vs 985.04 (L344/525, L349/531); highlights page gives live subsidiary revenues (SP Retail 188.3, SP UK 333.0, L230/233). Cost lines materially differ = real operations. |
| F4 | FINDING | Unreviewed-by-any-auditor loss Rs 74.84m = 30.1% of consol PAT; unreviewed revenue Rs 452.55m = 11.3% of consol revenue (L475-483). Both >10%. No prior ledger to trend (NO_PRIOR_LEDGER). A3-03. |
| F5 | PASS | Both limited-review reports carry unmodified conclusions (L292-298, L485-491); no Going Concern, no Emphasis of Matter, no Other-Matters scope beyond the two component-auditor paras. No EoM present to change; QoQ verbatim diff not runnable (NO_PRIOR_LEDGER). |
| F6 | FINDING | Multiple dated/dateable commitments in the board outcome + notes (split completion ~2 months, dividend within 30 days of AGM, AGM 21 Sep, Ritz acquisition "has acquired"). Commitment Register below. A3-04. |
| F7 | FINDING | Management immateriality hedge "not material to the Group" (L483) sitting on Rs 74.84m of unreviewed losses; other "subject to approval" hedges are corporate-action conditionality (captured F6/F13). A3-05. |
| F8 | FINDING | Consolidated prior-year tax adjustments non-zero (L545) vs standalone zero (L357); consolidated ETR 29-33% > 25.17% statutory, subsidiary losses unrelieved. A3-06. |
| F9 | FINDING | Single-quarter consol OCI +81.88 (cash-flow hedge +110.51, L561/565) ~= FY26 full-year OCI (86.48) in magnitude and opposite sign; actuarial component stable, so forex-hedge MTM. Verify at AR. A3-07. |
| F10 | FINDING | Standalone Q1FY26 paid-up 260.93 (L387) != consolidated 250.03 (L569) and != its own EPS-implied ~250.8; reconciled as a "6"-for-"0" typo. EPS spread narrow/stable (basic-diluted ~0.03-0.04). A3-08. |
| F11 | N.A. | Quarterly P&L + OCI only; no balance sheet, no Other Equity / reserves figure disclosed, no third-party net-worth (rating rationale) in context. Nothing to tie out. |
| F12 | N.A. | Single reportable segment declared (Note 3 standalone L397-399, consolidated L579-580); no segment table exists in either statement — no segment assets/liabilities/revenue to trend. |
| F13 | FINDING | Board outcome beyond results: 1:5 split, MOA alteration, ESOP alteration, Rs 3 dividend, 21st AGM 21 Sep 2026, book closure/cut-off dates; FY26 AR imminent. A3-09. |
| F14 | FINDING | Drafting inconsistencies (annexure label, formula-vs-SNo, entity-name variant, CIN variant — A3-10) plus a consistent +10.00 arithmetic gap in the standalone P&L (A3-11). |
| F15 | FINDING | New step-down subsidiary Ritz Clothing Yapahuwa acquired this quarter via Sri Lanka arm (L454, Note 4 L581). No prior ledger to confirm absence last quarter (in-document evidence: "During the quarter... has acquired"). A3-12. |
| F16 | N.A. | Doctype results. (Observed but out of scope: an embedded "Key Financial Highlights" page (L183-235) uses non-statutory "Adj. Revenue / Adj. EBITDA" metrics — L213-216; flagged to A4 for reconciliation, not scored here.) |
| F17 | N.A. | No concall transcript in scope and no Notion monitoring checklist available (uncovered name). Silence audit cannot be run; not fabricated. |

Checks marked: 17/17. Blanks: 0. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Final dividend Rs 3.00/share (30% on Rs 10 FV), FY26; paid within 30 days of AGM | record date 04.09.2026; pay by ~21.10.2026 | L39-42 | board approved (proposes to) |
| 1:5 stock split, FV Rs 10 -> Rs 2; completion "tentatively within 2 (two) months" of approval | ~Nov 2026 (post 21 Sep AGM) | L44-51, L148-150 | board approved, subject to approval |
| MOA Capital Clause (Clause V) alteration to Rs 47,25,00,000 / 23,62,50,000 shares of Rs 2 | on AGM approval 21.09.2026 | L63-65, L167-178 | board approved, subject to approval |
| Alteration of SPAL ESOP 2024 Scheme A & B (consequential to split) | on AGM approval 21.09.2026 | L71-76 | board approved, subject to approval |
| Split record date | "will be intimated in due course" (post approval) | L53-54 | pending / to be decided |
| Book closure for 21st AGM | 15.09.2026 to 21.09.2026 | L78-80 | fixed |
| Cut-off date for remote e-voting | 14.09.2026 | L82-83 | fixed |
| 21st AGM, virtual | Monday 21.09.2026 | L85-86 | will be held |
| Acquisition of Ritz Clothing Yapahuwa (Sri Lanka) by SP Apparels International, 2,100,004 shares @ LKR 10 | during Q1FY27 | L581-582 | completed ("has acquired") |

---

## NOTES FOR A4 (question-generation feed)

- FORWARD-SIGNAL findings to convert to management questions: A3-02 (subsidiary PAT drag reversal), A3-03/A3-05 (Rs 74.84m unreviewed loss vs "not material" assertion — highest priority), A3-06 (elevated consolidated ETR from unrelieved subsidiary losses), A3-07 (forex hedge book size/notional), A3-09 (split mechanics, EPS restatement, AR timing), A3-12 (Ritz / Sri Lanka expansion economics).
- AMBIGUOUS findings requiring a question rather than resolution: A3-03/A3-05 (immateriality claim), A3-11 (standalone +10.00 unreconciled expense).
- Data-quality items for source-PDF re-verification (not forward-material on their own): A3-08 (paid-up typo — already reconciled), A3-10 (annexure/formula/CIN/entity-name inconsistencies).
- Deliberately NOT asserted: any QoQ entity, EoM, or dropped-disclosure movement — NO_PRIOR_LEDGER. Any thesis/tripwire test — no monitoring checklist exists for this uncovered name.

```yaml
stage: A3-forensics
company: "SPAPPAREL"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/spapparel-q1fy27/work/forensics_spapparel_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "357", classification: "NEUTRAL-FACT", implication: "standalone prior-year tax line all-dash; consolidated twin non-zero"}
  - {id: "A3-02", check: "F2", line: "360/548", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap swung ~10.1pp YoY; subsidiaries turned net dilutive"}
  - {id: "A3-03", check: "F4", line: "464/475", classification: "FORWARD-SIGNAL", implication: "Rs 74.84m unreviewed loss = 30% of consol PAT; claimed immaterial"}
  - {id: "A3-04", check: "F6", line: "39/44/148/581", classification: "FORWARD-SIGNAL", implication: "dated commitments: split ~2mo, dividend, AGM 21 Sep, Ritz done"}
  - {id: "A3-05", check: "F7", line: "483", classification: "AMBIGUOUS", implication: "management immateriality hedge on largest group loss item"}
  - {id: "A3-06", check: "F8", line: "545/547", classification: "FORWARD-SIGNAL", implication: "consol prior-year tax non-zero; consol ETR ~30% > 25.17% statutory"}
  - {id: "A3-07", check: "F9", line: "561/565", classification: "FORWARD-SIGNAL", implication: "single-qtr OCI swing ~= full FY26 OCI; large forex hedge book"}
  - {id: "A3-08", check: "F10", line: "387/569", classification: "NEUTRAL-FACT", implication: "SA Q1FY26 paid-up 260.93 a 6-for-0 typo; reconciles EPS + inter-statement flags"}
  - {id: "A3-09", check: "F13", line: "39/44/85", classification: "FORWARD-SIGNAL", implication: "1:5 split + MOA + ESOP + Rs3 dividend at 21 Sep AGM; FY26 AR imminent"}
  - {id: "A3-10", check: "F14", line: "69/124/547/567", classification: "CONFIRMATORY-NEGATIVE", implication: "annexure/formula/CIN/entity-name drafting inconsistencies"}
  - {id: "A3-11", check: "F14", line: "348/353", classification: "AMBIGUOUS", implication: "standalone P&L consistent +10.00 gap; candidate dropped expense line"}
  - {id: "A3-12", check: "F15", line: "454/581", classification: "FORWARD-SIGNAL", implication: "new Sri Lanka step-down sub Ritz Clothing Yapahuwa acquired this quarter"}
forward_signals: ["A3-02", "A3-03", "A3-04", "A3-06", "A3-07", "A3-09", "A3-12"]
ambiguous: ["A3-05", "A3-11"]
commitments:
  - {commitment: "Final dividend Rs 3.00/share (30%) FY26, paid within 30 days of AGM", implied_date: "record 04.09.2026", ref: "L39-42", status_word: "approved"}
  - {commitment: "1:5 stock split FV Rs10->Rs2, completion tentatively within 2 months", implied_date: "~Nov 2026", ref: "L44-51,L148", status_word: "subject-to-approval"}
  - {commitment: "MOA Capital Clause alteration", implied_date: "AGM 21.09.2026", ref: "L63-65,L167", status_word: "subject-to-approval"}
  - {commitment: "SPAL ESOP 2024 Scheme A&B alteration", implied_date: "AGM 21.09.2026", ref: "L71-76", status_word: "subject-to-approval"}
  - {commitment: "Split record date to be intimated", implied_date: "post approval", ref: "L53-54", status_word: "pending"}
  - {commitment: "Book closure for AGM", implied_date: "15-21.09.2026", ref: "L78-80", status_word: "fixed"}
  - {commitment: "Cut-off date remote e-voting", implied_date: "14.09.2026", ref: "L82-83", status_word: "fixed"}
  - {commitment: "21st AGM (virtual)", implied_date: "21.09.2026", ref: "L85-86", status_word: "will-be-held"}
  - {commitment: "Ritz Clothing Yapahuwa acquisition (Sri Lanka)", implied_date: "Q1FY27", ref: "L581-582", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
