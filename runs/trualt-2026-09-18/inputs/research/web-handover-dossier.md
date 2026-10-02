# WEB HANDOVER DOSSIER — TRUALT (TruAlt Bioenergy Ltd, NSE: TRUALT, BSE: 544545)
## claude.ai live-verification layer, Halt 1 close-out

**Run:** `runs/trualt-2026-09-18/` | **Branch:** `run/trualt-2026-09-18`
**Produced:** 02-Oct-2026 in the claude.ai project (Dhruva Research), from the Halt 1 stress-test and six-vertical deep dive (V1 to V6).
**Corpus extractions consumed:** part1 to part7 on `run/trualt-2026-09-18`; part4 057cfca8 (feedstock formula, margin per litre, DDGS, units), part5 504bb92e (approvals, Unit 4, stock-in-trade, capex), part6 099e94d1 (term loans, covenants, DSCR, subvention, inventories, NSL payable, WC limits, SAF, NABARD guarantee), part7 df2c23d4 (CBG subsidiaries, Leafiniti gap, TGPL share trail, GAIL veto rights).
**Live documents read here:** CRISIL rating rationale 13-Aug-2026; Q1 FY27 Reg 33 results with restated FY26; Q1 FY27 and Feb-2026 call transcripts; screener.ai summaries of filings 01-Aug to 02-Oct-2026 (Unit 5 slump sale, GST demand); NHPL Form C 30-Sep-2026; Kamala Nirani Reg 31 / Form C 28-Sep-2026.

**Precedence rule.** Where this dossier conflicts with a corpus document, the corpus document wins UNLESS this dossier marks an explicit supersession with its evidence (Section 3). Evidence tiers: [FILED] filed document; [AGENCY] rating agency or regulator; [MGMT] management verbal; [COUNTERPARTY] a customer's or partner's own disclosure; [SECONDARY] news, forum, aggregator; [INFERENCE] analyst arithmetic or deduction, always labelled.

---

## 0. INSTRUCTIONS FOR CLAUDE CODE

1. Commit this file to `runs/trualt-2026-09-18/inputs/research/web-handover-dossier.md` on branch `run/trualt-2026-09-18`.
2. Update `companies/TRUALT.md` with the block in Section 12. Replace the THESIS, DECISION STATUS, HALT 1 GATE, OPERATOR RULINGS, ACTIVE TRIPWIRES and OPTIONALITY REGISTER sections. Keep SPEAR and RUN FOLDERS. The block carries the tracker proof line the Role 5.5 tracker gate needs.
3. **Halt 1 ruling is PROCEED.** After steps 1 and 2 are committed, run `/fttcp runs/trualt-2026-09-18`. The understanding gate, tracker gate and handover input gate should all pass from this commit.
4. At the Stage 11 P/E gate, STOP and present the inputs in Section 5.3 for operator rulings. Do not pick the sector cap, earnings basis or CBG treatment yourself.
5. Append the close-out table in Section 11 to `LESSONS_ARCHIVE.md`. Add one OPEN ACTIONS line per open row to `LESSONS.md`.
6. Open the PR for `run/trualt-2026-09-18` the same day (session-branch discipline). Run outputs only; no framework edits on this branch.
7. Unanswered extraction (not a blocker): **QX1.** NSL sugar-syrup MSA: quote the pricing clause from the MSA itself (if in corpus) and the two prospectus passages that conflict (FRP-linked vs market-linked), with page anchors. If the MSA is not in corpus, say NOT DISCLOSED and where it would be filed.

---

## 1. HALT 1 RULING AND MENTAL MODEL (SIGNED, operator, 02-Oct-2026)

**Operator rulings, 02-Oct-2026:**
- Mental model: SIGNED.
- Promoter verdict: **CONCERN (integrity).** Size ceiling **Small (2-3%)**. The Entrepreneur Ledger does not offset integrity items (Part 2.6).
- AVOID triggers (operator-named): (1) Accutrade balance Rs 40 Cr or more at H1 FY27 with no supplies shown; (2) TGPL rights price well below Rs 30.90; (3) NHPL dues still unpaid at 30-Sep-2026.
- Halt 1 decision: **PROCEED to `/fttcp`.** Operator override of Claude's SHALLOW WATCH recommendation.
- Decision Status in Notion: unchanged, WATCHLIST (operator-only field).

**Archetype: A RATIONED COMMODITY CONVERTER, inside a family group, trying to become a two-fuel bioenergy platform.**

| Line | Engine | Current rung → claimed destination |
|---|---|---|
| Ethanol (core) | Allocated litres × margin per litre. Price set by government; volume set by OMC allocation | R1 → R2 (cost-advantaged converter) if dual-feed holds year-round |
| CBG (51% subsidiaries; GAIL and Sumitomo partners) | Commissioned plants × fixed offtake price | R0 → R3 (policy-priced annuity) once plants run. **Pre-revenue capacity = CONVERTER slice** (Amendment 17) until commissioned |
| SAF | Claimed future option | Claimed R4. **Valued at zero:** no FID, no funding, Ind-Ra excludes it, CRISIL does not mention it |

**The analogy.** A bakery where the government is the only bread buyer. The government sets the price of bread and tells each bakery how many loaves it may sell. The baker's only levers are flour cost and keeping the ovens busy.

**Transition 1, Ethanol feed.**
- FROM: sugar-seasonal plants (sugar-only capacity 600 KLPD) [FILED, part5].
- TO: dual-feed, year-round running on maize and rice as well as cane syrup.
- Engine: fuller plants at a held margin near Rs 11-12/L.
- PROOF GATE: Q3 and Q4 FY27 each at 9 cr L or more, at EBITDA of Rs 10/L or more.
- Ugliness: ARTIFACT-OF-CLIMB (inventory build, grain-cost swing).
- Falsifier: ESY27 award below 25 cr L together with a sugar-route ban and an FCI rice cut.

**Transition 2, CBG.**
- FROM: pre-revenue build-out; Leafiniti did not break even [AGENCY, Ind-Ra].
- TO: commissioned, fixed-price annuity with GAIL and Sumitomo offtake.
- PROOF GATE: three Sumitomo plants commissioned and about Rs 15 Cr a quarter by Q2 FY28.
- Ugliness: ARTIFACT-OF-CLIMB (capex ahead of revenue).
- Falsifier: commissioning slips past FY28, or debt-funded CBG capex triggers a CRISIL downgrade.

**Transition 3, Governance.**
- FROM: family company with money at family entities (Rs 55.4 Cr).
- TO: listed company with arm's-length dealings.
- PROOF GATE: family-entity balances at zero by Mar-2027.
- Ugliness: STRUCTURAL until proven otherwise.
- Falsifier: Mar-2027 balance sheet still carries the Accutrade and NHPL balances.

**Emerging advantages:** (1) CBG fixed-price offtake with GAIL and Sumitomo. (2) Waste-to-fuel loop: spent wash feeds CBG and narrows its feedstock gap [INFERENCE]. (3) By-products (DDGS, CO2) cushion the grain margin. (4) Grain-buying skill in North Karnataka. (5) SAF: not forming.

**Dominant variables (the model watches four).**
1. Litres sold. FY27 base about 34 cr L [INFERENCE on AGENCY allocation 14 + 8 + 15 cr L and MGMT Q2 11 cr L orders in hand].
2. EBITDA per litre. Base about Rs 11-12/L [INFERENCE on FILED Q1 FY27 EBITDA Rs 132.76 Cr].
3. Net debt / EBITDA. 5.7x now; about 3.7x by Mar-2027 if inventory converts [INFERENCE].
4. Money at family entities. Rs 55.4 Cr (Accutrade Rs 40.31 Cr + NHPL Rs 15.08 Cr) [FILED].

**Rejected as noise:** SAF headlines; SC SLP 22411/2026 (TruAlt not a party; the Q4 top-up went to all bidders; operator judged it low importance); quarter-to-quarter grain price swings inside the Rs 10-12/L band.

**Model falsifiers:** (1) ESY27 award of 40 cr L or more with relaxed zoning (falsifies the rationing frame on the upside). (2) Mar-2027 balance sheet clean of family balances (falsifies the governance overhang). (3) Sugar-route ban + FCI rice cut + award below 25 cr L (business falsifier).

**Recognition gap: CLOSED.** At Rs 444 (01-Oct-2026 close, Screener [SECONDARY]; refresh from the exchange before any use), mcap about Rs 3,810 Cr, the stock trades at about 25x FY27 EPS of Rs 17-18 [INFERENCE] against an indicative 11-13x. The market already prices the dual-feed transition.

**Posture (Transition Decision Matrix):** proof gate NOT FIRED; ugliness mostly artifact-of-climb, governance structural; recognition gap CLOSED → Claude recommended SHALLOW WATCH; **operator ruled PROCEED.**

---

## 2. VERTICAL FINDINGS (verdicts with tiers)

**V1: Volumes and allocation. Verdict: FY27 base about 34 cr L.**
- CRISIL allocation read 14 + 8 + 15 cr L [AGENCY, 13-Aug-2026].
- Q2 FY27: 11 cr L "orders in hand" [MGMT].
- TruAlt is not a party to SC SLP 22411/2026. The Q4 top-up went to all bidders [SECONDARY].
- Base moved 31 → 33 → 34 cr L during the cycle (C24-C28).
- [INFERENCE] 34 cr L over about 330 operating days is about 1,030 KLPD, or about 56% of the 1,800-1,900 KLPD operating capacity. Q1 FY27 filed utilisation was 60.57% [FILED]. Allocation, not capacity, binds.
- Open: ESY27 award size and zoning; sugar-route order.

**V2: Feedstock and margin. Verdict: base EBITDA about Rs 11-12/L; rice no longer better than maize.**
- The Rs 15-16/L margin quoted by management was on maize, not rice [MGMT].
- DDGS yield 18% on maize, 22% on rice [FILED, part4].
- Sugar-supply MSA with NSL is FRP-linked [FILED].
- Prospectus conflicts on syrup pricing: FRP-linked in one passage, market-linked in another [FILED]. Unresolved (QX1).
- Open: which syrup clause governs; FCI rice price and quantity for ESY27.

**V3: Plant and trading. Verdict: operating capacity 1,800-1,900 KLPD; sugar-only capacity 600 KLPD.**
- Unit 4 is a conversion, not new capacity [FILED, part5]. The deck's "dual-feed 300 KLPD" exceeded the installed 200 KLPD [FILED, Q1 review].
- Q3 traded goods were probably diesel sold to NSL, matching the Rs 101.95 Cr related-party line [FILED + INFERENCE].
- Unit 5 slump sale disclosed in the Aug-Oct 2026 filings [SECONDARY, screener.ai summary of exchange filings; primary filing not pulled].
- Open: nature of stock-in-trade going forward; NSL dealings.

**V4: Debt and liquidity. Verdict: stretched but serviceable if inventory converts. CRISIL A-/Negative.**
- Facilities [AGENCY, CRISIL 13-Aug-2026]: SBI CC Rs 300 Cr; IREDA TL Rs 1,113 Cr; SBI TL Rs 204 Cr. Repayments Rs 180-260 Cr a year; expected accrual Rs 270-360 Cr.
- Rating history [AGENCY]: A-/Stable 28-Oct-2025 → A-/Negative from 30-Apr-2026. Downgrade triggers: operating margin below 12%, or large debt-funded capex.
- FY26 restated [FILED, Q1 FY27 results p.4]: revenue Rs 1,727.51 Cr; other income Rs 86.45 Cr; finance cost Rs 160.02 Cr; D&A Rs 86.23 Cr; PBT Rs 140.50 Cr; PAT Rs 104.76 Cr. Q1 FY27: finance Rs 44.03 Cr; PBT Rs 78.45 Cr; EBITDA Rs 132.76 Cr.
- FY26 cash accrual Rs 196-224 Cr, not Rs 130 Cr [INFERENCE on FILED].
- DSCR 0.99 against the AR's claim of full covenant compliance [FILED, part6].
- Reliable interest subvention about Rs 50 Cr; the TL1 subvention window ends about Mar-2028 [FILED, part6].
- WC limits Rs 600 Cr [FILED]. NABARD guarantee not disclosed in the AR [FILED, part6].
- Open: lender DSRA / bank-guarantee decision; H1 FY27 inventory and cash flow.

**V5: CBG and SAF. Verdict: CBG real but early; SAF valued at zero.**
- Leafiniti did not break even. Ind-Ra shows 9M EBITDA of Rs 19.4 Cr [AGENCY].
- The Rs 18 Cr gap is about Leafiniti's turnover less the CBG segment revenue; probably a relabelled part of Leafiniti's own turnover [INFERENCE on FILED, part7].
- GAIL entered cheaply, at about 2x FY25 earnings, with veto rights [FILED, part7].
- CBG capex Rs 950-1,000 Cr, of which Rs 650-700 Cr debt [AGENCY]. SAF not mentioned by CRISIL.
- SAF: no FID, no funding, Ind-Ra excludes it [AGENCY + FILED].
- TGPL share trail: rights issue to NHPL, then flip to Sumitomo at Rs 30.90; rights price not yet established [FILED, part7].
- Q1 FY27 deck-vs-filing contradiction on CBG segment PBT (reviewed +209% vs deck −10.51%) [FILED].
- Open: commissioning dates; Leafiniti AOC-4; TGPL PAS-3.

**V6: Promoter and governance. Verdict: CONCERN (integrity). Size ceiling Small.**
- I1 Rs 40.31 Cr advance to Accutrade Global LLP (the MD's LLP), no stated purpose [FILED + SECONDARY MCA].
- I2 Investor decks ahead of, or at odds with, filings [FILED].
- I3 AR gaps: FY26 restatement, NABARD guarantee, DSCR 0.99 vs "full compliance" [FILED].
- I4 TGPL rights issue to NHPL, then flip to Sumitomo at Rs 30.90 [FILED]; rights price pending.
- I5 Acuite classed TruAlt non-cooperative from 09-Jun-2025 [AGENCY].
- I6 Regulatory fines; GST demand disclosed Aug-Oct 2026 [SECONDARY, screener.ai summary of exchange filings].
- I7 Rs 15.08 Cr NHPL receivable for NHPL's own share-sale costs, unpaid over one year [FILED].
- Criminal cases are against the MD personally; the AR's silence is an omission, not a misstatement [FILED + SECONDARY].
- MRN Bhima: no FY26 transactions; the issue is the missing FY25 comparative [FILED].
- Promoter-group buying is pledge-funded: Kamala Nirani's 42,27,590 shares (4.93%) fully encumbered to Jio Credit (25-Sep-2026) to finance promoters' purchases [FILED]; NHPL pledged 14,00,000 shares (22-Sep) [SECONDARY]; NHPL bought 1,96,129 more shares on 30-Sep, to 2.48% [FILED]. Trading window closed from 01-Oct-2026.

**Entrepreneur Ledger (read with the verdict; cannot offset integrity items):**

| Head | Evidence | Credited |
|---|---|---|
| (a) Built from what base | Multi-unit ethanol platform at 1,800-1,900 KLPD operating capacity, converted to dual-feed; CBG subsidiaries with GAIL and Sumitomo [FILED] | YES |
| (b) Capital raised vs what it became | IPO at Rs 496; use-of-proceeds vs deployment not traced this cycle | NOT EVIDENCED (gap) |
| (c) Against-the-sector bets | Early move to grain feed [INFERENCE] | PARTIAL |
| (d) Skin in the game | Buying since Aug-2026, but funded by pledges; money flowing to family entities | NOT CREDITED |

---

## 3. EXPLICIT SUPERSESSIONS (corpus-derived views this dossier overrides)

- **S1. "Rs 15-16/L grain margin" (MGMT, read as rice).** SUPERSEDED: the figure was on maize. Rice is no better than maize once DDGS yields (18% vs 22%) and FCI pricing are applied.
- **S2. "Unit 4 adds dual-feed capacity of 300 KLPD."** SUPERSEDED: Unit 4 is a conversion; installed 200 KLPD. Operating capacity 1,800-1,900 KLPD; sugar-only 600 KLPD.
- **S3. FY26 cash accrual about Rs 130 Cr (earlier claude.ai draft).** SUPERSEDED: Rs 196-224 Cr from the restated FY26 lines [INFERENCE on FILED].
- **S4. "Full covenant compliance" (AR).** SUPERSEDED: DSCR 0.99 [FILED, part6].
- **S5. CBG at or near break-even (deck).** SUPERSEDED: Leafiniti did not break even; Ind-Ra 9M EBITDA Rs 19.4 Cr [AGENCY]. The Rs 18 Cr gap is probably relabelled turnover [INFERENCE].
- **S6. SAF as a near-term value line.** SUPERSEDED: no FID, no funding, Ind-Ra excludes it. Valued at zero.
- **S7. "Criminal cases undisclosed = misstatement" (earlier draft).** SUPERSEDED: the cases are against the MD personally; the AR's silence is an omission.
- **S8. MRN Bhima as an FY26 related party issue.** SUPERSEDED: no FY26 transactions; the issue is the missing FY25 comparative.
- **S9. Sugar-supply pricing read as market-linked.** SUPERSEDED for now: the MSA is FRP-linked [FILED]; the prospectus conflict is open (QX1).
- **S10. Q3 traded goods read as ethanol trading.** SUPERSEDED: probably diesel sold to NSL [FILED + INFERENCE].

---

## 4. PROMISE-VS-DELIVERY LEDGER

| Promise | Outcome | Grade |
|---|---|---|
| Rs 15-16/L margin from grain | Held on maize, not rice | PARTIAL |
| CBG at break-even | Leafiniti did not break even | MISS |
| Unit 4 dual-feed 300 KLPD | Conversion; installed 200 KLPD | MISS |
| SAF project | No FID, no funding | PENDING |
| Full covenant compliance (AR) | DSCR 0.99 | MISS |
| Q2 FY27 volumes | 11 cr L orders in hand | PENDING |
| CBG segment profit (Q1 deck) | Contradicts reviewed filing | MISS |

**Credibility split (binding for deliberation):** plant building and conversion are DELIVERED. Margin, CBG and covenant claims are MISSED or overstated. Discount management guidance by trailing-four-quarter delivery (Rule B, Rule E: Mixed). Carry no SAF value. Carry CBG as a CONVERTER slice until commissioning proof.

---

## 5. OPERATOR INPUTS FOR DELIBERATION AND STAGE 11

### 5.1 Base-case drivers (claude.ai; INFERENCE unless tiered)

| Driver | Bear | **Base** | Bull | Basis |
|---|---|---|---|---|
| FY27 litres (cr L) | about 25 (award cut + sugar ban) | **about 34** | 40+ (relaxed zoning) | Rule B: allocation evidence [AGENCY] + Q2 orders [MGMT] |
| EBITDA per litre | below Rs 10 | **Rs 11-12** | Rs 15-16 (maize at face value) | Rule C: feedstock mix bridge (V2) |
| FY27 EBITDA ex-PLI | — | **about Rs 390 Cr** | — | litres × margin |
| Net debt / EBITDA Mar-27 | stays near 5.7x | **about 3.7x** | — | inventory conversion |
| FY27 EPS | — | **Rs 17-18** | — | about 8.58 cr shares (Rs 3,810 Cr / Rs 444) |
| CBG | zero until commissioned | **CONVERTER slice** | annuity at R3 | Amendment 17 default |
| SAF | 0 | **0** | 0 | no FID, no funding |

### 5.2 Earnings-basis cautions
- Interest subvention (about Rs 50 Cr reliable) ends about Mar-2028. A Year-3 exit earnings basis must exclude it.
- FY26 was restated; use restated figures only.
- 100% deferred tax in Q1 FY27 implies a cash-tax step-up risk.

### 5.3 Rulings needed at the P/E gate (do not pick; present to operator)
1. **Sector cap.** No bioenergy row exists in the Section 1B table. Candidates: Agri processing 20x; Recycling / manufacturing 25x. Claude's recommendation for the operator: Agri processing 20x for the ethanol line (government-priced, feedstock-driven).
2. **CBG treatment.** CONVERTER at 0.5 × destination ROCE + 7.5 (Amendment 17 default), until three plants are commissioned.
3. **Earnings basis.** Ex-subvention for any year beyond FY28.
4. **Pillar 1 ROCE base and Pillar 2 cash band.** To be computed from filed FY26 restated and FY25. Cash conversion is INDETERMINATE until the H1 FY27 cash-flow statement.
5. **Size.** Small ceiling (2-3%) under the integrity CONCERN. A starter should wait for the H1 balance sheet (all three AVOID triggers resolve there or on MCA).

---

## 6. INDICATIVE VALUATION CHECK (NOT Stage 11; for the Halt 1 posture only)

| Step | Value |
|---|---|
| CMP (01-Oct-2026 close, Screener [SECONDARY]) | Rs 444; mcap about Rs 3,810 Cr |
| FY27 base EPS | Rs 17-18 [INFERENCE] |
| Current P/E on FY27 base | about 25x |
| Indicative destination | about 11-13x |
| Read | Recognition gap closed. The 25% CAGR hurdle needs the bull path (litres 40+ and margin near Rs 15/L) or a CBG re-rating. |

---

## 7. SECOND-ORDER CHAINS (Rule F floor of five)

- **Chain 1. Allocation, not capacity, binds.**
  - About 34 cr L fills about 56% of operating capacity [INFERENCE].
  - Fixed costs are spread over rationed litres; every extra litre allocated is high-margin.
  - [INFERENCE] The ESY27 award moves EPS more than any cost lever. Watch zoning, not capex.
  - Confirm or break: ESY27 award and zoning (tracker rows 1-2).
- **Chain 2. Grain economics sit in two other markets.**
  - Maize competes with poultry feed demand; DDGS sells into the same feed market.
  - Rice depends on FCI policy price and quantity.
  - [INFERENCE] A maize price spike hurts twice: input up, and DDGS competes with cheaper feed substitutes. The Rs 10/L floor can break without any policy change.
  - Confirm or break: Agmarknet maize prices; FCI rice notices (rows 9-10).
- **Chain 3. Inventory carries the deleveraging.**
  - The 5.7x → 3.7x path assumes inventory converts to cash by Mar-2027.
  - WC limits are Rs 600 Cr; CRISIL is already Negative.
  - [INFERENCE] If OMC lifting slows, inventory sits on WC lines and DSCR stays near 1.0, inviting a DSRA call.
  - Confirm or break: H1 FY27 balance sheet and cash flow; lender DSRA decision (rows 3, 5).
- **Chain 4. CBG debt lands on a watched balance sheet.**
  - Rs 650-700 Cr of CBG debt against CRISIL's "large debt-funded capex" trigger.
  - GAIL holds veto rights; TruAlt cannot steer the subsidiaries alone.
  - [INFERENCE] A downgrade raises funding cost for the core ethanol business before CBG earns.
  - Confirm or break: CRISIL review; commissioning (row 14).
- **Chain 5. The family needs liquidity.**
  - Promoters buy with borrowed money against pledged stock; Rs 55.4 Cr sits with family entities.
  - [INFERENCE] A price fall can force pledge invocation, and family liquidity needs can pull more cash from the listed company.
  - Unsaid: no purpose stated for the Accutrade advance; the NHPL receivable is for NHPL's own share-sale costs.
  - Confirm or break: H1 balances; pledge filings (rows 6, 13).
- **Chain 6. NSL is both supplier and customer.**
  - Syrup bought from NSL (FRP-linked MSA); diesel apparently sold to NSL.
  - [INFERENCE] The listed company acts as a group trading arm. Pricing either way can move value between NSL and minority shareholders.
  - Confirm or break: Reg 23(9) RPT disclosures; QX1 (row 12).

---

## 8. PROMOTER VERDICT (operator ruling, 02-Oct-2026)

**CONCERN (integrity).**
- **Size ceiling:** Small (2-3%).
- **Integrity items:** I1 to I7 (Section 2, V6). The ledger cannot offset these.
- **Structure concerns carried as tripwires:** S1 pledge-funded promoter buying; S2 NSL dealings.
- **AVOID triggers (hard stop if fired):** Accutrade Rs 40 Cr or more at H1 FY27 without supplies; TGPL rights price well below Rs 30.90; NHPL dues unpaid at 30-Sep-2026.

---

## 9. TRACKER, TRIPWIRES AND CALENDAR

**Tracker rows WRITTEN to DOWNSTREAM SIGNAL TRACKER, 02-Oct-2026: 19 rows**, all linked to the COMPANIES MASTER row (page 3acbb2b9d3ab81ddb7e1ea44725a4a32).

| # | Signal | Tier | Next check |
|---|---|---|---|
| 1 | ESY27 OMC allocation award | T1 | 15-Dec-2026 |
| 2 | ESY27 tender terms and zoning | T1 | 15-Nov-2026 |
| 3 | Q2 FY27 litres and H1 inventory conversion | T1 | 15-Nov-2026 |
| 4 | Q3 FY27 litres, EBITDA/L, margin | T1 | 15-Feb-2027 |
| 5 | Lender DSRA / BG decision and covenants | T1 | 15-Nov-2026 |
| 6 | Accutrade and NHPL balances (AVOID) | T1 | 15-Nov-2026 |
| 7 | TGPL rights price PAS-3 (AVOID) | T1 | 15-Oct-2026 |
| 8 | Sugar-route order ESY27 | T3 | 31-Oct-2026 |
| 9 | FCI rice for ethanol | T3 | 31-Oct-2026 |
| 10 | North Karnataka maize price | T2 | 01-Nov-2026 |
| 11 | Ugar Sugar peer volumes | T2 | 15-Nov-2026 |
| 12 | NSL related-party dealings | T2 | 15-Nov-2026 |
| 13 | Promoter-group pledges | T2 | 01-Nov-2026 |
| 14 | CBG commissioning (GOBARdhan) | T2 | 15-Feb-2027 |
| 15 | SAF FID or funding | T2 | 01-Nov-2026 |
| 16 | SC SLP 22411/2026 | T3 | 15-Nov-2026 |
| 17 | Blending mandate beyond E20 | T3 | 01-Jan-2027 |
| 18 | CC 977/2019 (MD personally) | T4 | 15-Jan-2027 |
| 19 | GST demand and water licences | T4 | 15-Nov-2026 |

URL verification: every row's Primary Source URL is an issuing-body landing page; deep links were not verified live this session, as stated in each row's Notes.

**Calendar:**
- Mid-Oct 2026: TGPL PAS-3 lookup (operator, MCA).
- ~21-Oct-2026: Sep-2026 shareholding pattern (pledge totals).
- By 31-Oct-2026: ESY27 sugar-route and FCI rice decisions.
- Late Oct / mid-Nov 2026: **Q2 FY27 results + first half-yearly cash flow (master gate).** Accutrade and NHPL balances; inventory; Q2 litres vs 11 cr L.
- Mid-Nov 2026: ESY27 tender; H1 Reg 23(9) RPT disclosure.
- Dec 2026: ESY27 award.
- Feb 2027: Q3 FY27 (proof-gate leg 1).
- May 2027: Q4 FY27 (proof-gate leg 2); Mar-2027 balance sheet (governance gate).

---

## 10. OPEN ITEMS (monitoring, not blockers)

- MCA lookups (operator, paid): TGPL PAS-3 rights price; Accutrade Global LLP Form 11; Leafiniti AOC-4; MRN Bhima; Onkar Agro.
- BSE: Reg 23(9) H2 FY26 RPT filing not yet checked.
- Jio Credit facility: LTV and margin-call price.
- QX1 (Section 0): NSL MSA pricing clause.
- Management questions for the Q2 call: Accutrade purpose and supplies; NHPL repayment date; DSRA / BG decision; CBG commissioning schedule per plant; Q3 traded-goods nature.

---

## 11. LESSONS_ARCHIVE CLOSE-OUT (append; OPEN ACTION lines to LESSONS.md for OPEN rows)

| # | What went wrong or was corrected | Stage | File / rule | Status |
|---|---|---|---|---|
| 1 | Margin-per-litre claim attached to the wrong feedstock (rice vs maize) | V2 / 09b | State the feedstock with every per-litre margin | OPEN (prompt fix) |
| 2 | Converted capacity read as added capacity (Unit 4) | V3 | Distinguish converted, installed and licensed capacity in every capacity line | OPEN (prompt fix) |
| 3 | Cash accrual first estimated at Rs 130 Cr; restated lines give Rs 196-224 Cr | V4 | Build accrual from filed PBT + D&A − tax, restated basis | CLOSED (this dossier) |
| 4 | Subsidiary turnover vs segment revenue gap (Rs 18 Cr) not reconciled by verifiers | V5 | Reconcile subsidiary turnover (AOC / agency) against segment revenue | OPEN (verifier check) |
| 5 | Personal cases of a director read as company misstatement | V6 | Separate company disclosure duty from director-personal matters | CLOSED |
| 6 | Deck claims entered drafts before filing cross-check (CBG break-even, Unit 4) | 09b | Every deck number gets a filed cross-check before entering a mental model | OPEN (prompt fix) |

---

## 12. BLOCK FOR `companies/TRUALT.md` (replace the named sections)

```
## THESIS (one line)
Rationed ethanol converter (OMC-allocated litres x margin per litre) inside a family group,
moving from sugar-seasonal to dual-feed year-round; CBG (51%, GAIL/Sumitomo) is a policy-priced
build-out held as a CONVERTER slice; SAF valued at zero. FY27 base ~34 cr L at ~Rs 11-12/L.
Priced for the transition (~25x FY27 EPS vs ~11-13x indicative). Promoter CONCERN (integrity).

## DECISION STATUS AND ENTRY ZONE
Halt 1 ruling 02-Oct-2026 (operator): PROCEED to /fttcp (override of Claude's SHALLOW WATCH).
Decision Status in Notion is operator-set only: WATCHLIST. Size ceiling Small (2-3%).
CMP Rs 444 (01-Oct-2026 close, Screener). Master gate: Q2 FY27 + first half-yearly cash flow.

## HALT 1 GATE
- Mental Model signed: YES (operator, 02-Oct-2026). Archetype: rationed commodity converter
  inside a family group; CBG = CONVERTER slice until commissioned; SAF = 0.
- Halt 1 decision: PROCEED (02-Oct-2026)
- Handover: runs/trualt-2026-09-18/inputs/research/web-handover-dossier.md
- Tracker proof: 19 rows written to DOWNSTREAM SIGNAL TRACKER 02-Oct-2026 (T1 x7, T2 x6,
  T3 x4, T4 x2), linked to COMPANIES MASTER page 3acbb2b9d3ab81ddb7e1ea44725a4a32.

## OPERATOR RULINGS
- 2026-10-02: Mental model signed. Promoter CONCERN (integrity): I1 Accutrade Rs 40.31 Cr,
  I2 decks ahead of filings, I3 AR gaps, I4 TGPL rights-then-flip, I5 Acuite non-cooperation,
  I6 fines, I7 NHPL Rs 15.08 Cr. Ledger cannot offset. Size ceiling Small (2-3%).
- 2026-10-02: AVOID triggers: Accutrade >= Rs 40 Cr at H1 FY27 without supplies; TGPL rights
  price well below Rs 30.90; NHPL dues unpaid at 30-Sep-2026.
- 2026-10-02: Halt 1 = PROCEED to /fttcp.
- Pending at P/E gate: sector cap (Agri processing 20x recommended), CBG converter treatment,
  ex-subvention earnings basis beyond FY28.

## ACTIVE TRIPWIRES
AVOID-1 Accutrade >= Rs 40 Cr at H1 FY27 | AVOID-2 TGPL rights price << Rs 30.90 |
AVOID-3 NHPL dues unpaid at 30-Sep-2026 | T1 ESY27 award < 25 cr L | T2 Q3 or Q4 FY27
< 9 cr L or EBITDA < Rs 10/L | T3 EBITDA margin < 12% or CRISIL downgrade | T4 DSRA cash call
or covenant waiver | T5 promoter encumbrance up / invocation | T6 NSL dealings rising |
T7 CBG commissioning slips past FY28

## OPTIONALITY REGISTER (summary)
- CBG (CONVERTER until three Sumitomo plants commissioned; ~Rs 15 Cr/qtr by Q2 FY28 gate)
- SAF (zero; reopens on FID with committed equity and offtake)
- Blending mandate above E20 (would loosen the ration)
```

*End of dossier. Where silent, the corpus governs.*
