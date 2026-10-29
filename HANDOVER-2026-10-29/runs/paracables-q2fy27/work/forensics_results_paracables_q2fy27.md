# A3 FORENSIC NOTES: results | PARACABLES | Q2 FY27 (quarter and half year ended 30-Sep-2026; board 26-Oct-2026)

Agent: A3 forensic notes | model: claude-opus-5-5 | run date: 2026-10-28
Inputs read: A1 structured (R001-R989 plus appendix R990-R993), A1 fulltext (713 lines, all read), A2 ledger (all sections), Notion snapshot 2026-10-28 (properties line 11; sections at lines 210, 489, 612, 619, 644, 665-745, 757-872). Source PDF and inputs/ not opened.

## 0. RECONCILIATION AND EVIDENCE GRADE

- Ledger rows reconciled: 993 of 993 (100%). R001-R989 as the A2 ledger lists them. M001-M004 resolve to the A1 appendix rows R990 (1.74), R991 (nil), R992 (97.67), R993 (nil) at fulltext lines 604 and 612. No ID is orphaned.
- Every structured value was checked against its fulltext line. Matches throughout. Three A1 context labels need care downstream:
  - R909/R910 add "(75% balance payable on conversion)". That phrase is not printed. Line 345 says only "upon receipt of 25% application money". The 75% balance is an inference, true by construction.
  - R973 calls CO para 5 an "emphasis on unreviewed subsidiaries". It is not an Emphasis of Matter. It is an other-matter style paragraph, and the conclusion is "not modified" (line 425).
  - R830 (SA UDIN) is an A1 reading of illegible OCR (line 145). R861 prints "DIN" (line 442). Both are unresolved.
- Evidence grade: statement pages 3, 4, 5, 9, 10, 11 and 13 are image-checked. Use-of-proceeds table values on pages 6 and 12 are image-checked. Note text on pages 6 and 12, both review reports (pages 2, 7, 8) and the board letter (page 1) are RAW OCR. A finding that rests on raw OCR says so in its quote cell.
- Prior-quarter fulltext: none in the repo. No verbatim diff of the auditor paragraphs or the entity list was possible. Where a check needs a prior period, the comparison uses the Notion snapshot as memory, not anchored evidence, and says so.
- "My arithmetic" marks every number that A3 computed. Every other number is filed.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R097-R114, R441-R458, R411-R416, R207-R208, R551-R552, R787-R792 | 182, 478, 470, 225, 706 | "X \| Profit from discontinued operations - - - - - -" (l.182); "(i) Investments 0.00 0.00" (l.225) | NEUTRAL-FACT | The Valens / Pipes exit never used the discontinued-operations lines, even in the FY26 columns that include Valens. The parent carries its two subsidiaries at nil. The only consolidated exceptional is FY26 0.03 (l.470), linked in memory to a subsidiary cessation. The next use of the exceptional line is most likely a small gain or loss when a shell subsidiary is struck off. Nothing larger is anticipated by the template. |
| A3-02 | F3 | R897, R898, R851-R856, R973, R975 | 407-413 | "total assets of Rs. NIL as at 30t September, 2026, total revenue of Rs. NIL, net profit after tax of Rs. NIL" (raw OCR) | NEUTRAL-FACT | Paramount Holdings Limited and AEI Power Cables Limited are shells. FY27 cost lines are identical standalone vs consolidated (COGS 432.33, employee 12.21, D&A 4.43). Neither report has a going-concern paragraph, so the auditor does not flag a balance-sheet cleanup. The S-vs-C gap is now zero by construction. Any future gap means a new entity or new activity. |
| A3-03 | F6 | R839, R840, R909, R910, R867, R868, R922 | 343-347 (SA 4b); 640-644 (CO 5b) | "upon receipt of 25% application money (i.e. Rs. 10.50/- per equity warrant) ... allotted the equity share warrants to respective allotees on 01.07.2026" (raw OCR) | FORWARD-SIGNAL | 72,00,000 promoter warrants are outstanding. The balance due on conversion is Rs 22.68 Cr (72,00,000 x Rs 31.50, my arithmetic). The filing gives no conversion date. The ICDR 18-month window from 01.07.2026 ends about 31-Dec-2027 [INFERENCE from regulation, not filed]. Full conversion adds 0.72 Cr shares, 2.2% of 32.72 Cr (my arithmetic). Notion trigger 2 (l.615) reads non-exercise within 12 months as a soft negative. |
| A3-04 | F6 | R841-R845, R947-R949, R869-R873, R982, R983 | 354-357 (SA 4c); 650-653 (CO 5c) | "Less: Utlization during the quarter endsd 30.09.2026 73.39" / "there is no deviation in utilization of issue proceeds" (table image-checked C36; text raw OCR) | FORWARD-SIGNAL | Rs 73.39 Cr is marked utilised ("completed") but the note does not name the objects. H1 capex paid was Rs 41.30 Cr (l.307), part of it in Q1 before the money arrived. So at least Rs 32 Cr of the utilisation was not capex (my arithmetic). The likely use is working capital, given that payables fell Rs 54.16 Cr (l.300) [INFERENCE]. If the proceeds funded working capital, the Rs ~300 Cr Narmadapuram Phase 1 (memory) needs debt. Non-current borrowings have already moved 1.85 to 20.68 (l.250). The unutilised Rs 26.66 Cr ties to mutual funds of Rs 26.33 Cr (l.233) plus about Rs 0.33 Cr in the utilisation account (my arithmetic). Status: Rs 26.66 Cr undeployed, undated. |
| A3-05 | F8 | R079-R090, R315, R316, R267, R268, R249, R250 | 177, 178, 304, 267 | "Income Tax Paid/ Refund/ Provisions (Net) (4.67) (1.62)" (l.304, image-checked) | AMBIGUOUS | H1 current tax was 16.26 (l.177). Net tax paid was 4.67, a 29% cash coverage (my arithmetic). Current tax liability rose 7.35 to 11.59 (l.267). 16.26 - 4.67 = 11.59 exactly, so the opening 7.35 left the balance sheet without a cash line (my arithmetic). Possible routes: netting against tax assets, or a refund netted into the "(Net)" line. Advance tax on 45% of estimated FY27 tax (about Rs 14.6 Cr on H1 x 2, my arithmetic) fell due by 15-Sep-2026. Memory (Notion l.11, l.677): the FY26 CARO flagged advance-tax delays of Rs 1.75/5.50/0.50 Cr. A repeat means a liquidity tell, interest under s.234B/C, and a possible CARO repeat. The ETR itself is clean: see the scorecard F8 basis. |
| A3-06 | F10 | R163-R174, R187-R198, R507-R518, R531-R542, R157-R162, R839 | 201-202, 210-211, 497-498, 506-507 | "(2) Diluted 0.74 0.64 0.44 1.38 1.06 1.97" (l.202, image-restored C07) | AMBIGUOUS | Basic equals diluted EPS in every period, standalone and consolidated. This holds even though 72,00,000 warrants at Rs 42 were outstanding for all of Q2 while the price traded above Rs 42 (memory: Rs 55-71). Treasury-stock dilution is about 0.2-0.3 Cr shares, or 0.7-0.9% (my arithmetic). That may round away at two decimals. The treatment is undisclosed. Paid-up capital traces cleanly: 61.04 + 4.40 (2,19,97,664 x Rs 2) + 0.0064 (31,995 x Rs 2) = 65.45 (my arithmetic). One oddity: Q1 basic 0.64 vs 19.70 / 30.52 Cr = 0.645 (my arithmetic). That is consistent with the new shares being counted from cash receipt in late June (see A3-07). |
| A3-07 | F11 | R794, R818, R158, R237-R242, R834-R838, R921 | 707, 712, 197, 339 | "Total Segment Assets 1,248.59 1,248.37" (l.707) / "Total Segment Liabilities 328.58 354.48" (l.712) (image-checked); "During the quarter ended 30.09.2026, upon receipt of amount of issue price" (l.339, raw OCR) | AMBIGUOUS | Implied equity at 30.06.2026 is 1,248.37 - 354.48 = 893.89 (my arithmetic). Without the issue money it would be about 797.9 (778.07 + Q1 TCI 19.75 + share-based expense, my arithmetic). The gap of about Rs 96 Cr is close to the Rs 97.67 Cr net proceeds. Paid-up capital at 30.06 is still 61.04 (l.197). Reading A: the cash arrived in Q1 and sat in equity as share application money pending allotment, and note 4a's "during the quarter ended 30.09.2026, upon receipt" wording is loose. Reading B: the Q1 segment balances are misstated. The 30.09 tie-out passes: 65.45 + 854.56 = 920.01 (l.244-246). The equity roll-forward 778.07 + 44.04 TCI + 97.67 net proceeds + 0.24 SBP = 920.02 vs 920.01 filed (my arithmetic). Issue expenses come to about Rs 2.28 Cr (99.95 gross - 97.67 net, my arithmetic). No third-party net-worth figure is in context. |
| A3-08 | F12 | R799-R804, R817-R822, R259, R260, R243, R244, R253, R254 | 709, 262, 250, 257 | "Wire and Cables 328.58 354.48 243.93" (l.709, image-checked) | AMBIGUOUS | Segment liabilities fell 25.90 in Q2 (-7.3% QoQ) while segment assets stayed flat (+0.22) (my arithmetic). Over H1, non-MSME payables fell 185.94 to 130.69 (-29.7%) (l.262) while borrowings rose 16.19. New non-current debt went 1.85 to 20.68 (l.250). Reading A: supplier credit is shrinking (copper suppliers moving to advance or LC terms), a working-capital strain. Reading B: issue money was used to pay creditors for cash discounts, which is margin-accretive. Bank balances other than cash rose 28.35 to 49.13 (l.236), which fits margin money for LCs but is not disclosed. |
| A3-09 | F12 | R213, R214, R319, R201, R202, R199, R200 | 228, 307-308, 221, 220 | "(f) Other Non-Current Assets 36.56 6.78" (l.228, image-checked) | FORWARD-SIGNAL | Other non-current assets rose +29.78 in H1. This roughly equals capex paid of 41.30 (l.307, "including Capital Work In Progress and Capital Advances") less PPE plus CWIP additions of about 12.35 (my arithmetic). So it is most likely capital advances: equipment ordered but not received [INFERENCE]. CWIP is only 3.59 (l.221). Visible next-capacity spend is about Rs 33 Cr, against the Rs ~300 Cr Phase 1 with partial commissioning in Q1 FY28 (memory, Notion l.11). Track the conversion of advances into CWIP each quarter as the capex proxy. The filing never names Narmadapuram. |
| A3-10 | F12 | R217, R218, R025-R028, R369-R372, R303 | 231, 166, 298 | "(b) Changes in inventories of finished goods, (13.97) (28.79)" (l.166, image-checked) | AMBIGUOUS | H1 inventory rose +44.55 (+15.6%) (l.231, l.298). Of that, 42.76 is a finished goods / WIP / scrap build through the P&L (l.166). QoQ revenue grew 5.9% (my arithmetic). Memory, as broker-relayed management: "production for US orders paused pending October tariff decisions" (Notion l.753). Reading A: dispatch pipeline for H2 orders. Reading B: export stock held or unsold. This build is what drove H1 CFO of -31.89 (l.305) alongside the payables paydown. |
| A3-11 | F12 | R691-R696, R703-R708, R781-R786, R805-R816, R985, R950 | 684, 686, 705, 711, 664, 362 | "Pipes - - 3.69 - 4.21 6.41" (l.684, image-checked) | NEUTRAL-FACT | The Pipes segment was Valens. Pipes revenue less inter-segment revenue equals the CO-SA revenue gap: Q2 FY26 3.69-3.26 = 0.43 = 428.00-427.57; H1 FY26 4.21-3.53 = 0.68 = 879.12-878.44; FY26 6.41-5.23 = 1.18 vs 1.19 (my arithmetic). CO note 8 still says "two reportable segments" (l.664). The group is now single-segment, which matches SA note 6 (l.362). Unallocated assets are nil in every period. Unallocated liabilities went 12.65 to nil. Expect the annexure to be dropped or restated, which is a disclosure change for F16 next quarter. |
| A3-12 | F14 | R992 (ex-M003), R335, R867, R868 | 612 vs 317, 640-644 | "Proceeds from Issue of Equity Share upon conversion of Equity share warrants (Net of issiie expenses)" (l.612-613, image-checked) | NEUTRAL-FACT | No warrant was converted. Note 5b records only the 25% application money. The consolidated label is wrong and the standalone label (l.317) is right. Individually immaterial. It adds to the governance data points below. |
| A3-13 | F14 | R945, R979, R942, R974 | 333-334, 628-629 vs 130-131, 402-403 | "The Statutory Auditors have expressed an unmodified opinion on these results." vs "we do not express an audit opinion" (both raw OCR) | NEUTRAL-FACT | The notes call a limited-review conclusion an "opinion", which overstates the assurance. This is a common drafting habit. It is cumulative with A3-12 and A3-14. |
| A3-14 | F14 | R830, R941, R861 | 145, 442 | "UDIN: 2 6O806GIIABTTN5 (83" (l.145); "DIN: 26080691VFYDBU8230" (l.442) (both raw OCR) | NEUTRAL-FACT | Both UDINs are unresolved, and the consolidated one is labelled "DIN". This may be scan noise, so it carries low weight. Verify both UDINs on the ICAI portal before any report cites them. |
| A3-15 | F15 | R897, R898, R902, R937, R416 | 406-408, 658-659, 470 | "4. The statement includes the result of the parent and the following subsidiaries: Paramount Holdings Limited AEI Power Cables Limited" (raw OCR) | AMBIGUOUS | Two subsidiaries are listed. Memory, not anchored (Notion AR FY26, l.677), lists three foreign subsidiaries, including "06196375 Cables Ltd UK in administration". No prior-quarter list exists to diff. Open points: when the third entity left the consolidation, whether the FY26 consolidated exceptional of 0.03 (l.470) was its cessation, and whether any guarantee or receivable remains. FY27 exceptional items are nil, so no deconsolidation hit P&L in H1. Valens (divested 06.11.2025, l.658) is a prior-year change, already in memory. |

## 2. CHECKLIST SCORECARD

| check | status | basis (one line) |
|---|---|---|
| F1 Zero-value standing lines | FINDING | 150 ZERO_STANDING cells reviewed. Discontinued-ops, exceptional, OCI-B, non-current investments, Pipes and unallocated lines are idle. Valens was never shown as discontinued (A3-01). |
| F2 Standalone vs consolidated | PASS | PAT gap as % of SA PAT: Q2 FY27 0.00%, Q1 FY27 0.00%, Q2 FY26 -0.08%, H1 FY27 0.00%, H1 FY26 -1.58%, FY26 -0.81%. Max swing 1.58 pp, under the 5 pp threshold. See section 4. |
| F3 Shell-entity detection | FINDING | FY27 COGS, employee cost and D&A are identical SA vs CO. Both subsidiaries are NIL on assets, revenue and PAT (l.411-412). No going-concern EoM (A3-02). |
| F4 Unaudited contribution ratio | PASS | Unreviewed subsidiaries contribute Rs NIL = 0% of consolidated PAT 24.24 (l.411-413). No JV or associate. Memory says FY26 subsidiaries were also immaterial. |
| F5 Going concern / EoM scope | PASS | No EoM, going-concern or qualification language in the SA (l.114-137) or CO (l.385-433) report. Both conclusions are unmodified (l.132, l.425-426). Prior-quarter verbatim auditor text was not available, so no line-by-line diff was run. Memory (Notion l.46, l.713) records FY26 as clean with no EoM. |
| F6 Forward-commitment phrases | FINDING | Lexicon hits: "commenc" (l.81, meeting time only), "being uploaded" (l.82), "has approved" (l.337, l.634, EGM), "upon receipt" (l.339, l.345), "upon conversion" (l.612, mislabel). Dateable commitments: the warrant balance and the undeployed proceeds (A3-03, A3-04). The filing contains no capex-commitment language. |
| F7 Hedge phrases | PASS | No lexicon hit. "Not material to the group" (l.424) is the auditor's materiality call on NIL subsidiaries. "Not directly comparable" (l.663) is the carried Valens comparability note (memory: FY26 note 7/8). No new hedge on revenue lumpiness or customer concentration. |
| F8 Tax forensics | FINDING | ETR: Q2 FY27 25.16%, Q1 FY27 25.77%, H1 FY27 25.44%, Q2 FY26 SA 25.59% / CO 25.56%, H1 FY26 SA 25.84% / CO 26.15%, FY26 SA 25.91% / CO 26.07%, vs 25.17% statutory (my arithmetic). The deferred-tax sign flipped to credit (Q2 -1.20, H1 -1.27) from debit (FY26 +0.55). Net DTL 3.57 to 2.33 ties to 1.27 P&L credit less 0.03 OCI tax (my arithmetic). No DTA and no earlier-years line. The finding is cash tax coverage (A3-05). |
| F9 OCI forensics | PASS | Actuarial gain 0.06 Q2, 0.07 Q1, 0.13 H1, vs 0.27 for FY26 (l.187). No single quarter exceeds the prior full year. No assumption-change signal. |
| F10 Share count and dilution | FINDING | Paid-up 61.04 to 65.45 traced to the preferential issue plus ESOP (l.341, l.361). The basic-diluted spread is zero despite in-the-money warrants (A3-06). |
| F11 Reserves and net worth tie-out | FINDING | 30.09 ties (65.45 + 854.56 = 920.01), and the roll-forward is within 0.01. The 30.06 equity implied by the segment table runs about Rs 96 Cr ahead of the note's timing (A3-07). |
| F12 Segment forensics | FINDING | Liabilities fell 25.90 QoQ with flat assets (A3-08). Capital advances +29.78 as the capex proxy (A3-09). FG/WIP build of 42.76 (A3-10). Pipes = Valens, now nil (A3-11). Unallocated assets nil throughout. |
| F13 Board outcome beyond results | PASS | Two items only: a) results, b) limited review report (l.76-80). No AR, AGM, record date, dividend, director term, capital-raising, capex approval or warrant-conversion item. Meeting ran 100 minutes (l.81). The CS signed at 15:52, 12 minutes after close (l.90). |
| F14 Note drafting inconsistencies | FINDING | Wrong CF label (A3-12), "opinion" vs review conclusion (A3-13), UDIN/"DIN" labels (A3-14). Excluded as OCR-risk: phone 45618600 (l.152) vs 45618800 (l.448); "pck@" (l.449); typos "Septmber", "conertible", "endsd". |
| F15 Entity list diffs | FINDING | 2 subsidiaries listed (l.407-408). Memory has 3 at FY26 AR. No prior-quarter list to diff (A3-15). |
| F16 Presentation: dropped / reframed | N.A. | Results filing, not a presentation. A3-11 flags the segment annexure for next quarter's F16. |
| F17 Concall silence audit | N.A. | Results filing, not a transcript. The Notion checklist cross-reference in section 5 is for A4's information only. |

Counts: PASS 6 (F2, F4, F5, F7, F9, F13) | FINDING 9 (F1, F3, F6, F8, F10, F11, F12, F14, F15) | N.A. 2 (F16, F17). No blanks.

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note / line ref | status word |
|---|---|---|---|
| Upload results to the company website | 26-Oct-2026 | Board letter, l.82-83 (R908) | underway ("is being uploaded") |
| Preferential issue: 2,19,97,664 equity shares at Rs 42 to non-promoters (Rs 92.39 Cr) | allotted 01-Jul-2026 | SA 4a l.337-342; CO 5a l.634-639 | completed |
| 72,00,000 promoter warrants at Rs 42; 25% paid (Rs 7.56 Cr); balance Rs 22.68 Cr on conversion (my arithmetic) | not in filing; ICDR window ends about 31-Dec-2027 [INFERENCE] | SA 4b l.343-347; CO 5b l.640-644 | initiated |
| Use of proceeds: Rs 73.39 Cr utilised, "no deviation"; objects not named | Q2 FY27 | SA 4c l.348-357; CO 5c l.645-653 | completed |
| Unutilised Rs 26.66 Cr "parked in mutual fund and utilization account" | not stated | SA 4c l.355-356; CO 5c l.651-652 | underway (pending deployment) |
| ESOP allotment, 31,995 shares | 14-Jul-2026 | SA 5 l.358-361; CO 6 l.654-657 | completed |
| Valens Technologies divestment | 06-Nov-2025 | CO 7 l.658-663 | completed |
| Narmadapuram capacity (Phase 1, partial commissioning Q1 FY28, per memory) | not in filing | none; CWIP 3.59 (l.221), advances (l.228) only | not mentioned |

## 4. F2 WORKING (Rs Cr; my arithmetic from filed lines 161-185 and 457-481)

| period | revenue SA / CO / gap | op EBITDA SA / CO / gap (PBT + fin + D&A - OI) | PAT SA / CO / gap | gap % of SA PAT |
|---|---|---|---|---|
| Q2 FY27 | 560.40 / 560.40 / 0 | 40.91 / 40.91 / 0 | 24.24 / 24.24 / 0 | 0.00% |
| Q1 FY27 | 529.40 / 529.40 / 0 | 34.74 / 34.74 / 0 | 19.70 / 19.70 / 0 | 0.00% |
| Q2 FY26 | 427.57 / 428.00 / +0.43 | 5.71 / 6.20 / +0.49 | 13.26 / 13.25 / -0.01 | -0.08% |
| H1 FY27 | 1,089.80 / 1,089.80 / 0 | 75.65 / 75.65 / 0 | 43.94 / 43.94 / 0 | 0.00% |
| H1 FY26 | 878.44 / 879.12 / +0.68 | 20.87 / 21.36 / +0.49 | 32.26 / 31.75 / -0.51 | -1.58% |
| FY26 | 1,912.16 / 1,913.35 / +1.19 | 65.73 / 66.33 / +0.60 | 60.24 / 59.75 / -0.49 | -0.81% |

Decomposition of the FY26-column gap: JV/associate share nil (no line). Subsidiary contribution was Valens (Pipes revenue net of inter-segment, A3-11). Eliminations: inter-segment revenue of 3.26 / 3.53 / 5.23 (l.686), and other income lower in CO by 0.31 / 0.60 / 0.67, consistent with eliminated interest from Valens (H1 FY26 interest income SA 2.48, l.290 vs CO 2.09, l.585). The FY27 gap is zero because both remaining subsidiaries are NIL.

## 5. NOTION CHECKLIST CROSS-REFERENCE (informational for A4; F17 is N.A. on a results filing)

| Notion item (memory line) | addressed in this filing? | filed anchor |
|---|---|---|
| Receivable days (l.213, l.648, l.741) | yes, balance only | trade receivables 394.79 vs 413.40 (l.234) |
| Operating CFO (l.649, l.737) | yes | H1 CFO (31.89) (l.305) |
| Other-expense reversal (l.494, l.737) | number yes, reason no | other expenses 88.92 Q2 (l.171) |
| Use of proceeds (l.617, l.647) | partly; objects not named | l.354-357 |
| Warrant exercise progress (l.615, l.651) | no conversion yet | l.345 |
| Allottee identity (l.614, l.646) | no; "non-promoter persons and entities" | l.338 |
| Narmadapuram date / CWIP build (l.737, l.741) | date silent; CWIP 3.59, advances 36.56 | l.221, l.228 |
| Keyman maturities (l.498) | no keyman visible; other income 3.80 | l.162 |
| Bill discounting, receivable ageing (l.705, l.843) | not in interim results | none |
| Pledge, FII/DII (l.497) | not in results filing | none |

## 6. ANALYST NOTE

See the YAML analyst_note. The four threads that matter for A4 are: the timing of the issue money (A3-07 with A3-06), the proceeds going to working capital while project debt starts (A3-04, A3-08, A3-09), cash tax coverage echoing the FY26 CARO advance-tax delays (A3-05), and the finished-goods build against the paused US orders (A3-10).

```yaml
stage: A3-forensics
company: "PARACABLES"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-paracables-q2fy27-a220cd/runs/paracables-q2fy27/work/forensics_results_paracables_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "182, 478, 470, 225, 706", classification: "NEUTRAL-FACT", implication: "Valens/Pipes exit never used discontinued-ops lines; parent carries subsidiaries at nil; next exceptional likely a small shell strike-off item"}
  - {id: "A3-02", check: "F3", line: "407-413", classification: "NEUTRAL-FACT", implication: "Paramount Holdings Ltd and AEI Power Cables Ltd are NIL shells; no going-concern EoM; S-vs-C gap now zero by construction"}
  - {id: "A3-03", check: "F6", line: "343-347; 640-644", classification: "FORWARD-SIGNAL", implication: "72L promoter warrants, Rs 22.68 Cr balance due on conversion (my arithmetic); no date filed; ICDR window ends about Dec-2027 [INFERENCE]"}
  - {id: "A3-04", check: "F6", line: "354-357; 650-653", classification: "FORWARD-SIGNAL", implication: "Rs 73.39 Cr utilised with objects unnamed; at least Rs 32 Cr non-capex (my arithmetic), likely working capital; Narmadapuram then needs debt; Rs 26.66 Cr undeployed"}
  - {id: "A3-05", check: "F8", line: "177, 304, 267", classification: "AMBIGUOUS", implication: "Net tax paid 4.67 vs current tax 16.26 (29%); 16.26-4.67=11.59 exactly, so opening 7.35 left without cash; possible repeat of FY26 CARO advance-tax delays"}
  - {id: "A3-06", check: "F10", line: "201-202, 497-498", classification: "AMBIGUOUS", implication: "Basic equals diluted in every period despite in-the-money Rs 42 warrants; treatment undisclosed; dilution about 0.7-0.9% (my arithmetic)"}
  - {id: "A3-07", check: "F11", line: "707, 712, 197, 339", classification: "AMBIGUOUS", implication: "Implied 30.06 equity 893.89 is about Rs 96 Cr above the no-issue level (my arithmetic), so issue cash was likely in by Q1 while note 4a says receipt in Q2; 30.09 tie-out passes"}
  - {id: "A3-08", check: "F12", line: "709, 262, 250", classification: "AMBIGUOUS", implication: "Segment liabilities -25.90 QoQ, assets flat; non-MSME payables -29.7% in H1; new non-current debt 1.85 to 20.68; supplier-credit squeeze vs paid-for-discount"}
  - {id: "A3-09", check: "F12", line: "228, 307-308, 221", classification: "FORWARD-SIGNAL", implication: "Other non-current assets +29.78, likely capital advances; with CWIP 3.59 about Rs 33 Cr visible vs Rs ~300 Cr Phase 1 (memory); track advances to CWIP"}
  - {id: "A3-10", check: "F12", line: "231, 166, 298", classification: "AMBIGUOUS", implication: "Inventory +44.55 in H1, of which FG/WIP build 42.76, vs revenue +5.9% QoQ; H2 dispatch pipeline or US export stock held on tariff pause (memory)"}
  - {id: "A3-11", check: "F12", line: "684, 686, 664, 362", classification: "NEUTRAL-FACT", implication: "Pipes segment was Valens (net Pipes revenue equals the CO-SA gap); group now single-segment; annexure likely dropped next quarter (F16 watch)"}
  - {id: "A3-12", check: "F14", line: "612 vs 317", classification: "NEUTRAL-FACT", implication: "Consolidated CF labels Rs 97.67 Cr as warrant conversion; none converted; standalone label correct; governance data point"}
  - {id: "A3-13", check: "F14", line: "333-334 vs 130-131", classification: "NEUTRAL-FACT", implication: "Notes say auditors expressed an unmodified opinion; review report says no audit opinion is expressed; overstated assurance wording (raw OCR)"}
  - {id: "A3-14", check: "F14", line: "145, 442", classification: "NEUTRAL-FACT", implication: "Both UDINs unresolved, consolidated one printed as DIN; possibly OCR noise; verify on ICAI portal"}
  - {id: "A3-15", check: "F15", line: "406-408", classification: "AMBIGUOUS", implication: "2 subsidiaries listed vs 3 in FY26 AR memory (06196375 Cables Ltd UK, in administration, absent); exit date, accounting and residual exposure unknown"}
forward_signals: ["A3-03", "A3-04", "A3-09"]
ambiguous: ["A3-05", "A3-06", "A3-07", "A3-08", "A3-10", "A3-15"]
commitments:
  - {commitment: "Upload results to company website", implied_date: "2026-10-26", ref: "Board letter l.82-83 (R908)", status_word: "underway"}
  - {commitment: "Preferential issue 2,19,97,664 shares at Rs 42 to non-promoters, Rs 92.39 Cr", implied_date: "2026-07-01", ref: "SA note 4a l.337-342; CO 5a l.634-639", status_word: "completed"}
  - {commitment: "72,00,000 promoter warrants at Rs 42, 25% paid; Rs 22.68 Cr balance on conversion (my arithmetic)", implied_date: "not filed; ICDR window about 2027-12-31 [INFERENCE]", ref: "SA note 4b l.343-347; CO 5b l.640-644", status_word: "initiated"}
  - {commitment: "Use of proceeds Rs 73.39 Cr utilised, no deviation, objects unnamed", implied_date: "Q2 FY27", ref: "SA note 4c l.354-357; CO 5c l.650-653", status_word: "completed"}
  - {commitment: "Unutilised Rs 26.66 Cr parked in mutual fund and utilisation account", implied_date: "not stated", ref: "SA note 4c l.355-356; CO 5c l.651-652", status_word: "underway"}
  - {commitment: "ESOP allotment 31,995 shares", implied_date: "2026-07-14", ref: "SA note 5 l.358-361; CO 6 l.654-657", status_word: "completed"}
  - {commitment: "Valens Technologies divestment", implied_date: "2025-11-06", ref: "CO note 7 l.658-663", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Consolidated equals standalone in FY27 because both subsidiaries are NIL shells, so the S-vs-C metric is now zero by construction. The forensic weight sits in the balance sheet. (1) Q1 segment totals imply the Rs 97.67 Cr was already in equity by 30-Jun, against note 4a's Q2 receipt wording. The Q1 EPS digits fit the same reading, so ask for the receipt date and the 30-Jun classification. (2) Rs 73.39 Cr utilised exceeds H1 capex by at least Rs 32 Cr while payables fell Rs 54 Cr and new term debt appeared. Proceeds likely funded working capital, so Narmadapuram leans on debt. Capital advances of +Rs 29.8 Cr are the first visible spend. (3) Net cash tax of Rs 4.67 Cr against Rs 16.26 Cr current tax, with the arithmetic exact to 11.59, echoes the FY26 CARO advance-tax delays. This is a liquidity tell, not an ETR issue. (4) A Rs 42.76 Cr finished-goods build next to the paused US orders (broker memory) drove negative CFO with payables. No prior-quarter auditor text was available, so F5 and F15 rest on Notion memory."
```
