# A3 FORENSIC NOTES — SAMHI Hotels Limited (SAMHI), Q1 FY27 — DOCTYPE: presentation (52-slide investor deck)

Source extract: `extract_presentation_samhi_q1fy27.txt` (1,917 lines, 52 pages, unit Millions, x0.1 -> Rs Crore).
Ledger: `ledger_presentation_samhi_q1fy27.md` — every row of Tables 1-6 (slide inventory, KPI ledger, 56 footnotes, 13 forward-looking statements, 7 discrepancy flags, 4 ZERO_STANDING items) read verbatim at its cited line in the extract. Reconciliation 100%.
Prior-quarter deck: NONE supplied (A2 flagged; DROPPED_SLIDE / entity diffs cannot be run). Notion monitoring checklist: EMPTY (new company, no companies/SAMHI.md). No tripwires fabricated.
Cross-document: reconciled against `forensics_pressrelease_samhi_q1fy27.md` (leverage, RevPAR/ARR/occupancy, net debt, tax, forward guidance) — deltas noted in F16-04.

Doctype applicability: on an investor presentation F16 applies plus any F6/F10/F11 numbers the deck carries. The deck presents CONSOLIDATED figures only (no standalone, no auditor report, no notes, no OCI, no share count/EPS, no Other Equity, no segment asset/liability tables, no concall). Accordingly F3, F4, F5, F9, F10, F11, F15, F17 are N.A. with reason. F1, F2, F6, F7, F8, F12, F14, F16 run on what the deck does carry; F13 PASS.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------|----------------|---------------------|
| P-01 | F1 | Table 6 r2/r3; Slide 15 | 485, 487 (fn 500,503) | "Exceptional Items — — 1,075" ; "Profit/(Loss) from discontinued operations — (28) (55)" | AMBIGUOUS | Both quarterly cols dash; FY26 Exceptional Rs 1,075 Mn = +966 impairment REVERSAL, -35 labor code, +145 Caspia sale gain (fn3, line 500). An impairment reversal implies assets were previously written down — asset-value volatility is live. Discontinued-ops line stands ready for future asset churn (Caspia Delhi precedent). Both inflate the FY26 base and anticipate recurrence at asset sales / GIC-type events. A4: nature & recurrence of the Rs 966 Mn reversal. |
| P-02 | F1 | Table 6 r1; Slide 9 | 300-303 | Leisure FY2026: Rooms "–", Revenue "–", Revenue/Key "–"; pipeline "% Change" = "NA" | FORWARD-SIGNAL | Standing segment row carries 75 hotels / 1,046 rooms (slides 8/37/44) but ZERO booked revenue in the FY26 baseline. RARE monetization (fee income, incentive fee, opportunistic investment) is pre-revenue; deck targets pilot go-live H2 FY27 (slide 37). The dash is a template placeholder for a revenue stream that has not yet switched on — a future P&L line to watch, currently zero. |
| P-03 | F2 | Slide 15 rows "Attributable to SAMHI" / "Minority Interest" | 503, 505 | "Attributable to SAMHI 183 173 5,030" ; "Attributable to Minority Interest 67 19 636" | FORWARD-SIGNAL | No standalone table, but the consolidated PAT attribution is the subsidiary/NCI decomposition. Consolidated PAT grew +29.7% (192->249) yet SAMHI-attributable grew only +5.8% (173->183); minority share leapt 19->67 (+253%) and was Rs 636 Mn of FY26 PAT. Growth is accruing disproportionately to minority (GIC/JV) holders — per-share economics lag the headline consolidated growth SAMHI leads with. A4: which subsidiary(ies) drive the rising NCI take and its trajectory. |
| P-04 | F6 | Table 4 (13 FLS); Slides 7/9/11/14/25/28/37 | see Commitment Register | "W, HITEC City, Hyderabad ... Opening Q4 FY27" (234) ; "targeted to go live in H2 FY27" (1307) | FORWARD-SIGNAL | 8 dated/dateable commitments with status words extracted (see register). Nearest catalysts: W Hyderabad opening Q4 FY27 (status "Under Fit out", construction completed, slide 29); RARE-Marriott pilot go-live H2 FY27 (40+/75 hotels agreed, 15 pilots shortlisted, "intended"/"targeted"). These seed the Role 5 promise-vs-delivery tracker; no prior deck exists to score status transitions, so this establishes the baseline. |
| P-05 | F6/F14 | Slide 7 vs Slide 28; ENUM-06 | 234, 1035-1036 | Slide 7 "Westin, Whitefield, Bangalore ... Opening FY30" vs Slide 28 row 11 "Westin, Whitefield, Bangalore ... Under Construction 220" (FY28 col) | AMBIGUOUS | Opening-year inconsistency: slide 7 labels Westin Whitefield Bangalore (220 rooms) and Mid-scale Financial District Hyderabad (260 rooms) "Opening FY30", but slide 28's timeline table seats those room counts in the FY28 column (Westin status "Under Construction"). Either slide-7 dates are stale/conservative or A2's TABLE_COLUMN_ALIGNMENT caveat bites — a ~2-year swing on 480 pipeline rooms is catalyst-timing material. A4: confirm true opening year (visual check of slide 28). |
| P-06 | F7 | Slides 11/12/14; Slide 3/34/37 | 340-341? 365, 435-436, 124, 1204, 1303 | "79.3% Occupancy withstanding impact of middle-east conflict" (365) ; "In discussion with operators for segment and brand finalization" (1203-1204) ; "Room counts in under development asset may vary based on final plan and statutory approvals" (124) | AMBIGUOUS | Three live hedges. (1) Geopolitical/international-travel softness ("middle-east conflict") newly framed as offset by domestic resilience — matches press-release A3-06; tells us Q2 demand risk. (2) Several FY30 pipeline hotels still at Design/Planning with brand/segment NOT finalized ("in discussion with operators", "may vary based on final plans/statutory approvals") — the 1,669-room pipeline count is soft. (3) RARE "selective opportunistic investments ... to be evaluated" (1303) keeps future capital deployment open-ended. |
| P-07 | F7 | Slide 14; Slide 28 row 6 | 435-436, 1030 | "22 apartments have been fully completed; delay in approvals causing loss of revenue in a strong market" | AMBIGUOUS | Concrete disclosed drag: Hyatt Regency Pune 22 apartments physically complete but stuck in "Pre-Opening" (slide 28) pending statutory approvals; management admits ongoing revenue loss in a strong market with no dated resolution. Duration open-ended -> continuing near-term revenue leakage. A4: expected approval date and quantum of foregone revenue. |
| P-08 | F8 | Slide 15 rows PBT/Tax/PAT (fn5,fn6) | 491, 495, 500, 505-506 | "Tax Expense 2,995" (credit) ; "Deferred tax asset of ~₹3,000mn recognized in FY26 based on ... greater visibility of future profits" | FORWARD-SIGNAL | FY26 PAT 5,665 EXCEEDS FY26 PBT 2,671 by ~Rs 2,994 Mn — a net tax CREDIT from ~Rs 3,000 Mn DTA recognition (non-cash, fn5). FY26 PAT is structurally inflated and is NOT a valuation anchor; matches press-release A3-02. Quarterly ETR rising toward statutory 25.17%: Q1FY26 39/231 = 16.9% -> Q1FY27 78/327 = 23.9%. Future book-tax step-up once the shield exhausts. The DTA recognition is also management's own signal of forward-profit confidence. |
| P-09 | F12 | Table 5 ND-03a/ND-03b, CLASS-07; Slides 9/22/41-45/50 | 300-303, 288-295 (12,499 vs 12,790), 1410/1447/1471 vs 837, 1452 | "Total - Aset Ownership 4,899 1,669 6,568" ; slide 42 fn1 "86 rooms of Fairfield, Srip. Chennai ... moved to the Upscale under-development section" | AMBIGUOUS | (a) FY26 segment-revenue sum 5,270+5,235+1,994 = Rs 12,499 Mn vs FY26 Total Income Rs 12,790 Mn — Rs 291 Mn unallocated gap not reconciled on-slide (plausibly corporate/other income per slide-22 bridge, unconfirmed). (b) Q1FY27 segment sum 1,239+1,298+517 = Rs 3,054 Mn vs Asset Income Rs 3,057 Mn — Rs 3 Mn foot (also brand-mix sum, slide 45). (c) Pipeline reclassification: Sriperumbudur 86 Fairfield rooms moved Upper Mid-scale->Upscale, now built as ~135-room Marriott (slide 42 fn1 / slide 36) — a QoQ pipeline-definition change; no prior deck to diff. Segment ASSET/LIABILITY tables not disclosed (that half of F12 N.A.). A4: reconcile the Rs 291 Mn FY26 gap. |
| P-10 | F14 | Table 5 ND-01/ND-02; Slide 12 vs Slide 13 | 360-363, 399, 405 | Slide 12 box "Consol. EBITDA ₹1,013mn +12.1% YoY Comparable ... -4.1% YoY Reported" ; slide 13 comparable Q1FY27 EBITDA = "1,105" | AMBIGUOUS | Slide-12 headline boxes pair a REPORTED rupee figure with a COMPARABLE-basis growth rate: EBITDA box shows Rs 1,013 Mn (reported) tagged "+12.1% Comparable", but the +12.1% belongs to comparable Rs 1,105 Mn (slide 13, line 399); PBT box shows Rs 327 Mn (reported) tagged "+121.7% Comparable", but +121.7% belongs to comparable Rs 419 Mn (line 405). A reader can misread Rs 1,013 Mn as growing both +12.1% and -4.1%. Favorable-number-with-favorable-rate mismatch. A4: confirm which figure/rate pair management intends. |
| P-11 | F14 | Table 5 ND-04; Slides 6/16 vs 15/48; misc | 199, 524 vs 471, 1618; 1844; 122-123 | "Consol EBITDA ... 4,721 pre ESOP" (199) vs "Consolidated EBITDA ... 4,626" (471) ; "Total - Aset Ownership" (1844) | NEUTRAL-FACT | Cumulative drafting inconsistencies, individually immaterial: (a) FY26 EBITDA shown as 4,721 (pre-ESOP/TTM, slides 6/16) AND 4,626 (reported, slides 15/48), both glossed simply "EBITDA FY26" — ~Rs 95 Mn ESOP-basis gap risks conflation (ND-04). (b) PAT attribution foots Rs 1 Mn high: SAMHI 183 + Minority 67 = 250 vs PAT 249. (c) Typo "Aset Ownership" (1844); "Pannel Kerr Forster" (1585) vs "Pannell Kerr Forster" (1554). (d) Slide-12 PAT box omits the YoY% shown on the other three boxes. A governance/proof-reading data point, no numeric disclosure materially impaired. |
| P-12 | F16 | Slides 11/12/13/15; press-release A3-07 | 340-341, 361-363, 471, 464 | "Operating margins of ~36% (ex GST impact)" (340) ; "EBITDA Margin 32.9% ... 36.8%" (464-471) | AMBIGUOUS | Reframing: the deck leads with "Comparable +10.8%/+12.1%" and "~36% ex-GST margin ... to improve to ~40%" while REPORTED EBITDA is -4.1% (1,013 vs 1,056) and reported EBITDA margin fell 36.8% -> 32.9% (line 464-471). "Comparable" strips GIC one-timers and the ~Rs 92 Mn Q1FY27 GST-ITC hit. The GST change (12%-with-ITC -> 5%-without) is presented as one-time/optical, but slide 49 fn (line 1789) confirms it is now the STRUCTURAL basis ("EBITDA reported for Q3'26, Q4'26 and Q1'27 is post GST implementation") — i.e. recurring, not a one-off. A4: confirm the ~Rs 92 Mn GST drag recurs every quarter and how the ~40% margin bridge absorbs it. |
| P-13 | F16 | Slide 21 fn1-4; Slides 11/12 fn | 807, 812-816, 349 | Slide 21 footnotes 1-4: differing same-store exclusion sets across the 13-quarter RevPAR series | AMBIGUOUS | The "same-store RevPAR" 13-quarter chart (slide 21) is built on a MOVING base — the exclusion set changes period to period (ACIC Aug'23; Trinity Oct'24; HIEX Greater Noida Dec'24; HIEX Kolkata May'25; Caspia Delhi; Sheraton Commercial phased in/out at different points, fn1-4). The headline +9.6% same-store RevPAR growth is therefore not a like-for-like series across the full window shown. A4: request a constant-composition RevPAR series. |
| P-14 | F16 | Slide 16 chart; Slide 6 fn2 | 555-587, 222 | Debt chart baseline "Sep 30 2023 ... 5.3x" ; "Restate CAGR ... calculated from FY16 to FY'26 i.e. for 10 years" | NEUTRAL-FACT | Favorable-baseline framing (standard IR practice, flagged not condemned): net-debt/EBITDA chart anchors to the Sep'30'23 IPO-era 5.3x to frame the 3.2x deleveraging; the 22%/38% CAGR headlines use a chosen FY16-FY26 window; FY26 EBITDA is headlined on the higher pre-ESOP basis (4,721) on slides 6/16. Each choice is disclosed in footnotes; presentation optics, not error. |
| P-15 | F16 | Cross-doc vs press release A3-03 | Slide 12 (371), Slide 16 (522/524) | "Net Debt : EBITDA ~3.2x" (371) ; net debt 14,928 / TTM EBITDA 4,664 = 3.20x | RESOLVED | Cross-check requested by task: the press release logged a CEO quote "~3.0x" (A3-03) unsupported by any table. This deck is INTERNALLY CONSISTENT at ~3.2x (slide 12 box and slide 16 Jun'30'26 column; 14,928/4,664 = 3.20x) and never states 3.0x — the deck stands behind 3.2x, resolving the press-release ambiguity in favor of 3.2x (the CEO's 3.0x was optimistic rounding). RevPAR Rs 5,219 / +9.6%, occupancy 79.3%, net debt 14,928, and the 9-11% revenue-guidance band all tie cleanly across deck and press release — no further discrepancy. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1  | FINDING | ZERO_STANDING lines: Exceptional Items / Discontinued ops (P-01) and the zero-revenue Leisure segment row (P-02). |
| F2  | FINDING | No standalone table, but consolidated PAT attribution shows minority take surging while SAMHI-attributable lags (P-03). |
| F3  | N.A. | No standalone-vs-consolidated cost lines in a deck; shell detection impossible. |
| F4  | N.A. | No auditor report / Other Matters paragraph; component-auditor unaudited ratio undisclosed. |
| F5  | N.A. | No auditor Going Concern / EoM paragraph and no prior quarter to verbatim-diff. |
| F6  | FINDING | 8 dated commitments mined (W Hyderabad Q4FY27, RARE-Marriott H2FY27, upscale mix FY2030, etc.); P-04, P-05, Commitment Register. |
| F7  | FINDING | Live hedges: middle-east-conflict demand softness, unfinalized pipeline brands "may vary", Hyatt Pune approval delay; P-06, P-07. |
| F8  | FINDING | FY26 PAT 5,665 > PBT 2,671 = ~Rs 3,000 Mn DTA credit; ETR 16.9% -> 23.9% rising to statutory; P-08. |
| F9  | N.A. | No OCI / actuarial disclosure in a presentation. |
| F10 | N.A. | No paid-up capital, share count or basic/diluted EPS disclosed (ESOP referenced but share dilution unquantifiable — see P-11 ND-04 for the ESOP EBITDA basis). |
| F11 | N.A. | No Other Equity / net-worth figures; only net debt and credit rating disclosed. |
| F12 | FINDING | Segment-revenue-vs-total gaps (Rs 291 Mn FY26, Rs 3 Mn Q1FY27), zero-revenue Leisure, pipeline reclassification; P-09 (segment asset/liability tables absent). |
| F13 | PASS | Cover letter (slide 1) = investor-presentation intimation only; board slide (47) lists 7 directors (4 independent) with no term dates/DINs/appointments — nothing beyond results to map to a catalyst window. |
| F14 | FINDING | Slide-12 reported-figure-with-comparable-rate mismatch (P-10), plus ND-04 basis conflation / Rs 1 Mn foot / typos (P-11), plus opening-date inconsistency (P-05). |
| F15 | N.A. | No legal-entity consolidation list (glossary is a hotel roster) and no prior-quarter ledger to diff. |
| F16 | FINDING | Comparable/ex-GST reframing masks reported EBITDA -4.1% & margin 32.9% (P-12), moving same-store base (P-13), favorable chart baselines (P-14), cross-doc leverage resolved (P-15). |
| F17 | N.A. | Not a concall; no transcript. Monitoring checklist empty — no silence audit possible/needed. |

Scorecard tally: FINDING x8 (F1, F2, F6, F7, F8, F12, F14, F16); PASS x1 (F13); N.A. x8 (F3, F4, F5, F9, F10, F11, F15, F17). No blank checks — GATE A3 pass.

---

## COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Slide/line ref | Status word |
|---|------------|--------------|----------------|-------------|
| 1 | W, HITEC City Hyderabad — new hotel opening (170 rooms) | Q4 FY27 | slide 7 (234) / slide 28 r7 / slide 29 (1061-1076) | under fit-out (construction completed) |
| 2 | RARE x Marriott "Outdoor Collection" pilot go-live (15 shortlisted properties) | H2 FY27 | slide 14 (444-447) / slide 37 (1306-1308) | underway (40+/75 agreed, visits completed) |
| 3 | Hyatt Regency Pune — 22 apartments into service | pending statutory approval | slide 14 (435-436) / slide 28 r6 | completed (revenue blocked on approval) |
| 4 | Westin Whitefield Bangalore — new opening (220 rooms) | FY28 (slide 28) / FY30 (slide 7) — see P-05 | slide 28 r11 (1035) | under construction |
| 5 | Upscale revenue-mix share ~41% -> ~60% | FY2030 | slide 25 (964-967) | underway (via rebranding/renovation) |
| 6 | Operating EBITDA margin -> ~40% (upscale mix, GST-unaffected) | medium-term | slide 11 (340-341) / slide 14 (430-432) | target |
| 7 | FY30/FY31 openings: Financial District Hyd (260), Marriott Sriperumbudur (135), Noida (162), Navi Mumbai combo (700) | FY30 / FY31 | slide 7 (232-241) / slide 28 r12-16 | design / planning |
| 8 | Itmenaan Estate (RARE succession capital): 8 -> 15-20 rooms | undated | slide 38 (1324, 1328) | initiated |

Baseline established for the Role 5 promise-vs-delivery tracker / FTTCP catalyst timeline; no prior deck exists to score status transitions this run.

---

## RECONCILIATION & GAP NOTES
- Ledger rows read: Table 1 (52 slides), Table 2 (full KPI ledger, all slides 1-51), Table 3 (56 footnotes), Table 4 (13 FLS), Table 5 (7 discrepancy flags ND-01..04, ENUM-05/06, CLASS-07), Table 6 (4 ZERO_STANDING items) — 100% read at cited lines and reconciled.
- A2-surfaced items all verified and line-cited: ND-01/ND-02 (P-10), ND-04 (P-11), ND-03a/b (P-09), CLASS-07 Sriperumbudur reclassification (P-09), CHART_LABEL_MAPPING/TABLE_ALIGNMENT caveats (noted in P-05/P-13 and carried as extraction limits, not treated as management error), four ZERO_STANDING dashes (P-01/P-02 for Leisure, Exceptional, Discontinued; glossary Addition/Renovation dash = neutral template, no finding).
- Cross-document reconciliation vs press-release forensics: leverage 3.2x resolved (P-15); RevPAR Rs 5,219/+9.6%, occupancy 79.3%, net debt 14,928, TTM EBITDA 4,664, tax-credit/DTA (P-08), 9-11% revenue guidance, ~40% margin target and FY2030 upscale-mix all tie across both documents. The press-release CEO "~3.0x" is the only cross-doc divergence, and the deck contradicts it (3.2x).
- GAPS (flagged, not defects): (a) no prior-quarter deck -> F16 dropped-metric diff and F15 entity/relationship diffs cannot be performed; A2 requests the prior deck ledger for any cross-quarter silence check. (b) Segment ASSET/LIABILITY and share-count/EPS not in the deck -> F12 (half) and F10 unquantifiable. (c) Interior-year chart labels (slides 6/16/19/21/48/49) are extraction-uncertain per A2 ENUM-05; only cross-validated endpoints were used for findings.

---

```yaml
stage: A3-forensics
company: "SAMHI"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/samhi-q1fy27/work/forensics_presentation_samhi_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "P-01", check: "F1", line: "485,487", classification: "AMBIGUOUS", implication: "Exceptional Items (FY26 1,075 incl +966 impairment reversal) & Discontinued-ops standing lines anticipate asset-churn recurrence; inflate FY26 base"}
  - {id: "P-02", check: "F1", line: "300-303", classification: "FORWARD-SIGNAL", implication: "Leisure segment 75 hotels/1,046 rooms but zero booked revenue; RARE monetization pre-revenue, pilot go-live targeted H2FY27"}
  - {id: "P-03", check: "F2", line: "503,505", classification: "FORWARD-SIGNAL", implication: "Consolidated PAT +29.7% but SAMHI-attributable only +5.8%; minority take 19->67, FY26 636 — growth accrues to minority/JV holders, per-share lags headline"}
  - {id: "P-04", check: "F6", line: "234,1307", classification: "FORWARD-SIGNAL", implication: "8 dated commitments; nearest catalysts W Hyderabad open Q4FY27 (under fit-out) and RARE-Marriott pilot H2FY27; baseline for Role 5 tracker"}
  - {id: "P-05", check: "F14", line: "234,1035", classification: "AMBIGUOUS", implication: "Opening-year conflict: Westin Whitefield & Financial District Hyd shown FY30 on slide 7 but FY28 column on slide 28 (Westin under construction); ~2yr swing on 480 rooms"}
  - {id: "P-06", check: "F7", line: "365,1204,124", classification: "AMBIGUOUS", implication: "Live hedges: middle-east-conflict intl demand softness (Q2 risk), FY30 pipeline brands not finalized ('may vary'/'in discussion'), RARE capital open-ended"}
  - {id: "P-07", check: "F7", line: "435-436", classification: "AMBIGUOUS", implication: "Hyatt Regency Pune 22 apartments complete but stuck pre-opening on approvals; ongoing revenue loss, no dated resolution"}
  - {id: "P-08", check: "F8", line: "491,495,505", classification: "FORWARD-SIGNAL", implication: "FY26 PAT 5,665 > PBT 2,671 = ~3,000 DTA credit; ETR 16.9%->23.9% rising to statutory 25.17%; FY26 PAT not a valuation anchor; future book-tax step-up"}
  - {id: "P-09", check: "F12", line: "288-295,1452", classification: "AMBIGUOUS", implication: "FY26 segment-rev sum 12,499 vs total 12,790 = 291 unallocated gap; Q1FY27 3 gap; Leisure zero-rev; Sriperumbudur 86 rooms reclassified Upper Mid->Upscale"}
  - {id: "P-10", check: "F14", line: "360-363,399,405", classification: "AMBIGUOUS", implication: "Slide-12 boxes pair reported EBITDA 1,013 / PBT 327 with comparable growth rates +12.1%/+121.7% (belong to 1,105/419); reads as one figure growing two ways"}
  - {id: "P-11", check: "F14", line: "199,471,1844", classification: "NEUTRAL-FACT", implication: "FY26 EBITDA 4,721 pre-ESOP vs 4,626 reported both glossed 'EBITDA FY26' (ND-04); Rs 1 Mn PAT foot; 'Aset'/Pannel typos — proof-reading/governance data point"}
  - {id: "P-12", check: "F16", line: "340,464,1789", classification: "AMBIGUOUS", implication: "Comparable/ex-GST reframing masks reported EBITDA -4.1% & margin 36.8%->32.9%; slide-49 fn confirms GST hit is now STRUCTURAL/recurring, not one-time"}
  - {id: "P-13", check: "F16", line: "807,812-816", classification: "AMBIGUOUS", implication: "Same-store RevPAR 13-qtr series built on a moving exclusion set (ACIC/Trinity/HIEX/Caspia/Sheraton phased in-out); +9.6% not like-for-like across window"}
  - {id: "P-14", check: "F16", line: "555,222", classification: "NEUTRAL-FACT", implication: "Favorable-baseline optics: debt chart anchored Sep'23 5.3x, FY16-26 CAGR window, pre-ESOP EBITDA headlined — disclosed in footnotes, not error"}
  - {id: "P-15", check: "F16", line: "371,522", classification: "RESOLVED", implication: "Deck consistent at 3.2x (14,928/4,664), never states 3.0x; resolves press-release CEO '~3.0x' (A3-03) in favor of 3.2x; RevPAR/occupancy/net-debt/guidance all tie cross-doc"}
forward_signals: ["P-02", "P-03", "P-04", "P-08"]
ambiguous: ["P-01", "P-05", "P-06", "P-07", "P-09", "P-10", "P-12", "P-13"]
commitments:
  - {commitment: "W HITEC City Hyderabad new opening (170 rooms)", implied_date: "Q4 FY27", ref: "slide 7 line 234 / slide 29", status_word: "under fit-out"}
  - {commitment: "RARE x Marriott Outdoor Collection pilot go-live (15 properties)", implied_date: "H2 FY27", ref: "slide 14 line 444 / slide 37 line 1307", status_word: "underway"}
  - {commitment: "Hyatt Regency Pune 22 apartments into service", implied_date: "pending approval", ref: "slide 14 line 435", status_word: "completed"}
  - {commitment: "Westin Whitefield Bangalore new opening (220 rooms)", implied_date: "FY28/FY30 (conflict, see P-05)", ref: "slide 28 line 1035", status_word: "under construction"}
  - {commitment: "Upscale revenue-mix share ~41% -> ~60%", implied_date: "FY2030", ref: "slide 25 line 964", status_word: "underway"}
  - {commitment: "Operating EBITDA margin -> ~40%", implied_date: "medium-term", ref: "slide 11 line 340 / slide 14 line 430", status_word: "target"}
  - {commitment: "FY30/FY31 openings (Fin.District Hyd, Sriperumbudur, Noida, Navi Mumbai)", implied_date: "FY30/FY31", ref: "slide 7 line 232 / slide 28 r12-16", status_word: "design"}
  - {commitment: "Itmenaan Estate 8 -> 15-20 rooms (RARE succession capital)", implied_date: "undated", ref: "slide 38 line 1324", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
