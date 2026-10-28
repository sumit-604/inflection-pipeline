# A3 FORENSIC NOTES: SONACOMS Q2 FY27, doctype PRESSRELEASE (presentation-class)

Agent: A3 forensic notes | Model: claude-opus-5-5 | Run date: 2026-10-28
Inputs read:
- A1 structured: runs/sonacoms-q2fy27/extracted/sonacoms-pressrelease-q2fy27-structured.md (R001-R127)
- A1 fulltext: runs/sonacoms-q2fy27/extracted/sonacoms-pressrelease-q2fy27-fulltext.md (L1-L196, 4 pages)
- A2 ledger: runs/sonacoms-q2fy27/work/ledger_pressrelease_sonacoms_q2fy27.md (127 IDs, gate_a2 pass)
- Prior-quarter fulltext: NOT AVAILABLE (no prior SONACOMS extraction in the repo)
- Notion COMPANIES MASTER page, fetched 28-Oct-2026 (operator memory, not corpus): properties block, Q1 FY27 press-release layer note (PR-FD rows), 26-Oct-2026 gate review.

Source discipline: no source PDF and nothing under inputs/ was opened. Cross-document numbers marked [NOTION MEMORY] come from the Notion page. They are memory to weigh, not anchored evidence. A4 must anchor them to the Q2 results filing and deck before use. Numbers marked [my arithmetic] are computed here from release figures.

---

## 0. LEDGER RECONCILIATION

Rows in ledger: 127 (R001-R127). Rows read verbatim in the fulltext: 127. Reconciled: 100%. Orphans: none. Missing from structured: none.

Every row's value was found verbatim in the fulltext. A1 line cites drift on these rows (content present, line placeholder wrong). This is a pipeline QC note, not a document finding:

| Rows | A1 cite | Actual location in fulltext |
|---|---|---|
| R002 | L22 | "400 051" L21; "400 001" L23 |
| R044 | L126 | "Rs 7.0 billion" L125 |
| R098 | L55 | "Q2 FY27" L56 (L55 blank) |
| R053-R058 | L24 (all) | NSE L18, BSE L20, SEBI L30-31, issuer L40, signatory L47-49 |
| R059-R067 | page 2 L91 (all) | CEO L87; Deming/JUSE/Driveline L110-111 (page 3, not page 2); programmes L74-76, L83; Sona Comstar 2.0 L99 |
| R068-R079 | L124 (all) | customers and products L117-149 |
| R080-R085 | L163 (all) | L162-176 |

A2 handoff item "R044-R049 sum Rs 29.2bn vs R005/R036 Rs 36bn; A3 to reconcile": reconciled in A3-PR-F14-03.

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-PR-F6-01 | F6 | R046, R088, R109 | L132-135 | "additional traction motor volumes under an existing order ... expected to commence in H2 FY27" | FORWARD-SIGNAL | Nearest dated SOP, inside the current year. Rs 12.5bn is 34.7% of Q2 additions [my arithmetic] and is an upsize, not a new program. Score at Q3/Q4 FY27. EV 2W traction motors sit in the EV-motors business being slump-sold into eDrive, where DENSO takes 49% [NOTION MEMORY]. Which entity books these volumes? |
| A3-PR-F6-02 | F6 | R086-R091, R107-R112, R124 | L126, L130, L135, L141, L145, L151 | "production expected to commence in H1 FY29" | FORWARD-SIGNAL | Six SOPs, all "expected". Itemised Rs 29.2bn phases: H2 FY27 Rs 12.5bn; H1 FY28 Rs 3.8bn; H2 FY28 Rs 2.6bn; H1 FY29 Rs 10.3bn. 44% of itemised value (Rs 12.9bn) starts H2 FY28 or later [my arithmetic]. Most of the quarter's book converts inside the FY29 base window, only late. Feeds Role 5 tracker and FTTCP catalyst timeline. |
| A3-PR-F6-03 | F6 | R039, R092, R064 | L99 | "greater confidence in our 10X ambition under Sona Comstar 2.0" | AMBIGUOUS | Undated and no base metric. The Q1 release dated it "next decade to FY35" [NOTION MEMORY, Q1 press-release layer note]; no prior fulltext, so the horizon drop is unverified. Ask: 10X of what, from which base year, by when. |
| A3-PR-F14-01 | F14 | R007, R011, R012, R117 | L69, L71 | "Revenue of Rs. 1,547 crores" / "EBITDA of Rs. 356 crores with a margin of 23.0%" | AMBIGUOUS | Revenue basis not labelled. Results revenue from operations is Rs 1,535.8 Cr and net forex gain Rs 10.6 Cr [NOTION MEMORY]. Rs 1,547 Cr matches revenue including forex (deck basis). The 23.0% margin then sits exactly on the bear line (<23.0%) of the binding gate. The operator ruling on forex inclusion is pending. Ask: confirm the release revenue and EBITDA include net forex, and state EBITDA ex-forex. |
| A3-PR-F14-02 | F14 | R114, R007-R026 | L32-33 vs L69-83 | "unaudited Standalone and Consolidated Financial Results" | NEUTRAL-FACT | The cover letter names both bases. The headline set (L69-83) carries no standalone or consolidated label. PAT Rs 223 Cr matches consolidated owners' PAT Rs 223.4 Cr, not standalone Rs 197.4 Cr [NOTION MEMORY]. Repeats Q1 PR-FD1. Second release in a row with an unlabelled basis. |
| A3-PR-F14-03 | F14 | R017-R019, R005, R036, R044-R049, R123 | L74-76; L60; L124-151 | "three BEV programs, one Intelligent and connected solution program and three ICE programs" | AMBIGUOUS | Seven programs claimed. Six itemised: three BEV, two ICE, one radar. Itemised orders total Rs 29.2bn against Rs 36bn headline (L60, L96). Rs 6.8bn (18.9%) is not itemised [my arithmetic]. The deck carries a third ICE tile of Rs 2.0bn and still leaves Rs 4.8bn unitemised [NOTION MEMORY]. The largest "BEV program" is an upsize "under an existing order" (L133). Ask: list the Rs 6.8bn; does the program count include upsizes? |
| A3-PR-F14-04 | F14 | R115, R120, R006, R028, R118 | L83 (also L60, L96) | "net order book* of Rs. 25,100 crores." | AMBIGUOUS | The asterisk has no footnote anywhere in L1-196. "Net" is not defined. Q1 open question on delay discount and EOL haircut is still unanswered [NOTION MEMORY, Q1 question 6 / N11]. Deck bridge shows Rs 25bn consumed on Rs 15.5bn revenue, 1.6x [NOTION MEMORY]. Ask: footnote text, gross book, haircut method, consumption definition. |
| A3-PR-F14-05 | F14 | R035, R043, R073, R075, R049, R091, R086 | L116-118 vs L149-151 and L126 | "commercialised three new products in Q2 FY27 ... rear radar sensors for two-wheelers" vs "production expected to commence in H2 FY28" | AMBIGUOUS | "Commercialised" is not defined. The only radar order shown starts H2 FY28. The only LSD order shown starts H1 FY29. So the Q2 commercialisation is with an unnamed earlier customer, or it is not SOP. The 26-Oct Notion review scored promise C3 "partly delivered" on this line. Ask: customer, Q2 revenue booked, and SOP date for each of the three products. |
| A3-PR-F14-06 | F14 | R004, R009, R121 | L59 vs L70 | "51% of Automotive revenues" vs "Revenue share from BEVs reached an all-time high of 51% in Q2" | NEUTRAL-FACT | The bullet drops the "Automotive" base given in the headline. The base excludes railway. BEV share of total revenue is lower and is not stated. The Q1 annualisation flag is fixed: L70 labels the figure "in Q2". |
| A3-PR-F16-01 | F16 | R027, R028 | L83 | "EV and Robotics & Physical AI programs contribute 65% to the net order book*" | FORWARD-SIGNAL | Metric redefined. Q1 EV-only share was 64%; the Q2 deck shows EV-only 61% (Rs 152bn of Rs 251bn) [NOTION MEMORY]. The release adds Robotics & Physical AI to the numerator. The headline then reads 65%, up from 64%, while EV-only eased for a third straight print (tripwire 9). The gap of about 4 pp implies about Rs 10-11bn of Robotics & Physical AI book [my arithmetic on a memory number], against about 1% of H1 revenue [NOTION MEMORY]. Ask: EV-only share and the Robotics & Physical AI order book in rupees. |
| A3-PR-F16-02 | F16 | R013, R008, R021, R022, R023, R026 | L71, L80-82, L58 | "EBITDA of Rs. 658 crores with an EBITDA margin of 23.0%" | CONFIRMATORY-NEGATIVE | H1 EBITDA is the only H1 headline with no YoY growth. Revenue (+43%, L80) and PAT (+36%, L82) carry one. Q2 EBITDA grew 23% against revenue 35% (L69, L71). Implied Q2 FY26 margin is about 25.3% (Rs 289 Cr / Rs 1,146 Cr), so about 220 bps YoY compression, within about 40 bps for rounded growth rates [my arithmetic]. The release headline says "Highest-ever ... EBITDA" (L58) and never states the margin decline. Repeats the Q1 silence on margin (PR-FD9). Tripwire 6. |
| A3-PR-F16-03 | F16 | R038, R103 | L97-98 | "more than one and a half times the free cash flow from operations compared to whole of FY26" | AMBIGUOUS | No rupee figure, no definition. The base is FY26: CFO/PAT 1.05x and heavy capex [NOTION MEMORY]. H1 CFO includes +Rs 278.8 Cr from trade payables; ex-payables CFO/PAT is 0.78x [NOTION MEMORY]. L97 calls cash generation "equally strong". Ask: FCFO definition, FY26 FCFO in rupees, and the payables and inventory contribution in H1. |
| A3-PR-F16-04 | F16 | none (absence); context R044-R046, R064 | L108 (section L106-151) | "Key Developments:" | FORWARD-SIGNAL | DENSO is dropped. The Q1 release framed the DENSO partnership as upside [NOTION MEMORY, PR-FD7]. The Q2 Key Developments section (L108-151) lists Deming, three products and six orders only. The carve-out has not closed: eDrive was still wholly owned at 30-Sep [NOTION MEMORY]. Rs 16.3bn (45.3%) of Q2 additions are EV 2W traction motors and motor controllers (L128-135) [my arithmetic]. These sit in the carve-out perimeter. Ask: close date, the entity that books these orders, and Sona's post-close economic share. |
| A3-PR-F17-01 | F17 | R119, R030-R032 | L87 | "Q2 FY27 was almost a perfect quarter for us" | CONFIRMATORY-NEGATIVE | Promise C1 (cost pass-through recovery "from Q2") is not addressed in the release. The margin stayed flat at 23.0% (L71, L81). The 26-Oct review scored C1 a miss: mix and input prices [NOTION MEMORY]. The CEO frame contradicts the gate reading. |
| A3-PR-F17-02 | F17 | R035, R043, R073-R075, R067 | L116-118 | "includes a helical limited slip differential for EVs, air springs for passenger coaches and rear radar sensors" | AMBIGUOUS | Promise C2 (first robotics SOP "this quarter") is not evidenced. None of the three Q2 products is a robotics product. Robotics appears only inside the combined order-book share at L83. Ask: did any robotics SOP occur in Q2; if not, the new date. |
| A3-PR-F17-03 | F17 | R029-R039 (CEO comment) | L87-99 | "Cash generation was equally strong." | CONFIRMATORY-NEGATIVE | The release is silent on deteriorating or open items on the checklist: short-term borrowings Rs 234 Cr to Rs 462 Cr; ROCE 16.4% below the 18% leg; Novelic impairment status; EV-only order share. Novelic and ROCE are now silent in two releases in a row (Q1 PR silences [NOTION MEMORY]). |
| A3-PR-F17-04 | F17 | R040-R042, R061-R063, R106 | L110-114 | "awarded the 2026 Deming Prize for Total Quality Management" | AMBIGUOUS | The release leads operations with a quality award. H1 warranty provision was Rs 12.5 Cr against Rs 2.2 Cr, and slow-moving inventory provision was Rs 8.0 Cr against Rs 1.2 Cr [NOTION MEMORY]. Both are silent here. Ask: drivers of the warranty and obsolescence provisions, the division they sit in, and whether they recur. |

---

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Press release has no statement template; ledger zero_standing = 0. |
| F2 Standalone vs consolidated | N.A. | Release carries one unlabelled headline set and no standalone figures. A gap cannot be computed from this document. The labelling issue goes to F14-02. |
| F3 Shell-entity detection | N.A. | No cost lines in the document. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph. |
| F5 Going concern / EoM tracking | N.A. | No EoM paragraph. No prior fulltext for a verbatim diff. |
| F6 Forward-commitment phrases | FINDING | Lexicon hit "commenc" six times (L126, L130, L135, L141, L145, L151) plus the undated 10X ambition (L99). Three findings. "will be" hit only at L192 (disclaimer, "will not be responsible"); no commitment. |
| F7 Hedge phrases | PASS | Only hedge hit is "subject to certain risks and uncertainties" (L189) in the boilerplate disclaimer. The Q1 release carried the same disclaimer [NOTION MEMORY, PR-FD5], so no new hedge. The body carries no hedge. The disclaimer's "conference call" now matches a real 26-Oct call. |
| F8 Tax forensics | N.A. | No tax data in the release. |
| F9 OCI forensics | N.A. | No OCI data. |
| F10 Share count and dilution | N.A. | The release carries no share count, paid-up capital or EPS. |
| F11 Reserves and net worth tie-out | N.A. | The release carries no net worth or reserves figure. |
| F12 Segment forensics | N.A. | No segment assets, liabilities or results. BEV share is a product mix figure; it is covered in F14-06. |
| F13 Board outcome beyond results | N.A. | Reg 30 press-release intimation (L26-34). No AR, AGM, director or fund-raise item. The signature timestamp 17:23:54 IST (L44-45) is recorded; it falls after the board close of 16:05 [NOTION MEMORY]. |
| F14 Drafting inconsistencies | FINDING | Six findings: unlabelled revenue basis on the gate variable; unlabelled S/C basis (repeat); 7 programs claimed vs 6 itemised and Rs 6.8bn unitemised; dangling asterisk on "net order book"; "commercialised" vs later SOP dates; BEV share base dropped. Positive: the Q1 stale dateline is fixed (L62 "October 26, 2026" = L18 and L44). Arithmetic ties: 356/1,547 = 23.0%; 223/1,547 = 14.4%; 658/2,857 = 23.0%; 403/2,857 = 14.1%; Rs 25,100 Cr = Rs 251bn. |
| F15 Entity list diffs | N.A. | No consolidation list in a press release. No prior list. The DENSO/eDrive status is covered under F16-04. |
| F16 Dropped and reframed disclosures | FINDING | EV order-share metric widened to include Robotics & Physical AI; H1 EBITDA YoY omitted and the margin decline unstated; FCFO claim unquantified; DENSO dropped. No prior fulltext; prior-release content comes from the Notion Q1 press-release layer note and is labelled [NOTION MEMORY]. |
| F17 Silence audit | FINDING | Run as a release silence audit against the Notion checklist (there is no transcript in this doctype, and the Q1 run applied F17 to the press release). Table in section 4. Four findings. |

---

## 3. COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Ref | Status word |
|---|---|---|---|---|
| 1 | Additional traction motor volumes, Indian 2W OEM, Rs 12.5bn, under an existing order | H2 FY27 (Oct-2026 to Mar-2027) | L132-135; R046/R088/R109 | initiated (order added; SOP expected) |
| 2 | Integrated motor controllers, EV 2W platform, Indian 2W OEM, Rs 3.8bn | H1 FY28 (Apr-2027 to Sep-2027) | L128-130; R045/R087/R108 | initiated |
| 3 | Differential assemblies for ICE PV, Indian multi-segment OEM, Rs 1.6bn (first ICE PV differential entry) | H2 FY28 (Oct-2027 to Mar-2028) | L137-141; R047/R089/R110/R122 | initiated |
| 4 | Rear radar sensors for 2W, new customer, Rs 1.0bn | H2 FY28 | L149-151; R049/R091/R112 | initiated |
| 5 | Helical limited slip differentials, global EV PV OEM, Rs 7.0bn | H1 FY29 (Apr-2028 to Sep-2028) | L124-126; R044/R086/R107 | initiated |
| 6 | Starter motors for ICE PV, North American OEM, Rs 3.3bn | H1 FY29 | L143-145; R048/R090/R111 | initiated |
| 7 | 10X ambition under Sona Comstar 2.0 | undated in this release (FY35 in Q1 release [NOTION MEMORY]) | L99; R039/R092 | initiated (aspiration) |
| 8 | Three new products commercialised: helical LSD for EVs, railway coach air springs, 2W rear radar | Q2 FY27 | L116-118; R035/R043/R073-R075 | completed (claimed; "commercialised" undefined, see F14-05) |

Status transitions vs Q1: not testable from a prior fulltext. Q1 SOP commitments on file in Notion (four dated SOPs H2 FY26-H2 FY29) are not restated in this release. A4 should check them against the deck.

---

## 4. F17 WHAT WAS NOT DISCUSSED (release silence audit)

Consecutive-quarter counts are release-to-release. The Q1 count comes from the Notion Q1 press-release layer note "Silences worth naming" [NOTION MEMORY].

| Checklist item (Notion 26-Oct Key Notes) | In Q2 release? | Ref | Consecutive release silences | Note |
|---|---|---|---|---|
| Consolidated op EBITDA margin vs gate (bull >=24.5% / bear <23.0%) | Level stated, decline not stated | L71, L81 | 2 (on the step-down) | 23.0% on a revenue basis that appears to include forex (F14-01). YoY decline unstated (F16-02). |
| CFO/PAT >=1.0x | Partial: FCFO multiple only | L97-98 | 1 | No CFO, no PAT ratio, no payables (F16-03). |
| C1 margin recovery from Q2 | Silent | L87-99 | 1 (first scorable quarter) | Release frames the quarter "almost a perfect quarter" (F17-01). |
| C2 first robotics SOP | Silent | L116-118 | 1 | No robotics product among the three commercialised (F17-02). |
| C3 ADAS radar | Partial | L117-118, L149-151 | 0 | 2W rear radar "commercialised"; radar order SOP H2 FY28 (F14-05). |
| DENSO close / eDrive deconsolidation | Silent | L108-151 | 1 (mentioned in Q1 release) | F16-04. |
| Auditor signing time vs board start | Not a release item | n/a | n/a | Belongs to the results filing. Release signature 17:23:54 IST (L44-45). |
| Short-term borrowings | Silent | L87-99 | 1 | Rs 234 Cr to Rs 462 Cr [NOTION MEMORY] (F17-03). |
| EV share of order book (tripwire 9) | Reframed, not silent | L83 | 2 on EV-only (Q1 release silent on 64%) | Combined with Robotics & Physical AI (F16-01). |
| ROCE (<18% leg) | Silent | L87-99 | 2 | F17-03. |
| Novelic impairment (tripwire 3) | Silent | L87-99 | 2 | F17-03. |
| Warranty and slow-moving inventory provisions | Silent | L110-114 | 1 | F17-04. |

---

## 5. ROUTING TO A4

FORWARD-SIGNAL (4): A3-PR-F6-01, A3-PR-F6-02, A3-PR-F16-01, A3-PR-F16-04.
AMBIGUOUS, convert to management questions (8): A3-PR-F6-03, A3-PR-F14-01, A3-PR-F14-03, A3-PR-F14-04, A3-PR-F14-05, A3-PR-F16-03, A3-PR-F17-02, A3-PR-F17-04.
CONFIRMATORY-NEGATIVE (3): A3-PR-F16-02, A3-PR-F17-01, A3-PR-F17-03.
NEUTRAL-FACT (2): A3-PR-F14-02, A3-PR-F14-06.

Every [NOTION MEMORY] number above must be anchored by A4 to the Q2 results filing or deck before it enters the review.

---

```yaml
stage: A3-forensics
company: "SONACOMS"
quarter: "q2fy27"
doctype: "pressrelease"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-sonacoms-q2fy27-c7173c/runs/sonacoms-q2fy27/work/forensics_pressrelease_sonacoms_q2fy27.md"
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
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-PR-F6-01", check: "F6", line: "L132-135", classification: "FORWARD-SIGNAL", implication: "Rs 12.5bn traction-motor upsize (34.7% of Q2 adds) SOP H2 FY27; nearest scorable SOP; sits in EV-motors carve-out perimeter"}
  - {id: "A3-PR-F6-02", check: "F6", line: "L126,L130,L135,L141,L145,L151", classification: "FORWARD-SIGNAL", implication: "Six 'expected' SOPs; 44% of itemised Rs 29.2bn starts H2 FY28 or later; feeds Role 5 tracker and FTTCP catalyst timeline"}
  - {id: "A3-PR-F6-03", check: "F6", line: "L99", classification: "AMBIGUOUS", implication: "10X ambition undated and baseless; Q1 FY35 horizon dropped (Notion memory, unverified)"}
  - {id: "A3-PR-F14-01", check: "F14", line: "L69,L71", classification: "AMBIGUOUS", implication: "Revenue Rs 1,547 Cr appears to include net forex; 23.0% margin sits on the gate bear line; basis ruling pending"}
  - {id: "A3-PR-F14-02", check: "F14", line: "L32-33,L69-83", classification: "NEUTRAL-FACT", implication: "Headline set unlabelled S/C for second release running; PAT matches consolidated owners"}
  - {id: "A3-PR-F14-03", check: "F14", line: "L74-76,L60,L124-151", classification: "AMBIGUOUS", implication: "7 programs claimed, 6 itemised; Rs 6.8bn (18.9%) of Rs 36bn additions unitemised; largest win is an upsize"}
  - {id: "A3-PR-F14-04", check: "F14", line: "L83", classification: "AMBIGUOUS", implication: "Asterisk on net order book has no footnote; 'net' undefined; haircut method still undisclosed"}
  - {id: "A3-PR-F14-05", check: "F14", line: "L116-118,L149-151,L126", classification: "AMBIGUOUS", implication: "'Commercialised' radar and LSD vs order SOPs H2 FY28/H1 FY29; C3 scoring depends on the definition"}
  - {id: "A3-PR-F14-06", check: "F14", line: "L59,L70", classification: "NEUTRAL-FACT", implication: "BEV 51% is of automotive revenue; L70 drops the base; share of total revenue unstated"}
  - {id: "A3-PR-F16-01", check: "F16", line: "L83", classification: "FORWARD-SIGNAL", implication: "EV order share restated as EV plus Robotics 65%; EV-only 61% (deck, Notion memory), third easing, tripwire 9"}
  - {id: "A3-PR-F16-02", check: "F16", line: "L71,L80-82,L58", classification: "CONFIRMATORY-NEGATIVE", implication: "H1 EBITDA YoY omitted; Q2 implies ~220 bps YoY margin compression unstated; tripwire 6; second release silent"}
  - {id: "A3-PR-F16-03", check: "F16", line: "L97-98", classification: "AMBIGUOUS", implication: "FCFO 1.5x FY26 claim unquantified; H1 CFO carried by +Rs 278.8 Cr payables (Notion memory)"}
  - {id: "A3-PR-F16-04", check: "F16", line: "L108", classification: "FORWARD-SIGNAL", implication: "DENSO dropped from release while unclosed; 45.3% of Q2 adds are EV 2W motors/controllers in carve-out perimeter"}
  - {id: "A3-PR-F17-01", check: "F17", line: "L87", classification: "CONFIRMATORY-NEGATIVE", implication: "C1 margin recovery unaddressed; 'almost a perfect quarter' against a flat 23.0% margin"}
  - {id: "A3-PR-F17-02", check: "F17", line: "L116-118", classification: "AMBIGUOUS", implication: "C2 first robotics SOP not evidenced; no robotics product among Q2 commercialisations"}
  - {id: "A3-PR-F17-03", check: "F17", line: "L87-99", classification: "CONFIRMATORY-NEGATIVE", implication: "Silent on ST borrowings doubling, ROCE <18%, Novelic (2 releases), EV-only share"}
  - {id: "A3-PR-F17-04", check: "F17", line: "L110-114", classification: "AMBIGUOUS", implication: "Deming headline vs warranty Rs 12.5 Cr (from 2.2) and obsolescence Rs 8.0 Cr (from 1.2) provisions, silent"}
forward_signals: ["A3-PR-F6-01", "A3-PR-F6-02", "A3-PR-F16-01", "A3-PR-F16-04"]
ambiguous: ["A3-PR-F6-03", "A3-PR-F14-01", "A3-PR-F14-03", "A3-PR-F14-04", "A3-PR-F14-05", "A3-PR-F16-03", "A3-PR-F17-02", "A3-PR-F17-04"]
commitments:
  - {commitment: "Additional traction motor volumes, Indian 2W OEM, Rs 12.5bn", implied_date: "H2 FY27", ref: "L132-135", status_word: "initiated"}
  - {commitment: "Integrated motor controllers EV 2W, Rs 3.8bn", implied_date: "H1 FY28", ref: "L128-130", status_word: "initiated"}
  - {commitment: "ICE PV differential assemblies, Rs 1.6bn", implied_date: "H2 FY28", ref: "L137-141", status_word: "initiated"}
  - {commitment: "2W rear radar sensors, new customer, Rs 1.0bn", implied_date: "H2 FY28", ref: "L149-151", status_word: "initiated"}
  - {commitment: "Helical LSD, global EV OEM, Rs 7.0bn", implied_date: "H1 FY29", ref: "L124-126", status_word: "initiated"}
  - {commitment: "Starter motors, North American OEM, Rs 3.3bn", implied_date: "H1 FY29", ref: "L143-145", status_word: "initiated"}
  - {commitment: "10X ambition under Sona Comstar 2.0", implied_date: "undated (FY35 in Q1 release, Notion memory)", ref: "L99", status_word: "initiated"}
  - {commitment: "Three new products commercialised (helical LSD, railway air springs, 2W rear radar)", implied_date: "Q2 FY27", ref: "L116-118", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The release is a marketing wrapper. Its forensic value lies in what it reframes or leaves out, and three items bear on the binding Q2 gate. (1) Release revenue Rs 1,547 Cr appears to include net forex (Notion: rev ops Rs 1,535.8 Cr plus forex Rs 10.6 Cr). The 23.0% margin therefore uses the deck basis, the basis the operator has not yet ruled on. Ex-forex, the margin fails the bear line. (2) The EV order-book share is restated as 'EV and Robotics & Physical AI' at 65%. That reads as up from Q1's 64%, while EV-only fell to 61% (deck, per Notion). This is a numerator change on tripwire 9. (3) H1 EBITDA is the only headline without a YoY figure. Q2 implies about 220 bps YoY margin compression, unstated for a second release. DENSO was framed as upside in Q1 and is now absent, yet 45% of Q2 additions sit in the EV 2W motor perimeter being carved out. All cross-document numbers come from the Notion page (operator memory). A4 must anchor them to the filing or deck. A1 line cites on entity rows R053-R085 are block placeholders; all content was found verbatim."
```
