# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3 (PATTERN PASS + CONSOLIDATION)
Company: Awfis Space Solutions Limited (AWFIS) | Run: awfis-2026-09-19
Source: runs/awfis-2026-09-19/inputs/annual-report/AR-FY26-with-AGM-notice.txt (page-marked text of
AR-FY26-with-AGM-notice.pdf, 176pp incl. 12th AGM notice). Figures in ₹ millions as filed (AR reporting
unit) unless noted; ÷10 gives ₹ Cr. This is the third and final pass: a pattern re-read, then the
consolidated analysis of all three passes, then the B02-notes YAML block.

═══════════════════════════════════════════════════════════════
## PASS 3 — PATTERN RE-READ
═══════════════════════════════════════════════════════════════
Read the standalone and consolidated Notes a third time hunting specifically for contradictions
between notes, numbers that do not match the primary statements, deliberately thin disclosure next
to detailed disclosure elsewhere, unflagged restatements, late-breaking events, and going-concern
language. Two of Pass 1's and Pass 2's largest findings (the Note 33 vs CARO gap; the GST SCN
absence) are themselves exactly this kind of pattern and are carried into the consolidated table
below rather than repeated here. Three additional pattern-level findings emerged that neither Pass 1
nor Pass 2 named explicitly:

**P1. Internal contradiction: "no long-term contracts" (Note 22(a)) vs the lessor maturity table
(Note 38, Part II).** Note 22(a) states the Company "has not entered into long term contracts with
customers." Note 38's own lessor disclosure, four paragraphs away in the same set of standalone
notes, shows undiscounted lease receivables spread out to 4-5 years and a finance-lease book that
grew from 9 to 30 leases during the year (Pass 1 Section 12a; Pass 2 item 5 of the re-verification).
Read together, the Note 22(a) statement is almost certainly addressing the Ind AS 115
practical-expedient carve-out for contracts of one year or less, not describing the underlying
client lease commitments, which the Company's own Note 38 shows running several years. Taken at
face value without that context, the two notes contradict each other. 🟡 Worth a direct management
question; Pass 1 flagged this as "worth a management question" in Section 11 but did not name it as
a contradiction pattern — doing so here.

**P2. Going-concern "net current liability" language sits beside a negative net-debt (net cash)
position.** Note 2 (Basis of Preparation, both standalone and consolidated) cites a growing net
current liability position (standalone Rs3,388.14mn FY26, +58.3% YoY) as the reason management
addresses going concern explicitly, citing plans to raise funds and optimise working capital. Note
34 (Note 41 ratios), in the same set of notes, shows the Company is net-cash: borrowings Rs509.03mn
against cash and bank balances that leave net debt at Rs(381.63)mn standalone / Rs(386.84)mn
consolidated — i.e. negative net debt both years. The tension resolves on inspection (the current
portion of Ind AS 116 lease liabilities, Rs3,950.44mn FY26, is what drives the net current liability
figure, not a shortage of cash or a debt problem), but a reader who sees "net current liability
position, management is planning to raise funds" without also reading Note 34 could reasonably
conclude the Company is cash-short, which it is not on the numbers disclosed. 🟡 A genuine
presentation-juxtaposition point, not a numbers error.

**P3. Statutory tax rate assumption changed between years with no election statement.** Note 39's
reconciliation uses a 25.17% statutory rate for FY26 against 29.12% for FY25 (Pass 1 Section 10) —
consistent with a Section 115BAA concessional-regime election, but the Notes never state when or
whether the Company formally elected into Section 115BAA. This is visible only by comparing the two
years' "at statutory rate" reconciliation lines side by side, which is exactly the kind of pattern
this pass is built to catch. Immaterial in cash terms (actual tax is Nil either year, Pass 1 Section
10) but a genuine disclosure-completeness gap, carried forward from Pass 1's input_gaps.

No further material new findings emerged from the pattern re-read beyond P1-P3 above; the
contradiction-and-cross-check method otherwise reconfirmed rather than added to Pass 1 and Pass 2's
work (consistent with Pass 2's own re-verification of five named findings, all of which held exact).

═══════════════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS, RANKED BY INVESTOR IMPORTANCE

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Note 33 (contingent liabilities) discloses zero quantified amounts in both standalone and consolidated FS, while the standalone auditor's CARO Annexure discloses ~Rs1,101.50mn (~₹110.15 Cr) of disputed statutory dues under appeal (Income Tax Rs1,083.38mn incl. Rs757.93mn at Delhi HC = 13.9% of net worth; GST Rs18.12mn) | Note 33, standalone p.112-113 / consol. p.155-156; CARO Annexure p.86 | 🔴 RED | The statutory Ind AS 37 note designed to carry exactly this information carries nothing; the only quantum in the entire AR sits in a different statutory report |
| 2 | Two GST Show Cause Notices (~Rs6.53 Cr FY23-24, ~Rs7.10 Cr FY22-23) are entirely absent from the Notes to Financial Statements; the first predates the 25-May-2026 board approval of the FY26 accounts and no subsequent-events note exists | Cross-checked against announcements 20260521-*, 20260602-*, 20260604-*; NOT FOUND in Note 33 or elsewhere | 🔴 RED | A known, dated, quantified tax demand that existed before the accounts were approved is missing from the notes specifically meant to capture it |
| 3 | Lease cash outflow (principal+interest) grew 67.4% YoY (Rs2,462.21mn to Rs4,121.64mn) while continuing-ops revenue grew 32.9%; principal repayment alone grew 114.2% | Note 38, p.120-121 | 🟡 | The single most direct notes-based number bearing on LBF1 (cash-EBITDA bridge); lease cash commitment growing materially faster than revenue |
| 4 | Managed Aggregation (MA) revenue-share accounting is NOT FOUND anywhere in the Notes; no numeric weighted-average incremental borrowing rate (IBR) is disclosed for lease liabilities either | Note 4A/4M policy text p.93-94, 96-97; Note 38, p.120-121 | 🟡 | Direct gap against LBF2; a reader cannot see from the Notes how MA is accounted for differently (if at all) from owned/leased centres, or what discount rate underlies the Rs14,502.69mn lease liability |
| 5 | Design & Build business transfer to Awfis Transform Pvt Ltd (100% subsidiary): slump sale Rs265.91mn, timeline extended to 31-Dec-2026 pending a revised valuation; the transferring segment's revenue fell 7.8% and PBT fell 31.9% YoY in the same year of the carve-out | Note 40, p.122-123 | 🟡 | Directly answers LBF3; the asset being transferred is shrinking, and the stated consideration is not final |
| 6 | Lessor-side finance lease reclassification: number of finance leases grew from 9 to 30 YoY; net investment in finance lease +76.1% (Rs2,035.33mn to Rs3,583.51mn); finance lease income +302.8% (Rs70.13mn to Rs282.51mn) | Note 38 Part II (lessor), p.121 | 🟡 | A real, quantified shift toward front-loaded interest-method income and away from straight-line rental; changes revenue quality and balance-sheet composition |
| 7 | Effective tax rate is 0% both years; mechanism is a large DTL (ROU/PPE Rs2,616.93mn + finance lease receivables Rs901.90mn, new this year) exactly netting a large DTA (lease liabilities Rs3,650.04mn + carryforwards), with management choosing not to recognise DTA in excess of DTL | Note 39, p.121-122 | 🟡 | Explains the "unusually low effective tax rate"; a structural, if anything conservative, feature of the lease book — ~Rs150-250mn of unrecognised carryforward benefit is a future non-cash-credit watch item |
| 8 | Total diluted EPS is flat YoY (Rs9.34 both years); basic EPS fell 0.6%, despite standalone continuing-ops revenue +32.9%, because FY25 PAT included a lapsed one-off Rs251.02mn exceptional gain and FY26 discontinued-ops profit fell 31.9%. Continuing-operations-only PAT actually grew 20.5% | Note 31, p.110-111 | 🟡 | A required priority-topic item Pass 1 skipped entirely; the flat headline is an optics artefact, not underlying deterioration, and a downstream stage using headline PAT/EPS would miss real 20.5% continuing-ops growth |
| 9 | Second GST SCN (dated 23-May, received 25-May-2026) was disclosed to exchanges only on 2-Jun-2026, an 8-day gap requiring a formal SEBI LODR "reason for delay" filing on 4-Jun-2026 citing a "material calculation error" under review | Cross-checked against announcements 20260602-*, 20260604-*; not in the AR Notes | 🟡 | A distinct compliance-timing point beyond the "absent from Notes" flag; the notice was received the same day the FY26 accounts were board-approved |
| 10 | Statutory auditor states it is unable to comment on whether the database-level audit-trail (edit-log) feature was enabled and operated throughout the year for the Company's core third-party-hosted accounting software, because the SOC Type 2 report did not address database-level logs | Note 45, p.124-125; Auditor's Report Rule 11(g), p.85-86 | 🟡 | A named, auditor-acknowledged scope gap on a mandatory Companies Act control; common industry-wide for third-party SaaS platforms, but Pass 1 did not surface it |
| 11 | Top-10 customer receivable concentration rose from 42.74% (FY25) to 61.66% (FY26) of total trade receivables outstanding | Note 36(b)(II), p.116 | 🟡 | Directly qualifies the "broadly stable to modestly improving" receivables ageing read; the ageing mix improved while customer concentration worsened materially in the same year |
| 12 | The ECL loss-rate-by-ageing-bucket matrix exists (Note 36, not Note 8 as Pass 1 first looked — corrected below) and swings non-monotonically YoY, including a new 17.32% rate on the previously zero-risk unbilled/current-not-due bucket (0.00% FY25) | Note 36(b)(II), p.116 | 🟡 | Corrects a Pass 1 "NOT FOUND"; the volatility pattern reads more like case-by-case specific provisioning than a stable statistical loss model |
| 13 | "Infra and allied service expenses" grew Rs110.48mn to Rs483.26mn (+337.4% YoY) with no narrative explanation anywhere in the Notes; total Other Expenses grew 40.8% YoY, outpacing continuing-ops revenue growth of 32.9% | Note 29, p.109-110 | 🟡 | A second, independent margin-quality data point beyond the lease-cost story; the single largest driver is disclosed as a number with zero explanation |
| 14 | New/enlarged doubtful-debt provisions inside Note 29 (Provision for doubtful debts Rs27.05mn FY26, first occurrence; doubtful advances/deposits Rs41.42mn vs Rs0.63mn) do not cleanly reconcile to Note 36's ECL roll-forward figure of Rs57.44mn "provision made" for the same receivables pool | Note 29, p.109-110, cross-checked against Note 36, p.117 | 🟡 | Two different bad-debt-related numbers for what may be overlapping pools, not bridged anywhere in the Notes |
| 15 | Internal contradiction: Note 22(a) states the Company "has not entered into long term contracts with customers," while Note 38's own lessor maturity table shows client lease receivables running 4-5 years and a finance-lease book that grew from 9 to 30 leases in the year | Note 22(a), p.108; Note 38 Part II, p.121 | 🟡 | Pattern-pass finding (P1); almost certainly an Ind AS 115 practical-expedient statement rather than a description of underlying lease terms, but reads as contradictory at face value |

*(Additional items not in the top 15 but worth carrying forward: MSME principal due +55.9% YoY with
MSMED Act interest payable for the first time, Note 20(b); ESOP charge +141.3% YoY with ~75%
concentrated in one KMP grant, Notes 26/37/32; recurring two-year customer default and NCLT
(Hyderabad) recovery, lease receivables derecognised Rs113.08mn FY26, Note 46B; going-concern
net-current-liability language sitting beside a negative net-debt position, pattern P2; RPT overall
clean but the Awliv trade payable grew 244% YoY on a small base, Note 32; consolidated Note 1
"Group overview" text drafted as if there were one subsidiary when two are consolidated, a QC point
not a scope error; digit-drop OCR artefacts in the consolidated segment note (Note 31) — a corpus
text-extraction defect, not a company error, named so no downstream stage cites the garbled
Rs2,075.35mn / Rs5,069.84mn figures as real.)*

## B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 7 | Loss-making construction projects recognised immediately; revenue capped at cost when outcome not reliably measurable (Note 4A). Offset by the lessor-side shift toward front-loaded finance-lease income (9→30 leases, +302.8% finance lease income, Note 38) and the Note 22(a)/Note 38 contradiction (finding 15) |
| Expense capitalisation honesty | 6.5 | ROU depreciation (Rs154.83mn) and lease interest (Rs70.10mn) during fit-out capitalised into leasehold improvements rather than expensed, fully quantified and disclosed (Note 3(iv), Note 28) — standard industry practice, but it does defer P&L recognition and inflate reported EBITDA/PBT relative to an expensing policy |
| Provisioning adequacy | 4 | The Note 33 zero-quantum contingent-liability note against a ~₹110 Cr CARO disputed-dues table (finding 1) is the dominant driver; compounded by the non-monotonic ECL-rate-by-bucket swings (finding 12) and the unreconciled doubtful-debt provision lines (finding 14) |
| RPT fairness | 8.5 | RPT immaterial at ~1.3% of revenue; all transactions stated arm's-length; no loans/ICDs/guarantees to promoter entities; only the Awliv trade-payable growth (+244% YoY on a small base) is worth naming |
| Disclosure transparency | 4.5 | Multiple genuine gaps: GST SCNs absent from the Notes entirely (finding 2), MA accounting and IBR not disclosed (finding 4), unexplained 337.4% Infra & allied cost growth (finding 13), auditor's audit-trail exception not echoed in Note 45's own text (finding 10) |
| Consistency with prior years | 6 | Accounting policies stable YoY; the Design & Build carve-out is Ind AS 105-compliant but not restated across every note (a comparability trap, not an error); the statutory tax-rate assumption changed 29.12%→25.17% with no explicit election statement (pattern P3) |
| **OVERALL** | **6** | Weighted read: no evidence of outright earnings manipulation or aggressive revenue recognition; the score is pulled down almost entirely by the provisioning and disclosure-transparency dimensions, concentrated in the Note 33/CARO gap and the GST SCN absence |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Disputed tax demand (~₹110 Cr total, ~₹75.8 Cr at Delhi HC alone = 13.9% of net worth) carried outside the Ind AS 37 note | Medium-High | ITAT / Delhi HC / CIT(A) case outcomes; whether a future AR recognises any provision | Multi-year; watch FY27/FY28 AR status updates |
| GST SCNs (~₹13.6 Cr combined) absent from the Notes; a disclosure-completeness and timing gap | Medium | Resolution of the "material calculation error" claim on the second notice; any further SCNs; recurrence of LODR delay filings | Near-term, FY27 Q1-Q2 results/announcements |
| Lease cash outflow growing faster than revenue (+67.4% vs +32.9%) | High (core to LBF1 thesis) | FY27 quarterly cash-EBITDA delivery vs the Rs195-200 Cr guide; lease principal+interest trend each quarter | Each FY27 quarterly result |
| Managed Aggregation accounting opacity; no disclosed IBR | Medium | Whether the FY27 AR or investor material discloses MA-specific treatment or a numeric IBR | FY27 AR (~May 2027) or interim investor material |
| Receivables concentration (top-10 at 61.66%) plus a recurring customer default now in NCLT | Medium | Further customer defaults; top-10 concentration trend each quarter; NCLT (Hyderabad) case progress | Ongoing, each quarter |
| Audit-trail control gap at database level for core accounting software | Low-Medium | Whether the SOC assurance scope is upgraded, or the auditor's Rule 11(g) statement changes in the FY27 AR | FY27 AR |
| Opex growing ahead of revenue (Note 29, +40.8% vs +32.9%), largest driver unexplained | Medium | FY27 margin trend; any management explanation of the Infra & allied line at Halt 1 verification | FY27 quarterly results and AR |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. Why does Note 33 (contingent liabilities) disclose zero quantified amounts when the CARO Annexure
   of the same Annual Report discloses ~₹110.15 Cr of disputed statutory dues under appeal? Will a
   future AR align the two disclosures?
2. The first GST Show Cause Notice (~₹6.53 Cr) was received before the 25-May-2026 board approval of
   the FY26 accounts. Why does it not appear in Note 33 or in a subsequent-events note?
3. What is the accounting policy and lease-liability treatment for Managed Aggregation (MA)
   revenue-share arrangements, and what is the weighted-average incremental borrowing rate used to
   discount lease liabilities?
4. What drove the 337.4% YoY increase in "Infra and allied service expenses" (Rs110.48mn to
   Rs483.26mn, Note 29), and why is total Other Expenses growing (+40.8%) faster than revenue
   (+32.9%)?
5. Note 29's "Provision for doubtful debts" (Rs27.05mn) and "Provision for doubtful advances and
   deposits" (Rs41.42mn) do not reconcile to Note 36's ECL "provision made" figure of Rs57.44mn for
   the same trade-receivables pool — can management bridge the two, and do the ECL rate matrix's
   non-monotonic bucket swings (e.g. 90-180 days 10.77%→0.00%) reflect a stable methodology or
   case-specific overrides?

## E. NOTES-BASED RED FLAGS

- Note 33 (Ind AS 37 contingent liabilities) discloses zero quantified amounts against a ~₹110.15 Cr
  CARO-disclosed disputed-dues table in the same Annual Report — a disclosure-consistency failure
  that under-presents known tax risk in the note designed to carry it.
- Both GST Show Cause Notices are entirely absent from the Notes to Financial Statements; the first
  predates the date the accounts were board-approved, and no subsequent-events note exists to
  capture either.
- The second GST SCN's market disclosure ran 8 days late, requiring a formal SEBI LODR "reason for
  delay" filing — a compliance-timing gap, separate from the Notes-absence finding.
- Statutory auditor names a database-level audit-trail scope exception for the Company's core
  accounting software (Rule 11(g)) — an auditor-acknowledged control-environment gap, industry-common
  but real.
- Note 22(a)'s "no long-term contracts" statement sits in direct tension with Note 38's own
  multi-year lessor maturity table and growing finance-lease book (pattern P1).
- Note 29's doubtful-debt provision lines (Rs27.05mn + Rs41.42mn) do not reconcile to Note 36's ECL
  "provision made" figure (Rs57.44mn) for what appears to be the same receivables pool, unbridged
  anywhere in the Notes.

No evidence of revenue manufactured outside disclosed policy, no undisclosed related-party
self-dealing, and no auditor qualification or Material Uncertainty paragraph on going concern in
either opinion. The red flags above sit on the disclosure-completeness and provisioning axis, not on
fabricated or manipulated revenue/expense recognition.

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices. Key concern: contingent-liability and GST-notice
disclosure gaps sit against a known, quantified ~₹110 Cr-plus tax exposure. Key strength: clean,
immaterial related-party transactions and fully quantified, well-disclosed lease and ESOP accounting.
Overall accounting quality: 6/10.

═══════════════════════════════════════════════════════════════
## LOAD-BEARING FACTS STATUS (final, after all three passes)
═══════════════════════════════════════════════════════════════
- **LBF1 (cash EBITDA bridge, lease cash outflow): PARTIALLY CONFIRMED FROM NOTES.** Note 38 gives
  the exact lease cash outflow (Rs4,121.64mn FY26, +67.4% YoY, finding 3) — the single largest,
  most directly relevant number the Notes contribute to the reported-to-cash EBITDA bridge. The
  Notes do not themselves compute or reconcile a cash-EBITDA figure to the FY27 Rs195-200 Cr guide
  or the Q1 FY27 Rs44 Cr delivery; that reconciliation needs the Cash Flow Statement and results
  filings, outside this stage's remit.
- **LBF2 (lease book and ALM): CONFIRMED FROM NOTES (partial).** Full lease liability maturity
  analysis given (finding 3 context); effective interest rate fell to 9.05% from 11%. No MA-vs-
  straight-lease split and no numeric IBR found (finding 4). The 2021 lease resets named in company
  memory are not in this AR's notes (too old for this year's comparatives; would need the FY22 AR).
- **LBF3 (governance and control, business transfer): CONFIRMED FROM NOTES.** Design & Build
  transfer fully detailed (finding 5); CFO change, Company Secretary change, and director
  resignation all confirmed in the Note 32 KMP list; GST SCNs confirmed present in the corpus but
  absent from the Notes (findings 2 and 9 — the governance-relevant fact is the disclosure gap
  itself).
- **LBF4 (occupancy and churn): OUT OF SCOPE for this stage.** Occupancy % and seat-count churn are
  MD&A/business-description KPIs, not Notes items. The only churn-adjacent Notes fact is the
  recurring two-year customer default/NCLT item (Note 46B), carried in the "additional items" list
  under Section A.

═══════════════════════════════════════════════════════════════
## RESTATEMENTS / RECLASSIFICATIONS FOUND (final)
═══════════════════════════════════════════════════════════════
- Note 48 (standalone) and its consolidated equivalent: standard "previous year figures
  regrouped/reclassified... not material" boilerplate, no items named.
- The Design & Build disposal group's FY25 comparatives sit in the supplementary Note 40 only, not
  restated as a continuing-operations-only column throughout every other note (Notes 8, 22).
  Ind AS 105-compliant, not an error, but a genuine comparability trap.
- Consolidated Note 1 "Group overview" and "Basis of consolidation" paragraphs are drafted in the
  singular, omitting Awfis Transform Pvt Ltd by name, even though the consolidated group-information
  table and related-party note correctly consolidate both subsidiaries at 100%. A note-preparation
  QC gap, not a consolidation-scope error.
- The statutory tax-rate assumption used in Note 39's reconciliation changed from 29.12% (FY25) to
  25.17% (FY26) with no explicit Section 115BAA election statement anywhere in the Notes (pattern P3).

═══════════════════════════════════════════════════════════════
## GOING CONCERN LANGUAGE (final)
═══════════════════════════════════════════════════════════════
Present in both standalone (Note 2, p.92) and consolidated (Note 2, p.133-134) Basis of Preparation
notes — management's own paragraph, not an auditor qualification. Cites a net current liability
position (standalone Rs3,388.14mn FY26, +58.3% YoY; consolidated Rs3,127.70mn, +48.2% YoY) and
concludes going-concern preparation is appropriate, citing planned fund-raising, operating cash
generation, and working-capital optimisation. The Independent Auditor's Report carries NO Material
Uncertainty Related to Going Concern paragraph and NO Emphasis of Matter paragraph in either opinion
— both unmodified. Pattern finding P2 (above) notes this sits beside a negative net-debt / net-cash
position (Note 34: net debt Rs(381.63)mn standalone), which resolves on inspection (the current
portion of lease liabilities drives the net-current-liability figure, not a cash shortage) but is
worth naming as a presentation-juxtaposition point.

═══════════════════════════════════════════════════════════════
## CORRECTION APPLIED FROM PASS 2
═══════════════════════════════════════════════════════════════
Pass 1's input_gaps stated "No numeric ECL loss-rate-by-ageing-bucket matrix disclosed." This was
incorrect as stated: the matrix exists in Note 36(b)(II) (standalone p.116), not Note 8 where Pass 1
looked. It is removed from the final input_gaps below and instead carried as finding 12 (Section A),
reflecting the matrix's non-monotonic, materially volatile bucket-level rates rather than its
absence.

═══════════════════════════════════════════════════════════════
## FINAL INPUT GAPS (genuine, after Pass 2's correction)
═══════════════════════════════════════════════════════════════
1. No weighted-average incremental borrowing rate (IBR) disclosed anywhere in the standalone or
   consolidated Notes (Note 4M references IBR, gives no numeric rate).
2. No separate accounting policy, revenue line, or lease treatment disclosed for Managed Aggregation
   (MA) revenue-share arrangements anywhere in the Notes; MA is discussed only in the MD&A/business-
   description sections, outside the Notes.
3. No explicit statement of when/whether the Company formally elected Section 115BAA (25.17%
   concessional rate); visible only by comparing the FY26 vs FY25 statutory-rate lines in Note 39.
4. 2021 lease resets named in company memory (LBF2) are not mentioned anywhere in the FY26 AR notes;
   would require the FY22 AR, which is not in the corpus.

```yaml
stage: B02-notes
company: "AWFIS"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
input_gaps:
  - "No weighted-average incremental borrowing rate (IBR) disclosed anywhere in the standalone or consolidated Notes (Note 4M references IBR, gives no numeric rate)"
  - "No separate accounting policy, revenue line, or lease treatment disclosed for Managed Aggregation (MA) revenue-share arrangements anywhere in the Notes; MA discussed only in MD&A/business-description sections outside the Notes"
  - "No explicit statement of when/whether the Company formally elected Section 115BAA (25.17% concessional rate); visible only by comparing the FY26 vs FY25 statutory-rate lines in Note 39"
  - "2021 lease resets named in company memory (LBF2) are not mentioned anywhere in the FY26 AR notes; would require the FY22 AR, not in corpus"
flags:
  - {type: FLAG-CASH, reason: "Standalone net current liability position grew 58.3% YoY (Rs2,140.98mn to Rs3,388.14mn, Note 2 going-concern paragraph); lease cash outflow grew 67.4% YoY (Note 38) outpacing continuing-ops revenue growth of 32.9%; top-10 customer receivable concentration jumped from 42.74% to 61.66% (Note 36); the previously zero-risk unbilled receivables bucket now carries a 17.32% ECL rate versus 0.00% prior year (Note 36). None individually breaches going-concern (auditor opinion unmodified, net debt negative), but together they are a working-capital and cash-conversion texture that downstream valuation and FTTCP stages should weigh against the FY27 cash-EBITDA guide."}
accounting_quality: 6
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Note 33 (contingent liabilities) discloses zero quantified amounts in both standalone and consolidated FS, while the standalone auditor's CARO Annexure discloses ~Rs1,101.50mn (~INR110.15 Cr) of disputed statutory dues under appeal (Income Tax Rs1,083.38mn incl. Rs757.93mn at Delhi HC = 13.9% of net worth; GST Rs18.12mn), none of which appear in the Ind AS 37 note itself", note_ref: "Note 33, standalone p.112-113 / consolidated p.155-156; CARO Annexure p.86", rating: "RED", why: "The statutory note designed to carry exactly this information carries nothing; the only quantum in the entire AR sits in a different statutory report"}
  - {rank: 2, finding: "Two GST Show Cause Notices (~Rs6.53 Cr FY23-24, ~Rs7.10 Cr FY22-23) are entirely absent from the Notes to Financial Statements; the first predates the 25-May-2026 board approval of the FY26 accounts and no subsequent-events note exists", note_ref: "Cross-checked against announcements 20260521-*, 20260602-*, 20260604-*; NOT FOUND in Note 33 or elsewhere", rating: "RED", why: "A known, dated, quantified tax demand that existed before the accounts were approved is missing from the notes meant to capture it"}
  - {rank: 3, finding: "Lease cash outflow (principal+interest) grew 67.4% YoY (Rs2,462.21mn to Rs4,121.64mn) while continuing-ops revenue grew 32.9%; principal repayment alone grew 114.2%", note_ref: "Note 38, p.120-121", rating: "YELLOW", why: "The most direct notes-based number bearing on LBF1's cash-EBITDA bridge; lease cash commitment growing materially faster than revenue"}
  - {rank: 4, finding: "Managed Aggregation (MA) revenue-share accounting is NOT FOUND anywhere in the Notes; no numeric weighted-average IBR disclosed for lease liabilities", note_ref: "Note 4A/4M p.93-94, 96-97; Note 38, p.120-121", rating: "YELLOW", why: "Direct gap against LBF2; the Notes do not show how MA is accounted for differently from owned/leased centres, or what discount rate underlies the Rs14,502.69mn lease liability"}
  - {rank: 5, finding: "Design & Build business transfer to Awfis Transform Pvt Ltd: slump sale Rs265.91mn, timeline extended to 31-Dec-2026 pending revised valuation; the transferring segment's revenue fell 7.8% and PBT fell 31.9% YoY in the same year of the carve-out", note_ref: "Note 40, p.122-123", rating: "YELLOW", why: "Directly answers LBF3; the asset being transferred is shrinking, and the stated consideration is not final"}
  - {rank: 6, finding: "Lessor-side finance lease reclassification: number of finance leases grew from 9 to 30 YoY, net investment in finance lease +76.1% (Rs2,035.33mn to Rs3,583.51mn), finance lease income +302.8%", note_ref: "Note 38 Part II (lessor), p.121", rating: "YELLOW", why: "A real, quantified shift toward front-loaded interest-method income and away from straight-line rental; changes revenue quality and balance-sheet composition"}
  - {rank: 7, finding: "Effective tax rate is 0% both years; large DTL (ROU/PPE + finance lease receivables) exactly nets a large DTA (lease liabilities + carryforwards), management choosing not to recognise DTA in excess of DTL", note_ref: "Note 39, p.121-122", rating: "YELLOW", why: "Explains the low effective tax rate as a structural, if anything conservative, feature of the lease book; ~Rs150-250mn of unrecognised carryforward benefit is a future non-cash-credit watch item"}
  - {rank: 8, finding: "Total diluted EPS flat YoY (Rs9.34 both years) despite standalone continuing-ops revenue +32.9%, because FY25 PAT included a lapsed one-off Rs251.02mn exceptional gain and FY26 discontinued-ops profit fell 31.9%; continuing-operations-only PAT actually grew 20.5%", note_ref: "Note 31, p.110-111", rating: "YELLOW", why: "A required priority-topic item Pass 1 skipped; flat headline PAT/EPS is an optics artefact, not underlying deterioration"}
  - {rank: 9, finding: "Second GST SCN disclosed to exchanges 8 days after receipt, requiring a formal SEBI LODR 'reason for delay' filing citing a material calculation error under review", note_ref: "Cross-checked against announcements 20260602-*, 20260604-*; not in the AR Notes", rating: "YELLOW", why: "A distinct compliance-timing point beyond the Notes-absence finding; the notice was received the same day the FY26 accounts were board-approved"}
  - {rank: 10, finding: "Statutory auditor states it is unable to comment on whether the database-level audit-trail feature was enabled and operated throughout the year for the Company's core third-party-hosted accounting software (SOC Type 2 report did not address database-level logs)", note_ref: "Note 45, p.124-125; Auditor's Report Rule 11(g), p.85-86", rating: "YELLOW", why: "An auditor-acknowledged control-environment scope gap on a mandatory Companies Act requirement; common industry-wide but not previously surfaced"}
  - {rank: 11, finding: "Top-10 customer receivable concentration rose from 42.74% (FY25) to 61.66% (FY26) of total trade receivables outstanding", note_ref: "Note 36(b)(II), p.116", rating: "YELLOW", why: "Qualifies the receivables-ageing improvement read; ageing mix improved while customer concentration worsened materially in the same year"}
  - {rank: 12, finding: "ECL loss-rate-by-ageing-bucket matrix exists (Note 36, not Note 8 as first checked) and swings non-monotonically YoY, including a new 17.32% rate on the previously zero-risk unbilled/current-not-due bucket", note_ref: "Note 36(b)(II), p.116", rating: "YELLOW", why: "Correction to a Pass 1 NOT FOUND claim; the volatility pattern reads more like case-specific provisioning than a stable statistical loss model"}
  - {rank: 13, finding: "'Infra and allied service expenses' grew Rs110.48mn to Rs483.26mn (+337.4% YoY) with no narrative explanation anywhere in the Notes; total Other Expenses grew 40.8% YoY, outpacing continuing-ops revenue growth of 32.9%", note_ref: "Note 29, p.109-110", rating: "YELLOW", why: "A second, independent margin-quality data point beyond the lease-cost story; the largest driver is disclosed with zero explanation"}
  - {rank: 14, finding: "New/enlarged doubtful-debt provisions in Note 29 (Rs27.05mn + Rs41.42mn) do not cleanly reconcile to Note 36's ECL roll-forward figure of Rs57.44mn 'provision made' for the same receivables pool", note_ref: "Note 29, p.109-110, cross-checked against Note 36, p.117", rating: "YELLOW", why: "Two different bad-debt-related numbers for what may be overlapping pools, unbridged in the Notes"}
  - {rank: 15, finding: "Internal contradiction: Note 22(a) states the Company has not entered into long-term contracts with customers, while Note 38's own lessor maturity table shows client lease receivables running 4-5 years and a finance-lease book that grew from 9 to 30 leases", note_ref: "Note 22(a), p.108; Note 38 Part II, p.121", rating: "YELLOW", why: "Pattern-pass finding; almost certainly an Ind AS 115 practical-expedient statement rather than a description of underlying lease terms, but reads as contradictory at face value"}
red_flags:
  - "Note 33 discloses zero quantified contingent liabilities against a ~Rs110.15 Cr CARO-disclosed disputed-dues table in the same Annual Report"
  - "Both GST Show Cause Notices are entirely absent from the Notes to Financial Statements; the first predates board approval of the accounts and no subsequent-events note exists"
  - "Second GST SCN market disclosure ran 8 days late, requiring a formal SEBI LODR 'reason for delay' filing"
  - "Statutory auditor names a database-level audit-trail scope exception for the Company's core accounting software (Rule 11(g))"
  - "Note 22(a) 'no long-term contracts' statement sits in direct tension with Note 38's own multi-year lessor maturity table and growing finance-lease book"
  - "Note 29 doubtful-debt provision lines (Rs27.05mn + Rs41.42mn) do not reconcile to Note 36's ECL 'provision made' figure (Rs57.44mn) for the same receivables pool"
questions_for_mgmt:
  - "Why does Note 33 disclose zero quantified contingent liabilities when the CARO Annexure of the same Annual Report discloses ~Rs110.15 Cr of disputed statutory dues under appeal? Will a future AR align the two disclosures?"
  - "The first GST Show Cause Notice (~Rs6.53 Cr) was received before the 25-May-2026 board approval of the FY26 accounts. Why does it not appear in Note 33 or in a subsequent-events note?"
  - "What is the accounting policy and lease-liability treatment for Managed Aggregation (MA) revenue-share arrangements, and what is the weighted-average incremental borrowing rate used to discount lease liabilities?"
  - "What drove the 337.4% YoY increase in 'Infra and allied service expenses' (Rs110.48mn to Rs483.26mn, Note 29), and why is total Other Expenses growing (+40.8%) faster than revenue (+32.9%)?"
  - "Note 29's doubtful-debt provisions (Rs27.05mn + Rs41.42mn) do not reconcile to Note 36's ECL 'provision made' figure of Rs57.44mn for the same trade-receivables pool - can management bridge the two, and do the ECL rate matrix's non-monotonic bucket swings reflect a stable methodology or case-specific overrides?"
receivables_trend: "stable (mixed signals): ageing >6 months improved from ~27.1% (Rs345.91mn/Rs1,277.20mn FY25) to ~21.1% (Rs107.56mn/Rs510.99mn FY26, Note 8), but this is distorted by the Design & Build carve-out (Rs937.14mn receivables moved to held-for-sale, Note 40); top-10 customer concentration rose from 42.74% to 61.66% (Note 36); the unbilled/current-not-due bucket ECL rate rose from 0.00% to 17.32% (Note 36). Net read: smaller, better-aged, but more concentrated and carrying a new pocket of expected loss versus a year ago."
restatements_found:
  - "Note 48 (standalone) and consolidated equivalent: standard 'previous year figures regrouped/reclassified... not material' boilerplate, no items named"
  - "Design & Build disposal group FY25 comparatives sit in the supplementary Note 40 only, not restated as a continuing-operations-only column throughout every other note (Notes 8, 22); Ind AS 105-compliant, not an error, but a comparability trap"
  - "Consolidated Note 1 'Group overview' and 'Basis of consolidation' paragraphs drafted in the singular, omitting Awfis Transform Pvt Ltd by name, even though the consolidated group-information table and related-party note correctly consolidate both subsidiaries at 100% - a note-preparation QC gap, not a consolidation-scope error"
  - "Statutory tax-rate assumption used in Note 39 changed from 29.12% (FY25) to 25.17% (FY26) with no explicit Section 115BAA election statement anywhere in the Notes"
going_concern_language: "PRESENT, both standalone (Note 2, p.92) and consolidated (Note 2, p.133-134): management's own paragraph (not an auditor qualification) cites a net current liability position (standalone Rs3,388.14mn FY26, +58.3% YoY; consolidated Rs3,127.70mn, +48.2% YoY) and concludes going-concern preparation is appropriate, citing planned fund-raising, operating cash generation, and working-capital optimisation. Auditor's Report carries NO Material Uncertainty Related to Going Concern paragraph and NO Emphasis of Matter paragraph in either opinion - both unmodified. Sits beside a negative net-debt/net-cash position (Note 34: Rs(381.63)mn standalone), which resolves on inspection (current portion of lease liabilities drives the figure) but is worth naming as a presentation-juxtaposition point."
analyst_note: >
  Three items should carry weight beyond their individual ratings. First, findings 1 and 2 (Note 33
  vs CARO; GST SCN absence) compound each other: both are disclosure-completeness failures on tax
  exposure, not earnings manipulation, but together they are a pattern of under-presenting known tax
  risk in the statutory notes specifically built to carry it, worth a direct Halt 1 question rather
  than two separate footnotes. Second, the accounting_quality score of 6/10 is driven almost entirely
  by the provisioning and disclosure-transparency dimensions; revenue recognition and RPT fairness
  score well, so this is not a red flag on core earnings quality. Third, LBF1's cash-EBITDA
  reconciliation is only partially answerable from the Notes: Note 38's Rs4,121.64mn FY26 lease cash
  outflow (+67.4% YoY) is the load-bearing anchor, but the actual bridge to the FY27 Rs195-200 Cr
  cash-EBITDA guide needs the Cash Flow Statement and results filings, which sit outside this stage.
```
