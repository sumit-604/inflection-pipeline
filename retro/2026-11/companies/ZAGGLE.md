# ZAGGLE — Zaggle Prepaid Ocean Services Ltd
Run folders read: runs/zaggle-2026-07-27 (origin/main)
Company file: NONE (no companies/ZAGGLE.md existed at the run)

## Our base case
```
L113: **Reading the tables.** FY23 to FY26 columns are ACTUAL and anchored. FY27 to FY31 columns are EXPECTED and illustrative. They are built from management guidance where guidance exists and from a stated taper where it does not. They are not forecasts I am anchoring and they are not facts. FY22 is NOT FOUND throughout, because Zaggle listed in September 2023, the prospectus is absent from this run, and the screener history begins FY23.
L114: 
L115: ### 2.1 Revenue growth
L116: 
L117: | Rs cr | FY22 | FY23 | FY24 | FY25 | FY26 | FY27E | FY28E | FY29E | FY30E | FY31E |
L118: |---|---|---|---|---|---|---|---|---|---|---|
L119: | Revenue | NOT FOUND | 553.46 | 775.60 | 1,303.76 | 1,907.65 | 2,671 | 3,338 | 4,006 | 4,807 | 5,528 |
L120: | Growth % | NOT FOUND | ACTUAL | 40.1 | 68.1 | 46.3 | 40 | 25 | 20 | 20 | 15 |
L121: | Basis | | ACTUAL | ACTUAL | ACTUAL | ACTUAL | guided | illustrative | illustrative | illustrative | illustrative |
L122: 
L123: Actuals are screener-data, consolidated, tied to results Q4 FY26 p.9. FY27E uses management's stated consolidated growth of about 40% (Q4 FY26 concall); FY28E onward is an illustrative taper with no management guidance behind it.
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/final/fttcp-draft.md §2.1 Revenue growth L113-123

```
L131: | % | FY22 | FY23 | FY24 | FY25 | FY26 | FY27E | FY28E | FY29E | FY30E | FY31E |
L132: |---|---|---|---|---|---|---|---|---|---|---|
L133: | Gross operating margin | NOT FOUND | 8.70 | 9.11 | 8.75 | 9.70 | 9.7 | 10.0 | 10.5 | 11.0 | 11.5 |
L134: | Basis | | ACTUAL | ACTUAL | ACTUAL | ACTUAL | not guided | illustrative | illustrative | illustrative | illustrative |
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/final/fttcp-draft.md §2.2 Margin L131-134

```
L144: | Rs cr | FY22 | FY23 | FY24 | FY25 | FY26 | FY27E | FY28E | FY29E | FY30E | FY31E |
L145: |---|---|---|---|---|---|---|---|---|---|---|
L146: | PAT | NOT FOUND | 22.90 | 44.02 | 87.92 | 138.08 | 193 | 240 | 288 | 346 | 398 |
L147: | CFO | NOT FOUND | -15.62 | -82.75 | 19.70 | -51.47 | 39 | 96 | 144 | 208 | 239 |
L148: | CFO/PAT | NOT FOUND | -0.68 | -1.88 | 0.22 | -0.37 | 0.20 | 0.40 | 0.50 | 0.60 | 0.60 |
L149: | Debtor days | NOT FOUND | 67.7 | 82.2 | 60.2 | 69.1 | 69 | 68 | 66 | 65 | 65 |
L150: | Net debt | NOT FOUND | 118.75 | -192.68 | -633.46 | -491.13 | illustrative | illustrative | illustrative | illustrative | illustrative |
L151: | Basis | | ACTUAL | ACTUAL | ACTUAL | ACTUAL | part guided | illustrative | illustrative | illustrative | illustrative |
L152: 
L153: Actuals from screener-data, cross checked to results Q4 FY26 p.11. Negative net debt is net cash. FY27E CFO reflects management's stated intent that operating cash flow turns positive in FY27; everything past FY27 is an illustrative path showing what a real cash transition would look like, not a prediction that it happens.
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/final/fttcp-draft.md §2.3 Cash conversion L144-153 (PAT row L146)

## Management guidance and promised catalysts
```
L33: guidance:
L34:   - {item: "Revenue growth guidance", number: "40% to 45%", timeframe: "FY26", stated_in: "Q2 FY26"}
L35:   - {item: "EBITDA guidance", number: "10% to 11%", timeframe: "FY26", stated_in: "Q2 FY26"}
L36:   - {item: "Adjusted EBITDA margin target", number: "14% to 15%", timeframe: "next 4-5 years", stated_in: "Q2 FY26"}
L37:   - {item: "Retail co-brand segment revenue/EBITDA", number: "INR500-600cr revenue, INR50-60cr EBITDA (standalone year)", timeframe: "4-5 years", stated_in: "Q2 FY26"}
L38:   - {item: "Cross-sell percentage", number: "21% (from 20% Sept-2024, 16% at IPO)", timeframe: "as of Q2 FY26", stated_in: "Q2 FY26"}
L39:   - {item: "OCF turnaround", number: "breakeven FY26, positive FY27 onwards", timeframe: "FY26/FY27", stated_in: "Q2 FY26, reaffirmed Q3 FY26"}
L40:   - {item: "$1 billion revenue + 14-15% EBITDA margin", number: "combined milestone", timeframe: "5 to 7 years", stated_in: "Q3 FY26"}
L41:   - {item: "Zagg.money 5-year goal", number: "INR500cr revenue, INR65cr EBITDA milestone", timeframe: "5 years", stated_in: "Q3 FY26, reaffirmed Q4 FY26"}
L42:   - {item: "Incentive/cashback as % of program fees", number: "stabilizing at ~50%", timeframe: "~5 years", stated_in: "Q3 FY26"}
L43:   - {item: "Dice acquisition value", number: "~INR68cr (down from INR123cr), asset purchase", timeframe: "signed Q4 FY26", stated_in: "Q4 FY26"}
L44:   - {item: "FY27 revenue growth guidance", number: "stand-alone 25-30%, consolidated ~40%", timeframe: "FY27", stated_in: "Q4 FY26"}
L45:   - {item: "U.S. operations kick-start", number: "originally June 2026, now pushed a couple of quarters", timeframe: "FY26-end (revised)", stated_in: "Q4 FY26"}
L46:   - {item: "GreenEdge FY27 growth", number: "40% to 50% (standalone)", timeframe: "FY27", stated_in: "Q4 FY26"}
L47:   - {item: "Propel margin recovery target", number: "~5.5%", timeframe: "coming years", stated_in: "Q4 FY26"}
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/blocks/B05-concall.yaml §guidance L33-47

```
L15:   - "FY27 EBITDA guidance explicitly withheld pending DICE integration, a guidance retreat versus FY26's specificity"
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/blocks/B05-concall.yaml §flags L15

```
L227: | 1 | Consolidated operating cash flow | Crosses zero for a full half year | H1 FY27 | Cash to STARTING, composite to 4, disposition cap lifts |
L228: | 2 | Consolidated CFO/PAT | Above 0.50x for two consecutive halves | 12 months | Cash to FIRING, composite to 5, BUY candidate band |
L229: | 3 | Incentive and cashback ratio | Below 65% of program fees | 2 quarters | Margin catalyst becomes real, margin to STARTING |
L230: | 4 | Propel gross margin | Above 5.5% for two quarters | 2 to 3 quarters | Confirms the redemption model change worked |
L231: | 5 | FY27 EBITDA guidance | Reissued at or above 10% | Next 1 to 2 calls | Removes the guidance retreat, margin to STARTING |
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/final/fttcp-draft.md §STEP 5 monitoring triggers L227-231

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
```
L119: | Revenue | NOT FOUND | 553.46 | 775.60 | 1,303.76 | 1,907.65 | 2,671 | 3,338 | 4,006 | 4,807 | 5,528 |
L120: | Growth % | NOT FOUND | ACTUAL | 40.1 | 68.1 | 46.3 | 40 | 25 | 20 | 20 | 15 |
L121: | Basis | | ACTUAL | ACTUAL | ACTUAL | ACTUAL | guided | illustrative | illustrative | illustrative | illustrative |
L133: | Gross operating margin | NOT FOUND | 8.70 | 9.11 | 8.75 | 9.70 | 9.7 | 10.0 | 10.5 | 11.0 | 11.5 |
L136: Actuals computed from screener-data. Adjusted EBITDA margin on the net revenue basis, which is the comparable one, was 19.9% in FY25 and 21.7% in FY26 (investor presentation May 2026 slide 9). Management's long run target is 14% to 15% adjusted EBITDA, stated variously as 4 to 5 years, 5 to 7 years, and next 5 years across three consecutive calls.
L146: | PAT | NOT FOUND | 22.90 | 44.02 | 87.92 | 138.08 | 193 | 240 | 288 | 346 | 398 |
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/final/fttcp-draft.md §2.1-2.3 L119-146

```
L59:     - {promised_in: "Q2 FY26", promise: "FY26 revenue growth guidance 40-45%", outcome: "Delivered — FY26 standalone ~42%, consolidated ~46%", explanation: "None needed"}
L60:     - {promised_in: "Q2 FY26", promise: "FY26 EBITDA guidance 10-11%", outcome: "Partial — landed at 9.7% standalone / 9.9% consolidated reported margin, at/below the guided floor", explanation: "None given"}
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/blocks/B05-concall.yaml §promise_delivery L59-60

```
L296: **Option 2, trailing P/E.** Apply the multiple to FY26 reported EPS of Rs 10.27. Fits a business where earnings quality is the open question: roughly Rs 107 cr a year of development cost is capitalised rather than expensed, other income was 22.6% of consolidated profit before tax and is treasury interest on idle cash, and Q4 FY26 standalone profit grew 18% against revenue growth of 44% as the depreciation from that capitalisation started biting. Forward earnings from a management graded C on del [...truncated]
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/final/fttcp-draft.md §P/E BASE CARD L296
(No Q1 or Q2 FY27 result in the files.)

## Management's stated reasons
```
L53: I chose STAGNANT over DECLINING because there is real executed action, not just words: management changed the Propel redemption model to cut cash intensity and you can see the cost of that decision in the take rate falling from 10% to 4%, and standalone quarterly operating cash flow improved from about negative Rs 33 cr to about negative Rs 6 cr across FY26 (Q4 FY26 concall). Catalyst strength is Weak, not NONE, so the Kernex cap does not engage.
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/final/fttcp-draft.md §Cash conversion ruling L53

```
L94: | 5 | (Undated, referenced retrospectively in Q4 FY26) | U.S. operations to kick-start by June 2026 | ❌ Missed — pushed "by a couple of quarters" (Q4 FY26 concall) | External-blame: "looking at the war and a lot of uncertainty around" (Raj Narayanam, Q4 FY26) |
L95: | 6 | Q2 FY26 (Aditya Kumar) | OCF to break even FY26, turn positive FY27 | Partial — Q4 FY26: standalone OCF near breakeven at -INR6cr; consolidated OCF still ~-INR52cr negative (Rohan Mandora Q&A, Q4 FY26) | "We are minutely focused... will look forward to improving it" (Raj Narayanam, Q4 FY26) — no firm date given for consolidated turn |
L96: | 7 | Q2 FY26 (Raj Narayanam) | FY26 revenue growth guidance 40-45% | ✅ Delivered — FY26 standalone revenue grew ~42%, consolidated ~46% (Raj Narayanam, Q4 FY26) | — |
L97: | 8 | Q2 FY26 (Raj Narayanam) | FY26 EBITDA guidance 10-11% | Partial — FY26 landed at reported margin 9.7% (standalone) / 9.9% (consolidated) (Rajesh Tummalaganti, Q4 FY26) — at or just below the guided floor | — |
L98: | 9 | Q2 FY26 / Q3 FY26 (Avinash Godkhindi) | OMC fleet contracts within "a quarter or two" then "very soon" | ❌ Missed — Q4 FY26: still only "hopeful... in the coming quarters," no OMC named | "It's very hard to crack into an IOCL, HPCL or BPCL... sizable would take some time" (Avinash Godkhindi, Q4 FY26) |
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/reports/05-concall.md §2 promise vs delivery table L94-98

## Risk flags raised before the result, and any overruling
NOT FOUND. First file is dated 2026-07-27, after the May 2026 (Q4 FY26) print.

## Verdicts and dates
```
L3: PROCEED WITH CAVEATS
L4: 
L5: This is the FTTCP gate decision on evidence alone. Stages 10 and 11 have not run, so no investment call, entry range, margin of safety, destination PE or Hurdle verdict is formed here. That decision forms in phase 3. The verdict is capped at PROCEED WITH CAVEATS because the cash conversion flag resolves INDETERMINATE, and INDETERMINATE cash never resolves to PROCEED.
```
Source: origin/main:runs/zaggle-2026-07-27/outputs/final/gate-recommendation.md L3-5

```
L1: company: Zaggle Prepaid Ocean Services Ltd
L2: ticker: ZAGGLE
L3: cmp: 203.0
L4: market_cap_cr: 2731.0
L5: run_date: 2026-07-27
L6: run_type: full
```
Source: origin/main:runs/zaggle-2026-07-27/manifest.yaml L1-6

## Lessons archive mentions
```
L165: - [2026-07-27] ZAGGLE phase 1 (evidence): PROCEED WITH CAVEATS, cash INDETERMINATE cap; Gate 0 AVOID mechanical (post-IPO/QIP dilution + cash conversion, not weak growth); confidence 82. Six operational notes: (1) PDF tooling dead at session start (pypdf broken on missing _cffi_backend; poppler/pdftoppm absent) so both pypdf and the Read tool failed on PDFs; fixed with pip install cffi and apt-get update then apt-get install poppler-utils (first apt attempt 404'd on the stale mirror, update fixed it). Verify PDF reads BEFORE launching stages. (2) Run folder shipped with only concalls/peer-concalls/presentation/screening; AR, results, rating arrived on a second push to origin/main not the run branch, pulled in via git checkout origin/main -- inputs/{annual-report,results,rating}. Re-inventory after any operator "re-uploaded" claim; fetch --all then compare origin/main. (3) screener-*.csv P&L/BS/CF/Quarters exports were EMPTY templates, only screener-Data_Sheet.csv carried figures; Gate 0 had to pull capex/payables/promoter/contingent from the AR. Flag empty screener exports at stage 0. (4) Stage 2 pass 3 wrote its report but returned the B02 YAML block only in chat, not in the file  [...truncated]
```
Source: origin/main:LESSONS_ARCHIVE.md §[2026-07-27] ZAGGLE phase 1 (evidence) L165

