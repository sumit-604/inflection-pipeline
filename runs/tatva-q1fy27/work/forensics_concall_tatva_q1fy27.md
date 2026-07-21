# A3 FORENSIC NOTES — Tatva Chintan Pharma Chem Limited (TATVA), Q1 FY27, DOCTYPE: CONCALL

Source extract: /home/user/inflection-pipeline/runs/tatva-q1fy27/work/extract_concall_tatva_q1fy27.txt
Reconciliation contract: /home/user/inflection-pipeline/runs/tatva-q1fy27/work/ledger_concall_tatva_q1fy27.md
Prior-quarter extract: none supplied (Q4 FY26 verbatim EoM/entity diffs not available; cross-quarter checks rely on the Notion prior-commitment list, weighed as memory, every finding still cited to a transcript line).

RECONCILIATION STATEMENT: Every A2 ledger row was read verbatim at its cited line in the A1 extract before judging. All ledger sections reconciled 100%: Participants (13), Speaker turns (118, lines 21-138), Questions (32), Management/analyst-cited numbers (56), Forward-commitment + hedge phrases (34: 23 FC + 11 H), Zero/nil-standing disclosures (5). No row unread; no row disputed. The A2 count-test (gate_a2: pass) and its anchor-grep methodology were confirmed against the transcript. Doctype = concall: per prompt applicability, F6/F7/F17 apply in full and are the substance of this report; F13 yields a board-outcome finding; the remaining balance-sheet/filing checks (F1-F5, F8-F12, F14-F16) are marked N.A. with a one-line basis each, never left blank (GATE A3).

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------------|----------------|---------------------|
| A3-F01 | F6 | N22, N23 | 41, 43 | "it should contribute around 70 to 80 crores of revenue uh from all these pharma molecules" / "200 in the range of 200" | FORWARD-SIGNAL | Pharma FY27 = Rs70-80cr, full-util ~Rs200cr. A dated promise-vs-delivery peg; ties directly to Notion item (3) SDA/PAC ramp and the Q4 FY26 "1 molecule Q1 + 2 by Q3 end" commitment. |
| A3-F02 | F6 | N25, N26, N33, N34 | 48, 64 | "1.2 to 1 1.5 uh times uh asset turnover ratio... around 300 crores of revenue at peak utilization"; "within 21 months. Internally we are pushing to get it through within 18 months" | FORWARD-SIGNAL | Greenfield adds only ~Rs300cr peak revenue for ~Rs200cr capex (1.5x turn), not the legacy 3.0x. Commissioning ~Jan-Apr 2028. Capacity ceiling 800-850cr hit "from next year itself" (line 64) => growth-stagnation risk if project slips. |
| A3-F03 | F6 | N30, N11 | 51, 53 | "between 40 to 50 cr is what we still hold the guidance"; "unfortunately we lost a couple of months due to unavailability of couple of key raw materials" | FORWARD-SIGNAL | ESS FY27 Rs40-50cr reaffirmed despite Q1 printing only Rs6.3cr (down 52% QoQ, N11) and losing "a couple of months" to Middle-East raw-material shortage. Implies a very steep H2 back-end load; monitoring item (3) at risk. |
| A3-F04 | F6 | N24, N35 | 45, 68 | "not before Q4 of 2028 I don't see that it will commercialize in a large volume" | FORWARD-SIGNAL | Semiconductor large-volume revenue explicitly deferred to >=Q4 CY2028; "we are not doing any capex at the moment" (Z3). First batch delivered/qualified this quarter (Notion item 5 met) but monetisation is 2+ years out. Manages down any near-term semi revenue in the model. |
| A3-F05 | F6 | N36, N37 | 70, 72 | "25 30% growth is what we forecasted and that's what we stick to"; "I would still stick to 20 22% margins" | FORWARD-SIGNAL | FY27 growth 25-30% and margin 20-22% reaffirmed AFTER admitting "we have lost one quarter with a little lesser margin" (line 72). Reconcile against Role 4 QoQ operating-margin fade 21.0%->19.3%; the 20-22% target is now a stretch off a sub-20% Q1 base (Notion item 4 RED-line 18%). |
| A3-F06 | F6 | N44, N45, N46, N47 | 121, 123 | "asset turn ratio of 1.5 we are very happy... when we were talking of the earlier three product ranges we were talking of asset of one is to three. So the ball game has changed"; "ROC we look at about 20 22%" | FORWARD-SIGNAL | MD openly confirms a STRUCTURAL halving of asset turnover (3.0x PTC/SDA/ESS -> 1.5x multi-stage pharma/agro). This is a permanent downshift to the ROCE anchor even as ROC is still framed at 20-22%. Directly stresses Notion item (2) ROCE clearing 8% and the exit-economics thesis. |
| A3-F07 | F7 | H1 | 36 | "uh none of them uh we don't foresee any uh obstacles to achieve our uh this year's guidance" | AMBIGUOUS | Asked to name the biggest execution risk (demand vs raw-material vs commercialization), management named NONE — a refusal to concede any risk. Contradicted within the same call by the ESS raw-material shortage (line 53) and margin-passthrough lag (line 60). Over-confidence flag; convert to a direct A4 question. |
| A3-F08 | F7 | H7, FC15 | 85 | "it is too early to predict and you never know what the China is going to do. So let us wait and watch and not speculate" | AMBIGUOUS | China anti-involution / subsidy withdrawal (dated "from January of next year") is the single largest external pricing swing factor for PTC/SDA/agro, yet left unquantified. The China price variable also drives the withheld monoglime plan (F12). |
| A3-F09 | F7 | H8, H9 | 112, 113 | "potentially we are the smallest player within the segment"; "I'm sure with given dedication or a given vision any one of them can crack this" | FORWARD-SIGNAL | MD concedes the continuous-flow-chemistry moat is replicable by any dedicated competitor. Bears directly on moat-durability and the terminal multiple; a candid negative on the core differentiation thesis. |
| A3-F10 | F7 | H4 | 60 | "honestly speaking we have not been thorough in terms of passing on the increase in cost that is visible on our margins" | CONFIRMATORY-NEGATIVE | Explains the QoQ margin fade: cost pass-through lagged. Pass-through only "started" 40-50 days ago (F07-adjacent, line 62), so margin recovery is unproven and back-loaded — confirms the Role 4 margin-fade concern rather than dispelling it. |
| A3-F11 | F7 | H10, FC20 | 119 | "there may not be a contract official contract in place but there is of of course some uh commitment from a customer" | AMBIGUOUS | The ~Rs200cr greenfield (2.0x book capex) rests on informal, non-contracted customer interest only. Combined with Z1 (ESS "never an order book in hand") the whole demand base is order-book-free. Convert to an A4 question on offtake visibility. |
| A3-F12 | F7 | N48-N53 | 30, 126 | "environment scenario in terms of pricing has become too aggressive from the Chinese supplies. So we have withheld our plan to invest as of now into the client's capacity addition" | FORWARD-SIGNAL | A previously-guided ~2,000-ton monoglime continuous-flow capex is WITHDRAWN after a Chinese price crash ($4.6-4.8 -> $2.1 in 30 days, N49-N51). The installed continuous-flow equipment was repurposed to a super-capacitor electrolyte product. A capex-plan reversal that should be struck from the catalyst timeline. |
| A3-F13 | F7 | H_note (line 53) / N11 | 53 | "we lost a couple of months due to unavailability of couple of key raw materials in this space it just happened because of this uh war situation" | CONFIRMATORY-NEGATIVE | Middle-East war-driven raw-material shortage is the mechanical cause of the ESS -52% QoQ print. Supply-chain single-point exposure; the "gradually getting streamlined" recovery (line 22) is unquantified and underpins the aggressive H2 ESS reaffirmation (F03). |
| A3-F14 | F13 | FC6, FC7, N19, N20 | 22 | "board of directors has today approved the establishment of a new green field manufacturing facility involving an investment of approximately rupees 200 crores... groundbreaking ceremony for this on 20th July 2026" | FORWARD-SIGNAL | Board outcome beyond results: a hard, dated catalyst (groundbreaking 20-Jul-2026, one day before this run date 21-Jul-2026 — verify it occurred, no 4th slip). Management never named it "Dahej-III"; whether this greenfield IS the previously-guided Dahej-III project (Notion item 5) or a separate multi-product site was not clarified on the call — schedule the FTTCP catalyst event and resolve the naming. |
| A3-F15 | F17 | (whole-call silence) | n/a (absent) | (no transcript line — item never raised) | CONFIRMATORY-NEGATIVE | The top Role 4 question — subsidiary earnings quality / transfer pricing (US/Europe WOS = 34.6% of consolidated PAT and 43% of PAT growth with a zero cost base) — was NOT raised by any of 8 analysts and NOT volunteered by management across all 118 turns. Sustained silence on the single largest earnings-quality question is a confirmatory negative; escalate to A4 as the priority management question. |
| A3-F16 | F17 | (whole-call silence) | n/a (absent) | (no transcript line — items never raised) | CONFIRMATORY-NEGATIVE | Rs 1.32 Cr unexplained exceptional charge, nil standalone current tax, and the standalone-vs-consolidated PAT split (parent profit share >50%, Notion item 7) — none addressed. The call disclosed segment revenue only (N7-N18); zero balance-sheet, tax, or standalone/consolidated commentary. These silences are why F2/F8 are N.A. here and must be carried forward. |
| A3-F17 | F17 | (whole-call silence) | n/a (absent) | (no transcript line — items never raised) | CONFIRMATORY-NEGATIVE | Cash conversion / receivable days (Notion item 1), net-debt/EBITDA under 0.65x and credit rating (item 6), and the Rs1,000cr / 3.3x borrowing-limit expansion — all unaddressed while the board approves fresh ~Rs200cr capex (F14). Rising-leverage-into-capex with no coverage commentary is a confirmatory negative on the cash/leverage watch. |
| A3-F18 | F17 | FC4 vs Notion prior commitment | 22 | "additional pharma molecules are also expected to move towards commercialization in the later half of the year" | AMBIGUOUS | Prior Q4 FY26 commitment "2 more molecules by Q3 end" appears SOFTENED to "later half of the year" (Q3 hard date dropped). Separately, SDA was discussed only qualitatively (Euro7 momentum, line 22/97) with NO FY27 rupee number given (Notion item 3 target Rs250-300cr) — a partial silence on a specific monitored figure. Convert both to A4 questions. |

Note on F13 dual-mapping: the board-approval FACT is logged as A3-F14 under F13 (board outcome / catalyst scheduling). The same capex's economics/timeline (turn ratio, 21/18-month, ~300cr peak) are logged as A3-F02 under F6 (forward-commitment), not double-counted.

---

## 2. CHECKLIST SCORECARD (all 17; PASS / FINDING / N.A.)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 Zero-value standing line items | N.A. | Concall, no filing template line items. Concall analogues captured as ledger section G (Z1-Z5, ZERO_STANDING) and folded into F04/F11/F12/F17 rather than dropped. |
| F2 Standalone vs consolidated decomposition | N.A. | Concall presented segment revenue only (N7-N18); no standalone/consolidated financials to decompose. The S-vs-C split's ABSENCE is itself flagged under F17 (A3-F16). |
| F3 Shell-entity detection | N.A. | Concall; no cost-line detail (COGS/employee/depreciation) standalone vs consolidated to compare. Subsidiary zero-cost-base concern routed to F17 (A3-F15). |
| F4 Unaudited contribution ratio | N.A. | Concall; no auditor "Other Matters" paragraph present in a transcript. |
| F5 Going concern / EoM scope tracking | N.A. | Concall; no EoM/going-concern language, and no prior-quarter extract supplied to verbatim-diff. |
| F6 Forward-commitment phrase mining | FINDING | 23 forward-commitment phrases (FC1-FC23) yield a dated commitment register; six carry material forward tension (A3-F01 to A3-F06). See register in section 3. |
| F7 Hedge phrase mining | FINDING | 11 hedges (H1-H11) incl. the "none of them" risk refusal (A3-F07), replicable-moat concession (A3-F09), margin-passthrough-lag admission (A3-F10), informal-only offtake (A3-F11), withdrawn monoglime capex (A3-F12), ESS shortage (A3-F13). |
| F8 Tax forensics | N.A. | Concall; no ETR / deferred-tax / earlier-year-adjustment data. Nil standalone current tax (Role 4) NOT raised on call -> flagged under F17 (A3-F16). |
| F9 OCI forensics | N.A. | Concall; no OCI / actuarial disclosure in transcript. |
| F10 Share count and dilution | N.A. | Concall; no paid-up capital / EPS spread disclosed. |
| F11 Reserves and net worth tie-out | N.A. | Concall; no equity/reserves figures disclosed. |
| F12 Segment forensics (assets/liabilities) | N.A. | Concall; only segment REVENUE (N7-N18) given, no segment assets/liabilities to trend. |
| F13 Board outcome beyond the results | FINDING | Board today approved ~Rs200cr greenfield with 20-Jul-2026 groundbreaking (A3-F14): a dated catalyst to schedule; naming vs prior Dahej-III unresolved. |
| F14 Note drafting inconsistencies | N.A. | Concall; no note text vs auditor letter to cross-check. (A2 POSSIBLE_FIRM_NAME_OVERLAP "Zenflow Finance" vs "Zenflow Finance Private Limited" noted; immaterial, not a governance data point.) |
| F15 Entity list diffs | N.A. | Concall; no consolidation entity list, and no prior extract to diff. |
| F16 Presentation-specific dropped/reframed disclosures | N.A. | Not a presentation deck. Cross-quarter guidance softening ("2 more by Q3 end" -> "later half of the year") is captured under F17 (A3-F18). |
| F17 Concall silence audit | FINDING | Top Role 4 items (subsidiary transfer price, Rs1.32cr exceptional, nil standalone tax, S-vs-C split, cash conversion, leverage) NOT raised by any analyst or management (A3-F15/F16/F17); one guidance softening (A3-F18). See section 4. |

Blank checks: none. GATE A3: pass.

---

## 3. COMMITMENT REGISTER (F6 — promise-vs-delivery tracker)

| # | Commitment | Implied date | Ref (line / FC / N) | Status word |
|---|-----------|--------------|----------------------|-------------|
| C1 | Greenfield facility ~Rs200cr, board-approved | groundbreaking 20-Jul-2026 | L22 / FC6-FC7 / N19-N20 | initiated (board-approved) |
| C2 | Greenfield in operation | 21 months (stretch 18) from GB => ~Jan-Apr 2028 | L64 / FC12 / N33-N34 | initiated |
| C3 | Greenfield peak revenue ~Rs300cr at 1.2-1.5x asset turn | at peak utilization (post-C2) | L48 / N25-N26 | planned |
| C4 | Pharma molecules incremental revenue Rs70-80cr | FY27 | L41 / N22 | underway (1 molecule commenced Q1) |
| C5 | Pharma molecules revenue ~Rs200cr | at full utilization | L43 / N23 | planned |
| C6 | Additional pharma molecules commercialization | later half FY27 (was "2 by Q3 end") | L22 / FC4 | underway (softened, see A3-F18) |
| C7 | ESS revenue Rs40-50cr | FY27 | L51 / N30 | underway (Q1 -52% QoQ; back-loaded) |
| C8 | Semiconductor first commercial batch delivered & qualified | Q1 FY27 | L22, L46 / FC3-adjacent | completed |
| C9 | Semiconductor 3-4 plant-scale trials | over next 2 years (~by 2028) | L45 / FC8 / N24 | underway |
| C10 | Semiconductor large-volume commercialization | not before Q4 CY2028 | L68 / N35 | planned (deferred) |
| C11 | FY27 revenue growth 25-30% | FY27 | L70 / FC13 / N36 | reaffirmed |
| C12 | FY27 EBITDA margin 20-22% | FY27 | L72 / FC14 / N37 | reaffirmed (off sub-20% Q1) |
| C13 | Revenue CAGR 20-25% | next 3-4 years | L121 / FC21 / N44 | reaffirmed |
| C14 | ROC target 20-22% (asset turn now 1.5x vs legacy 3.0x) | ongoing | L123 / FC22 / N45-N47 | reaffirmed (structural downshift) |
| C15 | Price pass-through to customers | started last 40-50 days | L61-62 / FC10-FC11 | initiated (unproven) |
| C16 | Euro7 rollout beyond Europe (US/Japan/China/India) | next 3-4-5 years | L97 / FC16 / N38 | underway (Europe begun) |
| C17 | Hybrid-battery customer commercialization | Oct/Nov CY2026 | L99 / FC17 / N39 | underway |
| C18 | Hybrid-battery full-scale commercialization | late CY2027 | L102 / FC18 / N40 | planned |
| C19 | 7-8 products into commercial/piloting phase | near future | L108 / FC19 / N42 | underway |
| C20 | China subsidy withdrawal (external, conditional) | from Jan 2027 if it happens | L85 / FC15 / H7 | monitoring (unquantified) |
| C21 | Monoglime ~2,000-ton continuous-flow capacity | WITHDRAWN / deferred | L30, L126 / N48-N53 | withdrawn (A3-F12) |

Status-transition notes (feed Role 5): C8 semiconductor moved initiated -> completed (first plant-scale batch delivered AND qualified) — a genuine milestone confirmation. C4/C6 pharma moved into "commenced" (industrial production of one intermediate began Q1) but C6's hard Q3 date was dropped. C21 is a reversal (previously-guided capex withdrawn), the only negative status transition on the call.

---

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit)

Cross-referenced against the Notion monitoring checklist and the Role 4 results-review items. Prior-quarter extract unavailable, so consecutive-quarter silence counts are stated as "at least" based on the supplied prior-commitment context; A4/A5 to confirm depth against the Q4 FY26 transcript.

| Item (monitoring / Role 4 source) | Raised by analyst? | Addressed by mgmt? | Consecutive-silence note | Finding |
|-----------------------------------|--------------------|--------------------|--------------------------|---------|
| Subsidiary earnings quality / transfer price — US/Europe WOS = 34.6% of consol PAT, 43% of PAT growth, zero cost base | No (0 of 8 analysts) | No | Top Role 4 question; silent this call (>=1 qtr). Deteriorating earnings-quality question => confirmatory negative | A3-F15 |
| Rs 1.32 Cr unexplained exceptional charge | No | No | Silent (>=1 qtr) | A3-F16 |
| Nil standalone current tax | No | No | Silent (>=1 qtr) | A3-F16 |
| Standalone vs consolidated PAT split; parent profit share >50% (Notion 7) | No | No | Silent (>=1 qtr) | A3-F16 |
| Cash conversion / receivable days (Notion 1) | No | No | Silent (>=1 qtr) while fresh capex approved | A3-F17 |
| Net-debt/EBITDA <0.65x, credit rating, Rs1,000cr / 3.3x borrowing-limit (Notion 6) | No | No | Silent (>=1 qtr) into a leverage-funded capex cycle | A3-F17 |
| ROCE clearing 8% (Notion 2) | Partial (Q28 asked ROIC) | Partial — only forward ROC 20-22% target given (L123), no current ROCE | Forward target, not the monitored actual | A3-F06 (partial) |
| SDA FY27 revenue >=20% to Rs250-300cr (Notion 3) | No (only qualitative Euro7) | No rupee figure | Qualitative only; specific number silent | A3-F18 |
| EBITDA margin holding 20-22% (Notion 4) | Yes (Q16) | Yes — reaffirmed 20-22% (L72) | Addressed | — (see A3-F05) |
| Dahej-III groundbreaking, no 4th slip (Notion 5) | Yes (Q9) | Yes — greenfield GB 20-Jul-2026 (L22), but not named "Dahej-III" | Addressed with naming ambiguity | A3-F14 |
| Semiconductor first dispatch Q1 FY27 (Notion 5) | Yes (Q6-Q8) | Yes — first batch delivered & qualified (L22/L46) | Addressed / delivered | C8 |
| Peer demand tone (Notion 8) | Yes (Q17/Q19) | Yes — China anti-involution + Euro7 color (L85/L97) | Addressed | — |

Silence verdict: the four highest-value Role 4 earnings-quality/leverage questions (subsidiary transfer price, exceptional charge, standalone tax, cash/leverage) went entirely unraised and unaddressed across 32 analyst questions and 118 turns. Per Role 5, sustained silence on deteriorating/unexplained items is a confirmatory negative. These are the priority conversions for A4 management questions.

---

## 5. HANDOFF TO A4

FORWARD-SIGNAL findings (build management questions / update FTTCP catalyst timeline): A3-F01, A3-F02, A3-F03, A3-F04, A3-F05, A3-F06, A3-F09, A3-F12, A3-F14.
AMBIGUOUS findings (lean-bear, convert to direct questions): A3-F07, A3-F08, A3-F11, A3-F18.
CONFIRMATORY-NEGATIVE (carry into verdict, no resolution on call): A3-F10, A3-F13, A3-F15, A3-F16, A3-F17.
Catalyst to schedule (F13): greenfield groundbreaking 20-Jul-2026 — verify occurrence (run date 21-Jul-2026) and resolve whether it is the Notion Dahej-III project.

---

```yaml
stage: A3-forensics
company: "TATVA"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/tatva-q1fy27/work/forensics_concall_tatva_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
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
  F13: FINDING
  F14: N.A.
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3-F01", check: "F6", line: "41,43", classification: "FORWARD-SIGNAL", implication: "Pharma FY27 Rs70-80cr, full-util ~Rs200cr; dated promise-vs-delivery peg"}
  - {id: "A3-F02", check: "F6", line: "48,64", classification: "FORWARD-SIGNAL", implication: "Greenfield ~Rs300cr peak at 1.5x turn, 21/18-mo; ceiling 800-850cr hit next year"}
  - {id: "A3-F03", check: "F6", line: "51,53", classification: "FORWARD-SIGNAL", implication: "ESS Rs40-50cr FY27 reaffirmed despite Q1 -52% QoQ and lost 2 months; steep H2 load"}
  - {id: "A3-F04", check: "F6", line: "45,68", classification: "FORWARD-SIGNAL", implication: "Semiconductor large-volume revenue deferred to >=Q4 CY2028; no capex now"}
  - {id: "A3-F05", check: "F6", line: "70,72", classification: "FORWARD-SIGNAL", implication: "FY27 25-30% growth + 20-22% margin reaffirmed off a sub-20% Q1 margin base"}
  - {id: "A3-F06", check: "F6", line: "121,123", classification: "FORWARD-SIGNAL", implication: "Structural asset-turn halving 3.0x->1.5x; permanent downshift to ROCE anchor"}
  - {id: "A3-F07", check: "F7", line: "36", classification: "AMBIGUOUS", implication: "MD names NO execution risk ('none of them'); over-confidence vs same-call raw-material/margin admissions"}
  - {id: "A3-F08", check: "F7", line: "85", classification: "AMBIGUOUS", implication: "China subsidy withdrawal (Jan-2027) left unquantified; largest external pricing swing"}
  - {id: "A3-F09", check: "F7", line: "112,113", classification: "FORWARD-SIGNAL", implication: "MD concedes continuous-flow moat is replicable by any dedicated competitor"}
  - {id: "A3-F10", check: "F7", line: "60", classification: "CONFIRMATORY-NEGATIVE", implication: "Cost pass-through lag explains margin fade; recovery only just 'started', unproven"}
  - {id: "A3-F11", check: "F7", line: "119", classification: "AMBIGUOUS", implication: "Rs200cr greenfield rests on informal, non-contracted offtake only; order-book-free demand base"}
  - {id: "A3-F12", check: "F7", line: "30,126", classification: "FORWARD-SIGNAL", implication: "Monoglime ~2,000t capex WITHDRAWN after Chinese price crash; strike from catalyst timeline"}
  - {id: "A3-F13", check: "F7", line: "53", classification: "CONFIRMATORY-NEGATIVE", implication: "Middle-East war raw-material shortage is mechanical cause of ESS -52% QoQ; single-point supply exposure"}
  - {id: "A3-F14", check: "F13", line: "22", classification: "FORWARD-SIGNAL", implication: "Board-approved ~Rs200cr greenfield, GB 20-Jul-2026; schedule catalyst, verify vs Dahej-III naming"}
  - {id: "A3-F15", check: "F17", line: "absent", classification: "CONFIRMATORY-NEGATIVE", implication: "Subsidiary transfer-price (34.6% of PAT, zero cost base) unraised/unaddressed across all 118 turns"}
  - {id: "A3-F16", check: "F17", line: "absent", classification: "CONFIRMATORY-NEGATIVE", implication: "Rs1.32cr exceptional, nil standalone tax, S-vs-C split all silent; segment revenue only disclosed"}
  - {id: "A3-F17", check: "F17", line: "absent", classification: "CONFIRMATORY-NEGATIVE", implication: "Cash conversion, net-debt/EBITDA, credit rating, Rs1000cr limit silent while fresh capex approved"}
  - {id: "A3-F18", check: "F17", line: "22", classification: "AMBIGUOUS", implication: "Prior '2 molecules by Q3 end' softened to 'later half of year'; SDA FY27 rupee figure not given"}
forward_signals: ["A3-F01","A3-F02","A3-F03","A3-F04","A3-F05","A3-F06","A3-F09","A3-F12","A3-F14"]
ambiguous: ["A3-F07","A3-F08","A3-F11","A3-F18"]
commitments:
  - {commitment: "Greenfield facility ~Rs200cr, board-approved", implied_date: "groundbreaking 2026-07-20", ref: "L22/FC6-FC7/N19-N20", status_word: "initiated"}
  - {commitment: "Greenfield in operation", implied_date: "21mo (stretch 18mo) from GB, ~Jan-Apr 2028", ref: "L64/FC12/N33-N34", status_word: "initiated"}
  - {commitment: "Greenfield peak revenue ~Rs300cr at 1.2-1.5x asset turn", implied_date: "at peak utilization", ref: "L48/N25-N26", status_word: "planned"}
  - {commitment: "Pharma molecules incremental revenue Rs70-80cr", implied_date: "FY27", ref: "L41/N22", status_word: "underway"}
  - {commitment: "Pharma molecules revenue ~Rs200cr", implied_date: "at full utilization", ref: "L43/N23", status_word: "planned"}
  - {commitment: "Additional pharma molecules commercialization", implied_date: "later half FY27", ref: "L22/FC4", status_word: "underway"}
  - {commitment: "ESS revenue Rs40-50cr", implied_date: "FY27", ref: "L51/N30", status_word: "underway"}
  - {commitment: "Semiconductor first commercial batch delivered & qualified", implied_date: "Q1 FY27", ref: "L22,L46", status_word: "completed"}
  - {commitment: "Semiconductor 3-4 plant-scale trials", implied_date: "over next 2 years (~2028)", ref: "L45/FC8/N24", status_word: "underway"}
  - {commitment: "Semiconductor large-volume commercialization", implied_date: "not before Q4 CY2028", ref: "L68/N35", status_word: "planned"}
  - {commitment: "FY27 revenue growth 25-30%", implied_date: "FY27", ref: "L70/FC13/N36", status_word: "reaffirmed"}
  - {commitment: "FY27 EBITDA margin 20-22%", implied_date: "FY27", ref: "L72/FC14/N37", status_word: "reaffirmed"}
  - {commitment: "Revenue CAGR 20-25%", implied_date: "next 3-4 years", ref: "L121/FC21/N44", status_word: "reaffirmed"}
  - {commitment: "ROC target 20-22% (asset turn 1.5x vs legacy 3.0x)", implied_date: "ongoing", ref: "L123/FC22/N45-N47", status_word: "reaffirmed"}
  - {commitment: "Price pass-through to customers", implied_date: "started last 40-50 days", ref: "L61-62/FC10-FC11", status_word: "initiated"}
  - {commitment: "Euro7 rollout beyond Europe", implied_date: "next 3-4-5 years", ref: "L97/FC16/N38", status_word: "underway"}
  - {commitment: "Hybrid-battery customer commercialization", implied_date: "Oct/Nov CY2026", ref: "L99/FC17/N39", status_word: "underway"}
  - {commitment: "Hybrid-battery full-scale commercialization", implied_date: "late CY2027", ref: "L102/FC18/N40", status_word: "planned"}
  - {commitment: "7-8 products into commercial/piloting phase", implied_date: "near future", ref: "L108/FC19/N42", status_word: "underway"}
  - {commitment: "China subsidy withdrawal (external, conditional)", implied_date: "from Jan 2027 if it happens", ref: "L85/FC15/H7", status_word: "monitoring"}
  - {commitment: "Monoglime ~2,000t continuous-flow capacity", implied_date: "withdrawn/deferred", ref: "L30,L126/N48-N53", status_word: "withdrawn"}
gate_a3: pass
blank_checks: []
```
