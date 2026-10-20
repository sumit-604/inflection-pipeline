# HFCL LIMITED (HFCL): Q2 FY27 ROLE 5 ADDENDUM (CONCALL ANALYSIS, A4 ANALYST)

Call: 19-Oct-2026, 16:30 IST, hosted by Nuvama Institutional Equities. Quarter: Q2 and H1 FY27.
Protocol: Role 5, Quarterly Concall Analysis Protocol v1.1 (frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md).
Companion: Role 4 review runs/hfcl-q2fy27/work/review_hfcl_q2fy27.md (not rewritten here). Role 5 Step 8D: deferred to /fttcp and Role 1 (operator ruling OR-30).
Model: claude-opus-5-5. Run date: 2026-10-20. Operator asleep: protocol STOP lines run as flags.
Revision: ROLE 5 LOOP 2 (final), after A5 re-audit runs/hfcl-q2fy27/work/audit_hfcl_q2fy27_role5_loop1.md. Fixes NF1 and NM1 only. Loop 1 (after A5 audit runs/hfcl-q2fy27/work/audit_hfcl_q2fy27_role5.md) fixed F1, C1, M1-M4 and style notes S1-S13. Both change logs follow the closing YAML.

This addendum is one document written as three part files (output size limit; no shell or edit tool in this agent). The orchestrator joins them in this order, with nothing between them, into runs/hfcl-q2fy27/work/review_hfcl_q2fy27_role5.md:
- Part 1: runs/hfcl-q2fy27/work/parts/review_hfcl_q2fy27_role5.loop2.part1.md: caveat, ledger preamble, Role 5 Steps 0 to 4.
- Part 2: runs/hfcl-q2fy27/work/parts/review_hfcl_q2fy27_role5.loop2.part2.md: Steps 5 to 8.
- Part 3: runs/hfcl-q2fy27/work/parts/review_hfcl_q2fy27_role5.loop2.part3.md: Step 9, additions to Step 8.5, additions to monitorables, verdict after Role 5, updated Plain-Language Brief, closing YAML, loop 1 and loop 2 change logs.
The loop 1 part files (runs/hfcl-q2fy27/work/parts/review_hfcl_q2fy27_role5.loop1.part2.md and .loop1.part3.md) and the earlier runs/hfcl-q2fy27/work/parts/review_hfcl_q2fy27_role5.part2.md are superseded and must not be joined.

## SOURCE CAVEAT (binds every concall finding in this addendum)

The transcript is a MACHINE transcript (faster-whisper, local CPU, medium.en and small.en mixed; C-L19-21). It is not an official transcript. Speakers are INFERRED, not labelled. Numbers and names may be mis-heard. Filed results win on any number conflict. Every C-L figure below carries this caveat. Three audio gaps sit at load-bearing points (C-L249-250, C-L482-483, C-L665-666), and one analyst dropped mid-question (C-L776-778). A3 turn-mapping note applied: R316, R441 and R387 (C-L599-600) sit in an analyst turn (T070) but are management speech; they are treated as MD commitments. The reverse case also occurs: analyst speech sits inside MD turn T093 (C-L723-727), so R119-R122 are partitioned as management numbers but are read here as analyst figures; an analyst interjection also sits inside T110 (C-L798-799).

## ANCHOR CONVENTION

| Prefix | Source |
|---|---|
| C-L### | runs/hfcl-q2fy27/extracted/hfcl-concall-q2fy27-fulltext.md (line number) |
| T### / R### | A1 structured concall rows (runs/hfcl-q2fy27/extracted/hfcl-concall-q2fy27-structured.md) |
| M## | A2 MISSING_FROM_STRUCTURED rows (ledger section 12, runs/hfcl-q2fy27/work/ledger_concall_hfcl_q2fy27.md) |
| CC-FN-## | A3 concall forensics (runs/hfcl-q2fy27/work/forensics_concall_hfcl_q2fy27.md) |
| Q## / MQ## | Q01-Q54 = A2 analyst question rows (Step 4A). Q1-Q42 = Role 4 questions. MQ43-MQ61 = new management questions from this addendum (Section 3A) |
| [ROLE 4] | Filed figure as anchored in the Role 4 review (R-L results, P-L deck, M-L MA report) |
| [MEMORY] | Notion brief (runs/hfcl-q2fy27/work/notion-brief.md); memory to weigh, not evidence |
| [COMPUTED] / [INFERENCE] | Arithmetic shown / reasoning, not a filed fact |

---

## (1) LEDGER RECONCILIATION PREAMBLE (contractual, before Step 1)

Ledger contains 0 notes / 145 turns / 0 slides. All 145 turns reviewed. Ledger rows: 615 structured IDs plus 14 MISSING_FROM_STRUCTURED rows (M01-M14) = 629, all reviewed. Findings incorporated: CC-FN-01 to CC-FN-25.

| Item | Count |
|---|---|
| Structured IDs in ledger (R001-R470 + T001-T145) | 615 |
| IDs referenced in ledger | 615; orphans 0 |
| MISSING_FROM_STRUCTURED rows (A2 loop 1, audit M1; ledger section 12) | 14 (M01-M14); all read by A4 at their fulltext lines (table below) |
| A2 count test | gate_a2 pass (numbers 166, entities 68, forward phrases 112, dates 46, qualifiers 78, turns 145, missing_from_structured 14) |
| Analyst question rows (A2 section 3) | 54 (Q01-Q54); T018 is an answer with no recorded question |
| A3 rows read at cited line | 615 of 615 (100%); fulltext C-L1-1020 read in full |
| A4 reading | Fulltext C-L15-1020 read in full by A4 for grading; every forward row R235-R346 classified (Step 6B); M01-M14 re-read at line in loop 1 |
| Unreviewed rows | none |

MISSING_FROM_STRUCTURED rows, reviewed, and where each is used:

| Row | Line | Speaker | Content (short) | Used in |
|---|---|---|---|---|
| M01 | C-L238 | MD (T017) | Telcos "have not been buying much since last two years" (prices rose too much, C-L239) | 4A Q05; Brief part 2 |
| M02 | C-L275 | MD (T018), forward | Target revenue "will get consolidated after acquisition being completed", dated "in this quarter itself" (C-L274) | 9A #18; 6B sensitivity |
| M03 | C-L432-433 | MD (T036) | BharatNet bill file goes through "25 different steps"; a query sends it back to step 0 | 4C Exchange 3; Brief part 2 |
| M04 | C-L676 | MD (T083), forward | Talking to international telcos "where we think we'll get some orders" | 9A #33; 6B sensitivity |
| M05 | C-L700 | Analyst (T086) | Average delivery "in 2 years time frame"; "10,000" garbled | 4A Q33 |
| M06 | C-L745-746 | Analyst (T094) | Visibility "3 year 2 years"; "6 7000 crores" a year | 4A Q36 |
| M07 | C-L755-756 | MD (T095), forward | "we will keep on receiving more orders ... orders would be more than the supply we do" | 4A Q36; 9A #6; 6B sensitivity |
| M08 | C-L852 | Analyst (T121) | Ballpark price/volume split asked: "50, 50, 60, 40 or 70, 30" | 4A Q46; 4C Exchange 2 |
| M09 | C-L878 | MD (T127) | Short-term contracts of "4 to 6" months carry no reset clause | 4A Q48; 4C Exchange 2 (margin readings) |
| M10 | C-L880-881 | MD (T127) | "four to six months", "five year" contract tenors (garbled) | 4A Q48; 4C Exchange 2 |
| M11 | C-L980 | Analyst (T140) | Data-centre story "planned out for four to five years" | 4A Q54 |
| M12 | C-L391 | Analyst (T033) | Defence Rs200 Cr quarter "into 3 or Q4" | 4A Q11 |
| M13 | C-L767 | Analyst (T098) | Revenue visibility for "the next 2 years" | 4A Q38 |
| M14 | C-L835 | Analyst (T119) | Realisation trend "in Q3 and Q4" | 4A Q45 |

Pipeline note for the orchestrator: the A3 forensics file still records "Orphan / MISSING_FROM_STRUCTURED 0 / 0" (forensics line 17) and holds no A3 reading of M01-M14. A4 read each row at its fulltext line. No M row changes an A3 finding, a count, a grade or a ruling; A5 found their content already reflected (audit section 1).

A3 finding classes: FORWARD-SIGNAL 10 (CC-FN-02, 03, 04, 05, 06, 07, 09, 10, 12, 17); AMBIGUOUS 9 (CC-FN-01, 08, 11, 13, 14, 15, 16, 18, 25); CONFIRMATORY-NEGATIVE 3 (CC-FN-22, 23, 24); NEUTRAL-FACT 3 (CC-FN-19, 20, 21). Every FORWARD-SIGNAL and AMBIGUOUS finding maps to a new question (Section 3 coverage table).

---

## (2) ROLE 5 ANALYSIS

### STEP 0: PRE-FLIGHT

#### 0A. Notion page

Taken from the Role 4 review Step 0A [MEMORY]: Decision Status WATCHLIST ("DO NOT INITIATE"), not held; entry zone Rs60-75; Promoter Verdict CONCERN (ruling pending, slip #5 toward AVOID); Management Grade (concalls) B- / C+; archetype "provisional OVERPROMISER-watch", Q1 specificity ~0.81 (seed-log basis, not a transcript).
Previous concall log: the Q1 FY27 transcript was never supplied or scored. No scored Role 5 log exists. Passed memory items: the Q1 promise seed log, Q4 FY26 concall points (fuze "couple of months" for 5 quarters; receivables ageing deferred; long-term hyperscaler margins 1-2% below spot), FY26 delivery record (AR Step 12), and a broker summary of 05-Oct (MGMT via broker, not verified). This is the first concall scored under the protocol. The promise-vs-delivery log starts here; Step 3 also gives a provisional score from the memory items, labelled as such.

#### 0B. Participants

| Role | Name | Notes |
|---|---|---|
| Hosting broker / IR | Achal Lohade, Nuvama Institutional Equities (C-L38-45) | Sell-side house broker; its analyst (Kushi Soni) asked 7th, on substance |
| CMD / Chairman | ND | Not on the introduction list |
| Managing Director | Mahendra Nahata, Promoter and MD (C-L42; ASR "Motor") | Promoter present. Answered every question (speaker inferred) |
| CEO | ND | None introduced |
| CFO | V.R. Jain (C-L42-43) | Present; no attributed turn (speaker-inference caveat) |
| COO / other | Manoj Baid, Company Secretary (C-L43) | No attributed turn |
| IR | Amit Agarwal, Head Investor Relations (C-L43) | Named as the email channel (C-L1010-1014) |

Yellow flags: none on promoter absence. One mild flag: the CFO gave no answer on cash, debt or tax; the MD answered the debt question himself (C-L551-555). No new senior names. IR firm did not speak beyond the moderator.

#### 0C. Structure

| Item | Reading |
|---|---|
| Date and time | 19-Oct-2026, 16:30 IST (same day as board approval 11:00-11:40) |
| Gap after filing | Same day (protocol label: canned timing) |
| Duration | 00:00:00 to 01:22:45, about 82.8 minutes (above 75: engaged audience) |
| Opening remarks | 00:01:48 to 00:12:40, about 10.9 minutes |
| Q&A | 00:12:54 to 01:22:07, about 69.2 minutes, 83.6% of the call [COMPUTED] |
| Analysts | 15 participants (14 named, 1 unnamed); 54 question rows (A2) |

#### 0D. Safe harbour

The moderator read one generic disclaimer (C-L26-32): forward-looking statements, business risks, investors to verify independently. No company-specific risk named (no raw material, geopolitics, rates). The deck has no disclaimer slide (PPT-FN-15) and the press release has none (RES-FN-15). A narrow, generic caveat sits beside bold forward numbers (defence Rs2,000 Cr, the Rs5,000 Cr defence aspiration, connectivity Rs2,000 Cr, "no chance" of worse margins).

#### 0E. Business type

Standard operating business. Step 2 (not 2L) applies.

---

### STEP 1: OPENING REMARKS: CLAIMS INVENTORY (T003, C-L46-148)

| # | Claim | Type | Quantified? | Source line |
|---|---|---|---|---|
| 1 | Best-ever quarterly performance | Backward | NO | C-L52 |
| 2 | Consolidated PBT Rs538.60 Cr, +406.49% YoY, +62.46% QoQ | Backward | YES | C-L59-61 |
| 3 | PAT Rs394.22 Cr, +448.14% YoY, +60.49% QoQ | Backward | YES | C-L61-63 |
| 4 | H1 PBT Rs870.12 Cr (+1311.62%), PAT Rs639.86 Cr (+1401.31%) | Backward | YES | C-L63-65 |
| 5 | Revenue Rs2,541.79 Cr, +143.62% YoY, +32.73% QoQ | Backward | YES | C-L65-66 |
| 6 | EBITDA Rs658 Cr; margin 25.89%, +640 bps YoY, +264 bps QoQ | Backward | YES | C-L66-69 |
| 7 | PAT margin 15.51% ("PED margin"), +862 bps YoY | Backward | YES | C-L69-70 |
| 8 | Invested ahead of the curve in capacity, integration, products | Strategic | NO | C-L73-76 |
| 9 | Exports grew about 493% YoY | Backward | YES | C-L77-78 |
| 10 | On track to maintain the growth trajectory | Forward Soft | NO | C-L81-82 |
| 11 | Order book Rs28,900 Cr | Customer/Order | YES | C-L85 |
| 12 | Pipeline at advanced stages, to convert "in due course" | Customer/Order | NO | C-L86-87 |
| 13 | Q2 is not a peak | Forward Soft | NO | C-L88-89 |
| 14 | Customers are large technology companies with long-term agreements | Customer/Order | NO | C-L90-92 |
| 15 | Order book to strengthen further | Forward Soft | NO | C-L93 |
| 16 | Demand accelerating across AI, hyperscale and telecom | Macro/Tailwind | NO | C-L97-98 |
| 17 | International opportunities converting into firm contracts | Customer/Order | NO | C-L99-101 |
| 18 | FY27 revenue growth "at least 80%" (history 20%, then 40%, then 80%) | Forward Guidance | YES | C-L104-108 |
| 19 | Rs10,000 Cr revenue "much before" FY29 | Forward Guidance | YES | C-L109-111 |
| 20 | Planned capex about Rs1,800 Cr across OF, OFC, preform | Operational | YES | C-L112-114 |
| 21 | Cable portfolio and DC connectivity "progressing well" | Forward Soft | NO | C-L115-116 |
| 22 | Defence and aerospace is the next major growth engine | Strategic | NO | C-L117-118 |
| 23 | Second batch of thermal weapon sights for AK-203 delivered in September | Operational | YES | C-L123 |
| 24 | Aerospace acquisition to complete during the current quarter | Forward Guidance | YES | C-L124 |
| 25 | Target has an "executed order book" of about Rs1,600 Cr | Customer/Order | YES | C-L125-126 |
| 26 | Working on several other large defence opportunities | Forward Soft | NO | C-L127-128 |
| 27 | On track to about Rs500 Cr defence revenue in FY27 ("expiration" = aspiration) | Forward Guidance | YES | C-L129-130 |
| 28 | Ammunition complex in Andhra Pradesh; 1,000 acres allotted | Operational | YES | C-L131-133 |
| 29 | Construction of the site will start soon | Operational | NO | C-L134 |
| 30 | OFC, connectivity and defence "on the cusp of enormous growth" | Macro/Tailwind | NO | C-L138-140 |
| 31 | Growth momentum to continue | Forward Soft | NO | C-L142 |
| 32 | Opportunity extends over the next 6-7 years | Forward Soft | NO | C-L143 |

Diagnostics:
- Quantified share: 16 of 32 claims = 50.0% [COMPUTED]. Backward claims (rows 1-7, 9, 23) are mostly quantified: 8 of 9. Forward-type claims (rows 10, 13, 15, 18, 19, 20, 21, 24, 26, 27, 29, 31, 32) are mostly not: 5 of 13 quantified (rows 18, 19, 20, 24, 27).
- New vs reaffirmed: new are the 80% guide (raise), export growth 493%, the AK-203 delivery, "complete during the current quarter", the Rs1,600 Cr target book (Q1 memory ~Rs2,000 Cr), and the land allotment. Reaffirmed are Rs10,000 Cr earlier than FY29, Rs500 Cr defence and Rs1,800 Cr capex.
- Quietly dropped from the opening: capacity dates (Dec-2026 step [MEMORY]), the Rs215 Cr DC facility, fuze approval, the EPC loss band of Rs80-90 Cr a quarter [MEMORY, broker], receivables, exports 60%+ target, Nivetti, warrants. The guide history "20-40, 40-80" (C-L109) omits the "at least 60%" step relayed by a broker on 05-Oct [MEMORY] (CC-FN-02).
- Internal contradictions: the target book is "executed" (C-L125) but later "pending" at Rs1,800 Cr (C-L273) and "16 or 1800" (C-L405); defence is an "aspiration" (C-L129) but later "surely" (C-L408). The opening EBITDA (25.89%) includes other income; the operating margin is 24.81% [ROLE 4] (CC-FN-19).

---

### STEP 2: FORWARD GUIDANCE EXTRACTION

| Metric | This quarter's guidance (call) | Last quarter's guidance | Two quarters ago | Trajectory | Confidence |
|---|---|---|---|---|---|
| Revenue growth FY27 | "at least 80%" (C-L108); "lower number ... I surprise you by better numbers" (C-L181); "definitely be growth in Q3" (C-L608) | 40% aspiration (C-L106; seed log [MEMORY]); "at least 60%" via broker 05-Oct [MEMORY] | ~20% aspiration (C-L104-105) | Raised (floor lifted; protocol has no "raised" label: nearest is New floor) | MEDIUM (floor stated; "based on current expectation"; basis not stated) |
| Revenue growth FY28 | "avoid giving any guidance for 28" (C-L484); Rs10,000 Cr "much sooner than ... 29 because you can see the run rate" (C-L484-486); "should be doing better" (C-L487) | ND | ND | New (implicit only) | LOW |
| EBITDA margin band | "going to get better only ... no chance ... worse" (C-L201-202); "somewhat increase" (C-L375); "may be some improvement" (C-L562). No number on the call. Deck: ">27% by FY29" (P-L503) [ROLE 4] | 22-25% by FY29 (seed [MEMORY]); ~25-26% after captive preform (broker [MEMORY]) | ND | Raised (deck); directional on call | LOW (call) |
| Order book / pipeline | Rs28,900 Cr (C-L85); pipeline "advanced stages" (C-L86) | Rs26,665 Cr (Q1 deck, P-L302 [ROLE 4]); MD recalls "26,000", hedged (C-L750-751) | Rs21,206 Cr (Q4 FY26, P-L306 [ROLE 4]) | Up | HIGH (ties to filed Rs28,911 Cr) |
| Capex envelope | "pending CAPEX is 1800 crores" (C-L785); preform Rs1,250 Cr (analyst, C-L548) | Rs820 Cr added 14-Sep, total ~Rs1,800 Cr [MEMORY]; ~Rs2,500 Cr over 2-2.5 years (broker [MEMORY]) | ND | Maintained | MEDIUM (no phasing, no funding split) |
| Utilisation | "fibre 100%"; cable "100%" "in money terms" (C-L322, C-L502-509) | ND | ND | New definition (revenue basis) | LOW (not physical) |
| Capacity timeline | Fibre 28 to 34 to 43; cable 34 to 63 mn fkm, undated (C-L361-362, C-L716-717); "34 to 53" outlier (C-L768); own preform 600 MT, "October 28" (C-L588) | OF 33.9 / OFC 42.36 mn fkm by Dec-2026 [MEMORY] | ND | Widened (interim dates dropped; end-states kept) | MEDIUM on Oct-2028 preform; LOW on interim steps |
| Strategic order execution | $1.1B hyperscaler order: "already started delivering" (C-L516-517), revenue not given; book delivery "4 to 6 months ... 3 years, 4 years" (C-L697-698), "next 5 years" (C-L702) | FY27-FY31 execution [MEMORY] | ND | Maintained | LOW |
| Working capital / CCC band | None given. BharatNet: "expenses were incurred but bills were not raised" (C-L427-429); bills "this quarter" (C-L435) | None (Q4 FY26 ageing deferred [MEMORY]) | None | No guidance in any quarter | n.a. |
| Net debt trajectory | "debt reduction will start in the current year" (C-L552); Mar-27 and Mar-28 debt "will substantially go down" (analyst-framed, MD-affirmed, C-L553-555) | ~Rs1,700 Cr debt to fall by end-FY28 (broker [MEMORY]) | ND | Pulled forward | MEDIUM (dated, no amount) |
| Export / segment: defence | FY27 "500 to 600" (C-L251); FY28 "at least 2000" (C-L251-252); ~5,000 framed three ways: "in expiration [aspiration], if you take it in three years time frame" (C-L252-253); "it should not be difficult for us to reach the 2000 crores figure and a 5000 crores figure" (C-L278-279); later "possibly 5,000 crores in next two years" (C-L770) | ~Rs500 Cr FY27, ~Rs1,500 Cr FY28, Rs4,000-5,000 Cr by FY30 (broker [MEMORY]) | ND | Raised; horizon inconsistent in one call; Rs5,000 Cr is an aspiration, not a commitment [INFERENCE: A4 classification from C-L252, C-L713, C-L770, weighed against the MD's "should not be difficult", C-L278-279] | MEDIUM (FY27, FY28); LOW (Rs5,000 Cr) |
| Export / segment: connectivity | FY27 "more than 800" (C-L369-370); Q2 "about 300" hedged (C-L796-802); Q1 "nil" then "fixed" (C-L819-820); FY28 Rs2,000 Cr (C-L370-371, C-L858) | Rs400-500 Cr FY26-27; Rs800-1,000 Cr FY27-28 [MEMORY] | ND | Raised 2x to 2.5x for FY28 | MEDIUM |
| Export share | None on the call. Deck: 63% now, 65%+ and >70% targets (P-L502-508) [ROLE 4] | 60%+ FY27 onward (seed [MEMORY]) | ND | Not discussed | n.a. |
| New product / contract milestones | Aerospace close "within November" (C-L404); foliage radar approval "another couple of weeks" (C-L397-399); Army AMC via BSNL signed "a week or 10 days" (C-L423); in-DC connectivity revenue "last quarter of the current financial year" (C-L368); preform "midterm solution" from Q1 CY2027 (C-L582); restructuring board meeting "week or 10 days" after the recommendation, finalisation within "another couple of weeks" (C-L539-545); Turnkey profit "first quarter of next year" (C-L443) | Aerospace "proposed" [MEMORY] | ND | New, dated | MEDIUM to HIGH on dates; content withheld on preform |
| Dividend / payout | None | Rs0.20 FY26 dividend [MEMORY] | ND | Not discussed | n.a. |

Diagnostics:
- Widened or tightened: the revenue floor rose. FY28 guidance was refused. Interim capacity dates were dropped (widened).
- Dropped without acknowledgment: the Dec-2026 capacity step date; the Rs215 Cr DC facility; the Rs80-90 Cr a quarter EPC loss band [MEMORY, broker], now replaced by an unreadable two-quarter ceiling (C-L441) and a Q1 FY28 profit date; the export-share target; fuze approval.
- Internal consistency [COMPUTED]:
  - Revenue: if Q3 and Q4 each equal Q2 (Rs2,541.79 Cr), FY27 is Rs9,540.35 Cr, +92.76% on FY26 Rs4,949.27 Cr. The "at least 80%" floor is Rs8,908.69 Cr and lets H2 grow only +46.69% YoY [ROLE 4]. The MD's own words ("definitely be growth in Q3") put the floor below his path (CC-FN-02).
  - Defence: FY27 Rs500-600 Cr against H1 Rs78.68 Cr [ROLE 4] needs Rs421.32-521.32 Cr in H2, 5.35x to 6.63x H1. The call leans on the aerospace target from November (C-L404-407).
  - Margins: "no chance" of worse margins (C-L202) sits beside a Q2 fibre price rise of about 20% the MD did not foresee (C-L646-647) and preform contracts that reset at expiry (C-L333-334). Customer long-term contracts also reprice year to year, up or down (C-L336-339).
  - Debt: lower debt in FY27 sits beside Rs1,800 Cr of pending capex (C-L785), H1 gross borrowings up Rs126.76 Cr [ROLE 4], and Rs123.40 Cr of H1 current tax still to pay [ROLE 4]. The call names no funding source; the Rs416.25 Cr warrant balance was not mentioned.
- Versus Four-Pillar projections: above the Notion FY27 base (revenue 6,200 [MEMORY]).
- Refused or not given when pressed: FY28 guidance (C-L484); hyperscaler revenue (C-L516); price vs volume split (C-L845, C-L853); the preform solution (C-L581, C-L885); customer names (C-L168-170); peer margin comparison (C-L667-692); OFC scale in rupees (C-L719-721).

---

### STEP 3: PROMISE vs DELIVERY AUDIT

No scored prior concall log was passed. The Q1 FY27 transcript was never supplied. Formal 3A-3E rows that need a scored prior concall are ND ("prior log not passed"). This is the first concall scored under the protocol; the log starts with the 34-item register in Step 9A. For operator use, a PROVISIONAL score is built from memory items and filed outcomes. It is labelled provisional and is not the Role 1 track-record input (the protocol makes the ratio the sole Role 1 source only once a Role 5 history exists).

Point schedule used: DELIVERED 1.0; PARTIALLY DELIVERED 0.5; MISSED 0.0; DELAYED 0.0; DROPPED 0.0 plus a flag; UNCLEAR excluded from the denominator.

#### 3A. Prior commitments with an outcome now visible (PROVISIONAL)

| Commitment (source) | Actual this period | Status | Points |
|---|---|---|---|
| FY26 revenue growth (AR Step 12 [MEMORY]) | Delivered per AR record | DELIVERED | 1.0 |
| FY26 margin expansion (AR [MEMORY]) | Delivered per AR record | DELIVERED | 1.0 |
| FY26 export mix (AR [MEMORY]) | Delivered per AR record | DELIVERED | 1.0 |
| FY26 capacity commissioning (AR [MEMORY]) | Delivered per AR record | DELIVERED | 1.0 |
| FY26 cash generation (AR [MEMORY]) | FY26 CFO (378.13) [MEMORY] | MISSED | 0.0 |
| FY26 Turnkey / EPC profitability (AR [MEMORY]) | FY26 Turnkey (113.01) [ROLE 4, R-L846] | MISSED | 0.0 |
| Demerger (FY26 [MEMORY]) | Reframed to HASPL consolidation, no acknowledgment of the change | DROPPED | 0.0 + flag |
| Fuze approval "couple of months" (Q4 FY26 and earlier concalls [MEMORY]) | No approval filed; not discussed on this call (CC-FN-24) | DELAYED (repeat delay) | 0.0 |
| Nivetti closure by 30-Sep-2026 [MEMORY] | Moved to 31-Dec-2026 on 1-Oct (second extension) [MEMORY]; not discussed | DELAYED (second time) | 0.0 |
| EPC loss Rs80-90 Cr a quarter (MGMT via broker, 05-Oct [MEMORY, SECONDARY]) | Q2 Turnkey loss Rs122.58 Cr [ROLE 4]; MD "121 or some crores" (C-L440) | MISSED | 0.0 |
| FY27 revenue growth 40% (Q1 seed [MEMORY]) | H1 +132.81% [ROLE 4]; FY not ended | UNCLEAR (pace ahead) | excluded |
| Rs215 Cr DC facility, Sep-2027 (seed) | Not in deck or call | UNCLEAR (DROPPED candidate) | excluded |
| OF 33.9 / OFC 42.36 mn fkm by Dec-2026 (seed) | Steps restated undated (C-L361-362); date not reaffirmed | UNCLEAR (DROPPED candidate for the date) | excluded |
| Preform 300 MT, Rs580 Cr, Jul-2029 (seed) | Now 600 MT, Oct-2028 (C-L588; P-L436-442) | UNCLEAR (reframed up) | excluded |
| MMHG Phase-1 Rs275 Cr (seed) | Rs230 Cr (P-L436) | UNCLEAR (reframed down) | excluded |
| Aerospace acquisition (seed; CY26 close [MEMORY]) | "within November" (C-L404); Rs90 Cr object deadline moved (M-L1095-1108) | UNCLEAR (re-dated inside CY26) | excluded |
| EBITDA 22-25% by FY29 (seed) | Superseded by ">27%" (deck) | UNCLEAR | excluded |
| Exports 60%+ FY27 onward (seed) | 63% (deck, base unstated) | UNCLEAR (FY not ended) | excluded |
| Warrant balance ~Nov-2027 (seed) | Rs416.25 Cr due; no Q2 receipt (M-L1056-1058) | UNCLEAR | excluded |

#### 3B. Cumulative track record

| Concall / basis | Total commitments | Delivered | Partially | Missed | Delayed | Dropped | Unclear | Points |
|---|---|---|---|---|---|---|---|---|
| Prior scored concalls (Q3 FY26 to Q1 FY27) | ND (prior log not passed) | ND | ND | ND | ND | ND | ND | ND |
| PROVISIONAL (memory + filed outcomes, table 3A) | 19 | 4 | 0 | 3 | 2 | 1 | 9 | 4.0 |
| Q2 FY27 call (this quarter; log starts) | 34 (Step 9A register) | 0 | 0 | 0 | 0 | 0 | 34 | n.a. |

Provisional credibility ratio = 4.0 / (19 - 9) = 40.0% [COMPUTED]. Excluding the broker-sourced EPC row: 4.0 / 9 = 44.4%. Both sit in the 40-60% band: Grade C (Mixed), provisional.
Sensitivity on the point schedule: with DELAYED scored at 0.5, the ratio is 5.0 / 10 = 50.0%, or 5.0 / 9 = 55.6% without the EPC row [COMPUTED]. Grade C and the provisional quadrant hold on every reading.
Formal trailing-4 ratio: ND. Role 1 track-record input: ND formally; the provisional reading is Mixed. /fttcp and Role 1 decide whether to use it.
DROPPED rule: 1 confirmed DROPPED (demerger) plus 2 candidates (DC facility; Dec-2026 capacity date). Two confirmed DROPPEDs in the trailing window trigger an automatic one-grade downgrade (C to D). Next check: Q3 FY27 deck and call.

#### 3C. Pattern recognition

- Revenue and margin delivered; cash and EPC missed (FY26 and Q2 FY27).
- Timelines slip repeatedly on the same items: fuze (5+ quarters [MEMORY]), Nivetti (twice), the HASPL Rs90 Cr object (30-Sep to 31-Dec), and now Turnkey profit (EPC loss band missed; profit moved to Q1 FY28).
- Quiet drops: the demerger, the Dec-2026 capacity date, the Rs215 Cr DC facility.
- Targets rise while delivery lags elsewhere: revenue guide 20, 40, 80%; defence FY28 ~1,500 to 2,000+; connectivity FY28 800-1,000 to 2,000.
- Trend of the ratio: ND (no prior ratio).

#### 3D. Management Grade / Promoter Verdict

No change written (operator-only). Evidence for the operator: provisional Grade C (Mixed) supports the "C+" side of the Notion B- / C+ grade. The pending Promoter Verdict ruling (slip #5) gains three data points from this quarter: the HASPL object slip by circular resolution, the EPC loss band miss, and the second silent quarter on receivables (Step 8C).

#### 3E. Last quarter's questions (Q1 FY27, 15): combined status (Q2 filings plus Q2 call)

| Q1 # | Question (short) | Filings (Role 4 0F) | Call (CC-FN, C-L) | Combined status |
|---|---|---|---|---|
| 1 | Export-OFC revenue; hyperscaler share of book | NOT ADDRESSED | "maybe 70 percent ... of the export orders" of the Rs18,500 Cr book, "I do not have the exact number" (C-L170-173); revenue "I do not have that number" (C-L516) | PARTIALLY ANSWERED (base of the 70% unclear; revenue evaded) |
| 2 | Guide floor or aspiration | PARTIAL | "we expect ... at least 80%" (C-L108); "lower number" (C-L181) | ANSWERED SPECIFICALLY |
| 3 | Consolidated vs standalone PAT; subsidiary; transfer price | NOT ADDRESSED | Not discussed | NOT ADDRESSED (2nd quarter) |
| 4 | Auditor other-matter coverage | PARTIAL | Not discussed | PARTIALLY ANSWERED |
| 5 | BharatNet III revenue, margin, receivables | NOT ADDRESSED | Cause of loss explained, no Rs figures (C-L427-438) | PARTIALLY ANSWERED |
| 6 | Receivables, DSO, unbilled; inventory deferral | NOT ADDRESSED | Not discussed (CC-FN-22) | NOT ADDRESSED (2nd quarter) |
| 7 | Steady-state ETR | PARTIAL (by numbers) | Not discussed | PARTIALLY ANSWERED |
| 8 | OCI swing | NOT ADDRESSED | Not discussed | NOT ADDRESSED (2nd quarter) |
| 9 | Diluted EPS vs warrants | ANSWERED (by numbers) | Not discussed | ANSWERED SPECIFICALLY (filing) |
| 10 | Rs215 Cr DC facility | NOT ADDRESSED | "installing higher capacity for connectivity solutions" (C-L364); facility not named | PARTIALLY ANSWERED |
| 11 | Defence via entity to be acquired | PARTIAL | Close "within November" (C-L404); target, price, structure not given | PARTIALLY ANSWERED |
| 12 | Promoter holding; pledge zero | PARTIAL | Not discussed | PARTIALLY ANSWERED (pledge open) |
| 13 | Capacity Dec-2026 | NOT ADDRESSED | Steps restated, undated (C-L361-362) | PARTIALLY ANSWERED (date not given) |
| 14 | Export share base period | NOT ADDRESSED | Not discussed | NOT ADDRESSED (2nd quarter) |
| 15 | Order book executable vs L1; margins | PARTIAL | Delivery tenor (C-L697-702); no L1 split, no margins | PARTIALLY ANSWERED |

Totals: ANSWERED SPECIFICALLY 2; PARTIALLY ANSWERED 9; EVADED 0; NOT ADDRESSED 4. No question was formally evaded, because analysts did not ask most of them. Four topics went unaddressed in both Q1 and Q2 disclosures (profit location, receivables, OCI, export base). Repeated non-address is logged as a governance signal for the Promoter Verdict review (operator).

---

### STEP 4: Q&A DECOMPOSITION

#### 4A. Q&A inventory (A2 question rows Q01-Q54; grades A full / B hedged / C partial / D evasion / E refusal)

| # | Analyst and firm | Question (1 line) | Category | Grade | Substance (line) |
|---|---|---|---|---|---|
| Q01 | Pranav Kshatriya, MK | Hyperscaler share of Rs18,500 Cr book; concentration | Customer/Order | C | Names under NDA; "maybe 70 percent ... of the export orders", "I do not have the exact number"; concentration unanswered (C-L168-174) |
| Q02 | Pranav Kshatriya, MK | Guide looks conservative (flat H2) | Forward Guidance | B | "This is a lower number and I surprise you by better numbers" (C-L181) |
| Q03 | Pranav Kshatriya, MK | Preform supply challenge? | Operational | B | "No, no, no, not at all" (C-L185) |
| (T018) | Question not recorded (audio gap) | Defence outlook | Forward Guidance | A | FY27 500-600, FY28 2,000+, ~5,000 in 3 years as an aspiration ("in expiration", C-L251-253) |
| Q04 | Ashutosh Kumar Jha, Baliyani AM | Margin trajectory this year and next two | Financial | B | "better only ... no chance ... worse" (C-L199-208) |
| Q05 | Ashutosh Kumar Jha | Demand slowdown from US rates? | Macro | B | No slowdown; Europe, Asia, telcos to add demand; telcos bought little "since last two years" because prices rose (C-L218-249; M01 C-L238-239) |
| Q06 | Chilmay Sapre, Schonfeld | Telecom revenue split telcos vs hyperscalers | Customer/Order | B | "70-30 ... not exactly" (C-L305-306) |
| Q07 | Chilmay Sapre | Repeat of Q06 (MD asked to repeat) | Clarification | B | Same; utilisation "in money terms ... 100%" (C-L307-322) |
| Q08 | Chilmay Sapre | Preform cost reset frequency | Financial | B | Supplier prices yearly, 18 or 24-month contracts, "price variation has to be there" at expiry; customer long-term prices also reset "year to year ... it can go down, it can go up" (C-L330-340) |
| Q09 | Chilmay Sapre | Maintain current margins? | Financial | B | "confident of getting it better" (C-L343) |
| Q10 | Rikin, Kapri family office | OFC three-year size; margin drivers | Strategic | B | Capacity steps; connectivity >800 / 2,000; preform late-2028 (C-L358-382) |
| Q11 | Rikin | Defence ramp to ~Rs200 Cr a quarter "into 3 or Q4" (M12, C-L391) | Forward Guidance | B | Product list; radar approval ~2 weeks; aerospace "within November"; "surely" (C-L393-408) |
| Q12 | Rikin | When does EPC turn positive? | Financial | B | AMC signing; BharatNet bills unraised; loss "121"; ceiling unreadable (C-L416-441) |
| Q13 | Rikin | Profit next year? | Forward Guidance | A | "first quarter of next year" (C-L443) |
| Q14 | Maarek | India DC opportunity | Macro | B | 1.6 GW to 6 GW by 2030; personal view 10 GW (C-L459-482) |
| Q15 | Maarek | FY28 guidance (start of question lost) | Forward Guidance | C | Refuses FY28 guide; Rs10,000 Cr sooner; "see the run rate" (C-L484-499) |
| Q16 | Maarek | Utilisation at current run rate | Operational | C | "fibre 100%"; cable 100% "on the basis of revenue numbers", some machines at 80% (C-L502-509) |
| Q17 | Kush Tandar | H1 revenue from the $1.1B order | Customer/Order | D | "I do not have that number in particular" (C-L516) |
| Q18 | Kush Tandar | Other hyperscaler orders? | Customer/Order | B | "Yes, yes, of course, we have" (C-L518-520) |
| Q19 | Kush Tandar | O&M margin (Rs5,000 Cr O&M book) | Financial | B | "15 to 20 percent" like turnkey (C-L522-530) |
| Q20 | Kush Tandar | EPC restructuring update | Governance | B | Committee with E&Y near recommendation; board meeting "week or 10 days" after it, to "discuss and take a decision"; finalise within "another couple of weeks" (C-L535-547) |
| Q21 | Kush Tandar | Capex and deleveraging | Financial | B | Repaying old debt, new debt for capex; reduction starts this year (C-L551-552) |
| Q22 | Kush Tandar | Debt lower at Mar-27 and Mar-28? | Financial | B | "Yes, it will substantially go down" (C-L555) |
| Q23 | Kush Tandar | Any one-time or high-margin event in Q2? | Financial | A | "No, there is no such thing" (C-L560-563) |
| Q24 | Kushi Soni, Nuvama (host) | Preform expansion progress, headwinds | Operational | B | "no such significant delay"; machine supplies ran "two three months" late, already absorbed in the October 2028 date; midterm solution Q1 CY27 (confidential) (C-L580-588) |
| Q25 | Kushi Soni | Germanium contracts | Operational | C | "too early to finalize content" (C-L593-595) |
| Q26 | Kushi Soni | Germanium follow-up | Operational | B | Low cost share; needed "two years from now" (C-L599-600) |
| Q27 | Kushi Soni | QoQ volume, pricing; DC vs telecom revenue history | Customer/Order | C | Q3 growth promised; DC 65-75%, telcos 25-35%; no history (C-L606-618) |
| Q28 | Kushi Soni | Revenue or volume basis? | Clarification | A | Revenue (C-L621) |
| Q29 | Kushi Soni | DC vs telecom realisation | Financial | B | Telco fibre ~$15, DC fibre ~$25-27; "not comparable" (C-L628-640) |
| Q30 | Kushi Soni | Blended price trend | Financial | B | "gone up by some 20%"; "some increase, but not as much" (C-L644-648) |
| Q31 | Debashish Mazumdar, Shagun Capital | Telecom margin 32-33% vs peers | Strategic | C | Declines peer comparison; audio gap (C-L664-692) |
| Q32 | Debashish Mazumdar | Order book delivery time | Customer/Order | B | "4 to 6 months ... 3 years, 4 years" (C-L697-699) |
| Q33 | Debashish Mazumdar | Average two years? (M05, C-L700) | Clarification | B | "Not necessarily ... next 5 years" (C-L701-702) |
| Q34 | Debashish Mazumdar | Is 600 MT preform enough? | Operational | A | "just half"; rest bought on long-term contracts (C-L705-709) |
| Q35 | Sagar Parikh, Renaissance AM | OFC scale in 2-3 years | Strategic | C | 34 to 63 mn fkm; rupee scale "very difficult to say"; disowns analyst figure (C-L716-741) |
| Q36 | Sagar Parikh | Visibility vs book (Rs28,000 Cr / 4 years; "6 7000 crores", M06 C-L745-746) | Customer/Order | B | More orders coming; 26,000 to 29,000 with 2,500 supply, so 5,500 inflow; "orders would be more than the supply we do" (C-L747-756; M07) |
| Q37 | Sagar Parikh | Follow-up on Rs6,000-7,000 Cr a year | Clarification | C | "not evenly distributed" (C-L759) |
| Q38 | Sagar Parikh | Visibility for "the next 2 years" (M13, C-L767) | Forward Guidance | B | Capacity "34 to 53"; defence "2,000 crores and possibly 5,000 crores in next two years" (C-L768-771) |
| Q39 | Rishabh Vasa, IntSec | Defence H1 ~Rs80 Cr vs Rs500 Cr gap | Forward Guidance | none | Participant dropped; unanswered (C-L776-778) |
| Q40 | Akshat Mehta | Hyperscaler capex needed for growth | Macro | C | Own capex Rs1,800 Cr; US figure "I may be wrong" (C-L785-793) |
| Q41 | Akshat Mehta | Clarification | Clarification | C | Same (C-L786-793) |
| Q42 | Akshat Mehta | Q2 connectivity revenue | Customer/Order | B | "I do not have the right number ... about 300" (C-L796-802) |
| Q43 | Smith Gara, RSP Ventures | Interconnect revenue Q2, Q1, FY27 | Customer/Order | B | 300 Q2 "expectation"; 800 FY27 (C-L815-816) |
| Q44 | Smith Gara | Quarter 1? | Clarification | C | "nil ... there was no quarter one ... fixed" (C-L819-820) |
| Q45 | Dhruv Sitlani, Vyomara Capital | Volume vs price split; realisation "in Q3 and Q4" (M14, C-L835) | Financial | D | "both"; "very difficult to say" (C-L839-849) |
| Q46 | Dhruv Sitlani | Ballpark split ("50, 50, 60, 40 or 70, 30", M08 C-L852) | Financial | E | "Cannot give you a ballpark number" (C-L853) |
| Q47 | Dhruv Sitlani | Connectivity revenue trend | Forward Guidance | A | "800 crore this year, 2000 crore next year" (C-L857-858) |
| Q48 | Unnamed participant | Pass-through of 20-25% price rise | Financial | B | 20-25% is fibre, "not for every raw material"; buyer-seller equilibrium; reset clause in most long-term contracts; none in "4 to 6" month contracts, where margin falls (C-L869-881; M09, M10) |
| Q49 | Unnamed participant | Preform midterm solution detail | Operational | E | "I cannot elaborate this is a trade statement" (C-L885) |
| Q50 | Unnamed participant | Cost, process or sourcing? | Operational | C | "it would reduce cost" (C-L889-890) |
| Q51 | Unnamed participant | In-DC certification needed? | Operational | B | "certification is already there ... started supplying" (C-L899-900); conflicts with in-DC revenue starting Q4 FY27 (C-L367-368) |
| Q52 | Unnamed participant | Global capacity +40-50%; margin outlook | Financial | B | Preform spot "insane", +600%; "no dent on the profitability" (C-L927-946) |
| Q53 | Saket Kapoor, Kapoor company | Key risks: germanium, OFC pricing | Macro | B | Germanium needed in two years; export restrictions (C-L963-974) |
| Q54 | Saket Kapoor | Margin sustainability; US cost of finance; DC story "four to five years" (M11, C-L980) | Financial | C | Demand narrative; margin question not addressed (C-L982-1007) |

Grade totals (54 rows): A 5 (Q13, Q23, Q28, Q34, Q47); B 31; C 13; D 2 (Q17, Q45); E 2 (Q46, Q49); unanswered 1 (Q39). The unattached T018 answer graded A is not in the 54.

#### 4B. Question pattern analysis

- Most asked: margins and pricing (Q04, Q08, Q09, Q10, Q27-Q31, Q45, Q46, Q48, Q52, Q54: 14 rows), preform and germanium (Q03, Q24-Q26, Q34, Q49, Q50, Q53: 8 rows), connectivity revenue (Q42-Q44, Q47, Q51: 5), order-book visibility (Q32, Q33, Q36-Q38: 5), EPC (Q12, Q13, Q19, Q20: 4), defence (T018, Q11, Q39: 3). Repetition on price and margin means the market does not yet trust the margin answer.
- Consistently graded C, D or E: price vs volume split, hyperscaler revenue, the preform solution, OFC scale in rupees, peer margins, FY28 guidance, physical utilisation. These are the topics management does not want discussed. All are delivered-period or structural splits, not forward targets (CC-FN-15).
- Buy-side vs sell-side: about 11 of 15 participants are asset managers or family offices (Baliyani AM, Schonfeld, Kapri family office, Shagun Capital, Renaissance AM, Vyomara Capital, RSP Ventures, Kapoor company, others); sell-side is MK, Nuvama and IntSec. Buy-side participation is strong. No yellow flag.
- Host broker: Nuvama's analyst asked 7th, on preform, germanium and pricing. Not a softball lead. No sign of an orchestrated call.
- Pushback: Pranav Kshatriya (guide looks conservative), Sagar Parikh (visibility; the MD replied "Again you are wrong", C-L759), Dhruv Sitlani (ballpark split, refused), the unnamed participant (pass-through, margin durability). Contested topics: visibility and price vs volume.
- Missing obvious questions: no analyst asked about receivables, unbilled revenue, cash flow, the tax accrual, the standalone vs consolidated profit gap, warrants, pledge, or the acquisition price. Market attention sat on growth and margin. The silence is not management evasion, but it leaves tripwire #4 untested by the market (Step 8C).

#### 4C. The three most important exchanges

**Exchange 1: EPC restructuring (Q20, T055-T056, C-L532-547)**
- Question: "you mentioned about the EPC business, there was some possibility of restructuring or some thoughts on that. Any update?" (C-L532-534)
- Response: "the committee board committee which we had formed for restructuring and we have some external advice also taking E and Y probably ... that committee is already on the just finishing line of making the recommendation. Once I receive the recommendation, I think maybe week or 10 days time, we would be calling for board meeting to discuss and take a decision on that. So, another couple of weeks, I think we should be able to finalize whatever restructuring we finally do. ... one thing which is under active consideration." (C-L535-547)
- Said: a board committee with E&Y advice is near its recommendation. The board meets about 10 days after the recommendation to discuss and decide (C-L539-542). The MD expects to finalise within "another couple of weeks" (C-L543-545). That phrase may be the total time or an addition after the board meeting; the transcript does not say which.
- Not said: the scope (EPC only, or the "verticals" of the deck, P-L124-129), whether listed HFCL keeps 100% of OFC, defence and aerospace economics, any swap ratio or price. The last sentence is cut off.
- Thesis implication: trigger #6 gets tested within about two to four weeks [INFERENCE: 19-Oct plus the recommendation, about 10 days to the board meeting, and up to about 2 weeks more; so early to mid November 2026 on either reading]. Bull reading: an EPC carve-out removes the loss-making, capital-heavy Turnkey book from the listed product company. Bear reading: a structure moves OFC or defence value into a vehicle where listed holders own less.
- Follow-up we would have asked: "Will every resulting entity have the same shareholding as listed HFCL today? Yes or no." (MQ43)

**Exchange 2: Q2 price rise, contract resets and the guide (Q02, Q08, Q27, Q30, Q48; C-L175-181, C-L330-339, C-L606-616, C-L641-648, C-L865-881)**
- Question: "your guidance seems very conservative because it seems like ... flat H2 or it may be slightly decline" (C-L176-178); "on a blended level have you seen prices go up" (C-L642-644); can you "pass on this complete 20-25% given our contracts are long term" (C-L865-868).
- Response: "This is a lower number and I surprise you by better numbers." (C-L181); "there will definitely be growth in Q3" (C-L608); "I said this in the last quarter also that looks to be stabilizing but then it has gone up by some 20%. ... there may be some increase, but not as much as what you have seen in the previous quarter." (C-L646-648); "With customers also, we have the similar situation on the long term contract, the price variation clause is there on the year to year basis. Year to year, we examine the prices and redo the prices, it can go down, it can go up" (C-L336-339); "there is a price reset clause in most of the cases, most of long term contracts there is a price reset clause, short term contract note 4 to 6 points there is no reset clause" (C-L876-878).
- Said: the floor is deliberately low. Q3 revenue will exceed Q2. Q2 carried a fibre price rise of about 20% that he did not forecast in Q1. Customer long-term contracts reprice every year, up or down (C-L336-339). Most long-term contracts carry a reset clause; short-term contracts of 4 to 6 months do not (C-L877-878; M09).
- Not said: how much of the 32.73% QoQ revenue growth was price (refused, C-L853; M08); how much of the 25.89% margin depends on price; which customer contracts reprice in H2 FY27 and on what dates; what share of the book sits in short-term contracts without a reset clause.
- Thesis implication, revenue: Bull reading, on what the extract supports: (a) mix shift to data-centre fibre at about $25-27 against about $15 for telco fibre (C-L629-631), with data centres at 65-75% of revenue (C-L617-618); (b) connectivity revenue of at least about Rs500 Cr in H2 [INFERENCE: FY27 "more than 800" (C-L369-370) less Q2 "about 300" (C-L796-802) and Q1 "nil" (C-L819-820)]; (c) headroom on some cable lines (some machines at 80%, C-L506; loose-tube lines idle, C-L735-736); (d) annual resets currently move up ("now a days the time is it is only going to go up", C-L339). On that reading H2 stays at or above Q2 and the guide is a sandbag. This reading has NO price floor: customer contracts reset every year in both directions (C-L336-339). It has NO new capacity in H2 FY27: fibre already runs at 100% (C-L308, C-L502), installed capacity is unchanged at OF 28 / OFC 39 mn fkm (P-L434 [ROLE 4]), and no capacity step is dated before July 2028 (P-L428-434 [ROLE 4]); the call gives the steps without dates (C-L361-362). Bear reading: Q2 sits near a price-cycle high. The MD's Q1 price call was wrong once (C-L646-647). Preform input contracts reset at expiry (C-L333-334). Yearly customer resets pass a price fall into revenue at the next annual review (C-L338). Global capacity may rise 40-50% (analyst, C-L920-921). Separating observation: Q3 realisation per fkm and Q3 Telecom Products revenue.
- Thesis implication, margin (M4): two readings of the claim that "part of the margin is price". Reading A (price widened the spread): fibre prices rose about 20% in the quarter that operating margin reached 24.81% [ROLE 4]; when prices ease, the margin falls back. Reading B (price passed through at a near-constant spread): consolidated gross margin fell from 38.82% in Q1 to 38.25% in Q2 [ROLE 4 2A] while prices rose about 20%. Telecom result margin moved only from 30.44% to 30.85% on Telecom revenue up 46.08% QoQ [ROLE 4 2C]. The MD framed the 20-25% as a fibre raw-material price for cable, "not for every raw material" (C-L869-870). He said buyer and seller reach an equilibrium "so that neither their purchase price is affected too much in percentage nor our profit margin is impacted" (C-L874-876). He said margin falls only on short-term contracts without a reset clause (C-L878-879; M09, M10). On Reading B the Q2 margin gain came from operating leverage, with gross margin flat YoY at 38.25% [ROLE 4 7A], not from price. Separating observation: Q3 gross margin and Q3 Telecom result margin against Q3 realisation per fkm. Margins that hold while realisation eases support Reading B. Margins that fall with realisation support Reading A.
- Follow-up: "What share of Q2's QoQ revenue growth came from price, in percentage points?" (MQ58)

**Exchange 3: EPC loss and unbilled BharatNet work (Q12-Q13, T035-T038, C-L409-443)**
- Question: "When do you start seeing that segment report positive numbers?" (C-L415)
- Response: the Army AMC via BSNL is "in final stage of approval, may be a week or 10 days" (C-L418-423); "last quarter we did a lot of work for BharatNet but ... the expenses were incurred but bills were not raised because the milestones are yet to be completed" (C-L427-429); the file "has to go through 25 different steps", and a query sends it back to step 0 (C-L432-433; M03); "This quarter those bills will be getting submitted" (C-L435); "this loss which you have seen 121 or some crores in the current quarter next two quarters put together should not be more than 7500 crores" (C-L440-441, unreadable); "first quarter of next year you would start seeing profit" (C-L443).
- Said: the Q2 loss came from cost booked before milestone billing; AMC cost runs ahead of a contract not yet signed; Q3 carries catch-up billing; profit from Q1 FY28.
- Not said: the rupee amount of unbilled BharatNet work; whether it sits as revenue-not-recognised or as a contract asset; the readable two-quarter loss ceiling; receivables ageing.
- Thesis implication: this is the only working-capital content on the call. It explains the Turnkey loss (Rs122.58 Cr on Rs136.07 Cr revenue [ROLE 4]) but adds a new unquantified item: completed work waiting for 25-step verification (M03). [INFERENCE] If revenue was not recognised, the unbilled work does not sit in other current assets, and the Rs317.31 Cr rise there [ROLE 4] has another cause. If it was recognised as a contract asset, it may be part of that rise. The call does not say which. Q3 Turnkey will carry catch-up billing for Q2 cost (C-L436-437), so Q3 is not a run-rate quarter. The EPC loss band of Rs80-90 Cr a quarter [MEMORY, broker] was missed, and segment profit moved to Q1 FY28.
- Follow-up: "How much BharatNet work done in Q2 was unbilled at 30-Sep, in Rs Cr, and where does it sit on the balance sheet?" (MQ48)

(Continued in Part 2: Steps 5 to 8.)



---

# ROLE 5 ADDENDUM: PART 2 (Steps 5 to 8)

Part 1 (caveat, preamble, Steps 0-4) precedes this part in the same document. Part 3 (Step 9 to the change log) follows it. The machine-transcript caveat binds every concall finding. Anchors as in Part 1.

### STEP 5: NEW INFORMATION AUDIT

#### 5A. New disclosures (on the call, not in the filing, deck or MA report)

| Disclosure | Type | Material? | Thesis impact |
|---|---|---|---|
| Restructuring: E&Y-advised board committee near recommendation; board meeting about 10 days after it; finalisation within "another couple of weeks" (C-L535-545) | Forward catalyst pre-announced | YES | Trigger #6 test within weeks; scope unstated (CC-FN-06) |
| Aerospace acquisition "within November"; target book "1600" (C-L126), "1800" (C-L273), "16 or 1800" (C-L405); "all the orders are for exports" (C-L276) | New segment entry | YES | Defence FY27 target leans on it; target, price and profit still NOT FOUND (CC-FN-05) |
| Defence FY28 "at least 2000" (C-L251-252); ~5,000 framed three ways: "in expiration [aspiration] ... three years time frame" (C-L252-253); "it should not be difficult for us to reach the 2000 crores figure and a 5000 crores figure" (C-L278-279); later "possibly ... in next two years" (C-L769-770) | Forward catalyst | YES | FY28 raised against broker ~1,500 [MEMORY]; A4 reads Rs5,000 Cr as an aspiration with an inconsistent horizon, not a commitment [INFERENCE], though the MD also said it "should not be difficult" to reach (C-L278-279) (CC-FN-04) |
| Connectivity FY27 "more than 800", Q2 "about 300", Q1 "nil", FY28 Rs2,000 Cr (C-L369-371, C-L796-820) | New product / capability | YES | 2x-2.5x raise for FY28 (CC-FN-12, CC-FN-01) |
| Fibre price up "some 20%" in Q2; telco fibre ~$15 vs DC fibre ~$25-27 (C-L629-631, C-L646-647); customer long-term prices reset "year to year ... it can go down, it can go up" (C-L336-339) | Negative surprise (cyclical driver) | YES | Two readings (Step 4C Exchange 2): price widened the spread, or price passed through at a near-constant spread. Filed counter: gross margin 38.82% to 38.25% QoQ [ROLE 4]. Separating observation: Q3 margins against Q3 realisation per fkm (CC-FN-17) |
| Preform "midterm solution" from Q1 CY2027, nature withheld (C-L580-583, C-L885) | New partnership / undisclosed | YES | Possible capital or related-party commitment (CC-FN-11) |
| Preform supplier contracts yearly, 18 or 24 months; spot "up by 600%"; own 600 MT covers "half" (C-L330-333, C-L705-709, C-L930) | Negative surprise | YES | Input-cost reset at expiry against "no chance worse" margins (CC-FN-10) |
| Hyperscalers "maybe 70 percent ... of the export orders" within the Rs18,500 Cr OFC/DCI book; "I do not have the exact number" (C-L170-173); telecom revenue ~70-30 (C-L305); DC 65-75% of revenue (C-L617) | Customer / contract | YES | Two readings. Upper: 70% of the whole Rs18,500 Cr = ~Rs12,950 Cr = 44.81% of Rs28,900 Cr [COMPUTED]. Lower: 70% of the export part only; the export part of the Rs18,500 Cr is ND. Exports are 57% of the total book (P-L314 [ROLE 4]), so this reading caps hyperscalers at 0.70 x 57% = 39.90% of the book [COMPUTED], at most ~Rs11,535 Cr on filed Rs28,911 Cr. 44.81% is the upper reading, not a firm figure (CC-FN-16) |
| O&M book Rs5,000 Cr; O&M margin "15 to 20 percent" (C-L522-530) | Customer / contract | YES | Positive margin claim beside a loss-making segment; may include unsigned AMC (CC-FN-08) |
| Army AMC via BSNL "a week or 10 days" from signing; cost incurred ahead (C-L418-425) | Negative surprise | YES | Cost runs before contract (CC-FN-07) |
| BharatNet work done, bills not raised pending milestones and a 25-step verification; bills "this quarter" (C-L427-437; M03) | Negative surprise | YES | Unquantified unbilled work (tripwire #4 context) |
| Turnkey profit from Q1 FY28 (C-L443) | Forward catalyst | YES | EPC loss band missed; profit date pushed (CC-FN-07) |
| Debt reduction "will start in the current year"; "substantially" lower Mar-27 and Mar-28 (C-L551-555) | Forward catalyst | YES | Testable; no funding split (CC-FN-09) |
| Utilisation measured "in money terms" (C-L322, C-L507-509) | Definition | YES | Physical headroom unreadable (CC-FN-14) |
| Exports +~493% YoY (C-L78) | Backward | YES | Unverifiable from the filing |
| Second batch of AK-203 thermal weapon sights delivered in September (C-L123) | New contract delivery | NO (small) | Defence delivery data point |
| Ammunition complex: 1,000 acres; revenue in ~2 years; MMHG 800,000-unit tender "participated" (C-L132-133, C-L282-285) | New capex / capacity | YES | Tender not won |
| Germanium not contracted; export restrictions acknowledged (C-L593-600, C-L963-974) | Negative surprise | YES | Input risk for the Oct-2028 preform plant (CC-FN-18) |
| In-DC connectivity certification "already there" (C-L899-900) | Regulatory / certification | NO | Conflicts with in-DC revenue "last quarter of the current financial year" (C-L367-368) |

#### 5B. What was NOT discussed

| Expected topic | Why it should have been discussed | Significance of silence |
|---|---|---|
| Receivables ageing, DSO, unbilled revenue | Tripwire #4; Q1 silent [MEMORY]; Role 4 Q2 | RED (second consecutive quarter; Step 8C) |
| Export-OFC / hyperscaler revenue in Rs Cr | Notion cleanest metric; trigger #1 | RED (declined, C-L516; second quarter; CC-FN-23) |
| Aerospace price and target financials | Role 4 Q6; 86.5% of the defence book in the target [ROLE 4] | AMBER to RED (thesis-relevant; CC-FN-05) |
| Standalone vs consolidated profit gap (47.09% [ROLE 4]) | Q1 Q3; Role 4 Q3 | AMBER (second quarter) |
| Tax charged but unpaid Rs123.40 Cr [ROLE 4] | Role 4 Q42; cash quality | AMBER |
| HASPL Rs90 Cr object and its 31-Dec deadline | Role 4 Q5, Q31 | AMBER |
| Fuze approval | Checklist #4; 5+ quarters of "couple of months" [MEMORY] | RED (second silent quarter; CC-FN-24) |
| BMP-2 sample | Checklist #4 | AMBER |
| Promoter pledge | Checklist #5; trigger #3 | AMBER |
| Nivetti closure (31-Dec-2026) | Checklist #9; slip #5 [MEMORY] | AMBER |
| Warrant conversion, Rs416.25 Cr balance | Funding of capex and preform | AMBER |
| Rs215 Cr DC facility (Sep-2027) | Q1 promise log | AMBER (DROPPED candidate) |
| Dec-2026 capacity step date | Q1 promise log; growth trigger 2 | AMBER (DROPPED candidate) |
| Export-share target (65%+ vs >70%) | Deck conflict (PPT-FN-06) | AMBER |
| Mobilisation and LC terms | Checklist #8, #12 | AMBER |
| HTL minority holding and transfer price | Notion open item | AMBER |
| Peer concalls | Protocol peer cross-check | UNVERIFIABLE this run (none passed) |

---

### STEP 6: TONE AND SPECIFICITY

#### 6A. Tone comparison (prior concall not transcribed; prior phrases from memory, labelled)

| Topic | Prior phrase [MEMORY] | This call | Direction |
|---|---|---|---|
| FY27 revenue | "aspiration" ~40% (Q1) | "we expect ... at least 80%" (C-L108) | UPGRADED |
| Defence FY28 | ~Rs1,500 Cr (broker 05-Oct) | "at least 2000" (C-L252) | UPGRADED |
| Defence long term | Rs4,000-5,000 Cr by FY30 (broker) | ~5,000 as an aspiration in "three years" (C-L252-253) / "possibly ... in next two years" (C-L770) | UPGRADED (aspiration; horizon inconsistent) |
| Connectivity | Rs800-1,000 Cr FY27-28 (seed) | Rs2,000 Cr FY28 (C-L371) | UPGRADED |
| Margin | 22-25% by FY29 (seed); ~25-26% after captive preform (broker) | "no chance ... worse" (C-L202) | UPGRADED |
| EPC losses | Rs80-90 Cr a quarter "for one or two more quarters" (broker) | Q2 "121"; profit "first quarter of next year" (C-L440-443) | DOWNGRADED |
| Capacity | OF 33.9 / OFC 42.36 mn fkm "by Dec 2026" | Steps undated (C-L361-362) | DOWNGRADED (date dropped) |
| Fuze | "couple of months" (Q4 FY26) | Product list only (C-L122) | DROPPED |
| Fibre price | "looks to be stabilizing" (Q1, as the MD recalls, C-L646) | "gone up by some 20% ... now see more or less stabilizing" (C-L644-647) | MAINTAINED (same call repeated after a miss) |
| Debt | ~Rs1,700 Cr to fall by end-FY28 (broker) | Reduction "will start in the current year" (C-L552) | UPGRADED |
| Receivables | "I don't have this detail as immediately available" (Q4 FY26) | Not discussed | DROPPED |
| Aerospace | "proposed" (Q1) | "within November" (C-L404) | UPGRADED |

#### 6B. Specificity score (rule applied to every A1 FORWARD row, R235-R346, 112 rows)

Rule: a forward row is QUANTIFIED if its cited line, or its A1 note, carries (a) a number for a company or market variable, or (b) a stated date or bounded period attached to a testable outcome (an event, or the direction of a named metric). Unbounded timing words ("soon", "in due course", "next few months", "in future", "immediately") do not count. A number the A3 marks unreadable (C-L441) does not count. Each A1 row is scored once, so a statement repeated in several rows counts each time.

- QUANTIFIED (45): R242, R243, R244, R245, R246, R261, R262, R263, R264, R267, R269, R270, R277, R278, R280, R281, R282, R285, R288, R289, R290, R291, R292, R294, R295, R297, R298, R299, R301, R303, R308, R309, R310, R312, R314, R316, R317, R318, R321, R322, R324, R328, R329, R333, R340.
- UNQUANTIFIED (67): R235, R236, R237, R238, R239, R240, R241, R247, R248, R249, R250, R251, R252, R253, R254, R255, R256, R257, R258, R259, R260, R265, R266, R268, R271, R272, R273, R274, R275, R276, R279, R283, R284, R286, R287, R293, R296, R300, R302, R304, R305, R306, R307, R311, R313, R315, R319, R320, R323, R325, R326, R327, R330, R331, R332, R334, R335, R336, R337, R338, R339, R341, R342, R343, R344, R345, R346.
- Specificity ratio = 45 / 112 = 0.40 [COMPUTED]. Band: 0.3-0.5, moderate.
- Excluding only the three quantified market-size rows (R298, R299, R301): 42 / 109 = 0.39. Same band.
- Borderline calls stated: R307 (board meeting; the "week or 10 days" sits on C-L540, not on its line C-L541) is UNQUANTIFIED; R308 (finalise "another couple of weeks", in its A1 note) is QUANTIFIED. R304-R306 (FY28 "better", C-L487-498) are UNQUANTIFIED because their lines carry no date; FY28 is named only on C-L486. R316 (germanium "two years from now", C-L600) is an MD statement under the A3 turn-mapping note and is QUANTIFIED.
- Further borderline rows scored UNQUANTIFIED: R313 (note "28 timeline"; C-L586 "when we talked about 28") arguably passes rule (b), which gives 46 / 112 = 0.41. R271 (note "800,000"), R320 (C-L647 "20%") and R302 (C-L484 "10,000") carry numbers from an adjacent clause or row; counting all four gives up to 48 / 112 = 0.43 [COMPUTED].
- Sensitivity, A2 loop-1 forward rows: M02 (consolidation "in this quarter itself", C-L274-275) is QUANTIFIED under rule (b). M04 (international telco orders, C-L676) is UNQUANTIFIED. M07 (orders above supply, C-L755-756) is UNQUANTIFIED, because its "5500" is the backward Q2 inflow. With them: 46 / 115 = 0.40 [COMPUTED]. Soft untagged repeats (C-L135, C-L136-138, C-L463, C-L471, C-L490) would move the ratio to about 0.38 (A5 count).
- Range on every reading: 0.38 to 0.43. The band, the quadrant and the archetype are unchanged.

#### 6C. Defensive language patterns

| # | Phrase | Line |
|---|---|---|
| 1 | "I do not have the exact number" (hyperscaler share) | C-L171 |
| 2 | "They will end under NDA" (customer names) | C-L170 |
| 3 | "I would avoid giving any guidance for 28" | C-L484 |
| 4 | "it's too early to give a guidance" | C-L486 |
| 5 | "I do not have that number in particular" ($1.1B order revenue) | C-L516 |
| 6 | "I cannot give you more details ... commercial confidentiality" | C-L580-581 |
| 7 | "It's too early to finalize content" (germanium) | C-L594 |
| 8 | "I cannot comment on what somebody else is doing" (peers) | C-L690 |
| 9 | "I do not have the right number" (Q2 connectivity) | C-L796 |
| 10 | "very difficult to say" (price vs volume) | C-L845 |
| 11 | "Cannot give you a ballpark number" | C-L853 |
| 12 | "I cannot elaborate this is a trade statement" | C-L885 |

Count: 12 (above 5: hedge-heavy on delivered-period data). Prior concall count: ND (Q1 not transcribed). A2 also tagged 66 hedge qualifiers in the transcript (ledger partition). The hedges sit on delivered numbers; the forward targets come as round numbers with "surely" (C-L408) and "no chance" (C-L202) (CC-FN-15).

#### 6D. Confidence indicators

- Promoter on the call answering operational questions directly (all answers, speaker inferred).
- Specific dates: aerospace close "within November" (C-L404); Turnkey profit Q1 FY28 (C-L443); preform solution Q1 CY2027 (C-L582); preform plant Oct-2028 (C-L588); restructuring board meeting about 10 days after the recommendation (C-L539-541); AMC signing in about 10 days (C-L423).
- Numerical commitments: defence FY27 Rs500-600 Cr and FY28 Rs2,000 Cr+; connectivity FY27 Rs800 Cr+ and FY28 Rs2,000 Cr. A4 reads the ~Rs5,000 Cr defence figure as NOT a commitment [INFERENCE]: the MD framed it as an aspiration ("in expiration", C-L252) and later as "possibly" (C-L770), and the analyst called these figures "your aspirations" (C-L713). Between those two framings the MD also gave a confidence line on the same figure: "it should not be difficult for us to reach the 2000 crores figure and a 5000 crores figure" (C-L278-279).
- An acknowledged miss with a recovery date: the EPC loss is explained and dated (C-L416-443).
- A named delivery: second AK-203 thermal-sight batch (C-L123).

#### 6E. Management archetype

- Specificity: 0.40 (range 0.38-0.43; at or below 0.5 on every reading).
- Credibility: formal trailing-4 ratio ND; provisional 40.0% (Step 3B; 50.0% with DELAYED at 0.5), below 60% on every reading.
- Quadrant (provisional): EVASIVE (specificity at or below 0.5, credibility below 60%). Grade D treatment would apply if confirmed: the call contributes mainly a governance signal.
- Overlay: the forward targets carry OVERPROMISER traits (round, raised inside one call and against broker figures two weeks earlier, CC-FN-04, CC-FN-12), while delivered-period splits are withheld (CC-FN-15).
- Shift flag: the Notion label was "provisional OVERPROMISER-watch" with Q1 specificity ~0.81 [MEMORY]. That figure came from a seed log, not a transcript, so the drop to 0.40 is partly a method change. The archetype shift is flagged for the operator, not ruled.

---

### STEP 7: CROSS-REFERENCE

#### 7A. Concall narrative vs filing numbers

| Concall claim | Filing evidence [ROLE 4] | Reconciliation |
|---|---|---|
| PBT, PAT, revenue, YoY and QoQ figures (C-L59-66) | R-L804-822, R-L715-721 | CONFIRMED |
| EBITDA margin 25.89% (C-L68) | Reported basis includes other income; operating 24.81% | PARTIALLY CONFIRMED (basis unstated) |
| Order book Rs28,900 Cr (C-L85) | Rs28,911 Cr (R-L681) | CONFIRMED |
| Last quarter's book "26,000", hedged: "I think ... if I am not [mistaken]" (C-L750-751) | Q1 deck Rs26,665 Cr (P-L302) | ROUNDED (hedged recollection, 2.5% below the filed figure; filing governs; not counted as a credibility contradiction) |
| Q2 inflow "5500" (C-L755) | ~Rs4,788 Cr [COMPUTED: 28,911 - 26,665 + 2,541.79] | PARTIALLY CONFIRMED (spoken inflow about Rs700 Cr above the filed basis) |
| Exports +~493% YoY (C-L78) | No export revenue line filed | UNVERIFIABLE |
| Margins "better only", "no one-time" (C-L201-202, C-L560) | Gross margin flat YoY at 38.25% and down QoQ from 38.82%; gain from operating leverage; no exceptional item; inventory release ~43.13 at cost and seasonal employee cost in Q2 | PARTIALLY CONFIRMED |
| Turnkey loss "121 or some crores" (C-L440) | Rs122.58 Cr (R-L846) | CONFIRMED |
| BharatNet cost booked, bills not raised (C-L427-429) | Turnkey revenue 136.07, loss 122.58; other current assets +317.31 unlabelled | UNVERIFIABLE (where the unbilled work sits) |
| Debt reduction "will start in the current year" (C-L552) | Gross borrowings +126.76 in H1 to 1,840.13 | CONTRADICTED in H1; testable at 31-Mar-2027 |
| Current cable capacity "34" (C-L361, C-L716) | Deck "Current: 39 mn fkm" (P-L434) | CONTRADICTED (company documents disagree) |
| Defence H1 "around 80" (analyst, C-L776) | Rs78.68 Cr (R-L840) | CONFIRMED |
| Q1 connectivity "nil" (C-L819) | Not segment-disclosed | UNVERIFIABLE |
| Pending capex Rs1,800 Cr (C-L785) | Rs1,800 Cr (R-L706; P-L118) | CONFIRMED |
| Aerospace book "1600" / "1800" (C-L126, C-L273) | Deck ~Rs1,600 Cr (P-L469-470) | PARTIALLY CONFIRMED (two figures on the call) |

#### 7B. Peer concall cross-check

No peer concall was passed to this run: UNVERIFIABLE this run. The direct peer on file is STLTECH [MEMORY]; no Q2 data in the inputs. An analyst cited an Indian peer at ~20% and a global peer at ~30% telecom margin (C-L654-659); these are analyst figures, unverifiable, and the MD declined to compare (C-L690-692).

#### 7C. Concall vs external channel (broker summary of 05-Oct, MGMT via broker [MEMORY, SECONDARY])

| Concall claim | External source | External says | Alignment |
|---|---|---|---|
| FY27 growth "at least 80%"; history "20-40, 40-80" (C-L108-109) | Broker 05-Oct | Guide "raised from 20% to 40% and now to at least 60%" | NOT ALIGNED: the 60% step is missing from the MD's history; the guide rose again in 14 days |
| Defence FY28 "at least 2000" (C-L252) | Broker | ~Rs1,500 Cr next year | NOT ALIGNED (higher) |
| Defence ~5,000 in 2-3 years (aspiration, C-L252-253, C-L770) | Broker | Rs4,000-5,000 Cr by FY30 | NOT ALIGNED (earlier) |
| Margins "no chance ... worse" | Broker | 23.25% sustainable; ~25-26% after captive preform | DIRECTIONALLY ALIGNED |
| EPC loss Q2 "121" | Broker | Rs80-90 Cr a quarter for one or two quarters | NOT ALIGNED (miss) |
| Debt reduction starts FY27 | Broker | ~Rs1,700 Cr to fall by end-FY28 | ALIGNED, pulled forward |

Pattern: numbers on the call run above figures relayed two weeks earlier. This is a candidate entry for the Notion narrative-amplification counter (now 2 [MEMORY]); the operator rules.

---

### STEP 8: UPDATE THESIS AND POSITION DECISION

#### 8A. Growth trigger status

| Trigger [MEMORY] | Status pre-concall (Role 4 6D) | Concall evidence | Status post-concall |
|---|---|---|---|
| 1. Hyperscaler OFC contract | ON TRACK (indirect) | "already started delivering" (C-L516-517); hyperscalers "maybe 70 percent ... of the export orders" in the Rs18,500 Cr book (C-L170-173), so up to 39.90% of the total book if the 70% applies only to export orders (a ceiling; the share may be lower), or 44.81% if it applies to the whole Rs18,500 Cr (Step 5A); "other Hyperscaler orders" (C-L518-520); revenue withheld | ON TRACK (still unverified) |
| 2. Capacity by Dec-2026 | DELAYED | Steps restated without dates; current cable "34" vs deck 39 (C-L361-362) | DELAYED |
| 3. HASPL aerospace consolidation | DELAYED | Close "within November" (C-L404); revenue consolidated after completion (C-L274-275; M02); price and target profit not given | DELAYED (re-dated inside CY26) |
| 4. PCS / interconnect / DC connectivity | ON TRACK (narrative) | Q2 ~Rs300 Cr hedged; FY27 Rs800 Cr+; FY28 Rs2,000 Cr (C-L369-371, C-L796-802) | ON TRACK (raised; number unverified) |
| 5. Defence indigenisation | DELAYED | FY27 and FY28 targets raised; Rs5,000 Cr an aspiration; fuze silent; radar trial pending; MMHG tender "participated" (C-L251-285, C-L397-399) | DELAYED |
| NEW: fibre price upcycle | n.a. | Q2 price +~20% (C-L647); "some increase, but not as much" ahead; customer prices reset yearly in both directions (C-L336-339) | NEW (cyclical, not structural; two margin readings, Step 4C Exchange 2) |
| NEW: restructuring outcome | n.a. | Decision about early to mid November (C-L535-545) | NEW (binary catalyst) |

#### 8B. Watchlist items: concall-specific updates

| # | Watchlist item | This concall reading | Status (post-concall) |
|---|---|---|---|
| 1 / G5 | Export-OFC revenue (>= Rs1,800 Cr a quarter) | Declined (C-L516) | UNKNOWN (withheld second quarter) |
| 2 / G4 | Receivables ageing, unbilled (tripwire #4) | Not discussed; BharatNet bills unraised, unquantified (C-L427-437) | RED (Step 8C ruling) |
| 3 | Telecom product margin (>= 17%) | Analyst "32, 33%" (C-L661); filed segment margin 30.85% [ROLE 4] | GREEN |
| 4 | Defence delivery (fuze, MMHG, BMP-2) | Fuze silent; MMHG tender participated (C-L284); BMP-2 silent | AMBER (green deadline passed; no red event) |
| 5 | Promoter holding and pledge | Not discussed | GREEN holding / UNKNOWN pledge |
| 6-7 | BharatNet III revenue, WC, margin | Cause of loss explained; no Rs figures (C-L427-438) | RED |
| 8 | Mobilisation / LC | Not discussed | UNKNOWN |
| 9 | Nivetti | Not discussed | RED (memory event; silent) |
| 10 | Second hyperscaler customer | "we have some other Hyperscaler orders" (C-L518-520) | AMBER (yes, no size) |
| G2 | EPC loss vs Rs80-90 Cr guide | "121" (C-L440); profit Q1 FY28 (C-L443) | RED |

#### 8C. Thesis-broken trigger check (rulings)

| Condition [MEMORY] | Threshold | Concall-relevant evidence | FIRED? |
|---|---|---|---|
| 1. Hyperscaler delivery | below 60% pro-rata by H1 FY28 | Delivery metric withheld again (C-L516; CC-FN-23) | NO. Flag: the trigger has no metric to test against at its date |
| 2. Promoter holding | below 25% | Not discussed; 28.29% filed (P-L569) | NO |
| 3. Promoter pledge | any initiation | Not discussed | NO on evidence; UNCONFIRMED |
| 4. Receivables silence / unbilled | two consecutive quarters of receivables silence, OR above Rs200 Cr unexplained unbilled increase | Silence limb: Q1 silent on ageing, DSO and unbilled (13-Oct review [MEMORY]). Q2 silent on the same items in the results, the deck (PPT-FN-12) and the call (CC-FN-22). The only call content is qualitative: BharatNet "bills were not raised" (C-L428-429). Role 4 6C pre-committed the test: "Fires if the Role 5 addendum shows the call was silent on ageing and unbilled" [ROLE 4 6C]. Unbilled limb: no rupee figure anywhere; other current assets +317.31 are unlabelled [ROLE 4] | **FIRED on the silence limb** (the most evidenced reading on the trigger wording and the Role 4 pre-commitment). Unbilled limb UNTESTABLE (no number to test) |
| 5. CARE rating | below A-/A2+ | Not discussed | NO |
| 6. Restructuring value transfer | structure that moves OFC/defence value to a private entity at a discount | Committee near recommendation; board meeting about 10 days after it; finalisation within about 2 weeks; scope unstated (C-L535-547) | NO. IMMINENT TEST (about early to mid November 2026) |

Tripwire #4 ruling, with both readings:
- Reading A (fired): the trigger targets management disclosure of receivables quality. Ageing, DSO and unbilled were absent in Q1 and in every Q2 channel. The MD added unquantified unbilled BharatNet work. Two consecutive silent quarters meet the trigger's own wording. The Notion G4 green test is "ageing and unbilled disclosed" [ROLE 4 6B], and Role 4 pre-committed this firing condition before the call was read.
- Reading B (not fired): the H1 balance sheet discloses receivables in rupees. Computed days improved from 183.04 to 140.78 on the total TTM basis [ROLE 4 5A]. That level still sits ABOVE the Notion red line of 130 days. Current-only days of 128.14 sit between green 110 and red 130. Only TR/TTM at 38.57% sits inside the Notion green band (45% or less). Role 4 scores watchlist item 2 AMBER and BUY-gate leg (b) NOT MET [ROLE 4 6B, 8A-W]. On the call, no analyst asked, so management did not refuse. The Q1 silence rests on memory, not a scored transcript.
- Weight: Reading B rests on improving days and the absence of a question. Its level evidence is mixed at best. The corrected Reading B is weaker than the loop-0 text stated, so the FIRED ruling stands and gains strength.
- Separating observation: a direct written request. If the IR reply to Q2 (ageing over 6 months and unbilled revenue at 30-Sep-2026) gives the numbers, Reading B gains; if it does not, Reading A is confirmed.
- What would reverse the ruling: a filed or written disclosure of ageing and unbilled revenue at 30-Sep-2026, with over-6-month ageing at or below 25% (Notion red line) and the +317.31 rise in other current assets explained.
- Consequence under 8A-W: "Reclassify to AVOID; record what would need to reverse." This is a PROPOSAL for the operator. Decision Status is not written.

Trigger #6 pre-committed test (for the filed structure): (i) which entity keeps listed minority holders; (ii) whether OFC, defence or aerospace assets move; (iii) any swap ratio or price; (iv) any promoter or related-party participation. A structure that moves OFC or defence value to an entity where listed holders own less, or at a discount, fires #6 (Notion hard-exit rule).

#### 8D. Four-Pillar inputs: deferred to /fttcp and Role 1 (OR-30)

Concall facts flagged for the deferred recompute (no pillar is revised here):
- Pillar 1 (ROCE via FTTCP): Q2 carries a ~20% fibre price rise (C-L647); preform contracts reset at expiry (C-L333-334); customer prices reset yearly in both directions (C-L336-339); own preform covers half of capacity from Oct-2028 (C-L705-708). Two readings of the price effect: (A) price widened the spread, so margin is at risk when price eases; (B) price passed through at a near-constant spread, with filed gross margin down from 38.82% to 38.25% QoQ and Telecom result margin only 30.44% to 30.85% [ROLE 4], and the MD's equilibrium account (C-L874-876). Separating observation: Q3 gross and Telecom result margins against Q3 realisation per fkm. The FTTCP ROCE forward verdict must weigh both.
- Pillar 2 (cash): no cash numbers on the call; debt reduction promised (C-L552-555) against H1 debt up; unbilled BharatNet work unquantified; tax accrual silent. Both Role 4 readings stand (H1 CFO/PAT 0.71 reported, 0.52 with tax counted when charged).
- Growth visibility: connectivity FY28 Rs2,000 Cr; defence FY28 Rs2,000 Cr+; defence ~Rs5,000 Cr as an aspiration only (C-L252-253, C-L770); book Rs28,900 Cr with ~5,500 spoken inflow (filed basis ~4,788); hyperscaler share of the book 39.90% (lower reading, cap) to 44.81% (upper reading) [COMPUTED]; the 70% base is "the export orders" (C-L171-173), so 44.81% is not a firm input.
- Strategic premium: restructuring decision pending; aerospace target unpriced (multiple NOT COMPUTABLE, no accretion credited); preform solution undisclosed.
- Track record (Role 1 scenario weights): formal ratio ND; provisional Grade C (Mixed).

#### 8E. Position decision

Decision Status verified: WATCHLIST ("DO NOT INITIATE"), not held. Branch: 8A-W.
- Thesis-broken trigger #4 FIRED (silence limb). 8A-W rule: reclassify to AVOID and record what would reverse it (8C). PROPOSAL only; the operator sets Decision Status.
- Concall overrides: provisional credibility below 60%, so discount management commentary by 30-50% and tighten add-back triggers. One confirmed DROPPED (two candidates): no automatic downgrade yet. Narrative contradicts the filing on debt direction (H1) and on current cable capacity: the filing governs; credibility issue logged. The prior order book "26,000" is a hedged rounding (Step 7A), not counted as a contradiction.
- If the operator keeps WATCHLIST: entry zone Rs60-75 unchanged pending /fttcp and Role 1; add tightener (h): written disclosure of receivables ageing and unbilled revenue at 30-Sep-2026, and (i) the restructuring filed with every resulting entity mirroring listed HFCL's shareholding.

#### 8F. Updated questions for next quarter

See Section 3A (MQ43-MQ61) and the Q1-Q42 status update in Section 3B.

(Continued in Part 3: Step 9 to the change log.)



---

# ROLE 5 ADDENDUM: PART 3 (Step 9, Sections 3 to 7, loop 1 and loop 2 change logs)

Parts 1 and 2 precede this part in the same document. The machine-transcript caveat binds every concall finding. Anchors as in Part 1.

### STEP 9: NOTION SAVE (payload only; not written by A4)

Supersession: the Role 5 Step 9B Key Notes line and Decision-Status proposal below supersede, for the save, the Role 4 Step 9 clauses "Proposed: no change (WATCHLIST, DO NOT INITIATE). No trigger fired." and the Role 4 Key Notes words "No trigger fired". Those clauses were written before the call was read.

#### 9A. Commitment register from this call (log starts; all UNCLEAR until due)

| # | Commitment | Implied date | Line |
|---|---|---|---|
| 1 | FY27 revenue growth at least 80% | FY27 | C-L104-108 |
| 2 | Q3 revenue above Q2 | Q3 FY27 | C-L607-611 |
| 3 | Q2 is not a peak | undated | C-L88-89 |
| 4 | Rs10,000 Cr revenue "much before" FY29 | before FY29 | C-L109-110, C-L484-485 |
| 5 | FY28 "better than what we are doing now" | FY28 | C-L486-495 |
| 6 | Pipeline converting; order book to strengthen; "orders would be more than the supply we do" | undated | C-L86-93, C-L755-756 (M07) |
| 7 | ~Rs1,800 Cr capex pending | to Oct-2028 | C-L112-113, C-L785 |
| 8 | Fibre 28 to 34 to 43; cable 34 to 63 mn fkm | undated | C-L360-362, C-L716-717 |
| 9 | Preform plant construction "soon" | undated | C-L377 |
| 10 | Own preform 600 MT | Oct-2028 | C-L377-378, C-L588 |
| 11 | Preform midterm solution | Q1 CY2027 | C-L580-583 |
| 12 | Germanium supply tie-up | before Oct-2028 | C-L593-600, C-L963-970 |
| 13 | Margins "better only"; "no chance ... worse" | undated | C-L201-202, C-L343 |
| 14 | Connectivity revenue more than Rs800 Cr | FY27 | C-L369-370, C-L815-816 |
| 15 | Connectivity revenue Rs2,000 Cr | FY28 | C-L371, C-L858 |
| 16 | In-DC connectivity products start revenue | Q4 FY27 or early FY28 | C-L366-369 |
| 17 | Aerospace acquisition completes | within Nov-2026 | C-L124, C-L273-274, C-L404 |
| 18 | Aerospace revenue consolidated after completion | Q3 FY27 | C-L274-275 (M02), C-L406 |
| 19 | Large aerospace export orders | "next few months" | C-L276-277 |
| 20 | Defence revenue Rs500-600 Cr | FY27 | C-L129-130, C-L251, C-L407-408 |
| 21 | Defence revenue at least Rs2,000 Cr | FY28 | C-L251-252, C-L278, C-L769 |
| 22 | Defence revenue ~Rs5,000 Cr. A4 classification: ASPIRATION, not a commitment [INFERENCE from C-L252, C-L713, C-L770]. The MD framed it three ways: "in expiration [aspiration], if you take it in three years time frame" (C-L252-253); "it should not be difficult for us to reach the 2000 crores figure and a 5000 crores figure" (C-L278-279); "possibly ... in next two years" (C-L770). Scored as an aspiration from Q3 FY27 onward; the scorer weighs all three framings | 2 or 3 years (FY29 or FY30) | C-L252-253, C-L278-279, C-L770 |
| 23 | Foliage radar second trial / approval | ~2 weeks | C-L262-263, C-L397-399 |
| 24 | Ground surveillance radar export orders | undated | C-L268-269 |
| 25 | Ammunition complex construction; revenue in ~2 years | soon; ~late 2028 | C-L134, C-L281-283 |
| 26 | MMHG 800,000-unit tender (participated) | undated | C-L284-285 |
| 27 | Army AMC via BSNL approved and signed | ~a week or 10 days | C-L418-423 |
| 28 | BharatNet milestone bills submitted | Q3 FY27 | C-L435-437 |
| 29 | No repeat of the unbilled-cost Turnkey loss; two-quarter ceiling (unreadable) | Q3-Q4 FY27 | C-L438-441 |
| 30 | Turnkey segment profit | Q1 FY28 | C-L443 |
| 31 | Restructuring recommendation, board meeting, decision | ~early to mid Nov-2026 | C-L535-545 |
| 32 | Debt reduction starts FY27; substantially lower Mar-27 and Mar-28 | 31-Mar-2027 / 31-Mar-2028 | C-L551-555 |
| 33 | Large telco orders, Indian and international | undated | C-L243-245, C-L675-676 (M04) |
| 34 | IR to "immediately reply" to emailed queries | immediate (from 19-Oct-2026) | C-L1011-1014 |

#### 9B. Concall verdict block

- Management credibility (this quarter): provisional Grade C (Mixed).
- Trailing 4-quarter credibility ratio: ND formally (prior log not passed); provisional 40.0% (4.0 points / 10 scored commitments; 50.0% with DELAYED at 0.5).
- Management archetype (6E): provisional EVASIVE, with OVERPROMISER traits on forward targets; shift from "provisional OVERPROMISER-watch" flagged.
- Role 1 track-record input: ND formally; provisional Mixed.
- Net concall impact on thesis: WEAKENED. Growth narrative strengthened (Q3 growth promise, raised FY27 and FY28 targets), but disclosure and governance weakened (receivables silent a second quarter, trigger #4 fired; acquisition unpriced; preform solution withheld; restructuring scope unstated). Three positive claims are bounded: the H2 case has no price floor and no new capacity; hyperscalers are up to 39.90% of the book if the 70% applies only to export orders (a ceiling; the share may be lower), or 44.81% if it applies to the whole Rs18,500 Cr; defence Rs5,000 Cr is an aspiration.
- Position decision: 8A-W. Proposal: reclassify to AVOID under the fired tripwire #4 (operator decides). If kept on WATCHLIST: entry zone Rs60-75 unchanged, tighteners (h) and (i) added.
- Key Notes line (proposed): "20-Oct-2026 Q2 FY27 Role 5 [machine transcript]: MD guides FY27 >=80% as a floor, 'definitely growth in Q3'; Q2 fibre price +~20%, customer prices reset yearly up or down; gross margin 38.82% to 38.25% QoQ, so price effect on margin unproven. Defence FY28 >=Rs2,000 Cr (Rs5,000 Cr an aspiration), connectivity FY28 Rs2,000 Cr (raised). Hyperscalers ~70% of export orders (up to 39.90% of book on that base, may be lower; 44.81% only if the 70% covers the whole Rs18,500 Cr). E&Y restructuring committee near recommendation; board ~10 days after, decision ~mid-Nov (trigger #6 test). Aerospace close 'within November', unpriced. Receivables ageing/unbilled silent second quarter: tripwire #4 FIRED (silence limb), proposal AVOID, operator decides. Specificity 0.40; provisional credibility 40% (C); provisional archetype EVASIVE."

---

## (3) ADDITIONS TO STEP 8.5

### 3A. New management questions MQ43-MQ61 (IR email; channel committed at C-L1011-1014)

| # | Question | Why it matters | Bull answer | Bear answer | From finding |
|---|---|---|---|---|---|
| MQ43 | Which businesses are in scope of the restructuring the committee will recommend (EPC only, or OFC, defence or aerospace too)? Will every resulting entity have the same shareholding as listed HFCL today? Yes or no. | Trigger #6 test in weeks | EPC-only carve-out; mirror shareholding | Product or defence assets move; non-mirror holding | CC-FN-06 |
| MQ44 | Is the "at least 80%" FY27 growth measured on consolidated FY26 revenue of Rs4,949.27 Cr? | Basis still unstated after two disclosures | Consolidated, confirmed in writing | No basis given | CC-FN-02 |
| MQ45 | In which fiscal year do you expect revenue to first exceed Rs10,000 Cr? | Guidance by inference ("see the run rate") | FY28 named | No year | CC-FN-03 |
| MQ46 | Is the ~Rs5,000 Cr defence figure a target or an aspiration, and is it for FY29 or FY30? Of the FY27 Rs500-600 Cr, how much is own business and how much the acquired aerospace target? | Called an aspiration with two horizons in one call; H2 needs 5.35x-6.63x H1 | Target with one year named; split given | Aspiration only; no split; horizon unclear | CC-FN-04 |
| MQ47 | Is the aerospace target's book Rs1,600 Cr or Rs1,800 Cr, and is it executed or unexecuted? | Three figures in one call | One figure, unexecuted, in writing | Inconsistent again | CC-FN-05 |
| MQ48 | How much BharatNet work done in Q2 was unbilled at 30-Sep-2026, in Rs Cr, and on which balance-sheet line does it sit? What is the two-quarter Turnkey loss ceiling in Rs Cr? | Tripwire #4 context; C-L441 unreadable | Amount and line given; ceiling stated | No amount | CC-FN-07 |
| MQ49 | Does the Rs5,000 Cr O&M book include the Army AMC via BSNL that was not signed on 19-Oct? Has it been signed? | "Secured" book may include an unsigned contract | Excluded, or now signed | Included and unsigned | CC-FN-08 |
| MQ50 | What gross borrowings do you expect at 31-Mar-2027, in Rs Cr, given Rs1,800 Cr of pending capex and H2 advance tax? | Debt promise vs H1 debt up Rs126.76 Cr | Below Rs1,840.13 Cr with a funding plan | No figure | CC-FN-09 |
| MQ51 | When do the current preform supply contracts expire, and what share of FY28 preform need is at fixed prices? Which customer contracts reprice in H2 FY27, and what share of the book is in short-term contracts without a reset clause? | Input-cost reset vs "no chance worse" margins; yearly customer resets | Most of FY28 fixed; few H2 resets | Expiries within FY27-28 at spot; large short-term share | CC-FN-10 |
| MQ52 | What is the preform "midterm solution" from Q1 CY2027 (tolling, partner, purchase), is the counterparty a related party, and what capital does it commit? | Undisclosed commitment | Arm's-length, small capital | Related party or large capital | CC-FN-11 |
| MQ53 | What was connectivity revenue in Q1 and Q2 FY27, in Rs Cr, and is the Rs215 Cr DC-connectivity facility still planned for Sep-2027? | Q1 "nil" vs "fixed"; Q2 hedged; facility unmentioned | Rs figures given; facility dated | No figures; facility dropped | CC-FN-01, CC-FN-12 |
| MQ54 | Is current cable capacity 34 or 39 mn fkm, and when does fibre reach 34 mn fkm? | Call vs deck conflict; Dec-2026 step undated | One figure; date given | No date | CC-FN-13 |
| MQ55 | What was Q2 physical output in fkm for fibre and cable against installed capacity? | Utilisation given "in money terms" | Physical figures | Money basis only | CC-FN-14 |
| MQ56 | Will the CFO provide H1 export-OFC revenue, Q2 connectivity revenue and the Q2 price vs volume split in writing? | Delivered-period splits withheld | Provided | Declined again | CC-FN-15 |
| MQ57 | Is the ~70% hyperscaler share measured on the export orders or on the full Rs18,500 Cr OFC/DCI book? What share of that book is the single $1.1B hyperscaler order, and how many hyperscaler customers are in it? | Concentration risk; 39.90% vs 44.81% of the book depends on the base | Full-book basis stated; several customers; single order a minority | Export basis only; one customer dominates | CC-FN-16 |
| MQ58 | What share of Q2's 32.73% QoQ revenue growth came from price, in percentage points, and what was Q3 realisation per fkm against Q2? | Margin durability; separates the two margin readings | Mostly volume and mix | Mostly price | CC-FN-17 |
| MQ59 | By what date will germanium supply be contracted, and from which countries? | Oct-2028 preform input risk | Dated contract, diversified sources | Undated; restricted sources | CC-FN-18 |
| MQ60 | When will the company reply to the emailed questions, and will it file an official transcript of the 19-Oct call? | Channel commitment; audio gaps | Reply within two weeks; transcript filed | No reply; no transcript | CC-FN-25, CC-FN-21 |
| MQ61 | What is the status and date of fuze approval? | Checklist #4; silent two quarters | Approval date filed | Silent again | CC-FN-24 |

Coverage of CC FORWARD-SIGNAL and AMBIGUOUS findings (19 of 19): CC-FN-01 MQ53; CC-FN-02 MQ44; CC-FN-03 MQ45; CC-FN-04 MQ46; CC-FN-05 MQ47; CC-FN-06 MQ43; CC-FN-07 MQ48; CC-FN-08 MQ49; CC-FN-09 MQ50; CC-FN-10 MQ51; CC-FN-11 MQ52; CC-FN-12 MQ53; CC-FN-13 MQ54; CC-FN-14 MQ55; CC-FN-15 MQ56; CC-FN-16 MQ57; CC-FN-17 MQ58; CC-FN-18 MQ59; CC-FN-25 MQ60. Confirmatory negatives route to existing or new rows: CC-FN-22 to Role 4 Q2 and MQ48; CC-FN-23 to Role 4 Q8 and MQ56; CC-FN-24 to MQ61. Neutral facts: CC-FN-19 (Step 7A), CC-FN-20 (Step 7A), CC-FN-21 (MQ60).

Top 3 by likelihood of thesis-changing information: MQ43 (restructuring scope; trigger #6), Role 4 Q2 with MQ48 (receivables and unbilled; tripwire #4 reversal), MQ58 (price share of growth; margin durability). Channel: IR email now (the call has passed); the MD committed to "immediately reply" (C-L1013). Score the reply date as commitment 34.

### 3B. Status update for Role 4 Q1-Q42 (after the call; protocol categories)

| Q | Topic | Status | Basis (line / CC-FN) |
|---|---|---|---|
| 1 | Strategic options: under 100% economics? | PARTIALLY ANSWERED | Timing only (C-L535-547); scope not given |
| 2 | Receivables over 6 months; unbilled | NOT ADDRESSED | Not asked; qualitative only (C-L427-438) |
| 3 | Consolidated vs standalone PAT gap | NOT ADDRESSED | Not asked |
| 4 | Guide basis; Q3 below Q2? | PARTIALLY ANSWERED | Q3 growth "definitely" (C-L608); basis not stated |
| 5 | Defence CPs; Rs90 Cr by 31-Dec | PARTIALLY ANSWERED | Close "within November" (C-L404); CPs and Rs90 Cr not discussed |
| 6 | Acquisition price; target financials | NOT ADDRESSED | Only book size and export orders (C-L273-276) |
| 7 | Quarter Turnkey reaches zero | ANSWERED SPECIFICALLY | "first quarter of next year" (C-L443) |
| 8 | Q2 export-OFC revenue | EVADED | "I do not have that number in particular" (C-L516) |
| 9 | Warrant conversion | NOT ADDRESSED | Not asked |
| 10 | Turnkey liabilities fall | NOT ADDRESSED | Not asked |
| 11 | Inventory release share of Q2 revenue | NOT ADDRESSED | Not asked |
| 12 | Target name; book inclusion | NOT ADDRESSED | Target unnamed |
| 13 | Defence Rs500 Cr dependence on target | PARTIALLY ANSWERED | "all put together 500" (C-L402-407); no split |
| 14 | Target book ~2,000 to ~1,600 | NOT ADDRESSED | MD's own "16 or 1800" (C-L405) |
| 15 | Capex funding split | PARTIALLY ANSWERED | "new debts for CAPEX" (C-L551-552); no split |
| 16 | Export guide >70% vs 65%+ | NOT ADDRESSED | Not asked |
| 17 | Book executing FY27 and FY28 | PARTIALLY ANSWERED | Tenor only (C-L697-702) |
| 18 | >27% margin incl. other income? | NOT ADDRESSED | Not stated |
| 19 | Capacity by Dec-2026? | PARTIALLY ANSWERED | Steps undated (C-L361-362) |
| 20 | Held-for-sale buyer | NOT ADDRESSED | Not asked |
| 21 | Other-equity debit Rs30.6 Cr | NOT ADDRESSED | Not asked |
| 22 | Deferred-tax credit source | NOT ADDRESSED | Not asked |
| 23 | OCI investment | NOT ADDRESSED | Not asked |
| 24 | Intangibles under development | NOT ADDRESSED | Radars "under trial" only (C-L259-262) |
| 25 | R&D payroll expensed or capitalised | NOT ADDRESSED | Not asked |
| 26 | QIP R&D money by 31-Mar-2027 | NOT ADDRESSED | Not asked |
| 27 | QIP money in CC account | NOT ADDRESSED | Not asked |
| 28 | Rs10.30 Cr FD; LC margin | NOT ADDRESSED | Not asked |
| 29 | QIP GCP use | NOT ADDRESSED | Not asked |
| 30 | Rs175 Cr preform money: equity or loan | NOT ADDRESSED | Preform solution withheld (C-L885) |
| 31 | Rs90 Cr extension by circular; Reg 32 | NOT ADDRESSED | Not asked |
| 32 | Other 19-Oct board items | NOT ADDRESSED | Future restructuring board promised (C-L541) |
| 33 | Rs10,000 Cr year; defence forecast or aspiration | PARTIALLY ANSWERED | "much sooner" (C-L484-485); defence "aspiration" (C-L129, C-L252) and "possibly" (C-L770) vs "surely" (C-L408) |
| 34 | Pledge zero? | NOT ADDRESSED | Not asked |
| 35 | Defence further investment | NOT ADDRESSED | Not asked |
| 36 | Para 7 subsidiaries' CFO; receivable from HFCL | NOT ADDRESSED | Not asked |
| 37 | Q2 PCS/DC revenue and book | PARTIALLY ANSWERED | ~Rs300 Cr hedged (C-L796-802) |
| 38 | Secured raw materials: terms | PARTIALLY ANSWERED | Tenors 12-24 months (C-L330-333); suppliers withheld |
| 39 | Q2 OFC realisation; long-term contracts | PARTIALLY ANSWERED | ~$15 vs ~$25-27; +~20%; customer prices reset yearly up or down (C-L336-339); reset clause in most long-term contracts, none in 4-6 month contracts (C-L877-878; M09) |
| 40 | "#1 in OFC": India or global | NOT ADDRESSED | Not asked |
| 41 | BharatNet Q2 revenue; remaining book | NOT ADDRESSED | Qualitative only |
| 42 | H2 advance tax due | NOT ADDRESSED | Not asked |

Totals: ANSWERED SPECIFICALLY 1; PARTIALLY ANSWERED 11; EVADED 1; NOT ADDRESSED 29 (sum 42). Most NOT ADDRESSED items were simply not asked; all go to the IR email with MQ43-MQ61.

---

## (4) ADDITIONS TO MONITORABLES

| # | Item | Implied date | Source |
|---|---|---|---|
| N1 | Army AMC via BSNL signed | ~end-Oct-2026 ("a week or 10 days" from 19-Oct) | C-L418-423 |
| N2 | IR reply to the emailed Q1-Q42 and MQ43-MQ61 list | "immediately" (C-L1013), so from 20-Oct-2026; score the actual date; scored as missed if no reply by the Q3 FY27 review | C-L1011-1014 |
| N3 | Foliage penetration radar second trial and approval | ~early Nov-2026 | C-L262-263, C-L397-399 |
| N4 | Restructuring: recommendation, board meeting, decision; trigger #6 test | ~early to mid Nov-2026 [INFERENCE] | C-L535-545 |
| N5 | Aerospace acquisition completes, with price and target financials filed; revenue consolidated from Q3 | within Nov-2026 | C-L404-406, C-L274-275 (M02) |
| N6 | Official company transcript of the 19-Oct call (re-read audio gaps) | date ND | CC-FN-21 |
| N7 | Tripwire #4 reversal evidence: written ageing and unbilled at 30-Sep-2026 | next IR reply or Q3 deck | Step 8C |
| N8 | BharatNet milestone bills submitted; Q3 Turnkey loss lower | Q3 FY27 | C-L435-439 |
| N9 | Q3 revenue above Q2 (Rs2,541.79 Cr); Q3 realisation per fkm; Q3 gross margin and Telecom result margin against realisation (separates the two margin readings) | Q3 FY27 results, date not filed | C-L608, C-L646-648; Step 4C Exchange 2 |
| N10 | Preform midterm solution begins | Q1 CY2027 (Jan-Mar 2027) | C-L580-583 |
| N11 | In-DC connectivity product revenue starts | Q4 FY27 or early FY28 | C-L366-369 |
| N12 | Connectivity revenue above Rs800 Cr; defence Rs500-600 Cr | 31-Mar-2027 | C-L369-370, C-L251 |
| N13 | Gross borrowings at 31-Mar-2027 below 30-Sep level (Rs1,840.13 Cr [ROLE 4]) | 31-Mar-2027 | C-L551-555 |
| N14 | Turnkey segment profit | Q1 FY28 results, date not filed | C-L443 |
| N15 | Connectivity Rs2,000 Cr; defence at least Rs2,000 Cr | FY28 | C-L371, C-L251-252 |
| N16 | Debt "substantially" lower | 31-Mar-2028 | C-L553-555 |
| N17 | Germanium supply contracted | before Oct-2028 | C-L593-600, C-L969 |
| N18 | Defence ~Rs5,000 Cr (A4 classification: ASPIRATION, not a commitment [INFERENCE]; MD framings: "in expiration", C-L252; "it should not be difficult for us to reach ... a 5000 crores figure", C-L278-279; "possibly", C-L770) | FY29 or FY30 | C-L252-253, C-L278-279, C-L770 |
| N19 | Rs10,000 Cr revenue | year unnamed (implied FY28) | C-L484-486 |
| N20 | Ammunition complex construction; revenue in ~2 years; MMHG tender outcome | soon; ~late 2028; undated | C-L134, C-L282-285 |
| N21 | Preform supply contract expiries and yearly customer price resets (cost and price reset) | undated | C-L330-339 |
| N22 | Full-year FY27 CFO after H2 advance tax: CFO/PAT on both readings against the 0.65 marker (resolves the cash class) | FY27 results, date not filed | Role 4 5A (0.65 and 0.80 band markers) |

---

## (5) VERDICT AFTER ROLE 5

| Item | Role 4 | After Role 5 | Change? | Why |
|---|---|---|---|---|
| Protocol verdict | PROCEED WITH FLAGS | PROCEED WITH FLAGS | NO | The call adds flags, not a mechanical failure. House rule: never halt on company quality; flags propagate |
| Cash conversion class | INDETERMINATE-WITH-DIRECTION | INDETERMINATE-WITH-DIRECTION | NO | The call gave no cash figures. It added unquantified unbilled BharatNet work and a debt-reduction promise that runs against H1. Both Role 4 readings stand: H1 CFO/PAT 0.71 reported, 0.52 with tax counted when charged. Missing evidence unchanged: ageing, unbilled breakup, full-year CFO after advance tax (N22), para 7 subsidiary CFO |
| Thesis-broken triggers | None fired; #4 at risk; #6 proximity | #4 FIRED (silence limb; unbilled limb UNTESTABLE); #6 imminent test | YES | Second consecutive quarter of receivables silence across results, deck and call; Role 4 6C pre-committed this test |
| Decision Status | WATCHLIST, no change proposed | WATCHLIST verified; PROPOSAL: reclassify to AVOID under 8A-W | YES (proposal) | Fired trigger rule; operator decides; nothing written. Supersedes the Role 4 Step 9 "no change" clause (Step 9 note) |
| Management view | n.a. | Provisional credibility 40% (C); specificity 0.40; provisional EVASIVE | NEW | First scored concall |

---

## (6) PLAIN-LANGUAGE BRIEF (UPDATED, full replacement)

Provenance tiers: FILED (Q2 results, press release, deck), AGENCY (CARE Monitoring Agency report), MGMT (management claim; on the call, from a machine transcript), SECONDARY (broker), INFERENCE. Each figure also says [Q2] for this quarter's documents or [Notion] for prior work.

### 1. Summary narrative

HFCL had its biggest quarter on record. Revenue was Rs2,541.79 Cr, up 143.62% on last year (FILED, Q2). Operating margin, without other income, was 24.81% against 18.24% a year ago (FILED, Q2, computed). Profit after tax was Rs394.22 Cr (FILED, Q2).

The new guide is at least 80% growth for FY27 (MGMT, Q2). Two times first-half revenue, Rs8,913.54 Cr, already equals the floor of Rs8,908.69 Cr (FILED, Q2, computed). So the guide lets the second half grow only 46.69% on last year. On the call the MD said the floor is low and Q3 will "definitely" grow (MGMT, Q2, call). He also said Q2 fibre prices rose about 20%, which he did not expect (MGMT, Q2, call). Whether price lifted the margin is not yet proven (INFERENCE). Gross margin slipped from 38.82% to 38.25% between Q1 and Q2 (FILED, Q2). Q3 margins against Q3 price per kilometre will show which reading holds.

Cash is weaker than the headline. In the half year, reported operating cash was Rs455.27 Cr, 71% of profit (FILED, Q2). Rs123.40 Cr of that is tax charged but not yet paid. Counted when charged, cash was 52% of profit (FILED, Q2, computed). Free cash was about zero, or negative on that reading.

The call did not cover receivables. Ageing and unbilled figures were missing in the results, the deck and the call. This is the second silent quarter, so tripwire #4 fires on its own wording (FILED and MGMT, Q2; Notion). Step 8C gives the counter-reading and the reversal test: a written IR reply with the figures. Until then the proposal is AVOID; the operator decides.

Two decisions come within weeks. A board committee with E&Y advice will soon recommend a restructuring, and a decision may follow by mid-November (MGMT, Q2, call; INFERENCE on the date). That tests trigger #6. The aerospace deal should close in November, but no document gives the price or the target's profit, so its value cannot be checked (MGMT and FILED, Q2).

### 2. Sector intelligence

Optical fibre demand comes from AI data centres and telecom networks (MGMT, Q2). The MD sees no slowdown from US rates and expects Europe, Asia and telcos to add demand (MGMT, Q2, call). Telcos bought little for two years because prices rose too much (MGMT, Q2, call). Data-centre fibre sells at about $25-27 against about $15 for telco fibre (MGMT, Q2, call).

Prices are cyclical. Q2 fibre prices rose about 20% (MGMT, Q2, call). Customer long-term contracts reprice once a year, up or down (MGMT, Q2, call). Spot preform, the key input, is up about 600% (MGMT, Q2, call, machine-transcript caveat). An analyst said global makers plan 40-50% more capacity (analyst, Q2 call). If supply catches up, prices can fall (INFERENCE).

Government work is the other leg. BharatNet bills wait on a 25-step verification process (MGMT, Q2, call). That slows cash in the Turnkey business, which lost Rs122.58 Cr in Q2 (FILED, Q2).

Defence is policy-driven. Revenue was Rs78.68 Cr in the half year (FILED, Q2). Targets are Rs500-600 Cr for FY27 and at least Rs2,000 Cr for FY28 (MGMT, Q2, call). The MD framed about Rs5,000 Cr in three ways (MGMT, Q2, call). First he called it an aspiration ("in expiration") over three years. Then he said it "should not be difficult" to reach. Later he said "possibly" within two years. We read it as an aspiration, not a commitment (INFERENCE).

### 3. Business-model intelligence

HFCL makes money mainly from fibre, cable and telecom products: 91.35% of Q2 revenue at a 30.85% segment margin (FILED, Q2, computed). Data centres are 65-75% of that revenue and telcos 25-35% (MGMT, Q2, call).

The model's cost base has a time limit. Preform supply runs on 12-24 month contracts, and prices reset at expiry (MGMT, Q2, call). Most customer long-term contracts carry a reset clause too, but 4-6 month contracts do not (MGMT, Q2, call). HFCL's own preform plant covers about half its needs and only from October 2028 (MGMT, Q2, call). A "midterm solution" starts in early 2027, but the MD would not describe it (MGMT, Q2, call).

Profit is moving below the parent. Group profit is 47.09% above the parent's (FILED, Q2, computed). The four fastest-growing subsidiaries earned Rs186.19 Cr in the half year, while their cash balances fell Rs0.29 Cr; their operating cash flow is not disclosed (FILED, Q2).

Utilisation is quoted "in money terms", so higher prices can show 100% while some lines sit idle (MGMT, Q2, call). Capacity steps to 43 and 63 million fibre kilometres have no dates on the call (MGMT, Q2, call).

### 4. Competition intelligence

HFCL claims to be number one in Indian optical fibre cable (MGMT, Q2, deck). The MD declined to compare margins with peers (MGMT, Q2, call). An analyst put HFCL's telecom margin at 32-33%, an Indian peer at about 20% and a global peer at about 30% (analyst, Q2 call; unverified).

The direct listed peer on file is Sterlite Technologies (STLTECH), which the operator holds (Notion). Peer concalls for this quarter are not in the inputs.

Strengths: hyperscaler relationships, DC-grade fibre and a path to own preform. The MD put hyperscalers at about 70% of the export orders in the Rs18,500 Cr fibre and connectivity book (MGMT, Q2, call). On that base, hyperscalers are at most 39.90% of the total book, and may be less (computed). Only if the 70% applies to the whole Rs18,500 Cr do they reach 44.81% (computed). Weaknesses: the loss-making EPC arm, long receivables, a defence plan that leans on an unpriced target, and a margin exposed to a price cycle.

Risk to watch: global capacity additions and preform contract resets can squeeze the spread between fibre price and input cost (INFERENCE).

### 5. Forward map (next about 10-11 months)

Make-or-break next reading: Q3 FY27 consolidated Telecom Products revenue. Bull at or above Rs2,321.98 Cr; bear below Rs2,006.15 Cr (FILED, Q2, computed). Results date not filed; about January-February 2027 on past cadence (INFERENCE).

- End-October 2026, Army AMC signing. Bull: signed, and the AMC cost turns into revenue. Bear: not signed, and Turnkey keeps bearing the cost.
- From 20-Oct-2026, IR reply to the emailed questions ("immediately", scored by the Q3 FY27 review at the latest). Bull: ageing and unbilled figures arrive and tripwire #4 can be reversed. Bear: no figures, and the AVOID proposal stands.
- Early to mid November 2026, restructuring decision. Bull: an EPC carve-out with the same shareholders. Bear: OFC or defence value moves to a vehicle where listed holders own less, and trigger #6 fires.
- November 2026, aerospace close. Bull: the target, price and profit are filed and the multiple can be checked. Bear: a close with no price, or another delay.
- 31-Dec-2026, HASPL Rs90 Cr and Nivetti deadlines; Dec-2026 capacity step. Bull: money deployed and capacity reached. Bear: a second HASPL extension, a third Nivetti extension, or the step folds into July 2028.
- Q3 FY27 results (about January-February 2027). Bull: revenue above Rs2,541.79 Cr, with gross margin holding near 38.25% as realisation moves. Bear: revenue falls toward the Rs2,225.96 Cr guide pace and margins fall with price.
- Q1 CY2027, preform midterm solution. Bull: disclosed, arm's-length, lower cost. Bear: undisclosed terms or a related party.
- 31-Mar-2027, FY27 close. Bull: revenue at or above Rs8,908.69 Cr, defence near Rs500 Cr, connectivity above Rs800 Cr, gross debt below Rs1,840.13 Cr. Bear: defence short, debt higher after Rs123.40 Cr of tax and capex payments.
- FY27 results, full-year cash flow (date not filed). Bull: CFO/PAT at or above the 0.65 marker on both readings after H2 advance tax, so the cash class can resolve. Bear: below 0.65 on the tax-counted reading, so the cash class stays INDETERMINATE.
- Q1 FY28 results (about July-August 2027), Turnkey profit. Bull: segment profit as promised. Bear: another quarter of loss.

---

## (7) CLOSING YAML

```yaml
stage: A4-analyst
substage: role5-addendum
loop: 2
company: "HFCL"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
docs_merged: [concall]
source_caveat: "machine transcript (faster-whisper); speakers inferred; filed results win on any number conflict"
ledger_reconciliation:
  notes: 0
  turns: 145
  slides: 0
  structured_ids: 615
  missing_from_structured_rows: 14
  missing_from_structured_ids: [M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11, M12, M13, M14]
  ledger_rows_total: 629
  question_rows: 54
  all_reviewed: true
  a3_findings_incorporated: [CC-FN-01, CC-FN-02, CC-FN-03, CC-FN-04, CC-FN-05, CC-FN-06, CC-FN-07, CC-FN-08, CC-FN-09, CC-FN-10, CC-FN-11, CC-FN-12, CC-FN-13, CC-FN-14, CC-FN-15, CC-FN-16, CC-FN-17, CC-FN-18, CC-FN-19, CC-FN-20, CC-FN-21, CC-FN-22, CC-FN-23, CC-FN-24, CC-FN-25]
  pipeline_note: "A3 forensics file still records MISSING_FROM_STRUCTURED 0 (line 17); no A3 reading of M01-M14 on file. A4 read each at its fulltext line; no finding, count, grade or ruling changes"
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "WATCHLIST (DO NOT INITIATE); not held"
position_branch: "8A-W"
proposed_decision_status: "AVOID (proposal under 8A-W after tripwire #4 fired; operator decides; not written; supersedes Role 4 Step 9 'no change / No trigger fired' for the save)"
tripwire_4_ruling: "FIRED on the silence limb (two consecutive quarters: Q1 per memory, Q2 results/deck/call); most evidenced reading on the trigger wording and the Role 4 6C pre-commitment. Unbilled limb UNTESTABLE (no number). Counter-reading corrected: 140.78 receivable days sit above the 130-day red line (Role 4 item 2 AMBER, BUY gate (b) NOT MET); only TR/TTM 38.57% is green. Reversal: written ageing and unbilled at 30-Sep-2026 with >6m ageing <=25% and the +317.31 other-current-assets rise explained"
trigger_6_ruling: "NOT FIRED; imminent test ~early to mid Nov-2026 (committee recommendation, board ~10 days after, finalisation within ~2 weeks; scope unstated)"
role5_step_8D: "deferred to /fttcp and Role 1 (OR-30)"
specificity: {quantified: 45, unquantified: 67, total_forward_rows: 112, ratio: 0.40, ratio_excl_market_size_rows: 0.39, with_M_forward_rows: "46/115 = 0.40", borderline_range: "0.38-0.43; band unchanged"}
credibility: {formal_trailing4: "ND (prior log not passed)", provisional_ratio_pct: 40.0, provisional_points: 4.0, provisional_scored: 10, provisional_grade: "C (Mixed)", point_schedule: "D 1.0, P 0.5, M 0, Dl 0, Dr 0 + flag, U excluded", delayed_at_half_pct: 50.0, dropped_confirmed: 1, dropped_candidates: 2}
archetype: "provisional EVASIVE (specificity 0.40, provisional credibility 40%), with OVERPROMISER traits on forward targets; shift from provisional OVERPROMISER-watch flagged"
defensive_phrases: 12
qa_grades: {A: 5, B: 31, C: 13, D: 2, E: 2, unanswered: 1}
hyperscaler_share_of_book: "39.90% (lower reading, cap: 70% of export orders x 57% export share of book) to 44.81% (upper reading: 70% of the full Rs18,500 Cr); base 'the export orders' (C-L171-173); not firm"
defence_5000: "aspiration, not a commitment (A4 classification, INFERENCE from C-L252, C-L713, C-L770); MD framings: C-L252-253 'in expiration'; C-L278-279 'it should not be difficult for us to reach the 2000 crores figure and a 5000 crores figure'; C-L770 'possibly'; horizon FY29 or FY30"
sc_gap_pat_pct: ["Q2FY26: 17.06", "Q1FY27: 37.07", "Q2FY27: 47.09", "H1FY26: 123.14", "H1FY27: 43.07", "FY26: 30.28"]
questions_for_management:
  - {q: "MQ43 Restructuring scope (EPC only or OFC/defence/aerospace); every entity mirrors listed HFCL holding? Y/N", from_finding_id: "CC-FN-06"}
  - {q: "MQ44 Is >=80% FY27 on consolidated FY26 Rs4,949.27 Cr?", from_finding_id: "CC-FN-02"}
  - {q: "MQ45 Fiscal year revenue first exceeds Rs10,000 Cr?", from_finding_id: "CC-FN-03"}
  - {q: "MQ46 Defence ~Rs5,000 Cr: target or aspiration; FY29 or FY30; FY27 split own vs acquired?", from_finding_id: "CC-FN-04"}
  - {q: "MQ47 Target book Rs1,600 or Rs1,800 Cr; executed or unexecuted?", from_finding_id: "CC-FN-05"}
  - {q: "MQ48 Unbilled BharatNet work at 30-Sep (Rs Cr) and its balance-sheet line; two-quarter Turnkey loss ceiling?", from_finding_id: "CC-FN-07, CC-FN-22"}
  - {q: "MQ49 Does Rs5,000 Cr O&M book include unsigned Army AMC via BSNL; signed yet?", from_finding_id: "CC-FN-08"}
  - {q: "MQ50 Gross borrowings expected at 31-Mar-2027, Rs Cr?", from_finding_id: "CC-FN-09"}
  - {q: "MQ51 Preform contract expiries; fixed-price share of FY28 need; customer contracts repricing in H2 FY27; short-term (no reset) share of book?", from_finding_id: "CC-FN-10"}
  - {q: "MQ52 Preform midterm solution: nature, related party?, capital committed?", from_finding_id: "CC-FN-11"}
  - {q: "MQ53 Connectivity revenue Q1 and Q2 FY27 Rs Cr; Rs215 Cr DC facility still planned?", from_finding_id: "CC-FN-01, CC-FN-12"}
  - {q: "MQ54 Current cable capacity 34 or 39 mn fkm; date fibre reaches 34?", from_finding_id: "CC-FN-13"}
  - {q: "MQ55 Q2 physical fkm output vs installed capacity?", from_finding_id: "CC-FN-14"}
  - {q: "MQ56 CFO to provide H1 export-OFC revenue, Q2 connectivity revenue, price/volume split in writing?", from_finding_id: "CC-FN-15, CC-FN-23"}
  - {q: "MQ57 Is ~70% hyperscaler share on export orders or full Rs18,500 Cr book; single $1.1B order share; number of hyperscaler customers?", from_finding_id: "CC-FN-16"}
  - {q: "MQ58 Price share of Q2 QoQ growth (pp); Q3 realisation per fkm vs Q2?", from_finding_id: "CC-FN-17"}
  - {q: "MQ59 Germanium contract date and source countries?", from_finding_id: "CC-FN-18"}
  - {q: "MQ60 Reply date for emailed questions; official transcript to be filed?", from_finding_id: "CC-FN-25, CC-FN-21"}
  - {q: "MQ61 Fuze approval status and date?", from_finding_id: "CC-FN-24"}
q1_q42_status: {answered: 1, partial: 11, evaded: 1, not_addressed: 29}
q1fy27_15_status: {answered: 2, partial: 9, evaded: 0, not_addressed: 4}
monitorables:
  - {item: "Army AMC via BSNL signed", implied_date: "~end-Oct-2026", source_ref: "C-L418-423"}
  - {item: "IR reply to emailed Q1-Q42 and MQ43-MQ61", implied_date: "from 2026-10-20 ('immediately'); missed if none by the Q3 FY27 review", source_ref: "C-L1011-1014"}
  - {item: "Foliage radar second trial / approval", implied_date: "~early Nov-2026", source_ref: "C-L262-263, C-L397-399"}
  - {item: "Restructuring recommendation, board meeting, decision; trigger #6 test", implied_date: "~early to mid Nov-2026 (INFERENCE)", source_ref: "C-L535-545"}
  - {item: "Aerospace close with price and target financials; consolidation from Q3", implied_date: "Nov-2026", source_ref: "C-L404-406, C-L274-275 (M02)"}
  - {item: "Official company transcript of 19-Oct call", implied_date: "ND", source_ref: "CC-FN-21"}
  - {item: "Tripwire #4 reversal evidence: written ageing and unbilled at 30-Sep-2026", implied_date: "next IR reply or Q3 deck", source_ref: "Step 8C"}
  - {item: "BharatNet bills submitted; Q3 Turnkey loss lower", implied_date: "Q3 FY27", source_ref: "C-L435-439"}
  - {item: "Q3 revenue above Q2 Rs2,541.79 Cr; Q3 realisation per fkm; Q3 gross and Telecom result margin vs realisation (margin readings A/B)", implied_date: "Q3 FY27 results, date not filed", source_ref: "C-L608, C-L646-648; Step 4C Exchange 2"}
  - {item: "Preform midterm solution begins", implied_date: "Q1 CY2027", source_ref: "C-L580-583"}
  - {item: "In-DC connectivity product revenue starts", implied_date: "Q4 FY27 or early FY28", source_ref: "C-L366-369"}
  - {item: "Connectivity > Rs800 Cr; defence Rs500-600 Cr", implied_date: "2027-03-31", source_ref: "C-L369-370, C-L251"}
  - {item: "Gross borrowings below Rs1,840.13 Cr", implied_date: "2027-03-31", source_ref: "C-L551-555"}
  - {item: "Full-year FY27 CFO/PAT on both readings vs 0.65 marker (cash class re-test)", implied_date: "FY27 results, date not filed", source_ref: "Role 4 5A"}
  - {item: "Turnkey segment profit", implied_date: "Q1 FY28 results, date not filed", source_ref: "C-L443"}
  - {item: "Connectivity Rs2,000 Cr; defence >= Rs2,000 Cr", implied_date: "FY28", source_ref: "C-L371, C-L251-252"}
  - {item: "Debt substantially lower", implied_date: "2028-03-31", source_ref: "C-L553-555"}
  - {item: "Germanium supply contracted", implied_date: "before Oct-2028", source_ref: "C-L593-600, C-L969"}
  - {item: "Defence ~Rs5,000 Cr (A4 classification: aspiration, not a commitment; MD also said 'should not be difficult', C-L278-279)", implied_date: "FY29 or FY30", source_ref: "C-L252-253, C-L278-279, C-L770"}
  - {item: "Rs10,000 Cr revenue", implied_date: "year unnamed (implied FY28)", source_ref: "C-L484-486"}
  - {item: "Ammunition complex construction; revenue ~2 years; MMHG tender outcome", implied_date: "soon; ~late 2028; undated", source_ref: "C-L134, C-L282-285"}
  - {item: "Preform supply contract expiries and yearly customer price resets", implied_date: "undated", source_ref: "C-L330-339"}
flags:
  - "Tripwire #4 FIRED (silence limb): receivables ageing/DSO/unbilled absent in Q1 (memory) and in Q2 results, deck and call; Role 4 6C pre-committed the test; counter-reading weaker than first stated (140.78 days above the 130-day red line); proposal AVOID under 8A-W; operator decides; reversal conditions stated"
  - "Trigger #6 imminent: E&Y-advised restructuring committee near recommendation; board ~10 days after; decision ~mid-Nov; scope unstated"
  - "Aerospace close 'within November'; target, price and profit NOT FOUND; book stated 1,600 / 1,800 / '16 or 1800'; no accretion credited"
  - "Q2 fibre price +~20% the MD did not foresee; price/volume split refused; two margin readings: price widened the spread, or passed through at a near-constant spread (gross margin 38.82% to 38.25% QoQ; Telecom result margin 30.44% to 30.85%); Q3 margins vs realisation separate them"
  - "Customer long-term contracts reset yearly in both directions; no price floor; no new capacity before July 2028 (fibre at 100%); preform contracts reset at expiry; own preform covers half from Oct-2028"
  - "Hyperscaler share of book: up to 39.90% if the 70% applies only to export orders, as the MD said (C-L171-173; a ceiling, the share may be lower); 44.81% only if it applies to the whole Rs18,500 Cr"
  - "Defence Rs5,000 Cr read by A4 as an aspiration, not a commitment (INFERENCE); MD framings: 'in expiration' (C-L252), 'it should not be difficult for us to reach ... a 5000 crores figure' (C-L278-279), 'possibly' (C-L770)"
  - "Guide floor 80% sits below MD's own 'definitely growth in Q3' path; basis still unstated"
  - "Targets raised inside one call and vs broker figures two weeks earlier (defence, connectivity); narrative-amplification counter candidate (operator)"
  - "Specificity 0.40 (range 0.38-0.43); 12 defensive phrases on delivered-period data; provisional credibility 40% (C); provisional archetype EVASIVE with overpromiser traits"
  - "Narrative vs filing contradictions: debt direction in H1, current cable capacity 34 vs 39; prior order book 26,000 is a hedged rounding (not counted)"
  - "Cash class unchanged INDETERMINATE-WITH-DIRECTION; both Role 4 readings stand (H1 CFO/PAT 0.71 reported, 0.52 tax-accrual); FY27 full-year CFO re-test is the resolver"
  - "Machine transcript with audio gaps at three load-bearing points; request official transcript"
  - "A3 forensics file does not yet record M01-M14 (A4 read them at line)"
  - "Role 5 Step 8D deferred to /fttcp and Role 1 (OR-30)"
plain_language_brief_included: true
analyst_note: "Loop 2 changes text only; rulings and verdict fields stand. Tripwire #4 FIRED on the silence limb is the most evidenced reading. Role 4 pre-committed that a call silent on ageing and unbilled fires it, and the call gave neither. The corrected counter-reading is weaker: 140.78 receivable days sit above the 130-day red line, and only TR/TTM is green. AVOID stays a proposal under 8A-W; the operator decides. Trigger #6 is a live test in early to mid November. Three positive claims are bounded. The H2 bull case rests on mix, connectivity and some cable headroom, not on a price floor or new capacity. The MD tied the 70% hyperscaler share to the export orders, so hyperscalers are at most 39.90% of the book on that base, and may be less; 44.81% assumes the whole book. I read the Rs5,000 Cr defence figure as an aspiration, though the MD also said it 'should not be difficult' to reach. The bear claim that price drives margin carries its filed counter: gross margin fell QoQ while prices rose about 20%. Q3 margins against realisation per fkm separate the readings. Machine transcript; filings govern."
review_path: "runs/hfcl-q2fy27/work/parts/review_hfcl_q2fy27_role5.loop2.part1.md + runs/hfcl-q2fy27/work/parts/review_hfcl_q2fy27_role5.loop2.part2.md + runs/hfcl-q2fy27/work/parts/review_hfcl_q2fy27_role5.loop2.part3.md, joined in that order into runs/hfcl-q2fy27/work/review_hfcl_q2fy27_role5.md"
```

---

## ROLE 5 LOOP 1 CHANGE LOG

Audit: runs/hfcl-q2fy27/work/audit_hfcl_q2fy27_role5.md (verdict INCOMPLETE; loop to A2, then A3 and A4). Rulings unchanged: tripwire #4 FIRED (silence limb) with the AVOID proposal; trigger #6 NOT FIRED with an imminent test. Protocol verdict and cash class unchanged.

| ID | Type | Fix | Where |
|---|---|---|---|
| F1 | FACTUAL | Exchange 2 bull reading restated. It now rests on DC mix (~$25-27 vs ~$15, C-L617-618, C-L629-631), H2 connectivity of at least about Rs500 Cr [INFERENCE from C-L369-370, C-L796-820], cable headroom (C-L506, C-L735-736) and the current upward reset direction (C-L339). It states there is no price floor (yearly resets in both directions, C-L336-339, C-L877-878) and no new capacity in H2 FY27 (fibre at 100%, C-L308, C-L502; capacity OF 28 / OFC 39, P-L434; no step dated before July 2028, P-L428-434). The "Not said: when long-term contracts reset" line is replaced (year to year was said) | 4C Exchange 2; 4A Q08, Q48; Step 2 margins; 8A; brief parts 2, 3 |
| C1 | CONTRADICTION | Tripwire #4 Reading B corrected: 140.78 days sit above the 130-day red line; current-only 128.14 sits between green and red; only TR/TTM 38.57% is green; Role 4 item 2 AMBER and BUY gate (b) NOT MET cited. Weight line added. FIRED ruling stands and gains strength. Label changed from "conservative reading" to "most evidenced reading", with the Role 4 6C pre-commitment quoted | 8C; (5); YAML tripwire_4_ruling, flags |
| M1 | MISSING | M01-M14 listed in the preamble with line, speaker, content and use; ledger rows 629; each cited where used (4A Q05, Q11, Q33, Q36, Q38, Q45, Q46, Q48, Q54; 4C Exchanges 2, 3; 6B sensitivity; 9A #6, #18, #33; N5; brief part 2). Pipeline note: the A3 forensics file does not yet record M01-M14 | Preamble; listed sections; YAML ledger_reconciliation |
| M2 | MISSING | Hyperscaler 70% tied to "the export orders" (C-L171-173). Two readings: upper 44.81% of the book (70% of the full Rs18,500 Cr); lower capped at 39.90% (0.70 x 57% export share of book, P-L314 [ROLE 4]). 44.81% marked the upper reading | 3E #1; 4A Q01; 5A; 8A; 8D; 9B; MQ57; brief part 4; YAML |
| M3 | MISSING | Defence Rs5,000 Cr restated as an aspiration ("in expiration", C-L252-253; "possibly", C-L770; analyst "your aspirations", C-L713), not a commitment | 0D; Step 2; T018 row; Q38; 5A; 6A; 6D; 7C; 8A; 8D; 9A #22; 9B; MQ46; 3B Q33; N18; brief part 2; YAML |
| M4 | MISSING | "Part of the margin is price" now carries its filed counter and two readings: gross margin 38.82% to 38.25% QoQ while prices rose ~20%; Telecom result margin 30.44% to 30.85%; MD raw-material framing and equilibrium (C-L869-879). Separating observation: Q3 gross and Telecom result margins against Q3 realisation per fkm. Brief sentence tagged INFERENCE and replaced with the two-reading lines | 4C Exchange 2; 5A; 7A; 8A; 8D Pillar 1; 9B; N9; brief part 1; YAML flags |
| S1 | STYLE | Borderline rows R313, R271, R320, R302 disclosed (0.40-0.43); M-row sensitivity 46/115 = 0.40; soft repeats ~0.38; "company-only" relabelled "excluding only the three market-size rows" | 6B; 6E; YAML |
| S2 | STYLE | Credibility point schedule stated; DELAYED at 0.5 gives 50.0% / 55.6%; grade unchanged | 3 intro; 3B; 9B; YAML |
| S3 | STYLE | Management questions renamed MQ43-MQ61; Role 4 questions stay Q1-Q42; A2 rows stay Q01-Q54 | Anchor table; 4C; 3A; coverage line; 8F; N2; YAML |
| S4 | STYLE | Brief CFO line now says "in the half year" | Brief part 1 |
| S5 | STYLE | IR reply dated (from 20-Oct-2026, scored by the Q3 FY27 review); HASPL "second" and Nivetti "third" extension; FY27 full-year CFO re-test restored to the forward map and added as N22 | Brief part 5; N2; N22; YAML |
| S6 | STYLE | Brief tripwire paragraph points to the Step 8C counter-reading and the IR reversal test | Brief part 1 |
| S7 | STYLE | "26,000" relabelled ROUNDED (hedged recollection); removed from the contradiction list | 7A; 8E; Step 2; YAML flags |
| S8 | STYLE | Supersession line for the Role 4 Step 9 "no change / No trigger fired" clauses | Step 9 note; (5); YAML |
| S9 | STYLE | Exchange 1 timing: decision at the board meeting; "another couple of weeks" may be the total or an addition; window covers both | 4C Exchange 1; 4A Q20; Step 2; 5A |
| S10 | STYLE | Unbilled limb labelled UNTESTABLE | 8C; (5); YAML |
| S11 | STYLE | Q24 now records the "two three months" machine-supply delay absorbed in the October 2028 date (C-L584-588) | 4A Q24 |
| S12 | STYLE | Caveat notes analyst speech inside MD turns T093 (C-L723-727) and T110 (C-L798-799); R119-R122 read as analyst figures | Source caveat |
| S13 | STYLE | Brief run-rate sentence reworded: two times H1 (Rs8,913.54 Cr) equals the floor (Rs8,908.69 Cr) | Brief part 1 |
| Other | ANCHOR | 6C phrase #8 and 7B peer-comparison decline now cite C-L690 (the same words also appear at C-L667) | 6C; 7B |

Files: Part 1 rewritten in place; Part 2 and Part 3 are new part files under runs/hfcl-q2fy27/work/parts/ (loop1). The earlier part file runs/hfcl-q2fy27/work/parts/review_hfcl_q2fy27_role5.part2.md is superseded. Block updated: runs/hfcl-q2fy27/work/blocks/a4-role5.yaml.

---

## ROLE 5 LOOP 2 CHANGE LOG

Role 5 loop 2 change log: audit runs/hfcl-q2fy27/work/audit_hfcl_q2fy27_role5_loop1.md (verdict INCOMPLETE; loop to A4 only). Two text-only fixes, NF1 and NM1, both checked against runs/hfcl-q2fy27/extracted/hfcl-concall-q2fy27-fulltext.md at C-L170-173 and C-L251-253, C-L276-279, C-L768-770. No number, ruling or verdict field changed: tripwire #4 FIRED (silence limb) with the AVOID proposal; trigger #6 NOT FIRED with an imminent test; PROCEED WITH FLAGS; INDETERMINATE-WITH-DIRECTION. Style notes NS1-NS6 are logged by A5 only and are not applied in this loop.

| ID | Type | Fix | Where |
|---|---|---|---|
| NF1 | FACTUAL | 39.90% now reads as the CEILING of the export-orders reading: hyperscalers are up to 39.90% of the total book if the 70% applies only to export orders (C-L171-173; export share 57% of book, P-L314 [ROLE 4]), and the share may be lower. 44.81% is kept only as the reading that assumes 70% of the whole Rs18,500 Cr. The "39.90%-44.81%" range wording is removed. 5A, 8D and YAML hyperscaler_share_of_book were already right and are unchanged | 8A trigger 1; 9B net impact; 9B Key Notes line; brief part 4; YAML flag; YAML analyst_note |
| NM1 | MISSING | The MD's confidence line on the same figure, "So overall it should not be difficult for us to reach the 2000 crores figure and a 5000 crores figure" (C-L278-279), now sits beside "in expiration" (C-L252-253) and "possibly" (C-L770). The aspiration reading is labelled as A4's classification [INFERENCE]. Brief part 2 no longer says the MD called it "not a target" (he did not); it gives his three framings and labels the aspiration reading INFERENCE | 9A #22; 6D; Step 2 defence row; 5A defence row; N18; brief part 2; YAML defence_5000, flag, monitorable, analyst_note |
| Other | BOOKKEEPING | Header revision line and part-file join list updated to loop 2; YAML loop 1 to 2; YAML review_path names the loop 2 part files | Header; YAML |

Files: three loop 2 part files under runs/hfcl-q2fy27/work/parts/ (review_hfcl_q2fy27_role5.loop2.part1.md, .loop2.part2.md, .loop2.part3.md), joined in that order into runs/hfcl-q2fy27/work/review_hfcl_q2fy27_role5.md. The loop 1 part files are superseded. Block updated: runs/hfcl-q2fy27/work/blocks/a4-role5.yaml.
