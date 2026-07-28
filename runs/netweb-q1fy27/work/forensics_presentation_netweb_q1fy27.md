# A3 FORENSIC NOTES — NETWEB Q1 FY27 — Investor Press Release (doctype: presentation)

Company: Netweb Technologies India Limited (NETWEB)
Quarter: Q1 FY27 (period ended 30-Jun-2026)
Doctype: presentation (3-page investor press release; STANDALONE unaudited — line 54)
A1 extract: extract_presentation_netweb_q1fy27.txt
A2 ledger: ledger_presentation_netweb_q1fy27.md
Ledger reconciliation: 50/50 rows read verbatim at cited lines (Tables 1-6, items 1-54) = 100%.
Prior-quarter ledger/extract: NONE supplied (NO_PRIOR_LEDGER). Verbatim EoM/entity diffs impossible;
cross-quarter comparisons use only the Notion baseline figures provided in the task message.

Doctype applicability: this is a standalone press release, not a full results filing, concall, or
slide deck. It carries a 7-row summary P&L, highlight bullets, and a CMD quote — no balance sheet,
no consolidation, no auditor letter, no segment BS, no OCI/tax/reserves lines. Per the F16-applies
rule for presentations, plus the F6/F10 numbers the document carries, plus the task's explicit
instruction to run an F17 silence audit against the supplied Notion checklist. Balance-sheet /
consolidation / audit checks (F1-F5, F8, F9, F11, F12, F14, F15) are marked N.A. with basis.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F16-1 | F16 | Table 2, item 19 | L102 | "Net Debt was 1,999.00 Mn as of 30th June'26" | FORWARD-SIGNAL | Position swung from Net Cash ₹833 Mn (Mar-26) to Net Debt ₹1,999 Mn — a ~₹2,832 Mn deterioration in one quarter despite ₹853 Mn PAT, implying ~₹3.6-3.7bn of cash absorbed by working capital / capex to fund AI-system order execution. No receivable-vs-inventory split disclosed. Monitor CCC against the 90-110 day guide; a large-order WC build is the single biggest near-term cash risk. |
| F16-2 | F16 | Table 3, items 21-23 | L108-109 | "its contribution to the company's operating revenue increased to 62.29%" | FORWARD-SIGNAL | AI Systems ₹5,105.70 Mn (+484.20% YoY) is 62.29% of revenue vs FY26's 43% and vs Q4-concall guidance that AI mix would NORMALISE to ~35%. Actual mix moved the opposite direction. Extreme single-segment dependence raises revenue-durability and lumpiness risk; the "normalisation" thesis is broken this quarter and needs a management explanation (durable demand vs a few large GPU deals). |
| F16-3 | F16 | Table 5, item 32 + Table 3 note | L152 vs L108-109 | "HPC and Private Cloud maintained robust traction at ₹1,252.94 million and ₹1,353.46 million respectively" | AMBIGUOUS | Selective framing: AI Systems gets a dedicated Business-Highlights bullet with growth% and revenue-share%; HPC (15.3% of rev) and Private Cloud (16.5%) appear only as bare absolutes buried in the CMD quote, with NO growth% and NO share%. Implied non-AI revenue grew ~44% YoY vs AI's 484% — the legacy pillars' relative deceleration is quietly unquantified. Three named pillars sum to ₹7,712.10 Mn = 94.1% of revenue; the residual ₹484.76 Mn (HPS / Data Centre Servers, ~5.9%) is entirely unquantified. A4 question: growth rates and share trend for HPC, Private Cloud, HPS, DC Servers. |
| F16-4 | F16 | Table 4, items 25-26 | L134-136 | "Operating EBITDA is calculated as Profit before Tax (PBT) plus Depreciation... plus Finance cost less Other income" / "PAT margin is a percentage of Profit... divided by Total Income" | AMBIGUOUS | Two non-standard, mutually inconsistent metric definitions in one table: (a) Op EBITDA excludes Other income and is margined on Revenue from Operations; (b) PAT margin is margined on Total Income (which INCLUDES Other income). Other income is ₹84.72 Mn Q1FY27 (Total Income 8,281.58 − Rev 8,196.86) and grew from ₹11.05 Mn in Q1FY26. NOTE: the A2 flag calls the Total-Income PAT denominator "margin-inflating" — that is arithmetically reversed (a larger denominator LOWERS the ratio: PAT/Total Income = 10.30% < PAT/Rev = 10.41%). The real forensic point is denominator inconsistency across the two margins, not inflation. A4 question: request a standard EBITDA bridge and a consistent-denominator margin set. |
| F17-1 | F17 | monitoring item 6 | L82-187 (whole doc) | (absent — no customer/concentration disclosure anywhere) | AMBIGUOUS | With AI now 62.29% of revenue and +484% YoY, customer concentration is the obvious risk, yet the release is silent on customer count, top-customer share, or order-book customer mix. No hedge language about lumpiness added either (F7). Silence on the metric that a 62% single-segment quarter most demands. A4 question: top-customer and top-5-customer revenue share, and AI order-book customer concentration. |
| F17-2 | F17 | monitoring item 2 | L102 | "Net Debt was 1,999.00 Mn" (no WC breakdown) | FORWARD-SIGNAL | The net-debt swing (F16-1) is stated as a single number with NO receivables / inventory / payables split and NO CCC figure, despite CCC being an explicit guided metric (90-110 days). Silence on the composition of a ₹2,832 Mn cash deterioration. A4 question: receivables, inventory, payables at 30-Jun-26 and resulting CCC vs guide. |
| F17-3 | F17 | monitoring item 5 | L142-169 (CMD quote) | (absent — no Skylus/Velox software mention) | CONFIRMATORY-NEGATIVE | Software (Skylus/Velox) revenue share is not disclosed. The three "growth pillars" named are all hardware/systems (AI Systems, HPC, Private Cloud); software optionality is unmentioned. Continued silence on the higher-margin software narrative. |
| F17-4 | F17 | monitoring item 8 | (whole doc) | (absent — no remediation statement) | CONFIRMATORY-NEGATIVE | Inventory-audit remediation is not addressed. Not expected in a summary press release, but logged as silence; relevant given the inventory-heavy WC build implied by F16-1/F17-2. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|---|---|---|
| F1  ZERO-STANDING | N.A. | A2 explicitly checked all 42 cells (7 rows x 6 periods); no zero/nil/dash cell; a summary P&L carries no exceptional/discontinued template lines to interrogate. |
| F2  STANDALONE vs CONSOLIDATED | N.A. | Standalone-only results (L54: "unaudited standalone quarterly financial results"); no consolidated column exists to decompose. |
| F3  SHELL-ENTITY | N.A. | No consolidation and no subsidiary cost lines disclosed; nothing to compare. |
| F4  UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other-Matters / component-auditor disclosure in a press release; the whole result is unaudited but no JV/associate carve-out exists. |
| F5  GOING CONCERN / EoM | N.A. | No EoM paragraph in a press release; no prior extract to verbatim-diff (NO_PRIOR_LEDGER). |
| F6  FORWARD-COMMITMENT MINING | PASS | Lexicon swept (commenc/will be/expected/underway/proposes to/board has approved/intends to): zero dated commitments. Board only "took on record" results (L88). Forward language present is non-dateable aspiration ("coming quarters" L154; "multi-year demand pipeline" L159); commitment register empty. |
| F7  HEDGE MINING | PASS | Strict lexicon (no assurance/subject to/evaluating/exploring/in discussions/endeavour): zero hits. "we remain confident... long-term sustainable growth" (L168) is aspirational, not a risk hedge. Notably NO lumpiness/concentration hedge added despite 62% AI mix — absence logged under F17-1. |
| F8  TAX FORENSICS | N.A. | No tax line, no PBT/ETR disclosed; Op EBITDA footnote references PBT but no reconciliation is given. |
| F9  OCI FORENSICS | N.A. | No OCI / actuarial line in a summary P&L press release. |
| F10 SHARE COUNT / DILUTION | PASS | Only Diluted EPS carried (14.98 / 5.38 / 12.43 / 36.30). Implied diluted share count is stable ~56.7-57.0 Mn (853.23/14.98=56.96M; 304.79/5.38=56.65M; 2,058.16/36.30=56.70M) — ~0.5% creep, no material dilution event. No basic EPS or share count disclosed, so basic-vs-diluted spread is uncomputable. |
| F11 RESERVES / NET WORTH | N.A. | No balance sheet, no net-worth or reserves figure to tie out. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities; only segment REVENUE disclosed (handled under F16-2/F16-3). |
| F13 BOARD OUTCOME BEYOND RESULTS | PASS | Board met 28-Jul-2026 and "took on record the unaudited Financial Results" (L88); no AGM notice, dividend, director appointment/term, or capital-raising resolution disclosed — nothing beyond results. |
| F14 NOTE DRAFTING INCONSISTENCIES | N.A. | No auditor letter and no entity tables to cross-check; the margin-definition inconsistency is captured as a forensic finding under F16-4 rather than a name/letter mismatch. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation list and no prior ledger to diff (NO_PRIOR_LEDGER). |
| F16 PRESENTATION-SPECIFIC | FINDING | Net-debt reframing/swing (F16-1), AI-mix vs guidance divergence (F16-2), segment disclosure asymmetry (F16-3), non-standard/inconsistent margin definitions (F16-4). |
| F17 SILENCE AUDIT | FINDING | Silent on customer concentration (F17-1), WC/CCC composition (F17-2), software revenue share (F17-3), inventory remediation (F17-4). CFO/PAT is INDETERMINATE per checklist (no cash flow in a press release) and is NOT inferred. Promoter stake / Chandelier Exit not applicable to this doctype. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| (none) | — | — | — |

No dated or dateable management commitments in this document. All forward language is non-dateable
aspiration (revenue visibility "for the coming quarters" L154; "multi-year demand pipeline" L159;
"remain confident... long-term sustainable growth" L168). Nothing feeds the promise-vs-delivery
tracker this quarter beyond the standing order-book (₹25,069.35 Mn) + L1 (₹8,480.47 Mn) visibility
claim (L153-154), which is a stock figure, not a dated milestone.

---

## RECONCILIATION / ARITHMETIC CROSS-CHECKS (for the record; all internally consistent)

- Revenue YoY 8,196.86/3,012.12 = +172.13% ✓ ; PAT YoY 853.23/304.79 = +179.94% ✓ ; Op EBITDA YoY
  1,205.15/448.02 = +168.99% ✓.
- Op EBITDA margin 1,205.15/8,196.86 = 14.70% ✓ (Revenue denominator per footnote 1).
- PAT margin 853.23/8,281.58 = 10.30% ✓ (Total Income denominator per footnote 2).
- AI share 5,105.70/8,196.86 = 62.29% ✓ ; implied Q1FY26 AI ≈ 5,105.70/5.842 ≈ ₹874 Mn (~29% of the
  ₹3,012.12 Mn Q1FY26 revenue) — i.e. AI share more than doubled YoY.
- Named pillars AI 5,105.70 + HPC 1,252.94 + Private Cloud 1,353.46 = 7,712.10 = 94.1% of revenue;
  residual ₹484.76 Mn (5.9%) undisclosed (HPS / DC Servers).
- Net position: Net Cash ₹833 Mn (Mar-26) → Net Debt ₹1,999 Mn (Jun-26) = ~₹2,832 Mn deterioration.
- Op EBITDA margin 14.70% sits at/above the FY27 guide of 13-14% (guidance not breached to the
  downside); PAT margin 10.30% vs FY26 9.35%.

---

## FORWARD-SIGNAL SUMMARY FOR A4

- FORWARD-SIGNAL: F16-1 (net-debt swing / WC absorption), F16-2 (AI mix 62.29% vs ~35% guide),
  F17-2 (WC composition silence).
- AMBIGUOUS (→ A4 management questions): F16-3 (segment disclosure asymmetry), F16-4 (non-standard /
  inconsistent margin definitions), F17-1 (customer-concentration silence).
- CONFIRMATORY-NEGATIVE: F17-3 (software revenue-share silence), F17-4 (inventory-remediation silence).

```yaml
stage: A3-forensics
company: "NETWEB"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/netweb-q1fy27/work/forensics_presentation_netweb_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: PASS
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: PASS
  F11: N.A.
  F12: N.A.
  F13: PASS
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "F16-1", check: "F16", line: "102", classification: "FORWARD-SIGNAL", implication: "Net Cash 833Mn (Mar-26) to Net Debt 1,999Mn (Jun-26); ~2,832Mn deterioration in one quarter, WC/capex absorption to fund AI orders; no receivable/inventory split"}
  - {id: "F16-2", check: "F16", line: "108-109", classification: "FORWARD-SIGNAL", implication: "AI Systems 62.29% of revenue (+484.20% YoY) vs guided ~35% normalisation; mix moved opposite to guidance; concentration/durability risk"}
  - {id: "F16-3", check: "F16", line: "152", classification: "AMBIGUOUS", implication: "Segment disclosure asymmetry: AI gets growth%/share%, HPC & Private Cloud only bare absolutes in CMD quote; legacy-pillar deceleration unquantified; 5.9% of revenue wholly undisclosed"}
  - {id: "F16-4", check: "F16", line: "134-136", classification: "AMBIGUOUS", implication: "Non-standard Op EBITDA (excl Other income, margined on Revenue) vs PAT margin on Total Income; inconsistent denominators; A2 'margin-inflating' label is arithmetically reversed; request standard bridge"}
  - {id: "F17-1", check: "F17", line: "82-187", classification: "AMBIGUOUS", implication: "No customer-concentration disclosure despite 62% AI mix; request top-customer / top-5 revenue share and AI order-book customer mix"}
  - {id: "F17-2", check: "F17", line: "102", classification: "FORWARD-SIGNAL", implication: "Net-debt swing stated with no receivables/inventory/payables split and no CCC vs the 90-110 day guide; composition of ~2,832Mn cash deterioration withheld"}
  - {id: "F17-3", check: "F17", line: "142-169", classification: "CONFIRMATORY-NEGATIVE", implication: "Software (Skylus/Velox) revenue share silent; all three named growth pillars are hardware/systems"}
  - {id: "F17-4", check: "F17", line: "82-187", classification: "CONFIRMATORY-NEGATIVE", implication: "Inventory-audit remediation not addressed; logged as silence, relevant to the inventory-heavy WC build"}
forward_signals: ["F16-1", "F16-2", "F17-2"]
ambiguous: ["F16-3", "F16-4", "F17-1"]
commitments: []
gate_a3: pass
blank_checks: []
```
