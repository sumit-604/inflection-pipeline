=== FILE: fttcp-handoff.md ===

# CAPILLARY archive dossier (phase 3, finalize, 10 Oct 2026)

Company: Capillary Technologies India Ltd (CAPILLARY). Run folder: runs/capillary-2026-09-19. Listed 21-Nov-2025 (manifest). CMP Rs 566.65, NSE close 09-Oct-2026 (fttcp-deliberation.md header); manifest CMP Rs 484.0 and market cap Rs 3,852 Cr are stale (B10 conflicts). Market cap Rs 4,669.2 Cr diluted (566.65 x 8.24 Cr) / Rs 4,503.3 Cr basic (566.65 x 7.9472 Cr, BSE SHP Jun-2026) (B10 identity).

Units: Rs Cr unless stated. Filings, the AR and the decks print INR million on their face (B00 reporting_units; Results Q1 FY27 p.9 "All amounts in Indian Rupees million"); screener prints Rs Cr. 10 INR million = 1 Rs Cr, converted once at stage 10.

Authority order (phase 3): outputs/final/fttcp-deliberation.md (operator sign-off 10-Oct-2026) > inputs/research/web-handover-dossier.md Section 6 (operator rulings 10-Oct-2026) > B11 > B14 > B15 > earlier blocks (B10 authority_note). Company memory (companies/CAPILLARY.md) is memory, never evidence.

Final gate verdict (stage 13): PROCEED WITH CAVEATS (rule 3 PROCEED WITH FLAGS on FLAG-CASH, downgraded one level by the 60 to 74 confidence band, overall 70). Valuation decision: WATCHLIST (B11) vs AVOID (B14), OPEN for operator ruling. Size at CMP: zero under both.

---

## 0. Block and report register

| Block | Stage | Model (block string) | Status | Key output | Report |
|---|---|---|---|---|---|
| B00-inputs | 0 intake | orchestrator inline | complete | Spear OVERRIDE 2026-09-19 gate PASS; LBF1 to LBF4; sector cap row Platform / SaaS / IT services 45x; corpus GAPPED, freshness pairs OK | n/a |
| B01-gate0 | 1 | claude-sonnet-5 | complete | 68/160 AVERAGE, core 51; FLAG-GATE0, FLAG-CASH | reports/01-gate0.md |
| B02-notes (+ pass1, pass2) | 2 | claude-sonnet-5 | complete | accounting quality 6/10; FLAG-DISCLOSURE-GAP, FLAG-RPT | reports/02-notes*.md |
| B03-ardeep | 3 | claude-sonnet-5 | complete | overall quality 6; FLAG-CASH (earnings quality), FLAG-DISCLOSURE-GAP, FLAG-RPT, FLAG-GOVERNANCE-COMMITTEE | reports/03-ardeep.md |
| B04-bizmodel | 4 | claude-sonnet-5 | complete | platform; subscription 89.3%; switching costs high | reports/04-bizmodel.md |
| B05-concall | 5 | claude-sonnet-5 | complete | credibility B; 5 delivered, 3 partial, 1 missed | reports/05-concall.md |
| B06-peers | 6 | claude-sonnet-5 | complete | 1 verified, 4 partial, 0 contradicted, 2 unverifiable | reports/06-peers.md |
| B07-emoat | 7 | claude-sonnet-5 | complete | EM 24 MODEST; combined AVERAGE | reports/07-emoat.md |
| B08-promoter | 8 | claude-sonnet-5 | complete | CAUTION (5 clean, 5 caution, 0 red) | reports/08-promoter.md |
| B09-tam | 9 | claude-sonnet-5 | complete | runway STRONG; 6 downstream candidates | reports/09-tam.md |
| B09b-dossier | 09b | claude-sonnet-5 | complete | Halt 1 dossier; mental model DRAFT; FRAGILE | reports/09b-understanding-dossier.md |
| B10-valinputs (phase 3) | 10 | claude-sonnet-5-5 | complete | deliberation carried; 12 conflicts; 10 unresolved | reports/10-valinputs.md |
| B11-valuation | 11 | claude-opus-5-5 | complete | WATCHLIST; entry Rs 291.4 to 327.7; 30x governing; pillar 16.8x / 13.1x | reports/11-valuation.md; outputs/expectation-ledger.md |
| B12a | Verifier A | claude-haiku-4-5 | complete | 41/41 clean; 0 findings | reports/12a-verifier-a.md |
| B12b | Verifier B | claude-opus-5 | complete | 70 rubric / 40 strict; 9 MAJOR, 16 MINOR | reports/12b-verifier-b.md |
| B12c (phase 1 + phase3_merge) | Verifier C | claude-opus-5 | complete | 86.7 (65/75); 6 MAJOR, 12 MINOR | reports/12c-verifier-c.md |
| B12c-phase3 | Verifier C | claude-opus-5-5 | complete | 93.6 (131/140); 1 MAJOR, 8 MINOR; 12 observations | reports/12c-verifier-c-phase3.md |
| B12d | Verifier D | claude-sonnet-5 | complete | 12/12 peers used; 1 MAJOR | reports/12d-verifier-d.md |
| confidence.yaml | orchestrator | n/a | phase 3 | numerical 100, redflag 70 (strict 40), framework 91.2, peer 100, overall 70 | n/a |
| B13-synthesis-lite | 13 (phase 1) | claude-opus-5 | complete | PROCEED WITH CAVEATS (INDETERMINATE cash cap) | final/gate-recommendation.md |
| B14-thesis | 14 | claude-opus-5-5 | complete | AVOID; 8 chains; Entrepreneur Ledger 4 of 4 | reports/14-thesis.md |
| B15-devil | 15 | claude-opus-5-5 | complete | Rule H gate PASS; WEAKENED BUT ALIVE | reports/15-devil.md |
| B13-synthesis (this) | 13 (phase 3) | claude-opus-5-5 | complete | PROCEED WITH CAVEATS | final/*.md |

Model string notes: B12c.yaml phase 1 carries "claude-opus-5" against frontmatter claude-opus-5-5 (B12c-phase3 O-12). B12a ran on claude-haiku-4-5 before the 2026-10-04 ruling that moved Verifier A to Sonnet 5.5; under the standing forward application ruling it is not re-run.

---

## 1. Transition data series

Revenue basis note: screener FY23 revenue (Rs 322.68 Cr) does not match the restated UDRHP-I figure (Rs 255.37 Cr); the FTTCP draft and stage 11 use the filed figure (fttcp-draft.md 2A). Both are shown.

### 1a. Topline

| Year | Revenue from operations (Rs Cr) | YoY growth | Organic revenue (Rs Cr) | Organic growth | Net revenue (ex campaign pass through) |
|---|---|---|---|---|---|
| FY21 | 170.91 (screener row 11; B01 Block C; B12a MATCH) | NOT FOUND (FY20 not held) | NOT FOUND | NOT FOUND | NOT FOUND |
| FY22 | 223.07 (screener; B01) | 30.5% [arithmetic 223.07 / 170.91] | NOT FOUND | NOT FOUND | NOT FOUND |
| FY23 | 255.37 restated (UDRHP-I p.55, fttcp-draft 2A); screener 322.68 (B01) | restated: NOT FOUND (no restated FY22); screener 44.7% [arithmetic] | 190.7 (AR p.79) | NOT FOUND | 207.09 (UDRHP-I p.55) |
| FY24 | 525.10 (UDRHP-I p.55; screener) | 105.6% on restated (fttcp-draft 2A); 62.7% on screener [arithmetic] | 350.3 (AR p.79) | 83.7% (AR p.79) | 483.40 (UDRHP-I p.55) |
| FY25 | 598.26 (AR p.232; AR Note 22 5,982.59 mn, B12a MATCH) | 13.9% gross; 23.8% net (UDRHP-I p.55, B15 Section 3B) | 474.5 (AR p.79) | 35.5% (AR p.79) | 598.26 |
| FY26 | 734.60 (Results Q4 FY26 p.14, 7,345.99 mn; AR p.232) | 22.8% (fttcp-draft 2A) | 547.9 (AR p.79) | 15.5% (AR p.79) | 734.60 |
| Q1 FY27 | 256.64 (Results Q1 FY27 p.9, 2,566.44 mn) | +42.7% YoY vs 1,798.93 mn (B10) | 155.1 (deck p.15, Rs 1,551 mn) | +17% (deck p.15) | n/a |
| TTM Q1 FY27 | 811.35 (B10 arithmetic) | n/a | n/a | n/a | n/a |

Other topline anchors: revenue CAGR FY21 to FY26 33.88% (B01 C1; B12a MATCH); FY23 to FY26 42.2% on restated (B10; 11-valuation 3.1); organic CAGR FY23 to FY26 42% (AR p.79). Acquired books 39.6% of Q1 FY27 revenue, Rs 101.54 Cr of Rs 256.64 Cr (deck p.15 arithmetic, 11-valuation 3.1; 14-thesis Chain 3). ARR Rs 1,026.6 Cr Q1 FY27 (B05 guidance; Q1 FY27 deck p.16); B15 notes ARR is Q1 revenue x 4 by the company definition (UDRHP-I p.55 note 5; deck p.16). Quarterly YoY: Q3 FY26 +15.7% (1,840.35 vs 1,590.00 mn, Results Q3 FY26); Q4 FY26 +25.8% (1,913.46 vs 1,520.8 mn, screener quarter) (fttcp-draft 2A). Revenue streams FY26: subscription 89.3%, installation 9.8%, campaign services 0.9% (B04; AR p.190); Q1 FY27 subscription 94.5%, installation 4.8%, campaign 0.7% (deck p.23, 11-valuation 1A, 2.2). USA 55.6% of FY26 revenue (AR Note 22; B03).

### 1b. Margin

| Year | Gross margin | EBITDA margin, filed basis (incl other income, pre exceptional) | Operating EBITDA margin (ex other income) | Adjusted EBITDA margin (company definition) | Net (PAT) margin |
|---|---|---|---|---|---|
| FY21 | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | -13.4% [arithmetic: -22.83 / 170.91, B01] |
| FY22 | NOT FOUND | (22.88)% screener basis (fttcp-draft 2B) | (22.88)% (B01 via fttcp-draft 2B) | NOT FOUND | -45.2% [arithmetic: -100.84 / 223.07] |
| FY23 | NOT FOUND | (22.84)% (UDRHP-I p.55) | NOT FOUND on restated basis | NOT FOUND | -34.4% on restated revenue; -27.2% on screener [arithmetic: -87.72 / 255.37; / 322.68] |
| FY24 | NOT FOUND | (0.28)% (UDRHP-I p.55) | NOT FOUND on restated basis | NOT FOUND | -10.9% [arithmetic: -56.99 / 525.10; UDRHP-I PAT -59.38 gives -11.3%] |
| FY25 | subscription GM 66.4% (AR p.81) | 13.13% (UDRHP-I p.55) | 10.86% (B01, fttcp-draft 2B) | about 11% Q1 FY26 (deck p.15) | 2.2% [arithmetic: 13.28 / 598.26] |
| FY26 | subscription GM 67.2% (AR p.81) | 14.51% (AR p.12); AR headline EBITDA Rs 106.59 Cr incl other income Rs 13.73 Cr (Results Q4 FY26 p.14) | 12.64%, Rs 92.85 Cr (B01 data_notes; B03; B12a MATCH) | 14.55%, Rs 106.92 Cr (Q1 FY27 deck p.28) | 7.13% reported, Rs 52.39 Cr incl Rs 24.96 Cr exceptional (B10); normalised PAT Rs 32.3 Cr (AR p.82) |
| Q1 FY27 | subscription GM 66% (Q1 FY27 deck p.9) | n/a | n/a | 17.15%, Rs 44.02 Cr (deck p.28) | loss Rs 9.55 Cr after Rs 33.39 Cr exceptional fraud loss (Results Q1 FY27 p.9) |
| TTM Q1 FY27 | n/a | n/a | n/a | Rs 131.97 Cr adjusted EBITDA (B10 arithmetic, deck p.28) | n/a |

Margin anchors: best quarter Q4 FY26 adjusted margin 18.7% (357.2 / 1,913.5 mn, deck p.28; 11-valuation 3.6). Management steady state 25 to 30%+ (70% GM, about 15 to 16% tech, similar S&M, 5 to 7% G&A), no date (Q4 FY26 call; B05). Acquired books move from about 30% to about 65% gross margin (Q1 FY27 deck p.9); May-2026 deck p.51 shows FY27 inorganic GM 57%, steady state 62%, contribution margin 5% to 45% (B15 Contradiction 6). Organic EBITDA about 23% (Q1 FY27 call p.8 per B15; dossier V5 INFERENCE).

### 1c. Cash conversion

| Year | OCF (Rs Cr) | OCF / EBITDA | CFO / PAT | Debtor days | WC days (receivable days less payable days; no inventory) | WC as % of sales | Contract liabilities (Rs Cr) |
|---|---|---|---|---|---|---|---|
| FY21 | 1.18 (screener; B01) | NOT FOUND | n.m. (loss) | 117.1 (B01 M4 per 12a-verifier-a rows 57-58) | NOT FOUND | NOT FOUND | NOT FOUND |
| FY22 | 7.16 (screener; B01) | NOT FOUND | n.m. (loss) | 93.2 (screener, fttcp-draft 2C) | NOT FOUND | NOT FOUND | NOT FOUND |
| FY23 | -20.05 (screener; B01); -20.06 (UDRHP-I p.459) | NOT FOUND | n.m. (loss) | 90.6 (B01 B4) | 24.0 (B01 B4) | 6.6% [arithmetic: 24.0 / 365] | NOT FOUND |
| FY24 | 97.14 (UDRHP-I p.459; B01) | NOT FOUND | n.m. (loss) | 101.2 (B01 B4) | 50.6 (B01 B4) | 13.9% [arithmetic] | 125.67 (AR Note 22.3 p.233), 23.9% of revenue (B15) |
| FY25 | -46.20 (Results Q4 FY26 p.16, (461.99) mn; B12a MATCH) | negative | negative | 98.3 (B01; B12a MATCH) | 67.4 (B01 B4) | 18.5% [arithmetic] | 74.65 (AR p.233), 12.5% of revenue (B15) |
| FY26 | 149.91 (Results Q4 FY26 p.16, 1,499.07 mn; AR p.193; B12a MATCH) | about 140% of adjusted EBITDA (B05; B10); 1.61x operating EBITDA (fttcp-draft 2C) | 2.86x (B10; PAT incl exceptional gain) | 89.8 (B01; B12a MATCH) | 52.8 (B01 B4) | 14.5% [arithmetic] | 98.55 (AR p.233), 13.4% of revenue (B15) |

Payable days (B01 B4): FY23 66.6, FY24 50.6, FY25 30.9, FY26 37.0; trade payables Rs Cr FY23 58.86, FY24 72.83 (UDRHP-I p.394), FY25 50.58, FY26 74.38 (AR p.230 Note 18; B12a MATCH). Capex Rs Cr: FY23 28.20, FY24 36.93, FY25 47.46 (UDRHP-I p.102), FY26 39.37 (AR p.193; Results Q4 FY26 p.16); FY21 to FY22 NOT FOUND. FCF Rs Cr: FY23 -48.25, FY24 60.21, FY25 -93.66, FY26 110.54 (B01 B2; B12a MATCH). Cumulative CFO FY21 to FY26 Rs 189.14 Cr against cumulative PAT Rs -202.71 Cr (B01; B12a MATCH). FY25 to FY26 average CFO / adjusted EBITDA 57% (103.7 / 181.4; 11-valuation 3.6). Management sustainable OCF / adjusted EBITDA range 105 to 110% (Q3 FY26 call; B05). Capitalised internally generated software Rs 36.62 Cr FY26 (AR p.109; B02 finding 9 states Rs 366.15 mn, about 34% of consolidated EBITDA, a KAM). Advance from customers Rs 6.57 Cr to Rs 21.45 Cr in FY26, Rs 14.9 Cr of the Rs 23.9 Cr contract liability rise (B15 row 9).

Rating agency working capital commentary, verbatim: NONE EXISTS. The FY26 AR states the company "has neither obtained nor revised any credit rating" and lists credit ratings as "Not obtained" (AR FY26, Board's report and corporate governance report, quoted in B00 input_gaps; page number NOT FOUND in the block record). No rating rationale exists to quote.

### 1d. ROCE and ROE

| Year | Operating ROCE (O1 basis: adj EBITDA less ESOP less D&A, over invested capital ex cash) GOVERNING | Company clean ROCE (EBIT pre exceptional / capital employed incl cash) | AR published ROCE | Gate 0 computed ROCE (EBIT / total assets less current liabilities) | ROE |
|---|---|---|---|---|---|
| FY21 | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND (capital employed not held) | -181.19% (B01 A3, closing NW basis) |
| FY22 | NOT FOUND | NOT FOUND | about 0.0% (AR p.11-12 five year arc, 09b B1) | NOT FOUND | -156.63% (B01 A3) |
| FY23 | NOT FOUND | NOT FOUND | -70.43% (AR p.11-12, 09b B1) | -33.63% (EBIT -81.49 / CE 242.35; B01 A) | -62.09% (B01 A3) |
| FY24 | NOT FOUND | NOT FOUND | -14.53% (AR p.11-12, 09b B1) | -8.22% (EBIT -46.19 / CE 561.89; B01 A) | -16.16% (B01 A3) |
| FY25 | 1.5% (EBIT 6.6 / IC 431.9; dossier 6.1; deck p.26, p.28) | 2.8% (deck p.26) | 4.56% (AR p.83; B12a MATCH) | 4.56% (AR figure used) | 2.40% (AR p.83); RONW 3.0% (deck p.26) |
| FY26 | 3.9% (EBIT 21.2 / IC 549.4) | 3.0% (deck p.26) | 8.82% (AR p.83, includes the churn indemnity; B12a MATCH) | 8.82% (AR figure used) | 6.58% (AR p.83); RONW 7.4% (deck p.26) |
| TTM Q1 FY27 | 6.84% (EBIT 40.95 / IC 598.62; 11-valuation 2.3) | 5.2% (deck p.26) | n/a | n/a | RONW 5.9% (deck p.26) |
| Q4 FY26 annualised | 9.1% (dossier 6.1; O2) | n/a | n/a | n/a | n/a |
| Q1 FY27 annualised | 13.6% (EBIT 81.2 / IC 598.6; dossier 6.1) | n/a | n/a | n/a | n/a |

Capital bases: invested capital = capital employed less cash, bank and demand deposits and short term investments (Q1 FY27 deck glossary p.29): Rs 431.9 / 549.4 / 598.6 Cr FY25, FY26, 30-Jun-2026 (deck p.26). Gate 0 capital employed = total assets less current liabilities: FY23 242.35, FY24 561.89, FY25 587.96, FY26 1,042.82 (B01 Block A; UDRHP-I p.100; AR p.189). Company capital employed 30-Jun-2026 Rs 1,067.62 Cr (deck p.26; 11-valuation 2.3). Quarterly operating EBIT Rs Cr: Q1 FY26 0.6, Q2 FY26 0.7, Q3 FY26 7.4, Q4 FY26 12.5, Q1 FY27 20.3 (dossier 6.1, verified by Claude Code against deck p.28). ROIC 3.2% / 4.8% / 7.3% and CROIC 17.4% / 21.8% / 23.2% FY25 / FY26 / TTM (deck p.26; B10). CROIC = adjusted EBITDA / average invested capital, not a cash measure (deck p.29; B14 FLAG-CROIC-BASIS). Goodwill Rs 309.58 Cr (Results Q4 FY26 p.15), 24% of consolidated assets (B02) and 51.7% of invested capital (B15 Chain 4 arithmetic). Forward operating ROCE [INFERENCE]: FY27E 11.7%, FY28E 17.0% (deliberation B), FY29E 23.2%, FY30E 30.5% (11-valuation 3.3, stage 11 inference, invested capital +Rs 52 Cr a year).

CONVERTER status: NON-CONVERTER (operator Part 1; 11-valuation 2.1). Amendment 17 spot ROCE bar does not apply.

---

## 2. Catalyst inventory

### 2a. From B05 triggers (concall)

| # | Catalyst | Type | Tier | Window | Conviction | Confirm signal | Kill signal |
|---|---|---|---|---|---|---|---|
| T1 | Organic NRR holds 114 to 116% ex large account | VOLUME/PRICE-MIX | claim (management NRR figures; B05) | near term | H | NRR ex large account stays at or above 114% for 2 more quarters | NRR ex large account falls below 105% |
| T2 | SessionM margin ramp to 35 to 40% contribution margin | INORGANIC/COST | claim | medium term | M-H | sequential margin step up each quarter as disclosed | margin stalls below 15% by Q4 FY27 or logo churn appears |
| T3 | Kognitiv full migration to Capillary platform by Sep 2027 | COST | claim | medium term | M | first customer live Sep 2026, rest over the following 2 to 3 quarters | first go live slips past Sep 2026 or migration stalls |
| T4 | aiRA scales to 5 to 10% of FY27 revenue | PRICE-MIX (new product) | claim | medium term | M | paying customer count and ARR run rate step up from USD 2 to 2.5 m each quarter | paying customers stay under 10 of 150+ through FY27 |
| T5 | FY27 revenue lands at or above Rs 1,065 Cr | VOLUME + INORGANIC | documented (Q1 revenue filed) plus claim | near term | H | quarterly ARR trajectory holds above Rs 1,026 Cr | guidance walked back |
| T6 | New logo / ACV momentum ex large account +30 to 40% FY27 | VOLUME | claim | medium term | M | full year new ACV growth in range | growth below 15% |
| T7 | Cash conversion normalises toward 105 to 110% | COST / governance | claim | near term | L-M | management reconciles the OCF / EBITDA gap | ratio unexplained and debtor days rise |
| T8 | Fraud / forensic audit resolves cleanly | governance | documented event (Reg 30 06-Jul-2026, 31-Jul-2026) | near term | L | KPMG findings disclosed, clean controls verdict, insurance quantified | further control lapses or adverse findings |

Dropped trigger (B05): tech plus corp cost as % of revenue (28% to 18%), tracked only on the Q3 FY26 call. Timeline slippage (B05): Kognitiv framed 12 to 18 months (Q4 FY26), now about 28 months from the May 2025 deal.

### 2b. From B07 catalysts_12m (emerging moat)

| # | Catalyst | Tier | Window | Anchor | Confirm | Kill |
|---|---|---|---|---|---|---|
| E1 | Kognitiv first customer live on Capillary platform | claim | stated 01-Sep-2026 | Q1 FY27 concall; Inv. Pres. slide 27 | dated go live on the Q2 FY27 call (B14 checklist row 5) | no dated go live on the Q2 call |
| E2 | aiRA rupee revenue disclosure vs 5 to 10% of FY27 revenue target | claim | FY27 quarterly | Q1 FY27 concall; B05 | aiRA revenue in rupees on a consistent basis | paying customers under 15 by Q4 FY27 (tracker row 11) |
| E3 | SessionM contribution margin ramp toward 35 to 45% | claim | quarterly FY27 to FY28 | Q4 FY26 / Q1 FY27 concalls | ARR at least USD 27 m and break even by Q4 FY27; CM at least 15% by Q4 FY28 (ledger L6) | falsifier 3 |
| E4 | KPMG forensic final report and insurance settlement, Czech fraud | documented | H2 FY27 (5 to 8 months from Jul 2026) | Reg 30 06-Jul-2026, 31-Jul-2026; Q1 FY27 deck slide 21 | Reg 30 outcome, no insider finding, insurance quantified | insider finding (falsifier 5) |
| E5 | FY26 top 10 customer concentration disclosure | documented pending (taxonomy flag, B12c O9) | next AR (FY27) or a quarterly filing | AR Note 36(iii), incomplete | FY27 AR names the >10% customer and top 10 share | n/a |

### 2c. Phase 3 catalyst register (expectation ledger, stage 11; probabilities NOT operator ruled)

| Row | Catalyst | PAT increment Rs Cr | p | Tier | Confirm metric | Confirm by |
|---|---|---|---|---|---|---|
| L1 | FY27 revenue reaches Rs 1,065 Cr | +4.94 | 0.85 | T2 | H1 FY27 revenue at least Rs 526 Cr; FY27 at least Rs 1,065 Cr | Nov-2026; May-2027 |
| L2 | Revenue compounds at least 10% a year FY28 to FY30 (to Rs 1,417.5 Cr) | +45.35 | 0.75 | T2 | blended NRR at least 105% in Q4 FY27 deck; FY28 revenue at least Rs 1,172 Cr | May-2027; May-2028 |
| L3 | Growth lifts from 10% to 15% a year FY28 to FY30 (to Rs 1,620 Cr) | +26.05 | 0.45 | T3 | H1 FY27 cc organic at least 15%; FY28 revenue at least Rs 1,225 Cr | Nov-2026; May-2028 |
| L4 | Organic operating leverage toward 25% organic EBITDA margin | +12.54 | 0.55 | T2 | organic margin up in cc two quarters; adjusted margin at least 17% in Q2 FY27 | Feb-2027 |
| L5 | Kognitiv migration completes, retained revenue at least 80% of FY26 | +20.91 | 0.40 | T3 | dated first migrated customer; full migration at 80% retained | Nov-2026; Sep-2027 (reported Nov-2027) |
| L6 | SessionM ARR at least USD 27 m and break even by Q4 FY27; CM at least 15% by Q4 FY28 | +33.45 | 0.40 | T3 | falsifier 3; then CM 15% | May-2027; May-2028 |
| U1 | aiRA reaches 5% of revenue | +15.00 | 0.15 | T3 | 15+ paying customers; Fortune 50 client live | May-2027 |
| U2 | Bull path beyond base (20% growth, 25% margin) | +74.14 | 0.15 | T3 | FY28 revenue at least Rs 1,320 Cr and margin at least 20% | May-2028 |
| D1 | Optum warrant charge to about Rs 31 Cr a year | -8.00 | 0.90 | netted | contra revenue line in Note 22 | Jul-2028 |
| D3 | Optum repriced >20% or not renewed by Mar-2029 | -30.00 | 0.25 | netted | Optum account revenue each quarter | Mar-2029 |
| D4 | Below EBITDA cost growth (D&A, ESOP, finance) | -16.80 | 0.90 | netted | FY27 D&A at or below Rs 85 Cr, ESOP at or below Rs 14 Cr | Nov-2026; May-2027 |
| D5 | Adjusted margin falls to 15% | -13.92 | 0.20 | netted | adjusted margin below 15% in any quarter | each quarter from Nov-2026 |

Ledger totals (expectation-ledger.md): T2 gross Rs 45.11 Cr, downside -Rs 32.60 Cr, T2 net Rs 12.51 Cr, T3 Rs 46.84 Cr, total Rs 59.34 Cr; probability weighted FY30 PAT Rs 116.70 Cr, EPS Rs 14.16. All 12 rows OPEN. D2 (tax normalisation, -Rs 25 Cr) not carried: run rate base already taxed at 25%.

Devil's advocate counters to the ledger (B15): L5's 80% line sits above the company's 68% acquired revenue retention record (May-2026 deck p.48) and the 75% plan (deck p.51, p.62); the bridge's Kognitiv lever (Rs 27.9 Cr EBITDA) exceeds management's Rs 10 to 20 Cr (Q1 FY27 call p.11); proof gate odds about 0.35 to 0.40 [INFERENCE].

---

## 3. Flags with complete underlying findings

### FLAG-PROMOTER: not active (B08 verdict CAUTION; flag fires only on CONCERN or AVOID)

Full B08 record for the archive:
- Verdict CAUTION; scorecard clean 5, caution 5, red 0; deal breakers none; pledge 0% at Dec-2025, Mar-2026, Jun-2026, stable, no NDU or other encumbrance (B08).
- Adverse findings:
  1. Promoter group entity Gowthami Agro Industries Private Limited received a notice seeking information from an Andhra Pradesh SIT on the 2019 liquor policy; a separate AP probe alleges about Rs 3,200 to 3,500 crore in kickbacks; no evidence ties the entity or the Boddu family to any chargesheet. Notice VERIFIED; implication UNVERIFIED (UDRHP-I p.4461-4464; web search 2026-09-19).
  2. Institutional shareholders voted 55.9% AGAINST the Feb-2026 postal ballot extending ESOP 2021 to subsidiary employees; passed on promoter (100% for) and retail (99.995% for) votes. VERIFIED (Reg 44(3) voting results 13-Mar-2026, scrutinizer BMP & Co. LLP).
  3. Head-Finance resigned 29-May-2026 and Head-Corporate Development 27-Jul-2026, inside the window of the Jul-2026 fraud and KPMG audit; causal link not established. Dates VERIFIED (Reg 30 20260529-e43c3912, 20260727-bcf6b0ea; fraud 20260706-07f4090c; forensic 20260731-17c4e00c).
  4. CTIPL sold 4.14% (3,292,428 shares) on 10-Aug-2026 by block, 48.92% to 44.78%, to fund Peak XV's exit; other PE investors hold >30% of CTIPL and may exit similarly. VERIFIED (Reg 29(2) 20260811-B8C7ECCC; CTIPL filing 20260811-B44A8DBB image; clarification 20260825-9a49d6e4). Block price Rs 520.86, Rs 171.5 Cr (dossier V6).
  5. Chairperson Neelam Dhawan holds Chairperson of 3 + Member of 9 = 12 audit / stakeholder committee positions in other listed companies, at or above the LODR Reg 26(1) ceiling depending on count method; not flagged by the secretarial audit; registry check not run (Corporate Governance Report p.52; AGM Notice Annexure-A p.268).
- Transition evidence (B08): Peeyush Ranjan (ex Google, Airbnb, Flipkart Internet) appointed independent director 07-May-2025 (UDRHP-I p.328-329); Kotak Mahindra MF crossed 5% on 14-Aug-2026 (Reg 29(1) 20260817-D8805431); Audit Committee self-initiated the KPMG forensic audit within 25 days (20260731-17c4e00c); voluntary clarifications on ESOP pricing (24-Feb-2026) and the CTIPL sale (25-Aug-2026) (20260224-e9874d34; 20260825-9a49d6e4); transparent postal ballot mechanism (Reg 44(3), 13-Mar-2026).
- OR-14 sizing read (B14): governing kind STRUCTURE; integrity items none evidenced; ledger heads 4 of 4 (built; capital raised vs deployed; contrarian, company reported; skin, thin); TRUSTWORTHY for sizing; tripwires: further CTIPL or PE block sales; KPMG insider finding (re-classifies to INTEGRITY, Small ceiling, possible promoter AVOID); finance SMP turnover inside the fraud window; chairperson committee count; any chargesheet naming Gowthami Agro Industries or the family.
- Additional promoter facts (B14 3G, B15 Chain 6): CTIPL sold 8,540,738 shares in the Nov-2025 OFS, about Rs 492.8 Cr at Rs 577 [arithmetic, UDRHP-I p.84 vs AR p.62, ties to 9,228,796 OFS shares, AR p.149]; CTIPL cost Rs 34.75 per share (UDRHP-I p.84); founder direct 1,733,380 shares, 2.18% (AR p.62), did not sell in the OFS; founder 7.53% economic / 8.00% voting of CTIPL (UDRHP-I p.355-356); look through about 5.6% [INFERENCE]; Pandora Holdings and Neytiri Holdings own 44% of CTIPL, owners PENDING LIVE VERIFICATION (ACRA). CTIPL issues the Optum warrants "on behalf of the Group", Rs 35.49 mn FY26 (AR Note 13 p.227; B15 FLAG-WARRANT-ISSUER).

### FLAG-CASH: active

- Determination: GROWTH-INDUCED (operator ruling O3, 10-Oct-2026, accepting draft R10, "prepayment timing"; dossier 6.2). Phase 1 determination INDETERMINATE (B13-synthesis-lite) superseded.
- Origin (B01 FLAG-CASH): "Working Capital Days worsened from 24.0 (FY23) to 52.8 (FY26) even as absolute CFO improved from Rs -46.2 Cr (FY25) to Rs +149.9 Cr (FY26); FY26 improvement leans on payable-days compression (66.6 to 37.0 days) rather than receivable discipline."
- Mechanism correction (Verifier C F-G2, MAJOR): 66.6 to 37.0 is FY23 to FY26 and consumes cash; FY26 receivable days fell 98.3 to 89.8 and payable days rose 30.9 to 37.0, both helping FY26 CFO; the multi year deterioration stands. B10 still carries the struck reading (F-V7).
- B03 FLAG-CASH (earnings quality, not cash quality): FY26 PAT growth +294.5% is 49% of PBT from the one off Kognitiv churn indemnity (Rs 249.60 mn) plus a net tax credit of Rs 12.78 mn against Rs 511.10 mn PBT; AR EBITDA Rs 1,065.85 mn includes Rs 137.34 mn other income; operating EBITDA Rs 928.51 mn, 12.64%; CFO genuinely improved with the one off correctly excluded.
- Cited evidence for GROWTH-INDUCED: contract liabilities Rs 125.67 / 74.65 / 98.55 Cr FY24 to FY26 (AR Note 22.3 p.233); FY26 build Rs 23.9 Cr of Rs 149.91 Cr CFO (B10); management: "we bill and collect money upfront in a healthy growing business" (Q4 FY26 call, Anant, [p10] L409-412, per B12b). O4 reasons for the 1.15x Pillar 2 multiplier: "upfront billing, CROIC 23.2% TTM (deck p.26), CFO/adjusted EBITDA 140% in FY26".
- Rating agency verbatim quote: none exists ("has neither obtained nor revised any credit rating", AR FY26 per B00).
- Capex commissioning timeline: not a capex led business (asset light, capex_embedded_growth_pct 0, B07; B09 capacity_check sufficient). IPO objects at 30-Jun-2026: net proceeds Rs 322.91 Cr, Rs 119.69 Cr used (Rs 85.01 Cr acquisitions incl SessionM, Rs 34.68 Cr cloud), Rs 203.22 Cr unused incl Rs 71.58 Cr R&D and Rs 10.34 Cr computer systems untouched (Results Q1 FY27 p.11; B14 3G). Acquisitions object Rs 12.97 Cr unused of Rs 97.99 Cr (B14 Chain 4).
- Receivables composition (B02 receivables_trend, AR Note 8 p.222-223): consolidated trade receivables +12.2% vs revenue +22.8%; credit impaired receivables down 65.3%, Rs 128.28 mn to Rs 44.52 mn; unbilled revenue Rs 274.51 mn to Rs 262.38 mn. Standalone unbilled revenue +126.5% (Rs 283.36 mn to Rs 641.83 mn, Note 8 p.146) is intercompany against Capillary Pte Ltd and nets out on consolidation. Standalone receivable turnover 3.97x to 3.49x (Note 36 p.175). AR receivable turnover 4.30x FY26 implies about 84.9 days on average receivables (AR p.82; B01).
- Counter evidence (B15): contract liabilities 23.9% (FY24), 12.5% (FY25), 13.4% (FY26) of revenue; Rs 51.0 Cr fall in FY25; Rs 14.9 Cr of the FY26 rise is "advance from customers", a lumpy line; May-2026 deck p.58 calls upfront billing "model design, not a one-off"; SessionM's likely assumed prepayments (USD 11.0 m EV to price gap on "debt-free entities", Q1 FY27 call p.22) unwind in FY27.
- Pillar 2: operator 1.15x vs chunk 02 band reading 1.00x on filed CFO / PAT (volatile: FY25 CFO negative, FY26 2.86x); Track 2 at 1.00x would be 14.9x (11-valuation 2.4).
- Falsifying quarterly metric: H1 FY27 OCF / adjusted EBITDA below 60% (Q2 FY27 results, about Nov-2026; tracker row 10 falsifier "below 60% for FY27", operator approved, dossier Section 5). Secondary: H1 FY27 receivable days above 98 (B14 checklist row 7); H1 PPA assumed contract liabilities above Rs 60 Cr (B15 early warning 7).

### FLAG-GATE0: active (informational, caps nothing)

- Score: grand 68/160 (Verifier C 66/160); core 51/100; moat 17/60, 4 moats, STRONG (Verifier C 15/60, 3 moats, MODERATE); classification AVERAGE on both (B01; B12c F-G1).
- Blocks: A 5, B 2, C 10, D 20, E 14 (B01).
- Deal breakers (B01): Block A below 8 (score 5), cap GOOD, non binding; Block B below 8 (score 2), cap GOOD, non binding; median ROCE below 10% (-1.83%, FY23 to FY26), cap AVERAGE, binding; cumulative CFO / PAT below 0.50 (cumulative PAT Rs -202.71 Cr, CFO Rs +189.14 Cr), cap AVERAGE, binding; PAT negative FY24 (Rs -56.99 Cr), cap AVERAGE, binding.
- Depressors: historical (PAT negative FY21 to FY24; loss years inside the window). FY25 to FY26 inflection real but two years deep; FY26 carries the Rs 24.96 Cr exceptional gain (B01).
- Open operator ruling (B12c O4): a four year balance sheet window would trigger the LIMITED downgrade, AVERAGE to AVOID.
- Alternative D2 reading (B12c O1): strip the one off and interest cover falls 10.36x to 5.79x, core 51 to 50.
- Effects downstream: Gate 0 AVERAGE bars Medium size; feeds the AVOID leg of Role 2 Section 7; Tier B unavailable; median ROCE deal breaker cannot clear on FY27 data on B01's series, so AVOID may bind to FY28 data (B14 Section 7 [INFERENCE]).

### Other flags on the record (full text)

- FLAG-DISCLOSURE-GAP (B02, B03): contingent liabilities note (Note 31 standalone / Note 34 consolidated) promises a claims description and supplies none; major customer >10% sentence (Note 36(iii)) has no name, amount or Nil; no capital commitments note despite Rs 979.85 mn earmarked from IPO proceeds; forward contract hedging policy stated with zero notional / MTM disclosed. Confirmed genuine, not extraction loss.
- FLAG-RPT (B02, B03): standalone revenue 75.7% related party (Capillary Pte Ltd Singapore hub); RP receivables 80.6%, RP payables 81.1%; FY26 transfer pricing study still in process at the 06-May-2026 sign off.
- FLAG-GOVERNANCE-COMMITTEE (B03): chairperson committee count as in FLAG-PROMOTER item 5.
- FLAG-EMOAT-CONCENTRATION, FLAG-EMOAT-COPYABLE-MOAT, FLAG-EMOAT-CASH-CONVERSION (B07): C1 sits above undisclosed FY26 concentration; H1 fails the I2 cannibalisation barrier test; F2 capped at Moderate by the OCF / EBITDA question.
- Valuation flags (B11, all text): FLAG-EXITPE-OVERRIDE; FLAG-RECOGNITION-GAP (CLOSED, PRICED NARRATIVE (TRAP)); FLAG-HURDLE (STOP; HR 0.75 ledger, base 1.13, bull 1.70, bear 0.39); FLAG-A25 (starter fails, T1 + T2 54.9% vs 75%, starter Rs 415.2); FLAG-DISPERSION (111.7%, Small); FLAG-C2-PROBABILITIES (ledger rebuilt to FY30, probabilities stage 11, not operator); FLAG-CASH (1.15x vs 1.00x band); FLAG-A14-FADE (A14 faded FY30 EPS Rs 19.67, value at 30x Rs 647, -Rs 50); FLAG-METHODS (P/E at 30x Rs 697.1 vs DCF Rs 412.5, 69% spread); FLAG-BRIDGE (Rs 57 at 31-Mar-2026 vs Rs 51.5 at 30-Jun-2026); FLAG-MACRO-STALE (August 2026 sheet); FLAG-PROOF-GATE (NOT FIRED); FLAG-CROSSGRADE (no GEMINI_API_KEY); FLAG-MULTI-RUNG (30x above R5 from R1 to R2).
- Thesis flags (B14): FLAG-VERDICT-CONFLICT; FLAG-CROIC-BASIS; FLAG-SESSIONM-BRIDGE; FLAG-KPMG-OVERDUE; FLAG-LEDGER-PROBABILITIES.
- Devil's advocate flags (B15): FLAG-ORGANIC-DEFINITION; FLAG-MGMT-OUTLOOK-VS-BASE; FLAG-RETENTION-BASE-RATE; FLAG-KOGNITIV-LEVER; FLAG-KOGNITIV-PRICE-BASIS (Rs 147.23 Cr filed, AR Note 39 p.254, vs about Rs 122 Cr presented, AR p.80); FLAG-SESSIONM-FIVE-FIGURES; FLAG-CASH-INTENSITY; FLAG-WARRANT-ISSUER; FLAG-GOODWILL-GROWTH (impairment test 4 to 10% growth, AR Note 4 p.220); FLAG-ZONE-MULTIPLE; FLAG-T1-VS-FY27E (run rate PAT Rs 57.36 Cr vs approved FY27E Rs 51.4 Cr, Rs 21.7 per share); FLAG-UGLINESS-CONTESTED.
- Stage 13 flag: FLAG-VERIFIER-A-PHASE3-COVERAGE (B12a phase 1 scope only; no OR-32 mandatory fields).

---

## 4. Credibility grade

- B05 credibility_grade: B. Basis: "5 of 9 tracked promise-delivery items fully delivered (incl. SessionM ahead of schedule, FY27 guidance sharpened not walked back), only 1 unreconciled miss (cash-conversion ratio); offset by under-detailed disclosure of the cyber-fraud/forensic-audit on the Q1 FY27 call and only 3 quarters of listed track record." Excuse pattern: "balanced-to-honest on operating misses; understated on the governance event".
- promise_delivery_score: delivered 5, partial 3, missed 1; credibility ratio 0.72 = 6.5 / 9 (11-valuation 3.1).
- repeated_evasions: none (empty list, B05).
- Verifier B concurrence: lower, B- to C+ (B12b). Spot checks 5 checked, 3 confirmed, 2 wrong.
- Operator ruling O9 (10-Oct-2026): B (operating delivery); Pillar 3a +2x stands; bull case enters the Hurdle Ratio at face value.
- Mode: concall mode (3 transcripts: Q3 FY26 Feb-2026, Q4 FY26 May-2026, Q1 FY27 Aug-2026; B00).

Guidance versus delivery (B05 promise_delivery rows, with Verifier B corrections):

| Promised in | Promise | Delivered (quarter anchor) | B05 outcome | Verifier B note |
|---|---|---|---|---|
| Q3 FY26 call | Tech plus corp cost keeps falling as % of revenue | FY26 EBITDA margin 14.7%; organic margin about 23% by Q1 FY27 | delivered (directionally) | metric 28% to 18% not restated (dropped trigger) |
| Q3 FY26 call | OCF / adjusted EBITDA normalises to 105 to 110% | FY26 about 140% (Rs 150 Cr / Rs 107 Cr), Q4 FY26 | missed / unreconciled | OVERSTATED: a norm, not a promise; Q4 FY26 [p10] L409-412 gave the upfront billing reason |
| Q4 FY26 call | Q1 FY27 margin softness from salary hikes | Q1 FY27 adjusted margin 17% (organic about 23%) | delivered, better than guided | wrong: margin fell from about 19% (Q4 FY26 [p6] L250-251) to 17% (Q1 [p8] L316), as guided |
| Q4 FY26 call | SessionM break even Y1, positive margin Y2 | "fully profitable", Rs 5 to 6 Cr FCF in two months (Q1 FY27 call) | delivered, ahead of schedule | overstated: cash, not EBITDA, in an upfront billing model (Q1 [p7] L270-273) |
| Q4 FY26 call | FY27 revenue Rs 1,000 to 1,050 Cr | Q1 FY27 ARR Rs 1,026.6 Cr; guide sharpened to "will definitely beat Rs 1,065 Cr" and Rs 172 Cr EBITDA (Q1 FY27 call p.24) | on track, reaffirmed | none |
| Q3 FY26 call | AI wave will not disrupt the system of record position | reaffirmed with agentic commerce framing, Q1 FY27 | consistent | none |
| Q3 FY26 call | aiRA monetisation clarity in a couple of quarters | Q4 and Q1 gave numbers; paying under 10 of about 150 | partial | MAJOR: sizing regressed, Q4 4 to 5% of revenue vs Q1 USD 2 to 2.5 m |
| Q4 FY26 call | Kognitiv AI led upgrade cycle 12 to 18 months | first customer Sep 2026, full by Sep 2027, about 28 months from May 2025 | partial | SessionM upgrades 2 to 3 years also not captured |
| Q4 FY26 call (implicit) | guidance discipline, no over promising | declined to raise guidance in Q1 FY27 call | delivered | none |

Guidance items on record (B05): 9M FY26 new order book Rs 66 Cr vs Rs 53 Cr; ARR +21% over Mar-2025 (9M FY26); FY26 revenue Rs 734 Cr (+23%), adjusted EBITDA Rs 107 Cr (14.7%), normalised PAT Rs 32 Cr; SessionM about USD 15 m EBITDA potential, 45% CM post migration; steady state EBITDA 25 to 30%+; Q1 FY27 revenue Rs 256 Cr (+43%, organic +17%), adjusted EBITDA Rs 44 Cr (17%), normalised PAT Rs 25 Cr; FY27 new ACV at least 30 to 40% above FY26 Rs 121 Cr; ESOP Rs 12 to 15 Cr; aiRA 5 to 10% of revenue target. AR guidance table (B03): Rule of 40 target at least 40, 38 achieved FY26 (High credibility); acquisition gate 20%+ ROIC per deal (Medium-high; 3 of 5 deals evidenced); acquired book CM 40 to 45% within 3 to 4 years (Medium; Persuade 41.2%, Brierley plus Persuade 40.4%, Rewards+ 45%, AR p.80).

---

## 5. Scorecards and market sizing

### Gate 0 (B01; Verifier C B12c)

grand_total 68/160 (VC 66); core_score 51/100; moat_score 17/60 (VC 15); blocks A 5, B 2, C 10, D 20, E 14; moats_confirmed 4/12 (M1, M4, M10, M11; VC strikes M11: 3/12); moat_class STRONG (VC MODERATE); classification AVERAGE; deal breakers as in Section 3 FLAG-GATE0. Peer EBITDA margins FY26 (old peer set, now excluded by O10): NEWGEN 25.78%, INTELLECT 19.22%, UNIECOM 17.34%, median 19.22% vs Capillary 12.64% (B01; B12a MATCH).

### Emerging Moat (B07; Verifier C)

em_score 24.0 (VC 21.9 before F-E1 / F-E6 rescoring); em_classification MODEST; combined assessment AVERAGE. Active categories: C1 customer ecosystem, Strong, documented (VC: claim tier, 2.8); H1 industry consolidation beneficiary, Strong, management claim, fails I2; B2 qualification lock in, Moderate, documented (VC: table stakes, HL 2.0); A3 process innovation, Moderate, claim; D1 proprietary data asset, Moderate, claim; F2 execution moat, Moderate, documented (VC: 2.1, double credit with H1). Evidence mix: documented 18, claim 14, inference 2 (VC recount: 12 items across 5 scan categories plus 6 profile items). Strip C1 and H1: about 12.4 (B07). I1 (Category 21, talent asymmetry) and I2 (Category 22, cannibalisation barrier) score 0. R&D incl ESOP Rs 1,212 mn disclosed (AR p.41; VC F-E6).

### Accounting quality (B02)

accounting_quality 6/10 (B03 overall quality 6: governance 6, accounting 6, balance sheet 6, earnings 5). Going concern: none beyond standard basis. Restatements: labelling carryover only (Note 2.1 p.195).

| # | Finding | Note ref | Rating |
|---|---|---|---|
| 1 | Standalone revenue 75.7% related party (Singapore hub); RP receivables 80.6%, payables 81.1%; FY26 TP study in process | Note 20/32 standalone, p.155-156, 166-168 | WATCH |
| 2 | Rs 249.60 mn one time churn indemnity (Kognitiv) = 49% of consolidated PBT | Note 28 consolidated p.235; MD&A p.82 | WATCH |
| 3 | Capillary Technologies LLC (US) contributed 104.9% of consolidated profit; -45.6% elimination | Note 40 p.274 | WATCH |
| 4 | Goodwill Rs 3,095.76 mn (24% of assets), 27.70% WACC, no sensitivity headroom; CGUs 1 to 2; KAM | Note 4 p.219-220; KAM p.180-181 | WATCH |
| 5 | Standalone ratios fell post IPO with a contradictory footnote | Note 36 p.174-176 | WATCH |
| 6 | IFC: books backup not on India servers daily; audit trail at third party host unconfirmed; opinion unmodified | Auditor's Report Annexure II p.184-185, 188 | WATCH |
| 7 | Contingent liabilities note promises claims description, supplies none | Note 31 p.166; Note 34 p.244 | WATCH |
| 8 | Major customer >10% sentence incomplete | Note 36(iii) p.246-247 | WATCH |
| 9 | Internally generated software capitalised Rs 366.15 mn (about 34% of EBITDA), 3 year amortisation; KAM | Note 4 / 2.3(f) p.131-132, 219; KAM p.178-179 | WATCH |
| 10 | Standalone unbilled revenue +126.5%, intercompany, reverses on consolidation | Note 8 p.146 vs p.222 | WATCH |
| 11 | Zero forward contract balance despite a stated hedging policy, 12 currency exposure | Note 34(2) p.172-173 | WATCH |
| 12 | Total Fund liquidity definition excludes Rs 3,232.40 mn of fixed deposits | Note 35 p.173-174; Note 38 p.253 | WATCH |
| 13 | Kognitiv acquired for CAD 23.44 mn; goodwill Rs 909.53 mn = 62% of consideration | Note 39 p.254 | WATCH |
| 14 | No capital commitments note despite Rs 979.85 mn earmarked for inorganic growth | full document search | WATCH |
| 15 | SessionM (USD 20.00 mn) signed 24-Feb-2026, completed 01-May-2026; not in FY26 figures | Note 44 p.259 | CLEAN / INFORMATIONAL |

B03 missing risks (MD&A risk table p.84-85 omits): cybersecurity; goodwill impairment; FX / treasury; promoter / PE lock in overhang; key person / founder dependency.

### Market (B09)

tam_cr: conservative 8,550, realistic 11,115 (software only pool); sam_cr 5,835 (52.5% of TAM); som_3yr_cr 1,361; som_5yr_cr 1,913; som_implied_revenue_cagr 22.8% (3 year), 21.1% (5 year); current SAM share 12.6%; revenue headroom 7.9x; TAM growth 12%; runway_class STRONG; mgmt_claim_cr 155,610 (USD 18.2 bn Zinnov); mgmt_claim_ratio 18.2, read "inflated" (software only denominator; about 1.4x against the broad market). Methods: top down broad market (MarketsandMarkets USD 12.89 bn, Grand View USD 13.59 bn, Roots USD 13.63 bn, Fortune USD 15.19 bn; B12a MATCH), bottom up software only (adopted), peer aggregation, regional. Stale data: Straits Research 2022. Capacity: sufficient (asset light). Base FY29 revenue Rs 1,410 Cr sits 3.6% above SOM; the excess is the closed SessionM deal (11-valuation 3.1).

### Peer triangulation (B06; Verifier B and D corrections)

- Verified: non COGS cost base grows well below revenue growth (NEWGEN, INTELLECT; 4 anchors).
- Partially verified: M&A margin bridge (INTELLECT; VC basis mismatch: operating vs gross margin); FX tailwind of similar order (INTELLECT); agentic AI manageable for system of record software (NEWGEN, UNIECOM, INTELLECT; Verifier D: NEWGEN cell reverses who wins); deal cycle length (NEWGEN, INTELLECT).
- Contradicted: none.
- Unverifiable: loyalty software under 10% of loyalty market (checked NEWGEN, INTELLECT, UNIECOM); 110%+ NRR top decile (UNIECOM, NEWGEN).
- Net narrative effect: complicates. Peer set for valuation replaced by O10 (Eagle Eye, Affle, RateGain, Braze, Klaviyo, Tanla or Route Mobile; Newgen and Intellect excluded; Zaggle reference only). Held live peer data: RateGain trailing P/E 41.8x, EV/EBITDA 21.6x, ROCE 12.6% (Value Research 09-Oct-2026 per Claude web; dossier 6.3); Eagle Eye about 13x EBITDA, 2.9x ARR, NRR 111% (dossier V4, SECONDARY, older); Adyen / Talon.One about 12.5x ARR (SECONDARY).

---

## 6. Valuation pillar detail (stage 11 ran; B11, 11-valuation.md)

- Methods (1A): P/E on one year forward operating EPS 80%; DCF 20%; EV/EBITDA, EV/ARR, P/B, SOTP, DDM not applied (reasons in 11-valuation 1A).
- Earnings base (A21): single quarter annualised Q1 FY27. Adjusted EBITDA Rs 44.02 Cr - ESOP 3.69 - D&A 20.04 - finance 1.17 = operating PBT Rs 19.12 Cr a quarter (deck p.28); x 4 x 0.75 = operating PAT Rs 57.36 Cr; EPS Rs 6.961 on 8.24 Cr diluted; run rate P/E 81.4x. One offs stripped: fraud loss Rs 33.39 Cr; non operating income Rs 5.68 Cr a quarter; tax at 25% (one time DTL Rs 1.61 Cr). Annual model divergence 77.6% vs AR normalised FY26 PAT Rs 32.3 Cr.
- Pillar 1: FTTCP ROCE RECOVERING (p about 0.65, Moderate); 60/40 of TTM 6.84% and FY28E 16.99% = 10.90%; route A operational (O1); base PE 0.5 x 10.90 + 7.5 = 12.9x.
- Pillar 2: GROWTH-INDUCED (O3); cash multiplier 1.15x (O4) vs band reading 1.00x; growth offset 0; C = 12.9 x 1.15 = 14.835x.
- Pillar 3: 3a +2x (SOM CAGR 22.8% and grade B, O9); 3b 0 (EM 24 below 25); 3c 0; A16 gate: minimum ROCE = r 14.5%; eligible from FY28 (base); not eligible in bear. growth_premium 2.
- Strategic premium +0x (no scarcity; recovery credited in Pillar 1). shared_catalyst_flag true.
- UA: not applied (listed under 12 months; Gate 0 core 51 and EM 24 miss; Kotak MF above 5%). ua_applied false.
- Sector cap: Platform / SaaS / IT services 45x; Category Break override N. sector_cap_used 45.
- destination_pe_track2_additive: F = 14.835 + 2 + 0 = 16.835x; H 16.8x (record 16.9x); range 15.5x to 18.0x.
- destination_pe_track1_rrm: r 14.5% (small cap 14.0 + complexity 0.5); RRM 1 + (13.5 - 14.5) x 0.12 = 0.88; 14.835 x 0.88 = 13.1x; range 12.0x to 14.0x. Divergence 22.5%.
- Governing: operator approved 30x on both tracks (O5, A20.9), range 28.0x to 32.5x; +78.6% vs Track 2, +129.0% vs Track 1; 30x needs a Pillar 1 ROCE of about 34%; DCF implies 16.7x; Year 3 metric pillar about 24x; 4G check 6 FAIL. Step 1C: PENDING LIVE PEER TABLE; relative route opens above 24.0x per B11, 18.7x per Verifier C F-V1 source reading; Section 1B reaches 30x only at an adjusted peer base of 30x or more.
- Relative PE: pillar 0.82 / approved 1.46 relative to Nifty 50 20.5x (stale); run rate 3.97 relative.
- Recognition gap: CLOSED; matrix PRICED NARRATIVE (TRAP). Market implied: price needs FY30 EPS Rs 26.45 at 30x (56.0% CAGR) to earn r; evidence supports 26.7% (ledger) to 45.3% (base); PRICED-WE-ARE-LATE. VC F-V5: Reading 1 at 25% gives EPS CAGR 22.8%.
- hurdle_ratio: ledger 0.75; base 1.13; bull 1.70; bear 0.39; Tier A threshold 1.953; hurdle_verdict STOP; caps nothing (OR-2).
- Scenarios (O11, dossier 6.5): revenue FY27 to FY30 bear 1,020 / 1,122 / 1,234 / 1,358; base 1,065 / 1,225 / 1,410 / 1,620; bull 1,100 / 1,320 / 1,584 / 1,901. Adjusted EBITDA margin bear 15% flat; base 16.2 / 18.0 / 19.9 / 22.0%; bull 17 / 20 / 23 / 25%. FY30 EPS bear Rs 7.44, base Rs 21.33, bull Rs 32.15.
- Margin bridge (base): 14.55% FY26 to 19.90% FY29 to 22.00% FY30: printed run rate +260 bps; organic leverage +65 / +103; Kognitiv +109 / +172; SessionM +175 / +275; Optum warrant -74 / -64 (11-valuation 3.2).
- fair_values: P/E at 30x bear Rs 280.1, base Rs 697.1, bull Rs 1,021.6; DCF bear Rs 175.5 (14%, g 4%), base Rs 412.5 (12%, g 5%, TV 88.2%), bull Rs 784.8 (11%, g 6%). Weighted Track 1 = Track 2: bear Rs 259.2, base Rs 640.1, bull Rs 974.2. Pillar P/E only: Track 2 Rs 182 / 415 / 597; Track 1 Rs 154 / 336 / 478.
- Returns: weighted bear -23.0%, base 4.1%, bull 19.8%; expected CAGR (Good 25/50/25) 1.3%; P/E only 3.8%; Excellent 3.4%; ledger basis -5.3%. Return matrix: 0 of 9 cells at 25%, 3 of 9 at 15%.
- entry_range: Rs 291.4 (30%) to Rs 327.7 (25%); P/E only Rs 317.3 to Rs 356.9. mos_price Rs 229.4 (reference; A25 governs). Upside / downside 0.24x; clears 2x at Rs 386.2 (B14).
- A24 at CMP: T1 46.9% (Rs 265.83 incl net cash Rs 57), T2 8.0% (Rs 45.54), T3 30.1% (Rs 170.52), residual 15.0% (Rs 84.76); at 16.8x residual 47.9%; bridge outside tiers (VC O-1) residual 25.0%.
- A25: fast growth Y; starter fails (54.9%); starter Rs 415.2 (VC O-1 reading about Rs 339); add to Medium Rs 443.1 but Gate 0 bars; dispersion 111.7%, Small.
- A19: FV today Rs 265.8, end FY27 Rs 358.7, end FY28 Rs 506.4, end FY29 Rs 697.1; FV CAGR 37.9% COMPOUNDER; price about 1.75 years ahead (FV reaches CMP about Jul-2028). Pillar FV CAGR 33.7% (B14), about 37.4% with A16 timing (VC F-R1).
- Equity bridge: Rs 57 per share approved (O7), anchored 31-Mar-2026 (deck May-2026 p.59, cash and bank Rs 506.99 Cr, less borrowings Rs 44.72 Cr and leases Rs 8.89 Cr, over basic shares); readings Rs 56.10 / 55.02 / 53.27 / 51.50 (30-Jun-2026). Tax shelter Rs 0 (NOT FOUND; claude.ai INFERENCE Rs 35 to 45 Cr).
- cash_multiplier_used 1.15; structural_or_growth growth-induced; ua_applied false; sector_cap_used 45.
- decision (B11): WATCHLIST, no position at Rs 566.65. Bands: A25 starter at or below Rs 415; 25% entry at or below Rs 328 (Rs 357 at 30x only); 30% entry at or below Rs 291.
- OR-16 sensitivity (deliberation A, base / bull / bear per share and base CAGR): 30x Rs 696 (7.1%) / 1,023 / 279; 19.5x Claude web Rs 472 (-5.9%) / 685 / 201; 16.9x Track 2 Rs 417 (-9.7%) / 601 / 182; 13.1x Track 1 Rs 336 (-16.0%) / 479 / 154; 12.1x draft Rs 315 (-17.8%) / 447 / 147. Cost of override at base: Rs 279 per share above the Track 2 pillar.

---

## 7. Gaps ledger

| # | Item | Needed by | Where to obtain |
|---|---|---|---|
| 1 | Live adjusted peer base (Affle, Braze, Klaviyo, Tanla or Route Mobile, Eagle Eye; clean or forward P/E, 4 to 6 peers) | B11 Step 1C; O5 support; zone re-cut | Claude web live peer table at /finalize |
| 2 | Net cash at the Q1 FY27 / H1 FY27 balance sheet date; borrowings at 30-Jun-2026 | B11 equity bridge | H1 FY27 results (BSE, about Nov-2026) |
| 3 | Tax loss shelter value | B11 equity bridge (O7) | FY27 AR tax note (Jul-2027); final RHP p.439 |
| 4 | FY26 top 10 customer concentration; >10% customer name | B04, B07 C1, B14 Chain 5 | FY27 AR Note 36(iii) (Jul-2027); IR query |
| 5 | SessionM purchase price allocation, cash acquired, assumed contract liabilities; reconciliation of USD 20 m / USD 9 m / Rs 16.91 Cr | B14 Chain 2; cash ruling O3 / O4 | H1 FY27 results notes (Nov-2026); Mastercard 8-K / 10-Q (PENDING LIVE VERIFICATION) |
| 6 | Final RHP / Prospectus (Nov-2025): Optum revenue, warrant schedule (pp.71-73), cloud commitment (p.62), cash tax (p.439), acquisition retention (pp.281-283) | B10, B11 D1 / D3, dossier V2 | capillarytech.com (HTTP 403 to script; operator push) |
| 7 | FY30 Optum warrant charge schedule; Optum renewal terms | ledger D1, D3 | final RHP; renewal disclosure by Mar-2029 |
| 8 | FII / DII split | B10 UA qualifier | full BSE Reg 31 category table |
| 9 | Promoter holding 3 year trend; Sep-2026 SHP | B01 E2; B14 Chain 6 | quarterly BSE SHP (Oct / Nov 2026 onward) |
| 10 | KPMG forensic outcome; insurance recovery quantum | falsifier 5; B14 Chain 7 | Reg 30 filing (overdue vs "later in August") |
| 11 | Migrated acquired revenue per quarter (organic definition) | proof gate half 1; ledger L3 | IR query; Q2 FY27 deck |
| 12 | Kognitiv revenue since purchase; customer count reconciliation (30+ brands vs 16 to 17 customers) | ledger L5 | IR query; Q2 FY27 call |
| 13 | 52 week low and lowest price since listing | zone reachability test | NSE / BSE price history (Claude web) |
| 14 | Invested capital FY29 to FY30; Year 3 net debt (B7) | B11 2D ROCE; A19 bridge | FY27 AR (Jul-2027); any Reg 30 acquisition |
| 15 | Year 5 (FY31) scenarios | B11 horizon (A18.0 met at Year 4) | operator, if wanted |
| 16 | Debt Capacity block; Market-Implied block (claude.ai) | B11 consumption clause | claude.ai runs |
| 17 | Rating rationale | B10 rating_wc_quote | none exists (company obtained no rating) |
| 18 | Contingent liabilities schedule; capital commitments; FX hedge notional | B02 FLAG-DISCLOSURE-GAP | management query; FY27 AR |
| 19 | FY26 transfer pricing study outcome | B02 FLAG-RPT | management query; FY27 AR |
| 20 | Chairperson committee count vs LODR Reg 26(1) | B08 | SEBI / MCA registry (live) |
| 21 | Pandora Holdings and Neytiri Holdings owners (44% of CTIPL) | B14 Chain 6; tracker row 8 | ACRA lookup (live) |
| 22 | Named SI / consulting partner programme | B14 Chain 1 | Claude web search |
| 23 | UnitedHealth vendor commentary; Adyen / Talon.One bundling; AI adoption surveys | B14 Chains 5, 8; tracker rows 3, 13 | 10-K / 10-Q; Gartner / Forrester (live) |
| 24 | BSE clarification reply of about 25-Sep-2026 | dossier Section 8 | BSE announcements |
| 25 | Founding capital, first product, first customer; pre IPO venture rounds | B14 3G | UDRHP "Our Journey" page is an image (p.275); final RHP |
| 26 | Margin at constant currency; cost split by country | B15 Section 3E | IR query |
| 27 | Sector Literacy log | B14 sizing (Medium gate) | operator |
| 28 | Portfolio holdings and capital base | B14 Section 9; Conviction Test (OR-23) | operator |
| 29 | Macro sheet refresh (Aug-2026 fill stale) | B11 r, terminal cap | frameworks macro sheet refresh |
| 30 | Screener P&L / BS / CF / Quarters export sheets (empty) | B01 | open Financials.xlsx, save, --push-again |

---

## 8. Deliberation confirmed inputs and overrides O1 to O11 (fttcp-deliberation.md Section A; dossier Section 6)

| # | Item | Draft (09-Oct) | Operator ruling (10-Oct-2026) | Reason as ferried |
|---|---|---|---|---|
| O1 | ROCE basis | company clean ROCE incl cash, TTM 5.2% | operating ROCE = (adj EBITDA - ESOP - D&A) / invested capital ex cash; standing rule, all names | "ROCE is measured on operations only." |
| O2 | Proof gate period | not defined | a quarter, annualised on period end invested capital; Q4 FY26 9.1%, Q1 FY27 13.6%; Q2 FY27 above 10% fires the ROCE half | ruled |
| O3 | Cash determination | R10 GROWTH-INDUCED pending | ACCEPTED; phase 1 cap lifted | contract liabilities, AR p.233 |
| O4 | Pillar 2 | 1.00x | 1.15x | "upfront billing, CROIC 23.2% TTM (deck p.26), CFO/adjusted EBITDA 140% in FY26" |
| O5 | Exit P/E | 12.1x additive / 8.9x RRM | 30x on one year forward operating EPS | "the peer cross-check, and Capillary is the only listed enterprise loyalty SaaS business in India" |
| O6 | Earnings basis | open | one year forward operating EPS; exit end FY29 on FY30 EPS | ruled |
| O7 | EPS adjustments | warrant not added back; tax 25% shelter in bridge; acquired amortisation not added back; capitalised development no adjustment | same; 8.24 Cr diluted; net cash about Rs 57 in bridge | ruled |
| O8 | Line B | A18 option slice | consolidated earnings at 30x; line B option value zero; calendar for tracking | single credit |
| O9 | Management grade | B with VB B-/C+ flagged | B; 3a +2x; bull at face value | ruled |
| O10 | Peer set | not built | Eagle Eye, Affle, RateGain, Braze, Klaviyo, Tanla or Route Mobile; exclude Newgen, Intellect; Zaggle reference | "They sell to banks and governments, on a licence and project model" |
| O11 | Scenarios | illustrative | bear / base / bull FY27 to FY30 approved (dossier 6.5) | "inclined to the bull case"; lean enters through weights and size |

FTTCP (deliberation B, D): window 3 / 6 / 12 months; Revenue FIRING / FIRING +2; Margin FIRING / FIRING +2; Cash IMPROVING / STARTING +1; ROCE STRUCTURALLY LOW / RECOVERING +1 (p about 0.65); composite 6 / 8, BUY candidate band, SMALL-MEDIUM sizing; Kernex cap no; TRIM no. Proof gate NOT FIRED. Cross family grade did not run. Signal gate: 14 tracker rows, 3 external (rows 3, 12, 13; dossier Section 5). Signed Part 1 (09-Oct-2026): archetype Outsourcing partner, system of record variant; NON-CONVERTER both lines; falsifiers 1 to 5 (dossier Section 4).

---

## 9. Role 1, Role 2 and Role 3 outputs

- Role 1 (B11): WATCHLIST; entry Rs 291.4 to 327.7; MoS Rs 229.4; 30x governing, pillar 16.8x / 13.1x; Hurdle STOP; expected CAGR 1.3%; one line: "Not buying CAPILLARY at Rs 566.65 ... at the four-pillar destination of 16.8x ... that is Rs 415 (-9.8% CAGR), and even at the operator-approved 30x it is Rs 697 (7.2%; Rs 640 and 4.1% weighted with the DCF). Key risk: the 30x exit itself ... plus acquired-book attrition. Cash quality: growth-induced."
- Role 2 (B14): verdict AVOID (Section 7: Gate 0 AVERAGE and U/D 0.24x); entry conjunction (price inside Rs 291 to 328 AND no thesis broken trigger fired); size NONE at CMP, ceiling Small starter; re-entry gates U/D 2x Rs 386.2, A25 starter Rs 415.2; Gate 0 leg may bind to FY28 data; eight second order chains (SI channel; SessionM bridge; retention before margin; shared ROCE; healthcare account; CTIPL supply; fraud and KPMG; AI price at renewal), each with [INFERENCE]; five PENDING LIVE VERIFICATION links; Entrepreneur Ledger 4 of 4 heads, Pillar 3 line supports +2x and no more. Thesis broken if: falsifiers 1 to 5, transition falsifier, time stop (both proof halves unfired by Q2 FY28 results, Nov-2027). Monitoring checklist 13 rows. B14 YAML position_size "Small" should read none (VC F-R2).
- Role 3 (B15): Rule H gate PASS; overall WEAKENED BUT ALIVE; growth triggers weakened; moat durability survives; management trust weakened; valuation safety weakened. Eleven contradictions the pipeline missed (organic definition; management FY30 revenue about Rs 1,323 Cr below the bear; 68% retention vs 80% ledger; Kognitiv lever; Kognitiv price basis; two margin mechanisms; goodwill test 4 to 10%; upfront billing reversal; SessionM net price tripled May to Aug; CTIPL warrant issuer; T1 vs FY27E). Three ways to lose: core engine about 11% (p 0.45), acquired books melt (p 0.35), multiple resets (p 0.40) or governance breaks (about 0.10). Shared catalyst: one year slip of every dated catalyst gives Rs 506 at end FY29 (-3.7% a year), two years Rs 359 (-14.1%). Zone returns 25 to 30% at 30x, 20.2 to 25.0% at 24x, 8.2 to 12.5% at 16.8x; at the pillar the 25% entry sits near Rs 212. Conviction Test (OR-23): 3x stress point 6 to 9% of portfolio; capital base NOT FOUND; questions handed to the operator. Success catalogue pending (0 of 4 names); failure catalogue match Tipco / Rappid / Ind Swift answered, not closed.

---

## 10. Operator decisions pending at /finalize

1. AVOID (B14) or WATCHLIST (B11): standing ruling needed (VC O-3; KISSHT precedent).
2. Verifier B rubric 70 or strict 40 (strict forces REWORK of stage 5).
3. Ratify or replace stage 11 ledger probabilities (FLAG-C2-PROBABILITIES; VC O-10).
4. Re-rule O5 or record that 4G yields (VC O-2); tie to the live peer table; relative route threshold 18.7x (VC F-V1).
5. UGLINESS verdict before any re-entry (B15 Section 3B).
6. Proof gate half 1 on like for like organic or NRR (B15).
7. Net cash placement in A24 (VC O-1): starter Rs 415 or about Rs 339.
8. Gate 0 data confidence window (B12c O4).
9. Conviction Test answers (OR-23).
10. Framework branch items (not this run): chunk 15 l.92, chunk 06 l.92, chunk 08 l.31 fixes (F-V1, F-V2, F-V3); Master l.296, l.1168, l.559 (O-4, O-5, O-6); record O1 as a standing rule in SKILL.md and CLAUDE.md (O-7); B11 YAML field for probability weighted EPS CAGR (O-8); stage 14 schema "none" value (F-R2).
