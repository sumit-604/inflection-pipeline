# A3 FORENSIC NOTES — E2E Networks Limited (E2E), Q1 FY27 — doctype: PRESENTATION (investor press release)

Source extract: `/home/user/inflection-pipeline/runs/e2e-q1fy27/work/extract_presentation_e2e_q1fy27.txt` (96 lines, 2 pages: cover letter + press-release body "E2E Networks Reports Q1 FY'27 Results").
Ledger contract: `/home/user/inflection-pipeline/runs/e2e-q1fy27/work/ledger_presentation_e2e_q1fy27.md`
Cross-check document (same-day results filing, used per A2 NUMERIC_INCONSISTENCY directive): `/home/user/inflection-pipeline/runs/e2e-q1fy27/work/extract_results_e2e_q1fy27.txt`
Unit convention: press release in **Rs Millions** (x0.1 -> Rs Cr). Filing in **Rs Lakhs** (x0.1 -> Rs Mn; x0.01 -> Rs Cr). All cross-doc comparisons below convert the filing Lakhs to Mn (x0.1) to match the release.
Ledger reconciliation: **100%** — every disclosure unit in all 9 ledger sections (2 slides, 42 KPI rows, 14 admin identifiers, 12 highlight bullets, 12 narrative statements, 2 about, 3 footnotes, 2 entities, 3 signature-block units) read verbatim at its cited line before judging.

Note on comparatives: per the same-day filing Note 9 (results extract L141-142/L227-228) the subsidiary Sovcloud was pre-operational at 30-Jun-2026, so consolidated = standalone this quarter; the press release carries a single unlabelled figure set that maps 1:1 to the consolidated filing.

---

## CROSS-DOCUMENT RECONCILIATION (press release Rs Mn vs filing Rs Lakhs x0.1) — core of this pass

| Metric | Press release (line) | Filing (line, Lakhs) | Filing x0.1 (Mn) | Match |
|--------|----------------------|----------------------|------------------|-------|
| Revenue from operations | ₹1,568 Mn (L82/87/97/102) | 15,675.99 (L79) | 1,567.6 | ✓ rounds |
| EBITDA (computed) | ₹1,179 Mn (L87/103) | 15,675.99 − 2,287.55 − 1,099.70 − 498.52 = 11,790.22 (L79/85/86/89) | 1,179.0 | ✓ exact |
| EBITDA margin | 75.2% (L83/87/103/116) | 11,790.22 / 15,675.99 = 75.21% | — | ✓ |
| PBT | ₹586 Mn (L83/87/105/117) | 5,862.64 (L93/96) | 586.3 | ✓ |
| PAT | ₹439 Mn (L87/106) | 4,388.21 (L104) | 438.8 | ✓ |
| Diluted EPS | ₹2.10 (L87/107) | 2.10 (L121) | — | ✓ |
| Depreciation | ₹606 Mn (L109) | 6,064.44 (L87) | 606.4 | ✓ |
| Depreciation QoQ increase | +₹93 Mn (L109) | 6,064.44 − 5,134.64 = 929.80 | +93.0 | ✓ exact |
| 93% of FY26 full-year EBITDA | 93% (L84/90) | FY26 EBITDA 24,558.01 − 6,595.13 − 3,743.11 − 1,593.54 = 12,626.23; 11,790.22 / 12,626.23 = 93.38% | — | ✓ |
| PBT Q4 comparator | ₹86 Mn (L91/105) | 855.82 (L93 col 31-Mar-26) | 85.6 | ✓ |
| PAT margin Q4 comparator | 6.7% (L106) | 643.56 / 9,564.27 = 6.73% | — | ✓ |
| EPS Q4 comparator | ₹0.32 (L91/107) | 0.32 (L121 col 31-Mar-26) | — | ✓ |
| **EBITDA margin QoQ change** | **+1,450 bps (L91)** vs **+1,446 bps (L103)** | Q4 margin 5,810.22/9,564.27 = 60.749%; Q1 75.212%; Δ = **14.463 pp = +1,446 bps** | — | **+1,446 correct; +1,450 WRONG** |
| EBITDA margin YoY change | +4,609 bps (L103) | Q1FY26 margin 1,051.44/3,611.02 = 29.12%; 75.21−29.12 = 46.09 pp | +4,609 | ✓ |
| Revenue YoY / QoQ | +334.1% / +63.9% (L91) | 15,675.99/3,611.02 = 4.341; /9,564.27 = 1.6391 | +334.1% / +63.9% | ✓ |

**Every figure the press release STATES reconciles to the same-day filing.** The forensic signal is not in the stated numbers; it is in (a) the single internal bps inconsistency, now resolved against the filing, and (b) what the release OMITS relative to the filing:

| Omitted from press release | Filing value (Lakhs -> Mn) | Why it matters |
|----------------------------|----------------------------|----------------|
| Other income | 1,142.01 -> ₹114.2 Mn (L80) | ~19% of the headlined PBT (114.2/586.3) is NON-operating other income; release headlines "PBT ₹586 Mn" with no hint. |
| Finance costs | 1,005.15 -> ₹100.5 Mn (L88), +173% QoQ (from 368.04), +449% YoY (from 183.05) | Leverage ramp fully concealed; near-tripling of finance cost QoQ against the GPU capex build. |
| Tax composition | Current tax NIL (L99); tax 100% DEFERRED 1,474.43 (L101) | PAT ₹439 Mn is flattered by zero cash tax; the ₹147 Mn implied charge is entirely deferred (DTA/carryforward consumption). |
| Basic EPS | 2.14 (L120) | Release shows only the lower Diluted ₹2.10; the 0.04 (~1.9%) basic/diluted dilution spread is hidden. |
| Standalone/consolidated label | S = C this quarter (Note 9) | Release does not state whether figures are S or C; benign this quarter, but undisclosed. |

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|------------|----------------|----------------|---------------------|
| P-F6 | F6 | narrative r11 / OH bullet r10, r7 | L118, L107-108, L84/102 | "remain focused on aggressive and judicious capacity expansion through the rest of FY'27" | FORWARD-SIGNAL | Guidance-adjacent capacity-expansion commitment for FY27, no number attached; separately "targeting industry benchmarks for NCCL and Model FLOPs Utilization" = targets not yet achieved. B200 go-live is the one completed milestone. Feed Role 5 promise-vs-delivery. |
| P-F7 | F7 | footnote r3, r2 | L124-125 | "All financial figures for Q1 FY'27 are unaudited and subject to limited review by the Statutory Auditors" | NEUTRAL-FACT | 100% of the beat carries only limited-review (moderate) assurance. Framing "subject to limited review" reads as pending, but the filing's unmodified Limited Review Report is dated the SAME day (results L370-372) — the review was already complete, so the hedge is stale/pre-emptive. |
| P-F8 | F8 | KPI r9 (PBT), r10 (PAT) | L105-106 (release); filing L99/L101 | "PAT: ₹439 Mn ... PBT: ₹586 Mn" | FORWARD-SIGNAL | Implied tax ₹147 Mn -> ETR 25.1% looks normal, but the release conceals that current tax is NIL and the entire charge is DEFERRED (filing 1,474.43 all deferred). PAT flattered by zero cash tax; cash-tax step-up risk once the depreciation/carryforward shield is exhausted. |
| P-F10 | F10 | KPI r34 (diluted EPS) + narrative (split) | L107, L99 (release); filing L120 | "Diluted EPS: ₹2.10 per share" ; "10:1 stock split" | AMBIGUOUS | 10:1 sub-division disclosed (corporate action). Release shows only Diluted ₹2.10 and omits Basic ₹2.14 (filing) — the ~1.9% dilution spread that first surfaced this quarter is hidden. Identify the dilutive instrument (ESOP/warrant) via A4. |
| P-F14 | F14 | KPI r15 vs r26; narrative r12 | L91 vs L103; L120 | "+1,450 bps QoQ" (L91) vs "+1,446 bps QoQ" (L103) | NEUTRAL-FACT | Same metric, two values in one document (A2 NUMERIC_INCONSISTENCY). Cross-doc math resolves it: Q4 60.75% -> Q1 75.21% = +1,446 bps, so the KPI-box +1,450 bps (L91) is the drafting error. Also the commentary is attributed only to "— Management" (L120) with no named CEO/CFO/MD (UNATTRIBUTED_QUOTE), and "Script Symbol" (NSE) vs "Scrip Code" (BSE) mismatch. Cumulative governance/controls data point. |
| P-F15 | F15 | entities r2 / OH bullet r9 | L105-106 | "Incorporated Sovcloud Technologies Limited, a wholly owned subsidiary" | FORWARD-SIGNAL | New consolidation entity, first appearance. Name "Sovcloud" points to a sovereign/government-cloud vehicle. Filing (L227-228, L370-372): incorporated 17-Jun-2026, pre-operational at quarter-end, yet already carries its own unmodified limited-review conclusion (dated 20-Jul) — suggests it may already hold capital/assets. Probe purpose, capex allocation, revenue plan and Q2 FY27 commencement. |
| P-F16 | F16 | KPI r28 (GPUs), narrative r10; omissions vs filing | L117, L104; filing L80/L88 | "utilization across our GPU fleet remains strong" (L117) | AMBIGUOUS | Presentation reframing / selective disclosure. Metrics the Notion monitor tracks are DROPPED or de-quantified: **Exit MRR absent** (Q4 baseline Rs37.4 Cr per company memory) — the #1 monitored recurring-revenue quality metric is not disclosed; **GPU utilisation qualitative only** ("remains strong", no % vs the 80%/60% green/red bands); **realised GPU-hour pricing absent**. The release headlines a +334% revenue surge driven by a single B200 cluster go-live while omitting other income (~19% of PBT) and surging finance costs (+173% QoQ, filing L88). Lean bear: revenue durability (recurring vs one-off B200 burst) and margin quality are unverifiable from the deck. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | N.A. | Press release carries no line-item P&L/BS table -> no ZERO_STANDING nil-lines to interrogate (done in the results-filing pass). |
| F2 | N.A. | Release states a single unlabelled figure set; no standalone-vs-consolidated split to decompose (filing confirms S = C this quarter, gap = 0). |
| F3 | N.A. | No standalone-vs-consolidated cost lines in the release to compare for shell detection (Sovcloud pre-operational per filing Note 9). |
| F4 | N.A. | No auditor's Other Matters paragraph in a press release; filing shows the subsidiary was reviewed (0% unaudited component contribution). |
| F5 | N.A. | No auditor report / Going Concern / EoM paragraph in the release to verbatim-diff. |
| F6 | FINDING | Forward-commitment phrases present: "capacity expansion through the rest of FY'27" (L118), "targeting ... NCCL and MFU" benchmarks (L107-108); B200 go-live completed milestone. |
| F7 | FINDING | Hedge/safe-harbour lexicon present: "subject to" limited review, "may contain forward-looking", "may differ materially" (L124-125) on 100% of KPIs; framing stale vs same-day completed LR. |
| F8 | FINDING | PBT/PAT carried in the deck imply ETR 25.1%, but the release conceals nil current tax / 100%-deferred charge revealed in the filing (L99/L101). |
| F9 | N.A. | Press release carries no OCI line (single-quarter OCI swing finding is in the results-filing pass). |
| F10 | FINDING | 10:1 split disclosed (L99); only Diluted EPS ₹2.10 shown (L107), Basic ₹2.14 (filing L120) omitted -> hidden ~1.9% dilution spread. |
| F11 | N.A. | No reserves / net-worth figure in the release to tie out (filing net worth reconciled in the results pass). |
| F12 | N.A. | No segment table in the release; filing Note 6 = single business segment. |
| F13 | N.A. | This is the press-release transmittal, not the Board-outcome letter; no AR/AGM/record-date/dividend/appointment agenda (covered in the results-filing pass). |
| F14 | FINDING | Within-document numeric inconsistency +1,450 bps (L91) vs +1,446 bps (L103) — resolved to +1,446 via cross-doc math; plus unattributed "— Management" quote (L120) and Script/Scrip mismatch. |
| F15 | FINDING | Entity diff: Sovcloud Technologies Limited, new wholly owned subsidiary, first appearance (L105-106). |
| F16 | FINDING | Dropped/reframed presentation disclosures: Exit MRR absent, GPU utilisation qualitative-only, realised pricing absent; other income and surging finance costs omitted vs same-day filing. |
| F17 | N.A. | No concall transcript in scope for this doctype; silence audit deferred to the concall pass. |

Counts: FINDING x7 (F6, F7, F8, F10, F14, F15, F16); N.A. x10 (F1, F2, F3, F4, F5, F9, F11, F12, F13, F17); PASS x0. No blanks — **GATE A3 satisfied**.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/slide ref | status word |
|------------|--------------|----------------|-------------|
| B200 cluster go-live and revenue contribution | achieved in Q1 FY27 | subheadline L84 / OH bullet L102 | completed |
| Capacity expansion "through the rest of FY'27" | by 31-Mar-2027 | mgmt quote L118 | underway |
| Target industry benchmarks for NCCL & Model FLOPs Utilization (MFU) | ongoing FY27 | OH bullet L107-108 | initiated |
| Sovcloud Technologies Limited incorporated (WOS); commence operations | incorporated 17-Jun-2026 (per filing); ops post 30-Jun-2026, watch Q2 FY27 | OH bullet L105-106 | completed (incorporation) / initiated (operations) |
| Investing in organisational capability / team strengthening | ongoing | OH bullet L110 | underway |
| 10:1 equity share sub-division | effective, record date 05-Jun-2026 (per filing) | FPO L99 | completed |
| Direct BSE Main Board listing | effective 12-Jun-2026 (per filing) | FPO L99 | completed |

---

## FORWARD NARRATIVE (context weighed, not anchored — Notion checklist targeting)

The press release is a clean, internally consistent beat on the numbers it chooses to show, but it is a curated subset of the same-day filing. Three things the filing carries and the deck drops define the forward tension: (1) **recurring-revenue quality** — Exit MRR (Notion item 1, Rs37.4 Cr in Q4) is not disclosed and GPU utilisation (Notion item 6) is reduced to "remains strong," precisely when a single B200 cluster go-live is credited with the +334% YoY / +64% QoQ surge, leaving recurring-vs-one-off durability unverifiable; (2) **cost of the capex ramp** — depreciation ₹606 Mn (Dep/EBITDA ~51%) and finance costs ₹100.5 Mn (+173% QoQ, filing only) are climbing fast while current tax is nil, so reported PAT is flattered by both the deferred-tax shield and undisclosed other income (~19% of PBT); (3) **structure** — a new "Sovcloud" sovereign-cloud subsidiary already reviewed despite zero operations. The B200 go-live confirms the Blackwell-anchor watch item positively (Notion item 3), and EBITDA margin 75.2% clears the 64% guide (item 9). These feed A4 as management questions, not conclusions; conservative bias applied on F10 and F16.

Findings flagged to A4 (FORWARD-SIGNAL + AMBIGUOUS): **P-F6, P-F8, P-F15** (forward-signal); **P-F10, P-F16** (ambiguous).

---

```yaml
stage: A3-forensics
company: "E2E"
quarter: "q1fy27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/e2e-q1fy27/work/forensics_e2e_q1fy27_presentation.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "P-F6", check: "F6", line: "118", classification: "FORWARD-SIGNAL", implication: "FY27 capacity-expansion + NCCL/MFU benchmark targets, no numbers; B200 go-live completed milestone"}
  - {id: "P-F7", check: "F7", line: "124-125", classification: "NEUTRAL-FACT", implication: "100% of beat is limited-review only; 'subject to limited review' framing stale vs same-day completed LR report"}
  - {id: "P-F8", check: "F8", line: "105-106", classification: "FORWARD-SIGNAL", implication: "Release hides nil current tax / 100%-deferred charge (filing L99/L101); PAT flattered, cash-tax step-up risk"}
  - {id: "P-F10", check: "F10", line: "107,99", classification: "AMBIGUOUS", implication: "10:1 split; only diluted EPS 2.10 shown, basic 2.14 omitted -> ~1.9% dilution spread hidden; identify instrument"}
  - {id: "P-F14", check: "F14", line: "91,103", classification: "NEUTRAL-FACT", implication: "+1,450 vs +1,446 bps one-doc inconsistency; cross-doc math resolves to +1,446; unattributed 'Management' quote"}
  - {id: "P-F15", check: "F15", line: "105-106", classification: "FORWARD-SIGNAL", implication: "New WOS Sovcloud (sovereign-cloud); pre-operational yet separately reviewed; probe purpose/capex/Q2 commencement"}
  - {id: "P-F16", check: "F16", line: "117,104", classification: "AMBIGUOUS", implication: "Exit MRR dropped, GPU utilisation qualitative-only, pricing absent; other income & +173% QoQ finance costs omitted vs filing; revenue durability/quality unverifiable"}
forward_signals: ["P-F6", "P-F8", "P-F15"]
ambiguous: ["P-F10", "P-F16"]
commitments:
  - {commitment: "B200 cluster go-live and revenue contribution", implied_date: "Q1 FY27 (achieved)", ref: "L84/L102", status_word: "completed"}
  - {commitment: "Capacity expansion through the rest of FY'27", implied_date: "2027-03-31", ref: "L118", status_word: "underway"}
  - {commitment: "Target NCCL & MFU industry benchmarks", implied_date: "FY27 (ongoing)", ref: "L107-108", status_word: "initiated"}
  - {commitment: "Sovcloud Technologies Limited incorporated; commence operations", implied_date: "incorporated 2026-06-17; ops Q2 FY27", ref: "L105-106", status_word: "initiated"}
  - {commitment: "Investing in organisational capability / team strengthening", implied_date: "ongoing", ref: "L110", status_word: "underway"}
  - {commitment: "10:1 equity share sub-division", implied_date: "2026-06-05", ref: "L99", status_word: "completed"}
  - {commitment: "Direct BSE Main Board listing", implied_date: "2026-06-12", ref: "L99", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
