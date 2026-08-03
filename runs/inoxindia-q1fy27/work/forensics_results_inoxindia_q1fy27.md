# A3 FORENSIC NOTES — INOX India (INOXINDIA / INOXCVA) — Q1 FY27 — Doctype: RESULTS

Source A1 extract: `extract_results_inoxindia_q1fy27.txt` (11 pages, 675 lines).
Source A2 ledger: `ledger_results_inoxindia_q1fy27.md`.
Unit convention: figures in the statement tables are Rs Lakhs (x0.01 = Rs Cr); the
Press Release (Annexure-2) is natively Rs Crores (`UNIT_SWITCH`).
Ledger reconciliation: 100% — every ledger row read at its cited line before judging.
Prior-quarter extract: NOT FOUND (`NO_PRIOR_LEDGER`); all quarter-over-quarter
verbatim diffs (F5, F15) unexecutable this cycle and flagged accordingly.

Doctype applicability: F1-F15 apply; F16 and F17 are N.A. on a results filing. The
Press Release inside this filing bundle (Board agenda item 2) is assessed and its
inconsistencies vs the audited-format statement are routed to F14.

---

## HEADLINE (read F14 first)

The Press Release presents **"PAT ₹ 61 Cr, 0% YoY, 15.9% margin"** (lines 597, 673).
The consolidated statement's actual **PAT is Rs 58.07 Cr** (line 242, 5,807.20 L),
**down ~5% YoY** from Rs 61.12 Cr (Q1 FY26, 6,111.79 L). The number the Press Release
labels "PAT" (Rs 61 Cr) equals **Total Comprehensive Income** (line 253, 6,054.12 L =
Rs 60.54 Cr), which is buoyed Rs 2.47 Cr by an OCI actuarial + FX gain (F9). Real
earnings declined; the headline reads flat only because OCI was substituted for PAT.
This is the single most important forward-signal in the filing.

---

## FINDINGS TABLE

| id | F# | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|----|----------------|------|----------------------|----------------|---------------------|
| F-01 | F1 | Zero-Standing tbl 8, rows 2-4 | 257, 260, 264 | "Non-controll Ing Interests … -" | NEUTRAL-FACT | Three standing NCI lines (nil all 4 periods) keep the consolidation template ready for a minority/JV structure not yet present; watch the WAYOUT Sweden (line 640) and semiconductor tie-ups for a future partly-owned entity. Captive Consumption (233/463) and standalone OCI-A (474) are benign structural nils. |
| F-02 | F2 | Line items §6/§7, PAT rows | 242 vs 472 | "5,807.20 … 5,636.82" | FORWARD-SIGNAL | Consolidated-minus-standalone PAT gap widened YoY 1.20%→3.02% of standalone PAT (+1.82pp, below the 5pp mechanical trigger) BUT subsidiary PAT contribution more than doubled: Rs 0.72 Cr→Rs 1.70 Cr (+136% YoY). Brazil operation is scaling; a first-class metric per mandate. |
| F-03 | F3 | Entities tbl 4 row c; auditor para 6 | 139, 160-164 | "INOXCYA Europe B.Y. - Wholly Owned subsidiary" | AMBIGUOUS | Only ONE subsidiary (Rs 1,332 L revenue) is separately quantified in the Other-Matter para; consolidated-standalone revenue gap is Rs 13.79 Cr vs that sub's Rs 13.32 Cr, leaving ~Rs 0.47 Cr for INOXCVA Europe B.V. — consistent with a near-dormant holding/finance shell. Purpose of the Europe B.V. is undisclosed. |
| F-04 | F4 | Auditor para 6 (`MGMT_FURNISHED`) | 160-170 | "has been furnished to us by the Management" | NEUTRAL-FACT | Rs 164.19 L subsidiary PAT = 2.83% of consolidated PAT rests on a component-auditor report obtained via Management, not independently by the principal auditor. Below the 10% trigger and opinion unmodified; monitor if Brazil scales (F-02) and this reliance grows. No YoY trend possible (`NO_PRIOR_LEDGER`). |
| F-06 | F6 | Notes 3 & 7; Press Release | 334, 623 | "will recognise the consequential impact, if any" | FORWARD-SIGNAL | Dated/dateable management commitments extracted — see Commitment Register. Milestone language: Bahamas mini-LNG "Installation activities commenced" (623); labour-code impact "will recognise … based on such developments" (334/551). Feeds Role 5 promise-vs-delivery tracker. |
| F-08 | F8 | Tax rows, "earlier years (credit)" | 241, 471 | "(3) TalC adjustment pertaining to earlier years (credIt) (70.46)" | NEUTRAL-FACT | Non-zero earlier-years tax credit of Rs 70.46 L (both cons + SA) = F8 auto-FINDING. Cut consolidated Q1 ETR to 23.17% vs 25.17% statutory (~93bps shield); normalized ETR ~24.1%. One-off; Q1 PAT flattered ~Rs 0.70 Cr. |
| F-09 | F9 | OCI remeasurement row | 247, 251 | "(li Re-measurement gain/(Ioss) … 211.42" | AMBIGUOUS | Single-quarter actuarial OCI gain of Rs 211.42 L exceeds the entire prior full-year remeasurement of Rs (40.09) L = assumption change (discount rate / New Labour Codes gratuity+leave, note 7). Verify assumptions at Annual Report. This gain is the buffer bridging the F-14 PAT/TCI substitution. |
| F-11 | F11 | Other Equity + Paid-up | 271 vs 489 | "1,09,945.58 … 1,12,052.40" | AMBIGUOUS | Consolidated net worth Rs 1,117.61 Cr is BELOW standalone Rs 1,138.68 Cr by Rs 21.07 Cr (1.85% of SA NW). Below the 5% trigger, but the sign inversion says overseas subs are cumulatively net-negative to group equity (historical losses / negative FX translation reserve, cf. wound-up CVA US). Watch whether growing Brazil profits rebuild the gap. |
| F-12 | F12 | Note 4 single-segment; PR `SEGMENT_PCT_GAP` | 288, 610-627 | "only one reportable business segment" | AMBIGUOUS | Single Ind AS segment → NO segment asset/liability disclosure (equity-funded-build test cannot be run). Press-release division shares 53%+22%+20% = 95%; the Stainless-Steel Keg + residual ~5% is NOT stated. Keg volume (Notion tripwire #4, red at flat 10-12k) is described qualitatively (Heineken/AB InBev/Molson Coors) with NO volume or revenue number. |
| F-14 | F14 | Press Release vs consolidated statement | 597, 673 vs 242, 253 | "PAT for Q1 FY27 stood at ₹ 61 Cr with PAT Margin of 15.9%" | AMBIGUOUS | Press Release "PAT Rs 61 Cr / 0% YoY / 15.9%" = consolidated TCI (Rs 60.54 Cr, line 253), NOT PAT (Rs 58.07 Cr, line 242). Real PAT DOWN ~5% YoY (61.12→58.07 Cr). Also: PR "Revenue Rs 382 Cr" = Total Income (incl Rs 10.81 Cr other income), not Revenue from Operations (Rs 370.79 Cr); PR "EBITDA Rs 90 Cr" does not tie to statement-derived EBITDA ~Rs 86.7 Cr (~Rs 3.3 Cr unreconciled). Minor: deferred-tax label "Charge/(Credit)" (240) vs "Charge" (470). Headline-vs-reported earnings-quality divergence. |
| F-15 | F15 | Entities tbl 4; notes 5/6 | 136-139, 291, 307 | "erstwhile USA 5ubsidJ.ry, I.e. CryOienic Vessels Alterniltilles Inc" | NEUTRAL-FACT | Consolidation list = 3 (Holding + Brazil Ltda + Europe B.V.). Cannot diff vs prior quarter (`NO_PRIOR_LEDGER`) — additions/renames/relationship changes unverifiable this cycle. Confirmed historical deletion: CVA Inc (US) wound up FY20, now "erstwhile." A4 should source the prior filing for an entity-stability check. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1  | FINDING | 6 `ZERO_STANDING` rows explained; 3 standing NCI lines (257/260/264) anticipate a minority/JV structure not yet present — mild forward signal; captive-consumption (233/463) and standalone OCI-A (474) benign structural nils. |
| F2  | FINDING | S-vs-C PAT gap 1.20%→3.02% of SA PAT (+1.82pp, below 5pp trigger) but subsidiary PAT contribution +136% YoY (Rs 0.72→1.70 Cr); Brazil scaling. First-class metric per mandate. |
| F3  | FINDING | Only one subsidiary quantified (Rs 1,332 L rev); Europe B.V. residual ~Rs 0.47 Cr revenue → near-dormant holding shell; no going-concern EoM present. |
| F4  | FINDING | Unaudited/`MGMT_FURNISHED` component contribution = Rs 164.19 L = 2.83% of consolidated PAT, below 10% trigger; report furnished by Management, opinion unmodified. |
| F5  | PASS | Both review reports clean/unmodified — no Emphasis of Matter, no Going Concern, no qualification (paras 5 cons / 4 SA). No EoM to scope-track; prior-quarter verbatim diff impossible (`NO_PRIOR_LEDGER`). |
| F6  | FINDING | Forward-commitment lexicon hits in notes 3, 7 and Press Release (Bahamas "commenced", CERN/ITER/space orders "secured", labour codes "will recognise"). See Commitment Register. |
| F7  | PASS | Only contractual "subject to" (ESOP, note 3) and mild "if any" (note 7) hedges; no newly-added revenue-lumpiness or customer-concentration hedge in the notes. |
| F8  | FINDING | Earlier-years tax credit Rs 70.46 L non-zero (241/471) = auto-FINDING; consolidated ETR 23.17% vs 25.17% statutory (~93bps one-off shield). |
| F9  | FINDING | Q1 actuarial OCI gain Rs 211.42 L exceeds full prior-year remeasurement Rs (40.09) L = assumption change; verify at AR. |
| F10 | PASS | Paid-up capital Rs 1,815.27 L unchanged all 4 periods; basic-vs-diluted spread stable Rs 0.02/qtr; ESOP options exist (note 3) but no widening. |
| F11 | FINDING | Consolidated NW (Rs 1,117.61 Cr) BELOW standalone NW (Rs 1,138.68 Cr) by Rs 21.07 Cr (1.85%, below 5% trigger); sign inversion = cumulative subsidiary equity erosion. |
| F12 | FINDING | Single reportable segment → no segment asset/liability data; press-release division shares sum to 95% (`SEGMENT_PCT_GAP`); keg volume undisclosed. |
| F13 | PASS | Board agenda = 2 items only (results+LRR, press release); meeting 04:20-04:38 (18 min). No AR/AGM/record-date/dividend/director/capital-raise resolution — routine quarterly outcome, no Role 6 AR event triggered. |
| F14 | FINDING | Press Release "PAT Rs 61 Cr / 0% YoY" = TCI, not PAT (real PAT Rs 58.07 Cr, -5% YoY); "Revenue" = Total Income; EBITDA Rs 90 Cr unreconciled vs ~Rs 86.7 Cr; deferred-tax label mismatch. |
| F15 | FINDING | 3-entity list; cannot diff vs prior quarter (`NO_PRIOR_LEDGER`); erstwhile CVA US noted as wound-up. |
| F16 | N.A. | Results filing; no investor presentation. Press-release omissions captured under F12/F14. |
| F17 | N.A. | Results filing; no concall transcript. Monitoring-checklist silences noted below for A4. |

GATE A3: pass — every check carries exactly one status; no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/PR ref | status word |
|------------|--------------|-------------|-------------|
| Recognise further New Labour Codes impact ("if any") | upon State Rules finalisation (undated) | Note 7 — line 334 (cons) / 551 (SA) | underway |
| ESOP options vest (3,64,895 / 7,593 / 2,267) | end of 2nd/3rd year from grant (Aug-2023, Feb-2025, Feb-2026 grants) | Note 3 — line 283 (cons) / 503 (SA) | underway |
| Bahamas mini-LNG terminal: install first batch of large storage tanks | in progress (Q1 FY27) | Press Release — line 623 | commenced |
| Space-exploration large cryogenic tanks + "six additional tanks from same customer" | Q1 FY27 secured; delivery forward | Press Release — line 611-612 | initiated |
| CERN cryogenic modules order; ITER France repeat order | Q1 FY27 secured; execution forward | Press Release — line 628-632 | secured/repeat |
| Semiconductor transportation tanks, Dholera facilities | "initial orders" secured | Press Release — line 615-616 | initiated |
| WAYOUT (Sweden) modular water micro-factories in India | partnership entered Q1 FY27 | Press Release — line 640-642 | initiated |
| AS9100D aerospace quality certification | received | Press Release — line 643-645 | completed |

---

## KEY COMPUTATIONS (auditable)

F2 — S-vs-C PAT gap (Cr, consolidated minus standalone):
- Q1 FY27: 58.07 − 56.37 = 1.70 (3.02% of SA PAT) | Q1 FY26: 61.12 − 60.40 = 0.72 (1.20%) | Q4 FY26: 75.24 − 74.28 = 0.95 (1.28%) | FY26: 257.89 − 252.39 = 5.50 (2.18%). YoY Q1 change +1.82pp (< 5pp trigger); sub PAT contribution +136% YoY.
- Revenue gap Q1 FY27 = 370.79 − 357.00 = 13.79 Cr; note-6 subsidiary revenue = 13.32 Cr → Europe B.V. + eliminations ≈ 0.47 Cr.
- Cost deltas (cons − SA, Cr): materials +6.48, employee +2.80, depreciation +1.33, finance +0.17 → subs (chiefly Brazil) DO operate (not identical cost lines; not a full shell set).

F4 — unaudited contribution: 164.19 / 5,807.20 = 2.83% of consolidated PAT.

F8 — ETR (consolidated): Q1 FY27 (1,763.49+58.33−70.46)/7,558.56 = 23.17%; ex-earlier-years-credit = 24.10%. Q1 FY26 24.09%; FY26 24.57%.

F9 — remeasurement OCI (cons L): Q1 FY27 +211.42 vs FY26 full-year (40.09); TCI−PAT = 246.92 L (2.47 Cr total OCI = 2.11 actuarial + 0.89 FX, net of tax).

F11 — net worth (FY26 column): consolidated 1,09,945.58 + 1,815.27 = 1,11,760.85 L (Rs 1,117.61 Cr); standalone 1,12,052.40 + 1,815.27 = 1,13,867.67 L (Rs 1,138.68 Cr); inversion Rs 21.07 Cr.

F14 — press-release map: "PAT 61" = TCI 6,054.12 L (60.54 Cr); actual PAT 5,807.20 L (58.07 Cr); Q1 FY26 PAT 6,111.79 L (61.12 Cr) → real PAT −4.99% YoY. "Revenue 382" = Total Income 38,159.54 L (381.60 Cr) not Rev-from-ops 370.79 Cr. EBITDA: statement-derived (PBT-pre-exceptional 7,558.56 + Dep 949.96 + Finance 159.15) = 8,667.67 L (86.68 Cr) vs PR 90 Cr → ~3.3 Cr unreconciled.

---

## MONITORING CROSS-REFERENCE (Notion lens — not evidence; for A4)

- Order book Rs 1,686 Cr (line 599/606) > Notion green Rs 1,500 Cr — GREEN; export order book Rs 1,140 Cr; inflow Rs 532 Cr ("highest-ever quarterly").
- EBITDA margin 23.5% (PR) / ~22.7% statement-basis — both > 20% tripwire — GREEN.
- Audit trail / Rule 11(g): quarterly LRR carries no Rule 11(g) commentary (an annual-audit matter); no qualification visible — cannot confirm ITGC remediation from this doc (silence, inherent to Reg 33 quarterly).
- Contract Assets / Revenue tripwire, CFO/PAT, ROCE, RPT with INOX Air Products (~11.6%), promoter royalty Rs 32.65 Cr: NONE disclosed in a quarterly Reg 33 filing (no balance sheet / cash flow / RPT schedule) — structural silence; assessable only at half-year / Annual Report. A4 to carry forward.
- Beer keg volume (tripwire #4): qualitative only, NO volume figure (F-12).

---

```yaml
stage: A3-forensics
company: "INOXINDIA"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/inoxindia-q1fy27/work/forensics_results_inoxindia_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F-01", check: "F1", line: "257,260,264", classification: "NEUTRAL-FACT", implication: "Standing NCI lines anticipate a minority/JV structure not yet present; watch WAYOUT/semiconductor tie-ups"}
  - {id: "F-02", check: "F2", line: "242", classification: "FORWARD-SIGNAL", implication: "Subsidiary (Brazil) PAT contribution +136% YoY; consolidated uplift scaling"}
  - {id: "F-03", check: "F3", line: "139,160", classification: "AMBIGUOUS", implication: "INOXCVA Europe B.V. appears near-dormant holding shell; purpose undisclosed"}
  - {id: "F-04", check: "F4", line: "160", classification: "NEUTRAL-FACT", implication: "2.83% of consolidated PAT on a Management-furnished component report; monitor as Brazil scales"}
  - {id: "F-06", check: "F6", line: "334,623", classification: "FORWARD-SIGNAL", implication: "Dated management commitments (labour codes, Bahamas LNG, CERN/ITER/space/semi orders) feed promise-vs-delivery tracker"}
  - {id: "F-08", check: "F8", line: "241", classification: "NEUTRAL-FACT", implication: "Rs 70.46 L earlier-years tax credit is one-off; normalized ETR ~24%, Q1 PAT flattered ~Rs 0.7 Cr"}
  - {id: "F-09", check: "F9", line: "247", classification: "AMBIGUOUS", implication: "Q1 actuarial OCI gain exceeds full prior year = assumption change; verify discount rate at AR; it bridges the F-14 PAT/TCI gap"}
  - {id: "F-11", check: "F11", line: "271", classification: "AMBIGUOUS", implication: "Consolidated NW below standalone by Rs 21.07 Cr = cumulative subsidiary equity erosion; watch reversal as Brazil earns"}
  - {id: "F-12", check: "F12", line: "288", classification: "AMBIGUOUS", implication: "Single segment hides asset/liability build; keg revenue share and volume undisclosed (tripwire #4)"}
  - {id: "F-14", check: "F14", line: "597", classification: "AMBIGUOUS", implication: "Headline PAT = TCI, masking ~5% real PAT decline; revenue = total income; EBITDA unreconciled; earnings-quality divergence"}
  - {id: "F-15", check: "F15", line: "136", classification: "NEUTRAL-FACT", implication: "Entity list cannot be diffed vs prior quarter (NO_PRIOR_LEDGER); A4 to source prior filing"}
forward_signals: ["F-02", "F-06"]
ambiguous: ["F-03", "F-09", "F-11", "F-12", "F-14"]
commitments:
  - {commitment: "Recognise further New Labour Codes impact (if any)", implied_date: "upon State Rules finalisation", ref: "Note 7 / line 334", status_word: "underway"}
  - {commitment: "ESOP options vest (3,64,895/7,593/2,267)", implied_date: "2nd/3rd year from Aug-2023/Feb-2025/Feb-2026 grants", ref: "Note 3 / line 283", status_word: "underway"}
  - {commitment: "Bahamas mini-LNG: install first batch of large storage tanks", implied_date: "in progress Q1 FY27", ref: "PR / line 623", status_word: "commenced"}
  - {commitment: "Space-exploration cryogenic tanks + six additional tanks", implied_date: "Q1 FY27 secured, delivery forward", ref: "PR / line 611", status_word: "initiated"}
  - {commitment: "CERN cryogenic modules + ITER repeat order", implied_date: "Q1 FY27 secured, execution forward", ref: "PR / line 628", status_word: "secured"}
  - {commitment: "Semiconductor transportation tanks, Dholera", implied_date: "initial orders secured Q1 FY27", ref: "PR / line 615", status_word: "initiated"}
  - {commitment: "WAYOUT Sweden modular water micro-factories in India", implied_date: "partnership entered Q1 FY27", ref: "PR / line 640", status_word: "initiated"}
  - {commitment: "AS9100D aerospace certification", implied_date: "Q1 FY27", ref: "PR / line 643", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
