# A3 FORENSIC NOTES — DHANBANK (Dhanlaxmi Bank Ltd) Q1 FY27 — DOCTYPE: results

Source extract: `runs/dhanbank-q1fy27/work/extract_results_dhanbank_q1fy27.txt` (369 body lines, 7 pages).
Ledger contract: `runs/dhanbank-q1fy27/work/ledger_results_dhanbank_q1fy27.md`.
Unit basis: Rs Lakh as printed (÷100 for Rs Crore). STANDALONE only (no subsidiaries/associates — extract lines 37-42).
Ledger reconciliation: 100% — every row in A2 Tables 1-9 was read at its cited extract line before judging.
Lender variant applied (scheduled commercial bank): F4 repurposed to asset-quality/provisioning; F5/F12 emphasised.

LOOP-BACK CORRECTION (A5 pass): A5 adversary found one coverage gap — two enumerated analytical-ratio rows (L281 Debt-Equity, L282 Total-Debts/Total-Assets) were read by A2 but not converted into a forensic finding, and together they disclose the TENOR of the +104% YoY borrowings jump. Closed here as **FN14** (MON-5 funding lane, cross-referenced to FN12). No F1-F17 status changes; the passing checks are untouched. GATE A3 re-satisfied below.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN1 | F4 (lender: provisioning) | P&L row 8 | 257 | "8. Provisions (other than tax) and Contingencies 1.591 3.471, 2,110 7.806" | FORWARD-SIGNAL | Provision charge cut 54% QoQ (3,471→1,591) and 25% YoY while GNPA is flat (28,638→28,657). ~Rs 1,880 lakh of the QoQ PBT delta vs a normalised charge is provision-light. Question the run-rate: is Rs 1,591 lakh sustainable or does it borrow from next quarter? |
| FN2 | F4 (lender: coverage) | Ratios 17(iv)a/b; Note 12 | 275-276, 464 | "Provision coverage ratio (including Technical Write off)...is 92.77 %" | NEUTRAL-FACT (confirmatory-positive) | Standard PCR ex-technical-write-off = 1−7,261/28,657 = 74.66% (Mar-26: 73.67%), far above the 53.63% Dec-25 low. Net NPA% 0.47% < 1.11% falsifier. FLAG-CASH falsifier NOT triggered; coverage improved. |
| FN3 | F8 (tax) | P&L row 11 | 261 | "11. Tax expense 1,063 3,547 - 3.547" | FORWARD-SIGNAL | Q1FY26 carried NIL tax on Rs 1,218 lakh PBT (0% ETR); Q1FY27 ETR = 1,063/3,554 = 29.9% (Q4FY26 44.9%, FY26 25.66%). The comparator base was tax-free, so PBT +192% YoY converts to PAT only +104% YoY. Tax normalisation is a structural RoE drag not present in FY26 optics. |
| FN4 | F11 (net worth) | Ratio 17(vi); BS L1/L2; Note 5 | 280, 354-355, 387 | "Net Worth 130887..." / "existing balance of Rs 3068 la[k]hs in the IFR has been transferred to accumulated balance in Profit & Loss Account" | AMBIGUOUS | Regulatory Net Worth 1,30,887 vs book equity (Capital 39,470 + Reserves 1,11,851 = 1,51,321) — gap Rs 20,434 lakh (13.5% > 5% threshold). Candidate reconciling items: revaluation reserve, DTA deduction, intangibles. IFR Rs 3,068 lakh released to distributable reserves this quarter (within-equity reclassification, not P&L income). Verify composition at AR. |
| FN5 | F12 (segment) | Segment Results 2c | 305 | "(c) Corporate/ Wholesale Banking 175 1,097 (739) (875)" | FORWARD-SIGNAL | Corporate/Wholesale swung from FY26 full-year loss (875) and Jun-25 loss (739) to a thin +175 lakh on Rs 4,77,897 lakh assets (≈0.04% return). Recovery is real but fragile and QoQ decelerating (1,097→175). Monitor for relapse. |
| FN6 | F12 (segment) | Segment Assets/Liab 3d/4d | 317, 324 | "(d) Other Banking Operations - , - -" | NEUTRAL-FACT | Other Banking Operations reports Revenue 309 and Result 309 (identical, line 297/306 — no cost/provision allocated) with NIL allocated assets and liabilities. Consistent with a pure fee/commission segment; not a balance-sheet build. No action. |
| FN7 | F14 (drafting) | Table 9 audit-status | 240, 292, 352 | p4: "Unaudited Audited Unaudited Audited" / p5: "Audited Unaudited Audited Audited" | NEUTRAL-FACT | A2's inversion flag RESOLVED: the segment table header (line 292) is the typo. Correct status for 30.06.2026 is Unaudited — confirmed by cover letter ("Unaudited Financial Results", line 119), auditor limited-review report (line 156-163), and Balance Sheet header (line 352 "Unaudited Unaudited Audited"). Governance data point, no number impact. |
| FN8 | F14 (drafting) | Segment Assets Tot vs BS Tot | 319, 359 | "Total 22,12,624 21,23,765 18,70,020" vs BS "Total 22,12,624 18,70,019 21.,23,766" | NEUTRAL-FACT | A2's Rs 1 lakh flag CONFIRMED: Segment Assets Total vs BS Total differ by exactly Rs 1 lakh in Mar-26 (21,23,765 vs 21,23,766) and Jun-25 (18,70,020 vs 18,70,019); Jun-26 ties exactly. Rounding in one source table. Immaterial. |
| FN9 | MON-1 (cost-to-income) | P&L rows 1,2,4,5 | 241,247,249,250 | "5. Operating expenses (a) + (b) 16,106..." | AMBIGUOUS | LOAD-BEARING TEST. C/I = 16,106/(NII 17,762 + Other income 3,489 = 21,251) = **75.79%**. Lands BETWEEN the 75% (supports recovery) and 80% (Q4 one-off) tripwires. Improved YoY (Q1FY26 81.35%) but deteriorated hard from Q4FY26 55.66%. Q4's 55.66% was flattered by Rs 6,929 lakh other income; normalised run-rate sits ~76%. Neither thesis confirmed nor falsified — escalate to A4. |
| FN10 | MON-1 (operating profit) | P&L rows 2,5a,7 | 247, 251, 255 | "7. Operating Profit(+)/Loss(-) before provisions...5,145 11,367 3,328 21,628" | FORWARD-SIGNAL | Pre-provision operating profit HALVED QoQ (11,367→5,145, −55%), driven by other income collapse (6,929→3,489, −50%, line 247) and employee cost jump (7,104→9,298, +31%, line 251). Q4 was the outlier, not the trend; other-income normalisation is the swing factor. |
| FN11 | MON-6 (RoA) | Ratio 17(v) | 279 | "(v) Return on Assets (average) - (Annualized) 0.45% 0.84% 0.27% 0.53%" | FORWARD-SIGNAL | Annualised RoA 0.45% is BELOW the 0.6% tripwire AND below the FY26 0.53% level; down from Q4 0.84%. Tripwire breached. Consistent with provision-light PBT (FN1) plus tax normalisation (FN3) plus other-income drop (FN10). |
| FN12 | MON-5 (funding) | BS L4/L1 | 357, 354 | "Borrowings 85,871 41,996 73,663" | FORWARD-SIGNAL | Borrowings +104% YoY (41,996→85,871) and +16.6% QoQ (73,663→85,871); Total-Debt/Total-Assets 3.88% vs 2.25% Jun-25 (line 282). Paid-up capital unchanged at 39,470 (line 354) — funded by borrowings, not equity. No QIP/rights (RoE-reset tripwire NOT triggered). Watch cost of funds and NIM. **Tenor of the jump is now resolved — see FN14: the increase is essentially all short-tenor (<1yr residual).** |
| FN13 | MON-4 (advances) | BS A4 | 364 | "Advances 15,57,166 12,21,820 14,91,806" | AMBIGUOUS | Advances +27.4% YoY (above 20% tripwire — supports thesis) and +4.4% QoQ. But NO gold-loan / LTV / product-mix disclosure anywhere in this filing (NOT_FOUND). Growth composition unverifiable from the print — A4 question for the concall. |
| FN14 | MON-5 (funding; sharpens FN12) | Ratios 17(vii)&(viii) + footnotes **/***; BS Borrowings | 281, 282, 223, 224, 357 | "(vii) Debt Equity Ratio (in times) ** 0.11 0.12 0.13 0.12" / "(viii) Total Debts to Total Assets*** 3.88% 3.47% 2.25% 3.47%" / "**Debi represents borrowings with residual maturity of more than one year." | FORWARD-SIGNAL | TENOR DECOMPOSITION of the +104% YoY borrowings jump. The two disclosed gauges move in OPPOSITE directions YoY: the >1yr-residual measure (Debt-Equity, footnote ** line 223) FELL 0.13→0.11 (−15%), while total-borrowings-to-assets (footnote *** = total borrowings, line 224) ROSE 2.25%→3.88% (+163 bps) — on Borrowings +104% YoY (41,996→85,871 lakh, i.e. +Rs 438.75 Cr, L357). Reconciling arithmetic: implied >1yr borrowings ≈ 0.11 × Net Worth 1,30,887 = ~Rs 144 Cr (Jun-26) vs 0.13 × 1,18,804 = ~Rs 154 Cr (Jun-25) — flat-to-slightly-DOWN; robust to using book equity as denominator (~Rs 166 Cr vs ~Rs 183 Cr). Therefore essentially the ENTIRE +Rs ~439 Cr YoY borrowings increase is SHORT-TENOR (<1yr residual maturity); short-tenor borrowings roughly ~2.7× YoY (~Rs 266 Cr → ~Rs 715 Cr). This is a DISCLOSED funding-durability / rollover / repricing risk sitting under FN12's funding-mix shift. It REFUTES any "tenor undisclosed" framing — the tenor IS disclosed, via these two ratios plus footnotes L223/L224. A4: cost-of-funds/NIM sensitivity and rollover-concentration question. |

---

## CHECKLIST SCORECARD (F1-F17 — every check an explicit status)

| F# | Status | One-line basis |
|---|---|---|
| F1 | PASS | All 24 ZERO_STANDING rows read (Exceptional/Extraordinary items lines 258/263; GoI Nil line 269; 10 segment nil rows; 11 Note-11 nil rows). All are standard template/regulatory-disclosure lines. Exceptional/Extraordinary correctly nil — the Rs 3,068 lakh IFR release was routed through reserves (Note 5, line 387), not the exceptional line. Note 11 nil rows = zero resolution-plan failures (positive). Nothing anomalous. |
| F2 | N.A. | No consolidated statements exist or are expected — standalone-only entity, no subsidiaries/associates (extract lines 37-42; ledger line 2). S-vs-C gap uncomputable. |
| F3 | N.A. | No subsidiaries to test for shell characteristics; no consolidated cost lines. |
| F4 | FINDING | Lender variant (asset-quality/provisioning): FN1 (provision charge −54% QoQ) and FN2 (PCR). Standard component-auditor unaudited-contribution test is N.A. (standalone; only carve-out is unreviewed Pillar 3 web disclosures — para 1 line 160-163 / Note 9 line 399-402 — which do not contribute to PAT). |
| F5 | PASS | Auditor conclusion unmodified — "nothing has come to our attention that causes us to believe..." (para 5, lines 211-219). No Emphasis of Matter, Other Matters, or Going Concern paragraph (ledger confirms 5 paras, none EoM). No prior-quarter EoM to diff. |
| F6 | PASS | No open forward-dated management commitments in the notes. Lexicon hits are completed actions or boilerplate: IFR "has been transferred" (completed), Note 4 "implemented prospectively...when it becomes applicable" (boilerplate), Note 8 net profit "has considered...as part of regulatory capital" (completed). Milestones logged in the Commitment Register below. |
| F7 | PASS | No new pre-emptive hedge language in notes about revenue lumpiness, customer concentration, or asset quality. Only boilerplate "to the extent applicable" (Note 3, line 380). No newly-added risk hedge vs a standard results note. |
| F8 | FINDING | FN3 — ETR 0% (Q1FY26) → 44.9% (Q4FY26) → 29.9% (Q1FY27); nil tax on positive PBT in the year-ago comparator (line 261) inflates YoY PAT-growth optics; tax normalisation is a forward RoE drag. No "tax adjustments relating to earlier years" line; deferred-tax not separately split in this interim format. |
| F9 | N.A. | Interim bank results in this format carry no OCI / actuarial gains-losses line; not disclosed at Q1. Verify assumptions at Annual Report. |
| F10 | PASS | Paid-up capital constant 39,470 across all four periods (line 265) — no corporate action. Basic EPS = Diluted EPS every period (0.63/0.63, 1.10/1.10, 0.31/0.31, 2.60/2.60; lines 272-273) — zero dilution spread, no dilutive instruments live. |
| F11 | FINDING | FN4 — regulatory Net Worth 1,30,887 vs book equity 1,51,321, 13.5% gap (>5%); IFR Rs 3,068 lakh reclassified into distributable reserves. Candidate reconciling items listed; verify at AR. |
| F12 | FINDING | FN5 (Corporate/Wholesale fragile swing from FY26 loss to thin +175) and FN6 (Other Banking Operations revenue with nil allocated assets/liabilities). All segment liabilities positive and growing — no equity-funded-build or WC-unwind signal. |
| F13 | PASS | Single agenda item — approval of Q1 FY27 results (cover letter lines 119-124; ledger agenda_items=1). No AR/Board's-Report approval, no AGM notice, no record date, no dividend, no director appointment/term, no capital-raise enabling resolution. Nothing to schedule for Role 6. Board meeting 12:00-12:45 (line 125). |
| F14 | FINDING | FN7 (audit-status label inversion p4 vs p5 — resolved as a segment-header typo) and FN8 (Rs 1 lakh Segment-vs-BS total difference — confirmed rounding). Minor source typos also noted: interest-earned formula "(a)+(b)+(e)+(d)" (line 241) and segment-assets sub-label "(e) Corporate/Wholesale" (line 316) both mis-letter "(c)"→"(e)"; ratio footnotes "Debi" (line 223) and "banic" (line 224) OCR-garbled. Cumulative governance data point. |
| F15 | N.A. | No prior-quarter ledger supplied (PRIOR_LEDGER_PATH not provided); standalone single reviewed entity + 2 audit firms (ledger line 236). No consolidation list to diff. |
| F16 | N.A. | Doctype is a results filing, not an investor presentation. |
| F17 | N.A. | No concall transcript in scope this run. Notion monitoring-checklist tripwires are tested in the section below and fed forward to A4/A5 in lieu of a silence audit. |

GATE A3: PASS — all 17 checks carry an explicit status; every FINDING (FN1-FN14) cites a line number. The A5 loop-back gap is closed at FN14 (line-cited L281/L282/L223/L224/L357); no check left blank.

---

## COMMITMENT REGISTER (from F6 — milestone/status words for the Role 5 promise-vs-delivery tracker)

| commitment / event | implied date | note / line ref | status word |
|---|---|---|---|
| IFR discontinued; Rs 3,068 lakh transferred to accumulated P&L balance (per RBI Investment Portfolio 2nd Amendment Directions 2026, dated 18-May-2026) | during Q1 FY27 | Note 5, line 385-388 | completed |
| Net profit for the quarter included in regulatory capital per extant RBI guidelines | during Q1 FY27 | Note 8, line 397 | completed |
| Pillar 3 disclosures (Leverage, LCR, NSFR) placed on Bank website (not auditor-reviewed) | as at 30-Jun-2026 | Note 9, line 399-402 | completed |
| 3 project accounts (Rs 586.71 lakh) — DCCO achieved during the quarter | during Q1 FY27 | Note 11 SI 3, line 434-435 | completed |
| 7 project accounts (Rs 1,937.94 lakh) — resolution plan implemented (DCCO extension) | during Q1 FY27 | Note 11 SI 5.1, line 439-440 | completed |
| Loan transfers / acquisitions / co-lending arrangements | during Q1 FY27 | Note 10 (i)-(iii), lines 415-421 | none (nil-activity negative assurance) |

No open forward-dated commitment (no "will be", "expected by", "proposes to", "board has approved [future action]") in the notes.

---

## NOTION MONITORING CHECKLIST — TESTED AGAINST THIS PRINT (7 pre-committed tripwires)

1. **Cost-to-income (LOAD-BEARING).** Q1 FY27 = 16,106 / 21,251 = **75.79%** (FN9). Between the 75% support and 80% one-off lines. Q4FY26 55.66% confirmed as an other-income-flattered outlier; the recovery is partial, not clean. → AMBIGUOUS, A4 question.
2. **PCR ex technical write-off.** Computed 74.66% (Jun-26) vs 73.67% (Mar-26) — above the 53.63% Dec-25 low. Reported PCR incl. tech w/o = 92.77% (Note 12, line 464). Coverage improving (FN2). PASS the tripwire.
3. **Net NPA% / GNPA%.** Net NPA 0.47% < 1.11% and GNPA 1.82% < 1.89% (lines 277-278). FLAG-CASH falsifier (PCR ex-w/o <53.63% AND net NPA >1.11%) NOT triggered. PASS.
4. **Advances growth YoY.** +27.4% (line 364), above 20% (FN13). No gold-loan / LTV disclosure (NOT_FOUND) → AMBIGUOUS, A4 question on mix.
5. **Capital raise / borrowings.** No QIP/rights — paid-up flat 39,470 (line 354); RoE-reset tripwire NOT triggered. Borrowings +104% YoY (FN12) → FORWARD-SIGNAL on funding mix / cost of funds. **TENOR now decomposed (FN14): the >1yr-residual gauge (D/E, L281) FELL 0.13→0.11 while total-borrowings/assets (L282) ROSE 2.25%→3.88%, so essentially the entire +Rs ~439 Cr YoY increase is short-tenor (<1yr residual) — a disclosed rollover/repricing/funding-durability risk, tenor DISCLOSED via footnotes L223/L224.** → FORWARD-SIGNAL.
6. **RoA annualised.** 0.45% (line 279) — BELOW the 0.6% tripwire and the FY26 0.53% level (FN11). Tripwire BREACHED → FORWARD-SIGNAL.
7. **Provisions QoQ/YoY & technical write-off pool.** Provisions 1,591 vs 3,471 QoQ / 2,110 YoY — down on both (FN1) → FORWARD-SIGNAL. Technical write-off pool movement not separately disclosed (only the 92.77% PCR-incl-w/o point estimate, Note 12); absolute pool NOT_FOUND → A4 question.

Standard forensic net (also run): 24 zero-standing lines cleared (F1); Board Outcome has no agenda item beyond results item 1 (F13); no open forward-commitment phrases in notes (F6); auditor limited-review conclusion unmodified with no EoM/qualification (F5, lines 211-219); STANDALONE-only confirmed (lines 37-42); Corporate/Wholesale segment profitability confirmed as a fragile turnaround from FY26 loss (FN5).

A2-raised items — dispositions: (a) audit-label inversion RESOLVED as a page-5 segment-header typo, current quarter is Unaudited (FN7); (b) Note 10 read in full — negative-assurance disclosure: no loan transfers, no loan acquisitions, no co-lending arrangements during the quarter (lines 415-421); (c) Rs 1 lakh Segment-vs-BS total difference CONFIRMED as rounding in Mar-26 and Jun-25 columns (FN8); (d) closing signatory name NOT_FOUND / garbled (lines 474-477), role "Director & CEO" recoverable (line 477 ":ctor & CE0") — not reconstructed, no estimate; (e) [A5 loop-back] analytical-ratio rows 17(vii)/(viii) (L281/L282) with footnotes ** and *** (L223/L224) CONVERTED to a forensic finding — FN14, funding-tenor decomposition, sharpening FN12.

---

```yaml
stage: A3-forensics
company: "DHANBANK"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/dhanbank-q1fy27/work/forensics_dhanbank_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: FINDING
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FN1", check: "F4", line: "257", classification: "FORWARD-SIGNAL", implication: "Provision charge -54% QoQ while GNPA flat; PBT is provision-light, run-rate sustainability in question"}
  - {id: "FN2", check: "F4", line: "275-276,464", classification: "NEUTRAL-FACT", implication: "PCR ex-write-off 74.66% vs 53.63% low; FLAG-CASH falsifier not triggered, coverage improving"}
  - {id: "FN3", check: "F8", line: "261", classification: "FORWARD-SIGNAL", implication: "Nil-tax Q1FY26 comparator + ETR normalisation to 29.9% is a structural RoE/PAT-growth drag"}
  - {id: "FN4", check: "F11", line: "280,354-355,387", classification: "AMBIGUOUS", implication: "13.5% net-worth-vs-book-equity gap plus Rs 3,068L IFR release to reserves; reconciling items undisclosed"}
  - {id: "FN5", check: "F12", line: "305", classification: "FORWARD-SIGNAL", implication: "Corporate/Wholesale fragile swing from FY26 loss to thin +175L, QoQ decelerating; relapse risk"}
  - {id: "FN6", check: "F12", line: "317,324", classification: "NEUTRAL-FACT", implication: "Other Banking Operations is pure-fee segment, revenue with nil allocated assets/liabilities; no build"}
  - {id: "FN7", check: "F14", line: "240,292,352", classification: "NEUTRAL-FACT", implication: "Audit-status label inversion is a page-5 segment-header typo; current quarter is Unaudited (resolved)"}
  - {id: "FN8", check: "F14", line: "319,359", classification: "NEUTRAL-FACT", implication: "Rs 1 lakh Segment-vs-BS total difference confirmed as rounding in Mar-26 and Jun-25 columns"}
  - {id: "FN9", check: "MON-1", line: "241,247,249,250", classification: "AMBIGUOUS", implication: "Load-bearing C/I 75.79% lands between 75% and 80% tripwires; recovery partial not clean"}
  - {id: "FN10", check: "MON-1", line: "247,251,255", classification: "FORWARD-SIGNAL", implication: "Pre-provision operating profit halved QoQ on other-income collapse and employee-cost jump"}
  - {id: "FN11", check: "MON-6", line: "279", classification: "FORWARD-SIGNAL", implication: "RoA 0.45% breaches the 0.6% tripwire and is below FY26 0.53%"}
  - {id: "FN12", check: "MON-5", line: "357,354", classification: "FORWARD-SIGNAL", implication: "Borrowings +104% YoY with no equity raise; funding-mix shift, cost-of-funds/NIM watch; tenor resolved by FN14"}
  - {id: "FN13", check: "MON-4", line: "364", classification: "AMBIGUOUS", implication: "Advances +27.4% YoY above tripwire but no gold-loan/LTV mix disclosure; composition unverifiable"}
  - {id: "FN14", check: "MON-5", line: "281,282,223,224,357", classification: "FORWARD-SIGNAL", implication: "Debt-Equity (>1yr-residual) FELL 0.13->0.11 while Total-Debt/Assets ROSE 2.25%->3.88% YoY; so ~all of the +Rs 439 Cr / +104% YoY borrowings rise is SHORT-TENOR (<1yr) - disclosed rollover/repricing/funding-durability risk; sharpens FN12; refutes 'tenor undisclosed'"}
forward_signals: ["FN1", "FN3", "FN5", "FN10", "FN11", "FN12", "FN14"]
ambiguous: ["FN4", "FN9", "FN13"]
commitments:
  - {commitment: "IFR discontinued; Rs 3,068L transferred to accumulated P&L balance", implied_date: "Q1 FY27", ref: "Note 5 line 385-388", status_word: "completed"}
  - {commitment: "Net profit for quarter included in regulatory capital", implied_date: "Q1 FY27", ref: "Note 8 line 397", status_word: "completed"}
  - {commitment: "Pillar 3 disclosures placed on Bank website (unreviewed)", implied_date: "as at 30-Jun-2026", ref: "Note 9 line 399-402", status_word: "completed"}
  - {commitment: "3 project accounts (Rs 586.71L) DCCO achieved", implied_date: "Q1 FY27", ref: "Note 11 SI3 line 434-435", status_word: "completed"}
  - {commitment: "7 project accounts (Rs 1,937.94L) resolution plan implemented", implied_date: "Q1 FY27", ref: "Note 11 SI5.1 line 439-440", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
