# A3 FORENSIC NOTES — Vaibhav Global Limited (VAIBHAVGBL) — Q1 FY27 — Doctype: RESULTS (Reg 33 unaudited, Consolidated + Standalone)

Source extract: extract_results_vaibhavgbl_q1fy27.txt (654 lines, 14 pages, Lakhs).
Ledger: ledger_results_vaibhavgbl_q1fy27.md. Rows reconciled: 100% (every ledger row read verbatim at its cited line in the extract).
Prior-quarter ledger: NONE (first-time coverage). Where a prior-quarter diff is required (F5 EoM diff, F15 entity diff, F4/F8/F9 trend), the absence is stated, not invented.
Applicability: results filing -> F1-F15 apply; F16 (presentation) and F17 (concall) are N.A.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F2 | S4 r18 / S6 r18 (PAT) | 98, 275 | consol PAT "5,638.26" vs standalone PAT "1,328.03" (Q1FY27); "9,113.98" vs "14,310.74" (Q4FY26) | AMBIGUOUS | Subsidiary contribution to consol PAT swings from +76.4% (Q1FY27) to -36% (Q4FY26, standalone exceeds consol) to +3.6% (FY26). Standalone PAT is polluted by intragroup dividends / one-offs eliminated on consol. Ask mgmt to bridge standalone other income + exceptional to intragroup flows. |
| A3-02 | F4 | S8 para 7 | 400-408 | "We did not review the interim financial information of four subsidiaries ... total net profit after tax ... of Rs. 414.01 lakhs" | AMBIGUOUS | Rs 414.01L = 7.34% of consol PAT rests on other-auditor numbers (below 10% threshold, so no quantitative FINDING) BUT the four subsidiaries are NOT named -> cannot map to the 14-entity list; un-trendable (no prior ledger). Ask which 4 and their growth rate. |
| A3-03 | F6 | Note 8 (S2 r8) | 227-229 | "the ultimate outcome of the refund, if any, are not considered probable at this stage and will be accounted for in future periods" | FORWARD-SIGNAL | Rs 1,425.73L (USD 1.5M) Section 122 tariffs paid, NOT recognized as a receivable. A favourable Federal Circuit merits ruling is an unbooked future gain; adverse = permanent cost. Dateable to US court calendar. |
| A3-04 | F7 | Note 8 (S2 r8) | 223-228 | "granted the US federal government's request to stay the CIT injunction pending appeal ... the ultimate outcome ... are not considered probable at this stage" | FORWARD-SIGNAL | Pre-emptive legal hedge on a live tariff-refund contingency. Contrast with the IEEPA leg, already resolved favourably this quarter. Tracks a binary catalyst (merits panel). |
| A3-05 | F8 | S4 r16 / S6 r16 (Def tax) | 96, 273 | consol deferred tax "credit (847.92)" every period; standalone FY26 "Total tax expense (3,710.06)" (a net CREDIT) | FORWARD-SIGNAL | Persistent deferred-tax credits shield ~1,196 bps of consol Q1FY27 PBT (current-tax-only ETR 32.4% vs blended 20.4%). Consol FY26 blended ETR 5.6%; standalone FY26 ETR -16.9%. Q4FY26 carried a large DTA recognition (consol credit 4,476.21, standalone 4,753.16). ETR step-up risk once carryforwards/DTA exhaust. |
| A3-06 | F9 | S4 r21 (FX translation OCI) | 104 | "Exchange difference on translation of foreign operations (80.27)" vs "4,931.10" (Q4FY26) and "2,190.77" (Q1FY26) | FORWARD-SIGNAL | The FX-translation tailwind that added Rs 10,959.16L to FY26 net worth reversed to a Rs 80.27L loss in Q1FY27. Currency tailwind to book value has stalled; watch USD/GBP vs INR. Actuarial OCI benign (Q1FY27 47.97 vs FY26 191.90, no assumption-change swing). |
| A3-07 | F12 | S5 r9 (UK) / r11 (Europe) | 140, 142 | UK segment result "(47.48)"; Europe ex-UK "(288.50)" (Q1FY27) vs UK "978.27" / Europe "1,287.87" (Q1FY26) | AMBIGUOUS | UK and Europe (ex-UK) segment PBIT turned negative YoY; USA (5,831.98) and India (2,123.69) now carry the group. Geographic profit concentration rising. Segment assets/liabilities NOT disclosed this filing, so equity-funded-build test cannot be run. Ask mgmt UK/Europe margin trajectory. |
| A3-08 | F13 | Agenda item 4 (S1) / S7b | 42-43, 611-619 | "the appointment of Ernst & Young LLP ('EY'), as an internal auditors of the Company, for two years" | AMBIGUOUS | Internal auditor changed to a Big 4 (EY) for FY27-FY28. "Reason for change" (line 611-615) does not name the outgoing internal auditor or the trigger. Governance upgrade OR control-remediation signal. Ask who was replaced and why. |
| A3-09 | F14 | S10 entity list | 180 vs 458 | "Vaibhav Global Employee Stock Option Welfare Trust" (Note 3) vs "Vaibhav Global Employee Stock Options Welfare Trust" (Annexure I) | NEUTRAL-FACT | Entity-name drift (Option vs Options); also "Mindful Souls BV" (171) vs "B.V." (445), "Pt." (173) vs "PT." (449). Individually immaterial; cumulatively a drafting-control data point. No note-vs-letter audit/review mismatch (Note 1 "reviewed by Statutory Auditors" matches LRR "limited review"). |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-STANDING | PASS | All 4 zero-standing lines benign template lines, cited and explained: line 105 tax-on-FX-translation-OCI (never a taxable event on translation); lines 110/113/116 the three Non-controlling-interest attribution lines, dash in all 4 periods because every subsidiary is wholly owned (S10 confirms 14/14 wholly owned or controlled trust). No exceptional/discontinued-ops/profit-on-sale zero line hiding a transaction class. |
| F2 S-vs-C DECOMP | FINDING | A3-01. Subsidiary PAT share swings +76.4% / -36% / +3.6% across periods; standalone PAT exceeds consol in Q4FY26 (intragroup dividend + exceptional). Revenue: subs = 82.8% of consol Q1FY27. Gap moves >5pp of standalone PAT. |
| F3 SHELL-ENTITY | PASS | No shells. Standalone cost lines (materials 5,034.53, employees 1,768.73, deprec 200.86) are distinct from and far below consol (9,863.73 / 15,287.61 / 2,662.96); subs are live retail operations (USA seg rev 59,800.88, UK 25,007.87). The Trust (Rs Nil rev, Rs 0.49L loss) is an ESOP SPV, not an operating shell. No going-concern EoM to reconcile. |
| F4 UNAUDITED CONTRIB | FINDING | A3-02. Other-auditor-reviewed contribution Rs 414.01L PAT = 7.34% of consol PAT (below 10% quantitative threshold), Rs 10,560.67L revenue = 11.5% of consol revenue. FINDING raised on the disclosure gap (4 subsidiaries unnamed) + un-trendable (NO_PRIOR_LEDGER), not on the ratio. |
| F5 GOING CONCERN/EoM | PASS | No Going Concern paragraph in either LRR. Only "attention is drawn" balancing-figure Other-Matters paras (consol para 5 line 374; standalone para 4 line 502) — standard Q4-balancing caveat, not a going-concern or scope EoM. Verbatim QoQ diff NOT possible (NO_PRIOR_LEDGER); absence of prior comparator recorded. |
| F6 FORWARD-COMMITMENT | FINDING | A3-03 + Commitment Register below. Hits: "shall be paid" / "within 30 days" (dividend, 36-37, 196), "will be accounted for in future periods" (tariff, 228-229), "appointment ... for two years" (EY, 42-43), "board approved" grant (39-40). Status-change milestone: IEEPA refund "have filed ... received a refund" = COMPLETED this quarter (211-217). |
| F7 HEDGE PHRASE | FINDING | A3-04. "subject to the conclusion of this matter" / "not considered probable at this stage" / "if any" on the Section 122 tariff (227-229); "probability of any further litigation ... is remote" on the IEEPA leg (213-214). Note-level legal cover on a live contingency. |
| F8 TAX FORENSICS | FINDING | A3-05. Persistent deferred-tax credits every period; consol blended ETR 20.4% (Q1FY27) / 5.6% (FY26); standalone -16.9% (FY26). ~1,196 bps shield. No "tax adjustments relating to earlier years" line present (that sub-test clean). |
| F9 OCI FORENSICS | FINDING | A3-06. FX-translation OCI reversed to (80.27) from +4,931.10 (Q4FY26)/+2,190.77 (Q1FY26); FY26 tailwind +10,959.16 stalled. Actuarial remeasurement benign (no single-quarter swing exceeding full prior year). |
| F10 SHARE COUNT/DILUTION | PASS | Paid-up 3,340.48 -> 3,346.01 (+5.53L) fully traced to 276,874 ESOP shares allotted (Note 4, FV Rs2 x 276,874 = Rs 5.54L). Basic-vs-diluted EPS spread modest and stable (consol 3.37/3.33 = 1.2%; FY26 15.97/15.75 = 1.4%); no sudden widening. Fresh MSOP/RSU/ESOP grants (agenda 3) keep dilution live but unchanged in character. |
| F11 RESERVES/NET WORTH | PASS | Other Equity disclosed only for audited FY26 column (consol 1,61,452.89 + paid-up 3,340.48 = 1,64,793.37; standalone 84,162.83 + 3,340.48 = 87,503.31). Internally consistent. Quarterly Other Equity blank per interim convention. No third-party comparator (rating/slide) in filing and no prior ledger -> 5% gap test has no counterparty this quarter. |
| F12 SEGMENT FORENSICS | FINDING | A3-07. UK and Europe segment PBIT turned negative YoY; USA/India concentration rising. Segment ASSETS and LIABILITIES not disclosed in this interim filing, so the equity-funded-build / WC-unwind sub-tests are not evaluable and that absence is recorded. |
| F13 BOARD OUTCOME | FINDING | A3-08. All 4 agenda items assessed: (1) results — routine; (2) interim dividend Rs1.50, record date 12 Aug 2026 — capital-return signal; (3) MSOP/RSU/ESOP grant — dilution/governance; (4) EY internal-auditor appointment FY27-FY28 — governance change flagged. No AR/AGM approval, no director term dates, no capital-raise enabling resolution, no statutory-auditor change (BSR unchanged). |
| F14 NOTE DRAFTING | FINDING | A3-09. Entity-name drift across tables (Option/Options; BV/B.V.; Pt./PT.). No substantive note-vs-auditor-letter mismatch. OCR noise (stray "?" line 361, garbled registered-office footer 390-392) is scanning artifact, not a drafting inconsistency, and is not counted. |
| F15 ENTITY LIST DIFFS | PASS | 14-entity consolidation list captured (S10). NO_PRIOR_LEDGER -> no baseline to diff against; no addition/deletion/rename/relationship-change detectable this quarter. This list is recorded as the baseline for all future ENTITY_CHANGE diffs. Prior-quarter diff required but unavailable (stated, not invented). |
| F16 PRESENTATION | N.A. | Doctype is results filing, not an investor presentation. |
| F17 CONCALL SILENCE | N.A. | Doctype is results filing, not a transcript. Notion monitoring checklist is EMPTY (first-time coverage), so no checklist items to silence-audit. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/agenda ref | status word |
|------------|--------------|-----------------|-------------|
| Interim dividend Rs 1.50/sh (FV Rs 2) paid within 30 days of declaration | record date 12 Aug 2026; payment by ~3 Sep 2026 | agenda 2 (lines 33-37); Note 6 (194-196) | declared / approved |
| IEEPA tariff refund received Rs 3,839.90L + interest 148.04L; Rs 2,559.15L booked as other operating revenue, Rs 1,280.75L netted from inventory | current quarter (Q1FY27) | Note 8 (lines 211-217) | completed |
| Section 122 tariff refund (Rs 1,425.73L / USD 1.5M paid) accounted for in future periods subject to US courts | undated — Federal Circuit merits panel pending | Note 8 (lines 219-229) | underway / pending |
| EY appointed Internal Auditors for FY 2026-27 and FY 2027-28 | effective 4 Aug 2026 | agenda 4 (42-43); annexure (617-619) | approved / appointed |
| Grant of 93,170 MSOPs + 11,858 RSUs + 14,970 ESOPs (Rs 2 exercise) | vesting yr1-yr3 (RSU/ESOP) and 2-yr cliff (MSOP), FY27-FY30 | agenda 3 (39-40); annexure (556-584) | granted / approved |

---

## NOTES ON A2-RAISED FLAGS (explicitly closed)

- ZERO_STANDING x4 (lines 105/110/113/116): closed benign under F1 — one FX-translation-tax template line + three NCI attribution lines, all consistent with a 100% wholly-owned group. Forward note: any future subsidiary minority stake / partial IPO would first surface in the NCI lines.
- UNNUMBERED_PARA x3 (lines 369-370, 419, 532): OCR/source formatting; continuation and "conclusion is not modified" sentences. No governance issue; noted under F14 as non-substantive.
- UNNAMED_SUBSIDIARIES_IN_LRR: routed to A3-02 (F4) as AMBIGUOUS -> A4 question (which 4 of 14, and their growth).
- NO_PRIOR_LEDGER: propagated explicitly into F5, F8, F9 (trend), F11, F15 — every place a prior-quarter comparator is required is marked unavailable, none fabricated.
- No Balance Sheet / Cash Flow in filing: confirmed absent (Reg 33 quarterly P&L-only), recorded, not a silent gap.

```yaml
stage: A3-forensics
company: "VAIBHAVGBL"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/vaibhavgbl-q1fy27/work/forensics_results_vaibhavgbl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F2", line: "98,275", classification: "AMBIGUOUS", implication: "S-vs-C PAT gap swings +76.4%/-36%/+3.6%; standalone polluted by intragroup dividends and one-offs"}
  - {id: "A3-02", check: "F4", line: "400", classification: "AMBIGUOUS", implication: "4 unnamed subsidiaries = 7.34% of consol PAT, un-trendable, unmappable to entity list"}
  - {id: "A3-03", check: "F6", line: "228", classification: "FORWARD-SIGNAL", implication: "Rs 1,425.73L Section 122 tariff unbooked; future court-dated gain or permanent cost"}
  - {id: "A3-04", check: "F7", line: "227", classification: "FORWARD-SIGNAL", implication: "Legal hedge on live tariff-refund contingency; binary Federal Circuit catalyst"}
  - {id: "A3-05", check: "F8", line: "96", classification: "FORWARD-SIGNAL", implication: "Persistent deferred-tax credits shield ~1,196 bps; ETR step-up risk on carryforward exhaustion"}
  - {id: "A3-06", check: "F9", line: "104", classification: "FORWARD-SIGNAL", implication: "FX-translation tailwind to net worth stalled/reversed in Q1FY27"}
  - {id: "A3-07", check: "F12", line: "140", classification: "AMBIGUOUS", implication: "UK and Europe segment PBIT turned negative YoY; USA profit concentration rising"}
  - {id: "A3-08", check: "F13", line: "42", classification: "AMBIGUOUS", implication: "Internal auditor changed to EY; outgoing auditor/trigger undisclosed"}
  - {id: "A3-09", check: "F14", line: "180", classification: "NEUTRAL-FACT", implication: "Entity-name drift across tables; drafting-control data point"}
forward_signals: ["A3-03", "A3-04", "A3-05", "A3-06"]
ambiguous: ["A3-01", "A3-02", "A3-07", "A3-08"]
commitments:
  - {commitment: "Interim dividend Rs 1.50/sh paid within 30 days", implied_date: "record 12 Aug 2026 / pay ~3 Sep 2026", ref: "agenda 2 / Note 6 (33-37,194-196)", status_word: "declared"}
  - {commitment: "IEEPA tariff refund Rs 3,839.90L received; Rs 2,559.15L booked as revenue", implied_date: "Q1FY27", ref: "Note 8 (211-217)", status_word: "completed"}
  - {commitment: "Section 122 tariff refund accounted in future periods subject to US courts", implied_date: "undated (Federal Circuit pending)", ref: "Note 8 (219-229)", status_word: "underway"}
  - {commitment: "EY appointed Internal Auditors FY27 and FY28", implied_date: "effective 4 Aug 2026", ref: "agenda 4 / annexure (42-43,617-619)", status_word: "approved"}
  - {commitment: "Grant 93,170 MSOP + 11,858 RSU + 14,970 ESOP", implied_date: "vesting FY27-FY30", ref: "agenda 3 / annexure (39-40,556-584)", status_word: "granted"}
gate_a3: pass
blank_checks: []
```
