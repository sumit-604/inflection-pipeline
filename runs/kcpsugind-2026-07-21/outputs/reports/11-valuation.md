# STAGE 11 — ROLE 1 MULTI-METHOD VALUATION (PIPELINE MODE)

**Company:** K.C.P. Sugar and Industries Corporation Ltd (KCPSUGIND)
**Run date:** 2026-07-21 | **Model:** claude-opus-4-8
**Frameworks:** Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2
**CMP:** Rs 21.71 (screener row 7) | **Market cap:** Rs 246.16 Cr (screener row 8) | **Shares (diluted):** 11.34 Cr (screener rows 39/63)

> **METHOD PRECEDENCE (operator-authoritative, fttcp-deliberation.md Override 3):**
> PRIMARY = SUM-OF-THE-PARTS. It leads. The Four-Pillar exit PE is a CROSS-CHECK
> ONLY, run on normalized *operating* trailing earnings, and is subordinate to the
> SOTP. This report leads with SOTP (Section 3-SOTP), then shows the operating
> cross-check (Section 1B) as a subordinate sanity read, exactly as the
> deliberation directs. The operator-approved pillars are used verbatim and are
> not re-derived.

---

## INTERIM CHECKPOINTS (pipeline mode — framework STOP lines written, not halted)

- *"Section 1 complete. Methods selected. Four-pillar destination PE (operating cross-check) 5.7x-6.7x additive / 6.65x-7.79x RRM. Current PE 22.2x (reported) / 86.8x (operating). Hurdle Ratio 0.37 → STOP. SOTP is the lead method; proceeding."*
- *"Section 2 complete. Projections built on segment PBITs (operating EBITDA ex-investment-income ~0.87 Cr FY26). Proceeding."*
- *"Section 3 complete. SOTP fair value Rs 10.97 / 22.50 / 33.07. Operating cross-check confirms operating equity worth ~Rs 1.5/share. Proceeding."*
- *"Valuation complete. SOTP base Rs 22.50 ≈ CMP. Operating Hurdle STOP. Entry Rs 10.24-11.52. Decision: AVOID (on valuation)."*

---

## SECTION 1A — METHOD SELECTION

KCPSUGIND is a de facto **holding company**: a Rs 332.11 Cr passive listed-equity +
mutual-fund portfolio (FVTPL Rs 292.76 Cr + cash Rs 39.35 Cr, B10 balance sheet)
sits inside an operating shell of three segments — a structurally loss-making
sugar core, a profitable Eimco-KCP engineering subsidiary, and a small urad-dal
trading business. Reported earnings are dominated by investment other income
(~Rs 28.56 Cr of the Rs 29.43 Cr reported EBITDA; operating EBITDA ex-other-income
~Rs 0.87 Cr, B10). Earnings-multiple methods on the consolidated entity are
therefore meaningless — they price investment income as if it were operating
earnings. This is textbook SOTP territory.

| Role | Method | Weight | Justification |
|---|---|---|---|
| **PRIMARY** | **Sum-of-the-Parts (NAV of investment book + going-concern operating slices)** | 70% | Holding-company structure; investment book > full market cap; segments have divergent economics that a single multiple cannot capture. Operator-mandated lead (Override 3). |
| SECONDARY | P/B (asset floor cross-check) | 20% | Trades 0.54x book (Rs 40.52 BV, B10); book is ~72% marked-to-market financial assets, so P/B is a meaningful floor lens, not just accounting. |
| CROSS-CHECK | Four-Pillar exit PE on normalized operating trailing earnings | 10% | Section 1B is the sole exit-PE authority; used to sanity-check what the *operating* business alone is worth. Subordinate to SOTP per Override 3. |

P/E, PEG, EV/EBITDA on the consolidated entity are REJECTED: PAT and EBITDA are
investment-income-inflated (B10). DCF rejected: CFO is negative (Rs -30.89 Cr, first
cash loss, CARO xvii) — no reliable forward FCF base.

---

## SECTION 1B — FOUR-PILLAR EXIT MULTIPLE (OPERATING CROSS-CHECK ONLY, SUBORDINATE)

Operator-approved pillars used verbatim (fttcp-deliberation.md "OPERATOR-APPROVED
VALUATION PILLARS", authoritative). I do not re-derive a different base.

**Pillar 1 — ROCE base**
- FTTCP ROCE forward verdict: **DECLINING (-1)** (B10; deliberation). → Pillar 1 ROCE = FY[Y+1] lower bound.
- ROCE used: **~4% reported** (operating basis 0-2%), B10 `roce_latest_pct`.
- Base PE = 0.5 × 4 + 7.5 = **9.5x**, floored at 9x → **9.5x** (Amendment 5).
- **Pillar 1 normalization route (v3.5.1): NONE.** Route A fails — no CWIP/idle-capital denominator bloat driving the low ROCE (the low ROCE is a real operating trough in sugar, not a not-yet-earning capital block). Route B fails — the verdict is DECLINING, and v3.5.1 explicitly bars invoking either route on a STAGNANT or DECLINING verdict, and there is no 📄-evidenced pre-depression high-ROCE cycle with a named unwind catalyst (the FY23-24 ROCE highs were investment income, not operating; deliberation). Statutory ROCE feeds Pillar 1 directly. Amendment 4.5 standalone is retired and NOT applied.
- **ROCE recovery credited via: not credited** (no recovery; Strategic Premium ROCE re-rating barred by the single-credit rule and by the DECLINING verdict).

**Pillar 2 — Cash conversion multiplier**
- Cumulative/latest CFO/PAT: negative — CFO Rs -30.89 Cr on PAT Rs 11.13 Cr (B10; first actual cash loss Rs 11.36 Cr per CARO xvii); FCF negative.
- Structural vs growth-induced: **STRUCTURAL.** "If growth stopped tomorrow, would WC days still be high?" YES — seasonal agri (cane) procurement is an inherent long-cash-cycle model; CARE flags cyclical/regulated sugar and lower cane availability; receivable days 31→81 (deliberation). FLAG-CASH is STRUCTURAL, not growth-induced.
- Multiplier: **0.65x** (structurally negative band). **No growth offset** (structural → 0 offset).

**Quality-adjusted base = 9.5 × 0.65 = 6.175 ≈ 6.2x**

**Pillar 3 — Growth visibility premium: +0x**
- EM score 5 (B10; deliberation), well below 25. SOM-implied revenue CAGR 9.7% 3yr / 7.5% 5yr (<20%). The Rs 257 Cr Eimco order was unfiled at run date (pending Reg 30). → +0x.

**Strategic premium: +0x** (nothing to credit; ROCE re-rating route barred).

**Undiscovered Alpha: NOT APPLIED.** Qualifiers fail — Gate 0 = 26 (<60) AND EM = 5 (<25); FII+DII UNRESOLVED. `all_met = NO`. UA withheld (B10 `ua_qualifiers`).

### Four-Pillar Summary (operating cross-check)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE ~4% → 0.5×4+7.5, floor 9x | 9.5x |
| B. Cash Multiplier (effective) | 0.65x structural + 0 offset | 0.65x |
| C. Quality-Adjusted Base | 9.5 × 0.65 | 6.175x |
| D. Growth Visibility Premium | EM 5, catalyst unfiled, SOM<20% | +0x |
| E. Strategic Premium | nothing to credit | +0x |
| F. Raw Destination PE | 6.175 + 0 + 0 | **6.2x** |
| F2. UA-Adjusted Raw PE | UA not applied → = F | 6.2x |
| G. Sector Cap | Agri processing (corrected) | 20x |
| **H. Final Destination PE (additive)** | **min(6.2, 20)** | **6.2x** |

**Track 2 (additive) destination PE range: 6.2x ±7.5% → 5.7x to 6.7x.**

### RRM dual-track (Track 1)
- Base r: small/micro 14%, adjusted **up** for weak durability, DECLINING quality, and passive-portfolio capital-allocation governance drag → **r = 15-16%** (bounded [9,18]).
- RRM = 1 + (13.5 − r) × 0.12 (percentage-points, Amendment 4.4): r=15 → 0.82; r=16 → 0.70. Mid r=15.5 → **RRM 0.76**.
- Track 1 destination PE = Fundamental base 9.5x × RRM → 9.5×0.70 = **6.65x** to 9.5×0.82 = **7.79x**, mid **7.2x**.

**Track divergence:** additive mid 6.2x vs RRM mid 7.2x = **16.1%** (>15%). The more conservative **additive (6.2x)** track governs the operating cross-check. Both tracks are subordinate to the SOTP.

### Applying the operating cross-check to NORMALIZED OPERATING trailing earnings

Reported EPS Rs 0.98 is investment-income-inflated and must not be used here (B10).
Normalized operating trailing earnings, from segment PBITs (B10):

| Operating earnings build | Rs Cr |
|---|---|
| Sugar segment PBIT | -17.31 |
| Engineering (Eimco) segment PBIT | +24.63 |
| Others (urad dal) segment PBIT | +4.21 |
| Total segment PBIT | 11.53 |
| Less interest | -7.75 |
| Operating PBT | 3.78 |
| Less tax @25% | -0.95 |
| **Normalized operating PAT** | **~2.84** |
| Operating EPS (÷11.34 Cr) | **~Rs 0.25** |

Operating equity value (operating business only, excludes investment book):
- Track 2 additive: 0.25 × 6.2x = **~Rs 1.55/share**
- Track 1 RRM: 0.25 × 7.2x = **~Rs 1.80/share**

**Read: on an earnings basis the entire operating enterprise is worth ~Rs 1.5-1.8/share.**
Everything above that in the SOTP is the investment book (asset), not operating
earnings. This is the numerical proof that the case is an asset case, not an
operating-earnings case — and why SOTP leads.

### Hurdle Ratio (operating cross-check)
HR = (1 + EPS CAGR)³ × (Destination PE mid ÷ Current PE).
- Generous basis (reported EPS 0.98 → current PE 22.2x; base operating EPS CAGR ~10%, grade C): HR = 1.331 × (6.2 ÷ 22.2) = **0.37**.
- Consistent operating basis (operating EPS 0.25 → current PE 86.8x): HR = 1.331 × (6.2 ÷ 86.8) = **0.10**.
- Bull (grade C → base +5% = 15% CAGR): 1.521 × (6.2÷22.2) = 0.42 (reported) / 0.11 (operating).

**Both bases, base and bull: HR far below 1.953 → STOP.** On operating earnings the
stock is "overvalued" because the price is supported by the asset book, not
earnings. Correct read: you are buying assets at a discount, not operating
earnings — which routes the decision to the SOTP.

---

## SECTION 2 — PROJECTIONS (segment-PBIT basis)

The operating projection is thin by design (operating earnings ~Rs 2.8 Cr). The
value driver is the balance sheet, not the P&L. Scenarios are built on the three
SOTP levers, not a single revenue CAGR.

| Lever | Bear | Base | Bull |
|---|---|---|---|
| Investment-book holdco discount | 50% | 35% | 20% |
| Eimco going-concern multiple | 6x on FY25 PAT proxy 16.56 | 8x on FY26 post-tax 18.47 | 10x on FY26 post-tax 18.47 |
| Sugar core | -Rs 25 Cr (capitalized losses) | Rs 0 (token) | +Rs 30 Cr (asset/replacement) |
| Others (urad dal) | 4x post-tax 3.16 = 12 | 6x = 19 | 7x = 22 |
| Eimco Rs 257 Cr order | not credited | credited as visibility (multiple) | executes, sustained |

**SOM cross-check:** SOTP base does not lean on an operating revenue CAGR above
B10's SOM-implied 9.7% (3yr); the only growth credited is Eimco order visibility,
consistent with SOM. → **consistent**.

### 2D Sanity checks

| Check | Result |
|---|---|
| Year-3 ROCE consistent with FTTCP DECLINING verdict? | Yes — no ROCE recovery assumed anywhere. |
| CFO/PAT trajectory consistent with 0.65x structural? | Yes — no cash-conversion improvement assumed. |
| EPS growth from operations not engineering? | N/A — value is asset-based; operating EPS held ~flat. |
| Investment book double-counted with segments? | No — cash/investments valued once; segment PPE captured via going-concern earnings, sugar assets credited only in bull. |

---

## SECTION 3 (LEAD) — SUM-OF-THE-PARTS

### (a) Investment book — Rs 332.11 Cr, holding-company discount

FVTPL Rs 292.76 Cr + cash Rs 39.35 Cr (B10, screener FY26). This is a passive
listed-equity + MF portfolio held inside an operating company.

**Holdco discount justification (typical range 20-50%; I widen toward the high end):**
1. The operating shell is **burning cash** (CFO Rs -30.89 Cr; first actual cash loss; sugar losing Rs 17.31 Cr/yr and widening) — the investment book is actively at risk of being consumed to fund sugar losses. It is a leaking container, not a ring-fenced fund.
2. **Mark-to-market risk** on Rs 292.76 Cr of listed equity/MF (devil's-advocate stress point, deliberation).
3. Minority holders cannot access or force distribution; **capital-gains tax** on realization.
4. **Capital-allocation drag**: promoter holds a large passive portfolio inside an operating company rather than distributing it.

| | Bear (50%) | Base (35%) | Bull (20%) |
|---|---|---|---|
| Investment book value (Rs Cr) | 166.06 | 215.87 | 265.69 |

### (b) Eimco-KCP engineering — going concern, 100% subsidiary

FY26 segment revenue Rs 78.64 Cr, segment PBIT Rs 24.63 Cr (31.3% margin), FY25 PAT
proxy Rs 16.56 Cr (B10). Post-tax FY26 ~Rs 18.47 Cr (24.63 × 0.75). The
operator-confirmed **Rs 257 Cr Hyundai Reactor-Clarifier order** (released 20-21 Jul
2026, ~3.3x segment revenue) is credited as **revenue visibility via a higher
going-concern multiple**, NOT via inflated earnings — and flagged **pending Reg 30
filing**.

| | Bear | Base | Bull |
|---|---|---|---|
| Multiple | 6x | 8x | 10x |
| Earnings (Rs Cr) | 16.56 (FY25 proxy) | 18.47 | 18.47 |
| Eimco value (Rs Cr) | 99 | 148 | 185 |

Multiples are conservative for a 30%+ margin engineering franchise (Engineering
services sector cap is 25x); the lumpy, order-driven nature and single-order
concentration justify the discipline.

### (c) Sugar core + others

- **Sugar** (PBIT -Rs 17.31 Cr, structurally widening): on an operating basis its value is **negative** (a discounted stream of losses); it holds mill + land assets with replacement/liquidation value. Bear = -Rs 25 Cr (≈1.5 years of losses before restructuring/closure); Base = Rs 0 (token; asset backing offsets near-term loss run-rate); Bull = +Rs 30 Cr (partial asset/replacement credit, losses stanched).
- **Others / urad dal** (PBIT +Rs 4.21 Cr → post-tax 3.16): 4x/6x/7x → Rs 12 / 19 / 22 Cr.

| Core (sugar + others) | Bear | Base | Bull |
|---|---|---|---|
| Value (Rs Cr) | -13 | 19 | 52 |

### (d) Net out borrowings and per-share

Total borrowings Rs 127.71 Cr (B10), all cases. ÷ 11.34 Cr shares.

| SOTP build (Rs Cr) | Bear | Base | Bull |
|---|---|---|---|
| (a) Investment book | 166.06 | 215.87 | 265.69 |
| (b) Eimco | 99.00 | 148.00 | 185.00 |
| (c) Sugar + others | -13.00 | 19.00 | 52.00 |
| (d) Less: total borrowings | -127.71 | -127.71 | -127.71 |
| **Equity value** | **124.35** | **255.16** | **374.98** |
| **÷ 11.34 Cr shares → per share** | **Rs 10.97** | **Rs 22.50** | **Rs 33.07** |

**SOTP fair value: Bear Rs 10.97 | Base Rs 22.50 | Bull Rs 33.07.**

Internal consistency: base SOTP equity Rs 255 Cr ≈ market cap Rs 246 Cr — the market
already prices the equity at roughly the base asset case. The 0.54x book optics
are explained by the justified holdco discount + cash burn + sugar losses, not by a
mispricing.

### Secondary cross-check — P/B
Book value Rs 40.52/share; the book is ~72% marked financial assets. A holdco P/B of
0.50-0.55x on Rs 40.52 = Rs 20.3-22.3 — brackets the base SOTP Rs 22.50 and CMP.
Consistent: the asset floor is roughly where the stock trades.

---

## SECTION 4 — TRIANGULATION, ENTRY, VERDICT

### 4A Governing fair value
SOTP is the governing method (Override 3). Because the dominant slice (the
investment book) is a direct NAV, not a PE multiple, the RRM/additive distinction
lives only in the tiny ~Rs 1.5-1.8/share operating cross-check and does not move the
SOTP. Both tracks in the verdict card therefore carry the SOTP; the operating
cross-check is reported alongside as subordinate.

| Fair value (Year-3 realization target) | Bear | Base | Bull |
|---|---|---|---|
| SOTP (governing) | Rs 10.97 | Rs 22.50 | Rs 33.07 |

### 4C / 4D Return expectation at CMP Rs 21.71 (grade C weights: 35/45/20)

| Scenario | SOTP FV | 3-yr CAGR from CMP | Prob | Weighted |
|---|---|---|---|---|
| Bear | 10.97 | -20.3% | 35% | -7.11% |
| Base | 22.50 | +1.2% | 45% | +0.54% |
| Bull | 33.07 | +15.1% | 20% | +3.01% |
| **Expected CAGR** | | | 100% | **-3.6%** |

Probability-weighted expected CAGR is **negative** at Rs 21.71. The stock does not
clear — or come near — the 25% hurdle on the asset case.

### 4E Entry price (Tier A, hurdle 25% — Tier B BARRED)

**Tier: A | Hurdle: 25%.** Tier B is barred: FLAG-CASH is STRUCTURAL (v3.4 Amendment
4.3 Tier-B gate "no structural FLAG-CASH" fails), and Gate 0 = 26 (not GOOD). So the
25% hurdle stands.

| Calculation | Value |
|---|---|
| Base SOTP fair value | Rs 22.50 |
| 25% CAGR entry = 22.50 ÷ 1.953 | **Rs 11.52** |
| 30% CAGR entry (extra safety) = 22.50 ÷ 2.197 | Rs 10.24 |
| MoS price (20% below 25% entry) | **Rs 9.22** |
| **Ideal entry range** | **Rs 10.24 - Rs 11.52** |

CMP Rs 21.71 is ~88% above the top of the entry zone. Even on the **bull** SOTP the
25% entry is Rs 33.07 ÷ 1.953 = Rs 16.93 — still below CMP. The stock offers no 25%
entry at Rs 21.71 on any SOTP scenario.

### 4F Risk-reward asymmetry

| | Value |
|---|---|
| Bull target Rs 33.07 → upside from CMP | +52.3% |
| Base target Rs 22.50 → upside from CMP | +3.6% |
| Bear floor Rs 10.97 → downside from CMP | -49.5% |
| Upside(base) / Downside(bear) — framework 4F definition | **0.07x** |
| Upside(bull) / Downside(bear) — asymmetry read | **1.06x** |

Both are far below the 2x minimum. Downside (asset erosion via cash burn + MTM)
roughly equals the entire upside. Unfavourable.

### 4G Four-Pillar validation
- Year-3 ROCE justifies base used? Yes — no recovery credited (DECLINING).
- CFO/PAT justifies 0.65x? Yes — structural, no improvement assumed.
- Catalyst fired by Year 3 (base)? Eimco order credited only as visibility; pending Reg 30.
- Strategic premium at Year 3 (single-credit)? +0x, respected.
- UA ordering min(F×1.25, Cap)? UA not applied — correct.
- Would you pay 6.2x for this operating quality? For the operating business alone, yes and it is still worth only ~Rs 1.5/share; the case is the asset book.

### 4H — VALUATION VERDICT CARD

**Tier: A | Hurdle: 25% | Earnings basis: TRAILING (operator-approved)**

- **CMP** Rs 21.71 | **Market cap** Rs 246.16 Cr | **Book value** Rs 40.52 (0.54x P/B)
- **PRIMARY METHOD: SUM-OF-THE-PARTS (lead).** Base fair value **Rs 22.50** (Bear 10.97 / Bull 33.07). Investment book Rs 332.11 Cr at 35% holdco discount (base); Eimco Rs 148 Cr going concern with Rs 257 Cr order as visibility (pending Reg 30); sugar core token Rs 0; others Rs 19 Cr; less borrowings Rs 127.71 Cr.
- **OPERATING CROSS-CHECK (subordinate):** Four-Pillar destination PE — ROCE base 9.5x (FTTCP DECLINING, ROCE ~4%, v3.5.1 route NONE, recovery not credited) × cash 0.65x (STRUCTURAL, FLAG-CASH) = 6.2x quality base + 0 growth + 0 strategic = **Raw 6.2x**; UA not applied; sector cap Agri processing 20x (not binding). **Destination PE: additive 5.7-6.7x (mid 6.2x); RRM 6.65-7.79x (mid 7.2x, r 15.5%, RRM 0.76); divergence 16.1%, additive governs.** Applied to normalized operating trailing EPS ~Rs 0.25 → operating business worth **~Rs 1.5-1.8/share**.
- **HURDLE RATIO (operating cross-check): 0.37 (reported basis) / 0.10 (operating basis) → STOP.** Bull also STOPs. 25% CAGR infeasible on operating earnings at CMP.
- **EXPECTED CAGR (prob-weighted, grade C): -3.6%.**
- **UPSIDE/DOWNSIDE: 0.07x (base/bear) / 1.06x (bull/bear)** — both below 2x.
- **ENTRY RANGE Rs 10.24 - Rs 11.52 | MoS Rs 9.22.**
- **DECISION: AVOID (on valuation) at Rs 21.71.** WATCHLIST the asset case; becomes a BUY-candidate only near Rs 10-12 (buying the Rs 332 Cr investment book at a deep discount with Eimco optionality quasi-free).

**Decision reconciliation (SOTP asset floor vs declining operating business):**
The SOTP asset floor does NOT create a buy at Rs 21.71 because the market already
prices the equity at the base SOTP (Rs 255 Cr equity ≈ Rs 246 Cr cap). Below that
floor sits a business whose sugar core is shrinking and cash-negative (FLAG-CASH
STRUCTURAL), whose operating earnings justify only ~Rs 1.5/share, whose operating
Hurdle STOPs, and whose FTTCP verdict is DEEP WATCH leaning AVOID with the Kernex
cash cap binding. Upside/downside is <2x and expected CAGR is negative. Every lens
converges on **AVOID-on-valuation** at CMP, with a defined asset-case re-open zone at
Rs 10-12. The Eimco Rs 257 Cr order is the live optionality that would move the base
SOTP up once filed (Reg 30) and executed — a monitor item, not a reason to pay up now.

**KEY ASSUMPTIONS THAT MOVE THE VALUATION**
- ▲ Eimco order fills (Reg 30 confirms) and margin holds → base Eimco multiple/earnings rise, base SOTP toward Rs 25-28.
- ▲ Holdco discount narrows (buyback/dividend of the portfolio, or cash burn stops) → base toward bull.
- ▼ Sugar losses widen / consume the investment book (cash burn continues) → bear discount 50% realized, SOTP toward Rs 11.
- ▼ MTM drawdown on the Rs 292.76 Cr FVTPL portfolio.

**EXIT / THESIS-BROKEN (for the asset case, if entered near zone):** exit toward base
SOTP; thesis broken if investment book is drawn down >20% to fund operating losses,
or Eimco order is cancelled/not filed, or sugar losses exceed Rs 25 Cr/yr.

**ONE-LINE THESIS:** Not a buy at Rs 21.71 — the market already pays the base SOTP
(Rs 22.50); the Rs 332 Cr investment book plus Eimco (Rs 148 Cr, Rs 257 Cr order
pending Reg 30) net of Rs 128 Cr debt is only worth owning near Rs 10-12, against a
cash-burning, structurally loss-making sugar core; AVOID-on-valuation, WATCHLIST the
asset case.

---

```yaml
stage: B11-valuation
company: "KCPSUGIND"
run_date: "2026-07-21"
model: claude-opus-4-8
status: complete
input_gaps:
  - "FII+DII institutional shareholding % UNRESOLVED (B10); did not affect UA (already withheld on Gate0/EM) or Tier (barred by structural FLAG-CASH)"
  - "Eimco-KCP FY26 standalone margins/audit-trail not extractable; FY25 PAT Rs 16.56 Cr used as conservative bear earnings proxy"
  - "Eimco Rs 257 Cr Hyundai order pending Reg 30 filing; credited as revenue visibility only, not as base-case earnings"
flags:
  - "FLAG-CASH: STRUCTURAL. Pillar 2 multiplier 0.65x APPLIED, no growth offset. Bars Tier B; caps operating verdict."
  - "EIMCO ORDER pending Reg 30 (operator-confirmed, released 20-21 Jul 2026); base credits it as visibility via multiple, not earnings"
  - "SUGAR segment PBIT -17.31 Cr, structurally widening; valued token/negative in SOTP"
  - "SOTP-LEAD per operator Override 3; Four-Pillar exit PE is subordinate operating cross-check only"
  - "Reported EBITDA/PAT investment-income-inflated (~28.56 Cr); operating read on segment PBITs, operating EPS ~Rs 0.25"
framework_versions: "Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2"
pe_basis: "trailing"
exit_pe_base_approved: "Pillar 1 base 9.5x at 9x floor; destination ~6x additive / ~7x RRM on normalized operating trailing earnings (operating cross-check only; SOTP leads, investment book valued direct)"
destination_pe:
  track1_rrm: {low: 6.65, mid: 7.2, high: 7.79, r_used: 15.5, rrm: 0.76}
  track2_additive: {low: 5.7, mid: 6.2, high: 6.7}
  divergence_pct: 16.1
  governing_track: "SOTP governs the entry zone; within the subordinate operating cross-check, additive (6.2x) is the more conservative track"
pillar_detail:
  roce_used: 4
  roce_base: 4
  roce_recovery_route: "not-credited"
  pillar1_normalization_route: "none"
  cash_multiplier: 0.65
  structural_or_growth: "structural"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 0
  shared_catalyst_flag: false
  ua_applied: false
  sector_cap_used: 20
hurdle_ratio: {base: 0.37, bull_used: false, verdict: "STOP"}
fair_values:
  track1: {bear: 10.97, base: 22.50, bull: 33.07}
  track2: {bear: 10.97, base: 22.50, bull: 33.07}
expected_cagr_prob_weighted: -3.6
entry_range: {low: 10.24, high: 11.52}
mos_price: 9.22
upside_downside_ratio: 1.06
decision: "AVOID (on-valuation) at CMP Rs 21.71; WATCHLIST asset case, re-open zone Rs 10-12"
unresolved_inputs_used:
  - "Eimco FY26 standalone earnings: conservative assumption Rs 16.56 Cr FY25 PAT proxy for bear; FY26 post-tax 18.47 Cr (from segment PBIT 24.63 x 0.75) for base/bull, because standalone audit-trail not extractable (B10)"
  - "Ethanol/Alcohol FY26 revenue not separately disclosed; subsumed in sugar/others segments, not separately valued, per B10 proxy note"
som_cagr_crosscheck: "consistent"
one_line_thesis: "Not a buy at Rs 21.71 — market already pays the base SOTP Rs 22.50; the Rs 332 Cr investment book plus Eimco (Rs 148 Cr, Rs 257 Cr order pending Reg 30) net of Rs 128 Cr debt is only worth owning near Rs 10-12 against a cash-burning, structurally loss-making sugar core; AVOID-on-valuation, WATCHLIST the asset case."
```
