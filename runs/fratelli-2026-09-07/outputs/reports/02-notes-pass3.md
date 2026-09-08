# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3 (PATTERN PASS + CONSOLIDATION)
Company: Fratelli Vineyards Ltd (FRATELLI) | Run date: 2026-09-07
Sources: Annual_Report_FY2026.pdf and Annual_Report_FY2025.pdf (.txt mirrors,
page markers cross-checked), plus runs/fratelli-2026-09-07/inputs/screening/
screener-Data_Sheet.csv and outputs/reports/01-gate0.md for the load-bearing
contradiction test below. Figures in Rs lakhs as filed; Rs crore shown once
per figure.

This is the third and final pass. Instead of a sequential note-by-note
re-read, this pass hunts for PATTERNS: contradictions between notes,
mismatches between notes and the main statements, deliberately thin
disclosure, restatements, post-balance-sheet events, and going-concern
language. It also carries the one mandatory task assigned to this run:
settling, on source, the contradiction between Stage 1's screener-derived
gross margin/Other Expenses read and Stage 2 Pass 1's audited Note 30 read.

═══════════════════════════════════════════════════════════
LOAD-BEARING FACT 2 — SETTLED: SAME ENTITY, SAME STATEMENT, SAME YEAR.
THE DIFFERENCE IS A THIRD-PARTY DATA VENDOR ARTIFACT, NOT A COMPANY
RECLASSIFICATION OR A DIFFERENT REPORTING BASIS.
═══════════════════════════════════════════════════════════

The hypothesis offered in the brief (different entity / different
consolidation basis / different presentation format) does NOT hold. Both
Stage 1 and Stage 2 Pass 1 are reading the SAME entity (FRATELLI
consolidated Group), the SAME statement (the audited consolidated
Statement of Profit and Loss under Ind AS Schedule III), the SAME year
(FY26), sourced ultimately from the SAME underlying filing. The screener
CSV's Sales (Rs 181.29 cr), Raw Material Cost (Rs 54.98 cr), Employee Cost
(Rs 35.22 cr), Depreciation (Rs 8.84 cr), Interest (Rs 13.26 cr) and PBT
(Rs -26.67 cr) all tie almost exactly to the audited AR figures already
anchored in Pass 1 (Note 23 revenue Rs 181.29 cr; Note 25(a) materials Rs
54.93 cr; Note 27 employee cost; Note 30 finance cost/depreciation split;
Note 31 PBT). What does NOT tie is the sub-classification of operating
costs into screener's own internal taxonomy: "Power and Fuel," "Other
Mfr. Exp," "Selling and admin," "Other Expenses" (screener-Data_Sheet.csv,
rows 14-18).

Arithmetic proof this is a vendor sub-classification break, not a real
number:
- Screener FY26 shows Power and Fuel and Other Mfr. Exp as BLANK, and
  Selling and admin as BLANK, with only Other Expenses populated at Rs
  114.14 cr (screener-Data_Sheet.csv, row 14-18, FY26 column). In FY24 and
  FY25, all four of these categories carry non-blank values (screener-
  Data_Sheet.csv, same rows, FY24/FY25 columns) — i.e. the FY26 column is
  the ONLY one where three of four sub-categories fail to populate.
- Rebuilding screener's own PBT bridge for FY26 (EBITDA = Sales − [Raw
  Material + Change in Inventory + Power&Fuel + Other Mfr Exp + Employee
  Cost + Selling&Admin + Other Expenses]; PBT = EBITDA + Other Income −
  Depreciation − Interest) using ONLY the non-blank FY26 cells: 54.98
  (Raw Material) − 15.26 (Change in Inventory, signed as a subtraction,
  matching the AR Note 26 sign of Rs (1,526.23) lakh, i.e. inventory
  build) + 35.22 (Employee Cost) + 114.14 (Other Expenses) = Rs 189.08 cr
  total cost. EBITDA = 181.29 − 189.08 = Rs -7.79 cr. PBT = -7.79 + 3.22 −
  8.84 − 13.26 = Rs -26.67 cr — this reproduces screener's own reported
  FY26 PBT (Rs -26.67 cr, screener-Data_Sheet.csv row 22) EXACTLY, and is
  independently corroborated by the sum of screener's own FY26 quarterly
  "Operating Profit" line (-2.97+0.79-0.59-5.0 = Rs -7.77 cr, matching the
  -7.79 cr EBITDA above to within rounding) (screener-Data_Sheet.csv, row
  36, quarters columns 6-9).
- Conclusion: the Rs 114.14 cr "Other Expenses" figure for FY26 is
  screener's OWN INTERNAL BALANCING FIGURE for the sum of what it could
  not separately classify that year (materially, whatever it labelled
  "Power and Fuel," "Other Mfr. Exp." and "Selling and admin" in FY24/FY25
  got folded into a single bucket for FY26), not a company-side
  reclassification and not a different number from a different basis. The
  Group total (Sales, PBT) is internally consistent across both sources;
  only the sub-line taxonomy inside the cost stack breaks down for one
  column of one vendor's spreadsheet.
- The AUDITED Note 30 (consolidated, Annual_Report_FY2026.pdf, p.176)
  "Other expenses" line is Rs 85.69 cr FY26, stable against Rs 89.90 cr
  FY25 and Rs 85.63 cr FY24 (Pass 1, Section 2) — no reclassification
  event exists in the audited note across any of the three years, and the
  correctly named "Selling, distribution & marketing expenses" sub-line
  inside Note 30 is Rs 42.14 cr FY26 (23.3% of wine revenue), not the
  screener "Selling and admin" figure of any year, which does not match
  this sub-line in any year either (screener FY25 "Selling and admin" Rs
  77.12 cr vs the AR's own Note 30 S&D sub-line of Rs 45.88 cr FY25 — a
  gap that pre-dates FY26 and confirms screener's category boundaries have
  never mapped 1:1 onto the AR's own note structure; FY26 is simply the
  year the vendor's parser broke down completely rather than partially).

RESOLUTION FOR DOWNSTREAM USE: use the AUDITED AR basis for all COGS,
gross margin, and A&P work on this name. Netting Note 25(a) materials
consumed (Rs 54.93 cr) plus purchase of stock-in-trade (Rs 0.05 cr) against
the change-in-inventories credit (Rs -15.26 cr) against Note 23 revenue
(Rs 181.29 cr) gives a properly computed gross margin of 78.1% FY26,
matching management's stated 77-80% range (Pass 1, Section 2). The correct
FY26 advertising/marketing figure is Rs 42.14 cr (23.3% of wine revenue),
per the Note 30 Selling, distribution & marketing sub-line, not "NOT
FOUND" as the screener-only read would suggest. Stage 1's Gate 0 "69.7%
material-cost-only" and "54.2%" FY25 figures were built on the Raw
Material Cost row alone without netting the inventory movement, which
independently explains the apparent gap even before the vendor-taxonomy
issue above is considered; the two effects compound into the discrepancy
Gate 0 flagged. Both stages' underlying source documents/data feeds are
accurately transcribed as far as they go; the resolution is that the AR
Note 25/26/30 basis (78.1% GM, Rs 85.69 cr Note 30 total, Rs 42.14 cr A&P)
is the figure of record for valuation, and the screener CSV's FY26 "Other
Expenses"/"Selling and admin" columns specifically should be treated as
unreliable for cost sub-classification (though Sales, PBT, Raw Material,
Employee Cost, Depreciation and Interest from the same CSV do tie out and
remain usable).

═══════════════════════════════════════════════════════════
OTHER PATTERN-PASS FINDINGS
═══════════════════════════════════════════════════════════

1. AUDITOR'S REPORT INTERNAL DRAFTING ERROR, SHARPENED FROM PASS 2. The
   consolidated Independent Auditor's Report carries an "Emphasis of
   matters" paragraph on Note 44 (Annual_Report_FY2026.pdf, p.~130,
   line-anchor "Emphasis of matters... We draw attention to note no. 44
   ... regarding decline in revenue from operations of the Holding
   company"), and then repeats the IDENTICAL paragraph, word for word,
   under a separate "Key Audit Matters" heading immediately below it
   (Annual_Report_FY2026.pdf, same page range). Both copies of the
   paragraph also contain an internal error: the CONSOLIDATED auditor's
   report twice refers to "the accompanying standalone financial
   statements of the Holding company have been prepared on a going
   concern basis" — language belonging in the STANDALONE opinion, carried
   over verbatim into the CONSOLIDATED opinion, which should refer to the
   consolidated financial statements. By contrast, the STANDALONE
   auditor's report states, correctly and separately, "there are no key
   audit matters to be communicated in our report" (Annual_Report_
   FY2026.pdf, p.~113) for the identical underlying fact pattern (revenue
   decline, going concern). 🟡 This is a document-quality finding about
   the AUDIT REPORT itself, not the financial statements: three separate
   drafting defects (duplication across two headings meant to serve
   different purposes under SA 701/706, a copy-paste of standalone
   language into the consolidated opinion, and inconsistent treatment of
   the same fact between the two opinions in one signed report set) in a
   single audit report. The opinion itself is unmodified/clean at both
   entity levels; this is a red flag for audit rigor/review quality, not
   an accounting or going-concern qualification.

2. DIRECTORS' REPORT HEADLINE ERROR, RE-VERIFIED AGAINST THE FACE OF THE
   P&L (confirms Pass 2 Finding 1 with an additional direct anchor). The
   Directors' Report's own "Key Financial Highlights" table
   (Annual_Report_FY2026.pdf, p.42/printed p.39, line-anchor "Revenue from
   Operations 67.83 12,471.59 18,128.65 17,844.09") states Consolidated
   FY 2024-25 Revenue from Operations as Rs 17,844.09 lakh. The audited
   consolidated Statement of Profit and Loss, same annual report
   (Annual_Report_FY2026.pdf, p.~155, line-anchor "Revenue from operations
   23 18,128.65 30,209.66"), states the FY25 comparative as Rs 30,209.66
   lakh. Both figures sit in the SAME document; the Directors' Report
   table is provably wrong (Pass 2 traced it to the wine subsidiary's own
   standalone contribution, mislabelled "Consolidated"). No new fact
   beyond Pass 2, but the pattern search independently re-confirms this
   is a real, anchored contradiction between two sections of the same
   filing, not a Pass 2 misreading.

3. GOING-CONCERN LANGUAGE, VERBATIM, BOTH ENTITY LEVELS (for the record;
   substance already flagged in Pass 2 Finding 4). Standalone Note 39 and
   the standalone auditor's Emphasis of Matter both state: "the Company
   has adequate surplus funds to meet its operational and financial
   obligations for the foreseeable future... the standalone financial
   statements have been prepared on a going concern basis"
   (Annual_Report_FY2026.pdf, p.129-130 and p.~112). The consolidated
   equivalent (Note 44) and consolidated auditor's paragraph use near-
   identical wording. Neither the standalone nor the consolidated
   going-concern paragraph names the Rs 114.50 cr guarantee, the Rs 9.24
   lakh standalone cash balance, or the Rs 7.78 lakh consolidated cash
   balance anywhere in the going-concern discussion itself (those figures
   sit in other notes: Note 42(a)/Note 6 standalone for the guarantee and
   loan, Note 38 consolidated Capital Management for cash). "Adequate
   surplus funds" is asserted, not reconciled to a stated cash figure, in
   either going-concern note.

4. No other contradiction between a note and the main financial
   statements was found beyond the two already identified (the Directors'
   Report comparator, and the vendor-artifact settled above). Cross-
   checks performed and found CONSISTENT: Note 39 contingent liability
   sub-items (Rs 1,148.59 + 732.85 + 1,906.46 lakh) sum exactly to the
   Rs 3,787.90 lakh total (Note 39, p.192); Note 8 DTA components sum to
   the stated net DTA; Note 15 share capital roll-forward ties to the
   closing share count; Note 37 segment revenue ties to Note 23 revenue
   from operations after inter-segment elimination.

PASS 3 additional findings beyond the mandatory contradiction: two
(the auditor's-report drafting-quality finding above, and the direct
face-of-P&L anchor corroborating Pass 2's Directors'-Report finding). No
further MATERIAL new findings emerged from the going-concern and
restatement sweep beyond what Pass 1 and Pass 2 already surfaced.

═══════════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Directors' Report "Key Financial Highlights" table mislabels the wine subsidiary's own standalone FY25 result (Rev Rs 17,844.09 lakh, PAT loss Rs 1,283.82 lakh) as total "Consolidated FY 2024-25" (true audited consolidated FY25: Rev Rs 30,209.66 lakh, PAT loss Rs 1,706.26 lakh, same AR); proven by arithmetic, Note 48 Schedule III entity-loss-share, and the FY2025 AR's own correct prior-year table | Directors' Report p.42/39; Note 48 p.200-201; audited P&L p.~155 | RED | The AR's own headline "1.59% consolidated revenue growth" claim is not like-for-like; true YoY movement is a 40.0% revenue decline |
| 2 | Only FY26 is a genuine wine-only year; FY24 (47% wine/53% legacy agro+steel) and FY25 (59% wine/41% legacy) both carry a material non-wine trading book; no Ind AS 105 discontinued-operations restatement exists; Note 1 Corporate Information still describes the company as an agro/steel trader | Note 37, consolidated, FY26 AR p.187 and FY25 AR p.187; Note 1 p.145 | RED | Any FY24-FY26 consolidated revenue CAGR is not like-for-like; only the wine segment line (Rs 212.88cr to Rs 178.44cr to Rs 181.20cr) is comparable |
| 3 | New Rs 114.50 cr corporate guarantee (from Nil FY25) plus new Rs 9.33 cr working-capital loan @10%, both from the near-zero-operations shell holding company to the wine subsidiary | Note 42(a) and Note 6, standalone, p.129 and p.103-104 | RED | Concentrates 100% of Group credit risk on the wine subsidiary with the shell parent as sole guarantor of record |
| 4 | Going-concern notes (standalone Note 39, consolidated Note 44) do not mention or stress-test the Rs 114.50 cr guarantee against a standalone cash balance of Rs 9.24 lakh and consolidated cash of Rs 7.78 lakh (down 84.5% YoY); consolidated auditor's Emphasis of Matter is duplicated verbatim under Key Audit Matters, with standalone-opinion language mistakenly carried into the consolidated opinion; standalone auditor's report states no KAMs for the same fact | Note 39 p.129-130; Note 44 p.198; Auditor's Report p.~112-130 | RED | The going-concern assessment is silent on the single largest financial commitment on the standalone balance sheet, against a near-zero cash cushion; the audit report itself shows drafting/review-quality defects |
| 5 | Promoter warrant forfeiture corrected to 65.1% (3,63,150 of 5,57,650 warrants lapsed at the Feb-2026 SEBI ICDR deadline), not the 39.5% previously assumed; five named related parties (Gaurav Sekhri, Aarti Sekhri, Puja Sekhri, Shobha Sekhri, Chin Min Developers) converted their entire allotments, so all lapsed warrants belong to other, unnamed allottees | Note 13(e)/(f) standalone p.108-109; Note 30(B)(i) standalone p.118-119 | RED | Corrects a load-bearing prior in the more negative direction: nearly two-thirds, not two-fifths, of the promoter warrant commitment was not honoured |
| 6 | Injected "Other Expenses reclassification" (Rs 114.14cr FY26/Rs 7.53cr FY25/"Selling and admin blank") does not exist in either audited AR; it is a third-party (screener.in) data-vendor sub-classification artifact for FY26 only, proven by an exact PBT-bridge reconciliation; the audited Note 30 total is stable at Rs 85-90cr across FY24-FY26, and the correctly netted gross margin is 78.1% FY26, matching management's 77-80% claim | Note 30, consolidated, p.176 (all 3 years); this pass's arithmetic proof above | GREEN (resolved) | Settles load-bearing fact 2: valuation should use the AR Note 25/26/30 basis (78.1% GM, Rs 42.14cr A&P), not the screener CSV's FY26 cost sub-classification |
| 7 | Holding company reversed Rs 3.53 cr of previously recognised DTA in full (all components: doubtful debts, bought-forward losses, PP&E timing, employee benefits, other), judging future standalone taxable profits no longer probable; recognised Group DTA is now 96.5% carried-forward-loss-based | Note 8 and Note 31(a), consolidated, p.163-165, 177; Note 8 standalone p.104-105 | RED | Sits uneasily against the going-concern note's "exploring new business opportunities" language in the same document; DTA realism increasingly dependent on future profits not yet evidenced |
| 8 | Gearing ratio 64.6% to 88.0% and current ratio 1.69 to 1.37 in one year; 89.4% of debt floating-rate, 69.8% technically repayable on demand (cash credit) | Note 38 and Note 36(B), consolidated, p.184, 189 | RED | Rising leverage into a second consecutive loss-making year with a thinning liquidity cushion |
| 9 | Of Rs 733.86 lakh gross bad debts written off in FY26, Rs 250.77 lakh was absorbed against the pre-existing ECL provision but Rs 483.09 lakh was a fresh, entirely un-provisioned P&L charge, 9.8x FY25's equivalent (Rs 49.29 lakh), possibly linked to the customer whose revenue share fell from 17.3% to 11.6% in the same year (unconfirmed) | Note 30 p.176/179; Note 10(b) and Note 36(C), p.163, 186 | RED | Bypasses the normal provide-then-write-off ECL lifecycle for over half the year's write-off; needs a direct management reconciliation |
| 10 | A Section 270 "misreporting of income" penalty order of Rs 663.03 lakh (AY 2018-19) sits inside the aggregate Income Tax contingent liability figure, not separately named until this stage | Note 39(A)(iii) consolidated p.189-190; Note 35(A)(iii) standalone p.127 | RED | A formal misreporting penalty is qualitatively more serious than an ordinary quantum tax dispute |
| 11 | Trade receivables Rs 105.11cr against Rs 181.29cr revenue = 212 days DSO; >6-month ageing bucket improved from 42.2% to 24.3% of receivables, but 23.4% of all receivables still sit in the 6-12 month band | Note 10(a), consolidated, p.161-163 | YELLOW | Mixed signal: ageing mix improving, but DSO remains very long for a consumer beverage business; feeds the working-capital deterioration pattern |
| 12 | MSME payable dues more than tripled (Rs 27.81 lakh to Rs 93.27 lakh, +235%); accrued unpaid MSME interest rose 20x | Note 19 and Note 40, consolidated, p.171-172 | YELLOW | Directional deterioration in small-supplier payment discipline; compliance/reputational exposure under the MSMED Act |
| 13 | Contingent liabilities up 27.5% YoY to Rs 37.88cr (27.9% of net worth), driven by two new Maharashtra CST "F-Form" demands totalling Rs 17.96cr, on top of recurring multi-state GST notices | Note 39(A)(v)-(xvi), consolidated, p.191-192 | YELLOW | VAT/CST is now the largest and fastest-growing contingent liability bucket |
| 14 | Consolidated auditor's Emphasis of Matter on Note 44 is duplicated verbatim under a separate Key Audit Matters heading, and both copies mistakenly reference "the standalone financial statements of the Holding company" inside the consolidated opinion; the standalone opinion, for the identical fact, states no KAMs at all | Independent Auditor's Report, consolidated, p.~130; standalone, p.~112-113 | YELLOW | Audit-documentation quality defect (SA 701/706 heading confusion, copy-paste error); opinion itself remains unmodified/clean |
| 15 | Consolidated cash and cash equivalents fell 84.5% YoY to Rs 7.78 lakh against Rs 119.74cr of Group borrowings; standalone cash is Rs 9.24 lakh, flat YoY | Note 38, Capital Management, consolidated, p.189 | YELLOW | The Group is running with, in practical terms, no cash buffer of its own, entirely dependent on the cash-credit facility renewing on demand |

## B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 6 | Point-in-time recognition, no channel-stuffing/bill-and-hold language in the accounting policy or notes; but the AR's own Directors' Report headline growth claim (Finding 1) is materially misleading on the same revenue figures |
| Expense capitalisation honesty | 7 | No aggressive capitalisation found; bearer-plants pre-operative pool (Note 45) is a legitimate agri-accounting practice, though the balance is growing with zero capitalisation this year, a forward watch item; no capitalisation threshold disclosed (gap, not a red flag) |
| Provisioning adequacy | 4 | Rs 483.09 lakh un-provisioned bad-debt charge bypassing the ECL lifecycle (Finding 9); DTA increasingly loss-carry-forward dependent (96.5%) even as the reversal on the standalone side was total and immediate (Finding 7); gratuity actuarial assumptions moved favourably in the same cost-cutting year (Pass 1, immaterial rupee impact) |
| RPT fairness | 5 | Rates disclosed (10% on related-party loans, market-rate-adjacent); but four separate promoter-controlled entities collect lease rent simultaneously with no independent valuation disclosed, and the Rs 114.50cr guarantee plus Rs 9.33cr loan structure concentrates risk without an arm's-length third party in the chain |
| Disclosure transparency | 3 | Directors' Report headline error (Finding 1) is a first-order transparency failure; Note 1 Corporate Information still describes a business that no longer exists; no Ind AS 105 restatement despite management's own "discontinued" language; auditor's report carries internal duplication/drafting errors (Finding 14) |
| Consistency with prior years | 6 | Note 30 Other Expenses is genuinely stable and consistent across three years (no reclassification, contrary to the injected prior); actuarial and warrant mechanics are traceable year to year; but the Directors' Report broke from its own FY2025 AR's correct prior-year presentation |
| **OVERALL** | **4** | Weighted toward disclosure transparency and provisioning, the two weakest dimensions; the underlying audited notes (Note 30, Note 25/26, Note 8, Note 39) are internally consistent and well-anchored, but the AR's own headline narrative (Directors' Report) and audit report drafting quality both show real defects that a reader relying on summary tables rather than primary notes would miss |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Holding-company guarantee (Rs 114.50cr) called against near-zero Group cash (Rs 7.78 lakh) | HIGH | Subsidiary's covenant compliance and cash-credit renewal (69.8% of debt is on-demand); any bank communication on the guarantee | Any quarter the wine subsidiary misses a covenant or the cash-credit facility is not renewed |
| DTA (96.5% loss-carry-forward-based) not realised if losses continue a third year | HIGH | FY27 PAT trajectory against the guided breakeven; further DTA reversals in the FY27 AR | FY27 annual results (management guides PAT breakeven) |
| Un-provisioned Rs 483.09 lakh bad-debt pattern repeating | MEDIUM-HIGH | FY27 receivables ageing and any further "written off with zero prior provision" line in Note 30 | Q4FY27/FY27 AR |
| Rising leverage (88.0% gearing) against negative EBITDA and floating-rate, on-demand debt | HIGH | Bank renewal terms, any covenant renegotiation, interest cost trend | Ongoing; acute if a lender does not renew the cash-credit line |
| Contingent liabilities growing (Rs 37.88cr, 27.9% of net worth), Section 270 misreporting penalty (Rs 6.63cr) unresolved | MEDIUM | CIT(Appeals) outcome on the Section 270 order and the two Maharashtra F-Form demands (Rs 17.96cr) | Whenever the respective appellate authorities rule |
| MSME payment discipline deteriorating (dues tripled, interest 20x) | LOW-MEDIUM | FY27 MSME ageing and interest-accrued figures in Note 40 | FY27 AR |
| Directors' Report headline figures not cross-checked against audited notes by a casual reader | MEDIUM (governance/transparency, not cash) | Whether the FY27 Directors' Report repeats the same comparator error | FY27 AR publication |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. Why does the Directors' Report "Consolidated FY 2024-25" comparator in the Key Financial Highlights table (Rs 17,844.09 lakh revenue, Rs 1,283.82 lakh loss) not match the audited consolidated P&L FY25 comparative (Rs 30,209.66 lakh revenue, Rs 1,706.26 lakh loss) presented later in the same annual report, and will the FY27 Directors' Report state the correct consolidated comparator?
2. What drove the Rs 733.86 lakh gross bad-debt write-off in FY26, of which Rs 483.09 lakh had no prior ECL provision, and is it linked to the customer whose revenue contribution fell from 17.3% to 11.6% in the same year?
3. Does the going-concern assessment (Note 39/44) factor in the Rs 114.50 cr corporate guarantee to the subsidiary's bankers against a standalone cash balance of Rs 9.24 lakh and consolidated cash of Rs 7.78 lakh, and what is the contingency plan if the guarantee is called?
4. Who are the other allottees of the 23-Aug-2024 promoter warrant issue whose 3,63,150 warrants (65.1% of the issue) lapsed, given the five named related parties converted their entire allotments?
5. What is the current status and expected resolution of the Rs 663.03 lakh Section 270 misreporting-of-income penalty order for AY 2018-19, and does management's "does not expect any liability" assessment rest on independent counsel's opinion?

## E. NOTES-BASED RED FLAGS

- Directors' Report consolidated FY25 comparator (revenue and loss) does not match the audited consolidated P&L FY25 comparative in the same annual report; the true YoY consolidated revenue movement is a 40.0% decline, not the reported 1.59% growth.
- Rs 483.09 lakh of FY26 bad-debt write-off went direct to P&L with zero prior provisioning, bypassing the normal ECL lifecycle.
- Promoter warrant forfeiture rate is 65.1%, not the 39.5% previously assumed; unnamed (non-KMP) allottees account for the entire lapse.
- Going-concern assessment (standalone and consolidated) does not address the Rs 114.50 cr guarantee against near-zero holding-company (Rs 9.24 lakh) and Group (Rs 7.78 lakh) cash.
- Rs 663.03 lakh Section 270 "misreporting of income" penalty order (AY 2018-19), not separately named until this stage.
- Holding-company DTA of Rs 3.53 cr reversed to Nil in full this year, a specific and more pessimistic admission than the going-concern note's "exploring new business opportunities" language in the same document.
- Consolidated auditor's report duplicates its Emphasis of Matter verbatim under Key Audit Matters and mistakenly carries standalone-opinion language into the consolidated opinion; the standalone opinion states no KAMs for the identical underlying fact.
- No Ind AS 105 discontinued-operations restatement exists despite management's own language elsewhere in the AR calling the agro/steel business "discontinued"; Note 1 Corporate Information is not updated for the wine-only reality.

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate-to-concerning accounting practices, clean at the
audited-note level (Note 30, Note 25/26, Note 8 are internally consistent
and well-disclosed) but let down by the surrounding annual report. Key
concern: the Directors' Report misstates the consolidated FY25 comparator,
making the headline growth claim false, while the going-concern note is
silent on a Rs 114.50 cr guarantee against near-zero Group cash. Key
strength: the audited notes themselves (Other Expenses, DTA components,
contingent liability arithmetic, share capital roll-forward) are internally
consistent and traceable, and the injected "reclassification" and "39.5%
forfeiture" priors were both correctable on source rather than genuine
company obfuscation. Overall accounting quality: 4/10.
