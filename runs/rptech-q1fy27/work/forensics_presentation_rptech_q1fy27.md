# A3 FORENSIC NOTES — Investor Presentation — RPTECH (Rashi Peripherals Ltd) — Q1 FY27

Doctype: presentation (23-page Q1 FY27 investor deck; page 1 = BSE/NSE Reg 30(6)
covering letter). Source extract: `extract_presentation_rptech_q1fy27.txt`.
Ledger reconciled: 265/265 gated rows read verbatim at cited lines (100%).
Model: claude-opus-4-8. Conservative bias applied; direction-uncertain items
lean bear and generate an A4 question rather than self-resolve.

Applicability note (per prompt line 128-131): on a presentation F16 is the
primary check plus any F6/F10/F11 numbers the deck carries. This deck is
unusually financials-heavy (full standalone + consolidated quarterly IS, a
historical consolidated IS and balance sheet, and a working-capital /
cash-flow / returns chart page), so F1, F2, F8, F9, F11, F14 are ALSO
evaluable from deck content and were run. Auditor-report / EoM / entity-list /
concall checks (F3, F4, F5, F12, F13, F15, F17) have no deck substrate and are
marked N.A. with basis.

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1 | F1 | ZS-1 / P17-9 | slide 16, line 578 | "Exceptional Item — - - - (NA)" | FORWARD-SIGNAL | Dormant exceptional-item line retained (FY24 104 / FY25 26 were live, P19-8 line 643). With the board-approved Embedded-Business slump sale to Rashi Semiconductor entities and the 67% VDA Infosolutions buy both pending (Notion), this line is the template slot a reorganisation gain/loss will land in next 1-2 quarters. |
| F2 | F2 | P16-10 / P17-12 / P16-1 / P17-1 | slides 15-16, lines 552, 581, 534, 570 | "PAT 972 (standalone) … 1,046 (consolidated)" | FORWARD-SIGNAL | Consolidated-minus-standalone PAT gap as % of standalone PAT swings 4.93% (Q1FY26) → 14.21% (Q4FY26) → 7.61% (Q1FY27); both step-changes exceed the 5pp FINDING threshold. Subsidiary PAT contribution is large and volatile before VDA even consolidates. Subsidiary EBITDA rose 15 → 91 Mn YoY (Q1FY26 → Q1FY27). |
| F6 | F6 | P12-2 / P12-3 | slide 11, lines 428-430, 432-433 | "strategic investment in VDA Infosolutions, marking a significant step towards forward integration"; "Entered a strategic partnership with WEKA.io to expand capabilities in AI infrastructure" | FORWARD-SIGNAL | Two dateable but unquantified catalyst commitments: VDA (managed IT services / lifecycle — forward integration into higher-WC services) and WEKA.io (AI infrastructure — maps to Notion catalyst "AI DC pipeline"). No size, margin, timeline, or WC impact given in the deck. |
| F8 | F8 | P17-11 / P20-9 | slides 16 & 19, lines 580, 681 | "Tax Expense 344 … 84.9% [YoY]"; "Deferred Tax Assets (Net) … FY26 -" | FORWARD-SIGNAL | Consolidated ETR 24.75% (344/1,390) vs 23.16% (Q1FY26) = +159bps YoY step-up, and net DTA is fully exhausted by FY26 (59→68→19→nil, FY23-26). The tax shield that held consol ETR ~1-3pp below the 25.17% statutory rate (FY25 21.96%, FY26 23.97%) is gone; future ETR normalises up → PAT-growth headwind not visible in the 65-69% headline. |
| F9 | F9 | P17-14 / P19-13 / P16-12 | slides 16 & 18, lines 583, 653, 556 | "Other Comprehensive Income 41 … NA" | AMBIGUOUS | Consolidated OCI swings to +41 Mn in one quarter, exceeding the entire FY26 OCI of (30) and flipping sign; standalone OCI is only (2), so the +43 delta is a consolidation-only item (Singapore Pte subsidiaries → most likely FX translation reserve, possibly an actuarial/discount-rate assumption change). Direction uncertain → A4 question; verify FCTR vs actuarial split at the Annual Report. |
| F14 | F14 | FN-1 / FN-2 / P9-3 / P6-5 | slide 2, lines 131-132; slide 8 line 317; slide 5 line 222 | "All figures as on Q1-FY27" vs "* Figures as on FY26" | NEUTRAL-FACT | Cumulative drafting inconsistency: two footnotes with conflicting scope on the same "at a Glance" slide (blanket "as on Q1-FY27" vs the CAGR / Net-D/E tiles being FY26-dated); "706 Locations" (exact) vs "700+" (rounded) across slides; "80" vs "80+" brands. Individually immaterial; cumulatively a disclosure-hygiene data point. |
| F16-A | F16 | P21-21..23 / Table 6 CFO row | slide 20, lines 730, 733, 741, 745 | "Cash Flow from Operation (INR Mn) … 1,137 … -1,020 … -2,992" | AMBIGUOUS | THE binding-gate finding. (i) NO Q1-FY27 CFO is disclosed anywhere in the deck — the cash-conversion metric that gates this quarter is absent while the favourable WC-days chart (73→56) is shown prominently. (ii) The deck's highest annual CFO across FY24-FY26 is 1,137 Mn = ₹113.7 Cr, which does NOT reconcile to the Notion thesis's FY26 CFO of ₹514 Cr (a ~₹400 Cr / 4.5x gap) — either a definitional/scope difference (standalone vs consol, gross vs post-tax) or a prior-work error. (iii) Year mapping is AMBIGUOUS_LAYOUT (indent-only). Resolve against the PDF image + results filing before any HOLD/TRIM branch call. |
| F16-B | F16 | (deck omission vs Notion) | whole deck; cf. Notion lines 85-90 | deck contains no reference to slump sale / Restar JV | FORWARD-SIGNAL | The deck OMITS two board-approved forward actions carried in the same filing batch: the Embedded-Business slump sale into Rashi Semiconductor Solutions (Pvt + Pte) and the proposed JV with Restar Corporation (Japan). Selective-disclosure reframing: the reorganisation that seeds the "semiconductor subsidiary scaling" catalyst (Notion checklist #8) is invisible in the IR deck. Also segment-level YoY is not computable (no Q1-FY26 PES/LIT split, only FY24-26 + latest quarter). |

---

## 2. CHECKLIST SCORECARD (all 17, one status each — GATE A3)

| # | Status | One-line basis |
|---|---|---|
| F1 | FINDING | ZS-1 Exceptional Item dash in all 3 shown periods (line 578) but live FY24/FY25; reorganisation pending — dormant, not dead. |
| F2 | FINDING | S-vs-C PAT gap swings 4.93%→14.21%→7.61% of standalone PAT across the three periods shown (>5pp). |
| F3 | N.A. | Shell detection needs entity-level cost lines / Going-Concern EoM; a presentation carries neither (only aggregate S vs C). |
| F4 | N.A. | No auditor's report / Other-Matters paragraph exists in an investor presentation. |
| F5 | N.A. | No Going-Concern / EoM language in a deck, and no prior-quarter deck supplied for a verbatim diff. |
| F6 | FINDING | VDA Infosolutions + WEKA.io forward-integration commitments (lines 428-433) plus 5 unquantified growth pillars (slide 10). |
| F7 | PASS | Only generic safe-harbor hedges present ("subject to known and unknown risks", line 763); no newly-added lumpiness/concentration hedge. |
| F8 | FINDING | Net DTA exhausted by FY26 (line 681); consol ETR +159bps YoY (line 580) → ETR step-up risk. |
| F9 | FINDING | Consol OCI +41 in one quarter > full-year FY26 (30), sign flip; standalone OCI only (2) → consolidation/FX item. |
| F10 | PASS | Paid-up equity capital flat at 330 Mn FY24-FY26 (line 668, P20-21); no corporate action in window; deck shows only diluted EPS (no basic → no spread to test). |
| F11 | PASS | Paid-up 330 + Other Equity 19,921 + NCI 112 = Total Equity 20,363 (line 673) ties exactly; Net D/E (9,586−812)/20,363 = 0.43x reconciles P3-9. |
| F12 | N.A. | Deck discloses PES/LIT segment REVENUE only (slide 9); no segment assets/liabilities → asset-build / liability-unwind test not evaluable. |
| F13 | N.A. | No board-outcome / AGM notice / director-term content in the deck; board actions live in the separate results & press-release filings (see F16-B). |
| F14 | FINDING | Footnote scope conflict FN-1 vs FN-2 (lines 131-132) + 700+/706 + 80/80+ inconsistencies. |
| F15 | N.A. | No consolidation entity list in the deck and no prior-quarter deck; additions/deletions not diffable here. |
| F16 | FINDING | No Q1-FY27 CFO disclosed; deck FY26 CFO ₹113.7 Cr vs Notion ₹514 Cr unreconciled; board slump sale + Restar JV omitted (F16-A, F16-B). |
| F17 | N.A. | Concall/transcript-specific; this is a deck. The deck-level silence audit vs the Notion checklist is folded into F16 and Section 4 below. |

Counts: 7 FINDING, 3 PASS, 7 N.A. = 17. No blanks. GATE A3: pass.

---

## 3. COMMITMENT REGISTER (from F6)

| commitment | implied date | note / slide ref | status word |
|---|---|---|---|
| Strategic investment in VDA Infosolutions — "forward integration" into managed IT services, solution implementation, lifecycle support | none stated in deck (67% for ₹368.5 Cr per Notion 02-Jul-26; path to 100%) | slide 11, lines 428-430 | initiated |
| Strategic partnership with WEKA.io — AI infrastructure & high-performance workload management | none stated | slide 11, lines 432-433 | completed (partnership "Entered") |
| Two new branches — Udaipur (Rajasthan) + Dhule (Maharashtra), Tier-2 expansion | done this quarter | slide 11, lines 435-437 | completed |
| Growth pillar: Expand into high-growth verticals | none (qualitative) | slide 10, lines 398-406 | intended |
| Growth pillar: Introduce new adjacent product segments | none | slide 10, lines 401-406 | intended |
| Growth pillar: Forge strategic OEM partnerships | none | slide 10, lines 407-415 | intended |
| Growth pillar: Accelerate market penetration (new geographies) | none | slide 10, lines 407-415 | intended |
| Growth pillar: Solution-based selling to lift wallet share per partner | none | slide 10, lines 407-415 | intended |

No commitment in this deck carries a numeric target or a date. Status-change
tracking (initiated→underway→completed) is not evaluable without the prior-quarter
deck; flagged for A4/Role-5 promise-vs-delivery once Q4 FY26 deck is sourced.

---

## 4. CASH-CONVERSION THESIS-GATE EXTRACTION & NOTION CHECKLIST COMPARISON

Every working-capital / cash-conversion / returns metric the deck volunteers,
extracted verbatim with cite, compared to the Notion green/red thresholds
(Notion lines 44-56). This is the binding gate for Q1 FY27.

| Notion metric (green / red) | Deck value + cite | Verdict | Note |
|---|---|---|---|
| 1. CFO/PAT TTM (>1.0 / <0.5) | **NOT DISCLOSED** — no Q1-FY27 CFO anywhere | **SILENT — GATE UNMET BY DISCLOSURE** | CFO shown only as FY24-26 annual bars (line 733 "1,137", 741 "-1,020", 745 "-2,992"), no current-quarter figure → CFO/PAT uncomputable from deck. |
| 2. Working Capital Days (≤58 / >65) | "56" (slide 17, line 610, unambiguous P18-8); FY26 "58" (slide 20, line 734) | GREEN | Q1FY26→Q1FY27 73→56 (lines 608→610). |
| 3. Debtor Days (≤50 / >55) | "41" (slide 17, line 598, P18-4) | GREEN | Q1FY26 value 53/55 carries AMBIGUOUS_LAYOUT; Q1FY27 41 is clear. |
| 4. ROCE annualised (>17 / <14) | FY26 "16.02%" (slide 20, line 737); no Q1-FY27 ROCE | AMBER + partial silence | FY24/FY25 12.79%/12.74% (LAYOUT_RECONSTRUCTED); current-quarter ROCE not given. |
| 5. Revenue ex-project YoY (>20 / <10) | Consol headline +61.9% (line 570); ex-project basis NOT disclosed | GREEN headline / SILENT on ex-project | Notion's key growth screen is ex-project; deck gives only reported growth. |
| 6. EBITDA Margin (≥2.7 / <2.5) | Consol Q1-FY27 "3.04%" (slide 16, line 573) | GREEN | Standalone 3.03% (line 540). |
| 7. Dell Commercial share (double-digit / low-single) | **SILENT** — Dell in logo grid (line 262) only, no revenue share | SILENT | Notion catalyst #2; no data label carries Dell mix. |
| 8. Semiconductor growth (>50% YoY / plateau) | **SILENT** — no Rashi Semiconductor reference; slump sale omitted | SILENT | See F16-B; the reorganisation seeding this catalyst is not in the deck. |
| 9. AI-PC penetration in PES (>35% / <25%) | **SILENT** — WEKA.io AI-infra mention qualitative only (line 432) | SILENT | No penetration %, no PES sub-mix. |
| 10. Net D/E (≤0.5 / >0.7) | FY26 "0.43x" (slide 20, line 736; P3-9 line 122); no Q1-FY27 | GREEN (FY26) | Reconciles from balance sheet (F11). |
| 11. Promoter pledge (0 / any) | **SILENT** — not in deck | SILENT | Kill-switch #3 unverifiable from this doctype. |
| 12. Promoter holding (≥63 / <60) | **SILENT** — not in deck | SILENT | Kill-switch #4 unverifiable from this doctype. |

**Pattern (conservative read).** The deck surfaces every working-capital ratio
looking healthy — WC days compressed 73→56 (lines 608/610), debtor days 41
(line 598), Net D/E 0.43x (line 736), EBITDA margin 3.04% (line 573) — but
withholds the one metric that would prove those ratios converted to cash: the
Q1-FY27 CFO. The CFO chart (slide 20) stops at FY26 and shows two of three
historical years deeply negative (-1,020 / -2,992 Mn). Per the Notion
hair-trigger table, the TRIM/EXIT branches are keyed to Q1-FY27 CFO in ₹ Cr;
the deck supplies none, so the decision branch cannot be resolved from this
document alone. This is a CONFIRMATORY-NEGATIVE-leaning silence held as
AMBIGUOUS (quarterly CFO is not customarily disclosed by distributors, so the
omission is not proof of a bad number) → escalated to A4/A5 as the primary
management question, and to A5 to reconcile the ₹113.7 Cr-vs-₹514 Cr FY26 CFO
gap.

Verbatim cash-conversion metric set captured (all with cite):
- CFO (INR Mn), FY24-26 annual only: 1,137 / -1,020 / -2,992 (slide 20, lines 733/741/745) — AMBIGUOUS_LAYOUT year map; no Q1-FY27.
- Inventory Days: 64 (line 595) → 55 (line 596) [AMBIGUOUS pairing].
- Debtor Days: 53/55 (line 596) → 41 (line 598).
- Creditor Days: 44 (line 597) → 40 (line 598).
- Working Capital Days: 73 (line 608) → 56 (line 610); annual 54/54/58/56 (slide 20, lines 734-735).
- Provision for Doubtful Debt %: 0.018% → 0.016% (lines 612-613) [AMBIGUOUS].
- Provision for Inventory Write-off %: 0.043% → 0.088% (lines 611/614) [AMBIGUOUS — note: write-off provision ROSE ~2x; carry to A4].
- Net D/E: 0.50x / 0.43x / 0.35x (slide 20, lines 734/736/737); FY26=0.43x anchored by P3-9.
- ROCE: 12.79% / 12.74% / 16.02% (lines 739/737) [LAYOUT_RECONSTRUCTED].
- ROE: 12.93% / 13.02% / 14.74% (lines 742/740) [LAYOUT_RECONSTRUCTED].

---

## 5. ITEMS FLAGGED FOR A4 (convert to management questions)

FORWARD-SIGNAL: F1, F2, F6, F8, F16-B.
AMBIGUOUS: F9, F16-A.

Suggested question seeds (A4 to formalise):
- F16-A: Q1-FY27 CFO in ₹ Cr, and reconcile the deck's FY26 CFO of ₹113.7 Cr
  against the ₹514 Cr FY26 CFO in prior work (definition/scope?). *(Binding gate.)*
- F16-A: With WC days at 56 and debtor days at 41, what was operating cash
  generation this quarter, and how much of the WC improvement is collection vs
  seasonal payables timing?
- F16-B: Terms/timing of the Embedded-Business slump sale to Rashi Semiconductor
  and the Restar JV; expected exceptional item and consolidation-scope change.
- F2/F8: Drivers of the volatile subsidiary PAT contribution and the ETR
  step-up as net DTA is exhausted — expected FY27 effective tax rate?
- F9: Split the +41 Mn consolidated OCI between FX translation and actuarial
  remeasurement.
- F16 (checklist silence): Dell Commercial revenue share, semiconductor
  run-rate, AI-PC penetration in PES, promoter pledge and holding — none
  addressed by the deck.

---

## 6. LEDGER RECONCILIATION STATEMENT

All 265 gated ledger rows (Tables 1-9) were read at their cited extract lines
and cross-checked against the extract text: Table 1 (23 slides), Table 2 (41
KPI tiles), Table 3 (86 chart labels), Table 4 (86 financial line items), Table
5 (11 splits), Table 6 (13 operating-metric cross-refs, ungated), Table 7 (11
forward statements), Table 8 (1 zero-standing), Table 9 (5 footnotes). Arithmetic
cross-foot PES+LIT = consolidated revenue (ledger note, line 174-177) verified.
Net-worth tie-out (F11) and Net-D/E reconciliation independently re-derived from
slide-20 balance sheet. Reconciled: 100%.

```yaml
stage: A3-forensics
company: "rptech"
quarter: "q1fy27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/rptech-q1fy27/work/forensics_presentation_rptech_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F1", check: "F1", line: "578", classification: "FORWARD-SIGNAL", implication: "Dormant exceptional-item line (live FY24/FY25) is the slot for a pending slump-sale/VDA reorganisation gain"}
  - {id: "F2", check: "F2", line: "552/581", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap swings 4.9%->14.2%->7.6% of standalone PAT; subsidiary contribution large and volatile pre-VDA"}
  - {id: "F6", check: "F6", line: "428-433", classification: "FORWARD-SIGNAL", implication: "VDA forward-integration + WEKA.io AI-infra catalysts announced with no size/timeline/WC impact"}
  - {id: "F8", check: "F8", line: "580/681", classification: "FORWARD-SIGNAL", implication: "Net DTA exhausted by FY26 and consol ETR +159bps YoY -> future ETR step-up, PAT-growth headwind"}
  - {id: "F9", check: "F9", line: "583", classification: "AMBIGUOUS", implication: "Consol OCI +41 (one quarter > full FY26 -30, sign flip) is a consolidation/FX item; verify FCTR vs actuarial at AR"}
  - {id: "F14", check: "F14", line: "131-132", classification: "NEUTRAL-FACT", implication: "Footnote scope conflict (as-on-Q1FY27 vs as-on-FY26) plus 700+/706 and 80/80+ - cumulative disclosure-hygiene point"}
  - {id: "F16-A", check: "F16", line: "730/733", classification: "AMBIGUOUS", implication: "No Q1-FY27 CFO disclosed (binding gate); deck FY26 CFO Rs113.7 Cr does not reconcile to Notion Rs514 Cr - resolve before TRIM/EXIT branch"}
  - {id: "F16-B", check: "F16", line: "whole-deck", classification: "FORWARD-SIGNAL", implication: "Deck omits board-approved Embedded-Business slump sale (Rashi Semiconductor) and Restar JV; segment-level YoY not computable"}
forward_signals: ["F1", "F2", "F6", "F8", "F16-B"]
ambiguous: ["F9", "F16-A"]
commitments:
  - {commitment: "Strategic investment in VDA Infosolutions - forward integration into managed IT services/lifecycle support", implied_date: "none stated (67% for Rs368.5 Cr per Notion; path to 100%)", ref: "slide11 line428-430", status_word: "initiated"}
  - {commitment: "Strategic partnership with WEKA.io - AI infrastructure & HPC workload management", implied_date: "none stated", ref: "slide11 line432-433", status_word: "completed"}
  - {commitment: "Two new Tier-2 branches - Udaipur and Dhule", implied_date: "done this quarter", ref: "slide11 line435-437", status_word: "completed"}
  - {commitment: "Growth pillars: expand verticals / adjacent segments / OEM alliances / market penetration / solution-based selling", implied_date: "none (qualitative)", ref: "slide10 line398-415", status_word: "intended"}
gate_a3: pass
blank_checks: []
```
