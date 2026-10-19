# A4 DOCUMENT REVIEW: QPOWER (Quality Power Electrical Equipments Limited), run cycle Q2 FY27

Agent: A4 analyst | model: claude-opus-5-5 | first pass: 2026-10-19 | LOOP ITERATION 1: 2026-10-20 (A5 audit runs/qpower-q2fy27/work/audit_qpower_q2fy27.md) | LOOP ITERATION 2: 2026-10-20 (A5 re-audit runs/qpower-q2fy27/work/audit_qpower_q2fy27_loop1.md); change logs at the end
Protocol loaded: frameworks/Document_Review_Protocol_v1_1.md (alone). Not loaded: Master, Role 4, Role 5, FTTCP, Section 1B, RDE manual.
Documents reviewed (two standalone one-off Reg 30 disclosures, merged):
- EGM: Outcome and proceedings of the Extra Ordinary General Meeting, 19-Oct-2026 (4 pages). Anchors "EGM Lnnn" = line in runs/qpower-q2fy27/extracted/qpower-egm-q2fy27-fulltext.md.
- TRK: Intimation of commencement of manufacturing at the Endoks PCS facility, Nigde, Turkiye, letter 17-Oct-2026 (1 page). Anchors "TRK Lnn" = line in runs/qpower-q2fy27/extracted/qpower-turkiye-q2fy27-fulltext.md.
A3 finding IDs are prefixed by document to remove the FN01 / FN-01 collision: EGM-FN01..FN15, TRK-FN-01..FN-05.
Inputs read: both A1 structured files, both A1 fulltexts (all lines), both A2 ledgers (TRK ledger as updated in loop 1 with M01, M02), both A3 forensics files (TRK file as updated in loop 1 with FN-05), runs/qpower-q2fy27/work/notion-brief.md, both A5 audits. Source PDFs and inputs/ not opened.

---

## FRAMING (set first)

THESIS CHECK. A live Notion thesis exists (notion-brief.md, page last edited 2026-09-30, fetched 2026-10-19).
- Decision Status verified: WATCHLIST (not held). Position Size "None". Avg cost ND.
- Entry Price Max Rs570; MoS Rs456; CMP on page Rs1,513.4 (24-Sep-2026, SECONDARY, not refreshed).
- Position branch: 8A-W (watchlist / non-held). No HOLD / ADD / TRIM / EXIT framing applies.
- Mental Model signed: ND (not on page). Notion has no Q1 FY27 reconciliation (its own sequencing flag, 07-Sep).
- Memory rule: Notion content is memory to weigh. Where it conflicts with filed text, the filed text wins.

QUARTER-TAG FLAG (A4). Both events fall in Q3 FY27 (October to December 2026), not Q2 FY27:
- TRK: manufacturing commenced 16-Oct-2026 (TRK L36). A3 TRK-FN-04 already flags A1 R028.
- EGM: e-voting 16-Oct to 18-Oct-2026 (EGM L122-123); meeting 19-Oct-2026 (EGM L29, L53-55). A1 R065 is a task label, not document text (A2 ledger anchor table). A3 did not flag the EGM tag; A4 extends TRK-FN-04 to it.
- Effect: "Q2 FY27" is the run-cycle label only. Promise-vs-delivery and tracker entries from both documents log against Q3 FY27. Nothing in either document can sit in Q2 FY27 reported numbers; at most a subsequent-event note.

---

## STEP 1. LEDGER RECONCILIATION PREAMBLE

Ledger contains 103 disclosure units (claims): 96 structured IDs plus 7 MISSING_FROM_STRUCTURED rows.
- EGM: 68 structured IDs R001-R068 (NUMBER 24, ENTITY 24, FORWARD 5, DATE 12, QUALIFIER 3) plus M1-M5 = 73 units; also 3 agenda items and 2 A1 foot notes.
- TRK: 28 structured IDs R001-R028 (NUMBER 7, ENTITY 12, FORWARD 2, DATE 7, QUALIFIER 0) plus M01-M02 (added by A2 in loop 1: M01 = TRK L41-43, M02 = TRK L45 first clause) = 30 units, on 1 slide (S1).
- Notes (to accounts) 0 / turns 0 / slides 1 (TRK S1; the EGM ledger carries no slides).

All 103 reviewed, plus the 3 agenda items and 2 foot notes. Both A2 count tests: match yes, gate_a2 pass, orphan_ids none (TRK ledger missing_from_structured 2, match yes). Both A3 files: 100% reconciled (EGM 68 IDs plus M1-M5; TRK 30 of 30 units), gate_a3 pass.

A3 findings incorporated: EGM-FN01, EGM-FN02, EGM-FN03, EGM-FN04, EGM-FN05, EGM-FN06, EGM-FN07, EGM-FN08, EGM-FN09, EGM-FN10, EGM-FN11, EGM-FN12, EGM-FN13, EGM-FN14, EGM-FN15, TRK-FN-01, TRK-FN-02, TRK-FN-03 (now citing M02), TRK-FN-04, TRK-FN-05 (new in loop 1, from M01) (20 of 20).

Rows reviewed with no finding (boilerplate; listed by ID per A5 S-3):
- EGM (19): R001, R002, R003, R004, R015, R016, R017, R018, R023, R026, R027, R029, R039, R040, R042, R044, R054, R060, R066.
- TRK (14): R001, R002, R004, R005, R006, R007, R008, R009, R010, R017, R018, R022, R025, R027.
Every other row is cited by ID or line in Steps 2-10.

Anchor corrections carried from A2, A3 and A5 (A4 uses the corrected lines throughout):
| Doc | Row | A1 line | Corrected line | Source of correction |
|---|---|---|---|---|
| EGM | R025 | 25-27 | 20 | A2, confirmed A3 |
| EGM | R045 | 140 | 151-153 | A2, confirmed A3 |
| EGM | R046 | 133 | 113-118 | A2, confirmed A3 |
| EGM | R062 | 117 | 113-118 | A2 |
| EGM | R021 | 135-143 | 136-144 | A2 |
| EGM | R047 | 141-143 | 142-144 | A2 |
| EGM | R028 | 46 | 45-46 | A2 |
| EGM | R065 | 31 | none (task label) | A2, confirmed A3 |
| EGM | R057 | 53 | 54 (heading L52) | A5 S-2 |
| EGM | R026 | 22-24 | 22-26 | A5 S-2 |
| EGM | R031 note | "line 145" | 146 | A5 S-2 |
| TRK | R003 | 24 | 25 | A3 |
| TRK | R011 | 34 | 35 | A3 |
| TRK | R016 | 47 | 46 | A3 |
| TRK | R019 | 21-24 | 22-25 | A3 |
| TRK | R021 | 45-47 | 46-48 (L45 first clause is M02) | A5 S-2, A2 M02 |
| TRK | R026, R028 | 62, 36 | not dates | A2 A1_NONDATE_IN_DATE_TABLE |

No row is unreviewed. Proceeding.

---

## STEP 2. EXTRACTION TABLES

### 2A. Financial statement metrics (standalone AND consolidated)

Neither document carries a financial statement or a results figure. Every cell is ND by document, not by omission. (The EGM carries transaction figures: 700 crore, 175 crore, 9%. They sit in 2B.)

| Metric | Standalone (EGM) | Consolidated (EGM) | Standalone (TRK) | Consolidated (TRK) | S-vs-C gap |
|---|---|---|---|---|---|
| Revenue from operations | ND | ND | ND | ND | ND |
| Operating EBITDA | ND | ND | ND | ND | ND |
| Other income | ND | ND | ND | ND | ND |
| PBT | ND | ND | ND | ND | ND |
| PAT | ND | ND | ND | ND | ND |
| PAT attributable to owners | ND | ND | ND | ND | ND |
| EPS | ND | ND | ND | ND | ND |
| CFO | ND | ND | ND | ND | ND |
| Total borrowings | ND | ND | ND | ND | ND |
| Cash and current investments | ND | ND | ND | ND | ND |
| Net worth | ND | ND | ND | ND | ND |
| Shares outstanding | ND | ND | ND | ND | ND |

Note: "consolidated results of the voting" (EGM L149) refers to voting results, not consolidated financials.

### 2B. EGM headline metrics

| Metric | Value | Anchor | Row |
|---|---|---|---|
| QIP size (enabling) | up to 700 crore | EGM L106 | R011, R050 |
| QIP uses named | 4: acquisition; working capital; Global Design Centre at Sangli; general corporate purposes | EGM L106-108 | R050, R043 |
| QIP rupee split by use | ND | not in document | (A3 EGM-FN02) |
| QIP timing / floor price | ND | not in document | |
| Promoter bridge loan facility | up to 175 crore | EGM L110 | R012, R051 |
| Bridge loan interest rate | 9% per annum | EGM L110 | R013 |
| Bridge loan tenor wording | "for 11 years" | EGM L110 | R014 |
| Bridge loan security | unsecured | EGM L109 | R067 |
| Bridge loan purpose | "to facilitate the acquisition pending receipt of QIP proceeds" | EGM L110-111 | R051, R067 |
| Bridge loan rationale | CFO "explained the terms and rationale" (content not recorded) | EGM L109 | R051 |
| Bridge loan lender (named promoter) | ND | not in document | |
| Bridge loan drawn amount | ND | not in document | |
| Bridge interest at full draw (derived: 175 x 9%) | 15.75 crore per year | arithmetic on EGM L110 figures only | (A3 EGM-FN05) |
| Bridge interest over 11 years at full draw, Reading B (derived: 15.75 x 11, simple) | 173.25 crore | arithmetic on EGM L110 figures only | (A5 S-9) |
| Res 3 counterparty | "the Promoters and the members of the Promoter Group" | EGM L142-144 | R047 |
| Res 3 covers the bridge loan | not stated; mapping is [INFERENCE] (A1 note, A5 S-8) | EGM L142-144 vs L109-111 | |
| Swap shares to WSIL sellers | ND | not in document (Notion memory: 10,17,123) | R048 |
| Swap issue price | ND | not in document (Notion memory: Rs1,460) | |
| WSIL consideration | ND | not in document (Notion memory: up to Rs272.34 Cr) | R053 |
| WSIL stake to be acquired / post-deal status | ND | not in document; EGM L95-96 says "proposed acquisition" only (Notion memory: up to 100%) | R049 |
| WSIL revenue / EBITDA / PAT | ND | not in document | (A3 EGM-FN15) |
| Resolutions transacted | 3 | EGM L136-144 | R021 |
| Resolution types | "Special / Special / Ordinary", column not aligned to items | EGM L136-139 | R021 (A3 EGM-FN10) |
| Voting result (for / against, per resolution) | ND | not in document; due "within 48 hours" | R022, R052 |
| Members attended | 35 | EGM L79 | R008 |
| Quorum count | ND | EGM L90 says "requisite quorum was present" | M1 |
| Meeting start / end | 4.00 p.m. / 04.40 p.m. IST (40 minutes) | EGM L55 | R005, R006 |
| Post-meeting e-voting window | 15 minutes | EGM L56, L154-155 | R007, R024 |
| Remote e-voting window | 16-Oct-2026 09:00 to 18-Oct-2026 17:00 IST | EGM L122-123 | R058, R059 |
| Directors present | 8 ("Following Directors were present", L57) | EGM L57-66 | R009 |
| Board size | ND | not in document | |
| Independent directors among those present | 3 or 4 of the 8 present (table offset, unresolved) | EGM L59-67 | (A3 EGM-FN07) |
| Cover letter signed | 19-Oct-2026 19:34:16 IST | EGM L43-44 | R056 |
| Proceedings (p4) signed | 19-Oct-2026 19:34:56 IST | EGM L166 | R060 |

### 2C. TRK headline metrics

| Metric | Value | Anchor | Row |
|---|---|---|---|
| Facility | new Power Conversion Systems (PCS) manufacturing facility | TRK L34 | R013 |
| Owner | subsidiary Endoks Energy Systems | TRK L35 | R011 |
| Location | Nigde, Turkiye (extracted as "Nide, T?rkiye") | TRK L30, L35 | R012 |
| Commencement date | 16-Oct-2026 ("commenced manufacturing operations") | TRK L35-36 | R023 |
| Production status word | "manufacturing operations"; the word "commercial" does not appear | TRK L29-30, L35-36 | R023 (A3 TRK-FN-01) |
| Filed target date for the start | ND (the only dates are L19 letter, L36 start, L65 signature) | TRK L19, L36, L65 | R022, R023, R024 |
| Products | power electronic converters and inverters | TRK L38 | R014 |
| End uses | utility-scale BESS and other grid-connected applications | TRK L38-39 | R015 |
| Strategic framing | "expansion into power electronics and energy storage technologies, complementing its established portfolio of high-voltage equipment and power quality solutions" | TRK L41-43 | M01 (A3 TRK-FN-05) |
| Capability claim | "strengthens the Group's manufacturing and system integration capabilities" | TRK L45 | M02 (A3 TRK-FN-03) |
| Installed capacity (MW or units) | ND | not in document | |
| Capex spent | ND | not in document (Notion memory: $2M Phase 1) | |
| Ramp path | "progressively ramp up ... in accordance with its operational plans and customer delivery schedules" (undated) | TRK L50-51 | R020 |
| International BESS order book | named, size ND | TRK L46 | R016, R021 |
| Revenue share / segment for the power electronics strand | ND | not in document | (A3 TRK-FN-05) |
| First revenue quarter | ND | not in document | |
| Endoks ownership % | ND | not in document (Notion memory: 51%) | |
| Letter signed | 17-Oct-2026 15:30:33 IST | TRK L65 | R024 |

---

## STEP 3. YoY / QoQ WALKS AND PAT BRIDGE

| Walk | Value | Reason |
|---|---|---|
| YoY revenue / EBITDA / PAT | ND | no periods in either document |
| QoQ revenue / EBITDA / PAT | ND | no periods in either document |
| PAT bridge | ND | no financials in either document |

Non-financial deltas against Notion memory (memory, not evidence; listed for the tracker only):
| Item | Prior state (Notion) | This document | Direction |
|---|---|---|---|
| Endoks PCS Nigde | "Dec 2026 ON TRACK ($2M Phase 1)" (s5) | manufacturing commenced 16-Oct-2026 (TRK L35-36); no filed target date | manufacturing start ahead of a memory target (46 to 76 days before Dec 2026); PROVISIONAL (trial vs commercial unresolved) |
| Capital raise | USD 75M "enabling, not committed" (s8); superseded by Rs700 Cr QIP at Board 23-Sep (s9) | QIP up to 700 crore put to members (EGM L106, L140-141) | moved from board approval to member vote; vote result ND |
| Promoter financing | FY26 Rs70 Cr unsecured Chitra Pandyan loan, taken and repaid, terms undisclosed (s9, 07-Sep) | new facility up to 175 crore, 9%, unsecured (EGM L109-111) | second promoter loan within about a year; first with a stated rate |
| Chitra Pandyan designation | WTD (s9, 30-Sep AGM entry, FILED) | "Joint Managing Director" beside her name in an offset table (EGM L61) | conflict is a table-layout artefact (EGM-FN07); L146 names Bharanidharan Pandyan Joint MD |
| Q&A disclosure | 29-Sep AGM: JMD answered queries, content not disclosed (s9) | 19-Oct EGM: JMD answered queries, content not recorded (EGM L145-147) | second consecutive general meeting with unrecorded Q&A |

---

## STEP 4. STANDALONE-vs-CONSOLIDATED GAP (A3 F2)

| Period | S-vs-C revenue gap | S-vs-C EBITDA gap | S-vs-C PAT gap | Decomposition | Direction |
|---|---|---|---|---|---|
| EGM document | ND | ND | ND | ND | ND |
| TRK document | ND | ND | ND | ND | ND |

A3 F2 is N.A. for both documents. The gap is a first-class metric, so A4 records the structural facts that will move it once financials file:
- The PCS facility sits in a subsidiary, Endoks (TRK L35). PCS output enters consolidated figures only. Notion memory: Endoks is 51%-owned, 51.1% of FY26 consolidated PAT, with 49% NCI leakage [memory]. The facility widens the S-vs-C gap and the owners-vs-total PAT gap [INFERENCE].
- WSIL's post-deal stake and status (subsidiary or not) are ND in the filed text. EGM L95-96 says only "proposed acquisition"; the swap goes to "certain selling shareholders" (EGM L136). Notion memory: SPA for up to 100% [Notion]. IF completion delivers control, WSIL becomes a new consolidated line with goodwill [conditional INFERENCE]. WSIL profit is ND (EGM-FN15).
- The promoter bridge loan funds the acquisition (EGM L110-111). The borrowing entity is not stated: ND.
Flag for downstream: the next Reg 33 filing must show both bases, with the Endoks share of consolidated PAT tested against the Notion falsifier (>55%).

---

## STEP 5. CASH-QUALITY NOTE

Case 5a applies. Neither document carries a cash-flow statement or a balance sheet.
- Cash conversion: INDETERMINATE.
- Missing evidence: Q2 FY27 CFO and PAT (standalone and consolidated), Q2 FY27 balance sheet (borrowings, cash, receivables, inventory, contract assets), bridge loan drawn amount, QIP receipts, present cash balance.
- Verdict cap: PROCEED WITH CAVEATS at most.
- Context only (memory, not anchored): FY26 CFO Rs80.28 Cr, CFO/PAT 43.3%, net cash Rs212.47 Cr at March 2026, FCF minus Rs45.6 Cr (Notion s9, s10). Cash in October 2026 is ND. The thesis-broken line is CFO/PAT below 30% for 4 consecutive quarters. These documents give no reading on it.
- Cash-relevant facts in the documents: a 9% promoter loan facility of up to 175 crore (EGM L110); a QIP of up to 700 crore (EGM L106); a new design centre capex use (EGM L107-108); new PCS manufacturing in Endoks (TRK L35-36). Each moves future cash. None is quantified in rupee flow or timing.

---

## STEP 6. THESIS RECONCILIATION (against Decision Status WATCHLIST)

### 6A. Thesis-broken conditions (Notion s4)

| Condition | Evidence in these documents | Status |
|---|---|---|
| Sangli commercial production delayed beyond March 2027 | None. The EGM names only a "Global Design Centre at Sangli" (EGM L107-108). The Chairman's briefing covers the deal, QIP and financing only (EGM L95-97). | NOT FIRED; NOT TESTED. Silence in 2 consecutive documents (29-Sep AGM per memory; this EGM). |
| Atlanta Electricals or peer 220kV+ HVDC coil qualification | None (out of scope for these documents) | NOT FIRED; NOT TESTED |
| ROCE below 20% for 2 consecutive years | ND | NOT TESTED |
| CFO/PAT below 30% for 4 consecutive quarters | ND | NOT TESTED |
| Promoter background red flags on re-verification | No integrity fact in either document. A promoter RPT (Res 3, EGM L142-144) and an unsecured promoter loan (EGM L109-111) put the item in play. | NOT FIRED; re-verification still pending (Notion property) |

Result: 0 of 5 thesis-broken conditions fired by these documents. No pre-committed trigger fired. Decision Status stays WATCHLIST. A4 flags; the human decides.

### 6B. Growth triggers and trackers touched

| Notion item | Prior status | This document | Updated tracker reading |
|---|---|---|---|
| Endoks PCS Nigde | Dec 2026 ON TRACK ($2M Phase 1) | Manufacturing commenced 16-Oct-2026 (TRK L35-36) | MANUFACTURING START AHEAD OF MEMORY TARGET, PROVISIONAL. Log in Q3 FY27. Provisional until commercial output is confirmed (TRK-FN-01). |
| BESS Europe scaling | FIRED ($30M order book; $60-80M FY27 target) | Order book named, no figure (TRK L46) | No update. Figures neither restated nor revised (TRK-FN-03). |
| PCS standalone line | NEW (1725 kW inverter launch Q1-Q2 FY27) | "converters and inverters ... and other grid-connected applications" (TRK L38-39); described as an "expansion into power electronics and energy storage technologies, complementing its established portfolio" (TRK L41-43, M01) | Scope widened beyond BESS; the company calls it an "expansion into" power electronics (TRK-FN-05). No product rating, segment or revenue share named. |
| Endoks % of consol PAT tracker (falsifier >55%) | 51.1% FY26 | New capacity in Endoks (TRK L35); the plant "strengthens the Group's manufacturing and system integration capabilities" (TRK L45, M02) | Pressure upward [INFERENCE]; no figure. |
| WSIL acquisition | SPA 23-Sep; completion by 31-Mar-27 | Put to members via preferential swap (EGM L136-138); voting result ND; stake ND in filed text | IN PROGRESS. Status gate: Reg 44 voting result. |
| Capital raise | USD 75M superseded by Rs700 Cr QIP | QIP up to 700 crore put to members (EGM L106, L140-141) | IN PROGRESS. Vote result ND. Market access untested. |
| Logged pattern "Capex slips 1-2 quarters" | Sangli | A manufacturing start ahead of a memory target | NOT YET A COUNTER-EXAMPLE. Sangli's slip is measured on commercial production; the filed letter records a manufacturing start and gives no target date (TRK L19, L35-36). |
| Insulator bottleneck (risk 8; lead time 18-24 months) | Open | WSIL acquisition progresses (EGM L95-96) | Possible vertical-integration path for insulators [INFERENCE]; benefit not quantified (EGM L104-105). |

### 6C. Monitoring checklist items touched (Notion s7)

| # | Item | Touched? | Reading |
|---|---|---|---|
| 5 | Sangli commissioning status | NO | Silence. Most material gap (EGM-FN13). |
| 10 | Promoter pledge | NO | Not expected in these documents. Relevant because promoters now lend to the company. |
| 11 | WSIL closure timing | NO date | ND; memory target 31-Mar-27. |
| 12 | WSIL post-DD margins | NO | Second filing silent on WSIL profit (EGM-FN15). |
| 14 | Raise utilisation | PARTIAL | Four categories, no rupee split (EGM L106-108). |
| 15 | ESOP definitive terms | NO | Bears on total dilution (EGM-FN11). |
| 1-4, 6, 7, 9 | Financial and operating metrics | NO | Not expected in these document types. No signal. |
| 8 | Atlanta / peer HVDC qualification | NO | Tracked in peer filings. No signal. |
| 16, 17 | Internal audit; cost auditor rotation | NO | Not expected. No signal. |

### 6D. Position-decision branch 8A-W (watchlist, not held)

- Entry zone Rs456-570 against page CMP Rs1,513.4 (24-Sep, SECONDARY, stale). CMP was not refreshed in this run: ND for 19-Oct.
- No entry action. From the page CMP, the price must fall 62.3% to reach Rs570 (1 - 570/1,513.4) and 69.9% to reach the MoS Rs456 (1 - 456/1,513.4). The Notion property text says "requires -59% from CMP". That figure fits the earlier Rs1,400 CMP (1 - 570/1,400 = 59.3%) [INFERENCE]; it is stale against Rs1,513.4.
- These documents do not move the zone; the zone is a downstream (Role 1) output.
- Alerts on page: QPEL_700 (watch) and QPEL_570 (entry trigger). Unchanged.
- Watchlist actions from this review: (1) read the Reg 44 voting result; (2) read the EGM notice explanatory statement for the bridge tenor and whether Res 3 covers the loan (the mapping is [INFERENCE]); (3) carry the dilution, promoter-financing and acquisition-economics facts to /fttcp.

### 6E. Pillar evidence flags (OR-30: flag only; recompute deferred to /fttcp and Role 1)

| Pillar input (Notion s6) | Fact | Anchor | Direction | Tier |
|---|---|---|---|---|
| Share count / Owners' EPS (feeds Y3 FV) | Two equity channels: preferential swap and QIP up to 700 crore. Share count ND. Memory: about 7% total dilution, FV trim about 7% unless capital earns its keep. | EGM L106, L136-141 | Down on per-share value unless returns on new capital match | FILED (resolutions); memory for the % |
| A ROCE base (23% FY26; dest 26%) | Up to 700 crore of new capital; a new design centre use; WSIL at about 16.0x FY26 sales with PAT NOT FOUND (memory inputs) | EGM L104-108 | Dilutes ROCE near term until deployed capital earns [INFERENCE] | FILED + INFERENCE |
| B Cash multiplier (CFO/PAT 43%) | Up to 15.75 crore per year interest at full bridge draw; QIP cash inflow is financing, not CFO | EGM L110 (derived) | Interest cost lowers PAT and CFO while the bridge is drawn | FILED (derived) |
| D Growth visibility premium (+6x) | Endoks PCS manufacturing started ahead of the memory target; commercial status unconfirmed | TRK L35-36 | Supports the catalyst register, provisional | FILED (event); MGMT (ramp) |
| E Strategic premium (+4x) | No HVDC or US DC fact in either document. The letter describes an "expansion into power electronics and energy storage technologies, complementing its established portfolio of high-voltage equipment and power quality solutions" | TRK L41-43 | No change; watch capital drift from the HVDC core (TRK-FN-05) | MGMT |
| Endoks concentration (DA Scenario B, partly fired) | More group capacity in the 51%-owned hyperinflation-accounted subsidiary | TRK L35, L45 | Raises concentration and NCI leakage risk [INFERENCE] | FILED + memory |
| Promoter Verdict TRUSTWORTHY (re-verification pending) | Unsecured promoter loan up to 175 crore at 9%; RPT resolution with promoters (loan mapping [INFERENCE]); "11 years" tenor sits against "bridge" | EGM L109-111, L142-144 | STRUCTURE item, not INTEGRITY, on this evidence: rate, security and purpose are disclosed and the RPT goes to a member vote; two readings (Step 8, Q3-Q6) | FILED |

---

## STEP 7. FORWARD-TARGET REGISTER (A3 F6 + A1 FORWARD rows)

| # | Commitment / target | Implied date | Source | A1/A2 row | A3 ref | Status word | Tracker quarter |
|---|---|---|---|---|---|---|---|
| F1 | Declare consolidated voting results; display at registered office and on company, BSE, NSE and RTA websites | By about 21-Oct-2026 (48 hours after the 04.40 p.m. IST 19-Oct conclusion; e-voting open 15 minutes more) | EGM L148-153 | R052, R022, R061, M4 | EGM C1, FN01 | initiated | Q3 FY27 |
| F2 | QIP of up to 700 crore for acquisition, working capital, Global Design Centre at Sangli, general corporate purposes | Undated in document | EGM L106-108, L140-141 | R050, R011 | EGM C2, FN02 | initiated | open |
| F3 | Establish Global Design Centre at Sangli | Undated in document | EGM L107-108 | R043 | EGM C3, FN03 | initiated | open |
| F4 | Acquire WSIL, partly by preferential share swap; stake ND in filed text | Undated in document; Notion memory: completion by 31-Mar-2027 | EGM L95-96, L103-105, L136-138 | R049, R041, R048, R053 | EGM C4, FN12 | initiated | Q4 FY27 (memory) |
| F5 | Unsecured promoter bridge loan up to 175 crore, 9% p.a., "for 11 years", pending QIP proceeds | Drawdown before QIP receipt; tenor sits against "bridge" | EGM L109-111 | R051, R012-R014, R067 | EGM C5, FN05, FN06 | initiated | Q3 FY27 balance sheet |
| F6 | Related-party transaction(s) with Promoters / Promoter Group (loan coverage [INFERENCE]) | Undated in document | EGM L142-144 | R047 | EGM C6 | initiated | open |
| F7 | Remote and in-meeting e-voting | 16-Oct to 19-Oct-2026 | EGM L122-126, L154-156 | R058, R059, R024 | EGM C7 | completed | Q3 FY27 |
| F8 | "Expected operational benefits" of the WSIL acquisition (briefed, not quantified) | Undated | EGM L103-105 | R053 | EGM FN15 | initiated | open |
| F9 | Endoks PCS facility, Nigde: start manufacturing | 16-Oct-2026 (no filed target; memory target Dec 2026) | TRK L34-36 | R011, R013, R023 | TRK FN-01 | completed (provisional: trial vs commercial) | Q3 FY27 |
| F10 | Progressive production ramp per operational plans and customer delivery schedules | Undated, unquantified | TRK L50-51 | R020 | TRK FN-02 | initiated | open |
| F11 | Facility supports execution of the international BESS order book | Undated; no order-book figure | TRK L45-48 | M02, R021, R016 | TRK FN-03 | initiated (A3 register says "underway"; the letter says only "supports", filed one day after the start) | open |
| F12 | Group "expansion into power electronics and energy storage technologies" | Undated; no figure | TRK L41-43 | M01 | TRK FN-05 | initiated (positioning statement; A3 adds no register line) | open |

Memory-only dated targets that these documents neither confirm nor revise (carried for the catalyst timeline, not anchored): Sangli commercial production Dec 2026-Jan 2027 (Q4 FY26 concall, s5, s8); HVDC CTC magnet wire Q3 FY27 (s5); FY27 revenue growth 15-20% (s5); BESS FY27 $60-80M (s5).

---

## STEP 8. QUESTIONS FOR MANAGEMENT

Every FORWARD-SIGNAL and AMBIGUOUS finding has at least one question. NEUTRAL-FACT findings (EGM-FN08, EGM-FN09, EGM-FN14, TRK-FN-04) are carried as flags or monitorables, noted at the foot.

| # | Question | From finding | Class | Priority |
|---|---|---|---|---|
| Q1 | Please file the Reg 44 voting result. Give votes for and against on each of Resolutions 1-3, and the non-promoter votes cast on Resolution 3. | EGM-FN01 | AMBIGUOUS | 1 |
| Q2 | Which of Resolutions 1-3 is the ordinary resolution? The type column (L136-139) does not align with the items. | EGM-FN10 | AMBIGUOUS | 2 |
| Q3 | What is the tenor of the promoter facility: a bridge that ends on QIP receipt, or 11 years? Can the company prepay it without penalty when QIP money arrives? Does Resolution 3 cover this loan? | EGM-FN06 | AMBIGUOUS | 1 |
| Q4 | Which promoter lends the up-to-175 crore facility? How much is drawn today? What triggers repayment? | EGM-FN05 | FORWARD-SIGNAL | 1 |
| Q5 | The filing gives timing until QIP receipt as the reason for the loan (L110-111). FY26 net cash was Rs212 Cr at March 2026 [Notion]. What is present cash, and why can it not fund the cash leg of about Rs124 Cr [Notion]? Why is the facility about Rs51 Cr larger than that cash leg? | EGM-FN05 | FORWARD-SIGNAL | 1 |
| Q6 | The Chairman briefed "promoter financing arrangements" (plural, L97). Are there arrangements other than the 175 crore facility? Please list each with amount, rate and tenor. | EGM-FN04 | AMBIGUOUS | 2 |
| Q7 | What "future strategic opportunities" (L97) does the QIP fund beyond WSIL? Is a further acquisition under evaluation? | EGM-FN04 | AMBIGUOUS | 2 |
| Q8 | Please give the rupee split of the up-to-700 crore QIP across the acquisition, working capital, the Global Design Centre and general corporate purposes, and the planned launch window. | EGM-FN02 | FORWARD-SIGNAL | 2 |
| Q9 | What does the Global Design Centre at Sangli cost, and when will it open? Is it separate from the Sangli HVDC plant capex? | EGM-FN03 | FORWARD-SIGNAL | 3 |
| Q10 | How many shares will the swap and the QIP issue, and what is the post-issue share count? What is the ESOP pool size and strike? | EGM-FN11 | FORWARD-SIGNAL | 2 |
| Q11 | What were WSIL's FY26 EBITDA, PAT, net debt and ROCE? Please quantify the "expected operational benefits" (L104-105), including the effect on group insulator lead times. | EGM-FN15 | AMBIGUOUS | 1 |
| Q12 | What stake will the company hold in WSIL at completion, and when will it complete? If WSIL becomes a subsidiary, from which quarter will it consolidate and what goodwill do you expect? | EGM-FN12 | FORWARD-SIGNAL | 3 |
| Q13 | Please publish a summary of the shareholder questions and answers at the 19-Oct EGM (L145-147). | EGM-FN13 | AMBIGUOUS | 3 |
| Q14 | What is the status of the Sangli HVDC plant: did the trial run happen, and what is the date for commercial production? | EGM-FN13 | AMBIGUOUS | 1 |
| Q15 | Please confirm the board: its size, the designations of Bharanidharan Pandyan, Chitra Pandyan and Rajendra Iyer, and the number of independent directors. Did the audit committee approve Resolution 3? | EGM-FN07 | AMBIGUOUS | 2 |
| Q16 | Is the Nigde PCS output commercial production with customer-accepted units, or trial and first-article runs? What was the internal target date for the start? | TRK-FN-01 | FORWARD-SIGNAL | 1 |
| Q17 | What is the Phase 1 capacity (MW or units a year)? How much capex is spent against the $2M Phase 1? In which quarter will PCS revenue first appear? | TRK-FN-02 | AMBIGUOUS | 2 |
| Q18 | What share of PCS output goes to in-group BESS projects, and what share to third-party or non-BESS customers? | TRK-FN-02 | AMBIGUOUS | 3 |
| Q19 | What is the current international BESS order book? What share of it will use in-house PCS? What is the in-house PCS margin against the bought-in cost? How does the plant change the group's system integration capability (L45), and which BESS projects used bought-in PCS or outside integration before? | TRK-FN-03 | AMBIGUOUS | 2 |
| Q20 | How does in-house PCS change Endoks' share of consolidated PAT in FY27 and FY28? | TRK-FN-03 | AMBIGUOUS | 3 |
| Q21 | Will power electronics and energy storage be reported as a separate segment or revenue line from the Q2 or Q3 FY27 filings? | TRK-FN-05 | AMBIGUOUS | 2 |
| Q22 | What share of the up-to-700 crore QIP and of group capex goes to power electronics and energy storage, and what revenue share do you target for this strand by FY28? | TRK-FN-05 | AMBIGUOUS | 2 |

Q5 inputs: Rs212 Cr net cash (March 2026) and Rs123.84 Cr cash leg are Notion memory (AR FY26 and SPA filing as logged); Rs51.16 Cr = 175 minus 123.84, arithmetic on one document figure (EGM L110) and one memory figure.

NEUTRAL-FACT disposition: EGM-FN08 and EGM-FN09 (attendee table offset, name misspellings, "compilation", double hand-off) and EGM-FN14 (35 members, quorum count not stated) feed the drafting-care flag. TRK-FN-04 (event in Q3 FY27) drives the quarter-tag flag above.

---

## STEP 9. MONITORABLES / CATALYST LIST

| # | Item | Implied date | Source ref | Bull reading | Bear reading |
|---|---|---|---|---|---|
| M1 | Reg 44 voting result, Resolutions 1-3 | by about 21-Oct-2026 | EGM L148-149 (F1); EGM-FN01 | All pass with wide non-promoter support on Res 3 | Res 3 passes on thin non-promoter support, or a resolution fails |
| M2 | EGM notice explanatory statement: bridge tenor, lender, prepayment, and whether Res 3 covers the loan ([INFERENCE] mapping) | already filed with the notice; date ND | EGM-FN06 | Bridge ends on QIP receipt; "11 years" a drafting error | 11-year promoter debt at 9%: up to Rs173.25 Cr simple interest at full draw, about equal to the principal |
| M3 | Q2 FY27 results (Jul-Sep 2026): revenue, margin, CFO/PAT, Sangli update, subsequent events | Reg 33 statutory deadline 14-Nov-2026 [INFERENCE, regulation; not in documents] | Notion s7 items 1-5; TRK-FN-04 | Sangli on Dec 2026-Jan 2027 track; CFO/PAT above 30% | Sangli date moves toward or past March 2027 |
| M4 | Bridge drawdown and balance | Q3 FY27 balance sheet (quarter ends 31-Dec-2026) | EGM L109-111 (F5); EGM-FN05 | Small or nil draw, repaid from QIP | Full draw held past QIP receipt |
| M5 | QIP launch and placement document (price, share count, use split) | undated in document | EGM L106-108 (F2); EGM-FN02, FN11 | Use split matches WSIL plus named capex; total dilution below 8% amber | Large general-corporate bucket; dilution plus ESOP crosses 8% within 24 months |
| M6 | WSIL completion, stake, first consolidation, profit disclosure | by 31-Mar-2027 [memory, Notion s5] | EGM L95-96 (F4); EGM-FN12, FN15 | WSIL profit disclosed. To match a 31x yardstick on the Rs272.34 Cr price [Notion] it needs FY26 PAT of Rs8.79 Cr, a 51.5% net margin on Rs17.07 Cr sales [Notion] (INFERENCE, arithmetic); or the parent shows faster insulator supply | Profit still undisclosed at closing; price near 16.0x sales stands; cash-leg carry at 9% (about Rs11.15 Cr a year) exceeds what WSIL earns |
| M7 | Sangli HVDC commercial production | Dec 2026-Jan 2027 guidance [memory]; thesis-broken if after 31-Mar-2027 | Notion s4, s5; EGM-FN13 silence | Commercial billing by Q4 FY27 | Any post-March 2027 reference: thesis broken, flag to human |
| M8 | Nigde PCS: commercial status, capacity, first PCS revenue | Q3 FY27 results; Reg 33 statutory deadline 14-Feb-2027 [INFERENCE, regulation] | TRK L35-36, L50-51 (F9, F10); TRK-FN-01, FN-02 | PCS revenue or units disclosed in Q3 FY27 | No PCS figure; "manufacturing operations" meant trial output |
| M9 | International BESS order book figure | next concall or presentation; date ND | TRK L46 (F11); TRK-FN-03 | Order book restated above $30M [memory] | Figure stays undisclosed |
| M10 | Endoks share of consolidated PAT | FY27 annual results; date ND | Notion s4 tracker; TRK-FN-03 | Stays near 51% or falls as parent and Mehru grow | Rises above 55% falsifier |
| M11 | Global Design Centre at Sangli: cost and date | undated in document | EGM L107-108 (F3); EGM-FN03 | Cost and timeline disclosed, small vs QIP | No cost; bucket used as a QIP filler |
| M12 | Promoter background re-verification | open on Notion; date ND | Notion s4; EGM L109-111, L142-144 | Clean; loan terms arm's length and short | Any red flag on re-verification |
| M13 | Board composition and independent-director count | next AGM notice or company board page; date ND | EGM L57-67; EGM-FN07 | Board size disclosed; at least half independent (the floor under SEBI LODR Reg 17(1)(b) when the Chairman is an executive director, L59) [INFERENCE, regulation] | Fewer than half independent with a promoter RPT live |
| M14 | Segment reporting and capital share for power electronics / energy storage | Q2 or Q3 FY27 filings; date ND | TRK L41-43 (F12, M01); TRK-FN-05 | Separate line with revenue and margin; small share of QIP and capex | No figure; capital drifts from the HVDC core that carries the strategic premium |

Single cleanest next-quarter metric (make-or-break): Sangli HVDC commercial-production status at the Q2 FY27 results (M3, statutory deadline 14-Nov-2026 [INFERENCE]). It is the only thesis-broken condition with a dated test inside the window, and it has gone unmentioned in two consecutive company documents. The first gate before it is the Reg 44 voting result (M1, about 21-Oct-2026).

---

## STEP 10. SILENCE AUDIT

A3 F16: N.A. for the EGM (no prior document of this type passed); FINDING for TRK (order book cited without a figure, TRK-FN-03; power electronics strand framed without a figure, TRK-FN-05). No metric shown in a prior deck can be diffed, so no "dropped metric" signal is available.

| Document | Omission | What a document of this type normally carries | Mark |
|---|---|---|---|
| EGM | Voting results | Proceedings under Reg 30 and the Reg 44 result file separately (within 2 working days) | ROUTINE (gated by M1) |
| EGM | Quorum count | Proceedings usually state "requisite quorum present" only | ROUTINE |
| EGM | Shareholder Q&A content | Indian proceedings often omit it | ROUTINE by type; second consecutive general meeting with unrecorded Q&A (EGM-FN13) |
| EGM | Sangli HVDC plant status in the Chairman's briefing on expansion plans | A briefing on a 700 crore raise "for funding the Company's expansion plans" (L96-97) would name the main plant | SILENCE SIGNAL. Thesis-broken item; 2 consecutive documents silent [memory count] |
| EGM | WSIL stake, profit, net debt and quantified benefits | Briefing named "consideration and expected operational benefits" (L104-105) without figures | SILENCE SIGNAL. Second filing silent on target profit (EGM-FN15) |
| EGM | QIP rupee split by use | Usually in the notice explanatory statement, not proceedings | ROUTINE by type; open item since 25-Sep (EGM-FN02) |
| EGM | Bridge loan lender, drawn amount, repayment trigger; what the CFO said on "rationale" (L109) | Notice explanatory statement | ROUTINE by type; the tenor wording inside this document is a drafting signal (EGM-FN06) |
| EGM | Share count, issue price, post-issue capital | Notice | ROUTINE by type |
| EGM | Board size | Proceedings list directors present only | ROUTINE |
| TRK | Installed capacity | Commencement disclosures usually state capacity | SILENCE SIGNAL (moderate) |
| TRK | The word "commercial" | A commencement-of-commercial-production disclosure says so | SILENCE SIGNAL (moderate). Status unresolved (TRK-FN-01) |
| TRK | Target date for the start | Often restated to show delivery against plan | ROUTINE by type; it means "early" rests on memory only |
| TRK | Capex spent | Often stated | SILENCE SIGNAL (low) |
| TRK | Order book figure | Memory carried $30M; the letter cites the order book as the reason for the plant | SILENCE SIGNAL (low) (TRK-FN-03) |
| TRK | Revenue share, segment or capex for the power electronics strand | The letter describes an "expansion into power electronics and energy storage technologies" (L41-43) | SILENCE SIGNAL (low) (TRK-FN-05) |
| TRK | First revenue quarter, utilisation path | Rarely in a one-page letter | ROUTINE |
| Both | Financial table behind the headline; auditor review status | Press-release standard | ROUTINE for these document types (neither reports financials) |

No sustained silence on a known deteriorating metric. No silence item is a confirmatory negative on this evidence. The Sangli silence is the one that matters; it becomes confirmatory only if the Q2 FY27 results also stay silent.

Drafting-care tally: 7 drafting defects in a 4-page filing, plus a possible eighth.
1. Tenor wording "for 11 years" on a bridge (EGM L110-111; EGM-FN06).
2. Directors table offset by one row (EGM L59-67; EGM-FN07).
3. Attendee table offset by one row (EGM L69-78; EGM-FN08).
4. "Suryanshi" for Suryavanshi (EGM L70; EGM-FN09).
5. "Jeyaraman" for Jayaraman (EGM L98; EGM-FN09).
6. "After the compilation of the speech" for completion (EGM L100; EGM-FN09).
7. Resolution-type column not aligned to items (EGM L136-139; EGM-FN10).
8. Possible: CFO hand-off recorded twice, by the Chairman (L98-99) and by the CS (L100-102) (EGM-FN09).
Each one alone is immaterial. Together they are a governance data point on disclosure care during a 700 crore raise and a promoter RPT.

---

## PROCESS VERDICT

PROCEED WITH FLAGS.
- Cash conversion INDETERMINATE (Step 5a) caps the verdict at PROCEED WITH CAVEATS. Missing: Q2 FY27 cash-flow statement and balance sheet.
- Material flags move it to PROCEED WITH FLAGS: the EGM document does not show that any resolution passed; the promoter loan's "11 years" tenor sits against "bridge"; Sangli silence in a briefing on expansion plans; quarter tag (both events in Q3 FY27).
- Not REWORK: all A2 and A3 gates passed (including the loop 1 TRK updates); no Verifier A finding applies to this stage. A5 loop findings are closed in the change logs below.
- Decision Status: WATCHLIST, unchanged. No pre-committed trigger fired. The human decides.

FLAGS (surfaced for the verdict):
1. NO_VOTING_RESULT: the EGM document does not show that any resolution passed (EGM L148-149). Treat QIP, swap and RPT as proposed until M1.
2. BRIDGE_TENOR_TENSION: "9% per annum for 11 years" sits against "pending receipt of QIP proceeds" (EGM L110-111). An 11-year facility can still bridge the deal; a bridge would normally end on QIP receipt. Lean bear (Reading B) until the explanatory statement is read. Reading B at full draw: Rs173.25 Cr simple interest over 11 years, about equal to the principal (derived, L110).
3. PROMOTER_FINANCING: second unsecured promoter loan within about a year; up to 15.75 crore a year interest at full draw (derived, EGM L110); facility about Rs51 Cr above the WSIL cash leg [memory arithmetic]. STRUCTURE item, not INTEGRITY, on this evidence.
4. SANGLI_SILENCE: thesis-broken item unmentioned in 2 consecutive company documents [memory count].
5. QUARTER_TAG: both events fall in Q3 FY27 (TRK L36; EGM L29, L122-123). Log tracker entries in Q3 FY27.
6. DILUTION_AMBER_WATCH: swap plus QIP about 7% [memory INFERENCE]; ESOP terms ND; amber line is >8% within 24 months.
7. BOARD_COMPOSITION_UNRESOLVED: 3 or 4 of the 8 directors present are independent (EGM L57-67); board size ND; a promoter RPT is on the agenda.
8. TRK_PROVISIONAL_START: Nigde PCS manufacturing started ahead of a memory target; the letter has no target date and says "manufacturing operations", not commercial production (TRK L19, L35-36). Not yet a counter-example to the capex-slip pattern.
9. WSIL_ECONOMICS_UNTESTED: price/PAT NOT COMPUTABLE (WSIL PAT NOT FOUND); about 16.0x FY26 sales; 51.5% net margin needed at 31x; cash-leg carry at 9% about Rs11.15 Cr a year, 65.3% of WSIL sales [memory inputs, arithmetic].
10. CASH_INDETERMINATE: no cash-flow statement or balance sheet in either document.
11. DRAFTING_CARE: 7 drafting defects in the 4-page EGM filing, plus a possible eighth.
12. MENTAL_MODEL_UNSIGNED_ON_PAGE, NO_Q1_FY27_RECONCILIATION, STALE_CMP: carried from Notion; downstream /fttcp must not run on an unsigned model.

Out of scope, named by reference only: Section 1B destination PE (31x on page), FV CAGR / Amendment 19, the FTTCP verdict, Role 1 valuation. The 31x figure is used in M6 only as a break-even yardstick for WSIL, not as a valuation. The share-count, ROCE, cash-multiplier, Endoks-concentration and WSIL-economics facts above are flagged for /fttcp and Role 1 (OR-30).

---

## STEP 11. PLAIN-LANGUAGE BRIEF

Provenance key: FILED = exchange-filed document (these two Reg 30 letters, or a filing logged on Notion); MGMT = management claim; SECONDARY = third-party data; INFERENCE = analyst reading. [Notion] marks figures from prior Notion work, not from this run's documents.

### 1. SUMMARY NARRATIVE

Quality Power filed two short notices in October. Neither notice carries a financial statement or a results figure.

The first notice is from Endoks, the Turkish subsidiary. Its new plant in Nigde started making power converters on 16 October 2026 (FILED). These converters go into large battery storage systems and other grid-connected uses. The company calls the plant an expansion into power electronics that complements its established portfolio (MGMT). Prior notes set the plant date at December 2026 [Notion, MGMT]. The start came ahead of that memory target. It does not yet show that plant dates now hold. The letter gives no target date of its own. It records a start of "manufacturing operations", not commercial production. The Sangli slip is measured on commercial production. The letter also gives no capacity, no cost and no order size.

The second notice records the 19 October shareholder meeting. Three items went to a vote: a share swap to buy Winwin Speciality Insulators, a share sale to institutions of up to Rs700 crore, and a deal with the promoters (FILED). The notice does not show that any item passed. The result is due in about 48 hours.

The promoter loan needs the most attention. Promoters offer an unsecured loan of up to Rs175 crore at 9% a year (FILED). Full draw costs up to Rs15.75 crore of interest a year (INFERENCE, arithmetic). The loan funds the deal until the share-sale money arrives. The same line gives a term of 11 years. The two terms pull apart: a bridge should end when the share-sale money arrives. The filing gives one reason for the loan, which is timing. It does not say why the Rs212 crore of March 2026 net cash [Notion] cannot cover the deal. Present cash is ND.

The meeting record never mentions the Sangli plant. No commercial output there by March 2027 breaks the thesis.

No thesis-broken condition fired. The stock stays on WATCHLIST, not held. The entry zone is Rs456 to Rs570 [Notion]. The last page price was Rs1,513.4 (SECONDARY, 24 September, stale). The price must fall 62.3% to reach Rs570. The next test is the vote result. The test that matters is Sangli in the Q2 results.

### 2. SECTOR INTELLIGENCE

- The company names grid flexibility, renewable energy integration and energy storage as the demand for its new plant (MGMT, TRK L46-48). Utility spending on these is the demand driver for the group (INFERENCE).
- Battery storage orders are lumpy. The plant ramps "in accordance with ... customer delivery schedules" (MGMT, TRK L50-51). Output follows project dates, not a steady line (INFERENCE).
- Insulators are a bottleneck input for high-voltage equipment. Prior notes logged an 18 to 24 month lead time [Notion, MGMT]. Buying an insulator maker may ease that constraint (INFERENCE). The filings do not quantify the benefit (EGM L104-105).
- The company asks members to approve a share sale to institutions of up to Rs700 crore (FILED, EGM L106, L140-141). Market access is untested. There is no vote result, launch date or price yet, and a promoter bridge covers the gap until the money arrives (FILED, EGM L110-111).
- Not disclosed this run: sector order data, price trends, any regulatory change.

### 3. BUSINESS-MODEL INTELLIGENCE

- The group earns from three engines [Notion]: the Indian parent (high-voltage coils and reactors), Mehru (instrument transformers), and Endoks in Turkey (power quality and battery storage systems).
- The company describes the plant as an "expansion into power electronics and energy storage technologies, complementing its established portfolio of high-voltage equipment and power quality solutions" (MGMT, TRK L41-43). It also says the plant "strengthens" the group's "manufacturing and system integration capabilities" (MGMT, TRK L45). The verb presents integration as a capability the group already has. Two readings: a planned growth line, or capital and attention moving away from the HVDC core (INFERENCE). The separating observation is a segment line with revenue and capital share.
- Endoks earned 51.1% of FY26 group profit [Notion, FILED]. The group owns 51% of it, so 49% of its profit goes to minority holders [Notion]. The new plant sits inside Endoks (FILED, TRK L35). In-house converters may raise the value the group keeps per storage system (INFERENCE). They also tilt the group further toward Turkey (INFERENCE).
- Winwin economics are untested. Price to profit cannot be computed: WSIL profit is NOT FOUND. On Notion figures the deal costs about 16.0x FY26 sales (Rs272.34 crore against Rs17.07 crore) [Notion, INFERENCE arithmetic]. At 31x earnings WSIL would need a 51.5% net margin. Carrying the Rs123.84 crore cash leg at the 9% bridge rate costs about Rs11.15 crore a year, 65% of WSIL's sales (INFERENCE). The filing names benefits but gives no figure (EGM L104-105).
- Model drift: the group plans to fund growth with outside equity, a share swap and promoter debt at once (FILED, EGM L106-111, L136-141; proposed, vote result ND). FY26 growth ran on internal cash [Notion]. Capital per rupee of profit is set to rise (INFERENCE).
- Dilution: the swap and the share sale together are about 7% [Notion, INFERENCE]. ESOP terms are not disclosed. The amber line is 8% within 24 months [Notion].
- Not disclosed this run: revenue, margins, cash flow, share count, plant capacity, Winwin stake and profit, use split of the Rs700 crore.

### 4. COMPETITION INTELLIGENCE

- Where it wins: the thesis rests on a lead in HVDC coils above 220 kV [Notion, MGMT]. The named threat is Atlanta Electricals or another peer qualifying at 220 kV or more [Notion]. Neither notice touches this.
- Converters: global inverter makers supply most storage converters (INFERENCE; peer names are not in the filings or Notion, PENDING LIVE VERIFICATION). The group calls the plant an "expansion into power electronics" (TRK L41-43). Its edge would be captive demand from its own storage projects (INFERENCE).
- Insulators: Winwin may give captive insulator supply. Revenue was Rs17.07 crore in FY26 (provisional) [Notion, FILED]; profit is undisclosed. The edge is supply security, not scale (INFERENCE). That edge would show in the parent's output, not in Winwin's own profit (INFERENCE).
- Risk to watch: if the converter plant serves only in-group projects, it adds cost without new customers (INFERENCE). The separating observation is third-party converter sales in a future filing.

### 5. FORWARD MAP (next about 10-11 months)

Make-or-break reading: Sangli commercial-production status at the Q2 FY27 results, statutory deadline 14-Nov-2026 [INFERENCE, regulation]. First gate: the vote result, about 21-Oct-2026.

| Date | Catalyst | Bull fork | Bear fork |
|---|---|---|---|
| About 21-Oct-2026 | Reg 44 vote result (M1) | All three pass with wide independent support | Promoter deal passes on thin independent support, or an item fails |
| Date ND (notice already filed) | Bridge tenor in the notice (M2) | Bridge ends when the share sale money arrives | 11-year promoter debt at 9%, Rs173.25 crore of interest at full draw |
| By 14-Nov-2026 | Q2 FY27 results (M3) | Sangli on the Dec 2026-Jan 2027 track; cash conversion above 30% | Sangli date moves toward or past March 2027 |
| Undated | Share sale launch (M5) | Use split is clear; dilution stays under 8% | Large general bucket; dilution with ESOP crosses 8% |
| Undated | Design centre cost and date (M11) | Small and dated | No cost given |
| Q2 or Q3 FY27 filings | Converter segment line (M14) | Separate line with revenue and capital share | No figure; capital drifts from the HVDC core |
| Quarter ends 31-Dec-2026 | Bridge balance on the Q3 balance sheet (M4) | Little or no draw | Full draw held after the share sale |
| Dec 2026 to Jan 2027 [Notion] | Sangli commercial output (M7) | Commercial billing starts | Any reference past March 2027 breaks the thesis |
| By 14-Feb-2027 [INFERENCE] | Q3 FY27 results: first converter figures (M8) | Converter revenue or units shown | No figure; the October start was trial output |
| Date ND | Storage order book figure (M9) | Restated above $30M [Notion] | Still undisclosed |
| By 31-Mar-2027 [Notion] | Winwin completion (M6) | Profit disclosed; a 51.5% net margin is needed to match 31x | Profit still undisclosed; about 16.0x sales stands |
| By 31-Mar-2027 | Sangli thesis-broken test (M7) | Passed | Fired: flag to the human |
| FY27 annual, date ND | Endoks share of group profit (M10) | Near 51% or lower | Above 55% |
| Date ND | Promoter re-check and board count (M12, M13) | Clean; board size shown, at least half independent | Any red flag; fewer than half independent with a promoter deal live |

---

## LOOP 1 CHANGE LOG (A5 audit runs/qpower-q2fy27/work/audit_qpower_q2fy27.md)

| A5 ID | Type | Change made | Lands on |
|---|---|---|---|
| F-1 | FACTUAL | "about 59%" replaced: 62.3% to Rs570 and 69.9% to Rs456 from Rs1,513.4; Notion 59% explained as the Rs1,400 basis [INFERENCE] | Step 6D; brief para 6 |
| F-2 | FACTUAL | "no financial number" changed to "no financial statement or results figure" | Step 2A note; brief para 1 |
| F-3 | FACTUAL | "Both cannot be true" changed to "The two terms pull apart"; "not explained" changed to the filed reason (timing, L110-111) plus the open gap (why March 2026 net cash cannot fund it; present cash ND) | Brief para 4; flag 2; Q5 |
| F-4 | FACTUAL | WSIL stake and subsidiary status marked ND in filed text, [Notion] up to 100%; consolidation and goodwill made conditional | Step 2B; Step 4; F4; Q12; M6 |
| F-5 | FACTUAL | "Equity markets are open to the sector" replaced with the A5 graft (request, not access) | Sector bullet 4 |
| F-6 | FACTUAL | Drafting tally enumerated: 7 defects including EGM L100 "compilation", plus a possible eighth (double CFO hand-off) | Step 10 tally; flag 11 |
| M-1 | MISSING | TRK M01 (L41-43) and M02 (L45) cited; preamble counts updated (103 units; TRK 30) | Step 1; Step 2C; 6B; F11, F12; Business-model and Competition parts |
| M-2 | MISSING | Claim 1 graft: "first time a plant beat its date" and "First counter-example" replaced; no filed target date; manufacturing start vs commercial production | 6B rows; Step 3 delta; flag 8; brief para 2 |
| M-3 | MISSING | Acquisition-economics graft: price/PAT NOT COMPUTABLE; 16.0x sales; 51.5% margin at 31x; Rs11.15 Cr carry = 65.3% of sales; M6 bull fork states the margin it needs | Business-model part; M6; flag 9; forward map Winwin row |
| M-4 | MISSING | "of the 8 directors present; board size ND"; Reg 17(1)(b) floor added as [INFERENCE] | Step 2B; M13; flag 7; forward map; Q15 |
| A3 TRK-FN-05 | upstream | Converted to Q21 and Q22; added M14, F12, 6B, 6E row E | Steps 6-9 |
| S-2 | STYLE | Extra anchor corrections recorded | Step 1 table |
| S-3 | STYLE | No-finding rows listed by ID | Step 1 |
| S-4 | STYLE | Cover-letter and p4 signatures split | Step 2B |
| S-5 | STYLE | YAML notes key annotated as notes to accounts; foot notes counted in preamble | Step 1; YAML |
| S-6 | STYLE | "proves no resolution passed" changed to "does not show that any resolution passed" | Flag 1; verdict; brief |
| S-7 | STYLE | F11 status changed to "initiated" | Step 7 |
| S-8 | STYLE | Res 3 to bridge-loan mapping labelled [INFERENCE] | Step 2B; 6D; 6E; F6; M2; Q3 |
| S-9 | STYLE | Reading B Rs173.25 Cr added | Step 2B; flag 2; M2; forward map |
| S-10 | STYLE | Sector bullet 1 tier-tagged | Sector part |
| S-1 | STYLE | Not applied: A1/A2 item (EGM address row) | none |

## LOOP 2 CHANGE LOG (A5 re-audit runs/qpower-q2fy27/work/audit_qpower_q2fy27_loop1.md)

| A5 ID | Type | Change made | Lands on |
|---|---|---|---|
| F-7 | FACTUAL | "claims new 'system integration capabilities'" replaced with the filed verb: the plant "strengthens" the group's "manufacturing and system integration capabilities" (TRK L45), read as an existing capability. Q19 reworded so it does not assume the capability is new: "How does the plant change the group's system integration capability (L45), and which BESS projects used bought-in PCS or outside integration before?" | Business-model bullet 2; Q19; YAML Q19 copy |
| S-11 | STYLE | "now funds growth" changed to "plans to fund growth ... (proposed, vote result ND)"; "is rising" changed to "is set to rise" | Business-model bullet 5 |
| S-12 | STYLE | "and other grid-connected uses" added (TRK L38-39) | Brief para 2 |
| S-13 | STYLE | "new" no longer put in the company's mouth; filed words quoted ("expansion into", "complementing its established portfolio of high-voltage equipment and power quality solutions") | Brief para 2; 6B PCS row; 6E row E; Step 10 TRK row and preamble; Competition bullet 2; 2C row label |
| S-1, S-2r | STYLE | Not applied: A1/A2 items | none |

Not re-run (unchallenged, carried forward): all other text. Verdict and Decision Status unchanged.

---

```yaml
stage: A4-analyst
company: "QPOWER"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
docs_merged: [presentation]   # two one-off Reg 30 disclosures: EGM outcome 19-Oct-2026; Turkiye PCS commencement 17-Oct-2026; no results filing, no concall
ledger_reconciliation:
  notes: 0     # notes to accounts; the 2 A1 foot notes (EGM) are counted in the preamble
  turns: 0
  slides: 1
  all_reviewed: true
  a3_findings_incorporated: ["EGM-FN01", "EGM-FN02", "EGM-FN03", "EGM-FN04", "EGM-FN05", "EGM-FN06", "EGM-FN07", "EGM-FN08", "EGM-FN09", "EGM-FN10", "EGM-FN11", "EGM-FN12", "EGM-FN13", "EGM-FN14", "EGM-FN15", "TRK-FN-01", "TRK-FN-02", "TRK-FN-03", "TRK-FN-04", "TRK-FN-05"]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "WATCHLIST (not held)"
position_branch: "8A-W"
sc_gap_pat_pct: ["EGM 19-Oct-2026: ND (no financials)", "TRK 17-Oct-2026: ND (no financials)"]
questions_for_management:
  - {q: "File the Reg 44 voting result: for/against on Res 1-3 and non-promoter votes on Res 3", from_finding_id: "EGM-FN01"}
  - {q: "Which of Res 1-3 is the ordinary resolution (type column L136-139 misaligned)?", from_finding_id: "EGM-FN10"}
  - {q: "Is the promoter facility a bridge ending on QIP receipt or 11 years? Prepayable without penalty? Does Res 3 cover it?", from_finding_id: "EGM-FN06"}
  - {q: "Which promoter lends the up-to-175 crore facility, how much is drawn, what triggers repayment?", from_finding_id: "EGM-FN05"}
  - {q: "Filing gives timing as the reason (L110-111); what is present cash, why can March 2026 net cash Rs212 Cr not fund the ~Rs124 Cr cash leg, and why is the facility ~Rs51 Cr above it?", from_finding_id: "EGM-FN05"}
  - {q: "List every 'promoter financing arrangement' (plural, L97) with amount, rate, tenor", from_finding_id: "EGM-FN04"}
  - {q: "What 'future strategic opportunities' (L97) does the QIP fund beyond WSIL?", from_finding_id: "EGM-FN04"}
  - {q: "Rupee split of the up-to-700 crore QIP across four uses, and launch window", from_finding_id: "EGM-FN02"}
  - {q: "Cost and opening date of the Global Design Centre at Sangli; separate from Sangli HVDC plant capex?", from_finding_id: "EGM-FN03"}
  - {q: "Shares issued by swap and QIP, post-issue share count, ESOP pool and strike", from_finding_id: "EGM-FN11"}
  - {q: "WSIL FY26 EBITDA, PAT, net debt, ROCE; quantify 'expected operational benefits' incl. insulator lead times", from_finding_id: "EGM-FN15"}
  - {q: "WSIL stake at completion, completion date; if a subsidiary, first consolidation quarter and expected goodwill", from_finding_id: "EGM-FN12"}
  - {q: "Publish a summary of the EGM shareholder Q&A (L145-147)", from_finding_id: "EGM-FN13"}
  - {q: "Sangli HVDC plant: did the trial run happen, and what is the commercial production date?", from_finding_id: "EGM-FN13"}
  - {q: "Confirm board size, designations of Bharanidharan Pandyan, Chitra Pandyan, Rajendra Iyer, independent-director count, audit committee approval of Res 3", from_finding_id: "EGM-FN07"}
  - {q: "Is Nigde PCS output commercial production with customer-accepted units, or trial runs? What was the internal target date?", from_finding_id: "TRK-FN-01"}
  - {q: "Phase 1 capacity, capex spent vs $2M Phase 1, first PCS revenue quarter", from_finding_id: "TRK-FN-02"}
  - {q: "Share of PCS output for in-group BESS vs third-party or non-BESS customers", from_finding_id: "TRK-FN-02"}
  - {q: "Current international BESS order book, share using in-house PCS, in-house PCS margin vs bought-in cost; how does the plant change the group's system integration capability (L45), and which BESS projects used bought-in PCS or outside integration before?", from_finding_id: "TRK-FN-03"}
  - {q: "Effect of in-house PCS on Endoks share of consolidated PAT in FY27 and FY28", from_finding_id: "TRK-FN-03"}
  - {q: "Will power electronics and energy storage be reported as a separate segment or revenue line from Q2 or Q3 FY27?", from_finding_id: "TRK-FN-05"}
  - {q: "Share of the up-to-700 crore QIP and group capex going to power electronics and energy storage; target revenue share of the strand by FY28", from_finding_id: "TRK-FN-05"}
monitorables:
  - {item: "Reg 44 voting result, Res 1-3", implied_date: "~2026-10-21", source_ref: "EGM L148-149; EGM-FN01"}
  - {item: "EGM notice explanatory statement: bridge tenor, lender, prepayment, Res 3 loan coverage", implied_date: "ND (notice already filed)", source_ref: "EGM L110-111, L142-144; EGM-FN06"}
  - {item: "Q2 FY27 results: revenue, margin, CFO/PAT, Sangli update", implied_date: "by 2026-11-14 (Reg 33 statutory deadline, INFERENCE)", source_ref: "Notion s7 items 1-5; TRK-FN-04"}
  - {item: "Bridge drawdown and balance", implied_date: "Q3 FY27 balance sheet (quarter end 2026-12-31)", source_ref: "EGM L109-111; EGM-FN05"}
  - {item: "QIP launch: price, share count, use split, total dilution vs 8% amber", implied_date: "undated in document", source_ref: "EGM L106-108; EGM-FN02, EGM-FN11"}
  - {item: "WSIL completion, stake, first consolidation, profit disclosure (51.5% net margin needed to match 31x yardstick)", implied_date: "by 2027-03-31 (Notion memory)", source_ref: "EGM L95-96, L104-105; EGM-FN12, EGM-FN15"}
  - {item: "Sangli HVDC commercial production (thesis-broken if after Mar-2027)", implied_date: "Dec 2026-Jan 2027 guidance (memory); test 2027-03-31", source_ref: "Notion s4, s5; EGM-FN13"}
  - {item: "Nigde PCS commercial status, capacity, first PCS revenue", implied_date: "Q3 FY27 results, by 2027-02-14 (Reg 33 statutory, INFERENCE)", source_ref: "TRK L35-36, L50-51; TRK-FN-01, TRK-FN-02"}
  - {item: "International BESS order book figure", implied_date: "ND", source_ref: "TRK L45-46 (M02, R016); TRK-FN-03"}
  - {item: "Endoks share of consolidated PAT vs 55% falsifier", implied_date: "FY27 annual results, ND", source_ref: "Notion s4; TRK-FN-03"}
  - {item: "Global Design Centre at Sangli cost and date", implied_date: "undated in document", source_ref: "EGM L107-108; EGM-FN03"}
  - {item: "Promoter background re-verification", implied_date: "ND (open on Notion)", source_ref: "Notion s4; EGM L109-111, L142-144"}
  - {item: "Board size and independent-director count (Reg 17(1)(b) half-independent floor, INFERENCE)", implied_date: "ND", source_ref: "EGM L57-67; EGM-FN07"}
  - {item: "Segment reporting and capital share for power electronics / energy storage", implied_date: "Q2 or Q3 FY27 filings, ND", source_ref: "TRK L41-43 (M01); TRK-FN-05"}
flags:
  - "NO_VOTING_RESULT: EGM document does not show that any resolution passed (L148-149); QIP, swap, RPT stay proposed until Reg 44 result ~21-Oct-2026"
  - "BRIDGE_TENOR_TENSION: '9% per annum for 11 years' sits against 'pending receipt of QIP proceeds' (EGM L110-111); Reading B full draw = Rs173.25 Cr simple interest over 11 years; lean bear until explanatory statement read"
  - "PROMOTER_FINANCING: second unsecured promoter loan in ~1 year; up to 15.75 crore/yr interest at full draw (derived, L110); facility ~Rs51 Cr above WSIL cash leg (memory arithmetic); STRUCTURE item on this evidence"
  - "SANGLI_SILENCE: thesis-broken item unmentioned in 2 consecutive company documents (memory count); make-or-break at Q2 FY27 results"
  - "QUARTER_TAG: both events fall in Q3 FY27 (TRK L36; EGM L29, L122-123); log tracker entries in Q3 FY27, not Q2"
  - "DILUTION_AMBER_WATCH: swap + QIP ~7% (memory INFERENCE); ESOP ND; amber >8% within 24 months"
  - "BOARD_COMPOSITION_UNRESOLVED: 3 or 4 of the 8 directors present are independent (EGM L57-67); board size ND; promoter RPT on agenda"
  - "TRK_PROVISIONAL_START: Nigde PCS manufacturing start ahead of a memory target; no filed target date; 'manufacturing operations' not commercial production (TRK L19, L35-36); not yet a counter-example to the capex-slip pattern"
  - "WSIL_ECONOMICS_UNTESTED: price/PAT NOT COMPUTABLE (PAT NOT FOUND); ~16.0x FY26 sales; 51.5% net margin needed at 31x; cash-leg carry at 9% ~Rs11.15 Cr/yr = 65.3% of WSIL sales (memory inputs)"
  - "CASH_INDETERMINATE: no cash-flow statement or balance sheet; verdict capped"
  - "DRAFTING_CARE: 7 drafting defects in 4-page EGM filing incl. L100 'compilation', plus a possible eighth (double CFO hand-off)"
  - "NOTION_GAPS: mental model not signed on page; no Q1 FY27 reconciliation; CMP stale (24-Sep); page '59%' fall text fits the Rs1,400 CMP, actual 62.3% to Rs570 / 69.9% to Rs456 from Rs1,513.4"
plain_language_brief_included: true
analyst_note: "Loop 2: F-7 closed; TRK L45 says the plant 'strengthens' an existing system integration capability, so the brief and Q19 no longer call it new. S-11 to S-13 applied. Loop 1 closed all 10 earlier A5 items. Verdict and WATCHLIST unchanged. Two one-off Reg 30 letters with no financial statements, so cash conversion is INDETERMINATE (cap CAVEATS); flags take it to PROCEED WITH FLAGS. The weight sits in promoter financing: a 175 crore unsecured 9% facility called a bridge but worded '11 years'. Reading A: short bridge, drafting error. Reading B: long-dated related-party debt, Rs173.25 Cr interest at full draw. Separating observation: notice explanatory statement and the Q3 FY27 drawn balance. WSIL price/PAT is not computable; about 16.0x sales. The Nigde start is ahead of a memory target only; the letter has no target date and no 'commercial'. Both events fall in Q3 FY27. Regulatory deadlines 14-Nov-2026 and 14-Feb-2027 are INFERENCE from Reg 33."
review_path: "runs/qpower-q2fy27/work/review_qpower_q2fy27.md"
```
