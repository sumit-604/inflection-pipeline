# A3 FORENSIC NOTES: PITTIENG, doctype PRESENTATION, Q2 FY27 (investor deck dated 22-Oct-2026, quarter and half-year ended 30-Sep-2026)

Agent: A3 forensic notes | Model: claude-opus-5-5 | Date: 2026-10-23
Inputs read: A1 structured (R001-R991, all rows), A1 fulltext (lines 1-908, all), A2 ledger (all sections), the results fulltext (cross-document test; cited as results:L###), the results A3 forensics (cited as results A3-##), and Notion context (memory, not evidence).
Not read: source PDF, anything under inputs/. Prior-quarter deck: NOT PASSED. Dropped-slide and slide-level entity diffs are not assessable.
Cite convention: L### = presentation fulltext line. presentation:R### = presentation ledger row (IDs restart per document). Quotes collapse runs of whitespace; words and figures are verbatim.
Units: Rs crores (deck). Basis: Q2/H1 FY27 standalone after the PIPL/DFPL merger; prior periods restated; FY23-FY25 historical columns are consolidated (L771, L809, L831, L859).

---

## 0. LEDGER RECONCILIATION AND CROSS-DOCUMENT TIE-OUT

| Ledger section | Rows | Read at cited line | Result |
|---|---|---|---|
| 1 Slides (32) | all | yes | all read |
| 2 Slide numbers | R001-R743 | yes | read; tables re-footed by arithmetic (scrambled slides read through footing, not layout) |
| 3 ZERO_STANDING (18) | R447-R448, R491-R492, R517-R535, R589-R592 | yes | all read (F1) |
| 4 Entities | R744-R810 | yes | all read |
| 5 Forward | R811-R834 | yes | all read (F6/F7) |
| 6 Dates | R835-R915 | yes | all read; TITLE_MISMATCH R839/R840 resolved (A3P-10) |
| 7 Qualifiers | R916-R991 | yes | all read; ESOP footnote conflict R933/R945 vs R962 (A3P-11) |
| 9 Cross-refs (RESTATED) | R028-R039 vs R004/R006/R015; slides 27-29 vs 9-10 | yes | capacity restatements tie; Mar-26 BS on p28 ties p10 except non-current liabilities 505.5 vs 505.4 (A3P-12) |

ids_in_structured 991 | ids read by A3 991 | ledger_reconciled_pct 100.

### Deck vs filing (results filing is primary)
- P&L slide 9: all 24 Q2/H1 values for revenue, other income, total income, COGS (materials + traded goods + inventory change), employee cost (filed less ESOP), other expenses, depreciation, PBT, tax and PAT tie to results:L187-L209 within rounding. The deck's EBIT includes other income: 61.6 = 88.9 - 29.4 + 2.1. Its "Finance Cost (excl FX loss)" plus "FX loss/(Gain)" sums to the filed finance cost: 18.2 - 1.8 = 16.4 vs results:L195 16.33 (A3P-14).
- BS slide 10: all Sep-26 and Mar-26 lines tie to results:L233-L280. Trade payables 474.8 = 7.87 + 466.91. The deck omits current investments of Rs 0.02 Cr (results:L246).
- CF slide 11: all lines in both columns tie to results:L288-L330.
- Historical P&L slide 27: FY26 restated ties to results:L187-L209. FY23-FY25 columns foot internally: GP = revenue - COGS, EBITDA = GP - employee - other, EBIT = reported EBITDA - depreciation + other income, PBT = EBIT - finance, PAT = PBT - tax.
- Historical BS slide 28: the Mar-26 restated column ties to results:L233-L280. All four columns foot (non-current assets, equity and liabilities totals).
- Historical CF slide 29: all four columns foot (CFO + CFI + CFF = net change; opening + change = closing).
- Exports slide 20: FY26 Rs 531 Cr ties to the filing's Outside India FY revenue of Rs 531.3 Cr (results:L395).

### A2 flags carried and resolved
| Flag | Slides / rows | Resolution |
|---|---|---|
| LAYOUT_SCRAMBLED | pp7, 9, 10, 15, 22, 23, 25, 27, 28, 29 | Numeric tables pp7, 9, 10, 27, 28, 29: A1's label mapping is confirmed by footing and by the filing tie-out above. p7 subtotals and all YoY % recompute. Text slides pp15, 22, 23, 25: pairing stays positional. Findings that rest on it say so (A3P-08, A3P-09). |
| CHART_ASSIGNMENT_BY_POSITION | pp6, 8, 30, 31 | p8: all growth labels recompute (+16.3%, +15.3%, +13.6%, +13.6%, -15.1%, -0.4%). p6: sheet metal 78% and machining 85% match results:L427. Castings 77%/52% are not covered by the filing and stay positional. p30: values tie to p27. p31: ROE and ROA order is verified FY23-FY25 by arithmetic. **D/E order is contradicted: computed FY24 1.36 and FY25 0.84, so R737/R738 (FY24 0.8, FY25 1.4) look swapped** (A3P-07). |
| PIE_ORDER_BY_LEGEND_UNVERIFIED | p16, R335-R366, R951 | All four pies sum to 100%. Slice-to-category mapping is unverified. Findings A3P-20 and A3P-21 carry the caveat. |
| TITLE_MISMATCH | p2, R839/R840 | A stale Q1 text object sits under the Q2 title (A3P-10). |
| ESOP tax footnote conflict | p8 L230, p9 L272 vs p27 L773 | Real contradiction in the deck (A3P-11). |
| LOGO_IMAGES_NO_TEXT | p17 | Logos carry no text, so the customer list cannot be checked. |

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3P-01 | F1 | presentation:R445-R448, R489-R492 | 750, 753 | "Impact of ESOP cost 10.3"; "0.6 - -" | NEUTRAL-FACT | The ESOP lines are nil in FY23-FY24 and first carry a value in FY25 (Rs 0.6 Cr). Expense in FY25 means grant 1 predates 31-Mar-2025. This supports the Notion "March 2025" date and the typo reading of results:L562 ("13th March 2026"), which closes most of results A3-24. ESOP is now recurring: FY26 Rs 10.3 Cr, H1 FY27 Rs 4.8 Cr, with grant 2 approved 22-Oct-2026. |
| A3P-02 | F6 | presentation:R010-R014, R756, R816-R818 | 125-126, 139, 142-143, 145 | "Target Capacity by FY31 : Post ~740 crore"; "Land acquisition planned in"; "capacities will be added at existing / leased premises in phased manner" | FORWARD-SIGNAL | The headline Rs 740 Cr combines the ongoing Rs 290 Cr programme with the new Rs 450 Cr (results:L445). It equals 81% of Sep-26 net worth (Rs 911.7 Cr, L278) and 3.6x FY26 CFO (Rs 204.9 Cr, L822). Funding is internal accruals and debt with no split (results:L447). Land in two cities is not costed. Interim leased premises add lease liabilities, which are debt-like. Ask: spend to date on the Rs 290 Cr, whether land sits inside the Rs 740 Cr, phasing by year, and peak net debt. |
| A3P-03 | F6 | presentation:R006-R007, R813, R846 | 133, 125 | "Castings Capacity 24,600 36,000"; "Target Capacity by FY31" | AMBIGUOUS | The deck dates castings 36,000 MT "by FY31". Memory has castings at 36,000 MT by Q1 FY29 under the Rs 290 Cr programme. The filing's capacity annexure omits castings entirely (results:L432-L439) and dates machining 10,80,000 hours to Q1 2029-30 (results:L424-L425). This is either a slip of about two years or header aggregation. Lean bear: ask for a milestone date per line. |
| A3P-04 | F6 | presentation:R076-R081, R020-R021, R026-R027, R032-R033, R921 | 195, 155-156, 163 | "Total Castings & Machined Components 3,086 2,897 6.5% 6,054 5,958 1.6%" | CONFIRMATORY-NEGATIVE | Q2 volume of 3,086 MT is 67% of the ~4,600 MT/qtr tracker line, so the falsifier wording "well under" is met. Castings utilisation is 52% on capacity up 32% YoY (18,600 to 24,600 MT; positional, R921). The FY27 guide of 17,000 MT (memory) needs 10,946 MT in H2, or 5,473 MT/qtr, +77% on Q2. Capacity is heading to 36,000 MT while 48% of current capacity is idle. A4 adjudicates the tracker. |
| A3P-05 | F10 | presentation:R581-R584, R589-R592, R577-R580 | 783, 781 | "Instrument Entirely Equity in nature 18.8 18.8 1.1 0.0" | NEUTRAL-FACT | Share capital went from Rs 16.0 Cr (Mar-24) to Rs 18.8 Cr (Mar-25), +17.5%, about 56 lakh shares at Rs 5 FV [derived]. The Rs 1.1 Cr equity instrument at Mar-24 is extinguished, which is consistent with a warrant or convertible conversion in FY25. Equity rose Rs 425.8 Cr in FY25 against PAT of Rs 122.3 Cr. Share capital is flat at 18.8 through Sep-26 (L279). The deck gives no EPS and no diluted count. Option dilution sits in results A3-13. |
| A3P-06 | F11 | presentation:R521-R524 (ZERO_STANDING), R522, R577-R578, R585-R586 | 786, 780-782 | "Intangible assets 0.0 136.1 0.0 0.0" (values sit one row below their label in the scrambled layout; footing assigns 136.1 to Goodwill, Mar-25) | FORWARD-SIGNAL | Goodwill was nil at Mar-23 and Mar-24, Rs 136.1 Cr at Mar-25 (an FY25 acquisition), and nil at restated Mar-26. Mar-25 non-current assets foot to 1,149.2 only with it. Equity fell 898.7 to 850.8 (-47.9) in FY26 against PAT of 117.8. With A3P-07, the restatement appears to have written about Rs 136 Cr of goodwill off against reserves, which answers results A3-15 in part. Forward: no impairment risk is left on the balance sheet, and restated ROE/ROCE get a mechanical lift (FY26 ROE 13.8% on restated vs 11.9% on the goodwill-inclusive period-end equity). Do not credit that lift as quality. Ask for the reserve entry. Ask also why consolidated goodwill was not carried into the merged standalone [INFERENCE: Appendix C practice usually carries consolidated carrying amounts; verify]. |
| A3P-07 | F11 | presentation:R724-R739, R985-R991 | 872, 870, 878-881, 885-888 | "ROE : PAT / Average Total Equity"; "12.5%" | AMBIGUOUS | FY26 ratios do not reproduce from the deck's own columns. ROE: 117.8 / avg(898.7, 850.8) = 13.5% vs 12.5% printed. ROA: 5.9% vs 5.7%. D/E: 0.80 vs 0.7. All three reproduce if Mar-26 equity and assets are about Rs 128-143 Cr higher, i.e. a goodwill-inclusive base: with +136.1, ROE 12.5%, ROA 5.7%, D/E 0.74. The gap is 15.9% of net worth, above the 5% threshold. FY23-FY25 ROE and ROA reproduce. ROCE does not reproduce on any tested definition. The slide is labelled "Consolidated" (L887). D/E chart order: arithmetic gives FY24 1.4 and FY25 0.8, the reverse of A1's positional R737/R738. A4 should use the arithmetic order. |
| A3P-08 | F13 | presentation:R792, R957, R764; R395 | 627-628, 632-634 | "A manufacturing entrepreneur turned senior leader post-"; "acquisition, he brings deep domain knowledge in laminations and"; "Chaitra Sundaresh" | AMBIGUOUS | The bio sits in the same column as Chaitra Sundaresh, COO Motor & Generator (positional, R957). Goodwill first appears at Mar-25 (A3P-06), and PIPL was formerly Bagadia Chaitra Industries (results:L345-L346). This strengthens results A3-20's name-match inference, but it stays [INFERENCE]. The "decade at Pitti ... motor and generator components" bio (L634-L635) also fits his title, so the pairing is not certain. Ask: is he a former owner of Bagadia Chaitra? Is there deferred consideration, an earn-out, or related-party flow? Is his pay tied to the business whose goodwill was removed? |
| A3P-09 | F13 | presentation:R787, R393, R956; R785-R790 | 604-605, 609, 591-618 | "Mechanical engineer with 40+ years of experience, including"; "executive roles at the company"; "Y B Sahgal" | AMBIGUOUS | An independent director is described as having held executive roles at the company (positional pairing, R956). Independence normally bars a KMP or employee role in the three preceding FYs [INFERENCE: s.149(6), verify]. The board is 2 promoter executives, 3 independent directors and 1 non-executive non-independent director. With an executive chairman that is 3 of 6, exactly at the 50% independence floor [INFERENCE: LODR Reg 17(1)(b)], so any independent director exit breaches it. Ask when the executive role ended. |
| A3P-10 | F14 | presentation:R839, R840, R749 | 57, 66, 55 | "Q1FY27 Investor Presentation"; "Q2 & H1FY27 Investor Presentation" | NEUTRAL-FACT | A stale Q1 title object sits under the Q2 title. The interleaved company name on L55 shows two overlapping text objects. This is template reuse. Content is Q2 throughout (L32-L33, L104). Counts toward the drafting cluster. |
| A3P-11 | F14 | presentation:R933, R945, R962, R489, R493 | 230, 272, 773 | "hence there is no Tax impact on ESOP for addback" vs "hence there is Tax impact on ESOP for addback" | AMBIGUOUS | The footnotes contradict each other. Both say a DTA is booked on ESOP, so the tax line already carries the benefit, and a gross add-back overstates Adjusted PAT by about the tax rate x ESOP. That is about Rs 0.6 Cr in Q2 (2.5 x 25.17%) and about Rs 2.6 Cr in FY26 [derived], roughly 2% of Adjusted PAT. FY26 Adjusted PAT 128.1 = 117.8 + 10.3 gross (L760-L762). Immaterial alone, but it is the basis of every Adjusted PAT on slides 8, 9, 27 and 30. |
| A3P-12 | F14 | presentation:R991, R931, R979, R497, R593, R414, R218, R802, R328-R330 | 887, 228, 858, 763, 789 vs 281, 742, 245, 368-371 vs 414-417 | "Consolidated"; "*Adjusted EBDITA"; "*Excluding other income including ESOP Cost of 10.3 crs for FY26"; "Adjusted Profit Tax Margin" | NEUTRAL-FACT | Drafting cluster. (a) The ratio slide says "Consolidated" while FY26 is standalone (L859). (b) "EBDITA". (c) The p30 footnote says "including ESOP", but the FY26 EBITDA of 326 is ex-ESOP (325.8, L748). (d) "Profit Tax Margin". (e) Mar-26 non-current liabilities are 505.5 on p28 (L789) vs 505.4 on p10 (L281). (f) FY25 total income printed to two decimals, "1,743.36" (L742). (g) Q2 PAT YoY is printed -15.3% (L245) but recomputes to -15.5% (33.9/40.1; results:L209). (h) "2 in Bangalore" (L371) vs Tumkur and Hoskote, Karnataka (L414-L417). (i) TMIEC and TMEIC both appear (R802). |
| A3P-13 | F15 | presentation:R764-R765, R927, R960, R970, R977, R981, R771-R776 | 223-224, 771 | "In September 2026, Company merged its two subsidiaries - Pitti Industries Private Limited and Dakshin Foundry Private Limited" | NEUTRAL-FACT | The deck confirms the entity deletion (matches results:L348-L353 and results A3-28). Historical slides join consolidated FY23-FY25 to standalone FY26 on the same perimeter. The six-plant list includes two Karnataka sites (L414-L417). The Rs 450 Cr plan merges the Karnataka lamination operations into one facility (results:L455-L457), so the plant list will change. No prior deck, so no slide-level diff. |
| A3P-14 | F16 | presentation:R194-R201 | 254-255 | "Finance Cost (excl FX loss) 18.2 18.4"; "FX loss / (Gain) -1.8 1.0" | AMBIGUOUS | The deck splits the filed finance cost into interest and FX. Q1 derived: interest 19.5 (37.7 - 18.2) and FX loss 3.1 (1.3 + 1.8), which sum to the filed Q1 Rs 22.6 Cr (results:L195). So Rs 4.9 Cr of the Rs 6.3 Cr QoQ fall in filed finance cost is an FX swing. Underlying interest fell Rs 1.3 Cr (-6.7%) while gross borrowings fell 8.3% (640.5 vs 698.8). This removes most of the support for results A3-18's capitalised-interest reading. Q2 PBT includes a Rs 1.8 Cr FX gain. Ask how much borrowing cost was capitalised against CWIP of Rs 120.3 Cr, and what FX exposure is booked in finance cost. |
| A3P-15 | F16 | presentation:R124-R127, R184-R191, R202-R207, R216-R221, R943 | 237, 250, 270 | "Other Income 2.1 21.3"; "EBIT 61.6 73.2"; "*Excluding other income" | AMBIGUOUS | EBITDA excludes other income but EBIT includes it. The headline EBIT -15.9%, PBT -15.9% and PAT -15.5% all come from a Q2 FY26 other-income base of Rs 21.3 Cr (results:L188). On the other side, PBT ex other income rose 32.5% (43.2 vs 32.6), and ex other income and FX it rose 23.2% (41.4 vs 33.6) [derived]. The source of the Q2 FY26 Rs 21.3 Cr is NOT FOUND (H1 FY26 interest income was Rs 2.4 Cr, results:L291). Ask what it was. Memory says management will not claim other income in FY27. |
| A3P-16 | F16 | presentation:R705-R708, R721-R723, R980, R984, R485-R486 | 859, 838, 760 | "^PAT for FY26 has been adjusted by adding back ESOP costs"; "+20% +29% +30%" | AMBIGUOUS | The PAT chart plots FY26 at 128 (adjusted), up from 123, but reported PAT fell 3.7% (122.3 to 117.8, L760). The unlabelled arrows are FY23-FY26 three-year CAGRs (20.4%, 29.2%, 29.5% [derived]). On reported PAT the CAGR is 26.1%. ESOP cost recurs (FY26 Rs 10.3 Cr, grant 2 approved), so the add-back removes a running cost. |
| A3P-17 | F16 | presentation:R424-R428, R432-R436, R440-R444, R709-R712, R961 | 772, 853 | "Regrouping in FY25, FY24, FY23 *Excluding other income"; "28.9%" | AMBIGUOUS | Gross margin jumps from 28.9% (FY23) to 38.0% (FY24) while EBITDA margin moves only from 13.8% to 14.6%. Other expenses / revenue goes from 9.7% to 15.5% [derived]. FY23 gross margin therefore sits on a different cost classification, yet slide 30 (L851-L853) shows it as one trend. Compare FY23 on EBITDA margin. Ask what the FY23 regrouping covers. |
| A3P-18 | F16 | presentation:R380-R388, R829, R955 | 515-516, 553 | "Increasing share of exports, especially to developed markets like the US and Europe"; "33% 34% 29% 27%" | AMBIGUOUS | The strengths slide claims a rising export share, but the deck's own series falls from 34% (FY24) to 27% (FY26). The shares reproduce on total income, not on "Total Revenue" as labelled. Exports grew 43% FY23-FY26 (12.7% CAGR) against revenue +73.9%. H1 FY27 exports are 26.3% (results:L395-L396), still falling. Q2 Outside India of Rs 154.3 Cr does break the Rs 135-139 Cr plateau. Ask the basis of the claim and the railway export split. |
| A3P-19 | F16 | presentation:R254-R255, R288-R289, R308-R315, R673, R549-R552, R621-R624, R276-R277, R286-R287 | 316, 319, 293, 822 | "Changes in working capital 164.8 -84.4"; "Net Cash from Operating Activities 323.0 95.4"; "474.8 243.3" (scrambled; trade payables per footing and results:L273-L274) | AMBIGUOUS | The deck shows H1 CFO of Rs 323.0 Cr, more than full-year FY26 (Rs 204.9 Cr), with no comment. Payables doubled (+95%) and inventory rose 21% to Rs 478.7 Cr, moving away from the Rs 300 Cr memory target. Payable days on COGS [derived]: Sep-26 128 (H1 annualised), Mar-26 77, Mar-25 118, Mar-24 113. Two readings: (a) payables normalising after an abnormally low Mar-26 (FY26 working capital absorbed Rs 125.2 Cr, L819); (b) supplier credit or LC acceptances stretched past the 113-118-day history. The observation that separates them: Q3 payable days, and whether the payables include LC acceptances (pending operator ruling). Deck net debt: 640.5 - 59.1 - 42.7 = Rs 538.7 Cr vs the Rs 491 Cr tracker (same as results A3-16). |
| A3P-20 | F16 | presentation:R082-R087, R342, R350, R951-R952 | 197, 462-463 | "By products & Scrap 21,081 12,498 68.7% 36,655 23,926 53.2%"; "Others includes home appliances, automotives, etc and scrap sales, other income" | AMBIGUOUS | By-product and scrap tonnage rose 68.7% and now exceeds lamination tonnage (21,081 vs 20,612 MT). Scrap per tonne of product (lamination and assemblies plus castings) rose from 0.62 to 0.85 [derived]. The pie's "By products & Others" share fell from 21% to 15% of total income: about Rs 83.5 Cr to Rs 85.0 Cr ex other income, flat value on +69% tonnage [derived; pie order unverified]. Readings: yield loss (consistent with gross margin -0.6 pp), a definition change, or traded scrap. Ask. |
| A3P-21 | F16 | presentation:R335-R366, R951, R757-R761, R824 | 437, 442-444, 456, 140-141 | "32% 27%"; "Traction motor and railway components" | AMBIGUOUS | Traction and railway (domestic plus export) falls from 32% to 27% of total income: about Rs 159.7 Cr to Rs 156.7 Cr, -2% YoY on revenue +21% [derived; pie order unverified; ±0.5 pp = ±Rs 3 Cr]. Data centres (3% to 7%, about Rs 15 Cr to Rs 41 Cr) and mining, oil and gas (6% to 10%, about Rs 30 Cr to Rs 58 Cr) carry the growth. Slide 5 still cites rail customers (Progress Rail, Siemens Mobility, Medha Servo) for the capex. The deck has no export-railway split, so the tracker row cannot be updated from the deck. |
| A3P-22 | F16 | presentation:R079-R080, R076-R077 | 195 | "3,086 2,897 6.5% 6,054 5,958 1.6%" | AMBIGUOUS | Implied Q1 FY27 castings volume is 2,968 MT (H1 6,054 less Q2 3,086, a -3.0% YoY change). Last quarter's reported 3,191 MT (+4.2%, memory) is 223 MT (-7.0%) higher, but the implied Q1 FY26 base (3,061 MT) is unchanged. So the current-year Q1 figure appears silently revised down. The integrated-assembly Q1 figure (+21.7%) is not revised. Ask whether Q1 was restated or reclassified. Memory is not evidence: the deck figure stands. |

Count: 22 findings. FORWARD-SIGNAL 2, AMBIGUOUS 14, CONFIRMATORY-NEGATIVE 1, NEUTRAL-FACT 5.

---

## 2. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing lines | FINDING | 18 ZERO_STANDING rows read. ESOP nil in FY23-FY24 dates the scheme to FY25 (A3P-01). Goodwill line is in A3P-06, the equity instrument in A3P-05. Investment property (1.9, Mar-23), investments (15.1, Mar-23) and intangible CWIP (0.1, Mar-25) are historical relics with no forward class. |
| F2 Standalone vs consolidated | N.A. | The deck has no same-period standalone/consolidated pair. The basis join (consolidated FY23-FY25, standalone FY26) is covered under F11/F16. |
| F3 Shell-entity detection | N.A. | No standalone vs consolidated cost lines in the deck. |
| F4 Unaudited contribution | N.A. | No auditor paragraph in the deck (see results A3-05). |
| F5 EoM scope tracking | N.A. | No EoM in the deck. |
| F6 Forward-commitment mining | FINDING | 9 commitments registered (section 3). Rs 740 Cr programme (A3P-02). Castings date (A3P-03). Castings delivery vs tracker and guide (A3P-04). |
| F7 Hedge phrase mining | PASS | Hits are Safe Harbour boilerplate only: "subject to known and unknown risks" (L82-L83), "not adopted by the Company" for third-party projections (L89-L90, which covers the slide 16 market claims), "which we believe" (L570). No new hedge on lumpiness or concentration. |
| F8 Tax forensics | PASS | Tax lines tie to the filing. ETR history FY23 26.4%, FY24 24.9%, FY25 24.3%, FY26 29.7%, H1 FY27 22.2% [derived] adds no new earlier-years item. The ETR analysis sits in results A3-10/A3-11. The ESOP DTA wording is in A3P-11. |
| F9 OCI forensics | N.A. | The deck carries no OCI. |
| F10 Share count and dilution | FINDING | Share capital +17.5% in FY25 and the equity instrument extinguished; flat since Mar-25 (A3P-05). No EPS in the deck. |
| F11 Reserves and net worth tie-out | FINDING | Paid-up plus other equity ties in all five columns (911.7, 850.8, 898.7, 472.9 incl. 1.1 instrument, 334.0) and to the filing. Goodwill Rs 136.1 Cr removed (A3P-06). FY26 ratios imply a base about 16% above printed equity (A3P-07). |
| F12 Segment forensics | N.A. | No segment assets or liabilities in the deck. Industry pie and exports are under F16. |
| F13 Board outcome beyond results | FINDING | No AR or AGM item. Management slide already reflects the 22-Oct-2026 re-designations. Post-acquisition bio (A3P-08). Independent director with former executive role, board at the 50% floor (A3P-09). |
| F14 Note drafting inconsistencies | FINDING | Stale Q1 title (A3P-10). ESOP tax footnote contradiction (A3P-11). Nine-item drafting cluster (A3P-12). |
| F15 Entity list diffs | FINDING | PIPL and DFPL merged; plant list to change with the Karnataka consolidation (A3P-13). |
| F16 Presentation dropped/reframed | FINDING | No prior deck, so dropped slides are not assessable. Reframes inside the deck: FX in finance cost (A3P-14), EBIT with other income (A3P-15), adjusted PAT chart (A3P-16), FY23 gross-margin break (A3P-17), export-share claim (A3P-18), CFO without working-capital drivers (A3P-19), scrap tonnage (A3P-20), railway share (A3P-21), Q1 castings revision (A3P-22). Order book unquantified ("Strong order visibility", L140). No FY27/FY28 guidance in the deck. |
| F17 Concall silence audit | N.A. | Doctype presentation. The call was scheduled for 23-Oct-2026 14:00 (L33-L34); the concall leg is a follow-up. Checklist data is in section 4. |

PASS 2 | FINDING 8 | N.A. 7 | blank 0. GATE A3: pass.

---

## 3. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Ref (line / row) | Status word |
|---|---|---|---|---|
| C1 | Phased investment of ~Rs 740 Cr (Rs 290 Cr ongoing + Rs 450 Cr new), "to be live in phased manner" | phased to FY31 | L125-L128, L145; R010-R014, R816 | initiated |
| C2 | Sheet metal capacity 1,08,000 to 1,60,000 MT | by FY31 | L130; R004-R005, R812 | initiated |
| C3 | Castings capacity 24,600 to 36,000 MT | by FY31 (memory: Q1 FY29) | L133; R006-R007, R813 | initiated |
| C4 | Machining 8,13,600 to 13,14,000 hours (interim 10,80,000 by Q1 2029-30, results:L424-L425) | by FY31 | L136, L149; R008-R009, R015, R814 | underway (interim leg) |
| C5 | Land acquisition in Hyderabad and Bengaluru | undated | L139-L140; R817 | initiated (planned) |
| C6 | Interim capacity at existing or leased premises | interim, undated | L142-L143; R818 | initiated (planned) |
| C7 | Expand into complex and critical machined components ("Intend to leverage") | undated | L569-L571; R831-R832 | initiated (intent) |
| C8 | Merger of PIPL and DFPL into PEL | September 2026 | L223; R927 | completed |
| C9 | Earnings call, Friday 23-Oct-2026, 2:00 PM IST | 23-Oct-2026 | L33-L34; R811 | initiated (scheduled) |

Status-change check: C8 is the only milestone word ("completed"), and it matches results C6. The C4 interim leg is "underway" per the filing. No prior deck, so no initiated-to-underway transitions can be checked.

---

## 4. MONITORING-CHECKLIST DATA VISIBLE IN THE DECK (for A4; F17 itself is N.A.)

| Item | Deck evidence | Read |
|---|---|---|
| Net debt vs Rs 491 Cr | Borrowings 372.5 + 268.0, cash 59.1, other bank 42.7 (L283, L289, L291-L292; A1-mapped, ties results:L248-L270): Rs 538.7 Cr. Mar-26: Rs 552.0 Cr. | Above the line. Payables +Rs 231.5 Cr carry the release (A3P-19). |
| Castings and machined volume vs ~4,600 MT/qtr | 3,086 MT (L195); Q1 implied 2,968 | Well under (A3P-04). Q1 revised (A3P-22). |
| Export railway vs Rs 135-139 Cr | No export-railway split. Total railway about Rs 157 Cr (pie, unverified). Total exports Rs 154.3 Cr (results:L395) | Not updatable from the deck (A3P-21). |
| Mix migration | Stator and rotor high value-added 4,786 MT (+51.1%); integrated stator-frame/rotor-shaft 1,350 MT (+17.8% YoY; Q1 implied 1,212, so +11.4% QoQ); loose 14,476 MT (+22.7%) (L184-L190) | Qualified tier is 29.8% of lamination tonnage vs 26.8%. The top tier keeps decelerating YoY (FY26 +31.9%, Q1 +21.7%, Q2 +17.8%) but recovered QoQ. |
| EBITDA/t | Adjusted EBITDA 91.3 over 24,757 MT (lamination and assemblies plus castings): Rs 36.9k/t, vs Rs 39.9k in Q2 FY26 (-7.5%). H1 Rs 38.4k vs Rs 40.2k [derived] | Below the Rs 41-42k memory band (memory basis unknown). |
| Machining bottleneck | 85% Q2 (90% Q2 FY26) on capacity +27%; hours used +19.9% [derived] (L157, L163) | Eased. |
| FY27/FY28 guidance | None in the deck. H2 needs revenue Rs 1,192.5 Cr (+7.7% vs H1) and EBITDA about Rs 189.9 Cr (+5.4% vs H1 adjusted) against memory guides of ~Rs 2,300 Cr and ~Rs 370 Cr | Within reach on revenue and EBITDA. Castings guide is far off (A3P-04). |
| SGST search (8-Oct-2026), dividend | Deck silent | Ask on the call. |

Notion differences logged (the deck and filing win): Q1 FY27 castings 2,968 MT implied vs 3,191 MT in memory; goodwill Rs 136.1 Cr at Mar-25 vs ~Rs 130 Cr in memory (FY26 figure not in the deck); ESOP grant-1 evidence points to FY25 (A3P-01).

---

```yaml
stage: A3-forensics
company: "PITTIENG"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/pittieng-q2fy27/work/forensics_presentation_pittieng_q2fy27.md"
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
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3P-01", check: "F1", line: "750, 753", classification: "NEUTRAL-FACT", implication: "ESOP cost nil FY23-24, Rs 0.6 Cr FY25: grant 1 predates Mar-2025; supports typo reading of results:L562 (results A3-24); ESOP now recurring"}
  - {id: "A3P-02", check: "F6", line: "125-126, 139, 142-143, 145", classification: "FORWARD-SIGNAL", implication: "Rs 740 Cr (290 ongoing + 450 new) = 81% of net worth, 3.6x FY26 CFO; land uncosted; leased interim capacity adds debt-like leases"}
  - {id: "A3P-03", check: "F6", line: "133, 125", classification: "AMBIGUOUS", implication: "Castings 36,000 MT dated by FY31 vs Q1 FY29 in memory; filing annexure omits castings; possible two-year slip"}
  - {id: "A3P-04", check: "F6", line: "195, 155-156, 163", classification: "CONFIRMATORY-NEGATIVE", implication: "Castings+machined 3,086 MT = 67% of 4,600 tracker; utilisation 52% on +32% capacity; FY27 17,000 MT guide needs +77% H2 run-rate"}
  - {id: "A3P-05", check: "F10", line: "783, 781", classification: "NEUTRAL-FACT", implication: "Share capital +17.5% in FY25 with 1.1 Cr equity instrument extinguished (warrant/convertible); flat since Mar-25; no EPS in deck"}
  - {id: "A3P-06", check: "F11", line: "786, 780-782", classification: "FORWARD-SIGNAL", implication: "Goodwill Rs 136.1 Cr (Mar-25) nil in restated Mar-26; equity -47.9 in FY26 vs PAT 117.8; write-off vs reserves likely; mechanical ROE/ROCE lift, do not credit as quality"}
  - {id: "A3P-07", check: "F11", line: "872, 870, 878-881, 885-888", classification: "AMBIGUOUS", implication: "FY26 ROE/ROA/D/E reproduce only on Mar-26 base ~Rs 136 Cr above printed equity (goodwill-inclusive); D/E order: FY24 1.4, FY25 0.8 by arithmetic, reverse of A1 positional"}
  - {id: "A3P-08", check: "F13", line: "627-628, 632-634", classification: "AMBIGUOUS", implication: "Post-acquisition entrepreneur bio beside Chaitra Sundaresh (positional) strengthens results A3-20 [INFERENCE]; ask earn-out, related party, former ownership"}
  - {id: "A3P-09", check: "F13", line: "604-605, 609", classification: "AMBIGUOUS", implication: "Independent director Y B Sahgal had executive roles at the company (positional); board 3 of 6 independent with executive chair, at the 50% floor"}
  - {id: "A3P-10", check: "F14", line: "57, 66", classification: "NEUTRAL-FACT", implication: "Stale Q1FY27 title object under Q2 title; template reuse; content is Q2"}
  - {id: "A3P-11", check: "F14", line: "230, 272, 773", classification: "AMBIGUOUS", implication: "ESOP add-back footnotes contradict (no tax impact vs tax impact); gross add-back with DTA overstates Adj PAT ~0.6 Cr Q2, ~2.6 Cr FY26"}
  - {id: "A3P-12", check: "F14", line: "887, 228, 858, 763, 789, 281, 742, 245, 371", classification: "NEUTRAL-FACT", implication: "Drafting cluster: Consolidated label on FY26 ratios, EBDITA, ESOP footnote wording, NCL 505.5 vs 505.4, PAT YoY -15.3% printed vs -15.5%, plant geography"}
  - {id: "A3P-13", check: "F15", line: "223-224, 771", classification: "NEUTRAL-FACT", implication: "PIPL and DFPL merged; FY23-25 consolidated joined to FY26 standalone; Karnataka plants to consolidate under Rs 450 Cr plan"}
  - {id: "A3P-14", check: "F16", line: "254-255", classification: "AMBIGUOUS", implication: "Rs 4.9 Cr of Rs 6.3 Cr QoQ finance-cost fall is FX swing; underlying interest -1.3 Cr; weakens results A3-18 capitalised-interest reading; Q2 PBT has 1.8 Cr FX gain"}
  - {id: "A3P-15", check: "F16", line: "237, 250, 270", classification: "AMBIGUOUS", implication: "PAT -15% is Q2FY26 other income base Rs 21.3 Cr (source NOT FOUND); PBT ex other income and FX +23.2%"}
  - {id: "A3P-16", check: "F16", line: "859, 838, 760", classification: "AMBIGUOUS", implication: "PAT chart uses adjusted FY26 128 (reported fell 3.7%); arrows are unlabelled 3-yr CAGRs; reported PAT CAGR 26.1% vs 30% shown"}
  - {id: "A3P-17", check: "F16", line: "772, 853", classification: "AMBIGUOUS", implication: "FY23 gross margin 28.9% on different cost classification (other exp/rev 9.7% vs 15.5%); FY23-24 GM trend not comparable"}
  - {id: "A3P-18", check: "F16", line: "515-516, 553", classification: "AMBIGUOUS", implication: "Claim of increasing export share vs deck's own 34% to 27% (FY24-FY26); H1 FY27 26.3%; exports 12.7% CAGR vs revenue +73.9%"}
  - {id: "A3P-19", check: "F16", line: "316, 319, 293, 822", classification: "AMBIGUOUS", implication: "H1 CFO 323 > FY26 CFO with no comment; payable days 128 vs 77 Mar-26 and 113-118 history; inventory 478.7 away from 300 target; net debt 538.7 vs 491"}
  - {id: "A3P-20", check: "F16", line: "197, 462-463", classification: "AMBIGUOUS", implication: "Scrap tonnage +68.7%, 0.85 t per t product vs 0.62; by-product value flat (pie, unverified); yield loss vs definition change"}
  - {id: "A3P-21", check: "F16", line: "437, 442-444, 456, 140-141", classification: "AMBIGUOUS", implication: "Railway share 32% to 27% (~Rs 157 Cr, -2% YoY) while data centres and mining carry growth (pie unverified); no export-railway split"}
  - {id: "A3P-22", check: "F16", line: "195", classification: "AMBIGUOUS", implication: "Implied Q1 FY27 castings 2,968 MT vs 3,191 reported last quarter (memory) with Q1 FY26 base unchanged; silent downward revision?"}
forward_signals: ["A3P-02", "A3P-06"]
ambiguous: ["A3P-03", "A3P-07", "A3P-08", "A3P-09", "A3P-11", "A3P-14", "A3P-15", "A3P-16", "A3P-17", "A3P-18", "A3P-19", "A3P-20", "A3P-21", "A3P-22"]
commitments:
  - {commitment: "Phased ~Rs 740 Cr investment (290 ongoing + 450 new)", implied_date: "phased to FY31", ref: "L125-128, L145", status_word: "initiated"}
  - {commitment: "Sheet metal capacity to 1,60,000 MT", implied_date: "FY31", ref: "L130", status_word: "initiated"}
  - {commitment: "Castings capacity to 36,000 MT", implied_date: "FY31 (memory Q1 FY29)", ref: "L133", status_word: "initiated"}
  - {commitment: "Machining to 13,14,000 hours (interim 10,80,000 by Q1 2029-30)", implied_date: "FY31", ref: "L136, L149; results:L424-425", status_word: "underway"}
  - {commitment: "Land acquisition in Hyderabad and Bengaluru", implied_date: "undated", ref: "L139-140", status_word: "initiated"}
  - {commitment: "Interim capacity at existing or leased premises", implied_date: "undated", ref: "L142-143", status_word: "initiated"}
  - {commitment: "Expand into complex and critical machined components", implied_date: "undated", ref: "L569-571", status_word: "initiated"}
  - {commitment: "Merger of PIPL and DFPL into PEL", implied_date: "September 2026", ref: "L223", status_word: "completed"}
  - {commitment: "Earnings call", implied_date: "23-Oct-2026 14:00 IST", ref: "L33-34", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Deck numbers tie to the filing on every Q2, H1 and Mar-26 line tested, so the deck adds framing, not new primary numbers. Three items change the results-A3 read. First, the deck splits finance cost: Rs 4.9 Cr of the Rs 6.3 Cr QoQ fall is an FX swing, and underlying interest fell only Rs 1.3 Cr, so results A3-18's capitalised-interest case weakens. Second, goodwill of Rs 136.1 Cr at Mar-25 is nil in restated Mar-26. FY26 ROE, ROA and D/E reproduce only on a base about Rs 136 Cr above printed equity, so the restatement likely wrote goodwill off against reserves. Future ROE and ROCE gain a mechanical lift that must not be credited as quality. Third, ESOP cost first appears in FY25, which supports a March 2025 grant 1. The Q2 PAT fall is the Q2 FY26 other-income base (Rs 21.3 Cr, source NOT FOUND); PBT ex other income and FX rose 23%. Castings volume is 67% of the tracker line, and implied Q1 castings sits 223 MT below last quarter's print. Pie and ratio charts are positional; D/E order is corrected by arithmetic."
```
