# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 1 (FULL EXTRACTION)
Company: Fratelli Vineyards Ltd (FRATELLI) | Run date: 2026-09-07
Sources: Annual_Report_FY2026.pdf (consolidated + standalone notes, Notes 1-49
consolidated, Notes 1-44 standalone) and Annual_Report_FY2025.pdf (comparative
figures for FY2024, pre-reclassification schedules). All figures as extracted
from the .txt mirrors, cross-checked against page markers. Amounts are stated
in the AR's native unit, Rs lakhs, with the Rs crore conversion shown once per
figure (1 cr = 100 lakh).

NOTE ON LOAD-BEARING FACTS: the AR text does not contain the literal figures
quoted in some of the injected priors (e.g. "Rs 114.14 cr Other Expenses",
"Rs 7.53 cr FY25", "Rs 77.12 cr Selling and admin"). These do not appear
anywhere in either AR. My reading of the audited Note 30 (consolidated) /
Note 27 (standalone) "Other Expenses" schedule across FY2024-FY26 shows NO
reclassification between an "Other Expenses" and a "Selling and
Administrative" line — both years use a single "Other expense" line on the
face of the P&L, with "Selling, distribution & marketing expenses" as one
consistent sub-line inside it in all three years (FY24, FY25, FY26). This is
flagged explicitly below (Finding 2) as a correction to the injected prior,
not a confirmation of it.

═══════════════════════════════════════════════════════════
1. ACCOUNTING POLICIES & CHANGES
═══════════════════════════════════════════════════════════

- No policy changes with quantified P&L impact this year. Standard Ind AS
  policy set (2.1-2.25 consolidated / 2.1-2.24 standalone), unchanged
  presentation basis (Annual_Report_FY2026.pdf, p.148-160, Note 2). 🟢
- Revenue recognition: point-in-time on dispatch/delivery for goods; no
  aggressive bill-and-hold or channel-stuffing language found. Revenue is
  grossed up for excise duty then netted for discounts/schemes (Note 2.10,
  p.157; Note 23, p.176). 🟢
- Depreciation useful lives (Note 2.8, p.150-151): Building 30 yrs, Oak
  Barrels 5 yrs, Plant & Machinery 10-25 yrs, Bearer Plants over lease term.
  All within Schedule II norms; no acceleration or extension flagged. 🟢
- Capitalisation threshold: not separately disclosed as a rupee figure in
  the notes — NOT FOUND IN DOCUMENT.
- Impairment test assumptions (growth/discount rate): the accounting policy
  (Note 2.19 / "Impairment of non-financial assets") describes the
  methodology qualitatively only. No numeric discount rate or CGU cash-flow
  assumption is disclosed anywhere in the notes — NOT FOUND IN DOCUMENT. No
  impairment loss was recognised in FY26 or FY25 on PP&E/goodwill (there is
  no goodwill; the wine subsidiary was consolidated as a common-control
  pooling-of-interest, not a purchase, so no goodwill arises — Note 43,
  p.194-195). 🟢
- ECL matrix: simplified lifetime-ECL approach on trade receivables (Note
  2.18(d), p.153; Note 10, p.161-166). Movement in allowance shown; no
  numeric provision matrix (ageing-bucket % rates) is disclosed — NOT FOUND
  IN DOCUMENT, only the resulting allowance movement. 🟡
- Ind AS 116 leases: incremental borrowing rate / effective interest rate on
  lease liabilities is 10% for both years (Note 42(iii), p.196). ROU assets
  net Rs 1,480.38 lakh (Rs 14.80 cr) at FY26-end vs Rs 1,560.79 lakh (Rs
  15.61 cr) FY25-end (Note 3, p.160). Lease liability Rs 1,785.51 lakh (Rs
  17.86 cr) FY26 vs Rs 1,964.00 lakh (Rs 19.64 cr) FY25 (Note 18, p.169;
  Note 42, p.196). Leases run 3 months to 14 years, covering wineries,
  vineyards and agricultural land (Note 42, p.196). 🟢
- No first-time standard adoption in FY26. MCA amendments to Ind AS 1/7/107
  (supplier finance disclosures) evaluated, no impact (Note 2.25, p.159).
  Ind AS 118 (replaces Ind AS 1, effective FY28) and the Ind AS 1 covenant
  breach amendment (effective FY27) are pending, company "assessing impact"
  (Note 2.25, p.159). 🟢

═══════════════════════════════════════════════════════════
2. RELATED PARTY TRANSACTIONS — Note 33 (consolidated, p.178-182), Note 30
   (standalone, p.117-122)
═══════════════════════════════════════════════════════════

LOAD-BEARING FACT: gross margin / Other Expenses reclassification.

- FY26 raw material + packing material consumed (Note 25(a), consolidated,
  p.175): Rs 5,493.35 lakh (Rs 54.93 cr) — matches the injected prior's Rs
  54.98 cr closely (rounding).
- Change in inventories (Note 26, p.175): Rs (1,526.23) lakh, i.e. minus
  Rs 15.26 cr — matches the injected prior's "Rs 15.26 cr inventory change"
  exactly.
- Properly netted COGS for gross margin purposes = materials consumed
  (5,493.35) + purchase of stock-in-trade (4.52) + change in inventories
  (-1,526.23) = Rs 3,971.64 lakh (Rs 39.72 cr) against revenue from
  operations Rs 18,128.65 lakh (Rs 181.29 cr) (Note 23, p.176). Gross
  margin = (18,128.65 - 3,971.64) / 18,128.65 = 78.1%. THIS MATCHES
  management's claimed 77-80% gross margin once the inventory build is
  netted in. The injected prior's "70% before the inventory change" is an
  incomplete calculation (it omits netting the inventory increase against
  COGS); once corrected, there is no gross-margin discrepancy to explain. 🟢
  Correction to load-bearing fact.
- Other Expenses (Note 30 consolidated, p.176; Note 27 standalone, p.113,
  not applicable at standalone level since standalone has near-zero
  operations): FY26 Rs 8,569.34 lakh (Rs 85.69 cr) vs FY25 Rs 8,989.78 lakh
  (Rs 89.90 cr) vs FY24 Rs 8,563.03 lakh (Rs 85.63 cr per FY2025 AR
  comparative, p. Note 30). These three years show NO reclassification —
  same single "Other expense" line all three years, same sub-line
  structure. The injected prior's Rs 114.14 cr FY26 / Rs 7.53 cr FY25 /
  "Selling and admin blank" figures do NOT appear anywhere in either AR.
  🔴 FLAG: this appears to be an artefact of a third-party data source
  (e.g. a financial aggregator), not the audited AR. Analysts should
  discard those two figures; the audited Note 30 numbers above are the
  source of record.
- Advertising/sales/marketing named line: "Selling, distribution & marketing
  expenses" (a sub-line inside Other Expenses, consolidated): FY26 Rs
  4,213.94 lakh (Rs 42.14 cr), FY25 Rs 4,587.84 lakh (Rs 45.88 cr), FY24 Rs
  4,080.45 lakh (Rs 40.80 cr) (Note 30, p.176 FY26 AR; Note 30 FY2025 AR).
  As % of wine-segment revenue: FY26 42.14/181.20=23.3%; FY25
  45.88/178.44=25.7%. This is the correct "brand spend eats the margin"
  number — it sits BELOW the gross-margin line as an operating expense, so
  it does not affect the ~78% gross margin but explains why the operating
  result is a loss despite that gross margin: S&D/marketing (~23-26% of
  wine revenue) + employee costs (Note 27, ~19.4% of revenue) + finance
  cost (~7.3%) + depreciation (~4.9%) exceed the ~78% gross margin. 🟡
- RPT full table (consolidated, Note 33(B)(i), p.179-181): largest lines —
  Gaurav Sekhri (MD) loan received Rs 775.50 lakh / repaid Rs 589.00 lakh,
  interest on loan Rs 50.46 lakh (FY26); Puja Sekhri loan taken Rs 240.00
  lakh, remuneration Rs 115.96 lakh; Charme Di Secci Alessio E Secci Andrea
  SNC (wine consultancy) Rs 38.16 lakh; Alessio Secci consultancy Rs 58.03
  lakh; multiple promoter-family lease payments (Ran Vijay Farms & Developers
  Rs 30.17 lakh, Shivratna Agro Products Rs 41.54 lakh, Sanyuktarjun Agro
  Farms Rs 35.08 lakh, Shankarratna Agro Farms Rs 46.64 lakh — all promoter-
  controlled entities leasing land/assets to the Group). 🟡
- RPT as % of revenue: aggregate identifiable RPT expense lines (lease
  payments + consultancy + interest + remuneration, excluding loan
  principal flows) ≈ Rs 3-4 cr against Rs 181.29 cr revenue, roughly
  1.7-2.2%. Not large in isolation, but the promoter family collects lease
  rent from FOUR separate promoter-controlled entities simultaneously
  (Ran Vijay Farms, Shivratna Agro, Sanyuktarjun Agro, Shankarratna Agro) —
  worth checking these are at arm's length given no independent valuation
  is disclosed. 🟡
- Loans to promoter entities: Gaurav Sekhri unsecured borrowings
  OUTSTANDING (Group owes him) Rs 583.50 lakh FY26 vs Rs 397.00 lakh FY25;
  Sanyuktarjun Agro Farms Rs 150.00 lakh unsecured loan (Group owes them),
  all @10% p.a. (Note 17, p.170-171). These are loans FROM related parties
  TO the Group (director/promoter-entity funding), not loans out. 🟢 (funds
  flowing in from promoters, not extracted)
- NEW at standalone (holding company) level this year: Loan GIVEN by the
  holding company TO its wholly-owned subsidiary Fratelli Wines Pvt Ltd —
  Rs 932.50 lakh (Rs 9.33 cr), @10%, repayable on demand, "for working
  capital, capex and general corporate purposes" (Note 6, standalone,
  p.103-104; Note 30(B)(i), standalone, p.118, "Loan given 932.50"). Zero in
  FY25. 🟡
- NEW corporate guarantee: holding company gave a corporate guarantee to
  the bankers of Fratelli Wines Pvt Ltd of Rs 11,450.00 lakh (Rs 114.50 cr)
  outstanding at FY26-end, vs Nil at FY25-end (Note 42(a)(ii), standalone,
  p.129; Note 30(B)(i), standalone, p.118). This guarantee is Ind AS 109
  fair-valued at Rs 69.53 lakh and booked as a deemed additional investment
  in the subsidiary (Note 5, standalone, p.100). 🔴 FLAG: the holding
  company (net worth Rs 296.48 cr, near-zero own operations) now stands
  behind essentially ALL of the wine subsidiary's bank debt (subsidiary
  total borrowings per Note 17 consolidated = Rs 119.74 cr FY26). This
  concentrates all Group credit risk on the wine subsidiary's operating
  performance with the shell entity as guarantor of record.
- Investment in subsidiary (standalone Note 5, p.100): Rs 28,550.59 lakh
  (Rs 285.51 cr) at cost + Rs 69.53 lakh guarantee-fair-value add-on =
  Rs 28,620.12 lakh (Rs 286.20 cr) total — this is 96.5% of the holding
  company's total assets (Rs 29,785.62 lakh, standalone balance sheet). The
  holding company is, in substance, a single-asset holding vehicle. 🟡
- Outstanding related-party balances (Note 33(C), consolidated, p.181-182):
  Tinna Tradefin Ltd trade receivable Rs 386.04 lakh at FY25-end, reduced to
  Nil at FY26-end (collected or written off — see receivables section).
  Expense payables to multiple promoter-linked lessors running Rs 5-136
  lakh each, all small in absolute terms.
- No new related parties added this year beyond the existing promoter-family
  and consultancy network already disclosed in FY25. 🟢
- Key management personnel compensation (consolidated, Note 33(D), p.182):
  Rs 180.56 lakh FY26 vs Rs 172.36 lakh FY25 — modest 4.8% increase, no
  perquisites or long-term benefits disclosed separately (both Nil). 🟢

═══════════════════════════════════════════════════════════
3. CONTINGENT LIABILITIES — Note 39 (consolidated, p.190-193)
═══════════════════════════════════════════════════════════

- Total contingent liabilities (claims not acknowledged as debt): Rs
  3,787.90 lakh (Rs 37.88 cr) FY26 vs Rs 2,971.35 lakh (Rs 29.71 cr) FY25 —
  up 27.5% YoY. 🟡
- Composition FY26: Income Tax cases Rs 1,148.59 lakh (Rs 11.49 cr); GST
  cases Rs 732.85 lakh (Rs 7.33 cr); VAT/CST cases Rs 1,906.46 lakh
  (Rs 19.06 cr) — VAT/CST is now the largest bucket and grew from Rs
  1,154.70 lakh to Rs 1,906.46 lakh, +65% YoY, driven largely by two large
  new Maharashtra CST "F-Form disallowance" demands: FY20-21 Rs 956.87 lakh
  and FY21-22 Rs 839.31 lakh (Note 39(A)(xv)-(xvi), p.192). 🔴 FLAG: these
  two items alone total Rs 17.96 cr, are new/escalated this year, and
  management "does not expect any liability" on them without independent
  corroboration in the note.
- Total contingent liabilities as % of net worth: Rs 37.88 cr / Rs 135.96
  cr consolidated net worth (Note 38, Total Equity FY26) = 27.9%. No SINGLE
  item exceeds 10% of net worth individually (largest single item Rs 9.57
  cr F-Form case = 7.0% of net worth), but the VAT/CST bucket in aggregate
  (Rs 19.06 cr = 14.0% of net worth) is a genuine watch item. 🟡
- Multiple GST demand orders received through FY26 relating to input tax
  credit disputes across several states (Tamil Nadu, Panipat) — a pattern
  of recurring, geographically dispersed GST notices (Note 39(A)(v)-(xi),
  p.191-192), suggesting systemic compliance friction rather than one-off
  issues. 🟡
- No guarantees for subsidiaries disclosed as a CONTINGENT item in Note 39
  (the corporate guarantee to Fratelli Wines' bankers is instead booked as
  a financial guarantee / deemed investment, per Note 5 standalone — see
  Section 2 above, since it is intra-group and eliminates on consolidation).
- Capital commitments: Rs 1.36 lakh FY26 (plant & machinery) vs Rs 91.56
  lakh FY25 — commitments have collapsed 98.5%, consistent with capex
  slowdown (Note 39(B), p.193). 🟡

═══════════════════════════════════════════════════════════
4. TRADE RECEIVABLES — Note 10 (consolidated, p.161-167)
═══════════════════════════════════════════════════════════

LOAD-BEARING FACT: receivables at 212 days.

- Current trade receivables, net: Rs 10,511.14 lakh (Rs 105.11 cr) FY26 vs
  Rs 10,992.60 lakh (Rs 109.93 cr) FY25 — down 4.4% YoY, against revenue
  UP 1.6% (wine-only basis). Confirms the injected "~Rs 105 cr against
  Rs 181 cr sales" figure. 🟡 That computes to 212 days sales outstanding on
  FY26 revenue (105.11/181.29*365=211.6 days) — matches the injected prior
  precisely.
- Ageing schedule, FY26 (Note 10(a), p.162, current receivables, gross
  before ECL, "considered good" bucket): Unbilled Rs 4.21 lakh; Not due Rs
  3,917.81 lakh (37.3%); <6 months Rs 4,036.86 lakh (38.4%); 6mo-1yr Rs
  2,460.86 lakh (23.4%); 1-2yr Rs 91.40 lakh (0.9%); 2-3yr Nil; >3yr Nil.
  Total considered-good Rs 10,511.14 lakh.
- Ageing schedule, FY25 comparative: Not due Rs 3,462.65 lakh (31.5%);
  <6mo Rs 2,892.02 lakh (26.3%); 6mo-1yr Rs 4,489.16 lakh (40.8%); 1-2yr Rs
  116.46 lakh; 2-3yr Rs 4.25 lakh; >3yr Rs 28.06 lakh.
- >6 months as % of total (considered good): FY26 = (2,460.86+91.40)/
  10,511.14 = 24.3%. FY25 = (4,489.16+116.46+4.25+28.06)/10,992.60 = 42.2%.
  So the >6-month bucket has IMPROVED sharply (from 42.2% to 24.3%),
  though the "not due + <6mo" combined bucket (75.7% FY26) is still
  concentrated in the 6mo-1yr band rather than genuinely current — 23.4% of
  ALL receivables sit in the 6-12 month overdue band even in the "good"
  bucket. 🟡 Mixed signal: improving mix, but 212 days DSO on the total is
  still very long for a consumer beverage business.
- Credit-impaired receivables (separately disclosed, fully provided): Rs
  454.17 lakh FY26 (down from Rs 704.95 lakh FY25) current, plus Rs 153.86
  lakh non-current (flat both years, fully provided both years) (Note 10,
  p.161-163). Total gross credit-impaired = Rs 608.03 lakh FY26 vs Rs
  858.81 lakh FY25.
- ECL / impairment allowance movement (Note 10(b), p.163 and Note 36(C),
  p.186): Opening Rs 858.81 lakh (FY26) → Amount provided Rs Nil → Amount
  WRITTEN BACK Rs (250.77) lakh → Closing Rs 608.04 lakh. In FY25: Opening
  Rs 564.77 lakh → provided Rs 294.04 lakh → Closing Rs 858.81 lakh. 🔴
  FLAG: FY26 shows a Rs 250.77 lakh (Rs 2.51 cr) WRITE-BACK of previously
  provided doubtful debts with ZERO new provisioning, even though the P&L
  (Note 30, Other Expenses) separately shows "Bad debts and short
  recoveries" of Rs 733.86 lakh gross, netted against "provision adjusted
  out of above written off" of Rs (250.77) lakh, giving a net Rs 483.09
  lakh bad debt charge for FY26 (vs Rs 49.29 lakh FY25) — a nearly 10x
  jump in net bad debts actually written off/charged, even as the BALANCE
  SHEET provision itself shrank. This combination (large write-off flowing
  through P&L, provision balance falling, and simultaneous receivables
  ageing improvement) should be read together with the customer
  concentration finding below.
- Related-party receivables inside trade receivables: Rs Nil FY26 vs Rs
  386.04 lakh (Tinna Tradefin Ltd) FY25 (Note 10, footnote, p.162; Note
  33(C), p.181) — the FY25 related-party receivable was resolved to zero
  during FY26 (collected, or reclassified/written off — the notes do not
  separately break out which).
- Single customer concentration: "one customer" contributed Rs 2,103.64
  lakh (Rs 21.04 cr) of Group revenue in FY26 = 11.6% of total revenue,
  down from Rs 5,243.04 lakh (Rs 52.43 cr) = 17.3% of revenue in FY25
  (Note 37, Segment information, "Information about customers", p.188). 🟡
  Concentration has fallen sharply in absolute and relative terms — could
  reflect either genuine diversification or loss of a large customer;
  notes do not name the customer or explain the decline.
- Standalone level: Fratelli Wines Pvt Ltd (subsidiary) trade receivable
  from the holding company Rs 46.72 lakh FY26 (Nil FY25) — immaterial
  (standalone Note, p.114 area).

═══════════════════════════════════════════════════════════
5. INVENTORY — Note 9 (consolidated, p.161)
═══════════════════════════════════════════════════════════

- Category breakdown FY26 vs FY25 (Rs lakh): Raw materials 1,279.00 vs
  1,572.47 (-18.7%); Work-in-progress 7,309.83 vs 5,588.69 (+30.8%);
  Finished goods 806.99 vs 965.59 (-16.4%); Stock-in-trade 81.24 vs 117.55
  (-30.9%); Stores and spares 37.69 vs 5.89 (+540%, small base). Total
  9,514.75 vs 8,250.19, +15.3% (Note 9, p.161).
- Finished goods DECLINED 16.4% while revenue grew 1.6% (wine-only) —
  inventory is not building at the finished-goods (sellable) stage. 🟢
- Work-in-progress grew 30.8% and now represents 76.8% of total inventory
  (7,309.83/9,514.75) — this is consistent with wine's multi-year barrel-
  ageing production cycle (oak-barrel-aged wine sits in WIP for 1-3+ years
  before bottling), not necessarily a red flag for THIS industry, but it
  means inventory days are rising faster than sales and tie up a growing
  share of working capital. Inventory days (FY26, on Note 25(a)+26 COGS
  basis, Rs 39.72 cr) = 9,514.75/100 crore-equivalent... using COGS Rs
  39.72 cr: 95.15/39.72*365 = 874 days. This is extremely long, but is an
  artefact of wine barrel-ageing being classified as WIP inventory rather
  than a true liquidity concern comparable to a non-aged-goods business. 🟡
- Inventories are hypothecated to bankers against working capital limits
  (Note 9, footnote, p.161; cross-referenced to Note 17 borrowings
  security). 🟢
- No inventory write-downs disclosed with amounts, no obsolete-inventory
  disclosure found — NOT FOUND IN DOCUMENT (only the "lower of cost or NRV"
  boilerplate policy, Note 2.12, p.152).

═══════════════════════════════════════════════════════════
6. INVESTMENTS — Note 6 (consolidated, p.161-162), Note 5 (standalone,
   p.100)
═══════════════════════════════════════════════════════════

- Consolidated non-current investments: SVC Co-Operative Bank Ltd equity
  (unquoted, FVTPL), 50,000 shares, carrying value Rs 25.08 lakh FY26 vs
  Rs 5.05 lakh FY25 — a 5x fair-value gain (Note 6, p.161-162; also flows
  through Note 24 Other Income "Gain due to fair value of investments Rs
  20.03 lakh"). Small in absolute size but a 5x mark-up on a bank equity
  stake in one year deserves a sense-check on the valuation basis — NOT
  FOUND (no valuation technique disclosed beyond "Level 3" classification,
  Note 35, p.185). 🟡
- Only one subsidiary in the Group: Fratelli Wines Pvt Ltd, 100% owned
  (became wholly owned 22-Apr-2024, up from 3.04% previously) (Note 1,
  p.145; Note 43, p.194-195). No JVs, no associates, no other investees. 🟢
- Standalone investment in subsidiary at cost: Rs 28,550.59 lakh (Rs 285.51
  cr), unchanged in absolute cost FY26 vs FY25, plus Rs 69.53 lakh deemed
  investment from the corporate guarantee (Note 5, p.100) — see Section 2.
  No impairment recognised; management states it assessed future
  projections and found "no provision required" (Note 5, footnote, p.100) —
  a bare assertion with no supporting sensitivity or cash-flow disclosure.
  🟡
- No ICDs given by the Group to third parties. The one loan (holding
  company to subsidiary, Rs 932.50 lakh @10%, repayable on demand) is
  intra-group and eliminates on consolidation — see Section 2. 🟢
- Advances in the nature of loans to Mr. Alessio Secci (Rs 322.26 lakh
  outstanding FY25) and Mr. Giovano Masi (Rs 46.63 lakh outstanding FY25)
  were fully recovered during FY26 (Nil outstanding FY26) (Note 46,
  consolidated, p.199; Note 42(a)(i), standalone, p.129). These were
  advances to individuals who also appear as related parties (consultancy
  fee recipients) — the notes flag that TDS deposited in FY25 was
  "recovered" in FY26, an unusual structure for a simple advance. 🟡

═══════════════════════════════════════════════════════════
7. BORROWINGS — Note 17 (consolidated, p.167-171)
═══════════════════════════════════════════════════════════

- Total borrowings: Rs 11,973.57 lakh (Rs 119.74 cr) FY26 vs Rs 10,150.27
  lakh (Rs 101.50 cr) FY25, +18.0% YoY.
- Instrument mix FY26: Secured term loans from banks Rs 3,426.87 lakh
  (SVC Co-operative Bank, three tranches, all @10.25% p.a., 84 monthly
  instalments, secured on machinery & equipment); Vehicle loans Rs 187.55
  lakh (multiple lenders, 8-11% p.a.); Cash credit Rs 7,275.65 lakh (SVC
  Co-op Bank @9.75-10% and SBI @10.65%, secured by hypothecation of current
  assets, unconditionally guaranteed by the holding company); Unsecured
  loans Rs 1,083.50 lakh (from directors Rs 733.50 lakh @10%, Sanyuktarjun
  Agro Farms Rs 150 lakh, TCI India Rs 100 lakh, Bhoruka Express
  Consolidated Rs 100 lakh, all @10%, repayable on demand) (Note 17(a),
  p.168-170).
- No covenant breach or waiver disclosed — NOT FOUND / none flagged. "As on
  balance sheet date, there is no default in repayment of loans and
  interest" (Note 17, p.168). 🟢
- Fixed vs floating: Rs 1,271.05 lakh fixed / Rs 10,702.53 lakh
  variable-rate (Note 36(A)(i), p.183) — 89.4% of debt is floating-rate,
  meaningful interest-rate sensitivity (50bp move = Rs 53.51 lakh P&L
  impact).
- 5-year repayment schedule: undiscounted maturity table shows On-demand
  Rs 8,359.15 lakh; <1yr Rs 602.32 lakh; 1-3yr Rs 1,262.30 lakh; 3-5yr Rs
  1,141.41 lakh; >5yr Rs 650.48 lakh (Note 36(B), p.184) — the bulk of debt
  (69.8%) is technically repayable on demand (cash credit), a normal
  working-capital funding structure but a genuine refinancing-risk
  exposure if banking relationships sour.
- Related-party borrowings: Rs 883.50 lakh payable to related parties
  (directors/promoter entities) within the Rs 1,083.50 lakh unsecured
  loans, i.e. 81.5% of unsecured borrowings are from promoters/directors
  (Note 17, footnote, p.168; Note 33, p.180-182). 🟡
- Gearing ratio (Note 38, consolidated): 88.01% FY26 vs 64.61% FY25 —
  rising leverage as equity erodes from losses while debt grows. 🔴 FLAG.
- Current ratio (Note 36(B), p.184): 1.37 FY26 vs 1.69 FY25 — liquidity
  cushion thinning.
- Standalone level: holding company itself carries essentially no
  third-party bank debt of its own (its only debt-like exposure is the
  Rs 114.50 cr guarantee to the subsidiary's lenders) — its balance sheet
  is dominated by the investment in and loan to the subsidiary.

═══════════════════════════════════════════════════════════
8. TRADE PAYABLES — Note 19 (consolidated, p.171-172)
═══════════════════════════════════════════════════════════

- Total trade payables: Rs 2,707.59 lakh (Rs 27.08 cr) FY26 vs Rs 2,241.37
  lakh (Rs 22.41 cr) FY25, +20.8% YoY.
- MSME dues: Rs 93.27 lakh FY26 vs Rs 27.81 lakh FY25 — MORE THAN TRIPLED
  (+235%) (Note 19, p.171; Note 40 MSME details, p.172). Interest accrued
  and unpaid on MSME dues: Rs 2.14-2.24 lakh FY26 vs Rs 0.10 lakh FY25 — a
  20x increase in accrued MSME interest, meaning the company is now
  routinely paying MSME suppliers beyond the 45-day statutory limit where
  it was not doing so materially last year. 🔴 FLAG — small absolute rupee
  amount but a clear directional deterioration in payment discipline
  toward small suppliers, and a compliance/reputational exposure under the
  MSMED Act.
- Ageing: MSME dues 100% in the "<1 year" (i.e. not yet 1 year overdue)
  bucket both years — no MSME dues >1 year (Note 19, p.171-172). Non-MSME
  payables: Rs 2,328.93 lakh "not due/<1yr" + Rs 280.20 lakh "1-2yr" FY26
  (up from Rs 2,183.35 lakh + Rs 30.21 lakh FY25) — the 1-2yr bucket grew
  9.3x, a genuine stretching of payment terms with larger creditors. 🟡
- No disputed dues disclosed either MSME or non-MSME, either year.
- Payable days (on Note 25(a)+25(b) purchases basis, FY26 ≈ Rs 3,222 lakh
  raw material purchases + Rs 4.52 lakh stock-in-trade): trending up given
  payables +20.8% against purchases roughly flat/declining — consistent
  with the company stretching payables to manage a tightening cash
  position (corroborated by the current ratio decline in Section 7).
- Related-party payables inside trade payables: Rs 76.79 lakh both years
  (Puja Sekhri entity/consultancy) (Note 19, footnote, p.171; Note 33(C),
  p.182) — unchanged, not growing.

═══════════════════════════════════════════════════════════
9. PROVISIONS — Note 21 (consolidated, p.172), Note 41 (employee benefits,
   p.192-197)
═══════════════════════════════════════════════════════════

- Gratuity + leave encashment provisions: Rs 476.76 lakh total FY26
  (306.36+67.35+82.92+20.13) vs Rs 442.89 lakh FY25 — up 7.6%, broadly
  tracking headcount/wage growth. 🟢
- Gratuity defined benefit obligation (unfunded — "Fair value of plan
  assets at the end of the year: Nil" both years, Note 41(iii), p.193):
  DBO Rs 373.71 lakh FY26 vs Rs 348.69 lakh FY25. Actuarial assumptions:
  discount rate 6.9-7.75% FY26 (7.10-7.22% FY25); salary growth 7.00% FY26
  (9-10% FY25) — salary growth assumption CUT sharply (from 9-10% to 7%),
  which mechanically LOWERS the DBO / gratuity expense; withdrawal rate
  10-15% FY26 (15-33% FY25) — also cut. 🟡 FLAG: two separate actuarial
  assumptions moved favourably (lower salary growth, lower withdrawal
  rate) in the same year the company was cutting costs — worth checking
  these track an independent actuary's methodology change vs a
  management-favourable assumption shift, though the rupee impact
  (sensitivity table shows +/-0.5-1% moves shifting the liability by only
  Rs 17-21 lakh) is immaterial in absolute terms.
- No warranty provisions (not applicable to this business model), no
  decommissioning provisions, no onerous-contract provisions, no
  litigation provisions beyond the contingent liabilities in Note 39 (none
  of the disputed tax/GST/VAT matters have been PROVIDED for; all are
  disclosed as contingent only) — NOT FOUND / not applicable.
- Gratuity plan is fully unfunded (no plan assets) — a genuine, if common
  for Indian SMEs/mid-caps, liquidity exposure that crystallises only on
  employee exit events. 🟡

═══════════════════════════════════════════════════════════
10. DEFERRED TAX — Note 8 (consolidated, p.163-165), Note 8 (standalone)
═══════════════════════════════════════════════════════════

- Effective tax rate reconciliation (Note 31(a), consolidated, p.177):
  statutory rate 25.17% both years; FY26 effective tax rate = credit of Rs
  175.11 lakh against a pre-tax loss of Rs 2,666.30 lakh (i.e. a small NET
  TAX CREDIT despite a large loss, effective rate ~6.6% credit vs the
  25.17% statutory rate that would imply a much larger credit) — the gap is
  explained by "Deferred tax asset of holding company reversed during the
  year Rs 353.46 lakh" and "Deferred tax not created on current year losses
  of holding company Rs 137.28 lakh" (Note 31(a), p.177). 🔴 FLAG: the
  holding company REVERSED Rs 353.46 lakh of previously-recognised DTA
  (built up through FY25) because management now judges future taxable
  profits at the STANDALONE level are no longer probable — i.e. management
  itself does not expect the holding company (ex-wine-subsidiary) to
  generate taxable profits again. This is a direct, quantified admission
  inside the tax note that is more conservative than, and somewhat at odds
  with, the going-concern paragraph's "actively pursuing new business
  opportunities... will continue as a going concern" framing (Note 39,
  standalone, and Note 44, consolidated — see Pass 3 territory for
  contradiction flag).
- MAT credit: not separately disclosed as an asset — NOT FOUND IN DOCUMENT
  (no MAT credit entitlement line in the DTA reconciliation, Note 8(a),
  p.164).
- DTA realism: carried-forward business losses now form the LARGEST
  component of the recognised DTA — Rs 1,138.66 lakh FY26 (96.5% of the
  total net DTA of Rs 1,180.12 lakh) vs Rs 738.88 lakh FY25 (73.7% of a
  smaller Rs 1,001.99 lakh total) (Note 8, p.163-164). The DTA is
  increasingly a bet on FUTURE PROFITABILITY to absorb accumulated losses,
  concentrated risk given the Group posted a loss in both FY25 and FY26.
  🔴 FLAG.
- Unrecognised DTA: business losses/capital losses/unabsorbed depreciation
  NOT recognised, itemised by assessment year with expiry dates (Note
  8(b), p.164-165) — total unrecognised carry-forward items ≈ Rs 1,687.25
  lakh (summing the AY-wise table) for which "continued uncertainty
  regarding availability of sufficient future taxable profits" is the
  stated reason (Note 8(b), footnote, p.165). Consistent, conservative
  treatment on the UNRECOGNISED side even as the RECOGNISED DTA leans
  heavily on loss carry-forwards — an internally consistent but
  aggressive-adjacent position given losses in both of the last two years.

═══════════════════════════════════════════════════════════
11. REVENUE DETAILS — Note 23 (consolidated, p.176-177), Note 37 Segment
    information (consolidated, p.187-189)
═══════════════════════════════════════════════════════════

LOAD-BEARING FACT: the revenue basis / discontinued operations.

- Segment note (Note 37, p.187, consolidated FY26 AR) still names THREE
  reportable segments (Agro Commodities, Steel Abrasives, Wine
  manufacturing and sales) even though Agro Commodities and Steel
  Abrasives are now near-zero. FY26 segment revenue: Agro Commodities Rs
  67.83 lakh (0.37% of total); Steel Abrasives Rs Nil; Wine manufacturing
  and sales Rs 18,120.04 lakh (99.6% of gross segment revenue, before
  inter-segment elimination of Rs 59.22 lakh) — Total Rs 18,128.65 lakh.
  FY26 IS effectively wine-only. 🟢 confirms load-bearing fact.
- FY25 (per same Note 37, comparative column): Agro Commodities Rs
  12,138.87 lakh (40.2%); Steel Abrasives Rs 332.72 lakh (1.1%); Wine
  Rs 17,844.09 lakh (59.0%, after Rs 106.02 lakh inter-segment
  elimination) — Total Rs 30,209.66 lakh. FY25 was NOT wine-only; the
  legacy agri-trading book was still 40% of Group revenue for the FULL
  YEAR, even though Fratelli Wines became a 100% subsidiary on 22-Apr-2024
  (i.e., from the very start of FY25).
- FY24 (per Note 37, FY2025 AR comparative, p.187 of that AR): Agro
  Commodities Rs 19,417.11 lakh (43.1%); Steel Abrasives Rs 5,118.25 lakh
  (11.3%); Wine manufacturing and sales Rs 21,287.71 lakh (47.2%, after Rs
  715.59 lakh inter-segment elimination) — Total Rs 45,107.48 lakh. Net of
  excise duty (Rs 2,971.78 lakh), this reconciles to Rs 42,135.70 lakh (Rs
  421.36 cr), matching the injected prior's "Rs 421.35 cr" exactly — that
  figure is REVENUE FROM OPERATIONS NET OF EXCISE DUTY, not the gross
  segment total. The wine segment alone in FY24 was Rs 21,287.71 lakh
  (Rs 212.88 cr) — close to, but not identical to, the injected prior's
  "Rs 215.6 cr" (a ~1.3% variance, source of the small gap not identified
  in the notes; Rs 212.88 cr per Note 37 is the figure of record).
- CONCLUSION on load-bearing fact 1: only FY26 is genuinely wine-only.
  FY24 and FY25 both carry a materially sized legacy agro-commodity /
  steel-abrasives trading book (43-47% and 40-43% of consolidated revenue
  respectively). Any YoY or CAGR comparison spanning FY24-FY26 on total
  consolidated revenue is NOT like-for-like; only the WINE SEGMENT LINE
  (Rs 212.88 cr FY24 → Rs 178.44 cr FY25 → Rs 181.20 cr FY26) is
  comparable across all three years, and even the FY24→FY25 wine-segment
  drop (-16.2%) needs explaining (this pass did not find a specific cause
  disclosed in the Notes; NOT FOUND IN DOCUMENT — worth a management
  question).
- No formal Ind AS 105 "Discontinued Operations" note exists anywhere in
  either AR (consolidated or standalone) — searched, not found. The wind-
  down of the agro/steel trading business is NOT presented under Ind AS
  105 discontinued-operations classification (which would require
  restating prior-period P&L and a single "profit/loss from discontinued
  operations" line); instead it simply shows up as a shrinking segment
  within continuing operations across the segment note. 🔴 FLAG: this is a
  disclosure quality point — a business genuinely wound down (management's
  own Board's Report at p.11 area calls the agri-trading business
  "discontinued") is not accounted for under the specific Ind AS standard
  that governs discontinued operations, which would otherwise force
  cleaner like-for-like restated comparatives for readers. Also Note 1
  (Corporate Information, both standalone and consolidated) STILL
  describes the company as "primarily engaged in the trading of agro
  commodities... and steel abrasives" (Note 1, p.145 consolidated; p.89
  standalone) — stale/inconsistent with the wine-only FY26 economic
  reality and with the going-concern note's own language about "absence of
  major revenue-generating activities."
- Revenue by geography (Note 23(i), p.176): India Rs 17,160.56 lakh
  (98.2%), Outside India Rs 313.95 lakh (1.8%) FY26 — export book is
  minimal.
- Revenue recognition timing: 100% point-in-time (goods transferred at a
  point in time), no material contract-asset/contract-liability balances
  beyond a small "advance from customers" of Rs 91.98 lakh (Note 23(v),
  p.176). No unsatisfied performance obligations disclosed for future
  periods (consistent with point-in-time goods sales, no long-term service
  contracts).
- Top customer: 11.6% of FY26 revenue from a single customer, down from
  17.3% FY25 (see Section 4) — not separately named.
- Government grant (WIPS — Maharashtra Wine Industry Promotion Subsidy):
  VAT-refund-linked grant income Rs 654.15 lakh FY26 (3.6% of revenue) vs
  Rs 651.75 lakh FY25 (Note 7, p.161; Note 23, p.176) — a MATERIAL,
  RECURRING state-subsidy dependency embedded in "Other operating revenue."
  If this subsidy scheme were withdrawn or capped, revenue/margin would
  take a direct hit. 🟡 FLAG.

═══════════════════════════════════════════════════════════
12. OTHER CRITICAL NOTES
═══════════════════════════════════════════════════════════

- Exceptional items: none labelled "exceptional" in the P&L or notes this
  year — NOT FOUND / not applicable.
- Goodwill: none exists (common-control pooling of interests, Note 43,
  p.194-195, precludes goodwill recognition) — not applicable.
- Intangibles: only computer software, net carrying value Rs 4.69 lakh
  FY26 (Note 4, p.160) — immaterial.
- Capital commitments: Rs 1.36 lakh FY26 vs Rs 91.56 lakh FY25 (Note 39(B),
  p.193) — see Section 3, capex intentions have collapsed.
- Foreign currency exposure: minimal, net EUR/USD exposure of Rs (2.34)
  lakh FY26 (Note 36(A)(ii), p.183) — immaterial, no hedging programme
  disclosed (no derivatives held; "Group policy not to carry out any
  trading in derivative for speculative purposes," Note 36, p.183).
- Segment reporting: covered in Section 11.
- Basic vs diluted EPS: IDENTICAL both years, both entity levels — Rs
  (5.75) basic and diluted FY26 consolidated (Note 32, p.177); Rs (2.09)
  standalone (Note 29, p.114). "Potential equity shares were anti-dilutive
  ... hence ignored" (i.e., the outstanding share warrants would have been
  dilutive-reducing the loss per share, so were excluded per Ind AS 33
  rules for loss-making entities) — standard treatment, no gap. 🟢
- Events after balance sheet date: Note 49 (consolidated, p.199-200) and
  the standalone equivalent both state explicitly "there were no
  subsequent events to be recognized or reported" as of the sign-off date,
  30-May-2026. NOTE: this AR was adopted/signed 30-May-2026, which PRE-
  DATES the August-2026 promoter inter-se gift transfers referenced in the
  injected load-bearing fact 5 — those transfers, by construction, CANNOT
  appear in this AR and are NOT FOUND IN DOCUMENT. The most recent
  ownership data in this AR is the FY26 year-end (31-Mar-2026) promoter
  shareholding table (Note 15(g), p.166), which should be treated as the
  pre-transfer baseline for any later comparison.
- CSR: standalone Note 38 (p.129) — Company "does not fall under the
  ceiling limit" of Section 135, Rs Nil required/spent both years. At the
  Group/subsidiary level, CSR Expense of Rs 0.56 lakh FY26 (down from Rs
  19.32 lakh FY25, an 97% cut) appears inside consolidated Other Expenses
  (Note 30, p.176) — no dedicated CSR-required-vs-spent table is presented
  for the subsidiary in these consolidated notes — NOT FOUND IN DOCUMENT
  (whether the subsidiary itself crosses the Section 135 threshold and, if
  so, what its shortfall/carry-forward position is).
- ESOP: no employee stock option scheme disclosed anywhere in the notes —
  not applicable / NOT FOUND.
- Share capital changes (Note 15, consolidated, p.165-167): equity share
  capital grew from 4,32,77,894 shares (FY25 open... actually FY25 close)
  to 4,34,72,394 shares FY26-end, via conversion of 1,94,500 share
  warrants (Rs 437.63 lakh received). SEPARATELY, 3,63,150 warrants
  LAPSED/were FORFEITED (unexercised within the 18-month SEBI ICDR window
  that expired 22-Feb-2026); the forfeited upfront money (Rs 272.36 lakh)
  was transferred to Capital Reserve (Note 15(e)(ii), p.166; Note 16,
  p.167). 🟡 Promoter warrant holders let a meaningful chunk (39.5% of the
  5,57,650 warrants allotted Aug-2024) lapse rather than pay up the
  balance 75% (Rs 225 each) to convert — a soft signal on promoter
  conviction/liquidity at the Rs 300 issue price, worth a question.
- Direct debits/credits to reserves bypassing P&L: the Rs 272.36 lakh
  warrant forfeiture (credited straight to Capital Reserve, not P&L) and
  the entire capital-reserve balance of Rs (13,458.94) lakh — a NEGATIVE
  capital reserve arising from the FY25 common-control share-swap
  accounting (Note 16, p.167; Note 43, p.194-195, "Capital reserve arising
  on combination" = Rs (13,070.17) lakh negative) — is a large, negative,
  non-P&L equity item that materially depresses "Other Equity" (Rs
  9,249.12 lakh FY26 vs Rs 11,304.68 lakh FY25) without ever running
  through the income statement. This is standard pooling-of-interests
  mechanics (not a red flag in itself) but a significant, non-obvious
  driver of the equity walk that a reader must trace through Note 16 and
  Note 43 together to understand. 🟡
- Retained earnings closing balance is NEGATIVE Rs (2,749.64) lakh FY26,
  having swung from a positive Rs 1,105.36 lakh at 01-Apr-2024 to negative
  within two loss-making years (Note 16, p.167) — accumulated losses have
  now wiped out the opening retained earnings entirely.

═══════════════════════════════════════════════════════════
PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS
═══════════════════════════════════════════════════════════

1. 🔴 Only FY26 is a genuine wine-only year. FY24 (47% wine / 53% legacy
   agro+steel) and FY25 (59% wine / 41% legacy) both carry a material
   non-wine trading book (Note 37, Segment information, consolidated
   FY2026 AR p.187 and FY2025 AR p.187). No Ind AS 105 discontinued-
   operations restatement exists to make prior years comparable; Note 1
   Corporate Information is still not updated to describe the current
   business. Any FY24-FY26 growth/CAGR claim on total consolidated revenue
   is not like-for-like — only the wine segment line is comparable.

2. 🔴 The holding company gave a NEW Rs 114.50 cr corporate guarantee to
   the wine subsidiary's bankers in FY26 (from Nil in FY25), covering
   essentially all of the subsidiary's Rs 119.74 cr debt, and separately
   lent the subsidiary a new Rs 9.33 cr working-capital loan @10% (Note
   42(a), standalone, p.129; Note 6, standalone, p.103-104; Note 30(B)(i),
   standalone, p.118). The nominally "diversified" corporate structure now
   concentrates 100% of Group credit risk on one operating entity, with
   the shell parent as sole guarantor.

3. 🔴 The claimed "Other Expenses reclassification" (Rs 114.14 cr FY26 vs
   Rs 7.53 cr FY25) does NOT exist in either audited AR. The actual Note
   30 figures are Rs 85.69 cr (FY26), Rs 89.90 cr (FY25), Rs 85.63 cr
   (FY24) — stable, no reclassification. Properly netting the FY26
   inventory movement (Rs -15.26 cr) against materials consumed (Rs 54.93
   cr) gives a gross margin of 78.1%, matching management's 77-80% claim.
   This corrects, rather than confirms, the injected load-bearing fact.

4. 🔴 Deferred tax note (Note 8/31, consolidated, p.163-165, 177): the
   holding company REVERSED Rs 3.53 cr of previously recognised DTA this
   year because management no longer judges future standalone taxable
   profits probable — a specific, quantified admission that sits uneasily
   against the going-concern note's "actively pursuing new business
   opportunities" language (Note 39 standalone / Note 44 consolidated).
   The recognised Group DTA is now 96.5% carried-forward-loss-based (Rs
   11.39 cr of Rs 11.80 cr total), an increasingly loss-dependent asset.

5. 🟡 Trade receivables ageing (Note 10, p.161-163): Rs 105.11 cr against
   Rs 181.29 cr revenue = 212 days DSO (confirms the injected fact
   exactly). The >6-month bucket improved from 42.2% to 24.3% of
   receivables, but 23.4% of ALL receivables still sit in the 6-12 month
   band. A Rs 2.51 cr provision write-back with zero new provisioning in
   FY26, alongside a Rs 4.83 cr net bad-debt charge through the P&L (up
   from Rs 0.49 cr FY25), needs reconciling by management (Note 10(b),
   p.163; Note 30, p.176).

6. 🔴 Gearing ratio jumped from 64.6% to 88.0% and the current ratio fell
   from 1.69 to 1.37 in one year (Note 38, 36(B), consolidated, p.184,
   189) — leverage is rising into a second consecutive loss-making year,
   with 89.4% of debt on floating rates and 69.8% technically repayable on
   demand (cash credit).

7. 🔴 MSME payable dues more than tripled (Rs 27.81 lakh → Rs 93.27 lakh)
   and accrued unpaid MSME interest rose 20x (Note 19/40, p.171-172) — a
   clear directional deterioration in small-supplier payment discipline,
   small in absolute rupees but a genuine compliance/reputational
   exposure.

8. 🟡 Contingent liabilities rose 27.5% YoY to Rs 37.88 cr (27.9% of net
   worth), driven by two large new Maharashtra CST "F-Form" demands
   totalling Rs 17.96 cr (Note 39(A)(xv)-(xvi), p.192), on top of a
   recurring pattern of multi-state GST notices.

9. 🟡 Government subsidy dependency: the Maharashtra WIPS VAT-refund
   scheme contributed Rs 6.54 cr (3.6% of revenue) to FY26 revenue (Note
   7/23, p.161, 176) — a state-policy-dependent revenue line embedded in
   "other operating revenue," not core trading income.

10. 🟡 Named advertising/marketing spend: "Selling, distribution &
    marketing expenses" (the correct line for the "brand spend eats the
    margin" narrative) was Rs 42.14 cr FY26 = 23.3% of wine-segment
    revenue, down from Rs 45.88 cr FY25 = 25.7% (Note 30, p.176). This
    sits below the gross-margin line — gross margin itself is healthy
    (~78%), but S&D/marketing plus employee costs plus finance costs
    consume the entire gross margin and more, which is the real driver of
    the operating loss, not a COGS/gross-margin problem.
