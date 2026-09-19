# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 3 OF 3 (PATTERN PASS + CONSOLIDATION)
KISSHT (OnEMI Technology Solutions Ltd) | Run date 2026-09-19
Sources: Annual_Report_2026.pdf (FY2025-26, Rs million on the face of the notes), cross-checked against
OnEMI_RHP_2026-04-25.txt (Rs million, restated FY23-FY25 plus 9M-Dec-2025 stub, consolidated only).
Figures below are given in Rs million as printed, with Rs Cr shown in brackets where useful for
readability (1 Cr = 10 million). All figures anchored to Pass 1 and Pass 2 extraction; no new document
re-reads were needed beyond a targeted pattern-test using numbers Pass 1/2 already extracted.

This is the third and final pass. Pass 1 read every note sequentially (Notes 1-44 standalone,
1-48 consolidated). Pass 2 re-read the same notes end to end, closed five specific re-check items
against the RHP, and surfaced four new findings inside Note 41 (Financial Risk Management) that Pass 1
had read only for its ECL sub-section. Pass 3 does not re-open the source documents; it looks across
Pass 1 and Pass 2's own numbers for patterns neither pass tested directly, then consolidates.

---
## PASS 3: PATTERN-LEVEL FINDING (new, not in Pass 1 or Pass 2)

### P3-1. Guarantee growth and the ECL build-release cycle do NOT move together
Pass 2 asked Pass 3 to test whether the four-year guarantee-to-net-worth escalation and the four-year ECL
build-release-rebuild cycle are the same phenomenon (i.e., whether provisioning volatility is simply a
function of balance-sheet growth funded by the guarantee). Laying the two Pass 1/2 series side by side:

| | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Corporate guarantee (Rs mn) | 3,895.17 | 7,024.42 | 12,217.64 | 21,982.06 |
| Guarantee YoY growth | — | +80.3% | +73.9% | +79.9% |
| ECL against standard assets, net (Rs mn) | 443.57 charge | 2,603.50 charge | (1,652.04) release | 495.27 charge |

The guarantee (a reasonable proxy for the scale of balance-sheet growth it funds) grew at a remarkably
steady 74-80% every single year. The ECL line did the opposite of steady: a moderate charge, then a much
larger charge, then a near-total release, then a smaller charge again. **The two series do not move
together.** If provisioning volatility were mechanically driven by book growth alone, ECL charges would
track the guarantee's steady climb; instead ECL swings independently of it, including one full year
(FY25) where the charge went negative while the guarantee kept growing at its normal 74% pace. This
rules out "faster book growth explains the FY25 release" as an explanation and strengthens, rather than
answers, the open management question from Pass 2 (item A3): the FY25 release and FY26 rebuild look
like discretionary or model-recalibration decisions independent of underlying loan-book scale, which is
exactly the kind of provisioning behaviour a verifier and the operator should press on directly at the next
concall or via a written management query. (Guarantee: RHP Note 36 p.325/333, Note 47 p.332-333; AR
standalone Note 32 p.88. ECL: RHP Note 26-equivalent p.318; AR Consolidated Note 26 p.119.)

No other pattern-level test (contradiction, restated/reclassified prior-year figures, deliberately vague
disclosure, subsequent events, going-concern language) surfaced anything beyond what Pass 1 and Pass 2
already named. The standalone-vs-consolidated customer-concentration framing (Pass 1 Finding 9, Pass 2
item B4) and the standalone-vs-consolidated KMP remuneration gap (Pass 1 Finding 7) remain the two
clearest cross-statement inconsistencies; both were investigated to their evidentiary limit in Pass 2 and
are carried into the consolidation below rather than re-litigated.

Going-concern language: searched across both note sets and the auditor's report. **NONE found.** Going
concern basis is stated as routine (Note 2, p.69); no emphasis-of-matter, no qualification, clean CARO,
clean audit opinion (Independent Auditor's Report paras 13(vi)-(vii), p.96-97).

Restatements/regroupings: the only quantified regrouping across all periods checked is the RHP's
Rs 0.17 million FY24 revenue/other-income reclass (Pass 2 item A5) — immaterial. The AR's own
FY26-vs-FY25 comparative regrouping language (standalone Note 43 p.93, consolidated Note 46 p.131)
remains unquantified and is not covered by the RHP's window; carried forward as an open, likely-immaterial
residual.

---
## A SYMMETRIC READING OF THE TWO STRUCTURAL FINDINGS (bull case and bear case, same evidence bar)

Two Pass 1/2 findings describe a pattern common to many Indian fintech-over-NBFC group structures: a
listed, asset-light parent that sources and services loans for a fee, and guarantees a wholly-owned,
separately-licensed NBFC subsidiary that carries the loan book and the formal credit risk. Both findings
deserve the benign reading stated alongside the concern, with the specific observation that separates the
two readings named explicitly, per the operator's instruction to this pass.

**Finding: parent corporate guarantee to Si Creva's lenders.**
- Benign reading: a parent guarantee to a wholly-owned NBFC subsidiary's lenders is a standard credit
  enhancement in Indian fintech-NBFC group structures. It lowers the subsidiary's cost of funds and is a
  normal feature of how a listed platform company backs its licensed lending arm; guarantees of this kind
  are common wherever a group separates the fee-earning origination/servicing entity from the
  balance-sheet-carrying regulated lender.
- Concerning reading: the guarantee (Rs 21,982.06 mn, FY26) is 228% of the parent's own standalone net
  worth (Rs 9,640.57 mn), a ratio that has risen every year for four straight years (70.3% FY23 to 228.0%
  FY26) and first exceeded 100% of net worth in FY24, two full years before the IPO. It backs 99.8% of the
  subsidiary's NCD book. At this scale the guarantee stops functioning as a genuine backstop: if invoked at
  any material fraction of its face value, the parent could not honour it from its own balance sheet.
- The observation that separates the two readings: whether the guarantee amount sits within the parent's
  capacity to actually make good on it. A guarantee below 100% of net worth is a real backstop; one that
  has run above 100% for three consecutive years (FY24, FY25, FY26) is a promise the numbers say the
  parent cannot keep at scale. FY24 (104.6%) is the specific crossover point; everything since has widened
  the gap, independent of the IPO. (Standalone Note 32 p.88, Note 31 p.88; Consolidated Note 18 p.116-117,
  Note 36 p.123-124; RHP Note 36 p.325/333, Note 47 p.332-333.)

**Finding: profit allocation skewed toward the risk-free parent.**
- Benign reading: the parent earning sourcing, servicing, and guarantee fee income while the licensed NBFC
  subsidiary carries formal credit risk is standard division-of-labour economics in a business-correspondent
  / co-lending style group. The guarantee fee itself is not obviously mispriced: guarantee fee income of
  Rs 394.06 mn against an average guarantee balance of roughly Rs 17,099.85 mn ((12,217.64+21,982.06)/2)
  implies a fee rate near 2.3% per year, broadly in line with market pricing for corporate credit
  enhancement rather than a below-market transfer.
- Concerning reading: the parent holds 43.9% of consolidated net assets but earns 49.3% of consolidated
  profit, while the risk-bearing subsidiary holds 56.1% of net assets and earns only 50.7% of profit
  (Consolidated Note 47, p.131). Fee income is extracted at the entity that carries none of the credit risk,
  ahead of any credit losses the risk-bearing entity may yet realise. No RPT benchmarking basis is disclosed
  (Note 34(5) asserts arm's length without evidence).
- The observation that separates the two readings: the guarantee fee rate looks broadly market-consistent
  (supports the benign reading on pricing), but the underlying guarantee itself already exceeds the parent's
  capacity to honour it (the finding above). A profit split that rewards the parent for bearing risk it
  structurally cannot absorb is different from one that rewards it for a genuinely transferable and
  affordable risk. The fee-pricing evidence and the guarantee-capacity evidence point in different
  directions, which is why this sits at 🟡 Watch rather than either a clean pass or a standalone red flag.

---
═══════════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Parent corporate guarantee to Si Creva's lenders has risen every year for 4 years: 70.3% of parent net worth (FY23) to 228.0% (FY26); crossed 100% in FY24, two years pre-IPO | Standalone Note 32 p.88, Note 31 p.88; RHP Note 36 p.325/333, Note 47 p.332-333 | 🔴 | Directly evidences LBF-4. The parent cannot honour this guarantee from its own balance sheet if called at scale; not an IPO-adjacent optic but a structural, worsening trend |
| 2 | Stage 3 (GNPA-equivalent) ratio of 2.12% is sustained by a ~15.7% annual write-off rate (Rs 4,725.95 mn written off, +10.7% YoY) while new inflow into Stage 3 grew 28.9% YoY; the 150-DPD write-off trigger is confirmed absent from BOTH the AR and the RHP | Consolidated Note 41 pp.127-129, Note 26 p.119; RHP p.278/350 | 🔴 | Directly evidences LBF-1. Low/improving headline asset-quality ratio is a write-off artefact, not evidence of improving credit quality; the specific control (DPD trigger) that would let a verifier test this independently is undisclosed in both filed documents |
| 3 | FLDG/off-balance-sheet guarantee cost more than tripled group-wide (standalone Rs 1,009.47 mn + consolidated Rs 1,546.85 mn FY26, vs combined well under Rs 0.8 bn FY25), outpacing revenue growth | Standalone Note 25 p.84; Consolidated Note 29 p.119-120 | 🔴 | Directly evidences LBF-2. Off-book guarantee cost is compounding faster than the business that generates it, a leading indicator for future credit-cost pressure as off-book AUM scales |
| 4 | 99.8% of the subsidiary's NCD book, and most of its term loans, rest on the same parent guarantee already exceeding parent net worth (Finding 1) | Consolidated Note 18 p.116-117, Note 19 p.117-118, Note 36 p.123-124 | 🔴 | The Group's borrowing structure is not standing on diversified, independently-adequate capital; it is contingent on a guarantee the numbers say the parent cannot fully honour |
| 5 | Guarantee growth (steady 74-80% YoY every year) and the ECL build-release-rebuild cycle (charge, larger charge, release, charge) do NOT move together — ruling out "book growth explains the FY25 release" | Consolidated Note 26 p.119; RHP p.318 (guarantee: Note 36 p.325/333) | 🟡 | Pass 3 pattern finding. Narrows the explanation space for the unexplained FY25 release to a discretionary or model-recalibration decision, sharpening the management question rather than resolving it |
| 6 | Four-year ECL build-release-rebuild cycle confirmed identical in AR and RHP at the overlap point (FY23 +443.57, FY24 +2,603.50, FY25 (1,652.04), FY26 +495.27, Rs mn), no narrative explanation in either document for any swing | Consolidated Note 26 p.119; RHP p.318 | 🟡 | A recurring, unexplained provisioning pattern across a listing event deserves a specific answer on what changed each year |
| 7 | Management overlay ECL (Rs 1,359.53 mn) is 59% the size of the model's own ECL output (Rs 2,309.56 mn) and stayed roughly flat while base model ECL grew 27% | Consolidated Note 41 p.127 | 🟡 | A very large, largely static discretionary layer for a newly listed lender; investors cannot see what judgment underlies more than a third of total reported ECL coverage |
| 8 | Related-party profit allocation favours the risk-free parent: 43.9% of consolidated net assets earns 49.3% of consolidated profit, vs the risk-bearing subsidiary's 56.1%/50.7% split; guarantee fee rate (~2.3% of average guarantee) looks broadly market-consistent | Consolidated Note 47 p.131; Standalone Note 34 pp.88-90 | 🟡 | Symmetric reading above: fee pricing looks fair on its own, but is paid by an entity (Finding 1) that structurally cannot back the risk it is compensated for taking on |
| 9 | Amortisation useful life for in-house software extended 5→10 years at the START of FY26, unquantified across BOTH the AR (signed 27-May-2026) and the RHP (dated 25-Apr-2026, ~9 months of investor visibility pre-listing) | Standalone Note 2.15 p.72; Consolidated Note 2.16 p.105; RHP p.278/350 | 🟡 | A profit-lifting policy change with zero quantified impact disclosed in either of two independent, SEBI-reviewed filings is a genuine, sustained disclosure gap |
| 10 | KMP remuneration understated by 60% if only the standalone RPT note is read: CEO and CFO each show Rs 10 mn standalone vs Rs 25 mn consolidated for FY26 | Standalone Note 34C p.89; Consolidated Note 38(b) p.124-125 | 🟡 | An investor reading only the parent-company notes materially understates promoter-management total compensation |
| 11 | Standalone revenue concentration (74.7% in three unnamed counterparties) appears to contradict the Group-level "no customer ≥10%" statement; reconcilable by differing definitions of "customer," confirmed as a 4-period pattern on the consolidated side but unverifiable across years on the standalone side (RHP carries no standalone-only note set) | Standalone Note 40 p.93; Consolidated Note 44 p.126; RHP p.333 | 🟡 | A genuine cross-statement framing inconsistency; an investor relying on only one note set gets a materially different concentration picture |
| 12 | New "Loan Against Property" business line disclosed at Group level with no corresponding standalone mention and no separate size/quality disclosure anywhere in the notes | Consolidated Note 1 p.101 | 🟡 | A new asset class inside a book otherwise described as ~92% unsecured personal loans changes the risk mix in a way the notes do not let an investor size |
| 13 | Liquidity risk note discloses only the financial-LIABILITY maturity ladder; no financial-asset (loan book) maturity table exists anywhere in the notes | Consolidated Note 41B pp.128-129 | 🟡 | A true asset-liability maturity gap cannot be assessed from the notes alone for an NBFC whose core risk is exactly that mismatch |
| 14 | Undrawn bank credit lines rose ~31x (Rs 61.72 mn to Rs 1,910.65 mn) | Consolidated Note 41B p.128 | 🟡 | Scale of the jump on a near-zero base is itself worth a management question on whether it is IPO-proceeds-linked or organically negotiated headroom |
| 15 | Interest rate risk is small and the lending book is fixed-rate matched (13.7% of borrowings floating; a 0.5% rate move affects P&L by only Rs 16.39 mn) | Consolidated Note 41D p.129 | 🟢 | A genuinely clean finding that balances the red flags above: no material floating-rate funding-cost squeeze on a fixed-rate lending book |

---
## B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 6.5 | EIR-based recognition, no accrual of overdue interest until cash received (conservative, Note 2.7(i)); offset by upfront (rather than amortised) recognition of Excess Interest Spread on direct-assignment sales, the more aggressive of two permitted treatments, currently small in absolute terms (Rs 89.70 mn FY26) |
| Expense capitalisation honesty | 5.0 | Software useful-life extension (5→10 yrs) adopted at FY26 start, unquantified across two independent filings (AR and RHP) covering 9+ months of investor visibility |
| Provisioning adequacy | 4.0 | Aggressive, rising write-off rate (~15.7% p.a.) alongside 28.9% growth in new Stage-3 inflow; a large, largely static management overlay (59% of model ECL); an unexplained four-year build-release-rebuild cycle |
| RPT fairness | 5.0 | Single dominant related party (30.3% of standalone revenue) asserted arm's length without benchmarking; guarantee fee rate looks market-consistent on its own; profit allocation skews toward the risk-free parent; KMP comp visibility gap between standalone and consolidated notes |
| Disclosure transparency | 4.5 | 150-DPD write-off trigger undisclosed in both the AR and RHP; asset-side maturity ladder absent from the liquidity note; new Loan Against Property line unsized; useful-life change unquantified |
| Consistency with prior years | 7.0 | Guarantee/net-worth escalation and the ECL cycle are both confirmed as genuine, long-running multi-year patterns (not new, not IPO-adjacent surprises) once cross-checked against the RHP; only trivial (Rs 0.17 mn) regrouping found in the checkable window; no restatement surprises; MSME timeliness and borrowings-at-parent-level clean and consistent |
| **OVERALL** | **5.0** | Simple average of the six dimensions, rounded. Three 🔴 red flags (guarantee-to-net-worth structure, write-off-masked asset quality, FLDG cost escalation) sit alongside genuinely clean findings (MSME timeliness, matched fixed-rate funding, no going-concern language, clean audit opinion); net picture is moderate-to-concerning, not alarming and not clean |

---
## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Parent guarantee exceeds its own capacity to honour it | High | Guarantee-to-net-worth ratio each quarter; pace of parent capital infusion into the subsidiary | A credit-quality shock in the unsecured personal-loan book that causes subsidiary lenders to invoke the guarantee at scale |
| Write-off pace masks true asset-quality deterioration | High | Stage-3 inflow rate, gross write-off rate as % of average book, any disclosed vintage/cohort delinquency data | If the write-off pace cannot keep outrunning inflow, or if the auditor/RBI tightens the write-off policy |
| FLDG/off-balance-sheet guarantee cost scaling faster than revenue | Medium-High | FLDG cost as % of off-book AUM; FLDG provision balance (Group total ~Rs 851 mn at FY26-end) | If off-book AUM growth continues into a credit-cycle downturn |
| Large, static, discretionary ECL overlay and an unexplained multi-year build-release cycle | Medium | Overlay-to-model-ECL ratio; any future large release or build disclosed at results | Next results call or annual report where a swing recurs without explanation |
| RPT/fee concentration and profit-allocation skew toward the risk-free parent | Medium | RPT as % of standalone revenue trend; standalone vs consolidated profit split each year | If subsidiary-level credit costs spike after parent-level fee profit has already been booked and distributed |
| Disclosure gaps (DPD trigger, asset-side ALM, unquantified accounting changes, unsized LAP book) | Medium | Any future quantification, or a live-verification hit that surfaces a discrepancy | If a regulator, auditor, or independent verification exercise queries one of these gaps directly |

---
## D. FIVE QUESTIONS FOR MANAGEMENT

1. What specific DPD (days-past-due) threshold, if any, triggers a write-off, and why does neither the AR
   nor the RHP disclose a numeric trigger despite qualitative "no reasonable expectation of recovery"
   language in both.
2. What specifically drove the FY25 release of Rs 1,652.04 million in standard-asset ECL, and what drove
   the FY26 rebuild — a model recalibration, a macro-overlay unwind, or a genuine credit-quality change?
   Given the guarantee (a proxy for book growth) grew at a steady 74-80% pace through both years, growth
   mechanics alone do not explain the swing.
3. What is management's target ceiling, if any, for the parent's corporate guarantee to Si Creva's lenders
   as a percentage of the parent's own net worth, given the ratio has risen every year since FY24 and now
   stands at 228%?
4. What is the quantified profit-and-loss impact, in the year of adoption and prospectively, of extending
   the in-house software amortisation useful life from 5 to 10 years?
5. What is the current size and risk profile of the new Loan Against Property book within the consolidated
   Rs 35,562.55 million loan book, and how does its underwriting differ from the unsecured personal-loan
   book?

---
## E. NOTES-BASED RED FLAGS

- Aggressive, rising write-off policy (~15.7% of average book annually, +10.7% YoY) sustaining a stable-
  to-improving Stage-3 ratio even as new defaults entering Stage 3 grew 28.9% YoY. Evidenced, not
  alleged: the ratio's stability is a mechanical consequence of removing defaulted assets from the
  denominator, not of improving credit selection.
- Parent corporate guarantee to the subsidiary's lenders has exceeded the parent's own net worth for
  three consecutive years (FY24-FY26) and widened every year, a structural capital-adequacy issue
  independent of the listing event.
- FLDG/off-balance-sheet guarantee cost tripled group-wide, materially outpacing revenue growth.
- The 150-DPD write-off trigger cited in company context is confirmed absent from both filed documents
  available in this container (AR and RHP); this is an undisclosed control that a verifier cannot test from
  the notes alone.
- Unquantified accounting policy change (software amortisation life) sustained across two independent
  filings spanning roughly nine months.
- No evidence of outright earnings management (no revenue-recognition manipulation, no aggressive
  capitalisation of routine expenses, no unusual reserve movements bypassing P&L, clean audit opinion,
  clean CARO) — the concerns above sit in the provisioning/guarantee/disclosure category, not in
  fabricated or manipulated top-line figures.

---
## F. ONE-LINE NOTES VERDICT

The notes reveal moderate to concerning accounting practices. Key concern: an aggressive and rising
write-off policy sustains a stable GNPA-equivalent ratio while new defaults grow 29% a year, sitting on
top of a parent guarantee that has exceeded its own net worth for three straight years and keeps
widening. Key strength: clean MSME payment discipline, matched fixed-rate funding with negligible
interest-rate exposure, no restatement surprises, no going-concern language, and a clean audit opinion.
Overall accounting quality: 5/10.
