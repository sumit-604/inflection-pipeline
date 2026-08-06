# A3 FORENSIC NOTES — Uni Abex Alloy Products Limited (UNIABEX) — Q1 FY27 — DOCTYPE: RESULTS

Source A1 extract: `/home/user/inflection-pipeline/runs/uniabex-q1fy27/work/extract_results_uniabex_q1fy27.txt`
Source A2 ledger: `/home/user/inflection-pipeline/runs/uniabex-q1fy27/work/ledger_results_uniabex_q1fy27.md`
Coverage: new coverage (no prior-quarter extract, no companies/UNIABEX.md, no Notion tripwires). Every ledger row read verbatim at its cited line. Ledger reconciled: 100%.

Units: Rs lakhs except EPS. Statutory tax rate assumed 25.17%.

---

## KEY RECONSTRUCTED NUMBERS (from the line-item table, page 4, lines 203-250)

- Q1 FY27 (30 Jun 2026, Unaudited): Revenue 4,103.25 | Other income 681.20 | Total income 4,784.45 | Total expenses 3,810.65 | PBT before exceptional 973.80 | Exceptional NIL | PBT 973.80 | Total tax 248.35 | PAT 725.45 | OCI NIL | EPS 36.73.
- Q1 FY26 (30 Jun 2025): Revenue 3,918.27 | Other income 211.76 | PBT before exceptional 749.02 | PAT 555.84 | EPS 28.14.
- Q4 FY26 (31 Mar 2026): Revenue 7,829.03 | Exceptional gain 27,353.05 | PBT 29,930.02 | PAT 25,762.95 | EPS 1,304.45.
- FY26 (Audited): Revenue 21,878.41 | Exceptional 27,353.05 | PAT 27,986.21 | Other equity 41,262.09.

Derived (operating profit = Revenue less Total expenses, i.e. ex-other-income):
- Q1 FY27 operating profit = 4,103.25 - 3,810.65 = **292.60**.
- Q1 FY26 operating profit = 3,918.27 - 3,381.01 = **537.26**.
- Operating profit fell **-45.5% YoY** while revenue rose +4.7% and reported PAT rose +30.5%.
- Net material cost (materials consumed less inventory change): Q1 FY27 = 2,933.41 - 1,417.69 = 1,515.72 vs Q1 FY26 = 2,052.49 - 464.58 = 1,587.91 (-4.5%).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| FN-01 | F1 | Sec.1 row 16 (Exceptional item) | 223 | "Exceptional item - gain (refer note no 6) ... 27,353.05" | NEUTRAL-FACT | The Rs 27,353.05 L Thane investment-property gain sits in the Q4 FY26 / FY26 columns only; Q1 FY27 and Q1 FY26 are nil. Presentation is clean (booked as exceptional per Ind AS 1 / Schedule III, note 6, line 288). For the next three FY27 quarters, YoY PAT and EPS optics will collapse against an FY26 base carrying a one-off gain (~30x normal quarterly PAT). Comparability caution: every FY27-vs-FY26 PAT/EPS delta must be read off PBT-before-exceptional (row 15, line 222), not reported PAT. |
| FN-02 | F1 | Sec.1 row 7 (Changes in inventories FG/WIP) | 210-211 | "Changes in inventories of finished goods and work-in-progress ... (1,417.69)" | AMBIGUOUS | Inventory build of 1,417.69 L is ~3.0x the year-ago build of 464.58 L and credited that much relief into expenses. Cost of materials consumed simultaneously jumped +42.9% YoY (2,933.41 vs 2,052.49) on only +4.7% revenue. Net material cost is roughly flat (-4.5%), so the gross-margin optics of the quarter rest on an abnormally large WIP/FG build. Either a genuine production ramp / order build ahead of shipment, or profit supported by inventory timing. A4 question required: what drove the build, and does it convert to Q2 revenue? |
| FN-03 | F1 | Sec.1 rows 3 & 15 (Other income; PBT before exceptional) | 205 / 222 | "(b) Other income 681.20" ... "Profit before exceptional item and tax (1-2) 973.80" | FORWARD-SIGNAL | Other income of 681.20 L is 69.9% of the 973.80 L PBT. Operating profit ex-other-income FELL to 292.60 L from 537.26 L a year ago (-45.5%). The entire +30.5% YoY PAT beat (725.45 vs 555.84) is non-operating: the +469.44 L rise in other income alone more than explains the +224.78 L rise in PBT. The reported "profit growth" masks an operating-profit contraction. Likely driver: treasury/interest income on the ~Rs 280 crore Thane sale proceeds not yet distributed. A4: quantify recurring vs treasury other income; the operating business is not growing profit. |
| FN-04 | F6 | Sec.2 note 5 | 278-284 | "the total dividend recommended by the Board for the financial year 2025-26 aggregates to Rs. 100 per share (1000% of the face value...) ... subject to shareholders approval in the upcoming Annual General Meeting." | FORWARD-SIGNAL | FY26 dividend Rs 100/share = Rs 40 final + Rs 60 special "on account of Thane land sale". On 19.75 lakh shares (paid-up 197.50 L / Rs 10), total outflow ~Rs 1,975 L, of which the special ~Rs 1,185 L. Capital-allocation read: the land-sale windfall is being largely returned to shareholders, not redeployed into capex/M&A. AGM is a dated near-term catalyst; the special resolution set foreshadows it. |
| FN-05 | F6 | Sec.3 item b / Annexure II row 1-2 | 56-63 / 322-324 | "He will be relieved from his responsibilities with effect from closing hours of 15th September, 2026." | FORWARD-SIGNAL | Dated management commitment / milestone: Company Secretary & Compliance Officer (KMP) Mr. Bhautesh Shah exits 15 Sep 2026. Compliance-officer vacancy opens; no successor named in this filing. Track for a successor-appointment disclosure before/around 15 Sep 2026 (a gap in the statutory Compliance Officer role is itself a governance tripwire). |
| FN-06 | F8 | Sec.1 rows 20 & 21 (Deferred tax; Prior period tax adj) | 228 / 229 | "(c) Prior period tax adjustments ... (21.62)" ; "(b) Deferred tax charge/(credit) 50.94 ... (18.31)" | AMBIGUOUS | F8 mandate: prior-year tax adjustment is non-zero — (21.62) L — but sits only in the FY26 audited column, nil in Q1 FY27; immaterial. Separately, deferred tax flips sign YoY: +50.94 L charge in Q1 FY27 vs (18.31) L credit in Q1 FY26. Q1 FY27 ETR = 248.35/973.80 = 25.50%, clean and near-statutory (confirms no residual land-sale tax leaking into FY27). The deferred-tax sign flip is small; flag as a minor A4 question (timing-difference reversal driver). |
| FN-07 | F13 | Sec.3 item b + Sec.2 note 5 | 56-63 / 272-284 | "accepted and taken on record resignation letter ... of Mr. Bhautesh Shah as the Company Secretary and Compliance Officer (Key Managerial Personnel)" | FORWARD-SIGNAL | Board-outcome governance signals: (1) KMP/Compliance-Officer departure effective 15 Sep 2026, reason "to pursue growth opportunities outside the organization" (boilerplate; watch for successor). (2) Note 5's "upcoming Annual General Meeting" plus the Rs 60 special dividend imply the FY26 AGM (with dividend + special resolutions) is imminent. NOT present in the outcome letter: any Annual Report / Board's Report approval, so no Role 6 AR Deep Dive event is schedulable yet from this filing. |

---

## CHECKLIST SCORECARD (all 17; PASS / FINDING / N.A.)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING LINE ITEMS | FINDING | 6 ZERO_STANDING rows read (16, 21, 26-28, 31). Exceptional line (223) carries the Rs 27,353.05 L Thane gain in FY26 columns only — comparability distortion (FN-01); the same "what the current-quarter profit is made of" lens surfaces the inventory build (FN-02, line 210) and the other-income-dominated PBT (FN-03, line 205). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Note 7, line 290: "The Company does not have any subsidiary/associate /joint venture, hence consolidated financial results is not applicable." No S-vs-C gap can exist; correctly resolved, no forced gap. |
| F3 SHELL-ENTITY DETECTION | N.A. | No consolidation and no subsidiaries (note 7, line 290) — no cost lines to compare across entities. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | Auditor letter (pages 2-3) reviews the single standalone entity; no Other Matters paragraph, no component/JV/associate auditors (ledger sec.5, lines 124-126). Nothing rests on un-reviewed numbers. |
| F5 GOING CONCERN / EoM SCOPE | PASS | No Emphasis-of-Matter, no Other-Matters, no going-concern language in the review report (lines 154-159; ledger sec.5). Clean unmodified conclusion. No prior-quarter paragraph to verbatim-diff (new coverage); nothing present to track. |
| F6 FORWARD-COMMITMENT PHRASE MINING | FINDING | Lexicon hits: "subject to shareholders approval in the upcoming Annual General Meeting" (line 282, dividend — FN-04) and "will be relieved ... with effect from ... 15th September, 2026" (line 60/322, KMP exit — FN-05). Both dated/dateable commitments; see Commitment Register. |
| F7 HEDGE PHRASE MINING | PASS | Only "subject to" hit is procedural (dividend requires AGM approval, line 282), not a defensive hedge. No newly-added notes on revenue lumpiness, customer concentration, "no assurance", "evaluating", "exploring". No pre-emptive legal cover language. |
| F8 TAX FORENSICS | FINDING | Q1 FY27 ETR 25.50% (248.35/973.80), near statutory 25.17% — clean, no land-sale tax residue. Q4 FY26/FY26 ETR depressed (~14%) by the exceptional-gain tax treatment. F8 mandate triggered by non-zero prior-year adjustment (21.62) in FY26 column (line 229) and by deferred-tax sign flip +50.94 vs (18.31) (line 228) — both minor (FN-06). |
| F9 OCI FORENSICS | PASS | OCI nil in Q1 FY27 and Q1 FY26 (lines 236-239). The only OCI (2.72 L, defined-benefit remeasurement) sits in Q4 FY26/FY26 — standard year-end actuarial booking. No single-quarter swing exceeding prior year; no assumption-change signal in this quarter. |
| F10 SHARE COUNT AND DILUTION | PASS | Paid-up capital 197.50 L flat across all four periods (line 243). EPS row is single "Basic and diluted" (line 249) — no basic/diluted spread, no dilutive instruments. EPS 36.73 vs 28.14 YoY reconciles to PAT on 19.75 L shares. |
| F11 RESERVES AND NET WORTH TIE-OUT | PASS | Other equity 41,262.09 L (FY26 audited, line 246) + paid-up 197.50 L = net worth 41,459.59 L. Interim columns blank by convention. No third-party figure (rating rationale / slide) available in this filing to reconcile against; no computable gap. |
| F12 SEGMENT FORENSICS | N.A. | Note 3 (lines 267-269): single operating segment "Alloy and Steel Castings"; "no separate disclosures of segment information have been made." No segment asset/liability split exists to trend. |
| F13 BOARD OUTCOME BEYOND THE RESULTS | FINDING | Two agenda items only (ledger sec.3): (a) results approval, (b) KMP resignation. KMP/Compliance-Officer departure 15 Sep 2026 + imminent FY26 AGM carrying the Rs 60 special dividend (FN-07). No AR/Board's-Report approval present — no Role 6 AR event yet. |
| F14 NOTE DRAFTING INCONSISTENCIES | PASS | Note 2 (line 265) says "limited review"; auditor letter (lines 110, 129-137) says limited review — consistent, no audit/review contradiction. "Uni Abex" (branding, page 1) vs "Uni-Abex" (legal, statement) hyphenation and CIN OCR variant (PLCO0.../PLC0...) are branding/OCR artifacts, not drafting defects. Note 7 right-shifted indentation confirmed a formatting artifact of note 6 running long, not a mis-numbering (content correct). |
| F15 ENTITY LIST DIFFS | N.A. | Zero consolidation entities (note 7, line 290) and no prior-quarter ledger (new coverage). No list exists and no baseline to diff. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype = results, not a presentation/deck. |
| F17 CONCALL-SPECIFIC: SILENCE AUDIT | N.A. | Doctype = results, not a transcript. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|----------------|-------------|
| FY26 dividend Rs 100/share (Rs 40 final + Rs 60 special, Thane land sale), subject to shareholder approval | Upcoming FY26 AGM (est. Aug-Sep 2026) | Note 5, lines 278-284 | recommended / board-approved (awaiting AGM) |
| CS & Compliance Officer (KMP) Mr. Bhautesh Shah relieved of responsibilities | 15 September 2026 (closing hours) | Board outcome item (b), line 60; Annexure II, lines 322-324 | accepted / taken on record |
| Successor Company Secretary / Compliance Officer appointment | not stated in filing | (implied by KMP vacancy; not disclosed) | not yet initiated (gap to track) |

---

## FORWARD-SIGNAL / AMBIGUOUS ITEMS FLAGGED FOR A4 (management questions)

- FORWARD-SIGNAL: FN-03 (operating profit down 45.5% YoY; PAT beat is entirely non-operating / treasury income on land-sale proceeds), FN-04 (special-dividend capital allocation — windfall returned not reinvested), FN-05 (Compliance Officer vacancy 15 Sep 2026, no successor), FN-07 (KMP departure + imminent AGM).
- AMBIGUOUS: FN-02 (3x inventory build vs +42.9% materials consumed on +4.7% revenue — production ramp or earnings-quality timing?), FN-06 (deferred-tax sign flip +50.94 vs prior (18.31)).

```yaml
stage: A3-forensics
company: "UNIABEX"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/uniabex-q1fy27/work/forensics_uniabex_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: FINDING
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
  F17: N.A.
findings:
  - {id: "FN-01", check: "F1", line: "223", classification: "NEUTRAL-FACT", implication: "Rs 27,353.05 L Thane exceptional gain in FY26 columns only; FY27 YoY PAT/EPS optics collapse vs one-off base; read off PBT-before-exceptional (line 222)"}
  - {id: "FN-02", check: "F1", line: "210", classification: "AMBIGUOUS", implication: "Inventory build (1,417.69) is 3x year-ago while materials consumed +42.9% on +4.7% revenue; gross-margin optics rest on abnormal WIP/FG build; does it convert to Q2 sales?"}
  - {id: "FN-03", check: "F1", line: "205", classification: "FORWARD-SIGNAL", implication: "Other income 681.20 = 70% of PBT; operating profit ex-OI fell -45.5% YoY; entire +30.5% PAT beat is non-operating (likely treasury income on land-sale proceeds)"}
  - {id: "FN-04", check: "F6", line: "282", classification: "FORWARD-SIGNAL", implication: "Rs 100/share FY26 dividend incl Rs 60 special from Thane sale (~Rs 1,975 L outflow); windfall returned to holders not reinvested; AGM near-term catalyst"}
  - {id: "FN-05", check: "F6", line: "60", classification: "FORWARD-SIGNAL", implication: "Compliance Officer/KMP exits 15 Sep 2026; statutory Compliance Officer vacancy; no successor named; track appointment disclosure"}
  - {id: "FN-06", check: "F8", line: "229", classification: "AMBIGUOUS", implication: "Prior-year tax adj (21.62) in FY26 column (immaterial); deferred-tax sign flip +50.94 vs (18.31) YoY; Q1 FY27 ETR 25.50% clean/near-statutory"}
  - {id: "FN-07", check: "F13", line: "56", classification: "FORWARD-SIGNAL", implication: "KMP resignation + imminent FY26 AGM carrying Rs 60 special resolution; no AR/Board's-Report approval yet (no Role 6 AR event schedulable)"}
forward_signals: ["FN-03", "FN-04", "FN-05", "FN-07"]
ambiguous: ["FN-02", "FN-06"]
commitments:
  - {commitment: "FY26 dividend Rs 100/share (Rs 40 final + Rs 60 special, Thane land sale), subject to shareholder approval", implied_date: "upcoming FY26 AGM (est. Aug-Sep 2026)", ref: "Note 5, lines 278-284", status_word: "recommended"}
  - {commitment: "CS & Compliance Officer (KMP) Bhautesh Shah relieved of responsibilities", implied_date: "2026-09-15", ref: "Board outcome (b) line 60; Annexure II lines 322-324", status_word: "accepted"}
  - {commitment: "Successor Company Secretary / Compliance Officer appointment", implied_date: "not stated", ref: "implied by KMP vacancy; not disclosed", status_word: "not-initiated"}
gate_a3: pass
blank_checks: []
```
