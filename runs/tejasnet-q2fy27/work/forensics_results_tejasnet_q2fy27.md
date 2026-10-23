# A3 FORENSIC NOTES: Tejas Networks (TEJASNET), Q2 FY27, doctype RESULTS
Inputs read: A1 structured R001-R851 (all), A1 fulltext lines 1-826 (all), A2 ledger (all sections), prior-quarter fulltext Q1 FY27 (all 486 lines), Notion digest sections 4 and 5 only. Source PDF and inputs/ not opened.
Units: Rs crore unless stated. "L###" = line in the Q2 fulltext. "P-L###" = line in the Q1 FY27 prior extract.

## 0. Ledger reconciliation and OCR integrity

Ledger rows read at cited lines: 851 of 851 IDs (100%). Every A2 section (notes, 238 line items, 37 zero rows, agenda, 11 auditor paras, entities, signatures, dates/misc) was checked against the structured file and the fulltext line.

A2 open item resolved: R830 FOOTNOTE_UNRESOLVED. Cons CoM "Refer note- 5" (L539) points to cons note 5, which is the Rs 145.43 Cr CoM charge note (L799). Cons other expenses "Refer note- 6" (L546) points to the warranty note (L802). Cross-references reconcile; no finding.

COLS_PARTIAL (18 rows) resolved by identity, not by estimate:
- R441-R445 (L556, cons remeasurement): the five values map to Q1 FY27, Q2 FY26, H1 FY27, H1 FY26, FY26. The Q2 FY27 cell is unread. TCI identity (L553, L556, L559, L560, L562) gives Q2 FY27 = 1.78 (check: Q1 1.05 + Q2 1.78 = H1 2.83, matches "283").
- R109 (L165, std remeasurement): OCR garbage; std TCI identity gives the same 1.05 / 1.78.
- R132-R134 (L174): reserves line; 2,750.70 is the FY26 audited column only.
- R594 (L686): 0.01 is the H1 FY26 column; H1 FY27 cell reads "é" (nil, consistent with R243 L299).

A1 coverage gaps (lines with financial data but no R-ID; not ledger rows, reported for the record):
- L159 std "(1) Current tax expense/(benefit) : ; 2 é" (nil cells; cons L550 shows nil for the same periods).
- L170 std "Income tax relating to above" on cash flow hedges (nil cells).
- L338 std "Ather finance cast 10.99) {NR" = Other finance cost. Std financing subtotal L339 641.14 requires (0.99) for H1 FY27.

OCR subtotal failures (values NOT corrected; both lines cited):

| # | Failing line | Value read | Check lines | Arithmetic | Status |
|---|---|---|---|---|---|
| O1 | L259 std total equity and liabilities Sep-26 | 3,440.67 | L234 total assets 8,440.67; L239 2,527.57 + L258 5,913.10 | = 8,440.67 | A2 flagged R187/R221 |
| O2 | L535 cons total revenue Q2 FY27 | 205.68 | L533 405.68 + L534 nil; L537 413.45 - L536 7.77 | = 405.68 | A2 flagged R327/R339 |
| O3 | L552 cons total tax FY26 | (945.12) | L550 (0.02) + L551 (445.10); P-L379 (445.12) | = (445.12) | A2 flagged R428/R434 |
| O4 | L160-L161 std deferred/total tax Q2 FY26 | (265.86) | L157 PBT (473.03) less L162 PAT (307.17); cons L552 (165.86) | = (165.86) | NEW, not in A2 |
| O5 | L160 std deferred tax H1 FY27 / L161 total | (238.51) / (238,53) | Q1 (68.57) + Q2 (69.94); DTA L221 365.24 to 503.75; cons L552 (138.53) | = (138.51) | NEW; L160 and L161 also differ by 0.02 with nil current tax |
| O6 | L162 std PAT H1 FY27 | (410.03) | note 4 L794 (410.01); Q1 (202.24) + Q2 (207.77) | = (410.01) | NEW |
| O7 | L790 note-4 std revenue Q2 FY27 | 404.31 | L144 404.91; L144 H1 806.86 - Q1 401.95 | = 404.91 | NEW (OCR or filing typo, see A3-15) |
| O8 | L151 std employee cost H1 FY26 | 123.84 | L156 H1 FY26 total expenses 1,249.27 less other lines | = 183.84 | NEW |
| O9 | L792 note-4 std PBT H1 FY26; L548 cons PBT H1 FY26 | (70.41); (70.34) | L157 (770.41); cons CF L675 (770.34) | leading 7 dropped | NEW |
| O10 | L310 std CF change in other liabilities H1 FY27 | 1,266.32 (no brackets) | L311 CFO (310.58) less other WC lines L301-L309 = (1,266.32); BS L256 1,420.72 to 154.40; cons L697 (1,266.27) | = (1,266.32), a decrease | NEW. A1 header places the sign misread on the consolidated cash flow; arithmetic places it on the standalone line L310. Cons L697 is correct. |
| O11 | L223 std total non-current assets | 2,864.85 / 2,515.19 | sum of L211-L222 = 2,865.85 / 2,516.19 | fails by 1.00 at both dates | NEW. Candidate: std goodwill L213 212.81 vs cons goodwill L599 211.81 |
| O12 | L598 cons ROU Mar-26 | 214.07 | std L212 114.07; cons subtotal L609 2,505.16 ties only with ROU near 114 | fails by about 100 | NEW. Other candidates in the same subtotal: L604 "4.33", L608 "22.15" |
| O13 | L171 std TCI H1 FY27 | (422.15) | Q1 (208.91) + Q2 (203.24) | = (412.15) | NEW |
| O14 | L570 cons diluted EPS Q1 FY27 | (41.37) | L569 basic (11.37); P-L398 (11.37) | (11.37) | NEW, trivial |
| O15 | L563 cons share capital Q2 FY27 | 181,42 | cons BS L623 181.41; std L172 181.41 | 181.41 | NEW, trivial |

Downstream rule: A4 uses the arithmetic column only where it labels the number "derived by identity from L### and L###"; the filed OCR value stays on record as read.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R007, R333 (ZERO_STANDING) | L143, L534 | "(b) Other operating revenue : 0.34 5.15" | AMBIGUOUS | Line is nil in Q2 FY27 vs 0.34 Q1 and 5.15 Q2 FY26. The filing does not name PLI anywhere; if PLI incentive is booked here, no PLI was recognised in Q2. A4 question: where is PLI income booked, and was any claim rejected, deferred or unrecognised in Q2? |
| A3-02 | F1 | R291, R641 (ZERO_STANDING) | L326, L713 | "Dividend paid : (44.15)" | NEUTRAL-FACT | No dividend paid in H1 FY27 against 44.15 in H1 FY26, after the FY26 loss of 916.43 (L162). Cash conservation; no forward action needed. |
| A3-03 | F4 | R713-R718, R826 | L499 | "total revenue of Rs. 3.52 crores and Rs. 4.38 crores, total net profit after tax of Rs. 0.80 crores" | AMBIGUOUS | Unreviewed subsidiaries: revenue 0.86 (P-L327) to 3.52 QoQ (4.1x); NPAT 0.00 to 0.80. Share of consolidated PAT 0.39%, revenue 0.87%, assets 0.26% (below 10% bar). S-vs-C revenue gap is only 0.77, so about 2.75 of the 3.52 appears intra-group [inference]. YoY comparator NOT FOUND. A4 question: what drove the jump, and how much is billed to the parent? |
| A3-04 | F5 | R826-R828, R711-R720 | L496-L505 vs P-L325-P-L331 | "whose financial results reflect total assets of Rs. 21.59 crores and net assets of Rs. 10.90 crores" | NEUTRAL-FACT | Other Matter scope expanded: total assets, net assets and net cash flows (0.89) added; "net loss ... Rs. 0.00" became "net profit ... Rs. 0.80". Same 3 entities, same "not material" representation, conclusion unmodified. Expansion matches the half-year format (balance sheet and cash flow now presented). Report title changed from "Independent Auditors' Review Report on the Statement of Unaudited Standalone Financial Results" (P-L56) to "Review Report" (L60). No Going Concern or EoM either quarter. |
| A3-05 | F8 | R165-R166, R516-R517, R091-R096, R417-R420 | L221, L607, L550-L551 | "Deferred tax assets (net) 503.75 365.24" | FORWARD-SIGNAL | DTA rose 138.51 in H1 (+37.9%), exactly the H1 deferred credit; current tax nil every period. DTA is 19.9% of consolidated equity 2,527.60 (L625); DTA plus intangibles under development (L601 897.75) = 1,401.50 = 55.4% of equity (44.9% at Mar-26). Both are year-end audit judgements (recoverability, impairment). A loss-making year 3 tests DTA recoverability at the FY27 audit; any derecognition hits book value directly. |
| A3-06 | F8 | R085-R102, R411-R434 | L157, L160 (H1 FY26 col); L548, L551 (Q2 FY27 col); P-L169, P-L172 | "(2) Deferred tax expense/{benefit) (69.94) (68.57)" | AMBIGUOUS | Deferred-tax credit rate: H1 FY26 34.96% (269.33 / 770.41), Q2 FY26 35.06% (165.86 by identity, see O4), Q4 FY26 24.12% (69.46 / 287.92, prior extract), Q1 FY27 25.32%, Q2 FY27 25.18%. Step of about 978 bps at Q4 FY26. Reading 1: move to the s.115BAA 25.17% rate. Reading 2: partial non-recognition of DTA on new losses. Separating observation: a regime switch would need a remeasurement charge on the opening DTA (about 100 on 365.24 [inference]); Q4 FY26 shows a credit of 69.46 against 72.47 at 25.17%, so no charge of that size is visible. Each Rs 100 of loss now books 25.17 of DTA, not 34.94. Tax adjustments for earlier years: no line in either statement (NOT FOUND). |
| A3-07 | F9 | R109, R441-R445 | L556, L562 | "en the post-employment benefit obligation nee 1.05 2.23 283 279 159" | NEUTRAL-FACT | Remeasurement gain Q2 FY27 = 1.78 (derived by TCI identity, cell OCR-unread) exceeds full FY26 1.59. H1 FY26 2.79 also exceeded FY26, so H2 FY26 reversed 1.20: a seasonal discount-rate pattern [inference]. Rs amounts immaterial. Verify actuarial assumptions at the FY27 Annual Report. |
| A3-08 | F10 | R126-R146, R474-R497, R540 | L172, L178-L179, L569-L570, L623 | "(1) Basic (11.62) ... (2) Diluted (11.62)" | AMBIGUOUS | Basic = diluted in all periods (loss year, instruments anti-dilutive): spread zero. Paid-up 181.25 to 181.41 in Q2 (+1.6 lakh shares), traced to RSU/ESOP exercise (L325 proceeds 0.84 H1). EPS-implied weighted shares 17.809 Cr (206.94 / 11.62) vs issued 18.141 Cr (181.41 / Rs 10): gap 0.33 Cr shares (1.8%), consistent with shares held by an employee trust [inference]. Spread will open when profit turns positive. A4 question: trust-held share count and the RSU/ESOP overhang. |
| A3-09 | F12 (entity = sole segment, L375) | R175-R176, R215-R216, R251-R252, R263-R266, R601, R613 | L228, L256, L304, L310, L697, L700 | "Other current liabilities 154.40 1,420.72" | AMBIGUOUS | H1: trade receivables fell 1,110.51 (L228) but other current liabilities fell 1,266.32 (L256; CF L697 (1,266.27)). The two net to an outflow of about 168; consolidated CFO stays (311.93) (L700). H1 revenue 806.86 cannot absorb a 1,266 liability as revenue. Reading 1: customer advances set off against billed receivables (non-cash). Reading 2: cash collected and an advance or statutory liability paid out. The filing does not say. A4 question: what made up the 1,420.72 at Mar-26, and was the H1 reduction settled by set-off or by cash? |
| A3-10 | F12 | R153-R156, R504-R507, R273-R274, R623, R061-R066 | L214, L215, L316, L153 | "Other intangible assets 688.10 386.05" | FORWARD-SIGNAL | Other intangibles +302.05 (+78%) while intangibles under development fell 52.68 with H1 spend of 358.59: roughly 411 moved from development into amortising intangibles [inference, cash basis]. D&A is still falling (100.98 Q2 FY26, 94.35 Q1, 91.48 Q2). Expect amortisation to step up from Q3 FY27. A4 question: amount capitalised, products, useful life. |
| A3-11 | F12 | R707-R709, R730-R732, R213-R214, R259 | L381, L255, L308 | "provision for warranty expenses amounting to Rs. 7.24 crore (Rs. 35.11 crore for the quarter ended June 30, 2026" | AMBIGUOUS | Warranty charge fell 79% QoQ on flat revenue: 1.8% of revenue vs 8.7% Q1, 17.0% Q2 FY26, 11.8% Q4 FY26 (39.30, P-L222). Current provisions 158.44 to 139.29. Same basis wording as Q1 ("potential fault rates, repair requirements and anticipated warranty claims"). Reading 1: fault-rate re-estimate. Reading 2: product mix or expiry of warranty periods on earlier shipments. Worth about 27.87 of Q2 PBT at the Q1 rate. |
| A3-12 | F12 | R067-R072, R393-R398, R227 | L154, L545 | "(g) Allowance for expected credit loss (10.55) 8.08 15.58" | AMBIGUOUS | ECL swung from an 8.08 charge (Q1) to a 10.55 write-back (Q2). With A3-11, estimate releases total about 46.50 vs Q1 rates; Q2 PBT loss (277.71) vs Q1 (270.81) would be about (324) at Q1 rates [inference]. A4 question: which receivables drove the write-back, and is it a collection or a model change? |
| A3-13 | F12 | R195-R196, R203-R204, R546-R547, R554-R555, R293-R314, R643-R662 | L243, L249, L327-L332, L336 | "(i) Borrowings 1,162.40 551.83" | CONFIRMATORY-NEGATIVE | Gross borrowings 4,035.47 to 4,835.35 (+799.88). Non-current borrowings 2.1x. Supplier finance proceeds 600.96 to 160.74 (H1 YoY): payables finance replaced by bank debt. Interest on current borrowings 125.92 vs 75.68 H1 FY26 (+66%). Net debt (gross borrowings less cash, current investments and other bank balances, ex-lease) 4,384.39 vs 3,530.67 at Mar-26; 4,518.90 including lease liabilities 134.51. |
| A3-14 | F14 | R818, R843 (note 3 / cons note 5) | L378, L799 vs P-L218, P-L460 | "For the quarter ended September 30, 2025, cost of materials consumed includes a charge of Rs. 145.43 crore" | AMBIGUOUS | Q1 note 3 disclosed the current-quarter inventory obsolescence movement (reversal 3.10, P-L218). Q2 note 3 discloses only the comparative-quarter charge; the current-quarter movement is silent. CoM rose 132.08 to 237.84 on flat revenue, offset by the inventory-change swing (109.05 to (13.70)). A4 question: did Q2 FY27 CoM include any obsolescence charge or reversal? |
| A3-15 | F14 | R677, R692 vs R013, R106 | L790 vs L144; L794 vs L162 | "Revenue from operations 404.31 401.95" | NEUTRAL-FACT | Note 4 summary vs standalone P&L: revenue 404.31 vs 404.91; H1 PAT 410.01 vs 410.03. Arithmetic supports 404.91 and 410.01. OCR or filing typo: cannot separate without the source (A1 domain). |
| A3-16 | F14 | R761, R764 | L484, L763 vs P-L312 | "a) Tejas Communication Pte. Limited, Singapore" | NEUTRAL-FACT | Q1 auditor list read "Tejas Communications Pte. Limited" (P-L312); Q2 auditor list and both notes read "Communication". "Saankhya Labs Inc" (L486) vs "Inc." (L767). Name variants only; no entity change (F15 PASS). |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 18 zero line items reviewed (table below). Material: other operating revenue nil (A3-01), dividend nil (A3-02). Rest are template lines (disposals, deposit withdrawals, ROU additions, OCI tax, interim reserves). |
| F2 Standalone vs consolidated | PASS | PAT gap as % of standalone PAT: Q2 FY27 0.40%, Q1 0.00%, Q2 FY26 0.01%, H1 FY27 0.20%, FY26 0.82%. Largest move under 1 pp, below the 5 pp bar. Decomposition below. |
| F3 Shell-entity detection | PASS | No shells: consolidated employee cost exceeds standalone by 4.30 (Q2, L151 vs L542). D&A identical in all six columns (L153 vs L544), so subsidiaries hold no material depreciable assets. Cons other expenses below standalone by 4.40 (L155 vs L546) and std trade payables exceed cons by 11.07 (L253 vs L639): intra-group recharges eliminated. Captive cost-centre pattern. No Going Concern EoM to reconcile. Subsidiary net assets 10.90 (L498) vs parent investment 10.87 (L217): no impairment indicator. |
| F4 Unaudited contribution | FINDING | 0.39% of consolidated PAT, below 10%. QoQ jump recorded as A3-03; YoY comparator NOT FOUND. |
| F5 Going concern / EoM scope | FINDING | No GC or EoM either quarter. Other Matter scope and wording changed (A3-04), driven by the half-year format. Verbatim diff: P-L325-P-L331 vs L496-L505. |
| F6 Forward-commitment phrases | PASS | Lexicon sweep over L1-L826: zero hits. Matches A1 FORWARD count 0. Commitment register empty. |
| F7 Hedge phrases | PASS | Lexicon sweep: zero hits. Warranty note basis wording unchanged from Q1 (L382 vs P-L222); no new hedge added. |
| F8 Tax forensics | FINDING | Credit rate ~25.2% vs statutory 25.17% in FY27; ~35% in H1 FY26 (A3-06). Persistent deferred credits, zero current tax, DTA build (A3-05). Shield: 2,518 bps of pre-tax loss in Q2 FY27. |
| F9 OCI forensics | FINDING | Q2 actuarial gain 1.78 (derived) > FY26 full-year 1.59 (A3-07). Cash-flow hedge OCI Q1 (7.72), Q2 2.75, under FY26 11.81. |
| F10 Share count and dilution | FINDING | Spread zero; issued vs EPS-implied weighted count gap 0.33 Cr shares (A3-08). |
| F11 Reserves and net worth | PASS | Std 181.41 + 2,346.16 = 2,527.57; cons 181.41 + 2,346.19 = 2,527.60; Mar-26 both tie. Roll-forward: 2,930.87 + TCI (411.28) + share-based payments 4.50 + RSU proceeds 0.84 = 2,524.93 vs 2,527.60. Residual 2.67 (0.1%), below 5%. Candidates: trust share movements, hedge-reserve recycling, RSU reserve transfers. |
| F12 Segment forensics | FINDING | Single reportable segment (L375, L775), so the entity balance sheet is the segment balance sheet. Liability unwind (A3-09), capitalisation (A3-10), warranty (A3-11), ECL (A3-12), debt build (A3-13). |
| F13 Board outcome | PASS | Sole agenda: results (L30-L34). No AR, AGM, dividend, director, auditor, ESOP or capital-raise item; no QIP enabling resolution. Meeting 2h15m (L36) vs 3h10m in Q1 (P-L35). |
| F14 Drafting inconsistencies | FINDING | Note 3 scope switch (A3-14); note 4 vs P&L mismatches (A3-15); entity-name variants and report-title change (A3-16). Note text and letters agree on "review", not "audit" (L33, L60, L407). |
| F15 Entity list diffs | PASS | Holding + 3 subsidiaries, same as Q1 (L482-L486 vs P-L310-P-L314; L763-L767 vs P-L426-P-L429). No addition, deletion or relationship change. Name variants logged under A3-16. |
| F16 Presentation: dropped/reframed | N.A. | Results filing; presentation-specific check. |
| F17 Concall silence audit | N.A. | Results filing; transcript-specific check. Filing-level checklist readout supplied below for A4, not scored. |

### F1 zero-standing item register

| Line item | Lines | Template purpose | Read |
|---|---|---|---|
| Other operating revenue (Q2 FY27) | L143, L534 | Incentives, scrap, export benefits, PLI | A3-01 |
| Income tax on OCI items | L167, L170, L557, L561 | Tax on remeasurement / hedge OCI | Nil all periods: no DTA booked through OCI; DTA build is P&L-only |
| Interim reserves cells | L174, L565 | Reserves shown for audited year only | Template |
| Current tax (cons) | L550 | Current tax charge | Nil FY27; see F8 |
| Profit/proceeds on PPE disposal | L299, L317, L686, L704 | Asset sales | No disposals H1 FY27 |
| Withdrawals of bank deposits | L319, L706 | Deposit maturity | None H1 FY27 |
| Dividend paid | L326, L713 | Distribution | A3-02 |
| Repayment of NC borrowings (H1 FY26 col) | L328 | Term-debt repayment | Now (161.22) in H1 FY27 |
| ROU additions (non-cash) | L345, L732 | New leases | None H1 FY27 |

### F2 decomposition (S = standalone, C = consolidated)

| Period | Rev S | Rev C | Gap | PAT S | PAT C | Gap | Gap % of S PAT |
|---|---|---|---|---|---|---|---|
| Q2 FY27 | 404.91 | 405.68 (L533) | +0.77 | (207.77) | (206.94) | 0.83 | 0.40% |
| Q1 FY27 | 401.95 | 402.16 | +0.21 | (202.24) | (202.24) | 0.00 | 0.00% |
| Q2 FY26 | 261.37 | 261.82 | +0.45 | (307.17) | (307.13) | 0.04 | 0.01% |
| H1 FY27 | 806.86 | 807.84 | +0.98 | (410.01) by identity | (409.18) | 0.83 | 0.20% |
| H1 FY26 | 463.30 | 463.20 | (0.10) | (501.08) | (501.00) | 0.08 | 0.02% |
| FY26 | 1,100.78 | 1,103.28 | +2.50 | (916.43) | (908.89) | 7.54 | 0.82% |

Q2 FY27 gap components: subsidiary revenue 3.52 (L499) less eliminations about 2.75 [inference]; employee cost +4.30; other expenses (4.40); CoM (0.03); finance cost +0.03; PBT gap 0.83 ≈ subsidiary NPAT 0.80. No JV or associate exists.

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| none (zero lexicon hits in L1-L826) | n/a | n/a | n/a |

## 4. Filing-level checklist readout for A4 (supplementary; F17 is N.A. on a results filing; mechanical reads, no RAG verdict)

| Item | Filed number (line) | Note |
|---|---|---|
| #2 revenue run-rate | Cons Q2 405.68 (L533 + L534 nil; L535 OCR fails, O2); Q1 402.16 (L535) | Second quarter above 400 |
| #4 net debt | 4,384.39 ex-lease; 4,518.90 incl. lease (L629, L630, L635, L636, L613, L615, L616) | The ex-lease definition gives Mar-26 3,530.67, which matches the Notion Q1 base (4,277 less 746 = 3,531). Up 107.39 vs Notion Q1 4,277 |
| #6 international mix | NOT FOUND (single segment, L775) | Subsidiary revenue 3.52 (0.87%) is not a proxy |
| #7 BSNL PO | NOT FOUND in filing | Results doctype carries no order disclosure |
| #8 PLI income | Not disclosed; other operating revenue nil Q2 (L534) | A3-01 |
| #9 BV/share | 139.33 on issued 18.141 Cr shares (L625 / L623 at Rs 10, L563); 141.93 on EPS-implied 17.809 Cr | The 140 line sits between the two readings; separating observation = trust-held share count (A3-08). Mar-26 161.92. No QIP in board outcome (L30-L34) |
| #10 finance cost | Cons Q2 86.53 (L543) vs Q1 85.07; std 86.50 vs 85.04 (L152) | +1.46 QoQ (+1.7%) |
| DTA | 503.75 (L607), 19.9% of equity | A3-05 |
| Intangibles under development | 897.75 (L601) vs 950.43 Mar-26 | A3-10 |
| Cash-loss track | H1 FY27 cons CFO (311.93) (L700); FCF after capex and intangibles (709.11) [L700, L702, L703] | |
| Warranty provision | 7.24 (L802) | A3-11 |

```yaml
stage: A3-forensics
company: "TEJASNET"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tejasnet-q2fy27/work/forensics_results_tejasnet_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
  F3: PASS
  F4: FINDING
  F5: FINDING
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "L143, L534", classification: "AMBIGUOUS", implication: "Other operating revenue nil Q2 (0.34 Q1, 5.15 Q2 FY26); if PLI sits here, no PLI recognised in Q2; ask where PLI is booked and claim status"}
  - {id: "A3-02", check: "F1", line: "L326, L713", classification: "NEUTRAL-FACT", implication: "No dividend paid H1 FY27 vs 44.15 H1 FY26 after FY26 loss"}
  - {id: "A3-03", check: "F4", line: "L499 (vs prior P-L327)", classification: "AMBIGUOUS", implication: "Unreviewed subsidiary revenue 0.86 to 3.52 QoQ, NPAT 0.00 to 0.80; 0.39% of PAT; about 2.75 appears intra-group; ask driver and parent billing"}
  - {id: "A3-04", check: "F5", line: "L496-L505 (vs P-L325-P-L331)", classification: "NEUTRAL-FACT", implication: "Other Matter scope expanded to assets, net assets, cash flows (half-year format); same 3 entities; no GC or EoM; report title shortened"}
  - {id: "A3-05", check: "F8", line: "L221, L607, L550-L551", classification: "FORWARD-SIGNAL", implication: "DTA 365.24 to 503.75, P&L credits only, zero current tax; DTA 19.9% of equity, DTA plus IAUD 55.4%; FY27 audit recoverability test can cut book value"}
  - {id: "A3-06", check: "F8", line: "L157, L160, L548, L551; P-L169, P-L172", classification: "AMBIGUOUS", implication: "Deferred credit rate ~35% (H1 FY26) to ~25.2% (FY27), step at Q4 FY26 with no visible remeasurement charge; regime switch vs partial non-recognition; ask"}
  - {id: "A3-07", check: "F9", line: "L556, L562", classification: "NEUTRAL-FACT", implication: "Q2 actuarial gain 1.78 (derived by TCI identity) exceeds FY26 full-year 1.59; immaterial; verify assumptions at FY27 AR"}
  - {id: "A3-08", check: "F10", line: "L172, L569-L570, L623, L325", classification: "AMBIGUOUS", implication: "Basic = diluted (loss); issued 18.141 Cr vs EPS-implied 17.809 Cr shares, gap 0.33 Cr; ask trust-held shares and RSU/ESOP overhang; decides BV/share side of 140"}
  - {id: "A3-09", check: "F12", line: "L228, L256, L304, L310, L697, L700", classification: "AMBIGUOUS", implication: "Receivables fell 1,110.51 but other current liabilities fell 1,266.32; CFO still (311.93); set-off of advances vs cash outflow; ask composition of 1,420.72 and settlement mode"}
  - {id: "A3-10", check: "F12", line: "L214, L215, L316, L153", classification: "FORWARD-SIGNAL", implication: "Other intangibles +302.05, IAUD -52.68 on 358.59 spend; about 411 capitalised into amortising base; D&A step-up from Q3 FY27 while D&A still falling"}
  - {id: "A3-11", check: "F12", line: "L381, L255, L308", classification: "AMBIGUOUS", implication: "Warranty provision 35.11 to 7.24 on flat revenue (1.8% vs 8.7% of revenue); about 27.87 PBT support; fault-rate re-estimate vs mix or warranty expiry; ask"}
  - {id: "A3-12", check: "F12", line: "L154, L545", classification: "AMBIGUOUS", implication: "ECL 8.08 charge to 10.55 write-back; with warranty, about 46.50 of estimate release; Q2 loss near (324) at Q1 rates; ask collection vs model change"}
  - {id: "A3-13", check: "F12", line: "L243, L249, L327-L332, L336", classification: "CONFIRMATORY-NEGATIVE", implication: "Gross borrowings +799.88 to 4,835.35; supplier finance replaced by bank debt; net debt 4,384.39 ex-lease, 4,518.90 incl. lease"}
  - {id: "A3-14", check: "F14", line: "L378, L799 (vs P-L218, P-L460)", classification: "AMBIGUOUS", implication: "Current-quarter inventory obsolescence movement no longer disclosed; note now comparative-only; ask Q2 obsolescence charge or reversal"}
  - {id: "A3-15", check: "F14", line: "L790 vs L144; L794 vs L162", classification: "NEUTRAL-FACT", implication: "Note 4 summary vs P&L: 404.31 vs 404.91, 410.01 vs 410.03; arithmetic supports 404.91 and 410.01; OCR vs typo unresolved"}
  - {id: "A3-16", check: "F14", line: "L484, L763 (vs P-L312); L486 vs L767", classification: "NEUTRAL-FACT", implication: "Subsidiary name variants Communication/Communications and Inc/Inc.; no entity change"}
forward_signals: ["A3-05", "A3-10"]
ambiguous: ["A3-01", "A3-03", "A3-06", "A3-08", "A3-09", "A3-11", "A3-12", "A3-14"]
commitments: []
gate_a3: pass
blank_checks: []
analyst_note: "Q2 loss looks flat QoQ (277.71 vs 270.81), but two estimate releases hold it there. Warranty fell 35.11 to 7.24; ECL went from an 8.08 charge to a 10.55 write-back. At Q1 rates the loss is about 46.5 larger. The 1,110 receivables fall did not reach cash: other current liabilities fell 1,266 in the same half and CFO stayed (311.93). That fits a set-off of advances; the filing is silent. Intangibles rose 302 while IAUD fell 53, so amortisation should rise from Q3. DTA plus IAUD equal 55% of equity, both year-end judgements. BV/share is 139.33 on issued shares, 141.93 on the EPS-implied count; trust-held shares decide which side of 140. Net debt on the Notion Mar-26 definition is 4,384; with leases 4,519. OCR: the other-liabilities sign misread is on standalone L310, not the consolidated line A1 named; std tax L160-L161 misread Q2 FY26 and H1 FY27 by 100. Results doctype has no forward or hedge language (F6, F7 zero hits)."
```
