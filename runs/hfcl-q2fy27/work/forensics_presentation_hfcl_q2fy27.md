# A3 FORENSIC NOTES: HFCL Q2 FY27, doctype PRESENTATION (investor deck, 25 slides)

Agent: A3 forensic notes | model claude-opus-5-5 | run date 2026-10-19 | loop iteration 1 update 2026-10-20
Inputs read: A1 structured (R001-R424), A1 fulltext (652 lines), A2 ledger (including loop-1 rows PM01-PM07), notion-brief.md sections 4, 7, 8 (plus 5 for cross-quarter capex and order references; memory, not evidence).
Not read: source PDF, anything under inputs/. Prior-quarter fulltext: none supplied.

Evidence rules for this file
- Line numbers refer to runs/hfcl-q2fy27/extracted/hfcl-presentation-q2fy27-fulltext.md.
- Slides 8-10 (R001-R218) are PAIRING_UNRESOLVED. Per the A2 note, no finding is built on those statement cells. The results filing is the primary source for them.
- Any cross-quarter comparison uses the Notion brief and is labelled [MEMORY]. Memory is weighed, not anchored. A4 must verify each [MEMORY] baseline against the Q1 FY27 deck or filing before it becomes a question premise.
- Derived numbers are labelled [DERIVED] with the arithmetic shown.

## 1. LEDGER RECONCILIATION

| Item | Count |
|---|---|
| Structured row IDs in A1 | 424 (R001-R424) |
| A2 MISSING_FROM_STRUCTURED rows (loop 1) | 7 (PM01-PM07) |
| Rows in ledger | 431 |
| Rows read at the cited fulltext line | 431 |
| ledger_reconciled_pct | 100 |

Every row was read at its line. Statement rows R001-R218 were read at lines 189-291 and confirmed scrambled (example: the 32.73% at line 189 is the revenue QoQ change, 2,541.79 / 1,914.98 = 1.3273, sitting one row above its label). The six ZERO_STANDING rows (R046, R049, R050, R099, R101, R139) were read at lines 202, 204, 236, 237 and 264.

Loop 1 (PM01-PM07): each row was read verbatim at its cited lines.
- PM01, line 215: "1.49". This is the Q1 FY27 diluted EPS token. It matches the Q1 figure on file [MEMORY: Rs 1.49]. It adds context to FN-14 but is not a new finding.
- PM02, lines 119-120: "Secured raw materials and advanced cable capabilities strengthen our ability to capture this long-term opportunity." New finding FN-17.
- PM03, lines 467-471, column 1: "Emphasis on high-end, customized solutions enables stronger customer engagement and higher value realization amid a structural demand upcycle." New finding FN-18.
- PM04, lines 467-471, column 2: "Emerging as a high-growth adjacency to the OFC business, driven by exports and hyper-scalers/ data centers". New finding FN-19.
- PM05, lines 503-518, column 1: "Focus on higher value-added products on the back of continued R&D driven innovation to aid margins and ease working capital". FN-12 is extended to cite lines 503-506. Commitments C-18 to C-20 are added. No separate finding.
- PM06, lines 532-533: "#1 in OFC and strong market share in Wifi and UBR". New finding FN-20.
- PM07, lines 537-538: "Actively catering to Domestic telcos and Bharatnet for rapid roll out". New finding FN-21.

Anchor drift found (non-material, recorded for A1 hygiene):
- R139 (line 264): the "-" is the hyphen in the label "TOTAL - NON – CURRENT LIABILITIES". It is an extraction artefact, not a zero cell.
- R321 (line 64): the name "(Manoj Baid)" sits at line 62; line 64 is the title.
- R333 (line 414): the R&D centre names sit at lines 416-419.
- R335 (line 451): "HFCL Eka Fiber" sits at line 453 and "HFCL A2- 180 Fiber" at lines 455-456.
- R342 (line 607): "SBTi" sits at line 588; line 607 holds the approval date.
- PM07 (lines 537-538): the phrase ends with "roll out" on line 539.
None changes a finding.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F7 (and F6) | R356, R357 | slide 5, lines 124-129 | "we are reviewing how best to position our different businesses for their next phase of growth ... each business vertical has a distinct operating, profitability and working capital profile ... we are evaluating various strategic options" | FORWARD-SIGNAL | Separation or restructuring language is new in a filed document. On this name it reopens the demerger history (slip log, [MEMORY]) and thesis-broken trigger #6 (structure that transfers OFC/defence value at a discount). No structure is announced, so trigger #6 does not fire. Reading A: carve out the working-capital-heavy EPC/turnkey book to clean up the product company. Reading B: a structure that moves OFC or defence value away from listed minorities. Separating observation: which entity keeps listed minorities, and the swap ratio or price. A4 question 1. |
| FN-02 | F16 | R227, R231, R349, R350 | slide 5, lines 111-113 | "Based on our current expectations, we now expect revenue growth of at least 80% in FY27" | FORWARD-SIGNAL | Guidance hardened from "aspiration" to "now expect" and lifted from 40% (Q1 seed log) through "at least 60%" (broker, 05-Oct, unverified) to at least 80% [MEMORY for both priors]. [DERIVED] FY27 floor = 4,949.27 x 1.8 = Rs 8,908.69 Cr (FY26 base per [MEMORY]). H1 = 2,541.79 + 1,914.98 = Rs 4,456.77 Cr. H2 needs Rs 4,451.92 Cr, about Rs 2,226 Cr a quarter, below the Q2 print of Rs 2,541.79 Cr. Holding Q2's run rate for H2 gives Rs 9,540 Cr (+92.8%). So either the guide is a floor, or it embeds an H2 step-down of about 12% a quarter from Q2. Also, Rs 10,000 Cr "much earlier than the FY29 horizon" (line 112-113) needs only +12.2% in FY28 on the FY27 floor. Ask which. |
| FN-03 | F16 | R288, R289, R367 | slide 19, lines 503-504 | "EBITDA margin is expected to expand from ~16.7% in FY26 to >27% by FY29" | FORWARD-SIGNAL | Target raised from "22-25% by FY29" (Q1 seed log, [MEMORY]) and above the "~25-26% after captive preform" broker line two weeks earlier [MEMORY]. Q2 headline is 25.89% (line 127), 111 bps short of the new target with preform not due until October 2028 (line 442). A raised margin target is a dated promise for the Role 5 tracker. |
| FN-04 | F16 | R233, R234, R246 | slide 5, lines 125-127; slide 7, line 168 | "₹658.00 Cr, ... 25.89 %" | AMBIGUOUS | Definition check. Q1 reported EBITDA (23.25%) included other income; Q1 operating EBITDA was 21.63% [MEMORY]. If Q2's Rs 658.00 Cr also includes other income, the operating margin is lower than 25.89%. The Q2 other-income cell (line 191) is PAIRING_UNRESOLVED, so the gap is not computed here. Verify in the results filing. The >27% FY29 target (FN-03) needs the same definition stated. |
| FN-05 | F16 | R257-R261, R262, R263, R292, R294, R298, R300 | slide 11, lines 302-314; slide 19, lines 507-510; slide 20, lines 532-539 | "57% of the total Order book comes from export"; "Revenue from private sector has increased to 92%"; "Products segment now ~91% of revenues" | FORWARD-SIGNAL | The book's mix runs against all three slide-19 mix targets. The result holds under any pairing of the unresolved series. [DERIVED] Customer split 10,105 + 18,806 = 28,911, so government is at least 10,105 / 28,911 = 35.0% of the book against 8% of revenue. Category split 4,090 + 5,070 + 19,751 = 28,911, so products are at most 68.3% and non-product at least Rs 9,160 Cr (31.7%), against ~9% of revenue. Export is 57% of the book against 63% of revenue and the >70% FY27 target. Reading A: long-dated O&M and EPC inflate the non-product and government share, and product orders turn faster. Reading B: as BharatNet III executes, the revenue mix moves back toward government, EPC and domestic work, and working-capital intensity rises. That contradicts "lowering working-capital intensity" (line 539-540). Separating observation: order book by execution year and by category. |
| FN-06 | F14 (F16) | R290, R291, R293, R298, R368, R369, R420 | slide 19, lines 502-504 and 507-508; slide 20, line 532 | "more than 70% Revenue from Export by FY27" vs "exports at 63% of revenues with a target to reach 65%+ from FY27 onwards"; "Targeting ~90% Revenue from Product" vs "Products segment now ~91% of revenues" | AMBIGUOUS | Two export targets for the same year sit on one slide, and the product target is already below the current actual. The base period for "63%" is not stated. [DERIVED] On the FY27 revenue floor of Rs 8,908.69 Cr, >70% exports needs Rs 6,236 Cr. With Q1 exports of Rs 1,063.30 Cr [MEMORY]: if 63% is the Q2 share (Rs 1,601 Cr), H2 needs 80.2% export share; if 63% is the H1 share (Rs 2,808 Cr), H2 needs 77.0%. The 65%+ version needs 67-70% in H2. Both sit well above the 57% export share of the order book (FN-05). Lean bear: treat 65%+ as the operative guide until management confirms the higher number. Ask which number is the guide, and for the base period. |
| FN-07 | F16 | R237, R286, R287, R339, R355, R375, R415, R416 | slide 5, lines 122-124; slide 17, lines 469-470; slide 20, lines 532-536 | "~₹1850 Cr total Defence order book ( ~INR 1600 crs through an entity proposed to be acquired)"; "FY27 Defence revenue aspiration of approximately ₹500 crore" | FORWARD-SIGNAL | [DERIVED] HFCL's own defence book is about 1,850 - 1,600 = Rs 250 Cr, half the Rs 500 Cr FY27 aspiration. The rest depends on H1 defence revenue already booked (not in deck), new orders, or the acquisition closing inside FY27. [MEMORY] says the aerospace book is excluded until consolidation in Q4 FY27. The "global scale" claim (line 532-536) rests on an entity HFCL does not yet own. Lean bear: the Rs 500 Cr aspiration is at risk if the close slips, and the fuze slip history (5 quarters, [MEMORY]) is the base rate. |
| FN-08 | F16 | R286, R287, R415 | slide 17, line 469 | "~₹1850 Cr total Defence order book ( ~INR 1600 crs through an entity proposed to be acquired)" | AMBIGUOUS | Against [MEMORY] Q1 baseline (~Rs 2,300 Cr total, ~Rs 2,000 Cr via the target; thesis also carries HASPL Rs 1,930 Cr), the total fell about Rs 450 Cr and the target's book about Rs 400 Cr in one quarter. That is executed, cancelled, re-scoped or redefined. Ask the reason, and whether the target's revenue on that execution accrues to HFCL. |
| FN-09 | F16 | R226, R229, R255, R257-R261, R302, R416, R419 | slide 5, lines 114-115; slide 11, lines 300-314; slide 20, lines 534-536 | "₹28,911 Cr CONFIRMED ORDER BOOK"; "confirmed unexecuted export order book of Rs.~1,600 crores through proposed aerospace business being acquired" | AMBIGUOUS | Order book definition. The deck does not say whether the Rs 28,911 Cr consolidated book includes the Rs ~1,600 Cr held by an entity not yet acquired. If it does, about 5.5% of the "confirmed" book is not HFCL's yet. Second point: [MEMORY] says the Q1 book was "~65% Networks". The Q2 "64% ... from OFC / DCI" line (314) implies Products is the Rs 19,751 Cr slice (68%), so Networks is at most 17.5%. If both are right, the category definitions changed between decks. The chart baseline is consistent: Q4 FY26 Rs 21,206 Cr and Q1 Rs 26,665 Cr (lines 302, 306) match the Q1 figure on file. [DERIVED] Implied Q2 inflow is about 28,911 - 26,665 + 2,541.79 = Rs 4,788 Cr (book-to-bill ~1.9x), using revenue as the execution proxy. |
| FN-10 | F16 | R278-R281, R361, R362, R394 | slide 16, lines 428-434 | "43.1 mn fkm ... 62 mn fkm ... Expanding by July 2028 ... Current: 28 mn fkm/annum ... Current: 39 mn fkm/annum" | AMBIGUOUS | The interim Dec-2026 milestone (OF 28 to 33.9, OFC 30.5 to 42.36 mn fkm, [MEMORY]) does not appear. Only "Current" and July-2028 end states are shown. OF "Current" is still 28, the pre-expansion level. OFC "Current" 39 implies part of the OFC step is already in. Ask whether the Dec-2026 OF step is on track or folded into the July-2028 target. A silent fold-in would be a delivery-slip candidate for the promise log. |
| FN-11 | F16 | R230, R283, R285, R353, R363, R364 | slide 5, line 118; slide 16, lines 436-442 | "planned investment of approximately ₹1,800 crore in optical fibre, cable and preform"; "₹230 Cr As Phase1 for creating facility for MMHG" | AMBIGUOUS | Capex reframes against [MEMORY]: MMHG Phase-1 was Rs 275 Cr and is now Rs 230 Cr. The Rs 215 Cr DC-connectivity facility (Sep-2027) is not in the deck. Deck capex adds to about Rs 1,800 + 230 = Rs 2,030 Cr [DERIVED], against the broker-quoted ~Rs 2,500 Cr [MEMORY]. No funding split is given (a 14-Sep watch item). Ask for the full capex list, phasing and debt/equity split. |
| FN-12 | F16 | R300, PM05 | slide 20, lines 538-540; slide 19, lines 503-506; slide 5, lines 126-127 | "Private customers contribute ~ 92% of revenues lowering working-capital intensity"; "Focus on higher value-added products ... to aid margins and ease working capital" | AMBIGUOUS | The deck makes two working-capital claims but shows no receivables, DSO, unbilled or CFO figure in its narrative slides. Balance-sheet cells (slide 10) are unresolved and not used. Tripwire #4 (second quarter of receivables silence, or >Rs 200 Cr unexplained unbilled rise) cannot be judged from the deck. It rests on the results filing and the concall. If both are also silent, it is a confirmatory negative under Role 5. (Loop 1: lines 503-506 added from PM05.) |
| FN-13 | F14 | R329, R339, R340, R360, R417 | slide 24, line 628; slide 13, lines 366-368; slide 17, lines 470-474; slide 20, line 536 | "HASPL HFCL Advance Systems Private Limited"; "entity proposed to be acquired"; "proposed aerospace business being acquired"; "(Aerospace Products through Proposed Acquisitions)" | AMBIGUOUS | The glossary defines HASPL, but no slide uses the term. The target is never named and appears in three phrasings, one plural ("Acquisitions"). This suggests a slide or name was removed, or the deal scope has more than one target. Ask: name the target(s), HASPL's role (acquirer or target), consideration, close date and approvals. This links to the AR question on a strategic-partner stake at HASPL [MEMORY] and to FN-01. |
| FN-14 | F10 | R310, PM01 | slide 8, lines 208 and 215; slide 22, line 574 | "EPS (Diluted ₹)"; "1.49"; "1,53,06,02,463" | AMBIGUOUS | The deck shows diluted EPS only. Basic EPS is absent, so the basic-diluted spread cannot be read. The Q1 diluted token "1.49" (line 215, PM01) matches the Q1 figure on file, when diluted equalled basic [MEMORY]. Shares outstanding are 153.06 cr at 30-Sep-2026. The 7.5 cr promoter warrants at Rs 74 [MEMORY] are 4.9% of that count [DERIVED: 7.5 / 153.06] and are not mentioned. Q1's open question carries forward. Verify the spread in the results filing. |
| FN-15 | F14 | R382, R409, R424 | slide 1, lines 40-41; slides 8-10, lines 184, 220, 251 | "Un-audited Financial Results ... both on Standalone and Consolidated basis" | NEUTRAL-FACT | The cover letter says the deck covers both bases, but the deck carries consolidated statements only. The standalone-consolidated PAT gap, a Q1 open question (37.1% of standalone, [MEMORY]), cannot be read from the deck; F2 runs on the results filing. The deck also has no forward-looking-statement disclaimer slide (R424), although it carries hard guidance (FN-02, FN-03, FN-06). Governance data point only. |
| FN-16 | F14 | R347 | slide 3, lines 80-89; lines 93, 146, 321, 479, 552; slide 19, line 499; slide 21, line 557 | "//CHAPTER 04" (Message), "//CHAPTER 05" (Financials), "//CHAPTER 01" (About HFCL), "//CHAPTER 02" (Strategic Focus), "//CHAPTER 07" (Appendix); "02 Expanding ... 02 Optimising"; "Emmission" | NEUTRAL-FACT | Divider chapter numbers do not match the contents page (01-05). Strategic priorities are numbered 01, 02, 02. There is a typo in the appendix index. Each is immaterial alone. Together with FN-13 and FN-15, they suggest the deck was assembled from older templates. Cumulative governance data point. |
| FN-17 | F6 | PM02, R285, R363 | slide 5, lines 119-120; slide 16, lines 440-442 | "Secured raw materials and advanced cable capabilities strengthen our ability to capture this long-term opportunity." | AMBIGUOUS | "Secured" is stated as complete, but the deck gives no counterparty, tenor, volume or price. Captive preform arrives only "By October 2028" (line 442), so FY27-FY28 preform is bought in. The >27% FY29 margin target (FN-03) and the ~25-26% "after captive preform" line [MEMORY] both depend on input cost until then. The Preform technology partner is an open 14-Sep watch item [MEMORY]. Ask: what is secured (preform, fiber, other), from whom, for how long, and at fixed or floating price. |
| FN-18 | F16 | PM03 | slide 17, lines 467-471 (column 1) | "Emphasis on high-end, customized solutions enables stronger customer engagement and higher value realization amid a structural demand upcycle." | AMBIGUOUS | The deck claims pricing gains with no realisation metric (Rs per fkm, or price/mix split of growth). Two points lean bear. First, the largest export order is a multi-year contract (FY27-FY31 [MEMORY]) with margins "1-2% lower than spot" (Q4 FY26 concall, [MEMORY]), so locked prices may miss an upcycle. Second, "structural" is a claim the deck does not evidence. OFC has cycled before, and "OFC realisation declining" is a standing early-warning signal [MEMORY]. Reading A: realisation rises because the mix shifts to high-fiber-count and customised cable. Reading B: volume drives growth and the price gain is spot-only. Separating observation: realisation per fkm, contract versus spot, by quarter. |
| FN-19 | F16 | PM04, R230 | slide 17, lines 467-471 (column 2) | "Emerging as a high-growth adjacency to the OFC business, driven by exports and hyper-scalers/ data centers" | AMBIGUOUS | The PCS/DC adjacency is described as high-growth, but the deck gives no PCS revenue, order book or margin. The capacity that would serve it, the Rs 215 Cr DC-connectivity facility due Sep-2027 [MEMORY], is absent from the capex slides (FN-11). Prior guidance was Rs 400-500 Cr in FY26-27 and Rs 800-1,000 Cr in FY27-28 [MEMORY]. Ask: H1 FY27 PCS revenue against that path, and the status of the Rs 215 Cr facility. |
| FN-20 | F14 | PM06, R264 | slide 20, lines 532-533; slide 13, line 347 | "#1 in OFC and strong market share in Wifi and UBR" vs "#1 OPTICAL FIBER CABLE ... SUPPLIER IN INDIA" | AMBIGUOUS | Slide 13 limits the #1 claim to India. Slide 20 drops "in India", and neither slide gives a source, metric (volume in fkm or revenue) or period. The Wi-Fi/UBR "strong market share" claim carries no number. The Notion moat score has 0 of 12 claims confirmed [MEMORY], so a leadership claim needs its basis before it counts. Ask: the source and metric for #1 in OFC (India and global), and the Wi-Fi/UBR share figures. |
| FN-21 | F14 | PM07, R373 | slide 20, lines 537-539; slide 19, lines 514-515 | "Actively catering to Domestic telcos and Bharatnet for rapid roll out" vs "deliberately shifting from low-profit turnkey work" | AMBIGUOUS | The deck says HFCL is moving away from low-profit turnkey work, while slide 20 promotes BharatNet roll-out, a government EPC programme (~Rs 4,834 Cr cumulative BharatNet III, [MEMORY]). Q1 turnkey lost Rs 87.53 Cr; EPC losses were guided at Rs 80-90 Cr a quarter [MEMORY]. Government is at least 35% of the book (FN-05). The deck gives no BharatNet III revenue, PBT margin or receivables, so checklist items 6-7 stay silent at deck level for a second quarter. Ask: BharatNet III revenue, PBT margin and receivables in Q2, and whether "shifting from turnkey" means no new EPC bids. |

## 3. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | N.A. | Results-filing check. All six ZERO_STANDING rows read (lines 202, 204, 236, 237, 264). R139 is a label hyphen (artefact). The rest are scrambled statement cells, not used per the A2 note. The template-line question moves to the results-filing A3. |
| F2 | N.A. | Deck is consolidated-only (lines 184, 220, 251). No standalone figures to decompose. See FN-15. |
| F3 | N.A. | No standalone cost lines in the deck. |
| F4 | N.A. | No auditor report or Other Matters paragraph in the deck. |
| F5 | N.A. | No Going Concern or EoM paragraph in the deck. No prior-quarter fulltext either. |
| F6 | FINDING | 20 dated or dateable commitments mined from slides 1, 5, 13, 16, 17, 19, 20 and 23 (register below). Lexicon hits: "expected to" (lines 503, 532, 539), "will" (lines 119, 513), "commences" (line 541), "proposed to be acquired" / "being acquired" (lines 366-368, 470, 536). Completion claim "Secured raw materials" (line 119, PM02). Material items: FN-01, FN-02, FN-03, FN-07, FN-17. |
| F7 | FINDING | Lexicon applied to the deck's narrative text (MD message, strategy slides). Hit: "evaluating" (line 127). Related hedges: "reviewing how best to position" (line 125), "Based on our current expectations" (line 111), "aspiration" (lines 112, 123). See FN-01. |
| F8 | N.A. | Tax cells on slides 8-9 are PAIRING_UNRESOLVED. Results filing is primary. |
| F9 | N.A. | OCI cells on slides 8-9 are PAIRING_UNRESOLVED. Results filing is primary. |
| F10 | FINDING | Share count 1,53,06,02,463 (line 574). Diluted EPS only; no basic EPS, no warrant mention. Q1 diluted token 1.49 (line 215, PM01) matches the Q1 figure on file. FN-14. Ties: market cap 34,691.10 / 153.06 cr shares = Rs 226.65 a share. Free-float market cap 24,871.37 / 34,691.10 = 71.69%, which matches line 572. Shareholding adds to 100.00% (lines 569-575). Promoter 28.29%, unchanged from the 22-Sep record date [MEMORY]. Pledge not disclosed. |
| F11 | PASS | Shareholder funds read at line 257 (5,755.44 / 4,948.59; column pairing per the header order on line 255, cell PAIRING_UNRESOLVED). The deck has no third-party net-worth figure to reconcile against. Full tie-out of Other Equity and paid-up capital runs on the results filing. |
| F12 | N.A. | No segment assets, liabilities or results in the deck. Segment share claims ("Products segment now ~91%", line 532) are used in FN-05 and FN-06. |
| F13 | N.A. | Board-outcome check belongs to the outcome letter and results filing. The cover letter (lines 35-46) states only results approval. No AR, AGM, fund-raise or director items. |
| F14 | FINDING | Deck-internal drafting checks: FN-06 (conflicting export targets, product target below actual), FN-13 (HASPL orphan and unnamed target), FN-15 (standalone claim, no disclaimer), FN-16 (numbering and typo), FN-20 (#1 claim qualifier dropped, unsourced), FN-21 (turnkey exit vs BharatNet roll-out). |
| F15 | N.A. | No consolidation entity list in the deck. Entity mentions (target entity, HASPL) are handled under F14 (FN-13). |
| F16 | FINDING | No prior deck supplied. Cross-deck diffs use Notion memory, labelled [MEMORY]. Findings: FN-02 (guide hardened and raised), FN-03 (margin target raised), FN-04 (EBITDA definition), FN-05 (book mix vs revenue mix targets), FN-07 and FN-08 (defence book), FN-09 (order book definition and category split), FN-10 (dropped Dec-2026 capacity step), FN-11 (capex reframes), FN-12 (working-capital claims with no metric), FN-18 (realisation claim with no metric), FN-19 (PCS adjacency with no figures). Order-book chart baseline is consistent with the Q1 figure on file. |
| F17 | N.A. | Concall-specific. A presentation is not a transcript. A deck-coverage table of the Notion checklist follows as information for A4. It does not count as a silence audit. |

## 4. COMMITMENT REGISTER (F6)

| # | commitment | implied date | slide / line ref | status word |
|---|---|---|---|---|
| C-01 | FY27 revenue growth of at least 80% over FY26 ("now expect") | FY27 (Mar-2027) | slide 5, line 111 | initiated (raised from 40% aspiration, [MEMORY]) |
| C-02 | Rs 10,000 Cr revenue aspiration "much earlier than the FY29 horizon" | before FY29 | slide 5, lines 112-113 | initiated (pulled forward) |
| C-03 | Pipeline "at advanced stages of conversion" into orders | undated | slide 5, line 115 | underway |
| C-04 | ~Rs 1,800 Cr investment in optical fibre, cable and preform | to Oct-2028 (C-07 to C-09) | slide 5, line 118 | initiated |
| C-05 | FY27 Defence revenue ~Rs 500 Cr (aspiration) | FY27 | slide 5, line 123 | initiated (see FN-07) |
| C-06 | Review of business positioning; "evaluating various strategic options" | undated | slide 5, lines 124-129 | initiated (evaluating) |
| C-07 | OF capacity 28 to 43.1 mn fkm | July 2028 | slide 16, lines 428-434 | underway ("Expanding") |
| C-08 | OFC capacity 39 to 62 mn fkm | July 2028 | slide 16, lines 428-434 | underway ("Expanding") |
| C-09 | Preform 600 MT/annum, capex Rs 1,250 Cr | October 2028 | slide 16, lines 436-442 | initiated |
| C-10 | MMHG Phase-1 facility, Rs 230 Cr, Andhra Ammunition Complex | undated ("upcoming") | slide 16, lines 436-439 | initiated (amount reframed from Rs 275 Cr, [MEMORY]) |
| C-11 | Acquisition of aerospace business / "entity proposed to be acquired" (Rs ~1,600 Cr book) | undated in deck (CY26 close per [MEMORY]) | slide 13, lines 366-368; slide 17, lines 469-474; slide 20, lines 534-536 | initiated ("proposed", "being acquired") |
| C-12 | EBITDA margin >27% by FY29 (from ~16.7% FY26) | FY29 | slide 19, lines 503-504 | initiated (raised from 22-25%, [MEMORY]) |
| C-13 | ~90% revenue from product; >70% revenue from export | by FY27 | slide 19, lines 502-504 | initiated |
| C-14 | Exports 65%+ of revenue | from FY27 onwards | slide 19, lines 507-508 | initiated (raised from 60%+, [MEMORY]; conflicts with C-13) |
| C-15 | Domestic defence serial production "commences" on Indian defence contracts | undated | slide 20, lines 538-544 | underway |
| C-16 | SBTi targets: Scope 1&2 -42%, Scope 3 -25%, 51.1% supplier engagement | FY2030 (base FY2024); approval 15-Sep-2026 | slide 23, lines 588-607 | completed (validation); targets initiated |
| C-17 | Products under development (radars, loitering munition, hollow-core fiber, fuel/pylon tank) | undated | slide 17, lines 455-474 | underway ("UNDER DEVELOPMENT") |
| C-18 | Raw materials "secured" | undated (stated as done) | slide 5, lines 119-120 (PM02) | completed (claimed; terms not given, FN-17) |
| C-19 | Higher value-added products to "aid margins and ease working capital"; high-end OFC and interconnect solutions customised for hyperscalers | undated | slide 19, lines 503-512 (PM05) | underway |
| C-20 | Move to higher value-added offerings in the defence and aerospace value chain | undated | slide 19, lines 514-518 (PM05) | initiated |

## 5. DECK COVERAGE OF THE NOTION CHECKLIST (information for A4; F17 is N.A. on a presentation)

Q1 status comes from [MEMORY]. "Deck Q2" is this document only. The concall and results filing may still cover an item.

| checklist item | Q1 status [MEMORY] | Deck Q2 | ref |
|---|---|---|---|
| Q2 revenue gate (about Rs 2,000 Cr or more) | n/a | ADDRESSED: Rs 2,541.79 Cr, clears the gate | line 119 |
| 1 Hyperscaler pace (export OFC >= Rs 1,800 Cr/q) | RED/SILENT | PARTIAL: exports given as % only ("63%", base period unstated). [DERIVED] Rs 1,601-1,744 Cr total exports in Q2, all products. Export-OFC in Rs not given. | lines 507, 535 |
| 2 Receivables ageing / DSO / unbilled (tripwire #4) | RED | SILENT in narrative; statement cells unresolved | FN-12 |
| 3 Telecom product PBT margin | GREEN | SILENT (no segment data) | n/a |
| 4 Defence delivery (fuze approval, MMHG tender, BMP-2) | SILENT | PARTIAL: MMHG Rs 230 Cr facility; "serial production commences"; no fuze approval stated | lines 436-439, 541 |
| 5 Promoter holding and pledge | GREEN holding / SILENT pledge | Holding 28.29% ADDRESSED; pledge SILENT | line 569 |
| 6-7 BharatNet III revenue, WC, PBT margin | RED / RED | SILENT; only "catering to Domestic telcos and Bharatnet for rapid roll out" and "shifting from low-profit turnkey work" | lines 515, 537-539; FN-21 |
| 8 Mobilisation and LC terms | SILENT | SILENT | n/a |
| 9 Nivetti closure (now 31-Dec-2026) | SILENT | SILENT | n/a |
| EPC losses Rs 80-90 Cr a quarter | n/a | SILENT | n/a |
| CFO / cash conversion (INDETERMINATE) | n/a | SILENT | n/a |
| Capacity Dec-2026 step | undated in Q1 deck | DROPPED (only July-2028 shown) | FN-10 |
| Rs 215 Cr DC-connectivity facility | promise logged | ABSENT | FN-11, FN-19 |
| Preform technology partner (14-Sep watch) | open | "Secured raw materials", no terms | FN-17 |
| HASPL structure / external stake | open | Target unnamed; HASPL glossary-only; strategic options under review | FN-01, FN-13 |

## 6. FLAGS FOR A4 (management questions)

FORWARD-SIGNAL: FN-01, FN-02, FN-03, FN-05, FN-07.
AMBIGUOUS: FN-04, FN-06, FN-08, FN-09, FN-10, FN-11, FN-12, FN-13, FN-14, FN-17, FN-18, FN-19, FN-20, FN-21.
Suggested order for A4:
1. FN-01: strategic options and trigger #6.
2. FN-05 with FN-06 and FN-21: book mix against mix targets, and BharatNet against the turnkey exit.
3. FN-07 with FN-08 and FN-13: defence book and target entity.
4. FN-12: receivables and tripwire #4.
5. FN-02: H2 implied by the guide.
6. FN-17 with FN-18: input security and realisation behind the margin target.
Loop 1 added FN-17 to FN-21. None displaces the top three.

```yaml
stage: A3-forensics
company: "HFCL"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/hfcl-q2fy27/work/forensics_presentation_hfcl_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F7", line: "slide 5, lines 124-129", classification: "FORWARD-SIGNAL", implication: "'evaluating various strategic options' for verticals with distinct working capital profiles; reopens demerger history and trigger #6 (not fired, no structure announced)"}
  - {id: "FN-02", check: "F16", line: "slide 5, lines 111-113", classification: "FORWARD-SIGNAL", implication: "guide hardened to 'now expect' >=80%; implied H2 ~Rs4,452 Cr (~Rs2,226 Cr/q) is below Q2 Rs2,541.79 Cr; floor or H2 step-down"}
  - {id: "FN-03", check: "F16", line: "slide 19, lines 503-504", classification: "FORWARD-SIGNAL", implication: "EBITDA target raised to >27% by FY29 (from 22-25% memory); Q2 25.89% is 111 bps short, preform only by Oct-2028"}
  - {id: "FN-04", check: "F16", line: "slide 5, lines 125-127", classification: "AMBIGUOUS", implication: "EBITDA may include other income (Q1 reported 23.25% vs operating 21.63% memory); verify Q2 operating margin in results filing"}
  - {id: "FN-05", check: "F16", line: "slide 11, lines 302-314; slide 19, lines 507-510; slide 20, line 532", classification: "FORWARD-SIGNAL", implication: "book mix (govt >=35%, non-product >=31.7%, export 57%) runs against revenue mix (8%, ~9%, 63%) and all slide-19 targets; WC intensity may rise"}
  - {id: "FN-06", check: "F14", line: "slide 19, lines 502-504 and 507-508; slide 20, line 532", classification: "AMBIGUOUS", implication: ">70% vs 65%+ FY27 export targets on one slide; >70% needs 77-80% H2 export share; product target ~90% already below ~91% actual"}
  - {id: "FN-07", check: "F16", line: "slide 17, lines 469-470; slide 5, line 123", classification: "FORWARD-SIGNAL", implication: "own defence book ~Rs250 Cr vs Rs500 Cr FY27 aspiration; Rs~1,600 Cr sits in an entity not yet acquired"}
  - {id: "FN-08", check: "F16", line: "slide 17, line 469", classification: "AMBIGUOUS", implication: "defence book down ~Rs450 Cr total, ~Rs400 Cr in target vs Q1 memory; executed, cancelled or redefined"}
  - {id: "FN-09", check: "F16", line: "slide 5, line 114; slide 11, lines 300-314; slide 20, lines 534-536", classification: "AMBIGUOUS", implication: "unclear if 'confirmed' Rs28,911 Cr includes target entity's Rs~1,600 Cr; category split implies Networks <=17.5% vs ~65% Q1 memory"}
  - {id: "FN-10", check: "F16", line: "slide 16, lines 428-434", classification: "AMBIGUOUS", implication: "Dec-2026 interim capacity step absent; OF 'Current' still 28 mn fkm; possible silent fold-in to July-2028"}
  - {id: "FN-11", check: "F16", line: "slide 5, line 118; slide 16, lines 436-442", classification: "AMBIGUOUS", implication: "MMHG Rs230 Cr vs Rs275 Cr memory; Rs215 Cr DC facility absent; deck capex ~Rs2,030 Cr vs ~Rs2,500 Cr broker; no funding split"}
  - {id: "FN-12", check: "F16", line: "slide 20, lines 538-540; slide 19, lines 503-506", classification: "AMBIGUOUS", implication: "two WC claims ('lowering working-capital intensity', 'ease working capital') with no receivables/unbilled/CFO metric; tripwire #4 rests on results filing and concall"}
  - {id: "FN-13", check: "F14", line: "slide 24, line 628; slide 13, lines 366-368; slide 17, lines 470-474", classification: "AMBIGUOUS", implication: "HASPL defined in glossary but unused; acquisition target unnamed, phrased three ways incl. plural 'Acquisitions'"}
  - {id: "FN-14", check: "F10", line: "slide 8, lines 208 and 215; slide 22, line 574", classification: "AMBIGUOUS", implication: "diluted EPS only, no basic (Q1 token 1.49 matches file); 7.5 cr warrants (memory, 4.9% of 153.06 cr shares) unmentioned; spread unreadable"}
  - {id: "FN-15", check: "F14", line: "slide 1, lines 40-41", classification: "NEUTRAL-FACT", implication: "cover letter claims standalone and consolidated; deck is consolidated-only; no disclaimer slide despite hard guidance"}
  - {id: "FN-16", check: "F14", line: "slide 3, lines 80-89; lines 93, 146, 321, 479, 552, 499, 557", classification: "NEUTRAL-FACT", implication: "chapter numbering mismatches contents, duplicate '02', typo; cumulative governance data point"}
  - {id: "FN-17", check: "F6", line: "slide 5, lines 119-120", classification: "AMBIGUOUS", implication: "'Secured raw materials' with no counterparty, tenor, volume or price; captive preform only by Oct-2028, so margin target rests on bought-in input until then"}
  - {id: "FN-18", check: "F16", line: "slide 17, lines 467-471", classification: "AMBIGUOUS", implication: "'higher value realization amid a structural demand upcycle' with no realisation metric; long-term contract priced below spot (memory) may miss the upcycle"}
  - {id: "FN-19", check: "F16", line: "slide 17, lines 467-471", classification: "AMBIGUOUS", implication: "PCS/DC 'high-growth adjacency' with no revenue, book or margin; Rs215 Cr DC facility absent from capex slides"}
  - {id: "FN-20", check: "F14", line: "slide 20, lines 532-533; slide 13, line 347", classification: "AMBIGUOUS", implication: "'#1 in OFC' drops slide 13's 'in India' qualifier; no source or metric; Wi-Fi/UBR share unquantified"}
  - {id: "FN-21", check: "F14", line: "slide 20, lines 537-539; slide 19, lines 514-515", classification: "AMBIGUOUS", implication: "BharatNet roll-out promoted while 'deliberately shifting from low-profit turnkey work'; no BharatNet III revenue, margin or receivables; checklist 6-7 silent at deck level"}
forward_signals: ["FN-01", "FN-02", "FN-03", "FN-05", "FN-07"]
ambiguous: ["FN-04", "FN-06", "FN-08", "FN-09", "FN-10", "FN-11", "FN-12", "FN-13", "FN-14", "FN-17", "FN-18", "FN-19", "FN-20", "FN-21"]
commitments:
  - {commitment: "FY27 revenue growth at least 80% over FY26", implied_date: "FY27", ref: "slide 5, line 111", status_word: "initiated"}
  - {commitment: "Rs10,000 Cr revenue earlier than FY29", implied_date: "before FY29", ref: "slide 5, lines 112-113", status_word: "initiated"}
  - {commitment: "pipeline at advanced stages of conversion", implied_date: "undated", ref: "slide 5, line 115", status_word: "underway"}
  - {commitment: "~Rs1,800 Cr investment in OF, OFC and preform", implied_date: "to Oct-2028", ref: "slide 5, line 118", status_word: "initiated"}
  - {commitment: "FY27 defence revenue ~Rs500 Cr (aspiration)", implied_date: "FY27", ref: "slide 5, line 123", status_word: "initiated"}
  - {commitment: "evaluating strategic options for business verticals", implied_date: "undated", ref: "slide 5, lines 124-129", status_word: "initiated"}
  - {commitment: "OF capacity 28 to 43.1 mn fkm", implied_date: "July 2028", ref: "slide 16, lines 428-434", status_word: "underway"}
  - {commitment: "OFC capacity 39 to 62 mn fkm", implied_date: "July 2028", ref: "slide 16, lines 428-434", status_word: "underway"}
  - {commitment: "preform 600 MT/annum, capex Rs1,250 Cr", implied_date: "October 2028", ref: "slide 16, lines 436-442", status_word: "initiated"}
  - {commitment: "MMHG Phase-1 facility Rs230 Cr, Andhra Ammunition Complex", implied_date: "undated", ref: "slide 16, lines 436-439", status_word: "initiated"}
  - {commitment: "acquire aerospace business (Rs~1,600 Cr export book)", implied_date: "undated in deck", ref: "slide 17, lines 469-474; slide 20, lines 534-536", status_word: "initiated"}
  - {commitment: "EBITDA margin >27% by FY29", implied_date: "FY29", ref: "slide 19, lines 503-504", status_word: "initiated"}
  - {commitment: "~90% product revenue and >70% export revenue", implied_date: "FY27", ref: "slide 19, lines 502-504", status_word: "initiated"}
  - {commitment: "exports 65%+ of revenue", implied_date: "from FY27 onwards", ref: "slide 19, lines 507-508", status_word: "initiated"}
  - {commitment: "domestic defence serial production commences", implied_date: "undated", ref: "slide 20, lines 538-544", status_word: "underway"}
  - {commitment: "SBTi FY2030 targets (Scope 1&2 -42%, Scope 3 -25%, 51.1% suppliers)", implied_date: "FY2030; approved 15-Sep-2026", ref: "slide 23, lines 588-607", status_word: "completed"}
  - {commitment: "new defence and fiber products under development", implied_date: "undated", ref: "slide 17, lines 455-474", status_word: "underway"}
  - {commitment: "raw materials secured (terms not given)", implied_date: "undated, stated as done", ref: "slide 5, lines 119-120", status_word: "completed"}
  - {commitment: "higher value-added products to aid margins and ease WC; high-end OFC and interconnect for hyperscalers", implied_date: "undated", ref: "slide 19, lines 503-512", status_word: "underway"}
  - {commitment: "move to higher value-added defence and aerospace offerings", implied_date: "undated", ref: "slide 19, lines 514-518", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Loudest signal: lines 124-129. Management is 'evaluating various strategic options' because verticals differ in 'working capital profile'. On this name that wording sits on the demerger-flip slip and trigger #6. No structure is announced, so nothing fires, but A4 should make it question one. Second: the order book's own mix runs against all three slide-19 targets under any pairing. Government is at least 35% of the book against 8% of revenue, non-product at least 32% against ~9%, export 57% against 63% now and >70% targeted. Reading A: long-dated O&M/EPC inflates those shares and product orders turn fast. Reading B: revenue mix reverts toward government, EPC and domestic work as BharatNet III executes, and WC intensity rises. Separating observation: order book by execution year. Third: the Rs500 Cr FY27 defence aspiration rests on a ~Rs250 Cr own book; Rs1,600 Cr sits in an entity not yet owned. Cross-quarter diffs use Notion memory, not a prior deck. Loop 1 added FN-17 to FN-21; none displaces the top three."
```
