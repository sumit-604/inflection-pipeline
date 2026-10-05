# ARCHIVE DOSSIER (FTTCP HANDOFF): KISSHT, OnEMI Technology Solutions Ltd

Ticker KISSHT (NSE) / 544754 (BSE). Run folder runs/kissht-2026-09-19. Phase 3 finalize, written 04-Oct-2026 by Stage 13 (claude-opus-5-5).
Machine anchored. Self sufficient for a reader without the source PDFs. Units Rs Cr unless stated; statements are in Rs million in the source (10 million = 1 crore; B00 reporting_units).
**Priced under the Section 1B v3.11 unmerged draft (open item I5).**

## 0. Block and file index

| Ref | Path | Content |
|---|---|---|
| B00 | outputs/blocks/B00-inputs.yaml | Corpus inventory, spear override, LBF-1 to LBF-4, units, freshness PASS |
| B01 | outputs/blocks/B01-gate0.yaml; reports/01-gate0.md | Gate 0 scorecard |
| B02 | outputs/blocks/B02-notes.yaml | Notes forensic pass |
| B03 | outputs/blocks/B03-ardeep.yaml | AR deep read |
| B04 | outputs/blocks/B04-bizmodel.yaml | Business model |
| B05 | outputs/blocks/B05-concall.yaml | Concall analysis |
| B06 | outputs/blocks/B06-peers.yaml | Peer triangulation |
| B07 | outputs/blocks/B07-emoat.yaml | Emerging Moat scan |
| B08 | outputs/blocks/B08-promoter.yaml | Promoter review (status partial) |
| B09 | outputs/blocks/B09-tam.yaml | Market sizing (status partial) |
| B09b | outputs/blocks/B09b.yaml | Halt 1 dossier block |
| B10 | outputs/blocks/B10-assembly.yaml | Valuation input table incl. operator_signed_fttcp_pillars |
| B11 | outputs/blocks/B11-valuation.yaml; reports/11-valuation.md | Role 1 valuation |
| B12a / B12b / B12d | outputs/blocks/B12a.yaml, B12b.yaml, B12d.yaml | Verifiers A, B, D |
| B12c | outputs/blocks/B12c.yaml (phase 1 + phase 3 halves); B12c-valuation.yaml (phase 3 standalone) | Verifier C |
| B14 | outputs/blocks/B14-thesis.yaml; reports/14-thesis.md | Role 2 thesis |
| B15 | outputs/blocks/B15-devil.yaml; reports/15-devil.md | Role 3 devil's advocate |
| CONF | outputs/blocks/confidence.yaml | Confidence delta, phase 3 |
| LEDGER | outputs/expectation-ledger.md | Expectation ledger (A22-A24) |
| DELIB | outputs/final/fttcp-deliberation.md | Signed FTTCP deliberation, 04-Oct-2026 (authoritative) |
| GATES | outputs/final/fttcp-signoff-gates-2026-10-04.md | Sign-off gates I1 to I5 and recompute |
| DOSSIER | inputs/research/web-handover-dossier.md | Claude web handover, 03-Oct-2026 (live web facts, tier labelled) |
| MEMORY | companies/KISSHT.md | Company memory (weigh, never anchor) |

## 1. Transition data series

### 1a. Topline

| Year | Revenue (Rs Cr) | Growth YoY | Anchor |
|---|---|---|---|
| FY21 | 175.02 | n/a | screener-data (01-gate0 C1) |
| FY22 | NOT FOUND as a value in the record | +195% | screener-data (01-gate0 C3) |
| FY23 | NOT FOUND as a value in the record | +94% | screener-data (01-gate0 C3) |
| FY24 | 1,700.0 | +70% | screener-data (01-gate0 C3) |
| FY25 | 1,352.49 | -20.4% | screener-data (01-gate0 C3) |
| FY26 | 2,208.81 (screener) / 2,179.25 revenue from operations | +63.3% (screener) / +63.0% | screener-data (01-gate0 C1, C3); results FY26 consolidated p.6, 21,792.46 mn (B10 revenue_fy26_cr, revenue_growth_fy26_yoy_pct) |
| Q1 FY27 | 669.50 (quarter) | +44.8% YoY | results Q1 FY27 consolidated p.5, 6,695.00 mn (B10 revenue_q1fy27_cr, revenue_growth_q1fy27_yoy_pct) |
| 5-year revenue CAGR FY21-FY26 | 66.02% | | screener-data (01-gate0 C1) |

AUM (the lender's revenue analog): FY26 Rs 7,066 Cr, +73.0% (AR KPI p.5; B10 aum_fy26_cr); Q1 FY27 Rs 8,001 Cr, +13.2% QoQ, +61% YoY (Q1 FY27 press release 20260729-74639f09 p.2; B10 aum_q1fy27_cr; B05). Q2 FY27 Rs 9,317 Cr is a Claude web reading of the 03-Oct-2026 business update, not in the corpus (open item I4; GATES §7; B14 3B).

### 1b. Margin

Gross margin and EBITDA margin: NOT APPLICABLE for a lender (no COGS; finance cost is the core input cost; B04 irrelevant_ratios; B10 ebitda_note).

| Year | PAT (Rs Cr) | Net margin (PAT / revenue) | Cost to income | Anchor |
|---|---|---|---|---|
| FY21 | -58.45 | -33.4% [INFERENCE: -58.45 / 175.02] | NOT FOUND | screener-data (01-gate0 B1) |
| FY22 | 62.62 | NOT FOUND (revenue value not in record) | NOT FOUND | screener-data |
| FY23 | 27.67 | NOT FOUND (revenue value not in record) | NOT FOUND | screener-data |
| FY24 | 197.29 | 11.6% [INFERENCE: 197.29 / 1,700.0] | 45.54% | screener-data; AR p.10 KPI table (B01 FLAG-QUALITY) |
| FY25 | 160.62 | 11.9% [INFERENCE: 160.62 / 1,352.49] | 54.30% | screener-data; AR p.10 KPI table (01-gate0 M1) |
| FY26 | 281.45 | 12.91% on revenue from operations (B10); 12.7% on screener revenue [INFERENCE] | 56.64% | results FY26 p.6, 2,814.52 mn (B10 pat_fy26_cr, pat_margin_fy26_pct); AR p.10 |
| Q1 FY27 | 95.08 (quarter), +59.2% YoY | 14.21% | NOT FOUND | results Q1 FY27 p.5, 950.77 mn (B10) |

Lender margin proxies: return on average AUM ~5.05% FY26 and Q1 FY27 run rate (B04 unit_economics; B11 §2B); total income / avg AUM Rs 39.6 per Rs 100 FY26, Rs 35.9 Q1 FY27 annualised (B04 unit_economics; IP1 p.41). Core cost / avg AUM 14.6% FY25 to 12.2% FY26; marketing 2.9% to 4.6%; off book ECL 1.9% to 2.8% of AUM (DOSSIER §1C, [INFERENCE on FILED AR Note 29]; B14 3A). Standalone NIM / lending yield: NOT FOUND (B04 input_gaps; B10 unresolved).

### 1c. Cash conversion

| Year | CFO (Rs Cr) | CFO / EBITDA | CFO / PAT | Debtor days | WC % sales | Anchor |
|---|---|---|---|---|---|---|
| FY21 | 78.95 | n/a (lender) | n.m. (PAT negative) | 1.71 | NOT FOUND | screener-data (01-gate0 B1, M10) |
| FY22 | -15.63 | n/a | -0.25x [INFERENCE] | NOT FOUND | NOT FOUND | screener-data |
| FY23 | 48.36 (screener) / 111.48 (RHP restated) UNRESOLVED | n/a | 1.75x / 4.03x [INFERENCE] | NOT FOUND | NOT FOUND | screener-data; RHP p.271, 1,114.78 mn (B01 FLAG-DATA-CONFLICT; B12a source fidelity) |
| FY24 | -637.43 | n/a | -3.23x [INFERENCE] | NOT FOUND | NOT FOUND | screener-data = RHP restated -6,374.33 mn (01-gate0 Data Basis Note 2) |
| FY25 | -661.43 | n/a | -4.12x [INFERENCE] | NOT FOUND | NOT FOUND | screener-data = AR/RHP -6,614.26 mn |
| FY26 | -460.82 | n/a | -1.64x [INFERENCE] | 17.24 | NOT FOUND | screener-data = AR consolidated CF -4,608.21 mn; loans and advances line -15,621.28 mn (AR consolidated CF p.99) |
| Cumulative FY21-FY26 | -1,648.00 (screener basis, embeds the disputed FY23 value) | | -2.46x against PAT 671.20 | | | B01 B1 |
| Q1 FY27 | NOT FOUND (quarterly CFO not extracted) | | | | | B10 cfo_note |

FCF (CFO less capex) FY23 +102.37 (RHP matched CFO), FY24 -640.48, FY25 -669.17, FY26 -471.06; cumulative FY23-FY26 -1,678.33, ratio -2.52x (01-gate0 B2, B3). Debtor days are trade (fee) receivables, not the loan book (01-gate0 Data Basis Note 5). Standalone CFO/PAT above 1.2x (B03 strengths_top3).

Rating agency working capital commentary, VERBATIM (CRISIL Ratings on Si Creva Capital Services, 13-Feb-2026, Liquidity section; B10 rating_wc_quote, rating_wc_quote_source "p.64"; inputs/rating/CRISIL-SiCreva-RR-2026-02-13.txt lines 63-64):

"Liquidity Strong. As on December 31, 2025, the group had unencumbered cash, cash equivalent and liquid investment of Rs 290.4 crore. This is sufficient to cover one month debt repayments. Additionally, the group's average monthly collections stood at over Rs 500 crore over the last six months. Crisil Ratings also understands that Si Creva will not do any incremental disbursements unless it has adequate resources to service maturing debt obligations in the near term; this will remain a key monitorable."

Second CRISIL passage, VERBATIM (same file, line 59; retrieved at phase 1 synthesis, not extracted by a stage; quote only): "Gross non-performing assets (GNPA) stood at 2.95% as on September 30, 2025 and was at similar levels as on March 31, 2025 (2.92%). Nevertheless, write-offs and FLDG cost for trailing 12-months (as % of AUM) improved to 8.5% as on September 30, 2025 from 12.2% as on March 31, 2025. ... While these measures have shown early signs of improvement in the collection efficiency, sustained improvement in asset quality will need to be seen."

### 1d. ROCE and ROE

| Year | ROCE (EBIT / (TA - CL)) | ROE | Anchor |
|---|---|---|---|
| FY21 | NOT FOUND | -36.39% (screener PAT / closing net worth) | 01-gate0 A1, A3 |
| FY22 | NOT FOUND | 31.66% (screener computed) | 01-gate0 A3 |
| FY23 | 12.67% | 6.93% (company reported) | RHP restated BS p.267, CF p.271; RHP p.132/p.43 KPI (01-gate0 A1, A3) |
| FY24 | 33.12% | 28.78% | same |
| FY25 | 28.93% | 17.74% | AR consolidated BS p.98; AR p.10 KPI |
| FY26 | 32.93% | 23.97% | AR consolidated BS p.98, CF p.99; AR KPI p.5/p.10 (B10 roe_fy26_pct) |
| Q1 FY27 | NOT FOUND | 21.20% annualised on average equity; 16.9% on 30-Jun equity (operator ruling H) | B10 roe_q1fy27_ann_pct; DELIB override 2; B12b I15 |

Capital employed basis: total assets less current liabilities, consolidated, FY23-FY26 only. Finance cost is added back into EBIT, so the ROCE is structurally inflated for a lender and is directional only (01-gate0 Data Basis Note 3; B01 data_notes). Lender metrics: CRAR 25.77% / 25.18% / 25.28% FY24-FY26 and 40.2% Q1 FY27 before the raise (AR p.10; Q1 press release p.2); PCR 100.00% / 91.48% / 86.15% FY24-FY26 (AR p.10); D/E 0.97x / 1.50x / 1.78x FY24-FY26 (AR p.10, p.35); GNPA 2.89% FY25, 2.12% FY26, 2.25% Q1 FY27; NNPA 0.29% FY26 (B10; AR KPI p.5; press release p.2).

## 2. Catalyst inventory

From B05.triggers:

| # | Catalyst | Tier | Window | Conviction | Confirm signal | Kill signal |
|---|---|---|---|---|---|---|
| T-1 | AUM growth sustaining >40% FY27 guidance | documented (Q1 print) / claim (guidance) | near, FY27 | M-H | Continued 13%+ QoQ AUM prints through FY27 | QoQ AUM growth decelerating below ~8-9% without explanation |
| T-2 | Credit cost reduction 10-15% YoY FY27 | claim | FY27 | M | Sequential decline below 6.80% of average AUM | Any sequential credit cost rise without a clearly explained seasonal or one off cause |
| T-3 | GNPA direction vs guided <2.25% ceiling | documented | immediate, next quarter | L | Sequential GNPA decline back toward or below 2.12% in Q2 FY27 | Further sequential GNPA rise past 2.25%. SUPERSEDED for the thesis by the operator T3 trigger: Q2 FY27 vs Q2 FY26, Stage 2 > 4.11% or GNPA > 2.92% (DELIB override 1) |
| T-4 | Cost of borrowing decline from rating upgrade cycle | claim | FY27-28 | M | Confirmed second notch upgrade from CRISIL or India Ratings within FY27 | No upgrade by end FY27. Note: Acuité A- to A on 21-Aug-2026 (DOSSIER V3, AGENCY) |
| T-5 | LAP branch scale up and breakeven | claim | FY27 | L | Branch count toward ~178 FY27 end and Q3 FY27 breakeven | Continued sub-pace adds with no explanation, or pushed out breakeven. B12b: the "reframed breakeven" inconsistency is NOT SUPPORTED |
| T-6 | Rationale for Rs 832 Cr preferential raise | documented (pending) | immediate, next call | NOT YET RATEABLE | Clear numeric capital need given at next call | Continued silence on why Rs 832 Cr was needed at 40.2% CRAR |
| T-7 | Fee income diversification (insurance, MF distribution) | claim | long | L | Disclosed fee income contribution in a future quarter | Continued non-disclosure after several quarters |

From B07.catalysts_12m (B07 records tier and window; confirm and kill from B07 optionality_register where it names converting evidence):

| # | Catalyst | Tier | Window | Anchor | Confirm signal | Kill signal |
|---|---|---|---|---|---|---|
| E-1 | LAP branch pace recovery toward FY27 end target (3 vs ~27 per quarter needed) | documented | FY27 end | Concall_Jun_2026 p.20; B05 FLAG-LAP-PACE | Branch count and AUM mix matching the guided run rate | Not recorded in B07; see T-5 |
| E-2 | Rs 832 Cr preferential rationale disclosed (or continued silence) | documented (pending) | EGM 14-Oct-2026 / next concall | 20260917-acc1d37a; 20260918-4643d424 | Management explanation with a specific capital need number | Not recorded in B07; see T-6 |
| E-3 | Second rating notch upgrade (CRISIL / India Ratings) cutting cost of borrowing | claim | FY27-FY28 | Concall_Jun_2026 p.9-10; Concall_Aug_2026 p.11 | Rating agency press release / rationale | Not recorded in B07; see T-4 |
| E-4 | First quantified insurance / MF fee income disclosure | claim | 2-4 quarters | Concall_Aug_2026 p.5, 14 | Quarterly fee income % breakout in results or deck | Not recorded in B07; see T-7 |
| E-5 | Repeat customer AUM share trend in the next AR (73% to 49% FY25-26) | documented | 12 months | AR p.7; B04 FLAG-BUSINESS-MODEL | Not recorded in B07 | Not recorded in B07. DOSSIER supersession 19: the fall is driven by 2.6 Mn new customers at ~Rs 995 CAC |

Expectation ledger rows (LEDGER; probabilities PROVISIONAL, open item C2P): row 1 FY27 exit AUM Rs 11,600 Cr (+205.29 PAT, p 0.70, confirm-by 31-May-2027, interim Q2 >= Rs 9,055 Cr by 30-Nov-2026); row 2 FY28 AUM Rs 15,660 Cr (+102.48, p 0.60, 31-May-2028); row 3 bull FY28 PAT Rs 700 Cr (+77.00, p 0.20, 31-May-2027 / 31-May-2028); D1 return on AUM 5.05% to 4.571% (-65.09, p 0.70, fires if FY28 <= 4.60%); D2 partner exit, partner PAT -1/3 (-112.14, p 0.15, 31-May-2027); D3 asset quality reversal (NOT FOUND, uncredited, 30-Nov-2026); W1 Rs 832 Cr raise approval and rationale (0, 30-Nov-2026).

## 3. Flags with complete underlying findings

### FLAG-PROMOTER

Machine verdict B08: CAUTION (scorecard clean 4, caution 6, red 0); deal breakers: none (B08 deal_breakers). B08 status partial. Operator Part 2.6 ruling 03-Oct-2026: INTEGRITY concern, size ceiling Small, reopen on disclosure that the RBI inspection covered FY23-24 only; trust falsifier: inspection covered FY25 or later (MEMORY HALT 1 GATE; B14 3D). Carried active on the operator ruling; the B08 verdict alone sits below the CONCERN trigger.

Every B08 adverse finding:
1. Two live NFAC personal income tax disputes against Ranvir Singh (Chairman/CEO): AY2022-23 demand Rs 73.79 mn (order 18-Mar-2024, s.54F disallowance, s.68 addition); AY2023-24 demand Rs 175.97 mn plus a penalty SCN u/s 274/271AAC(1) (order 28-Mar-2025, s.54F, s.69). Combined ~Rs 249.76 mn (Rs 24.98 Cr), both under appeal. VERIFIED. RHP p.368-369.
2. Si Creva PMLA s.50(2)/50(3) summons from the ED Hyderabad Zonal Office dated 23-Mar-2023; no further ED communication as of 25-Apr-2026. VERIFIED. RHP p.39, p.374. Scope includes FLDG funds received from fintech service providers (DOSSIER §6; RHP p.32).
3. Si Creva previously classified "High Risk Financial Institution" by FIU-IND under PMLA (principal officer details); show cause notice; resolved and removed; dates NOT FOUND. VERIFIED (undated). RHP p.41.
4. RBI declined Si Creva's Dec-2021 application to co-brand a PPI with ICICI Bank (letter 10-Feb-2022), citing a net owned funds shortfall after an FY21 net loss. VERIFIED. RHP p.40-41.
5. Independent Director Atul Bheda, Audit Committee chair, resigned after under 5 months (8-Jul-2025 to 26-Nov-2025, "personal reasons"). VERIFIED. AR p.46, Corp Gov S.G.
6. Board carries zero non-executive nominee directors after Piyush Kharbanda's (Vertex Ventures SEA) resignation effective 17-Aug-2026, while institutions held 61.96% of the 31-Mar-2026 cap table. VERIFIED. BSE 20260817-93673f0b; AR p.51.
7. Parent corporate guarantee to Si Creva's lenders reached 228% of parent standalone net worth in FY26, rising four years, not named in the AR's "Balanced liability base" narrative. VERIFIED. Standalone Note 32 p.88; CARO Annexure A p.118.
8. CFO Amit Gupta's tenure under 11 months (20-Aug-2024 to 17-Jul-2025); founder Krishnan Vishwanathan retook the CFO seat. VERIFIED. RHP p.250-251.
9. COO Sonali Jindal and CTO Karan Mehta both resigned 29-Nov-2024, "other opportunities". VERIFIED. RHP p.250.
10. Non-audit fees Rs 50.00 lakh exceed the statutory audit fee Rs 49.00 lakh, consolidated; composition undisclosed. VERIFIED. AR Corp Gov Report S.9.
11. Public complaint forums allege aggressive recovery conduct; no regulatory penalty disclosed for these complaints. FORUM/SOCIAL, uncorroborated.
12. A single substack claims RBI caught Si Creva upgrading NPA accounts to standard. UNVERIFIED in B08. Later FILED: RHP risk factor 13 records "certain instances of upgradation of non-performing assets accounts to standard accounts", no penalty, period and amount undisclosed (DOSSIER supersession 15; B14 chain 7).

Transition evidence (B08, complete list):
- Rs 832 Cr preferential (board 17-Sep-2026) to 34 institutional allottees (Axis MF, HDFC MF, MIT, Ashoka WhiteOak, 360 One, Groww MF, Bandhan MF, Citigroup Global Markets, Unity SFB, others), 2,64,93,882 shares at Rs 314.11, zero promoter participation. BSE 20260917-acc1d37a, 20260918-4643d424.
- Three independent directors appointed Jun-Dec 2025: Sangeeta Tanwani, Alok Bansal, Yogesh Chadha. RHP p.245.
- Internal auditor upgraded from KKC & Associates to BDO India from FY27 (board 9-Jul-2026). Announcement 20260709-295aada2.

Pledge 0%, stable (B08 pledge_pct_latest, pledge_trend). Promoters 24.80% (BSE Jun-2026), about 21.4% after the preferential [INFERENCE, B14 §2].

### FLAG-CASH

Determination: GROWTH-INDUCED (operator ruling 7, DELIB §2, 04-Oct-2026). Phase 1 determination was INDETERMINATE (B13 phase 1 cash_determination). B10 FLAG-CASH and B11 FLAG-CASH carry GROWTH INDUCED; for a lender the multiplier applied is Pillar 2L 1.00x, not a cash multiplier (B11 pillar_detail).

Cited items:
- Cumulative CFO FY21-26 -1,648.00 Cr vs PAT +671.20 Cr, -2.46x (B01 FLAG-CASH; screener basis embeds the disputed FY23 value). Trend -661.43 (FY25) to -460.82 (FY26) (B01 block_b_trend).
- Ind AS 7 mechanic: FY26 loans and advances -15,621.28 mn (AR consolidated CF p.99; 01-gate0 Block B note).
- Rating agency quotes: reproduced verbatim in section 1c above.
- Capex commissioning timeline: not applicable to a lender. Capital deployment analogue: IPO fresh issue Rs 850 Cr; 75% (Rs 636.8 Cr) infused into Si Creva by 16-May-2026; CRISIL monitoring agency report confirms Rs 6,368.03 mn of Rs 6,375 mn utilised, no deviation (B05 promise_delivery; 20260729-4997d936 p.5, p.8). Preferential Rs 832.20 Cr: 75% (Rs 624.15 Cr) to Si Creva, 25% (Rs 208.05 Cr) general purpose (release 18-Sep-2026 p.2); EGM 14-Oct-2026.
- Receivables composition: standalone trade receivables (fee income) Rs 817.92 mn to Rs 983.83 mn (+20.3%), nil ECL, >6 month bucket Rs 14.83 mn (Standalone Note 7 p.76); consolidated trade receivables Rs 700.77 mn to Rs 1,042.97 mn (+48.8%), ECL Rs 8.18 mn to Rs 4.11 mn (Note 7 p.109) (B02 receivables_trend). The material asset quality signal is the loan book, not trade receivables.
- Loan book loss content: write offs FY26 Rs 4,725.95 mn (+10.7%), ~15.7% of average book; Stage 3 inflow +28.9% (B02 rank 2; Consolidated Note 41 pp.127-129, Note 26 p.119). DOSSIER supersession 2: two bases; P&L write off Rs 408.7 Cr down 6.7%; Stage 3 inflow flat; default inflow rate 24.7% to 15.8% of avg on book AUM.
- Partner book loss: group off book ECL Rs 154.7 Cr FY26 vs Rs 61.9 Cr FY25; parent FLDG cost Rs 100.9 Cr inside it; booked in other expenses (DOSSIER supersessions 3 and 4; AR Note 29). B02's "~Rs 2.5 bn, tripled" is a double count per the DOSSIER. FLDG outstanding at the parent Rs 737.80 mn (CARO Annexure A, AR p.118; B03).
- All in loss / avg AUM 11.6% FY25 to 10.97% FY26 (B10 FLAG-PROOF-GATE; DOSSIER §1C).
- Missing evidence: H1 FY27 FLDG cost in bps of avg off book AUM and booking line; numeric write off DPD trigger and vintage curves; asset side maturity ladder (B13 phase 1 cash_missing_evidence).
- Falsifying quarterly metric: Q2 FY27 Stage 2 > 4.11% or GNPA > 2.92% vs Q2 FY26 (DELIB override 1), by 30-Nov-2026.

### FLAG-GATE0

Grand 55/160; core 51/100; moat 4/60; blocks A 18, B 0, C 8, D 17, E 8; moats confirmed 1/12; moat class THIN; classification AVERAGE (B01). Depressor detail:
- Block B 0/20: B1 cumulative CFO/PAT -2.46x (0); B2 FCF positive years 1 of 4 (0); B3 cumulative FCF/PAT -2.52x (0); B4 WC days NOT FOUND (0). Driven by Ind AS 7 loan disbursal (01-gate0 Block B).
- Block C 8/20: C1 revenue CAGR 66.02% (5); C2 PAT CAGR N/M (0); C3 4 of 5 positive years (3); C4 N/M (0).
- Block A 18/20 is inflated by adding finance cost back into EBIT (B01 analyst_note).
- Moat tests: M1 0 on cost to income (45.54% to 56.64%); M3 0 on judgment; M8, M10, M11 0 (01-gate0 Block F).
- Deal breakers fired: Block B < 8 caps at GOOD; cumulative CFO/PAT < 0.50 caps at AVERAGE (binding) (B01 deal_breakers).
- Verifier C phase 1: moat as written 18 pts / 4 present / STRONG (floor 16 / 3 / MODERATE); grand 69 (floor 67); AVERAGE unchanged (B12c recomputed_gate0). Rulings requested: Gate 0 lender variant for Blocks A and F (G0V); deal breaker 6 for financials.

### FLAG-DISAGREEMENT

FY23 CFO 48.36 (screener) vs 111.48 (RHP p.271), unresolved; B12a source fidelity MINOR. See outputs/final/verifier-disagreement-log.md.

### Other active flags (carried)

B02/B03/B10 FLAG-CAPITAL-STRUCTURE; B02/B03/B10 FLAG-ASSET-QUALITY; B02 FLAG-OFF-BALANCE-SHEET; B03 FLAG-AUDITOR-FEES, FLAG-GOVERNANCE-STRUCTURE, FLAG-GUIDANCE-DIVERGENCE; B04 FLAG-DISCLOSURE-INCONSISTENCY (LAP ticket: AR Rs 30 lakh / 15 yr p.9; deck Rs 15 lakh / 10 yr IP1 p.11; CRISIL Rs 20 lakh / 10 yr), FLAG-BUSINESS-MODEL (repeat share 73% to 49%, AR p.7; cost to income 45.54% to 56.64%); B05 FLAG-SILENCE-GUARANTEE, FLAG-FRAMING-GNPA, FLAG-FLDG-QUANTUM, FLAG-CAPITAL-RAISE-SILENCE, FLAG-LAP-PACE; B06 FLAG-COST-OF-BORROWING-TAILWIND-CONTRADICTED (corrected to MIXED by B12b), FLAG-CAPITAL-RAISE-NO-PEER-PRECEDENT; B07 FLAG-EMOAT-EXECUTION-LEAD, FLAG-EMOAT-CONTRADICTION, FLAG-EMOAT-CAPITAL-SILENCE; B09 FLAG-TAM-SOURCE, FLAG-INTERPOLATION, FLAG-CAPACITY-CONDITIONAL; B10 FLAG-PROOF-GATE, FLAG-CREDENTIAL-GRADE, FLAG-EM-SCORE, FLAG-COST-OF-BORROWING, FLAG-CAPITAL-RAISE; B11 FLAG-I5, FLAG-ENTRY-OVERRIDE-VS-MECHANICAL, FLAG-FV-LABEL-MARGIN, FLAG-HURDLE-TRACK1, FLAG-BOOK-BASE-CONFLICT, FLAG-PILLAR2L-READING, FLAG-DECOMP-PROBABILITIES-PROVISIONAL, FLAG-UGLINESS-TEXT, FLAG-MACRO-STALE, FLAG-CONSUMED-BLOCKS-MISSING.

## 4. Credibility grade

B05 credibility_grade: **C**, at the C/B boundary. Basis (B05 credibility_basis): two clean quarters mostly ahead of guidance would support B, but the GNPA / write off "technicality" framing is not supported by B02/B03, and the 228% guarantee and the Rs 832 Cr rationale are absent from the call record. Moves to B on a clean quarter with GNPA falling and proactive disclosure; toward D if the "technicality" framing repeats (B05 analyst_note). Verifier B concurs C on a different basis: drop the LAP breakeven inconsistency; add guidance drift, the CoB KPI method change in an adverse quarter, contradictory FLDG answers, and the peer unsupported "Q1 seasonal" reading (B12b credibility_grade_concur). DOSSIER §5: delivery on numbers about B, disclosure about D. DOSSIER supersession 9: the "technicality" quote answered the FY23 to FY25 GNPA rise, not the Q1 FY27 rise.

promise_delivery_score: delivered 6, partial 3, missed 1 (B05). Spot check by Verifier B: 6 checked, 5 confirmed, 1 wrong (B12b).
repeated_evasions: [] in B05. Verifier B: the FLDG economics were left unquantified on both calls with contradictory Q1 answers, which B05 did not record as an evasion (B12b I1, MAJOR).

Guidance versus delivery (B05 promise_delivery rows, two calls: Q4 FY26 29-May-2026, Concall_Jun_2026_Transcript; Q1 FY27 30-Jul-2026, Concall_Aug_2026_Transcript):

| Promised in | Promise | Outcome | Delivery anchor |
|---|---|---|---|
| Q4 FY26 call p.8 | AUM growth >40% FY27 | delivered so far | Q1 FY27: +61% YoY, +13% QoQ to Rs 8,001 Cr (press release; Concall_Aug_2026 p.3, p.7). DOSSIER: +32% in H1 to Rs 9,317 Cr (Claude web, I4) |
| Q4 FY26 call p.9 | Credit cost -10 to -15% YoY FY27 | delivered so far | 6.80% Q1 FY27 vs 8.85% Q1 FY26 (Concall_Aug_2026 p.4, p.9). Headline is on book impairment over total AUM (DOSSIER supersession 6) |
| Q4 FY26 call p.9 | GNPA below 2.25% FY27 | partial | Exactly 2.25% Q1 FY27, up from 2.12% (Concall_Aug_2026 p.4) |
| Q4 FY26 call p.9 | RoAUM 4.5-5%, RoAE 19-21% FY27 | delivered so far | RoAUM 5.05%, RoAE 21.20% Q1 FY27; RoAE on part period IPO equity (B12b I15); 16.9% on 30-Jun equity (DELIB) |
| Q4 FY26 call | Further CoB cut on second rating upgrade | partial | Incremental borrowing ~150 bps below FY26 average in Q1 FY27; no second CRISIL/Ind-Ra upgrade yet |
| Q4 FY26 call p.20 | 80+ more LAP branches (98 to 178+) by FY27 end | missed pace | 3 added in Q1 FY27 (98 to 101; IP1 p.11) |
| Q4 FY26 call p.15 | LAP breakeven "a year or two away" | partial / inconsistent per B05; NOT SUPPORTED per B12b | Q4 phrase referred to steady state ROA; Q1 guides breakeven ~Q3 FY27 (Q1 p.18) |
| Q4 FY26 call | 450 paused pin codes reviewed on data | delivered | 180 of 450 reopened by Q1 FY27 |
| RHP 25-Apr-2026 | Objects: 75% to Si Creva, 25% GCP | delivered | Rs 6,368.03 mn of Rs 6,375 mn utilised, no deviation (20260729-4997d936 p.5, p.8) |
| Q1 FY27 call | FLDG number "offline" | not delivered | DOSSIER §5 |

Guidance drift (B12b I4): credit cost 10-15% restated to "15%", RoE 19-21% to "20% plus", AUM FY27 to "next 12 months", historical growth floor 50% to 60% (Q1 [page 5], [page 7], [page 11], [page 14], [page 16]).

## 5. Scorecards and market sizing

**Gate 0** (B01): grand 55/160; core 51/100; moat 4/60; A 18, B 0, C 8, D 17, E 8; moats confirmed 1/12; classification AVERAGE; deal breakers: Block B < 8 caps at GOOD (superseded); cumulative CFO/PAT < 0.50 caps at AVERAGE (binding). Verifier C as written: moat 18 (floor 16), grand 69 (floor 67), AVERAGE (B12c).

**Emerging Moat** (B07): em_score 18.5; em_classification MODEST (12-24 band; below the EM >= 25 UA threshold). Verifier C recompute 15.6 to 16.6, MODEST (B12c). Active categories: A3 process innovation (underwriting AUC trend) Moderate, documented (B12c: deck/concall only; DOSSIER supersession 7: the AUC chart is the fraud model); C1 customer ecosystem / cross sell Moderate, documented/claim, counterweighted by repeat share fall; D1 proprietary underwriting data asset Strong, documented, execution lead per I2 = 0; D2 digital platform Moderate, documented; G1 war chest Moderate, documented, counterweighted; H2 strategic partnerships Moderate, documented (B12c recompute H2 0). evidence_mix: documented 11, claim 8, inference 4. combined_assessment AVERAGE. capex_embedded_growth_pct 57.8 (B12c recompute 21.9 / 29.2).

**Accounting quality** (B02): 5/10. Top findings:

| Rank | Finding | Note ref | Rating |
|---|---|---|---|
| 1 | Parent guarantee to Si Creva's lenders 70.3% of parent net worth FY23 to 228.0% FY26; crossed 100% in FY24 | Standalone Note 32 p.88, Note 31 p.88; RHP Note 36 p.325/333, Note 47 p.332-333 | RED FLAG |
| 2 | Stage 3 2.12% sustained by ~15.7% write off rate (+10.7%) while Stage 3 inflow +28.9%; 150 DPD trigger absent from AR and RHP | Consolidated Note 41 pp.127-129, Note 26 p.119; RHP p.278/350 | RED FLAG (narrowed by DOSSIER supersession 2) |
| 3 | FLDG / off balance sheet cost more than tripled (~Rs 2.5 bn vs < Rs 0.8 bn) | Standalone Note 25 p.84; Consolidated Note 29 p.119-120 | RED FLAG (DOSSIER supersession 3: double count; off book ECL Rs 154.7 Cr) |
| 4 | 99.8% of the NCD book and most term loans rest on the parent guarantee | Consolidated Note 18 p.116-117, Note 19 p.117-118, Note 36 p.123-124 | RED FLAG |
| 5 | Guarantee growth (74-80% YoY) and the ECL build-release-rebuild cycle do not move together | Consolidated Note 26 p.119; RHP p.318; RHP Note 36 | WATCH |
| 6 | ECL cycle FY23 +443.57, FY24 +2,603.50, FY25 (1,652.04), FY26 +495.27 Rs mn, unexplained | Consolidated Note 26 p.119; RHP p.318 | WATCH |
| 7 | Management overlay ECL Rs 1,359.53 mn = 59% of model ECL, flat while base ECL +27% | Consolidated Note 41 p.127 | WATCH |
| 8 | Parent 43.9% of net assets earns 49.3% of profit; guarantee fee ~2.3% of average guarantee | Consolidated Note 47 p.131; Standalone Note 34 pp.88-90 | WATCH |
| 9 | Software amortisation life 5 to 10 years, unquantified | Standalone Note 2.15 p.72; Consolidated Note 2.16 p.105; RHP p.278/350 | WATCH |
| 10 | KMP pay Rs 10 mn standalone vs Rs 25 mn consolidated each for CEO and CFO | Standalone Note 34C p.89; Consolidated Note 38(b) p.124-125 | WATCH |
| 11 | Standalone revenue 74.7% in three unnamed counterparties vs group "no customer >= 10%" | Standalone Note 40 p.93; Consolidated Note 44 p.126; RHP p.333 | WATCH |
| 12 | New LAP line disclosed at group level, no size or quality disclosure | Consolidated Note 1 p.101 | WATCH |
| 13 | Only the liability side of the maturity ladder is disclosed | Consolidated Note 41B pp.128-129 | WATCH |
| 14 | Undrawn bank lines ~31x (Rs 61.72 mn to Rs 1,910.65 mn) | Consolidated Note 41B p.128 | WATCH |
| 15 | Interest rate risk small; 13.7% of borrowings floating; 0.5% move = Rs 16.39 mn | Consolidated Note 41D p.129 | CLEAN |

Guarantee fee gap: Rs 39.41 Cr in the related party note (AR Note 34 p.89) vs Rs 21.72 Cr in standalone other income (AR p.84); NOT EXPLAINED (GATES §4; DELIB §6 IR question 2).

**Market** (B09, status partial): tam_cr conservative 26,00,000 / realistic 27,00,000; sam_cr 60,000 (FY25, 1Lattice, issuer commissioned); sam_pct_of_tam 2.3; som_3yr_cr 33,620; som_5yr_cr 63,747; som_implied_revenue_cagr yr3 61.4%, yr5 51.4%; current_sam_share_pct 6.2; revenue_headroom_x 23.4; tam_growth_pct 20; runway_class MASSIVE; mgmt_claim_cr 4,10,000 (FY30P SAM); mgmt_claim_ratio 0.061 ("conservative"; SAM scoped claim against a TAM denominator). Personal loan leg corroborated within 2-13% by four aggregators; LAP and SAM funnel 1Lattice only (B09 FLAG-TAM-SOURCE); SAM interim years interpolated at 46.9% CAGR (FLAG-INTERPOLATION).

**Peer triangulation** (B06; corrections from B12b, B12d):
- Verified: none.
- Partially verified: "divergence beneath a calm surface" (SBICARD, UGROCAP); 150 DPD write off within a plausible industry range (POONAWALLA 180/365/730 schedule, Jan-2026).
- Contradicted: (1) FCNR(B) cost of borrowing tailwind, SBICARD-Concall_Jul_2026 p.5, POONAWALLA-Concall_Jul_2026 p.16. B12b: OVERSTATED; UGRO CoB fell 7 quarters, incremental 9.8% (UGROCAP-Concall_Aug_2026 p.7); SBICARD mixed (p.5 vs p.7); POONAWALLA cause stated by an analyst; carried MIXED. (2) Rs 832 Cr raise at 40.2% CRAR as a sector pattern: POONAWALLA QIP at 16.83% CRAR (May-2026 p.14, p.19); UGRO ~18% CRAR (Nov-2025 p.9). B12b: POONAWALLA gave no numeric rationale either; direction holds.
- Added by Verifier B (P1): same quarter peers improved asset quality (SBICARD GNPA -36 bps, Stage 2 -10 bps, Jul-2026 p.5-6; POONAWALLA GNPA 1.44% to 1.37%, Jul-2026 p.8, p.15). DOSSIER supersession 8: Kissht's own Q1 FY26 pattern supports "seasonal"; peers do not.
- Unverifiable: FLDG cost trend and accounting mirroring a sector trend (no comparable peer structure); peers naming Kissht, Bajaj or Chola as share gainers or losers.
- peer_mentions_of_company: none. net_narrative_effect: complicates.

## 6. Valuation pillar detail (Stage 11 ran; priced under unmerged v3.11, I5)

**Approved base (DELIB §5; B10 operator_signed_fttcp_pillars):** SOTP primary (A27.2), FORWARD, valuation date 31-Mar-2027; own book on Mar-27 book; partner half on FY28 PAT; same basis at exit (A27.3). PAT FY27 / FY28 base 441 / 623 (return on avg AUM 4.75% / 4.6%; AUM 11,600 / 15,660), bear 400 / 500, bull 470 / 700. Split 46 / 54 by AUM share. Shares 20.8416 Cr fully diluted post raise (paid-up 16,84,83,022, AR Note 48 p.131; options in force 13,438,960, RHP p.105; preferential 2,64,93,882). Market value post raise = CMP x 18.1922 Cr + Rs 832.20 Cr = Rs 7,555.1 Cr (Rs 362.50 per share) at CMP Rs 369.55 (Trendlyne 01-Oct-2026).

**destination_pe_track1_rrm** (B11 destination_pe.track1_rrm): low 17.0x, mid 18.62x, high 20.0x; r 15.5% = 14 base + 0.5 durability (Unproven, listed ~5 months) + 0.5 governance (operator override 4) + 0.5 complexity (A13); RRM = 1 + (13.5 - 15.5) x 0.12 = 0.76; 24.5 x 0.76 = 18.62x.
**destination_pe_track2_additive** (B11 destination_pe.track2_additive): low 21.0x, mid 22.67x, high 22.67x (cap binds).
Divergence 17.9% > 15%: Track 1 governs the entry (chunk 06, OR-1).

Partner half pillar build (B11 §1B.1):
| Row | Value | Basis |
|---|---|---|
| A. RoE base | 24.5x | Parent RoE ex investment in Si Creva: 84.4% FY26 actual, ~34% FY27 projected (operator). Formula gives 24.3x at 34% (F5); approved 24.5x implies 34.7%. Basis of ~34% NOT FOUND (GATES §2; F3). At 16.7% (reported standalone equity) Pillar 1 would be 15.85x (GATES §2) |
| B. Pillar 2L | 1.00x Sound | Operator ruled on YoY GNPA (+13 bps vs +75 bps). Second reading 0.80x Stressed (sequential GNPA 2.12% to 2.25%): Track 2 19.6x, Track 1 14.9x, today Rs 353.9 |
| C. Quality adjusted | 24.5x | |
| D. Pillar 3 | +0x | A16 gate; EM 18.5 < 25; grade C |
| E. Strategic premium | +0x | No scarce asset |
| F / F2. Raw, UA | 24.5x; UA not qualified | Listed < 12 months; EM < 25; FII/DII NOT FOUND |
| G. Cap | 22.67x | Operator set blend 1/3 x 18x + 2/3 x 25x (override 3); no Section 1B row (F1). 25x matches the Master rows "Logistics (asset-light)" and "Consulting / Engineering services" (GATES §2) |
| H. Track 2 | 22.67x | min(24.5, 22.67) |
| Track 1 | 18.62x | 24.5 x 0.76 |
| Slice PAT FY28 | Rs 336.42 Cr | 54% x 623 |
| Slice value | Rs 6,264.1 / 6,944.8 / 7,625.5 Cr | Track 1 / midpoint / Track 2 |

Partner cap revisit (override 3): FLDG charge above ~40% of partner revenue (FY26 23.4% of revenue from outside Si Creva, 27.9% of outside sourcing and servicing fees; GATES §2, AR p.84-85, p.89), or top two partner share above 90% through FY27 (95% of parent DLG pools at 31-Aug-2026, DOSSIER V2; 68.2% on RHP off book AUM Dec-25, B15). Measure undefined (CAPM).

Own book (B11 §1B.2): Mar-27 book Rs 2,695.8 Cr = FY26 1,231.98 (AR AOC-1 p.57) + IPO 636.8 (monitoring agency p.5) + 75% of raise 624.15 (release 18-Sep-2026 p.2) + 46% of FY27 PAT 202.86. P/B 0.8 / 1.0 / 1.2x (operator: "RoE ~10% post-raise, recovering toward FY26's 14% as capital is lent out"). Slice value Rs 2,156.6 / 2,695.8 / 3,235.0 Cr. Own book RoE path FY28 10.1%, FY29 11.8%, FY30 12.9%, FY31 13.5%; theoretical P/B 0.65x to 0.87x at 15.5% (B11). Verifier C F2 earned band 0.65x / 0.72x.

Whole company cross check (B11 §1B.3): Pillar 1 RoE ~17% = 16.0x; 2L 1.00x; P3 +0; cap 18x; Track 2 16.0x; Track 1 12.16x.

Cash line: Rs 208.05 Cr (Rs 9.98/share), general purpose 25% of the raise, at face, constant (A27.1); FLDG deposits excluded. Treasury income NOT FOUND, not stripped. F4: ~Rs 171.2 Cr IPO proceeds at the parent unclassified (+Rs 8.2/share if surplus). D15-5: possible double count with FLDG collateral.

**hurdle_ratio** (B11): base 2.30, prob_weighted 2.04, bull 2.54 (bull_used false), Track 1 prob-weighted 1.79, threshold 1.953 (Tier A), time-exact 2.177 over 3.487 years. Basis FORWARD; current PE 19.70x = (369.55 - 9.98) / A21 EPS 18.25 (F11: forward form 12.03x); prob-weighted EPS CAGR 39.9%; destination PE mid 14.67x. **hurdle_verdict PASS** (feasibility only; caps nothing). F1: ~1.84 at the 18x row (CONDITIONAL).

**fair_values** (B11):
| Track | Date | Bear | Base | Bull |
|---|---|---|---|---|
| Track 1 | 31-Mar-2027 | 354.0 | 414.0 | 451.7 |
| Midpoint | 31-Mar-2027 | 405.9 | 472.5 | 514.4 |
| Track 2 | 31-Mar-2027 | 457.8 | 531.1 | 577.1 |
| Track 1 | 31-Mar-2030 | 519.5 | 737.7 | 899.5 |
| Midpoint | 31-Mar-2030 | 593.7 | 837.5 | 1,018.0 |
| Track 2 | 31-Mar-2030 | 668.0 | 937.3 | 1,136.5 |

FV path Track 1 base: 414.0 (31-Mar-2027), 517.3 (2028), 623.2 (2029), 737.7 (2030). **FV CAGR 21.2%, COMPOUNDER** (B11 fv_cagr, return_source_label). Sensitivity: midpoint 21.0%, Track 2 20.9%, Reading B 17.9% (HYBRID), prob-weighted 20.5%, bear 13.6%, bull 25.8%. Decomposition 19.3: cash line 2.4% of FV today (1.4% at exit); no option value; partner half 72.6% compounding 24.6%/yr; own book 25.0% at 12.3%/yr; no re-rating lever credited.

Projection extension (B11 projection_extension): PAT base FY27-FY32 441 / 623 / 814.2 / 1,003.9 / 1,204.7 / 1,445.6; bear 400 / 500 / 580.3 / 672.7 / 778.9 / 900.7; bull 470 / 700 / 949.8 / 1,218.6 / 1,523.3 / 1,904.1; AUM base 11,600 / 15,660 / 19,966.5 / 23,959.8 / 28,751.8 / 34,502.1; return on avg AUM held 4.571% (Reading A); fade to 20% industry anchor by FY30 (A14 MODEST).

**entry_range** (B11): mechanical Rs 301.5 (30% CAGR) to Rs 344.2 (chunk 06, Track 1 Year 3 operating FV Rs 727.76 / 1.25^3.487 + Rs 9.98). Operator override ~Rs 350 BINDING (DELIB override 5; reasoning: SOTP base 2.88x Mar-27 book needs 12.4% perpetual growth at 17% RoE and 14% CoE, 14.7% at 15.5%). Deliberation today value method Rs 371.4 (A27.1 consistent Rs 372.4); midpoint chunk 06 Rs 390.1; Reading B Rs 317.2. Override sits 1.7% above mechanical. B14 entry_range {301.5, 350}.
**mos_price**: Rs 243.9 (reference only; FAST-GROWTH carve-out).
**decision**: B11 "WATCHLIST"; B14 "AVOID" (Section 7, Gate 0 AVERAGE); B12c F12 concurs AVOID. Carried: AVOID.
**cash_multiplier_used**: 1.00 (Pillar 2L asset quality, Sound; lender, not a cash multiplier).
**structural_or_growth**: GROWTH INDUCED.
**ua_applied**: false.
**sector_cap_used**: 22.67x partner slice (operator blend); 18x whole company (Banks / NBFCs / MFIs).
**converter_classification**: NON-CONVERTER (A17 test a fails).
Upside / downside: Year 3 n.m. (all states above CMP); valuation date headline 0.80x (base Track 1 Rs 414.0 vs partner exit Rs 313.8); against the bear headline 2.9x. F6 and F9 contest the 0.80x use.
Stress (B11 §4F, today value): bear low Rs 354.0; partner exit low Rs 313.8; bear base Rs 405.9; partner exit base Rs 361.5; compound bear plus partner exit Rs 273.5; 2L 0.80x Rs 353.9. B15: a 50% partner cut gives Rs 263.7 at 18.62x and Rs 237.7 at 15.4x.
Recognition gap (B11): OPEN on forward basis (current forward PE 12.03x vs SOTP implied 13.5x / 15.5x / 17.4x; market implied partner PE 15.4x / 13.8x / 12.2x at own 0.8x / 1.0x / 1.2x); counter reading CLOSED on book (CMP 2.25x Mar-27 BVPS 164.3 vs theoretical 1.10x to 1.21x).
Price decomposition (B11 price_decomposition; denominator Rs 7,555.1 Cr = Rs 362.50 per diluted share): T1 Rs 6,061.4 Cr / Rs 290.83 / 80.2%; T2 Rs 1,510.8 Cr / Rs 72.49 / 20.0%; T3 Rs 162.9 Cr / Rs 7.82 / 2.2%; residual -Rs 180.1 Cr / -Rs 8.64 / -2.4%. Midpoint cross check T1 92.4%, T2 22.3%, T3 2.4%, residual -17.2%. At CMP x diluted shares (Rs 7,702.0 Cr) Track 1 residual -0.4%. Probabilities PROVISIONAL (C2P).
Size state (B11 size_state): fast_growth true (Q1 FY27 revenue +44.8%, PAT +59.2%); A25 STARTER (Small, 2-3%); ceiling Small (Part 2.6); dispersion 51.5% (Medium cap); add trigger none inside the ceiling; trim 25% per decayed ledger row, 50% if residual > 40% after a decay.

## 7. Gaps ledger

| Item | Needed by | Where to obtain |
|---|---|---|
| Q2 FY27 business update (03-Oct-2026), I4 | Ledger row 1 interim; T1 watch; DBB | BSE announcements (API Access Denied 04-Oct-2026); operator drops the PDF into inputs/announcements/ |
| Section 1B v3.11 merge, I5 | Stage 11 sign-off; downstream presentation | Operator framework PR to main |
| Disbursement by book, on vs off, FY25 / FY26 / Q1 FY27, DBB | 46/54 split; transfer pricing; entry override revisit | IR reply (DELIB §6 IR question 1) |
| Guarantee fee gap Rs 39.41 Cr vs Rs 21.72 Cr | Transfer pricing | IR reply (DELIB §6 IR question 2) |
| Ledger probabilities ratification, C2P | Price decomposition finality | Operator ruling |
| Gate 0 lender variant, G0V; deal breaker 6 for financials | Section 7 decision; Gate 0 | Operator ruling |
| Partner cap revisit share measure, CAPM | Partner slice cap | Operator ruling |
| ~34% partner RoE basis (F3); Rs 171 Cr IPO remainder classification (F4) | Pillar 1; A27.1 cash line | Operator ruling; AR Note 47 p.131, Note 6 p.75, AR p.98 |
| BOOK, Mar-27 consolidated book | Cross checks | Closable on AR p.57 (Si Creva Rs 1,231.98 Cr) and AR p.98 (consolidated Rs 1,342.78 Cr), pending operator confirmation (F8) |
| Structural optic name, UGLY / D15-1 | Transition posture | Operator ruling |
| Pillar 2L partner slice on its own rows, D15-3 | Partner Track 1 | Operator ruling; CRISIL / Acuité FLDG cost split |
| H1 FY27 FLDG cost in bps of avg off book AUM and booking line | Proof gate; FLAG-CASH | Q2 FY27 results; IR reply (DOSSIER §10 Q2); next CRISIL or Acuité rationale |
| RBI inspection years | Part 2.6 ceiling; T3; Pillar 2L | IR reply (DOSSIER §10 Q1) |
| Numeric write off DPD trigger; static pool / vintage curves | LBF-1; FLAG-CASH | IR reply; Si Creva AR; CRISIL detailed review |
| Asset side maturity ladder | Liquidity | Si Creva ALM return (not public); IR |
| Treasury income on IPO and raise cash | A21 run rate; current PE | Q2 FY27 other income line |
| FY23 CFO conflict (48.36 vs 111.48) | FLAG-DISAGREEMENT | RHP p.271 restated (audited); screener vendor check |
| FY21-FY22 ROCE; FY21-FY22 capex; FY21 WC days | Gate 0 | Pre-FY23 audited statements (not in corpus) |
| FII/DII split of public holding | UA qualifier; E1 | BSE detailed shareholding pattern |
| Promoter holding trend | E2 | Future quarterly shareholding filings |
| SBICARD screening sheet | M5 peer cap | Screener Data_Sheet; collector defect |
| Standalone NIM / lending yield | Margin bridge levers (F18) | IR; CRISIL detailed review |
| LAP ticket size and tenure reconciled; LAP asset quality | B04 flag; I16 | Management |
| Q1 FY27 CFO | Cash series | Q1 FY27 results cash flow annexure |
| Debt Capacity, FTTCP Part B (B1-B8), Market-Implied blocks | Stage 11 consumption | claude.ai (Market-Implied PENDING) |
| Live peer table, Step 1C | Peer multiple cross check | claude.ai live peer table |
| Macro sheet refresh (August 2026, stale) | RRM neutral check | macro-sheet.md refresh |
| Tax rate and credit cost base | Ledger D3 credit | Results; AR |
| MCA / RoC status of nine promoter group entities; SEBI SCORES | B08 (partial) | Paid MCA lookup; SEBI SCORES |
| Primary RBI FSR PDF; CRIF High Mark / DLAI-CRIF PDFs; independent LAP market size; KreditBee / Navi / Fibe / Moneyview AUM re-verification | B09 (partial) | RBI site; CRIF site; rating rationales |
| Final prospectus (05/06-May-2026); Si Creva AR and audit opinion; Piramal Nov-2025 decks | DOSSIER §8 | BSE; sicrevacapital.com; Piramal IR |
| 5-year FV (F13) | Role 2 template | Stage 11 rerun with FY33 PAT |

## 8. Deliberation record, operator overrides, Role 2 and Role 3 outputs

**FTTCP verdict (DELIB §1, operator's words):** "Composite +2 of 8. DEEP WATCH leaning AVOID. Posture VALUE-TRAP RISK." T1 AUM FIRING +2; T2 NIM DECLINING -1; T3 asset quality STARTING +1 (override 1); T4 RoA/RoE STAGNANT 0; proof gate NOT FIRED; Pillar 2L 1.00x; Hurdle Tier A 25%; UA not qualified; cash GROWTH INDUCED; RoA/RoE backward SUSTAINED (DELIB §2 rulings 1-18). Cross family grade did not run (no Gemini key; DELIB §4).

**Operator overrides (DELIB §3):**
1. T3 STARTING (+1) over draft STAGNANT; trigger Q2 FY27 vs Q2 FY26: STARTING if Stage 2 <= 3.3% and GNPA < 2.92%; DECLINING if Stage 2 > 4.11% or GNPA > 2.92%. Baselines operator supplied. At STAGNANT the composite is +1, same band.
2. SOTP primary, FORWARD, valuation date 31-Mar-2027; Q1 RoE 21.2% is an average equity artifact, 16.9% on 30-Jun equity; partner slice RoE measured ex the investment in Si Creva.
3. Partner slice cap 22.7x blend (not a framework output); revisit triggers as in section 6.
4. Governance add-on +0.5 everywhere: r 15.5%, RRM 0.76.
5. Entry zone ~Rs 350 held by override; revisit on DBB and the A19 FV CAGR.
6. Share count fully diluted 18.19 Cr pre raise, 20.84 Cr post raise.

**Signed mental model (MEMORY; DOSSIER §1):** FROM ultra-short checkout / pay later credit with a synthetic partner guarantee (FY23-24); TO Reading 1 well run high yield lender, RoE ~17-18% (R2), Reading 2 data edge, RoE 20%+ (R3; a two rung leap). Proof gate: all in loss / avg AUM < 10.5% for H2 FY27, off book loss rate not rising. Transition falsifier: all in loss > 11.6%; off book loss rate rising two half-years; revenue margin minus all in loss narrowing two quarters. Business falsifier: a top two partner exits or cuts pools > 1/3 with no replacement; RBI cuts the 5% DLG cap or changes recognition. Trust falsifier: RBI inspection covered FY25 or later. Ugliness: "STRUCTURAL-FEATURE (negative CFO and cost-to-income optics are artifacts)"; structural optic not named.

**Role 1 (Stage 11):** as section 6. One line thesis (B11): "Buying KISSHT at or below ~Rs 350 because forward EPS grows from Rs 29.9 (FY28) to Rs 57.8 (FY31) as AUM compounds at a held 4.57% return, valued as an SOTP at Track 1 (own book 0.8x P/B; partner half 18.62x) = Rs 737.7 end-FY30 = 23.8% CAGR from Rs 350; FV CAGR 21.2% COMPOUNDER; key risk two-partner concentration and the 228% parent guarantee behind write-off-assisted GNPA; cash quality growth-induced."

**Role 2 (Stage 14, B14):** verdict AVOID; entry_range 301.5 to 350; position_size field "Small" (F10: should read "None (AVOID); ceiling Small if re-opened"); card "SIZE: none now". Rule H readiness confirmed: forward basis, return on AUM bridge, seven chains each with [INFERENCE], Entrepreneur Ledger filled (4 of 5 rows filed evidence; Pillar 3 line: supports a growth visibility reading, not a Pillar 3 premium). Chains: (1) off book losses in opex; (2) default flow down a third, Q1 Stage 2 unresolved; (3) two partners carry the largest slice, cap revisit crossed on one measure; (4) Rs 832 Cr raise buys safety at the cost of RoE; (5) AUM up while disbursement fell, yield falling; (6) cheaper funding real but small (Rs 23-35 Cr pre tax vs ~Rs 87 Cr per point of loss); (7) size ceiling, T3 and Pillar 2L hang on one undisclosed inspection date. thesis_broken_if (B14): Q2 FY27 Stage 2 > 4.11% or GNPA > 2.92%; H2 FY27 all in loss > 11.6% or off book loss rate rising two half-years; revenue margin minus all in loss narrowing two quarters; a top two partner exits or cuts pools > 1/3; RBI cuts the 5% DLG cap or changes recognition; RBI inspection covered FY25 or later; time stop: proof gate not fired by 31-May-2027. Re-open path (B14 §7): Gate 0 lender variant ruling or re-score; price at or below Rs 347.2 (F9 asks to strike); Q2 T3 STARTING; no thesis broken trigger. Return matrix CMP to 31-Mar-2030: Track 1 10.3% / 21.9% / 29.1%; midpoint 14.6% / 26.4% / 33.7%; Track 2 18.5% / 30.6% / 38.0%; cells >= 25%: 5/9.

**Role 3 (Stage 15, B15):** overall WEAKENED BUT ALIVE; growth triggers, moat durability, management trust and valuation safety all weakened. Top counters as in B15 top_counters (partner half multiple and the borrowed 25x row; partner exit mis-sized; Pillar 2L read from on book GNPA; COMPOUNDER at a 1.2 point margin; FY31 partner PAT needs partner AUM ~3.6x; the raise worth Rs 0.85 per Rs 1 and costing ~Rs 21.4 a share; zone above every mechanical entry; proof gate cannot disprove the permanent optics; T3 falsifier loose). Conviction test: NO to 3x; sizing held at Small ceiling, current verdict AVOID. Open items D15-1 to D15-6 (see section 7 and the recommendation).

**Verifier C phase 3 (B12c-valuation):** 0 CRITICAL, 10 MAJOR, 17 MINOR; acceptance 82.1% (78/95); rework not triggered; rulings requested F1, F2, F3, F4, F8; F9 and F10 recomputations pending operator.
