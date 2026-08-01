# A3 FORENSIC NOTES — SASKEN Q1 FY27 (Doctype: RESULTS, Reg 33 audited quarterly)

Source extract: `/home/user/inflection-pipeline/runs/sasken-q1fy27/work/extract_results_sasken_q1fy27.txt` (57 pages / 2,092 lines)
Ledger reconciled: 100% (every A2 ledger row read at its cited line before judging).
Units: statutory statements pages 7-15 in **Lakhs** (x0.01 -> Cr); media release / analyst letter pages 16-25 in **Crores** (x1); investor presentation pages 26-57 in **Millions** (x0.1 -> Cr). Every figure below stated in **Rs Cr**, source section named.
Auditor: MSKA & Associates LLP, unmodified opinion both reports; **0 KAM, 0 EOM, 0 going-concern material uncertainty** (A2 confirmed). One step-down subsidiary audited by other auditor (Other Matters para 1). Q4FY26 comparative is an Ind AS 34 balancing figure (Other Matters para 2 / standalone Other Matter).

---

## CHECKLIST SCORECARD (all 17 — no blank; GATE A3)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 Zero-value standing items | **FINDING** | Labour-code exceptional line (l.350-351/653-654) nil in all 3 quarters, only FY26 populated; all-dash inter-segment revenue (l.411). 6 ZERO_STANDING rows read. |
| F2 Standalone vs consolidated | **FINDING** | Standalone PAT 28.86 Cr > consolidated PAT 23.52 Cr; subsidiary net contribution swung +9.26 Cr (Q4) to −5.33 Cr (Q1FY27); NCI −1.34 Cr (l.356/659/373). |
| F3 Shell-entity detection | PASS | Subs carry real cost of materials 89.83 Cr, employees +68.2 Cr, D&A +7.68 Cr over standalone (l.342/344/346 vs 647/649) — genuine operations, not shells; no GC flag to reconcile. |
| F4 Unaudited/other-auditor ratio | **FINDING** | Other-auditor step-down sub: rev 65.44 Cr (19.3% of consol), PAT 0.65 Cr (0.99% net margin), entity **not named** in para (l.285-293). Below 10%-of-PAT threshold but thin margin + unnamed = flagged. |
| F5 Going concern / EoM scope | PASS | Zero EoM / zero going-concern uncertainty (only boilerplate l.208-212, 550-553). Zero KAM is normal for Reg 33 quarterly (SA 701 applies to annual), not a regression from FY26 AR. No prior-quarter para to diff (NO_PRIOR_LEDGER). |
| F6 Forward-commitment mining | **FINDING** | 6 numbered notes are boilerplate, but release/analyst letter carry dateable commitments (freshers, MediaTek ownership, Massive MIMO tapeout, "profitable growth through FY27") — see Commitment Register. |
| F7 Hedge-phrase mining | **FINDING** | New hedges on memory supply/pricing; disclosure that memory-cost **pass-through inflated Product Solutions reported revenue** (l.853-855, 857-860, 948). |
| F8 Tax forensics | **FINDING** | Consol ETR 20.5% vs 25.17% statutory (467 bps below) via 3.60 Cr deferred-tax **credit**; persistent deferred credits (Q1FY27, Q1FY26, FY26) = DTA drawdown / future ETR step-up; disputed tax not disclosed (l.353-355). |
| F9 OCI forensics | PASS | Actuarial remeasurement loss only 0.26 Cr (l.359), well within FY26's 6.17 Cr; no assumption-change breach. Large FX-translation swing (−6.11 Cr vs +32.24 Cr Q4, l.366-367) is consolidation of foreign subs — neutral, noted. |
| F10 Share count / dilution | PASS | Paid-up 15.12 Cr (Q1FY26) -> 15.19 Cr (FY26) = +0.06 Cr ESOP exercise; basic-vs-diluted spread 0.05 (0.3%), stable (l.379/382-383). No large dilutive instrument. |
| F11 Reserves / net-worth tie-out | PASS | FY26 consol other equity 839.56 Cr + paid-up 15.19 = 854.75 Cr net worth = presentation Mar-26 shareholders' equity 854.75 Cr (l.380/1763), exact tie. |
| F12 Segment forensics | **FINDING** | Product Solutions segment assets 54.90 -> 128.32 Cr (+134% QoQ, l.430) while revenue −3.9% QoQ and segment result 16.00 -> 7.08 Cr; blended op-EBITDA margin 9.5% misses Notion 10% gate; goodwill impairment risk building. |
| F13 Board outcome beyond results | PASS | SINGLE_ITEM_AGENDA — only results approval (l.75, 78-79, 194-201). No AR/AGM/dividend/director/capital-raise resolution bundled; nothing material buried. |
| F14 Note-drafting inconsistencies | **FINDING** | Top-5 / Top-10 concentration disagree **within the same filing**: 50.8% / 66.1% (release+analyst, l.841/1009) vs 56% / 69% (presentation, l.1669/1679). Bears directly on the <=56% gate. |
| F15 Entity-list diffs | **FINDING** | Sasken Mexico "under liquidation process" (l.139 asterisk, l.152). Full list-diff not computable (NO_PRIOR_LEDGER). 13 entities read (l.136-151). |
| F16 Presentation dropped/reframed | **N.A.** | Doctype results; embedded deck present but no prior-quarter deck to diff (NO_PRIOR_LEDGER) — DROPPED_SLIDE / baseline-shift not assessable. Internal reframing captured under F14. |
| F17 Concall silence audit | **N.A.** | No concall transcript in this filing (A2: 0 turns, 0 questions). Notion-checklist silences folded into Findings narrative below. |

**Tally: 9 FINDING (F1,F2,F4,F6,F7,F8,F12,F14,F15) / 6 PASS (F3,F5,F9,F10,F11,F13) / 2 N.A. (F16,F17) = 17. No blank check. GATE A3 = PASS.**

---

## FINDINGS TABLE

| id | F# | ledger row / line | verbatim quote | Rs Cr | classification | forward implication |
|----|----|-------------------|----------------|-------|----------------|---------------------|
| FN1 | F1 | Sec4 r.VI, l.350-351 (consol) / l.653-654 (stand); Sec6 r.2 l.411 | "Impact of labour code — - - -" ; "Less :Inter segment revenue - - - -" | FY26 8.31 (consol) / 4.57 (stand) | NEUTRAL-FACT | Exceptional template line stands empty this Q (clean comparability); Labour Codes not yet fully notified — reactivation possible. Nil inter-segment = single delivery model. |
| FN2 | F2 | Sec4 r.IX l.356 vs Sec5 r.IX l.659; NCI l.373 | consol PAT "2,352.15" vs standalone "2,885.58"; NCI "(133.84)" | consol 23.52 vs stand 28.86; subs −5.33; NCI −1.34 | FORWARD-SIGNAL | Subsidiaries (Borqs ODM + Silicon) turned net loss-making; contribution swung +9.26 Cr (Q4) to −5.33 Cr (Q1), ~50pp of standalone PAT >> 5pp. Headline masked by standalone-services strength. |
| FN3 | F4 | Sec3 item1, l.285-293 | "one step-down subsidiary whose financial information reflect total revenue of Rs. 6,543.83 lakhs, net profit after tax of Rs. 64.71 lakhs" | rev 65.44 / PAT 0.65 | AMBIGUOUS | 19.3% of consol revenue on 0.99% net margin, via a component auditor, entity unnamed (ENTITY_NAME_NOT_IN_OTHER_MATTER_PARA). Confirms product-sub margin dilution; A4 to ask which entity. |
| FN4 | F6 | release/analyst l.1073, 1183-1185, 1241, 1348 | "subsequent batches are expected to join in the coming months"; "broader ownership of the MediaTek-based portfolio"; "culminating in a tapeout-ready design"; "sustain a profitable growth through FY27" | n/a | FORWARD-SIGNAL | Dateable management commitments feeding Role 5 promise-vs-delivery tracker (see register). |
| FN5 | F7 | release l.853-855, 857-860; analyst l.948 | "the contractual pass-through of increased memory costs supported reported revenue"; "navigate industry-wide memory supply and pricing pressures" | n/a | FORWARD-SIGNAL | Product Solutions topline is partly memory-cost pass-through, not real growth; new pre-emptive hedge signals continued Product margin pressure next quarter. |
| FN6 | F8 | Sec4 r.VIII l.353-355 | "Tax expense 604.94 … (2) Deferred tax (360.24)" | tax 6.05 on PBT 29.57 = 20.5%; deferred credit 3.60 | FORWARD-SIGNAL | ETR 467 bps below statutory 25.17%; current-tax-only ETR = 32.6%. Persistent deferred credits = DTA drawdown -> future ETR step-up. Disputed/uncertain tax (Notion Rs295.78 Cr) not disclosed anywhere in filing. |
| FN7 | F12 | Sec6 r.7 l.430; BS slide l.1756-1757; seg result l.418 | Product solutions segment assets "12,831.64 … 5,489.90"; Inventories "653.84 … 353.07"; Trade receivables "2,324.16 … 1,747.27" | assets 128.32 vs 54.90 (+73.4); inv +30.1; recv +57.7 | FORWARD-SIGNAL | Product/ODM working-capital balloon (+134% assets QoQ) while revenue fell −3.9% and result halved. Cash-conversion red flag — and CFO is NOT disclosed (see FN12). |
| FN8 | F12 | IS slide l.1705; seg-margin slide l.1513; seg result l.418 | "EBITDA 321.20 … 9.5%"; "Product Solutions 5.9% / 12.8% / 9.0%" | op-EBITDA 32.12 / 339.24 = 9.5%; PS result 7.08 vs 16.00 | FORWARD-SIGNAL | Blended operating EBITDA margin 9.5% **misses Notion Q1 pass-criterion (>=10%)**; not <8% so thesis-broken (a) NOT fired. Product Solutions gross margin collapsed 12.8% -> 5.9% QoQ. |
| FN9 | F14 | release/analyst l.841, 1009 vs presentation l.1669, 1679, 1396 | "Top 5 customers stood at 50.8% … Top 10 … 66.1%" vs "Top 5 … 56% … top 10 … 69%" | n/a | AMBIGUOUS | Same filing, two different Top-5 figures on the exact metric of the <=56% gate: 50.8% passes clearly, 56% sits on the ceiling. Top 3 (thesis-broken >45% NEW) not disclosed at all. A4 must reconcile. |
| FN10 | F15 | Sec9 l.139, 152 | "Sasken … Mexico S.A. de C.V ('Sasken Mexico') *" ; "Under liquidation process" | n/a | NEUTRAL-FACT | Mexico sub winding up (balance-sheet cleanup, not operations). Full entity-diff blocked by NO_PRIOR_LEDGER. |
| FN11 | F12 | BS slide l.1754 | "Intangible assets (including ROU and Goodwill) 3,131.31 … 3,092.46" | 313.13 vs 309.25 (+3.88) | FORWARD-SIGNAL | Borqs goodwill (Notion ~Rs173.23 Cr) buried inside a combined intangibles+ROU+goodwill line, grew (FX), **no impairment taken** — thesis-broken (e) NOT fired. But loss-making Borqs sub (FN2) raises FY27 year-end impairment/KAM risk; not separately disclosed. |
| FN12 | (cash) | BS slide only, l.1748-1767; no CFO statement anywhere in 57 pages | (no cash flow statement present) | CFO = INDETERMINATE | AMBIGUOUS | Consolidated CFO — the Notion "single most important signal" and a Q1 pass-criterion — is **absent** (Reg 33 Q1 carries no cash flow stmt). Do NOT resolve positive; against the visible WC balloon (FN7) this is a material gap. A4 to demand H1 CFO at Q2. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|-----------|--------------|-----|-------------|
| Subsequent fresher batches to join | H1/H2 FY27 | l.1073 | underway |
| Annual increment roll-out across all levels | July FY27 | l.1071 | underway/completed |
| Move to "sustained product responsibility … broader ownership of MediaTek-based portfolio" | FY27 | l.1183-1185 | underway |
| Massive MIMO Open RAN "tapeout-ready design on an advanced process node" | future milestone | l.1241 | underway |
| 5G NR-NTN "moving closer to commercial device adoption" | FY27+ | l.1191 | initiated |
| Hyderabad CoE to "add delivery capacity … scale strategic programmes" | Q1 done, ramping | l.1185, 1601 | completed(inaugurated) + ramping |
| Sasken Silicon Incubation Centre, Hubballi | Q1 FY27 | l.1057, 1599 | completed |
| CFO: "sustain a profitable growth through FY27" | FY27 | l.1348 | guidance/underway |

---

## NOTION MONITORING SILENCE (folded from N.A. F17 — items the filing does NOT address)
- **Consolidated CFO** (master gate): not disclosed — INDETERMINATE (FN12).
- **Working-capital strategy** (pass-criterion 4): not disclosed; only supply-chain commentary (l.857-860). WC actually built sharply (FN7).
- **Disputed/uncertain tax Rs295.78 Cr / Karnataka HC Rs81.59 Cr / Rs42.55 Cr under protest**: no contingent-liabilities note (FN6).
- **Silicon SSTPL revenue vs Rs50 Cr** and **60x4x3 $4M+ account count**: partial — deck shows 6 accounts at $4M+ (l.1669), active base 93; SSTPL revenue not broken out.
- **Bunpai India RPT**: no related-party disclosure in this filing.
- **Borqs goodwill Rs173.23 Cr**: not separately disclosed; no impairment language (FN11).
- **Governance flags (3 on file)**: no new governance event this filing (single-item board agenda, F13) — 4th flag not triggered here.

## GATE-RELEVANT SCORECARD vs NOTION Q1 PASS CRITERIA
1. EBITDA >=10% -> **9.5% FAIL** (FN8). 2. Product Solutions >=Rs100 Cr -> **119.68 Cr PASS**. 3. Consol CFO positive -> **INDETERMINATE** (FN12). 4. WC strategy disclosed -> **NOT DISCLOSED** (WC built). 5. Top-5 <=56% -> **AMBIGUOUS** 50.8% vs 56% (FN9). Thesis-broken triggers: (a) EBITDA<8% two-Q — not fired (9.5%); (b) Top5>60% — no; (c) CFO negative — indeterminate; (d) Silicon stall — not disclosed; (e) Borqs goodwill impairment — not taken. NEW Top3>45% — not disclosed.

```yaml
stage: A3-forensics
company: "SASKEN"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sasken-q1fy27/work/forensics_sasken_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FN1", check: "F1", line: "350-351/653-654/411", classification: "NEUTRAL-FACT", implication: "Exceptional labour-code line empty this Q; Labour Codes not yet notified, reactivation possible"}
  - {id: "FN2", check: "F2", line: "356/659/373", classification: "FORWARD-SIGNAL", implication: "Subs net loss-making; standalone PAT 28.86 Cr > consol 23.52 Cr; contribution swung +9.26 to -5.33 Cr"}
  - {id: "FN3", check: "F4", line: "285-293", classification: "AMBIGUOUS", implication: "Other-auditor sub 65.44 Cr rev / 0.65 Cr PAT (0.99%), entity unnamed; product-sub margin dilution"}
  - {id: "FN4", check: "F6", line: "1073/1183-1185/1241/1348", classification: "FORWARD-SIGNAL", implication: "Dateable commitments (freshers, MediaTek ownership, MIMO tapeout, FY27 profitable growth) for Role 5 tracker"}
  - {id: "FN5", check: "F7", line: "853-855/857-860/948", classification: "FORWARD-SIGNAL", implication: "Memory-cost pass-through inflates Product Solutions revenue; margin pressure persists next Q"}
  - {id: "FN6", check: "F8", line: "353-355", classification: "FORWARD-SIGNAL", implication: "ETR 20.5% (467bps below statutory) on deferred-tax credit; DTA drawdown = future ETR step-up; disputed tax undisclosed"}
  - {id: "FN7", check: "F12", line: "430/1756-1757", classification: "FORWARD-SIGNAL", implication: "Product Solutions segment assets +134% QoQ (inv +30, recv +57.7 Cr) vs falling revenue = WC balloon, cash risk"}
  - {id: "FN8", check: "F12", line: "1705/1513/418", classification: "FORWARD-SIGNAL", implication: "Op-EBITDA 9.5% misses Notion 10% gate; Product Solutions gross margin 12.8%->5.9% QoQ"}
  - {id: "FN9", check: "F14", line: "841/1009 vs 1669/1679", classification: "AMBIGUOUS", implication: "Top-5 disclosed 50.8% and 56% in same filing; straddles the <=56% gate; Top-3 undisclosed"}
  - {id: "FN10", check: "F15", line: "139/152", classification: "NEUTRAL-FACT", implication: "Sasken Mexico under liquidation; full entity-diff blocked (NO_PRIOR_LEDGER)"}
  - {id: "FN11", check: "F12", line: "1754", classification: "FORWARD-SIGNAL", implication: "Borqs goodwill buried in combined intangibles line, no impairment; loss-making sub raises FY27 impairment/KAM risk"}
  - {id: "FN12", check: "cash", line: "1748-1767", classification: "AMBIGUOUS", implication: "No cash flow statement; consolidated CFO INDETERMINATE, do not resolve positive; demand H1 CFO at Q2"}
forward_signals: ["FN2","FN4","FN5","FN6","FN7","FN8","FN11"]
ambiguous: ["FN3","FN9","FN12"]
commitments:
  - {commitment: "Fresher batches to join", implied_date: "H1/H2 FY27", ref: "l.1073", status_word: "underway"}
  - {commitment: "Annual increment roll-out", implied_date: "Jul FY27", ref: "l.1071", status_word: "underway"}
  - {commitment: "Broader ownership of MediaTek-based portfolio", implied_date: "FY27", ref: "l.1183-1185", status_word: "underway"}
  - {commitment: "Massive MIMO Open RAN tapeout-ready design", implied_date: "future milestone", ref: "l.1241", status_word: "underway"}
  - {commitment: "5G NR-NTN commercial device adoption", implied_date: "FY27+", ref: "l.1191", status_word: "initiated"}
  - {commitment: "Hyderabad CoE delivery capacity", implied_date: "Q1 done, ramping", ref: "l.1185,1601", status_word: "completed"}
  - {commitment: "Sasken Silicon Incubation Centre Hubballi", implied_date: "Q1 FY27", ref: "l.1057,1599", status_word: "completed"}
  - {commitment: "Sustain profitable growth through FY27", implied_date: "FY27", ref: "l.1348", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
