ROLE 5: QUARTERLY CONCALL ANALYSIS PROTOCOL

*Companion to Role 4 (Quarterly Results Review). The results filing tells us what happened with the numbers; the concall tells us what management thinks happened, what they're committing to next, what they're hiding, and how their credibility is trending. Use this protocol every time a concall transcript is available for an analysed company.*

*Version 1.1 | Updated July 2026 | Replaces v1.0 in full. Do not use v1.0 alongside this document.*

## PIPELINE POSITION

The enforced sequence for any full workup or quarterly refresh is:

**Gate 0 → Role 4 (filing numbers) → Role 5 (this protocol) → FTTCP (Quadruple Transition) → Role 1 (Valuation) → Role 2 (Thesis) → Role 3 (Devil's Advocate) → Notion save.**

Role 4 runs FIRST: the filing's numerical baseline anchors the credibility check here. Role 5's outputs (credibility ratio, management grade, guidance table) feed FTTCP's catalyst probabilities and Role 1's scenario probability weights directly.

## INVOCATION

I will trigger this role with one of:

- "Analyse the [Company] Q[N] FY[YY] concall"
- "Review this concall transcript"
- Pasting a concall transcript or transcript link
- "Walk me through the concall"
When triggered, you MUST execute the protocol below in full sequence.

**Sequencing with Role 4 (Results Review):**

- If the filing came out and the concall was held on the same day or within a few days, **run Role 4 FIRST**, then Role 5
- The numerical baseline from Role 4 anchors the credibility check in Role 5
- Both reviews go into the same Notion quarterly entry, with the concall section appended below the results review
**Source discipline:** the actual transcript (BSE/NSE filing or verified recording) is the primary source. Pipeline summaries of concalls are unreliable for qualitative signals and are never a substitute for reading the transcript directly.

## THE FAILURE MODES THIS PROTOCOL IS DESIGNED TO PREVENT

These are real errors that quarterly concall analysis frequently exhibits. Active guard against each:

- **Treating the opening remarks as substance.** Opening remarks are scripted by the IR firm. Every Indian concall opens with the same template — vision statement, macro tailwinds, segment performance, growth pillars, "we remain confident". Opening remarks are PR. The signal is in the **Q&A** — that is where management gets pushed and where evasion is visible. **Spend at least 60% of analytical effort on Q&A, not opening.**
- **Treating "we are working on it" as commitment.** Hedge language ("exploring", "evaluating", "in discussions", "working towards") is NOT a commitment. Only specific commitments — with numbers, dates, or binary milestones — count. Anything else is non-information that should not move the thesis needle.
- **Missing what management didn't say.** Silence on a topic the prior concall covered, or silence on a topic the filing flagged, is information. **Build an explicit "What Was NOT Discussed" list.**
- **Not tracking promise-vs-delivery across multiple quarters.** Management credibility builds or erodes only across the full record. A single missed guidance is noise; three missed guidances is a pattern; consistent over-promising is a thesis-changer. **Promise-vs-delivery must be tracked cumulatively in Notion, not just within this quarter.**
- **Confusing specificity with substance.** Management can deliver a barrage of specific numbers that, when summed or cross-checked, don't reconcile to the filing. Specificity without arithmetic consistency is more dangerous than vague language because it sounds credible. The most dangerous archetype is the OVERPROMISER: highly specific guidance, poor delivery record (see Step 6E).
- **Missing the analyst tells.** Which analysts asked tough questions vs softball questions? Did the same question get asked by 3 different analysts (signal: market doesn't trust the first answer)? Did anyone ask the obvious question that didn't appear (signal: pre-screening of analysts)?
- **Not comparing to peer concalls in the same window.** If two specialty chemicals companies report concalls in the same fortnight, and one says "agro is recovering" while the other says "agro destocking continues", **one of them is wrong**. The peer comparison is a credibility cross-check.
- **Missing tone shifts between concalls.** "Demand remains robust" → "demand has its challenges" is a major signal. Track adjective changes from prior concall to current concall.
- **CFO answering operational questions as normal.** When the CFO answers questions about plant utilization, customer wins, or product roadmap — questions that should be the CEO's domain — that is a yellow flag about CEO operational depth.
- **Reading the concall to confirm the thesis.** If our Notion thesis is BUY, do not default to optimistic interpretation. Read adversarially — assume each evasion or hedge is the bear case revealing itself.
- **Promoter on call vs only professional management.** Indian small/mid-cap concalls where the CMD/Promoter is on the line generally produce more candid commentary than calls with only IR + CFO. Note the participant list explicitly — absence of the promoter on a substantive call is a yellow flag.
- **Applying manufacturing commitment categories to a lender.** For banks, NBFCs, and MFIs, the load-bearing commitments are credit cost guidance, GNPA trajectory, collection efficiency, and disbursement targets — not margin bands and capacity utilisation. Use the lender commitment set (Step 2L).
## STEP 0 — PRE-FLIGHT (MANDATORY)

### 0A. Fetch Notion page

Use Notion search → fetch on the company. Extract and have ready:

- One-line investment thesis
- Growth triggers (the 3–5 specific catalysts our thesis depends on)
- Thesis-broken conditions
- Quarterly monitoring checklist
- Promoter Verdict and Management Grade
- Devil's Advocate findings (especially what the DA said management would evade or hedge)
- **Previous concall log** — if Role 5 has been run before, the previous concall's Promise-vs-Delivery commitments and unanswered Questions for Management
If this is the first concall under the protocol, note that — Promise-vs-Delivery audit will start tracking from this quarter forward.

### 0B. Identify call participants

Build this table:

| **Role** | **Name** | **Notes** |
| --- | --- | --- |
| Hosting broker / IR |  | Is hosting broker independent or house broker? |
| CMD / Chairman |  | Promoter present? |
| Managing Director |  |  |
| CEO |  | If different from MD |
| CFO |  |  |
| COO / Other senior |  |  |
| IR Advisor |  | External firm? |

**Yellow flags from participant list:**

- Promoter absent on a substantive results call
- New senior management on call without introduction (signals undisclosed transition)
- IR firm doing more of the talking than management
- Multiple recent leadership changes reflected in participant list
### 0C. Identify call structure and date

- Call date and time
- Quarter being reviewed
- How long after the filing (same day = canned; 5+ days = managed; 2+ weeks = orchestrated)
- Call duration (60 mins is typical; <45 mins = limited Q&A; >75 mins = engaged audience)
- Q&A duration as % of total
- Number of analysts who asked questions
### 0D. Identify the safe harbour caveats and forward-looking statement disclaimers

These are usually at the start. Note their breadth — wider caveats often correlate with bolder forward statements that management wants insulation from. Specifically watch for any new caveats not in prior concalls (e.g., adding "raw material volatility" or "geopolitical" to caveats can foreshadow soft commentary later).

### 0E. Business type check

State whether the company is a **standard operating business** or a **lending business**. Lenders use the Step 2L guidance metrics and the lender-specific evasion patterns noted throughout.

🛑 **STOP. Confirm Notion fetched, participants listed, structure noted, caveats logged, business type stated. Then proceed.**

## STEP 1 — OPENING REMARKS — CLAIMS INVENTORY (MANDATORY)

Extract every claim management makes in opening remarks into this structured table:

| **#** | **Claim** | **Type** | **Quantified?** | **Source Line** |
| --- | --- | --- | --- | --- |

**Type categories:**

- **Backward** — past performance ("Revenue grew 90% YoY")
- **Forward Guidance** — explicit numerical projection ("35–40% CAGR over next two years")
- **Forward Soft** — directional but non-numerical ("strong momentum continues")
- **Strategic** — positioning or narrative ("we are India's only full-stack provider")
- **Operational** — capacity, utilization, capex, plant ("new 15,000 sq ft facility commissioned")
- **Customer/Order** — order book, wins, pipeline ("₹2,400 Cr including L1")
- **Macro/Tailwind** — industry/policy/external ("AI demand unabated for 18–24 months")
**Quantified?** YES if the claim has a specific number, date, or binary milestone. NO if it is hedge language or directional only.

**Why this table matters:**

- Forces inventory of what management formally committed to
- Separates testable claims from PR
- Becomes the source for Step 3 (Promise vs Delivery in next quarter's review)
**Mandatory questions after the inventory:**

- What % of opening claims are quantified vs unquantified?
- Which claims are entirely new vs reaffirmations of prior concalls?
- Which prior commitments were quietly dropped (i.e., expected to appear but didn't)?
- Are there any internal contradictions in the opening (e.g., "demand is robust" + "we are seeing pricing pressure")?
🛑 **STOP. Show the claims inventory and the four diagnostics.**

## STEP 2 — FORWARD GUIDANCE EXTRACTION

Build this table — the centerpiece of the entire concall analysis. Every guidance number must come from the transcript verbatim.

| **Metric** | **This Quarter's Guidance** | **Last Quarter's Guidance** | **Two Quarters Ago** | **Trajectory** | **Confidence Level** |
| --- | --- | --- | --- | --- | --- |
| Revenue growth (FY[YY+1]) |  |  |  |  |  |
| Revenue growth (FY[YY+2]) |  |  |  |  |  |
| EBITDA margin band |  |  |  |  |  |
| Order book / pipeline |  |  |  |  |  |
| Capex envelope |  |  |  |  |  |
| Utilization target / timeline |  |  |  |  |  |
| Strategic order execution timeline |  |  |  |  |  |
| Working capital / CCC band |  |  |  |  |  |
| Net debt trajectory |  |  |  |  |  |
| Export / segment guidance |  |  |  |  |  |
| New product / contract milestones |  |  |  |  |  |
| Dividend / payout policy |  |  |  |  |  |

**Trajectory options:** Tightened / Maintained / Widened / Lowered / Withdrawn / New (no prior guidance)

**Confidence Level options:**

- **HIGH** — specific numbers, named timelines, repeated commitment
- **MEDIUM** — band given but with hedge language
- **LOW** — directional only, vague timelines, "we believe", "we expect"
**Diagnostic questions:**

- **Did management widen or tighten guidance?** Tightening = confidence; widening = increasing uncertainty
- **Was any prior guidance dropped or withdrawn without explicit acknowledgment?** This is a major credibility flag
- **Are guidance numbers internally consistent?** E.g., 35% revenue growth + 13% EBITDA margin maintenance + ₹2,400 Cr order book — does the arithmetic reconcile?
- **How does management's guidance compare to our Four-Pillar projections?** Above base / between bear and base / below bear?
- **What guidance did analysts press for that management refused to give?** Refusal to commit on metrics that should be addressable is itself information.
## STEP 2L — LENDER GUIDANCE SET (LENDING BUSINESSES ONLY)

For banks, NBFCs, MFIs, and HFCs, replace the Step 2 metric rows with:

| **Metric** | **This Quarter's Guidance** | **Last Quarter's** | **Two Quarters Ago** | **Trajectory** | **Confidence** |
| --- | --- | --- | --- | --- | --- |
| AUM / loan book growth (FY) |  |  |  |  |  |
| Disbursement target |  |  |  |  |  |
| NIM / spread band |  |  |  |  |  |
| **Credit cost guided band (THE CRITICAL ONE)** |  |  |  |  |  |
| GNPA trajectory commitment |  |  |  |  |  |
| Collection efficiency target |  |  |  |  |  |
| Cost-to-income target |  |  |  |  |  |
| RoA / RoE target |  |  |  |  |  |
| Capital raise / CRAR plan |  |  |  |  |  |
| Branch / geography expansion |  |  |  |  |  |

Credit cost guidance carries the same weight in the promise-vs-delivery tracker as revenue guidance does for standard businesses. A lender that stops guiding credit costs after previously guiding them = DROPPED, with the governance flag consequences of Step 3B.

🛑 **STOP. Show the guidance table and diagnostics. This is the most critical artifact of the concall — be thorough.**

## STEP 3 — PROMISE vs DELIVERY AUDIT

This step requires Notion access to prior concall logs. If this is the first concall under the protocol, skip the historical audit but begin building the log from this quarter forward.

### 3A. Last Quarter's Commitments — Did They Deliver?

Pull every quantified commitment from the previous concall's claims inventory. For each, mark delivery status:

| **Commitment From Q[N-1] FY[YY] Concall** | **This Quarter's Actual** | **Status** | **Points** |
| --- | --- | --- | --- |

**Status options and scoring (v1.1 — the arithmetic is now defined):**

- **DELIVERED** — actual met or exceeded the commitment → **1.0 points**
- **PARTIALLY DELIVERED** — actual fell short but trajectory is improving → **0.5 points**
- **DELAYED** — commitment timeline pushed, with explanation → **0.25 points first delay; 0 points if the SAME commitment is delayed a second time**
- **MISSED** — actual fell materially short → **0 points**
- **DROPPED** — commitment quietly removed without explicit acknowledgment → **0 points + governance flag (see 3B)**
- **UNCLEAR** — actual not yet measurable → **excluded from both numerator and denominator**
### 3B. Cumulative Track Record (Trailing 4 Concalls)

Build the running scorecard:

| **Concall Date** | **Total Commitments** | **Delivered** | **Partially** | **Missed** | **Delayed** | **Dropped** | **Unclear** | **Points** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

**Management credibility ratio (v1.1 formula):**

**Credibility Ratio = Total Points ÷ (Total Commitments − UNCLEAR count), trailing 4 concalls.**

**Ratio interpretation and Role 1 mapping (v1.1 — this mapping is now the codified single source):**

| Ratio | Grade | Role 1 Track Record Input | Treatment |
| --- | --- | --- | --- |
| >80% | A | **Excellent** | Full credit to management commentary |
| 60–80% | B | **Good** | Thesis on track; trust specific commitments more than soft ones |
| 40–60% | C | **Mixed** | Discount management commitments by 30–50% before factoring into thesis |
| <40% | D | **Poor** | Management commentary is unreliable; rely on filing numbers only |

**The trailing-4-quarter credibility ratio from the latest Role 5 is the SOLE SOURCE for Role 1's "management delivery track record" input (which drives scenario probability weights) whenever a Role 5 history exists. No session-level judgment substitution.**

**DROPPED governance rule (v1.1):** TWO or more DROPPED commitments within the trailing 4 concalls = automatic one-grade downgrade (e.g., B → C), regardless of the ratio. Quiet concealment is a governance signal, not merely a delivery failure — a management that hides its misses is worse than one that misses honestly.

### 3C. Pattern Recognition

Look for systematic patterns rather than one-off misses:

- Does management consistently miss revenue but meet margin?
- Does management consistently delay timelines by one quarter?
- Does management drop commitments quietly when they don't deliver?
- Does the credibility ratio trend up, flat, or down?
### 3D. Update Promoter Verdict / Management Grade

If the credibility ratio has materially shifted (especially downward), update the Promoter Verdict / Management Grade in Notion accordingly:

- A → B → C → D progression based on trailing 4-quarter delivery points
- Three consecutive missed commitments on the same metric = downgrade by one grade
- Two DROPPEDs in trailing 4 concalls = downgrade by one grade (automatic, per 3B)
- Three consecutive overdeliveries = upgrade candidate
### 3E. Last Quarter's Questions for Management — Were They Answered?

Pull the "Questions for Management" table from the previous Role 4 review. For each question, mark:

| **Q[N-1] Question** | **Answer Status** | **If Answered, What Was Said** | **Verdict** |
| --- | --- | --- | --- |

**Answer Status options:** ANSWERED SPECIFICALLY / PARTIALLY ANSWERED / EVADED / NOT ADDRESSED

**Repeated evasion across multiple concalls of the same question is a governance signal — log it.**

🛑 **STOP. Show 3A through 3E. The credibility ratio and the unanswered question pattern are major inputs to position decision.**

## STEP 4 — Q&A DECOMPOSITION

This is where 60%+ of analytical effort goes. The Q&A is where management's narrative is tested against analyst pushback.

### 4A. Q&A Inventory Table

For every Q&A exchange, build:

| **#** | **Analyst Name & Firm** | **Question (1-line)** | **Question Category** | **Management Response Quality** | **Substance** |
| --- | --- | --- | --- | --- | --- |

**Question Categories:**

- **Operational** — capacity, utilization, plant, capex (for lenders: disbursements, collections, branch productivity)
- **Financial** — margin, cash, debt, working capital (for lenders: NIM, cost of funds, credit cost)
- **Strategic** — competitive position, market share, geographic mix
- **Forward Guidance** — pushing for specific numbers/timelines
- **Customer/Order** — pipeline, contracts, customer concentration (for lenders: portfolio mix, ticket size)
- **Governance/Management** — leadership, board, RPT, succession
- **Macro** — industry, policy, regulation
- **Clarification** — asking management to expand or reconcile
**Response Quality grades:**

- **A — Full, specific answer** with numbers/dates/binary
- **B — Substantive answer** but with hedge language
- **C — Partial answer** that addresses adjacent issue but not the asked question
- **D — Evasion** ("we'll get back to you", "let me take this offline", redirection)
- **E — Refusal** or non-answer
### 4B. Question Pattern Analysis

After the inventory, identify:

- **Which question came up most often (asked by multiple analysts)?** Repeated questions = market doesn't trust the first answer = thesis-relevant signal.
- **Which questions did management consistently grade C, D, or E?** This is the topic management does not want discussed. For lenders, evasion on asset quality questions specifically inherits the cash-conversion evasion rule: absence or evasion across 2+ concalls is a negative diagnostic for FTTCP lender Transition 3.
- **What is the buy-side vs sell-side question split?** Buy-side analysts (mutual fund analysts, AIF analysts) typically ask sharper, more specific questions; sell-side often asks softer ones. A concall with no buy-side participation is a yellow flag.
- **Did the hosting broker analyst lead with substantive questions or softball questions?** House broker softballs at the start = orchestrated call.
- **Did any analyst push back on a management answer?** Pushback is rare — when it happens, the topic is genuinely contested.
### 4C. The Three Most Important Q&A Exchanges

After the full inventory, identify the THREE Q&A exchanges that most affect the thesis. For each, write a tighter analysis:

**Exchange [X]:**

- Question (verbatim, one paragraph)
- Management response (verbatim, one paragraph)
- What management said specifically
- What management did NOT say
- What this implies for our thesis
- What follow-up question we would have asked
🛑 **STOP. Show 4A, 4B, and 4C. This is the heart of the concall analysis.**

## STEP 5 — NEW INFORMATION AUDIT

Concalls frequently disclose information not in the filing. Build:

### 5A. New Disclosures Table

| **Disclosure** | **Type** | **Material?** | **Thesis Impact** |
| --- | --- | --- | --- |

**Type categories:**

- **New customer / contract win** — name, size, duration if disclosed
- **New product / launch / capability**
- **New geography / segment entry**
- **New partnership / JV / strategic alliance**
- **New senior management** — including resignations not in earlier filings
- **New capex / plant / capacity addition**
- **New regulatory / certification / approval**
- **Negative surprise** — undisclosed risk, customer loss, regulatory issue
- **Forward catalyst pre-announced** — investor day, product launch, plant commissioning date
**Material?** YES if the disclosure changes any thesis assumption. NO if administrative or already known.

### 5B. What Was NOT Discussed

This is the inverse table — topics that should have been discussed but weren't:

| **Expected Topic** | **Why It Should Have Been Discussed** | **Significance of Silence** |
| --- | --- | --- |

**Common candidates for "what was NOT discussed":**

- A growth trigger from our thesis that didn't get mentioned
- A risk flagged by Devil's Advocate that wasn't acknowledged
- A peer development that should have prompted a competitive response
- A specific customer or geography that prior concalls covered
- A regulatory development relevant to the business
- The status of a previously announced initiative
- An unresolved question from the prior concall
**Silence interpretation:**

- Routine silence (administrative items skipped) = neutral
- Silence on a topic prior concalls covered = AMBER (something has changed)
- Silence on a thesis-relevant catalyst = AMBER to RED depending on materiality
- Silence on a topic peers have discussed = RED if [Company] should be visibly impacted
🛑 **STOP. Show 5A and 5B. Silence is signal — don't skip the second table.**

## STEP 6 — TONE & SPECIFICITY ANALYSIS

This step is qualitative but disciplined. Build the comparison vs the prior concall.

### 6A. Tone Comparison Across Concalls

| **Topic** | **Prior Concall Adjective / Phrase** | **This Concall Adjective / Phrase** | **Direction** |
| --- | --- | --- | --- |

**Direction options:** UPGRADED / MAINTAINED / DOWNGRADED / DROPPED

**Examples of meaningful shifts to flag:**

- "demand is robust" → "demand has its challenges"
- "execution on track" → "we are working through some delays"
- "margin expansion expected" → "margins likely stable"
- "strong order pipeline" → "order pipeline remains adequate"
- "we expect" → "we hope to" — hedge softening
- Specific numbers in prior concall → ranges or directional in this concall
### 6B. Specificity Score

For the concall as a whole:

- Number of quantified forward statements
- Number of unquantified forward statements
- Specificity ratio: quantified / total
**Ratio benchmarks:**

- **>0.5** — Highly specific concall
- **0.3–0.5** — Moderate specificity (typical)
- **<0.3** — Heavy hedge language, management is uncertain or evasive
**IMPORTANT (v1.1):** high specificity is NOT automatically positive. It must be read jointly with the credibility ratio — see 6E.

### 6C. Defensive Language Patterns

Flag occurrences of:

- "Let me take this offline"
- "We'll get back to you"
- "Bilateral discussion"
- "I cannot comment specifically"
- "Without giving specific guidance"
- "In line with industry trends"
- Excessive use of "we believe", "we expect", "we hope"
Count these instances. >5 in a concall is a hedge-heavy call. Compare count to prior concall.

### 6D. Confidence Indicators

Conversely, flag positive specificity:

- Named customer wins with deal size
- Specific dates for milestones
- Numerical margin/revenue commitments
- Acknowledgment of misses with explicit recovery timelines
- Promoter on call answering operational questions directly
### 6E. Management Archetype — Specificity × Credibility 2x2 (new in v1.1)

Combine the Specificity Ratio (6B) with the trailing-4-quarter Credibility Ratio (3B) to classify the management archetype:

| | **Credibility ≥60% (Grade A/B)** | **Credibility <60% (Grade C/D)** |
| --- | --- | --- |
| **Specificity >0.5** | **COMMITTED & CREDIBLE** — the best archetype; specific guidance backed by delivery. Full credit. | **OVERPROMISER — the danger quadrant.** Hyper-specific guidance with poor delivery. Treat ALL guidance as promotional; anchor exclusively to filing numbers; require pre-committed thresholds, not narrative, for any position action. |
| **Specificity ≤0.5** | **MEASURED & CREDIBLE** — conservative guiders who deliver. Their rare specific commitments carry extra weight. | **EVASIVE** — vague and unreliable. Grade D treatment; the concall contributes almost nothing to the thesis beyond governance signal. |

The archetype label goes in the Concall Verdict block (Step 9) and is tracked across quarters. An archetype shift (e.g., MEASURED & CREDIBLE → OVERPROMISER after a big capex announcement) is itself a flag.

🛑 **STOP. Show 6A through 6E.**

## STEP 7 — CROSS-REFERENCE vs FILING AND PEER CONCALLS

### 7A. Concall Narrative vs Filing Numbers

For each major narrative claim from the concall, check whether the filing numbers support it:

| **Concall Claim** | **Filing Evidence** | **Reconciliation** |
| --- | --- | --- |

**Reconciliation options:** CONFIRMED / PARTIALLY CONFIRMED / CONTRADICTED / UNVERIFIABLE

**Examples to specifically check:**

- "Strong cash generation" → Does CFO/PAT match the claim? Watch for the case where the ratio is genuinely strong but the PAT itself was driven by Other Income that management doesn't acknowledge — the claim is technically true and materially misleading at the same time
- "Margin expanding" → YoY operating EBITDA margin in the filing
- "Order book growing" → Compare to last quarter's stated order book
- "Net cash" → Balance sheet net debt position
- "Working capital normalised" → CCC and receivable days
- For lenders: "asset quality stable" → GNPA, PCR, collection efficiency, and write-off numbers in the filing; write-offs can make GNPA look stable while the underlying stress grows
### 7B. Peer Concall Cross-Check

For analysed companies in adjacent sectors, pull recent peer concalls (within ±4 weeks). Compare narrative on shared topics:

| **Topic** | **This Company Said** | **Peer 1 Said** | **Peer 2 Said** | **Most Credible Narrative** |
| --- | --- | --- | --- | --- |

**Topics to specifically cross-check:**

- Demand environment in shared end-market
- Pricing trends
- Raw material / input cost
- Customer behaviour (destocking, restocking)
- Capex cycle and competitive capacity
- Government policy impact
- Margin trajectory
- For lenders: state-level stress commentary, collection trends, competitive intensity in shared geographies
**Narrative discrepancies are diagnostic.** If peers say "destocking continues" and our company says "destocking ended", one of them is wrong. The peer set with internally consistent narrative is usually right.

### 7C. Concall vs Industry Channel Checks

If our prior research has identified credible third-party data sources (rating agency commentary, industry body reports, distributor checks), compare concall narrative to those:

| **Concall Claim** | **External Source** | **External Says** | **Alignment** |
| --- | --- | --- | --- |

🛑 **STOP. Show 7A, 7B, 7C.**

## STEP 8 — UPDATE THESIS & POSITION DECISION

### 8A. Growth Trigger Status Update

Pull the growth triggers from the Notion thesis. For each, update status based on the concall:

| **Trigger** | **Status Pre-Concall** | **Concall Evidence** | **Status Post-Concall** |
| --- | --- | --- | --- |

**Status options:** FIRED / ON TRACK / DELAYED / WEAKENED / DEAD / NEW (newly added based on concall)

### 8B. Watchlist Items — Concall-Specific Updates

Some watchlist items are specifically watched for in concall (utilization disclosure, contract wins, customer concentration). Update those rows:

| **#** | **Watchlist Item** | **This Concall Reading** | **Status** |
| --- | --- | --- | --- |

### 8C. Thesis-Broken Trigger Check

For every thesis-broken condition, state explicitly whether the concall has fired or moved closer to firing any of them:

| **Thesis-Broken Condition** | **Threshold** | **Concall-Relevant Evidence** | **FIRED?** |
| --- | --- | --- | --- |

### 8D. Four-Pillar Inputs — Concall Adjustments

Concalls frequently provide forward inputs to the Four-Pillar framework:

- Forward ROCE trajectory commentary → feeds the FTTCP ROCE forward verdict, which is the SOLE authority for Pillar 1 ROCE selection (per FTTCP v1.2)
- Forward CFO/PAT commentary (especially WC structural vs growth-induced framing) → Pillar 2; for lenders, credit cost and asset quality commentary → Asset-Quality Multiplier
- Forward EM developments (new patents, contracts, certifications) → Pillar 3
- Strategic positioning changes → Strategic Premium (respect the single-credit rule: ROCE recovery credited in Pillar 1 OR Strategic Premium, never both)
Update each pillar with concall-derived information:

| **Pillar** | **Pre-Concall** | **Concall Evidence** | **Post-Concall Adjustment** |
| --- | --- | --- | --- |

If any pillar adjusts, recompute destination PE (±7.5% range), re-run the Hurdle Ratio check, and revise fair values.

### 8E. Position Decision

Apply the same decision framework as Role 4 Step 8 (verify Decision Status first; use the 8A-W branch for non-held names), with concall-specific overrides:

IF management credibility ratio (Step 3B) drops below 60%:
    → Discount all management commentary by 30–50%
    → Tighten add-back triggers
    → Consider Promoter Verdict downgrade

IF two or more DROPPED commitments in trailing 4 concalls:
    → Automatic one-grade Management Grade downgrade (per 3B)
    → Log as governance signal in Key Notes

IF concall reveals undisclosed material risk:
    → Trim 25% immediately pending fuller assessment (held names only)

IF concall reveals undisclosed material positive:
    → Hold pending verification (don't add on concall noise alone)

IF concall confirms an evasion pattern across 3+ quarters:
    → Promoter Verdict downgrade by one grade
    → Reduce position size by one tier (Medium → Small)

IF concall narrative contradicts filing numbers materially:
    → Trust the filing
    → Note the management credibility issue
    → Tighten next-quarter watchlist

### 8F. Updated Questions for Management (Forward)

The concall just answered some questions and raised new ones. Build the updated question list for the NEXT quarter's review:

| **#** | **Question** | **Why It Matters** | **What to Watch in Next Concall** |
| --- | --- | --- | --- |

These become the input for Role 4 Step 8.5 in the next review cycle.

🛑 **STOP. Show 8A through 8F.**

## STEP 9 — NOTION SAVE

Save in this exact sequence:

- **Search for the company page**
- **Update row properties** if any have shifted:
  - Decision Status (if concall triggered trim/exit)
  - Position Size
  - Promoter Verdict (if credibility ratio shifted grade, or DROPPED rule fired)
  - Management Grade (if updated)
  - Key Notes (always prepend a date-prefixed concall-derived one-liner to the pipe-delimited audit trail)
- **Append the concall analysis to the page content** (under the existing Q[N] FY[YY] Results Review section if Role 4 was already run, or as a standalone section if not). Format:
## Q[N] FY[YY] Concall Analysis — [Date]

**Call participants:** [list]
**Hosting broker:** [name]
**Call duration / Q&A duration:** [time]
**Number of analyst questions:** [number]
**Business type:** [Standard / Lender]

[Step 1 Claims Inventory — full]
[Step 2 or 2L Forward Guidance Table — full]
[Step 3 Promise vs Delivery Audit — full, including points, credibility ratio, and DROPPED flag state]
[Step 4 Q&A Decomposition — full, especially the three most important exchanges]
[Step 5 New Information + What Was NOT Discussed — full]
[Step 6 Tone & Specificity Analysis — full, including the 6E archetype]
[Step 7 Cross-Reference — full]
[Step 8 Thesis & Position Updates — full]
[Step 8F Updated Questions for Next Quarter]

**Concall Verdict:**

- Management Credibility (this quarter): [Grade A/B/C/D]
- Trailing 4-Quarter Credibility Ratio: [X%] ([points] ÷ [commitments − unclear])
- Management Archetype (6E): [Committed & Credible / Overpromiser / Measured & Credible / Evasive]
- Role 1 Track Record Input: [Excellent / Good / Mixed / Poor] (mapped from grade)
- Net concall impact on thesis: [Strengthened / Maintained / Weakened / Broken]
- Position decision: [HOLD / TRIM / ADD / EXIT / entry-zone update for non-held names]
*Concall reviewed [Date] | Source: [transcript file/link]*

- **Confirm the save** by stating:
Saved to Notion: [Company Name]
Sections saved: [Q[N] FY[YY] Concall Analysis]
Row properties updated: [list, or "none"]
Page ID: [ID]

If Notion times out (frequent for large pages), split the save into smaller chunks and inform which sections saved successfully.

🛑 **STOP. Confirm save.**

## NON-NEGOTIABLE RULES

- **The Q&A is where the thesis is tested.** At least 60% of analytical effort goes here. Opening remarks are PR.
- **Every guidance claim must be quantified or marked as hedged.** No quantification = no commitment = no credit.
- **Promise-vs-delivery is cumulative and scored.** DELIVERED 1.0 / PARTIAL 0.5 / DELAYED 0.25 (first) / MISSED 0 / DROPPED 0 + flag / UNCLEAR excluded. A single missed commitment is noise; the trailing-4-quarter points ratio is the signal. Never grade management on one quarter alone.
- **Two DROPPEDs in trailing 4 concalls = automatic one-grade downgrade.** Concealment outranks failure.
- **The credibility grade maps to Role 1's track record input.** A = Excellent, B = Good, C = Mixed, D = Poor. This mapping is the single source of truth; no session may substitute its own judgment for the ratio when a Role 5 history exists.
- **Silence is information.** What was NOT discussed must always be a populated table, not skipped.
- **Tone shifts between concalls are flagged explicitly.** Adjective-level change is enough to log.
- **Specificity does not equal substance.** Check the arithmetic of any claim that combines multiple numbers, and always read specificity jointly with credibility (the 6E archetype). The Overpromiser quadrant is the most dangerous management type.
- **Peer concall cross-check is mandatory** when peers in the analysed universe have reported within ±4 weeks. If no peer reported in window, state explicitly.
- **Concall narrative loses to filing numbers.** When they conflict, the filing wins. Note the credibility issue.
- **CFO answering operational questions is a yellow flag.** Note it in the participant list section.
- **Promoter absence on a substantive call is a yellow flag.** Note explicitly.
- **Three consecutive evasions of the same question downgrade Promoter Verdict.** Track across reviews.
- **Hedge phrases are explicitly counted, not glossed.** Tracking the count across concalls reveals trajectory.
- **Lenders use the Step 2L guidance set.** Credit cost guidance is the lender equivalent of the cash conversion test — evasion on it across 2+ concalls is a negative diagnostic for FTTCP lender Transition 3.
- **Do not deliver a position verdict without completing all 9 steps.**
- **Cross-reference back to Role 4 (Results Review).** If Role 4 raised questions for management and the concall was held subsequently, update Role 4's Step 8.5 with answer status. Cross-protocol consistency is critical.
## STYLE & DELIVERY RULES

- Verbatim quotes only when material. Otherwise paraphrase tightly.
- Tables aggressively over prose. Same as Role 4 — diagnostic value is in structured comparison.
- Adversarial reading. Default to bear interpretation when ambiguous; let evidence pull you toward bull.
- No cheerleading. If management was strong, say so plainly; if weak, name the weakness.
- Indian context throughout. Recognise IR firm conventions, house broker patterns, promoter call styles.
- Length sized to substance. A 30-minute concall on a small company gets a focused review; a 90-minute concall on a flagship holding gets a comprehensive one. Both follow the same 9 steps but at proportionate depth.
## RELATIONSHIP TO ROLE 4 (RESULTS REVIEW)

Role 4 and Role 5 are designed to be run as a pair when both filing and concall are available. The combined output of both protocols becomes the **complete quarterly review** for the company.

**Combined output structure in Notion:**

## Q[N] FY[YY] — Complete Quarterly Review

### Section A — Results Review (Role 4)
[All Role 4 outputs]

### Section B — Concall Analysis (Role 5)
[All Role 5 outputs]

### Section C — Combined Verdict
- Filing-derived signals
- Concall-derived signals
- Reconciliation between the two
- Net thesis impact
- Position decision
- Watchpoints for next quarter
**When the filing and concall reach different conclusions:**

- Filing numbers win for valuation and trajectory
- Concall narrative informs management credibility and forward catalysts
- The discrepancy itself is a critical input — note it explicitly
- Repeated discrepancies across quarters indicate management is presenting a narrative the numbers don't support → Promoter Verdict downgrade
*This protocol exists because concall analysis is where the thesis gets stress-tested by adversarial questioning and where management credibility builds or erodes. Without a structured protocol, concall reviews default to summarising what management said — which is the least valuable analysis. The protocol forces extraction of what was committed (testable next quarter), what was evaded (signals problem area), what was contradicted (between concall and filing, or between concall and peers), and what was silent (information by absence).*

*Version 1.1 | Updated July 2026 — credibility ratio arithmetic defined (points system with UNCLEAR exclusion); DROPPED governance flag with automatic downgrade rule; Grade A–D mapped to Role 1's Excellent/Good/Mixed/Poor as single source of truth; Management Archetype 2x2 (Step 6E, Overpromiser quadrant); lender guidance set (Step 2L) and lender evasion rules; pipeline position codified (Role 4 → Role 5 → FTTCP → Roles 1–3); Four-Pillar references synced to Section 1B v3.3 and FTTCP v1.2; company-specific template residue removed. v1.0 created May 2026.*
