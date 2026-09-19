# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 1 OF 3 (FULL EXTRACTION)
Company: SHAREINDIA (Share India Securities Limited) | Run date: 2026-09-19
Source: inputs/annual-report/SHAREINDIA-AR-FY26.txt (FY26 AR, 335 pages, page markers cited)
Scope: Notes to the Standalone Financial Statements (Note 1–64, pp.140–221) and
Notes to the Consolidated Financial Statements (Note 1–68, pp.251–335). All rupee
figures are as printed in the source, in ` Lakhs, unless the source itself states
Lakhs/Cr differently. Cr equivalents shown in parentheses are arithmetic shown
inline (÷100), never a silent conversion.

Units reminder: AR reports in ` Lakhs (face: "(` in Lakhs)"). 1 Cr = 100 Lakhs.

═══════════════════════════════════════════════════════════════════
## LOAD-BEARING FACTS — WHAT THE NOTES SHOW (first verification priority)
═══════════════════════════════════════════════════════════════════

### LBF1 — PROP vs CLIENT revenue/profit split
The notes CANNOT fully answer this question; they establish the shape of the
problem instead of resolving it.

- Standalone income statement notes separate revenue lines cleanly:
  - Fees and commission income (broking, market making, distribution, depository,
    research advisory) = ` 13,197.33 lakhs (~₹131.97 Cr) FY26 vs ` 15,123.41 lakhs
    (~₹151.23 Cr) FY25 (Note 29, p.180) — DOWN 12.7% YoY.
  - Interest income = ` 21,826.59 lakhs (~₹218.27 Cr) FY26 vs ` 16,575.02 lakhs
    (~₹165.75 Cr) FY25 (Note 27, p.176) — up 31.7%, driven by MTF book growth
    (Note 9).
  - Net gain on fair value changes (securities for trade + derivatives + other
    investments — i.e. the proprietary trading book) = ` 72,005.77 lakhs
    (~₹720.06 Cr) FY26 vs ` 68,933.58 lakhs (~₹689.34 Cr) FY25 (Note 30, p.176–177).
    Of this, derivatives alone contributed ` 52,517.71 lakhs (~₹525.18 Cr) FY26.
  - Sale of commodities (physical Agri/Non-Agri trading) = ` 13,731.45 lakhs
    (~₹137.31 Cr) FY26 (Note 31, p.177).
  - Total income = ` 1,24,679.52 lakhs (~₹1,246.80 Cr) FY26 (Note 48a, p.194).
  🔴 The single largest income line by far, standalone, is the proprietary
  trading fair-value gain (₹720.06 Cr), 57.8% of total income, more than 5x
  fees-and-commission income (₹131.97 Cr, 10.6% of total income). This is a
  P&L fact, not an inference: management's "60% client by volume" claim
  (company memory) is a volume statistic and is not reconcilable to this
  revenue mix from the notes.
- Consolidated mirrors and amplifies the same shape: Net gain on fair value
  changes = ` 86,730.03 lakhs (~₹867.30 Cr) FY26 vs ` 88,758.57 lakhs
  (~₹887.59 Cr) FY25 (Note 31, p.282) — 58.3% of consolidated total income of
  ` 1,48,884.97 lakhs (~₹1,488.85 Cr) (Note 50a, p.295). Fees and commission
  income (incl. consultancy, loan processing) = ` 16,518.37 lakhs
  (~₹165.18 Cr) FY26 vs ` 20,306.56 lakhs (~₹203.07 Cr) FY25 (Note 30, p.278) —
  DOWN 18.7% YoY.
- Segment reporting (Note 45, consol, p.289–290) is the note that should
  resolve prop vs client, but it does NOT: "Share broking/trading business" is
  reported as ONE segment — revenue ` 1,38,784.39 lakhs (~₹1,387.84 Cr) FY26
  vs ` 1,36,666.72 lakhs (~₹1,366.67 Cr) FY25; segment result (EBIT)
  ` 53,389.97 lakhs (~₹533.90 Cr) FY26 vs ` 47,805.21 lakhs (~₹478.05 Cr) FY25.
  Standalone Note 43 (p.183) explicitly defers all segment disclosure to
  consolidated statements and gives none itself. 🔴 STRUCTURAL GAP: the notes,
  as filed, do not disaggregate the broking/trading segment into proprietary
  vs client-driven components. This must come from claude.ai live
  verification or a management Q&A, not this corpus.
- Other segments (consol, Note 45): Insurance business revenue ` 869.18 lakhs
  FY26 (down from ` 1,078.28 lakhs FY25); Merchant banking ` 2,397.25 lakhs;
  NBFC business revenue ` 5,552.63 lakhs, EBIT ` 2,496.55 lakhs; Technology
  services revenue ` 1,281.52 lakhs, EBIT ` 318.82 lakhs; Wealth management
  business (new) revenue nil, EBIT ` (3.24) lakhs loss.

### LBF2 — Promoter pledge and contingent liabilities
- Contingent liabilities (guarantees) are large and disclosed in granular
  detail, but the notes carry NO promoter-pledge disclosure at all — pledge
  status is not an Ind AS notes item; it lives in the shareholding pattern
  filed separately with the exchanges (BSE SHP), outside the AR's financial
  statement notes. **NOT FOUND IN DOCUMENT: pledgee identity, purpose of
  pledge, or any note cross-reference to promoter share encumbrance.**
- Guarantees given, standalone (Note 42, p.186): ` 2,91,103.00 lakhs
  (~₹2,911.03 Cr) as at 31-Mar-2026 vs ` 2,08,429.00 lakhs (~₹2,084.29 Cr) at
  31-Mar-2025 — UP 39.7% YoY. Almost entirely bank guarantees for exchange
  margin: NSE Clearing Ltd ` 2,11,622.25 lakhs (margin) + ` 100 lakhs
  (security deposit); MCX Clearing Corp ` 58,129.00 lakhs (margin, up from
  ` 40,129.00 lakhs) + ` 62.50 lakhs; BSE ` 48.75 lakhs; Indian Clearing
  Corp ` 80 lakhs; NCDEX ` 62.50 lakhs; NCCL ` 1,198.00 lakhs. Plus a
  standing ` 19,800.00 lakhs corporate guarantee to banks on behalf of
  wholly-owned subsidiary Share India Algoplus Private Limited (unchanged
  YoY).
- Guarantees given, consolidated (Note 44, p.288): ` 3,23,271.75 lakhs
  (~₹3,232.72 Cr) FY26 vs ` 2,18,065.75 lakhs (~₹2,180.66 Cr) FY25 — UP 48.3%
  YoY. NSE Clearing alone ` 2,63,542.25 lakhs (up from ` 1,76,336.25 lakhs).
  🟡 This growth rate (48% YoY) materially outpaces revenue growth (~1–2%
  consol) — the guarantee corpus is scaling with trading book/derivatives
  exposure, not with reported income.
- Collateral behind the guarantees: fixed deposits pledged rose from
  ` 92,141.81 lakhs to ` 1,26,478.28 lakhs standalone (+37.3%, Note 42a,
  p.186); ` 1,06,980.95 lakhs to ` 1,52,688.19 lakhs consolidated (+42.7%,
  Note 44a, p.288). Property pledged (company + promoters/directors,
  "market value after haircut") ` 3,517.01 lakhs → ` 6,708.86 lakhs, both
  standalone and consol (same amount, so this is company-only property, not
  incremental subsidiary property) — UP 90.8% YoY. 🟡 Property owned by
  promoters/directors is explicitly named as part of the collateral pool for
  bank guarantees (Note 42a(2)/44a), i.e. promoter personal assets already
  back company obligations, separate from any share pledge.
- Income tax and indirect tax demands are immaterial: ` 68.15 lakhs and
  ` 3.79 lakhs respectively (consol Note 44b/c, p.288) — company contesting,
  no provision. 🟢.
- Net worth (standalone) ` 2,23,406.19 lakhs (~₹2,234.06 Cr, Note 58, p.218);
  consol net worth (incl. NCI) ` 2,65,484.74 lakhs (~₹2,654.85 Cr, Note 63,
  p.328). Standalone guarantees-to-net-worth = 130.3%; consol = 121.8%. This
  ratio is very large for a non-bank entity but is standard for a
  broker/clearing member (guarantees are margin deposits with exchanges, not
  credit risk in the ordinary sense) — flagged for the risk sections to
  weigh, not asserted here as distress.

### LBF3 — Cash conversion: growth-induced or structural?
The notes point to GROWTH-INDUCED, not trading-inventory buildup, though the
funding mix (external debt/NCDs, not retained cash) is itself worth watching.
- MTF book (standalone, Note 9, p.157–158): ` 40,261.41 lakhs (~₹402.61 Cr)
  at 31-Mar-2026 vs ` 23,705.55 lakhs (~₹237.06 Cr) at 31-Mar-2025 — UP 69.8%
  YoY. Consol MTF-inclusive gross loans ` 71,723.82 lakhs vs ` 52,963.89
  lakhs (+35.4%, Note 9, p.257).
  - Impairment allowance on the consol loan book grew faster than the book
    itself: ` 555.45 lakhs vs ` 349.56 lakhs (+58.9%) against gross-loan
    growth of 35.4% (Note 9, p.257) — the allowance is rising as a share of
    the book. Standalone MTF impairment allowance is ` NIL both years (Note
    9, p.157) — the Company holds MTF is stated 100% collateral-covered and
    "does not have any margin trading facilities which may fall under stage
    2 or stage 3" (Note 54, p.211/consol Note 55, p.318). 🟡 This "always
    Stage 1" assumption for MTF, unchanged across years, is an aggressive
    modelling choice worth testing against the group's stated GNPA of 4.30%
    for the NBFC book (per MD&A, not the notes) — the two books (parent MTF
    vs Fincap NBFC loans) are NOT the same exposure and the notes do not
    give a rupee-value NPA bucket for either.
  - Securities for trade (the closest thing to "trading inventory"): grew
    from ` 17,367.40 lakhs to ` 24,276.59 lakhs standalone (+39.8%, Note 6,
    p.155) and ` 17,479.35 lakhs to ` 25,888.96 lakhs consol (+48.1%, Note 6,
    p.255) — smaller in absolute rupees than MTF growth (` 16,556 lakh
    increase standalone) but a similar percentage rate; both are growing,
    consistent with a business scaling its balance sheet on both the client
    (MTF) and prop (securities/derivatives) sides simultaneously.
  - Deposits/margin with exchanges and clearing corporations barely moved
    (` 401.08 lakhs → still small, Note 11, p.161–162) — the margin drag is
    mostly channelled through fixed deposits pledged for bank guarantees
    (above), not a separate cash-margin line.
  - Financing side: Debt securities (NCDs) ` NIL → ` 11,243.17 lakhs
    standalone (new, Note 17, p.171–172); Borrowings (other than debt
    securities) ` 34,937.39 lakhs → ` 45,725.00 lakhs (+30.9%, Note 18,
    p.172–173). Cash-flow reconciliation (Note 57, p.217) confirms net new
    financing inflows of ` 21,504.92 lakhs standalone during the year,
    funding the MTF/securities growth described above — this is the
    mechanical link between "CFO negative" and "MTF book growth", visible
    directly in the notes.
  - 🔴 RED FLAG within LBF3: the ` 9,990 lakh (~₹99.9 Cr) First-Issue NCD
    (allotted 23-Jun-2025) needed an end-use CHANGE that the Board sought
    from NCD holders/Debenture Trustee under SEBI rules, but "owing to
    practical difficulties in obtaining the requisite approvals," the Board
    (19-May-2026) instead approved EARLY REDEMPTION of these NCDs, "subject
    to receipt of necessary approvals and on such date as may be determined
    by the Company" (Note 17e, p.171; identical language, Note 18e consol,
    p.271–272). This is filed BEFORE the Sep-2026 stress events in company
    memory (adjourned NCD holders' meeting, Aug–Sep 2026) and is very likely
    the same instrument — the notes give the origin of that adjourned
    meeting, four months before it happened.

### LBF4 — Funding and disclosure stress, Sep-2026
**NOT FOUND IN DOCUMENT — and this absence is itself the finding.** The AR's
"Events after the reporting date" notes (standalone Note 62, p.221; consol
Note 66, p.334) both state: "There were no significant events after the end
of the reporting period which require any adjustment or disclosure... the
Company has not recognised Final dividend... as a liability." The financial
statements were "approved for issue by the Board of Directors on May 19,
2026" (accounting policy 2.1(a)(b), p.140, standalone and consol identical).
Every element of LBF4 — the Infomerics ISSUER NOT COOPERATING downgrade
(16-Sep-2026), the adjourned NCD holders' meeting, the board meeting on the
preferential equity/warrant raise (21-Sep-2026), and the Enshrine Leasing
property purchase (17-Sep-2026) — post-dates the AR's signing by four
months and is absent from this document by construction. The only note-level
evidence bearing on LBF4 is the NCD end-use/early-redemption item under LBF3
above, which is a plausible root cause of the adjourned NCD holders' meeting.
LBF4 must be verified from the rating rationale documents, Reg 30
announcements, and Q1 FY27 filings — not this AR.

═══════════════════════════════════════════════════════════════════
## NOTE-BY-NOTE EXTRACTION — STANDALONE FINANCIAL STATEMENTS (Notes 1–64, pp.140–221)
═══════════════════════════════════════════════════════════════════

**Note 1 — Corporate Information (p.140).** Share India Securities Ltd,
incorporated 12-Jul-1994, registered office Gujarat. Trading/clearing member
of BSE, NSE, MSEI, MCX, NCDEX; depository participant with CDSL and (new
this year) NSDL; registered as Portfolio Manager and Research Analyst with
SEBI. 🟢.

**Note 2 — Material accounting policies (pp.140–153).**
- Depreciation: diminishing balance method per Schedule II useful lives
  (Building 60y, Computer 3y, Server 6y, Motor Car 8y, Motor Bike 10y,
  Electrical Equipment 10y, Furniture 10y, Office Equipment 5y, Plant &
  Machinery 15y) (p.142) — all within Schedule II norms, no aggressive
  extension. 🟢.
- Investment property depreciated straight-line (p.142–143) — inconsistent
  method vs PPE's diminishing balance, but this is permitted and disclosed,
  not a red flag on its own; small balance (₹2.78 Cr net block).
  Intangibles (computer software): 5-year straight line (p.144).
- ECL policy: simplified approach, lifetime ECL for trade receivables based
  on 3–5 year historic loss experience (p.145–146); three-stage ECL model
  described for loans, not spot-tested against actual GNPA in the notes
  (see LBF3 above). Ind AS 116 leases: incremental borrowing rate used when
  implicit rate not determinable (p.143) — actual rate not separately
  disclosed in the notes (NOT FOUND).
- Revenue recognition (2.13, p.147–148): five-step Ind AS 115 model for
  fee/brokerage income; proprietary trading income explicitly carved OUT of
  Ind AS 115 and booked under Ind AS 109 "as and when trade is executed" —
  a correct and conservative classification, not aggressive. 🟢.
- 2.26/2.27 (pp.151–153): no supplier finance arrangements; Ind AS 1 current/
  non-current liability classification amendments have no P&L effect;
  company not in scope of OECD Pillar Two. No first-time-adoption impact
  disclosed this year (no new standard materially changed P&L). 🟢.

**Note 3 — Cash and cash equivalents (p.154).** ` 48,593.29 lakhs (FY26) vs
` 52,419.77 lakhs (FY25) — down 7.3%. Of this, FDs under lien with exchanges
` 16,859.33 lakhs (up from ` 7,039.52 lakhs); FDs for bank guarantee/OD fell
to nil from ` 33,016.99 lakhs (reclassified into Note 4, >3 month maturity
bucket). 🟢 mechanical, not a red flag.

**Note 4 — Bank balance other than cash and cash equivalents (p.154).**
` 2,27,021.64 lakhs vs ` 1,71,329.85 lakhs (+32.5%) — FDs for bank
guarantee/overdraft ` 1,54,432.89 lakhs (up from ` 1,12,361.82 lakhs). This
is the primary home of the collateral discussed under LBF2.

**Note 5 — Derivative financial instruments (pp.154–155).** Notional value
` 5,35,494.48 lakhs (FY26) vs ` 8,67,495.32 lakhs (FY25) — notional DOWN
38.3% even as the fair-value P&L on derivatives (Note 30) rose. Asset side
` 5,114.76 lakhs, liability side ` 4,411.89 lakhs FY26. Options are the bulk
of exposure (equity-linked options ` 2,48,889.94 lakhs notional; commodity
options ` 1,90,686.80 lakhs notional). 🟡 Falling notional with rising
realised gain is consistent with either better risk-adjusted positioning or
a smaller book turning over more profitably — cannot be distinguished from
the notes alone.

**Note 6 — Securities for trade (p.155).** Equity shares held for trade
` 24,276.59 lakhs vs ` 17,367.40 lakhs (+39.8%). See LBF3.

**Note 7 — Trade receivables (pp.156–157).** Total (net of ECL) ` 3,011.91
lakhs vs ` 2,263.75 lakhs. Provision for ECL unchanged at ` 39.50 lakhs both
years. Ageing: 98.7% of gross receivables under 6 months both years — clean
ageing profile. 🔴 BUT: "Trade receivables from related parties" jumped from
` 6.12 lakhs to ` 826.37 lakhs, and "Dues from Directors or firms in which a
director is a partner/director" jumped from ` 0.24 lakhs to ` 788.61 lakhs
(p.156) — a >100x increase, unexplained in the note. This is a genuine new
finding, not previously in company memory, and should be a Q&A item (see
Section D below).

**Note 8 — Other receivables (p.157).** Income receivables ` 370.71 lakhs vs
` 830.16 lakhs — DOWN 55.3%. Ageing clean (<6 months: 99.9%). 🟢.

**Note 9 — Loans (pp.157–159).** See LBF3 for MTF detail. Also: intercorporate
loans ` 12,666.80 lakhs (up from ` 8,974.45 lakhs), including a loan to
wholly-owned subsidiary Share India Algoplus Pvt Ltd of ` 9,486.19 lakhs at
11% (up from 8% prior year and ` 6,007.95 lakhs balance) repayable on
demand, and a loan to foreign subsidiary Share India Global Pte Ltd of
` 3,180.61 lakhs at 11%, repayable within 10 years. 🟡 The Algoplus loan
rate was raised from 8% to 11% YoY and remains repayable on demand for a
subsidiary whose profit fell 65% this year (see Note 61/62 consol below) —
worth checking whether this loan is itself now under credit stress. Loans
to promoters: ` 0.07 lakhs only (no terms specified) — immaterial.

**Note 10 — Investments (pp.159–164).** Total ` 30,706.44 lakhs vs
` 28,949.96 lakhs. Investment in subsidiaries at cost rose sharply from
` 4,575.01 lakhs to ` 13,100.00 lakhs (+186.4%) — two new subsidiaries
incorporated this year (Share India Wealth Multiplier Solutions, Share India
Cred Capital) plus capital infusion into Share India Fincap (` 6,016.25
lakhs, up from ` 1,016.26 lakhs — a 6x increase, funding the NBFC book) and
Share India Capital Services (` 3,325.00 lakhs, up from ` 525.00 lakhs).
FVPL equity book (listed proprietary stock positions) fell from ` 18,194.26
lakhs to ` 15,692.00 lakhs — portfolio turned over, individual holdings
listed in full (pp.160–163) including stakes in Metropolitan Stock Exchange
(` 8,535.34 lakhs, an unquoted strategic holding) and National Commodity &
Derivatives Exchange (` 2,800.00 lakhs, new this year). 🟢 no impairment
booked on any investment.

**Note 11 — Other financial assets (p.164).** ` 1,020.62 lakhs vs
` 1,035.72 lakhs — flat. New impairment allowance of ` 56.71 lakhs booked
this year (100% of a receivable from liquidation of Total Securities
Overseas Ltd, outstanding >3 years — see Note 54C, p.212).

**Note 12 — Current tax assets (net) (p.164).** ` 758.46 lakhs vs
` 682.67 lakhs. 🟢 routine.

**Note 13(a) — Investment property (pp.164–165).** Net block ` 277.89 lakhs.
Fair value of leasehold land ` 2,464.38 lakhs (up from ` 2,124.90 lakhs) per
external registered valuer, Level 2 — carrying value at cost is ~9x below
fair value, a conservative (not aggressive) carrying policy. 🟢.

**Note 13(b) — Property, plant & equipment (p.166).** Net block ` 3,552.25
lakhs vs ` 3,846.70 lakhs. No revaluation during the year (confirmed at
Note 58c, p.219). Additions ` 631.91 lakhs, largely Building (` 187.85
lakhs) and Electrical Equipment (` 102.74 lakhs). 🟢 routine capex.

**Note 13(c) — Right-of-use assets (p.167).** Net block ` 1,859.31 lakhs vs
` 2,148.27 lakhs. Additions ` 354.63 lakhs; deletions ` 271.38 lakhs
(a lease surrendered/renegotiated).

**Note 13(d) — Capital work-in-progress (p.167).** ` 38.95 lakhs, entirely
"less than 1 year" ageing, no overdue projects. 🟢.

**Note 13(e) — Intangible assets (p.168).** Computer software net block
` 27.89 lakhs. Immaterial, no new intangible additions this year. 🟢.

**Note 14 — Other non-financial assets (p.168).** ` 3,548.20 lakhs vs
` 2,744.47 lakhs (+29.3%) — driven by prepaid expenses (` 2,057.87 lakhs, up
from ` 1,260.73 lakhs, +63.2%). NOT FOUND: no breakdown of what drove the
prepaid-expense jump.

**Note 15 — Assets held for sale (p.169).** ` NIL vs ` 105.59 lakhs — Delhi
branch buildings previously held for sale were disposed of during the year;
no impairment was needed on reclassification. 🟢 closed out cleanly.

**Note 16 — Trade payables (pp.169–170).** ` 57,098.64 lakhs vs
` 41,247.71 lakhs (+38.4%) — grew roughly in line with the balance-sheet
scale-up. Zero MSME dues in trade payables. Ageing: 99.9% under 1 year both
years. 🟢 no stretching of payment terms evident.

**Note 17 — Debt securities (pp.170–171).** See LBF3 red flag above (NCD
end-use change failure → planned early redemption).

**Note 18 — Borrowings (other than debt securities) (pp.171–172).** Total
` 45,725.00 lakhs vs ` 34,937.39 lakhs (+30.9%). New this year: ` 5,003.69
lakhs term loan secured against "lien on shares of promoter, directors and
relatives" (Tenure 12 months) — 🟡 this is new-in-FY26 financing secured
directly against promoter/director/relative shareholdings, distinct from
(but adjacent to) the promoter-pledge question in LBF2; it is a company
borrowing collateralised by promoter shares, which is a related-party credit
support arrangement worth separate tracking from any personal promoter
margin pledge. Loan from related parties (repayable on demand) fell from
` 1,366.55 lakhs to ` 389.58 lakhs. No defaults in repayment (p.172).

**Note 19 — Lease liabilities (p.172).** ` 2,084.68 lakhs vs ` 2,262.62
lakhs. 🟢.

**Note 20 — Other financial liabilities (p.172).** ` 54,925.68 lakhs vs
` 41,083.88 lakhs (+33.7%) — "Margin money received from client" is the
largest line, ` 40,099.40 lakhs (up from ` 25,217.00 lakhs, +59.0%) —
client-side margin liability growing faster than most other balance sheet
items, consistent with more client trading activity funnelled through the
Company. "Payable to exchanges" FELL from ` 13,160.56 lakhs to ` 9,690.36
lakhs (-26.4%).

**Note 21 — Provisions (p.173).** Gratuity provision ` 725.19 lakhs vs
` 510.77 lakhs (+42.0%) — see Note 45 for actuarial detail.

**Note 22 — Deferred tax assets/(liabilities), net (p.173).** Net DTL
` (659.10) lakhs vs ` (556.49) lakhs — driven mainly by fair-value gains on
investments/derivatives creating deferred tax liabilities (p.184–185). 🟢
routine, no unusual DTA recognition.

**Note 23 — Other non-financial liabilities (p.173).** ` 2,827.58 lakhs vs
` 569.31 lakhs (+396.7%) — driven by "Revenue received in advance" jumping
from ` 103.40 lakhs to ` 1,941.88 lakhs. NOT FOUND: nature of this advance
revenue is not detailed in the note; worth a Q&A item given the size of the
jump.

**Note 24 — Liabilities towards Assets held for sale (p.173).** ` NIL vs
` 130.00 lakhs — cleared out alongside Note 15 disposal. 🟢.

**Note 25 — Equity share capital (pp.174–177).**
- Issued/paid-up ` 4,376.51 lakhs (21,88,25,530 shares of ` 2 each) vs
  ` 4,364.39 lakhs (21,82,19,615 shares) — 6,05,915 new shares from ESOP
  exercise only this year (no warrant conversions, unlike FY25's 2,60,69,745
  shares from warrant conversion).
- Promoter/promoter-group holding 48.62% at 31-Mar-2026 vs 48.67% at
  31-Mar-2025 (p.175–176) — broadly flat; individual promoter entities show
  large percentage swings (e.g. Rachit Gupta -42.81%, Yash Pal Gupta -89.03%,
  RS Futures LLP +60.11%, Skyveil Trade Solutions LLP +107.85%) — i.e.
  shares moved BETWEEN promoter-group entities, not out of the group. This
  note does NOT disclose pledge status (see LBF2).
- Dividend: FY26 three interim dividends totalling ` 0.30+0.40+0.40 = ` 1.10
  per share paid during the year (` 2,406.88 lakhs) plus FY25 final dividend
  ` 0.25/share paid in FY26 (` 547.07 lakhs) = ` 2,954.15 lakhs total paid.
  FY26 final dividend of ` 0.50/share RECOMMENDED (up from ` 0.25/share for
  FY25) — a doubling of the final dividend rate even as the company sought
  NCD early redemption and expanded borrowings. 🟡 worth weighing dividend
  policy against the funding stress narrative.
- ESOP schemes: ESOS 2022 fully granted/exercised (30,00,000 authorised,
  19,14,965 granted-and-exercised, balance 10,85,035 not yet granted); ESOS-II
  10,00,000 authorised, only 3,77,000 granted to date (p.177).

**Note 26 — Other equity (pp.177–179).** Total ` 2,19,029.68 lakhs vs
` 1,91,700.34 lakhs (+14.3%). Retained earnings ` 1,28,264.99 lakhs (up from
` 1,00,801.36 lakhs). Securities premium grew only ` 1,835.40 lakhs this
year (vs ` 37,613.38 lakhs in FY25 from warrant conversion) — FY26 equity
growth is organic (retained profit), not capital-raise driven, unlike FY25.
🟢 clean reserve movements, nature/purpose of each reserve properly
disclosed per Ind AS requirement.

**Note 27 — Interest income (p.176).** See LBF1.

**Note 28 — Dividend income (p.176).** ` 1,966.21 lakhs vs ` 2,869.78 lakhs
(-31.5%) — from subsidiaries ` 348.00 lakhs (down from ` 1,113.60 lakhs,
-68.7%) and from trading/investment shares ` 1,618.21 lakhs (down from
` 1,756.18 lakhs). 🟡 the sharp fall in dividend FROM SUBSIDIARIES (mainly
Algoplus, per Note 52 detail) again correlates with Algoplus's profit
decline this year.

**Note 29 — Fees and commission income (p.176).** See LBF1. Income from
broking and related services fell from ` 13,575.98 lakhs to ` 11,665.97
lakhs (-14.1%) — the core brokerage line is SHRINKING in absolute terms.

**Note 30 — Net gain on fair value changes (pp.176–177).** See LBF1.
Realised gains ` 75,666.92 lakhs vs unrealised ` (3,661.15) lakhs FY26 —
i.e. the FY26 fair-value gain line is entirely realised-trade profit with a
small unrealised drag, a cleaner quality-of-earnings signal than a year
where unrealised marks dominate. 🟢 on quality-of-earnings grounds (realised,
not mark-to-market paper gains), though the SIZE relative to fee income
remains the LBF1 concern.

**Note 31 — Sale of products (p.177).** Commodities trading ` 13,731.45
lakhs vs ` 10,278.93 lakhs (+33.6%).

**Note 32 — Other income (p.177).** ` 1,952.17 lakhs vs ` 2,061.00 lakhs.
Includes "User ID/Other charges received" ` 1,448.66 lakhs (down from
` 1,635.68 lakhs) — a fee line tied to the uTrade algo platform user base
(company memory: 72,507 subscriptions, 6,543 paid).

**Note 33 — Finance costs (p.177).** ` 10,421.40 lakhs vs ` 6,793.59 lakhs
(+53.4%) — guarantee charges alone ` 2,410.46 lakhs (up from ` 2,189.83
lakhs) and interest on borrowings ` 5,218.83 lakhs (up from ` 2,693.07 lakhs,
+93.8%). Finance cost growth (53.4%) far outpaces revenue growth — the cost
of funding the balance-sheet scale-up is rising faster than income from it.

**Note 34 — Operating expenses (p.177).** ` 26,035.48 lakhs vs ` 30,571.82
lakhs (-14.8%) — Exchange/SEBI charges fell from ` 22,245.52 lakhs to
` 18,771.26 lakhs (-15.6%), consistent with lower derivatives notional
(Note 5) even as fair-value gains rose — i.e. FY26 generated MORE trading
profit on a SMALLER, more efficient book. 🟢 improving unit economics on the
prop book, a genuinely positive finding.

**Note 35 — Impairment on financial instruments (p.178).** ` 56.71 lakhs vs
` 63.40 lakhs — small, tied to the Total Securities Overseas Ltd write-down
(Note 11). 🟢.

**Note 36 — Purchases of stock-in-trade (p.178).** ` 13,952.38 lakhs vs
` 10,290.64 lakhs, tracking commodity sales (Note 31).

**Note 37 — Employee benefits expenses (p.178).** ` 27,090.48 lakhs vs
` 28,391.91 lakhs (-4.6%) — Salaries roughly flat (` 25,818.08 lakhs vs
` 25,448.05 lakhs) but ESOP compensation expense fell sharply from
` 2,133.88 lakhs to ` 658.02 lakhs (-69.2%) as the 2022 ESOP scheme largely
finished vesting. Gratuity expense also fell (` 167.17 lakhs vs ` 436.76
lakhs) due to a large FY25 actuarial gain reversing (see Note 45).

**Note 38 — Depreciation and amortisation (p.178).** ` 1,365.09 lakhs vs
` 1,420.52 lakhs — broadly flat. 🟢.

**Note 39 — Other expenses (p.179).** ` 4,469.15 lakhs vs ` 4,437.74 lakhs —
flat overall. Notable items: Legal/professional/consultancy charges ` 1,255.38
lakhs (largest single line); Payments to auditor ` 49.70 lakhs (up from
` 34.70 lakhs, +43.2%) — the FY25 figure "includes the remuneration paid... to
the erstwhile auditor amounting to ` 1.50 lakhs" (p.183), confirming an
auditor CHANGE occurred at or before FY25 (predecessor firm not named in the
notes; reason for change NOT FOUND here). 🟡 flag for Q&A: why did the prior
auditor leave, and is MSKA & Associates LLP (formerly M S K A & Associates)
a fresh appointment or continuation under a new legal form? GST expense fell
sharply from ` 152.89 lakhs to ` 5.06 lakhs (unexplained one-off in FY25,
reversed in FY26 — NOT FOUND why FY25 GST expense was so much higher).

**Note 40 — Income taxes (pp.179–181).** Effective tax rate 24.58% FY26 vs
22.89% FY25, against a statutory rate of 25.17% both years — close to
statutory, no aggressive tax-rate arbitrage. Current tax ` 9,565.90 lakhs
(relating to current year); a small ` 59.28 lakhs adjustment relating to
prior years. 🟢 clean reconciliation, no unusual items.

**Note 41 — Earnings per share (p.182).** Basic EPS ` 13.61 (FY26) vs
` 11.73 (FY25); Diluted EPS ` 13.58 vs ` 11.22. Basic-diluted gap narrow
(0.2% FY26) — minimal dilution drag from ESOPs/warrants this year, a
material narrowing from FY25's larger gap (11.73 vs 11.22, ~4.3%) as warrant
dilution fully worked through. 🟢.

**Note 42 — Contingent liabilities and commitments (pp.182–183).** See LBF2.
Capital commitments: NIL both years.

**Note 43 — Segment reporting (p.183).** Explicitly deferred to consolidated
statements; standalone gives NO segment disclosure. See LBF1.

**Note 44 — Leases (pp.183–184).** Company as lessee: office premises,
11–120 month terms. Lease liability roll-forward and maturity profile
disclosed in full (p.184). As lessor: sub-letting arrangements, immaterial
income (` 72.95 lakhs). 🟢 routine, Ind AS 116 compliant.

**Note 45 — Employee benefits (pp.185–188).** Gratuity (unfunded defined
benefit): obligation ` 725.19 lakhs vs ` 510.77 lakhs. Discount rate 6.85%
(up from 6.45%). Attrition assumption for trading employees is EXTREME:
76.30% FY26 (up from 72.73% FY25) vs 30.02% for other employees (up from
24.71%) (p.187) — this is a disclosed, industry-typical assumption for
broker dealing-room staff, not a red flag per se, but it signals very high
staff churn in the revenue-producing (trading) function, worth noting for
franchise-durability analysis. FY25 had a large actuarial GAIN of ` (637.95)
lakhs (mainly demographic-assumption change, ` (360.63) lakhs); FY26 shows
an actuarial LOSS of ` 78.60 lakhs — the direction reversed. Sensitivity
table disclosed in full (p.188). 🟢 disclosure quality good; assumption
itself (76% attrition) is a business-model observation, not an accounting
red flag.

**Note 46 — Employee stock option plan (pp.189–191).** Two schemes detailed
in full (grant dates, Black-Scholes inputs, vesting/exercise activity).
ESOS 2022 fully exercised out this year (6,04,665 options); ESOS-II has
3,65,750 outstanding, weighted average exercise price ` 2.00 (i.e.
effectively free shares at par — high dilution value per option, though
volumes are small relative to the 21.88 Cr shares outstanding). 🟢 disclosure
complete; ESOP fair values used volatility inputs ranging 32.03%–50.00%,
consistent with a high-beta trading-house stock — a subtle corroboration of
this being a volatile, trading-driven equity story even from the ESOP
valuation inputs.

**Note 47 — Assets pledged as security (p.191).** Total assets pledged for
borrowings ` 2,50,828.23 lakhs vs ` 2,45,533.85 lakhs — dominated by
"Current assets, receivables (including MTF)" ` 2,10,987.83 lakhs (up from
` 1,85,819.49 lakhs). Cross-reference confirms the MTF book (Note 9) is
itself pledged to secure the Company's own borrowings — a leverage-on-
leverage structure (client MTF exposure funded by, and pledged against,
company borrowings) that is standard for the business model but worth
naming precisely.

**Note 48 — Revenue from Contract with Customers (pp.191–192).** See LBF1.
Disaggregation: 98.8% India, 1.2% outside India (p.192) — the international
subsidiary (Share India Global Pte Ltd, Singapore) contributes marginally
to fee revenue.

**Note 49 — Foreign currency earnings and expenditure (p.192).** Small,
` 93.91 lakhs expenditure vs ` 466.26 lakhs income — net foreign currency
inflow, immaterial to scale.

**Note 50 — Unhedged foreign currency exposure (pp.192–193).** ALL foreign
currency exposure is stated as HEDGED both years; unhedged exposure NIL.
🟢 — consistent with the stated hedging policy (Note 2.11h).

**Note 51 — Corporate social responsibility (pp.193–194).** Required spend
` 590.10 lakhs; actual spend ` 291.83 lakhs; shortfall ` 298.27 lakhs tied
to an ongoing hospital project (Project Ujjwal Drishti, Kapurthala, Punjab)
whose unspent amount was correctly deposited to an Unspent CSR Account by
30-Apr-2026 per Companies Act requirements. 🟢 fully compliant treatment of
a genuine shortfall (not a governance red flag — the law explicitly permits
this route for ongoing projects).

**Note 52 — Related party disclosures (pp.194–207).** Extensive: 14
subsidiaries, 17 KMPs, ~38 relatives of KMPs, and ~65 entities under KMP/
relative control or influence are named (pp.195–199). Transaction table
(p.199–201) and party-level detail (pp.201–207) cover remuneration, rent,
dividends, brokerage, loans, and guarantees. Notable items beyond LBF1–4:
- Rent paid to Aggarwal Enterprises rose from ` 109.20 lakhs to ` 254.40
  lakhs (+133.0% YoY, p.205) — the largest percentage jump in any RPT rent
  line; no explanation given in the note (new premises? rate increase?
  NOT FOUND).
- Loan taken from/repaid to Kalyan Capitals Limited: ` 3,860.00 lakhs taken
  AND ` 3,860.00 lakhs repaid within the same year (p.202) — a full
  round-trip, closing balance nil; interest paid ` 64.55 lakhs (down from
  ` 157.19 lakhs). Not inherently improper, but worth naming as a pattern.
  Similar round-trip: loan taken/repaid with Share India Fincap
  (` 13,138.09 lakhs taken, ` 14,129.98 lakhs repaid, p.201).
  Similar with Share India Securities (IFSC): ` 1,815.60 lakhs given and
  ` 1,815.60 lakhs recovered same year (p.201) — same-year in-and-out
  intercompany loans, consistent with short-term treasury management
  between group entities, not concealment (fully disclosed), but the sheer
  number of round-trip loans warrants a treasury-policy question.
- Corporate guarantee RECEIVED (income) from Algoplus: guarantee charges
  ` 198.00 lakhs booked both years but the CLOSING balance receivable fell
  from ` 52.73 lakhs to ` NIL (p.196/207) — collected in full this year.
- No loans to promoters, directors, or KMPs on a repayable-on-demand or
  no-terms basis beyond ` 0.07 lakhs to a promoter (Note 9d, p.158) — this
  disclosure format (SEBI LODR Reg 53(F)) is present and clean. 🟢.

**Note 53 — Fair value measurement (pp.207–209).** Full Level 1/2/3
hierarchy tables for both years. Level 3 investments (unquoted equity, e.g.
Metropolitan Stock Exchange stake) total ` 14,660.68 lakhs FY26 (up from
` 11,849.06 lakhs) — 23.5% of total financial-asset fair value is Level 3
(model/unobservable-input based), a meaningful chunk of illiquid,
judgement-dependent valuation. Valuation techniques disclosed (quoted price,
NAV, "quotation price available" for unquoted equity — this last phrase is
vague; NOT FOUND: no further detail on how unquoted strategic stakes like
MSE/NCDEX are actually valued). 🟡 valuation-technique disclosure for the
largest Level 3 holdings (exchange stakes, ` 8,535+2,800 = ` 11,335.34
lakhs combined) is thin relative to their size.

**Note 54 — Financial risk management (pp.209–215).** Comprehensive market/
liquidity/credit risk disclosure with quantified sensitivities (FX ±5%,
interest rate ±100bp, equity price ±5%) — see LBF3 for the MTF ECL staging
detail. Liquidity maturity table (p.212) shows ` 57,098.64 lakhs of trade
payables and the bulk of borrowings due "on demand/less than 3 months" or
"3–12 months" — i.e. most financial liabilities are short-dated, which is
normal for a broker but means refinancing risk is a live, recurring event,
not a one-off. 🟢 disclosure quality high; the underlying maturity mismatch
(short-dated liabilities funding an MTF book with informal duration) is a
business-model observation for Role 1/6, not a notes-level red flag.

**Note 55 — Capital management (p.212).** Generic Ind AS 1 boilerplate;
confirms the Company must maintain minimum net worth per SEBI (Stock
brokers and sub-brokers) Regulations, 1992 and asserts compliance. No
specific minimum quantum disclosed (NOT FOUND).

**Note 56 — Maturity analysis (pp.212–213).** See LBF3; confirms 76% of
total assets and 91% of total liabilities are due within 12 months —
a short-duration balance sheet consistent with the broking/MTF model.

**Note 57 — Reconciliation of financing-activity liabilities (p.213).**
See LBF3 — the direct evidence that ` 21,504.92 lakhs of net new financing
cash flow (borrowings + NCDs) funded the year's balance-sheet growth.

**Note 58 — Other regulatory requirements (pp.214–217).** Full Schedule III
ratio table — see LBF2/LBF3 for debt-equity, DSCR, ISCR deterioration.
Additional clean confirmations: no benami property, no wilful defaulter
status, no struck-off company dealings, no undisclosed income, no crypto
trading, compliance with Section 186 and layering rules. 🟢. One open item:
Scheme of amalgamation of Silverleaf Capital Services Private Limited into
the Company — NCLT process ongoing, Joint Second Motion Petition filed
25-Mar-2026, final approval pending (p.219) — a live corporate-structure
event to track through to Phase 3.

**Note 59 — MSME dues (p.220).** ` 71.40 lakhs principal outstanding vs
` 43.42 lakhs — small, no interest/penalty due. 🟢.

**Note 60 — Fund utilisation, Rights/Warrant issue (p.220).** Historical
FY2022-23 rights-cum-warrant issue (` 80,404.51 lakhs total) fully utilised
by FY25 (` 76,154.50 lakhs to fund client margin/MTF, ` 3,964.11 lakhs
general corporate purpose) — no deviation from stated objects. Closed item,
no FY26 activity. 🟢.

**Note 61 — Books of account / audit trail (pp.220–221).** Confirms audit
trail (edit log) enabled on all accounting software except "tally" (used for
negligible transactions at a single branch), and audit trail not enabled at
database level for certain applications — a routine, honestly disclosed
limitation under the amended audit-trail rules, not evidence of tampering
(explicitly: "no instances of audit trail feature being tampered with").

**Note 62 — Events after the reporting date (p.221).** See LBF4 — "no
significant events," dated as of 19-May-2026 Board approval.

**Note 63 — Labour Code (p.221).** ` 11.97 lakhs incremental gratuity
impact from new Labour Codes, recognised in FY26. 🟢 routine, immaterial.

**Note 64 — Previous year regrouping (p.221).** Generic reclassification
statement, "does not affect overall financial position." No quantified
restatement given — see Section E (pattern pass) below.

═══════════════════════════════════════════════════════════════════
## NOTE-BY-NOTE EXTRACTION — CONSOLIDATED FINANCIAL STATEMENTS (Notes 1–68, pp.251–335)
═══════════════════════════════════════════════════════════════════
Consolidated notes largely mirror standalone in structure and policy
content (Notes 1–2, pp.251–262, identical accounting policies — not
repeated here). Differences and consolidation-specific findings only:

**Note 3–6 (Cash, bank balances, derivatives, securities for trade,
pp.253–255).** Consol cash ` 52,276.96 lakhs vs standalone ` 48,593.29
lakhs — subsidiaries add ` 3,683.67 lakhs of cash. Securities for trade
consol ` 25,888.96 lakhs includes ` 921.77 lakhs of debt securities held for
trade (new line, not present standalone) — a subsidiary (likely Fincap or
Algoplus) holds a debt-trading book the parent does not.

**Note 7 — Trade receivables, consol (pp.255–256).** ` 3,325.69 lakhs vs
standalone ` 3,011.91 lakhs — subsidiaries add ` 313.78 lakhs. Ageing
broadly consistent with standalone (clean, <6 months dominant).

**Note 9 — Loans, consol (pp.257–258).** Gross loans ` 71,723.82 lakhs
(includes Fincap NBFC book, loan to employees, inter-corporate loans, loans
to others beyond MTF) vs standalone MTF+ICD-only ` 52,928.21 lakhs —
confirms Fincap's book (not visible standalone) adds materially to group
loan exposure (~` 18,795.61 lakhs incremental beyond standalone,
approximating loans to others less standalone's own ICDs). Impairment
allowance ` 555.45 lakhs (consol) vs ` NIL (standalone) — ALL loan-loss
allowance in the group sits at the NBFC-subsidiary/other-loans level, not
in the parent's MTF book. This is the clearest note-level evidence that
credit risk concentrates in Fincap, consistent with the GNPA 4.30% figure
from the MD&A (not itself in the notes).

**Note 10 — Investments, consol (pp.258–262).** Group-level FVPL book
includes positions not held by the parent standalone: Chennai Chettinad
Products Pvt Ltd (` 471.72 lakhs, unquoted), Swastika Investmart Limited
(` 1,286.35 lakhs, a listed broking peer — held both as an investment and
implicitly a comparable), and offshore AIF/hedge fund positions (Kingsman
Class G shares ` 946.54 lakhs, Stellar Growth Fund VCC reduced to NIL from
` 1,703.07 lakhs — a full exit this year, gain/loss on exit not separately
quantified in this note — NOT FOUND). 🟡 the Stellar Growth Fund VCC full
redemption/exit (` 1,703.07 lakhs to nil) is a size-relevant event with no
explanatory note.

**Note 13 — Deferred tax, consol (p.261).** Swung from a NET DEFERRED TAX
LIABILITY of ` (497.38) lakhs (FY25) to a NET DEFERRED TAX ASSET of
` 148.11 lakhs (FY26) — a ` 645.49 lakh swing (Note 42, income tax note),
driven by MAT credit entitlement (` 199.11 lakhs recognised) and fair-value
timing differences. This DTA swing does not appear at standalone level
(where DTL grew), confirming it originates in a subsidiary (most likely
Algoplus, given its profit collapse — a loss-making or lower-profit year
can flip timing differences into a net asset position). 🟡 worth confirming
the DTA is backed by genuine expected future taxable profit at the
subsidiary generating it, especially given that subsidiary's 65% profit
decline this year (Ind AS 12 realisability test — not resolvable from the
notes alone).

**Note 14(a)–(f) — Investment property, PPE, ROU, CWIP, intangibles under
development, other intangibles, consol (pp.262–269).** Broadly mirrors
standalone plus subsidiary assets. Note 14(f) "Other intangible assets"
consol shows a distinct "uTrade Algo Software & App" intangible (net block
` 140.76 lakhs, amortising ` 60.76 lakhs/year on a straight-line basis over
what appears to be a ~5-year estimated life) NOT present in the standalone
schedule — this is Utrade Solutions Pvt Ltd's platform IP, held at the
subsidiary level.

**Note 17–19 — Trade payables, debt securities, borrowings, consol
(pp.267–274).** Consol debt securities ` 14,327.95 lakhs vs standalone
` 11,243.17 lakhs — the ` 3,084.78 lakhs difference is an 11.50% unlisted,
secured NCD (3,000 NCDs of ` 1 lakh face value) issued by A SUBSIDIARY,
"secured on receivables of the subsidiary company," maturing 1-Oct-2026
(Note 18c, p.271) — 🔴 this subsidiary NCD matures within days of this
run's date window (Sep-2026) and is a DISTINCT instrument from the
` 9,990 lakh parent NCD flagged under LBF3/LBF4. There are therefore
potentially TWO NCD-related events in play around Sep-Oct 2026: the
parent's proposed early redemption of the ` 9,990 lakh First Issue, AND a
subsidiary NCD (` 3,000 lakh face, ` 3,084.78 lakhs carrying) reaching
contractual maturity around 1-Oct-2026. This distinction is not visible at
standalone level and is a materially important disaggregation for LBF4
verification.

**Note 22 — Current tax liabilities, consol (p.269).** ` 99.93 lakhs vs
` 70.01 lakhs — small net payable position (differs from standalone's net
asset position, Note 12) reflecting subsidiary-level tax positions.

**Note 26–27 — Equity share capital / other equity, consol (pp.269–274 /
via index; not re-extracted, identical to standalone at parent level).**

**Note 31 — Net gain on fair value changes, consol (p.279).** See LBF1.

**Note 42 — Income taxes, consol (pp.282–285).** Effective tax rate 26.34%
FY26 vs 23.81% FY25 — HIGHER than statutory (25.17%) this year, driven by
"Difference in tax rates of certain entities under the Group" (` 328.00
lakhs adverse) — i.e. some group entities are taxed at rates above the
parent's, pulling the blended rate up. This is consistent with a
loss-making/lower-profit subsidiary (Algoplus) not being able to fully
utilise tax shields, or a different tax regime for the Singapore subsidiary.
🟡 the consol effective rate now EXCEEDING statutory (a reversal from FY25,
when it was below statutory) is worth tracking as a quality-of-earnings
signal — it typically means losses in some entities cannot offset profits
in others for tax purposes.

**Note 43 — EPS, consol (pp.284–285).** Basic EPS ` 14.79 FY26 vs ` 15.58
FY25 — DOWN 5.1%, even though standalone EPS ROSE (` 13.61 vs ` 11.73,
+16.0%). This is the single cleanest headline number confirming the
consol-vs-standalone divergence driven by subsidiary performance (see Note
61/62 below): the group's per-share earnings power weakened this year
despite the parent's own performance improving.

**Note 44 — Contingent liabilities, consol (pp.285–288).** See LBF2.

**Note 45 — Segment reporting, consol (pp.286–287).** See LBF1 — the key
note for the prop/client question, and its key structural limitation.

**Note 53 — Related party disclosures, consol (pp.296+, per index; content
consistent with standalone, Group-level).** No new counterparties beyond
standalone's universe were identified in the sampled sections.

**Note 59 — Consolidation principles / subsidiary list (pp.322–323).** 13
subsidiaries listed with ownership %; explicitly states "There are no
Associates/Joint-ventures of the Group as on March 31, 2026" (p.327,
Note 61 footnote) — no equity-method entities to separately assess.
Two new subsidiaries this year: Share India Wealth Multiplier Solutions
Pvt Ltd (100%, incorporated 6-Nov-2025) and Share India Cred Capital Pvt
Ltd (60%, NCI 40%, incorporated 6-Jan-2026) — the latter's purpose
("Cred Capital") suggests a further lending-adjacent entity; no business
description given in these notes (NOT FOUND — purpose must come from the
Board resolution/MOA, outside this AR's notes).

**Note 60 — Non-controlling interest (pp.323–325).** NCI total ` 1,990.94
lakhs (FY26) vs ` 1,490.58 lakhs (FY25). Per-entity detail shows Utrade
Solutions Pvt Ltd (NCI 36.61%) is the largest NCI-bearing entity
(` 1,135.59 lakhs), profitable (` 166.00 lakhs PAT FY26 vs ` 62.18 lakhs
FY25, up 167%) — a genuinely improving subsidiary, a useful counterweight
to the Algoplus/IFSC declines below. 🟢 for Utrade specifically.

**Note 61 — AOC-1, subsidiary salient features (pp.325–327).** 🔴 KEY
FINDING: Share India Algoplus Private Limited (100% owned, the algo-trading
subsidiary; note footnote confirms it was "Formerly Total Commodities
(India) Private Limited") — Turnover (Total Income) FELL from an implied
much larger base to ` 16,755.59 lakhs FY26, and Profit Before Tax COLLAPSED
from a FY25 level (back-calculated from Note 62 below, PAT ` 6,761.36
lakhs) to PBT ` 3,691.46 lakhs / PAT ` 2,383.04 lakhs FY26 — a 64.7% YoY
PAT decline. Separately, Share India Securities (IFSC) Private Limited
swung from PROFIT to LOSS: PBT ` (403.23) lakhs FY26 (a loss) vs an implied
FY25 profit (Note 62 confirms FY25 PAT ` 396.87 lakhs) — a full reversal.
No narrative explanation for either movement is given in the AOC-1 note
(NOT FOUND — this is a numbers-only Schedule III disclosure by design; the
"why" must come from the Board's Report / MD&A or management Q&A).

**Note 62 — Additional Schedule III information, consol (pp.327–330).**
Confirms and quantifies the Note 61 findings precisely (see LBF-adjacent
finding above): Algoplus PAT ` 2,383.04 lakhs FY26 (7.37% of consol profit)
vs ` 6,761.36 lakhs FY25 (20.64% of consol profit) — Algoplus's SHARE of
group profit fell from over a fifth to under a tenth in one year. IFSC
subsidiary: ` (417.60) lakhs FY26 [(1.29)% of consol profit] vs ` 396.87
lakhs FY25 [1.21% of consol profit]. Parent (Share India Securities
Limited) share of consol profit ROSE from 75.28% (FY25) to 92.03% (FY26) —
the group's profit base is becoming MORE concentrated in the standalone
entity and LESS diversified across subsidiaries this year, the opposite
direction from a "transition to annuity/fee businesses via subsidiaries"
narrative. 🔴 This is directly relevant to the run's transition thesis: if
the bull case rests on subsidiaries (Fincap/NBFC, Algoplus/algo-tech,
insurance, wealth) diversifying earnings away from the parent's prop/
broking book, FY26's Schedule III numbers show the OPPOSITE — concentration
in the parent rose, not fell.

**Note 63 — Other regulatory requirements, consol (pp.328–332).** See
LBF2/LBF3 for ratio deterioration (mirrors standalone pattern, marginally
worse: DSCR 4.62x→2.74x, ISCR 5.94x→4.42x). Same amalgamation-scheme
disclosure as standalone (Note 58j).

**Note 64 — MSME dues, consol (p.330).** Identical figures to standalone
(` 71.40 lakhs) — confirms MSME exposure sits entirely at the parent, none
at subsidiary level.

**Note 65 — Books of account, consol (p.330).** Same audit-trail
disclosure as standalone, extended to "the Group."

**Note 66 — Events after reporting date, consol (p.330).** See LBF4 —
identical "no significant events" statement.

**Note 67 — Labour Code, consol (p.330).** ` 141.73 lakhs incremental
gratuity impact group-wide (vs ` 11.97 lakhs standalone-only) — confirms
` 129.76 lakhs of the Labour Code gratuity impact sits at subsidiary level,
disproportionately larger than the parent's own share of group headcount
would suggest (NOT FOUND: per-subsidiary breakdown).

**Note 68 — Previous year regrouping, consol (p.331).** Same generic
statement as standalone Note 64.

═══════════════════════════════════════════════════════════════════
PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS
═══════════════════════════════════════════════════════════════════

1. 🔴 Segment reporting (Note 45 consol, p.289) reports "Share broking/
   trading business" as ONE undifferentiated segment (₹1,387.84 Cr revenue,
   ₹533.90 Cr EBIT FY26); the notes structurally cannot answer the LBF1
   prop-vs-client question. Net gain on fair value changes (proprietary
   trading) is ₹867.30 Cr consol FY26, 58.3% of total income and >5x fee
   income (Note 31, p.282; Note 50, p.295).

2. 🔴 Consolidated Schedule III additional information (Note 62, pp.327–
   330) shows the PARENT's share of consolidated profit rose from 75.28%
   (FY25) to 92.03% (FY26) — group earnings concentration in the standalone
   entity INCREASED this year, the opposite of a subsidiary-led
   diversification/transition narrative.

3. 🔴 Share India Algoplus Private Limited (100%-owned algo-trading
   subsidiary) PAT fell 64.7% YoY (₹67.61 Cr FY25 to ₹23.83 Cr FY26, Note
   62, p.329–330); Share India Securities (IFSC) Private Limited swung from
   a ₹3.97 Cr profit to a ₹4.18 Cr loss (Note 61/62). No explanation given
   in the notes (Schedule III is numbers-only by design).

4. 🔴 NCD funding stress origin, pre-dating Sep-2026: the ₹99.90 Cr First-
   Issue NCD (allotted 23-Jun-2025) needed an end-use change that NCD
   holders/Debenture Trustee would not approve; the Board (19-May-2026)
   pivoted to proposing early redemption instead (Note 17e standalone
   p.171, Note 18e consol p.271–272). A SEPARATE subsidiary NCD (₹30.85 Cr
   carrying value, 11.50%, secured on subsidiary receivables) matures
   1-Oct-2026 (Note 18c consol, p.271) — two distinct NCD events cluster
   around Sep-Oct 2026.

5. 🔴 Contingent liabilities (bank guarantees, almost entirely exchange
   margin) grew 48.3% YoY consolidated to ₹3,232.72 Cr (Note 44, p.288),
   far outpacing revenue growth (~1–2% consol); fixed deposits pledged as
   collateral grew 42.7% to ₹1,526.88 Cr (Note 44a).

6. 🟡 Debt-service and interest-coverage ratios weakened meaningfully
   BEFORE the Sep-2026 rating action: standalone DSCR 4.79x→3.25x, ISCR
   5.84x→4.87x (Note 58a, p.218); consol DSCR 4.62x→2.74x, ISCR 5.94x→4.42x
   (Note 63a, p.328).

7. 🟡 Trade receivables from related parties and director-linked firms
   jumped from near-zero to ₹8.26 Cr and ₹7.89 Cr respectively (standalone
   Note 7, p.156), unexplained in the notes.

8. 🟡 LBF2's promoter-pledge question has NO note-level home at all — the
   AR's financial statement notes carry no pledge disclosure; separately,
   NEW FY26 company borrowing (₹50.04 Cr) is secured against "lien on
   shares of promoter, directors and relatives" (Note 18, standalone
   p.171) — a related but distinct related-party credit-support fact.

9. 🟡 Consolidated deferred tax swung from a ₹4.97 Cr net liability to a
   ₹1.48 Cr net asset (Note 13/42 consol, pp.261, 282–285), most plausibly
   originating in the lower-profit Algoplus subsidiary — DTA realisability
   is not independently testable from the notes given that subsidiary's
   profit collapse.

10. 🟢/🟡 LBF3 (cash conversion) IS answered by the notes: MTF book +69.8%
    YoY standalone (₹402.61 Cr, Note 9, p.157) funded by ₹215.05 Cr of net
    new financing cash flow (new NCDs + higher borrowings, Note 57, p.213)
    — growth-induced, not trading-inventory buildup (securities for trade
    grew a smaller ₹68.99 Cr in absolute terms). The financing MIX (external
    debt, not retained cash) funding that growth is itself the emerging
    concern feeding into finding #6 above.

Events after reporting date (both standalone Note 62, p.221, and consol
Note 66, p.334) confirm NONE of LBF4 (Infomerics downgrade, NCD holders'
meeting adjournment, Enshrine Leasing purchase, 21-Sep-2026 board meeting)
is disclosed in this AR — it is signed 19-May-2026, four months before
those events. LBF4 requires the rating rationale and Reg 30 announcement
documents, not this corpus.
