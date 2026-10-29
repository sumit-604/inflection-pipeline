# A3 FORENSIC NOTES: Route Mobile (ROUTE) Q2FY27, doctype pressrelease (narrative release; presentation-class structure)

Agent: A3 forensics | Model: claude-opus-5-5 | Run date: 2026-10-29
Inputs read: A1 structured (R001-R074), A1 fulltext (131 lines + header), A2 ledger, Q1FY27 prior release extract, Notion monitoring checklist extract (29-Oct-2026). No source PDF and nothing under inputs/ was opened.
Line numbers: Q2 lines = A1 fulltext line numbers. "prior line N" = Q1FY27 extract line numbers.
Derived numbers are arithmetic on two or more filed figures and are labelled "derived". Nothing is estimated.

## 0. LEDGER RECONCILIATION

- Rows in ledger: 74 (R001-R074). Rows read verbatim at their cited fulltext line: 74. Reconciled: 100%.
- Every cited line matched its structured value (spot-tied each R### to its line; multi-line rows R036/R069 lines 48-49, R054 lines 128-131, R055-R059, R062 all tie).
- A2 count test ties: page-level numbers p1 8, p2 26, p3 7 = 41. Entities 13 + R054 summary = 14, as A2 states.
- Minor A1 notes, no impact: R041 is an email address captured under NUMBER (over-capture, flagged by A1). A1 header line_count 131 matches the last text line 131.
- Ligature drops ("Proit", "irst", "signiicant") are extraction artefacts, not document errors. They are not counted under F14.
- Grep on the Q2 fulltext for truecaller / ebitda / guidance / traffic / cash / dividend / buyback / delist / open offer / subject to / underway / will be / expected: one hit only, "guidance" at line 94.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN01 | F1 | R008, R009, R010, R011, R071 | 71-72 | "Proit Before Tax and Exceptional items stands at Rs 100.93 crore as against Rs. 137.87 crore in Q2FY26" / "Proit Before Tax stand at Rs 100.93 crore as against Rs 2.00 crore in Q2FY26" | AMBIGUOUS | Q2FY27 exceptional line is nil (derived: R008 = R010). Q2FY26 carried an exceptional charge of Rs 135.87 crore (derived: 137.87 - 2.00) that the release never names. The pre-exceptional bullet is new versus the Q1 release (prior lines 66-69 carry no such line). A4: name the Q2FY26 item and ask whether any residual (reversal, recovery, tax true-up, further charge) is open in H2 FY27. |
| FN02 | F6 | R040, R056 | 94-95 | "alongside a recovery in gross proit margin compared with the previous quarter" | FORWARD-SIGNAL | Status change on the Q1 margin commitment. Q1: "these are already being actively addressed through targeted actions to support margin recovery" and "With these initiatives already underway" (prior lines 89-92). Q2: recovery claimed, no number. Q1 GM was 20.88% (checklist Step 6B). Checklist red leg 2 (<22% for 2 consecutive quarters) cannot be tested from this release. Tracker: underway -> partial delivery claimed, unverified. |
| FN03 | F6 | R055, R057, R058, R064 | 96-99 | "We are seeing an encouraging pipeline for these offerings and remain focused on converting these opportunities into revenue" | FORWARD-SIGNAL | Heltar moves to "completed on July 29" (line 97). The follow-on commitment (pipeline to revenue) carries no date, no size and no KPI. The promise-vs-delivery tracker can only score it when a revenue number appears. Checklist item 14 green test (Rs 5+ Cr/quarter by Q2 FY27) is not met at release level. |
| FN04 | F8 | R005, R008, R010, R012, R019, R022 | 72-73, 81, 84 | "Proit After Tax, reported was at Rs 82.55 crore" | AMBIGUOUS | Derived ETR (PBT - PAT reported) / PBT: Q2FY27 18.21% (tax 18.38 on 100.93); Q1FY27 25.06% (22.92 on 91.47); Q4FY26 17.84% (24.84 on 139.27, prior lines 77, 80); Q1FY26 23.23% (17.79 on 76.57, prior lines 67-68); Q2FY26 n.m. (tax 20.83 on PBT 2.00). Q2 sits 696 bps below statutory 25.17%, a shield of Rs 7.02 crore (derived). At the Q1 ETR, Q2 PAT would be Rs 75.64 crore: Rs 6.91 crore, or 49% of the Rs 14.00 crore QoQ PAT rise, comes from the lower tax rate. Caveat: if "PAT reported" is after minority interest, the derived tax includes the NCI share. A4: ask the ETR drivers (deferred tax, prior-year adjustment, jurisdiction mix). Lean bear: treat the Q2 rate as non-recurring until shown otherwise. |
| FN05 | F10 | R005, R012, R014, R015, R074 | 74 | "EPS stands at Rs. 12.63 (basic) and Rs. 12.63 (diluted) for Q2FY2027" | AMBIGUOUS | Implied weighted share count (PAT reported / EPS, derived): Q2FY27 6.5360 crore; Q1FY27 6.8964 crore (68.55 / 9.94, prior lines 68-69). Fall of 0.36 crore shares, 5.2% QoQ. EPS rounding (+/-0.005) moves each count by under 0.04%, so the gap is real. Candidate readings: (a) a buyback or other share reduction, which the release never mentions (capital-return watch); (b) EPS computed on owners' PAT that differs from "PAT reported" by a changing NCI share. Basic = diluted in both quarters: spread zero, no new dilution signal. A4 cross-checks paid-up capital and the ESOP pool against Notion. |
| FN06 | F14 | R029/R060, R030/R061, R036/R069 | 21, 48-49, 63 | "Mumbai, October 27, 2026" vs "Date: October 28, 2026" and "Date: 2026.10.28 / 00:03:52 +05'30'" | AMBIGUOUS | Release dated 27-Oct, cover letter dated 28-Oct, signed 3 min 52 s after midnight. Q1 was dated, covered and signed on one day (prior lines 17, 44-45, 60: July 23, signed 22:12:03). The release carries no board-meeting end time, so Reg 30 timeliness cannot be tested here. Low materiality. A4: confirm board conclusion time from the outcome filing. |
| FN07 | F14 | R064, R032, R033, R031 | 97, 100, 74, 31, 59 | "completed on July 29" / "business.,\" added Mr. Tushar Agnihotri" | NEUTRAL-FACT | Drafting tally: completion date carries no year (line 97); stray punctuation "business.," (line 100); period labels mix "Q2FY2027" (line 74), "Q2 FY27" (line 31, 94) and "Q2FY27" (line 59). Individually immaterial; cumulatively a looser draft than Q1. |
| FN08 | F15 | R048, R064 | 88, 96-97 | "The acquisition of Heltar's business, completed on July 29" | FORWARD-SIGNAL | New entity versus the Q1 release (no Heltar mention in prior lines 54-126). The release calls it a business acquisition and does not state the consolidation basis or the consideration. Q2 holds about two months of Heltar from 29-Jul. QoQ revenue rose Rs 28.16 crore, 2.45% (derived), with no organic / inorganic split, so organic growth may be lower than headline. Q3 carries a full quarter, which shifts the QoQ base again. Checklist item 15 (M&A pace) stays unscorable: consideration undisclosed for a second quarter. |
| FN09 | F16 | R040 | 94 | "We delivered revenue performance in Q2 FY27 in line with our guidance" | AMBIGUOUS | First release-level reference to guidance; the Q1 release carries none (prior lines 82-94). No guidance number appears anywhere in the release. Derived growth: revenue +5.38% YoY (60.25 on 1,119.42), +2.45% QoQ. A4: ask the guidance figure, its basis (YoY, constant currency, organic) and where it was given. |
| FN10 | F16 | R004, R005, R007, R008, R009, R013, R020 | 61, 71, 73 | "Q2FY27 Revenue from operations stands at Rs. 1,179.67 crore, PAT stands at Rs. 82.55 crore" | CONFIRMATORY-NEGATIVE | The headline leads with revenue and PAT. PAT is compared with a Q2FY26 loss of Rs (18.83) crore (line 73). The like-for-like read is pre-exceptional PBT: down 26.79% YoY (100.93 vs 137.87, derived); pre-exceptional PBT margin 12.32% in Q2FY26 vs 8.56% now, a 376 bps compression (derived). The release discloses this; the headline does not lead with it. Confirms the margin pressure the thesis already tracks. |
| FN11 | F16 | R046, R056, R059, R070 | 89-92 | "we recognize the importance of translating business momentum into sustainable proitability and delivering value for shareholders. As we review our irst-half performance, our priorities remain disciplined execution, prudent cost management" | FORWARD-SIGNAL | Narrative shift. Q1 Chairman: "The underlying demand for our solutions remains strong, resulting in healthy traffic growth" (prior lines 83-84). Q2 drops demand and traffic language. The Chairman, who is also CEO of the parent, now speaks of profitability, cost management and a first-half review. Forward statements fall from 9 to 5 (A2 ledger line 3). Bear reading: parent pressure on profitability, with an H2 cost or restructuring action possible; the exceptional-items line (FN01) is the place it would land. Bull reading: routine emphasis after a margin recovery quarter. Separating observation: any H2 restructuring charge or announced cost programme. |
| FN12 | F16 | R020, R040 | 82, 95-96 | "The company's PBT margin stood at 8.56 %." / "New product revenues also recorded a signiicant increase" | AMBIGUOUS | PBT margin is the only margin in the release. No EBITDA, no Adjusted EBITDA, no gross margin figure, no new-product number. The Q1 checklist values (EBITDA 9.5% / reported ~9.16%, GM 20.88%, new products 13.9% YoY) came from the deck, not the release, so this is not a dropped release metric. It does mean the decisive thesis-broken test (Adjusted EBITDA <10% for a second consecutive quarter) cannot be fired or cleared from this document. The 62 bps QoQ PBT margin rise (7.94% prior line 78 to 8.56%) includes other income and D&A, so it is not an EBITDA proxy. A4: source Q2 Adjusted EBITDA, GM and new-product YoY from the Q2 results filing or deck before any status call. |
| FN13 | F17 | R057, R059 (absence test) | 94-100 | "New product revenues also recorded a signiicant increase, relecting the contribution of our expanding solutions portfolio" | AMBIGUOUS | Truecaller Business Messaging is not named anywhere in the release (grep nil). Checklist item 13: Q1 = silence 1 of 3; Q2 release = silence 2 of 3. The green deadline ("disclosed by Q2 FY27 with material INR attribution, Rs 15+ Cr/quarter") is missed at release level. One more silent quarter turns item 13 red. Lean bear. |
| FN14 | F17 | R046, R047, R058 (absence test) | 86-100 | "remain focused on converting these opportunities into revenue while maintaining disciplined execution across the business" | AMBIGUOUS | The Q1 CEO commitments "rebuilding traffic with existing customers, expanding new customer relationships" (prior line 91) get no Q2 mention. Checklist item 7 carried one account with a "transitory traffic reduction" at Q1. Q2 drops all traffic language (see FN11). Items 6 (top 10 concentration) and 7 (large-client loss) are silent. Silence on a watched deterioration leans confirmatory-negative if it persists into Q3. |
| FN15 | F17 | R045, R049, R052 (absence test) | 63, 104, 110 | "Route Mobile is now a part of Proximus Group" | NEUTRAL-FACT | Structural silence of the doctype. The release carries no balance-sheet, cash-flow or shareholding data in Q1 or Q2, so items 3 (CFO/PAT), 4 (DSO), 10 (cash), 11 (Proximus holding) and the capital-return, delisting and open-offer watch are all silent. Parentage is restated three times (lines 63, 104, 110); "a Proximus Global company" is newly added to the About paragraph (line 104 vs prior line 98). No delisting or open-offer note. These items need the results filing and shareholding pattern, not this release. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | No ZERO_STANDING ledger rows. The pre-exceptional PBT line shows a nil Q2FY27 exceptional item and an unnamed Q2FY26 charge of Rs 135.87 crore (derived); line new versus Q1 release (FN01). |
| F2 | N.A. | Release reports consolidated figures only (R073, lines 68, 76); no standalone figures to decompose. |
| F3 | N.A. | No standalone cost lines in a press release. |
| F4 | N.A. | No auditor report or Other Matters paragraph in the release. |
| F5 | N.A. | No EoM or going-concern paragraph in the Q2 release or the Q1 prior extract; nothing to verbatim-diff. |
| F6 | FINDING | Strict lexicon: zero exact hits. Status words found: "completed" (line 97), "remain focused" (lines 98-99). Q1 "already underway" margin actions move to a claimed GM recovery (FN02); Heltar completed with an undated revenue-conversion commitment (FN03). Register below. |
| F7 | PASS | Hedge lexicon run on lines 18-131: zero hits ("subject to", "evaluating", "exploring", "in discussions", "endeavour", "no assurance" all nil). Q1 release also carries none. Neither release has a safe-harbour paragraph. Soft verb "can support" (line 87) is outside the lexicon. |
| F8 | FINDING | PBT and PAT are carried, so ETR is derivable. Q2FY27 18.21% vs Q1FY27 25.06% vs statutory 25.17%; 49% of QoQ PAT rise from the lower rate (FN04). No tax line or prior-year adjustment is disclosed. |
| F9 | N.A. | No OCI or actuarial data in the release. |
| F10 | FINDING | Basic = diluted (12.63 / 12.63; Q1 9.94 / 9.94): spread zero. EPS-implied share count falls 5.2% QoQ, outside rounding (FN05). |
| F11 | N.A. | No paid-up capital, other equity or net worth figures in the release. |
| F12 | N.A. | No segment revenue, result, asset or liability data in the release. |
| F13 | N.A. | Release reports no board outcome beyond results (no AR approval, AGM, director appointment, enabling resolution). The board outcome filing was not passed to A3. |
| F14 | FINDING | Dateline 27-Oct vs filing and signature 28-Oct 00:03:52, unlike the Q1 same-day pattern (FN06); drafting tally (FN07). |
| F15 | FINDING | Heltar is a new entity versus the Q1 release; consideration and consolidation basis undisclosed; no organic split (FN08). No other entity additions, deletions or relationship changes (Telesign, BICS, Proximus Group unchanged versus prior lines 103, 109). |
| F16 | FINDING | No release metric dropped versus Q1 (Q1 bullets revenue / PBT / PAT / EPS all present; pre-exceptional PBT added). Reframes: unquantified guidance claim (FN09), PAT-led headline over a loss base (FN10), narrative shift from demand and traffic to profitability and cost (FN11), unquantified GM and new-product claims with no EBITDA (FN12). |
| F17 | FINDING | No concall exists for Q2. The silence audit runs against this release, the only management voice of the quarter, as the task message directs. Counts are release-level and noted as such (FN13, FN14, FN15; table in section 4). |

## 3. COMMITMENT REGISTER (from F6)

| # | commitment | implied date | ref | status word |
|---|---|---|---|---|
| C1 | Acquisition of Heltar's business (conversational AI) | 29-Jul (year not stated; 2026 implied by the Q2 window) | lines 88-89, 96-97 (R048, R055, R064) | completed |
| C2 | Convert the Heltar / new-offering pipeline into revenue | undated | lines 98-99 (R057, R058) | underway (implied: "remain focused on converting") |
| C3 | Margin recovery through targeted actions (Q1: "already being actively addressed", "initiatives already underway", prior lines 89-92) | undated; Q2 claims GM recovery QoQ | lines 94-95 | underway -> partial delivery claimed (no number) |
| C4 | Revenue in line with guidance | Q2 FY27 | line 94 (R040) | completed (claimed; guidance figure not stated) |
| C5 | Priorities: disciplined execution, prudent cost management, foundation for the future | H2 FY27 implied ("As we review our first-half performance") | lines 91-92 (R056, R070) | underway (implied) |
| C6 | Translate business momentum into sustainable profitability and shareholder value | undated | lines 89-91 (R046) | initiated (recognition statement, no action named) |
| C7 | Strengthen core business; expand into differentiated, higher-value solutions | undated | lines 86-88 (R059) | underway |
| C8 | Q1 carry-forward: rebuild traffic with existing customers; expand new customer relationships | undated | prior line 91; not repeated in Q2 | no Q2 status (silent) |

## 4. WHAT WAS NOT DISCUSSED (F17; release-level, no Q2 concall)

Count basis: consecutive quarters with no figure in management communication held by this pipeline. Q1 readings in Notion came from the Q1 deck and concall, so a Q1 figure resets the count to start at Q2. If a Q2 deck or results filing carries the figure, the count for that item falls to zero.

| # | checklist item / commitment | Q2 release coverage | line | consecutive silent quarters |
|---|---|---|---|---|
| 1 | Gross margin (consol) | qualitative only: "recovery in gross proit margin" | 94-95 | number silent 1 (Q2); red leg 2 untestable |
| 2 | Adj. EBITDA margin (thesis-broken trigger) | absent; PBT margin 8.56% only | 82 | 1 (Q2); trigger 1 UNRESOLVED by this document |
| 3 | CFO/PAT trailing 4Q | absent | - | 2 (Q1 ND, Q2) |
| 4 | DSO / receivables | absent | - | 2 (Q1 ND, Q2) |
| 5 | New products revenue YoY | qualitative only: "signiicant increase" | 95-96 | number silent 1 (Q2) |
| 6 | Top 10 client concentration | absent | - | 1 (Q2) |
| 7 | Loss of large enterprise clients / traffic | absent; traffic language dropped | - | 1 (Q2) |
| 8 | Proximus cross-sell revenue | absent; Proximus named as parent only | 63, 104, 110, 115 | 2 (Q1 not disclosed, Q2) |
| 9 | Rs 113 Cr arbitration | absent; closed GREEN at Q1 (settled 19-Feb-2026) | - | n/a (closed) |
| 10 | Cash position | absent | - | 1 (Q2) |
| 11 | Proximus holding / delisting / open offer | parentage restated; no holding figure, no delisting or open-offer note | 63, 104, 110 | 2 (Q1 not disclosed, Q2) |
| 12 | CEO continuity | addressed: Agnihotri (CEO) and Arikan (Chairman) both quoted | 86, 100 | 0 |
| 13 | Truecaller BM revenue KPI | absent (grep nil) | - | 2 of 3 to red (Q1, Q2) |
| 14 | Heltar integration | partial: completion date and pipeline; no consideration, no revenue, no founder status | 96-99 | consideration silent 2 (Q1, Q2); revenue attribution silent 1 |
| 15 | Aggregate FY27 M&A pace | one deal known; consideration absent | 96-97 | 2 (Q1, Q2) |
| C8 | Q1 traffic rebuild and new customer relationships | absent | - | 1 (Q2) |
| - | Capital return (dividend, buyback) | absent; EPS-implied share count falls 5.2% (FN05) | 74 | 1 (Q2) at release level |

## 5. FLAGS FOR A4 (questions to convert)

FORWARD-SIGNAL: FN02, FN03, FN08, FN11.
AMBIGUOUS: FN01, FN04, FN05, FN06, FN09, FN12, FN13, FN14.
Priority for A4: FN12 (thesis-broken test needs the Q2 Adjusted EBITDA from another document), FN05 (share count), FN04 (tax quality of PAT), FN01 (the unnamed Q2FY26 exceptional item).

## 6. YAML BLOCK

```yaml
stage: A3-forensics
company: "ROUTE"
quarter: "q2fy27"
doctype: "pressrelease"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/route-q2fy27/work/forensics_route_q2fy27_pressrelease.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "FN01", check: "F1", line: "71-72", classification: "AMBIGUOUS", implication: "Q2FY27 exceptional nil (R008=R010); Q2FY26 exceptional charge Rs 135.87 cr derived (137.87-2.00) unnamed; new line vs Q1; ask the item and any H2 residual"}
  - {id: "FN02", check: "F6", line: "94-95", classification: "FORWARD-SIGNAL", implication: "Q1 'already underway' margin actions -> Q2 GM recovery claimed QoQ, no number; checklist GM red leg 2 (<22% 2Q) untestable"}
  - {id: "FN03", check: "F6", line: "96-99", classification: "FORWARD-SIGNAL", implication: "Heltar completed 29-Jul; pipeline-to-revenue commitment undated and unsized; item 14 green test not met at release level"}
  - {id: "FN04", check: "F8", line: "72-73,81,84", classification: "AMBIGUOUS", implication: "Derived ETR 18.21% vs Q1 25.06% vs statutory 25.17%; Rs 6.91 cr = 49% of QoQ PAT rise from lower tax; treat as non-recurring until drivers shown"}
  - {id: "FN05", check: "F10", line: "74", classification: "AMBIGUOUS", implication: "EPS-implied shares 6.5360 cr vs Q1 6.8964 cr (-5.2%, beyond rounding): undisclosed buyback or EPS on owners' PAT differing from PAT reported; basic=diluted"}
  - {id: "FN06", check: "F14", line: "21,48-49,63", classification: "AMBIGUOUS", implication: "Dateline 27-Oct vs filing and signature 28-Oct 00:03:52; Q1 was same-day; Reg 30 timing untestable without board end time"}
  - {id: "FN07", check: "F14", line: "97,100,74", classification: "NEUTRAL-FACT", implication: "Drafting tally: completion date with no year, stray punctuation, mixed period labels"}
  - {id: "FN08", check: "F15", line: "88,96-97", classification: "FORWARD-SIGNAL", implication: "Heltar new vs Q1; consideration and consolidation basis undisclosed; ~2 months in Q2 with no organic split of +2.45% QoQ revenue; Q3 base shifts again"}
  - {id: "FN09", check: "F16", line: "94", classification: "AMBIGUOUS", implication: "First release-level guidance reference; no guidance number; revenue +5.38% YoY, +2.45% QoQ derived"}
  - {id: "FN10", check: "F16", line: "61,71,73", classification: "CONFIRMATORY-NEGATIVE", implication: "Headline PAT vs a loss base; pre-exceptional PBT -26.79% YoY, margin 12.32% -> 8.56% (-376 bps) derived"}
  - {id: "FN11", check: "F16", line: "89-92", classification: "FORWARD-SIGNAL", implication: "Chairman (parent CEO) shifts from demand/traffic (prior 83-84) to profitability, cost management and H1 review; fwd statements 9 -> 5; bear read H2 cost or restructuring action"}
  - {id: "FN12", check: "F16", line: "82,95-96", classification: "AMBIGUOUS", implication: "No EBITDA, GM or new-product number; thesis-broken trigger 1 (Adj EBITDA <10% 2Q) cannot be fired or cleared from this release; PBT margin +62 bps QoQ is not an EBITDA proxy"}
  - {id: "FN13", check: "F17", line: "94-100", classification: "AMBIGUOUS", implication: "Truecaller BM absent; silence 2 of 3 to red; Q2 FY27 green deadline missed at release level"}
  - {id: "FN14", check: "F17", line: "86-100", classification: "AMBIGUOUS", implication: "Q1 traffic-rebuild and new-customer commitments (prior 91) silent; items 6 and 7 silent; leans confirmatory-negative if Q3 silent"}
  - {id: "FN15", check: "F17", line: "63,104,110", classification: "NEUTRAL-FACT", implication: "Doctype-structural silence on cash, CFO, DSO, holding, capital return; parentage restated, no delisting or open-offer note"}
forward_signals: ["FN02", "FN03", "FN08", "FN11"]
ambiguous: ["FN01", "FN04", "FN05", "FN06", "FN09", "FN12", "FN13", "FN14"]
commitments:
  - {commitment: "Acquisition of Heltar's business", implied_date: "29-Jul (2026 implied)", ref: "lines 96-97", status_word: "completed"}
  - {commitment: "Convert Heltar/new-offering pipeline into revenue", implied_date: "undated", ref: "lines 98-99", status_word: "underway"}
  - {commitment: "Margin recovery via targeted actions (Q1 underway)", implied_date: "undated", ref: "lines 94-95; prior 89-92", status_word: "underway"}
  - {commitment: "Revenue in line with guidance", implied_date: "Q2 FY27", ref: "line 94", status_word: "completed"}
  - {commitment: "Disciplined execution and prudent cost management", implied_date: "H2 FY27 implied", ref: "lines 91-92", status_word: "underway"}
  - {commitment: "Translate momentum into sustainable profitability", implied_date: "undated", ref: "lines 89-91", status_word: "initiated"}
  - {commitment: "Expand into differentiated higher-value solutions", implied_date: "undated", ref: "lines 86-88", status_word: "underway"}
  - {commitment: "Q1 carry: rebuild traffic, expand new customers", implied_date: "undated", ref: "prior line 91", status_word: "silent in Q2"}
gate_a3: pass
blank_checks: []
analyst_note: "This release cannot settle the decisive Q2 test. Thesis-broken trigger 1 needs Q2 Adjusted EBITDA. The only margin given is PBT 8.56% (line 82). PBT carries other income and D&A, so its 62 bps QoQ gain is not an EBITDA proxy. A4 must source EBITDA and gross margin from the Q2 results filing or deck before any status call. Two derived numbers carry weight. First, Rs 6.91 of the Rs 14.00 crore QoQ PAT rise comes from a lower effective tax rate (18.21% vs 25.06%). Q4FY26 also ran near 17.8%, so the Q1 rate may be the outlier, but PAT quality is weaker than the headline. Second, EPS implies 5.2% fewer shares than Q1. That is either a buyback the release never mentions or an EPS base that differs from PAT reported. Either answer matters for capital return or minority interest. The Chairman is also the parent CEO. He moves from demand and traffic in Q1 to profitability, cost discipline and a first-half review. With the exceptional line kept, the bear reading is an H2 cost or restructuring action. F17 counts are release-level only; no concall exists."
```
