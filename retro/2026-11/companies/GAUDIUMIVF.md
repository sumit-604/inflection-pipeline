# GAUDIUMIVF — Gaudium IVF and Women Health Ltd
Run folders read: runs/gaudiumivf-2026-07-16 (origin/claude/gaudiumivf-pipeline-tvrgn0), runs/gaudiumivf-q1fy27 (origin/claude/quarterly-results-analysis-7dqyyn)
Company file: companies/GAUDIUMIVF.md (origin/claude/gaudiumivf-pipeline-tvrgn0)

## Our base case
Valuation basis line:
> **Valuation basis (operator override, Override 3):** ONE-YEAR-FORWARD earnings multiples. Current multiple on FY27E EPS; exit priced at the FY29 exit on the year-ahead (FY30E) EPS. Three-year hold FY27→FY30.
Source: origin/claude/gaudiumivf-pipeline-tvrgn0:runs/gaudiumivf-2026-07-16/outputs/reports/B11-valuation.md §header L6

Inputs (FY26 actuals, the base is built after these):
> | FY26 consol PAT | Rs 24.49 Cr | B10 latest_financials.pat_cr |
> | FY26 diluted EPS | Rs 3.37 | B10 diluted_eps_rs |
> | FY26 revenue | Rs 104.36 Cr | B10 revenue_cr |
> | FY26 EBITDA / margin | Rs 37.70 Cr / 36.13% | B10 ebitda_cr / ebitda_margin_pct |
Source: B11-valuation.md §Inputs L19-L22 (same branch/path as above)

Margin and CAGR inputs unresolved:
> **INPUT UNRESOLVED — forward margin guidance (B10 margin_guidance NOT FOUND).** Conservative assumption used: hold FY26 consolidated EBITDA margin 36.13% flat across the projection (no expansion credited)
> **INPUT UNRESOLVED — 3yr revenue/PAT CAGR (B10 NOT FOUND).** Base EPS CAGR set per deliberation at 25%, cross-checked below against the SOM-implied 31.4% and the FY25→FY26 prints (rev +47.6%, PAT +27.8%).
Source: B11-valuation.md L35, L37

Scenario assumptions:
> | EPS CAGR | 15% | 25% | 30% (C-cap = base+5%) |
> | Growth logic | Hub delays + receivables drag; 1-2 triggers fail | IPO-funded hubs ramp; SOM headroom 28x | Hubs + AI-embryology + international spokes all fire |
> | EBITDA margin | 34% (−200bps) | 36% (hold FY26) | 38% (mix toward IVF core) |
Source: B11-valuation.md §2A/2B L143-L145

EPS ladder:
> | FY26 (actual) | 3.37 | 3.37 | 3.37 |
> | FY27 | 3.88 | 4.21 | 4.38 |
> | FY28 | 4.46 | 5.27 | 5.70 |
> | FY29 | 5.13 | 6.58 | 7.40 |
> | **FY30 (exit-year, year-ahead)** | **5.89** | **8.23** | **9.63** |
Source: B11-valuation.md §2C L154-L158

> Base revenue (illustrative, 25% ≈ EPS CAGR at flat margin/nil dilution): FY26 104.36 → FY30 ~254.8 Cr; base FY30 EBITDA ~91.7 Cr at 36%.
Source: B11-valuation.md L160

> Current PE (one-year-forward, FY27E EPS): 137 / 4.2125 = **32.5x** (trailing = 137/3.37 = 40.7x).
Source: B11-valuation.md L120

Date of the base: 2026-07-16 (company file L4 "First workup 2026-07-16"; manifest run_date 2026-07-16). Source: companies/GAUDIUMIVF.md L4; manifest.yaml.

## Management guidance and promised catalysts
Q4/FY26 call (date not stated in the files) guidance table:
> | New IVF hubs | 19 total (10 FY27 / 8 FY28 / 1 FY29); base 7→17 by FY27-end | FY27-FY29 | Q4/FY26 call |
> | Near-term hubs | South Delhi (opening "coming month"), Nagpur, Gurgaon "in progress" | Next 1-2 months from call date | Q4/FY26 call |
> | New spokes | 9 domestic + 3 international (Nigeria, Sydney, Paris) | "Next couple of months" / "this quarter" | Q4/FY26 call |
> | FY27 capex | ~₹25 crore, avg ₹2.5 crore/hub, funded from IPO proceeds + internal accruals | FY27 | Q4/FY26 call |
> | ROCE | 35-40% | 3-5 years | Q4/FY26 call |
> | Receivables collection cycle | ~150 average days currently; management "very confident" of a "significant" reduction | By end of "this quarter" (Q1 FY27) | Q4/FY26 call |
Source: origin/claude/gaudiumivf-pipeline-tvrgn0:runs/gaudiumivf-2026-07-16/outputs/reports/B05-concall.md §1B L54-L64

> | Q4/FY26 call, Manika Khanna | Trade receivables to "reduce significantly" by end of "this quarter" (Q1 FY27) via the ₹40k→₹80k initial-payment hike and ₹40k late-transfer fee | PENDING |
Source: B05-concall.md L98

Q1 FY27 review guidance extraction (deck, unaudited):
> | Hub rollout FY27 | 2 of 10 hubs "launching soon" — 1 Delhi/NCR + 1 Nagpur | deck slide 22 (items 65-67) | MEDIUM |
> | Centres / capex (monitoring) | FY27 10 centres / Rs 26.31 Cr; FY28 8 / Rs 21.05 Cr; FY29 1 / Rs 2.63 Cr | `ledger_monitoring` L622-624 | The hard, filed number (FND-2) |
Source: origin/claude/quarterly-results-analysis-7dqyyn:runs/gaudiumivf-q1fy27/work/review_gaudiumivf_q1fy27.md §B3 L330-L336

> Against Rs 1.03 Cr deployed in Q1, FY27 is a **steeply back-loaded ramp** — the Board formally deferred the FY25-26 spend to FY26-27 on 28 May 2026 (L696-699)
Source: review_gaudiumivf_q1fy27.md L377

Q2 FY27 monitorables listed by the reviewer (not management promises):
> {item: "Q2 FY27 first half-yearly CFO/balance sheet", implied_date: "~2026-11", source_ref: "Reg33/Step5"}
> {item: "FY27 deployment vs Rs 26.31 Cr / 10 centres", implied_date: "FY27", source_ref: "monitoring L622-624"}
Source: review_gaudiumivf_q1fy27.md L504-L506

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
Consolidated table (Rs Cr), columns Q1FY26 | Q4FY26 | Q1FY27 | FY26:
> | Revenue from operations | 17.76 | 30.35 | 19.38 | 104.36 |
> | PAT (before discontinued) | 3.08 | 8.36 | 1.78 | 24.49 |
> | Operating EBITDA margin | 29.02% | 40.10% | **12.51%** | 36.13% |
> | EPS (reported, Rs) | 0.50 | 1.34 | 0.25 | 3.94 |
Source: review_gaudiumivf_q1fy27.md §Step 1B L101, L114, L123, L116-L117 (EPS row at L116)

Standalone:
> | Revenue from operations | 12.27 | 22.17 | 13.68 | 71.58 |
> | Operating EBITDA margin | 33.86% | 50.81% | **15.89%** | 48.29% |
> | PAT | 2.35 | 7.73 | 1.66 | 22.29 |
Source: review_gaudiumivf_q1fy27.md §Step 1A L66, L88, L79

YoY:
> | Operating EBITDA margin | 29.02% | 12.51% | **−1,651 bps** | Collapse |
> | PAT | 3.08 | 1.78 | −42.3% | — |
Source: review_gaudiumivf_q1fy27.md §2B L158, L161

Q1 review base statement:
> 1. **Did revenue grow YoY?** Yes. Standalone +11.4% (12.27→13.68), consolidated +9.1% (17.76→19.38). ... No Notion base case exists to compare against (pre-position name).
Source: review_gaudiumivf_q1fy27.md L165

Results board meeting date: "Outcome of the Board Meeting held on August 13, 2026." Source: runs/gaudiumivf-q1fy27/work/out_layout.txt L17 (origin/claude/quarterly-results-analysis-7dqyyn)

Cash conversion for Q1:
> **Reg 33 data-availability rule:** this is a **Q1** review — the CFO statement and balance sheet are NOT mandated until Q2 (half-yearly). ... cash conversion is INDETERMINATE.
Source: review_gaudiumivf_q1fy27.md L229

Q2 FY27 / H1 FY27 result: NOT FOUND (no file for it).

## Management's stated reasons
> S&M ... supports the deck's "front-loaded expansion" narrative (Delhi South Extension Hub, Nagpur/Gurgaon prep, clinical hiring, AI tools; deck slide 26 comments).
Source: review_gaudiumivf_q1fy27.md L388

> with a stated cause: proceeds only reached the company's account in the third week of March 2026, too late to build before FY-end.
Source: review_gaudiumivf_q1fy27.md L377 (reviewer paraphrase of the monitoring report; raw cell at runs/gaudiumivf-q1fy27/work/monitoring_layout.txt L585 "third week of March")

> The subsidiary's net margin fell from about 13% to about 2%, which the marketing story does not explain and which management has not addressed.
Source: review_gaudiumivf_q1fy27.md L450

## Risk flags raised before the result, and any overruling
Flags dated 2026-07-16 (before the Q1 print of 13 Aug 2026):
> 3. IPO hub capex spend. Rs 0 of the Rs 50 Cr hub allocation was used at FY26 close; watch openings track the 10, 8, 1 split across FY27 to FY29 in quarterly results. Tests whether the growth story is real.
> 4. Pharmacy revenue share against consolidated EBITDA margin. Watch pharmacy climbing past 35 to 40% while margin slips below 35%, in investor presentations. Tests margin quality.
Source: origin/claude/gaudiumivf-pipeline-tvrgn0:runs/gaudiumivf-2026-07-16/outputs/final/gate-recommendation.md L54-L55 (item 3 at L54, item 4 at L55)

> | **Shared catalyst slips — hubs don't open, cash doesn't turn, ROCE dilutes** | Rs 0 of Rs 50 Cr hub-capex still undeployed by Q2 FY27; openings slip past FY27; base EPS CAGR falls below 15%. ... | 2-4 quarters | **Medium** — Rs 0 deployed at FY26 close; peers routinely slip 9-12 months |
Source: outputs/reports/B15-devil.md L37

> ▼ hub-opening delay (zero capex utilised as of 31-Mar-FY26) cuts base EPS CAGR below 25%
Source: outputs/reports/B11-valuation.md L303

> - THESIS BROKEN: trade receivable days stay above 150 for two consecutive quarters (through H1 FY27) while zero incremental IPO hub-capex is deployed / no new hub opens.
Source: companies/GAUDIUMIVF.md §ACTIVE TRIPWIRES L21

Subsidiary margin collapse (Gaudium International): no flag before the result found in these files.

Overruling / non-application: the Q1 review (separate branch) states
> **Decision Status:** NO POSITION / PRE-DILIGENCE. No Notion page, no companies/GAUDIUMIVF.md, no Decision Status, no entry zone, no tripwire.
Source: review_gaudiumivf_q1fy27.md L6
and "The prior evidence-only run (runs/gaudiumivf-2026-07-16) carried a 'Pharma/CDMO' tag — that tag is WRONG and is superseded here." (L5). No explicit waiver of the 2026-07-16 flags found.

## Verdicts and dates
- 2026-07-16 gate: "PROCEED WITH CAVEATS" (gate-recommendation.md L1; companies/GAUDIUMIVF.md L10: "As of 2026-07-16: WATCHLIST (not a buy at CMP Rs 137; Hurdle STOP). Evidence gate PROCEED WITH CAVEATS.")
- Entry zone Rs 90 to 93, MoS Rs 74 (companies/GAUDIUMIVF.md L11; fttcp-recommendation.md §Valuation decision, Entry range and MoS lines).
- Q1 FY27 review protocol verdict: "PROCEED WITH FLAGS"; decision_status_verified "NO POSITION / PRE-DILIGENCE" (review_gaudiumivf_q1fy27.md L482-L484).

## Lessons archive mentions
> - OPEN (2026-10-03, corpus): CLEANMAX run folder holds six Vinyas filings; GAUDIUMIVF and VINYAS have mislabelled-year annual reports; KRONOX's annual-report folder holds the IPO prospectus. Fix before reusing those runs.
Source: origin/main:LESSONS_ARCHIVE.md L1000-L1003 (export copy)
