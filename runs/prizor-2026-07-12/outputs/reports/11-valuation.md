# STAGE 11 — ROLE 1 DUAL-TRACK VALUATION: PRIZOR VIZTECH LTD

**Run date:** 2026-07-12 | **Model:** claude-opus-4-8 | **Framework:** Master v3.3 / Section 1B v3.3 (Amendments 1-8, 4.1-4.4) / FTTCP v1.2
**Input source:** B10-valinputs (sole input table). Exit-multiple authority: Section 1B v3.3 ONLY.

**Tier: A | Hurdle: 25%** (assigned mechanically — see two-tier check in Section 1B)

---

## PIPELINE-MODE CHECKPOINT LINE (interim states written, no stops)

Interim after Section 1B: "Four-pillar destination PE = 14.0x-16.0x (Track 2 additive, mid 15.0x); RRM track 15.0x-17.5x (mid 16.2x). Current PE 86.9x (FY25 audited EPS). Hurdle Ratio (base) 0.23 -> STOP. Proceeding through all sections for the record."

---

## SECTION 1A — METHOD SELECTION

Business model: hybrid trading + manufacturing, video surveillance / security electronics. Asset base ramping (installed capacity ~5.5% utilised), leverage present (net debt Rs 7.389 Cr), earnings distorted by IPO-year effects and negative cash conversion.

| Role | Method | Weight | Justification |
| --- | --- | --- | --- |
| PRIMARY | EV/EBITDA | 50% | Capital-intensive hybrid with rising leverage and varying capital structure; neutralises the debt-funded capex ramp. Per B10 primary_method. |
| SECONDARY | EV/Sales | 30% | Margins contested vs peer (CP Plus 13.7% EBITDA vs claimed 21-23%); EV/Sales cross-checks the margin assumption independently. Per B10 secondary_method. |
| TERTIARY | P/E | 20% | Sanity-check only. Earnings clean-ish but PAT quality undermined by CFO/PAT -1.02x cumulative. Per B10 tertiary_method. |

DCF rejected: negative FCF (-22.371 Cr FY25), <3 years history, structural WC drag — DCF would be pure terminal-value fiction. P/B rejected: not a lender. Peer multiples (P/E, EV/EBITDA medians) NOT FOUND (only CP Plus as direct peer) — external anchoring unavailable; exit multiples come solely from Section 1B.

---

## SECTION 1B — FOUR-PILLAR EXIT MULTIPLE (Section 1B v3.3, SOLE authority)

### Pillar 1 — ROCE Base Multiple (continuous formula, Amendment 5)

- **FTTCP ROCE forward verdict: STAGNANT** (B10 fttcp_authoritative, deliberation-confirmed).
- Per the FTTCP v1.2 Pillar 1 integration table: **STAGNANT -> Pillar 1 uses CURRENT ROCE.**
- Current audited ROCE = **FY25 31.29%** (AR Note 32). FY26 ROCE is unaudited and internally inconsistent (37.2% vs 47.4%, FLAG-INTERNAL-ROCE-INCONSISTENCY) — **NOT used.**
- ROCE 31.29% <= 33%, so: **Base PE = 0.5 x 31.29 + 7.5 = 15.645 + 7.5 = 23.145 -> 23.1x** (floor 9x / cap 24x not binding).
- **ROCE recovery credited via: NOT CREDITED** (STAGNANT verdict = no forward uplift enters Pillar 1). Single-credit rule: therefore NO Strategic Premium ROCE re-rating either (explicitly barred by deliberation and by FLAG-FORWARD-ROCE-DILUTION, which projects mechanical ROCE compression).

**Pillar 1 ROCE Base = 23.1x**

### Pillar 2 — Cash Conversion Multiplier

- Cumulative CFO/PAT: **-1.02x** | Latest FY CFO/PAT: **-1.39x** | FCF positive? **No** (FCF -22.371 Cr, FCF/PAT -2.20x).
- Cash quality band: CFO negative both years and deteriorating -> band is either "CFO negative (growth-phase drag)" 0.80x OR "Structurally negative" 0.65x.
- Determination (B10, deliberation-confirmed): **INDETERMINATE, leaning structural.** Rating agency WC quote **NOT FOUND** (no rating PDF).
- **Wrapper/framework rule for INDETERMINATE: use the MORE CONSERVATIVE multiplier and say so.** Cumulative CFO/PAT is not merely <30% but deeply negative (-1.02x), and the determination leans structural. Conservative default = **0.65x.**
  - *INPUT UNRESOLVED: rating_wc_quote. Conservative assumption used: 0.65x structural multiplier, because INDETERMINATE-leaning-structural + framework conservative-default rule + absent rating confirmation. (If one insisted on growth-induced treatment, 0.80x with +0.05 offset would give ~0.85x and a raw PE ~19.7x; conservative bias and the leaning-structural determination reject this.)*
- Structural or growth-induced? **INDETERMINATE leaning structural** -> **NO growth offset** (structural row = 0 offset). growth_offset = 0.
- **Effective Cash Multiplier = 0.65x**

**Quality-Adjusted Base = 23.145 x 0.65 = 15.04 -> 15.0x**

### Pillar 3 — Growth Visibility Premium (decoupled 3a/3b/3c, Amendment 4.1-4.2, combined +6x cap)

**3a Growth Visibility (documented machinery, grade C caps at +2x):**
- capex-embedded growth >=15%: itemised FY26 capex NOT FOUND; installed capacity vastly exceeds SOM (~5.5% utilisation) -> capex is NOT translating to embedded near-term growth. Fails.
- order book >=1.0x revenue / book-to-bill >=1.2x: **NOT FOUND** (no order book). Fails.
- SOM-implied revenue CAGR >=20%: SOM-implied is **16-17%** (3yr 17.0%, 5yr 15.9%), below 20%. Fails.
- management delivery grade A/B: grade is **C**. Fails.
- Fewer than two qualify -> **3a = +0x**

**3b Moat Formation (EM-gated table):** EM score **13.6** (MODEST), which is below 25 -> **3b = +0x**

**3c Duration Premium (documented forward visibility >=2.5yr):** no signed contracts / LoAs / order book documented -> **3c = +0x**

**Pillar 3 total = +0x**

### Strategic Asset Premium

- Rare licence / regulatory monopoly? No. Strong brand with documented pricing power? No (FLAG-MARGIN-PEER-CONTRADICTED — margins run above the only direct peer and are unexplained). ROCE re-rating optionality? Barred by single-credit rule AND no genuine optionality (STAGNANT + FLAG-FORWARD-ROCE-DILUTION). Institutional turnaround backing? No.
- **Strategic Premium = +0x**

### Undiscovered Alpha Multiplier (Amendment 3)

- listed_12m: TRUE | gate0_or_em: TRUE | **fii_dii_lt3: NOT FOUND (null, unverified)**.
- All three qualifiers must be evidenced. The third cannot be confirmed (aggregator sites 403). **UA NOT APPLIED.** F2 = F.
  - *Conditional note: IF fii_dii_lt3 were later confirmed <3%, UA would give F x 1.25 = 18.8x raw, still min() with 25x cap -> 18.8x. Default per instruction: NOT applied.*

### Sector Reality Cap

- **Sector cap row: Manufacturing / Industrial products = 25x** (B10 authoritative). Manifest "Pharma / CDMO" 38x is **REJECTED.** No quality uplift (UA not triggered). **Cap = 25x (absolute).**

### Four-Pillar Summary (Track 2 additive)

| Step | Calculation | Value |
| --- | --- | --- |
| A. ROCE Base | 31.29% -> 0.5x+7.5 | 23.1x |
| B. Cash Multiplier (effective) | 0.65x + 0 offset | 0.65x |
| C. Quality-Adjusted Base | 23.145 x 0.65 | 15.0x |
| D. Growth Visibility Premium (3a+3b+3c) | 0+0+0 | +0x |
| E. Strategic Premium | none | +0x |
| F. Raw Destination PE | C+D+E | 15.0x |
| F2. UA-Adjusted Raw PE | UA not applied -> F | 15.0x |
| G. Sector Cap | Manufacturing/Industrial | 25x |
| **H. Final Destination PE** | **min(F2, G) = min(15.0, 25)** | **15.0x** |

**Track 2 Destination PE Range: 15.0 +/-7.5% = 13.875 to 16.125 -> rounded 14.0x to 16.0x (mid 15.0x)**

### RRM Dual-Track Derivation (Track 1)

- Fundamental Base PE = Pillar 1 ROCE base = 23.1x (durability/governance flow through r, not additive points).
- Base r (small/micro) = 14%. Adjustments UP for weak governance and durability: FLAG-RPT-UNRECONCILED (HIGH, Rs3.00cr loan-to-equity unreconciled), FLAG-DISCLOSURE-QUALITY, FLAG-GATE0-DEAL-BREAKER (AVERAGE), structural cash negativity, no-concall mode. **r used = 16%** (conservative; any r>=16% floors the RRM identically). Bounded [9%,18%] — within.
- **RRM = 1 + (13.5 - 16) x 0.12 = 1 + (-2.5)(0.12) = 1 - 0.30 = 0.70** (percentage-point reading, Amendment 4.4; at/against the 0.70 floor).
- **Track 1 Destination PE = 23.1 x 0.70 = 16.17 -> 16.2x** (capped at 25x — not binding).
- **Track 1 Range: 16.2 +/-7.5% = 14.98 to 17.4 -> 15.0x to 17.5x (mid 16.2x)**

### Track divergence

- Track 1 mid 16.2x vs Track 2 mid 15.0x -> divergence = 1.2/15.0 = **8.0%** (<15%, tracks agree).
- **Governing track = Track 2 (additive), the more conservative -> sets the entry zone.**

### Two-Tier Hurdle assignment (Amendment 4.3)

- Tier B requires ALL of: FII+DII >=3% AND Gate0 GOOD+ AND promoter TRUSTWORTHY AND no structural FLAG-CASH. Here: FII+DII NOT FOUND (cannot confirm >=3%), Gate0 AVERAGE, structural FLAG-CASH present -> Tier B **fails.**
- **Tier A applies. Hurdle 25%. HR pass threshold 1.953.**

### HURDLE RATIO (Amendment 2)

- Current PE = CMP / FY25 diluted EPS = 825 / 9.495 = **86.9x** (FY25 audited; FY26 unaudited excluded per instruction — even on FY26 unaudited EPS ~19.42, current PE ~42.5x, still far above destination).
- Base EPS CAGR (from Section 2 projections) = **10.5%**. Grade C -> Bull row uses Base + 5% = **15.5%** max (genuine bull EPS CAGR not usable, grade C).
- **HR(Base) = (1.105)^3 x (15.0 / 86.9) = 1.3492 x 0.1726 = 0.23**
- **HR(Bull, 15.5%) = (1.155)^3 x (15.0 / 86.9) = 1.5407 x 0.1726 = 0.27**
- Both << 1.953. **HURDLE VERDICT = STOP.** Overvalued; 25% CAGR is infeasible even on bull-case earnings. Complete remaining sections for the record; verdict card = AVOID-on-valuation.

*Would I personally pay 15x for this quality of business? Yes — 15x is a fair destination for a 31% ROCE / structurally cash-negative / grade-C micro-cap. The problem is not the destination; it is that the market already prices 87x.*

---

## SECTION 2 — PROJECTIONS (Year 0 = FY25 audited; conservative bias)

### 2A/2B Assumptions

| Assumption | Bear | Base | Bull |
| --- | --- | --- | --- |
| Revenue CAGR | 8% | 14% | 18% |
| Revenue logic | share loss / dealer churn; peer-margin reality bites | scaling below SOM ceiling | dealer network + BIS tailwind execute |
| EBITDA margin | 15% (toward CP Plus 13.7%) | 18% (partial compression from 21.42%) | 21% (sustain near current) |
| PAT margin | 9% (interest + D&A drag) | 13% | 15% |
| Dilution | assume none (conservative on count) | none | none |

SOM cross-check: base revenue CAGR 14% < SOM-implied ceiling 17% -> **CONSISTENT.** (FY26 unaudited ~99% growth is NOT used to set base; SOM ceiling and structural cash negativity govern.)

### 2C Projection table (Base case, Year 0 = FY25)

| Line | Y0 (FY25) | Y3 (Base) |
| --- | --- | --- |
| Revenue (Cr) | 70.98 | 105.2 |
| EBITDA (Cr) | 15.077 (21.42%) | 18.9 (18%) |
| PAT (Cr) | 10.15 (14.29%) | 13.68 (13%) |
| EPS (Rs, diluted) | 9.495 | 12.79 |

Bear Y3: Rev 89.4, EBITDA 13.4, PAT 8.05, EPS 7.53. Bull Y3: Rev 116.6, EBITDA 24.5, PAT 17.49, EPS 16.36.

EPS CAGR: Bear (7.53/9.495)^(1/3)-1 = **-7.4%** | Base (12.79/9.495)^(1/3)-1 = **10.5%** | Bull (16.36/9.495)^(1/3)-1 = **19.9%** (Bull EPS CAGR capped to 15.5% only inside the HR check per grade C).

### 2D Sanity checks

| Check | Result | Pass |
| --- | --- | --- |
| Revenue faster than capacity? | No — capacity vastly under-utilised (~5.5%) | Yes |
| Margins require unprecedented? | Base compresses toward peer; conservative | Yes |
| ROCE >15%? | Yes (~20-25% range on ramp) but FLAG mechanical compression | Caveat |
| FCF funds growth w/o excess debt? | No — negative CFO, debt-funded (FLAG-CASH) | **No** |
| EPS growth operational? | Yes (topline-led), but cash quality undermines | Caveat |
| Implied share gain realistic? | Base within SOM ceiling | Yes |
| CFO/PAT trajectory consistent w/ Pillar 2 (0.65x)? | Yes — no assumed cash-conversion miracle | Yes |
| Y3 ROCE consistent with FTTCP STAGNANT? | Yes — no forward ROCE uplift credited | Yes |

---

## SECTION 3 — METHOD APPLICATION (Year 3 targets)

Forward net debt (scenario assumptions, flagged; conclusion is insensitive to these — CMP-implied EV ~Rs 889 Cr dwarfs all method EVs): Bear 45 Cr, Base 25 Cr, Bull 10 Cr.

### EV/EBITDA (PRIMARY, 50%)
Exit EV/EBITDA derived from Section 1B PE via PAT/EBITDA ratio (0.673) and equity/EV (~0.98): ~9.9x theoretical, discounted to **9.5x mid (band 8.5x-10.5x)** because forward capex >> depreciation will inflate future D&A (EBITDA overstates cash earnings).

| | Bear (8.5x) | Base (9.5x) | Bull (10.5x) |
| --- | --- | --- | --- |
| EV (Cr) | 13.4x8.5=113.9 | 18.9x9.5=179.6 | 24.5x10.5=257.3 |
| less Net Debt | 45 | 25 | 10 |
| Equity (Cr) | 68.9 | 154.6 | 247.3 |
| /1.069 Cr sh | **Rs 64** | **Rs 145** | **Rs 231** |

### EV/Sales (SECONDARY, 30%)
Exit EV/Sales = EV/EBITDA x margin: ~1.4x bear / 1.7x base / 2.0x bull.
Bear 89.4x1.4-45=80/1.069=**Rs 75** | Base 105.2x1.7-25=153.8/1.069=**Rs 144** | Bull 116.6x2.0-10=223/1.069=**Rs 209**

### P/E (TERTIARY, 20%)
Exit PE from Section 1B: 14x bear / 15x base / 16x bull (Track 2 range).
Bear 7.53x14=**Rs 105** | Base 12.79x15=**Rs 192** | Bull 16.36x16=**Rs 262**

---

## SECTION 4 — TRIANGULATION, ENTRY, VERDICT

### 4A Triangulated fair value (Track 2, governing)

| | Bear | Base | Bull |
| --- | --- | --- | --- |
| EV/EBITDA x0.50 | 64x.5=32.0 | 145x.5=72.3 | 231x.5=115.7 |
| EV/Sales x0.30 | 75x.3=22.5 | 144x.3=43.2 | 209x.3=62.7 |
| P/E x0.20 | 105x.2=21.0 | 192x.2=38.4 | 262x.2=52.4 |
| **Weighted FV** | **Rs 76** | **Rs 154** | **Rs 231** |

**Track 1 (RRM, ~x1.09 on higher 16.2x destination): Bear ~Rs 84, Base ~Rs 170, Bull ~Rs 253.** Governing = Track 2 (lower).

### 4B Methods agreement
All three methods point the same direction (deep downside from CMP). Spread base Rs 144-192 = ~30%, P/E the high outlier (destination PE 15x on clean EPS ignores cash quality); EV/EBITDA most trusted for this leveraged, cash-negative ramp. All methods land Rs 145-192 base vs CMP 825.

### 4C Return at current price (Year 3 vs CMP 825)

| Scenario | FV Y3 | Total Return | CAGR | 25% hurdle |
| --- | --- | --- | --- | --- |
| Bear | 76 | -91% | -54.9% | red |
| Base | 154 | -81% | -42.8% | red |
| Bull | 231 | -72% | -34.6% | red |

### 4D Probability-weighted expected return (Grade C: 35/45/20)

| Scenario | Prob | 3yr CAGR | Weighted |
| --- | --- | --- | --- |
| Bear | 35% | -54.9% | -19.2% |
| Base | 45% | -42.8% | -19.3% |
| Bull | 20% | -34.6% | -6.9% |
| **Expected CAGR** | 100% | | **-45.4%** |

### 4E Entry price (Tier A, divisor 1.953)
- Base FV (Y3) = Rs 154. **Entry = 154 / 1.953 = Rs 79.** 30% CAGR entry = 154/2.197 = Rs 70. **MoS price (20% below entry) = Rs 63.**
- **Ideal entry range: Rs 63 (MoS) to Rs 79 (entry).** CMP 825 is ~10.4x the entry ceiling.

### 4F Risk-reward asymmetry
Bull Y3 231 (-72%), Base 154 (-81%), Bear 76 (-91%). **No scenario exceeds CMP — risk-reward is downside-only. Upside/downside ratio not meaningful (reported 0.0); fails the >=2x test outright.**

### 4G Four-pillar validation
Year 3 ROCE consistent with STAGNANT (no uplift credited) — pass. Year 3 CFO/PAT does not assume a cash miracle (0.65x held) — pass. Primary catalyst (FY26 audited AR) unfired at valuation date — noted. Strategic premium correctly zero (single-credit) — pass. UA ordering min(F x1.25, cap) correctly NOT triggered — pass. Would I buy a different stock at 15x with these Y3 metrics? Yes — 15x is fair; the stock's problem is the 87x entry, not the destination.

### 4H VERDICT CARD

**Tier: A | Hurdle: 25%**
- CMP Rs 825 | Market cap Rs 891 Cr (B10; note per-share math uses 825 x 1.069 = Rs 882 Cr, minor input inconsistency, immaterial) | EV Rs 898 Cr | 1.069 Cr shares.
- **FOUR-PILLAR EXIT PE:** ROCE base 23.1x (FTTCP STAGNANT, ROCE 31.29% current) x cash 0.65x (INDETERMINATE-leaning-structural, conservative) = QA base 15.0x; Growth +0x (3a0/3b0/3c0, EM 13.6, grade C); Strategic +0x (single-credit); Raw 15.0x; UA NOT applied (fii_dii_lt3 unverified); sector cap 25x (Manufacturing/Industrial, absolute; no uplift). **DESTINATION PE 14.0x-16.0x (mid 15.0x).**
- **RRM TRACK:** r 16%, RRM 0.70 (floor), destination 15.0x-17.5x (mid 16.2x); FV bear/base/bull Rs 84/170/253.
- **HURDLE RATIO:** base 0.23, bull 0.27 -> **STOP.**
- **METHODS:** EV/EBITDA 50% / EV/Sales 30% / P/E 20%.
- **WEIGHTED FV (Y3) Track 2:** Bear Rs 76 | Base Rs 154 | Bull Rs 231. **Track 1:** Rs 84 / 170 / 253.
- **EXPECTED CAGR (prob-weighted, Grade C 35/45/20): -45.4%.**
- **UPSIDE/DOWNSIDE: downside-only (0.0x).**
- **ENTRY Rs 63-79 | MoS Rs 63.**
- **DECISION: AVOID (on valuation).** CMP Rs 825 vs entry ceiling Rs 79. Hurdle STOP; every scenario 72-91% below CMP.
- **KEY SWINGS:** ▲ audited FY26 confirming durable 20%+ ROCE AND positive CFO would lift Pillar 1/Pillar 2 (STAGNANT->RECOVERING, 0.65x->0.80x+) but destination still ~19-22x vs 87x current — insufficient. ▼ margin reversion to peer 13.7% and continued cash burn pushes destination below 13x.
- **EXIT FRAMEWORK:** N/A (not a holding). Re-engage only if price enters Rs 63-79 AND audited FY26 shows CFO positive + ROCE sustained + WC days compressing.
- **ONE-LINE THESIS:** "Prizor at Rs 825 trades at 87x FY25 audited EPS against a four-pillar destination of 15x (ROCE 31.29% stagnant, cash 0.65x structural, EM 13.6, sector cap 25x); base Year-3 fair value Rs 154 = -43% CAGR; Hurdle Ratio STOP; AVOID on valuation. Cash quality: structural (INDETERMINATE-leaning)."

**"Valuation complete. Four-pillar exit PE 14.0x to 16.0x. Hurdle Ratio STOP. Entry price Rs 63 to Rs 79. Decision: AVOID (on valuation)."**

---

```yaml
stage: B11-valuation
company: "PRIZOR"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Rating agency WC/cash quote NOT FOUND (no rating PDF) - Pillar 2 defaulted conservative 0.65x"
  - "FII+DII shareholding NOT FOUND (aggregator 403) - UA third qualifier unverifiable, UA not applied"
  - "Peer P/E and EV/EBITDA medians NOT FOUND (only CP Plus) - no external multiple anchor"
  - "FY26 audited financials absent - valuation anchored to FY25 audited; FY26 unaudited excluded"
  - "Forward net debt/margins are scenario assumptions (flagged); conclusion insensitive"
flags:
  - "FLAG-CASH HIGH: cash multiplier 0.65x applied (INDETERMINATE leaning structural, conservative default); disposition capped at PROCEED WITH CAVEATS"
  - "FLAG-INTERNAL-ROCE-INCONSISTENCY: FY26 ROCE 37.2% vs 47.4% unaudited - excluded, FY25 31.29% used"
  - "FLAG-FORWARD-ROCE-DILUTION: mechanical ROCE compression risk - STAGNANT verdict, no uplift credited"
  - "FLAG-MARGIN-PEER-CONTRADICTED: claimed 21-23% EBITDA above CP Plus 13.7% - base compresses to 18%"
  - "FLAG-RPT-UNRECONCILED / FLAG-DISCLOSURE-QUALITY / FLAG-GATE0-DEAL-BREAKER propagate into RRM r=16%"
framework_versions: "Master v3.3 / Section 1B v3.3 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 15.0, mid: 16.2, high: 17.5, r_used: 16, rrm: 0.70}
  track2_additive: {low: 14.0, mid: 15.0, high: 16.0}
  divergence_pct: 8.0
  governing_track: "Track 2 additive - more conservative (15.0x), sets entry zone"
pillar_detail:
  roce_used: 31.29
  roce_base: 23.1
  roce_recovery_route: "not-credited"
  cash_multiplier: 0.65
  structural_or_growth: "INDETERMINATE leaning structural (conservative 0.65x per framework)"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 0
  shared_catalyst_flag: false
  ua_applied: false
  sector_cap_used: 25
hurdle_ratio: {base: 0.23, bull_used: false, verdict: "STOP"}
fair_values:
  track1: {bear: 84, base: 170, bull: 253}
  track2: {bear: 76, base: 154, bull: 231}
expected_cagr_prob_weighted: -45.4
entry_range: {low: 63, high: 79}
mos_price: 63
upside_downside_ratio: 0.0
decision: "AVOID (on valuation)"
unresolved_inputs_used:
  - "rating_wc_quote NOT FOUND -> conservative Pillar 2 multiplier 0.65x (INDETERMINATE leaning structural)"
  - "fii_dii_lt3 NOT FOUND -> UA multiplier NOT applied (all three qualifiers not evidenced)"
  - "current PE uses FY25 audited EPS 9.495 (86.9x); FY26 unaudited EPS excluded"
  - "forward net debt Bear45/Base25/Bull10 Cr - scenario assumptions, conclusion insensitive"
som_cagr_crosscheck: "consistent"
one_line_thesis: "Prizor at Rs 825 trades at 87x FY25 audited EPS vs a four-pillar destination of 15x (ROCE 31.29% stagnant, cash 0.65x structural, EM 13.6, cap 25x); base Year-3 fair value Rs 154 = -43% CAGR; Hurdle Ratio STOP; AVOID on valuation."
```
