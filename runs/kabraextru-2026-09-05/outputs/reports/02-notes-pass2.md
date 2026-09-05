# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 2: WHAT WAS MISSED
Company: Kabra Extrusiontechnik Ltd (KABRAEXTRU) | Run date: 2026-09-05
Source: Annual Report FY2025-26 (`Annual_Report_2026.txt`/`.pdf`). Figures in ₹
Lakhs in the source; converted to ₹ Crores (Lakhs ÷ 100) per pipeline
instruction, lakh figure shown on first use. Ratings: 🟢 Clean | 🟡 Watch |
🔴 Red Flag. This pass reports ONLY items not already covered in Pass 1
(`02-notes-pass1.md`). Where a Pass-1 item is referenced only to anchor new
context, it is marked "[Pass 1 context, not re-counted]".

═══════════════════════════════════════════════════════════════════
## NOTE 1 — ACCOUNTING POLICIES (standalone p.72-79 / consolidated p.127-134)
═══════════════════════════════════════════════════════════════════

**Government Grant policy is internally contradictory (Note 1(m) standalone
p.76, Note 1(p) consolidated p.130) — MISSED in Pass 1.** The policy states:
"When the grant relates to an asset, it is treated as deferred income and
recognised in the Statement of Profit and Loss on a systematic basis over the
useful life of the asset using capital approach." This conflates the two
mutually exclusive Ind AS 20 treatments in one sentence — "deferred income
recognised in P&L over useful life" is the INCOME approach; "capital
approach" is the alternative method of netting the grant against the asset's
carrying value. The treatment actually applied (see Note 2A/2C below) is the
capital approach (asset-netting), not deferred income. 🟡 Watch — drafting
imprecision in a policy note, not a numeric misstatement, but symptomatic of
the QC pattern Pass 1 flagged (dating defects, stale RPT copies).

═══════════════════════════════════════════════════════════════════
## NOTE 2A/2C — PPE / INTANGIBLES, NOTE 23/31 OTHER INCOME — GOVERNMENT
   INCENTIVE (MISSED ENTIRELY IN PASS 1)
═══════════════════════════════════════════════════════════════════

**FY25 profit and asset base were flattered by a ₹17.07 Cr one-time
Maharashtra government incentive, entirely absent in FY26; Pass 1 did not
extract this anywhere.** Note 23 (Other Income, standalone p.95) / Note 23
(consolidated p.152) footnote, verbatim: "The Company has received an
incentive under 'Modified Special Incentive Package' Scheme amounting to
₹17.07 crores during the year [FY25], out of which ₹16.37 crores have been
adjusted against the carrying value of eligible Property, Plant and Equipment
and Intangible Assets using Capital Approach and ₹0.70 crores are being
recognised as income in the Profit and Loss Account."

This reconciles exactly to two items Pass 1 did not connect to this cause:
- Note 2A PPE roll-forward (standalone p.82): FY25 "Government Incentive
  (Adjustments)" line reduces gross block by ₹1,513.56 Lakh (₹15.14 Cr)
  across Building (-₹90.25L), Plant & Equipment (-₹1,416.22L), Furniture
  (-₹4.01L), Office Equipment (-₹0.62L), Computer (-₹2.46L). FY26 shows
  ₹0 in this line for every category — the incentive did not recur.
- Note 2C Intangibles roll-forward (standalone p.83): FY25 "Government
  Incentive (Adjustments)" reduces gross block by ₹124.15 Lakh (₹1.24 Cr).
  ₹15.14 Cr + ₹1.24 Cr = ₹16.38 Cr ≈ the ₹16.37 Cr capitalised portion cited
  in the Note 23 footnote.
- Note 23 Other Income (standalone/consolidated): "Government Incentive"
  line shows ₹70.00 Lakh (₹0.70 Cr) FY25, ₹0 FY26 — the direct P&L portion.

This is a material YoY earnings-comparability item that Pass 1's segment and
D&A analysis did not surface: FY25's reported profitability benefited from a
₹17.07 Cr non-recurring government incentive (mostly capitalised, which also
lowered FY25's depreciation base relative to what it otherwise would have
been), none of which repeated in FY26. 🟡 Watch — legitimate incentive, but a
significant comparability distortion with zero cross-reference from the
segment or MD&A-adjacent notes.

═══════════════════════════════════════════════════════════════════
## NOTE 2E / NOTE 29 / NOTE 40 — NEW LEASE, UNIDENTIFIED (MISSED IN PASS 1)
═══════════════════════════════════════════════════════════════════

**A large new lease was taken in FY26 with zero narrative identifying it.**
Note 2E ROU assets (standalone p.84): gross carrying amount rose 147.9%
(₹277.61 Lakh → ₹688.09 Lakh, i.e. ₹2.78 Cr → ₹6.88 Cr); net carrying amount
rose from ₹2.78 Cr to ₹3.71 Cr. Note 40 (Leases, standalone p.107-108): lease
liability additions of ₹409.78 Lakh (₹4.10 Cr) in FY26 (vs ₹267.81 Lakh
FY25); lease payments made jumped 780.9% (₹34.15 Lakh → ₹300.82 Lakh, i.e.
₹0.34 Cr → ₹3.01 Cr). Depreciation on ROU assets appears for the first time
at a meaningful level: ₹270.35 Lakh (₹2.70 Cr) FY26 vs ₹46.27 Lakh FY25.
Corresponding "Rent" expense (Note 29, standalone p.96) FELL 88.2% (₹120.63
Lakh → ₹14.21 Lakh) — consistent with a new arrangement being capitalised
under Ind AS 116 rather than expensed as rent (a reclassification, not a
real cost saving). The notes only generically describe leased assets as
"office buildings & warehouses" on 3-5 year tenures (Note 40 narrative,
standalone p.107) — no property, location, or business-segment link (e.g.
Battery Division) is disclosed. NOT FOUND IN DOCUMENT (which segment/site).
🟡 Watch — meaningful new leased-asset base with no narrative context, in
the same year capital commitments rose 22x (Pass 1 Section 3).

═══════════════════════════════════════════════════════════════════
## NOTE 4 / NOTE 39D(i) — GROWING NON-EQUITY EXPOSURE TO VAROS (PARTIALLY
   MISSED)
═══════════════════════════════════════════════════════════════════

- Note 4 (Other Financial Assets, non-current, standalone p.85): a security
  deposit of ₹20.35 Lakh (₹0.2035 Cr) given to Kolsite Corporation LLP
  (promoter entity), unchanged both years — disclosed in Note 4 but not
  cross-referenced to, or repeated in, the Note 39 RPT balance tables Pass 1
  extracted. 🟡 Watch (minor, completeness gap).
- Note 39D(i) Debit Balance Outstanding (standalone p.106): Varos Technology
  debit balance rose 50.1% (₹41.40 Lakh → ₹62.12 Lakh, ₹0.4140 Cr → ₹0.6212
  Cr) — an additional, smaller trade/other receivable exposure to the
  subsidiary Pass 1 already flagged as insolvent-on-a-standalone basis,
  layered on top of the ₹13.32 Cr cumulative equity+CCD funding. Also: a
  residual debit balance of ₹0.56 Lakh (FY26) / ₹1.10 Lakh (FY25) is still
  owed by Penta Auto Feeding India Ltd, roughly 19 months after it ceased to
  be a related party (6-Feb-2025) — unexplained residual balance from a
  divested entity. Kabra Energy also carries a small, growing debit balance
  (₹0.53 Lakh FY26 vs ₹0.34 Lakh FY25). None of these three balances were in
  Pass 1's RPT receivables cross-reference. 🟡 Watch.

═══════════════════════════════════════════════════════════════════
## NOTE 6 — CAPITAL ADVANCES NEARLY TRIPLED (QUANTIFIES A PASS-1 FLAG)
═══════════════════════════════════════════════════════════════════

Capital advances (Other Non-current Assets, standalone p.87) rose 175.9%:
₹433.44 Lakh (₹4.33 Cr) FY25 → ₹1,196.09 Lakh (₹11.96 Cr) FY26. Pass 1
flagged the aggregate ₹31.77 Cr Note 41(b) capital commitment as a Red Flag
with "zero narrative context"; this note quantifies the advance-payment
leading indicator for the first time — capital advances given to vendors
nearly tripled, corroborating an active capex ramp (still unexplained by
segment). 🟡 Watch — new supporting quantum, not a new theme.

═══════════════════════════════════════════════════════════════════
## NOTE 10/10A — CASH POSITION IS EXTREMELY THIN (MISSED IN PASS 1)
═══════════════════════════════════════════════════════════════════

Standalone actual Cash and Cash Equivalents (Note 10, p.86): just ₹197.17
Lakh (₹1.97 Cr) FY26 (₹194.92 Lakh, ₹1.95 Cr FY25) — essentially flat and
trivially small against ₹140.92 Cr of secured, on-demand short-term
borrowings (Pass 1, Section 7). Pass 1's liquidity narrative referenced the
₹53.49 Cr → ₹22.59 Cr mutual-fund drawdown but never stated the underlying
bank-cash balance. Separately, Note 10A "Other Balances with Banks" — margin
money/security deposits with 3-12 month maturity — FELL 86.4% (₹521.02 Lakh
→ ₹70.98 Lakh, ₹5.21 Cr → ₹0.71 Cr) in the same year Note 41(a) bank
guarantees nearly doubled (Pass 1, ₹11.33 Cr → ₹21.89 Cr). (Cross-checked:
the broader "Other balances with banks" figure of ₹369.94 Lakh used in the
Note 34.3(b) liquidity table also includes Note 12's short-term bank
deposits and reconciles cleanly — not an inconsistency, just a wider
definition.) 🟡 Watch, feeds FLAG-CASH — actual cash buffer is thinner than
the mutual-fund figures alone suggest.

═══════════════════════════════════════════════════════════════════
## NOTE 16(a) — MOOWR CUSTOMS DUTY DEFERRAL, ₹8.41 CR (MISSED ENTIRELY)
═══════════════════════════════════════════════════════════════════

**A ₹840.53 Lakh (₹8.4053 Cr) "Other Non-current liabilities" balance,
unchanged both years, was not extracted by Pass 1 at all.** Note 16(a)
(standalone p.90, consolidated equivalent): "The other dues pertain to the
'Manufacturing and Other Operations in Warehouse Regulations' (MOOWR)
scheme. Under this scheme, the Basic Customs Duty and IGST on the import of
the plant & Machinery are deferred until the goods are cleared for home
consumption." This is a real, quantified customs/IGST deferral liability
tied to imported plant & machinery held under a bonded-manufacturing scheme
— it crystallises as a cash outflow if/when the underlying machinery is
cleared for domestic use rather than re-exported or kept within the scheme.
Static at ₹8.41 Cr for two years suggests the underlying machinery has not
yet been cleared for home consumption. NOT in Pass 1's contingent-liability
or borrowings sections. 🟡 Watch — new, quantified, unflagged deferred
duty exposure.

═══════════════════════════════════════════════════════════════════
## NOTE 22/23/26/27/28/29 — P&L LINE-ITEM DETAIL MISSED IN PASS 1
═══════════════════════════════════════════════════════════════════

**1. Unexplained ~73x jump in generic "Other" income — the single largest
new finding of this pass.** Note 23 Other Income (standalone p.95): "Other"
₹1,668.41 Lakh (₹16.68 Cr) FY26 vs ₹22.91 Lakh (₹0.23 Cr) FY25. Verified
identical in substance at the consolidated level: Note 23 consolidated
(p.152) shows "Others" ₹1,668.10 Lakh (₹16.68 Cr) FY26 vs ₹22.91 Lakh FY25.
No footnote, sub-schedule, or narrative anywhere in the standalone or
consolidated notes explains the composition of this line (searched both
statements; only the adjacent "Government Incentive" line has a footnote).
Given standalone PBT was a loss of ₹(4.2321) Cr and consolidated PBT was
worse, a ₹16.68 Cr unexplained "Other" income credit is material to the
year's headline result — without it, the pre-tax position would have been
dramatically worse on a comparable basis. NOT FOUND IN DOCUMENT (composition
of "Other"/"Others"). 🔴 Red Flag — the most consequential gap this pass
found; a priority question for management.

**2. Depreciation & amortisation nearly doubled — not discussed anywhere in
Pass 1.** Note 28 (standalone p.94): Depreciation on owned PPE ₹2,498.55
Lakh (₹24.99 Cr) FY26 vs ₹1,298.83 Lakh (₹12.99 Cr) FY25, +92.4%;
Depreciation on ROU assets ₹270.35 Lakh (new, nil FY25); Amortisation of
intangibles ₹174.06 Lakh vs ₹244.44 Lakh, -28.8%. TOTAL D&A: ₹2,956.87 Lakh
(₹29.57 Cr) FY26 vs ₹1,557.18 Lakh (₹15.57 Cr) FY25, +89.9% (+₹14.00 Cr).
This single cost line change is comparable in magnitude to the segment-loss
swing Pass 1 identified as the #1 finding, and mechanically explains a large
share of the FY26 PBT collapse from ₹41.92 Cr (FY25) to a ₹(4.23) Cr loss.
Unlike a one-off charge, this is a structural step-up in the depreciation
base from the capex ramp (Plant & Equipment additions of ₹63.03 Cr, Note
2A) — future years will carry this higher D&A base too. 🟡 Watch — material
context for normalising forward earnings; not itself an accounting-quality
defect, but its absence from Pass 1's earnings-bridge is a real gap.

**3. Employee costs +20.4% and Other Expenses +15.1% against revenue -7.9%
— broad-based cost inflation beyond the Battery Division.** Note 26
(standalone p.92): Salaries ₹7,089.17 Lakh (₹70.89 Cr) vs ₹6,068.58 Lakh
(₹60.69 Cr), +16.8%; "Contribution to provident and other funds" ₹528.29
Lakh (₹5.28 Cr) vs ₹260.09 Lakh (₹2.60 Cr), +103.1%. This jump is
substantially explained by Note 37.1(b)(i)'s ₹233.15 Lakh (₹2.33 Cr) gratuity
Past Service Cost (new labour code) plus Current Service Cost rising ₹103.88
Lakh vs ₹82.25 Lakh — Pass 1 flagged the ₹2.33 Cr past-service cost in
isolation but did not trace it into the 103% jump in this P&L line. Total
employee benefit expense: ₹7,617.46 Lakh (₹76.17 Cr) vs ₹6,328.67 Lakh
(₹63.29 Cr), +20.4%. Separately, Note 29 Other Expenses (standalone p.96)
rose 15.1% (₹8,114.64 Lakh vs ₹7,052.77 Lakh) driven by Sales Promotion
+284.1% (₹174.21 Lakh → ₹669.08 Lakh), Contract Labour Charges +27.5%
(₹1,033.98 Lakh → ₹1,317.84 Lakh), Legal & Professional +22.8% (₹378.68 Lakh
→ ₹464.94 Lakh), and Travelling +19.4% (₹769.88 Lakh → ₹918.90 Lakh) — a
broad-based cost inflation across discretionary lines while revenue fell,
not confined to the Battery Division segment loss Pass 1 identified. 🟡
Watch — margin-compression driver additional to the segment story.

**4. Finance costs stayed nearly flat (+2.0%) despite gross debt +12.2%,
because bill discounting/factoring collapsed.** Note 27 (standalone p.93):
Bill discounting & factoring charges fell 94.7% (₹175.47 Lakh → ₹9.23 Lakh),
offsetting a 16.0% rise in plain interest expense (₹914.04 Lakh → ₹1,059.88
Lakh). Consistent with the 89.4% collapse in export receivables Pass 1 noted
elsewhere; the company appears to have largely stopped factoring/discounting
export bills. 🟡 Watch, minor — explains an otherwise puzzling "flat finance
cost despite rising debt" pattern.

**5. "Sale of Services" revenue nearly doubled off a small base.** Note 22
(standalone p.92): Sale of products ₹44,073.43 Lakh (₹440.73 Cr) vs
₹46,935.32 Lakh (₹469.35 Cr), -6.1%; Sale of Services ₹564.76 Lakh (₹5.65
Cr) vs ₹295.35 Lakh (₹2.95 Cr), +91.2%. A mix shift toward maintenance/service
revenue as machinery sales slow — the one mildly positive new data point
this pass found. 🟢/🟡. Export incentive within "Other Operating Revenue"
fell 12.7% (₹85.49 Lakh → ₹74.65 Lakh), consistent with the export decline.

═══════════════════════════════════════════════════════════════════
## NOTE 29/30 — THIRD, MUTUALLY CONTRADICTORY CSR-SPEND FIGURE, STANDALONE
   ONLY (NEW RED FLAG, MISSED IN PASS 1)
═══════════════════════════════════════════════════════════════════

Pass 1 accepted the standalone CSR figures at face value. On a full re-read,
THREE different numbers appear for the same FY26 CSR spend within the
standalone statements alone:
- Note 29 (Other Expenses, P&L line, p.96): "Contributions towards CSR
  (Refer note 29)" = ₹82.59 Lakh.
- Note 30 CSR sub-note table, item (e) "Amount of expenditure incurred
  during the year" (p.96) = ₹69.66 Lakh.
- Note 30 CSR narrative sentence (p.96), verbatim: "The Company has
  contributed ₹85.59 Lakhs (31 March 2024: ₹99.95 Lakhs) towards Corporate
  Social Responsibility (CSR)..." — a THIRD figure, and the prior-year date
  is also wrong ("31 March 2024" should read "31 March 2025": the FY25
  spend of ₹99.95/99.94 Lakh is the correct comparative, one year removed
  from FY26, not two).

Cross-checked against the CONSOLIDATED Note 30 (p.151), which gets this
right: "The Company has contributed ₹69.66 Lakhs (31 March 2025: ₹99.94
Lakhs)" — matching its own table exactly and using the correct date. This
means the STANDALONE Note 30 narrative sentence is uniquely wrong on two
counts (figure and date) relative to its own table AND relative to the
consolidated version of the identical sentence. This is a clean, fully
cross-referenced arithmetic/dating error in the audited standalone
financial statements — a fourth/fifth instance of the "internal
inconsistency" pattern Pass 1's top finding #10 identified, but this is the
first instance found IN THE STANDALONE accounts rather than only in the
consolidated ones, meaning the QC weakness is not confined to
consolidation-copy errors. 🔴 Red Flag.

═══════════════════════════════════════════════════════════════════
## NOTE 29/31 — AUDITOR REMUNERATION MISMATCH, CURRENT YEAR ONLY (NEW,
   MINOR)
═══════════════════════════════════════════════════════════════════

Note 29 "Payment to Auditor" P&L line (standalone p.96) shows ₹12.50 Lakh
FY26, but Note 31 Auditor's Remuneration (p.97) itemises Audit Fees ₹5.00 +
Limited Review ₹7.50 + Tax Audit Fees ₹0.50 + Certification ₹0.50 +
Reimbursement ₹1.38 = ₹14.88 Lakh — a ₹2.38 Lakh (₹0.0238 Cr) gap. The FY25
comparative ties out exactly in both notes (₹12.00 Lakh = ₹12.00 Lakh). 🟡
Watch — small quantum, but an isolated, current-year-only internal
inconsistency, consistent with the broader QC theme.

═══════════════════════════════════════════════════════════════════
## NOTE 38 — SEGMENT LIABILITIES SHARPEN THE CAPITAL-EFFICIENCY RED FLAG
   (PASS 1 PARTIALLY COVERED, NEW COMPUTATION HERE)
═══════════════════════════════════════════════════════════════════

Pass 1 compared only gross segment ASSETS (Extrusion ₹363.38 Cr vs Battery
₹364.37 Cr, "near parity"). Note 38 (standalone p.106) also discloses
segment LIABILITIES, not previously extracted: Extrusion ₹12,107.34 Lakh
(₹121.07 Cr) vs Battery ₹5,256.96 Lakh (₹52.57 Cr). Netting the two: Battery
Division's NET segment capital (assets less liabilities) is ₹311.80 Cr
(₹36,437.25L - ₹5,256.96L) versus Extrusion's ₹242.31 Cr (₹36,338.05L -
₹12,107.34L) — the loss-making Battery Division actually ties up MORE net
capital than the profitable Extrusion Machinery business, a sharper and
previously uncomputed version of Pass 1's capital-efficiency red flag (#1).
🔴 Red Flag — refines an existing Pass 1 finding with a materially worse
number than the gross-asset comparison implied.

═══════════════════════════════════════════════════════════════════
## NOTE 39C — RELATED PARTY TRANSACTION TABLE WAS MATERIALLY INCOMPLETE IN
   PASS 1 (NEW LINE ITEMS, INCLUDING A FIRST-TIME CATEGORY)
═══════════════════════════════════════════════════════════════════

Pass 1's RPT summary table (Section 2) captured a subset of Note 39C
(standalone p.105-106). A full re-read surfaces at least eight further line
items Pass 1 did not extract:
- Kabra Mecanor Belling Technik (JV): Reimbursement Income ₹1.07 Lakh FY26
  vs ₹1.95 Lakh FY25 (-45.1%) — separate from the "Rent income" line Pass 1
  already had.
- Kolsite Corporation LLP (promoter): Reimbursement Expenses ₹2.24 Lakh FY26
  vs ₹2.19 Lakh FY25 — a category Pass 1 did not list at all for this party.
- Maharashtra Plastics & Ind.: Purchase of goods & Services ₹0 FY26 vs
  ₹0.05 Lakh FY25; Rent Income ₹2.01 Lakh FY26 vs ₹1.80 Lakh FY25 — both
  new to Pass 1's table (which had only the "Sales of goods & services"
  line for this party).
- Plastiblends India Ltd (promoter cross-holding): Purchase of goods &
  Services ₹8.43 Lakh FY26 vs ₹12.58 Lakh FY25 (-33.0%); Rent Expense ₹14.86
  Lakh FY26 vs ₹13.53 Lakh FY25 (+9.8%); Rent Income ₹3.03 Lakh FY26 vs
  ₹3.94 Lakh FY25 (-23.1%); Reimbursement Income ₹0.36 Lakh FY26 vs ₹15.84
  Lakh FY25 (-97.7%) — none of these four lines were in Pass 1's table.
- **New this year: Plastiblends India Ltd, Reimbursement Expense ₹16.68
  Lakh FY26 vs NIL FY25** — a related-party expense category that did not
  exist in the prior year, appearing for the first time in FY26 with no
  narrative explaining its nature. 🟡 Watch — a genuinely new RPT category,
  modest in quantum but new in kind.

This does not change Pass 1's qualitative RPT conclusions (no
non-arm's-length signal evident, no loans to promoters) but the completeness
gap itself, and specifically the first-time Plastiblends reimbursement-
expense line, are worth surfacing. 🟡 Watch.

═══════════════════════════════════════════════════════════════════
## NOTE 34.3(c) — CURRENCY COMPOSITION OF THE UNHEDGED FX EXPOSURE (ADDS
   THE "WHY" TO A PASS-1 RED FLAG)
═══════════════════════════════════════════════════════════════════

Pass 1 flagged the 6.8x growth in unhedged net FX exposure (₹-5.61 Cr to
₹-38.21 Cr) using only the combined figure and a USD-only sensitivity. Note
34.3(c)(i) (standalone p.101) gives the currency breakdown Pass 1 did not
extract: USD net liability ₹(2,135.08) Lakh (₹21.35 Cr), EUR net liability
₹(1,401.75) Lakh (₹14.02 Cr), CNH (Chinese Yuan) net liability ₹(283.81)
Lakh (₹2.84 Cr). The CNH exposure is effectively BRAND NEW: it was only
₹(0.41) Lakh at FY25 (trivial) and grew ~690x to ₹(283.81) Lakh at FY26 —
consistent with rising Chinese-sourced import content (plausibly battery
cell/component sourcing for the Battery Division), though the notes do not
state this. EUR sensitivity (5% move) also rose 17.5x (₹4.00 Lakh → ₹70.09
Lakh). NOT FOUND IN DOCUMENT (narrative link to Battery Division sourcing).
🟡 Watch — adds the currency-composition "why" behind an existing Pass 1 red
flag; the new CNH exposure specifically is worth a management question.

═══════════════════════════════════════════════════════════════════
## NOTE 43 — RATIOS PASS 1 DID NOT CITE (CURRENT RATIO, ROCE, ROE, NET
   PROFIT RATIO, AND A MISMATCHED DSCR "REASON")
═══════════════════════════════════════════════════════════════════

Pass 1's Section 4/5/8 cited only the turnover ratios (inventory, trade
receivables, trade payables, net capital turnover). Note 43 (standalone
p.108, consolidated p.166-167) discloses five further company-computed
ratios not previously extracted:
- Current Ratio: 1.55x (FY26) vs 1.67x (FY25), -7.2% — a new, unflagged
  liquidity-trend data point consistent with the working-capital
  deterioration theme already established.
- Return on Capital Employed: 1.20% (FY26) vs 8.90% (FY25), -86.5%.
- Return on Equity: -0.54% (FY26) vs 7.40% (FY25), -107.2%.
- Net Profit Ratio: -0.55% (FY26) vs 7.18% (FY25), -107.6%.
- Debt Service Coverage Ratio: 14.36x (FY26) vs 10.32x (FY25), +39.2%
  IMPROVEMENT — but the note's own stated "Reason" column reads "Due to
  generate lower net operating income," which describes a DETERIORATION,
  not the improvement the ratio itself shows. This is an internally
  contradictory disclosure (the explanatory text does not match the
  direction of the number it is meant to explain) — likely a templated
  explanation applied without adapting to this particular ratio's actual
  movement (the DSCR improved because scheduled debt service collapsed
  after the Pune term loan was fully repaid, per Pass 1 Section 7, a
  bigger effect than the fall in operating earnings). 🟡 Watch — a further,
  isolated instance of the drafting-QC pattern; the standalone-only ROCE/ROE/
  Net Profit figures are useful new quantification of the year's
  profitability collapse.

═══════════════════════════════════════════════════════════════════
## NOTE 45 (CONSOLIDATED) — SCHEDULE III ADDITIONAL INFORMATION: TOTAL
   COMPREHENSIVE LOSS IS MORE THAN DOUBLE THE NET LOSS PASS 1 CITED
═══════════════════════════════════════════════════════════════════

Pass 1's top finding #2 cited the consolidated NET loss of ₹(5.3659) Cr and
Varos's 54.32% share of it. Note 45 (consolidated, p.167-168), which Pass 1
referenced only for the profit/loss split, also discloses:
- Consolidated TOTAL comprehensive loss for FY26: ₹(1,215.59) Lakh
  (₹12.1559 Cr) — more than double the ₹5.37 Cr net loss, because a ₹679.00
  Lakh (₹6.79 Cr) OCI loss (the FVOCI mark-down on the Plastiblends stake,
  per Pass 1 Section 6) sits entirely at the parent level (100.00% of
  consolidated OCI) and is not captured in the net-profit-only framing.
- Consolidated net worth: ₹44,148.25 Lakh (₹441.4825 Cr) FY26 vs ₹46,238.15
  Lakh (₹462.3815 Cr) FY25, -4.5% YoY — a precise consolidated net-worth
  figure not previously stated (Pass 1 used the standalone net worth of
  ₹447.3769 Cr for its contingent-liability ratio).
- **Nuance on Pass 1's #2 finding:** Varos's SHARE of consolidated loss
  ballooned from -6.87% (FY25) to 54.32% (FY26), but Varos's own absolute
  loss only grew from ₹221.24 Lakh to ₹291.49 Lakh (+31.7%) — the dramatic
  percentage swing is driven mainly by the collapse in the PARENT's own
  result (from a ₹3,441.67 Lakh consolidated profit contribution to a
  ₹(244.91) Lakh loss contribution), which shrank the denominator, not
  primarily by Varos deteriorating further. Both points are true and not
  mutually exclusive, but the percentage alone (as Pass 1 stated it) can
  overstate how much worse Varos itself got year-on-year. 🟡 Watch,
  informational — refines rather than contradicts Pass 1.

═══════════════════════════════════════════════════════════════════
## NOTE 16 — STANDALONE NON-CURRENT PROVISIONS SUB-LINES POSSIBLY A STRAY
   CONSOLIDATED-NOTE COPY (EXTENDS AN EXISTING PASS 1 OBSERVATION)
═══════════════════════════════════════════════════════════════════

Pass 1 already flagged that the standalone Note 16 provisions breakdown was
"harder to parse from the extracted text" but concluded the balance-sheet
total tied (₹423.28 Lakh) and did not flag an error. On a second look, the
standalone Note 16 table (p.89) shows sub-lines "Provision for employee
benefits" ₹144.07 Lakh / ₹102.02 Lakh, "Compensated Absences" ₹19.30 Lakh
(flat), and "Other Employee Benefits" ₹259.91 Lakh / ₹541.03 Lakh (-52.0%)
ABOVE the "Provision for Long term Warranty" line (₹423.28 Lakh / ₹662.35
Lakh) that alone equals the standalone balance-sheet total (verified against
the Balance Sheet: standalone non-current Provisions = ₹423.28 Lakh exactly,
line 3866 of the balance sheet). The ₹144.07 Lakh and ₹259.91 Lakh figures
are IDENTICAL to two of the three components that DO sum correctly to the
CONSOLIDATED non-current provisions total (₹144.07L + ₹33.03L + ₹259.91L =
₹437.01L, matching the consolidated balance sheet exactly, as Pass 1 noted).
This raises the possibility that the standalone note's employee-benefit
sub-lines are a stray carry-over from the consolidated note rather than
standalone-only figures — a further, more granular instance of the
"stale copy between statements" pattern Pass 1's top finding #10 already
named, though here embedded within a single note's own sub-totals rather
than between the two full statements. 🟡 Watch — presented as a refinement
of an existing observation, not a new standalone conclusion, given the
genuine ambiguity in how the table is laid out.

═══════════════════════════════════════════════════════════════════
## MINOR / CONTEXT-ONLY ITEMS (not separately rated, recorded for
   completeness)
═══════════════════════════════════════════════════════════════════

- Note 14.4: Kolsite Corporation LLP (promoter entity) trimmed its own
  holding slightly during FY26 (3,828,888 → 3,807,295 shares, 10.95% →
  10.89%, -0.06pp) even as overall promoter holding rose via the
  Shreevallabh Kabra Family Trust transfer Pass 1 already described — a
  small, previously unstated promoter-ENTITY reduction running alongside
  the intra-family transfer.
- Note 39E: KMP received ₹2.4079 Cr of the total ₹8.74 Cr dividend paid
  during FY26 (down from ₹4.2954 Cr of the FY25-paid amount) — quantifies
  promoter-family dividend receipts in the same note Pass 1 covered for
  remuneration; not a red flag on its own.
- Note 39: the "no transactions" related-party list includes three entities
  Pass 1 did not name — Smartech Global Solution Ltd, Kabra Gloucester
  Engineering Ltd, and Taiyou Green Solutions Pvt Ltd — alongside VTRO
  Motors (already flagged by Pass 1) and Kolsite Industries. All show zero
  transactions and, where disclosed, static/trivial balances; noted for
  completeness only.
- Note 45 (standalone, p.110/168) IEPF transfer confirmation ("All amounts
  which became due... have been transferred to that fund") is boilerplate
  and consistent with Note 19's ₹4.02 Lakh unclaimed-dividend-to-IEPF
  disclosure; not separately flagged by Pass 1 but immaterial.

═══════════════════════════════════════════════════════════════════
## PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════════

1. **Unexplained ~73x jump in "Other" income to ₹16.68 Cr (FY26) from ₹0.23
   Cr (FY25), identical in both standalone and consolidated statements, with
   zero composition disclosure anywhere in the notes** — material to a
   loss-making year. (Note 23, standalone p.95 / consolidated p.152). 🔴 Red
   Flag.

2. **Total depreciation & amortisation nearly doubled: ₹29.57 Cr (FY26) vs
   ₹15.57 Cr (FY25), +89.9% (+₹14.00 Cr), driven by owned-PPE depreciation
   +92.4%** — a structural, recurring step-up from the capex ramp that
   mechanically explains much of the FY26 PBT collapse and was absent from
   Pass 1's earnings-bridge analysis. (Note 28, standalone p.94). 🟡 Watch.

3. **FY25 earnings and asset base were flattered by a one-time ₹17.07 Cr
   Maharashtra government incentive (₹16.37 Cr netted against PPE/
   intangibles gross block, ₹0.70 Cr direct P&L income), entirely absent in
   FY26 and not mentioned anywhere in Pass 1** — a material YoY earnings-
   comparability distortion. (Note 23 footnote + Note 2A/2C, standalone
   p.82-83/95). 🟡 Watch.

4. **A third, mutually contradictory FY26 CSR-spend figure and a wrong
   prior-year date, found only in the standalone accounts** — Note 29 says
   ₹82.59 Lakh, Note 30's table says ₹69.66 Lakh, Note 30's own narrative
   says ₹85.59 Lakh and misdates the comparative as "31 March 2024"; the
   CONSOLIDATED Note 30 gets both the figure (₹69.66 Lakh) and date right.
   (Notes 29/30, standalone p.96, cf. consolidated p.151). 🔴 Red Flag.

5. **Battery Division ties up MORE net segment capital (assets less
   liabilities) than the profitable Extrusion Machinery division: ₹311.80
   Cr vs ₹242.31 Cr** — a sharper, previously uncomputed refinement of Pass
   1's capital-efficiency red flag, using segment liabilities Pass 1 did not
   net against segment assets. (Note 38, standalone p.106). 🔴 Red Flag.

6. **Employee benefit expense +20.4% and Other Expenses +15.1% against
   revenue -7.9%**, with "Contribution to provident and other funds" more
   than doubling (+103.1%, largely gratuity past-service cost) and Sales
   Promotion expense nearly quadrupling (+284.1%) — broad-based cost
   inflation beyond the Battery Division segment loss, not discussed in
   Pass 1. (Notes 26, 29, standalone p.92/96). 🟡 Watch.

7. **A new, unexplained ₹8.41 Cr MOOWR customs/IGST duty-deferral liability
   on imported plant & machinery, static for two years, entirely missed by
   Pass 1.** (Note 16(a), standalone p.90). 🟡 Watch.

8. **A new lease was taken in FY26 (ROU gross carrying amount +147.9%,
   lease payments +780.9%) with no property, location, or segment
   identified in the notes; the offsetting 88.2% fall in "Rent" expense is
   a reclassification under Ind AS 116, not a real cost saving.** (Notes 2E/
   29/40, standalone p.84/96/107-108). 🟡 Watch.

9. **RPT disclosure (Note 39C) was materially more extensive than Pass 1's
   table captured — at least eight additional line items, including a
   brand-new FY26-only "Reimbursement Expense to Plastiblends India Ltd"
   (₹16.68 Lakh, nil FY25).** (Note 39C, standalone p.105-106). 🟡 Watch.

10. **Standalone cash & cash equivalents are just ₹1.97 Cr against ₹140.92
    Cr of secured, on-demand borrowings; bank margin money/security deposits
    fell 86.4% even as bank guarantees nearly doubled** — quantifies the
    liquidity thinness behind Pass 1's FLAG-CASH mutual-fund drawdown
    finding. (Notes 10/10A, standalone p.86). 🟡 Watch, feeds FLAG-CASH.

11. **Growing non-equity exposure to Varos: trade/other debit balance +50.1%
    (₹0.41 Cr → ₹0.62 Cr), plus a residual ₹0.56 Lakh balance still owed by
    the divested Penta Auto Feeding JV 19 months after divestment.** (Note
    39D(i), standalone p.106). 🟡 Watch.

12. **New, previously trivial Chinese Yuan (CNH) unhedged exposure grew
    ~690x to ₹2.84 Cr net liability; EUR sensitivity rose 17.5x** — adds
    currency-composition detail and a new-in-kind exposure to Pass 1's FX
    red flag. (Note 34.3(c), standalone p.101). 🟡 Watch.

13. **Note 43 ratios not cited by Pass 1: ROCE collapsed to 1.20% from
    8.90% (-86.5%), ROE to -0.54% from 7.40%, Net Profit ratio to -0.55%
    from 7.18%, Current Ratio -7.2%; the DSCR's stated "reason" text
    ("lower net operating income") contradicts the ratio's own 39.2%
    improvement** — a further internally-contradictory disclosure. (Note
    43, standalone p.108). 🟡 Watch.

14. **Consolidated total comprehensive loss for FY26 was ₹12.16 Cr, more
    than double the ₹5.37 Cr net loss Pass 1 highlighted, once the ₹6.79 Cr
    parent-level OCI loss is included; consolidated net worth fell 4.5% to
    ₹441.48 Cr.** Also: Varos's ballooning loss-share percentage (-6.87% to
    54.32%) is driven mainly by the parent's own profit-to-loss swing
    shrinking the denominator, not primarily by Varos itself worsening much
    (+31.7% YoY) — a nuance on Pass 1's #2 finding. (Note 45 consolidated,
    p.167-168). 🟡 Watch, informational.

15. **Capital advances (Note 6) nearly tripled (+175.9%, ₹4.33 Cr → ₹11.96
    Cr)**, quantifying for the first time the capex-ramp leading indicator
    behind Pass 1's 22x capital-commitment red flag. (Note 6, standalone
    p.87). 🟡 Watch.

16. **Standalone auditor-remuneration mismatch, current year only:** Note
    29's P&L line (₹12.50 Lakh) does not match Note 31's itemised total
    (₹14.88 Lakh) for FY26; FY25 ties out exactly. (Notes 29/31, standalone
    p.96-97). 🟡 Watch, minor.

17. **Government Grant accounting policy (Note 1(m)/1(p)) conflates the
    "deferred income" and "capital approach" Ind AS 20 treatments in one
    sentence; only the capital (asset-netting) approach was actually
    applied.** 🟡 Watch, minor drafting item.

18. **Standalone Note 16 non-current provisions sub-lines ("Provision for
    employee benefits," "Other Employee Benefits") appear to match the
    CONSOLIDATED note's figures rather than genuine standalone-only
    numbers, while the standalone balance-sheet total ties only to the last
    ("Warranty") line** — a further, more granular instance of the
    stale-copy pattern Pass 1's top finding #10 already named. 🟡 Watch,
    presented as a refinement.
