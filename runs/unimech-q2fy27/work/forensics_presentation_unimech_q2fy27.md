# A3 FORENSIC NOTES: UNIMECH q2fy27, doctype: presentation (Investor Presentation Q2 & H1 FY27, filed 27-Oct-2026)

Agent: A3 forensic notes | model: claude-opus-5-5 | run date 2026-10-28
Inputs read: A1 structured extraction (R001-R670, all rows), A1 fulltext (lines 1-782, all), A2 ledger (all sections incl. M1/M2), monitoring checklist extract, Notion snapshot lines 782-911 (Q1 FY27 sections, memory to weigh, not evidence). Source PDF and inputs/ not opened.
Units: Rs Mn on deck financial slides (Rs Mn / 10 = Rs Cr); order book slide in Rs Cr. "My arithmetic" marks every A3 computation. Notion-derived figures are labelled (Notion memory).

## 0. LEDGER RECONCILIATION
- Structured IDs R001-R670: 670 of 670 read at their cited fulltext line (100%). A2 ledger accounts for 670 of 670 (orphan_ids none) plus M1 (line 163) and M2 (line 560); both read.
- A1 row values spot-verified against the render transcriptions on pages 6, 7, 8, 20, 24, 25: no value error found. P&L arithmetic ties for all five period columns on page 8 (EBITDA + OI - D&A = EBIT; EBIT - finance = PBT; PBT - tax + associate = PAT, within 0.1 rounding) and Q1 + Q2 = H1 on every line. Balance sheet: Equity + NCL + CL = Total Assets for all four columns.
- A3-observed unrowed item (M3, not in A2's 2): page 7 line 175 "Advanced Negotiations", a label on the order-book slide next to the Key Highlights heading. Material to D-A3-04.
- Pipeline note: one Grep across extracted/ incidentally returned lines from the results-filing extract (a different document in this run). Those lines are not used as evidence anywhere below.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| D-A3-01 | F1 | R438-R441, R442-R445 (ZERO_STANDING R438-R440) | l.752-753, p25 | "Goodwill: --- \| --- \| --- \| 3,219.9" | FORWARD-SIGNAL | The goodwill line, nil for three years, now carries Rs 322.0 Cr: 29.8% of total assets (10,795.8) and 40.3% of total equity (7,981.6). Intangibles rose 18.7 to 492.2. Goodwill plus intangibles added Rs 369.3 Cr (my arithmetic), so the Hobel price cannot be the Rs 148 Cr reading (Notion memory); the deck BS supports the Rs 450 Cr scale. The FY27-end impairment test runs on Hobel cash flows, and the deck gives no Hobel revenue or EBITDA (trigger c). PPA provisional or final: NOT FOUND. |
| D-A3-02 | F1 | R063, R064, R525, R603 | l.197 (l.163), p7; l.378-380, p14 | "Oil and Gas --/4" | AMBIGUOUS | Zero proven Oil & Gas FAIs, 4 in pipeline. The Saudi JV targets "Upstream & downstream / oil & gas" (l.378-379). The JV's Unimech-side capability is not yet qualified in its target industry. Ask: which O&G customers, which qualification timeline before the ~Mar/Apr-2027 production start (Notion memory). |
| D-A3-03 | F16 | R041-R043, R005, R048-R050, R656, R658 | l.153-155, l.192, p7; l.89-90, p5 | "Total Order Book as on 30th Sept’ 26 : ~Rs. 855 Cr" / "(Including Rs. 266 Cr (Confirmed PO’s) + LTA & Award Letter ~Rs. 589 Cr )" | AMBIGUOUS | Order-book definition widened. Q1 book was Rs 280.3 Cr (Notion memory). Confirmed POs now Rs 266 Cr: down Rs 14.3 Cr, -5.1% QoQ. Implied Q2 confirmed inflow ~Rs 108.7 Cr against Q2 revenue Rs 123.0 Cr: book-to-bill ~0.88 (my arithmetic; assumes Q1 280.3 was a confirmed-PO basis). The MD letter cites "consolidated order book of / Rs.8,546 Mn" with no split, so 69% of the headline is non-PO. The 153% YoY on confirmed POs (l.192) has Hobel (acquired Apr-2026) in Sep-26 and not in Sep-25: inorganic. Lean bear: headline visibility rose, binding visibility did not. |
| D-A3-04 | F7 | R043, R045, R047, M3 | l.175-176, l.178, l.188, p7 | "Advanced Negotiations" / "Award Letters & Long Term Supply Agreements" | AMBIGUOUS | The ~Rs 589 Cr LTA/award pool equals the two valued instruments (FACC USD 7.5M + Tier-1 USD 43M = USD 50.5M) only at Rs ~116.6 per USD (my arithmetic). At any lower rate the pool holds something else: the Honeywell LTA (no value disclosed anywhere) or items under the "Advanced Negotiations" label. On a ~Rs 855 Cr base, Aerospace 71% of PCA (91%) is ~Rs 552 Cr, below the Rs 589 Cr pool (my arithmetic), so the pool is not all aerospace or the mix chart sits on another base. Ask for the itemised pool and whether anything under negotiation is counted. |
| D-A3-05 | F16 | R051-R056, R528 | l.195 (l.171-185), p7 | "Industrials (Hobel) 7%" | AMBIGUOUS | Hobel was ~36% of the Q1 book (Rs 100.1 Cr, Notion memory). Now 7% of the PCA mix: ~Rs 54.5 Cr on the ~855 base or ~Rs 16.9 Cr on the 266 base (my arithmetic). Nuclear 11% of PCA = ~Rs 85.6 Cr on the 855 base, which fits the ~Rs 87 Cr nuclear order, so the 855 base is the likelier one. Either reading: the Hobel book roughly halved in one quarter. Hobel is short-cycle (schedules, not backlog) so this may be definitional. Ask: Hobel order book at 30-Sep, like-for-like with Q1. |
| D-A3-06 | F6 | R010, R011, R044, R067, R068, R246, R592, R594 | l.124-127, p6; l.169, p7; l.521, p19 | "596 parts expected for qualification by end FY27" | FORWARD-SIGNAL | 596 = 250 done + 346 to come. 250 FAIs were executed over "FY26 – Till Date" (~18 months, ~14 per month). 346 by FY27-end (~6 months) needs ~58 per month, a ~4.2x pace step-up (my arithmetic). Aerospace is 322 of the 346. First numeric FAI target on record (Q1 call evaded the FAI target, Notion memory). Score at Q4 FY27: count qualified vs 596. "by year end" (l.126-127) vs "end FY27" (l.169): confirm which year end. |
| D-A3-07 | F6 | R009, R047, R521, R529 | l.116, p6; l.186-188, p7 | "~USD43mn award letter from French Tier-1 aerospace co." | AMBIGUOUS | New on the record: the Notion Key Notes carry the Honeywell and FACC LTAs, not this award (memory). USD 43M is large against FY26 revenue of Rs 240.5 Cr. Counterparty unnamed; tenor, start date and volume missing; an award letter is not a PO. A4: check for a Reg 30 disclosure and its date (trigger (d) is a disclosure-discipline trigger). |
| D-A3-08 | F6 | R588, R589, R591, R615, R616, R426-R437 | l.101-102, p5; l.119-121, p6; l.749-751, p25 | "Building scale-ready infrastructure ahead of demand is fundamental to our growth philosophy." | AMBIGUOUS | PPE + ROU + CWIP went 1,996.1 to 2,147.8 Mn in H1: +Rs 15.2 Cr, and that includes Hobel's acquired assets (my arithmetic). The Q1 call promised gross block ~2x by FY27-end (Notion memory), so capex is back-ended into H2 or the promise slips. Capex figure, IPO capex-object utilisation and Hobel PPE at acquisition: NOT FOUND (no cash flow statement in deck). Utilisation ~65% (l.576) leaves headroom, which weakens the "ahead of demand" urgency. |
| D-A3-09 | F8 | R157-R164, R310-R313, R382-R385, R454-R457 | l.241, p8; l.682, p24; l.737, l.756, p25 | "Tax Expense: 123.8 \| 49.0 \| 153% \| 86.9 \| 42% \| 210.7 \| 99.4 \| 112%" | FORWARD-SIGNAL | ETR: Q2 FY27 27.6%, Q1 23.7%, H1 25.8%, H1 FY26 22.1%, FY26 20.8%, FY25 18.0%, FY24 24.0% (my arithmetic) vs statutory 25.17%. The FY26 shield (~436 bps, ~Rs 3.5 Cr) is gone; Q2 sits 240 bps above statutory. Tax grew 42% QoQ on PBT +22%. Net DTA rose 2.3 to 35.5 Mn while DTL stays nil, although intangibles rose Rs 47.4 Cr (an expected DTL of ~Rs 11.9 Cr at 25.17%, my arithmetic). Ask: PPA deferred-tax treatment; ETR guide for H2. FY24 and FY25 tax are both 183.7 (l.682): verify against the ARs. |
| D-A3-10 | F10 | R358-R361 | l.731, p25 | "Equity Share Capital: 220.0 \| 254.3 \| 254.3 \| 254.5" | NEUTRAL-FACT | Paid-up capital +0.2 Mn in H1 (about 40,000 shares if FV is Rs 5; FV not in deck) with no corporate action stated. The deck shows no EPS, so the basic vs diluted spread cannot be measured. Open dilution vectors on file: Rs 750 Cr QIP, Hobel CCDs, ESOPs (Notion memory). A4 to cross-check. |
| D-A3-11 | F11 | R358-R369, R244, R402-R405, R410-R413 | l.731-733, l.742, l.744, p25; l.516, p19 | "Total Equity: 1085.9 \| 6,689.1 \| 7,373.9 \| 7,981.6" | AMBIGUOUS | Tie-out passes: 254.5 + 7,727.1 = 7,981.6 (all four columns tie). Other Equity +607.5 vs H1 PAT 596.4: residual +11.1 (candidates: ESOP premium, OCI, FCTR). No NCI line, though the Q1 record shows the first NCI (Notion memory) and the deck says "Acquired ~100% stake in Hobel Bellows" (l.516). Candidate reconciling items: NCI netted inside Other Equity; Hobel CCDs (equity or liability, location not shown); the 10% Hobel holdback (Notion memory) possibly in Other Financial Liabilities (+280.0 Mn) or Current Provisions (+112.7 Mn). No third-party net worth figure in the deck to tie. |
| D-A3-12 | F11 | R475-R477, R482-R489, R370-R373, R390-R393, R117-R124 | l.761, l.763-764, l.734, l.739, p25; l.236, p8 | "Current Financial Assets - Investments: --- \| 3,385.8 \| 4,684.1 \| 1,808.5" | FORWARD-SIGNAL | Liquid assets (cash + other bank + current investments) 5,918.0 to 2,264.4 Mn; borrowings 1,120.9 to 1,609.9 Mn; net cash Rs 479.7 Cr to Rs 65.5 Cr, down Rs 414.3 Cr, about the Hobel cash price (my arithmetic). Q2 other income was 69.8 Mn, -5% QoQ, not "~half again" as the Q1 call guided (Notion memory). On period-end liquidity that is ~12.3% annualised, too high for treasury yield, so OI likely carries non-treasury items (FX on 90-95% export receivables?); Q1-end balance NOT FOUND in deck. Short-term borrowing +Rs 46.1 Cr while Rs 180.9 Cr sits in current investments: carry-cost question. The treasury cushion under PAT is mostly gone. |
| D-A3-13 | F11 | R470-R473, R478-R481, R398-R401 | l.760, l.762, l.741, p25 | "Trade Receivables: 468.4 \| 549.8 \| 648.0 \| 1,226.0" | NEUTRAL-FACT | Receivables +89% in rupees (part acquired with Hobel), but days are flat: ~97 on annualised H1 revenue vs ~98 FY26, ~83 FY25; ~91 on Q2 annualised. Net trade WC ~107 days vs ~108 FY26 (my arithmetic). Below the Q1 call's "160+ days" guide (Notion memory); inside the green <150 line. |
| D-A3-14 | F14 | R322-R325, R270-R273, R181-R185 | l.685, l.672, p24 | "Materials %: 21.0% \| 21.8% \| 24.5% \| 32.8%" | AMBIGUOUS | The FY24-FY26 Materials % does not reconcile to the deck's own rupee line: computed 33.8%, 30.6%, 30.3% (my arithmetic). All other ratio rows reconcile, and the cost-share rows sum to 87.1% / 91.2% / 94.2% / 100.0%. History is on a narrower basis (likely materials without conversion). Like-for-like, materials went 30.3% (FY26) to 32.8% (H1 FY27), +250 bps, not the +830 bps the slide implies. The page 8 quarterly ratios reconcile (Q2 30.6%, Q1 35.3%). The gross-margin tracking basis must be fixed before any trend is scored. |
| D-A3-15 | F14 | R346-R353 | l.691-692, p24 | "ROE (%): 53.3% \| 33.1% \| 16.0% \| 14.9%" | AMBIGUOUS | Basis unstated. H1 FY27 ties: ROCE 14.9% = (EBITDA - D&A) x2 / (equity + borrowings) = 14.86%; ROE 14.9% = annualised PAT / closing equity = 14.94%. FY24 ROCE ties on the same basis (54.4%). FY25-FY26 do not: ROE by PAT / closing equity is 12.5% and 8.6%, not 33.1% and 16.0%; FY26 ROCE is 5.8% (ex-OI) or 11.3% (incl. OI), not 9.6% (my arithmetic). The FY26 9.6% to H1 14.9% "recovery" mixes bases. The Q1 call's ROCE path (~14.3% to 20-21%, Notion memory) needs one stated definition. |
| D-A3-16 | F14 | R516, R570, R643, R649, R555, R012, R249 | l.90, l.584; l.486, l.511; l.465; l.132, l.531 | "Co-Founder, CEO & Chairman" vs "Chairman & Managing Director" | NEUTRAL-FACT | Drafting bundle: Anil Kumar P titled CMD (l.90) and CEO & Chairman (l.584); "Founded 2016" (l.484-486) vs "Incorporated in 2014" (l.511); "Hobell Bellow’s" (l.465); the JV first tranche is "~USD 4mn" (l.132, Unimech share) and "the SAR 30 Mn / first equity tranche" (l.531-532, both partners). The Q2 scoreboard lists the JV tranche (paid 01-Oct per Notion memory) and the Honeywell LTA (filed 26-Oct) without labelling them post-period. Each is small; together they are a governance data point. |
| D-A3-17 | F15 | R513, R520, R527, R531, R543-R545 | l.115, p6; l.182, p7; l.142, p6 | "Secured a 10-year LTA with Honeywell Aerospace and" | AMBIGUOUS | The deck names Hobel, the Kanoo-Unimech JV and Dheya. It never names Innomech (the WOS that signed the Honeywell LTA and held all Rs 112.09 Cr FY26 borrowings, Notion memory; deck FY26 borrowings 274.8 + 846.1 = 1,120.9 Mn ties) or Uniflux Renewable Energy (WOS incorporated 27-Apr-2026, Notion memory). The Honeywell LTA is attributed to "Unimech". The US-tariff exposure that hit Innomech in FY26 is not visible in the deck. No prior deck entity list to diff (A2: DROPPED_SLIDE not assessable). |
| D-A3-18 | F15 | R216, R222-R226, R247-R249, R544, R664 | l.309, p12; l.373-374, l.396, p14 | "51:49 JV for establishing an advanced" | FORWARD-SIGNAL | The deck labels Kanoo-Unimech a JV. At 51% it is a subsidiary from 01-Oct (Notion memory): a relationship change. From Q3 FY27 the group consolidates a pre-revenue Dammam greenfield, with start-up costs in consolidated EBITDA and a 49% NCI. Production date (Mar/Apr-2027, Notion memory) and second-tranche date are not in the deck. "Joint Investment in JV : ~USD 30 Mn" (l.369) vs SAR 60 Mn planned equity (Notion memory): the funding gap is not explained. |
| D-A3-19 | F15 | R165-R172, R314-R317, R530, R545 | l.242, p8; l.683, p24 | "Share of profit/(loss) of associate entity: -7.5 \| -1.1 \| NA \| -1.4 \| -NA \| -8.9 \| -1.5 \| NA" | FORWARD-SIGNAL | Associate loss (Dheya, related party, 35.07% after the 7-Sep purchase, Notion memory) is -7.5 Mn in Q2 vs -1.4 in Q1 (5.4x). The H1 -8.9 already exceeds the FY26 full year (-4.1). The NA growth cells hide the step. Non-current investments 111.5 + 30.0 purchase - 8.9 loss = 132.6, which ties to 132.5 (my arithmetic). The losses scale with the stake, and a Dheya USD 10M raise is pending (Notion memory). |
| D-A3-20 | F16 | R196-R200, R334-R337 | l.247, p8 | "EBDIT%: 39.8% \| 29.9% \| - \| 36.5% \| - \| 38.3% \| 30.7% \| -" | AMBIGUOUS | The deck carries no FY27 guidance. The Q1 call guided 34-35% (floor 30-32%) (Notion memory). With H1 at 38.3%, keeping the guide at flat H2 revenue needs an H2 margin of ~29.7-31.7% (my arithmetic). Two readings: the guide is a sandbag, or H2 compression is embedded (semis step-up, PCA mix, Saudi start-up costs from Q3). Ask management to restate or upgrade the guide. |
| D-A3-21 | F16 | R252-R255, R235, R236, R250, R567 | l.576, l.556, p20; l.532, p19; l.337, p13 | "Footprint: 5 Manufacturing Facilities + 1 FTW \| 5.6 Lakh Sq. Ft. Manufacturing Footprint \| 155+ CNC Machines \| 3-axis to 5-axis CNC Capability \| ~65% Capacity Utilization" | AMBIGUOUS | The facility list includes "(Saudi JV)" (l.556), a greenfield with no production before ~Mar/Apr-2027 (Notion memory). Unimech 2.4 lakh (l.532) + Hobel 2.0 lakh (l.337) = 4.4 lakh, so ~1.2 lakh sq ft of the 5.6 lakh is unexplained (my arithmetic). The ~65% utilisation has no stated denominator (machine hours? 6.9 lakh hours H1, l.442). Against the ~58% Q1 call figure (Notion memory) it is up. It sits below the >70% mid-FY27 green line and above the <60% red line: AMBER. |
| D-A3-22 | F7 | R586, R591, R616 | l.121, p6; l.457, p16; l.97, p5 | "Progressively pursue NADCAP approvals" | AMBIGUOUS | The same deck holds two registers: "NADCAP certification targeted by FY27-end" (l.121) and the undated "Progressively pursue NADCAP approvals" (l.457). The semis step-up is "anticipated" (l.97), not committed. Score NADCAP at Q4 FY27 against the dated version; ask which one is the commitment. |
| D-A3-23 | F17 | R523, R524 (no CRISIL row exists) | l.135-139, p6 | "Credit Rating Validation" / "'CARE A; Stable’ rating by CARE, underscoring strong" | CONFIRMATORY-NEGATIVE | CRISIL "Issuer Not Cooperating" (master variable) is absent again. The deck builds a "Credit Rating Validation" item from CARE and D&B instead. This is at least the third consecutive quarterly deck of silence (Q4 FY26, Q1 FY27, Q2 FY27 per Notion memory), within a 7+ document running count. Persistence leg of trigger (d) stays confirmed. |
| D-A3-24 | F17 | R531, R655, R662 | l.142, p6; l.228/l.250, p8 | "*Hobel consolidation wef from 1st May 2026" | AMBIGUOUS | Hobel is a footnote only: no Hobel revenue, EBITDA or organic ex-Hobel split, in the second consecutive deck (Q1 deck also silent, Notion memory; two call refusals on segment margin). Trigger (c) Hobel EBITDA <40% stays untestable for another quarter, while Hobel's order-book share fell (D-A3-05). Q2 revenue +98% and confirmed POs +153% both include Hobel inorganically. |
| D-A3-25 | F17 | R239 | l.488-490, p18 | "Customers" / "41" | AMBIGUOUS | Customer count (41) and countries (8) are given; no top-1 or top-3 share. File: top-1 44.5%, top-3 72.4% (FY26 AR), Hobel two OEM groups 93% (Notion memory). Prior-deck count of silence NOT FOUND in memory; at least 1. Ask for top-1/top-5 share on the consolidated base after Hobel. |
| D-A3-26 | F17 | R611 | l.433-434, p15 | "Strong revenue, attractive margins and robust cash" / "conversion" | AMBIGUOUS | "robust cash conversion" is claimed with no cash flow statement in the deck. The pre-set cash upgrade test (H1 CFO/PAT >0.90x moves Pillar 2, Notion memory) cannot be run from the deck: CFO NOT FOUND. Hand to the results-filing A3 / A4 for the H1 cash flow. |
| D-A3-27 | F17 | R008, R046, R520, R527 | l.115, p6; l.182, p7 | "Honeywell Aerospace: Signed a 10-year LTA for aero-engine" | AMBIGUOUS | The Notion separating observation for the Honeywell LTA is "a disclosed number ... on the 28-Oct call or in the Q2 deck". The deck gives tenor only: no value, PO, part count or FAI date. Deck leg NOT MET; the call is the remaining chance before the Q3 FY27 deadline. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 14 ZERO_STANDING rows read. Goodwill nil to Rs 322 Cr (D-A3-01); Oil & Gas FAI proved "--" vs Saudi O&G focus (D-A3-02). Others (FY24 leases, provisions, DTL, NC investments, current investments, income-tax assets; FY24 associate 0.0) reflect pre-IPO / pre-acquisition years: no anticipatory transaction class. |
| F2 Standalone vs consolidated | N.A. | Deck carries consolidated figures only; no standalone column to decompose. Standalone parent analysis belongs to the results-filing A3. |
| F3 Shell-entity detection | N.A. | No standalone cost lines in the deck. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph in a deck; deck notes "Un-audited Financial Results" (l.31) only. |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph in a deck. |
| F6 Forward-commitment phrases | FINDING | 16 commitments registered (section 3); FAI pace step-up (D-A3-06), unnamed USD 43M award (D-A3-07), capex back-ending (D-A3-08). |
| F7 Hedge phrases | FINDING | "Advanced Negotiations" on the order-book slide (D-A3-04); NADCAP dated vs "progressively pursue" (D-A3-22). Disclaimer "subject to known and unknown risks" (l.70) is boilerplate; no prior deck text to diff. |
| F8 Tax forensics | FINDING | ETR now above statutory; DTA/DTL pattern vs acquired intangibles; identical FY24/FY25 tax (D-A3-09). |
| F9 OCI forensics | N.A. | Deck shows no OCI line. |
| F10 Share count and dilution | FINDING | Paid-up +0.2 Mn with no stated action; no EPS shown (D-A3-10). |
| F11 Reserves and net worth tie-out | FINDING | Equity ties exactly; NCI absent and CCD / holdback location unclear (D-A3-11); net cash collapse and other-income composition (D-A3-12); receivable days flat (D-A3-13). |
| F12 Segment forensics | N.A. | Deck gives no segment revenue, results, assets or liabilities (only an order-book mix). The absence is logged under F17 (D-A3-24). |
| F13 Board outcome beyond results | N.A. | Deck carries no board outcome, AGM or appointment term dates; slide 22 lists five independent directors without terms. |
| F14 Drafting inconsistencies | FINDING | Materials % basis break (D-A3-14); ROE/ROCE basis break (D-A3-15); title, date, spelling and tranche-size inconsistencies (D-A3-16). |
| F15 Entity list diffs | FINDING | Innomech and Uniflux unnamed (D-A3-17); Kanoo JV to subsidiary from 01-Oct (D-A3-18); Dheya associate loss step-up (D-A3-19). No prior deck list to diff; memory used. |
| F16 Dropped / reframed disclosures | FINDING | Order-book definition widened (D-A3-03); Hobel book share (D-A3-05); no restated margin guide (D-A3-20); footprint includes pre-commissioning Saudi site (D-A3-21). |
| F17 Silence audit | FINDING | Run against the deck at coordinator direction (doctype rule would mark it N.A. on a presentation). 18 silence rows (section 4); key: CRISIL (D-A3-23), Hobel split (D-A3-24), concentration (D-A3-25), cash flow (D-A3-26), Honeywell value (D-A3-27). |

Counts: PASS 0 | FINDING 10 | N.A. 7 | blank 0.

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | slide / line | status word |
|---|---|---|---|---|
| C1 | Semiconductor revenue "sharp step-up anticipated in H2" | H2 FY27 (by 31-Mar-2027) | p5 l.96-97 | initiated (anticipated) |
| C2 | Serial production scaling "over coming quarters" | undated | p5 l.98-99 | initiated |
| C3 | Automated special-process cell installation | undated (tied to C4) | p5 l.102; p6 l.119; p16 l.456 | underway |
| C4 | NADCAP certification | FY27-end (31-Mar-2027) | p6 l.121; p16 l.457 | initiated (targeted) |
| C5 | 346 more FAIs qualified; 596 parts total | end FY27 | p6 l.124-127; p7 l.169 | underway |
| C6 | Kanoo-Unimech JV first equity tranche (SAR 15.3 Mn Unimech, SAR 14.7 Mn YBAK) | done (paid 01-Oct per Notion) | p6 l.130-132; p14 l.396; p19 l.529-532 | completed |
| C7 | Establish Saudi manufacturing facility (Dammam; O&G and utility) | undated in deck (Notion: production Mar/Apr-2027) | p6 l.132-133; p16 l.452-454 | initiated (advancing plans) |
| C8 | Honeywell Aerospace 10-year LTA, aero-engine and control systems | signed; value undisclosed | p6 l.115; p7 l.182 | completed |
| C9 | ~USD 43M award letter, unnamed French aerospace Tier-1, aerostructures | received; execution undated | p6 l.116; p7 l.186-188 | completed (award, not PO) |
| C10 | FACC LTA USD 7.5M, aerostructure components | signed | p7 l.178 | completed |
| C11 | Strategic LTAs in pipeline with aerospace and semiconductor Tier-1s / OEMs | undated | p19 l.527-528 | initiated |
| C12 | Items under "Advanced Negotiations" (order-book slide) | undated | p7 l.175 | initiated |
| C13 | Hobel products cross-sold to other customers | undated | p16 l.465-466 | underway |
| C14 | Portfolio expansion: micro gas turbines, GSE, air cargo handling, industrial products | undated | p16 l.452-457 | initiated |
| C15 | Inorganic growth via JVs and acquisitions | undated | p16 l.452, l.458; p19 l.507 | initiated |
| C16 | Earnings presentation to analysts/investors | 28-Oct-2026 call (Notion) | p1 l.32 | scheduled |

Status transitions vs the Q1 FY27 call baseline (Notion memory, not a prior extract):
- Engine Tier-1 LTA "advanced stage" to Honeywell LTA secured (C8): completed; size untested.
- Saudi JV "USD 10M infusion in Aug-2026" to ~USD 4M Unimech share (SAR 30 Mn JV-level), paid ~01-Oct: completed, late and smaller.
- FAI target (evaded on the Q1 call) to 596 by FY27-end: new dated commitment.
- FY27 EBITDA 34-35%: H1 38.3%, running ahead (D-A3-20).
- Other income "to ~half again": Q2 69.8 vs Q1 73.3 Mn, not delivered (D-A3-12).
- WC "160+ days": deck BS implies ~107 days net trade WC, better than guided (D-A3-13).
- Utilisation ~58%: now ~65% (D-A3-21).
- ROCE ~14.3% annualised: H1 14.9% (basis caveat D-A3-15).
- Gross block ~2x by FY27-end: H1 shows +Rs 15.2 Cr in PPE + ROU + CWIP (D-A3-08).
- Hobel AS9100 by Q4 FY27, two new Hobel customers, Dheya USD 10M raise, nuclear ~50% executed in H2: not stated in deck (section 4).

## 4. WHAT WAS NOT DISCUSSED (F17, deck silence audit vs Notion monitoring checklist and coordinator watch items)

| # | checklist / commitment item | deck treatment | consecutive quarters silent (decks) | note |
|---|---|---|---|---|
| S1 | CRISIL "Issuer Not Cooperating" (threshold 6, master variable) | absent; CARE/D&B shown instead (l.135-139) | >=3 (Q4 FY26, Q1, Q2) | D-A3-23; confirmatory negative |
| S2 | Hobel EBITDA margin (threshold 3, trigger c) | absent; footnote only (l.142) | 2 (Q1, Q2) plus 2 call refusals | D-A3-24 |
| S3 | Organic ex-Hobel revenue split | absent | 2 (Q1, Q2) | headline +98% / +85% part inorganic |
| S4 | CFO/PAT (threshold 7) and cash flow statement | absent; "robust cash conversion" claim (l.433-434) | >=1 | D-A3-26; NOT FOUND in deck |
| S5 | Customer concentration (top-1 / top-3) | absent; 41 customers (l.490) | >=1 (prior decks NOT FOUND in memory) | D-A3-25 |
| S6 | Gross-margin bridge (Q1 follow-up) | absent; Materials % only; Q2 30.6% vs Q1 35.3% unexplained (l.244) | 2 | basis break D-A3-14 |
| S7 | FY27 numeric guidance (revenue, margin) | absent | 2 (Q1 deck zero numeric guidance) | D-A3-20 |
| S8 | IPO proceeds utilisation / capex object | absent | >=1 | D-A3-08 |
| S9 | Rs 750 Cr QIP (structure, timing, dilution) | absent | >=1 | MPS-driven raise due ~Feb-2028 (Notion) |
| S10 | Honeywell LTA value / first PO / FAI date | absent (tenor only) | 1 (first deck after signing) | D-A3-27 |
| S11 | Saudi JV second tranche date; production start | absent ("advancing plans", l.132-133) | 1 | tracker rows on file |
| S12 | Hobel AS9100 (Weissac) by Q4 FY27 | absent | 1 | Q1 call promise |
| S13 | Two new Hobel customers by FY27-end | partial: "being cross sold" (l.465), no count | 1 | |
| S14 | Dheya USD 10M raise and Unimech participation | absent; associate loss up (l.242) | 1 | D-A3-19 |
| S15 | Promoter pledge (Preetham S V, 29-Sep-2026) | absent; listed as Co-Founder (l.583-589) | 1 | first deck since pledge |
| S16 | Hobel consideration reconciliation (Rs 450 vs Rs 148 Cr) | restates "₹450 crore all-cash" (l.309), no reconciliation | 2 | BS goodwill supports ~Rs 450 Cr scale (D-A3-01) |
| S17 | Innomech and Uniflux (entities, plans) | unnamed | >=1 | D-A3-17 |
| S18 | Cummins QSK95 / data-centre pull; Force MTU; AMCA engine | absent | >=2 (Q4 FY26 deck silent on Cummins, Notion) | low priority |

Addressed in the deck (with numbers): consolidated revenue (threshold 1: H1 Rs 230.6 Cr; trigger (a) needs H2 >= Rs 169.4 Cr against a Q2 run-rate of ~Rs 246 Cr per half, my arithmetic: not fired); blended EBITDA (threshold 2: Q2 39.8%, H1 38.3%, green); capacity utilisation (threshold 4: ~65%, amber); WC (threshold 5: no days metric, derivable ~107 days, green); export share (order book 90% exports l.196; company ~95% l.494); order book (D-A3-03); gross margin (materials 30.6% Q2); subsidiary consolidation (Hobel footnote; Kanoo JV slide; Dheya slide).

## 5. KEY WORKINGS (all my arithmetic from deck lines; Rs Mn unless stated)
- Core PBT ex-OI: Q2 FY27 379.3 vs Q2 FY26 108.1. OI share of PBT: Q2 15.5%, Q1 20.0%, Q2 FY26 47.7%, FY26 58.4%. Earnings quality improved as treasury fades.
- Gross margin (1 - Material & Conversion %): Q2 FY27 69.4%, Q1 64.7%, Q2 FY26 67.8%, H1 67.2%, FY26 like-for-like 69.7%.
- Trigger (a): 4,000 - 2,306.2 = 1,693.8 needed in H2; Q2 x2 = 2,460.
- Net cash: FY26 5,918.0 - 1,120.9 = 4,797.1; H1 FY27 2,264.4 - 1,609.9 = 654.5 (leases excluded).
- Goodwill + intangibles added: 3,219.9 + (492.2 - 18.7) = 3,693.4.

## 6. FLAGS FOR A4 (management questions)
Forward signals: D-A3-01, 06, 09, 12, 18, 19. Ambiguous: D-A3-02, 03, 04, 05, 07, 08, 11, 14, 15, 17, 20, 21, 22, 24, 25, 26, 27. Confirmatory negative: D-A3-23. Neutral facts: D-A3-10, 13, 16.
Top three for the call: (1) itemise the Rs 589 Cr LTA/award pool and confirm the confirmed-PO book like-for-like vs Q1 Rs 280.3 Cr; (2) Hobel revenue, EBITDA and order book at 30-Sep; (3) other-income composition and the H2 ETR, with net cash now Rs 65.5 Cr.

```yaml
stage: A3-forensics
company: "UNIMECH"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-unimech-q2fy27-1b1895/runs/unimech-q2fy27/work/forensics_presentation_unimech_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "D-A3-01", check: "F1", line: "752-753", classification: "FORWARD-SIGNAL", implication: "Goodwill nil to Rs 322.0 Cr (29.8% of assets, 40.3% of equity); FY27-end impairment test rests on undisclosed Hobel EBITDA; goodwill+intangibles Rs 369 Cr rules out Rs 148 Cr price reading"}
  - {id: "D-A3-02", check: "F1", line: "197", classification: "AMBIGUOUS", implication: "Zero proven Oil & Gas FAIs (4 in pipeline) while the Saudi JV targets oil & gas"}
  - {id: "D-A3-03", check: "F16", line: "153-155; 192; 89-90", classification: "AMBIGUOUS", implication: "Headline book ~Rs 855 Cr is 69% LTA/award letters; confirmed POs Rs 266 Cr vs Q1 Rs 280.3 Cr = -5.1% QoQ, book-to-bill ~0.88; 153% YoY includes Hobel"}
  - {id: "D-A3-04", check: "F7", line: "175-176; 178; 188", classification: "AMBIGUOUS", implication: "Rs 589 Cr pool exceeds the two valued instruments unless Rs ~116.6/USD; residual is Honeywell (no value) or items under 'Advanced Negotiations'"}
  - {id: "D-A3-05", check: "F16", line: "195", classification: "AMBIGUOUS", implication: "Hobel 7% of PCA order mix (~Rs 54 Cr on 855 base) vs Rs 100.1 Cr at Q1; Hobel book roughly halved or redefined"}
  - {id: "D-A3-06", check: "F6", line: "124-127; 169; 521", classification: "FORWARD-SIGNAL", implication: "596 parts by FY27-end needs ~58 FAIs/month vs ~14/month history (~4.2x); first numeric FAI target; score at Q4 FY27"}
  - {id: "D-A3-07", check: "F6", line: "116; 186-188", classification: "AMBIGUOUS", implication: "Unnamed ~USD 43M Tier-1 award letter new to the record; check Reg 30 disclosure and date (trigger d relevance); award is not a PO"}
  - {id: "D-A3-08", check: "F6", line: "101-102; 119-121; 749-751", classification: "AMBIGUOUS", implication: "PPE+ROU+CWIP +Rs 15.2 Cr in H1 incl. Hobel; gross block ~2x by FY27-end promise is back-ended; capex and IPO utilisation NOT FOUND"}
  - {id: "D-A3-09", check: "F8", line: "241; 682; 737; 756", classification: "FORWARD-SIGNAL", implication: "ETR Q2 27.6% vs 25.17% statutory, FY26 20.8% shield gone; DTA up, DTL nil despite Rs 47 Cr intangibles; FY24=FY25 tax 183.7 to verify"}
  - {id: "D-A3-10", check: "F10", line: "731", classification: "NEUTRAL-FACT", implication: "Paid-up capital +0.2 Mn with no stated action; no EPS in deck; QIP, CCD, ESOP dilution vectors open"}
  - {id: "D-A3-11", check: "F11", line: "731-733; 742; 744; 516", classification: "AMBIGUOUS", implication: "Equity ties; no NCI line despite '~100% stake' and Q1 NCI; Hobel CCD and 10% holdback location unclear"}
  - {id: "D-A3-12", check: "F11", line: "734; 739; 761; 763-764; 236", classification: "FORWARD-SIGNAL", implication: "Net cash Rs 479.7 Cr to Rs 65.5 Cr; Q2 other income not halved as guided and implies ~12% yield on period-end liquidity; composition and treasury fade question"}
  - {id: "D-A3-13", check: "F11", line: "760; 762; 741", classification: "NEUTRAL-FACT", implication: "Receivable days ~97 vs ~98 FY26; net trade WC ~107 days, inside green line and better than 160+ guide"}
  - {id: "D-A3-14", check: "F14", line: "685; 672", classification: "AMBIGUOUS", implication: "FY24-FY26 Materials % (21.0/21.8/24.5) does not reconcile to rupee line (33.8/30.6/30.3); like-for-like gross margin move is +250 bps not +830 bps"}
  - {id: "D-A3-15", check: "F14", line: "691-692", classification: "AMBIGUOUS", implication: "ROCE/ROE basis unstated; H1 FY27 and FY24 tie, FY25-FY26 do not; FY26 9.6% to H1 14.9% trend mixes bases"}
  - {id: "D-A3-16", check: "F14", line: "90; 584; 486; 511; 465; 132; 531", classification: "NEUTRAL-FACT", implication: "Title, founding-year, spelling and tranche-size inconsistencies; post-period events in Q2 scoreboard unlabelled"}
  - {id: "D-A3-17", check: "F15", line: "115; 182; 142", classification: "AMBIGUOUS", implication: "Innomech (Honeywell LTA signatory, FY26 borrower) and Uniflux not named; US tariff exposure invisible in deck"}
  - {id: "D-A3-18", check: "F15", line: "309; 373-374; 396", classification: "FORWARD-SIGNAL", implication: "Kanoo JV is a 51% subsidiary from 01-Oct; Q3 consolidates a pre-revenue greenfield with start-up costs and 49% NCI"}
  - {id: "D-A3-19", check: "F15", line: "242; 683", classification: "FORWARD-SIGNAL", implication: "Related-party associate (Dheya) loss -7.5 Mn Q2 vs -1.4 Q1; H1 exceeds FY26 full year; NA cells hide the step"}
  - {id: "D-A3-20", check: "F16", line: "247", classification: "AMBIGUOUS", implication: "No guidance in deck; H1 EBITDA 38.3% vs 34-35% FY guide implies H2 ~30-32% or a sandbag"}
  - {id: "D-A3-21", check: "F16", line: "576; 556; 532; 337", classification: "AMBIGUOUS", implication: "Footprint and facility count include the pre-commissioning Saudi site; ~1.2 lakh sq ft unexplained; utilisation ~65% amber, denominator unstated"}
  - {id: "D-A3-22", check: "F7", line: "121; 457; 97", classification: "AMBIGUOUS", implication: "NADCAP dated FY27-end on one slide, 'progressively pursue' on another; semis step-up only 'anticipated'"}
  - {id: "D-A3-23", check: "F17", line: "135-139", classification: "CONFIRMATORY-NEGATIVE", implication: "CRISIL non-cooperation absent for >=3rd consecutive deck; CARE/D&B substituted; trigger (d) persistence leg stays confirmed"}
  - {id: "D-A3-24", check: "F17", line: "142; 228", classification: "AMBIGUOUS", implication: "No Hobel revenue/EBITDA or organic split, 2nd consecutive deck; trigger (c) untestable again"}
  - {id: "D-A3-25", check: "F17", line: "488-490", classification: "AMBIGUOUS", implication: "Customer concentration absent; only customer count 41"}
  - {id: "D-A3-26", check: "F17", line: "433-434", classification: "AMBIGUOUS", implication: "'robust cash conversion' claimed with no cash flow; H1 CFO/PAT upgrade test cannot run from deck"}
  - {id: "D-A3-27", check: "F17", line: "115; 182", classification: "AMBIGUOUS", implication: "Honeywell LTA carries no value, PO or FAI date in deck; Notion separating observation not met in deck leg"}
forward_signals: ["D-A3-01", "D-A3-06", "D-A3-09", "D-A3-12", "D-A3-18", "D-A3-19"]
ambiguous: ["D-A3-02", "D-A3-03", "D-A3-04", "D-A3-05", "D-A3-07", "D-A3-08", "D-A3-11", "D-A3-14", "D-A3-15", "D-A3-17", "D-A3-20", "D-A3-21", "D-A3-22", "D-A3-24", "D-A3-25", "D-A3-26", "D-A3-27"]
commitments:
  - {commitment: "Semiconductor revenue sharp step-up anticipated in H2", implied_date: "H2 FY27 (by 2027-03-31)", ref: "p5 l.96-97", status_word: "initiated"}
  - {commitment: "Serial production scaling over coming quarters", implied_date: "undated", ref: "p5 l.98-99", status_word: "initiated"}
  - {commitment: "Automated special-process cell installation", implied_date: "undated (tied to NADCAP FY27-end)", ref: "p5 l.102; p6 l.119; p16 l.456", status_word: "underway"}
  - {commitment: "NADCAP certification", implied_date: "FY27-end (2027-03-31)", ref: "p6 l.121; p16 l.457", status_word: "initiated"}
  - {commitment: "346 more FAIs qualified, 596 parts total", implied_date: "end FY27", ref: "p6 l.124-127; p7 l.169", status_word: "underway"}
  - {commitment: "Kanoo-Unimech JV first equity tranche SAR 30 Mn (Unimech SAR 15.3 Mn)", implied_date: "done (~2026-10-01 per Notion)", ref: "p6 l.130-132; p14 l.396; p19 l.529-532", status_word: "completed"}
  - {commitment: "Establish Saudi manufacturing facility, Dammam", implied_date: "undated in deck (Notion: Mar/Apr-2027)", ref: "p6 l.132-133; p16 l.452-454", status_word: "initiated"}
  - {commitment: "Honeywell Aerospace 10-year LTA", implied_date: "signed; value undisclosed", ref: "p6 l.115; p7 l.182", status_word: "completed"}
  - {commitment: "~USD 43M award letter, unnamed aerospace Tier-1", implied_date: "received; execution undated", ref: "p6 l.116; p7 l.186-188", status_word: "completed"}
  - {commitment: "FACC LTA USD 7.5M", implied_date: "signed", ref: "p7 l.178", status_word: "completed"}
  - {commitment: "Strategic LTAs in pipeline with aerospace and semiconductor Tier-1s/OEMs", implied_date: "undated", ref: "p19 l.527-528", status_word: "initiated"}
  - {commitment: "Items under Advanced Negotiations", implied_date: "undated", ref: "p7 l.175", status_word: "initiated"}
  - {commitment: "Hobel products cross-sold to other customers", implied_date: "undated", ref: "p16 l.465-466", status_word: "underway"}
  - {commitment: "Portfolio expansion: micro gas turbines, GSE, air cargo handling, industrial products", implied_date: "undated", ref: "p16 l.452-457", status_word: "initiated"}
  - {commitment: "Inorganic growth via JVs and acquisitions", implied_date: "undated", ref: "p16 l.452, l.458; p19 l.507", status_word: "initiated"}
  - {commitment: "Earnings presentation to analysts/investors", implied_date: "2026-10-28 call (Notion)", ref: "p1 l.32", status_word: "scheduled"}
gate_a3: pass
blank_checks: []
analyst_note: "The headline order book triples to ~Rs 855 Cr only by adding ~Rs 589 Cr of LTA and award letters. The like-for-like confirmed-PO book fell ~5% QoQ (Rs 280.3 Cr to Rs 266 Cr). Forward visibility now rests on non-binding instruments: Honeywell has no value, and the slide carries an 'Advanced Negotiations' label. That is the first question for A4. Second, the balance sheet shows the Hobel cost: goodwill Rs 322 Cr (30% of assets), net cash down Rs 414 Cr to Rs 65.5 Cr, short-term debt up, ETR above statutory. Treasury income cannot keep carrying PAT. Q2 other income did not halve as guided, and its implied yield looks too high, so its composition matters. Third, the deck's historical ratio rows are unreliable: FY24-FY26 Materials % and FY25-FY26 ROE do not reconcile to the deck's own rupee lines. Use computed ratios. The operating print is strong (EBITDA 39.8%, materials 30.6%, receivable days flat ~97). The margin question stays open both ways: H1 38.3% vs a 34-35% FY guide means a sandbag or H2 compression. CRISIL silence continues; the deck substitutes CARE and D&B."
```
