# Stage 6: Peer concall verification. Jupiter Life Line Hospitals (JLHL)

Run date: 2026-11-12. Model: claude-sonnet-5-5. Protocol v1.1.

Sources: 12 peer transcripts (KIMS x4, MEDANTA x4, YATHARTH x4) in inputs/peer-concalls/, read from the page-marked .txt beside each PDF. Claims are the 10 peer_questions in outputs/blocks/B05-concall.yaml. Citation form: (PEER, Q_ FY__ call, PDF page). Page numbers are the PDF page of the transcript, not the page number printed inside it.

Units. KIMS and YATHARTH speak in Rs Cr in the Q&A. MEDANTA reports in Rs million (10 million = 1 Cr). YATHARTH prepared remarks use Rs million. Every figure carries its source unit. "Derived" means I did the arithmetic from anchored inputs. No screener data sheet was needed.

Quarter map read from each transcript's own pages: KIMS Feb-26 = Q3 FY26 (call 9 Feb 2026), May-26 = Q4 FY26 (18 May 2026), Aug-26 = Q1 FY27 (4 Aug 2026), Nov-26 = Q2 FY27 (5 Nov 2026). MEDANTA Feb = Q3 FY26 (5 Feb 2026), May = Q4 FY26, Aug = Q1 FY27 (31 Jul 2026), Nov = Q2 FY27 (4 Nov 2026). YATHARTH Feb = Q3 FY26 (6 Feb 2026), Jun file = Q4 FY26 (call 26 May 2026), Aug = Q1 FY27 (11 Aug 2026), Nov = Q2 FY27 (4 Nov 2026).

## Input gaps carried

From B00 (carried, none closed by this stage):
- shareholding/ holds one quarter only (30-Sep-2026 NSE XBRL); no promoter pledge trend.
- Screener export sheets empty; only four Data_Sheet CSVs populated. This stage used none of them.
- Results-filing text layers garbled. This stage used no results-filing figure.
- research/ and other/ empty; no broker notes.
- Final Prospectus (11-Sep-2023) not in corpus.
- Announcements are a selection, not the full 12-month record.
- Verifier A shadow claimed by another run; not run here.
Added by this stage:
- No peer reports hospital-wise occupancy, ARPOB or EBITDA on the same basis as JLHL. JLHL's own hospital-wise split is NOT FOUND (B03, B05). So comparisons are cluster or group level.
- No peer gives doctor cost as a percent of revenue. NOT FOUND in all 12 transcripts.
- No peer gives pharmacy share of revenue or margin. NOT FOUND (MEDANTA, YATHARTH decline; KIMS not asked).
- Peer capex per bed splits between land and construction are NOT FOUND, except where stated below.
- Transcript quality: MEDANTA and YATHARTH say their transcripts are "edited for readability" (MEDANTA Nov p.18; YATHARTH Nov p.19). KIMS May p.10 has an internally inconsistent funding line ("equity of 40% ... and 65% is debt"). I do not use that line as a number.
- No peer names Jupiter, Dombivli, Pune or Mira Road in any of the 12 transcripts (searched).

## Part 1: Claim-by-claim verification

### Q1. Greenfield breakeven time, year-1 loss, 40% occupancy reset

| Field | Content |
|---|---|
| Claim | "How many months do peers take to EBITDA breakeven on a new greenfield hospital, and what is the typical loss per month in year 1? Does any peer run a 40% occupancy reset on expansion as Jupiter describes?" (B05 peer_questions 1). JLHL base: Dombivli opened 15-Feb-2026, breakeven by end of year 2. |
| Verdict | VERIFIED on breakeven timing and loss size (three peers). The 40% reset rule itself is PARTIALLY VERIFIED (closest analogues only, no peer describes a "reset"). |
| Peer evidence | MEDANTA Noida (550 beds; started Sep 2025, inaugurated Nov 2025): EBITDA loss Rs 320 million (Rs 32.0 Cr) in Q3 FY26, "peak quarterly loss" (MEDANTA Q4 FY26, p.5); Rs 236 million in Q4 FY26; Rs 49 million in Q1 FY27 (MEDANTA Q1 FY27, p.5); EBITDA positive Rs 86 million on revenue Rs 1,059 million in Q2 FY27 (MEDANTA Q2 FY27, p.5). Chairman: breakeven "within a year of its inauguration" (MEDANTA Q2 FY27, p.3). CEO rule: hospitals "normally" break even at "40% to 45%" occupancy (Pankaj Sahni, MEDANTA Q4 FY26, p.9). Noida occupancy "30% to 40%" in Jul 2026 (MEDANTA Q1 FY27, p.11). YATHARTH Faridabad Sector 20: breakeven in 9 months against a 12-14 month plan (Yatharth Tyagi, YATHARTH Q1 FY27, p.8); Model Town Delhi: guide 15-17 months (YATHARTH Q1 FY27, p.8), losses Rs 55 million in Q1 FY27 and Rs 38 million in Q2 FY27, December named as breakeven month (YATHARTH Q2 FY27, p.13), census-bed occupancy 41% (YATHARTH Q2 FY27, p.7). Earlier YATHARTH rule: breakeven at "30%, 35% of the full operational bed" (Amit Kumar Singh, YATHARTH Q3 FY26, p.18). KIMS: Nashik breakeven in 13 months (KIMS Q3 FY26, p.14); Mahadevapura month-level breakeven in June 2026 after an Oct 2025 opening (KIMS Q1 FY27, p.16 and p.5); Electronic City broke even in September 2026, quarterly breakeven pushed to Q4 FY27 "to give some buffer" (KIMS Q2 FY27, p.9); Thane EBITDA-neutral in Mar and Apr 2026 (KIMS Q4 FY26, p.17). |
| Loss per month and per bed | MEDANTA Noida peak: Rs 32.0 Cr per quarter, about Rs 10.7 Cr a month (derived). On 328 beds at quarter end (MEDANTA Q3 FY26, p.5) that is about Rs 9.8 lakh per bed per quarter (derived). JLHL Dombivli Q1 FY27 drag Rs 9.5 Cr on 200 operating beds is about Rs 4.75 lakh per bed per quarter (derived; B05). KIMS Q4 FY26 quarterly EBITDA losses: Electronic City Rs 25 Cr, Mahadevapura Rs 14 Cr, Thane Rs 5 Cr, Nashik Rs 1 Cr (Abhinay Bollineni, KIMS Q4 FY26, p.7). YATHARTH Q4 FY26 quarter: Model Town Rs 21 Cr, Faridabad Rs 9 Cr (YATHARTH Q4 FY26, p.16). |
| 40% reset analogues | No peer describes a reset to 40%. Two analogues exist. First, the denominator effect: YATHARTH Model Town occupancy fell when census beds rose from 100 to 150, which management called a counting effect (YATHARTH Q1 FY27, p.8). KIMS adds census beds only at 55-60% occupancy (KIMS Q1 FY27, p.18) and wants 70% before adding beds at large new sites (KIMS Q2 FY27, p.14). Second, the MEDANTA 40-45% breakeven rule above. |
| Peers silent | None silent on breakeven. |
| Net read | Peer breakevens at monthly EBITDA level come at 9-13 months and at quarterly level at 12-15 months. JLHL's "end of year 2" (about Feb 2028) is slower than every peer data point, and Dombivli's Q2 FY27 drag of Rs 0.2 Cr (month 7-9) is already faster than MEDANTA Noida. Peers also show the path is not monotonic: KIMS Thane losses were flat for three quarters (Rahul Jeewani question, KIMS Q1 FY27, p.11); KIMS Mahadevapura lost Rs 1.5 Cr (Rs 15 million) in the quarter even though June was breakeven (KIMS Q1 FY27, p.16). So the guidance is normal-to-conservative on timing. The unresolved risk is Q3 FY27 seasonality and monthly versus quarterly definition, not the two-year horizon. |

### Q2. Occupancy basis and ex-new-hospital presentation

| Field | Content |
|---|---|
| Claim | "Is occupancy reported on census/operational beds or total beds, and how do peers present new-hospital dilution (ex-new-hospital occupancy)?" JLHL: 59.5% H1 FY27 (64.8% ex Dombivli) on census beds. |
| Verdict | VERIFIED |
| Peer evidence | KIMS counts census beds and excludes non-census beds such as dialysis machines (KIMS Q2 FY27, p.11); it corrected the presentation to show beds under renovation or not operational (Abhinay, KIMS Q1 FY27, p.8 and KIMS Q2 FY27, p.11). It gives an ex-new-capacity figure: 65% after removing 500 Kondapur beds and 200 Secunderabad beds under renovation, 61% on a second cut (KIMS Q1 FY27, p.15). KIMS Bangalore: 210 operating beds include non-census beds; census occupancy about 40% (Nitish Shetty, KIMS Q1 FY27, p.18). MEDANTA reports occupancy "on expanded bed capacity" and ex-Noida: 63% network, about 66% ex-Noida (MEDANTA Q1 FY27, p.5); census capacity 3,115 versus total 3,811 beds (MEDANTA Q2 FY27, p.5). MEDANTA refuses a Noida occupancy headline because bed additions make it "misleading" (Pankaj Sahni, MEDANTA Q1 FY27, p.11). YATHARTH reports occupancy on census beds: 1,820 census beds versus 2,555 total at 68% (Nitin Gupta, YATHARTH Q1 FY27, p.10); headline 72% "on the currently operationalized beds", with 350-400 beds not yet operational (YATHARTH Q2 FY27, p.4); hospital-wise occupancy given. |
| Peers silent | None. |
| Net read | JLHL's census-bed basis and its ex-Dombivli cut are standard practice. Peers go one step further than JLHL: they name beds not yet operational and give per-hospital figures. JLHL's hospital-wise occupancy is NOT FOUND. MEDANTA also warns that occupancy alone misleads and should be read with ARPP and length of stay (MEDANTA Q2 FY27, p.13). |

### Q3. Mature-hospital ARPOB growth, price versus mix

| Field | Content |
|---|---|
| Claim | "What ARPOB growth do peers report for mature hospitals, and how much is price (insurance renewals) vs case mix? Is it above or at inflation?" JLHL says mature ARPOB grows only with inflation; ARPOB rose 11.7% in Q4 FY26. |
| Verdict | PARTIALLY VERIFIED. Direction (low to mid single digit on mature sites) is corroborated by two peers. The price-versus-mix split runs against JLHL's framing: peers attribute growth to case mix and length of stay, not price. |
| Peer evidence | KIMS: guides ARPOB growth at 4-5% and calls 6-7% inflationary growth "too aggressive" (Abhinay, KIMS Q1 FY27, p.15). KIMS says ARPOB swings with seasonal case mix and ARPP is the better gauge (KIMS Q1 FY27, p.7). KIMS group ARPOB per operating bed +13.7% yoy in Q4 FY26 (KIMS Q4 FY26, p.4), +9.7% in Q1 FY27, +14.9% in Q2 FY27 (KIMS Q2 FY27, p.4); Q2 was +2.3% sequentially. MEDANTA: mature Cluster 1 ARPOB +7% in Q1 FY27 on "favorable specialty mix" (MEDANTA Q1 FY27, p.6); Cluster 1 ARPP +2% in Q2 FY27 (MEDANTA Q2 FY27, p.6); group ARPOB +5% to Rs 70,244 in Q1 FY27 (MEDANTA Q1 FY27, p.5). MEDANTA says tariff rises are rare and "5% or less", and growth is volume led (Pankaj Sahni, MEDANTA Q2 FY27, p.15); Patna went about 4-5 years with zero increases (same page). YATHARTH guides ARPOB +8-10% a year, driven by new premium hospitals and case mix; existing three hospitals to improve "marginally" (YATHARTH Q1 FY27, p.16; Q2 FY27, p.14). YATHARTH CGHS rate revision added "1 -2%" to government revenue (YATHARTH Q1 FY27, p.13). Insurer price pressure: KIMS says it negotiates against insurers "to lower the price" (KIMS Q3 FY26, p.7). |
| Peers silent | None. Nobody gives an insurance-renewal price split. NOT FOUND. |
| Net read | Mature-site ARPOB at peers runs 4-7% and is explained by mix and shorter stays. JLHL's "inflation only" claim fits that range. JLHL's 11.7% in Q4 FY26 sits near the KIMS group figure (13.7%) but above MEDANTA (+6.1% for FY26, MEDANTA Q4 FY26, p.5), so Q4 is not a clean read of price. The price-versus-mix split for JLHL stays unproven. |

### Q4. NABH, cashless empanelment time and payer mix at 6 and 12 months

| Field | Content |
|---|---|
| Claim | "How long does NABH plus cashless insurer empanelment take for a new hospital, and what is the payer mix at 6 and 12 months?" JLHL: Dombivli empanelment in about one year; NABH applied. |
| Verdict | VERIFIED on timing (three peers, with a long tail at KIMS). Payer mix at 6 and 12 months is PARTIALLY VERIFIED. |
| Peer evidence | KIMS: NABH "is not a prerequisite for empanelment with insurance company" (Abhinay, KIMS Q3 FY26, p.7). Thane and Nashik had 2 of the top 5 insurers at about 6-12 months (same page). KIMS "underestimated the time it takes" (KIMS Q4 FY26, p.9), and wants 6-9 months as a target (same page). At 15 months Thane still lacks "two, three major companies"; Mahadevapura lacks GIPSA and Star (KIMS Q2 FY27, p.9). Nashik got GIPSA only in Nov 2026, about 22-23 months after opening (derived from a Jan 2026 breakeven at month 13; KIMS Q3 FY26, p.14; KIMS Q2 FY27, p.10). KIMS Aug 2026: 50% of insurers empanelled across four new assets (KIMS Q1 FY27, p.9). Cause named: a common empanelment initiative by general insurers that created delay (KIMS Q4 FY26, p.9; KIMS Q1 FY27, p.21). MEDANTA Noida: 4-5 major insurance contracts signed by about month 4 (MEDANTA Q3 FY26, p.7); "major empanelments" concluded by Q1 FY27 (about month 9-10, MEDANTA Q1 FY27, p.5); CGHS only in May 2026 (MEDANTA Q4 FY26, p.5); almost all done by the May call (MEDANTA Q4 FY26, p.18). YATHARTH Faridabad Sector 20 expected "full-fledged with all empanelment" about 5 months after opening (YATHARTH Q3 FY26, p.8); Model Town and Faridabad have "a majority of the government empanels" yet keep government share low (YATHARTH Q1 FY27, p.7). Payer mix: YATHARTH new hospitals more than 80-90% cash plus private insurance, government 10-20% (YATHARTH Q1 FY27, p.3 and p.13; Q2 FY27, p.15); MEDANTA Cluster 2 insurance 26-27%, Patna 19-20% under a PPP project at CGHS rates (MEDANTA Q2 FY27, p.11); KIMS Thane/Nashik-type markets: insurance about 30%, public sector about 30%, cash 25-30% (KIMS Q3 FY26, p.14, the Nashik discussion). |
| Peers silent | No peer gives a payer mix at exactly month 6 or month 12. NOT FOUND. |
| Net read | One year to cashless empanelment is inside the peer range of 5-23 months. The tail matters: KIMS shows 15 and 22 month cases in Maharashtra, close to Dombivli. KIMS also says NABH is not the gate; insurer pricing talks are. JLHL's confirm signal "NABH award" may therefore not be the event that unlocks cashless volume. Cash-pay markets absorb the delay at KIMS Thane and Bangalore (KIMS Q3 FY26, p.14); price-sensitive Tier-2 markets do not. Dombivli's cash share is NOT FOUND. |

### Q5. Doctor cost, attrition, full-time contracts

| Field | Content |
|---|---|
| Claim | "Doctor cost as % of revenue and attrition in regions where a peer opened a new hospital; any shift to exclusive full-time contracts?" JLHL claims 20-25% doctor cost and near-zero attrition. |
| Verdict | PARTIALLY VERIFIED. Attrition corroborated by three peers. Doctor cost as % of revenue is UNVERIFIABLE (no peer gives it). |
| Peer evidence | MEDANTA: "very negligible to no attrition at any of our senior clinical levels"; nursing and junior doctor attrition high (Pankaj Sahni, MEDANTA Q1 FY27, p.13); no senior clinician lost to hospitals opening near Gurugram (MEDANTA Q4 FY26, p.16). YATHARTH: doctor attrition about 7% overall, senior doctors "not even 3% to 4%" (Nitin Gupta, YATHARTH Q1 FY27, p.15); doctor cost rose 2% quarter on quarter, shown inside other expenses as "specialist charges" (YATHARTH Q1 FY27, p.20; the unit, points of revenue or percent growth, is not stated). KIMS: lost "one or two doctors" in Hyderabad, "nothing material" (KIMS Q4 FY26, p.12); doctor pay model unchanged across states (KIMS Q4 FY26, p.16); doctors "never completed fully", added continuously, which slows margin ramp (KIMS Q2 FY27, p.12). Full-time contracts: KIMS says full-time practice is easier to align in the South; in Maharashtra doctors "first join us as a part-time model" and move to full time over time; Nagpur took 18-24 months to stabilise (Abhinay, KIMS Q1 FY27, p.13-14). YATHARTH pitches freedom from "P&L pressures" and has begun ESOPs (YATHARTH Q1 FY27, p.16). MEDANTA flags a "war for talent" and aggressive hiring (MEDANTA Q3 FY26, p.10). |
| Peers silent | Doctor cost as % of revenue: all three. |
| Net read | Low senior attrition is a sector pattern, so JLHL's claim is plausible. The sharper finding is KIMS on Maharashtra: part-time-first doctors slow new-hospital ramps in Thane and Nashik. JLHL sits in the same labour market. Its 20-25% doctor cost cannot be benchmarked from this corpus. |

### Q6. Leverage ceiling and funding mix in a capex cycle

| Field | Content |
|---|---|
| Claim | "Leverage ceiling and funding mix peers use during a capex cycle (debt/EBITDA, internal accruals share)." JLHL: 3x EBITDA board ceiling versus ICRA 1.8x trigger (B03) and a Rs 500 Cr term loan. |
| Verdict | PARTIALLY VERIFIED. Funding mix (accruals plus debt) is corroborated. The ceiling level is not: no peer states 3x, and two state lower. |
| Peer evidence | KIMS: investors see "1 is to 2" net debt to EBITDA as healthy; the chairman says debt/EBITDA should not cross "1 is to 2" (KIMS Q4 FY26, p.18-19; the transcript wording on the current level is garbled). Debt peaked at Rs 3,000+ Cr, then a Rs 1,500 Cr QIP retired Rs 1,125 Cr of it (KIMS Q1 FY27, p.4 and p.12). Net debt Rs 2,150 Cr, ratio "about 1.9" at Sep 2026 (Sachin Salvi, KIMS Q2 FY27, p.18). KIMS had said in Feb 2026 that debt "peaked out" (KIMS Q3 FY26, p.17), then announced the QIP within a month (KIMS Q4 FY26, p.8). KIMS FY26 PAT Rs 242 Cr versus Rs 415 Cr, and the chairman links the raise to ROE and ROC falling (KIMS Q4 FY26, p.4 and p.19). YATHARTH: comfortable to "2x of the trailing last 12 months EBITDA" (Yatharth Tyagi, YATHARTH Q1 FY27, p.18); debt Rs 210 Cr to about Rs 300 Cr, partly acquisition-funded, rest from accruals (same page); net debt Rs 39.2 Cr (Rs 392 million) at Sep 2026 (YATHARTH Q2 FY27, p.6); "peak level of debt" (YATHARTH Q2 FY27, p.11-12). Advent Rs 3,150 Cr primary capital, first tranche Rs 1,750 Cr (YATHARTH Q2 FY27, p.8). MEDANTA: net cash Rs 5,906 million (Rs 590.6 Cr) at Mar 2026, Rs 7,815 million (Rs 781.5 Cr) at Sep 2026; capex "fully supported by a combination of internal accruals and project-specific debt" (MEDANTA Q4 FY26, p.7; MEDANTA Q2 FY27, p.5). |
| Peers silent | MEDANTA states no numeric ceiling. |
| Net read | Peers fund growth from accruals plus debt, as JLHL says. But the stated comfort bands are 1-2x (KIMS, YATHARTH). JLHL's 3x ceiling sits above both, and KIMS shows what happens near the top of the band: PAT fell 41% in FY26 (derived from Rs 242 Cr and Rs 415 Cr) and management turned to equity. Two peers fund the gap with new equity (KIMS QIP, YATHARTH Advent) or sit net cash (MEDANTA). JLHL funds with debt. This is the peer-set item that most complicates JLHL's funding story. |

### Q7. Capex per bed, with and without land

| Field | Content |
|---|---|
| Claim | "Capex per bed with and without land for new hospitals, and recent escalation." JLHL: about Rs 1.5 Cr per bed including land across 1,700 beds; Pune Rs 1.2 Cr and Mira Road Rs 1.3 Cr ex land. |
| Verdict | VERIFIED on range and escalation direction. The land versus no-land split is NOT FOUND at every peer. |
| Peer evidence | MEDANTA plan averages (derived, bed count from the same call): May 2026 Rs 45,000 million (Rs 4,500 Cr) for about 500 brownfield plus 2,700 greenfield beds = about Rs 1.41 Cr per bed (MEDANTA Q4 FY26, p.7); Jul 2026 Rs 4,850 Cr future capex (Yogesh Gupta, MEDANTA Q1 FY27, p.9) for about 3,350 beds (same call, p.7) = about Rs 1.45 Cr; Nov 2026 "over Rs 6,000 Cr" for about 3,450 beds = at least Rs 1.74 Cr (MEDANTA Q2 FY27, p.7). Guwahati: 650 beds at about Rs 9,700 million (Rs 970 Cr) = about Rs 1.49 Cr per bed (MEDANTA Q1 FY27, p.7); analyst puts the earlier plan at Rs 500 Cr for 400 beds (Rs 1.25 Cr) and the extra 250 beds at about Rs 500 Cr, and management explains larger floor plates, double the operating rooms, no new land (MEDANTA Q1 FY27, p.15-16). Ghaziabad: 500 beds, capex about Rs 1,000 Cr, plus land bought at Rs 166 Cr (MEDANTA Q2 FY27, p.6); about Rs 2.0 Cr per bed on the Rs 1,000 Cr figure (derived; whether land is inside it is not stated). YATHARTH: about Rs 60 lakh per bed overall, Rs 80-90 lakh at newer Delhi and Faridabad hospitals (YATHARTH Q3 FY26, p.6); Rs 75 lakh for Noida brownfield on owned land, no escalation expected (YATHARTH Q4 FY26, p.16); capex per bed went from Rs 30.7 lakh to Rs 61.4 lakh over three years (analyst figure, accepted); next 1,800 beds Rs 75-80 lakh; Gurugram "almost a Rs 1 crore capex bed" (Yatharth Tyagi, YATHARTH Q1 FY27, p.18). KIMS: Kakinada, Rs 80 Cr for 51% of 183 beds (p.4) or 150 beds (p.16) with no debt = about Rs 0.86-1.05 Cr per bed on an implied 100% equity value (derived; KIMS Q2 FY27, p.4 and p.16). O&M call options priced at 10-12x trailing EBITDA (KIMS Q2 FY27, p.13). |
| Peers silent | KIMS gives no per-bed build cost for its greenfields (NOT FOUND). |
| Net read | JLHL's Rs 1.2-1.5 Cr per bed sits inside the peer range of Rs 1.4-2.0 Cr (MEDANTA, premium, multi-OT) and Rs 0.75-1.0 Cr (YATHARTH, NCR owned land). Both peers show escalation. MEDANTA's plan average rose from Rs 1.41 Cr to at least Rs 1.74 Cr in two quarters. JLHL's kill signal for Pune South (above Rs 1.2 Cr) is therefore live: scope growth can move cost per bed without a land change. |

### Q8. Seasonality: Q1/Q3 weak, Q2/Q4 strong, medical-heavy Q2 ARPOB

| Field | Content |
|---|---|
| Claim | "Do peers see Q1 and Q3 weaker and Q2 and Q4 stronger, and do medical-heavy Q2 admissions lower ARPOB?" JLHL: Dombivli Q2 near-breakeven is partly seasonal; Q3 FY27 is the test. |
| Verdict | PARTIALLY VERIFIED. Weak Q1 and Q3 corroborated by two peers. "Q2 medical admissions lower ARPOB" is not corroborated; KIMS shows the opposite in Q2 FY27. |
| Peer evidence | KIMS: "Q3 is traditionally a weak quarter" (KIMS Q3 FY26, p.3); Maharashtra Q1 "usually a weak quarter" (Abhinay, KIMS Q1 FY27, p.11); AP Q2 expected "quite better than Q1" (KIMS Q1 FY27, p.17); Q2 FY27 EBITDA margin 20.5% versus 20.1% in Q1 (KIMS Q2 FY27, p.3). MEDANTA: "quarter 3 normally is a softer quarter due to festival season" (Yogesh Gupta, MEDANTA Q2 FY27, p.10); dengue and respiratory seasons lengthen stays and shift mix, so read length of stay over nine months or a year (MEDANTA Q3 FY26, p.9; MEDANTA Q1 FY27, p.10). YATHARTH: Q4 better than Q3 (management, YATHARTH Q3 FY26, p.4); H1 collections run below full year (YATHARTH Q2 FY27, p.9); Q2 FY27 was its "strongest quarter to date" (YATHARTH Q2 FY27, p.3). On ARPOB: KIMS Q2 FY27 ARPOB per operating bed rose 2.3% sequentially (KIMS Q2 FY27, p.4); MEDANTA Q2 FY27 ARPP Rs 2.06 lakh versus Rs 201,891 in Q1 (MEDANTA Q2 FY27, p.5; Q1 FY27, p.6) while length of stay fell to 2.89 days. KIMS says ARPOB shifts on "seasonal case mix" but names no direction (KIMS Q1 FY27, p.7). |
| Peers silent | No peer states Q2 medical mix lowers ARPOB. YATHARTH and MEDANTA do not discuss Q2 as a strong quarter by name. |
| Net read | Q1 and Q3 softness is a sector pattern, so Q3 FY27 is a fair test for Dombivli. The ARPOB-in-Q2 mechanism is not seen at peers. The seasonal help to Dombivli's Q2 drag stays unsized; peers do not size it either. |

### Q9. Onco-drug margin cap and pharmacy exposure

| Field | Content |
|---|---|
| Claim | "Exposure to the 30% onco-drug margin cap (from 1 Nov 2026) and Supreme Court review of medicine markups; pharmacy share of revenue and margin." JLHL has not modelled it; pharmacy is reported gross (B03). |
| Verdict | PARTIALLY VERIFIED. One peer quantifies a small hit; the other two give direction only. |
| Peer evidence | YATHARTH: EBITDA effect "around 0.3%" on the capped list; guidance of close to 24% unchanged; offset by other efficiencies (Yatharth Tyagi, YATHARTH Q2 FY27, p.7-8). The wording does not say whether 0.3% is points of margin or percent of EBITDA. Oncology is "close to 10%" of YATHARTH revenue with one LINAC (YATHARTH Q1 FY27, p.5). On the Supreme Court and other-drug markups: "very premature", matter before the court (Amit Kumar Singh, YATHARTH Q2 FY27, p.7 and p.17). KIMS: "oncology is not a big part of our revenue stream, the impact may not be significant"; final detail due 9 Nov (Abhinay, KIMS Q2 FY27, p.6). KIMS also launched two large onco programmes in AP that cost about Rs 2 Cr a month each at the centre until volumes build (KIMS Q2 FY27, p.12-13). MEDANTA: "too early to evaluate", does not track pharmacy or drug share, disputes that oncology is the highest margin line, and says its cancer work is spread across other institutes (Pankaj Sahni, MEDANTA Q2 FY27, p.11-12 and p.16-17). MEDANTA retail pharmacy outside hospitals is a separate line, Rs 699 million in Q2 FY27, +53% (MEDANTA Q2 FY27, p.5). YATHARTH does not track pharmacy as a separate business because procedures run on packages (YATHARTH Q2 FY27, p.7). |
| Peers silent | Pharmacy share of revenue and margin: all three (NOT FOUND). |
| Net read | For mixed-specialty chains the onco cap looks small. YATHARTH's 0.3 is the only number, and it depends on an onco share near 10%. JLHL's onco share is NOT FOUND, so the peer number cannot be carried across. Management said it will give the impact on the Q3 FY27 call (B05). The Supreme Court markup issue is open at every peer. |

### Q10. Bed supply in Thane, Pune and Indore-type markets

| Field | Content |
|---|---|
| Claim | "Is high-quality bed supply short in Thane, Pune and Indore-type markets, and which peers are adding beds there?" JLHL says supply is insufficient. |
| Verdict | PARTIALLY VERIFIED for demand. Peers are also adding supply in two of the three markets, which complicates "insufficient". Pune is UNVERIFIABLE. |
| Peer evidence | MEDANTA: "our real challenge will be, can we deliver the supply and ... high quality, ethical supply to meet that demand" (Pankaj Sahni, MEDANTA Q1 FY27, p.13); sees a shortage of high-quality ICU and medical care in its Tier-2 regions (MEDANTA Q2 FY27, p.13). Those regions are UP, Bihar and Northeast, not JLHL's. MEDANTA is adding in Indore: an 80-bed acquired facility "towards the end of Q2, maybe early Q3" plus cancer services in Indore and Ranchi (MEDANTA Q1 FY27, p.8 and p.17). Cluster 1 (Gurugram, Indore, Ranchi) occupancy 66% in Q2 FY27 (MEDANTA Q2 FY27, p.6); Indore alone is NOT FOUND. MEDANTA Mumbai greenfield: land acquired, extra FSI approved (MEDANTA Q3 FY26, p.6), approvals mostly in hand, piling to start (MEDANTA Q2 FY27, p.10). KIMS Thane (opened about Aug 2025, 15 months old on 5 Nov 2026, KIMS Q2 FY27, p.14): July 2026 revenue Rs 21 Cr and 10% EBITDA margin (KIMS Q1 FY27, p.11); about 75 beds not operational (KIMS Q2 FY27, p.7). KIMS Maharashtra occupancy 60.5% in Q4 FY26 (KIMS Q4 FY26, p.11). KIMS calls Hyderabad the most competitive market, with 4-5 new hospitals in a year (KIMS Q4 FY26, p.12). Large-format KIMS sites expect to reach 70% occupancy only in "four to six years" (KIMS Q2 FY27, p.14). |
| Peers silent | Pune: no peer. Thane: KIMS only. Indore: MEDANTA only. |
| Net read | Demand is strong in both KIMS Thane and MEDANTA's network. But KIMS Thane took long to fill (insurance, part-time doctors), which says supply of beds is not the limit. The limit is empanelment and doctors. MEDANTA and KIMS are adding competing supply in Indore and Thane. JLHL's "insufficient supply" claim is supported by demand strength, not by a bed shortage, and the peer Indore and Thane additions are a competitive signal. |

## Part 2: Unprompted cross-read

### 2A Demand environment

Consensus: strong volume growth. Inpatient volume +27% yoy at KIMS in Q2 FY27 (KIMS Q2 FY27, p.4); +30% at MEDANTA (MEDANTA Q2 FY27, p.5); +28% at YATHARTH existing hospitals (YATHARTH Q2 FY27, p.5). MEDANTA names a "flight to quality" and rising awareness in north and central India (MEDANTA Q1 FY27, p.13). No peer reports soft demand. Silence on softness is itself informative: it matches JLHL's framing. The split is on price: MEDANTA drives growth by volume and holds tariffs near flat; KIMS and YATHARTH lean on mix and ARPOB. Occupancy levels: MEDANTA 67%, YATHARTH 72-78%, KIMS Telangana low 50s on a bed base that includes idle beds (KIMS Q2 FY27, p.11). JLHL's 59.5% H1 is inside this band.

### 2B Pricing and input costs

- Tariff: MEDANTA tariff increases "5% or less" (MEDANTA Q2 FY27, p.15); KIMS ARPOB 4-5% guide (KIMS Q1 FY27, p.15).
- Insurer pricing: KIMS and MEDANTA say insurers push prices down in empanelment (KIMS Q3 FY26, p.7; MEDANTA Q3 FY26, p.7 on delaying panels to keep ARPOB).
- Talent cost: MEDANTA "war for talent" (MEDANTA Q3 FY26, p.10); YATHARTH doctor cost +2% sequential (YATHARTH Q1 FY27, p.20); KIMS onco programmes drag margin by about Rs 2 Cr a month per centre (KIMS Q2 FY27, p.12-13).
- Material: MEDANTA says material cost optimisation is under way and targets "a couple of hundred basis points" of efficiency (MEDANTA Q3 FY26, p.10).
- Receivables: KIMS booked Rs 7.8 Cr of provision for doubtful government debt in Q2 FY27 though it expects reversal (KIMS Q2 FY27, p.7-8); YATHARTH expects EBITDA to cash conversion above 70% by year end and says H1 is lower seasonally (YATHARTH Q2 FY27, p.9). This is a peer comparator for the JLHL conversion flag (H1 FY27 73% derived, about 70% guided, B05). JLHL's number matches the peer pattern. JLHL's receivable rise (Rs 75.5 Cr to Rs 118.3 Cr, B05) is not explained by the peer seasonality line.
Margin read: JLHL's narrative that mature margin holds while new units drag matches all three. KIMS mature units 29.5% margin (KIMS Q4 FY26, p.17), YATHARTH ex-ramp 28%, MEDANTA ex-Noida about 26% (MEDANTA Q1 FY27, p.9). MEDANTA also changed its EBITDA definition to "operating EBITDA" after ESOP and ex-other income (MEDANTA Q2 FY27, p.4-5), which blocks a clean quarter-on-quarter margin read.

### 2C Capex cycle

This is a capacity race among listed chains, not a lone expander in a cautious set. MEDANTA plans about 3,450 beds and over Rs 6,000 Cr over 4-5 years (MEDANTA Q2 FY27, p.7). YATHARTH targets 5,000 beds, plus 2,000-3,000 more with Advent money (YATHARTH Q2 FY27, p.8). KIMS adds Rajahmundry, Ongole, Secunderabad, Kondapur and acquisitions, then slows to 400-500 beds in 24 months to stabilise (KIMS Q2 FY27, p.18). JLHL is one of four expanders. The difference is funding. KIMS (QIP, promoter preferential issue), YATHARTH (Advent) and MEDANTA (net cash) have equity or cash. JLHL carries a Rs 500 Cr term loan. Construction risk is shared: pollution-linked construction halts in Delhi NCR (MEDANTA Q2 FY27, p.10; YATHARTH Q2 FY27, p.13) and monsoon delays (YATHARTH Q1 FY27, p.19).

### 2D Competitive mentions

No peer mentions Jupiter by name or by an unmistakable description. I searched all 12 transcripts for "Jupiter", "Dombivli", "Pune" and "Mira Road": no hit. Location overlaps without a name: KIMS Thane (KIMS Q2 FY27, p.14), MEDANTA Indore (MEDANTA Q1 FY27, p.8) and MEDANTA Mumbai greenfield (MEDANTA Q2 FY27, p.10). These are competitive signals only.

### 2E Risks peers discuss that JLHL does not (from B05)

- Common insurer empanelment initiative delaying new-hospital panels (KIMS Q4 FY26, p.9; KIMS Q1 FY27, p.21).
- Room-rent ceiling recommendation (a "3-star hotel" level) from a panel (YATHARTH Q1 FY27, p.11-12).
- Kerala bill on private hospital charges (KIMS Q2 FY27, p.19).
- Pollution and monsoon construction halts (MEDANTA Q2 FY27, p.10; YATHARTH Q1 FY27, p.19).
- Government receivable delays and doubtful debt provisions (KIMS Q2 FY27, p.7-8).
- Income tax demand notice and appeal (YATHARTH Q2 FY27, p.12-13).
- Gulf conflict affecting international patients (YATHARTH Q2 FY27, p.11).
- Part-time doctor practice in Maharashtra slowing ramp (KIMS Q1 FY27, p.13-14).
- Lease cost and GST on rented hospitals (KIMS Q2 FY27, p.15 and p.17-18).
- Returns dilution during a capex cycle: KIMS FY26 PAT -41%, ROE and ROC down (KIMS Q4 FY26, p.19).
- Minority leakage, 10-15% of PAT at KIMS (KIMS Q2 FY27, p.14).

### 2F Load-bearing fact tests (not a handoff question)

1. Dombivli ramp and breakeven by end of year 2: supported. All three peers break even in 9-15 months. Q2 FY27 is a seasonal best case (see Q8).
2. Profit squeeze below EBITDA in a capex cycle: confirmed at all three. KIMS FY26 PAT Rs 242 Cr versus Rs 415 Cr (KIMS Q4 FY26, p.4), Q1 FY27 PAT Rs 37 Cr versus Rs 85 Cr a year earlier (KIMS Q1 FY27, p.3). MEDANTA Q1 FY27 PAT Rs 1,573 million versus Rs 1,590 million with "higher depreciation and finance costs" (MEDANTA Q1 FY27, p.4). YATHARTH Q2 FY27 PAT +17% against EBITDA +50% (YATHARTH Q2 FY27, p.6) and a depreciation run of about Rs 29 Cr a quarter (YATHARTH Q1 FY27, p.19). JLHL's H1 PAT -7.4% is consistent with this pattern.
3. Capex funding, debt ceiling, cost per bed: see Q6 and Q7. Peers use lower ceilings and fund with equity.
4. Occupancy and ARPOB definitions: see Q2 and Q3.

## Part 3: Peer coverage map

| Peer | Quarter | Used how | Key contribution |
|---|---|---|---|
| KIMS | Q3 FY26 (call 9 Feb 2026) | SUBSTANTIVE | NABH not a prerequisite for empanelment (p.7); Nashik breakeven month 13 (p.14); "debt has peaked" (p.17) |
| KIMS | Q4 FY26 (18 May 2026) | SUBSTANTIVE | Empanelment delay, GIC initiative (p.9); QIP and debt cut (p.8, p.10); doctor retention (p.12); mature margin 29.5% and new-unit loss Rs 128 Cr (p.17) |
| KIMS | Q1 FY27 (4 Aug 2026) | SUBSTANTIVE | ARPOB 4-5% guide (p.15); census and ex-new occupancy (p.15, p.18); Maharashtra part-time doctors (p.13-14); Q1 weak (p.11) |
| KIMS | Q2 FY27 (5 Nov 2026) | SUBSTANTIVE | Onco cap view (p.6); Electronic City breakeven (p.9); net debt Rs 2,150 Cr and 1.9x (p.18); 70% occupancy in 4-6 years (p.14) |
| MEDANTA | Q3 FY26 (5 Feb 2026) | SUBSTANTIVE | Noida peak loss Rs 320 million (p.4, p.8); single-tower build-out (p.11); seasonality of stays (p.9) |
| MEDANTA | Q4 FY26 (May 2026) | SUBSTANTIVE | 40-45% occupancy breakeven rule (p.9); capex Rs 4,500 Cr plan and funding mix (p.7); net cash (p.7); attrition (p.16) |
| MEDANTA | Q1 FY27 (31 Jul 2026) | SUBSTANTIVE | Noida loss Rs 49 million (p.5); Guwahati capex rise (p.15-16); attrition (p.13); Indore beds (p.8); occupancy ex-Noida (p.5) |
| MEDANTA | Q2 FY27 (4 Nov 2026) | SUBSTANTIVE | Noida breakeven Rs 86 million (p.5); capex Rs 6,000 Cr (p.7); Ghaziabad Rs 1,000 Cr (p.6); tariff restraint (p.15); onco cap view (p.11-12) |
| YATHARTH | Q3 FY26 (6 Feb 2026) | SUBSTANTIVE | Capex per bed Rs 60 lakh and Rs 80-90 lakh (p.6); breakeven at 30-35% of full beds (p.18) |
| YATHARTH | Q4 FY26 (26 May 2026) | SUBSTANTIVE | Debt Rs 230 Cr, net cash (p.7-8); Noida brownfield Rs 75 lakh per bed (p.16); breakeven timelines (p.11) |
| YATHARTH | Q1 FY27 (11 Aug 2026) | SUBSTANTIVE | Faridabad 9-month breakeven (p.8); 2x EBITDA debt comfort (p.18); attrition 7% (p.15); census beds (p.10); capex per bed to Rs 75-80 lakh (p.18) |
| YATHARTH | Q2 FY27 (4 Nov 2026) | SUBSTANTIVE | Onco cap 0.3% (p.7-8); Advent Rs 3,150 Cr (p.3, p.8); Model Town breakeven December (p.13); OCF conversion seasonality (p.9) |

All 12 are SUBSTANTIVE: each carries at least one citation used in Part 1 or Part 2.

## Part 4: Triangulation summary

- Claims verified: 4 of 10 (Q1, Q2, Q4, Q7). Each carries a stated sub-part that stays unproven.
- Claims partially verified: 6 of 10 (Q3, Q5, Q6, Q8, Q9, Q10).
- Claims contradicted: 0. No peer states the opposite of a JLHL claim in the list. Q6 comes closest: the leverage ceiling is higher than every peer's stated band.
- Claims unverifiable: 0 as a whole question. Sub-parts unverifiable: doctor cost as percent of revenue, pharmacy share, Pune bed supply, payer mix at months 6 and 12, land versus no-land capex.
- Most consequential complication (not a contradiction): JLHL funds its capex cycle with debt under a 3x ceiling. KIMS and YATHARTH state 1-2x as comfortable. KIMS reached a debt peak, saw PAT fall 41% and raised equity. This feeds the funding and position-size discussion.
- Strongest independent confirmation: breakeven timing. MEDANTA Noida, YATHARTH Faridabad Sector 20 and Model Town, and KIMS Mahadevapura, Thane and Electronic City break even at 9-15 months. JLHL's end-of-year-2 guidance sits behind them.
- Overall: the peer set supports JLHL's operating claims (ramp speed, census-bed occupancy, low senior attrition, seasonality, capex per bed range). It complicates the funding claim (higher ceiling, no equity cushion) and the "insufficient supply" claim (peers add beds in Indore and Thane). It leaves doctor cost, onco exposure and Pune untested. Symmetric note: JLHL's early Dombivli result beats peers on pace, and the same peers show that early pace can stall in the next quarter.

## Part 5: Cross-peer hypothesis

cross_peer_hypothesis: PAT growth runs 20-30 points below EBITDA growth through the capex cycle, even in the quarter a large new unit reaches EBITDA breakeven. The three peers show this in Q2 FY27, the quarter each had a unit at or near breakeven. MEDANTA operating EBITDA +60% yoy versus PAT +38% (MEDANTA Q2 FY27, p.5). YATHARTH EBITDA +50% versus PAT +17% (YATHARTH Q2 FY27, p.6). KIMS total EBITDA +34% versus PAT Rs 76 Cr against Rs 72 Cr, about +6% (derived; KIMS Q2 FY27, p.3). No peer names this lag. Each explains its own PAT through its own cause (labour code, depreciation, interest, a call-option gain). The pattern is common and large. It implies EBITDA breakeven of the last big unit is not the date PAT growth recovers. Depreciation and interest start at commissioning and keep running. KIMS Q2 PAT also includes a Rs 13.2 Cr call-option fair-value gain booked below EBITDA (KIMS Q2 FY27, p.14), so its gap is, if anything, understated.

Test for JLHL. H1 FY27 PAT is -7.4% (B05). If the pattern holds, JLHL's Q3 and Q4 FY27 PAT growth will stay at least 15 points below EBITDA growth even if Dombivli reaches zero EBITDA. A PAT-versus-EBITDA gap below 10 points by Q4 FY27 would reject the hypothesis. The result bears on the entry price: EPS, not EBITDA, drives the Section 1B earnings basis.

## Analyst note

Q1 and Q4 are the two cleanest tests. Both support JLHL's timing, and the real exposure is the quarter after a seasonal best case. Watch the KIMS Thane path as the Maharashtra analogue: monthly EBITDA-neutral in Mar-Apr 2026, flat losses through Q1 FY27, quarterly breakeven only by Q2 FY27 (analyst statement, KIMS Q2 FY27, p.9). KIMS NABH comment may change the Dombivli confirm signal in B05. Management's debt line moved at KIMS too (Feb "peaked", May QIP). That matches the JLHL funding drift flag.


## ERRATUM (stage 6 hand-back, recorded by the orchestrator, 2026-11-12)
Section 2B attributes "insurers push prices down in empanelment" to KIMS and MEDANTA. Stage 6 reported in its hand-back that the MEDANTA half is void: MEDANTA Q3 FY26 p.7 says only that Noida ARPOB is high now and will balance as panels are added. The claim rests on KIMS alone (Q3 FY26 p.7). The stage could not edit the line itself.

```yaml
stage: B06-peers
company: "JLHL"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "B00: shareholding/ one quarter only (30-Sep-2026 NSE XBRL); no promoter pledge trend."
  - "B00: screener export sheets empty; only four Data_Sheet CSVs populated; none used in this stage."
  - "B00: results text layers garbled; no results-filing figure used."
  - "B00: research and other folders empty; no broker notes."
  - "B00: final Prospectus 11-Sep-2023 not in corpus; announcements are a selection."
  - "No peer reports hospital-wise metrics on JLHL's basis; JLHL hospital-wise occupancy/ARPOB/EBITDA NOT FOUND (B03, B05)."
  - "Doctor cost as percent of revenue NOT FOUND in all 12 peer transcripts."
  - "Pharmacy share of revenue and margin NOT FOUND in all 12 peer transcripts."
  - "Peer capex per bed split between land and construction NOT FOUND."
  - "No peer names Jupiter, Dombivli, Pune or Mira Road in any transcript."
  - "KIMS Q4 FY26 p.10 funding line (equity 40% and debt 65%) is internally inconsistent; not used."
flags:
  - {type: FLAG-LEVERAGE-CEILING-ABOVE-PEERS, reason: "JLHL 3x EBITDA ceiling sits above peer comfort bands: KIMS 1-2x (Q4 FY26 p.18-19), YATHARTH about 2x (Q1 FY27 p.18). KIMS debt peaked, PAT fell 41% in FY26, equity raised."}
  - {type: FLAG-PAT-LAG-PATTERN, reason: "All three peers show PAT growth 20-30 points below EBITDA growth in Q2 FY27 (MEDANTA 60 vs 38, YATHARTH 50 vs 17, KIMS 34 vs about 6). Applies to JLHL H1 PAT -7.4%."}
  - {type: FLAG-NABH-NOT-GATE, reason: "KIMS says NABH is not a prerequisite for insurer empanelment (Q3 FY26 p.7); B05 confirm signal for Dombivli names NABH award."}
  - {type: FLAG-MAHARASHTRA-DOCTOR-MODEL, reason: "KIMS: Maharashtra doctors join part-time first; Nagpur took 18-24 months to stabilise (Q1 FY27 p.13-14). Relevant to Dombivli ramp."}
  - {type: FLAG-PEER-SUPPLY-IN-JLHL-MARKETS, reason: "MEDANTA adds 80 beds and cancer services in Indore (Q1 FY27 p.8, p.17) and a Mumbai greenfield (Q2 FY27 p.10); KIMS Thane operating (Q2 FY27 p.14)."}
  - {type: FLAG-CAPEX-PER-BED-ESCALATION, reason: "MEDANTA plan average about Rs 1.41 Cr (May) to at least Rs 1.74 Cr (Nov) per bed, derived; YATHARTH per bed doubled in three years. Pune South kill signal Rs 1.2 Cr is live."}
  - {type: FLAG-CONFIRMED-NO-NAMED-PEER-MENTION, reason: "No peer mentions JLHL by name or description; overlaps by location only."}
peers_provided: 12
verified:
  - {claim: "Q1 greenfield breakeven timing and year-1 loss (40% reset sub-part only partly corroborated)", peers: [KIMS, MEDANTA, YATHARTH], anchor_count: 12}
  - {claim: "Q2 occupancy on census/operational beds with ex-new-hospital presentation", peers: [KIMS, MEDANTA, YATHARTH], anchor_count: 7}
  - {claim: "Q4 cashless empanelment takes about one year or longer (payer mix at 6/12 months not found)", peers: [KIMS, MEDANTA, YATHARTH], anchor_count: 9}
  - {claim: "Q7 capex per bed range and escalation (land split NOT FOUND)", peers: [MEDANTA, YATHARTH, KIMS], anchor_count: 9}
partially_verified:
  - {claim: "Q3 mature ARPOB grows at low to mid single digits (price vs mix split runs against JLHL: peers cite mix)", peers: [KIMS, MEDANTA, YATHARTH]}
  - {claim: "Q5 low senior doctor attrition (doctor cost percent of revenue NOT FOUND)", peers: [MEDANTA, YATHARTH, KIMS]}
  - {claim: "Q6 accruals plus debt funding mix (3x ceiling not corroborated; peers 1-2x)", peers: [KIMS, YATHARTH, MEDANTA]}
  - {claim: "Q8 Q1 and Q3 seasonally weaker (Q2 medical mix lowering ARPOB not corroborated)", peers: [KIMS, MEDANTA, YATHARTH]}
  - {claim: "Q9 onco cap impact small (one peer quantifies 0.3; pharmacy share NOT FOUND)", peers: [YATHARTH, KIMS, MEDANTA]}
  - {claim: "Q10 demand strong in Tier-2 style markets (bed shortage not shown; peers add supply in Indore and Thane)", peers: [MEDANTA, KIMS]}
contradicted: []
unverifiable:
  - {claim: "Q5 doctor cost as percent of revenue", peers_checked: [KIMS, MEDANTA, YATHARTH]}
  - {claim: "Q9 pharmacy share of revenue and margin", peers_checked: [KIMS, MEDANTA, YATHARTH]}
  - {claim: "Q10 Pune high-quality bed supply", peers_checked: [KIMS, MEDANTA]}
  - {claim: "Q4 payer mix at 6 and 12 months", peers_checked: [KIMS, MEDANTA, YATHARTH]}
peer_coverage_map:
  - {peer: "KIMS", quarter: "Q3 FY26", usage: "SUBSTANTIVE", contribution: "NABH not a prerequisite; Nashik breakeven month 13; debt peaked statement"}
  - {peer: "KIMS", quarter: "Q4 FY26", usage: "SUBSTANTIVE", contribution: "Empanelment delay; QIP debt cut; doctor retention; mature margin 29.5%"}
  - {peer: "KIMS", quarter: "Q1 FY27", usage: "SUBSTANTIVE", contribution: "ARPOB 4-5% guide; census occupancy cuts; Maharashtra part-time doctors"}
  - {peer: "KIMS", quarter: "Q2 FY27", usage: "SUBSTANTIVE", contribution: "Onco cap; Electronic City breakeven; net debt 2,150 Cr 1.9x; 70% occupancy in 4-6 years"}
  - {peer: "MEDANTA", quarter: "Q3 FY26", usage: "SUBSTANTIVE", contribution: "Noida peak loss Rs 320 million; single-tower build; seasonality of stays"}
  - {peer: "MEDANTA", quarter: "Q4 FY26", usage: "SUBSTANTIVE", contribution: "40-45% occupancy breakeven rule; Rs 4,500 Cr capex plan; net cash; attrition"}
  - {peer: "MEDANTA", quarter: "Q1 FY27", usage: "SUBSTANTIVE", contribution: "Noida loss Rs 49 million; Guwahati capex rise; Indore beds; occupancy ex-Noida"}
  - {peer: "MEDANTA", quarter: "Q2 FY27", usage: "SUBSTANTIVE", contribution: "Noida breakeven Rs 86 million; Rs 6,000 Cr capex; Ghaziabad Rs 1,000 Cr; tariff restraint"}
  - {peer: "YATHARTH", quarter: "Q3 FY26", usage: "SUBSTANTIVE", contribution: "Capex per bed Rs 60 lakh and Rs 80-90 lakh; breakeven at 30-35% of full beds"}
  - {peer: "YATHARTH", quarter: "Q4 FY26", usage: "SUBSTANTIVE", contribution: "Debt Rs 230 Cr; Noida brownfield Rs 75 lakh per bed; breakeven timelines"}
  - {peer: "YATHARTH", quarter: "Q1 FY27", usage: "SUBSTANTIVE", contribution: "Faridabad 9-month breakeven; debt comfort 2x EBITDA; attrition 7%; census beds"}
  - {peer: "YATHARTH", quarter: "Q2 FY27", usage: "SUBSTANTIVE", contribution: "Onco cap 0.3; Advent Rs 3,150 Cr; Model Town December breakeven; OCF conversion seasonality"}
industry_cross_read:
  demand: "Strong and consistent: inpatient volume +27% KIMS, +30% MEDANTA, +28% YATHARTH existing hospitals in Q2 FY27; no peer reports softness."
  pricing_inputs: "Tariffs near flat (MEDANTA 5% or less; KIMS ARPOB 4-5%); growth comes from mix; talent cost rising; insurers push price down at empanelment."
  capex_cycle: "Industry-wide capacity race among listed chains (MEDANTA +3,450 beds, YATHARTH to 5,000 plus Advent, KIMS pausing to 400-500 beds); JLHL is not a lone expander but is the debt-funded one; peers use equity or net cash."
peer_mentions_of_company: []
risks_peers_raise:
  - "Common insurer empanelment initiative delaying new-hospital panels (KIMS Q4 FY26 p.9; Q1 FY27 p.21)"
  - "Room-rent ceiling recommendation (YATHARTH Q1 FY27 p.11-12)"
  - "Kerala bill on private hospital charges (KIMS Q2 FY27 p.19)"
  - "Pollution and monsoon construction halts (MEDANTA Q2 FY27 p.10; YATHARTH Q1 FY27 p.19)"
  - "Government receivable delays and doubtful debt provisions (KIMS Q2 FY27 p.7-8)"
  - "Income tax demand notice and appeal (YATHARTH Q2 FY27 p.12-13)"
  - "Gulf conflict hitting international patients (YATHARTH Q2 FY27 p.11)"
  - "Part-time doctor practice in Maharashtra slowing ramp (KIMS Q1 FY27 p.13-14)"
  - "Returns dilution in capex cycle: KIMS FY26 PAT -41%, ROE/ROC down (KIMS Q4 FY26 p.4, p.19)"
  - "Medicine markup review at Supreme Court, open at all three peers"
net_narrative_effect: "complicates"
analyst_note: "Operating claims hold: breakeven in 9-15 months at all three peers, census-bed occupancy standard, seasonality real. Weak points are funding (3x ceiling vs peer 1-2x; peers raise equity or hold net cash) and the PAT lag (peer PAT growth 20-30 points below EBITDA growth in Q2 FY27). KIMS says NABH is not the empanelment gate, which may weaken the Dombivli NABH confirm signal. KIMS Thane is the Maharashtra analogue: flat losses for three quarters before breakeven. Dombivli Q2 is a seasonal best case. No peer names JLHL."
```
