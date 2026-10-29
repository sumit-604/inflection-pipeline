# FORENSICS: presentation (Reg 30 PRESS RELEASE, routed as management narrative; 1 PDF page = 1 slide) | IndiaMART InterMESH Limited (INDIAMART) | q2fy27 | A3 forensic notes (claude-opus-5-5)

Inputs read: extracted/indiamart-pressrelease-q2fy27-structured.md (R001-R140, all rows); extracted/indiamart-pressrelease-q2fy27-fulltext.md (L1-L195, every line); work/ledger_pressrelease_indiamart_q2fy27.md (all sections); work/notion_snapshot_2026-10-28.md L1350-1379 (Q1 FY27 press-release and concall findings, labelled NOTION MEMORY, not filed evidence); work/notion_monitoring_checklist.md. Filed values for the cross-document tie come from work/forensics_results_indiamart_q2fy27.md (labelled RESULTS-A3, INR million, divide by 10 for Rs Cr) and work/forensics_presentation_indiamart_q2fy27.md (labelled DECK-A3). No prior-quarter press-release fulltext exists, so no verbatim Q1-vs-Q2 diff was possible. The source PDF and inputs/ were not opened.

Line numbers are press-release fulltext lines. Page 4 table values follow A1's render-verified header note (L16), which governs the displaced text layer at L150-L153. "Derived" means computed from printed rounded values; bands are stated where they matter.

## RECONCILIATION (ledger contract)
- Ledger rows: 140 (R001-R140, orphan_ids none). Rows read at structured ID and fulltext line: 140. ledger_reconciled_pct = 100.
- RESTATED internal ties (headline vs body vs p4 table), all pass: 429 (R019/R024/R081); 10% (R020/R026/R082); 156 (R021/R056/R084); 40% (R022/R057/R090); 135 (R023/R042/R109); 389 (R027/R046/R078); 8% (R048/R079); 443 (R030/R103); 9% (R031/R104); 394 (R032/R051/R100); 8% (R052/R101); 2,029 (R035/R115); 16% (R036/R116); 1,863 (R037/R053/R112); 14% (R054/R113); 91 (R041/R095); 106 (R058/R092); 3,234 (R043/R121); 217 (R062/R124).
- A2 FOOTNOTE_UNRESOLVED R034 and R039: resolved as composition residuals, see F14-03.
- A2 ZERO_STANDING R127-R129: read and treated under F1.
- R018 stray "66" (L71): unlabelled numeral from the headline graphic. No figure in the release maps to it. Not a finding.
- R130 text-layer displacement (L150-L153): an A1 extraction issue, not a company drafting issue. The render header (L16) governs.

## CROSS-DOCUMENT TIE (press release vs filed results and deck)
| PR figure (row, line) | Filed value (source) | Status |
| --- | --- | --- |
| Consol revenue 429, +10% (R019, L72) | about 4,291 mn derived from consol EBITDA 1,592 at 37.1%; growth +9.6% (RESULTS-A3 F2-04) | ties (rounding) |
| SA revenue 389 vs 360, +8% (R046-R048, L98-99) | 3,890 (R122) vs about 3,603; +8.0% (RESULTS-A3 F2-04, F12-04) | ties |
| SA EBITDA 156, 40% (R021-R022, L73) | 1,564, 40.2% (RESULTS-A3 coverage map #5) | ties |
| Consol EBITDA 159, 37%, +23% (R087-R091, L137-139) | 1,592, 37.1%, vs 1,297 (+22.7%) (RESULTS-A3 F2-04) | ties |
| Consol PAT 91, +10%, (47%) QoQ (R095-R097, L141) | 908 vs Q1 1,722 (-47.3%) (RESULTS-A3 F2-01, F4-01) | ties |
| SA PAT 106, (40%) QoQ (R092-R094, L141) | 908 + 155 gap = 1,063 (RESULTS-A3 F2-01); Q1 176 (DECK-A3 F2-01) | ties |
| Consol CFO 135, +19%, (17%) QoQ (R109-R111, L147) | H1 2,988 mn (RESULTS-A3 coverage map #6); Q1 derived 163.8 | ties inside a narrow band (Q2 must be 135.07-135.49 for (17%) to print) |
| SA CFO 124, (19%) QoQ (R106-R108, L147) | H1 2,768 mn; Q1 derived 152.8 | ties |
| Collections consol 443 +9%, SA 394 +8% (R030-R032, L82-83) | deck R441/R442, R832/R833; H1 consol 906 (DECK-A3 F12-02, values list) | ties |
| Deferred revenue consol 2,029 +16%, SA 1,863 +14% (R035-R037, L86-87) | deck R527/R015, R966/R973; SA Q1 1,858 (DECK-A3 F12-02) | ties |
| Busy revenue 37, collections 46, deferred 155 (R028, R033, R038) | deck Busy billing 46 (R1165), deferred 155 (DECK-A3 F12-01); segment Accounting Software 398 mn incl. others (RESULTS-A3 F12-03) | ties |
| Total income consol 421, SA 380 (R072, R075, L133) | other income consol (76) mn (RESULTS-A3 F2-03); deck (8) consol, (9) SA (DECK-A3 F16-02) | ties: 421 - 429 = (8); 380 - 389 = (9) |
| Cash and investments 3,234 (R043, L91) | about 3,234 Cr treasury (DECK-A3 F16-02) | ties |
| Paying suppliers 217K, (2%) YoY (R062, R124-R125) | 217K base, deck L753 (DECK-A3 values list) | ties; QoQ "(0%)" vs deck -615, see F16-04 |
| Unique enquiries 27 million (R059, L111) | 27 Mn, (14%) YoY, deck L1679-L1680 (DECK-A3 F16-03) | level ties; YoY omitted, see F16-01 |
| Supplier storefronts 8.9 million, +4% (R060-R061, L111-112) | no filed value in the A3 inputs | NOT CHECKED |
| "Audited" results (R007, L26) | results Note 1 unmodified audit opinion (RESULTS-A3 F14) | ties; the Q1 PR "audited" query (NOTION MEMORY F17-d) does not recur |

Numeric mismatches against filed values: 0. Every press-release finding below is a framing, basis or omission finding, not a number error.

## FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
| --- | --- | --- | --- | --- | --- | --- |
| F1-01 | F1 | R127-R129, R124-R126 | L151-L153 (render L16) | "Paying Suppliers (In `000) ... Consolidated - / - / -" | NEUTRAL-FACT | The template carries every metric in both columns. Paying suppliers is a marketplace (standalone) unit, so the consolidated cell is a dash. The group has no published customer count. Busy's unit (licences, 465K, new 11K vs 12K YoY per DECK-A3 F6-02) is not in the release. Consolidated revenue +10% has no volume denominator in this document. |
| F2-01 | F2 | R092-R097, R041, R058, R024-R028 | L141, L90, L106-107, L78-80 | "Net Profit for the period 106 27% (40%) 91 10% (47%)" | FORWARD-SIGNAL | Consol-minus-SA PAT: Q2 FY27 -15 (-14.2% of SA PAT). Q1 FY27 about -5 (-2.6%, derived from the QoQ prints: 91/0.53 = 172, 106/0.60 = 177; NOTION MEMORY 172/176 gives -2.3%). Q2 FY26 about -1 (-1%, derived from the YoY prints: 82.7 vs 83.5). Widened about 12pp QoQ and 13pp YoY (above 5pp). Revenue gap +40 (Busy 37 + others 3) and EBITDA gap +3 (159 - 156) are positive, so the -15 sits below EBITDA: associate losses 15.3 Cr (RESULTS-A3 F2-01). The release splits revenue, collections and deferred revenue into Standalone + Busy (L80, L83-84, L87-88) but does not split net profit, the one line where the non-standalone piece is negative. |
| F6-01 | F6 | R065, R064 | L117-118 | "fostering greater confidence and deeper, more meaningful engagement across the marketplace" | AMBIGUOUS | The CEO states engagement is deepening. Filed demand KPIs fell: active buyers (7%), unique enquiries (14%), enquiries delivered (12%) YoY (DECK-A3 F17-02). Two readings: (a) the trust programme (bank verification, NOTION MEMORY FA-02) deliberately removes low-quality enquiries and engagement per buyer rises; (b) demand loss narrated as quality. The separating observation: enquiries per active buyer and conversion per enquiry, plus bank-verification % against the >50%-in-one-year ladder. The statement is undated and unquantified. |
| F7-01 | F7 | R067 | L119-120 | "while we also explore new monetisation avenues" | AMBIGUOUS | Lexicon hit ("explore", stem of "exploring"). This is the release's only text near the new subsidiary IndiaMart Finance Limited, incorporated 04-Aug-2026 (RESULTS-A3 F6-01, F15-01). The release never names it. Question: is the lending subsidiary one of these avenues, what is its capital envelope, and when does it start. |
| F12-01 | F12 | R028, R033, R038, R029 | L80, L83-84, L88 | "Busy Infotech Revenue of Rs 37 Crore"; "Busy Infotech Collections of Rs 46 Crore" | FORWARD-SIGNAL | Busy collections minus revenue = 9 = the deferred build 155 - 146 (ties DECK-A3 F12-01). Q1 PR showed collections 59 vs revenue 36 (NOTION MEMORY F17-b), so Busy collections fell 22% QoQ. Busy explains about 13 of the 20 Cr consol QoQ collections fall (Q1 consol 463 derived from H1 906; SA about 402 to 394). The release gives no Busy YoY or margin. Filed: billing +20% YoY, at the checklist #7 red line (below 20% = red); margin 12% vs about 18% a year ago (DECK-A3 F12-01). Second consecutive release with Busy figures and no YoY. |
| F14-01 | F14 | R090, R091, R098, R099, R072, R075, R078, R081 | L137-L143, L133-L135 | "EBITDA Margin (%) 40% 37%"; "Net Profit Margin (%) 28% 22%" | AMBIGUOUS | The table uses two denominators. EBITDA margin is on revenue (156/389 = 40.1%; 159/429 = 37.1%; on total income it would print 41% and 38%). Net profit margin is on total income: 28% and 22% fit only total income (SA band 27.7-28.1%; consol 21.5-21.8%). On revenue they print 27% and 21%. With other income negative this quarter, the total-income basis lifts the NP margin by about 0.5-0.7pp. Question: which basis did the Q1 release use for NP margin. A basis switch in the quarter other income turned negative would be a reframing. |
| F14-02 | F14 | R023, R042, R109 | L74, L90, L147 | "Consolidated Cash generated from Operations of Rs. 135 Crore" | NEUTRAL-FACT | The headline calls 135 "Cash generated from Operations"; the body and table call it "Cash Flow from Operations". In an Ind AS 7 statement, "cash generated from operations" is the pre-tax subtotal. The 135 ties to the net operating cash flow split (H1 2,988 mn, RESULTS-A3). Label slip in the headline. Immaterial alone. |
| F14-03 | F14 | R034, R039, R024-R028 | L83, L87 | "primarily comprising"; "This primarily includes" | NEUTRAL-FACT | Resolves A2 FOOTNOTE_UNRESOLVED. Revenue residual 429 - 389 - 37 = 3 = deck "Revenue - Others" 3 Cr (DECK-A3 F12-03). Deferred residual 2,029 - 1,863 - 155 = 11 = subsidiary deferred revenue 166 (RESULTS-A3 F12-04, 1,660 mn) less Busy 155. Collections residual 443 - 394 - 46 = 3 fits the same "Others" perimeter [INFERENCE; no filed collections split]. The residual entities (Livekeeping and others) are not named. |
| F16-01 | F16 | R059-R062, R125 | L111-112 | "Unique business enquiries of 27 million in Q2FY27. Supplier Storefronts grew to 8.9 million, an increase of 4% YoY" | FORWARD-SIGNAL | The operational paragraph gives YoY only for the metric that grew. Enquiries fell 14% YoY (DECK-A3 F16-03, deck L1680); the release prints the level only. Paying suppliers fell 2% YoY; the text says "were 217K" and the decline sits only in the p4 table (R125). Active buyers (40 Mn, (7%)) are absent from the release. Values for thesis-broken #6 and checklist #3 (enquiries decline above 5% YoY for 2 quarters): Q2 -14%; Q1 -11% (Q1 deck, NOTION MEMORY) or about -7% (this deck's restated base, DECK-A3 F16-03). Both readings exceed 5%. A4 rules. |
| F16-02 | F16 | R021, R022, R084, R085, R087, R088, R091, R093 | L73, L137, L141 | "Standalone EBITDA of Rs. 156 Crore representing EBITDA margin of 40%" | AMBIGUOUS | Mixed-basis headline: consolidated revenue, standalone EBITDA, consolidated cash flow (L72-L74). Standalone is the higher margin (40% vs 37% consol). Second consecutive release with this choice (Q1 PR F16-a: 40% vs 35%, NOTION MEMORY). The SA EBITDA +36% YoY (R085) and SA PAT +27% YoY (R093) rest on a Q2 FY26 base that likely carries a 16 Cr investment impairment in SA other expenses (RESULTS-A3 F2-02, INFERENCE). Like-for-like SA EBITDA growth is about 19% (DECK-A3 F16-01). Like-for-like SA PAT growth is about 6.5% [INFERENCE: 106 / (83.5 + 16); the impairment is non-deductible per RESULTS-A3 F8]. Consol EBITDA +23% is the cleaner figure. |
| F16-03 | F16 | R041, R058, R072-R077, R092-R097 | L90, L106-107, L133, L141 | "Net Profit for the quarter was Rs. 91 Crore."; "Total Income 380 3% (18%) 421 5% (19%)" | FORWARD-SIGNAL | Each other body line carries "grew", "increased" or a YoY figure. Net profit gets the level only, and PAT is absent from the headline. PAT fell 47% consol and 40% SA QoQ (table only). The cause is other income: derived (8) consol (421 - 429) and (9) SA (380 - 389), vs 107 and 88 in Q1. The release never names other income or treasury. Checklist #9 red wording (sequential drop above 50%) is met on values 107 to (8); rolling 4Q 200.6 Cr is inside band (RESULTS-A3 F2-03). Second consecutive release: Q1 PR F16-b omitted PAT from the headline and F17-c left other income uncomposed (NOTION MEMORY). PAT stays exposed to treasury MTM on 3,234 Cr. |
| F16-04 | F16 | R062, R124-R126 | L112, L151-L153 (render L16) | "paying suppliers at the end of the quarter were 217K"; "217 (2%) (0%)" | FORWARD-SIGNAL | The table prints QoQ "(0%)". The deck states "615 paying suppliers declined this quarter" (deck L202, DECK-A3 values list), the fourth consecutive printed sequential fall. Q1 PR: flat YoY, -1% QoQ (NOTION MEMORY F1-a). Q2: (2%) YoY, (0%) QoQ, so the YoY trend worsened while the QoQ print rounds the decline away. Checklist #1 red (net adds below 0) met; base 217K above the 215K red line; thesis-broken #2 (below 209K) not fired. Watch 8B: supplier leg met on deck values; active-buyer leg unresolvable at a printed 40 Mn (DECK-A3 F16-06), and the release prints no active buyers. |
| F16-05 | F16 | R035-R036, R053-R054, R112-R117 | L86-87, L103-104, L149 | "Deferred Revenue as on September 30, 2026 increased to Rs. 2,029 Crore representing a YoY growth of 16%" | FORWARD-SIGNAL | The text frames deferred revenue on YoY (16% consol, 14% SA). The table shows QoQ 1% and 0%. SA deferred revenue rose 5 Cr QoQ (1,858 to 1,863), the smallest of four sequential builds (DECK-A3 F12-02). The 16% YoY mostly carries the Q4 FY26 build (+178 SA). Collections lead revenue, so forward revenue growth drifts toward high single digits (RESULTS-A3 F12-04, DECK-A3 F12-02 reach the same reading). |
| F17-01 | F17 | R050, R049, R125 | L99-100 | "The growth was primarily driven by improvement in realization from paying suppliers." | AMBIGUOUS | The driver claim is accurate on filed values: paying suppliers (2%) YoY, total ARPU +10%, top 10% ARPU +12% (DECK-A3 values list), so SA revenue +8% is all price and mix. The release prints no ARPU (checklist #4). Second consecutive release that names realization as the driver and prints no ARPU (Q1 PR F17-a, NOTION MEMORY). Question: split of realization into price increase vs mix shift to higher tiers, and the churn cost of price increases. |
| F17-02 | F17 | R029, R041, R095-R097 | L80, L90 | "Busy Infotech" (only entity named); "Net Profit for the quarter was Rs. 91 Crore" | AMBIGUOUS | The release is silent on every item that moved the S-vs-C gap and the group perimeter this quarter: associate losses 15.3 Cr, +20% QoQ (monitor #11; RESULTS-A3 F2-01); Fleetx mark (monitor #12); IndiaMart Finance Limited incorporated 04-Aug-2026 (Q2 concall monitorable "first capitalisation"); MonotaRO associate exit 29-May-2026 with no disclosed outcome (RESULTS-A3 F1-02). The consolidated paragraph is framed as "Standalone + Busy", which leaves these out of view. |

## CHECKLIST SCORECARD
| Check | Status | Basis |
| --- | --- | --- |
| F1 Zero-value standing | FINDING | 3 ZERO_STANDING rows (R127-R129), consolidated paying-supplier dash: no group customer count (F1-01). R114 0% and R126 (0%) are real rounded values; R126 is used in F16-04. |
| F2 Standalone vs consolidated | FINDING | The release carries SA and consol revenue, EBITDA, PAT. PAT gap -14.2% vs about -2.6% QoQ and about -1% YoY (above 5pp). The gap sits below EBITDA and the release does not decompose it (F2-01). |
| F3 Shell-entity | N.A. | The release carries no cost lines (no employee, material or depreciation lines). Group-level shell test is in RESULTS-A3 F3. |
| F4 Unaudited contribution | N.A. | No auditor paragraph in a press release. |
| F5 Going concern / EoM | N.A. | No EoM or going-concern text in a press release. |
| F6 Forward-commitment mining | FINDING | Lexicon hits "will host" (L160) and "will be available" (L168-169) are procedural. The CEO quote (L116-121) carries undated strategic statements; one contradicts the filed demand KPIs (F6-01). |
| F7 Hedge-phrase mining | FINDING | One hit, "explore new monetisation avenues" (F7-01). No "subject to", "no assurance" or "endeavour". The release carries no safe-harbour text at all. No hedge on revenue lumpiness or concentration. |
| F8 Tax forensics | N.A. | No tax, PBT or deferred-tax line in the release. |
| F9 OCI forensics | N.A. | No OCI line in the release. |
| F10 Share count / dilution | N.A. | The release prints no EPS, share count or paid-up capital. |
| F11 Reserves / net-worth tie-out | N.A. | The release prints no net worth or reserves. Its only balance-sheet figures (cash and investments 3,234; deferred revenue 2,029) tie to the deck and results (cross-document tie table). |
| F12 Segment forensics | FINDING | Applied to the Standalone + Busy split, the release's segment-like disclosure. Busy collections -22% QoQ; no YoY or margin (F12-01). |
| F13 Board outcome beyond results | N.A. | A Reg 30 press-release cover (L19-L59) carries no board outcome. Release signed 15:35:42 (R012), after the results meeting close at 15:00 (RESULTS-A3 F14-01), webinar 17:00 (R131). No timing issue. |
| F14 Note drafting inconsistencies | FINDING | Mixed margin denominators in one table (F14-01). Headline CFO label (F14-02). Composition residuals resolved (F14-03). |
| F15 Entity list diffs | PASS | The release names one subsidiary (Busy Infotech, R029). The Q1 release also split by Busy only (NOTION MEMORY F17-b), so the release's own entity list did not change. Group perimeter changes (IndiaMart Finance added, MonotaRO exit) are filed in the results (RESULTS-A3 F15) and are recorded here as silence (F17-02). No verbatim diff possible (no prior fulltext). |
| F16 Dropped / reframed disclosures | FINDING | Selective YoY in operational highlights (F16-01); mixed-basis headline on a contaminated base (F16-02); PAT and other income level-only (F16-03); paying suppliers (0%) QoQ vs -615 (F16-04); deferred revenue on YoY while QoQ is flat (F16-05). Dropped-metric test vs Q1 release limited to NOTION MEMORY; no Q1 fulltext. |
| F17 Silence audit | FINDING | Checklist cross-check below. ARPU silent for a second release (F17-01). Associates, Fleetx, IndiaMart Finance and MonotaRO silent (F17-02). |

## COMMITMENT REGISTER (F6)
| commitment | implied date | note/turn ref | status word |
| --- | --- | --- | --- |
| Earnings webinar for investors and analysts | 27-Oct-2026 17:00 IST | p5 L160-162 (R131, R132) | scheduled ("will host") |
| Audio and video recording of the call on the IR website | undated, after the call | p5 L168-170 (R135) | pending ("will be available") |
| Build a trusted, reliable marketplace; strengthen platform trustworthiness | undated | p3 L116-118 (R064, R065) | underway ("efforts ... are fostering") |
| AI central to user experience (discovery, matchmaking, conversational tools) | undated | p3 L118-119 (R066) | underway ("remains") |
| Explore new monetisation avenues | undated | p3 L119-120 (R067) | initiated ("explore") |
| Create long-term value for stakeholders | undated | p3 L120-121 (R068) | none |

## F17 WHAT WAS NOT DISCUSSED (release vs Notion checklist, triggers and Q2 monitorables)
Consecutive-quarter counts use the Q1 press-release findings in NOTION MEMORY (L1359-1371). Where that record does not log an item, the count is ">=1" (Q1 release status unknown).

| item | release status | consecutive releases silent |
| --- | --- | --- |
| #1 Net paying suppliers | PARTIAL: base 217K (L112), (2%) YoY and (0%) QoQ in table; net count -615 not printed (F16-04) | >=1 (net count) |
| #2 Active buyers (LTM) | SILENT (filed 40 Mn, (7%), deck) | >=1 |
| #3 Unique enquiries | PARTIAL: level 27 Mn (L111); YoY (14%) omitted (F16-01) | >=1 (YoY) |
| #4 Top 10% ARPU | SILENT, though realization is named as the driver (F17-01) | 2 (Q1 PR F17-a) |
| #5 SA EBITDA margin | ADDRESSED: 40% (L73, L106, L139) | 0 |
| #6 CFO/PAT rolling 12m | PARTIAL: quarter CFO and PAT printed; derived Q2 consol 1.48x, SA 1.17x; no rolling ratio | 2 (Q1 PR F16-c gave no ratio) |
| #7 Busy billing growth and margin | PARTIAL: collections 46 (L84) with no YoY; no margin (F12-01) | 2 (Q1 PR F17-b) |
| #8 Promoter holding and pledge | SILENT (not a release item) | n/a |
| #9 Treasury other income | SILENT in text; derivable (8) consol, (9) SA from the table (F16-03) | 2 (Q1 PR F17-c) |
| #10 Auditor commentary | "Audited" only (L26); annual item | n/a |
| #11 Associate cohort P&L | SILENT; consol PAT not decomposed (F2-01, F17-02) | >=1 |
| #12 Fleetx mark | SILENT (F17-02) | >=1 |
| IndiaMart Finance Ltd first capitalisation | SILENT; "explore new monetisation avenues" only (F7-01) | >=1 |
| Bank-verification % vs ladder | PARTIAL: "efforts to strengthen platform trustworthiness" (L117), no % (F6-01) | >=1 |
| Busy licences / CAGR vs guidance | SILENT | >=1 |
| Enquiry-decline residual quantification | SILENT | >=1 |
| Advertising actual figure | SILENT | >=1 |
| Realized vs unrealized other income | SILENT | 2 (Q1 PR F17-c) |
| MonotaRO associate exit outcome | SILENT (F17-02) | >=1 |

## VALUES FOR A4 TESTS (stated, not ruled)
- Thesis-broken #6 / checklist #3, enquiries YoY: Q2 FY27 (14%) (deck L1680); Q1 FY27 -11% (Q1 deck, NOTION MEMORY) or about -7% (this deck's base). Both above 5%. The release prints the level only (L111).
- Checklist #1 / watch 8B, paying suppliers: 217K (R124), (2%) YoY (R125), (0%) QoQ (R126); deck net -615.
- Checklist #5: SA EBITDA margin 40% (R090). Like-for-like YoY gain about 4pp, not 8pp (F16-02, INFERENCE).
- Checklist #9: other income derived (8) consol, (9) SA (R072-R081).
- Checklist #7: Busy collections 46 (R033); filed billing +20% YoY, margin 12%.

```yaml
stage: A3-forensics
company: "INDIAMART"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/indiamart-q2fy27/work/forensics_pressrelease_indiamart_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
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
  F13: N.A.
  F14: FINDING
  F15: PASS
  F16: FINDING
  F17: FINDING
findings:
  - {id: "F1-01", check: "F1", line: "L151-L153, render L16 (R127-R129)", classification: "NEUTRAL-FACT", implication: "Consolidated paying-supplier cell is a dash; no group customer count; Busy licence volume absent from release"}
  - {id: "F2-01", check: "F2", line: "L141/L90/L106-107 (R092-R097,R041,R058)", classification: "FORWARD-SIGNAL", implication: "Consol-SA PAT gap -15 (-14.2%) vs ~-2.6% QoQ and ~-1% YoY; sits below EBITDA (associates 15.3 Cr); release splits revenue/collections/deferred into SA+Busy but not PAT"}
  - {id: "F6-01", check: "F6", line: "L117-118 (R065)", classification: "AMBIGUOUS", implication: "CEO claims deeper engagement while active buyers -7%, enquiries -14%, enquiries delivered -12% YoY; trust-filter vs demand-loss readings"}
  - {id: "F7-01", check: "F7", line: "L119-120 (R067)", classification: "AMBIGUOUS", implication: "'explore new monetisation avenues' is the only text near IndiaMart Finance Ltd (incorporated 04-Aug-2026), which the release never names"}
  - {id: "F12-01", check: "F12", line: "L80/L83-84/L88 (R028,R033,R038)", classification: "FORWARD-SIGNAL", implication: "Busy collections 46 vs 59 in Q1 (-22% QoQ), ~13 of the 20 Cr consol QoQ collections fall; no YoY or margin; filed billing +20% at checklist #7 red line, margin 12% vs ~18%"}
  - {id: "F14-01", check: "F14", line: "L137-L143 (R090,R091,R098,R099)", classification: "AMBIGUOUS", implication: "EBITDA margin on revenue, NP margin on total income; negative OI lifts printed NP margin ~0.5-0.7pp (28%/22% vs 27%/21%); ask Q1 basis"}
  - {id: "F14-02", check: "F14", line: "L74 vs L90/L147 (R023,R042,R109)", classification: "NEUTRAL-FACT", implication: "Headline labels 135 'Cash generated from Operations' (Ind AS pre-tax subtotal); figure ties to net CFO"}
  - {id: "F14-03", check: "F14", line: "L83/L87 (R034,R039)", classification: "NEUTRAL-FACT", implication: "'primarily' residuals resolved: revenue 3 = deck Others; deferred 11 = subsidiary deferred 166 less Busy 155; collections 3 same perimeter [INFERENCE]"}
  - {id: "F16-01", check: "F16", line: "L111-112 (R059-R062,R125)", classification: "FORWARD-SIGNAL", implication: "YoY printed only for storefronts (+4%); enquiries (-14%) level only; suppliers -2% table only; active buyers omitted; thesis-broken #6 values both quarters above 5%"}
  - {id: "F16-02", check: "F16", line: "L73/L137/L141 (R021,R022,R085,R093)", classification: "AMBIGUOUS", implication: "Headline picks SA EBITDA (40% vs consol 37%), second release running; SA EBITDA +36% and PAT +27% on base with likely 16 Cr impairment; like-for-like ~19% and ~6.5% [INFERENCE]"}
  - {id: "F16-03", check: "F16", line: "L90/L106-107/L133/L141 (R041,R058,R072-R077,R092-R097)", classification: "FORWARD-SIGNAL", implication: "PAT level-only, -47%/-40% QoQ in table only; OI derived (8)/(9) vs 107/88 in Q1, never named; checklist #9 drop wording met; second release running"}
  - {id: "F16-04", check: "F16", line: "L112/L151-L153 (R062,R124-R126)", classification: "FORWARD-SIGNAL", implication: "Paying suppliers (0%) QoQ rounds away deck net -615 (fourth sequential fall); YoY worsened flat to (2%); checklist #1 red met; 8B supplier leg met"}
  - {id: "F16-05", check: "F16", line: "L86-87/L103-104/L149 (R035-R036,R053-R054,R114,R117)", classification: "FORWARD-SIGNAL", implication: "Deferred revenue framed on YoY 16%/14% while QoQ 1%/0% (SA +5 Cr, smallest build); forward revenue growth drifting to high single digits"}
  - {id: "F17-01", check: "F17", line: "L99-100 (R050)", classification: "AMBIGUOUS", implication: "Realization named as driver; no ARPU printed for second release; filed ARPU +10%, top 10% +12%, suppliers -2%; growth is all price/mix"}
  - {id: "F17-02", check: "F17", line: "L80/L90 (R029,R041,R095)", classification: "AMBIGUOUS", implication: "Silent on associate losses (#11), Fleetx (#12), IndiaMart Finance capitalisation and MonotaRO exit; consol framed as SA+Busy only"}
forward_signals: ["F2-01", "F12-01", "F16-01", "F16-03", "F16-04", "F16-05"]
ambiguous: ["F6-01", "F7-01", "F14-01", "F16-02", "F17-01", "F17-02"]
commitments:
  - {commitment: "Earnings webinar for investors and analysts", implied_date: "2026-10-27 17:00 IST", ref: "p5 L160 (R131,R132)", status_word: "scheduled"}
  - {commitment: "Call recording on IR website", implied_date: "undated, after call", ref: "p5 L168-170 (R135)", status_word: "pending"}
  - {commitment: "Strengthen platform trustworthiness", implied_date: "undated", ref: "p3 L116-118 (R064,R065)", status_word: "underway"}
  - {commitment: "AI central to user experience", implied_date: "undated", ref: "p3 L118-119 (R066)", status_word: "underway"}
  - {commitment: "Explore new monetisation avenues", implied_date: "undated", ref: "p3 L119-120 (R067)", status_word: "initiated"}
  - {commitment: "Create long-term value for stakeholders", implied_date: "undated", ref: "p3 L120-121 (R068)", status_word: "none"}
gate_a3: pass
blank_checks: []
analyst_note: "Every release number ties to the filed results and deck within rounding; zero numeric mismatches. The release misleads by selection, not by error. It prints YoY where the number grew (storefronts +4%, deferred revenue +16%, SA EBITDA +36%) and levels where it fell (enquiries 27M, -14% filed; PAT 91, -47% QoQ; paying suppliers 217K, -615 net rounded to (0%)). Active buyers and ARPU are absent. The headline uses standalone EBITDA, the higher-margin basis, for a second release running, and its +36% YoY likely rides a 16 Cr impairment in the base (inference). Consolidated PAT is the only line not split into Standalone + Busy, and it is the line where associate losses (15 Cr) bite. Other income turned negative ((8) derived) and is never named. A4 should note the thesis-broken #6 values: enquiries fell more than 5% YoY in both Q1 and Q2 on either Q1 base. The CEO's 'deeper engagement' claim needs its separating test: enquiries per buyer and the bank-verification %."
```
