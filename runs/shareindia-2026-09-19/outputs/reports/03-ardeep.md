# STAGE 3 — ANNUAL REPORT DEEP DIVE, BACKWARD READ
Company: Share India Securities Limited (SHAREINDIA) | Run date: 2026-09-19
Source: inputs/annual-report/SHAREINDIA-AR-FY26.txt (FY26 AR, filed 05-Sep-2026, page markers cited).
Backward-reading method used (auditor's report and financial statements first,
front matter and Chairman's letter last), cross-referenced throughout with the
Stage 2 triple-pass Notes analysis (outputs/reports/02-notes.md, B02-notes.yaml).

LOAD-BEARING FACTS CHECKED FIRST (from B00/companies/SHAREINDIA.md):
- LBF1 (prop vs client split): the AR's Note 45 segment note cannot answer this
  (confirmed, B02 rank 1). **New evidence found in this stage**: the Business
  Responsibility and Sustainability Report (BRSR, Annexure 7, p.84) discloses,
  under "Products/Services... % of Turnover", **"Trading in Securities" =
  73.47% of turnover** against **"Stock Broking Services... = 15.19%"**
  (p.84). "Turnover" is confirmed as revenue from operations (BRSR Section VI
  item 24a states Turnover ₹1,22,727.35 lakhs, which ties exactly to the
  standalone Total revenue from operations, p.136). This is a filed, numeric,
  more granular answer than the segment note and is the single most
  load-bearing new finding of this stage. It measures revenue share, not
  volume share, so it does not mechanically contradict management's "60%
  client by volume" language, but it is hard evidence that revenue is
  dominated by the proprietary trading line, not the client-fee line.
- LBF2 (pledge): no pledge % of promoter holding is disclosed anywhere in
  this AR's Corporate Governance Report shareholding tables (p.53); the AR
  discloses only that promoter/promoter group holds 48.62% of equity as at
  31-Mar-2026 (48.67% at 31-Mar-2025) (Annexure 1, p.53). Separately, the
  Corporate Governance Report's related-party remuneration note states the
  Company paid **"interest on pledged shares"** to Mrs. Saroj Gupta and Mr.
  Rajesh Gupta during FY26 (Annexure 1, p.46) — confirming, from the
  governance side, that a company-level borrowing is secured on promoter/
  relative shares (matching B02 rank 9, Note 18 standalone, "lien on shares
  of promoter, directors and relatives," ₹50.04 Cr FY26 borrowing).
- LBF3 (cash conversion): confirmed and quantified. Standalone CFO FY26 =
  ₹(16,426.65) lakhs = ₹(164.27) Cr on PAT ₹29,769.04 lakhs = ₹297.69 Cr
  (Standalone Statement of Cash Flow, p.134). Consolidated CFO FY26 =
  ₹(18,239.92) lakhs = ₹(182.40) Cr on PAT ₹32,444.16 lakhs = ₹324.44 Cr
  (Consolidated Statement of Cash Flow, p.230). Both negative, consistent
  with B00's "CFO negative FY23/FY24/FY26" screener read.
- LBF4 (Sep-2026 funding/disclosure stress cluster): this AR is dated/signed
  19-May-2026 (financials) and the Board's Report/CSR annexures are dated
  03-Sep-2026/24-Jul-2026 — i.e. the AR itself straddles the run-up to the
  Sep-2026 stress cluster. Two items in this AR bear directly on it (see
  Phase 6E): the NCD early-redemption Board resolution of 19-May-2026 and
  the 24-Jul-2026 Board approval of the Enshrine Leasing acquisition, both
  dated **after** the FY26 balance sheet date but treated as "no material
  changes or commitments" in Board's Report Item 25 (p.35).

═══════════════════════════════════════════════════════════════════
PHASE 1: AUDITOR'S REPORT & CARO
═══════════════════════════════════════════════════════════════════

## 1A Core Opinion
Both standalone and consolidated opinions are **unmodified/unqualified**
("give a true and fair view... in conformity with Ind AS") (Auditor's Report
pp.120, 219). No emphasis-of-matter, no material-uncertainty-on-going-concern
paragraph in either report. Going-concern language is standard boilerplate,
confirmed clean by B02 Pass 3 (Note 2.1(c) p.140 standalone; Note 2.1 p.238
consol): "no material uncertainty exists."

## 1B Key Audit Matters
Both reports carry exactly **one KAM: Revenue from operations** (Auditor's
Report p.121 standalone; p.220 consol), verbatim near-identical text.

| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| Revenue recognition (fair-value gains on securities for trade/investments under Ind AS 109, realised vs unrealised; fees and commission under Ind AS 115) | High transaction volume, materiality, mixed recognition bases | Control walkthroughs, contract-note/trade-data test checks, position-statement verification against exchange closing rates, cut-off testing, Ind AS 115/109 disclosure review | 🟡 Standard-form KAM language for a broker; no company-specific quantification of test-check sample sizes given, so depth cannot be independently assessed from the report text alone |

No separate KAM for impairment, provisioning, or fair-value Level 3
valuation, despite B02's Pass 2/3 findings of a NIL, always-Stage-1 MTF
impairment allowance and a new 13.6% Level 3 slice inside "Securities for
trade" (Note 53 standalone pp.207-208). **This is itself a finding**: the
auditor's single KAM covers revenue recognition broadly but does not carve
out impairment/valuation-model risk as a distinct KAM, even though the notes
show a material change (0% to 13.6% Level 3) year-on-year.

## 1C Emphasis of Matter / Other Matters
No Emphasis of Matter in either report. **Other Matter** (consol only,
p.221): the auditor did not audit 12 subsidiaries (total assets ₹82,270.07
lakhs, total revenue ₹29,204.26 lakhs, PAT ₹3,930.18 lakhs, total
comprehensive income ₹4,086.66 lakhs, net cash inflow ₹133.32 lakhs), relying
on other auditors' reports (Consolidated Auditor's Report p.221). Opinion not
modified for this reliance.

## 1D CARO 2020 — Clause by Clause

**Standalone (Annexure B, pp.126-133):**

| Clause | Finding |
|---|---|
| i (fixed assets) | Clean; physical verification phased over 3 years, no material discrepancies (p.126) |
| ii Inventory | Commodities held with third parties, "substantially confirmed," no discrepancies; no year-end inventory (p.126) |
| iii Loans/guarantees | Subsidiary loans outstanding ₹12,666.80 lakhs, guarantees ₹19,800.00 lakhs; "Others" (non-subsidiary incl. MTF) loans outstanding ₹40,261.41 lakhs, guarantees ₹2,71,303.00 lakhs. MTF loans have **no stipulated repayment schedule** — auditor states "we are unable to comment on the regularity of repayment of principal and payment of interest" for MTF (p.127). No loans >90 days overdue. 98.10% of all loans are repayable on demand or have no repayment terms specified (p.128) |
| vii Statutory dues | "Slight delay in a few cases" on undisputed dues, none >6 months overdue (p.128). Disputed: ₹39.55 lakhs + ₹9.14 lakhs + ₹2.68 lakhs income tax across AY2008-09/2015-16/2022-23, all at ITAT/Assessing Officer level, small quantum (p.128) |
| ix Borrowing defaults | (a) No default in repayment of loans/borrowings/interest to any lender. (b) Not a wilful defaulter. (c)-(f) Term-loan use, no short-term-for-long-term diversion, no funds taken to meet subsidiary obligations, no loans against pledge of subsidiary shares (pp.128-129) |
| xi Fraud | (a) No fraud by or on the Company noticed. (b) No Section 143(12)/ADT-4 report filed. (c) No whistleblower complaints received (p.129) |
| xvii Cash losses | **Not applicable — Company has not incurred cash losses** in current or immediately preceding year (standalone, p.129). Note: this is an *accounting*-loss test (P&L), separate from the negative *operating cash flow* found in Phase 3; the two are not in conflict but should not be conflated |
| xx CSR | (a) No unspent non-ongoing-project CSR amount. (b) Ongoing-project unspent amount (₹298.27 lakhs, Project Ujjwal Drishti) transferred to the special account within 30 days per Section 135(6) (p.129) |
| Other | ii(b) working capital limits >₹5 Cr against current-asset security, quarterly returns agree with books (p.126); xii Nidhi N/A; xiii RPT compliant with Sections 177/188; xiv internal audit system commensurate with size; xv no non-cash director transactions; xvi(a-d) RBI Section 45-IA/NBFC/CIC clauses N/A to the standalone entity; xix no material uncertainty on 1-year liability coverage (auditor caveat: "not an assurance as to future viability") (pp.128-130) |

**Consolidated (Annexure A to consol Auditor's Report, p.224):** four
subsidiaries carry adverse/qualified CARO remarks from their own auditors:

| Subsidiary | Clause | Nature |
|---|---|---|
| Silverleaf Securities Research Pvt Ltd | xvii | Cash losses (subsidiary-level) |
| Share India Wealth Multiplier Solutions Pvt Ltd | xvii | Cash losses (newly incorporated Nov-2025) |
| Share India Cred Capital Pvt Ltd | xvii | Cash losses (newly incorporated Jan-2026) |
| Share India Securities (IFSC) Pvt Ltd | xviii | Auditor resignation clause |

This directly corroborates B02's rank-3 finding (IFSC swung to a ₹4.18 Cr
loss; Algoplus PAT fell 64.7%) from an independent source (CARO, not the
Schedule III AOC-1 numbers).

**Standalone-vs-consolidated qualification, Rule 11(g) (audit trail):** both
reports carry an identical qualification — one accounting software used by
the Holding Company could not be confirmed for (a) daily India-server backup
and (b) uninterrupted audit-trail operation throughout the year, "in the
absence of sufficient appropriate audit evidence" (Auditor's Report p.123
standalone Note 61; p.225 consol Note 65). This is a narrow IT-control
finding, not a financial-statement qualification, but it recurs verbatim in
both reports and both years' books-of-account paragraphs (2(b)/1(b)) name it
as the sole "except" to an otherwise clean books-of-account opinion.

## 1E Auditor Continuity
Firm: M S K A & Associates LLP (formerly M S K A & Associates), ICAI Firm
Reg. No. 105047W/W101187; signing partner Sriparna De (Auditor's Report
p.124/221). **Appointment date / tenure start: NOT FOUND IN DOCUMENT** (this
AR does not state when MSKA was first appointed or its rotation-due year).
Fees FY26 (Corp Gov Report p.54): Statutory Audit & Limited Reviews ₹39.00
lakhs, Other Services (incl. Tax Audit/Certifications) ₹6.50 lakhs, Out of
Pocket ₹4.20 lakhs; Total ₹49.70 lakhs (Company + subsidiaries + MSKA
network). Non-audit/audit ratio = 6.50/39.00 = **16.7%** — well under any
"exceeds audit fee" threshold; no independence-economics flag.
**Separately** (B02 rank 14, Note 39 standalone p.183): a ₹1.50 lakh
FY25-comparative payment to an unnamed "erstwhile auditor" appears in the
notes with no reason disclosed — this is a predecessor-auditor signal the AR
itself never names or explains, carried forward as an open Q&A item.

## 1F Standalone vs Consolidated Differences
- Consol carries an Other Matter paragraph (reliance on 12 other auditors);
  standalone does not (single entity).
- Consol CARO carries four subsidiary-level qualifications (table above);
  standalone CARO is clean except the shared audit-trail/backup exception.
- No differences in opinion type, KAM, or going-concern treatment between
  the two.

### Phase 1 Summary Table

| Item | Standalone | Consolidated |
|---|---|---|
| Opinion | Unmodified | Unmodified |
| KAM count | 1 (revenue recognition) | 1 (revenue recognition) |
| CARO qualifications | Audit-trail/backup software only | Audit-trail/backup + 4 subsidiaries (xvii x3, xviii x1) |
| Fraud (xi) | None noticed | Not separately restated (relies on subsidiary auditors) |
| Cash losses (xvii) | None (standalone) | 3 subsidiaries flagged cash losses |

**Phase 1 Verdict: 🟡 Watch.** Clean opinions and no fraud/default findings,
but the single KAM does not reach impairment/valuation-model risk despite a
material Level 3 shift, and four subsidiaries carry their own CARO cash-loss
or auditor-resignation flags that corroborate the profit-concentration story
found in the notes.
**Kill Switch (informational):** a human reviewer would not stop here alone;
the auditor opinions are clean and the CARO issues are disclosure-depth and
subsidiary-scale, not standalone-entity solvency, issues.

═══════════════════════════════════════════════════════════════════
PHASE 2: NOTES TO FINANCIAL STATEMENTS (verify, extend, summarize)
═══════════════════════════════════════════════════════════════════

Per the pipeline's Phase 2 special instruction, the Stage 2 triple-pass
(outputs/reports/02-notes.md) is the primary source. This stage's incremental
read of the notes (undertaken while reading the surrounding financial
statements) found the Top 15 findings **all still consistent with the filed
text** on spot-check — no discrepancy identified between the triple-pass
figures and the document.

**Triple-pass verification: 15 of 15 confirmed, 0 discrepancies.**

### 2A Accounting policy aggressiveness (extension)
Confirmed from the financial statements read in this stage: revenue
recognition splits cleanly between Ind AS 115 (fees/commission) and Ind AS
109 (fair value changes, "as and when trade is executed" per Note 2.13),
and the standalone revenue notes tie to the Total Income line to the rupee
(Pass 3 finding #2, ₹1,24,679.52 lakhs). Depreciation lives, ESOP expensing
through P&L, and lease accounting show no aggressive variance from Schedule
II norms. The one policy-application item this stage adds: the standalone
P&L shows "Impairment on financial instruments" of only ₹56.71 lakhs (0.05%
of Total Expenses) against a loan book (MTF + others) that grew from
₹32,680.00 lakhs to ₹52,928.21 lakhs (+61.9%) (Balance Sheet p.133); consol
impairment is ₹1,653.31 lakhs against a consol loan book of ₹71,168.37 lakhs
(+35.3%) (Consol Balance Sheet p.228) — the parent-level ECL charge is
disproportionately thin relative to book growth, corroborating B02's
"always Stage 1" finding (rank 15/accounting-quality table).

### 2B RPT map (extension)
Confirmed from Corp Gov Report (p.46): Company paid "interest on pledged
shares" to Mrs. Saroj Gupta and rent plus "interest on pledged shares" to Mr.
Rajesh Gupta during FY26, alongside brokerage/user-ID charges — new,
governance-report-level confirmation that promoter/relative shares stand
behind company borrowing (Note 18 standalone, per B02 rank 9). Board's
Report Item 24 (p.35) and Corp Gov Report Item 8A (p.55) both state, in
boilerplate, that "the Company did not enter into any... transaction with
related parties which could be considered material" under the RPT policy —
this boilerplate framing sits directly beside the >100x jump in
related-party trade receivables and the 133.0%/-99.2% RPT revenue swings
B02 found in Note 7/Note 52; none of those swings is individually reportable
under Section 188 materiality thresholds, but the aggregate pattern is worth
naming again here as a Phase 2/6 cross-reference.

### 2C Contingent liabilities (extension)
Confirmed: FY26 consol contingent liabilities ₹3,232.72 Cr (B02 rank 6; also
independently confirmed at B01's ₹3,233.44 Cr, Note 44, p.287/284 printed),
up 48.3% YoY, against consol net worth ₹2,654.85 Cr (Total Equity, Consol
Balance Sheet p.228) = **121.7%** of net worth by this stage's own
balance-sheet figure (close to B01's 122.7%, small variance from equity
attributable-to-owners vs total-equity denominator choice). Both exceed the
100% flag threshold named in this protocol.

### 2D Receivables / 2E Inventory / 2F Borrowings / 2G Deferred tax / 2H
Exceptional items — all confirmed as reported in B02 (ranks 7, 8, 4, 5, 10,
12, 13); no extension needed, no new discrepancy found against the primary
financial statements read in Phase 3 below.

### Phase 2 Cross-reference with Phase 1
The Phase 1 KAM (revenue recognition) and the notes-level finding that
segment reporting cannot disaggregate prop vs. client (B02 rank 1) are two
sides of the same disclosure gap: the auditor tested revenue recognition
*mechanics* (cut-off, trade-file controls) but the KAM text never engages
with revenue *composition* (prop vs client mix), which is the run's central
question. The BRSR finding in this stage (73.47% trading vs 15.19% broking,
p.84) is the closest the AR comes to answering it, and it sits in a
completely different annexure (Business Responsibility Report) from both the
segment note and the KAM.

**Phase 2 Verdict: 🟡 Watch** (unchanged from B02's accounting_quality: 6/10).
Reconciled with the Stage 2 verdict; no disagreement.
**Kill Switch (informational):** would not stop here; no fraud or manipulation
signal, only disclosure-design and provisioning-conservatism concerns.

═══════════════════════════════════════════════════════════════════
PHASE 3: FINANCIAL STATEMENTS
═══════════════════════════════════════════════════════════════════

## 3A Cash Flow (read first)

| Metric | Standalone FY26 | Standalone FY25 | Consol FY26 | Consol FY25 |
|---|---|---|---|---|
| PAT (₹ lakhs) | 29,769.04 | 24,663.19 | 32,444.16 | 32,808.46 |
| CFO (₹ lakhs) | **(16,426.65)** | (1,560.65) | **(18,239.92)** | 584.88 |
| CFO/PAT | **-0.55x** | -0.06x | **-0.56x** | 0.02x |
| EBITDA (₹ lakhs, MD&A p.77) | 51,314.01 | 40,260.78 | 60,548.70 | 53,783.85 |
| CFO/EBITDA | **-0.32x** | -0.04x | **-0.30x** | 0.01x |
| Capex (PPE+intangibles+ROU, ₹ lakhs) | 413.79 | 1,124.69 | 505.97 | 1,434.53 |
| FCF (CFO - capex, ₹ lakhs, approx.) | **(16,840.44)** | (2,685.34) | **(18,745.89)** | (849.65) |

Source: Standalone/Consolidated Statement of Cash Flow (pp.134, 230-231),
Standalone/Consolidated P&L (pp.133, 229).

**CFO/PAT is deeply negative both years' comparisons and both entity levels
in FY26** — flagged per protocol threshold (<0.7 consistently; here it is
*negative*, a materially worse state than "below 0.7"). This is the single
biggest quantified deterioration in the filing.

**CFO quality checks:**
- The swing from FY25's near-breakeven CFO to FY26's deeply negative CFO is
  driven by working-capital use, not one-time inflators: "Bank balance other
  than cash and cash equivalents" absorbed ₹55,691.79 lakhs standalone /
  ₹69,232.18 lakhs consol (client-margin and exchange-deposit growth), and
  "Loans for margin trading" absorbed a further ₹16,555.86 lakhs standalone /
  ₹16,708.38 lakhs consol (p.134/230). This is **balance-sheet growth funding
  itself through operating cash use**, consistent with B02's FLAG-CASH
  narrative (MTF book +69.8% YoY funded by financing inflows, not retained
  cash).
- No unsustainable payable stretching detected in isolation — trade payables
  rose ₹15,850.93 lakhs (standalone) as a *source* of cash, which is a
  normal counterparty of growing the trading book, not a distress signal on
  its own.
- Interest classification: finance costs (₹8,010.94 lakhs standalone) are
  added back in the indirect-method reconciliation and finance costs *paid*
  (₹7,798.26 lakhs) are shown separately under financing activities (p.135)
  — a conventional, non-aggressive classification choice.
- Net cash generated from financing activities was strongly positive both
  years (₹10,764.60 lakhs FY26, ₹30,528.83 lakhs FY25 standalone), confirming
  B02's point: growth was funded by new debt/equity issuance, not internal
  cash generation.

## 3B Balance Sheet

**Asset/liability walk (standalone, ₹ lakhs, Balance Sheet p.133):**
Total Assets grew 25.0% (₹3,22,494.90 → ₹4,03,107.12), driven by Bank
balance other than cash (+32.5%, ₹1,71,329.85→₹2,27,021.64) and Loans
(+61.9%, ₹32,680.00→₹52,928.21). Total Financial Liabilities grew 40.8%
(₹1,24,663.60→₹1,75,489.06), led by Trade payables (+38.4%) and Other
financial liabilities (+33.7%). A new Debt securities line of ₹11,243.17
lakhs (NCDs) appears (nil in FY25). Total Equity grew 13.9%
(₹1,96,064.73→₹2,23,406.19). **Assets grew faster than equity**, consistent
with the leverage-funded growth story.

**Key ratio table (this stage's independent computation, cross-checked
against MD&A's own SEBI-format ratio table, p.77):**

| Ratio | Standalone FY26 | Standalone FY25 | Consol FY26 | Consol FY25 |
|---|---|---|---|---|
| D/E (MD&A, in times) | 0.25 | 0.18 | 0.25 | 0.21 |
| Current ratio (MD&A) | 1.89 | 1.95 | 2.04 | 2.04 |
| Interest coverage (MD&A) | 4.87 | 5.84 | 4.42 | 5.94 |
| Return on net worth / ROE (MD&A) | 14.19% | 14.44% | 12.97% | 15.97% |
| Net profit margin (MD&A) | 24.26% | 21.68% | 22.07% | 22.65% |
| Trade receivables turnover (days, MD&A) | 88.67 | 62.13 | 77.88 | 51.17 |

D/E is low in absolute terms (no leverage-distress signal on this metric
alone), matching B01's general-corporate cross-check. **CAR/PCR/Current
Ratio in the strict NBFC sense are not disclosed at group level** (D1/D2/D4
input_gaps carried from B01, unchanged).

**DuPont-adjacent finding (new in this stage):** consol ROE fell -18.79% YoY
(15.97%→12.97%) while standalone ROE fell only -1.70% (14.44%→14.19%) — the
**consol ROE decline is more than 10x the standalone decline**. Since consol
= standalone + subsidiaries, and standalone ROE barely moved, the entire
incremental consol ROE deterioration is attributable to the subsidiaries
(Algoplus, IFSC, Fincap — all separately confirmed weaker in B02 ranks 3, 15
and this stage's CARO cross-reference). This is an **independent,
ratio-table-only confirmation** of B02's profit-concentration finding (rank
2, 92.03% parent share), arrived at without touching the AOC-1 schedule.
**Is ROE operational or leverage-driven?** Given D/E is low (0.25x) and
falling ROE occurs *despite* rising leverage YoY (0.18x→0.25x standalone;
0.21x→0.25x consol), the ROE decline is **operational** (margin/earnings
mix), not a deleveraging artefact — if anything, rising leverage should have
supported ROE, and it still fell at the consol level.

**Goodwill % of net worth:** no separate goodwill line identified in the
standalone or consolidated balance sheet extracts read in this stage
(neither balance sheet shows a goodwill line item) — **NOT FOUND / not
material enough to require separate disclosure on this balance sheet
format**.

## 3C P&L

**Line walk (₹ lakhs, Standalone P&L p.133, Consol P&L p.229):**

| Line | Standalone FY26 | YoY | Consol FY26 | YoY |
|---|---|---|---|---|
| Interest income | 21,826.59 | +31.7% | 27,444.66 | +22.4% |
| Dividend income | 1,966.21 | -31.5% | 1,636.87 | -24.7% |
| Fees and commission | 13,197.33 | -12.7% | 16,518.37 | -18.6% |
| Net gain on fair value changes | 72,005.77 | +4.5% | 86,730.03 | -2.3% |
| Sale of products | 13,731.45 | +33.6% | 13,731.45 | +33.6% |
| Total revenue | 1,22,727.35 | +7.9% | 1,47,025.58 | +1.5% |
| PBT | 39,470.81 | +23.4% | 44,047.02 | +2.3% |
| PAT | 29,769.04 | +20.7% | 32,444.16 | -1.1% |

**Fees and commission income fell both at standalone (-12.7%) and consol
(-18.6%) levels even as total revenue rose** — the client-facing,
fee-based line shrank in absolute terms while the fair-value-gain line held
roughly flat (standalone) or fell slightly (consol) and still dominates
composition. This is the P&L-level mirror of the BRSR's 73.47%/15.19% split
and directly contradicts the MD&A's stated management priority (see Phase 4,
"reducing dependence on proprietary trading by increasing... client-led and
fee-based businesses" p.75) — the fee line moved the wrong way in the very
year that statement was written.

**Other income:** ₹1,952.17 lakhs standalone (1.6% of Total Income, p.133);
₹1,859.39 lakhs consol (1.2% of Total Income, p.229). **Well under the 20%
flag threshold** — no other-income inflation concern.

**Tax rate:** standalone effective rate 24.6% (FY26) vs 22.9% (FY25); consol
26.3% (FY26) vs 23.8% (FY25) — both years within a normal band around the
statutory corporate rate, rising modestly YoY, no erratic swing.

**Basic vs diluted EPS gap:** standalone 13.61 vs 13.58 (FY26, 0.2% gap),
11.73 vs 11.22 (FY25, 4.3% gap — likely FCCB/warrant-related, since
"Proceeds from issue of equity shares" was ₹27,271.34 lakhs that year, p.134);
consol 14.79 vs 14.76 (FY26, 0.2% gap), 15.58 vs 14.90 (FY25, 4.4% gap).
Modest, ESOP/warrant-driven dilution; no aggressive EPS management signal.

**Exceptional items:** none identified in either P&L (no "Exceptional items"
line appears in the Standalone or Consolidated Statement of Profit and Loss)
— consistent with B02's "no unusual one-off/exceptional-item pattern"
finding.

### Phase 3 Cross-reference with Phases 1-2
The CFO/PAT collapse (Phase 3A) is the financial-statement-level fact behind
B02's FLAG-CASH; the ROE divergence (Phase 3B) is an independent
confirmation of B02's parent-concentration finding; the fee-income decline
(Phase 3C) is the P&L-level fact behind the BRSR's 73.47%/15.19% split found
in this stage. All three financial-statement phases converge on one story:
**FY26 revenue and profit growth came from the proprietary/interest-bearing
side of the book, funded by new debt and margin/collateral movements, while
the client-fee side contracted and consolidation subsidiaries weakened.**

**Phase 3 Verdict: 🔴 Red Flag** (cash conversion). The negative CFO/PAT and
CFO/EBITDA at both entity levels, in the same year contingent liabilities
rose 48% and an NCD required Board-level early-redemption action, is the
most severe single finding across all statements read.
**Kill Switch (informational):** a human reviewer would have real reason to
pause here on cash-flow quality alone, but this is not a going-concern-level
finding (D/E and current ratio remain low/adequate) — it flags for
FTTCP/valuation scrutiny of cash conversion, not for a halt.

═══════════════════════════════════════════════════════════════════
PHASE 4: RISK FACTORS & MD&A
═══════════════════════════════════════════════════════════════════

## 4A Disclosed risks — real vs boilerplate
The MD&A's "RISK MANAGEMENT" table (p.75-76) names five risks: Socio-Economic,
Regulatory, Business, Competition, Operational. Reading the actual
descriptions and mitigations against the rest of this AR:

| Risk named | Real or boilerplate? | Evidence |
|---|---|---|
| Socio-Economic Risk | Boilerplate | Generic language ("navigates vulnerabilities arising from economic contractions"), no company-specific metric, no link to the actual FY26 events (FPI outflows, RBI rate stance) discussed two pages earlier in the same MD&A |
| Regulatory Risk | Boilerplate | "unwavering observance of directives," no mention of the SEBI algo-platform settlement scheme (see 4B) or the specific SEBI algo-trading framework changes the MD&A itself cites as an opportunity two pages earlier (p.72) |
| Business Risk | Partially real | Names market/economic sensitivity and cites "stringent cash oversight," which is directly falsified by Phase 3A's cash-flow findings — the mitigation language is not supported by the year's own cash-flow statement |
| Competition Risk | Boilerplate | Standard fintech-competition language, no metric |
| Operational Risk | Boilerplate | Generic "dual verification process" language, no mention of the audit-trail/backup-server IT-control exception the auditor itself flagged (CARO/Rule 11(g), Phase 1D) |

None of the five risk descriptions names a single FY26-specific number,
counterparty, or instrument. This is materially thinner and more generic
than the rest of the MD&A (which does cite specific figures for market size,
branch counts, and AUM), a genuine style contrast worth noting.

## 4B Missing Risks
Risks that are obvious from Phases 1-3 but absent from the named risk table:

| Missing risk | Evidence from Phases 1-3 | Likely reason for omission |
|---|---|---|
| NCD refinancing / early-redemption execution risk | Board-approved early redemption of ₹99.90 Cr First-Issue NCD, 19-May-2026 (B02 rank 4/5); reported DSCR explicitly excludes it | The event occurred concurrently with/after the MD&A was drafted (same Board date as accounts approval); management chose not to retrofit the risk table |
| Cash conversion / negative operating cash flow | Phase 3A: CFO/PAT -0.55x standalone, -0.56x consol | This would require naming the company's own weakest metric in its own risk table |
| Contingent liability / exchange-guarantee growth outpacing revenue | +48.3% YoY vs ~1-2% revenue growth (B02 rank 6) | Standard for a clearing member and may be considered "not a risk" internally, but the growth-rate gap is unaddressed |
| Prop-trading revenue concentration | BRSR 73.47% "Trading in Securities" (this stage); Note 45 segment concentration (B02 rank 1) | Naming this as a "risk" would concede the diversification narrative is not yet real |
| Regulatory/SEBI enforcement history | SEBI settlement order re: algo-platform scheme, Mar-2026 (per company memory/B00; **no mention found anywhere in this AR's full text**, confirmed by document-wide search) | Item 37 of Board's Report (p.37) states "no significant and material orders passed by the Regulators or Courts" — a settlement order may reasonably be judged sub-threshold, but its complete absence from the AR, even as a footnote, is a gap worth naming for management Q&A |
| IT audit-trail/backup-server control gap | Auditor's Rule 11(g) exception, both years, both reports (Phase 1D) | This is the auditor's finding, not management's; MD&A's "Operational Risk" mitigation language ("dual verification process") does not acknowledge it |

## 4C MD&A Deep Dive

**Industry claims:** Macro and industry sections (pp.71-73) cite specific,
sourced figures (PLI investment ₹2.16 lakh Cr, Union Budget capex ₹12.2
lakh Cr, CPI 3.4% Mar-2026, repo rate 5.25%, demat accounts 22.45 Cr, Nifty
50/500 5-year CAGR) with source lines attached ("Source: IMF...", "Source:
TimesofIndia, Moneycontrol") — reasonably well-sourced for a listed-company
MD&A, though several sources (TimesofIndia, Moneycontrol) are secondary
press rather than primary data.

**Growth/margin explanation:** MD&A attributes FY26 EBITDA margin expansion
(standalone +19.81% variation YoY per the ratio table, p.74) to no specific
named driver in the narrative text — the "Reasons for variations ≥25%"
column in the ratio table is populated only for D/E, interest coverage, and
trade receivables turnover, **not** for the 19.81%/8.80% operating-margin
swings, despite the ≥25% disclosure requirement nominally targeting large
swings (Key Financial Ratios table, p.74). This is a disclosure-completeness
gap: the company answers the variance question for ratios that moved for
explainable reasons (higher borrowings) but leaves the operating-margin
expansion — arguably the more interesting number for a reader — unexplained.

**External-factor credit-taking/blaming pattern:** Management credits
"diversified business model, disciplined risk management practices" for
navigating "uneven market conditions" (Chairman's letter, p.16) and separately
blames "regulatory developments, geopolitical uncertainties and market
volatility" for near-term challenges (MD&A "Going Forward," p.75) — a
standard credit-taking/externalize-blame pattern, unremarkable in degree but
present.

**Forward guidance table:**

| Claim | Number | Timeframe | Credibility check |
|---|---|---|---|
| PMS AUM target | ₹200 Cr | FY27 | PMS AUM "already crossed ₹100 Cr" per MD&A (p.75) — target is 2x current; no history to check delivery against yet (new business line, launched FY26) |
| Category III AIF launch | N/A | "awaiting regulatory approval" | Stated as pending in both Chairman's letter and MD&A; no date given |
| Branch expansion | 7 new branches named (Hyderabad, Indore, Bhopal, Varanasi, Agra, Raipur, Nagpur) | FY26 (completed) | Names are specific and checkable; NBFC branch count fell 80→73 the same year (B01 M8) and broking branch-count comparability across years is itself flagged as broken by B01 — the "expansion" claim needs reconciling against a branch count that fell in one segment |
| uTrade subscriptions | 5,000+ paid, 71,062 total subscriptions | FY26 (achieved) | Specific and checkable against the platform; no independent verification possible from this document |
| Fixed-income/wealth diversification (Share India Cred, Wealth Multiplier) | Two new subsidiaries incorporated Nov-2025/Jan-2026 | FY26 (incorporation only) | Both are pre-revenue at FY26 close (incorporated in the last 5 months of the year); "expanded fixed-income capabilities" (Performance Snapshot, p.6) describes incorporation, not operating results |

**Segment analysis:** the MD&A's own operational-review section (p.75-76)
gives useful per-vertical KPIs (broking clients 47,253, institutional
clients 186, MTF ₹402.61 Cr, insurance ₹56 Cr premium, NBFC loan book
₹265.33 Cr with GNPA 4.30%/NNPA 2.66%, mutual fund AUM ₹212 Cr, algo
subscriptions 71,062) — this KPI-level detail is more granular and more
useful than the accounting segment note (Note 45), which is a genuine
strength worth crediting even as the segment *note* itself is thin.

## 4D Tone and Credibility Ratings (1-5, with evidence)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2/5 | Risk table is generic (4A); operating-margin swing unexplained (4C); SEBI order absent (4B); BRSR prop/broking split sits in an annexure the ordinary reader would not connect to the segment note |
| Consistency | 2/5 | MD&A states a strategy of "reducing dependence on proprietary trading" (p.75) in the same filing where fee income fell and FV-gain/prop revenue rose in share (Phase 3C, BRSR) — stated strategy and filed numbers point opposite directions |
| Specificity | 4/5 | Operational KPIs (branches, AUM, GNPA, subscriptions) are specific and numerous; the weak spot is specifically where specificity would be most useful (risk factors, margin-variance explanation) |
| Accountability | 3/5 | Board's Report and MD&A do not shy from disclosing negative YoY items (interest coverage -25.60% consol, ROE -18.79% consol, all in the ratio table with variance column populated for the ones legally required) |
| Capital allocation sense | 3/5 | Enshrine Leasing acquisition (IT Zone Mumbai property) and two new pre-revenue subsidiaries (Wealth Multiplier, Cred Capital) show active capital deployment into stated growth verticals, but occur alongside an NCD early-redemption stress event the same Board sitting created — allocation and liquidity management pulling in different directions in the same period |

**Phase 4 Verdict: 🔴 Red Flag.** The risk section is the thinnest, most
boilerplate part of an otherwise reasonably detailed MD&A, and it omits
every risk this stage's own Phases 1-3 surfaced as material. The "reducing
dependence on proprietary trading" claim is directly contradicted by the
year's own revenue mix shift.
**Kill Switch (informational):** would flag strongly for FTTCP/Role 2 to test
the stated diversification strategy against delivery, but this is a
disclosure-quality finding, not a going-concern one.

═══════════════════════════════════════════════════════════════════
PHASE 5: CORPORATE GOVERNANCE & BOARD
═══════════════════════════════════════════════════════════════════

## 5A Board Composition
15 directors as at 31-Mar-2026: 5 Executive, 8 Independent (incl. 1 woman),
2 Non-Executive Non-Independent (incl. 1 woman) (Annexure 1, p.39). This
meets the ≥50% independent requirement given an Executive Chairman
(8/15 = 53.3%).

**Family relationships (p.40):** Parveen Gupta (Chairman & MD) and Rajesh
Gupta (Non-Exec Non-Independent Director) are **brothers**; Saroj Gupta
(Non-Exec Non-Independent Director) is **mother** of Sachin Gupta (CEO &
Whole-time Director). Three of the top-five shareholding directors
(Sachin Gupta 74,60,195 shares; Rajesh Gupta 1,41,50,140 shares; Saroj Gupta
1,04,69,830 shares) are members of one family, alongside Parveen Gupta
(18,95,530 shares) (p.42-43).

**Attendance:** flagged departures from the 100% norm — Saroj Gupta attended
only 1 of 5 board meetings (20%) (p.43); Piyush Khandelwal and Arun Kumar
Jain did not attend the last AGM ("No"/"NA") (p.42-43). No independent
director shows tenure >10 years disclosed; no director holds >8 other
board seats (max disclosed is Arun Kumar Jain with directorships in listed
entities count of 3 including this one, plus committee positions, p.43).

**Post-FY26 board churn (both after the balance sheet date, both inside the
LBF4 stress window):** Subhash Chander Kalia (Independent Director) resigned
effective 2-Jun-2026, "no material reasons... other than those stated" in
his resignation letter (p.41). Shanti Kumar Jain (Independent Director)
ceased to hold office 27-Aug-2026 on attaining age 75 under Reg 17(1A)
(p.41) — an age-based, non-discretionary exit, but its timing (three weeks
before the Infomerics downgrade, per LBF4) means the Company lost two
independent directors, including the outgoing Audit Committee/SRC/CSR
Committee member (Kalia) and a long-serving Audit/CSR Committee member
(Jain), within the same three-month window as the rating-agency stress
event. Both exits are individually explained (resignation, age-limit) and
neither is evidenced as connected to the financial stress, but the
coincidence in timing is worth naming as a monitorable, not a finding of
misconduct.

## 5B Committee Analysis
Four committees confirmed operating per Listing Regulations requirements:
Audit Committee (6 meetings, 2/3+ independent, chaired by Yogesh Lohiya,
Independent), Nomination & Remuneration Committee (4 meetings, all-
independent+Rajesh Gupta), Stakeholders Relationship Committee (1 meeting),
CSR Committee (3 meetings), Risk Management Committee (3 meetings)
(pp.43-49). All committees show full attendance by continuing members;
mid-year reconstitutions (Audit Committee July-2025; CSR Committee
Oct-2025) are disclosed with reasons. No committee shows a chair or
majority conflict with the family-member directors named above (Audit
Committee chair is an unrelated Independent Director throughout the year).

## 5C Compensation
**KMP table (Executive Directors, FY26, p.46):** Parveen Gupta (Chairman &
MD) ₹36.00 lakhs; Kamlesh Vadilal Shah (MD) ₹35.07 lakhs; Sachin Gupta (CEO
& WTD) ₹65.16 lakhs; Vijay Girdharlal Vora (WTD) ₹32.76 lakhs; **Suresh
Kumar Arora (WTD) ₹1.43 Cr** — nearly **4x the Chairman & Managing
Director's own remuneration** and the highest-paid executive on the Board
(p.46/80). This is an atypical structure (a Whole-time Director outearning
the Chairman & MD by a wide margin) worth naming as a governance-design
observation, though no rule is breached and the NRC/Board approved it.

**Comp as % of PAT:** total Executive Director remuneration ≈ ₹3.12 Cr +
Non-Executive sitting fees ≈ ₹0.51 Cr = **≈₹3.63 Cr, ≈1.2% of standalone PAT
(₹297.69 Cr)** — low by market norms, no excess-extraction flag.

**CEO-to-median multiple:** Sachin Gupta (CEO) 13.58:1; Suresh Kumar Arora
(highest-paid WTD) 29.79:1 (Annexure 5, p.80) — the 29.79:1 ratio for a
Whole-time Director who is not the CEO is the more unusual data point.
Median employee remuneration rose 30.96% YoY; average employee increase
40.46% vs average managerial increase 13.89% (p.80) — **employee pay grew
faster than managerial pay this year**, a mitigating fact against any
"management pays itself first" reading.

**Promoter family payroll:** covered above (three Gupta-family
non-executive directors hold significant shareholdings and receive sitting
fees/RPT payments — see 5D and Note 52 cross-reference in Phase 2B).

**ESOP dilution:** ESOP compensation expense fell from ₹2,133.89 lakhs
(FY25) to ₹658.02 lakhs standalone (FY26) (Cash Flow Statement adjustments,
p.134) — a 69.2% decline, consistent with a maturing/slowing options
program rather than fresh dilution pressure.

## 5D Shareholding
Promoter & Promoter Group: 48.62% (31-Mar-2026) vs 48.67% (31-Mar-2025) —
a **5 bps decrease**, essentially flat, not a promoter-selling pattern
against a growth narrative (Corp Gov Report p.53). **Pledge % of promoter
holding is not disclosed in this AR's shareholding tables** — LBF2's
57.80%/Jun-2026 figure remains sourced only from the BSE SHP summary
outside this document, confirming B00's input_gaps note that "pledge status
is not an Ind AS notes item" and, per this stage's read, is also absent
from the Corporate Governance Report's shareholding disclosure (a standard
SEBI LODR shareholding-pattern filing would typically show pledge
separately; its absence from the *AR's own reproduction* of the table,
while present in the underlying BSE filings, is a completeness gap in the
AR's cross-referencing, not a securities-law violation, since the pledge
itself is disclosed in the standalone BSE SHP filings). FII 1.87%/DII 0.48%
(screener-sourced, per B00) not independently re-confirmed in this AR
(shareholding-by-ownership table in the AR shows only Promoter/Public, not
the FII/DII sub-split).

## 5E Governance Red-Flag Checklist

| Item | Finding |
|---|---|
| Whistleblower complaints | 9 total (7 Investors-other, 2 Shareholders), 0 pending, all "N.A." remarks — high-volume but fully resolved (BRSR p.87) |
| SEBI actions | Not disclosed in this AR at all (see 4B); per company memory, a Mar-2026 settlement order exists outside this document |
| RPT committee | Audit Committee holds RPT approval authority per its terms of reference (item viii, p.44); functioning per meeting records |
| Auditor fee ratio | 16.7% non-audit/audit — clean (Phase 1E) |
| CSR compliance | Compliant; ₹590.03 lakhs obligation, ₹291.83 lakhs spent + ₹298.27 lakhs correctly transferred to Unspent CSR Account for the ongoing Ujjwal Drishti hospital project (Annexure 4, p.78) |
| Section 143 fraud | None reported (CARO xi, Phase 1D) |
| Material subsidiary auditor | Share India AlgoPlus (material subsidiary) audited by M/s B D G & Co. LLP, appointed 25-Sep-2025 — a **different firm from the parent's MSKA & Associates** (p.56) — normal practice but means the parent auditor relies on another firm's work for the largest subsidiary, consistent with the Other Matter paragraph in Phase 1C |

**Phase 5 Verdict: 🟡 Watch.** Procedurally compliant governance (committee
structure, independence ratio, evaluation process, CSR, whistleblower
mechanism) sits alongside a family-concentrated board, an atypical executive
pay structure, promoter-shares-as-loan-security (interest paid to
promoters), and two independent-director exits clustering with the Sep-2026
stress window. None of these individually breaches a rule; together they
are the governance-side mirror of the cash-flow and disclosure findings in
Phases 2-4.
**Kill Switch (informational):** would not stop on governance mechanics
alone, but would flag the promoter-pledge-secured borrowing and the family
board composition for the Role 2/Promoter Ledger.

═══════════════════════════════════════════════════════════════════
PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER
═══════════════════════════════════════════════════════════════════

## 6A Narrative vs Reality

| Claim (Chairman's letter, pp.12-16) | Cross-check | ✅/❌ |
|---|---|---|
| "Evolved from a traditional broking firm into a diversified, technology-driven financial services group... spans capital markets, algorithmic trading, wealth management, lending, insurance, investment banking, research and investment distribution" | Parent's share of consol profit rose to 92.03% (B02 rank 2); BRSR shows 73.47% of turnover is "Trading in Securities" (this stage); NBFC/Algoplus/IFSC all weakened FY26 | ❌ Diversification is claimed in structure (many subsidiaries exist) but not yet in earnings mix |
| "Resilient performance... total revenue ₹1,470 Cr, PAT ₹324 Cr" | Matches Consol P&L exactly (₹1,47,025.58 lakhs, ₹32,444.16 lakhs incl. NCI / ₹323.47 Cr owners' share) | ✅ Figures tie out |
| "Balance sheet remained strong, with a net worth of ₹2,187.26 crore as of March 31, 2026" (first instance, standalone context) | Standalone Total Equity per Balance Sheet = ₹2,234.06 Cr (₹2,23,406.19 lakhs, p.133) — a ₹46.8 Cr gap | 🟡 Likely a Companies-Act "net worth" definitional difference (excludes certain OCI/reserve components) vs Ind AS total equity; not reconciled anywhere in the AR text — worth a management Q&A, not a fraud signal |
| "Our balance sheet remained strong, with a net worth of ₹2,577 crore as of March 31, 2026" (second instance, appears to be consol) | Consol Total Equity = ₹2,654.85 Cr; Equity attributable to owners = ₹2,634.94 Cr (p.228) — gaps of ₹77.9 Cr / ₹57.9 Cr respectively | 🟡 Same definitional-gap pattern; the letter uses two different "net worth" figures for the same date without labelling which basis (standalone/consol) or which definition (Ind AS equity vs Companies Act net worth) each uses |
| "prudent risk management standards" / "disciplined risk management practices" (used twice) | MD&A's own risk section is generic/boilerplate (Phase 4A); NCD early-redemption stress required Board action same-day as accounts approval (Phase 6E below) | ❌ Not supported by the risk-disclosure quality or the NCD event |
| "diversified business model... enabled us to navigate these challenges" | Fee income fell -12.7%/-18.6% while FV-gain/interest income carried the year (Phase 3C) | ❌ The "diversified" business model's client-facing lines contracted; the concentrated proprietary line delivered the resilience |

## 6B Strategic Priorities
Named priorities: strengthen wealth management (PMS/AIF), expand
fixed-income distribution (Cred Capital, Wealth Multiplier), scale
technology (uTrade), international expansion exploration, disciplined
governance/risk/capital efficiency (p.15). **Capital allocated:** two new
subsidiaries incorporated (pre-revenue at FY26 close), PMS crossed ₹100 Cr
AUM, Enshrine Leasing acquisition initiated (property-strategic, not a
wealth/fixed-income business) (p.15). **Execution evidence:** specific and
checkable for PMS/uTrade (KPI numbers given); the fixed-income and AIF
priorities are pre-revenue "in progress" statements with no delivered
numbers yet — appropriately hedged as forward-looking rather than achieved.

## 6C Metrics Showcased vs Conspicuously Absent
**Showcased:** revenue, PAT, EBITDA, PAT margin, EBITDA margin (all
consol, all favourable-framing YoY deltas) (p.5); branch/client/AUM
counts (p.72-76); dividend history (p.15).
**Conspicuously absent from the Chairman's letter and Performance Snapshot:**
CFO/operating cash flow (negative both years at both entity levels — never
mentioned in the letter or snapshot); contingent liabilities/guarantee
growth (48.3% YoY); the NCD early-redemption event (occurred the same day
the letter's underlying accounts were approved, 19-May-2026, and is not
mentioned in the Chairman's letter or Performance Snapshot at all); fee
income decline (-12.7%/-18.6%). All four are numbers this stage's own
Phases 2-4 found material.

## 6D Tone and Priority Drift vs Prior Year
Not independently inferable from this AR alone (FY25 AR is in inputs/other/,
not to be treated as primary per run instructions); B01/company memory does
not carry a prior-year Chairman's-letter comparison. **NOT FOUND /
out-of-scope for this stage** — flagged as a gap rather than estimated.

## 6E Quiet Abandonment Check (mandatory)

Reading the opening sections (Chairman's letter, MD&A opening/Going Forward)
against the operational and statutory sections side by side:

**Finding 1 — "No material changes and commitments" (Board's Report Item 25,
p.35) vs. two Board-level events in the same window.**
Quote (opening/statutory claim): *"There have been no material changes and
commitments affecting the financial position of the Company since the close
of the financial year ended March 31, 2026 and the date of this report"*
(Board's Report, Item 25, p.35; report dated 03-Sep-2026).
Where it should have shown up but did not: (a) the Board's own 19-May-2026
resolution to pursue early redemption of the ₹99.90 Cr First-Issue NCD after
holders/Trustee declined an end-use change (Note 17e standalone p.171,
surfaced only in the debt note, per B02 rank 4/13); (b) the Board's
24-Jul-2026 approval of the 100% Enshrine Leasing and Infotech Pvt Ltd
acquisition (Board's Report note to the subsidiary list, p.34, and MD&A
p.75) — both dated after 31-Mar-2026 and before the 03-Sep-2026 report date,
both plausibly "material" to financial position (a debt-instrument
acceleration and a full-equity acquisition), neither named in Item 25.
Classification: **(a) implicit retraction** for the NCD item (the Company
discloses the fact in the debt note's background section but the
"no material changes" statement never engages with it) and **(b) silent
drop** for the Enshrine acquisition (mentioned prominently in MD&A/Chairman's
letter as a *future* growth initiative, but not connected back to Item 25's
"no material changes" test even though the Board approved it before the
report was signed).
Materiality: **changes the thesis.** This is the second, independent
sighting (after B02 Pass 3's Note 62/66 vs Note 17e/18e finding) of the same
disclosure-placement pattern — the Company consistently places
Board-approved, post-year-end financial commitments inside a background
note rather than in the section designed to surface them (subsequent
events / material changes), across two different statutory sections of the
same AR.

**Finding 2 — "Reducing dependence on proprietary trading" (MD&A p.75) vs.
the year's own revenue mix (Phase 3C, BRSR).**
Quote: *"The management continues to focus on reducing dependence on
proprietary trading by increasing the contribution from client-led and
fee-based businesses."*
Where it should have shown up but did not: fees and commission income fell
-12.7% standalone / -18.6% consol the same year (Phase 3C); the BRSR filed
in the same AR shows "Trading in Securities" at 73.47% of turnover against
"Stock Broking Services" at 15.19% (p.84); parent's share of consol profit
rose to 92.03% (B02 rank 2).
Classification: **implicit retraction** (opening/MD&A says "reducing
dependence," the filed numbers in the same document say the dependence grew).
Materiality: **changes the thesis** — this is the run's central LBF1
question, and the Company's own forward-looking claim in this AR moves in
the opposite direction from its own same-year filed numbers.

**Finding 3 — "Retail Expansion... expanded the branch network" (Performance
Snapshot, p.6) vs. branch-count trend (MD&A operational data, B01 M8).**
Quote: *"Expanded the branch network across key Tier-II and Tier-III
markets to deepen customer engagement and distribution reach."*
Where it should have shown up but did not: NBFC branch count fell from 80
(FY25) to 73 (FY26) (AR p.74; B01 M8); broking branches are reported as 95
(FY26, p.72) against a differently-categorised FY25 base of "280 branches
and franchises" that B01 flagged as not comparable. The MD&A does name 7
new city branches opened (Hyderabad, Indore, Bhopal, Varanasi, Agra, Raipur,
Nagpur, p.75), which supports *some* expansion, but the front-matter
Performance Snapshot presents this as an unqualified "Retail Expansion"
highlight without reconciling the NBFC branch decline or the broking
branch-count discontinuity.
Classification: **hedged retreat** (the underlying operational section does
show *some* expansion — 7 new cities — but the front-matter claim omits the
NBFC-branch decline and the base-count discontinuity that would qualify the
headline).
Materiality: **framework noise** — a real but small operational item, not
central to the transition thesis; named for completeness.

No further quiet abandonments identified beyond these three.

**Phase 6 Verdict: 🔴 Red Flag.** Two of the three findings (NCD/Enshrine
placement, prop-trading-dependence claim) are directly load-bearing for the
run's central questions (LBF1, LBF4) and represent the same
disclosure-placement pattern recurring across independent sections of the
same document (Notes, Board's Report, MD&A).

═══════════════════════════════════════════════════════════════════
PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION
═══════════════════════════════════════════════════════════════════

| Strategy | Verdict | Top 3 reasons |
|---|---|---|
| **GARP (fullest reasoning)** | **WATCHLIST** | (1) Growth is real and fast at the top line (consol revenue +34.8% 3-yr, per B01 M4) but its *composition* is proprietary-trading-heavy (BRSR 73.47%), not the client/fee franchise a GARP re-rating thesis for a broker typically prices; (2) "Reasonable" on price needs a valuation this stage does not run, but earnings *quality* is weak this year (negative CFO/PAT, contingent liabilities up 48%) — the "R" in GARP is compromised by cash-conversion risk this year specifically; (3) the transition-to-diversified-platform narrative (wealth mgmt, NBFC, insurance, merchant banking) is structurally present (13 subsidiaries) but not yet earnings-accretive (parent profit share rose to 92%, NBFC/Algoplus/IFSC all weakened) — the growth engine and the "quality improving" engine are currently pulling in opposite directions |
| **Turnaround (fullest reasoning)** | **WATCHLIST** | (1) No single business-model failure to turn around from — this is a growing, profitable company with a *disclosure and cash-conversion* problem, not an operational distress problem, so classic turnaround signals (asset write-downs, going concern, cash losses) are absent (CARO xvii clean at standalone level); (2) the subsidiaries that *would* need a turnaround (Algoplus -64.7% PAT, IFSC swung to loss) are too small individually to move the group thesis (12 audited-by-others subsidiaries = ₹82,270.07 lakhs total assets, 17.9% of consol assets) — a subsidiary-level turnaround exists but is not group-material yet; (3) the NCD refinancing situation is the closest thing to a turnaround-style stress event in this filing, but it is a liquidity/covenant-management event, not a business-model failure |
| Value+Quality | FAIL | Quality dimension fails on cash conversion (negative CFO/PAT) and earnings composition (prop-trading concentration); value not assessed at this stage (no price data read) |
| Capex-Led Growth | WATCHLIST | Capex itself is low (₹413.79-505.97 lakhs, <0.5% of revenue) — this is not a capex-led growth story; the "growth" is balance-sheet (MTF book, trading book) and M&A-led (Enshrine, new subsidiaries), not capex-led |
| Cash Flow Compounder | FAIL | Direct contradiction — CFO is negative both years at both entity levels FY26; this is the opposite of a cash flow compounder profile this year |
| Contrarian | WATCHLIST | The Sep-2026 rating downgrade/NCD stress cluster (LBF4) creates a contrarian setup only if the underlying franchise (broking/MTF client base) is sound and the stress is refinancing-technical rather than credit-quality; this AR's own numbers (fee income declining, prop-dependence rising) do not yet confirm the franchise is strengthening underneath the stress |
| Insider Confidence | WATCHLIST | Promoter shareholding essentially flat (48.67%→48.62%, not a sell-down); but promoter/relative shares are pledged as security for a new company borrowing (interest paid to Rajesh Gupta/Saroj Gupta) — a nuanced signal, not a clean "insider buying" positive |
| Guidance Divergence | FAIL (divergence found) | MD&A's "reducing dependence on proprietary trading" claim diverges from the same-year filed revenue mix (Phase 6E finding 2) — a direct, filed guidance-vs-delivery divergence |

**Best-fit strategy label for Phase 8: GARP (WATCHLIST)** — the operator's
mandate strategy, and the one where this AR's findings are most directly
actionable (the transition thesis is legible and testable, but not yet
confirmed by FY26's own numbers).

═══════════════════════════════════════════════════════════════════
PHASE 8: FINAL VERDICT DASHBOARD
═══════════════════════════════════════════════════════════════════

## Company Snapshot
Share India Securities Ltd — technology-led broking/capital-markets group
(equity/derivatives/commodity broking, MTF, algo-trading platforms, NBFC
lending, insurance distribution, merchant banking, wealth management).
FY26 consol: revenue ₹1,470 Cr (+1.5%), PAT ₹324 Cr (-1.1%), EBITDA margin
41.2%. 13 subsidiaries, 15-member board (family-concentrated), listed on
BSE/NSE.

## Phase-wise Verdict Summary

| Phase | Verdict |
|---|---|
| 1 — Auditor's Report & CARO | 🟡 Watch |
| 2 — Notes | 🟡 Watch |
| 3 — Financial Statements | 🔴 Red Flag (cash conversion) |
| 4 — Risk Factors & MD&A | 🔴 Red Flag (missing risks, guidance divergence) |
| 5 — Governance & Board | 🟡 Watch |
| 6 — Chairman's Letter & Front Matter | 🔴 Red Flag (quiet abandonments) |
| 7 — Best fit strategy | GARP (WATCHLIST) |

## Overall Quality Score: 5.5/10

| Component | Weight | Score /10 | Basis |
|---|---|---|---|
| Governance | 25% | 6 | Procedurally compliant (committees, independence ratio, CSR, whistleblower); offset by family board concentration, atypical WTD pay (₹1.43 Cr vs Chairman's ₹36L), promoter shares pledged for company borrowing, two independent-director exits clustering with the Sep-2026 stress window |
| Accounting quality | 25% | 6 | Per B02, reconciled and confirmed unchanged this stage: realised-gain revenue recognition and internal tie-outs are strong; offset by thin MTF impairment provisioning, new Level 3 valuation slice, and structural segment-note opacity on prop-vs-client |
| Balance sheet | 25% | 5 | Low D/E (0.25x) and adequate current ratio are genuine strengths; offset by contingent liabilities at ~122% of net worth (+48% YoY), NCD refinancing stress requiring Board action, and no group-level CAR/PCR/current-ratio disclosure to test NBFC-style balance-sheet health directly |
| Earnings quality | 25% | 5 | Revenue recognition itself is conservative (mostly realised gains); offset by fee-income decline, rising prop-trading revenue share (73.47% per BRSR), 92% parent profit concentration, and negative CFO/PAT converting accounting profit into cash at a deeply negative rate |

## Top 3 Strengths
1. **Clean audit opinions, no fraud/default findings, low leverage.**
   Unmodified standalone and consol opinions, no CARO fraud/wilful-default
   findings at the standalone level, D/E only 0.25x (Auditor's Report
   pp.120-219; MD&A p.74).
2. **Conservative, realised-gain-heavy revenue recognition with clean
   internal tie-outs.** 95%+ of the FY26 fair-value gain is realised-trade
   profit, not unrealised marks; standalone revenue notes tie to Total
   Income to the rupee (B02 Pass 3 finding, accounting_quality table).
3. **Granular, specific operational KPI disclosure in the MD&A.** Branch
   counts, client counts, AUM, GNPA/NNPA, subscription numbers are all named
   with specific figures, well above the norm for the risk-factor section
   of the same document (MD&A pp.72-76).

## Top 3 Red Flags
1. **Negative operating cash flow at both entity levels, funding growth
   with debt instead of retained cash.** Standalone CFO/PAT -0.55x, consol
   -0.56x, FY26; contingent liabilities +48.3% YoY to ~122% of net worth
   (Phase 3A; B02 FLAG-CASH).
2. **The BRSR discloses 73.47% of turnover from "Trading in Securities"
   against 15.19% from "Stock Broking Services"** (p.84) — filed evidence
   that the business remains revenue-dominated by the proprietary line, in
   the same AR where MD&A claims a strategy of "reducing dependence on
   proprietary trading" and fee income fell -12.7%/-18.6% YoY (Phases 3C,
   4C, 6E).
3. **Recurring disclosure-placement pattern that keeps Board-approved,
   post-year-end financial commitments out of the sections designed to
   surface them.** The 19-May-2026 NCD early-redemption resolution and the
   24-Jul-2026 Enshrine acquisition approval are both absent from Board's
   Report Item 25's "no material changes and commitments" statement
   (03-Sep-2026), echoing the Note 62/66 "no significant events" pattern
   B02's Pass 3 already found (Phase 6E, findings 1-2).

## Key Monitorables for Next Quarter

| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| CFO/PAT (standalone and consol) | Return to positive, or explain persistent negative | Quarterly cash flow statement (results filings) | This stage's single largest red flag; a second consecutive negative year would harden the FLAG-CASH finding |
| NCD early-redemption execution / holders' meeting outcome | Redemption completed or holders' meeting resolved | BSE Reg 30 filings, next quarterly results notes | Directly connects this AR's Note 17e finding to the Sep-2026 adjourned-meeting stress (LBF4) |
| Fee and commission income (standalone) | Return to growth vs FY26's -12.7% | Quarterly P&L | Direct test of the MD&A's "reducing dependence on proprietary trading" claim (Phase 6E finding 2) |
| Prop-trading revenue share (BRSR-equivalent disclosure, or Note 30/Note 45 proxy) | Declining trend toward parity with claimed strategy | Next AR's BRSR Annexure, or quarterly investor presentation if disclosed | Only annual disclosure point found for this split; quarterly proxy needed given B02's finding that quarterly segment notes are equally thin |
| Contingent liabilities / net worth | Stabilising below 100%, or continued rise | Quarterly notes / next AR Note 44 | Guarantee corpus scaling with trading book; a further sharp rise alongside continued negative CFO would compound the cash-conversion flag |
| Enshrine Leasing acquisition completion and consideration | Deal closes at or near the disclosed terms | Next quarterly results / Reg 30 filings | Tests whether capital allocation (property acquisition) proceeds as planned despite the NCD liquidity event in the same period |

## Best-fit Strategy: GARP (WATCHLIST)

## One-line verdict
Growing broking group funds expansion with debt while its own numbers
contradict its stated shift away from proprietary trading.

═══════════════════════════════════════════════════════════════════

## Analyst Note (cross-stage, <=200 words)
The single most consequential discovery in this stage is the BRSR's
73.47%/15.19% trading-vs-broking turnover split (p.84) — a filed, numeric
answer to LBF1 that sits in a completely different annexure from the
segment note B02 already found unable to answer it. Read together with the
FY26 fee-income decline (Phase 3C) and the MD&A's claim of "reducing
dependence on proprietary trading" (Phase 6E), the filing contains its own
internal contradiction on the run's central question. Separately, this
stage found a second, independent instance of the same disclosure-placement
pattern B02's Pass 3 first identified: Board's Report Item 25 ("no material
changes and commitments") omits both the NCD early-redemption resolution and
the Enshrine acquisition approval, both dated after the balance sheet date
and before the report's signing date. Neither finding is accounting fraud;
both are business-model and disclosure-design findings for Role 1/2/6 to
weigh alongside B02's existing flags.
