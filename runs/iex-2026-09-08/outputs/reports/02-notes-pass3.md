# IEX — Stage 2 Notes Triple-Pass — PASS 3 (PATTERN PASS + CONSOLIDATION)
## RUN 2 — full re-consolidation with all three real passes in hand

Run date: 2026-09-08. Source: `runs/iex-2026-09-08/work/annual-report__Annual_Report_2026.txt`
(FY2025-26 Annual Report, board-approved 23-Apr-2026, filed to BSE 14-Aug-2026).

## NOTE ON RUN 1

Run 1 of this pass executed while `02-notes-pass1.md` was absent from the run folder
(a mechanical handoff failure, external rebase mid-run). It compensated by
reconstructing Pass 1 content from Pass 2's verbatim quoting plus a fresh direct
re-read of the primary source, and logged `pass1_output_missing` as an input_gap.
Pass 1's output is now present and complete (31.5KB, read in full this run). This
run redoes the consolidation with all three real passes in hand. The
`pass1_output_missing` gap is RESOLVED and is not carried forward. Substantively,
Run 1's findings held up well against the real Pass 1 — nothing in Pass 1 contradicts
what Run 1 reconstructed. Two corrections came out of this run's own direct
page-anchor verification (see below), both citation-only, no figure changes.

## ANCHOR CORRECTIONS FOUND THIS PASS

This pass opened the whistleblower and MSME pages directly (as instructed) rather
than relying on the prior anchors. Three page-marker citations used by Pass 1/2/
Run-1-Pass-3 were off, all because the AR's printed footer page number runs 4 pages
behind the file's `=== PAGE n ===` marker in the standalone section (and similarly
in the consolidated section) — earlier passes anchored some findings to the printed
footer number instead of the file marker used everywhere else. Corrected here,
verified by opening each page:
- Note 49 (consolidated whistleblower disclosure): file marker **p.291**, not p.290
  as previously cited. Confirmed by direct read: page marker "=== PAGE 291 ==="
  (line 20370) immediately precedes "49. During the year, the Holding Company
  received a whistle blower complaint..." (line 20373).
- Note 53 (consolidated CERC market-coupling note): file marker **p.291**, not p.290.
  Same page as Note 49, confirmed in the same read (line 20399).
- Note 52 (standalone MSMED Act disclosure): file marker **p.230**, not p.226 as
  previously cited (and as the task brief itself states). Confirmed: page marker
  "=== PAGE 230 ===" (line 15997) precedes "52. Dues of Micro and Small enterprises"
  (line 16004); the printed footer on that physical page reads "226," which is the
  number earlier passes picked up instead of the file marker.
- Note 22 (consolidated Trade Payables classification): file marker **p.271**,
  refined from the earlier "~p.268 area" hedge. Confirmed: page marker "=== PAGE
  271 ===" (line 19124) precedes "22. Trade Payables" (line 19135).
All other anchors carried from Pass 1/Pass 2 were spot-checked against page markers
opened directly in this pass (Note 39/38 contingent liabilities p.217/p.279; Note
46/47 standalone whistleblower/CERC p.224; Note 28/29 revenue and other income
p.211; Note 11 trade receivables p.202-203; Board's Report whistleblower p.80) and
confirmed correct. No figure in any note changes; only four citations move.

## PATTERN PASS: DIRECTED CONTRADICTIONS

### 1. Whistleblower status: Board's Report vs Notes 46/49 — sharpened, not resolved

Both approved by the same Board on the same date, 23-Apr-2026:
- Board's Report, "Whistle Blower & Anti-Fraud Policy" (Annual Report FY26, p.80,
  verified this pass): "During the year under review, the Company received a
  complaint under the said mechanism, which was reviewed by the Audit Committee
  and subjected to an independent investigation in accordance with the established
  procedures. Based on the findings of the investigation, appropriate actions were
  implemented as directed by the Audit Committee." Past tense throughout.
- Note 46 standalone (p.224, verified this pass) / Note 49 consolidated (p.291,
  corrected this pass from p.290): "The Audit Committee has initiated an
  independent investigation, which remains ongoing as at the date of approval of
  the [standalone/Consolidated] financial statements by the Board... which do not
  have a material impact." Present-progressive, unresolved.

Pass 2 found the corroborating evidence: CARO Annexure I clause xi (standalone
p.176-177) uses the identical "ongoing... as on the date of our audit report"
framing, and the consolidated auditor's report confirms no adverse CARO remarks
anywhere in the group. Three independent documents (the Notes, CARO, and by
extension the auditor's own procedures) agree the investigation was still open at
sign-off, against one document (the Board's Report) that reads as concluded. The
weight of evidence favours the Notes/auditor framing. The most likely explanation,
unresolved by the AR itself, is that the Board's Report prose describes an earlier
procedural step (the Audit Committee's initial review that triggered the
investigation, or a different, already-closed vigil-mechanism matter) in language
loose enough to read as a conclusion of the still-open one. Judgement this pass:
CONTRADICTION SHARPENED, NOT RESOLVED — the Notes/CARO framing carries the greater
weight of evidence; the Board's Report is the outlier document.

### 2. MSME dues: Note 23 vs Note 52 — sharpened, not resolved

Note 23, standalone trade payables classification (p.209, verified this pass):
total outstanding dues to micro/small enterprises = ₹38.03L FY26 vs ₹6.76L FY25
(+462%), inside a full ageing schedule with a ₹335.03L unclassified "Accruals"
plug that carries no MSME/non-MSME split. Note 52, the dedicated MSMED Act, 2006
disclosure (p.230, corrected this pass from p.226): "Dues remaining unpaid to any
supplier — Principal" = ₹44.41L FY26 vs ₹76.90L FY25 (-42%). Same balance sheet
date, same nominal subject (MSME supplier dues outstanding at year end), opposite
YoY direction, and neither note cross-references the other. The pattern repeats in
consolidated: Note 22 (p.271, refined from "~p.268 area") shows ₹38.03L FY26 vs
₹7.47L FY25 (rising) against Note 48 (p.290) showing ₹44.41L FY26 vs ₹77.61L FY25
(falling). Both note-pairs agree on one point: zero interest accrued or paid under
the MSMED Act, either note, either year, either statement — so this is not a
disclosed compliance failure, it is an unreconciled pair of sub-schedules that most
plausibly draw from two different source systems (a trade-payables ageing/vendor-
master query for Note 23/22 versus a supplier-master MSME-flag query for Note
52/48). The AR states neither mechanism nor a reconciliation; this remains
inference. Immaterial in rupee terms against ₹1,364.56cr consolidated net worth.
Judgement this pass: CONTRADICTION SHARPENED, NOT RESOLVED — a genuine, unexplained
internal inconsistency between two notes that should tie out and do not.

### 3. Read across the disclosure set: pattern, not three unrelated slips

Three internal numeric/status inconsistencies stand inside one FY26 annual report,
all board-approved 23-Apr-2026:
- RTM FY26 volume share: 34% at p.17, p.25, p.62 vs "nearly 40%"/"approximately
  39%" at p.33, p.36-37 (Stage 1 Gate 0 finding, cross-stage evidence; the revenue
  note, Note 28 p.211, cannot arbitrate because Electricity revenue is reported as
  one combined DAM+RTM+TAM+Green line, not split by product).
- Whistleblower status: concluded (Board's Report, p.80) vs ongoing (Notes 46/49,
  p.224/p.291).
- MSME dues: rising (Note 23/22, p.209/p.271) vs falling (Note 52/48, p.230/p.290).

Adjacent in character though not a strict numeric contradiction: Note 47 (p.224)
narrates the CERC market-coupling order, the APTEL ruling and the Supreme Court
civil appeal in full prose, but carries no rupee amount, no probability assessment,
and is not classified as a contingent liability — unlike Note 39 (p.217), which
gives the far smaller ₹5.04cr GST dispute a complete management assessment ("not
tenable... no amount will be payable"). The largest structural risk in the filing
is the least quantified line in the financial statements.

Judgement, anchored: this reads as a disclosure-quality pattern, not three
unrelated drafting slips. Each note, read alone, is detailed and internally
consistent — the RTM percentages are each individually sourced to named data
providers in their own MD&A sections; Note 23/22's ageing schedule is complete;
Note 52/48 follows the MSMED Act statutory template exactly; Note 47 narrates the
litigation timeline accurately as far as it goes. The common thread is that THE
SAME underlying fact gets a different number or characterisation depending on
WHICH section of the report supplies it — MD&A narrative vs formal Notes, Board's
Report vs Notes, one Notes sub-schedule vs another Notes sub-schedule. That pattern
is consistent with sections being drafted by different functions (investor
relations/MD&A, company secretarial, financial controllership, legal) without a
final cross-document reconciliation pass before sign-off, rather than with any
single author being careless within their own section. It is a process observation
about how the AR is assembled, not a finding about the underlying business or its
cash economics, and none of the four items move any audited total or the unqualified
audit opinion.

## EARNINGS QUALITY, TRACED ACROSS ALL THREE PASSES

Operating revenue vs treasury and IGX equity pickup (Note 28/29 standalone p.211;
consolidated equivalents Note 27/28 p.273; Note 54 p.291; P&L p.188/p.238; all
figures taken directly from Pass 1's extraction, cross-checked against the primary
source at p.211 this pass):
- Standalone: revenue from operations ₹608.39cr, other income ₹136.55cr, PBT
  ₹624.81cr, PAT ₹473.71cr, basic/diluted EPS ₹5.33.
- Consolidated: PBT ₹645.56cr (matches the spear-gate load-bearing fact in
  companies/IEX.md and B00-inputs.yaml exactly), profit attributable to equity
  shareholders ₹492.92cr, basic/diluted EPS ₹5.54.
- The screener's ₹151.10cr "other income" figure resolves EXACTLY to the sum of
  two distinct P&L lines the consolidated accounts keep separate: Consolidated
  Other Income ₹131.30cr (Note 28 consol, p.273 — treasury/investment income only:
  interest ₹5.09cr bank + ₹57.51cr amortised-cost investments, gains on sale
  ₹8.09cr + ₹23.31cr, FV gain ₹34.15cr, dividend ₹0.05cr, business support ₹0.31cr,
  misc ₹2.56cr) plus "Share in profit of associate (net of tax)" ₹19.80cr (Note 54,
  p.291 — the 47.28% IGX equity-method pickup, disclosed on its own line below
  "Profit before share of profit of associates and tax," not inside Other Income).
  ₹131.30cr + ₹19.80cr = ₹151.10cr to the rupee. Together these are 23.4% of
  consolidated PBT — non-operating, none of it contractually assured. This is the
  single most load-bearing reconciliation this stage produces: it directly answers
  the spear-gate load-bearing fact "operating vs treasury earnings" named in
  companies/IEX.md and B00-inputs.yaml, with exact anchors on both sides.
- Standalone Other Income (₹136.55cr) is ₹5.25cr higher than consolidated almost
  entirely because standalone recognises ₹5.37cr dividend income from IGX directly
  (IGX carried at cost, ₹35.46cr, standalone Note 6 p.193/198), which consolidation
  correctly eliminates and instead nets against the equity-method carrying value —
  clean, correct equity-method accounting, no double-count.
- IGX consolidated carrying value: opening ₹75.75cr + share of PAT ₹19.80cr −
  distribution received ₹5.32cr + share of OCI ₹0.03cr = closing ₹90.25cr at
  31-Mar-2026 (Note 54, p.291), up 19.2% YoY purely from retained equity pickup.
  The PNGRB-mandated OFS/dilution to 25% — a spear-gate load-bearing fact — is
  disclosed NOWHERE in either note set (no dedicated subsequent-events note exists
  in this AR at all); the only trace of an IGX-level control gap anywhere in the
  filing is the consolidated auditor's Rule 11(g) audit-trail exception on IGX's
  third-party accounting software (Consolidated Auditor's Report, p.234-236,
  outside the Notes, found by Pass 2).

Settlement float's effect on CFO: the cash flow statement (standalone p.183,
consolidated p.244) backs treasury-related non-cash items (fair value gains, gains
on sale, EIR-accrued interest income) out of operating cash flow and shows actual
cash received from investments under investing activities, not operating — standard
treatment, not aggressive revenue recognition. Separately, the "Increase in trade
payables, other financial liabilities, provisions and other liabilities" cash flow
line swung from ₹256.2cr (FY25) to ₹12.0cr (FY26), a ~₹244cr YoY swing driven by
settlement/margin balance timing (Note 41, "Other financial liabilities — Others,
Current" ₹951.27cr FY26 vs ₹946.07cr FY25, larger than the company's entire net
worth, member money not IEX capital, no P&L exposure). Confirms the mechanism that
can take CFO far above or below PAT on float timing alone, independent of earnings
quality; FY23's negative CFO cited in company memory cannot be verified or
explained from this document (FY23 sits outside this AR's two-year comparative
window) — NOT FOUND for FY23 specifically, plausible on the same mechanism but not
an anchored finding.

Does reported PAT convert to cash: standalone net CFO ₹424.64cr against standalone
PAT ₹473.71cr is 89.6% conversion (consolidated: CFO ₹432.77cr vs PAT ₹492.92cr =
87.8%). Trade receivables are trivial (₹1.22cr, Note 11, p.202) and fully current,
so working-capital drag is not a factor; the conversion gap is explained almost
entirely by the operating/investing classification split on treasury income, not by
deterioration in collections or accrual quality. Verdict: the core transaction-fee
business converts cleanly to cash; the treasury sleeve (roughly a fifth of total
income) is real cash income too, one line removed from CFO by standard Ind AS 7
classification, not by any aggressive accounting choice.

## WHAT AN INVESTOR CANNOT LEARN FROM THESE NOTES

- No rupee split within the "Electricity" revenue bundle (Note 28, p.211): DAM,
  RTM, TAM and Green segment transaction-fee revenue are one combined line,
  ₹558.51cr FY26 (up 16.8% YoY, against Certificates ₹25.45cr, down 27.7% YoY — a
  real mix shift the headline P&L does not show). The volume-share percentages
  quoted narratively elsewhere in the AR (which themselves conflict, see above)
  cannot be checked against revenue mix because no revenue-basis segment split
  exists below the two-way Electricity/Certificates cut.
- No quantified financial-impact estimate for the CERC market-coupling litigation
  (Note 47, p.224), despite it being the single largest structural regulatory risk
  to the DAM franchise. No probability language, no amount, no contingent
  liability entry, and no coverage of events after the 17-Apr-2026 draft
  regulations (the APTEL judgment date and the two later Supreme Court orders
  named in the manifest's freshness-pair check are entirely absent from the Notes).
- No identity or nature disclosed for the single customer contributing 16.2% of
  FY26 revenue from operations (₹98.62cr, Note 28, p.211, up from 15.65%/₹83.79cr
  FY25) — whether this is a large discom, a scheduled entity, or a member category
  is not stated.
- No explicit bridge reconciling standalone PAT (₹473.71cr) to consolidated profit
  attributable to equity shareholders (₹492.92cr); the exact IGX equity-pickup
  contribution inside that ₹19.21cr gap (net of ICX subsidiary results and minority
  interest) is not separately stated anywhere in the Notes.
- No rationale for the FY26 treasury reallocation out of target-maturity/fixed-
  maturity plans and market-linked debentures (cut 96.7% and fully exited
  respectively) into arbitrage/liquid funds and equity-index funds (up 280%) —
  Note 41 (p.214-215) shows the movement, not the reason.
- No disclosure anywhere in the Notes of the IGX OFS / dilution to the PNGRB 25%
  ownership ceiling — a spear-gate load-bearing fact with zero financial-statement
  footprint; only the auditor's Rule 11(g) exception (outside the Notes) hints at
  an IGX-level visibility gap.
- No management acknowledgement, anywhere, that Note 23/22 and Note 52/48
  disagree on MSME dues, or that the Board's Report and Notes 46/49 disagree on
  the whistleblower investigation's status.

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Whistleblower investigation status conflict: Board's Report (p.80) says concluded with findings and remedial action; Notes 46/49 (p.224/p.291) say still ongoing; both signed 23-Apr-2026. CARO corroborates the Notes' framing, making the Board's Report the outlier document. | Note 46/49 | RED FLAG | Governs whether "no material impact" was reached before or after the investigation's substantive findings were known. |
| 2 | Market-coupling regulatory exposure (Note 47) carries zero financial quantification or contingent-liability classification, while the far smaller ₹5.04cr GST dispute (Note 39) receives a full management assessment. | Note 47 vs Note 39 | RED FLAG | The single largest structural risk to the DAM franchise is the least-quantified item in the financial statements. |
| 3 | MSME dues contradiction: Note 23/22 shows dues rising 462% to ₹38.03L; Note 52/48 shows dues falling 42% to ₹44.41L, same balance sheet date, unreconciled, in both standalone and consolidated. | Note 23 (p.209) / Note 52 (p.230); consol Note 22 (p.271) / Note 48 (p.290) | RED FLAG | Genuine internal-consistency gap between two notes serving the same disclosure purpose; immaterial in rupees but a disclosure-control weakness. |
| 4 | RTM FY26 volume share stated inconsistently across the AR: 34% (p.17/25/62) vs approximately 39-40% (p.33/36-37); Note 28's revenue split cannot arbitrate because Electricity revenue is one combined line. | MD&A, cross-checked against Note 28 (p.211) | RED FLAG | Third internal inconsistency in the same annual report; blocks verification of the market-coupling exposure's actual revenue base. |
| 5 | Other income (₹131.30cr) plus IGX equity pickup (₹19.80cr) = ₹151.10cr of ₹645.56cr consolidated PBT (23.4%) is non-operating treasury/associate income; reconciles exactly to the screener's ₹151.10cr "other income" figure. | Note 28 consol (p.273) / Note 54 (p.291) / P&L (p.238) | LOAD-BEARING (CLEAN accounting, WATCH for valuation) | Directly resolves the spear-gate "operating vs treasury earnings" load-bearing fact with an exact rupee bridge; caps how much of PBT should carry an operating multiple. |
| 6 | IGX carrying value ₹90.25cr (equity method, 47.28% stake, up 19.2% YoY on retained pickup alone); the PNGRB-mandated OFS/dilution to 25% is disclosed nowhere in the financial statement notes. | Note 54, p.291 | WATCH | Material forward-looking event, a spear-gate load-bearing fact, with zero financial-statement footprint; must be sourced elsewhere. |
| 7 | Settlement/margin float swung the cash flow statement by ~₹244cr YoY (₹256.2cr inflow FY25 vs ₹12.0cr FY26 on "increase in other financial liabilities"), driven by member balances of ₹951.27cr, larger than net worth, that are not IEX's capital. | Cash Flow Statement p.183/p.244; Note 41, p.219 | WATCH (mechanism, not earnings quality) | Explains float-driven CFO volatility independent of earnings quality; must not be read as a working-capital red flag. |
| 8 | Revenue disaggregation exists but is coarser than assumed: two-way Electricity vs Certificates split only; Certificates revenue fell 27.7% YoY while Electricity grew 16.8%, a mix shift the headline P&L does not show. | Note 28, p.211 | WATCH | Corrects the assumption of "no split anywhere"; a real product-mix signal with no DAM/RTM/TAM/Green breakout underneath it. |
| 9 | Single customer contributes 16.2% of FY26 revenue from operations (₹98.62cr), up from 15.65% (₹83.79cr) FY25; identity not disclosed. | Note 28, p.211 | WATCH | Real concentration risk in a nominally atomised multilateral exchange model; durability and identity unknown. |
| 10 | Trade receivables trivial and clean: ₹1.22cr FY26 (down from ₹2.01cr), 100% under 6 months, zero disputed, credit-impaired, not-due, or unbilled. | Note 11, p.202-203 | CLEAN | Confirms the pre-funded settlement model carries near-zero credit risk on members. |
| 11 | ESOP charge nearly halved YoY (₹80.59L vs ₹164.65L, -51%) despite a fresh 1,00,000-option grant on 29-Jul-2025; total options outstanding fell to 8,93,760 from 9,98,175 as forfeitures and exercises outpaced the new grant. | Note 51, p.224-225 | WATCH | Plausible mechanical explanation (largest historical tranche nearing end of vesting) but not stated by the company. |
| 12 | Investment fair-value hierarchy shows sharp within-year reallocation: Level-1 target-maturity/fixed-maturity plans cut 96.7%, market-linked debentures fully exited, equity-index mutual fund exposure up 280%; no stated rationale. | Note 41, p.214-215 | WATCH | Genuine, unexplained change in treasury risk posture on a ₹1,900+cr book. |
| 13 | Contingent liabilities: single GST dispute, ₹5.0376cr total (tax ₹260.71L + interest ₹216.97L + penalty ₹26.08L), 0.37% of net worth, management assesses not tenable; no guarantees for subsidiaries. | Note 39, p.217 | CLEAN | Small, well-characterised, fully assessed; the contrast case for finding 2. |
| 14 | Standalone net CFO ₹424.64cr vs PAT ₹473.71cr, 89.6% conversion; the gap is explained by treasury income sitting under investing rather than operating cash flow (standard Ind AS 7 classification), not by working-capital drag or accrual quality. | Cash Flow Statement, p.183-184 | CLEAN | Core transaction-fee business converts cleanly to cash; treasury income is real cash, one line removed from CFO. |
| 15 | Consolidated auditor's report carries a Rule 11(g) audit-trail exception specific to IGX's third-party accounting software (no visibility on database-level edit logs); standalone audit trail is fully clean; not disclosed in the Notes themselves. | Consolidated Auditor's Report p.234-236, outside the Notes | WATCH | Layers on top of the Notes' complete silence on IGX's OFS/dilution, a spear-gate load-bearing fact. |

### B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 8 | Point-in-time recognition under Ind AS 115, KAM-level external cross-check to GST returns and NLDC/RLDC/CERC traded volumes, zero unbilled receivables, contracted-price-to-recognised-revenue reconciliation disclosed (₹624.41cr contracted less ₹16.03cr incentives/discounts = ₹608.39cr recognised, standalone). |
| Expense capitalisation honesty | 8 | Useful lives disclosed and stable, no aggressive capitalisation observed, ESOP fully and transparently expensed. |
| Provisioning adequacy | 7 | The one item classified as a contingent liability (GST, ₹5.04cr) is fully assessed; the far larger market-coupling exposure receives no provisioning treatment or quantification at all (Note 47), which caps this dimension below where the GST-only evidence would otherwise put it. |
| RPT fairness | 7 | Transactions small, CARO confirms s.177/188 compliance, promoter holding is Nil so no promoter-extraction channel exists; no explicit arm's-length pricing commentary in the Notes beyond boilerplate assertion. |
| Disclosure transparency | 4 | Three same-report internal contradictions (whistleblower status, MSME dues, RTM volume share) plus one major unquantified risk sitting beside a fully quantified trivial one; this is the dimension the pattern pass exists to catch, and it is the weakest one in this filing. |
| Consistency with prior years | 8 | Accounting policies unchanged, no restatements or reclassifications found, YoY ratio variances explained in the analytical ratios note. |
| **OVERALL** | **6/10** | Moderate. Every reported number checks out and reconciles internally (including the exact ₹151.10cr other-income + IGX-pickup bridge); what does not reconcile is which of two or three competing narratives about status or materiality to believe. Unqualified audit opinion both statements, fraud-focused KAM found nothing, no going-concern language. |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Market-coupling regulatory restructuring of DAM, unquantified in the Notes | HIGH | CERC's draft (Power Market) (Second Amendment) Regulations, 2026 (issued 17-Apr-2026, Note 47); Supreme Court civil appeal outcome | On regulation finalisation or Supreme Court ruling; timing outside company's control |
| Single-customer revenue concentration, 16.2% and rising | MEDIUM | Whether the concentration customer's share keeps rising in FY27 quarterly disclosures | Gradual; visible in quarterly revenue mix if reported |
| Disclosure-reconciliation discipline across AR sections | MEDIUM | Whether the FY27 AR reconciles the MSME notes and resolves the whistleblower/Board's Report language gap | Next annual report cycle |
| IGX associate-level audit-trail visibility gap, layered on the IGX OFS silence | LOW-MEDIUM | Whether the Rule 11(g) exception clears in FY27's consolidated audit report | Next annual audit cycle |
| Treasury book reallocation toward equity-linked exposure, unexplained | LOW | Whether the shift continues and whether price-risk sensitivity (currently trivial, ₹3.80L per 5% move) grows materially | Ongoing, visible each year in Note 41 |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. Which is accurate as of the 23-Apr-2026 Board approval: the Board's Report's
   characterisation of the whistleblower investigation as concluded with findings
   and remedial action taken (p.80), or the Notes' characterisation of it as still
   open (Note 46/49)? What were the findings and what remedial action was taken?
2. What accounts for the divergence between Note 23/22's trade-payables MSME
   classification (₹38.03L, up 462%) and Note 52/48's MSMED Act disclosure
   (₹44.41L, down 42%) for the same balance sheet date, and will FY27 reconcile
   the two?
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

- Whistleblower investigation status conflict between the Board's Report (p.80,
  concluded) and Notes 46/49 (p.224/p.291, still ongoing), both signed 23-Apr-2026.
- MSME dues contradiction between Note 23/22 (p.209/p.271, rising) and Note 52/48
  (p.230/p.290, falling), same balance sheet dates, unreconciled.
- RTM FY26 volume share stated inconsistently across the annual report (34% vs
  approximately 39-40%), no revenue-basis split available to arbitrate.
- Market-coupling regulatory exposure (Note 47, p.224), the company's largest
  structural risk, carries zero financial quantification or contingent-liability
  treatment, unlike the much smaller GST matter (Note 39).
No evidence of earnings management or aggressive accounting was found on any
audited total; all four items above are disclosure-consistency and disclosure-
completeness defects, not numeric manipulation of the accounts.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices: clean and internally consistent
within each individual note, but inconsistent across the wider annual report on
three separate matters signed off the same day. Key concern: the whistleblower
status conflict between the Board's Report and Notes 46/49, compounded by an
unquantified market-coupling exposure and an unreconciled MSME dues pair. Key
strength: near-zero receivables risk, an unqualified audit opinion on both
statements, a fraud-focused Key Audit Matter that found nothing, and an exact
rupee-for-rupee reconciliation of the treasury/IGX-pickup share of PBT. Overall
accounting quality: 6/10.

```yaml
stage: B02-notes
company: "IEX"
run_date: "2026-09-08"
model: claude-sonnet-5
status: complete
input_gaps:
  - type: rating
    severity: NOT_A_GAP
    detail: >
      inputs/rating/ empty. IEX has no listed debt (confirmed by Note 42/43,
      "does not have any debt outstanding," and IEX told BSE it does not qualify
      as a Large Corporate). Unrateable by absence of rated debt, not by missed
      collection.
  - type: research
    severity: LOW
    detail: "inputs/research/ empty. Broker notes are non-anchored, leads only."
  - type: regulatory_order_text
    severity: HIGH
    detail: >
      The CERC market-coupling order, the APTEL judgment, and the two Supreme
      Court orders are referenced in the corpus (and in Note 47, p.224) but their
      full texts are absent. Note 47 itself gives no financial quantification of
      this exposure, sharpening the need for the order texts.
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
  - {rank: 1, finding: "Whistleblower investigation status conflict: Board's Report (p.80) says concluded with findings and remedial action; Notes 46/49 (p.224/p.291) say still ongoing; both signed 23-Apr-2026. CARO corroborates the Notes' framing, making the Board's Report the outlier document.", note_ref: "Note 46 (standalone p.224) / Note 49 (consolidated p.291)", rating: "RED FLAG", why: "Governs whether 'no material impact' was reached before or after the investigation's substantive findings were known."}
  - {rank: 2, finding: "Market-coupling regulatory exposure (Note 47) carries zero financial quantification or contingent-liability classification, while the far smaller Rs5.04cr GST dispute (Note 39) receives a full management assessment.", note_ref: "Note 47 vs Note 39, p.224 vs p.217", rating: "RED FLAG", why: "The single largest structural risk to the DAM franchise is the least-quantified item in the financial statements."}
  - {rank: 3, finding: "MSME dues contradiction: Note 23/22 shows dues rising 462% to Rs38.03L; Note 52/48 shows dues falling 42% to Rs44.41L for the same balance sheet date; unreconciled; repeats in consolidated.", note_ref: "Note 23 (p.209) / Note 52 (p.230); consol Note 22 (p.271) / Note 48 (p.290)", rating: "RED FLAG", why: "Genuine internal-consistency gap between two notes serving the same disclosure purpose; immaterial in rupees but a disclosure-control weakness."}
  - {rank: 4, finding: "RTM FY26 volume share stated inconsistently across the AR: 34% (p.17/25/62) vs approximately 39-40% (p.33/36-37); no revenue-basis segment split exists to arbitrate.", note_ref: "MD&A, cross-checked against Note 28 (p.211)", rating: "RED FLAG", why: "Third internal inconsistency in the same annual report; blocks verification of the market-coupling exposure's actual revenue base."}
  - {rank: 5, finding: "Other income Rs131.30cr plus IGX equity pickup Rs19.80cr equals Rs151.10cr of Rs645.56cr consolidated PBT (23.4%) non-operating; reconciles exactly to the screener's Rs151.10cr 'other income' figure, resolving the spear-gate load-bearing fact with an exact rupee bridge.", note_ref: "Note 28 consol (p.273) / Note 54 (p.291) / P&L (p.238)", rating: "LOAD-BEARING", why: "Caps how much of PBT should carry an operating multiple; directly answers the spear-gate 'operating vs treasury earnings' fact."}
  - {rank: 6, finding: "IGX carrying value Rs90.25cr (equity method, 47.28% stake, up 19.2% YoY on retained pickup alone); the PNGRB-mandated OFS/dilution to 25% is disclosed nowhere in the financial statement notes.", note_ref: "Note 54, p.291", rating: "WATCH", why: "Material forward-looking event, a spear-gate load-bearing fact, with zero financial-statement footprint."}
  - {rank: 7, finding: "Settlement/margin float swung the cash flow statement by approximately Rs244cr YoY (Rs256.2cr inflow FY25 vs Rs12.0cr FY26), driven by member balances of Rs951.27cr, larger than net worth, that are not IEX's own capital.", note_ref: "Cash Flow Statement p.183/p.244; Note 41, p.219", rating: "WATCH", why: "Explains float-driven CFO volatility independent of earnings quality; must not be read as a working-capital red flag."}
  - {rank: 8, finding: "Revenue disaggregation exists but is coarser than assumed: two-way Electricity vs Certificates split only; Certificates revenue fell 27.7% YoY while Electricity grew 16.8%, a mix shift the headline P&L does not show.", note_ref: "Note 28, p.211", rating: "WATCH", why: "Corrects the assumption of 'no split anywhere'; a real product-mix signal with no DAM/RTM/TAM/Green breakout underneath it."}
  - {rank: 9, finding: "Single customer contributes 16.2% of FY26 revenue from operations (Rs98.62cr), up from 15.65% (Rs83.79cr) FY25; identity not disclosed.", note_ref: "Note 28, p.211", rating: "WATCH", why: "Real concentration risk in a nominally atomised multilateral exchange model; durability and identity unknown."}
  - {rank: 10, finding: "Trade receivables trivial and clean: Rs1.22cr FY26 (down from Rs2.01cr), 100% under 6 months, zero disputed, credit-impaired, not-due, or unbilled.", note_ref: "Note 11, p.202-203", rating: "CLEAN", why: "Confirms the pre-funded settlement model carries near-zero credit risk on members."}
  - {rank: 11, finding: "ESOP charge nearly halved YoY (Rs80.59L vs Rs164.65L, -51%) despite a fresh 1,00,000-option grant on 29-Jul-2025; total options outstanding fell to 8,93,760 from 9,98,175 as forfeitures and exercises outpaced the new grant.", note_ref: "Note 51, p.224-225", rating: "WATCH", why: "Plausible mechanical explanation (largest historical tranche nearing end of vesting) but not stated by the company."}
  - {rank: 12, finding: "Investment fair-value hierarchy shows sharp within-year reallocation: Level-1 target-maturity/fixed-maturity plans cut 96.7%, market-linked debentures fully exited, equity-index mutual fund exposure up 280%; no stated rationale.", note_ref: "Note 41, p.214-215", rating: "WATCH", why: "Genuine, unexplained change in treasury risk posture on a Rs1,900+cr book."}
  - {rank: 13, finding: "Contingent liabilities: single GST dispute, Rs5.0376cr total (tax Rs260.71L + interest Rs216.97L + penalty Rs26.08L), 0.37% of net worth, management assesses not tenable; no guarantees for subsidiaries.", note_ref: "Note 39, p.217", rating: "CLEAN", why: "Small, well-characterised, fully assessed; the contrast case for finding 2."}
  - {rank: 14, finding: "Standalone net CFO Rs424.64cr vs PAT Rs473.71cr, 89.6% conversion; the gap is explained by treasury income sitting under investing rather than operating cash flow, not by working-capital drag or accrual quality.", note_ref: "Cash Flow Statement, p.183-184", rating: "CLEAN", why: "Core transaction-fee business converts cleanly to cash; treasury income is real cash, one line removed from CFO."}
  - {rank: 15, finding: "Consolidated auditor's report carries a Rule 11(g) audit-trail exception specific to IGX's third-party accounting software (no visibility on database-level edit logs); standalone audit trail is fully clean; not disclosed in the Notes themselves.", note_ref: "Consolidated Auditor's Report p.234-236, outside the Notes", rating: "WATCH", why: "Layers on top of the Notes' complete silence on IGX's OFS/dilution, a spear-gate load-bearing fact."}
red_flags:
  - "Whistleblower investigation status conflict between the Board's Report (p.80, concluded) and Notes 46/49 (p.224/p.291, still ongoing), both signed 23-Apr-2026."
  - "MSME dues contradiction between Note 23/22 (p.209/p.271, rising) and Note 52/48 (p.230/p.290, falling), same balance sheet dates, unreconciled."
  - "RTM FY26 volume share stated inconsistently across the annual report (34% vs approximately 39-40%), no revenue-basis split available to arbitrate."
  - "Market-coupling regulatory exposure (Note 47, p.224), the company's largest structural risk, carries zero financial quantification or contingent-liability treatment, unlike the much smaller GST matter (Note 39)."
questions_for_mgmt:
  - "Which is accurate as of the 23-Apr-2026 Board approval: the Board's Report's 'concluded with findings and remedial action' characterisation of the whistleblower investigation, or the Notes' 'still ongoing' characterisation? What were the findings and what remedial action was taken?"
  - "What accounts for the divergence between Note 23/22 (Rs38.03L, up 462%) and Note 52/48 (Rs44.41L, down 42%) on MSME dues for the same balance sheet date, and will FY27 reconcile the two schedules?"
  - "What is management's probability and financial-impact assessment of the CERC market-coupling litigation (Note 47), and why does it carry no contingent-liability entry while the much smaller GST dispute does?"
  - "Who is the single customer contributing 16.2% of FY26 revenue from operations (Rs98.62cr, up from 15.65%), and what is the durability of that relationship?"
  - "What drove the FY26 treasury reallocation out of target-maturity/fixed-maturity plans and market-linked debentures into arbitrage/liquid and equity-index funds, and does it reflect a deliberate change in risk appetite for the Rs1,900+cr treasury book?"
receivables_trend: "improving: standalone trade receivables Rs1.22cr FY26 vs Rs2.01cr FY25 (Note 11, p.202), entirely in the under-6-months bucket both years, zero disputed/credit-impaired/not-due/unbilled; reflects the pre-funded settlement model, not a working-capital risk indicator for this business."
restatements_found: []
going_concern_language: "NONE beyond standard boilerplate ('accrual and going concern basis,' p.185; capital-management going-concern objective language, p.220/p.285 area); no material uncertainty, no adverse opinion, no emphasis-of-matter paragraph in either the standalone or consolidated auditor's report."
analyst_note: >
  This run redid the consolidation with all three real passes in hand; Pass 1's
  file, missing in Run 1, is now present and its Run-1 reconstruction held up
  against it with no substantive contradiction. This pass's own direct-page
  verification corrected four citations (Note 49 and Note 53 consolidated to
  p.291 from p.290; Note 52 standalone to p.230 from p.226; Note 22 consolidated
  refined to p.271), all citation-only, no figures changed. The single most
  important read-across finding stands: three internal numeric or status
  contradictions (RTM volume share, whistleblower status, MSME dues) sit inside
  one board-approved annual report, all traceable to disagreement BETWEEN
  sections of the AR rather than errors WITHIN any one note. A fourth item, the
  unquantified market-coupling exposure against the fully-quantified trivial GST
  matter, is a materiality-judgement gap of the same character. Separately, this
  pass produced an exact rupee-for-rupee bridge (Rs131.30cr other income + Rs19.80cr
  IGX equity pickup = Rs151.10cr, 23.4% of consolidated PBT) that directly answers
  a spear-gate load-bearing fact and should carry forward unmodified into Stage 11.
  None of this touches audited totals: the audit opinion is unqualified both
  statements, the fraud-focused KAM found nothing, and core operating cash
  conversion is clean at 89.6%. The accounting quality score of 6/10 reflects a
  report that is numerically trustworthy but cross-document-inconsistent on
  qualitative status and materiality calls, a disclosure-discipline flag, not an
  earnings-quality flag.
```
