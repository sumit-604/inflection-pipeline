# FTTCP SIGN-OFF GATES: KISSHT, 04-Oct-2026

Run runs/kissht-2026-09-19, branch run/kissht-2026-09-19. Input: operator rulings of
04-Oct-2026 (consolidated set A to J, recorded in companies/KISSHT.md). This file reports
gates I1 to I5 and the exact recompute that ruling J asked for. It is not the deliberation
file. /fttcp writes outputs/final/fttcp-deliberation.md only at sign-off.

Rs Cr unless stated. AR = Annual Report FY26 (PDF page). RHP = red herring prospectus,
25-Apr-2026 (printed page; PDF page = printed + 6). [INFERENCE] = my arithmetic on the
quoted inputs.

---

## 1. RECOMPUTE (ruling J), fully diluted, valuation date 31-Mar-2027

Share base (ruling C):
- Paid-up 16,84,83,022 (AR Note 48 p.131).
- Options outstanding in force 13,438,960 (RHP p.105).
- Pre-raise fully diluted 18.1922 Cr.
- Preferential 2,64,93,882 shares at Rs 314.11 (board outcome 17-Sep-2026 p.1) = Rs 832.20 Cr
  [INFERENCE].
- Post-raise fully diluted 20.8416 Cr.

CMP Rs 369.55 (Trendlyne LTP, 01-Oct-2026). Market value post-raise = 369.55 x 18.1922 +
832.20 = Rs 7,555.1 Cr, Rs 362.5 per share [INFERENCE].

Own book (Si Creva), Mar-27 book [INFERENCE]:
- FY26 book 1,231.98 (AR AOC-1 p.57; Note 47 p.131).
- Plus the IPO infusion of 636.8 (monitoring agency report 29-Jul-2026 p.5).
- Plus 75% of the raise, 624.15 (company release 18-Sep-2026 p.2).
- Plus 46% of FY27 PAT.
- Base: 2,695.8.

Partner half: 54% of FY28 PAT. Cash: 25% general-purpose slice of the raise, 208.05
(ruling G; release 18-Sep-2026 p.2).

| Case | Own book | Partner half | Cash | Total | Per share | vs post-raise value | Claude web (J) | Diff |
|---|---|---|---|---|---|---|---|---|
| Low (0.8x / 17.2x) | 2,156.6 | 5,786.4 | 208.05 | 8,151.1 | 391.1 | +7.9% | ~391 | 0.0% |
| Base (1.0x / 19.95x) | 2,695.8 | 6,711.6 | 208.05 | 9,615.4 | 461.4 | +27.3% | ~461 | 0.1% |
| High (1.2x / 22.7x) | 3,235.0 | 7,636.7 | 208.05 | 11,079.7 | 531.6 | +46.7% | ~531 | 0.1% |
| Bear PAT 400/500, base multiples | 2,676.9 | 5,386.5 | 208.05 | 8,271.5 | 396.9 | +9.5% | ~354 | **+12.1% FLAG** |
| Bear PAT 400/500, low multiples | 2,141.5 | 4,644.0 | 208.05 | 6,993.6 | 335.6 | -7.4% | ~354 | **-5.2% FLAG** |
| Bull PAT 470/700, base multiples | 2,709.1 | 7,541.1 | 208.05 | 10,458.3 | 501.8 | +38.4% | not given | |
| Top partner exits (partner PAT -1/3), base multiples | 2,695.8 | 4,474.4 | 208.05 | 7,378.2 | 354.0 | -2.3% | ~298 | **+18.8% FLAG** |
| Top partner exits, low multiples | 2,156.6 | 3,857.6 | 208.05 | 6,222.3 | 298.6 | -17.6% | ~298 | 0.2% |

Post-raise value today: Rs 362.5 vs Claude web ~Rs 364 (0.4%).

FLAG, stress labels. No definition of the bear case reproduces ~Rs 354. Rs 354.0 is exactly
the top-partner-exit case at base multiples. Claude web's ~Rs 298 is the partner exit at low
multiples. The two web stress numbers are likely the same stress at two multiple sets. The
bear row is then missing. The operator rules which multiple set each stress case carries.

Entry zone (Track 1, 25% a year): low case Rs 391.1 discounted over 0.487 years (04-Oct-2026
to 31-Mar-2027) = **Rs 350.8** [INFERENCE: 391.1 / 1.25^0.487]. Claude web ~Rs 350, a 0.2%
difference.

FLAG, Amendment 19 (CLAUDE.md NEVER list). No entry zone stands without the FV CAGR and the
return-source label. The 3-year FV path needs FY29 to FY31 PAT. The operator inputs stop at
FY28. One-year step for illustration only [INFERENCE]:
- Inputs: FY29 PAT about Rs 811 Cr (draft illustrative AUM path 15,660 to 19,600, 4.6% on
  average AUM), base multiples.
- FV at Mar-28 is Rs 572.3 against Rs 461.4 at Mar-27, a step of +24.0%.
- That step sits in the COMPOUNDER band. Stage 11 computes the governed 3-year FV CAGR and
  label. The entry zone above stays PROVISIONAL until it does.

FLAG, transfer-pricing sensitivity (ruling I1):
- Rs 10 Cr of PAT moved between the halves moves value by Rs 9.09 per share at base
  multiples [INFERENCE: 10 x (19.95 - 1.0) / 20.84].
- The ruled ~Rs 7.7 matches the low multiples (Rs 7.87) and differs by 15% at base.

---

## 2. SECTION 1B CHECKS ON THE PARTNER-HALF SLICE (ruling F)

- **Pillar 1 on parent RoE of about 34%: basis NOT FOUND.** The corpus gives two readings:
  - 16.7% on reported standalone equity [INFERENCE: PAT 1,441.24 mn / average net assets of
    9,640.57 and 7,643.59 mn, AR Note 47 p.131].
  - 84.4% on equity ex the investment in Si Creva [INFERENCE: average of (9,640.57 - 8,060.01)
    and (7,643.59 - 5,810.01) mn; AR Note 6 p.75].

  Track 2 hits the 22.7x slice cap at any RoE of 30.4% or more. So 34% and 84% give the same
  answer. At 16.7%, Pillar 1 is 15.85x and the slice falls below the ruled Track 1 figure.
  The operator names the basis for 34%.
- **Track 1 governance add-on: the rulings conflict.**
  - The slice's 17.2x implies r = 16.5% (governance +1.5) and RRM floored at 0.70.
  - Ruling H sets the whole-company governance add-on at +0.5. If the slice takes +0.5 too,
    then r = 15.5%, RRM = 0.76, and Track 1 = 24.5 x 0.76 = 18.6x [INFERENCE].
  - Effect on the low case at 18.6x: partner half +478 Cr, +Rs 22.9 per share. The entry
    zone moves with it. The operator rules one add-on for both.
- **Slice cap 22.7x: operator-set.** Section 1B has no blended-row mechanism. The 25x
  "asset-light services" figure matches the Master cap table rows "Logistics (asset-light)
  25x" and "Consulting / Engineering services 25x" in the Master sector cap table. It is
  recorded as an operator override. It is not a framework output.
- **FLDG charge vs partner revenue (the revisit trigger at ~40%).** The FY26 standalone charge
  is ECL on off-balance-sheet exposure 239.57 mn plus first loan default guarantee cost
  1,009.47 mn = 1,249.04 mn (AR p.84 to 85). That equals:
  - 23.4% of revenue from outside Si Creva [INFERENCE: 6,981.74 - 1,413.15 - 240.00 =
    5,328.59 mn, AR p.84, p.89].
  - 27.9% of outside sourcing and servicing fees.

  The ruled "about one third" is above both. The 40% trigger has more headroom than the
  ruling assumes.
- **FY26 per-AUM returns (ruling D).**
  - Si Creva: 4.9% [INFERENCE: PAT 148.24 / average on-book AUM 3,013; AR p.10 off-book
    shares 39% and 50%]. This matches the ruling.
  - Parent: 5.6% on the same rounded shares [INFERENCE: PAT 144.12 / average off-book AUM
    2,563.5], against the ruled 5.2%. The gap comes from rounded off-book shares on AR p.10.
    It does not change the 46/54 split.

---

## 3. WHOLE-COMPANY CROSS-CHECKS (ruling H, not primary)

- **P/E:**
  - FY28 EPS, fully diluted = Rs 29.89 [INFERENCE: 623 / 20.84].
  - Pillar 1 RoE of 17% gives 16.0x, and Rs 478 per share.
  - Track 1: r = 14 + 0.5 + 0.5 + 0.5 = 15.5%, RRM 0.76, 12.2x, Rs 363 per share.
- **P/B:**
  - Mar-27 net worth: Jun-26 net worth Rs 2,245.9 Cr (BVPS basic Rs 133.3 x 16.85 Cr, Q1
    FY27 deck BVPS table) + Q2 to Q4 FY27 PAT 345.9 + raise 832.20 = Rs 3,424.0 Cr.
  - Fully diluted BVPS Rs 164.3 [INFERENCE].
  - Market P/B on the post-raise value: 2.21x.
  - Theoretical P/B at RoE 17% is 1.10x to 1.42x (cost of equity 15.5% to 12%), so Rs 180
    to Rs 233 per share.
- **FLAG, method divergence.**
  - The base SOTP of Rs 461 is 2.81x Mar-27 book. The P/B cross-check sits 50% to 61% below
    it.
  - The premium comes entirely from the partner half at 19.95x on fee PAT that carries no
    equity in the split.
  - The ruling makes SOTP primary under Amendment 27.2. Master §1A names P/B primary for
    lenders. The divergence is printed here and goes to Stage 11 and Role 3.

---

## 4. GATE I1: TRANSFER PRICING

**Parent standalone FY26 cost base** (Rs mn; AR p.84 to 85 unless stated):

| Line | FY26 | FY25 |
|---|---|---|
| Employee benefits (incl. share-based payments 57.18) | 669.24 | 978.13 |
| Technology: server and communication cost | 27.84 | 24.04 |
| Depreciation and amortisation (incl. right-of-use 108.80) | 131.67 | 139.55 |
| Branding and marketing | 2,551.46 | 949.24 |
| Collections: outsourcing and back office | 557.48 | 133.42 |
| Business support service expenses | 28.08 | 3.10 |
| FLDG: ECL on off-balance-sheet exposure | 239.57 | 138.01 |
| FLDG: first loan default guarantee cost | 1,009.47 | 4.65 |
| Finance costs (lease) | 31.87 | 37.00 |
| Operating cost excluding the two FLDG lines [INFERENCE] | 4,173.14 | |

**Fees from Si Creva, FY26** (AR Note 34 p.89):

| Fee | Rs mn |
|---|---|
| Sourcing fees | 1,413.15 |
| Corporate guarantee fees | 394.06 |
| Other fees and charges | 240.00 |
| Interest on loan | 66.12 |

The standalone P&L carries corporate guarantee fees of 217.15 mn in other income (AR p.84).
The related-party figure is 394.06 mn. The gap is NOT EXPLAINED in the notes read.

**Basis of the fees.** The AR states the arrangement, not the formula.

> "Cost and Revenue Sharing Agreement ("Agreement") for as long as the services are availed
> by the Subsidiary Company" (AR AOC-2 p.58)

> "receipt of fees in accordance with the Agreement" (AR AOC-2 p.58)

> "Details of contracts or arrangements or transactions not at arm's length basis – Not
> Applicable" (AR AOC-2 p.58)

The rate, the cost key and the guarantee-fee rate are NOT DISCLOSED. Phase 1 B02 inferred
a guarantee fee of about 2.3% of the average guarantee (B02 rank 8; Note 34 pp.88 to 90).

**Does the fee match the cost of serving Si Creva?** [INFERENCE] Two readings.
- **Reading 1: allocate by AUM share.** The on-book share is 54.0% of average FY26 AUM
  [INFERENCE: 3,013 / 5,576]. That allocates Rs 225.3 Cr of the parent's Rs 417.3 Cr
  operating cost to Si Creva. Service fees received were Rs 165.3 Cr (sourcing 141.32 +
  other fees 24.00). The fees cover 73% of the allocated cost.
  - The shortfall is about Rs 60 Cr pre-tax, about Rs 45 Cr after tax.
  - On this reading Si Creva's profit is flattered and the parent's is understated.
  - Per-AUM returns would then be about 3.4% (own book) vs about 7.4% (partner half), not
    4.9% vs 5.6%.
  - At Rs 9.09 per Rs 10 Cr, Rs 45 Cr at FY26 scale is about Rs 41 per share. It is larger at
    FY28 scale.
- **Reading 2: allocate by the cost that originates each book.** Marketing (Rs 255.1 Cr, 61%
  of the cost) tracks disbursement, not AUM. Disbursement by book is NOT FOUND. On this
  reading the AUM key may overstate Si Creva's share.

The observation that separates them is disbursement by book (on vs off). It is not in the
corpus.

The 46/54 split itself runs on group PAT, so the fee does not enter it directly. The fee
matters because ruling D justifies the split with equal per-AUM returns after the fee. If
Reading 1 holds, that justification fails and the split moves toward the partner half,
which raises the SOTP.

---

## 5. GATE I2: STRESS CASES

Reported in section 1: bear, bull and top partner exit, each at two multiple sets. The
labels need a ruling (FLAG above).

---

## 6. GATE I3: ESOPs

- **FY26 share-based payment expense:**
  - Consolidated Rs 29.34 Cr, inside employee benefit expenses (AR p.119, consolidated
    note; Note 43 referenced). FY25: Rs 37.72 Cr.
  - Booked as Rs 5.72 Cr in the parent (standalone employee benefits, AR p.84) plus
    Rs 23.62 Cr granted to Si Creva employees (AR Note 34 p.89). These sum to the
    consolidated figure [INFERENCE].
- **Holders by category** (RHP p.101):
  - Promoters and directors Ranvir Singh and Krishnan Vishwanathan: options outstanding
    "Nil".
  - Senior management: Neha Shivran 161,800; Sandeep Kadam 60,000.
  - Grants to current KMP under all three schemes: "Nil" (RHP p.106, p.109, p.112).
  - Former CFO Amit Gupta: 35,400 under ESOP-2021 (RHP p.113).
  - The 59,708 shown against each promoter on RHP p.103 are preference shares, not options.
- **Unvested options:**
  - In force 13,438,960. Vested including exercised 10,714,550. Exercised 123,670 (RHP
    p.105).
  - Unvested = 2,848,080 [INFERENCE]. This matches the ruled 2.84M.
  - Tranche-level vesting schedule: NOT FOUND. The grant valuation tables show expected
    lives of 1 to 4 years (RHP p.107 to 114).
  - Latest grant: 25-Nov-2025 at an exercise price of Rs 1 (RHP p.114).
- **Exercise price.** Options carry Rs 1 post split (Rs 10 pre split). One ESOP-2019 lot of
  28,985 options shows "₹509" (RHP p.106), which is likely the pre-split price. It is 0.2%
  of options in force. The fully diluted count treats it as dilutive.
- **Exercises or grants after the RHP:** NOT FOUND in the corpus.

---

## 7. GATE I4: Q2 FY27 BUSINESS UPDATE (03-Oct-2026)

OPEN. The BSE announcements API returned "Access Denied" on 04-Oct-2026 (one attempt, one
header retry). The filing is not in the corpus.

A cloud search excerpt (Free Press Journal, 03-Oct-2026; not corpus, not anchored) reports:
- AUM Rs 9,317 Cr, +68.4% YoY.
- Disbursements Rs 4,612 Cr.

The operator drops the PDF into runs/kissht-2026-09-19/inputs/announcements/ or gives the
AttachLive URL.

---

## 8. GATE I5: SECTION 1B v3.11

OPEN. Amendment 27 is not on main. The draft sits uncommitted in the main checkout, which
holds another session's work. This session does not touch it. **Stage 11 rests on an
unmerged framework** until the operator merges v3.11 through its own framework branch and PR.

---

## 9. OTHER POINTS FOR THE OPERATOR

- **Band wording.** FTTCP v2.3 maps a composite of 1 to 2 to "DEEP WATCH leaning AVOID" and
  3 to "DEEP WATCH" (FTTCP Step 4 table). The ruled composite is +2 and the ruled band is
  "DEEP WATCH". Both are recorded; the operator's words govern the verdict line.
- **T3 trigger baselines.** The Q2 FY26 Stage 2 (4.11%) and GNPA (2.92%) baselines are
  operator-supplied. The corpus does not carry Q2 FY26 asset-quality figures.
- **Cross-family grade:** did not run (exit 3, no Gemini or Google key).
