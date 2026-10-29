# A3 FORENSIC NOTES: SYNGENE Q2 FY27, doctype RESULTS (quarter and half year ended 30-Sep-2026)

Agent: A3 forensics | model: claude-opus-5-5 | run date: 2026-10-28
Inputs read: A1 structured `runs/syngene-q2fy27/extracted/syngene-results-q2fy27-structured.md` (R001-R828, all rows read); A1 fulltext `runs/syngene-q2fy27/extracted/syngene-results-q2fy27-fulltext.md` (lines 1-639, all read); A2 ledger `runs/syngene-q2fy27/work/ledger_results_syngene_q2fy27.md`; checklist `runs/syngene-q2fy27/work/monitoring_checklist.md`.
Not read: the source PDF and anything under `inputs/`.
Prior-quarter fulltext: NONE AVAILABLE. The F5 auditor-paragraph diff and the F15 entity-list diff could not run against a prior-quarter text. Both checks ran on the evidence inside this filing (comparative columns, dated notes, and the auditor's own statement of which periods the predecessor reviewed).
Units: Rs million as filed (x0.1 to Rs crore). "Computed" marks an A3 arithmetic result from filed figures. It is not a filed number.

## 0. LEDGER RECONCILIATION

- Structured IDs in ledger: 828 of 828 (A2 orphan_ids: []). A3 read 828 of 828 rows: **100%**.
- 227 line-item rows (667 cells): each read at its cited fulltext line (pages 2-7, lines 76-442). No value mismatch found between structured rows and fulltext lines.
- 9 notes (lines 455-509), 12 auditor paragraphs (lines 519-638), 5 entities, 4 signature blocks, 1 agenda item, 15 ZERO_STANDING rows: each read at its line.
- Arithmetic ties checked: consolidated and standalone balance sheet totals foot (e.g. consolidated current liabilities sum to 11,829, l.189). Consolidated CFO build from l.204 to l.226 foots to (1,432). Equity = paid-up + other equity in all four balance-sheet columns.
- A1 flags carried: R807 (note numbers mapped by elimination), R827/R828 (column unresolved, l.290 and l.402). A3 does not resolve these. No inference is drawn from the l.290 "- -" row.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R073-R078, R408-R413, R685-R687, R817 | l.89, l.486-489 | "Considering the nature, significance and frequency of these benefits, these are disclosed as "exceptional items"" | FORWARD-SIGNAL | The exceptional line was nil in Q2 FY26 and H1 FY26 (l.89). It is now live in three straight periods: termination benefits of Rs 303m (FY26), 135m (Q1 FY27), 67m (Q2 FY27). The note cites "frequency" as the reason to treat a cost as exceptional. Exceptional means infrequent. A recurring headcount-exit cost sits below "PBT before exceptional items". That PBT (537, l.88) is flattered by 67m. Expect more charges until management states the programme size and end date. FY26 ties: consolidated 766 = 463 labour code + 303 termination; standalone 732 = 429 + 303 (computed). |
| A3-02 | F1 | R222-R223, R559-R560, R240-R241, R575-R576 | l.174, l.186, l.367, l.378 | "Provisions - 180" | AMBIGUOUS | Non-current provisions went from 180 to nil. Current provisions went from 1,144 to 832. Total consolidated provisions fell 492 in six months (computed; standalone fell 433). Reading 1: gratuity and benefit liabilities were funded or settled in cash. This would sit inside the (3,822) working-capital line at l.223. Reading 2: a reclassification only. The separating observation is the provisions roll-forward and gratuity plan contributions for H1. Ask. |
| A3-03 | F1 | R298-R299, R632-R633, R176-R177, R513-R514 | l.231, l.423 | "Investment in equity shares (25) -" | AMBIGUOUS | This is a new Rs 25m equity investment. The same 25 appears in both the standalone and consolidated cash flows, so it was not eliminated on consolidation. The investee is therefore outside the group. The parent's net investment in subsidiaries (standalone NC investments minus consolidated) is 8,339 at both dates (computed). The investee is not named. Ask for its identity, purpose and any related-party link (T6). |
| A3-04 | F2 | R001-R006 vs R336-R341; R067-R072 vs R402-R407; R103-R108 vs R438-R443 | l.76, l.88, l.95, l.267, l.279, l.286 | cons "Profit for the period / year (5-6) 322 (90) 671 232 1,538 3,167" vs stand "487 (21) 662 466 1,402 3,049" | FORWARD-SIGNAL | Subsidiaries moved from adding to subtracting. Subsidiary PAT gap (cons minus stand) as % of standalone PAT: Q2 FY26 +9 (+1.4%), Q2 FY27 -165 (-33.9%), a 35.3 pp swing. H1 FY26 +136 (+9.7%), H1 FY27 -234 (-50.2%), a 59.9 pp swing. Both exceed the 5 pp trigger. The subsidiary EBITDA gap went 220 to 0 YoY. Subsidiary revenue went 805 to 548 (-32%). All computed; see table 2.1. This is after Rs 661m of US-site pre-operative cost was capitalised (A3-06). The drag grows when that site starts to depreciate. |
| A3-05 | F5 | R822, R825, R720, R770-R772, R776-R778, R821, R824 | l.563-568, l.618-623 | "were reviewed by the predecessor auditor ... on November 05, 2025, July 29, 2026 and April 29, 2026 respectively" | AMBIGUOUS | The predecessor auditor reviewed Q1 FY27 (29-Jul-2026). S.R. Batliboi & Associates LLP signed Q2 FY27. So the statutory auditor changed between Q1 and Q2 FY27, and this is the new auditor's first review. The predecessor is not named (R720). Neither report carries an Emphasis of Matter or going-concern language. Both conclusions are unmodified (l.555, l.612). The Other Matter paragraph is new by construction. A verbatim diff against prior-quarter text could not run. Ask: rotation at AGM or resignation? Is there a predecessor resignation letter or Reg 30 filing? |
| A3-06 | F6 | R679-R682, R728, R755, R756, R814, R815 | l.474-478 | "including Rs 1,246 million (31 March 2026: Rs 585 million) of pre-operative costs as management is of the view the same is eligible for capitalisation" | FORWARD-SIGNAL | The note gives no commissioning or capitalisation date for the USA biologics site. Pre-operative cost rose 585 to 1,246, which is +661 (+113%) in six months. That 661 exceeds consolidated H1 PBT of 278 (l.90). If expensed, H1 PBT would be -383 (computed). Pre-op is 25.6% of the 4,876 site CWIP (computed). Capitalisation rests on a management view. On commissioning, 4,876 moves to PPE and starts depreciating. If the site is delayed, the 1,246 of pre-op is the first write-off candidate (checklist T4). |
| A3-07 | F7 | R729, R711, R757, R819, R683-R684 | l.481, l.484-485 | "would continue to assess the accounting implications basis such developments/ guidance as may be needed" | AMBIGUOUS | This is a legal-cover hedge on the New Labour Codes. FY26 already took 463m (consolidated) and 429m (standalone) in exceptional items "based on the best information" (l.481). Rules are not final, so a further gratuity or leave charge is possible. The direction is uncertain, so A3 leans bear. Ask whether a second-round estimate exists. No hedge on revenue lumpiness or customer concentration appears in the notes. |
| A3-08 | F8 | R085-R102, R420-R437, R079-R084, R414-R419 | l.94, l.285 | stand "Total tax expense 203 (79) 180 124 282 903" | AMBIGUOUS | Standalone ETR (computed): Q2 FY27 29.4%, Q1 FY27 a credit at 79% of the loss, Q2 FY26 21.4%, H1 FY27 21.0%, FY26 22.8%. Consolidated: Q2 FY27 31.5%, H1 FY27 16.5%, FY26 22.9%. Statutory rate is 25.17%. Quarterly swings net out in H1, but full-period ETRs run 2-9 pp below statutory. Reading 1: a durable tax benefit (e.g. a unit-level deduction) with a sunset date. That means a future ETR step-up. Reading 2: timing only. Ask for the driver and its expiry. No "tax adjustments relating to earlier years" line exists in either statement. |
| A3-09 | F8 | R091-R096 vs R426-R431; R182-R183; R184-R185; R288; R272 | l.93, l.284, l.148, l.225, l.216 | cons "Deferred tax 54 (103) 4 (49) (78) 72" vs stand "109 (79) 50 30 (6) 222" | FORWARD-SIGNAL | Subsidiaries book persistent deferred-tax credits (cons minus stand, computed): FY26 -150, H1 FY26 -72, Q1 FY27 -24, Q2 FY27 -55, H1 FY27 -79. These are DTA recognitions on subsidiary losses. The group H1 DT credit of 49 on PBT of 278 is a 1,763 bps ETR shield. The subsidiary credit alone is 2,842 bps (computed). Recognition relies on future subsidiary profits, mainly the US site. If the site is delayed, the DTA is at risk of derecognition and ETR steps up. Subsidiary current tax fell from 117 (H1 FY26) to 1 (H1 FY27), which corroborates A3-04. Income tax assets rose 1,088 to 1,548 (taxes paid 525 vs current tax 95), so refund claims are building. |
| A3-10 | F9 | R055-R060, R121-R126, R266-R267, R178-R179, R200-R201, R218-R219, R236-R237 | l.86, l.99, l.213 | "Foreign exchange fluctuation loss, net 614 501 118 1,115 166 609" | FORWARD-SIGNAL | H1 FY27 FX loss of 1,115 is 183% of full FY26 (609). The cash-flow add-back shows an unrealised FX gain of (36) (l.213), so the H1 loss is realised. [INFERENCE] This fits FY26 hedge losses parked in OCI (B(i) -2,679, l.99) now recycling to P&L as hedges settle (OCI B(i) +620 in H1 FY27). Net derivative liability is 965 at Sep-26, down from 1,247 at Mar-26 (computed: 1,043+196-248-26). Further realised FX losses are likely unless the rupee moves. The reported FX loss alone cut Q2 EBITDA margin from 25.1% to 17.7% (computed). Actuarial OCI (A)(i) is small: Q2 (23) against FY26 (63). The literal single-quarter actuarial trigger did not fire. Verify hedge reserve and maturity profile at the Annual Report. |
| A3-11 | F10 | R262-R263, R596-R597, R145-R150, R482-R487, R678, R707, R152-R163, R489-R500 | l.211, l.403, l.471-473 | "Share-based payment expenses (net) 4 216" | AMBIGUOUS | SBP (net) fell to 4 from 216 (-98%). Meanwhile 729,727 shares were allotted on 29-Apr-2026 to the trust for the "Long Term Incentive Performance Share Plan 2023". Reading 1: cumulative charge reversed because performance conditions are no longer expected to vest. That would mean management's own targets are being missed. Reading 2: forfeitures by leavers (see termination benefits, A3-01). Either way H1 PBT carries a non-recurring tailwind of about 212 vs the H1 FY26 run rate (computed). Paid-up 4,029 to 4,037 (+8) traces to note 4. Basic = diluted in every consolidated column. Standalone spread is 0.01 in FY26 only (l.298-299), with no widening. |
| A3-12 | F12 | R166-R167, R503-R504, R679-R680, R228-R229, R314-R315, R292-R293, R626-R627, R176-R177, R513-R514, R290 | l.138, l.179, l.228, l.240, l.420, l.476, l.226 | "(i) Borrowings 672 94" | FORWARD-SIGNAL | Single segment (l.495), so the group balance sheet is the segment balance sheet. The US site is a pre-commissioning build: CWIP 4,047 to 4,876 (+829, +20.5% in six months), with zero site revenue disclosed. Consolidated capex 2,099 vs standalone 1,269 puts about 830 at subsidiaries (computed), matching the +829. The parent put in no new equity: net investment in subsidiaries is flat at 8,339 (computed). Subsidiary short-term borrowings rose 94 to 672 (+578, l.240). The standalone balance sheet has no borrowings line. Group CFO is (1,432). The build runs on short-term debt and group cash. Expect a funding event (intra-group equity or loan, or external debt) until the site earns. |
| A3-13 | F12 | R244-R245, R579-R580, R224-R225, R561-R562, R284-R285, R618-R619 | l.188, l.380, l.223 | "Other current liabilities 4,674 7,808" | AMBIGUOUS | Other current liabilities fell 3,134 (-40%) in six months. Almost all of it is at the parent (standalone -3,127). Other non-current liabilities fell 202, all at the parent. This drives the (3,822) WC outflow. [INFERENCE] For a CRDMO this line usually holds customer advances and contract liabilities; the filing gives no breakdown. Reading 1: advances consumed into revenue without replenishment, meaning weaker new manufacturing orders. Reading 2: settlement of other payables (capex creditors, statutory or employee dues). The separating observation is the contract-liability balance and advance inflow for H1. |
| A3-14 | F12 | R198-R199, R180-R181, R202-R203, R300-R303, R270-R271, R304-R305, R176-R177, R192-R193 | l.157, l.146, l.159, l.232, l.215, l.234 | "(iv) Bank balances other than (iii) above 8 2,021" | AMBIGUOUS | Treasury was reshuffled. Bank balances fell 2,021 to 8. NC other financial assets fell 3,116 to 1,946. Current other financial assets rose 4,247 to 6,765. The cash-flow line names "inter corporate deposits" (l.232). Interest income was 419 but interest received only 222, leaving 197 accrued and uncollected (computed). The H1 FY26 gap was 68. Liquid funds (investments + cash + bank balances) fell 11,780 to 7,305 (computed). Ask: ICD counterparties, any group or related-party placement (T6), maturity, and the accrued-interest collection date. |
| A3-15 | F14 | R712 vs R714/R732; R595 vs R260; R797-R798; R216-R221 | l.491, l.508, l.553, l.402, l.210, l.171-173, l.376, l.331, l.204 | "Syngene Manufacturing Limited (SMSL)" | NEUTRAL-FACT | (a) Note 8 names "Syngene Manufacturing Limited (SMSL)" (l.491). Note 2 and the auditor name "Syngene Manufacturing Solutions Limited" (l.508, l.553). (b) The same (7) is labelled "Provision for doubtful advances to supplier" in the standalone cash flow (l.402) and "Advances to suppliers written off" in the consolidated (l.210). The negative sign on an add-back implies a reversal. (c) Consolidated NC liabilities start at "(ii)" and carry two "(iii)" labels (l.171-173). Standalone shows "(iII)" (l.376). (d) Standalone CWIP carries "[refer note 5]" (l.331), but note 5 describes a subsidiary's asset. (e) Six-month cash flows open with "Profit for the year" (l.204, l.396). Note 1 says "limited review" (l.502), which agrees with the SRE 2410 letters, so audit-vs-review wording is consistent. Each item is immaterial. Together they are a governance data point in a new auditor's first review. |
| A3-16 | F15 | R714, R731, R732, R811, R712, R760-R763, R730, R166-R167, R503-R504, R679-R680 | l.490-494, l.508, l.553, l.138, l.331 | "Syngene Manufacturing Solutions Limited (In the process of liquidation from 15 June 2026)" | AMBIGUOUS | Relationship change: wholly owned subsidiary moved to voluntary liquidation (board 18-May-2026, shareholders 15-Jun-2026). It was "ongoing" at 30-Sep-2026 (l.493). Deconsolidation at completion; any gain or loss lands in exceptional items. A second computed point: consolidated minus standalone CWIP is 5,848, which exceeds note 5's US-site CWIP of 4,876 by 972 (Mar-26: 998). About Rs 1bn of CWIP sits in a subsidiary other than the US site project. Ask which entity holds it, and whether any of it is in SMSL. If so, what happens to it on liquidation? No prior-quarter list, so additions, deletions and renames could not be diffed. Entities listed: 5 (l.504-508, l.549-554). |

### 2.1 F2 decomposition table (all computed from filed lines; cons minus stand = subsidiaries net of eliminations)

| Period | Rev cons | Rev stand | Rev gap | EBITDA cons* | EBITDA stand* | EBITDA gap | PAT cons | PAT stand | PAT gap | PAT gap % of stand PAT |
|---|---|---|---|---|---|---|---|---|---|---|
| Q2 FY27 | 8,327 | 7,779 | 548 | 1,474 | 1,474 | 0 | 322 | 487 | -165 | -33.9% |
| Q1 FY27 | 7,360 | 6,630 | 730 | 908 | 784 | 124 | (90) | (21) | -69 | n.m. (stand loss) |
| Q2 FY26 | 9,106 | 8,301 | 805 | 1,995 | 1,775 | 220 | 671 | 662 | +9 | +1.4% |
| H1 FY27 | 15,687 | 14,409 | 1,278 | 2,382 | 2,258 | 124 | 232 | 466 | -234 | -50.2% |
| H1 FY26 | 17,851 | 16,294 | 1,557 | 4,059 | 3,456 | 603 | 1,538 | 1,402 | +136 | +9.7% |
| FY26 | 37,387 | 34,238 | 3,149 | 9,185 | 8,146 | 1,039 | 3,167 | 3,049 | +118 | +3.9% |

*EBITDA computed = PBT before exceptional + finance costs + D&A - other income (FX loss left inside). Ex-FX consolidated EBITDA: Q2 FY27 2,088 (25.1%), H1 FY27 3,497 (22.3%), Q2 FY26 2,113 (23.2%), FY26 9,794 (26.2%). Reported-basis consolidated margin: Q2 FY27 17.7%, H1 FY27 15.2%, Q2 FY26 21.9%, FY26 24.6%.
Eliminations visible: consolidated other expenses run below standalone (Q2 FY27 -71, Q1 -180, Q2 FY26 -187, FY26 -878; l.85 vs l.276). This points to intra-group service fees paid by the parent. The Q2 FY27 elimination is the smallest in the series.
No JV or associate line exists, so the full gap is subsidiaries plus eliminations.

## 2. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing lines | FINDING | 15 ZERO_STANDING rows read. Exceptional line now live three periods (A3-01). NC provisions to nil (A3-02). New external Rs 25m equity investment (A3-03). Rest: bad debts nil vs 278 prior (l.209), interest on IT refund 51 new (l.216), standalone Q1 current tax nil (l.283), standalone interest paid nil (l.434), l.290 row column unresolved (no inference). |
| F2 Standalone vs consolidated | FINDING | PAT-gap swing 35.3 pp (Q2) and 59.9 pp (H1) of standalone PAT, above the 5 pp trigger (A3-04, table 2.1). |
| F3 Shell-entity detection | PASS | Subsidiaries carry real cost lines in Q2: materials 158, employee 447, D&A 166, finance 59 (computed gaps). The aggregate is not a shell. FG/WIP inventory change is near-identical cons vs stand ((44) vs (42), l.81/l.272), so subsidiaries hold almost no FG/WIP. SMSL alone cannot be isolated. No going-concern EoM exists to reconcile (l.555, l.612). |
| F4 Unaudited contribution ratio | PASS | Neither review report has an Other Matter on component auditors or unreviewed subsidiaries. All 5 entities are within the reviewer's scope (l.549-554). Unreviewed share of PAT disclosed: 0%. Predecessor reliance on comparatives is covered at F5. |
| F5 Going concern / EoM scope | FINDING | No EoM or going-concern language. Auditor changed after Q1 FY27; new predecessor Other Matter paragraph (A3-05). The prior-quarter verbatim diff could not run because no prior extract exists. |
| F6 Forward-commitment phrases | FINDING | Lexicon hits: "subject to" l.493, "In the process of" l.508, "Board of Directors ... approved" l.471 and l.490, "continues to monitor" l.484, "will also be made available" l.48, "commenced" l.46 (meeting time, not a commitment). The key gap is that note 5 has no capitalisation date (A3-06). Register in section 3. |
| F7 Hedge phrases | FINDING | Labour Code hedge l.484-485 (A3-07). Also "based on the best information" l.481, "management is of the view" l.477 (at A3-06), "subject to" l.493 (SMSL). No customer-concentration or lumpiness hedge. |
| F8 Tax forensics | FINDING | ETR below statutory in full periods with quarterly swings (A3-08). Persistent subsidiary DT credits, a 1,763 bps group ETR shield in H1 (A3-09). No earlier-years tax adjustment line. |
| F9 OCI forensics | FINDING | Actuarial trigger not met ((23) vs (63)). FX: realised loss of 1,115 in H1 and net derivative liability of 965 remaining (A3-10). Verify at AR. |
| F10 Share count and dilution | FINDING | Paid-up +8 traced to note 4. No basic/diluted spread widening. SBP collapse 216 to 4 under the performance share plan (A3-11). |
| F11 Reserves and net worth tie-out | PASS | Cons 4,037+44,551=48,588 (l.165-167). Stand 4,037+43,271=47,308 (l.358-360). Mar-26 ties to the P&L reserves line (l.104 = l.166, l.296 = l.359). Other equity roll-forward (opening + TCI - dividend + SBP) agrees within Rs 2m rounding. No third-party net-worth figure in context to reconcile. |
| F12 Segment forensics | FINDING | Single segment (l.495). Applied to the group balance sheet: US site build funded by subsidiary short-term debt (A3-12); other current liabilities unwind (A3-13); treasury reshuffle into ICDs with accrued interest uncollected (A3-14). |
| F13 Board outcome beyond results | PASS | Letter l.39-44 approves only the results ("inter-alia" with no other item named). No AR, AGM, record date, dividend, director term, auditor, ESOP or fund-raising item. A CFO exit filed in a separate Reg 30 letter the same day is in the orchestrator checklist (line 31), not in this document. A3 has not verified it; A4 carries it. Signature sequence is proper: board ended 18:30, auditor signed 18:32-18:33 after approval, Chairperson 18:24 during the meeting. |
| F14 Note drafting inconsistencies | FINDING | Five drafting items (A3-15). Note 1 and the auditor letters agree on "limited review". |
| F15 Entity list diffs | FINDING | SMSL moved to liquidation (A3-16). About Rs 1bn of non-US-site subsidiary CWIP is unexplained. Prior-quarter diff not possible. |
| F16 Presentation: dropped / reframed | N.A. | Results filing, not a presentation. |
| F17 Concall: silence audit | N.A. | Results filing, not a transcript. Checklist items are mapped to filing evidence in section 4 for A4 (informational, not a silence audit). |

Status line: F1 FINDING | F2 FINDING | F3 PASS | F4 PASS | F5 FINDING | F6 FINDING | F7 FINDING | F8 FINDING | F9 FINDING | F10 FINDING | F11 PASS | F12 FINDING | F13 PASS | F14 FINDING | F15 FINDING | F16 N.A. | F17 N.A.

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note/line ref | status word |
|---|---|---|---|
| Voluntary liquidation of Syngene Manufacturing Solutions Limited (SMSL), subject to statutory, regulatory and legal formalities | Not dated. Board 18-May-2026, shareholders 15-Jun-2026 | Note 8, l.490-494; note 2 l.508; auditor l.553 | underway ("ongoing"). Moved from approved (Q1 FY27) to ongoing (Q2 FY27), dated inside the note; no prior text to diff |
| Capitalisation of USA biologics site CWIP Rs 4,876m, incl. pre-operative Rs 1,246m, "eligible for capitalisation" per management | NOT STATED (no commissioning date; checklist T4 watches Mar-2027) | Note 5, l.474-478 | underway (accumulating; +829 CWIP, +661 pre-op in H1) |
| Continue to monitor New Labour Codes and assess accounting implications | Not dated (on notification of rules / guidance) | Note 6, l.484-485 | underway ("continues to monitor") |
| Termination benefits extended under the approved policy, shown as exceptional | Recurring: FY26, Q1 FY27, Q2 FY27 | Note 7, l.486-489 | underway (third consecutive period) |
| Allotment of 729,727 shares to Syngene Employees Welfare Trust for LTIP Performance Share Plan 2023 | 29-Apr-2026 | Note 4, l.471-473; paid-up l.103 | completed (paid-up 4,029 to 4,037) |
| Post results on company website | 27-Oct-2026 | l.48-49 | initiated ("will also be made available") |

## 4. CHECKLIST CROSS-REFERENCE FOR A4 (informational; F17 is N.A. on a results filing)

| Checklist item | What this filing shows | Line |
|---|---|---|
| Q2 consolidated revenue path (745 bear / ~790 base / ~840 bull / ~930 guidance, Rs cr) | 8,327m = Rs 832.7 cr: above base, below bull and guidance path | l.76 |
| R2 / T1 research revenue; CDMO share | NOT DISCLOSED (single segment) | l.495 |
| Bayview figure in CWIP note; T4 | Yes: 4,876m incl. 1,246m pre-op. No operational date. No impairment or write-down disclosed | l.476-477 |
| T3 H1 CFO < 70% of operating EBITDA | CFO (1,432) vs computed EBITDA 2,382 reported / 3,497 ex-FX. On filing numbers the condition is met | l.226 |
| T5 EBITDA margin < 25% | H1 computed 15.2% reported / 22.3% ex-FX (T5 is a full-year test) | l.76-88 |
| CWIP Rs 1,046 cr at Mar-2026 (checklist) | Filing shows 10,404m = Rs 1,040.4 cr: 0.5% gap; checklist figure to recheck | l.138 |
| Rs 277 mn write-off counterparty | Bad debts written off 278 in H1 FY26; nil H1 FY27; counterparty not named | l.209 |
| SSSL (T10) | Still a consolidated subsidiary; no OCRPS or terms disclosure | l.507, l.551 |
| Zoetis, client concentration, Unit 3 litres, Biocon stake (T7), BMS (T8) | Not in this filing | - |
| CFO exit (Reg 30, 27-Oct-2026) | Not in this filing | - |

## 5. A4 HAND-OFF

FORWARD-SIGNAL (convert to management questions): A3-01, A3-04, A3-06, A3-09, A3-10, A3-12.
AMBIGUOUS (convert to management questions): A3-02, A3-03, A3-05, A3-07, A3-08, A3-11, A3-13, A3-14, A3-16.
NEUTRAL-FACT: A3-15.

```yaml
stage: A3-forensics
company: "SYNGENE"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/syngene-q2fy27/work/forensics_syngene_q2fy27_results.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "l.89, l.486-489", classification: "FORWARD-SIGNAL", implication: "Termination benefits 303/135/67 held in exceptional items three periods running; note cites 'frequency'; recurring cost below PBT-before-exceptional; more charges likely until programme end stated"}
  - {id: "A3-02", check: "F1", line: "l.174, l.186", classification: "AMBIGUOUS", implication: "NC provisions 180 to nil, total provisions down 492 in H1; cash settlement or funding vs reclassification; ask for roll-forward"}
  - {id: "A3-03", check: "F1", line: "l.231, l.423", classification: "AMBIGUOUS", implication: "New Rs 25m equity investment in both standalone and consolidated cash flows, so investee is outside the group; identity undisclosed; ask, T6 link"}
  - {id: "A3-04", check: "F2", line: "l.76, l.88, l.95, l.267, l.279, l.286", classification: "FORWARD-SIGNAL", implication: "Subsidiary PAT gap +1.4% to -33.9% of standalone PAT YoY (H1 +9.7% to -50.2%); subsidiary EBITDA 220 to 0; revenue 805 to 548; worse once US site depreciates"}
  - {id: "A3-05", check: "F5", line: "l.563-568, l.618-623", classification: "AMBIGUOUS", implication: "Auditor changed after Q1 FY27 review (29-Jul-2026); Q2 is S.R. Batliboi's first review; predecessor unnamed; no EoM; rotation vs resignation unstated; prior-quarter diff could not run"}
  - {id: "A3-06", check: "F6", line: "l.474-478", classification: "FORWARD-SIGNAL", implication: "US site CWIP 4,876 incl pre-op 1,246 (+661 in H1, above H1 PBT 278); capitalised on management view; no commissioning date; write-off candidate if delayed (T4)"}
  - {id: "A3-07", check: "F7", line: "l.481, l.484-485", classification: "AMBIGUOUS", implication: "Labour Code hedge: further gratuity or leave charge possible after 463m FY26 exceptional; ask for second-round estimate"}
  - {id: "A3-08", check: "F8", line: "l.94, l.285", classification: "AMBIGUOUS", implication: "Full-period ETRs 16.5-22.9% below 25.17% statutory; Q1 credit 79% then Q2 29.4% standalone; durable benefit with sunset vs timing; ask driver and expiry"}
  - {id: "A3-09", check: "F8", line: "l.93, l.284, l.148", classification: "FORWARD-SIGNAL", implication: "Subsidiaries book persistent DT credits on losses (H1 -79, FY26 -150); 1,763 bps group ETR shield in H1; DTA rests on US-site profits; derecognition risk if delayed; income tax assets 1,088 to 1,548"}
  - {id: "A3-10", check: "F9", line: "l.86, l.99, l.213", classification: "FORWARD-SIGNAL", implication: "H1 FX loss 1,115 = 183% of FY26, realised (unrealised line is a gain); FY26 OCI hedge losses recycling [INFERENCE]; net derivative liability 965 left; drag likely continues; verify hedge reserve at AR"}
  - {id: "A3-11", check: "F10", line: "l.211, l.403, l.471-473", classification: "AMBIGUOUS", implication: "SBP net 4 vs 216 under Performance Share Plan 2023; vesting conditions failing vs leaver forfeitures; ~212m non-recurring H1 PBT tailwind; no EPS spread widening"}
  - {id: "A3-12", check: "F12", line: "l.138, l.179, l.240, l.476", classification: "FORWARD-SIGNAL", implication: "US build +829 CWIP funded by subsidiary short-term debt 94 to 672 and group cash; parent net investment in subsidiaries flat 8,339; group CFO -1,432; funding event likely before site earns"}
  - {id: "A3-13", check: "F12", line: "l.188, l.380, l.223", classification: "AMBIGUOUS", implication: "Other current liabilities -3,134 (-40%), all at parent; if customer advances, weaker new manufacturing orders; else payables settlement; ask contract-liability breakdown"}
  - {id: "A3-14", check: "F12", line: "l.157, l.146, l.159, l.232, l.215, l.234", classification: "AMBIGUOUS", implication: "Bank balances 2,021 to 8, current other financial assets 4,247 to 6,765 via ICDs; interest accrued not received 197; liquid funds 11,780 to 7,305; ask ICD counterparties (T6)"}
  - {id: "A3-15", check: "F14", line: "l.491, l.508, l.402, l.210, l.171-173, l.376, l.331, l.204", classification: "NEUTRAL-FACT", implication: "SMSL name mismatch; provision vs write-off label on same (7); BS numbering errors; note 5 marker on standalone CWIP; 'Profit for the year' on 6M cash flow; cumulative governance data point in new auditor's first review"}
  - {id: "A3-16", check: "F15", line: "l.490-494, l.508, l.553, l.138, l.331", classification: "AMBIGUOUS", implication: "SMSL moved to voluntary liquidation from 15-Jun-2026, ongoing; deconsolidation effect to exceptional; ~972m of subsidiary CWIP outside the US site unexplained (computed); prior-list diff not possible"}
forward_signals: ["A3-01", "A3-04", "A3-06", "A3-09", "A3-10", "A3-12"]
ambiguous: ["A3-02", "A3-03", "A3-05", "A3-07", "A3-08", "A3-11", "A3-13", "A3-14", "A3-16"]
commitments:
  - {commitment: "Voluntary liquidation of SMSL subject to statutory, regulatory and legal formalities", implied_date: "not dated; approved 18-May-2026 board, 15-Jun-2026 shareholders", ref: "Note 8 l.490-494", status_word: "underway"}
  - {commitment: "Capitalise USA biologics site CWIP Rs 4,876m incl pre-op Rs 1,246m", implied_date: "NOT STATED", ref: "Note 5 l.474-478", status_word: "underway"}
  - {commitment: "Monitor New Labour Codes and assess accounting implications", implied_date: "not dated", ref: "Note 6 l.484-485", status_word: "underway"}
  - {commitment: "Termination benefits under approved policy, shown as exceptional", implied_date: "recurring FY26, Q1 FY27, Q2 FY27", ref: "Note 7 l.486-489", status_word: "underway"}
  - {commitment: "Allot 729,727 shares to Syngene Employees Welfare Trust for LTIP 2023", implied_date: "29-Apr-2026", ref: "Note 4 l.471-473", status_word: "completed"}
  - {commitment: "Post results on company website", implied_date: "27-Oct-2026", ref: "l.48-49", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Q2 reads better than it is. Three items flatter consolidated PBT: Rs 661m of US-site pre-operative cost capitalised in H1 (above H1 PBT of 278; note 5 gives no commissioning date), share-based payment down to 4 from 216, and recurring termination benefits kept in exceptional items. Subsidiaries swung from +9 to -165 PAT YoY with EBITDA at zero, before any US-site depreciation. They book deferred-tax credits on losses and fund capex with short-term debt (672) while the parent put in no new equity. The H1 FX loss of 1,115 is realised and a net derivative liability of 965 remains, so the drag likely continues [INFERENCE]. Other current liabilities fell 3,134; if these are customer advances, order inflow is weak (two readings). This is the new auditor's first review; the predecessor is unnamed; the orchestrator checklist reports a same-day CFO exit not in this document. No prior-quarter text existed, so F5 and F15 ran on internal evidence only. On filing numbers T3 is met: H1 CFO is -1,432 against computed EBITDA of 2,382."
```
