# A3 FORENSIC NOTES — MAPMYINDIA (C.E. Info Systems Ltd) — Q1 FY27 — DOCTYPE: PRESENTATION

Source extract: `/home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/extract_presentation_mapmyindia_q1fy27.txt`
Ledger reconciled: `/home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/ledger_presentation_mapmyindia_q1fy27.md`
Ledger reconciliation: 100% (all 8 ledger tables read at cited lines: 30 line items, 60 chart labels, 32 narrative numbers, 4 notes, 4 governance disclosures, 7 TOC items, 17 slides). No prior-quarter deck supplied — F16 dropped-disclosure checks are diffed against the FY26 Notion baselines, and absence-of-disclosure findings are marked as un-confirmable-by-verbatim-diff, not invented.

Doctype scope applied per instruction: F16 is the primary check; F6/F7/F12(partial)/F13/F14 carry live findings; balance-sheet checks F2-F5, F8, F9, F11, F15 are N.A.; F10 N.A. (no share-count/EPS/dilution numbers); F17 N.A. (no transcript). Every check is marked; none blank (GATE A3).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| MMI-01 | F16 | Table 6 #2 (SEGMENT_FRAMEWORK_CHANGE) | slide 4 line 194 / slide 10 lines 437-447 | "instead of the previously reported A&M and C&E market segments" | AMBIGUOUS | Market-view segmentation switched from 2 segments (A&M, C&E) to 3 (AEG) mid-thesis. AEG comparatives ARE restated FY25/FY26 (slide 11), and Government is now broken out separately — a gain for monitoring item 1. But no A&M/C&E->AEG bridge is given, the old series is discontinued, and any reclassification cannot be audited from the deck. Re-baseline items 1 and 5; ask management for the mapping. -> A4 question. |
| MMI-02 | F16 | Table 3 (chart data labels) | slides 12/13/14 lines 557, 601, 645 | Government chart "gridline labels: 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10"; Enterprise "70, 68 ... 52, 50"; Automotive "65, 60 ... 40, 35" | CONFIRMATORY-NEGATIVE | All three AEG market-revenue bar charts use truncated y-axes (Automotive base 35, Enterprise base 50, Government base 10), not zero. This visually amplifies modest YoY growth — most starkly Enterprise (60.6->64, only +6%) which looks like a large bar step. Presentation optics only; numbers in Tables 2C-2E are authoritative. Flag for A4. |
| MMI-03 | F16 (+F14) | Table 2D line 493 / Table 2E line 506 / Table 4 line 186 | slide 14 line 614 | "the Government business grew at 11% on a YoY basis" | FORWARD-SIGNAL | Disclosed figures are Q1FY26 15.3 (line 493) -> Q1FY27 16.7 (line 506) = +9.2%. The 11% callout reconciles only if computed off the rounded chart bar "17", inflating growth ~2pp. Automotive (58.8/45.7=29%) and Enterprise (64.2/60.6=6%) callouts reconcile exactly; Government is the sole inflated one — and it is monitoring item 1 (target 15-20% YoY). Actual 9.2% is far below target; even the claimed 11% misses. Selective rounding on the most-watched, weakest segment. -> A4 question. |
| MMI-04 | F12 (partial) | Table 2B lines 406-408 / Table 4 lines 421-423 | slide 9 lines 408, 421 | "51.4% ... 54.8% ... 13.1% ... 8.7%"; "IoT-led business revenue grew 75% YoY to ₹41.1 crore" | FORWARD-SIGNAL | Product-mix margin dilution is structural: IoT revenue share rose to 29.4% (41.1/139.7) from 19.2% (23.4/121.6); Map-led EBITDA margin fell to 51.4% from 54.8% (-340bps, partly the Rs4Cr write-off), IoT margin 13.1% vs 8.7%. As low-margin IoT scales 75% YoY, blended EBITDA margin compresses. Monitoring item 4 (blended margin >38% for two quarters) at structural risk. Segment ASSETS/LIABILITIES are not disclosed in the deck (that half of F12 is N.A.). -> A4 question. |
| MMI-05 | F16 | Table 2A lines 274-285 | slide 6 lines 264, 279, 281 | headline: "Revenue grew 14.9% ... PAT rose by 8.6% YoY"; table: "EBITDA 56.1 55.9 0.4%"; "40.2% 45.9%" | FORWARD-SIGNAL | Deck headlines Revenue +14.9% and PAT +8.6% but de-emphasises EBITDA +0.4% (flat) and a 570bps EBITDA-margin compression (45.9%->40.2%). Other income (Total Income 159.4 minus Rev 139.7 = 19.7 Cr vs 135.3-121.6 = 13.7 Cr prior, +44%) is doing the PAT lifting while operating profit stagnates. Headline PAT growth is treasury-aided, not operating. -> A4 question. |
| MMI-06 | F16 | Table 4 lines 282-284, 419 | slide 6 line 282; slide 9 line 419 | "one-time Rs 4 ... cr write off for a specific government customer"; "Rs 4Cr one-time write off for a specific government customer" | FORWARD-SIGNAL | A Rs4 Cr write-off against a government customer is a receivables-quality / collection event on the exact segment (Government) tied to monitoring items 1 and 2 and to FLAG-CASH INDETERMINATE (FY26 receivables Rs176.4 Cr). Labelled "one-time"; that label must be tested next quarter. Also the sole named driver (with "product mix") of the margin miss. -> A4 question. |
| MMI-07 | F16 | Table 1 (TOC) / Table 2A | slide 3 lines 146-157; slide 6 lines 271-291 | (absence — no order-book line in TOC or financial-highlights table) | AMBIGUOUS | FY26 baseline carried order book Rs1,754 Cr (+17%, 3.7x rev) and intake +24% to Rs785 Cr. This Q1FY27 deck discloses NO order book or intake anywhere (TOC lines 146-157 list no such slide; financial-highlights table lines 271-291 carry none). A true prior-deck verbatim diff is impossible (prior deck not supplied), so this is a candidate dropped forward-visibility disclosure, not a confirmed drop. Without order book, monitoring item 8 (FY28 Rs1,000 Cr pacing) is untrackable from the deck. -> A4 question: request order book / intake. |
| MMI-08 | F6 (+F13) | Table 6 #1 | slide 4 line 204 | "subject to shareholder approval, effective 1st July 2026" | FORWARD-SIGNAL | Rohan Verma appointed Joint Managing Director, effective 2026-07-01, ratification pending -> a shareholder resolution is incoming at the next AGM/EGM (F13 board-outcome signal). Ties FLAG-PROMOTER CONCERN and monitoring item 9 (MD succession). The commentary frames him as shaping the "AI roadmap" — succession is being executed. Commitment register + A4 question (approval timing, scope of role vs Rakesh Verma). |
| MMI-09 | F14 | Table 2A line 285 | slide 6 line 285 | "PAT Margin (%) 2  31.2% 33.9% 17.8% 25.5%" | NEUTRAL-FACT | The YoY cell for PAT Margin reads 17.8% — identical to Total Income's YoY (line 274) and nonsensical as the "growth" of a percentage margin. Copy/paste table error. Immaterial alone; a data-quality/governance data point. Also note inconsistent margin denominators: EBITDA Margin = EBITDA/Rev-from-Ops but PAT Margin = PAT/Total-Income (note lines 296) — mixing denominators across two headline margins. |
| MMI-10 | F16 | Table 1 (TOC) / slides 4-5 | slide 3 lines 146-157; slides 4-5 lines 181-250 | (absence — no revenue target / guidance figure) | AMBIGUOUS | No FY28 Rs1,000 Cr target, nor any quantified forward revenue/margin guidance, appears in the deck; management commentary (slides 4-5) is qualitative ("golden era", "next phase of growth") only. Prior-deck verbatim diff impossible, so this is a candidate softened/absent-guidance item, not a confirmed softening. Monitoring item 8 unpaceable. -> A4 question. |
| MMI-11 | F7 | Table 6 #4 | slide 14 line 633 | "Q1 is seasonally weakest quarter for Government business" | AMBIGUOUS | A pre-emptive framing hedge attached precisely to the Government segment that missed its 15-20% target (actual +9.2%, MMI-03) and carried the Rs4Cr write-off (MMI-06). Seasonality is plausible, but the hedge lands exactly where the number is weak. Conservative read: test whether "seasonality" or demand/collection softness explains the miss. -> A4 question. |
| MMI-12 | F16 | Table 4 lines 286-289 | slide 6 line 286 | "Cash & Cash equivalents grew to 745 Cr from 685 Cr in this quarter" | FORWARD-SIGNAL | Treasury rose to Rs745.3 Cr (from Rs685.0 FY26 close, +Rs60 Cr in one quarter); other income up 44% YoY (see MMI-05). No capital-allocation plan is disclosed anywhere in the deck. Idle-treasury accretion continues with growing dependence of PAT on treasury income — monitoring item 10 (capital-allocation plan) unaddressed. -> A4 question. |

---

## CHECKLIST SCORECARD (F1-F17, every check marked)

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing line items | PASS | Reviewed all 3 ZERO_STANDING rows: two are non-computable YoY dashes on a % (EBITDA margin, line 281) and a balance (cash, line 288); one is Sale of Hardware Map-led = 0 both periods (structural — maps carry no hardware, line 401). None is an exceptional / anticipatory statutory-template line. |
| F2 Standalone vs consolidated | N.A. | Deck presents consolidated figures only; no standalone column to decompose. |
| F3 Shell-entity detection | N.A. | No entity-level cost lines (no CoM/employee/depreciation by entity) in a presentation. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters / component-auditor disclosure in a presentation. |
| F5 Going concern / EoM scope | N.A. | No auditor report or Emphasis-of-Matter paragraph in a presentation. |
| F6 Forward-commitment phrase mining | FINDING | MMI-08 (Joint MD "effective 1st July 2026", line 204); reporting-policy commitment "Now onwards ... we shall report" AEG (line 447); AI-native push (lines 227-230). See Commitment Register. |
| F7 Hedge phrase mining | FINDING | MMI-11 — new qualitative hedge "Q1 is seasonally weakest quarter for Government business" (line 633) framing the sub-target Govt quarter; plus "subject to shareholder approval" (line 204) and boilerplate disclaimer "no obligation to update... undue reliance" (lines 726-727). |
| F8 Tax forensics | N.A. | No tax line, ETR, or deferred-tax disclosure in the deck. |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure in the deck. |
| F10 Share count and dilution | N.A. | No EPS, share count, or paid-up capital disclosed. Shareholding % only: promoters 51.4% (line 671), consistent with 51.41% baseline, no corporate action / dilutive instrument shown. |
| F11 Reserves and net-worth tie-out | N.A. | No balance sheet / other-equity / net-worth figure to reconcile. |
| F12 Segment forensics | FINDING | MMI-04 — product-mix margin dilution (IoT share 19%->29%, blended margin -570bps). Segment assets/liabilities not disclosed (that half N.A.). |
| F13 Board outcome beyond results | FINDING | MMI-08 — Joint MD appointment pending shareholder approval implies an incoming AGM/EGM resolution; MD-succession governance signal (monitoring item 9, FLAG-PROMOTER CONCERN). |
| F14 Note-drafting inconsistencies | FINDING | MMI-09 — PAT Margin YoY cell = 17.8% (erroneous duplicate of Total Income YoY, line 285); plus inconsistent margin denominators across EBITDA vs PAT margin (note, line 296). |
| F15 Entity-list diffs | N.A. | No consolidation entity list in the deck; no prior deck to diff. |
| F16 Presentation dropped/reframed disclosures | FINDING | MMI-01 (A&M/C&E->AEG reframe), MMI-02 (truncated chart axes), MMI-03 (Govt growth 11% vs 9.2%), MMI-05 (headline emphasis vs flat EBITDA), MMI-06 (Rs4Cr Govt write-off), MMI-07 (order book absent), MMI-10 (no revenue guidance), MMI-12 (treasury / no allocation plan). |
| F17 Concall silence audit | N.A. | No transcript supplied; presentation doctype. |

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | slide/line ref | status word |
|---|---|---|---|
| Rohan Verma appointed Joint Managing Director, subject to shareholder approval | effective 2026-07-01; ratification pending (next AGM/EGM) | slide 4, line 204 | appointed (pending shareholder ratification) |
| Report market-wise segmental revenue in AEG framework ("Now onwards ... we shall report") | commenced Q1 FY27 ("Beginning this quarter") | slide 10, lines 439, 447 | commenced / implemented |
| Push into "AI-native product development, AI-native product offerings and AI-native organizational work" | no date ("coming time", "golden era") | slide 5, lines 227-230 | underway |
| Customer wins disclosed as delivered (Tata Sierra EV live; 2-wheeler OEM contract renewal; new export maps program won) | Q1 FY27 (stated as done) | slide 12, lines 538, 553-555 | completed (delivery confirmations, not forward commitments) |

---

## SUMMARY FOR A4

- FORWARD-SIGNAL (convert to management questions): MMI-03 (Govt growth inflated / below target), MMI-04 (structural margin dilution from IoT scale), MMI-05 (flat operating EBITDA, treasury-lifted PAT), MMI-06 (Rs4Cr Govt write-off / collection risk), MMI-08 (Joint MD succession + pending approval), MMI-12 (rising idle treasury, no allocation plan).
- AMBIGUOUS (convert to management questions): MMI-01 (AEG reframe / request A&M-C&E->AEG bridge), MMI-07 (order book absent — request it), MMI-10 (no revenue guidance — request FY28 Rs1,000 Cr pacing), MMI-11 (Govt seasonality hedge — seasonality vs demand softness).
- PRIORITY (SEGMENT_FRAMEWORK_CHANGE, MMI-01): the AEG switch does NOT bury the Map-led core — the Map-led vs IoT-led product split is retained on slide 9, and Government is now broken out separately (net gain for monitoring item 1). The real cost is loss of the A&M/C&E historical series with no bridge, and the reframe conveniently arrives the same quarter the Government number needed rounding help (MMI-03) and Map-led core went flat (+0.5%, marginally meeting item 5 vs FY26's -8.7%). Lean AMBIGUOUS; ask for the restatement mapping and confirmation no revenue was reclassified between segments.

---

```yaml
stage: A3-forensics
company: "MAPMYINDIA"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/forensics_presentation_mapmyindia_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "MMI-01", check: "F16", line: "194", classification: "AMBIGUOUS", implication: "A&M/C&E->AEG reframe; comparatives restated but no bridge, old series discontinued; re-baseline items 1 and 5"}
  - {id: "MMI-02", check: "F16", line: "645", classification: "CONFIRMATORY-NEGATIVE", implication: "Truncated y-axes (Govt base 10, Ent 50, Auto 35) visually amplify modest growth"}
  - {id: "MMI-03", check: "F16", line: "614", classification: "FORWARD-SIGNAL", implication: "Govt growth stated 11% vs disclosed 15.3->16.7 = 9.2%; below 15-20% target (item 1); selective rounding on weakest segment"}
  - {id: "MMI-04", check: "F12", line: "408", classification: "FORWARD-SIGNAL", implication: "IoT share 19%->29% dilutes blended margin (-570bps); item 4 >38% at structural risk; segment assets/liab not disclosed"}
  - {id: "MMI-05", check: "F16", line: "279", classification: "FORWARD-SIGNAL", implication: "EBITDA flat +0.4% and margin -570bps de-emphasised; PAT +8.6% lifted by other income +44%, not operations"}
  - {id: "MMI-06", check: "F16", line: "282", classification: "FORWARD-SIGNAL", implication: "Rs4Cr one-time write-off on a government customer; receivables/collection risk (items 1,2; FLAG-CASH); test 'one-time' next quarter"}
  - {id: "MMI-07", check: "F16", line: "148", classification: "AMBIGUOUS", implication: "Order book/intake absent from deck (TOC 146-157, table 271-291); candidate dropped disclosure, prior-deck diff impossible; item 8 untrackable"}
  - {id: "MMI-08", check: "F6", line: "204", classification: "FORWARD-SIGNAL", implication: "Rohan Verma Joint MD effective 2026-07-01, approval pending -> AGM resolution; MD succession (item 9, FLAG-PROMOTER)"}
  - {id: "MMI-09", check: "F14", line: "285", classification: "NEUTRAL-FACT", implication: "PAT Margin YoY cell 17.8% erroneous duplicate; inconsistent margin denominators; data-quality data point"}
  - {id: "MMI-10", check: "F16", line: "146", classification: "AMBIGUOUS", implication: "No FY28 Rs1,000 Cr target / revenue guidance in deck; prior-deck diff impossible; item 8 unpaceable"}
  - {id: "MMI-11", check: "F7", line: "633", classification: "AMBIGUOUS", implication: "'Q1 seasonally weakest' hedge lands on the sub-target Govt segment; seasonality vs demand/collection softness"}
  - {id: "MMI-12", check: "F16", line: "286", classification: "FORWARD-SIGNAL", implication: "Treasury Rs745.3 Cr (+60 Cr QoQ), other income +44%, no capital-allocation plan; item 10 unaddressed"}
forward_signals: ["MMI-03", "MMI-04", "MMI-05", "MMI-06", "MMI-08", "MMI-12"]
ambiguous: ["MMI-01", "MMI-07", "MMI-10", "MMI-11"]
commitments:
  - {commitment: "Rohan Verma appointed Joint Managing Director, subject to shareholder approval", implied_date: "2026-07-01 (ratification pending)", ref: "slide 4 line 204", status_word: "appointed-pending-ratification"}
  - {commitment: "Report market-wise segmental revenue in AEG framework", implied_date: "Q1FY27 (commenced)", ref: "slide 10 lines 439,447", status_word: "commenced"}
  - {commitment: "Push into AI-native product development / offerings / organizational work", implied_date: "undated", ref: "slide 5 lines 227-230", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
