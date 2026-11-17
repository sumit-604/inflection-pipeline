# Margin-source check, 30 names (17-Nov-2026, v2)

Run date 2026-11-17. Source order: Bull AI first, screener.in through the operator's Chrome second (one gap-fill pass). Bull AI calls used: 199 (batches 158, gap-fill 41). Periods: Q1 FY27 = Apr-Jun 2026, Q2 FY27 = Jul-Sep 2026. Foseco uses a calendar year, and Kennametal India uses a Jul-Jun year. For both, the last two reported quarters are used.

"Derived" = arithmetic on filed lines, not a company figure. BAI = Bull AI document_id (first 8 characters; full IDs are in the workpapers). Full extraction notes: `screens/margin_source_check_2026-11-17_workpapers/` (batch1-5.md, gapfill.md).

## Findings that change the screen's premise

| Name | Screen assumption | What the filings show |
|---|---|---|
| Om Power | Debtor days ~180 | Management cites 118 days at Mar-26, and 176 days was Mar-23. Mar-26 ageing: 77.7% not yet due (retention money). |
| Adisoft | Receivables rising | The H1 FY27 cash flow shows receivables **down** Rs 3,324 lakh. |
| Marsons | Receivables rising | The **revised** Sep-26 filing (BAI 4f09c9f3) shows consolidated receivables of Rs 9,016 lakh, against Rs 10,734 lakh at Mar-26: **down**. The cash flow ties to it. The other 13-Nov filing (Rs 11,152 lakh) has a mapping error (other current liabilities 1.92). The Rs 9,011 / 11,146 figures are the standalone sheets. |
| CFF Fluid | Receivables rising | The H1 FY27 rise is only Rs 336 lakh. H1 FY27 is the first Ind AS period, and the comparatives are restated. |
| Foseco | Margin rise | The consolidated rise comes from consolidating Foseco Crucible. Standalone derived EBITDA margin for Jul-Sep 2026 is 17.5%, against 18.3% a year earlier: **down**. |
| Kennametal | Margin rise | The company says it came from "timing of raw material-related pricing compared to costs". This is a price-cost lag gain. |
| Bajaj Consumer | Ad-cut suspicion | A&P rose 7% in rupees. Its share of sales fell from 14.9% to 12.5% on 27% sales growth. That is sales leverage, not an ad cut. |
| Mayur | Mix/exports suspicion | Management calls the Q1 spike a one-time forex gain and ties Q2 gross margin to raw-material and crude prices. Export OEM revenue fell. |

## Table

| Name | Grp | Stated margin reason | Class | H2 FY27 / FY28 margin guidance | Temporary flag | Receivables reason (A2) | Funding (last 18m) | Source file and page |
|---|---|---|---|---|---|---|---|---|
| Timex | A1 | Fixed-cost leverage on ~35% growth; product gross margin fell 1.1% (inputs, forex); ~8% price rise from Apr-26 | OPERATING LEVERAGE | No H2 number; "close to about 20%" in "a year or so" (H1 17.5%) | None. Says Q3 purchase-price-variance (PPV) hit will be smaller | n/a | NOT DISCLOSED | Q2 call 4-Nov-26 pp.7,16,21,32 (BAI 2a2600a5); Q2 deck p.20 (5cb49176) |
| MPS | A1 | AI-driven operating leverage | OPERATING LEVERAGE | FY27 EBITDA "at least INR 310 crores", H2 leans to Q4; steady-state 30%; FY28 ~INR 450 cr EBITDA | None | n/a | None; zero debt, INR 163 cr cash | Q2 call 4-Nov-26 pp.3-4,11 (c2ccb704); Q1 call 29-Jul-26 pp.11,14 (38ba42fa) |
| KMC Speciality | A1 | NOT DISCLOSED. Filed data: occupancy 86% vs 69%, ARPOB +11% | NOT DISCLOSED | NOT DISCLOSED | None found | n/a | NOT DISCLOSED | Q1 deck 28-Aug-26 pp.14,24 (38b74eb0); Q2 results 13-Nov-26 p.3 (805e4052) |
| Krishna Defence | A1 | Product mix (bulb bars, welding wire, Army items) | PRICING/MIX | 25-26% for FY27: "We make all our efforts". FY28 NOT DISCLOSED | Margin moves with the quarter's category mix | n/a | NOT FOUND | Q2 call 30-Oct-26 pp.4,9-10 (1dd3ab90) |
| Valiant Comm. | A1 | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | None found | n/a | Preferential warrants 6,00,000 at Rs 768; 3,50,000 outstanding 30-Sep-26 | Q2 results 5-Nov-26 p.5 (590c0cd1) |
| Foseco India | A1 | NOT DISCLOSED. Consolidated rise = Foseco Crucible consolidation | NOT DISCLOSED | NOT DISCLOSED | None found | n/a | None; acquisition plus open offer | Jul-Sep 26 results 6-Nov-26 pp.2-5 (f1277d9f); H1 CY26 deck p.9 (1b486a16) |
| Adroit | A1 | Product mix (low-volume ~50% margin parts, finished shafts, US stocking) plus procurement and pricing | PRICING/MIX | "approximately 30%, plus or minus 2 percentage points" | None | n/a | IPO Sep-26; "manage the growth without raising additional funds" | Q2 call 28-Oct-26 pp.5,8-9 (9c0604c8) |
| Uniparts | A1 | Held 23.4% despite RM inflation; channel mix (warehousing 53% vs 56%) and lower treasury income cut QoQ | PRICING/MIX | "We don't guide to an EBITDA number"; "20% margins over a cycle" | RM pass-through lags (a headwind that reverses) | n/a | None; INR 172 cr net cash | Q2 call 5-Nov-26 pp.5-6,10,12 (231c97b1) |
| Kennametal India | A1 | "favorable timing of raw material-related pricing compared to costs", plus Hard Metal volume | INPUT DEFLATION (price-cost timing) | NOT DISCLOSED | "Timing" wording; reversal not stated | n/a | None found | Board outcome 12-Nov-26 note 3 p.6, PR p.7 (cdee140b) |
| Thyrocare | A1 | Operating leverage on 25% growth | OPERATING LEVERAGE | Long-term "about 31%, 31.5% ... not above that" (H1 32.6%) | Launch cost INR 1.5 cr Q2, INR 3 cr Q3. Sep-26 negative item = ONE-OFF non-cash NHL goodwill impairment INR 45 cr consol / INR 9 cr standalone | n/a | None; zero debt, INR 211 cr net cash | Q2 call 29-Oct-26 pp.8,16-17 (dc640cb3) |
| Kanohar | A1 | None given: "no one-off", order-to-order variation | NOT DISCLOSED | FY27 held at FY26 level (analyst: 27-28%); implies H2 ~24% | Implicit: H1 ~32% sits above the full-year guide | n/a | IPO Sep-26 | Q2 call 3-Nov-26 pp.8,17 (e82ab857) |
| SRM Contractors | A1 | NOT DISCLOSED | NOT DISCLOSED | FY27 "EBITDA Guidance 15-18%+" (Q1 deck) | None found | n/a | Bank debt; NCI Rs 4,180 lakh FY26 | Q1 deck 14-Aug-26 p.15 (b5fa430a); Q2 results 14-Nov-26 pp.4-13 (97e05fb8) |
| BCC Fuba | A1 | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | None found | n/a | Rights issue, partly paid; call Rs 37.50 (Letter of Offer 5-Mar-26) | Q2 results p.5 (7ba7d3a5); capital filing 11-Sep-26 p.1 (07b1fe9a) |
| Exato | A1 | International share and order execution (Q1) | PRICING/MIX | No margin number; new verticals start at 10-12% | Management expects dilution from new lines | n/a | IPO plus pre-IPO placement | Q1 call 19-Aug-26 pp.7,22 (2d711ada). Q2 call held 19-Nov-26, not yet available |
| Technocraft Ventures | A2 | Board: supplier advances "secure competitive discounts on the procurement of raw materials" | INPUT DEFLATION (procurement discount) | NOT DISCLOSED | Not stated. [INFERENCE] The discount depends on IPO-funded advances | Govt certification delays and retention; receivables 34.2% of FY26 revenue | IPO fresh issue Rs 201.51 cr, Aug-26 | Monitoring agency report 4-Nov-26 p.5 (56aa4135); RHP p.37 (82a0ee41) |
| Kwality Pharma | A2 | Registered-product mix in MENA and LATAM | PRICING/MIX | "27%-28% is very much achievable"; 28-29% with hormone plant in FY28 | None: "very sustainable" | INR 60-70 cr Middle East debtors stuck in Q4 FY26, realised in Q1-Q2; days 203 to 178 | Export (MENA, LATAM). Internal accruals; extended loan unused | Q2 call 13-Nov-26 pp.14-15 (e257576b); H1 deck p.9 (c84578a8); Q1 call p.11 (65e1b815) |
| M E T S (Maestros) | A2 | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED. Working capital moved through customer advances unwinding (Rs -597 lakh H1) | None; 1:1 bonus Oct-26 (not funding) | Q2 results 5-Nov-26 pp.4,12,14 (4abdf46a) |
| Marine Electricals | A2 | NOT DISCLOSED ("improved profitability" only) | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | "2H-weighted in line with the order execution cycle"; customer split NOT FOUND | Preferential equity plus warrants, Rs 213.76 cr revised to Rs 149.22 cr (EGM 13-Aug-24); Rs 76.52 cr reallocated to WC | PR 4-Nov-26 p.3 (f0114a43); deck 22-Sep-26 p.45 (d6340b24); ICRA MA report pp.3-4 (791529cb) |
| Silver Touch | A2 | "software-led operating leverage"; hardware resale down ~75% | OPERATING LEVERAGE (mix is the same move; do not credit twice) | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED; govt/PSU clients named, no share given | Short-term borrowing +Rs 1,262 lakh H1 FY27 | Q1 deck 23-Sep-26 p.6 (a746b291); Q2 results 29-Oct-26 pp.13,15 (1c478f1b) |
| KRM Ayurveda | A2 | MoD hospital empanelment, high ticket size, low marketing spend (Q4 FY26 call) | PRICING/MIX | ">= 50%" revenue growth; margins "definitely going to increase"; no number | None | "increase in amount due from the Government Panel Debtor" | Govt panel. IPO Rs 77.49 cr, listed 29-Jan-26 | Q4 FY26 call 5-May-26 pp.8-9 (d908f605); AR FY26 p.184 (0f264fe7); Q2 deck p.8 (96020c1a) |
| Menon Bearings | A2 | Lower RM consumption per unit, productivity +25% absorbs overheads, price pass-through | OPERATING LEVERAGE + PRICING/MIX (input prices rose) | "we will definitely sustain"; no number | None | Export stock build "to the extent of three months" at US customers; funded by packing credit | Export (US OEMs). Internal accruals and packing credit | Q2 call 30-Oct-26 pp.6,21,23 (d17076f4) |
| Marsons | A2 | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED. Revised filing shows receivables falling | Preferential Rs 80.25 cr, 18-Apr-24 (outside 18m) | Revised Sep-26 results 13-Nov-26 pp.10-11 (4f09c9f3) |
| CFF Fluid Control | A2 | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED; H1 rise Rs 336 lakh; Ind AS restatement | FPO Rs 87.75 cr, 14-Jul-25 | Sep-26 results note 2 p.5 (0c8e2dea); Reg 32 p.2 (008651cb); AR FY26 p.113 (beccbe91) |
| Adisoft | A2 | More service components billed in H1 | PRICING/MIX | FY27 "sustainable PAT margin of around 13% to 14%" (H1 standalone 15.7%) | Implicit yes: the guide sits below H1 | NOT DISCLOSED; collection 50-60 days; receivables fell in H1 | IPO net Rs 74.10 cr, H1 FY27 | Q2 call 6-Nov-26 pp.4,10-11 (972a32ba); H1 results p.24 (bf839e6c) |
| Om Power | A2 | Mix: transmission lines 79%, substations 17%, Dholera fast-track job | PRICING/MIX | Yearly "12% to 13% at EBITDA level and PAT margin between 8% to 9%" | Conditional: "will depend on the project mix" | Retention money released after two years; "temporarily spiked up but it will normalize" | PSU utilities 83% of FY26 revenue (GETCO lead). IPO net Rs 119.32 cr | Q2 call 2-Nov-26 pp.6-8 (bf9768dd); Q2 deck p.20 (b88d3acc); AR FY26 p.112 (23031aa3) |
| Mayur Uniquoters | A3 | Q1 spike = one-time forex; Q2 gross margin moves with RM and crude; consolidated lift from US warehouse stock clearance | ONE-OFF (Q1) + INPUT DEFLATION (Q2) | "sustainable margin will be 25 plus 1% or 2%" (basis not stated) | Yes: Q1 forex "onetime"; Q1 labour-code provision reversed in Q2 | n/a | None seen | Q1 call 6-Aug-26 pp.6-7 (c2e2e2c7); Q2 call 5-Nov-26 pp.5-6,9 (c4f64911) |
| Raghav Productivity | A3 | Value-added and R&D variant mix; exports with full freight pass-through | PRICING/MIX | NOT DISCLOSED | None | n/a | None seen | Q1 PR 15-Jul-26 p.2 (ba986c8d); deck p.7 (01c1070d) |
| Nidhi Granites | A3 | NOT DISCLOSED. Segment data: garments to nil; fintech subsidiary added Rs 1,723 lakh revenue | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | n/a | All-cash acquisition Rs 60.57 lakh | AR FY26 pp.39,118,129 (1cb9fe2f) |
| Bajaj Consumer | A3 | "savings in fixed costs and employee costs"; non-working A&P optimised | OPERATING LEVERAGE | "we don't give guidances"; ~5% price rise and ml-age cut in Q3 | No ad cut (A&P +7% in rupees); inputs volatile | n/a | None | Q2 call 15-Oct-26 pp.3-5,13 (1f505424); Q2 deck pp.21,23 (2ebf29c1) |
| Frontier Springs | A3 | NOT DISCLOSED for margin; growth from Q1 orders delayed by RM shortage | NOT DISCLOSED (catch-up volume implied) | No margin number; FY27 revenue "at least Rs 450 crore" | Yes: steel, oil and gas "could put some pressure on margins" | n/a | None seen | Q2 deck 12-Nov-26 p.21 (549a68df) |

## Quotes

**Timex**
- "it's a leverage of my fixed cost. If you see my fixed cost hasn't gone much higher." Q2 FY27 call, p.32, BAI 2a2600a5, 4-Nov-26.
- "our product margin has actually dropped by about 1.1% versus the same quarter last year." Same, p.7.
- "I believe this can expand in a year or so to close to about 20%." Same, p.16.
- Mix check: "EBITDA margins are almost similar for all our brands" (p.21). Own-brand share rising to 60% "doesn't have any larger impact on our EBITDA percentage" (p.28). The pages read show no line reclassification. The results notes pages (pp.4-5, BAI 408ac237) were not retrieved. Purchases of stock-in-trade were 14,743 against 2,930 in Jun-26, so the material and trading lines move together.
- Capacity: about 100% utilisation, with a double shift above 500,000 units (p.32). Capex amount NOT DISCLOSED.

**MPS**
- "Over the last six quarters, revenue grew about 20%, and EBITDA grew about 53%. That gap is operating leverage." Q2 call, p.3, BAI c2ccb704, 4-Nov-26.
- "we expect FY'27 EBITDA to be at least INR 310 crores. The second half leans towards the fourth quarter" Same, p.4.
- "In a steady state, the business should operate at a 30% EBITDA margin" Q1 call, p.14, BAI 38ba42fa, 29-Jul-26.

**KMC Speciality Hospitals**
- "EBITDA as a % of revenue for Q1 FY'26 is 32% as compared to 26% in the Q1 previous year" Q1 FY27 deck, p.19, BAI 38b74eb0, 28-Aug-26. The slide label reads FY'26, but the context is Q1 FY27.
- Occupancy 86% on 330 census beds, against 69% a year earlier (p.24). Q2 FY27 derived EBITDA margin is 30.5% (BAI 805e4052 p.3).

**Krishna Defence**
- "With the product mix in place, there are some products with high margins, some products with slightly lesser margin." Q2 call, p.9, BAI 1dd3ab90, 30-Oct-26.
- "if the particular category revenue for that quarter is more, you will see an uptick in the EBITDA levels" Same, p.10.

**Valiant Communications**
- "issued 6,00,000 Warrants on a preferential basis to the 'Non-Promoter' category at Rs. 768/- per Warrant" Q2 results, p.5, BAI 590c0cd1, 5-Nov-26.
- Only historic commentary exists (FY24 AR p.24, BAI e35dcf21): "The increase in the above reported margin and return ratios are primarily because of the reported increase in revenue." This is not current.

**Foseco India**
- "H1CY26 includes Foseco Crucible India Limited, & was not part of H1CY25" H1 CY26 deck, p.9 footnote, BAI 1b486a16.
- Jul-Sep 2026, derived: standalone EBITDA 17.5% (Jun-26 17.7%, Sep-25 18.3%); consolidated 22.2%. BAI f1277d9f pp.2-5, 6-Nov-26.
- 2026 price increase: NOT FOUND. The Aug-26 deck on fosecoindia.com returned 403 and renders image-only.

**Adroit**
- "we aim to maintain an EBITDA margin of approximately 30%, plus or minus 2 percentage points, supported by disciplined procurement, manufacturing efficiency and appropriate pricing." Q2 call, p.5, BAI 9c0604c8, 28-Oct-26.
- "Certain products may sell only around 200 units a year but can deliver margins of approximately 50%." Same, pp.8-9.
- Utilisation: forging "approximately 93% - 94%"; Pithampur "around 81%". Machining doubles in Q4 FY27; forging 3,000 to 5,500 t in Q1 FY28 (pp.4,10).

**Uniparts**
- "Q2 delivered 23.4% EBITDA margins despite the raw material and West Asia inflation." Q2 call, p.10, BAI 231c97b1, 5-Nov-26.
- "our contracts with customers are that we pass on the raw material increase through to customers. However, this pass happens through a lag." Same, p.6.
- Capex "around INR60 crores to be spent over next year" (p.5).

**Kennametal India**
- "The financial results for the quarter ended September 30, 2026 were primarily driven by the favorable timing of raw material-related pricing compared to costs." Board outcome note 3, p.6, BAI cdee140b, 12-Nov-26.
- Press release cites "historically high tungsten prices" (p.7).

**Thyrocare**
- "When you're growing at 25%, your cost never grows at 25%. So, you get a significant operating leverage into the business." Q2 call, p.16, BAI dc640cb3, 29-Oct-26.
- "a long-term guidance of about 31%, 31.5% ... is what I would anchor on, right, and not above that." Same, p.16.
- "taken an impairment of INR9 crores in Thyrocare standalone books and of INR45 crores in the consolidated financials against the goodwill arising from the acquisition of NHL." Same, p.8. NHL sale consideration is about INR 141 cr (p.17).

**Kanohar**
- "There is no one-off as such, but having said that, it will be fair to say that there is variation in the, quarter-to-quarter or order-to-order kind of margins." Q2 call, p.8, BAI e82ab857, 3-Nov-26.
- "we don't have a specific reason why we are guiding towards a lower number" Same, p.17.

**SRM Contractors**
- "Previous periods' figures are regrouped to make them comparable with those of current period, wherever applicable." Q2 results notes, pp.7,13, BAI 97e05fb8, 14-Nov-26.
- Reclassification check: no specific reclassification is disclosed. Standalone material share fell to 65.7% from 71.6%, and direct-expense share rose to 11.2% from 7.0% (derived). The RHP says "Sub-contracting charges includes payments on account of sub-contracting with materials" (BAI b975c289 p.50). So material inside subcontracts can move between the two lines. Not proven either way.
- Data flag: the consolidated Q2 FY26 comparative column does not reconcile to the standalone column.

**BCC Fuba**
- "Paid-up Equity Share capital of Company stands at Rs. 19,89,89,015 comprising of 1,98,94,738 Fully Paid-up Equity Shares ... and 8,327 Partly Paid-up" BAI 07b1fe9a p.1, 11-Sep-26. This is a rights issue (call money Rs 37.50, BAI 079bf49f, 29-Apr-26).

**Exato**
- "There is a strong contribution from the international business, and we saw very strong order execution happening in Q1" Q1 call, p.7, BAI 2d711ada, 19-Aug-26.
- "in the initial year of setup the margins are going to be relatively lower... would be in the range of 10 to 12%" Same, p.22.

**Technocraft Ventures**
- "advance payments have enabled the Company to secure competitive discounts on the procurement of raw materials, thereby contributing to improve the profitability." Board comment, monitoring agency report, p.5, BAI 56aa4135, 4-Nov-26.
- "Delays in certification of work done, disputes on variation claims, or fiscal constraints of the awarding authority can lead to extended collection timelines" RHP p.37, BAI 82a0ee41, Aug-26.
- Filing defect: H1 results note 5 says "have not been subject to limited review or audit", but note 1 says a limited review was done (BAI ff056c41 p.10, 14-Nov-26).
- Dispute: RUIDP arbitration, about Rs 50.15 mn, "in abeyance" (RHP p.37).

**Kwality Pharmaceuticals**
- "the portfolio of registered products from the Latin market and the MENA region has been the major driving force" Q2 call, p.15, BAI e257576b, 13-Nov-26.
- "another INR60 crore-INR70 crores of debtors were stuck in the Middle East. But that all realized in Q1 and Q2." Same, p.14.
- "we have actually taken an extended loan. However, we have not utilized it." Q1 call, p.11, BAI 65e1b815, 10-Aug-26.
- Internal conflict: the Q1 call said the hormone plant finishes in Nov-26, but the Q2 call says it goes live in Q3 FY28.

**M E T S (Maestros Electronics & Telecommunications Systems, BSE 538401)**
- No management commentary is filed. Q2 other income is Rs 128.12 lakh consolidated (Rs 127.53 lakh standalone) against PBT of Rs 411.45 / 408.57 lakh, about 31%, derived (BAI 4abdf46a p.4).
- The other-income composition is not itemised. H1 cash-flow non-operating items: interest Rs 110.04 lakh, rent Rs 20.77 lakh, sundry balances written back Rs 47.47 lakh (p.14). That totals Rs 178.88 lakh against H1 other income of Rs 180.05 lakh. [INFERENCE] The Q2 jump is mostly the write-back, which does not recur.

**Marine Electricals**
- "This momentum has also translated into improved profitability, reinforcing the strength of our operating performance." Q2 PR, p.3, BAI f0114a43, 4-Nov-26.
- "Change in working capital remains 2H-weighted in line with the order execution cycle" Deck, p.45, BAI d6340b24, 22-Sep-26. Debtor days: FY25 155, FY26 176.
- "Type of Issue: Preferential Issue; Type of specified securities: Warrants fully convertible into Equity shares" ICRA MA report p.3, BAI 791529cb, 4-Nov-26.
- FY26 consolidated ageing: Rs 43,300 lakh total; Rs 2,500 lakh above 3 years; ECL Rs 527 lakh (AR FY26 note 57 p.305, BAI 5e1f1335). H1 FY27: bad debts written off Rs 272.84 lakh against Rs 10.91 lakh a year earlier (BAI 38d5b9cf p.6).
- Customers named (not a receivables split): Navy, Coast Guard and PSU shipyards on the defence side; Adani Connex, STT, Equinix and others on the data-centre side. Open orders: Industrial Rs 3,065 cr against Defence & Marine Rs 449 cr.

**Silver Touch**
- "EBITDA nearly doubled at Rs 17.04 Cr (+89% YoY), with margin expanding ~782 bps to 22.21%, driven by software-led operating leverage." Q1 deck, p.6, BAI a746b291, 23-Sep-26.
- The auditor's limited review carries a reservation: "except for the possible effects of the matter described in paragraph 8". The matter is unaudited foreign subsidiaries with Rs 7,074 lakh of assets (BAI 1c478f1b p.15, 29-Oct-26).
- Q2 FY27 margin commentary NOT FOUND.

**KRM Ayurveda**
- "Ministry of Defense was running a pilot project wherein they empaneled our hospitals" and "we do not have to spend much on marketing either." Q4 FY26 call, pp.8-9, BAI d908f605, 5-May-26. This is a pre-H1 reason; no H1 FY27 reason is stated.
- "Trade Receivables turnover ratio – Decrease in ratio on account of increase in amount due from the Government Panel Debtor." AR FY26 p.184, BAI 0f264fe7.
- Mar-26 ageing: 20.2% older than 6 months; "There are no disputed trade receivables" (AR FY26 note 15 p.138, BAI f9cea8fe).

**Menon Bearings**
- "we have reduced substantially so far as the consumption of all these raw material and input material is concerned." Q2 call, p.6, BAI d17076f4, 30-Oct-26.
- "productivity has substantially increased, that is by 25% over last period. That has really helped us in reducing the overheads overall." Same, p.6.
- "we have built up our inventories with the customers in USA, so which were to the extent of three months." Same, p.23.
- Material vs other costs check: no regrouping note in the 29-Oct-26 results. Management treats it as a real change, with input prices up (tin +72%, copper +50%) and overhead absorption up. Unsettled: management did not explain the fall in other expenses line by line. The consolidated receivables figure of Rs 9,992 lakh is from a garbled pdftotext; check it against the PDF.

**Marsons**
- No management text is filed. The screener announcement is titled "Unaudited Financial Results (Standalone & Consolidated) Revised For 30Th September 2026". It matches BAI 4f09c9f3, which is final.
- The FY25 ageing shows 23.9% older than 6 months, with no ECL.

**CFF Fluid Control**
- "the Company has adopted Indian Accounting Standards ("Ind AS") ... with effect from 1 April 2026" Results note 2, p.5, BAI 0c8e2dea, 13-Nov-26.
- Reg 32 "Yes" deviation: "The unutilized amount of issue expenses has been utilized for General Corporate Purpose." That is a Rs 27.51 lakh shift (BAI 008651cb p.2, 5-May-26).
- Mar-26 ageing: Rs 10,461 lakh, nothing beyond 1 year (AR FY26 p.113).

**Adisoft**
- "Billing of the service components has been more in this first half. So, that's why you can see the service impact on this overall PAT margin improvement." Q2 call, p.4, BAI 972a32ba, 6-Nov-26.
- "we are targeting a revenue growth of around 25%, a sustainable PAT margin of around 13% to 14%" Same, p.4.
- Capex: about Rs 33 cr Bhosari facility from IPO money, operational by end Q3 FY27 (p.11).

**Om Power Transmission**
- "79% of the revenue mix comes from the transmission line vertical. And sub-station vertical 17%." Q2 call, p.6, BAI bf9768dd, 2-Nov-26.
- "so that's why retention accumulation is there. So that's why receivables temporarily spiked up but it will normalize" Same, p.8.
- "Trade receivables are inclusive of Retention money receivables." AR FY26 note 8, p.112, BAI 23031aa3. Loss allowance Rs 527 lakh at Mar-26.

**Mayur Uniquoters**
- "last quarter, it was abnormally high because of foreign exchange increase... So that was a onetime increase basically." Q1 call, p.6, BAI c2e2e2c7, 6-Aug-26.
- "it is varying because of raw material prices and crude oil prices." CFO, Q2 call, p.6, BAI c4f64911, 5-Nov-26.
- Q1 utilisation was 75-78%. An INR 50 cr additional line is planned (Q1 call p.6).

**Raghav Productivity Enhancers**
- "Sequential increase in share of value-added products (foundry, etc.) and R&D backed new variants in sales mix driving higher realizations and margin expansion." Q1 PR, p.2, BAI ba986c8d, 15-Jul-26.
- Q4 FY26 utilisation was 87%. Brownfield expansion to 5,34,000 MT was due Oct-26. Q2 commentary NOT FOUND.

**Nidhi Granites**
- "The Company's performance has been steadily improving and the outlook very promising with the addition of Fintech business." AR FY26 MD&A, p.39, BAI 1cb9fe2f.
- Business-model check: [INFERENCE from segment data] The cost ratio fell because revenue mix changed. Garments went from Rs 853.91 lakh to Rs 0.06 lakh. An IT-services subsidiary acquired 1-Apr-25 added Rs 1,722.81 lakh of revenue with almost no material cost (AR Note 33 p.118, Note 40 p.129). Management does not explain it. A further "Acquisition" filing dated 22-Oct-26 is unread.

**Bajaj Consumer Care**
- "our teams... deliver very strong savings in fixed costs and employee costs, which have allowed us to deliver a near-term high EBITDA margin of 25%" MD, Q2 call, p.5, BAI 1f505424, 15-Oct-26.
- "Our consolidated A&P spend for the quarter were up 7% over the same period last year, and are up 18% on H1 basis." Same, p.3.
- Slide: A&P 12.5% of sales against 14.9%; employee cost 10.3% against 13.1%; other expenses 12.0% against 14.6%; gross margin 59.9% against 59.7% (Q2 deck p.21, BAI 2ebf29c1). Derived: about 2.4 of the 6.4-point EBITDA gain is the A&P ratio, all from sales leverage.

**Frontier Springs**
- "Part of this growth came from executing orders that could not be completed in Q1, when raw material availability was constrained" MD, Q2 deck, p.21, BAI 549a68df, 12-Nov-26.
- "Higher steel, oil and gas prices could put some pressure on margins in the coming quarters" Same, p.21.
- The Q2 call was held 16-Nov-26. Only the audio intimation exists (BAI fabb16dd); no transcript yet.

## Open gaps and where each fact should exist

| Name | Missing | Where it should exist |
|---|---|---|
| KMC | Margin reason, guidance, capex | BSE Investor Presentation Q2 FY27 (due after 13-Nov-26 results) |
| Valiant | Any margin commentary | BSE Annual Report FY26 MD&A (not in Bull AI) |
| Foseco | 2026 price rise and whether it held | H1 CY26 concall transcript (Aug-26) and deck on fosecoindia.com, image-only; operator copy needed |
| Timex | Reclassification note, capex | Q2 FY27 results notes pp.4-5 (BAI 408ac237) |
| SRM | Margin reason | BSE Investor Presentation Q2 FY27 (not yet filed) |
| BCC Fuba, M E T S, Marsons, CFF | Margin reason, receivables reason | No concall or deck filed; AR FY26 MD&A only |
| Marine | Margin reason, receivables by customer | NSE Q2 FY27 concall transcript; AR FY26 related-party notes |
| Exato, Frontier | Q2 margin reason | Q2 transcripts: Exato call 19-Nov-26; Frontier call 16-Nov-26 |
| Raghav | Q2 margin reason | BSE Q2 FY27 press release / deck (not in Bull AI) |
| Silver Touch | Receivables reason, Q2 commentary | AR FY26 notes; Q2 FY27 deck |

## Verification

Files quoted, with dates (Bull AI document_id prefix): Timex Q2 call 2a2600a5 (4-Nov-26), Q2 deck 5cb49176 (3-Nov-26), Q2 results 408ac237 (3-Nov-26); MPS Q2 call c2ccb704 (4-Nov-26), Q1 call 38ba42fa (29-Jul-26); KMC Q1 deck 38b74eb0 (28-Aug-26), Q2 results 805e4052 (13-Nov-26); Krishna Defence Q2 call 1dd3ab90 (30-Oct-26); Valiant Q2 results 590c0cd1 (5-Nov-26), FY24 AR e35dcf21; Foseco Jul-Sep results f1277d9f (6-Nov-26), H1 CY26 deck 1b486a16 (Aug-26); Adroit Q2 call 9c0604c8 (28-Oct-26); Uniparts Q2 call 231c97b1 (5-Nov-26); Kennametal board outcome cdee140b (12-Nov-26); Thyrocare Q2 call dc640cb3 (29-Oct-26); Kanohar Q2 call e82ab857 (3-Nov-26); SRM Q2 results 97e05fb8 (14-Nov-26), Q1 deck b5fa430a (14-Aug-26), RHP b975c289; BCC Fuba Q2 results 7ba7d3a5 (Nov-26), capital filings 07b1fe9a (11-Sep-26), 079bf49f (29-Apr-26); Exato Q1 call 2d711ada (19-Aug-26), call invite 8fde0397 (16-Nov-26); Technocraft MA report 56aa4135 (4-Nov-26), RHP 82a0ee41 (Aug-26), Q2 results ff056c41 (14-Nov-26); Kwality Q2 call e257576b (13-Nov-26), Q1 call 65e1b815 (10-Aug-26), H1 deck c84578a8 (12-Nov-26); M E T S Q2 results 4abdf46a (5-Nov-26); Marine PR f0114a43 (4-Nov-26), deck d6340b24 (22-Sep-26), ICRA MA 791529cb (4-Nov-26), board outcome 38d5b9cf (4-Nov-26), FY26 AR 5e1f1335 (Sep-26); Silver Touch Q1 deck a746b291 (23-Sep-26), Q2 results 1c478f1b (29-Oct-26); KRM Q4 FY26 call d908f605 (5-May-26), Q2 deck 96020c1a (14-Nov-26), AGM/AR 0f264fe7 (7-Sep-26), AR f9cea8fe (5-Oct-26); Menon Q2 call d17076f4 (30-Oct-26); Marsons revised results 4f09c9f3 and earlier filing 4fdfeb8b (both 13-Nov-26); CFF Sep-26 results 0c8e2dea (13-Nov-26), Reg 32 008651cb (5-May-26), FY26 AR beccbe91; Adisoft Q2 call 972a32ba (6-Nov-26), H1 results bf839e6c (4-Nov-26); Om Power Q2 call bf9768dd (2-Nov-26), Q2 deck b88d3acc (2-Nov-26), FY26 AR 23031aa3; Mayur Q1 call c2e2e2c7 (6-Aug-26), Q2 call c4f64911 (5-Nov-26); Raghav Q1 PR ba986c8d (15-Jul-26), deck 01c1070d (1-Sep-26); Nidhi FY26 AR 1cb9fe2f (Jun-26); Bajaj Consumer Q2 call 1f505424 (15-Oct-26), Q2 deck 2ebf29c1 (14-Oct-26); Frontier Q2 deck 549a68df (12-Nov-26), call intimation fabb16dd (17-Nov-26). Screener.in announcement list for Marsons, via Chrome, 17-Nov-26. No exchange PDF was re-read against Bull AI text except Marsons (the two filings) and Kennametal (BSE PDF 403; the Bull AI chunk is the BSE filing). No other CONFLICT was found.
