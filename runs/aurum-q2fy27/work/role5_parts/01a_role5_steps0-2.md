## ROLE 5: CONCALL ANALYSIS (Q2 FY27 call, 16-Oct-2026; machine transcript)

Agent: A4 analyst | model: claude-opus-5-5 | Role 5 addendum written 2026-10-18 | Protocol: Quarterly Concall Analysis Protocol v1.1 (frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md). Role 4 tables and numbers above are unchanged.

BINDING CAVEAT FOR THIS WHOLE SECTION: the source is a MACHINE TRANSCRIPT (faster-whisper medium.en), not an official transcript. Speakers are inferred by A1; numbers and names may be misheard. On any number conflict the filing wins. Every CALL-anchored statement below carries this caveat, written short as [MGMT-CALL*].

Anchor key addition: CALL Lnnn = extracted/aurum-concall-q2fy27-fulltext.md line; Tnnn = A2 turn; Qnn = A2 question; Rnnn = A1 structured row (extracted/aurum-concall-q2fy27-structured.md); A3C-nn = A3 concall finding (work/forensics_concall_aurum_q2fy27.md). RES, DECK, PR and NOTION anchors as in the Role 4 key.

Inputs read for Role 5: A1 concall structured and fulltext, A2 concall ledger, A3 concall forensics, the Role 4 review above, the three filing fulltexts (Step 7), and the Notion copy. Source audio, the raw transcript, and inputs/ were NOT opened.

### LEDGER RECONCILIATION PREAMBLE (Role 5)

Ledger contains 0 notes / 65 turns / 0 slides. All 65 turns reviewed. Also reviewed: 19 questions (Q01-Q19; Q12 not heard), 341 structured rows (R001-R341; 185 number, 43 entity, 54 forward, 23 date, 36 qualifier), 179 management-number rows. Ledger count test: all categories match, ids_in_structured 341, ids_referenced 341, orphan IDs none, gate_a2 pass (ledger L1-L13). Unreviewed rows: none.

Findings incorporated: [A3C-01, A3C-02, A3C-03, A3C-04, A3C-05, A3C-06, A3C-07, A3C-08, A3C-09, A3C-10, A3C-11, A3C-12, A3C-13, A3C-14, A3C-15, A3C-16, A3C-17, A3C-18, A3C-19, A3C-20, A3C-21, A3C-22, A3C-23, A3C-24, A3C-25, A3C-26, A3C-27, A3C-28, A3C-29, A3C-30, A3C-31] (31 IDs: 7 FORWARD-SIGNAL, 16 AMBIGUOUS, 4 CONFIRMATORY-NEGATIVE, 4 NEUTRAL-FACT).

Ledger annotations carried from A3: six line-cite offsets of 1-2 lines (R150, R218, R219, R227, R328, R339), no row lost; R200 "Integral" (CALL L142) is likely Integrow as heard, not flagged NAME_AS_HEARD by A2; CONFLICT_INCALL pairs R006/R015 (rounding) and R180/R181/R183 (approximation then exact figure) are not conflicts. A3C-26's statement that the SM-REIT count is "at least 6" is NOT carried: the record does not state that Q1 FY27 was the 5th call (see Step 8C).

---

### STEP 0: PRE-FLIGHT

#### 0A. Notion baseline (Decision Status verified BEFORE any framing)

| Field | Value | Anchor |
|---|---|---|
| Decision Status | AVOID (operator-only; never written by the pipeline) | NOTION L6 |
| Position | None; name NOT HELD, so Step 8E runs the 8A-W branch | NOTION L8 |
| One-line thesis | AVOID; BUY only on the three BUY-break conditions | NOTION L13 |
| Growth triggers | ND (not passed); BUY-break conditions used, as in Role 4 6D | NOTION L76 |
| Thesis-broken conditions | 4 | NOTION L25-L28 |
| Monitoring checklist | 9 items, Q1 FY27 status | NOTION L33-L46 |
| Promoter Verdict / Management Grade | CONCERN / ND (not passed) | NOTION L9 |
| Devil's Advocate findings | ND (not passed) | NOTION L76 |
| Previous concall log | ND: prior log not passed; no Q1 FY27 transcript on file | NOTION L73 |

Previous concall status: this is NOT the company's first concall. The chairman calls it "the 22nd earnings call of Aurum PropTech" (CALL L34) [MGMT-CALL*], and a management speaker refers to "one of the calls" with the same analyst (CALL L368). The protocol's first-concall skip therefore does not apply. Steps 3A-3D are marked ND (prior log not passed). This call opens the baseline promise log for the pipeline.

#### 0B. Call participants [MGMT-CALL*]

| Role | Name | Notes |
|---|---|---|
| Hosting broker / IR | MK Global Financial Services; host Shivang Pagla (CALL L24-L27) | House broker: 2 of the 10 heard questioners are from MK (Jimit Gandhi, Deepesh Mehta). Independence ND. |
| CMD / Chairman | Ashish Deora, non-executive chairman (CALL L28) | Founder of Aurum Ventures, the parent of Aurum PropTech (DECK L911-L913). Promoter PRESENT, in a non-executive role. |
| Managing Director | none listed | ND |
| CEO | none listed | ND |
| CFO | Kunal Karan (CALL L29) | Listed, but no inferred speaking turn (A3C-24). Absence unconfirmed: speakers are machine-inferred. |
| COO / Other senior | Onkar Shetye, executive director (CALL L29); Shikant Chaktap, deputy CFO, as heard (CALL L29); Rehan Shah, lead strategy and IR (CALL L30) | ED gave business performance (T004); deputy CFO read the financials (T005). |
| IR Advisor | Closing by "Sonia Duyishmukh" as heard (CALL L406); moderator "Aishwashi" as heard (CALL L407) | Firm and role ND |

Yellow flags from the participant list:
- CFO listed but silent; the deputy CFO presented the financials (A3C-24). Unconfirmed.
- Unlisted names appear in management turns as heard: "Priyayan" (CALL L200) and "Rokat" (CALL L360). They may be mishearings of listed people. Q&A management speakers are SPEAKER_UNRESOLVED in every A2 management turn, so the "CFO answering operational questions" test is NOT DETERMINABLE.
- Promoter absence: no. The founder chairman is on the call. The analyst at CALL L387 addresses the answerer "as the founder of the company" [INFERENCE: Ashish Deora answered T058-T060].
- IR firm talking more than management: no.

#### 0C. Call structure and date

| Item | Reading | Anchor |
|---|---|---|
| Call date | 16-Oct-2026, evening ("good evening", CALL L33) | CALL L20 |
| Quarter reviewed | Q2 FY27 | CALL L27 |
| Gap to filing | Same day as the board approval of results (note C1, RES L525): "same day = canned" per protocol | RES L525 |
| Call duration | about 59 minutes (00:00:18 to 00:59:22) | CALL L24, L417 |
| Opening remarks | about 18 minutes (00:01:28 to 00:19:35) | CALL L33, L179 |
| Q&A duration | about 39 minutes (00:19:39 to 00:58:26), about 66% of the call | CALL L180, L405 |
| Questioners | 11 queued, 10 heard; 19 questions; 4 of the 10 heard questioners were text questions read by the moderator | ledger L130; CALL L207, L312, L328, L336 |

#### 0D. Safe harbour

One sentence: statements "may be forward-looking in nature and subject to risks and uncertainties as detailed in annual report and other investor disclosures" (CALL L31) [MGMT-CALL*]. Breadth: narrow and generic. New caveats against the prior call: ND (prior transcript not passed). The breadth is now on record for the Q3 FY27 diff.

#### 0E. Business type

Standard operating business. KuberX is home-loan distribution that earns a bank commission of "1 to 1.2% of the disbursed value" (CALL L338) [MGMT-CALL*]; it is not balance-sheet lending. The Capital segment holds a lending platform (DECK L139-L140) but is 3.3% of revenue (RES L369, L370). Step 2 standard rows apply; Step 2L does not.

Checkpoint: Notion fetched (AVOID verified), participants listed, structure noted, caveats logged, business type stated.

---

### STEP 1: OPENING REMARKS, CLAIMS INVENTORY [MGMT-CALL*]

Opening remarks = T003 (chairman, CALL L33-L84), T004 (executive director, CALL L86-L117) and T005 (deputy CFO, CALL L118-L179).

| # | Claim | Type | Quantified? | Source Line |
|---|---|---|---|---|
| 1 | This is "the 22nd earnings call of Aurum PropTech" | Backward | YES | CALL L34 |
| 2 | Since 2021 the group builds to capture the end-to-end real estate value chain | Strategic | NO | CALL L36 |
| 3 | Housing.com marks the beginning of "Aurum PropTech 2.0" | Strategic | NO | CALL L37 |
| 4 | Vision: India's AI-native real estate operating system | Strategic | NO | CALL L39 |
| 5 | Promise of "the best ROI in the industry" to developers, consumers, partners | Strategic | NO | CALL L41 |
| 6 | "Q2 of FY27 is our fourth consecutive profitable quarter" | Backward | YES | CALL L45 |
| 7 | A full year of profitability shows unit economics "tested through the cycle" | Backward | NO | CALL L46 |
| 8 | Q2 is the industry's softest quarter; PBT margin up "1200 plus basis points" | Backward | YES | CALL L47 |
| 9 | Housing is "the largest possible opportunity in the PropTech segment" | Macro/Tailwind | NO | CALL L49 |
| 10 | Housing.com has "58 million plus visits every month" | Operational | YES | CALL L57 |
| 11 | Deep cost optimisation and AI-led initiatives at Housing.com already begun | Operational | NO | CALL L60 |
| 12 | Housing.com profitable "within 12 to 18 months" (repeated) | Forward Guidance | YES | CALL L61 |
| 13 | Synergies being unlocked across all three segments | Forward Soft | NO | CALL L62 |
| 14 | "Broker first" endeavour | Strategic | NO | CALL L63-L64 |
| 15 | Potential to become a "virtual partner" to developers | Forward Soft | NO | CALL L65 |
| 16 | Revenue per team member up quarter on quarter "for next 10 to 12 quarters" | Forward Guidance | YES | CALL L69 |
| 17 | Medium-term seamless consumer layer from discovery to living | Forward Soft | NO | CALL L70-L72 |
| 18 | Evolving into "the single largest platform with network effects" | Strategic | NO | CALL L74 |
| 19 | Aurum "has triggered consolidation in the Indian PropTech segment" | Macro/Tailwind | NO | CALL L76-L77 |
| 20 | Sector business models will move to profitability "taking a cue from Aurum" | Macro/Tailwind | NO | CALL L78-L79 |
| 21 | FY27 focus 1: "improving our financial metrics each quarter" (no metric named) | Forward Soft | NO | CALL L81 |
| 22 | FY27 focus 2: Housing.com integration roadmap "on time" (no date) | Forward Soft | NO | CALL L82 |
| 23 | FY27 focus 3: AI "across all five layers" | Forward Soft | NO | CALL L83 |
| 24 | Total income 137 Cr, +56% YoY | Backward | YES | CALL L88 |
| 25 | Adjusted EBITDA margin +840 bps to 11.5% | Backward | YES | CALL L89 |
| 26 | PBT margin +1270 bps to 4.8% | Backward | YES | CALL L90 |
| 27 | Performance reflects "improving monetization, cost discipline and increasing operating leverage" | Backward | NO | CALL L91 |
| 28 | Distribution revenue 70 Cr, segment profit 11 Cr | Backward | YES | CALL L94 |
| 29 | 1,70,000 leads (+79% YoY), 10,560 licences, 850 Cr home sales, gross commission (heard "emissions") +144% | Operational | YES | CALL L97-L100 |
| 30 | Rental revenue 56 Cr | Backward | YES | CALL L103 |
| 31 | 16,500 beds at 82% occupancy; 137 buildings above 90% | Operational | YES | CALL L104-L105 |
| 32 | 8,900 signed units, 35 Cr quarterly rent, AI bookings 7.6x QoQ | Operational | YES | CALL L106-L107 |
| 33 | Housing.com 45 mn monthly active users, 1.2x nearest competitor, 52% of app downloads | Strategic | YES | CALL L108-L110 |
| 34 | Housing.com ranks number one on brand awareness, consideration and preference | Strategic | NO | CALL L111-L112 |
| 35 | "Operating business delivered its strongest quarter yet"; revenue +64% to 130.2 Cr; profit from continuing operations | Backward | YES | CALL L122-L123 |
| 36 | Housing.com acquired 29-Sep via Locon, all-stock; balance sheet "roughly doubles" | Backward | YES | CALL L124-L125 |
| 37 | Revenue 130.2 Cr (+64% YoY, +16% QoQ); H1 242 Cr (+67%) | Backward | YES | CALL L126-L127 |
| 38 | QoQ growth of 16% "is entirely organic" (perimeter effectively unchanged) | Backward | YES | CALL L130 |
| 39 | Employee cost 34.2 Cr = 26.2% of revenue (Q1 27.9%); other expenses 62.2 Cr = 47.8% (Q1 45%; YoY 49.5%) | Backward | YES | CALL L131-L134 |
| 40 | EBITDA 41 Cr, 29.8% of total income; H1 78.5 Cr, 30.6% | Backward | YES | CALL L135-L137 |
| 41 | "Other income is mainly treasury and deposit income" (no amount) | Backward | NO | CALL L138 |
| 42 | D&A 28.1 Cr, finance cost 6.3 Cr, broadly flat; almost no bank debt; associate share 0.2 Cr | Backward | YES | CALL L140-L142 |
| 43 | PBT 6.8 Cr (Q2 FY26 loss 8.9 Cr; Q1 1.3 Cr); tax 2.5 Cr, ETR about 37%; PAT 4.3 Cr, 4.5 Cr to owners; EPS 0.52 | Backward | YES | CALL L143-L146 |
| 44 | H1 net profit 49.5 Cr incl. 45.5 Cr discontinued; building sale 112 Cr, pre-tax gain 52.4 Cr; H1 continuing PAT 3.9 Cr | Backward | YES | CALL L147-L149 |
| 45 | Total assets 1,641 Cr (March 948 Cr); equity "roughly doubled to 1,020 crore" | Backward | YES | CALL L150 |
| 46 | 1.98 Cr shares to REA India, 458 Cr to equity; goodwill and intangibles 960 Cr | Backward | YES | CALL L151 |
| 47 | Housing.com PPA provisional; may be refined in the 12-month measurement period | Forward Soft | YES | CALL L152-L153 |
| 48 | Cash, bank and current investments 191.6 Cr (March 141 Cr), incl. 22 Cr from Housing.com | Backward | YES | CALL L154-L155 |
| 49 | 29.5 Cr warrant money received 13-Oct; 88.5 Cr payable on exercise within 18 months | Backward / Forward | YES | CALL L156-L157 |
| 50 | Current assets 399 Cr vs current liabilities 404 Cr, incl. 78.3 Cr lease liabilities | Backward | YES | CALL L158-L159 |
| 51 | Borrowings under 1 Cr; lease liabilities 216 Cr vs RoU 196.8 Cr; DTL 50.4 Cr "non-cash" | Backward | YES | CALL L160-L162 |
| 52 | H1 OCF 60.8 Cr (25.4 Cr); capex 8.8 Cr; lease principal 47.8 Cr; OCF "covered both product investment and our full lease commitments" | Backward | YES | CALL L163-L165 |
| 53 | Discontinued operations net cash 24 Cr | Backward | YES | CALL L166 |
| 54 | Distribution 69.7 Cr, 54%, +25% QoQ, 2.6x YoY; result 11.4 Cr, 16.3% (5.5 Cr, 8 Cr) | Backward | YES | CALL L169-L171 |
| 55 | "From Q3, distribution will include a full quarter of housing" | Forward Guidance | YES | CALL L172 |
| 56 | Rental 56.1 Cr (+10% YoY, +3% QoQ); profit 0.9 Cr vs loss 4.3 Cr | Backward | YES | CALL L173-L174 |
| 57 | Capital 4.3 Cr (Q1 1.6 Cr, year ago 1.2 Cr); profit 0.4 Cr | Backward | YES | CALL L175 |
| 58 | Enter H2 "with a larger platform and strong balance sheet" | Forward Soft | NO | CALL L178 |

Mandatory diagnostics:
1. Quantified share: 37 of 58 claims (63.8%). Of the 37, 32 are backward. Of the 12 forward claims (rows 12, 13, 15, 16, 17, 21, 22, 23, 47, 49, 55, 58), 5 are quantified (41.7%). The opening is specific about the past and soft about the future.
2. New vs reaffirmed: the prior transcript was not passed, so no row can be classed against a prior call. Against the same-quarter documents, row 6 reaffirms PR L80 ("fourth consecutive quarter of positive PBT"). New to the record: rows 12 and 16, and in Q&A the KuberX target, the Rs120 Cr cut and the 4-6 / 6-8 quarter break-even tiers.
3. Quietly dropped (expected, absent): SM-REIT (the deck still lists an "SM REIT investment platform" offering, DECK L135, L441-L443); the other-income amount; the Integrow control abeyance ending 31-Mar-2027 (RES L585); the Rs9.52 Cr external loan; the named AREDL loan test (NOTION L52).
4. Internal contradictions: (a) "increasing operating leverage" (row 27) against the deputy CFO's own ratios, other expenses up from 45% to 47.8% of revenue QoQ and EBITDA margin down from 31.5% to 29.8% (rows 39-40; A3C-17). (b) "fourth consecutive profitable quarter" (row 6) while Q2 PBT of 6.8 Cr sits below other income of Rs7.12 Cr (RES L309; A3C-01). (c) "Rental has turned profitable" (CALL L168) while the deputy CFO says co-living rent sits in D&A and finance cost (CALL L139-L141; A3C-07). (d) "1200 plus" bps (row 8) vs "1270" bps (row 26): rounding and basis, see Step 7A.

Checkpoint: inventory and four diagnostics shown.

---

### STEP 2: FORWARD GUIDANCE EXTRACTION [MGMT-CALL*]

Prior columns: ND, prior log not passed. Trajectory is therefore "New to the record" for every row. That label means new to this pipeline's log, not proven new to the company.

| Metric | This Quarter's Guidance | Last Quarter's Guidance | Two Quarters Ago | Trajectory | Confidence Level |
|---|---|---|---|---|---|
| Revenue growth (FY27) | ND (no group guide). Soft only: "improving our financial metrics each quarter" (CALL L81) | ND | ND | New to the record | LOW |
| Revenue growth (FY28) | ND for the group. Housing.com: "revenue growth of another 150 crores over next four to six quarters" (CALL L321) | ND | ND | New to the record | MEDIUM ("we believe"; base undisclosed) |
| EBITDA margin band | ND for the group. Housing.com "profitable within 12 to 18 months" (CALL L61); "break even in four to six quarters ... internal target, six to eight quarters is our external target ... profitable with housing before that" (CALL L234, L237-L239) | ND | ND | New to the record | MEDIUM (two tiers; metric undefined) |
| Order book / pipeline | n.a. (services). Distribution growth "not going to be sequential. It's going to be exponential" (CALL L289-L290); channel partners 18-19k to 50,000, developers 1,300+ to 4,000+, undated (CALL L361, L363) | ND | ND | New to the record | LOW |
| Capex envelope | ND | ND | ND | n.a. | n.a. |
| Utilization target / timeline | Network occupancy 82% now, "88% occupancy by the end of this year" (CALL L276-L277); beds to grow, "no reason to cut beds now on a net basis" (CALL L270-L277) | ND | ND | New to the record | MEDIUM (year undefined: Dec-2026 or Mar-2027) |
| Strategic order execution timeline | Synergies visible "in the coming two quarters" (CALL L307-L308); integration roadmap "on time", no date (CALL L82); Housing.com cost cut of about 120 Cr "already done" (CALL L318, L321) | ND | ND | New to the record | MEDIUM |
| Working capital / CCC band | ND | ND | ND | n.a. | n.a. |
| Net debt trajectory | ND. Backward: "effectively debt-free" (CALL L160). Warrant balance 88.5 Cr on exercise within 18 months (CALL L157) | ND | ND | New to the record | HIGH on the warrant terms (filed, RES L569-L571); exercise is AREDL's option |
| Export / segment guidance | "From Q3, distribution will include a full quarter of housing" (CALL L172); KuberX 2,400 Cr run rate to 25,000 Cr disbursal "in next four to six quarters" at a 1-1.2% take rate (CALL L212-L216, L338-L339); KPIs to move to developer / broker / consumer segments (CALL L294-L295) | ND | ND | New to the record | HIGH (Q3 segment inclusion, binary); MEDIUM (KuberX); LOW (KPI reframe) |
| New product / contract milestones | Rent and education payments to restart with Housing.com and NestAway, "currently evaluating", undated (CALL L341-L342); AI consumer journey, "yet to see defined and tangible results" (CALL L324) | ND | ND | New to the record | LOW |
| Dividend / payout policy | ND | ND | ND | n.a. | n.a. |
| Revenue per team member (added row) | "go up quarter on quarter for next 10 to 12 quarters" (CALL L69); 40 lakh to "50 plus lakhs", target "56 lakhs by the end of the year" (CALL L323) | ND | ND | New to the record | MEDIUM (definition unstated) |
| Disclosure promise (added row) | "We will try to articulate that separately in different slides ... what is organic and what is coming out of synergies" (CALL L308-L311) | ND | ND | New to the record | LOW ("try") |
| Tax (added row) | Locon carry-forward losses 1,020 Cr; use "yet to be seen"; "taking more opinion" (CALL L378-L385) | ND | ND | New to the record | LOW |
| M&A (added row) | "we will not do something inorganic in a short run for sure" (CALL L333-L334), undated | ND | ND | New to the record | LOW |

Diagnostics:
- Widened or tightened: NOT TESTABLE (no prior log).
- Dropped without acknowledgement: NOT TESTABLE against a prior call. Same-quarter test: SM-REIT sits in the deck as an offering (DECK L135) and is absent from all 417 call lines (A3C-26).
- Internal consistency: (1) Housing.com: "profitable within 12 to 18 months" (CALL L61) equals 4-6 quarters, consistent with the internal break-even tier, but "we will be profitable with housing before that" (CALL L238-L239) puts profit before break-even. The metric is undefined. (2) The cost and revenue bridge cannot be checked. Management declined to give Housing.com numbers ("still early days", CALL L222-L223). [INFERENCE] Losses of 1,020 Cr over 10-12 years (CALL L381) average about 85-102 Cr a year. An annual cut of about 120 Cr with no revenue dip (CALL L320) would then make Housing.com profitable at once. Yet management needs a further 150 Cr of revenue over 4-6 quarters. So either the recent loss run-rate is far above the average, or the 120 Cr is not an annual figure, or the cut is gross of reinvestment. (3) KuberX: 25,000 Cr x 1-1.2% = Rs250-300 Cr of annual commission [derived], against Capital segment Q2 revenue of Rs4.33 Cr (RES L369) and group FY26 revenue of Rs381.10 Cr (RES L370). The September run rate gives Rs24-29 Cr a year [derived]. The target is a 10.4x scale-up in 4-6 quarters on one month of data.
- Against Four-Pillar projections: ND (projections not passed). The only forward figure on record is the operator house case: FY31 revenue about Rs1,100 Cr at an 8% PAT margin (NOTION L17). Pillar comparison deferred (OR-30).
- Guidance refused when pressed: Housing.com quarterly or annual numbers (Q04, CALL L222-L223); transaction volumes (Q05, CALL L231-L232, not given); segment most hit in a downturn (Q02, CALL L202-L205, not given); AI investment amount (Q11, CALL L315, not given); restart date for rent and education payments (Q16, CALL L337, not given).

Checkpoint: guidance table and diagnostics shown.
