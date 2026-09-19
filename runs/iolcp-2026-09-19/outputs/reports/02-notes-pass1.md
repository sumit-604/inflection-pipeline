# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 1 OF 3 (FULL EXTRACTION)
IOLCP (IOL Chemicals & Pharmaceuticals Ltd) | FY26 Annual Report | RUN_DATE 2026-09-19

Source: `inputs/annual-report/Annual_Report_2026.txt`, page-marked extraction ([page N] = PDF
page). Standalone Notes to Financial Statements: Note 1 to Note 53, pages 138-178. Consolidated
Notes: Note 1 to Note 50, pages ~192-230. Prior-year AR (FY25) used only where a note needs a
second comparative. All figures ₹ Crore unless stated. Ratings: 🟢 Clean | 🟡 Watch | 🔴 Red Flag.

Scope check: standalone and consolidated notes are near-identical (three of four subsidiaries are
non-operating shells; consolidated total assets differ from standalone by only ~₹0.1-0.5 Cr per B00
input note). Where a consolidated note repeats the standalone note verbatim (contingent liabilities,
gratuity, financial risk management, related-party balances ex-intercompany), this pass anchors to
the standalone note and flags only true consolidated-only content (subsidiary list, Schedule III
net-asset/profit share table, IOL Pharmaxis UK non-consolidation).

---

## 1. ACCOUNTING POLICIES & CHANGES

- Standard Ind AS policy set (Note 2(i)/(ii), p.138-146; consolidated Note 2, p.192-196):
  historical cost convention, functional currency INR, going-concern basis stated explicitly
  (Note 2(i).I, p.138). 🟢
- Depreciation: straight-line per Schedule II lives, with three named exceptions on management
  technical estimate — general plant & equipment (triple shift) 15 years, general plant &
  equipment (continuous process) 15 years, co-generation plant 4-15 years (Note 2(ii).VIII,
  p.139-140). Same exceptions and lives as disclosed in FY25 policy — **no change this year**. 🟢
- Intangible asset useful lives: software 6 years, technical know-how 5 years, patents 20 years
  (Note 2(ii).IX, p.140). Unchanged. 🟢
- Capitalisation threshold: NOT FOUND IN DOCUMENT (no rupee threshold disclosed).
- Impairment testing: Note 43 (p.175) states the company assessed indicators of impairment and
  found none, so **no formal recoverable-amount computation was performed** — i.e. no growth/
  discount-rate assumptions are disclosed because no formal test was run. No goodwill exists on
  either balance sheet (search returned zero hits for "goodwill" anywhere in the AR). 🟢 (nothing
  to test) but flagged 🟡 as an evidence gap if the operator later wants impairment sensitivity on
  the new capex-heavy PP&E base.
- ECL matrix: provision-matrix based on ageing and historical loss experience, no numeric matrix
  disclosed (Note 10, p.152; policy at Note 2(ii).XX.i, p.145). Allowance moved 2.63 → 4.59 Cr
  (+74.5% YoY) against trade receivables gross +17.4% YoY (Note 10 continuation, p.152) — coverage
  ratio rising faster than the book. 🟡 Watch, cross-ref Section 4 below.
- Ind AS 116 (leases): **first ROU asset and lease liability recognised this year** — opening
  balance Nil at both 01-Apr-2024 and 01-Apr-2025, additions of ₹3.51 Cr (ROU) / ₹3.50 Cr (lease
  liability) during FY26 (Note 37, p.164). Discount rate used for lease liability: NOT FOUND IN
  DOCUMENT (only the gratuity discount rate, 7.25%, is disclosed; no lease-specific discount rate
  stated). Lease liability split: current ₹1.02 Cr, non-current ₹2.40 Cr (Note 17, p.156). Small
  quantum, 🟢, but the missing discount rate is a genuine gap for anyone wanting to check the
  liability's sensitivity.
- First-time standard adoptions this year: **the four Labour Codes (notified 21-Nov-2025)**,
  treated as a plan amendment under Ind AS 19, triggering immediate past-service-cost recognition
  of ₹11.21 Cr as an exceptional item in the Dec-2025 quarter (Note 50 standalone p.178 / Note 47
  consolidated p.229-230). This is the single largest one-off P&L item in the note set. 🟡 Watch —
  legitimate and well-explained, but it inflates FY26 gratuity/compensated-absences expense and
  must be excluded when normalising YoY margin comparisons (chemicals segment result "nearly
  doubling" partly reflects where this hit landed — see Section 11).
- Revenue recognition: point-in-time on transfer of control (generally on shipment), 0-90 day
  credit terms (Note 2(ii).V, p.140-141). No aggressive bill-and-hold or over-time recognition for
  a commodity/API manufacturer of this kind. 🟢. Independent Auditor's Key Audit Matter on
  consolidated revenue (p.179 onward) specifically probes cut-off near year-end — auditor did not
  raise any exception. 🟢

## 2. RELATED PARTY TRANSACTIONS (Note 40, standalone p.169-171; consolidated p.223-224)

Related parties: three "Enterprises over which KMP is able to exercise significant influence or
control" — **NM Merchantiles Limited** (formerly NM Merchantiles Private Limited), **Mayadevi
Polycot Limited**, **NCVI Enterprises Limited** — plus Varinder Gupta (HUF), the IOL Group Gratuity
Trust, and KMP/non-executive directors. This directly confirms three of the five LBF2 names.
**G Consultants and Fabricators and Synthorix Trading are NOT named anywhere in the FY26 Note 40
related-party list** — consistent with the company-memory finding that they were classified as
public/non-related before their Jun-2026 amalgamation into NM Merchantiles (which post-dates this
AR's 20-May-2026 board sign-off, so the amalgamation itself falls outside this AR's coverage
period and disclosure obligation). 🟡 Watch — flag for the live-web/claims verification stage: the
AR gives no visibility on what these two entities were before the merger.

| Party | Nature | FY26 ₹Cr | FY25 ₹Cr | YoY % |
|---|---|---|---|---|
| NCVI Enterprises Ltd | Purchase of goods/services | 40.00 | 38.35 | +4.3% |
| Mayadevi Polycot Ltd | Purchase of goods/services | 69.42 | 54.96 | +26.3% |
| NM Merchantiles Ltd | Purchase of goods/services | 22.52 | 7.37 | +205.6% |
| KMP | Managerial remuneration (incl. incentives) | 21.75 | 22.13 | -1.7% |
| Non-exec directors | Sitting fees | 0.31 | 0.34 | -8.8% |
| Subsidiaries | CSR contribution to IOL-Foundation | 0.94 | 1.56 | -39.7% |
| Post-employment plan | Contribution to Gratuity Trust | 5.55 | 5.55 | 0.0% |
| Related parties (aggregate KMP + enterprises + directors + PEB) | Rent paid | 1.55 | 1.53 | +1.3% |

RPT purchases total (three promoter-group entities) = ₹131.94 Cr FY26 vs ₹100.68 Cr FY25
(+31.1% YoY), against total raw-material consumption of ₹1,501.61 Cr FY26 (Note 27, p.158) —
**RPT purchases are 8.8% of material consumed** (up from 7.4% FY25). 🟡 Watch: NM Merchantiles'
purchase value nearly tripled YoY (₹7.37 Cr → ₹22.52 Cr), the steepest move of the three, in the
same year its shareholding also jumped — worth a management question on whether NM Merchantiles'
commercial role in the supply chain is expanding alongside its equity stake.

Outstanding related-party payables: NCVI ₹4.02 Cr, Mayadevi Polycot ₹11.12 Cr (nearly doubled from
₹6.26 Cr), NM Merchantiles ₹1.69 Cr — total ₹16.83 Cr vs ₹11.82 Cr FY25 (+42.4%), i.e. related-party
trade payables are 3.5% of total trade payables (₹482.56 Cr) and are rising faster than the payable
book overall (+12.9% YoY). 🟡 Watch, not disqualifying, but a pattern to track across quarters.

Note (iii) under Note 40C: **NCVI Enterprises Limited has given a personal/corporate surety of
₹27.65 Cr on customs bonds executed by the company** for concessional-duty raw-material imports,
with ₹2.83 Cr of the underlying export/production obligation still pending as at 31-Mar-2026
(down from ₹4.69 Cr FY25). This ties the promoter-group entity into the company's customs
compliance chain — non-arm's-length signal in the sense that a related party is standing surety
for the company's regulatory bonds, though this is common practice for promoter-linked entities in
family-run manufacturers. 🟡 Watch.

No loans to promoter entities: Note 48(v) standalone (p.177) states explicitly "The Company has
not given any loan or advances to its Promoters, Directors, KMP and related Parties." 🟢. No
royalty/licence-fee/franchise payments to promoter family found (only rent, purchases, sitting
fees, CSR, gratuity-trust contribution). Rent paid to related parties (KMP + enterprises)
₹1.55 Cr FY26 vs ₹1.53 Cr FY25 — flat. New related party this year: none named beyond the
existing set (IOL Pharmaxis UK Limited is a wholly-owned subsidiary, not an arm's-length RPT
counterparty in the disclosed transaction table since it has not commenced operations — Note 48
consolidated, p.229-230).

## 3. CONTINGENT LIABILITIES (Note 35, standalone p.161; consolidated p.215-216, identical figures)

| Nature | FY26 ₹Cr | FY25 ₹Cr | Company assessment |
|---|---|---|---|
| Claims not acknowledged as debts | 0.26 | 0.26 | Ordinary course; no material adverse effect expected |
| Bank guarantees issued in favour of others | 3.34 | 5.26 | — |
| Others* (Customs O-I-O, see below) | 2.06 | 0.00 | Company to file appeal |
| **Total contingent liabilities** | **5.66** | **5.52** | |
| Capital commitments (contracts remaining, net of advances) | 69.35 | 25.42 | Rising with capex ramp |
| Export obligations under Advance Authorisation/DFIA | 0.00 | 0.00 | — |
| Obligations against concessional-duty imports (IGCR) | 2.83 | 4.69 | — |
| **Total commitments** | **72.18** | **30.11** | |

Total contingent liabilities ₹5.66 Cr against total equity ₹1,798.38 Cr (standalone, Note 42
p.174) = **0.31% of net worth** — immaterial, no single item near 10% of net worth. 🟢

*"Others" item — new this year: **Order-In-Original confirming differential Customs duty of
₹0.28 Cr, penalty ₹0.28 Cr under Section 114A, additional penalty ₹1.00 Cr under Section 114AA,
redemption fine ₹0.50 Cr, aggregating ₹2.06 Cr**, alleging incorrectly availed ASEAN-India FTA
exemption via non-conforming Certificates of Origin (Note 35 footnote, p.161). Company intends to
appeal. 🟡 Watch — this appears to be the same matter referenced in the corpus manifest as the
"customs penalty order 09-May-2026" BSE filing; the AR figure (₹2.06 Cr) is the anchor to
cross-check against that announcement in a later stage. Small quantum but a compliance-process
finding (import documentation/FTA certificate handling), not a one-off external shock.

Capital commitments jumped from ₹25.42 Cr to ₹69.35 Cr (+172.8% YoY) — consistent with the
Rs 500 Cr capex programme ramping (LBF3), and directionally supports the capex narrative, though
₹69 Cr committed is still far short of the ₹500 Cr+₹1,200-1,400 Cr guided programme. 🟡 Watch for
Section 6/7 cross-reference on funding.

No guarantees for subsidiaries disclosed (subsidiaries are immaterial/non-operating). No tax
dispute beyond the one customs matter above; no income-tax contingent liability disclosed
(Note 32 tax reconciliation shows no disputed demands carried as contingent).

## 4. TRADE RECEIVABLES (Note 10, standalone p.152; consolidated identical structure)

Ageing schedule, 31-Mar-2026 (₹Cr):

| Bucket | Undisputed good | Disputed (SICR/impaired) | Total |
|---|---|---|---|
| Not due | 482.92 | — | 482.92 |
| <6 months | 114.32 | — | 114.32 |
| 6m-1yr | 3.88 | — | 3.88 |
| 1-2 yrs | 0.22 | 1.34 | 1.56 |
| 2-3 yrs | — | 4.36 | 4.36 |
| >3 yrs | — | 0.68 | 0.68 |
| **Total gross** | **601.34** | **6.38** | **607.72** |
| Less ECL allowance | | | (4.59) |
| **Net** | | | **603.13** |

31-Mar-2025 comparative: gross ₹516.32 Cr (undisputed good ₹510.02 Cr), >6 months overdue
₹8.29 Cr (1.6% of gross); 31-Mar-2026 >6 months overdue = ₹10.48 Cr (1.7% of gross) — the overdue
share is essentially flat YoY, so the ageing profile itself is **not** visibly deteriorating. 🟢
on ageing mix.

However: gross trade receivables grew ₹516.32 Cr → ₹607.72 Cr (**+17.7% YoY**) against revenue
growth of +11.5% YoY (Note 25, ₹2,079.21 Cr → ₹2,319.06 Cr) — **receivables are outrunning
revenue**, which is the mechanism behind the debtor-days rise the company memory already flags
(79 days FY22 → 95 days FY26). 🟡 Watch, feeds FLAG-CASH.

No single customer concentration risk: top-1 customer 2.98% of sales (FY26) vs 3.08% (FY25);
top-5 customers 12.46% vs 13.18% (Note 41(iii), p.174). Concentration is actually easing. 🟢

ECL allowance movement: opening ₹2.63 Cr → expected credit loss recognised ₹1.96 Cr → closing
₹4.59 Cr (Note 10 continuation, p.152) — allowance nearly doubled while gross receivables grew
17.7%, i.e. **coverage ratio rose from 0.51% to 0.76% of gross receivables**. Could read as
prudent (management tightening provisioning ahead of a larger book) or as an early credit-quality
signal. 🟡 Watch, insufficient on its own to call deterioration — cross-check against customer-wise
ageing detail not disclosed at that granularity.

Receivables from related parties: Note 7 (other financial assets non-current, p.151) shows "From
related parties (Refer note 40)" = Nil both years — **no related-party trade receivable balance**,
consistent with related parties being suppliers to IOL (payables direction), not customers. 🟢

## 5. INVENTORY (Note 9, standalone p.152; consolidated identical)

| Category | FY26 ₹Cr | FY25 ₹Cr | YoY % |
|---|---|---|---|
| Raw materials and components | 158.95 | 168.36 | -5.6% |
| Work-in-progress | 47.21 | 38.62 | +22.2% |
| Finished goods | 146.36 | 137.67 | +6.3% |
| Stores and spares | 17.30 | 15.97 | +8.3% |
| Stock in trade | 1.25 | 0.00 | new line |
| **Total** | **371.07** | **360.62** | **+2.9%** |

Finished-goods growth (+6.3%) is well below revenue growth (+11.5%) — **no red flag of channel
stuffing or unsold-goods build-up**. 🟢

Write-downs: inventory carried at NRV = ₹22.39 Cr FY26 vs ₹18.84 Cr FY25; provision for
write-down to NRV = ₹2.23 Cr FY26 vs ₹5.34 Cr FY25 (**provision more than halved** even as the
NRV-valued pool grew) — improving inventory quality signal. 🟢

Cost of inventory recognised as expense: ₹1,663.63 Cr FY26 vs ₹1,484.57 Cr FY25 (+12.1%, roughly
tracking revenue growth). No obsolete-inventory disclosure beyond the NRV write-down note; no
separate obsolescence commentary. Inventory hypothecated to secure borrowings (Note 9 footnote,
p.152), standard security arrangement. 🟢

Inventory days (approx, using FY26 average inventory ₹365.85 Cr and COGS-basis turnover ratio
5.11x from Note 49, p.177) ≈ 71 days FY26 vs 4.33x / ≈84 days FY25 — **inventory days improving**,
a positive working-capital signal even as receivable days worsen (see Section 4). 🟢

## 6. INVESTMENTS

Subsidiaries (consolidated Note 2(i) subsidiary table, p.193): IOL-Foundation (India, 100%),
IOL Speciality Chemicals Limited (India, 100%), IOL Pharmaxis UK Limited (UK, 100%, incorporated
16-Oct-2025 — new this year). **IOL Life Sciences Limited (India, was 100%) struck off the
register effective 01-Apr-2026** after a voluntary Section 248 application filed 24-Jan-2026;
no outstanding balance with the company at strike-off (Note 48(ix) standalone p.177 / Note 46(viii)
consolidated). 🟢 — clean wind-down of a dormant shell, well disclosed, no impairment or write-off
needed (carrying value was only ₹0.10 Cr, Note 5, p.151).

**IOL Pharmaxis UK Limited has not commenced operations and its financial statements are NOT
included in the FY26 consolidation** (Note 48 consolidated, p.230) — its Schedule III share table
row (p.230) shows 0.000% of consolidated net assets/profit across the board. 🟡 Watch — new
overseas entity flagged in the Directors' Report (line ~8016/9483 of the extraction) as part of
the international/CDMO push; nothing financial to anchor yet, purely a name-and-status finding for
later verification of what it is intended to do.

Investment carrying values (Note 5, standalone p.151): subsidiaries at cost — IOL-Foundation
₹0.10 Cr, IOL Speciality Chemicals ₹0.10 Cr (IOL Life Sciences written down to Nil from ₹0.10 Cr
on strike-off). Investment in an unquoted overseas equity instrument ("US Pharma Limited", 420
shares, face value $1) carried at FVTOCI, ₹17.41 Cr both years, Level 3 fair value, valued by an
independent Registered Valuer using income/market/asset approaches; management judges historical
cost an appropriate FV estimate (Note 38(b) note, p.166). No impairment on any investment either
year. No ICDs or loans given to any party (Note 48(xiii): "has not loaned or advanced or invested
funds to any other person(s) or entity(ies)... with any understanding"). 🟢 Current investments in
mutual funds (₹0.30 Cr) and a portfolio-manager absolute-return strategy (₹3.21 Cr) — immaterial,
FVTPL. No JVs or associates disclosed anywhere.

## 7. BORROWINGS (Note 19, standalone p.156; Note 41/42 for terms)

Only **short-term working-capital borrowing from banks, secured, repayable on demand**:
₹132.00 Cr FY26 vs ₹117.04 Cr FY25 (+12.8% YoY). **Zero long-term/term debt on the balance sheet
in either year** (Note 41 interest-rate-risk table, p.173, shows Nil across all long-term-debt
maturity buckets). Security: first pari-passu charge on all present and future current assets
(hypothecation of finished goods, WIP, raw material, stores, book debts) plus pari-passu charge on
fixed assets as collateral, further secured by the Managing Director's personal guarantee
(Note 19 footnote, p.156). No covenant breaches or waivers disclosed; Note 42 (p.174) states "no
breaches in the financial covenants of any interest-bearing loans and borrowing in the current
year." Gearing ratio N.A. both years (net debt is negative — cash exceeds borrowings). 🟢

This is directly load-bearing for LBF3: the company is entering a ₹500 Cr + ₹1,200-1,400 Cr capex
programme guided as "internally funded" while **carrying zero term debt and only ₹132 Cr of
working-capital borrowing** — either the capex will be funded from internal accruals/cash (FY26
cash + bank balances ₹240.44 Cr, Note 42) plus fresh term borrowing not yet drawn as at 31-Mar-2026,
or the funding plan implies debt to be raised in FY27+ that isn't yet on this balance sheet. No
related-party borrowings (only related-party trade payables, covered in Section 2). 🟡 Watch —
flag squarely for the FTTCP/valuation stage: FY26 FCF (per company memory) was ₹43 Cr against a
capex programme an order of magnitude larger; this AR's borrowing note shows no term facility yet
sanctioned or drawn for the greenfield.

## 8. TRADE PAYABLES (Note 20, standalone p.156-157; consolidated identical)

| Bucket | FY26 ₹Cr | FY25 ₹Cr |
|---|---|---|
| MSME, not due | 14.17 | 14.14 |
| MSME, <1yr overdue | 1.46 | 2.81 |
| MSME total | 15.63 | 16.95 |
| Others, not due | 430.33 | 383.75 |
| Others, 1yr+ overdue (sum of buckets) | 19.69 | 15.04 |
| Related party (Note 40) | 16.83 | 11.82 |
| **Total** | **482.56** | **427.56** |

MSME dues >45 days / interest on delayed MSME payments (Note 46, standalone p.176): principal
remaining unpaid to MSME suppliers ₹21.69 Cr FY26 vs ₹26.66 Cr FY25 (**improving**, -18.6%);
interest due thereon ₹0.15 Cr FY26 vs ₹0.12 Cr FY25; **no interest actually paid** under Section 16
either year (line "iii" = Nil both years) — company is not paying the statutory interest it
technically owes on delayed MSME payments, though it discloses the accrued interest. 🟡 Watch,
small quantum (₹0.15 Cr) but a governance-hygiene point: interest liability is being recognised
but not settled.

Payable days improving: Note 49 trade-payables turnover ratio 3.65x FY26 vs 3.24x FY25 (+12.6%)
→ payable days fell (~100 days → ~89 days), i.e. **the company is paying suppliers faster**, which
sits oddly next to the receivables stretching out slower collection (Section 4) — net effect is a
working-capital squeeze from both directions, funded so far by the flat/negative net-debt position.
🟡 Watch, ties into Section 7.

## 9. PROVISIONS

Gratuity (Note 36, p.162-164): funded defined-benefit plan through the IOL Group Gratuity Trust
(100% invested with LIC). PBO moved ₹34.18 Cr → ₹46.07 Cr (+34.8%), driven mainly by the **Past
Service Cost / curtailment gain-loss of ₹9.08 Cr** (Labour Codes recognition, see Section 1) —
current service cost and interest cost alone would have taken PBO to roughly ₹40.2 Cr. Plan assets
₹27.77 Cr → ₹34.58 Cr; net liability (unfunded status) widened from ₹6.41 Cr to ₹11.49 Cr. Discount
rate 7.25% (unchanged), salary growth 5.50% (unchanged), average remaining working life 26.91 years
(unchanged) — **actuarial assumptions held flat YoY**, so the PBO jump is entirely
plan-amendment-driven, not assumption-shading. 🟢 on assumption discipline, 🟡 flag on the
quantum/comparability impact already noted. Sensitivity: ±0.5% discount rate moves PBO by
∓₹1.80/+₹1.96 Cr; ±0.5% salary growth moves it by +₹2.00/-₹1.85 Cr — normal magnitude. Company
expects to contribute ₹4.85 Cr to the trust in FY27 (Note 36 xiii).

No warranty provisions, no decommissioning provisions, no onerous-contract provisions, and no
litigation provisions beyond the contingent-liability disclosures in Section 3 — this is a
manufacturer with a clean provisions note; compensated absences (₹2.48 Cr non-current + ₹0.41 Cr
current FY26 vs ₹1.96 Cr + ₹0.29 Cr FY25) rose in the same Labour-Codes wave. 🟢

## 10. DEFERRED TAX (Note 32, standalone p.159-160)

Effective tax rate 25.32% FY26 vs 26.75% FY25, against statutory rate 25.168% both years —
reconciling items are routine (earlier-year adjustments, permanent-nature allowances, 80JJAA
deduction, depreciation timing) — nothing unusual, no aggressive shading. 🟢. No MAT credit
mentioned anywhere (company appears to be a full taxpayer under normal provisions, not MAT).

Net deferred tax liability rose ₹77.81 Cr → ₹84.86 Cr, driven by PP&E temporary differences
(₹81.18 Cr → ₹89.91 Cr, i.e. accelerated tax depreciation on the capex build vs book depreciation)
partially offset by growing DTA on gratuity (₹1.61 Cr → ₹2.88 Cr) and ECL (₹0.66 Cr → ₹1.15 Cr).
**No unrecognised DTA disclosed** — implies management is confident all deductible temporary
differences and any carry-forwards (none disclosed) will be utilised against future taxable
profit; consistent with a profitable, growing business, and there is no realism concern raised
in the note itself. 🟢

## 11. REVENUE DETAILS

Product-wise sale of products (Note 25, standalone p.157-158): Chemicals ₹910.59 Cr (+6.1% YoY)
vs Pharmaceuticals ₹1,350.00 Cr (+15.2% YoY) vs Others ₹43.92 Cr — **pharma is growing more than
2.5x faster than chemicals at the product level**, consistent with LBF1's mix-shift thesis, though
this note does not break pharma further into ibuprofen vs non-ibuprofen (that split is only in the
investor presentations/concalls, not the AR notes). Segment note (Note 39, p.167-169) gives a
second cut, including inter-segment transfers: Chemical segment total revenue (external + inter-
segment) ₹1,160.53 Cr FY26 vs ₹1,079.39 Cr FY25 (+7.5%); Pharmaceutical external sales ₹1,396.25 Cr
vs ₹1,212.32 Cr (+15.2%). Inter-segment transfer (Chemical → Pharmaceutical, captive acetyls into
API production) ₹237.72 Cr FY26 vs ₹212.52 Cr FY25 (+11.9%) — this is the captive-transfer pricing
LBF4 asks about; **the note discloses the transfer amount but not the transfer-pricing basis**
(cost, market, or formula) — NOT FOUND IN DOCUMENT. 🟡 Watch, a direct gap against LBF4.

**Segment results: Chemical ₹30.24 Cr FY26 vs ₹15.39 Cr FY25 (+96.5%, "nearly doubled" — confirms
LBF4 verbatim), Pharmaceutical ₹172.27 Cr vs ₹126.27 Cr (+36.4%)** (Note 39, p.168). Segment EBIT
margin: Chemical 30.24/1160.53 = 2.6% FY26 vs 15.39/1079.39 = 1.4% FY25 (still thin, doubling off a
low base); Pharmaceutical 172.27/1396.25 = 12.3% FY26 vs 126.27/1212.32 = 10.4% FY25. Note that
segment results exclude "income or expenses which are non-recurring in nature and are classified
as an exceptional item" (Note 39 note (i), p.169) — **meaning the ₹11.21 Cr Labour Codes
exceptional item is NOT embedded in either segment's result**, so the chemicals doubling is a real
operating improvement, not an artifact of where the one-off landed. 🟢 clarifies Section 1's
concern for the segment-level numbers specifically (the exceptional item still hits consolidated/
standalone PBT below the segment-result line).

Geographic split (Note 39 continuation, p.169): India ₹1,754.79 Cr FY26 vs ₹1,523.12 Cr FY25
(+15.2%); Switzerland ₹52.54 Cr; Indonesia ₹47.13 Cr (+46.9% YoY, fastest-growing single
geography); Rest of world ₹464.60 Cr (-1.7% YoY, the only declining bucket) — domestic outgrew
export overall, slightly at odds with the "exports 25-30% guidance" framing; export share of
revenue ≈ 24.4% FY26 vs 26.8% FY25 (declining), worth a management question. 🟡 Watch.

No customer contributes >10% of revenue (Note 39 note (ii), confirmed also at Note 41(iii)). No
contract-asset/contract-liability roll-forward or unsatisfied-performance-obligation disclosure
found — NOT FOUND IN DOCUMENT (only "advances from customers" ₹10.70 Cr appears as a contract
liability inside Note 22 "Other current liabilities," p.157, with no further breakdown).

## 12. OTHER CRITICAL NOTES

- **Exceptional items ₹11.21 Cr** (Note 50 standalone p.178 / Note 47 consolidated p.229-230):
  Labour Codes-driven gratuity/compensated-absences past-service cost, explicitly non-recurring,
  government-mandated, ICAI-guidance-consistent treatment. One-off by construction; **watch FY27
  for any second wave** if further Labour Code rules affect other benefit heads. 🟡
- Goodwill: none exists (no hits anywhere in the AR). No intangibles impairment sensitivity issue.
- Capital commitments ₹69.35 Cr (Section 3) — foreign-currency exposure: forward contracts
  outstanding ₹181.05 Cr (USD) at 31-Mar-2026 vs ₹314.87 Cr FY25 (Note 41(a), p.173) — hedge cover
  shrinking even as the unhedged net USD trade exposure *reversed sign*, from a net receivable
  position (+₹72.29 Cr FY25) to a **net payable position (-₹124.89 Cr FY26)** on the unhedged book
  (Note 41 table, p.172) — i.e. IOL is now a net USD payer on unhedged transactions, meaning INR
  depreciation would now hurt rather than help, a reversal of the prior year's exposure direction.
  🟡 Watch — worth a treasury/FX-policy question.
- Segment reporting: covered fully in Section 11.
- Basic vs diluted EPS: **identical both years** (₹4.69 FY26, ₹3.44 FY25) — no dilution, no ESOP
  (explicitly stated the company has not granted stock options, extraction line ~10571/10683). 🟢
- Share capital: no change in issued capital this year (29,35,27,510 shares, ₹58.71 Cr, face value
  ₹2, flat both years) — the FY25 stock split (₹10 → ₹2 face value, record date 11-Mar-2025) is the
  only capital-structure event in the two-year window; **confirms LBF2's "share capital flat"
  framing at the AR level**. 🟢
- Promoter and Promoter Group shareholding (Note 15h, standalone p.155): **57.48% at 31-Mar-2026
  vs 52.63% at 31-Mar-2025 (+4.85pp)** — this is the AR's own snapshot, one quarter earlier than the
  62.28% figure quoted for Jun-2026 in company memory, so the AR captures roughly half of the total
  promoter-holding rise attributed to LBF2, with the RD-sanctioned amalgamation (Jun-2026) landing
  in the gap between AR sign-off (20-May-2026) and the Jun-2026 shareholding-pattern date. Within
  the AR window itself, NM Merchantiles rose 13.08% → 17.08% (+4.00pp) and NCVI Enterprises rose
  15.96% → 16.58% (+0.62pp) (Note 15h continuation, p.155-156) — i.e. **most of the FY26 promoter
  increase is attributable to NM Merchantiles specifically**, even before the Jun-2026 merger event.
  🔴 Red Flag candidate for deeper work: **Vasudeva Commercials Limited held 7.94% (2,33,19,295
  shares) at 31-Mar-2025 and disappears entirely from the >5% shareholder table at 31-Mar-2026**
  (Note 15c, p.153-154) — it is not named anywhere in the Note 40 related-party list either, in
  either year. The AR gives no explanation for where those shares went (below-5% dispersal, sale,
  or absorption into another holder). This name is **not** among the five LBF2 entities the company
  memory already tracks, so it is a new thread: who is Vasudeva Commercials Limited, and did its
  stake migrate into NM Merchantiles or elsewhere. Flag for stage 9/live verification.
- CSR: required ₹3.40 Cr FY26 vs ₹4.06 Cr FY25; spent ₹3.51 Cr FY26 (excess ₹0.11 Cr) vs ₹2.26 Cr
  FY25 (shortfall ₹0.56 Cr, later made up) — FY26 fully compliant with a small excess. 🟢. CSR routed
  partly through related party IOL-Foundation (₹0.94 Cr FY26 vs ₹1.56 Cr FY25) — already captured
  in Section 2.
- Direct debits/credits to reserves bypassing P&L: none found beyond the standard OCI items
  (remeasurement of defined benefit obligation, cash-flow hedge reserve) which are Ind-AS-mandated,
  not discretionary. 🟢
- Additional Regulatory Info (Note 48 standalone, p.177 / Note 45 consolidated, p.228-229): no
  benami property, no wilful-defaulter status, no crypto trading/investment, no revaluation of
  PP&E/intangibles/ROU, title deeds held in company's own name, quarterly borrowing returns align
  with books, no income surrendered in tax assessments. Clean set of standard negative
  confirmations. 🟢
- Going concern: standard boilerplate management/auditor language only (Note 2(i).I; auditor's
  report going-concern paragraphs) — **no material uncertainty flagged, no emphasis-of-matter
  paragraph, no qualified/adverse/disclaimer opinion, no fraud reported by auditors** (extraction
  line ~8698). 🟢

---

## PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

1. **Promoter shareholding rose 52.63% → 57.48% within the AR year itself (Note 15h, p.155-156)**,
   driven mainly by NM Merchantiles (+4.00pp) and NCVI Enterprises (+0.62pp) — this predates and
   partially explains the Jun-2026 62.28% figure in company memory. 🟡 Watch, LBF2-load-bearing.
2. **Vasudeva Commercials Limited (7.94% at 31-Mar-2025) vanishes from the >5% shareholder table
   at 31-Mar-2026 with no AR explanation and no related-party classification either year**
   (Note 15c, p.153-154). 🔴 Red Flag candidate — new thread beyond the five LBF2 names already
   tracked.
3. **Related-party purchases from the three named promoter-group entities rose 31.1% YoY to
   ₹131.94 Cr (8.8% of material consumed), with NM Merchantiles' purchase value nearly tripling**
   (₹7.37 Cr → ₹22.52 Cr) in the same year its shareholding jumped (Note 40, p.169-170). 🟡 Watch.
4. **₹11.21 Cr exceptional item from Labour Codes-driven gratuity/compensated-absences past
   service cost** (Note 50/47, p.178/p.229-230) is excluded from segment results but hits
   consolidated/standalone PBT — must be normalised out for any YoY margin comparison. 🟡 Watch.
5. **Chemicals segment result nearly doubled (₹15.39 Cr → ₹30.24 Cr) net of the exceptional item,
   confirming LBF4**, while Pharmaceutical segment result grew a more modest 36.4%; captive
   inter-segment transfer pricing basis (chemicals → pharma, ₹237.72 Cr FY26) is not disclosed
   (Note 39, p.168-169). 🟡 Watch — direct LBF4 gap.
6. **Zero term/long-term debt on the balance sheet in either year; only ₹132 Cr working-capital
   borrowing**, against a guided ₹500 Cr + ₹1,200-1,400 Cr "internally funded" capex programme
   (Note 19/41/42, p.156/173-174). No funding facility for the greenfield is yet visible in this
   AR. 🟡 Watch, LBF3-load-bearing.
7. **Trade receivables grew 17.7% YoY (₹516.32 Cr → ₹607.72 Cr gross) against 11.5% revenue
   growth**, while ECL allowance nearly doubled (₹2.63 Cr → ₹4.59 Cr) — receivables outrunning
   revenue is the mechanism behind the debtor-days trend already flagged in company memory
   (Note 10, p.152). 🟡 Watch, feeds FLAG-CASH.
8. **Net foreign-currency exposure reversed from a net USD receivable (+₹72.29 Cr FY25) to a net
   USD payable (-₹124.89 Cr FY26) on the unhedged book**, even as total forward-hedge cover shrank
   from ₹314.87 Cr to ₹181.05 Cr (Note 41, p.172-173). 🟡 Watch — reversed FX sensitivity direction.
9. **New customs Order-In-Original, ₹2.06 Cr aggregate demand/penalty for incorrectly availed
   ASEAN-India FTA exemption**, company appealing (Note 35 footnote, p.161) — likely the same
   matter as the 09-May-2026 BSE filing in the corpus manifest; small quantum, compliance-process
   finding. 🟡 Watch.
10. **Clean audit opinion, no going-concern uncertainty, no fraud, no material weakness, no
    goodwill, no ESOP dilution, no related-party loans, CSR fully compliant, inventory and payable
    days both improving** — the note set overall shows disciplined, unshaded disclosure quality
    with no aggressive accounting signals. 🟢 Foundation finding: the promoter/receivables/capex-
    funding items above are the real watch list, not a broader accounting-quality concern.

---

*Pass 1 complete. Proceeding to Pass 2 (what was missed) in the next call.*
