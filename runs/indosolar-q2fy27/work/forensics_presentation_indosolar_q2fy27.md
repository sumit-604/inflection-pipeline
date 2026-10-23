# A3 FORENSIC NOTES: INDOSOLAR Q2 FY27 (doctype: presentation; Reg 30 press release dated 21-Oct-2026, 3 pages)

Agent: A3 forensic notes | Model: claude-opus-5-5 | Run date: 2026-10-23
Inputs read: A1 structured (R001-R084), A1 fulltext (162 lines; page-2 table read ONLY at repaired lines 121-128, raw lines 84-95 not used for cell values), A2 ledger (84 IDs).
Cross-document reference (reconciliation only): results-filing A1 structured file (Rs Lakhs; converted x0.01 to Rs Crores below). It was used only to test whether press-release numbers and claims reconcile to the filed statement. The full F1-F15 run on the filed statement belongs to the results-doctype A3.
Prior-quarter fulltext: none (first run for this name). Notion monitoring checklist: no Notion checklist passed. No companies/INDOSOLAR.md, no spear on record.
Source PDF and inputs/ were not opened.

## 0. LEDGER RECONCILIATION (Rule 2)

Rows in ledger: 84 (R001-R084). Rows read at cited fulltext line: 84. ledger_reconciled_pct = 100.

Anchor notes (A1 extraction defects, not company findings; no value is affected):
- R048 (www.indosolar.co.in) cites line 26. Fulltext line 26 is blank. The website text sits at line 44: "available on the website of the Company i.e. www.indosolar.co.in".
- R050 ("a WAAREE group company") cites line 19. Fulltext line 19 reads "a itA/s'U.; group company" (garbled letterhead). The clean text is at line 72: "a WAAREE group company".
- R059 address-block anchor "28-30,65-67" is approximate. The addresses sit at lines 25-28 and 64-67.

## 1. PRESS RELEASE TO FILED STATEMENT RECONCILIATION (cross-document, Rs Crores)

| Item | Press release (line) | Filed statement (results ID, Rs Lakhs -> Cr) | Ties? |
|---|---|---|---|
| Revenue Q2 FY27 | 155.59 (L123) | Goods 15,277.09 (R001) + Services 281.54 (R007) = 15,558.63 -> 155.59 | yes |
| Revenue Q2 FY26 | 202.55 (L123) | 17,118.31 (R003) + 3,136.48 (R009) = 20,254.79 -> 202.55 | yes |
| Revenue H1 FY27 | 223.95 (L123) | 16,674.51 (R004) + 5,720.26 (R010) = 22,394.77 -> 223.95 | yes |
| Revenue H1 FY26 | 397.22 (L123) | 34,591.14 (R005) + 5,131.22 (R011) = 39,722.36 -> 397.22 | yes |
| Operating EBITDA Q2 FY27 | 14.82 (L124) | PBT 671.02 + fin 5.88 + D&A 962.93 - OI 158.05 = 1,481.78 -> 14.82 | yes |
| Operating EBITDA Q2 FY26 | 70.73 (L124) | 6,113.68 + 38.47 + 921.70 - 1.11 = 7,072.74 -> 70.73 | yes |
| Operating EBITDA H1 FY27 | 63.28 (L124) | 5,418.04 + 13.56 + 1,893.23 - 996.75 = 6,328.08 -> 63.28 | yes |
| Operating EBITDA H1 FY26 | 134.29 (L124) | 11,629.43 + 100.90 + 1,832.13 - 133.17 = 13,429.29 -> 134.29 | yes |
| PAT Q2 FY27 / Q2 FY26 / H1 FY27 / H1 FY26 | 5.02 / 46.34 / 41.64 / 163.13 (L126) | 501.85 (R103) / 4,633.76 (R105) / 4,163.78 (R106) / 16,313.02 (R107) | yes |
| YoY cells (6) | L123, L124, L126 | recomputed from lakh values | yes, all six |
| EBITDA margin (4) | 9.52 / 34.92 / 28.26 / 33.81% (L125) | Operating EBITDA / Revenue from operations | yes |
| PAT margin (4) | 3.19 / 22.88 / 17.80 / 40.93% (L127) | PAT / TOTAL INCOME (R019, R021, R022, R023), not revenue | ties only on total-income basis; see A3-08 |
| Release timing | signed 20:40:15 IST (L53) | board met 16:30-17:30 IST, 21-Oct-2026 (results R278, R279, R340) | release follows board close; no pre-release |

Result: every press-release figure ties to the filed standalone statement. One undisclosed denominator switch (PAT margin). "Operating EBITDA" is undefined in the release but reconstructs exactly (A3-07).

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F6 | R065, R052, R055 | 117 | "The proposed amalgamation with Waaree Energies marks an important strategic milestone" | FORWARD-SIGNAL | Release gives no date, swap ratio, appointed date or approval path. Filed Note 4 (results R374, R351, R337): board approved the draft scheme on 23-Sep-2026 and "Upon the Scheme becoming effective, Indosolar Limited shall stand dissolved without being wound up". The listed equity has a terminal event. Its value converts at a swap ratio that neither document states. Any standalone transition thesis is capped at scheme effectiveness. |
| A3-02 | F6 | R061, R053 | 104-105 | "strategic transition of a major share of its volumes from tolling to owned manufacturing" | FORWARD-SIGNAL | "Major share" carries no %, MW or date. Filed statement confirms the switch landed in Q2: Sale of Services Rs 54.39 Cr Q1 FY27 -> Rs 2.82 Cr Q2 (results R008, R007); Sale of Goods Rs 13.97 Cr -> Rs 152.77 Cr (R002, R001). Owned manufacturing carries material cost and inventory: Inventories Rs 21.08 Cr (31-Mar-26) -> Rs 221.97 Cr (30-Sep-26) (R170, R169). Margin % baseline and working-capital need both reset. |
| A3-03 | F16 | R037, R039 | 100-101 | "Module sold stood at 98 MW in Q2FY27 as compared to 249 MW in Q2FY26" | AMBIGUOUS | Produced 148 MW, sold 98 MW: 50 MW unsold in the quarter. Filed Changes in Inventories Q2 FY27 = (10,591.83) lakhs, a Rs 105.92 Cr build (results R031). Reading 1: stock built against H2 orders. Reading 2: sell-through weakness. Separating observation: Q3 FY27 MW sold vs produced and inventory level. With "elevated raw material costs" (line 104), a module-price fall puts NRV write-down risk on this stock. |
| A3-04 | F16 | R041, R054, R037 | 104, 133 | "lower capacity utilisation across the solar manufacturing industry" / "capacity of 1.3 GW module manufacturing" | AMBIGUOUS | Release attributes low utilisation to the industry and gives no company figure. Derived: 148 MW / (1,300 MW / 4) = 45.5% for Q2 FY27, IF 1.3 GW is annual nameplate (basis not stated). Q2 FY26 capacity NOT FOUND in this document, so no YoY utilisation. Fixed-cost absorption is the operating-leverage lever for H2. |
| A3-05 | F16 | R019, R029, R073-R076 | 125 | "EBITDA Margin | 9.52% | 34.92% | (blank) | 28.26%" | FORWARD-SIGNAL | Release shows YoY and H1 only; no QoQ column, though the filed statement carries Q1 FY27. Q1 FY27 PAT Rs 36.62 Cr (results R104) -> Q2 Rs 5.02 Cr = -86.3% QoQ. Q1 Operating EBITDA (derived, H1 63.28 - Q2 14.82) = Rs 48.46 Cr on Rs 68.36 Cr revenue = 70.9% margin, a tolling-heavy quarter. H1 margin 28.26% is Q1-weighted. Q2's 9.52% is the owned-manufacturing exit run rate, not H1. |
| A3-06 | F16 | R002, R003, R031-R034, R039, R040 | 97-98, 101 | "Operating EBITDA stood at Rs. 14.82 crores in Q2FY27 compared to Rs. 70.73 crores in Q2FY26" | AMBIGUOUS | Derived: revenue per MW sold Rs 0.81 Cr (202.55/249) -> Rs 1.59 Cr (155.59/98), consistent with the volume mix moving from tolled to owned. Operating EBITDA per MW sold Rs 28.4 lakh (70.73/249) -> Rs 15.1 lakh (14.82/98), -47%. Owned manufacturing should RAISE EBITDA per MW (module margin plus conversion). Reading 1: spread compression and under-absorption (line 104 causes). Reading 2: transition one-offs in a first owned quarter. Separating observation: Q3 FY27 EBITDA per MW once inventory clears. Lean bear: the fall is not only a revenue gross-up artifact. |
| A3-07 | F16 | R081, R003, R011 | 79 | "Operating EBITDA for the quarter stood at  14.82 Crores" | NEUTRAL-FACT | No definition in the release (R081 FOOTNOTE_UNRESOLVED). It reconstructs to the lakh in all four periods as PBT + finance costs + D&A - other income. It excludes other income, which in H1 FY27 includes a government grant of Rs 6.69 Cr (results R221) and interest income Rs 2.51 Cr (R227). Conservative choice. Track for definition drift in later releases. |
| A3-08 | F14 | R027-R030, R017-R020 | 127 | "PAT Margin | 3.19% | 22.88% | (blank) | 17.80% | 40.93%" | NEUTRAL-FACT | PAT margin uses total income as denominator; EBITDA margin (line 125) uses revenue from operations. Not disclosed. On revenue basis PAT margin would read 3.23% / 22.88% / 18.59% / 41.07%. Direction understates, so no upward bias. Drafting inconsistency only. Minor: plant "situated at Noida" (line 133) vs factory "Greater Noida" (line 67). |
| A3-09 | F17 | R063, R064, R065, R061 | 111-112 | "positioning the business for long-term growth" | AMBIGUOUS | CEO speaks of standalone long-term growth and a "future-ready manufacturing platform" (lines 114-115) for an entity the filed Note 4 says will dissolve on scheme effectiveness. Release is silent on the items in Section 5 table. One quarter of silence (first run; prior count NOT FOUND). Not yet a confirmatory negative; A4 converts to questions. |

FORWARD-SIGNAL: A3-01, A3-02, A3-05. AMBIGUOUS (to A4 as management questions): A3-03, A3-04, A3-06, A3-09. NEUTRAL-FACT: A3-07, A3-08.

Questions A4 should form (lean-bear phrasing suggested):
1. (A3-01) What are the swap ratio, appointed date, valuation report and approval timeline (exchanges, SEBI, NCLT, shareholders) for the scheme approved on 23-Sep-2026?
2. (A3-02) What share of Q2 FY27 MW was owned vs tolled? What mix is targeted for H2, and how is the working-capital build funded?
3. (A3-03) Is the 50 MW gap between production and sales backed by orders? What is the inventory carrying value per MW against current module prices?
4. (A3-04) What utilisation did the Noida plant run in Q2 FY27 against what nameplate basis?
5. (A3-06) What was EBITDA per MW on owned modules vs tolled modules in Q2 FY27, and what drove the 47% fall in EBITDA per MW sold?
6. (A3-09) Why does the release discuss standalone long-term growth while the scheme dissolves the company?

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Press release carries no statutory template. A2 ZERO_STANDING count 0 (ledger section 7). |
| F2 Standalone vs consolidated | N.A. | Release is standalone only (line 41). Filed Note 5 states no subsidiary/associate/JV (results R375). |
| F3 Shell-entity detection | N.A. | No consolidated cost lines in a press release; no subsidiaries. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters in a press release. |
| F5 Going concern / EoM scope | N.A. | No auditor paragraph in a press release; no prior quarter to diff. |
| F6 Forward-commitment phrases | FINDING | Lexicon scan of lines 1-162: zero literal hits ("will" at line 154 is the safe-harbour word list). Non-lexicon commitments found and registered: A3-01, A3-02, plus intent rows R063, R064, R066. |
| F7 Hedge phrases | PASS | Lexicon scan of lines 1-162: no hit on "may sometimes", "could have an effect", "no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour". Safe harbour (lines 147-162) is generic boilerplate. |
| F8 Tax forensics | N.A. | Release carries no tax line. Tax runs in the results-doctype A3. |
| F9 OCI forensics | N.A. | Release carries no OCI line. |
| F10 Share count and dilution | N.A. | Release carries no EPS, share count or paid-up capital. |
| F11 Reserves and net worth tie-out | N.A. | Release carries no net worth or reserves figure. |
| F12 Segment forensics | N.A. | Release carries no segment data. |
| F13 Board outcome beyond results | N.A. | Release reports no board outcome. The scheme board date (23-Sep-2026) sits in the filed results, not the release; handled under F6. |
| F14 Drafting inconsistencies | FINDING | A3-08: undisclosed PAT margin denominator switch; Noida vs Greater Noida. Release timing after board close checked, nothing. |
| F15 Entity list diffs | N.A. | No consolidation list in a press release; no prior quarter. Pending amalgamation (R052 ENTITY_CHANGE candidate) handled under F6 (A3-01). |
| F16 Dropped and reframed disclosures | FINDING | No prior deck, so no quarter-on-quarter dropped-metric diff is possible. In-document reframes found: no QoQ column (A3-05), no own utilisation (A3-04), sold below produced unexplained (A3-03), undefined Operating EBITDA (A3-07), EBITDA per MW fall masked by margin framing (A3-06). |
| F17 Silence audit | FINDING | Run per task message against the F6 register and the general set; no Notion checklist passed. Strictly a concall check; this release is a one-way document, so silence here is one quarter and weak. A3-09. |

## 4. COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Amalgamation of Indosolar into Waaree Energies (release: "proposed"; filed Note 4: draft scheme board-approved 23-Sep-2026, Indosolar dissolves on effectiveness) | NOT FOUND (no effective or appointed date in either document) | line 117, R065; results R374, R351, R337 | initiated |
| Transition of a "major share" of volumes from tolling to owned manufacturing | NOT FOUND | lines 104-105, R061 | underway (Q2 revenue 98% sale of goods per results R001, R007) |
| Strengthen manufacturing capabilities, improve operational efficiencies | NOT FOUND | lines 111-112, R063 | none (intent) |
| Build a more efficient, future-ready manufacturing platform | NOT FOUND | lines 114-115, R064 | none (intent) |
| Operational synergies from integration with Waaree's manufacturing ecosystem | NOT FOUND | lines 118-119, R066 | none (expectation) |

No numeric guidance exists in the document (ledger section 4).

## 5. WHAT WAS NOT DISCUSSED (F17 silence table)

| Item | Source of expectation | Addressed in release? | Consecutive quarters of silence |
|---|---|---|---|
| Swap ratio, appointed date, approval timeline of the scheme | F6 commitment A3-01; filed Note 4 | no | 1 (first run) |
| Dissolution of Indosolar on scheme effectiveness | filed Note 4 (results R337) | no | 1 (first run) |
| Owned vs tolled MW split, target mix | F6 commitment A3-02 | no ("major share" only) | 1 (first run) |
| Company capacity utilisation | line 104 cites industry utilisation | no | 1 (first run) |
| 50 MW production over sales; inventory build | lines 100-101 | no | 1 (first run) |
| QoQ comparison vs Q1 FY27 | filed statement carries Q1 column | no | 1 (first run) |
| Other income incl. government grant | filed statement (results R221) | no (excluded from Operating EBITDA, unmentioned) | 1 (first run) |

## 6. YAML BLOCK

```yaml
stage: A3-forensics
company: "INDOSOLAR"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\quarterly-indosolar-q2fy27-2614ff\\runs\\indosolar-q2fy27\\work\\forensics_presentation_indosolar_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F6", line: "117", classification: "FORWARD-SIGNAL", implication: "Amalgamation undated, no swap ratio; filed Note 4 says Indosolar dissolves on effectiveness (board approved draft scheme 23-Sep-2026). Listed equity has a terminal event; value turns on an undisclosed swap ratio."}
  - {id: "A3-02", check: "F6", line: "104-105", classification: "FORWARD-SIGNAL", implication: "Tolling-to-owned shift unquantified; filed statement shows services Rs 54.39 Cr Q1 -> Rs 2.82 Cr Q2, goods Rs 13.97 Cr -> Rs 152.77 Cr, inventory Rs 21.08 Cr -> Rs 221.97 Cr. Margin % baseline and working-capital need reset."}
  - {id: "A3-03", check: "F16", line: "100-101", classification: "AMBIGUOUS", implication: "Produced 148 MW, sold 98 MW; Q2 inventory build Rs 105.92 Cr. Order-backed stock vs sell-through weakness; NRV risk if module prices fall."}
  - {id: "A3-04", check: "F16", line: "104, 133", classification: "AMBIGUOUS", implication: "No company utilisation given; derived 45.5% (148 MW vs 325 MW quarterly at 1.3 GW, nameplate basis unstated). Under-absorption drives H2 operating leverage."}
  - {id: "A3-05", check: "F16", line: "125", classification: "FORWARD-SIGNAL", implication: "No QoQ column; Q1 FY27 PAT Rs 36.62 Cr -> Q2 Rs 5.02 Cr (-86.3%); derived Q1 EBITDA margin 70.9% (tolling). H1 28.26% overstates run rate; Q2 9.52% is the owned-model exit margin."}
  - {id: "A3-06", check: "F16", line: "97-98, 101", classification: "AMBIGUOUS", implication: "Derived EBITDA per MW sold Rs 28.4 lakh -> Rs 15.1 lakh (-47%) while revenue per MW rose Rs 0.81 Cr -> Rs 1.59 Cr. Owned model should raise EBITDA/MW; spread compression vs first-quarter transition costs."}
  - {id: "A3-07", check: "F16", line: "79", classification: "NEUTRAL-FACT", implication: "Operating EBITDA undefined but reconstructs exactly as PBT + finance + D&A - other income; excludes H1 government grant Rs 6.69 Cr. Track for definition drift."}
  - {id: "A3-08", check: "F14", line: "127", classification: "NEUTRAL-FACT", implication: "PAT margin on total income, EBITDA margin on revenue, undisclosed; revenue-basis PAT margin 3.23% / 18.59% for Q2 / H1 FY27. Understates; drafting inconsistency only."}
  - {id: "A3-09", check: "F17", line: "111-112", classification: "AMBIGUOUS", implication: "CEO standalone long-term-growth language vs scheduled dissolution; release silent on swap ratio, mix, utilisation, inventory, QoQ. One quarter of silence (first run)."}
forward_signals: ["A3-01", "A3-02", "A3-05"]
ambiguous: ["A3-03", "A3-04", "A3-06", "A3-09"]
commitments:
  - {commitment: "Amalgamation of Indosolar into Waaree Energies; Indosolar dissolves on effectiveness", implied_date: "NOT FOUND (draft scheme board-approved 23-Sep-2026)", ref: "line 117, R065; results R374/R351/R337", status_word: "initiated"}
  - {commitment: "Transition of a major share of volumes from tolling to owned manufacturing", implied_date: "NOT FOUND", ref: "lines 104-105, R061", status_word: "underway"}
  - {commitment: "Strengthen manufacturing capabilities, improve operational efficiencies", implied_date: "NOT FOUND", ref: "lines 111-112, R063", status_word: "none (intent)"}
  - {commitment: "Build a more efficient, future-ready manufacturing platform", implied_date: "NOT FOUND", ref: "lines 114-115, R064", status_word: "none (intent)"}
  - {commitment: "Operational synergies from integration with Waaree", implied_date: "NOT FOUND", ref: "lines 118-119, R066", status_word: "none (expectation)"}
gate_a3: pass
blank_checks: []
analyst_note: "Every release figure ties to the filed standalone statement to the lakh. Operating EBITDA = PBT + finance + D&A - other income. PAT margin uses total income, not revenue, and understates. The material point is not a number. The release calls the amalgamation a milestone and the CEO speaks of long-term growth, but filed Note 4 says Indosolar dissolves when the scheme takes effect. The listed equity's value then turns on a swap ratio neither document gives. Second, the Q2 fall is not only a tolling-to-owned revenue gross-up. Derived EBITDA per MW sold fell 47% (Rs 28.4 lakh to Rs 15.1 lakh) while revenue per MW doubled; owned manufacturing should raise EBITDA per MW. Third, 50 MW produced but unsold and a Rs 105.92 Cr Q2 inventory build put H2 revenue and NRV risk on module prices. Derived 45.5% utilisation assumes 1.3 GW is annual nameplate. F17 was run per the task message though it is concall-specific; one quarter of silence in a one-way release is weak evidence. A1 anchor defects at R048 and R050 change no value."
```
