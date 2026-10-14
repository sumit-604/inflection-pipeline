# Stage 11: Role 1 valuation, PHASE 3: CAPILLARY

Run folder: runs/capillary-2026-09-19. Executed 2026-10-10. Model: claude-opus-5-5.
Company: Capillary Technologies India Ltd (CAPILLARY). Entity count ONE; consolidated earnings; line B option value zero (O8).
Frameworks: Master v3.7 Role 1 (file Master_Project_Prompt_v3_6.md) / Section 1B v3.3+v3.5.1+v3.6+v3.7+v3.8+v3.9+v3.10 via the section-1b skill / FTTCP v2.3.
Sole input source: outputs/blocks/B10-valinputs.yaml (Phase 3). Anchoring sources read: outputs/final/fttcp-deliberation.md (authoritative), inputs/research/web-handover-dossier.md Section 6, and the page-marked .txt beside each source PDF (pages cited are PDF pages).

Units: all figures in Rs Cr unless stated. The filings and decks print INR million on their face ("All amounts in Indian Rupees million", Results Q1 FY27 p.9; Results Q4 FY26 p.14-16; Q1 FY27 deck p.26, p.28 "Mn"). Conversion: 10 mn = 1 Cr, done once, shown in each anchor. Per-share figures use 8.24 Cr fully diluted shares (O7) unless stated.

CMP Rs 566.65 (NSE close 09-Oct-2026; deliberation header). Market cap Rs 4,669.2 Cr diluted (566.65 x 8.24) / Rs 4,503.3 Cr basic (566.65 x 7.9472 Cr, BSE SHP Jun-2026).

---

## 0. PRE-FLIGHT, AUTHORITY AND CONSUMED INPUTS

| Check | Result | Anchor |
|---|---|---|
| Halt 1 decision | PROCEED; Mental Model Part 1 signed 09-Oct-2026 | commit 39fe4f1f; dossier Section 2 |
| FTTCP run (mechanical gate) | YES. Part A verdicts, C.2 table with downside rows, Part B sheet present. Signed off 10-Oct-2026 | fttcp-deliberation.md header, Sections B, D; fttcp-draft.md C.2, Part B (section-1b chunk 16) |
| FTTCP verdicts (Phase 3) | Revenue FIRING/FIRING +2; Margin FIRING/FIRING +2; Cash IMPROVING/STARTING +1; ROCE STRUCTURALLY LOW / RECOVERING (p about 0.65) +1. Composite 6/8, BUY-candidate SMALL-MEDIUM. Kernex cap no; TRIM no | deliberation B; B10.fttcp_scores |
| Signal Gate | Passed: 14 tracker rows, 3 external (rows 3, 12, 13); demand_externally_verifiable true, so no DEEP WATCH cap | dossier Section 5; B10.demand_externally_verifiable |
| Debt Capacity block (consumed) | NOT FOUND. Not run in claude.ai. Gap named, run continues (consumption clause). The company is net cash (borrowings Rs 44.72 Cr at 31-Mar-2026 against cash Rs 506.99 Cr), so capacity does not bind | Master Role 1 consumption clause; Results Q4 FY26 p.15; deck May-2026 p.59 (section-1b chunk 13) |
| Market-Implied block (consumed) | NOT FOUND. Not run in claude.ai. Stage 11 computes its own reverse-engineered growth in Section 2.13 for the recognition-gap resolution (override 13) | section-1b chunk 14 |
| Entity-count gate | ONE entity. Single valuation. Line B is a tracked slice with zero separate value (O8) | B10.entity_count; dossier 6.7(1) |
| Credibility grade | B (Good), operator O9; Verifier B read B-/C+ (conflict recorded) | B10.credibility_grade; deliberation A O9 |
| Tier | A (25% hurdle, threshold 1.953). Tier B fails: Gate 0 AVERAGE (core 51) and EM 24 (Verifier C 21.9) both miss; promoter CAUTION | deliberation C; B10 (section-1b chunk 06, A4.3) |
| Macro sheet | August 2026 fill, filled 18-Aug-2026, next refresh 1-Sep-2026. **STALE on 10-Oct-2026.** Values used with the stamp: 10-yr G-sec 6.76%, ERP 7.31%, market CoE about 14.1%, nominal GDP 10.0%, Nifty 50 PE about 20.5x, Smallcap 250 PE 34.4x, terminal growth cap 6.0% | macro-sheet.md (section-1b chunk 15) |
| Operator-approved base | Destination exit P/E 30x on BOTH tracks (operator override O5, 10-Oct-2026); earnings basis FORWARD, exit end-FY29 on FY30 operating EPS (O6) | deliberation, OPERATOR-APPROVED VALUATION PILLARS |

Single-credit map, verified before valuing (section-1b chunk 04): ROCE recovery credited in Pillar 1 (60/40 blend), not in Strategic Premium. Capital base fixed once, by Route A (operator O1 operating basis), not by FTTCP B6 (B6 route NONE). Depressed base year: not applicable (no Route B; B3 normalised PAT not used, the A21 run-rate base governs). Cash quality priced once, in Pillar 2. Complexity priced once, in r (+0.5). Line B priced once, through consolidated EPS on the ledger (rows L5, L6), never as a separate option slice (O8).

Interim state: pre-flight complete; no mechanical stop; two consumed blocks NOT FOUND and named.

---

## 1. SECTION 1A: METHOD SUITABILITY MATRIX

Business: asset-light enterprise loyalty SaaS. Subscription 94.5% of Q1 FY27 revenue (Q1 FY27 deck p.23). Profitable at the operating line but thin (run-rate operating PAT Rs 57.4 Cr). Heavy D&A from acquired intangibles (Rs 74.97 Cr FY26, Results Q4 FY26 p.14). Net cash. No dividend. FCF positive in FY26 (Rs 110.54 Cr).

**Earnings-based**

| Method | Suitable here? | Weight | Reason |
|---|---|---|---|
| P/E | YES, PRIMARY | 80% | Profitable on the operator's operating EPS definition (O7), which strips the distortions (exceptionals, treasury income, tax shelter). The Section 1B destination PE is defined on this basis. Forward basis approved (O6) |
| PEG | Cross-check only | 0% | Growth is decelerating organically (83.7% to 35.5% to 15.5%, FY24-FY26, AR p.79) and FY27 growth is acquisition-led. PEG would read the SessionM step as organic |

**Enterprise value**

| Method | Suitable here? | Weight | Reason |
|---|---|---|---|
| EV/EBITDA | Partially; not applied | 0% | D&A is about 28% of FY30 base adjusted EBITDA (Rs 100 Cr of Rs 356.4 Cr), mostly acquired amortisation. The Master 0.6-0.7x-of-PE rule would reprice that amortisation, which the operator kept inside EPS (O7), and so credit it a second time. A structure-consistent EV/EBITDA (15.5x on FY30 operating EBITDA, the arithmetic twin of 30x P/E) adds no information |
| EV/Sales | No | 0% | The company is profitable; margin path is the thesis |
| EV/Gross profit | No | 0% | Revenue is not pass-through (campaign services 0.7%, deck p.23) |
| EV/Capacity | No | 0% | Asset-light service |

**Asset-based**

| Method | Suitable here? | Weight | Reason |
|---|---|---|---|
| P/B | No | 0% | Book value Rs 128.9/share (basic) is mostly IPO cash and goodwill (Rs 309.58 Cr, Results Q4 FY26 p.15); it captures none of the contract base |
| NAV | No | 0% | Operating business |

**Cash flow**

| Method | Suitable here? | Weight | Reason |
|---|---|---|---|
| DCF | Partially, SECONDARY | 20% | FCF positive and 94.5% recurring revenue make cash flows forecastable. But growth is high and terminal value is 88% of base EV (Section 3), above the Master's 70% sensitivity line, so the weight stays low |
| DDM | No | 0% | No dividend (B10.dps_rs) |

**Sector-specific**

| Method | Suitable here? | Weight | Reason |
|---|---|---|---|
| EV/ARR | Suitable in principle; not applied | 0% | Needs a live, dated peer EV/ARR. Held: Eagle Eye about 2.9x ARR (dossier V4, secondary, older) and Talon.One about 12.5x ARR (secondary). Neither is a live peer table; model-memory multiples are barred (Correction 6). PENDING LIVE PEER TABLE |
| SOTP | Not used | 0% | The signed Part 1 named SOTP primary; operator O8 / dossier 6.7(1) superseded it: line B option value zero, consolidated earnings valued once |

### Final method selection

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E on one-year-forward operating EPS at the Section 1B destination (operator-approved 30x) | 80% | The framework's default primary; clean operating EPS exists; forward basis approved |
| SECONDARY | DCF (FCF after ESOP, Master parameter sets) | 20% | Independent of the exit multiple; low weight for terminal sensitivity |
| | | 100% | |

---

## 2. SECTION 1B: FOUR-PILLAR EXIT MULTIPLE

### 2.1 Converter gate (Amendment 17.0)

Classification: **NON-CONVERTER** because (a) no traded commodity input: costs are people, cloud hosting and software (Results Q1 FY27 p.9 expense lines); (b) pricing is subscription and usage-based, not cost-plus (deck p.10); (c) gross margin did not co-move with any input price: subscription GM 66.4% FY25, 67.2% FY26 (AR p.81), 66% Q1 FY27 (deck p.9). Ambiguity: none. Operator ruling, signed Part 1: NON-CONVERTER for both lines (dossier Section 2). 17.1-17.4 do not apply. (section-1b chunk 11)

### 2.2 Earnings basis and the Amendment 21 run-rate base

Earnings basis (entry and exit): **forward** (operator-approved: Y, O6). Entry: today's price on one-year-forward operating EPS (the A21 run-rate). Exit: 30x on FY30 operating EPS at end-FY29. (section-1b chunk 10, A18.1)

Earnings base: **single-quarter-annualised** (Q1 FY27). B10.seasonal = false (UDRHP-I p.465 "our business is not seasonal"); installation revenue labelled "seasonal fluctuation" is 4.8% of Q1 FY27 revenue (deck p.23), immaterial. (section-1b chunk 08)

| Line (Q1 FY27, deck p.28, Rs mn) | Quarter Rs Cr | Annualised Rs Cr |
|---|---|---|
| Revenue from operations 2,566.4 | 256.64 | 1,026.58 |
| Adjusted EBITDA 440.2 | 44.02 | 176.08 (17.15%) |
| less ESOP 36.9 | 3.69 | 14.76 |
| less D&A 200.4 | 20.04 | 80.16 |
| less finance costs 11.7 | 1.17 | 4.68 |
| = Operating PBT 191.2 | 19.12 | 76.48 |
| less tax at 25% (O7) | 4.78 | 19.12 |
| **= Operating PAT (A21 base)** | **14.34** | **57.36** |
| Operating EPS (8.24 Cr shares) | | **Rs 6.961** |
| Run-rate operating P/E at Rs 566.65 | | **81.4x** |

Check: reported PBT before exceptional items 248.0 mn less "finance income, asset disposal profits, fair valuation and FX gains" 56.8 mn = 191.2 mn (deck p.28; Results Q1 FY27 p.9 line VI 247.98 mn). Ties.

One-offs adjusted: (1) exceptional fraud loss Rs 33.39 Cr stripped (Results Q1 FY27 p.9 line VII 333.86 mn; note p.11); (2) treasury and other non-operating income Rs 5.68 Cr a quarter stripped (deck p.28, 56.8 mn), a depleting IPO cash pile; (3) tax normalised to 25%: the printed Q1 tax of Rs 0.96 Cr includes a one-time deferred tax charge of Rs 1.61 Cr (deck p.13) on a sheltered base; the shelter belongs in the equity bridge (O7). Not adjusted, and named: SessionM is in Q1 for two of three months (closed 01-May-2026; deck p.14), PAT-neutral at its stated break-even, so the annualised revenue understates one month of SessionM per quarter; FX contributed about 6 points of Q1 growth (Q1 FY27 call, B05).

Annual model divergence (cross-check and floor):

| Comparator | Operating PAT Rs Cr | Run-rate vs comparator |
|---|---|---|
| AR FY26 normalised PAT (AR p.82, "Normalized PAT 323" mn; FTTCP B3) | 32.3 | +77.6% |
| FY26 like-for-like at 25% tax (106.92 - 10.73 - 74.97 - 5.46 = 15.76 PBT, deck p.28) | 11.82 | +385% |
| TTM Q1 FY27 at 25% tax (131.97 - 13.28 - 77.74 - 5.46 = 35.49 PBT, deck p.28) | 26.62 | +115% |
| FY27E approved base (dossier 6.5) | 51.4 | +11.6% |

Governing: the run-rate. The FY26 annual model is pre-SessionM and carries a 14.55% adjusted margin against 17.15% now; A21 and A26 bar anchoring to the audited past. The annual model sits below the run-rate, so the floor does not bind. (section-1b chunks 08, 07)

Worksheet line: "Earnings base: single-quarter-annualised | PAT run-rate Rs 57.36 Cr | one-offs adjusted: Q1 FY27 fraud loss Rs 33.39 Cr and non-operating income Rs 5.68 Cr stripped; tax at 25% | annual model divergence 77.6% vs AR normalised FY26 (governing: run-rate, because FY26 predates SessionM and the margin step)."

### 2.3 Pillar 1: ROCE base (row A)

FTTCP ROCE forward verdict: **RECOVERING**, probability about 0.65 with Moderate catalysts (deliberation B). The ">60% with Strong catalysts" row needs Strong catalysts, so the 40-60% row applies: 60/40 weighted average of current and FY[Y+2]. (section-1b chunk 01; FTTCP hybrid-label ban, chunk 16)

| Input | Value | Anchor |
|---|---|---|
| Operating ROCE basis | (adjusted EBITDA - ESOP - D&A) / invested capital ex cash, standing operator rule | O1; dossier 6.1 |
| TTM operating EBIT | Rs 40.95 Cr = (212.2 + 202.9 - 5.6) mn | deck p.28 (FY26 1,069.2 - 107.3 - 749.7; Q1 FY27 440.2 - 36.9 - 200.4; Q1 FY26 189.7 - 11.4 - 172.7) |
| Invested capital, 30-Jun-2026 | Rs 598.62 Cr (5,986.2 mn) | deck p.26 |
| Current (TTM) operating ROCE | **6.84%** (record 6.8%) | arithmetic |
| FY28E operating ROCE | **16.99%** = (220.5 - 15 - 90) / about 680 | deliberation B [INFERENCE], operator-approved |
| Pillar 1 ROCE (60/40) | 0.6 x 6.84 + 0.4 x 16.99 = 4.104 + 6.794 = **10.90%** | approved 10.9% confirmed |
| Base PE | 0.5 x 10.90 + 7.5 = 12.949, rounded **12.9x** | approved 12.9x confirmed |

Normalization route (consolidated Amendment 9): **A-Operational.** Disclosure: company ROCE (EBIT including finance income over capital employed Rs 1,067.62 Cr) 5.2% TTM (deck p.26). Stripped: cash, bank deposits and short-term investments Rs 469.0 Cr (capital employed 10,676.2 mn less invested capital 5,986.2 mn, deck p.26; definitions glossary p.29); finance income Rs 14.91 Cr TTM removed from EBIT (deck p.28: 103.9 + 56.8 - 11.6 mn); ESOP Rs 13.28 Cr TTM deducted (O1 definition). Operational ROCE 6.84%. Route test: unutilised IPO proceeds Rs 203.2 Cr at 30-Jun-2026 (Results Q1 FY27 p.11, 2,032.17 mn) = 19.0% of capital employed, just under 20%; Rs 322.9 Cr = 30.2% at 31-Mar-2026 (AR p.29); total non-operating cash Rs 469.0 Cr = 43.9%. The operator's standing O1 rule fixes the denominator in every case. 9.2 staleness: the IPO objects carry a dated deployment plan (Results Q1 FY27 p.11: cloud, R&D, systems, acquisitions). Route B is not available (STRUCTURALLY LOW; ROCE never stood higher; no pre-depression history). Blend basis: operational-consistent (both endpoints on the O1 basis).

Worksheet line: "FTTCP ROCE forward verdict: RECOVERING (p about 0.65, Moderate) | ROCE used for base: 10.90% | ROCE Base Multiple: 12.9x | ROCE recovery credited via: Pillar 1 (60/40 blend row)." (section-1b chunk 01)

### 2.4 Pillar 2: cash multiplier (rows B, C)

| Line | Value | Anchor |
|---|---|---|
| Cumulative CFO/PAT | N/M (cumulative CFO FY21-FY26 Rs +189.14 Cr against cumulative PAT Rs -202.71 Cr) | B10 (B01 FLAG-GATE0) |
| Latest FY CFO/PAT | 2.86x (149.91 / 52.39; PAT includes the Rs 24.96 Cr exceptional gain) | Results Q4 FY26 p.14, p.16 |
| FCF positive? | Yes FY26 (Rs 110.54 Cr); no FY25 (CFO Rs -46.20 Cr) | Results Q4 FY26 p.16 |
| Band on filed numbers (chunk 02) | 1.00x, volatile ("some good years, some bad"; FY25 negative, FY26 2.86x) | section-1b chunk 02 |
| Structural or growth-induced? | **GROWTH-INDUCED** (prepayment timing). Contract liabilities Rs 125.67 / 74.65 / 98.55 Cr FY24-FY26 (AR Note 22.3 p.233) | operator O3; B10.cash_determination |
| Growth offset | 0 (offsets attach only to the 0.80x growth-induced band) | section-1b chunk 02 |
| **Effective cash multiplier** | **1.15x** (operator ruling O4: upfront billing, CROIC 23.2% TTM deck p.26, CFO/adjusted EBITDA 140% FY26) | deliberation A O4 |
| **Quality-adjusted base (C)** | 12.9 x 1.15 = **14.835x (14.8x)** | record shows 14.9x (carried an unrounded 12.95 base); the chunk 01 rule rounds A first |

Divergence reported, not re-litigated: the chunk 02 band reading is 1.00x; the operator ruled 1.15x. At 1.00x, Track 2 would be 14.9x. FLAG-CASH carried with the multiplier applied (1.15x). The Phase 1 INDETERMINATE cap is superseded by O3. (section-1b chunk 02; OR-5 does not arise because the determination is no longer INDETERMINATE)

### 2.5 Pillar 3: growth visibility (row D) and the Amendment 16 gate

Amendment 16 gate first (section-1b chunk 12): minimum ROCE = the r the valuation uses. A computed RRM r now exists (14.5%, Section 2.9), so it governs over the 13.5% Gate E default (OR-21, chunk 15). Base path operating ROCE: FY27E about 11.7%, FY28E about 17.0% (deliberation B [INFERENCE]). Crossover of 14.5% in FY28. **Growth premium eligible: YES from FY28 (base); NO (bear: FY30E about 11.1%, Section 3.6).** The exit at end-FY29 sits after the crossover.

| Component | Test | Award | Anchor |
|---|---|---|---|
| 3a growth visibility | Two of four qualify: SOM-implied revenue CAGR 22.8% with capacity passing (B09) and delivery grade B (O9). Capex-embedded growth: N/A (asset-light). Order book: none disclosed | **+2x** | B09; O9 (section-1b chunk 03) |
| 3b moat formation | EM 24 (B07), Verifier C 21.9: below 25 | +0x | B07; B13 |
| 3c duration | No filed contracted revenue of 2.5 years' tenor at 2.5x revenue. The Fortune 50 USD 20 m / 5-year contract (Reg 30, 04-Mar-2026) is one account | +0x | B10 downstream candidates |
| **Pillar 3 total** | cap +6x not reached | **+2x** | operator-approved |

Note on 3a: the chunk gates 3a on documented evidence; the SOM figure is a research-built estimate (B09). The operator ruled +2x at grade B (O9); this stands. OR-3 (Amendment 22 vs the 3a/3b/3c evidence gates) remains open; the C.2 probabilities sit beside the table in Section 5.5.

Worksheet: "Emerging Moat Score: 24 / 100 (Verifier C 21.9) | Catalyst proximity: 0-6 months (Kognitiv first migration result and proof gate on the Q2 FY27 call, about Nov-2026) | Evidence quality: mixed (18 documented, 14 claim, 2 inference, B07)". "Growth Visibility Premium: +2x | Shared catalyst? **YES**: revenue compounding and acquired-book margin (ledger L2-L6) drive both the FY28E ROCE endpoint in Pillar 1 and the A16 crossover that unlocks Pillar 3. Role 3 must stress-test this single point of failure." "Entrepreneur Ledger: not yet filled (stage 14, Role 2 §3G). Pillar 3 rests on 3a evidence alone; no ledger fact is credited here or in Strategic." (section-1b chunks 03, 04, 12)

### 2.6 Strategic premium (row E) and single credit

Strategic position: no scarcity. Forrester Leader alongside Kobie and Epsilon (dossier V4) is a competitive position, not a barrier to entry; B07 H1 fails the copyability test. The operator cites "only listed enterprise loyalty SaaS business in India" as a reason for 30x, not as a scarcity premium (B10). **Strategic Premium: +0x.** ROCE recovery credited via Pillar 1, so the +1x/+2x re-rating-optionality route is barred. (section-1b chunk 04)

Single-credit map verified: ROCE recovery Pillar 1 | capital base Route A | base year not applicable | catalyst split revenue 100% / Pillar 3 0% (3a pays on documented growth machinery, not on a catalyst).

### 2.7 UA multiplier, sector cap and override (rows F2, G, G2, G3, H)

| Row | Value | Basis |
|---|---|---|
| UA qualifiers | listed >= 12 m: NO (listed 21-Nov-2025) / Gate 0 >= 60 or EM >= 25: NO (core 51; EM 24) / FII+DII < 3%: NO (Kotak MF crossed 5% on 14-Aug-2026) | B10.ua_qualifiers (section-1b chunk 05) |
| F2 | UA not applied: F2 = F | section-1b chunk 05, Amendment 3 order |
| G sector cap | Platform / SaaS / IT services, **45x**; quality uplift N (UA not triggered) | manifest via B10; deliberation R4 (section-1b chunk 05) |
| G2 Category-Break Override | **N**. Condition 1 fails (loyalty SaaS is an established category with a Forrester Wave); condition 4 fails (named competitors exist) | section-1b chunk 05 |
| G3 | 45x | section-1b chunk 05 |

### 2.8 Four-Pillar Summary (Track 2, additive)

| Step | Calculation | Value | Chunk |
|---|---|---|---|
| A. ROCE Base | 10.90% -> 0.5 x 10.90 + 7.5 | 12.9x | 01 |
| B. Cash Multiplier | 1.15 (O4) + offset 0 | 1.15x | 02 |
| C. Quality-Adjusted Base | 12.9 x 1.15 | 14.835x | 02 |
| D. Growth Visibility Premium | 3a +2, 3b 0, 3c 0; A16 eligible from FY28 | +2x | 03, 12 |
| E. Strategic Premium | no scarcity | +0x | 04 |
| F. Raw Destination PE | 14.835 + 2 + 0 | 16.835x | 06 |
| F2. UA-Adjusted Raw PE | UA not applied | 16.835x | 05 |
| G. Sector Cap | Platform / SaaS / IT services | 45x | 05 |
| G2. Category-Break Override | N | N | 05 |
| G3. Override-Adjusted Cap | G2 = N | 45x | 05 |
| **H. Final Destination PE** | **min(16.835, 45)** | **16.8x** | 06 |

Destination PE range: H +/- 7.5% = 15.57x to 18.10x, rounded to the nearest 0.5x: **15.5x to 18.0x** (section-1b chunk 06). The record shows H 16.9x; the 0.1x gap is rounding of row C (above). Range unchanged.

### 2.9 Track 1 (RRM)

r-adjustment worksheet line: "r base 14.0% (small cap); durability adj 0 (band: Unproven, reason: listed 21-Nov-2025, under five years; numeric band adjustments NOT FOUND in frameworks/, so none is invented; the record carried 0); governance adj 0 (promoter CAUTION, B08; no integrity finding; numeric table NOT FOUND); cyclical surcharge 0 (not cyclical, Part B cyclical flag NO; 12B not engaged); complexity adj +0.5 (Amendment 13: 12 subsidiaries across 9 countries per Results Q1 FY27 p.10; standalone revenue 75.7% related party per the draft; the Czech step-down fraud shows where cash sits is hard to see); cash-conversion r-UP: none per 12A; short-record r-UP: none per 12C; final r 14.5% (bounded [9%, 18%])." (section-1b chunk 15)

RRM = 1 + (13.5 - 14.5) x 0.12 = **0.88** (within x0.70 to x1.60). Track 1 = C x RRM = 14.835 x 0.88 = 13.055, **13.1x** (record 13.1x confirmed). Range 12.08x to 14.03x, rounded **12.0x to 14.0x**. Macro check: market CoE about 14.1% vs RRM neutral 13.5%, gap 60 bps, below the 100 bps review trigger (macro Aug-2026, stale).

Track divergence: (16.835 - 13.055) / 16.835 = **22.5%**, above 15%. Track 2 fits this business better on the pillar build: it carries the evidenced 3a growth premium that the RRM spine omits, and the RRM already prices complexity in r. Under open ruling OR-1 the more conservative track (Track 1) would set the entry zone on a pillar base. Here the operator approved 30x on BOTH tracks, so the two tracks coincide at the governing multiple; OR-1 is moot for the entry zone. (section-1b chunk 06, OR-1)

### 2.10 Approved base against the pillar destination (Amendment 20.9)

| Item | Value |
|---|---|
| Pillar destination, Track 2 (re-derived) | 16.8x (15.5x to 18.0x); record 16.9x |
| Pillar destination, Track 1 (re-derived) | 13.1x (12.0x to 14.0x); record 13.1x |
| Operator-approved base (governing) | **30x both tracks** (O5), range +/- 7.5%: 28.0x to 32.5x |
| Approved vs Track 2 | +78.6% (30 / 16.8) |
| Approved vs Track 1 | +129.0% (30 / 13.1) |
| Pillar 1 ROCE that 30x would need at 1.15x and +2x | about 34%: (30 - 2) / 1.15 = 24.35x base PE; 24 + 0.3 x (R - 33) = 24.35 gives R = 34.2% |
| Independent DCF (Section 4.2) | implies 16.7x on FY30 EPS at end-FY29 |
| Adjusted peer base (Step 1C) | PENDING LIVE PEER TABLE |

Divergence stated plainly: Section 1B, on the operator's own operating-ROCE basis, supports about 17x (Track 2) or 13x (Track 1). The DCF agrees with the pillar build. 30x needs either a Pillar 1 ROCE near 34% or a live adjusted peer base at or above 30x (Section 2.12). CLAUDE.md bars round-number exit defaults; the deliberation records 30x as a dated operator ruling with reasons ("the peer cross-check, and Capillary is the only listed enterprise loyalty SaaS business in India"). **Valued on the approved 30x (A20.9; wrapper "do not overwrite the operator's call"). No different exit multiple substituted.** (section-1b chunk 15, 20.9)

### 2.11 Relative PE expression (Amendment 15)

absolute H 16.8x (pillar) / 30x (approved) | market PE 20.5x (Nifty 50, macro sheet dated Aug-2026, STALE) | relative destination PE 0.82 (pillar) / 1.46 (approved) | current run-rate 81.4x = 3.97 relative | name historical relative band: NOT FOUND (listed 21-Nov-2025, under one year) | sector historical relative band: NOT FOUND (no live peer table) | B8 rating NONE (FTTCP draft Part B) | conclusion: B8 NONE makes this a check that H assumes no unsupported re-rating. The pillar H sits below the market multiple; the approved 30x embeds a 1.46 relative premium that no held peer evidence supports yet. Against the Smallcap 250 (34.4x, itself 22% above its 5-year median per the sheet), 30x is 0.87 relative. (section-1b chunk 15)

### 2.12 Step 1C: relative valuation cross-check (Amendment 20)

| Item | Value |
|---|---|
| Peer set (operator O10) | Eagle Eye, Affle, RateGain, Braze, Klaviyo, Tanla or Route Mobile; Newgen and Intellect excluded; Zaggle reference only |
| Held live data | RateGain trailing P/E 41.8x, EV/EBITDA 21.6x, ROCE 12.6% (Value Research, 09-Oct-2026, per Claude web; dossier 6.3). Eagle Eye about 13x EBITDA, 2.9x ARR (dossier V4, secondary, older) |
| Adjusted peer base | **PENDING LIVE PEER TABLE.** One trailing P/E is not an adjusted peer base; A20 needs 4-6 peers on clean or forward earnings, clustered, with signed adjustments. Not built from memory (Correction 6) |
| Pillar destination (governing track) | 16.8x |
| Relative route opens (A20.5) | adjusted peer base above 16.8 / 0.70 = **24.0x** |
| Section 1B reaches 30x only if | the live adjusted peer base is **30x or higher** (relative governs at the adjusted base, bounded by [pillar, 45x cap], A20.6) |
| % gap, pillar vs approved | pillar sits 44.0% below 30x |
| Governing multiple | operator-approved 30x (A20.9) |

Non-governing observation: the two held EBITDA multiples (RateGain 21.6x trailing; Eagle Eye about 13x, older) sit below Capillary's own EV / run-rate adjusted EBITDA at CMP of 23.8x (EV Rs 4,199.5 Cr / Rs 176.08 Cr). They neither support nor refute 30x on their own.

### 2.13 Recognition gap resolution and market-implied growth (override 13)

Signed model (09b Section 2 Part B1): FROM sits between R1 and R2; TO is R3 VALUE-ADDED / SPEC'D SUPPLIER (about 19x neighbourhood), with a stated ambition toward R4 (about 21x).

Current PE: **81.4x** on the A21 run-rate (82.5x trailing on FY26 diluted EPS Rs 6.87; 90.8x on FY27E base EPS Rs 6.24; 56.3x on FY28E Rs 10.06).

**RECOGNITION GAP: CLOSED.** The current PE sits far above the TO rung's neighbourhood on every earnings reading, above R5 (about 24x plus strategic premium), and above the operator's own 30x. The re-rating engine is negative: the exit at 30x on forward EPS means a multiple fall from 81.4x to 30x (-63%). The return rides EPS CAGR alone, against a de-rating headwind. With the proof gate NOT FIRED and the ugliness ARTIFACT-OF-CLIMB (09b B5), the Transition Decision Matrix cell is **PRICED NARRATIVE (TRAP)**: "AVOID or hard WATCH with no position until the proof gate fires AND the price re-opens the gap." The deliberation carried RESEARCH / WATCH on "gap OPEN" before this resolution. Stage 13 applies the matrix; this stage resolves the gap.

Rung note: 30x sits above the R5 neighbourhood. FROM R1-R2 to an R5-level multiple inside three years is a multi-rung leap; CLAUDE.md treats a claimed multi-rung leap as itself a red flag.

Market-implied growth (stage 11 computation; the claude.ai block was not run). Price CAGR identity on the forward basis, net cash Rs 57 held static, cost of equity r = 14.5% (Section 2.9). Required end-FY29 value to earn r: 566.65 x 1.145^3 = Rs 850.6.

| Reading | Exit PE | FY30 EPS the price needs | EPS CAGR from Rs 6.96 |
|---|---|---|---|
| 1. Flat multiple | 81.4x (not admissible as an exit: above the 45x cap) | (850.6 - 57) / 81.4 = Rs 9.75 | 11.9% |
| 2a. Sector cap (chunk 14 default) | 45x | Rs 17.64 | 36.3% |
| 2b. Operator-approved | 30x | Rs 26.45 | 56.0% |

Evidence: approved base FY30 EPS Rs 21.33 (45.3% CAGR); grade-weighted scenarios Rs 20.56 (43.5%); probability-weighted ledger Rs 14.16 (26.7%, Section 5.5).

Implied story at Rs 566.65 and a 30x exit: the market assumes FY30 revenue near Rs 1,875 Cr at the base 22% margin (the bull revenue path), or base revenue of Rs 1,620 Cr at a 25.5% margin (above the bull's 25%). It assumes the acquired books migrate cleanly and grow, and ROCE keeps climbing past 17%. It assumes a fall in multiple from 81x only to 30x, not to the 17x the pillar build gives.

Spread statement: "Price assumes 56.0% EPS CAGR at the operator's 30x (36.3% at the 45x cap); FTTCP evidence supports 26.7% (ledger) to 45.3% (approved base). The spread runs against the buyer." **Flag: PRICED-WE-ARE-LATE** at the governing multiple. (section-1b chunk 14)

### 2.14 Hurdle Ratio (feasibility band)

HR = (FY30 EPS / run-rate EPS) x (30 / 81.40). Forward basis at both ends (A18.1). Threshold Tier A 1.953. Bull EPS CAGR usable: grade B (O9). (section-1b chunk 06; OR-2; OR-27)

| Case | FY30 EPS | (1 + EPS CAGR)^3 | EPS CAGR | HR |
|---|---|---|---|---|
| Bear | 7.436 | 1.068 | 2.2% | 0.39 |
| Base (approved scenario) | 21.335 | 3.065 | 45.3% | 1.13 |
| Bull | 32.153 | 4.619 | 66.5% | 1.70 |
| Grade-weighted scenarios (Good) | 20.565 | 2.954 | 43.5% | 1.09 |
| **Probability-weighted ledger on the A21 base (governing HR input)** | **14.163** | **2.035** | **26.7%** | **0.75** |

**Feasibility band: STOP** (HR on bull earnings 1.70 < 1.953). The 25% hurdle is infeasible at 30x even on bull-case earnings, because the multiple falls from 81.4x to 30x. Per OR-2 the band caps no verdict; every section runs. Confirms the deliberation's base 1.13 and bull 1.71 (1.70 here on unrounded EPS).

Final validation: "Would you personally pay this destination PE for this quality of business?" At the pillar 16.8x, yes: the DCF lands at the same place. At 30x, no on current evidence: 30x is what Section 1B pays a business with an operating ROCE near 34%; Capillary's blend is 10.9% and its TTM is 6.8%.

**Checkpoint.** Section 1 complete. Methods selected (P/E 80%, DCF 20%). Four-pillar destination PE calculated at 15.5x to 18.0x (H 16.8x; RRM track: 12.0x to 14.0x, H 13.1x). Operator-approved governing exit 30x (28.0x to 32.5x). Current PE is 81.4x (run-rate operating). Hurdle Ratio band: STOP (caps no verdict).

---

## 3. SECTION 2: EARNINGS AND CASH FLOW PROJECTIONS

Scenarios are operator-approved (O11, dossier 6.5). All figures are [INFERENCE] per the dossier. Common inputs: ESOP Rs 14/15/16/17 Cr; D&A Rs 85/90/95/100 Cr (FY27-FY30); finance cost Rs 5 Cr; tax 25%. Stage 11 recomputed every PAT and EPS from these inputs; all tie to the dossier within rounding.

### 3.1 2A Revenue

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| Growth logic | One or two triggers fail: acquired books shrink in migration, organic slows to about 10%, FX reverses | Run-rate plus guide for FY27; then guidance-discounted 15% a year | Management's 20%+ organic at face value (grade B allows) |
| Revenue CAGR FY26-FY30 | 16.6% | 21.9% | 26.8% |
| Revenue CAGR FY27-FY30 | 10.0% | 15.0% | 20.0% |
| Year 0 FY26 (Results Q4 FY26 p.14) | 734.60 | 734.60 | 734.60 |
| A21 run-rate (Q1 FY27 x 4) | 1,026.58 | 1,026.58 | 1,026.58 |
| Year 1 FY27 | 1,020 | 1,065 | 1,100 |
| Year 2 FY28 | 1,122 | 1,225 | 1,320 |
| Year 3 FY29 | 1,234 | 1,410 | 1,584 |
| Year 4 FY30 (committed, A18.0) | 1,358 | 1,620 | 1,901 |
| Year 5 FY31 | NOT PROJECTED (not in the approved scenarios; A18.0 requires Year 4, met). DCF uses a named extension: 1,494 / 1,814 / 2,281 | | |

Bear rule check: lower of historical CAGR 42.2% - 5 = 37.2%, industry growth 12% (B09 tam_growth_pct), or triggers failing: 10% after FY27 sits below industry. Bull rule: guidance at face value, grade B. (section-1b chunk 07)

Base-case basis (Rule B, A26.1): **RUN-RATE for FY27** (Q1 FY27 revenue Rs 256.64 Cr x 4 = Rs 1,026.58 Cr, Results Q1 FY27 p.9; the step to Rs 1,065 Cr is the FY27 guide, "on track" per deck p.20, with SessionM in every month from Q2), then **GUIDANCE-DISCOUNTED for FY28-FY30**: management's "20%+ organic annual growth rate" (deck May-2026 p.62) x trailing credibility ratio 0.72 (5 of 9 promises delivered, 3 partial at half credit: 6.5 / 9, B05) = 14.4%, approved at 15%.

Historical CAGR cross-check: 42.2% FY23-FY26 (UDRHP-I p.55; AR p.232). Divergence: base FY26-FY30 21.9% is 20.3 pp BELOW historical. The divergence exceeds 10 pp; confirm-by observations: H1 FY27 constant-currency organic growth (Q2 FY27 results, about Nov-2026) and FY28 revenue of at least Rs 1,225 Cr (May-2028). Both sit on the ledger (L2, L3).

SOM cross-check: base FY29 Rs 1,410 Cr vs SOM Rs 1,361 Cr (B09), +3.6%; base FY26-FY29 CAGR 24.3% vs SOM-implied 22.8%. **Justified excess:** B09 states its SOM math does not underwrite the SessionM step (+37.2% one-off, closed 01-May-2026, filed). FY28-FY30 base growth of 15% sits below the SOM-implied 22.8% (3-year) and 21.1% (5-year).

A14 fade check (FLAG): EM MODEST fades growth to industry growth by Year 3. Industry growth = 12% (B09 tam_growth_pct). The approved base holds 15.1% in Year 3 (FY29) and 14.9% in Year 4. An A14-faded base (FY28 15%, FY29 12%, FY30 12%) gives FY30 revenue Rs 1,537 Cr, PAT Rs 162.1 Cr, EPS Rs 19.67 and a 30x value of Rs 647 (-Rs 50 vs Rs 697). Valued on the approved scenarios (O11); divergence reported.

Second reading on revenue (A26.3). Reading (a): consolidated growth holds about 15%, because organic NRR is 111% (deck p.22), TTM new ACV rose 75% (deck p.16) and organic revenue grew 17% in Q1 FY27 (Rs 1,551 mn, deck p.15). Reading (b): consolidated growth settles near 10%. Acquired books were 39.6% of Q1 FY27 revenue: Rs 1,015.4 mn of Rs 2,566.4 mn, from deck p.15 by arithmetic. The company itself says migration dynamics normally put inorganic NRR below 100% (deck p.22). Organic growth also carries three live readings: 17%, about 11% in constant currency, and 3-6% (09b C1.1). The separating observation is the Q2 FY27 deck's constant-currency organic growth and blended NRR (about Nov-2026), then inorganic NRR in the Q4 FY27 deck, after the Kognitiv base effect lapses (May-2027). The doubt is sized, not shaded: ledger row L3 at p 0.45 (Section 5.5) and the dispersion cap.

### 3.2 2B Profitability

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| Adjusted EBITDA margin FY30 | 15.0% | 22.0% | 25.0% |
| Margin logic | Q1 FY27 run-rate 17.15% less about 200 bps. Margin-reset name (OR-11): the trailing three-year average (about 9% on the filed basis: FY24 -0.28%, FY25 13.13%, FY26 14.51%, UDRHP-I p.55, AR p.12) includes the pre-reset loss year, so the bear comes from the evidence | Destination-mix bridge below | Management's 25-30% steady state at its floor (grade B) |
| Depreciation (FY30) | 100 | 100 | 100 |
| Interest cost | 5 | 5 | 5 |
| Tax rate | 25% | 25% | 25% |
| PAT margin FY30 | 4.5% | 10.9% | 13.9% |
| Share dilution | 8.24 Cr fully diluted held (includes 29.02 lakh ESOPs, BSE SHP Jun-2026); future grants priced through ESOP expense inside EPS | same | same |

Base-case margin bridge (Rule C, A26.2). Lever sizes split the approved base lift across the named levers in the proportions of the FTTCP draft's C.2 increments (row 2 : row 4 : row 3 = 15 : 25 : 40). The approved scenario sets the total, and the draft rows set the split.

| Lever | bps to Year 3 (FY29) | bps to Year 4 (FY30) | Evidence | Confirm-by |
|---|---|---|---|---|
| Current margin FY26 | 14.55% | 14.55% | adjusted EBITDA 1,069.2 / revenue 7,346.0 mn, deck p.28 | n/a |
| Printed to the Q1 FY27 run-rate (non-COGS leverage, SessionM synergies, FX) | +260 | +260 | Q1 FY27 17.15% (deck p.28); non-COGS +32% vs revenue +43% (deck p.9) | printed |
| Organic operating leverage (ledger L4) | +65 | +103 | about 60% of costs are non-COGS (deck p.9) | Q3 FY27 results (Feb-2027) |
| Kognitiv migration, 30% to about 65% GM (ledger L5) | +109 | +172 | deck p.9; prior books migrated, "only two customers remain" (deck p.27); first go-live 01-Sep-2026, full by Sep-2027 (Q1 FY27 call) | Q2 FY27 call (Nov-2026); Sep-2027 |
| SessionM ramp from break-even (ledger L6) | +175 | +275 | "tracking to the planned $32M ARR", break-even in year one (deck p.14) | Q4 FY27 (May-2027); Q4 FY28 (May-2028) |
| Optum warrant charge step-up, contra revenue (ledger D1) | -74 | -64 | about Rs 31 Cr a year from Rs 20.6 Cr (RHP pp.71-73 per claude.ai; not in corpus) | FY28 AR |
| **Base-case margin** | **19.90%** | **22.00%** | | |

The bridge lifts margin 535 bps from FY26 to Year 3, above 400 bps. The Rule F chain that pays for it is FTTCP Step 4.5 Chain 3: acquired books move to the Capillary platform at about 65% GM, so cost to serve falls while subscription billing holds, but retention is lost before margin rises. Chain 1 carries the capital side. Stage 14 (Role 2 §3.5) must carry this chain by number. (section-1b chunk 07)

### 3.3 2C Projection table (base primary; bear | bull as ranges)

| Line | Year 0 FY26 | Run-rate | Y1 FY27 | Y2 FY28 | Y3 FY29 | Y4 FY30 | Y5 FY31 |
|---|---|---|---|---|---|---|---|
| Revenue | 734.60 | 1,026.58 | 1,065 (1,020 / 1,100) | 1,225 (1,122 / 1,320) | 1,410 (1,234 / 1,584) | 1,620 (1,358 / 1,901) | NOT PROJECTED |
| Adjusted EBITDA | 106.92 | 176.08 | 172.5 | 220.5 | 280.6 | 356.4 (203.7 / 475.3) | |
| Adjusted EBITDA margin | 14.55% | 17.15% | 16.2% | 18.0% | 19.9% | 22.0% (15 / 25) | |
| Operating PAT (25% tax) | 11.82 (reported 52.39) | 57.36 | 51.4 (36.8 / 62.3) | 82.9 (43.7 / 115.5) | 123.4 (51.8 / 186.2) | 175.8 (61.3 / 264.9) | |
| Operating EPS (8.24 Cr) | 1.43 (reported diluted 6.87) | 6.96 | 6.24 (4.46 / 7.55) | 10.06 (5.31 / 14.02) | 14.98 (6.29 / 22.60) | 21.33 (7.44 / 32.15) | |
| Book value / share (8.24 Cr) | 124.2 (basic 128.9) | | 126.4 | 136.5 | 151.4 | 172.8 | |
| Est. CFO (adj. EBITDA less 25% tax; WC neutral) | 149.91 | | 155.4 | 192.9 | 239.4 | 297.8 | |
| Est. FCF (CFO less capex at 5.36% of revenue) | 110.54 | | 98.3 | 127.2 | 163.9 | 211.0 | |
| Est. net cash (held at the anchor, A19.0) | 438.95 B/S; 469.7 bridge | | 469.7 | 469.7 | 469.7 | 469.7 | |
| Est. operating ROCE | 3.9% | 13.6% (Q1 annualised) | 11.7% | 17.0% | 23.2% | 30.5% | |
| Est. ROE | 7.4% (RONW, deck p.26) | | 5.0% | 7.7% | 10.4% | 13.2% | |

Notes: Capex ratio 5.36% = 393.74 / 7,345.99 mn (Results Q4 FY26 p.16, p.14). Book value path = FY26 equity Rs 1,023.49 Cr (Results Q4 FY26 p.15) plus base operating PAT less the Q1 FY27 fraud loss Rs 33.39 Cr; it excludes OCI and the ESOP reserve. ROCE FY27E and FY28E are the deliberation's [INFERENCE] (invested capital about Rs 628 Cr and about Rs 680 Cr). FY29E and FY30E are stage 11 [INFERENCE]: invested capital extrapolated at +Rs 52 Cr a year (the FY27E to FY28E step). A new acquisition would reset it higher (draft Chains 1 and 5). Net cash is held static: interim FCF of Rs 389.4 Cr (FY27-FY29 base) is not credited, because B7 Year-3 net debt is NOT FOUND and the company states it will deploy closing cash and accruals into M&A (deck May-2026 p.63).

### 3.4 2C-w worksheet line (state in full)

"Base-case basis: RUN-RATE (FY27) then GUIDANCE-DISCOUNTED (FY28-FY30). Evidence: Results Q1 FY27 p.9 (revenue 2,566.44 mn, quarter ended 30-Jun-2026, filed 04-Aug-2026); FY27 guide Rs 10,650 mn 'on track' (Q1 FY27 deck p.20); 20%+ organic aspiration (deck May-2026 p.62) x trailing credibility ratio 0.72 = 14.4%, approved at 15%. Historical CAGR cross-check: 42.2% (divergence -20.3 pp, confirm-by observation: H1 FY27 constant-currency organic growth at least 15% and FY28 revenue at least Rs 1,225 Cr, dates: Nov-2026 and May-2028). Margin bridge: current 14.55% -> Year 3 19.90% via [printed run-rate step: +260 bps, deck p.28] + [organic operating leverage: +65 bps, deck p.9] + [Kognitiv migration: +109 bps, deck p.9 and Q1 FY27 call] + [SessionM ramp: +175 bps, deck p.14] + [Optum warrant step-up: -74 bps, RHP per claude.ai] x 5. Track-record period for weighting: trailing 3 quarters (listed 21-Nov-2025; Q3 FY26, Q4 FY26, Q1 FY27), Role 5 grade B (operator O9). Catalyst credit split: revenue 100% / Pillar 3 0%." (section-1b chunk 17)

### 3.5 Horizon, exit basis and the Option Resolution Calendar (Amendment 18)

- Horizon: Year 4 (FY30) is committed in bear, base and bull. Year 5 is preferred, not mandatory; not in the approved scenarios. Credible Year 4-5 story: yes (EM MODEST, not None; runway STRONG, 7.9x headroom, B09). No exit haircut. (section-1b chunk 10, 18.0)
- Exit basis: forward at both ends (O6). Year-3 exit = 30x x FY30 EPS + net cash. (18.1)
- Option slices (18.2): calendar kept for tracking only (O8; dossier 6.7(1)).

| Slice | Window | Class | Resolution event | Tracker row | Valuation treatment |
|---|---|---|---|---|---|
| SessionM | FY28-FY29 | RESOLVES-WITHIN-HOLD | ARR at least USD 27 m and break-even by Q4 FY27; CM at least 15% by Q4 FY28 | Row 4 | Separate value ZERO (O8). Credited once through consolidated EPS, ledger L6 |
| Kognitiv | FY28 | RESOLVES-WITHIN-HOLD | Full migration with retained revenue at least 80% of FY26 | Row 5 | Separate value ZERO (O8). Credited once, ledger L5 |
| Unmigrated remainder | NOT FOUND | none | No nameable event in the corpus | none | Zero (18.2) |

- 18.3 mirrored: the bear case carries L5 and L6 at failure. 18.6 dual display: static-carry exit Rs 0 and resolution-based exit Rs 0 for the separate slices; delta Rs 0 per share, because O8 moves line B inside consolidated earnings.

### 3.6 2D Projection sanity checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than capacity allows? | Asset-light SaaS; capacity not binding (B09 capacity_check: sufficient) | PASS |
| Margins require something unprecedented? | 22.0% FY30 has never printed at company level (best quarter Q4 FY26 18.7%: 357.2 / 1,913.5 mn, deck p.28). Deal-cohort precedent exists: three earlier books reached 40-45% contribution margin after migration (09b B2, AR p.79-80) | PASS WITH FLAG |
| ROCE stays above 15%? | Base: from FY28E (17.0%) onward; FY27E 11.7% below. Bear: never (FY30E about 11.1% [INFERENCE]) | PARTIAL |
| FCF sufficient to fund growth without excessive new debt? | Base FCF positive every year; net cash Rs 469 Cr | PASS |
| EPS growth driven by operations, not financial engineering? | Operating EPS strips treasury income; tax held at 25%; no buyback. FY27 growth is partly acquired (SessionM), which is operations | PASS |
| Implied market share gain realistic? | SAM share 12.6% today (B09); base FY29 Rs 1,410 Cr against SAM grown at 12% (Rs 8,198 Cr) = 17.2%; justified excess over SOM is the closed SessionM deal | PASS WITH NOTE |
| CFO/PAT trajectory consistent with Pillar 2? | Projected CFO/PAT 3.0x / 2.3x / 1.9x / 1.7x supports 1.15x. History is volatile: FY25-FY26 average CFO / adjusted EBITDA = 103.7 / 181.4 = 57% (Results Q4 FY26 p.16; deck p.28). Tracker row 10 falsifier: OCF/EBITDA below 60% in FY27 | PASS WITH FLAG |
| Year 3 ROCE consistent with the FTTCP verdict used in Pillar 1? | FY29E 23.2% [INFERENCE] fits RECOVERING (crosses 13.5% on TTM by Q2 FY28). FIRING needs the recovery to print first | PASS |
| **Did the base case credit the transition, or price the audited past?** | It credits the transition. Revenue runs off the run-rate and discounted guidance, not historical CAGR. Margin runs off the bridge (14.55% to 22%), not the trailing three-year average (about 9%) | PASS |

**Checkpoint.** Section 2 complete. Projections built on the approved scenarios. Flags: A14 fade divergence; margin 22% unprecedented at company level; revenue second reading named.

---

## 4. SECTION 3: APPLY EACH VALUATION METHOD

### 4.1 PRIMARY: P/E

Step 1: exit P/E from Section 1B.

| Source | Exit PE range |
|---|---|
| Four-Pillar destination (Track 2, re-derived) | 15.5x to 18.0x (H 16.8x) |
| RRM-track destination (Track 1) | 12.0x to 14.0x (H 13.1x) |
| Sector cap | 45x |
| **Applied exit PE range (operator-approved, A20.9)** | **28.0x to 32.5x (mid 30x)** |

Step 2: target price matrix, end-FY29 (Year 3), value = PE x FY30 EPS + Rs 57; CAGR over 3 years from Rs 566.65.

| | Exit PE 28.0x | Exit PE 30.0x | Exit PE 32.5x |
|---|---|---|---|
| Bear EPS Rs 7.44 | Rs 265 -> -22.4% (red) | Rs 280 -> -20.9% (red) | Rs 299 -> -19.2% (red) |
| Base EPS Rs 21.33 | Rs 654 -> 4.9% (red) | Rs 697 -> 7.2% (red) | Rs 750 -> 9.8% (red) |
| Bull EPS Rs 32.15 | Rs 957 -> 19.1% (amber) | Rs 1,022 -> 21.7% (amber) | Rs 1,102 -> 24.8% (amber) |

Colour code: green at 25% or more; amber 15-25%; red below 15%. No cell is green.

Cross-check at the pillar destinations (not governing):

| | Track 2 15.5x | Track 2 16.8x | Track 2 18.0x | Track 1 13.1x |
|---|---|---|---|---|
| Bear EPS 7.44 | Rs 172 | Rs 182 (-31.2%) | Rs 191 | Rs 154 |
| Base EPS 21.33 | Rs 388 (-11.9%) | Rs 415 (-9.8%) | Rs 441 (-8.0%) | Rs 336 (-16.0%) |
| Bull EPS 32.15 | Rs 555 | Rs 597 (+1.8%) | Rs 636 | Rs 478 |

Step 3: reverse-engineered entry. Year 3 target = Rs 21.335 x 30 + 57 = Rs 697.05. Required entry for 25% = 697.05 / 1.953125 = **Rs 356.9** (confirms dossier 6.6 "about Rs 356").

P/E method fair value range (Year 3): Rs 280 (bear) / Rs 697 (base) / Rs 1,022 (bull). These confirm dossier 6.6 (Rs 280 / 696 / 1,023) within unrounded-EPS rounding.

### 4.2 SECONDARY: DCF

Parameters (Master Section 3 parameter sets; macro sheet Aug-2026, STALE):

| Parameter | Bear (conservative) | Base | Bull (aggressive) |
|---|---|---|---|
| Explicit cash flows | FY30, FY31 to the end-FY29 valuation point (FY27-FY31 projected) | same | same |
| Revenue CAGR FY27-FY30 | 10% | 15% | 20% |
| FCF definition | adj. EBITDA - ESOP - 25% tax on PBT - capex at 5.36% of revenue | same | same |
| FCF % of revenue FY30 | 6.9% | 12.0% | 14.1% |
| Terminal growth | 4% | 5% | 6% |
| WACC / discount rate (net cash, so about CoE) | 14% | 12% | 11% |

Terminal growth ceiling = min(6% Master cap, nominal GDP 10.0%, risk-free 6.76%) = 6.0% (macro sheet August 2026, flagged stale). FY31 is a named extension, not an approved scenario: base revenue +12% (A14 industry growth, B09) at the FY30 margin; bear +10%; bull +20%; ESOP Rs 18 Cr and D&A Rs 105 Cr (the approved increments continued). FCF is consistent with Pillar 2 (FCF/PAT 1.10x base FY30) and with operating earnings (O7).

| Base FCF build (Rs Cr) | FY30 | FY31 |
|---|---|---|
| Adjusted EBITDA | 356.40 | 399.17 |
| less ESOP | 17.00 | 18.00 |
| less tax at 25% on PBT (234.40 / 271.17) | 58.60 | 67.79 |
| less capex (5.36% of revenue) | 86.83 | 97.25 |
| **FCF** | **193.97** | **216.13** |

Base valuation at end-FY29 (WACC 12%, g 5%): PV FCF30 = 194.0 / 1.12 = 173.2; PV FCF31 = 216.1 / 1.2544 = 172.3; terminal value = 216.1 x 1.05 / 0.07 = 3,241.5, PV 2,584.1. EV = Rs 2,929.6 Cr. Plus net cash Rs 469.7 Cr = Rs 3,399.3 Cr; / 8.24 = **Rs 412.5**. EV / FY30 PAT = 16.7x. Share of value from terminal value: **88.2%** (above 70%, so low weight).

Sensitivity (end-FY29 value per share, base cash flows):

| WACC \ g | 4% | 5% | 6% |
|---|---|---|---|
| 11% | Rs 416 | Rs 472 | Rs 551 |
| 12% | Rs 371 | **Rs 412.5** | Rs 468 |
| 13% | Rs 336 | Rs 368 | Rs 409 |
| 14% | Rs 308 | Rs 333 | Rs 365 |

Bear (14%, 4%): FCF30 Rs 93.5 Cr, FCF31 Rs 102.0 Cr, EV Rs 976.6 Cr, value **Rs 175.5** (terminal 83.6%). Bull (11%, 6%): FCF30 Rs 268.1 Cr, FCF31 Rs 319.5 Cr, EV Rs 5,997.4 Cr, value **Rs 784.8** (terminal 91.7%). Even the highest grid cell (11%, 6%: Rs 551) sits below CMP on base cash flows.

### 4.3 Method-wise fair value summary (Year 3, end-FY29)

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/E at the approved 30x | 80% | Rs 280.1 | Rs 697.1 | Rs 1,021.6 |
| DCF (Master parameter sets) | 20% | Rs 175.5 | Rs 412.5 | Rs 784.8 |

**Checkpoint.** Section 3 complete. All selected methods applied.

---

## 5. SECTION 4: TRIANGULATION, ENTRY PRICE AND VERDICT

### 5.1 4A Triangulated fair value (both tracks)

The operator approved 30x on both tracks, so Track 1 and Track 2 carry identical fair values at the governing multiple. Pillar-track values are cross-checks (Section 4.1).

| Track 1 = Track 2 (governing 30x) | Bear | Base | Bull |
|---|---|---|---|
| P/E x 80% | 280.1 x 0.8 = 224.1 | 697.1 x 0.8 = 557.6 | 1,021.6 x 0.8 = 817.3 |
| DCF x 20% | 175.5 x 0.2 = 35.1 | 412.5 x 0.2 = 82.5 | 784.8 x 0.2 = 157.0 |
| **Weighted fair value** | **Rs 259.2** | **Rs 640.1** | **Rs 974.2** |

Pillar cross-check, P/E-only: Track 2 (16.8x) Rs 182 / 415 / 597; Track 1 (13.1x) Rs 154 / 336 / 478.

### 5.2 4B Methods agreement

| Check | Result |
|---|---|
| Same direction? | No. P/E at 30x gives base Rs 697 (above CMP); DCF gives Rs 412.5 (below CMP) |
| Spread, highest to lowest base | (697.1 - 412.5) / 412.5 = 69.0% |
| Outlier and why | The P/E at the operator's 30x. The DCF (16.7x implied) and the Section 1B pillar build (16.8x) agree with each other; the 30x override is the source of the spread |
| Method trusted most | P/E on a Section-1B-derived multiple. The method is right; the governing multiple is the open question |

### 5.3 4C Return expectation at CMP (Year 3 = end-FY29, N = 3, approved convention)

| Scenario | Weighted FV | CMP | Total return | CAGR | Meets 25%? |
|---|---|---|---|---|---|
| Bear | Rs 259.2 | Rs 566.65 | -54.3% | -23.0% | NO |
| Base | Rs 640.1 | Rs 566.65 | +13.0% | 4.1% | NO |
| Bull | Rs 974.2 | Rs 566.65 | +71.9% | 19.8% | NO |

P/E-only at 30x: bear -20.9%, base 7.2%, bull 21.7% (confirms the deliberation's -21.0% / 7.1% / 21.8%). Calendar sensitivity: end-FY29 is 2.47 years from 10-Oct-2026. On that calendar the weighted base CAGR is 5.1%; the P/E base is 8.7% and the P/E bull 26.9%. The approved convention (N = 3) governs.

### 5.4 4D Probability-weighted expected return

Weights from the Role 5 grade only (Rule E, A26.4): grade B = Good, 25/50/25, over the trailing three quarters of listed delivery (period stated, under four quarters). Re-weighting rule (actuals below bear on two metrics for two quarters): not triggered. (section-1b chunk 17)

| Scenario | Probability | 3-year CAGR (weighted FV) | Weighted return |
|---|---|---|---|
| Bear | 25% | -23.0% | -5.74% |
| Base | 50% | 4.1% | 2.07% |
| Bull | 25% | 19.8% | 4.95% |
| **Expected CAGR (Good)** | 100% | | **1.3%** |

Alternative reads: CAGR of the weighted value (Rs 628.4) 3.5%. Excellent weights 20/50/30 (operator sensitivity): 3.4%. On the P/E-only 30x values: Good 3.8% (weighted value Rs 673.9, 5.9%); Excellent 5.9% (Rs 711.0, 7.9%). Confirms the deliberation's 3.7% / 5.9%. On the probability-weighted ledger (A22 basis, Section 5.5): FY30 EPS Rs 14.16, value Rs 481.9, CAGR -5.3%.

The grade-weighted scenarios and the ledger disagree. The scenario weights put 75% on base-or-better; the catalyst probabilities put the base revenue lift (L3) at 0.45 and the line B ramps at 0.40. The separating observation is the Q2 FY27 print (about Nov-2026).

### 5.5 Amendments 22 and 23: the Expectation Ledger, rebuilt and ruled

**What stage 11 did, and why.** The C.2 probabilities on B10 are Claude Code proposals, not operator-ruled (B10 flag; LESSONS KISSHT C2P). Stage 11 **replaced** the table rather than ruling the draft rows as they stand, for three reasons:
1. Exit-basis symmetry. The draft built increments for FY29; the operator's forward basis exits on FY30 EPS (O6, A18.1). The ledger target year is now FY30.
2. The ledger gap. The approved base grows PAT from Rs 57.36 Cr (run-rate) to Rs 175.80 Cr (FY30), Rs 118.44 Cr of growth. The draft ledger, probability-weighted, supported about Rs 47 Cr, and much of the base path had no row. A23 bars crediting growth that is off the ledger. The rebuilt ledger puts **100% of the base-case growth on rows**: when all base rows fire they sum to Rs 118.44 Cr exactly. The gap between Rs 118.44 Cr and the probability-weighted Rs 56.25 Cr credit on those rows is the probability discount, not unsupported growth. Anything in the price above T1 + T2 + T3 is the residual.
3. Line B against O8. Rows for SessionM (L6) and Kognitiv (L5) stay on the ledger as consolidated-earnings increments, credited once, through EPS at 30x. The separate line B option value is zero (O8), and no SOTP slice is added. That is single credit. The draft's note that these rows "must never be credited in line A" belonged to the superseded SOTP treatment; under O8, line A and line B merge into consolidated earnings. There is no double count. First, no separate slice value exists. Second, increments are measured above the A21 base, which already holds line B at its current, break-even state. Third, the base margin bridge levers map one-to-one onto L4, L5, L6 and D1.

Increments: FY30 PAT vs the A21 base, 25% tax. Revenue rows use the run-rate margin of 17.152%. Margin rows split the approved base lift (Section 3.2). Probabilities are ruled by stage 11 with the evidence stated, and remain open for operator ratification at /finalize.

| # | Catalyst | Rs Cr PAT increment | p | Evidence basis | Weighted | Tier | Downstream candidate (unverified) |
|---|---|---|---|---|---|---|---|
| L1 | FY27 revenue at least Rs 1,065 Cr (SessionM in every month from Q2, plus Q2-Q4 growth) | +4.94 | 0.85 | Documented: Q1 Rs 256.64 Cr (Results p.9), SessionM closed 01-May-2026 (deck p.14). Management: "on track" (deck p.20). Section C revenue composite 0.85 | +4.20 | T2 | US MarTech budget growth; USD/INR |
| L2 | Revenue compounds at least 10% a year FY28-FY30 (to Rs 1,417.5 Cr) | +45.35 | 0.75 | Documented: organic NRR 111% (deck p.22); TTM new ACV +75% (deck p.16). Drag: inorganic NRR below 100% in migration (deck p.22). Set equal to the grade-B bear weight on a 10% path | +34.01 | T2 | SI/consulting referrals; US MarTech budget; named large-customer renewals |
| L4 | Organic operating leverage: organic EBITDA margin toward 25% | +12.54 | 0.55 | Documented: non-COGS +32% vs revenue +43% (deck p.9). Inferred: organic EBITDA about 23% (dossier V5). FX flatters Q1. 25-30% steady state has no date | +6.90 | T2 | USD/INR |
| L3 | Revenue lifts from 10% to 15% a year FY28-FY30 (to Rs 1,620 Cr) | +26.05 | 0.45 | Documented: organic +17% Q1 (deck p.15). Against: 39.6% of revenue is acquired books, organic decelerated 83.7% / 35.5% / 15.5% (AR p.79), three readings of organic (09b C1.1). Holding 15% needs organic near 20%. MODERATE band, below its midpoint | +11.72 | T3 | SI/consulting referrals; US MarTech budget; USD/INR |
| L5 | Kognitiv migration completes, retained revenue at least 80% of FY26 (line B, consolidated) | +20.91 | 0.40 | Management: full by Sep-2027 (Q1 FY27 call). Inferred: Kognitiv revenue down 16-20% since purchase (tracker row 5). Timeline slipped 12-18 months to about 28 (20% promise discount). No external candidate, so evidence-thin and magnitude capped MODERATE | +8.36 | T3 | none (company filing events only) |
| L6 | SessionM reaches ARR at least USD 27 m and break-even by Q4 FY27, contribution margin at least 15% by Q4 FY28 (line B, consolidated) | +33.45 | 0.40 | Documented: "tracking to the planned $32M ARR" (deck p.14). ARR restated from USD 35 m to 32 m (09b C1.2). EUR 3.04 m fraud at SessionM Czech (Results p.11). Evidence-thin (no external candidate), magnitude capped MODERATE | +13.38 | T3 | none (company filing events only) |
| U1 | aiRA reaches 5% of revenue, above the base path | +15.00 | 0.15 | Management: under 10 paying of 26 live (dossier V7) | +2.25 | T3 | Enterprise gen-AI adoption (shared) |
| U2 | Bull path beyond base, excluding U1 (FY28 revenue at least Rs 1,320 Cr, margin to 25% by FY30) | +74.14 | 0.15 | Management: 20%+ organic and 25-30% steady state at face value. Needs the deceleration to reverse. LOW band | +11.12 | T3 | US MarTech budget; SI referrals |
| D1 | Optum warrant charge steps up to about Rs 31 Cr a year (contra revenue) | -8.00 | 0.90 | Documented per claude.ai: RHP pp.71-73 (not in corpus). FY30 schedule NOT FOUND, carried at the FY28-29 level | -7.20 | netted | Named large-customer renewals |
| D3 | Optum repriced by more than 20% or not renewed by Mar-2029 | -30.00 | 0.25 | Documented per claude.ai: Optum net revenue Rs 98.9 Cr FY25 (RHP); falsifier 2 | -7.50 | netted | Named large-customer renewals; tracker row 3 (UnitedHealth filings, external) |
| D4 | Below-EBITDA cost growth to the base path (D&A Rs 80.2 to 100 Cr with SessionM amortisation; ESOP Rs 14.8 to 17 Cr; finance Rs 4.7 to 5 Cr) | -16.80 | 0.90 | Documented: D&A Rs 20.04 Cr in Q1 with two months of SessionM (Results p.9); preliminary PPA (p.10 note 7). Management: ESOP Rs 12-15 Cr (B05) | -15.12 | netted | none |
| D5 | Adjusted EBITDA margin falls to the bear's 15%: compression beyond D1, (17.152% - 15.0%) x 1,358 x 0.75 - 8.0 | -13.92 | 0.20 | Kill trigger (draft T3); AI build-vs-buy price pressure (Chain 6). Section C margin FIRING at 0.70 | -2.78 | netted | Enterprise gen-AI adoption (shared) |

D2 (tax normalisation, -Rs 25 Cr) is not carried. The A21 base is already taxed at 25%, so crediting D2 would double count (deliberation C).

Ledger worksheet line: "Ledger: 12 items (T2 3, T3 5, downside 4) | prob-weighted T2 gross Rs 45.11 Cr, downside -Rs 32.60 Cr, T2 net Rs 12.51 Cr | T3 Rs 46.84 Cr | total Rs 59.34 Cr | items past confirm-by: 0 (all OPEN)." (section-1b chunk 09)

Consistency checks. All base rows firing: L1 + L2 + L3 + L4 + L5 + L6 - D1 - D4 = 4.94 + 45.35 + 26.05 + 12.54 + 20.91 + 33.45 - 8.00 - 16.80 = **118.44 = base FY30 PAT 175.80 - 57.36**. Bear rows (L2 on, L1/L3/L4/L5/L6 off, D1, D4, D5 on) give 45.35 - 8.00 - 16.80 - 13.92 = +6.6 against the bear's +3.9. The Rs 2.7 Cr gap is L2's sizing on the Rs 1,065 Cr guide base rather than the bear's Rs 1,020 Cr: 21.1 Cr of FY30 revenue x 17.152% x 0.75. The ledger spans bear to base, and U1 and U2 carry the bull side at their probabilities (Rule J symmetry). Probability-weighted credit of the base rows is Rs 56.25 Cr (47.5% of the base increment); beyond-base rows net +Rs 3.09 Cr.

Reconciliation to the deliberation's ledger (draft probabilities, FY29): T2 net Rs 18.4 Cr, T3 Rs 28.3 Cr, total Rs 46.7 Cr. Rebuilt: T2 net Rs 12.51 Cr, T3 Rs 46.84 Cr, total Rs 59.34 Cr. T2 falls because D4 (cost growth) is now carried. T3 rises because the base revenue lift (L3) and the bull side (U2) are now on the ledger.

The file outputs/expectation-ledger.md carries this ledger in the Appendix A schema.

### 5.6 Amendment 24: price decomposition at Rs 566.65 (governing 30x)

Tier multiple: the operator-approved 30x (the governing destination, A20.9). Step 1C cross-check: PENDING LIVE PEER TABLE. Pillar 16.8x is shown beside it. (section-1b chunk 08)

| Tier | Basis | Rs Cr | Rs / share | % of CMP |
|---|---|---|---|---|
| **T1 Confirmed** | A21 run-rate PAT Rs 57.36 Cr x 30 = Rs 1,720.8 Cr (Rs 208.83; 36.9%) plus net cash Rs 469.7 Cr (Rs 57.00; 10.1%) | 2,190.4 | 265.83 | **46.9%** |
| **T2 High-probability** | (45.11 - 32.60) = Rs 12.51 Cr x 30 | 375.2 | 45.54 | **8.0%** |
| **T3 Speculative** | Rs 46.84 Cr x 30 | 1,405.1 | 170.52 | **30.1%** |
| **Residual** | 566.65 - (265.83 + 45.54 + 170.52) | 698.4 | 84.76 | **15.0%** |
| Total (diluted market cap) | | 4,669.1 | 566.65 | 100% |

Verdict as four percentages: **T1 46.9% | T2 8.0% | T3 30.1% | residual 15.0%.** T1 + T2 = 54.9%. T3 is the explicit bet: almost one third of the price rides catalysts under 50% probability. The residual (15.0%) is below the 25% starter cap. Position size keys to T1 + T2.

Sensitivities: without U2 (bull row), T3 22.9% and residual 22.1%. On the deliberation's draft ledger: T1 46.9%, T2 11.8%, T3 18.2%, residual 23.1%. At the pillar 16.8x: T1 30.7% (Rs 173.95), T2 4.5%, T3 16.9%, residual **47.9%**.

Worksheet: "Decomposition at Rs 566.65: T1 46.9% | T2 8.0% | T3 30.1% | residual 15.0% | governing multiple: operator-approved 30x (pillar 16.8x cross-check; relative route not open, no live peer table)."

### 5.7 Amendment 25: fast-growth sizing state

Fast-growth: **YES**. A21 run-rate growth +42.7% YoY (Results Q1 FY27 p.9: 2,566.44 vs 1,798.93 mn), and the forward Revenue Transition is FIRING (OR-12). Margin of safety is position size, not a price haircut (OR-31). (section-1b chunk 08)

| Gate | Requirement | At Rs 566.65 | Price where it holds |
|---|---|---|---|
| Starter (Small, 2-3%) | T1 + T2 at least 75% of price, AND residual at most 25% | 54.9%: **FAILS**; residual 15.0%: passes | T1 + T2 = Rs 311.37, so **Rs 415.2** (311.37 / 0.75); residual there is negative |
| Add to Medium (4-6%) | T1 alone at least 60% of price, after the starter | 46.9% | Rs 443.1 (but the starter must come first, at Rs 415 or below) |
| Large (7-10%) | T1 at least 80%, Gate 0 EXCELLENT, promoter TRUSTWORTHY | 46.9%; Gate 0 AVERAGE | Not available |
| Dispersion cap | width above 80% caps at Small | 111.7% | Small binds |

Sizing state: **no starter at CMP.** The first gate opens at Rs 415 or below. The deliberation's Rs 444 used the draft ledger. Next add trigger: L3 (H1 FY27 constant-currency organic at least 15%, Nov-2026). If it confirms, L3 moves to T1 at the next A21 refresh. Trim ladder: 25% per decayed item; 50% if the residual passes 40% after a decay.

Worksheet: "Fast-growth: Y (basis: A21 run-rate +42.7% YoY; forward revenue FIRING, OR-12) | size: none at CMP; starter at Rs 415 or below; capped Small by dispersion | next add trigger: ledger L3."

### 5.8 Amendment 19: fair-value path, FV CAGR and return-source label

Governing destination: 30x P/E machinery (primary method). Base case. The forward basis rolls one year at each step. Net cash is held at the anchor. Option slices carry zero (O8). (section-1b chunk 12)

| Point | Forward EPS used | FV = 30 x EPS + Rs 57 |
|---|---|---|
| Today (Oct-2026) | A21 run-rate Rs 6.961 | **Rs 265.8** |
| End-Year-1 (end-FY27) | FY28 Rs 10.058 | Rs 358.7 |
| End-Year-2 (end-FY28) | FY29 Rs 14.981 | Rs 506.4 |
| End-Year-3 (end-FY29, exit) | FY30 Rs 21.335 | **Rs 697.1** |

FV CAGR over the hold: **37.9%** (today Rs 265.8 to end-Year-3 Rs 697.1, governing 30x, base case) = (697.1 / 265.8)^(1/3) - 1. Bear FV CAGR 1.8% (Rs 265.8 to Rs 280.1). Bull 56.6% (to Rs 1,021.6). On the triangulated end-point (Rs 640.1) the FV CAGR is 34.0%.

Return-source label: **COMPOUNDER** (FV CAGR at or above 20%).

Decomposition line: fair value compounds because operating EPS rises 3.06x at a constant 30x. No re-rating lever remains: the multiple is held at the destination, and the recognition gap is closed. The static share is net cash: Rs 57 is 21.4% of today's FV and 8.2% of the end-FY29 FV. 0% of fair value is non-compounding option value (O8). The fade schedule is not applied (approved base; A14 flag, -Rs 50 at exit). The label says where the return would come from. It does not rescue the price: CMP (Rs 566.65) is 2.13x today's FV and sits above the end-FY28 FV (Rs 506.4). On the base path, FV reaches CMP around Jul-2028, so the price is about 1.75 years ahead of value.

FV-step lines (19.4): none. No separate within-hold slice exists under O8. Tracking equivalents at 30x through consolidated EPS: L6 SessionM fires +Rs 121.8 per share (33.45 x 30 / 8.24); L5 Kognitiv +Rs 76.1; D3 Optum fires -Rs 109.2.

### 5.9 4E Entry price

| Calculation | Weighted FV (Master 4A, governs 4E) | P/E at 30x only (confirms dossier 6.6) |
|---|---|---|
| Base fair value (Year 3) | Rs 640.1 | Rs 697.1 |
| Tier A hurdle price = FV / 1.25^3 (A4.3, A18.5, OR-8) | **Rs 327.7** | Rs 356.9 |
| FV CAGR and return-source label (A19) | 37.9% COMPOUNDER (governing 30x machinery) | same |
| Price for 30% CAGR = FV / 1.30^3 | **Rs 291.4** | Rs 317.3 |
| Margin of safety price (reference only; A25 governs fast-growth names): mixed evidence, 30% | Rs 229.4 | Rs 249.8 |
| Ideal entry range | **Rs 291 to Rs 328** | Rs 317 to Rs 357 |

Bear and bull hurdle prices (P/E at 30x): Rs 143.4 and Rs 523.1 (dossier 6.6 confirmed: about Rs 143 and Rs 524). A25 starter gate: Rs 415. CMP is 72.9% above the top of the entry range (Rs 327.7) and 58.8% above the 30x-only hurdle price. Buy at the bottom of the revealed band, never the top. (section-1b chunk 06)

### 5.10 4F Risk-reward asymmetry

| | Value |
|---|---|
| Bull target (Year 3) | Rs 974.2: upside +71.9% |
| Base target (Year 3) | Rs 640.1: upside +13.0% |
| Bear floor (Year 3) | Rs 259.2: downside -54.3% |
| Upside (base) / downside (bear) | **0.24x** (needs 2x or more). P/E at 30x only: 23.0% / 50.6% = 0.45x |

### 5.11 4G Four-pillar exit multiple validation

| Check | Result | Pass? |
|---|---|---|
| Year 3 ROCE justifies the ROCE base and matches the FTTCP verdict? | Base FY29E 23.2% [INFERENCE] is above the 10.9% blend; consistent with RECOVERING. Bear about 10% does not | PASS (base) |
| Year 3 CFO/PAT justifies the cash multiplier? | Projected 1.9x supports 1.15x; history volatile (57% two-year CFO / adj. EBITDA) | PASS WITH FLAG |
| Primary catalyst fired by Year 3 in the base case? | Proof gate (Nov-2026) and Kognitiv migration (Sep-2027) both inside the hold | PASS |
| Strategic premium still justified, single credit respected? | +0x; recovery in Pillar 1 only | PASS |
| UA ordering min(F x 1.25, cap)? | UA not applied | PASS |
| Would you buy a different stock at this exit PE with similar Year 3 metrics? | Year 3 metrics: ROCE about 23%, growth fading toward industry 12%, cash 1.15x, EM MODEST. A fresh pillar build on them gives 0.5 x 23.2 + 7.5 = 19.1; x 1.15 = 22.0; + 2 = **about 24x**. 30x is 25% above that. At 24x the base end-FY29 value is Rs 569 (0.1% CAGR) | **FAIL at 30x** |

Master 4G says: "If any check fails, revise the exit PE downward and recalculate." The operator ruling (O5) binds under A20.9, so stage 11 does not revise. The failure is reported here and in the flags for the operator's final review.

### 5.12 4H-pre Mandatory conclusion elements

1. **Value vs price.**
   - Line one: the weighted fair value at end-FY29 is Rs 640, or Rs 697 on P/E alone at the operator's 30x. The single driver is FY30 operating EPS of Rs 21.3, a 3.1x climb from the Rs 6.96 run-rate, led by margin migration of the acquired books.
   - Line two: at Rs 566.65, a 30x exit needs FY30 EPS of Rs 26.5 just to earn the 14.5% cost of equity. That is the bull revenue path at the base margin. Flag: **PRICED-WE-ARE-LATE**. The gap closes three ways: the price falls toward Rs 415 (A25 starter) or Rs 328 (25% entry); or a live adjusted peer base comes in at 30x or more AND the proof gate fires on the Q2 FY27 print (about Nov-2026).
2. **Margin of safety.** Fast-growth name, so A25 governs: margin of safety is position size. The evidence-scaled reference row is 30% (mixed evidence: 18 documented, 14 claim, 2 inference, B07), MoS price Rs 229.4, shown for reference only.
3. **Dispersion sizing.** Width = (974.2 - 259.2) / 640.1 = **111.7%**, above 80%, so the position is **capped at Small** regardless of conviction (106.4% on P/E at 30x only).
4. **Edge claimed: PROCESS**, because the pipeline read the Q1 FY27 deck and results notes and found two facts. First, acquired books are 39.6% of revenue (deck p.15 by arithmetic) and, by the company's own words, run below 100% NRR while migrating (deck p.22). Second, the base case's 15% consolidated growth therefore needs organic growth near 20%, which has not yet printed.

### 5.13 4H Final valuation verdict card

```
Tier: A | Hurdle: 25%
CAPILLARY | CMP Rs 566.65 (NSE 09-Oct-2026) | Market cap Rs 4,669.2 Cr diluted (Rs 4,503.3 Cr basic)
CONVERTER: NON-CONVERTER (A17.0; operator Part 1)

FOUR-PILLAR EXIT PE (Track 2, re-derived; cross-check to the approved base)
  ROCE base: FTTCP RECOVERING (p ~0.65) -> Pillar 1 ROCE 10.90% (60/40 of TTM 6.84% and FY28E 16.99%), Route A -> 12.9x
  Cash mult: 1.15x (operator O4; GROWTH-INDUCED, O3) [chunk 02 band reading 1.00x]
  Quality base: 14.8x | Growth prem: +2x (3a; EM 24; catalyst 0-6 m; mixed evidence; A16 eligible FY28)
  Strategic: +0x (recovery credited in Pillar 1) | Raw PE: 16.8x | UA applied: N | Sector cap: 45x (uplift N; override N)
  DESTINATION PE (pillar): 15.5x - 18.0x (H 16.8x; record 16.9x)
RRM TRACK: r 14.5% | RRM 0.88 | destination 13.1x (12.0x - 14.0x) | divergence 22.5%
GOVERNING EXIT PE: 30x on BOTH tracks, operator override O5 (A20.9), forward basis (O6), range 28.0x - 32.5x
  30x = +78.6% vs Track 2, +129.0% vs Track 1; DCF implies 16.7x; Year-3-metric pillar ~24x; 4G check 6 FAILS
STEP 1C: pillar 16.8x | adjusted peer base PENDING LIVE PEER TABLE | relative route opens above 24.0x | 30x needs a base >= 30x | governing: operator-approved 30x
RECOGNITION GAP: CLOSED (run-rate P/E 81.4x vs TO rung R3 ~19x / R4 ~21x). Re-rating engine negative (81.4x -> 30x). Return rides EPS CAGR alone.
HURDLE RATIO: 0.75 on the probability-weighted ledger EPS (base scenario 1.13; bull 1.70, usable at grade B) vs 1.953 -> STOP band (caps no verdict, OR-2)
METHODS: P/E at 30x 80% (Rs 280 / 697 / 1,022) | DCF 20% (Rs 175.5 / 412.5 / 784.8) | EV/EBITDA, EV/ARR, P/B, SOTP not applied
WEIGHTED FAIR VALUE (Year 3, end-FY29), Track 1 = Track 2 at 30x: Bear Rs 259.2 | Base Rs 640.1 | Bull Rs 974.2
  Pillar cross-check (P/E only): Track 2 16.8x Rs 182 / 415 / 597 | Track 1 13.1x Rs 154 / 336 / 478
EXPECTED CAGR (grade B -> Good 25/50/25, Rule E, trailing 3 listed quarters): 1.3% (P/E at 30x only: 3.8%; Excellent sensitivity 3.4% / 5.9%; ledger basis -5.3%)
UPSIDE / DOWNSIDE: 0.24x (needs >= 2x)
ENTRY: ideal range Rs 291 - Rs 328 (25% Tier A hurdle Rs 327.7; 30% Rs 291.4) | 30x P/E only: Rs 357 | A25 starter gate Rs 415
MARGIN OF SAFETY PRICE: Rs 229.4 (reference; 30% mixed-evidence row) -> A25 governs: margin of safety = position size
FV CAGR: 37.9% COMPOUNDER (today Rs 265.8 -> end-FY29 Rs 697.1 at 30x). Price is ~1.75 years ahead of base FV.
PRICE DECOMPOSITION at Rs 566.65 (30x): T1 46.9% | T2 8.0% | T3 30.1% | residual 15.0% (at pillar 16.8x: residual 47.9%)
A25: fast-growth Y; starter FAILS at CMP (T1+T2 54.9% < 75%); starter at Rs 415 or below
VALUE VS PRICE: worth Rs 640 weighted / Rs 697 at 30x on FY30 EPS Rs 21.3 | price needs FY30 EPS Rs 26.5 at 30x to earn 14.5% -> PRICED-WE-ARE-LATE; closes on price toward Rs 415 / Rs 328, or a live peer base >= 30x plus a fired proof gate (Q2 FY27, ~Nov-2026)
DISPERSION SIZING: (Bull - Bear) / Base = 111.7% -> Small
EDGE CLAIMED: process (acquired books 39.6% of revenue run sub-100% NRR in migration; base 15% needs ~20% organic)
DECISION: WATCHLIST (no position at Rs 566.65, on valuation). Bands: A25 starter <= Rs 415 | 25% entry <= Rs 328 (Rs 357 at 30x only) | 30% entry <= Rs 291
```

Key assumptions that could change the valuation:
- ▲ A live adjusted peer base at 30x or more. Section 1B would then support 30x through A20.5 (bounded by the 45x cap) instead of an override.
- ▲ The proof gate fires on Q2 FY27: constant-currency organic growth of at least 15% and operating ROCE above 10%. L3 would move from 0.45 toward 0.60 and into T2: +Rs 57 per share to T2 and -Rs 43 from T3. T1 + T2 would then be about 65% of CMP, still short of the 75% starter gate.
- ▲ The SessionM margin ramp beats break-even in year one: L6 is worth Rs 122 per share at 30x.
- ▲ The tax-loss shelter is valued in the bridge (NOT FOUND today). claude.ai's unanchored Rs 35-45 Cr would add about Rs 4-5 per share.
- ▼ The operator re-rules the exit to the pillar 16.8x: base Rs 415 (-9.8% CAGR) and residual 47.9%.
- ▼ The A14 fade applies (growth to 12% by Year 3): -Rs 50 per share at 30x.
- ▼ Acquired books attrite (inorganic NRR below 100%): L3 fails and consolidated growth settles near 10%.
- ▼ Optum is repriced or not renewed (D3): -Rs 109 per share at 30x.
- ▼ A new acquisition resets invested capital and goodwill: the FY28E ROCE endpoint falls, so Pillar 1 and the A16 crossover move.
- ▼ The bridge is re-ruled to 30-Jun-2026: -Rs 5.5 on every value.

Exit framework:
- Target exit: end-FY29, at the weighted base Rs 640 (Rs 697 at 30x).
- Thesis-broken conditions: falsifiers 1-5 (dossier Section 4). These are core NRR ex Optum below 105% for two quarters; Optum repriced or not renewed; SessionM below USD 27 m ARR or still at break-even by Q4 FY27; organic EBITDA margin falling in constant currency; and a KPMG finding of insider involvement.
- Time stop: both halves of the proof gate (cc organic growth at least 15%; operating ROCE above 10% for two consecutive quarters) not fired by Q2 FY28 (Nov-2027).
- PE compression floor: bear EPS at 30x Rs 280; at the pillar 16.8x Rs 182.

One-line thesis: "Not buying CAPILLARY at Rs 566.65. EPS can grow from Rs 6.96 to Rs 21.33 by FY30 on acquired-book margin migration and about 15% revenue compounding. But at a four-pillar destination PE of 16.8x (ROCE 10.9%, cash 1.15x, EM 24, sector cap 45x) the target is Rs 415 (-9.8% CAGR). Even at the operator-approved 30x it is Rs 697 (7.2% CAGR); weighted with the DCF it is Rs 640 (4.1%). Key risk: the 30x exit itself, since Section 1B and the DCF both land near 17x, plus acquired-book attrition. Cash quality: growth-induced."

**Valuation complete.** Four-pillar exit PE of 15.5x to 18.0x (operator-approved 30x governs). Hurdle Ratio STOP. Entry price: Rs 291 to Rs 328. Decision: WATCHLIST.

---

## 6. UNRESOLVED INPUTS USED (override 3)

1. INPUT UNRESOLVED: net cash at the Q1 FY27 balance sheet date (B10.unresolved). Assumption used: Rs 57.00 per share (Rs 469.7 Cr on 8.24 Cr), because the operator approved it (O7) and asked stage 11 to anchor its date.
   - Bridge date anchored: **31-Mar-2026**. Deck May-2026 p.59: "Total cash & bank Rs 5,069.9 Mn, 31 March 2026 (incl. IPO proceeds)" = Rs 506.99 Cr.
   - Most likely reconstruction [INFERENCE]: Rs 506.99 Cr less borrowings Rs 44.72 Cr and lease liabilities Rs 8.89 Cr (Results Q4 FY26 p.15: 447.21 + 40.34 + 48.52 mn) = Rs 453.38 Cr, divided by 7.9472 Cr BASIC shares = Rs 57.05.
   - Readings per diluted share:
     - (a) approved Rs 57.00.
     - (b) 31-Mar-2026, ex lease: Rs 56.10.
     - (c) 31-Mar-2026, incl. lease: Rs 55.02.
     - (d) 31-Mar-2026 audited current cash items less borrowings: Rs 53.27. This is Rs 438.95 Cr, which excludes about Rs 23.3 Cr of non-current deposits (inferred by difference to the deck's Rs 506.99 Cr).
     - (e) **30-Jun-2026** gross cash, bank deposits and short-term investments Rs 469.0 Cr (capital employed less invested capital, Q1 FY27 deck p.26) less the last filed borrowings Rs 44.72 Cr = Rs 424.3 Cr = **Rs 51.50**.
   - Two Q1 FY27 events used cash after the anchor date: the SessionM cash consideration of Rs 16.91 Cr net of debt-like items (deck p.14), and the fraud remittances of Rs 33.39 Cr, of which Rs 4.67 Cr is frozen (Results Q1 FY27 p.11). B10's "USD 20m" SessionM payment note is not supported by the filed Rs 169.1 mn.
   - Separating observation: the H1 FY27 consolidated balance sheet (Q2 FY27 results, about Nov-2026). The spread is Rs 51.5 to 57.0, Rs 5.5 per share (1.0% of CMP). It moves every value by the same rupee amount and changes no verdict.
2. INPUT UNRESOLVED: peer medians and the adjusted peer base. Assumption used: none; Step 1C is PENDING and the approved 30x governs (A20.9). Both readings: adjusted peer base at 30x or more (Section 1B supports 30x) / below 24.0x (the pillar 16.8x would govern on Section 1B alone). Separating observation: the live peer table from Claude web, confirm-by /finalize.
3. INPUT UNRESOLVED: tax-loss shelter value (O7 places it in the bridge). Assumption used: Rs 0, because NOT FOUND in corpus. Both readings: Rs 0 / claude.ai INFERENCE Rs 35-45 Cr (RHP p.439, not held), about Rs 4.2-5.5 per share. Filed loss pools: Rs 92.16 Cr (AR p.158) and Singapore Rs 47.76 Cr (AR p.236). Separating observation: FY27 AR tax note, confirm-by Jul-2027.
4. INPUT UNRESOLVED: FY30 Optum warrant charge schedule. Assumption used: the FY28-29 step-up level carried (D1 -Rs 8 Cr). Both readings: charge ends after FY29 (about +Rs 20.6 Cr revenue vs run-rate if renewed at the same gross price) / charge persists at about Rs 31 Cr under a renewal with new warrants. Separating observation: Optum renewal terms, confirm-by Mar-2029.
5. INPUT UNRESOLVED: invested capital FY29-FY30 (2D ROCE only). Assumption used: +Rs 52 Cr a year [INFERENCE]. Both readings: no new M&A (operating ROCE 23-31%) / a new deal resets invested capital higher (ROCE lower). Separating observation: FY27 AR invested capital, confirm-by Jul-2027.
6. FTTCP B7 Year-3 net debt: NOT FOUND (depends on M&A). Net cash held at the anchored figure (A19.0).

## 7. INPUT GAPS AND FLAGS

Input gaps:
- Debt Capacity block not run.
- Market-Implied block not run (stage 11 computed its own).
- Live peer table pending.
- Borrowings at 30-Jun-2026 NOT FOUND.
- Tax shelter value NOT FOUND.
- FY30 Optum warrant schedule NOT FOUND.
- B7 Year-3 net debt NOT FOUND.
- Invested capital FY29-FY30 NOT FOUND.
- Year 5 not in the approved scenarios.
- FY26 top-10 concentration NOT FOUND.

Flags (all carried to the YAML):
- FLAG-EXITPE-OVERRIDE.
- FLAG-RECOGNITION-GAP (CLOSED; matrix cell PRICED NARRATIVE).
- FLAG-HURDLE (STOP).
- FLAG-A25 (starter fails at CMP).
- FLAG-DISPERSION (Small).
- FLAG-C2-PROBABILITIES (ruled by stage 11, not the operator).
- FLAG-CASH (1.15x operator vs 1.00x band).
- FLAG-A14-FADE.
- FLAG-METHODS (69% spread).
- FLAG-BRIDGE.
- FLAG-MACRO-STALE.
- FLAG-PROOF-GATE.
- FLAG-CROSSGRADE.
- FLAG-MULTI-RUNG.

Chunk-versus-source disagreements found: none. No frameworks/ source file was opened beyond the Master Role 1 sections. The Master's own 4G instruction ("revise the exit PE downward") conflicts with the operator-approved base. The wrapper and A20.9 resolve that conflict in favour of the approved base, and the conflict is reported above.

---

## 8. YAML

```yaml
stage: B11-valuation
company: "CAPILLARY"
run_date: "2026-09-19"
model: "claude-opus-5-5"
status: complete
entity: "consolidated single-entity"
entity_count: 1
input_gaps:
  - "Debt Capacity output block not run (consumed input NOT FOUND); company is net cash (borrowings Rs 44.72 Cr vs cash Rs 506.99 Cr at 31-Mar-2026), so capacity does not bind"
  - "Market-Implied Assumptions block not run in claude.ai (consumed input NOT FOUND); stage 11 computed its own reverse-engineered growth for the recognition-gap resolution"
  - "Step 1C live peer table PENDING LIVE PEER TABLE: only RateGain trailing P/E 41.8x held; no adjusted peer base"
  - "Borrowings at 30-Jun-2026 NOT FOUND (no Q1 FY27 balance sheet); bridge carried at the approved Rs 57 (31-Mar-2026 anchor)"
  - "Tax-loss shelter value NOT FOUND in corpus; O7 places it in the equity bridge but the Rs 57 bridge is net cash only; shelter carried at zero"
  - "FY30 Optum warrant charge schedule NOT FOUND (RHP not in corpus); ledger D1 carried at the FY28-29 step-up level"
  - "FTTCP B7 Year-3 net debt NOT FOUND (depends on M&A); net cash held at the anchored figure (A19.0)"
  - "Invested capital FY29-FY30 NOT FOUND; operating ROCE FY29E 23.2% and FY30E 30.5% in 2D are stage 11 [INFERENCE]"
  - "Year 5 (FY31) not in the approved scenarios; the DCF uses a named FY31 extension (A14 industry growth 12%, B09)"
  - "FY26 top-10 customer concentration NOT FOUND"
flags:
  - "FLAG-EXITPE-OVERRIDE: valued on operator-approved 30x both tracks (O5, A20.9). Re-derived pillar Track 2 16.8x (15.5-18.0x; record 16.9x, rounding of row C), Track 1 13.1x (r 14.5%, RRM 0.88). 30x is +78.6% vs Track 2 and +129.0% vs Track 1; DCF implies 16.7x on FY30 EPS; a Year-3-metric pillar gives about 24x; 30x needs a Pillar 1 ROCE of about 34% at 1.15x and +2x. Master 4G check 6 FAILS and says revise down; operator ruling binds; divergence reported, no other multiple substituted"
  - "FLAG-RECOGNITION-GAP: CLOSED. Run-rate operating P/E 81.4x vs TO rung R3 (about 19x) and ambition R4 (about 21x). Re-rating engine negative (81.4x to a 30x exit, -63%); return rides EPS CAGR alone. With proof NOT FIRED and ARTIFACT-OF-CLIMB the Transition Decision Matrix cell is PRICED NARRATIVE (TRAP), not the RESEARCH / WATCH (gap OPEN) carried before resolution; stage 13 applies the matrix"
  - "FLAG-HURDLE: STOP band vs Tier A 1.953. HR on the probability-weighted ledger EPS (A21 base) 0.75; base scenario 1.13; bull 1.70 (bull usable, grade B, O9); bear 0.39. Caps nothing (OR-2)"
  - "FLAG-A25: fast-growth Y (A21 run-rate +42.7% YoY; forward revenue FIRING, OR-12). Starter FAILS at CMP: T1+T2 54.9% of CMP vs 75% needed; starter price Rs 415.2 (deliberation's Rs 444 used the draft ledger). Residual 15.0%, under the 25% cap"
  - "FLAG-DISPERSION: (bull - bear) / base = 111.7% on the weighted FV (106.4% on 30x P/E only) > 80%: position capped at Small"
  - "FLAG-C2-PROBABILITIES: C.2 replaced. Ledger rebuilt to FY30 (exit-basis symmetry) with all Rs 118.44 Cr of base-case PAT growth on rows; probabilities ruled by stage 11 with stated evidence, NOT operator-ruled; operator to ratify or replace at /finalize"
  - "FLAG-CASH: carried. Determination GROWTH-INDUCED (operator O3); multiplier applied 1.15x (operator O4). Chunk 02 band reading on filed CFO/PAT is 1.00x (volatile: FY25 CFO negative, FY26 2.86x). Phase 1 INDETERMINATE cap superseded by O3"
  - "FLAG-A14-FADE: approved base holds about 15% growth through Year 4; EM MODEST fades to industry growth (12%, B09) by Year 3. A14-faded FY30 EPS Rs 19.67, value at 30x Rs 647 (-Rs 50). Valued on the approved scenarios (O11)"
  - "FLAG-METHODS: P/E at 30x (base Rs 697.1) and DCF (base Rs 412.5) diverge 69%; the DCF agrees with the pillar destination, not with 30x"
  - "FLAG-BRIDGE: approved Rs 57 anchors to 31-Mar-2026 (deck May-2026 p.59), pre-SessionM close and pre-fraud, and reconstructs on the basic share count; latest-dated reading (30-Jun-2026, diluted) Rs 51.5; re-ruling moves every value -Rs 5.5; no verdict changes"
  - "FLAG-MACRO-STALE: macro-sheet.md is the August 2026 fill (next refresh 1-Sep-2026), stale on 10-Oct-2026; Nifty PE 20.5x, market CoE 14.1% and terminal cap 6.0% used with that flag"
  - "FLAG-PROOF-GATE: NOT FIRED; both halves read on Q2 FY27 results (about Nov-2026)"
  - "FLAG-CROSSGRADE: cross-family grade did not run (no GEMINI_API_KEY); FTTCP confidence one notch lower"
  - "FLAG-MULTI-RUNG: 30x sits above the R5 neighbourhood (about 24x); FROM R1-R2 to an R5-level multiple inside 3 years is a multi-rung leap (CLAUDE.md red flag)"
framework_versions: "Master v3.7 / Section 1B v3.3+v3.5.1+v3.6+v3.7+v3.8+v3.9+v3.10 / FTTCP v2.3"
pe_basis: "forward"
exit_pe_base_approved: "30x on both tracks (operator override O5 at the P/E gate, 10-Oct-2026), applied to one-year-forward operating EPS; exit end-FY29 on FY30 EPS (O6). Range +/-7.5%: 28.0x-32.5x. Sector cap 45x"
destination_pe:
  track1_rrm: {low: 12.0, mid: 13.1, high: 14.0, r_used: 14.5, rrm: 0.88}
  track2_additive: {low: 15.5, mid: 16.8, high: 18.0}
  divergence_pct: 22.5
  governing_track: "Neither pillar track: the operator-approved 30x governs both tracks (O5, A20.9), so Track 1 and Track 2 fair values coincide; pillar tracks are cross-checks and OR-1 is moot for the entry zone"
pillar_detail:
  roce_used: 10.9
  roce_base: 12.9
  roce_recovery_route: "pillar1-midpoint (Pillar 1 route; RECOVERING 40-60% row, 60/40 blend of TTM 6.84% and FY28E 16.99%)"
  pillar1_normalization_route: "A-operational"
  cash_multiplier: 1.15
  structural_or_growth: "growth-induced"
  growth_offset: 0
  growth_premium: 2
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 45
hurdle_ratio: {base: 0.75, bull_used: true, verdict: "STOP"}
run_rate_base:
  basis: "single-quarter-annualised"
  pat_run_rate_cr: 57.36
  one_offs_adjusted: "Q1 FY27 (deck p.28; Results Q1 FY27 p.9): exceptional cyber-fraud loss Rs 33.39 Cr stripped; finance income, asset disposal, fair value and FX gains Rs 5.68 Cr a quarter stripped (depleting IPO cash pile); tax normalised to 25% (printed tax includes a one-time DTL Rs 1.61 Cr on a sheltered base; shelter belongs in the bridge, O7). Operating PBT Rs 19.12 Cr a quarter x 4 x 0.75 = Rs 57.36 Cr; EPS Rs 6.961 on 8.24 Cr; run-rate P/E 81.4x. Not adjusted, named: SessionM in Q1 for 2 of 3 months (PAT-neutral at break-even); FX about 6 points of growth"
  annual_model_divergence_pct: 77.6
price_decomposition:
  t1_confirmed: {rs_cr: 2190.4, rs_per_share: 265.83, pct_cmp: 46.9}
  t2_high_prob: {rs_cr: 375.2, rs_per_share: 45.54, pct_cmp: 8.0}
  t3_speculative: {rs_cr: 1405.1, rs_per_share: 170.52, pct_cmp: 30.1}
  residual: {rs_cr: 698.4, rs_per_share: 84.76, pct_cmp: 15.0}
  step1c_peer_base_crosscheck: "PENDING LIVE PEER TABLE. Pillar destination 16.8x; adjusted peer base not buildable from held data (RateGain trailing 41.8x only); relative route opens above 24.0x; Section 1B reaches 30x only at an adjusted peer base of 30x or more; pillar sits 44.0% below the approved 30x. At the pillar 16.8x the residual would be 47.9%"
  governing_multiple: "operator-approved 30x (A20.9) in the pillar slot; pillar 16.8x is the cross-check; relative route not open (no live peer table)"
fair_values:
  track1: {bear: 259.2, base: 640.1, bull: 974.2}
  track2: {bear: 259.2, base: 640.1, bull: 974.2}
expected_cagr_prob_weighted: 1.3
entry_range: {low: 291.4, high: 327.7}
mos_price: 229.4
upside_downside_ratio: 0.24
decision: "WATCHLIST: no position at Rs 566.65 (on valuation; base CAGR 4.1% weighted, 7.2% at 30x P/E only). Bands: A25 starter <= Rs 415; 25% entry <= Rs 328 (Rs 357 at 30x P/E only); 30% entry <= Rs 291"
unresolved_inputs_used:
  - "INPUT UNRESOLVED: net cash at the Q1 FY27 balance sheet date. Assumption used: Rs 57.00/share (Rs 469.7 Cr), because operator-approved (O7); date anchored 31-Mar-2026 (deck May-2026 p.59, Rs 506.99 Cr less borrowings Rs 44.72 Cr and leases Rs 8.89 Cr = Rs 453.38 Cr over 7.947 Cr basic shares = Rs 57.05 [INFERENCE reconstruction]). Both readings: 31-Mar-2026 Rs 57.0 / 30-Jun-2026 Rs 51.5 (Rs 469.0 Cr gross cash, Q1 FY27 deck p.26, less last filed borrowings, on 8.24 Cr). Separating observation: H1 FY27 consolidated balance sheet, confirm-by Nov-2026"
  - "INPUT UNRESOLVED: peer medians / adjusted peer base. Assumption used: none; Step 1C PENDING; approved 30x governs (A20.9). Both readings: adjusted base >= 30x (Section 1B supports 30x) / < 24.0x (pillar 16.8x would govern). Separating observation: live peer table from Claude web, confirm-by /finalize"
  - "INPUT UNRESOLVED: tax-loss shelter value. Assumption used: Rs 0 (NOT FOUND in corpus). Both readings: Rs 0 / claude.ai INFERENCE Rs 35-45 Cr (about Rs 4.2-5.5/share). Separating observation: FY27 AR tax note, confirm-by Jul-2027"
  - "INPUT UNRESOLVED: FY30 Optum warrant charge. Assumption used: FY28-29 step-up level carried (D1 -Rs 8 Cr PAT). Both readings: charge ends after FY29 / persists at about Rs 31 Cr on renewal. Separating observation: Optum renewal terms, confirm-by Mar-2029"
  - "INPUT UNRESOLVED: invested capital FY29-FY30 (2D ROCE only). Assumption used: +Rs 52 Cr a year [INFERENCE]. Both readings: no new M&A (ROCE 23-31%) / new deal resets IC higher. Separating observation: FY27 AR invested capital, confirm-by Jul-2027"
som_cagr_crosscheck: "justified excess: base FY26-FY29 revenue CAGR 24.3% vs SOM-implied 22.8% (FY29 Rs 1,410 Cr vs SOM Rs 1,361 Cr, +3.6%); the excess is the closed SessionM acquisition (B09: +37.2% one-off step its SOM math does not underwrite); FY28-FY30 base growth of 15% sits below SOM 22.8% (3yr) / 21.1% (5yr)"
one_line_thesis: "Not buying CAPILLARY at Rs 566.65: EPS can grow from Rs 6.96 to Rs 21.33 by FY30 on acquired-book margin migration and about 15% revenue compounding, but at the four-pillar destination of 16.8x (ROCE 10.9%, cash 1.15x, EM 24, sector cap 45x) that is Rs 415 (-9.8% CAGR), and even at the operator-approved 30x it is Rs 697 (7.2%; Rs 640 and 4.1% weighted with the DCF). Key risk: the 30x exit itself, since Section 1B and the DCF both land near 17x, plus acquired-book attrition. Cash quality: growth-induced."
```
