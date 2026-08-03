# A3 FORENSIC NOTES — GANECOS Q1 FY27 — DOCTYPE: PRESENTATION (investor deck)

Company: Ganesha Ecosphere Limited (GANECOS) | Quarter: Q1 FY27 | Model: claude-opus-4-8
Inputs read verbatim: A1 deck extract (`extract_presentation_ganecos_q1fy27.txt`, 717 lines),
A2 deck ledger (`ledger_presentation_ganecos_q1fy27.md`, Tables A-H), and the filed results
extract (`extract_results_ganecos_q1fy27.txt`, 386 lines) used as the source of truth for
reconciliation. Ledger rows reconciled: 100% (every Table A-H row opened at its cited line).

CENTRAL FORENSIC FOR A DECK: reconcile every quantified deck claim to the filed numbers, capture
every forward-looking guidance number, and flag selective framing / non-GAAP metrics / any claim
the filing is silent on or contradicts. Result up front: **the deck's Q1 FY27 P&L ties cleanly to
the filing on every line, and the deck's EBITDA is on a genuine operating basis (excl. other
income), not dressed up.** The forensic value is not a broken number; it is (i) a very large
subsidiary-profit swing the deck under-narrates, (ii) a consolidated ETR that fell below statutory
because subsidiary profit bore zero current tax, (iii) incremental Warangal utilisation/capacity
disclosure the filing lacks, and (iv) the deck's continued silence on net debt / capex / CCPS —
leaving Notion decision-gate item (ii) unmet.

---

## DECK-vs-FILING RECONCILIATION TABLE (source of truth = filed results, Rs Cr)

### Consolidated Q1 FY27
| Metric | Deck value (line) | Filing value (line) | Tie? |
|---|---|---|---|
| Net revenue from operations | 423.67 (slide32 L673) / 423.7 chart (L108) | 42,366.67 Lakh = 423.67 (L212) | ✓ exact |
| Other income | 3.62 (L674) | 361.98 Lakh = 3.62 (L201) | ✓ |
| Total income | 427.29 (L675) / 427.3 chart (L229) | 42,728.65 Lakh = 427.29 (L215) | ✓ |
| Profit before tax | 37.09 (L684) | 3,709.47 Lakh = 37.09 (L218) | ✓ |
| Tax expense | (8.06) (L685) | curr 507.73 + def 298.26 = 805.99 Lakh = 8.06 (L220-221) | ✓ |
| PAT | 29.03 (L686) | 2,903.48 Lakh = 29.03 (L222) | ✓ |
| OCI | 1.00 (L687) | 1.53+115.70-17.69 = 99.54 Lakh = 1.00 (L225-228) | ✓ |
| Total comprehensive income | 30.03 (L688) | 3,003.02 Lakh = 30.03 (L238) | ✓ |
| Operating EBITDA | 59.8 (chart L111) / 14.11% bullet (L302) | PBT-before-assoc 37.18 + fin 8.87 + dep 17.34 − OI 3.62 = 59.77 (L216,209,210,201) | ✓ EBITDA = **operating basis, excl other income** |
| EBITDA margin | 14.11% (L302); 14.1% chart | 59.77/423.67 = 14.11% | ✓ |
| Basic EPS | 10.86 labelled "Basic" (slide8 L180) | Basic **10.85** / Diluted 10.86 (L245-246) | ✗ deck labels the **diluted** figure as Basic (see F10) |

### Standalone Q1 FY27
| Metric | Deck value (line) | Filing value (line) | Tie? |
|---|---|---|---|
| Net revenue | 262.30 (L694) / 262.3 chart | 26,230.11 Lakh = 262.30 (L67) | ✓ |
| Other income | 3.52 table (L695) / **3.53** bullet (L306) | 351.68 Lakh = 3.52 (L68) | table ✓; **bullet +0.01 mismatch** (F14) |
| PBT | 18.46 (L705) | 1,845.53 Lakh = 18.46 (L83) | ✓ |
| Tax expense | 4.71 shown positive (L706) | curr 507.73 + def (37.15) = 470.58 Lakh = 4.71 charge (L85-86) | ✓ value; **sign shown un-parenthesised while all prior periods parenthesised** (F14) |
| PAT | 13.75 (L707) | 1,374.95 Lakh = 13.75 (L88) | ✓ |
| Operating EBITDA | 23.8 (chart L137) / 9.07% bullet (L303) | 18.46 + 2.00 + 6.85 − 3.52 = 23.79 | ✓ margin 23.79/262.30 = 9.07% |
| Basic EPS | 5.13 (slide9 L216) | 5.13 (L98) | ✓ |

### Subsidiary contribution & balance-sheet items
| Item | Deck | Filing | Note |
|---|---|---|---|
| Consol PAT − Standalone PAT | 29.03 − 13.75 = **+15.28** | matches auditor Other-Matter: 2 domestic subs net +1,504.03 Lakh = +15.04; Nepal sub −26.81 Lakh = −0.27; assoc −8.55 Lakh (L347-370) | Notion pre-registered +15.29 → **matches**; F2 |
| Consolidated net debt | **NOT DISCLOSED** | **NOT DISCLOSED** (P&L only, no balance sheet) | decision-gate item (ii) still unmet; F16-01 |
| Capex / Warangal CWIP (Rs 192.58 Cr) | **NOT DISCLOSED** (capacity in TPA only) | not in P&L | F16-01 |
| Rs 410 Cr CCPS into subs | not quantified; only referenced as "subsidiary loans converted into equity" (L307) | not in P&L | F2-02 |
| Warangal commissioning / utilisation | **DISCLOSED: 72% capacity** (L300) — incremental | absent | F16-03 (deck adds value) |
| Dividend | not disclosed | not disclosed | neither doc |

Verdict on the A2 flags: the **NUMBER_DISCREPANCY** is a 0.01 Cr bullet-vs-table rounding gap on
standalone other income (immaterial; F14). The **GUIDANCE** flag resolves into 6 forward
commitments (F6 register). No headline Q1 FY27 figure fails to reconcile.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F2-01 | F2 | Table F cons/SA PAT | slide32 L686 / slide33 L707 | "Net Profit after tax 29.03 … 13.75" | FORWARD-SIGNAL | Subsidiary contribution to PAT swung from **−9.62 Cr (FY26 full year)** to **+15.28 Cr in Q1 FY27 alone** (111% of standalone PAT). The rPET-granules/Warangal subsidiary block has inflected to strong profit; this is the transition-alpha thesis showing up. Gap moved >100pp of standalone PAT vs any prior period → far beyond the 5pp FINDING threshold. |
| A3-F2-02 | F2 | Table C 12.7 | slide12 L306-308 | "Standalone other income dropped from ₹9.86 crore to ₹3.53 crore due to the discontinuation of interest income on subsidiary loans converted into equity" | FORWARD-SIGNAL | Standalone other income structurally reset ~Rs 6 Cr/qtr lower because inter-company loans were converted to equity (ties to Notion Rs 410 Cr CCPS tripwire). Standalone PAT will read lower going forward on this line; consolidated unaffected. Deck does not quantify the CCPS. |
| A3-F6-01 | F6 | Table E; Table B slide26 fn | slide26 L577; slide22 L469-472; slide30 L649-650 | "Another brownfield expansion of 22,500 TPA is underway"; "Ramping up capacities in rPET granules to 42,000 TPA"; "Target revenue contribution of value added products ~65% (vs 40% currently)" | FORWARD-SIGNAL | Six dateable/undated management commitments (see Commitment Register). The 22,500 TPA brownfield "underway" confirms the Notion tripwire (Odisha 67,500 greenfield dropped, 22,500 brownfield remaining). None carry an explicit completion date → A4 question. |
| A3-F7-01 | F7 | Table C 12.3 | slide12 L298-299 | "Consolidated sales declined by 11.2% due to a 13.4% drop in standalone sales volumes, driven by weaker demand amid higher polymer prices and geopolitical tensions" | AMBIGUOUS | Pre-emptive demand-softness explanation. Volume fell double-digits while the deck headlines margin/PAT. Is the polymer-price/demand pressure continuing into Q2 FY27? → A4 question. |
| A3-F8-01 | F8 | Table F cons tax | slide32 L685 (deck) / filing L220-221 | deck: "Tax Expense (8.06)"; filing: "Current tax 507.73 … Deferred tax 298.26" | FORWARD-SIGNAL | Consolidated ETR fell to **21.7%** (Q1FY27) from 24.8% (Q4) / 24.9% (Q1FY26) / 29.2% (FY26), i.e. below statutory 25.17%. Cause (from filing): consolidated **current tax 507.73 Lakh = standalone current tax exactly** — the +15 Cr subsidiary profit bore **zero current tax** (loss carryforward / holiday). Future ETR step-up risk as subsidiary shields exhaust. Deck shows only aggregate tax and does not explain. |
| A3-F10-01 | F10 | Table B slide8 EPS | slide8 L180,189 vs filing L245-246 | deck "Basic EPS … 10.86"; filing "Basic 10.85 / Diluted 10.86" | NEUTRAL-FACT | Deck labels the **diluted** EPS (10.86) as "Basic"; filed basic is 10.85. Deck also omits paid-up capital / share count entirely (filing: unchanged 2,679.60 Lakh, no corporate action; ESOP trust holding rose 55,390 → 58,590 shares). Minor optimistic labelling. |
| A3-F14-01 | F14 | Table F SA tax; Table C 12.7 | slide33 L706; slide12 L306; slide8 L189 | "Tax Expense 4.71" (un-parenthesised) vs "(5.78)/(2.62)/(16.64)"; bullet "3.53" vs table "3.52" | NEUTRAL-FACT | Cumulative drafting inconsistencies: (a) standalone Q1FY27 tax charge shown positive while every other period parenthesised; (b) other-income 3.53 (bullet) vs 3.52 (table); (c) EPS basic/diluted mislabel. Individually immaterial, collectively a governance-tidiness data point. |
| A3-F15-01 | F15 | Table C slide23 JV; slide15 subs | slide23 L500; slide15 L341-347 vs filing L319-335 | deck: "Strategic JV with Race Eco Chain (49:51)"; filing: "Ganesha Recycling chain Private Limited … Associate" | AMBIGUOUS | Deck's "Company Structure" slide names only the 3 wholly-owned subs and omits the two other consolidated entities in the filing scope list — Ganesha Employees' Welfare Trust and the associate. The associate (49% → below control) is styled a "JV (49:51)" on slide 23. Same entity as "Race Eco Chain"? Why JV framing vs Associate classification? → A4 question. |
| A3-F16-01 | F16 | Table G; Tables F | whole deck (no balance sheet) | (absence) — deck P&L slides 32-33 carry no balance-sheet, cash-flow, net-debt, or capex line | CONFIRMATORY-NEGATIVE | The deck does **not** disclose consolidated net debt, capex, Warangal CWIP (Rs 192.58 Cr), or the Rs 410 Cr CCPS. Notion decision-gate item (ii) — a clean re-verifiable consolidated net-debt read — remains **unmet** after both the filing and the deck. Escalate: net-debt read must come from the AR/rating rationale. |
| A3-F16-02 | F16 | Table C 12.5-12.6; Table B slides6-9 | slide12 L301-305; slides 6-9 | "Consolidated margins improved to 14.11% … Consolidated PAT growth surged 25% QoQ"; non-GAAP "EBITDA / Ton", "Cash Profits" | AMBIGUOUS | Selective framing: headline leads with margin/PAT while the 11.2% consolidated / 13.4% standalone sales-volume decline sits in one bullet. "EBITDA/Ton" rose 11.6→14.9 partly because volume (denominator) fell. "Cash Profits" and "EBITDA/Ton" are non-GAAP, not in the filing (they do reconcile: cash profit 46.4 = PAT 29.03 + dep 17.34). → A4: is margin gain sustainable if volume recovers at lower price? |
| A3-F16-03 | F16 | Table C 12.4; Table B slide26 | slide12 L300; slide26 L552-578 | "Legacy business operated at 102% and Warangal unit operated at 72% capacity"; capacity table Warangal 77,640 TPA (rPET Granules 64,500*) | FORWARD-SIGNAL | Incremental over the filing: utilisation (legacy 102%, Warangal 72%) and facility-level TPA. 72% Warangal utilisation with a 22,500 TPA brownfield still underway = volume runway. This is the deck's genuine added value; feed the FTTCP catalyst timeline. |
| A3-F16-04 | F16 | Table H | ledger Table H / A2 note L4 | "No prior-quarter presentation ledger or extract exists … PRIOR_LEDGER_UNAVAILABLE" | NEUTRAL-FACT | The dropped-metric / softened-guidance comparison cannot be run this cycle — no Q4 FY26 deck to diff. Recorded as a coverage gap, not a clean pass; A4 should request the prior deck or accept the gap. |

---

## CHECKLIST SCORECARD (all 17 statused — GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | PASS | A2 count = 0; no P&L line item is nil/dash across all four periods on either deck statement. |
| F2 STANDALONE vs CONSOLIDATED | **FINDING** (A3-F2-01, -02) | Subsidiary PAT contribution swung −9.62 Cr (FY26) → +15.28 Cr (Q1FY27) = 111% of standalone PAT; ties to Notion +15.29 and to standalone other-income reset. |
| F3 SHELL-ENTITY DETECTION | PASS | Cons vs SA cost lines differ materially (materials 303.52 vs 201.08; dep 17.34 vs 6.85) — subsidiaries have real operations (Warangal plant); not shells. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | A presentation carries no auditor Other-Matters paragraph. (Cross-ref: filing shows ~Rs 14.7 Cr net profit / ~50% of consolidated PAT rests on component-auditor / management-certified numbers — flagged in results-doc forensics, not here.) |
| F5 GOING CONCERN / EoM | N.A. | No auditor report or EoM in a presentation; filing review is clean/unmodified. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** (A3-F6-01) | Lexicon hits "is underway", "ramping up", "target", "operationalized" → 6 commitments (register below). |
| F7 HEDGE PHRASE MINING | **FINDING** (A3-F7-01) | Demand-softness / "geopolitical tensions" / "higher polymer prices" pre-emptive explanation of the volume decline. |
| F8 TAX FORENSICS | **FINDING** (A3-F8-01) | Consolidated ETR 21.7% < statutory 25.17%; subsidiary profit bore zero current tax (cons current tax = standalone current tax). Future step-up risk. |
| F9 OCI FORENSICS | PASS | Single-quarter OCI +1.00 does not exceed full prior-year OCI (−6.23 cons); no assumption-change signal at deck granularity (deck shows aggregate OCI only). |
| F10 SHARE COUNT & DILUTION | **FINDING** (A3-F10-01) | Deck labels diluted EPS 10.86 as "Basic" (filed basic 10.85); omits paid-up capital/share count; ESOP trust holding rose 55,390→58,590. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | Presentation carries no balance sheet / net-worth / other-equity figure to reconcile (filing gives only FY26 year-end other equity). |
| F12 SEGMENT FORENSICS | N.A. | Single reportable segment (filing note 4: no reportable segments); deck facility table is not a financial segment schedule. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | IR presentation, not a board-outcome filing; director slide 27 carries no DINs/term dates; no AGM/dividend/enabling-resolution content. |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** (A3-F14-01) | Standalone tax sign inconsistency, 3.53-vs-3.52 bullet/table gap, basic/diluted EPS mislabel. |
| F15 ENTITY LIST DIFFS | **FINDING** (A3-F15-01) | Deck omits Welfare Trust + associate from structure slide; associate styled "JV (49:51)"; no prior deck to diff for additions/deletions. |
| F16 PRESENTATION-SPECIFIC | **FINDING** (A3-F16-01..04) | Net-debt/capex/CCPS omitted (gate item ii unmet); selective volume framing + non-GAAP metrics; incremental Warangal utilisation/capacity disclosure; prior-deck comparison unavailable. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is a presentation, not a transcript; no concall turns to silence-audit. |

Blank checks: none. GATE A3: **pass**.

---

## COMMITMENT REGISTER (from F6)

| # | commitment | implied date | ref | status word |
|---|---|---|---|---|
| 1 | Brownfield expansion of 22,500 TPA (Warangal rPET granules, base 64,500 TPA) | undated | slide26 L575-577 | underway |
| 2 | Ramp rPET-granules capacity to 42,000 TPA | undated | slide22 L469-472 | ramping up |
| 3 | Value-added products to ~65% of revenue (vs 40% currently) | undated (target) | slide30 L649-650 | target/intends |
| 4 | Additional food-grade application approvals at Warangal | undated | slide26 L569-571 | in process |
| 5 | 40+ brands across various stages of approval for rPET products | undated | slide30 L642-643 | in process |
| 6 | Warangal 50,000 TPA & Temra→Nepal 12,000 TPA facilities | already done | slide22 L471-474 | operationalized (completed) |

All forward commitments except #6 are **undated** — A4 should convert "underway/ramping/target"
into explicit management questions on timeline and capex quantum for the Role 5 promise-vs-delivery
tracker and the FTTCP catalyst timeline.

---

## HANDOFF TO A4
- FORWARD-SIGNALS → question candidates: A3-F2-01, A3-F2-02, A3-F6-01, A3-F8-01, A3-F16-03.
- AMBIGUOUS → question candidates: A3-F7-01, A3-F15-01, A3-F16-02.
- CONFIRMATORY-NEGATIVE: A3-F16-01 (net-debt gate item (ii) unmet — deck did not fill it).
- Deck reconciles 100% to the filing on all headline Q1 FY27 figures; EBITDA is a true operating
  figure (excl. other income), so the A2 NUMBER_DISCREPANCY collapses to a 0.01 Cr rounding note.

```yaml
stage: A3-forensics
company: "GANECOS"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ganecos-q1fy27/work/forensics_presentation_ganecos_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-F2-01", check: "F2", line: "slide32 L686 / slide33 L707", classification: "FORWARD-SIGNAL", implication: "Subsidiary PAT contribution swung -9.62 Cr (FY26) to +15.28 Cr (Q1FY27) = 111% of standalone PAT; rPET-granules/Warangal block inflected to profit."}
  - {id: "A3-F2-02", check: "F2", line: "slide12 L306-308", classification: "FORWARD-SIGNAL", implication: "Standalone other income reset ~6 Cr/qtr lower as inter-co loans converted to equity (CCPS); standalone PAT structurally lower, consolidated unaffected."}
  - {id: "A3-F6-01", check: "F6", line: "slide26 L577; slide22 L469-472; slide30 L649-650", classification: "FORWARD-SIGNAL", implication: "Six management commitments incl 22,500 TPA brownfield underway (confirms Notion tripwire) and 65% value-added revenue target; all undated."}
  - {id: "A3-F7-01", check: "F7", line: "slide12 L298-299", classification: "AMBIGUOUS", implication: "Pre-emptive demand-softness / polymer-price / geopolitical hedge on a 11.2%/13.4% volume decline; is pressure continuing into Q2?"}
  - {id: "A3-F8-01", check: "F8", line: "slide32 L685 / filing L220-221", classification: "FORWARD-SIGNAL", implication: "Consolidated ETR 21.7% below statutory 25.17%; subsidiary profit bore zero current tax; future ETR step-up risk."}
  - {id: "A3-F10-01", check: "F10", line: "slide8 L180,189 / filing L245-246", classification: "NEUTRAL-FACT", implication: "Deck labels diluted EPS 10.86 as Basic (filed basic 10.85); paid-up capital/share count omitted; ESOP trust 55,390->58,590."}
  - {id: "A3-F14-01", check: "F14", line: "slide33 L706; slide12 L306; slide8 L189", classification: "NEUTRAL-FACT", implication: "Standalone tax sign inconsistency, 3.53-vs-3.52 bullet/table gap, basic/diluted EPS mislabel; cumulative governance-tidiness point."}
  - {id: "A3-F15-01", check: "F15", line: "slide23 L500; slide15 L341-347 / filing L319-335", classification: "AMBIGUOUS", implication: "Structure slide omits Welfare Trust + associate; associate styled JV (49:51); reconcile Race Eco Chain vs Ganesha Recycling Chain and JV-vs-associate framing."}
  - {id: "A3-F16-01", check: "F16", line: "slides 32-33 (no balance sheet)", classification: "CONFIRMATORY-NEGATIVE", implication: "Deck discloses no net debt, capex, Warangal CWIP, or Rs 410 Cr CCPS; Notion decision-gate item (ii) clean net-debt read remains unmet."}
  - {id: "A3-F16-02", check: "F16", line: "slide12 L301-305; slides 6-9", classification: "AMBIGUOUS", implication: "Selective framing leads with margin/PAT while volume decline buried; non-GAAP EBITDA/Ton and Cash Profits (EBITDA/Ton rises partly on lower volume denominator)."}
  - {id: "A3-F16-03", check: "F16", line: "slide12 L300; slide26 L552-578", classification: "FORWARD-SIGNAL", implication: "Incremental over filing: legacy 102% / Warangal 72% utilisation and facility-level TPA; 72% Warangal + 22,500 TPA brownfield = volume runway."}
  - {id: "A3-F16-04", check: "F16", line: "ledger Table H / L4", classification: "NEUTRAL-FACT", implication: "No prior-quarter deck exists; dropped-metric/softened-guidance comparison cannot run this cycle (coverage gap, not a clean pass)."}
forward_signals: ["A3-F2-01", "A3-F2-02", "A3-F6-01", "A3-F8-01", "A3-F16-03"]
ambiguous: ["A3-F7-01", "A3-F15-01", "A3-F16-02"]
commitments:
  - {commitment: "Brownfield expansion 22,500 TPA (Warangal rPET granules)", implied_date: "undated", ref: "slide26 L575-577", status_word: "underway"}
  - {commitment: "Ramp rPET-granules capacity to 42,000 TPA", implied_date: "undated", ref: "slide22 L469-472", status_word: "ramping up"}
  - {commitment: "Value-added products to ~65% of revenue (vs 40%)", implied_date: "undated", ref: "slide30 L649-650", status_word: "target"}
  - {commitment: "Additional food-grade approvals at Warangal", implied_date: "undated", ref: "slide26 L569-571", status_word: "in process"}
  - {commitment: "40+ brands across various stages of approval", implied_date: "undated", ref: "slide30 L642-643", status_word: "in process"}
  - {commitment: "Warangal 50,000 TPA and Nepal 12,000 TPA facilities", implied_date: "completed", ref: "slide22 L471-474", status_word: "operationalized"}
gate_a3: pass
blank_checks: []
```
