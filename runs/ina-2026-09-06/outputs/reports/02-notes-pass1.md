# STAGE 2 / PASS 1: FULL EXTRACTION OF NOTES TO FINANCIAL STATEMENTS
Company: Insolation Energy Limited (INA), CIN L40104RJ2015PLC048445
Source: Annual Report FY2025-26 (year ended 31-Mar-2026), the only document in corpus
File: runs/ina-2026-09-06/work/extracted/annual-report__Annual_Report_2026.txt (200 pages,
page markers = PDF page numbers)
Run date: 2026-09-06

## STRUCTURAL NOTE BEFORE THE EXTRACTION (read this first)

The AR contains TWO complete note sets:
- CONSOLIDATED financial statements and notes: PDF pages 116-158 (Balance Sheet at p.116,
  Notes 4-59 running p.119-152, Note 57 subsidiary list p.150-151, Note 59 Business
  Combination p.152).
- STANDALONE (parent-only) financial statements and notes: PDF pages 154-189 (Notes 4-58,
  mirroring the consolidated numbering with a one-note offset from Note 41 onward because the
  standalone set has no Non-Controlling-Interest note).

Screener figures cited in the task brief (receivables, inventory, borrowings, net block,
total assets, other assets, cash) were checked against the AR and match the CONSOLIDATED
figures, not standalone (verified line by line: e.g. consolidated Trade Receivables Note 13
FY26 = Rs 281.59 cr, FY25 = Rs 110.09 cr, exact match; consolidated Inventory Note 12 FY26 =
Rs 379.05 cr, FY25 = Rs 76.98 cr, exact match). This Pass 1 therefore treats the CONSOLIDATED
notes as primary and pulls the STANDALONE notes only where the task brief asked for a
cross-check or where a material divergence surfaced (it did, on receivables ageing — see
Finding 1).

Net block reconciliation: the brief's "Rs 77.29 cr to Rs 524.89 cr" is PPE net block (Note 4,
consolidated: Rs 77.29 cr FY25 → Rs 473.77 cr FY26) PLUS Right-of-use asset net block (Note 6:
Rs 10.74 cr FY25 → Rs 51.11 cr FY26); 473.77 + 51.11 = 524.88 ≈ 524.89. This is a screener
classification convention, not an AR discrepancy — noted for downstream stages so nobody
re-flags it as an error.

CWIP: the brief's FY25 figure of Rs 46.10 cr does not match the AR consolidated CWIP of
Rs 52.88 cr (Note 5, FY25). NOT FOUND why screener differs; flagged for stage 0/reconciliation,
not chased further here (immaterial to the thesis either way).

### CORPUS GAP: Material Accounting Policies (Notes 1-3) — text not present in extraction

Both the consolidated and standalone Balance Sheets explicitly reference "MATERIAL ACCOUNTING
POLICIES ... Note No. 1-3" as a distinct block preceding the numbered schedule notes (p.116
line "MATERIAL ACCOUNTING POLICIES / ACCOMPANYING NOTES TO THE FINANCIAL STATEMENTS / 1-3 /
4-59"). I searched the full 200-page extraction exhaustively (page-by-page around the
Balance Sheet, and targeted phrase searches for "Revenue is recognised", "straight-line
method", "useful life", "lower of cost and net realisable value" as prose, "cash and cash
equivalents comprise", "borrowing costs", "Provisions are recognised when", etc.) and found
NO accounting-policy prose anywhere in the document, consolidated or standalone. The printed
page numbers run continuously from the CARO/IFC annexures (pages 223-226) straight into the
Balance Sheet (pages 227-228) with no room for the policy pages, and the standalone notes end
at Note 58 and go straight into the AGM Notice with no policy appendix either.
NOT FOUND IN DOCUMENT (extraction) — Notes 1-3 (Corporate Information, Basis of Preparation,
Significant/Material Accounting Policies) are almost certainly present in the actual filed
PDF (SEBI/Companies Act mandate them) but were not captured by whatever process produced this
.txt extraction. This is a real limitation on this Pass 1: revenue recognition policy wording,
depreciation useful-life table vs Schedule II, capitalisation threshold, impairment
assumptions, ECL matrix policy, and Ind AS 116 discount rate ASSUMPTION (the ROU asset and
lease liability AMOUNTS are captured from Notes 6/19A/19B, but the discount rate used to
compute them is not) are all NOT FOUND. Recommend the operator re-pull pages ~108-116 and
~186-190 of the source PDF directly if the policy text is load-bearing for a later stage.
🟡 Watch (corpus/extraction issue, not evidence of company non-disclosure).

---

## 1. ACCOUNTING POLICIES & CHANGES

- Full policy text: NOT FOUND IN DOCUMENT (see corpus gap above).
- First-time Ind AS adoption: this is the Group's and Company's FIRST Ind AS financial
  statements; transition date 1 April 2024, previously reported under Indian GAAP (Note 43
  consolidated / Note 42 standalone, p.137-139). Deemed-cost exemption availed for PPE at
  transition (Note 4 footnote, p.120: "the Company has availed the deemed cost exemption as
  per IND AS 101... net block carrying amount under previous GAAP has been considered as the
  gross block carrying amount"). This means FY26 is only the second year of Ind AS reporting
  and FY24 (1 April 2024) opening balances are IGAAP-derived deemed-cost numbers, not
  independently Ind-AS-measured — a normal but relevant caveat for any 3-year trend analysis.
  🟡 Watch (limits comparability of pre-FY25 figures, not a red flag).
- Revenue recognition: per Note 51 (consolidated, p.149) / Note 49 (standalone), 100% of
  revenue from contracts with customers is recognised "at a point in time" — both "Goods
  transferred at a point in time" (Rs 2,15,373.64 lakh, i.e. Rs 2,153.74 cr FY26) AND
  "Services transferred at a point in time" (Rs 978.74 lakh, Rs 9.79 cr FY26) — there is no
  over-time (percentage-of-completion) revenue recognised at all, despite the subsidiary being
  in solar EPC/generation. This narrows revenue-recognition judgment risk on timing, but sits
  oddly against the very large "Unbilled" receivables balance (Rs 135.98 cr, 48% of the
  consolidated receivables book, Note 13) — see Finding 1 discussion. 🟡 Watch.
- Deferred tax: statutory rate 25.17% both years (Note 36(a)/35, p.129/167). FY26 effective
  rate = Tax expense Rs 44.65 cr / PBT Rs 245.29 cr = 18.2%, well below statutory, driven
  mainly by "Difference Between Accounting Depreciation and Depreciation allowable as per
  Income Tax Act" (−Rs 8.33 cr effect) and "Fair Value Gain on Equity Investments" (−Rs 8.61
  cr effect) in the reconciliation (Note 36(iii), p.129). This is consistent with a capex-heavy
  manufacturer claiming accelerated tax depreciation (the deferred tax liability on PPE grew
  from Rs 1.39 cr to Rs 8.93 cr net swing per Note 22, p.128) — 🟢 Clean, normal pattern, not
  earnings management.
- No disclosed change in depreciation useful lives, capitalisation threshold, or impairment
  assumptions this year (none found in extracted schedule notes; policy text itself NOT FOUND
  per above, so a genuine "no change" cannot be fully distinguished from "not disclosed
  because the policy note is missing from this extraction"). 🟡 Watch.
- ECL matrix: allowance for expected credit losses on trade receivables is Rs NIL in every
  ageing bucket, every year, both consolidated (Note 13) and standalone (Note 12) — company
  carries zero ECL provision on a Rs 281.59 cr consolidated receivables book of which Rs 111.35
  cr is aged beyond 6 months (see Finding 1). No ECL methodology/matrix disclosed (would
  normally sit in the missing policy note). 🔴 Red Flag — a NIL provision against a rapidly
  aging book with no visible impairment methodology is a genuine provisioning-adequacy
  concern, feeds directly into the accounting-quality score.

## 2. RELATED PARTY TRANSACTIONS (Note 41 consolidated, p.135-137; Note 40 standalone, p.181-183)

Related party universe is very large: 9 KMP, 16 "enterprises where KMP has control/interest,"
4 relatives of KMP, 7 direct subsidiaries, and a further ~76 step-down subsidiaries (mostly
tiny single-project SPVs with scrambled four-letter names, e.g. "GNVP Green Infra Private
Limited," "MGJR Green Infra Private Limited" — consistent with a PM-KUSUM-style model of one
SPV per generation project) (Note 41(i), p.135-136).

Transaction table (amounts in Rs Lakh, both years shown; NOTE: the source table's column
headers for the two comparative years are internally inconsistent in the extracted text —
figures below are anchored to the note but year-attribution for a few line items could not be
verified against the original PDF table grid and should be spot-checked there):
| Nature | Party | Relationship | Magnitude (Rs Lakh, either year) |
|---|---|---|---|
| Sales | Fluidcon Engineers | Entity controlled by KMP | 2.73 / 3.42 |
| Purchase | Fluidcon Engineers | Entity controlled by KMP | 173.55 / 184.91 |
| Interest income | VM Portfolio Pvt Ltd | Entity controlled by KMP | ~347 (combined) |
| Rent expense | Manish Gupta, Vikas Jain | KMP | 2.87 combined |
| Consultancy | Mahendra Kumar Jain | Relative of KMP | 315.00 / 283.00 |
| Remuneration (all KMP) | — | KMP | 806.14 / 704.07 |
| Directors sitting fees | 6 independent directors | NEID | 9.50 / 18.25 |
| Loan given | VM Portfolio | Entity controlled by KMP | 1,082.00 |
| Loan repaid | VM Portfolio | Entity controlled by KMP | 230.00 |
| Advance received | Ganesh Decor India Pvt Ltd (GDIPL) | Formal holding co of subsidiary | 13.50 |
| Investment made | DRIPL Solar Raj Project Seven Pvt Ltd, GDIPL Solar Raj Project Pvt Ltd | Associate concerns | 0.49 each |

Outstanding balances (Note 41(iv), p.136-137): Loan & advances to VM Portfolio Rs 15.18-15.82
cr across the two years; Directors' remuneration/rent payable — small, single-digit-lakh
amounts; "Advance against capital goods — Fluidcon Engineers" Rs 182.11 lakh (Rs 1.82 cr) and
"Creditor for capital goods — Fluidcon Engineers" Rs 30.76 lakh — i.e. a KMP-controlled entity
is a capital-goods vendor to the company, in addition to being a trading counterparty.

No "arm's length" language or independent pricing benchmark is disclosed anywhere in the RPT
note (would normally sit in the missing policy note or a dedicated RPT-fairness statement).

🔴 Red Flag — Investment in promoter-controlled LLPs (Note 8, Non-Current Investments,
consolidated, p.121): the subsidiary Insolation Green Energy Private Limited (via the Group)
holds a 10% partnership interest in two LLPs — Happy Buildmart LLP and Harmony Buildestate
LLP — with the remaining 90% split 85%/5% between the promoter-director and spouse pairs
(Vikas Jain 85% / Ekta Jain 5% in Happy Buildmart; Manish Gupta 85% / Payal Gupta 5% in
Harmony Buildestate). The Group's investment per LLP is disclosed as Rs 5,00,00,000 fixed
capital + Rs 12,25,26,547 current capital in the table (Note 8, p.121) — but the accompanying
narrative text on the same page states the fixed-capital contribution as "Rs. 40,000,000"
(Rs 4 cr), a direct internal inconsistency between the table and the prose within the same
note. Total Group capital tied up across both LLPs is ~Rs 34.5 cr (per the table) or ~Rs 32.5
cr (per the narrative). Both LLPs were formed/invested into on the same date, 26 Feb 2025, at
the same registered address as the Company (C-02, Fluidcon House, New Aatish Market,
Mansarover Extension, Jaipur). No stated business rationale for these investments is given in
the extracted note. RPTs as % of FY26 revenue (Rs 2,146.02 cr consolidated): remuneration
alone is ~0.37%; the LLP capital deployment, while a balance-sheet item rather than a P&L RPT,
represents ~4.3% of FY26 net worth (~Rs 807 cr) diverted into vehicles majority-owned
personally by the two promoter-directors. This is the single most important RPT finding and
belongs in the top findings list.

Personal guarantees: BOTH promoter-directors (Vikas Jain, Manish Gupta) personally guarantee
nearly every secured borrowing facility across the parent and subsidiaries (see Section 7).

## 3. CONTINGENT LIABILITIES (Note 42 consolidated, p.137-138; Note 41 standalone, p.183-184)

| Nature | FY26 (Rs Cr) | FY25 (Rs Cr) | FY24 (Rs Cr) | Note |
|---|---|---|---|---|
| Corporate guarantees given to banks/IREDA for subsidiary borrowings | 1,654.01 | 99.68 | NIL | Note 42(i), p.137 |
| Counter-guarantee to bank | 0.51 | 13.65 | NIL | Note 42(ii), p.137 |
| GST demand under protest + Customs (junction box valuation) + ITC-on-IPO demand (3 years) | 0.98 | 0.18 | NIL | Note 42(iii), p.138 |
| Export obligation under EPCG licence (unfulfilled) | 1.05 | NIL | NIL | Note 42(iv), p.138 |
| Bank guarantee | 7.89 | NIL | NIL | Note 42(v), p.138 |
| Letter of credit issued | 40.97 | NIL | NIL | Note 42(vi), p.138 |

🔴 Red Flag — Corporate guarantee exposure of Rs 1,654.01 cr as at 31-Mar-2026 (up 16.6x from
Rs 99.68 cr FY25), entirely for facilities availed by subsidiary Insolation Green Energy
Private Limited: SBI credit facility Rs 215 cr, HDFC credit facility Rs 130 cr, Bajaj Finance
term loan Rs 50 cr, IREDA term loan Rs 1,134 cr, AU Bank credit facility Rs 48.72 cr, plus
co-borrower arrangements with two step-down SPVs (GDIPL Solar Raj Project One/Two, Rs 34.19 cr
+ Rs 17.14 cr) and a reverse guarantee from the subsidiary back to the parent for Rs 24.96 cr
(AU Bank). This single contingent-liability line is ~205% of consolidated net worth
(~Rs 807 cr, per Note 15+16) and ~77% of total consolidated assets (Rs 2,155.13 cr). It is the
direct off-balance-sheet mirror of the Rs 1,134 cr IREDA loan (see Section 7) funding the
subsidiary's capacity build-out. Not itself evidence of distress, but a material amplifier of
group-level financial risk that a Section 1B/valuation stage must weigh.

ITC-on-IPO demands (context flagged this specifically): the Rajasthan GST department has
disallowed input tax credit claimed on IPO-related expenses across THREE separate years
(FY2021-22, FY2022-23, FY2023-24), listed as three separate contingent-liability line items
(Note 42(iii), p.138) — small in absolute rupee terms (~Rs 82.6 lakh cumulative) but a
recurring, multi-year dispute specific to the company's own IPO costs, consistent with the
brief's flag. Company's assessment of likelihood is NOT separately stated for any contingent
liability item (no "remote/possible/probable" language found) — a disclosure-adequacy gap.

## Capital Commitments (Note 42(b) consolidated, p.138)

🔴 Red Flag (scale) — Estimated contracts remaining to be executed on capital account (net of
advances): Rs 901.43 cr as at 31-Mar-2026, up from Rs 152.08 cr FY25 and Rs 1.28 cr FY24 (1
April 2024). This confirms an enormous, still-in-progress capacity expansion program,
consistent with the Note 4/5 PPE and CWIP growth and the Note 20A "Creditors for Capital
Goods" jump to Rs 51.53 cr (from Rs 9.54 cr FY25). Against consolidated net worth of ~Rs 807
cr, forward capital commitments of Rs 901 cr plus contingent guarantees of Rs 1,654 cr
represent a very large multiple of the current equity base — execution and funding-completion
risk for this program should be a first-order question for the valuation stage.

## 4. TRADE RECEIVABLES (Note 13 consolidated, p.122-123; Note 12 standalone, p.166)

FLAG-CASH — This is the single most important finding of Pass 1.

Consolidated ageing (Note 13), reconstructed from the ageing schedule (bucket figures
cross-checked against the note's own reported totals; the raw extracted table interleaves a
duplicate "grand total" row mid-sequence, a known extraction artefact — the reconstruction
below sums exactly to the disclosed totals in every year, so is high-confidence despite the
underlying table's messy layout):

| Bucket | 1-Apr-2024 (Rs Cr) | 31-Mar-2025 (Rs Cr) | 31-Mar-2026 (Rs Cr) |
|---|---|---|---|
| Unbilled | 44.76 | 95.79 | 135.98 |
| Not due | 51.96 | 0.00 | 1.09 |
| < 6 months | 1.28 | 0.94 | 33.17 |
| 6 months-1 year | 5.16 | 12.38 | 95.79 |
| 1-2 years | 0.13 | 0.31 | 12.25 |
| 2-3 years | 0.25 | 0.43 | 3.07 |
| > 3 years | 0.38 | 0.24 | 0.24 |
| **Total** | **103.92** | **110.09** | **281.59** |
| **Aged > 6 months** | **5.92 (5.7%)** | **13.36 (12.1%)** | **111.35 (39.5%)** |

Receivables aged beyond 6 months grew from 5.7% of the book (1-Apr-2024) to 12.1% (FY25) to
39.5% (FY26) — both the absolute rupee amount (8.4x in one year) and the proportion of a book
that itself grew 2.56x deteriorated sharply. This is the accounting-level confirmation of the
FY26 net-profit-vs-CFO divergence flagged in the task brief (PAT Rs 200.22 cr vs CFO −Rs 73.13
cr). Allowance for expected credit losses against this book is Rs NIL in every bucket, every
year (see Section 1).

Critical localisation, from cross-checking the STANDALONE note (Note 12, p.166): parent-only
(Insolation Energy Limited) trade receivables are only Rs 48.85 cr (FY26), Rs 32.12 cr (FY25),
Rs 14.63 cr (1-Apr-2024) — a small fraction of the consolidated book — and the parent's OWN
ageing is clean: 93.9% "Not due," only ~6% (Rs 2.96 cr) aged beyond 6 months, spread evenly
across buckets, no concentration. This means essentially the ENTIRE receivables deterioration
(Rs 232.74 cr of the FY26 consolidated book, and effectively all of the >6-month overdue
balance) sits in the subsidiary Insolation Green Energy Private Limited — the solar
EPC/generation arm, not the parent's module-manufacturing business. A later stage should
treat this as a subsidiary-specific (project/EPC collection cycle, plausibly DISCOM or
government-counterparty related) problem rather than a group-wide one, though it is fully
consolidated into the numbers the market sees.

Customer concentration: per Note 46 (Operating Segments, p.144), ONE customer — Solarworld
Energy Solutions Ltd — generated Rs 265.19 cr of revenue in FY26 (>10% of total revenue from
operations; NIL in FY25). New, single-year concentration at >12% of consolidated revenue
(Rs 265.19 cr / Rs 2,146.02 cr). No ageing-by-customer disclosure to confirm whether this
customer specifically sits in the overdue buckets — flagged as a question for management.

Receivables from related parties: none disclosed in the ageing note; the Note 13 summary
table shows the entire book as "Trade Receivables from others" (Note 13, p.122).

## 5. INVENTORY (Note 12 consolidated, p.121-122; Note 11 standalone, p.165)

Consolidated total: Rs 379.05 cr (FY26), Rs 76.98 cr (FY25), Rs 73.79 cr (1-Apr-2024) — a
4.9x jump in one year, well ahead of the 60.9% revenue growth (Note 25/51 revenue figures).

Category breakdown extracted with a caveat: the source table's row/column alignment could not
be reconstructed with full confidence for FY25 vs FY26 sub-splits (recommend PDF verification
if granular composition is load-bearing downstream). The clearly anchored figures are:
Raw Materials Rs 138.02 cr (FY26) vs Rs 56.62 cr (FY25); Finished Goods Rs 183.13 cr (FY26,
the single largest category and the fastest-growing) vs Rs 12.46 cr (FY25); Traded Goods
Rs 40.18 cr (FY26); Consumables/stores, Stock-in-trade, Packing Material and Goods-in-Transit
each in single-digit-crore range both years. Valued "at lower of cost and net realisable
value" (Note 12 header, standard policy statement, no elaboration).

No inventory write-down, obsolescence provision, or slow-moving stock disclosure was found
anywhere in Note 12 or the Ind AS 2 disclosure (Note 37 consolidated / Note 36 standalone,
which only shows "inventories recognised as expense" — RM + packing consumed, Rs 1,662.13 cr
FY26 vs Rs 803.11 cr FY25 — no NRV write-down line). Given Finished Goods grew ~14.7x in one
year, the absence of any write-down/ageing disclosure for inventory is a gap worth flagging.
🟡 Watch.

RM consumed as % of revenue rose from 60.2% (FY25: Rs 803.11 cr / Rs 1,333.77 cr) to 77.4%
(FY26: Rs 1,662.13 cr / Rs 2,146.02 cr) — a large jump in the RM cost ratio; downstream margin
analysis should confirm whether this is offset elsewhere (e.g. lower "Purchase of Stock-in-
Trade" mix) or represents genuine gross-margin compression. NOT reconciled fully in this pass
(out of scope for a notes-only extraction; flagged for the financial-analysis stage).

## 6. INVESTMENTS (Note 8 consolidated, p.120-121)

- Direct subsidiaries (7): Insolation Green Energy Private Limited, Insolation Green Infra
  Private Limited, and MGVI Green Infra One/Two/Three/Four/Five Private Limited (Note 41(i)C,
  p.135-136).
- ~76 step-down subsidiaries, listed by name in Note 41(i)E (p.136), mostly single-project
  SPVs with scrambled four-letter naming (e.g. GNVP, MGPE, PRMJ, HVJN Green Infra Private
  Limited). Per Note 59 (Business Combination, p.152), several of these were acquired during
  FY25 and FY26 by paying just Rs 0.49 lakh each for a 49% VOTING interest, yet are
  consolidated as subsidiaries ("the Group obtained control over the acquiree entities"). The
  extracted text does not explain the basis of control given only 49% voting interest is
  acquired (likely a contractual/board-majority arrangement typical of PM-KUSUM-style SPV
  structuring, but NOT FOUND explicitly in the extraction). Worth a question for management.
- Investments in Associates: DRIPL Solar Raj Project Seven Pvt Ltd and GDIPL Solar Raj Project
  Private Limited, Rs 0.49 lakh each (trivial).
- Investment in LLPs: see Section 2 (related-party finding) — Happy Buildmart LLP and Harmony
  Buildestate LLP, ~Rs 32.5-34.5 cr combined, 90% owned by promoter-director families.
- Quoted equity FVTPL portfolio: a basket of listed small/microcap names (Brisk Technovision,
  Goyal Salt, Motisons Jewellers, Network People Services Technologies, Swaraj Suiting, Chavda
  Infra, Jubilant Foodworks, TAC Infosec, Suzlon Energy, Alpex Solar, Knowledge Marine and
  Engineering Works, Rattanindia Power) plus an SBI Dynamic Bond mutual fund — aggregate
  carrying value Rs 6.46 cr (FY26). No impairment recognised; carrying value = market value in
  all years (Note 8(a)/(b), p.121). This is treasury-management of surplus IPO/preferential-
  issue proceeds in listed micro/smallcap equities — a use-of-proceeds observation, not itself
  a red flag, but notable given the company's own scale and capital needs.
- No loans given to promoter entities beyond VM Portfolio (covered in RPT section); Note 9A
  also shows "Kolumbus Financial Advisory Services LLP" and "Concorde International" as
  non-related-party loan recipients (Note 9A, p.121) — relationship/purpose NOT FOUND in the
  extracted text.

## 7. BORROWINGS (Note 18A/18B consolidated, p.124-128; Note 17A/17B standalone, p.168-169)

Consolidated non-current borrowings, gross Total(A) Rs 486.32 cr (FY26), net of current
maturities Rs 468.89 cr (Note 18A, p.126). Consolidated current borrowings Total(A+B)
approximately Rs 365.91 cr (FY26) vs Rs 96.65 cr (FY25) (Note 18B, p.128) — precise per-
instrument mapping to FY26/FY25/FY24 columns could not be fully disambiguated from the
extracted table layout (recommend PDF spot-check if exact per-loan outstanding balances are
needed); the note's aggregate totals are anchored as above and are broadly consistent with the
task brief's Rs 887.91 cr FY26 / Rs 108.09 cr FY25 consolidated borrowings figures.

Standalone (parent-only) non-current borrowings, by contrast, are tiny: Total(A+B) net of
current maturities = Rs 34.25 cr (FY26) vs Rs 6.44 cr (FY25) (Note 17A, p.168) — confirming
that essentially all of the large-ticket debt (especially the IREDA facility) sits in the
subsidiary Insolation Green Energy Private Limited, not the parent, consistent with the
receivables localisation finding above.

Key instruments (both parent and subsidiary level), with security and guarantee structure
(Note 18A, p.126-128):
- IREDA (Indian Renewable Energy Development Agency) term loan to the subsidiary: SANCTIONED
  Rs 1,134 cr, repayable in 36 quarterly instalments of Rs 34.02 cr each after a 12-month
  moratorium, commencing 31-Dec-2027; interest 9.20% p.a. Secured by first charge on all
  project immovable/movable assets, project escrow accounts, and Government
  approvals/contracts; personal guarantees of both promoter-directors; corporate guarantee
  from the parent (this is the Rs 1,134 cr line inside the Rs 1,654.01 cr contingent-guarantee
  total in Section 3).
- HDFC Bank, Bajaj Finance, AU Small Finance Bank, SBI term loans across parent and
  subsidiaries for specific project sites (Bassi, Mamana, Shahpura, Gorchiya I/II, Laxman
  Nagar, Ridmalsar 1/2, Badgaon, Idana, Bhabharana, Punjpur, Richha), rates ranging 8.00%-9.96%.
- Cash Credit/WCDL from SBI and HDFC at the parent and Insolation Green Energy Pvt Ltd level.
- External Commercial Borrowing from Energy Access Relief Fund B.V. (Netherlands), personally
  guaranteed by both directors — terms/rate NOT FOUND in extracted text.

🔴 Red Flag — Title deed disclosure contradiction: Note 4 (PPE, p.120) states plainly "Title
Deeds of all Immovable properties are held in the name of Company." Note 18A (Borrowings,
p.126 consolidated and p.169 standalone) directly contradicts this: the SBI cash-credit
collateral security is described as an "Equitable mortgage of factory Land and Building
situated at Khasra No. 766/2, Village Bagwara, Tehsil-Amer Dist.-Jaipur IN THE NAME OF Sh.
Manish Gupta and Sh. Vikas Jain Director of the Company," and a second property (Jatawali
Industrial Plot) is similarly mortgaged "in the name of Sh. Manish Gupta and Sh. Vikas Jain."
Two notes within the same financial statements make directly conflicting factual claims about
whether the company's core manufacturing land is held in the company's name or personally by
its two promoter-directors. This is a material, well-anchored internal inconsistency and
belongs in the top findings.

Personal guarantees: both promoter-directors (Vikas Jain, Manish Gupta) personally guarantee
nearly EVERY secured facility disclosed across the parent and all subsidiaries — a pervasive
pattern, not a one-off (Note 18A throughout, p.126-128 and p.169-171).

Covenant breaches/waivers: NOT FOUND (no covenant-breach disclosure anywhere in the borrowings
notes). Fixed vs floating split: NOT FOUND explicitly (rates disclosed are stated as fixed
per-instrument annual rates; no separate fixed/floating classification table). 5-year
repayment schedule: NOT FOUND as a consolidated table (only per-instrument monthly/quarterly
instalment amounts and start dates, scattered across the note).

## 8. TRADE PAYABLES (Note 23 consolidated, p.128-130; Note 22 standalone, p.174)

Total FY26 = Rs 292.73 cr (MSME Rs 44.96 cr + Others Rs 247.77 cr); FY25 = Rs 72.04 cr (MSME
Rs 12.78 cr + Others Rs 59.26 cr); 1-Apr-2024 = Rs 37.42 cr (MSME Rs 12.13 cr + Others
Rs 25.28 cr). MSME dues grew 3.5x in FY26, broadly tracking the scale-up.

MSME interest disclosure (Note 23(i), p.129): "Amount of interest paid," "interest due and
payable for delay," and "further interest remaining due" are all disclosed as Rs NIL / dash in
every year — company reports no interest liability for delayed MSME payments despite the
MSME payables balance rising sharply. This is a self-assessed disclosure (not independently
verifiable from the extraction) but is at least a complete, non-evasive statement.

Ageing bucket-level reconstruction for payables could not be reliably disambiguated from the
extracted table (same reordering artefact as receivables, but the payables table's totals did
not cross-validate cleanly against my attempted bucket reconstruction) — reported here only at
the total/MSME-vs-Other level; recommend PDF verification if bucket-level payable ageing is
needed downstream.

## 9. PROVISIONS (Notes 21A/21B consolidated, p.128-129)

Gratuity and Leave Encashment provisions move in normal, modest amounts (Gratuity: Rs 30.76
lakh → Rs 39.41 lakh → Rs 83.06 lakh non-current+current combined across the three balance
sheet dates; Leave Encashment similar scale). No litigation provisions, warranty provisions,
onerous-contract provisions, or decommissioning provisions were found in the extracted notes
— NOT FOUND (may be genuinely nil for a module manufacturer, or may sit in the missing policy
note's disclosure of provisioning policy). Employee benefit funded status and actuarial
assumptions (discount rate, salary escalation, mortality table) for the defined-benefit
gratuity plan: partial figures found (Note 48 consolidated, p.145-146, "Amount recognised in
balance sheet," "Net Liability" Rs 17.32/12.50/25.76 lakh across the three dates) but the
underlying ACTUARIAL ASSUMPTIONS TABLE (discount rate, salary growth rate, attrition/
withdrawal rate, mortality table) was not reached in this pass within the available extraction
— NOT FOUND, flagged for Pass 2 to locate if present later in Note 48's continuation.

## 10. DEFERRED TAX (Note 36 consolidated, p.128-129; Note 35 standalone, p.176)

See Section 1 for the full reconciliation. Statutory rate 25.17% both years; FY26 effective
rate 18.2% (below statutory, driven by tax-depreciation timing differences and a fair-value-
gain-on-investments adjustment). Net deferred tax liability (consolidated) grew from a net
position that swung from Rs (138.82) lakh look at Note 22 lines — closing DTA/(DTL) net
figures: the note shows both DTA and DTL sub-schedules; net closing position is a liability
of roughly Rs 9.94-11.61 lakh crore-scale... the precise net closing DTL FIGURE could not be
stated with full confidence from the interleaved table (Note 22, p.128) beyond confirming the
PPE-driven DTL component rose to Rs 8.93 cr (893.22 lakh) FY26 from Rs 1.98 cr (198.15 lakh)
FY25 — a genuine, expected effect of accelerated tax depreciation on the large capex programme.
MAT credit: NOT FOUND (no MAT credit entitlement line in the deferred tax note, consistent
with the company likely paying tax under a regime without MAT, e.g. Section 115BAA — NOT
CONFIRMED, policy text missing). Unrecognised DTA: NOT FOUND explicitly (Carried Forward
Losses appear as a recognised DTA component, Rs 8.93 cr FY26, suggesting the company DOES
recognise DTA on carried-forward losses — no disclosure of any UNRECOGNISED portion or the
judgment behind recognising it).

## 11. REVENUE DETAILS (Note 25/51 consolidated, p.129-130, p.149; Note 46 segment, p.144)

Consolidated revenue from operations: Rs 2,146.02 cr FY26 vs Rs 1,333.77 cr FY25 (+60.9%
YoY). Composition: Domestic Finished Goods sales Rs 1,757.22 cr (81.9% of Total(a)), Trading
Sales Rs 364.91 cr (17.0%), Sale of Electricity Rs 4.22 cr (new line, subsidiary IPP revenue
beginning to show), Other Operational Revenue Rs 19.67 cr. 100% domestic — NIL export sales in
either year (Note 51(i), p.149), notable for a company styling itself "one of India's leading
solar panel manufacturers" with an EPCG export-obligation line still outstanding (Section 3).
Segment: single reportable segment, "Manufacturing & Trading of Solar Photovoltaic Modules"
(Note 46, p.144) — CODM identified as the CFO. Customer concentration: Solarworld Energy
Solutions Ltd, Rs 265.19 cr FY26 (>10% of revenue), NIL FY25 (Note 46(ii), p.144) — see
Finding 1 discussion. Contract liabilities (advances from customers) grew from Rs 15.94 cr
(1-Apr-2024) to Rs 26.62 cr (FY25) to Rs 56.83 cr (FY26) (Note 51(iii), p.149) — tracking scale
growth, not itself concerning. Unsatisfied performance obligations: NOT FOUND as a separate
disclosure (consistent with 100% point-in-time recognition, which typically does not require
this disclosure).

## 12. OTHER CRITICAL NOTES

- Exceptional items: NOT FOUND (no exceptional/extraordinary item line in the P&L notes
  reviewed).
- Goodwill: Rs 0.20 lakh (Note 7, p.121) — trivial, arising from a step-down acquisition; no
  impairment testing disclosure given the immateriality.
- Capital commitments: see Section 3 (Rs 901.43 cr FY26).
- Foreign currency exposure/hedging: "Net Gain on Foreign Currency Transactions" and "Exchange
  gain/(loss) on foreign currency forward contracts" appear as small other-income/expense
  lines (Note 25/26); a dedicated Ind AS 21 note exists in the standalone set (Note 38,
  standalone, p.178) — content NOT reached in this pass; External Commercial Borrowing (Note
  18A) implies FX exposure on that liability with no disclosed hedge — NOT FOUND whether
  hedged.
- Segment reporting: see Section 11 (single segment).
- Basic vs diluted EPS: Note 34, standalone (p.176) location identified but figures NOT
  reached in this pass — flagged for Pass 2. ESOP dilution: 20,00,000-option pool (max ~0.9%
  of post-exercise share count), exercise price uniformly Rs 3.80 (Rs 1 face + Rs 2.80
  premium) across all six grant tranches, against grant-date share prices of Rs 238-258 —
  i.e. options are issued deeply in-the-money at a price close to face value rather than at
  or near market (Note 44 consolidated / 43 standalone, p.141-143). This is a generous
  ESOP structure (not unusual for an SME-origin company transitioning to main board) but
  worth naming as a governance/dilution-economics observation.
- Share capital changes (Note 15, p.123-124): (a) FY22-23 IPO on BSE SME platform, 58,32,000
  shares of Rs 10, Rs 5.83 cr (matches brief); (b) face-value split Rs 10 → Rs 1, effective
  24-Jan-2025 record date, approved at EGM 5-Dec-2024; (c) preferential issue 11-Dec-2024,
  12,02,300 shares of Rs 10 at Rs 3,277 premium, Rs 395.20 cr (39,519.60 lakh) — exact match to
  brief; (d) ESOP issue of 51,625 shares of Rs 1 at Rs 2.80 premium, Rs 1,96,175 — matches
  brief, but the note DATES this issue "14/11/2026" (Note 15(h), p.124), which is AFTER both
  the FY26 year-end (31-Mar-2026) and the auditor's report signing date (25-May-2026) — an
  evident typo (should almost certainly read 14/11/2025), but a genuine internal-date
  inconsistency in the notes as filed. (e) A 1:1-ish bonus issue in FY21-22 of 1,25,00,000
  shares "for consideration other than cash" (Note 15(g)) — standard bonus-share language, not
  a red flag on its own. Promoter shareholding declined from 69.91% (1-Apr-2024) to 65.94%
  (FY25) to 65.92% (FY26) — modest dilution from the preferential issue and ESOP, not alarming.
- CSR (context flagged as an item to check): required Rs 10.42 lakh FY26 (2% of average net
  profit under s.135(5), less a Rs 2.22 lakh set-off), actual spend Rs 10.50 lakh — fully
  compliant, no shortfall (found in the Board's Report annexure rather than the financial
  notes themselves; the amount is immaterial and lags the FY26 profit surge because it is
  based on average PRIOR-year profits per the statutory formula). 🟢 Clean.
- Direct debits/credits to reserves bypassing P&L: dividend paid FY25 (Rs 2.20 cr, Note 16(c)
  Retained Earnings movement, p.124) is the only direct reserve movement found; no unusual
  bypass items identified. NIL dividend declared for FY26 (Note 58(i) standalone, p.187).
- Government grants/incentives: RIPS (Rajasthan Investment Promotion Scheme) Subsidy
  Receivable appears in Other Current Assets (Note 11B, p.122) and "RIPS Subsidy" / "Subsidy
  Received" appear as modest Other Income lines (Note 26, p.130) — amounts in the Rs 40-76 lakh
  range, not material. No distinct PLI (Production Linked Incentive) scheme line item found in
  the financial notes — NOT FOUND (ALMM references in the document are all in the MD&A/
  business sections as a regulatory listing requirement for solar module empanelment, not a
  cash subsidy, and are outside the notes-to-accounts scope of this pass).
- Auditor: Badaya & Co, Jaipur (FRN 006395C), signed both opinions 25-May-2026. BOTH the
  consolidated and standalone auditor's reports state, verbatim in substance, that the auditor
  observed NO Key Audit Matters ("We have not observed anything which falls under this" /
  "We have not observed some audit matters which falls under this," p.114 and p.166). No
  Emphasis of Matter, qualification, or going-concern uncertainty paragraph was found in
  either opinion. AGM Notice Item 4 proposes replacing Badaya & Co with ARS & Company
  (FRN 009406C) for a fresh 5-year term from this AGM, i.e. the outgoing auditor who reported
  zero KAMs is being replaced concurrently with the year the company scaled 5x on several
  balance-sheet metrics and migrated to the main board. 🟡 Watch — flagged as a question for
  management/governance point, not asserted as improper.
- Consolidation scope / subsidiaries: 7 direct + ~76 step-down subsidiaries (see Section 6);
  several step-down entities consolidated on the basis of a 49% VOTING interest acquired for
  a token Rs 0.49 lakh consideration each (Note 59, p.152) — basis of control not elaborated
  in the extracted text (NOT FOUND).
- Going concern language: NONE found anywhere in the extraction (no management going-concern
  qualifier, no auditor going-concern paragraph).
- Restatements: prior-year figures are described as "Regrouped, Recast, Reclassified... to
  ensure comparability" (Note 52 consolidated / Note 54 standalone, p.130/177) — standard
  boilerplate; no specific restated line item or quantified restatement impact identified in
  this pass (would need Pass 3's pattern re-read against the primary statements to confirm
  whether any specific number changed vs a prior filing, which is not available in this
  single-AR corpus in any case since there is no separate prior-year standalone filing to
  compare against).

---

## DRAFTING-QUALITY PATTERN (cuts across categories, worth naming as one item)

Multiple internal labelling/dating errors recur across the notes, individually immaterial but
collectively a signal of loose review discipline in note preparation:
1. The "Consolidated" Statement of Changes in Equity is headed "STANDALONE STATEMENT OF
   CHANGES IN EQUITY" (p.119) — confirmed mislabelled by its own footer text, "The
   accompanying notes are an integral part of these Consolidated financial statements."
2. The section header "NOTES ON STANDALONE FINANCIAL STATEMENTS" (p.123) precedes what are
   actually the CONSOLIDATED schedule notes 10 onward (confirmed by the presence of a
   Non-Controlling-Interest note, Note 17, which only exists in consolidation).
3. Note 25 is titled "Other Income" (p.129) but its content is Revenue from Operations; the
   genuine Other Income note is the following Note 26, also titled "Other Income" (p.130) —
   i.e. one of the two notes has the wrong title.
4. The ESOP note (Note 15(h), p.124) dates a share issue "14/11/2026," after both the FY26
   year-end and the audit signing date — an evident typo.
5. The LLP investment note (Note 8, p.121) shows Rs 5,00,00,000 fixed capital in its table but
   Rs 40,000,000 in its accompanying narrative sentence for the same investment.
🟡 Watch — named once here rather than five separate times; feeds the "consistency/disclosure
transparency" dimension of the accounting-quality score in Pass 3.

---

# PASS 1 SUMMARY

Read every numbered note in both the CONSOLIDATED (Notes 4-59) and STANDALONE (Notes 4-58)
financial statements, cross-checking the task brief's screener-sourced figures against the AR
and confirming they are consolidated-basis numbers. The Material Accounting Policies (Notes
1-3) are referenced on the face of both balance sheets but their full text is absent from this
extraction across all 200 pages — flagged as a corpus gap, not a company disclosure failure,
and named wherever it limited a specific finding (revenue recognition detail, depreciation
policy, ECL methodology, Ind AS 116 discount rate).

The dominant story in the notes is a company mid-way through a very large, debt-funded
capacity expansion (Rs 901 cr of capital commitments, a Rs 1,134 cr IREDA facility at the
subsidiary, Rs 1,654 cr of parent corporate guarantees backing subsidiary debt) layered on top
of a solar-module manufacturing base that grew revenue 61% but saw its working-capital cycle
deteriorate sharply — and that deterioration is fully traceable, via the standalone-vs-
consolidated cross-check, to the EPC/generation subsidiary rather than the parent's own
manufacturing receivables. Governance-adjacent findings (the promoter-controlled LLP
investment, the title-deed contradiction, the pervasive personal guarantees, zero Key Audit
Matters from an auditor being replaced this year) form a second cluster that a valuation stage
should weigh alongside the growth story, not net against it.

## TOP 10 MOST SIGNIFICANT FINDINGS (ranked by investor importance)

1. 🔴 **Receivables ageing collapse, entirely at the subsidiary.** Consolidated receivables
   aged >6 months rose from 5.7% (1-Apr-2024) to 12.1% (FY25) to 39.5% (Rs 111.35 cr of
   Rs 281.59 cr, FY26); standalone parent-only book is clean (93.9% not due). (Note 13, p.122-
   123; Note 12 standalone, p.166.) Directly explains the PAT-vs-CFO divergence.
2. 🔴 **Corporate guarantee exposure of Rs 1,654.01 cr (FY26), up 16.6x from Rs 99.68 cr
   (FY25)** — parent guaranteeing subsidiary debt including the Rs 1,134 cr IREDA facility;
   ~205% of consolidated net worth. (Note 42(i), p.137.)
3. 🔴 **Capital commitments of Rs 901.43 cr (FY26)**, up from Rs 152.08 cr (FY25) and Rs 1.28
   cr (FY24) — confirms a capacity build-out of a scale that dwarfs current net worth
   (~Rs 807 cr). (Note 42(b), p.138.)
4. 🔴 **Title deed contradiction between notes.** Note 4 states all immovable property title
   deeds are "held in the name of Company"; Note 18A describes the same factory land as
   mortgaged "in the name of Sh. Manish Gupta and Sh. Vikas Jain" personally. (Note 4, p.120
   vs Note 18A, p.126/169.)
5. 🔴 **Investment of ~Rs 32.5-34.5 cr in two promoter-controlled LLPs** (Happy Buildmart LLP,
   Harmony Buildestate LLP) where the two promoter-director families hold 90% of the
   partnership interest and the Group only 10%; internal figure inconsistency (table vs
   narrative) within the same note. (Note 8, p.121.)
6. 🟡 **Zero ECL provision against a rapidly aging Rs 281.59 cr receivables book**, with no
   disclosed impairment methodology anywhere in the extraction. (Note 13, p.122-123.)
7. 🟡 **Self-disclosed Schedule III ratio variances all point the same direction**: Debt/Equity
   +481% (0.18x→1.03x), Inventory turnover −46.8%, Trade receivable turnover −33.4%, Trade
   payable turnover −45.2%, ROCE −23.5% (25.15%→19.25%) — company's own explanations are
   generic ("due to increase in X"). (Note 53, p.150-151.)
8. 🟡 **New customer concentration**: Solarworld Energy Solutions Ltd = Rs 265.19 cr (12.4% of
   FY26 revenue), Nil in FY25. (Note 46, p.144.)
9. 🟡 **Zero Key Audit Matters reported** by the outgoing auditor (Badaya & Co) in both
   consolidated and standalone opinions, for a company whose inventory grew 4.9x, receivables
   2.6x, and guarantee exposure 16.6x in one year; auditor is being replaced this AGM.
   (p.114/166; AGM Notice Item 4.)
10. 🟡 **Material Accounting Policies (Notes 1-3) text absent from the entire 200-page
    extraction** — a corpus gap limiting assessment of revenue-recognition wording,
    depreciation policy vs Schedule II, ECL matrix, and Ind AS 116 discount rate; recommend
    direct PDF verification if load-bearing downstream.

Also logged but outside the top 10: the ITC-on-IPO GST demands spanning three years (~Rs 0.83
cr cumulative, Note 42(iii)); the drafting-quality pattern (five separate labelling/dating
errors across notes); the ~76 step-down SPV subsidiaries consolidated via 49%-voting-interest
acquisitions with control basis unexplained (Note 59); the deeply in-the-money ESOP pricing
(Note 44); and 100% domestic, 100% point-in-time revenue recognition despite a large unbilled
receivables component (Note 51).
