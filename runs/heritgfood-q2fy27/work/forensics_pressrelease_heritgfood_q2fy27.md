# A3 FORENSIC NOTES: HERITGFOOD Q2 FY27, doctype presentation (press release, tag "pressrelease")

Agent: A3 forensic notes | Model: claude-opus-5-5 | Run date: 2026-10-17
Inputs read: A1 structured (R001-R180), A1 fulltext (212 body lines), A2 ledger (180 rows).
Prior-quarter fulltext: ND (not available). Notion monitoring checklist: ND (not passed). No Notion page, no spear on record. This is a PRE-THESIS READ.
Source PDF and inputs/ were not opened.

Units: INR Mn as in the release (x0.1 = Rs Cr). Every "derived" figure is arithmetic on disclosed numbers. The release rounds YoY growth to whole percent, so derived prior-period figures carry a stated rounding range. They are not estimates of undisclosed numbers.

---

## 1. LEDGER RECONCILIATION

| Item | Count |
|---|---|
| Ledger rows (A2) | 180 |
| Structured IDs | 180 (R001-R180), orphans 0 |
| Rows read verbatim in fulltext | 180 |
| Value mismatches (verbatim text not present in fulltext) | 0 |
| Rows whose verbatim text sits 1-3 lines away from the A1-cited line | 45 (pipeline note, not a document finding) |
| ledger_reconciled_pct | 100 |

A1 line-cite drift, for A4 and A5 (actual fulltext line in brackets): R001 [27], R013 [73], R015 [77], R017 [82], R021-R022 [87], R023-R025 [88], R026-R027 [90], R049-R053 [111], R054-R058 [112], R068 [123], R087 [136], R098 [144], R101 [147], R105 [152], R106-R107 [163], R112 [203], R118 [24], R119 [25], R123 [66 and 86], R124-R125 [87], R126-R128 [88], R129 [93], R136 [151], R138 [159], R141 [164], R143-R144 [221-223], R163 [96], R165 [164], R167 [203], R171 [96]. The H1 table is the main case: A1 cites line 110 (the column-header row), but the values are on line 111 and the YoY row is on line 112. Every finding below cites the actual fulltext line.

A2 flags verified:
- R046 "QoQ: 20%" (L102) is unsigned. Implied Q1 FY27 EBITDA = 1,358 - 740 = 618, and 740 / 618 = +19.7%, so the sign is positive. Ties.
- R175 LLPD is undefined in the release. The A1 header gives "lakh litres per day". Neutral.
- R174 says there are no footnote markers. Confirmed by a full sweep.
- R180 says segment results are not in the release (L187-188). Confirmed.

Arithmetic tie-out of the headline tables (L100-102, L111-112):
- Q2 EBITDA margin: 740 / 13,196 = 5.61%, stated 5.6%. Ties.
- H1 EBITDA margin: 1,358 / 26,577 = 5.11%, stated 5.1%. Ties.
- Implied Q1 FY27: revenue 13,381; EBITDA 618 (4.62%); PAT 249. The stated QoQ figures (1)% revenue, +20% EBITDA, +98 bps margin and +24% PAT all tie within rounding.
- Milk revenue growth: 1.025 x 1.06 = 1.0865, stated 8.5% (L82-83). Ties.

---

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F16 | R005, R006, R007, R041, R042, R043, R109 | L63-64; L101; L170-171 | "Robust 19% YoY Revenue Growth; EBITDA Margin Recovers 98 bps QoQ to 5.6%" vs "YoY: (4) %" ... "YoY: (133) bps" ... "YoY: (39) %" | AMBIGUOUS | The release reports revenue YoY but margin QoQ. The headline and the ED commentary (L170-171 "98bps sequential recovery") omit the YoY declines of 133 bps in EBITDA margin and 39% in PAT. The YoY margin trough is not yet behind the company. Question: when does management expect the YoY EBITDA margin to stop falling? |
| A3-02 | F16 | R036, R038, R041, R043, R051, R053, R056, R058 | L100; L101; L111-112 | "INR 740 Mn" ... "INR 309 Mn"; "YoY: (4) %" ... "YoY: (39) %" | AMBIGUOUS (lean bear) | EBITDA fell 4% YoY but PAT fell 39%. The release gives no D&A, finance cost, other income, tax or minority line. Derived PAT/EBITDA conversion: Q2 FY27 41.8% vs about 65.8% in Q2 FY26. Derived EBITDA-minus-PAT drag: Q2 431 Mn vs 256-273 Mn a year earlier (+158-175 Mn). Q1 FY27 369 Mn vs 306-354 Mn a year earlier (+15-63 Mn). Sequentially the drag rose from 369 to 431 Mn. The step-up sits in Q2. If it is D&A and interest from capacity or acquisitions, it recurs. If it is a base-quarter other-income or one-off item, it does not. Question: give the Q2 bridge from EBITDA to PAT, and name what was capitalised or consolidated in Q2. |
| A3-03 | F16 | R080, R082, R083, R085, R088, R090, R091, R093 | L131-132; L136-138; L100; L111 | "INR4,510 million in Q2 FY27" ... "increased to 35.4% in Q2 FY27"; "its contribution reaching 42.5% of revenue in Q2 FY27" | AMBIGUOUS | VAP share does not tie to consolidated revenue (INR 13,196 Mn). 4,510 / 13,196 = 34.2%, stated 35.4%. 5,408 / 13,196 = 41.0%, stated 42.5%. H1: 10,146 / 26,577 = 38.2%, stated 39.6%. 11,730 / 26,577 = 44.1%, stated 45.7%. The implied denominator is about 12,730 Mn for Q2 and about 25,640 Mn for H1, roughly 466 Mn and 940 Mn below consolidated revenue. On a consolidated basis the VAP mix is 1.2-1.6 pp lower than stated. Question: what revenue base does "VAP contribution" use (standalone, dairy only, or net of something)? Has the base been constant across periods? |
| A3-04 | F16 | R079, R081, R087, R089 | L130-131; L136 | "grew 32% YoY" ... "and 36% to INR10,146 million in H1FY27"; "increased 31% YoY to INR 5,408 million and 35% YoY to INR 11,730 million in H1 FY27" | FORWARD-SIGNAL | The H1 framing hides a Q2 slowdown in VAP growth. Derived Q1 FY27 VAP (excl. ghee/butter) is 5,636 Mn, up about 39% YoY, against +32% in Q2. Including ghee/butter, Q1 is about +39% against +31% in Q2. VAP revenue also fell sequentially: excl. ghee/butter 5,636 to 4,510 (-20%), incl. ghee/butter 6,322 to 5,408 (-14%). Part of this is summer seasonality. The growth-rate slowdown is not seasonal. Read it with "expanding VAP capacity" (L175). Question: does the slowdown come from base effect, capacity limits or demand? Track whether VAP growth holds near 30% in Q3. |
| A3-05 | F16 | R008, R009, R084 | L65; L132 | "VAP Contribution expands 4.1% YoY to 35.4% in Q2 FY27" | NEUTRAL-FACT | 35.4% - 31.3% = 4.1 percentage points, but the release labels it "%". The relative expansion is 13.1%. This is a drafting looseness only. A4 should quote it as pp. |
| A3-06 | F6 | R014, R015, R016, R019, R020, R040, R152 | L76-77; L83-84; L180-181 | "up Rs.4.74/Lt compared to Q2 FY26"; "Average milk realisation improved 6% YoY"; "While near-term cost pressures persist, we remain confident in our ability to drive sustainable margin" | FORWARD-SIGNAL | Landed milk cost rose Rs 4.74/L. Derived ASP rose about Rs 3.42/L (60.34 / 1.06 = 56.92). Pass-through was about 72%. The per-litre spread (ASP minus landed cost) fell from about 13.93 to 12.61, about -9.5%. The 271 bps gross-margin fall is consistent with this. Management says pressure "persist[s]" and gives no date or number for the margin improvement claim. Q3 YoY gross margin pressure is pre-signalled. Question: what is the Q3 procurement price trend, and is a further consumer price increase planned? |
| A3-07 | F6 | R150, R153 | L175; L182-183 | "expanding VAP capacity"; "supported by strategic investments" | FORWARD-SIGNAL | This is an undated, unquantified capex commitment. It links to A3-02 (a recurring D&A or interest step-up) and A3-04 (capacity as a possible growth limit). Question: what capacity, at what capex, commissioning when, funded by debt or internal accruals? |
| A3-08 | F6 | R012, R018, R063, R071, R149 | L72-74; L82; L121; L126 | "Milk procurement volumes grew 7% YoY in Q2"; "Village-level outreach is being intensified to strengthen milk availability"; "supported by 2.5% volume growth" | AMBIGUOUS | Procurement (17.28 LLPD, +7%) grew faster than liquid milk sales (12.35 LLPD, +2.5%). The non-liquid-milk draw is about 4.93 LLPD, against a derived 4.10 a year earlier (+20%). Strong VAP volumes (curd +15%, paneer +21%, L90) may absorb it. It may also be commodity conversion (SMP, fat) or an inventory build at inflated cost. The outreach is "underway" with no date. Question: where did the incremental procured milk go? Did inventory or commodity sales rise in Q2? |
| A3-09 | F16 | R095-R100, R101, R102, R133, R134, R135 | L142-144; L146-148; L100 | "profit before tax of INR37 million"; "ranked among the Top 5 yogurt brands, while 71%-owned Get-A-Way recorded robust revenue growth in Q2FY27" | AMBIGUOUS (lean bear) | Disclosure is selective. Nutrivet gets revenue and PBT. The two acquisitions under the header "Strategic Acquisitions Scaling Up" (L146) get a rank and an adjective, with no number. Get-A-Way is 71%-owned, so a minority interest exists. The release does not say whether PAT of INR 309 Mn is total or attributable to owners. A loss at the acquired units is one candidate for the A3-02 drag. Question: give revenue, EBITDA and PBT for Heritage Novandie and Get-A-Way, and PAT attributable to owners. |
| A3-10 | F16 | R035, R037, R040, R042, R050, R052, R055, R057 | L100-101; L111-112 | "21.8%" ... "YoY: (271) bps" ... "YoY: (133) bps" | NEUTRAL-FACT | This is the bull-side counterweight, held to the same bar. Derived opex (gross margin minus EBITDA margin) was 16.2% of revenue against about 17.6% a year earlier, about 138 bps lower. H1 was about 104 bps lower. Operating leverage on 19% revenue growth offset about half of the gross-margin loss. This supports the "operating leverage" claim at L181-182. The test is whether it persists once A3-02 fixed charges are included. |

---

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Press release. No line-item tables. The ledger has 0 ZERO_STANDING rows. |
| F2 Standalone vs consolidated | N.A. | No standalone figures. Only one subsidiary's revenue and PBT are given (L142-144). Decomposition needs the results filing. |
| F3 Shell-entity detection | N.A. | No standalone or consolidated cost lines. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph. The cover says results are "Un-audited" (L31). |
| F5 Going concern / EoM tracking | N.A. | No EoM paragraph. Prior quarter ND. |
| F6 Forward-commitment phrase mining | FINDING | Lexicon hits: "will be" at L39, L191, L195; "shall also be hosted" at L195. Non-lexicon forward language: "is being intensified" (L73-74), "expanding VAP capacity" (L175), "remain confident ... sustainable margin improvement" (L180-181). Findings A3-06, A3-07, A3-08. |
| F7 Hedge phrase mining | PASS | Full lexicon swept with zero hits. There is no safe-harbour paragraph. The cost-pressure qualifier at L180 is a forward signal, logged under F6. |
| F8 Tax forensics | N.A. | No tax line. ETR cannot be computed from the release. |
| F9 OCI forensics | N.A. | No OCI line. |
| F10 Share count and dilution | N.A. | The release carries no EPS or paid-up capital. |
| F11 Reserves and net worth | N.A. | The release carries no net worth or other equity figure. |
| F12 Segment forensics | N.A. | "along with segment results, are available in the Investor section of our website" (L187-188). Segment results are not in this document. |
| F13 Board outcome | N.A. | Cover letter only (L31-37). No board outcome items. |
| F14 Note drafting inconsistencies | N.A. | No notes or auditor letter. Internal metric-definition issues go to F16 (A3-03, A3-05). |
| F15 Entity list diffs | N.A. | No consolidation list. Prior quarter ND. Baseline entity set for next quarter: Heritage Nutrivet Limited (wholly owned subsidiary, L142), Heritage Novandie ("wholly owned yogurt business", L146), Get-A-Way (71%-owned, L147). |
| F16 Dropped and reframed disclosures | FINDING | The prior-deck diff cannot be assessed (prior ND). The in-document framing and definition checks were run: A3-01, A3-02, A3-03, A3-04, A3-05, A3-09, A3-10. |
| F17 Concall silence audit | N.A. | The document is a press release, not a transcript. Notion checklist ND. |

GATE A3: pass. 17 of 17 marked, 0 blank.

---

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Village-level milk procurement outreach intensified | none stated (ongoing) | p2 L73-74 (R149) | underway |
| Expand VAP capacity | none stated | p4 L175 (R150) | none (stated intent) |
| Sustained profitability improvement from mix, volume and pricing | none stated | p4 L176-178 (R151) | none (stated intent) |
| Sustainable margin improvement via premiumisation, cost control and operating leverage, while "near-term cost pressures persist" | none stated; near term excluded by wording | p4 L180-182 (R152) | none (stated intent) |
| Strategic investments behind long-term profitable growth | none stated | p4 L182-183 (R153) | none (stated intent) |
| Earnings call | 16 Oct 2026, 11:00 IST | p4 L191 (R154, R166) | scheduled |
| Investor presentation to be filed with exchanges and hosted on website | none stated | p4 L195-196 (R155) | pending |
| Press release to be uploaded on company website | none stated | p1 L39 (R148) | pending (administrative) |
| Nourish+ High Protein Curd (25g) and Greek Yogurt (8g / 40g) launched | Q2 FY27 | p3 L150-152 (R103-R105, R136-R137) | completed |
| Alpenvie Ice Cream additions and Organic Curd introduced | Q2 FY27 | p4 L158-159 (R138-R139) | completed |
| Curd above 500 tons per day; yogurt above 100 tons for the quarter | Q2 FY27 | p2 L92-93 (R031-R032) | completed |

---

## 5. ROUTING NOTES FOR A4

- Questions for management come from: A3-01, A3-02, A3-03, A3-04, A3-06, A3-07, A3-08, A3-09.
- Get these numbers from the Q2 FY27 results filing, not from this release: D&A, finance cost, other income, tax, exceptional items, minority interest, segment results, standalone figures. They resolve A3-02 and A3-09. They also make F2, F3, F8, F10, F11 and F12 testable on the filing.
- Investor deck (L195) and call transcript (L191): if they are in the run corpus, A4 checks them against A3-02, A3-03 and A3-09.

---

```yaml
stage: A3-forensics
company: "HERITGFOOD"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/heritgfood-q2fy27/work/forensics_pressrelease_heritgfood_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F16", line: "L63-64; L101; L170-171", classification: "AMBIGUOUS", implication: "Headline reports revenue YoY but margin QoQ; omits EBITDA margin -133 bps and PAT -39% YoY. YoY margin trough not yet passed."}
  - {id: "A3-02", check: "F16", line: "L100-101; L111-112", classification: "AMBIGUOUS", implication: "EBITDA -4% YoY vs PAT -39%. Derived EBITDA-minus-PAT drag +158-175 Mn YoY in Q2 vs +15-63 Mn in Q1. Bridge not disclosed. Recurring D&A or interest vs one-off unresolved; lean bear."}
  - {id: "A3-03", check: "F16", line: "L131-132; L136-138; L100", classification: "AMBIGUOUS", implication: "VAP contribution denominator about 12,730 Mn, not consolidated 13,196 Mn. Consolidated VAP mix 1.2-1.6 pp below stated."}
  - {id: "A3-04", check: "F16", line: "L130-131; L136", classification: "FORWARD-SIGNAL", implication: "VAP growth slowed from derived ~39% YoY (Q1) to 32% (Q2), hidden by H1 framing. Possible capacity limit; watch Q3."}
  - {id: "A3-05", check: "F16", line: "L65; L132", classification: "NEUTRAL-FACT", implication: "4.1 is percentage points (35.4-31.3), labelled %. Quote as pp."}
  - {id: "A3-06", check: "F6", line: "L76-77; L83-84; L180-181", classification: "FORWARD-SIGNAL", implication: "Cost +Rs 4.74/L vs derived ASP +Rs 3.42/L, ~72% pass-through, spread -9.5%. 'near-term cost pressures persist' pre-signals Q3 YoY gross-margin pressure."}
  - {id: "A3-07", check: "F6", line: "L175; L182-183", classification: "FORWARD-SIGNAL", implication: "Undated, unquantified VAP capacity and strategic-investment commitment. Links to A3-02 fixed-charge step-up and A3-04 capacity limit."}
  - {id: "A3-08", check: "F6", line: "L72-74; L82; L121; L126", classification: "AMBIGUOUS", implication: "Procurement +7% vs liquid milk sales +2.5%. Non-liquid draw 4.93 LLPD vs derived 4.10 (+20%). VAP absorption vs commodity or inventory build at inflated cost."}
  - {id: "A3-09", check: "F16", line: "L142-144; L146-148; L100", classification: "AMBIGUOUS", implication: "Nutrivet gets revenue and PBT; Novandie and 71%-owned Get-A-Way get no numbers. PAT basis (total vs owners) not stated. Possible source of A3-02 drag; lean bear."}
  - {id: "A3-10", check: "F16", line: "L100-101; L111-112", classification: "NEUTRAL-FACT", implication: "Derived opex/revenue -138 bps YoY (H1 -104 bps) offset about half the 271 bps gross-margin loss. Supports operating-leverage claim before fixed charges."}
forward_signals: ["A3-04", "A3-06", "A3-07"]
ambiguous: ["A3-01", "A3-02", "A3-03", "A3-08", "A3-09"]
commitments:
  - {commitment: "Village-level milk procurement outreach intensified", implied_date: "none stated (ongoing)", ref: "p2 L73-74 (R149)", status_word: "underway"}
  - {commitment: "Expand VAP capacity", implied_date: "none stated", ref: "p4 L175 (R150)", status_word: "none (stated intent)"}
  - {commitment: "Sustained profitability improvement from mix, volume and pricing", implied_date: "none stated", ref: "p4 L176-178 (R151)", status_word: "none (stated intent)"}
  - {commitment: "Sustainable margin improvement; near-term cost pressures persist", implied_date: "none stated; near term excluded", ref: "p4 L180-182 (R152)", status_word: "none (stated intent)"}
  - {commitment: "Strategic investments behind long-term profitable growth", implied_date: "none stated", ref: "p4 L182-183 (R153)", status_word: "none (stated intent)"}
  - {commitment: "Earnings call", implied_date: "2026-10-16 11:00 IST", ref: "p4 L191 (R154, R166)", status_word: "scheduled"}
  - {commitment: "Investor presentation filed with exchanges and hosted on website", implied_date: "none stated", ref: "p4 L195-196 (R155)", status_word: "pending"}
  - {commitment: "Press release uploaded to company website", implied_date: "none stated", ref: "p1 L39 (R148)", status_word: "pending"}
  - {commitment: "Nourish+ High Protein Curd and Greek Yogurt launched", implied_date: "Q2 FY27", ref: "p3 L150-152 (R136-R137)", status_word: "completed"}
  - {commitment: "Alpenvie Ice Cream additions and Organic Curd introduced", implied_date: "Q2 FY27", ref: "p4 L158-159 (R138-R139)", status_word: "completed"}
  - {commitment: "Curd >500 tons/day; yogurt >100 tons in quarter", implied_date: "Q2 FY27", ref: "p2 L92-93 (R031-R032)", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The release gives headline numbers only. It has no line below EBITDA, no segment results, no tax and no share data, so most checks are N.A. here and testable on the results filing. The load-bearing signal is A3-02. Q2 EBITDA fell 4% YoY while PAT fell 39%. Derived from the stated growth rates, the EBITDA-minus-PAT drag rose about Rs 16-17 Cr YoY in Q2 against Rs 2-6 Cr in Q1. It also rose Rs 6 Cr sequentially, so something new hit in Q2. Candidates: D&A or interest from VAP capacity or acquisitions, lower other income, tax, or a base-quarter one-off. The release gives Nutrivet's PBT but no numbers for Novandie or Get-A-Way (A3-09), so the reading leans bear until the filing resolves it. VAP share uses a base about Rs 47 Cr below consolidated revenue (A3-03). Bull side: opex fell about 138 bps of revenue, offsetting half the gross-margin loss (A3-10). Milk cost pass-through was about 72%, and management says cost pressure persists. A1 line cites drift 1-3 lines on 45 rows. All values match; the findings cite actual fulltext lines."
```
