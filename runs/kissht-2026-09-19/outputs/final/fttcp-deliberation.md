# FTTCP DELIBERATION: OnEMI Technology Solutions Ltd (Kissht)

Ticker KISSHT (NSE), 544754 (BSE). Signed off 04-Oct-2026 by the operator, Keerti Kaushik.
Run folder runs/kissht-2026-09-19. Protocol FTTCP v2.3, lender transition set, one entity.
Exit multiple authority: Section 1B v3.3 to v3.11 (v3.11 unmerged; see OPEN ITEMS).

Inputs to this file:
- outputs/final/fttcp-draft.md (autonomous draft, commit 8a3421ee)
- outputs/final/fttcp-signoff-gates-2026-10-04.md (gate results, commit 074995f8)
- the operator rulings of 03-Oct and 04-Oct-2026, logged in companies/KISSHT.md

Rs Cr unless stated. [INFERENCE] marks arithmetic on quoted inputs.

Sign-off taken with two open items (I4, I5) under the operator's ruling of 04-Oct-2026:
"Sign off once both land, or sign off now with both recorded as open items, at your
discretion under the command." Claude Code signed off now. The Q2 update changes no
pillar input. The v3.11 merge already gates Stage 11 sign-off (ruling I5).

---

## 1. THE VERDICT, IN THE OPERATOR'S WORDS

"Composite +2. Band DEEP WATCH. Posture VALUE-TRAP RISK." (ruling B, 04-Oct-2026), with the
band wording set by the sign-off ruling of 04-Oct-2026: "use the FTTCP table: +2 = 'DEEP
WATCH leaning AVOID'."

Final: **Composite +2 of 8. DEEP WATCH leaning AVOID. Posture VALUE-TRAP RISK.**

---

## 2. FINAL RULINGS (draft rulings 1 to 18, after review)

| # | Call | Final | Changed? |
|---|---|---|---|
| 1 | Forward window | 3m primary, 6m secondary, 12m RoA/RoE | no |
| 2 | Business type | Lender transition set | no |
| 3 | Workup intent | First workup | no |
| 4 | Sector cap row | Banks / NBFCs / MFIs 18x for the whole company and the own-book slice; partner slice on an operator-set blended cap (ruling F) | yes, partner slice |
| 5 | Entity count | One entity; SOTP slices own book and partner half (Amendment 27.2) | no |
| 6 | Framework version | v3.11 applied, unmerged; OPEN ITEM I5 | no |
| 7 | Cash conversion | GROWTH INDUCED | no |
| 8 | RoA/RoE backward | SUSTAINED | no |
| 9 | T1 AUM growth | FIRING +2 | no |
| 10 | T2 NIM / spread | DECLINING -1 | no (reasoning added) |
| 11 | T3 asset quality | **STARTING +1** | yes, override 1 |
| 12 | T4 RoA / RoE | STAGNANT 0 | no |
| 13 | Proof gate | NOT FIRED | no |
| 14 | Composite and band | **+2, DEEP WATCH leaning AVOID**; Kernex cap and TRIM rule not engaged | yes, follows override 1 |
| 15 | Pillar 2L | 1.00x Sound | no |
| 16 | Pillar 1 | Per slice, and whole company on post-raise RoE ~17% | yes, override 2 |
| 17 | Hurdle tier | A, 25% | no |
| 18 | Undiscovered Alpha | Not qualified | no |

Posture: proof gate NOT FIRED plus ugliness STRUCTURAL-FEATURE gives VALUE-TRAP RISK.

---

## 3. OPERATOR OVERRIDES

**Override 1. T3 asset quality.**
- Draft: STAGNANT (0), genuinely uncertain. Reason: Q1 FY27 Stage 2 rose 2.4% to 3.15%.
- Ruling: STARTING (+1).
- Operator's reasoning: "Compare Q1 FY27 with Q1 FY26 YoY (GNPA +13 bps vs +75 bps;
  seasonal)."
- New trigger: "Reset trigger to Q2 FY27 vs Q2 FY26: STARTING if Stage 2 <=3.3% and GNPA
  <2.92%; DECLINING if Stage 2 >4.11% or GNPA >2.92%."
- Default-track sensitivity: at the draft's STAGNANT the composite is +1, the same band.
- Note: the corpus does not carry the Q2 FY26 baselines (4.11%, 2.92%). They are
  operator-supplied.

**Override 2. Valuation method and Pillar 1.**
- Draft: a whole-company card on Pillar 1 ROE 21.2%. Track 2 18.0x, Track 1 12.7x.
- Ruling: SOTP primary on a FORWARD basis, valued at 31-Mar-2027 (rulings D to H).
- Operator's reasoning on the RoE:
  - "Q1 21.2% is an average-equity artifact; 16.9% on 30-Jun equity" (ruling H).
  - For the partner slice: "measure on parent capital EXCLUDING the investment in Si Creva
    ... The 16.7% double-counts Si Creva equity valued in the own-book slice. Cap binds
    either way."

**Override 3. Partner-slice sector cap.**
- Draft: Banks / NBFC 18x.
- Ruling: "Slice cap (operator-set) = 1/3 x 18x (NBFC row) + 2/3 x 25x (asset-light
  services row) = 22.7x."
- Reason: "Not a pure lender: credit loss capped at 5% DLG per pool."
- Section 1B has no blended-row mechanism. This is an operator ruling, not a framework
  output.
- Revisit "if the FLDG charge exceeds ~40% of partner revenue, or the top-two partner share
  stays above 90% through FY27."
- FY26 charge: 23.4% of revenue from outside Si Creva (gate file section 2).

**Override 4. Governance add-on.**
- Draft: +1.5. Ruling: "+0.5 everywhere (integrity priced in sizing and hurdle)."
- Effect: r = 15.5%, RRM 0.76.

**Override 5. Entry zone.**
- Mechanical Track 1 entry at the ruled multiples is Rs 371.4 [INFERENCE: low case Rs 414.0
  / 1.25^0.487].
- Ruling: "ENTRY ZONE: hold at ~Rs 350 by operator override."
- Operator's reasoning: "book-value cross-check: base implies 2.81x Mar-27 book, needing
  ~13% perpetual growth at 17% RoE."
- Revisit "when disbursement-by-book and the Amendment 19 three-year FV CAGR are available."
- At the ruled multiples the base is 2.88x Mar-27 book. The implied perpetual growth is
  12.4% at a 14% cost of equity and 14.7% at 15.5% [INFERENCE: P/B = (ROE - g) / (CoE - g)].

**Override 6. Share count.**
- Draft: 16.85 Cr paid-up.
- Ruling: fully diluted, 18.19 Cr before the raise and 20.84 Cr after (options in force
  13,438,960, RHP printed p.105).

---

## 4. CROSS-FAMILY GRADE

Cross-family check did not run. verifiers/fttcp_crossgrade.py exited 3 on 03-Oct-2026
because no Gemini or Google key is configured. No grader divergence existed to resolve.

---

## 5. OPERATOR-APPROVED VALUATION PILLARS (authoritative for Phase 3)

Stage 11 MUST use this base and basis. It may not silently derive a different exit PE.

**Earnings basis: FORWARD.**
- Valuation date 31-Mar-2027. Own book on Mar-27 book; partner half on FY28 PAT.
- Operator's reason: "Valuation date 31-Mar-2027. Own book on Mar-27 book; partner half on
  FY28 PAT. Same basis at exit (Amendment 27.3)."

**Method:** SOTP primary (Amendment 27.2). Whole-company P/E and P/B are cross-checks only.

**Earnings and share base:**
- PAT FY27 / FY28: base 441 / 623 (return on average AUM 4.75% / 4.6%; AUM 11,600 /
  15,660); bear 400 / 500; bull 470 / 700.
- Split 46 / 54 (own / partner) by AUM share.
- Shares fully diluted: 20.8416 Cr after the raise.
- Market value after the raise = CMP x 18.1922 Cr + Rs 832.20 Cr.

**Slice 1: own book (Si Creva), P/B**

| Input | Approved |
|---|---|
| Book | Mar-27 book 2,695.8 [INFERENCE: FY26 1,231.98 (AR p.57) + IPO 636.8 + 75% of raise 624.15 + 46% of FY27 PAT] |
| P/B low / base / high | 0.8x / 1.0x / 1.2x |
| Reason (operator) | "RoE ~10% post-raise, recovering toward FY26's 14% as capital is lent out." |

**Slice 2: partner half (parent fee business), P/E on FY28 PAT**

| Input | Approved |
|---|---|
| Pillar 1 | Parent RoE ex the investment in Si Creva: 84.4% FY26 actual, ~34% FY27 projected → 24.5x on the operator's figure. v3.5.1 route: none |
| Pillar 2L | 1.00x Sound |
| Pillar 3 | +0x (EM 18.5; no pricing power, no moat premium) |
| Strategic premium | +0x |
| Undiscovered Alpha | Not qualified |
| Sector cap | 22.67x, operator-set blend (override 3) |
| Track 2 destination | 22.67x (cap binds) |
| Track 1 destination | 24.5 x RRM 0.76 (r 15.5% = 14 + 0.5 durability + 0.5 governance + 0.5 complexity) = **18.62x** |
| Track divergence | Track 1 is 17.9% below Track 2 (above 15%): Track 1 sets the entry zone |
| SOTP P/E low / base / high | 18.62x / 20.64x (midpoint) / 22.67x |

**Cash:** Rs 208.05 Cr general-purpose slice of the raise, at face value, held constant on
the FV path (Amendment 27.1). FLDG deposits are excluded as locked collateral.

**Whole-company cross-checks (not primary):**
- Pillar 1 RoE ~17% → 16.0x Track 2.
- Track 1 at r 15.5%, RRM 0.76 → 12.2x.
- P/B on Mar-27 fully diluted BVPS Rs 164.3 [INFERENCE: Jun-26 net worth 2,245.9 (Q1 FY27
  deck BVPS Rs 133.3 x 16.85 Cr) + Q2 to Q4 FY27 PAT 345.9 + raise 832.20, over 20.84 Cr].

**Hurdle:** Tier A, 25%. **Sizing:** Small ceiling (Part 2.6); Small starter (Amendment 25).

**Values at the approved multiples** (31-Mar-2027, fully diluted; CMP Rs 369.55, Trendlyne
01-Oct-2026; post-raise value Rs 7,555.1 Cr = Rs 362.5 per share) [INFERENCE]:

| Case | Total | Per share | vs post-raise value |
|---|---|---|---|
| Low (0.8x / 18.62x) | 8,628.8 | 414.0 | +14.2% |
| Base (1.0x / 20.64x) | 9,848.7 | 472.5 | +30.4% |
| High (1.2x / 22.67x) | 11,068.5 | 531.1 | +46.5% |
| Bear 400/500, low multiples (HEADLINE) | 7,377.0 | **354.0** | -2.4% |
| Bear, base multiples | 8,458.7 | 405.9 | +12.0% |
| Partner exit (partner PAT -1/3), low multiples (HEADLINE) | 6,540.8 | **313.8** | -13.4% |
| Partner exit, base multiples | 7,533.7 | 361.5 | -0.3% |
| Bull 470/700, base multiples | 10,720.4 | 514.4 | +41.9% |

**Entry zone: ~Rs 350, by operator override (override 5).** It is PROVISIONAL.

Amendment 19 FV CAGR and return-source label: NOT YET COMPUTED, because operator inputs
stop at FY28. Stage 11 computes them. CLAUDE.md bars presenting the entry zone downstream
without them.

**Alignment notes against the sign-off rulings of 04-Oct-2026:**
- Ruling 1 quoted the headline stresses as "bear Rs 335.6; partner exit Rs 298.6". Those
  were computed at the old 17.2x low multiple. At the ruled 18.62x the low-multiple
  headlines are **Rs 354.0** and **Rs 313.8**. This file uses the ruled multiples.
- Ruling 5 set the sensitivity at Rs 9.1 per Rs 10 Cr. At the ruled base multiple of
  20.64x it is **Rs 9.4** [INFERENCE: 10 x (20.64 - 1.0) / 20.84]. This file uses Rs 9.4.

---

## 6. TRANSFER PRICING, ESOPs, IR QUESTIONS

- **Transfer pricing (ruling 6):** "fees cover ~73% of the parent's cost of serving Si Creva
  on an AUM split (Si Creva flattered ~Rs 45 Cr after tax); the 46/54 equal-return split is
  therefore conservative for the partner half." Fee rates are NOT DISCLOSED (AR AOC-2 p.58).
- **ESOPs (ruling 7):** "ordinary employee compensation (promoters/KMP hold none; Rs 29.34 Cr
  FY26 cost already in PAT). No change to the Entrepreneur Ledger."
- **IR question list, additions of 04-Oct-2026:**
  1. Disbursement by book, on-book (Si Creva) vs off-book (partner), FY25, FY26 and Q1 FY27.
  2. The guarantee fee gap: Rs 39.41 Cr in the related-party note (AR Note 34 p.89) vs
     Rs 21.72 Cr in standalone other income (AR p.84).

---

## 7. WATCH LIST CHANGES vs THE DRAFT

- **Added, T1:** average ticket and loans per borrower in the Q2 FY27 deck (new-customer
  adds slowing while disbursements grow).
- **Replaced, triggers 1 and 2 (T3):** the operator's Q2 FY27 vs Q2 FY26 trigger in
  override 1.
- **T2 note:** "~half of the 5.2-pt income fall is mix (partner share rising, LAP rising),
  not price; return on AUM held ~5%." Finance cost to AUM fell mainly because equity
  replaced debt. Expect it to rise as debt is rebuilt.
- **Added, partner-slice cap revisit:** the FLDG charge above ~40% of partner revenue, or
  top-two partner share above 90% through FY27.

---

## 8. OPEN ITEMS

| # | Item | Owner | Blocks |
|---|---|---|---|
| I4 | Q2 FY27 business update (03-Oct-2026) not in the corpus; BSE API returned Access Denied on 04-Oct-2026 | operator drops the PDF into inputs/announcements/ | none at sign-off; T1 watch item reads it |
| I5 | Section 1B v3.11 (Amendment 27) not merged to main | operator, separate framework PR | Stage 11 sign-off (ruling I5) |
| A19 | Amendment 19 three-year FV CAGR and return-source label | Stage 11 | the entry zone's presentation downstream |
| DBB | Disbursement by book (IR question 1) | IR reply | the entry-zone override revisit and the transfer-pricing reading |
