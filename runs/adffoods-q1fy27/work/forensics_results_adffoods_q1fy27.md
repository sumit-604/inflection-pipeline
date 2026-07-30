# A3 FORENSIC NOTES — ADF Foods Limited (ADFFOODS) — Q1 FY27 (quarter ended 30 June 2026) — DOCTYPE: results

Sources reconciled verbatim at cited lines:
- A1 results extract: `extract_results_adffoods_q1fy27.txt` (558 lines, 8 pages, Lakhs; x0.01 = Rs Cr)
- A1 companion disclosure extract (Ireland step-down subsidiary, same 29-Jul-2026 board meeting): `extract_disclosure_adffoods_q1fy27.txt` (112 lines)
- A2 ledger: `ledger_results_adffoods_q1fy27.md`
- Notion thesis / monitoring checklist + FY26 baseline: `notion_thesis_inline.md`

Ledger reconciliation: 100%. Every A2 ledger row read at its cited line before judging —
8 notes, 12 auditor paras, 8 entities (7 consol table + 1 excluded), 76 statement/segment line
items, 5 signature blocks, 6 board-letter items, 1 FX sub-table row. No unread rows.

Prior-quarter limitation (applies to F5 and F15): this is the first pipeline run for ADFFOODS;
no prior-quarter extract exists, so the required verbatim quarter-over-quarter diff of EoM language
(F5) and the entity list (F15) could NOT be performed. FY26 Annual Report baseline (supplied inline
via Notion thesis + injected entity baseline) is used as the best available comparator, and this
substitution is flagged explicitly in each check.

Units reminder: all statement/segment figures are Rs Lakhs unless stated; x0.01 to reach Rs Cr.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn/slide | short verbatim quote | classification | forward implication |
|----|-------|----------------|-----------------|----------------------|----------------|---------------------|
| A3-F1 | F1 ZERO-STANDING | §6 r14/r34/r37/r40; §8 r6 | 339, 409/412/415, 517 | "Exceptional Items (Refer note 5)"; "Less: lnterse[g]ment Revenue" (dash all periods) | AMBIGUOUS | Exceptional-items slot is LIVE (used FY26 for Rs 6.83 Cr Labour Codes) — future tariff/Ascot/restructuring one-offs will land here; zero intersegment revenue every period despite a manufacture-then-distribute group is a presentation question (are distribution subs selling third-party goods, or are inter-co sales eliminated elsewhere?); NCI lines blank across all 8 columns confirm 100% wholly-owned structure (no minority partners) |
| A3-F2 | F2 S-vs-C DECOMP | §6 r2 (rev), r21 (PAT) | 323, 363-365 | rev "12,094.45" (S) vs "16,728.89" (C); PAT "1,827.89" (S) vs "1,728.52" (C) | FORWARD-SIGNAL | Consol PAT is BELOW standalone every period (overseas cluster is a net drag). Drag NARROWED YoY: Q1FY27 99.37L = 5.44% of standalone PAT vs Q1FY26 174.71L = 10.28% (subsidiary losses improving — checklist item 11 Green). BUT revenue gap WIDENED: 38.3% of standalone (Q1FY27) vs 32.4% (Q1FY26) — overseas/distribution revenue growing faster than parent |
| A3-F3 | F3 SHELL DETECTION | §6 r5/r6/r8/r10 | 327, 328, 332, 335 | "Cost of material consumed 4,232.79 ... 4,232.79" (S = C, identical) | CONFIRMATORY-NEGATIVE | Cost of materials consumed is IDENTICAL standalone vs consolidated in every period — all manufacturing sits in the Indian standalone entity; subsidiaries buy finished goods (Purchases of Stock-in-trade C 1,528.38 vs S 440.62) and carry real employee (C 1,549.60 vs S 859.66) and depreciation (C 657.08 vs S 328.58) costs. Conclusion: NO shells — subsidiaries are live distribution/trading operations, NOT dormant. Confirms 100% concentration of manufacturing/operational risk in one Indian plant network (thesis 98% export concentration corroborated) |
| A3-F4 | F4 UNAUDITED RATIO | §3 para 6 + para 7 | 226-227, 265-267 | "total revenues of Rs. 8,440.93 lakhs, total net profit after tax of Rs. 77.20 lakhs"; "total revenue of Rs. 177.02 lakhs, total net loss after tax of Rs. (115.82) lakhs" | AMBIGUOUS | Two non-MSKA buckets. (a) Other-auditor-reviewed foreign subs: rev 8,440.93L = 50.5% of consol revenue, PAT 77.20L = 4.47% of consol PAT — over HALF of group revenue is not reviewed by the principal auditor. (b) UNREVIEWED management-furnished subs: rev 177.02L, net LOSS (115.82)L = 6.70% of consol PAT. Combined non-statutory-auditor-reviewed PAT exposure = 193.02L = 11.17% of consol PAT (>10% threshold → FINDING). Forensic red flag: the loss-making subs are precisely the ones with the WEAKEST assurance (unreviewed, "not material per Management"). Trend vs prior quarters NOT computable (first run) — flag for baseline next quarter |
| A3-F6 | F6 FWD-COMMITMENT | §5 note 6; disclosure Annex I | 481-483; disclosure 34-36, 78 | "actively engaging with its customers and implementing appropriate commercial strategies to mitigate the potential impact of such tariffs"; "approved the incorporation of a wholly owned step-down subsidiary in Ireland to support the Company's growth plans in Europe" | FORWARD-SIGNAL | Dated/dateable management commitments — see COMMITMENT REGISTER. Ireland incorporation "To be incorporated" (open); Rs 9.28 Cr of the tariff refund "recognized for evaluating commercial arrangements with Customers" is a held/contingent amount whose P&L landing is a future event. These feed the Role 5 promise-vs-delivery tracker |
| A3-F7 | F7 HEDGE MINING | §5 note 6 | 481, 482, 483 | "recognized for evaluating commercial arrangements with Customers"; "continues to closely monitor developments relating to the imposition of import tariffs"; "will continue to evaluate the evolving regulatory environment and reassess its position as further developments arise" | AMBIGUOUS | Note 6 newly loads a substantial tariff hedge (evaluate / monitor / reassess). Pre-emptive legal cover inside a NOTE tells you Q2 still carries live US-tariff uncertainty. The Rs 9.28 Cr held "for evaluating commercial arrangements" may or may not stick to P&L — direction uncertain, generate concall question |
| A3-F8 | F8 TAX FORENSICS | §6 r18 (deferred), r19 (earlier-period) | 347, 350/354, 355 | deferred tax "(197.93)" (S Q1FY27), "(249.43)" (C Q1FY27); "Adjust[ment] of t[a]x re[l]ating to e[a]rlier per[io]ds (72.18)" | AMBIGUOUS | ETR Q1FY27 near statutory (S 25.56%, C 26.41% vs 25.17%), BUT driven by a large deferred-tax CREDIT: consol current-tax-only rate = 869.62/2,348.71 = 37.03%; deferred credit of 249.43L shields ~1,062 bps (standalone shield ~806 bps). Consol deferred credits persistent (FY26 -514.33L, Q1FY27 -249.43L) = DTA recognition / carryforward utilisation → future ETR step-up risk if credits reverse. "Adjustment of tax relating to earlier periods" is non-zero (72.18 credit Q4FY26, 62.58 credit FY26) — in comparatives only, nil in Q1FY27 |
| A3-F12 | F12 SEGMENT | §8 r9/r10 (results), r18 (assets) | 513/520, 533 | Distribution result "266.52" on revenue "2,324.36"; Processed assets "59,164.18" | AMBIGUOUS | DISTRIBUTION segment margin COLLAPSED YoY: 266.52/2,324.36 = 11.5% (Q1FY27) vs 358.93/2,066.33 = 17.4% (Q1FY26) — ~590 bps compression on +12.5% revenue; results fell -25.7% YoY while revenue rose. Needs a concall question. PROCESSED foods assets grew 47,728.25 -> 59,164.18 (+24% YoY) = Surat greenfield capex proxy (Rs 50.52 Cr capitalised Mar-26), matched by rising segment liabilities (7,764 -> 11,833) so NOT an equity-only build. No segment shows assets with zero revenue. Unallocated corporate assets jumped 7,811.57 -> 10,407.00 (tariff refund + cash) |
| A3-F13 | F13 BOARD BEYOND | §1 r2 (inter alia); disclosure | letter 37-38; disclosure 34-36 | "has inter alia approved the Unaudited Standalone and Consolidated Financial Results"; "inter alia considered and approved the incorporation of a wholly owned step-down subsidiary in Ireland" | FORWARD-SIGNAL | Board outcome BEYOND results: same 29-Jul-2026 meeting approved a NEW Europe-expansion vehicle (Ireland step-down under ADF Foods UK Ltd). The results letter's "inter alia" is partially explained by the Ireland approval, but BOTH letters use "inter alia" (INTER_ALIA_UNDISCLOSED) — other unitemised business may exist. NO AR approval, AGM notice, record date, dividend, or director appointment disclosed this cycle (no Role 6 AR event triggered, no dividend/capital-raise signal) |
| A3-F14 | F14 DRAFTING | §4 r3 vs §5 note 3; note 8 | 193 vs 464; 489; 458 | table "ADF Foods Australia Pty Limited" vs note 3 "ADF Australia PTY Limited"; "www.adf.foods.com"; "Quater ended June 30, 2026" | NEUTRAL-FACT | Australia subsidiary named inconsistently between the auditor's consolidation table (line 193) and Note 3 prose (line 464, drops "Foods"); website URL typo (adf.foods.com vs adf-foods.com); "Quater" misspelling. Each immaterial; cumulatively a drafting-care/governance data point. No note-vs-letter audit/review contradiction (Note 1 and auditor both say "limited review") |
| A3-F15 | F15 ENTITY DIFF | §4 entity list; disclosure Annex I | disclosure 74-88; results 189-201 | "Name of the entity: ADF Foods Ireland Limited ..."; "Upon incorporation, Irish Subsidiary will be a wholly owned subsidiary of ADF Foods UK Limited" | FORWARD-SIGNAL | ENTITY-LIST ADDITION: new wholly-owned step-down subsidiary in Ireland (EUR 20,000 cash equity), held under ADF Foods UK Limited, "To be incorporated" — Europe expansion vehicle not in the prior thesis. Consol list otherwise reconciles to FY26 AR baseline: 7 entities (India subs merged into Telluric; Australia sub now consolidating; Vibrant Foods NJ wholly owned); Power Brands (Foods) Pvt Ltd still under voluntary liquidation and still excluded — no change vs baseline; NO JV/associates (Nil) confirmed. Prior-quarter VERBATIM entity diff NOT possible (first run) — FY26 AR baseline used |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINE ITEMS | FINDING | 9 ZERO_STANDING rows read; exceptional slot LIVE (FY26 Labour Codes), NCI blank confirms wholly-owned, zero intersegment revenue is a presentation question (line 339, 415, 517) |
| F2 STANDALONE vs CONSOLIDATED DECOMP | FINDING | PAT drag narrowed 10.28% -> 5.44% of standalone PAT YoY (subsidiary losses improving); revenue gap WIDENED 32.4% -> 38.3% (line 323, 363-365) |
| F3 SHELL-ENTITY DETECTION | FINDING | Cost of materials IDENTICAL S=C all periods -> manufacturing 100% in parent; subs have real employee/trading/depn costs -> distribution ops, NOT shells (line 327) |
| F4 UNAUDITED CONTRIBUTION RATIO | FINDING | 50.5% of consol revenue via other auditors; unreviewed mgmt-furnished subs carry a (115.82)L loss = 6.70% of PAT; combined non-MSKA PAT exposure 11.17% > 10% (line 226-227, 265-267) |
| F5 GOING CONCERN / EoM SCOPE | PASS | No Going Concern and no Emphasis-of-Matter paragraph in either report; Other-Matters paras 6-8 are reliance/exclusion, not GC. Vs FY26 AR baseline (Power Brands liquidation already known) no scope expansion. Prior-quarter verbatim diff not possible (first run) — flagged |
| F6 FORWARD-COMMITMENT PHRASE MINING | FINDING | 4 dateable commitments mined (Ireland incorporation, tariff customer strategies, Rs 9.28 Cr held-for-evaluation, ongoing regulatory reassessment) — see register (line 481-483; disclosure 34-36) |
| F7 HEDGE PHRASE MINING | FINDING | Note 6 newly loads a tariff hedge (evaluate/monitor/reassess) + Rs 9.28 Cr contingent amount -> Q2 tariff uncertainty pre-signalled (line 481-483) |
| F8 TAX FORENSICS | FINDING | Deferred-tax credit shields consol ETR ~1,062 bps (persistent credits FY26/Q1FY27) -> future ETR step-up risk; earlier-period tax adjustment non-zero in comparatives (line 347, 350/354, 355) |
| F9 OCI FORENSICS | PASS | Actuarial remeasurement (7.41L) well within FY26 full-year (29.62L); no single-quarter OCI swing exceeds prior full year; no assumption-change signal (line 377) |
| F10 SHARE COUNT AND DILUTION | PASS | Paid-up constant 2,197.27L every period (10,98,63,595 shares); basic = diluted EPS in every column -> no dilutive instruments, no warrant/ESOP spread (line 416-418, 430-432) |
| F11 RESERVES AND NET WORTH TIE-OUT | PASS | Other Equity disclosed year-end only (FY26: S 57,236.78L / C 54,957.74L); consol reserves below standalone by 22.79L Cr = 3.98% (< 5%), consistent with cumulative subsidiary losses; no third-party net-worth figure in filing to reconcile against (line 421) |
| F12 SEGMENT FORENSICS | FINDING | Distribution margin compressed ~590 bps YoY (17.4% -> 11.5%); Processed assets +24% YoY (Surat capex proxy) with matching liabilities; no zero-revenue asset build (line 513/520, 533) |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Same board meeting approved a new Ireland Europe-expansion step-down subsidiary; both letters "inter alia" (undisclosed residual business); no AR/AGM/dividend/director item (letter 37-38; disclosure 34-36) |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Australia sub named two ways (line 193 vs 464); website typo (line 489); "Quater" typo (line 458) — cumulatively a governance/drafting-care data point |
| F15 ENTITY LIST DIFFS | FINDING | New Ireland step-down subsidiary added (under ADF Foods UK Ltd, EUR 20,000); rest of 7-entity list reconciles to FY26 AR baseline; Power Brands liquidation unchanged; prior-quarter verbatim diff not possible (disclosure 74-88; results 189-201) |
| F16 PRESENTATION DROPPED/REFRAMED | N.A. | Doctype = results filing; no presentation deck in scope |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype = results filing; no concall transcript in scope (thesis notes concall is the Aug-2026 master gate, not supplied) |

Scorecard integrity: 17/17 marked, 0 blank. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Incorporate wholly-owned step-down subsidiary in Ireland (ADF Foods Ireland Limited) under ADF Foods UK Ltd, EUR 20,000 cash equity, to support Europe growth | "To be incorporated" — pending Irish regulatory approval; board-approved 29-Jul-2026 | disclosure lines 34-36, 74-88 | approved / initiated |
| "actively engaging with its customers and implementing appropriate commercial strategies to mitigate the potential impact of such tariffs" | ongoing, no date | Note 6, lines 482-483 | underway |
| Rs 9.28 Cr (USD 0.98mn) of US tariff refund "recognized for evaluating commercial arrangements with Customers" — resolution/landing pending | ongoing, no date | Note 6, line 481 | underway / evaluating |
| "will continue to evaluate the evolving regulatory environment and reassess its position as further developments arise" (US tariffs) | ongoing, no date | Note 6, line 483 | underway |

Status-change tracking (for Role 5 next quarter): no prior-quarter register exists, so no
initiated->underway->completed transitions can be confirmed this cycle. The four items above are the
Q1 FY27 baseline for next quarter's promise-vs-delivery comparison.

---

## NOTES FOR A4 (analyst) — questions to convert

FORWARD-SIGNAL findings (A3-F2, A3-F6, A3-F13, A3-F15): subsidiary PAT drag narrowing vs revenue
gap widening; the four dated commitments; the Ireland Europe-expansion vehicle (entity addition +
board action). AMBIGUOUS findings needing management questions (A3-F1, A3-F4, A3-F7, A3-F8, A3-F12):
zero intersegment revenue in a manufacture-then-distribute group; unreviewed loss-making subsidiaries
at 6.70% of PAT + 50.5% of revenue via other auditors; live US-tariff hedge and the Rs 9.28 Cr
contingent; deferred-tax credit shielding consol ETR ~1,062 bps; Distribution segment ~590 bps margin
collapse YoY. CONFIRMATORY-NEGATIVE (A3-F3): manufacturing 100% concentrated in the Indian standalone
entity. NEUTRAL (A3-F14): drafting inconsistencies. A3 does not resolve direction on the ambiguous
items — conservative bias, they are handed up as questions.

```yaml
stage: A3-forensics
company: "ADFFOODS"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/adffoods-q1fy27/work/forensics_results_adffoods_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F1", check: "F1", line: "339,415,517", classification: "AMBIGUOUS", implication: "exceptional slot live for future one-offs; zero intersegment revenue in a manufacture-then-distribute group; NCI blank confirms wholly-owned"}
  - {id: "A3-F2", check: "F2", line: "323,363-365", classification: "FORWARD-SIGNAL", implication: "consol PAT drag narrowed YoY (subs improving) but revenue gap widened 32.4pct->38.3pct of standalone"}
  - {id: "A3-F3", check: "F3", line: "327", classification: "CONFIRMATORY-NEGATIVE", implication: "identical cost of materials S=C -> all manufacturing concentrated in Indian parent; subs are distribution ops, not shells"}
  - {id: "A3-F4", check: "F4", line: "226-227,265-267", classification: "AMBIGUOUS", implication: "50.5pct of consol revenue via other auditors; unreviewed mgmt-furnished subs carry (115.82)L loss = 6.70pct of PAT; combined non-MSKA PAT exposure 11.17pct >10pct"}
  - {id: "A3-F6", check: "F6", line: "481-483", classification: "FORWARD-SIGNAL", implication: "four dateable commitments incl Ireland incorporation and Rs 9.28 Cr held-for-evaluation tariff refund"}
  - {id: "A3-F7", check: "F7", line: "481-483", classification: "AMBIGUOUS", implication: "Note 6 newly loads tariff hedge -> Q2 tariff uncertainty pre-signalled; Rs 9.28 Cr contingent may not stick to P&L"}
  - {id: "A3-F8", check: "F8", line: "347,355,350", classification: "AMBIGUOUS", implication: "deferred-tax credit shields consol ETR ~1062 bps (persistent) -> future ETR step-up risk; earlier-period tax adjustment non-zero in comparatives"}
  - {id: "A3-F12", check: "F12", line: "513,520,533", classification: "AMBIGUOUS", implication: "Distribution margin collapsed ~590 bps YoY (17.4pct->11.5pct); Processed assets +24pct YoY = Surat capex proxy with matching liabilities"}
  - {id: "A3-F13", check: "F13", line: "37-38 (results); 34-36 (disclosure)", classification: "FORWARD-SIGNAL", implication: "board approved new Ireland Europe-expansion step-down sub; both letters inter alia -> possible residual undisclosed business; no AR/AGM/dividend/director item"}
  - {id: "A3-F14", check: "F14", line: "193 vs 464; 489; 458", classification: "NEUTRAL-FACT", implication: "Australia sub name mismatch, website typo, Quater typo -> cumulative drafting-care governance data point"}
  - {id: "A3-F15", check: "F15", line: "74-88 (disclosure); 189-201 (results)", classification: "FORWARD-SIGNAL", implication: "new Ireland step-down subsidiary added under ADF Foods UK Ltd; rest reconciles to FY26 AR baseline; prior-quarter verbatim diff not possible"}
forward_signals: ["A3-F2", "A3-F6", "A3-F13", "A3-F15"]
ambiguous: ["A3-F1", "A3-F4", "A3-F7", "A3-F8", "A3-F12"]
commitments:
  - {commitment: "Incorporate wholly-owned step-down subsidiary in Ireland (ADF Foods Ireland Limited) under ADF Foods UK Ltd, EUR 20,000, Europe growth", implied_date: "To be incorporated; approved 29-Jul-2026", ref: "disclosure lines 34-36,74-88", status_word: "approved"}
  - {commitment: "engaging customers and implementing commercial strategies to mitigate US tariff impact", implied_date: "ongoing, no date", ref: "Note 6, lines 482-483", status_word: "underway"}
  - {commitment: "Rs 9.28 Cr of US tariff refund recognized for evaluating commercial arrangements with Customers", implied_date: "ongoing, no date", ref: "Note 6, line 481", status_word: "underway"}
  - {commitment: "continue to evaluate evolving regulatory environment and reassess position (US tariffs)", implied_date: "ongoing, no date", ref: "Note 6, line 483", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
