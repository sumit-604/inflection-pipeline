# A3 FORENSIC NOTES: Knack Packaging Limited (KNACK) q2fy27 | doctype: results

Source inputs (A1/A2 only; no PDF, nothing under inputs/ opened):
- Structured: runs/knack-q2fy27/extracted/knack-results-q2fy27-structured.md (R001-R921, all read)
- Fulltext: runs/knack-q2fy27/extracted/knack-results-q2fy27-fulltext.md (lines 1-1030, all read)
- Ledger: runs/knack-q2fy27/work/ledger_results_knack_q2fy27.md (921 IDs + M1 at line 79, all read at cited lines)
- Prior extract: none (first quarterly review). Auditor-paragraph and entity diffs run against comparatives inside this filing; marked "no prior extract".
- Units: Rs million (x0.1 to Rs Cr). The press release exists only as Annexure B (pp17-19, lines 754-899) and is treated inside this document.

Ledger reconciliation: 921 of 921 structured IDs plus ledger-added row M1 read at their lines. A2 cross-refs verified: JV share 26.15 ties the CON P&L line 542 to the auditor para 6 at line 498; JV H1 loss 60.60 ties line 542 to line 841; press-table figures tie to the CON P&L (lines 817-821 vs 526-548); IPO table p9 = p16 = Annexure C. One A2 entry is out of A3 scope: the R730 DIN OCR (line 1021 stamp "08380254" vs line 1027 "06380254"). It is an OCR artefact, not a source inconsistency. ledger_reconciled_pct = 100.

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| R-A3-01 | F1 | R496, R497, R413-R416 | 577, 542 | "(d) Investments accounted for using equity method \| - \| 34.55" | FORWARD-SIGNAL | JV equity-method carrying value is exhausted. H1FY27 group share of loss is 60.60 against an opening carrying value of 34.55, so 26.05 was recognised beyond the carrying value. Under Ind AS 28 that needs a legal or constructive obligation, or long-term interests (loans) that absorb losses. The group is therefore funding the JV beyond its USD 0.5M commitment (line 369). From Q3, every rupee of JV loss hits consolidated PAT with no equity cushion and likely needs cash. |
| R-A3-02 | F1 | R075-R080, R401-R406, R790, R791 | 200, 540, 355-357 | "would provide appropriate accounting effects on the basis of such developments as needed" | FORWARD-SIGNAL | The "Impact of Labour Codes" exceptional line stays in the template, nil in all five interim columns and 10.77 in FY26. The line anticipates a second past-service-cost charge when Central/State rules are finalised. Size and date are not given. Low materiality (10.77 = 0.9% of FY26 SA PBT). |
| R-A3-03 | F2 | R105-R110, R443-R448, R413-R418 | 206, 548, 542 | "Share of profit/(loss) of joint venture, net of tax \| (26.15) \| (34.45) \| (1.78)" | FORWARD-SIGNAL | CON minus SA PAT is -8.24 in Q2FY27 (-3.19% of SA PAT), -9.78 in Q1FY27 (-3.10%), +2.40 in Q2FY26 (+1.18%), -18.01 in H1FY27 (-3.14%), +10.81 in H1FY26 (+2.69%) and +33.03 in FY26 (+3.69%). The H1 swing is 5.83pp (above the 5pp threshold) and FY26 to Q2FY27 is 6.88pp. Q2FY27 decomposition: subsidiary PAT +15.58 (line 491), eliminations/adjustments +2.33, JV -26.15. Revenue gap 50.10 (1.73% of SA) vs subsidiary revenue 122.33, so about 72 of subsidiary revenue is intra-group. Consolidation now subtracts value, and the JV is the only driver. |
| R-A3-04 | F2 | R253, R599, R170-R171, R514-R515, R158, R502 | 307, 651, 244, 587, 237, 580 | "Loan (given) / received back (net) \| (138.29)" (CON) vs "(124.49)" (SA) | AMBIGUOUS | CON loans given exceed SA by 13.80. CON other non-current assets are 18.21 below SA at 30-Sep-2026 (493.33 vs 511.54) after being equal at 31-Mar-2026 (402.53). SA "Loans" fell from 56.52 to 16.94 although 124.49 net was lent in H1. About 164 left the current Loans line for another line. Counterparty not disclosed. These consolidation residues fit intra-group or JV funding. Question: who received the 124.49, and is any of it a long-term interest in Sayem Knack? |
| R-A3-05 | F3 | R027, R347, R353, R320-R322 | 191, 530, 531, 490-491 | "Cost of materials consumed \| 1,912.38" (identical SA and CON, all six periods) | AMBIGUOUS | Cost of materials is identical in every period, and "Purchase of stock-in-trade" (16.91) appears only in CON. The South African subsidiary does no manufacturing. It is a trading/distribution arm, not a shell: revenue 122.33, PAT 15.58. Subsidiary PAT margin is 12.7% vs parent SA 8.9% (258.44/2,897.47). There is no going-concern language. Question: transfer-pricing basis on parent-to-subsidiary sales (about 72 eliminated per quarter). |
| R-A3-06 | F4 | R320-R325, R756, R876, R877 | 489-503 | "We did not review the interim financial results of the subsidiary ... reviewed by another auditor" | AMBIGUOUS | Amounts not reviewed by Talati in Q2FY27: subsidiary PAT 15.58 plus JV share (26.15). The gross absolute total is 41.73, which is 16.7% of CON PAT 250.20, above the 10% threshold. The net figure is -10.57 (4.2%). Neither other auditor is named (lines 493, 500); both reports were "furnished to us by the Management". Subsidiary figures are given for the quarter only, so the H1 ratio cannot be computed. |
| R-A3-07 | F4 | R324, R413, R414, R415 | 498, 542 | "Group's share of net loss of 26.15 million" | FORWARD-SIGNAL | The unreviewed JV share rose from 1.78 (Q2FY26) to 34.45 (Q1FY27) and 26.15 (Q2FY27), a 14.7x YoY jump. The fastest-growing P&L drag rests entirely on an unnamed auditor's review. |
| R-A3-08 | F4 | R851, R873, R871, R897 | 127-129, 434-436, 381-383 | "have been approved by the Board of Directors, but have not been subjected to review" | NEUTRAL-FACT | The whole Q2FY26 and H1FY26 comparative columns are unreviewed because the company was unlisted. The 52.52% headline revenue growth (line 805) and every YoY ratio rest on unreviewed bases. The same caveat should recur for Q3FY26 and Q4FY26 comparatives through Q4FY27. |
| R-A3-09 | F6 | R792, R795, R796, R841 | 835-839, 856-860 | "customer pricing revisions ... are currently underway, with adjustments expected to reflect in realizations from Q3 FY27 onwards" vs "we implemented customer price revisions over past few months. The benefits of the same are likely to materialise over next few quarters." | FORWARD-SIGNAL | The same press release dates the pass-through two ways. The status word is "underway" in the narrative and "implemented" in the CMD quote. Timing is "from Q3 FY27" in the narrative and "next few quarters" in the CMD quote. Baseline to test in Q3: CON gross margin (COMC + stock-in-trade + inventory change, lines 530-532) was 34.64% in Q2FY27, 42.07% in Q1FY27 and 41.15% in Q2FY26. Q1's large FG/WIP build (316.12, line 532) flattered Q1. Q2 drew no inventory cushion (2.69). |
| R-A3-10 | F6 | R793, R794, R905, R709 | 841-847 | "as JV operations reach breakeven, this drag reverses and PAT margin recovers fully" | AMBIGUOUS | The commitment is undated. The arithmetic does not support "recovers fully". On the press release's own total-income basis, Q2 PAT margin excluding JV is 9.08% ((250.20+26.15)/3,044.61) vs 10.43% excluding JV in Q2FY26 (reported 10.34%). The incremental JV drag explains about 77bp of the 212bp margin decline. The Q2 JV loss is 10.5% of CON PAT, so "slightly impacted" (line 841) understates it. The text uses the H1 loss (60.60) to explain a Q2 margin. "Zero revenue offset today" (line 845) means the JV has no revenue. |
| R-A3-11 | F6 | R299-R303, R720, R920, R799, R015, R251, R219 | 404, 957-971, 188, 306, 288 | "The funds will be utilised progressively as the project progresses" / "The Project has recently commenced" | FORWARD-SIGNAL | Borisana capex has used 7.04 of 3,200.00 (0.22%), with no milestone or date. Unutilised proceeds sit in FDs (2,643.41, line 306) and cash. SA other income was 95.68 in Q2 (22.81 in Q1), which is 28.7% of SA PBT. H1 interest income was 61.33 (line 288). SA PBT excluding other income was 237.29 vs 210.88 in Q2FY26 (+12.5%) and 396.30 in Q1FY27 (-40.1% QoQ). Other income decays as capex draws down the FDs, so reported PBT growth overstates core growth. |
| R-A3-12 | F6 | R304-R308, R724, R267, R253 | 405, 315, 307 | "2. General Corporate Purposes \| 311.49 \| - \| 294.69 \| 294.69 \| 16.80" | AMBIGUOUS | 94.6% of the GCP allocation was spent in the first quarter after listing. In the same half, short-term borrowings rose 81.01 and net loans given were 124.49. The use of GCP is not described. Question: what did the 294.69 fund? |
| R-A3-13 | F7 | R792, R796, R910 | 839, 859-860 | "subject market stabilization" / "likely to materialise over next few quarters" | FORWARD-SIGNAL | A market-condition escape clause is attached to the only margin-recovery promise. With the "next few quarters" softener in the CMD quote, a Q3FY27 miss is pre-excused. The safe harbour (lines 880-888) is boilerplate and not counted. |
| R-A3-14 | F8 | R093-R104, R156-R157, R190-R191, R431-R442 | 204-205, 236, 258, 546 | "(b) Deferred Tax \| (5.80) \| 2.46 \| 6.53" | AMBIGUOUS | SA deferred tax turned to a credit in Q2 (5.80) after charges in Q1 (+2.46), Q2FY26 (+6.53) and FY26 (+28.56). SA ETR: Q2FY27 22.38%, Q1 24.83%, Q2FY26 25.89%, FY26 25.72%. Q2 is 279bp below the 25.17% statutory rate, and the deferred-tax shield is 174bp of PBT. CON ETR on PBT after JV is 24.32%. The SA balance sheet swung from a DTL of 43.35 to a DTA of 6.95 (50.30). Of that, 3.34 went through P&L. The inferred split of the rest is 45.94 through equity (IPO issue costs, see R-A3-19) and about 1.03 through OCI. There is no prior-year tax adjustment line (nil). Single-quarter credit, not yet persistent. Question: driver of the Q2 credit. |
| R-A3-15 | F10 | R129-R134, R139-R144, R473-R478, R483-R488, R295 | 211, 214, 554, 557, 377 | "Paid-up Equity Share Capital ... \| 1,223.65 \| 1,000.00" | FORWARD-SIGNAL | The capital change traces to the IPO fresh issue of 2,23,65,164 shares (Note 7, line 377), a 22.37% increase in share count. Basic equals diluted in every period, so there are no dilutive instruments. Q2 EPS uses about 120.9m weighted shares. On the full 122.365m count, Q2FY27 CON EPS is 2.04 vs 2.06 in Q2FY26 (about -1%) while PAT grew 21.24%. Q3 carries the full dilution. |
| R-A3-16 | F13 | M1 (MISSING_FROM_STRUCTURED) | 79 | "3. Consideration and approval of other businesses as per agenda circulated." | AMBIGUOUS | The Board approved unnamed "other businesses". The letter shows no AR, AGM, dividend, director, auditor, ESOP or fund-raise item. Question: what item 3 covered, and whether any of it needs a Reg 30 disclosure, for example JV funding (see R-A3-01 and R-A3-04). |
| R-A3-17 | F14 | R684-R688, R697-R701, R902 | 819, 821, 823 | "*EBITDA is calculated including Other Income EBITDA margins = EBITDA/Revenue from Operations" | AMBIGUOUS | Every printed margin is computed on Total Income, not on Revenue from Operations as the footnote states. Q2 is 497.65/3,044.61 = 16.35%; the footnote basis gives 16.88%. Q2FY26 is 383.04/1,995.48 = 19.2% (19.82% on revenue). PAT margins use the same total-income base. EBITDA also includes other income. On revenue and excluding other income, CON EBITDA margin was 13.59% in Q2FY27, 21.66% in Q1FY27 and 16.57% in Q2FY26. The core margin fell 807bp QoQ, which the 16.35% headline hides. |
| R-A3-18 | F14 | R152-R153, R250, R416, R418 | 234, 305, 542 | "(d) Investments accounted for using equity method \| 45.59 \| 45.59" (standalone) | FORWARD-SIGNAL | The standalone balance sheet uses the equity-method label for an investment that is held at cost and unchanged at 45.59. Cumulative group share of JV losses is 70.01 (FY26 9.41 + H1FY27 60.60), above the 43.96 paid (line 305). This is a standalone impairment indicator that is not reflected. Risk: an SA impairment of up to 45.59 (13.7% of Q2 SA PBT, 17.6% of Q2 SA PAT) when tested, likely at the FY27 audit. |
| R-A3-19 | F14 | R265, R611, R309-R313, R182-R183 | 314, 406, 252 | "Share Issue Expense (net of tax) \| (253.03)" | AMBIGUOUS | Three issue-expense figures appear. CF cash outflow "net of tax" is 253.03, Note 9 issue expenses utilised is 259.03, and the equity roll-forward residual is 207.09 (opening other equity 2,047.76 + TCI 570.42 + premium 3,576.35 - closing 5,987.44). A cash line cannot be net of a deferred tax. The 45.94 gap matches the unexplained DT swing (R-A3-14). Question: gross issue cost borne by the company vs the selling shareholders, and the 6.00 timing gap. |
| R-A3-20 | F14 | R806, R821, R320-R323 | 125, 432, 492 | SA: "for the period ended September 30, 2026"; CON: "for the quarter ended September 30, 2026" | AMBIGUOUS | The consolidated review report names only the quarter, yet the statement carries H1 YTD and a half-year cash flow (lines 627-665). Subsidiary figures are given "for the quarter ended" only. The review scope of the CON H1 figures and CON cash flow is not stated. |
| R-A3-21 | F14 | R250, R596, R566, R415 | 305, 649, 632 | "Purchase of equity investment measured at cost \| - \| (42.18)" (CON) vs "(43.96)" (SA) | NEUTRAL-FACT | The H1FY26 JV investment outflow is 43.96 in SA and 42.18 in CON. The 1.78 gap equals the H1FY26 JV loss share (line 632), so the loss may be netted in investing cash flow as well as added back in operating. Rounding-level relative to the totals. Recorded for the cumulative governance tally with the 0.01 PBT mismatches (R863, R888). |
| R-A3-22 | F15 | R747-R750, R768-R770, R754-R755, R890, R778 | 365-373, 461-462, 689-690, 841 | "the equity interests held by "Sacos Y Empaques Internacionales S.A. de C.V." and "Mauricio Ferretis Diaz Infante" in the joint venture were transferred to "Bessher Holding S.A.P.I. de C.V."" | AMBIGUOUS | No prior extract, so this is the baseline: one subsidiary and one JV, and the auditor para 4 agrees with CON Note 1. Relationship change: the JV co-venturer moved from the company's "key strategic customer" (40%) plus an individual (10%) to Bessher Holding (50%) on 30-Dec-2025, eight months after formation. Bessher's link to Sacos is not disclosed. The customer anchor that justified the JV may have exited while the JV's losses accelerated. The press release does not name the JV. |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 41 ZERO_STANDING rows read. Labour Codes line nil x5 interim (R-A3-02). CON JV equity-method investment nil at 30-Sep-2026 (R-A3-01). The remaining zeros are template or timing items: DTA/DTL sign swaps, FD/share-issue lines nil in H1FY26, opening IPO balances nil, Annexure C modified allocation/deviation 0.00. |
| F2 S-vs-C decomposition | FINDING | PAT gap swings from +2.69% (H1FY26) to -3.14% (H1FY27) of SA PAT, 5.83pp. Decomposition: subsidiary +15.58, eliminations +2.33, JV -26.15 (R-A3-03). Funding residues (R-A3-04). EBITDA gap Q2 23.59, Q1 34.13, Q2FY26 5.57. |
| F3 Shell-entity detection | FINDING | Identical COMC means the subsidiary is non-manufacturing, a trading arm with real revenue and PAT, not a shell. The JV has zero revenue. No going-concern language (R-A3-05). |
| F4 Unaudited contribution ratio | FINDING | Gross 41.73 = 16.7% of CON PAT (R-A3-06). JV unreviewed share up 14.7x YoY (R-A3-07). Comparative columns unreviewed (R-A3-08). |
| F5 Going concern / EoM scope | PASS | No going concern, no Emphasis of Matter (lines 147-164, 464-505). The Other Matter para 6 is unmodified (line 505). No prior extract to diff, so this quarter's para 1 caveat and para 6 wording are the baseline. |
| F6 Forward-commitment mining | FINDING | 9 commitments registered. Pass-through timing conflict (R-A3-09), JV breakeven claim (R-A3-10), Borisana and other income (R-A3-11), GCP use (R-A3-12). |
| F7 Hedge mining | FINDING | "subject market stabilization" and "likely ... next few quarters" attached to the pass-through promise (R-A3-13). |
| F8 Tax forensics | FINDING | SA Q2 ETR 22.38% (-279bp vs 25.17%). Deferred tax sign flip. DT balance-sheet swing of 50.30 vs 3.34 through P&L. No prior-year tax line (R-A3-14). |
| F9 OCI forensics | PASS | SA remeasurement: Q2 (1.46), Q1 (1.62), H1 (3.07) vs FY26 +3.62. No single quarter exceeds the prior full year. CON reclassifiable FX: Q2 (2.97) vs FY26 3.90. Immaterial (<1% of PAT). Verify actuarial assumptions at the FY27 AR as routine. |
| F10 Share count and dilution | FINDING | Paid-up 1,000.00 to 1,223.65, traced to the IPO (Note 7). Basic = diluted throughout. Per-share Q2 PAT on the full count is about flat YoY (R-A3-15). |
| F11 Reserves and net worth tie-out | PASS | SA 1,223.65 + 5,987.44 = 7,211.09; CON 1,223.65 + 5,999.59 = 7,223.24. Roll-forward residual 207.09 SA / 207.07 CON = issue costs net of deferred tax, 2.9% of net worth (<5%). No third-party net worth number in this filing. |
| F12 Segment forensics | PASS | Single segment per Ind AS 108 (Note 5, lines 363, 706). No segment assets or liabilities are disclosed to trend. Capex proxy: SA PPE +176.90 plus D&A 200.70 = about 377.6 gross additions vs cash capex 274.97 (line 303). Other non-current assets +109.01. No CWIP line on either balance sheet. |
| F13 Board outcome beyond results | FINDING | Agenda item 3 "other businesses" is undisclosed (M1, line 79; R-A3-16). No AR, AGM, dividend, director-term, auditor or fund-raise item, so no Role 6 AR event is triggered. |
| F14 Note drafting inconsistencies | FINDING | Margin denominator vs footnote (R-A3-17). Standalone equity-method label and unimpaired JV cost (R-A3-18). Issue-expense triple (R-A3-19). CON review scope "quarter" only (R-A3-20). JV investment outflow 1.78 gap (R-A3-21). 0.01 PBT mismatches (R863, R888) are rounding-level. |
| F15 Entity list diffs | FINDING | No prior extract; baseline set at 1 subsidiary + 1 JV. JV co-venturer changed from key customer to Bessher Holding on 30-Dec-2025 (R-A3-22). |
| F16 Presentation: dropped/reframed | N.A. | Results filing (doctype rule). The deck is covered by the D- file. |
| F17 Concall silence audit | N.A. | Results filing (doctype rule). The coordinator watch list is mapped below for information only. The concall C- file runs the silence audit. |

## COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Further Labour Code accounting effects as Central/State rules are finalised | undated | SA Note 3 lines 355-357; CON Note 3 lines 698-700 (R790, R791) | initiated (monitoring) |
| Customer price revisions pass input-cost increases into realisations, "subject market stabilization" | Q3FY27 onwards | PR lines 835-839 (R792, R841) | underway |
| Benefits of price revisions already implemented materialise | "next few quarters" | PR lines 856-860 (R795, R796) | completed (implementation) / pending (benefit). Conflicts with the row above |
| JV drag reverses and PAT margin "recovers fully" at JV breakeven | undated | PR lines 845-847 (R793, R794) | not started (JV in "peak scale-up investment phase", zero revenue) |
| Borisana facility IPO capex 3,192.96 unutilised, used "progressively as the project progresses" | undated | Note 9 line 404; Annex C lines 957-971 (R299-R303, R799, R920) | commenced ("recently commenced") |
| GCP balance 16.80 and issue-expense balance 29.48 to be deployed | undated | Note 9 lines 405-406 (R308, R313) | underway |
| Investments in capacity, growth, innovation, sustainability | undated | PR lines 867-870 (R797, R798) | intent (boilerplate) |
| IPO completed, listed NSE/BSE | 8-Jul-2026 (allotment 6-Jul-2026) | Note 7 lines 375-379; Annex C line 926 | completed |
| JV capital commitment USD 0.5M | 6-Aug-2025 | Note 6 line 369 | completed (now exceeded per R-A3-01) |

## WATCH-LIST COVERAGE (informational; F17 stays N.A. on a results filing)

| # | coordinator item | in this filing? | cite |
|---|---|---|---|
| 1 | volume (tonnes/bags) | NOT DISCLOSED | - |
| 2 | realisation per kg | NOT DISCLOSED (qualitative only: revisions "underway") | 835-839 |
| 3 | PP input-cost pass-through | qualitative; CON gross margin 34.64% Q2 vs 42.07% Q1 vs 41.15% Q2FY26 | 530-532, 831-839, 854-860 |
| 4 | export share | NOT DISCLOSED ("exporter to 75 countries" only) | 835, 876 |
| 5 | capacity utilisation | NOT DISCLOSED | - |
| 6 | Units 4 and 5 timeline | NOT DISCLOSED (only Borisana IPO project "recently commenced") | 969-971 |
| 7 | receivable / inventory days | computable: CON receivables 55.3 days and inventory 45.3 days on Q2 annualised revenue, vs 61.3 / 52.9 days on FY26. H1 CFO 220.59 vs 389.44 H1FY26 (CFO/EBITDA about 20%) | 583-584, 641, 645 |
| 8 | customer concentration | NOT DISCLOSED (one "key strategic customer" named, the JV ex-partner) | 368 |
| 9 | IPO proceeds use | DISCLOSED: Borisana 7.04/3,200.00, GCP 294.69/311.49, issue 259.03/288.51, no deviation, monitoring agency CARE | 404-407, 924-1004 |

```yaml
stage: A3-forensics
company: "KNACK"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/knack-q2fy27/work/forensics_results_knack_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: PASS
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "R-A3-01", check: "F1", line: "577, 542", classification: "FORWARD-SIGNAL", implication: "CON JV equity-method investment nil (34.55 at Mar); H1 JV loss 60.60 means 26.05 booked beyond carrying value; group funding JV beyond USD 0.5M; future JV losses hit PAT in full and need cash"}
  - {id: "R-A3-02", check: "F1", line: "200, 540, 355-357", classification: "FORWARD-SIGNAL", implication: "Labour Codes exceptional line retained; further past-service-cost charge possible when rules finalise; undated, low materiality"}
  - {id: "R-A3-03", check: "F2", line: "206, 548, 542", classification: "FORWARD-SIGNAL", implication: "CON-SA PAT gap +2.69% (H1FY26) to -3.14% (H1FY27) of SA PAT, 5.83pp swing; Q2 = sub +15.58, elim +2.33, JV -26.15"}
  - {id: "R-A3-04", check: "F2", line: "307, 651, 244, 237, 580", classification: "AMBIGUOUS", implication: "CON loans given exceed SA by 13.80; CON other NCA 18.21 below SA; SA Loans fell 56.52 to 16.94 despite 124.49 lent; counterparty undisclosed, possible JV funding"}
  - {id: "R-A3-05", check: "F3", line: "191, 530, 531, 490-491", classification: "AMBIGUOUS", implication: "Subsidiary is non-manufacturing trading arm (identical COMC); PAT margin 12.7% vs parent 8.9%; transfer-pricing question"}
  - {id: "R-A3-06", check: "F4", line: "489-503", classification: "AMBIGUOUS", implication: "Unreviewed sub PAT 15.58 + JV (26.15) = 41.73 gross, 16.7% of CON PAT; other auditors unnamed"}
  - {id: "R-A3-07", check: "F4", line: "498, 542", classification: "FORWARD-SIGNAL", implication: "Unreviewed JV share up 14.7x YoY (1.78 to 26.15); fastest-growing drag rests on unnamed auditor"}
  - {id: "R-A3-08", check: "F4", line: "127-129, 434-436, 381-383", classification: "NEUTRAL-FACT", implication: "Q2FY26/H1FY26 comparatives unreviewed; all YoY growth rests on unreviewed base; caveat persists through Q4FY27"}
  - {id: "R-A3-09", check: "F6", line: "835-839, 856-860", classification: "FORWARD-SIGNAL", implication: "Pass-through dated 'from Q3 FY27' and 'next few quarters', status 'underway' vs 'implemented' in same release; test vs CON gross margin 34.64% Q2 (42.07% Q1, 41.15% Q2FY26)"}
  - {id: "R-A3-10", check: "F6", line: "841-847", classification: "AMBIGUOUS", implication: "'PAT margin recovers fully' at JV breakeven unsupported: ex-JV Q2 PAT margin 9.08% vs 10.43%; JV explains ~77bp of 212bp decline; Q2 JV loss 10.5% of PAT called 'slightly'"}
  - {id: "R-A3-11", check: "F6", line: "404, 957-971, 188, 306", classification: "FORWARD-SIGNAL", implication: "Borisana 7.04 of 3,200 used, undated; other income 28.7% of SA Q2 PBT from parked IPO cash; core SA PBT ex-OI +12.5% YoY, -40.1% QoQ; OI decays as capex draws"}
  - {id: "R-A3-12", check: "F6", line: "405, 315, 307", classification: "AMBIGUOUS", implication: "GCP 294.69 of 311.49 spent in first quarter while ST borrowings rose 81.01 and 124.49 lent; use undescribed"}
  - {id: "R-A3-13", check: "F7", line: "839, 859-860", classification: "FORWARD-SIGNAL", implication: "'subject market stabilization' and 'likely ... next few quarters' pre-excuse a Q3 pass-through miss"}
  - {id: "R-A3-14", check: "F8", line: "204-205, 236, 258, 546", classification: "AMBIGUOUS", implication: "SA DT credit (5.80) in Q2, ETR 22.38% (-279bp vs 25.17%); DT BS swing 50.30 vs 3.34 P&L, residual ~45.94 via equity on IPO costs; no prior-year tax line"}
  - {id: "R-A3-15", check: "F10", line: "211, 214, 554, 557, 377", classification: "FORWARD-SIGNAL", implication: "Shares +22.37% via IPO; basic=diluted; full-count Q2 CON EPS 2.04 vs 2.06 Q2FY26 (about -1%) despite PAT +21.24%"}
  - {id: "R-A3-16", check: "F13", line: "79", classification: "AMBIGUOUS", implication: "Agenda item 3 'other businesses' undisclosed (A2 M1); ask what was approved, incl any JV funding"}
  - {id: "R-A3-17", check: "F14", line: "819, 821, 823", classification: "AMBIGUOUS", implication: "Margins printed on Total Income, footnote says Revenue from Ops (16.88% on own definition); ex-OI EBITDA margin 13.59% Q2 vs 21.66% Q1 vs 16.57% Q2FY26"}
  - {id: "R-A3-18", check: "F14", line: "234, 305, 542", classification: "FORWARD-SIGNAL", implication: "SA labels JV 'equity method', carried unchanged at 45.59; cumulative group JV loss 70.01 above 43.96 cost; standalone impairment risk up to 45.59 (17.6% of Q2 SA PAT)"}
  - {id: "R-A3-19", check: "F14", line: "314, 406, 252", classification: "AMBIGUOUS", implication: "Issue expense 253.03 (CF 'net of tax') vs 259.03 (Note 9) vs 207.09 equity residual; label inconsistent"}
  - {id: "R-A3-20", check: "F14", line: "125, 432, 492", classification: "AMBIGUOUS", implication: "CON review report names quarter only; CON H1 and cash flow scope unstated"}
  - {id: "R-A3-21", check: "F14", line: "305, 649, 632", classification: "NEUTRAL-FACT", implication: "H1FY26 JV investment outflow SA 43.96 vs CON 42.18; 1.78 gap equals H1FY26 JV loss share; rounding-level"}
  - {id: "R-A3-22", check: "F15", line: "365-373, 461-462, 689-690", classification: "AMBIGUOUS", implication: "No prior extract, baseline 1 sub + 1 JV; JV co-venturer moved from key strategic customer to Bessher Holding 30-Dec-2025; link undisclosed"}
forward_signals: ["R-A3-01", "R-A3-02", "R-A3-03", "R-A3-07", "R-A3-09", "R-A3-11", "R-A3-13", "R-A3-15", "R-A3-18"]
ambiguous: ["R-A3-04", "R-A3-05", "R-A3-06", "R-A3-10", "R-A3-12", "R-A3-14", "R-A3-16", "R-A3-17", "R-A3-19", "R-A3-20", "R-A3-22"]
commitments:
  - {commitment: "Further Labour Code accounting effects as rules finalise", implied_date: "undated", ref: "SA Note 3 L355-357; CON Note 3 L698-700", status_word: "initiated"}
  - {commitment: "Price revisions reflect in realisations, subject to market stabilisation", implied_date: "Q3FY27 onwards", ref: "PR L835-839", status_word: "underway"}
  - {commitment: "Benefits of implemented price revisions materialise", implied_date: "next few quarters", ref: "PR L856-860", status_word: "completed (implementation); conflicts with L835-839"}
  - {commitment: "JV drag reverses, PAT margin recovers fully at JV breakeven", implied_date: "undated", ref: "PR L845-847", status_word: "not started"}
  - {commitment: "Borisana IPO capex 3,192.96 used progressively", implied_date: "undated", ref: "Note 9 L404; Annex C L957-971", status_word: "commenced"}
  - {commitment: "Deploy GCP balance 16.80 and issue-expense balance 29.48", implied_date: "undated", ref: "Note 9 L405-406", status_word: "underway"}
  - {commitment: "Investments in capacity, growth, innovation, sustainability", implied_date: "undated", ref: "PR L867-870", status_word: "intent"}
  - {commitment: "IPO completed and listed", implied_date: "2026-07-08", ref: "Note 7 L375-379", status_word: "completed"}
  - {commitment: "JV capital commitment USD 0.5M", implied_date: "2025-08-06", ref: "Note 6 L369", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Q2 headline growth hides a margin break. CON gross margin fell to 34.64% from 42.07% in Q1 and 41.15% a year ago. EBITDA excluding other income was 13.59% of revenue against 21.66% in Q1. Other income, mostly interest on parked IPO cash, is 28.7% of SA PBT and decays as Borisana capex (0.22% used) draws the FDs. The Mexico JV is the second thread. Its equity-method carrying value hit nil, the group booked 26.05 of loss beyond it, and CON loans given exceed SA by 13.80. So the group funds a zero-revenue JV whose strategic-customer partner exited in Dec-2025. The standalone 45.59 cost is unimpaired against 70.01 cumulative losses. Per share, Q2 CON PAT on the full post-IPO count is about flat YoY. The press release dates pass-through two ways. Its 'recovers fully' claim fails arithmetic: the JV explains about 77bp of the 212bp PAT-margin drop. All YoY bases are unreviewed. F17 is N.A. by doctype; 6 of 9 coordinator watch items are not disclosed in this filing."
```
