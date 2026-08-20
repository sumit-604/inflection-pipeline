# STAGE 11 — ROLE 1 VALUATION, v3.6 RECOMPUTE (11-valuation-v2)

**Company:** Jubilant Agri and Consumer Products Ltd (JACPL) | **Ticker:** JUBLCPL
**CMP:** Rs 2,342.40 (18-Aug-2026, B00-inputs) | **Shares:** 1.5152 Cr | **Market cap:** Rs 3,549 Cr
**Run folder:** runs/jublcpl-2026-08-18 | **Recompute date:** 2026-08-20
**Model:** claude-opus-4-8 | **Method:** SUM OF THE PARTS (operator direction 18-Aug-2026)
**Framework stack:** Master v3.6 / Section 1B v3.3 + v3.5.1 + v3.6 / Debt Capacity v1.0 / Market-Implied Assumptions v1.0

**Versioning note.** This is the ORDERED v3.6 recompute. The 18-Aug B11 (v3.3 stack)
and the 19/20-Aug surgical B11-valuation-v2.yaml (which held Business B verbatim and
found "no output number changed") are both PRESERVED as the audit record. This run is
the FULLER v3.6 pass the operator ordered: it runs the two Damodaran pre-steps that the
surgical pass declared NOT FOUND (Debt Capacity, and Market-Implied against the
now-present macro-sheet.md), applies the Amendment 14 fade horizon with an explicit
year-by-year step-down (the surgical pass asserted the ladder "already fades" and did not
rebuild it), re-decides Amendment 13 on the dense-RPT trigger (the surgical pass found no
trigger), and computes Amendment 15 relative PE against the market PE that now exists.
Where the surgical pass said "does not bite," this pass shows where v3.6 DOES bite.

Operator-approved bases are held as the CEILING and re-derived under v3.6:
Business A 35x specialty-chemicals cap; Business B 14x normalized (20x agri cap, not
binding); blended 29.5x (pre-demerger context only). Earnings basis: ONE-YEAR FORWARD
(operator choice). Per-entity PAT/ROCE/cash are illustrative allocations — no standalone
accounts exist pre-demerger; stated at every use, never estimated into an anchor.

---

## PRE-STEP 1 — DEBT CAPACITY ASSESSMENT v1.0 (runs FIRST)

Backward-only judgement of solvency on the company's own history, before any transition
work. JACPL is near debt-free.

**Anchored inputs.** FY26 segment EBIT Rs 212.30 Cr (AR Note 39 p.150, B10). Interest
coverage FY25 8.93x -> FY26 23.91x; D/E FY25 0.17 -> FY26 0.06 (B03-ardeep, Financial
Highlights p.7 / standalone P&L pp.97-98). Net debt ~Rs 45 Cr (task input; near
debt-free). Implied FY26 finance cost = 212.30 / 23.91 = Rs 8.88 Cr.

**Unresolved, stated not estimated.** FY24 and FY25 standalone EBIT are NOT FOUND in the
anchored blocks (only the coverage RATIOS are anchored). Blended cost of debt is NOT
FOUND in the extracts. Per the input-unresolved rule I use a conservative mid-cycle EBIT
and a conservative cost of debt and then show the verdict is insensitive to both.

- Mid-cycle EBIT: FY26 was an above-trend year (gross margin +200bps, PBT margin +178bps
  YoY, B03). Conservative mid-cycle proxy = Rs 180 Cr (FY26 212.30 anchored, ~15% haircut
  for the lower-margin FY24-25 base that is NOT FOUND at segment level). INPUT UNRESOLVED:
  FY24-25 EBIT. Conservative assumption used: Rs 180 Cr mid-cycle, because the framework
  requires a mid-cycle (not peak) base and FY26 is above trend.
- Cost of debt: INPUT UNRESOLVED: blended borrowing rate. Conservative assumption used:
  9.0%, because that is ~225bps over the Aug-2026 10yr G-sec of 6.76% (macro-sheet), a
  conservative small-cap spread; a higher cost of debt only lowers capacity, and the
  verdict survives it.
- Coverage threshold: default 3x (the historical record — 8.93x then 23.91x — clears a
  far higher bar, so 3x is conservative).

**Step 1 — capacity.**
Maximum sustainable debt = mid-cycle EBIT / (3 x cost of debt) = 180 / (3 x 0.09) =
180 / 0.27 = **Rs 667 Cr**. (On the anchored FY26 EBIT 212.30 without haircut: Rs 786 Cr.)
Current net debt Rs 45 Cr. Headroom = 667 - 45 = **Rs 622 Cr = 93.3% of capacity.**

**Step 2 — coverage trend.** Anchored end-points: FY25 8.93x -> FY26 23.91x. Direction is
sharply IMPROVING (D/E 0.17 -> 0.06 over the same window; deleveraging plus margin
expansion, DuPont-confirmed margin/turnover-led not leverage-led, B03). Full FY22-24
series NOT FOUND; the two anchored years plus the deleveraging give a confident IMPROVING
read.

```
DEBT CAPACITY OUTPUT
Mid-cycle EBIT (Rs Cr, years used): 180 (conservative; FY26 212.30 anchored haircut ~15%; FY24-25 NOT FOUND)
Coverage threshold applied: 3x (default; historical 8.93x->23.91x clears a far higher bar)
Cost of debt (blended, %): 9.0 (conservative assumption; actual NOT FOUND)
Maximum sustainable debt (Rs Cr): 667 (786 on anchored FY26 EBIT)
Current debt (Rs Cr): 45 (net; near debt-free)
Headroom (Rs Cr): 622   Headroom (% of capacity): 93.3%
Coverage trend (5-yr): IMPROVING (FY25 8.93x -> FY26 23.91x; D/E 0.17 -> 0.06)
VERDICT: COMFORTABLE
```

**Consumed by Role 1:** COMFORTABLE, headroom 93%, coverage IMPROVING. The balance sheet
imposes no constraint on the forward thesis; the deleveraging is genuine, not a rescue.
Business B carries the working-capital/subsidy-receivable cash drag, but even loaded onto
agri it does not threaten group solvency. This does not change any fair value (the name is
near debt-free); it removes a downside tail.

---

## PRE-STEP 2 — MARKET-IMPLIED ASSUMPTIONS v1.0 (runs after operating EPS, before the Role 1 conclusion)

Reads the price backward before Role 1 reads the business forward.

**Inputs.** CMP Rs 2,342.40. Operating EPS ~Rs 84 (FY26 diluted 83.16 / basic 84.49,
B10; treasury/rental/investment gains not material at this level). Current PE = 2,342.40 /
84 = **27.9x** (blended pre-demerger entity). Market PE (macro-sheet 17-Aug-2026): Nifty 50
TTM **20.5x**; Nifty Smallcap 250 **34.4x**. Cost of equity ~14.1% (macro-sheet: 6.76% RF +
7.31% ERP). Operator hurdle 25%.

**Step 1 — reverse-engineered growth (algebra shown).**
Identity: Price CAGR = EPS CAGR x (Exit PE / Entry PE)^(1/3).

- Reading 1 (flat multiple, exit = current 27.9x). Price CAGR = EPS CAGR. To deliver the
  operator's 25% price hurdle the price needs **25% EPS CAGR**. To merely return the cost
  of equity (14.1%) it needs **14.1% EPS CAGR**.
- Reading 2 (reasonable exit PE). Reasonable exit = 27x — essentially flat with a token
  de-rate, justified because the name has ALREADY re-rated +58% in five months (SOTP
  reconciled read) and the macro-sheet GARP regime note has growth plentiful, both of
  which say the re-rating leg is largely spent; this is NOT a Section 1B multiple and NOT
  a round-number default. Solve for the EPS CAGR that returns cost of equity 14.1% at that
  exit: 1.141 = (1+g) x (27/27.9)^(1/3) = (1+g) x 0.9891, so 1+g = 1.1536, **g = 15.4%.**

**Step 2 — the market's implied story (4-6 sentences).**
1. At Rs 2,342, the market is assuming blended EPS compounds ~15% a year for three years
   just to return the 14.1% cost of equity at a roughly flat 27-28x exit.
2. At Rs 2,342, the market is assuming the specialty-chemicals margin holds and grinds up
   (Q1 FY27 segment margin 17.1% vs FY26 13.9%), not that it compresses.
3. At Rs 2,342, the market is assuming the retained polymer business stays elite-ROCE
   (segment 67.5% / group 36%) and does not fade to industry economics inside three years.
4. At Rs 2,342, the market is assuming NO further re-rating — the +58% five-month re-rating
   is treated as banked, and the price sits at 27.9x against a 20.5x Nifty (relative 1.36x).
5. At Rs 2,342, the market is assuming the demerger completes and the agri cash drag leaves
   with Business B, so the retained entity reports as a clean high-ROCE compounder.

**Step 3 — the spread.**
FTTCP evidence-supported growth (faded, blended) ~13% (polymer faded base ~10.5%, blended
down by the agri stub; task-stated ~13%).

> Price assumes ~15.4% EPS CAGR to be fair (25% to clear the hurdle at a flat multiple);
> FTTCP evidence supports ~13% faded. The spread is the trade.

Evidence (~13%) sits just BELOW the fair-value implied growth (~15.4%) and far below the
hurdle-clearing growth (25%). The 30% SOTP premium to fair value is almost entirely a
RE-RATING bet (27.9x -> 35x cap), and the re-rating potential is MODERATE-to-NONE
(+58% already done). Growth itself is roughly priced.

```
MARKET-IMPLIED ASSUMPTIONS OUTPUT
CMP: Rs 2,342.40    Operating EPS (FTTCP B4 proxy): Rs 84    Current PE: 27.9x
Reasonable exit PE used: 27x (basis: re-rating +58% already banked; GARP regime growth-plentiful; token de-rate)
Implied EPS CAGR at flat multiple: 25% to clear hurdle / 14.1% to return CoE
Implied EPS CAGR at reasonable exit PE: 15.4% (returns CoE 14.1%)
Market's implied story: [Step 2, five sentences above]
FTTCP evidence-supported growth: ~13% (faded, blended)
SPREAD: price ~15.4% (fair) / 25% (hurdle) vs evidence ~13%
Flag: FAIRLY PRICED (leaning PRICED-WE-ARE-LATE on the re-rating-exhausted read)
```

**Consumed by Role 1:** FAIRLY PRICED. The growth is priced; the only upside is a
re-rating the B8-proxy says is largely spent. This reinforces a WATCHLIST, wants-a-dip
posture and argues for the conservative end of the destination band and a wider MoS.

---

## SECTION 1A — METHOD SELECTION

Unchanged from the 18-Aug run and confirmed by operator direction. PRIMARY = **SUM OF THE
PARTS** (demerger special situation; value the retained polymer business and the departing
agri business separately). Within each part, PRIMARY = P/E on the Section 1B destination
multiple applied to forward operating EPS (both dual tracks), SECONDARY = the intrinsic
"fair value today" cross-check on FY27 forward PAT. EV/EBITDA de-emphasised (per-entity
capex/CFO NOT FOUND). DCF not run as primary (forward EPS is un-guided, built off one
seasonally strong quarter; a DCF would be false precision). Blended 29.5x retained for
the pre-demerger entity as CONTEXT only.

---

## SECTION 1B — FOUR-PILLAR DESTINATION PE, v3.6

### Business A — Performance Polymers & Chemicals (retained -> Jubilant Industries Ltd)

**Pillar 1 (Amendment 11 — 30x elite ceiling confirmed).**
FTTCP ROCE forward verdict FIRING; Pillar 1 uses current ROCE. Segment 67.5% (Note 39,
inflated by allocation) / group 36% (AR p.7). Both are > 33%, so the elite extension
governs: Base PE = 24 + 0.3 x (67.5 - 33) = 24 + 10.35 = 34.35 -> **capped at 30.0x.** (On
group 36%: 24 + 0.3 x 3 = 24.9x; either way the cap or the number lands well inside the
sector cap.) Amendment 11 supplies the AUTHORITY for the 30x that the 18-Aug card printed;
under the superseded Amendment 5 (24x cap) the base would have been 24.0x. Normalization
route NONE (Route A fails the 20% CWIP/idle test; Route B barred on a FIRING verdict).
ROCE recovery credited via: NOT credited (36% is the current high, not a recovery). Break-
even note: the 30x cap binds above 53% ROCE; the quality base only has to reach 22.6x for
the 35x sector cap to still bind downstream, so Pillar 1 is not the swing variable.

**Pillar 2.** Cash multiplier 1.15x, tagged clean AT SEGMENT LEVEL but unconfirmable
without a standalone cash statement (the structural FLAG-CASH drag is located in the
DEMERGING agri half, not here). CFO/PAT entity-level INDETERMINATE -> this caps the
cash-quality read at PROCEED WITH CAVEATS with the missing evidence (standalone cash flow)
named; it does not resolve silently to comfort. Quality-adjusted base = 30.0 x 1.15 =
**34.5x.**

**Pillar 3 (Amendment 16 gate).** EM 22.5 < 25 -> +0x on the evidence gate. The Amendment
16 crossover gate is SATISFIED (projected ROCE far above the ~13.5% minimum), so the gate
does not itself bar a premium, but the evidence gate (EM<25) does. Net **+0x. No change.**

**Strategic premium.** +2x (VP-latex #1 India / #2 global ex-China; sole food-grade PVAc
in India). ROCE re-rating optionality route stays barred by the single-credit rule.

**Raw / UA / cap.** Raw = 34.5 + 0 + 2 = 36.5x. UA applies (JACPL >12m listed; FII+DII
0.45% < 3%; Gate 0 71): F2 = 36.5 x 1.25 = 45.6x. Sector cap = 35x specialty chemicals, no
quality uplift. Category-Break Override: NOT invoked (no first-mover new category, no
binding named contract of that kind). **H = min(45.6, 35) = 35.0x (Track 2 additive).**

**Track 1 (RRM) — with the Amendment 12/13 r-worksheet.**

> r base 14.0%; durability adj 0 (band: **Unproven**, reason: <2yr public record /
> demerger-created — short-record risk OWNED here per 12C, so the -0.5 durability credit
> the v3.3 run gave is REMOVED); governance adj +0.25 (Finance Committee with Rs 1,250 Cr
> borrowing authority and zero independent directors; promoter CAUTION, partly offset by 0%
> pledge and an external CEO); cyclical surcharge 0 (Business A is not cyclical; band not
> docked for cyclicality; 12B cap N/A); **complexity adj +0.5 (Amendment 13 — dense-RPT
> trigger, see below)**; cash-conversion r-UP: none per 12A (Pillar 2 owns it at 1.15x);
> short-record r-UP: none per 12C; **final r 14.75%** (bounded [9,18]); RRM = 1 + (13.5 -
> 14.75) x 0.12 = **0.85.**

Track 1 destination = fundamental base 36.5x x RRM 0.85 = 31.03x, x1.25 UA = 38.78x,
min(38.78, 35) = **35.0x.** The cap binds. Sensitivity: the cap only moves once r > 15.44%
(RRM < 0.767); at 14.75% we are below that, so the +0.5 complexity charge and the removed
durability credit are REAL but fully absorbed by the 35x cap. **Both tracks: 35.0x. Range
32.5x-35.0x** (H +/-7.5%, capped).

**Amendment 13 decision (dense RPT) — the trigger I turn ON.** The 19-Aug surgical pass
found "no trigger" (2 subsidiaries, RPT 3.84% of revenue, unmodified audit). I re-decide:
the demerger is actively CREATING a more complex group, and the RPT is dense in KIND even
if small in revenue percentage — CSR routed 100% through a promoter foundation, KMP
compensation +63.6% YoY, a Finance Committee holding Rs 1,250 Cr borrowing authority with
zero independent directors. That is material related-party machinery that can move value
between the listed entity and promoter vehicles: the dense-RPT trigger fires. Audit is
unmodified (no qualification trigger) and subsidiary count is low (not that trigger), but
one trigger is enough. **+0.5 to r for BOTH entities.** This is priced once, in r, and
nowhere else (it does not dock a pillar or scale a premium). For Business A the cap absorbs
it; for Business B (below) it flows straight through the RRM track.

**Amendment 14 (fade horizon) — the material change, applied to the projection below.**

**Amendment 15 (relative PE).** Absolute H = 35.0x. Market PE 20.5x (Nifty 50 TTM,
macro-sheet 17-Aug-2026). **Relative destination PE = 35.0 / 20.5 = 1.71x.** Against the
Nifty Smallcap 250 (34.4x): 35.0 / 34.4 = 1.02x. Current relative = 27.9 / 20.5 = 1.36x
(Nifty), 0.81x (smallcap). Name's own and specialty-chemicals sector historical relative
bands: **NOT FOUND** (no anchored series; specialty-chem quality names historically sit at
a premium to market, ~1.4-1.8x, but that is general context, not an anchor). B8-proxy
re-rating potential = **MODERATE-to-NONE** (JACPL already re-rated +58% in five months; the
re-rating is banked). Conclusion: a 1.71x relative on a name that has just re-rated +58%,
in a regime the macro-sheet flags as growth-plentiful (re-rating leg weak) and with the
Smallcap 250 already 22% above its own 5-yr median, does NOT support pushing the exit to
the top of the band. The relative read places the realized exit toward the **LOW end
(32.5x)**, not the 35x cap. The absolute 35x cap remains the binding ceiling; the relative
expression only says: do not assume the re-rating the peer set no longer supports. Held on
the card at H = 35x (operator ceiling), with the fair value leaning to the low end and the
MoS widened (below).

### Business B — Agri (P&K Fertilizers + Agri Nutrients -> Jubilant Agri Solutions Ltd)

Earnings unchanged (cyclical, valued NORMALIZED, no fade needed). Only the r-worksheet
moves under v3.6.

- Pillar 1: ROCE 19.9% (segment, STAGNANT, normalized below the FY26 peak). ROCE <= 33% ->
  Base = 0.5 x 19.9 + 7.5 = **17.5x.** Route NONE. (Elite extension cannot reach a sub-33%
  ROCE — confirmed unchanged.)
- Pillar 2: 0.80x STRUCTURAL (NBS subsidy receivable). Quality-adjusted base = 17.5 x 0.80
  = **14.0x.** No growth offset (structural).
- Pillar 3 +0x; Strategic +0x; UA does NOT apply (JASL fresh listing <12m). Sector cap 20x
  agri processing (not binding). **Track 2 additive H = 14.0x.**

**Track 1 (RRM) r-worksheet, Business B.**

> r base 14.0%; durability adj 0 (band: Moderate/Unproven, docked FOR cyclicality);
> governance adj +0.25 (same group governance); **cyclical surcharge +0.75 (CAPPED per 12B
> — band docked for cyclicality: subsidy-linked commodity, monsoon-driven, FY25 segment
> loss to FY26 peak)**; **complexity adj +0.5 (Amendment 13, same group dense RPT)**;
> cash-conversion r-UP: none per 12A (structural drag priced in Pillar 2 at 0.80x);
> short-record r-UP: none per 12C; **final r 15.5%** (bounded [9,18]); RRM = 1 + (13.5 -
> 15.5) x 0.12 = **0.76.**

Track 1 destination = 14.0 x 0.76 = **10.6x** (no UA; cap 20x not binding). Track 2 additive
14.0x. Divergence ~28% -> the more conservative Track 1 (10.6x) governs the entry, but it
is moot: Business B is a value stub, AVOID either way. The 18-Aug run carried Business B
RRM at 13.2x (r 14.0, no cyclical/complexity surcharge); **v3.6 drops it to 10.6x** because
the cyclical surcharge (+0.75) and complexity (+0.5) that v3.3 did not levy now flow
straight through (no cap to absorb them here).

### Blended entity (pre-demerger context only)
Pillar 1 blended base 24.9x (group 36% ROCE, Amdt 11 elite extension; 24.0x under the
superseded Amdt 5). Cap binds at the revenue-weighted 29.5x (62.7% at 35x + 37.3% at 20x).
Destination 29.5x, range 27.5-31.5x. Context, not a usable multiple for the SOTP.

---

## SECTION 2 — PROJECTIONS WITH THE AMENDMENT 14 FADE HORIZON (Business A)

EM classification **MODEST** -> **growth fades to industry growth by Year 3** (not a flat
CAGR line). Industry (adhesives / specialty-chemicals blend) terminal ~8% (task band
7-10%). The hold is FY27->FY30 (Year 1 = FY28, Year 2 = FY29, Year 3 = FY30). Base year is
FY27 forward EPS (operator basis). Explicit year-by-year step-down:

**Base case (FY27 EPS 83):**

| Year | Growth rate | EPS (Rs) | Note |
|---|---|---|---|
| FY27 (base) | — | 83 | operator forward base (PAT 125 / 1.5152) |
| FY28 (Yr1) | +13.5% | 94 | near-term full rate (grounded PP&C rev CAGR 13-14%) |
| FY29 (Yr2) | +10.0% | 104 | fading |
| FY30 (Yr3) | +8.0% | 112 | faded to industry |

Faded 3-yr EPS CAGR = (112/83)^(1/3) - 1 = **10.5%.**

**Bear (FY27 EPS 74):** +9% -> 80.7, +8% -> 87.1, +7% -> 93.2 ~ **93.** CAGR ~7.9%.
**Bull (FY27 EPS 89):** +17% -> 104.1, +14% -> 118.7, +11% -> 131.7 ~ **132.** CAGR ~14.0%.

**Delta vs the v3.3 flat-CAGR path (the point of Amendment 14).**

| Case | v3.3 flat path FY30 EPS | v3.6 faded FY30 EPS | Delta |
|---|---|---|---|
| Bear | 96 (flat 9%) | 93 | -3 (-3.1%) |
| Base | 114 printed (implied ~11% flat; a clean flat 13% would be ~120) | 112 | -2 vs printed / -8 (-6.7%) vs clean flat 13% |
| Bull | 125 printed | 132 | +7 (bull holds growth longer, fades slower) |

The fade LOWERS the base and bear terminal EPS (the 18-Aug SOTP had already smuggled some
conservatism into its printed 114, which is why the base delta looks small against the
printed number and larger — -6.7% — against a genuine flat 13% line). The bull rises
slightly because a bull case fades from a higher near-term rate. The decision-relevant move
is the BASE and BEAR coming down, which lowers the base Hurdle Ratio.

Sanity checks: ROCE stays > 15% every year (segment 67.5% / group 36%); EPS growth is
operations-led (margin expansion off Q1 FY27 17.1% print), not financial engineering; FCF
funds growth (COMFORTABLE debt capacity, 93% headroom); Year 3 ROCE consistent with the
FIRING verdict feeding Pillar 1. SOM-implied revenue CAGR 24.3% is the upper range and
capacity-bound from Yr3 (633 Cr gap, B10); my faded 10.5% EPS base sits well below it —
**consistent, no cut needed** (my assumption is the conservative one).

Business B: cyclical, valued on normalized mid-cycle PAT ~Rs 16-18 Cr (bear ~10, base ~18,
bull ~23), no fade line (already normalized). No change to the earnings ladder.

---

## SECTION 3 — FAIR VALUES, HURDLE RATIO, ENTRY/MoS (both tracks, faded path)

### Business A — 3-year target matrix (destination 35x cap; entry = target / 1.953; MoS 20%)

| Case | FY30 EPS (faded) | Target @ 35x (Rs/sh) | Entry (Rs/sh) | MoS 20% (Rs/sh) | v3.3 target |
|---|---|---|---|---|---|
| Bear | 93 | 3,255 | 1,667 | 1,334 | 3,360 |
| Base | 112 | 3,920 | 2,007 | 1,606 | 3,990 |
| Bull | 132 | 4,620 | 2,366 | 1,893 | 4,375 |

Relative-PE lean (Amendment 15): at the low end 32.5x the base target is 32.5 x 112 =
Rs 3,640, entry Rs 1,864 — carried as the conservative shadow, given re-rating exhausted.

**Fair value today (intrinsic cross-check, FY27 forward PAT at the cap):** 35x x Rs 125 Cr
= Rs 4,375 Cr (Rs 32.5x lean = Rs 4,063 Cr). Unchanged from v3.3 on this lens (the fade
touches FY28-30, not the FY27-based today-value).

**Hurdle Ratio (faded).** HR = (1 + EPS CAGR)^3 x (Destination PE mid 35x / imputed current
PE 27x). Imputed polymer forward PE ~27x (whole 3,549 Cr minus agri ~190-250 Cr = ~3,330 Cr
/ FY27 PAT 125). Ratio 35/27 = 1.296.

- Base: (1.105)^3 x 1.296 = 1.349 x 1.296 = **1.75.** Below 1.953 -> base FAILS.
- Bull: credibility grade **C**, so the Bull row is capped at Base + 5% = 15.5% CAGR (the
  full 14% bull is below that cap anyway, but the rule sets the ceiling at 15.5%):
  (1.155)^3 x 1.296 = 1.541 x 1.296 = **2.00.** >= 1.953 -> bull PASSES (barely).

**HR verdict: CONDITIONAL** (base fails, bull passes). Flag "growth-dependent with
de-rating headwind"; verdict capped at WATCHLIST / BUY-ON-DIPS, no BUY NOW. This is the
SAME category as v3.3 but MORE marginal: the base HR fell from **1.87 to 1.75** because the
fade cut the base CAGR from 13% to 10.5%.

### Business B — value (both tracks)

| Case | Normalized PAT | Track 2 (14x base) | Track 1 (RRM 10.6x) |
|---|---|---|---|
| Bear | ~10 Cr | 12x -> 120 Cr (Rs 79/sh) | 106 Cr (Rs 70/sh) |
| Base | ~18 Cr | 14x -> 250 Cr (Rs 165/sh) | 191 Cr (Rs 126/sh) |
| Bull | ~23 Cr | 17.5x -> 400 Cr (Rs 264/sh) | 244 Cr (Rs 161/sh) |

More conservative Track 1 governs -> agri base ~Rs 191 Cr. HR fails by nature (revenue
5-6%, cyclical). **Decision AVOID** (value/monetization stub; hold small if received, sell
into an agri up-cycle).

### Combined SOTP

**Fair value today (primary, 35x cap on polymer + Track 1 agri):** 4,375 + 191 = **Rs 4,566
Cr**, ~28.6% above the Rs 3,549 Cr market cap; ~88% of value and essentially all the
upside is in the polymer business. (Relative-informed 32.5x lens: 4,063 + 191 = Rs 4,254
Cr, ~19.9% above.) Broadly unchanged from the v3.3 Rs 4,625 Cr; the fade does not move the
FY27-based today-value.

**25% entry basis (faded, where v3.6 bites):**
- Polymer base entry Rs 2,007/sh x 1.5152 = Rs 3,041 Cr.
- Agri ~Rs 191 Cr (no growth premium; ~fair value, not an entry discount).
- **Combined Tier A entry ~Rs 3,232 Cr** (= Rs 2,133/sh). Market cap Rs 3,549 Cr sits
  **~9.8% ABOVE** this (v3.3: ~6% above). CMP Rs 2,342.40 sits ~9.8% above the Rs 2,133
  combined per-share entry, and ~14.6% above the Rs 2,007 polymer-only entry top.
- **Combined MoS (20%): Rs 1,706/sh.** Evidence-scaled 30% tier (mixed evidence, catalyst
  beyond 12m on the standalone accounts, re-rating exhausted) would move it to ~Rs 1,493 —
  carried as the operator ruling item.

**Prob-weighted expected CAGR at CMP** (grade C weights 35/45/20 bear/base/bull; combined
3-yr targets per share incl. static agri ~3,334 / 4,085 / 4,884): price CAGR from 2,342.40
= 12.5% / 20.3% / 27.7%; weighted = 0.35x12.5 + 0.45x20.3 + 0.20x27.7 = **19.1%.** Below
the 25% hurdle (v3.3: 20%).

**Upside/downside:** fair value today Rs 4,566 Cr vs CMP Rs 3,549 Cr = +28.6% upside; bear
today-value ~Rs 4,026 Cr still above CMP; downside contained. Ratio ~**2.5** (v3.3: 2.6).

**Dispersion sizing:** (bull-bear)/base 3-yr = (4,884-3,334)/4,085 = 37.9% < 80% -> does not
bar sizing; the promoter CAUTION cap binds sizing at **Small**.

---

## DECISION AND v3.3 -> v3.6 DELTA

**Decision: WATCHLIST (CONDITIONAL), BUY-ON-DIPS at zone. Size Small.** Same verdict
category as the 18-Aug v3.3 B11, but the v3.6 stack makes it demonstrably MORE marginal:
the base Hurdle Ratio fell 1.87 -> 1.75, the CMP-vs-entry gap widened ~6% -> ~9.8%, and the
Market-Implied read is FAIRLY PRICED with the re-rating (the entire 30% intrinsic premium)
largely spent. The call still turns on the first standalone polymer accounts and on a
~10-15% pullback delivering the 25% entry.

**What moved and why:**

| Item | v3.3 (18-Aug) | v3.6 (this run) | What moved / why |
|---|---|---|---|
| Debt Capacity | not run | **COMFORTABLE**, 93% headroom, IMPROVING | new pre-step; removes a downside tail, no FV change (near debt-free) |
| Amdt 11 Pillar 1 base A | 30.0x (on Amdt 5 authority, 24x cap — could not produce it) | 30.0x (elite extension authority) | authority formalized; no output change, 35x cap absorbs it |
| Amdt 12 r (Business A) | r 13.5x (implicit -0.5 durability credit) | r 14.75% | Unproven band removes the durability credit (12C); +0.5 complexity added; cap absorbs -> destination still 35x |
| Amdt 12 r (Business B) | r 14.0, RRM 0.94, Track 1 13.2x | r 15.5%, RRM 0.76, **Track 1 10.6x** | cyclical +0.75 (12B cap) and complexity +0.5 now levied; flows through (no cap); agri value trimmed |
| Amdt 13 complexity | no trigger (surgical pass) | **+0.5 both entities** (dense-RPT trigger ON) | CSR 100% via promoter foundation, KMP +63.6%, Finance Committee no-independents; re-decided |
| Amdt 14 fade horizon | flat CAGR line | **explicit step-down 13.5->10->8** | base FY30 EPS 114->112 (vs clean-flat 120, -6.7%); base CAGR 13%->10.5% |
| Base Hurdle Ratio | **1.87** | **1.75** | the fade cut the base CAGR; still CONDITIONAL, more marginal |
| Bull Hurdle Ratio | 2.13 | 2.00 (grade-C bull capped at base+5%=15.5%) | still passes, thinner |
| Polymer base entry | Rs 2,043/sh | **Rs 2,007/sh** | faded terminal EPS lowered the target |
| Combined Tier A entry | ~Rs 3,345 Cr (CMP ~6% above) | **~Rs 3,232 Cr (CMP ~9.8% above)** | fade widened the CMP-to-entry gap |
| Amdt 15 relative PE | not expressed | **1.71x vs Nifty 20.5x**; re-rating MODERATE-to-NONE | destination leans to low-end 32.5x; MoS widened |
| Amdt 16 growth gate | +0x | +0x (gate satisfied, EM<25 bars anyway) | no change, stated |
| Market-Implied flag | not run | **FAIRLY PRICED** (lean PRICED-WE-ARE-LATE) | new pre-step; 30% premium is a spent re-rating bet |
| Decision | WATCHLIST | **WATCHLIST (CONDITIONAL)** | held, but weaker on every marginal metric |

**Single-credit map holds:** ROCE recovery not credited anywhere (no recovery); capital
base route NONE; cash quality priced once in Pillar 2 (12A confirms no r double-charge);
short record priced once in the Unproven band (12C); complexity priced once in r (Amdt 13);
cyclicality priced once via the capped surcharge (12B). No lever is credited twice.

**Open items carried to the operator:** (1) rule on the 30% evidence-scaled MoS tier (moves
combined MoS to ~Rs 1,493); (2) confirm the Amendment 13 dense-RPT trigger decision (this
run turns it ON; +0.5 r, absorbed by the cap for A, live for B); (3) the polymer HR uses
the imputed ~27x current PE — first standalone accounts will replace it; (4) sector/name
historical relative bands remain NOT FOUND; (5) full FTTCP v2.1 Part B (Modules B1-B8) and
Signal Gate re-run remains an open action.

---

```yaml
stage: B11-valuation-v2
company: "JUBLCPL"
run_date: "2026-08-18"
recompute_date: "2026-08-20"
model: claude-opus-4-8
status: complete
supersedes_arithmetic_of: "outputs/reports/11-valuation.md and outputs/blocks/B11-valuation.yaml (18-Aug v3.3 stack); extends the 19-Aug surgical B11-valuation-v2.yaml which held Business B verbatim and did not run the pre-steps or rebuild the fade path. Prior artifacts preserved as the audit record."
scope: "FULL v3.6 recompute per operator order: both Damodaran pre-steps run (Debt Capacity; Market-Implied vs macro-sheet.md), Amendment 14 fade horizon rebuilt year-by-year, Amendment 13 dense-RPT trigger re-decided ON, Amendment 15 relative PE computed against the market PE."
input_gaps:
  - {source: "standalone_accounts", severity: "MEDIUM", note: "no standalone accounts pre-demerger; per-entity PAT/ROCE/cash illustrative allocations"}
  - {source: "forward_guidance", severity: "MEDIUM", note: "no numeric FY27 guidance; forward EPS operator-engaged illustrative off Q1 FY27 annualized"}
  - {source: "unit_economics", severity: "HIGH", note: "no MT/kg volumes; unit-level growth validation not performed"}
  - {source: "rating_pdf", severity: "MEDIUM", note: "rating_wc_quote NOT FOUND; cash multipliers on deliberation-approved structural determination"}
  - {source: "debt_capacity_inputs", severity: "MEDIUM", note: "FY24-25 standalone EBIT and blended cost of debt NOT FOUND; conservative mid-cycle EBIT 180 Cr and 9.0% cost of debt used; verdict insensitive"}
  - {source: "relative_pe_history", severity: "LOW", note: "name and specialty-chem sector historical relative bands NOT FOUND; market PE anchored from macro-sheet"}
flags:
  - {type: "FLAG-CASH", applied_multiplier: "0.80x (Business B agri, STRUCTURAL subsidy receivable); Business A 1.15x with structural drag located in the demerging division", falsification: "retained-entity CFO:PAT <0.70x two consecutive quarters with >6m subsidy bucket >8%"}
  - {type: "SHARED-CATALYST", note: "Samlaya drives Business A revenue STARTING and ROCE FIRING; one point of failure across revenue, margin, ROCE"}
  - {type: "DEMERGER-EXECUTION", note: "scheme not yet effective; forward earnings still contain agri; per-entity PAT illustrative-allocated"}
  - {type: "CASH-CONVERSION-INDETERMINATE", note: "Business A entity CFO/PAT unconfirmable without a standalone cash statement; caps the cash read at PROCEED WITH CAVEATS with the missing evidence named"}
  - {type: "COMPLEXITY-TRIGGER-ON", note: "Amendment 13 dense-RPT trigger turned ON this run (CSR 100% via promoter foundation, KMP +63.6%, Finance Committee no independents); +0.5 r both entities; pending operator confirmation"}
  - {type: "RE-RATING-EXHAUSTED", note: "B8-proxy MODERATE-to-NONE; JACPL +58% in 5 months; the 30% intrinsic premium is a spent re-rating bet"}
framework_versions: "Master v3.6 / Section 1B v3.3+v3.5.1+v3.6 / Debt Capacity v1.0 / Market-Implied v1.0 / FTTCP verdicts held from 18-Aug gate"
pe_basis: "forward"
exit_pe_base_approved: "Business A 35x (specialty chemicals cap) / Business B 14x (normalized, agri cap 20x not binding) / Blended 29.5x (context)"
method: "SUM OF THE PARTS (operator direction 18-Aug-2026)"
earnings_perimeter: "Forward earnings still contain the agri division until the scheme is effective; per-entity PAT illustrative-allocated (no standalone accounts exist)."
debt_capacity_verdict: "COMFORTABLE (mid-cycle EBIT ~180 Cr, cost of debt 9.0% assumed, max debt 667 Cr, net debt 45 Cr, headroom 93.3%, coverage 8.93x->23.91x IMPROVING)"
market_implied_flag: "FAIRLY PRICED (leaning PRICED-WE-ARE-LATE); price implies ~15.4% EPS CAGR to be fair (25% to clear hurdle) vs ~13% evidence-supported faded; re-rating largely spent"
fade_horizon_applied: "true - EM MODEST -> fade to industry ~8% by Year 3; Business A base path FY28 +13.5% / FY29 +10% / FY30 +8%, 3yr CAGR 10.5%; base FY30 EPS 114->112 (vs clean-flat-13% 120, -6.7%); Business B cyclical/normalized, no fade"
relative_pe:
  business_a_absolute_h: 35.0
  market_pe_nifty50_ttm: 20.5
  market_pe_smallcap250: 34.4
  relative_vs_nifty: 1.71
  relative_vs_smallcap250: 1.02
  current_relative_vs_nifty: 1.36
  name_sector_historical_band: "NOT FOUND"
  b8_proxy_rerating: "MODERATE-to-NONE (+58% in 5 months already banked)"
  conclusion: "destination sits at the LOW end (32.5x) on the relative read; absolute 35x cap remains binding ceiling; MoS widened"
r_worksheet:
  business_a: "r base 14.0%; durability 0 (band Unproven, <2yr record, short-record owned per 12C, -0.5 v3.3 credit removed); governance +0.25 (Finance Committee no independents, promoter CAUTION); cyclical surcharge 0 (not cyclical, 12B N/A); complexity +0.5 (Amdt 13 dense RPT); cash-conversion r-UP none (12A); short-record r-UP none (12C); final r 14.75%; RRM 0.85; destination still 35x (cap absorbs, binds until r>15.44%)"
  business_b: "r base 14.0%; durability 0 (Moderate/Unproven, docked for cyclicality); governance +0.25; cyclical surcharge +0.75 (CAPPED per 12B, band docked for cyclicality); complexity +0.5 (Amdt 13); cash-conversion r-UP none (12A, Pillar 2 0.80x); short-record r-UP none (12C); final r 15.5%; RRM 0.76; Track 1 destination 10.6x (was 13.2x on v3.3)"
destination_pe:
  track1_rrm: {low: 32.5, mid: 35.0, high: 35.0, r_used: 14.75, rrm: 0.85}
  track2_additive: {low: 32.5, mid: 35.0, high: 35.0}
  divergence_pct: 0
  governing_track: "either; the 35x specialty-chemicals cap binds identically on both tracks and is insensitive to r below 15.44%; relative-PE lean places realized exit toward 32.5x"
pillar_detail:
  roce_used: 67.5
  roce_base: 30.0
  roce_base_authority: "Amendment 11 elite extension 24+0.3*(67.5-33)=34.35 capped 30x"
  roce_recovery_route: "not-credited"
  pillar1_normalization_route: "none"
  cash_multiplier: 1.15
  structural_or_growth: "clean-at-segment (structural FLAG-CASH drag located in demerging Business B); entity CFO/PAT INDETERMINATE"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 2
  shared_catalyst_flag: true
  ua_applied: true
  sector_cap_used: 35
  amendment_13_complexity_adj: 0.5
  amendment_13_decision: "trigger ON (dense RPT); +0.5 r both entities; absorbed by cap for A, live for B"
  amendment_16_growth_gate: "satisfied (ROCE >> min) but EM<25 bars premium; net +0x, no change"
hurdle_ratio: {base: 1.75, bull: 2.00, bull_used: true, verdict: "CONDITIONAL"}
fair_values:
  track1: {bear: 4026, base: 4566, bull: 5020}
  track2: {bear: 4080, base: 4625, bull: 5090}
businesses:
  business_a_polymer:
    destination_pe: {low: 32.5, mid: 35.0, high: 35.0}
    faded_fy30_eps: {bear: 93, base: 112, bull: 132}
    faded_3yr_eps_cagr: {bear: 7.9, base: 10.5, bull: 14.0}
    target_3yr_per_share: {bear: 3255, base: 3920, bull: 4620}
    fair_value_today_cr: 4375
    entry_range_per_share: {low: 1667, base: 2007, high: 2366}
    mos_price_per_share_20pct: 1606
    hurdle_ratio: {base: 1.75, bull: 2.00, verdict: "CONDITIONAL"}
    decision: "WATCHLIST"
  business_b_agri:
    destination_pe_track1_rrm: {low: 10.6, mid: 10.6, high: 10.6, r_used: 15.5, rrm: 0.76}
    destination_pe_track2_additive: {low: 12.0, mid: 14.0, high: 17.5}
    value_cr: {bear_t1: 106, base_t1: 191, bull_t1: 244, base_t2: 250}
    hurdle_ratio: {base: 1.09, verdict: "STOP"}
    decision: "AVOID"
combined_sotp:
  fair_value_today_cr: 4566
  fair_value_today_relative_informed_cr: 4254
  market_cap_cr: 3549
  premium_to_cmp_pct: 28.6
  tier_a_entry_cr: 3232
  tier_a_entry_per_share: 2133
  cmp_vs_entry: "market cap ~9.8% above combined Tier A entry; CMP Rs 2,342 ~9.8% above Rs 2,133/sh entry, ~14.6% above the Rs 2,007 polymer-only entry"
expected_cagr_prob_weighted: 19.1
entry_range: {low: 2007, high: 2133}
mos_price: 1706
mos_pct_applied: 20
upside_downside_ratio: 2.5
dispersion_width_pct: 37.9
dispersion_sizing_cap: "Normal from dispersion; Small binds from promoter CAUTION"
decision: "WATCHLIST (CONDITIONAL, BUY-ON-DIPS at zone; size Small)"
unresolved_inputs_used:
  - "mid-cycle EBIT Rs 180 Cr (FY24-25 EBIT NOT FOUND; conservative haircut off FY26 212.30)"
  - "cost of debt 9.0% (actual blended rate NOT FOUND; conservative G-sec+225bps)"
  - "per-entity PAT/ROCE/cash: illustrative allocations, no standalone accounts"
  - "forward FY27/FY28 PAT: operator-engaged illustrative, un-guided"
  - "name/sector historical relative PE bands NOT FOUND; market PE anchored from macro-sheet"
som_cagr_crosscheck: "consistent (faded 10.5% base sits well below the 24.3% upper-range SOM CAGR, which is capacity-bound from Yr3)"
v3.3_vs_v3.6_delta: "Decision held at WATCHLIST/CONDITIONAL but more marginal on every metric. Amdt 14 fade cut base 3yr CAGR 13%->10.5%, base FY30 EPS 114->112 (-6.7% vs clean-flat-13%), base Hurdle Ratio 1.87->1.75, polymer entry Rs 2,043->2,007, combined CMP-vs-entry gap ~6%->~9.8%. Amdt 13 dense-RPT trigger turned ON (+0.5 r both) - absorbed by the 35x cap for Business A, live for Business B. Amdt 12 removed Business A's -0.5 durability credit (Unproven band, 12C) and added Business B cyclical +0.75 (12B cap) + complexity, dropping Business B RRM track 13.2x->10.6x. Amdt 11 formalized the 30x Pillar-1 authority (no output change). Amdt 15 relative PE 1.71x with re-rating MODERATE-to-NONE places the exit at the low end. New pre-steps: Debt Capacity COMFORTABLE (no FV change), Market-Implied FAIRLY PRICED (the 30% premium is a spent re-rating bet). Business A destination PE unchanged at 35x throughout because the sector cap absorbs Amendments 11, 12 and 13; the material bite is on the projection path (fade), the hurdle ratio, and the entry gap, not the exit multiple."
one_line_thesis: "WATCHLIST JACPL at Rs 2,342 on the full v3.6 recompute: the SOTP fair value ~Rs 4,566 Cr still sits ~29% above the Rs 3,549 Cr market cap with ~88% in the retained 35x-capped polymer business, but the Amendment 14 fade cuts the base 3yr CAGR to 10.5% and the base Hurdle Ratio to 1.75 (CONDITIONAL), the Market-Implied read is FAIRLY PRICED with the +58% re-rating already banked, and CMP now sits ~9.8% above the 25% entry - the same WATCHLIST call as v3.3, weaker on every margin, still wanting a ~10-15% dip or the first standalone polymer accounts."
```
