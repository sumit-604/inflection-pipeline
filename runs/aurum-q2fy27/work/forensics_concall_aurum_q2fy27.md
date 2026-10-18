# A3 FORENSIC NOTES: AURUM | q2fy27 | doctype: concall (earnings call 16-Oct-2026)

Inputs read: A1 structured (extracted/aurum-concall-q2fy27-structured.md), A1 fulltext (extracted/aurum-concall-q2fy27-fulltext.md, 417 lines), A2 ledger (work/ledger_concall_aurum_q2fy27.md), work/notion-thesis.md (Monitoring checklist, triggers, Events since Q1, Prior quarter Questions), work/review_aurum_q2fy27.md lines 520-554 (Step 8.5 table only). Prior-quarter fulltext: not available (no Q1 FY27 concall on file). No source PDF and nothing under inputs/ was opened.

SOURCE CAVEAT: machine transcript (faster-whisper). Speakers are A1-inferred. Where a spoken number conflicts with the filing, the filing wins. Misheard-number doubts are classified AMBIGUOUS, not management error. Filing figures cited below come only from the Notion checklist and the review Step 8.5 table passed in the task.

## 0. LEDGER RECONCILIATION

- Structured IDs R001-R341: 341. Ledger references 341, orphans 0 (ledger L13). All 341 rows read at their cited fulltext line. Reconciled: 341/341 = 100%.
- Turns T001-T065 and questions Q01-Q19 checked against the turn table line ranges.
- Line-cite offsets found (text present, cited line off by 1-2; no row lost):
  - R150 cites L291; "two 80" sits at L290 ("projects" at L291).
  - R218 cites L291; "let it go" sits at L290.
  - R219 cites L292; "sell.do" first appears at end of L291.
  - R227 cites L405; "Aishwashi" sits at L407.
  - R328 cites L158; "78.3 crores of the lease payments" sits at L159 (R100 correctly cites L159).
  - R339 cites L339; "commission between 1 to 1.2%" sits at L338 (R166 correctly cites L338).
- A2 flag gap: R200 "Integral" (L142, associate) is very likely Integrow as heard. A2 did not flag NAME_AS_HEARD.
- A2 CONFLICT_INCALL pairs resolved here: R006/R015 (1200+ vs 1270 bps) is rounding, not a conflict. R180/R181/R183 (a thousand vs 1020 crore) is an approximation followed by the exact figure, not a conflict. R026/R147-R149 (occupancy), R031/R175/R340 (MAU) and R177/R178 (100x/345x) are handled in F14.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3C-01 | F17 (item 1) | R004, R005, R067, R317 | L45, L46, L138, L143 | "Q2 of FY27 is our fourth consecutive profitable quarter." / "Other income is mainly treasury and deposit income." | CONFIRMATORY-NEGATIVE | The call says profit comes from unit economics. It never states the other-income amount. Q2 PBT continuing Rs6.8 Cr (L143) is below filed OI of Rs7.12 Cr (review row 1). Core PBT ex-OI is Rs(0.52) Cr, or Rs(4.26) Cr with capitalised team cost expensed. Trigger 1 stays FIRED. The call adds no evidence against it. Unanswered for 2 quarters (Q1 filing, Q2 call). |
| A3C-02 | F17 (item 1) | R090, R091, R317 | L138, L154-155 | "Other income is mainly treasury and deposit income." | AMBIGUOUS | [INFERENCE] Average cash ex Housing.com was about Rs150-165 Cr (141 to 169.6, L154-155). At about 7% that gives Rs2.6-2.9 Cr a quarter. Add about Rs1.0 Cr a quarter on the Rs9.52 Cr loan (Rs2.01 Cr H1 interest). Total is about Rs3.6-3.9 Cr against Q2 OI of Rs7.12 Cr, so about half is not treasury. The filing's H1 non-treasury items (lease-termination 4.51, provision reversal 2.67, PPE 0.23 = Rs7.41 Cr) point the same way. Ask for the Q2 split. |
| A3C-03 | F6 | R008, R231, R138-R140, R252-R255, R333, R334 | L61, L222-223, L234, L237-239 | "We are targeting to make housing.com profitable within 12 to 18 months." / "four to six quarters is our internal target, six to eight quarters is our external target" | FORWARD-SIGNAL | The target has two tiers. The external one (6-8 quarters, to about Q2 FY29) is the accountable date. The internal 4-6 quarters is about Q2-Q4 FY28. "Profitable" vs "break even" is undefined: EBITDA, or PBT after PPA amortisation? The same call says "It's still early days to give some kind of a projection" (L222-223). The target has no disclosed base. |
| A3C-04 | F6 | R156, R157, R159, R265, R266, R337 | L317-318, L320, L321 | "we have cut costs of approximately 120 crores from the business." / "revenue growth of another 150 crores over next four to six quarters, which will kind of move housing.com to profitability" | AMBIGUOUS | The period basis of Rs120 Cr (annualised or not) is unstated. Housing.com's revenue and cost base is not given. [INFERENCE] The Rs120 Cr cost plus Rs150 Cr revenue bridge implies a pre-deal annual loss of up to that order. Rs1,020 Cr of losses over 10-12 years (L381) averages about Rs85-100 Cr a year. "We have gone very deep with the cuts" (L320), yet no one-time severance or restructuring cost is mentioned. That is a Q3 charge risk. Q3 consolidated PBT carries Housing.com's result, so trigger 1 remains exposed. |
| A3C-05 | F12 | R242 | L172 | "From Q3, distribution will include a full quarter of housing" | FORWARD-SIGNAL | Housing.com goes inside the Distribution segment, not into its own segment. From Q3, checklist item 6 (Distribution margin >=12%) and item 2 (organic growth) lose comparability unless management splits it out. A loss-making Housing.com will dilute the 16.3% segment margin mechanically. |
| A3C-06 | F7 | R262, R264 | L294-295, L308-311 | "We will try to articulate that separately in different slides in the investor presentation going forward to say, look, what is organic and what is coming out of synergies." | FORWARD-SIGNAL | The one disclosure that would resolve item 2 carries a "try" hedge. A KPI reframe to developer / broker / consumer segments (L294-295) may drop current KPIs (leads, licences, beds, occupancy). Run F16 on the Q3 FY27 deck. Test: does the Q3 deck carry an organic vs synergy slide? |
| A3C-07 | F12 | R102, R121, R318, R319 | L139, L140-141, L161, L174, L272 | "The segment reported a profit of 0.9 crore" / "Most of the finance cost is the interest component of these liabilities." | AMBIGUOUS | Under Ind AS 116, co-living rent sits in D&A and finance cost (L139). Lease liabilities of Rs216 Cr "relate mainly to co-living" (L161). Most of the Rs6.3 Cr finance cost is lease interest (L140-141). [INFERENCE] If most of that interest belongs to Rental, Rental after lease interest is a loss of about Rs4-5 Cr. "we are profitable across the rental segment" (L272) then holds only before lease interest. This bears on the item 5 breakeven definition. Lean bear. |
| A3C-08 | F17 (FLAG-CASH) | R105, R107, R108, R109, R090-R092 | L154-155, L163-166 | "Operating cash flow, therefore, covered both product investment and our full lease commitments." | AMBIGUOUS | H1: 60.8 OCF - 8.8 capex - 47.8 lease principal = Rs4.2 Cr headroom. Cash rose Rs50.6 Cr (141 to 191.6). Less Rs22 Cr Housing.com cash (L155) and Rs24 Cr discontinued (L166), the continuing build is about Rs4.6 Cr, which ties to the Rs4.2 Cr. The call does not say where lease interest sits. If it sits in financing, OCF does not cover about Rs12 Cr of H1 lease interest [INFERENCE from Rs6.3 Cr a quarter]. Cash stays INDETERMINATE. |
| A3C-09 | F6 | R129-R133, R166, R167, R210, R211, R248-R250, R272, R339 | L211-216, L338-339 | "they have dispersed 200 crores of loans, which means that they are at 2,400 crores of run rate" / "spiral up to 25,000 crores in next four to six quarters" | FORWARD-SIGNAL | The run rate annualises one month (September). The target is 10.4x in 4-6 quarters (by Q2-Q4 FY28). At a 1-1.2% take rate, annualised revenue would go from about Rs24-29 Cr to Rs250-300 Cr. The call does not say whether the rate is gross or net of sub-agent payouts. It also does not say which segment books it: KuberX is "run within the PropTiger team" (L215), so Capital or Distribution. Capital Q2 revenue was Rs4.3 Cr (L175). Track it quarterly. |
| A3C-10 | F6 | R009, R161-R163, R234, R267, R338 | L69, L323-324 | "revenue per team member will continue to go up quarter on quarter for next 10 to 12 quarters" / "But this is mostly driven from a cost point of view." | FORWARD-SIGNAL | A dated quarter-on-quarter promise: 40 to 50+ lakh now, 56 lakh by year end. The period basis and headcount definition are unstated. The gain is cost-driven. From Q3 the post-cut Housing.com headcount enters, so the metric moves mechanically. Test it every quarter to about FY30. |
| A3C-11 | F7 | R164 | L324 | "we are yet to see defined and tangible results on that." | CONFIRMATORY-NEGATIVE | Management concedes that the AI consumer-journey investment (last two quarters) shows no tangible revenue result yet. AI gains so far are cost-side (L324). This supports FLAG-NARRATIVE-VS-EVIDENCE (AI moat). |
| A3C-12 | F8 | R070, R071, R104, R180-R183, R280, R281, R321, R329, R341 | L144, L162, L378-385 | "losses in some subsidiaries are not yet recognized as a tax asset" / "how much of this can be amortized over the larger ecosystem is something yet to be seen" | FORWARD-SIGNAL | The ETR of about 37% against the 25.17% statutory rate is a drag of about 1,180 bps. Locon adds another loss entity from Q3, so the ETR stays high or rises. [INFERENCE] India has no group tax consolidation. Without a merger, Locon's Rs1,020 Cr losses offset only Locon's own income, and change-of-ownership rules may restrict them. Reading (a): losses usable, so a later DTA recognition gives a non-cash tax credit that flatters PAT (up to about Rs257 Cr at 25.17% if all recognised). Reading (b): not usable, so the analyst's "no taxes for 3-4 years" premise (L375) fails. The tax-opinion outcome (L384) or a DTA note separates the two. The non-current DTL of Rs50.4 Cr (L162) is not split by entity or by PPA. |
| A3C-13 | F10 | R072-R074, R086, R095 | L145-146, L151, L156 | "Basic EPS from continuing operations was 0.52 for the quarter" | AMBIGUOUS | 4.5 / 0.52 gives about 865 lakh weighted shares. About 765 lakh were in issue before 29-Sep, and the 1.98 Cr swap shares weight in for about 2 days, so about 769 lakh is expected and EPS should be about 0.59 [INFERENCE]. The filing prints 0.52 too (review Q8), so this is not a mishearing. The bridge is unanswered. Dilution on the call: 1.98 Cr swap shares (L151) and 51 lakh warrants. Rs29.5 Cr = 25% implies Rs231.4 per warrant (L156), which ties to Notion's Rs231.421. |
| A3C-14 | F11 | R084, R085, R087, R088, R062, R064 | L140, L150-151 | "Shareholders' equity roughly doubled to 1,020 crore." / "Woodville and Intangible assets now totaled 960 crores." | FORWARD-SIGNAL | Goodwill plus intangibles of Rs960 Cr = 94% of equity (Rs1,020 Cr), so tangible equity is about Rs60 Cr. Any impairment hits net worth almost 1:1 (item 7). Locon intangibles (Rs319.07 Cr, review Q4) amortise from Q3. The Q2 D&A of Rs28.1 Cr "broadly flat on quarter one" (L140) will step up. The call is silent on the Q3 D&A charge. |
| A3C-15 | F11 | R076, R084, R085, R087 | L147, L150-151 | "Shareholders' equity roughly doubled to 1,020 crore." | AMBIGUOUS | Tie-out: "roughly doubled" implies about Rs510 Cr in March. 510 + 458 swap + 49.5 H1 PAT = Rs1,017.5 Cr, which ties to 1,020. But Notion's one-line thesis (Rs174.25 Cr goodwill = 61% of NW) implies NW of about Rs286 Cr. 286 + 458 + 49.5 = Rs793.5 Cr, a gap of about Rs226 Cr (>5%). Candidate reconciling items: NCI included or excluded, owners vs total equity, the Notion base being standalone or a different date, warrant or rights money. A4 checks the filed balance sheet. The filing wins. |
| A3C-16 | F7 | R089, R325, R326 | L152-153 | "The Housing.com purchase price allocation was prepared by an independent valuer and its provisional." / "it may be refined with the 12-month measurement period" | AMBIGUOUS | The item 7 baseline (Rs549.45 Cr provisional goodwill) can move up to about 29-Sep-2027 without any impairment. The call does not state the CGU allocation, intangible classes or useful lives (review Q4). |
| A3C-17 | F17 (review Q13) | R013, R045-R051, R053, R056, R057 | L91, L131-136 | "Our performance reflects improving monetization, cost discipline and increasing operating leverage." | CONFIRMATORY-NEGATIVE | The call's own numbers: employee plus other expenses were 26.2% + 47.8% = 74.0% of revenue in Q2, against 27.9% + 45.0% = 72.9% in Q1 (+110 bps). EBITDA margin on total income fell from 31.5% (Q1) to 29.8% (L135-136). The QoQ operating-leverage claim is not supported. YoY other expenses did fall, from 49.5% to 47.8% (L134). |
| A3C-18 | F14 (in-call conflict) | R007, R031, R174, R175, R340 | L57, L109, L364 | "with 45 million monthly active users" / "it has 12 million monthly active users" | AMBIGUOUS | The two figures differ by 3.75x; this is a machine transcript. 58 mn visits a month (L57, L364) over 45 mn MAU gives 1.3 visits per user; over 12 mn it gives 4.8 [INFERENCE: 12 mn is the more consistent figure]. The "1.2 times its nearest competitor" claim (L109) depends on which is right. The deck or filing wins. |
| A3C-19 | F14 (in-call conflict) | R026, R147-R149, R259, R298 | L104, L276-277 | "16,500 beds at 82% occupancy" / "we are at 88% occupancy, 82% occupancy, and the team has projected it to be 88% occupancy by the end of this year" | AMBIGUOUS | This reads as a self-correction to 82% now and 88% target. "End of this year" could mean Mar-2027 or Dec-2026. That is +600 bps in at most 2 quarters while beds are set to grow (L270-273). The deck wins. |
| A3C-20 | F14 (in-call conflict) | R006, R015, R016, R068 | L47, L90, L143 | "PVT margins improved 1270 basis points to 4.8%" / "against the loss of 8.9 crore in Q2 of FY26" | AMBIGUOUS | 4.8% is about 6.6 / 137 (PBT before associate over total income), so the implied base is -7.9%. On L143's Rs(8.9) Cr over about Rs85-88 Cr of income, the base is about -10.1% to -10.5%, which gives about 1,490-1,530 bps [INFERENCE]. The spoken expansion must use a different Q2 FY26 PBT, possibly one that includes discontinued operations. This is basis mixing and minor. 1200+ (L47) vs 1270 (L90) is rounding. |
| A3C-21 | F14 | R011-R014, R309 | L88-89 | "Adjusted EBITDA margins expanded 840 basis points to 11.5%" / "137 crores in total income, growing 56% year on year" | NEUTRAL-FACT | 11.5% - 8.4 pp gives a 3.1% Q2 FY26 base. That matches deck slide 3, not slide 29's -3.2% (partly answers review Q11). 137 / 1.56 gives a base of about Rs87.8 Cr, the press-release base that includes discontinued income (partly answers review Q20). |
| A3C-22 | F15 | R199, R200, R203, R210, R211 | L124, L142, L156, L211, L215 | "we completed the acquisition of housing.com through Lokon solutions" / "Orem has recently launched their business in the same segment with the name of KuberX" | AMBIGUOUS | Additions: Locon (Housing.com) from 29-Sep, and KuberX, a new business line whose legal entity and segment are not named. The associate "Integral" (L142) is likely Integrow as heard. The call does not mention AMSA (the SM-REIT vehicle) or the Integrow control abeyance. No prior-quarter fulltext exists, so no wider diff is possible. |
| A3C-23 | F13 | R184, R185, R304 | L389-390, L400 | "both created a subcommittee to say, okay, look, this team will, this, these directors will work with you" | AMBIGUOUS | The board formed a directors' subcommittee on the Housing.com integration and held three board meetings on it. The call does not give its composition, its mandate, its independent members, or whether it was formally constituted. |
| A3C-24 | F17 (management presence) | R191 | L29 | "Mr. Kunal Karan, CFO." | NEUTRAL-FACT | The CFO is listed but has no inferred turn. The deputy CFO read the financials. The chairman is non-executive (L28). Speakers are machine-inferred, so the absence is unconfirmed. |
| A3C-25 | F6 | R134, R270, R271 | L222, L333-334 | "we will not do something inorganic in a short run for sure" | NEUTRAL-FACT | An M&A pause with no date ("short run"), after the "eighth acquisition in the last four years" (L222). It indirectly answers review Q21 (no other pending deal implied). |
| A3C-26 | F17 (item 3) | R123, R126, R129 (absence of SM-REIT) | L175, L207-216 (searched L24-417) | "Capital revenue was 4.3 crores ... a segment broke even with 0.4 crore profit." | CONFIRMATORY-NEGATIVE | SM-REIT, AMSA and AUM are not mentioned once. The Capital discussion covers KuberX only. The trigger 3 condition extends: Q1 status RED (5th consecutive), plus this call, makes at least 6. |
| A3C-27 | F17 (item 2) | R313, R314, R332 | L128-130, L169-170 | "The sequential growth of 16% is entirely organic because the group perimeter was effectively unchanged" | AMBIGUOUS | Organic growth is given QoQ only (+16% group, +25% Distribution, which is positive). YoY ex-PropTiger is still not given ("boosted by RockTiger's first full year", L170). This is the 2nd quarter unanswered. Housing.com changes the perimeter again in Q3. |
| A3C-28 | F17 (item 4) | R105, R106 (no receivables row) | L163 (searched L24-417) | "Operating cash flow from continuing operations in H1 was 60.8 crore, up from 25.4 crore a year ago." | AMBIGUOUS | The call says nothing on receivables ageing, the over-1-year bucket, or the Rs4.44 Cr H1 provision. OCF more than doubled with no working-capital split. This is the 2nd quarter of silence (FY26 ageing also missing). |
| A3C-29 | F17 (item 8) | R093, R203 | L156 (searched L24-417) | "we also received 29.5 crore from our promoter, Odum Real Estate Developers" | AMBIGUOUS | AREDL appears only as the warrant payer. The call is silent on the Rs9.52 Cr loan borrower (about 42% annualised), the named AREDL loan/advance test, the auditor and RPTs. Item 8 was RED at Q1, so this is the 2nd quarter. Lean bear. |
| A3C-30 | F17 (item 9) | R086, R087, R093-R097 | L151, L156-157 | "The remaining 88.5 crores is payable when the warrants are exercised within 18 months." | AMBIGUOUS | The amounts tie to Notion (Rs29.51 / 88.52 Cr, about 13-Apr-2028). The call gives no objects or use of proceeds and no plan if the warrants are not exercised. For the Housing.com swap (1.98 Cr shares, Rs458 Cr) it gives no accretion view. This is the 2nd quarter unanswered. |
| A3C-31 | F17 | R221 | L325-328 | "We've lost the connection of Yash." | NEUTRAL-FACT | The question from Yash Sajpal (IFC) was not heard. Its content is not on record. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | N.A. | Concall. The ledger has 0 ZERO_STANDING rows (ledger L10, L469). This is a results-template check. |
| F2 | N.A. | No standalone figures are spoken. The call is consolidated only. |
| F3 | N.A. | No standalone vs consolidated cost lines on a call. |
| F4 | N.A. | No auditor Other Matters on a call. Noted: the associate share is Rs0.2 Cr (L142), about 4.7% of Rs4.3 Cr PAT. |
| F5 | N.A. | No EoM or going-concern language on a call. |
| F6 | FINDING | 22 commitments registered. Key ones: Housing.com break-even two-tier target (A3C-03), cost/revenue bridge (A3C-04), KuberX 10x (A3C-09), revenue per team member (A3C-10). |
| F7 | FINDING | "try" (L308, L310, L385), "evaluating" (L341), "endeavor" (L64), "subject to" (L31), "yet to be seen" (L383), "may be refined" (L153), "yet to see ... tangible results" (L324). A3C-06, 11, 16. |
| F8 | FINDING | ETR about 37% vs 25.17%. Subsidiary losses not recognised. Locon Rs1,020 Cr losses with usability unresolved (A3C-12). |
| F9 | N.A. | OCI is not spoken. |
| F10 | FINDING | The EPS 0.52 denominator is inconsistent with the shares in issue (A3C-13). Dilution instruments are stated and tie to Notion. |
| F11 | FINDING | Equity is 94% intangible (A3C-14). The equity tie-out against Notion's 61%-of-NW line has a gap of about Rs226 Cr (A3C-15). |
| F12 | FINDING | Housing.com goes into Distribution from Q3 (A3C-05). Rental profit is before lease interest (A3C-07). Segment assets and liabilities are not spoken. |
| F13 | FINDING | Directors' subcommittee on integration, composition unstated (A3C-23). |
| F14 | FINDING | Adapted to concall as internal in-call inconsistencies: MAU (A3C-18), occupancy (A3C-19), PBT bps base (A3C-20). The base checks in A3C-21 tie. |
| F15 | FINDING | Locon added. KuberX entity and segment unnamed. "Integral" likely Integrow. AMSA and Integrow absent (A3C-22). |
| F16 | N.A. | Concall, not a presentation. The announced KPI reframe and synergy slides (A3C-06) are forwarded to the Q3 deck's F16 run. |
| F17 | FINDING | Silence audit below: 9 checklist items, 10 prior questions, 22 review questions. |

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | turn / line | status word |
|---|---|---|---|---|
| C01 | Housing.com profitable within 12-18 months | Sep-2027 to Mar-2028 | T003 L61 | initiated ("already begun deep cost optimization", L60) |
| C02 | Housing.com break-even: 4-6 qtrs internal, 6-8 qtrs external, "profitable ... before that" | internal Q2-Q4 FY28; external to Q2 FY29 | T026 L234, L237-239 | initiated |
| C03 | Cost cut of about Rs120 Cr at Housing.com in the first week | done (Oct-2026) | T035 L317-318, L321 | completed ("The cost optimization is already done") |
| C04 | Housing.com revenue +Rs150 Cr over 4-6 qtrs | Q2-Q4 FY28 | T035 L321 | initiated |
| C05 | Synergies visible in the coming two quarters | by Q4 FY27 results | T033 L305-308 | underway ("already mapped all these synergies") |
| C06 | Separate organic vs synergy slides in the investor presentation | Q3 FY27 deck onward | T033 L308-311 | initiated (hedged: "will try") |
| C07 | KPI reporting by developer / broker / consumer segment; "follow up with the numbers" | undated (Q3 FY27 onward implied) | T031 L286-287, L294-295 | initiated |
| C08 | Distribution includes a full quarter of Housing.com from Q3 | Q3 FY27 results | T005 L172 | scheduled |
| C09 | KuberX Rs2,400 Cr run rate to Rs25,000 Cr | 4-6 qtrs: Q2-Q4 FY28 | T015 L212-216; T044 L339 | initiated ("recently launched", L211) |
| C10 | Revenue per team member up QoQ for 10-12 qtrs; 56 lakh by year end | Mar-2027 (56 lakh); about FY29-FY30 (QoQ run) | T003 L69; T035 L323 | underway |
| C11 | Network occupancy 88% | "end of this year" (Mar-2027 or Dec-2026, ambiguous) | T029 L276-277 | underway |
| C12 | Rental consolidation done; beds to grow; no net bed cuts | next quarter test (Q3 FY27) | T029 L270-273, L277 | completed (consolidation); initiated (growth) |
| C13 | No inorganic deal in the short run | undated | T041 L333-334 | standing |
| C14 | Restart rent and education payments with Housing.com and Nestaway | undated | T044 L341-342 | initiated ("currently evaluating") |
| C15 | Optimise use of Locon carry-forward losses; taking opinion | undated | T058 L382-385 | initiated ("yet to be seen") |
| C16 | FY27 priorities: improve financial metrics each quarter; integration roadmap on time; AI across five layers | each quarter to Mar-2027 | T003 L80-83 | underway |
| C17 | Warrant balance Rs88.5 Cr payable on exercise within 18 months | about Apr-2028 | T005 L156-157 | initiated (25% received 13-Oct) |
| C18 | Channel partners 18-19k to 50,000; developers 1,300+ to 4,000+ | undated | T050 L361, L363 | initiated |
| C19 | Distribution growth "exponential", not sequential | undated | T031 L289-290 | initiated |
| C20 | AI consumer-journey investment; results not yet visible | undated | T035 L324 | underway |
| C21 | Housing.com PPA may be refined in the 12-month measurement period | by about 29-Sep-2027 | T005 L152-153 | initiated (provisional) |
| C22 | Next connect "next week" | about 23-Oct-2026 | T064 L413 | scheduled (possibly misheard; a live channel for questions if real) |

## 4. SILENCE AUDIT: WHAT WAS NOT DISCUSSED (F17)

### 4a. Notion monitoring checklist (9 items)

| # | item | call status | cite | consecutive quarters unanswered |
|---|---|---|---|---|
| 1 | Operating profit ex one-times | NOT ADDRESSED on substance. The call frames "fourth consecutive profitable quarter" and gives no OI amount. It admits capitalised product development of Rs8.8 Cr H1 (L164). Trigger 1 FIRED on the filing. | L45, L138, L164 | 2 (Q1, Q2) |
| 2 | Organic revenue ex-PropTiger YoY | NOT ADDRESSED. QoQ organic only. | L128-130, L170 | 2 |
| 3 | SM-REIT first scheme with AUM | SILENT. No mention in 417 lines. | L175 (Capital = KuberX only) | at least 6 concalls (Q1 RED + this call) |
| 4 | Receivables >1yr buckets | SILENT. | L163 (cash section, no receivables) | 2 (FY26 ageing also missing) |
| 5 | Rental segment breakeven | ADDRESSED (claim): Rs0.9 Cr profit, "profitable across the rental segment". Basis is before lease interest (A3C-07). | L174, L272 | 0 |
| 6 | Distribution margin >=12% | ADDRESSED (partial): segment result 16.3%. No EBITDA or loaded margin. Housing.com goes in from Q3. | L171-172 | 0 (comparability breaks Q3) |
| 7 | Goodwill not impaired | PARTIAL: goodwill plus intangibles Rs960 Cr, PPA provisional. No impairment, CGU or amortisation view. | L151-153 | 1 |
| 8 | Audit / RPT / auditor; AREDL loan test; Rs9.52 Cr borrower | SILENT. | L156 (only AREDL mention) | 2 (AREDL loan test: 1, named 14-Oct) |
| 9 | July-2026 fund-raise use of proceeds | PARTIAL: amounts stated. Objects not stated. | L151, L156-157 | 2 |

### 4b. Prior-quarter (Q1 FY27) questions

| # | question (short) | call status | cite |
|---|---|---|---|
| 1 | Organic Distribution ex-PropTiger | NOT ADDRESSED | L169-170 |
| 2 | Housing.com swap ratio, consideration, pro-forma shares, accretion | PARTIAL: all-stock, 1.98 Cr shares, Rs458 Cr. No accretion view. | L124, L151, L222-223 |
| 3 | AREDL warrants: price, cash, timeline, use, valuer | PARTIAL: Rs29.5 Cr, 25%, 51 lakh, Rs88.5 Cr, 18 months. Use and valuer silent. | L156-157 |
| 4 | FY26 receivables ageing | NOT ADDRESSED | none (searched L24-417) |
| 5 | SM-REIT filed, AUM, date | NOT ADDRESSED | none |
| 6 | Rental margin band, sustainability | PARTIAL: profitable claim, 88% occupancy target, beds to grow. No band. | L270-277 |
| 7 | Standalone OI composition | PARTIAL (claim only): consolidated OI "mainly treasury". No standalone split. | L138 |
| 8 | Distribution margin FY27 target; PropTiger mix | PARTIAL: 16.3% stated. No target or mix. | L171 |
| 9 | Fully diluted share count; FY27 EPS | NOT ADDRESSED | L151, L156 (components only) |
| 10 | Housing.com revenue and EBITDA; guide | PARTIAL: no base financials. Forward: 12-18 months, 4-6 / 6-8 qtrs, Rs120 Cr cut, +Rs150 Cr revenue, Rs1,020 Cr losses. | L61, L222-223, L234, L318, L321, L381 |

Tally: 0 fully, 6 partial, 4 not addressed.

### 4c. Role 4 review Step 8.5 questions (22)

| # | topic | call status | cite |
|---|---|---|---|
| 1 | Q2 OI composition | NOT ADDRESSED (claim "mainly treasury", no amounts) | L138 |
| 2 | Locon financials; separate Q3 segment | PARTIAL: Housing.com goes into Distribution (no separate segment); "try" to show organic vs synergy; no financials | L172, L222-223, L308 |
| 3 | Integration date, synergy Rs Cr, one-time cost | PARTIAL: synergies in 2 quarters; Rs120 Cr cut; "roadmap on time" with no date; integration cost silent | L82, L307-308, L318 |
| 4 | Intangible classes, lives, amortisation, CGU | PARTIAL: Rs960 Cr total; PPA provisional | L151-153 |
| 5 | DTA/DTL by entity; note 12 sign | PARTIAL: DTL Rs50.4 Cr; ETR explanation; note 12 silent | L144, L162 |
| 6 | Rs9.52 Cr loan borrower; AREDL balance | NOT ADDRESSED | none |
| 7 | Warrant objects; non-exercise | NOT ADDRESSED (amounts only) | L156-157 |
| 8 | Weighted share bridge | NOT ADDRESSED; EPS 0.52 repeated | L146 |
| 9 | Distribution by brand; segment EBITDA | NOT ADDRESSED; KPIs only (280 projects, 134 developers, 1.7 lakh leads, 10,500+ licences, 982 clients) | L290-292 |
| 10 | PropTiger gross vs net | NOT ADDRESSED; "gross emissions growing 144%" repeated | L99-100 |
| 11 | Adjusted EBITDA Q2 FY26 base | PARTIAL: +840 bps to 11.5% implies a 3.1% base; Ind AS line silent | L89 |
| 12 | Lease payments by brand | NOT ADDRESSED; group lease totals only | L161, L165 |
| 13 | Expense-ratio claim | PARTIAL: ratios restated; the call's own numbers rise QoQ (A3C-17) | L131-134 |
| 14 | Rental after lease interest | NOT ADDRESSED | L141, L174 |
| 15 | NestAway 7.6x base | NOT ADDRESSED; 7.6x repeated | L107 |
| 16 | Receivables ageing; provision | NOT ADDRESSED | none |
| 17 | Integrow abeyance; SM-REIT vehicle; associate swing | PARTIAL: associate share Rs0.2 Cr only | L142 |
| 18 | SM-REIT filing | NOT ADDRESSED | none |
| 19 | HelloWorld Living Pvt Ltd review scope | NOT ADDRESSED | none |
| 20 | +57% basis | PARTIAL: 56% on total income, implied base about Rs87.8 Cr | L88 |
| 21 | "business combination" disclaimer | PARTIAL (indirect): no other deal implied by the M&A pause | L333-334 |
| 22 | Capitalised team cost policy | PARTIAL: "mostly capitalized product development" Rs8.8 Cr H1; policy and amortisation silent | L164 |

Tally: 0 fully, 10 partial, 12 not addressed. The top-3 review questions (Q2 Housing.com financials, Q6 Rs9.52 Cr borrower and AREDL balance, Q8 share bridge) all remain open. Q6 and Q8 got total silence.

### 4d. Other silences worth a question
- The Q3 D&A step-up from Locon intangibles amortisation (A3C-14).
- The one-time severance or integration charge from the "very deep" cuts (A3C-04).
- Housing.com headcount and its effect on revenue per team member (A3C-10).
- KuberX legal entity, segment, and gross vs net take rate (A3C-09).

## 5. FLAGGED FOR A4
- FORWARD-SIGNAL: A3C-03, 05, 06, 09, 10, 12, 14.
- AMBIGUOUS: A3C-02, 04, 07, 08, 13, 15, 16, 18, 19, 20, 22, 23, 27, 28, 29, 30.
- CONFIRMATORY-NEGATIVE (context): A3C-01, 11, 17, 26.

```yaml
stage: A3-forensics
company: "AURUM"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\aurum-q2fy27\\work\\forensics_concall_aurum_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
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
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3C-01", check: "F17", line: "L45, L46, L138, L143", classification: "CONFIRMATORY-NEGATIVE", implication: "Call frames 'fourth consecutive profitable quarter' without the OI amount; PBT Rs6.8 Cr sits under filed OI Rs7.12 Cr; trigger 1 stays FIRED; 2 quarters unanswered"}
  - {id: "A3C-02", check: "F17", line: "L138, L154-155", classification: "AMBIGUOUS", implication: "Treasury plus loan interest explains about Rs3.6-3.9 Cr of Rs7.12 Cr OI [INFERENCE]; ask for the Q2 split"}
  - {id: "A3C-03", check: "F6", line: "L61, L222-223, L234, L237-239", classification: "FORWARD-SIGNAL", implication: "Housing.com target in two tiers (internal 4-6 qtrs, external 6-8 qtrs to about Q2 FY29); metric undefined; no base disclosed"}
  - {id: "A3C-04", check: "F6", line: "L317-318, L320, L321", classification: "AMBIGUOUS", implication: "Rs120 Cr cut period basis and Housing.com base unstated; no severance charge mentioned; Q3 PBT exposure"}
  - {id: "A3C-05", check: "F12", line: "L172", classification: "FORWARD-SIGNAL", implication: "Housing.com goes inside Distribution from Q3; item 6 margin and item 2 organic lose comparability"}
  - {id: "A3C-06", check: "F7", line: "L294-295, L308-311", classification: "FORWARD-SIGNAL", implication: "Organic vs synergy slide hedged with 'try'; KPI reframe may drop current KPIs; run F16 on Q3 deck"}
  - {id: "A3C-07", check: "F12", line: "L139, L140-141, L161, L174, L272", classification: "AMBIGUOUS", implication: "Rental Rs0.9 Cr profit is before lease interest; after it, likely a loss of about Rs4-5 Cr [INFERENCE]; item 5 basis"}
  - {id: "A3C-08", check: "F17", line: "L154-155, L163-166", classification: "AMBIGUOUS", implication: "H1 continuing cash build about Rs4.2-4.6 Cr after lease principal; lease-interest CF location unstated; cash stays INDETERMINATE"}
  - {id: "A3C-09", check: "F6", line: "L211-216, L338-339", classification: "FORWARD-SIGNAL", implication: "KuberX 10.4x in 4-6 qtrs on a one-month run rate; at 1-1.2% revenue goes about Rs24-29 Cr to Rs250-300 Cr; segment and gross/net unstated"}
  - {id: "A3C-10", check: "F6", line: "L69, L323-324", classification: "FORWARD-SIGNAL", implication: "Revenue per team member promised up QoQ for 10-12 qtrs; cost-driven; Housing.com headcount moves it from Q3"}
  - {id: "A3C-11", check: "F7", line: "L324", classification: "CONFIRMATORY-NEGATIVE", implication: "AI consumer-journey revenue results not yet tangible; supports FLAG-NARRATIVE-VS-EVIDENCE"}
  - {id: "A3C-12", check: "F8", line: "L144, L162, L375, L378-385", classification: "FORWARD-SIGNAL", implication: "ETR about 37% persists; Rs1,020 Cr Locon losses do not shield group without merger [INFERENCE]; future DTA recognition could flatter PAT"}
  - {id: "A3C-13", check: "F10", line: "L145-146, L151, L156", classification: "AMBIGUOUS", implication: "EPS 0.52 implies about 865 lakh weighted shares vs about 769 lakh expected; bridge unanswered"}
  - {id: "A3C-14", check: "F11", line: "L140, L150-151", classification: "FORWARD-SIGNAL", implication: "Goodwill plus intangibles Rs960 Cr = 94% of equity; tangible equity about Rs60 Cr; Q3 D&A step-up unstated"}
  - {id: "A3C-15", check: "F11", line: "L147, L150-151", classification: "AMBIGUOUS", implication: "Call ties to about Rs510 Cr March equity; Notion 61%-of-NW implies about Rs286 Cr; gap about Rs226 Cr; check filed balance sheet"}
  - {id: "A3C-16", check: "F7", line: "L152-153", classification: "AMBIGUOUS", implication: "PPA provisional to about 29-Sep-2027; item 7 goodwill baseline can move without impairment"}
  - {id: "A3C-17", check: "F17", line: "L91, L131-136", classification: "CONFIRMATORY-NEGATIVE", implication: "Own numbers: opex 74.0% vs 72.9% of revenue QoQ and EBITDA margin 29.8% vs 31.5%; operating-leverage claim unsupported QoQ"}
  - {id: "A3C-18", check: "F14", line: "L57, L109, L364", classification: "AMBIGUOUS", implication: "MAU 45 mn vs 12 mn as heard; deck wins; leadership claim depends on it"}
  - {id: "A3C-19", check: "F14", line: "L104, L276-277", classification: "AMBIGUOUS", implication: "Occupancy 82% now, 88% target 'end of this year' (FY or CY unclear); deck wins"}
  - {id: "A3C-20", check: "F14", line: "L47, L90, L143", classification: "AMBIGUOUS", implication: "1270 bps PBT margin gain does not reconcile with Rs(8.9) Cr Q2 FY26 PBT; basis mixing likely"}
  - {id: "A3C-21", check: "F14", line: "L88-89", classification: "NEUTRAL-FACT", implication: "+840 bps implies a 3.1% base (slide 3, not -3.2%); 56% growth implies about Rs87.8 Cr base incl. discontinued"}
  - {id: "A3C-22", check: "F15", line: "L124, L142, L156, L211, L215", classification: "AMBIGUOUS", implication: "Locon added; KuberX entity and segment unnamed; 'Integral' likely Integrow; AMSA and Integrow absent"}
  - {id: "A3C-23", check: "F13", line: "L389-390, L400", classification: "AMBIGUOUS", implication: "Directors' integration subcommittee; composition, mandate and independents unstated"}
  - {id: "A3C-24", check: "F17", line: "L28-29", classification: "NEUTRAL-FACT", implication: "CFO listed, no inferred turn; deputy CFO read financials; absence unconfirmed (machine speakers)"}
  - {id: "A3C-25", check: "F6", line: "L222, L333-334", classification: "NEUTRAL-FACT", implication: "Undated M&A pause after eighth acquisition in four years"}
  - {id: "A3C-26", check: "F17", line: "L175, L207-216", classification: "CONFIRMATORY-NEGATIVE", implication: "SM-REIT not mentioned; trigger 3 condition extends to at least 6 concalls"}
  - {id: "A3C-27", check: "F17", line: "L128-130, L169-170", classification: "AMBIGUOUS", implication: "Organic given QoQ only; YoY ex-PropTiger unanswered 2nd quarter; Q3 perimeter changes again"}
  - {id: "A3C-28", check: "F17", line: "L163", classification: "AMBIGUOUS", implication: "Receivables ageing and Rs4.44 Cr provision silent; 2nd quarter"}
  - {id: "A3C-29", check: "F17", line: "L156", classification: "AMBIGUOUS", implication: "Rs9.52 Cr loan borrower, AREDL loan test, auditor and RPT silent; lean bear"}
  - {id: "A3C-30", check: "F17", line: "L151, L156-157", classification: "AMBIGUOUS", implication: "Warrant and swap amounts tie to Notion; use of proceeds and non-exercise plan silent"}
  - {id: "A3C-31", check: "F17", line: "L325-328", classification: "NEUTRAL-FACT", implication: "Yash Sajpal (IFC) question not heard; not on record"}
forward_signals: ["A3C-03", "A3C-05", "A3C-06", "A3C-09", "A3C-10", "A3C-12", "A3C-14"]
ambiguous: ["A3C-02", "A3C-04", "A3C-07", "A3C-08", "A3C-13", "A3C-15", "A3C-16", "A3C-18", "A3C-19", "A3C-20", "A3C-22", "A3C-23", "A3C-27", "A3C-28", "A3C-29", "A3C-30"]
commitments:
  - {commitment: "Housing.com profitable within 12-18 months", implied_date: "Sep-2027 to Mar-2028", ref: "T003 L61", status_word: "initiated"}
  - {commitment: "Housing.com break-even 4-6 qtrs internal, 6-8 qtrs external", implied_date: "Q2-Q4 FY28 internal; to Q2 FY29 external", ref: "T026 L234, L237-239", status_word: "initiated"}
  - {commitment: "Rs120 Cr cost cut at Housing.com in first week", implied_date: "Oct-2026", ref: "T035 L317-318, L321", status_word: "completed"}
  - {commitment: "Housing.com revenue +Rs150 Cr over 4-6 qtrs", implied_date: "Q2-Q4 FY28", ref: "T035 L321", status_word: "initiated"}
  - {commitment: "Synergies visible in coming two quarters", implied_date: "by Q4 FY27", ref: "T033 L305-308", status_word: "underway"}
  - {commitment: "Separate organic vs synergy slides in investor presentation (will try)", implied_date: "Q3 FY27 deck onward", ref: "T033 L308-311", status_word: "initiated"}
  - {commitment: "KPI reporting by developer/broker/consumer segment", implied_date: "undated (Q3 FY27 implied)", ref: "T031 L286-287, L294-295", status_word: "initiated"}
  - {commitment: "Distribution includes full quarter of Housing.com", implied_date: "Q3 FY27", ref: "T005 L172", status_word: "scheduled"}
  - {commitment: "KuberX Rs2,400 Cr to Rs25,000 Cr run rate", implied_date: "Q2-Q4 FY28", ref: "T015 L212-216; T044 L339", status_word: "initiated"}
  - {commitment: "Revenue per team member up QoQ 10-12 qtrs; 56 lakh by year end", implied_date: "Mar-2027; about FY29-FY30", ref: "T003 L69; T035 L323", status_word: "underway"}
  - {commitment: "Network occupancy 88%", implied_date: "end of this year (Mar-2027 or Dec-2026)", ref: "T029 L276-277", status_word: "underway"}
  - {commitment: "Rental consolidation done; beds to grow, no net cuts", implied_date: "Q3 FY27 test", ref: "T029 L270-273, L277", status_word: "completed"}
  - {commitment: "No inorganic deal in the short run", implied_date: "undated", ref: "T041 L333-334", status_word: "standing"}
  - {commitment: "Restart rent and education payments with Housing.com and Nestaway", implied_date: "undated", ref: "T044 L341-342", status_word: "initiated"}
  - {commitment: "Optimise use of Locon carry-forward losses; taking opinion", implied_date: "undated", ref: "T058 L382-385", status_word: "initiated"}
  - {commitment: "FY27 priorities: metrics up each quarter; integration roadmap on time; AI in five layers", implied_date: "to Mar-2027", ref: "T003 L80-83", status_word: "underway"}
  - {commitment: "Warrant balance Rs88.5 Cr on exercise within 18 months", implied_date: "about Apr-2028", ref: "T005 L156-157", status_word: "initiated"}
  - {commitment: "Channel partners to 50,000; developers to 4,000+", implied_date: "undated", ref: "T050 L361, L363", status_word: "initiated"}
  - {commitment: "Distribution growth exponential, not sequential", implied_date: "undated", ref: "T031 L289-290", status_word: "initiated"}
  - {commitment: "AI consumer-journey investment; tangible results pending", implied_date: "undated", ref: "T035 L324", status_word: "underway"}
  - {commitment: "Housing.com PPA may be refined in 12-month window", implied_date: "by about 29-Sep-2027", ref: "T005 L152-153", status_word: "initiated"}
  - {commitment: "Next connect next week", implied_date: "about 23-Oct-2026", ref: "T064 L413", status_word: "scheduled"}
gate_a3: pass
blank_checks: []
analyst_note: "The call's profit story rests on other income it never quantifies. Q2 PBT of Rs6.8 Cr (L143) sits below filed OI of Rs7.12 Cr, so trigger 1 stays FIRED and 'fourth consecutive profitable quarter' (L45) is framing, not new evidence. Three items decide Q3. Housing.com folds into Distribution (L172), so items 2 and 6 lose comparability unless the promised organic/synergy slide appears; it is hedged with 'try' (L308). Locon base financials stay undisclosed while a Rs120 Cr cut and Rs150 Cr revenue bridge are offered (L318, L321). Locon intangibles start amortising with equity 94% intangible (L150-151). Tax: Locon's Rs1,020 Cr losses likely do not shield other group entities without a merger [INFERENCE]; management says 'yet to be seen' (L383). Cash: the H1 continuing build after lease principal was about Rs4-5 Cr; the building sale and acquired cash explain the rest. SM-REIT is absent again. Of 22 review questions, 12 got silence, including Q6 (Rs9.52 Cr borrower) and Q8 (share bridge). The MAU and occupancy conflicts go to the deck; the filing wins. The equity tie-out against Notion's 61%-of-NW line needs the filed balance sheet."
```
