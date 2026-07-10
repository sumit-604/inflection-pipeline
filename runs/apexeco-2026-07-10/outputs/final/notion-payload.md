Execute via the claude.ai project; never overwrite Decision Status.

# NOTION SAVE PAYLOAD — Apex Ecotech Ltd (APEXECO)

This file is a payload, not an action. Do not write to Notion from the pipeline
session. The operator executes the save in the claude.ai project. If the company
page already exists, fetch it live first, append this run summary, and never
overwrite the Decision Status field from a pipeline run.

## Target
- Database: COMPANIES MASTER (data_source_id 345bb2b9-d3ab-8032-9b46-000ba16ab827)
- Page title: Apex Ecotech Ltd (APEXECO)
- Section to add: "Inflection Alpha Run — 2026-07-10"

## Run summary
- Ticker: APEXECO | CMP ₹242 | Market cap ₹319 Cr | Sector: EPC / Civil construction (water and wastewater treatment EPC, asset light integrator)
- Run type: full | Concalls: available (semi annual H1/H2 reporting)
- Gate 0: 86/160, AVERAGE (capped by cash deal-breaker), moat class STRONG, 5 moats
- Emerging Moat: 10.1, NONE
- FTTCP composite: +5 of 8, BUY-candidate (operator-final rulings applied)
- Promoter verdict: CAUTION (clean legal record, pledge 0%)
- Management grade (Role 5): B
- TAM runway: STRONG (TAM ₹11,250 to ₹14,500 Cr; SOM 3yr ₹277 Cr; ~43x revenue headroom)

## Gate and investment decision
- Gate verdict: PROCEED WITH CAVEATS
- Investment decision: WATCHLIST | Position size: Small
- Entry range: ₹161 to ₹202 | Margin of safety price: ₹161 | CMP ₹242 (about 20% above entry top)
- Destination PE: 16.8x required-return track (governing) / 20.0x additive track (EPC sector cap)
- Hurdle Ratio: CONDITIONAL (base fails, bull passes) — growth dependent, no buy today
- Base fair value (3yr): ₹394 governing track (bear ₹232, bull ₹572)
- Probability-weighted expected CAGR: 16.7% vs 25% target | Upside/downside ~1.9x
- Devil's advocate: WEAKENED BUT ALIVE (moat durability destroyed)
- Confidence delta overall: 81 (numerical 89, red-flag 87, framework 97, peer 81)

## Cash determination (operator final)
- GROWTH-INDUCED (not structural), cash multiplier 1.00x
- Falsification trigger: H1 FY27 (~Nov 2026) CFO/PAT prints below 0.7x while working capital days climb faster than revenue. If it fires, cash reverts to STRUCTURAL (Pillar 2 to 0.65x, destination PE ~11 to 16x) and the thesis breaks.

## Active flags (surfaced, not gating)
- FLAG-CASH: GROWTH-INDUCED with the falsification trigger above
- FLAG-GATE0: AVERAGE cap driven by post-IPO cash rebase, not weak returns
- FLAG-GOVERNANCE: independent director attendance <42%, remuneration disclosure contradiction (Note 20(b) vs Annexure III), 3 company secretaries in 16 months, undisclosed Bank of India cash credit facility ~₹665 lakh
- FLAG-CONCENTRATION: Reliance plus Bhartiyam ~70% of H2 FY26 execution; book to bill 0.84x
- SHARED-CATALYST: a working capital unwind drives both Pillar 1 ROCE and Pillar 2 cash
- FLAG-PROMOTER: NOT triggered (B08 CAUTION, clean legal record)

## Thesis-broken triggers
1. H1 FY27 CFO/PAT below 0.7x while working capital days rise faster than sales (primary; cash reverts structural)
2. Order book not replaced (book to bill stays below 1.0, order book below ₹150 Cr) and FY27 revenue decelerates or declines
3. EBITDA margin falls below 14.6% at H1 FY27
4. A doubtful-debt provision taken against the receivables build (signals FY25 to FY26 PAT was overstated)

## Monitoring checklist (H1 FY27 and FY27)
1. CFO/PAT rises toward 0.7x and does not fall below it
2. Working capital days fall as growth cools; receivable days near 41 to 45
3. EBITDA margin holds at or above 14.6%
4. Order book above ₹150 Cr, book to bill above 1.0
5. Top-customer (Reliance) concentration disclosed and falling below ~50%
6. ROCE stays above 25%
7. No bad-debt write off against the concentration exposure
8. FII/DII holding disclosed (UA test) and Bank of India cash credit facility terms disclosed and reconciled to the borrowing note

## Publish candidate
No publish candidate this analysis.

## Links
- Drive folder: NOT PROVIDED
- Run folder: runs/apexeco-2026-07-10/
- Deliverables: outputs/final/business-narrative.md, fttcp-recommendation.md, verifier-summary.md, fttcp-handoff.md, fttcp-deliberation.md

## Data caveats for the reader
- No credit rating exists (SME issuers exempt); the cash determination rests on internal evidence, peer read, and operator ruling.
- PDF rendering was unavailable to the orchestrator and two verifiers; figures rest on the screener CSV plus stage-agent AR extractions (Verifier A numerical acceptance 89%).
- Verifier D found two CRITICAL peer citation-integrity errors in B06 (one misattributed TAM quote, one unlocatable FELIX price-variation quote); peer corroboration is weaker than the peer stage stated.
- FY26 free cash flow and capex are estimated (±20%); FY26 trade receivables (screener ~₹16.76 Cr) do not fully reconcile with management's stated ₹61.72 Cr working capital and should be checked against the FY26 signed balance sheet.
