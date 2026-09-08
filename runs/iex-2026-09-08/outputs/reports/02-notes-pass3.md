# IEX — Stage 2 Notes Triple-Pass — PASS 3 (PATTERN PASS + CONSOLIDATION)

Run date: 2026-09-08. Source: `runs/iex-2026-09-08/work/annual-report__Annual_Report_2026.txt`
(FY2025-26 Annual Report, board-approved 23-Apr-2026, filed to BSE 14-Aug-2026).

## MECHANICAL GAP DECLARED UP FRONT

`runs/iex-2026-09-08/outputs/reports/02-notes-pass1.md` does not exist in the run
folder. Only `02-notes-pass2.md` was found. This is a mechanical failure of the
pipeline handoff, not a company-quality issue, so per the operating rules this run
does not halt; it proceeds and the gap is logged and compensated for.

Compensation method: Pass 2's own text extensively quotes and cross-references Pass
1's findings verbatim ("Pass 1's ₹3.32cr accrual finding," "Pass 1 wrote '~889.3cr
shares outstanding,'" "already flagged by Pass 1," etc.), which recovers a
substantial share of Pass 1's content indirectly. Cross-stage evidence from Stage 1
(Gate 0) supplied additional anchored figures (contingent liabilities, the RTM
volume-share contradiction). For everything else a genuine Top-15 consolidated list
needs — trade receivables ageing, the cash flow statement, revenue disaggregation
(Note 28), other income breakup (Note 29), deferred tax (Note 21/33), the settlement
liability structure (Note 41), contingent liabilities (Note 39), operating segments
(Note 44), and the market-coupling note (Note 47) — this pass re-read the primary
source directly rather than rely on an absent Pass 1. Every figure below carries its
own page anchor, opened and verified in this pass. This is logged as an input_gap
(`pass1_output_missing`) in the YAML block below.

## PATTERN PASS: DIRECTED CONTRADICTIONS

### 1. Whistleblower status: Board's Report vs Notes 46/49 — sharpened, not resolved

Both approved by the same Board on the same date, 23-Apr-2026:
- Board's Report (Annual Report FY26, p.80): investigation described as concluded,
  "based on the findings of the investigation, appropriate actions were implemented."
- Note 46 standalone (p.224) / Note 49 consolidated (p.290): "The Audit Committee
  has initiated an independent investigation, which remains ongoing as at the date
  of approval of the financial statements by the Board... which do not have a
  material impact." Point-in-time verified again this pass at p.224 (Note 46 sits
  immediately before Note 47, the market coupling note, on the same page).

Pass 2 already found the corroborating evidence: CARO Annexure I clause xi
(standalone p.176-177) uses the identical "ongoing... as on the date of our audit
report" framing, and the consolidated auditor's report confirms no adverse CARO
remarks anywhere in the group. That makes THREE independent documents (the Notes,
CARO, and by extension the auditor's own procedures) agree the investigation was
still open at sign-off, against ONE document (the Board's Report) that says it
concluded. The weight of evidence favours the Notes/auditor framing. The most
likely explanation, unresolved by the AR itself, is that the Board's Report prose
describes an earlier procedural step (the Audit Committee's initial review that
triggered the investigation) in language loose enough to read as a conclusion. This
pass does not find new evidence that changes Pass 2's conclusion; it sharpens the
conclusion from "contradiction, unresolved" to "contradiction, weight of evidence
favours the Notes' 'still open' reading, Board's Report is the outlier document."

### 2. MSME dues: Note 23 vs Note 52 — sharpened, not resolved

Re-verified directly this pass. Note 23, standalone trade payables classification
(p.209): total outstanding dues to micro/small enterprises = ₹38.03L FY26 vs ₹6.76L
FY25 (+462%). Note 52, the dedicated MSMED Act, 2006 disclosure (p.226): "Dues
remaining unpaid to any supplier — Principal" = ₹44.41L FY26 vs ₹76.90L FY25 (-42%).
Same balance sheet date, same underlying population in principle (MSME supplier
dues outstanding at year end), opposite YoY direction, and neither note
cross-references the other. The pattern repeats in the consolidated statements
(Note 22 vs Note 48). Both notes agree on one point: zero interest accrued or paid
under the MSMED Act, either note, either year, either statement — so this is not a
disclosed compliance failure, it is an unreconciled pair of sub-schedules. Sharpened
judgement: the two notes almost certainly draw from two different source systems
(Note 23's ageing schedule sits inside the formal trade-payables ageing exercise,
which carries a separate ₹335.03L unclassified "Accruals" plug not split by
MSME/non-MSME status; Note 52 is likely sourced from a supplier-master MSME-flag
query run independently for statutory-disclosure purposes). The AR states neither
mechanism nor reconciliation; this remains inference. Immaterial in rupee terms
against ₹1,364.56cr net worth.

### 3. Read across the disclosure set: pattern, not three unrelated slips

Three internal numeric/status inconsistencies now stand inside one FY26 annual
report, all board-approved 23-Apr-2026:
- RTM FY26 volume share: 34% at p.17, p.25, p.62 vs "nearly 40%"/"approximately
  39%" at p.33, p.36-37 (Stage 1 Gate 0 finding, cross-stage evidence, not
  re-derived in this pass).
- Whistleblower status: concluded (Board's Report, p.80) vs ongoing (Notes 46/49,
  p.224/p.290).
- MSME dues: rising (Note 23, p.209) vs falling (Note 52, p.226).

A fourth item, found fresh in this pass, is adjacent in character though not a
strict numeric contradiction: Note 47 (p.224-225) narrates the CERC market-coupling
order, the APTEL ruling and the Supreme Court civil appeal in full prose, but
carries no rupee amount, no probability assessment, and is not classified as a
contingent liability — unlike Note 39 (p.217), which gives the far smaller ₹5.04cr
GST dispute a complete management assessment ("not tenable... no amount will be
payable"). The largest structural risk in the filing is the least quantified line
in the financial statements.

Judgement, anchored: this reads as a disclosure-quality pattern, not three
unrelated drafting slips. The common thread is not carelessness within any single
note — each note, read alone, is detailed and internally consistent (the RTM
percentages are each individually sourced to named data providers in their own
sections; Note 23's ageing schedule is complete; Note 52 follows the MSMED Act
template exactly; Note 47 narrates the litigation timeline accurately). The common
thread is that THE SAME underlying fact gets a different number or characterisation
depending on WHICH section of the report supplies it — MD&A narrative vs formal
Notes, Board's Report vs Notes, one Notes sub-schedule vs another Notes
sub-schedule. That is consistent with sections being drafted by different
functions (investor relations/MD&A, company secretarial, financial
controllership, legal) without a final cross-document reconciliation pass before
sign-off, rather than with any single author being sloppy. It is a process
observation about how the AR is assembled, not a finding about the underlying
business or its cash economics, and none of the four items move any audited total.

## EARNINGS QUALITY, TRACED ACROSS ALL THREE PASSES

Operating revenue vs treasury and IGX equity pickup (Note 28/29 standalone p.211;
Note 33 consolidated p.275, all re-verified this pass):
- Standalone: revenue from operations ₹608.39cr, other income ₹136.55cr (18.3% of
  ₹744.94cr total income), PBT ₹624.81cr, PAT ₹473.71cr, basic/diluted EPS ₹5.33.
- Consolidated: PBT ₹645.56cr (matches the spear-gate load-bearing fact in
  companies/IEX.md and B00-inputs.yaml exactly), profit attributable to equity
  shareholders ₹492.92cr, basic/diluted EPS ₹5.54. The ₹19.21cr gap between
  standalone and consolidated PAT (₹473.71cr to ₹492.92cr) is the net effect of the
  IGX equity-method pickup (Stage 1 cross-stage evidence: IGX FY26 PAT growth
  35.29%) offset by ICX subsidiary losses and minority interest; the Notes do not
  give a single-line reconciliation of this ₹19.21cr bridge, so the exact IGX
  contribution inside it is not separately stated anywhere in the standalone or
  consolidated Notes.
- Other income composition (Note 29, p.211): almost entirely treasury —
  interest income on amortised-cost investments ₹57.51cr, fair value gains on FVTPL
  investments ₹33.97cr, gains on sale of investments ₹23.29cr + ₹8.09cr, dividend
  income ₹5.37cr, bank deposit interest ₹5.09cr. None of it is disclosed as
  recurring in the sense of being contractually assured; all of it is a function of
  the size and allocation of the ₹1,900+cr treasury book (Note 41, fair value
  hierarchy, p.214-215), which itself was reallocated meaningfully within the year
  (Pass 2 Finding 9, confirmed this pass: Level-1 target-maturity/fixed-maturity
  holdings cut 96.7%, market-linked debentures fully exited, equity-index mutual
  fund exposure up 280%).

Settlement float's effect on CFO: the cash flow statement (p.183-184, re-read in
full this pass) backs treasury-related non-cash items (fair value gains, gains on
sale, EIR-accrued interest income) out of operating cash flow and shows the actual
cash received from investments (₹82.48cr interest, ₹5.37cr dividend) under investing
activities, not operating. This is standard treatment and it means net operating
cash flow (₹424.64cr FY26) understates total company cash generation relative to
PAT (which includes the treasury income); it is not evidence of aggressive revenue
recognition, it is a classification consequence of holding a large investment book.
Separately, the member settlement/margin money the Company holds on behalf of
members sits in "Other financial liabilities — Others (excluding settlement
guarantee fund), Current" at ₹951.27cr FY26 vs ₹946.07cr FY25 (Note 41, p.219) —
larger than the Company's entire net worth. This is not IEX's capital and does not
move through the P&L; it is disclosed as a financial liability at amortised cost,
approximately equal to fair value, with no volatility signal. The visible cash
counterpart sits in "balances with banks — in settlement accounts," ₹23.10cr FY26
vs ₹44.25cr FY25 (Note 12, p.203) — a modest, declining slice of total cash, most of
the settlement obligation being funded and returned same-day or next-day per the
credit-risk note (p.221).

Does reported PAT convert to cash: standalone net CFO ₹424.64cr against standalone
PAT ₹473.71cr is 89.6% conversion — a reasonable ratio for a company where roughly
a fifth of PBT is treasury income booked through investing rather than operating
cash flow. Trade receivables are trivial (₹1.22cr, Note 11, p.202) and fully
current, so working-capital drag is not a factor holding back conversion; the gap
is explained almost entirely by the operating/investing classification split on
treasury income, not by any deterioration in collections or accruals quality.
Overall verdict on earnings quality: the core transaction-fee business converts
cleanly to cash; the treasury sleeve (18% of total income) is real cash income too,
just parked one line down the cash flow statement from where PAT would suggest.

## WHAT AN INVESTOR CANNOT LEARN FROM THESE NOTES

- No rupee split within the "Electricity" revenue bundle (Note 28, p.211): DAM,
  RTM, TAM and Green segment transaction-fee revenue are reported as one combined
  line, ₹558.51cr FY26. The volume-share percentages quoted narratively elsewhere in
  the AR (and which themselves conflict, see above) cannot be checked against
  revenue mix because no revenue-basis segment split exists below the two-way
  Electricity/Certificates cut.
- No quantified financial-impact estimate for the CERC market-coupling litigation
  (Note 47, p.224-225), despite it being the single largest structural regulatory
  risk to the DAM franchise. No probability language, no amount, no contingent
  liability entry.
- No identity or nature disclosed for the single customer contributing 16.2% of
  FY26 revenue from operations (₹98.62cr, Note 28, p.211, up from 15.65%/₹83.79cr
  FY25) — whether this is a large discom, a scheduled entity, or a category of
  member is not stated.
- No explicit bridge reconciling standalone PAT (₹473.71cr) to consolidated profit
  attributable to equity shareholders (₹492.92cr); the IGX equity-pickup
  contribution inside that ₹19.21cr gap is not separately stated.
- No rationale given for the FY26 treasury reallocation out of target-maturity/
  fixed-maturity plans and market-linked debentures into arbitrage/liquid funds and
  equity-index funds (Note 41, p.214-215) — a genuine change in treasury risk
  posture with no stated reason.
- No disclosure anywhere in the Notes of the IGX OFS / 22.3% sell-down to the
  PNGRB 25% ownership ceiling (a spear-gate load-bearing fact); the only trace of
  an IGX-level control gap in the whole filing is the consolidated auditor's Rule
  11(g) audit-trail exception (p.234-236, outside the Notes, found by Pass 2).
- No management explanation reconciling Note 23 to Note 52 on MSME dues, or any
  acknowledgement that the two notes disagree.

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Whistleblower investigation status conflict: Board's Report (p.80) says concluded with findings/remedial action; Notes 46/49 (p.224/p.290) say still ongoing; both signed 23-Apr-2026. CARO corroborates the Notes' framing. | Note 46/49 | RED FLAG | Same-board same-date contradiction on a fraud/conflict-of-interest matter; governs whether "no material impact" was reached before or after substantive findings were known. |
| 2 | Market-coupling regulatory exposure carries zero quantification or contingent-liability classification, versus full treatment for the far smaller ₹5.04cr GST matter. | Note 47 vs Note 39 | RED FLAG | The single largest structural risk to the DAM franchise is the least-quantified item in the financial statements. |
| 3 | MSME dues contradiction: Note 23 shows dues rising 462% to ₹38.03L; Note 52 shows dues falling 42% to ₹44.41L; same date, unreconciled; repeats in consolidated. | Note 23/52 | RED FLAG | Genuine internal-consistency gap; immaterial in rupees but a disclosure-control weakness. |
| 4 | RTM FY26 volume share stated inconsistently across the AR: 34% (p.17/25/62) vs ~39-40% (p.33/36-37); no revenue-basis split exists to arbitrate. | MD&A, cross-referenced by Note 28 | RED FLAG | Third internal inconsistency in the same report; blocks verification of the market-coupling exposure's revenue base. |
| 5 | Single customer contributes 16.2% of FY26 revenue from operations (₹98.62cr), up from 15.65% (₹83.79cr) FY25; identity undisclosed. | Note 28 | WATCH | Real concentration risk in a two-sided exchange model; durability unknown. |
| 6 | Trade receivables trivial and clean: ₹1.22cr FY26 (down from ₹2.01cr), 100% under 6 months, zero disputed/credit-impaired/not-due/unbilled. | Note 11 | CLEAN | Confirms the pre-funded settlement model carries near-zero credit risk; a genuine strength. |
| 7 | Member settlement/margin liability of ₹951.27cr sits on the balance sheet (Other financial liabilities, current, excl. SGF), larger than net worth; not IEX's capital, no P&L exposure. | Note 41 | CLEAN (informational) | Explains why balance-sheet ratios read unlike a normal company's; must not be mistaken for leverage. |
| 8 | ESOP charge nearly halved YoY (₹80.59L vs ₹164.65L, -51%) despite a fresh 1,00,000-option grant; total options outstanding fell as forfeitures+exercises outpaced the new grant; diluted EPS impact stays under 0.003% via treasury-stock-method netting. | Note 51 | WATCH | Mechanical explanation plausible (largest historical tranche nearing end of vesting) but not stated by the company. |
| 9 | Investment book fair-value hierarchy shows a sharp within-year reallocation: Level-1 TMF/FMP cut 96.7%, MLD fully exited, equity-index MF exposure up 280%; no stated rationale. | Note 41 | WATCH | Genuine change in treasury risk posture on a ₹1,900+cr book, unexplained. |
| 10 | Contingent liabilities: single GST dispute, ₹5.0376cr total, 0.37% of net worth, management assesses not tenable; no guarantees for subsidiaries. | Note 39 | CLEAN | Small, well-characterised, fully assessed — the contrast case for finding 2. |
| 11 | Standalone CFO ₹424.64cr vs PAT ₹473.71cr, 89.6% conversion; gap explained by treasury income sitting in investing not operating cash flow, not by working-capital drag or accrual quality. | Cash Flow Statement | CLEAN | Core business converts cleanly to cash; treasury income is real cash, one line removed from CFO. |
| 12 | Related party transactions: KMP variable-pay payable rose ₹278.22L to ₹332.31L; ICX recoverable balance collected down 93% (₹159.87L to ₹11.22L); all transactions small; CARO confirms ss.177/188 compliance. | Note 50 | CLEAN | No non-arm's-length signal found; completeness addition over the P&L-only table. |
| 13 | Deferred tax: net DTL ₹29.21cr FY26 (down from ₹34.62cr), driven by investment fair-value and ROU timing differences; effective rate 24.18% vs enacted 25.17%, mild favourable variance from capital-gains-rate differences. | Note 21/33 | CLEAN | No aggressive DTA recognition; movement is mechanical and explained. |
| 14 | Consolidated auditor's report carries a Rule 11(g) audit-trail exception specific to IGX's third-party accounting software (no visibility on database-level edit logs); standalone audit trail fully clean; not disclosed in the Notes themselves. | Consol Auditor's Report, outside Notes | WATCH | Layers on top of the Notes' silence on IGX OFS/dilution; a real visibility gap at the associate level. |
| 15 | Revenue Key Audit Matter (fraud-risk presumption under SA 240) cross-checked total revenue to monthly GST returns and traded volumes to NLDC/RLDC/CERC data; no exceptions noted. | Auditor's Report, both statements | CLEAN | Independent external corroboration of revenue integrity beyond management representation. |

### B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 8 | Point-in-time recognition under Ind AS 115, KAM-level external cross-check to GST/NLDC/RLDC/CERC data, zero unbilled receivables, contracted-price-to-recognised-revenue reconciliation disclosed. |
| Expense capitalisation honesty | 8 | Useful lives disclosed and stable, no aggressive capitalisation observed, ESOP fully and transparently expensed. |
| Provisioning adequacy | 7 | The one item classified as a contingent liability (GST, ₹5.04cr) is fully assessed; the far larger market-coupling exposure receives no provisioning treatment or quantification at all (Note 47), which caps this dimension below where the GST-only evidence would otherwise put it. |
| RPT fairness | 7 | Transactions small, CARO confirms s.177/188 compliance; no explicit arm's-length pricing commentary in the Notes themselves. |
| Disclosure transparency | 4 | Three same-report internal contradictions (whistleblower status, MSME dues, RTM volume share) plus one major unquantified risk sitting beside a fully quantified trivial one; this is the dimension the pattern pass exists to catch, and it is the weakest one in this filing. |
| Consistency with prior years | 8 | Accounting policies unchanged, no restatements or reclassifications found, YoY ratio variances explained (Note 49). |
| **OVERALL** | **6/10** | Moderate. Every reported number checks out and reconciles internally; what does not reconcile is which of two or three competing narratives about status or materiality to believe. Unqualified audit opinion both statements, fraud-focused KAM found nothing, no going-concern language. |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Market-coupling regulatory restructuring of DAM, unquantified in the Notes | HIGH | CERC's draft (Power Market) (Second Amendment) Regulations, 2026 (issued 17-Apr-2026, Note 47); Supreme Court civil appeal outcome | On regulation finalisation or Supreme Court ruling; timing outside company's control |
| Single-customer revenue concentration, 16.2% and rising | MEDIUM | Whether the concentration customer's share keeps rising in FY27 quarterly disclosures | Gradual; visible in quarterly revenue mix if reported |
| Disclosure-reconciliation discipline across AR sections | MEDIUM | Whether FY27 AR reconciles MSME notes and resolves the whistleblower/Board's Report language gap | Next annual report cycle |
| IGX associate-level audit-trail visibility gap | LOW-MEDIUM | Whether the Rule 11(g) exception clears in FY27's consolidated audit report | Next annual audit cycle |
| Treasury book reallocation toward equity-linked exposure, unexplained | LOW | Whether the shift continues and whether price-risk sensitivity (currently trivial, ₹3.80L per 5% move) grows materially | Ongoing, visible each year in Note 41 |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. Which is accurate as of the 23-Apr-2026 Board approval: the Board's Report
   characterisation of the whistleblower investigation as concluded with findings
   and remedial action taken (p.80), or the Notes' characterisation of it as still
   open (Note 46/49)? What were the findings and what remedial action was taken?
2. What accounts for the divergence between Note 23's trade-payables MSME
   classification (₹38.03L, up 462%) and Note 52's MSMED Act disclosure (₹44.41L,
   down 42%) for the same balance sheet date, and will FY27 reconcile the two?
3. What is management's probability and financial-impact assessment of the CERC
   market-coupling litigation (Note 47), given DAM is the segment coupling would
   restructure, and why does this risk carry no contingent-liability entry while
   the much smaller GST matter does?
4. Who is the single customer contributing 16.2% of FY26 revenue from operations
   (₹98.62cr, up from 15.65%), and what is the durability of that relationship?
5. What drove the FY26 treasury reallocation out of target-maturity/fixed-maturity
   plans and market-linked debentures into arbitrage/liquid funds and equity-index
   funds, and does it reflect a deliberate change in risk appetite for the
   ₹1,900+cr treasury book?

### E. NOTES-BASED RED FLAGS

- Whistleblower investigation status conflict between the Board's Report and
  Notes 46/49, same Board, same sign-off date (23-Apr-2026).
- MSME dues contradiction between Note 23 and Note 52 (and their consolidated
  counterparts Note 22/48), same balance sheet dates, opposite YoY direction.
- RTM FY26 volume share stated inconsistently across the annual report (34% vs
  approximately 39-40%), with no revenue-basis split available to arbitrate.
- The company's largest structural regulatory risk (market coupling, Note 47)
  carries zero financial quantification or contingent-liability treatment, while a
  much smaller, unrelated dispute (GST, Note 39) receives full assessment.
No evidence of earnings management or aggressive accounting was found on any
audited total; all four items above are disclosure-consistency and
disclosure-completeness defects, not numeric manipulation.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices: clean and internally consistent
within each individual note, but inconsistent across the wider annual report on
three separate matters signed off the same day. Key concern: the whistleblower
status conflict between the Board's Report and Notes 46/49, compounded by an
unquantified market-coupling exposure and an unreconciled MSME dues pair. Key
strength: near-zero receivables risk, an unqualified audit opinion on both
statements, and a fraud-focused Key Audit Matter that found nothing. Overall
accounting quality: 6/10.

```yaml
stage: B02-notes
company: "IEX"
run_date: "2026-09-08"
model: claude-sonnet-5
status: complete
input_gaps:
  - type: pass1_output_missing
    severity: MEDIUM
    detail: >
      runs/iex-2026-09-08/outputs/reports/02-notes-pass1.md was not present in the
      run folder at Pass 3 start. Compensated by (a) Pass 2's extensive verbatim
      quoting and cross-referencing of Pass 1 findings, (b) Stage 1 cross-stage
      evidence, and (c) a fresh direct re-read of the primary Notes in this pass
      for receivables, cash flow, revenue/other-income disaggregation, deferred
      tax, the settlement-liability structure, contingent liabilities, operating
      segments and the market-coupling note. Every figure in this block carries
      its own page anchor opened in this pass or attributable to Pass 2's quotes.
  - type: rating
    severity: NOT_A_GAP
    detail: >
      inputs/rating/ empty. IEX has no listed debt (confirmed by borrowings, all
      Ind AS 116 lease liabilities, Note 41/43) and told BSE it does not qualify
      as a Large Corporate. Unrateable by absence of rated debt, not by missed
      collection.
  - type: research
    severity: LOW
    detail: "inputs/research/ empty. Broker notes are non-anchored, leads only."
  - type: regulatory_order_text
    severity: HIGH
    detail: >
      The CERC market-coupling order, the APTEL judgment, and the two Supreme
      Court orders are referenced in the corpus (and in Note 47, p.224-225) but
      their full texts are absent. Note 47 itself gives no financial
      quantification of this exposure, sharpening the need for the order texts.
  - type: screening_csv
    severity: MEDIUM
    detail: >
      screener-Profit_Loss.csv, screener-Balance_Sheet.csv, screener-Cash_Flow.csv
      and screener-Quarters.csv hold row labels and no values. Data_Sheet CSVs
      are populated and were not needed by this stage, which read the AR directly.
  - type: sector_cap_row
    severity: MEDIUM
    detail: >
      The Section 1B cap table has no Market Infrastructure/Exchange row.
      Not consumed by this stage; carried forward for Stage 11.
  - type: prospectus_own
    severity: NOT_A_GAP
    detail: "IEX listed in 2017; its own IPO prospectus is not foundational for this run."
  - type: image_only_pdfs
    severity: LOW
    detail: "Two SAST Reg 29(2) disclosures are scanned, non-extractable. Not needed by this stage."
flags: []
accounting_quality: 6        # /10
pass_2_empty: false
pass_3_empty: false
top_findings:                # max 15
  - {rank: 1, finding: "Whistleblower investigation status conflict: Board's Report (p.80) says concluded with findings and remedial action; Notes 46/49 (p.224/p.290) say still ongoing; both signed 23-Apr-2026. CARO corroborates the Notes' framing, making the Board's Report the outlier document.", note_ref: "Note 46 (standalone p.224) / Note 49 (consolidated p.290)", rating: "RED FLAG", why: "Governs whether 'no material impact' was reached before or after the investigation's substantive findings were known."}
  - {rank: 2, finding: "Market-coupling regulatory exposure (Note 47) carries zero financial quantification or contingent-liability classification, while the far smaller Rs5.04cr GST dispute (Note 39) receives a full management assessment.", note_ref: "Note 47 vs Note 39, p.224-225 vs p.217", rating: "RED FLAG", why: "The single largest structural risk to the DAM franchise is the least-quantified item in the financial statements."}
  - {rank: 3, finding: "MSME dues contradiction: Note 23 shows dues rising 462% to Rs38.03L; Note 52 shows dues falling 42% to Rs44.41L for the same balance sheet date; unreconciled; repeats in consolidated Note 22/48.", note_ref: "Note 23 (p.209) / Note 52 (p.226)", rating: "RED FLAG", why: "Genuine internal-consistency gap between two notes serving the same disclosure purpose; immaterial in rupees but a disclosure-control weakness."}
  - {rank: 4, finding: "RTM FY26 volume share stated inconsistently across the AR: 34% (p.17/25/62) vs approximately 39-40% (p.33/36-37); no revenue-basis segment split exists to arbitrate.", note_ref: "MD&A, cross-checked against Note 28 (p.211)", rating: "RED FLAG", why: "Third internal inconsistency in the same annual report; blocks verification of the market-coupling exposure's actual revenue base."}
  - {rank: 5, finding: "Single customer contributes 16.2% of FY26 revenue from operations (Rs98.62cr), up from 15.65% (Rs83.79cr) FY25; identity not disclosed.", note_ref: "Note 28, p.211", rating: "WATCH", why: "Real concentration risk in a two-sided exchange model; durability and identity unknown."}
  - {rank: 6, finding: "Trade receivables trivial and clean: Rs1.22cr FY26 (down from Rs2.01cr), 100% under 6 months, zero disputed, credit-impaired, not-due, or unbilled.", note_ref: "Note 11, p.202-203", rating: "CLEAN", why: "Confirms the pre-funded settlement model carries near-zero credit risk on members."}
  - {rank: 7, finding: "Member settlement/margin liability of Rs951.27cr FY26 sits on the balance sheet under Other financial liabilities (current, excl. settlement guarantee fund), larger than net worth; this is not IEX's own capital and carries no P&L exposure.", note_ref: "Note 41, p.219", rating: "CLEAN (informational)", why: "Explains why balance-sheet ratios read unlike a normal company's; must not be mistaken for leverage or liquidity risk."}
  - {rank: 8, finding: "ESOP charge nearly halved YoY (Rs80.59L vs Rs164.65L, -51%) despite a fresh 1,00,000-option grant on 29-Jul-2025; total options outstanding fell to 8,93,760 from 9,98,175 as forfeitures and exercises outpaced the new grant.", note_ref: "Note 51, p.224-225", rating: "WATCH", why: "Plausible mechanical explanation (largest historical tranche nearing end of vesting) but not stated by the company."}
  - {rank: 9, finding: "Investment fair-value hierarchy shows sharp within-year reallocation: Level-1 target-maturity/fixed-maturity plans cut 96.7%, market-linked debentures fully exited, equity-index mutual fund exposure up 280%; no stated rationale.", note_ref: "Note 41, p.214-215", rating: "WATCH", why: "Genuine, unexplained change in treasury risk posture on a Rs1,900+cr book."}
  - {rank: 10, finding: "Contingent liabilities: single GST dispute, Rs5.0376cr total (tax Rs260.71L + interest Rs216.97L + penalty Rs26.08L), 0.37% of net worth, management assesses not tenable; no guarantees for subsidiaries.", note_ref: "Note 39, p.217", rating: "CLEAN", why: "Small, well-characterised, fully assessed; the contrast case for finding 2."}
  - {rank: 11, finding: "Standalone net CFO Rs424.64cr vs PAT Rs473.71cr, 89.6% conversion; the gap is explained by treasury income sitting under investing rather than operating cash flow, not by working-capital drag or accrual quality.", note_ref: "Cash Flow Statement, p.183-184", rating: "CLEAN", why: "Core transaction-fee business converts cleanly to cash; treasury income is real cash, one line removed from CFO."}
  - {rank: 12, finding: "Related party transactions: KMP variable-pay payable rose Rs278.22L to Rs332.31L; ICX recoverable balance collected down 93% (Rs159.87L to Rs11.22L); all transactions small; CARO confirms ss.177/188 compliance.", note_ref: "Note 50, p.218 and p.223", rating: "CLEAN", why: "No non-arm's-length signal found."}
  - {rank: 13, finding: "Deferred tax: net DTL Rs29.21cr FY26 (down from Rs34.62cr), driven by investment fair-value and ROU timing differences; effective tax rate 24.18% vs enacted 25.17%, mild favourable variance from capital-gains-rate differences on investment sales.", note_ref: "Note 21 (standalone, p.208-209) / Note 33 (consolidated, p.275)", rating: "CLEAN", why: "No aggressive DTA recognition; movement is mechanical and fully explained."}
  - {rank: 14, finding: "Consolidated auditor's report carries a Rule 11(g) audit-trail exception specific to IGX's third-party accounting software (no visibility on database-level edit logs); standalone audit trail is fully clean; not disclosed in the Notes themselves.", note_ref: "Consolidated Auditor's Report p.234-236, outside the Notes", rating: "WATCH", why: "Layers on top of the Notes' complete silence on IGX's OFS/dilution, a spear-gate load-bearing fact."}
  - {rank: 15, finding: "Revenue Key Audit Matter (fraud-risk presumption, SA 240) cross-checked total revenue to monthly GST returns and traded volumes to NLDC/RLDC/CERC data; no exceptions noted.", note_ref: "Auditor's Report, both statements, p.172-173/p.231-232", rating: "CLEAN", why: "Independent external corroboration of revenue integrity beyond management representation."}
red_flags:
  - "Whistleblower investigation status conflict between the Board's Report (p.80, concluded) and Notes 46/49 (p.224/p.290, still ongoing), both signed 23-Apr-2026."
  - "MSME dues contradiction between Note 23 (p.209, rising) and Note 52 (p.226, falling), same balance sheet dates, and their consolidated counterparts."
  - "RTM FY26 volume share stated inconsistently across the annual report (34% vs approximately 39-40%), no revenue-basis split available to arbitrate."
  - "Market-coupling regulatory exposure (Note 47, p.224-225), the company's largest structural risk, carries zero financial quantification or contingent-liability treatment, unlike the much smaller GST matter (Note 39)."
questions_for_mgmt:
  - "Which is accurate as of the 23-Apr-2026 Board approval: the Board's Report's 'concluded with findings and remedial action' characterisation of the whistleblower investigation, or the Notes' 'still ongoing' characterisation? What were the findings and what remedial action was taken?"
  - "What accounts for the divergence between Note 23 (Rs38.03L, up 462%) and Note 52 (Rs44.41L, down 42%) on MSME dues for the same balance sheet date, and will FY27 reconcile the two schedules?"
  - "What is management's probability and financial-impact assessment of the CERC market-coupling litigation (Note 47), and why does it carry no contingent-liability entry while the much smaller GST dispute does?"
  - "Who is the single customer contributing 16.2% of FY26 revenue from operations (Rs98.62cr, up from 15.65%), and what is the durability of that relationship?"
  - "What drove the FY26 treasury reallocation out of target-maturity/fixed-maturity plans and market-linked debentures into arbitrage/liquid and equity-index funds, and does it reflect a deliberate change in risk appetite for the Rs1,900+cr treasury book?"
receivables_trend: "improving: standalone trade receivables Rs1.22cr FY26 vs Rs2.01cr FY25 (Note 11, p.202), entirely in the under-6-months bucket both years, zero disputed/credit-impaired/not-due/unbilled; reflects the pre-funded settlement model, not a working-capital risk indicator for this business."
restatements_found: []
going_concern_language: "NONE beyond standard boilerplate ('accrual and going concern basis,' p.185/p.262 area; capital-management going-concern objective language, p.220/p.284 area); no material uncertainty, no adverse opinion, no emphasis-of-matter paragraph in either the standalone or consolidated auditor's report."
analyst_note: >
  Pass 1's output file was missing from the run folder; this pass reconstructed
  Top-15 coverage from Pass 2's extensive quoting of Pass 1 plus a fresh direct
  re-read of the primary source (flagged as input_gap pass1_output_missing). The
  single most important read-across finding: three internal numeric or status
  contradictions (RTM volume share, whistleblower status, MSME dues) sit inside
  one board-approved annual report, all traceable to disagreement BETWEEN sections
  of the AR rather than errors WITHIN any one note. A fourth item, the unquantified
  market-coupling exposure against the fully-quantified trivial GST matter, is a
  materiality-judgement gap of the same character. None of this touches audited
  totals: the audit opinion is unqualified both statements, the fraud-focused KAM
  found nothing, and core operating cash conversion is clean. The accounting
  quality score of 6/10 reflects a report that is numerically trustworthy but
  cross-document-inconsistent on qualitative status and materiality calls, which
  downstream stages should treat as a disclosure-discipline flag, not an earnings
  quality flag.
```
