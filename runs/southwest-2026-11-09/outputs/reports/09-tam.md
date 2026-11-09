# STAGE 9: TAM / SAM / SOM — SOUTHWEST (South West Pinnacle Exploration Ltd)
Run date 2026-11-09. Base year FY26 (year to 31 Mar 2026). All figures INR Cr unless stated. Status: PARTIAL (searches skipped, listed in Section 5E and the YAML).

Reading guide: "claim" = management statement, no filing evidence. "derived" = arithmetic shown from cited inputs. Anchors read (source, page): AR = Annual_Report_2026; Deck = Investor_Presentation_1 (Nov 2026); May call = Concall_May_2026; Jul call = Concall_Jul_2026; DS = inputs/screening/screener-Data_Sheet.csv.

Headline: the sourced market is a fraction of management's number. Conservative TAM INR 1,498 Cr against a management claim of INR 15,000-18,000 Cr (10.0x to 12.0x, inflated). SAM INR 987 Cr. Central SOM-implied revenue CAGR 14.3% (3 yr) and 14.1% (5 yr), below the 20% management guidance.

---------------------------------------------------------------------

## SECTION 1: MARKET DEFINITION

### 1A Boundaries
- Product scope IN: contract drilling for coal and non-coal minerals (core, large diameter, RC, underground), CBM production drilling, onshore 2D/3D seismic and passive seismic, aquifer mapping, geological and geophysical services (AR p.58-59).
- Product scope OUT: coal block mining (an owned option, no capex stated, production FY2028-29, AR p.60), Oman JVs (separate geography, AR p.60), oil and gas rig drilling, offshore seismic, drilling equipment sales.
- Geography: India only. Global figures are shown for reference, not summed.
- Customers: PSUs (CMPDI, Oil India, CGWB, Hindustan Copper) and private miners and energy firms (Reliance, Hindustan Zinc, Vedanta, Hindalco) (AR p.60-61).
- Channel: tendered or negotiated contract services. Spend that clients do with in-house (departmental) rigs is demand, but not contractor-addressable. The channel filter in Section 3A removes it.
- Price segment: per-metre and per-project contract pricing. Rigs are paid per metre in mineral exploration (May call p.16).
- Revenue base: FY26 sales INR 243.02 Cr (DS, Sales row, FY26). AR p.56 states INR 2,430 Mn.

### 1B Management's own TAM claim
| Item | Claim | Definition and date | Source | Credibility read |
|---|---|---|---|---|
| India exploration services market | INR 15,000-18,000 Cr, CAGR 8-10% | "Indian exploration services market", undated, no source named | AR p.57 | BROAD. No year, no source, no segment cut. |
| Global mineral exploration services | USD 10.31 bn (2024), USD 10.84 bn (2025), USD 18 bn (2035), CAGR about 5.2% | Third party data (wiseguyreports, IMARC per slide footer) | Deck p.24; AR p.56 | BROAD, 2024 base. Check: (18/10.84)^(1/10)-1 = 5.2%, arithmetic holds. |
| Coal block revenue | INR 700-800 Cr over first three years of production, EBITDA 40-42% | Option, outside this TAM | AR p.60 | SPECIFIC but unfunded. Calls give INR 300-400 Cr a year (B07 flag). Excluded here. |
| Rig population | "145 to 150 rigs operating, hydraulic rigs" nationally | Verbal, no definition of rig class | May call p.16 | CLAIM, scope unclear. |
| Growth guidance | "around 20% growth year on year in short to medium term" | CMD message | AR p.6 | Company guidance, used in Section 5. |

The India claim of INR 15,000-18,000 Cr is the figure held for comparison in Section 2.

---------------------------------------------------------------------

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

### Method 1, top-down. NOT EXECUTABLE on sourced data
The only top-down figure is management's INR 15,000-18,000 Cr. No third party source, no breakdown by oil and gas, equipment, in-house spend, or geoscience consulting is given, so no line-by-line subtraction can be sourced. Subtractions are marked NOT FOUND, not guessed. The claim is carried as a claim only.
Independent search (three queries, results in Section 5E) found no India exploration drilling services market size in INR from IBEF, CRISIL, ICRA or similar. The nearest figures are equipment: IMARC India mineral exploration equipment market USD 6.73 bn (2024), USD 13.45 bn (2033), scope is equipment, not services. Not used.

### Method 2, bottom-up on rig population (Confidence L)
- Addressable unit: one hydraulic exploration rig-year.
- Total units: 145 to 150 rigs operating in India (May call p.16, claim, scope unverified).
- Revenue per unit, SWPE-derived: drilling revenue = FY26 revenue less seismic and aquifer. Stream split from Deck p.5 via B04: CBM 37.19%, aquifer 24.93%, non-coal drilling 17.21%, seismic 16.13%, other 4.54%. Drilling-type revenue = 243.02 x (1 - 0.1613 - 0.2493) = 243.02 x 0.5894 = INR 143.24 Cr. Rig count 45 (AR p.58). Revenue per rig = 143.24 / 45 = INR 3.18 Cr.
- Market = 145 x 3.18 = INR 461 Cr; 150 x 3.18 = INR 477 Cr. Range INR 461-477 Cr.
- Cross-check: SWPE share by rig count = 45 / 147.5 = 30.5%; by revenue = 143.24 / 469 = 30.5%. The two agree because the method is circular by construction. This is not independent confirmation.
- Limits: SWPE rig yield is applied to the whole fleet; CBM rigs earn more per rig than mineral rigs; rig counts differ across documents (43 Jul call p.2, 45 AR p.58, 47 Deck per B04); departmental rigs may sit outside the 145-150.
- Staleness: May 2026 call, current.

### Method 3, programme and spend aggregation (Confidence L to M)
Government-funded exploration flows with a named annual figure:
| Flow | INR Cr | Arithmetic | Source and date | Staleness |
|---|---|---|---|---|
| Exploration of Coal and Lignite scheme, FY22-FY26 | 596 per year | 2,980 / 5 years = 596 (split 1,650 promotional, 1,330 non-CIL detailed drilling) | Cabinet approval June 2023 (Deccan Herald / PressReader reports) | STALE (3.4 yrs); lower confidence |
| NMET approved projects, 1 Jan 2024 to 31 Jan 2025 | 712 | 146 exploration and procurement projects, one year | Tripura Star News report of NMET data | STALE borderline (up to 2.8 yrs); includes procurement, so overstates drilling spend |
| Mission Anveshan 2D seismic (API) | 792 stock | Outlay INR 792 Cr across seven onland basins, 2,954 LKM acquired | DGH Annual Report 2024-25, p.84-88 | Annual flow NOT FOUND, so not added |
Annual government-funded flow used = 596 + 712 = INR 1,308 Cr. Two weaknesses are named: the coal figure is a scheme average, not FY26 actual spend; the NMET figure includes non-drilling and equipment procurement.

Private spend: NOT FOUND (no sourced captive or commercial block owner exploration spend). The evidenced private floor is what SWPE's private clients paid it.

Segments with no market size found (CBM production drilling outside Reliance, seismic annual flow, aquifer NAQUIM 2.0 budget): the demand floor is SWPE's own revenue in those streams, derived from Deck p.5 split: CBM 243.02 x 0.3719 = 90.38; seismic 243.02 x 0.1613 = 39.20; aquifer 243.02 x 0.2493 = 60.58. Floor total = INR 190.16 Cr. A floor says demand is at least this large. It is not a market estimate.

Peer revenue (DS Sales row, FY26): Asian Energy Services 791.05; Deep Industries 890.71; Jindal Drilling 996.57. Sum INR 2,678.33 Cr. These are oil and gas services and rig businesses with a small overlap in seismic and drilling; in-scope share NOT FOUND. Not used in TAM. SWPE at 243.02 is 9.1% of the peer-group sum (not like-for-like).
Unorganised sector: no source found. The stage instruction suggests a 30-60% range as a typical India bracket. It is applied only in the sensitivity below, labelled an assumption.

Realistic reading (Confidence L). The conservative reading counts only government-funded flows. SWPE's order mix is 70-75% private (Jul call p.12-15 claim; Deck p.17 shows 77% of order book). If the market had the same private share, private S1 spend = 1,308 x (72.5 / 27.5) = 1,308 x 2.636 = INR 3,448 Cr. Realistic TAM = 1,308 + 3,448 + 190 = INR 4,947 Cr. This extrapolates one company's mix to the market and is labelled so. If unorganised share is 30-60%, a 30% share on the 4,947 figure would scale only the unregistered portion, not the evidenced flows; no further scaling is done.

### Method 4, import substitution (partial)
Consumption and import data exist (India coal imports 246.37 MT FY26, Deck p.26; AR p.57 states 268.24 MT; the two documents disagree by 21.9 MT, not reconciled). Government targets: coal production 1,040.08 MT FY26 (Deck p.26). No conversion from import substitution to drilling metres or INR is sourced. Method gives direction only, no size.

### Method 5, global benchmark (not executable)
Global USD 10.31 bn (2024). A per-capita or per-GDP benchmark against China or SE Asia is not sourced, and the USD to INR rate is not in the corpus. Not computed.

### Triangulation table
| Method | Estimate INR Cr | Confidence | Staleness flag |
|---|---|---|---|
| M1 top-down (management) | 15,000-18,000 | L (claim) | undated |
| M2 rig bottom-up | 461-477 (drilling only, excludes seismic, aquifer, geoscience) | L | current |
| M3 programme flows, conservative (1,308 + 190 floor) | 1,498 | L-M | coal scheme STALE, NMET borderline |
| M3 with private extrapolation, realistic | 4,947 | L | extrapolation |
| M4 import substitution | NOT FOUND | - | - |
| M5 global benchmark | NOT FOUND | - | 2024 base borderline STALE |

Conservative TAM = INR 1,498 Cr. Realistic TAM = INR 4,947 Cr.

Divergence flag. M2 (INR 469 Cr) against the drilling part of M3 (INR 1,308 Cr) differs 2.8x. Reason: M3 counts all exploration spend, including geophysics, geochemistry, laboratory work, procurement, and departmental drilling; M2 counts hydraulic rigs only. The one observation that separates them is a rig census with owner (departmental vs contractor) from MECL, CMPDI or the IBM. NOT FOUND today. I carry M3 conservative as central because it rests on a filed or reported programme figure, where M2 rests on a verbal rig count and SWPE's own yield.

Management claim vs conservative: low end 15,000 / 1,498 = 10.0x; high end 18,000 / 1,498 = 12.0x. Read: INFLATED (above 2x). Against the realistic estimate: 15,000 / 4,947 = 3.0x, still above 2x. The "inflated" read holds on both readings. The observation that would change it: a dated third-party report that shows private exploration spend near INR 10,000 Cr. NOT FOUND.

---------------------------------------------------------------------

## SECTION 3: SAM AND SOM

### 3A SAM
Filters applied to the conservative TAM (INR 1,498 Cr):
| Filter | Treatment | INR Cr after |
|---|---|---|
| Product fit | TAM already limited to SWPE's service lines. Oil and gas rig drilling and offshore seismic excluded at definition | 1,498 |
| Geography | India only; all flows are India | 1,498 |
| Channel | Government-funded flow of 1,308 reduced to outsourced share. CMPDI FY26 outsourced 6.70 lakh m of 11.00 lakh m = 60.9% (IndianMasterminds report on CMPDI FY26 drilling; the report's departmental plus outsourced sum 11.00 does not match its achieved total 11.505, flagged). 1,308 x 0.609 = 796.7. Floor of 190.16 kept whole | 986.9 |
| Customer | Tender qualification (turnover, experience) cuts the contestable pool. Size NOT FOUND | no cut |
| Capability | Depth, CBM directional, seismic crew limits. Size NOT FOUND | no cut |
SAM = INR 987 Cr = 65.9% of conservative TAM (19.9% of realistic TAM 4,947). Two filters (customer, capability) carry no cut because the data is not found. SAM is therefore an upper bound on what SWPE can serve.

### 3B SOM
Current share. SAM has two parts: S1 coal and mineral drilling (INR 796.7 Cr) and the floor segments (INR 190.16 Cr, equal to SWPE's own revenue by construction). SWPE S1 revenue = 243.02 - 190.16 = 52.86 Cr, a 6.6% share of S1. The combined share is 243.02 / 986.9 = 24.6%. The 24.6% is inflated by the floor construction and is carried as the arithmetic base only. The honest reading: SWPE's share of the S1 pool is 6.6%; its share of the CBM, seismic and aquifer pools is NOT FOUND.

SAM growth. Evidence: management 8-10% (AR p.57, claim); CMPDI drilling +14% in FY26 (IndianMasterminds, one year); global 5.2% (stale, borderline). Central 10% (top of management range, supported by the CMPDI year). Two readings:
- Reading A (central, most evidenced): SAM grows 10% a year. FY29 SAM = 986.9 x 1.10^3 = 1,313.6. FY31 SAM = 986.9 x 1.10^5 = 1,589.4.
- Reading B (upside): the coal exploration scheme steps up. One report (single secondary source, not verified against Cabinet release) says INR 5,925 Cr for FY27-FY31 = 1,185 per year against 596 now. Then S1 government flow = (1,185 + 712) x 0.609 = 1,155.4; SAM = 1,155.4 + 190.2 = 1,345.6 in FY27, 36.3% above 986.9. Then 10% growth: FY29 = 1,345.6 x 1.10^2 = 1,628.2; FY31 = 1,345.6 x 1.10^4 = 1,970.1.
Separating observation: the Ministry of Coal's actual FY27 scheme release (Ministry of Coal Annual Report 2026-27 or Cabinet release).

Share trajectory. Rules: +1-2 pp in 3 years normal; +3-5 pp aggressive with capacity and execution; more than 5 pp only on competitor exit. Evidence for the aggressive case: order book INR 761 Cr = 3.1x FY26 revenue (AR p.59; B05), rigs on order, more than 100% utilisation (Jul call p.13 claim, includes subcontracted rigs), CBM competitors few (Jul call p.16). Evidence against: Q2 FY27 revenue 57.73 Cr, down 7.5% from 62.44 Cr in Q2 FY26 (DS Quarters); three customers 72.27% of revenue (AR p.146); margin 14.38% in Q2. I apply +3 pp at 3 years (27.6%) and +5 pp at 5 years (29.6%), the aggressive band, because forward evidence is documented. I do not shade lower or higher.

SOM, Reading A (central):
- 3 years (FY29): 1,313.6 x 27.63% = INR 362.9 Cr. CAGR = (362.9 / 243.02)^(1/3) - 1 = 1.4933^0.3333 - 1 = 14.3%.
- 5 years (FY31): 1,589.4 x 29.63% = INR 470.9 Cr. CAGR = (470.9 / 243.02)^(1/5) - 1 = 1.9377^0.2 - 1 = 14.1%.
SOM, Reading B:
- 3 years: 1,628.2 x 27.63% = 449.9; CAGR = (449.9 / 243.02)^(1/3) - 1 = 22.8%.
- 5 years: 1,970.1 x 29.63% = 583.7; CAGR = (583.7 / 243.02)^(1/5) - 1 = 19.2%.
Cross-check on delivery: FY23 to FY26 revenue CAGR = (243.02 / 117.73)^(1/3) - 1 = 27.3% (DS Sales row; includes the one-time coal trading end noted in B04). H1 FY27 revenue = 61.68 + 57.73 = 119.41 vs H1 FY26 = 40.22 + 62.44 = 102.66, growth 16.3% (DS Quarters, derived). The 16.3% sits between Reading A and Reading B.
Management guidance of 20%: FY29 revenue at 20% = 243.02 x 1.728 = 419.9, which needs a 32.0% share of Reading A SAM (+7.4 pp, above the 5 pp rule), or SAM growth near 15.5% with +3 pp. The guidance holds only if Reading B arrives.

### 3C Capacity cross-check
Input: capex_embedded_growth_pct 22 (range 19-32, a ceiling not a forecast; B07 analyst_note, uses the low reading of garbled capital commitments INR 17.21 Cr).
- Capacity-supported FY29 revenue = 243.02 x 1.22^3 = 243.02 x 1.8158 = INR 441.3 Cr. Reading A SOM3 = 362.9, Reading B SOM3 = 449.9.
- Capacity-supported FY31 revenue = 243.02 x 1.22^5 = 243.02 x 2.7027 = INR 656.8 Cr. SOM5 = 470.9 (A) and 583.7 (B).
Result: sufficient on both readings at 5 years and on Reading A at 3 years. Reading B SOM3 (449.9) exceeds the 22% ceiling (441.3) by INR 8.6 Cr, so at 3 years under Reading B the capex plan is the tighter limit. Capacity is not the binding limit for Reading A; demand and cash conversion are. Caveats: capital commitments column order garbled (AR note 42), rig capex per rig and funding NOT FOUND, rig count differs across documents (43 / 45 / 47). The ceiling is not a forecast; the SOM is the more optimistic side only under Reading B.

---------------------------------------------------------------------

## SECTION 4: GROWTH DRIVERS, RISKS AND STRUCTURE

### 4A TAM growth drivers
| Driver | Impact | Evidence |
|---|---|---|
| Regulatory tailwind | High | 500+ non-coal blocks for auction, 100% FDI, OALP, Mission Anveshan (AR p.58; Deck p.28). Coal scheme FY27-31 INR 5,925 Cr per one report vs 2,980 prior (single source, unverified) |
| Import substitution | Medium | Coal imports 246.37 MT FY26 (Deck p.26); AR p.57 says 268.24 MT |
| Penetration (depth) | Medium | "Exploration depth remains low" (Deck p.24, claim, no metric) |
| Formalisation | Medium | Private block owners outsourcing: CMPDI outsourced 60.9% of FY26 metres |
| New applications | Low-Medium | UCG: four blocks awarded, tenders to be floated by clients (Jul call p.12 claim); no order yet |
| Technology | Low | Seismic, PST, AI modelling (AR p.57) |
| Geographic (Oman) | Out of TAM | Outside India scope |
| Premiumisation, demographics | Not applicable | |

### 4B TAM risks and monitoring signals
| Risk | Signal |
|---|---|
| Cyclicality, mineral price falls cut private capex | LME copper and zinc, coal index (Section 6) |
| Government budget slippage or delay in new scheme cycle | Ministry of Coal scheme release |
| Aquifer re-tender gap: NAQUIM 1.0 identified area covered before 31 Mar 2023; NAQUIM 2.0 budget NOT FOUND; aquifer is 24.93% of SWPE revenue | CGWB tender notices |
| Monsoon and weather execution | Q2 margin (14.38%) |
| Tender price pressure (AR p.63) | Gross margin, order wins |
| Concentration on one client set (72.27% in three clients) | Receivables ageing, order mix |
| Substitution by in-house rigs of PSUs | CMPDI departmental vs outsourced metres |

### 4C Market structure
- Competitor count: NOT FOUND as a number. Management says two or three competitors per segment (May call p.9, claim), few CBM drilling players (Jul call p.16). Named: Alphageo and Asian Energy in seismic (May call p.9, analyst question).
- Top-3 concentration: NOT FOUND.
- Organised vs unorganised: NOT FOUND. MECL and CMPDI departmental rigs sit alongside contractors (CMPDI 39.1% departmental of reported split).
- Direction: management says "huge shortage of resources" and rising rates (May call p.16, claim). Entry barrier claim: capex heavy (Jul call p.16, claim). Rigs range INR 1.5 Cr to 40 Cr (Nov 2025 call), so entry cost for small rigs is low.
- Price vs differentiation: PSU work is tender and L1; private work is quotation with execution weight (Jul call p.15-16).
- Import share: not applicable to services.

---------------------------------------------------------------------

## SECTION 5: SUMMARY AND RUNWAY

### 5A Funnel
```
Management claim (India)       INR 15,000-18,000 Cr   claim, undated
        |   10.0x - 12.0x above conservative
Realistic TAM                  INR  4,947 Cr   (L, private extrapolated at SWPE mix)
Conservative TAM  (central)    INR  1,498 Cr   (1,308 govt flows + 190 floor)
        |   channel filter 60.9% on govt flows
SAM                            INR    987 Cr   (65.9% of conservative TAM)
SOM 3 yr (FY29), Reading A     INR    363 Cr   (27.6% share)
SOM 5 yr (FY31), Reading A     INR    471 Cr   (29.6% share)
SWPE FY26 revenue              INR    243 Cr   (24.6% of SAM, 6.6% of S1 pool)
```

### 5B Runway
- Revenue headroom = SAM / revenue = 986.9 / 243.02 = 4.06x. For S1 alone 796.7 / 52.86 = 15.1x.
- TAM growth: 10% central (management 8-10%, CMPDI +14%).
- Company vs TAM: FY23-26 CAGR 27.3% vs 10%, so SWPE is gaining share. H1 FY27 growth 16.3%, Q2 FY27 -7.5% YoY.
- Years to saturate SAM at historical pace: growth ratio 1.273 / 1.10 = 1.157 per year; ln(4.06) / ln(1.157) = 1.401 / 0.1459 = 9.6 years. At the central SOM pace of 14.3%: 1.143 / 1.10 = 1.039; 1.401 / 0.0383 = 36.6 years. Not a constraint inside a 3-5 year hold.

### 5C Runway class: GOOD
Headroom 4.06x, TAM growth about 10%, share gain evidenced in the past and in the order book. Not STRONG: market evidence is low confidence, SAM is an upper bound, and revenue per Q2 FY27 fell YoY. The standard matrix text was not supplied; class applies the stated labels with judgement.

### 5D SAM expansion levers
| Lever | Addition | Status |
|---|---|---|
| Coal scheme step-up (FY27-31) | +358.7 Cr SAM in FY27 (1,345.6 - 986.9), Reading B | single secondary source, unverified |
| UCG exploration | NOT FOUND | tenders to be floated by clients |
| Oil India seismic empanelment (3 yr, B07 B2) | NOT FOUND | no work order yet |
| Non-Reliance CBM | NOT FOUND | no order |
| Aquifer re-tender | replaces run-off of INR 59.5 Cr (595 Mn, B07) | not awarded |
| Oman and Jharkhand coal block | outside this TAM | options |
Revised headroom with the coal scheme step-up: 1,345.6 / 243.02 = 5.54x.

### 5E Final card and valuation implication
| Field | Value |
|---|---|
| Market | India contract exploration services (coal, minerals, CBM, seismic, aquifer) |
| TAM conservative / realistic | INR 1,498 Cr / 4,947 Cr |
| SAM | INR 987 Cr (65.9% of conservative TAM) |
| SOM 3y / 5y | INR 363 Cr / 471 Cr (Reading A); 450 / 584 (Reading B) |
| SOM-implied revenue CAGR | 14.3% / 14.1% (A); 22.8% / 19.2% (B) |
| Management claim ratio | 10.0x at low end, read INFLATED |
| Runway | GOOD |
| Capacity | sufficient on A; INR 8.6 Cr over the 22% ceiling at 3y on B |

Valuation implication line. At 14.3% revenue CAGR implied by SOM (Reading A), with margin held at the four-quarter PAT margin of 13.7% (TTM PAT 9.22 + 13.05 + 9.34 + 3.98 = 35.59 over TTM revenue 62.67 + 77.7 + 61.68 + 57.73 = 259.78, DS Quarters, derived), the earnings growth embedded here is about 14.3% CAGR. This neither supports a re-rating nor meets the 25% CAGR target. It supports the current trailing multiple of about 14.7x (market cap 524.08 Cr and price 160.58 from DS, date of price not stated; 524.08 / 35.59) only as roughly 1.0x PEG; the 15.9x on FY26 PAT 33.03 is the same price on the peak year. Share count rose from 2.98 Cr to about 3.26 Cr (524.08 / 160.58) after warrant conversion, so per share growth runs below PAT growth. Reading B (22.8%) would carry growth near the hurdle; the separator is the FY27 coal scheme release plus Q3 FY27 margin above 20%. Margin path itself belongs to stage 11 Section 1B; this stage does not set it.

Searches performed (Nov 2026 run):
1. India mineral exploration drilling market size crore NMET: found no INR drilling market size; found equipment USD figures, NMET and MECL and CMPDI volumes.
2. NAQUIM CGWB area mapped and budget: NAQUIM 1.0 area complete; NAQUIM 2.0 budget not found.
3. Ministry of Coal exploration plan 2025-26: scheme outlay and drilling targets found.
4. Fetch CMPDI FY26 drilling article: 11.00 target, 11.505 achieved, 4.30 departmental, 6.70 outsourced (sums do not reconcile).
5. Seismic market India 2D/3D: Mission Anveshan INR 792 Cr, contract examples; no market size.
6. Coal scheme FY27-31 outlay: INR 5,925 Cr from one report.
7. NMET 146 projects INR 712 Cr: confirmed by one report.
Skipped or failed: independent India exploration services market report (IBEF, CRISIL, ICRA, Ken, RedSeer) not found; apbi-icma fetch returned an unrelated page; no primary Cabinet or Ministry of Coal release fetched for the FY27-31 scheme; CBM production drilling market size; CGWB NAQUIM 2.0 budget; USD to INR rate. Status therefore partial.

---------------------------------------------------------------------

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

Candidates only. Verification at Role 5.5 per Downstream_Source_Discovery_Protocol_v1_0. No URL checked here. Eight externally observable demand drivers exist.

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | Reliance Industries CBM production drilling programme and well counts | End-customer | CBM is 37.19% of revenue and the INR 166 Cr extension (B07) | RIL Reg 30 filings, quarterly results, DGH production data | Quarterly |
| 2 | Hindustan Zinc exploration drilling and capex; Vedanta group | End-customer | INR 307 Cr order is about 40% of book (B04) | HZL and Vedanta quarterly production reports, Reg 30 | Quarterly |
| 3 | CMPDI outsourced drilling tenders and metres (SHARED) | End-customer | 6.70 lakh m outsourced FY26; coal exploration orders | CMPDI tender notices, Coal India annual report | Event-driven |
| 4 | Ministry of Coal exploration scheme FY27-31 outlay and release (SHARED with row 3) | Regulatory | Funds CMPDI and non-CIL block drilling; Reading B separator | Ministry of Coal annual report, PIB, Cabinet release | Event-driven |
| 5 | NMET approvals and mineral block auctions | Regulatory | Funds non-coal exploration; 500+ blocks per AR p.58 | Ministry of Mines, NMET governing body minutes, PIB | Event-driven |
| 6 | CGWB NAQUIM 2.0 tenders | Counterparty | Aquifer is 24.93% of revenue; NAQUIM 1.0 area covered | CGWB, Ministry of Jal Shakti tenders, Lok Sabha answers | Event-driven |
| 7 | Oil India and ONGC onshore seismic: OALP rounds, Mission Anveshan work orders | Counterparty | Seismic 16.13% of revenue; Oil India empanelment | DGH, Oil India Reg 30 | Event-driven |
| 8 | Copper, zinc and coal index prices | Macro | Private exploration capex follows commodity prices | Ministry of Coal notified prices, LME | Monthly |

SHARED flags: rows 3 and 4 depend on the same Ministry of Coal funding line; FTTCP counts them once.

```yaml
stage: B09-tam
company: "SOUTHWEST"
run_date: "2026-11-09"
model: claude-sonnet-5-5
status: partial
input_gaps:
  - "shareholding/ is empty: FII+DII UA qualifier and promoter pledge trend open (B00)"
  - "screener Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization sheets empty for main and three peers; Data_Sheet only (B00). Quarterly values in this stage come from Data_Sheet quarterly rows"
  - "no Q2 FY27 transcript: call is 11 Nov 2026, after this run (B00, HIGH freshness)"
  - "Q3 FY26 concall transcript (Feb 2026) not in corpus (B00)"
  - "annual-report/ holds FY25 and FY26 only; announcements Nov 2025 to Nov 2026 only (B00)"
  - "research/ empty: no broker notes (B00)"
  - "B04 gaps carried: rig utilisation, annual metres drilled, cost per metre, top-three customer names, competitor count NOT FOUND; rig count 45/47/43 and order book 7,613 Mn vs 5,812 Mn unreconciled"
  - "B09 gaps: no independent India exploration services market size in INR; private exploration spend, competitor count, top-3 concentration, unorganised share, NAQUIM 2.0 budget, FX rate NOT FOUND"
flags:
  - {type: FLAG-MGMT-TAM-INFLATED, reason: "Claim INR 15,000-18,000 Cr is 10.0x-12.0x conservative TAM 1,498 and 3.0x realistic 4,947; undated, unsourced (AR p.57)"}
  - {type: FLAG-SAM-UPPER-BOUND, reason: "Customer and capability filters carry no cut (data NOT FOUND); floor segments equal SWPE revenue by construction so combined share 24.6% is biased; S1 share 6.6%"}
  - {type: FLAG-STALE-INPUTS, reason: "Coal scheme INR 2,980 Cr (June 2023) STALE; NMET INR 712 Cr (Jan 2024-Jan 2025) borderline; global USD 10.31 bn (2024) borderline"}
  - {type: FLAG-SINGLE-SOURCE-UPSIDE, reason: "Reading B rests on INR 5,925 Cr FY27-31 coal scheme from one secondary report, not verified against Cabinet release"}
  - {type: FLAG-GUIDANCE-GT-SOM, reason: "Management 20% guidance (AR p.6) exceeds central SOM-implied 14.3%; needs +7.4 pp share on Reading A SAM or Reading B"}
  - {type: FLAG-METHOD-DIVERGENCE, reason: "Rig bottom-up INR 461-477 Cr vs programme flows INR 1,308 Cr, 2.8x; separator is a rig census by owner, NOT FOUND"}
  - {type: FLAG-CONCENTRATION, reason: "Three customers 72.27% of revenue (AR p.146); HZL + Reliance extension 62% of book (B07)"}
market_definition: "India contract exploration services (coal and mineral drilling, CBM production drilling, onshore seismic, aquifer mapping, geoscience), ex Oman, ex coal block mining"
tam_cr: {conservative: 1498, realistic: 4947}
sam_cr: 987
sam_pct_of_tam: 65.9           # of conservative TAM; 19.9 of realistic
som_3yr_cr: 363                # Reading A central; Reading B 450
som_5yr_cr: 471                # Reading A central; Reading B 584
som_implied_revenue_cagr: {yr3: 14.3, yr5: 14.1}   # Reading A; Reading B 22.8 / 19.2
current_sam_share_pct: 24.6    # floor-biased; S1 share 6.6
revenue_headroom_x: 4.06
tam_growth_pct: 10
runway_class: "GOOD"
mgmt_claim_cr: 15000           # low end of 15,000-18,000
mgmt_claim_ratio: 10.0
mgmt_claim_read: "inflated"
capacity_check: "sufficient on Reading A (SOM3 363 and SOM5 471 below 22% ceiling 441 and 657); Reading B SOM3 450 exceeds ceiling 441 by INR 8.6 Cr, capex plan is the tighter side there"
methods_used: ["M2 bottom-up rig population", "M3 programme and spend aggregation with demand floor", "M3 peer scale check (not used in TAM)", "M4 import substitution (direction only)"]
stale_data_flags:
  - {datapoint: "Exploration of Coal and Lignite scheme INR 2,980 Cr FY22-26", source: "Cabinet approval reports", year: 2023}
  - {datapoint: "NMET 146 projects INR 712 Cr", source: "NMET data via Tripura Star News", year: "2024-25"}
  - {datapoint: "Global mineral exploration services USD 10.31 bn", source: "wiseguyreports/IMARC via Deck p.24", year: 2024}
  - {datapoint: "Mission Anveshan INR 792 Cr outlay", source: "DGH Annual Report 2024-25", year: 2025}
  - {datapoint: "NAQUIM 1.0 area completion", source: "CGWB / PIB reports", year: 2023}
searches_performed:
  - "India mineral exploration drilling market size crore NMET exploration expenditure 2025"
  - "National Aquifer Mapping NAQUIM CGWB area mapped remaining crore programme"
  - "Ministry of Coal exploration plan 2025-26 drilling meters coal exploration scheme crore target"
  - "WebFetch CMPDI FY26 drilling targets (indianmasterminds)"
  - "India seismic data acquisition 2D 3D market OALP ONGC Oil India Mission Anveshan 2026"
  - "Cabinet approves continuation exploration of coal and lignite scheme 2026-27 to 2030-31 outlay"
  - "NMET approves exploration projects worth Rs 712 crore 146 projects"
searches_skipped:
  - "Independent India exploration/drilling services market report (IBEF, CRISIL, ICRA, Ken, RedSeer): not found in three searches"
  - "apbi-icma.org fetch returned unrelated page; FY27-31 coal scheme not verified against primary Cabinet or Ministry of Coal release"
  - "CBM production drilling market size: not searched, no source"
  - "CGWB NAQUIM 2.0 budget and remaining area: not found"
  - "USD to INR rate: not in corpus, global USD figure not converted"
downstream_candidates:
  - {signal: "Reliance Industries CBM production drilling programme and well counts", entity_type: "end-customer", demand_link: "CBM is 37.19% of revenue plus INR 166 Cr extension", likely_source: "RIL Reg 30 filings, quarterly results, DGH production data", cadence: "quarterly", shared: false}
  - {signal: "Hindustan Zinc exploration drilling and capex; Vedanta group", entity_type: "end-customer", demand_link: "INR 307 Cr order is about 40% of order book", likely_source: "HZL and Vedanta quarterly production reports, Reg 30", cadence: "quarterly", shared: false}
  - {signal: "CMPDI outsourced drilling tenders and metres", entity_type: "end-customer", demand_link: "6.70 lakh m outsourced in FY26; coal exploration orders", likely_source: "CMPDI tender notices, Coal India annual report", cadence: "event-driven", shared: true}
  - {signal: "Ministry of Coal exploration scheme FY27-31 outlay and release", entity_type: "regulatory", demand_link: "Funds CMPDI and non-CIL block drilling; separates Reading A and B", likely_source: "Ministry of Coal annual report, PIB, Cabinet release", cadence: "event-driven", shared: true}
  - {signal: "NMET approvals and mineral block auctions", entity_type: "regulatory", demand_link: "Funds non-coal exploration; 500+ blocks for auction", likely_source: "Ministry of Mines, NMET governing body minutes, PIB", cadence: "event-driven", shared: false}
  - {signal: "CGWB NAQUIM 2.0 tenders", entity_type: "counterparty", demand_link: "Aquifer mapping is 24.93% of revenue; run-off replacement", likely_source: "CGWB, Ministry of Jal Shakti tenders, Lok Sabha answers", cadence: "event-driven", shared: false}
  - {signal: "Oil India and ONGC onshore seismic: OALP, Mission Anveshan work orders", entity_type: "counterparty", demand_link: "Seismic is 16.13% of revenue; Oil India empanelment", likely_source: "DGH, Oil India Reg 30", cadence: "event-driven", shared: false}
  - {signal: "Copper, zinc and coal index prices", entity_type: "macro", demand_link: "Private exploration capex follows commodity prices", likely_source: "Ministry of Coal notified prices, LME", cadence: "monthly", shared: false}
demand_externally_verifiable: true
analyst_note: "Central case is Reading A (SAM +10% a year, +3 pp share at 3y, +5 pp at 5y) because it rests on filed and reported figures. Reading B (22.8% / 19.2%) assumes the coal exploration scheme rises from about INR 596 Cr to 1,185 Cr a year from FY27, one secondary report. Separator: FY27 Ministry of Coal scheme release plus Q3 FY27 margin and revenue. SAM is an upper bound (two filters uncut) and the 24.6% share is floor-biased; the S1 share is 6.6%. Rig bottom-up (INR 469 Cr) is circular on SWPE yield. Valuation line: 14.3% growth, TTM PAT margin 13.7%, trailing P/E about 14.7x on DS price (date unstated)."
```
