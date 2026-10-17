# A3 FORENSIC NOTES: KARNIKA concall H1 FY27 (doctype: concall)

Company: Karnika Industries Limited (KARNIKA). Period: Q2 / H1 FY27, ended 30-Sep-2026. Call: 13-Oct-2026. Transcript filed 16-Oct-2026 (L24).
Inputs read: A1 structured (R001-R246), A1 fulltext (L1-L1109, read in full), A2 ledger (246 IDs, 167 turns, 67 questions and 105 mgmt numbers after the A2 Loop 1 delta).
Not read: source PDF, inputs/. Prior-quarter fulltext: not available. Notion checklist: NONE (pre-thesis read, no spear on record, no companies/KARNIKA.md).
Model: claude-opus-5-5.
Correction loop: iteration 1 applied (section 6). New findings A3-18 and A3-19. No checklist status changed.

Derived figures in this report are arithmetic on figures the call states. Each one is labelled [derived] and shows its formula. Rounded inputs ("INR106 crores", "approx INR23 crores") carry rounding error of about +/-0.5 cr. Nothing here is estimated beyond that arithmetic.

## 0. LEDGER RECONCILIATION

| item | result |
|---|---|
| Structured IDs in ledger | 246 of 246 (R001-R246) |
| IDs read at cited fulltext line | 246 of 246 |
| Verbatim present at or within 3 lines of cite | 246 of 246 |
| Ledger turns cross-checked against fulltext speaker labels | 167 of 167 |
| Loop 1 units (q36 at T87/T88; M001-M005) read at cited fulltext line | 6 of 6 (L306, L704-705, L723-726, L867, L901, L1027) |
| ledger_reconciled_pct | 100 |

Line-cite drifts found while reading. The verbatim text exists, but the A1 line cite is off. None changes a finding.
- R035 "13%": at L227, cited L228.
- R072 context says "confirmed Yes line 576". The "Yes" is at L593 and the analyst's "Roughly 50 in total" is at L590. R245 is cited at L587, which is the FY27-28 timing answer.
- R073 "INR500 crores": at L601, cited L600.
- R092 "INR150 to INR500": at L807, cited L806.
- R099 "approx 55%": at L919, cited L918-919.
- R146 / R148 "Panda or Disney": at L546 (page 10), cited L540 (page 9).
- R236 "Maybe we might be wrong": at L565, cited L562 (turn start).

Paraphrase in "verbatim" fields. Several FORWARD rows are paraphrases, not verbatim. R189 is the one that matters. The transcript reads "trying to reduce it by 90 to 100 days" (L791-792). R189 normalises this to "reduce ... to 90 to 100 days". A3 judged every row on the fulltext wording.

A2 interpretive note corrected. The A2 analyst_note says the Kidcity H1 INR40 cr against an INR80-100 cr FY target "implies a steep H2 ramp". [derived] H2 needs INR40-60 cr. At the low end that equals H1 (0% step-up). At the high end it is +50%. Only the top of the range needs a steep ramp (see A3-14).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F2 | R051 R052 R053 R233 R057 R174; T26, T32 | L395-396; L425-426 | "INR140 crores is from the Karnika, INR40 crores is from Kidcity. Consolidation is around INR180 crores" / "60% of the goods what we are selling via Kidcity, these are the production will be held by the Karnika" | AMBIGUOUS | The parts add up exactly (140 + 40 = 180) with no intercompany elimination. Yet Karnika makes 60% of Kidcity's goods. Reading 1: the INR140 cr is already net of sales to Kidcity. Reading 2: intercompany revenue sits inside both parts, and organic standalone growth is overstated. The results filing's standalone vs consolidated revenue separates the two. Lean bear until seen. |
| A3-02 | F2 | R017-R026, R029-R037, R242, R243; T4 | L215-228 | "Although, we are strengthening our operational leverage, our PAT grew 51% to INR14 crores" (L221) vs "EBITDA has increased 38.1% ... margin moderated to 18.8% from 20.7%" (L216-217) | AMBIGUOUS | PAT grew faster than EBITDA while EBITDA margin fell 190 bps. Operating leverage would show above EBITDA, so the stated cause does not fit the numbers. The gain sits below EBITDA. [derived] EBITDA% minus PAT% fell from 7.2pp (20.7-13.5) to 5.4pp (18.8-13.4) in Q2, and from 6.8pp to 5.2pp in H1. At a constant 25.17% tax rate, D&A plus finance cost net of other income falls from about 2.7% to about 0.9% of revenue, with D/E at 0.6x (L181). Candidates: other income, a lower tax rate, a deferred-tax credit, lower minority interest. Check the results filing tax line (F8) and other income. |
| A3-03 | F2 | R017 R027 R028 R093 R119 R191; T4, T104 | L215, L223, L262, L821 | "Q2 FY27 revenue from operations grew by 52.3%" / "H1 FY27 revenue increased 74.7% to INR180 crores" / "Our second company, which is acquired by Karnika" | FORWARD-SIGNAL | [derived] H1 FY26 = 180/1.747 = 103.0; Q2 FY26 = 106/1.523 = 69.6; Q1 FY26 = 33.4; Q1 FY27 = 180-106 = 74. Q1 FY27 growth was about +121%, and Q2 slowed to +52.3%. The call never states when Kidcity was acquired or consolidated, or the stake. Reading 1: the H1 growth is mostly acquisition base effect, and growth will move toward the 30-35% guide once the base laps. Reading 2: the growth is organic. The organic or like-for-like growth figure separates them. Expect a further slowdown in Q3/Q4. |
| A3-04 | F6 | R194 R195 R196 R158 R230 R013; T144, T146, T3 | L981-983; L989-993; L117-118 | "If we required next round of fund for the expansion, we will go for preferential allotment or equity" / "for which I will require a healthy capital infusion" | FORWARD-SIGNAL | Management caps debt at the current level ("continue with this debt level", L981) and names equity as the funding route for Brands of Brand. Main board migration "effective 13th October 2026, subject to completion of the applicable regulatory and procedural requirements" (L117-118) opens a larger investor pool. A preferential issue or QIP is likely once the Brands of Brand plan is final. Size, price and timing are not given ("This will consider how the capital funding requirement arises", L989). Guidance is on PBT, not EPS (A3-09), so dilution falls outside the guided number. |
| A3-05 | F6 | R102 R104 R200 R201 R244 R080 R081 R188 R235 R182 R237 R079 R016 R165; T158, T160, T86, T53, T84 | L1065-1072; L719-720; L546-548; L697; L189-190 | "Around INR6 crores to INR8 crores will be your MG" / "targeting for INR50 lakhs per year. If we are achieving that, we will be margin of around 13% to 14%" / "They will not be profitable businesses for me" | FORWARD-SIGNAL | [derived] 50 stores x INR50 lakh = INR25 cr a year. A licence minimum guarantee (MG) of INR6-8 cr is 24-32% of that revenue, and it is a fixed cost that comes before sales. Airport rent runs "4x to 6x plus" (L697), and airport stores aim for break-even at best. The 13-14% per-EBO margin probably excludes MG. The MG is recovered only if licensed product also sells through SIS, online or B2B. The 17-20% EBITDA band (L190) is held through FY28 with none of this cost in view. Risk: margin drag in FY28 as the format ramps. Ask whether any licence is signed. "we are already spending on MG" (L1041) conflicts with the hypothetical "if I take licensing of Disney" (L1042). |
| A3-06 | F6 | R009 R010 R160 R072 R184 R221 R245 R074 R075 R077 R078 R186 R094 R153; T3, T58-T59, T61, T63, T78, T110; Loop 1: M001 (T11) | L164-165; L300-301; L306; L584-593; L602-603; L670-671; L844 | "We currently operate one kiosk and are targeting 55-plus kiosks" / "Shop-in-shop is our major component where we are selling through our kiosk model" / "shop-in-shop around 1,000 kiosk" / "We have only one EBO, which is in Purnia" | AMBIGUOUS | The word "kiosk" names three formats: airport/high-street outlets (L165), shop-in-shop counters (L301, L670), and EBOs (L602-603). The prepared remarks say 55-plus kiosks with no date. The analyst introduced "these 50 stores" (L584), and the CFO confirmed with "Yes" (L593), but management did not originate the 50 figure. The current base is one kiosk / one EBO. Loop 1: one SIS partner family shop runs "four, five, or six retail outlets" (L306), so the unit of the "1,000" SIS target (counter or partner) is also undefined. A store-count tracker cannot run until management fixes one definition and one dated target per format. |
| A3-07 | F6 | R178 R225 R179 R224 R177 R180 R183 R143-R145; T36, T41, T57 | L446-447; L471-472; L578 | "by the end of this quarter or by the end of this year" / "for this calendar year end or maybe financial year end" / "We are trying to get the space" | AMBIGUOUS | The Brands of Brand launch date moves within one call, from Dec-2026 to Mar-2027. No airport space is secured; talks are open with GMR Delhi, Kolkata and Lucknow. The "roughly 50" stores fall in FY27-FY28 from a base of one. If launch is Q4 FY27, nearly all openings fall in FY28. The rollout is back-ended. Track the launch quarter against the stated Dec-2026 / Mar-2027 window. |
| A3-08 | F6 | T24 (L378-391; no R-ID in turn), Q8; R038 R039 R046 R047 | L379; L385-387 | "Earlier we didn't go for the white labeling, now we are open" / "in the puja sales, because they had gaps available in buying, we sold to them under our own brand name as well" | FORWARD-SIGNAL | The first named Q2 growth driver is one-time festive buying by large retail chains that "had gaps available in buying". That is opportunistic, not contracted. White labeling is still only 2% of revenue (L246, L298, L740). Puja shipments booked in Q2 may leave a softer Q3 for Karnika B2B. Ask what part of Q2 Karnika revenue came from corporate puja orders, and whether they repeat. |
| A3-09 | F6 | R014 R015 R164 R215 R093 R191; T3, T24, T104 | L189-190; L373-375; L821 | "guided towards 30% to 35% CAGR in revenue and profit before tax through FY28" | AMBIGUOUS | The base year of the CAGR is not stated (FY26 or FY27). The metric is PBT, not PAT or EPS, so a tax-rate step-up (A3-02) or equity dilution (A3-04) does not show in it. Asked "what sort of overall growth are you forecasting for this year?" (L373-375), the CFO named drivers and gave no FY27 number. H1 growth of 74.7% against a 30-35% guide implies a sharp H2 slowdown (A3-03). Karnika standalone is guided at a "standard 20% to 25%" (L821), so the gap depends on Kidcity. |
| A3-10 | F6 | R049 R050 R166 R167 R168 R169 R170 R016 R165 R218 R219 R226 R031; T16, T18, T20, T21-T22 | L345-347; L353-354; L360-364; L367-370 | "So we expect margins to be in this 18%, 19% sort of range" (analyst) / "EBITDA margins would be in between 17% to 20%" | AMBIGUOUS | The analyst framed 18-19%. The CFO widened it to 17-20%, and earlier said "Margins will remain almost same what we are achieving in this H1" (L345). [derived] H1 margin is 18.2%. A full-year 17% needs H2 below 17%. Pass-through runs a quarter behind: "In the next first quarter, if anything increases recently, we have to take the hard hit" (L362). Management sees no cotton price relief in Q3/Q4 (L353-354). Any new input-cost rise lands on the next quarter's margin. [derived] Q1 FY27 EBITDA = 33-20 = 13 cr on 74 cr, about 17.6%, which is the low end of the band. |
| A3-11 | F6 | R011 R012 R246 R163 R086 R087 R088 R089 R090 R189 R190; T3, T100, T106, T108 | L180-181; L790-799; L828-838 | "Working capital days improved to 143 days in H1 FY27 from 178 days in FY26" / "still it's above or approx 4 months" / "So, the working capital intensity will be same in the future?" "Right." | AMBIGUOUS | 143 days is a half-year figure. 178 days is a full-year figure. The periods differ. Fast-growing H1 revenue raises the denominator, and a cash-sale subsidiary is now inside the consolidated number. The CFO then says the B2B cycle is "still ... approx 4 months", Kidcity's "inventory channel will be much higher", and WC intensity will stay the same. The target wording is "reduce it by 90 to 100 days" (L791-792), which read literally means a cut of 90-100 days. The 143-day gain may not hold at the FY27 year-end. Ask for receivable, inventory and payable days on a like-for-like basis. |
| A3-12 | F6 | R197 R176 R152 R220 R242; T148, T34, T4 | L1000-1002; L435-437; L217-218 | "wherever capex is required, all those processes we are doing on job working only" / "margin moderated ... primarily due to higher yarn prices, dyeing-related chemical costs, and processing charges" | AMBIGUOUS | Karnika keeps capex low by outsourcing processing to job workers. That turns processing into a variable cost exposed to job-work rates, and "processing charges" is one of the three named causes of the Q2 margin drop. The "not much capex" commitment (L437) and the margin band are linked through this cost. Ask what share of processing is outsourced and how job-work rates moved YoY. |
| A3-13 | F7 | R182 R236 R237 R241 R070 R069 R079; T53, T55, T84; Loop 1: M002 | L547-548; L562-565; L571-572; L698; L704-705 | "They will not be profitable businesses for me" / "Maybe we might be wrong, that we might get profitability from there as well" / "even if we are selling 15 piece per day from per kiosk, we are profitable" | AMBIGUOUS | Within three turns, airport outlets move from "not profitable", to break-even, to "profitable" at 15 pieces a day. The unit economics are not settled, and the 15-piece threshold has no stated price or rent behind it. Airports are the visibility arm of a format that needs equity funding (A3-04). Loop 1: the visibility case rests on dwell time of "one and a half hours, an hour" (L704-705) under "what we are currently presuming" (L698), a presumption, not a measured figure. Ask for the airport kiosk P&L at 15 pieces a day: ASP, rent, MG allocation. |
| A3-14 | F7 | R052 R054 R055 R171 R172 R232 R185; T26, T28, T63 | L403; L411-412 | "we are targeting, assuming in between from INR80 crores to INR100 crores ... and hopefully, we want to achieve that target" | AMBIGUOUS | [derived] H1 Kidcity is INR40 cr. The FY27 low end needs H2 equal to H1, and the high end needs +50%. Hedging a target that is half delivered at the low end ("assuming", "hopefully") is a weak signal on H2 B2C demand. The FY28 target of INR180-200 cr (about 2x) and the INR500 cr FY29-30 target (L600-601) rest on this base. Track the H2 Kidcity figure against INR40 cr. |
| A3-15 | F7 | R238 R095 R096-R099 R084 R239 R004 R005 R006 R138 R139; T9, T94, T121, T123, T127, T129; Loop 1: M004 (T123) | L257-259; L754-756; L893; L901-906; L926 | "our billings will be in the name of some of the big buying houses" / "we don't have that data. Their billing ... for me, that sale shows West Bengal" / "we directly doesn't sell to any wholesalers" (L893) vs "In Karnika, we are doing B2B only to wholesalers only" (L926) | AMBIGUOUS | Karnika bills a small set of large buying houses (arhats, commission agents). The 28-state reach and the 55/45 regional split come from buyer data, not from Karnika's own billing. Loop 1: the CFO names "two methods of billing" (L901). Own-name buying-house billing shows as West Bengal. The 55/45 split covers only the bill-to-ship-to part, and the share of each method is not given. The CFO contradicts himself on whether Karnika sells to wholesalers directly. The 2,500-plus customers (L132) do not fit billing "in the name of some of the big buying houses". Debtor and counterparty concentration is the real exposure on a 3-4 month cycle. Ask for the number of billed counterparties, the top-5 / top-10 receivable share, and the sales share under each billing method. |
| A3-16 | F14 | R110 R111 R085 R240 R189; T0, T94, T100, T3 | L57-62 vs L73; L766; L791-792; L179 | "Niranjan Mundha" (L62) vs "NIRANJAN MUNDHRA" (L57-58, L73) / "100 square feet or 100-kilometer radius" / "reduce it by 90 to 100 days" / "cash conversation" | NEUTRAL-FACT | The filing spells the MD's name two ways (cover letter typed name vs digital signature and participant list). The transcript has unit and wording errors. Each item is minor alone. Together they are a governance data point on filing care. No question needed. |
| A3-17 | F17 | Q3 (T10/T11), Q8 (T23/T24), Q21 (T52/T53), Q30-Q31 (T75-T78), Q58 (T145/T146); A2 MD_SILENT_IN_QA (R111) | L281; L373-375; L535-536; L660-670; L986-993; L130; L163; L181; L262 | "Can you give a breakdown of revenue by each model?" / "how much will you spend on branding and marketing in next two, three years?" / "When do you plan to do this, in which year?" | AMBIGUOUS | Six direct questions got no number or got a different horizon (table in section 4). Topics the MD raised in prepared remarks never return with a figure: exports, institutional supplies, digital channels. Also absent: absolute debt and finance cost, the Kidcity stake and acquisition date, customer concentration, operating cash flow. The MD speaks only in prepared remarks (T3), and the CFO answers all 77 Q&A turns. Silence count is 1 quarter: this is the first transcript read, with no prior quarter and no Notion checklist. A4 converts each row into a question. (Question numbers here follow the pre-Loop-1 A2 numbering; A2 renumbered questions after q35 by +1.) |
| A3-18 | F6 | Loop 1: q36 (T87/T88); R080 R081 R188 R235; with R182 R237 | L719-720; L723-726; L697; L547-548 | "This is across both your outlets like your..." / "Yes. This is across our airport and malls revenue, consolidation, in console with that." | AMBIGUOUS | The INR50 lakh a year, 13-14% margin per-store target (L719-720) covers airport and mall outlets alike (L726). The same CFO puts airport rent at "4x to 6x plus" (L697), and the MD says airport outlets "will not be profitable businesses for me" (L547-548). Reading 1: 13-14% is a blended average, so mall stores must run well above 13-14% to carry airports at or below break-even. Reading 2: each format is meant to reach INR50 lakh at 13-14%, which contradicts the airport statements. The per-format P&L (revenue, rent, margin, MG share) for airport vs mall stores separates the two. Lean bear: the per-store target is not yet a usable tracker input. The L726 wording is garbled ("consolidation, in console with that"). Feeds A3-05 and A3-13. |
| A3-19 | F14 | Loop 1: M003 (T116), M005 (T154); R149 R150 R100 | L867; L1026-1027 | "their four or five brands" (L867) vs "We primarily do with these three" (L1027) | NEUTRAL-FACT | The CFO gives two counts for FirstCry white-label brands in one call: "four or five" at L867, then three named (Mark & Mia, Ed-a-Mamma, Disney) at L1026-1027. White labeling is 2% of sales (L246, L740), so the gap is immaterial. It adds to the A3-16 filing-care data point. One fact for A4 context, no question: one of the three, Disney, is a licensed character (L1049). Karnika already makes licensed product as a contract maker, with the licence and MG held by the buyer. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing line items | N.A. | Concall. Ledger ZERO_STANDING count 0. No line-item tables. |
| F2 Standalone vs consolidated decomposition | FINDING | The call gives a Karnika / Kidcity revenue split with no elimination (A3-01). The EBITDA-to-PAT bridge narrows below EBITDA (A3-02). Acquisition base effect is not separated (A3-03). No standalone EBITDA or PAT on the call. Full S-vs-C trend waits for the results filing. |
| F3 Shell-entity detection | N.A. | Concall. No standalone vs consolidated cost lines. |
| F4 Unaudited contribution ratio | N.A. | Concall. No auditor report or Other Matters paragraph. "Unaudited Financial Results" (L47, R227) is the results basis, not an auditor scope statement. |
| F5 Going concern / EoM scope | N.A. | Concall. No EoM paragraph. No prior-quarter text to diff. |
| F6 Forward-commitment phrase mining | FINDING | Lexicon hits: "will be" (19 lines, L90-L1071), "subject to" L118. No hits for "expected to be/by", "is underway", "has been completed", "commenc", "in the process of", "proposes to", "board has approved", "intends to", "fast-track", "shall be completed", "upon submission". Concall forms ("planning", "targeting", "supposed to", "trying to") are mined too. 22 commitments in the register. Findings A3-04 to A3-12, plus A3-18 (Loop 1). |
| F7 Hedge phrase mining | FINDING | Notes lexicon: only "subject to" (L118). Concall hedges: "assuming"/"hopefully" (L403, L411), "Maybe we might be wrong" (L565), "I think" (L346, L437, L712), "we don't have that data" (L903), "what we are currently presuming" (L698). Findings A3-13, A3-14, A3-15. |
| F8 Tax forensics | N.A. | No tax line, ETR or deferred tax on the call. The below-EBITDA anomaly that may be tax-driven is logged under F2 (A3-02). It is routed to the results-filing F8 check. |
| F9 OCI forensics | N.A. | Concall. No OCI disclosure. |
| F10 Share count and dilution | N.A. | No paid-up capital or basic/diluted EPS on the call. The forward dilution signal (preferential allotment / equity) is logged under F6 (A3-04). |
| F11 Reserves and net worth tie-out | N.A. | The call states D/E of 0.6x only (L181, R013). No net worth or reserves figure to tie out. |
| F12 Segment forensics | N.A. | No segment assets or liabilities on the call. Only the entity revenue split (handled in F2). |
| F13 Board outcome beyond results | N.A. | A concall has no board outcome. Main board migration (L117-118) is a listing event and sits in the F6 register. No enabling resolution is cited. |
| F14 Note drafting inconsistencies | FINDING | MD name variant across the filing. Transcription unit error. "by" vs "to" in the debtor target. A3-16. FirstCry brand count stated two ways (A3-19, Loop 1). |
| F15 Entity list diffs | N.A. | No consolidation list on the call. No prior-quarter ledger (A2: ENTITY_CHANGE not assessable). Kidcity is named as an acquired company with no stake or date. That gap is logged under F17. |
| F16 Presentation: dropped / reframed disclosures | N.A. | Doctype is concall. The analyst refers to a PPT (L250), but that deck is not an A3 input. |
| F17 Concall silence audit | FINDING | Notion checklist arm not runnable (NONE, pre-thesis). Commitment arm and in-call non-answer arm run. Silence count 1 quarter (first read). A3-17. q36 (Loop 1) was answered ("Yes", L726), so it adds no silence row. |

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | turn / line ref | status word |
|---|---|---|---|---|
| C01 | Migration to NSE main board, "subject to completion of the applicable regulatory and procedural requirements" | effective 13-Oct-2026; completion pending | T3 L117-118 (R158 R230 R211) | initiated (eligible; completion not confirmed in a 16-Oct filing) |
| C02 | Revenue and PBT CAGR 30-35% "through FY28"; base year unstated | FY28 (Mar-2028) | T3 L189 (R014 R015 R164) | target |
| C03 | EBITDA margin band 17-20%, group level through FY28 and for FY27 | FY27 and FY28 | T3 L190; T22 L370 (R016 R049 R165 R170) | target |
| C04 | FY27 margin "almost same" as H1 (18.2%); cotton stable for "next half" | H2 FY27 | T16 L345-347; T18 L353-354 (R166 R167 R168) | target |
| C05 | Input-cost pass-through with a one-quarter lag | rolling | T20 L360-364 (R169) | ongoing |
| C06 | 55-plus kiosks at airports and premium high-street (current base: one) | undated | T3 L164-165 (R009 R010 R160) | initiated |
| C07 | About 50 stores (analyst figure, confirmed "Yes") | FY27-FY28 | T58-T61 L584-593 (R072 R184 R221 R245) | initiated |
| C08 | Brands of Brand / new EBO model launch, capex INR10-15 lakh plus inventory INR10-15 lakh per store | "end of this quarter or ... end of this year" (Dec-2026) vs "calendar year end or maybe financial year end" (Mar-2027) | T36 L446-448; T41 L471-481 (R178 R179 R224 R225 R059 R063 R064) | initiated |
| C09 | Airport space with GMR Delhi, Kolkata, Lucknow ("trying to get the space") | undated | T57 L578-581 (R071 R183 R143-R145) | initiated |
| C10 | Cross-city exchange tech, "already started building", close by Feb or March | Feb-Mar 2027 | T84 L710-713 (R187 R223) | underway |
| C11 | Kidcity FY27 revenue INR80-100 cr ("assuming ... hopefully"); H1 INR40 cr | FY27 (Mar-2027) | T28 L403-411 (R054 R171 R232) | target |
| C12 | Kidcity FY28 revenue about INR180-200 cr | FY28 | T28 L411-412 (R055 R172) | target |
| C13 | Kidcity PAT margin 10-13% | current / FY27 | T30 L418 (R056 R173) | target |
| C14 | Kidcity INR500 cr internal target; about 1,000 SIS counters; 300-400 EBO/kiosk outlets | FY29-30 | T63 L600-603; T78 L670-671 (R073-R075 R077 R078 R185 R186 R222) | target |
| C15 | Per-EBO INR50 lakh a year; 13-14% margin "if we are achieving that"; applies "across our airport and malls" outlets (Loop 1, L726) | undated | T86 L719-720; T88 L726 (R080 R081 R188 R235; q36) | target |
| C16 | SIS break-even in 9-12 months (stated as present fact) | per store | T76 L664 (R076 R203) | stated |
| C17 | Karnika standalone growth "standard 20% to 25%" YoY | annual | T104 L821-822 (R093 R191) | target |
| C18 | Debtor cycle to 90-100 days ("reduce it by"; now about 4 months) | undated | T100 L790-799 (R086-R090 R189 R190) | initiated |
| C19 | Debt held at current level; next round via preferential allotment or equity; "healthy capital infusion" for Brands of Brand | when the requirement arises; undated | T144 L981-983; T146 L989-993 (R194 R195 R196) | initiated (intent only) |
| C20 | No significant Karnika capex; manufacturing expansion via job work; accessories outsourced | ongoing | T34 L435-437; T148 L1000-1002; T150 L1009 (R176 R197 R198) | stated |
| C21 | About 12 licensed character brands; MG about INR6-8 cr a year | from Brands of Brand launch | T158 L1065; T160 L1071-1072 (R102 R104 R200 R201) | initiated (projection) |
| C22 | Expansion into Central India / MP belt, region by region; own Indian character "in the long run" | undated | T137 L951; T139 L958; T156 L1057; T162 L1079-1081 (R192 R193 R199 R202) | initiated |

## 4. WHAT WAS NOT DISCUSSED (F17)

Consecutive quarters of silence = 1 for every row. This is the first transcript read. No prior quarter and no Notion checklist exist.

| # | item | where raised | what the call gave | quarters silent |
|---|---|---|---|---|
| S01 | Revenue by sales model (Karnika B2B, SIS, aggregation, Ojos B2B) | Q3, L281 | Qualitative description only, L286-319 | 1 |
| S02 | FY27 consolidated growth forecast | Q8, L373-375 | Drivers only, L378-389 | 1 |
| S03 | Brands of Brand branding/marketing spend over 2-3 years | Q21, L535-536 | No figure, L539-554. MG given later, L1071 | 1 |
| S04 | Store inventory requirement | Q30, L660-661 | Break-even period only, L664 | 1 |
| S05 | Store count by FY28 | Q31, L667 | Answered for FY29-30 instead, L670-671 | 1 |
| S06 | Year of equity raise | Q58, L986 | "This will consider how the capital funding requirement arises", L989 | 1 |
| S07 | Exports and institutional supplies (MD lists both as platform parts) | T3, L130, L143 | Not mentioned again. SEDEX unit noted L436. Kidcity "100% ... domestic", L657 | 1 |
| S08 | Digital / online channel revenue | T3, L163; L551, L1019 | No figure | 1 |
| S09 | Absolute debt, finance cost, operating cash flow | T3, L179-186 | D/E 0.6x only, L181 | 1 |
| S10 | Kidcity stake, acquisition date, consideration; minority interest | T9, L262 | "acquired by Karnika" only | 1 |
| S11 | Buying-house / customer concentration | L257-259, L754-756 | No count or share | 1 |
| S12 | Intercompany sales Karnika to Kidcity | L425-426 | 60% production share, no Rs figure | 1 |
| S13 | MD participation in Q&A | T3 only | CFO answers all Q&A | 1 |

Question labels Q3-Q31 above are unchanged by the A2 renumbering. Q58 is q59 in the amended ledger (A2 renumbered every question after q35 by +1).

## 5. FLAGGED FOR A4

FORWARD-SIGNAL (turn into management questions and Role 5 tracker rows): A3-03, A3-04, A3-05, A3-08.
AMBIGUOUS (turn into management questions): A3-01, A3-02, A3-06, A3-07, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-17, A3-18.
NEUTRAL-FACT: A3-16, A3-19.

## 6. LOOP 1 DELTA

Scope: the six new A2 ledger units only (q36 and M001-M005). The rest of the checklist was not re-run. Each unit was read at its fulltext line.

| unit | fulltext line | verbatim | effect on F1-F17 | new finding |
|---|---|---|---|---|
| q36 (T87, answered T88) | L723-726 | "This is across our airport and malls revenue, consolidation, in console with that." | None. F6 stays FINDING. C15 scope widened to airport and mall outlets. No F17 row: the question got a "Yes". | A3-18 (F6, AMBIGUOUS) |
| M001 | L306 | "their own almost four, five, or six retail outlets where kids' counter is handled by the Kidcity" | None. Added to A3-06: the unit of the 1,000 SIS target (counter or partner) is undefined. | none |
| M002 | L704-705 | "you spend one and a half hours, an hour of time" | None. Added to A3-13: the airport visibility case rests on a presumed dwell time (L698). F7 hedge list gains "what we are currently presuming" (L698). | none |
| M003 | L867 | "their four or five brands to them" | None. F14 stays FINDING. | A3-19 (F14, NEUTRAL-FACT), with M005 |
| M004 | L901 | "there are two methods of billing" | None. A3-15 already cited L901-906. Its implication and question now name the share of sales under each billing method. | none |
| M005 | L1026-1027 | "around 10 to 12 products on which work is done. We primarily do with these three." | None. Conflicts with M003 ("four or five"). | A3-19 (with M003) |

Checklist status changes: 0. New findings: 2 (A3-18 AMBIGUOUS to A4; A3-19 NEUTRAL-FACT). Amended findings: A3-06, A3-13 and A3-15 (Loop 1 text added). The verdicts are unchanged. Ledger reconciliation stays at 100%: 246 IDs, 167 turns and the 6 Loop 1 units were read. gate_a3 stays pass.

```yaml
stage: A3-forensics
company: "KARNIKA"
quarter: "h1fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/karnika-h1fy27/work/forensics_concall_karnika_h1fy27.md"
correction_loop: 1
loop1_units_reviewed: ["q36", "M001", "M002", "M003", "M004", "M005"]
loop1_status_changes: []
loop1_new_findings: ["A3-18", "A3-19"]
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3-01", check: "F2", line: "L395-396; L425-426", classification: "AMBIGUOUS", implication: "140+40=180 with no intercompany elimination though Karnika makes 60% of Kidcity goods; standalone growth may be overstated; results filing S-vs-C revenue separates the readings"}
  - {id: "A3-02", check: "F2", line: "L216-217; L221-222", classification: "AMBIGUOUS", implication: "PAT +51% vs EBITDA +38.1% with margin -190bps; EBITDA-PAT gap 7.2pp->5.4pp; gain is below EBITDA, not operating leverage; check ETR, other income, MI in results filing"}
  - {id: "A3-03", check: "F2", line: "L215; L223; L262", classification: "FORWARD-SIGNAL", implication: "derived Q1 FY27 YoY ~+121% vs Q2 +52.3%; Kidcity acquisition date and stake undisclosed; growth likely slows toward 30-35% as base laps"}
  - {id: "A3-04", check: "F6", line: "L981-983; L989-993; L117-118", classification: "FORWARD-SIGNAL", implication: "debt capped; preferential allotment or equity named for Brands of Brand; main board migration precedes; dilution not in PBT guidance"}
  - {id: "A3-05", check: "F6", line: "L1065-1072; L719-720; L546-548; L697", classification: "FORWARD-SIGNAL", implication: "MG INR6-8cr vs derived INR25cr revenue at 50 stores x INR50 lakh (24-32%); airports break-even at best; FY28 margin drag vs 17-20% band"}
  - {id: "A3-06", check: "F6", line: "L164-165; L300-301; L306; L584-593; L602-603; L670; L844", classification: "AMBIGUOUS", implication: "'kiosk' names SIS, EBO and airport formats; 55-plus vs analyst-sourced 50; base of one; SIS partners run 4-6 outlets each (L306) so the 1,000 SIS unit is undefined; store tracker needs one definition"}
  - {id: "A3-07", check: "F6", line: "L446-447; L471-472; L578", classification: "AMBIGUOUS", implication: "Brands of Brand launch drifts Dec-2026 to Mar-2027 in one call; no airport space secured; rollout back-ended into FY28"}
  - {id: "A3-08", check: "F6", line: "L379; L385-387", classification: "FORWARD-SIGNAL", implication: "Q2 driver includes one-time puja buying by chains with 'gaps available in buying'; Q3 Karnika B2B may soften"}
  - {id: "A3-09", check: "F6", line: "L189-190; L373-375; L821", classification: "AMBIGUOUS", implication: "CAGR base year unstated; PBT not EPS; no FY27 number when asked; H1 +74.7% implies sharp H2 slowdown"}
  - {id: "A3-10", check: "F6", line: "L345; L362; L367-370", classification: "AMBIGUOUS", implication: "analyst 18-19% widened to 17-20%; FY 17% needs H2 below 17% vs H1 18.2%; one-quarter pass-through lag; derived Q1 ~17.6%"}
  - {id: "A3-11", check: "F6", line: "L180; L790-799; L828-838", classification: "AMBIGUOUS", implication: "143d (H1) vs 178d (FY) not like-for-like; CFO says B2B ~4 months and WC intensity unchanged; year-end WC days may revert"}
  - {id: "A3-12", check: "F6", line: "L1000-1002; L217-218", classification: "AMBIGUOUS", implication: "capex-light via job work makes processing a variable cost; processing charges named in Q2 margin drop"}
  - {id: "A3-13", check: "F7", line: "L547-548; L565; L571-572; L698; L704-705", classification: "AMBIGUOUS", implication: "airport outlets go from not profitable to break-even to profitable at 15 pcs/day in three turns; visibility case rests on presumed 1-1.5 hour dwell time; unit economics unsettled"}
  - {id: "A3-14", check: "F7", line: "L403; L411-412", classification: "AMBIGUOUS", implication: "hedged Kidcity FY27 INR80-100cr; low end needs H2 = H1 INR40cr; weak signal on H2 B2C demand; FY28 and FY29-30 targets rest on it"}
  - {id: "A3-15", check: "F7", line: "L257-259; L893; L901-906; L926", classification: "AMBIGUOUS", implication: "billing to few buying houses; two billing methods (L901), 55/45 split covers bill-to-ship-to only, share of each method undisclosed; CFO contradicts on wholesaler sales; counterparty and debtor concentration undisclosed"}
  - {id: "A3-16", check: "F14", line: "L57-62; L73; L766; L791-792; L179", classification: "NEUTRAL-FACT", implication: "MD name variant, unit transcription error, by/to wording; minor filing-care data point"}
  - {id: "A3-17", check: "F17", line: "L281; L373-375; L535-536; L667-670; L986-989; L130; L262", classification: "AMBIGUOUS", implication: "6 non-answers plus 7 undisclosed topics (exports, debt quantum, Kidcity stake, concentration, OCF, intercompany, MD in Q&A); silence count 1 quarter"}
  - {id: "A3-18", check: "F6", line: "L719-720; L723-726; L697; L547-548", classification: "AMBIGUOUS", implication: "INR50 lakh / 13-14% per-store target applies across airport and mall outlets (L726) though airports carry 4-6x rent and are called not profitable; either mall stores run well above 13-14% or the target contradicts the airport statements; per-format P&L separates the readings; feeds A3-05 and A3-13"}
  - {id: "A3-19", check: "F14", line: "L867; L1026-1027", classification: "NEUTRAL-FACT", implication: "FirstCry white-label brand count given as 'four or five' then 'these three'; white label is 2% of sales so immaterial; adds to A3-16 filing-care point"}
forward_signals: ["A3-03", "A3-04", "A3-05", "A3-08"]
ambiguous: ["A3-01", "A3-02", "A3-06", "A3-07", "A3-09", "A3-10", "A3-11", "A3-12", "A3-13", "A3-14", "A3-15", "A3-17", "A3-18"]
commitments:
  - {commitment: "NSE main board migration, subject to regulatory and procedural requirements", implied_date: "effective 2026-10-13; completion pending", ref: "T3 L117-118", status_word: "initiated"}
  - {commitment: "Revenue and PBT CAGR 30-35% through FY28 (base year unstated)", implied_date: "FY28", ref: "T3 L189", status_word: "target"}
  - {commitment: "EBITDA margin 17-20% (FY27 and through FY28)", implied_date: "FY27-FY28", ref: "T3 L190; T22 L370", status_word: "target"}
  - {commitment: "FY27 margin almost same as H1; cotton stable next half", implied_date: "H2 FY27", ref: "T16 L345-347; T18 L353-354", status_word: "target"}
  - {commitment: "Input-cost pass-through with one-quarter lag", implied_date: "rolling", ref: "T20 L360-364", status_word: "ongoing"}
  - {commitment: "55-plus kiosks at airports/high-street from base of one", implied_date: "undated", ref: "T3 L164-165", status_word: "initiated"}
  - {commitment: "About 50 stores (analyst figure, confirmed Yes)", implied_date: "FY27-FY28", ref: "T58-T61 L584-593", status_word: "initiated"}
  - {commitment: "Brands of Brand launch; capex INR10-15 lakh plus inventory INR10-15 lakh per store", implied_date: "Dec-2026 to Mar-2027 (drifts within call)", ref: "T36 L446-448; T41 L471-481", status_word: "initiated"}
  - {commitment: "Airport space with GMR Delhi, Kolkata, Lucknow", implied_date: "undated", ref: "T57 L578-581", status_word: "initiated"}
  - {commitment: "Cross-city exchange tech close", implied_date: "Feb-Mar 2027", ref: "T84 L710-713", status_word: "underway"}
  - {commitment: "Kidcity FY27 revenue INR80-100cr (hedged)", implied_date: "FY27", ref: "T28 L403-411", status_word: "target"}
  - {commitment: "Kidcity FY28 revenue about INR180-200cr", implied_date: "FY28", ref: "T28 L411-412", status_word: "target"}
  - {commitment: "Kidcity PAT margin 10-13%", implied_date: "FY27", ref: "T30 L418", status_word: "target"}
  - {commitment: "Kidcity INR500cr; ~1,000 SIS; 300-400 EBO/kiosk", implied_date: "FY29-30", ref: "T63 L600-603; T78 L670-671", status_word: "target"}
  - {commitment: "Per-EBO INR50 lakh a year at 13-14% margin (conditional), across airport and mall outlets", implied_date: "undated", ref: "T86 L719-720; T88 L726", status_word: "target"}
  - {commitment: "SIS break-even in 9-12 months", implied_date: "per store", ref: "T76 L664", status_word: "stated"}
  - {commitment: "Karnika standalone growth 20-25% YoY", implied_date: "annual", ref: "T104 L821-822", status_word: "target"}
  - {commitment: "Debtor cycle to 90-100 days from about 4 months", implied_date: "undated", ref: "T100 L790-799", status_word: "initiated"}
  - {commitment: "Debt held flat; next round via preferential allotment or equity", implied_date: "when requirement arises", ref: "T144 L981-983; T146 L989-993", status_word: "initiated"}
  - {commitment: "No significant Karnika capex; job work; accessories outsourced", implied_date: "ongoing", ref: "T34 L435-437; T148 L1000-1002; T150 L1009", status_word: "stated"}
  - {commitment: "About 12 licensed brands, MG INR6-8cr a year", implied_date: "from Brands of Brand launch", ref: "T158 L1065; T160 L1071-1072", status_word: "initiated"}
  - {commitment: "Central India / MP expansion; own Indian character long run", implied_date: "undated", ref: "T137 L951; T156 L1057; T162 L1079-1081", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read; no prior quarter or checklist, so F17 silence counts are 1. Three threads matter most. First, growth quality: derived Q1 FY27 YoY of about +121% falling to +52.3% in Q2, plus an acquired subsidiary with no stated stake or date, points to acquisition base effect; the 140+40=180 split carries no intercompany elimination though Karnika makes 60% of Kidcity goods. Second, the earnings bridge: PAT outgrew EBITDA while EBITDA margin fell 190 bps, so the gain sits below EBITDA, not in the operating leverage the CFO cited. Third, the B2C build: licence MG of INR6-8cr against about INR25cr revenue at 50 stores, a launch date that drifts within one call, and equity named as the funding route. Loop 1 (q36, L726) sharpens the third: the INR50 lakh, 13-14% per-store target is blended across airport and mall outlets, though airports carry 4-6x rent and are called not profitable, so mall stores must run well above 13-14%. These put the 17-20% band and EPS growth at risk in FY28. A1 line drifts are in report section 0; M001-M005 change no check status."
```
