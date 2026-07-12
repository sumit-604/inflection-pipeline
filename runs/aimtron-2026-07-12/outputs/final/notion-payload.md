Execute via the claude.ai project; never overwrite Decision Status.

# Notion Save Payload — COMPANIES MASTER (data_source_id 345bb2b9-d3ab-8032-9b46-000ba16ab827)

This is a PAYLOAD, not an action. Do not write to Notion from the pipeline session. The operator executes the save in the claude.ai project. If the company page already exists, fetch the live page first and APPEND the run summary; never overwrite the Decision Status property from a pipeline run.

## Page title
Aimtron Electronics (AIMTRON) — Phase 3 Finalize (2026-07-12)

## Run summary
Aimtron Electronics Ltd (NSE: AIMTRON, ISIN INE0RUV01018), EMS/ESDM contract manufacturer (PCBA, Box Build, ODM), IPO June 2024, reports half-yearly. First full workup.

Real growth, priced far above value. FY26 standalone revenue Rs257.13cr / PAT Rs39.16cr / diluted EPS Rs18.49 / ROCE 24.0%; consolidated FY26 revenue Rs301.16cr / PAT Rs45.97cr / operating cash flow -Rs40cr. Revenue and PAT both compounded above 65% FY24-26; balance sheet net cash. Gate 0 72/160, Emerging Moat 23/80 MODEST.

The decision is AVOID on valuation. At CMP Rs1,390 (~75x FY26 standalone PE) the market prices Aimtron 3 to 10 times above the four-pillar destination of 8.9x (RRM, governing) to 12.7x (additive) against a 25x sector cap. Fair value base Rs314 (RRM) / Rs448 (additive), bull ceiling Rs504, all far below CMP. Hurdle Ratio STOP; probability-weighted CAGR at CMP minus 41.6%.

Cash conversion is INDETERMINATE (cumulative CFO/PAT -0.13x FY24-26; 0.65x multiplier), which caps the evidence gate at PROCEED WITH CAVEATS. Promoter verdict CONCERN (related-party revenue ~31.5%, Chairman is CEO of the largest counterparty, Rs120cr RPT ceiling with no external valuation). Credibility grade C. FTTCP composite +1/8, DEEP WATCH leaning AVOID, Kernex cap engaged. Devil's advocate SURVIVES on all four dimensions; the 24% margin and ROCE may be a related-party artifact, which threatens even the entry-zone buyer.

## Verdict
- Evidence gate: PROCEED WITH CAVEATS (INDETERMINATE cash caps it; confidence band 60-74 holds it there)
- Investment decision: AVOID (on valuation)
- FTTCP: DEEP WATCH leaning AVOID (composite +1/8, Kernex cap engaged)
- Devil's advocate: SURVIVES (robust AVOID)

## Entry zones
- Tier A (25% hurdle): entry Rs129-161, MoS Rs129
- Zone top Rs161 is ~88% below CMP Rs1,390 (MARKET-UNLIKELY; price history unavailable from inputs)
- Decision Status suggestion (operator sets, pipeline never overwrites): DEEP WATCH / AVOID

## Thesis-broken and re-open triggers
- Re-open requires ALL: price inside Rs129-161 AND a genuinely third-party-collection-driven positive H1 FY27 consolidated operating cash flow (related-party receivables falling, no offsetting related-party payable build, third-party DSO <120) AND promoter verdict upgrading from CONCERN
- A netted or RPT-manufactured positive OCF does NOT count
- Permanent AVOID if: a third straight negative consolidated OCF (H1 FY27) or rising related-party receivables

## Monitoring checklist
1. H1 FY27 consolidated operating cash flow (~Nov-2026): third-party-driven positive with debtor days <120 = green; third straight negative or RPT-netted = red
2. Trade receivables turnover >=6x (~60 days) recovering from 3.07x FY25; red if <4x or DSO >120
3. Consolidated EBITDA margin >=18-20% with AIC ramp from 11%; red if sustained sub-18%
4. Related-party revenue share below 20% and external valuation adopted for the Rs120cr ceiling; red if >~30% or ceiling drawn without valuation
5. Vadodara SMT lines shipping on FY27 schedule; red if delay past FY27-Q4 or per-line far below Rs100cr (peer Vinyas discloses Rs500-600cr/line)
6. Price re-rating into Rs129-161 vs the 8.9-12.7x destination; red if price stays multiples above destination (value trap)

## Flags
- FLAG-PROMOTER: CONCERN
- FLAG-CASH: INDETERMINATE (falsification metric: H1 FY27 consolidated OCF, third-party-collection driven)
- FLAG-HURDLE-STOP
- FLAG-GATE0 (Gate 0 AVOID; order-sensitive AVOID vs AVERAGE, operator-ruling item)
- FLAG-DATA-QUALITY: manifest sector cap mis-set (Pharma/CDMO 38x, overridden to Manufacturing 25x)

## Confidence delta
numerical 95.2 | redflag 63 (binding floor) | framework 95 | peer 91.7 | overall 63 (band 60-74). No CRITICAL; REWORK not triggered.

## Links
- Run folder: runs/aimtron-2026-07-12/
- Drive folder: NOT PROVIDED
- Deliverables: outputs/final/business-narrative.md, fttcp-recommendation.md, verifier-summary.md, fttcp-handoff.md

## Notion field hygiene (per Notion_Save_Instructions)
- Clean < and -> characters from text properties before saving.
- EM Classification select lacks a NONE option; write MODEST.
- Promoter Verdict select lacks CAUTION; CONCERN exists. Use CONCERN.
- Never overwrite Decision Status from a pipeline run; append the run summary and link the folder.
