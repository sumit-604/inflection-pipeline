# STAGE 11 — ROLE 1 DUAL-TRACK VALUATION: CMS INFO SYSTEMS (CMSINFO)

Run: runs/cmsinfo-2026-08-29. Model: Opus 4.8. Date: 2026-08-31.
Framework: Master v3.6 / Section 1B v3.3+v3.5.1+v3.6+v3.7+v3.8+v3.9 / FTTCP v2.1.

Entity count: 1. Single consolidated pass. SOTP REJECTED: segment returns are
unusable (inter-segment billing 9.1% of revenue; its FY26 increase = 72% of the
Managed Services segment result). Combined Cash Management + Managed Services
returns are used only where segment returns are discussed (role1-handover Sec 8.3).

Section 1B is SETTLED by operator ruling (fttcp-deliberation.md Sec 4). It is
reproduced below, not re-derived. All pillar numbers are verbatim from the
operator-approved table.

---

## SECTION 1A — METHOD SUITABILITY MATRIX (mandatory before any 1B math)

| Method | Suitable? | Weight | Reason |
|---|---|---|---|
| P/E (destination) | YES — PRIMARY | 50% | Profitable, clean earnings, PAT margin 12.2%. Section 1B settled. Framework default primary. Forward basis both ends (Amendment 18.1). |
| EV/EBIT | YES — secondary | 20% | Asset-owning operator. Strips both leverage and depreciation-policy differences; the fairest single cross-comparison against Brink's/Radiant. Carries the ATM useful-life caveat (7->10yr lowered D&A ~Rs 48m, flatters EBIT). |
| EV/EBITDA | YES — secondary | 15% | Capital-intensive; peer table live. Reads CHEAP (5.8x vs 8.1-8.2x). Disagrees with P/E; the disagreement is a Brink's-leverage artefact, shown not averaged. |
| DCF | YES — tertiary, constrained | 15% | FY26 FCF NEGATIVE Rs 19 Cr. FCF% must stay consistent with the 1.15x cash multiplier (do not assume conversion improves). High terminal sensitivity. |
| P/B | CONSIDERED, REJECTED | 0% | Book does not carry the Rs 8,126m contracted rental book. CMS 1.8x vs Radiant 1.4-1.5x is a weak signal. |
| EV/Sales | REJECTED | 0% | Mature business; sales multiple uninformative. |
| DDM | REJECTED | 0% | Payout ~28-30%; not a dividend story. |
| EV/capacity | REJECTED | 0% | Machine counts not cleanly disclosed; brown-label sits under sponsor banks. |

Method plurality satisfied: four methods applied, primary/secondary weighting
declared. Triangulation table in Section 3.

---

## SECTION 1B — SETTLED. REPRODUCED, NOT RE-DERIVED.

Converter classification stated first (override 7): **NON-CONVERTER**. Amendment 17
machinery does not apply. Pillar 1 ROCE input is spot FY26 post-tax ROCE, no
through-cycle smoothing (fttcp-deliberation Sec 4).

| Step | Value | Note (source: fttcp-deliberation Sec 4 / role1-handover Sec 4) |
|---|---|---|
| A. Pillar 1 ROCE | 16.6% current | FTTCP sole authority. Normalisation route NONE. RECOVERING but NO forward uplift (proof gate FY28 ROCE>22% NOT fired). |
| Pillar 1 base PE | 16.0x | Band table. General Amendment 5 formula (0.5x16.6+7.5) = 15.8x, immaterial 0.2x. |
| B. Pillar 2 cash multiplier | 1.15x | Operator Override 1. CFO/PAT 1.28x sustained 5yr earns top band; FY26 FCF NEGATIVE breaks the 1.30x condition. One notch down, not two. |
| C. Quality-adjusted base | 18.4x | 16.0 x 1.15. |
| D. Pillar 3 growth/moat premium | +0x | EM 23 < 25 (MODEST not STRENGTHENING). |
| E. Strategic premium | +0x | No licence/scarcity; L1 lowest-bidder on SBI; awaiting IBA pricing committee. |
| F. Raw destination PE | 18.4x | C + D + E. |
| F2. UA-adjusted | 18.4x | No uplift. FII+DII ~58.70%, fails <3% threshold. UA does NOT apply. |
| G. Sector cap | 25x "Cables / Industrial products" | Non-binding. |
| H. Pre-trim destination | 18.4x | min(F2, G). |
| I. Amendment 20 relative trim | **-> 17.0x** | 30% test FAILED at 18.4x vs ~12.9x peer median (43% premium). Trimmed. |
| **FINAL destination (exit) PE** | **17.0x, band 15.7x to 18.3x** | Operator-approved, non-negotiable. Governs both tracks. |

ROCE-recovery credit route: NEITHER Pillar 1 midpoint NOR Strategic Premium
(proof gate not fired; single-credit preserved for later). SHARED CATALYST flag:
YES (FY28 ROCE recovery and any future growth premium ride the same capex-fill
event). Disposition cap: PROCEED WITH CAVEATS (FLAG-CASH INDETERMINATE).

Earnings basis (Amendment 18.1, one basis both ends): **FORWARD.** Entry = CMP /
FY27E EPS. Exit = 17.0x x FY30E EPS. Rationale stated once: the three-year hold to
August 2029 lands five months into FY30, so the exit multiple looks one year
forward exactly as the entry does.

### Step 1C — Relative valuation cross-check (Amendment 20): CLOSED

The live peer table was supplied by Claude web (role1-handover Sec 3). Step 1C is
not PENDING; it ran and produced the trim to 17.0x already embedded above. Not
re-run here (operator ruling settled). Recorded for the card:

| | CMS | Brink's | Radiant |
|---|---|---|---|
| P/E | 13.2x TTM / 11.0x fwd | 12.9x TTM / 11.3x fwd | 11.3-13.0x |
| EV/EBITDA | 5.8x | 8.2x TTM / 6.8x fwd | 8.1x |
| EV/EBIT | 8.9x | 12.3x TTM / 9.2x fwd | — |
| ROCE / ROIC | 16.6% | 6.5% | 12.7% |
| Balance sheet | Net cash Rs 442 Cr | Net debt $2.94bn, 2.7x | Net cash |

Divergence recorded (Amendment 20.5 printout): pillar destination 18.4x vs peer
median ~12.9x = +43% > 30% -> relative check governs the exit multiple choice,
trimmed to 17.0x. The P/E leg fails the 30% test; the EV/EBITDA and EV/EBIT legs
pass comfortably (CMS cheaper than peers). The split is a leverage artefact
(Brink's net debt 2.7x inflates its EV and depresses its equity P/E; CMS net cash
does the reverse). Carried into triangulation, not averaged away.

### Option Resolution Calendar (Amendment 18.2-18.4): N/A

CMS is a single operating entity with no discrete SOTP option slices. There is no
within-hold option to price as a resolved state and no beyond-hold option to
re-date. The FY28 ROCE proof gate is a RESOLUTION EVENT for the transition thesis,
not an option slice carrying separate value. Transition dual-display (18.6): N/A.

---

## SECTION 2 — PROJECTIONS FY27 THROUGH FY31 (three cases + probability-weighted base)

Horizon = hold + 1 (Amendment 18.0): hold years FY27/FY28/FY29, exit prices FY30E,
Year-4 = FY31 shown. All figures Rs Cr unless EPS (Rs). Shares 16.00 Cr.

### 2.1 Revenue — SERVICES and TOTAL separately (role1-handover Sec 6, constraints 4-5)

Services is the right line. Hardware resale fell 25.9% by deliberate choice and
drags total. Q1 FY27 services grew 9.5% YoY (Rs 571 Cr -> Rs 625 Cr), ~13.8%
adjusting back the Rs 25 Cr currency-shortage loss.

Revenue guidance DISCOUNTED one band (three straight years of revenue misses,
management grade B-). Margin taken NEAR FACE (Q1 FY27 printed 27.2%; guide raised
to ~27% while revenue was cut).

| | FY26A | FY27E | FY28E | FY29E | FY30E | FY31E |
|---|---|---|---|---|---|---|
| Services revenue | ~2,360 | 2,650 | 2,940 | 3,265 | 3,625 | 4,000 |
| Services YoY | — | +12.3% | +10.9% | +11.1% | +11.0% | +10.3% |
| Hardware / other | ~127 | 100 | 90 | 85 | 80 | 78 |
| **Total revenue** | **2,487** | **2,750** | **3,030** | **3,350** | **3,705** | **4,078** |
| Total YoY | — | +10.6% | +10.2% | +10.6% | +10.6% | +10.1% |

Services CAGR FY27->FY30 = (3,625/2,650)^(1/3)-1 = **11.0%**. Below management's
13-14% organic + ~4% inorganic (16-18%) and below the SOM-implied signed pipeline
(~21,000 ATMs across SBI/HDFC/ICICI + FSS). Conservative by one band.

FY27 guide sanity (constraint 5): services low-end Rs 2,650 Cr against Q1 actual
Rs 625 Cr needs Rs 675 Cr/quarter x3, +8% on the highest quarter CMS has printed.
Low-end plausible; high-end (Rs 2,750) a stretch. Base uses the low end.

### 2.2 Margin, depreciation, earnings — probability-weighted BASE path

Binding constraint 1: **FY27 is the depreciation peak, not FY26.** Q1 FY27 D&A
Rs 72.8 Cr annualises ~Rs 291 Cr vs FY26 Rs 208 Cr (+40%). FY27 is NOT the recovery
year. Constraint 3: capital employed FALLS if capex (guided Rs 100-125 Cr) stays
below depreciation (~Rs 290 Cr); the FY26 capital base is not permanent.

| | FY27E | FY28E | FY29E | FY30E | FY31E |
|---|---|---|---|---|---|
| Total revenue | 2,750 | 3,030 | 3,350 | 3,705 | 4,078 |
| EBITDA margin | 26.5% | 26.8% | 27.0% | 27.1% | 27.1% |
| EBITDA | 730 | 812 | 905 | 1,004 | 1,105 |
| D&A | 291 | 296 | 300 | 302 | 305 |
| EBIT | 439 | 516 | 605 | 702 | 800 |
| Net other income (net cash) | ~21 | ~24 | ~28 | ~32 | ~36 |
| PBT | ~460 | ~522 | ~595 | ~676 | ~766 |
| Tax @ ~25.5% | ~117 | ~133 | ~152 | ~172 | ~195 |
| PAT | ~342 | ~389 | ~443 | ~504 | ~571 |
| **EPS (Rs)** | **21.4** | **24.3** | **27.7** | **31.5** | **35.0** |

EPS CAGR FY27->FY30 = (31.5/21.4)^(1/3)-1 = **13.8%**. FY31 fade ~+11%.

FY27E EPS: consensus Rs 22.51 (four analysts, cut from Rs 23.20 post-Q1); operator
build Rs 21.4. **Use the lower Rs 21.4 (conservative), both shown.** The handover
midpoint of Rs 22.0 is between the two. Sensitivity: at FY27 EPS Rs 19 (a 14% miss)
entry P/E rises to 12.8x but required growth to FY30 rises and the Hurdle still
lands ~2.21. The effects offset; FY30 is what matters.

### 2.3 FY27 ROCE — tested at both readings (constraint 2)

FTTCP draft ~16% counts the depreciation rise but not the EBITDA rise. Operator
~19-20% holds capital flat and credits EBITDA at ~Rs 730 Cr.

- FTTCP reading: post-tax EBIT = (730-291) x 0.745 = Rs 327 Cr; on a grossed
  capital base ~Rs 2,040 Cr -> **~16.0%**.
- Operator reading: same post-tax EBIT Rs 327 Cr on FY26 capital ~Rs 1,700 Cr held
  flat -> **~19.5%**.

**I use the operator ~19.5% FY27 ROCE.** It is immaterial to Section 1B: the exit
PE is locked at 17.0x and no forward uplift is credited regardless, because the
proof gate is FY28 ROCE>22%, not FY27. FY27 is the depreciation peak, not the gate.

Do NOT model a return to FY25 segment returns (constraint 7): combined Cash
Management + Managed Services capital employed rose Rs 12,123m -> Rs 16,141m
(+33%). Restoring FY25 profit on FY26 capital gives 20.3%, not 25.2%.

### 2.4 The three cases (role1-handover Sec 6) — the FY28 fork

FY28 ROCE is the fork. Everything follows from it.

| | Case A one-off build | Case B treadmill | Case C margin fails |
|---|---|---|---|
| Probability | 40% | 40% | 20% |
| Capex FY27/28/29 (Rs Cr) | 125 / 250 / 280, then maintenance | 250 / 350 / 400, rising | overshoots |
| Capital employed | roughly flat | keeps rising | rising |
| EBITDA margin FY28/29/30 | 26.0 / 26.8 / 27.1% | ~26% | reverts to 24.5% |
| **FY28 ROCE** | **~23.8%** | **~20.8%** | **~15.8%** (~CoC) |
| FY29 ROCE | ~26.7% | ~22.0% | stuck |
| Proof gate (FY28 >22%) | **FIRES** | **MISSES** | falsifier fires |
| **FY30E EPS (Rs)** | **35.0** | **32.5** | **22.5** |

Probability-weighted FY30E EPS = 0.4x35.0 + 0.4x32.5 + 0.2x22.5 =
14.0 + 13.0 + 4.5 = **Rs 31.5**. This is the base-case exit earnings.

Probability-weighted FY28 ROCE = 0.4x23.8 + 0.4x20.8 + 0.2x15.8 = **~21.0%**,
marginally below the 22% gate. On the blended base the proof gate is NOT FIRED,
consistent with the settled Pillar 1 (no forward uplift). This is not a valuation
input; it confirms the pillar treatment.

FTTCP-consistency row: base services CAGR 11.0% is BELOW the SOM-implied pipeline
and below management guidance -> conservative. No assumption exceeds the SOM;
nothing to cut.

---

## SECTION 3 — APPLY EACH METHOD

Two reference frames: a THREE-YEAR exit value (what the P/E primary delivers on the
holding period) and a TODAY fair value (what the EV/DCF cross-checks say CMS is
worth now). Both carried; the P/E three-year value governs the entry zone.

### 3.1 P/E (primary, 50%) — locked 17.0x on FY30E, forward basis

- Exit price = 17.0x x FY30E EPS 31.5 = **Rs 535.5**.
- Three-year dividends over the hold (FY27+FY28+FY29 DPS at ~28% payout on rising
  EPS: ~6.0 + ~6.8 + ~7.8) = **~Rs 19** (conservative; rounds to operator's Rs 19).
- **Three-year value = 535.5 + 19 = Rs 554.5 ~ Rs 555.**
- Band (15.7x to 18.3x on FY30E 31.5, + Rs 19 div): Rs 514 to Rs 595.
- Today-equivalent (17.0x x FY27E 21.4) = Rs 364 (used in the today-basis triangulation).

### 3.2 EV/EBIT (secondary, 20%) — CMS cheap; ATM useful-life caveat

CMS 8.9x vs Brink's 12.3x TTM / 9.2x fwd. Applying Brink's forward 9.2x to CMS
FY27E EBIT Rs 439 Cr: EV = Rs 4,039 Cr; + net cash Rs 442 Cr = Rs 4,481 Cr;
/16 = **Rs 280/share** today. At CMS's own 8.9x -> Rs 272. At Brink's TTM 12.3x ->
Rs 365. Central read **~Rs 290**. CMS is CHEAP on EV/EBIT. Caveat: the FY26 ATM
useful-life change (7->10yr) lowered depreciation ~Rs 48m and flatters EBIT, so the
8.9x is marginally understated (CMS looks slightly cheaper than like-for-like).

### 3.3 EV/EBITDA (secondary, 15%) — CMS cheap; leverage artefact

CMS 5.8x vs Brink's 6.8x fwd / 8.2x TTM and Radiant 8.1x. Applying a
quality-and-proof-discounted 6.5-7.0x to CMS FY27E EBITDA Rs 730 Cr: EV
Rs 4,745-5,110 Cr; + net cash Rs 442 Cr; /16 = **Rs 324 to Rs 347**, central
**~Rs 330**. At CMS's own 5.8x on forward EBITDA -> ~Rs 292 (near CMP). CMS is
CHEAP on EV/EBITDA. **This is the method that most loudly disagrees with the P/E
trim.** The disagreement is a leverage artefact: Brink's 2.7x net debt inflates its
EV (raising its EV/EBITDA) and depresses its equity P/E; CMS net cash does the
reverse. Shown in the range, not averaged (operator standing instruction).

### 3.4 DCF (tertiary, 15%) — hard constraint, consistent with 1.15x

FY26 FCF was NEGATIVE Rs 19 Cr. Pillar 2 is 1.15x precisely for that. FCF% is held
consistent with a 1.15x cash multiplier — no magic improvement. Capex guided
Rs 100-125 Cr against depreciation ~Rs 290 Cr is not sustainable; **capex reverts
toward depreciation by FY30.**

- WACC 12% (net cash, low beta, offset by small-cap and INDETERMINATE cash).
- Terminal growth 5%.
- FCF held to ~7-9% of revenue (conservative; steady state capex ~= D&A, WC drag on
  a growing book keeps FCF below PAT):

| | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|
| FCF (Rs Cr) | 250 | 280 | 320 | 360 |
| PV @12% | 223 | 223 | 228 | 229 |

- PV of explicit FCF = Rs 903 Cr.
- Terminal = 360 x 1.05 / (0.12-0.05) = Rs 5,400 Cr; PV = Rs 3,434 Cr.
- EV = Rs 4,337 Cr; + net cash Rs 442 Cr = equity Rs 4,779 Cr; /16 = **~Rs 299/share** today.
- Sensitivity: WACC 13% / g 4% -> ~Rs 250; WACC 11% / g 5% -> ~Rs 350. Range
  Rs 250-350, central ~Rs 290-300. Corroborates the EV cross-checks.

### 3.5 Triangulation

**Three-year (holding-period) value — P/E primary governs:**

| Method | Three-year value | Weight |
|---|---|---|
| P/E 17.0x x FY30E 31.5 + Rs 19 div | Rs 555 | primary |

**Today fair value — all four methods (governs the reasonableness of the entry zone):**

| Method | Today value (Rs/sh) | Weight | Read |
|---|---|---|---|
| P/E (17.0x x FY27E 21.4) | 364 | 50% | destination applied to forward EPS |
| EV/EBIT (~9.2x fwd) | 290 | 20% | CMS cheap; ATM life caveat |
| EV/EBITDA (~6.5-7.0x fwd) | 330 | 15% | CMS cheap; leverage artefact |
| DCF (12% / 5%, FCF cons.) | 290 | 15% | corroborates |
| **Weighted today fair value** | **~Rs 333** | | |

The methods DIVERGE on the multiple narrative (P/E trims the exit multiple to 17x;
EV multiples say CMS trades cheap now), but they CONVERGE on the number: the entry
zone Rs 284 (Section 4, from the P/E three-year method) sits inside the EV/DCF
today-fair-value band Rs 280-330. The divergence is displayed, not averaged: the
final range carries both the cheap-EV read (~Rs 330) and the trimmed-P/E read.

---

## SECTION 4 — DUAL TRACK, ENTRY ZONE, AMENDMENT 19, VERDICT

### 4.1 Dual track (both carried)

- **Track 2 (additive Four-Pillar): 17.0x, band 15.7x to 18.3x. GOVERNS.** Operator-
  approved final destination, post Amendment 20 trim.
- **Track 1 (RRM): ~14.9x** (draft from fttcp-deliberation Override 2; not re-derived
  here). More conservative.
- Divergence = (17.0 - 14.9) / 17.0 = **12.4%**, under the 15% threshold. Governing
  track = Track 2 (operator-approved base binds; the operator ruled on the additive
  destination after the Amendment 20 trim). RRM shown as the conservative reference.

**Fair values (three-year value = destination x FY30E EPS + dividends):**

| | Bear (Case C, 15.7x) | Base (prob-wtd, 17.0x) | Bull (Case A, 18.3x) |
|---|---|---|---|
| Track 2 additive | 15.7 x 22.5 + 15 = **Rs 368** | 17.0 x 31.5 + 19 = **Rs 555** | 18.3 x 35.0 + 21 = **Rs 661** |
| Track 1 RRM (14.9x) | 14.9 x 22.5 + 15 = Rs 350 | 14.9 x 31.5 + 19 = Rs 488 | 14.9 x 35.0 + 21 = Rs 543 |

### 4.2 Entry zone and Hurdle (Tier A, divisor 1.953)

Tier B is BARRED: FLAG-CASH is INDETERMINATE, which fails Tier B's "no structural
FLAG-CASH" gate. Tier A only.

- **Entry = exit-consistent three-year value / 1.953 = 554.5 / 1.953 = Rs 284.**
- Entry band (destination band 15.7x-18.3x): Rs 513.6/1.953 = Rs 263 to
  Rs 595.5/1.953 = Rs 305. Central **Rs 284**.
- **MoS = 20% below entry = 284 x 0.80 = Rs 227.**
- CMP Rs 243: **14.4% below entry** (243/284) and **7.0% above MoS** (243/227).
  CMP sits between MoS and entry -> BUY-ON-DIPS zone on price.

**Hurdle Ratio** = (1 + EPS CAGR)^3 x (Destination PE mid / Current PE), pass >= 1.953.
- Current (entry) PE = CMP / FY27E EPS = 243 / 21.4 = 11.35x (11.05x on EPS 22.0).
- EPS CAGR FY27->FY30 = 13.8%; (1.138)^3 = 1.472.
- HR = 1.472 x (17.0 / 11.35) = 1.472 x 1.498 = **2.20**.
- Equivalent closed form: HR = exit price / CMP = 535.5 / 243 = 2.204.
- **HR 2.20 >= 1.953 -> PASS.** Bull EPS CAGR not needed (base passes). Credibility
  grade B- would cap Bull at Base+5% if used; not used.

### 4.3 Recognition gap resolution (override 13)

Current PE 11.35x forward vs destination 17.0x. TO-rung neighbourhood is R2-R3
(~15-19x). The current PE sits WELL BELOW the destination -> **recognition gap is
OPEN**; the market has not repriced to the TO rung. Re-rating engine is LIVE:
17.0 / 11.35 = +50%. The gap is exactly the re-rating the destination PE captures.
Transition Decision Matrix read: proof NOT FIRED + ARTIFACT (the ROCE dip is an
artefact of the capex climb) + gap OPEN -> RESEARCH / WATCH. Constructive but not
yet a trade; watch the FY28 gate.

### 4.4 Amendment 19 — fair-value path, FV CAGR, return-source class

FV path on the governing track (Track 2, 17.0x), base case, forward basis rolled
one year at each step (18.1). Net debt held at net cash; no option slices to carry.

| Point | Forward EPS | FV = 17.0x x EPS (Rs) |
|---|---|---|
| Today (Aug-2026) | FY27E 21.4 | 364 |
| End-Year-1 (FY27 close) | FY28E 24.3 | 413 |
| End-Year-2 (FY28 close) | FY29E 27.7 | 471 |
| End-Year-3 (FY29 close, exit) | FY30E 31.5 | 535 |

**FV CAGR over the hold: 13.8% (today Rs 364 to end-Year-3 Rs 535, governing track,
base case).** Computed (535/364)^(1/3)-1 = 13.8%.

**Return-source classification: HYBRID (FV CAGR 10-20%).**

Decomposition line (19.3): the FV path compounds at 13.8% on EARNINGS alone — the
multiple is held at the destination 17.0x at every step, so the FV path carries NO
re-rating lever. The re-rating lever is separate: it lives in the gap between CMP
(11.35x) and the destination (17.0x), which the entry discount closes. Total holding
return from CMP to exit (535/243 = 2.20 over 3yr = 30.1% CAGR) splits roughly half
earnings (ln 1.472 = 49%) and half re-rating (ln 1.498 = 51%); on the operator's
framing ~55% earnings / ~45% re-rating. Both readings land HYBRID: return comes
partly from FV growth, partly from the discount closing, and the entry zone matters
proportionally. There are no non-compounding option slices (single operating entity),
so no static-slice drag and no FV-step events (19.4 N/A).

### 4.5 VERDICT CARD

| Field | Value |
|---|---|
| CMP | Rs 243 (NSE close 28-Aug-2026) |
| Destination PE — Track 2 additive (GOVERNS) | 17.0x, band 15.7x-18.3x |
| Destination PE — Track 1 RRM | ~14.9x (conservative reference); divergence 12.4% <15% |
| Earnings basis | FORWARD, both ends (Amendment 18.1) |
| Three-year value (base) | Rs 555 (bear Rs 368 / bull Rs 661) |
| Entry price (25% CAGR, /1.953) | **Rs 284** (band Rs 263-305) |
| MoS price (20% below entry) | **Rs 227** |
| CMP position | 14.4% below entry, 7.0% above MoS -> BUY-ON-DIPS zone |
| Hurdle Ratio | **2.20 >= 1.953 -> PASS** |
| Expected 3-yr CAGR (prob-weighted, ex-div) | ~30% |
| Upside/downside | ~5:1 (today FV Rs 333 vs CMP; downside to MoS Rs 227) |
| FV CAGR | **13.8% -> HYBRID** |
| Recognition gap | OPEN; re-rating engine LIVE (+50%) |
| Method divergence | P/E trims the exit multiple; EV/EBITDA + EV/EBIT say CMS cheap (leverage artefact) — carried in the range |
| **Valuation-level verdict (on price)** | **WATCHLIST / BUY-ON-DIPS** — CMP below the 25% entry and Hurdle PASS put price in buy-on-dips territory; not below MoS, so not a strong buy |
| **Disposition** | **PROCEED WITH CAVEATS** — FLAG-CASH INDETERMINATE (INDUSTRY-EVENT-INDUCED); proof gate FY28 ROCE>22% NOT fired |
| Decision Status | operator-only, NOT set here |

**Read.** On price alone CMS clears the 25% hurdle: the Hurdle Ratio is 2.20, CMP
sits 14% below the Rs 284 entry, and every cross-check method says the stock is
cheap-to-fair today (Rs 280-364). The re-rating engine is live and the return is
HYBRID, roughly half earnings and half discount closing. But two things cap the
disposition at PROCEED WITH CAVEATS and hold the verdict at WATCHLIST: FLAG-CASH is
INDETERMINATE (1-2yr overdue receivables +752% YoY while a standalone loss allowance
was released), and the FY28 ROCE>22% proof gate has not fired. Price does not clear
those. Constructive setup, gated on the FY28 print. This matches the operator's
indicative WATCHLIST call.

**Cross-check against operator reference numbers (role1-handover Sec 9):** three-year
value Rs 555 (op ~555, match), entry Rs 284 (op ~284, match), MoS Rs 227 (op ~227,
match), Hurdle 2.20 (op ~2.20, match), HYBRID with ~50/50-to-55/45 earnings/re-rating
split (op ~55/45 HYBRID, match), CMP 14% below entry / 7% above MoS (op match). The
independent build lands on the operator's numbers; no material divergence to flag.

---

```yaml
stage: B11-valuation
company: "CMSINFO"
run_date: "2026-08-29"
model: claude-opus-4-8
status: complete
entity: "consolidated single-entity"
entity_count: 1
input_gaps: []
flags:
  - "FLAG-CASH: INDETERMINATE (INDUSTRY-EVENT-INDUCED). Pillar 2 multiplier applied = 1.15x (one notch below top band, FY26 FCF NEGATIVE breaks the 1.30x condition). Caps disposition at PROCEED WITH CAVEATS."
  - "Proof gate FY28 ROCE>22% NOT fired. No forward Pillar 1 uplift credited. Shared catalyst: FY28 ROCE recovery and any future growth premium ride the same capex-fill event."
  - "SOTP REJECTED: inter-segment billing 9.1% of revenue, its FY26 increase = 72% of Managed Services segment result; segment returns unusable. Combined Cash Management + Managed Services returns only."
  - "Method divergence displayed not averaged: P/E relative check fails 30% test (trim to 17.0x); EV/EBITDA 5.8x vs 8.1-8.2x and EV/EBIT 8.9x vs 12.3x say CMS cheap. Leverage artefact (Brink's net debt 2.7x)."
framework_versions: "Master v3.6 / Section 1B v3.3+v3.5.1+v3.6+v3.7+v3.8+v3.9 / FTTCP v2.1"
pe_basis: "forward"
exit_pe_base_approved: "17.0x (band 15.7x to 18.3x), forward basis both ends; operator-approved at FTTCP gate 30-Aug-2026, post Amendment 20 trim"
destination_pe:
  track1_rrm: {low: 14.9, mid: 14.9, high: 14.9, r_used: 0, rrm: 0}   # RRM ~14.9x draft from fttcp-deliberation Override 2; not re-derived; r_used/rrm not recomputed
  track2_additive: {low: 15.7, mid: 17.0, high: 18.3}
  divergence_pct: 12.4
  governing_track: "Track 2 additive 17.0x (operator-approved post Amendment 20 trim); RRM 14.9x conservative reference; divergence 12.4% < 15%"
pillar_detail:
  roce_used: 16.6
  roce_base: 16.6
  roce_recovery_route: "not-credited"
  pillar1_normalization_route: "none"
  cash_multiplier: 1.15
  structural_or_growth: "INDETERMINATE (industry-event-induced); conservative 1.15x multiplier applied"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 25
hurdle_ratio: {base: 2.20, bull_used: false, verdict: "PASS"}
fair_values:
  track1: {bear: 350, base: 488, bull: 543}
  track2: {bear: 368, base: 555, bull: 661}
expected_cagr_prob_weighted: 30.1
entry_range: {low: 263, high: 305}
mos_price: 227
upside_downside_ratio: 5.1
decision: "WATCHLIST (BUY-ON-DIPS on price: CMP Rs 243 is 14% below the Rs 284 entry, 7% above MoS Rs 227, Hurdle PASS 2.20; on-valuation favourable but disposition capped at PROCEED WITH CAVEATS by FLAG-CASH INDETERMINATE and unfired FY28 proof gate)"
unresolved_inputs_used: []
som_cagr_crosscheck: "consistent (base services CAGR 11.0% below management guidance 16-18% and below the SOM-implied signed pipeline; conservative, one band discounted)"
one_line_thesis: "A contracted cash-logistics operator trading 14% below its 25% entry at 11x forward on a live re-rating gap to a 17x destination; HYBRID return, half earnings half discount closing, gated on the FY28 ROCE proof and the unresolved receivables flag."
```
