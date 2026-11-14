# STAGE 9 TAM / SAM / SOM: Onward Technologies Ltd (ONWARDTEC), run 2026-11-12

Status: partial (web searches skipped or blocked, listed in the block). Units: USD bn shown beside INR Cr. FX: Rs 94.68 per USD (RBI-linked close of 22 Jun 2026, newsonair.gov.in, seen in a search result snippet only; the page was not opened; no November 2026 rate found). Every USD to INR conversion below uses it. The rate is 4.7 months old; a move of 5% shifts every INR TAM figure by 5%. SOM figures do not use FX (INR native).

Load-bearing facts from B00 (carried, checked before this stage's work):
1. Q2 FY27 margin 15.6% vs guide 13.8-14.3%: not a TAM item. Carried to the margin line in 5E (guide used, not the 15.6%).
2. Guidance vs delivery: checked in 3B. H1 FY27 revenue = 149.43 + 170.18 = 319.61 vs H1 FY26 133.15 + 138.97 = 272.12, +17.5% (screener-Data_Sheet.csv quarterly Sales). FY27 guide 15-18% (Concall_Oct_2026_Transcript.pdf p.4; Investor_Presentation_1.pdf slide p.14).
3. Concentration: 18.3% single customer, top 25 = 87% (Investor_Presentation_1.pdf p.15; B04). Used as the binding SOM constraint in 5B.
4. Promoter holding fall: not a TAM item.

---
## SECTION 1: MARKET DEFINITION

1A Boundaries.
- Product scope: outsourced engineering R&D and digital engineering services: mechanical, electronics and embedded, digital and data, digital factory (B04; AR26 p.10-11 by B04 cite). Billed 88% time and material in FY26, 85% in Q2 FY27 (B04, Inv. Pres. slide 11).
- Customer scope: OEMs. Industrial and heavy machinery 65%, transportation and mobility 32%, healthcare and life sciences 3% of H1 FY27 revenue (Investor_Presentation_1.pdf p.5).
- Geography: 100% overseas clients, 70% North America and 30% Europe (Investor_Presentation_1.pdf p.5; Annual_Report_2026.pdf p.10). "No India customers" (Concall_Oct_2026_Transcript.pdf p.5). B04 flags a conflict on the geography split basis (billing entity vs client location); this stage uses the client-location reading (70/30).
- Channel: direct master service agreements, 72 active clients, 16 above USD 1 mn (Investor_Presentation_1.pdf p.5, p.15).
- Price segment: mid-cost offshore-led delivery, 69% offshore in Q2 FY27 (Investor_Presentation_1.pdf p.11).
- Includes: third-party (vendor) ER&D services bought by OEMs. Excludes: captive centres (GCCs) as a revenue pool (they are a substitute, see 4B), software-product engineering for ISVs, semiconductor design, aerospace and defence certification work, hardware sales, domestic Indian demand.

1B Management claims.
- Claim A: "GLOBAL ER&D MARKET (TAM) >$2.5 Trillion by 2030, growing at 8-9% CAGR" (Investor_Presentation_1.pdf p.20, dated 16 Oct 2026). Credibility: BROAD. It is total enterprise ER&D spend, which includes in-house spend; most of it is never bought from a vendor.
- Claim B: ER&D outsourcing $81.5 bn (CY2024) to $133-135 bn (CY2030P) (same slide; AR p.45 states "$81-82 billion in CY 2024 to around $133-135 billion by CY 2030, 8.5-9.5%", source Nasscom-Everest ER&D Report 2025). Credibility: REASONABLE. It is the vendor pool.
- Claim C: "India engineering offshoring ... projected to compound at ~22% CAGR" (Investor_Presentation_1.pdf p.20). Credibility: unsupported. No source on the slide. INFERENCE: the 22% matches the BCG-Nasscom figure that India's share of the global ER&D sourcing market rises to 22% by FY30 (autocarpro.in, 12 Oct 2023), so the slide may have turned a share into a growth rate. Nasscom's own path is India ER&D $63 bn (FY26) to over $100 bn by 2030 (letsdatascience.com summary of a Nasscom study, seen in snippet): ln(100/63)/4 gives 12.2% CAGR (derived). The 22% is not carried into any estimate here.
- Also: Investor_Presentation_1.pdf p.15 states "FY26 revenue Rs 550.9 cr (+10.5% YOY)". That is total income. Revenue from operations is Rs 543.85 Cr (screener-Data_Sheet.csv Sales FY26; AR26 Note 34 p.93 per B02/B03). Stage 9 uses 543.85.

---
## SECTION 2: TAM ESTIMATION

Method 1, top-down (vendor pool).
- CY2024: $81.5 bn (Investor_Presentation_1.pdf p.20; AR p.45; Nasscom-Everest ER&D Report 2025). In INR: 81.5 x 94.68 = 7,716.4 bn = Rs 7,71,640 Cr. STALE flag: CY2024 data is more than 2 years before the run date at its mid-point; confidence lowered to M.
- CY2030P: $133-135 bn. Implied CAGR from the midpoint: (134/81.5)^(1/6) - 1 = 8.6% (ln 1.644 = 0.4968; /6 = 0.0828; e^0.0828 = 1.0863). The AR states 8.5-9.5%; the 8.6% derived here sits at the low end of the AR range. Low case (133): 8.5%.
- CY2026E: 81.5 x 1.0863^2 = 81.5 x 1.1800 = $96.2 bn = 96.2 x 94.68 = 9,108 bn = Rs 9,10,820 Cr. This is a projection of the CY2024 base, not a filed figure.
- No subtraction at this level: the pool is already vendor-only. Vertical, geography and capability subtractions are in SAM (Section 3).

Method 2, bottom-up on spend and outsourcing penetration.
- Global enterprise ER&D spend $1.8 tn (2023) to $2.5-3.3 tn (2030), AR26 p.9 (Chairman's message) citing Nasscom; AR p.45 cites 8-9% growth. 2023 spend to 2024 outsourced pool is a year mismatch; stated.
- Penetration: 81.5 / 1,800 = 4.5% (year mismatch, indicative).
- CY2026E spend at 8.5%: 1.8 tn x 1.085^3 (= 1.2773) = $2.30 tn. At 4.5% penetration: $104.1 bn. Versus Method 1: +8%. Methods agree within 10%. Confidence L-M (the 8.5% is the low end of the AR's 8-9%).
- Penetration path check: CY2030 133-135 / 2,500-3,300 = 4.0-5.4%, so the sources assume outsourcing share of spend roughly flat. The market is not assumed to shift to vendors.

Method 3, peer revenue aggregation (organised Indian-listed floor, plus Quest Global). Latest fiscal year, Rs Cr:
| Company | Revenue | Source |
|---|---|---|
| LTTS | 10,995.9 | LTTS-Data_Sheet.csv Sales FY26 |
| Tata Technologies | 5,505.57 | TATATECH-Data_Sheet.csv Sales FY26 |
| Cyient | 7,268.2 | CYIENT-Data_Sheet.csv Sales FY26 (includes non-ER&D lines) |
| KPIT | 6,454.93 | web search snippet, FY26 revenue from operations (autocarpro/Business Standard class report; not opened) |
| Tata Elxsi | 3,757.4 | web search snippet, FY26 (not opened) |
| Quest Global | about 10,415 | USD 1.1 bn (Reuters-based report Feb 2026, snippet) x 94.68; fiscal year not confirmed; current FX overstates it |
| Onward | 543.85 | screener-Data_Sheet.csv Sales FY26 |
- Sum = Rs 44,941 Cr = $4.75 bn = 4.9% of the CY2026E pool of $96.2 bn.
- Global vendors (Capgemini Engineering, Akkodis, Alten, Tech Mahindra and others) NOT FOUND: not searched. The sum is a floor for the organised vendor revenue, not a TAM estimate. Unorganised share: NOT FOUND, no source; no estimate given. Confidence L as a TAM method.

Method 4, import substitution: not applicable (export service). Method 5, per-capita global benchmark: not applicable (B2B services sold to foreign OEMs; no per-capita driver).

Divergent estimate, shown not averaged. BCG-Nasscom puts the global ER&D sourcing market at about $210-280 bn (2023; autocarpro.in 12 Oct 2023 and a snippet of the BCG report). That is 2.6x to 3.4x the Nasscom-Everest $81.5 bn. INFERENCE: sourcing counts captive (GCC) and offshore in-house spend, while the Everest outsourcing figure counts only third-party vendors. The separating observation is the scope table in the BCG report, which was not opened. The central estimate carries the Everest vendor pool because Onward sells to third parties only. STALE: the BCG data is 2023, direction only. A third figure (Mordor Intelligence, India ER&D services $133.7 bn in 2025, snippet) is a different scope again and is not used.

Triangulation table:
| Method | Estimate (USD bn) | Rs Cr | Confidence | Flag |
|---|---|---|---|---|
| 1 Everest/Nasscom CY24 | 81.5 | 7,71,640 | M | STALE (CY24) |
| 1 projected CY26E | 96.2 | 9,10,820 | M | projection |
| 2 spend x penetration CY26E | 104.1 | 9,85,600 | L-M | year mismatch |
| 3 peer floor | 4.75 | 44,941 | L | floor only |
| BCG sourcing 2023 | 210-280 | 19,88,000-26,51,000 | L | STALE, wider scope |
- Conservative TAM: Rs 7,71,640 Cr (CY24 pool, no growth carried). Realistic TAM: Rs 9,10,820 Cr (CY26E).
- Management claim vs conservative: Claim A, $2.5 tn = 2,500 x 94.68 = 236,700 bn = Rs 2,36,70,000 Cr. Ratio = 2,36,70,000 / 7,71,640 = 30.7x. Standard read: INFLATED (more than 2x), but the claim is a different scope (total spend, in-house included) and a different year (2030). Claim B (vendor pool, CY30, $134 bn = Rs 12,68,700 Cr) is 1.64x the CY24 base, which is growth, and reads REASONABLE. The block carries Claim A as the headline claim and says so.

---
## SECTION 3: SAM AND SOM

3A SAM. The five filters applied to the realistic TAM of $96.2 bn. The vertical split of global outsourced ER&D was searched for and NOT FOUND (Everest/Nasscom full report paywalled; two searches). Every filter percentage below is therefore an ANALYST ASSUMPTION, not a sourced figure. Each carries a range, and the sensitivity is shown. Confidence in the SAM level is LOW.
| Filter | Basis | Central | Range | Running USD bn |
|---|---|---|---|---|
| Product and vertical fit | Onward serves industrial, transport, healthcare only; ISV/internet is the largest ER&D spend vertical (Everest 2024 snippet) and is excluded, as are semiconductors, telecom, A&D | 35% | 25-45% | 33.67 |
| Geography | Clients are North America and Europe only (Inv. Pres. p.5); Asia/Japan buyers excluded | 85% | 80-90% | 28.62 |
| Channel and customer | OEM programs from about USD 0.5 mn up to large multi-year programs; 72 active clients | 60% | 50-70% | 17.17 |
| Capability | Mechanical, embedded, digital, data; about 3,000 engineers (Concall_Oct_2026_Transcript.pdf p.5) | 75% | 70-80% | 12.88 |
- Central SAM = 96.2 x 0.35 x 0.85 x 0.60 x 0.75 = $12.88 bn = x 94.68 = 1,219.4 bn = Rs 1,21,936 Cr. SAM / TAM = 13.4%.
- Low SAM: 0.25 x 0.80 x 0.50 x 0.70 = 7.0% of TAM = $6.73 bn = Rs 63,760 Cr. High SAM: 0.45 x 0.90 x 0.70 x 0.80 = 22.7% = $21.82 bn = Rs 2,06,570 Cr.
- The two readings (low vs high) differ by 3.2x. The observation that separates them: the vertical split of the Everest/Nasscom pool, and the share of it bought by NA/Europe OEMs. Position size, not the SAM, carries the caution. The SOM and the stage 11 handoff below do not depend on the SAM level, because Onward's share is far under 1% in every case (see 3B).
- Current share of SAM = 543.85 / 1,21,936 = 0.446% (low SAM: 0.85%; high SAM: 0.26%).

3B SOM. The pp share-gain rules (1-2 pp in 3 years) are for companies with material share. Onward holds 0.45% of SAM. One pp of SAM is Rs 1,219 Cr, more than twice Onward's revenue, so the pp rule does not bind and is not used to set growth. The SOM is built from the filed trajectory instead, and the pp rule is run afterwards as a check.
- Evidence anchors: FY22-FY26 revenue CAGR 15.3% (Investor_Presentation_1.pdf p.5; check: 307.27 to 543.85 in screener-Data_Sheet.csv, ratio 1.7699, fourth root 1.1534). FY26 growth 10.5% against Nasscom's ER&D export growth of 7.7% in FY25-26 (AR p.44), so the observed excess over market is 2.8 pp. H1 FY27 growth 17.5% (derived above). FY27 guide 15-18%.
- Two readings of FY27. Reading 1, the guide: Rs 543.85 x 1.15 to 1.18 = Rs 625.4 to 641.7 Cr; this implies H2 revenue of Rs 305.8 to 322.1 Cr, below the Q2 quarter of Rs 170.18 Cr (x2 = 340.4). Reading 2, run-rate flat: H1 319.61 + 340.4 = Rs 660.0 Cr, +21.4%. The observation that separates them is Q3 FY27 revenue against Rs 170.18 Cr. The SOM uses the top of the guide (18%), since H1 delivered 17.5% and the run rate supports at least that. Reading 2 is the upside.
- Growth rule after FY27: linear fade from 18% in FY27 to 11.4% in FY31, where 11.4% = SAM growth 8.6% + the observed 2.8 pp excess. Step: (18.0 - 11.4) / 4 = 1.65 pp a year.
| Year | Growth | Revenue Rs Cr |
|---|---|---|
| FY26 | actual | 543.85 |
| FY27 | 18.0% | 641.74 |
| FY28 | 16.35% | 746.66 |
| FY29 | 14.7% | 856.42 |
| FY30 | 13.05% | 968.18 |
| FY31 | 11.4% | 1,078.55 |
- 3-year (FY29) SOM = Rs 856 Cr. CAGR = (856.42 / 543.85)^(1/3) - 1 = 16.3% (ratio 1.5747, ln 0.4543, /3 = 0.1514).
- 5-year (FY31) SOM = Rs 1,079 Cr. CAGR = (1,078.55 / 543.85)^(1/5) - 1 = 14.7% (ratio 1.9833, ln 0.6846, /5 = 0.1369).
- Cross-check, careful case (SAM growth + 2.8 pp, flat 11.4%): FY29 Rs 752 Cr, FY31 Rs 933 Cr. Cross-check, history case (15.3% flat): FY29 Rs 835 Cr, FY31 Rs 1,110 Cr. The central 5-year CAGR of 14.7% sits 0.6 pp under the 15.3% history, as the cross-check requires. The central case is built off forward evidence (guide, H1 delivery), not history.
- Share check: SAM grows at 8.6% from CY26E: x1.2818 by year 3 = Rs 1,56,300 Cr, x1.5126 by year 5 = Rs 1,84,440 Cr. Share = 856 / 1,56,300 = 0.548% (3 years) and 1,079 / 1,84,440 = 0.585% (5 years). Gain = +0.10 pp in 3 years, below the 1-2 pp normal band. The SOM is not a share-grab story.
- The SOM conflicts with nothing in the TAM. The risk to it is concentration: one customer is 18.3% and the top 25 are 87% (B04; Inv. Pres. p.15). Loss of the largest account (18.3% of Rs 543.85 = Rs 99.5 Cr, derived) is a larger swing than the SOM's first-year increase would absorb quickly. This sits in position size.

3C Capacity cross-check. B07 has not run; no capex_embedded_growth figure exists. The business is people-based, so capacity is heads times revenue per head.
- FY26 cash capex Rs 1,911.07 lakh = Rs 19.11 Cr, 3.5% of revenue (AR26 p.66 per B03; 19.11 / 543.85).
- Revenue per head Rs 23.3 lakh annualised in Q2 FY27 on 2,917 closing heads (170.18 x 4 = 680.72 Cr; /2,917 = Rs 0.2334 Cr, derived; B04). Held flat, FY29 SOM needs 856.42 / 0.2334 = 3,669 heads (+752); FY31 SOM needs 1,078.55 / 0.2334 = 4,621 heads (+1,704 over 4.25 years, about 400 a year).
- H1 FY27 net hires = 432 (Inv. Pres. p.7), a pace of about 860 a year, which is twice the 400 a year needed. Four Pune and other delivery centres: Pune, Chennai, Bangalore, Hyderabad (Concall_Oct_2026_Transcript.pdf p.4). Capacity is sufficient. Which side is optimistic: neither. The constraint is billable utilisation, not seats: the hires made ahead of revenue have pushed H1 incremental EBITDA margin to 16.6% (10.5% ex credit) from 51.7% in FY26 (B04 FLAG-LOW-OPERATING-LEVERAGE-H1). PERM and onsite hiring in the US is a stated constraint on guidance (Concall_Oct_2026_Transcript.pdf p.5).

---
## SECTION 4: GROWTH DRIVERS, RISKS AND STRUCTURE

4A Drivers.
| Driver | Impact | Evidence |
|---|---|---|
| Technology enablement / new applications (AI data-centre power and cooling engineering) | High, unsized | Rs 33 Cr new 3-year contract (Jun 2026, power-management leader's data-centre unit) and active RFQs (Inv. Pres. p.14; Concall p.4). Share of revenue from data-centre work: NOT FOUND. Hyperscaler capex about $600 bn for 2026 and Vertiv backlog $15.0 bn (web snippets, Dell'Oro/Bloomberg Intelligence; not opened) is demand for the OEMs' products, not proof of outsourced engineering demand. |
| Outsourcing shift by OEMs | Medium | Deck p.14; AR p.45 states the outsourcing pool grows 8.5-9.5%, faster than the spend growth of 8-9% only at the top of the range; penetration is roughly flat (Method 2). So the shift is not evidenced as share gain from in-house to vendors. |
| Geographic expansion within existing accounts | Medium | USA share of revenue 34% to 41% from Q2 FY26 to Q2 FY27 (Inv. Pres. p.11). |
| New applications: EV, SDV, electrification | Medium | Deck p.21 and p.20; no revenue split. |
| Formalisation, import substitution, per-capita, regulatory tailwind, demographics | Not applicable | Export service to OEMs. |

4B Risks.
| Risk | Monitoring signal |
|---|---|
| Cyclical R&D budget cuts by OEMs (AR p.44: R&D budget rationalisation, delayed decisions) | Heavy machinery and mining OEM order books; Onward Q3 FY27 revenue vs Rs 170.18 Cr |
| AI-driven engineering productivity cuts billable hours (AR p.45 notes a shift "away from headcount-based growth toward outcome-driven"); Onward is 85% T&M | fixed price share above 15%; revenue per head |
| Captive substitution (GCCs; India 34% of new R&D centre announcements in CY25, AR p.44) | GCC announcements in Onward's verticals |
| US onsite regulation (PERM), management "a bit cautious" (Concall p.5) | onsite hiring cost, offshore share below 68% |
| FX: reported 22.4% vs constant currency 17.7% in Q2 FY27 (B04) | INR per USD |
| Concentration (18.3% single customer) | top client above 20% |

4C Structure. Competitor count globally: NOT FOUND. Top-3 concentration: NOT FOUND. Indian listed peers alone sum to Rs 44,941 Cr (Method 3), 83x Onward. Consolidating at the top: Cyient bought TAO Digital (event call 1 Jun 2026, peer-concalls file); Quest Global is preparing an Indian IPO (snippet). Price versus differentiation: Onward pricing power is weak (B04). Organised vs unorganised: NOT FOUND.

---
## SECTION 5: SUMMARY AND RUNWAY

5A Funnel (Rs Cr, USD bn at 94.68):
- Global enterprise ER&D spend (claim A, context only): $2.5 tn by 2030, Rs 2,36,70,000 Cr
- TAM, outsourced ER&D CY2024 (conservative): $81.5 bn, Rs 7,71,640 Cr
- TAM CY2026E (realistic): $96.2 bn, Rs 9,10,820 Cr
- SAM central: $12.9 bn, Rs 1,21,936 Cr (13.4% of TAM; range Rs 63,760 to 2,06,570 Cr)
- SOM FY29 Rs 856 Cr; SOM FY31 Rs 1,079 Cr
- Onward FY26 revenue Rs 543.85 Cr = 0.446% of SAM

5B Runway.
- Headroom = 1,21,936 / 543.85 = 224x (low SAM 117x; high SAM 380x).
- TAM growth 8.6%. SOM CAGR 14.7% (5 years) is 6.1 pp above it, so the model has Onward gaining share on a very small base, not riding the market. FY26 actual (10.5%) was 2.8 pp above the 7.7% Nasscom ER&D growth.
- Years to saturate SAM at 14.7% growth against SAM growth of 8.6%: ln(224) / ln(1.1467 / 1.0863) = 5.412 / 0.0544 = about 99 years. Saturation is not a constraint.

5C Class. The standard classification matrix is not in the injected inputs; the thresholds are not available to this stage. Headroom alone reads MASSIVE. TAM growth of 8.6% is moderate. The binding limits are account concentration and utilisation, not market size. Classified STRONG, stated as a judgement. The separating observation from MASSIVE: wins outside the existing top 25 accounts.

5D SAM expansion levers pursued: data-centre infrastructure engineering for power and cooling OEMs (Rs 33 Cr contract; potential addition NOT FOUND, no sizing source); deeper US accounts (revenue share 41%); healthcare and life sciences at 3% of revenue (no investment sizing found). Revised headroom: no change, because no lever is sized.

5E Output card. At 14.7% revenue CAGR implied by SOM (5 years; 16.3% over 3 years), with EBITDA margin trajectory of 13.2% (FY26) to the FY27 guide of 13.8-14.3% (midpoint 14.05%, Concall_Oct_2026_Transcript.pdf p.4) and held flat after, the earnings growth embedded here is about 16.1% EBITDA CAGR (1.1467 x (14.05 / 13.21)^(1/5) = 1.1467 x 1.0124 = 1.1609, derived; FY26 margin 13.21% from B04). Below EBITDA the tax, D&A and other-income bridge is not built at this stage. Against a market cap of Rs 841.82 Cr and FY26 net profit of Rs 44.32 Cr (screener-Data_Sheet.csv), the trailing P/E is 19.0x (derived). The step 1 brief shows 16.5x (screener, 11 Nov 2026; memory, not anchored). The embedded growth of 16.1% supports a multiple in the high teens on a PEG near 1.2. It does not reach the 25% CAGR hurdle through earnings growth alone; any gap to 25% would have to come from re-rating, which belongs to stage 11 and Section 1B. The Q2 margin of 15.6% is not used (it includes the Rs 2.93 Cr R&D credit, B04).

---
## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

Onward's named end-customers are NOT FOUND (all unnamed in the corpus: the 18.3% customer, the construction and mining equipment leader, the power-management leader's data-centre unit). Candidates are therefore classes of entity, not Onward's customers by name. Verification at Role 5.5 per the Downstream_Source_Discovery_Protocol_v1_0 source registry; no URLs checked here.
| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | Order backlog of data-centre power and cooling OEMs (for example Vertiv, Eaton) | End-customer | Onward engineers for OEMs that equip and power data centres (Inv. Pres. p.14). SHARED with row 2 | OEM quarterly filings and earnings releases (SEC EDGAR) | Quarterly |
| 2 | Hyperscaler data-centre capex guidance | Macro | Sets the OEM order flow behind the Rs 33 Cr and RFQ pipeline. SHARED with row 1 | Hyperscaler 10-Q and earnings calls; Dell'Oro | Quarterly |
| 3 | Construction, mining and heavy machinery OEM order books and R&D spend | End-customer | Industrial and heavy machinery is 65% of revenue; the Rs 44 Cr renewal is from this class (Inv. Pres. p.14) | OEM quarterly filings (SEC EDGAR); industry association data | Quarterly |
| 4 | Peer ER&D services quarterly revenue and deal wins (LTTS, Tata Technologies, Cyient, KPIT, Tata Elxsi) | Counterparty | Peers sell to the same OEM budgets; they show sector demand before Onward reports | BSE/NSE filings and concall transcripts | Quarterly |
| 5 | US PERM and onsite work rules | Regulatory | Management says guidance is "post the new regulatory environment"; onsite share is 31% (Inv. Pres. p.11) | USCIS and Department of Labor notices, Federal Register | Event-driven |
| 6 | USD/INR | Macro | Reported growth 22.4% vs constant currency 17.7% in Q2 FY27; revenue is dollar-linked | RBI reference rate | Monthly |
| 7 | Nasscom/Everest ER&D market releases | Macro | Sets the TAM growth input (8.6%) | Nasscom Strategic Review; Everest Group ER&D reports | Event-driven |
Shared dependencies: rows 1 and 2 are one correlated catalyst (hyperscaler build-out); FTTCP counts them once. Rows 3 and 6 are not shared.

---
## SEARCHES

Performed: Nasscom-Everest ER&D market; Nasscom Strategic Review 2026; Zinnov/IBEF India ER&D; KPIT and Tata Elxsi FY26 revenue; Quest Global revenue; USD/INR; data-centre capex and cooling; ER&D vertical split (two searches); BCG-Nasscom page fetch (autocarpro.in, opened).
Skipped or blocked: yourstory.com and letsdatascience.com fetches (HTTP 403, snippets used only); Everest Group 2026 ER&D report page (not opened); USD/INR for November 2026 (not found); global ER&D vertical split (NOT FOUND); global vendor revenues (Capgemini Engineering, Akkodis, Alten, Tech Mahindra: not searched); data-centre engineering services outsourcing market size (no result); Onward data-centre revenue share (NOT FOUND in the corpus).

```yaml
stage: B09-tam
company: "ONWARDTEC"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: partial
input_gaps:
  - "B07 not yet run: capex_embedded_growth_pct unavailable; 3C used heads x revenue per head instead"
  - "Vertical split of global outsourced ER&D NOT FOUND: SAM filter percentages are analyst assumptions with ranges, SAM level confidence LOW"
  - "Names of Onward's customers NOT FOUND (18.3% customer, construction and mining leader, power-management leader): downstream candidates are entity classes"
  - "Data-centre share of Onward revenue and sizing of the data-centre lever NOT FOUND"
  - "Global vendor revenues, competitor count, top-3 concentration and unorganised share NOT FOUND"
flags:
  - "FLAG-SAM-ASSUMED: all four SAM filters are unsourced assumptions; low-to-high SAM spans Rs 63,760 to 2,06,570 Cr (3.2x); SOM does not depend on the level"
  - "FLAG-MGMT-22PCT: deck's ~22% India engineering offshoring CAGR is unsourced; matches BCG-Nasscom 22% share by FY30 (inference); Nasscom path implies about 12.2%"
  - "FLAG-FX: Rs 94.68 per USD from a 22 Jun 2026 close seen in a search snippet; no November 2026 rate found"
  - "FLAG-FY27-TWO-READINGS: guide 15-18% (Rs 625-642 Cr) vs flat Q2 run rate Rs 660 Cr (+21.4%); separator is Q3 FY27 revenue vs Rs 170.18 Cr"
  - "FLAG-CONCENTRATION: 18.3% single customer, top 25 = 87%; the binding runway limit"
  - "FLAG-REVENUE-LABEL: deck p.15 Rs 550.9 cr is total income; revenue from operations is Rs 543.85 Cr"
market_definition: "Outsourced (third-party) ER&D and digital engineering services bought by North American and European OEMs in industrial, transportation and healthcare verticals"
tam_cr: {conservative: 771640, realistic: 910820}
sam_cr: 121936
sam_pct_of_tam: 13.4
som_3yr_cr: 856
som_5yr_cr: 1079
som_implied_revenue_cagr: {yr3: 16.3, yr5: 14.7}
current_sam_share_pct: 0.446
revenue_headroom_x: 224
tam_growth_pct: 8.6
runway_class: "STRONG"
mgmt_claim_cr: 23670000
mgmt_claim_ratio: 30.7
mgmt_claim_read: "inflated"
capacity_check: "sufficient: FY31 SOM needs about 4,621 heads at flat Rs 23.3 lakh per head (+1,704, about 400 a year) against 432 net hires in H1 FY27; constraint is utilisation and concentration, not capacity"
methods_used: ["top-down Nasscom-Everest vendor pool", "spend x outsourcing penetration", "peer revenue aggregation (floor)", "BCG-Nasscom sourcing (divergence, not used)"]
stale_data_flags:
  - {datapoint: "Global ER&D outsourcing $81.5 bn", source: "Nasscom-Everest ER&D Report 2025 via AR26 p.45", year: 2024}
  - {datapoint: "Global ER&D sourcing $210-280 bn; India share 17% to 22%", source: "BCG-Nasscom via autocarpro.in", year: 2023}
  - {datapoint: "Global ER&D spend $1.8 tn", source: "Nasscom via AR26 p.9", year: 2023}
searches_performed:
  - "Nasscom Everest ER&D report 2025 global ER&D outsourcing market"
  - "Nasscom Strategic Review 2026 India ER&D FY26"
  - "India engineering R&D services market size Zinnov"
  - "BCG-Nasscom ER&D sourcing page fetch (autocarpro.in, opened)"
  - "KPIT and Tata Elxsi FY26 revenue"
  - "Quest Global revenue FY26"
  - "USD INR exchange rate November 2026"
  - "data center capex power cooling OEM demand"
  - "global ER&D outsourcing by vertical (two searches)"
searches_skipped:
  - "yourstory.com Sept 2026 India ER&D article (HTTP 403)"
  - "letsdatascience.com Nasscom ER&D article (HTTP 403, snippet only)"
  - "Everest Group ER&D 2026 report page (not opened)"
  - "USD/INR for November 2026 (not found; 22 Jun 2026 rate used)"
  - "Global ER&D vertical split (NOT FOUND)"
  - "Global ER&D vendor revenues: Capgemini Engineering, Akkodis, Alten, Tech Mahindra (not searched)"
  - "Data-centre engineering services outsourcing market size (no result)"
downstream_candidates:
  - signal: "Order backlog of data-centre power and cooling OEMs"
    entity_type: "end-customer"
    demand_link: "Onward engineers for OEMs that equip and power data centres; Rs 33 Cr contract and RFQs"
    likely_source: "OEM quarterly filings, SEC EDGAR"
    cadence: "quarterly"
    shared: true
  - signal: "Hyperscaler data-centre capex guidance"
    entity_type: "macro"
    demand_link: "Drives OEM orders behind Onward's data-centre engineering pipeline"
    likely_source: "Hyperscaler 10-Q and earnings calls; Dell'Oro"
    cadence: "quarterly"
    shared: true
  - signal: "Construction, mining and heavy machinery OEM order books and R&D spend"
    entity_type: "end-customer"
    demand_link: "Industrial and heavy machinery is 65% of revenue; Rs 44 Cr renewal"
    likely_source: "OEM quarterly filings, SEC EDGAR"
    cadence: "quarterly"
    shared: false
  - signal: "Peer ER&D services quarterly revenue and deal wins"
    entity_type: "counterparty"
    demand_link: "Peers sell to the same OEM budgets and report before Onward"
    likely_source: "BSE/NSE filings and concall transcripts"
    cadence: "quarterly"
    shared: false
  - signal: "US PERM and onsite work rules"
    entity_type: "regulatory"
    demand_link: "Guidance is stated post new regulation; onsite is 31% of revenue"
    likely_source: "USCIS, Department of Labor, Federal Register"
    cadence: "event-driven"
    shared: false
  - signal: "USD/INR"
    entity_type: "macro"
    demand_link: "Reported growth exceeds constant currency by 4.7 pp in Q2 FY27"
    likely_source: "RBI reference rate"
    cadence: "monthly"
    shared: false
  - signal: "Nasscom/Everest ER&D market releases"
    entity_type: "macro"
    demand_link: "Sets the 8.6% TAM growth input"
    likely_source: "Nasscom Strategic Review; Everest Group ER&D reports"
    cadence: "event-driven"
    shared: false
demand_externally_verifiable: true
analyst_note: "SAM level is assumption-driven (vertical split NOT FOUND), so read headroom (224x) as 'large', not as a number. The handoff CAGR does not depend on SAM: it is the guide's top (18%) fading linearly to SAM growth 8.6% plus Onward's observed 2.8 pp FY26 excess (11.4%) by FY31. Two readings of FY27: guide Rs 625-642 Cr vs run-rate Rs 660 Cr; Q3 FY27 revenue vs Rs 170.18 Cr separates them. Mgmt claim ratio 30.7x compares total ER&D spend (in-house included) to the vendor pool; the vendor-pool claim itself is reasonable. Earnings-growth line: 16.1% EBITDA CAGR vs 19.0x trailing P/E."
```
