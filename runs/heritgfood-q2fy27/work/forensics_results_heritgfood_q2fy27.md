# A3 FORENSIC NOTES: results | Heritage Foods Limited (HERITGFOOD) | Q2 FY27

Agent: A3 forensic notes | model: claude-opus-5-5 | date: 2026-10-17
Doctype: results (Board Outcome letter, standalone and consolidated Ind AS results for the quarter and six months ended 30 September 2026, two limited review reports, Annexure 1 entity list)
Inputs read:
- A1 structured: runs/heritgfood-q2fy27/extracted/heritgfood-results-q2fy27-structured.md (R001-R1242, all 1,242 rows read)
- A1 fulltext: runs/heritgfood-q2fy27/extracted/heritgfood-results-q2fy27-fulltext.md (L1-L782, all read)
- A2 ledger: runs/heritgfood-q2fy27/work/ledger_results_heritgfood_q2fy27.md
- Prior-quarter fulltext: NOT AVAILABLE (ND). F5 and F15 are single-period reads; no verbatim diff was possible.
- Notion monitoring checklist: ND (no company page, no spear). PRE-THESIS READ.
Source PDF and inputs/ were not opened.
Units: Rs millions as filed (L71). Percentages and differences below are A3 arithmetic on filed values.

## 1. LEDGER RECONCILIATION

| ledger block | ledger rows | read at cited line | result |
|---|---|---|---|
| Line items L001-L299 (R001-R1114) | 1,114 NUMBER rows | yes, every table line L75-L624 | all values match fulltext |
| Standing zero rows | 60 | yes | itemised under F1 |
| Other NUMBER rows R1115-R1141 | 27 | yes | match |
| Entities R1142-R1169 | 28 | yes | match |
| Dates R1170-R1192 | 23 | yes | match |
| Qualifiers R1193-R1242 | 50 | yes | match; IMAGE_PARTIAL rows R1238-R1241 noted |
| Agenda items | 0 in A1; agenda read at fulltext L35-L46 | yes | results and limited review only |

ids_in_structured 1,242 = ids_referenced_in_ledger 1,242. Rows read 1,242 of 1,242: 100%.

A2 flags resolved by A3:
- R1209/R1228 RESTATED: this is the consolidated note repeating standalone note 4a. It is not a restatement of prior numbers. The consolidated note omits 4b (HNFL impairment) correctly, because the impairment eliminates on consolidation. Tie: standalone FY26 exceptional 95.98 (L89) = 69.33 + 32.02 - 5.37; consolidated FY26 101.35 (L423) = 69.33 + 32.02. Q2 FY26 93.56 = 61.54 + 32.02 in both.
- AUDITOR_SIGNED_BEFORE_BOARD_CONCLUSION: review reports signed 13:04:00 (L380) and 13:05:27 (L742); meeting ran 11:30 to 14:50 (L45-46); CS letter signed 14:59:25 (L55). Information only. See F13.
- R1242 SIGN_CONVENTION: leading minus signs in the consolidated segment FY column (L472-474). See F14-5.
- IMAGE_PARTIAL R1238-R1241: consolidated CF depreciation 539.57 (L570) vs P&L 539.58 (L416); CF interest income (5.06) (L580) vs segment 5.05 (L475). Within blur tolerance; sub-totals tie per A1.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-1 | F1 | R079-R084, R609-R614, R1120-R1122, R1209 | L89, L296-298 | "refund of differential GST liability deposited under protest on the classification of flavoured milk, following a favourable order" | AMBIGUOUS | Exceptional line is dash in Q1 and Q2 FY27 but stays in the template. The note does not say the order is final or name the total amount deposited under protest. Q2 FY26 PBT carried 93.56 of this. Reported standalone PBT falls 35.0% YoY (637.74 to 414.53); pre-exceptional PBT falls 23.8% (544.18 to 414.53). A4: is the order final or under appeal, and is more refund pending? |
| F1-2 | F1 | R055-R060, R366-R371, R1123, R1210, R450-R455, R876-R877 | L85, L225, L299, L254-255, L507 | "a provision of Rs 5.37 million on account of impairment loss provided on investment made in Heritage Novandie Foods Limited" | FORWARD-SIGNAL | Impairment lines are dash in H1 FY27, after FY26 booked 5.37 on HNFL and 6.12 on assets. In H1 FY27 the parent put 72.00 equity and 4.86 loans into subsidiaries. Consolidated goodwill is 71.85, and NCI losses are widening (F2-1). The FY27 year-end impairment test on the HNFL investment and goodwill is a live risk to this line. |
| F1-3 | F1 | R597-R602, R772-R777, R968-R970, R1167 | L421, L772 | "Share of loss of an associate and a joint venture ... - - - -" | NEUTRAL-FACT | The associate SKIL Raigam Power (India) Limited contributes nil in every FY27 period. The only non-nil values (13.12 in 6M FY26 and FY26) date from before the 16 June 2025 HNFL control change. [INFERENCE] The equity-accounted carrying value is likely nil. |
| F2-1 | F2 | R103-R108, R633-R638, R663-R668, R681-R686, R748-R765 | L94, L428, L436, L440, L468-470 | "Loss for the period / year (5.06) (2.48) (0.86)" | FORWARD-SIGNAL | Consolidated-minus-standalone PAT, as % of standalone PAT: 6M FY26 6.24% to 6M FY27 0.98%, a narrowing of 5.26 pp (above the 5 pp threshold). Q2 FY26 5.35% to Q2 FY27 1.12%. Subsidiary operating EBITDA fell from 53.10 to 28.50 YoY. Feed segment result fell from 52.50 to 33.29. Dairy subsidiaries' drag rose from 13.29 to 20.51. NCI loss is 5.9x YoY. Subsidiaries are turning from contributors into drags. A4: ask for profit and loss by subsidiary. |
| F4-1 | F4 | R1131-R1138, R1168, R1233-R1235 | L721-725 | "one subsidiary, which has not been reviewed by their auditors ... net loss after tax of Rs 10.82 million and Rs 11.76 million" | AMBIGUOUS | The unreviewed loss is 3.5% of Q2 consolidated PAT (10.82 / 308.57), below the 10% threshold. Implied Q1 figures: revenue 195.73, loss 0.94. Q2 revenue fell 27% to 142.62 and the loss rose about 11x, so the unreviewed share of PAT rose from about 0.4% to 3.5% in one quarter. The entity is not named. A4: which subsidiary is it, and why did revenue fall and the loss widen in Q2? |
| F8-1 | F8 | R085, R091, R097, R615, R621, R627 | L90, L92-93, L424, L426-427 | "a. Current tax expense 104.00 ... b. Deferred tax expense 13.42" | AMBIGUOUS | Q2 FY27 ETR: consolidated 27.56% (117.42 / 425.99) and standalone 26.39% (109.38 / 414.53), against 25.17% statutory. Standalone ETR was 24.59% in Q1 FY27 and 24.10% in Q2 FY26. Tax on the subsidiary increment: 8.04 on 11.46 PBT (70%), against 35% in Q2 FY26. [INFERENCE] Loss-making subsidiaries recognise no tax shield while the feed subsidiary pays tax. Deferred tax is an expense in every period: there is no DTA credit shield and no ETR step-up risk from that side. A4: what lifts the standalone Q2 ETR above statutory, and do subsidiaries carry unrecognised losses? |
| F9-1 | F9 | R109-R114, R639-R644 | L97, L431 | "(i) Re-measurement loss on defined benefit plan, net of tax 0.44 0.44 (3.13) 0.88 (6.27) 1.76" | NEUTRAL-FACT | The YoY single-quarter swing ((3.13) to 0.44, 3.57) is larger than the FY26 full-year figure (1.76). Q1 and Q2 FY27 are each 0.44, exactly 1.76 / 4, so FY27 quarters book the FY26 actuarial result pro rata with no interim revaluation. H2 FY26 implied +8.03 after H1 (6.27): an assumption change near March 2026. The amounts are immaterial (0.1% of PAT). Check the discount-rate assumption in the FY27 Annual Report. Not for A4. |
| F12-1 | F12 | R176, R178, R224, R226, R248, R250, R276-R277, R043, R045, R324-R325, R340-R341 | L125, L134, L139, L158, L83 | "(c) Capital work-in-progress 1,275.79 466.13" | FORWARD-SIGNAL | Standalone Dairy segment YoY: assets +34.4% (11,471.15 to 15,413.37), liabilities +39.4% (5,560.53 to 7,754.16), result -27.7% (634.42 to 458.58), margin 5.82% to 3.60%. CWIP rose 174% in six months (466.13 to 1,275.79) and no note names the project or a commissioning date. Finance cost rose 105% YoY (35.82 to 73.37). Gross borrowings rose from 3,241.34 to 3,416.95. Unallocated segment liabilities (382.03) equal DTL (382.03, L193), so all borrowings sit in Dairy liabilities. This is a debt-funded build ahead of earnings. Depreciation and interest step up again when the CWIP capitalises. A4: what is the project, its total cost and its COD? |
| F12-2 | F12 | R724-R729, R760-R765, R820-R825, R850-R855, R164-R169, R736-R741 | L463, L470, L465, L122 | "c. Feed 852.50 728.67 581.12" | AMBIGUOUS | Feed revenue +46.7% YoY. Feed result -36.6% (52.50 to 33.29). Feed margin 9.03% to 3.91% (Q1 FY27 2.29%; 6M 10.60% to 3.16%). Consolidated inter-segment revenue minus standalone inter-segment revenue rose from 369.54 to 546.97 (+177.43), against feed revenue growth of +271.38. [INFERENCE] Much of the feed growth may be intra-group and eliminated, not external. The filing does not split it. A4: what is external feed revenue, and is the margin loss from price or from input cost? |
| F12-3 | F12 | R248-R249, R429, R432, R328-R329, R336-R337, R348-R351 | L139, L246-247, L190, L194, L202-203 | "Changes in other financial liabilities 270.11" | AMBIGUOUS | Dairy segment liabilities fell 323.52 QoQ (8,077.68 to 7,754.16). This could be working-capital unwind or debt reduction. Standalone cash flow vs balance sheet: other financial liabilities add +270.11 in the CF (L246) but fell 148.12 on the BS (L190, L202). Other liabilities show (93.26) in the CF (L247) but rose 80.04 on the BS (L194, L203). Trade payables, inventories and receivables all tie exactly. Candidate reconciling items: capital creditors moved to investing, a reclassification of non-current other liabilities (+86.65), and grant or deposit movements. A4: what are the non-current other liabilities of 196.25, and how did capital creditors move? |
| F14-1 | F14 | R109-R120, R639-R650, R669-R674 | L97-98, L431-432, L437 | "(ii) Net loss / (gain) on fair value through OCI equity securities (0.07)" | NEUTRAL-FACT | The OCI caption signs are inverted. The "loss" rows show positive values that add to TCI (305.15 + 0.44 - 0.07 = 305.52). The "Net loss / (gain)" row shows (0.07), which reduces TCI, so it is a loss, not a gain. The amounts are immaterial. This is a drafting-quality data point. |
| F14-2 | F14 | R453, R284-R285, R369-R370, R450, R286-R287, R306-R307 | L255, L163, L225 | "Investment in a subsidiaries (72.00)" | AMBIGUOUS | H1 FY27 standalone cash out to subsidiary equity was 72.00, but the BS line "Investment in subsidiary, joint venture and associate" rose only 0.50 (660.94 to 661.44). Impairment on investments is dash (L225). About 71.50 cannot be traced on the face of the statements. Candidate items: share application money held in other non-current or financial assets (other non-current financial assets +17.25), an impairment netted elsewhere, or a capital reduction. A4: where is the 72.00 carried, and which subsidiary received it? |
| F14-3 | F14 | R1046-R1048, R453-R455 | L600, L255 | "Investment in a Subsidiaries - 85.00 (162.23)" | AMBIGUOUS | Consolidated CF 6M FY26 shows +85.00 (an inflow) where standalone shows (85.00), and FY26 shows (162.23) against standalone (175.00). Intra-group equity should eliminate to nil, as it does in H1 FY27. [INFERENCE] The 6M FY26 figure likely nets cash acquired on the 16 June 2025 HNFL control change. Low materiality. A4 may confirm. |
| F14-4 | F14 | R790-R795, R206-R211 | L475, L130 | "Add: i. Interest income (0.89) 5.94 1.60 5.05" | AMBIGUOUS | Consolidated Q2 FY27 interest income is negative (0.89), while standalone is +2.00. [INFERENCE] This implies a reversal of about 2.89 at subsidiary or elimination level, possibly a catch-up elimination of intra-group interest on loans to subsidiaries. Amount is small, but negative interest income needs an explanation. |
| F14-5 | F14 | R1209, R1227-R1228, R1242, R591-R620, R778-R783, R043-R048, R194-R199, R1168, R1167 | L296, L293, L639, L642, L422, L424, L421, L771-772, L472-474, L473 vs L415, L128 vs L83, L721 | "30 September 22025" | NEUTRAL-FACT | Cumulative drafting defects: "quatter" (L296); "Decesion" (L293, L639); "22025" (L642). Two captions read "Profit before tax" (L422, L424); the first sits before exceptional items. The caption says "associate and a joint venture" (L421) but Annexure 1 lists no JV (L771-772). The FY column uses leading minus signs (L472-474). Finance cost 38.42 (segment, L473) vs 38.41 (P&L, L415). 165.90 (L128) vs 165.89 (L83). The unreviewed subsidiary is not named (L721). Each item is immaterial. Together they are a governance data point on filing care. |
| F15-1 | F15 | R1155, R1162, R1165, R1188, R1229 | L300, L645, L768 | "Heritage Novandie Foods Limited ('HNFL') (formerly Heritage Novandie Foods Private Limited)" | AMBIGUOUS | Two relationship or identity changes appear in this filing: (a) HNFL converted from a private company to a public company; (b) HNFL moved from JV to subsidiary effective 16 June 2025 (note 5). The prior-quarter list is ND, so A3 cannot say which change is new this quarter. [INFERENCE] Conversion to a public company often comes before a new equity round or a wider shareholder base. A4: why convert, and is a stake change or fund raise planned at HNFL? |

## 3. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | 60 standing-zero rows read. The exceptional, impairment and associate-share lines carry live transaction classes (F1-1, F1-2, F1-3). OCI reclassifiable, consolidated deposits up to 3 months and consolidated provision for doubtful advances are template-only. |
| F2 | FINDING | S-vs-C PAT gap narrowed 5.26 pp (6M) and 4.23 pp (Q2). Decomposition in section 5 (F2-1). |
| F3 | PASS | Subsidiary cost lines are non-trivial in aggregate (Q2 employee cost gap 54.69, depreciation gap 17.29, material cost gap 488.40). No shell signal at aggregate level. Individual entities cannot be separated from the filing. No Going Concern EoM to reconcile. |
| F4 | FINDING | Unreviewed subsidiary is 3.5% of Q2 PAT (below 10%), but it jumped from about 0.4% in implied Q1. Prior-year Other Matter is ND (F4-1). |
| F5 | PASS | No Going Concern or EoM paragraph. Both conclusions are unmodified (L364-369, L713-719, L732). The only scope item is the Other Matter on one unreviewed subsidiary (L721-733). Prior-quarter paragraph is ND, so no verbatim diff was possible. |
| F6 | PASS | Lexicon run on the full fulltext. Hits are only "commenced" (board meeting time, L45) and the template caption "will be reclassified" (L99, L433). Zero management commitments in the notes. |
| F7 | PASS | Hedge lexicon run. Zero hits. The "potential interest obligations" in note 4a (L298) describes a reversed accrual, not a hedge. |
| F8 | FINDING | Q2 ETR is 27.56% consolidated and 26.39% standalone, above 25.17% statutory. Subsidiary increment taxed at 70%. Deferred tax is an expense in all periods. No earlier-year tax line (F8-1). |
| F9 | FINDING | YoY quarterly swing of 3.57 exceeds the FY26 full-year 1.76. FY27 quarters book 1.76/4 pro rata. Immaterial; verify at AR (F9-1). |
| F10 | PASS | Paid-up capital is 463.98 in all six periods (L101, L443) = 92.796m shares at Rs 5. Basic = diluted (single row, L104, L446), so the spread is 0. EPS ties: 305.15 / 92.796 = 3.29; 313.63 / 92.796 = 3.38. Dividend 231.99 = Rs 2.50 x 92.796m. |
| F11 | PASS | Standalone: 463.98 + 10,495.76 = 10,959.74. Roll-forward 10,174.04 + 553.71 - 231.99 = 10,495.76 exact. Consolidated: 463.98 + 10,903.89 = 11,367.87, + NCI 40.39 = 11,408.26. Roll-forward 10,569.23 + 566.65 - 231.99 = 10,903.89 exact. NCI 47.93 - 7.54 = 40.39. No third-party number in the document. Gap 0%. |
| F12 | FINDING | Dairy build: assets +34% and result -28% YoY, CWIP up 174% (F12-1). Feed margin compression with rising intra-group share (F12-2). Dairy liabilities fell QoQ and the CF/BS liability lines do not tie (F12-3). Renewable energy is stable: 94% captive (37.14 of 39.67 is inter-segment, L120/L122) and assets decline with depreciation only. |
| F13 | PASS | Agenda (L35-46) holds only (1) the unaudited results and (2) the limited review report. No AR, AGM, record date, dividend, fund raise or director item. Review reports were signed at 13:04 and 13:05, during the 11:30 to 14:50 meeting. Information only. |
| F14 | FINDING | OCI sign labels (F14-1). CF-to-BS subsidiary investment gap (F14-2). Consolidated CF investment sign (F14-3). Negative interest income (F14-4). Cumulative typos and caption defects (F14-5). Note language ("unaudited", "reviewed") matches the auditor letter (SRE 2410 review). |
| F15 | FINDING | Annexure 1 (L766-772): 3 subsidiaries and 1 associate. HNFL name change (Private to public) and JV-to-subsidiary note (F15-1). Prior list is ND, so no add/delete diff was possible. |
| F16 | N.A. | Results filing; presentation-only check. |
| F17 | N.A. | Results filing; concall-only check. No Notion checklist exists (PRE-THESIS). |

GATE A3: 17 of 17 checks marked. No blanks. gate_a3 = pass.

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| none found: the filing holds zero forward-commitment language in its notes | n/a | lexicon run over L1-L782 | n/a |

Silent items that would normally carry a commitment (for A4, not commitments):
- CWIP of 1,275.79 (L158): no project name, cost or COD in any note.
- GST flavoured milk matter (L296-298): no statement of finality or appeal status.

## 5. F2 DECOMPOSITION (A3 arithmetic on filed values, Rs m)

Gap = consolidated minus standalone.

| period | Revenue gap | % of S rev | Op. EBITDA S | Op. EBITDA C | EBITDA gap | PAT S | PAT C (total) | PAT gap | % of S PAT | PAT C owners | owners gap % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q2 FY27 | 462.04 | 3.63% | 711.17 | 739.67 | 28.50 | 305.15 | 308.57 | 3.42 | 1.12% | 313.63 | 2.78% |
| Q1 FY27 | 463.40 | 3.59% | 594.02 | 618.63 | 24.61 | 247.70 | 249.71 | 2.01 | 0.81% | 252.19 | 1.81% |
| Q2 FY26 | 221.03 | 2.03% | 718.78 | 771.88 | 53.10 | 484.04 | 509.95 | 25.91 | 5.35% | 510.81 | 5.53% |
| 6M FY27 | 925.44 | 3.61% | 1,305.21 | 1,358.29 | 53.08 | 552.86 | 558.26 | 5.40 | 0.98% | 565.80 | 2.34% |
| 6M FY26 | 399.18 | 1.81% | 1,393.85 | 1,510.75 | 116.90 | 861.62 | 915.41 | 53.79 | 6.24% | 916.53 | 6.37% |
| FY26 | 1,109.26 | 2.51% | 2,461.99 | 2,668.82 | 206.83 | 1,397.01 | 1,501.38 | 104.37 | 7.47% | 1,505.21 | 7.75% |

Operating EBITDA = revenue from operations minus (total expenses minus finance costs, D&A and impairment). Other income is excluded.

PBT gap bridge, Q2 FY27 (11.46) vs Q2 FY26 (39.86), from segment tables L125-131 and L468-476:

| component | Q2 FY27 | Q2 FY26 |
|---|---|---|
| Feed segment result (subsidiary) | +33.29 | +52.50 |
| Dairy: consolidated minus standalone result (dairy subsidiaries) | -20.51 | -13.29 |
| Finance cost difference | +0.73 | -2.60 |
| Other un-allocable expenses difference | -3.37 | +1.29 |
| Interest income difference | -2.89 | +0.21 |
| Other un-allocable income difference | +4.21 | +1.75 |
| JV / associate share | 0.00 | 0.00 |
| Total = PBT gap | 11.46 | 39.86 |

Eliminations visible on the face of the statements: purchases of stock-in-trade are lower in consolidated (326.12 vs 570.60, L80/L412), so the parent buys goods from its subsidiaries. Other income is lower in consolidated (33.66 vs 34.14), from eliminated intra-group interest, guarantee income and rent. Investment property is 16.04 consolidated vs 39.34 standalone (L159/L506), so the parent leases property to its subsidiaries.

## 6. ITEMS FLAGGED FOR A4 (management questions)

FORWARD-SIGNAL: F1-2, F2-1, F12-1.
AMBIGUOUS: F1-1, F4-1, F8-1, F12-2, F12-3, F14-2, F14-3, F14-4, F15-1.

```yaml
stage: A3-forensics
company: "HERITGFOOD"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/heritgfood-q2fy27/work/forensics_results_heritgfood_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-1", check: "F1", line: "L89, L296-298", classification: "AMBIGUOUS", implication: "GST flavoured-milk refund 'following a favourable order'; finality and total deposit not stated; Q2 FY26 PBT held 93.56 exceptional, so reported PBT -35.0% YoY vs -23.8% pre-exceptional"}
  - {id: "F1-2", check: "F1", line: "L85, L225, L299, L254-255, L507", classification: "FORWARD-SIGNAL", implication: "FY26 booked 5.37 HNFL investment impairment; parent funded subsidiaries 72.00 equity + 4.86 loans in H1 FY27; goodwill 71.85; NCI losses widening; FY27 year-end impairment risk"}
  - {id: "F1-3", check: "F1", line: "L421, L772", classification: "NEUTRAL-FACT", implication: "Associate SKIL Raigam Power contributes nil in all FY27 periods; carrying value likely nil [INFERENCE]"}
  - {id: "F2-1", check: "F2", line: "L94, L428, L436, L440, L468-470", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap narrowed 6.24% to 0.98% of standalone PAT (6M, 5.26 pp); subsidiary EBITDA 53.10 to 28.50 YoY; feed result 52.50 to 33.29; dairy subsidiary drag 13.29 to 20.51; NCI loss 0.86 to 5.06"}
  - {id: "F4-1", check: "F4", line: "L721-725", classification: "AMBIGUOUS", implication: "Unreviewed unnamed subsidiary: Q2 loss 10.82 (3.5% of PAT) vs implied Q1 loss 0.94; revenue 195.73 to 142.62 QoQ"}
  - {id: "F8-1", check: "F8", line: "L90, L92-93, L424, L426-427", classification: "AMBIGUOUS", implication: "Q2 ETR consolidated 27.56%, standalone 26.39% vs 25.17%; standalone up from 24.59% in Q1; subsidiary increment taxed at 70%; deferred tax an expense in all periods, no DTA shield"}
  - {id: "F9-1", check: "F9", line: "L97, L431", classification: "NEUTRAL-FACT", implication: "YoY quarterly OCI swing 3.57 exceeds FY26 full-year 1.76; FY27 quarters book 1.76/4 pro rata; immaterial; verify actuarial assumptions at FY27 AR"}
  - {id: "F12-1", check: "F12", line: "L125, L134, L139, L158, L83", classification: "FORWARD-SIGNAL", implication: "Dairy assets +34.4% and liabilities +39.4% YoY, result -27.7%, margin 5.82% to 3.60%; CWIP 466.13 to 1,275.79 with no project note; finance cost +105% YoY; depreciation and interest step up at capitalisation"}
  - {id: "F12-2", check: "F12", line: "L463, L470, L465, L122", classification: "AMBIGUOUS", implication: "Feed revenue +46.7% but result -36.6%, margin 9.03% to 3.91%; extra consolidated inter-segment revenue +177.43 vs feed growth +271.38, so growth may be mostly intra-group [INFERENCE]"}
  - {id: "F12-3", check: "F12", line: "L139, L246-247, L190, L194, L202-203", classification: "AMBIGUOUS", implication: "Dairy liabilities -323.52 QoQ; CF other financial liabilities +270.11 vs BS -148.12; CF other liabilities (93.26) vs BS +80.04; trade lines tie"}
  - {id: "F14-1", check: "F14", line: "L97-98, L431-432, L437", classification: "NEUTRAL-FACT", implication: "OCI caption signs inverted vs TCI arithmetic; drafting quality"}
  - {id: "F14-2", check: "F14", line: "L255, L163, L225", classification: "AMBIGUOUS", implication: "Standalone CF (72.00) investment in subsidiaries vs BS investment +0.50 and nil impairment; about 71.50 untraced on the face of the statements"}
  - {id: "F14-3", check: "F14", line: "L600, L255", classification: "AMBIGUOUS", implication: "Consolidated CF investment in subsidiaries +85.00 in 6M FY26 vs standalone (85.00); likely net cash acquired on HNFL control [INFERENCE]; low materiality"}
  - {id: "F14-4", check: "F14", line: "L475, L130", classification: "AMBIGUOUS", implication: "Consolidated Q2 interest income (0.89) vs standalone +2.00; implies a reversal of about 2.89 at subsidiary or elimination level"}
  - {id: "F14-5", check: "F14", line: "L296, L293, L639, L642, L421-424, L472-474, L473, L128, L721", classification: "NEUTRAL-FACT", implication: "Cumulative typos ('quatter', 'Decesion', '22025'), duplicate PBT caption, JV caption with no JV listed, mixed sign convention, 0.01 cross-table mismatches, unreviewed subsidiary unnamed"}
  - {id: "F15-1", check: "F15", line: "L300, L645, L768", classification: "AMBIGUOUS", implication: "HNFL converted from Private to public company and moved from JV to subsidiary (16 Jun 2025); conversion may come before a stake change or fund raise [INFERENCE]; prior list ND"}
forward_signals: ["F1-2", "F2-1", "F12-1"]
ambiguous: ["F1-1", "F4-1", "F8-1", "F12-2", "F12-3", "F14-2", "F14-3", "F14-4", "F15-1"]
commitments: []
gate_a3: pass
blank_checks: []
analyst_note: "This is a pre-thesis read. No prior-quarter extract was available, so the F5 and F15 diffs are single-period only. The filing holds no forward language, so the forward content sits in the numbers. Three threads matter. One: standalone Dairy added Rs 3,942m of assets YoY (+34%) while its result fell 28%. CWIP nearly tripled in six months, and no note names the project. Finance cost doubled. The commissioning date sets when depreciation and interest step up again. Two: subsidiaries are turning from contributors into drags. Feed margin fell from 9.0% to 3.9%. Dairy subsidiaries lost Rs 20.5m. The NCI loss rose about 6x. The unreviewed subsidiary went from a Rs 0.9m loss in Q1 to a Rs 10.8m loss in Q2. The parent keeps funding them (Rs 76.9m in H1), but the investment carrying value rose only Rs 0.5m. Either the money sits on another line or an impairment is building. FY26 already booked Rs 5.37m on HNFL, and goodwill is Rs 71.85m. Three: the YoY PAT fall overstates the operating decline, because Q2 FY26 included a Rs 93.56m GST exceptional."
```
