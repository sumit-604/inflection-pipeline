# STAGE 5 — CONCALL ANALYSIS: APEX ECOTECH LIMITED (APEXECO)
Run date: 2026-07-10 | Model: claude-sonnet-5 | Pipeline stage B05-concall

## CHRONOLOGY AND LABELLING NOTE (read before the rest of this report)

Three transcripts were supplied, oldest first, with a tentative quarter map:
1. Concall_May_2025_Transcript.pdf → mapped as "Q4 FY25"
2. Concall_Nov_2025_Transcript.pdf → mapped as "Q2 FY26"
3. Concall_May_2026_Transcript.pdf → mapped as "Q4 FY26"

**Flag: labelling conflict, not a date conflict.** The transcripts' own cover
titles and internal commentary make clear Apex Ecotech reports on a
half-yearly (H1/H2) cadence, not a quarterly one — this is stated explicitly
and repeatedly by both management and analysts across all three calls
(analyst Agastya Dave calls the 6-month reporting gap "a vacuum" in every
single call). The actual periods discussed are:
- Call 1 (26-May-2025): "H2 FY'25 Earnings Conference Call" — H2 FY25 and
  full-year FY25 results (year ended 31-Mar-2025).
- Call 2 (18-Nov-2025): "H1 FY26 Earnings Conference Call" — H1 FY26 results
  only (six months to 30-Sep-2025).
- Call 3 (12-May-2026): "H2 FY26 & FY26 Earnings Conference Call" — H2 FY26
  and full-year FY26 results (year ended 31-Mar-2026).

The call dates themselves do NOT conflict with the injected map (May 2025,
Nov 2025, May 2026 all match). Per instructions I retain the map's quarter
labels (Q4 FY25 / Q2 FY26 / Q4 FY26) for cross-pipeline consistency and to
satisfy the downstream YAML contract, but every figure below is anchored to
its true underlying period (H2 FY25/FY25, H1 FY26, H2 FY26/FY26) so no
number is misread as a discrete quarterly figure. This distinction matters
for stage 6 and stage 11: Apex Ecotech does not disclose quarterly
financials, only semi-annual ones, despite three consecutive analyst
requests to do so (see Section 2E).

---

## SECTION 1: GROWTH TRIGGERS & DRIVERS

### 1A. Growth triggers and drivers table

| Trigger | Type | Timeframe | Confidence | Specificity |
|---|---|---|---|---|
| Order book conversion (spillover into execution) | Volume | Near (same FY) | Committed | High — gestation period repeatedly quantified at 6-10 months (Q4 FY25 call, Anuj Dosajh, p.4-5, p.11) |
| Shift toward ZLD (Zero Liquid Discharge) mix | Price-mix | Medium | Planned | Medium — ZLD framed as "the name of the game," ~20-30% of revenue at Q4 FY25 call, no updated % given later (Q4 FY25 call, Anuj Dosajh, p.7) |
| Bigger ticket-size orders (Toyota/L&T ~₹40cr, then Reliance ₹100-125cr) | Volume | Near-medium | Committed (delivered) | High — named clients, named order sizes (Q4 FY25 call p.5; Q2 FY26 call p.6) |
| International expansion (Bangladesh, Vietnam) | Volume/Sectoral | Medium-long | Planned | Low — no specific order/revenue figures ever given (Q4 FY25 call, Anuj Dosajh, p.3) |
| International expansion (Vietnam, Indonesia, Middle East; Bangladesh "back seat") | Volume/Sectoral | Medium-long | Aspirational, then abandoned | Low — degraded from "planned" to explicit failure admission by Q4 FY26 call (Q2 FY26 call, Anuj Dosajh, p.13; Q4 FY26 call, Anuj Dosajh, p.15) |
| Government/power-sector order entry (policy shift) | Regulatory-policy/Volume | Near | Committed (small, delivered) | Medium — Pragati Power Corporation order (₹3-5cr) delivered as the concrete instance (Q4 FY25 call, Anuj Dosajh, p.9; Q2 FY26 call, presentation, p.6) |
| Automation/SAP/digital systems investment | Cost | Medium | Planned | Low — mentioned once, no cost figure, no later follow-up (Q4 FY25 call, Anuj Dosajh, p.12) |
| ESOP for core team | Cost (retention) | Near (specific deadline given) | Committed, then silently dropped | High deadline given ("by the end of this financial year," i.e. FY26), zero mention in Q4 FY26 call (Q2 FY26 call, Anuj Dosajh, p.13) |
| Steadier H1/H2 revenue split (reduce crest-trough skew) | Volume/Cash-flow | Near | Committed | High — explicit "30-70 ratio... trying to bring it closer" (Q4 FY25 call, Anuj Dosajh, p.17); actual result moved the OTHER way (see 1C) |
| India manufacturing capex cycle / larger factory sizes | Sectoral | Long | Management view | Medium — asserted, not quantified with any external data point (Q4 FY26 call, Anuj Dosajh, p.9) |
| Market consolidation among water-treatment players favouring scaled players | Sectoral | Long | Management view | Low — asserted with no supporting data ("a couple of lakh companies," self-admitted guess) (Q4 FY26 call, Anuj Dosajh, p.16-17) |
| Raw-material/logistics cost pass-through on new orders | Cost/Price-mix | Near | Committed | Medium — "we would definitely raise our prices and we have done that already," no % given (Q4 FY26 call, Anuj Dosajh, p.10) |

### 1B. Quantified guidance table (see also YAML `guidance:`)

| Item | Number | Timeframe | Stated in |
|---|---|---|---|
| Opening order book | >₹55 crore | Start of FY26 | Q4 FY25 call (Anuj Dosajh, p.3) |
| Prior-year (FY25) order book | ~₹119 crore | FY25 | Q4 FY25 call (Anuj Dosajh, p.5) — later contradicted by CFO in Q4 FY26 call, who cited "~₹62 crore plus" for the same reference point (Rakesh Kaul, p.8) |
| Minimum revenue growth expectation | "at least" ~25% (FY24 was 34%) | FY26 | Q4 FY25 call (Anuj Dosajh, p.5) |
| Order book (mid-year) | ₹145 crore (incremental to already-billed ₹32.56cr H1) | As of Nov 2025 | Q2 FY26 call (Anuj Dosajh, presentation p.8, and clarification p.18) |
| Reliance Consumer Products order | ₹100-125 crore, ~70% to execute within FY26 | FY26 | Q2 FY26 call (Anuj Dosajh, p.6) |
| Bharatiyam Beverages order | ₹10-15 crore, invoicing complete by March | FY26 | Q2 FY26 call (Anuj Dosajh, p.6) |
| Pragati Power Corporation order | ₹3-5 crore | FY26 | Q2 FY26 call (Anuj Dosajh, p.6-7) |
| ESOP for core employees | No amount given | "By the end of this financial year" (FY26) | Q2 FY26 call (Anuj Dosajh, p.13) — NOT mentioned again in Q4 FY26 call |
| FY26 actual revenue | ₹148.65 crore, +109.5% YoY | FY26 (delivered) | Q4 FY26 call (Anuj Dosajh, p.2) |
| FY26 actual EBITDA | ₹21.76 crore, +96.82% YoY | FY26 (delivered) | Q4 FY26 call (Anuj Dosajh, p.2) |
| FY26 actual PAT | ₹17.02 crore, +98.85% YoY | FY26 (delivered) | Q4 FY26 call (Anuj Dosajh, p.2) |
| FY26 actual EPS | 12.91, +63.21% YoY | FY26 (delivered) | Q4 FY26 call (Anuj Dosajh, p.2) |
| Cash and bank balance | ₹35.06 crore | As of 31-Mar-2026 | Q4 FY26 call (Anuj Dosajh, p.2) |
| Working capital | ₹61.72 crore | As of 31-Mar-2026 | Q4 FY26 call (Anuj Dosajh, p.2) |
| Closing order book | >₹125 crore (spillover into FY27) | As of 31-Mar-2026 | Q4 FY26 call (Anuj Dosajh, p.4) |
| FY27 growth guidance | "30 to 40% growth overall" — verbal, non-numeric, declined to confirm specific ₹200cr revenue / 15% EBITDA margin figures put to him by an analyst | FY27 | Q4 FY26 call (Anuj Dosajh, p.12-13) |
| Raw material (metal) cost inflation absorbed in H2 FY26 | 25-40% increase | H2 FY26 | Q4 FY26 call (Anuj Dosajh, p.10) |

### 1C. Trigger evolution across the three calls

| Trigger | Q4 FY25 status | Q2 FY26 status | Q4 FY26 status | Trend |
|---|---|---|---|---|
| Order-book-to-revenue conversion | Committed, ~55cr opening | Scaled up massively (145cr, Reliance-led) | Delivered — FY26 revenue +109.5% YoY | Strengthening |
| ZLD mix / margin accretion narrative | Central theme, ~20-30% of revenue | Repeated qualitatively, no % update | Margins actually declined YoY (RM cost cited as cause, not ZLD-mix offset) | Weakening — promise partially undercut by results |
| H1/H2 revenue skew reduction (steadier turnover) | Explicit commitment to narrow the 30-70 split | Not addressed | H1 FY26 was 32.56cr of 148.65cr FY26 total = ~22/78 split — MORE skewed, not less | **Reversed — flag** |
| International expansion (Bangladesh/Vietnam) | New trigger, aspirational | Widened to Vietnam/Indonesia/Middle East; Bangladesh explicitly "taken a back seat" | Gulf effort admitted a failure ("anti-modal to our thought process"); focus now "primarily India itself" | **Dropped, with rare honest admission of failure** |
| ESOP for core team | Referenced as an old IPO-era intention | Reiterated with a hard deadline (by end of FY26) | **Zero mention** in the FY26 year-end call, despite the deadline having just passed | **Dropped — silent, unexplained. Flag.** |
| Quarterly reporting | Promised for "subsequent quarters" | Still not delivered; vague "some things are coming up" | Partial delivery revealed — a Q3 FY26 percentage-only circular was issued, but full quarterly numbers still not committed | Timeline slippage across all 3 calls — see 2E |
| Government/power-sector orders | New policy shift announced | Pragati Power Corporation order delivered (₹3-5cr) | Not mentioned again as a growth vector | Delivered once, then quietly not scaled |
| Customer concentration (Reliance dependency) | N/A (pre-Reliance order) | Raised implicitly by analyst re: Reliance/L&T reliance | Directly raised twice (Rushwithnag, Shivam Mehra); management reassures but never quantifies top-customer % of revenue | New trigger risk that is growing, not shrinking |

---

## SECTION 2: MANAGEMENT CREDIBILITY CHECK

### 2A. Promise vs. delivery tracker (chronological)

| Promised in | Promise | Outcome | Explanation given |
|---|---|---|---|
| Q4 FY25 call | Revenue growth "at least" ~25% for FY26 | ✅ Delivered — vastly exceeded (109.5% YoY per Q4 FY26 call) | N/A — beat, no excuse needed |
| Q4 FY25 call | Order book (₹55cr+) will convert to revenue within the year (6-10 month gestation) | ✅ Delivered | Consistently explained via gestation-period mechanics each call |
| Q4 FY25 call | "We are trying to bring [H1/H2 split] closer" — reduce the 30-70 skew | ❌ Missed — FY26 split moved to roughly 22/78, more skewed than before | No acknowledgment that this reversed; not raised proactively by management in Q4 FY26 call |
| Q4 FY25 call | Quarterly reporting "from subsequent quarters" | Partial — a percentage-only circular appeared at Q3 FY26, no full quarterly financials across 3 calls | Repeatedly cited SEBI SME six-month rule and "compliance" burden as the constraint (external-blame leaning, though grounded in a real regulatory carve-out for SMEs) |
| Q2 FY26 call | ESOP for core people "by the end of this financial year" (FY26) | ❌ Missed, not mentioned again | Silence — no explanation offered in Q4 FY26 call at all |
| Q2 FY26 call | ZLD/bigger-ticket mix will be margin accretive | Partial/❌ — margins declined YoY in H2 FY26 despite bigger tickets | Explained via raw-material cost inflation (25-40%) and logistics costs, not disputed as a real headwind, but original accretion claim not revisited or reconciled |
| Q2 FY26 call | International expansion into Vietnam/Indonesia/Middle East | ❌ Missed — Gulf effort explicitly abandoned | Rare honest admission: "that has turned out to be totally anti-modal to our thought process" (Q4 FY26 call, Anuj Dosajh, p.15) |
| Q2 FY26 call | Order book of ₹145cr as of Nov-2025 | Not reconciled — Q4 FY26 call shows ₹125cr closing order book and management cannot cleanly walk the bridge from 145 to 125, nor from the original 55cr (Q4 FY25) to a separately-cited 62cr (CFO, Q4 FY26) | "I'm not too sure about the..." / "We will get back to you on that if you want" (Anuj Dosajh, Rakesh Kaul, Q4 FY26 call, p.8, p.17) |

**Promise-delivery scoreboard: delivered 3, partial 2, missed 3** (see YAML for exact counts used).

### 2B. Excuse pattern analysis

- **External-blame instances**: raw-material/metal cost inflation (25-40%) attributed to "the war and other maybe geopolitical things" (Q4 FY26 call, Anuj Dosajh, p.10) — grounded and specific, not vague deflection; SEBI's six-month SME reporting rule blamed for the quarterly-reporting gap (all three calls) — this is a real regulatory feature, not invented, but is used consistently as the reason for not doing MORE than what SEBI requires, even though the analyst's request (a one-paragraph voluntary update) does not require SEBI compliance.
- **Honest-admission instance**: the Gulf/Middle-East expansion failure — management volunteered the setback unprompted in response to a general international-orders question, using blunt language ("anti-modal to our thought process") rather than reframing it as a strategic pivot. This is a genuine positive data point for tone.
- **Deflection instances**: order-book reconciliation across calls (Q4 FY26 call) — management and CFO give three different historical order-book figures (55cr, 62cr, and an unreconciled 145-to-125 bridge) without ever settling on one number; "we'll get back to you" is used as a placeholder without a committed follow-up channel.
- **Silence instance**: ESOP promise from Q2 FY26 call — simply never mentioned again, with no acknowledgment that the self-imposed deadline (end of FY26) had passed.
- **Pattern check**: management does raise hard topics somewhat proactively (raw-material cost pressure and the Gulf failure were both volunteered, not extracted under pressure) — a positive signal. But it also lets some commitments (ESOP, H1/H2 skew, precise order-book bridging) lapse without any proactive acknowledgment; these are only exposed when an analyst happens to ask. Management does say once, self-critically, "we are not the kind of guys who will blow trumpets without actually performing" (Q4 FY25 call, Anuj Dosajh, p.12) — an implicit acknowledgment of the standard it is holding itself to, against which the ESOP silence reads as a genuine miss rather than a forgivable oversight.

### 2C. Tone ratings (1-5, evidence-based)

| Dimension | Rating | Evidence |
|---|---|---|
| Transparency | 3/5 | Volunteers the Gulf failure and RM cost pressure unprompted (+); but ESOP dropped silently and order book numbers not reconciled across calls (-) |
| Specificity | 3/5 | Order sizes, client names, and gestation periods are consistently specific; but growth/margin guidance for FY27 stays deliberately non-numeric even under direct analyst pressure (Q4 FY26 call, Keshav exchange, p.12-13) |
| Consistency | 2/5 | Order-book figures conflict across calls (55cr vs 62cr vs 145cr vs 125cr, never bridged); H1/H2 skew-reduction promise reversed without comment; Veolia relationship described as a "strategic alliance... deepened" (Q4 FY25 call, p.3) and "strong collaboration" (Q2 FY26 call, p.4) but then explicitly disclaimed as "not in any partnership, any JV... understanding per se" (Q4 FY26 call, Anuj Dosajh, p.19) |
| Accountability | 3/5 | Genuine ownership of the Gulf failure; but zero acknowledgment of the ESOP miss or the reversed H1/H2 skew promise |
| Defensiveness | 2/5 (low defensiveness is good) | Management answers pointed questions (margin decline, customer concentration, EPS-vs-PAT growth gap) directly rather than stonewalling; CFO steps in with data corrections rather than deflecting |
| Over-promotion | 2/5 (low over-promotion is good) | Chairman explicitly disclaims "blowing trumpets" and gives conservative, hedge-heavy language on forward guidance rather than promotional framing; some IPO-era enthusiasm in early call but tempers over time |

### 2D. What management is NOT saying

- **No quantified customer concentration disclosure.** Despite being asked about Reliance/L&T dependency in two separate calls (Q4 FY26: Rushwithnag and, implicitly, Shivam Mehra), management never states the % of FY26 revenue derived from the top 1, 3, or 5 customers — a number that is directly calculable given a single order (Reliance) was ~70-100cr against ~148cr total FY26 revenue, i.e. potentially majority-weighted to one client. This is a material omission the financial statements and industry situation (project-based EPC with lumpy large orders) demand be addressed and it was not, even when directly invited to.
- **No update on ZLD's actual % of revenue mix** after the initial ~20-30% figure cited in the Q4 FY25 call — despite ZLD being repeatedly cited as the central margin-accretion thesis.
- **No explanation for the reversed H1/H2 skew** (promised to narrow, actually widened) — never proactively addressed.
- **No mention of the ESOP program** in the Q4 FY26 call at all, despite its own stated deadline having passed.
- **No receivable-days trend disclosure after the initial FY25 spike** — the FY25 receivable spike (21cr to 50cr) was explained as a Feb/March invoicing timing effect; no subsequent call gives a concrete "receivables now stand at X days" update to close the loop, only qualitative reassurance ("no red flag").

### 2E. Repeated question tracker (mandatory)

| Question | Quarters asked | Responses | Classification |
|---|---|---|---|
| "Please consider quarterly (or at least more frequent, one-paragraph) reporting — six months is too large a gap" | Asked by Agastya Dave in Q4 FY25 call (p.13-15), Q2 FY26 call (p.10-11), AND Q4 FY26 call (p.10-11); echoed independently by Mahender Konda (Q2 FY26 call, p.16) and Shivam Mehra (Q4 FY26 call, p.17) | Q4 FY25: "if not this quarter, I can't promise it, but definitely from subsequent quarters, we'll be doing it." Q2 FY26: "Last time also I had said that we will definitely be putting up the quarter. It does. It's just that... some of the things are coming up." Q4 FY26: "we did take out a circular at the third quarter... it was not in terms of numbers, but it was in terms of percentages... we intend to continue" | **Answer changed between quarters — from outright deferral, to unfulfilled repetition of the same promise, to a partial (percentage-only, non-numeric) delivery that still falls short of what was requested.** This is a genuine cross-quarter evasion pattern and the single clearest credibility data point available in these transcripts. |

No other question meeting the "asked in two or more quarters, never directly answered" bar was identified. The order-book-reconciliation confusion and the ESOP silence are both real credibility issues (documented above) but each surfaced from a single specific question rather than the same question being asked across multiple calls, so they are captured in 2A/2B/2D/4D rather than here.

---

## SECTION 3: COMPETITIVE INTELLIGENCE FROM CONCALLS

### 3A. Competitor commentary and credibility check

- **Thermax, Ion Exchange, Concord** cited as pan-India competitors (Q4 FY25 call, Anuj Dosajh, p.9). Credible — these are established, verifiable listed/large players in the Indian water-treatment space; consistent with public market structure.
- **Va Tech Wabag** explicitly distinguished (Q4 FY26 call, p.18) as operating in "much larger plants like desalination and into government jobs and operation and maintenance" — i.e., not a direct competitor to Apex's turnkey industrial ZLD niche. Plausible segmentation claim, worth checking against Wabag's own disclosed segment mix in stage 6.
- **Ion Exchange** described as one of the few companies present across all three water sub-segments (household/industrial/municipal) (Q4 FY26 call, p.18) — a specific, checkable claim.
- Apex discloses it **sources components from competitors** — Ion Exchange, Thermax, and Pentair are named as component suppliers even while being described as competitors in certain segments (Q4 FY26 call, Anuj Dosajh, p.20). This is an unusually candid disclosure and internally consistent with the "integrator, not manufacturer" positioning management repeats across all three calls.
- **Filtra Engineers / Filtra Consultants** named as a distributor Apex sources some end products from (Q4 FY26 call, p.20-21).
- Regional/sector-specific competitors are acknowledged generically (e.g., an unnamed "Membrane and another company" competing for the Luminous order) but never named with specificity (Q4 FY25 call, p.9) — a gap for peer-stage follow-up.

### 3B. Industry and market intelligence dropped in the calls

- ZLD adoption in India cited as "only... single-digit percentages" of applicable industrial water use as of the Q4 FY25 call, with a claimed multi-decade runway (Anuj Dosajh, p.8) — an unverified but specific claim worth checking against independent industry data in stage 6/9.
- Recycling/reuse penetration cited even more conservatively later: "could be only 1% of the total industrial water being used for recycling and reuse" (Q4 FY26 call, Anuj Dosajh, p.18-19) — note this is a different (lower, narrower) figure than the ZLD "single digit %" claim from a year earlier; the two statistics are not the same metric but are used interchangeably in the growth narrative, which merits a peer check for consistency.
- Raw-material (metal) cost inflation of 25-40% attributed to "war and... geopolitical things" during H2 FY26 (Q4 FY26 call, Anuj Dosajh, p.10) — a sector-wide claim, checkable against peer commentary and metal price indices.
- Market consolidation thesis: "there could be a couple of lakh companies in this country doing this kind of water treatment," moving toward consolidation as customer ticket sizes grow (Q4 FY26 call, Anuj Dosajh, p.16-17) — explicitly hedged by management itself ("I don't know") and should be treated as a soft claim, not verified data.
- Jan Jeevan Mission-related government-sector receivable stress flagged by an analyst (not management) as a known industry issue Apex is insulated from due to low government-order exposure (Q2 FY26 call, Agastya Dave, p.10) — worth checking against peers with heavier government exposure.

### 3C. Toughest analyst questions across all three calls

| Question | Management response | Satisfactory? | Real risk? |
|---|---|---|---|
| Receivables tripling/spiking (Q4 FY25 call, multiple analysts) | Explained via Feb/March invoicing timing, 45-60 day standard terms, no bad-debt history | Reasonably satisfactory but never closed the loop with a later "receivables now at X" confirmation | Low-moderate — project-based billing lumpiness is structural, not necessarily a red flag, but the lack of follow-up data is a transparency gap |
| Order book reconciliation across years (Q4 FY26 call, Agastya Dave, Madhur Rathi) | Management could not reconcile its own historical order-book figures; CFO gave yet a third number | **Not satisfactory** | Moderate — doesn't affect the cash economics much given the short gestation period, but it is a real specificity/credibility issue for anyone modelling order-book-to-revenue conversion |
| Margin decline despite bigger ticket sizes (Q4 FY26 call, Agastya Dave) | Attributed to raw material and logistics cost spikes on already-committed fixed-price jobs | Satisfactory and specific | Real, ongoing risk — company is exposed to commodity price volatility on fixed-price contracts signed before input costs move |
| Customer concentration on Reliance/L&T (Q4 FY26 call, Rushwithnag, Shivam Mehra) | Reassurance without quantification | **Not satisfactory** | Real and material — a single customer relationship (Reliance) appears to represent a large share of FY26 execution; no diversification metric was ever offered |
| EPS growth (73.69% H2) lagging PAT growth (~106%) (Q4 FY26 call, Majid Ahmed) | Attributed to weighted-average share count changes, explicitly denied dilution | Adequately answered but under-explained (no detail on why weighted-average share count moved) | Low-moderate — worth a direct check against the share register in stage 3/8 |
| Whether H2 FY26 was a one-off vs. a new base (Q4 FY26 call, Keshav) | Non-numeric, hedged ("difficult to answer... in terms of numbers and certainty"), fell back to a generic "30-40% growth" framing | Not fully satisfactory | Real — investors cannot cleanly distinguish a structural step-change from lumpy large-order timing without more disclosure |

### 3D. Customer and order book signals

- **Wins**: Toyota (via L&T) ~₹40cr (FY25); Reliance Consumer Products ₹100-125cr, Bharatiyam Beverages ₹10-15cr, Pragati Power Corporation ₹3-5cr (all cited in H1/H2 FY26); CRD Food Products named as an additional FY26 win in the Q4 FY26 opening remarks without a size figure given.
- **Concentration**: shift from a diversified small-ticket base toward a small number of very large, blue-chip orders (Reliance being the standout) — a genuine structural change in the revenue mix versus FY25, flagged above as an unresolved question.
- **Renewals/repeat business**: management repeatedly emphasizes a "repeat orders from the same company" strategy, citing multi-factory clients (Luminous ~13-14 factories, Escorts ~10, Mahindra ~17) as a deliberate wedge strategy (Q4 FY25 call, Anuj Dosajh, p.16) — a specific, checkable claim about how the sales pipeline is built.
- **Geographic spread**: essentially India-only by the end of the period covered; international ambitions (Vietnam, Indonesia, Middle East) explicitly walked back by Q4 FY26.
- **Sector spread**: expanded from automobile-only (pre-COVID) to ~14 sectors (steel, pharma, beverages, food, FMCG, chemicals, etc.) — consistently repeated across all three calls with the same "14 sectors" figure, a point of internal consistency.
- **Pricing renegotiation**: no explicit renegotiation event disclosed; management states new orders are being priced to reflect higher input costs going forward (Q4 FY26 call, p.10), but does not disclose whether existing/spillover order-book pricing was renegotiated.

---

## SECTION 4: KEY TAKEAWAYS & TRIGGERS SUMMARY

### 4A. Investment-ready trigger list, ranked by earnings impact

| Priority | Trigger | Type | Timeframe | Conviction | Confirms it | Kills it |
|---|---|---|---|---|---|---|
| 1 | Reliance Consumer Products order execution (₹100-125cr, ~70% due in FY26/FY27) | Volume | Near | H | H2 FY26 already shows the bulk of this converting to revenue (148.65cr FY26 actual vs. prior guidance) | Any disclosed delay/dispute on the Reliance order, or a customer-concentration shock |
| 2 | Order-book-to-revenue conversion discipline (6-10 month gestation) | Volume | Near | H | Consistent delivery across FY25 and FY26 (order book has converted broadly as guided each period) | A slippage in the historically tight gestation window, or a repeat of the order-book-figure confusion seen in Q4 FY26 |
| 3 | ZLD/higher-margin mix shift | Price-mix | Medium | M | A disclosed, updated ZLD % of revenue with margin expansion attached | Continued margin compression despite bigger tickets (already seen once in H2 FY26) |
| 4 | Raw-material cost pass-through on new orders | Cost | Near | M | Stable or improving EBITDA margin in FY27 despite input cost volatility | Renewed margin compression blamed again on commodities without price-escalation clauses being adopted |
| 5 | Customer diversification beyond Reliance/L&T | Volume | Medium | L | A disclosed top-customer revenue concentration metric showing declining reliance | Continued non-disclosure plus a second mega-order from the same handful of clients |
| 6 | ESOP delivery | Cost/retention | Near (deadline already passed) | L | Any future disclosure that the ESOP was actually implemented | Continued silence — as of the Q4 FY26 call this trigger already shows signs of failure |
| 7 | International expansion (Vietnam/Indonesia) | Sectoral | Long | L | A first disclosed order or revenue contribution from outside India | Continued retreat to "India itself," as already stated in Q4 FY26 |
| 8 | Quarterly (or more frequent) financial disclosure | Governance | Near | L | A genuine move to numeric quarterly reporting, not just a percentage circular | Continued semi-annual-only reporting into FY27 |

### 4B. Questions for peer verification (formal handoff to stage 6)

- {question: "Is ZLD/water-recycling penetration in Indian industrial water use genuinely in the 'single-digit percent' to '~1%' range as management claims, and is this consistent across the two different figures management cited a year apart?", why: "This is the core TAM/runway thesis for the entire investment case; the two cited figures (single-digit % in Q4 FY25 call, ~1% in Q4 FY26 call) are not reconciled and may refer to different metrics conflated for effect.", check_peers: ["Ion Exchange", "Thermax", "Va Tech Wabag", "Concord"]}
- {question: "Did peer water-treatment EPC players also see 25-40% raw material (metal) cost inflation in H2 FY26, and how did they handle pricing on fixed-price contracts signed before the spike?", why: "Tests whether Apex's margin compression is an industry-wide, structural feature (lower company-specific risk) or company-specific execution/pricing weakness.", check_peers: ["Ion Exchange", "Thermax", "Va Tech Wabag", "Concord", "any listed steel/metal fabrication proxy for input cost trend"]}
- {question: "What is Apex's actual revenue concentration in the top 1/3/5 customers for FY26, and how does that compare to peer disclosure practices?", why: "Management has been asked this directly twice and never quantified it; a single order (Reliance) may represent a majority of FY26 revenue, which is a material concentration risk the company has not disclosed.", check_peers: ["Ion Exchange", "Thermax", "Va Tech Wabag"]}
- {question: "Is the 'market consolidation' claim (fragmented industry of small players consolidating around scaled players with larger ticket sizes) supported by any peer commentary or industry data, or is it an unsupported, self-admitted guess by Apex management?", why: "This underpins the bigger-ticket-order growth thesis; management itself hedged the 'couple of lakh companies' figure as a guess.", check_peers: ["Ion Exchange", "Thermax", "Va Tech Wabag", "Concord"]}
- {question: "Do peer companies report quarterly financials, and if SME-listed peers also fall under the same SEBI six-month disclosure carve-out, do any of them nonetheless provide voluntary interim (quarterly) updates the way Apex has only partially done (one percentage-only circular)?", why: "Tests whether the quarterly-reporting gap is an industry-wide SME feature (lower company-specific governance concern) or an Apex-specific communication discipline gap.", check_peers: ["other SME-listed water treatment / industrial EPC companies"]}

### 4C. Management quality verdict table

| Dimension | Assessment |
|---|---|
| Execution against numeric commitments (revenue/order book) | Strong — consistently met or exceeded stated guidance across all three periods, with FY26 numbers internally reconciling cleanly (H1 + H2 = FY total for revenue, EBITDA, and PAT) |
| Execution against qualitative/governance commitments (quarterly reporting, ESOP, H1/H2 skew) | Weak — three consecutive misses/partial misses, one (ESOP) delivered in complete silence |
| Transparency on bad news | Mixed-to-good — volunteers the Gulf expansion failure and raw-material cost pressure unprompted, a genuinely positive signal; but stays silent on the ESOP miss and never proactively revisits the reversed H1/H2 skew promise |
| Numerical consistency/specificity | Weak — order-book figures conflict across calls and management/CFO cannot reconcile them live on the call |
| Forward guidance discipline | Weak — declines to give numeric FY27 guidance even under direct, repeated analyst pressure, offering only a generic "30-40% growth" framing |
| **Overall grade** | **B** |

**Grading rationale**: the single most important test — whether management delivers on the numbers it commits to — is a clear pass, with FY26 results materially exceeding the conservative growth language set in the Q4 FY25 call, and FY26 H1/H2 figures reconciling cleanly to the full-year total (no red flag on the core financial narrative). This keeps the grade out of C/D territory. However, credibility is held back from an A by a cluster of governance/communication failures that recur across all three calls: chronic non-delivery of the repeatedly-promised quarterly reporting (2E), a silently dropped ESOP commitment with a specific missed deadline, an order-book figure that management itself cannot reconcile across calls, and forward guidance that stays deliberately non-numeric even when directly pressed. This is "Good, not Excellent" — a B.

### 4D. Concall red flags with severity

| Flag | Severity | Evidence |
|---|---|---|
| ESOP promise (specific deadline: end of FY26) silently dropped, zero mention in the FY26 year-end call | Medium | Q2 FY26 call, Anuj Dosajh, p.13 (promise) vs. Q4 FY26 call transcript (no mention at all) |
| Order-book figures cannot be reconciled across calls — three different numbers offered for the same historical reference point (55cr, 62cr, and an unbridged 145-to-125 sequence) | Medium | Q4 FY26 call, Agastya Dave / Anuj Dosajh / Rakesh Kaul exchange, p.8, and Madhur Rathi exchange, p.17-18 |
| Chronic non-delivery of quarterly reporting despite three consecutive, repeated analyst requests across all three calls | Medium | Section 2E |
| H1/H2 revenue-skew reduction explicitly promised, then result moved in the opposite direction, with no proactive acknowledgment | Low-Medium | Q4 FY25 call, Anuj Dosajh, p.17 vs. FY26 actuals (₹32.56cr H1 / ₹116.08cr H2) |
| Undisclosed customer concentration — a single order (Reliance) plausibly represents a majority of FY26 execution, never quantified despite being asked twice | Medium | Section 2D, 3C |
| Inconsistent characterization of the Veolia relationship — from "strategic alliance... deepened" and "strong collaboration" to an explicit "not in any partnership, any JV" disclaimer | Low | Q4 FY25 call p.3, Q2 FY26 call p.4, vs. Q4 FY26 call p.19 |
| Data-quality flag (not a management credibility issue): the Q4 FY25 call transcript states H2 FY25 EBITDA as "₹8927.78 lakhs, up 331.85%," which is arithmetically inconsistent with the same call's stated FY25 full-year EBITDA of ₹1105.67 lakhs (H2 cannot exceed the full year by 8x). This is very likely a transcription or verbal slip in the source PDF, not a deliberate misstatement, but it means the H2 FY25 EBITDA and its 331.85% growth figure should NOT be used downstream without independent verification against the audited results PDF. | Low (data quality, not credibility) | Q4 FY25 call, Anuj Dosajh, p.3 |

---

## INPUT GAPS CARRIED FORWARD

- No credit rating PDF was provided for this run.
- No shareholding pattern / pledge data was provided for this run.

These gaps do not originate in this stage but are carried forward per pipeline instruction.

---

```yaml
stage: B05-concall
company: "APEXECO"
run_date: "2026-07-10"
model: claude-sonnet-5
status: complete
input_gaps:
  - {type: rating, detail: "no credit rating PDF"}
  - {type: shareholding, detail: "no shareholding pattern / pledge data"}
flags:
  - "Transcripts are semi-annual (H1/H2) calls, not discrete quarterly calls, despite the injected quarter map labelling them Q4 FY25 / Q2 FY26 / Q4 FY26 — figures are period-anchored to their true H1/H2 basis throughout this report"
  - "Q4 FY25 call transcript states H2 FY25 EBITDA (INR8927.78 lakhs, +331.85%) inconsistent with the same call's FY25 full-year EBITDA (INR1105.67 lakhs) — likely a transcription/verbal error in the source document; do not use H2 FY25 EBITDA downstream without independent verification"
  - "Order book figures cannot be reconciled by management across the three calls (55cr vs 62cr vs 145cr vs 125cr for overlapping reference points)"
  - "Customer concentration (Reliance order plausibly majority of FY26 revenue) never quantified despite being asked twice"
quarters_analysed: ["Q4 FY25", "Q2 FY26", "Q4 FY26"]
triggers:
  - {priority: 1, name: "Reliance Consumer Products order execution", type: "volume", timeframe: "near", conviction: "H", confirm_signal: "Continued on-schedule conversion of the ~INR100-125cr Reliance order into revenue with no dispute/delay disclosed", kill_signal: "Disclosed delay, dispute, or scope-cut on the Reliance order, or a customer-concentration shock"}
  - {priority: 2, name: "Order-book-to-revenue conversion discipline (6-10 month gestation)", type: "volume", timeframe: "near", conviction: "H", confirm_signal: "FY27 revenue continues to track disclosed order book within the historical gestation window", kill_signal: "A slippage in the gestation window or a repeat of the order-book-figure confusion seen in the Q4 FY26 call"}
  - {priority: 3, name: "ZLD / higher-margin mix shift", type: "price-mix", timeframe: "medium", conviction: "M", confirm_signal: "A disclosed, updated ZLD percent of revenue paired with margin expansion", kill_signal: "Continued margin compression despite bigger ticket sizes"}
  - {priority: 4, name: "Raw-material cost pass-through on new orders", type: "cost", timeframe: "near", conviction: "M", confirm_signal: "Stable or improving EBITDA margin in FY27 despite input cost volatility", kill_signal: "Renewed margin compression blamed again on commodities with no price-escalation clauses adopted"}
  - {priority: 5, name: "Customer diversification beyond Reliance/L&T", type: "volume", timeframe: "medium", conviction: "L", confirm_signal: "Disclosed top-customer revenue concentration metric showing declining reliance", kill_signal: "Continued non-disclosure plus a second mega-order concentrated in the same handful of clients"}
  - {priority: 6, name: "ESOP delivery for core team", type: "cost", timeframe: "near (deadline already passed)", conviction: "L", confirm_signal: "Future disclosure confirming the ESOP was implemented", kill_signal: "Continued silence on the ESOP commitment"}
  - {priority: 7, name: "International expansion (Vietnam/Indonesia)", type: "sectoral", timeframe: "long", conviction: "L", confirm_signal: "A first disclosed order or revenue contribution from outside India", kill_signal: "Continued retreat to India-only focus as stated in the Q4 FY26 call"}
  - {priority: 8, name: "Quarterly (or more frequent) financial disclosure", type: "regulatory-policy", timeframe: "near", conviction: "L", confirm_signal: "A genuine move to numeric quarterly reporting, not just a percentage-only circular", kill_signal: "Continued semi-annual-only reporting into FY27"}
guidance:
  - {item: "Opening order book", number: "INR55 crore or more", timeframe: "start of FY26", stated_in: "Q4 FY25 call"}
  - {item: "Minimum revenue growth expectation", number: "at least ~25%", timeframe: "FY26", stated_in: "Q4 FY25 call"}
  - {item: "Order book (mid-year)", number: "INR145 crore (incremental to already-billed INR32.56cr H1)", timeframe: "as of Nov 2025", stated_in: "Q2 FY26 call"}
  - {item: "Reliance Consumer Products order", number: "INR100-125 crore, ~70% to execute within FY26", timeframe: "FY26", stated_in: "Q2 FY26 call"}
  - {item: "Bharatiyam Beverages order", number: "INR10-15 crore", timeframe: "FY26", stated_in: "Q2 FY26 call"}
  - {item: "Pragati Power Corporation order", number: "INR3-5 crore", timeframe: "FY26", stated_in: "Q2 FY26 call"}
  - {item: "ESOP for core employees", number: "amount not disclosed", timeframe: "by end of FY26", stated_in: "Q2 FY26 call"}
  - {item: "FY26 actual revenue", number: "INR148.65 crore, +109.5% YoY", timeframe: "FY26 (delivered)", stated_in: "Q4 FY26 call"}
  - {item: "FY26 actual EBITDA", number: "INR21.76 crore, +96.82% YoY", timeframe: "FY26 (delivered)", stated_in: "Q4 FY26 call"}
  - {item: "FY26 actual PAT", number: "INR17.02 crore, +98.85% YoY", timeframe: "FY26 (delivered)", stated_in: "Q4 FY26 call"}
  - {item: "FY26 actual EPS", number: "12.91, +63.21% YoY", timeframe: "FY26 (delivered)", stated_in: "Q4 FY26 call"}
  - {item: "Cash and bank balance", number: "INR35.06 crore", timeframe: "as of 31-Mar-2026", stated_in: "Q4 FY26 call"}
  - {item: "Working capital", number: "INR61.72 crore", timeframe: "as of 31-Mar-2026", stated_in: "Q4 FY26 call"}
  - {item: "Closing order book", number: "INR125 crore or more", timeframe: "as of 31-Mar-2026, spillover into FY27", stated_in: "Q4 FY26 call"}
  - {item: "FY27 growth guidance", number: "verbal, non-numeric: 30-40% growth overall", timeframe: "FY27", stated_in: "Q4 FY26 call"}
  - {item: "Raw material (metal) cost inflation absorbed", number: "25-40% increase", timeframe: "H2 FY26", stated_in: "Q4 FY26 call"}
promise_delivery:
  delivered: 3
  partial: 2
  missed: 3
  rows:
    - {promised_in: "Q4 FY25 call", promise: "Revenue growth at least ~25% for FY26", outcome: "delivered", explanation: "FY26 revenue grew 109.5% YoY, vastly exceeding the floor guidance"}
    - {promised_in: "Q4 FY25 call", promise: "Order book (INR55cr+) will convert to revenue within the year via the 6-10 month gestation cycle", outcome: "delivered", explanation: "Consistently explained and delivered across both FY25 and FY26"}
    - {promised_in: "Q4 FY25 call", promise: "Narrow the H1/H2 revenue skew (from a 30-70 split) toward a steadier year-round cadence", outcome: "missed", explanation: "FY26 actual split was roughly 22/78 (H1 INR32.56cr / H2 INR116.08cr), more skewed than before; not proactively acknowledged"}
    - {promised_in: "Q4 FY25 call", promise: "Move to quarterly reporting from subsequent quarters", outcome: "partial", explanation: "Only a percentage-only, non-numeric circular was issued at Q3 FY26; full quarterly financials still not delivered across all three calls"}
    - {promised_in: "Q2 FY26 call", promise: "ESOP for core people by the end of FY26", outcome: "missed", explanation: "Zero mention in the Q4 FY26 (FY26 year-end) call; no explanation offered"}
    - {promised_in: "Q2 FY26 call", promise: "ZLD mix and bigger ticket sizes will be margin accretive", outcome: "partial", explanation: "Margins declined YoY in H2 FY26 due to raw-material and logistics cost inflation; original accretion claim not reconciled against the actual result"}
    - {promised_in: "Q2 FY26 call", promise: "International expansion into Vietnam/Indonesia/Middle East", outcome: "missed", explanation: "Gulf effort explicitly abandoned by the Q4 FY26 call, with a rare honest admission of failure; focus retreated to India-only"}
    - {promised_in: "Q2 FY26 call", promise: "Order book of INR145 crore as of Nov-2025 will convert cleanly", outcome: "partial", explanation: "Q4 FY26 closing order book of INR125cr could not be cleanly bridged from the 145cr figure; management and CFO gave conflicting historical order-book numbers on the same call"}
excuse_pattern: "balanced"
repeated_evasions:
  - {question: "Please consider quarterly (or at least one-paragraph, more frequent) financial reporting; six months is too large a gap", quarters_asked: ["Q4 FY25", "Q2 FY26", "Q4 FY26"], classification: "answer changed between quarters — from outright deferral, to an unfulfilled repeat of the same promise, to a partial percentage-only (non-numeric) delivery that still falls short of the original request"}
credibility_grade: "B"
credibility_basis: "Core numeric commitments (revenue growth, order-book conversion) were consistently met or exceeded across all three periods with clean FY26 internal reconciliation, but governance/communication commitments (quarterly reporting, ESOP, H1/H2 skew reduction, order-book number consistency, forward guidance specificity) show a recurring pattern of misses and unreconciled figures."
peer_questions:
  - {question: "Is ZLD/water-recycling penetration in Indian industrial water use genuinely in the 'single-digit percent' to '~1%' range as management claims, and are the two different figures cited a year apart (Q4 FY25 vs Q4 FY26 calls) actually the same metric?", why: "This is the core TAM/runway thesis for the investment case and the two cited figures are not reconciled by management.", check_peers: ["Ion Exchange", "Thermax", "Va Tech Wabag", "Concord"]}
  - {question: "Did peer water-treatment EPC players also see 25-40% raw material (metal) cost inflation in H2 FY26, and how did they handle pricing on fixed-price contracts signed before the spike?", why: "Tests whether Apex's margin compression is industry-wide (lower company-specific risk) or company-specific.", check_peers: ["Ion Exchange", "Thermax", "Va Tech Wabag", "Concord"]}
  - {question: "What is Apex's actual revenue concentration in the top 1/3/5 customers for FY26, and how does that compare to peer disclosure practices?", why: "Management was asked directly twice and never quantified this; a single order (Reliance) may represent a majority of FY26 revenue.", check_peers: ["Ion Exchange", "Thermax", "Va Tech Wabag"]}
  - {question: "Is the 'market consolidation' claim (fragmented industry consolidating around scaled players with larger ticket sizes) supported by any peer commentary or industry data, given management itself hedged it as a guess?", why: "This underpins the bigger-ticket-order growth thesis central to the FY27 guidance narrative.", check_peers: ["Ion Exchange", "Thermax", "Va Tech Wabag", "Concord"]}
  - {question: "Do SME-listed peers under the same SEBI six-month disclosure carve-out nonetheless provide voluntary interim (quarterly) updates, the way Apex has only partially done with one percentage-only circular?", why: "Tests whether the quarterly-reporting gap is an industry-wide SME feature or an Apex-specific governance/communication gap.", check_peers: ["other SME-listed water treatment / industrial EPC companies"]}
red_flags:
  - {flag: "ESOP promise (specific deadline: end of FY26) silently dropped, zero mention in the FY26 year-end call", severity: "medium"}
  - {flag: "Order-book figures cannot be reconciled by management across calls (55cr vs 62cr vs 145cr vs 125cr for overlapping reference points)", severity: "medium"}
  - {flag: "Chronic non-delivery of quarterly reporting despite three consecutive, repeated analyst requests across all three calls", severity: "medium"}
  - {flag: "H1/H2 revenue-skew reduction explicitly promised, then result moved in the opposite direction, with no proactive acknowledgment", severity: "low-medium"}
  - {flag: "Undisclosed customer concentration — a single order (Reliance) plausibly represents a majority of FY26 execution, never quantified despite being asked twice", severity: "medium"}
  - {flag: "Inconsistent characterization of the Veolia relationship across calls (from 'strategic alliance deepened' to an explicit 'not in any partnership, any JV')", severity: "low"}
  - {flag: "Data-quality issue in the Q4 FY25 call transcript: H2 FY25 EBITDA figure (INR8927.78 lakhs) is arithmetically inconsistent with the same call's stated FY25 full-year EBITDA (INR1105.67 lakhs); likely a transcription/verbal error, not a management misstatement, but should not be used downstream without independent verification", severity: "low (data quality, not credibility)"}
dropped_triggers:
  - "International expansion (Bangladesh, then Vietnam/Indonesia/Middle East) — Gulf effort explicitly abandoned by the Q4 FY26 call, focus retreated to India-only"
  - "ESOP for core team — promised with a specific deadline (end of FY26), zero mention thereafter"
timeline_slippages:
  - "Quarterly (or more frequent) financial reporting — promised 'from subsequent quarters' in the Q4 FY25 call, still not fully delivered by the Q4 FY26 call three periods later, only a partial percentage-only circular issued"
  - "H1/H2 revenue skew reduction — promised to narrow in the Q4 FY25 call, actually widened by FY26"
```
