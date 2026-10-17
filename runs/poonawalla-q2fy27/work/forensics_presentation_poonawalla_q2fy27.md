# A3 FORENSIC NOTES: POONAWALLA Q2FY27 (doctype: presentation, investor deck, 42 slides)

Agent: A3 forensic notes | model: claude-opus-5-5 | date: 2026-10-17
Inputs read: A1 structured (R001-R676, all rows), A1 fulltext (lines 1-1341, all lines), A2 ledger (676 IDs).
Not read: source PDF, inputs/. Prior-quarter fulltext: ND. Notion checklist: NOT SUPPLIED (pre-thesis read, no companies/ file, no spear).
Lender (NBFC). Orchestrator rule 12 applied: F4/F5 have no auditor or EoM text in a deck (N.A.). F12 is run in a lender form: stage buckets, product book and ALM buckets serve as the "segments".

## RECONCILIATION
- Ledger IDs: 676. Structured IDs: 676. Orphans: none. Rows read at cited line: 676 of 676 (100%).
- A2 flags checked: 9 ZERO_STANDING (all in the F1 register below), RESTATED cross-refs (R019/R026, R022/R034/R036, R028/R040, R029/R675, R037/R609; all consistent), ENTITY_CHANGE candidate R572 (Balance Book discontinued; prior ND), FOOTNOTE_UNRESOLVED R591-R598, R601 (left unresolved per task).
- Arithmetic tie-outs done (all pass within Rs 1 cr rounding): P&L slide 26 (NII, NII incl fees, PPoP, PBT, PAT, three periods); Balance Sheet slide 27 (assets = liabilities, three dates); Stage 1+2+3 = 70,516 vs Loans 69,563 + derived ECL 946 = 70,509; Stage %, GNPA %, NNPA %, PCR recomputed; AI project table (143 total, 84 delivered); shareholding sums to 100.00% both dates; headline growth rates (AUM, NII, PPoP, PAT) recomputed.
- Unresolved chart mappings named in the task (borrowing mix R191-R225, ALM inflow/outflow R231-R250, collection efficiency R337-R348, vintage R349-R356, PBT/PAT Q3-Q4 R176-R179/R377-R380) were NOT resolved and NOT used in any finding.

## FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F1 | R399, R400, R401, R393-R395 | L806 / s26 | "Net gain on derecognition of financial instruments         -        51       35" | AMBIGUOUS | Q2 carried no derecognition gain (Q1 Rs 51 cr, Q2FY26 Rs 35 cr). Two readings: assignment / co-lending sell-down paused (more on-book growth, faster re-levering) or a policy shift to hold. Derived off-book gap (AUM minus Stage 1+2+3 book) fell from Rs 4,018 cr (Jun-26) to Rs 3,492 cr (Sep-26) [DERIVED from R136/R137, R280/R285/R315, R281/R286/R316], yet servicing income rose Rs 70 cr to Rs 91 cr (L803). Bull side: Q1 PBT ex-derecognition was Rs 360 cr, so Q2 PBT Rs 501 cr is +39% QoQ on that basis versus the 21.8% headline. A4 question: why no sell-down in Q2, and what drives servicing income if the off-book pool shrank? |
| FN-02 | F1 | R029, R675 | L124 / s6 | "No accelerated write-off during the quarter" | AMBIGUOUS | The line exists because accelerated write-offs are a known transaction class for this book. The deck states only that none was "accelerated"; normal write-off amount is NOT DISCLOSED. GNPA fell Rs 18 cr QoQ (863 to 845, L713) on that basis. A4 question: Q2 gross slippages, normal write-offs and recoveries in Rs cr. See FN-10. |
| FN-03 | F1 | R093, R094, R660, R060 | L344 / s13; L207 / s8 | "Shopkeeper ... 1                      0%" | AMBIGUOUS | Shopkeeper Loan is one of the six new products (L207) from the FY25 launch cohort ("Launched 6 new products", L283), yet AUM is Rs 1 cr at 30-Sep-2026. Pilot, paused or re-scoped? It is inside the "28% of total disbursement" new-product definition (L206-207). A4 question. |
| FN-04 | F6 | R609, R610, R037, R067 | L156 / s7; L297-301 / s12 | "We seek to continue growing our AUM at ~35- 40% CAGR over the next couple of years" / "Aspiration for 5-6x AUM over next 5 years" | FORWARD-SIGNAL | 5x in 5 years needs 38.0% CAGR; 6x needs 43.1% [arithmetic]. The aspiration sits at or above the top of the two-year guidance band, so it needs growth to hold or accelerate in years 3-5 on a larger base. No credit-cost, RoA or leverage guidance is paired with the growth guidance. Feeds Role 5 promise tracker. |
| FN-05 | F11 | R036, R022, R444-R446, R450-R455, R012, R035 | L154 / s7; L836, L840, L842 / s27 | "Post capital raise debt to equity ratio stands at 4.30x as on 30th September 2026" | FORWARD-SIGNAL | Book net worth (Share Capital + Reserves) Rs 13,703 cr Sep-26 vs Rs 13,060 cr Jun-26 (+Rs 643 cr); borrowings +Rs 8,999 cr in the same quarter. D/E recomputes to 3.82x Jun-26 and 4.30x Sep-26 [58,865 / 13,703]. Annualised Q2 PAT Rs 1,500 cr on average net worth about Rs 13,382 cr gives about 11% RoE [DERIVED]; internal accrual of about 11% a year cannot fund 35-40% AUM CAGR at constant leverage. The QIP (Rs 2,500 cr, April-26, L148-150) gave back about one quarter of leverage headroom. Implication: another equity raise, leverage above the Mar-26 peak, or slower growth within roughly 12-18 months. CAR 18.68% (L129) gives the regulatory runway; Tier 1 split NOT DISCLOSED. |
| FN-06 | F11 | R030-R034 vs R445, R451, R454 | L147-152, L162 / s7; L836-842 / s27 | "4.67x" (L147) / "3.82x" (L151) / "Sep-25   Dec-25      Mar-26       Jun-26   Sep-26" (L162) | NEUTRAL-FACT (capture) | A1 maps R032 = 3.82x to Mar-26 and R033 = 4.67x to Jun-26 ("labels as extracted"). The slide 27 balance sheet gives Jun-26 D/E = 49,866 / (175 + 12,885) = 3.82x, and the text-layer column positions place 4.67x over Mar-26 and 3.82x over Jun-26. R032/R033 should not be used as mapped. Corrected reading (balance-sheet anchored): leverage peaked at Mar-26, fell after the April-26 QIP, and rose again to 4.30x within one quarter. A4/A5: anchor D/E to slide 27, not to R032/R033. |
| FN-07 | F10 | R450, R451, R453, R454, R012 | L840, L842 / s27 | "Share Capital ... 176 ... 175" / "Reserves & Surplus ... 13,527 ... 12,885" | AMBIGUOUS | Net worth rose Rs 643 cr QoQ against Q2 PAT of Rs 375 cr: a non-PAT equity addition of about Rs 268 cr [DERIVED], with share capital +Rs 1 cr (rounded). Candidate reconciling items: ESOP exercise premium, warrant conversion, share-based payment reserve, OCI / cash-flow hedge reserve, dividend (outflow). The deck carries no EPS, so basic vs diluted spread cannot be assessed. A4 question: what added about Rs 268 cr of equity in Q2? A4 to cross-check against known warrants / ESOPs. |
| FN-08 | F10 | R545, R546, R450, R452 | L1284-1285 / s40; L840 / s27 | "Promoter 59.01% (63.96%)" | AMBIGUOUS | Promoter share-capital units = 63.96% x 161 = 102.98 (Sep-25) vs 59.01% x 176 = 103.86 (Sep-26) [DERIVED]. Allowing Rs 0.5 cr rounding on each capital figure, the increase stays positive (+0.26 to +1.49). Promoter holding fell only through dilution; the promoter's absolute stake rose. Candidate causes: promoter warrant conversion, preferential allotment, market purchase. A4 cross-check against the filings record. MF holding nearly doubled, 6.04% to 11.75% (L1284-1287). |
| FN-09 | F12 | R302-R306, R282-R286, R297-R301 | L710 / s23; L692 / s23 | "Stage 2 PCR              23.63%  22.92%  18.97%  17.90%  14.61%" | FORWARD-SIGNAL | Stage 2 coverage fell in four consecutive quarters while Stage 2 assets rose Rs 577 cr to Rs 661 cr. Derived Stage 2 provision: about Rs 136 cr (Sep-25), Rs 116 cr (Jun-26), Rs 97 cr (Sep-26); a Rs 20 cr release in Q2 alone, while Stage 1 provision rose about Rs 84 cr (0.57% to 0.63%). Slide headline: "Adequately provisioned" (L692). Two readings: Stage 2 mix moved to secured / lower-LGD products, or ECL model recalibration supporting reported credit cost. The observation that separates them: product-level Stage 2 split and any ECL model-change note in the results filing. Lean bear. |
| FN-10 | F12 | R411, R412, R297-R321 | L811 / s26; L709-714 / s23 | "Credit cost                                              376       373      288" | AMBIGUOUS | Derived total ECL stock (Stage 1 + Stage 2 provision + GNPA - NNPA): Mar-26 ~Rs 839 cr, Jun-26 ~Rs 891 cr, Sep-26 ~Rs 946 cr. The stock rose about Rs 52-55 cr per quarter against P&L credit cost of Rs 373 cr and Rs 376 cr. That implies about Rs 320 cr per quarter of write-offs or other non-stock charges [DERIVED arithmetic identity, rounded PCRs; NOT a disclosed figure; write-offs NOT DISCLOSED]. If correct, about 1.9% of average loans is written off per year, and the falling GNPA ratio depends on normal write-offs. A4 question: Q2 write-offs, recoveries, and whether credit cost includes FLDG, off-book or other components. |
| FN-11 | F12 | R312-R316, R322-R326, R272, R019 | L713, L715 / s23; L695 / s23 | "Gross NPA (Stage 3)          711     785     818     863     845" | AMBIGUOUS | GNPA ratio fell 39 bps YoY (1.59% to 1.20%) while absolute GNPA rose 18.8% YoY (Rs 711 cr to Rs 845 cr). The stage book grew 57.6% (44,731 to 70,516) [DERIVED], so the denominator drives the ratio gain. The QoQ absolute fall (-Rs 18 cr) is the first in the series and coincides with FN-10. The slide frames this as "Sequentially improved asset quality" (L695). |
| FN-12 | F12 | R669, R118, R119, R073, R074, R098-R102 | L750 / s24; L381 / s14 | "6MoB 30+% is calculated for all retail loans excluding Mid Market and Gold Loans" | AMBIGUOUS | The vintage metric excludes Mid-market (15% of AUM, Rs 11,142 cr, Rs 20-50 cr tickets to "Well rated corporates and NBFCs", L380-382) and Gold (3%). The deck gives no product-level asset quality for any product, including Instant Consumer Loan (20% of AUM, 22-29% ROI, L358). Derived residual "Balance Book (discontinued) & Others" = Rs 362 cr (74,008 minus product sum 73,646) [DERIVED; R572 / L394]. A4 question: GNPA and credit cost by product, and wholesale NBFC exposure inside Mid-market. |
| FN-13 | F12 | R251-R260 (cumulative gap row, bucket-mapped), R432-R434, R187 | L644 / s21; L828 / s27; L651 / s21 | "Positive Gap       4,376  4,898  4,343  6,811  8,845  9,384  3,846  4,894  433  0" | AMBIGUOUS | The cumulative gap stays positive in every bucket. The bucket-level net from the cumulative row is -Rs 5,538 cr in 6-12m (9,384 to 3,846) and -Rs 4,461 cr in 3-5Y (4,894 to 433) [DERIVED]: concentrated liability maturities in Apr-Sep 2027 and in years 3-5. In the same quarter, Investments rose from Rs 814 cr to Rs 3,078 cr (+Rs 2,264 cr), about equal to the Rs 2,265 cr NCD raise (L651), and borrowings grew Rs 1,575 cr faster than loans. Reading: pre-funding (negative carry on Q3 NII) or a buffer for the 6-12m maturity wall. A4 question: what instruments mature in 6-12m, and what is the refinancing plan? The inflow/outflow chart mapping (R231-R250) was not used. |
| FN-14 | F16 | R226-R230, R603-R607 axis | L626-L630, L647 / s21 | "7.76%" (L627, column 65) / "7.72%" (L628, column 51) / "7.69%         7.65%       7.63%" (L629, columns 10/24/36) / axis "Q2FY26 ... Q2FY27" (L647, columns 10/24/36/51/65) | AMBIGUOUS | A1 maps cost of borrowing as falling, 7.76% (Q2FY26) to 7.63% (Q2FY27), "labels as extracted". The label column positions line up with the axis in the opposite order: Q2FY26 7.69%, Q3 7.65%, Q4 7.63%, Q1FY27 7.72%, Q2FY27 7.76%. That reading shows CoB rising 13 bps over the last two quarters. The A1 mapping of the D/E chart on this deck was wrong (FN-06), which weakens the A1 reading here. A rough cross-check (Q2 interest expense annualised over average endpoint borrowings, about 7.55-7.62%) does not settle it, because borrowings arrived late in the quarter. Lean bear: treat CoB direction as UNRESOLVED and possibly rising. A1 render check of slide 21 before A4/A5 use R226-R230. A4 question: Q1 and Q2 FY27 cost of borrowing, and marginal cost of new NCDs. |
| FN-15 | F16 | R149, R148, R154, R153, R405, R406, R402, R403, R011 | L119-121 / s6; L682 / s22; L809 / s26 | "PPOP expanded by 11.8% QoQ highlighting strong operating leverage" / "Ongoing Investment in Collections & Tech Infrastructure" | FORWARD-SIGNAL | Q2 opex grew 12.8% QoQ (631 to 712) against income growth of 12.3% (1,415 to 1,589). Opex/AUM rose 4.06% to 4.15% and cost-to-income rose 44.6% to 44.8%. The quarter showed slightly negative operating leverage; the slide 6 caption says the opposite. Slide 22 names the cause as "Ongoing" investment, which signals the opex ratio may not resume falling next quarter. |
| FN-16 | F16 | R058, R643, R057, R659, R023 | L279-282 / s12; L206 / s8; L116 / s6 | "Scaled new products to 24% of incremental disbursements as of Q4FY26" / "New products* disbursement contributed 28% to total disbursement" | AMBIGUOUS | The new-product metric changes basis across the deck: % of incremental disbursements (Q4FY26), % of total disbursement (Q2FY27), % of AUM (18%). The 24% and 28% figures are not comparable. Total disbursement is NOT DISCLOSED in Rs. A4 question: new-product share of total disbursement for Q4FY26 and Q1FY27 on the same basis, and total disbursement in Rs cr. |
| FN-17 | F16 | R062, R043, R044, R059, R612 | L285-286 / s12; L181 / s8; L281-283 / s12 | "12,500+ consumer-durable retailers" / "20,000+ dealer points across 360 locations as of September 2026" / "Scale priority businesses: >2x Consumer Durables franchise" | AMBIGUOUS | The consumer-durable reach metric changed name and unit between the FY26 phase box ("retailers") and Q2 ("dealer points"). The ">2x" scale target has no stated base (AUM, disbursement, or network) and no date. The 20,000 / 12,500 ratio (1.6x) cannot be read as progress against ">2x" until the base is defined. |
| FN-18 | F16 | R028, R040, R061 | L126-127 / s6; L175 / s8; L285 / s12 | "Successfully expanded Gold loan branches to 550 as on date" | NEUTRAL-FACT | The branch count is "as on date" (deck dated 09-Oct-2026, L67), not quarter-end, so post-quarter data sits inside Q2 highlights. FY26 phase box: "400 branches" (L285), with no statement whether these are gold-only. Gold AUM Rs 2,355 cr (L320) over 550 branches is about Rs 4.3 cr per branch [DERIVED]. Branches are ahead of the book: gold loan unit economics depend on branch seasoning. |
| FN-19 | F16 | chart axes, s21/s22/s24 | L626, L630, L645 / s21; L671, L686 / s22; L743 / s24 | "8.1%" / "7.6%" / "7.1%"; "3.80%"; "40.0%"; "96.0%" | NEUTRAL-FACT | Truncated axes: cost of borrowing 7.1-8.1%, opex/AUM from 3.80%, cost-to-income from 40.0%, collection efficiency from 96.0%. Small moves look large. A prior deck is not available to test whether the baselines changed. |
| FN-20 | F14 | R657, R605, R662, R115/R116, R658/R387 | L62 / s1; L1326, L1313 / s41; L394 / s14; L374 / s14; L134 vs L801 | "Classification \| INTERNAL" / "TL: Term Plan" / "CD: Continuous Deployment" / "September30, 2026" / "6 –- 60M" | NEUTRAL-FACT | Cumulative drafting slippage: (a) an exchange filing cover letter is stamped INTERNAL; (b) the glossary defines TL as "Term Plan", while TL means Term Loan in the borrowing legend "[NCD+ TL]" (L598); (c) CD is glossed as Continuous Deployment in a lender deck; (d) typos on the product table; (e) "NII" means Rs 1,589 cr (incl fees, L134) on slides 6/20/22 and Rs 1,380 cr on the P&L (L801). Disclosed by qualifier, but the headline 75.6% growth is on the fee-inclusive basis (core NII +80.6% YoY). Each item is immaterial; together they are a governance data point. |
| FN-21 | F14 | R599, R591-R598, R601 | L964-968 / s33; L946-955 / s32 | "Sunil Samdani                             Iyer" / "ED             Miranka" / "CFO" | NEUTRAL-FACT (capture) | R599 carries "Sunil Samdani ED & CFO". In the text layer, "CFO" (L968) sits in the column under "Sanjay Miranka" (L965-967), not under Sunil Samdani. A1 marks the role pairing unresolved. Do not use R599 roles for KMP tracking (who is CFO) until a render check is done. R591-R598 board title pairing is left unresolved, as instructed. |
| FN-22 | F17 | (silence table below) | deck-wide | "Total borrowings stood at ₹58,865 crore ... Liquidity stood at ₹6,526 crore, comprising cash, cash equivalents and undrawn bank lines" (L595) | AMBIGUOUS | The deck is silent on 9 of the 15 standard lender monitorables, or gives them in a form that cannot be used (table below). NIM / yield, write-offs, Tier 1, total disbursement and product-level asset quality are absent. The borrowing mix cannot be read (mapping unresolved). Silence count is 1 quarter (floor; prior deck ND). Each row is an A4 question. |

## F1 ZERO-STANDING REGISTER (all 9 A2 ZERO_STANDING rows)

| row | line | item | why the line exists / transaction class | disposition |
|---|---|---|---|---|
| R029 (=R675) | L124 | "No accelerated write-off" | accelerated write-off class used in prior periods; normal write-offs not disclosed | FN-02 |
| R094 | L344 | Shopkeeper Loan 0% of AUM (Rs 1 cr) | product launched in FY25 new-product cohort; still at pilot scale | FN-03 |
| R260 | L644 | cumulative positive gap >5Y = 0 | mechanical: cumulative inflows = cumulative outflows at the last bucket (78,860 both, L621) | no finding |
| R270 | L647 | cumulative gap % >5Y = 0% | same mechanical closure | no finding |
| R396 | L804 | Other Income Q2FY27 = 0 | catch-all miscellaneous income line; Q1FY27 had Rs 7 cr | no finding (NEUTRAL) |
| R398 | L804 | Other Income Q2FY26 = 0 | same | no finding |
| R399 | L806 | Net gain on derecognition Q2FY27 = "-" | assignment / co-lending sell-down gain class; Rs 51 cr Q1, Rs 35 cr Q2FY26 | FN-01 |
| R494 | L869 | AI projects delivered, Fraud Control Unit = 0 (of 3) | function pipeline row; fraud analytics named on slide 16 (L440-454) but no FCU AI project delivered | no finding (NEUTRAL; minor) |
| R496 | L871 | AI projects delivered, ORM = 0 (of 1) | same | no finding (NEUTRAL) |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | 9 zero-standing rows explained; derecognition gain nil (FN-01), write-off non-disclosure (FN-02), Shopkeeper stall (FN-03). |
| F2 | N.A. | Deck shows one basis only. The words standalone / consolidated appear nowhere in L1-1341, so no S-vs-C decomposition is possible. Basis question goes to A4 (FN-22 table). |
| F3 | N.A. | No standalone vs consolidated cost lines in a deck. |
| F4 | N.A. | No auditor report or Other Matters paragraph in a deck (lender rule 12 noted; doctype does not carry it). |
| F5 | N.A. | No Going Concern / EoM text in the deck; prior-quarter fulltext ND. |
| F6 | FINDING | Forward hits: "seek to" (L156), "Aspiration" (L297), "Projects Underway" (L860), "Implementing" (L1103), "Preparing for Scale" (L527). Guidance vs aspiration gap (FN-04). Register below. |
| F7 | PASS | Hedge hits ("subject to" L76, L88; "no assurance" L82) are disclaimer boilerplate on slide 3, not new note-level hedges. Whether any are new cannot be assessed (prior ND). |
| F8 | PASS | ETR 25.15% Q2FY27 (126/501), 25.30% Q1FY27 (104/411), 25.25% Q2FY26 (25/99), all at the 25.17% statutory rate. Deferred-tax split and earlier-year tax are not in the deck. |
| F9 | N.A. | Deck carries no OCI line. (OCI is one candidate for the Rs 268 cr non-PAT equity, FN-07.) |
| F10 | FINDING | Share capital 161 to 175 to 176 (QIP in Q1, +1 in Q2); about Rs 268 cr non-PAT equity in Q2 (FN-07); promoter absolute stake rose (FN-08); no EPS, so spread not assessable. |
| F11 | FINDING | NW tie-out passes on slide 27 and matches the 4.30x tile. Capital runway (FN-05). A1 D/E chart mapping conflicts with the balance sheet (FN-06). CAR 18.68% cannot be reconciled (RWA not disclosed). |
| F12 | FINDING | Lender form: Stage 2 PCR erosion (FN-09), derived write-off flow (FN-10), denominator-led GNPA ratio (FN-11), metric scope and product asset quality gap (FN-12), ALM 6-12m maturity concentration (FN-13). No reported segment assets/liabilities. |
| F13 | N.A. | No board meeting outcome, AR approval, AGM, enabling resolution or director term dates in a deck. Board roster only (s32); title pairing R591-R598 left unresolved. |
| F14 | FINDING | Drafting slippage (FN-20); capture caveat on R599 role pairing (FN-21). |
| F15 | N.A. | No consolidation / entity list in the deck; prior ND. Balance Book (discontinued) is a product, covered under FN-12. |
| F16 | FINDING | No prior deck, so dropped-metric diff is not assessable. Within-deck reframes and basis shifts: CoB direction (FN-14), operating-leverage claim (FN-15), new-product basis switch (FN-16), CD reach metric renamed (FN-17), post-quarter branch count (FN-18), truncated axes (FN-19). |
| F17 | FINDING | Notion checklist NOT SUPPLIED; silence audited against standard lender monitorables (table below, FN-22). |

## COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref | status word |
|---|---|---|---|---|
| C1 | Grow AUM at ~35-40% CAGR | "next couple of years": about FY27-FY29 (to ~Sep-2028) | L156-157, R609 | initiated |
| C2 | 5-6x AUM | "next 5 years": about FY31 | L297-301, R610 | initiated (aspiration) |
| C3 | >2x Consumer Durables franchise (base undefined) | "FY27 onwards", undated | L281-283, R612 | initiated |
| C4 | Gold Loan network expansion | FY27 onwards | L126, L175, L283-284 | underway (550 branches "as on date" 09-Oct-2026; 400 in FY26 box) |
| C5 | Digital Business Loans as a scale priority | FY27 onwards | L284-285, R612 | initiated |
| C6 | AI-powered consumer ecosystem | FY27 onwards | L290-295, R613 | initiated |
| C7 | AI projects: 59 underway, 42 new | undated | L859-860, R621 | underway (84 of 143 delivered; FY26 box 42 of 76, L299-301) |
| C8 | Collections GenAI voice bots, "Preparing for Scale" | undated | L525-532, R614 | underway (Collections AI 3 of 8 delivered, L874) |
| C9 | Email Bot rollout | undated | L1103 | underway ("Implementing") |
| C10 | Zero-Click HR ecosystem | undated | L1117-1118, R618 | initiated |
| C11 | Distribution franchise, growth corridors | undated | L1089-1107, R615/R616 | initiated |
| C12 | IIT Bombay research support | FY26-FY27 | L1241-1243, R620 | completed ("PFL supported") |
| C13 | QIP Rs 2,500 cr | April-26 | L148-150, R035/R639 | completed |

## F17 SILENCE AUDIT: WHAT WAS NOT DISCLOSED (checklist NOT SUPPLIED; standard lender monitorables)

| monitorable | deck status | ref | consecutive quarters silent |
|---|---|---|---|
| AUM | disclosed | L557 | - |
| Disbursement (total, Rs) | NOT DISCLOSED (new-product Rs 4,400+ cr and product run-rates only) | L182, L206 | 1 (floor; prior ND) |
| NIM / yield | NOT DISCLOSED | - | 1 |
| Cost of funds | disclosed; series direction disputed (FN-14) | L627-629 | - |
| Credit cost | disclosed | L697, L811 | - |
| GNPA / NNPA | disclosed | L713-716 | - |
| Stage 2 / Stage 3 | disclosed | L703-714 | - |
| ECL coverage | disclosed by stage | L709-711, L718 | - |
| Write-offs (Rs) | NOT DISCLOSED ("No accelerated write-off" only) | L124 | 1 |
| CRAR / Tier 1 | CAR 18.68% disclosed; Tier 1 NOT DISCLOSED | L129 | 1 |
| ALM | cumulative gap disclosed; inflow/outflow mapping unresolved | L644-647 | - |
| Borrowing mix | present but cannot be read (pie mapping unresolved) | L598-616 | 1 |
| Liquidity | Rs 6,526 cr disclosed; cash vs undrawn split and LCR NOT DISCLOSED | L595 | 1 |
| Product-level asset quality | NOT DISCLOSED (6MoB excludes Mid Market and Gold) | L750 | 1 |
| Off-book / co-lending / assignment pool | NOT DISCLOSED (derived only, FN-01) | L806 | 1 |
| Reporting basis (standalone / consolidated) | NOT STATED | deck-wide | 1 |
| Guidance on credit cost / RoA / leverage | NOT GIVEN (AUM growth only) | L156 | 1 |

## A4 HANDOFF (FORWARD-SIGNAL and AMBIGUOUS -> management questions)
FORWARD-SIGNAL: FN-04, FN-05, FN-09, FN-15.
AMBIGUOUS: FN-01, FN-02, FN-03, FN-07, FN-08, FN-10, FN-11, FN-12, FN-13, FN-14, FN-16, FN-17, FN-22.
Pipeline notes (not company findings): FN-06 and FN-14 show that A1 "labels as extracted" chart mappings on this deck can run in reverse period order. R032/R033 should not be used (anchor to slide 27). R226-R230 need a slide 21 render check before A4/A5 use them. FN-21: R599 roles are unreliable.

```yaml
stage: A3-forensics
company: "POONAWALLA"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/poonawalla-q2fy27/work/forensics_presentation_poonawalla_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "FN-01", check: "F1", line: "L806 (s26)", classification: "AMBIGUOUS", implication: "Derecognition gain nil in Q2 vs Rs 51 cr Q1; sell-down paused? derived off-book fell 4,018 to 3,492 while servicing income rose 70 to 91; core PBT +39% QoQ ex-derecognition vs 21.8% headline"}
  - {id: "FN-02", check: "F1", line: "L124 (s6)", classification: "AMBIGUOUS", implication: "Only 'no accelerated write-off' stated; normal write-offs, slippages, recoveries not disclosed"}
  - {id: "FN-03", check: "F1", line: "L344 (s13); L207 (s8)", classification: "AMBIGUOUS", implication: "Shopkeeper Loan (FY25 new-product cohort) at Rs 1 cr AUM; pilot, paused or re-scoped"}
  - {id: "FN-04", check: "F6", line: "L156 (s7); L297-301 (s12)", classification: "FORWARD-SIGNAL", implication: "5-6x AUM in 5 yrs needs 38-43% CAGR, at or above the 35-40% two-year guidance; no credit cost/RoA/leverage guidance paired"}
  - {id: "FN-05", check: "F11", line: "L154 (s7); L836-842 (s27)", classification: "FORWARD-SIGNAL", implication: "NW +Rs 643 cr vs borrowings +Rs 8,999 cr in Q2; D/E 3.82x to 4.30x in one quarter; ~11% RoE cannot fund 35-40% AUM CAGR; next equity raise likely within ~12-18 months"}
  - {id: "FN-06", check: "F11", line: "L147-152, L162 (s7); L836-842 (s27)", classification: "NEUTRAL-FACT", implication: "Capture: BS gives Jun-26 D/E 3.82x; A1 R033 maps 4.67x to Jun-26; do not use R032/R033 as mapped"}
  - {id: "FN-07", check: "F10", line: "L840, L842 (s27)", classification: "AMBIGUOUS", implication: "About Rs 268 cr non-PAT equity added in Q2 with share capital +1; ESOP/warrant/OCI; no EPS so dilution spread not assessable"}
  - {id: "FN-08", check: "F10", line: "L1284-1285 (s40); L840 (s27)", classification: "AMBIGUOUS", implication: "Promoter absolute share-capital units rose (102.98 to 103.86) despite QIP dilution; warrant conversion or purchase to verify"}
  - {id: "FN-09", check: "F12", line: "L710 (s23)", classification: "FORWARD-SIGNAL", implication: "Stage 2 PCR 23.63% to 14.61% over 4 quarters while Stage 2 assets rose; about Rs 20 cr Stage 2 release in Q2 supports flat credit cost"}
  - {id: "FN-10", check: "F12", line: "L811 (s26); L709-714 (s23)", classification: "AMBIGUOUS", implication: "Derived ECL stock +~Rs 55 cr vs credit cost Rs 376 cr implies ~Rs 320 cr/qtr write-offs or other charges (derived, undisclosed)"}
  - {id: "FN-11", check: "F12", line: "L713, L715 (s23)", classification: "AMBIGUOUS", implication: "GNPA Rs +18.8% YoY while ratio fell 39 bps; denominator-led improvement"}
  - {id: "FN-12", check: "F12", line: "L750 (s24); L381 (s14)", classification: "AMBIGUOUS", implication: "6MoB excludes Mid Market and Gold (18% of AUM); no product-level asset quality incl ICL 20% of AUM"}
  - {id: "FN-13", check: "F12", line: "L644 (s21); L828 (s27)", classification: "AMBIGUOUS", implication: "Derived bucket net outflow Rs 5,538 cr in 6-12m and Rs 4,461 cr in 3-5Y; investments +Rs 2,264 cr = pre-funding / negative carry"}
  - {id: "FN-14", check: "F16", line: "L626-630, L647 (s21)", classification: "AMBIGUOUS", implication: "Column positions show cost of borrowing rising 7.63% to 7.76% over Q1-Q2 FY27, opposite to A1 mapping; render check needed; lean bear"}
  - {id: "FN-15", check: "F16", line: "L119-121 (s6); L682 (s22); L809 (s26)", classification: "FORWARD-SIGNAL", implication: "Opex +12.8% QoQ vs income +12.3% despite 'strong operating leverage' caption; 'Ongoing' collections and tech investment"}
  - {id: "FN-16", check: "F16", line: "L279-282 (s12); L206 (s8)", classification: "AMBIGUOUS", implication: "New-product share switches basis (incremental vs total disbursement vs AUM); total disbursement not disclosed"}
  - {id: "FN-17", check: "F16", line: "L285-286 (s12); L181 (s8)", classification: "AMBIGUOUS", implication: "CD reach metric renamed retailers to dealer points; '>2x Consumer Durables franchise' has no base or date"}
  - {id: "FN-18", check: "F16", line: "L126-127 (s6); L175 (s8)", classification: "NEUTRAL-FACT", implication: "Gold branch count is post-quarter 'as on date'; ~Rs 4.3 cr AUM per branch; branches ahead of book"}
  - {id: "FN-19", check: "F16", line: "L626-645 (s21); L671, L686 (s22); L743 (s24)", classification: "NEUTRAL-FACT", implication: "Truncated chart axes magnify small moves; prior baseline not testable"}
  - {id: "FN-20", check: "F14", line: "L62; L1313; L1326; L394; L374; L134 vs L801", classification: "NEUTRAL-FACT", implication: "Cumulative drafting slippage incl INTERNAL stamp and dual NII meaning; governance data point"}
  - {id: "FN-21", check: "F14", line: "L964-968 (s33)", classification: "NEUTRAL-FACT", implication: "Capture: R599 'Sunil Samdani ED & CFO' conflicts with column layout; do not use for KMP tracking"}
  - {id: "FN-22", check: "F17", line: "L595 (s21); deck-wide", classification: "AMBIGUOUS", implication: "Silent on NIM/yield, write-offs, Tier 1, total disbursement, product asset quality, off-book pool, reporting basis; borrowing mix unreadable; 1 quarter (floor)"}
forward_signals: ["FN-04", "FN-05", "FN-09", "FN-15"]
ambiguous: ["FN-01", "FN-02", "FN-03", "FN-07", "FN-08", "FN-10", "FN-11", "FN-12", "FN-13", "FN-14", "FN-16", "FN-17", "FN-22"]
commitments:
  - {commitment: "AUM growth ~35-40% CAGR", implied_date: "next couple of years (~FY27-FY29)", ref: "L156-157 R609", status_word: "initiated"}
  - {commitment: "5-6x AUM aspiration", implied_date: "next 5 years (~FY31)", ref: "L297-301 R610", status_word: "initiated"}
  - {commitment: ">2x Consumer Durables franchise (base undefined)", implied_date: "FY27 onwards, undated", ref: "L281-283 R612", status_word: "initiated"}
  - {commitment: "Gold Loan network expansion", implied_date: "FY27 onwards", ref: "L126, L175, L283-284", status_word: "underway"}
  - {commitment: "Digital Business Loans scale priority", implied_date: "FY27 onwards", ref: "L284-285 R612", status_word: "initiated"}
  - {commitment: "AI-powered consumer ecosystem", implied_date: "FY27 onwards", ref: "L290-295 R613", status_word: "initiated"}
  - {commitment: "AI projects 59 underway, 42 new (84 of 143 delivered)", implied_date: "undated", ref: "L859-860 R621", status_word: "underway"}
  - {commitment: "Collections GenAI voice bots, preparing for scale", implied_date: "undated", ref: "L525-532 R614", status_word: "underway"}
  - {commitment: "Email Bot rollout", implied_date: "undated", ref: "L1103", status_word: "underway"}
  - {commitment: "Zero-Click HR ecosystem", implied_date: "undated", ref: "L1117-1118 R618", status_word: "initiated"}
  - {commitment: "Distribution franchise and growth corridors", implied_date: "undated", ref: "L1089-1107 R615 R616", status_word: "initiated"}
  - {commitment: "IIT Bombay research support", implied_date: "FY26-FY27", ref: "L1241-1243 R620", status_word: "completed"}
  - {commitment: "QIP Rs 2,500 cr", implied_date: "April-26", ref: "L148-150 R035", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read with no prior deck, so F16/F17 diffs are within-deck and silence counts floor at 1. Three items matter most. (1) Capital runway: net worth grew Rs 643 cr in Q2 while borrowings grew Rs 8,999 cr. About 11% annualised RoE cannot fund 35-40% AUM CAGR, so D/E climbs from 4.30x unless equity comes again, and the QIP was only April-26. (2) Credit cost quality: Stage 2 PCR fell four straight quarters (23.63% to 14.61%). Derived ECL stock rose only ~Rs 55 cr against Rs 376 cr credit cost, which implies ~Rs 320 cr a quarter of write-offs or other charges the deck does not disclose. GNPA ratio gains are denominator-led. (3) Two A1 chart mappings conflict with text-layer column positions. For D/E, the balance sheet proves Jun-26 = 3.82x, not 4.67x. For cost of borrowing, the column reading shows 7.63% rising to 7.76%, not falling. Render-check slide 21 before A4 uses R226-R230. Bull side, same bar: Q2 carried zero derecognition gain against Rs 51 cr in Q1, so core PBT growth beats the 21.8% headline. The deck never states whether it is standalone or consolidated."
```
