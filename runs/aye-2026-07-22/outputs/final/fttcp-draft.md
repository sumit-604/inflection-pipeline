# FTTCP Draft: Aye Finance Limited (AYE)

Company: Aye Finance Limited. Ticker: AYE. CMP: not provided in the run inputs (manifest cmp 0.0; Phase 3 must source it). Run date: 2026-07-22. Mode: first workup. Lender business, so this runs the Lender Transition Set (AUM growth, NIM/spread, asset quality, RoA/RoE) in place of the four standard transitions. Concall coverage is thin: one collected transcript, the Q3 FY26 maiden call. This is not no-concall mode, but the two most recent calls (Q4 FY26 and Q1 FY27) were not collected, so their content reaches this analysis only through the operator digest, which is non-anchored. FTTCP confidence is reduced accordingly and the reduction is flagged in every section that leans on the digest.

---

## MY RULINGS

Every call below is made. Nothing here is a question. For a `genuinely uncertain` call, both readings are stated and the one the draft used is named, for the operator to overturn if wanted.

**Setup 1, forward window.** 3 months primary, 6 months secondary, 12 months for the RoA and RoE transition. AYE reports quarterly and Q1 FY27 just printed, so the standard windows hold. Confidence: `sure`. Proven wrong if the company stops quarterly reporting, which it will not.

**Setup 2, business type.** Lender. B04 sets business_type to lending, 84% of income is loan interest, and the balance sheet is a loan book funded by borrowings. The Lender Transition Set applies. Confidence: `sure`. Proven wrong only if the business were misclassified, which the prospectus and results rule out.

**Setup 3, workup intent.** First workup. No companies/AYE.md exists and run_type is full. Every Role 1 derived field (destination PE, prior thesis, prior devil's advocate) is N/A because FTTCP precedes Role 1. Confidence: `sure`.

**Setup 4, sector cap row.** The manifest says "Pharma / CDMO". That is a collector error. AYE is a lending NBFC, so the correct Section 1B row is Banks / NBFCs / MFIs, exit PE ceiling 18x, with P/B as the primary method and the PE only a cross-check (Section 1B Amendment 7 and Amendment 8). Phase 3 stage 11 must use this corrected row. Confidence: `sure`. Proven wrong only if a lender-specific row finer than "NBFC" were added to the Section 1B table, which does not exist today.

**AUM growth transition, forward verdict FIRING.** AUM compounded about 25% to 28% and reached Rs 7,044 Cr in FY26 and Rs 7,324 Cr at June 2026, with disbursements growing about 20% to 22%. Confidence: `fairly sure`. Proven wrong if AUM growth prints below 20% year on year for two consecutive quarters.

**NIM and spread transition, forward verdict STAGNANT.** NIM is a peer leading 15.94% and cost of borrowing is falling with a documented rating tailwind, but management guides NIM down to 14.25% to 14.75% for FY27 on a deliberate shift toward lower yield secured lending. A transition guided lower is not expanding, so it rounds down to STAGNANT rather than STARTING. Confidence: `fairly sure`. This is the softest of the four calls. The alternative reading is STARTING at +1, on the view that the cost of funds tailwind and the elite absolute NIM deserve credit; the draft used STAGNANT at 0 because management's own guidance is a decline. Proven wrong if NIM holds at or above 15% through FY27 while cost of borrowing keeps falling.

**Asset quality transition, forward verdict STARTING.** This is the critical lender transition. Credit cost has fallen for five to six consecutive quarters toward the guided band, GNPA has fallen for four consecutive quarters, and collection efficiency sits above 99%. But credit cost has not yet printed four quarters inside the guided 3.5% to 4.0% band, the mortgage book is only about three years old and unseasoned, and 41% of the book is unsecured. So the recovery is real and documented but not yet confirmed through a full cycle. It scores STARTING, not FIRING. Confidence: `fairly sure`. Proven wrong, in the bad direction, if GNPA reverses upward from 4.49% in the next anchored quarter.

**RoA and RoE transition, backward TEMPORARILY DEPRESSED, forward RECOVERING.** RoE fell from about 17% in FY24 to 9.3% in FY26, then rose to 11.7% in Q1 FY27; RoA fell from about 4.3% to 1.9% at the H1 FY26 trough, then rose to 3.71% in Q1 FY27. The depression has two identifiable temporary causes: the credit cost spike, now normalising, and the post IPO excess capital, which drags RoE until it is leveraged into loan growth. If growth stopped tomorrow, RoE would still recover as credit cost falls, so this is TEMPORARILY DEPRESSED, not DECLINING. Confidence: `fairly sure`. Proven wrong if RoA falls below 3% or RoE below 9% again in the next two prints.

**Cash determination reframed for a lender.** For a balance sheet lender, negative cash from operations is structural: loan disbursements are an operating outflow under Ind AS 7. The FTTCP cash transition is read as asset quality, which is STARTING. There is one residual issue that is not resolved: reported profit leans increasingly on gain on derecognition from securitisation, which rose from 1.94% of income in FY23 to 3.65% in FY26. That residual keeps the Phase 1 gate at PROCEED WITH CAVEATS. Confidence: `fairly sure`. Proven wrong if gain on derecognition stays near or below 3.65% of income while reported profit growth stops depending on it.

**Pillar 1 normalization route, Route A governs.** AYE carries post IPO excess capital: CRAR is about 42% against a roughly 15% regulatory floor, so a large share of net worth is not yet earning, which is the denominator bloat Route A corrects. The Route B condition is also present (TEMPORARILY DEPRESSED plus RECOVERING with a pre depression RoE history near 16% to 17%), but under the single credit rule Route A governs and Route B is suppressed so the recovery is not counted twice. Confidence: `fairly sure`. The single pre depression clean year (FY24) is thin, so the operational RoE anchor is held conservative. Proven wrong if the excess capital is deployed faster than modelled, lifting operational RoE toward the 17% to 20% management target sooner.

**Composite and position, +4, DEEP WATCH leaning BUY-ON-DIPS.** AUM +2, NIM 0, asset quality +1, RoA and RoE +1, sum +4. No Kernex cap (no transition is DECLINING with no catalyst). No TRIM (not all four fired backward). Confidence: `fairly sure`. Proven wrong, upward, if NIM holds and asset quality prints a fourth quarter inside the guided band (either would push toward +5 or +6); proven wrong, downward, if GNPA reverses.

**Tier assignment, Tier A, 25% hurdle.** Tier B is barred because Gate 0 is AVOID and EM is 19.6, so the "Gate 0 GOOD or better OR EM at least 25" quality gate fails, even though institutions hold about 35% and the promoter read is TRUSTWORTHY. Confidence: `sure`.

**Undiscovered Alpha, not applied.** UA needs FII plus DII below 3%. AYE is at about 35%. Institutions are heavily present, so UA does not apply. Confidence: `sure`.

---

## Transition 1: AUM and disbursement growth (replaces revenue)

| Period | AUM (Rs Cr) | AUM YoY % | Disbursements (Rs Cr) | Basis |
|---|---|---|---|---|
| FY22 | NOT FOUND | NOT FOUND | NOT FOUND | private pre-IPO, restated series starts FY23 |
| FY23 | NOT FOUND (AUM ~Rs 3,000s) | NOT FOUND | NOT FOUND | prospectus restated, exact AUM not isolated in extract |
| FY24 | NOT FOUND | NOT FOUND | NOT FOUND | rating cites 25% CAGR FY20-25 |
| FY25 (ACTUAL) | 5,525 | ~25% CAGR context | NOT FOUND | rating p.1 (AUM Rs 5,525 Cr at Mar-2025; Rs 5,721 Cr at Jun-2025) |
| FY26 (ACTUAL) | 7,044 | +26 to 27% | 5,169 | digest (Q4FY26 deck); AUM growth corroborated by B01 on-book loans +26.6% |
| Q1 FY27 (ACTUAL) | 7,324 | +28% | 1,219 (+22% YoY) | digest (Q1FY27 deck); results filing 2246e44a confirms the period |
| FY27 (EXPECTED) | ~8,800 to 9,200 | +25 to 30% guided | ~6,200 to 6,700 | illustrative, from management FY27 AUM guidance 25-30% (digest, non-anchored) |
| FY28-FY31 (EXPECTED) | illustrative | ~25 to 30% aspiration | illustrative | management medium-term aspiration ~28-33% (digest); framework-disciplined SOM implies ~18% (B09) |

What it means: AUM growth is the clearest of the four transitions. The book has compounded in the mid twenties, disbursements are still growing around 20%, and management guides 25% to 30% for FY27. Forward verdict FIRING. The one honest caution is that the framework disciplined three year SOM in B09 implies about 18% revenue CAGR, well below management's 28% to 33% aspiration, so the aspiration is aggressive against the addressable market maths even though the near-term growth is real.

## Transition 2: NIM and spread (replaces margin)

| Period | NIM on ATA % | Cost of borrowing % | Basis |
|---|---|---|---|
| FY23-FY25 (ACTUAL) | NOT FOUND (not isolated) | NOT FOUND | prospectus; spread level not cleanly extracted |
| Q3 FY26 (ACTUAL) | NOT FOUND | 10.96 (incremental 10.31) | digest (Q3FY26 deck) |
| Q4 FY26 (ACTUAL) | NOT FOUND | 10.87 (incremental 10.13) | digest (Q4FY26 deck) |
| Q1 FY27 (ACTUAL) | 15.94 (+161 bps YoY) | 10.78 (incremental 10.20) | digest (Q1FY27 deck) |
| FY27 (EXPECTED) | 14.25 to 14.75 guided | ~10.4 to 10.6 (25-35 bps cut guided) | illustrative, management FY27 guidance (digest) |
| FY28-FY31 (EXPECTED) | illustrative, mix-driven down | illustrative, lower | secured mix shift lowers yield; rating upgrade lowers funding cost |

What it means: NIM is peer leading at 15.94% and the cost of borrowing is falling, helped by the India Ratings upgrade to A plus and a plan to refinance about Rs 2,400 Cr of roughly 11% legacy debt. But management guides NIM down to 14.25% to 14.75% because it is deliberately shifting toward lower yield secured mortgage lending. A margin guided lower is not expanding, so the forward verdict is STAGNANT. The quality point is that the lower NIM buys lower credit cost, so RoA is guided up even as NIM comes down; that benefit is scored in the asset quality and RoA transitions, not here, to avoid double counting.

## Transition 3: Asset quality (replaces cash conversion, the critical one)

| Period | GNPA / Gross Stage III % | NNPA % | Credit cost % | Collection efficiency % | Basis |
|---|---|---|---|---|---|
| FY24 (ACTUAL) | 3.0 to 3.2 | NOT FOUND | NOT FOUND | NOT FOUND | rating p.2 (3.0% at Mar-2024) |
| FY25 (ACTUAL) | 3.5 | NOT FOUND | 6.16 (Q4FY25) | NOT FOUND | rating p.2; credit cost from digest |
| Sep 2025 (ACTUAL) | 4.85 (Stage III); 90+dpd 5.1 | 1.78 net Stage III | NOT FOUND | NOT FOUND | prospectus Note 53.13.4/5; rating p.2 (90+dpd 5.1%) |
| Q3 FY26 (ACTUAL) | 4.94 | 1.98 | 4.67 | 99.3 to 99.4 | digest (Q3FY26); concall corroborates direction |
| FY26 / Q4 (ACTUAL) | 4.77 | 1.80 | 4.30 | 99.5 | results FY26 (audited) + digest; PCR 63.7% |
| Q1 FY27 (ACTUAL) | 4.49 | 1.50 | 4.01 | 99.2 | results filing 2246e44a (GNPA 4.49% anchored); PCR 63.8% |
| FY27 (EXPECTED) | ~4.0 to 4.5 | ~1.3 to 1.6 | 3.5 to 4.0 guided | ~99 | illustrative, management FY27 credit cost guidance (digest) |
| FY28-FY31 (EXPECTED) | illustrative, ~3.5 to 4 | illustrative | 3.25 to 3.75 aspiration | ~99 | management medium-term aspiration (digest) |

What it means: this is a genuine, documented recovery. Credit cost has fallen for five to six straight quarters, GNPA has fallen for four straight quarters from 4.94% to 4.49%, and collections run above 99%. The stress was growth induced, from an over lending phase before mid 2024 that management has since tightened; 92% of the book is now originated after that phase. Against that, the recovery is only a few quarters old, credit cost at 4.01% has only just reached the top edge of the guided band rather than printing four quarters inside it, the mortgage book is unseasoned, and 41% of lending is unsecured. So the forward verdict is STARTING, one notch below FIRING, and the whole FTTCP call turns on this transition continuing.

## Transition 4: RoA and RoE trajectory (replaces ROCE)

| Period | RoA % | RoE % | Basis |
|---|---|---|---|
| FY24 (ACTUAL) | 3.7 | 16.1 (restated ~17.28) | rating p.1; B03 restated RoE |
| FY25 (ACTUAL) | 2.8 | 11.8 | rating p.1 |
| H1 FY26 trough (ACTUAL) | 1.92 (annualised) | 7.63 (annualised) | B03 (DuPont: profitability-driven, leverage flat) |
| FY26 (ACTUAL) | 3.1 | 9.3 | digest (FY26); PAT Rs 194 Cr |
| Q1 FY27 (ACTUAL) | 3.71 (on assets); 4.18 on AUM | 11.7 | digest (Q1FY27); PAT Rs 74.5 Cr anchored in results filing |
| FY27 (EXPECTED) | 4.0 to 4.5 guided | ~12 to 15 | illustrative, management FY27 RoA guidance (digest); RoE lags on excess capital |
| FY28-FY31 (EXPECTED) | ~4.0 to 4.5 | 17 to 20 aspiration | illustrative, management medium-term aspiration (digest) |

What it means: returns collapsed on the credit cost spike and the post IPO capital raise, and are now recovering. RoA is already back to 3.71%, near the guided 4% to 4.5%. RoE at 11.7% is still well below the 17% to 20% target because CRAR at 42% means a lot of equity is sitting idle; RoE lifts as that capital is leveraged into AUM growth. Backward this is TEMPORARILY DEPRESSED, forward it is RECOVERING. It is not FIRING because RoE is still far from target and the recovery is young.

---

## The catalyst story in plain words

AUM growth needs no catalyst to keep firing; it needs the book not to break. The growth is already in the numbers and management has the capital to fund it. The risk is not too little growth, it is growth of the wrong kind: the one major red flag the verifier layer caught, and the pipeline did not, is that 39% of FY26 growth came from repeat loans to existing borrowers and about 60% from lending more per branch, in a micro borrower segment that has already been through one over lending cycle. More debt per borrower is exactly what caused the last stress.

The asset quality recovery is the catalyst that matters. What would confirm it: credit cost printing inside 3.5% to 4.0% for a fourth straight quarter, GNPA staying below 4.5%, and the unseasoned mortgage book holding sub 2% credit cost as it ages. What would kill it: GNPA turning back up, or a state level microfinance disruption spilling into the business loan book. On that last point the peers are a warning, not a comfort. SBFC lived through the Karnataka ordinance and said the damage travelled by ticket size, not geography, which undercuts AYE's framing that a Bihar style event stays contained. SBFC also said its sub Rs 7 lakh secured book carries higher credit cost and near double the recovery time, which cautions AYE's sub 2% mortgage aspiration.

The funding and returns catalysts are documented and real. The India Ratings upgrade to A plus and A1 plus in June 2026 is a public, dated event that lowers the cost of funds, and the plan to refinance Rs 2,400 Cr of 11% legacy debt is specific. The post IPO capital is deployed and CRAR is at 42%, so growth is funded for at least two years. These support the RoA recovery. The honest caveat across all of this is that the two most recent calls were not collected, so much of the forward evidence sits in a non anchored digest, and confidence is reduced.

Management intent and action ledger, in one line per transition: AUM has both vision and documented action (capital raised, disbursements growing), so it holds at FIRING. NIM has vision (cost of funds down) but management itself guides the margin lower, so it stays STAGNANT. Asset quality has both vision and documented action (tightened underwriting, five to six quarters of falling credit cost), which is why it earns STARTING rather than STAGNANT. RoA and RoE have documented action (capital deployed, credit cost falling) and score RECOVERING. Nothing here is a case of vision without action being used to lift a verdict, and nothing lifts a Kernex cap because none is engaged.

---

## THE VERDICT

The composite is +4 out of a possible +8: AUM growth FIRING at +2, NIM STAGNANT at 0, asset quality STARTING at +1, and RoA and RoE RECOVERING at +1. That lands in the DEEP WATCH leaning BUY-ON-DIPS band, meaning a small starter is defensible only with a strict entry zone, which Phase 3 will set. The Kernex cap did not engage because no transition is going backwards without a catalyst, and the TRIM rule did not engage because the four transitions did not all fire backward. The whole call turns on one print: Gross Stage III staying on its downward path from 4.49%. If that reverses, asset quality and returns both weaken together and the composite falls; if credit cost instead prints a fourth quarter inside the guided band while NIM holds, the composite rises toward +5 or +6.

### Step 3 scorecard

| Transition | Backward verdict | Catalyst strength | Forward probability | Forward verdict | Score |
|---|---|---|---|---|---|
| AUM growth | FIRING | Strong | >60% (3-6m) | FIRING | +2 |
| NIM / spread | SUSTAINED at elite, guided down | Moderate (cost of funds) | 20-40% of expansion (3-6m) | STAGNANT | 0 |
| Asset quality | DETERIORATING then recovering | Moderate to Strong, documented | >40% continued improvement (3-6m) | STARTING | +1 |
| RoA / RoE | TEMPORARILY DEPRESSED | Moderate to Strong | >60% RoA, lower for RoE (12m) | RECOVERING | +1 |
| | | | | COMPOSITE | +4 / 8 |

### Step 5 monitoring triggers

| # | Trigger | Threshold | Horizon | What it changes |
|---|---|---|---|---|
| 1 | GNPA reversal | Gross Stage III rises for any two consecutive quarters from 4.49% | 3-6 m | Asset quality STARTING to STAGNANT or DECLINING; composite falls |
| 2 | Credit cost in band | Credit cost inside 3.5-4.0% for a fourth consecutive quarter | 6 m | Asset quality STARTING to FIRING; composite to +5 |
| 3 | NIM defence | NIM holds at or above 15% while cost of borrowing keeps falling | 6-12 m | NIM STAGNANT to STARTING; composite to +5 |
| 4 | AUM growth | AUM YoY below 20% for two consecutive quarters | 3-6 m | AUM FIRING to STARTING; composite falls |
| 5 | RoE recovery | RoE rises through 14% toward the 17-20% target | 12 m | Confirms RoA/RoE RECOVERING; supports Pillar 1 |
| 6 | Over-lending check | Repeat-loan share of growth or AUM per borrower rising while GNPA rises | 6 m | Confirms the verifier-B major flag; hits asset quality |
| 7 | Earnings quality | Net gain on derecognition rises above about 4% of total income | 3-6 m | Reinforces the residual INDETERMINATE earnings-quality caveat |
| 8 | Covenant breaches | The 14 unwaived instances (23.6% of borrowings) resolve or grow | 6 m | Funding risk; tests the disclosure-gap flag |
| 9 | Concall collection | Q4 FY26 and Q1 FY27 transcripts obtained and read directly | next refresh | Raises FTTCP confidence from the current reduced level |

### Handoff to valuation (Phase 3)

| Field | Value |
|---|---|
| RoA/RoE forward verdict | RECOVERING (TEMPORARILY DEPRESSED backward) |
| Pillar 1 basis (lender) | ROE, not ROCE (Section 1B Amendment 7) |
| Pillar 1 normalization route | Route A (operational RoE, excess-capital denominator fix); Route B condition present but suppressed per single-credit |
| Pillar 1 RoE anchor | operational RoE, held conservative ~15% (see base card); management target 17-20% |
| ROE recovery credited via | Pillar 1 (Strategic Premium ROE re-rating barred) |
| Pillar 2 (lender) | Asset-Quality Multiplier, drafted 0.80x (GNPA >4%), live alternative 1.00x |
| Sector cap row | Banks / NBFCs / MFIs, 18x, P/B primary and PE cross-check only |
| Tier | A, 25% hurdle |
| UA | not applied (FII+DII ~35%) |
| SHARED CATALYST flag | asset-quality normalisation drives BOTH the asset-quality transition AND the RoA/RoE recovery; the devil's advocate must stress-test this single point of failure |

---

## THE P/E BASE CARD (for operator approval)

This is a preview of the exit multiple, computed from Section 1B off what is known now, for the operator to approve. It is not the valuation; Role 1 runs the full dual track exercise in Phase 3. For a lender, P/B is the primary method and the destination PE is a secondary cross check, so read the P/B line first.

Primary lens, P/B: theoretical P/B is ROE divided by cost of equity. On a normalised RoE near 16% to 17% and a cost of equity around 14.5%, fair P/B is about 1.1x to 1.2x. On the current depressed RoE of 11.7%, fair P/B is about 0.8x. Fair value on this lens rests entirely on whether the RoE recovery to the mid teens is believed.

Secondary lens, destination PE cross check:

- Pillar 1: RoE used, held conservative at operational RoE about 15% under Route A (post IPO excess capital stripped from the base; the single pre depression clean year FY24 near 16% to 17% is thin, so the anchor is held down). Continuous formula 0.5 times RoE plus 7.5 gives a base of about 15.0x. On current reported RoE of 11.7% the base would be 13.4x. Provisional on the operator's RoE anchor choice.
- Pillar 2: Asset-Quality Multiplier 0.80x drafted, because GNPA at 4.49% is above 4% and the book is unseasoned. Live alternative 1.00x, because PCR is 63.8%, the ECL cushion is 3.4 times the RBI floor, and GNPA and credit cost have improved for several quarters. This single choice moves the card materially and is the second key operator input.
- Pillar 3: +2x. Component 3a growth visibility earns +2x on documented AUM growth of about 26%, which is the lender analog of the growth machinery test, held at +2x because the delivery grade is C (grade C caps 3a at +2x). Component 3b moat formation earns +0x because EM is 19.6, MODEST, below the premium threshold. Component 3c duration earns +0x, no documented multi year contracted revenue.
- Strategic premium: +0x. The RoE recovery is credited in Pillar 1, so the Strategic Premium ROE re-rating route is barred by the single credit rule.
- Undiscovered Alpha: not applied. FII plus DII is about 35%, far above the 3% institutional absence test.
- Sector cap: 18x absolute (Banks / NBFCs / MFIs).

Destination PE, both tracks:

- Additive track: (Pillar 1 base times Pillar 2) plus Pillar 3. On the drafted inputs, (15.0 times 0.80) plus 2 equals about 14.0x. On current RoE and 0.80x, about 12.7x. On operational RoE and 1.00x, about 17.0x. All sit under the 18x cap. Anchored to Section 1B Amendment 5 (Pillar 1 formula), Amendment 7 (asset-quality multiplier), Amendment 4.1 (Pillar 3a), Amendment 8 (sector cap).
- RRM track: the reversion multiplier is RRM equals 1 plus (13.5 minus r) times 0.12, bounded 0.70 to 1.60 (Amendment 4.4, percentage points). For a Tier A transition NBFC carrying residual asset quality risk, r is about 15% to 16%, giving RRM about 0.70 to 0.82. Applied to the additive base that produces a governing destination PE of roughly 10x to 11.5x. The exact r and the dual track construction are finalised in Phase 3; this track is provisional. On divergence the lower RRM track typically governs.

Provisional destination PE, pending operator approval of the RoE anchor and the asset-quality multiplier: roughly 11x to 14x on the drafted conservative inputs, with an upper path to about 17x if the operator approves the 1.00x asset-quality multiplier and the operational RoE anchor. All under the 18x sector ceiling. P/B remains primary.

THE EARNINGS BASIS QUESTION, for the operator to decide, not chosen here: one year forward P/E, applied to forward EPS, versus trailing P/E, applied to trailing EPS. The note for the decision: trailing EPS is depressed by the credit cost trough, so a trailing multiple prices a temporarily low earnings base; forward EPS captures the credit cost normalisation the whole thesis rests on. Forward looks the better fit for a lender mid recovery, but the choice is the operator's at the gate, and it interacts with the RoE anchor above.

Card status: provisional on two operator inputs, the Pillar 1 RoE anchor (conservative operational ~15% versus the 17% to 20% management target) and the Pillar 2 asset-quality multiplier (0.80x versus 1.00x), plus the earnings basis choice.

---

*FTTCP v1.2, first workup, lender transition set. Confidence reduced by single collected concall (Q3 FY26 maiden); the two most recent calls reach this analysis through a non-anchored digest.*
