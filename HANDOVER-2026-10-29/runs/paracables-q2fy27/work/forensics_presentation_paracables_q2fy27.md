# A3 FORENSIC NOTES: PARACABLES Q2 FY27 (doctype: presentation, investor deck, 37 slides)

Inputs read: A1 structured (R001-R522), A1 fulltext (563 lines), A2 ledger, Notion snapshot 28-Oct-2026 (line 11 properties, L210-215, L489-506, L612-622, L644-651, L735-737 only). No prior-quarter deck exists. The source PDF and inputs/ were not opened.
Quotes are verbatim from the fulltext. Runs of spaces are collapsed. Line numbers are fulltext lines (L###), slide = page.
Notion content is memory to weigh. It is never cited as anchored evidence below. Where it is used, it is tagged [NOTION MEMORY].

## 0. LEDGER RECONCILIATION

- Rows in ledger: 522 (R001-R522). Rows read in the structured file and at their cited fulltext line: 522. Reconciled: 100%.
- LAYOUT_UNRESOLVED rows R293, R294, R295, R385, R386, R387, R388 were read and treated as UNPLACED. No finding rests on them.
- Pipeline defects found during the read. These are A1/A2 issues, not document findings:
  1. Line drift. On slide 28, A1 cites R217-R292 one line early. Example: R225 (40.9) cites L419; the token sits on L420 "Operating Profit 40.9 34.7". The same drift affects R346 (65 cites L448; the token is on L447).
  2. R371 cite. A1 cites L448 for the FY26 CWIP dash. L448 reads "Capital Work - in - Progress 4 228" and has no dash value. The two value dashes sit at L450 "Total Non - Current Assets 346 -" and L453 "Trade Receivables 395 -". See F1 for why nil FY26 CWIP still holds.
  3. Missing tokens. "20.4%" (L425) and "85.3%" (L426) are not in the structured file. A2's sweep reported MISSING_FROM_STRUCTURED: none. These are the H1 YoY cells of the depreciation and finance-cost rows.
  4. Possible Dep/FC swap. PBT arithmetic gives the same result if depreciation and finance cost trade places, so it cannot test A1's placement of R260/R266 (Q2 FY26) and R262/R268 (H1 FY26). The column order in L416-L427 reads Q2 FY26 as 3.8 then 4.0, and H1 FY26 as 7.4 then 7.9. The YoY tokens (15.7%, 96.8%, 20.4%, 85.3%) fit Dep 3.8/FC 4.0 and Dep 7.4/FC 7.9. A1 assigned the reverse. This is NOT used as evidence. A4/A5 confirm against the filed results. The finance-cost finding (A3-14) holds under both placements.
  5. R385-R388 (285, 413, 33, 81) sum to 812, which equals FY26 total current assets (R382). The FY26 column order fits inventories 285, receivables 413, cash 33, other CA 81, with FY26 investments nil. This is NOT used as evidence (orchestrator ruling: unplaced).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R371, R370, R372-R375, R047, R048, R008 | L448, L450 (s30); L353, L356 (s23); L211-212 (s15); L96 (s6) | "Capital Work - in - Progress 4 228"; "31 acres \| ₹ 300 Cr Investment"; "(3rd under construction)" | FORWARD-SIGNAL | FY26 CWIP is nil: 228 PPE + 89 other NCA = 317 total NCA, so no room for CWIP whichever dash is placed. H1 FY27 CWIP is Rs 4 Cr (1.3% of the Rs 300 Cr project). The most build visible on the balance sheet is about Rs 31 Cr (CWIP 4 plus the Rs 27 Cr rise in ROU + other NCA, 89 to 116). PPE fell 228 to 226 against Rs 8.8 Cr H1 depreciation. At least Rs 269 Cr of spend, and its funding, must land in the 6-9 months before Q1 FY28 partial commissioning, or the date slips. The CWIP line exists to show that build. It is close to empty while slide 23 says civil works "have commenced". Bear lean: ask for CWIP plus capital advances, the capex phasing and the funding mix. |
| A3-02 | F6 | R443, R452, R456, R484, R450, R451 | L212, L353, L356, L358, L361, L476 | "Project work is on track, with partial commissioning planned for Q1 FY28, as previously guided."; "Orders for most critical plant and machinery already placed." | FORWARD-SIGNAL | A dated milestone, reaffirmed. Status words: civil works "commenced" (underway), critical P&M orders "already placed" (completed, "most"), hiring "underway". Slide 32 (L476) drops "partial" ("Progress toward Q1 FY28 commissioning"). Tracker: the next deck must show CWIP accretion that matches these words (see A3-01). |
| A3-03 | F6 | R444, R050, R051, R485, R486, R507 | L216-219 (s15) | "T argeted T urnover" ... "₹ 500 Cr" ... "₹ 1,200 Cr" | FORWARD-SIGNAL | Rs 500 Cr in FY28 must come from a plant that is only partially commissioned in Q1 FY28. Rs 1,200 Cr in FY29 is 4.0x turnover on the Rs 300 Cr investment. [NOTION MEMORY] line 11 recorded "targeted Rs 1,200 Cr over 2-3 yrs"; the deck now ties it to FY29. Testable each quarter from Q1 FY28. |
| A3-04 | F6 | R458, R389, R496, R506 | L481 (s32); L211-212 (s15) | "Medium - term ambition: ₹5,000 crore revenue over five years"; "Near - optimal utili zation" | FORWARD-SIGNAL | This needs a 21.2% revenue CAGR from FY26 Rs 1,912 Cr. Both existing plants run at "near-optimal" use, and Narmadapuram targets Rs 1,200 Cr. The deck names no capacity or capex for the rest. This points to unannounced capex and possibly more equity. Ask for the capacity bridge. |
| A3-05 | F7 | R499, R500, R501 | L27, L35 (s2) | "indicative and provisional in nature and may be subject to change"; "time and cost overruns on projects" | NEUTRAL-FACT | The deck calls its own figures provisional. A4 anchors numbers to the filed results, not to the deck. The safe-harbour list names project time and cost overruns while Narmadapuram is the live project. No prior deck exists, so a newly added hedge cannot be tested. |
| A3-06 | F10 | R285-R292, R346, R347, R400 | L428, L447, L550 | "EPS (Rs.) 0.74 0.64 ... 1.38"; "32,72,39,473" | NEUTRAL-FACT | EPS growth lags PAT growth. Q2 YoY: EPS +68.2% vs PAT +82.8%. QoQ: +15.6% vs +23.0%. H1: +30.2% vs +36.2%. This implies a share base up about 8.7% YoY. Paid-up capital rose Rs 61 Cr to Rs 65 Cr. Q2 EPS implies 32.7 Cr shares (24.2/0.74), which matches shares outstanding. The deck names no corporate action. [NOTION MEMORY] June-2026 preferential issue plus 72L promoter warrants. EPS growth will keep trailing PAT growth until the warrants convert. |
| A3-07 | F10 | R192, R290 | L406-407 (s27); L428 (s28) | "₹1.38" "Diluted EPS"; "EPS (Rs.) ... 1.38" | AMBIGUOUS | Slide 27 labels the figure diluted. Slide 28 shows the same figure with no label. Basic EPS is not shown. Outstanding promoter warrants ([NOTION MEMORY] 72L) should open a basic-to-diluted spread. Ask for basic and diluted EPS and the warrant count in the diluted base. |
| A3-08 | F11 | R346-R351, R194, R195, R282, R025, R340 | L447-449 (s30); L406-408 (s27) | "₹920 Cr ... Networth vs ₹ 749 Cr in H1 FY26" | NEUTRAL-FACT | The tie-out holds: 65 + 855 = 920 and 61 + 717 = 778, matching slides 9, 27 and 29. The roll-forward does not close inside the deck: 778 + H1 PAT 43.9 = 821.9 against 920, a Rs 98.1 Cr gap (10.7% of net worth). Candidate reconciling items: preferential equity allotment ([NOTION MEMORY] Rs 97.67 Cr), promoter warrant upfront money ([NOTION MEMORY] Rs 7.56 Cr), issue costs, OCI, dividend. The +22.8% YoY net-worth line on slide 27 includes raised capital. The deck never mentions the raise. |
| A3-09 | F14 | R001, R027, R301-R305, R296-R300 | L85 (s6); L156 (s9) | "35.4 % ... Revenue CAGR"; "4 - year R evenue CAGR: 34.7%" | NEUTRAL-FACT | The deck uses two definitions of the same metric. 35.4% is total revenue including other income (585 to 1,964). 34.7% is sales (581 to 1,912). |
| A3-10 | F14 | R075-R078, R057, R113, R006, R416 | L258-260 (s17); L233-236 (s16); L275 (s18) | "US (Exports) Revenue Revenue (8.5)%"; "₹ 158 Cr ₹ 173 Cr ₹ 550 Cr ₹ 483 Cr"; "USA remains the largest export market," | AMBIGUOUS | The "US (Exports)" row equals TOTAL exports: FY26 Rs 550 Cr (slide 16) and FY25 Rs 483 Cr (slide 18, Rs 483.0 Cr). Two readings: (a) the row is mislabelled; (b) the "35+ geographies" export nothing, so 100% of export revenue carries US tariff exposure. A product-and-geography mix chart (slide 17, "Export Sales" next to product lines) adds to the blur. Ask for the US share of exports. |
| A3-11 | F14 | R515, R168, R227, R514, R518 | L435 (s29); L382 (s25); L420 (s28) | "Operating Margin* 20.4" | NEUTRAL-FACT | The asterisk has no footnote. No slide says whether figures are standalone or consolidated. Operating profit QoQ reads 17.9% on slide 25 and 17.8% on slide 28. Each item is immaterial. Together they are a drafting data point. |
| A3-12 | F16 | R098-R109, R069, R132, R133, R143-R147 | L271, L274, L285 (s18); L258 (s17); L293-294 (s19) | "Export share rebounds to 29% from 16% in H2 FY26; strong recovery in export demand." | AMBIGUOUS | The baseline is the H2 FY26 tariff trough. YoY, H1 FY27 exports were Rs 313.1 Cr against Rs 381.5 Cr (-17.9%), and Q2 US exports fell 8.5%. Q2 export (Rs 158 Cr) is flat on Q1 (about Rs 155 Cr). The export share of the order book fell from 16% to 14% QoQ. Export orders (about Rs 99 Cr) cover less than one quarter of export revenue. H1 growth is all domestic (+56.3%). Bear lean: the recovery is half-on-half off a trough, not YoY. |
| A3-13 | F16 | R002, R003, R023, R306-R310, R316-R320, R513, R517 | L85 (s6); L149 (s9); L437 (s29) | "48.5% ... 4 - Year EBITDA CAGR"; "EBITDA ₹ 118 Cr" | NEUTRAL-FACT | The headline EBITDA includes other income. FY26 other income is about Rs 52.3 Cr (118 - 65.7), 44% of FY26 EBITDA. Operating EBITDA CAGR for FY22-FY26 is 34.0% (20.4 to 65.7), 14.5 pp below the headline. The 64.6% PAT CAGR ends on a FY26 PAT that the same other income lifted. |
| A3-14 | F16 | R197, R198, R263-R268, R352, R353, R358, R359 | L410-412 (s27); L425 (s28); L450, L453 (s30) | "0.14 x Debt / Equity (FY22: 0.87x)"; "Finance Cost 7.9 6.9" | FORWARD-SIGNAL | Slide 27 frames leverage against FY22. Gross borrowings rose from Rs 116 Cr to Rs 132 Cr (+13.8%) after about Rs 98 Cr of new equity. Long-term borrowings went from Rs 2 Cr to Rs 21 Cr. Q2 finance cost was Rs 7.9 Cr against Rs 3.8-4.0 Cr in Q2 FY26 (+98% to +108% under either A1 placement). H1 was Rs 14.8 Cr against Rs 7.4-7.9 Cr. Annualised Q2 finance cost (Rs 31.6 Cr) is about 24% of period-end borrowings. The cost likely sits outside reported debt: bill discounting, LC or acceptance interest, or intra-quarter peaks. Finance cost now takes 24% of Q2 PBT. Ask for average gross debt, bills discounted, and the finance-cost split. |
| A3-15 | F16 | R199, R200, R519, R360, R361 | L410-412 (s27); L454 (s30) | "108 ... Working Capital Days vs 109 days in H1 FY26" | AMBIGUOUS | The deck chose a YoY comparator. [NOTION MEMORY] recorded WC days of 101 (FY26) and 96 (Q1 FY27). On that record, 108 is a 12-day sequential rise. Trade payables fell from Rs 197 Cr to Rs 143 Cr (-27%) while revenue grew. Ask for the definition and the Q1 FY27 and FY26 figures on the same basis. |
| A3-16 | F16 | R049, R460, R441, R461 | L214-215 (s15); L166-170 (s10) | "EHV cables up to 220 kV" | AMBIGUOUS | [NOTION MEMORY] line 11 (from the FY26 AR) records the Narmadapuram scope as "EHV<=132kV". The deck now says up to 220 kV and adds e-beam and specialised conductors, while the budget stays at Rs 300 Cr. Either the scope grew with no capex change, or the earlier record was narrow. Verify against the AR and filings. |
| A3-17 | F16 | R152, R511, R136, R148, R446, R149 | L315 (s21); L287-294, L296 (s19) | "₹200+ Cr HTLS order book (as on date)"; "No firm - price orders beyond 3 to 4 months" | AMBIGUOUS | The HTLS book is undated, while the main book is dated 30 Sep 2026. The deck does not say whether the HTLS book sits inside the Rs 731 Cr. No slide defines the order book (gross or net of GST, pending or executed). Utility HTLS tenders do not fit easily with a 3-4 month firm-price cap. Rs 731 Cr covers about 1.3 quarters of Q2 revenue. |
| A3-18 | F17 | Notion L493-498, L612-622, L644-651, L737 | deck-wide (s25-s30) | (silence; see table 4) | CONFIRMATORY-NEGATIVE | The deck is silent on operating CFO (Trigger B), the preferential issue and use of proceeds, warrant exercise, the other-expenses driver, keyman and other-income repeatability, pledge status, and receivable ageing or ECL. [NOTION MEMORY] line 11 records filed H1 CFO of -Rs 31.89 Cr. Silence on a deteriorating cash metric is a confirmatory negative under Role 5. |
| A3-19 | F10 | R401-R404, R429, R521 | L546-551 (s36) | "45.87%" ... "48.11%" | AMBIGUOUS | The label pairing is unresolved (CHART_LABEL_ORDER), but the four values sum to 100.00%. If the two small slices are FPI and DII, combined institutional holding is 6.02%. [NOTION MEMORY] puts the promoter at 49.18% before the issue. 45.87% fits that stake diluted by the larger share base. This is unplaced; A4 reads the filed shareholding pattern. |

## 2. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | R371 FY26 CWIP nil (confirmed by 228 + 89 = 317) and H1 FY27 CWIP Rs 4 Cr against the Rs 300 Cr build (A3-01). R097 "zero rejections" is a quality claim, not a template line. |
| F2 | N.A. | The deck carries one unlabelled set of figures. There is no standalone vs consolidated pair to decompose. |
| F3 | N.A. | No standalone vs consolidated cost lines in a presentation. |
| F4 | N.A. | No auditor Other Matters paragraph in a deck. |
| F5 | N.A. | No EoM or going-concern paragraph in a deck. No prior-quarter text either. |
| F6 | FINDING | Narmadapuram Q1 FY28 reaffirmed with status words; FY28/FY29 turnover targets; Rs 5,000 Cr five-year ambition (A3-02, A3-03, A3-04). |
| F7 | FINDING | Safe harbour calls the figures "indicative and provisional" and lists project overruns. No prior deck to diff (A3-05). |
| F8 | PASS | ETR from deck PBT and PAT: Q2 FY27 25.3%, Q1 FY27 25.7%, Q2 FY26 25.3%, H1 FY27 25.5%, H1 FY26 25.7%, all near the 25.17% statutory rate. No deferred-tax split or prior-year tax line in the deck. |
| F9 | N.A. | No OCI line in the deck. |
| F10 | FINDING | Share base up about 8.7% YoY; EPS growth trails PAT growth; diluted-only labelling; shareholding pairing unresolved (A3-06, A3-07, A3-19). |
| F11 | FINDING | Net worth ties internally. The Rs 98.1 Cr roll-forward gap (10.7%) is unexplained in the deck (A3-08). |
| F12 | N.A. | Slide 17 carries segment revenue only. There are no segment assets or liabilities to trend. |
| F13 | N.A. | No board outcome in a deck. |
| F14 | FINDING | Two revenue CAGR definitions; the "US (Exports)" row equals total exports; footnote-less asterisk; basis unlabelled (A3-09, A3-10, A3-11). |
| F15 | N.A. | No consolidation entity list in the deck. No prior list to diff. |
| F16 | FINDING | Export "recovery" off a trough baseline; EBITDA headline includes other income; D/E vs FY22 while finance cost doubled; WC days comparator; 220 kV scope; undated HTLS book and undefined order book (A3-12 to A3-17). DROPPED-metric test not possible (no prior deck). |
| F17 | FINDING | Silence audit run against the Notion checklist: 13 of 19 items not addressed in the deck (A3-18, table 4). |

Counts: PASS 1 | FINDING 8 | N.A. 8 | blank 0.

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Narmadapuram partial commissioning ("as previously guided") | Q1 FY28 (Apr-Jun 2027) | s15 L212; s23 L361; s32 L476 | underway |
| Narmadapuram foundation and civil works | in line with indicated schedule (undated) | s23 L353 | underway ("commenced") |
| Orders for most critical plant and machinery | by 30 Sep 2026 | s23 L356 | completed ("already placed", "most") |
| Plant hiring, phased ramp to commissioning | to Q1 FY28 | s23 L358 | underway |
| Narmadapuram targeted turnover Rs 500 Cr | FY28 | s15 L216-218 | initiated (target) |
| Narmadapuram targeted turnover Rs 1,200 Cr | FY29 | s15 L216-219 | initiated (target) |
| HTLS capacity augmentation at Narmadapuram | FY28 | s21 L325 | initiated (planned) |
| Revenue of Rs 5,000 Cr | within five years (about FY31) | s32 L481 | initiated (ambition) |
| Move toward pre-tariff margins as export markets normalise | FY27 roadmap | s32 L467-471 | initiated |
| Rebuild exports, broaden international diversification | FY27 roadmap | s32 L466-470 | initiated |
| HTLS tenders "under bid and finalization stages" | undated | s21 L317 | underway |
| Data-centre approvals with other developers "progressing" | undated | s22 L336-339, L346 | underway |
| No firm-price orders beyond 3-4 months (standing policy) | ongoing | s19 L296 | standing |

Lexicon hits with no commitment: "will be equally important" (L48, industry text). No hits for "expected to be", "fast-track", "shall be completed", "has been completed", "in the process of", "proposes to", "board has approved", "intends to".

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit vs Notion checklist)

Consecutive-quarter count: the deck is the only Q2 FY27 document read here, and no prior deck exists. "1" means silent in this deck. Prior silences are added only where the Notion record states them [NOTION MEMORY].

| checklist item (Notion ref) | addressed in deck? | deck evidence | quarters silent |
|---|---|---|---|
| Op EBITDA margin above 5.2% toward 7-8% (L212, L650) | YES | L421 "Operating Margin % 7.3% 6.6%" | 0 |
| Receivables unwind / days level (L213, L648, 8E Q1 L493) | PARTIAL | L453 "Trade Receivables 395" (about 66 days on H1 revenue, my arithmetic). Receivable days not disclosed. | 1 (days) |
| Operating CFO, Q1/Q2 (8E Q1 L493, L649, Trigger B L622, Step 12 Q3 L737) | NO | no cash-flow slide; WC days only (L410-412) | 1 |
| Pref issue terms, dilution, use of proceeds (L214, 8E Q3 L495, L617, L647) | NO | net worth jump with no narrative (L406-408, L449) | 2 (Q4 FY26 call "terms withheld", L495; this deck) |
| Allottee identity (L614, L646, Trigger A L621) | NO | none (resolved by filing per line 11) | 1 |
| Warrant exercise pace (L615, L651) | NO | none | 1 |
| Other Expenses +331 bps driver (8E Q2 L494, Step 12 Q2 L737) | NO | only L156 "FY26: tariff disruption + one - time items weighed on margins"; no expense split on s28 | 2 (Q4 FY26 call "unprobed", L494; this deck) |
| Q1 FY27 exit op margin number (8E Q4 L496) | YES | L421 "6.6%" | 0 |
| Promoter pledge and FII+DII (8E Q5 L497, L215) | PARTIAL | s36 percentages with unresolved labels (L546-551); pledge not stated | 1 (pledge) |
| Keyman insurance maturities / other-income repeatability (8E Q6 L498) | NO | other income Q2 3.8 vs 19.9 YoY (L417), no explanation | 1 |
| Receivables overdue under 6m: collection and ECL (Step 12 Q1 L737) | NO | none | 1 |
| Narmadapuram hard commissioning date (L737) | YES | L361 "partial commissioning planned for Q1 FY28" | 0 |
| Narmadapuram CWIP build (L737; line 11 "CWIP Rs 3.59 Cr") | NO (narrative) | BS only, L448 "Capital Work - in - Progress 4" | 1 |
| Narmadapuram long-lead equipment status (L737) | YES | L356 "Orders for most critical plant and machinery already placed." | 0 |
| Q1 FY27 results gate (L616) | YES (superseded) | s25/s28 Q1 FY27 column | 0 |
| Use-of-proceeds ring-fence (L617) | NO | none | 1 |
| Trigger B: CFO negative hardens 0.65x cash multiplier (L622) | NO | none | 1 |
| Funding plan for the Rs 300 Cr Narmadapuram capex | NO | L211 "₹ 300 Cr Investment" with no funding line | 1 |
| Promoter background / Role 2 (L215) | N.A. to deck | analyst-side item | - |

Not addressed: 13 of 19 rows (counting PARTIAL as not addressed; the N.A. row excluded from the denominator gives 13 of 18).

## 5. QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)

A3-01, A3-02, A3-03, A3-04, A3-14 (FORWARD-SIGNAL); A3-07, A3-10, A3-12, A3-15, A3-16, A3-17, A3-19 (AMBIGUOUS). A3-18 (CONFIRMATORY-NEGATIVE) carries the silence list.

```yaml
stage: A3-forensics
company: "PARACABLES"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-paracables-q2fy27-a220cd/runs/paracables-q2fy27/work/forensics_presentation_paracables_q2fy27.md"
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
  - {id: "A3-01", check: "F1", line: "s30 L448/L450; s23 L353,L356; s15 L211", classification: "FORWARD-SIGNAL", implication: "CWIP nil FY26, Rs 4 Cr H1 FY27 vs Rs 300 Cr plant; at most ~Rs 31 Cr build visible; >=Rs 269 Cr spend plus funding must land before Q1 FY28 or date slips"}
  - {id: "A3-02", check: "F6", line: "s23 L353,L356,L358,L361; s32 L476", classification: "FORWARD-SIGNAL", implication: "Q1 FY28 partial commissioning reaffirmed; civil commenced, critical P&M placed, hiring underway; tracker milestone"}
  - {id: "A3-03", check: "F6", line: "s15 L216-219", classification: "FORWARD-SIGNAL", implication: "Narmadapuram Rs 500 Cr FY28 / Rs 1,200 Cr FY29 = 4.0x turnover on Rs 300 Cr; FY28 target rests on partial commissioning"}
  - {id: "A3-04", check: "F6", line: "s32 L481; s15 L211-212", classification: "FORWARD-SIGNAL", implication: "Rs 5,000 Cr in 5 yrs = 21.2% CAGR; plants near-full, no capacity bridge named; foreshadows further capex and funding"}
  - {id: "A3-05", check: "F7", line: "s2 L27,L35", classification: "NEUTRAL-FACT", implication: "deck figures self-described provisional; anchor to filed results; project-overrun risk listed"}
  - {id: "A3-06", check: "F10", line: "s28 L428; s30 L447; s36 L550", classification: "NEUTRAL-FACT", implication: "share base ~+8.7% YoY; EPS +68.2% vs PAT +82.8%; paid-up 61->65; EPS growth trails PAT until warrants settle"}
  - {id: "A3-07", check: "F10", line: "s27 L406-407; s28 L428", classification: "AMBIGUOUS", implication: "single EPS labelled diluted on s27, unlabelled on s28; basic not shown; warrant spread unknown"}
  - {id: "A3-08", check: "F11", line: "s30 L447-449; s27 L406-408", classification: "NEUTRAL-FACT", implication: "net worth ties; Rs 98.1 Cr (10.7%) roll-forward gap = unnamed equity raise; slide 27 +22.8% includes raised capital"}
  - {id: "A3-09", check: "F14", line: "s6 L85; s9 L156", classification: "NEUTRAL-FACT", implication: "revenue CAGR 35.4% (incl OI) vs 34.7% (sales); two definitions in one deck"}
  - {id: "A3-10", check: "F14", line: "s17 L258-260; s16 L233-236; s18 L275", classification: "AMBIGUOUS", implication: "US (Exports) row = total exports 550/483; mislabel or 100% US tariff exposure despite 35+ geographies"}
  - {id: "A3-11", check: "F14", line: "s29 L435; s25 L382; s28 L420", classification: "NEUTRAL-FACT", implication: "Operating Margin* without footnote; basis unlabelled; minor QoQ drift; cumulative drafting data point"}
  - {id: "A3-12", check: "F16", line: "s18 L271,L274,L285; s17 L258; s19 L293-294", classification: "AMBIGUOUS", implication: "export recovery framed off H2 FY26 trough; H1 exports -17.9% YoY; Q2 US -8.5%; export order share 16%->14%"}
  - {id: "A3-13", check: "F16", line: "s6 L85; s9 L149; s29 L437", classification: "NEUTRAL-FACT", implication: "headline EBITDA CAGR 48.5% incl OI; operating EBITDA CAGR 34.0%; FY26 OI ~44% of EBITDA"}
  - {id: "A3-14", check: "F16", line: "s27 L410-412; s28 L425; s30 L450,L453", classification: "FORWARD-SIGNAL", implication: "D/E framed vs FY22; borrowings +13.8% after equity; finance cost ~2x YoY, ~24% of period-end debt annualised; off-BS financing likely; 24% of PBT"}
  - {id: "A3-15", check: "F16", line: "s27 L410-412; s30 L454", classification: "AMBIGUOUS", implication: "WC days 108 vs H1 FY26 109; Notion memory FY26 101 / Q1 96 implies sequential rise; payables -27%"}
  - {id: "A3-16", check: "F16", line: "s15 L214-215", classification: "AMBIGUOUS", implication: "EHV up to 220 kV vs Notion AR memory <=132kV; scope up, Rs 300 Cr budget unchanged"}
  - {id: "A3-17", check: "F16", line: "s21 L315; s19 L287-296", classification: "AMBIGUOUS", implication: "HTLS Rs 200+ Cr undated, inclusion in Rs 731 Cr unstated; order-book definition absent; tender tenor vs 3-4 month cap"}
  - {id: "A3-18", check: "F17", line: "deck-wide s25-s30; Notion L493-498,L612-622,L644-651,L737", classification: "CONFIRMATORY-NEGATIVE", implication: "13 of 19 checklist items unaddressed incl CFO (filed H1 CFO negative per memory), pref issue, warrants, other-expenses driver"}
  - {id: "A3-19", check: "F10", line: "s36 L546-551", classification: "AMBIGUOUS", implication: "shareholding labels unpaired; promoter likely 45.87% post-dilution; FPI+DII 6.02% if small slices; verify from filed SHP"}
forward_signals: ["A3-01", "A3-02", "A3-03", "A3-04", "A3-14"]
ambiguous: ["A3-07", "A3-10", "A3-12", "A3-15", "A3-16", "A3-17", "A3-19"]
commitments:
  - {commitment: "Narmadapuram partial commissioning", implied_date: "Q1 FY28", ref: "s15 L212; s23 L361; s32 L476", status_word: "underway"}
  - {commitment: "Narmadapuram foundation and civil works", implied_date: "per indicated schedule", ref: "s23 L353", status_word: "underway"}
  - {commitment: "Orders for most critical plant and machinery", implied_date: "by 30-Sep-2026", ref: "s23 L356", status_word: "completed"}
  - {commitment: "Plant hiring phased to commissioning", implied_date: "to Q1 FY28", ref: "s23 L358", status_word: "underway"}
  - {commitment: "Narmadapuram targeted turnover Rs 500 Cr", implied_date: "FY28", ref: "s15 L216-218", status_word: "initiated"}
  - {commitment: "Narmadapuram targeted turnover Rs 1,200 Cr", implied_date: "FY29", ref: "s15 L216-219", status_word: "initiated"}
  - {commitment: "HTLS capacity augmentation at Narmadapuram", implied_date: "FY28", ref: "s21 L325", status_word: "initiated"}
  - {commitment: "Revenue Rs 5,000 Cr", implied_date: "within five years (~FY31)", ref: "s32 L481", status_word: "initiated"}
  - {commitment: "Move toward pre-tariff margins", implied_date: "FY27 roadmap", ref: "s32 L467-471", status_word: "initiated"}
  - {commitment: "HTLS tenders under bid and finalisation", implied_date: "undated", ref: "s21 L317", status_word: "underway"}
  - {commitment: "Data-centre approvals with other developers", implied_date: "undated", ref: "s22 L336-339", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck's most forward-looking silence is the balance sheet under Narmadapuram. CWIP is nil at FY26 and Rs 4 Cr at 30-Sep-26 against a Rs 300 Cr plant guided to partial commissioning in Q1 FY28. At least Rs 269 Cr of spend, and its funding, must land within three quarters or the date slips. The H1 equity raise (about Rs 98 Cr, never named in the deck) did not lower debt. Borrowings rose Rs 16 Cr, and finance cost doubled YoY to an annualised 24% of period-end debt, which points to financing outside the debt lines. Export 'recovery' is half-on-half off the tariff trough: YoY exports fell 17.9% and the export share of the order book slipped to 14%. Headline CAGRs include other income. Pipeline defects: A1 line cites on slides 28 and 30 run one line early. R371's cited line has no value dash (the dashes are at L450 and L453). Tokens 20.4% (L425) and 85.3% (L426) were not captured. Column order and YoY tokens suggest A1 swapped depreciation and finance cost for Q2 FY26 and H1 FY26. None of this was used as evidence. A4/A5 confirm against the filed results."
```
