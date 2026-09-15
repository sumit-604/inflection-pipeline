# Chunk 07. Base-case revenue basis hierarchy and margin bridge (Rules B and C)

Loaded by: Role 1 Section 2A and 2B. Pipeline: stage 11; stage 15 (Rule H preconditions 1 and 2: declared basis, stated bridge); Verifier C (12c).
Sources in force: Section 1B v3.10 Amendments 26.1, 26.2, 26.3; Master v3.7 §2A, §2B (as amended by Amendment 26); v3.6 Amendment 14; v3.7 Amendment 17.3; FTTCP v2.3 cyclical margin rule and Modules B1, B5.

## Operating rule for every projection (Amendment 26.3)

"State the most evidenced path. Where evidence is thin, present both readings and the single observation that separates them. Size the position for the doubt (Amendment 25). Do not shade individual inputs."

Bear and bull cases remain as defined below. The base case is never built by stacking cautious choices. This rule governs Role 1 projections only; the document-reading protocols (Annual Report Analysis Protocol, Quarterly Results Review Protocol, quarterly forensic agents) and the TAM estimate-selection rule keep their own interpretation rules.

## 2A. Revenue

### Base case: Rule B, the revenue basis hierarchy (Amendment 26.1)

Base-case revenue uses whichever basis rests on harder evidence. The worksheet declares which.

| Basis | Definition | Evidence tier required |
|---|---|---|
| RUN-RATE | Exit-quarter revenue annualised, adjusted for stated seasonality | filed quarterly results |
| ORDER-BOOK | Executable order book at disclosed execution cycle, plus disclosed pipeline at historical conversion | filing, or concall with Role 5 grade A/B |
| CAPACITY | Commissioned or dated capacity at guided utilisation ramp and realisation | capex commissioning filing plus utilisation guidance on the concall |
| GUIDANCE-DISCOUNTED | Management guidance discounted by the trailing-4-quarter Role 5 credibility ratio | concall with Role 5 history |
| HISTORICAL | Historical CAGR | fallback only when none of the above exists |

- Historical CAGR is always computed and shown beside the chosen basis as the cross-check. It governs only when no forward evidence exists.
- If the chosen basis diverges from historical CAGR by more than 10 percentage points, name the observation that will confirm or refute the divergence and its confirm-by date. It feeds the Expectation Ledger (chunk 09).
- RUN-RATE uses the same run-rate definition as the Amendment 21 earnings base (chunk 08).
- Single credit: a catalyst credited into revenue at its probability (CAPACITY or ORDER-BOOK) is not credited again in Pillar 3 at full weight. State the split in the 2C-w line (chunk 17).

### Bear and bull

- Bear: Lower of (historical CAGR − 5%) or (industry growth rate) or (what happens if 1-2 triggers fail).
- Bull: management guidance at face value, only if the Role 5 credibility grade is A or B.

### Growth fade horizon (Amendment 14)

The Emerging Moat classification sets how fast growth fades toward industry growth. Show the step-down year by year. Rule B sets the level the fade starts from; the fade sets the path.

| Emerging Moat classification | Durability of growth |
|---|---|
| Moat Expansion | Holds high growth through Year 5 |
| Strengthening | Fades by Year 4 |
| Modest | Fades to industry growth by Year 3 |
| None | Fades immediately (industry growth from Year 1) |

"Fades" means the growth rate steps down toward industry growth across the horizon, not that growth stops. Where the fade needs an industry growth anchor the corpus does not hold, the anchor is a named assumption in the table (Amendment 18.0). Horizon and exit haircut rules are in chunk 10.

### Funding and incentive checks feeding revenue and margin

- FTTCP Module B1: each projection year declares its funding channel (new reinvestment at growth ÷ incremental ROCE, or utilization ramp capped at nameplate × realistic peak utilization × current realization). Unfunded growth fails for that year. A STRETCHED or BREACH debt verdict cannot fund Channel 1 growth with new debt.
- FTTCP Module B5: an incentive expiring inside three years is not sustainable earnings. Year 3 uses post-expiry margins and EPS.

## 2B. Margin

### Base case: Rule C, the margin bridge (Amendment 26.2)

Base margin = the margin implied by destination mix and operating leverage, shown as a bridge.

| Lever | bps contribution | Evidence | Confirm-by |
|---|---|---|---|
| Current margin | ___% | latest FY filing | n/a |
| Mix shift (name the product/segment) | +/- ___ bps | | |
| Operating leverage on fixed cost base | +/- ___ bps | | |
| Input cost / pricing pass-through | +/- ___ bps | | |
| **Base-case margin Year 3** | ___% | | |

Bridge rules:

- A lever with no evidence line is not a lever. Drop it.
- Every confirm-by date feeds the Expectation Ledger (chunk 09).
- If the bridge lifts margin more than 400 bps in three years, the Second-Order Section (Role 2 §3.5, Rule F) carries a chain showing the customer-side or cost-side mechanism that pays for it, and the bridge names that chain by number.

### Bear and bull

- Bear: lowest margin from the last 5 years (excluding a one-off year), or current − 200 bps, or the trailing 3-year average margin, whichever the evidence supports.
- Bull: highest sustainable margin from the last 5 years, or guided margin at face value where the Role 5 grade is A or B.

### Cyclical override (supersedes the bridge for sectors flagged cyclical)

For any sector flagged cyclical (asset-heavy manufacturing, industrial and cyclical names, capital goods, commodity-linked processors): base = full-cycle average margin; bear = cycle trough margin; bull = cycle peak margin. State the cycle years that define peak, trough and full-cycle average, consistent with the FTTCP Part B Output Sheet.

### Converters

The bear case carries at least one input-price mean-reversion year with spreads compressing to the 5-year median spread, even where guidance says otherwise (Amendment 17.3, chunk 11).

## 2C. Projection table

Base case primary, bear and bull as ranges. Rows: Revenue, EBITDA, EBITDA margin, PAT, EPS (diluted), Book value/share, Est. CFO, Est. FCF, Est. net debt, Est. ROCE, Est. ROE. Columns: Year 0, Year 1, Year 2, Year 3, Year 4 (committed, chunk 10), Year 5. EPS is operating EPS (FTTCP Module B4).
