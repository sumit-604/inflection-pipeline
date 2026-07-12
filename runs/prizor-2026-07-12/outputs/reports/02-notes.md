# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3 (PATTERN PASS + CONSOLIDATION)
Company: Prizor Viztech Limited (PRIZOR) | FY 2024-25 Annual Report (8th AR)
Run date: 2026-07-12 | Sources: Pass 1 (02-notes-pass1.md), Pass 2 (02-notes-pass2.md), and a
final pattern re-read of runs/prizor-2026-07-12/inputs/_textcache/Annual_Report_2025.txt
(figures in ₹ Crore, converted from "₹ In Thousands" ÷10,000, per stage convention).

═══════════════════════════════════════════════════════════════
PASS 3 — PATTERN RE-READ FINDINGS
═══════════════════════════════════════════════════════════════

Reading for contradictions between notes, notes-vs-primary-statement mismatches, deliberately
thin disclosure next to detailed disclosure, restatements, subsequent events, and going-concern
language. This pass is NOT empty: it resolves the loan-to-equity/securities-premium/bonus-issue
sequencing question Pass 2 raised as an open item, and corrects one arithmetic characterisation
carried in Pass 1.

--- PATTERN FINDING 1: FULL RECONSTRUCTION OF THE PRE-IPO CAPITAL SEQUENCE (resolves Pass 2's
open flag on Notes 3/4/31) ---

Reading Note 3 (Share Capital, p.79), Note 4 (Reserves & Surplus, p.79) and Note 31 (RPT, p.87-88)
together, in date order, the full pre-IPO capital-restructuring sequence reconciles exactly:

1. Opening base (pre-FY25): 8,00,000 equity shares.
2. 07-May-2024 — Loan-to-equity conversion (Note 3(i), p.79): 4,00,000 shares issued at ₹75/share
   (₹10 face + ₹65 premium) = ₹3.00 Cr, "by way of Conversion of Loans into equity," per
   shareholder resolution. This creates Securities Premium of ₹2.60 Cr (4,00,000 × ₹65) — the
   exact "Add: Security Premium From Conversion of Loan to Share Capital" line in Note 4.
   Running base: 8,00,000 + 4,00,000 = 12,00,000 shares.
3. 09-May-2024 — Bonus issue (Note 3.1, p.79; Note 4, p.79), two days later: 66,00,003 shares
   issued. 66,00,000 = 12,00,000 × 5.5 — i.e. the bonus ratio is 5.5:1 on the POST-CONVERSION
   base of 12,00,000 shares (the 3-share residual is immaterial, likely a rounding/fractional-
   entitlement adjustment). Funded by capitalising ₹4.000003 Cr from Reserves & Surplus (Note 4;
   confirmed by Pass 2's unit-error correction, R&S closing reconciliation ties exactly) plus
   ₹2.60 Cr from Securities Premium — the identical amount created two days earlier by the loan
   conversion. ₹4.000003 Cr + ₹2.60 Cr = ₹6.600003 Cr = 66,00,003 shares × ₹10 face value. Exact
   match.
   Running base: 12,00,000 + 66,00,003 = 78,00,003 shares.
4. July 2024 — IPO (Note 3, Note 49, p.79/91): 28,91,200 shares at ₹87/share (₹10 face + ₹77
   premium) = ₹25.1534 Cr.
   Final base: 78,00,003 + 28,91,200 = 1,06,91,203 shares — matches Note 3's closing balance
   exactly.

CORRECTION TO PASS 1: Pass 1 (Section 12, "Share capital changes") characterised the bonus issue
as "roughly 8.25:1 on the pre-bonus 8,00,000 base." That arithmetic (66,00,003/8,00,000 = 8.25)
is numerically valid but uses the WRONG base — it ignores that the loan-to-equity conversion had
already lifted the share count to 12,00,000 two days before the bonus issue. The bonus was
actually struck at 5.5:1 on the 12,00,000-share post-conversion base. This is a corrected
characterisation, not a new number; both the ₹4.00 Cr (Pass 2's correction) and the 5.5:1 ratio
(this pass's correction) should be carried forward together into any downstream synthesis that
discusses the pre-IPO capital structure. 🟡 Watch (correction).

WHAT REMAINS UNRESOLVED (elevates Pass 2 Finding 2 to a top-tier red flag here): the sequence
above is arithmetically airtight on the SHARE and RESERVES side, but the identity of the lender
whose ₹3.00 Cr loan was converted into equity on 07-May-2024 still cannot be established from any
note. Note 31's RPT tables account for the two director loan accounts in FULL via cash
transactions alone (net repayment of ₹2.2306 Cr, matching the combined balance movement exactly,
per Pass 2 Finding 2) — leaving zero room for an equity-conversion component in either director's
account. The only other related party named anywhere in the notes, "Prizor Snacks Private
Limited" (Group Company, Note 31(i)), appears in NO transaction or balance line in either year, in
either note set — it cannot be confirmed OR ruled out as the converted-loan counterparty from the
disclosures given. This means a party received ₹3.00 Cr of pre-IPO equity (at a valuation two days
before an 5.5:1 bonus issue and ~10 weeks before a listing at nearly 9x that price) whose identity,
relationship to the company, and original loan terms are entirely absent from the notes. 🔴 Red
Flag — elevated from Pass 2's framing given the pattern-pass confirms there is no disclosure path
left unexamined; this is a genuine, closed gap that only a direct management question can resolve.

--- PATTERN FINDING 2: NOTE 42 (SECURITY) vs CARO ANNEXURE A PARA 2(b) — CONFIRMED AS A
DISCLOSURE-CONSISTENCY ITEM, NOT A CONTRADICTION ---

Revisiting Pass 1's flag on Note 42 (bank borrowings secured by inventory, quarterly stock
statements filed) against CARO Annexure A para 2(b) ("not sanctioned working capital limits in
excess of five crore rupees... provisions... not applicable"): on a pattern re-read, both
statements CAN be true simultaneously — the total secured borrowing base (Note 5 + Note 8 secured-
from-banks lines: ₹2.1800 Cr long-term + a portion of ₹2.2439 Cr short-term loan-repayable-on-
demand) does not obviously exceed ₹5 Cr in either year, so the quarterly-filing practice in Note 42
is plausibly a facility-level covenant rather than a CARO-threshold trigger. Downgraded from an
open contradiction to a confirmed non-contradiction requiring no further flag, though the notes
still do not disclose the exact secured borrowing amount separately from the total, so this cannot
be verified to the rupee. 🟢 Resolved (no red flag).

--- PATTERN FINDING 3: NO RESTATEMENTS, NO SUBSEQUENT EVENTS, NO GOING-CONCERN LANGUAGE ---

- Restatements/reclassifications: searched both note sets and the primary statements for
  "restated," "reclassified," "regrouped," "previous year figures have been" — NOT FOUND IN
  DOCUMENT. Only one AR is available for this exercise so a prior-year note set cannot be
  independently cross-checked, but nothing in the current AR's own text signals a restatement.
- Events after the balance sheet date: confirmed again on this pass — NOT FOUND IN DOCUMENT, no
  captioned note exists in either note set (consistent with Pass 1).
- Going concern: confirmed again — no going-concern qualifying language anywhere in the notes;
  auditor's report and CARO para 19 both affirm no material uncertainty. NONE.

--- PATTERN FINDING 4: DELIBERATE-VAGUENESS CHECK ACROSS ALL NOTES ---

Comparing disclosure density note-by-note: the RPT note (31), PPE note (12), and inventory note
(16) are all granular and specific. By contrast, three notes stand out as conspicuously thin
relative to their financial significance: Note 49 (IPO fund utilisation — generic "used for the
purpose for which it was raised," no object-wise table, against ₹25.15 Cr raised); Note 2(f)
impairment and Note 2(m) employee benefits (both boilerplate with zero company-specific
assumptions, against a ₹10.46 Cr gross PPE base and a now-derecognised gratuity provision
respectively); and the absence of any Capital Commitments note despite an active capex pipeline
(Note 19's ₹1.1567 Cr plant & machinery advance, Note 39's ₹1.8634 Cr CWIP). All three were
already surfaced individually in Passes 1-2; the pattern read confirms they form a genuine cluster
of disclosure thinness concentrated exactly where the company raised and is deploying the most
capital (IPO proceeds, PPE/capex), rather than being randomly distributed across routine notes.
🟡 Watch, consolidated.

END OF PASS 3 PATTERN RE-READ.

═══════════════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Operating cash flow negative in both FY24 (₹-1.82 Cr) and FY25 (₹-14.10 Cr) despite PAT growth (₹5.52 Cr → ₹10.15 Cr); cash conversion -33% then -139%; entirely IPO-funded (Financing Activities +₹22.64 Cr) | Cash Flow Stmt (p.73), cross-ref Notes 16/17/9 | 🔴 Red Flag | Reported profit is not converting to cash at all; the business is currently dependent on one-time IPO proceeds to fund operations, not organic cash generation |
| 2 | ₹3.00 Cr loan-to-equity conversion (Note 3, 4,00,000 shares at ₹75, 07-May-2024) cannot be reconciled to any named lender; director loan account (Note 31) fully explained by cash alone; sole other named related party (Prizor Snacks Pvt Ltd) has zero transactions in either year | Note 3, Note 31 | 🔴 Red Flag | A party received pre-IPO equity at a fraction of the IPO price nine days before a 5.5:1 bonus issue; identity, relationship, and original loan terms are undisclosed — a governance and disclosure gap, not just an accounting one |
| 3 | Finished-goods inventory +281.7% YoY vs revenue +99.4% YoY; inventory turnover fell 4.19x → 3.32x, under a delivery-triggered revenue-recognition policy | Note 16, Note 2(l), Note 32 | 🔴 Red Flag | Inventory building far ahead of sales raises a legitimate sell-in vs. sell-through question in the IPO year; risk of future write-down if the build does not convert |
| 4 | Related-party revenue (Om Security Solutions, Relative-of-Director entity) was ₹3.55 Cr / 9.95% of FY24 revenue, and fell to zero in FY25, the IPO year, with no explanation | Note 31(ii) | 🔴 Red Flag | Pre-IPO related-party revenue reliance that vanished exactly at listing is a classic pattern warranting direct scrutiny of FY24 revenue quality |
| 5 | Pre-IPO capital sequence (loan conversion → bonus issue → IPO) reconciles exactly on shares/reserves; corrected bonus ratio is 5.5:1 on the post-conversion 12,00,000-share base (not 8.25:1 on the pre-conversion base as Pass 1 first computed) | Note 3, Note 4 | 🟡 Watch (correction) | Mechanically clean once correctly sequenced, but the sequencing itself (create premium via conversion, consume it for bonus two days later) is nowhere narrated and only visible by reading three notes together |
| 6 | Gratuity Provision (₹0.0978 Cr) derecognised to NIL in FY25 with zero disclosure of cause; cash-flow placement (within working-capital changes) suggests a cash payout rather than an actuarial reversal, but no actuarial assumptions are disclosed in either year; forms a 3-line benefit-derecognition cluster with Director's Insurance (₹0.10 Cr) and Bonus & Incentive (₹0.0073 Cr), both also to NIL | Note 7, Note 2(m), Note 26 | 🟡 Watch (softened from 🔴 in Pass 1) | A cluster of simultaneous benefit-line disappearances with no disclosed cause is a governance/disclosure concern even if the cash-flow mechanics point to a mundane explanation |
| 7 | Business-model shift from manufacturing to trading: Cost of Material Consumed -68.7% (₹17.68 Cr → ₹5.53 Cr) while Purchases of Stock-in-Trade +434% (₹11.77 Cr → ₹62.83 Cr); net margin compressed 15.47% → 14.27% | Note 23, Note 24, Note 32 | 🟡 Watch | Structural change toward a lower-differentiation, lower-margin revenue mix; directly relevant to any quality-of-earnings and moat assessment downstream |
| 8 | No customer-concentration disclosure exists despite receivables and revenue both roughly doubling; no product/geography segment disaggregation despite a new export line (₹0.2494 Cr) and new import dependency (₹1.1118 Cr, 20.2% of raw-material consumption) | Notes 21, 34, 35, 52 | 🟡 Watch | Investors cannot assess customer or product concentration risk from the disclosures given, despite clear underlying business change (new export/import exposure) |
| 9 | Non-audit "Professional Services" fees to the statutory auditor rose from NIL to ₹0.3796 Cr (~19x the ₹0.0200 Cr audit fee) in the IPO year, with no description of services rendered | Note 30 | 🟡 Watch | Scale of non-audit fees relative to audit fee warrants a direct question on auditor-independence safeguards |
| 10 | No deferred-tax component breakdown or effective-vs-statutory tax rate reconciliation disclosed in either year, despite a swing from net DTA (₹0.0553 Cr, FY24) to net DTL (₹0.0532 Cr, FY25) | Note 6, Note 14 | 🟡 Watch | Cannot independently assess DTA realism or the tax-rate composition |
| 11 | Note 32's own ratios show Current Ratio 5.08x (FY25) — a balance sheet overcapitalised with IPO cash, not organic liquidity; FY24's Return on Equity 141% and ROCE 70% are base-effect artefacts of a near-nil pre-IPO equity base, not operating-economics signals | Note 32 | 🟡 Watch | Flags for downstream valuation/synthesis stages that FY24 ROE/ROCE must not be used as like-for-like inputs without adjustment |
| 12 | Total Other Expenses +205% YoY (vs +99.4% revenue growth); two new compliance-friction lines (GST interest/late fees + income-tax interest, ₹0.2948 Cr combined) appear for the first time in the IPO year | Note 28 | 🟡 Watch | Rate of cost growth outpacing revenue, plus new statutory-payment friction, both worth monitoring into FY26 |
| 13 | No Capital Commitments note exists anywhere in either note set despite a clear open capex pipeline (₹1.1567 Cr new advance for plant & machinery, Note 19; ₹1.8634 Cr CWIP, Note 39; ₹8.28 Cr FY25 PPE additions, Note 12) | Note 19, Note 12, Note 39 | 🟡 Watch | Standard Schedule III disclosure gap for a company mid-capex-cycle; limits forward capex-commitment visibility |
| 14 | Finance Costs nearly doubled (+91.9%, ₹0.65 Cr → ₹1.24 Cr) despite period-end borrowings falling (LT -4.3%, ST -40.9%), consistent with higher average debt carried through the ~4 pre-IPO months of FY25 | Note 27 | 🟡 Watch | Corroborates the pre-IPO cash squeeze already evidenced in the Cash Flow Statement; a real P&L cost of the working-capital build ahead of IPO proceeds landing |
| 15 | IPO fund utilisation disclosed only as a generic statement ("used for the purpose for which it has been raised"), no object-wise itemised table against the stated IPO objects | Note 49 | 🟡 Watch | Cannot independently verify fund application against issue objects from the notes alone |

## B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 5 | Policy itself (delivery-triggered) is standard and not overtly aggressive on its face (Note 2(l)), but the +281.7% finished-goods build against +99.4% revenue growth (Note 16) and the vanishing related-party revenue stream (Note 31) both raise unresolved quality-of-revenue questions this pass could not close from disclosures alone |
| Expense capitalisation honesty | 7 | PPE/CWIP additions are well-documented and reconcile cleanly (Note 12, Note 39), no revaluation (Note 38), no exceptional/extraordinary items in either year to mask through capitalisation |
| Provisioning adequacy | 4 | Gratuity provision derecognised with zero disclosed cause; no warranty provision for a hardware seller; no capital commitments note; no litigation/onerous-contract provisions (all consistent with NIL contingent liabilities, but unverifiable) |
| RPT fairness | 3 | Unidentified ₹3.00 Cr loan-to-equity conversion counterparty; Om Security Solutions revenue reversal to zero in the IPO year; director loans carry no disclosed interest terms |
| Disclosure transparency | 4 | Extensive list of "NOT FOUND IN DOCUMENT" items — no borrowing rate/covenant/maturity table, no customer concentration, no segment disaggregation, no actuarial assumptions, no tax-rate reconciliation, no capital commitments, generic IPO fund-utilisation statement |
| Consistency with prior years | 5 | Only one AR available so true consistency cannot be tested against a prior note set; the underlying business itself shifted materially (manufacturing to trading) within the single year observed, which is disclosed but not narrated as a strategic change anywhere in the notes |
| **OVERALL** | **4** | Multiple unresolved red flags (cash conversion, inventory build, RPT revenue reversal, unidentified equity counterparty) concentrated in exactly the areas (cash, related parties, capital structure) that matter most for a first-year-listed small-cap; disclosure gaps are pervasive even where no wrongdoing is evidenced |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Unidentified pre-IPO equity counterparty (₹3.00 Cr loan conversion) | High | Any FY26 AR disclosure naming the converted-loan lender; SEBI/exchange scrutiny of pre-IPO allotments; RPT note additions | Could surface at any regulatory review of the IPO period, or at FY26 AR if disclosure improves |
| Cash burn / working-capital squeeze funded by one-time IPO proceeds | High | FY26 CFO trend, receivables/inventory days, any fresh external funding need | Within 12-18 months if the current ~5.08x Current Ratio cushion is consumed by continued negative CFO |
| Inventory built far ahead of demand (+281.7% vs +99.4% revenue) | Medium-High | FY26 revenue growth vs inventory growth; any write-down/obsolescence provision appearing | At FY26 year-end if the inventory build does not convert to sales |
| Related-party revenue reversal (Om Security Solutions) in the IPO year | Medium | Any reappearance of related-party sales; customer-concentration disclosure in future filings | Relevant now, for FY24 revenue-quality assessment, and at each future RPT note |
| Provisioning/disclosure thinness (gratuity, warranty, capital commitments, tax reconciliation) | Medium | Whether FY26 notes close these gaps or new provisions appear | Ongoing, cumulative governance signal rather than a single event |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. Who was the lender in the ₹3.00 crore loan-to-equity conversion (Note 3, 4,00,000 shares at
   ₹75, resolution dated 07-May-2024), on what original terms (rate, tenure, arm's-length basis),
   and why does this conversion not appear as a movement in the only loan account the notes
   disclose (director loans, Note 31)?
2. What caused related-party revenue from Om Security Solutions (₹3.55 crore, 9.95% of FY24
   revenue) to fall to zero in FY25, the IPO year, and was there any change in the commercial
   relationship, ownership, or classification of this counterparty?
3. What explains finished-goods inventory growing 281.7% against 99.4% revenue growth, and is any
   portion of this build unsold goods recorded ahead of dispatch under the company's stated
   delivery-triggered revenue recognition policy?
4. What triggered the simultaneous derecognition of the gratuity provision (₹0.0978 Cr),
   Director's Insurance (₹0.10 Cr) and Bonus & Incentive (₹0.0073 Cr) to NIL in FY25, and what
   actuarial assumptions (discount rate, salary escalation, attrition) underlie the gratuity
   valuation in either year?
5. What professional services (₹0.3796 crore, ~19x the statutory audit fee) were rendered by the
   statutory auditor in FY25, and what independence safeguards were applied given the scale of
   non-audit fees relative to the audit fee?

## E. NOTES-BASED RED FLAGS

- Earnings management / quality-of-revenue: finished-goods inventory growing nearly 3x faster
  than revenue under a delivery-triggered recognition policy (Note 16, Note 2(l)), combined with
  deeply negative operating cash flow in both years despite reported profit growth (Cash Flow
  Statement) — reported profit is not being validated by cash generation.
- Undisclosed related party / governance: ₹3.00 crore of pre-IPO equity issued to a counterparty
  whose identity cannot be established from any note, nine days before a 5.5:1 bonus issue and
  ~10 weeks before listing (Note 3, Note 31).
- Aggressive/undisclosed risk indicator: related-party revenue of 9.95% of FY24 revenue (Om
  Security Solutions) reversing to zero exactly in the IPO year, unexplained (Note 31).

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate to concerning accounting practices. Key concern: an unidentified
counterparty received pre-IPO equity nine days before a bonus issue while operating cash flow
stayed deeply negative through both years shown. Key strength: PPE, contingent-liability, and
trade-payable disclosures are clean, granular, and internally consistent with the primary
statements. Overall accounting quality: 4/10.

```yaml
stage: B02-notes
company: "PRIZOR"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
input_gaps: []
flags:
  - {type: FLAG-CASH, reason: "CFO negative both years and deteriorating sharply despite PAT growth (FY25 CFO -Rs14.10cr vs PAT +Rs10.15cr, cash conversion -139%; FY24 CFO -Rs1.82cr vs PAT +Rs5.52cr, -33%), driven by finished-goods inventory +281.7% YoY vs revenue +99.4% YoY and a simultaneous trade-payables squeeze; entirely IPO-funded, not organic (Cash Flow Statement p.73; Note 16 p.83; Note 32 p.89)"}
accounting_quality: 4        # /10
pass_2_empty: false
pass_3_empty: false
top_findings:                # max 15
  - {rank: 1, finding: "Operating cash flow negative both years despite PAT growth (FY25 CFO -Rs14.10cr vs PAT Rs10.15cr, -139% conversion; FY24 CFO -Rs1.82cr vs PAT Rs5.52cr, -33%), entirely IPO-funded", note_ref: "Cash Flow Stmt p.73; Notes 16/17/9", rating: "red_flag", why: "Reported profit is not converting to cash; business currently dependent on one-time IPO proceeds"}
  - {rank: 2, finding: "Rs3.00cr loan-to-equity conversion (07-May-2024) unreconciled to any named lender; director loan account fully explained by cash alone", note_ref: "Note 3, Note 31", rating: "red_flag", why: "Unidentified counterparty received pre-IPO equity nine days before a 5.5:1 bonus issue and ~10 weeks before listing"}
  - {rank: 3, finding: "Finished-goods inventory +281.7% YoY vs revenue +99.4% YoY; inventory turnover fell 4.19x to 3.32x", note_ref: "Note 16, Note 32", rating: "red_flag", why: "Inventory building far ahead of sales under a delivery-triggered revenue policy raises sell-in vs sell-through question"}
  - {rank: 4, finding: "Related-party revenue (Om Security Solutions) was 9.95% of FY24 revenue (Rs3.55cr) and fell to zero in FY25, the IPO year, unexplained", note_ref: "Note 31(ii)", rating: "red_flag", why: "Pre-IPO related-party revenue reliance vanished exactly at listing"}
  - {rank: 5, finding: "Pre-IPO capital sequence (loan conversion then bonus issue then IPO) reconciles exactly on shares/reserves; correct bonus ratio is 5.5:1 on the post-conversion 12,00,000-share base, not 8.25:1 on the pre-conversion base", note_ref: "Note 3, Note 4", rating: "watch", why: "Mechanically clean once correctly sequenced but the sequencing itself is nowhere narrated"}
  - {rank: 6, finding: "Gratuity Provision Rs0.0978cr derecognised to NIL in FY25 with no disclosure; forms a 3-line benefit-derecognition cluster with Director's Insurance and Bonus & Incentive, both also to NIL; cash-flow placement suggests a payout not a reversal but no actuarial assumptions disclosed either year", note_ref: "Note 7, Note 2(m), Note 26", rating: "watch", why: "Cluster of simultaneous benefit-line disappearances with no disclosed cause"}
  - {rank: 7, finding: "Business-model shift manufacturing to trading: Cost of Material Consumed -68.7%, Purchases of Stock-in-Trade +434%, net margin 15.47% to 14.27%", note_ref: "Note 23, Note 24, Note 32", rating: "watch", why: "Structural shift toward lower-differentiation, lower-margin revenue mix"}
  - {rank: 8, finding: "No customer-concentration or segment/geography disaggregation disclosed despite revenue roughly doubling and new export/import exposure", note_ref: "Note 21, Note 34, Note 35, Note 52", rating: "watch", why: "Cannot assess customer or product concentration risk from disclosures given"}
  - {rank: 9, finding: "Non-audit Professional Services fees to statutory auditor rose NIL to Rs0.3796cr (~19x audit fee) with no description of services", note_ref: "Note 30", rating: "watch", why: "Scale of non-audit fees warrants an auditor-independence question"}
  - {rank: 10, finding: "No deferred-tax component breakdown or effective-vs-statutory rate reconciliation despite swing from net DTA (Rs0.0553cr) to net DTL (Rs0.0532cr)", note_ref: "Note 6, Note 14", rating: "watch", why: "Cannot independently assess DTA realism or tax-rate composition"}
  - {rank: 11, finding: "Current Ratio 5.08x reflects IPO cash overcapitalisation not organic liquidity; FY24 ROE 141% and ROCE 70% are base-effect artefacts of a near-nil pre-IPO equity base", note_ref: "Note 32", rating: "watch", why: "FY24 ROE/ROCE must not be used as like-for-like inputs downstream without adjustment"}
  - {rank: 12, finding: "Total Other Expenses +205% YoY vs revenue +99.4%; new GST/income-tax interest lines (Rs0.2948cr combined) appear first time in IPO year", note_ref: "Note 28", rating: "watch", why: "Cost growth outpacing revenue plus new statutory-payment friction"}
  - {rank: 13, finding: "No Capital Commitments note exists despite an open capex pipeline (Rs1.1567cr plant and machinery advance, Rs1.8634cr CWIP, Rs8.28cr FY25 PPE additions)", note_ref: "Note 19, Note 12, Note 39", rating: "watch", why: "Standard disclosure gap limiting forward capex-commitment visibility"}
  - {rank: 14, finding: "Finance Costs nearly doubled (+91.9%) despite falling period-end borrowings, consistent with higher average pre-IPO debt carrying costs", note_ref: "Note 27", rating: "watch", why: "Corroborates the pre-IPO cash squeeze evidenced in the Cash Flow Statement"}
  - {rank: 15, finding: "IPO fund utilisation disclosed only as a generic statement with no object-wise itemised table", note_ref: "Note 49", rating: "watch", why: "Cannot verify fund application against stated IPO objects from the notes alone"}
red_flags:
  - "Rs3.00cr loan-to-equity conversion (Note 3, 07-May-2024) unreconciled to any named lender; director loan account (Note 31) fully explained by cash alone, leaving the counterparty of a pre-IPO equity issuance unidentified"
  - "Operating cash flow negative both FY24 and FY25 despite PAT growth, cash conversion -139% FY25 / -33% FY24, funded entirely by IPO proceeds (Cash Flow Statement; Notes 16/17/9)"
  - "Finished-goods inventory +281.7% YoY vs revenue +99.4% YoY under a delivery-triggered revenue recognition policy, inventory turnover falling 4.19x to 3.32x (Note 16, Note 2(l), Note 32)"
  - "Related-party revenue (Om Security Solutions) was 9.95% of FY24 revenue and fell to zero in the IPO year with no explanation (Note 31)"
questions_for_mgmt:
  - "Who was the lender in the Rs3.00 crore loan-to-equity conversion (Note 3, 4,00,000 shares at Rs75, resolution dated 07-May-2024), on what original terms, and why does this not appear as a movement in the director loan account (Note 31)?"
  - "What caused related-party revenue from Om Security Solutions (Rs3.55cr, 9.95% of FY24 revenue) to fall to zero in FY25, the IPO year?"
  - "What explains finished-goods inventory growing 281.7% against 99.4% revenue growth, and is any of this build unsold goods recorded ahead of dispatch?"
  - "What triggered the simultaneous derecognition of the gratuity provision, Director's Insurance and Bonus & Incentive to NIL in FY25, and what actuarial assumptions underlie gratuity valuation in either year?"
  - "What professional services (Rs0.3796cr, ~19x the audit fee) were rendered by the statutory auditor in FY25, and what independence safeguards were applied?"
receivables_trend: "improving (ageing composition), stable (days outstanding): FY25 ageing is 95.0% <6mo / 4.97% in 6mo-1yr bucket (Rs14.9614cr / Rs0.7830cr of Rs15.7443cr total) vs FY24 which was 99.2% concentrated in the 6mo-1yr bucket (Rs7.9034cr of Rs7.9634cr total) with nothing <6mo; receivable days roughly flat at 80.8 (FY25) vs 81.5 (FY24); feeds FLAG-CASH context alongside the inventory and CFO findings (Note 17, Note 17.1/17.2, Note 32)"
restatements_found: []
going_concern_language: "NONE - no going-concern qualifying language in the notes; auditor's report and CARO para 19 both affirm no material uncertainty"
```
