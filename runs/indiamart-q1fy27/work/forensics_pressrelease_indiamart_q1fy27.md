# A3 FORENSIC NOTES — Press Release — INDIAMART (IndiaMART InterMESH Limited) — Q1 FY27

Doctype: pressrelease (Results Press Release — management narrative + quantitative highlights)
A1 extract: `runs/indiamart-q1fy27/work/extract_pressrelease_indiamart_q1fy27.txt` (194 lines, 5 pages, unit: Crores)
A2 ledger: `runs/indiamart-q1fy27/work/ledger_pressrelease_indiamart_q1fy27.md`
Prior-quarter extract: NONE (first pipeline run for this ticker — no verbatim EoM / entity / dropped-metric diff possible; silence counts are baseline = 1 quarter)

## LEDGER RECONCILIATION
100% of A2 ledger rows read verbatim at their cited extract lines before judging:
Table 1 bullets B1 (L70), B2 (L71), B3 (L72); Table 2 claims #1–#24 (L70–L119, L174–175);
Table 3 metrics T1 (L144), T2 (L146), T3 (L148), T4 (L149), T5 (L151), T6 (L152), T7 (L155),
T8 (L158), T9 (L162), T10 (L164), T11 (L165); Table 4 quote Q1 (L123, 126–131);
Table 5 structural S1–S7. Rows read / rows in ledger = 100%.

Key derived cross-checks (from lines read, not estimates):
- Standalone EBITDA 149 (L148) > Consolidated EBITDA 146 → Busy Infotech is EBITDA-dilutive ≈ −3 Cr.
- Standalone PAT 176 (L151) > Consolidated PAT 172 → Busy Infotech is earnings-dilutive ≈ −4 Cr.
- Implied other income (Total Income − Revenue from Ops): standalone 464−376 = 88 Cr; consol 521−414 = 107 Cr (~19–21% of Total Income) — undisclosed as to composition.
- Standalone CFO/PAT = 153/176 = 0.87 (<1.0); Consol CFO/PAT = 163/172 = 0.95.
- Net Profit QoQ +153% standalone / +243% consol (L151) implies a sharply depressed prior quarter (Q4 FY26 consol PAT ≈ Rs 50 Cr) — base effect source undisclosed.

---

## COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Ref (line) | Status word |
|---|---|---|---|
| Host earnings webinar for investors/analysts to discuss Q1 FY27 | Tue 21 Jul 2026, 17:00 IST | L174–176 ("will host earnings webinar") | scheduled / underway |
| Audio & video recording of management discussion + Q&A made available in IR section | Post-call, undated | L182–183 ("will be available online and will be accessible") | initiated |

No operational, strategic, capex, or capital-action dated commitments appear in the release. CEO quote (L112–117) is directional sentiment ("remain confident in our ability to create long-term value"), not a datable commitment.

---

## FINDINGS TABLE

| id | check | ledger ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-a | F1 | T11 | 165, 88–89 | "Paying Suppliers (In '000) 218 0% (1%)" ; "growth was primarily driven by improvement in realization from paying suppliers" | FORWARD-SIGNAL | Paying-supplier base is flat YoY and −1% QoQ (declined sequentially) while standalone revenue grew 9% — growth is now entirely realization/ARPU-led, not net adds. Ceiling/churn risk on the core engine. Consolidated column dashed because Busy Infotech has no paying-supplier concept (structural template-only, not a data gap). |
| F16-a | F16 | B2 / T4 | 71, 149 | "Standalone EBITDA of Rs. 149 Crore representing EBITDA margin of 40%" ; "EBITDA Margin (%) 40% ... 35%" | FORWARD-SIGNAL | Headline bullet cherry-picks the 40% STANDALONE margin while consolidated margin is 35% (T4). Standalone EBITDA (149) > consolidated (146) → Busy Infotech dilutes group EBITDA (~−3 Cr). Selective framing masks subsidiary drag. |
| F16-b | F16 | T5 | 151 | "Net Profit for the period 176 6% 153% 172 12% 243%" | AMBIGUOUS | Net profit is absent from all three headline bullets. Consolidated PAT 172 < standalone PAT 176 → Busy is earnings-dilutive (~−4 Cr). QoQ +243% consol / +153% standalone implies a depressed Q4 FY26 base (consol PAT ≈ Rs 50 Cr); cause of the base effect undisclosed → A4 question. |
| F16-c | F16 | B3 / T8 | 72, 158 | "Consolidated Cash generated from Operations of Rs. 163 Crore" ; "Cash flow from Operations 153 6% (47%) 163 2% (44%)" | AMBIGUOUS | Headline states CFO with no YoY; actual YoY only +2% consol / +6% standalone and QoQ −44%/−47%. Sharp sequential cash-generation drop not addressed in narrative; standalone CFO/PAT = 0.87 (<1.0) — cash conversion below unity, monitor next quarter. |
| F17-a | F17 (#4) | claim rows 5,16 | 88–89 | "growth was primarily driven by improvement in realization from paying suppliers" | FORWARD-SIGNAL | Growth is explicitly realization-led, yet NO ARPU / top-10% ARPU figure is disclosed — silence on the exact metric that would size the realization runway. Baseline quarter. |
| F17-b | F17 (#7) | rows 6,9,12 | 80–81, 84–85 | "Busy Infotech Revenue of Rs 36 Crore" ; "Busy Infotech Collections of Rs 59 Crore" | FORWARD-SIGNAL | Busy figures carry NO YoY growth rate (ledger rows 6,9,12 "no YoY stated") while IndiaMART standalone and consolidated growth are both stated — selective omission of subsidiary growth. Busy collections (59) far exceed revenue (36), hinting at deferred-revenue build or billing lumpiness. |
| F17-c | F17 (#9) | T1 vs T2 | 144, 146 | "Total Income 464 ... 521" vs "Revenue from Operations 376 ... 414" | FORWARD-SIGNAL | Implied other income = 88 Cr standalone / 107 Cr consol (~19–21% of Total Income) is undisclosed as to source. Treasury income on a Rs 3,553 Cr cash pile drives roughly a fifth of income yet is never broken out — rate-sensitive earnings tail unquantified. |
| F17-d | F17 (#2,#10) | B-block / claim 21 | 23–24, 118 | "Audited Consolidated and Standalone Financial Results" ; "Unique business enquiries of 26 million" | AMBIGUOUS | Release repeatedly claims results are AUDITED (not the usual quarterly limited review) yet carries zero auditor commentary (checklist #10 silent). Active buyers LTM (#2) also silent — only unique enquiries (26M) given, not buyer count. Q1 "audited" wording worth confirming with management. |

---

## CHECKLIST SCORECARD (all 17 — no blanks)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING | FINDING | T11 Consolidated Paying-Suppliers dashed (structural — Busy has no supplier concept); standalone 218K flat YoY, −1% QoQ → realization-led growth (F1-a). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Full JV/associate/subsidiary/elimination decomposition needs segment + balance-sheet detail absent from a press release. Headline S-vs-C gap (PAT 172<176, EBITDA 146<149) captured under F16-a/F16-b. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consol cost-line detail in a press release; cannot compare Cost of Materials / Employee Benefits / Depreciation. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor "Other Matters" paragraph in a press release; component-auditor Rs/% not disclosable here. |
| F5 GOING CONCERN / EoM | N.A. | No auditor report/EoM in a press release; also first run, no prior-quarter paragraph to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | PASS | Only lexicon hits are logistical: "will host" earnings webinar (L174–176) and recording "will be available" (L182–183); both logged in Commitment Register; no operational/strategic dated commitments. |
| F7 HEDGE PHRASE MINING | PASS | No hedge-lexicon terms ("subject to", "evaluating", "no assurance", "exploring", "in discussions", "endeavour", etc.) present in the narrative or CEO quote. Attribution phrase "primarily driven by improvement in realization" (L88–89) is not a hedge; carried in F1-a/F17-a. |
| F8 TAX FORENSICS | N.A. | No PBT/tax line, no ETR, no deferred-tax disclosure in a press release (only net profit shown). |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial line in a press release. |
| F10 SHARE COUNT & DILUTION | N.A. | No paid-up capital, share count, or basic/diluted EPS disclosed in the press release. |
| F11 RESERVES & NET WORTH | N.A. | No Other Equity / paid-up / net-worth figures; Cash & Investments (Rs 3,553 Cr) is not net worth. No third-party number to tie out. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities disclosed; only Busy Infotech revenue/collections given (no segment BS). |
| F13 BOARD OUTCOME | N.A. | No board resolutions, AGM notice, record date, or director appointments in the release — only an earnings-call notice. |
| F14 NOTE DRAFTING INCONSISTENCIES | N.A. | No notes-to-accounts or auditor letter to cross-check; "Audited" wording (L23–24) surfaced under F17-d instead. |
| F15 ENTITY LIST DIFFS | N.A. | First run, no prior consolidation list; release names only IndiaMART + Busy Infotech, no full entity roster. |
| F16 DROPPED/REFRAMED DISCLOSURES | FINDING | Headline bullets selectively mix standalone EBITDA margin (40%) with consolidated revenue/cash, omit net profit, and strip YoY/QoQ context from CFO — three reframing choices (F16-a/b/c). No prior deck to diff for dropped metrics. |
| F17 SILENCE AUDIT | FINDING | Against the monitoring checklist: silent on Top-10% ARPU (#4), Busy billing growth (#7), Treasury/Other Income composition (#9), Active buyers LTM (#2), Auditor commentary (#10). Disclosed: paying suppliers (#1), unique enquiries (#3), standalone EBITDA margin (#5), CFO/PAT components (#6). Promoter shareholding (#8) not expected in a release (low signal). See table below. |

---

## F17 SILENCE TABLE (monitoring checklist vs press release; baseline quarter = 1)

| # | Checklist metric | Disclosed? | Note | Consec. quarters silent |
|---|---|---|---|---|
| 1 | Net paying suppliers seq | YES | 218K, 0% YoY, −1% QoQ (L165) — flat/declining, see F1-a | 0 |
| 2 | Active buyers LTM | NO | Only "unique business enquiries 26 million" (L118) given, not buyer count | 1 (baseline) |
| 3 | Unique business inquiries | YES | 26 million (L118) | 0 |
| 4 | Top 10% ARPU growth YoY | NO | Growth called realization-led (L88–89) but no ARPU figure → F17-a | 1 (baseline) |
| 5 | Standalone EBITDA margin | YES | 40% (L71, T4 L149) | 0 |
| 6 | CFO/PAT | PARTIAL | Components present (CFO & PAT); ratio not shown; standalone 0.87 (<1.0) → F16-c | 0 |
| 7 | Busy Infotech billing growth | NO | Busy revenue 36 / collections 59 given, no YoY (L80–85) → F17-b | 1 (baseline) |
| 8 | Promoter shareholding | NO | Not customary in a results press release (low signal) | 1 (baseline) |
| 9 | Treasury Other Income | NO | ~Rs 88 Cr standalone / 107 Cr consol implied, uncomposed → F17-c | 1 (baseline) |
| 10 | Auditor commentary | NO | Claims "Audited" (L23–24) but zero auditor opinion/commentary → F17-d | 1 (baseline) |

---

## HANDOFF TO A4 (questions to raise with management)
- FORWARD-SIGNAL: F1-a (paying suppliers flat/−1% QoQ; realization runway?), F16-a (consolidated EBITDA margin 35% vs headlined 40%; Busy margin trajectory), F17-a (quantify ARPU / top-10% ARPU growth), F17-b (Busy Infotech YoY growth and collections>revenue gap), F17-c (composition and rate-sensitivity of ~Rs 88–107 Cr other income).
- AMBIGUOUS: F16-b (what depressed Q4 FY26 PAT driving +243% QoQ; Busy loss run-rate), F16-c (CFO QoQ −44% and sub-1.0 standalone cash conversion — seasonal or structural), F17-d ("audited" vs limited review for Q1; absence of auditor commentary; active-buyers count).

```yaml
stage: A3-forensics
company: "INDIAMART"
quarter: "Q1 FY27"
doctype: "pressrelease"
model: claude-opus-4-8
status: complete
forensics_path: "runs/indiamart-q1fy27/work/forensics_pressrelease_indiamart_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: PASS
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "F1-a", check: "F1", line: "165, 88-89", classification: "FORWARD-SIGNAL", implication: "Paying suppliers flat YoY / -1% QoQ; 9% standalone growth is realization-led, ARPU ceiling/churn risk; consol column dashed is structural (Busy has no supplier concept)"}
  - {id: "F16-a", check: "F16", line: "71, 149", classification: "FORWARD-SIGNAL", implication: "Headline cherry-picks 40% standalone EBITDA margin; consolidated is 35%; Busy Infotech EBITDA-dilutive ~-3 Cr"}
  - {id: "F16-b", check: "F16", line: "151", classification: "AMBIGUOUS", implication: "Net profit omitted from headline; consol PAT 172 < standalone 176 (Busy earnings-dilutive ~-4 Cr); +243% QoQ implies depressed Q4 FY26 base, cause undisclosed"}
  - {id: "F16-c", check: "F16", line: "72, 158", classification: "AMBIGUOUS", implication: "CFO headlined without YoY; actual +2% YoY / -44% QoQ; standalone CFO/PAT 0.87 (<1.0) cash conversion below unity"}
  - {id: "F17-a", check: "F17", line: "88-89", classification: "FORWARD-SIGNAL", implication: "Growth explicitly realization-led but no ARPU / top-10% ARPU disclosed; silence on runway-sizing metric"}
  - {id: "F17-b", check: "F17", line: "80-81, 84-85", classification: "FORWARD-SIGNAL", implication: "Busy Infotech revenue/collections given with no YoY growth; collections 59 >> revenue 36 hints deferred-revenue build/lumpiness"}
  - {id: "F17-c", check: "F17", line: "144, 146", classification: "FORWARD-SIGNAL", implication: "Implied other income ~88 Cr SA / 107 Cr consol (~19-21% of total income) uncomposed; rate-sensitive treasury tail unquantified"}
  - {id: "F17-d", check: "F17", line: "23-24, 118", classification: "AMBIGUOUS", implication: "Claims AUDITED (not usual Q1 limited review) with zero auditor commentary; active buyers LTM also silent"}
forward_signals: ["F1-a", "F16-a", "F17-a", "F17-b", "F17-c"]
ambiguous: ["F16-b", "F16-c", "F17-d"]
commitments:
  - {commitment: "Host Q1 FY27 earnings webinar for investors/analysts", implied_date: "2026-07-21 17:00 IST", ref: "L174-176", status_word: "scheduled"}
  - {commitment: "Make audio/video recording of management discussion + Q&A available in IR section", implied_date: "post-call (undated)", ref: "L182-183", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
