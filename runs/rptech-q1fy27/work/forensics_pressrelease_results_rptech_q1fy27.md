# A3 FORENSIC NOTES — RPTECH Q1 FY27 (doctype: results / company PRESS RELEASE)

Source extract: `extract_pressrelease_results_rptech_q1fy27.txt` (185 doc lines, 4 pages, unit convention Millions).
Ledger reconciled: `ledger_pressrelease_results_rptech_q1fy27.md` — all rows read verbatim at cited lines; 100% reconciled.
Thesis weight (Notion, memory only): Q1 FY27 is the BINDING CASH-CONVERSION gate. CFO/PAT, working-capital days, debtor days are hair-trigger.

Artifact nature: this is the covering letter + press release, NOT the full reviewed results package. No numbered notes, no auditor report, no financial statement schedules, no consolidation-entity list, no board-outcome agenda, no concall transcript are present. That constraint drives the large N.A. count below; the substantive checks that DO apply are F6, F7, F10, F13 (F14 PASS).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F6-1 | F6 | Fwd/hedge rows 1-6 (quotes) | 110-111 | "we remain firmly committed to profitable growth and long-term value creation" | FORWARD-SIGNAL | Every management commitment is growth/quality-flavored; there is ZERO commitment to cash conversion, CFO/PAT, or working-capital discipline at the exact quarter the thesis makes cash the binding gate. A4: ask for a CFO/PAT target band for FY27-FY28. |
| F6-2 | F6 | KPI row 19 (NUMBER_OMITTED) | 96-98 | "Achieved the highest annualized Return on Capital Employed (ROCE) and Return on Equity (ROE) for the quarter post-listing" | AMBIGUOUS | Superlative ROCE/ROE claim with NO percentage anywhere in the document; Notion checklist item 4 (ROCE >17% green / <14% red) cannot be verified from this artifact. A4: ask management to state the actual Q1 FY27 annualised ROCE and ROE. |
| F6-3 | F6 | KPI rows 1,5-6 vs omission | 71-73, 84 | "Revenue for Q1 FY27 stood at INR 51,019 million, registering the highest growth of 61.9% YoY" | AMBIGUOUS | Press release leads with Revenue +61.9% / PAT +69.5% / "Highest Ever" but does NOT state CFO, CFO/PAT, working-capital days or debtor days — the four binding-gate metrics. Full P&L/segment data is hosted separately (line 134-135), so this is presentational emphasis, not proven suppression. A4: extract Q1 FY27 CFO, CFO/PAT, WC days, debtor days from the reviewed statements. |
| F6-4 | F6 | KPI rows 3,8-9,13-14 | 84, 86 | "EBITDA Margin 3.04% ... (24) Bps" | FORWARD-SIGNAL | EBITDA +50.0% LAGS Revenue +61.9%; margin contracted 24 bps YoY to 3.04% (prior Q1 ~3.28%). Bullet frames this as a "healthy increase of 50.0%" (line 72), masking operating deleverage this quarter. Margin level still green vs checklist item 6 (>=2.7%), but the YoY trend is yellow. A4: is the 24 bps contraction mix (VDA/enterprise) or price competition? |
| F7-1 | F7 | Fwd/hedge row 1 (quote) | 110-111 | "While driving strong revenue expansion, we remain firmly committed to profitable growth" | AMBIGUOUS | Management-quote concessive hedge: the "While ..." construction pre-emptively concedes tension between revenue growth and profitability, corroborated by the F6-4 margin contraction. Reads as soft guidance that growth is being bought at some margin cost. A4: convert to a margin-trajectory question. |
| F10-1 | F10 | KPI rows 11,16 | 86 | "Diluted EPS ... YoY Growth: 64.0%" (vs Net Profit YoY 69.5%) | AMBIGUOUS | Diluted EPS +64.0% grows ~5.5pp slower than PAT +69.5%, implying ~3.3% MORE diluted shares in Q1 FY27 than Q1 FY26 — i.e. YoY dilution AFTER the IPO base (the IPO share count was already in the prior-year base). Basic EPS not disclosed, so intra-quarter basic-vs-diluted spread is uncomputable. A4: what corporate action (ESOP exercise / issuance) added shares in the last 12 months, and are there further dilutive instruments outstanding? |
| F13-1 | F13 | Segment/brand row 4; corp-action context | 101-102 | "Announced acquisition of 67% stake in VDA Infosolutions, expanding into fast growing enterprise technology and digital infrastructure" | FORWARD-SIGNAL | Board-level corporate action beyond the results: VDA becomes a 67% subsidiary (Notion: Rs 368.5 Cr cash, plan to 100%), a forthcoming consolidation-list addition next quarter. External agency (CRISIL, per Notion) flagged VDA's "thin margin and LARGE WORKING CAPITAL REQUIREMENT" — directly aggravating the Pillar 2 cash-conversion gate. A4: pro-forma WC-days impact of VDA consolidation; funding source and net-debt effect of the Rs 368.5 Cr cash outlay. |

---

## CHECKLIST SCORECARD (all 17; no blanks — GATE A3)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | Ledger zero_standing_items = 0; no financial-statement line-item table in this press-release artifact (schedules hosted separately, line 134-135). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Press release reproduces only "Consolidated Financial Performance" (line 81-86); no standalone figures present to decompose, though the covering letter (line 17-18) confirms standalone exists elsewhere. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost lines and no standalone-vs-consolidated cost comparison in this artifact. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor "Other Matters" paragraph / component-auditor data; entire results are unaudited (line 17) but no auditor report is in this artifact. |
| F5 GOING CONCERN / EoM | N.A. | No auditor report, EoM or going-concern paragraph; no prior-quarter extract supplied for a verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Findings F6-1..F6-4: growth-only commitment set with zero cash commitment; ROCE/ROE claimed without a number; binding cash-gate KPIs omitted; margin-contraction masked by "healthy increase" framing. |
| F7 HEDGE PHRASE MINING | FINDING | F7-1: management-quote concessive hedge "While driving strong revenue expansion..." The 7 Safe-Harbor hedges (rows 7-13, lines 148-154) are standard boilerplate and not separately flagged. |
| F8 TAX FORENSICS | N.A. | No tax line or ETR data in this artifact. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial data in this artifact. |
| F10 SHARE COUNT & DILUTION | FINDING | F10-1: diluted EPS +64.0% vs PAT +69.5% implies ~3.3% YoY diluted-share increase; basic EPS not disclosed. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No balance sheet, other-equity or paid-up-capital figures in this artifact. |
| F12 SEGMENT FORENSICS | N.A. | Segment results hosted separately (line 134); no segment assets/liabilities reproduced. Two verticals named (PES line 165, LIT line 166) without financials. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | F13-1: VDA Infosolutions 67% acquisition announced (line 101-102) — WC-heavy consolidation incoming. (Notion-referenced Embedded slump sale and Restar JV are SEPARATE press releases, not in this artifact.) |
| F14 NOTE DRAFTING INCONSISTENCIES | PASS | Entity names consistent across tables ("Rashi Peripherals Limited", "VDA Infosolutions" L101/L126, "WEKA" L99/L128); no note-vs-auditor-letter contradiction (no notes/letter present). Branch count 57 (L162) = FY26 base 55 + 2 new (L103-104), self-consistent. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list and no prior-quarter list in this artifact to diff; the VDA forthcoming addition is captured under F13-1 to avoid double-counting. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is results/press release, not an investor-presentation deck (deck to be submitted later, line 143-144). |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is not a concall transcript; the earnings call is scheduled for the next day, 2026-08-05 (line 138). Checklist-coverage note carried below for A4. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/line ref | status word |
|------------|--------------|---------------|-------------|
| Analyst/institutional-investor presentation "will be submitted to Stock Exchanges" & hosted on website | ~2026-08-05/06 (around the call) | line 143-144 | will be (pending) |
| Q1 FY27 earnings conference call to discuss results | 2026-08-05, 10:00 AM IST | line 138 | scheduled |
| Acquisition of 67% stake in VDA Infosolutions (Notion: plan to reach 100%) | announced Q1 FY27; consolidation forthcoming | line 101-102 | announced / initiated |
| WEKA (WEKA.io) added to Enterprise vertical | Q1 FY27 | line 99 | completed |
| "we remain firmly committed to profitable growth and long-term value creation" | ongoing / undated | line 110-111 | ongoing |
| "we continue to invest in advanced technical capabilities and build meaningful strategic partnerships" | ongoing / undated | line 112-113 | ongoing |

---

## NOTION CHECKLIST COVERAGE NOTE (context for A4; F17 formally N.A. on a press release)

Of the 12 Notion monitoring metrics, this press release addresses only two and is silent on the binding cash cluster:

- CFO/PAT (item 1) — SILENT (not in PR). Binding gate.
- Working-capital days (item 2) — SILENT. Binding gate.
- Debtor days (item 3) — SILENT. Binding gate.
- ROCE annualised (item 4) — CLAIMED "highest post-listing" but NO NUMBER (F6-2).
- Revenue ex-project growth (item 5) — only headline Revenue +61.9% given; no ex-project split.
- EBITDA margin (item 6) — DISCLOSED 3.04% (green level) but DOWN 24 bps YoY (yellow trend, F6-4).
- Dell Commercial share (item 7) — SILENT.
- Semiconductor growth (item 8) — SILENT (Embedded/semiconductor reorg is a separate PR).
- AI PC penetration (item 9) — SILENT.
- Net D/E (item 10) — SILENT (relevant given VDA Rs 368.5 Cr cash outlay).
- Promoter pledge (item 11) — SILENT (not expected in a PR).
- Promoter holding (item 12) — SILENT (not expected in a PR).

The press release leads with revenue growth and "Highest Ever" superlatives while every binding cash-conversion metric is only available in the separately-hosted reviewed statements (line 134-135). This is the emphasis-vs-omission signal the task flagged; it is carried into A4 questions via findings F6-1, F6-2, F6-3.

---

## RECONCILIATION STATEMENT

All A2 ledger categories (kpi_figures 25+1, management_quotes 2, forward_looking_hedge 13, segment_brand_mentions 12, zero_standing_items 0, letter_recipients 2, reference_identifiers 5, signature_block 3, corporate_actions 5, contacts 2) were read at their cited lines within the 185-line extract. 100% reconciled; no unread rows.

```yaml
stage: A3-forensics
company: "rptech"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/rptech-q1fy27/work/forensics_pressrelease_results_rptech_q1fy27.md"
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
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: PASS
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F6-1", check: "F6", line: "110-111", classification: "FORWARD-SIGNAL", implication: "All management commitments are growth/quality-flavored; zero cash-conversion or CFO/PAT commitment at the binding cash-gate quarter."}
  - {id: "F6-2", check: "F6", line: "96-98", classification: "AMBIGUOUS", implication: "'Highest annualized ROCE and ROE post-listing' claimed with no percentage; Notion checklist item 4 unverifiable from this artifact."}
  - {id: "F6-3", check: "F6", line: "71-73,84", classification: "AMBIGUOUS", implication: "Leads with Revenue +61.9%/PAT +69.5%/'Highest Ever'; CFO, CFO/PAT, working-capital days and debtor days (the binding gate) are not stated in the press release."}
  - {id: "F6-4", check: "F6", line: "84,86", classification: "FORWARD-SIGNAL", implication: "EBITDA +50.0% lags Revenue +61.9%; margin (24) bps YoY to 3.04%; 'healthy increase' framing masks operating deleverage this quarter."}
  - {id: "F7-1", check: "F7", line: "110-111", classification: "AMBIGUOUS", implication: "Concessive management-quote hedge 'While driving strong revenue expansion...' telegraphs revenue-vs-profit tension, corroborating the margin contraction."}
  - {id: "F10-1", check: "F10", line: "86", classification: "AMBIGUOUS", implication: "Diluted EPS +64.0% vs PAT +69.5% implies ~3.3% YoY diluted-share increase post-IPO-base; basic EPS not disclosed."}
  - {id: "F13-1", check: "F13", line: "101-102", classification: "FORWARD-SIGNAL", implication: "67% VDA Infosolutions acquisition announced; WC-heavy consolidation and entity-list addition incoming, aggravating the Pillar 2 cash gate; Rs 368.5 Cr cash outlay per Notion."}
forward_signals: ["F6-1", "F6-4", "F13-1"]
ambiguous: ["F6-2", "F6-3", "F7-1", "F10-1"]
commitments:
  - {commitment: "Analyst/institutional-investor presentation to be submitted to exchanges and hosted on website", implied_date: "~2026-08-05/06", ref: "line 143-144", status_word: "will be (pending)"}
  - {commitment: "Q1 FY27 earnings conference call to discuss results", implied_date: "2026-08-05 10:00 IST", ref: "line 138", status_word: "scheduled"}
  - {commitment: "Acquisition of 67% stake in VDA Infosolutions (plan to 100%)", implied_date: "announced Q1 FY27; consolidation forthcoming", ref: "line 101-102", status_word: "announced/initiated"}
  - {commitment: "WEKA (WEKA.io) added to Enterprise vertical", implied_date: "Q1 FY27", ref: "line 99", status_word: "completed"}
  - {commitment: "Remain committed to profitable growth and long-term value creation", implied_date: "ongoing/undated", ref: "line 110-111", status_word: "ongoing"}
gate_a3: pass
blank_checks: []
```
