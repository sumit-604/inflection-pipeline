# A3 FORENSIC NOTES: CYBERTECH q2fy27 (doctype: results)

Source of record: A1 fulltext `extracted/cybertech-results-q2fy27-fulltext.md` (443 lines, L-numbers below), A1 structured `extracted/cybertech-results-q2fy27-structured.md` (R001-R739), A2 ledger `work/ledger_results_cybertech_q2fy27.md`. No source PDF and nothing under `inputs/` was opened. Prior-quarter extract: NONE (first quarterly run). Notion checklist: NONE. Units: Rs Lakhs as printed. "computed" = arithmetic on filed figures by A3; "[INFERENCE]" = reading of those figures, not a filed fact.

## 0. LEDGER RECONCILIATION

- Structured IDs in ledger: 739 of 739 (R001-R739). Every ID's cited line was read in the fulltext; all 443 fulltext lines read. ledger_reconciled_pct = 100.
- A2 flags addressed: ZERO_STANDING (F1), SIGNATURE_BEFORE_MEETING_CLOSE (F13), AGENDA_NOT_LISTED (F13), ENTITY_WORDING_DIFF (F14 A3-18), ENTITY_UNNAMED (F1 A3-01), RESTATED (F10, F14), FOOTNOTE_UNRESOLVED (F14 A3-16).
- A1 DEFECT (pipeline note, not a document finding): R123 and R396 label the Other equity values 18,116.94 and 11,793.41 as "Quarter Ended 30-09-2025". The fulltext rows L125 `11 Other equity | | | | | | 18,116.94` and L308 `| | | | | | 11,793.41` put each value in the sixth column, Year Ended 31-03-2026. The values match the 31-03-2026 balance sheets (L167, L348). Downstream stages must read R123/R396 as FY26 year-end. R121, R122, R394, R395 carry a literal "|" as value (blank cells).
- A1 note: L415 standalone buyback row carries one cell `(1,498.00)` with no prior-year cell. Source or transcription cannot be told apart without source access (not opened).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R521-R522, R624, R731; R254, R523, R154-R155, R427-R428, R417-R418 | L405 | "Investment in a wholly owned subsidiary \| (4,113.13) \| -" | FORWARD-SIGNAL | Parent pushed Rs 4,113.13 lakh into an unnamed WOS in H1 FY27 (nil H1 FY26). Subsidiaries bought 3,263.77 of investments (L226 3,293.77 less L406 30.00, computed). That equals the rise in subsidiary-held current investments 10,428.51 to 13,692.28 (computed, L154 less L336). 95.1% of group current investments now sit in subsidiaries (computed). Parent non-current investments tie exactly: 3,036.69 less 701.16 plus 4,113.13 = 6,448.66 (L329, L147, computed) [INFERENCE: subsidiary cost base 2,335.53 at Mar-26]. No note names the sub or the purpose. Two readings: acquisition or expansion war chest in the US, or treasury parking offshore. Separating observation: Q3 subsidiary investment balance and any acquisition disclosure. |
| A3-02 | F1 | R188-R189, R459-R460, R266, R535 | L178 | "(i) Borrowings \| - \| 377.23" | NEUTRAL-FACT | Group debt-free at 30-Sep-2026; 377.23 repaid in H1 (L233). Template lines live and nil this half: loss on disposal (L205), ECL provision (L208), credit write-back (L209), PPE sale proceeds (L225), intangibles (L145, 0.64 fully amortised, no capitalised IP), current tax assets (L160). Template carries no exceptional-items or discontinued-operations line at all. Full 27-item table in Section 4. |
| A3-03 | F2 | R079-R084 vs R364-R369; R001-R006 vs R286-R291 | L115, L301 | "7 Profit for the period (5-6) \| 867.73" / "7 Profit for the period (5-6) \| 540.44" | FORWARD-SIGNAL | Subsidiary PAT (consol less standalone, computed) 327.29 = 60.6% of standalone PAT vs 33.6% in Q2 FY26: widened 27.0 pp YoY, 30.4 pp vs FY26 (30.2%). Subsidiary revenue 2,920.29, +54.3% YoY and +19.6% QoQ, vs standalone +10.6% YoY and +0.2% QoQ. Subsidiaries now 39.8% of consolidated revenue (32.2% Q2 FY26). The earnings centre is migrating to the US perimeter, which this filing never breaks out by entity. |
| A3-04 | F2 | R019-R030, R043-R048 vs R304-R315, R328-R333 | L105, L291 | "b) Employee benefits expense \| 3,952.35 \| 3,733.58" / "\| 2,149.64 \| 2,142.60" | AMBIGUOUS | Subsidiary EBITDA (computed) 60.02 Q1 to 326.61 Q2 (margin 2.5% to 11.2%) while standalone EBITDA fell 511.87 to 482.26 (11.63% to 10.94%). Two readings: real US operating leverage, or a transfer-pricing shift that moves margin from parent to sub. Separating observation: intercompany revenue and the sub's own external revenue, both NOT DISCLOSED here. A4 question. |
| A3-05 | F2 | R007-R012 vs R292-R297; R218, R230-R231 vs R489, R497-R498 | L101, L212, L391 | "2 Other income \| 473.23 \| 818.55 \| 794.68" | AMBIGUOUS | Consolidated other income fell 42.2% QoQ. Subsidiary other income (computed) 435.07 Q1 to 133.12 Q2, while subsidiary-held investments rose (A3-01). Subsidiary fair-value gain on investments 155.23 H1 FY26 (L212 264.50 less L391 109.27) to nil H1 FY27 (18.69 both lines). A change in how the sub's T-bill book is measured is possible; not stated. A4 question: what made Q1 sub income 435.07, and was the treasury book reclassified. |
| A3-06 | F2 | R156-R157 vs R429-R430; R236, R503; R248 vs R515 | L337, L395 | "(ii) Trade receivables \| 1,010.43 \| 3,035.28" | AMBIGUOUS | Standalone receivables fell 2,024.85 (66.7%) while consolidated receivables stayed flat (3,447.70 vs 3,472.50, L155). Standalone OCF 4,146.63 exceeds consolidated OCF 2,826.32 (L401, L222). Two readings: the sub settled intercompany dues to the parent (cash round-trip with the 4,113.13 injection, A3-01), or billing moved from parent to sub. Use consolidated OCF as the clean cash number. A4 question. |
| A3-07 | F6 | R640-R642, R737-R738 | L435 | "would provide appropriate accounting effect on the basis of such developments as needed" | FORWARD-SIGNAL | Open, undated, unquantified future charge to Employee Benefits Expense once Central/State Labour Code rules are final. Feeds Role 5 tracker and FTTCP catalyst timeline as a margin risk with no date. |
| A3-08 | F8 | R073-R078, R358-R363, R061-R072, R184-R185 | L114 | "c) Tax adjustments for earlier years \| (0.18) \| 7.41 \| - \| 7.23 \| - \| (2.26)" | NEUTRAL-FACT | Non-zero earlier-year adjustments: 7.41 Q1, (0.18) Q2, 7.23 H1 (0.30% of H1 PBT). Standalone is nil in all FY27 periods (L300), so FY27 adjustments sit in subsidiaries. ETR consolidated 24.83% Q2, 34 bps under 25.17%; standalone 24.59%, 58 bps under. No persistent deferred-tax credits: subsidiary deferred-tax charges 33.97 / 44.47 / 37.53 per quarter (computed) build DTL 235.72 to 326.47 (L174). That is tax deferred at the sub, not a DTA shield, so no ETR step-up risk. |
| A3-09 | F9 | R085-R096, R370-R381 | L118, L304 | "a Remeasurement of the net defined benefit liabilities \| - \| - \| (16.81) \| - \| (33.62) \| 33.30" | AMBIGUOUS | FY26 booked a straight-line quarterly remeasurement loss (16.81 a quarter, 33.62 H1). The full year closed at a 33.30 gain, so H2 FY26 carried +66.92 (computed): twice the FY26 net and a sign flip. That points to a year-end assumption change (discount rate, or the Labour Code wage definition in Note 5). FY27 books nil in both quarters, a change in interim practice. Verify actuarial assumptions at the FY26/FY27 Annual Report. |
| A3-10 | F10 | R115-R120, R174-R175, R268-R271, R537-R539, R579-R582, R124-R135, R397-R408 | L124, L235 | "10 Paid up equity share capital ... \| 3,038.06 \| 3,028.06 \| 3,113.06" | NEUTRAL-FACT | Capital fell 85.00 in Q1 FY27 (8,50,000 shares, computed). That ties to the buyback outflow 1,498.00 at L235 (about Rs 176.24 a share including costs, computed). Capital rose 10.00 in Q2 = Note 3 ESOP 1,00,000 shares; proceeds 47.60 (L234), about Rs 47.60 a share including premium (computed). No note in this filing describes the buyback (size, price, dates). Basic-diluted spread 0.00 to 0.02 in all periods, 0.00 in Q2 FY27: no new dilutive instruments. Closing count 3,03,80,600 shares (computed). Q2 EPS +2.9% YoY on PAT +0.3%. |
| A3-11 | F11 | R176-R177, R447-R448, R196-R197, R467-R468, R109-R114, R382-R387 | L348, L364 | "(b) Other equity \| 10,337.53 \| 11,793.41" / "(iv) Other financial liabilities [current] \| 1,420.33 \| 124.47" | AMBIGUOUS | Statutory tie holds (Section 5). Roll-forward of Other equity: opening + H1 TCI less buyback premium and costs (1,413.00) + ESOP premium (37.60) leaves an unexplained debit of 1,215.22 standalone and 1,215.24 consolidated (computed). That is 10.3% of opening standalone Other equity and 9.1% of standalone net worth. Standalone other financial liabilities (current) rose 1,295.86. Standalone liability movements exceed the cash-flow working-capital line (L397, 275.09) by 1,217.83 (computed), so about 1,215 sits outside OCF. The gap equals Rs 4.00 x 3,03,80,600 shares to the lakh (computed). Leading candidate [INFERENCE]: FY26 final dividend appropriated and unpaid at 30-Sep; neither half-year cash flow shows a dividend line (L233-L237). Other candidates: ESOP reserve and buyback reserve entries. If it is a dividend, about 1,215 of cash leaves in Q3 FY27. Dividend NOT DISCLOSED in this filing. A4 question. |
| A3-12 | F12 | R160-R161, R148-R149, R258-R261, R433-R434, R421-R422 | L157, L149 | "(iv) Bank balances other than (iii) above \| 538.30 \| 3,771.62" | AMBIGUOUS | Single segment (Note 4), so the group balance sheet is the segment. Bank balances fell 3,233.32; net FD run-off was only 993.63 (L228-L229). The other 2,239.69 is consistent with long-dated deposits moved into non-current other financial assets (+1,747.46, L149) [INFERENCE]; 492.23 untraced (computed). A4 question: maturity reclass or lien/escrow (buyback)? |
| A3-13 | F12 | R031-R036, R316-R321, R180-R181, R190-R191 | L106 | "c) Finance costs \| 46.48 \| 41.31 \| 22.75" | AMBIGUOUS | Finance cost 2.0x YoY while borrowings went to nil (L178) and lease liabilities fell 448.41 to 402.05 (computed). Nearly all of it is in the parent (44.98, L292). Its source is not explained: interest on tax, on other financial liabilities, or reclassified bank charges. A4 question. |
| A3-14 | F12 | R240-R249, R192-R199 | L218 | "Increase in trade payables, other financial liabilities and other liabilities \| 1,112.60 \| 752.33" | AMBIGUOUS | Working-capital release 1,305.74 = 94.6% of H1 consolidated EBITDA 1,380.76 (computed). OCF/PAT is 1.56x. Non-MSE trade payables rose 538.39 (L182) while MSE payables fell 79.65 (L181). Other current liabilities rose 337.36 (L184). A payables stretch or advance billing can reverse in H2. Treat H1 OCF as flattered until H2 confirms. |
| A3-15 | F14 | R735, R581-R582 vs R115, R388 | L432 | "the equity share capital of the Company stands increased to Rs. 10,00,000 comprising of 1,00,000 equity shares" | NEUTRAL-FACT | Note 3 states the allotment as if it were total capital. Paid-up is 3,038.06 lakh (L124, L307). Drafting error in a note the board approved. |
| A3-16 | F14 | R652, R711 | L199 | "For the Half Year ended 31-09-2025" | NEUTRAL-FACT | Invalid date in the consolidated cash-flow header. The standalone header reads 30-09-2025 (L380). |
| A3-17 | F14 | R103-R108 | L122 | "b Income tax relating to items that will not be reclassified to profit and loss [reclassified block; caption as printed]" | NEUTRAL-FACT | The caption under "Items that will be reclassified" (L120) says "will not". Template caption error. |
| A3-18 | F14 | R734, R625-R627 vs R609-R611, R700 | L431 vs L73 | "CyberTech Systems and Software Inc. USA, along with its subsidiary CyberTech Systems and Software, Canada Inc." / "following wholly owned subsidiaries" | NEUTRAL-FACT | Note 2 shows Canada as a step-down of the USA entity. The auditor lists three WOS with no hierarchy. Both can be true. The holding chain matters for which entity received the 4,113.13 (A3-01). |
| A3-19 | F14 | R737, R640, R687-R688 | L434 | "Considering the materiality nature of this impact, the Company has presented such incremental impact under \"Employee Benefits Expense\" ... for the year ended March 31, 2026" | AMBIGUOUS | The sentence does not say whether the impact is material, and no amount is given. A restructure effective 1-Apr-2026 is presented in the FY26 P&L. The note carries FY26 wording into a Q2 FY27 filing with no FY27 update. A4 question: amount booked in FY26, and any FY27 run-rate effect inside EBE. |
| A3-20 | F14 | R210 vs R058; R483 vs R325; R492 vs R320; R559 vs page-3 letterhead | L201 vs L110; L384 vs L293; L388 vs L292; L20 vs L96 | "Profit before tax \| 2,415.95" / "\| 2,415.96" | NEUTRAL-FACT | Rounding differences of 0.01 between cash flow and P&L (PBT, standalone D&A, standalone finance cost H1 FY26). Telephone differs: L20 "+91 226983-9200" vs L96 "+91 22-4283-9200". Each is immaterial. Together with A3-15 to A3-17 they are a governance data point on document control. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | 45 dash cells in 27 items read (Section 4). The live WOS investment (A3-01) and the nil borrowings line (A3-02) carry forward weight. No exceptional or discontinued template line exists. |
| F2 | FINDING | Subsidiary PAT gap 60.6% of standalone PAT vs 33.6% YoY (+27.0 pp > 5 pp threshold). No JV or associate, so the whole gap is subsidiaries net of eliminations (Section 3). A3-03 to A3-06. |
| F3 | PASS | Subsidiaries carry their own cost base: Q2 employee cost 1,802.71 (45.6% of consolidated), outsourced 401.22, D&A 20.43 (computed). No shells in aggregate. Entity-level split NOT DISCLOSED. No Going Concern EoM to reconcile. |
| F4 | PASS | L73 "the same are reviewed by us": all three WOS reviewed by the statutory auditor. Unreviewed contribution 0% of PAT. No prior period for trend (first run). |
| F5 | PASS | No EoM, Other Matter or Going Concern paragraph in either review report (L65-L89, L255-L275). No prior-quarter text to verbatim-diff (first run); baseline recorded as "none". |
| F6 | FINDING | Lexicon hits L46 "Commenced" (procedural) and L120 "will be" (caption), neither a commitment. Note 5 carries one completed and one open undated commitment (A3-07). Register in Section 6. |
| F7 | PASS | Zero hedge-lexicon hits in the notes ("subject to", "evaluating", "exploring", "in discussions", "endeavour", "no assurance", "may sometimes", "could have an effect"). Note 5 "continues to monitor" is captured under F6. A newly added hedge cannot be tested with no prior quarter. |
| F8 | FINDING | Earlier-year tax adjustments non-zero (A3-08). ETRs 23.88% to 24.88% across periods, all under 25.17%. No DTA shield. |
| F9 | FINDING | H2 FY26 remeasurement +66.92 vs FY26 net 33.30, sign flip; FY27 interim remeasurement nil (A3-09). FCTR swing Q1 to Q2 is 242.84, under FY26 FCTR 866.80; no finding on FCTR. |
| F10 | FINDING | Capital changes trace to the buyback (Q1) and the ESOP (Q2); the buyback is undisclosed in notes. Basic-diluted spread narrow and narrowing (A3-10). |
| F11 | FINDING | Tie holds: 3,038.06 + 17,534.67 = 20,572.73 (L166-L168); 3,038.06 + 10,337.53 = 13,375.59 (L347-L349). No third-party number in context. The roll-forward leaves a 1,215.22 debit, over 5% of Other equity (A3-11). |
| F12 | FINDING | Single segment (L433), so the group balance sheet is the proxy. Bank-balance reclass, finance cost with nil debt, and the WC release are all ambiguous (A3-12 to A3-14). |
| F13 | PASS | One agenda item: results (L36-L40). No AR, AGM, dividend, director term or enabling resolution. "inter-alia" is boilerplate (A2 AGENDA_NOT_LISTED read, no item found). A2 SIGNATURE_BEFORE_MEETING_CLOSE read: review reports signed 20:04:40 / 20:05:15 (L269, L83), result pages 20:20:36 to 20:23:06, close 20:30 (L46), CS letter 20:45:14 (L51). That is the ordinary approve-then-sign order inside the meeting window, not an anomaly. |
| F14 | FINDING | Note 3 capital misstatement, invalid header date, OCI caption error, Note 2 vs auditor hierarchy wording, Note 5 materiality wording, rounding and telephone mismatches (A3-15 to A3-20). Results labelled "Un-audited" match the auditor's "limited review" (L37, L65, L255): no audit-vs-review mismatch. |
| F15 | PASS | No prior consolidation list exists (first run), so no diff is possible. Baseline recorded: CyberTech Systems and Software Inc. USA, Spatialitics LLC (USA), CyberTech Systems and Software Canada Inc. (L74-L76, L431). The intra-document lists agree on the same three entities; the wording difference is logged under F14 A3-18. |
| F16 | N.A. | Results doctype; presentation-only check. |
| F17 | N.A. | Results doctype, no transcript. No Notion monitoring checklist exists for CYBERTECH (none supplied). Silence audit not runnable. |

## 3. F2 DECOMPOSITION (computed; subsidiary = consolidated less standalone; no JV/associate)

| period | sub revenue | sub % of consol rev | sub EBITDA | sub EBITDA margin | sub other income | sub PBT | sub PAT | sub PAT % of SA PAT |
|---|---|---|---|---|---|---|---|---|
| Q2 FY27 | 2,920.29 | 39.8% | 326.61 | 11.2% | 133.12 | 437.80 | 327.29 | 60.6% |
| Q1 FY27 | 2,442.45 | 35.7% | 60.02 | 2.5% | 435.07 | 473.59 | 353.42 | 59.5% |
| Q2 FY26 | 1,892.26 | 32.2% | 45.05 | 2.4% | 276.11 | 288.62 | 217.73 | 33.6% |
| H1 FY27 | 5,362.74 | 37.8% | 386.63 | 7.2% | 568.19 | 911.39 | 680.71 | 60.0% |
| H1 FY26 | 3,749.43 | 32.1% | 196.93 | 5.3% | 583.14 | 739.88 | 553.67 | 49.0% |
| FY26 | 7,676.50 | 32.4% | 284.44 | 3.7% | 733.90 | 937.02 | 706.04 | 30.2% |

EBITDA = revenue less outsourced, employee and other expenses (L100-L108, L286-L294). Consolidated EBITDA Q2 FY27 808.87 (11.0%) vs 461.92 (7.9%) Q2 FY26, +75.1%. Standalone 482.26 (10.9%) vs 416.87 (10.5%). Consolidated PBT less other income: 681.20 vs 345.66, +97.1%; other income share of PBT 41.0% vs 69.7%. Gap trend: sub PAT share of SA PAT +27.0 pp YoY, +1.1 pp QoQ, +11.0 pp H1-on-H1. FINDING threshold (5 pp) breached on YoY and H1.

Sub PBT quality: Q1 FY27 92% from other income; Q2 FY27 75% from EBITDA (computed). Sub ETR Q2 25.24%, Q1 25.37% (computed).

## 4. F1 ZERO_STANDING TABLE (27 items, 45 cells)

| line | item | dash cells | transaction class anticipated | read |
|---|---|---|---|---|
| L114 | consol tax adj earlier years | Q2FY26, H1FY26 | assessment true-ups | live in FY27 (A3-08) |
| L118 | consol remeasurement DBO | Q2, Q1, H1 FY27 | actuarial valuation | practice change (A3-09) |
| L119 | consol OCI tax, not-reclass | Q2, Q1, H1 FY27 | tax on remeasurement | follows L118 |
| L122 | consol OCI tax, reclass block | all 6 | tax on FCTR | never used; caption error (A3-17) |
| L145 | consol intangibles | Sep-26 | capitalised software / IP | 0.64 fully amortised; no capitalised IP |
| L147 | consol NC investments | Sep-26 | long-dated bonds/funds | 701.16 moved to current at parent (A3-01 tie) |
| L160 | consol current tax assets | Sep-26 | tax refunds | net liability position |
| L178 | consol borrowings | Sep-26 | WC lines | repaid (A3-02) |
| L205 | consol loss on disposal | H1FY27 | asset sales / write-offs | nil |
| L208 | consol ECL provision | H1FY27 | credit losses | nil; 0.05 reversal L210 |
| L209 | consol credit balances written back | H1FY27 | stale payable reversals | nil |
| L210 | consol ECL reversal | H1FY26 | provision release | 0.05 in FY27 |
| L225 | consol PPE sale proceeds | H1FY27 | asset sales | nil |
| L234 | consol ESOP proceeds | H1FY26 | option exercise | 47.60 live (A3-10) |
| L235 | consol buyback | H1FY26 | capital return | 1,498.00 live (A3-10) |
| L300 | SA tax adj earlier years | 5 of 6 | assessment true-ups | only FY26 (2.26) |
| L304 | SA remeasurement | Q2, Q1, H1 FY27 | actuarial | as L118 |
| L305 | SA OCI tax | Q2, Q1, H1 FY27 | tax on remeasurement | as L119 |
| L327 | SA intangibles | Sep-26 | capitalised IP | as L145 |
| L359 | SA borrowings | Sep-26 | WC lines | as L178 |
| L386 | SA loss on disposal | H1FY27 | asset sales | nil |
| L389 | SA ECL reversal | H1FY26 | provision release | 0.05 in FY27 |
| L404 | SA PPE sale proceeds | H1FY27 | asset sales | nil |
| L405 | SA investment in WOS | H1FY26 | subsidiary capitalisation / acquisition funding | 4,113.13 live (A3-01) |
| L406 | SA purchase of investments | H1FY26 | treasury deployment | 30.00 live |
| L407 | SA sale of investments | H1FY26 | treasury liquidation | 379.78 live |
| L414 | SA ESOP proceeds | H1FY26 | option exercise | as L234 |

## 5. F11 ROLL-FORWARD (computed)

| | standalone | consolidated |
|---|---|---|
| Other equity 31-03-2026 | 11,793.41 (L348) | 18,116.94 (L167) |
| + H1 FY27 TCI | 1,134.74 (L306) | 2,008.37 (L123) |
| less buyback beyond face value (1,498.00 less 85.00) | (1,413.00) | (1,413.00) |
| + ESOP premium (47.60 less 10.00) | 37.60 | 37.60 |
| expected 30-09-2026 | 11,552.75 | 18,749.91 |
| filed 30-09-2026 | 10,337.53 (L348) | 17,534.67 (L167) |
| unexplained debit | (1,215.22) | (1,215.24) |

Cross-check: standalone liability movements (MSE -79.65, other creditors +441.14, OFL current +1,295.86, OFL non-current -104.85, other current liabilities -161.88, provisions +102.30) sum to 1,492.92, against the WC line 275.09 (L397). The residual is 1,217.83. Candidate reconciling items: (1) declared, unpaid FY26 dividend (gap = Rs 4.00 x 3,03,80,600 shares); (2) share-based payment reserve movements; (3) capital redemption reserve transfer (net zero inside Other equity, so not a candidate for the gap). None is disclosed.

## 6. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Restructure employee compensation consistent with the four Labour Codes; impact assessed and presented in EBE for FY26 | effective 1-Apr-2026 | Note 5, L434 | completed |
| Provide accounting effect on finalisation of Central/State Labour Code rules | undated; on rule finalisation | Note 5 para 2, L435 | initiated |
| ESOP allotment 1,00,000 shares (corporate action, no commitment language) | quarter ended 30-Sep-2026 | Note 3, L432 | completed |

Not in any note: the Q1 FY27 buyback (L235, completed, undisclosed in notes) and the 4,113.13 WOS investment (L405, purpose undisclosed). Both feed A4 questions.

## 7. A4 HAND-OFF (FORWARD-SIGNAL and AMBIGUOUS ids)

FORWARD-SIGNAL: A3-01, A3-03, A3-07. AMBIGUOUS: A3-04, A3-05, A3-06, A3-09, A3-11, A3-12, A3-13, A3-14, A3-19.

```yaml
stage: A3-forensics
company: "CYBERTECH"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/cybertech-q2fy27/work/forensics_results_cybertech_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "L405", classification: "FORWARD-SIGNAL", implication: "Parent injected 4,113.13 into an unnamed WOS; subs bought 3,263.77 of investments (computed); 95.1% of group current investments now offshore; purpose undisclosed (acquisition vs parking)"}
  - {id: "A3-02", check: "F1", line: "L178", classification: "NEUTRAL-FACT", implication: "Borrowings nil at 30-Sep-2026 (377.23 repaid); no exceptional/discontinued template lines"}
  - {id: "A3-03", check: "F2", line: "L115, L301", classification: "FORWARD-SIGNAL", implication: "Sub PAT 60.6% of SA PAT vs 33.6% YoY (+27.0 pp); sub revenue +54.3% YoY vs SA +10.6%; earnings centre migrating to US perimeter"}
  - {id: "A3-04", check: "F2", line: "L105, L291", classification: "AMBIGUOUS", implication: "Sub EBITDA 60.02 to 326.61 QoQ while SA EBITDA fell; real leverage vs transfer-pricing shift"}
  - {id: "A3-05", check: "F2", line: "L101, L212, L391", classification: "AMBIGUOUS", implication: "Consol other income -42.2% QoQ; sub other income 435.07 to 133.12 despite larger book; sub FV gain line 155.23 to nil"}
  - {id: "A3-06", check: "F2", line: "L337, L395", classification: "AMBIGUOUS", implication: "SA receivables -66.7% while consol flat; SA OCF 4,146.63 > consol 2,826.32; intercompany round-trip or billing shift"}
  - {id: "A3-07", check: "F6", line: "L435", classification: "FORWARD-SIGNAL", implication: "Undated, unquantified future EBE charge on final Labour Code rules"}
  - {id: "A3-08", check: "F8", line: "L114", classification: "NEUTRAL-FACT", implication: "Earlier-year tax adj 7.23 H1 in subs; ETR 24.83% vs 25.17%; sub deferred-tax charges build DTL, no DTA shield"}
  - {id: "A3-09", check: "F9", line: "L118, L304", classification: "AMBIGUOUS", implication: "H2 FY26 remeasurement +66.92 vs FY26 net 33.30 (sign flip); FY27 interim remeasurement nil; verify assumptions at AR"}
  - {id: "A3-10", check: "F10", line: "L124, L235", classification: "NEUTRAL-FACT", implication: "Capital -85.00 Q1 (buyback 1,498.00, undisclosed in notes), +10.00 Q2 (ESOP); basic-diluted spread 0.00-0.02, narrowing"}
  - {id: "A3-11", check: "F11", line: "L348, L364", classification: "AMBIGUOUS", implication: "Other equity roll-forward leaves 1,215.22 debit (= Rs 4.00 x 3,03,80,600 shares, computed) outside OCF; candidate unpaid FY26 dividend, Q3 cash outflow"}
  - {id: "A3-12", check: "F12", line: "L157, L149", classification: "AMBIGUOUS", implication: "Bank balances -3,233.32 vs net FD run-off 993.63; 2,239.69 likely reclassified to non-current; 492.23 untraced; lien/escrow?"}
  - {id: "A3-13", check: "F12", line: "L106", classification: "AMBIGUOUS", implication: "Finance cost 2.0x YoY with borrowings nil and leases falling; source unexplained"}
  - {id: "A3-14", check: "F12", line: "L218", classification: "AMBIGUOUS", implication: "WC release 1,305.74 = 94.6% of H1 EBITDA; OCF/PAT 1.56x on payables and other liabilities; H2 reversal risk"}
  - {id: "A3-15", check: "F14", line: "L432", classification: "NEUTRAL-FACT", implication: "Note 3 states capital as Rs 10,00,000 vs paid-up 3,038.06 lakh"}
  - {id: "A3-16", check: "F14", line: "L199", classification: "NEUTRAL-FACT", implication: "Invalid date 31-09-2025 in consolidated cash-flow header"}
  - {id: "A3-17", check: "F14", line: "L122", classification: "NEUTRAL-FACT", implication: "OCI reclassified-block caption reads 'will not be reclassified'"}
  - {id: "A3-18", check: "F14", line: "L431 vs L73", classification: "NEUTRAL-FACT", implication: "Note 2 shows Canada as step-down of USA entity; auditor lists three WOS flat"}
  - {id: "A3-19", check: "F14", line: "L434", classification: "AMBIGUOUS", implication: "Note 5 materiality unstated, amount unquantified, FY26 wording carried into Q2 FY27"}
  - {id: "A3-20", check: "F14", line: "L201 vs L110; L384 vs L293; L388 vs L292; L20 vs L96", classification: "NEUTRAL-FACT", implication: "0.01 rounding mismatches and telephone mismatch; cumulative document-control data point"}
forward_signals: ["A3-01", "A3-03", "A3-07"]
ambiguous: ["A3-04", "A3-05", "A3-06", "A3-09", "A3-11", "A3-12", "A3-13", "A3-14", "A3-19"]
commitments:
  - {commitment: "Restructure employee compensation per four Labour Codes; impact presented in FY26 EBE", implied_date: "2026-04-01 effective", ref: "Note 5, L434", status_word: "completed"}
  - {commitment: "Provide accounting effect on finalisation of Central/State Labour Code rules", implied_date: "undated", ref: "Note 5 para 2, L435", status_word: "initiated"}
  - {commitment: "ESOP allotment of 1,00,000 shares", implied_date: "quarter ended 2026-09-30", ref: "Note 3, L432", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Operating engine improved while headline PAT stalled. Consolidated EBITDA 808.87 vs 461.92 YoY (+75%), but other income fell 42% QoQ, so PAT rose only 0.3% YoY. Growth sits in the US subsidiaries: sub revenue +54% YoY, sub EBITDA 60.02 to 326.61 QoQ. Real leverage vs transfer pricing is the first question (A3-04). Treasury is moving offshore. The parent put 4,113.13 into an unnamed WOS and the subs bought 3,263.77 of investments (exact tie, computed). Acquisition and parking readings separate on what the sub does with that cash in Q3. Other equity leaves a 1,215.22 debit that equals Rs 4.00 on 3,03,80,600 shares and sits outside OCF. A declared, unpaid FY26 dividend is the leading candidate; this filing does not confirm it. Parent OCF is flattered by a 2,025 receivable fall that consolidated receivables do not show, so use consolidated OCF. A1 defect: R123/R396 label FY26 year-end other equity as Q2 FY26 (fulltext L125/L308 put it in the FY26 column)."
```
