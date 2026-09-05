# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 1: FULL EXTRACTION
Company: Kabra Extrusiontechnik Ltd (KABRAEXTRU) | Run date: 2026-09-05
Source: Annual Report FY2025-26 (`Annual_Report_2026.txt`/`.pdf`, 170 PDF pages).
Standalone Financial Statements = printed p.55-111 = PDF p.57-113. Consolidated
Financial Statements = printed p.112-167 = PDF p.114-169. Notes are in ₹ Lakhs
in the source (company's stated rounding policy); this report converts to ₹
Crores (Lakhs ÷ 100) per pipeline instruction and shows the lakh figure in
parentheses on first use for traceability. Prior-year AR (FY2024-25) cited as
"AR FY25" where used. Ratings: 🟢 Clean | 🟡 Watch | 🔴 Red Flag.

═══════════════════════════════════════════════════════════════════
## 1. ACCOUNTING POLICIES & CHANGES
═══════════════════════════════════════════════════════════════════

**Standalone (Note 1, PDF p.72-79).** Ind AS basis, historical cost except
FVTPL/FVTOCI instruments and defined-benefit plan assets. Rounding to nearest
lakh (Note 1(c), PDF p.72).

- Depreciation: Straight Line Method, useful lives DIFFER from Schedule II:
  Plant & Equipment 2-15 years, Building 20-30 years, Furniture & Fixtures
  2-15 years, Vehicles 8-10 years, Office Equipment 2-8 years, Computer 2-3
  years (PDF p.72). Wide bands (e.g. plant 2-15 years) give management broad
  discretion; no separate note quantifies the P&L impact of this deviation
  from Schedule II norms. 🟡 Watch.
- Capitalisation threshold: assets ≤₹5,000 fully depreciated in year of
  purchase (PDF p.72).
- Impairment testing: qualitative policy present (value in use vs fair value
  less cost to sell) but NO quantified growth/discount-rate assumptions are
  disclosed anywhere in the standalone or consolidated notes for any
  cash-generating unit. NOT FOUND IN DOCUMENT.
- ECL: trade receivables use the Ind AS 109 "provision matrix" practical
  expedient (PDF p.76); the matrix itself (rates by ageing bucket) is NOT
  separately tabulated, but implied rates can be derived from the Note 9
  ageing/provision table (see Section 4 below).
- Ind AS 116 leases: ROU assets and lease liabilities recognised; discount
  rate not separately disclosed as a stated %, but the lease liability
  reconciliation shows Accretion of Interest ₹0.4465 Cr (44.65 lakh) on an
  opening balance of ₹2.4308 Cr (243.08 lakh) (Note 40, PDF p.107),
  implying an effective rate in the high-teens % — high for a lease discount
  rate and worth a management question. 🟡 Watch.
- First-time adoptions: Ind AS 117 (Insurance Contracts) and Ind AS 116
  sale-and-leaseback amendments noted as evaluated with "no impact" (Note
  1(u), PDF p.79). No new standard adoption with quantified impact this year.
- **DATING DEFECT (both standalone and consolidated):** the standalone Basis
  of Preparation paragraph (Note 1(a), PDF p.72) states the financial
  statements comprise "the Statement of Profit and Loss for the year ended
  31 March 2025" (should read 2026) while the adjoining Balance Sheet and
  Cash Flow references correctly say 2026 — an internally inconsistent
  sentence. The CONSOLIDATED version of the same paragraph (Note 1(a), PDF
  p.127) is entirely unrevised from the prior year: it states the financial
  statements comprise the Balance Sheet, P&L, Cash Flow and SOCE all "as at
  /for the year ended 31 March 2025" and records Board approval as "16th
  May, 2025" — both wrong (should be 31 March 2026 and 28 May 2026,
  matching the signature block at the end of the same note, which correctly
  reads 28 May 2026). This indicates the consolidated accounting-policy
  section was not reviewed/updated from the FY25 report before signing. 🟡
  Watch (drafting/QC quality, not a numeric misstatement).
- Basis of Consolidation (Note 1(d), PDF p.127) opens "The consolidated
  financial statements relate to Kabra Extrusion Technik Limited ('the
  Company') and its Joint Ventures" — omitting subsidiaries from that
  opening sentence even though the same paragraph goes on to describe full
  consolidation of subsidiaries and equity accounting for JVs, and the
  balance sheet/notes confirm both subsidiaries (Varos Technology, Kabra
  Energy) ARE fully consolidated (their standalone "Investment" carrying
  values disappear from consolidated Note 3, replaced by consolidated
  PPE/intangibles/P&L that are larger than standalone by amounts matching
  Varos's AOC-1 figures). 🟡 Watch — sloppy drafting, not a scope error in
  substance.

═══════════════════════════════════════════════════════════════════
## 2. RELATED PARTY TRANSACTIONS (Note 39 standalone PDF p.104-107;
   Note 39 consolidated PDF p.161-164)
═══════════════════════════════════════════════════════════════════

Related parties with control: Varos Technology Pvt Ltd (subsidiary, 100%),
Kabra Energy Pvt Ltd (subsidiary, 100%, formerly Kolsite Energy), Kabra
Mecanor Belling Technik Pvt Ltd (JV, 69.98%), Penta Auto Feeding India Ltd
(JV, ceased 6-Feb-2025). Promoter entities: Kolsite Corporation LLP,
Plastiblends India Ltd, Maharashtra Plastic & Industries.

**Standalone transactions, FY26 vs FY25 (₹ Cr, converted from lakh):**
| Party | Nature | FY26 | FY25 | YoY % |
|---|---|---|---|---|
| Varos Technology (subsidiary) | Investment in CCD | 12.5225 | 9.3425 | +34.0% |
| Varos Technology | Purchase of goods & services | 0.1261 | 3.8899 | -96.8% |
| Varos Technology | Reimbursement income | 0.0018 | 0.0263 | -93.2% |
| Kabra Energy (subsidiary) | Purchase/sale of goods & svcs, reimb. | 0.0019 | 0.0021 | -9.5% |
| Kabra Mecanor Belling Technik (JV) | Rent income | 0.0240 | 0.0240 | 0.0% |
| Kolsite Corporation LLP (promoter) | Rent income | 0.5973 | 0.5274 | +13.3% |
| Kolsite Corporation LLP | Dividend paid | 0.00 | 1.3401 | n/a (no div FY26) |
| Plastiblends India Ltd (promoter, cross-holding) | Sales of goods & services | 1.2262 | 1.1440 | +7.2% |
| Plastiblends India Ltd | Dividend received | 0.3441 | 0.6094 | -43.5% |
| Plastiblends India Ltd | Dividend paid | 0.00 | 0.2896 | n/a |
| Maharashtra Plastics & Ind. | Sales of goods & services | 0.2610 | 0.3211 | -18.7% |

The 96.8% YoY drop in standalone purchases from Varos (₹3.89 Cr → ₹0.126 Cr)
is a large unexplained swing in intercompany sourcing that is not narrated
anywhere in the notes. 🟡 Watch — question for management.

**Investment/CCD balances (standalone, Note 39D(iii)/(iv), PDF p.106):**
Varos equity investment ₹0.80 Cr (unchanged); CCD outstanding rose from
₹9.3425 Cr (FY25) to ₹12.5225 Cr (FY26), i.e. the company advanced a further
₹3.18 Cr to Varos via CCD in FY26 on top of the ₹8.00 Cr zero-rated CCD and
₹1.3425 Cr rated-CCD base already in place. Cumulative equity+CCD exposure to
Varos is now ₹13.3225 Cr (Note 3, PDF p.85).

**Debit/credit balances of note (standalone, PDF p.106):** VTRO Motors
Private Limited (an "other related party" with "no transactions in the
current year") had a credit balance outstanding of ₹1.497 Cr at FY25 that is
NIL at FY26 — settled or written off with no note explaining which. 🟡 Watch.

**Compensation to KMP:** short-term employee benefits fell to ₹3.7939 Cr
(FY26) from ₹6.5307 Cr (FY25), -41.9%; sitting fees rose ₹0.207 Cr from
₹0.147 Cr (+40.8%) (Note 39E, PDF p.106).

**Consolidated RPT note (PDF p.161-164) disclosure defect:** the consolidated
RPT balance tables (Debit/Credit Balance Outstanding, D(i)/D(ii)) still list
"Varos Technology Private Limited" and "Kabra Energy Private Limited" under
"Subsidiary" with non-zero balances (e.g. Varos debit balance ₹0.414 Cr FY26,
Kabra Energy debit ₹0.0034 Cr FY26). Since both are fully consolidated
subsidiaries, their balances with the parent should be eliminated in full on
consolidation and should NOT appear as related-party balances in the
CONSOLIDATED financial statements under Ind AS 24/Schedule III practice —
this reads like the standalone note table was copied into the consolidated
notes without stripping intra-group eliminations. 🟡 Watch (disclosure
quality, same "stale copy" pattern as Section 1 dating defect).

No RPT loans to promoters/directors disclosed (Note 46(a) standalone/
consolidated, "no loans or advances in the nature of loan to promoters,
directors, KMPs" — PDF p.110/168). No new related parties created this year;
Penta Auto Feeding India Ltd ceased to be a related party 6-Feb-2025 (sold,
Note 32 exceptional item, gain ₹8.4898 Cr in FY25).

═══════════════════════════════════════════════════════════════════
## 3. CONTINGENT LIABILITIES (Note 41(a), standalone PDF p.108-109,
   consolidated PDF p.165)
═══════════════════════════════════════════════════════════════════

| Item | FY26 (₹ Cr) | FY25 (₹ Cr) | YoY % |
|---|---|---|---|
| Bank guarantees & counter-guarantees (LC) | 21.8887 | 11.3297 | +93.2% |
| Disputed income tax demand | 1.2776 | 1.2776 | 0.0% |
| Service tax & excise disputes | 0.1211 | 0.1211 | 0.0% |
| GST matters under dispute | 1.7496 | 0.0924 | +1793.5% |
| Custom duty matter under dispute | 0.0143 | 0.0143 | 0.0% |
| **Total** | **25.0513** | **12.8351** | +95.2% |

Standalone/consolidated figures are identical (no subsidiary-level
contingencies). Net worth (standalone total equity) at FY26 = ₹447.3769 Cr;
total contingent liabilities = 5.60% of net worth (not >10%, no single item
disclosure trigger on that test alone). Excluding bank guarantees (routine
LC/BG for order execution, not a tax dispute), tax-related contingencies are
just ₹3.1626 Cr = 0.71% of net worth — immaterial. The GST dispute growth
(+1793%) and bank-guarantee near-doubling are both 🟡 Watch items on trend,
not magnitude. Tax disputes are pending before appellate authorities;
management/tax advisors expect no material adverse effect (standard
language, PDF p.109/165). No guarantees issued FOR subsidiaries are
disclosed (Note 39C standalone shows "Issuance of Corporate Guarantee" line
for Varos Technology with NIL value both years) — NOT a live guarantee.

**Capital commitments (Note 41(b)):** ₹31.7738 Cr (FY26) vs ₹1.4342 Cr
(FY25) — a +2115.6% increase. No narrative in the notes explains which
segment/project this commitment relates to (not disclosed by segment). Given
the PPE addition pattern (Plant & Equipment additions of ₹62.83-63.03 Cr in
the current year, Note 2A) and the Executive Chairman's letter (non-note
source) references to Geon capacity, this large jump most plausibly relates
to further Battery Division capacity, but the notes themselves do not say
so. 🔴 Red Flag — large forward capital commitment disclosed with zero
narrative context, in a year the same division lost ₹43.35 Cr.

═══════════════════════════════════════════════════════════════════
## 4. TRADE RECEIVABLES (Note 9, standalone PDF p.87-88, consolidated
   PDF p.142-143)
═══════════════════════════════════════════════════════════════════

Standalone/consolidated gross and provision figures are effectively
identical (Varos contributes negligible receivables).

| Ageing bucket | FY26 gross (₹ Cr) | FY26 provision (₹ Cr) | FY25 gross (₹ Cr) | FY25 provision (₹ Cr) |
|---|---|---|---|---|
| Not due | 41.2845 | 0.00 | 44.3787 | 0.00 |
| <6 months | 3.7988 | 0.00 | 12.5632 | 0.00 |
| 6mo-1yr | 1.1541 | 0.2436 | 0.6336 | 0.0859 |
| 1-2 yr | 4.7176 | 0.9696 | 20.3730 | 2.9226 |
| 2-3 yr | 20.2156 | 4.7699 | 11.4622 | 2.7375 |
| >3 yr | 19.3536 | 4.5513 | 9.5268 | 2.2746 |
| **Total** | **90.5243** | **10.5344** | **98.9376** | **8.0206** |
| Net receivables | **79.9899** | | **90.9170** | |

- Gross receivables DOWN 8.5% YoY, but the ageing mix deteriorated sharply:
  the >3-year bucket nearly DOUBLED (₹9.53 Cr → ₹19.35 Cr, +103.2%) and the
  2-3 year bucket also grew (+76.4%), while the 1-2yr bucket collapsed
  (-76.8%) — consistent with a cohort of old receivables ageing further
  rather than being collected or written off. 🔴 Red Flag.
- ECL provision as % of gross rose from 8.1% (FY25) to 11.6% (FY26).
  Implied ECL rates by bucket (computed, not separately disclosed as a
  matrix): 6mo-1yr ≈21.1% (FY26) vs 13.6% (FY25); 1-2yr ≈20.6% vs 14.3%;
  2-3yr ≈23.6% vs 23.9%; >3yr ≈23.5% vs 23.9%. The >6-months-overdue
  cohort (6mo-1yr + 1-2yr + 2-3yr + >3yr) = ₹45.44 Cr = 50.2% of gross
  receivables at FY26 (vs ₹42.00 Cr = 42.4% at FY25) — receivable quality
  is deteriorating. 🔴 Red Flag → feeds FLAG-CASH.
- Receivable days (computed from Note 22 revenue ₹450.9983 Cr FY26 /
  ₹476.8469 Cr FY25 and average trade receivables): trade receivables
  turnover ratio disclosed directly in Note 43 as 5.22x (FY26) vs 4.97x
  (FY25) (+5.2%) — i.e. days IMPROVED slightly (≈70 days FY26 vs ≈73 days
  FY25) even though the ageing mix worsened; this is consistent with a
  shrinking, but proportionally older, receivables book.
- **HEVPL (Hero Electric Vehicle Pvt Ltd) exposure — disclosure not
  updated for FY26.** Note 9 states verbatim: "As at March 31, 2025, the
  Company has outstanding trade receivables amounting to ₹3,039 lakhs
  [₹30.39 Cr] from Hero Electric Vehicle Pvt. Ltd. (HEVPL). Pursuant to an
  order dated December 20, 2024, the Hon'ble NCLT has admitted an
  application to initiate corporate insolvency resolution process (CIRP)
  against HEVPL... the Company has recognized a provision for doubtful
  debts pertaining to receivables from HEVPL... additionally... warranty
  provisions... reversed." (Note 9, PDF p.87-88 standalone / p.142-143
  consolidated — IDENTICAL wording in both, and identical to the wording in
  the FY25 AR, Note 9). The FY26 annual report gives NO update on the
  current (31 March 2026) HEVPL balance, the CIRP's progress, additional
  provisioning during FY26, or any write-off/recovery. Given a ~₹30 Cr
  exposure to a company in insolvency proceedings, the absence of a current
  status update is a material disclosure gap. 🔴 Red Flag.
- Trade receivables from related parties: cross-referenced to Note 38
  (standalone)/39 (consolidated) — outstanding debit balances are small
  (Plastiblends ₹0.1082 Cr, Kabra Mecanor ₹0.4092 Cr) and not separately
  aged.
- Foreign-currency trade receivables (Note 34.3(c)(i), PDF p.99): USD 1.94
  lakh (₹1.8135 Cr), EUR 0.16 lakh (₹0.1695 Cr) at FY26, DOWN from USD 10.60
  lakh (₹9.0593 Cr) at FY25 — export receivables collapsed 89.4%
  standalone-currency-equivalent (consistent with the export revenue decline
  discussed under Section 11).

═══════════════════════════════════════════════════════════════════
## 5. INVENTORY (Note 7, standalone PDF p.87, consolidated PDF p.141)
═══════════════════════════════════════════════════════════════════

**Standalone:**
| Category | FY26 (₹ Cr) | FY25 (₹ Cr) | YoY % |
|---|---|---|---|
| Raw materials | 164.5094 | 178.8583 | -8.0% |
| Work-in-progress | 120.8714 | 111.2895 | +8.6% |
| **Total** | **285.3808** | **290.1477** | -1.6% |

**Consolidated:** Raw materials ₹165.2880 Cr, WIP ₹120.8714 Cr, Total
₹286.1594 Cr (FY26) vs ₹290.9127 Cr (FY25), -1.6%. The ₹0.78 Cr gap to
standalone raw materials is Varos's own inventory.

No separate "Finished Goods" line is disclosed by the company (its
presentation nets FG and WIP into "Changes in Inventories of Finished Goods
and Work-in-progress," Note 25, and the Note 7 balance-sheet table shows
only Raw Materials + WIP — i.e., the company appears to carry NO finished
goods inventory of its own on the balance sheet, consistent with a
build-to-order machinery business). Revenue fell 5.6% (₹450.9983 Cr vs
₹476.8469 Cr standalone) while WIP inventory GREW 8.6% — WIP is growing
faster than revenue, a mild efficiency/execution-pace flag. 🟡 Watch.

Inventory turnover ratio (Note 43): 1.55x (FY26) vs 1.79x (FY25), -13.1% —
inventory days lengthened (≈235 days FY26 vs ≈204 days FY25 on a sales-based
turn). No inventory write-down/obsolescence amount is separately disclosed
in the notes (inventory is carried at "lower of cost and NRV" per policy,
Note 1(e), but no line item for write-downs taken this year is shown). NOT
FOUND IN DOCUMENT (write-down amount). This is itself a gap given the WIP
growth above sales growth and the Battery Division's operating history.

═══════════════════════════════════════════════════════════════════
## 6. INVESTMENTS (Note 3, standalone PDF p.85-86, consolidated
   PDF p.140-141; AOC-1, PDF p.23)
═══════════════════════════════════════════════════════════════════

**Subsidiaries and JV (AOC-1 Form, printed p.21 / PDF p.23):**

| Entity | % holding | Share capital (₹ Cr) | Reserves & Surplus (₹ Cr) | Total Assets (₹ Cr) | Total Liab. (₹ Cr) | Turnover (₹ Cr) | PBT (₹ Cr) | PAT (₹ Cr) |
|---|---|---|---|---|---|---|---|---|
| Varos Technology Pvt Ltd | 100% | 0.01 | (5.5717) | 7.9890 | 0.8910 | 0.1784 | (3.5400) | (2.9149) |
| Kabra Energy Pvt Ltd | 100% | 0.001 | (0.0081) | 0.0000 | 0.0071 | 0.00 | (0.0019) | (0.0019) |
| Kabra Mecanor Belling Technik Pvt Ltd (JV) | 69.98% | 1.00 | 0.5173 | 0.9613 | 0.4786 | 0.00 | (0.00891) | (0.00891) |

Varos Technology (Pune; IoT/website/multimedia services per corporate
overview, Note "Corporate overview" PDF p.127) has accumulated negative
reserves of ₹(5.5717) Cr against share capital of just ₹0.01 Cr — i.e. it is
fully insolvent on a stand-alone-entity basis and is kept solvent only
because the parent has funded it via ₹13.3225 Cr of cumulative equity + CCD
investment (Note 3, PDF p.85; incorporated FY22 per AR FY25 MD&A). Turnover
of ₹0.1784 Cr against a loss of ₹2.9149 Cr this year alone means Varos burnt
roughly 16x its own revenue in losses in FY26. 🔴 Red Flag.

Kabra Energy Pvt Ltd (formerly Kolsite Energy) is a dormant shell: nil total
assets, nil turnover, both years. Investment carrying value is ₹0.001 Cr.

**Non-current investments (standalone Note 3, PDF p.85-86):**
| Category | FY26 (₹ Cr) | FY25 (₹ Cr) |
|---|---|---|
| Equity instruments (incl. Plastiblends, Varos, Kabra Mecanor) | 18.2352 | 27.3367 |
| Debentures (CCD in Varos) | 12.5225 | 9.3425 |
| Bonds (IRFC tax-free) | 0.2610 | 0.2610 |
| **Total** | **31.0187** | **36.9402** |

**Plastiblends India Ltd (promoter cross-holding, FVOCI, quoted):** carrying
value fell from ₹25.8358 Cr (1,433,967 shares) to ₹16.7343 Cr (1,376,519
shares) — a ₹9.10 Cr decline, driven by BOTH a reduction in unit holding
(57,448 shares sold — the "gain on sale of 122,402 shares" note in the SOCE
refers to a different/prior transaction, PDF p.124 footnote — reconcile the
share-count discrepancy: SOCE footnote says 122,402 shares sold but the Note
3 unit roll-forward implies ~57,448 shares reduced; NOT FOUND IN DOCUMENT —
an explicit reconciling schedule) and a market price decline on the retained
stake. This is an unrealised loss routed through OCI (Retained Earnings
"Gain on Equity Instruments... transferred" ₹1.221 Cr, Note 15) rather than
P&L, per FVOCI election — a legitimate but P&L-flattering classification
choice for a quoted equity stake held for strategic/promoter-group reasons.
🟡 Watch.

**Current investments (Note 8, PDF p.87):** Mutual funds fell from ₹53.4926
Cr to ₹22.5874 Cr (-57.8%) — liquid buffer drawn down by ₹30.91 Cr during
the year, primarily funding continued capex and rising working capital
needs (see Section 7).

**Consolidated-only difference (Note 3, PDF p.140):** Kabra Mecanor Belling
Technik (JV) equity carrying value under equity method is ₹0.3363 Cr (FY26)
vs ₹0.3425 Cr (FY25) — reflects JV's own tiny loss share. Varos does not
appear as a separate "investment" line in consolidated Note 3 (fully
consolidated; its net assets, not investment cost, flow through).

**Goodwill (consolidated balance sheet line item, no note number assigned,
PDF p.121):** ₹0.8363 Cr, UNCHANGED both years. No dedicated note explains
its origin (presumably arising on Varos acquisition, FY22) and NO impairment
test disclosure (assumptions, discount rate, growth rate, headroom) is given
anywhere despite the stated accounting policy that goodwill is tested at
least annually for impairment (Note 1(d)/1(e)). Given Varos's ongoing losses
and negative net worth, an impairment test would ordinarily be expected to
be evidenced. NOT FOUND IN DOCUMENT. 🟡 Watch.

No new investment entities added this year (Penta Auto Feeding India Ltd
ceased as a JV in FY25, already reflected). No ICDs or loans given to any
external party (Note 46(a): "not granted any loans/advances in the nature of
loans to promoters, directors, KMPs and related parties").

═══════════════════════════════════════════════════════════════════
## 7. BORROWINGS (Note 17/17(a), standalone PDF p.90/92-93,
   consolidated PDF p.147)
═══════════════════════════════════════════════════════════════════

| Item | FY26 (₹ Cr) | FY25 (₹ Cr) | YoY % |
|---|---|---|---|
| Long-term secured bank loan (gross) | 0.1689 | 5.6249 | -97.0% |
| — of which current maturity | 0.1106 | 5.4560 | -98.0% |
| Long-term borrowing (net of current maturity) | 0.0583 | 0.1689 | -65.5% |
| Short-term unsecured | 0.00 | 30.00 | -100% |
| Short-term secured | 140.9164 | 90.1615 | +56.3% |
| **Total borrowings (Gross Debt, Note 35)** | **141.0853** | **125.7864** | +12.2% |

- Term loan (Pune land & building, first charge) reduced to ₹0 Cr from
  ₹5.35 Cr (Note 17(ii)) — fully repaid/matured during the year.
- Short-term unsecured borrowing of ₹30 Cr (FY25) was fully repaid and
  REPLACED with additional secured working-capital borrowing — the entire
  incremental debt need this year was met via secured facilities
  (hypothecation of all present/future movable assets and book debts, Note
  17(i)) rather than unsecured lines. This is consistent with (though the
  notes do not explicitly state) reduced lender willingness to extend
  unsecured credit — worth cross-checking against the CRISIL downgrade
  (13-May-2026, per company memory/corporate governance report, outside
  notes scope) at Halt 1. 🟡 Watch.
- Working capital loans are payable ON DEMAND (Note 17(i)) — standard for
  Indian CC/OD facilities but means the ₹140.92 Cr secured short-term book
  is technically callable at any time.
- No covenant breach or waiver is disclosed. Note 17(ii)/(iii) explicitly
  states "There was no default continuing or otherwise as at the Balance
  Sheet date" and Note 46(k) states the company "has not been declared
  wilful defaulter by any bank or financial institution." No covenant
  RATIOS or covenant terms are quantified anywhere in the notes (e.g. no
  DSCR/leverage covenant threshold disclosed) — NOT FOUND IN DOCUMENT.
- Interest rate profile (Note 34.3(c)(ii)): borrowings are classified as
  "Fixed rate instruments" for the sensitivity table, yet a "±50bp interest
  rate sensitivity" table is also given (impact ₹0.7054 Cr FY26) — an
  internal inconsistency (fixed-rate debt should have zero rate
  sensitivity); more likely the CC/OD book floats with bank MCLR/repo and
  the "fixed rate" label is a template error carried from a boilerplate
  disclosure. 🟡 Watch.
- No related-party borrowings (no borrowing from promoter entities
  disclosed).
- 5-year repayment schedule: NOT separately tabulated for FY26 (only
  current/non-current split and lease-liability maturity buckets are given,
  Note 34.3(b) "remaining contractual maturities": borrowings — repayable
  on demand ₹140.9164 Cr, <1yr ₹0.1106 Cr, >1yr ₹0.0583 Cr).
- Net Debt (Note 35, Capital management, PDF p.102): ₹138.0782 Cr (FY26) vs
  ₹118.2758 Cr (FY25), +16.7% — net debt growing faster than gross debt
  because cash & liquid balances fell simultaneously (see Section 6).
  Debt-Equity ratio (Note 43) rose to 0.32x from 0.27x (+16.7%,
  standalone; consolidated 0.32x vs 0.27x, +17.5%).

═══════════════════════════════════════════════════════════════════
## 8. TRADE PAYABLES (Note 18, standalone PDF p.93-94, consolidated
   PDF p.147-148)
═══════════════════════════════════════════════════════════════════

| Item | FY26 (₹ Cr) | FY25 (₹ Cr) | YoY % |
|---|---|---|---|
| MSME dues (standalone) | 2.1974 | 3.0988 | -29.1% |
| Other than MSME (standalone) | 62.6994 | 70.9407 | -11.6% |
| **Total (standalone)** | **64.8968** | **74.0395** | -12.3% |
| **Total (consolidated)** | **64.9624** | **74.6962** | -13.0% |

Ageing (standalone, Note 18(ii)): Not due ₹57.5862 Cr, <1yr ₹4.7125 Cr,
1-2yr ₹1.8878 Cr, 2-3yr disputed ₹0.3160 Cr, >3yr disputed ₹0.3942 Cr. NO
MSME dues are >45 days overdue and NO interest on delayed MSME payment is
accrued or paid in either year (Note 18/36, both years show ₹0 interest
accrued/paid) — clean on this dimension. 🟢.

Payable days (Note 43 Trade Payables Turnover Ratio): 3.97x (FY26) vs 4.43x
(FY25) standalone, -10.4% — i.e. payable days LENGTHENED slightly
(≈92 days FY26 vs ≈82 days FY25), a working-capital source even as
receivables and inventory both deteriorated/lengthened — net effect
captured in Net Capital Turnover Ratio improving to 2.67x from 2.37x
(+12.9%), i.e. the company is running a tighter working-capital cycle
overall by stretching payables, not by collecting receivables faster.

═══════════════════════════════════════════════════════════════════
## 9. PROVISIONS (Note 16/21, standalone PDF p.91-92/94, consolidated
   PDF p.146/148-149)
═══════════════════════════════════════════════════════════════════

**Warranty provision movement — STANDALONE (Note 16(ii), PDF p.90,
reconciles correctly):**
Opening ₹11.6272 Cr + Additions ₹2.3038 Cr − Utilised/reversed ₹5.1208 Cr =
Closing ₹8.8101 Cr (FY26); FY25: Opening ₹13.4047 Cr + Additions ₹3.6013 Cr
− Utilised ₹5.3789 Cr = Closing ₹11.6272 Cr. Arithmetic ties in both years. 🟢

**Warranty provision movement — CONSOLIDATED (Note 16(ii), PDF p.146) —
DOES NOT RECONCILE:**
Opening ₹11.6272 Cr + Additions ₹2.3038 Cr − Utilised ₹5.1208 Cr = ₹8.8102
Cr by arithmetic, but the disclosed Closing Balance is ₹19.0518 Cr — a
₹10.2416 Cr (₹1,024.16 lakh) unexplained gap, verified directly against the
PDF page image (PDF p.146; printed p.144). This is the same table, same
opening/additions/utilised figures as the correctly-reconciling standalone
note — only the consolidated closing balance figure is wrong. 🔴 Red Flag
— clear numerical error in the audited consolidated financial statements,
not an extraction artifact (confirmed via direct PDF image read).

**Total non-current provisions (Note 16 balance-sheet total):** Standalone
₹4.2328 Cr (FY26) vs ₹6.6235 Cr (FY25); Consolidated ₹4.3701 Cr vs ₹6.6235
Cr. Employee-benefit sub-components: Compensated Absences, "Other employee
Benefits," Provision for Long-term Warranty — consolidated table reconciles
cleanly (₹1.4407+0.3303+2.5991=₹4.3701 Cr); the standalone table's row
labelling is harder to parse from the extracted text but the balance-sheet
total ties (₹4.2328 Cr) — treated as a text-layout artifact, not flagged as
an error (unlike the warranty movement error above, which is unambiguous).

**Current provisions (Note 21):** Standalone: Compensated Absences ₹0.4055
Cr, Gratuity ₹0.7675 Cr (FY26, nil FY25 — gratuity flipped from a net asset
to a net liability, consistent with Note 37.1 showing DBO ₹11.9689 Cr now
exceeding plan assets ₹11.2014 Cr), Provision for warranty ₹6.2110 Cr (FY26)
vs ₹6.2169 Cr (FY25) ≈ flat. Total ₹7.3840 Cr vs ₹6.4618 Cr, +14.3%.

**Employee benefits (Ind AS 19), Note 37/37.1, PDF p.100-103:**
- Gratuity DBO: ₹11.9689 Cr (FY26) vs ₹10.2610 Cr (FY25), +16.6%. Fair value
  of plan assets ₹11.2014 Cr vs ₹10.8709 Cr, +3.1%. Net liability flipped
  from a NET ASSET of ₹(0.6099) Cr (FY25) to a NET LIABILITY of ₹0.7675 Cr
  (FY26) — a ₹1.3774 Cr swing, driven substantially by a Past Service Cost
  of ₹2.3315 Cr this year (FY25: nil) attributed to "additional provision
  for Gratuity as per new labour code" (also separately shown as an
  exceptional item of ₹(0.2412) Cr, Note 32 — the two disclosures appear
  related but are not explicitly cross-referenced to each other; the ₹2.33
  Cr past-service cost in the actuarial note is far larger than the ₹0.24
  Cr "exceptional" gratuity charge in the P&L, and the notes do not
  reconcile the two figures. 🟡 Watch — reconciliation gap between Note
  32 and Note 37.1(b)(i).
- Discount rate: 7.36% (FY26) vs 6.79% (FY25). Salary growth rate: 7.00%
  (FY26) vs 8.00% (FY25). Sensitivity: a 1% discount-rate decrease would
  increase DBO by ₹0.9255 Cr; a 1% increase would decrease it by ₹0.8033
  Cr (Note 37.1(j)).
- No decommissioning provisions, no onerous-contract provisions, no
  litigation provisions beyond the contingent-liability disclosures in
  Section 3 are separately provided for in the notes. NOT FOUND IN
  DOCUMENT (no separate litigation-provision note; all litigation is
  treated as contingent/disclosed-only, consistent with the policy that
  outflow is not "probable").

═══════════════════════════════════════════════════════════════════
## 10. DEFERRED TAX (Note 5 / Note 42, both statements)
═══════════════════════════════════════════════════════════════════

Net DTL: Standalone ₹6.7018 Cr (FY26) vs ₹8.1766 Cr (FY25); Consolidated
₹5.6202 Cr vs ₹7.7202 Cr.

Effective vs statutory rate reconciliation (standalone, Note 42, PDF
p.108-109): FY25 (profitable year) — statutory rate 25.17%, expected tax
₹10.6169 Cr, actual total tax expense ₹8.0505 Cr (effective rate 19.2%),
driven by "Allowances/Deductible" (₹-7.1605 Cr) and "Expenses not deductible"
(+₹6.8599 Cr) largely offsetting, plus a tax-related capital-gains add-back
of ₹0.5871 Cr (from the Penta Auto Feeding JV sale) and an MAT-timing
adjustment of ₹-2.6994 Cr. FY26 (loss year): profit before tax is negative
(₹-4.2321 Cr standalone), so "Expected tax expense" is nil and the entire
tax reconciliation table for FY26 shows zero line items except a net
DEFERRED TAX CREDIT of ₹-1.7893 Cr (standalone) recognised — this credit
arises from reversal of existing temporary differences (doubtful debts,
leave encashment, gratuity, bonus, depreciation, fair valuation), NOT from
recognition of a new deferred tax asset on the current-year operating loss
itself.

**MAT credit entitlement:** ₹0 in both years, both statements (Note 5) — no
MAT credit carried or utilised.

**Unrecognised DTA / carry-forward tax losses:** the notes do NOT disclose
whether the company has any unrecognised deductible temporary differences or
unused tax losses arising from the FY26 loss, nor a reason for
non-recognition if any exist. Given the company reported a PRE-tax loss in
both standalone (₹-4.2321 Cr) and consolidated (₹-7.7804 Cr) terms, Ind AS
12 disclosure of unrecognised DTA (or a positive statement that none exists)
would ordinarily be expected. NOT FOUND IN DOCUMENT. 🟡 Watch — flag as a
question for management (does the FY26 loss create a carry-forward tax
loss, and if so why is no DTA recognised or discussed?).

**Consolidated income tax reconciliation — internal inconsistency (Note 42,
PDF p.166, verified via PDF image):** The reconciliation table's own
computed "Total tax expense" row for FY25 reads ₹7.9720 Cr, but the
Consolidated Statement of Profit and Loss (and the top of the same Note 42)
report Total tax expense for FY25 as ₹7.6101 Cr — a ₹0.3619 Cr discrepancy
that does not reconcile anywhere in the note. 🔴 Red Flag — second
independent, PDF-verified numerical inconsistency in the consolidated notes
(alongside the Note 16 warranty error in Section 9).

═══════════════════════════════════════════════════════════════════
## 11. REVENUE DETAILS (Note 22/38, standalone PDF p.94/103-104,
   consolidated PDF p.149/160-161)
═══════════════════════════════════════════════════════════════════

| Segment | FY26 Revenue (₹ Cr) | FY25 Revenue (₹ Cr) | YoY % | FY26 Result (₹ Cr) | FY25 Result (₹ Cr) | YoY % |
|---|---|---|---|---|---|---|
| Extrusion Machinery | 314.8899 | 362.8502 | -13.2% | 50.7479 | 70.1387 | -27.6% |
| Battery Division (Geon) | 136.1084 | 126.9812 | +7.2% | (43.3464) | (25.5328) | +69.8% (loss widened) |
| **Total** | **450.9983** | **489.8314** | -7.9% | **7.4016** | **44.6058** | -83.4% |

(Note: standalone Note 38's "Total Segment Revenue" line literally sums to
₹489.8314 Cr for FY25, which is Total Income basis, not Note 22's Revenue
from Operations of ₹476.8469 Cr — the segment note's FY25 comparative
appears to include Other Income in the revenue total for FY25 only; the
FY26 column of the same table, ₹450.9983 Cr, matches Note 22's Revenue from
Operations exactly. This is an internal inconsistency in how the two years
are presented within Note 38 itself. 🟡 Watch.)

This directly resolves verification priority (a): **the Battery Division
(Geon, erstwhile Battrixx) carries the FY26 loss, and its segment loss
WIDENED 69.8% YoY (₹-25.53 Cr → ₹-43.35 Cr) even as its revenue grew 7.2%** —
i.e. losses are scaling faster than revenue, the opposite of an operating
leverage story. The Extrusion Machinery division remains solidly profitable
but its own revenue and profit both fell double digits (-13.2% / -27.6%).
Segment assets are near parity (Extrusion ₹363.38 Cr vs Battery ₹364.37 Cr
standalone) despite the profit gap, meaning the Battery Division carries a
similar capital base to the profitable Extrusion business while generating
under a third of its revenue and a large loss — a capital-efficiency red
flag. 🔴 Red Flag.

**Consolidated-only reconciling item:** Note 38 consolidated shows an
"Unallocated Corporate income net of unallocated expenses" of ₹(3.5420) Cr
(FY26) vs ₹(2.6549) Cr (FY25) that does NOT appear in the standalone segment
note (standalone shows nil here). This ₹3.54 Cr unallocated expense closely
matches Varos Technology's own FY26 loss (₹2.9149 Cr PAT loss / ₹3.5400 Cr
PBT loss per AOC-1) — i.e. Varos's losses sit OUTSIDE both named business
segments in the consolidated presentation, further obscuring where the
consolidated loss originates unless cross-read against Note 45 (Schedule
III additional information, Section on Investments above) and the AOC-1.

**Geography (Note 38):** India ₹391.9186 Cr (FY26) vs ₹410.2211 Cr (FY25),
-4.5%; Outside India (exports) ₹57.5182 Cr vs ₹65.0794 Cr, -11.6%. Exports
are 12.8% of revenue (FY26) vs 13.3% (FY25).

**Customer concentration:** ONE customer ≥10% of revenue in FY26 (19.11% of
revenue), down from TWO customers in FY25 (26.94% combined). Customer
name(s) NOT disclosed (standard Ind AS 108 practice, no naming requirement).
🟡 Watch — concentration remains material even after the reduction from two
to one qualifying customer.

**Revenue recognition:** point-in-time on delivery for goods; services
(maintenance) also point-in-time/period-based, no material change in
policy. No contract assets/contract liabilities note beyond "Advances from
customers" (Note 20, ₹59.3868 Cr standalone FY26 vs ₹73.2194 Cr FY25, -18.9%
— a meaningful decline in customer advances, consistent with a weaker order
book / slower Extrusion Machinery bookings). No "unsatisfied performance
obligation" quantum table is disclosed (NOT FOUND IN DOCUMENT — Ind AS 115
practical-expedient exemption likely applies but is not explicitly cited).

═══════════════════════════════════════════════════════════════════
## 12. OTHER CRITICAL NOTES
═══════════════════════════════════════════════════════════════════

**Exceptional items (Note 32, both statements, PDF p.97/152):** FY26: a
₹(0.2412) Cr charge for "Additional provision for Gratuity as per new
labour code" — a genuine one-off, non-recurring by nature, though see the
Section 9 cross-reference gap with Note 37.1's much larger ₹2.33 Cr past
service cost. FY25: ₹8.4898 Cr gain on sale of the Penta Auto Feeding India
Ltd JV stake (ceased 6-Feb-2025) — a one-off gain that flattered FY25's
reported profit and is not repeatable; excluding it, FY25 standalone PBT
would have been ₹35.4329 Cr vs the reported ₹41.9227 Cr (still far above
FY26's loss).

**EPS (Note 33):** Standalone Basic/Diluted EPS ₹(0.70) (FY26) vs ₹9.69
(FY25); Consolidated ₹(1.53) vs ₹9.21. No dilutive instruments outstanding
(weighted average basic = diluted shares in both years, 3.4973 Cr shares) —
no ESOP or warrant dilution live in FY26 (the 2022 preferential warrants
referenced in company memory appear to have been FULLY CONVERTED/EXERCISED
prior to FY25: Note 14.1 records "Previous year the Company has issued
1,381,730 shares of ₹5 each at a premium of ₹324 each" as a FY25 event, with
NO further share/warrant issuance in FY26 — Note 15's "Share Premium &
Warrant proceeds" opening and closing balances are IDENTICAL at ₹105.4261 Cr
in both years, confirming no warrant activity in FY26).

**Segment/goodwill/impairment:** see Sections 6, 9, 11 above.

**Foreign currency exposure (Note 34.3(c), PDF p.98-99):** Net unhedged
foreign-currency liability position widened to ₹(38.2064) Cr (FY26) from
₹(5.6142) Cr (FY25) — a 6.8x increase in unhedged net FX exposure, driven by
trade payables in USD/CNH/EUR rising far faster than trade receivables in
the same currencies (Trade payables FX-equiv. ₹40.1894 Cr FY26 vs ₹14.6966
Cr FY25, +173.5%). Forward contracts hedged were reduced to NIL at FY26
from USD 2.42 lakh (₹2.0133 Cr) at FY25 (Note 34.3(c)(i)) — the company
REDUCED hedging exactly as its unhedged exposure grew. Sensitivity: a 5% USD
move now swings PBT by ₹1.0675 Cr (FY26) vs ₹0.1399 Cr (FY25), a 7.6x
increase in FX sensitivity. 🔴 Red Flag — rising unhedged FX exposure with
falling hedge cover, in a year of net losses.

**CSR (Note 30, both statements, PDF p.94-97/151):** Gross CSR obligation
₹0.826 Cr (FY26) vs ₹0.9303 Cr (FY25); amount spent ₹0.6966 Cr vs ₹0.9994
Cr; shortfall of ₹0.0894 Cr (FY26) was covered by drawing down ₹0.04 Cr of
the prior year's ₹0.0691 Cr surplus, leaving the note to state a net
shortfall/surplus of "-" (nil) at FY26 year-end, with the note affirming any
shortfall was deposited into a separate bank account as prescribed and
utilised in-year. Broadly compliant, though spend fell short of the gross
obligation for the second consecutive year in absolute terms (before
set-offs). 🟡 Watch (minor).

**Share capital / promoter holding (Note 14, both statements, PDF
p.87-88/144-145):** No new shares issued in FY26 (34,972,836 shares flat).
Promoter holding rose marginally to 60.49% from 60.24% (+0.25pp), driven by
an internal transfer: Shreevallabh G. Kabra's holding fell from 3.57% to
0.00% (upon his cessation as Executive Chairman/Director, 15-Sep-2025 /
25-Jul-2025) with a corresponding rise in the Shreevallabh Kabra Family
Trust's holding from 5.14% to 8.72% — an intra-family/trust transfer, not
open-market promoter buying. 🟡 Watch (note as context, not a red flag).

**Dividend (Note 44, both statements, PDF p.110/167):** Board recommends
₹0.00 per share for FY26, down from ₹2.50 per share recommended for FY25
(the ₹3.50/share actually PAID during FY26, per Note 15, relates to the
FY25 final dividend approved at the FY25 AGM plus an interim component from
an earlier year — the two figures, ₹2.50 "recommended for FY25" in Note 44
and ₹3.50 "paid — FY 2024-25" in Note 15, are not the same number and the
notes do not reconcile the discrepancy). Regardless of the exact prior-year
figure, the FY26 recommendation of a FLAT NIL dividend is a clear signal of
capital conservation amid the loss and rising secured debt. 🔴 Red Flag
(signal, not an accounting-quality issue).

**Direct debits/credits to reserves bypassing P&L:** OCI movements (equity
instruments FVOCI ₹-7.8804 Cr, remeasurement of defined benefit plans
+₹1.4050 Cr, both net of tax) are correctly routed through OCI, not P&L,
per Ind AS — not an aggressive practice, standard FVOCI/actuarial treatment.
The ₹1.221 Cr "Gain on Equity Instruments... transferred" from OCI to
Retained Earnings (Note 15, both statements) represents realised gains on
partial sale of the Plastiblends stake being recycled within equity (never
through P&L, consistent with the irrevocable FVOCI election under Ind AS
109 — this DEPRESSES reported P&L profit/loss relative to a FVTPL
classification, i.e. it is a conservative, not aggressive, choice).

**Other Statutory Information (Note 46, both statements, PDF p.110/168-169):**
No struck-off company transactions; no charges pending registration; layers
compliant; no scheme of arrangement; no intermediary fund-routing; no crypto
trading; no Benami property; no undisclosed income; no revaluation of PPE;
NOT a declared wilful defaulter. All clean, boilerplate-negative
disclosures — no exceptions raised. 🟢

**Events after balance sheet date:** No separate "subsequent events" note
number exists in the standalone or consolidated notes (Note 47 is only
"previous year regrouping"). The CFO change (Daulat Jain ceased 27-Apr-2026;
interim CFO Uttam Singh 13-May-2026 to 19-Jun-2026; new CFO Bhavin Sheth
w.e.f. 20-Jun-2026, per Corporate Information page, outside notes scope) and
the CRISIL downgrade (13-May-2026, per company memory, in the Corporate
Governance Report, also outside notes scope) both occurred AFTER the balance
sheet date (31-Mar-2026) and BEFORE the financial statements were approved
(28-May-2026), yet NEITHER is disclosed as a subsequent event anywhere in
the Notes to Financial Statements (standalone or consolidated). Under Ind
AS 10, a CFO change of this nature is not normally required to be
disclosed, but a credit rating downgrade occurring 15 days before the
financial statements were approved, for a company that just took on more
secured short-term debt, is the kind of event an investor would expect to
see referenced (even if only in the Director's Report, which is outside
this Pass's scope). NOT FOUND IN DOCUMENT (Notes to FS). 🔴 Red Flag —
disclosure gap on a subsequent event with direct bearing on the borrowings
disclosed in Note 17.

**Going concern:** No "material uncertainty related to going concern"
paragraph appears in either the standalone or consolidated Independent
Auditor's Report (searched both Key Audit Matters and Auditor's
Responsibility sections, PDF p.55-66 standalone, p.112-120 consolidated) —
only the standard boilerplate describing the auditor's responsibility to
conclude on going concern. The Key Audit Matters in BOTH statements are
identical: (A) Revenue Recognition, (B) Valuation of Inventory (cross-ref
Note 7), (C) Contingent Liability (cross-ref Note 41(a)) — notably, NEITHER
the Battery Division's widening losses, NOR the HEVPL receivable, NOR the
Varos subsidiary's negative net worth were called out as a Key Audit Matter
in either report, despite each being individually larger in P&L or balance
sheet terms than the matters that WERE flagged. 🟡 Watch (audit-scope
observation, not itself an accounting-quality defect).

═══════════════════════════════════════════════════════════════════
## PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS
═══════════════════════════════════════════════════════════════════

1. **Battery Division (Geon) segment loss widened 69.8% YoY to ₹43.35 Cr
   (FY25: ₹25.53 Cr) even as its revenue grew 7.2%; Extrusion Machinery
   segment profit fell 27.6% to ₹50.75 Cr on revenue down 13.2%** — directly
   answers which division carries the FY26 loss. (Note 38, standalone PDF
   p.103-104 / consolidated PDF p.160-161). 🔴 Red Flag.

2. **Varos Technology Pvt Ltd (100% subsidiary) alone contributed 54.32% of
   the ENTIRE consolidated net loss (₹-2.9149 Cr of ₹-5.3659 Cr) on revenue
   of just ₹0.1784 Cr, and carries negative net worth of ₹-6.9608 Cr against
   ₹13.32 Cr of cumulative parent funding (equity + CCD).** Its losses sit
   outside both named segments, in "unallocated corporate" (Note 38
   consolidated). (Note 45 Schedule-III additional info, PDF p.167; AOC-1,
   PDF p.23; Note 3, PDF p.85/140). 🔴 Red Flag.

3. **Consolidated Note 16 warranty-provision movement table does not
   arithmetically reconcile:** Opening ₹11.6272 Cr + Additions ₹2.3038 Cr −
   Utilised ₹5.1208 Cr = ₹8.8102 Cr, but the disclosed Closing Balance is
   ₹19.0518 Cr (a ₹10.24 Cr gap) — verified directly against the PDF page
   image, not an extraction artifact; the parallel standalone note (Note
   16, PDF p.90) reconciles correctly to ₹8.8101 Cr. (Note 16, consolidated,
   PDF p.146). 🔴 Red Flag — audited-statement arithmetic error.

4. **Consolidated income-tax reconciliation note's own computed "Total tax
   expense" for FY25 (₹7.972 Cr) does not match the ₹7.6101 Cr reported in
   the Consolidated P&L / same note's opening summary** — a second,
   independent, PDF-verified inconsistency. (Note 42, consolidated, PDF
   p.166). 🔴 Red Flag.

5. **HEVPL (Hero Electric) receivable of ₹30.39 Cr, disclosed as under NCLT
   insolvency (CIRP admitted 20-Dec-2024), is described in Note 9 using
   language STILL dated "as at March 31, 2025" with zero update on
   FY26-year status, further provisioning, or recovery** — identical
   wording to the FY25 AR's Note 9. (Note 9, standalone PDF p.87-88 /
   consolidated PDF p.142-143). 🔴 Red Flag — stale, unrevised disclosure on
   a ~₹30 Cr at-risk exposure.

6. **Liquid buffer drawn down 57.8% (mutual funds ₹53.49 Cr → ₹22.59 Cr)
   while secured short-term borrowings rose 56.3% (₹90.16 Cr → ₹140.92 Cr)
   and capital commitments rose 22x (₹1.43 Cr → ₹31.77 Cr) in the same year
   the company reported a loss and cut its dividend to nil** — the company
   is running down cash reserves and leaning on secured debt to keep funding
   capex despite widening Battery Division losses. (Notes 8, 17, 41(b), 44).
   🔴 Red Flag — compound liquidity/capital-allocation signal → feeds
   FLAG-CASH.

7. **Trade receivables ageing deteriorated sharply despite a falling gross
   balance: the >3-year bucket nearly doubled (₹9.53 Cr → ₹19.35 Cr,
   +103%), and the >6-months-overdue share of total receivables rose from
   42.4% to 50.2%; ECL coverage rose from 8.1% to 11.6% of gross.** (Note 9,
   standalone PDF p.87-88 / consolidated PDF p.142-143). 🔴 Red Flag →
   feeds FLAG-CASH.

8. **Unhedged net foreign-currency exposure grew 6.8x (₹-5.61 Cr →
   ₹-38.21 Cr) while forward-contract hedge cover was cut to ZERO (from USD
   2.42 lakh at FY25) — the company reduced hedging exactly as its unhedged
   FX exposure and FX sensitivity (7.6x higher) both grew.** (Note 34.3(c),
   standalone PDF p.98-101). 🔴 Red Flag.

9. **Dividend cut to ₹0.00/share for FY26 from a recommended ₹2.50/share
   for FY25** (the two dividend figures in Notes 15 and 44 do not
   themselves reconcile to each other, a minor secondary disclosure gap),
   alongside a CRISIL long/short-term rating downgrade 15 days before FS
   approval (company memory; not itself disclosed as a subsequent event
   anywhere in the Notes to FS). (Note 44, PDF p.110/167). 🔴 Red Flag.

10. **A pattern of stale/unrevised disclosure across THREE independent
    notes** — the consolidated Basis of Preparation paragraph still dated
    "31 March 2025"/"16 May 2025" (Note 1, PDF p.127), the consolidated RPT
    note still showing balances with fully-consolidated subsidiaries Varos
    and Kabra Energy that should be eliminated (Note 39, PDF p.161-164),
    and the HEVPL receivable note (#5 above) — suggests the consolidated
    financial statements notes were adapted from the standalone / prior-year
    notes without full review before audit sign-off. 🟡 Watch — accounting
    quality / drafting-control theme, feeds the accounting-quality score.
