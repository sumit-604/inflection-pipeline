# SECTION 1B AMENDMENTS — FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3

*Framework review conducted 02-Jul-2026 (Fable 5). Amendments adopted by Keerti; Amendment on premium scaling (original point 4) REJECTED with rationale recorded in Appendix A. Companion change: FTTCP v1.2 single-credit rule (Section 6 below).*

---

## AMENDMENT 1 — The 20x Rule Is Deleted

**Problem:** "Never assume exit P/E above 20x in any scenario" (Rules section) and "Exit P/E maximum: 15-20x" (criteria header) directly contradict Section 1B, which produces destination PEs of 24-45x by design. Whichever instruction a session anchors on determines the verdict.

**Change:**
- DELETE from RULES: "Never assume exit P/E above 20x in any scenario."
- DELETE from criteria header: "Exit P/E maximum: 15-20x (I will not assume market pays more than 20x)."
- REPLACE both with: **"Exit PE is governed solely by the Section 1B Four-Pillar Framework. The Sector Cap Table is the only ceiling. No other exit PE assumption is permitted anywhere in the analysis."**

---

## AMENDMENT 2 — 25% CAGR Feasibility Check (replaces the binary STOP rule AND the fixed 1.3x PE-gap check)

**Problem 1:** "If current PE > destination PE → STOP, fails 25% CAGR regardless of earnings growth" is mathematically false. Price CAGR = EPS CAGR × (PE_exit / PE_entry)^(1/3). A 40% EPS compounder de-rating from 30x to 25x still delivers ~32% CAGR. The old rule forecloses fast-growth de-rating winners.

**Problem 2:** The fixed 1.3x PE-gap requirement is arbitrary. The true required gap depends on EPS growth: Required gap = 1.953 ÷ (1 + EPS CAGR)³. At 20% EPS CAGR the required gap is only 1.13x; at 10% it is 1.47x.

**Change — both checks are replaced by one Hurdle Ratio:**

**Hurdle Ratio (HR) = (1 + EPS CAGR)³ × (Destination PE mid ÷ Current PE)**

Pass threshold: HR ≥ 1.953 (which is 1.25³, i.e., 25% price CAGR over 3 years).

| Condition | Verdict |
|---|---|
| HR(Base EPS CAGR) ≥ 1.953 | PASS — proceed normally |
| HR(Base) < 1.953 but HR(Bull) ≥ 1.953 | CONDITIONAL — proceed, but flag "growth-dependent with de-rating headwind"; verdict capped at WATCHLIST / BUY-ON-DIPS; no BUY NOW |
| HR(Bull EPS CAGR) < 1.953 | STOP — overvalued; 25% CAGR is infeasible even on bull-case earnings |

Conservative-bias note: Bull EPS CAGR may only be used in this check if management delivery track record is Good or Excellent (consistent with existing Section 2A bull-case rules). If track record is Mixed or Poor, the Bull row of this check uses Base EPS CAGR + 5% maximum.

---

## AMENDMENT 3 — Undiscovered Alpha Multiplier Ordering Codified

**Problem:** Whether UA applies before or after the sector cap was undefined. Applied after, a 1.25x uplift silently turns a 30x cap into 37.5x, defeating "sector reality" entirely.

**Change:**

**Final Destination PE = min( Raw Destination PE × 1.25, Sector Cap )**

- The UA multiplier applies to the RAW destination PE (Row F of the summary table), BEFORE the sector cap comparison.
- The Sector Cap is ABSOLUTE. UA can never breach it.
- UA applies only when all three qualifiers hold: listed ≥12 months; Gate 0 ≥60 OR EM ≥25; FII+DII combined <3%.
- The Four-Pillar Summary Table gains one row: **F2. UA-Adjusted Raw PE = F × 1.25 (if qualified) — then H = min(F2, G).**
- Retroactive note: any existing Notion save where a UA-uplifted destination PE exceeds the sector cap (verify Hester Biosciences first) must be re-stated at next quarterly refresh.

---

## AMENDMENT 4 — Single-Credit Rule for ROCE Recovery (Section 1B + FTTCP v1.2)

**Problem:** ROCE recovery can currently be credited in up to three places: Pillar 1 trajectory smoothing (midpoint ROCE), the Strategic Premium ("+1x ROCE re-rating optionality" per FTTCP v1.1 Section 8), and the Growth Premium (when the named catalyst IS the capex commissioning). The Pace Digitek worked example in FTTCP v1.1 itself double-credits: destination-ROCE-informed Pillar 1 base AND +1x strategic ROCE re-rating premium.

**Change:**
- ROCE recovery may be credited in **Pillar 1 (midpoint smoothing) OR the Strategic Premium — never both.**
- Default: credit it in Pillar 1. The Strategic Premium route is permitted only when trajectory smoothing was NOT applied (e.g., hard evidence exists but the +4 trajectory-adjustment threshold was not met).
- The Section 1B worksheet must state explicitly which route was used: "ROCE recovery credited via: [Pillar 1 midpoint / Strategic Premium / not credited]."
- Growth Premium interaction: if the primary catalyst driving the EM/catalyst premium is the same capex commissioning that justifies midpoint smoothing, this is permitted (the premiums measure different things — earnings visibility vs capital efficiency) but must be flagged in the worksheet as "shared catalyst" so Role 3 can stress-test the single point of failure.
- FTTCP v1.1 Section 8 (Pace worked example) is annotated: the +1x ROCE re-rating strategic premium in that example is superseded; under v1.2 Pace credits recovery via Pillar 1 only. This log entry constitutes FTTCP v1.2.

---

## AMENDMENT 5 — Continuous Pillar 1 Formula (replaces the ROCE band table)

**Problem:** Step-function bands create cliff effects: ROCE 24.9% → 19x but 25.1% → 21x. A 20bps measurement difference moves fair value ~10%.

**Change — the band table is replaced by:**

**ROCE Base PE = 0.5 × ROCE(%) + 7.5, floored at 9x, capped at 24x.**

Verification against the old table (matches within rounding): 12% → 13.5x (was 12x), 17% → 16x (was 16x), 22% → 18.5x (was 19x), 27% → 21x (was 21x), 32% → 23.5x (was 24x).

- Trajectory smoothing rule unchanged: where applicable, the midpoint ROCE feeds this formula.
- Round the resulting base to one decimal; do not round intermediate ROCE.
- The old band table is retained in the document as a quick-reference approximation only, marked "superseded by formula."

---

## AMENDMENT 6 — Proportional Destination PE Range (replaces fixed ±2x)

**Problem:** ±2x on a 12x destination is ±17% implied uncertainty; on a 37x destination it is ±5%. Same nominal band, wildly different implied confidence.

**Change:** **Destination PE Range = calculated value ±7.5%, rounded to the nearest 0.5x.**

Examples: 12x → 11-13x; 20x → 18.5-21.5x; 37x → 34-39.5x (upper bound still subject to sector cap).

---

## AMENDMENT 7 — Lender Carve-Out for Pillar 2 (Asset-Quality Multiplier)

**Problem:** CFO/PAT is meaningless for banks, NBFCs, and MFIs (Satin, Bandhan), yet the sequence makes Section 1B mandatory and FTTCP v1.1 makes the quadruple framework mandatory for lending. Pillar 2 had no lender variant.

**Change:** For lending businesses (banks, NBFCs, MFIs, HFCs), the Cash Conversion Multiplier is REPLACED by an **Asset-Quality Multiplier**:

| Asset-Quality Band | Multiplier | Description |
|---|---|---|
| Credit costs stable/declining 2+ yrs, GNPA <2%, PCR >70% | 1.15x | Elite underwriting |
| GNPA 2-4% and stable, PCR 60-70%, credit costs within guided band | 1.00x | Sound |
| GNPA rising OR >4%, PCR <60%, credit cost guidance missed once | 0.80x | Stressed |
| Rising credit costs + PCR <50% + growing restructured/written-off book | 0.65x | Structural underwriting weakness |

- No growth offset applies to the Asset-Quality Multiplier (loan growth cannot offset bad underwriting — it compounds it).
- P/B (theoretical P/B = ROE ÷ CoE) remains the PRIMARY valuation method for lenders; the Section 1B destination PE becomes the SECONDARY cross-check.
- Pillar 1 for lenders uses ROE bands in place of ROCE (same formula: 0.5 × ROE + 7.5, floor 9x, cap 24x), since ROCE is not meaningful for leveraged financials.
- FTTCP Transition 3 (cash conversion) for lenders is likewise read as asset-quality trajectory (credit costs, GNPA, collection efficiency), not CFO/PAT.

---

## AMENDMENT 8 — Sector Cap Table Additions

New rows covering the active universe (proposals — adjust caps if you disagree):

| Sector | Maximum Exit PE |
|---|---|
| Hospitals / dialysis / healthcare services | 35x |
| Data centers / cloud infrastructure (capital-heavy) | 30x |
| EV charging / energy transition equipment | 28x |
| City gas distribution | 22x |
| Mining / mineral exploration | 20x |
| Banks / NBFCs / MFIs | 18x (P/B primary; PE is cross-check only) |

---

## AMENDMENT 4 (v3.4) — PILLAR 3 DECOUPLED

**Change:** Pillar 3 splits into two additive components, combined hard cap **+6x** (the existing Pillar 3 maximum):

**3a Growth Visibility Premium** — paid on documented growth machinery, independent of EM score. Qualifying evidence (📄 documented tier only, never claims):
- capex-embedded growth ≥15% (committed capex × historical fixed-asset turnover ÷ current revenue)
- order book ≥1.0x revenue or book-to-bill ≥1.2x
- SOM-implied revenue CAGR ≥20% with the capacity cross-check passing
- management delivery grade A or B

Award: **+2x if any two qualify; +3x if three or more qualify AND delivery grade is A or B; +0x otherwise.** Grade C caps 3a at +2x; grade D pays +0x.

**3b Moat Formation Premium** — the existing EM-gated table, unchanged, applied as before.

**3c Duration Premium** — paid on documented forward revenue visibility. **+1x when visibility covers ≥2.5 years** (executable order book ÷ current annual revenue ≥2.5, or contracted/regulated revenue streams of equivalent tenor); **+2x when ≥4 years.** Evidence tier 📄 only — signed contracts, LoAs with stated values, regulatory annuity terms; management pipeline talk and TAM stories pay nothing. Example: order book 15x annual revenue, documented via LoAs → 3c = +2x.

3a prices documented growth; 3b prices forming moats; 3c prices the duration of documented revenue. A company may earn any without the others. Combined 3a+3b+3c never exceeds the +6x Pillar 3 cap. Sector caps remain absolute.

---

## AMENDMENT 6 (v3.4) — TWO-TIER RETURN HURDLE

The single 25% CAGR hurdle is replaced by two declared tiers, assigned mechanically.

**Tier A — Transition / Undiscovered (hurdle 25% CAGR).** Default tier. Applies when FII+DII combined <3% (the UA institutional-absence test), OR the combined Gate0+EM assessment is TURNAROUND or HIGH POTENTIAL. This is the core strategy sleeve; nothing changes for it.

**Tier B — Discovered Quality (hurdle 20% CAGR).** Applies only when ALL hold:
- FII+DII ≥3% (the market has found it)
- Gate 0 classification GOOD or better OR EM ≥25
- promoter verdict TRUSTWORTHY or better
- no structural FLAG-CASH

Companies failing Tier B's quality gates stay at 25% regardless of discovery.

**Cascade rules:**
- Entry price = base fair value ÷ (1 + hurdle)³. Tier A divisor 1.953 (1.25³); Tier B divisor 1.728 (1.20³).
- MoS price remains 20% below entry.
- The Hurdle Ratio pass threshold becomes **1.953 for Tier A and 1.728 for Tier B.**
- 4D probability weights unchanged.
- Position sizing: Tier B positions default to a **Medium (4-6%) ceiling** unless the operator documents an override in the thesis — the lower-return sleeve must not crowd the core sleeve's capital.
- The verdict card MUST state, on its first line: **"Tier: [A/B] | Hurdle: [25%/20%]".**

Tier B exists because discovered-quality names structurally do not offer 25% entries in functioning markets; participating in them at 20% is a declared strategy choice, not a framework relaxation. The 25% tier remains the strategy's core.

---

## APPENDIX A — REJECTED AMENDMENT (RECORDED FOR AUDIT TRAIL)

**Proposal (rejected 02-Jul-2026):** Scale Growth and Strategic Premiums by the Cash Multiplier (or cap premiums at 50% of quality-adjusted base when multiplier <1.0x), on the grounds that a structurally cash-negative business can currently earn premiums exceeding its quality base.

**Rejection rationale:** The premiums are already independently evidence-gated — EM score thresholds, documented (📄) evidence requirements, and catalyst proximity. Cash quality is separately policed twice: the structural vs growth-induced test inside Pillar 2, and FTTCP Transition 3 (which independently produces AVOID when cash conversion is declining with no catalyst, as in Kernex). Scaling premiums by the cash multiplier would double-punish inflection-stage businesses — the exact class the FTTCP-first sequencing exists to price correctly. The additive premium structure stands as designed.

**Residual risk accepted:** a structurally cash-negative name with genuine high EM and near catalyst can still reach a destination PE where premiums exceed the quality base. Mitigant: FTTCP runs before Role 1 and will flag Transition 3 as DECLINING/no-catalyst, which caps or kills the verdict before valuation matters.

---

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 3.2 | Jun 2026 | Prior spec (Notion: Valuation Framework v3.2) |
| 3.3 | 02-Jul-2026 | Amendments 1-8 above. 20x rule deleted; Hurdle Ratio replaces STOP rule and 1.3x gap check; UA ordering codified as min(Raw × 1.25, Cap); ROCE single-credit rule (FTTCP v1.2); continuous Pillar 1 formula; proportional ±7.5% range; lender Asset-Quality Multiplier carve-out; six sector cap rows added. Premium-scaling proposal rejected (Appendix A). |
| 3.4 | 11-Jul-2026 | Amendment 4 (v3.4): Pillar 3 decoupled into 3a Growth Visibility Premium (documented growth machinery, independent of EM score), 3b Moat Formation Premium (existing EM-gated table), and 3c Duration Premium (documented forward revenue visibility: +1x ≥2.5yr, +2x ≥4yr, 📄 only). Combined 3a+3b+3c hard-capped at +6x; sector caps absolute. |
