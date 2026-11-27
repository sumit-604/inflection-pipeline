# STAGE 4: BUSINESS MODEL DECODER. Azad Engineering Ltd (AZAD). Run 2026-11-15

Model: claude-sonnet-5-5. Inputs read: Annual_Report_2026 (AR26), Annual_Report_2025 (AR25, pointer only), AZAD_Prospectus_2023-12-23 (PRO), AZAD_Q2FY27_investor_presentation_2026-11-06 (Q2P), AZAD_Q2FY27_results_2026-11-06 (Q2R), AZAD_Q2FY27_concall_transcript_2026-11-14 (Q2C), AZAD_CARE_rating_rationale_2026-06-22 (CARE), and blocks B00 to B03 plus conflicts.yaml. All cites use [page N] of the PDF named. Not opened by this stage: the Q1 FY27 presentation and results, the Q4 FY26 and Q1 FY27 concalls, the peer concalls, the shareholding file. The Q2 deck carries the H1 data, so no number here depends on them.

UNITS. AR26, Q2R, Q2P and PRO financials are in Rs Mn (INR million). CARE and the concall speak in Rs Cr. 1 Rs Cr = 10 Rs Mn. Every figure carries its unit. No silent conversion. "calc" means this stage computed it from anchored lines. "mgmt" means a management claim, not audited.

---

## 0. SETTLED AT THE PAGE: THE Q2 FY27 REVENUE BASIS QUESTION

The two figures are the same quarter on two different perimeters. Both are revenue from operations. Neither is total income.

| Figure | Line it is | Perimeter | Value in Rs Mn | Source |
|---|---|---|---|---|
| Rs 187.8 Cr (Q2) | Revenue from operations | Standalone (parent only) | 1,878.03 | Q2R [page 3] statement of standalone results; Q2C [page 5] "standalone revenue from operation reached INR187.8 crores" |
| Rs 358.3 Cr (H1) | Revenue from operations | Standalone | 3,583.22 | Q2R [page 3]; Q2C [page 5] |
| Rs 190.94 Cr (Q2) | Revenue from operations | Consolidated (parent + Azad VTC + Azad Prime) | 1,909.35 | Q2R [page 9] |
| Rs 363.53 Cr (H1) | Revenue from operations | Consolidated | 3,635.34 | Q2R [page 9]; Q2C [page 6] "consolidated H1 revenue was INR363.5 crores" |
| Rs 192.46 Cr (Q2) | Total income | Standalone | 1,924.58 | Q2R [page 3] (not what the concall quotes) |
| Rs 195.11 Cr (Q2) | Total income | Consolidated | 1,951.05 | Q2R [page 9] |

Reading: the CFO states "unless I mention otherwise, the figures are standalone" (Q2C [page 5]). So 187.8 and 358.3 are standalone revenue from operations. The consolidated figures are 190.94 and 363.53. The gap is subsidiary revenue net of intercompany: 31.32 Rs Mn in Q2 and 52.12 Rs Mn in H1 (calc from the rows above). Growth rates differ slightly by perimeter: Q2 standalone +31.6% (Q2P [page 6]) vs consolidated +31.1% (calc 1,909.35 / 1,456.25, Q2R [page 9]); H1 standalone +29.3% vs consolidated +28.6% (calc 3,635.34 / 2,827.17). The conflict in conflicts.yaml (item "Q2 FY27 consolidated revenue") is closed: no source is wrong.

Presentation blemish found while settling this: Q2P [page 7] chairman text says "Revenue grew 26.8% Y-o-Y this quarter" and shows "Rs xx in Q4FY26 to Rs yy in Q1FY27" placeholders. The 26.8% matches Q1 FY27 standalone growth (1,705.19 / 1,345.12, Q2R [page 3], calc), not Q2 (31.6% in the same deck, Q2P [page 6]). The slide text is stale copy from the prior quarter. Use the tables, not that text.

---

# SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

## 1A. One-line description

Azad makes precision metal parts, mainly turbine blades (airfoils), to a customer's drawing for gas turbine, steam turbine, aircraft engine and oil and gas equipment makers, ships about 93% of them abroad, and gets paid per part under multi-year supply contracts (AR26 [page 6], [page 17]; Q2P [page 16]).

## 1B. Money flow chain for each revenue stream

| Stream | Input | What Azad does | What it delivers | Who pays | How they pay |
|---|---|---|---|---|---|
| 1. Energy turbine parts (compressor and turbine airfoils, machined components) | Customer-approved alloy bar and castings bought back to back from mills the customer names (AR26 [page 33]; PRO [page 226]) | Forges, machines to micron tolerance, heat treats, coats, inspects (AR26 [page 17], [page 22]) | Qualified airfoils and machined parts, plus a growing share of non-airfoil parts (airfoils ~75% of energy output vs ~90% four years ago, AR26 [page 20]) | GE Vernova, Siemens Energy, Mitsubishi Heavy Industries, Baker Hughes, BHEL (AR26 [page 9], [page 30]; Q2P [page 10]) | Per part, on delivery, export credit terms 120 to 180 days (CARE [page 3]); customers pay in foreign currency (net long USD exposure, AR26 [page 245] via B03) |
| 2. Aerospace and defence parts | Titanium, nimonic, inconel and aluminium (PRO [page 226]) | Same make-to-print process; aero engine airfoils, APU and actuator parts; assembles and integrates a full turbojet engine for GTRE (AR26 [page 22]) | Aero systems parts (Honeywell, Eaton, Boeing, HAL, Godrej, Tata) and aero engine airfoils (Rolls-Royce, Pratt & Whitney Canada, Safran MOU) (AR26 [page 22]) | Global aero OEMs; Indian defence bodies | Per part on delivery; the GTRE engine is a one-off programme and "not reflected in management revenue guidance" (AR26 [page 22]) |
| 3. Oil and gas parts | Same alloys and steels | Drill bits, bonnet frames, slips, hatch covers; airfoils for Baker Hughes (AR26 [page 23]) | Parts from a 7,600 sq m dedicated Baker Hughes plant opened April 2026 (AR26 [page 23]) | Baker Hughes (Nuovo Pignone agreement to CY2030, Q2P [page 10]) | Per part. FY26 revenue "under Rs 100 Mn" (AR26 [page 19], [page 23]) |
| 4. Job work (reported as "Sale of services") | Parts or material sent for processing (customer or in-group) | Machining, coating, heat treatment as a service (AR26 [page 200] policy) | Processed parts | Customers; possibly in-group | Fee at the point the processed goods are sent. 1,193.62 Rs Mn FY26 (AR26 [page 229]). Who owns the material: NOT FOUND, check concall |
| 5. Other operating revenue | Scrap generated; export schemes | Sells scrap; claims export incentives | Cash from scrap and incentives | Scrap buyers; government | 55.54 + 29.08 Rs Mn (AR26 [page 229]) |

## 1C. Revenue model classification

Two cuts are shown because the AR gives two. Cut A is by accounting nature (consolidated, AR26 [page 229]). Cut B is by end market (standalone, AR26 [page 18], [page 31]).

Cut A. Consolidated revenue from operations FY26 = 6,029.75 Rs Mn (AR26 [page 192]).

| Stream | Type (taxonomy) | Description | Rs Mn | % of revenue (calc) | Predictability |
|---|---|---|---|---|---|
| Sale of products | Transactional, per-unit, under long-term supply contracts (make-to-print) | Parts sold at contract price per piece | 4,751.51 | 78.8% | High on contracted programmes; Medium on timing (qualification, delta qualification) |
| Sale of services (job work) | Fee-for-service | Processing charges | 1,193.62 | 19.8% | Medium. Grew +71.7% (1,193.62 vs 695.17) vs products +27.0% (calc, AR26 [page 229]). Reason not stated: NOT FOUND |
| Scrap sales | Incidental | Alloy scrap | 55.54 | 0.9% | Low |
| Export incentives | Government scheme | Duty and export benefits | 29.08 | 0.5% | Low |

Cut B. Standalone revenue from operations FY26 = 5,903.8 Rs Mn.

| End market | Type | Rs Mn | % of revenue | Growth | Predictability |
|---|---|---|---|---|---|
| Energy and Oil & Gas (one reported segment) | Contracted OEM supply, 3 to 10 year agreements (PRO [page 33]; CARE [page 1] says typically 4 to 5 years) | 4,811.3 | 81.5% (AR26 [page 19]) | +34.2% | High on volume visibility, Medium on timing |
| of which Oil & Gas | Early programme | under 100 | under 1.7% calc | n/a | Low (first year of revenue is FY27, AR26 [page 23]) |
| Aerospace & Defence | Contracted OEM supply plus one development programme | 1,012.6 | 17.2% (AR26 [page 21]) | +25.4% | Medium (aero engine qualification still open) |
| Others (scrap, incentives) | Incidental | 79.9 | 1.35% calc | n/a | Low |

Order book 65,000 Rs Mn at 31 March 2026 = 10.8x consolidated revenue (calc 65,000 / 6,029.8). Split by value: Energy ~37,000 (about 57%), Aerospace & Defence ~18,500 (about 29%), Oil & Gas ~9,500 (about 14%) (AR26 [page 18], [page 19], [page 21], [page 23]). It is a management estimate and "not audited" (AR26 [page 18]). Average contract tenure 5 to 6 years (AR26 [page 18]).

Small unreconciled gap: AR26 [page 30] says Energy is 79.7% of standalone revenue and [page 19] says Energy plus Oil & Gas is 81.5%. The difference of 1.8 points is about 106 Rs Mn (calc on 5,903.8), while [page 19] and [page 23] say Oil & Gas revenue is under 100 Rs Mn. The gap is about 6 Rs Mn and rounding may explain it. Not resolved in the AR.

H1 FY27 mix (standalone, Q2P [page 8]): Energy and Oil & Gas 2,904.6 Rs Mn (81.1%), Aerospace & Defence 603.7 (16.8%), others about 74.9 (2.1%, calc). Domestic share rose to 12.0% from 6.1% (domestic 430.3 vs 168.2 Rs Mn, +155.9%, Q2P [page 8]). The CFO ties this to BHEL indigenisation (Q2C [page 5]). A GTRE engine delivery on 22 July 2026 (AR26 [page 22]) may also sit in domestic revenue. That link is an [INFERENCE]; the company does not state it.

## 1D. Business model canvas

| Element | Answer | Source |
|---|---|---|
| What they sell | Mission-critical precision parts made to the customer's drawing. 1,700+ qualified components, 45+ qualified processes | AR26 [page 32], [page 33]; Q2P [page 16] |
| Who buys | A small set of global turbine and aero engine makers. Top customer 18.64%, top five 47.02% of consolidated revenue (calc, 1,123.97 and 1,711.10 on 6,029.75 Rs Mn). Names of the two customers at or above 10%: NOT FOUND | B03 triple-pass; AR26 [page 242], [page 237] |
| Why them | Qualification takes 30 to 48 months per supplier; zero-defect ppm limits; a switched OEM must repeat it. Management estimates 15 to 20 years for a new entrant to match the portfolio | AR26 [page 31], [page 32] |
| How delivered | 93% exported (standalone); six customer-dedicated plants of 44,800 sq m total at Tuniki Bollaram (Q2P [page 9]); about 20,000 sq m operating before that | AR26 [page 6]; Q2P [page 9], [page 16] |
| Cost structure | Labour and conversion cost dominate, not material. Per Rs 100 of FY26 consolidated revenue (calc): net materials 9.6, employees 22.5, other expenses 30.5, EBITDA 37.4, depreciation 8.8, finance cost 5.1 | AR26 [page 192], [page 230], [page 231] |
| Scarce resource | Qualified status with named OEMs and machines/people to run it. The AR names skilled machining talent as scarce | AR26 [page 33] |
| Pricing power source | Partial. Price fixed per part in long-term contracts; "firm pricing" (AR26 [page 6]) but also "pricing competitively against international suppliers" (AR26 [page 33]). Some contracts require year-on-year price cuts and cost-efficiency demonstrations (PRO [page 33]). Raw material is passed through, Azad absorbs a plus or minus 5% band (AR26 [page 34]) | as cited |
| Asset intensity | Heavy. PPE + CWIP + right-of-use = 12,017.65 Rs Mn of 24,046.59 total assets at 30 Sep 2026 (50.0%, calc, Q2R [page 10]) | Q2R [page 10] |
| Working capital intensity | Very high. Company days 244 (FY26) vs 202 (FY25) (AR26 [page 7]); CARE cycle 344 vs 287 days (CARE [page 3]) | as cited |
| Regulatory moat or burden | Moat is private (OEM audits, Nadcap, AS9100, EDF/Arabelle approval, CARE [page 3]; AR26 [page 22]). No licence moat. Burden: export dependence and trade policy risk (AR26 [page 34]); land title on the core campus (B03) | as cited |

## 1E. The chai-stall-uncle version

Imagine a tiny workshop that makes one special bolt for a jet engine. The engine company will not buy from you until its own inspectors have spent three or four years checking your shop. After that, they do not change you, because checking a new shop costs them the same three or four years again. Azad is that workshop, grown up. It now makes 1,700 such parts, mostly for power plant turbines, and it sells almost all of them abroad. The catch is cash. Azad buys expensive metal months before the customer approves the part, and then waits another 4 to 6 months after delivery to be paid. So profit shows on paper while the bank balance falls, and that is the number to watch.

## Section 1 summary table

| Item | Answer |
|---|---|
| Business type | Manufacturing, build-to-spec precision components, export led |
| Revenue nature | Per-unit product sales (79%) plus job work (20%), under multi-year OEM contracts |
| Asset intensity | Heavy and rising (50% of assets in plant and CWIP at Sep 2026) |
| Working capital intensity | Very high (company days 244; CARE 344; calc 369 on annualised H1 revenue, B01) |
| Pricing power | Moderate. Contracted price, raw material pass-through, annual price-down clauses in some contracts |

---

# SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

## 2A. Five forces

| Force | Plain answer | Helps / hurts / neutral | Source |
|---|---|---|---|
| Competition | Management says the field is narrow: suppliers in the US, Europe, China and Japan (AR26 [page 17], [page 30]). CARE names three global peers, AECC Aero Science & Tech, Pietro Rosa and Wuxi, and calls Azad one of four major global players for this class of part (CARE [page 3]). Count of qualified suppliers per part: NOT FOUND | Helps | as cited |
| Entry barriers | 30 to 48 months to qualify, ppm-level defects, capital for plants, separate qualification per component (AR26 [page 31]; Q2P [page 19]). Qualification even repeats when an approved part moves to a new plant ("delta qualification", Q2C [page 8]) | Helps | as cited |
| Supplier power | Raw material comes from "a limited pool of approved mills" the customer mandates (AR26 [page 33]); minimum order quantity forces bulk buys of customised alloy (CARE [page 3]). Cost is passed through within a plus or minus 5% band (AR26 [page 34]) | Hurts on cash, neutral on margin | as cited |
| Customer power and concentration | High. Two customers at or above 10% of revenue (AR26 [page 237]); top one 18.64% and top five 47.02% (calc, B03; AR26 [page 242]). Contracts can be terminated "including without cause", with price-down clauses in some (PRO [page 33]). Offsetting: customers carry the qualification cost and "do not generally reconsider incumbent suppliers" (AR26 [page 31]) | Hurts | as cited |
| Substitutes | Components must match part numbers qualified in a given engine design; no like-for-like substitute inside a programme. A design change to a new engine generation is the real threat, and it is also a new qualification (AR26 [page 29]) | Neutral | AR26 [page 29] |

## 2B. Competitive positioning map

Peer data in the prospectus is FY23 and stale. Use it for shape, not level. Live peer numbers belong to the peer-concall stages.

| Company | Why comparable | FY23 revenue (Rs Cr, as printed) | FY23 EBITDA margin | FY23 ROCE | Source |
|---|---|---|---|---|---|
| Azad Engineering | n/a | 262 | 31.4% | 14.9% | PRO [page 190], [page 191] |
| MTAR Technologies | Precision parts for clean energy, space, defence | 593 | 29.2% | 21.4% | PRO [page 190], [page 191] |
| Paras Defence & Space | Defence optics and space | 231 | 28.1% | 12.2% | PRO [page 190], [page 191] |
| Dynamatic Technologies | Aerospace and hydraulics (A&D about 34% of revenue in 2021) | 1,326 | 14.4% | 13.2% | PRO [page 190], [page 191] |
| Maini Precision | Precision components | 841 | 22.3% | 48.4% | PRO [page 190], [page 191] |
| International Aerospace Manufacturing | Aerospace parts | 192 | 16.5% | 18.3% | PRO [page 190], [page 191] |
| AECC Aero Science & Tech, Pietro Rosa, Wuxi | Global peers per CARE | NOT FOUND | NOT FOUND | NOT FOUND | CARE [page 3] |

Azad's FY26 consolidated EBITDA margin is 37.4% and its reported ROCE 10.7% (adjusted 15.3%) (AR26 [page 18], [page 32]; Q2P [page 16]). The margin gap to Indian peers is wide and has held since FY20 (PRO [page 191]). The ROCE gap has closed because Azad's capital base grew faster than its profit.

## 2C. Moat assessment (eight standard moat types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Switching costs | Yes, strong | 30 to 48 month qualification, per component; dedicated plants lock programme to Azad plant (AR26 [page 31]; Q2C [page 8]) | High per part. Low per customer, because wallet share is under 2% (Q2C [page 16]) and customers can qualify a second source on new parts |
| Intangible assets (qualifications, accreditations, process know-how) | Yes, strong | 1,700+ components, 45+ processes; Nadcap coatings and heat treatment; EDF/Arabelle approval (AR26 [page 22], [page 32]) | High, but decays if quality slips: "Withdrawal by a major OEM would remove revenue that could not be substituted" (AR26 [page 34]) |
| Cost advantage | Partial | Machining time reduction, local sourcing, backward integration; gross margin before depreciation 45.2% vs 43.7% a year ago (company metric, Q2C [page 5], [page 6]). Cost advantage vs Chinese suppliers: NOT FOUND | Medium |
| Efficient scale / niche | Partial | Few suppliers worldwide for hot section airfoils (AR26 [page 20]); Azad is small against global peers | Medium; improves as six plants fill |
| Network effects | No | Not a platform | n/a |
| Brand | No (B2B) | Customer awards exist (Q2P [page 22]) but do not set price | Low |
| Regulatory / licence | Weak | Defence work needs Indian approvals; no quota or licence protection stated | Low |
| Ecosystem lock-in via dedicated plants | Yes, new | Six customer-dedicated plants for four OEMs (Q2P [page 9]); "very high switching cost" claimed (Q2C [page 8]). Proof will be repeat volume, not yet shown | Medium until volumes ramp |

## 2D. Industry lifecycle

Growth phase, supply constrained. The AR states OEM order books have lengthened and supplier capacity "expanded far more slowly", so OEMs contract further forward and underwrite dedicated capacity (AR26 [page 28]). Azad sits in the early-to-middle scaling stage inside it: wallet share "historically low single-digit" (AR26 [page 17]) and "under 2%" (Q2C [page 16]), floor area being multiplied (about nine times at completion, AR26 [page 32]), and only the compressor-side airfoil line fully proven. Aero engine and hot section lines are in qualification, which is the stage the energy line was in years ago by management's own comparison (AR26 [page 31]).

## 2E. Key industry drivers

| Driver | Direction | Impact on Azad | Source |
|---|---|---|---|
| Gas turbine order intake ahead of OEM capacity (AI/data-centre power demand) | Up | Raises volume per qualified part | AR26 [page 28] |
| Installed-base replacement of rotating parts | Steady | Revenue less tied to new build cycle | AR26 [page 28] |
| Commercial aero build-rate recovery; supply chain the constraint | Up | Aero engine ramp opportunity | AR26 [page 29] |
| Indian defence indigenisation | Up | GTRE and domestic A&D | AR26 [page 29] |
| LNG liquefaction build (North America, Middle East) | Up | Oil & Gas vertical | AR26 [page 29] |
| Trade policy, tariffs | Unknown | 93% exports; "direction and timing outside the Company's control" | AR26 [page 34] |
| Raw material prices (nickel/titanium alloys) | Volatile | Pass-through within plus or minus 5% band; timing lag hits cash (PRO [page 37]) | AR26 [page 34]; PRO [page 37] |
| Rupee | Rupee weakness helps; net long USD | FX gain was 214.01 Rs Mn of other income in FY26 (AR26 [page 229]) | AR26 [page 229] |

Market-size claims (EY, quoted by the company, unverified here): Aerospace and Defence addressable Rs 1,190 bn (2023) to Rs 2,190 bn (CY29); energy turbine components Rs 310 bn (CY29) (Q2P [page 20], [page 21]). A third figure, Rs 930 bn CY29, appears unlabelled on Q2P [page 16]; it belongs to Oil & Gas by elimination [INFERENCE]. Verification of the EY report belongs to the market stage.

---

# SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

## 3A. Ignore these, track these

| Common ratio | Verdict for Azad | Why |
|---|---|---|
| Spot-year ROCE (10.7% reported; adjusted 15.3%) | MISLEADING right now | Capital employed includes 2,124.90 Rs Mn of CWIP (Q2R [page 10]) and 1,563.35 Rs Mn of unspent QIP capex object at March (B03). Plant carries cost before revenue. Use ROCE after plants reach steady output, not this year |
| Inventory turnover 0.22 (AR26 [page 32]) | IRRELEVANT as printed | Numerator is cost of materials less inventory change, no conversion cost (B03 triple-pass, finding 15). Use inventory days on a full cost base |
| Current ratio 3.29 (AR26 [page 32]) | MISLEADING | Held up by "other current assets" and receivables that are slow to cash. Fell from 5.30 as QIP cash was spent |
| Debt to equity 0.29 (AR26 [page 32]) | MISLEADING alone | Net debt moved from net cash 4,534.45 to net debt 2,720.48 Rs Mn in FY26 (B03), and to 4,740.69 Rs Mn at Sep 2026 (calc: borrowings 5,616.25 less cash and bank 875.56, Q2R [page 10]). The ratio ignores the speed of change |
| PAT margin and EPS growth | MISLEADING | Other income was 24.4% of FY26 PBT (B03); treasury income is falling as QIP cash is spent: other income H1 FY27 77.19 vs 209.36 Rs Mn (Q2R [page 9]). PAT fell 5.2% in Q2 while revenue rose 31.1% (Q2P [page 5]) |
| EBITDA margin (printed on three bases: 36.9%, 37.2%, 37.4%) | USE WITH A LABEL | Standalone reported 36.9%, adjusted 37.2%, consolidated 37.4% (AR26 [page 18]; Q2P [page 30]). EBITDA counts inventory build as a cost offset, so it runs ahead of cash |
| P/B | IRRELEVANT | Value sits in qualifications, not book assets |
| Order book to revenue multiple (10.8x) | CONTEXT ONLY | Unaudited management estimate, includes programmes still in qualification (AR26 [page 18]) |
| Dividend yield | IRRELEVANT | Cash is consumed by growth; no payout evidence read at this stage |
| Debtor days alone | MISLEADING | Export credit of 120 to 180 days is contractual (CARE [page 3]); read with inventory days and creditor days |

Track instead: operating cash flow after tax, working capital days on one fixed definition, gross margin before depreciation, EBIT margin (after depreciation), sequential revenue, CWIP to PPE transfer, and the top-customer share.

## 3B. Must-track metrics

No industry benchmark ranges are in the corpus (peer data stale). Healthy ranges below are the company's own history or its own guidance. That is the honest anchor.

### Growth

| Metric | What it tells | Healthy | Where | Red flag |
|---|---|---|---|---|
| Revenue growth vs guidance "over 25% per annum" (AR26 [page 36]) | Whether capacity converts to sales | Above 25%. Now: Q2 +31.1%, H1 +28.6% consolidated (calc, Q2R [page 9]) | Quarterly results | Below 25% for two quarters |
| H2 FY27 revenue vs required level | Whether FY27 guidance holds | H2 FY27 above 3,901.85 Rs Mn (calc: 1.25 x 6,029.75 less H1 3,635.34) | Q3 and Q4 results | H2 below that level |
| Sequential growth toward Rs 1,300 Cr run-rate | Whether the capacity story is real | About 9.3% per quarter for six quarters from Q2 FY27 base 1,909.35 Rs Mn to a 3,250 Rs Mn quarter (calc: 13,000 / 4) | Quarterly results | Sequential growth under 5% for two quarters |
| Aero and defence share of revenue | Mix shift toward higher-quality rung | Rising from 16.8% H1 FY27 (Q2P [page 8]) | Segment table | Falling below 15% |
| Order inflow vs conversion | Visibility vs delivery | Order book above 65,000 Rs Mn with revenue ramping | Presentation | Order book flat while revenue lags |

### Profitability and efficiency

| Metric | What it tells | Healthy | Where | Red flag |
|---|---|---|---|---|
| Gross margin before depreciation (company metric) | Pricing and conversion efficiency | Around 45% (45.2% Q2 FY27; 43.7% Q2 FY26, Q2C [page 5], [page 6]) | Concall | Below 43.7% |
| EBIT margin ex other income (calc) | True operating profit after plant cost | H1 FY27 26.3% (955.04 / 3,635.34, calc) vs 28.3% H1 FY26 | Results | Below 24% as depreciation steps up again in Q3 and Q4 (Q2C [page 6]) |
| Other income share of PBT | Quality of profit | H1 FY27 9.6% (77.19 / 804.57, calc) | Results | Above 25%, as FY26 was 24.4% (B03) |
| Incremental EBITDA margin | Operating leverage | 43.1% in H1 FY27 (calc) | Results | Falls below blended margin |
| Fixed asset turn (revenue / net PPE + CWIP) | Whether plants fill | Rising from 0.80x FY26 standalone (calc) toward management's 1.11x run-rate case (1,300 Cr on 1,169 Cr, Q2C [page 7]) | Balance sheet | Below 0.6x on annualised revenue |

### Balance sheet and risk

| Metric | What it tells | Healthy | Where | Red flag |
|---|---|---|---|---|
| Consolidated operating cash flow after tax | Whether profit is cash | Positive. H1 FY27 was (436.24) Rs Mn, FY26 (1,189.66) (Q2R [page 11]; B03) | Cash flow statement | Still negative in H2 FY27, or positive only after factoring, bill discounting or one-time advances |
| Working capital days, fixed definition | Cash cycle | Below 202 (FY25 company basis) | Chairman letter; concall | Above 244 (FY26) |
| Short-term borrowings | Funding of WC | Stable | Balance sheet | Current borrowings 2,746.58 vs 1,756.92 Rs Mn in six months (+56.3%, calc, Q2R [page 10]); a further rise with OCF negative |
| Interest cover | Debt safety | EBITDA / finance cost about 5.8x (management, standalone, Q2C [page 6]) | Results | Below 5.6x (B03 monitorable) |
| Customer concentration | Dependence | Top one under 20%, top five under 65% (operator tripwires; B03) | Notes to AR | Top one at or above 20% |

## 3C. Industry-specific non-financial KPIs

| KPI | Why | Where to find it |
|---|---|---|
| Dedicated facilities commissioned and their ramp stage | Capacity precedes revenue by quarters | Presentation; six plants now, 44,800 sq m (Q2P [page 9]) |
| Delta qualification completions | Gate to billing on a new plant | Concall; "several running at the same time" (Q2C [page 8]) |
| Rolls-Royce first shipment | Aero engine proof | AR26 [page 22] says before end FY27 |
| Capacity utilisation percentage | Operating leverage driver | NOT FOUND in AR26 or Q2P; ask management |
| On-time-in-full delivery and defect ppm | Qualification status | Customer awards only (Q2P [page 22]); metric NOT FOUND |
| Wallet share per OEM | Growth runway | "Under 2%" (Q2C [page 16]); no annual series |
| Headcount and training cadence | Scarce skill is a stated constraint | 2,500+ staff (AR26 [page 35]); training under 90 days per recruit (AR26 [page 7]) |
| QIP object spend | Capital discipline | Q2R [page 6]: 4,494.60 of 5,250.00 Rs Mn capex object spent; 755.40 unspent at 30 Sep 2026 |
| Share of top customer in revenue | Concentration | AR note on major customers |

## 3D. Unit economics

Defining one unit. The parts differ too much to price one "average part". The deck gives parts delivered since FY09 (3.82 million, Q2P [page 16]) but no annual count or price per part: NOT FOUND, so revenue per part cannot be computed. This stage uses two honest units: Rs 100 of revenue, and Rs 100 of net plant.

A. Per Rs 100 of consolidated revenue from operations (calc from the consolidated P&L, AR26 [page 192] and Q2R [page 9]).

| Line | FY26 (Rs) | H1 FY26 (Rs) | H1 FY27 (Rs) |
|---|---|---|---|
| Revenue | 100.0 | 100.0 | 100.0 |
| EBITDA excluding other income | 37.4 | 36.0 | 37.6 |
| Depreciation | 8.8 | 7.7 | 11.3 |
| EBIT excluding other income | 28.6 | 28.3 | 26.3 |
| Finance cost | 5.1 | 4.5 | 6.3 |
| Other income | 7.6 | 7.4 | 2.1 |
| PBT | 31.1 | 31.2 | 22.1 |
| PAT | 22.2 | 21.9 | 18.2 |

How these were built: H1 FY26 EBITDA = PBT 882.95 + depreciation 217.97 + finance 126.19 less other income 209.36 = 1,017.75 Rs Mn; H1 FY27 EBITDA = 804.57 + 411.31 + 227.66 less 77.19 = 1,366.35 Rs Mn (Q2R [page 9], [page 11]). The H1 FY27 figure agrees with the company's 1,366.4 Rs Mn (Q2P [page 5]).

B. FY26 cost shape (consolidated, Rs Mn, AR26 [page 192], [page 230], [page 231]).

| Cost | Rs Mn | % of revenue (calc) |
|---|---|---|
| Cost of materials consumed | 1,304.73 | 21.6% |
| Change in inventories (credit) | (723.50) | (12.0%) |
| Net material cost | 581.23 | 9.6% |
| Employee benefits | 1,355.23 | 22.5% |
| Other expenses (stores 263.65, job work charges 315.41, tools 270.42, power and fuel 263.16, transport 144.44) | 1,840.16 | 30.5% |

Reading the table: net material cost is low because 723.50 Rs Mn of cost was parked in work-in-progress and finished stock, not because parts are cheap to make. That inventory build is the same cost that shows as negative operating cash flow.

C. Volume, price and cost drivers.
- Volume drivers: qualified parts moved into serial production, plant fill at six dedicated plants, hours of machine time available (Q2C [page 8]).
- Price drivers: contract price per part, annual price-down clauses (PRO [page 33]), raw material pass-through inside plus or minus 5% (AR26 [page 34]), mix toward hot section and aero engine parts that carry "better return metrics" (AR26 [page 20]).
- Cost drivers: machine time and labour (employees plus other expenses = 53.0% of revenue, calc), alloy price, tooling, power. Management says local sourcing and backward integration into special processes lifted gross margin 150 bps (Q2C [page 5], [page 6]).

D. Incremental margin and operating leverage (calc).
- Incremental EBITDA margin H1 FY27: (1,366.35 less 1,017.75) / (3,635.34 less 2,827.17) = 348.60 / 808.17 = 43.1%.
- Incremental EBIT margin H1 FY27: (955.04 less 799.78) / 808.17 = 19.2%.
- Reading: operating leverage shows at EBITDA and is eaten by depreciation, which rose 88.7% (411.31 vs 217.97 Rs Mn). This agrees with B03 verdict 6 that the "operating leverage" claim does not yet show at EBIT. Management says depreciation steps up again in Q3 and Q4 as the September GE Vernova plants are capitalised (Q2C [page 6]).
- PBT bridge H1 FY27 vs H1 FY26: EBITDA +348.60, other income (132.17), depreciation (193.34), finance cost (101.47), net PBT (78.38) (calc, Q2R [page 9], [page 11]).

E. Capital per unit of revenue.
- FY26 standalone revenue 5,903.8 / average of (PPE + CWIP) 7,411 Rs Mn = 0.80x (calc; opening 4,010.2 + 797.8, closing 7,447.7 + 2,566.8, Q2P [page 32]).
- Management's case: Rs 1,300 Cr run-rate on Rs 1,169 Cr of fixed assets including CWIP = 1.11x (Q2C [page 7]).

### Key lever
One lever matters most: how fast Rs 4,273.54 Mn of inventory (Q2R [page 10]) turns into billed, approved parts. It sets cash, depreciation absorption and the ramp claim at once.

---

# SECTION 4: RISKS, VALUATION APPROACH & MONITORING

## 4A. Business-model-specific risks

| Category | Risk | First line item to deteriorate | Evidence now |
|---|---|---|---|
| Revenue model | Qualification or delta qualification slips, so plants sit unbilled | Work-in-progress and inventory grow faster than revenue | Inventory +73.9% vs revenue +31.8% in FY26 (B03); Sep 2026 inventory 4,273.54 vs 3,291.13 Rs Mn (+29.9%, calc) vs H1 revenue +28.6% |
| Revenue model | Customer concentration | Top-customer share in the AR note | Top one 18.64%, up 4.45 points (B03); two customers at or above 10% |
| Margin | Depreciation steps up faster than revenue | EBIT margin (not EBITDA) | 28.3% to 26.3% in H1 (calc); further step-up in Q3 and Q4 (Q2C [page 6]) |
| Margin | Raw material outside the plus or minus 5% band; annual price-downs | Gross margin before depreciation | 45.2% now; 43.7% a year ago |
| Balance sheet | Cash conversion does not turn | Operating cash flow after tax, and current borrowings | OCF (436.24) Rs Mn H1; net debt 4,740.69 Rs Mn (calc) vs 2,720.48 at March (B03); current borrowings +56.3% |
| Balance sheet | Non-operating items flatter OCF | OCF split: customer advances, bill discounting, non-recourse factoring | CARE: Azad is "exploring non-recourse factoring" (CARE [page 3]). Q2C [page 9]: bill discounting lines with ICICI Bank and DP World usable "from Q4 FY27"; one OEM agrees 50% advance on POs, about USD 4.5 Mn. AR26 prints no factoring wording (B03) |
| Execution | Capacity ramp claim fails: revenue ramp from Q4 FY27, full ramp by Q2 FY28, over Rs 1,300 Cr run-rate by end FY28 (Q2P [page 7]; Q2C [page 5]) | Sequential revenue growth in Q3 and Q4 FY27 | Management admits a 2 to 3 week delay already (Q2C [page 10]) |
| Execution | QIP object overrun; land title | Unspent QIP capex object; CWIP | 755.40 Rs Mn unspent at 30 Sep 2026 (Q2R [page 6]); deadline 31 March 2027 (B03); Tunkibollaram and Mangampet land issues (B03) |
| Structural | OEM order cycle or trade policy | Order inflow commentary and export share | Exports 88% in H1 FY27 vs 93.9% (Q2P [page 8]) because domestic rose, not because exports fell: exports grew +21.1% |
| Structural | FX | Other income (FX gain) | Net long USD; 5% rupee move = 104.07 Rs Mn pre-tax (B03; AR26 [page 245]) |

## 4B. Valuation method applicability (formal handoff to Role 1)

| Method | Applicable? | Reason |
|---|---|---|
| P/E on normalised earnings power | PRIMARY | Profitable, earnings explain value, and the destination PE is set by Section 1B. Normalise other income out and use post-depreciation earnings on ramped plants. EBITDA is flattered by inventory build |
| EV/EBITDA | SECONDARY cross-check | Removes the treasury-income and financing swing. Use with net debt including working capital borrowings. Read beside EV/EBIT because depreciation is rising fast |
| DCF (including reverse DCF) | TERTIARY, low weight | Free cash flow is deeply negative (FCF (6,914.46) Rs Mn FY26 calc, B03). Use only as a check on what the ramp must deliver |
| P/B | Not applicable | Value is qualification and earnings, not book |
| EV/Sales | Not applicable | Margins are high and differ from peers; sales multiple hides the cash gap |
| PEG | Limited | Growth guidance exists but earnings fell in Q2; use only as a sanity check |
| SOTP | Not applicable | One reportable segment for statutory purposes (Q2R [page 6]; AR26 [page 236]); segment margins NOT FOUND |
| NAV / replacement cost | Not applicable | Asset value is not the thesis |
| DDM | Not applicable | Growth company reinvesting; payout not read here |

Primary: P/E. Secondary: EV/EBITDA. Tertiary: reverse DCF. Cycle stage that matters: Azad's own capacity ramp stage (plants built, revenue and cash still lagging) matters more than the OEM order cycle, because the AR describes OEM backlogs as multi-year (AR26 [page 28]).

Sector cap row check (stage does not value). The manifest row "Cables / Industrial products" (25x) fits the revenue mix. Energy turbine parts are about 80% of revenue (79.7% energy, AR26 [page 30]; 81.5% with Oil & Gas, AR26 [page 19]) and aerospace and defence is 17.2% (AR26 [page 21]); these are industrial precision components, not defence equipment. Rows tested and rejected for today's revenue: Defence / strategic (38x) because Aerospace & Defence is 17.2% of revenue and the AR does not split civil aerospace from defence (NOT FOUND); EV charging / energy transition equipment (28x) because the turbines are mostly gas and steam; Recycling / Manufacturing (25x) gives the same number. On the order book, Aerospace & Defence is about 29% (AR26 [page 21]). If that share becomes revenue and a defence portion is evidenced, the row question reopens. The operator rules the row at the /fttcp pillar gate, as B00 states.

## 4C. Quarterly monitoring checklist

| # | Item | Good looks like | Trouble looks like |
|---|---|---|---|
| 1 | Consolidated OCF after tax | Positive in H2 FY27 without discounting or one-time advances | Still negative; or positive only after bill discounting from Q4 FY27 (Q2C [page 9]) |
| 2 | Working capital days (same definition each print) | Below 244, trending to 202 | Above 244. Ask for the definition (AR26 [page 7]) |
| 3 | Sequential revenue | About 9% a quarter toward 3,250 Rs Mn | Under 5% for two quarters |
| 4 | H2 FY27 revenue vs 3,901.85 Rs Mn | Above it | Below it |
| 5 | Gross margin before depreciation | At or above 45% | Below 43.7% |
| 6 | EBIT margin ex other income | Holds near 26% as depreciation rises | Falls below 24% |
| 7 | Inventory vs revenue growth | Inventory grows slower than revenue | Faster, as in FY26 |
| 8 | Current and total borrowings | Flat or falling | Up again while OCF is negative |
| 9 | Top-1 and top-5 customer share | Under 20% and under 65% | At or above either |
| 10 | CWIP and QIP object | CWIP down from 2,124.90 Rs Mn; 755.40 spent by 31 March 2027 | CWIP flat; deadline extended again |
| 11 | Rolls-Royce first shipment | Before end FY27 (AR26 [page 22]) | No shipment by Q4 FY27 |
| 12 | Domestic share and GTRE revenue | Stable | Domestic growth fades after one-off delivery |
| 13 | Other income share of PBT | Falling toward zero | Above 25% |
| 14 | Promoter holding and pledge | No further sale | Another sale (59.35% to 54.88% in FY26, B03) |

## 4D. Questions for management

| # | Question | Reassuring answer | Worrying answer |
|---|---|---|---|
| 1 | Define "working capital days" of 244 and say how it maps to CARE's 344 | Same formula each year, written down, with a target path | Definition changes, or no target |
| 2 | How much of H2 FY27 operating cash flow will come from discounting, advances or factoring, and how will each be reported? | Split disclosed; OCF positive before them | OCF positive only because of them |
| 3 | Which delta qualifications clear in Q3 and Q4 by plant, and what revenue is held up behind each? | Named plants and dates, small held-up revenue | Vague timing; revenue depends on one unqualified customer |
| 4 | Who are the two customers above 10%, and does either have a termination or price-down clause? | Multi-year volume commitments, no unilateral exit | Short contracts, price cuts each year |
| 5 | Why did job work revenue rise 71.7% while product sales rose 27.0%, and who owns the material? | Customer-owned material, so less cash tied up | Azad buys the material and sells it back as services |
| 6 | What utilisation do the six plants run at today, and what utilisation does the Rs 1,300 Cr run-rate assume? | Single figures per plant | Refusal, or a number that moves each quarter |
| 7 | When will the QIP capex balance of Rs 755.40 Mn be spent, and what is it for? | Dated list of orders | Another extension beyond 31 March 2027 |

---

# SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
+----------------------------------------------------------------------------------+
| AZAD ENGINEERING LTD (AZAD)          Business model card          Run 2026-11-15 |
+----------------------------------------------------------------------------------+
| ONE-LINE: Precision turbine and aero engine parts made to OEM drawings; 93% export |
| BUSINESS TYPE:     Manufacturing, build-to-spec components (AR26 p6, p17)          |
| REVENUE NATURE:    Per-part sales 78.8% + job work 19.8% (consol FY26, AR26 p229)  |
| END MARKETS:       Energy + Oil & Gas 81.5%; Aerospace & Defence 17.2% (AR26 p19,21)|
| ASSET INTENSITY:   Heavy. Plant + CWIP 50.0% of assets at Sep 2026 (calc)          |
| WC INTENSITY:      Very high. Company days 244 (FY25: 202); CARE cycle 344         |
| PRICING POWER:     Moderate. Contract price, pass-through +/-5%, price-down clauses|
| MOAT:              Qualification + switching cost (strong per part), dedicated     |
|                    plants (medium until volumes show). Wallet share under 2%        |
| CYCLICALITY:       Secular growth tied to OEM backlogs; export and OEM concentrated|
| CONCENTRATION:     Top-1 18.64%, top-5 47.02% (calc); tripwires 20% / 65%          |
| PRIMARY VALUATION: P/E on normalised earnings. Secondary EV/EBITDA. Tertiary rev DCF|
| SECTOR CAP ROW:    Cables / Industrial products 25x supported by revenue mix       |
+----------------------------------------------------------------------------------+
| TOP 5 MUST-TRACK                                                                   |
| 1. Consolidated OCF after tax    H1 FY27 (436.24) Rs Mn; need positive, undiscounted|
| 2. Working capital days          244 vs 202; same definition                       |
| 3. Revenue growth vs 25%         H1 +28.6%; H2 needs above 3,901.85 Rs Mn          |
| 4. EBIT margin ex other income   26.3% H1 FY27 vs 28.3%; depreciation rising       |
| 5. Customer concentration        Top-1 under 20%, top-5 under 65%                  |
+----------------------------------------------------------------------------------+
| KEY LEVER: inventory (4,273.54 Rs Mn) converting to approved, billed parts          |
| FIRST WARNING: current borrowings (2,746.58 vs 1,756.92 Rs Mn in six months)        |
+----------------------------------------------------------------------------------+
```

---

## Load-bearing facts check (what this stage can and cannot say)

1. July falsifier (OCF sign, working capital days vs 344, factoring). H1 FY27 consolidated OCF is (436.24) Rs Mn against (758.90) a year earlier (Q2R [page 11]). The sign is negative. It contains no factoring; the cash flow lines show receivables up 837.45 and inventories up 982.41 Rs Mn. The 344 is CARE's working capital cycle at 31 March 2026 (287 a year earlier), built from inventory 262 days, collection 163 days and creditor 80 days (CARE [page 3]). It is not in the AR. This corrects B03, which found no basis for 344 in the AR: the basis is CARE. It is not comparable to the company's own 244 (AR26 [page 7]) or to B01's 369 on annualised revenue. All three show the same direction, worse. No H1 FY27 figure on CARE's basis exists in the corpus. New risk for the next two prints: factoring and bill discounting are being lined up (CARE [page 3]; Q2C [page 9]) and a customer advance of about USD 4.5 Mn is expected (Q2C [page 7], [page 9]). Any positive OCF from Q4 FY27 must be split from these.
2. Growth guidance. Delivered: FY26 +31.8%; H1 FY27 +28.6% consolidated, Q2 +31.1%. Guidance "over 25% per annum" stands. Required H2 FY27 revenue is 3,901.85 Rs Mn, which is +21.8% on H2 FY26 (3,202.58 = 6,029.75 less 2,827.17, calc), so FY27 guidance needs no acceleration. The capacity claim is harder. An annual run-rate of over Rs 1,300 Cr (13,000 Rs Mn) by end FY28 equals the top of the range 10,833 to 13,000 Rs Mn a year that results from spreading the 65,000 Rs Mn order book evenly over its 5 to 6 year average tenor (calc, AR26 [page 18]). It also needs about 9.3% sequential growth for six quarters from Q2 FY27 (calc). Ramp timing: throughput Q3 FY27, revenue ramp Q4 FY27, all plants by Q2 FY28 (Q2P [page 7]); the AR26 [page 31] says peak utilisation over "a longer horizon". Management says "two, three weeks delay" has already happened (Q2C [page 10]).
3. Customer concentration. Top one 18.64% and top five 47.02% (calc, B03; AR26 [page 242], [page 237]). Both are inside the 20% and 65% tripwires. Top one rose 4.45 points in a year (B03). The H1 FY27 figure is NOT FOUND (no customer note in a quarterly filing).
4. QIP deployment. 4,494.60 of 5,250.00 Rs Mn capex object spent at 30 Sep 2026; 755.40 unspent; general corporate purposes 1,562.10 fully used; issue expenses 160.90 of 187.90 (Q2R [page 6]). H1 use of the capex object = 807.95 Rs Mn (4,494.60 less 3,686.65 at March, B03), which agrees with the CFO's "80.8 crores" (Q2C [page 7]). Plant commissioning: six dedicated plants now commissioned, 44,800 sq m (Q2P [page 9]). CWIP fell from 2,566.82 to 2,124.90 Rs Mn while PPE rose from 7,632.31 to 9,747.98 (consolidated, Q2R [page 10]), consistent with capitalisation.

## Blemishes and open items in this report

- Net debt: management quotes Rs 423.8 Cr net debt (Q2C [page 7]); this stage computes 4,740.69 Rs Mn consolidated on total borrowings less cash and bank balances. The difference of about 502 Rs Mn is not reconciled in the corpus (perimeter or composition).
- The Q1 FY27 deck and the Q4 FY26 and Q1 FY27 concalls were not opened.
- Q2P [page 30] working capital charts did not extract into readable numbers; no figure from them is used.
- Page cites for the AR use the marker that precedes each block; Q2R standalone figures print without decimal points in the extraction ("1,878 03"), restored from the deck (Q2P [page 6]), which agrees.

```yaml
stage: B04-bizmodel
company: "AZAD"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "QIP placement document (2025) not collected (carried from B00 and B03); QIP use read from Q2R [page 6] and AR26 only."
  - "Five screener formula sheets absent; research/ empty (carried from B00). No effect on anchored evidence."
  - "Q1 FY27 presentation and results, Q4 FY26 and Q1 FY27 concalls, peer concalls not opened by this stage; Q2 FY27 deck and concall carry the H1 and Q2 data used."
  - "Definition of company working-capital days (244 vs 202, AR26 [page 7]): NOT FOUND IN DOCUMENT. The 344 tripwire is CARE basis (CARE [page 3]); no H1 FY27 figure on that basis in the corpus."
  - "Names of the two customers at or above 10% of revenue; H1 FY27 customer concentration: NOT FOUND."
  - "Capacity utilisation percentage by plant, segment-level margins, civil vs defence split of Aerospace & Defence, annual parts delivered and revenue per part: NOT FOUND."
  - "Job work (sale of services 1,193.62 Rs Mn) contract terms and who owns the material; reason for +71.7% growth: NOT FOUND."
  - "Cost advantage versus Chinese suppliers, count of qualified suppliers per part: NOT FOUND."
  - "Peer comparison in the prospectus is FY23 (stale); live peer data belongs to the peer-concall stages."
flags:
  - {type: FLAG-BASIS-SETTLED, reason: "Concall Rs 187.8 Cr (Q2) and Rs 358.3 Cr (H1) are STANDALONE revenue from operations (1,878.03 and 3,583.22 Rs Mn, Q2R [page 3]). Rs 190.94 Cr and Rs 363.53 Cr are CONSOLIDATED revenue from operations (1,909.35 and 3,635.34 Rs Mn, Q2R [page 9]). Neither is total income. No source is wrong."}
  - {type: FLAG-CASH, reason: "H1 FY27 consolidated OCF (436.24) Rs Mn (Q2R [page 11]), no factoring in the period. Bill discounting lines usable from Q4 FY27 and a 50 percent OEM advance of about USD 4.5 Mn expected (Q2C [page 9]); CARE says non-recourse factoring is being explored (CARE [page 3]). Any positive OCF from Q4 FY27 must be split from these."}
  - {type: FLAG-WC-344-BASIS, reason: "The July tripwire 344 days is CARE working capital cycle at 31 March 2026 (287 prior year; inventory 262, collection 163, creditor 80 days, CARE [page 3]). Company figure is 244 vs 202 (AR26 [page 7]); stage 1 calc is 369 on annualised H1 revenue. Three bases, same direction (worse). Corrects B03, which found no basis for 344."}
  - {type: FLAG-LEVERAGE-NOT-AT-EBIT, reason: "H1 FY27 incremental EBITDA margin 43.1% but incremental EBIT margin 19.2% (calc, Q2R [page 9], [page 11]); depreciation +88.7%, finance cost +80.4%, other income down 63.1%; PBT (8.9)% on revenue +28.6%. Further depreciation step-up in Q3 and Q4 (Q2C [page 6])."}
  - {type: FLAG-CAPACITY-CLAIM, reason: "Over Rs 1,300 Cr run-rate by end FY28 needs about 9.3 percent sequential growth for six quarters from Q2 FY27 (calc) and equals the top of the 10,833 to 13,000 Rs Mn a year implied by spreading the 65,000 Rs Mn order book over 5 to 6 years (calc). FY27 guidance of over 25 percent needs H2 FY27 revenue of 3,901.85 Rs Mn, only +21.8 percent on H2 FY26 (calc). A 2 to 3 week delay is already admitted (Q2C [page 10])."}
  - {type: FLAG-NET-DEBT-UNRECONCILED, reason: "Consolidated net debt calc 4,740.69 Rs Mn at 30 Sep 2026 (borrowings 5,616.25 less cash and bank 875.56, Q2R [page 10]) vs 2,720.48 at March (B03); management says Rs 423.8 Cr (Q2C [page 7]). Gap of about 502 Rs Mn not reconciled."}
  - {type: FLAG-JOBWORK-MIX, reason: "Sale of services (job work) 1,193.62 Rs Mn, +71.7% vs products +27.0% (AR26 [page 229]); 19.8% of revenue. Material ownership and cash profile NOT FOUND."}
  - {type: FLAG-SEGMENT-GAP, reason: "Energy 79.7% of standalone revenue (AR26 [page 30]) vs Energy plus Oil & Gas 81.5% (AR26 [page 19]) implies Oil & Gas about 106 Rs Mn, while AR26 [page 19], [page 23] say under 100 Rs Mn. About 6 Rs Mn gap, unreconciled."}
  - {type: FLAG-DECK-STALE-TEXT, reason: "Q2P [page 7] chairman text says revenue grew 26.8 percent and shows xx / yy placeholders; 26.8 percent is Q1 FY27 standalone growth (calc). Q2P [page 6] shows 31.6 percent for Q2. Use tables."}
  - {type: FLAG-SECTOR-CAP, reason: "Revenue mix supports Cables / Industrial products 25x (energy about 80 percent, A&D 17.2 percent). Defence / strategic 38x not supported by revenue; civil vs defence split of A&D NOT FOUND; A&D is about 29 percent of order book. Operator rules at /fttcp."}
business_type: "manufacturing"
revenue_streams:
  - {name: "Sale of products, consolidated FY26 (AR26 [page 229])", type: "transactional per-unit under long-term OEM contracts", pct_of_revenue: 78.8, predictability: "high on contracted volume, medium on timing"}
  - {name: "Sale of services, job work, consolidated FY26 (AR26 [page 229])", type: "fee for service", pct_of_revenue: 19.8, predictability: "medium"}
  - {name: "Scrap and export incentives, consolidated FY26 (AR26 [page 229])", type: "incidental", pct_of_revenue: 1.4, predictability: "low"}
  - {name: "End market view, standalone FY26: Energy and Oil & Gas (AR26 [page 19])", type: "contracted OEM supply 3 to 10 years", pct_of_revenue: 81.5, predictability: "high on visibility, medium on timing"}
  - {name: "End market view, standalone FY26: Aerospace & Defence (AR26 [page 21])", type: "contracted OEM supply plus development programme", pct_of_revenue: 17.2, predictability: "medium"}
  - {name: "End market view, standalone FY26: Others (AR26 [page 18])", type: "incidental", pct_of_revenue: 1.35, predictability: "low"}
asset_intensity: "heavy"
wc_intensity: "high"
pricing_power: "moderate"
cyclicality: "secular-growth"
moats_present:
  - "Switching costs from 30 to 48 month OEM qualification, per component: strong, durable per part, weak per customer while wallet share is under 2 percent"
  - "Intangible qualifications: 1,700+ components, 45+ processes, Nadcap, EDF/Arabelle approval: strong, decays if quality slips"
  - "Dedicated customer plants (six, 44,800 sq m): medium until volumes ramp"
  - "Partial cost advantage (gross margin before depreciation 45.2 percent): medium"
valuation_methods:
  primary: {method: "P/E on normalised earnings power", why: "Profitable and earnings explain value; destination PE set by Section 1B; strip other income and use post-depreciation earnings on ramped plants"}
  secondary: {method: "EV/EBITDA cross-check", why: "Removes treasury income and financing swing; read beside EV/EBIT because depreciation is rising fast; use net debt including working capital borrowings"}
  tertiary: {method: "Reverse DCF", why: "Free cash flow is deeply negative (FCF (6,914.46) Rs Mn FY26 calc, B03); use only to test what the ramp must deliver"}
  not_applicable: ["P/B", "EV/Sales", "SOTP (single reportable segment, segment margins NOT FOUND)", "NAV / replacement cost", "DDM"]
irrelevant_ratios:
  - "Spot-year ROCE 10.7 percent (adjusted 15.3): CWIP and unspent QIP capex inflate capital employed before plants earn"
  - "Inventory turnover 0.22: numerator excludes conversion cost (B03 finding 15)"
  - "Current ratio 3.29: held up by slow-to-cash current assets"
  - "Debt to equity 0.29: ignores the swing from net cash to net debt of 4,740.69 Rs Mn (calc, Sep 2026)"
  - "PAT margin and EPS growth: other income 24.4 percent of FY26 PBT and falling as QIP cash is spent"
  - "P/B and dividend yield: value sits in qualifications and growth reinvestment"
must_track_metrics:
  - {metric: "Consolidated operating cash flow after tax, with discounting, factoring and advances split out", healthy: "Positive without those items; H1 FY27 was (436.24) Rs Mn", red_flag: "Still negative in H2 FY27, or positive only after bill discounting or one-time advances"}
  - {metric: "Working capital days on one fixed definition", healthy: "Below 202 (FY25 company basis)", red_flag: "Above 244 (FY26); definition changes"}
  - {metric: "Revenue growth vs over 25 percent guidance and H2 FY27 level", healthy: "Above 25 percent; H2 FY27 above 3,901.85 Rs Mn", red_flag: "Below 25 percent for two quarters or sequential growth under 5 percent"}
  - {metric: "EBIT margin excluding other income (and gross margin before depreciation)", healthy: "Near 26 percent EBIT; gross margin at or above 45 percent", red_flag: "EBIT below 24 percent or gross margin below 43.7 percent"}
  - {metric: "Customer concentration (top-1, top-5)", healthy: "Top-1 under 20 percent, top-5 under 65 percent (18.64 and 47.02 now)", red_flag: "Top-1 at or above 20 percent"}
unit_economics:
  unit: "Rs 100 of consolidated revenue from operations (revenue per part NOT FOUND)"
  revenue_per_unit: "Rs 100: net material 9.6, employees 22.5, other expenses 30.5 (FY26 calc, AR26 [page 192], [page 230], [page 231])"
  margin_per_unit: "FY26 EBITDA ex other income Rs 37.4, EBIT Rs 28.6, PAT Rs 22.2; H1 FY27 EBITDA Rs 37.6, EBIT Rs 26.3, PAT Rs 18.2; incremental EBITDA 43.1 percent but incremental EBIT 19.2 percent (calc)"
  key_lever: "Speed at which 4,273.54 Rs Mn of inventory converts to approved, billed parts across six new plants; it sets cash, depreciation absorption and the Rs 1,300 Cr run-rate claim"
first_deterioration_signals:
  - {risk: "Qualification or delta qualification slips", first_signal: "Inventory and work-in-progress grow faster than revenue (inventory +29.9 percent in H1 FY27 vs revenue +28.6 percent; FY26 +73.9 vs +31.8)"}
  - {risk: "Depreciation outruns revenue", first_signal: "EBIT margin ex other income below 24 percent (26.3 percent in H1 FY27)"}
  - {risk: "Cash conversion does not turn", first_signal: "Operating cash flow after tax negative and current borrowings rising (2,746.58 vs 1,756.92 Rs Mn in six months)"}
  - {risk: "Non-operating items flatter OCF from Q4 FY27", first_signal: "Bill discounting, factoring or customer advances inside operating cash flow"}
  - {risk: "Capacity ramp claim fails", first_signal: "Sequential revenue growth under 5 percent in Q3 or Q4 FY27; H2 FY27 below 3,901.85 Rs Mn"}
  - {risk: "Customer concentration", first_signal: "Top-1 share at or above 20 percent in the AR27 customer note"}
  - {risk: "QIP object and land title", first_signal: "755.40 Rs Mn capex object unspent after 31 March 2027; CWIP not falling"}
mgmt_questions:
  - "Define working capital days of 244 and map it to CARE's 344; give the target path."
  - "How much of H2 FY27 operating cash flow comes from discounting, advances or factoring, and how will it be reported?"
  - "Which delta qualifications clear in Q3 and Q4 by plant, and how much revenue is held behind each?"
  - "Who are the two customers above 10 percent and do they hold termination or price-down clauses?"
  - "Why did job work revenue rise 71.7 percent against products 27.0 percent, and who owns the material?"
  - "What utilisation do the six plants run at, and what does the Rs 1,300 Cr run-rate assume?"
  - "When is the 755.40 Rs Mn QIP capex balance spent and for what orders?"
one_line_verdict: "A real qualification moat with contracted demand and 28.6 percent H1 growth, but operating leverage stops at EBITDA, cash is still negative at (436.24) Rs Mn, and the Rs 1,300 Cr run-rate by FY28 needs about 9 percent sequential growth for six quarters; value on P/E, test the cash."
analyst_note: "Four things a later stage cannot rebuild from the fields. First, the revenue basis: concall 187.8 and 358.3 Cr are standalone revenue from operations; 190.94 and 363.53 Cr are consolidated; neither is total income. Second, the July tripwire 344 days is CARE's cycle (CARE p3), not a company or AR figure, so B03's statement that it has no AR basis is right but incomplete; the company prints 244 vs 202. Third, the factoring risk is forward: CARE says non-recourse factoring is being explored, the Q2 concall says bill discounting lines open from Q4 FY27 and one OEM will advance about USD 4.5 Mn; the H1 OCF of (436.24) contains none of it. Any later positive OCF must be split. Fourth, the 25x Cables / Industrial products row fits the revenue mix (energy about 80 percent); Defence / strategic is not supported because civil and defence aerospace are not split. Net debt of 4,740.69 Rs Mn is this stage's calc; management quotes Rs 423.8 Cr and the gap is open."
```


---
CAVEATS (appended by the orchestrator 2026-11-15 from the stage's own hand-back; the stage has no edit tool):
- Net debt: the stage calculation is 4,740.69 Rs Mn consolidated at 30 Sep 2026; management quotes Rs 423.8 Cr (Q2 FY27 call p.7). The gap of about 502 Rs Mn is unreconciled.
- AR26 p.30 (Energy 79.7%) against p.19 (Energy plus Oil and Gas 81.5%) implies Oil and Gas of about 106 Rs Mn, against "under 100 Rs Mn" on p.19 and p.23. About 6 Rs Mn, unreconciled.
- Q2 FY27 deck p.7 chairman text is stale Q1 text; the tables govern. The deck p.30 working-capital chart did not extract and is not used.
- Not opened by this stage: Q1 FY27 presentation and results, Q4 FY26 and Q1 FY27 concalls, peer concalls. The peer table uses FY23 prospectus data (stale).
- The Q2 FY27 standalone results figures print without decimal points in the text extraction; the stage restored them from the deck, which agrees.
