# FORENSICS presentation NETWEB q2fy27 (A3)

Document: Netweb_Q2FY27_Investor_Presentation.pdf (22 slides, "Earnings Update October 2026", cover letter dated 24.10.2026)
Inputs read: A1 structured (R001-R423, all rows), A1 fulltext (lines 1-849, including the raw reading-order supplement at 563+), A2 ledger (423 IDs), Notion checklist excerpt (memory, not evidence).
Source PDF and inputs/ not opened. Prior-quarter fulltext: not available (first NETWEB pipeline run).
Units: Rs Mn unless stated. "Line" = fulltext line number. "Supp" = supplement line (same source, raw order).

---

## 0. LEDGER RECONCILIATION

Rows in ledger: 423. Rows read at cited line: 423. Reconciled: 100%.

| Ledger block | IDs | Read and tied | Notes |
|---|---|---|---|
| Slide numbers p1-p7 | R001-R068 | yes | p5/p6/p7 headline figures tie to p11 P&L. p7 mapping checked against supp 631-637. |
| Offering revenue p10 | R069-R101 | yes, one mapping query | H1 FY27 offerings sum to 21,430 (= revenue). FY26 sum 21,837 (= 21,836). CAGRs 42.2/39.8/244.4% recompute. See MAPPING QUERY M1. |
| P&L p11 | R102-R191 | yes | Supp 802-813 used. Q1+Q2 ties for revenue, finance cost, depreciation, PBT, PAT. Other income and Op EBITDA do NOT tie (finding A3-15). |
| Balance sheet p12 | R192-R236 | yes | Supp 816-848 used. Net worth, Net Debt, ROE, ROCE, ND/E, ND/EBITDA all recompute. |
| Customers p13 | R237-R257 | yes | 171+147+131+49 = 498 (R257). Top-10 >= Top-5 in every period. |
| Funnel p15 | R258-R260 | yes | |
| Shareholding p17 | R261-R269 | yes | Total 64.16+9.47+6.68+1.35+18.34 = 100.00. Non-promoter split recomputes (9.47/35.84 = 26.42%). |
| CCC p20 | R271-R282 | yes | A+B-C ties all three periods. |
| QIP p21 | R283-R294 | yes | 7,667.45+2,037.56 = 9,705.01; 0.00+1,995.02 = 1,995.02; 76.79+223.18 = 299.97; columns total 12,000.00 / 7,744.24 / 4,255.76. Unique arithmetic fit; GCP 16.6% is inside the 25% ICDR cap. |
| Notes p22 | R295-R296, R405-R418 | yes | Definitions used for every ratio recompute. |
| Entities | R298-R320 | yes | |
| Forward | R321-R342 | yes | |
| Dates | R343-R362 | yes | |
| Qualifiers | R363-R404, R419-R423 | yes | |

A2 queries resolved:
- R040 vs R041 (QUERY_A1): one sentence, not a conflict. Supp 591-593: "03 Supercomputers listed 17 times in the world's top 500 supercomputers". Three systems, 17 cumulative listings across TOP500 editions. No finding.
- R388 (FOOTNOTE_UNRESOLVED): resolved. Two footnote strings overlap on p13. Supp 714: "Note: *CAGR FY20 -FY24, ^As a % of revenue from operations excludes other operating revenue". Supp 716: "* % of revenue from operations excludes other operating revenue; #Compounded annual growth in the number of customers from FY2020 to H1FY27". One is a stale note (finding A3-13).
- R393 (FOOTNOTE_UNRESOLVED): confirmed unresolvable. Supp 703-713 carries segment labels only (Government & Defense, Academia and Research, Large Enterprises, New Age Financial Services), no shares. Carried as a question in A3-18.
- R290 (ZERO_STANDING): F1, finding A3-01.
- R416 (183-day basis): F11 and F14, findings A3-10 and A3-12.

MAPPING QUERY M1 (for A4 / verifier, not a document finding): R084-R091 and R100-R101 may have HPS and Data Centre servers swapped. Evidence: (a) layout line 288 puts "339 275 328" in the left chart whose label "High-Performance Storage" sits at lines 292-294, and "337 373 321 285" in the middle chart under "Data Centre servers" (line 291); (b) supp 646-650 groups "339 275 328 204" as one series; (c) the pie raw order (supp 684-694) pairs 17.4 HPC, 17.7 Private cloud, 59.9 AI (all three correct), then 1.0 HPS, 1.3 Data centre server. 204/21,430 = 0.95% and 285/21,430 = 1.33%. Probable reading: HPS = 339/275/328/204 (1.0%), DC servers = 337/373/321/285 (1.3%). A1 has the reverse. Totals unchanged; each line about 1% of revenue; immaterial to the thesis. A3 does not override A1.

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R290 (R289, R291, R292-R294) | p21, line 518, 520 | "1,995.02       0.00                1,995.02" | AMBIGUOUS | General corporate purposes 1,995.02 Mn (16.6% of 12,000) is unspent, discretionary cash with no named use. The line exists because ICDR lets up to 25% of gross proceeds go to GCP; it anticipates capex, acquisitions, subsidiary funding or debt repayment. Issue expenses are 25.6% paid (76.79 of 299.97, line 520); an unspent balance of 223.18 Mn usually rolls into GCP. A4: planned use and date of the GCP bucket, and whether any of it funds the subsidiary the disclaimer names (line 77). |
| A3-02 | F6 | R022/R260, R023/R259, R321 | p5, lines 142-143; p15, line 425 | "providing strong revenue visibility for the coming quarters" | FORWARD-SIGNAL | Order book 26,290 Mn = 1.99x Q2 revenue (13,233); with L1 6,525 Mn, 2.48x. Visibility covers about two quarters at the Q2 run-rate. Q4 FY27 needs Q3 conversion of L1 and pipeline. Opening order book is not in the deck, so H1 order inflow and book-to-bill are NOT FOUND. |
| A3-03 | F6 | R329, R284-R288 | p21, lines 511-522 | "Amount Un-Utilized as on 30.09.2026" | FORWARD-SIGNAL | 64.5% of the raise (7,744.24 of 12,000) and 79.0% of the working-capital tranche (7,667.45 of 9,705.01) were spent by 30-Sep, inside the quarter of issue. The remaining WC tranche of 2,037.56 Mn is the H2 buffer before new debt. Deployment schedule NOT FOUND in deck. |
| A3-04 | F6 | R340 | p14, line 397 | "Commenced R&D of quantum simulators and emulators" | FORWARD-SIGNAL | Status word "Commenced" opens a new R&D line. Spend, capitalise-vs-expense treatment and revenue date are NOT FOUND. Track initiated, then underway, then completed in later decks. |
| A3-05 | F7 | R401, R403 | p20, lines 506-507 | "The impact is not material" | AMBIGUOUS | Unquantified assurance on an inventory valuation change (FIFO to moving weighted average cost) that restates FY25. It sits on the slide where inventory days go 53 to 86 to 117 (line 501). Under WAC, falling input costs across GPU generations reach COGS more slowly than under FIFO. A4: Rs impact on FY25 inventory, COGS and PAT; effective date; does Q2 FY27 run on WAC. |
| A3-06 | F10 | R183-R191, R377-R378, R192-R194 | p11, supp 812-813 (layout 311, 316) | "Diluted EPS* ()" ... "*Annualized" | NEUTRAL-FACT | The asterisk mislabels quarterly EPS. Q1 14.98 + Q2 23.54 = 38.52, about the H1 38.60, so the quarter figures are NOT annualised. Share capital 114 to 119 Mn (+4.4%) traces to the QIP (line 144; p21). Q2 PAT +60.2% QoQ vs EPS +57.1%, so about 2% weighted dilution sits in Q2; the remaining about 2.4% lands in Q3 EPS. Basic EPS is not shown, so the basic-diluted spread is NOT testable. |
| A3-07 | F11 | R202-R203, R208-R212, R285 | p12, supp 820-823; p5, line 163 | "a strengthened balance sheet following the recent capital raise" | FORWARD-SIGNAL | Net cash fell from 1,244 to 136 Mn in H1 (free cash 4,066 to 3,464; borrowings 2,717 to 3,213) despite a 12,000 Mn raise and 2,220 Mn H1 PAT. Working capital absorbed the raise in one quarter. H2 working capital falls on the 2,037.56 Mn WC balance and on debt. |
| A3-08 | F11 | R209, R285, R218, R408, R411 | p12, supp 822; p21, line 522 | "Free Cash4 1,701 4,066 3,464" | AMBIGUOUS | Free cash (3,464) sits 792 Mn below unutilised QIP proceeds (4,255.76). Part of the unspent money is outside Free Cash: current investments inside Net Current Assets (note 7, line 539), lien-marked deposits excluded by note 4 (line 533), or used temporarily. The Net Debt (0.02x) headline depends on which. A4: where the 4,255.76 Mn sits on 30-Sep. |
| A3-09 | F11 | R138-R146, R201-R203, R271-R273 | p11, supp 807; p12, supp 820; p20, line 500 | "Finance Cost 238 9 2459.1% 115 106.5% 353 19 1751.4% 130" | AMBIGUOUS | Q2 finance cost 238 Mn on average borrowings of 2,965 Mn is about 32% annualised. FY26 was about 9.5% (130 on an average of 1,365). H1 finance cost (353) is 2.7x the FY26 full year. Receivable days fell 86 to 62 in the same half. Candidates: intra-quarter debt peak above period-end, bill discounting or factoring, LC/acceptance charges on imports carried in payables. Each sits outside "Borrowings" (note 5), so Net Debt would understate financing. Lean bear. A4: peak intra-quarter debt, discounting with or without recourse, acceptances in trade payables. |
| A3-10 | F11 | R216-R218, R222-R224, R280-R282, R415-R417 | p12, supp 825, 828; p20, line 503 | "Net Current Assets7 3,024 5,397 20,268" | FORWARD-SIGNAL | NCA rose 3.76x (5,397 to 20,268) while CCC moved only 84 to 94 days. NCA in revenue days: about 97 (Mar-25, on p10 offering sum 11,432 as the FY25 revenue proxy), 90 (Mar-26), 173 (Sep-26 on H1 x2) or 140 (on Q2 x4). Even with all 4,255.76 Mn of unspent QIP removed, Sep-26 is 110-136 days. Notes 11-13 average opening and closing balances, which halves a closing-balance step-up. The 94-day CCC understates working-capital intensity at 30-Sep. A4: closing-balance inventory, receivable and payable days at 30-Sep-26. |
| A3-11 | F11 | R194-R200, R231-R236, R413-R414, R418 | p12, supp 841-846; p22, lines 545-550 | "annualized PAT for September'26 divided by average of September'26 & March'26 `Total Equity'" | FORWARD-SIGNAL | ROE 31.4% averages opening equity of 7,233 with closing equity of 21,041. On closing equity, annualised H1 PAT (4,440) gives 21.1%. FY27 ROE and ROCE step down as the QIP equity enters full-period averages. This is mechanical, not operating; A4 must not read it as decay. |
| A3-12 | F14 | R412, R415-R418 | p22, lines 541-562 | "Revenue from operations' for September'26 quarter as multiplied by 183 days" | AMBIGUOUS | Notes 11-13 pair one quarter's revenue with a half-year day count. Note 8 (line 541) says Sep-26 GFAT uses "annualized `Revenue from operations' for the quarter", but note 14 (line 561) says H1 x2. Either the label or the arithmetic is wrong. Read literally, Sep-26 days are about 2x a true quarterly basis, which would make the 117 inventory days not comparable with the 86 for Mar-26. A4: which revenue base (Q2 or H1) sits under Sep-26 days and GFAT. |
| A3-13 | F14 | R386-R392 (R388), R306, R283-R294, R364 | p13, supp 714-716; p6, supp 596, 619; p10, supp 681; p17, supp 795, 798; p21, line 517 | "Note: *CAGR FY20 -FY24, ^As a % of revenue from operations excludes other operating revenue" | NEUTRAL-FACT | On p13, "*" and "^" each carry two definitions; one footnote is stale from an earlier template. Leftover "To be" placeholder text sits under p6 and p10 headers (it garbles layout lines 173, 188, 271). "Helios MF" appears twice in the shareholder list. "Total Net Proceeds" labels a 12,000.00 total that includes 299.97 Mn of issue expenses; true net proceeds are 11,700.03. Add the EPS label in A3-06. Each item is immaterial alone; together they are a deck-control data point. |
| A3-14 | F14 | R310, R363 | p3, line 77; p1, line 35 | "OR ITS SUBSIDIARY (TOGETHER" | NEUTRAL-FACT | The deck never states whether its figures are consolidated or standalone, although a subsidiary exists. A4: tie the deck to the consolidated results filing before using any deck number as anchored. |
| A3-15 | F16 | R111, R114, R116, R125, R127, R129, R132, R134, R059, R066 | p11, supp 804-806; p7, supp 635-637 | "Operating EBITDA Margin1 (%) 14.9% 15.0% (6 bps) 14.7% 21 bps 15.1% 14.9% 14 bps 13.0%" | AMBIGUOUS | The H1 column does not sum. Other income: H1 161 vs Q1 85 + Q2 129 = 214. Op EBITDA: H1 3,230 vs 1,205 + 1,973 = 3,178 (+52 Mn). The H1 margin of 15.1% sits above both quarters (14.7%, 14.9%), which a sum of two quarters cannot do. On 3,178 the H1 margin is 14.8%, and "+14 bps" YoY becomes about -10 bps. Revenue, PBT, finance cost, depreciation and PAT all tie, so the gap is in other income (a regrouping into operating lines, or an error). The figure also feeds Net Debt/Op EBITDA via note 14. Lean bear: the headline H1 margin is overstated by about 24 bps. A4: which column is right, and was about 53 Mn regrouped from other income in H1. |
| A3-16 | F16 | R237-R240, R244-R252, R254 | p13, supp 728-741 | "reflecting limited customer concentration" | FORWARD-SIGNAL | The caption sits over Top-5 50.3 / 50.8 / 62.2 / 76.5% and Top-10 64.5 / 65.8 / 76.4 / 85.2% (FY24 to H1 FY27). New customers onboarded fell 171 / 147 / 131 / 49 (H1). Repeat-customer revenue is 94.4%. Revenue now rides on a few accounts; quarterly lumpiness risk rises. Checklist #6 red threshold (Top-10 above 70%) is crossed on the headline. The ex-strategic split is NOT FOUND. The caption contradicts the slide's own numbers. |
| A3-17 | F16 | R017-R021, R082, R092-R095, R099, R301 | p5, lines 140-142; p10, supp 698 | "highlighting the strength of our diversified growth portfolio" | FORWARD-SIGNAL | AI Systems is 58.4% of Q2 and 59.9% of H1 revenue. Software, services and spares fell from 6.9% (FY24) and 8.8% (FY25) to 5.6% (FY26) and 2.65% (H1 FY27). H1 568 x2 = 1,136 Mn, below FY26 1,232 Mn in absolute terms. The mix is moving to hardware. Checklist #5 is on the red side (below the 4% flat threshold). |
| A3-18 | F16 | R258-R260, R393-R398 | p15, lines 436-445; p13, line 350 | "pending execution/ billing as on the reporting date" | AMBIGUOUS | The order book definition states no GST basis. "execution/ billing" lets delivered-but-unbilled orders stay in the book. The pipeline (111,518 Mn, 2.1x annualised Q2 revenue) has no conversion history. The customer-segment pie (R393) has no extractable shares. Without a prior deck, definition drift across quarters is NOT testable this run. A4: GST basis, unbilled-delivered treatment, H1 order inflow, segment split. |
| A3-19 | F17 | checklist #1, #3, #8, #9; thesis-broken #4; Notion markers | p4, line 128; p11-p12, p20-p21 | "Financial Summary" | AMBIGUOUS | The financial section (P&L, balance sheet, CCC, QIP) has no cash-flow statement and no CFO figure, although this half is the master cash gate (checklist #1). There is no strategic/Blackwell order split (#3, #9), nothing on inventory-control remediation (#8), no Rubin mention (thesis-broken #4), and no subsidiary detail. Silence count: 1 deck known. The consecutive-quarter count is NOT FOUND (no prior run). Lean bear while the deck frames the balance sheet as "strengthened". |

---

## 2. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | One ZERO_STANDING row (R290, GCP utilised 0.00). A3-01. |
| F2 Standalone vs consolidated | N.A. | The deck carries one unlabelled set of figures, with no S-vs-C split (label gap in A3-14). |
| F3 Shell-entity detection | N.A. | No entity-level cost lines in deck. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph. The cover letter calls the results "unaudited" (line 35). |
| F5 Going concern / EoM tracking | N.A. | No EoM paragraph in the deck; no prior extract to diff. |
| F6 Forward-commitment mining | FINDING | One lexicon hit outside boilerplate ("Commenced", line 397), plus dateable QIP and order-book commitments. Disclaimer hits (lines 84, 91, 100-104, 116, 120) are boilerplate and excluded. A3-02, A3-03, A3-04; register below. |
| F7 Hedge mining | FINDING | Disclaimer hedges (lines 87, 90, 97, 111, 115) are standard safe-harbour text. The one substantive hedge is "The impact is not material" (line 507). A3-05. |
| F8 Tax forensics | PASS | Limited scope: implied ETR from PBT/PAT is Q2 FY27 25.1%, Q1 25.2%, H1 25.2%, Q2 FY26 25.2%, H1 FY26 26.0%, FY26 25.6%, all near 25.17%. Deferred tax and earlier-years tax are not in the deck; test them at the results filing. |
| F9 OCI forensics | N.A. | No OCI line in the deck. |
| F10 Share count and dilution | FINDING | Paid-up 114 to 119 Mn traces to the QIP. EPS asterisk mislabelled; Q3 carries the remaining dilution. A3-06. |
| F11 Reserves / net worth tie-out | FINDING | Tie-out passes: 119 + 20,923 = 21,042 vs 21,041 (rounding). The H1 bridge of +13,808 vs PAT 2,220 + QIP 11,700-11,923 leaves a 112-335 Mn gap (0.5-1.6%, under 5%; candidates are the FY26 dividend (NOT FOUND), issue-expense charge, OCI, ESOP). Balance-sheet findings A3-07 to A3-11. |
| F12 Segment forensics | N.A. | The deck gives offering revenue only; no segment assets or liabilities. Offering-mix observations sit in A3-17. |
| F13 Board outcome beyond results | N.A. | The presentation is not a board outcome; no AGM, director or enabling-resolution content. |
| F14 Drafting inconsistencies | FINDING | Conflicting ratio-basis notes, stale footnotes, placeholders, duplicate holder, net-proceeds label, unlabelled consolidation basis. A3-12, A3-13, A3-14 (and the A3-06 EPS label). |
| F15 Entity list diffs | N.A. | No consolidation list in the deck. The disclaimer names one unnamed subsidiary (line 77). No prior list. |
| F16 Dropped / reframed disclosures | FINDING | Cross-deck diff is untestable (no prior deck). In-deck framing contradicts the deck's own numbers on the H1 margin, concentration and diversification; definitions are ambiguous. A3-15 to A3-18. |
| F17 Silence audit | FINDING | Run against the deck as management's chosen disclosure, using the Notion checklist. Cash flow, strategic orders, inventory controls, Rubin and the subsidiary are absent. A3-19; table below. |

GATE A3: all 17 marked; no blanks.

---

## 3. COMMITMENT REGISTER (F6)

| Commitment | Implied date | Note / slide ref | Status word |
|---|---|---|---|
| Execute order book 26,290 Mn plus L1 6,525 Mn; "strong revenue visibility for the coming quarters" | Q3-Q4 FY27 (about 2 quarters at the Q2 run-rate) | p5 lines 142-143; p15 lines 420-425 | underway |
| Deploy unutilised QIP proceeds 4,255.76 Mn (WC 2,037.56; GCP 1,995.02; issue expenses 223.18) | NOT FOUND in deck | p21 lines 511-522 | underway (7,744.24 of 12,000 used) |
| R&D of quantum simulators and emulators | undated | p14 line 397 | initiated ("Commenced") |
| Physical AI R&D across hardware, agentic and interface layers; defence and strategic manufacturing priority | undated | p14 lines 397-405 (R337-R339) | none (intention) |
| HPC: align with NSM 2.0 "build & design in India"; expand to enterprises | undated | p14 lines 397-404 (R330-R332) | none (intention) |
| Private cloud: Tyrone Skylus; push into Tier-II and DC parks backed by 22 offices | undated | p14 lines 396-407 (R333-R334) | none (intention) |
| AI Systems: pre-curated sovereign AI appliances for enterprise and central/state programmes | undated | p14 lines 403-407 (R336) | none (intention) |

---

## 4. F17 "WHAT WAS NOT DISCUSSED" (deck vs Notion checklist; memory, not evidence)

| Checklist / marker | Deck status | Consecutive quarters silent |
|---|---|---|
| #1 CFO/PAT (master cash gate) | Absent. No cash-flow slide in 22. | 1 known; prior NOT FOUND |
| #3 Blackwell order execution (Rs 1,734 Cr by H2 FY27) | Absent. Order book total only. | 1 known; prior NOT FOUND |
| #8 Inventory audit remediation | Absent. Only the FIFO-to-WAC note (line 506). | 1 known; prior NOT FOUND |
| #9 New strategic AI orders >= Rs 500 Cr | Not itemised. | 1 known; prior NOT FOUND |
| #6 Concentration ex-strategic order | Headline only (Top-10 85.2%). | 1 known; prior NOT FOUND |
| Thesis-broken #4 Rubin inclusion | Not named. The deck says "OEM partnership with NVIDIA" (line 181) and "chip-agnostic" (line 163). | 1 known; prior NOT FOUND |
| Notion marker: overseas WOS | Absent. Disclaimer says "its Subsidiary" (line 77). | 1 known; prior NOT FOUND |
| Notion marker: finance cost | Number shown (238), no commentary. | 1 known; prior NOT FOUND |
| Notion marker: strategic vs core revenue split | Absent. | 1 known; prior NOT FOUND |

Addressed in deck: #2 CCC 94 days (green band on headline; see A3-10); #4 Op EBITDA margin 14.9% (green); #5 software share 2.65% (red side, A3-17); #6 Top-10 85.2% (red on headline, A3-16); #7 promoter 64.16% (supp 764). With memory Mar-26 66.98% and deck paid-up 114 to 119: 66.98 x 114 = 76.36 vs 64.16 x 119 = 76.35, so promoter shares are unchanged and the drop is QIP dilution. #10 Chandelier is not a deck item.

---

```yaml
stage: A3-forensics
company: "NETWEB"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-netweb-q2fy27-a60c5c/runs/netweb-q2fy27/work/forensics_presentation_netweb_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F1", line: "p21 L518,L520 (R290)", classification: "AMBIGUOUS", implication: "GCP 1,995.02 Mn (16.6% of raise) unspent with no named use; issue-expense balance 223.18 Mn likely rolls into GCP. Ask use and timing, incl. subsidiary funding."}
  - {id: "A3-02", check: "F6", line: "p5 L142-143; p15 L425", classification: "FORWARD-SIGNAL", implication: "Order book 26,290 = 1.99x Q2 revenue (2.48x with L1); about two quarters of cover; Q4 FY27 needs Q3 conversion. H1 inflow NOT FOUND."}
  - {id: "A3-03", check: "F6", line: "p21 L511-522", classification: "FORWARD-SIGNAL", implication: "64.5% of QIP and 79% of WC tranche spent within the issue quarter; 2,037.56 Mn WC left for H2 before new debt."}
  - {id: "A3-04", check: "F6", line: "p14 L397", classification: "FORWARD-SIGNAL", implication: "'Commenced' quantum simulator R&D; spend and accounting NOT FOUND; track status next quarter."}
  - {id: "A3-05", check: "F7", line: "p20 L506-507", classification: "AMBIGUOUS", implication: "FIFO to WAC inventory policy change restating FY25 called 'not material' without a number while inventory days hit 117. Ask Rs impact and effective date."}
  - {id: "A3-06", check: "F10", line: "p11 supp L812-813", classification: "NEUTRAL-FACT", implication: "EPS '*Annualized' label wrong (quarters sum to H1). Paid-up +4.4% from QIP; about 2% weighted in Q2, about 2.4% more lands in Q3 EPS. Basic EPS absent."}
  - {id: "A3-07", check: "F11", line: "p12 supp L820-823; p5 L163", classification: "FORWARD-SIGNAL", implication: "Net cash 1,244 to 136 Mn despite 12,000 Mn raise; 'strengthened balance sheet' contradicted; H2 WC leans on remaining tranche and debt."}
  - {id: "A3-08", check: "F11", line: "p12 supp L822; p21 L522", classification: "AMBIGUOUS", implication: "Free cash 3,464 is 792 Mn below unutilised QIP 4,255.76; part parked outside Free Cash or used. Ask where proceeds sit."}
  - {id: "A3-09", check: "F11", line: "p11 supp L807; p12 supp L820; p20 L500", classification: "AMBIGUOUS", implication: "Finance cost implies about 32% on reported debt (FY26 about 9.5%); receivable days 86 to 62. Possible discounting, acceptances or intra-quarter peak debt outside Net Debt. Lean bear."}
  - {id: "A3-10", check: "F11", line: "p12 supp L825,L828; p20 L503", classification: "FORWARD-SIGNAL", implication: "NCA 3.76x (5,397 to 20,268) vs CCC 84 to 94; NCA days about 90 to 140-173 (110-136 ex all unspent QIP). Averaged-balance CCC understates 30-Sep WC intensity."}
  - {id: "A3-11", check: "F11", line: "p12 supp L841-846; p22 L545-550", classification: "FORWARD-SIGNAL", implication: "ROE 31.4% on averaged equity; 21.1% on closing equity. FY27 ROE/ROCE fall mechanically as QIP equity enters averages; not operating decay."}
  - {id: "A3-12", check: "F14", line: "p22 L541-562", classification: "AMBIGUOUS", implication: "Notes 11-13 pair quarter revenue with 183 days; notes 8 and 14 conflict on GFAT base. Sep-26 days comparability unproven. Ask revenue base."}
  - {id: "A3-13", check: "F14", line: "p13 supp L714-716; supp L596,L619,L681; supp L795,L798; p21 L517", classification: "NEUTRAL-FACT", implication: "Stale duplicate footnotes, 'To be' placeholders, duplicate Helios MF, 'Total Net Proceeds' on a gross total. Cumulative deck-control data point."}
  - {id: "A3-14", check: "F14", line: "p3 L77; p1 L35", classification: "NEUTRAL-FACT", implication: "Deck never states consolidated or standalone basis though a subsidiary exists; tie to results filing before anchoring."}
  - {id: "A3-15", check: "F16", line: "p11 supp L804-806; p7 supp L635-637", classification: "AMBIGUOUS", implication: "H1 other income 161 vs 85+129=214; H1 Op EBITDA 3,230 vs 3,178; 15.1% H1 margin exceeds both quarters. Corrected 14.8%, H1 YoY flips +14 to about -10 bps. Ask which is right."}
  - {id: "A3-16", check: "F16", line: "p13 supp L728-741", classification: "FORWARD-SIGNAL", implication: "'limited customer concentration' over Top-5 76.5% / Top-10 85.2%, rising three periods; new customers 171 to 49 (H1). Checklist #6 red on headline."}
  - {id: "A3-17", check: "F16", line: "p5 L140-142; p10 supp L698", classification: "FORWARD-SIGNAL", implication: "'diversified' while AI is 59.9% of H1; software/services 8.8% (FY25) to 2.65% (H1), falling in absolute terms. Checklist #5 red side."}
  - {id: "A3-18", check: "F16", line: "p15 L436-445; p13 L350", classification: "AMBIGUOUS", implication: "Order book definition silent on GST and lets delivered-unbilled stay in book; pipeline has no conversion history; segment pie shares absent. Ask all four."}
  - {id: "A3-19", check: "F17", line: "p4 L128; p11-p12, p20-p21", classification: "AMBIGUOUS", implication: "No cash-flow slide in the master cash-gate half; silent on strategic orders, inventory controls, Rubin, subsidiary. Count 1 known; prior NOT FOUND. Lean bear."}
forward_signals: ["A3-02", "A3-03", "A3-04", "A3-07", "A3-10", "A3-11", "A3-16", "A3-17"]
ambiguous: ["A3-01", "A3-05", "A3-08", "A3-09", "A3-12", "A3-15", "A3-18", "A3-19"]
commitments:
  - {commitment: "Execute order book 26,290 Mn plus L1 6,525 Mn; strong revenue visibility for the coming quarters", implied_date: "Q3-Q4 FY27", ref: "p5 L142-143; p15 L420-425", status_word: "underway"}
  - {commitment: "Deploy unutilised QIP 4,255.76 Mn (WC 2,037.56; GCP 1,995.02; issue exp 223.18)", implied_date: "NOT FOUND", ref: "p21 L511-522", status_word: "underway"}
  - {commitment: "R&D of quantum simulators and emulators", implied_date: "undated", ref: "p14 L397", status_word: "initiated"}
  - {commitment: "Physical AI R&D; defence and strategic manufacturing priority", implied_date: "undated", ref: "p14 L397-405", status_word: "none (intention)"}
  - {commitment: "HPC NSM 2.0 alignment; expand to enterprises", implied_date: "undated", ref: "p14 L397-404", status_word: "none (intention)"}
  - {commitment: "Private cloud Tyrone Skylus; Tier-II and DC parks push", implied_date: "undated", ref: "p14 L396-407", status_word: "none (intention)"}
  - {commitment: "Sovereign AI appliances for enterprise and state programmes", implied_date: "undated", ref: "p14 L403-407", status_word: "none (intention)"}
gate_a3: pass
blank_checks: []
analyst_note: "Three findings carry weight. First, the H1 column does not sum: other income 161 vs 85+129=214, so H1 Op EBITDA 3,230 sits 52 Mn above the quarters, and a 15.1% H1 margin above both 14.7% and 14.9% cannot come from a sum. The H1 YoY margin claim flips to about -10 bps. Second, the 12,000 Mn raise did not strengthen the balance sheet. Net cash fell to 136 Mn and NCA nearly quadrupled, but the 94-day CCC hides it because it averages opening and closing balances. Free cash also sits 792 Mn below unspent proceeds. Third, finance cost implies about 32% on reported debt while receivable days fell, which fits discounting or acceptances outside Borrowings. Memory cross-check only: Notion inventory Rs 805 to 1,931 Cr fits 117 days on H1 revenue, so notes 11-13 likely mislabel the base. Mapping query M1: A1 probably swapped the HPS and DC-server series (R084-R091, R100-R101); totals are unchanged and it is immaterial. R040/R041 are one claim. With no prior deck, cross-quarter diffs are untestable."
```
