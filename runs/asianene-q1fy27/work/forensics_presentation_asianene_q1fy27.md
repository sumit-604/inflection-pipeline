# FORENSIC NOTES — Investor Presentation — Asian Energy Services Limited (ASIANENE) — Q1 FY27

Agent: A3 Forensic Notes | Model: claude-opus-4-8 | Doctype: presentation (34-page deck, Aug-2026)
Inputs reconciled: A1 extract `extract_presentation_asianene_q1fy27.txt` (1,088 lines) and A2 ledger
`ledger_presentation_asianene_q1fy27.md` (Tables 1-3, 96 number rows, 5 footnotes). Every ledger row read
verbatim at its cited line before judging. Ledger reconciliation: 100% (all Table 1 slide rows, all Table 2
number rows, all Table 3 footnotes accounted for).

Prior-quarter deck: NONE. This is the first quarterly review for the ticker. F16 dropped-slide / reframing
diffs have no baseline; per instruction I record this deck's ABSOLUTE framing choices (chart axes,
order-book definition, guidance phrasing) so the Q2 FY27 review can diff against them.

Doctype applicability applied: F16 full; F6/F7/F10 live (deck carries the phrases/numbers); F8 computed from
deck P&L; F1 live because the deck itself states the zero-standing Exceptional Item row; F14 live because
the naming inconsistency is on the deck; F3/F4/F5/F9/F11/F12/F13/F15/F17 N.A. (need the filing/concall or a
number the deck does not carry) — each marked with basis.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-1 | F1 | Tbl2 slide 12, Exceptional Item (ZERO_STANDING) | line 418 (slide 12) | "Exceptional Item 0.0 - -9.4" | AMBIGUOUS | Standing exceptional-item line prints 0.0 this quarter but FY26 full year carried a **-9.4cr** exceptional charge that the deck never explains. A4 to ask: nature of the FY26 -9.4cr item; is any recurrence expected around the Oilmax merger close? |
| F2-1 | F2 | Tbl2 slides 9,10,12 | lines 270-276, 312-317, 400-432 | "EBITDA Margin (%) 8.1% 10.5%" | FORWARD-SIGNAL | Consol EBITDA margin **fell 10.5%→8.1% YoY** while headline shouts "+81%". Standalone EBITDA margin is 10.9% (16.3/149.3); consolidated is 8.1% — the Kuiper leg added Rs 121.9cr revenue for only Rs 5.6cr EBITDA (~4.6% incremental margin). Consol PAT gap vs standalone swung from **-0.5cr in Q1FY26** (consol below standalone) to **+3.2cr in Q1FY27** — a ~41pp-of-standalone-PAT swing (>5pp threshold). Directly hits ACTIVE TRIPWIRE #5 (consol EBITDA margin <12%): it is at 8.1% this quarter (one of the two consecutive quarters needed). |
| F6-1 | F6 | Tbl2 slides 8,18,19,20,21; Tbl3 fn 2,3 | lines 205-228, 607-671, 714, 729-736 | "Merger expected to be completed by September/October 2026 subject to other regulatory clearances" | FORWARD-SIGNAL | Dense dated-commitment cluster — see Commitment Register below. Oilmax merger Sep/Oct 2026 (NCLT final hearing 28 Aug 2026); four separate "FY27 focus" production-start commitments (Amguri IGGL, Tiphuk, Duarmara, Quartzite Mine); Mewad ramp to ~1,000 bopd "FY27 onwards"; Kuiper to ~US$100Mn by FY29. Feeds Role 5 promise-vs-delivery tracker and FTTCP timeline; several map to OPTIONALITY CATALYSTS on the checklist (Duarmara, Kuiper, coal/GSECL, CBM). |
| F6-2 | F6 | Tbl2 slide 7 | lines 205-207 | "We remain confident of achieving our FY27 guidance for both Asian Energy Services and Kuiper" | AMBIGUOUS | Management reaffirms "FY27 guidance" but **no numeric guidance appears anywhere in the deck** — no revenue or EBITDA target figure. A4 to convert: what is the referenced FY27 guidance (Rs figure), and does the standalone ex-Kuiper piece meet the 30-40% order-backed guide (TRIPWIRE #4)? |
| F7-1 | F7 | Tbl2 slides 7,8,9 | lines 201-202, 238, 291 | "despite volatile Middle East situation" | AMBIGUOUS | Middle East risk hedge appears twice (CFO quote + Quarter Highlights). Paired with "Kuiper operations stabilized **in June** with profitability returning to sustainable levels" — implies Kuiper was loss-making/unstable for Apr-May of the quarter. A pre-emptive hedge on Kuiper (Middle East) revenue lumpiness/customer concentration; tells us next-quarter Kuiper is geopolitics-exposed. |
| F7-2 | F7 | Tbl2 slide 8 | line 228 | "subject to other regulatory clearances" | AMBIGUOUS | Merger-completion hedge. Sep/Oct 2026 window is conditional on unspecified further clearances beyond the 28 Aug NCLT hearing; slippage risk on the merger date that gates the dilution event (TRIPWIRE #1). |
| F10-1 | F10 | Tbl2 slide 12, EPS | line 434 | "EPS 2.53 1.24 11.43" | FORWARD-SIGNAL | Implied share count: PAT/EPS = 12.8/2.53 = **~5.06cr shares** (Q1FY27) vs 5.6/1.24 = ~4.52cr (Q1FY26) and 51.9/11.43 = ~4.54cr (FY26) — an implied **~11% share increase** between Q1FY26 and Q1FY27 that the deck never explains (no paid-up capital line, no basic-vs-diluted split, no corporate-action note). Separately, EPS growth (2.53 vs 1.24, +104%) is presented pre-Oilmax-merger; the deck shows Oilmax as a growth lever but **omits the 35-51% EPS dilution** the reverse merger implies (TRIPWIRE #1). A4: reconcile the implied ~0.5cr new shares to a corporate action; restate EPS post-merger. |
| F14-1 | F14 | Tbl1 OCR slides 5,13,22,24; Tbl2 slide 24 | lines 143, 451, 764, 808, 832 | "An Oilmax Company" | AMBIGUOUS | Deck brands AESL as "An Oilmax Company" and titles slide 24 "Oilmax-Asian and Kuiper" while the merger is only "expected to be completed by September/October 2026" and the NCLT final hearing is still pending (28 Aug). Presenting the merged entity as already existing before legal effectiveness is a cumulative governance/framing data point; A4 to note when tying the deck's platform framing to the standalone reporting entity. |
| F16-1 | F16 | Tbl2 slide 12 | lines 400-432 | "Y-o-Y 135.0% ... 81.0% ... 128.6%" | FORWARD-SIGNAL | Selective YoY disclosure: the "Y-o-Y" column prints growth only for the **favourable** lines (Revenue +135.0%, EBITDA +81.0%, Adj PBT/PBT +119.2%, PAT +128.6%) and leaves YoY **blank** for every cost line — Project Expenses (92.8→219.1, +136%), Employee (6.8→18.4, +171%), Other Expenses (4.3→12.6, +193%), Finance Cost (1.5→3.7, +147%), Tax, and EPS. Cost lines that grew FASTER than revenue carry no YoY%. Margin compression (EBITDA 10.5→8.1%, PBT 6.8→6.3%, PAT 4.9→4.7%) is present only inside the table, never in the headline. |
| F16-2 | F16 | Tbl2 slides 8,26; Tbl3 fn 1,5 | lines 249, 255, 874-898 | "*Order book represents AESL standalone and includes third-party orders only. Orders pertaining to Kuiper and Oilmax are excluded" | FORWARD-SIGNAL | BASELINE ESTABLISHED. Order book definition = **Rs 1,754cr, AESL standalone, ex-Kuiper, ex-Oilmax, third-party only, excluding GST**, split ~60% O&G (~Rs 1,055cr) / ~40% Mineral (~Rs 699cr), stated to give "2-3 years" visibility (slide 21). No "as-on" date is printed. The GSECL Rs 187.6cr order's inclusion in the 1,754cr is NOT stated. Active bidding pipeline Rs 3,000-4,000cr is explicitly INCREMENTAL (not in order book). Record verbatim so Q2 can diff for silent definition drift (gross-vs-net, executed-vs-pending, adding Oilmax/Kuiper). Mineral order book (Rs 699cr) is large vs its ~26.4cr/qtr revenue run-rate — long backlog, thin execution. |
| F16-3 | F16 | Tbl2 slides 9,10,11 | lines 270-281, 312-322, 350-388 | "(Rs in Crore)" (bar-chart clusters) | AMBIGUOUS | BASELINE FLAG. Slides 9/10/11 are bar charts (Revenue/EBITDA/PAT and segment). Axis start / bar-baseline truncation cannot be verified from pdftotext/OCR text alone. Flag for a human visual check: whether the FY26→FY27 bars use a zero baseline (a 115.4→271.2 revenue jump beside a 12.1→21.9 EBITDA bar on shared axes is a common truncation trap). Recorded as this quarter's baseline; A4/visual-review to confirm no axis game. |

---

## CHECKLIST SCORECARD (all 17 — exactly one status each)

| # | Status | One-line basis |
|---|---|---|
| F1 | FINDING | Deck states the Exceptional Item zero-standing row (line 418): Q1FY27 0.0, FY26 -9.4cr unexplained (F1-1). |
| F2 | FINDING | S-vs-C decomposed: consol EBITDA margin fell to 8.1% (vs 10.9% standalone); PAT gap swung ~41pp of standalone PAT; hits tripwire #5 (F2-1). |
| F3 | N.A. | Shell detection needs standalone cost lines; deck gives standalone Revenue/EBITDA/PAT only (slide 10), no cost breakdown to compare vs consolidated. Needs the filing. |
| F4 | N.A. | No auditor "Other Matters" in a presentation; unaudited results deck carries no component-auditor / unreviewed-contribution figure. |
| F5 | N.A. | No going-concern / EoM paragraph in the deck and no prior-quarter deck to verbatim-diff. |
| F6 | FINDING | Rich dated-commitment lexicon: merger Sep/Oct 2026, four FY27 production-starts, Mewad ~1,000 bopd, Kuiper US$100Mn by FY29; plus reaffirmed-but-unquantified FY27 guidance (F6-1, F6-2). |
| F7 | FINDING | Hedges present: "despite volatile Middle East situation" (x2) + Kuiper "stabilized in June"; merger "subject to other regulatory clearances" (F7-1, F7-2). |
| F8 | PASS | ETR Q1FY27 4.3/17.1 = 25.1% ≈ statutory 25.17%; Q1FY26 28.2%; FY26 24.7%. No deferred-tax detail or prior-year tax-adjustment line in deck; nothing anomalous. |
| F9 | N.A. | No OCI / actuarial line disclosed in the presentation. |
| F10 | FINDING | Implied share count rose ~11% (12.8/2.53=5.06cr vs 4.54cr FY26), unexplained; Oilmax 35-51% dilution omitted while EPS growth headlined (F10-1). |
| F11 | N.A. | Deck carries no net worth / other equity / reserves / paid-up capital figure to tie out against any third-party number. |
| F12 | N.A. | Deck gives segment revenue and a segment "profit" (slide 11) but NO segment assets/liabilities; the assets/liabilities trend F12 requires needs the filing. |
| F13 | N.A. | Directors listed (slide 27) without DIN/term dates; no AR/Board's-Report/AGM/record-date/board-outcome disclosed in the deck. |
| F14 | FINDING | "An Oilmax Company" branding and "Oilmax-Asian" naming used before merger legal effectiveness — cumulative governance/framing data point (F14-1). |
| F15 | N.A. | No formal consolidation entity list in the deck and no prior-quarter baseline; note for baseline: "Anirit Ventures" (line 946) appears as a group entity for the first time — capture for Q2 diff. |
| F16 | FINDING | Selective YoY on cost lines, margin compression buried, order-book definition captured as baseline, unquantified FY27 guidance, chart-axis truncation flagged for visual review (F16-1/2/3). |
| F17 | N.A. | Presentation, not a concall; silence audit runs against a transcript. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6) — dated / dateable management commitments

| commitment | implied date | slide / line ref | status word |
|---|---|---|---|
| Oilmax merger completion "subject to other regulatory clearances" | September/October 2026 | slide 8 line 228; slide 20 line 714 | underway (NCLT final hearing scheduled) |
| Oilmax merger — final NCLT hearing | 28 August 2026 | slide 8 line 226 | scheduled |
| Oilmax merger — shareholders' approval | (achieved) | slide 8 line 226; slide 6 line 164 | completed |
| GSECL coal handling plant, Ukai (Rs 187.6cr) — "Work has commenced" | FY27 execution | slide 8 lines 232-233; slide 11 line 370 | commenced/underway |
| Amguri — IGGL connections to ramp production | FY27 | slide 19 lines 669 | underway |
| Tiphuk — start commercial production (50,000 SCMD achieved in EWT) | FY27 | slide 19 lines 653, 670 | initiated |
| Duarmara — commercial production; "testing underway" (40 MMBOE) | FY27 | slide 19 lines 658-659, 670 | underway |
| Chhattisgarh CBM Block — core drilling / test-well programme, ~2-yr timeline | FY27 (drilling) / ~2yr | slide 19 lines 655, 657 | underway |
| Uttarakhand Quartzite Mine (7.6 MMT) — obtain permissions & start production | FY27 | slide 19 lines 668, 671 | initiated |
| Mewad/Indrora — scale to ~1,000 bopd; revenue increase | FY27 onwards | slide 18 lines 611-612, 632 | underway (rig mobilized) |
| Oilmax production ~2,500 → ~10,000 boepd | FY29/FY30E | slide 19 line 640; slide 21 line 729 | target |
| Kuiper revenue scale ~US$60-70Mn → ~US$100Mn | by FY29 | slide 21 lines 734-736 | target |
| Oilmax — preferred bidder DSF Round IV block + Pakro critical-mineral (Vanadium/Graphite) mine | pending award | slide 8 lines 242-243 | initiated/awarded-pending |
| "FY27 guidance for both Asian Energy Services and Kuiper" (no numeric figure given) | FY27 | slide 7 lines 205-207 | reaffirmed (unquantified) |
| Deploy similar value-chain in Mineral Assets | not dated | slide 17 line 589 | proposed |

---

## RECONCILIATION-TO-FILING FLAGS FOR A4 (arithmetic-check against the results filing)

The deck P&L is INTERNALLY consistent (EBITDA 271.2-219.1-18.4-12.6+0.8 = 21.9; walks cleanly to PAT 12.8;
FY26 and Q1FY26 columns tie within rounding; segment revenue 244.8+26.4 = 271.2 = consol revenue). A4 should
still cross-check these deck headline numbers against the filed unaudited results, and specifically:

1. **EBITDA definition quirk** — the deck's EBITDA (line 406) INCLUDES "Share of Profit/Loss from JV" Rs 0.8cr
   (line 404). EBITDA ex-JV = Rs 21.1cr; the 81.0% growth and 8.1% margin both rest on a non-standard EBITDA
   that folds in associate/JV share. Verify against the filing's EBITDA build.
2. **Implied share count** — EPS 2.53 on PAT 12.8 implies ~5.06cr shares vs ~4.54cr in FY26; reconcile the
   ~11% increase to a corporate action and confirm against the filed share capital.
3. **Segment "Profit"** — segment profit 33.3+4.7 = 38.0 does NOT reconcile to consol EBITDA 21.9 (different,
   unlabelled metric); confirm what the slide-11 "Profit" bars measure against the filing's segment note.
4. **Order book Rs 1,754cr** — standalone/ex-Kuiper/ex-Oilmax/ex-GST/third-party only; no as-on date; GSECL
   Rs 187.6cr inclusion unstated. Not in the filing (a deck-only figure) — A4 to treat as unverifiable claim.

---

## NOTES FOR NEXT QUARTER (F16 baseline, no prior deck)

- Order-book definition (verbatim): "AESL standalone ... third-party orders only. Orders pertaining to Kuiper
  and Oilmax are excluded" (line 898) + "excluding GST" (line 255). Split 60/40 O&G/Mineral, Rs 1,754cr,
  "2-3 years" visibility, no as-on date. Watch Q2 for silent broadening (adding Oilmax/Kuiper, gross-of-GST).
- Guidance phrasing (verbatim): "confident of achieving our FY27 guidance" — qualitative only, no number.
- Absolute margins this deck: consol EBITDA 8.1%, PBT 6.3%, PAT 4.7% (all down YoY). Chart axes unverified.
- Group-entity names appearing: Kuiper (integrated 1 Sep 2025), Oilmax (merger pending), Anirit Ventures
  (first mention, line 946). Establish as F15 baseline.

```yaml
stage: A3-forensics
company: "ASIANENE"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/asianene-q1fy27/work/forensics_presentation_asianene_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F1-1", check: "F1", line: "418", classification: "AMBIGUOUS", implication: "Standing exceptional-item line 0.0 this Q but FY26 carried unexplained -9.4cr; ask nature/recurrence"}
  - {id: "F2-1", check: "F2", line: "408", classification: "FORWARD-SIGNAL", implication: "Consol EBITDA margin 8.1% (down from 10.5%), Kuiper ~4.6% incremental margin; PAT S-vs-C gap swung ~41pp; hits tripwire #5"}
  - {id: "F6-1", check: "F6", line: "228", classification: "FORWARD-SIGNAL", implication: "Dated catalyst cluster: merger Sep/Oct 2026, four FY27 production-starts, Mewad 1000bopd, Kuiper US$100Mn FY29"}
  - {id: "F6-2", check: "F6", line: "205", classification: "AMBIGUOUS", implication: "FY27 guidance reaffirmed but never quantified; ask for the number and standalone ex-Kuiper split vs tripwire #4"}
  - {id: "F7-1", check: "F7", line: "291", classification: "AMBIGUOUS", implication: "Middle East hedge x2 + Kuiper 'stabilized in June' implies Apr-May instability; Kuiper revenue lumpiness/concentration"}
  - {id: "F7-2", check: "F7", line: "228", classification: "AMBIGUOUS", implication: "Merger 'subject to other regulatory clearances' - slippage risk on the date that gates dilution tripwire #1"}
  - {id: "F10-1", check: "F10", line: "434", classification: "FORWARD-SIGNAL", implication: "Implied share count +~11% unexplained; Oilmax 35-51% dilution omitted while EPS growth headlined; reconcile & restate"}
  - {id: "F14-1", check: "F14", line: "143", classification: "AMBIGUOUS", implication: "'An Oilmax Company' / 'Oilmax-Asian' branding used before merger legal effectiveness; governance/framing point"}
  - {id: "F16-1", check: "F16", line: "400", classification: "FORWARD-SIGNAL", implication: "Selective YoY: growth% shown only on favourable lines, cost lines (all up faster than revenue) blank; margin compression buried"}
  - {id: "F16-2", check: "F16", line: "898", classification: "FORWARD-SIGNAL", implication: "Order-book definition baseline (standalone/ex-Kuiper/ex-Oilmax/ex-GST/no as-on-date); watch Q2 for silent drift"}
  - {id: "F16-3", check: "F16", line: "270", classification: "AMBIGUOUS", implication: "Bar-chart axis truncation unverifiable from OCR; flag for human visual review; recorded as baseline"}
forward_signals: ["F2-1", "F6-1", "F10-1", "F16-1", "F16-2"]
ambiguous: ["F1-1", "F6-2", "F7-1", "F7-2", "F14-1", "F16-3"]
commitments:
  - {commitment: "Oilmax merger completion (subject to further regulatory clearances)", implied_date: "Sep/Oct 2026", ref: "slide 8 line 228; slide 20 line 714", status_word: "underway"}
  - {commitment: "Oilmax merger final NCLT hearing", implied_date: "28 Aug 2026", ref: "slide 8 line 226", status_word: "scheduled"}
  - {commitment: "Oilmax merger shareholders' approval", implied_date: "achieved", ref: "slide 8 line 226", status_word: "completed"}
  - {commitment: "GSECL coal handling plant Ukai (Rs 187.6cr), work commenced", implied_date: "FY27", ref: "slide 8 lines 232-233", status_word: "commenced"}
  - {commitment: "Amguri IGGL connections to ramp production", implied_date: "FY27", ref: "slide 19 line 669", status_word: "underway"}
  - {commitment: "Tiphuk start commercial production", implied_date: "FY27", ref: "slide 19 line 670", status_word: "initiated"}
  - {commitment: "Duarmara commercial production (testing underway, 40 MMBOE)", implied_date: "FY27", ref: "slide 19 lines 658-670", status_word: "underway"}
  - {commitment: "Chhattisgarh CBM core drilling/test-well programme", implied_date: "FY27 / ~2yr", ref: "slide 19 lines 655-657", status_word: "underway"}
  - {commitment: "Uttarakhand Quartzite Mine permissions & production start", implied_date: "FY27", ref: "slide 19 lines 668-671", status_word: "initiated"}
  - {commitment: "Mewad/Indrora scale to ~1,000 bopd; revenue increase", implied_date: "FY27 onwards", ref: "slide 18 lines 611-632", status_word: "underway"}
  - {commitment: "Oilmax production ~2,500 to ~10,000 boepd", implied_date: "FY29/30E", ref: "slide 19 line 640; slide 21 line 729", status_word: "target"}
  - {commitment: "Kuiper revenue scale to ~US$100Mn", implied_date: "by FY29", ref: "slide 21 lines 734-736", status_word: "target"}
  - {commitment: "Oilmax preferred bidder DSF Round IV + Pakro critical-mineral mine", implied_date: "pending award", ref: "slide 8 lines 242-243", status_word: "initiated"}
  - {commitment: "FY27 guidance (unquantified) for AESL and Kuiper", implied_date: "FY27", ref: "slide 7 lines 205-207", status_word: "reaffirmed"}
gate_a3: pass
blank_checks: []
```
